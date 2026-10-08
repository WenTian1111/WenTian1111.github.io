---
layout: han-project
title: Steel-Plate Cutting Path Planning
description: A geometric study of contour scheduling, continuous entry points, split visits, and finite-width bridge unions, with explicit limits on optimality claims.
permalink: /projects/modeling/cutting-paths/
discipline: Manufacturing geometry · Route optimization
period: 2024 study
question: How can operation structure and continuous boundary geometry jointly reduce non-cutting travel?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Contour scheduling, boundary-point optimization, candidate screening, dynamic-programming bounds, finite-width geometric unions
outcome: Four reconstructed routes · verified travel accounting · sensitivity analysis · qualified search evidence
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Geometry and study design
    id: geometry
  - label: 3. Joint structure and entry-point model
    id: model
  - label: 4. Search and verification methods
    id: search
  - label: 5. Continuous entry geometry
    id: first
  - label: 6. Split-contour scheduling
    id: second
  - label: 7. Nested pieces and the lower-bound gap
    id: third
  - label: 8. Finite-width bridge design
    id: bridges
  - label: 9. Geometry sensitivity
    id: sensitivity
  - label: 10. Independent numerical checks
    id: verification
  - label: 11. Discussion
    id: discussion
  - label: 12. Conclusions
    id: conclusions
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

The shortest cutting schedule is not determined by contour order alone. Each operation also has a geometric interface: a point at which the cutting head enters and, for an open segment, a potentially different point at which it leaves. This study joins discrete operation scheduling with continuous boundary-point selection across four idealized steel-plate layouts. The progression begins with a rectangular example that admits an analytic solution, introduces split visits to an irregular outer contour, adds nested rectangular pieces and precedence, and finally connects pieces through finite-width material bridges.

The recorded feasible non-cutting distances are **64.0312, 130.5356, 203.2436, and 133.9784**, respectively, in the supplied coordinate units. In the second layout, a split-contour schedule reduces travel by 13.34% relative to the evaluated single-loop alternative. In the third, the selected route improves on a nearest-neighbor reference by 15.26%, while a relaxed lower bound leaves a 27.21% gap relative to the feasible objective. Three-bridge designs outperform the tested four-bridge cycle under the fourth layout's travel objective. Fresh independent reconstruction reproduces all four travel totals to within $2.85\times10^{-14}$ coordinate units and checks 28 stored entry points against their required boundaries. These checks establish route consistency, not unrestricted global optimality. The article therefore distinguishes analytic evidence, numerical candidate screening, heuristic refinement, and the further physical assumptions needed for a manufacturing application.

<h2 id="introduction">1. Introduction</h2>

A cutting head alternates between processing material and moving to its next operation. If every prescribed line is cut exactly once, the processing distance is fixed for a given material-boundary construction. The connecting travel is the part that can change with the schedule. Reducing it can be useful, but it is a different objective from minimizing production time, energy consumption, thermal distortion, or material loss.

The geometric issue is easy to miss. A closed contour is not a point target: its entry may slide along an edge, a circular arc, or an ellipse. A representative corner can make a convenient graph vertex, yet it may discard the best interface. Moreover, the best point for an operation depends on both its predecessor and its successor. Choosing independently nearest points and then optimizing the order does not generally solve the same problem as choosing them jointly.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/cutting-paths/cover.webp' | relative_url }}" alt="Conceptual steel-plate cutting head and toolpath setting" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual manufacturing setting. The illustration is not an observed machine trial or a to-scale reconstruction of the supplied layouts.</figcaption></figure>

The study addresses three linked questions. How much does a continuous entry point change a simple schedule? When does splitting a contour create useful interfaces? How do structural constraints and finite-width connections alter the feasible operations? The four layouts isolate these questions progressively. Their distances should be read within each layout; comparing their absolute totals as though they were scores on the same task would be misleading.

<h2 id="geometry">2. Geometry and study design</h2>

