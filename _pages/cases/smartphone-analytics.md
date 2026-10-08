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
  - label: Study roadmap
    id: roadmap
  - label: Cross-section
    id: geometry
  - label: 3D geometry
    id: heading
  - label: Ideal slope
    id: ideal-plan
  - label: Real terrain
    id: terrain-plan
  - label: Validation
    id: validation
  - label: Discussion
    id: discussion
---

<style>
.hy-case-study .hy-equation { overflow-x: auto; font-size: 1.05rem; }
.hy-case-study .hy-multibeam-zoom { display: block; position: relative; background: #fff; border: 1px solid var(--hy-line); border-radius: 12px; overflow: hidden; }
.hy-case-study .hy-multibeam-zoom img { display: block; width: 100%; max-width: 100%; height: auto; margin: 0; }
.hy-case-study .hy-multibeam-zoom-label { display: block; padding: .5rem .85rem; text-align: right; font-size: .8rem; background: var(--hy-surface); color: var(--hy-teal); }
.hy-case-study .hy-multibeam-zoom:focus-visible { outline: 3px solid var(--hy-teal); outline-offset: 3px; }
.hy-case-study .hy-stage-map { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: 1rem; padding: 0; list-style: none; }
.hy-case-study .hy-stage-map li { padding: 1.05rem; border: 1px solid var(--hy-line); border-radius: 12px; background: var(--hy-surface); }
.hy-case-study .hy-stage-map strong { display: block; color: var(--hy-teal); margin-bottom: .3rem; }
.hy-case-study .hy-stage-map a { text-decoration: none; }
.hy-case-study .hy-stage-map p { font-size: .95rem; margin: 0; }
@media (max-width: 600px) { .hy-case-study .hy-stage-map { grid-template-columns: 1fr; } }
</style>

<h2 id="abstract">Abstract</h2>

Multibeam bathymetry measures a strip of seabed on each vessel pass. The strip changes with water depth, seabed slope, and heading, so uniform survey-line spacing can leave shallow areas unmeasured while oversampling deeper water. This study connects an analytical coverage model to a terrain-aware planning algorithm. Ray–plane intersections give the coverage width on a sloping cross-section; an effective-slope transformation extends the result to arbitrary headings on a planar seabed. For gridded terrain, edge rays intersect an interpolated depth surface, and a greedy placement rule adapts line spacing to local coverage. A separate interval-union evaluator checks the resulting plan.

On an ideal planar region, the constructed plan uses 34 lines and 68 nautical miles, with 10% overlap between adjacent swaths. On the supplied bathymetric grid, a selected north–south plan uses 63 lines and 315 nautical miles, achieving numerical full coverage under the stated geometry and evaluation resolution. Relative to a shallow-depth uniform-spacing baseline evaluated on the same domain, route length falls by 46.6% and excess-overlap length by 68.9%. These results support adaptive survey planning within the tested candidate set; they do not establish global optimality or field-validated measurement accuracy.

<aside class="hy-study-insight" aria-label="Study takeaway">
<p class="hy-label">Central idea</p>
<p>First understand the footprint of one sonar pass; then use that geometry to decide how an entire region should be surveyed.</p>
</aside>

<h2 id="background">1. Background: from a sonar fan to a survey plan</h2>

A multibeam survey vessel measures a strip of seabed on each pass. Its transducer emits a fan of rays in a vertical plane perpendicular to the direction of travel. The intersection between this fan and the seabed defines the coverage swath. Adjacent passes must cover the gaps between them, while repeated coverage consumes survey effort.

The difficulty is that the footprint is not fixed. A ray travels farther before meeting a deeper seabed, creating a wider swath. A slope changes the two edge intersections asymmetrically. A different heading changes both the slope seen by the fan and the depths encountered along the vessel's path. Consequently, a single spacing chosen for an entire region can be too wide in shallow water and unnecessarily narrow elsewhere.

<figure class="hy-research-figure hy-multibeam-cover">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
    <img src="{{ '/assets/img/research/multibeam/cover.webp' | relative_url }}" alt="Conceptual survey vessel sending a multibeam sonar fan toward an undulating seabed." width="1647" height="955" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 1.</span> The physical setting: a vessel-mounted fan covers a strip of seabed. This AI-generated illustration introduces the mechanism; it is not a reconstruction of the supplied terrain or an observed sonar measurement.</figcaption>
</figure>

This study asks how to translate that three-dimensional mechanism into a transparent planning procedure. It proceeds in four stages, increasing the complexity one step at a time. The first two stages explain coverage geometry; the third tests how it can guide line placement on an ideal slope; the fourth extends the calculation to a supplied depth grid.

The model treats the sea surface as a horizontal reference and the sonar fan as continuous geometric coverage. It neglects refraction, discrete beam footprints, vessel motion, tides, and navigation uncertainty. These assumptions isolate the layout problem. Coverage here means geometric coverage under the model, rather than a claim about acoustic detection probability or field measurement accuracy.

<h2 id="roadmap">Study roadmap</h2>

<ol class="hy-stage-map">
<li><a href="#geometry"><strong>A · Explain one cross-section</strong></a><p>Intersect the fan edges with a sloping seabed. Determine how depth changes width and why fixed spacing can create gaps.</p></li>
<li><a href="#heading"><strong>B · Account for heading</strong></a><p>Reduce the three-dimensional plane geometry to an equivalent cross-section with a heading-dependent effective slope.</p></li>
<li><a href="#ideal-plan"><strong>C · Plan an ideal region</strong></a><p>Use the coverage model to place contour-parallel lines with a prescribed overlap and a clear boundary stopping rule.</p></li>
<li><a href="#terrain-plan"><strong>D · Adapt to supplied terrain</strong></a><p>Interpolate the depth grid, intersect rays numerically, compare candidate plans, and evaluate the coverage union.</p></li>
</ol>

<figure class="hy-research-figure hy-multibeam-workflow">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
    <img src="{{ '/assets/img/research/multibeam/workflow.webp' | relative_url }}" alt="Four-panel infographic linking analytical cross-sections, effective-slope reduction, ideal-slope planning, and terrain-aware planning, followed by numerical checks." width="1774" height="887" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 2.</span> Overview of the method and its checks. Panel C concerns the ideal planar region; Panel D concerns the supplied-grid calculation. Terrain drawings and line counts shown visually are illustrative; the printed result values come from the computational study. Exact geometry, width conventions, and coverage definitions are specified below.</figcaption>
</figure>

<h2 id="geometry">2. Stage A: coverage on a sloping cross-section</h2>

### 2.1 The footprint of a single pass

The first task is deliberately local. Before placing any regional route, consider a vessel above a plane with a 1.5° slope and a 120° sonar opening angle. The sloping surface makes the shallow-side edge ray meet the bottom sooner than the deep-side ray. Treating these two distances separately is the key to a consistent coverage calculation.

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

### 2.2 Why a fixed spacing can fail

In the analytical example, nine line positions are separated by 200 m, with a 70 m reference depth. Moving across the slope changes depth from approximately 49.05 to 90.95 m. The widening swath changes the outcome even though the line spacing remains identical: the shallow pairs leave gaps, while deeper pairs overlap increasingly.

<figure class="hy-research-figure hy-multibeam-data">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/cross-section.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
    <img src="{{ '/assets/img/research/multibeam/cross-section.svg' | relative_url }}" alt="Recomputed swath widths across nine positions and adjacent geometric overlap ratios, including negative overlap in shallow water." width="1000" height="580" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 3.</span> A controlled demonstration of the spacing problem. Widths range from 170.33 to 315.81 m; adjacent overlap ranges from −11.17% to 33.64%. The first line has no preceding pair, so its overlap is not plotted.</figcaption>
</figure>

The implication is a planning principle rather than a final route: spacing should depend on the local footprint. A width formula is useful because it explains both failures—missing shallow water and repeatedly covering deep water—with the same geometric mechanism.

<h2 id="heading">3. Stage B: reduce three-dimensional geometry to an effective slope</h2>

### 3.1 What changes when the vessel turns?

A seabed has one physical slope, but the sonar fan sees a cross-section determined by the vessel's heading. The slope inside that section differs from the slope along the vessel's path. Separating those two effects avoids confusing a wider footprint with a change in depth encountered during travel.

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

### 3.2 Three interpretable heading cases

For the 120 m reference-depth example, a down-slope heading encounters increasing depths and widening coverage; an up-slope heading encounters decreasing depths and narrowing coverage. A contour-following heading stays at constant depth. Its cross-sectional slope is nonzero, but that slope and the footprint remain constant along the line.

<figure class="hy-research-figure hy-multibeam-data">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/heading.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
    <img src="{{ '/assets/img/research/multibeam/heading.svg' | relative_url }}" alt="Analytical swath width versus travel for down-slope, contour-following, and up-slope headings on the same planar seabed." width="1000" height="580" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 4.</span> Heading changes the depth encountered during travel. The contour-following case stays at approximately 416.69 m width; the other two cases widen or narrow. These curves use the archived analytical equations, not generated terrain imagery.</figcaption>
</figure>

This stage supplies a compact model for heading comparison. Agreement with direct three-dimensional intersections checks the reduction within the assumed plane geometry; it does not by itself validate the model against measured sonar data.

<h2 id="ideal-plan">4. Stage C: place survey lines on an ideal planar region</h2>

### 4.1 Define the region and the overlap convention

The next step moves from one pass to an entire region. The ideal domain measures 4 nautical miles east–west and 2 nautical miles north–south, with 110 m central depth and a 1.5° slope. Water is shallower toward the east and deeper toward the west. North–south lines follow its straight depth contours, so each line has constant depth along its length.

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

### 4.2 A boundary-aware greedy construction

The first line is positioned so that its shallow-side footprint just reaches the eastern boundary. Each subsequent line is placed as far toward deeper water as the 10% overlap constraint permits. The algorithm stops when the deep-side footprint covers the western boundary; the final line is not simply forced onto that boundary.

<figure class="hy-research-figure hy-multibeam-data">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/ideal-plan.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
    <img src="{{ '/assets/img/research/multibeam/ideal-plan.svg' | relative_url }}" alt="Actual computed positions of the 34 ideal-region lines and their changing horizontal spacing, with wider spacing in deep western water." width="1000" height="580" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 5.</span> The ideal-slope construction produces 34 lines of 2 nautical miles each: 68 nautical miles in total. Line spacing is denser in shallow eastern water and wider in deep western water. The numerical interval union has no gaps, and the 33 adjacent overlap ratios are approximately 10%.</figcaption>
</figure>

This controlled case shows how the local formula becomes a regional plan. The greedy argument applies within the specified contour-parallel family and overlap convention. It is not a demonstration that contour-parallel lines are globally shortest among arbitrary headings or curved routes. All lengths in this account exclude turns and transit between lines; one nautical mile equals 1,852 m.

<h2 id="terrain-plan">5. Stage D: plan on the supplied bathymetric grid</h2>

### 5.1 Replace the plane with a depth surface

The final case uses a different region: 4 nautical miles east–west by 5 nautical miles north–south. The supplied grid contains 251 × 201 samples, or 50,451 depth values, with 0.02 nautical mile spacing (37.04 m) and depths from 20 to approximately 197.2 m. Here a single slope no longer describes the whole seabed, and a straight north–south line need not follow a depth contour.

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

### 5.2 Comparing candidate plans

The outer search tests headings between −45° and 45°, with 5° spacing and 1° refinement near the selected direction. It also tests overlap lower bounds of 5%, 8%, 10%, and 12%. A missed-area tolerance of 0.1% defines admissibility; among admissible candidates, selection first minimizes the cumulative line length with overlap above 20%, then total line length. This is a chosen multi-objective priority, not a universal optimum criterion.

The selected plan has heading 0°—north–south—and a 5% design overlap lower bound. The 10% overlap rule belongs to the separate ideal-slope example; the terrain case does not require its local overlap to stay within 10–20%. Local terrain variation still produces substantial overlap above 20%, which is measured and reported rather than hidden.

### 5.3 Inspect the selected plan before comparing costs

The terrain plan uses 63 north–south lines of 5 nautical miles each, totaling 315 nautical miles. At the 9.26 m evaluation slice spacing, the independent interval-union calculation returns a missed-area proportion of about $4.9\times10^{-13}$, which is numerical zero for the reporting precision.

<figure class="hy-research-figure hy-multibeam-data">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/multibeam-overview.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
    <img src="{{ '/assets/img/research/multibeam/multibeam-overview.svg' | relative_url }}" alt="Supplied bathymetric grid with the computed 63 north–south lines, beside the 590 versus 315 nautical mile comparison." width="1000" height="580" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 6.</span> The actual supplied depth grid and selected line positions, introduced after the geometry and ideal-slope construction. The selected plan contains 63 straight north–south lines and totals 315 nautical miles. Both the selected plan and the shallow-depth baseline achieve numerical full coverage under the stated evaluator.</figcaption>
</figure>

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

### 5.4 Why the baseline matters

Uniform spacing based on the shallowest depth provides numerical full coverage but requires 118 lines. Relative to that admissible baseline, the selected terrain-aware plan reduces survey-line length from 590 to 315 nautical miles, a 46.6% decrease, and reduces excess-overlap length by 68.9%. The mean-depth baseline is shorter but leaves approximately 14.83% of the domain unmeasured; it is not an equivalent full-coverage alternative.

<figure class="hy-research-figure hy-multibeam-data">
  <a class="hy-multibeam-zoom" href="{{ '/assets/img/research/multibeam/multibeam-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size">
    <img src="{{ '/assets/img/research/multibeam/multibeam-comparison.svg' | relative_url }}" alt="Survey length and excess-overlap length for the selected terrain-aware plan and two uniform-spacing baselines." width="1000" height="580" loading="lazy">
    <span class="hy-multibeam-zoom-label">View full size ↗</span>
  </a>
  <figcaption><span>Figure 7.</span> Comparing efficiency requires a coverage condition. The 39-line mean-depth baseline is shorter but misses 14.83% of the region. Relative to the admissible shallow-depth baseline, adaptive spacing reduces survey length by 46.6% and excess-overlap length by 68.9%.</figcaption>
</figure>

The important distinction from Stage C is that terrain adaptation means changing the spacing of straight lines according to spatially varying footprints. It does not mean bending every line along a depth contour. The illustrated terrain in the workflow explains the procedure; Figure 6 provides the actual depth field and computed line coordinates.

<h2 id="validation">6. Numerical checks, sensitivity, and uncertainty</h2>

### 6.1 Check the equations and the coverage arithmetic

The study uses complementary checks rather than treating one performance number as validation of the whole system. Analytical cross-sections agree with numerical ray tracing to machine precision, and the heading-dependent model agrees with direct three-dimensional intersections. These checks establish implementation consistency within the assumed geometry.

Coverage is checked on cross-sections perpendicular to the survey heading. At each along-line station, the evaluator sorts the cross-track swath intervals, merges their union, and measures any remaining uncovered interval inside the region. This matters because a location may be covered by more than two swaths: subtracting only adjacent-pair overlaps would not recover the full union correctly.

### 6.2 Test evaluation resolution and interpolation

For the terrain plan, coverage interval ordering shows no violations in the evaluator. Refining evaluation spacing from 0.02 to 0.0025 nautical miles changes the reported excess-overlap length by about 47 m, or 0.015%, while missed area remains numerically zero. This is a resolution-sensitivity result, not a proof that no arbitrarily small gap exists in continuous space.

The archived strip-holdout experiment compares interpolation against withheld values from the supplied grid. Bilinear interpolation gives approximately 3.07 mm mean absolute error and 4.26 mm root mean squared error; the maximum is about 15 mm. These small values describe interpolation on this particular grid, not sonar accuracy or an independently measured seabed truth.

### 6.3 Distinguish fixed-plan noise from replanning

The archived fixed-plan perturbation experiment adds Gaussian depth noise with an assumed standard deviation of 0.5 m. Across 30 realizations, maximum missed area is approximately 0.000624% and the excess-overlap standard deviation is approximately 388 m. Replanning under perturbation is a separate experiment and does not demonstrate that the unchanged plan remains strictly gap-free. These noise results depend on the assumed perturbation model and have not been verified against field observations.

The assumed noise distribution is part of the experiment, not a measured sensor-error specification. A small missed-area percentage under perturbation is evidence of numerical sensitivity at that noise scale, while strict zero-gap coverage and operational reliability are different claims.

<h2 id="discussion">7. Discussion: what the study establishes</h2>

The useful connection is between local geometry and regional planning. An interpretable coverage formula explains why spacing should change with depth; the effective-slope transformation explains how heading changes the footprint; a numerical terrain model extends that logic beyond planar seabeds. The selected plan demonstrates that the resulting adaptive spacing can outperform a conservative uniform-spacing baseline under a common numerical evaluator.

The search remains restricted: headings are sampled, inner placement is greedy, and mixed-heading or curved routes are not exhaustively optimized. Therefore the result is a selected candidate within the tested design procedure, not a globally shortest survey or a proven optimum over all parallel-line placements. The ideal-slope greedy argument also applies within its specified contour-following line family.

Operational follow-up would include turn and transit costs, refraction and beam footprints, correlated terrain errors, vessel motion, and navigation uncertainty. An expanded search could vary the first-line position, compare mixed-heading plans, and report a Pareto frontier over missed area, excess overlap, and travel. Field validation would require independent soundings and an explicit survey-accuracy specification.

<p class="hy-source-note">Study record: the archived 2023 multibeam survey-planning manuscript, supplied bathymetric grid, Python implementation, and numerical output files. Core geometry and the selected route were recomputed for this web account; the extended convergence, interpolation, and noise experiments are reported from the archived records. This is an AI-assisted computational research note.</p>
