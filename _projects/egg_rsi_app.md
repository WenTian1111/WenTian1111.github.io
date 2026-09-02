---
layout: page
title: Egg_RSI_App
description: Machine-learning egg rolling-risk prediction from a single static photo — deployed live on Streamlit Cloud.
img: assets/img/egg_rsi_app.png
importance: 1
category: research
---

**Egg Roll Stability Analysis System** — upload an egg photo and get a real-time rolling-risk score (RSI 0–100) predicted by machine learning models.

## Live Demo (no installation required)

👉 [**https://egg-rsi-app.streamlit.app**](https://egg-rsi-app.streamlit.app)

## Overview

A machine-learning-based intelligent prediction system for egg roll stability. The app automatically extracts morphological features from a static egg image and predicts the rolling-risk level in real time. Completed as a solo researcher under the provincial-level College Students' Innovation and Entrepreneurship Training Program (Excellent completion).

## Method

- Built a standardized image acquisition platform with a 2.87° inclined flexible-contact surface; collected static contour images of 90 egg samples and 270 rolling videos
- Extracted 11 static morphological features (egg shape index ESI, asymmetry index AI, Hu moments, etc.) and 3 dynamic rolling indicators (lateral deviation, attitude-angle variance, velocity coefficient of variation) via machine vision
- Vision-based ESI achieved **0.788% mean error** vs. manual measurement
- Fused dynamic indicators into a fragility index (**RSI 0–100**) via PCA and K-means clustering
- Trained and compared SVM / RF / GBDT / LR classifiers — **SVM selected as the optimal model**

## Highlights

- 📷 Single static photo → full rolling-risk prediction pipeline
- 🚀 Deployed on Streamlit Cloud, usable directly in the browser
- 💻 Fully offline-capable source package with one-command launch

## Stack

Python · OpenCV · Streamlit · scikit-learn · PCA · K-means · SVM / RF / GBDT
