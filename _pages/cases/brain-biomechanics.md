---
layout: han-project
title: "A Two-Stage Brain Mechanics Model"
description: "Two connected competition studies progressing from idealized whole-domain deformation to solid and fluid lesion scenarios."
permalink: /projects/modeling/brain-biomechanics/
discipline: "Computational biomechanics"
period: "2024"
question: "How do material and boundary assumptions change a deformation model?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Nonlinear mechanics, finite elements, Ogden constitutive modeling"
outcome: "Certification Cup · 2024 · competition manuscript"
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

This two-stage project explores how an idealized mechanical model can represent deformation in a cranial-opening scenario. The first stage considers a domain without a space-occupying lesion. The second changes the constitutive formulation and examines solid and fluid lesion assumptions. The work is a numerical modeling exercise rather than a clinical study.

The shared mathematical question is how geometry, material response, and boundary conditions combine to determine displacement. Moving from the first manuscript to the second extends that question to different inclusion assumptions, while retaining the need to distinguish a model output from a measured anatomical response.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>The two manuscripts form a staged investigation of modeling assumptions. Their displacement examples illustrate the proposed framework; they are not evidence of clinical prediction accuracy.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable two-stage mechanics diagram"><img src="{{ '/assets/img/research/brain-methods.svg' | relative_url }}" alt="The two-stage modeling framework. This is a conceptual comparison of assumptions and outputs, not an anatomical or clinical result." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> The two-stage modeling framework. This is a conceptual comparison of assumptions and outputs, not an anatomical or clinical result.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### Stage one: defining a deformation problem

The first manuscript brings together a simplified three-dimensional domain, a nonlinear constitutive relationship, equations of motion, and initial and boundary conditions. The domain is approximated geometrically rather than reconstructed from a verified patient-specific dataset. Material values are drawn from the literature and used as assumptions for the numerical examples.

The study separates cases in which pressure is supplied from cases in which it must be estimated. That creates two sources of uncertainty: uncertainty in the loading itself and uncertainty in the mechanical response to that loading. A more elaborate solver would not, on its own, resolve an uncertain input pressure.

### Stage two: changing the constitutive and inclusion assumptions

The second manuscript introduces an Ogden constitutive formulation and considers solid and fluid space-occupying inclusions. Within the proposed model, the constitutive relationship describes material response, the equations of motion connect forces to deformation, and the boundary conditions describe how the surrounding domain is constrained or loaded. Each part has a distinct role; naming a material model is not a substitute for specifying the complete problem.

Finite-element reasoning provides the proposed route from a continuous spatial problem to a numerical calculation. MATLAB-based illustrative calculations accompany that formulation. This portfolio does not treat literature illustrations of detailed head meshes as an independently constructed, patient-specific mesh, or claim a fully validated finite-element implementation from those illustrations.

### Inputs, computation, and observable quantities

The calculation depends on the initial geometry, material assumptions, loading, and boundary conditions. Its outputs concern displacement within the modeled domain and the associated inclusion scenarios. Figure 1 makes the progression between the two manuscripts explicit without suggesting that an idealized ellipsoid is a detailed anatomical model.

The source's simplified geometry and loading make it possible to discuss how the formulation behaves. They also restrict interpretation: a numerical displacement is only meaningful in relation to the assumptions used to obtain it. Surrounding-tissue displacement, inclusion motion, and error in predicting either quantity are not interchangeable measurements.

<h2 id="findings">Selected results</h2>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable research result figure"><img src="{{ '/assets/img/research/brain-displacement.svg' | relative_url }}" alt="Reported surrounding-tissue displacement in two second-stage model scenarios. These are single numerical examples under the manuscript's idealized assumptions, without reported uncertainty—not clinical measurements or lesion-tracking accuracy." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 2.</span> Reported surrounding-tissue displacement in two second-stage model scenarios. These are single numerical examples under the manuscript's idealized assumptions, without reported uncertainty—not clinical measurements or lesion-tracking accuracy.</figcaption>
</figure>

### Two illustrative displacement values

The second-stage manuscript reports surrounding-tissue displacement of 2.4 cm in its solid-inclusion example and 1.57 cm in its fluid-inclusion example. Figure 2 redraws those two reported values on a shared axis. It is a summary of the manuscript's numerical examples, not a new simulation or a patient measurement.

The shorter bar identifies a smaller reported displacement in that particular example. It does not establish lower clinical risk, superior prediction, or a general material effect. The source provides no uncertainty intervals for these two values, so the figure does not add error bars or imply repeated measurements. Nor does a displacement magnitude measure how accurately the inclusion's location has been predicted.

### The contribution across the two stages

The value of the series is the explicit extension from a whole-domain deformation question to inclusion-specific assumptions. The second manuscript makes the choice of constitutive formulation more prominent, while the comparison shows how strongly a result depends on the modeled problem. This is a record of model formulation and illustrative computation, rather than an established clinical tool.

<h2 id="discussion">Discussion</h2>

The supplied materials do not establish patient-specific calibration or clinical validation. Important uncertainties include the idealized geometry, simplified pressure distribution, selected material values, and numerical treatment of the boundaries. A detailed-looking anatomical illustration would not remove those uncertainties, which is why the portfolio uses a methods diagram and an explicitly labeled result summary.

A stronger research continuation would first document a reproducible numerical implementation, then check units, boundary-condition consistency, and mesh convergence. Comparing predictions with independently measured deformation would be a separate validation step. These checks are proposed future work, not completed studies. No patient images or clinical records are included, and the project is not presented as guidance for medical decisions.

<p class="hy-source-note">Research record: Certification Cup first- and second-stage competition manuscripts, 2024. Original study: <em>Finite-element head models using nonlinear elasticity and the Ogden constitutive model</em>. Independently developed by Han Yang.</p>
