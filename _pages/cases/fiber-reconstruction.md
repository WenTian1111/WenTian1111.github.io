---
layout: han-project
title: Planar Curve Reconstruction from Fiber Sensors
description: A detailed study of wavelength calibration, sparse curvature interpolation and arc-length reconstruction, with independent quadrature
  checks and explicit sign, pose and uncertainty limits.
permalink: /projects/modeling/fiber-reconstruction/
discipline: Inverse geometry · Optical sensing
period: 2024 study
question: Which parts of a curve can six curvature magnitudes determine, and which still depend on unmeasured assumptions?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Wavelength calibration, spline interpolation, planar Frenet equations, independent quadrature, synthetic refinement and uncertainty tests
outcome: Two conditional reconstructions · 41-node synthetic experiment · verified numerical consistency · unresolved sign ambiguity
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Measurements and geometry assumptions
    id: data
  - label: 3. Wavelength-to-curvature inference
    id: curvature
  - label: 4. Sparse curvature interpolation
    id: interpolation
  - label: 5. Shape reconstruction
    id: integration
  - label: 6. Sign and pose identifiability
    id: sign
  - label: 7. Exact-curve experiment
    id: synthetic
  - label: 8. Numerical convergence
    id: convergence
  - label: 9. Measurement and structural uncertainty
    id: sensitivity
  - label: 10. Independent verification
    id: verification
  - label: 11. Discussion
    id: discussion
  - label: 12. Conclusions
    id: conclusions
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Local curvature measurements can describe how a fiber bends, but reconstructing its global shape also requires a sign convention, material coordinates and an initial pose. This study follows six optical sensing nodes through wavelength calibration, continuous curvature interpolation and planar arc-length integration. Two test records yield nearly constant curvature magnitudes, with means 2.22636 and 2.97955 m⁻¹. Under a prescribed positive-sign convention and initial tangent of 45°, the resulting three-meter curves resemble circular arcs with radii 0.44916 and 0.33562 m and accumulated turning of 382.89° and 512.13°.

A new independent method integrates the exact spline antiderivative and then quadratures the tangent components. It agrees with the source fixed-step reconstruction within 3.2 × 10⁻¹⁴ m on the shared grid, establishing strong numerical consistency for the assumed curvature field. This precision is distinct from physical accuracy: the sensor records lack independent shape truth, and alternating unmeasured curvature signs produce meter-scale endpoint changes. An exact synthetic curve supplies a separate reference experiment. Its 40 intervals, hence 41 sampling nodes, reproduce maximum shape error about 8.87 × 10⁻⁸ m under noise-free assumptions. The article also corrects interpretation of refinement rates, continuous error bounds and an archived error-separation diagnostic, keeping numerical verification separate from identifiability and measurement uncertainty.

<h2 id="introduction">1. Introduction</h2>

A shape sensor measures locally while its intended output is global. A small wavelength change is converted into a local bending quantity; that quantity must then be interpolated and accumulated along the fiber. Each step adds assumptions. Interpolation supplies information between sensing locations, integration supplies a curve relative to a starting pose, and a sign convention decides whether a bend turns left or right.

This project makes that sequence explicit rather than treating a visually smooth reconstruction as evidence of a uniquely measured shape. Its measured-data stage contains two small wavelength records. Its numerical stage compares integration methods and an analytic circular-arc limit. Its synthetic stage uses a curve whose coordinates and curvature are known. Its uncertainty stage perturbs sensor readings and reconfigures signs, layout and interpolation.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/cover.webp' | relative_url }}" alt="Supplied optical-sensing concept illustration. The visible fiber and hardware illustrate the theme; they are not photographed evidence of the two reconstructed test shapes." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 1.</span> Supplied optical-sensing concept illustration. The visible fiber and hardware illustrate the theme; they are not photographed evidence of the two reconstructed test shapes.</figcaption></figure>

