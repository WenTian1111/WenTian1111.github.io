---
layout: han-project
title: Bench-Dragon Procession Dynamics
description: "A linked-body study of spiral kinematics, finite-width contact, trajectory-wide pitch feasibility, tangent turns, and downstream velocity amplification."
permalink: /projects/modeling/bench-dragon/
discipline: Computational geometry · Linked-body motion
period: 2024 study
question: How do local rigid-distance constraints determine the motion and geometric limits of a long articulated procession?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Arc-length inversion, implicit kinematics, separating-axis contact tests, trajectory search, tangent-arc construction
outcome: 224 handles · finite-width geometry · full-entry feasibility · propagated speed limits
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Geometry and study design
    id: geometry
  - label: 3. Spiral kinematics
    id: kinematics
  - label: 4. Finite-width contact
    id: collision
  - label: 5. Full-entry feasibility
    id: pitch
  - label: 6. Tangent turning construction
    id: turning
  - label: 7. Speed amplification
    id: speed
  - label: 8. Sensitivity and tolerance
    id: sensitivity
  - label: 9. Numerical verification
    id: verification
  - label: 10. Discussion
    id: discussion
  - label: 11. Conclusions
    id: conclusions
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

A long articulated procession has two different geometries: the curve followed by its handles and the finite-width boards connecting them. Prescribing the leading handle's path therefore does not determine safety or motion limits by itself. This study reconstructs a chain of **223 rigid segments and 224 handles**, propagates velocity through chord constraints, detects contact between nonadjacent rectangles, and searches for a spiral pitch that remains feasible throughout inward entry. A separate turning experiment constructs two tangent arcs and examines the speed amplification experienced by followers.

For a 0.55 m spiral pitch and a 1 m/s leading speed, the archived first-contact calculation gives **412.473838 s**, with contact between the first and ninth benches. A trajectory-wide search gives a critical entry pitch near **0.450337 m**, whereas an endpoint-only check suggests approximately 0.420216 m and misses earlier interference. In the turning experiment, which uses a different **1.7 m pitch**, two arcs with radii 3.005418 and 1.502709 m connect the boundary endpoints over 13.621245 m. Within the fixed-endpoint tangent family, redistributing the two radii does not shorten the combined route. The saved speed search reaches an amplification of **1.604793**, corresponding to a leading-speed limit of **1.246266 m/s** for a 2 m/s handle constraint over the evaluated trajectory.

The results illustrate how local constraints produce collective limits. Fresh checks reproduce the reference-day kinematics, contact sign change, tangent construction, and peak configuration without modifying the source outputs. Width perturbations show that a design at the critical pitch has little geometric tolerance. The findings describe deterministic planar geometry and prescribed motion, rather than measured performance or a certified operating plan.

<p class="hy-source-note"><strong>Keywords:</strong> articulated chains; Archimedean spiral; rigid-distance kinematics; separating-axis test; trajectory feasibility; tangent arcs; speed amplification.</p>

<h2 id="introduction">1. Introduction</h2>

The bench-dragon procession provides a concrete example of a linked-body problem: many long, narrow segments must follow a compact route while maintaining their connections. The leading point can move smoothly even when a downstream board approaches another board or a follower moves faster than the leader. The relevant object is consequently the complete configuration, including its physical extent and velocity field.

Three modeling distinctions organize the study. **Arc length and chord length serve different purposes:** the first measures progression along a path, while the second maintains a rigid connection. **Path geometry and occupied geometry differ:** handles can remain on a valid curve while board corners interfere. **Endpoint feasibility and trajectory feasibility differ:** a safe arrival configuration can conceal an earlier collision.

The analysis begins with prescribed spiral motion, establishes a contact event for finite-width segments, then searches the entire inward interval as pitch changes. It next constructs a tangent turn under explicitly fixed boundary conditions and evaluates follower speeds. Each stage uses the previous stage's geometry rather than introducing a separate visual approximation.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/bench-dragon/cover.webp' | relative_url }}" alt="Conceptual spiral procession of connected benches" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual application setting. The illustration introduces the procession; its segment count, spacing, and occupied area are not a numerical reconstruction.</figcaption></figure>

