---
layout: han-project
title: "Submersible Search under Uncertainty"
description: "A numerical exploration of drift, random-walk uncertainty, probability regions, and search-equipment trade-offs."
permalink: /projects/modeling/submersible-search/
discipline: "Stochastic modeling"
period: "2024"
question: "How can uncertain drift be translated into a useful search region?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Kinematic modeling, random walks, probability regions, weighted comparison"
outcome: "MCM / ICM · 2024 · competition manuscript"
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

When a submersible loses propulsion, a single predicted coordinate can hide substantial uncertainty. This study connects a simplified drift model to a spatial search description, then considers the trade-offs involved in choosing search equipment. The work was developed for the 2024 MCM/ICM submersible scenario.

The manuscript links four questions: how the vehicle might move, what equipment characteristics matter, how possible locations can be summarized, and how the interpretation changes under alternative assumptions. The emphasis is on connecting a motion model with an uncertainty-aware comparison, rather than treating an estimated endpoint as an observed location.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>There is no single equipment winner independent of the evaluation criteria. The reported ranking changes substantially when search range receives priority.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable uncertainty modeling diagram"><img src="{{ '/assets/img/research/submersible-methods.svg' | relative_url }}" alt="Conceptual route from uncertain motion to search-region and equipment analysis. No synthetic trajectories or probability heat maps are presented as study results." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> Conceptual route from uncertain motion to search-region and equipment analysis. No synthetic trajectories or probability heat maps are presented as study results.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### From deterministic motion to possible locations

The first stage establishes a three-dimensional coordinate system and a simplified motion model incorporating currents and buoyancy. Random-walk perturbations then produce candidate trajectories around this idealized description. The manuscript describes 1,000 realizations in the search analysis, representing possible outcomes under its assumptions rather than 1,000 observed vehicle tracks.

This separation matters: the mechanical assumptions determine the broad movement, while the random component describes the variability the model allows. More realizations can describe that assumed variability more densely, but cannot correct an inaccurate current field or an unrepresentative disturbance model by themselves.

### Summarizing a spatial distribution

The manuscript calls its geometric summaries a density sphere and a probability circle. These representations connect a collection of candidate locations to a more compact description of the search problem. Figure 1 shows the relationship between the motion calculation, uncertain locations, and the subsequent comparison without inventing a reconstructed trajectory ensemble or probability heat map.

A concentration of simulated endpoints is conditional on the model that generated them. It is not, without calibration, a measured probability that a real vehicle occupies that region. Likewise, predicting a location and detecting a vehicle there are different questions. The latter would require evidence about sensing performance and environmental conditions that is not established by the motion model alone.

### Comparing equipment under explicit priorities

The equipment analysis considers six categories: sonar, a submersible, an aerial drone, an underwater drone, a positioning tag, and a communication buoy. The manuscript normalizes assessment criteria and assigns weights to aspects such as range, precision, advantages, limitations, and cost. Its alternative settings ask how the ranking changes when the balance between those criteria changes.

The source also describes sensitivity exercises involving random iterations and support-vessel position. These explore dependence on the chosen setup; they are not independent observations validating the predicted search region.

<h2 id="findings">Selected results</h2>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable research result figure"><img src="{{ '/assets/img/research/submersible-ranking.svg' | relative_url }}" alt="Reported ranks under the two evaluation settings in manuscript Tables 4 and 5. These are outcomes of the author's weighted model, not independently measured equipment performance." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 2.</span> Reported ranks under the two evaluation settings in manuscript Tables 4 and 5. These are outcomes of the author's weighted model, not independently measured equipment performance.</figcaption>
</figure>

### A change in priorities changes the ordering

Figure 2 reproduces only the ranks in manuscript Tables 4 and 5. Under the combined evaluation, the order begins with the submersible, aerial drone, and communication buoy. Under range priority, the aerial drone moves to first and the underwater drone to second, while the submersible moves from first to sixth. The communication buoy remains third in both settings.

The connecting lines make this sensitivity visible. They show changes in ordinal position, not the size of a performance difference: the distance between ranks one and two does not represent the same physical quantity as a difference in detection range or cost. The rankings are outputs of the author's assessment model, not measured hardware benchmarks or procurement recommendations.

### What the available evidence supports

The study's central contribution is the connection between uncertain motion, a spatial representation, and criteria-dependent equipment comparison. It demonstrates why the choice of evaluation priorities should be visible alongside an optimization result. The original abstract contains inconsistent speed values, so this page does not reproduce a definitive drift speed or use it to construct a new quantitative search prediction.

<h2 id="discussion">Discussion</h2>

The manuscript recognizes systematic error from idealized mechanics and incomplete equipment costs, including omitted labor and failure-related costs. Its geometric summaries also compress a potentially irregular distribution into simple shapes. Those choices make a competition model tractable, but limit the precision of conclusions drawn from it.

A research continuation would separate numerical repeatability from empirical validity: checking stability across random seeds is different from checking a prediction against observed drift. Calibrated current data, uncertainty estimates, and an independently evaluated detection model would be needed for stronger conclusions. This remains a competition modeling study, not an operational search-and-rescue procedure.

<p class="hy-source-note">Research record: 2024 MCM/ICM competition manuscript, especially the motion, search-region, equipment-evaluation, and limitations sections. Original study: <em>Submersible search modeling based on a density-sphere and probability-circle approach</em>. Independently developed by Han Yang.</p>
