---
layout: han-project
title: "Multi-Object Localization of Rocket Debris"
description: "From a single sound source to four unlabeled arrival sequences: a numerical study of space–time localization, signal association, and timing sensitivity."
permalink: /projects/rocket_debris_localization/
img: assets/img/projects/rocket/rocket_cover.png
importance: 2
category: research
discipline: Applied mathematics · Inverse problems
period: 2024
question: How can ground-station arrival times reveal where several sound events occurred—and which measurements belong together?
role: Sole author — mathematical modeling, numerical analysis, and manuscript
methods: Space–time constraints, nonlinear least squares, candidate enumeration, weighted fitting, timing sensitivity
outcome: Four-source numerical case study · Research article
card_summary: "Seven stations, four unlabeled sound sources, and one coupled inference problem: estimating position and emission time while resolving arrival identities."
image_alt: Geometric illustration of multi-object localization
publication: true
contents:
  - label: Abstract
    id: abstract
  - label: 1. Research question
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: 3. Measurements and coordinates
    id: measurements
  - label: "4. Stage A: locate one source"
    id: single-source
  - label: "5. Stage B: associate arrivals"
    id: association
  - label: "6. Stage C: locate four sources"
    id: multiple-sources
  - label: "7. Stage D: timing sensitivity"
    id: uncertainty
  - label: 8. Interpretation and limitations
    id: discussion
  - label: 9. Further development
    id: next-steps
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Ground stations can record the arrival of acoustic events produced by returning rocket debris, but an arrival timestamp does not directly reveal the source position. The emission time is also unknown. When several sources are present, the stations record multiple timestamps without source labels: the first arrival at one station may correspond to the last arrival at another. This study treats localization and measurement association as connected inverse problems.

The analysis develops in four stages. A constant-speed propagation model first estimates the three spatial coordinates and emission time of one source. The same model is then applied to candidate combinations of unlabeled arrivals. Compatible combinations are selected for a four-source case, before a weighted-fitting formulation examines the effect of timing errors. The manuscript uses seven supplied monitoring stations and selects four for each main localization calculation.

The single-source example reports a mean position of 110.588° E, 27.163° N, and 987.16 m altitude, with emission time 4.568 s. In the multiple-source example, 256 candidate arrival tuples lead to a reported shortlist of 73 candidates and a selected four-source assignment. Reported emission times span 4.859 s, within the stipulated five-second window. A separate timing-error comparison produces horizontal changes smaller than 0.7 km under the supplied distance approximation, while altitude changes reach about 2.05 km. These results motivate examining geometry, source identity, and vertical sensitivity together.

<aside class="hy-study-insight" aria-label="Research insight">
<p class="hy-label">Central idea</p>
<p>A timestamp is useful only after its source identity is understood. The geometric fit and the arrival assignment must support the same explanation of the observations.</p>
</aside>

<h2 id="background">1. Research question: what can an arrival tell us?</h2>

Recovering returning debris provides the practical motivation, but the quantity estimated here is more specific: the position and time of an airborne sound-emission event. Ground-impact coordinates, a complete descent trajectory, and a moving shock-wave front would require additional physical modeling. The study uses an idealized point source whose disturbance propagates at a constant 340 m/s.

A nearby station receives a disturbance after a short travel time; a more distant station receives it later. Yet the travel time is not the recorded timestamp itself. It is the difference between the recorded arrival and the unknown emission time. This distinction adds a fourth unknown to an otherwise three-dimensional positioning problem.

With one source, every timestamp already belongs to the same event. With four sources, that correspondence is absent. Sorting the arrivals chronologically at each station gives an ordering of measurements, not a shared ordering of source identities. A valid explanation must both fit travel times and assign the observations consistently.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/measurement-geometry.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/rocket-study/measurement-geometry.svg' | relative_url }}" alt="Conceptual station-to-source distances with an unknown emission time" width="680" height="380" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual measurement geometry for the single-source case. The illustration explains the unknowns; it is not a recovered trajectory or measured terrain.</figcaption></figure>

The manuscript describes this geometry as a “four-sphere” model. That description is useful if the radii are understood to depend on the unknown emission time. Four observations supply the minimal equation count for four unknowns; they do not, by themselves, establish a unique or well-conditioned solution.

<h2 id="roadmap">2. Study roadmap</h2>

