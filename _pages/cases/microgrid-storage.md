---
layout: han-project
title: "Wind–Solar–Storage Coordination"
description: "A scenario-based study of renewable curtailment, daily supply cost, and battery sizing across three park microgrids."
permalink: /projects/modeling/microgrid-storage/
discipline: "Energy systems"
period: "2024"
question: "When does battery storage improve the balance between renewable supply and demand?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Energy-balance modeling, dispatch optimization, storage sizing"
outcome: "Electrician Cup · 2024 · competition manuscript"
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: Model design
    id: method
  - label: Results
    id: findings
  - label: Discussion
    id: discussion
---

<h2 id="abstract">Abstract</h2>

Renewable generation and electricity demand do not necessarily peak together. This study compares separate and joint operation of three microgrids, then examines how storage shifts energy between surplus and deficit periods. The central design question is not simply whether to add a battery, but how operating rules, power capacity, and energy capacity interact.

The supplied typical-day profiles allow the same question to be examined at two scales: each park balancing its own supply, and the parks operating as a combined system. The analysis progresses from a no-storage reference to a common battery configuration and then to park-specific sizing candidates.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>The common battery lowers reported supply cost and curtailment in all three parks, but by different amounts. Storage value depends on the shape of the supply–demand mismatch, not capacity alone.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable microgrid result figure"><img src="{{ '/assets/img/research/energy-dispatch.svg' | relative_url }}" alt="Supply cost and renewable curtailment before and after the common storage configuration. Redrawn from manuscript Tables 2 and 3; both vertical axes begin at zero." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> Supply cost and renewable curtailment before and after the common storage configuration. Redrawn from manuscript Tables 2 and 3; both vertical axes begin at zero.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### System boundary and operating assumptions

I formulated daily energy-balance and supply-cost models using the supplied renewable-generation and load profiles. In the competition scenario, renewable output supplies local demand first. The main grid supplies a shortfall, while surplus generation cannot be sold back to the grid and is therefore curtailed unless it can be stored. These operating rules make the timing of a surplus as important as its total size.

The source fixes the grid-purchase price at 1 CNY/kWh and gives battery cost assumptions of 800 CNY/kW for power capacity and 1,800 CNY/kWh for energy capacity, with a ten-year service-life assumption. These are inputs to the competition model, not current market quotations.

### Dispatch before sizing

The baseline contains no battery. The next scenario gives every park the same 50 kW / 100 kWh configuration, subject to the source's 10–90% state-of-charge range and 95% charge/discharge efficiency assumption. The calculation tracks renewable supply, grid purchases, curtailment, and storage behavior across the typical day.

The two capacity units describe different constraints. Power capacity limits how quickly the battery can charge or discharge; energy capacity limits how much it can hold. A large energy capacity cannot, on its own, absorb a short surplus peak if the charging-power limit is too low. The subsequent sizing exercise treats the two capacities separately instead of scaling a single battery-size number.

### Separate parks and joint operation

The final level of comparison combines the parks' generation and demand. Complementary profiles can then offset one another before storage is used. This changes the balance seen by the battery and makes joint operation a different scenario, not simply the sum of three independently optimized batteries. MATLAB calculations support the operating comparisons and candidate sizing results.

<h2 id="findings">Selected results</h2>

### A paired comparison under the common battery

Figure 1 reproduces the baseline and common-storage results in manuscript Tables 2 and 3. Reported average supply costs change from 0.8183 to 0.8104 CNY/kWh in Park A, 0.7159 to 0.6997 in Park B, and 0.7037 to 0.6854 in Park C. Relative to the respective baselines, these are reductions of approximately 1.0%, 2.3%, and 2.6%, calculated from the table values.

Daily curtailment falls from 951.20 to 869.48 kWh in Park A, 897.50 to 741.95 kWh in Park B, and 1,128.02 to 997.51 kWh in Park C. Park B has the largest relative curtailment reduction in this comparison, about 17.3%, whereas Park C has the largest relative decrease in average supply cost. The two panels therefore answer different questions; less wasted renewable energy and lower supply cost should not be treated as interchangeable measures.

### Why sizing remains park-specific

The separate sizing exercise reports candidates of 377 kW / 1,130 kWh for Park A, 163 kW / 544 kWh for Park B, and 274 kW / 821 kWh for Park C. Their different power–energy combinations reinforce the need to account for each park's profile. They are submitted model outputs, not independently verified global optima or investment recommendations. Figure 1 concerns only the common battery and does not attribute its savings to these later sizing candidates.

<h2 id="discussion">Discussion</h2>

These are scenario-dependent calculations, not measured savings from an installed microgrid. The manuscript's purchase-volume column remains unchanged between the baseline and common-storage tables, so this page does not infer reduced grid purchases from that column. Reconciling that accounting is a prerequisite to a stronger economic conclusion.

A follow-up would check energy conservation at every interval, confirm consistent initial and final stored energy, and test alternative generation and demand days. Battery aging, tariff uncertainty, and an explicitly defined efficiency convention would also need attention. A typical-day result should not be multiplied into an annual saving without examining how representative that day is. The contribution here is the structured comparison of operating rules and capacity choices, with the limits of the supplied accounting kept visible.

<p class="hy-source-note">Research record: Electrician Cup competition manuscript, 2024, Tables 2–5 and storage-sizing sections. Original study: <em>Coordinated optimization of wind, solar, and storage in park microgrids</em>. Independently developed by Han Yang.</p>
