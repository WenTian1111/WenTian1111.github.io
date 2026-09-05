---
layout: han-project
title: "Bench-Dragon Procession Dynamics"
description: "A kinematic model linking spiral geometry, collision detection, turning paths, and speed constraints."
permalink: /projects/modeling/bench-dragon/
discipline: "Computational geometry"
period: "2024"
question: "How does a linked procession move through a spiral without colliding?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Arc-length integration, iterative kinematics, collision checking"
outcome: "CUMCM · 2024 · competition manuscript"
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

A bench-dragon procession is a long chain of connected rigid segments. Even when the head follows a prescribed curve, the rest of the chain must satisfy linkage geometry and avoid self-intersection. This study models a 223-segment procession from entry into an Archimedean spiral through turning and outward motion.

The five competition tasks form a connected sequence: calculate positions and velocities, locate the first collision, examine a tighter spiral, construct a turning path, and search for a compatible head speed. Each task adds a new constraint to the previous geometric calculation.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>A feasible path for the head is not enough. The full linked chain determines whether that path is collision-free and whether every handle remains within the speed limit.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable procession geometry diagram"><img src="{{ '/assets/img/research/dragon-geometry.svg' | relative_url }}" alt="Ideal spiral geometry from the stated 0.55 m pitch, paired with the modeling sequence. The curve is not a snapshot of the simulated 223-segment chain." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> Ideal spiral geometry from the stated 0.55 m pitch, paired with the modeling sequence. The curve is not a snapshot of the simulated 223-segment chain.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### Geometry, scale, and the moving head

The chain comprises one head board, 221 body boards, and one tail board, joined through 224 handles. The head board is 3.41 m long and the other boards are 2.20 m long. With the stated handle offsets, the corresponding handle separations are 2.86 m and 1.65 m. Distinguishing a board's full outline from the distance between its handles matters because motion is propagated through the handles, while collision concerns the board geometry.

The original winding case uses an Archimedean spiral, <em>r = bθ</em>, with <em>b = 0.55 / (2π)</em> metres per radian. The head begins at an angle of 32π and moves at 1 m/s. I used numerical arc-length integration and an iterative time–angle calculation to locate it. Constant speed along the curve is not constant angular speed: equal time steps must correspond to equal traveled distance.

### Propagating the chain and checking feasibility

The geometric model then propagates handle positions along the chain and estimates their velocities. The first task reports the motion over 0–300 seconds at one-second intervals. This converts a prescribed head trajectory into a linked-body calculation rather than drawing the same curve independently for every segment.

The collision stage uses point–rectangle geometry to check the moving head against other boards. The manuscript refines the time step from one second to 0.01 seconds near the detected contact. The pitch study reuses the motion and collision calculations to examine whether the procession can reach a turning region nine metres in diameter.

### Turning geometry and the speed constraint

The later scenario uses a 1.7 m spiral pitch and a turning connection formed by two circular arcs with a 2:1 radius ratio. The task is to connect inward and outward motion while respecting the given geometric conditions. A final speed search evaluates the largest handle speed for candidate head speeds. This recognizes that the speed constraint applies to the entire procession, not just its leading handle.

<h2 id="findings">Selected results</h2>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable research result figure"><img src="{{ '/assets/img/research/dragon-initialization.svg' | relative_url }}" alt="Initial positions and radial distance for 224 handles, recalculated from the submitted initialization equations. The source's approximate angular update is preserved; this is an initial geometry calculation, not a newly validated full-motion simulation." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 2.</span> Initial positions and radial distance for 224 handles, recalculated from the submitted initialization equations. The source's approximate angular update is preserved; this is an initial geometry calculation, not a newly validated full-motion simulation.</figcaption>
</figure>

### What the two figures show

Figure 1 explains the prescribed spiral and the modeling sequence. Figure 2 reconstructs the initial 224-handle geometry from the submitted initialization script and pairs it with radial distance along the chain. The larger separation near the head and the outward progression of subsequent handles follow the source's initialization rules.

That script updates angle approximately using handle separation divided by current radius. The reconstruction preserves this approximation; it is not an exact fixed-chord solver or a newly validated simulation of all five tasks. The distinction keeps an illustrative recalculation separate from the manuscript's reported motion results.

### Reported feasibility boundaries

For the original winding scenario, the submitted calculation detects first collision at approximately 412.47 seconds. The pitch search reports a feasible boundary near 45.03 cm for the stated turning region. Under the later turning scenario, the manuscript reports a 13.84 m connecting arc length. These values belong to different tasks and should not be combined as one simultaneously tested configuration.

The final speed search reports a head speed of 1.243984 m/s and a corresponding maximum handle speed of 1.999983 m/s, just below the 2 m/s limit. The last refinement was manual. These digits reproduce the submitted calculation; they do not establish that the physical system is safe to that precision or that a global maximum has been proved.

<h2 id="discussion">Discussion</h2>

The useful outcome is the coupling of geometry, motion, collision, and speed feasibility. It also exposes where numerical confidence is needed. A finer time step improves temporal resolution, but does not by itself establish that every relevant collision has been checked. Likewise, a successful parameter search does not prove a globally minimal pitch or turning path.

A stronger continuation would audit fixed handle distances, compare the submitted collision test with complete segment/polygon intersection tests, and report explicit step-size convergence. The speed boundary would benefit from a documented tolerance and reproducible search bracket. Physical flexibility, human coordination, and manufacturing variation remain outside this rigid-link model.

<p class="hy-source-note">Research record: Submitted CUMCM manuscript, Spiral Bench-Dragon Procession Simulation Design, 2024. Original study: <em>Simulation design for a spiral bench-dragon procession</em>. Independently developed by Han Yang.</p>