The analysis begins with a single event so the geometric model can be understood before introducing association ambiguity. It then reuses that model for one candidate arrival tuple at a time, compares compatible candidates, and studies changes under perturbed timing measurements. Each stage adds one source of difficulty rather than replacing the preceding question.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/study-roadmap.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/rocket-study/study-roadmap.svg' | relative_url }}" alt="Four-stage sequence from single-source fitting through arrival association to timing sensitivity" width="680" height="525" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Study roadmap, redrawn from the archived manuscript. The stages separate geometric inference, measurement association, and sensitivity analysis.</figcaption></figure>

The archived workflow combines MATLAB fitting with spreadsheet-assisted candidate comparison. The website presents this sequence as a research method; it does not imply that the supplied folder contains a fully automated, independently reproduced localization service.

<h2 id="measurements">3. Measurements and coordinate preparation</h2>

Each monitoring station has a longitude, latitude, altitude, and one or more recorded arrival times. The single-source case provides one timestamp per station. The multiple-source case provides four timestamps per station, with the additional condition that the four emission times differ by no more than five seconds.

The two cases use different station-coordinate tables. For example, Station F is at 27.921° N in the single-source case and 28.081° N in the multiple-source case; Station G changes from 27.121° N to 27.521° N. These are separate supplied inputs. Combining a station location from one case with an arrival from the other would change the inverse problem.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/station-layouts.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/rocket-study/station-layouts.svg' | relative_url }}" alt="Separate geographic station layouts for the single-source and multiple-source input cases" width="792" height="403.2" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Two supplied station layouts and the subsets selected in the manuscript. Both panels use the same geographic axis limits; shaded terrain is not inferred.</figcaption></figure>

The manuscript selects A, B, E, and G for the first case and A, B, F, and G for the second. Spreading stations across the observation region is a sensible geometric consideration, but the archive does not compare every possible four-station subset against a common error criterion. The selections should therefore be read as the study's chosen subsets rather than proven optimal layouts.

<div class="hy-model-table"><table><caption>Selected multi-source stations and their recorded arrivals, before assigning source identities.</caption><thead><tr><th scope="col">Station</th><th scope="col">Longitude / latitude</th><th scope="col">Altitude</th><th scope="col">Four arrivals (s)</th></tr></thead><tbody><tr><td>A</td><td>110.241° E / 27.204° N</td><td>824 m</td><td>100.767, 164.229, 214.850, 270.065</td></tr><tr><td>B</td><td>110.783° E / 27.456° N</td><td>727 m</td><td>92.453, 112.220, 169.362, 196.583</td></tr><tr><td>F</td><td>110.467° E / 28.081° N</td><td>678 m</td><td>67.274, 166.270, 175.482, 266.871</td></tr><tr><td>G</td><td>110.047° E / 27.521° N</td><td>575 m</td><td>103.738, 163.024, 206.789, 210.306</td></tr></tbody></table></div>

Distance calculations require spatial coordinates in consistent units. The archived manuscript uses ellipsoid-based expressions for horizontal coordinates and retains height as the vertical coordinate:

<div class="hy-equation">
\[
\begin{aligned}
x_i&=(N_i+h_i)\cos\phi_i\cos\lambda_i,\\
y_i&=(N_i+h_i)\cos\phi_i\sin\lambda_i,\\
z_i&=h_i,\\
N_i&=\frac{a}{\sqrt{1-e^2\sin^2\phi_i}}.
\end{aligned}
\tag{1}
\]
</div>

Here $\lambda_i$, $\phi_i$, and $h_i$ denote longitude, latitude, and height; $a$ and $e$ are the reference ellipsoid's semi-major axis and eccentricity. This is the coordinate expression documented in the manuscript. Because its vertical coordinate is height, it is not the complete Earth-centered, Earth-fixed transformation. The distinction matters when interpreting three-dimensional distances. Horizontal scaling in the archived tables must also be undone before combining coordinates with heights in metres.

For a display of horizontal differences, the supplied problem uses 97.304 km per degree of longitude and 111.263 km per degree of latitude. Those factors are used only for the approximate displacement comparison below. A rebuilt solver should use a single documented coordinate frame and consistent units throughout.

<h2 id="single-source">4. Stage A: locate one sound source</h2>

Let $\mathbf{s}_i$ be a station's spatial position and $\mathbf{p}$ the unknown source position. An arrival time $t_i$ is the sum of the emission time $t_0$ and the modeled travel time. The corresponding distance constraint is

<div class="hy-equation">
\[
\begin{aligned}
t_i&=t_0+\frac{\|\mathbf{p}-\mathbf{s}_i\|}{c},\\
\|\mathbf{p}-\mathbf{s}_i\|&=c(t_i-t_0),
\\ c&=340\ \mathrm{m/s}.
\end{aligned}
\tag{2}
\]
</div>

