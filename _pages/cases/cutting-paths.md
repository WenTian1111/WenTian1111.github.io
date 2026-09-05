---
layout: han-project
title: "Steel-Plate Cutting Path Planning"
description: "A geometric treatment of connected contours, separate components, and the travel needed to move between them."
permalink: /projects/modeling/cutting-paths/
discipline: "Graph optimization"
period: "2024"
question: "How can a tool visit every contour while reducing non-cutting travel?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Eulerian reasoning, greedy construction, parametric geometry"
outcome: "May Day Modeling · 2024 · competition manuscript"
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

Cutting time is not determined solely by the length of the required contours. A tool must also travel between components without cutting. This study separates those two forms of movement and investigates how graph structure and geometric entry points affect the non-cutting portion of a route.

The four supplied layouts develop the question progressively: first a connected contour arrangement, then separate circular and elliptical components, followed by additional internal rectangular parts. The work combines a topological question—whether a continuous traversal exists—with a geometric one—where to enter, leave, and connect the contours.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>Continuous traversal and minimum travel are different goals. Graph structure helps organize the cutting sequence; geometric entry points determine the additional movement between components.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable contour and route diagram"><img src="{{ '/assets/img/research/cutting-methods.svg' | relative_url }}" alt="Connected contours and links between separate components. Solid teal lines represent cutting; dashed ochre connections represent non-cutting motion. Schematic geometry, not a claimed optimum." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> Connected contours and links between separate components. Solid teal lines represent cutting; dashed ochre connections represent non-cutting motion. Schematic geometry, not a claimed optimum.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### Define what the objective counts

The competition defines idle travel as movement in the horizontal plane that does not cut material; vertical lifting is excluded. Each layout uses the specified lower-right starting point. The reported objective is therefore not total cutting time, total contour length, or a complete machine-cycle cost. All lengths shown here retain the source drawing's units, without assuming millimetres or centimetres.

This definition separates the contour segments that must be cut from the extra connections used to reach them. Figure 1 shows that distinction schematically: solid lines represent cutting, while dashed links represent non-cutting movement. The drawing explains the model structure and is not a scaled manufacturing plan.

### Use connectivity before optimizing distances

For connected layouts, I used Eulerian reasoning to examine the possibility of traversing the required edges continuously. Once components are disconnected, that traversal question no longer determines the whole route. The calculation must also choose links, component order, and suitable entry points.

The manuscript uses greedy route construction for these choices, supported by planar geometry. This offers a workable candidate construction, but a locally short next connection need not produce the shortest complete route. The graph and geometric parts of the problem must therefore be interpreted together.

### Parameterize curved boundaries

For the elliptical component, candidate entry locations are expressed through an ellipse parameter, and their approach distances are evaluated geometrically. The manuscript uses MATLAB calculations to search this parameterized problem, alongside geometric drawings of the selected routes. In the second layout, it reports an ellipse parameter of approximately 1.1552 radians and an approach contribution of 15.5535 drawing units.

The third layout adds twelve symmetric rectangular parts within the ellipse. Its construction includes the preceding approach, an additional connector, and travel associated with the internal rectangles. The fourth layout instead considers a different internal arrangement with four rectangular parts and a bridging construction. These are distinct geometric cases, not successive benchmark runs on an unchanged instance.

<h2 id="findings">Selected results</h2>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable research result figure"><img src="{{ '/assets/img/research/cutting-travel.svg' | relative_url }}" alt="Decomposition of the third layout's reported non-cutting route length. Values are in the source drawing's units. This displays the paper's construction and does not establish a globally optimal route." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 2.</span> Decomposition of the third layout's reported non-cutting route length. Values are in the source drawing's units. This displays the paper's construction and does not establish a globally optimal route.</figcaption>
</figure>

### Interpreting the route-length decomposition

The result figure focuses on the third layout because the reported total can be broken into interpretable contributions. The preceding approach accounts for approximately 31.55 drawing units, the additional link for 6.1406, and the internal rectangular travel for 44. Their sum is 81.6906, reported as 81.69 after rounding. Figure 2 displays this accounting as a cumulative route-length decomposition rather than an unexplained total.

The internal-rectangle contribution is the largest component in that construction. This helps identify where the reported route spends its idle distance; it does not prove that the same contribution could be removed while preserving feasibility. Nor is the 31.55-unit component a baseline algorithm against which an improvement percentage should be calculated.

### Four layouts, four different questions

Across the four tasks, the manuscript reports idle-travel lengths of approximately 64.03, 31.55, 81.69, and 47.55 drawing units. The second total combines the elliptical approach with the circular-component contribution. The third and fourth reflect different internal arrangements. A lower total between tasks cannot establish a better algorithm when the geometry and required operations have changed.

The central result is the construction of routes that connect contour topology with explicit geometric choices. The decomposition makes that reasoning inspectable while avoiding an unsupported claim of global optimality.

<h2 id="discussion">Discussion</h2>

A greedy construction is not, by itself, proof of a globally shortest route. A useful continuation would compare complete routes for the same layout against an exact or exhaustive small-instance baseline. Each candidate would need to satisfy the same contour, starting-point, and bridging requirements before its length could be meaningfully compared.

For a manufacturing application, the objective would also need to account for kerf, cut order, thermal effects, and part stability, as well as motion excluded by the competition's idle-travel definition. Those extensions were not validated in this study. The portfolio presents the submitted geometric reasoning and selected route accounting, not a machine-ready cutting program.

<p class="hy-source-note">Research record: May Day Mathematical Modeling competition manuscript, 2024. Original study: <em>Steel-plate cutting modeling using an improved greedy algorithm based on Euler's theorem</em>. Independently developed by Han Yang.</p>
