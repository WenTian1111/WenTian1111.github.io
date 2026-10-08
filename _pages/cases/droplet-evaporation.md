---
layout: han-project
title: Closed-Container Droplet Evaporation
description: A coupled heat–mass model of a sessile water droplet, linking closed-system
  vapor capacity to humidity, liquid volume, transient cooling and a temperature-driven
  regime switch.
permalink: /projects/modeling/droplet-evaporation/
discipline: Multiphysics · Heat and mass transfer
period: Foundational study
question: When can a droplet disappear inside a sealed container, and how do vapor
  accumulation and evaporative cooling shape the process?
role: AI-assisted mechanistic modeling, numerical verification, and research synthesis
methods: Mass and energy balances, spherical-cap geometry, coupled ODEs, capacity
  thresholds, independent reduced-model verification
outcome: 20°C / 25°C scenarios · 17.32 / 23.07 mm³ capacity thresholds · independent
  event and conservation checks
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Closed-system capacity
    id: capacity
  - label: 3. Coupled heat–mass model
    id: formulation
  - label: 4. Humidity accumulation
    id: humidity
  - label: 5. Volume evolution and the D² window
    id: volume
  - label: 6. Evaporative cooling
    id: temperature
  - label: 7. Substrate heat transfer
    id: substrate
  - label: 8. Warming and the regime-switch window
    id: comparison
  - label: 9. Parameter and assumption sensitivity
    id: sensitivity
  - label: 10. Numerical verification
    id: verification
  - label: 11. Discussion and conclusions
    id: discussion
  - label: Materials and related work
    id: materials
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

A droplet in an open environment can continually lose vapor to its surroundings. Inside a sealed container, the evaporated water remains in the air, reducing the driving force for further evaporation. Complete disappearance is therefore conditional on the available vapor capacity. This study first derives that condition, then couples vapor accumulation, shrinking liquid volume and evaporative cooling in one mechanistic model.

The baseline is a 10 mm³ pure-water droplet in a sealed 1 L container, initially dry air, a constant ambient temperature and an ideal hemispherical cap on an insulating substrate. At 20°C, the model reaches a 10 μm radius cutoff after 3.994 h, with final relative humidity 57.74% and a minimum droplet temperature near 7.18°C. At 25°C, the corresponding event occurs after 2.775 h, final relative humidity is 43.34%, and the minimum is 9.73°C. These are conditional numerical predictions, not experimental measurements.

The dry-air capacity thresholds are 17.32 and 23.07 mm³ at the two temperatures. A 20 mm³ droplet consequently retains liquid at 20°C but reaches the cutoff at 25°C after approximately 10.374 h. A new two-state Radau calculation eliminates vapor mass using exact conservation and independently reproduces the baseline event times within 0.00064 s. Parameter scans, solver comparisons and conservation checks support numerical consistency, while substrate conduction, contact-line behavior and spatial vapor transport remain major physical assumptions.

<h2 id="introduction">1. Introduction</h2>

### 1.1 Why three outputs need one model

Evaporation simultaneously decreases liquid mass, increases water vapor in the surrounding air and removes latent heat from the droplet. Treating humidity, volume and temperature as unrelated curves misses their feedback. A cooler droplet has a lower surface saturation density. A more humid container has a weaker vapor-density difference. A shrinking droplet changes its evaporation and heat-transfer scales.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/cover.webp' | relative_url }}" alt="Supplied conceptual illustration of a droplet in a glass cube. The visible glow, mist and apparent droplet scale are artistic devices, not observed vapor flow or experimental geometry. The calculation uses a sealed 1 L volume." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 1.</span> Supplied conceptual illustration of a droplet in a glass cube. The visible glow, mist and apparent droplet scale are artistic devices, not observed vapor flow or experimental geometry. The calculation uses a sealed 1 L volume.</figcaption></figure>

The physical scenario specifies a 10 cm cubic container and compares ambient temperatures of 20°C and 25°C. It does not supply an observed evaporation dataset, an initial droplet volume, initial humidity, contact angle or substrate thermal properties. Those missing quantities must be declared as scenario inputs rather than inferred from the picture.

### 1.2 A feasibility check before a time prediction

