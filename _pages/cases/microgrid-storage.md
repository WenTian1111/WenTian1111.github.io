---
layout: han-project
title: Wind–Solar–Storage Coordination
description: "An investment-aware study of three industrial parks: hourly energy balance, battery sizing, resource sharing, renewable expansion, and seasonal tariff effects."
permalink: /projects/modeling/microgrid-storage/
discipline: Energy systems · Optimization
period: 2024 study
question: How should renewable generation, storage, and shared operation be coordinated when both timing and investment matter?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Capacity–dispatch LP, engineering-grid MILP, controlled comparisons, sensitivity analysis
outcome: Three parks · hourly dispatch · spatial sharing · seasonal capacity planning
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Data and study design
    id: data
  - label: 3. Dispatch and capacity model
    id: model
  - label: 4. Individual-park storage
    id: individual
  - label: 5. Shared operation
    id: coordination
  - label: 6. Renewable expansion
    id: expansion
  - label: 7. Seasonal planning
    id: seasonal
  - label: 8. Controlled comparison
    id: attribution
  - label: 9. Numerical verification
    id: verification
  - label: 10. Sensitivity analysis
    id: sensitivity
  - label: 11. Discussion
    id: discussion
  - label: 12. Conclusions
    id: conclusions
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Industrial parks with substantial renewable generation can import electricity and curtail renewable output on the same day. The underlying issue is the timing of supply relative to demand. This study develops an investment-aware optimization framework for three parks with different wind and photovoltaic portfolios. Hourly dispatch, battery power, and battery energy are optimized together; resource sharing and renewable expansion are then examined through explicitly defined comparisons. A final experiment separates changes in seasonal resource data from changes in the tariff schedule.

For the supplied reference day, individually operated parks without storage incur a combined cost of **17,457.3 CNY/day**. Ideal pooling reduces this to **15,717.8 CNY/day** before a battery is installed. A jointly sized **445 kW / 1,465 kWh** battery lowers the investment-inclusive cost to **15,424.4 CNY/day**. Relative to the separate, no-storage baseline, spatial sharing accounts for 85.6% of the combined reduction along this comparison sequence. Relative to separately optimized batteries, the pooled design saves 985.6 CNY/day and uses approximately half the nominal battery energy. Under 50% higher demand, renewable expansion becomes central; monthly resource profiles and time-of-use pricing substantially change the preferred generation mix and storage scale. Billing sensitivity further shows that paying only for utilized renewable energy can eliminate the incentive to install a battery in some parks.

These are deterministic numerical results for supplied profiles and specified economic assumptions. The study connects capacity decisions to hourly operating mechanisms and distinguishes numerical feasibility from field performance.

<p class="hy-source-note"><strong>Keywords:</strong> industrial microgrids; renewable integration; battery sizing; coordinated dispatch; linear programming; representative days; time-of-use pricing.</p>

<h2 id="introduction">1. Introduction</h2>

Renewable abundance does not guarantee hourly self-sufficiency. A photovoltaic park can have a large midday surplus and a substantial evening deficit, while a wind-powered park may have a different pattern of surplus hours. Adding storage addresses mismatch across time. Connecting parks addresses mismatch across locations. Their economic contributions need to be examined separately because equipment investment, renewable billing, and the choice of reference case can change the apparent benefit.

The study asks three linked questions. First, how much storage is justified by each park's hourly imbalance? Second, how much of that imbalance disappears when parks share their existing resources? Third, how should additional renewable capacity and storage be co-designed when demand grows and the resource representation becomes seasonal? The analysis follows this sequence so each expansion of the model has an interpretable baseline.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/cover.webp' | relative_url }}" alt="Conceptual industrial campus supplied by wind, solar generation, and battery storage" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> The wind–solar–storage setting. This conceptual illustration introduces the application; it does not depict surveyed infrastructure, actual network topology, or measured equipment.</figcaption></figure>

<h2 id="data">2. Data and study design</h2>

### 2.1 Resource portfolios and temporal resolution

The inputs comprise 24 hourly load values for each park, a reference-day set of per-unit renewable profiles, and twelve monthly representative-day sets of renewable profiles. Nameplate capacities convert the per-unit profiles into available power. Each one-hour interval represents a constant average power; numerical kW and kWh values coincide over that interval, although their units remain distinct.

