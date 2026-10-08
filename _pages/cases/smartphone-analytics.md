---
layout: han-project
title: Multibeam Bathymetry & Survey Planning
description: From edge-ray geometry and a three-dimensional orientation model to adaptive
  survey spacing, explicit coverage evaluation, and independently checked terrain
  scenarios.
permalink: /projects/modeling/multibeam-bathymetry/
discipline: Marine surveying · Computational geometry
period: 2023 study
question: How should survey spacing adapt to water depth and terrain while keeping
  coverage claims numerically and physically explicit?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Ray–terrain intersection, effective-slope reduction, greedy spacing, interval-union
  evaluation, candidate and uncertainty analysis
outcome: 34 ideal-slope lines · 63 terrain lines · 315 NM survey length · independent
  geometric and coverage checks
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Geometry, inputs and assumptions
    id: scope
  - label: 3. Cross-section coverage
    id: cross-section
  - label: 4. Three-dimensional survey orientation
    id: heading
  - label: 5. Ideal-slope planning
    id: ideal-plan
  - label: 6. Terrain-aware formulation
    id: terrain
  - label: 7. Selected terrain plan
    id: real-plan
  - label: 8. Candidate selection and boundary effects
    id: selection
  - label: 9. Resolution and interpolation
    id: sensitivity
  - label: 10. Terrain uncertainty
    id: uncertainty
  - label: 11. Independent verification
    id: verification
  - label: 12. Discussion and conclusions
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

A multibeam sonar covers a strip of seabed whose width depends on local depth, seabed slope and survey orientation. A uniform spacing rule can therefore leave shallow-water gaps while producing excessive overlap in deeper water. This study follows that mechanism in stages: a two-dimensional ray-intersection model, a three-dimensional orientation reduction, contour-parallel planning on an ideal plane, and numerical planning on a supplied bathymetric grid.

For the ideal 4 × 2 nautical-mile area, a 10% adjacent-swath overlap rule generates 34 survey lines and 68 nautical miles of survey length. For a separate 4 × 5 nautical-mile terrain grid, the selected straight north–south family contains 63 lines totaling 315 nautical miles. Its evaluated missed area is numerically negligible; compared with a corrected, full-coverage shallow-depth spacing baseline, survey length is 46.61% shorter and cumulative excess-overlap length is 68.93% lower.

New checks independently reconstruct planar placement, solve 94 analytical ray cases by bracketed root finding, compare 70 terrain-edge intersections and merge coverage intervals at 465 stored slices. Archived resolution, interpolation and perturbation studies are interpreted separately. These results establish a reproducible geometric planning scenario within the tested candidate family. They do not establish field measurement accuracy, continuous coverage under unknown terrain, or global optimality over arbitrary routes.

<h2 id="introduction">1. Introduction</h2>

### 1.1 The planning question

A survey vessel does not measure every seabed point directly beneath its track. A fan of acoustic beams reaches to both sides, producing a depth-dependent swath. On a sloping seabed, the two edge beams meet different depths and travel different distances. The shallow-side reach is narrower than the deep-side reach. Designing tracks from one representative depth hides this asymmetry.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size"><img src="{{ '/assets/img/research/multibeam/cover.webp' | relative_url }}" alt="Supplied conceptual cover showing the vessel, sonar fan and seabed. It illustrates the research setting; the rendered seabed is not the supplied depth grid or a record of a field survey." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 1.</span> Supplied conceptual cover showing the vessel, sonar fan and seabed. It illustrates the research setting; the rendered seabed is not the supplied depth grid or a record of a field survey.</figcaption></figure>

The practical objective is to cover the modeled area with appropriately overlapping swaths while limiting survey effort. Three quantities must remain distinct: the length of vessel survey tracks, the proportion of area not covered, and cumulative along-track length where adjacent swaths overlap excessively. Minimizing one does not necessarily minimize the others.

### 1.2 A progression from mechanism to deployment

The cross-section model first explains why width changes. The orientation model then asks how a three-dimensional plane appears within the vertical sonar-fan plane. The ideal-slope calculation isolates spacing decisions under transparent geometry. Only after those mechanisms are established does the study introduce irregular bathymetry, interpolation, numerical intersections and candidate comparison.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size"><img src="{{ '/assets/img/research/multibeam/workflow.webp' | relative_url }}" alt="Supplied research roadmap. Panels progress from analytical geometry to ideal-slope and terrain-aware planning. The terrain image is conceptual; numerical results refer to the supplied grid. The verification band summarizes types of checks, whose specific evidence and limits are described below." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 2.</span> Supplied research roadmap. Panels progress from analytical geometry to ideal-slope and terrain-aware planning. The terrain image is conceptual; numerical results refer to the supplied grid. The verification band summarizes types of checks, whose specific evidence and limits are described below.</figcaption></figure>

