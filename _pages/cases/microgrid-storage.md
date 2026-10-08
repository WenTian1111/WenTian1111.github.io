---
layout: han-project
title: Wind–Solar–Storage Coordination
description:
  "From hourly renewable mismatches to investment-aware battery sizing: separating the value of sharing resources from the incremental value
  of storage."
permalink: /projects/modeling/microgrid-storage/
discipline: Energy systems · Optimization
period: 2024 study
question: When does a battery improve renewable integration, and when does sharing resources matter more?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Hourly energy balance, joint capacity sizing, LP and MILP, representative-day comparison
outcome: Three parks · shared operation · investment-aware storage sizing
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: the mismatch within a day"
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: "3. Stage A: a consistent dispatch model"
    id: balance
  - label: "4. Stage B: from a common battery to tailored capacity"
    id: individual
  - label: "5. Stage C: identify the value of coordination"
    id: coordination
  - label: "6. Stage D: account for seasonality and tariff structure"
    id: seasonal
  - label: 7. Verification, interpretation, and limitations
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

A renewable-rich industrial park can still import electricity while discarding renewable generation at other hours. This study models that mismatch in three parks and asks how storage capacity and coordinated operation change the daily balance. It begins with hourly load, wind, and photovoltaic profiles; establishes a no-storage baseline; tests a common battery; then sizes batteries jointly with dispatch. Finally, it considers pooled operation and monthly representative days under alternative tariff structures.

The revised archived results show that pooling resources already removes much of the imbalance. Separate parks without batteries cost 17,457.3 CNY per day; joint operation without storage costs 15,717.8 CNY per day. A jointly sized 445 kW / 1,465 kWh battery reduces the latter to approximately 15,424.4 CNY per day. These comparisons include the study's investment allocation. They show why operational savings should be compared on a consistent accounting basis, rather than treating a battery as free equipment.

<h2 id="background">1. Background: the mismatch within a day</h2>

Park A has photovoltaic generation, Park B wind generation, and Park C both. Their daily electricity demands are 7,901, 7,710, and 7,776 kWh. Solar production is concentrated in daylight hours; wind and demand vary differently. A surplus at noon cannot directly meet a deficit at night without storage or another source of flexibility.

The study uses supplied hourly spreadsheets rather than an observed year of grid operation. It treats each park as an energy balance with idealized access to grid imports. The baseline peak loads are 447, 419, and 506 kW; the aggregated peak is 1,328 kW because the individual peaks do not occur at exactly the same hour.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/cover.webp' | relative_url }}" alt="Conceptual renewable industrial campus" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual renewable industrial campus. The illustration introduces the wind–solar–storage setting; it does not show the actual park topology or measured assets.</figcaption></figure>

The question is therefore sequential: establish the imbalance first, test flexibility second, and only then decide how much flexibility to purchase. This order prevents a visually attractive battery scenario from replacing the accounting baseline.

<h2 id="roadmap">2. Study roadmap</h2>

The analysis proceeds from individual parks to shared operation, increasing the scope only after establishing a comparable daily objective. The last stage changes the temporal representation and price schedule, rather than silently replacing the original input day.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/workflow.webp' | relative_url }}" alt="Method overview supplied with the project, with the comparison matrix aligned to flat versus time-of-use tariffs and one versus twelve representative days" width="1491" height="1055" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Method overview supplied with the project, with the comparison matrix aligned to flat versus time-of-use tariffs and one versus twelve representative days. Embedded miniature profiles are conceptual; the quantitative results below use saved calculation tables.</figcaption></figure>

<h2 id="balance">3. Stage A: a consistent dispatch model</h2>

For hour $t$, renewable energy is either consumed, stored, or curtailed. Grid imports and battery discharge cover the remaining demand. The power balance is written before the cost function so every claimed saving can be traced to an energy flow.

<div class="hy-equation">
\[
L_t=R_t-C_t+G_t+P_t^{\mathrm{dis}}-P_t^{\mathrm{ch}}.
\tag{1}
\]
</div>

Here $L_t$ is load, $R_t$ available renewable power, $C_t$ curtailed power, and $G_t$ grid imports. Charging and discharging are bounded by battery power $P$. Stored energy is bounded by capacity $E$ and evolves with the assumed efficiencies:

<div class="hy-equation">
\[
e_{t+1}=e_t+\eta_{\mathrm{ch}}P_t^{\mathrm{ch}}\Delta t-\frac{P_t^{\mathrm{dis}}\Delta t}{\eta_{\mathrm{dis}}},\qquad 0\le e_t\le E.
\tag{2}
\]
</div>

A daily cyclic energy condition prevents the optimizer from obtaining a free benefit by emptying a battery that was charged before the modeled day. The objective combines daily operating expenditure with allocated capital cost. Renewable generation cost is treated consistently across comparisons. A dispatch-only objective and an investment-aware objective answer different questions and should not be mixed.

Capacity and dispatch are first optimized in a continuous linear formulation. An engineering grid of 1 kW power and 5 kWh energy increments is then checked with a mixed-integer formulation. Saved comparisons give small objective differences of 0.304, 0.121, and 0.187 CNY per day for the three parks. These figures refer to the corresponding optimization objective, not a different total-cost column. Postchecks examine simultaneous charging and discharging; a continuous model does not prohibit that behavior simply by having separate charge and discharge variables.