### 2.1 Inputs and coordinate conventions

The lower-left plate corner defines the origin; $x$ increases to the right and $y$ upward. Layout I occupies an 80-by-50 rectangle and contains an inner rectangle from $(20,15)$ to $(60,35)$. The machine starts at $(80,0)$. Three outer edges are prescribed cutting lines; the left edge is a plate boundary and is not cut.

Layouts II–IV use a 100-by-80 plate, starting at $(100,0)$. Their common irregular outer contour has slots along its top and bottom and two notches on its left edge. Four circles of radius 3 have centers $(10,75)$, $(35,75)$, $(60,75)$, and $(85,75)$. An ellipse centered at $(60,40)$ has horizontal and vertical semiaxes 15 and 20. Layout III adds twelve 4-by-3 rectangles inside that ellipse. Layout IV replaces them with four unequal rectangular pieces and explicitly constructed bridge strips.

<div class="hy-model-table"><table><caption>Table 1. The four computational layouts and their added decisions.</caption><thead><tr><th scope="col">Layout</th><th scope="col">Geometry</th><th scope="col">Additional decision or condition</th></tr></thead><tbody>
<tr><td>I</td><td>Three outer edges and one inner rectangle</td><td>Split open-chain runs; continuous rectangle entry</td></tr>
<tr><td>II</td><td>Irregular outer contour, four circles, one ellipse</td><td>One outer-loop visit or two complementary arcs</td></tr>
<tr><td>III</td><td>Layout II plus twelve small rectangles</td><td>All rectangles processed before the ellipse</td></tr>
<tr><td>IV</td><td>Layout II plus four bridge-connected pieces</td><td>Bridge topology and position; connected piece before ellipse</td></tr>
</tbody></table></div>

All reported lengths retain the problem's coordinate units. The source does not establish a conversion to millimeters or a calibrated machine speed. The bridge width of 2 and vertex-clearance requirement of 1 are therefore geometric parameters in these same units.

### 2.2 Scope of the idealization

The head travels straight between interfaces while not cutting and may pass above any plate region. Prescribed cutting lines are processed once. A closed inner contour is normally completed in one visit, whereas the outer contour can be split within the evaluated structure family. The plate remains fixed, with no thermal deformation or piece motion. Pierce time and lead-in and lead-out motions are omitted.

These assumptions permit a geometric comparison of schedules. They also explain why the recorded outer-first or split-outer sequences should not be transferred directly to a real machine without checking workholding, part release, and process order. The model encodes the stated precedence conditions, not every possible manufacturing rule.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/cutting-paths/workflow.webp' | relative_url }}" alt="Conceptual overview of geometry construction, discrete scheduling, continuous refinement, and route checks" width="1672" height="941" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Research overview. The quantitative results below use the reconstructed boundaries and saved route interfaces rather than paths inferred from this conceptual illustration.</figcaption></figure>

<h2 id="model">3. Joint structure and entry-point model</h2>

### 3.1 Account for interfaces, not just visited shapes

Let $S$ be the initial location, $q_j$ the entry to operation $j$, and $q'_j$ its exit. For a closed contour completed in one visit, $q'_j=q_j$. An open chain or a complementary outer arc generally has different endpoints. With $q'_0=S$, the objective is

<div class="hy-equation">
\[
L_{\mathrm{idle}}=\sum_{j=1}^{m}\|q'_{j-1}-q_j\|.
\tag{1}
\]
</div>

No terminal return is added unless the operation structure itself requires it. Conversely, entering a circle from a split point and returning to that point before continuing the remaining outer arc creates **two paid moves**. Omitting the return would undercount that schedule. Cutting along an arc changes the head's location even though the arc contributes nothing to the non-cutting objective.

### 3.2 Optimize an entry on its actual boundary

For a closed contour $C_i(s)$ between neighboring interfaces $a$ and $b$, its local entry problem is

