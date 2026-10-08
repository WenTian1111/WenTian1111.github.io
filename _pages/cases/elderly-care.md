---
layout: han-project
title: Healthy Aging & Equitable Care Networks
description: Country-level healthy-life profiles, transparent service rules, and a capacity-constrained regional network with independently checked
  feasibility and explicit evidence limits.
permalink: /projects/modeling/elderly-care/
discipline: Population data · Service-network modeling
period: 2024 study
question: How can descriptive aging indicators inform a transparent network scenario without being mistaken for causal policy evidence?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Data harmonization, clustering, out-of-fold random forests, capacity-constrained location, integer-programming benchmarks
outcome: 184 country profiles · 31 regional nodes · nine modeled centers · seven new integer-programming checks
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Data and comparability
    id: data
  - label: 3. Descriptive country profiles
    id: profiles
  - label: 4. Prediction and interpretation
    id: prediction
  - label: 5. Service rules and regional translation
    id: rules
  - label: 6. Network formulation
    id: network
  - label: 7. Selected compromise and benchmarks
    id: selection
  - label: 8. Optimization diagnostics
    id: diagnostics
  - label: 9. Assumption sensitivity
    id: sensitivity
  - label: 10. Uniform-growth scenario
    id: scenario
  - label: 11. Independent verification
    id: verification
  - label: 12. Discussion and conclusions
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Aging populations differ in health, resources and geographic access. This study separates three tasks: describing national contexts, predicting an aggregate healthy-life proxy, and exploring a regional service network under declared planning assumptions. An archived public-data pipeline produces 184 country profiles with eight features and a life-expectancy-minus-healthy-life-expectancy outcome at age 60. Clustering selects three descriptive profiles; five-fold out-of-fold random-forest predictions achieve R² 0.790 and RMSE 0.453 years. These results characterize associations in a mixed-year cross-sectional sample, rather than individual disability or treatment effects.

A separate 31-node regional scenario uses dependency-adjusted older-population weights, approximate travel times, normalized construction costs and whole-region capacity assignments. Its selected nine-center compromise covers 68.25% of modeled weight at cost 7.9201 and an unweighted travel-time Gini of 0.2062. New independent reconstruction reproduces all three objectives. Two fresh binary-programming benchmarks confirm the archived coverage and cost envelopes; five further solves substantiate low-count and low-capacity exclusions. Code inspection exposes an incorrectly signed hypervolume calculation and a service-tier boundary issue. The article preserves useful computational results while qualifying convergence, equity and the scale-invariant 2030 scenario.

<h2 id="introduction">1. Introduction</h2>

Older-age share is an important planning descriptor, but it is not a direct measure of unmet care. Two countries with similar age structure may differ in longevity, health-service capacity, income and family support. Conversely, a population with a lower older-age share may have substantial health burdens. A useful framework must explain which quantity is estimated before proposing where resources should be located.

National indicators first form descriptive profiles. A predictive model then estimates the difference between remaining life expectancy and healthy life expectancy at age 60. A rule layer proposes combinations of service intensity. Finally, a separate provincial-capital network examines coverage, construction cost and inequality in modeled access time.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size"><img src="{{ '/assets/img/research/elderly-care/cover.webp' | relative_url }}" alt="Supplied conceptual cover. Devices, people and services illustrate the theme; they do not document an implemented system or measured clinical outcomes." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 1.</span> Supplied conceptual cover. Devices, people and services illustrate the theme; they do not document an implemented system or measured clinical outcomes.</figcaption></figure>

The connection between these stages is conceptual rather than a validated transfer model. Country-level prediction is not an identified provincial treatment effect. The regional scenario has its own population and geography inputs; its demand multiplier comes from dependency structure rather than the random forest. Keeping these links explicit makes each stage independently assessable.

<h2 id="data">2. Data and comparability</h2>

### 2.1 Sources and sample construction

The saved extraction includes 217 World Bank economies, eight indicators and 21,371 records spanning 2010–2023, after removing aggregate regions. WHO supplies remaining life expectancy and healthy life expectancy at age 60. ISO3 identifiers align the sources. For each country and feature, the pipeline selects the latest available observation within the extraction period.

Countries are retained when the outcome is available and at most two of eight features are missing. Remaining feature gaps are filled with sample medians, producing 184 complete modeling rows. Fresh checks confirm that both WHO measures use 2023 for all retained rows, without within-row WHO year mismatch. Feature observations can nevertheless come from different years; a common outcome year does not make the full vector contemporaneous.

