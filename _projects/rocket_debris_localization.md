---
layout: han-project
title: "Multi-Object Localization of Rocket Debris"
description: "A mathematical modeling study linking WGS84 ellipsoidal geodesy, four-sphere intersection, combinatorial traversal, and Monte Carlo sensitivity analysis."
permalink: /projects/rocket_debris_localization/
img: assets/img/projects/rocket/rocket_cover.png
importance: 2
category: research
discipline: "Applied mathematics"
period: "2024"
question: "How can asynchronous vibration arrivals locate multiple supersonic debris pieces and separate overlapping shock waves?"
role: "Sole author — mathematical modeling, algorithm design, numerical solution, and manuscript"
methods: "WGS84 ellipsoidal transformation, Four-Sphere intersection, nonlinear least squares (lsqnonlin), traversal exclusion algorithm, Monte Carlo simulation"
outcome: "Journal article · Front. Prog. Comput. Math. Model. · Dec. 2024, Vol. 5, No. 1, pp. 1–24"
card_summary: "A numerical study of seven monitoring stations and four sound sources, combining WGS84 geodesy, 4-sphere intersection, combinatorial traversal, and Monte Carlo error analysis."
image_alt: "Multi-object localization of rocket debris"
publication: true
contents:
  - label: Abstract
    id: abstract
  - label: Model design
    id: method
  - label: Selected results
    id: findings
  - label: Discussion
    id: discussion
---

<h2 id="abstract">Abstract</h2>

During multistage rocket ascent and orbital insertion, spent rocket stages and booster casings separate and fall back toward Earth. As this debris plunges through the atmosphere at supersonic speeds, transonic shock waves generate intense sonic booms that propagate outward as atmospheric vibration waves. Deploying ground monitoring stations to capture these arrival times offers a viable pathway for rapid debris localization and recovery.

However, field monitoring encounters two fundamental mathematical challenges:
1. **Coupled spatial-temporal unknowns:** Both the 3D position $(x, y, z)$ and the exact sonic boom initiation time $t_0$ are unknown, requiring simultaneous estimation of four state variables per source.
2. **Combinatorial signal association ambiguity:** When multiple debris pieces fall simultaneously, ground sensors record multiple arrival timestamps without source identifiers, creating an overlapping multi-signal assignment problem.

This study formulates an end-to-end mathematical modeling framework: converting geodetic coordinates to geocentric Cartesian coordinates under the WGS84 reference ellipsoid, establishing the **Four-Sphere Intersection** positioning model, designing a **Traversal Exclusion Algorithm** that filters $4^4 = 256$ candidate timestamp permutations down to 73 feasible candidates and isolates four distinct sources, and evaluating error propagation through **Weighted Least Squares** and **Monte Carlo** simulations under $0.5\text{ s}$ measurement noise.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>Spatial localization and signal association cannot be treated separately. A valid model must couple nonlinear geometric sphere intersection with multi-tiered combinatorial screening to resolve both spatial coordinates and arrival-wave identities simultaneously.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Four-sphere intersection diagram">
    <img src="{{ '/assets/img/projects/rocket/four_sphere_model.png' | relative_url }}" alt="Four-sphere intersection geometric positioning model" loading="lazy" width="1000" height="580">
  </div>
  <figcaption><span>Figure 1.</span> Geometric schematic of the Four-Sphere Intersection Model. While three spheres intersect along a circle or at two conjugate points, a fourth non-coplanar sphere breaks the degeneracy and determines a unique physical coordinate and initiation time.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### Geodetic coordinate transformation under WGS84

Because monitoring devices are deployed across a regional scale exceeding 100 km, planar flat-Earth approximations introduce unacceptable geometric distortion. The Earth's surface is modeled as an oblate ellipsoid using the standard **WGS84** reference system, with semi-major axis $a = 6{,}378{,}137\text{ m}$ and first eccentricity squared $e^2 = 0.00669437999014$.

For each monitoring station situated at longitude $\lambda$, latitude $\phi$, and ellipsoidal altitude $h$, its coordinates are transformed into a geocentric Earth-Centered Earth-Fixed (ECEF) Cartesian coordinate system:

<div class="hy-equation" role="math" aria-label="WGS84 coordinate transformation equations">
  \begin{cases}
    X = (N + h) \cos \phi \cos \lambda \\
    Y = (N + h) \cos \phi \sin \lambda \\
    Z = \left[ N(1 - e^2) + h \right] \sin \phi
  \end{cases}
</div>

where $N(\phi)$ represents the prime vertical radius of curvature:

<div class="hy-equation" role="math" aria-label="Prime vertical radius equation">
  N(\phi) = \frac{a}{\sqrt{1 - e^2 \sin^2 \phi}}
</div>

The seven monitoring stations (designated A through G) provide the ground spatial framework for all subsequent localization tasks.

<div class="table-responsive">
  <table class="table table-sm table-striped">
    <thead>
      <tr>
        <th scope="col">Device</th>
        <th scope="col">Longitude (°E)</th>
        <th scope="col">Latitude (°N)</th>
        <th scope="col">Altitude (m)</th>
        <th scope="col">Single-Debris Arrival $t_i$ (s)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>A</td><td>110.241</td><td>27.204</td><td>824</td><td>100.767</td></tr>
      <tr><td>B</td><td>110.780</td><td>27.456</td><td>727</td><td>112.220</td></tr>
      <tr><td>C</td><td>110.712</td><td>27.785</td><td>742</td><td>188.020</td></tr>
      <tr><td>D</td><td>110.251</td><td>27.825</td><td>850</td><td>258.985</td></tr>
      <tr><td>E</td><td>110.524</td><td>27.617</td><td>786</td><td>118.443</td></tr>
      <tr><td>F</td><td>110.467</td><td>27.921</td><td>678</td><td>266.871</td></tr>
      <tr><td>G</td><td>110.047</td><td>27.121</td><td>575</td><td>163.024</td></tr>
    </tbody>
  </table>
</div>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Three-dimensional distribution of monitoring stations">
    <img src="{{ '/assets/img/projects/rocket/station_distribution_3d.jpg' | relative_url }}" alt="Three-dimensional spatial distribution of the seven monitoring devices" loading="lazy" width="1000" height="580">
  </div>
  <figcaption><span>Figure 2.</span> Three-dimensional spatial distribution and geodetic layout of the seven vibration wave monitoring stations deployed around the predicted drop zone.</figcaption>
</figure>

### The Four-Sphere intersection positioning principle

Sound waves emitted at the supersonic boom origin $\mathbf{p} = (x, y, z)^\top$ travel isotropically at atmospheric sound speed $c = 340\text{ m/s}$. If the sonic boom is initiated at time $t_0$, the distance traveled to station $i$ located at $\mathbf{s}_i = (x_i, y_i, z_i)^\top$ satisfies:

<div class="hy-equation" role="math" aria-label="Distance constraint equation">
  \|\mathbf{p} - \mathbf{s}_i\| = \sqrt{(x - x_i)^2 + (y - y_i)^2 + (z - z_i)^2} = c(t_i - t_0)
</div>

This defines a sphere centered at station $\mathbf{s}_i$ with time-dependent radius $R_i = c(t_i - t_0)$:
- **One device:** Defines a continuous spherical shell of candidate positions.
- **Two devices:** Intersect along a spatial circle perpendicular to their baseline.
- **Three devices:** Intersect at exactly two conjugate points.
- **Four devices:** Because the boom emission time $t_0$ is also unknown, the problem contains **four unknowns** $(x, y, z, t_0)$. Four independent, non-coplanar monitoring devices are the strict analytical minimum required to eliminate $t_0$ and isolate a unique point in space and time.

To solve this nonlinear system robustly without false local divergence, the residual vector $\mathbf{F}(\mathbf{x})$ is minimized using MATLAB's trust-region reflective nonlinear least squares algorithm (`lsqnonlin`):

<div class="hy-equation" role="math" aria-label="Nonlinear least squares objective">
  \min_{\mathbf{p}, t_0} \sum_{i=1}^{n} \left[ \|\mathbf{p} - \mathbf{s}_i\| - c(t_i - t_0) \right]^2
