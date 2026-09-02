---
layout: page
title: Applied Mathematical Modeling
description: Seven competition challenges — user analytics, energy dispatch, biomechanics, precision cutting, cultural simulation, submarine rescue and aerial operations.
img: assets/img/projects/modeling/modeling_cover.png
importance: 3
category: research
---

**Three years of mathematical modeling competitions, seven real-world problems.** As team leader (and, several times, as a solo researcher), I built end-to-end solutions spanning data science, energy systems, biomechanics, computational geometry and operations research — each one a complete cycle of problem analysis, model design, numerical implementation and result validation. Each challenge is described below together with a schematic of the modeling approach.

### 1 · Smartphone User Behavior Analytics

Millions of users generate app-usage telemetry, and mobile operators need to understand who uses what, when. I applied three clustering approaches — crow-search, density-peak and DBSCAN — over 20 app categories to segment users, then built prediction models for app usage: logistic regression for usage classification and random-forest regression (evaluated under NMSE) for forecasting daily effective use of key app classes. The analysis also drove per-user app recommendations from traffic and hourly-activity patterns.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m1_clustering.png" title="User clustering" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 1.</em> Users are segmented into behaviour clusters; each segment receives tailored app recommendations.
</div>

### 2 · Microgrid Dispatch with Renewable Storage

A campus microgrid powered by wind and solar must satisfy load while avoiding curtailment — the classic renewable-storage scheduling problem. I built day-ahead dispatch models for the three sub-grids with and without storage: without storage, unit power-supply costs were 0.818 / 0.716 / 0.704 yuan/kWh with 951–1128 kWh curtailed; adding battery storage, I derived optimal storage sizing (e.g. 377 kW/1130 kWh for grid A) and operating strategies that minimize curtailment and total supply cost.

<div class="row justify-content-center">
    <div class="col-md-7 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m2_dispatch.png" title="Microgrid dispatch" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 2.</em> Matching wind–solar generation with load; the battery absorbs surplus and releases it at peak hours.
</div>

### 3 · Bench-Dragon Procession Simulation

A 223-segment bench dragon (one head, 221 body links, one tail) winds into an equi-spaced spiral of pitch 55 cm at 1 m/s. I built a full kinematic simulation of the linked rigid-body chain: positions and velocities of every joint at each second up to 300 s, the latest collision-free winding time, and the minimal spiral pitch that allows the dragon to reverse direction inside a 9 m-diameter turning circle — combining polar-angle iteration with Simpson-rule integration over the spiral.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m3_dragon.png" title="Bench dragon spiral" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 3.</em> The linked dragon chain winding along the 55 cm-pitch spiral; every joint position and speed is computed per second.
</div>

### 4 · Submarine Search & Rescue

Searching for a lost submarine is a stochastic, current-dominated positioning problem. My model combined a **density-sphere / probability-circle** framework with buoyancy-and-current trajectory dynamics, solved via randomized search and multi-objective optimization, to support deployment, rescue and search planning for a disabled submarine under ocean-current drift.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m4_submarine.png" title="Submarine search" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 4.</em> From the last known position, the drift model expands a probability region that guides the search pattern.
</div>

### 5 · Craniotomy Biomechanics

Opening the skull for tumour removal or haematoma evacuation deforms the brain — dangerous when millimetres matter. I built a three-dimensional finite-element head model from constitutive equations, state equations and Newtonian motion, parameterized by literature elastic moduli, Poisson ratios, pre-operative CT and intracranial pressure. Stage one simulated whole-brain displacement for uncomplicated craniotomy (forcing at 0.1 N); stage two extended the model with the **Ogden hyperelastic constitutive law** to track how solid or fluid lesions migrate under the open window.

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m5_craniotomy.png" title="Craniotomy FE model" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 5.</em> FE mesh of the brain section with a surgical window and retraction force, tracking lesion displacement.
</div>

### 6 · Steel-Plate Cutting Path Optimization

In mould manufacturing, cutting efficiency comes down to minimizing the tool's idle travel. Framing the plate as a graph problem, I applied Euler-circuit reasoning from the seven-bridges problem: for open contours the cut is executed as a single-stroke path, and for closed contours I built a greedy Eulerian algorithm. Elliptical and circular inserts were parameterized and solved with Euclidean-distance geometry, giving provably short idle paths (validated against brute-force alternatives).

<div class="row justify-content-center">
    <div class="col-md-6 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m6_cutting.png" title="Cutting path" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 6.</em> A one-stroke (Eulerian) tool tour that visits every contour while minimizing idle travel.
</div>

### 7 · UAV Smoke-Screen Jamming

A defensive UAV carrying smoke jammers must blind an incoming missile's seeker over a ground target for as long as possible. I built 3-D kinematic models of the UAV, missile and smoke-cloud, a **dual-perpendicular-plane occlusion model** that projects target, missile and cloud onto the xy-plane and the uv-plane along the line of sight, and a Boolean indicator-function decision rule for visibility. A particle-swarm optimizer tuned the UAV's heading, speed, drop time and detonation time: maximum occlusion time of **4.448 s** for one jammer, extended later to multi-cloud cooperative jamming (optimal concealment 11.926 s).

<div class="row justify-content-center">
    <div class="col-md-7 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/modeling/m7_uav.png" title="Smoke occlusion" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    <em>Figure 7.</em> The smoke cloud intersects the missile–target line of sight; PSO-optimized drop and detonation maximize occlusion time.
</div>

---

*Competition series: served as team leader or independent researcher across these challenges, earning first-class awards at national and provincial levels (2023–2025). Figures are schematic illustrations of each modeling approach.*