<div class="hy-model-table"><table><caption>Table 1. Data layers and roles.</caption><thead><tr><th scope="col">Layer</th><th scope="col">Saved scope</th><th scope="col">Interpretation</th></tr></thead><tbody><tr><td>Country features</td><td>184 rows × eight features</td><td>Latest feature snapshot; median filling allowed</td></tr><tr><td>WHO outcome</td><td>LE60 and HALE60, 2023</td><td>Aggregate healthy-life gap</td></tr><tr><td>Regional population</td><td>31 records, 2020 census basis</td><td>Separate population-structure scenario</td></tr><tr><td>Economic costs</td><td>2024 GDP-per-person snapshot</td><td>Normalized cost proxy</td></tr><tr><td>Geography</td><td>Provincial capitals and distances</td><td>Coarse spatial abstraction</td></tr></tbody></table></div>

### 2.2 Define the outcome before naming it

<div class="hy-equation">
\[
Y_i=\operatorname{LE60}_i-\operatorname{HALE60}_i.
\tag{1}
\]
</div>

The gap is measured in expected years. It is an aggregate proxy for years outside full health under the source definitions. It is not an observed individual disability duration, a count of patients requiring institutional care, or a nursing-workload estimate. Later service names should not imply clinical specificity absent from the country data.

Provincial inputs also differ in time and provenance. The archive records extraction dates and sources, including secondary mirrors for some tables. Aggregate plausibility checks do not replace row-by-row verification against original statistical releases. This note accordingly presents a reproducible planning scenario rather than an official needs assessment.

<h2 id="profiles">3. Descriptive country profiles</h2>

### 3.1 Standardization and profile selection

The features are older-age share, old-age dependency, log GDP per person, health expenditure, urban share, life expectancy at birth, physicians and hospital beds. Standardization prevents large numerical units from dominating distance. K-means is evaluated at three through six clusters, with the highest saved silhouette at three: 0.302, compared with 0.294, 0.265 and 0.241.