Even a perfectly implemented differential equation cannot make excess water disappear into a finite sealed vapor volume at equilibrium. The first question is therefore whether the total water amount fits within the container's unsaturated vapor capacity. Only then does an event time have a physical interpretation under the chosen model.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/workflow.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/workflow.svg' | relative_url }}" alt="Vector research roadmap derived from the governing equations. Liquid loss and vapor gain have opposite signs; the event is a small-radius cutoff. Humidity and energy feedback are evaluated within the same coupled model." width="1136" height="569" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 2.</span> Vector research roadmap derived from the governing equations. Liquid loss and vapor gain have opposite signs; the event is a small-radius cutoff. Humidity and energy feedback are evaluated within the same coupled model.</figcaption></figure>

The exposition follows capacity, governing equations, humidity, volume, temperature and then the temperature comparison. Numerical verification and assumption sensitivity are presented after the mechanism is established.

<h2 id="capacity">2. Closed-system capacity</h2>

### 2.1 Total water is conserved

Let mᵥ be vapor mass, mₗ liquid mass, V꜀ container volume, Tₐ ambient temperature and ρsat(Tₐ) saturated vapor density. Relative humidity here refers to the well-mixed container air evaluated at ambient temperature. The model conserves liquid plus vapor:

<div class="hy-equation">
\[
m_\ell(t)+m_v(t)=m_{\ell,0}+m_{v,0},\qquad \operatorname{RH}(t)=\frac{m_v(t)}{\rho_{\mathrm{sat}}(T_a)V_c}.
\tag{1}
\]
</div>

If all liquid enters the vapor phase, its limiting relative humidity is RH₀ + ρwV₀/[ρsat(Tₐ)V꜀]. For an unsaturated final state this quantity must be strictly less than one. The corresponding threshold is:

<div class="hy-equation">
\[
V_0^*=\frac{(1-\operatorname{RH}_0)\rho_{\mathrm{sat}}(T_a)V_c}{\rho_w},\qquad V_0\lt V_0^*\ \Longrightarrow\ \operatorname{RH}_\infty\lt 1.
\tag{2}
\]
</div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/capacity-regimes.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/capacity-regimes.svg' | relative_url }}" alt="Capacity thresholds calculated from the implemented saturation-density relation. Initial humidity consumes part of the capacity. The region below the threshold permits an unsaturated final state under the model assumptions." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 3.</span> Capacity thresholds calculated from the implemented saturation-density relation. Initial humidity consumes part of the capacity. The region below the threshold permits an unsaturated final state under the model assumptions.</figcaption></figure>

### 2.2 Three regimes, including the marginal case

Below the threshold, complete evaporation is compatible with mass conservation. Above it, the equilibrium residual liquid mass is ρw(V₀ − V₀\*), and vapor approaches saturation. At exact equality, the driving force also tends to zero as the droplet shrinks. Equality should not be advertised as a guaranteed finite disappearance time; it is a marginal limiting case, and the numerical cutoff further complicates that distinction.

For initially dry air, the 20°C threshold is 17.3195 mm³ and the 25°C threshold is 23.0750 mm³. A 10 mm³ droplet fits at both temperatures. At 20°C, its critical initial humidity is approximately 42.26%; above that, even this baseline water amount exceeds the remaining vapor capacity.

<div class="hy-model-table"><table><caption>Table 1. Declared baseline and what is actually supplied.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">Value</th><th scope="col">Evidence status</th></tr></thead><tbody><tr><td>Container geometry</td><td>10 cm cube; 1 L</td><td>Specified physical scenario</td></tr><tr><td>Ambient temperature</td><td>20°C and 25°C</td><td>Specified comparison</td></tr><tr><td>Initial water amount</td><td>10 mm³, or 9.98 mg</td><td>Declared baseline, not measured</td></tr><tr><td>Initial relative humidity</td><td>0%</td><td>Declared initially dry air</td></tr><tr><td>Contact angle</td><td>90°, constant</td><td>Ideal hemispherical cap</td></tr><tr><td>Substrate heat supply</td><td>Conductivity parameter zero</td><td>Insulating baseline</td></tr><tr><td>Stopping radius</td><td>10 μm</td><td>Numerical termination convention</td></tr></tbody></table></div>

The capacity result is more general than a particular rate calculation: changing transfer coefficients can change the time course without changing total-water equilibrium under the same volume, temperature and phase assumptions.