<div class="hy-model-table"><table><caption>Table 1. Existing portfolios and the supplied reference-day baseline.</caption><thead><tr><th scope="col">Park</th><th scope="col">Existing wind / PV (kW)</th><th scope="col">Daily demand (kWh)</th><th scope="col">Available renewable energy (kWh)</th><th scope="col">Peak load (kW)</th><th scope="col">No-storage curtailment (%)</th></tr></thead><tbody>
<tr><td>A</td><td>0 / 750</td><td>7,901</td><td>3,978.1</td><td>447</td><td>23.91</td></tr>
<tr><td>B</td><td>1,000 / 0</td><td>7,710</td><td>6,175.2</td><td>419</td><td>14.53</td></tr>
<tr><td>C</td><td>500 / 600</td><td>7,776</td><td>6,204.6</td><td>506</td><td>18.18</td></tr>
</tbody></table></div>

Curtailment rate means curtailed energy divided by **available renewable generation**, rather than by load. Unit supply cost means total reported cost divided by delivered load energy. The aggregated demand is 23,387 kWh/day, and its hourly peak is 1,328 kW. The lower aggregate peak relative to the sum of individual peaks reflects differences in load timing.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/hourly-mismatch.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/hourly-mismatch.svg' | relative_url }}" alt="Hourly load and available renewable output in Parks A, B, and C, highlighting surplus and deficit intervals" width="1186" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Reference-day power profiles. Surplus and deficit intervals are identified before installing storage. Park A's concentrated midday photovoltaic surplus differs from the more distributed wind-related imbalances in B and C.</figcaption></figure>

### 2.2 Comparison sequence and economic assumptions

The first two stages preserve existing renewable capacities and use a flat grid import price of 1 CNY/kWh. Existing photovoltaic and wind energy are billed at 0.4 and 0.5 CNY/kWh, respectively, including curtailed generation in the main accounting basis. Battery power and energy investment are 800 CNY/kW and 1,800 CNY/kWh, allocated over ten years in these stages.

Expansion experiments multiply every hourly load by 1.5, preserving the original load shape. They introduce additional wind and PV investment at 3,000 CNY/kW and 2,500 CNY/kW. All additional investment is allocated over **five years** for this planning experiment. This is an assumed allocation horizon, distinct from the subsequently calculated simple payback period. The monthly experiment uses the same increased load profile in every month; only renewable availability changes seasonally.

The time-of-use schedule is a case assumption: 1 CNY/kWh from **07:00 inclusive to 22:00 exclusive**, and 0.4 CNY/kWh otherwise. It is not a claim about a current utility tariff. Exports are excluded, imports are unrestricted, and the pooled system is an ideal single balance node with lossless, unconstrained internal exchange.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/workflow.webp' | relative_url }}" alt="Overview of dispatch, capacity optimization, shared operation, and a seasonal-data by tariff comparison" width="1491" height="1055" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Study roadmap. The supplied illustration summarizes the sequence of models; embedded miniature profiles are conceptual. The numerical evidence is presented in the tables and data-based figures below.</figcaption></figure>

<h2 id="model">3. Dispatch and capacity model</h2>

### 3.1 Hourly energy balance

For each hour $t$, let $L_t$ denote load, $R_t$ available renewable power, $g_t$ grid imports, $s_t$ curtailed power, and $c_t,d_t$ battery charging and discharging power. The operating balance is

<div class="hy-equation">
\[
R_t-s_t+g_t+d_t=L_t+c_t,
\qquad \Delta t=1\ \mathrm{h}.
\tag{1}
\]
</div>

Without storage, each hour can be evaluated directly: $g_t=\max(L_t-R_t,0)$ and $s_t=\max(R_t-L_t,0)$. This closed-form baseline is useful both for interpretation and for checking the input conversion independently of the optimizer.

### 3.2 Stored energy and daily closure

Let $e_t$ be stored energy at the **beginning** of hour $t$, $P$ nominal battery power, and $E$ nominal battery energy. Each-way efficiency is 0.95, giving a round-trip efficiency of 0.9025. The implemented energy dynamics can be expressed as