<h2 id="geometry">2. Geometry and study design</h2>

### 2.1 Handles, board lengths, and numbering

The leading handle is $P_0$, the shared connection behind the first board is $P_1$, and the final rear handle is $P_{223}$. Board $k$ connects $P_{k-1}$ to $P_k$ when boards are numbered from 1. This separates human-readable board numbering from zero-based handle indices used in calculation.

Each hole center lies 0.275 m from its nearest board end. The head board is 3.41 m long; body and tail boards are 2.20 m long. Their handle separations therefore differ from their physical lengths:

<div class="hy-equation">
\[
\begin{aligned}
\ell_1&=3.41-2(0.275)=2.86\ \mathrm{m},\\
\ell_k&=2.20-2(0.275)=1.65\ \mathrm{m},\quad k\ge2.
\end{aligned}
\tag{1}
\]
</div>

<div class="hy-model-table"><table><caption>Table 1. Geometric parameters and the distinct experimental stages.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Value</th><th scope="col">Role</th></tr></thead><tbody>
<tr><td>Rigid boards / handles</td><td>223 / 224</td><td>Complete linked configuration</td></tr>
<tr><td>Head / other board lengths</td><td>3.41 / 2.20 m</td><td>Occupied rectangle geometry</td></tr>
<tr><td>Head / other handle separations</td><td>2.86 / 1.65 m</td><td>Rigid chord constraints</td></tr>
<tr><td>Board width</td><td>0.30 m</td><td>Finite-width contact test</td></tr>
<tr><td>Initial spiral experiment</td><td>Pitch 0.55 m; angle $32\pi$; head speed 1 m/s</td><td>Position, velocity, and first contact</td></tr>
<tr><td>Entry feasibility experiment</td><td>Pitch varies; terminal head radius 4.5 m</td><td>Trajectory-wide inward clearance</td></tr>
<tr><td>Turning experiment</td><td>Pitch 1.7 m; region diameter 9 m</td><td>Two-arc route and propagated speeds</td></tr>
</tbody></table></div>

The total handle-to-handle chord length is 369.16 m. It is not the sum of board lengths, since board ends extend beyond the joints. The turning experiment changes the spiral pitch to 1.7 m; its numerical results must not be interpreted as a continuation of the minimum-pitch entry configuration.

### 2.2 Modeling scope

All motion is planar and prescribed. Boards are rigid, hole spacing is fixed, and handles follow the specified path. Adjacent boards sharing a joint are exempted from collision tests under the articulated-connection convention. No performer dynamics, board flexure, joint slack, vertical offsets between nonadjacent boards, or response delays are modeled.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/bench-dragon/workflow.webp' | relative_url }}" alt="Five-stage modeling framework for spiral motion, collision, entry pitch, turning, and speed" width="1491" height="1055" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Conceptual modeling roadmap. Spiral pitch is the radial increase over one revolution, with $b=p/(2\pi)$ in $r=b\theta$. The quantitative configurations below are generated from the computational model.</figcaption></figure>

<h2 id="kinematics">3. Spiral kinematics: reconstruct positions and velocities</h2>

### 3.1 Arc-length progression of the leading handle

For pitch $p$ and angular parameter $\theta$, the spiral position is

<div class="hy-equation">
\[
\begin{aligned}
\mathbf x(\theta)&=b\theta(\cos\theta,\sin\theta),\\
b&=\frac{p}{2\pi}.
\end{aligned}
\tag{2}
\]
</div>

Inward motion follows decreasing $\theta$. The arc length from the center and its derivative are

<div class="hy-equation">
\[
\begin{aligned}
s(\theta)&=\frac b2\,\theta\sqrt{1+\theta^2}\\
&\quad+\frac b2\operatorname{asinh}\theta,\\
\frac{ds}{d\theta}&=b\sqrt{1+\theta^2},\\
s(\theta_0)-s(\theta_h(t))&=v_0t.
\end{aligned}
\tag{3}
\]
</div>

