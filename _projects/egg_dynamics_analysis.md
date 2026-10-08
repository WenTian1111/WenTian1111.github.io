---
layout: han-project
title: Egg Rolling Analysis & Risk Sorting
description: An undergraduate thesis and provincial innovation project connecting egg morphology, rolling experiments, interpretable risk grading, and an interactive prediction application.
img: assets/img/projects/egg/experiment_platform.png
importance: 1
category: research
discipline: Machine vision
period: 2025–2026
question: Can a still image of an egg help anticipate its rolling instability?
role: Thesis author and innovation-project lead
methods: Controlled experiments, machine vision, statistical analysis, machine learning
outcome: Undergraduate thesis, risk-grading framework, and companion web application
card_summary: A study of 90 eggs and 270 repeated rolling trials, linking visual morphology to instability and translating the analysis into an interactive application.
image_alt: Illustration of the paired static-imaging and inclined rolling experiment platforms
demo: https://egg-rsi-app.streamlit.app
source_code: https://github.com/WenTian1111/egg-rsi-app
contents:
  - label: Question & contribution
    id: question
  - label: Experiment
    id: experiment
  - label: Measurement
    id: measurement
  - label: Risk grading
    id: risk
  - label: Results
    id: results
  - label: Application
    id: application
  - label: Limits & next steps
    id: limitations
---

<h2 id="question">The research question</h2>

Egg sorting usually begins with properties that can be measured in a still image. Transport introduces a different problem: eggs roll, change orientation, and drift away from their intended paths. My research asks whether differences in **static shape** can help explain and anticipate that **dynamic instability**.

I developed this work through my undergraduate thesis, _Coupling Analysis of Static-Dynamic Characteristics and Sorting Research of Eggs Based on Machine Vision_, and a related Chongqing municipal-level innovation training project. They are connected stages of the same experimental research, not two independent datasets.

Under academic supervision, my responsibilities covered building the experimental platform, collecting and processing the image and video data, developing feature-extraction algorithms, comparing prediction models, and implementing the companion application. The innovation project ran from July 2025 to May 2026; the thesis was defended in May 2026.

<h2 id="experiment">A paired static–dynamic experiment</h2>

The study used **90 intact eggs from one batch**, with one standardized static image and **three rolling trials per egg**. The resulting 270 videos are repeated observations of 90 physical specimens—not 270 different eggs.

The platform combined a fixed camera and controlled illumination for shape measurement with a rolling surface inclined at **2.87°**. A blue flexible towel provided contrast for image segmentation and a consistent contact interface. The release position, viewing geometry, inclination, and surface were held constant to focus on differences between eggs.

<div class="row justify-content-center">
  <div class="col-md-8">
    {% include figure.liquid loading="lazy" path="assets/img/projects/egg/experiment_platform.png" title="Controlled static imaging and inclined rolling platform" class="img-fluid rounded" %}
  </div>
</div>
<p class="caption">The static imaging and rolling-acquisition setup. Results apply to this controlled experimental setting.</p>

The data pipeline linked each egg's static measurements to its repeated videos. Frame-level records were summarized into trial-level outcomes before statistical analysis, preserving the connection between a specimen's shape and its observed motion.

<h2 id="measurement">From images to measurable features</h2>

**Static morphology.** The processing pipeline separates the egg from the contrasting background, cleans the binary mask, extracts the contour, and measures its geometry. Basic descriptors include area, perimeter, axis lengths, egg shape index (ESI), and eccentricity. Asymmetry and Hu moments add information about uneven ends and higher-order contour structure. The companion application implements a 19-feature static descriptor.

**Dynamic behavior.** Video tracking produces centroid trajectories and orientation time series. These are summarized into three outcomes:

- **Lateral displacement:** the change in transverse centroid position between the beginning and end of a trial.
- **Orientation variance:** variation in the egg's fitted major-axis angle over the rolling sequence.
- **Speed coefficient of variation:** the standard deviation of speed divided by its mean.

<div class="row justify-content-center">
  <div class="col-md-8">
    {% include figure.liquid loading="lazy" path="assets/img/projects/egg/static_pipeline.png" title="Original egg image, grayscale image, binary mask, and extracted contour" class="img-fluid rounded" %}
  </div>
</div>
<p class="caption">An example of the static image-processing sequence. Contour quality affects the reliability of the extracted features.</p>