<div class="hy-equation">
\[
\begin{aligned}
e_{t+1}&=e_t+0.95c_t\Delta t-\frac{d_t\Delta t}{0.95},\\
0.1E&\le e_t\le0.9E,\\
0&\le c_t,d_t\le P,\qquad e_{24}=e_0.
\end{aligned}
\tag{2}
\]
</div>

Thus only **80% of nominal energy** is available between the SOC limits. A 100 kWh battery has an 80 kWh usable window. Daily closure equates the pre-hour-0 state with the post-hour-23 state; it prevents free energy from an externally precharged battery. Each representative day has its own cyclic state. No battery energy is carried between representative months.

The LP uses separate nonnegative charging and discharging variables without a binary operating-mode restriction. The saved schedules are checked for simultaneous charging and discharging. Physical curtailment is also checked against available generation. These checks concern the returned schedules; they do not imply that a future model with negative prices or different incentives would preserve the same behavior automatically.

### 3.3 Investment-aware objective and reporting basis

With fixed renewable capacities, their generation bill $C_R$ is constant across battery designs. The optimizer therefore minimizes imports plus allocated battery investment, while the reported total adds that renewable bill back:

<div class="hy-equation">
\[
\begin{aligned}
F(P,E)&=\sum_t\lambda_tg_t\Delta t\\
&\quad+\frac{800P+1800E}{10\times365},\\
C_{\mathrm{day}}&=F+C_R,\\
C_R&=0.5\sum_t R_t^{\mathrm{wind}}\Delta t\\
&\quad+0.4\sum_t R_t^{\mathrm{PV}}\Delta t.
\end{aligned}
\tag{3}
\]
</div>

This distinction avoids confusing an optimization objective with a complete supply-cost report. Charging, discharge, energy bounds, and capacity costs remain linear when $P$ and $E$ are decision variables, so capacity and dispatch can be solved in one LP. The archived implementation uses HiGHS. For reference-day storage sizing, a MILP restricts power to 1 kW increments and nominal energy to 5 kWh increments.

Simple payback compares upfront battery investment with annual **operating** savings before capital allocation:

<div class="hy-equation">
\[
T_{\mathrm{pb}}=
\frac{800P+1800E}
{365\left(C_{\mathrm{op},0}-C_{\mathrm{op},1}\right)}.
\tag{4}
\]
</div>

Subtracting allocated investment again in this denominator would double-count capital. These paybacks assume repeated daily operation, constant prices, and no financing, battery replacement, or degradation expenditure.

<h2 id="individual">4. Results I: individual-park storage</h2>

### 4.1 A common battery as a controlled intervention

Without storage, the three parks import 4,874.1, 2,432.3, and 2,699.4 kWh/day and curtail 951.2, 897.5, and 1,128.0 kWh/day. Installing the same 50 kW / 100 kWh battery in each park reduces imports by 76.0, 184.2, and 121.1 kWh/day. Its daily investment allocation is 60.27 CNY per park, so the corresponding investment-inclusive gains are **15.73, 123.93, and 60.85 CNY/day**.

The differences arise from utilization rather than equipment specifications. Park A's saved dispatch charges 84.21 kWh and delivers 76.0 kWh, effectively using its 80 kWh energy window once. Park B delivers 184.2 kWh across several surplus and deficit intervals. A small battery can cycle more than once per day, so daily transferred energy is not limited to one nominal-capacity equivalent.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/dispatch-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/dispatch-comparison.svg' | relative_url }}" alt="Park C charging, discharging, imports, and stored energy with a common battery versus optimized capacity" width="1186" height="610" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Saved reference-day dispatch for Park C. Upper panels show imports and battery power; charging is plotted below zero. Lower panels show end-of-hour stored energy and the 10%–90% admissible window. The two energy axes have different scales because battery sizes differ.</figcaption></figure>

### 4.2 Tailored capacity and its economic trade-off

Optimizing power and energy together produces different designs for each park. Power limits the rate at which a surplus can be absorbed; energy limits its accumulation and subsequent transfer. Similar daily curtailment does not imply similar optimal nominal capacity because surplus timing and repeated cycles also matter.

