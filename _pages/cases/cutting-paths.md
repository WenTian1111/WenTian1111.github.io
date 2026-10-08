---
layout: han-project
title: Steel-Plate Cutting Path Planning
description: Four cutting layouts connect discrete scheduling with continuous geometry, while separating a feasible route from an optimality certificate.
permalink: /projects/modeling/cutting-paths/
discipline: Manufacturing geometry · Route optimization
period: 2024 study
question: How can contour order and continuous entry points reduce travel between cuts?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Contour scheduling, geometric entry optimization, lower bounds, finite-width bridge unions
outcome: Four layouts · continuous entry points · qualified optimality evidence
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: optimize the distance that can change"
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: 3. Formulate structure and geometry together
    id: objective
  - label: "4. Layout I: a continuous entry point matters"
    id: first
  - label: "5. Layout II: split visits and certify a candidate family"
    id: second
  - label: "6. Layout III: an improved route with an open gap"
    id: third
  - label: "7. Layout IV: bridges change the boundary"
    id: bridges
  - label: 8. Verification, limitations, and next steps
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Cutting a collection of contours creates two different lengths: the material-processing distance and the non-cutting travel between operations. This study targets the latter. Four layouts progressively introduce geometric entry points, split contour visits, precedence constraints, and finite-width bridges between pieces. Discrete structure selection and continuous geometric refinement are treated together because neither the contour order nor the entry point alone determines travel.

Selected non-cutting distances are 64.0312, 130.5356, 203.2436, and 133.9784 in the problem's coordinate units. The second layout has a certificate within the implemented candidate family; the third retains a sizable lower-bound gap and is presented as a feasible improved route. This distinction is part of the result rather than a footnote: a smaller objective than a baseline is not, by itself, evidence of global optimality.

<h2 id="background">1. Background: optimize the distance that can change</h2>

Some cutting length is prescribed by the contours. Travel between those contours, however, depends on the machine's order of visits, where each visit begins, and whether a contour can be split into multiple operations. The study therefore measures non-cutting travel rather than treating all visible path length as an interchangeable objective.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/cutting-paths/cover.webp' | relative_url }}" alt="Conceptual cutting-head and steel-plate setting" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual cutting-head and steel-plate setting. The illustration is not a machine trial or a to-scale reconstruction of one of the four supplied layouts.</figcaption></figure>

The inputs are idealized contour geometries including polylines, rectangles, circles, and ellipses. Coordinates are retained in their supplied units. The source does not justify converting the reported lengths into millimeters, minutes, or production cost. A real manufacturing objective would need feed rates, acceleration, pierce delays, heat effects, and machine constraints.

<h2 id="roadmap">2. Study roadmap</h2>

The first layout isolates continuous entry geometry. The second adds structural alternatives such as split visits. The third introduces further order constraints and demonstrates the importance of lower bounds. The fourth asks how finite-width connections change the contour to be cut.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/cutting-paths/workflow.webp' | relative_url }}" alt="Overview of contour preprocessing, candidate structures, continuous geometric refinement, and route verification" width="1672" height="941" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Overview of contour preprocessing, candidate structures, continuous geometric refinement, and route verification. Diagram routes are explanatory; numerical distances below come from saved output tables.</figcaption></figure>

<h2 id="objective">3. Formulate structure and geometry together</h2>

Let an operation finish at $q_j^{\mathrm{out}}$ and the next begin at $q_{j+1}^{\mathrm{in}}$. The objective sums the straight non-cutting moves required by the selected sequence:

<div class="hy-equation">
\[
L_{\mathrm{idle}}=\sum_j\left\|q_j^{\mathrm{out}}-q_{j+1}^{\mathrm{in}}\right\|.
\tag{1}
\]
</div>

For a closed contour, the entry point may lie anywhere on its parameterized boundary $C(s)$, with $0\le s<\operatorname{perimeter}(C)$. Restricting entry to corners converts a continuous geometric decision into an artificial discrete rule and can miss a shorter move. The sequence must also respect required precedence, such as processing an inner shape before its enclosing boundary.

The computational procedure separates a candidate's combinatorial structure from the continuous entry-point problem inside it. Simple lower bounds discard structures that cannot beat the best known route; promising structures receive a more detailed geometric refinement. Finally, an independent route walk recomputes length and checks whether the prescribed operations and constraints are respected.

This layered design makes the evidence interpretable: structural enumeration, continuous refinement, and physical feasibility are different checks. Each has to be specified before an optimality claim can be assessed.

<h2 id="first">4. Layout I: a continuous entry point matters</h2>

