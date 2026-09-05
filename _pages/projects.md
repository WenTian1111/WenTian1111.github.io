---
layout: han-page
title: Projects
heading: Selected projects
eyebrow: Research portfolio
permalink: /projects/
description: Experimental studies and mathematical models, with the questions, methods, and contributions behind each project.
nav: true
nav_order: 2
page_class: hy-projects-page
---

{% assign sorted_projects = site.projects | sort: 'importance' %}

<div class="hy-project-list">
  {% for project in sorted_projects %}
    <article class="hy-project-row">
      <a class="hy-project-thumbnail" href="{{ project.url | relative_url }}" aria-label="Read {{ project.title | escape }}">
        <img src="{{ project.img | relative_url }}" alt="{{ project.image_alt | escape }}" loading="lazy" width="640" height="400">
      </a>
      <div class="hy-project-summary">
        <p class="hy-label">{{ project.discipline }} <span> / {{ project.period }}</span></p>
        <h2><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h2>
        <p class="hy-project-question">{{ project.question }}</p>
        <p>{{ project.card_summary }}</p>
        <dl><div><dt>Contribution</dt><dd>{{ project.role }}</dd></div><div><dt>Outcome</dt><dd>{{ project.outcome }}</dd></div></dl>
        <a class="hy-all-work" href="{{ project.url | relative_url }}">Read case study <span aria-hidden="true">→</span></a>
      </div>
    </article>
  {% endfor %}
</div>

<aside class="hy-page-note">
  <p>My current interests extend these quantitative foundations toward Chinese philosophy and digital humanities.</p>
  <a href="{{ '/#research' | relative_url }}">Read about my research direction <span aria-hidden="true">→</span></a>
</aside>