<div class="hy-model-table"><table><caption>Table 2. Selected reference-day storage designs on the 1 kW × 5 kWh engineering grid.</caption><thead><tr><th scope="col">Park</th><th scope="col">Power / nominal energy (kW / kWh)</th><th scope="col">Allocated investment (CNY/day)</th><th scope="col">Total cost (CNY/day)</th><th scope="col">Supply cost (CNY/kWh)</th><th scope="col">Curtailment (kWh/day)</th><th scope="col">Simple payback (years)</th></tr></thead><tbody>
<tr><td>A</td><td>195 / 1,130</td><td>600.00</td><td>6,206.90</td><td>0.7856</td><td>0</td><td>6.99</td></tr>
<tr><td>B</td><td>212 / 625</td><td>354.68</td><td>5,065.50</td><td>0.6570</td><td>1.01</td><td>4.38</td></tr>
<tr><td>C</td><td>261 / 1,270</td><td>683.51</td><td>5,137.55</td><td>0.6607</td><td>0</td><td>6.71</td></tr>
</tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/individual-results.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/individual-results.svg' | relative_url }}" alt="Three battery scenarios compared by total daily cost and renewable curtailment for each park" width="1186" height="447" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Cost and curtailment are evaluated separately. All cost bars include the same existing-renewable billing basis and the applicable battery investment allocation. Near-zero curtailment in the selected designs is an outcome of this price structure.</figcaption></figure>

Storage reduces each park's total cost by approximately 3.9%–8.2% relative to its no-storage baseline. However, maximizing renewable utilization alone is not the objective. An additional unit of capacity is justified only while its avoided operating expenditure exceeds its allocated investment. Different billing rules can change that marginal comparison substantially, as Section 10 shows.

<h2 id="coordination">5. Results II: shared operation</h2>

### 5.1 Why pooling has value before storage

The pooled model sums hourly loads and renewable output before calculating imports and curtailment. With $x_{i,t}=L_{i,t}-R_{i,t}$, the positive-part inequality explains the no-storage import reduction:

<div class="hy-equation">
\[
\max\!\left(\sum_i x_{i,t},0\right)
\le\sum_i\max(x_{i,t},0).
\tag{5}
\]
</div>

A surplus and a deficit occurring in different parks at the same hour can cancel within the shared balance. The analogous inequality holds for curtailment. Aggregation reduces daily imports from 10,005.8 to 8,266.3 kWh and curtailment from 2,976.7 to 1,237.2 kWh. This requires no battery energy transfer across hours.

### 5.2 Keep weak and strong reference cases separate

<div class="hy-model-table"><table><caption>Table 3. Five reference-day scenarios on the same full-generation billing basis.</caption><thead><tr><th scope="col">Operation and storage</th><th scope="col">Operating cost (CNY/day)</th><th scope="col">Battery allocation (CNY/day)</th><th scope="col">Total cost (CNY/day)</th></tr></thead><tbody>
<tr><td>Separate, no storage</td><td>17,457.33</td><td>0</td><td>17,457.33</td></tr>
<tr><td>Separate, 50 kW / 100 kWh each</td><td>17,076.01</td><td>180.82</td><td>17,256.83</td></tr>
<tr><td>Separate, individually optimized</td><td>14,771.75</td><td>1,638.19</td><td>16,409.94</td></tr>
<tr><td>Pooled, no storage</td><td>15,717.79</td><td>0</td><td>15,717.79</td></tr>
<tr><td>Pooled, jointly optimized</td><td>14,604.39</td><td>820.00</td><td>15,424.39</td></tr>
</tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/coordination-costs.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/coordination-costs.svg' | relative_url }}" alt="Operating expenditure and battery investment allocation across five separate and pooled scenarios" width="1090" height="485" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 6.</span> Cost decomposition across explicitly named reference cases. Storage can reduce operating expenditure while increasing the investment component; the total determines the comparison.</figcaption></figure>

Along the sequence “separate/no storage → pooled/no storage → pooled/optimized storage,” sharing saves **1,739.545 CNY/day**, and the battery adds **293.400 CNY/day** of investment-inclusive saving. Their combined reduction is 2,032.945 CNY/day, or 11.65% of the starting cost. The 85.6% / 14.4% shares describe this particular sequence; they are not universal causal shares and would depend on a different ordering or reference case.