<div class="hy-equation">
\[
\begin{aligned}
s_i^*&\in\arg\min_s f_i(s),\\
f_i(s)&=\|a-C_i(s)\|+\|C_i(s)-b\|.
\end{aligned}
\tag{2}
\]
</div>

On a polygon edge, the sum of distances is convex in its line-segment parameter. Each edge can therefore be minimized and compared with the other edges. This local convexity does not make the complete mixed scheduling problem convex: choosing an edge, ordering operations, and allowing split visits introduce separate decisions.

The circle and ellipse implementations use a periodic parameter, a coarse grid, several local brackets, and golden-section refinement. The ellipse parameter is proportional to angle, not exact arc length. That distinction does not invalidate a point on the ellipse, but it matters when interpreting sample density or constructing conservative distance bounds.

### 3.3 A useful mixed decision structure

An evaluated plan comprises an operation order, a split pattern, any outer split position, and entry parameters. In Layout IV it also includes bridge topology and bridge locations. Joint optimization is organized as a finite structure search followed by boundary-point refinement within each selected structure.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/selected-routes.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/cutting-paths/selected-routes.svg' | relative_url }}" alt="Four supplied plate layouts with reconstructed contours and selected non-cutting moves" width="1152" height="994" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Reconstructed input geometry and selected interfaces for all four layouts. Orange arrows represent paid non-cutting moves; the square marks the initial location. Cutting direction along a complete contour is not depicted. The dotted left boundary in Layout I is not a prescribed cutting line.</figcaption></figure>

<h2 id="search">4. Search and verification methods</h2>

### 4.1 Separate structural search from continuous refinement

Layout I is small enough to enumerate its open-chain partitions, directions, and interleavings with the rectangle. The archive records 244 structures. Later layouts use a generalized solver whose outer contour is either completed once or split into two complementary arcs, with groups of inner operations inserted between those arcs. For a fixed order, coordinate descent revisits each entry point using its current neighbors until the travel and coordinate changes stabilize.

This arrangement is computationally practical, but its layers provide different evidence. Enumerating every structure in a specified finite family does not enumerate every continuous split location. A converged coordinate descent calculation is not automatically a globally solved continuous subproblem. Both distinctions are retained in the results.

### 4.2 Lower bounds and screening

A relaxation replaces a jointly shared entry point with independently favorable contour-to-contour connections. For a closed-contour order, the schematic bound is

<div class="hy-equation">
\[
\begin{aligned}
D_{ij}&=\min_{p\in C_i,\ q\in C_j}\|p-q\|,\\
B(\sigma)&=D_{S,\sigma_1}+\sum_jD_{\sigma_j,\sigma_{j+1}}.
\end{aligned}
\tag{3}
\]
</div>

Each pair can choose its own best point in the relaxation. A realizable closed-contour visit, however, must use the same entry and exit interface for its two neighboring links. This decoupling can make a bound much lower than a feasible route. For split structures, the implementation includes the corresponding endpoint transitions and group distances.

The archive samples noncircular boundaries and subtracts half-grid corrections when constructing screening values. A rigorous certificate would require these corrections to bound geometric sampling error for the actual parameterization, together with complete coverage of the claimed structure space. The present article reports the stored screening evidence without promoting it to a new interval-certified continuous optimum.

### 4.3 Reconstruct before interpreting

The first verification question is whether the saved plan really costs what it claims. For this revision, a separate reconstruction walks the stored interfaces, explicitly switches from entry to exit at each cutting operation, and sums only paid jumps. Boundary and precedence checks follow. This separates arithmetic consistency and geometric feasibility from the harder question of whether another plan could do better.

<h2 id="first">5. Layout I: continuous entry geometry</h2>

The selected plan starts at $(80,0)$, cuts the bottom edge to $(0,0)$, visits the inner rectangle through its left-edge midpoint $(20,25)$, and moves to $(0,50)$. It then cuts the top and right edges back to the initial corner. There are two nonzero jumps; their lengths are equal.