<h2 id="formulation">3. Coupled heat–mass model</h2>

### 3.1 Geometry and material closures

The state variable s = r² uses an equivalent radius defined from liquid–vapor surface area. For contact angle θ, cap volume and exposed area are:

<div class="hy-equation">
\[
V=C_\theta s^{3/2},\qquad A_{\ell v}=2\pi s,\qquad C_\theta=\frac{\pi}{3}(2+\cos\theta)\sqrt{1-\cos\theta}.
\tag{3}
\]
</div>

At 90°, Cθ = 2π/3 and the equivalent radius is the hemispherical radius. The 10 mm³ baseline gives r₀ = 1.68389 mm. A constant contact angle implies a receding contact line; it does not represent a pinned footprint.

The source uses a Buck-type saturation-pressure expression with explicit implemented coefficients, an ideal-gas conversion to vapor density, a temperature-dependent vapor diffusivity, an air-conductivity approximation and a temperature-dependent latent heat. Water density is fixed at 998 kg/m³ and heat capacity at 4,186 J/(kg·K). These are model closures; their use does not constitute a fitted evaporation experiment.

### 3.2 Evaporation flux

The baseline hemispherical diffusion approximation gives a positive outward evaporation rate:

<div class="hy-equation">
\[
\dot m=2\pi D(T_a)\Phi(T_s)\sqrt{s}\left[\rho_{\mathrm{sat}}(T_s)-\frac{m_v}{V_c}\right]_+,\qquad \Phi(T_s)=\frac{p_{\mathrm{atm}}}{p_{\mathrm{atm}}-p_{\mathrm{sat}}(T_s)}.
\tag{4}
\]
</div>

The positive-part operator prevents condensation in the implementation. Diffusivity is evaluated at ambient temperature, while saturation density and the Stefan-type correction use droplet temperature. This is a defined approximation, rather than a full multicomponent gas-transport solution.

### 3.3 Mass and energy use the same flux

The vapor gain is +ṁ, liquid loss is −ṁ, and the radius-squared equation follows by differentiating the cap volume. Air-side heat supply combines a conduction-limit coefficient kair/√s with linearized radiation. An optional substrate conductance is Gsub = 4kwalla, where a is the cap's base radius.

<div class="hy-equation">
\[
\begin{aligned}\frac{ds}{dt}&=-\frac{\dot m}{(3/2)\rho_w C_\theta\sqrt{s}},\\ \frac{dm_v}{dt}&=+\dot m,\\ \rho_w C_\theta s^{3/2}c_p\frac{dT_s}{dt}&=Q_{\mathrm{in}}-\dot m L_v(T_s).\end{aligned}
\tag{5}
\]
</div>

The liquid temperature is lumped: the same Tₛ represents bulk and surface. Ambient air is held at Tₐ by the modeled external thermostat. The base of the droplet does not evaporate. Contact-angle scans retain the area-equivalent hemispherical transfer approximation; only the hemispherical baseline is exact within that simplified geometry.

The shrinking liquid mass requires care in integrated energy accounting. Evaporation carries liquid sensible enthalpy as well as consuming latent heat:

<div class="hy-equation">
\[
\int_0^t Q_{\mathrm{in}}\,dt=\int_0^t\dot mL_v\,dt+\int_0^t\dot m c_pT_s\,dt+\left[m_\ell c_pT_s\right]_0^t.
\tag{6}
\]
</div>

This expression is the numerical balance used for verification. It should not be confused with a measured calorimetric balance.

<h2 id="humidity">4. Humidity accumulation</h2>

### 4.1 The container air becomes wetter

The saved baseline humidity trajectories rise monotonically from initially dry air. Their growth slows as the droplet shrinks and the vapor-density difference decreases. At the end of the 20°C trajectory, relative humidity is approximately 57.7383%; at 25°C it is 43.3370%.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/humidity-evolution.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/humidity-evolution.svg' | relative_url }}" alt="Relative humidity and absolute vapor density rebuilt from saved trajectories. Both cases evaporate the same baseline water mass, so final vapor density is approximately 9.98 g/m³, while temperature-dependent saturation density makes their relative humidities different." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 4.</span> Relative humidity and absolute vapor density rebuilt from saved trajectories. Both cases evaporate the same baseline water mass, so final vapor density is approximately 9.98 g/m³, while temperature-dependent saturation density makes their relative humidities different.</figcaption></figure>