A stronger comparison starts from **separately optimized** batteries. Pooling then reduces total cost by 985.554 CNY/day, approximately 6.01%. The independent designs sum to 668 kW / 3,025 kWh, whereas the shared design is 445 kW / 1,465 kWh: nominal energy is 51.6% lower. Upfront battery investment falls from 5.9794 million to 2.9930 million CNY. The shared battery's simple payback is about 7.36 years relative to the **pooled, no-storage** operating baseline. Using the separate baseline for this calculation would incorrectly credit the battery with the benefit of sharing.

<h2 id="expansion">6. Results III: co-design under demand growth</h2>

### 6.1 Extend capacity decisions to generation

When demand rises by 50%, a battery can redistribute existing energy but cannot create the additional electricity required. The expansion model therefore jointly chooses added wind $\Delta W$, added PV $\Delta S$, and battery $P,E$. Available generation is linear in installed capacity:

<div class="hy-equation">
\[
\begin{aligned}
R_{m,t}={}&(W^0+\Delta W)w_{m,t}\\
&+(S^0+\Delta S)v_{m,t}.
\end{aligned}
\tag{6}
\]
</div>

Here $w_{m,t},v_{m,t}$ are known per-unit profiles. Where a park lacks an existing source type, the assumed new-source profile is the capacity-weighted profile of that type across the other parks. This is a resource-transfer assumption, not an independently measured wind or solar assessment at the proposed installation site.

For representative-day weights $a_m$ summing to 365, the optimized annual objective is

<div class="hy-equation">
\[
\begin{aligned}
\min Z={}&\sum_m a_m\sum_t\lambda_tg_{m,t}\Delta t+\frac{I}{5},\\
I={}&3000\Delta W+2500\Delta S\\
&+800P+1800E.
\end{aligned}
\tag{7}
\]
</div>

New renewable assets incur investment rather than an additional purchased-energy bill. Existing renewable payments are constant and excluded from $Z$. Consequently, the annual objective below is **imports plus allocated new investment**, not the full daily supply-cost measure used in Tables 2–3. Baseline expansion results omit operation and maintenance costs; a later sensitivity run adds them for new wind and PV assets.

### 6.2 Reference-day expansion and ablation

<div class="hy-model-table"><table><caption>Table 4. Expansion designs with 50% higher demand, one repeated reference day, and flat pricing.</caption><thead><tr><th scope="col">Operation</th><th scope="col">Added wind / PV (kW)</th><th scope="col">Battery power / energy (kW / kWh)</th><th scope="col">Upfront investment (million CNY)</th><th scope="col">Annual objective (million CNY/year)</th><th scope="col">Curtailment rate (%)</th></tr></thead><tbody>
<tr><td>Park A</td><td>1,397 / 0</td><td>223 / 635</td><td>5.513</td><td>1.361</td><td>9.54</td></tr>
<tr><td>Park B</td><td>521 / 387</td><td>456 / 990</td><td>4.678</td><td>1.041</td><td>0</td></tr>
<tr><td>Park C</td><td>1,247 / 0</td><td>217 / 413</td><td>4.656</td><td>1.075</td><td>15.34</td></tr>
<tr><td>Pooled</td><td>3,006 / 54</td><td>1,100 / 2,259</td><td>14.099</td><td>3.233</td><td>1.15</td></tr>
</tbody></table></div>

The expansion values are rounded continuous LP decisions, rather than a newly solved catalog or integer equipment design. The pooled upfront investment is below the 14.847 million CNY sum of independent investments. Its lower annual objective reflects both complementary profiles and a coordinated choice of new assets.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/expansion-ablation.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/expansion-ablation.svg' | relative_url }}" alt="Annual optimization objective for storage-only, renewables-only, and jointly designed expansion scenarios" width="1090" height="457" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 7.</span> Ablation under the same increased demand and flat tariff. Each scenario is re-optimized with its permitted decision variables. Annual costs exclude the same constant existing-renewable payments within each operating case.</figcaption></figure>

