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
    <div class="col-10 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/roadmap.png" title="Research roadmap" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Overall research roadmap: sample collection → feature extraction → database → PCA-based risk grading → ML prediction → sorting.
</div>

---

## 1 · Experiment setup

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/experiment_platform.png" title="Experiment platform" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Dual-zone rig: static contour imaging plus high-speed recording of the rolling phase on a 2.87° inclined flexible-contact surface.
</div>

Each egg is photographed statically and rolled down the incline under a high-speed camera. In total, static contours of **90 eggs** and **270 rolling videos** were collected for analysis.

## 2 · Feature extraction

<div class="row justify-content-center">
    <div class="col-11 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/static_pipeline.png" title="Static feature extraction pipeline" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Static processing chain: original image → grayscale → binary mask → contour with centroid and bounding box.
</div>

- **11 static morphological features** per egg: egg shape index (ESI), asymmetry index (AI), eccentricity, area, axis lengths, Hu moments…
- **3 dynamic rolling indicators** per video: lateral deviation ΔY, attitude-angle variance, speed coefficient of variation.
- Vision-based ESI reached only **0.788% mean error** against manual measurement — accurate enough to replace hand measurement entirely.

## 3 · Static–dynamic coupling analysis

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/correlation_top_pairs.png" title="Top static-dynamic correlations" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Top Pearson correlations between static morphology and dynamic rolling behaviour (N = 270 trials). Significance: * p &lt; 0.05.
</div>

Correlation analysis shows that **higher-order contour features dominate rolling stability** — Hu3 and asymmetry index are the strongest predictors of speed variation during rolling (r ≈ 0.50, p < 0.001), while first-order size features matter far less.

## 4 · Rolling Stability Index (RSI)

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/rsi_distribution_groups.png" title="RSI distribution and risk groups" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    RSI histogram (top) and trial-level RSI values coloured by K-means risk group (bottom).
</div>

The three dynamic indicators are fused by **PCA** into a single fragility index — RSI on a **0–100 scale** — then **K-means** separates trials into low / medium / high risk groups (12 / 127 / 131 of 270 trials). One number now summarizes an egg's rolling risk.

## 5 · Classification & results

<div class="row justify-content-center">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/model_performance.png" title="Classifier performance" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/roc_curves.png" title="Macro-average ROC curves" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    SVM / RF / GBDT / LR trained on static-plus-dynamic features; SVM achieves the best macro-AUC.
</div>

Four classifiers were trained on the fused feature set. **SVM achieves the highest macro-AUC (0.861)** with 72–74% test accuracy, making automated rolling-risk sorting feasible in practice.

---

## Try it live 🚀

The trained pipeline is wrapped in an interactive web app — upload one egg photo and get an instant rolling-risk prediction:

👉 [**Egg_RSI_App — live demo**](https://egg-rsi-app.streamlit.app)

**Stack:** Python · OpenCV · MATLAB · scikit-learn · PCA · K-means · SVM / RF / GBDT · Streamlit Cloud

*Carried out as a provincial-level College Students' Innovation and Entrepreneurship Training Program (solo leader, Excellent completion) and as the graduation thesis "Static–Dynamic Coupled Analysis and Sorting of Eggs Based on Machine Vision" (four-member team, led by me).*
