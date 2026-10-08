---
layout: han-project
title: Planar Curve Reconstruction from Fiber Sensors
description:
  From six optical sensor readings to a reconstructed planar curve, separating integration accuracy from the much larger uncertainty of curvature
  sign and measurement noise.
permalink: /projects/modeling/fiber-reconstruction/
discipline: Inverse geometry · Optical sensing
period: 2024 study
question: How much curve information can six local curvature measurements determine?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Wavelength–curvature conversion, spline interpolation, Frenet integration, convergence and noise tests
outcome: Six sensing nodes · numerical consistency · unresolved curvature-sign ambiguity
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: local sensing, global shape"
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: "3. Stage A: convert wavelength shifts to curvature"
    id: curvature
  - label: "4. Stage B: integrate curvature along material distance"
    id: integration
  - label: "5. Stage C: expose the sign ambiguity"
    id: sign
  - label: "6. Stage D: verify with a known curve"
    id: benchmark
  - label: "7. Stage E: distinguish measurement error from solver error"
    id: noise
  - label: 8. Discussion and reconstruction limits
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Reconstructing a curve from fiber-sensor readings is an inverse problem: local curvature measurements must be converted into a consistent global shape. This study uses six sensing nodes, converts wavelength shifts into curvature magnitude, interpolates the curvature field, and integrates the planar Frenet equations with a stated initial position and direction. It then compares integration methods, tests a known reference curve, and perturbs the measurements.

Under the all-positive curvature convention, the two supplied tests produce near-circular trajectories with mean curvatures about 2.2264 and 2.9795 m⁻¹. Integration methods agree to roughly $10^{-10}$ m, yet alternative curvature signs move the reconstructed endpoint by about 2.55 and 2.90 m. That difference defines the central result: numerical precision can be excellent while physical shape remains weakly identified.

<h2 id="background">1. Background: local sensing, global shape</h2>

Fiber Bragg grating measurements record wavelength shifts at a small number of material locations. A calibrated bending relationship can convert these shifts into local curvature information. The global shape emerges only after those local values are connected and integrated.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/fiber-reconstruction/cover.webp' | relative_url }}" alt="Conceptual fiber-sensor curve reconstruction" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual fiber-sensor curve reconstruction. The illustration is thematic and does not show a measured trajectory, calibrated sensor hardware, or a demonstrated accuracy level.</figcaption></figure>

The supplied records contain six nodes separated by 0.6 m along a 3 m material interval, with baseline and deformed wavelengths for two tests. The coordinate convention places the first node at material position zero. Assigning it to 0.6 m instead would require unsupported extrapolation near the beginning and would change the reconstruction problem.

The essential assumptions are planar bending, the supplied wavelength calibration, a known initial tangent, and a chosen curvature-sign convention. The numerical solution must retain all of them, because curvature magnitudes alone do not uniquely determine a signed planar shape.

<h2 id="roadmap">2. Study roadmap</h2>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/fiber-reconstruction/workflow.webp' | relative_url }}" alt="Measurement-to-shape workflow" width="1491" height="1055" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Measurement-to-shape workflow. The two output panels are labeled as schematic: Test 1 has lower average curvature and Test 2 higher average curvature. The plotted reconstructions below show the actual saved coordinates, including their near-circular wrapping.</figcaption></figure>

<h2 id="curvature">3. Stage A: convert wavelength shifts to curvature</h2>

At sensor $i$, the supplied calibration relates the wavelength shift to curvature magnitude. With the calibration factor 4,200 and the stated wavelength units, the resulting curvature is in inverse meters:

<div class="hy-equation">
\[
\kappa_i=4200\,\frac{\lambda_i-\lambda_i^0}{\lambda_i^0}.
\tag{1}
\]
</div>

The six Test 1 values lie near 2.22 m⁻¹; Test 2 values lie near 2.98 m⁻¹. Their means are approximately 2.2264 and 2.9795 m⁻¹, corresponding to local circular radii around 0.4492 and 0.3356 m.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/curvature.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/fiber-reconstruction/curvature.svg' | relative_url }}" alt="Curvature values derived from the saved wavelength inputs" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Curvature values derived from the saved wavelength inputs. Test 2 has the higher average curvature; both profiles are nearly constant across the six nodes.</figcaption></figure>

A cubic spline supplies curvature between the nodes. Values at the node locations remain tied to the measured input, while values between them depend on the interpolation assumption. PCHIP and piecewise-linear alternatives provide a comparison of that assumption. None adds independent shape observations.

<h2 id="integration">4. Stage B: integrate curvature along material distance</h2>

The independent variable is arc length $s$. A planar curve's tangent angle changes according to signed curvature, and the position advances in the tangent direction:

<div class="hy-equation">
\[
\frac{d\theta}{ds}=\kappa(s),\qquad \frac{dx}{ds}=\cos\theta(s),\qquad \frac{dy}{ds}=\sin\theta(s).
\tag{2}
\]
</div>

The initial conditions are $x(0)=y(0)=0$ and $\theta(0)=45^\circ$. They fix translation and rotation; without them, the same intrinsic curvature could describe many globally positioned curves. A fourth-order Runge–Kutta integration with step $10^{-4}$ m is compared against an independent adaptive DOP853 calculation.

