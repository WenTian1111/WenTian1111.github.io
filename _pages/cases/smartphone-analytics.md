---
layout: han-project
title: "Smartphone Usage & Recommendation"
description: "An independent study connecting behavioral segmentation, usage prediction, and collaborative recommendation."
permalink: /projects/modeling/smartphone-analytics/
discipline: "Data science"
period: "2023"
question: "What can app-usage records reveal about behavior—and what can they predict?"
role: Independent researcher — modeling, implementation, analysis, and writing
methods: "Clustering, logistic regression, random forests, collaborative filtering"
outcome: "Dingding Cup · 2023 · competition manuscript"
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

A usage record describes an event; a useful behavioral model needs to connect those events across people, app categories, and time. This study developed a sequence of data-cleaning, exploratory-analysis, clustering, and prediction tasks around 20 common app categories. A final-round extension introduced collaborative filtering to connect user similarity with app recommendations.

The project moves between three levels of analysis: describing patterns in historical activity, predicting a specified target, and using similarity to propose relevant apps. Keeping those levels separate is important: an interpretable user grouping is not automatically a predictive model, and an accurate classifier is not automatically a useful recommender.

<aside class="hy-study-insight" aria-label="Study takeaway">
  <p class="hy-label">In brief</p>
  <p>The most revealing result is a contrast: an overall accuracy near 98% sits alongside minority-class recall rounded to zero. The evaluation must follow the question, not just the largest headline number.</p>
</aside>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable smartphone modeling diagram"><img src="{{ '/assets/img/research/smartphone-methods.svg' | relative_url }}" alt="Methods overview spanning the initial submission and final-round extension. This is a schematic, not an empirical cluster plot." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> Methods overview spanning the initial submission and final-round extension. This is a schematic, not an empirical cluster plot.</figcaption>
</figure>

<h2 id="method">Model design</h2>

### From event logs to behavioral profiles

The supplied records combine app identity, time information, usage duration, and upload/download traffic. The initial analysis organizes the activity around common app categories and compares crow-search-based clustering, density-peak clustering, and DBSCAN. Traffic volumes and hourly activity profiles provide a basis for interpreting the resulting groups. These are descriptive groupings of observed behavior, not independently verified user types.

### Two predictive targets

The final-round classification workflow groups records by user and separates training and evaluation by the recorded end day. It encodes the selected app class as one and the remaining records as zero, then fits logistic regression using duration and upload/download traffic. This is a record-classification task using observed activity features; it should not be described as forecasting a person's future app use before that activity occurs.

The duration-regression workflow maps app identities to categories, applies one-hot encoding, and screens discrete features with chi-square tests and continuous features with Spearman correlation. The manuscript then describes principal-component reduction retaining 95% of variance and a 1% sample of 185,824 training records. Its parameter search selects a random forest with 200 trees, maximum depth five, minimum leaf size two, and minimum split size ten. These settings document the submitted experiment rather than a generally optimal configuration.

### Extending profiles into recommendations

The recommendation component considers user-to-user and app-to-app similarity. Its purpose is to connect historical preferences with candidate app categories. This is a distinct task from the two supervised models: it would need an evaluation based on held-out interactions and recommendation relevance, not the classifier's accuracy. The supplied manuscript presents the recommendation design but does not establish an online deployment or measured engagement uplift.

<h2 id="findings">Selected results</h2>

<figure class="hy-research-figure">
  <div class="hy-figure-canvas" tabindex="0" role="region" aria-label="Scrollable research result figure"><img src="{{ '/assets/img/research/smartphone-evaluation.svg' | relative_url }}" alt="Evaluation-set composition and class-specific recall, redrawn from the final-round classification report. Recall is rounded as reported; the near-98% overall accuracy does not demonstrate useful minority-class recall." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 2.</span> Evaluation-set composition and class-specific recall, redrawn from the final-round classification report. Recall is rounded as reported; the near-98% overall accuracy does not demonstrate useful minority-class recall.</figcaption>
</figure>

### Reading the classification result

Figure 2 places the class distribution beside class-specific recall. The report contains 27,058,692 majority-class records and 536,486 selected-class records: approximately 98.06% and 1.94% of the evaluation set. Those are record counts, not counts of distinct people. The selected class has reported precision 0.02 and recall 0.00, while majority-class recall is 1.00; the report rounds these metrics to two decimal places.

A classifier that always selected the majority class would already obtain approximately 98.06% accuracy on this composition. This baseline is calculated from the reported class counts, not from an additional training run. It explains why the rounded 98% accuracy cannot establish useful identification of the selected app class. The figure therefore emphasizes the asymmetry in performance rather than presenting the overall score as a success metric.

### Keeping metrics tied to their task

The duration model reports normalized mean squared error, NMSE = 0.95113. It is a regression measure, not an accuracy percentage. Without an accompanying reference prediction and a fully specified normalization convention, this number alone does not establish practical improvement. The clustering comparisons and recommendation design similarly remain separate contributions; this page does not assign them unsupported performance scores.

<h2 id="discussion">Discussion</h2>

The project connects data preparation, descriptive analysis, supervised learning, and recommendation within one study. Its clearest methodological lesson is to define the unit of analysis and the intended prediction before choosing a metric. A large number of records does not resolve class imbalance or guarantee that information available during evaluation would also be available at prediction time.

A follow-up would audit chronological separation and user overlap, fit preprocessing only within the training split, and compare class-specific precision and recall against simple baselines. Recommendation quality would be tested on held-out interactions. These are proposed checks, not completed experiments. Only aggregate methods and findings are presented here; individual usage logs and identifiers remain private.

<p class="hy-source-note">Research record: Initial competition paper and final-round manuscript, 2023; classification report in the final-round manuscript. Original study: <em>Smartphone data monitoring and analysis using clustering and regression models</em>. Independently developed by Han Yang.</p>