</div>

### Traversal Exclusion Algorithm for multi-source matching

When four rocket debris pieces generate sound waves simultaneously, ground sensors record multiple arrival timestamps without source tags. Choosing four stations (A, B, F, G) each recording 4 arrivals yields $4^4 = 256$ candidate timestamp combinations.

The **Traversal Exclusion Algorithm** resolves this combinatorial ambiguity through a three-stage screening pipeline:

1. **Full candidate permutation:** Enumerate all 256 possible quadruplets $(t_{A,j}, t_{B,k}, t_{F,l}, t_{G,m})$.
2. **Physical and numerical screening:** Solve the Four-Sphere model for every candidate quadruplet and apply strict physical filters:
   - **Time causality:** $t_0 < \min(t_i)$ (sound must be emitted before it arrives).
   - **Atmospheric elevation bounds:** Debris altitude must lie within the supersonic atmospheric envelope ($0\text{ m} < h < 100{,}000\text{ m}$).
   - **Residual convergence:** Norm of solver residuals must satisfy $\|\mathbf{F}\|_2 < 10^{-4}$.
   This stage automatically eliminates 183 unphysical combinations, leaving exactly **73 mathematically viable candidates**.
3. **Bijective cross-source association:** Partition the 73 candidates into quadruplets of mutually exclusive combinations such that every recorded timestamp across all four stations is utilized exactly once. This uniquely pairs each vibration wave with its originating rocket debris.

### Weighted Least Squares and Monte Carlo error formulation

Real-world vibration sensors suffer from clock drift, environmental acoustic noise, and arrival-picking uncertainty. To model realistic conditions, a zero-mean random timing error with standard deviation $\sigma = 0.5\text{ s}$ is introduced:

<div class="hy-equation" role="math" aria-label="Error model equation">
  \tilde{t}_i = t_i + \epsilon_i, \quad \epsilon_i \sim \mathcal{N}(0, 0.5^2)
</div>

A Weighted Least Squares (WLS) objective balances station contributions according to signal quality and distance weighting factors $w_i$:

<div class="hy-equation" role="math" aria-label="Weighted least squares objective">
  \min_{\mathbf{p}, t_0} \sum_{i=1}^{n} w_i \left[ \|\mathbf{p} - \mathbf{s}_i\| - c(\tilde{t}_i - t_0) \right]^2
</div>

A Monte Carlo simulation framework evaluates spatial error propagation, running repeated perturbed trials to determine the variance and confidence bounds of the estimated debris coordinates.

<h2 id="findings">Selected results</h2>

### Single-debris localization (Problem 1)

Based on baseline separation and geometric conditioning, stations A, B, E, and G were selected. To confirm global numerical stability, four widely dispersed initial guess vectors were tested:

<div class="table-responsive">
  <table class="table table-sm table-striped">
    <thead>
      <tr>
        <th scope="col">Initial Guess $[\lambda_0, \phi_0, h_0, t_0]$</th>
        <th scope="col">Solved Lon (°E)</th>
        <th scope="col">Solved Lat (°N)</th>
        <th scope="col">Solved Alt (m)</th>
        <th scope="col">Solved $t_0$ (s)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>$[0, 0, 0, 160.72]$</td><td>110.589951</td><td>27.160875</td><td>981.80</td><td>3.973</td></tr>
      <tr><td>$[50, 20, 400, 160.72]$</td><td>110.587741</td><td>27.164292</td><td>978.60</td><td>4.767</td></tr>
      <tr><td>$[100, 25, 600, 160.72]$</td><td>110.587695</td><td>27.164326</td><td>994.18</td><td>4.778</td></tr>
      <tr><td>$[110.5, 27.1, 680, 160.72]$</td><td>110.587741</td><td>27.164290</td><td>994.05</td><td>4.754</td></tr>
    </tbody>
  </table>
</div>

