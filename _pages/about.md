---
layout: about
title: about
permalink: /
subtitle: <a href='mailto:2549675208a@gmail.com'>2549675208a@gmail.com</a>

profile:
  align: right
  image:
  image_circular: false
  more_info: >

selected_papers: true
social: true

announcements:
  enabled: true
  scrollable: true
  limit: 10

latest_posts:
  enabled: false
---

I graduated from **Southwest University** in 2026, where I majored in Animal Science and minored in Applied Mathematics. My academic vision is to bridge ancient Chinese philosophical frameworks with modern scientific inquiry, exploring the fundamental logic underlying the universe.

During my undergraduate years, I developed strong analytical skills through mathematical modeling competitions and hands-on research — from trajectory analysis and optical sensing to semiconductor thermal modeling. I also completed a provincial-level College Students' Innovation and Entrepreneurship Training Program as a solo researcher, applying machine vision and data-driven methods to agricultural engineering.

Beyond the lab, I have a deep interest in the _Yijing_, _Daoism_, and traditional Chinese cosmology. My long-term research goal is to bridge ancient Chinese philosophical frameworks with modern scientific inquiry, exploring the fundamental logic underlying the universe. CUHK offers the ideal interdisciplinary environment to pursue this vision.

### Education

- **B.Sc. Animal Science** (Sep. 2022 - Jun. 2026)
  - Minor in Applied Mathematics
  - Southwest University (SWU)

### Research Experience

- **ESI-Curvature Modeling of Egg Trajectories: Morphological Effects** (*Independent Research*)
  - Jun. 2025 - Jun. 2026
  - Completed independently as the project leader. Built a standardized image acquisition platform with a 2.87-degree inclined flexible-contact surface, collecting static contour images of 90 egg samples and 270 rolling videos. Extracted 11 static morphological features (egg shape index ESI, asymmetry index AI, Hu moments, etc.) and 3 dynamic indicators (lateral deviation, attitude-angle variance, velocity coefficient of variation) via machine vision, with vision-based ESI achieving only 0.788% mean error vs. manual measurement. Statistical analysis revealed AI as the dominant driver of rolling instability and higher-order contour features as modulators. Fused the dynamic indicators into a fragility index (RSI 0-100) via PCA and K-means clustering, and trained SVM/RF/GBDT/LR classifiers, with SVM selected as the optimal model. Developed and deployed the web application `Egg_RSI_App` (Streamlit Cloud) for rolling-risk prediction from static images.

- **Machine Vision for Coupled Egg Dynamics & Intelligent Sorting** (*Leader*)
  - May 2025 - May 2026
  - Led and supervised a four-member team in machine-vision-based egg analysis and sorting theses: developed kinematic time-series extraction (centroid, attitude, velocity, acceleration), coupled static morphology with dynamic rolling for risk prediction via a PCA-based rolling stability index, trained four ML classifiers with SVM optimal (74.07% on 90 eggs, 270 videos), clustered trajectories into three stability classes via GMM, and built multi-species egg classifiers from fused HSV and LBP features (8 species, 713 images; KNN 99.30%).

- **Research on Multi-Object Localization of Rocket Debris** (*Independent Research*)
  - May 2024 - Aug. 2024
  - Developed a rocket debris localization and landing-point prediction strategy based on sonic-boom signals: converted WGS84 geodetic coordinates to Earth-centered Cartesian coordinates, built an improved tri-sphere and quad-sphere intersection model solved by nonlinear least squares (MATLAB lsqnonlin) to locate single debris with at least four monitoring devices, applied a traversal algorithm over 256 time combinations with feasibility filtering to match four debris pieces to their arrival times, and introduced weighted least squares with Monte Carlo simulation to analyze localization stability under 0.5 s timing errors.

- **Various Mathematical Modeling Competitions** (*Leader; Independent Research*)
  - Mar. 2023 - Jan. 2026
  - Led teams or worked independently on competition papers for mathematical modeling. Notable works include: the 2024 Certified Cup Challenge (finite-element skull model based on the Ogden constitutive model), the 2024 CUMCM (helical coiling dragon simulation via polar-angle iteration and Simpson's rule), and the 2025 CUMCM (multi-objective UAV smoke-screen jamming simulation optimized by a particle swarm algorithm with dual-plane projection occlusion modeling).