<h2 id="individual">4. Stage B: from a common battery to tailored capacity</h2>

Without storage, Parks A, B, and C curtail 951.2, 897.5, and 1,128.0 kWh per day. A common 50 kW / 100 kWh battery offers a controlled comparison, but it need not match each park's renewable surplus. After investment allocation, its daily net gains are approximately 15.7, 123.9, and 60.9 CNY. Thus the same equipment has different economic value in different hourly profiles.

The next calculation allows capacity to respond to each park. Power capacity controls how quickly the battery can absorb a surplus; energy capacity controls how long it can retain it. Optimizing only one of these quantities would leave the other as an implicit constraint.

<div class="hy-model-table"><table><caption>Selected engineering-grid designs from the revised archived results.</caption><thead><tr><th scope="col">Park</th><th scope="col">Battery power / energy</th><th scope="col">Total daily cost</th><th scope="col">Curtailed energy</th></tr></thead><tbody><tr><td>A</td><td>195 kW / 1,130 kWh</td><td>6,206.9 CNY</td><td>0 kWh</td></tr><tr><td>B</td><td>212 kW / 625 kWh</td><td>5,065.5 CNY</td><td>1.01 kWh</td></tr><tr><td>C</td><td>261 kW / 1,270 kWh</td><td>5,137.5 CNY</td><td>0 kWh</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/independent.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/independent.svg' | relative_url }}" alt="Individual-park comparisons on a consistent total-cost basis, with curtailed renewable energy shown separately" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Individual-park comparisons on a consistent total-cost basis, with curtailed renewable energy shown separately. Values are from the revised result table.</figcaption></figure>

Near-zero curtailment is a modeled outcome, not a universal design target. A battery that eliminates every surplus may still be unattractive under different equipment prices or financing assumptions. The archived simple payback estimates are about 7.0, 4.4, and 6.7 years; they inherit the study's assumed daily repetition and cost model.

<h2 id="coordination">5. Stage C: identify the value of coordination</h2>

Pooling loads and renewable output makes a surplus in one park available to another in the idealized shared system. This is distinct from shifting energy across time with a battery. The following comparisons keep those mechanisms separate.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/joint.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/joint.svg' | relative_url }}" alt="Five daily total-cost scenarios" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Five daily total-cost scenarios. Joint operation is first evaluated without a battery; storage is then added to the same pooled system.</figcaption></figure>

Joint operation without storage reduces daily cost by 1,739.5 CNY relative to separate parks without storage. Adding the optimized shared battery contributes a further 293.4 CNY per day. Together the modeled reduction is about 2,032.9 CNY per day. On this particular sequence of baselines, pooling contributes roughly 85.6% and incremental storage 14.4% of the combined reduction.

This is a decomposition of the stated comparisons, not a universal causal allocation. A different reference scenario or tariff can change the shares. The jointly optimized system is also about 985.5 CNY per day less costly than separately optimized batteries. That finding supports studying spatial coordination before assuming each park requires its own large battery.

The pooled model abstracts away feeder limits, losses, congestion, and arrangements for settling exchanges. A deployable park network would have to add those constraints. The modeled saving should therefore be read as the value of coordination under the supplied energy profiles and idealized sharing rules.

<h2 id="seasonal">6. Stage D: account for seasonality and tariff structure</h2>

A single day can conceal seasonal differences in wind and photovoltaic availability. The expanded study uses twelve monthly representative days and compares flat pricing with time-of-use pricing. The two factors form a 2 × 2 experimental structure: changing the price schedule is distinguished from changing the set of representative days.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/seasonal.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/seasonal.svg' | relative_url }}" alt="Additional renewable and battery capacities in the monthly time-of-use scenario" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Additional renewable and battery capacities in the monthly time-of-use scenario. Wind and solar capacities use kW; battery power and energy are displayed separately with their own units.</figcaption></figure>

Under that expanded scenario, the selected additional wind / photovoltaic capacities are 1,045 / 90 kW for A, 93 / 719 kW for B, and 657 / 163 kW for C. The corresponding battery power / energy pairs are 90 / 143, 100 / 163, and 165 / 291 in kW / kWh. These are new scenario designs, not replacements for the earlier single-day battery results.

A separate increased-load scenario scales demand by 1.5 and studies joint resource expansion. Its output is conditional on that demand assumption. Twelve typical days offer a tractable seasonal representation, but they do not preserve the chronology of 8,760 hourly observations or long multi-day storage events.

<h2 id="discussion">7. Verification, interpretation, and limitations</h2>

The saved project compares continuous and engineering-grid solutions, checks energy balance and cyclic state of charge, and examines changes in operating and investment assumptions. The website figures are redrawn from the revised tables; the older backup manuscript contains different capacity values and is not used for this presentation.

The main conclusion is about sequencing decisions. First quantify the renewable mismatch, then test the value of pooling, and only then price the additional value of temporal storage. This is more informative than reporting a single optimized battery without its reference case.

The results remain sensitive to capital allocation, financing, efficiency, equipment degradation, and how representative days are weighted. Ideal pooling also omits network constraints. A next-stage study should use chronologically ordered data, include degradation and physical exchange limits, and validate the dispatch against independent operational measurements. Numerical feasibility in the current model is useful evidence, but it is not an operating guarantee.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
