---
layout: page
title: Egg Rolling Analysis & Risk Sorting
description: Coupled static–dynamic analysis of egg rolling via machine vision — from a 90-egg experiment to an ML-driven rolling-risk index and a live web app.
img: assets/img/projects/egg/egg_pipeline.png
importance: 1
category: research
---

An end-to-end machine-vision study of egg rolling dynamics: a standardized experiment on 90 eggs (270 rolling trials) produces static morphology and dynamic rolling features, which are coupled into a Rolling Stability Index (RSI) and used to train classifiers for automated quality sorting. The complete pipeline — from experiment to a deployable web application — was delivered as a **provincial-level Innovation & Entrepreneurship Training Program** (Excellent completion) and formed the basis of my graduation thesis.

## Experiment & feature pipeline

![Egg rolling pipeline](/assets/img/projects/egg/egg_pipeline.png)

Eggs roll down a 2.87° inclined flexible-contact surface and are recorded by a high-speed camera. Static contour images and rolling videos are processed automatically to extract 11 static morphological features (egg shape index ESI, asymmetry index AI, Hu moments, etc.) and 3 dynamic rolling indicators (lateral deviation, attitude-angle variance, speed coefficient of variation). Vision-based ESI matched manual measurement with only **0.788% mean error**.

## Static–dynamic coupling

![Top static-dynamic correlations](/assets/img/projects/egg/correlation_top_pairs.png)

Pearson correlation analysis over 270 trials revealed that higher-order contour features (e.g., Hu3, asymmetry index) are the dominant drivers of rolling instability, with speed variation showing the strongest associations (r ≈ 0.50, p < 0.001).

## Rolling Stability Index (RSI)

![RSI distribution and K-means risk groups](/assets/img/projects/egg/rsi_distribution_groups.png)

The three dynamic indicators are fused via PCA into a fragility index — **RSI on a 0–100 scale** — and K-means clustering separates the trials into three risk groups (low / medium / high). The index gives egg processors a single interpretable number for rolling-risk.

## Model comparison

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/model_performance.png" title="Classifier performance" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/egg/roc_curves.png" title="Macro-average ROC curves" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

SVM/RF/GBDT/LR classifiers were trained on static-plus-dynamic features; **SVM achieved the highest macro-AUC (0.861)**, with 72–74% test accuracy across the top models.

## Try it live 🚀

The trained pipeline is wrapped in an interactive web app — upload a single egg photo and receive a real-time rolling-risk prediction:

👉 [**Egg_RSI_App — live demo**](https://egg-rsi-app.streamlit.app)

**Stack:** Python · OpenCV · MATLAB · scikit-learn · PCA · K-means · SVM / RF / GBDT · Streamlit Cloud

*This project was completed as a provincial-level College Students' Innovation and Entrepreneurship Training Program (solo leader, Excellent completion) and as the graduation thesis "Static–Dynamic Coupled Analysis and Sorting of Eggs Based on Machine Vision" (four-member team, led by me).*