Relative to renewable expansion alone, co-design reduces the annual objective by approximately 6.9% for A, 14.7% for B, 15.2% for C, and 15.4% for pooled operation. Storage-only expansion selects no battery in A, C, or the pooled case and only a small 10.1 kW / 12.0 kWh battery in B. Higher load absorbs most existing surplus, reducing the value of storage until additional renewable generation is introduced.

Some co-designed cases deliberately retain curtailment. Additional low-cost generation can still avoid enough imports to justify its investment even when part of its output is unused. Generation-to-load ratios of 0.99–1.15 do not mean hourly self-sufficiency: annual or daily energy totals cannot resolve hourly deficits, storage losses, or surplus timing.

<h2 id="seasonal">7. Results IV: monthly resources and time-of-use pricing</h2>

The seasonal planning case retains the 50% load increase and optimizes one common capacity design against twelve renewable representative days. Its primary result uses equal weights of $365/12$ days per month. The tariff distinguishes fifteen high-price hourly intervals from nine low-price intervals, and every representative day has a separate cyclic battery schedule.

<div class="hy-model-table"><table><caption>Table 5. Independent expansion with monthly profiles, equal month weights, and time-of-use pricing.</caption><thead><tr><th scope="col">Park</th><th scope="col">Added wind / PV (kW)</th><th scope="col">Battery power / energy (kW / kWh)</th><th scope="col">Upfront investment (million CNY)</th><th scope="col">Annual grid imports cost (million CNY)</th><th scope="col">Generation / load energy</th><th scope="col">Annual curtailment (MWh)</th></tr></thead><tbody>
<tr><td>A</td><td>1,045 / 90</td><td>90 / 143</td><td>3.690</td><td>1.200</td><td>0.712</td><td>413.5</td></tr>
<tr><td>B</td><td>93 / 719</td><td>100 / 163</td><td>2.451</td><td>1.149</td><td>0.732</td><td>476.1</td></tr>
<tr><td>C</td><td>657 / 163</td><td>165 / 291</td><td>3.035</td><td>1.027</td><td>0.755</td><td>426.3</td></tr>
</tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/monthly-capacities.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/monthly-capacities.svg' | relative_url }}" alt="Added generation, battery power, and battery energy for the monthly time-of-use scenario" width="1186" height="428" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 8.</span> Seasonal designs. Generation and battery power use kW; nominal battery energy uses kWh and is shown on a separate axis. The quantities are rounded from continuous optimization results.</figcaption></figure>

The generation mix changes substantially. A primarily adds wind to complement existing PV, whereas B adds predominantly PV alongside its existing wind. The value of each technology depends on its incremental output during import-dependent hours, the tariff at those hours, and whether a battery can shift otherwise unused production. This offers a more precise explanation than assuming that the cheapest average-energy source should always be expanded most.

Investment falls relative to the repeated-reference-day experiment, but that comparison changes **both resources and prices**. The main monthly table also uses equal month weights. The controlled comparison below uses calendar-length weights normalized to a 365-day year, so its seasonal investment values differ slightly. Neither set is silently substituted for the other.

<h2 id="attribution">8. Controlled comparison: resources versus prices</h2>

A two-factor experiment evaluates one reference day versus twelve monthly days, under flat versus time-of-use tariffs. Within the experiment, demand growth, source-profile construction, capital costs, and the five-year allocation horizon are held fixed. Monthly weights are $365D_m/366$, where $D_m$ follows the supplied 2024 calendar. This preserves relative month lengths while keeping the annual total at 365 days.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/controlled-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/controlled-comparison.svg' | relative_url }}" alt="Two-by-two matrices of upfront investment for each park under one-day versus monthly resources and flat versus time-of-use prices" width="1186" height="485" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 9.</span> Controlled scenario comparison. Each number is <strong>total upfront investment</strong> in million CNY, rather than annual allocated capital expenditure. The monthly cells use calendar-normalized weights.</figcaption></figure>

For A, changing resources while retaining flat pricing reduces upfront investment from 5.513 to 4.106 million CNY. Changing the tariff after adopting monthly resources reduces it further to 3.620 million CNY. The corresponding changes are −1.407 and −0.486 million CNY. For B they are −1.729 and −0.512 million; for C, −0.704 and −0.918 million. Thus resource representation is the larger component along this sequence for A and B, while the tariff component is larger for C.

