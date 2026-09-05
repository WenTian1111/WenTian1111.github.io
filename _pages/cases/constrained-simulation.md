---
layout: han-project
title: "Constrained Geometric Simulation"
description: "A method-level account of geometric abstraction, constrained objectives, population-based search, and sensitivity review."
permalink: /projects/modeling/constrained-simulation/
discipline: "Numerical optimization"
period: "2025"
question: "How can a simulation be organized around explicit geometry and feasibility?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Geometric abstraction, constrained numerical search, sensitivity analysis"
outcome: "CUMCM · 2025 · competition manuscript"
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: Study structure
    id: method
  - label: Research reflection
    id: findings
  - label: Discussion
    id: discussion
---

<h2 id="abstract">Abstract</h2>

This competition project studies how to translate a scenario into a numerical model with explicit geometric assumptions and feasibility checks. It connects simulation and optimization, treating the interpretation of an objective as part of the modeling task rather than a detail to add after the search.

The original scenario concerns a defensive military application. This public research note therefore focuses on general mathematical concepts and the interpretation of computational evidence. It is a methodological account, not a reproduction of the application model or its optimized settings.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>A numerical search result is conditional on its model. The transferable lesson is to distinguish a computed score, satisfaction of stated constraints, and evidence that a model represents reality.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable general modeling diagram"><img src="{{ '/assets/img/research/visibility-methods.svg' | relative_url }}" alt="A non-operational overview of the numerical modeling process. No deployment parameters or optimized trajectories are shown." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> A non-operational overview of the numerical modeling process. No deployment parameters or optimized trajectories are shown.</figcaption>
</figure>

<h2 id="method">Study structure</h2>

### Representation and assumptions

The manuscript develops a geometric abstraction of its scenario and formulates a constrained numerical objective. At the general mathematical level, this requires distinguishing fixed assumptions, quantities represented by the model, and the quantity being evaluated. The public summary retains those conceptual distinctions without reproducing application-specific formulas or decision variables.

### Simulation and numerical search

The submitted work uses population-based optimization, identified in the manuscript as particle-swarm optimization. Simulation and optimization play different conceptual roles: simulation evaluates a modeled situation, while optimization compares candidate outcomes within a stated formulation. The method name alone does not establish accuracy, convergence, or a globally optimal result.

Figure 1 summarizes this organization at a non-operational level. It is a conceptual diagram, not an empirical convergence curve, a reproduced simulation output, or a newly run experiment. No numerical settings or implementation details from the application are included.

<h2 id="findings">Research reflection</h2>

### What a computed result means

The transferable contribution is the organization of the calculation: make assumptions visible, state what is evaluated, recognize the role of constraints, and interpret the result within that scope. A high objective value and satisfaction of modeled constraints answer different questions. Neither, on its own, establishes how the result would translate to the physical world.

This distinction also separates verification from validation. Verification concerns whether a calculation follows its mathematical specification; validation concerns whether the model is supported by evidence about the phenomenon it represents. This page does not claim field validation, a certified optimum, or a new numerical performance result.

### Documenting a modeling study

The project provides a record of independently connecting abstraction, mathematical formulation, computation, and written analysis in a competition setting. In this portfolio, the emphasis is on explaining that chain of reasoning and its evidential limits. The account is intentionally narrower than the original manuscript: it presents general modeling literacy without turning the source material into an operational guide.

<h2 id="discussion">Discussion</h2>

The interpretation of any simulation is conditional on its assumptions, numerical approximations, and available evidence. Sensitivity and repeatability are relevant concepts, but this page does not introduce new application-specific tests, improved strategies, or performance claims. The figure should be read as an explanation of the study's structure only.

Operational trajectories, deployment settings, timing schedules, and implementation code are not reproduced. The public account remains limited to high-level mathematical methods and research reflection, with no claim of field validation.

<p class="hy-source-note">Research record: Submitted CUMCM competition manuscript, 2025, summarized at the level of general mathematical methods. Original study: <em>Multi-objective simulation design using particle-swarm optimization</em>. Independently developed by Han Yang.</p>
