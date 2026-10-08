---
layout: han-project
title: Bench-Dragon Procession Dynamics
description: A linked-body geometry study that progresses from spiral motion to collision-aware pitch, turning construction, and speed amplification.
permalink: /projects/modeling/bench-dragon/
discipline: Computational geometry · Linked-body motion
period: 2024 study
question: How does a prescribed spiral motion propagate through a long chain with finite-width segments?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Arc-length parameterization, chord constraints, collision detection, tangent-arc geometry
outcome: 223 segments · collision-aware pitch · whole-chain speed limits
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: a path is not a chain"
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: "3. Stage A: solve positions and velocities"
    id: motion
  - label: "4. Stage B: detect collision between physical segments"
    id: collision
  - label: "5. Stage C: constrain the entire entry interval"
    id: pitch
  - label: "6. Stage D: construct and interpret the turn"
    id: turning
  - label: "7. Stage E: propagate the speed limit through the chain"
    id: speed
  - label: 8. Verification and discussion
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

A long linked procession cannot be represented by the motion of its leading point alone. This study models 223 finite-width bench segments connected by 224 handles and follows five related questions: where the chain is at a given time, when collision first occurs, which spiral pitch permits safe entry, how a turn can connect entry and exit, and how the speed of a downstream handle can exceed the leader's speed.

For the supplied geometry, the archived calculation finds a first collision at 412.474 s for the initial 0.55 m pitch. A whole-entry search identifies a critical pitch of approximately 0.450337 m, whereas a boundary-only check would admit an unsafe smaller pitch. The maximum handle-speed amplification in the evaluated turning trajectory is about 1.60479, giving a leading-speed bound of 1.24627 m/s when every handle is limited to 2 m/s. These are deterministic model results under rigid geometry, not measurements of an actual performance.

<h2 id="background">1. Background: a path is not a chain</h2>

The leading handle follows a spiral, but each later handle must satisfy its distance to the previous handle. A point-path diagram therefore omits two important effects: the geometric lag along the chain and the width of each physical segment. Together they determine whether the procession fits through a densely packed region.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/bench-dragon/cover.webp' | relative_url }}" alt="Conceptual spiral procession" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual spiral procession. This illustration introduces the linked-body geometry; its visible segment count and positions are not a numerical reconstruction.</figcaption></figure>

The modeled chain has 223 segments and 224 handles. The first handle spacing is 2.86 m; the remaining spacings are 1.65 m. Segment width is 0.30 m. These distances are kept distinct from any decorative or overall board dimensions. The entry pitch is initially 0.55 m, and the prescribed leading-point speed is 1 m/s.

The study begins with kinematics because collision and speed constraints depend on the complete configuration. It then adds finite-width collision checks, searches pitch over the whole entry interval, constructs a turn within the stated region, and finally evaluates speed amplification through that turn.

<h2 id="roadmap">2. Study roadmap</h2>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/bench-dragon/workflow.webp' | relative_url }}" alt="Five-stage motion-model overview" width="1491" height="1055" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Five-stage motion-model overview. The spiral uses r = bθ with b = p/(2π), so pitch p is the radial increase per complete revolution. The illustrations introduce the stages; the quantitative plots below show archived numerical records.</figcaption></figure>

<h2 id="motion">3. Stage A: solve positions and velocities</h2>

For an Archimedean spiral, pitch $p$ is the increase in radius per revolution, not the coefficient multiplying angle. This distinction is essential when dimensions are checked.

<div class="hy-equation">
\[
r(\theta)=b\theta,\qquad b=\frac{p}{2\pi},\qquad \frac{ds}{d\theta}=b\sqrt{1+\theta^2}.
\tag{1}
\]
</div>

The leading handle is positioned by integrating arc length and inverting the traveled distance. With its position fixed, later handles are solved successively on the appropriate branch of the spiral using the chord-length constraint:

<div class="hy-equation">
\[
\left\|\mathbf x_i(\theta_i)-\mathbf x_{i-1}(\theta_{i-1})\right\|=\ell_i.
\tag{2}
\]
</div>

Choosing the branch matters: a distance equation can have multiple roots, but only one corresponds to the next handle along the chain. Implicit differentiation of these constraints gives downstream angular rates and velocities. Assigning the same speed to every point would violate the rigid-distance relation.

The archived position calculation checks chord residuals to approximately $10^{-9}$ m. At 300 s the leading radius is about 4.992315 m. The remaining arc length from the stated initial angle to the spiral center is not the same as the elapsed travel at 300 s; the head has not reached the center at that snapshot. This establishes a consistent motion baseline before collision detection is introduced.

<h2 id="collision">4. Stage B: detect collision between physical segments</h2>

Each segment is represented as a finite-width rectangle constructed from its two handles and the specified overhang convention. A separating-axis test checks nonadjacent segment pairs. Adjacent pieces that share a joint are treated consistently with the articulated connection rather than counted as an arbitrary self-intersection.