For a proposed emission time, each station defines a sphere centered on its location. Changing that time changes every radius. The inverse problem is thus to fit the position and time together, with the physical requirement that emission precedes reception. Counting equations is only a starting point: station geometry, numerical initialization, and the admissible domain affect the solution.

The manuscript solves the nonlinear system using MATLAB's `lsqnonlin`. A travel-time residual expresses the fitting problem directly. Let $\theta=(\mathbf{p},t_0)$ collect the four unknowns:

<div class="hy-equation">
\[
\begin{aligned}
r_i(\mathbf{p},t_0)
&=t_i-t_0-\frac{\|\mathbf{p}-\mathbf{s}_i\|}{c},\\
\widehat\theta
&\in\operatorname*{arg\,min}_{\theta}
\sum_i r_i(\mathbf{p},t_0)^2.
\end{aligned}
\tag{3}
\]
</div>

Equation (3) makes the residual interpretable in seconds. Exact roots also satisfy the paper's squared-distance equations, but minimizing squared-distance residuals and minimizing travel-time residuals need not produce the same answer when observations are noisy. The archive does not contain a runnable solver that would establish which residual scaling was used in every reported calculation.

<div class="hy-model-table"><table><caption>Four initialization runs reported for the single-source calculation.</caption><thead><tr><th scope="col">Run</th><th scope="col">Longitude</th><th scope="col">Latitude</th><th scope="col">Altitude (m)</th><th scope="col">Emission time (s)</th></tr></thead><tbody><tr><td>1</td><td>110.589951°</td><td>27.160875°</td><td>981.80</td><td>3.973066</td></tr><tr><td>2</td><td>110.587741°</td><td>27.164292°</td><td>978.60</td><td>4.766855</td></tr><tr><td>3</td><td>110.587695°</td><td>27.164326°</td><td>994.18</td><td>4.778151</td></tr><tr><td>4</td><td>110.587741°</td><td>27.164290°</td><td>994.05</td><td>4.754152</td></tr></tbody></table></div>

The manuscript averages these four outputs and reports 110.588° E, 27.163° N, 987.16 m, and 4.568 s. The neighboring outputs show how the numerical answers vary with initialization. Their average is the paper's reported summary; averaging nonlinear solutions is not itself a proof of improved accuracy or minimum residual.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/single-source-original.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/rocket-study/single-source-original.webp' | relative_url }}" alt="Original manuscript three-dimensional view of seven stations and the single-source estimate" width="1800" height="1200" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Original manuscript plot of the single-source case, compressed for web display. Its longitude, latitude, and altitude axes have different units and visual scales.</figcaption></figure>

This first stage establishes the reusable building block: given an associated set of arrivals, estimate one position and one emission time. The next stage asks how to obtain an associated set when the sources are unknown.

<h2 id="association">5. Stage B: associate unlabeled arrivals</h2>

Stations A, B, F, and G each record four arrivals. To construct a candidate explanation for one source, choose one arrival from each station. There are $4^4=256$ such tuples. This count refers to single-source candidate tuples; it is not the number of complete four-source assignments.

Every tuple is passed through the localization model to obtain candidate coordinates and an emission time. The manuscript reports retaining 73 candidates after screening, then importing the shortlist into Excel for comparison. Its written screening rule contains an inconsistent sign description, and the supporting workbook and executable filtering code are absent from the supplied folder. The shortlist size is consequently presented as an archived result, without inventing a precise screening threshold.

Selecting four candidates adds conditions that individual fits cannot enforce. Each arrival at a station must be assigned once, and the selected emission times must lie within the specified window. Writing $\pi_i(j)$ for the arrival index assigned to source $j$ at station $i$ gives

<div class="hy-equation">
\[
\begin{aligned}
\pi_i&\in S_4,\\
\max_j t_{0j}-\min_j t_{0j}&\le 5\ \mathrm{s}.
\end{aligned}
\tag{4}
\]
</div>

Here $S_4$ is the set of permutations of four arrival indices. The permutation condition prevents two sources from explaining the same arrival at a station. The time-window condition connects events observed at different locations. Neither condition alone validates the geometry; candidate residuals and physically admissible positions remain important checks.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/arrival-association.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/rocket-study/arrival-association.svg' | relative_url }}" alt="Arrival ranks cross across stations A, B, F, and G for the four assigned sources" width="792" height="388.8" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Source identities redrawn from the manuscript assignment table. Lines join the same source across stations and do not represent motion or a propagation path.</figcaption></figure>