This sequence prevents the final 63-line result from arriving before the reader understands the underlying coverage model. It also separates an idealized analytical example from the terrain calculation; their areas, depth trends and overlap settings differ.

<h2 id="scope">2. Geometry, inputs and assumptions</h2>

### 2.1 Coordinate and measurement conventions

Depth is positive downward. One nautical mile (NM) is 1,852 m. The nominal sonar opening angle is 120°, so each edge beam makes 60° with the vertical. The analytical plane has slope 1.5°. Its cross-section depth increases along the horizontal downslope coordinate.

<div class="hy-model-table"><table><caption>Table 1. Three distinct model settings.</caption><thead><tr><th scope="col">Setting</th><th scope="col">Inputs</th><th scope="col">Purpose</th></tr></thead><tbody><tr><td>Local cross-section</td><td>Center depth 70 m; nine positions from −800 to 800 m</td><td>Width and adjacent-track overlap</td></tr><tr><td>Oriented planar survey</td><td>Center depth 120 m; eight headings and eight travel distances</td><td>Orientation-dependent width</td></tr><tr><td>Ideal planning rectangle</td><td>4 × 2 NM; center depth 110 m</td><td>Analytical contour-parallel placement</td></tr><tr><td>Terrain planning rectangle</td><td>4 × 5 NM; 251 × 201 depth grid</td><td>Numerical adaptive spacing</td></tr></tbody></table></div>

### 2.2 Declared assumptions

The geometric model treats beams as straight rays in a homogeneous medium and the fan plane as vertical and perpendicular to the survey line. Vessel motion, refraction, sound-speed profiles, beam footprint size and detection quality are not estimated. Depth is a surface intersection rather than an acoustic signal model.

Ideal planning uses a plane, straight parallel lines and a specified overlap floor. Terrain planning keeps straight parallel lines but replaces the plane with a bilinear depth surface. Its interpolator clamps outside-domain queries to the nearest boundary. This explicit boundary extension allows edge rays to be evaluated but is not observed bathymetry beyond the supplied rectangle.

Track length counts survey-line chords only. Turns, transit, acceleration, obstacles and navigational restrictions are excluded. An apparent reduction in survey length is consequently not an established reduction in operational time or cost.

<h2 id="cross-section">3. Cross-section coverage</h2>

### 3.1 Intersect the two edge rays

Let D be the depth below the vessel, α the seabed slope and θ the sonar opening angle. The ray on the shallow side intersects the bed sooner than the ray on the deep side. Horizontal half-widths follow directly from intersecting each ray with the linear depth function:

<div class="hy-equation">
\[
a_L=\frac{D\sin(\theta/2)}{\cos(\theta/2)+\sin(\theta/2)\tan\alpha},\qquad a_R=\frac{D\sin(\theta/2)}{\cos(\theta/2)-\sin(\theta/2)\tan\alpha}.
\tag{1}
\]
</div>

Both denominators must remain positive for the intended intersections. The horizontal width and the distance measured along the sloping bed are related by:

<div class="hy-equation">
\[
W_h=a_L+a_R,\qquad W_{\mathrm{bed}}=\frac{W_h}{\cos\alpha},\qquad D(x)=D_0+x\tan\alpha.
\tag{2}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/cross-section.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size"><img src="{{ '/assets/img/research/multibeam/cross-section.svg' | relative_url }}" alt="Analytical cross-section and overlap behavior. Width measured along the seabed differs from its horizontal projection. Negative overlap indicates a geometric gap rather than a negative physical area." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 3.</span> Analytical cross-section and overlap behavior. Width measured along the seabed differs from its horizontal projection. Negative overlap indicates a geometric gap rather than a negative physical area.</figcaption></figure>

The nine reference positions have depths from 49.05 to 90.95 m and along-bed widths from 170.33 to 315.81 m. A fixed 200 m separation is too wide at shallow positions and comparatively conservative at deeper positions. The saved geometric overlap range is −11.17% to 33.64%.

### 3.2 Overlap must compare the actual neighboring edges

For neighboring tracks separated by horizontal distance d, the deeper-side reach of the previous swath combines with the shallower-side reach of the current swath:

<div class="hy-equation">
\[
\eta_i=\frac{a_{R,i-1}+a_{L,i}-d_i}{W_{h,i}}.
\tag{3}
\]
</div>

All distances in this ratio use the same horizontal metric. Dividing a horizontal overlap by along-bed width introduces an unnecessary cosine factor. The simpler expression 1 − d/W assumes a common width and symmetric alignment; it is not generally the correct neighboring-swath ratio on a slope.

The current archive includes a corrected overlap convention. This article uses the revised outputs rather than older backup results. Distinguishing a definition correction from a new optimization result makes the numerical history auditable.

<h2 id="heading">4. Three-dimensional survey orientation</h2>

### 4.1 Reduce the three-dimensional plane

Let β be the angle between the survey direction and the horizontal downslope direction. The sonar fan lies in the vertical plane perpendicular to the vessel's track. Restricting a planar seabed to this fan plane produces an effective cross-sectional slope:

<div class="hy-equation">
\[
\tan\alpha_{\mathrm{eff}}=\tan\alpha\,|\sin\beta|,\qquad D(t,\beta)=D_0+t\tan\alpha\cos\beta.
\tag{4}
\]
</div>

The width formula is then evaluated with the local depth and effective slope. For a contour-following direction, β = 90° or 270°, the vessel stays at constant depth. For downslope or upslope headings, depth changes strongly along the line even though the perpendicular fan section is flat.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/heading.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size"><img src="{{ '/assets/img/research/multibeam/heading.svg' | relative_url }}" alt="Orientation affects both the effective fan-section slope and the depth encountered along the track. The constant-depth contour-following cases and changing-depth slope-aligned cases are different geometric mechanisms." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 4.</span> Orientation affects both the effective fan-section slope and the depth encountered along the track. The constant-depth contour-following cases and changing-depth slope-aligned cases are different geometric mechanisms.</figcaption></figure>

### 4.2 Reference calculation and checks

Eight headings and eight travel distances from 0 to 2.1 NM generate 64 reference widths. The saved range is 62.90–768.48 m. At the central point, the contour-following width is approximately 416.69 m and remains constant along that ideal plane.

The new verification constructs a three-dimensional ray vector for each side, intersects it with the plane using bracketed root finding, and measures the distance between the resulting points. Seventy-two heading/depth cases agree with the effective-slope expression to approximately 3.4 × 10⁻¹³ m. This independent algebraic route tests the reduction; it does not introduce refraction or nonplanar terrain.

<h2 id="ideal-plan">5. Ideal-slope planning</h2>

### 5.1 Place the first and subsequent tracks

The ideal rectangle is 4 NM across the slope and 2 NM along the contours. Central depth is 110 m. Its east boundary is shallow, around 13 m, while the west boundary is deep, around 207 m. Let ξ measure distance from the shallow boundary toward deeper water.

The first line is placed so its shallow edge reaches the area boundary. Each next line uses the largest separation satisfying a 10% neighboring-swath overlap. The last deep edge must reach or pass the far boundary:

<div class="hy-equation">
\[
\xi_1=a_L(D(\xi_1)),\qquad a_R(D(\xi_{i-1}))+a_L(D(\xi_i))-(\xi_i-\xi_{i-1})=\eta_{\min}W_h(D(\xi_i)).
\tag{5}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/ideal-plan.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size"><img src="{{ '/assets/img/research/multibeam/ideal-plan.svg' | relative_url }}" alt="Ideal planar placement. Lines stay straight and parallel to depth contours; spacing increases toward deeper water. The overlap rule applies between neighboring swaths." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 5.</span> Ideal planar placement. Lines stay straight and parallel to depth contours; spacing increases toward deeper water. The overlap rule applies between neighboring swaths.</figcaption></figure>

A new closed recurrence independently reproduces the 34 archived placements within 0.00492 m, consistent with saved coordinates rounded to two decimals. All 33 neighboring overlap ratios are 10%. The last deep edge extends slightly beyond the rectangle; the model does not require an edge beam to stop exactly at the boundary.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/planar-recurrence.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size"><img src="{{ '/assets/img/research/multibeam/planar-recurrence.svg' | relative_url }}" alt="New independent planar reconstruction showing increasing depth and spacing. These coordinates come from a closed recurrence rather than the source placement solver." width="950" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 6.</span> New independent planar reconstruction showing increasing depth and spacing. These coordinates come from a closed recurrence rather than the source placement solver.</figcaption></figure>

### 5.2 Compare equivalent coverage tasks

<div class="hy-model-table"><table><caption>Table 2. Ideal-plane spacing strategies.</caption><thead><tr><th scope="col">Strategy</th><th scope="col">Lines</th><th scope="col">Survey length</th><th scope="col">Coverage behavior</th></tr></thead><tbody><tr><td>Adaptive 10% overlap</td><td>34</td><td>68 NM</td><td>No gaps; 10% adjacent overlap</td></tr><tr><td>Spacing from average depth</td><td>22</td><td>44 NM</td><td>Ten coverage gaps; unsuitable for full coverage</td></tr><tr><td>Spacing from shallowest depth</td><td>174</td><td>348 NM</td><td>No gaps; substantial excessive overlap</td></tr></tbody></table></div>

The short average-depth plan is not an equivalent full-coverage competitor. The shallow-depth plan meets coverage but spends many tracks on regions where wider spacing is feasible. Within the declared contour-parallel family, the adaptive rule advances as far as possible at each step while preserving the overlap requirement. This structure explains the efficiency of the constructed candidate; it is not a proof of minimum length over curved tracks, other orientations or multiple line families.

Raising the ideal overlap floor from 5% to 20% increases saved line counts from 33 to 39, or 66 to 78 NM. Increasing a safety margin has a quantifiable survey-effort cost.

<h2 id="terrain">6. Terrain-aware formulation</h2>

### 6.1 Replace the plane with a grid

The supplied terrain has 251 north–south rows and 201 east–west columns: 50,451 depth values spaced by 0.02 NM, or 37.04 m. Depth ranges from 20 to 197.2 m, with mean 62.54 m and standard deviation 29.79 m. There are no missing grid entries.

A fitted plane leaves residual standard deviation 19.68 m and maximum absolute residual 99.49 m. The grid therefore cannot be treated simply as the preceding ideal plane. Its broad eastward depth trend also differs from the east-shallow ideal planning example. The two cases demonstrate different settings rather than a single progressively enlarged dataset.

### 6.2 Numerical edge intersection

For vessel position p, a horizontal cross-track direction v and edge sign ±, the distance τ along the ray solves:

<div class="hy-equation">
\[
F_\pm(\tau)=\tau\cos(\theta/2)-D\!\left(\mathbf p\pm\tau\sin(\theta/2)\mathbf v\right)=0.
\tag{6}
\]
</div>

The source brackets intersections and performs 24 bisection iterations. Design samples are approximately 20 m apart along the survey line, with endpoints explicitly included. The new check instead uses SciPy's regular-grid interpolator with declared clamping and Brent's root solver. Seventy selected intersections across seven tracks and five along-track positions differ from saved edges by at most 1.754 × 10⁻⁶ m.

A conservative gradient bound is 0.058918. The ray derivative has a positive lower bound, cos(60°) − sin(60°)G ≈ 0.448975, for this bilinear surface and its clamped extension. This supports a unique intersection for the modeled edge rays. It does not guarantee that an acoustic system resolves all bottom returns or that unobserved terrain between grid points follows the interpolant.

<h2 id="real-plan">7. Selected terrain plan</h2>

### 7.1 Evaluate coverage as a union

At each along-track slice u, each swath contributes a cross-track interval Iᵢ(u). Intersecting those intervals with the area boundary and taking their full union avoids double-counting areas covered by three or more swaths:

<div class="hy-equation">
\[
A_{\mathrm{miss}}=\int\left|[v_{\mathrm{lo}}(u),v_{\mathrm{hi}}(u)]\setminus\bigcup_i I_i(u)\right|\,du,\qquad r_{\mathrm{miss}}=\frac{A_{\mathrm{miss}}}{A_{\mathrm{region}}}.
\tag{7}
\]
</div>

The selected plan uses straight north–south tracks with terrain-adaptive cross-track spacing. On an irregular surface these straight tracks do not literally follow every depth contour. The adaptation is in line spacing, not in bending the vessel path.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/multibeam-overview.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size"><img src="{{ '/assets/img/research/multibeam/multibeam-overview.svg' | relative_url }}" alt="Supplied depth grid and the selected 63 straight survey lines. The terrain-dependent spacing is visible across the rectangle. This is a computational coverage plan, not a recorded survey." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 7.</span> Supplied depth grid and the selected 63 straight survey lines. The terrain-dependent spacing is visible across the rectangle. This is a computational coverage plan, not a recorded survey.</figcaption></figure>

### 7.2 Quantitative outcome

The final plan has 63 lines of 5 NM each, totaling 315 NM. The saved evaluation at 9.26 m along-track spacing reports missed area at floating-point scale. Independent archived interval-union evaluation likewise reports a negligible residual, while a separate grid occupancy check reports zero uncovered cells.

<div class="hy-model-table"><table><caption>Table 3. Terrain plans after corrected endpoint evaluation.</caption><thead><tr><th scope="col">Plan</th><th scope="col">Lines</th><th scope="col">Survey length</th><th scope="col">Missed area</th></tr></thead><tbody><tr><td>Selected adaptive plan</td><td>63</td><td>315 NM</td><td>Numerically negligible</td></tr><tr><td>Shallow-depth fixed spacing</td><td>118</td><td>590 NM</td><td>Numerically negligible</td></tr><tr><td>Average-depth fixed spacing</td><td>39</td><td>195 NM</td><td>Approximately 14.83%</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/multibeam-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size"><img src="{{ '/assets/img/research/multibeam/multibeam-comparison.svg' | relative_url }}" alt="Length comparison under numerical full coverage. The corrected shallow-depth baseline totals 590 NM. The selected plan is 46.61% shorter; turns and transit are excluded from both values." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 8.</span> Length comparison under numerical full coverage. The corrected shallow-depth baseline totals 590 NM. The selected plan is 46.61% shorter; turns and transit are excluded from both values.</figcaption></figure>

Excess-overlap length is a separate diagnostic. It accumulates distance along adjacent line pairs where overlap exceeds 20%. The selected value is 318,664.38 m, or 172.065 NM, versus 1,025,693.16 m for the corrected shallow-depth baseline. This is not overlap area or unique vessel distance; multiple adjacent pairs may contribute at the same along-track location.

The archive's earlier baseline omitted endpoints, producing a false 0.2% coverage loss and chords of 9,240 rather than 9,260 m. Revised baseline outputs include both endpoints. The selected 63-line design is unchanged; using the corrected comparison is essential for the reported 46.61% and 68.93% reductions.

<h2 id="selection">8. Candidate selection and boundary effects</h2>

### 8.1 The selection rule

The direction search evaluates 19 coarse headings from −45° to +45°, then eight locally refined headings: 27 saved candidates. It is a finite candidate search within a prescribed angular window. Additional ±60° checks do not make the search exhaustive.

Candidates are first screened by a missed-area ceiling of 0.1%. Among admissible candidates, lower cumulative excess overlap is preferred, with total survey length breaking ties. This lexicographic choice is a declared planning preference, rather than a universal objective:

<div class="hy-equation">
\[
\text{admit }r_{\mathrm{miss}}\le 0.001;\qquad \operatorname{lexmin}\left(L_{\mathrm{excess}},L_{\mathrm{survey}}\right).
\tag{8}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/candidate-tradeoffs.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size"><img src="{{ '/assets/img/research/multibeam/candidate-tradeoffs.svg' | relative_url }}" alt="Saved heading feasibility and overlap-floor tradeoffs. The feasibility panel uses the tested parallel families; boundary completion and candidate design affect the interpretation of apparently unfavorable headings." width="958" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 9.</span> Saved heading feasibility and overlap-floor tradeoffs. The feasibility panel uses the tested parallel families; boundary completion and candidate design affect the interpretation of apparently unfavorable headings.</figcaption></figure>

At the selected north–south heading, an extended overlap-floor scan from 5% to 14% yields 63–70 lines and 315–350 NM. Excess-overlap length also rises. The 5% setting is selected for this terrain candidate family. It must not be confused with the 10% setting of the ideal-plane demonstration or described as a universal surveying requirement.

### 8.2 Boundary loss does not prove orientation infeasibility

Oblique parallel families in the saved scan lose coverage around clipped line ends. That is partly a boundary-completion problem, rather than evidence that the corresponding physical heading cannot cover the area. An archived augmented −5° candidate adds 18 cross-direction boundary lines, reducing missed area from 0.2348% to approximately 0.0810% at its stated grid resolution, while increasing total length to 386.34 NM.

This augmented result passes the 0.1% ceiling but belongs to a broader route family. Its stored excess-overlap diagnostic still refers to the original oblique family, so it is not a complete like-for-like excess-overlap comparison for the mixed plan. Relaxing the ceiling to 0.5% or 1% can instead select a different, shorter candidate with admitted gaps. These results show that conclusions depend on the area-loss tolerance, objective priorities and allowed boundary repairs.

<h2 id="sensitivity">9. Resolution and interpolation</h2>

### 9.1 Separate design resolution from evaluation resolution

The archived evaluation repeats the fixed plan at along-track steps of 0.02, 0.01, 0.005 and 0.0025 NM, or 37.04 down to 4.63 m. Missed area remains numerically negligible. Excess-overlap length ranges from 318,664.38 to 318,710.68 m, a span of 46.30 m, about 0.015% of the reported value.

Reducing design sampling from 20 to 10 m leaves the selected line count and placement behavior unchanged in the saved comparison. These tests support numerical stability over the tested resolutions. They do not prove coverage everywhere on a continuous, unknown seabed.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/resolution-and-interpolation.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size"><img src="{{ '/assets/img/research/multibeam/resolution-and-interpolation.svg' | relative_url }}" alt="Evaluation-step stability and interpolation cross-validation. The interpolation errors compare withheld grid values with predictions from remaining grid information, rather than sonar measurements with independent seabed truth." width="950" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 10.</span> Evaluation-step stability and interpolation cross-validation. The interpolation errors compare withheld grid values with predictions from remaining grid information, rather than sonar measurements with independent seabed truth.</figcaption></figure>

### 9.2 What interpolation validation measures

The saved strip holdout removes selected rows and columns, yielding 20,090 validation grid values at a 185.2 m spacing pattern. Nearest-neighbor interpolation gives RMSE 0.4767 m; bilinear interpolation gives 0.004264 m; bicubic interpolation gives 0.004467 m.

<div class="hy-model-table"><table><caption>Table 4. Saved withheld-grid interpolation errors.</caption><thead><tr><th scope="col">Method</th><th scope="col">MAE (m)</th><th scope="col">RMSE (m)</th><th scope="col">Maximum absolute error (m)</th></tr></thead><tbody><tr><td>Nearest neighbor</td><td>0.329794</td><td>0.476730</td><td>2.000</td></tr><tr><td>Bilinear</td><td>0.003070</td><td>0.004264</td><td>0.015</td></tr><tr><td>Bicubic</td><td>0.003664</td><td>0.004467</td><td>0.017745</td></tr></tbody></table></div>

The small bilinear error indicates that the supplied grid is smooth under this particular holdout test. It does not establish centimeter-scale physical bathymetric accuracy. Shared structure within one supplied grid, uncertainty in the original depths and the absence of independent field control remain relevant.

<h2 id="uncertainty">10. Terrain uncertainty</h2>

### 10.1 Keep the plan fixed before assessing robustness

Thirty archived scenarios add independent Gaussian grid perturbations with assumed standard deviation 0.5 m. The final 63-line geometry stays fixed. Every trial produces a small nonzero missed-area value: median 0.00037195%, 95th percentile 0.00058413%, and maximum 0.00062434%. Mean excess-overlap length is 318,890.324 m, with standard deviation 387.865 m.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/multibeam/terrain-uncertainty.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 11 at full size"><img src="{{ '/assets/img/research/multibeam/terrain-uncertainty.svg' | relative_url }}" alt="Two archived perturbation protocols under assumed 0.5 m grid noise. The first evaluates the existing plan; the second allows redesigned line placement. Their different protocols should not be merged into one robustness claim." width="950" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 11.</span> Two archived perturbation protocols under assumed 0.5 m grid noise. The first evaluates the existing plan; the second allows redesigned line placement. Their different protocols should not be merged into one robustness claim.</figcaption></figure>

### 10.2 Replanning is a different experiment

Ten separate archived scenarios allow a new plan after perturbing the depths. They retain the selected 5% overlap setting and produce 65 lines, totaling 325 NM, with numerically negligible evaluated missed area. This is approximately 3.17% more survey length than the unperturbed 315 NM plan.

<div class="hy-model-table"><table><caption>Table 5. Fixed versus adaptive response to assumed noise.</caption><thead><tr><th scope="col">Protocol</th><th scope="col">Trials</th><th scope="col">Plan treatment</th><th scope="col">Interpretation</th></tr></thead><tbody><tr><td>Fixed geometry</td><td>30</td><td>63 saved lines retained</td><td>Small admitted coverage losses under the assumed perturbations</td></tr><tr><td>Replanning</td><td>10</td><td>New line placement; 65 lines</td><td>Coverage recovered by changing survey effort</td></tr><tr><td>Noise model</td><td>Both</td><td>Independent Gaussian grid noise, σ = 0.5 m</td><td>Scenario assumption; not calibrated field uncertainty</td></tr></tbody></table></div>

Noise magnitude and spatial independence are assumptions. Spatially correlated depth error, systematic sound-speed bias, unknown terrain outside the rectangle and vessel-position uncertainty are not tested. Replanning also presumes that enough updated terrain information exists before the new survey. Thus the experiment demonstrates conditional response to a specified perturbation, not operational reliability under all measurement errors.

<h2 id="verification">11. Independent verification</h2>

### 11.1 New checks for this research note

The new audit preserves the original project and reconstructs critical quantities through separate code paths. Bracketed ray equations replace closed-form substitutions; a vector plane intersection checks the effective-slope reduction; a closed recurrence checks the ideal placement; a separate interpolator and root solver check selected terrain edges. Interval merging is independently performed on every stored design slice.

<div class="hy-model-table"><table><caption>Table 6. New independent checks and their scope.</caption><thead><tr><th scope="col">Check</th><th scope="col">Result</th><th scope="col">Limit</th></tr></thead><tbody><tr><td>22 cross-section edge cases</td><td>Maximum difference 5.69 × 10⁻¹⁴ m</td><td>Planar straight-ray geometry</td></tr><tr><td>72 three-dimensional cases</td><td>Maximum width difference 3.42 × 10⁻¹³ m</td><td>Planar orientation reduction</td></tr><tr><td>34 ideal placements</td><td>Maximum saved-coordinate difference 0.00492 m</td><td>Archive coordinates rounded to 0.01 m</td></tr><tr><td>70 terrain intersections</td><td>Maximum edge difference 1.754 × 10⁻⁶ m</td><td>Selected points on the same supplied grid</td></tr><tr><td>465 interval-union slices</td><td>Maximum uncovered width 0 m</td><td>Stored design slice locations</td></tr><tr><td>Original materials</td><td>354 source-file hashes unchanged</td><td>Read-only project preservation</td></tr></tbody></table></div>

### 11.2 Archived checks retained with attribution

The archive additionally reports 2,850 interior-beam checks with no edge-containment violations, a full interval-union evaluator and an independent occupancy check. The interval evaluator changes the coverage arithmetic but shares the source ray-intersection implementation. It is therefore useful cross-checking, not a wholly independent physical model.

The public article distinguishes these archived outputs from the fresh checks and from conceptual images. The new tests do not overwrite the original result files, regenerate the manuscript, or relabel a synthetic picture as a measured bathymetric surface. Publication does not require changing the preserved research archive.

<h2 id="discussion">12. Discussion and conclusions</h2>

The study supports a clear geometric conclusion: swath width should be evaluated at the local depth and cross-sectional slope, and track separation should use actual neighboring edge intersections. The ideal example makes the mechanism analytically visible. The supplied-grid example shows how the same reasoning can be transferred to numerical terrain intersections and interval-union coverage.

The selected 63-line plan is an effective candidate within its tested straight-line family. Its survey-length advantage over the corrected conservative baseline is substantial, while the average-depth shortcut fails the full-coverage task. Those findings are stronger when overlap definitions, endpoints, feasibility ceilings and cumulative-length metrics are stated explicitly.

Several extensions remain open. A broader route family could combine headings or curved tracks and handle boundary completion directly. Operational effort should include turns, transit and restrictions. Physical uncertainty should be calibrated against independent measurements and include correlated bathymetric error, vessel pose and sound-speed effects. Coverage evaluation should then be linked to actual measurement quality, rather than only a straight-ray footprint.

### Materials and evidence

This note is based on the original bathymetric grid, revised October 2026 result summaries, saved placement arrays, source geometry and evaluator implementations, interpolation holdouts and the two perturbation protocols in the local research archive. Newly drawn verification and sensitivity figures were created from those saved quantities or explicitly labeled independent calculations. The supplied cover and research roadmap are retained as conceptual illustrations. The note is a project research exposition; it does not claim field deployment or independent sonar accuracy validation.
