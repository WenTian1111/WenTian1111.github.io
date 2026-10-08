---
layout: han-project
title: Geometric Simulation & Evidence Discipline
description: A non-operational research reflection on assumptions, reproducibility, numerical verification, and the limits of simulation evidence.
permalink: /projects/modeling/constrained-simulation/
discipline: Numerical research · Verification practice
period: 2025 study
question: How should a computational study distinguish an internally consistent calculation from a validated real-world claim?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Model documentation, baseline comparison, numerical crosschecks, sensitivity interpretation
outcome: A non-operational account of modeling and verification
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: a computational artifact needs an evidence contract"
    id: background
  - label: 2. A general verification workflow
    id: roadmap
  - label: 3. Make assumptions inspectable
    id: assumptions
  - label: 4. Compare against a declared reference
    id: baselines
  - label: 5. Use checks that do not repeat the same calculation
    id: checks
  - label: 6. Separate fixed-design sensitivity from reoptimization
    id: sensitivity
  - label: 7. Preserve versions and report what was actually checked
    id: reproducibility
  - label: "8. Discussion: a useful result has a bounded claim"
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Simulation can turn a complicated scene into a calculable model, but the existence of a numerical answer does not establish that the model captures reality. This research note examines that distinction through an archived 2025 geometric-simulation project. It focuses on the evidence practices shared by computational studies: declaring assumptions, documenting a baseline, separating solver output from independent checks, examining sensitivity, and qualifying the scope of a conclusion.

The presentation is deliberately non-operational. It does not reproduce deployment parameters, tactical optimization methods, or strategy diagrams from the underlying scenario. Instead, it provides a general account of how a research artifact can be organized and assessed without treating a polished visualization or a solver's success message as validation.

<h2 id="background">1. Background: a computational artifact needs an evidence contract</h2>

A simulation begins by choosing what the model represents. Some aspects of the setting become state variables or constraints; others become fixed inputs, approximations, or omissions. Those choices determine the question the calculation can answer.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/constrained-simulation/cover.webp' | relative_url }}" alt="Unquantified fictional scenario illustration from the supplied project" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Unquantified fictional scenario illustration from the supplied project. It provides thematic context only; no operational settings, performance evidence, or deployment plan is encoded in this page.</figcaption></figure>

The first useful document is therefore an evidence contract: what is given, what is assumed, what is computed, and what would count as an independent check. A saved numerical result may be reproducible under those assumptions while remaining untested outside them.

That distinction is relevant well beyond this source scenario. A material model, route planner, service-network model, or inverse sensor calculation can all produce an exact-looking number. The research question is whether the number is supported by the model's inputs and by checks appropriate to the claim being made.

<h2 id="roadmap">2. A general verification workflow</h2>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/workflow.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/constrained-simulation/workflow.svg' | relative_url }}" alt="General research-verification workflow prepared for this public note" width="1000" height="580" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> General research-verification workflow prepared for this public note. It concerns documentation and evidence assessment, without representing the source scenario’s operational decision procedure.</figcaption></figure>

<h2 id="assumptions">3. Make assumptions inspectable</h2>

Assumptions should be stated before results, because they define the boundary of interpretation. Fixed environmental conditions, simplified geometry, ideal measurements, and omitted dynamics each remove a source of complexity. That may be appropriate for a first model, but it is not evidence that the omitted effects are negligible in practice.

A useful assumption record also explains why each simplification is made. Some assumptions isolate a mechanism for analytical clarity; others compensate for missing data. These have different implications. An assumption made because no measurement is available should remain a visible uncertainty rather than disappearing into a fitted constant.

The public note follows that practice by retaining the distinction between a fictional setting and an observed system. It does not assign the archived scenario the status of a real deployment or an independently tested experiment.

<h2 id="baselines">4. Compare against a declared reference</h2>

An improvement has meaning only relative to a specified reference. The same input conventions, objective definition, and evaluation procedure should be used on both sides of a comparison. If any of those change, the difference no longer isolates the purported improvement.

There are at least three common references in computational work: a simple feasible construction, an established algorithm, and a theoretical bound. They answer different questions. Beating a simple construction may show practical improvement; approaching a bound may support an optimality argument. Neither should be silently substituted for the other.

The most informative comparison records both the objective and feasibility. A shorter route that violates a constraint is not an improved feasible route. Conversely, a feasible result can be scientifically useful even when the available bound is too weak to establish global optimality.

<h2 id="checks">5. Use checks that do not repeat the same calculation</h2>

A verification script is strongest when it evaluates an artifact from another direction. It might recompute a stored length directly from coordinates, inspect a constraint independently, compare two numerical schemes, or test a small case with an analytical answer.

Re-executing the same implementation with the same assumptions can establish repeatability, but it is a weaker check against a shared modeling or coding error. A passing file or formatting check establishes that an artifact is present and readable; it does not prove the scientific conclusion.

Numerical agreement should also be reported with a meaningful scale. A tiny absolute discrepancy can be impressive in arithmetic while irrelevant to an uncertain input. Conversely, a modest residual may be acceptable if it is far below the measurement noise. The criterion must connect to the physical or mathematical claim, rather than simply displaying more decimal places.

<h2 id="sensitivity">6. Separate fixed-design sensitivity from reoptimization</h2>

Sensitivity analysis can ask two distinct questions. First, how does a saved result behave when an input changes but the design remains fixed? Second, what result can be recovered if the model is allowed to redesign after that change? The latter can conceal the fragility of the original decision.

Both questions are useful when labeled correctly. A fixed-design experiment estimates margin; a reoptimized experiment estimates adaptability under an ideal decision process. Neither guarantees robustness to unspecified disturbances.

Uncertainty in an assumption also differs from random variability in a measured input. A Monte Carlo experiment samples a chosen distribution; its output is conditional on that distribution and on the model. It should not be described as an empirical probability unless the data and calibration support that interpretation.

<h2 id="reproducibility">7. Preserve versions and report what was actually checked</h2>

A reproducible project should retain input provenance, code versions, parameter conventions, result tables, and figure sources. These make it possible to trace a statement back to the calculation that produced it. A PDF alone often cannot reveal which of several revised outputs supplied a particular figure.

The website collection follows a modest but explicit reporting rule: quantitative plots are tied to saved numerical records, conceptual illustrations are labeled, and a website review is distinguished from rerunning every source experiment. This prevents a fresh presentation from implying a fresh scientific acceptance test.

Version differences are themselves evidence to inspect. A revised result should replace an older value only when its source is identified and its accounting conventions understood. Conflicting records should be resolved or acknowledged rather than averaged into a convenient narrative.

<h2 id="discussion">8. Discussion: a useful result has a bounded claim</h2>

The final task of a computational study is to state what the result supports. Internal numerical consistency, performance within a tested candidate family, robustness under selected perturbations, and independent real-world validation are different achievements.

A transparent research note can be valuable without claiming the last of those. It can explain a model, expose a failure of identifiability, demonstrate a useful comparison, or show where further data are needed. Those contributions depend on clear evidence boundaries rather than a comprehensive-looking diagram.

This page therefore presents the archived project through general verification and research-communication practices. It carries no operational optimization details or full-source download. Its purpose within the collection is to make the evidence discipline behind numerical research visible.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