Let $I_{r,p}$ be investment, with $r=0,1$ denoting one-day and monthly resources and $p=0,1$ denoting flat and time-of-use prices. The interaction is

<div class="hy-equation">
\[
\Delta_{\mathrm{int}}=I_{1,1}-I_{1,0}-I_{0,1}+I_{0,0}.
\tag{8}
\]
</div>

The interaction is +0.528 million CNY for A, +0.521 million for B, and −0.815 million for C. The effect of changing the tariff therefore depends on the resource dataset. The experiment provides attribution **within the specified optimization model**; it is not a field estimate of the causal effect of a tariff reform. In particular, applying time-of-use prices alone cannot explain the full change from the original single-day design to the seasonal design.

<h2 id="verification">9. Numerical verification and reproducibility</h2>

The archived calculations include LP solver evidence, engineering-grid MILP results, enumeration comparisons, and a physical feasibility report. The grid-constrained objective exceeds its continuous lower bound by only **0.304, 0.121, 0.187, and 0.423 CNY/day** for A, B, C, and pooled operation, respectively. The saved MILP records report zero solver gaps for these designs. These are differences in $F$, the imports-plus-investment objective, with the same renewable constants excluded from both sides.

The pooled continuous solution is 448.115 kW / 1,469.145 kWh; the engineering-grid optimum is 445 kW / 1,465 kWh. The grid optimum need not be obtained by independently rounding each continuous coordinate. Its saved dual stationarity residual is near machine precision. This supports optimization quality for the stated linear model, rather than uniqueness or applicability to a network-constrained engineering design.

For this website revision, the no-storage baseline was recomputed directly from hourly inputs. **Forty-three saved schedules** were independently checked: three common-battery schedules, three individual engineering-grid schedules, one pooled schedule, and thirty-six monthly schedules. Power balance, cyclic stored-energy recursion, SOC and power bounds, nonnegative imports, curtailment not exceeding generation, and absence of simultaneous charging and discharging all passed at a $10^{-6}$ tolerance. The maximum power-balance residual was below $3\times10^{-13}$ kW.

This revision checks saved outputs and redraws the plots; it does not rerun the complete optimization and sensitivity pipeline. Small algebraic residuals establish internal numerical consistency. They do not measure forecast error, prove the representativeness of the input profiles, or validate performance against independently observed operations.

<h2 id="sensitivity">10. Sensitivity to billing and planning assumptions</h2>

### 10.1 Renewable billing can change the investment decision

Under the main basis, all available renewable generation is billed, so recovering curtailed electricity can avoid grid imports without an additional renewable-energy payment. Under utilized-energy billing, recovered renewable energy is also paid for. The marginal value of storing it is therefore lower. The archived sensitivity study fully re-optimizes capacity under the alternative billing rule.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/microgrid-storage/billing-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size">
<img src="{{ '/assets/img/research/microgrid-storage/billing-sensitivity.svg' | relative_url }}" alt="Continuous optimal battery energy under full-generation billing versus source-aware billing for utilized generation" width="1090" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 10.</span> Billing sensitivity using continuous LP decisions for both alternatives. Utilized-energy billing accounts for the source of curtailed energy; it is distinct from proportional allocation across wind and PV.</figcaption></figure>

With source-aware utilized-energy billing, A and pooled operation select **zero storage**. B contracts to approximately 161.6 kW / 397.2 kWh, and C to 58.8 kW / 69.8 kWh. Pooling still costs less than separate optimized operation on this alternative basis: approximately 15,107.7 versus 16,061.1 CNY/day. This supports the value of sharing under the tested accounting alternatives while showing that battery selection itself is not invariant to the billing rule.

### 10.2 Capacity choices depend on physical and financial assumptions