The first example gives a compact demonstration of the geometric issue. The selected idle distance is $2\sqrt{1025}=64.0312$. A corner-only alternative gives approximately 65.3112. The improvement comes from allowing the entry location to move along an edge rather than treating the contour as a list of corner candidates.

<div class="hy-equation">
\[
L_{\mathrm{I}}=2\sqrt{1025}\approx64.0312.
\tag{2}
\]
</div>

The lesson is broader than the size of this particular reduction: when the object to be visited is a curve, the best connection is a nearest-point or jointly optimized boundary-point problem. A graph of representative vertices may be useful as a bound or initialization, but it is not automatically equivalent to the continuous problem.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/layouts.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/cutting-paths/layouts.svg' | relative_url }}" alt="Selected non-cutting travel for the four layouts" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Selected non-cutting travel for the four layouts. These are different input geometries, so their absolute bar heights are not a performance ranking between tasks. All values retain the problem coordinate units.</figcaption></figure>

<h2 id="second">5. Layout II: split visits and certify a candidate family</h2>

The second layout permits more elaborate operation structures. The selected split-contour route has idle distance 130.5355649, compared with 150.62541385 for the evaluated single-loop alternative and 177.6145593 for the nearest-neighbor baseline. These correspond to reductions of about 13.3% and 26.5% against the two stated references.

The archived search enumerates 86,400 candidate structures and refines 594 of them. The next candidate's saved lower bound is 130.5363128, already above the selected objective. Under the implemented structural family and refinement conventions, that bound closes the remaining structural search.

This is a meaningful certificate, but its scope must be retained. It applies to the operations, structure enumeration, and continuous-solving assumptions actually encoded. It does not prove optimality after adding arbitrary contour splitting, new machine motions, or manufacturing constraints absent from the study.

<h2 id="third">6. Layout III: an improved route with an open gap</h2>

For the third layout, the selected feasible route has idle distance 203.2436, versus 239.8391 for the nearest-neighbor reference. The relaxed lower bound is 147.9435. The absolute gap is approximately 55.30, or about 27.3% of the feasible objective.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/comparison.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/cutting-paths/comparison.svg' | relative_url }}" alt="Reference comparisons for Layouts II and III" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Reference comparisons for Layouts II and III. The relaxed lower bound is not a feasible cutting route; it indicates how much room remains before optimality is established.</figcaption></figure>

The large gap limits what can be concluded. The selected route is better than the chosen baseline and passes the saved feasibility checks, but the lower bound is too loose to establish that no better route exists. Describing it as an improved feasible solution communicates the actual state of the evidence more accurately than labeling every selected route “optimal.”

A useful next calculation would either tighten the relaxation or systematically enlarge and certify the candidate search. Those are different improvements from merely rerunning a local optimizer with another initial point.

<h2 id="bridges">7. Layout IV: bridges change the boundary</h2>

In the connected-piece example, a bridge has finite width. Its union with the pieces changes the outline that the cutter must follow. Treating a bridge as a zero-width graph edge would miss that geometric change and could count lengths or connected components incorrectly.

Four symmetry-related three-bridge trees have the same selected idle distance, approximately 133.978394. A tested four-bridge cycle gives approximately 136.6798. The additional connection therefore does not improve the stated idle-travel objective in this comparison.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/cutting-paths/bridges.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/cutting-paths/bridges.svg' | relative_url }}" alt="Three-bridge tree alternatives versus a four-bridge cycle" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Three-bridge tree alternatives versus a four-bridge cycle. The vertical scale is restricted to show the small difference; printed values provide the complete distances.</figcaption></figure>

Bridge width is 2 in the supplied coordinate units. The calculation forms and verifies the finite-width geometric union before planning travel. The result is conditional on that construction rule and objective; fewer bridges need not always be better under an alternative strength, heat, or material-loss objective.

<h2 id="discussion">8. Verification, limitations, and next steps</h2>

The archived independent route walk reproduces the selected travel totals within zero to approximately $10^{-9}$ numerical discrepancy, and the saved feasibility-error lists are empty. These checks support consistency between a stored route and its reported objective. They do not, by themselves, prove that the route is globally shortest.

One perturbation series contains an inconsistent reference: its zero-perturbation reoptimized value differs from the stated baseline. That series is not used here as clean quantitative robustness evidence. Baseline alignment should be resolved before interpreting its apparent improvement as sensitivity to geometry.

The main contribution is the connection between discrete operation structure and continuous boundary geometry. The main limitation is that the objective is purely geometric non-cutting travel. A production study would add acceleration, pierce costs, thermal distortion, collision clearance, and independent machine trials. Those extensions may change both the best sequence and the best entry points.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