For an entry $(20,y)$ on the left rectangle edge, their sum is

<div class="hy-equation">
\[
\begin{aligned}
f(y)&=\sqrt{400+y^2}\\
&\quad+\sqrt{400+(50-y)^2},\\
15&\le y\le35.
\end{aligned}
\tag{4}
\]
</div>

The function is convex and symmetric about $y=25$, giving $L^*=2\sqrt{1025}=64.0312424$. The saved entry differs from the exact midpoint only at the numerical refinement scale. A corner-only comparison gives $25+\sqrt{1625}=65.3112887$, approximately 1.28 units longer. The improvement is modest in absolute size, yet it demonstrates why the target must remain a boundary rather than an arbitrary representative vertex.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/entry-geometry.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/cutting-paths/entry-geometry.svg' | relative_url }}" alt="Convex two-jump distance on the rectangle edge and comparison with corner-only entry" width="1186" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Analytic entry-distance function and the two entry conventions. The midpoint follows from symmetry and convexity, independently of the stored numerical route.</figcaption></figure>

The analytic match is stronger evidence than repeated convergence alone for this simple example. Its scope is the specified layout and admissible cutting rules. It should not be generalized into a claim that midpoint entry is always best for rectangles with different neighboring interfaces.

<h2 id="second">6. Layout II: split-contour scheduling</h2>

### 6.1 Why an interrupted outer visit can help

The selected outer split point is $A=(7.8333,80)$. The head cuts from $S=(100,0)$ along the right and top portions of the outer contour to $A$, visits circle C1, and returns to $A$. The complementary outer arc then carries it back to $S$ while cutting. From there the inner chain visits E, C4, C3, and C2. This uses the outer contour's changing endpoint as part of the scheduling decision.

<div class="hy-equation">
\[
\begin{aligned}
L_{\mathrm{II}}&=2\|A-p_{C1}\|+\|S-p_E\|\\
&\quad+\|p_E-p_{C4}\|\\
&\quad+\|p_{C4}-p_{C3}\|\\
&\quad+\|p_{C3}-p_{C2}\|.
\end{aligned}
\tag{5}
\]
</div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/split-accounting.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/cutting-paths/split-accounting.svg' | relative_url }}" alt="Six separately reconstructed paid transitions in the selected split-contour route" width="1138" height="437" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Independent accounting of the six nonzero jumps in Layout II. The outer cutting arcs move the head between interfaces but are excluded from this travel objective. Both legs of the embedded C1 visit are included.</figcaption></figure>

The selected distance is 130.5355649. The evaluated single-loop alternative costs 150.6254139, so the split structure saves 20.0898490 units, or 13.34%. The nearest-neighbor reference costs 177.6145593, corresponding to a 26.51% reduction. These are comparisons against specific evaluated references, not production-time savings.

### 6.2 Interpret the stored stopping evidence

The archive counts $120$ inner orders, $120$ sampled outer split positions, and six visit-group patterns, for $120\times120\times6=86{,}400$ candidate records. It refines 594 candidates before the next stored screening bound, 130.5363128, exceeds the selected objective by approximately 0.0007479. It also reports identical evaluated objectives across several entry-grid refinements and repeated starts.

These records support stability within the implemented search. Their very small stopping margin makes bound validity especially important. Continuous outer split positions between samples, nonuniform ellipse sampling, and local entry refinement need explicit treatment before claiming an unrestricted continuous optimum. This revision independently verifies the selected route, while treating the archive's closure as **conditional numerical screening evidence**.

<h2 id="third">7. Layout III: nested pieces and the lower-bound gap</h2>