<div class="hy-model-table"><table><caption>Table 6. Selected archived sensitivity tests and their interpretation.</caption><thead><tr><th scope="col">Change</th><th scope="col">Observed model response</th><th scope="col">Interpretation</th></tr></thead><tbody>
<tr><td>Each-way efficiency reduced by one percentage point</td><td>Reported scan slopes imply approximately 12–15 CNY/day higher cost across individual parks.</td><td>Conversion losses have an economic effect well above the engineering-grid objective gap; the figure is a scan-based slope, not a universal local derivative.</td></tr>
<tr><td>Equal month weights replaced by calendar-normalized weights</td><td>A investment: 3.690 → 3.620 million CNY; B: 2.451 → 2.437; C unchanged.</td><td>Weighting shifts some equipment decisions without changing the broad seasonal configuration.</td></tr>
<tr><td>Five-year capital recovery with a 5% discount rate</td><td>A/B/C investments fall to approximately 3.182 / 1.887 / 2.284 million CNY.</td><td>Higher annual capital charges reduce selected capacity; the baseline uses straight-line allocation.</td></tr>
<tr><td>Annual wind/PV O&amp;M charge at 5% of new generation investment</td><td>Pooled reference-day expansion shifts to approximately 2,775 kW new wind and 921 kW / 2,094 kWh storage.</td><td>The tested charge applies to new wind and PV assets; battery O&amp;M and degradation remain absent.</td></tr>
<tr><td>Alternative supplied-park profiles for missing source types</td><td>The archived profile-substitution tests report annual-objective changes within approximately 1.7%.</td><td>This tests selected proxies, not the accuracy of local resource forecasts or extreme-weather performance.</td></tr>
</tbody></table></div>

An input inconsistency also matters: the reference-day and monthly source tables give different hour-23 wind output for Park B. The archived alternative-input test changes its cost by roughly 1.9%. The displayed primary results preserve each experiment's specified source table. This is a reason to retain input provenance and compare scenarios explicitly rather than assuming all representative days are interchangeable.

<h2 id="discussion">11. Discussion and scope</h2>

The principal operational finding is that simultaneous exchange across parks can remove a substantial imbalance before any temporal storage is bought. The principal planning finding is that the value of capacity is conditional on hourly utilization, renewable payments, resource representation, and capital allocation. Neither a small trial battery nor a single optimized battery is sufficient to explain the system's economics without those conditions.

Three distinctions are especially important. **Operating saving differs from investment-inclusive saving:** imports fall even when equipment cost erodes the benefit. **Renewable energy abundance differs from hourly self-sufficiency:** a high generation-to-load ratio can coexist with imports and curtailment. **Model feasibility differs from empirical validation:** a perfectly balanced dispatch can still rely on profiles or network assumptions that are unsuitable for actual operation.

The shared balance omits feeder capacity, power-flow constraints, transmission losses, congestion, and exchange settlement. The battery has constant efficiency and no modeled degradation, replacement schedule, or reliability requirement. Each representative day resets through a cyclic condition, excluding inter-day and seasonal energy carryover. Expanded generation follows assumed per-unit curves without site-specific resource assessment or integer equipment limits. These simplifications keep the problem linear and interpretable, but limit engineering conclusions.

The next substantive extension would use chronologically ordered annual data, measured resource and demand uncertainty, feeder-constrained exchanges, and degradation-aware dispatch. A stronger comparison would evaluate candidate designs on withheld operating periods and examine reliability as well as cost. Those are proposed extensions, distinct from completed tests in this archive.

<h2 id="conclusions">12. Conclusions</h2>

For these supplied profiles, ideal resource sharing creates most of the saving relative to separate operation without storage; a shared battery contributes an additional, explicitly priced benefit. Individually optimized storage and shared storage should be compared directly, because their costs and required capacities differ even after both systems have been optimized.

Under increased demand, expanding renewable generation and sizing storage together is more effective than either restricted design alone in the tested model. Seasonal availability, time-of-use prices, and renewable billing materially change the preferred capacities. The study therefore supports a decision sequence: **establish hourly imbalance, quantify spatial coordination, then optimize temporal storage and additional generation on a declared economic basis.**

<p class="hy-source-note"><strong>Source and evidence basis.</strong> This research note uses the current archived manuscript, original hourly spreadsheets, saved dispatch schedules, capacity tables, solver records, and sensitivity outputs from the project. Quantitative plots are redrawn from those records. The cover and roadmap are conceptual AI-generated illustrations. Website preparation adds independent arithmetic and feasibility checks without changing the source documents. This is a computational case study, not an independently field-validated or peer-reviewed publication. No manuscript download is attached at this stage.</p>