To check the measurement stage, I compared vision-derived ESI with manual caliper measurements. The study reported a **mean relative error of 0.788%** and a **maximum relative error of 3.108%** across the 90 eggs. These are measurement-agreement results under the study conditions, not a guarantee for arbitrary uploaded images.

<h2 id="risk">Linking morphology to rolling-risk grades</h2>

I used descriptive statistics, Pearson correlations, and one- and two-factor analyses of variance to examine associations between morphology and rolling behavior. Asymmetry and selected Hu moments showed relationships with instability that were not captured by size alone. These associations suggest useful predictors; they do not establish a causal mechanism by themselves.

The three dynamic outcomes were standardized and combined through principal component analysis. The first two components explained **81.751%** of their variance. A weighted composite was scaled to a **0–100 Rolling Stability Index (RSI)**, with higher values representing higher instability within this study. K-means then produced three risk grades.

The resulting groups are strongly imbalanced, with relatively few low-risk trials. That imbalance is important when interpreting the classification results.

RSI is an **experiment-derived instability label**, not a measured probability of shell breakage. The risk groups summarize motion in this dataset; their proportions should not be interpreted as the prevalence of damage in commercial egg handling.

<h2 id="results">Predicting risk from static morphology</h2>

The prediction task uses static features as inputs and the dynamic RSI grade as the target. The final thesis reports an **80:20 stratified trial-level split**: 216 training records and 54 test records, with five-fold cross-validation within the training set for model selection.

<figure class="hy-research-figure">
  <div class="hy-figure-canvas"><img src="{{ '/assets/img/research/egg-performance.svg' | relative_url }}" alt="A compact comparison of reported accuracy, macro F1, and macro AUC. Redrawn from final-thesis Table 2.15; the axes span 50–100%. These are reported scores, not a new training run." loading="lazy" width="1000" height="580"></div>
  <figcaption><span>Figure 1.</span> A compact comparison of reported accuracy, macro F1, and macro AUC. Redrawn from final-thesis Table 2.15; the axes span 50–100%. These are reported scores, not a new training run.</figcaption>
</figure>

**SVM led on accuracy and macro F1; gradient boosting led on macro AUC.** These metrics measure different aspects of classification, so a model should not be described as best on every measure. The results above follow the final thesis table; earlier analysis exports and the companion app contain different training results and are not combined with this benchmark.

Random-forest and gradient-boosting feature importance offered a complementary view of the predictors, including asymmetry, axis length, and Hu moments. These tree-model explanations are not explanations of the SVM's internal decisions, and feature importance is not causal attribution.

<h2 id="application">From the innovation project to an interactive application</h2>

The innovation project extended the experimental analysis into **Egg_RSI_App**, a Streamlit application with two complementary uses: exploring the study dataset and trying image-based risk classification.

The interface exposes the segmentation and feature-extraction stages, supports selecting example eggs or uploading a photograph, and provides model selection with predicted classes and class probabilities. Its image-processing implementation uses OpenCV, including an optional pretrained segmentation model and fallback segmentation strategies.

The application is a **research demonstration**. It has its own saved models and preprocessing implementation; its outputs should not be treated as a reproduction of the final-thesis benchmark or as production-validated handling instructions. Photographs taken under different lighting, scales, backgrounds, or viewpoints may differ substantially from the training conditions.

[Open the application](https://egg-rsi-app.streamlit.app) · [Explore the public code](https://github.com/WenTian1111/egg-rsi-app)

<h2 id="limitations">What remains to be tested</h2>

The study establishes a workflow for relating observable shape to measured motion, but several boundaries matter:

- **Independent specimens.** Three trials come from each egg. Stronger generalization evidence requires holding out entire eggs and new batches, not only individual trial records.
- **Class imbalance.** Only 12 trials fall in the low-risk group, so apparently strong performance on that class needs confirmation with more specimens.
- **External conditions.** The experiment uses one inclination, surface, batch, and acquisition setup. New surfaces, breeds, sizes, and conveyor conditions require further testing.
- **Outcome validity.** Motion-based risk grades are not direct measurements of breakage or economic loss. Those outcomes would need separate validation.
- **End-to-end evaluation.** Feature extraction, scaling, risk-label construction, and model selection should all be checked together under a specimen-independent evaluation protocol.

A useful next step is a larger, multi-condition experiment with egg-level holdouts and direct damage measurements. That would test whether the proposed risk grading remains useful outside the original setup.

<p class="hy-source-note">Research record: final undergraduate thesis (May 2026), municipal innovation-training research and completion reports (2026), and the companion application. These materials describe related work using the same experimental series.</p>
