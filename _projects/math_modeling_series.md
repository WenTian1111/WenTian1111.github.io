---
layout: han-project
title: Applied Mathematical Modeling
description: A collection of computational studies across data science, energy systems, geometry, uncertainty, and computational mechanics.
img: assets/img/research/dragon-geometry.svg
importance: 3
category: research
discipline: Applied mathematics
period: 2023–2025
question: How can real-world constraints become a useful mathematical model?
role: Modeling, computation, analysis, and research communication
methods: Statistical learning, numerical simulation, optimization, computational geometry
outcome: Seven research notes
card_summary: A collection of seven computational studies, each presented through its research question, modeling approach, selected figures, and discussion.
image_alt: Spiral geometry and a linked-body modeling workflow
---

<div class="hy-collection-intro">
  <p>These studies connect physical and practical questions with explicit mathematical models. Each research note presents its assumptions, computational methods, selected results, and the limits of the evidence.</p>
  <p>Each research note follows the problem through model design, selected results, and discussion. Read them individually for the details, or across the collection to see how prediction, optimization, geometry, and uncertainty call for different forms of evidence.</p>
</div>

<div class="hy-paper-grid">
{% for study in site.data.modeling_cases %}
  <article class="hy-paper-card">
    <a class="hy-paper-image" href="{{ study.url | relative_url }}" aria-label="Read {{ study.title | escape }}">
      <img src="{{ study.figure | relative_url }}" alt="{{ study.title | escape }} — selected research figure" loading="lazy" width="1000" height="580">
    </a>
    <div class="hy-paper-copy">
      <p class="hy-label">{{ study.number }} <span> / {{ study.event }} · {{ study.year }}</span></p>
      <h2><a href="{{ study.url | relative_url }}">{{ study.title }}</a></h2>
      <p>{{ study.summary }}</p>
      <a class="hy-all-work" href="{{ study.url | relative_url }}">Read research note <span aria-hidden="true">→</span></a>
    </div>
  </article>
{% endfor %}
</div>

<p class="hy-source-note">Computational studies, 2023–2025. The figures distinguish reported numerical results from conceptual method diagrams. These studies are not presented as peer-reviewed publications or field-validated systems.</p>