The analytical full-evaporation values are 57.738358% and 43.337014%. Saved numerical deviations are only 0.0000347 and 0.0000415 percentage points, respectively. This is a mass-balance consistency check, not an accuracy comparison with a humidity sensor.

### 4.2 Container RH is not surface saturation

The air at a wet interface is locally saturated at the cooler droplet temperature in the diffusion approximation. Container relative humidity instead uses ambient temperature and a volume-mean vapor concentration. These are different quantities. A droplet can continue evaporating while container RH is far below 100% and its surface vapor density has already been reduced by cooling.

The archive also includes a quasistatic near-field profile proportional to r/ξ away from the effective droplet center. It provides an illustrative spatial correction around a spherical source. It is not a solved three-dimensional concentration field in the cube and does not establish actual mixing patterns at the walls.

<h2 id="volume">5. Volume evolution and the D² window</h2>

### 5.1 Volume decreases, but not at a constant rate

The coupled trajectories show monotonic liquid-volume loss. At 20°C the radius threshold is reached after 3.994217 h; at 25°C after 2.775195 h. Humidity feedback changes the evaporation rate, and the cap volume is nonlinear in radius squared. A straight line in r² therefore does not imply a straight line in volume.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/volume-and-d2.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/volume-and-d2.svg' | relative_url }}" alt="Volume and radius-squared evolution from saved outputs. The highlighted 10–40 min interval is the D² fitting window, after the initial rapid temperature adjustment. Later humidity accumulation causes departures from a constant slope." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 5.</span> Volume and radius-squared evolution from saved outputs. The highlighted 10–40 min interval is the D² fitting window, after the initial rapid temperature adjustment. Later humidity accumulation causes departures from a constant slope.</figcaption></figure>

### 5.2 A conditional D² relation

For the hemispherical baseline, differentiating volume simplifies the s equation to:

<div class="hy-equation">
\[
\frac{d(r^2)}{dt}=-\frac{2D(T_a)\Phi(T_s)}{\rho_w}\left[\rho_{\mathrm{sat}}(T_s)-\rho_v(t)\right]_+.
\tag{7}
\]
</div>

If the right-hand side varies slowly, r² is nearly linear over a window. The archive's 10–40 min fits have R² 0.999211 and 0.999293. New fits to the rounded five-second CSV outputs give 0.999207 and 0.999290, with slope magnitudes 3.00955 × 10⁻⁴ and 3.68113 × 10⁻⁴ mm²/s. The small difference is attributable to sampling and output precision.

These fit scores describe smooth model-generated trajectories. They are not experimental validation of the D² law or of the absolute evaporation rate. They also do not justify extending the fitted line through the late humidity-limited stage.

### 5.3 What “complete” means numerically

The solver terminates at r = 10 μm, not exactly zero. Output CSVs are sampled before the detected event, so their last remaining volumes differ slightly from the exact event residual. The event itself has hemispherical residual volume around 2.09 × 10⁻⁶ mm³, approximately 2.09 × 10⁻⁷ of the initial 10 mm³.

For readability, event times can be called near-disappearance times. Descriptions of mathematical zero volume, numerical cutoff and last saved output must retain this distinction.

<h2 id="temperature">6. Evaporative cooling</h2>

### 6.1 Fast cooling, then slow recovery

Both baseline droplets start at ambient temperature. Latent heat removal initially exceeds the available heat supply, causing a rapid temperature decrease. The 20°C case reaches 7.1777°C around 284 s, or 4.73 min. The 25°C case reaches 9.7290°C around 264 s, or 4.40 min.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/temperature-response.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/temperature-response.svg' | relative_url }}" alt="Absolute temperature and ambient-relative cooling. The 25°C case has a higher minimum in degrees Celsius, but its maximum drop below ambient is larger: approximately 15.27 K versus 12.82 K. Absolute temperature and cooling excursion should not be conflated." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 6.</span> Absolute temperature and ambient-relative cooling. The 25°C case has a higher minimum in degrees Celsius, but its maximum drop below ambient is larger: approximately 15.27 K versus 12.82 K. Absolute temperature and cooling excursion should not be conflated.</figcaption></figure>