The monotone arc-length equation is inverted numerically for the leader. At the initial angle $32\pi$, the 0.55 m-pitch spiral gives a radius of 8.8 m and 442.590256 m of arc length to the center. Traveling 300 m therefore leaves the head on the spiral at radius 4.992315 m; it has not reached the center.

### 3.2 Successive chord constraints and physical branch selection

Each follower lies farther outward on the same spiral and maintains its fixed Euclidean distance to the preceding handle:

<div class="hy-equation">
\[
\begin{aligned}
Q_i&=\|\mathbf x(\theta_i)-\mathbf x(\theta_{i-1})\|^2-\ell_i^2=0,\\
\theta_{i-1}&<\theta_i\le\theta_{i-1}+\pi.
\end{aligned}
\tag{4}
\]
</div>

The stated branch is important. A broad angular search can identify another point on a later spiral turn with the same Euclidean separation. The implementation brackets the next root within the increasing-distance half-turn interval and reconstructs handles in sequence. It does not approximate a rigid board by a fixed arc-length gap.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/spiral-configurations.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/bench-dragon/spiral-configurations.svg' | relative_url }}" alt="Numerically reconstructed finite-width chain at 0, 100, 200, and 300 seconds" width="976" height="898" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Four complete configurations in the initial inward-motion experiment. Rectangles include the board overhangs beyond the handles. The head moves inward while much of the chain remains on outer turns.</figcaption></figure>

### 3.3 Velocity from implicit differentiation

Differentiating $Q_i=0$ propagates angular velocity, and the local arc-length derivative converts it into speed:

<div class="hy-equation">
\[
\begin{aligned}
\dot\theta_i&=-\frac{\partial Q_i/\partial\theta_{i-1}}{\partial Q_i/\partial\theta_i}\dot\theta_{i-1},\\
\dot\theta_h&=-\frac{v_0}{b\sqrt{1+\theta_h^2}},\\
v_i&=b\sqrt{1+\theta_i^2}|\dot\theta_i|.
\end{aligned}
\tag{5}
\]
</div>

This velocity field is derived from the same constraints as the positions. Assigning every handle the leader's 1 m/s speed would generally violate the rigid-distance condition. In the initial spiral window, selected outer handles move slightly more slowly, with a smooth accumulated reduction along the chain.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/spiral-speeds.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/bench-dragon/spiral-speeds.svg' | relative_url }}" alt="Selected handle speeds over time and the full handle-speed profile at 300 seconds" width="1186" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Velocity propagation in the inward spiral. The narrow vertical range exposes small differences that would be obscured by an axis beginning at zero. Handle indices are zero-based.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 2. Selected kinematic results from the archived six-time-point table.</caption><thead><tr><th scope="col">Time (s)</th><th scope="col">Head x / y (m)</th><th scope="col">Head speed (m/s)</th><th scope="col">Rear-tail x / y (m)</th><th scope="col">Rear-tail speed (m/s)</th></tr></thead><tbody>
<tr><td>0</td><td>8.800000 / 0.000000</td><td>1.000000</td><td>−5.305444 / −10.676584</td><td>0.999311</td></tr>
<tr><td>60</td><td>5.799209 / −5.771092</td><td>1.000000</td><td>7.364557 / −8.797992</td><td>0.999136</td></tr>
<tr><td>120</td><td>−4.084887 / −6.304479</td><td>1.000000</td><td>10.974348 / 0.843473</td><td>0.998883</td></tr>
<tr><td>180</td><td>−2.963609 / 6.094780</td><td>1.000000</td><td>7.383896 / 7.492370</td><td>0.998489</td></tr>
<tr><td>240</td><td>2.594494 / −5.356743</td><td>1.000000</td><td>3.241051 / 9.469336</td><td>0.997816</td></tr>
<tr><td>300</td><td>4.420274 / 2.320429</td><td>1.000000</td><td>1.785033 / 9.301164</td><td>0.996478</td></tr>
</tbody></table></div>

