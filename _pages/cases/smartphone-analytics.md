---
layout: han-project
title: "Multibeam Bathymetry & Survey Planning"
description: "A geometric framework linking three-dimensional sonar coverage to terrain-aware survey-line planning."
permalink: /projects/modeling/multibeam-bathymetry/
discipline: "Computational geometry · Marine surveying"
period: "2023 study"
question: "How can a three-dimensional sonar footprint become an efficient survey plan?"
role: "AI-assisted modeling, numerical analysis, and research synthesis"
methods: "Ray–surface geometry, effective-slope reduction, adaptive line spacing"
outcome: "63 survey lines · 315 nautical miles · numerical full coverage"
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: Background
    id: background
  - label: Geometry
    id: geometry
  - label: Planning
    id: planning
  - label: Results
    id: results
  - label: Validation
    id: validation
  - label: Discussion
    id: discussion
---

<style>
.hy-case-study .hy-equation { overflow-x: auto; font-size: 1.05rem; }
</style>

<h2 id="abstract">Abstract</h2>

Multibeam bathymetry measures a strip of seabed on each vessel pass. The strip changes with water depth, seabed slope, and heading, so uniform survey-line spacing can leave shallow areas unmeasured while oversampling deeper water. This study connects an analytical coverage model to a terrain-aware planning algorithm. Ray–plane intersections give the coverage width on a sloping cross-section; an effective-slope transformation extends the result to arbitrary headings on a planar seabed. For gridded terrain, edge rays intersect an interpolated depth surface, and a greedy placement rule adapts line spacing to local coverage. A separate interval-union evaluator checks the resulting plan.

On an ideal planar region, the constructed plan uses 34 lines and 68 nautical miles, with 10% overlap between adjacent swaths. On the supplied bathymetric grid, a selected north–south plan uses 63 lines and 315 nautical miles, achieving numerical full coverage under the stated geometry and evaluation resolution. Relative to a shallow-depth uniform-spacing baseline evaluated on the same domain, route length falls by 46.6% and excess-overlap length by 68.9%. These results support adaptive survey planning within the tested candidate set; they do not establish global optimality or field-validated measurement accuracy.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">Central finding</p>
  <p>Let spacing follow the sonar footprint. Depth-dependent coverage can reduce unnecessary surveying while preserving coverage in the numerical model.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable bathymetric terrain and route comparison"><img src="{{ '/assets/img/research/multibeam-overview.svg' | relative_url }}" alt="Supplied bathymetry with 63 north–south survey lines, beside the 590 versus 315 nautical mile route-length comparison." width="1000" height="580" loading="lazy"></div>
  <figcaption><span>Figure 1.</span> Terrain-aware planning on the supplied 4 × 5 nautical mile region. The left panel shows the depth grid and the selected 63-line plan. The right panel compares survey-line length with a 118-line shallow-depth uniform-spacing baseline. Lengths exclude vessel turns and transit between lines.</figcaption>
</figure>

<h2 id="background">1. Background and study domain</h2>

A multibeam transducer emits a fan of acoustic rays in a plane perpendicular to the vessel's heading. Where that fan meets the seabed, it defines a coverage swath. Survey planning must balance three quantities: unmeasured area, repeated coverage, and vessel travel. Spacing based only on mean depth can be too wide near shallow water; spacing based on the minimum depth can be unnecessarily dense across the rest of the region.

The study proceeds from a controlled geometry to a spatially varying surface. The analytical examples use a 120° opening angle and a 1.5° planar slope. The ideal planning region is 4 nautical miles across the slope and 2 nautical miles along it, with a central depth of 110 m. The terrain example uses a supplied 251 × 201 depth grid spanning 4 × 5 nautical miles: 50,451 depth values at 0.02 nautical mile spacing, equivalent to 37.04 m. One nautical mile is 1,852 m throughout.