In the manuscript's selected assignment, Source 1 arrives first at A, second at B and G, and fourth at F. Source 4 is the first arrival at F but the last at A and G. The crossing identity lines in Figure 5 illustrate why pairing timestamps solely by their sorted rank would fail.

<div class="hy-model-table"><table><caption>The selected arrival assignment, organized by source rather than chronological rank.</caption><thead><tr><th scope="col">Source</th><th scope="col">A (s)</th><th scope="col">B (s)</th><th scope="col">F (s)</th><th scope="col">G (s)</th></tr></thead><tbody><tr><td>1</td><td>100.767</td><td>112.220</td><td>266.871</td><td>163.024</td></tr><tr><td>2</td><td>164.229</td><td>196.583</td><td>175.482</td><td>103.738</td></tr><tr><td>3</td><td>214.850</td><td>92.453</td><td>166.270</td><td>206.789</td></tr><tr><td>4</td><td>270.065</td><td>169.362</td><td>67.274</td><td>210.306</td></tr></tbody></table></div>

The 266.871 s entry follows the supplied observations and the paper's station-by-station assignment table. A subsequent summary table prints 268.871 s for the same arrival. This presentation keeps the input-consistent value and does not silently reinterpret the discrepancy as a new measurement.

<h2 id="multiple-sources">6. Stage C: estimate four positions and emission times</h2>

After association, each source has its own four station observations. The single-source constraint is applied independently to each source, while the association and time-window conditions connect the four solutions:

<div class="hy-equation">
\[
\begin{aligned}
\|\mathbf{p}_j-\mathbf{s}_i\|
&=c\bigl(t_{i,\pi_i(j)}-t_{0j}\bigr),\\
i&\in\{A,B,F,G\},\\
j&\in\{1,2,3,4\}.
\end{aligned}
\tag{5}
\]
</div>

The selected numerical outputs are shown below. Keeping longitude, latitude, altitude, and time separate helps distinguish a geographic position from a temporal ordering. Source labels describe the selected assignment; they do not indicate the chronological order of emissions.

<div class="hy-model-table"><table><caption>Four-source estimates reported in manuscript Table 11.</caption><thead><tr><th scope="col">Source</th><th scope="col">Longitude</th><th scope="col">Latitude</th><th scope="col">Altitude (m)</th><th scope="col">Emission time (s)</th></tr></thead><tbody><tr><td>1</td><td>110.318° E</td><td>27.640° N</td><td>25,931.21</td><td>20.159</td></tr><tr><td>2</td><td>110.493° E</td><td>27.331° N</td><td>21,900.58</td><td>18.374</td></tr><tr><td>3</td><td>110.678° E</td><td>27.672° N</td><td>12,271.43</td><td>17.567</td></tr><tr><td>4</td><td>110.557° E</td><td>27.893° N</td><td>11,030.54</td><td>15.300</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/four-source-results.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
<img src="{{ '/assets/img/research/rocket-study/four-source-results.svg' | relative_url }}" alt="Reported four-source geographic positions, altitudes, and emission times in separate panels" width="900" height="403.2" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 6.</span> Selected estimates redrawn from manuscript Table 11. The geographic panel uses longitude and latitude; the altitude and time panels preserve their own units.</figcaption></figure>

The earliest reported emission is Source 4 at 15.300 s and the latest Source 1 at 20.159 s. Their difference is 4.859 s, satisfying the five-second condition. The corresponding altitude range is approximately 11.03–25.93 km. Checking the time span is an arithmetic consistency check on the saved table, not independent validation of the inferred positions.

All seven stations are available in the supplied case, but the reported main solve uses four. Requiring a candidate to predict the remaining stations' arrivals would add useful out-of-subset checks. Those comparisons should be made before calling an assignment globally unique or interpreting the number of displayed decimal places as positional precision.

<h2 id="uncertainty">7. Stage D: how do timing errors propagate?</h2>

Recorded arrivals need not be exact. The manuscript introduces zero-mean timing errors with standard deviation 0.5 s and proposes weighted least squares with repeated perturbation and fitting:

<div class="hy-equation">
\[
\begin{aligned}
t_i'&=t_i+\epsilon_i,\\
\mathbb{E}[\epsilon_i]&=0,\\
\operatorname{SD}(\epsilon_i)&=0.5\ \mathrm{s}.
\end{aligned}
\tag{6}
\]
</div>

At 340 m/s, 0.5 s corresponds to 170 m of modeled one-way travel distance. This is a range-error scale, not a guarantee that the position error is 170 m. Several unknowns are fitted simultaneously, and poorly constrained directions can amplify measurement errors.