<h2 id="collision">4. Finite-width geometry and the first contact event</h2>

### 4.1 Construct occupied rectangles

For each board, the chord direction determines a unit longitudinal axis $\hat{\mathbf u}_k$ and perpendicular axis $\hat{\mathbf n}_k$. Its center is the midpoint of the handles, and its half-length includes the overhang:

<div class="hy-equation">
\[
\begin{aligned}
\mathbf c_k&=\frac{\mathbf P_{k-1}+\mathbf P_k}{2},\\
h_k&=\frac{\ell_k}{2}+0.275,\qquad w=0.15,\\
\mathbf z_k^{\pm,\pm}&=\mathbf c_k\pm h_k\hat{\mathbf u}_k\pm w\hat{\mathbf n}_k.
\end{aligned}
\tag{6}
\]
</div>

Here $w$ is half-width. Checking only chord intersections would omit collisions involving corners and overhangs. Adjacent boards are excluded at shared joints; all tested nonadjacent pairs are evaluated through their occupied rectangles.

### 4.2 Signed separating-axis margin

On a candidate separating axis $\mathbf a$, each rectangle has a projected half-extent $e_k(\mathbf a)$. The pair margin is the maximum projection separation, and the configuration margin is the minimum across tested pairs:

<div class="hy-equation">
\[
\begin{aligned}
g_{ij}&=\max_{\mathbf a}\left[| (\mathbf c_j-\mathbf c_i)\cdot\mathbf a|-e_i(\mathbf a)-e_j(\mathbf a)\right],\\
F(t)&=\min_{|i-j|\ge2}g_{ij}(t).
\end{aligned}
\tag{7}
\]
</div>

Positive $F$ indicates separation, zero indicates a contact threshold, and negative values indicate interference for a tested pair. This is a **signed SAT margin**, not an exact Euclidean minimum-distance measurement. The implementation prunes clearly distant pairs with bounding circles, scans time at 0.5 s increments after 300 s, and refines the detected crossing with a bracketed root solver.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/first-contact.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/bench-dragon/first-contact.svg' | relative_url }}" alt="Signed collision margin versus time and enlarged geometry of benches one and nine at contact" width="1186" height="495" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> The detected first contact. The oscillatory margin reflects changing configurations and active board pairs. The enlarged right panel highlights boards 1 and 9 rather than relying on a centerline-only sketch.</figcaption></figure>

The saved event occurs at **412.473837682 s**, with a head radius of 2.288743 m. At 300 s, the SAT margin is still +0.120694 m. For this revision, evaluating the configurations $10^{-7}$ s before and after the saved event gives margins of approximately +$2.635\times10^{-9}$ and −$2.629\times10^{-9}$ m and identifies the same first/ninth-board pair.

This confirms the local contact crossing. The time-scan resolution and physical contact convention remain part of the event definition; a highly precise root does not by itself constitute continuous collision certification over every unexamined time interval.

<h2 id="pitch">5. Full-entry feasibility and critical pitch</h2>

### 5.1 Formulate a trajectory constraint

The pitch experiment asks whether the head can move from the sixteenth-turn starting radius $16p$ to the 4.5 m boundary without nonadjacent-board interference. It is an inward-entry problem; it does not require the complete 369.16 m handle chain to fit inside the turning circle.

For a candidate pitch, the relevant margin is the worst value along the inward trajectory:

<div class="hy-equation">
\[
\begin{aligned}
G(p)&=\min_{r_h\in[4.5,16p]}F(r_h;p),\\
p^*&=\inf\{p:G(p)\ge0\}.
\end{aligned}
\tag{8}
\]
</div>

The archived numerical procedure scans radius, locally refines a candidate minimum, and solves for a zero of the resulting envelope. Its reported pitch is approximately **0.450337393 m**. The root tolerance controls the outer solve; the accuracy of the critical design also depends on the inner trajectory search and geometry assumptions.

