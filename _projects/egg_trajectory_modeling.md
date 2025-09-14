---
layout: page
title: ESI-Curvature Modeling of Egg Trajectories
description: A research project on modeling the morphological effects on egg trajectories using high-speed cameras and MATLAB.
importance: 1
category: Research
---

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/egg_project_placeholder.jpg" title="Egg Rolling Test Rig" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    A placeholder image for the custom-designed egg rolling test rig.
</div>

This project, which I led, focused on understanding the relationship between an egg's physical shape and its dynamic rolling behavior. Our primary goal was to create a predictive model that could eventually be used for intelligent egg sorting systems.

---

### Methodology

1.  **Experimental Setup**: We designed and built a custom egg rolling test rig. This setup allowed us to release eggs from a consistent height and initial velocity, ensuring standardized data collection.
2.  **Data Acquisition**: Using a high-speed camera, we captured video footage of 90 different egg samples rolling on a planar surface.
3.  **Data Processing**: We utilized **MATLAB** for video processing. Key steps included:
    -   Converting 3D motion into a 2D planar model.
    -   Applying Kalman filtering and its extended forms to accurately track the egg's position.
    -   Extracting key dynamic features, such as trajectory path, instantaneous velocity, acceleration, and wobble patterns.
4.  **Modeling and Analysis**: We applied polynomial fitting to the extracted trajectories and analyzed the impact of the egg's shape index and eccentricity on its path.

---

### Outcomes & Impact

The project was successfully approved at the university level and is currently being prepared for submission to the **National Undergraduate Innovation and Entrepreneurship Training Program**. The methodologies and findings have laid the groundwork for a planned JCR Q1 research paper, contributing a novel, data-driven basis for advanced agricultural sorting technologies.