Twelve rectangular pieces add a larger ordering problem inside the ellipse. Their centers form four columns at $x=51,57,63,69$ and three rows at $y=45,40,35$. All twelve must precede the ellipse. The selected route completes the outer contour, traverses the lower row right-to-left, the middle row left-to-right, and the upper row right-to-left, then visits E, C4, C3, C2, and C1.

The snake-like chain is geometrically economical because successive interfaces on nearby rectangles can align. That interpretation follows from the reconstructed interfaces; it is not a general proof that row snakes minimize travel for every nested arrangement.

<div class="hy-model-table"><table><caption>Table 2. Feasible objectives and their named comparisons.</caption><thead><tr><th scope="col">Layout</th><th scope="col">Selected feasible distance</th><th scope="col">Reference</th><th scope="col">Difference</th></tr></thead><tbody>
<tr><td>I</td><td>64.0312</td><td>Corner-only entry: 65.3113</td><td>1.2800 shorter</td></tr>
<tr><td>II</td><td>130.5356</td><td>Single outer loop: 150.6254</td><td>13.34% shorter</td></tr>
<tr><td>II</td><td>130.5356</td><td>Nearest neighbor: 177.6146</td><td>26.51% shorter</td></tr>
<tr><td>III</td><td>203.2436</td><td>Nearest neighbor: 239.8391</td><td>15.26% shorter</td></tr>
<tr><td>IV</td><td>133.9784</td><td>Four-bridge cycle: 136.6798</td><td>2.7015 shorter</td></tr>
</tbody></table></div>

A Held–Karp-style dynamic program on relaxed contour connections supplies the stored lower bound 147.9434814, with 524,304 expanded states. The feasible route has distance 203.2436082. Their difference is 55.3001268, or 27.21% of the feasible objective. Because the relaxation lets successive pairwise connections use independently favorable points, it need not describe a realizable cutting route.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/reference-and-bounds.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
<img src="{{ '/assets/img/research/cutting-paths/reference-and-bounds.svg' | relative_url }}" alt="Layout II reference comparisons and Layout III feasible objectives versus its relaxed lower bound" width="1186" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 6.</span> Within-layout comparisons. The orange lower-bound bar in Layout III is not a feasible schedule. Its separation from the selected route identifies an unresolved optimality gap, rather than an additional achieved travel reduction.</figcaption></figure>

The archive refines a screened set of 24 candidate orders and also tests split variants. It does not establish that every admissible order and continuous interface has been solved globally. The result is therefore an improved feasible route. A stronger conclusion would require either a tighter relaxation or a larger certified search, not merely another local optimization start.

<h2 id="bridges">8. Layout IV: finite-width bridge design</h2>

### 8.1 A bridge is material, not a zero-width graph edge

The four pieces have bounding rectangles $(48,43,57,52)$, $(60,43,69,54)$, $(48,27,57,40)$, and $(60,34,71,40)$. A bridge is a strip of width 2 across an eligible gap. Its location must remain at least 1 from the relevant piece vertices. The connected material is constructed as

<div class="hy-equation">
\[
G=\left(\bigcup_{i=1}^{4}R_i\right)\cup\left(\bigcup_k B_k\right).
\tag{6}
\]
</div>

Planning uses the boundary of this union. Internal shared edges disappear from the material boundary. A cyclic connection can additionally enclose a hole, whose boundary must be treated as another cutting contour. Omitting that hole would change the operation set.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/bridge-boundaries.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size">
<img src="{{ '/assets/img/research/cutting-paths/bridge-boundaries.svg' | relative_url }}" alt="Independent finite-width material unions for a three-bridge tree and a four-bridge cycle, including the cycle's inner boundary" width="1096" height="514" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 7.</span> Fresh geometric unions at recorded bridge positions. The tree has no hole and boundary length 160. The cycle has outer boundary length 125 plus an inner boundary of length 37, for total boundary length 162. Boundary length is a separate quantity from non-cutting travel.</figcaption></figure>

### 8.2 Topology, position, and route are coupled