### 5.2 Why checking only the boundary fails

An endpoint-only test suggests approximately 0.420216 m. Yet this pitch produces interference before arrival, near a head radius of 4.593 m. Clearance is not monotone as the chain descends: one board pair can approach, separate, and be replaced by another restrictive pair. The final configuration therefore cannot summarize the whole route.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/entry-feasibility.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
<img src="{{ '/assets/img/research/bench-dragon/entry-feasibility.svg' | relative_url }}" alt="Trajectory feasibility envelope against pitch and signed margin along inward entry at the selected pitch" width="1186" height="476" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 6.</span> Full-trajectory pitch selection. In the right panel, radius decreases from left to right. The near-contact region precedes the terminal 4.5 m boundary, where the margin has already recovered.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 3. Endpoint feasibility and trajectory feasibility answer different questions.</caption><thead><tr><th scope="col">Test</th><th scope="col">Reported pitch (m)</th><th scope="col">Evidence and interpretation</th></tr></thead><tbody>
<tr><td>Boundary-only check</td><td>≈0.420216</td><td>Accepts arrival geometry but misses earlier interference near radius 4.593 m.</td></tr>
<tr><td>Full-entry envelope</td><td>≈0.450337</td><td>Includes nonadjacent contact throughout the evaluated inward interval.</td></tr>
<tr><td>Sampled near-contact point at selected pitch</td><td>Same design</td><td>Radius 4.58 m; margin +0.000204 m on the saved 0.02 m radius grid.</td></tr>
<tr><td>Arrival at the boundary</td><td>Same design</td><td>Radius 4.5 m; margin +0.019957 m.</td></tr>
</tbody></table></div>

The positive near-contact grid value is not a contradiction of the zero-envelope search: a discrete plot sample need not land on the refined minimum. It should not be interpreted as a guaranteed 0.204 mm operating clearance. The outer threshold has many saved decimal places, but meaningful geometric tolerance is addressed by perturbation tests rather than numerical print precision.

<h2 id="turning">6. A tangent turning construction with fixed endpoints</h2>

### 6.1 Change the spiral pitch and define boundary conditions

The turning stage uses pitch **1.7 m** and a circular region of radius 4.5 m. Its entry endpoint $M_1$ is the inward spiral's intersection with the boundary, and the centrally symmetric outward spiral gives $M_2=-M_1$. Both endpoint travel directions are fixed by the spirals. A right-turning arc followed by a left-turning arc joins them with continuous tangent direction.

Let $\hat{\mathbf N}$ be the right normal to the shared endpoint travel direction. For radii $R_1,R_2$, the centers and tangency condition give

