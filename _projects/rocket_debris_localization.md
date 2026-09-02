---
layout: page
title: Multi-Object Localization of Rocket Debris
description: Sonic-boom triangulation of rocket debris — WGS84 coordinate conversion, a four-sphere intersection model, traversal matching and Monte Carlo error analysis.
img: assets/img/projects/rocket/rocket_cover.png
importance: 2
category: research
---

**How do you recover multiple pieces of rocket debris that fell over an unknown area?** After a rocket stage separates, its debris falls at supersonic speed, generating sonic booms that ground monitoring devices can record. This project turns those arrival-time recordings into precise geographic positions — for one debris piece, and for several pieces at once — using spherical-intersection geometry, nonlinear optimization and Monte Carlo simulation.

The work was published in *Frontiers of Progress in Computational Mathematics and Modeling* (Vol. 5, No. 1).

---

## 1 · From sonic boom to position

Each monitoring device records the arrival time of the sonic-boom shock wave. Given the sound speed, the device–debris distance is known, so the debris must lie on a sphere centred at the device. With **geodetic coordinates (WGS84) converted to Earth-centred Cartesian coordinates**, several spheres can be intersected to pin the debris down.

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/rocket/devices_global.png" title="Seven monitoring devices around the predicted impact area" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Seven monitoring devices deployed around the predicted impact area (global view).
</div>

## 2 · The four-sphere intersection model

Two spheres intersect in a circle; three spheres intersect in at most two points; and a fourth sphere resolves the ambiguity — but now the unknown sonic-boom *time* adds a fourth unknown, which is why **four devices are the mathematical minimum**.

<div class="row justify-content-center">
    <div class="col-7 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/rocket/sphere_intersection.png" title="Sphere intersection geometry" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Geometry of sphere intersection used for the positioning model.
</div>

The system is solved by **nonlinear least squares** (MATLAB `lsqnonlin`), jointly estimating the debris position (longitude, latitude, altitude) and the sonic-boom time.

## 3 · Single-debris localization (Problem 1)

Among the seven devices, the four **furthest apart** — A, B, E, G — give the smallest positioning error. With exactly four arrival-time readings, the model recovers the debris location and boom time:

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/rocket/problem1_localization.png" title="Single-debris localization result" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Localization result for a single debris piece (Problem 1).
</div>

**Key result:** at least **four monitoring devices** are required to locate one debris piece and its sonic-boom time.

## 4 · Multi-debris matching (Problems 2 & 3)

With four debris pieces, each device may hear multiple booms, and the readings must first be **matched** to the right debris. A traversal exclusion algorithm enumerates all plausible assignments — the 4×4 arrival-time table yields **256 combinations** of possible time assignments; each is substituted into the positioning model, and infeasible (non-negative constraint violated) solutions are eliminated, leaving **73 valid candidate sets** that identify the correct debris–reading correspondence.

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/rocket/problem3_matching.png" title="Four debris pieces localized" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Localization of the four debris pieces after traversal matching (Problem 3).
</div>

## 5 · Error analysis (Problem 4)

Real devices record arrival times with error, so the model is refined with **weighted least squares** and stress-tested with **Monte Carlo simulation** — repeatedly re-solving under timing errors (e.g. ±0.5 s) to map the stability of the solution:

<div class="row justify-content-center">
    <div class="col-9 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/rocket/problem4_error.png" title="Error simulation under device noise" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Positioning stability under simulated device recording errors (Problem 4).
</div>

**Takeaway:** if timing error cannot be reduced, positioning accuracy improves by **increasing the number of devices**, which dilutes the influence of any single faulty reading.

---

**Stack:** MATLAB (`lsqnonlin`, `geoscatter`) · WGS84 ↔ ECEF conversion · nonlinear least squares · weighted least squares · Monte Carlo simulation

*Published as: YANG Han. "Research on Multi-Object Localization of Rocket Debris." Frontiers of Progress in Computational Mathematics and Modeling, Vol. 5, No. 1.*