All trials converged consistently, yielding the final single-debris solution:
- **Longitude:** $110.588^\circ\text{E}$
- **Latitude:** $27.163^\circ\text{N}$
- **Altitude:** $987.16\text{ m}$
- **Sonic boom time $t_0$:** $4.568\text{ s}$

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="3D single debris localization view">
    <img src="{{ '/assets/img/projects/rocket/single_debris_3d.jpg' | relative_url }}" alt="Three-dimensional positioning visualization of single rocket debris" loading="lazy" width="1000" height="580">
  </div>
  <figcaption><span>Figure 3.</span> Reconstructed three-dimensional positioning of the single rocket debris in relation to the ground monitoring network.</figcaption>
</figure>

### Multi-debris trajectory resolution (Problems 2 & 3)

Applying the Traversal Exclusion Algorithm across stations A, B, F, and G resolves the four distinct sound arrival combinations:

<div class="table-responsive">
  <table class="table table-sm table-striped">
    <thead>
      <tr>
        <th scope="col">Debris</th>
        <th scope="col">Station A Time (s)</th>
        <th scope="col">Station B Time (s)</th>
        <th scope="col">Station F Time (s)</th>
        <th scope="col">Station G Time (s)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>Debris 1</strong></td><td>100.767</td><td>112.220</td><td>266.871</td><td>163.024</td></tr>
      <tr><td><strong>Debris 2</strong></td><td>164.229</td><td>196.583</td><td>175.482</td><td>103.738</td></tr>
      <tr><td><strong>Debris 3</strong></td><td>214.850</td><td>92.453</td><td>166.270</td><td>206.789</td></tr>
      <tr><td><strong>Debris 4</strong></td><td>270.065</td><td>169.362</td><td>67.274</td><td>210.306</td></tr>
    </tbody>
  </table>
</div>

Substituting each confirmed arrival quadruplet into the Four-Sphere model yields the exact geodetic coordinates and sonic boom initiation times for all four debris pieces:

<div class="table-responsive">
  <table class="table table-sm table-striped">
    <thead>
      <tr>
        <th scope="col">Rocket Debris</th>
        <th scope="col">Longitude (°E)</th>
        <th scope="col">Latitude (°N)</th>
        <th scope="col">Altitude (m)</th>
        <th scope="col">Sonic Boom Time $t_0$ (s)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>Debris 1</strong></td><td>110.318</td><td>27.640</td><td>25,931.21</td><td>20.159</td></tr>
      <tr><td><strong>Debris 2</strong></td><td>110.493</td><td>27.331</td><td>21,900.58</td><td>18.374</td></tr>
      <tr><td><strong>Debris 3</strong></td><td>110.678</td><td>27.672</td><td>12,271.43</td><td>17.567</td></tr>
      <tr><td><strong>Debris 4</strong></td><td>110.557</td><td>27.893</td><td>11,030.54</td><td>15.300</td></tr>
    </tbody>
  </table>
</div>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="3D multi-debris localization view">
    <img src="{{ '/assets/img/projects/rocket/four_debris_3d.jpg' | relative_url }}" alt="Three-dimensional spatial visualization of the four rocket debris pieces" loading="lazy" width="1000" height="580">
  </div>
  <figcaption><span>Figure 4.</span> Spatial positions of the four resolved rocket debris pieces in 3D atmosphere, showing altitude stratification between 11 km and 26 km.</figcaption>
</figure>

### Timing noise sensitivity and error bounds (Problem 4)

When simulated Gaussian noise ($\sigma = 0.5\text{ s}$) is injected into sensor arrivals, the WLS algorithm converges to the following perturbed estimates:

<div class="table-responsive">
  <table class="table table-sm table-striped">
    <thead>
      <tr>
        <th scope="col">Debris</th>
        <th scope="col">Perturbed Lon (°E)</th>
        <th scope="col">Perturbed Lat (°N)</th>
        <th scope="col">Perturbed Alt (m)</th>
        <th scope="col">Perturbed $t_0$ (s)</th>
        <th scope="col">Altitude Shift $\Delta h$ (m)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><strong>Debris 1</strong></td><td>110.311</td><td>27.640</td><td>24,931.21</td><td>19.159</td><td>−1,000.00</td></tr>
      <tr><td><strong>Debris 2</strong></td><td>110.494</td><td>27.328</td><td>21,700.59</td><td>18.771</td><td>−199.99</td></tr>
      <tr><td><strong>Debris 3</strong></td><td>110.683</td><td>27.672</td><td>10,217.43</td><td>17.662</td><td>−2,053.99</td></tr>
      <tr><td><strong>Debris 4</strong></td><td>110.557</td><td>27.893</td><td>9,030.21</td><td>14.920</td><td>−2,000.33</td></tr>
    </tbody>
  </table>
</div>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Monte Carlo error visualization">
    <img src="{{ '/assets/img/projects/rocket/monte_carlo_error_3d.png' | relative_url }}" alt="Monte Carlo error simulation and spatial uncertainty comparison" loading="lazy" width="1000" height="580">
  </div>
  <figcaption><span>Figure 5.</span> Spatial sensitivity and Monte Carlo uncertainty analysis under 0.5 s measurement noise, contrasting horizontal stability against vertical dispersion.</figcaption>
</figure>

#### Geometric Dilution of Precision (GDOP) analysis
The numerical results reveal a pronounced asymmetry:
- **Horizontal positioning stability:** Longitude and latitude shifts remain below $0.007^\circ$ ($\approx 700\text{ m}$), demonstrating high planar robustness.
- **Vertical altitude sensitivity:** Estimated altitudes exhibit deviations between $0.20\text{ km}$ and $2.05\text{ km}$.

This behavior directly reflects the **Geometric Dilution of Precision (GDOP)** inherent to ground-based monitoring networks: ground stations are distributed horizontally across the Earth's surface (elevation spread $< 300\text{ m}$), while the supersonic sources occur at high altitudes ($11\text{ km} \sim 26\text{ km}$). The shallow vertical geometric aperture naturally magnifies vertical timing errors relative to horizontal baselines.

<h2 id="discussion">Discussion</h2>

### Methodological strengths
- **Geodetic ellipsoidal rigor:** Incorporating the WGS84 ellipsoid prevents systematic spherical distortion over regional baselines exceeding 100 km.
- **Analytical minimal configuration:** Formally establishes that four non-coplanar sensors are the exact necessary and sufficient condition for simultaneous spatio-temporal estimation.
- **Exhaustive combinatorial resolution:** The Traversal Exclusion Algorithm resolves the overlapping multi-signal assignment problem deterministically without arbitrary heuristic clustering.
- **Probabilistic uncertainty auditing:** Monte Carlo simulations identify vertical geometric sensitivity, establishing realistic error bounds rather than claiming unverified point accuracy.

### Assumptions and physical limitations
- **Constant acoustic propagation:** The model assumes uniform sound velocity ($c = 340\text{ m/s}$). In reality, temperature lapse rates with altitude, atmospheric pressure gradients, and wind shear cause acoustic ray refraction and path curvature.
- **Point-source shock simplification:** A supersonic body produces an extended Mach cone envelope rather than a single spherical point source. The estimated position represents the effective sonic boom emission center.
- **Airborne origin versus ground touchdown:** The model determines the airborne coordinates where the sonic boom was generated. Extrapolating the physical ground impact coordinates requires coupling this solution with aerodynamic drag, ballistic trajectory equations, and local wind field data.

### Research extensions
A production-grade operational system would incorporate:
1. **Ray-tracing through stratified atmospheres:** Integrating standard atmospheric models (e.g., NRLMSISE-00) to account for temperature and wind refraction.
2. **Optimal network sensor deployment:** Optimizing station coordinates to minimize geometric dilution of precision (GDOP) across high-probability re-entry corridors.

<p class="hy-source-note">Research record: Published journal article — Han Yang, <em>Research on Multi-Object Localization of Rocket Debris</em>, <strong>Frontier and Progress of Computational Mathematics and Modeling</strong>, December 2024, Vol. 5, No. 1, pp. 1–24. ISSN: 2313-4194. Sole author.</p>
