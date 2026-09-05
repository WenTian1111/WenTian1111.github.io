---
layout: han-page
permalink: /publications/
title: Publications
heading: Publications & intellectual property
eyebrow: Research outputs
description: Published work and a design patent application.
nav: true
nav_order: 3
page_class: hy-publications-page
---

{% include bib_search.liquid %}

<section class="hy-output-section" aria-labelledby="papers-title">
  <h2 id="papers-title">Research publications</h2>
  <div class="publications">
    {% bibliography --query @article %}
  </div>
  <a class="hy-all-work" href="{{ '/projects/rocket_debris_localization/' | relative_url }}">Explore the localization study <span aria-hidden="true">→</span></a>
</section>

<section class="hy-output-section" aria-labelledby="ip-title">
  <h2 id="ip-title">Design patent application</h2>
  <p class="hy-output-note">Application information is listed separately from research publications.</p>
  <div class="publications">
    {% bibliography --query @patent %}
  </div>
</section>