As container humidity rises, evaporation weakens and the droplet temperature recovers. The last sampled values are approximately 14.40°C and 16.10°C. They remain below their respective ambient temperatures when the small-radius event ends the integration. The article does not continue a nonexistent lumped droplet after disappearance.

### 6.2 Quasisteady thermal balance

A wet-bulb-type scalar check finds the temperature at which instantaneous heat supply balances latent demand:

<div class="hy-equation">
\[
Q_{\mathrm{in}}(T_{\mathrm{wb}})=\dot m(T_{\mathrm{wb}})L_v(T_{\mathrm{wb}}).
\tag{8}
\]
</div>

At the dynamic minimum, this check differs from the saved temperature by about 0.000335 K at 20°C and 0.000856 K at 25°C. It supports the interpretation of a short initial relaxation toward a slowly evolving thermal balance. It is not an independent psychrometric observation, and the archived checking function is formulated for the insulating baseline.

The saved maximum lumped-temperature Biot indicators are approximately 0.058 and 0.060. Those values support the lumped approximation under the coefficients used in the calculation, while internal circulation, contact-line thermal gradients and substrate-induced spatial variations remain unresolved.

<h2 id="substrate">7. Substrate heat transfer</h2>

Substrate heat supply has a large effect. With the baseline substrate parameter zero, heat comes from the air and radiation, and the droplet cools substantially. Increasing the conductivity parameter makes the modeled base conductance larger, supplies more heat and shortens the evaporation process.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/substrate-envelope.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/substrate-envelope.svg' | relative_url }}" alt="Saved substrate scenarios at 20°C. The conductivity parameter enters an ideal spreading-conductance relation. The curves are scenario envelopes, not measured behavior of particular glass or acrylic containers." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 7.</span> Saved substrate scenarios at 20°C. The conductivity parameter enters an ideal spreading-conductance relation. The curves are scenario envelopes, not measured behavior of particular glass or acrylic containers.</figcaption></figure>

<div class="hy-model-table"><table><caption>Table 2. Archived substrate comparison at 20°C.</caption><thead><tr><th scope="col">Conductivity parameter</th><th scope="col">Minimum droplet temperature</th><th scope="col">Event time</th><th scope="col">Model interpretation</th></tr></thead><tbody><tr><td>0 W/(m·K)</td><td>7.18°C</td><td>3.994 h</td><td>Insulating baseline</td></tr><tr><td>0.2 W/(m·K)</td><td>15.24°C</td><td>Approximately 2.05 h</td><td>Additional idealized base heat supply</td></tr><tr><td>0.8 W/(m·K)</td><td>18.27°C</td><td>Approximately 1.67 h</td><td>Stronger idealized base heat supply</td></tr></tbody></table></div>

The conductance formula uses a contact radius and an ideal spreading resistance. Actual wall thickness, finite wall size, contact resistance, thermostat connection and changing wetting behavior are not measured or fitted. A material name alone cannot establish that its real container follows one of these curves.

The comparison is especially important for the supplied glass-cube cover: the picture should not imply that a strongly insulating baseline has already been verified in a glass device. A physical experiment would need to characterize heat transfer through the bottom wall before interpreting the deepest predicted cooling.

<h2 id="comparison">8. Warming and the regime-switch window</h2>

### 8.1 Same droplet, warmer ambient

Warming from 20°C to 25°C increases the saturated vapor capacity from roughly 17.28 to 23.03 mg, approximately 33.3%. The same 9.98 mg of water then occupies a smaller fraction of capacity. Vapor diffusivity also increases by roughly 3%. The coupled response gives a shorter event time and lower final relative humidity.

<div class="hy-model-table"><table><caption>Table 3. Temperature comparison under identical baseline inputs.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">20°C</th><th scope="col">25°C</th><th scope="col">Change</th></tr></thead><tbody><tr><td>Event time</td><td>3.994 h</td><td>2.775 h</td><td>30.52% shorter</td></tr><tr><td>Final relative humidity</td><td>57.74%</td><td>43.34%</td><td>14.40 percentage points lower</td></tr><tr><td>Minimum absolute temperature</td><td>7.18°C</td><td>9.73°C</td><td>2.55°C higher</td></tr><tr><td>Maximum drop below ambient</td><td>12.82 K</td><td>15.27 K</td><td>2.45 K larger</td></tr><tr><td>D²-window slope magnitude</td><td>3.010 × 10⁻⁴ mm²/s</td><td>3.681 × 10⁻⁴ mm²/s</td><td>Approximately 22.3% larger</td></tr><tr><td>Dry-air capacity volume</td><td>17.32 mm³</td><td>23.07 mm³</td><td>Approximately 33.3% larger</td></tr></tbody></table></div>