The model treats the vessel as located at the sea surface and represents the fan as continuous geometric coverage. It neglects refraction, discrete beam footprints, vessel motion, tides, and navigation uncertainty. These assumptions isolate the survey-layout problem; a field survey would require additional acoustic and operational modeling.

<h2 id="geometry">2. From three-dimensional geometry to coverage width</h2>

### 2.1 Ray intersections on a sloping cross-section

Let $D$ be the depth immediately beneath the vessel, $\theta$ the full transducer opening angle, and $\alpha$ the seabed slope in the cross-section. Write $c=\cos(\theta/2)$ and $s=\sin(\theta/2)$. Intersecting the two edge rays with the seabed gives the shallow-side and deep-side horizontal half-widths:

<div class="hy-equation">
\[
a_{\mathrm{sh}}=\frac{Ds}{c+s\tan\alpha},
\qquad
a_{\mathrm{dp}}=\frac{Ds}{c-s\tan\alpha}.
\tag{1}
\]
</div>

Their sum is the horizontal footprint. The corresponding distance measured along the sloping seabed is

<div class="hy-equation">
\[
W(D,\alpha)=
\frac{D\sin\theta\,\sec\alpha}
{c^2-s^2\tan^2\alpha}.
\tag{2}
\]
</div>

The formula requires positive ray-intersection denominators. In the flat-seabed limit it reduces to $W=2D\tan(\theta/2)$. With 200 m line spacing and a central depth of 70 m, the nine analytical positions produce widths from 170.33 m to 315.81 m. Geometric overlap ranges from −11.17% to 33.64%: a negative value marks a gap, while a large positive value indicates repeated coverage.

### 2.2 Heading-dependent effective slope

Let $\beta$ be the angle between the survey heading and the horizontal projection of the seabed normal. The fan lies in the vertical plane perpendicular to that heading. The slope seen inside that plane is

<div class="hy-equation">
\[
T=\tan\alpha_{\mathrm{eff}}
=\tan\alpha\,|\sin\beta|.
\tag{3}
\]
</div>

For a vessel traveling a horizontal distance $t$ from the reference point, the adopted down-slope coordinate convention gives $D(t)=D_0+t\tan\alpha\cos\beta$. The cross-section result becomes

<div class="hy-equation">
\[
W(t,\beta)=
\frac{D(t)\sin\theta\sqrt{1+T^2}}
{c^2-s^2T^2}.
\tag{4}
\]
</div>

This reduction retains the three-dimensional heading dependence while avoiding repeated spatial construction. At $\beta=90^\circ$, travel follows a depth contour and the width remains approximately 416.69 m for the 120 m reference-depth example. Across 64 heading–distance combinations, the closed form agrees with direct three-dimensional ray–plane intersections to a maximum relative difference of about $2.7\times10^{-15}$.

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable geometric method diagram"><img src="{{ '/assets/img/research/multibeam-method.svg' | relative_url }}" alt="A sonar fan intersects a sloping seabed; the workflow connects coverage geometry, terrain-dependent line placement, and interval-union evaluation." width="1000" height="580" loading="lazy"></div>
  <figcaption><span>Figure 2.</span> Geometric interpretation and planning workflow. The ray diagram is conceptual and not to scale; the workflow describes the implemented numerical model.</figcaption>
</figure>

<h2 id="planning">3. Terrain-aware survey-line planning</h2>

### 3.1 Overlap as an intersection, not a fixed-width shortcut

When neighboring swaths have different widths, the flat-seabed expression $1-d/W$ can misclassify a gap. For a planar slope, let $d_i$ be the separation between adjacent lines and $D_i$ the depth beneath line $i$. The overlap relative to the new swath is

<div class="hy-equation">
\[
\eta_{i+1}=\frac{
a_{\mathrm{dp}}(D_i)+a_{\mathrm{sh}}(D_{i+1})-d_i}
{a_{\mathrm{sh}}(D_{i+1})+a_{\mathrm{dp}}(D_{i+1})}.
\tag{5}
\]
</div>