The first-contact search advances the configuration and refines the time interval around a sign change in minimum clearance. For the initial pitch, the first reported contact occurs at 412.473837682 s between segments 1 and 9. The leading radius is approximately 2.288743 m. During the first 300 s, the minimum saved clearance is still about 0.120694 m.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/collision.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/bench-dragon/collision.svg' | relative_url }}" alt="Archived clearance histories and the minimum clearance over the full entry path as pitch varies" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Archived clearance histories and the minimum clearance over the full entry path as pitch varies. A zero crossing marks the boundary between feasible and colliding configurations.</figcaption></figure>

The collision time is meaningful only under the rigid rectangle geometry and the tested contact convention. Board deformation, joint play, human movement, and vertical separation are absent. The useful result is a reproducible geometric limit, not a prediction of when an actual procession would physically strike another segment.

<h2 id="pitch">5. Stage C: constrain the entire entry interval</h2>

A safe configuration at the turn boundary does not guarantee safe arrival there. Collision can occur earlier and disappear before the endpoint. The pitch decision therefore uses the worst clearance along the complete entry interval:

<div class="hy-equation">
\[
G(p)=\min_{t\in[0,T_{\mathrm{entry}}(p)]}\ \min_{(i,j)\in\mathcal P}g_{ij}(t;p),\qquad G(p)\ge0.
\tag{3}
\]
</div>

Here $g_{ij}$ is signed separation for a tested nonadjacent pair and $\mathcal P$ is the checked pair set. The boundary is the 4.5 m turning radius. Searching only that endpoint suggests a pitch of approximately 0.420216 m, but the chain collides before it arrives, at a leading radius around 4.593 m. The whole-entry search instead gives approximately 0.450337393 m.

The difference illustrates a general optimization lesson: feasibility is a property of the trajectory, not merely of its final state. Numerical refinement of a threshold is valuable only after the correct interval and physical geometry have been specified.

Width perturbations reinforce that point. At the nominal critical pitch, reducing width by 5% leaves about 0.0174 m clearance, while increasing it by 5% produces approximately −0.0118 m clearance. Reoptimizing pitch gives approximately 0.4353 and 0.4644 m for those two widths. A design located exactly at a modeled threshold has little margin for uncertain geometry.

<h2 id="turning">6. Stage D: construct and interpret the turn</h2>

Within a 9 m diameter turning region, the study connects entry and exit with two tangent circular arcs whose radii have a 2:1 ratio. The archived radii are approximately 3.005418 and 1.502709 m. Their common sweep angle is approximately 3.021487 radians, giving a total arc length of 13.621245 m.

<div class="hy-equation">
\[
L_{\mathrm{turn}}=(R_1+R_2)\alpha.
\tag{4}
\]
</div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/turning.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/bench-dragon/turning.svg' | relative_url }}" alt="Supporting-circle geometry for the turn" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Supporting-circle geometry for the turn. The complete circles are drawn to explain centers and tangency; only the connecting arcs contribute to the reported turning length.</figcaption></figure>

A tested family of radius redistributions with fixed boundary endpoints and tangency leaves the combined length effectively unchanged: 441 evaluated candidates have a spread near $10^{-14}$ m. This is evidence of an invariant within that construction family. It does not prove that the two-arc route is shortest among every possible curve or every alternative endpoint choice.

Keeping those claims separate improves the interpretation of the geometry. The calculation demonstrates a feasible tangent construction and an internal invariance, rather than a universal shortest-path theorem.

<h2 id="speed">7. Stage E: propagate the speed limit through the chain</h2>

A constant leading speed does not imply constant downstream speed. Curvature and linkage geometry can amplify motion at particular handles. The archived evaluation computes each handle's speed ratio relative to the head and searches the complete evaluated turn.

<div class="hy-equation">
\[
A_{\max}=\max_{i,t}\frac{v_i(t)}{v_{\mathrm{head}}},\qquad v_{\mathrm{head}}^{\max}=\frac{v_{\mathrm{handle}}^{\max}}{A_{\max}}.
\tag{5}
\]
</div>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/bench-dragon/speed.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/bench-dragon/speed.svg' | relative_url }}" alt="Speed amplification through the evaluated turn, alongside the effect of width perturbation on minimum clearance at a fixed pitch" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Speed amplification through the evaluated turn, alongside the effect of width perturbation on minimum clearance at a fixed pitch.</figcaption></figure>

The largest saved amplification is 1.604793379. With a 2 m/s limit for every handle, the derived head limit is 1.246266358 m/s. This is a whole-chain bound in the stated kinematic model. It excludes acceleration limits, fatigue, response delays, and the practical coordination of performers.

<h2 id="discussion">8. Verification and discussion</h2>

The calculation is strongest when it connects independent checks: chord residuals for motion, rectangle geometry for collision, full-path feasibility for pitch, tangency for turning, and propagated velocity limits for speed. A visually plausible spiral alone supports none of those claims.

The archived sensitivity results vary width and turning-space size and distinguish a fixed design from a reoptimized design. That distinction matters because reoptimization can conceal how fragile the original plan is. The website presents selected records rather than claiming a new exhaustive numerical audit.

The study shows how a simple local rule can produce a complex collective limit. Its next practical step would be to add articulated-joint uncertainty, dynamic acceleration, and observations of a real chain. The current results describe rigid planar geometry with prescribed motion and should be read within that scope.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