A higher temperature minimum does not mean a smaller cooling excursion, because the ambient temperature also changes. Likewise, the D² slope magnitude increases; it should not be illustrated as a decrease. Keeping signs and reference temperatures explicit makes the mechanistic comparison more useful.

### 8.2 A change in regime, not merely speed

For a 20 mm³ droplet in initially dry air, the two temperatures lie on opposite sides of the capacity threshold. At 20°C the new independent integration does not reach the stopping event over 48 h and retains 2.675413 mg of liquid. The equilibrium mass-balance expression gives 2.675130 mg. The difference is approximately 0.011%, consistent with an approach to equilibrium.

At 25°C the same new reduced model reaches the radius cutoff after 10.374294 h, agreeing with the archived 10.374295 h. Its final relative humidity is approximately 86.67%. This example illustrates a qualitative transition from a persistent liquid equilibrium to an admissible near-disappearance trajectory.

Failure to detect an event within a finite integration horizon is not by itself proof that liquid persists forever. Here the residual conclusion has the additional analytical capacity argument. This distinction is essential when interpreting other scanned cases near the threshold.

<h2 id="sensitivity">9. Parameter and assumption sensitivity</h2>

### 9.1 Initial amount and initial humidity

The archive scans initial volume from 5 to 20 mm³ at 20°C. Event time increases from approximately 1.81 h at 5 mm³ to 28.4 h at 17 mm³. Cases above the 17.3195 mm³ capacity threshold do not reach the event within 48 h and approach residual-liquid equilibria.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/initial-condition-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/initial-condition-sensitivity.svg' | relative_url }}" alt="Initial-condition scans rebuilt from saved files. The volume threshold is analytical; missing event-time values denote no detected event in the simulated horizon. Their equilibrium interpretation requires the accompanying capacity calculation." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 8.</span> Initial-condition scans rebuilt from saved files. The volume threshold is analytical; missing event-time values denote no detected event in the simulated horizon. Their equilibrium interpretation requires the accompanying capacity calculation.</figcaption></figure>

At fixed 10 mm³, raising initial relative humidity from zero to 40% increases the saved event time to approximately 24.7 h. The final RH changes linearly with initial RH in the full-evaporation regime, while the duration grows sharply as the remaining capacity becomes small.

A saved residual-mass expression is negative below threshold if used without its positive-part restriction. Such negative values are not physical residual liquid. The equation is applied only above the threshold, or clipped at zero for a combined regime plot.

### 9.2 Rate and geometry assumptions

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/geometry-and-transfer.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/geometry-and-transfer.svg' | relative_url }}" alt="Contact-angle approximation and joint air-side transfer scaling. The contact-angle calculation changes area-equivalent cap geometry; it is not the exact arbitrary-angle diffusion solution. The transfer scan changes both heat and mass coefficients together." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 9.</span> Contact-angle approximation and joint air-side transfer scaling. The contact-angle calculation changes area-equivalent cap geometry; it is not the exact arbitrary-angle diffusion solution. The transfer scan changes both heat and mass coefficients together.</figcaption></figure>

Contact angles from 5° to 90° produce time ratios of approximately 0.41–1.00 relative to the hemispherical baseline. The source uses a general cap-volume coefficient but retains the area-equivalent hemispherical transfer approximation. Its result is a geometric sensitivity envelope, not an exact prediction for every wetting angle.

A second scan multiplies both air-side heat and mass transfer by φ = 0.70–1.65. Event time changes from about 5.50 to 2.51 h. Final RH stays approximately 57.7383%, as required by conservation for fixed initial water and temperature. This is a useful internal regression check: a rate multiplier should not arbitrarily change the full-evaporation mass endpoint.