<div class="hy-equation">
\[
z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad \min_{\{\mu_k\}}\sum_i\|z_i-\mu_{c_i}\|_2^2.
\tag{2}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/country-profiles.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size"><img src="{{ '/assets/img/research/elderly-care/country-profiles.svg' | relative_url }}" alt="Rebuilt country profiles and cluster-selection scores. PCA is a display projection; clustering uses all eight standardized features. Separation is moderate rather than sharply categorical." width="1046" height="399" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 2.</span> Rebuilt country profiles and cluster-selection scores. PCA is a display projection; clustering uses all eight standardized features. Separation is moderate rather than sharply categorical.</figcaption></figure>

### 3.2 Read profiles through their features

The clusters contain 66, 57 and 61 countries. Mean older-age shares are approximately 3.80%, 18.65% and 7.19%; corresponding birth-life-expectancy means are 65.81, 79.62 and 74.65 years. Resource indicators also differ. Descriptive names such as younger/lower-resource, older/higher-resource and intermediate contexts summarize these particular observations.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/profile-contrasts.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size"><img src="{{ '/assets/img/research/elderly-care/profile-contrasts.svg' | relative_url }}" alt="Colors compare each feature across the three profile means. They do not convert different indicators into a common clinical severity scale." width="971" height="324" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 3.</span> Colors compare each feature across the three profile means. They do not convert different indicators into a common clinical severity scale.</figcaption></figure>

One hundred archived bootstrap refits give mean adjusted Rand agreement 0.864, with fifth percentile around 0.728. Each refitted model assigns the original standardized sample to its nearest centroid. This measures stability under resampling within the observed country pool. It does not test another year, alternative imputation, revised indicators or excluded countries.

The result is a reasonably stable descriptive partition with substantial within-profile variation. National categories should not assign an individual person a care package.

<h2 id="prediction">4. Prediction and interpretation</h2>

### 4.1 Out-of-fold prediction

A 500-tree random forest with minimum leaf size two predicts the healthy-life gap. Five shuffled folds ensure each saved prediction comes from a model that did not fit that country's outcome. Recalculation reproduces R² 0.790300 and RMSE 0.452824 years.

<div class="hy-equation">
\[
\operatorname{RMSE}=\sqrt{\frac1n\sum_i(\hat Y_i^{\mathrm{OOF}}-Y_i)^2}.
\tag{3}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/prediction-checks.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size"><img src="{{ '/assets/img/research/elderly-care/prediction-checks.svg' | relative_url }}" alt="Out-of-fold predictions and residuals. The residual panel shows over- and underestimation of the aggregate proxy, rather than service effectiveness." width="1046" height="399" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 4.</span> Out-of-fold predictions and residuals. The residual panel shows over- and underestimation of the aggregate proxy, rather than service effectiveness.</figcaption></figure>

Validation estimates cross-country prediction under a random split of this snapshot. It does not evaluate future-year forecasts, new-region transfer or individuals. Median filling happens before the folds in the original pipeline, so preprocessing is not fully isolated within training folds. A stricter evaluation should fit imputation inside each fold and add geographic or temporal holdouts.

### 4.2 Importance is not an intervention effect

The source computes impurity importance and permutation importance on a forest fitted to all rows. Birth-life expectancy ranks prominently. It is distinct from remaining life expectancy at age 60, but both are related population summaries; predictive strength may reflect shared longevity structure. This cannot establish that changing an indicator would causally reduce the outcome gap.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/predictive-importance.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size"><img src="{{ '/assets/img/research/elderly-care/predictive-importance.svg' | relative_url }}" alt="Two saved importance definitions. Permutation importance is evaluated on full-model training data; its magnitude is neither held-out explanatory power nor causal policy leverage." width="1046" height="418" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 5.</span> Two saved importance definitions. Permutation importance is evaluated on full-model training data; its magnitude is neither held-out explanatory power nor causal policy leverage.</figcaption></figure>

Relative tiers use prediction terciles near 4.529 and 5.597 years, yielding 61, 61 and 62 countries. These cut points divide this sample, not validated clinical categories. A country can change tier when the comparison population changes without its own health conditions changing.

<h2 id="rules">5. Service rules and regional translation</h2>

The nine-row service matrix crosses three profiles with three predicted-gap tiers. It proposes remote consultation, monitoring and household devices. These are design suggestions, not terms in the prediction loss or network objectives. No trial evaluates their benefits, adoption, staffing or cost-effectiveness.

Code inspection reveals a boundary issue. Percentile ranks of three profile income means are 1/3, 2/3 and 1. The archived integer-index rule assigns one profile to the standard package and two to the enhanced package; basic is never used. The nine rows therefore do not span all three intended equipment levels. This is documented rather than silently replacing the saved matrix.

<div class="hy-model-table"><table><caption>Table 2. Interpretation of service rules.</caption><thead><tr><th scope="col">Component</th><th scope="col">Saved output</th><th scope="col">Untested question</th></tr></thead><tbody><tr><td>Profile</td><td>Three national clusters</td><td>Transfer to local households</td></tr><tr><td>Priority tier</td><td>Relative prediction groups</td><td>Patient eligibility</td></tr><tr><td>Equipment package</td><td>One standard, two enhanced</td><td>Basic/standard/enhanced boundary rule</td></tr><tr><td>Frequency</td><td>Illustrative service schedule</td><td>Staffing and health effects</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size"><img src="{{ '/assets/img/research/elderly-care/workflow.webp' | relative_url }}" alt="Confirmed supplied workflow. Devices, maps and miniature curves are conceptual; numerical figures in this article are reconstructed from saved records." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 6.</span> Confirmed supplied workflow. Devices, maps and miniature curves are conceptual; numerical figures in this article are reconstructed from saved records.</figcaption></figure>

The regional exercise begins with separate provincial inputs. It does not transform national predictions into local patient totals. Instead, it adjusts older-population weights by relative dependency, encoding a hypothesis about support pressure that deserves separate sensitivity analysis.

<h2 id="network">6. Network formulation</h2>

### 6.1 Demand, distance and costs

There are 31 demand nodes and possible facilities at provincial capitals. Older-population weights are adjusted by dependency relative to the provincial mean, with baseline exponent γ=1. Weighted demand totals 20,810.283 in the archive's ten-thousand-unit scale. This is not a census count of distinct patients.

<div class="hy-equation">
\[
 w_i=P_i(d_i/\bar d)^\gamma,\qquad t_{ij}=1.3D_{ij}/70\ (i\ne j),\qquad t_{ii}=1.5\ \mathrm h.
\tag{4}
\]
</div>

Distance becomes travel time using an assumed road multiplier 1.3 and speed 70 km/h. Nonzero within-region time avoids treating a facility host as instantly served. Construction cost is GDP per person normalized by its regional mean. Budget 14 is thus a model scale rather than a currency estimate.

### 6.2 Indivisible regional demands

Binary y opens a facility and x assigns a region to at most one center. Regions are indivisible blocks. A region whose full weight exceeds remaining capacity is skipped, rather than partly served. Baseline capacity is 2,269.84 per center, at most twelve centers, a five-hour eligibility threshold and a 60% coverage floor.

<div class="hy-equation">
\[
\begin{aligned}\sum_jx_{ij}&\le1,&x_{ij}&\le y_j,\\\sum_iw_ix_{ij}&\le Cy_j,&\sum_jc_jy_j&\le B,\\\sum_jy_j&\le N_{\max},&x_{ij}&=0\ (t_{ij}>T_{\max}).\end{aligned}
\tag{5}
\]
</div>

The evolutionary search chooses facility sets with a deterministic decoder: process regions in descending weight, then choose the eligible center with greatest remaining capacity, breaking ties by time and index. This restricts allocation rather than optimizing every possible assignment for each facility set.

### 6.3 Distinct objectives and equity definitions

<div class="hy-equation">
\[
f_1=\sum_iw_i\sum_jx_{ij},\quad f_2=\sum_jc_jy_j,\quad G=\frac{\sum_{i,j}|A_i-A_j|}{2n\sum_iA_i}.
\tag{6}
\]
</div>

A is assigned travel time or a censored six-hour value for an unassigned region. G is **unweighted across regions**: small and large populations count equally, while coverage is population-weighted. Censoring compresses differences among poorly served regions. Both choices should be compared with population-weighted inequality and alternative censoring definitions.

<h2 id="selection">7. Selected compromise and benchmarks</h2>

### 7.1 Placement and loads

The compromise opens centers in Hebei, Liaoning, Heilongjiang, Zhejiang, Jiangxi, Shandong, Henan, Hunan and Chongqing. Independent decoding reproduces coverage 14,203.512829, cost 7.9201 and Gini 0.206163. Fifteen regions are assigned and sixteen unassigned. Maximum center load is 2,183.738, below capacity.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/regional-assignments.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size"><img src="{{ '/assets/img/research/elderly-care/regional-assignments.svg' | relative_url }}" alt="Capital-node assignment links, not road routes. Zhejiang and Chongqing host centers but their own whole-region demands remain unassigned under the saved decoder." width="1046" height="455" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 7.</span> Capital-node assignment links, not road routes. Zhejiang and Chongqing host centers but their own whole-region demands remain unassigned under the saved decoder.</figcaption></figure>

Opening a center does not force self-assignment; earlier large demands can consume its capacity. Facility count alone therefore does not identify which host populations receive service. Minimum local service would need another constraint or allocation rule.

<div class="hy-model-table"><table><caption>Table 3. Recomputed selected scenario.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Result</th><th scope="col">Meaning</th></tr></thead><tbody><tr><td>Facilities</td><td>9</td><td>Capital-node locations</td></tr><tr><td>Assigned / unassigned</td><td>15 / 16</td><td>Whole-region assignments</td></tr><tr><td>Weighted coverage</td><td>68.2524%</td><td>Adjusted-demand fraction</td></tr><tr><td>Cost</td><td>7.9201 / 14</td><td>Normalized proxy units</td></tr><tr><td>Time Gini</td><td>0.206163</td><td>Unweighted censored times</td></tr><tr><td>Largest load</td><td>2,183.738 / 2,269.84</td><td>Capacity feasibility</td></tr></tbody></table></div>

### 7.2 Objective-specific comparisons

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/network-tradeoffs.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size"><img src="{{ '/assets/img/research/elderly-care/network-tradeoffs.svg' | relative_url }}" alt="Archived candidates retain duplicate rows. Color represents time Gini; maximum-coverage MILP is an objective-specific reference, not an equity-matched alternative." width="1046" height="408" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 8.</span> Archived candidates retain duplicate rows. Color represents time Gini; maximum-coverage MILP is an objective-specific reference, not an equity-matched alternative.</figcaption></figure>

The uniform twelve-center reference covers 10,874.761 at cost 13.2495 and Gini 0.264773. The selected point improves all three saved quantities. Across 1,000 archived random configurations, mean coverage is 13,271.252 and maximum 16,150.752; selected coverage is around the 95.9th percentile, not better than every draw.

Two new independently built binary programs reproduce the saved envelopes. Free assignment with maximum coverage reaches 17,539.863989. Minimum cost at the selected coverage is 7.6721, giving a 3.23% relative cost gap from 7.9201. These benchmarks allow assignments beyond the greedy decoder. They bound individual objectives in a broader feasible model, without certifying a globally optimal three-objective compromise.

<h2 id="diagnostics">8. Optimization diagnostics</h2>

The source uses five seeds, binary crossover, mutation, feasibility repair, nondominated sorting and crowding distance. The compromise minimizes distance to the componentwise ideal after scaling by candidate-front ranges. This equal-weight rule is interpretable, but neither a demonstrated stakeholder preference nor a unique mathematical knee.

A convergence implementation issue changes the evidence. The monitoring routine divides negative coverage by total demand, while drawing comparison samples in a positive box. Every sample automatically passes the coverage-coordinate test. The quantity therefore depends on the cost–Gini projection and loses the coverage dimension.

<div class="hy-equation">
\[
u_{\rm archived}=(-f_1/W,\ f_2/B,\ G),\qquad u_{\rm comparable}=(1-f_1/W,\ f_2/B,\ G).
\tag{7}
\]
</div>

The identical final values 0.640211 cannot establish stable three-dimensional hypervolume or complete convergence. This does not invalidate the independently checked selected solution, but weakens stopping claims. A corrected search should monitor a consistently translated objective box and retain generation-level nondominated sets.

Five seeds selecting the same compromise is repeatability within this algorithm and decoder. It is narrower than full frontier exploration. A flawed stagnation monitor, shared repair rules and the same candidate representation can produce similar outcomes without resolving all competing objectives.

<h2 id="sensitivity">9. Assumption sensitivity</h2>

Archived one-at-a-time sweeps vary six parameters at eleven values each. Reduced searches use one seed, population 60 and a 120-generation cap. Their curves describe this search budget, not exact comparative statics of globally solved optima.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/assumption-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size"><img src="{{ '/assets/img/research/elderly-care/assumption-sensitivity.svg' | relative_url }}" alt="Lines join sampled search outputs. Crosses show coverage attained by greedy screening, not a mathematical upper bound. New exact checks substantiate the five exclusions separately." width="1039" height="568" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 9.</span> Lines join sampled search outputs. Crosses show coverage attained by greedy screening, not a mathematical upper bound. New exact checks substantiate the five exclusions separately.</figcaption></figure>

The original feasibility screen constructs a greedy solution, which supplies a lower bound on maximum coverage. Falling below the floor does not prove infeasibility. Here independent maximum-coverage programs check all five exclusions, each with zero MIP gap and optimum below the 12,486.169719 floor.

<div class="hy-model-table"><table><caption>Table 4. New exact exclusion checks.</caption><thead><tr><th scope="col">Setting</th><th scope="col">Maximum coverage</th><th scope="col">Required floor</th><th scope="col">Conclusion</th></tr></thead><tbody><tr><td>At most 2 centers</td><td>4,272.217</td><td>12,486.170</td><td>Below floor</td></tr><tr><td>At most 4 centers</td><td>8,087.763</td><td>12,486.170</td><td>Below floor</td></tr><tr><td>At most 6 centers</td><td>11,452.418</td><td>12,486.170</td><td>Below floor</td></tr><tr><td>Capacity × 0.5</td><td>9,387.644</td><td>12,486.170</td><td>Below floor</td></tr><tr><td>Capacity × 0.6</td><td>11,209.200</td><td>12,486.170</td><td>Below floor</td></tr></tbody></table></div>

Travel threshold and speed alter eligible links; capacity determines which entire demand blocks fit. Budget variation near a solution spending only 7.92 of 14 has limited effects under the other restrictions and compromise rule. These outcomes do not predict returns to a real investment: capital distance omits local roads, transport modes and response times.

Likewise, sampled saturation around ten built centers does not prove more construction is useless. It describes a selected compromise under fixed capacity, weights, decoder and search. Different assignments or equity requirements can change the outcome.

<h2 id="scenario">10. Uniform-growth scenario</h2>

The saved demographic extension fits a bounded logistic curve to a 1990–2023 older-age-share series. Its R² is 0.9664, but asymptote L reaches the imposed upper bound 40%. Saved standard errors are about 29.22 percentage points for L and 32.13 years for the midpoint, showing weak long-term identification. In-sample fit does not validate a future forecast.

<div class="hy-equation">
\[
s(t)=\frac{L}{1+e^{-k(t-t_0)}},\qquad r=s(2030)/s(2020)=1.281281.
\tag{8}
\]
</div>

The ratio defines a uniform-growth scenario: every regional weight, center capacity and coverage floor is scaled together; costs and travel remain fixed. This preserves all assignment feasibility relations. Relative coverage and time inequality stay unchanged for a fixed assignment.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/growth-scenario.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size"><img src="{{ '/assets/img/research/elderly-care/growth-scenario.svg' | relative_url }}" alt="The demographic extension is assumption based. Capacity rises with demand, explicitly explaining why placement need not change." width="1046" height="408" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 10.</span> The demographic extension is assumption based. Capacity rises with demand, explicitly explaining why placement need not change.</figcaption></figure>

The same nine centers remain selected; covered weight rises from 14,203.513 to 18,198.693, while its fraction stays 68.2524%. This is mainly scale invariance, not evidence of robustness to future spatial demographic change. Fixed capacity or unequal provincial aging would break that invariance.

<div class="hy-model-table"><table><caption>Table 5. Joint scaling in the growth scenario.</caption><thead><tr><th scope="col">Component</th><th scope="col">Change</th><th scope="col">Consequence</th></tr></thead><tbody><tr><td>Weights</td><td>× 1.281281 everywhere</td><td>No regional redistribution</td></tr><tr><td>Capacity and floor</td><td>Same proportional increase</td><td>Assignments remain feasible</td></tr><tr><td>Travel and costs</td><td>Unchanged</td><td>No new geography</td></tr><tr><td>Locations</td><td>Same nine</td><td>Conditional scale invariance</td></tr><tr><td>Uneven aging / fixed capacity</td><td>Untested</td><td>Separate stress test needed</td></tr></tbody></table></div>

<h2 id="verification">11. Independent verification</h2>

The revision reopens saved data without running source scripts that write into the original project. Outcome identity is confirmed to floating-point precision, cluster counts recalculated and scores recomputed from saved held-out predictions. A separate decoder verifies every regional assignment and reconstructs all selected objectives.

Seven new binary-programming solves use the same whole-region demands, budget, facility limits and capacity constraints. Two baseline envelopes reproduce saved values; five exclusion checks supply stronger evidence than the greedy screen. They verify the declared mathematical model, not the assumed costs, travel times or conversion from population to care.

<div class="hy-model-table"><table><caption>Table 6. Evidence ledger.</caption><thead><tr><th scope="col">Claim</th><th scope="col">Evidence</th><th scope="col">Boundary</th></tr></thead><tbody><tr><td>Profiles and prediction</td><td>Saved panel, recomputed scores</td><td>Snapshot generalization</td></tr><tr><td>Selected network</td><td>Independent assignment reconstruction</td><td>Declared decoder</td></tr><tr><td>Objective envelopes</td><td>Two fresh exact solves</td><td>Broader free assignment</td></tr><tr><td>Five exclusions</td><td>Five fresh exact solves</td><td>Baseline eligibility rules</td></tr><tr><td>Repeated compromise</td><td>Archived selected sets</td><td>No full-frontier certificate</td></tr><tr><td>Convergence and packages</td><td>Code audit finds issues</td><td>Corrected rerun remains future work</td></tr></tbody></table></div>

New figures reconstruct country data, predictions, allocations, trade-offs and assumptions. Manuscripts and result files are preserved. Conceptual illustrations remain distinguishable from quantitative plots so visual polish does not imply additional empirical validation.

<h2 id="discussion">12. Discussion and conclusions</h2>

The contribution is a clear separation of descriptive profiling, predictive evaluation, design rules and constrained network exploration. Country analysis offers a reproducible aggregate prediction task. The regional exercise shows how capacity, travel eligibility, weighted demand and an equity definition change which locations appear useful.

Further work should prioritize three improvements. Prediction needs fold-specific preprocessing, held-out regions and years, and uncertainty-aware indicator harmonization. Network modeling needs finer demand points, real travel information, divisible service allocations and explicit minimum-access or self-service requirements. Optimization needs a corrected monitor and a compromise rule tied to stated priorities.

The equipment-package boundary rule also needs repair before its intended three levels are interpreted. Any service package requires separate feasibility and outcome evaluation. Neither an importance bar nor a coverage percentage identifies a medical intervention's effectiveness.

Within these boundaries, the selected saved solution is reproducible and feasible, and new exact checks strengthen narrow mathematical claims. The research supports transparent discussion of planning assumptions without claiming a validated national care system, individual risk predictor or optimal policy.