The key research distinction is between consistency and identification. Multiple accurate integrators can agree on the same assumed model while the available observations still permit very different physical curves. A useful research account should explain both what the calculation reproduces and what extra measurement would make the inverse problem better determined.

<h2 id="data">2. Measurements and geometry assumptions</h2>

### 2.1 The supplied wavelength table

The input table contains six sensing locations in each of two tests and their two reference wavelengths. Reference values are 1,529 and 1,540 nm. Test wavelengths range from 1,529.807 to 1,529.814 nm and from 1,541.090 to 1,541.095 nm. These small within-test differences are retained rather than smoothed away.

<div class="hy-model-table"><table><caption>Table 1. The six supplied wavelengths.</caption><thead><tr><th scope="col">Node</th><th scope="col">Material coordinate (m)</th><th scope="col">Test 1 (nm)</th><th scope="col">Test 2 (nm)</th></tr></thead><tbody><tr><td>FBG1</td><td>0.0</td><td>1529.808</td><td>1541.095</td></tr><tr><td>FBG2</td><td>0.6</td><td>1529.807</td><td>1541.092</td></tr><tr><td>FBG3</td><td>1.2</td><td>1529.813</td><td>1541.090</td></tr><tr><td>FBG4</td><td>1.8</td><td>1529.812</td><td>1541.093</td></tr><tr><td>FBG5</td><td>2.4</td><td>1529.814</td><td>1541.094</td></tr><tr><td>FBG6</td><td>3.0</td><td>1529.809</td><td>1541.091</td></tr></tbody></table></div>

The sensing interval is assumed to be 0.6 m, with the first node at zero, making the sensed segment three meters long. The queried positions 0.3–0.7 m are interpreted as initial material coordinates, not the reconstructed curve's horizontal coordinates. For an inextensible fiber, this material distance supplies the arc-length parameter used in reconstruction.

### 2.2 Four assumptions that define the calculation

The reconstruction is planar; the supplied calibration is accepted; the material coordinate is identified with arc length; and positive curvature signs plus an initial tangent of 45° are prescribed. The starting point is placed at the origin. These assumptions determine a relative planar curve, not an absolute three-dimensional location.

No compensation model for temperature, axial strain, mounting effects or calibration uncertainty is estimated from these records. The analysis therefore evaluates the given conversion model rather than validating a full optical measurement system. It also imposes no self-contact or mechanical equilibrium constraint. Multi-turn curves can be mathematically admissible without constituting a physically realizable unrestrained fiber configuration.

<h2 id="curvature">3. Wavelength-to-curvature inference</h2>

For node i, the given calibration converts a relative wavelength shift into curvature:

<div class="hy-equation">
\[
k_i=C\,\frac{\lambda_i-\lambda_0}{\lambda_0},\qquad C=4200\ \mathrm{m}^{-1}.
\tag{1}
\]
</div>

The wavelength ratio is dimensionless and the calibration coefficient supplies inverse meters. Direct recalculation reproduces the stored node curvatures within their six-decimal CSV rounding. Test 1 spans approximately 2.21674–2.23597 m⁻¹; test 2 spans 2.97273–2.98636 m⁻¹. Both sets are nearly constant, suggesting an approximately circular curve when all signs are positive.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/sensor-curvature.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/sensor-curvature.svg' | relative_url }}" alt="Six converted node values and their not-a-knot cubic splines. Dashed lines mark mean curvature. Curves between nodes are inferred rather than independently measured." width="1046" height="389" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 2.</span> Six converted node values and their not-a-knot cubic splines. Dashed lines mark mean curvature. Curves between nodes are inferred rather than independently measured.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 2. Curvature summaries and conditional geometric scales.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Test 1</th><th scope="col">Test 2</th></tr></thead><tbody><tr><td>Mean magnitude (m⁻¹)</td><td>2.226357</td><td>2.979545</td></tr><tr><td>Node range (m⁻¹)</td><td>0.019228</td><td>0.013636</td></tr><tr><td>Inverse mean curvature (m)</td><td>0.449164</td><td>0.335622</td></tr><tr><td>Prescribed positive-sign turning</td><td>382.890°</td><td>512.130°</td></tr><tr><td>Three-meter winding count</td><td>1.0636</td><td>1.4226</td></tr></tbody></table></div>