The weighted objective gives each station's residual a specified influence. Here $r_i'(\theta)$ is the residual in Equation (3) evaluated with the perturbed arrival $t_i'$:

<div class="hy-equation">
\[
\begin{aligned}
\min_{\theta}\quad
&\sum_i w_i r_i'(\theta)^2,\\
&w_i>0.
\end{aligned}
\tag{7}
\]
</div>

If all stations have the same error variance, equal weights are a natural baseline. Unequal weights require a stated reliability or variance model. Weighting alone does not remove association errors, and a noisy refit can still depend on its starting point.

The manuscript discusses Monte Carlo sampling, but the supplied archive does not include the repeat-level results, sample count, random seed, or a documented confidence interval. What can be compared directly is its baseline table and its timing-error result table. Figure 7 redraws that comparison without converting it into an unreported probability distribution.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/rocket-study/timing-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size">
<img src="{{ '/assets/img/research/rocket-study/timing-sensitivity.svg' | relative_url }}" alt="Comparison of horizontal and vertical changes between baseline and perturbed reported outputs" width="792" height="388.8" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 7.</span> Changes calculated from manuscript Tables 11 and 12. Horizontal distance uses the supplied geographic approximation; bars summarize one reported comparison, not confidence intervals.</figcaption></figure>

Under the supplied longitude and latitude distance factors, horizontal changes are approximately 0.681, 0.348, 0.487, and 0 km. Altitude changes are −1.000, −0.200, −2.054, and −2.000 km. The zero horizontal change for Source 4 is based on coordinates rounded to three decimal places, so it does not establish an exactly unchanged horizontal solution.

The comparison is particularly informative vertically. Stations lie near ground level, while the reported sources are kilometres above them. Similar horizontal positions can coexist with substantial altitude changes. The saved example therefore supports examining vertical sensitivity separately; it does not justify a blanket claim that a 0.5 s error has negligible effect.

<h2 id="discussion">8. Interpretation and limitations</h2>

The study's main contribution is the connection between two tasks that are easy to separate prematurely: fitting a space–time source and deciding which arrivals belong to it. A good geometric fit for one arbitrary tuple is insufficient if the resulting collection reuses observations or violates the common emission window.

The single-source calculation provides a readable entry into that structure. Candidate enumeration extends it to unlabeled measurements, and the timing comparison shows that an apparently stable geographic location can conceal a sensitive altitude estimate. Together these stages form a coherent numerical case study, rather than a single final coordinate table without an explanation of how it was obtained.

The conclusions remain conditional on constant-speed point-source propagation, synchronized timestamps, the supplied station geometry, and the documented coordinate approximation. Atmospheric variation, refraction, multipath effects, moving shock-wave geometry, and a descent trajectory are outside the fitted model. Extra stations can provide redundancy, but their benefit depends on geometry and how their observations enter the fit.

There are also limits in the computational record. Candidate screening and spreadsheet-assisted selection cannot be independently reconstructed from the retained manuscript and images alone. Four equations do not prove global uniqueness. A reported fit is not field ground truth, and one perturbed comparison is not a Monte Carlo confidence bound. These distinctions define what the current results can support without discarding the useful modeling structure.

<h2 id="next-steps">9. Further development</h2>

A reproducible extension would first fix the coordinate convention and units, then preserve every candidate's initialization, residual, physical admissibility checks, and assigned arrival indices. Fitting with more than four stations would create an overdetermined system and allow the withheld observations to test candidate explanations.

The association stage can then be formalized as a joint comparison of assignments and fitted parameters, enforcing arrival non-reuse and the five-second window explicitly. Multiple starting points and comparison of competing assignments would be more informative than claiming uniqueness from a station-count argument.

For uncertainty, repeated timing perturbations should record the distribution of horizontal position, altitude, and emission time, along with the frequency of changed assignments. Sample count, noise distribution, weighting rules, and solver failures should be retained. This would distinguish sensitivity within one chosen assignment from uncertainty about source identity itself.

These are extensions proposed from the existing research record, not additional experiments claimed by this page. The present contribution is a numerical study of coupled localization and association, with a clearly traceable sequence from observations to selected estimates and sensitivity interpretation.

<p class="hy-source-note">Source basis: the supplied 24-page manuscript, its LaTeX source, and archived figures. New diagrams summarize the documented method; quantitative graphics are redrawn from manuscript tables. The original single-source plot is retained as a web-optimized copy. This update does not rerun the original solver or add independent field validation. Bibliographic information remains accessible through the site's existing publication record.</p>