Both numerator and denominator use horizontal distances; measuring both along the planar slope gives the same ratio. The ideal-region planner starts at the shallow boundary and places each next contour-following line at the largest spacing compatible with a 10% overlap lower bound. It stops when the deep-side edge covers the opposite boundary. The resulting 34 lines have 33 adjacent overlaps of approximately 10% and cover the full cross-slope interval in the model.

### 3.2 Intersecting rays with gridded terrain

For varying bathymetry, bilinear interpolation defines the depth field $D(x,y)$. Let $\mathbf p$ be the vessel position, $\mathbf v$ the horizontal unit vector perpendicular to the survey heading, and $\tau$ the slant range. Each edge intersection solves

<div class="hy-equation">
\[
\tau\cos(\theta/2)=
D\!\left(\mathbf p\pm\tau\sin(\theta/2)\mathbf v\right).
\tag{6}
\]
</div>

The implementation brackets a root and refines it by bisection. For the supplied interpolated surface, the estimated gradient bound is about 0.0589, below $\cot60^\circ$. This provides a positive derivative margin of about 0.449 for the edge-ray intersection function, supporting a unique intersection under these assumptions.

At each tested heading, greedy placement increases the separation until the local overlap constraint would fail. The design uses 20 m along-line sampling. A separate evaluator samples cross-sections and merges all coverage intervals, accounting for multiple overlaps rather than subtracting only adjacent pairs. This separation tests coverage arithmetic, although the evaluator shares the ray–surface intersection implementation with the planner.

### 3.3 An explicit decision rule

The outer search tests headings between −45° and 45°, with 5° spacing and 1° refinement near the selected direction. It also tests overlap lower bounds of 5%, 8%, 10%, and 12%. A missed-area tolerance of 0.1% defines admissibility; among admissible candidates, selection first minimizes the cumulative line length with overlap above 20%, then total line length. This is a chosen multi-objective priority, not a universal optimum criterion.

The selected plan has heading 0°—north–south—and a 5% design overlap lower bound. The 10% overlap rule belongs to the separate ideal-slope example; the terrain case does not require its local overlap to stay within 10–20%. Local terrain variation still produces substantial overlap above 20%, which is measured and reported rather than hidden.

<h2 id="results">4. Results</h2>

### 4.1 Coverage and route length

The ideal-region plan uses 34 contour-following lines of 2 nautical miles each. Its spacing increases with depth, and the numerical union of swaths covers the 7,408 m cross-slope interval without gaps. The terrain plan uses 63 north–south lines of 5 nautical miles each, totaling 315 nautical miles. At the 9.26 m evaluation slice spacing, the independent interval-union calculation returns a missed-area proportion of about $4.9\times10^{-13}$, which is numerical zero for the reporting precision.

<div class="hy-table-scroll" tabindex="0" role="region" aria-label="Scrollable survey-plan comparison">
  <table>
    <caption>Table 1. Plans on the supplied terrain grid, evaluated using the same boundary and coverage conventions.</caption>
    <thead><tr><th scope="col">Plan</th><th scope="col">Lines</th><th scope="col">Survey length (NM)</th><th scope="col">Missed area (%)</th><th scope="col">Excess-overlap length (NM)</th></tr></thead>
    <tbody>
      <tr><th scope="row">Terrain-aware selected plan</th><td>63</td><td>315.0</td><td>≈ 0</td><td>172.065</td></tr>
      <tr><th scope="row">Uniform spacing: shallowest depth</th><td>118</td><td>590.0</td><td>≈ 0</td><td>553.830</td></tr>
      <tr><th scope="row">Uniform spacing: mean depth</th><td>39</td><td>195.0</td><td>14.83</td><td>68.005</td></tr>
    </tbody>
  </table>
</div>