The tested family includes four three-edge spanning trees and one four-edge cycle on the eligible adjacency graph. Continuous bridge positions are searched using successively smaller steps of 1.0, 0.25, and 0.05. Each material union is reconstructed before the cutting schedule is reevaluated. This is topology enumeration with numerical position and route refinement, not an exhaustive continuous search over every possible bridge design.

The selected tree omits the upper horizontal bridge. Its remaining bridge parameters are $y=36.0$ for the lower horizontal strip and $x=51.5,63.5$ for the two vertical strips. The selected travel is 133.9783944. All four recorded tree designs achieve the same objective, even though the unequal piece dimensions do not justify describing them as exactly mirrored copies.

<div class="hy-model-table"><table><caption>Table 3. Material-boundary checks and recorded route objectives for the two displayed bridge constructions.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Selected tree</th><th scope="col">Four-edge cycle</th></tr></thead><tbody>
<tr><td>Bridges</td><td>3</td><td>4</td></tr>
<tr><td>Union area</td><td>381</td><td>387</td></tr>
<tr><td>Inner boundaries</td><td>0</td><td>1</td></tr>
<tr><td>Outer boundary length</td><td>160</td><td>125</td></tr>
<tr><td>Total boundary length, including holes</td><td>160</td><td>162</td></tr>
<tr><td>Selected non-cutting distance</td><td>133.9784</td><td>136.6798</td></tr>
</tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/topology-comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size">
<img src="{{ '/assets/img/research/cutting-paths/topology-comparison.svg' | relative_url }}" alt="Recorded non-cutting distances of four three-bridge trees and the four-bridge cycle" width="1138" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 8.</span> Five evaluated bridge topologies under the same travel objective. A zero-based vertical scale preserves the size of the small difference; printed values show it precisely. Equal tree totals are observed search results, not a symmetry proof.</figcaption></figure>

A separate open-chain interpretation of bridging gives a best recorded reference of 192.6406. It uses different operation semantics, so the 43.78% larger value is a modeling comparison, not the performance of another physically equivalent algorithm. Similarly, adding material strength, heat effects, or release constraints could favor a different topology despite the present travel ranking.

<h2 id="sensitivity">9. Geometry sensitivity</h2>

### 9.1 Two response conventions

A perturbed geometry can be evaluated while retaining the original structural decision or by selecting and refining another candidate. These answer different questions. The first asks how the existing plan responds; the second asks what can be recovered through adaptation.

In the circle-row experiment, the fixed convention preserves the split position and contour order but projects the saved entries onto the moved boundaries. It is therefore not a fully frozen coordinate plan. The reoptimization convention screens 40 candidates and further refines four; it does not rebuild the full baseline screening closure for every perturbation.

<div class="hy-model-table"><table><caption>Table 4. Layout II response to a common circle-row displacement, in coordinate units.</caption><thead><tr><th scope="col">Displacement</th><th scope="col">Fixed structure, projected entries</th><th scope="col">Reselected/refined candidate</th></tr></thead><tbody>
<tr><td>−1.0</td><td>131.8381</td><td>131.4294</td></tr>
<tr><td>−0.5</td><td>131.0726</td><td>130.9766</td></tr>
<tr><td>0.0</td><td>130.5356</td><td>130.5356</td></tr>
<tr><td>+0.5</td><td>130.1956</td><td>130.1096</td></tr>
<tr><td>+1.0</td><td>130.0596</td><td>129.7031</td></tr>
</tbody></table></div>

The maximum absolute change in the fixed-structure series is approximately 1.3025 units, or 0.998% of its zero-displacement value. The reselected candidate is no worse than the corresponding fixed response at these five points, and its zero-displacement value reproduces the baseline exactly. It can still cost more than the unperturbed baseline when the geometry becomes less favorable; adaptation is not a guarantee that all perturbations improve travel.

### 9.2 Left-column displacement