The inverse mean is a useful radius scale, not an independent fitted measurement of a circle. The actual spline field varies slightly, and the reconstruction integrates those variations. Similarly, the winding count describes accumulated tangent turning; it should not automatically be interpreted as a count of mechanically separated physical loops.

<h2 id="interpolation">4. Sparse curvature interpolation</h2>

### 4.1 Compare interpolation rules

Not-a-knot cubic interpolation is the main continuous model. PCHIP, piecewise linear interpolation and a constant mean provide alternative constructions. All share the same sparse measurements, so their agreement is a model-choice diagnostic rather than statistical replication.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/interpolation-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/interpolation-comparison.svg' | relative_url }}" alt="Four interpolation rules at the queried material positions. Differences quantify sensitivity to the chosen continuous representation; they are not a probability-based confidence interval." width="1046" height="399" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 3.</span> Four interpolation rules at the queried material positions. Differences quantify sensitivity to the chosen continuous representation; they are not a probability-based confidence interval.</figcaption></figure>

The main spline gives test-1 values 2.21198, 2.21257, 2.21425, 2.21674 and 2.21977 m⁻¹ at 0.3–0.7 m. Test-2 values are 2.98317, 2.98159, 2.97989, 2.97818 and 2.97655 m⁻¹. At 0.6 m, interpolation passes through the second sensor value, providing a direct implementation check.

### 4.2 Sparse-data checks and coordinate ambiguity

Leave-one-node-out tests fit a spline to five nodes and predict the omitted sixth. The archived mean absolute discrepancies are 0.0347 and 0.0125 m⁻¹, with maxima 0.0797 and 0.0334. Endpoint omissions require extrapolation and contribute large errors, so these six-point summaries are not simply interior interpolation accuracy.

An alternative placement starts the first sensor at 0.6 m. Then queries below 0.6 m are outside the observed interval; 0.6 itself is a sensor location. The original annotation code labels points below 1.2 m as extrapolation, a broader label than the actual shifted support warrants. This revision uses support boundaries rather than those labels.

A second coordinate interpretation projects queries by s=x/cos45°. Its maximum discrepancy is about 0.00924 m⁻¹ in test 1 and 0.00372 in test 2. This tests one proposed semantic alternative. Small differences under nearly constant curvature do not resolve which coordinate definition the original sensing experiment intended.

<h2 id="integration">5. Shape reconstruction</h2>

### 5.1 Integrate a tangent field

For signed planar curvature k(s), the tangent angle accumulates along material distance. Position follows by integrating its unit tangent:

<div class="hy-equation">
\[
\frac{d\theta}{ds}=k(s),\qquad \frac{dx}{ds}=\cos\theta(s),\qquad \frac{dy}{ds}=\sin\theta(s).
\tag{2}
\]
</div>

The prescribed initial state is θ(0)=π/4 and (x(0),y(0))=(0,0). The source uses classical fixed-step RK4 with nominal h=10⁻⁴ m and a 0.01 m output grid. A DOP853 calculation is archived as a cross-method reference.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/workflow.webp' | relative_url }}" alt="Confirmed supplied workflow. The numerical study proceeds from calibration through interpolation and integration to separate synthetic and uncertainty checks; miniature examples are conceptual." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 4.</span> Confirmed supplied workflow. The numerical study proceeds from calibration through interpolation and integration to separate synthetic and uncertainty checks; miniature examples are conceptual.</figcaption></figure>

### 5.2 Circular-arc limit and actual reconstructed shapes

If curvature is constant, the equations have an analytic solution:

<div class="hy-equation">
\[
\begin{aligned}\theta(s)&=\theta_0+\bar k s,\\x(s)&=\frac{\sin(\theta_0+\bar k s)-\sin\theta_0}{\bar k},\\y(s)&=\frac{\cos\theta_0-\cos(\theta_0+\bar k s)}{\bar k}.\end{aligned}
\tag{3}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/reconstructed-curves.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/reconstructed-curves.svg' | relative_url }}" alt="Positive-sign spline reconstruction compared with the mean-curvature circular arc. Markers locate sensing material positions along the reconstructed curve, not separate measured Cartesian points." width="854" height="418" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 5.</span> Positive-sign spline reconstruction compared with the mean-curvature circular arc. Markers locate sensing material positions along the reconstructed curve, not separate measured Cartesian points.</figcaption></figure>

Fresh quadrature gives endpoints (0.09705137, 0.15396152) m and (−0.33748178, 0.55560365) m. Maximum deviations from the corresponding mean-curvature arcs are 6.972 mm and 2.838 mm. These are model-to-model distances, not physical reconstruction error against an observed shape.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/turning-accumulation.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/turning-accumulation.svg' | relative_url }}" alt="Accumulated tangent turning along the fiber. Small positive curvature integrated over three meters exceeds one full revolution; the 360° line is a geometric reference." width="1046" height="399" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 6.</span> Accumulated tangent turning along the fiber. Small positive curvature integrated over three meters exceeds one full revolution; the 360° line is a geometric reference.</figcaption></figure>

The difference from a gentle-wave illustration in the original task is unsurprising: the numerical data imply the displayed multi-turn geometry under the stated sign convention. A conceptual sketch is not a substitute for the actual measurements or an additional shape constraint.

<h2 id="sign">6. Sign and pose identifiability</h2>

Curvature magnitudes alone do not fix turning direction. The archived alternative assigns alternating positive and negative signs at the same sensing nodes and interpolates them. Because between-node behavior is unobserved, this alternative can produce a very different continuous field while matching the available node magnitudes.

<div class="hy-equation">
\[
k_i^{(\sigma)}=\sigma_i|k_i|,\qquad \sigma_i\in\{-1,+1\}.
\tag{4}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/sign-ambiguity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/sign-ambiguity.svg' | relative_url }}" alt="The same measured node magnitudes with all-positive versus alternating node signs. These are competing conditional reconstructions, not two independently observed fibers." width="1066" height="401" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 7.</span> The same measured node magnitudes with all-positive versus alternating node signs. These are competing conditional reconstructions, not two independently observed fibers.</figcaption></figure>

The alternating-sign endpoint differs from the positive-sign endpoint by approximately 2.550 m and 2.896 m. This is far larger than interpolation-choice differences. The wavelength table therefore cannot substantiate the circular-arc conclusion without a sign or orientation assumption.

Even a fully signed curvature field determines shape only up to initial translation and rotation until the starting pose is specified. Replacing the planar model with three-dimensional reconstruction introduces further information requirements; this project does not infer torsion or out-of-plane behavior.

Sign ambiguity is a structural uncertainty rather than a small-noise confidence band. More decimal places or smaller integration steps cannot remove it. Additional orientation-sensitive measurements, an independently tracked initial pose or justified mechanical constraints would be needed to exclude alternative shapes.

<h2 id="synthetic">7. Exact-curve experiment</h2>

### 7.1 A reference with known geometry

The synthetic experiment uses y=x³+x on 0≤x≤1. Its initial tangent is 45°, and its curvature is analytically available:

<div class="hy-equation">
\[
k(x)=\frac{6x}{[1+(3x^2+1)^2]^{3/2}},\qquad s(x)=\int_0^x\sqrt{1+(3u^2+1)^2}\,du.
\tag{5}
\]
</div>

The arc length is 2.270731886 m. Numerical inversion of s(x) creates equal-arc-length samples. The production setting uses **40 intervals and 41 nodes**, with spacing about 0.0567683 m. A cubic spline of these exact curvature samples is integrated using the same reconstruction equations.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/synthetic-reconstruction.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/synthetic-reconstruction.svg' | relative_url }}" alt="Exact synthetic curve and a fresh reconstruction using the spline antiderivative plus tangent quadrature. The nanometer error scale is a noise-free numerical benchmark, not sensor-system accuracy." width="926" height="399" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 8.</span> Exact synthetic curve and a fresh reconstruction using the spline antiderivative plus tangent quadrature. The nanometer error scale is a noise-free numerical benchmark, not sensor-system accuracy.</figcaption></figure>

### 7.2 Compare at matched arc length

The error compares the inferred and exact Cartesian points at the same s, rather than selecting each point's nearest location on the reference:

<div class="hy-equation">
\[
e(s)=\|\hat{\mathbf r}(s)-\mathbf r_{\rm exact}(s)\|_2.
\tag{6}
\]
</div>

The archive reports maximum error 8.8678926 × 10⁻⁸ m, RMS 5.64945 × 10⁻⁸ m and an endpoint maximum. New independent quadrature reproduces maximum error 8.8678950 × 10⁻⁸ m; its RMS is 5.63268 × 10⁻⁸ m because the output comparison avoids the archive's linear interpolation from RK steps.

This is a genuine reference experiment for that synthetic curvature field, but it contains exact samples, a correct sign convention and no calibration or wavelength noise. Its very small error demonstrates numerical capability under these assumptions; it does not validate nanometer accuracy on the supplied sensing records.

<h2 id="convergence">8. Numerical convergence</h2>

### 8.1 Separate density and integration refinement

The archived density scan increases intervals N from 5 to 320, using the same synthetic reference. Errors fall from 1.254 × 10⁻² m to 5.064 × 10⁻¹⁰ m, but adjacent observed rates vary substantially. The unusually rapid 20-to-40 reduction is followed by a much smaller 40-to-80 reduction; one constant fourth-order empirical rate does not describe the full table.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/numerical-convergence.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/numerical-convergence.svg' | relative_url }}" alt="Two archived refinement scans. N counts intervals, not sensor nodes. The h comparison includes interpolation onto a fixed evaluation grid, so it is not a pure RK4 truncation-error measurement." width="1045" height="394" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 9.</span> Two archived refinement scans. N counts intervals, not sensor nodes. The h comparison includes interpolation onto a fixed evaluation grid, so it is not a pure RK4 truncation-error measurement.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 3. Saved density scan against the exact curve.</caption><thead><tr><th scope="col">Intervals N</th><th scope="col">Nodes</th><th scope="col">Maximum error (m)</th></tr></thead><tbody><tr><td>5</td><td>6</td><td>1.254 × 10⁻²</td></tr><tr><td>10</td><td>11</td><td>1.707 × 10⁻³</td></tr><tr><td>20</td><td>21</td><td>3.558 × 10⁻⁵</td></tr><tr><td>40</td><td>41</td><td>8.868 × 10⁻⁸</td></tr><tr><td>80</td><td>81</td><td>3.245 × 10⁻⁸</td></tr><tr><td>160</td><td>161</td><td>2.641 × 10⁻⁹</td></tr><tr><td>320</td><td>321</td><td>5.064 × 10⁻¹⁰</td></tr></tbody></table></div>

For unequal step ratios, observed order must divide the logarithm of error ratios by the logarithm of step ratios:

<div class="hy-equation">
\[
p=\frac{\log(E(h_1)/E(h_2))}{\log(h_1/h_2)}.
\tag{7}
\]
</div>

The archive instead labels log₂(error ratio) as order even when h changes by factors of three or 3.33. Correct recalculation gives about 1.98–2.01 for this output-grid comparison, consistent with a substantial linear-interpolation contribution. It does not show that the RK4 method itself becomes second order.

### 8.2 Repair interpretation of error separation

The source's purported continuous-true-curvature diagnostic clips arc length at 1.0 m before inverting s(x), despite total arc length 2.27 m. Beyond that point it no longer uses the correct continuous reference curvature. Comparing two integrators on this shared clipped field cannot establish the claimed percentage contribution to true-curve error.

This note therefore withdraws that attribution and uses the independently reconstructed spline-versus-exact comparison instead. A future decomposition should use the full domain, exact or dense output at matched evaluation points, and separate interpolation, integration and output-grid errors.

<h2 id="sensitivity">9. Measurement and structural uncertainty</h2>

The archived Monte Carlo test perturbs each wavelength with assumed independent uniform noise in ±0.02 nm, holding the rest of the reconstruction pipeline fixed. One thousand draws per test with a fixed seed give mean endpoint displacements about 22.6 and 17.7 mm, and 95th percentiles about 43.8 and 33.1 mm.

<div class="hy-equation">
\[
\delta k_i=\frac{4200}{\lambda_0}\,\delta\lambda_i.
\tag{8}
\]
</div>

These are sensitivity results under an imposed noise distribution, not empirically estimated confidence bounds. The ±0.02 nm amplitude is several times the small within-record wavelength variation. That variation itself is not a calibrated measurement-error distribution.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/uncertainty-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size"><img src="{{ '/assets/img/research/fiber-reconstruction/uncertainty-comparison.svg' | relative_url }}" alt="Archived endpoint-displacement distributions under assumed wavelength noise and model-reconfiguration shifts. The log scale distinguishes millimeter interpolation effects from meter-scale sign effects." width="1046" height="404" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 10.</span> Archived endpoint-displacement distributions under assumed wavelength noise and model-reconfiguration shifts. The log scale distinguishes millimeter interpolation effects from meter-scale sign effects.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 4. Distinct uncertainty questions.</caption><thead><tr><th scope="col">Perturbation</th><th scope="col">Test 1</th><th scope="col">Test 2</th><th scope="col">Interpretation</th></tr></thead><tbody><tr><td>Uniform ±0.02 nm, mean shift</td><td>22.6 mm</td><td>17.7 mm</td><td>Assumed measurement-noise scenario</td></tr><tr><td>Uniform ±0.02 nm, P95</td><td>43.8 mm</td><td>33.1 mm</td><td>Empirical percentile within that scenario</td></tr><tr><td>Mean-curvature replacement</td><td>6.971 mm</td><td>2.712 mm</td><td>Interpolation/model choice</td></tr><tr><td>First-node layout shifted</td><td>7.475 mm</td><td>3.381 mm</td><td>Coordinate assumption</td></tr><tr><td>Alternating node signs</td><td>2.550 m</td><td>2.896 m</td><td>Structural non-identifiability</td></tr></tbody></table></div>

The reconfiguration table lists a small nonzero displacement even for its nominal spline reference because that sensitivity implementation differs slightly from the main integration path. Those few-micrometer offsets should not be mistaken for sensor noise. More importantly, combining all these quantities into one error bar would merge assumptions with different meanings.

<h2 id="verification">10. Independent verification</h2>

### 10.1 A method independent of the stepper

The new check first obtains the exact piecewise-polynomial antiderivative of the cubic spline, then evaluates its integrated tangent components by quadrature, splitting at spline knots:

<div class="hy-equation">
\[
\theta(s)=\theta_0+K(s)-K(0),\qquad \mathbf r(s)=\int_0^s(\cos\theta(u),\sin\theta(u))\,du.
\tag{9}
\]
</div>

It agrees with a fresh execution of the source RK4 routine within 2.86 × 10⁻¹⁴ m and 3.18 × 10⁻¹⁴ m on the 301-point measured-test grid. The saved six-decimal coordinate CSV differs by up to about 0.69 μm, as expected from serialization rounding. Numerical verification therefore uses fresh unrounded arrays rather than claiming sub-rounding precision from the stored table.

### 10.2 Bounds must hold between nodes

For two curvature fields with the same starting pose, an endpoint-distance bound follows from integrating curvature difference twice:

<div class="hy-equation">
\[
\|\mathbf r_k(s)-\mathbf r_{\bar k}(s)\|_2\le\frac{s^2}{2}\max_{0\le u\le s}|k(u)-\bar k|.
\tag{10}
\]
</div>

The original bound substitutes a maximum over sensor nodes, which need not bound spline overshoot. A fresh check includes every in-domain derivative root of the spline. At three meters, corrected continuous bounds are 0.0646924 and 0.0313355 m, rather than the node-only values 0.0432636 and 0.0306818. Both observed arc differences lie within the corrected bounds.

<div class="hy-model-table"><table><caption>Table 5. New checks on the conditional measured-data reconstructions.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Test 1</th><th scope="col">Test 2</th></tr></thead><tbody><tr><td>RK4 versus independent quadrature</td><td>2.85 × 10⁻¹⁴ m</td><td>3.18 × 10⁻¹⁴ m</td></tr><tr><td>Saved CSV rounding discrepancy</td><td>0.692 μm</td><td>0.692 μm</td></tr><tr><td>Arc-reference maximum difference</td><td>6.972 mm</td><td>2.838 mm</td></tr><tr><td>Continuous-spline bound</td><td>64.692 mm</td><td>31.335 mm</td></tr></tbody></table></div>

<div class="hy-model-table"><table><caption>Table 6. Evidence hierarchy.</caption><thead><tr><th scope="col">Evidence</th><th scope="col">What it checks</th><th scope="col">What it does not establish</th></tr></thead><tbody><tr><td>Calibration substitution</td><td>Formula and units</td><td>Physical calibration validity</td></tr><tr><td>Independent integration</td><td>Same assumed curvature field</td><td>Measured shape accuracy</td></tr><tr><td>Exact synthetic experiment</td><td>Noise-free reconstruction error</td><td>Sensing-system accuracy</td></tr><tr><td>Noise Monte Carlo</td><td>Chosen perturbation propagation</td><td>Empirical error distribution</td></tr><tr><td>Sign alternatives</td><td>Multiple compatible node magnitudes</td><td>Preferred physical sign pattern</td></tr></tbody></table></div>

<h2 id="discussion">11. Discussion</h2>

The study demonstrates why inverse geometry benefits from several kinds of evidence. Formula substitution catches scale errors; interpolation alternatives expose unmeasured between-node behavior; independent quadrature tests the stepper; a synthetic reference quantifies a controlled shape error; and sign reconfiguration reveals a limitation that all the numerical checks alone would miss.

The main remaining need is independent physical shape information. A tracked curve, orientation-sensitive sensing or a justified structural model could test the calibration and distinguish sign patterns. Repeated measurements under controlled temperature and loading would also help replace assumed wavelength-noise amplitudes with observed uncertainty.

Numerically, future refinement should compare at exact output locations and use a full-domain reference curvature in error decomposition. Sparse-node validation should distinguish interior omissions from extrapolated endpoints. Modeling changes should remain separate from fixed-pipeline noise propagation so improvements in one category are not misreported as certainty in another.

The original project files are preserved. New website figures and calculations are derived artifacts with a clearly stated relationship to the saved data, rather than revisions that silently replace the experiment.

<h2 id="conclusions">12. Conclusions</h2>

Under positive signs, prescribed initial pose and the given calibration, both measured-test curves are reproducible near circular arcs. Independent antiderivative–quadrature calculations confirm the numerical integration extremely closely, while a separate exact-curve experiment confirms small noise-free reconstruction error at 41 nodes.

The stronger conclusion is methodological: reliable computation does not eliminate sign, coordinate, calibration or pose uncertainty. Meter-scale sign alternatives and millimeter noise sensitivity remain meaningful even when numerical disagreement is near machine precision. The project therefore supports a carefully bounded reconstruction study, with its geometric assumptions, reference experiments and unresolved measurements made visible together.
