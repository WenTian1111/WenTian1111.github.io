---
layout: han-project
title: Multi-Object Localization of Rocket Debris
description: A numerical study of sonic-boom source localization, joint position–time estimation, multi-signal matching, and sensitivity to recording errors.
img: assets/img/projects/rocket/rocket_cover.png
importance: 2
category: research
discipline: Geometric modeling
period: "2024"
question: How can arrival-time recordings distinguish and locate several sonic-boom sources?
role: Sole author; mathematical modeling, numerical solution, and analysis
methods: Geometric constraints, nonlinear least squares, combinatorial matching, Monte Carlo analysis
outcome: Journal article · December 2024 · issue 6 · pages 1–24
card_summary: A numerical case study of seven monitoring stations and four sound sources, combining position–time estimation with signal association and error analysis.
image_alt: Overview of the numerical rocket-debris localization study
publication: true
contents:
  - label: Scope & contribution
    id: question
  - label: Position & time
    id: model
  - label: Multiple sources
    id: matching
  - label: Numerical results
    id: results
  - label: Uncertainty
    id: uncertainty
  - label: Limits
    id: limitations
---

<h2 id="question">The question and the scope</h2>

When several pieces of falling rocket debris produce sonic booms, ground stations may record several arrivals without knowing which sound belongs to which source. This creates two linked problems: **estimate where and when each boom occurred**, and **match observations across stations to the same source**.

I developed the mathematical formulation, MATLAB solution, numerical comparisons, and manuscript for this sole-authored study. The work proceeds from one source to four sources, then examines the effect of recording-time error.

The direct output is the estimated **airborne position at the time of the sonic boom**, not a field-validated ground-impact location. Recovering debris on the ground would require an additional trajectory or landing model.

<div class="row justify-content-center">
  <div class="col-md-7">
    {% include figure.liquid loading="lazy" path="assets/img/projects/rocket/devices_global.png" title="Seven monitoring stations in the numerical study" class="img-fluid rounded" %}
  </div>
</div>
<p class="caption">Station locations in the supplied numerical scenario. The study does not report a physical sensor deployment or a flight experiment.</p>

<h2 id="model">Estimating position and emission time together</h2>

The model relates the distance from a source to a station to the time taken by sound to travel between them. For station i, the basic constraint is:

<div class="hy-equation" role="math" aria-label="Distance between source position p and station position s i equals sound speed c times arrival time t i minus emission time t zero">‖p − sᵢ‖ = c(tᵢ − t₀)</div>

Here, p is the unknown source position, sᵢ is a known station position, tᵢ is its recorded arrival time, and t₀ is the unknown boom time. The numerical problem assumes a constant propagation speed of **340 m/s**.

The three spatial coordinates and emission time give **four unknowns**. Four independent arrival measurements are therefore a minimum equation-count requirement for this formulation; they do not alone guarantee a unique or stable solution. Station geometry, initialization, and physical constraints also matter.

I used a WGS84-based coordinate formulation to prepare the station geometry and MATLAB's <code>lsqnonlin</code> to solve the nonlinear residual equations. The manuscript's coordinate treatment is approximate; it should not be treated as a fully validated geodetic positioning system.

<div class="row justify-content-center">
  <div class="col-md-7">
    {% include figure.liquid loading="lazy" path="assets/img/projects/rocket/sphere_intersection.png" title="Geometric illustration of sphere-intersection constraints" class="img-fluid rounded" %}
  </div>
</div>
<p class="caption">Sphere-intersection geometry motivates the distance constraints. The unknown emission time must be estimated together with position.</p>

For the single-source example, I selected stations A, B, E, and G based on their spatial separation. This was a geometric selection heuristic, not an exhaustive demonstration of the globally optimal four-station subset.

<h2 id="matching">Associating arrivals from multiple sources</h2>

With four arrivals at each of four selected stations, choosing one arrival per station produces **4⁴ = 256 candidate combinations** for a source. In the multiple-source example, the selected stations are A, B, F, and G.

The matching procedure has three stages:

1. Enumerate one arrival from each selected station.
2. Solve the position–time equations for each candidate and screen the solutions using physical and temporal constraints.
3. Check cross-source consistency so that the selected combinations associate the recordings with four distinct sources.

