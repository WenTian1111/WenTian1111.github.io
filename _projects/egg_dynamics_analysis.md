---
layout: page
title: Egg Rolling Analysis & Risk Sorting
description: Machine-vision study of egg rolling dynamics — from a 90-egg experiment to an ML rolling-risk index and live web app.
img: assets/img/projects/egg/egg_pipeline.png
importance: 1
category: research
---

**This project builds an end-to-end machine-vision pipeline for egg rolling dynamics.** A standardized experiment on 90 eggs produces static morphology and rolling-video data; statistical coupling analysis links the two; a data-driven Rolling Stability Index (RSI) quantifies rolling risk; and machine-learning classifiers turn the whole pipeline into automated sorting. The work was carried out as a **provincial-level Innovation & Entrepreneurship Training Program** (Excellent completion) and as my graduation thesis.

<div class="row justify-content-center">
    <div class="col-md-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/roadmap.png" title="Research roadmap" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 1.</em> Overall research roadmap: sample collection, feature extraction, database construction, PCA-based risk grading, ML prediction and intelligent sorting.
</div>

### 1 · Experiment setup

Each egg is photographed statically and then rolled down a 2.87° inclined flexible-contact surface under a high-speed camera. In total, static contours of **90 eggs** and **270 rolling videos** were collected.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/experiment_platform.png" title="Experiment platform" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 2.</em> Dual-zone rig: static contour imaging plus high-speed recording of the rolling phase.
</div>

### 2 · Feature extraction

From each egg, **11 static morphological features** are extracted — egg shape index (ESI), asymmetry index (AI), eccentricity, area, axis lengths and Hu moments — and from each rolling video **3 dynamic indicators**: lateral deviation ΔY, attitude-angle variance and speed coefficient of variation. Vision-based ESI reaches only **0.788% mean error** against manual measurement, accurate enough to replace hand measurement entirely.

<div class="row justify-content-center">
    <div class="col-md-8 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/static_pipeline.png" title="Static feature extraction pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 3.</em> Static processing chain: original image → grayscale → binary mask → contour with centroid and bounding box.
</div>

### 3 · Static–dynamic coupling analysis

Correlation analysis over 270 trials shows that **higher-order contour features dominate rolling stability** — Hu3 and asymmetry index are the strongest predictors of speed variation during rolling (r ≈ 0.50, p < 0.001), while first-order size features matter far less.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/correlation_top_pairs.png" title="Top static-dynamic correlations" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 4.</em> Top Pearson correlations between static morphology and dynamic rolling behaviour (N = 270). Significance: * p &lt; 0.05.
</div>

### 4 · Rolling Stability Index (RSI)

The three dynamic indicators are fused by **PCA** into a single fragility index — RSI on a **0–100 scale** — then **K-means** separates trials into low / medium / high risk groups (12 / 127 / 131 of 270). One number now summarizes an egg's rolling risk.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/rsi_distribution_groups.png" title="RSI distribution and risk groups" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 5.</em> RSI histogram (top) and trial-level RSI coloured by K-means risk group (bottom).
</div>

### 5 · Classification & results

Four classifiers are trained on the fused feature set; **SVM achieves the highest macro-AUC (0.861)** with 72–74% test accuracy, making automated rolling-risk sorting feasible in practice.

<div class="row justify-content-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/model_performance.png" title="Classifier performance" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/roc_curves.png" title="Macro-average ROC curves" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 6.</em> (a) Classifier performance on the independent test set. (b) Macro-average ROC curves of LR / SVM / RF / GBDT.
</div>

---

### Try it live 🚀

The trained pipeline is wrapped in an interactive web app — upload one egg photo and get an instant rolling-risk prediction:

👉 [**Egg_RSI_App — live demo**](https://egg-rsi-app.streamlit.app)

**Stack:** Python · OpenCV · MATLAB · scikit-learn · PCA · K-means · SVM / RF / GBDT · Streamlit Cloud

*Carried out as a provincial-level College Students' Innovation and Entrepreneurship Training Program (solo leader, Excellent completion) and as the graduation thesis "Static–Dynamic Coupled Analysis and Sorting of Eggs Based on Machine Vision" (four-member team, led by me).*