For Layout IV, moving the left pair of pieces horizontally by −1, 0, or +1 yields the same recorded reoptimized travel, 133.9783944. The material union and bridge intervals are rebuilt in that experiment. The unchanged total is consistent with the selected travel interface lying on an unchanged right-hand piece. It demonstrates local insensitivity of this objective under those three tested displacements, not invariance to arbitrary dimensional or bridge-width changes.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/geometry-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size">
<img src="{{ '/assets/img/research/cutting-paths/geometry-sensitivity.svg' | relative_url }}" alt="Fixed-structure and reselected-candidate response to circle-row motion, alongside the recorded Layout IV left-column displacement test" width="1186" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 9.</span> Saved, corrected sensitivity series. The two left-panel curves use distinct response conventions. The right panel includes only three evaluated points; the connecting line does not establish a continuously constant response.</figcaption></figure>

The current archive documents a correction to an earlier perturbation calculation that omitted part of the split-route accounting. This page uses the corrected series, with the zero-displacement self-check. That repair is a concrete example of why matching a perturbation's baseline is necessary before interpreting its numerical differences.

<h2 id="verification">10. Independent numerical checks</h2>

### 10.1 Fresh route and boundary reconstruction

This revision adds selected checks independent of the archived optimizer's objective routine. Stored interfaces are walked with direct Euclidean differences, including both legs of an embedded visit and the correct exit after a cutting arc. The maximum discrepancy across four layouts is $2.84\times10^{-14}$ coordinate units.

Circle interfaces are checked by radius residuals, ellipse interfaces by their implicit equation, and rectangular and union interfaces by point-to-boundary distance. Across 28 entries in Layouts II–IV, the largest residual is approximately $5.8\times10^{-15}$. Required rectangle-before-ellipse and union-before-ellipse orderings pass. The tree and cycle union areas, boundary lengths, and hole counts are independently rebuilt from the supplied rectangles and strips.

<div class="hy-model-table"><table><caption>Table 5. New checks performed for this research-note revision.</caption><thead><tr><th scope="col">Check</th><th scope="col">Observed result</th><th scope="col">What it supports</th></tr></thead><tbody>
<tr><td>Four stored routes, direct travel summation</td><td>Maximum difference 2.84 × 10⁻¹⁴</td><td>Travel accounting matches the recorded plans</td></tr>
<tr><td>28 contour-entry boundary checks</td><td>Maximum residual about 5.8 × 10⁻¹⁵</td><td>Stored interfaces lie on their specified contours</td></tr>
<tr><td>Nested-piece and connected-piece precedence</td><td>Pass for the selected orders</td><td>These specific schedule conditions hold</td></tr>
<tr><td>Layout I analytic reconstruction</td><td>2√1025 equals the saved objective</td><td>Independent simple-case agreement</td></tr>
<tr><td>Bridge unions including interior rings</td><td>Tree: 0 holes; cycle: 1 hole</td><td>Complete boundary accounting for the displayed constructions</td></tr>
<tr><td>Corrected sensitivity zero-displacement check</td><td>Reoptimized difference 0</td><td>Perturbation and baseline use consistent accounting</td></tr>
</tbody></table></div>

These checks do not repeat the complete 86,400-record search, solve every bridge-position alternative, or prove every sampling bound. They also do not validate a real machine. Stating their scope keeps a strong route-consistency result from being mistaken for stronger search or physical evidence.

### 10.2 Convergence is useful but has a boundary