The manuscript reports **73 candidates after the initial screening**, followed by correspondence analysis to select four source assignments. The 73 candidates are intermediate possibilities, not 73 identified debris pieces.

<div class="row justify-content-center">
  <div class="col-md-8">
    {% include figure.liquid loading="lazy" path="assets/img/projects/rocket/problem3_matching.png" title="Visualization of four inferred sonic-boom sources" class="img-fluid rounded" %}
  </div>
</div>
<p class="caption">Visualization of the four inferred sources after arrival-time association in the numerical example.</p>

<h2 id="results">Numerical case-study results</h2>

The four-source solution reported in the manuscript is summarized below. These coordinates and times are **model estimates for the problem dataset**, not independently measured ground truth.

<div class="hy-table-scroll" role="region" aria-label="Four-source localization results" tabindex="0">
  <table>
    <caption>Reported four-source solution · manuscript Table 11</caption>
    <thead><tr><th scope="col">Source</th><th scope="col">Longitude °E</th><th scope="col">Latitude °N</th><th scope="col">Altitude (m)</th><th scope="col">Boom time (s)</th></tr></thead>
    <tbody>
      <tr><th scope="row">1</th><td>110.318</td><td>27.640</td><td>25,931.21</td><td>20.159</td></tr>
      <tr><th scope="row">2</th><td>110.493</td><td>27.331</td><td>21,900.58</td><td>18.374</td></tr>
      <tr><th scope="row">3</th><td>110.678</td><td>27.672</td><td>12,271.43</td><td>17.567</td></tr>
      <tr><th scope="row">4</th><td>110.557</td><td>27.893</td><td>11,030.54</td><td>15.300</td></tr>
    </tbody>
  </table>
</div>

The value of the exercise is the linked workflow: a nonlinear localization model and a correspondence search must work together. A small fitting residual is not sufficient evidence that the chosen correspondence or geographical estimate is correct.

<h2 id="uncertainty">What recording errors change</h2>

The error study adds recording noise with a **0.5-second standard deviation**, applies a weighted least-squares formulation, and uses Monte Carlo reasoning to examine sensitivity. A standard deviation is not a hard ±0.5-second bound.

The manuscript's example comparison shows noticeable altitude changes: approximately **0.20–2.05 km** across the four estimated sources. This makes uncertainty a central part of the result; it does not support a claim of uniformly high-precision localization.

<div class="row justify-content-center">
  <div class="col-md-8">
    {% include figure.liquid loading="lazy" path="assets/img/projects/rocket/problem4_error.png" title="Numerical localization under perturbed recording times" class="img-fluid rounded" %}
  </div>
</div>
<p class="caption">A numerical comparison under perturbed recording times. Reported examples illustrate sensitivity rather than a guaranteed error bound.</p>

The study proposes more stations and a wider, better-conditioned layout as ways to add redundancy when timing precision cannot be improved. These are directions for further evaluation, not guarantees that adding any station will improve the estimate.

<h2 id="limitations">Limits and a stronger follow-up study</h2>

- **Propagation model:** constant-speed, point-source distance constraints simplify the behavior of a moving supersonic source and atmospheric propagation.
- **Coordinate consistency:** the approximate coordinate treatment needs further validation before precision claims are made.
- **Combinatorial cost:** exhaustive arrival matching becomes expensive as the number of recordings grows.
- **Solver behavior:** nonlinear least squares may converge to local solutions; initialization and alternative solutions need explicit testing.
- **Validation:** the study uses numerical problem data. Physical measurements, independently known source positions, and an evaluated landing model would be needed for operational recovery claims.

A follow-up would separate coordinate validation, signal association, and source estimation into independently testable stages, then evaluate uncertainty under more realistic noise and propagation conditions.

<h2 id="publication">Publication</h2>

Han Yang. “Research on Multi-Object Localization of Rocket Debris.” _Frontier and Progress of Computational Mathematics and Modeling_, December 2024, no. 6, pp. 1–24. ISSN 2313-4194.

[View publications]({{ '/publications/' | relative_url }})

<p class="hy-source-note">Research record: the 24-page manuscript, especially Sections 3 and 5–7. Publication month, issue, and page range follow the journal's publication notice dated December 1, 2024.</p>