<div class="hy-model-table"><table><caption>Table 4. Assumption sensitivity and evidence limits.</caption><thead><tr><th scope="col">Assumption</th><th scope="col">Saved test</th><th scope="col">What remains unknown</th></tr></thead><tbody><tr><td>Initial water and humidity</td><td>Volume and RH scans with threshold crossing</td><td>Actual experimental initial conditions</td></tr><tr><td>Substrate heat supply</td><td>0–0.8 W/(m·K) parameter scan</td><td>Real wall and contact resistance</td></tr><tr><td>Ambient temperature</td><td>15–30°C scan</td><td>Humidity and thermal control in a device</td></tr><tr><td>Contact angle</td><td>5–90° area-equivalent scan</td><td>Pinning, hysteresis and exact-angle diffusion</td></tr><tr><td>Air-side transfer</td><td>Joint φ scaling, 0.70–1.65</td><td>Calibrated convection and mass-transfer coefficients</td></tr><tr><td>Well-mixed vapor</td><td>Geometric correction and timescale argument</td><td>Observed spatial concentration field</td></tr></tbody></table></div>

### 9.3 Mixing and natural convection

The source estimates a first diffusion-mode timescale near 41.75 s and a larger box-scale diffusion-front timescale near 400 s. These are different approximations; neither should be called an observed mixing time. A geometric mean-concentration correction changes archived baseline durations by −1.06% and −1.03%, without changing final humidity materially.

Archived thermal Rayleigh estimates are approximately 51.1 and 59.1 using droplet diameter. The small values and the modeled wall-adjacent configuration motivate a diffusion-dominated baseline, but low Rayleigh number alone does not experimentally prove that convection is absent. Correlations restricted to much larger Rayleigh numbers cannot be treated as directly validated for these cases. A spatial heat–mass calculation and measurements would be needed to substantiate the approximation more strongly.

<h2 id="verification">10. Numerical verification</h2>

### 10.1 Solver refinement is distinct from physical validation

The saved convergence CSV contains 36 configurations: two solvers, three tolerances, two output spacings and three stopping radii. Across all configurations, event time spans 3.993504–3.994451 h, a relative spread around 0.0237%. For a fixed stopping radius, the maximum relative solver/configuration spread falls to approximately 1.21 × 10⁻⁶.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/droplet-evaporation/verification-diagnostics.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size"><img src="{{ '/assets/img/research/droplet-evaporation/verification-diagnostics.svg' | relative_url }}" alt="Solver and cutoff diagnostics, together with conservation residuals. The small residuals demonstrate numerical consistency of the stated model. They do not measure agreement with a real evaporation experiment." width="1046" height="380" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 10.</span> Solver and cutoff diagnostics, together with conservation residuals. The small residuals demonstrate numerical consistency of the stated model. They do not measure agreement with a real evaporation experiment.</figcaption></figure>

The difference matters: varying the disappearance convention contributes much of the overall spread, while varying the solver within the same convention is much smaller. Counting all differences as solver error would misdescribe the numerical evidence.

<div class="hy-model-table"><table><caption>Table 5. Selected archived internal checks.</caption><thead><tr><th scope="col">Check</th><th scope="col">20°C</th><th scope="col">25°C</th><th scope="col">Interpretation</th></tr></thead><tbody><tr><td>Relative mass drift</td><td>3.20 × 10⁻⁷</td><td>2.13 × 10⁻⁷</td><td>Integrated state consistency</td></tr><tr><td>Maximum Biot indicator</td><td>0.0582</td><td>0.0597</td><td>Conditional lumped-temperature plausibility</td></tr><tr><td>Wet-bulb-type check deviation</td><td>0.000335 K</td><td>0.000856 K</td><td>Thermal-balance consistency</td></tr><tr><td>Energy accumulator residual</td><td>1.75 × 10⁻⁷</td><td>7.11 × 10⁻⁸</td><td>Shared-equation energy accounting</td></tr><tr><td>Trajectory quadrature residual</td><td>2.06 × 10⁻⁸</td><td>8.57 × 10⁻⁹</td><td>A separate integration of saved-state fluxes</td></tr></tbody></table></div>

### 10.2 New reduced-model reconstruction

The fresh calculation removes vapor mass from the ODE using mᵥ = mᵥ₀ + ρw(V₀ − V). It reconstructs the two remaining equations directly and uses Radau with different tolerances and step constraints. This provides a separate implementation path for the same physical assumptions.

