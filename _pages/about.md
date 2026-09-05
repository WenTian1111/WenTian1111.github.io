---
layout: about
title: About
permalink: /
subtitle:

profile: false
selected_papers: false
social: false

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<div class="hy-home" id="top">
  <section class="hy-hero" aria-labelledby="home-title">
    <div class="hy-hero-copy">
      <p class="hy-kicker">Philosophy · Mathematical modeling · Data-driven inquiry</p>
      <h1 id="home-title">Han YANG</h1>
      <p class="hy-role">Admitted to the M.A. in Religious Studies at The Chinese University of Hong Kong · enrollment forthcoming</p>
      <h2>Studying how conceptual frameworks and quantitative models help us understand complex systems.</h2>
      <p class="hy-intro">
        My work brings together Chinese philosophy, mathematical modeling, and empirical research. I am interested in how ideas
        shape the questions we ask—and how models, experiments, and evidence can refine those ideas.
      </p>
      <div class="hy-actions" aria-label="Primary actions">
        <a class="hy-button hy-button-primary" href="#work">View selected work</a>
        <a class="hy-button hy-button-secondary" href="{{ '/cv/' | relative_url }}">View CV</a>
        <a class="hy-text-link" href="mailto:2549675208a@gmail.com">Email me <span aria-hidden="true">↗</span></a>
      </div>
    </div>

    <aside class="hy-profile-card" aria-label="Profile and research direction">
      <div class="hy-cosmos-band" aria-hidden="true"></div>
      <img
        class="hy-portrait"
        src="{{ '/assets/img/han-yang-avatar.jpg' | relative_url }}"
        alt="Han Yang's chosen avatar"
        width="132"
        height="132"
      >
      <div class="hy-profile-copy">
        <p class="hy-label">Current direction</p>
        <p>Chinese thought, models of natural order, and rigorous ways of connecting concepts with evidence.</p>
        <div class="hy-profile-links">
          <a href="https://github.com/WenTian1111">GitHub</a>
          <a href="mailto:2549675208a@gmail.com">Email</a>
        </div>
      </div>
    </aside>

  </section>

  <div class="hy-fact-strip" aria-label="Academic snapshot">
    <div><strong>2026</strong><span>B.Sc. Animal Science</span></div>
    <div><strong>Applied Mathematics</strong><span>Undergraduate minor</span></div>
    <div><strong>{{ site.projects | size }}</strong><span>Project collections</span></div>
    <div><strong>1</strong><span>Research publication</span></div>
  </div>

  <section class="hy-section" id="research" aria-labelledby="research-title">
    <header class="hy-section-header">
      <div>
        <p class="hy-label">Research interests</p>
        <h2 id="research-title">Three connected lines of inquiry</h2>
      </div>
      <p>My long-term interests connect philosophical questions about order and change with the practical discipline of building and testing models.</p>
    </header>

    <div class="hy-research-grid">
      <article class="hy-research-card">
        <span class="hy-index">01</span>
        <h3>Chinese philosophy &amp; cosmology</h3>
        <p>How the <em>Yijing</em>, Daoist thought, and classical ideas of order frame change, relation, and natural processes.</p>
      </article>
      <article class="hy-research-card">
        <span class="hy-index">02</span>
        <h3>Modeling complex systems</h3>
        <p>Using geometry, simulation, optimization, and uncertainty analysis to make difficult systems tractable.</p>
      </article>
      <article class="hy-research-card">
        <span class="hy-index">03</span>
        <h3>Evidence through computation</h3>
        <p>Combining machine vision, statistical learning, and experimental design to connect models with observed behavior.</p>
      </article>
    </div>

  </section>

  <section class="hy-section" id="work" aria-labelledby="work-title">
    <header class="hy-section-header">
      <div>
        <p class="hy-label">Selected work</p>
        <h2 id="work-title">Research in practice</h2>
      </div>
      <p>Three projects showing how I move from a concrete question to a model, a test, and a usable result.</p>
    </header>

    {% assign featured_projects = site.projects | sort: 'importance' %}
    <div class="hy-project-grid">
      {% for project in featured_projects limit: 3 %}
        <a class="hy-project-card" href="{{ project.url | relative_url }}">
          <div class="hy-project-media">
            {% if project.img %}
              <img src="{{ project.img | relative_url }}" alt="{{ project.image_alt | escape }}" loading="lazy" width="640" height="400">
            {% endif %}
          </div>
          <div class="hy-project-copy">
            <p class="hy-project-type">{{ project.discipline | default: 'Selected research' }}</p>
            <h3>{{ project.title }}</h3>
            <p>{{ project.card_summary | default: project.description }}</p>
            <span>View project <span aria-hidden="true">↗</span></span>
          </div>
        </a>
      {% endfor %}
    </div>
    <a class="hy-all-work" href="{{ '/projects/' | relative_url }}">Explore all projects <span aria-hidden="true">→</span></a>

  </section>

  <section class="hy-section hy-background" aria-labelledby="background-title">
    <div class="hy-background-lead">
      <p class="hy-label">Background</p>
      <h2 id="background-title">A deliberately interdisciplinary path</h2>
      <p>
        Training across the life sciences and applied mathematics led me from observation to measurement, and from measurement
        to deeper questions about how knowledge is organized.
      </p>
    </div>

    <div class="hy-timeline">
      <article>
        <span>Admitted</span>
        <div>
          <h3>M.A. in Religious Studies</h3>
          <p>The Chinese University of Hong Kong · enrollment forthcoming</p>
        </div>
      </article>
      <article>
        <span>2022–26</span>
        <div>
          <h3>B.Sc. in Animal Science</h3>
          <p>Southwest University · minor in Applied Mathematics</p>
        </div>
      </article>
      <article>
        <span>2024</span>
        <div>
          <h3>First research publication</h3>
          <p>Multi-object localization of rocket debris using sonic-boom arrival times</p>
        </div>
      </article>
    </div>

  </section>

  <section class="hy-contact" aria-labelledby="contact-title">
    <div>
      <p class="hy-label">Contact</p>
      <h2 id="contact-title">Interested in the same questions?</h2>
      <p>I welcome conversations about graduate research, interdisciplinary methods, and possible collaboration.</p>
    </div>
    <a class="hy-button hy-button-light" href="mailto:2549675208a@gmail.com">Start a conversation</a>
  </section>
</div>
