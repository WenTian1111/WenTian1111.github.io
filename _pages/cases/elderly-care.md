---
layout: han-project
title: Healthy Aging & Equitable Care Networks
description:
  From country-level healthy-aging indicators to a modeled service network, with clear boundaries between association, prediction, and policy
  effects.
permalink: /projects/modeling/elderly-care/
discipline: Public-health data · Service-network modeling
period: 2024 study
question: How can country-level aging profiles inform a transparent, equity-aware service-network scenario?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Public-data harmonization, clustering, out-of-fold prediction, multiobjective facility location
outcome: 184 country profiles · a 31-region network scenario · explicit proxy limits
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: healthy life and service access"
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: "3. Stage A: build comparable country profiles"
    id: data
  - label: "4. Stage B: predict a proxy without claiming causation"
    id: prediction
  - label: "5. Stage C: state the regional network assumptions"
    id: network
  - label: "6. Stage D: compare the trade-offs"
    id: selection
  - label: 7. Scenario sensitivity and a future-demand test
    id: sensitivity
  - label: "8. Discussion: three types of evidence"
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

This study links two analytical levels without treating them as the same dataset or the same causal question. First, public country-level indicators describe economic, demographic, and healthy-aging differences. Clustering summarizes those profiles, and cross-validated prediction estimates a healthy-life gap proxy. Second, a simplified regional service network compares facility arrangements using weighted coverage, normalized cost, and accessibility inequality.

The country analysis retains 184 economies, with three clusters selected by the evaluated silhouette criterion. A five-fold out-of-fold random forest gives an archived $R^2$ of 0.790 and RMSE of 0.453 years for the proxy. In the regional scenario, a nine-facility compromise covers 68.3% of the modeled weighted demand at cost 7.9201 normalized units and accessibility Gini 0.206. These are exploratory associations and conditional planning outputs, not evidence that a policy intervention improves health or that facilities have been built.

<h2 id="background">1. Background: healthy life and service access</h2>

Longer life does not necessarily mean that additional years are spent in good health. At age 60, the difference between life expectancy and healthy life expectancy offers a broad population-level proxy for years lived outside full health. It is not an individual diagnosis, a clinical disability score, or an observed need for a specific service.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/elderly-care/cover.webp' | relative_url }}" alt="Conceptual connected-care network for an aging population" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual connected-care network for an aging population. The illustration is thematic, not a map of implemented facilities or measured patient flows.</figcaption></figure>

The country-level data are assembled from World Development Indicators and World Health Organization sources in the archived project. The input tables contain indicators over different periods; the analysis selects available recent values rather than a single uniform observation year. The page retains the study's 2024 framing but does not imply that every input was measured in 2024.

The service-location scenario is a separate regional exercise using 31 provincial-capital nodes, population structure, and an economic snapshot. Country-level clusters do not become proven provincial treatment effects. This separation prevents a descriptive global pattern from being presented as direct evidence for a local intervention.

<h2 id="roadmap">2. Study roadmap</h2>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/elderly-care/workflow.webp' | relative_url }}" alt="Supplied overview of data preparation, profile analysis, prediction, and service-network optimization" width="1491" height="1055" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Supplied overview of data preparation, profile analysis, prediction, and service-network optimization. Embedded maps and miniature curves are conceptual; the plots below present saved analytical records.</figcaption></figure>

<h2 id="data">3. Stage A: build comparable country profiles</h2>

The raw collection includes 217 WDI economies and eight indicators, with 21,371 records across 2010–2023. Aggregates are removed and availability rules produce 184 usable country profiles. The WHO component contains life expectancy and healthy life expectancy at age 60. The outcome proxy is:

<div class="hy-equation">
\[
Y_i=\operatorname{LE60}_i-\operatorname{HALE60}_i.
\tag{1}
\]
</div>

For each indicator, the latest available value is selected and numeric features are scaled before clustering. The admissible missingness rule allows up to two missing features while requiring an available outcome. This creates a workable exploratory sample, but it does not make the records contemporaneous. Differences in observation year, reporting quality, and missingness can influence the apparent profiles.

The selected three-cluster solution has silhouette approximately 0.3018, versus 0.2936, 0.2652, and 0.2406 for four through six clusters. The groups contain 66, 57, and 61 countries. Bootstrap resampling gives mean adjusted Rand agreement around 0.8645, with a lower fifth percentile around 0.728. These support a reasonably stable descriptive partition in this sample; they do not establish natural clinical categories.

<h2 id="prediction">4. Stage B: predict a proxy without claiming causation</h2>

The prediction task evaluates whether the observed features can recover the healthy-life gap across held-out countries. Five-fold out-of-fold predictions ensure that each plotted country is predicted by a model that did not fit that country's outcome.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/profiles.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/elderly-care/profiles.svg' | relative_url }}" alt="Cluster-selection silhouette scores and out-of-fold predictions of the healthy-life gap" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Cluster-selection silhouette scores and out-of-fold predictions of the healthy-life gap. The diagonal indicates agreement; the scatter does not demonstrate the effect of any intervention.</figcaption></figure>

The archived random forest achieves $R^2=0.7903$ and RMSE 0.4528 years. Relative tiers use sample cut points near 4.5293 and 5.5966 years, giving groups of 61, 61, and 62 countries. These are sample-relative classifications, not medical thresholds.