<div class="hy-model-table"><table><caption>Table 6. New independent verification for this article.</caption><thead><tr><th scope="col">Quantity</th><th scope="col">20°C</th><th scope="col">25°C</th></tr></thead><tbody><tr><td>Fresh event time</td><td>3.994216904 h</td><td>2.775194518 h</td></tr><tr><td>Difference from archived event</td><td>−0.000631 s</td><td>+0.0000139 s</td></tr><tr><td>Maximum temperature difference on comparison grid</td><td>6.32 × 10⁻⁶ K</td><td>5.02 × 10⁻⁶ K</td></tr><tr><td>Maximum volume difference</td><td>5.54 × 10⁻⁸ mm³</td><td>9.33 × 10⁻⁸ mm³</td></tr><tr><td>Fresh energy quadrature residual</td><td>5.04 × 10⁻⁸</td><td>8.72 × 10⁻⁸</td></tr><tr><td>Recomputed rounded-CSV D² R²</td><td>0.999207</td><td>0.999290</td></tr></tbody></table></div>

Energy is independently integrated from the new state trajectory at 0.2 s sampling, rather than read from the source solver's cumulative energy states. The new capacity-window integration separately reproduces the 20 mm³ comparison. All 42 entries in the archive's run manifest match their recorded SHA-256 hashes, and all 115 original project files remain unchanged after analysis.

Rounded CSV outputs are less precise than full solver states. Their mass-balance discrepancies reach about 5.14 × 10⁻¹¹ kg, while the state-level drift is smaller. The article therefore does not substitute rounded-output differences for the original high-precision residuals.

These checks verify equations, implementation and numerical stability. Both implementations share the same material closures and idealized geometry, so their agreement cannot establish physical validity on its own.

<h2 id="discussion">11. Discussion and conclusions</h2>

The model explains three connected responses in a sealed volume. Evaporated water accumulates in the air; the shrinking cap changes the mass-transfer scale; latent heat removal lowers the droplet temperature. The resulting feedback produces rapid initial cooling, a near-linear intermediate D² window and a slower humidity-limited tail.

The strongest structural conclusion is the capacity threshold. It explains why a finite sealed container does not guarantee complete evaporation of an arbitrary droplet and why warming can change the equilibrium regime. Rate coefficients control when the system approaches that outcome; they cannot bypass closed-system mass conservation.

The reported durations and temperature minima remain scenario-dependent. Initial dryness, a 10 mm³ droplet, a hemispherical receding cap, an insulating substrate, a well-mixed far field and the chosen transfer closures jointly determine the baseline. A real glass-bottom experiment could supply substantially more substrate heat. Pinning or changing contact angle could alter geometry. Condensation, wall sorption and spatial vapor gradients could change the water partition.

A next experimental step would record initial liquid mass, RH, substrate temperature and droplet shape, then track volume and surface temperature over time. Calibration should estimate transfer and thermal parameters from part of those data and test the model against held-out conditions. A spatial transport model could then assess whether mean concentration is adequate and where the lumped approximation breaks down.

The current project is a verified mechanistic calculation and an explicit hypothesis about coupled evaporation. It is presented as foundational modeling work, with conditional predictions and a reproducible numerical record, rather than a completed experimental validation.

<h2 id="materials">Materials and related work</h2>

The article uses the original physical-scenario document, current model and verification reports, October 2026 run manifest, saved humidity/volume/temperature trajectories, six sensitivity scans and convergence results. The supplied cover is retained as a conceptual illustration. The scientific workflow is redrawn from the checked governing equations; original figures and manuscripts remain unchanged in the research archive.

For broader context, [Popov's analytical treatment of sessile-drop evaporation](https://doi.org/10.1103/PhysRevE.71.036313) develops a diffusion-based geometric description in a study of deposition from colloidal drops. That work has a different setting, including contact-line behavior and deposition, and is not empirical validation of this sealed pure-water scenario. Its general-angle treatment also underscores why an area-equivalent hemisphere should be labeled as an approximation when extending beyond 90°.

The figures distinguish archived numerical outputs, new independent reconstructions and conceptual illustrations. The original manuscripts and computational archive provide the underlying project record.