The archive reports the same Layout II objective for entry-refinement grid sizes 360, 720, 2,880, 11,520, and 46,080. This is evidence that the evaluated numerical result is stable under those refinements. It does not test every outer split position, every alternative structure, or every modeling assumption.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/search-evidence.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size">
<img src="{{ '/assets/img/research/cutting-paths/search-evidence.svg' | relative_url }}" alt="Saved entry-grid convergence and the small numerical gap between the selected route and the next screening bound" width="1186" height="437" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 10.</span> Two forms of archived search evidence. The left panel concerns stability of the evaluated objective. The right panel concerns a conditional screening stopping criterion. Neither substitutes for validated error bounds and complete coverage of the claimed continuous search space.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 6. Evidence level retained for each principal result.</caption><thead><tr><th scope="col">Result</th><th scope="col">Evidence</th><th scope="col">Remaining boundary</th></tr></thead><tbody>
<tr><td>Layout I midpoint and selected travel</td><td>Analytic convex subproblem and archived finite enumeration</td><td>Specific idealized geometry and operation rules</td></tr>
<tr><td>Layout II split route</td><td>Feasible reconstructed route; stored closure and convergence</td><td>Continuous split coverage, conservative sampling bounds, local refinement</td></tr>
<tr><td>Layout III improved route</td><td>Feasible route above a relaxed dynamic-programming bound</td><td>27.21% gap remains open</td></tr>
<tr><td>Layout IV three-bridge selection</td><td>Five recorded topologies with position and route refinement</td><td>Restricted adjacency graph and numerical continuous search</td></tr>
</tbody></table></div>

<h2 id="discussion">11. Discussion</h2>

The central result is the interaction between operation structure and boundary geometry. Continuous entries matter even in a small rectangle example. Splitting an outer visit changes which interfaces are available to connect inner operations. Adding precedence alters the useful schedule family. Adding finite-width material bridges changes the contours themselves, including whether internal rings must be processed.

The numerical results also reveal why a lower objective is only one part of a research claim. Baseline improvement, feasibility, repeated-start stability, and optimality are distinct. A loose relaxation can leave a large gap; a tiny screening gap can demand more careful numerical bounds. Equal recorded objectives can arise without exact geometric symmetry. Corrected sensitivity calculations can restore baseline consistency without turning a screened adaptive search into a global certificate.

A production extension should combine travel with machine dynamics and process costs. A schematic objective might be

<div class="hy-equation">
\[
\begin{aligned}
T&=T_{\mathrm{cut}}+T_{\mathrm{travel}}\\
&\quad+T_{\mathrm{pierce}}+T_{\mathrm{handling}}.
\end{aligned}
\tag{7}
\]
</div>

This is a proposed extension, not a computed result here. The conversion from distance to time would require measured feed rates, acceleration and cornering behavior, and pierce delays. Thermal and workholding constraints could remove apparently attractive schedules from the feasible set. Machine trials or a validated process simulator would then be needed to assess practical benefit.

For stronger numerical evidence, the most direct next steps are explicit arc-length or Lipschitz sampling bounds, interval treatment of continuous split positions, globally bounded entry subproblems, and a tighter coupled relaxation for the nested-piece example. These address the actual limits of the present calculation more directly than adding another decorative algorithm label.

<h2 id="conclusions">12. Conclusions</h2>

Four layouts connect continuous contour interfaces with increasingly complex schedule and material decisions. Their selected non-cutting distances are reproduced from the saved plans; the first has an independent analytic explanation, the second benefits from a split outer visit, the third retains a substantial relaxed-bound gap, and the fourth demonstrates the geometric effect of finite-width bridge unions.

The most transferable lesson is to keep **operation entry, operation exit, contour order, and material boundary construction** consistent in the same objective. The selected routes provide computational evidence under an idealized geometric model. Their numerical accuracy is stronger than their global-search or manufacturing validation, and the presentation preserves that distinction.

<p class="hy-source-note"><strong>Source and evidence basis.</strong> The current supplied manuscript, geometry definitions, saved route interfaces, corrected sensitivity records, and archived verification report. New figures and selected independent checks were generated for this page without changing the original project materials. Cover and workflow images are conceptual AI-generated illustrations. This is a computational research note, not a peer-reviewed publication, a machine-performance experiment, or a certified production schedule. No manuscript download is attached at this stage.</p>