Life expectancy is a prominent predictor, but it also participates in the construction of the outcome proxy. Its apparent importance must therefore be interpreted with that mathematical coupling in mind. Feature importance measures predictive contribution under a fitted model; it does not identify which policy would cause the largest health improvement.

The project further constructs a 3 × 3 service-priority matrix from profile and outcome tiers. Those nine combinations are designed planning rules. They have not been evaluated as treatments or prospectively tested service packages.

<h2 id="network">5. Stage C: state the regional network assumptions</h2>

The regional model treats provincial capitals as candidate service nodes. Travel time is approximated from distance, a road multiplier of 1.3, and a speed of 70 km/h. The baseline uses a five-hour travel limit, a budget of 14 normalized cost units, at most twelve facilities, and a per-facility capacity of 2,269.84 modeled demand units.

Demand weights are adjusted population quantities. Their sum is 20,810 in the model's ten-thousand-unit scale. Covered weighted demand is consequently not a head count of real patients served. A network meeting those aggregate weights can still miss local communities or face unmodeled capacity bottlenecks.

<div class="hy-equation">
\[
C(\mathbf x)=\frac{\sum_i w_i\,a_i(\mathbf x)}{\sum_i w_i},\qquad a_i(\mathbf x)\in[0,1].
\tag{2}
\]
</div>

The modeled accessibility $a_i$ depends on the assignment and feasibility rules. The optimization compares weighted coverage, facility cost, and accessibility Gini. A coverage floor is essential: an empty or almost empty network can otherwise appear artificially equal because almost nobody has access.

<h2 id="selection">6. Stage D: compare the trade-offs</h2>

A multiobjective evolutionary search generates candidate compromises, with repeated random seeds used to inspect solution stability. In the archived baseline, all five runs select the same knee arrangement: Hebei, Liaoning, Heilongjiang, Zhejiang, Jiangxi, Shandong, Henan, Hunan, and Chongqing.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/network.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/elderly-care/network.svg' | relative_url }}" alt="Archived feasible coverage–cost candidates, with accessibility inequality distinguished by color, and selected network comparisons" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Archived feasible coverage–cost candidates, with accessibility inequality distinguished by color, and selected network comparisons. The knee is a compromise within the modeled objectives, not a uniquely best policy.</figcaption></figure>

<div class="hy-model-table"><table><caption>Coverage counts are model weights; the selected compromise covers 68.3% of their total.</caption><thead><tr><th scope="col">Scenario</th><th scope="col">Weighted demand covered</th><th scope="col">Cost units</th><th scope="col">Accessibility Gini</th></tr></thead><tbody><tr><td>Uniform 12-facility reference</td><td>10,874.8</td><td>13.2495</td><td>0.2648</td></tr><tr><td>Selected 9-facility compromise</td><td>14,203.5</td><td>7.9201</td><td>0.2062</td></tr></tbody></table></div>

Exact mixed-integer reference problems bound particular objectives. A maximum-coverage formulation reaches approximately 17,539.9 weighted units. A minimum-cost formulation at the knee's coverage reaches cost 7.6721, compared with the selected 7.9201, a gap of about 3.2%. These are useful objective-specific benchmarks; neither proves that the selected point globally optimizes all three competing objectives.

Against 1,000 saved random arrangements, the compromise lies around the 95.9th percentile of the evaluated reference comparison. It is not claimed to outperform every random arrangement. The reference distributions help characterize performance without turning one selected seed into a universal guarantee.

<h2 id="sensitivity">7. Scenario sensitivity and a future-demand test</h2>

The sensitivity study reoptimizes across six parameter families. Travel-time assumptions are particularly influential: the saved comparison changes weighted coverage by about 34.4% across the evaluated settings. Budget has a smaller reported effect because another constraint can become binding first.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/elderly-care/sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/elderly-care/sensitivity.svg' | relative_url }}" alt="Selected feasible reoptimized sensitivity records for travel-time and budget settings" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Selected feasible reoptimized sensitivity records for travel-time and budget settings. Each point reflects a new model solution; it does not describe uncertainty around one fixed implemented network.</figcaption></figure>

The future-demand exercise applies a logistic projection factor near 1.281. The projection parameters are weakly identified, and demand, capacity, and the coverage floor are scaled in a coordinated way. An unchanged selected layout under that construction is therefore not evidence of robustness to independently changing provincial populations or service needs.

A stronger scenario design would perturb regional growth unevenly, vary capacity independently of demand, and test out-of-sample travel and utilization patterns. Reporting uniform scaling as a conditional scenario keeps the forecast from implying precision that its data cannot support.

<h2 id="discussion">8. Discussion: three types of evidence</h2>

The study contains descriptive evidence about country profiles, predictive evidence about a constructed healthy-life proxy, and optimization evidence about a simplified service network. None of those automatically supplies a causal estimate of a policy's health effect. Keeping the three levels separate makes the project more useful rather than less ambitious.

The modeled network improves its own reference coverage and equity measures, but a provincial-capital approximation omits local geography, waiting times, workforce availability, quality of care, and actual service uptake. The normalized costs also require a real budgeting model before investment decisions.

The next research step should align observation years, validate the proxy and prediction externally, and develop a finer service-demand model with observed travel and utilization. Policy recommendations should then be tested against those independent constraints. The current work is an exploratory analytical framework and a transparent scenario calculation.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