<div class="hy-equation">
\[
\begin{aligned}
C_1&=M_1+R_1\hat{\mathbf N},\\
C_2&=M_2-R_2\hat{\mathbf N},\\
\|C_1-C_2\|&=R_1+R_2,\\
S=R_1+R_2&=-\frac{\|M_1\|^2}{M_1\cdot\hat{\mathbf N}}.
\end{aligned}
\tag{9}
</div>

The 2:1 radius condition then determines the selected member. This construction fixes a route for handle centers. It does not establish that every finite-width board or the complete procession remains inside the circular region at all times.

<div class="hy-model-table"><table><caption>Table 4. Selected turning geometry for the 1.7 m-pitch experiment.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Value</th></tr></thead><tbody>
<tr><td>First / second radius</td><td>3.005418 / 1.502709 m</td></tr>
<tr><td>Radius sum $S$</td><td>4.508127 m</td></tr>
<tr><td>Common arc sweep angle</td><td>3.021487 rad</td></tr>
<tr><td>First / second arc length</td><td>9.080830 / 4.540415 m</td></tr>
<tr><td>Combined route length</td><td>13.621245 m</td></tr>
<tr><td>Entry endpoint x / y</td><td>−2.711856 / −3.591078 m</td></tr>
<tr><td>Exit endpoint x / y</td><td>2.711856 / 3.591078 m</td></tr>
</tbody></table></div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/turn-construction.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size">
<img src="{{ '/assets/img/research/bench-dragon/turn-construction.svg' | relative_url }}" alt="Two selected tangent arcs inside the turning circle and constant combined length across radius redistribution" width="1163" height="514" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 7.</span> Actual connecting arcs, with radius guides and the turning boundary. Complete supporting circles are deliberately omitted: containment of a connecting arc does not imply containment of its complete circle. The second panel shows length invariance in the evaluated fixed-endpoint family.</figcaption></figure>

### 6.2 What the length-invariance result establishes

For these symmetric endpoints and tangents, tangency fixes $S$. The two arc sweep angles remain equal and constant as $S$ is redistributed between positive radii. Consequently,

<div class="hy-equation">
\[
L=\alpha R_1+\alpha R_2=\alpha S.
\tag{10}
\]
</div>

The archive evaluates 441 family members with a length spread near $10^{-14}$ m. A fresh sampled family for this revision gives the same invariant to floating-point precision. This means radius redistribution cannot shorten the route **within that fixed-endpoint two-arc family**. It is not a shortest-path certificate over arbitrary curves, alternative endpoints, or different tangent requirements.

### 6.3 Reconstruct the chain on the composite route

The composite route joins inward spiral, first arc, second arc, and outward spiral. Its oriented arc-length coordinate $u$ is zero at entry and $L$ at exit. Following handles satisfy chord constraints with $u_i<u_{i-1}$. Position and tangent continuity are checked at all three transitions. Curvature changes at the joins, so tangent continuity does not imply smooth acceleration.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/turn-configurations.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size">
<img src="{{ '/assets/img/research/bench-dragon/turn-configurations.svg' | relative_url }}" alt="Full handle configurations before entry, at entry, and near the speed peak with the leading handle already outside the turning arcs" width="1186" height="484" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 8.</span> Composite-path configurations. The orange point is the leading handle; darker and brighter handle colors distinguish the calculated speed field. The circle locates the turning region, which contains the connecting arcs rather than the entire chain.</figcaption></figure>

<h2 id="speed">7. Speed amplification and the leading-speed bound</h2>

For a unit-speed path $\mathbf P(u)$ with tangent $\hat{\mathbf T}(u)$, differentiating the follower chord condition gives a local velocity ratio:

<div class="hy-equation">
\[
\dot u_i=\dot u_{i-1}
\frac{(\mathbf P_i-\mathbf P_{i-1})\cdot\hat{\mathbf T}_{i-1}}
{(\mathbf P_i-\mathbf P_{i-1})\cdot\hat{\mathbf T}_i}.
\tag{11}
\]
</div>

The numerator and denominator encode how the same chord projects onto the two local travel directions. A difference between those projections can amplify speed even though board length remains unchanged. Ratios accumulate through the linked chain; equal leader and follower speeds cannot be assumed during a turn.

Because the differentiated constraints are homogeneous in velocity, changing leading speed scales the field at the same configuration. For the evaluated trajectory set $\mathcal U$, the bound is

<div class="hy-equation">
\[
\begin{aligned}
A_{\max}&=\max_{i,u_h\in\mathcal U}\frac{v_i(u_h)}{v_0},\\
v_0^{\max}&=\frac{2}{A_{\max}}.
\end{aligned}
\tag{12}
\]
</div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/speed-amplification.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size">
<img src="{{ '/assets/img/research/bench-dragon/speed-amplification.svg' | relative_url }}" alt="Saved speed envelope for the first 34 handles and downstream speed plateau at the peak configuration" width="1186" height="476" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 9.</span> The archived search envelope covers the first 34 handles, sampled at 0.05 m leading-coordinate increments through 55 m. The right panel is recomputed at the saved peak using the full chain and shows the leading portion of its speed profile.</figcaption></figure>

The saved peak is **1.604793379** at $u_h=14.479969607$ m, giving **1.246266358 m/s** for the leading-speed bound. The leader has already completed the 13.621245 m arcs, while several followers are still within the turn. Handles associated with the third through seventh body benches share the peak to the reported precision. Equal-chord segments on the constant-curvature first arc propagate the same speed, producing a plateau rather than an isolated peak at one chosen handle.

The archive refines its strongest sampled peak and checks a later 55–85 m interval with a truncated handle search. This revision additionally reconstructs all 224 handles at selected configurations, including the peak and later coordinates 55, 85, and 120 m. Those checks reproduce the peak and give lower amplification at the later sampled states. They are useful checks of the truncation but are **not an exhaustive full-chain search over every later position**. The displayed bound should therefore be read with the evaluated trajectory and numerical search protocol, rather than as an unconditional operating guarantee.

<h2 id="sensitivity">8. Sensitivity, safety margin, and reoptimization</h2>

The archive varies width and turning-region size. These are geometric perturbations of a deterministic model, not confidence intervals or estimates of performer variability. The main width scan covers full widths of 26–38 cm; its stored parameter is half-width and must be doubled before labeling a plot.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/geometry-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size">
<img src="{{ '/assets/img/research/bench-dragon/geometry-sensitivity.svg' | relative_url }}" alt="Contact time and critical pitch versus board width, pitch versus turning-space diameter, and signed margin under fixed-design width perturbation" width="1186" height="754" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 10.</span> Archived sensitivity results. The turning-space trend includes small reversals associated with numerical resolution; it is not a strictly monotone curve at every stored point. The final panel keeps pitch fixed and exposes interference after a positive width perturbation.</figcaption></figure>

Wider boards cause earlier contact and generally require a larger inward-entry pitch. Across the stored width scan, contact time falls from 419.17 to 359.27 s, while selected pitch rises from 0.4115 to 0.5265 m. Increasing turning diameter from 7 to 11 m generally relaxes the entry pitch from about 0.4872 to 0.4248 m, with small numerical steps and a local reversal in the saved scan.

The most informative robustness test holds the original design fixed before reoptimizing it:

<div class="hy-model-table"><table><caption>Table 5. Fixed-pitch perturbation and reoptimized pitch are distinct evidence.</caption><thead><tr><th scope="col">Full width</th><th scope="col">SAT margin at fixed $p=0.450337$ m</th><th scope="col">Reoptimized pitch (m)</th><th scope="col">Interpretation</th></tr></thead><tbody>
<tr><td>28.5 cm (−5%)</td><td>+0.0174 m</td><td>0.4353</td><td>The original design remains separated in the tested model.</td></tr>
<tr><td>31.5 cm (+5%)</td><td>−0.0118 m</td><td>0.4644</td><td>The original design interferes; restoring feasibility requires more pitch.</td></tr>
</tbody></table></div>

Reoptimization alone would hide the fragility of the original threshold design. The positive width perturbation requires roughly another 0.014 m of pitch in the saved calculation. The archived joint width/radius corner tests provide additional checks, but their four cases do not define a probabilistic safety envelope. A practical design would choose explicit margins for measured board and joint variation rather than use the nominal threshold without allowance.

<h2 id="verification">9. Numerical verification and evidence provenance</h2>

The preserved project contains a manuscript, scripts, three populated result workbooks, intermediate JSON records, and a run manifest. Stored coordinates and velocities cover the initial spiral, the contact state, and the composite turning route. The web figures distinguish these model-derived quantities from the conceptual cover and roadmap.

<div class="hy-model-table"><table><caption>Table 6. Checks performed for this website revision, separate from archived verification claims.</caption><thead><tr><th scope="col">Check</th><th scope="col">Observed result</th><th scope="col">What it supports</th></tr></thead><tbody>
<tr><td>Reconstruct all 224 handles at 301 spiral times</td><td>Maximum chord residual $5.30\times10^{-13}$ m.</td><td>Rigid-distance consistency in the 0–300 s window.</td></tr>
<tr><td>Analytic velocity versus position differences at three times</td><td>Maximum difference $1.96\times10^{-8}$ m/s with a $10^{-4}$ s difference step.</td><td>Agreement between two calculation routes for the sampled states.</td></tr>
<tr><td>Before/after contact evaluations</td><td>Positive/negative margins around the saved event; same first/ninth-board pair.</td><td>Local crossing and contact-pair identification.</td></tr>
<tr><td>Three composite-path joins</td><td>Position differences ≈$2\times10^{-8}$ m across $2\times10^{-8}$ m coordinate intervals; tangent differences below $9\times10^{-9}$.</td><td>Position and tangent continuity in the selected construction.</td></tr>
<tr><td>Sample the connecting arcs</td><td>Maximum sampled radius 4.500000 m at the boundary endpoints.</td><td>Sampled handle-center route containment.</td></tr>
<tr><td>Recompute the peak configuration with all handles</td><td>Maximum amplification 1.604793379; speed-bound product ≈2 m/s.</td><td>Reproduction of the saved critical configuration.</td></tr>
</tbody></table></div>

Brent root refinement and very small constraint residuals establish numerical consistency; they do not validate rigid-board assumptions or guarantee that every possible trajectory minimum has been found. Likewise, agreement with a workbook created by the same model is a provenance check rather than independent physical validation.

This revision recomputes selected configurations and kinematic checks while retaining the archived critical-pitch and sensitivity searches. It does not rerun all optimization stages or modify the original manuscript and workbooks. The distinction keeps the claimed evidence aligned with what was actually checked.

<h2 id="discussion">10. Discussion and limitations</h2>

The complete configuration is the necessary link between every major result. Position recursion supplies the rectangles used for contact detection; the contact function supplies the trajectory-wide pitch condition; composite-path chord constraints supply the speed amplification. This chain of evidence is more informative than a visually plausible spiral or a single final clearance value.

The study also demonstrates why superficially similar optimization statements must be separated. An endpoint test can be solved precisely while imposing the wrong safety condition. A tangent family can exhibit exact length invariance without proving an unrestricted shortest path. A speed bound can be reproduced at its critical configuration without an exhaustive certification of every later handle position. Each numerical result should retain its domain, search protocol, and physical convention.

Several extensions would be needed for practical motion planning. Joint slack and manufacturing tolerances could be modeled as geometric uncertainty. Acceleration and jerk constraints would address curvature discontinuities at the spiral–arc and arc–arc joins. A full-turn finite-width collision audit would complement the inward-entry collision calculation, and a complete chronological speed scan would strengthen the search evidence. Actual motion measurements would be required to assess how performers depart from the prescribed rigid planar trajectory.

These are proposed extensions. The existing results are a computational study of geometry and kinematics, with no observed performance trials, dynamic force model, or certified operating margin.

<h2 id="conclusions">11. Conclusions</h2>

For the supplied geometry, the initial 0.55 m-pitch inward spiral reaches its detected contact threshold at approximately 412.474 s. Entry feasibility must be checked across the route: the approximately 0.450337 m trajectory-wide pitch is larger than the unsafe endpoint-only estimate. The separate 1.7 m-pitch turning construction yields a 13.621245 m tangent route whose length is invariant under the tested fixed-endpoint radius redistribution.

Follower speed can exceed leading speed during the turn. The saved amplification of approximately 1.604793 gives a 1.246266 m/s leading bound for the evaluated trajectory under a 2 m/s handle limit. Width perturbations show that nominal threshold designs are sensitive to small positive changes. The broader lesson is to carry **occupied geometry, full-trajectory constraints, and downstream motion** together through the analysis, then state the numerical and physical limits of the resulting design.

<p class="hy-source-note"><strong>Source and evidence basis.</strong> Current project manuscript, deterministic geometry scripts, intermediate results, result workbooks, and archived verification records. New quantitative figures and selected checks were generated for this research note without changing source materials. The cover and overview are conceptual AI-generated illustrations. This page presents a computational case study rather than a peer-reviewed publication, a measured performance study, or a certified motion plan. No manuscript download is attached at this stage.</p>
