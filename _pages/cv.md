---
layout: han-page
permalink: /cv/
title: CV
heading: Curriculum vitae
eyebrow: Academic background
nav: true
nav_order: 4
page_class: hy-cv-page
description: Han YANG · Animal Science, Applied Mathematics, and an emerging research interest in Chinese philosophy.
---

{% assign cv = site.data.cv.cv %}

<div class="hy-cv-top">
  <div>
    <h2>{{ cv.name }}</h2>
    <p>{{ cv.location }} · <a href="mailto:{{ cv.email }}">{{ cv.email }}</a> · <a href="https://github.com/WenTian1111">GitHub</a></p>
    <p>{{ cv.summary }}</p>
  </div>
  <button type="button" class="hy-button hy-button-secondary hy-print-button" onclick="window.print()">Print / save PDF</button>
</div>

<section class="hy-cv-downloads" aria-label="Downloadable curricula vitae">
  <a class="hy-cv-download" href="{{ '/assets/pdf/han-yang-academic-cv.pdf' | relative_url }}" target="_blank" rel="noopener" type="application/pdf" aria-label="Open Academic CV, English PDF, 2 pages, in a new tab">
    <span class="hy-label">English · Academic</span>
    <span class="hy-cv-download-title">Academic CV <span aria-hidden="true">↗</span></span>
    <span class="hy-cv-download-detail">Research, education & selected achievements</span>
    <span class="hy-cv-file">PDF · 2 pages</span>
  </a>
  <a class="hy-cv-download" href="{{ '/assets/pdf/han-yang-resume-zh.pdf' | relative_url }}" target="_blank" rel="noopener" type="application/pdf" aria-label="Open Chinese résumé, PDF, 2 pages, in a new tab">
    <span class="hy-label">中文 · Professional</span>
    <span class="hy-cv-download-title"><span lang="zh-CN">中文简历</span> <span aria-hidden="true">↗</span></span>
    <span class="hy-cv-download-detail" lang="zh-CN">教育背景、科研经历与专业实践</span>
    <span class="hy-cv-file">PDF · 2 pages</span>
  </a>
</section>

<nav class="hy-section-nav" aria-label="CV sections">
  <a href="#education">Education</a><a href="#projects">Research</a><a href="#publications">Publications</a><a href="#experience">Experience</a><a href="#awards">Awards</a><a href="#skills">Skills</a>
</nav>

{% assign section_order = 'Education|Projects|Publications|Experience|Awards|Skills|Languages|Interests' | split: '|' %}
{% for section_name in section_order %}

  <section class="hy-cv-section" id="{{ section_name | downcase }}">
    <h2>{% case section_name %}{% when 'Projects' %}Research experience{% when 'Publications' %}Publications &amp; intellectual property{% when 'Experience' %}Professional experience{% when 'Awards' %}Selected honors{% when 'Skills' %}Methods &amp; tools{% when 'Interests' %}Research interests{% else %}{{ section_name }}{% endcase %}</h2>
    <div class="hy-cv-entries">
      {% assign entries = cv.sections[section_name] %}
      {% if section_name == 'Awards' %}{% assign entries = entries | sort: 'date' | reverse %}{% endif %}
      {% for entry in entries %}
        <article class="hy-cv-entry">
          <div class="hy-cv-entry-heading">
            <h3>{{ entry.title | default: entry.position | default: entry.institution | default: entry.name }}</h3>
            {% if entry.status %}
              <span class="hy-status">{{ entry.status }}</span>
            {% elsif entry.start_date %}
              <span>{% if section_name == 'Projects' %}{{ entry.start_date | date: '%b %Y' }} – {{ entry.end_date | date: '%b %Y' }}{% else %}{{ entry.start_date }} – {{ entry.end_date }}{% endif %}</span>
            {% elsif entry.date %}
              <span>{{ entry.date | date: '%Y' }}</span>
            {% elsif entry.releaseDate %}
              <span>{{ entry.releaseDate | slice: 0, 4 }}</span>
            {% endif %}
          </div>
          {% if entry.studyType %}<p class="hy-cv-subtitle">{{ entry.area }} · {{ entry.studyType }}</p>{% endif %}
          {% if entry.company %}<p class="hy-cv-subtitle">{{ entry.company }} · {{ entry.location }}</p>{% endif %}
          {% if entry.publisher %}<p class="hy-cv-subtitle">{{ entry.authors | join: ', ' }} · {{ entry.publisher }}</p>{% endif %}
          {% if entry.awarder %}<p class="hy-cv-subtitle">{{ entry.awarder }}</p>{% endif %}
          {% if entry.score %}<p>{{ entry.location }} · {{ entry.score }}</p>{% endif %}
          {% if entry.summary and entry.summary != '' %}<p>{{ entry.summary }}</p>{% endif %}
          {% if entry.keywords %}<p>{{ entry.keywords }}</p>{% endif %}
          {% if entry.highlights.size > 0 %}<ul>{% for highlight in entry.highlights %}<li>{{ highlight }}</li>{% endfor %}</ul>{% endif %}
        </article>
      {% endfor %}
      {% if section_name == 'Projects' %}<a class="hy-all-work" href="{{ '/projects/' | relative_url }}">Read illustrated project accounts <span aria-hidden="true">→</span></a>{% endif %}
      {% if section_name == 'Awards' %}<a class="hy-all-work" href="{{ '/certificates/' | relative_url }}">Explore honors, awards & further learning <span aria-hidden="true">→</span></a>{% endif %}
    </div>
  </section>
{% endfor %}
