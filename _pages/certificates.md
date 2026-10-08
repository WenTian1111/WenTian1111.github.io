---
layout: han-page
permalink: /certificates/
title: Awards
heading: Honors & awards
eyebrow: Recognition · 2022–2025
page_class: hy-awards-page
nav: true
nav_order: 5
description: Selected academic honors, scholarships, and competition results—a record of curiosity translated into sustained work.
---

{% assign awards = site.data.awards %}

<section class="hy-award-highlights" aria-label="Selected distinctions">
  {% for award in awards.featured %}
    <article class="hy-award-highlight{% if forloop.first %} hy-award-highlight-lead{% endif %}">
      <div class="hy-award-overline"><span>{{ award.category }}</span><span>{{ award.year }}</span></div>
      <h2>{{ award.title }}</h2>
      <p class="hy-award-highlight-detail">{{ award.detail }}</p>
      {% if award.chinese %}<p class="hy-award-chinese" lang="zh-CN">{{ award.chinese }}</p>{% endif %}
      <p class="hy-award-issuer">{{ award.issuer }}</p>
      {% if award.url %}<a class="hy-award-link" href="{{ award.url | relative_url }}">{{ award.link }} <span aria-hidden="true">↗</span></a>{% endif %}
    </article>
  {% endfor %}
</section>

<nav class="hy-section-nav" aria-label="Awards sections">
  <a href="#honors">Honors & scholarships</a>
  <a href="#modeling">Modeling</a>
  <a href="#mathematics">Mathematics</a>
  <a href="#innovation">Innovation</a>
  <a href="#learning">Further learning</a>
</nav>

<section class="hy-awards-section" id="honors" aria-labelledby="honors-title">
  <header class="hy-awards-section-heading">
    <p class="hy-label">Academic recognition</p>
    <h2 id="honors-title">Honors & scholarships</h2>
    <p>University and industry-supported recognition for academic work, innovation, and engagement.</p>
  </header>
  <div class="hy-honors-grid">
    {% for award in awards.honors %}
      <article class="hy-honor-card">
        <span class="hy-award-year">{{ award.year }}</span>
        <h3>{{ award.title }}</h3>
        <p class="hy-award-chinese" lang="zh-CN">{{ award.chinese }}</p>
        <p class="hy-award-issuer">{{ award.issuer }}</p>
        <p class="hy-award-note">{{ award.detail }}</p>
      </article>
    {% endfor %}
  </div>
</section>

{% for group in awards.competitions %}

  <section class="hy-awards-section hy-awards-ledger" id="{{ group.id }}" aria-labelledby="{{ group.id }}-title">
    <header class="hy-awards-section-heading">
      <p class="hy-label">Competitions / {{ group.number }}</p>
      <h2 id="{{ group.id }}-title">{{ group.title }}</h2>
      <p>{{ group.description }}</p>
    </header>
    <ol class="hy-award-list">
      {% for award in group.entries %}
        <li class="hy-award-row">
          <span class="hy-award-year">{{ award.year }}</span>
          <div class="hy-award-body">
            <h3>{{ award.title }}{% if award.short %} <span class="hy-award-abbr">{{ award.short }}</span>{% endif %}</h3>
            <p class="hy-award-scope">{{ award.scope }}</p>
            {% if award.detail %}<p class="hy-award-note">{{ award.detail }}</p>{% endif %}
            {% if award.url %}<a class="hy-award-link" href="{{ award.url | relative_url }}">{{ award.link }} <span aria-hidden="true">↗</span></a>{% endif %}
          </div>
          <span class="hy-award-result">{{ award.result }}</span>
        </li>
      {% endfor %}
    </ol>
  </section>
{% endfor %}

<section class="hy-awards-section hy-awards-learning" id="learning" aria-labelledby="learning-title">
  <header class="hy-awards-section-heading">
    <p class="hy-label">Beyond competitions</p>
    <h2 id="learning-title">Further learning</h2>
    <p>Short courses and professional development, listed separately from competitive awards.</p>
  </header>
  <ul class="hy-learning-list">
    {% for item in awards.learning %}
      <li>
        <div><h3>{{ item.title }}{% if item.subtitle %} <span class="hy-award-abbr">{{ item.subtitle }}</span>{% endif %}</h3><p>{{ item.provider }}</p></div>
        <p class="hy-learning-type">{{ item.type }} <span>{{ item.year }}</span></p>
      </li>
    {% endfor %}
  </ul>
</section>

<aside class="hy-awards-footer">
  <div><h2>The work behind the recognition</h2><p>Models, findings, and reflections from seven independently completed mathematical modeling projects.</p></div>
  <a class="hy-button hy-button-secondary" href="{{ '/projects/math_modeling_series/' | relative_url }}">Explore the portfolio <span aria-hidden="true">→</span></a>
</aside>