The maximum saved differences are approximately $2.42	imes10^{-10}$ m and $1.42	imes10^{-11}$ m for the two tests. That demonstrates agreement between numerical integration schemes on the same interpolated signed-curvature input. It does not validate the calibration, recover an unknown sign, or measure physical shape accuracy.

<h2 id="sign">5. Stage C: expose the sign ambiguity</h2>

The supplied wavelength conversion does not identify the sign of curvature at each node. The main reconstruction adopts positive signs throughout. Since the mean curvature is high and nearly constant, the resulting curves wrap around near-circular paths: approximately 1.064 and 1.423 revolutions across the material interval.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/curves.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/fiber-reconstruction/curves.svg' | relative_url }}" alt="Saved all-positive-sign reconstructions compared with an alternating-sign convention" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Saved all-positive-sign reconstructions compared with an alternating-sign convention. Axes are geometric coordinates in meters; the alternative curves demonstrate structural ambiguity, not additional observed tests.</figcaption></figure>

The positive-sign endpoints are approximately (0.0971, 0.1540) m and (−0.3375, 0.5556) m. With the illustrated alternating-sign convention, endpoint displacement relative to those curves is about 2.55 and 2.90 m. These large differences dominate the integration discrepancy by many orders of magnitude.

This is not a numerical defect that can be fixed by a smaller time step. It is missing information in the inverse problem. A unique physical reconstruction would require signed bending information, additional sensor geometry, orientation constraints, or independent shape observations. Presenting only the smooth positive-sign curve would hide that requirement.

<h2 id="benchmark">6. Stage D: verify with a known curve</h2>

A separate benchmark uses a prescribed curve $y=x^3+x$ for $0\le x\le1$. Its analytical curvature provides an independent reference for checking interpolation and integration:

<div class="hy-equation">
\[
\kappa(x)=\frac{6x}{\left[1+(3x^2+1)^2\right]^{3/2}}.
\tag{3}
\]
</div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/verification.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/fiber-reconstruction/verification.svg' | relative_url }}" alt="Known-curve reconstruction and sensor-count convergence" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Known-curve reconstruction and sensor-count convergence. The benchmark supplies a true curve by construction; the two measured wavelength tests do not have that ground truth.</figcaption></figure>

The reference arc length is approximately 2.270732 m. With forty sampling nodes, the archived maximum reconstruction error is about $8.87	imes10^{-8}$ m and RMS error $5.65	imes10^{-8}$ m. An integration-only comparison gives approximately $5.34	imes10^{-10}$ m, showing that interpolation of the curvature field accounts for more of the remaining benchmark error.

Errors decrease strongly as sensor count increases, but the observed order varies across the tested range. It would be misleading to describe every part of the complete reconstruction pipeline as uniformly fourth order merely because its integration method is RK4. This benchmark is noise-free and has known signed curvature; it tests the numerical pipeline under those favorable assumptions.

<h2 id="noise">7. Stage E: distinguish measurement error from solver error</h2>

The uncertainty experiment perturbs wavelengths with independent uniform noise. For a half-width of 0.02 nm, 1,000 archived Monte Carlo runs give mean endpoint displacements of approximately 22.6 mm and 17.7 mm, with 95th percentiles about 43.8 mm and 33.1 mm. The largest saved displacements are approximately 60.8 and 47.5 mm.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/fiber-reconstruction/noise.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
<img src="{{ '/assets/img/research/fiber-reconstruction/noise.svg' | relative_url }}" alt="Archived mean endpoint displacement as the wavelength-noise half-width changes" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 6.</span> Archived mean endpoint displacement as the wavelength-noise half-width changes. This is a conditional Monte Carlo experiment using uniform perturbations, not a calibrated confidence interval for real hardware.</figcaption></figure>

At a half-width of 0.004 nm, mean displacements fall to roughly 4.5 and 3.3 mm. These remain far larger than the integration discrepancy. Under a fixed sign convention, spline, PCHIP, and linear interpolation differences are comparatively small; sign ambiguity is the more consequential structural uncertainty.

The simulated noise model is an assumption. Actual sensors can have calibration drift, correlated errors, temperature effects, and unequal precision. Those would need measured characterization before the endpoint spread could be used as a hardware accuracy claim.

<h2 id="discussion">8. Discussion and reconstruction limits</h2>

The project successfully links optical measurements to a reproducible curve-integration calculation. Its evidence is strongest when numerical agreement, interpolation error, noise sensitivity, and sign identifiability are reported separately.

For the two supplied tests, no independent true shape is available. Therefore, the page does not claim nanometer-level physical accuracy, even though integration methods agree at a very small numerical scale. The all-positive curves are conditional reconstructions, not unique recoveries of the observed fiber.

A useful next experiment would measure the shape independently, establish signed curvature through the sensor arrangement, and characterize actual wavelength uncertainty. Only then could the model's geometric accuracy be assessed against physical truth. The current work demonstrates a numerical reconstruction framework and clarifies what additional evidence that assessment requires.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