Excess-overlap length is the sum, across adjacent swath pairs, of the along-line portions whose overlap exceeds 20%; it is not an overlap-area percentage. The selected plan gives 318,664.38 m, equivalent to 172.065 nautical miles. A location covered by several swaths can contribute to several adjacent-pair terms.

### 4.2 Why the baseline matters

Uniform spacing based on the shallowest depth provides numerical full coverage but requires 118 lines. Relative to that admissible baseline, the selected terrain-aware plan reduces survey-line length from 590 to 315 nautical miles, a 46.6% decrease, and reduces excess-overlap length by 68.9%. The mean-depth baseline is shorter but leaves approximately 14.83% of the domain unmeasured; it is not an equivalent full-coverage alternative.

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable route and overlap comparison"><img src="{{ '/assets/img/research/multibeam-comparison.svg' | relative_url }}" alt="Comparison of route length and excess-overlap length for the terrain-aware, shallow-depth uniform, and mean-depth uniform plans, noting the 14.83 percent missed area of the last plan." width="1000" height="580" loading="lazy"></div>
  <figcaption><span>Figure 3.</span> Two objectives under a common evaluation convention. The mean-depth baseline has the lowest lengths but fails the coverage condition. Reductions are relative to the shallow-depth baseline, not to every possible survey plan.</figcaption>
</figure>

<h2 id="validation">5. Numerical validation and uncertainty</h2>

The study uses complementary checks rather than treating one performance number as validation of the whole system. Analytical cross-sections agree with numerical ray tracing to machine precision, and the heading-dependent model agrees with direct three-dimensional intersections. These checks establish implementation consistency within the assumed geometry.

For the terrain plan, coverage interval ordering shows no violations in the evaluator. Refining evaluation spacing from 0.02 to 0.0025 nautical miles changes the reported excess-overlap length by about 47 m, or 0.015%, while missed area remains numerically zero. This is a resolution-sensitivity result, not a proof that no arbitrarily small gap exists in continuous space.

The archived strip-holdout experiment compares interpolation against withheld values from the supplied grid. Bilinear interpolation gives approximately 3.07 mm mean absolute error and 4.26 mm root mean squared error; the maximum is about 15 mm. These small values describe interpolation on this particular grid, not sonar accuracy or an independently measured seabed truth.

The archived fixed-plan perturbation experiment adds Gaussian depth noise with an assumed standard deviation of 0.5 m. Across 30 realizations, maximum missed area is approximately 0.000624% and the excess-overlap standard deviation is approximately 388 m. Replanning under perturbation is a separate experiment and does not demonstrate that the unchanged plan remains strictly gap-free. These noise results depend on the assumed perturbation model and have not been verified against field observations.

<h2 id="discussion">6. Discussion and next steps</h2>

The useful connection is between local geometry and regional planning. An interpretable coverage formula explains why spacing should change with depth; the effective-slope transformation explains how heading changes the footprint; a numerical terrain model extends that logic beyond planar seabeds. The selected plan demonstrates that the resulting adaptive spacing can outperform a conservative uniform-spacing baseline under a common numerical evaluator.

The search remains restricted: headings are sampled, inner placement is greedy, and mixed-heading or curved routes are not exhaustively optimized. Therefore the result is a selected candidate within the tested design procedure, not a globally shortest survey or a proven optimum over all parallel-line placements. The ideal-slope greedy argument also applies within its specified contour-following line family.

Operational follow-up would include turn and transit costs, refraction and beam footprints, correlated terrain errors, vessel motion, and navigation uncertainty. An expanded search could vary the first-line position, compare mixed-heading plans, and report a Pareto frontier over missed area, excess overlap, and travel. Field validation would require independent soundings and an explicit survey-accuracy specification.

<p class="hy-source-note">Study record: the archived 2023 multibeam survey-planning manuscript, supplied bathymetric grid, Python implementation, and numerical output files. Core geometry and the selected route were recomputed for this web account; the extended convergence, interpolation, and noise experiments are reported from the archived records. This is an AI-assisted computational research note.</p>
