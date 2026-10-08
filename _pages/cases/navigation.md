---
layout: han-project
title: Multi-Source Navigation under Uncertain Signals
description: A study of heterogeneous signal fusion, moving-source geometry, channel-bias diagnostics, and correctly defined three-dimensional uncertainty checks.
permalink: /projects/modeling/navigation/
discipline: Statistical estimation · Sensor fusion
period: 2024 study
question: What can heterogeneous signals establish about motion when both channel reliability and uncertainty calibration are imperfect?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Physical measurement models, iterated Kalman filtering, timing-reference diagnostics, joint state–bias estimation, synthetic calibration checks
outcome: Two inferred trajectories · channel diagnostics · five new covariance-ellipsoid checks · explicit evidence limits
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Introduction
    id: introduction
  - label: 2. Data and source geometry
    id: data
  - label: 3. Measurement models
    id: measurement
  - label: 4. Temporal estimation
    id: temporal
  - label: 5. Timing-reference diagnostics
    id: diagnostics
  - label: 6. Joint state and offset estimation
    id: offsets
  - label: 7. Synthetic uncertainty calibration
    id: calibration
  - label: 8. Detection versus recovery
    id: detection
  - label: 9. Assumption sensitivity
    id: sensitivity
  - label: 10. Independent checks
    id: verification
  - label: 11. Discussion
    id: discussion
  - label: 12. Conclusions
    id: conclusions
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Position inference from opportunity signals combines measurements with different units, geometries, and error mechanisms. This study develops a transparent sequence from physical signal models to temporal estimation, timing-reference channel diagnostics, and joint trajectory–offset fitting. Two supplied ten-second records contain 1,001 samples and ten channels each. Known source positions and motions connect time of arrival, time difference of arrival, differential frequency, bearing tangents, and received power to a six-dimensional receiver state. A forward iterated extended Kalman filter is compared with pointwise nonlinear least squares and retrospective smoothing; subsequent stages screen suspect channels and estimate persistent offsets.

The supplied records have no independent position truth, so state smoothness, residual consistency, and posterior scale are not presented as field accuracy. Archived synthetic simulations report position RMSE of 3.69 ± 0.48 m across 50 trials. Their reported 41.64% coverage uses a scalar-radius rule that is **not a three-dimensional 95% confidence region**. This revision corrects that interpretation and adds five paired synthetic checks using the full position covariance: nominal 95% ellipsoids cover the generating trajectory in 69.0–88.7% of scored samples, averaging 76.3%. Channel-injection examples also separate detection from accurate bias recovery. The result is a research account of heterogeneous inference and its limits, with measurement definitions, numerical outputs, calibration checks, and identifiable evidence boundaries kept together.

<h2 id="introduction">1. Introduction</h2>

A moving receiver can infer position from signals that were not necessarily designed as a single navigation system. Timing constrains distance, differential timing compares distances, differential frequency depends on relative motion, bearing describes directional geometry, and received power introduces a propagation model. Their combination can improve inference, but only when units, sign conventions, source motion, and reliability assumptions are explicit.

The central difficulty is that unreliable measurements and weak geometry can look similar. A persistent received-power residual may indicate propagation bias, yet it can also reflect a misplaced reference trajectory. An estimated altitude can become smooth while remaining weakly identified. A covariance can shrink because an estimator trusts its assumptions, even when those assumptions do not describe the generating motion well.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/navigation/cover.webp' | relative_url }}" alt="Conceptual environment for positioning from heterogeneous opportunity signals" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual signal-fusion setting. It is not the supplied transmitter layout, a measured trajectory, or evidence of a deployed navigation system.</figcaption></figure>

The study therefore asks three distinct questions: what trajectory follows from the assumed measurement and motion models; which channels disagree with a selected reference; and how well the estimator's uncertainty describes errors in controlled synthetic trials. These questions are answered separately rather than reduced to a single accuracy score.

<h2 id="data">2. Data and source geometry</h2>

### 2.1 Two independent observation records

Each case contains ten channels sampled at 0.01 s from 0 to 10 s. Fresh input checks confirm two 1,001-by-10 measurement tables without missing values. The channel composition differs between cases. Case 1 includes four timing channels, one differential-frequency channel, two bearing tangents, and three received-power channels. Case 2 includes three timing channels, two differential-frequency channels, two bearing tangents, and three power channels.

The cases are solved independently. They are not assumed to follow the same trajectory, and differences between them do not supply a missing ground-truth reference.

<div class="hy-model-table"><table><caption>Table 1. Supplied source positions and constant velocities.</caption><thead><tr><th scope="col">Source</th><th scope="col">Initial position (m)</th><th scope="col">Velocity (m/s)</th></tr></thead><tbody>
<tr><td>1</td><td>(100, 300, 50)</td><td>(0, 0, 0)</td></tr>
<tr><td>2</td><td>(1,000, 100, 150)</td><td>(0, 0, 0)</td></tr>
<tr><td>3</td><td>(−1,000, −100, 450)</td><td>(0, 0, 8)</td></tr>
<tr><td>4</td><td>(−200, −100, 1,050)</td><td>(20, 0, 0)</td></tr>
</tbody></table></div>

### 2.2 Assumptions that define the inference

The sources follow their supplied constant-velocity motions. Time references are taken as synchronized, allowing direct use of arrival time and simultaneous-source timing differences. In the baseline estimation stage, channels are treated as unbiased with independent noise; later stages explicitly allow persistent offsets. Receiver motion is approximated by a constant-velocity state with process noise, and an above-ground position prior helps exclude geometrically ambiguous branches.

These assumptions are consequential. An unknown receiver clock would introduce another state or bias term. Incorrect source motion changes both ranges and range rates. A nonlinear bearing tangent can become singular near its denominator crossing. None of these issues is resolved merely by collecting more scalar measurements.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/source-and-trajectories.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/navigation/source-and-trajectories.svg' | relative_url }}" alt="Supplied transmitter geometry with two independently inferred receiver paths and altitude profiles" width="1186" height="514" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Source geometry and saved inferred trajectories. The source-4 arrow shows its horizontal displacement over ten seconds; source 3 moves vertically and therefore has no horizontal arrow. Curves are estimates, not measured position truth.</figcaption></figure>

<h2 id="measurement">3. Measurement models</h2>

### 3.1 Range and timing

For receiver position $\mathbf p$, source position $\mathbf s_i(t)$, and light speed $c$, timing predictions follow geometric range:

<div class="hy-equation">
\[
\begin{aligned}
\mathbf s_i(t)&=\mathbf s_{i0}+\mathbf v_i t,\\
d_i(t)&=\|\mathbf p-\mathbf s_i(t)\|,\\
\tau_i&=d_i/c,\\
\tau_{ij}&=(d_i-d_j)/c.
\end{aligned}
\tag{1}
\]
</div>

Observed TOA and TDOA values are multiplied by $c=3\times10^8$ m/s before fitting. Their residuals are therefore in meters, as are the corresponding model outputs. This avoids mixing tiny time values with much larger raw channel quantities in the numerical objective.

### 3.2 Relative range rate and differential frequency

Receiver velocity $\mathbf v$ and source velocity $\mathbf v_i$ give

<div class="hy-equation">
\[
\begin{aligned}
\dot d_i&=\frac{(\mathbf v-\mathbf v_i)\cdot(\mathbf p-\mathbf s_i)}{d_i},\\
F_{ij}&=\frac{f_0}{c}(\dot d_j-\dot d_i).
\end{aligned}
\tag{2}
\]
</div>

The supplied $f_0=3\times10^8$ Hz makes $f_0/c=1$ in the stated units. The difference order is retained as implemented: reversing it would change the sign of an inferred frequency discrepancy. Source motion enters both range and range rate; treating a moving source as stationary is a different model.

### 3.3 Bearing tangents and received power

The observations are already tangent quantities, rather than angles requiring angular wrapping. For source 4, their definitions are

<div class="hy-equation">
\[
\begin{aligned}
\tan\alpha&=\frac{s_y-p_y}{s_x-p_x},\\
\tan\beta&=\frac{\sqrt{(p_x-s_x)^2+(p_y-s_y)^2}}{p_z-s_z}.
\end{aligned}
\tag{3}
\]
</div>

Received power uses the supplied attenuation relationship, with coefficient $10k=200$, nominal power 100 dB, and nominal distance 1,000 m:

<div class="hy-equation">
\[
P_i=100-200\log_{10}(d_i/1000).
\tag{4}
\]
</div>

This coefficient is specific to the supplied model; it is not a measured universal propagation law. An offset in dB changes inferred distance multiplicatively. The tangent and power equations also show how an error in the reference position can create a systematic channel residual without a physical channel bias.

### 3.4 Normalize uncertainty before combining channels

The initial channel scale is estimated from first differences:

<div class="hy-equation">
\[
\widehat\sigma_k=\frac{\operatorname{sd}(z_{k,n+1}-z_{k,n})}{\sqrt2}.
\tag{5}
\]
</div>

This estimate assumes sufficiently slow signal change and approximately independent high-frequency errors. Correlation or rapid dynamics can violate that interpretation. It is a calibration rule, not a direct observation of true measurement noise.

<div class="hy-model-table"><table><caption>Table 2. Recomputed Case 1 channel scales, retained in their native fitting units.</caption><thead><tr><th scope="col">Channels</th><th scope="col">Estimated scales</th><th scope="col">Unit</th></tr></thead><tbody>
<tr><td>TOA1 / TOA4</td><td>25.35 / 26.23</td><td>m</td></tr>
<tr><td>TDOA12 / TDOA34</td><td>34.49 / 35.82</td><td>m</td></tr>
<tr><td>DFD12</td><td>0.691</td><td>m/s in the equivalent range-rate convention</td></tr>
<tr><td>tan α / tan β</td><td>0.217 / 0.226</td><td>Dimensionless</td></tr>
<tr><td>RSSI1 / RSSI2 / RSSI3</td><td>0.973 / 1.026 / 1.007</td><td>dB</td></tr>
</tbody></table></div>

The resulting weighted residual sum combines standardized quantities. Counting ten channels alone does not establish observability: local Jacobian rank, source geometry, and any added offset states determine which state directions are constrained.

<h2 id="temporal">4. Temporal estimation</h2>

### 4.1 Pointwise and state-based estimators

Pointwise nonlinear least squares provides a reference without a temporal trajectory prior. The forward filter instead uses $\mathbf x=(\mathbf p,\mathbf v)$ and a constant-velocity transition. For time step $\Delta t$, its transition and white-acceleration process covariance have the block form

<div class="hy-equation">
\[
\begin{aligned}
A&=\begin{bmatrix}I&\Delta t I\\0&I\end{bmatrix},\\
Q&=q\begin{bmatrix}\Delta t^3 I/3&\Delta t^2 I/2\\\Delta t^2 I/2&\Delta t I\end{bmatrix}.
\end{aligned}
\tag{6}
\]
</div>

The process scale is $q=5$ in the baseline. Constant velocity is a local prior, not a claim that acceleration is zero throughout the record. The IEKF performs three local measurement-linearization iterations at each sample. Initialization scores a 7-by-7-by-8 position grid and refines the best coarse start by nonlinear least squares; that is not 392 independently converged nonlinear solutions.

<div class="hy-equation">
\[
\begin{aligned}
\widehat{\mathbf x}_n&\approx\arg\min_{\mathbf x}\Big\{
\|\mathbf x-\mathbf x_n^-\|^2_{(P_n^-)^{-1}}\\
&\qquad+\sum_k\frac{[z_{k,n}-h_k(\mathbf x)]^2}{\sigma_k^2}\Big\}.
\end{aligned}
\tag{7}
\]
</div>

This expression describes the local prior-plus-measurement update. It does not turn a nonlinear likelihood into an exact global posterior or guarantee convergence to the same solution from every initialization.

### 4.2 Forward recursion versus retrospective information

The forward state recursion uses current and earlier measurements. However, the channel scales in this archive are estimated from the complete record. Its forward curves should therefore be understood as **offline-calibrated forward estimates**, not a fully demonstrated self-calibrating real-time system. An operational causal evaluation would freeze calibration from earlier independent data.

The RTS smoother uses future samples to revise earlier states and is explicitly retrospective. Later full-record channel selection and offset estimation also use information beyond an individual sample. These distinctions matter when comparing the curves or describing response latency.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/navigation/workflow.webp' | relative_url }}" alt="Conceptual progression from heterogeneous measurement equations through trajectory inference and channel diagnostics" width="1672" height="941" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Overview of the analysis stages. The timing-reference core uses TOA and TDOA, rather than treating bearing observations as trusted reference measurements. The narrative distinguishes forward recursion, whole-record calibration, and retrospective estimation.</figcaption></figure>

### 4.3 Case 1 results

The saved all-channel filter starts near $(12.99,-33.25,999.46)$ m. Its inferred altitude spans 958.98–1,001.01 m. Recomputed mean and maximum speeds are 18.28 and 34.09 m/s. These are properties of the inferred trajectory, not independently observed motion.

The RMS marginal position standard deviation starts at 15.28 m and reaches 3.92 m at 0.2 s. Over the explicitly selected 2–10 s summary window, its median is 1.319 m and maximum 1.502 m. Median three-dimensional position differences are 18.76 m between filter and pointwise NLS, and 3.69 m between filter and smoother. Neither comparison is an error against truth.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/temporal-estimation.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/navigation/temporal-estimation.svg' | relative_url }}" alt="Saved x, y, and altitude estimates from pointwise fitting, forward filtering, and smoothing, alongside posterior uncertainty scale" width="1186" height="706" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Estimator comparisons and posterior scale. The shaded initial 0.2 s identifies startup. Smoothness and small posterior scale are internal estimation characteristics; neither establishes physical accuracy.</figcaption></figure>

<h2 id="diagnostics">5. Timing-reference diagnostics</h2>

### 5.1 Use a reference while retaining its uncertainty

Case 1 uses its four time-based channels as a diagnostic core. The remaining channels are evaluated against the resulting geometry. This isolates some discrepancies from the all-channel state fit, but it does not make the timing core error-free. Weakly constrained altitude, timing calibration, or source-motion errors can leak into residuals of several other families.

For a trailing residual window, the diagnostic tests the mean relative to an estimated standard error:

<div class="hy-equation">
\[
\lambda_{k,n}=\frac{\overline e_{k,n}}{\widehat{\operatorname{se}}(\overline e_{k,n})},
\qquad |\lambda_{k,n}|\ge3.3.
\tag{8}
\]
</div>

The default window contains 100 samples; three consecutive windows confirm or release a flag. Correlation-adjusted standard errors and separate differential-frequency handling are used rather than assuming all residual samples are independent. The full-record assessment additionally uses block summaries. These are related diagnostics with different time and aggregation conventions.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/reference-residuals.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/navigation/reference-residuals.svg' | relative_url }}" alt="Altitude differences among reference and selected-channel estimates, with baseline standardized post-fit residual means and dispersions" width="1186" height="476" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Changing the reference or channel set changes the inferred altitude. The right panel shows saved baseline standardized post-fit residuals after the first second; its bars are empirical dispersion, not confidence intervals for channel bias.</figcaption></figure>

### 5.2 Transient flags and record-level judgments

The saved whole-record verdict identifies RSSI1, RSSI3, RSSI2, and tan α. The first two have the stronger supporting evidence, while injection tests reveal that reference-state leakage can also flag the latter channels. A threshold crossing therefore identifies disagreement with the selected reference, not a uniquely established physical cause.

<div class="hy-model-table"><table><caption>Table 3. Distinct Case 1 diagnostic outputs from the saved records.</caption><thead><tr><th scope="col">Candidate channel</th><th scope="col">Record-level statistic</th><th scope="col">Record-level flag</th><th scope="col">Flagged time samples</th></tr></thead><tbody>
<tr><td>DFD12</td><td>0.01</td><td>No</td><td>138 / 1,001</td></tr>
<tr><td>tan α</td><td>9.29</td><td>Yes</td><td>809 / 1,001</td></tr>
<tr><td>tan β</td><td>2.68</td><td>No</td><td>434 / 1,001</td></tr>
<tr><td>RSSI1</td><td>33.38</td><td>Yes</td><td>899 / 1,001</td></tr>
<tr><td>RSSI2</td><td>−4.95</td><td>Yes</td><td>358 / 1,001</td></tr>
<tr><td>RSSI3</td><td>258.56</td><td>Yes</td><td>899 / 1,001</td></tr>
</tbody></table></div>

RSSI1 and RSSI3 first trigger trailing-window flags at 1.02 s in the saved calibration setting. DFD12 and tan β still trigger transient flags despite being unflagged in the whole-record verdict. These are not contradictory outputs: a local time test and a persistent record-level assessment answer different questions.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/channel-gating.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size">
<img src="{{ '/assets/img/research/navigation/channel-gating.svg' | relative_url }}" alt="Trailing-window flag heatmap and sample-flag proportions distinguished from full-record channel judgments" width="1186" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 6.</span> Saved sample-level flags. Orange proportion bars indicate a flagged whole-record verdict; teal bars indicate an unflagged one. Neither color labels observed truth about a physical transmitter.</figcaption></figure>

<h2 id="offsets">6. Joint state and offset estimation</h2>

Case 2 uses TOA2, TOA3, and TDOA34 as its timing reference and fits additional persistent offsets. The observation model becomes

<div class="hy-equation">
\[
z_{k,n}=h_k(\mathbf x_n)+b_k+\epsilon_{k,n}.
\tag{9}
\]
</div>

Trajectory fitting and offset updates alternate for three rounds. Channels are retained, corrected, or dropped according to their diagnostic state and residual dispersion. These offsets are fitted relative to the assumed timing core and motion model; they are not external calibrations of actual equipment.

The final DFD12 offset is −16.9226 in the equivalent m/s convention. The two tangent corrections are −0.3493 and +1.5336. RSSI1 and RSSI3 corrections are +9.1895 and −0.6390 dB, while RSSI4 remains uncorrected. Detection statistics and final fitted corrections can differ in sign or magnitude because they are calculated at different reference-state stages.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/case2-offsets.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size">
<img src="{{ '/assets/img/research/navigation/case2-offsets.svg' | relative_url }}" alt="Final fitted Case 2 offsets displayed in separate panels for frequency, tangent, and power units" width="1186" height="447" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 7.</span> Conditional fitted offsets, grouped by unit. A zero correction means the channel was not adjusted under this procedure; it does not prove its true offset is exactly zero.</figcaption></figure>

The resulting inferred altitude spans 835.71–1,006.38 m, with a maximum inferred speed of 169.04 m/s. The source also retains tension between core timing observations and corrected channels. Adding free offsets can improve fit while increasing state–bias ambiguity, especially when the reference geometry weakly identifies altitude. Consequently, small final residual means cannot establish uniquely correct offset recovery.

<h2 id="calibration">7. Synthetic uncertainty calibration</h2>

### 7.1 Define the confidence region before checking coverage

The archive defines a scalar position scale as $s_n=\sqrt{\operatorname{tr}(P_{p,n})/3}$ and scores whether the Euclidean error is at most $1.96s_n$. This borrows a one-dimensional Gaussian multiplier. In three dimensions, it is not generally a 95% region. Even under an isotropic Gaussian with correctly specified covariance, that radius covers approximately **72.09%**, not 95%.

For a full-rank three-dimensional Gaussian covariance, the nominal 95% ellipsoid instead satisfies

<div class="hy-equation">
\[
\begin{aligned}
\mathcal E_n&=\{\mathbf p:\Delta\mathbf p^T P_{p,n}^{-1}\Delta\mathbf p\le7.8147\},\\
\Delta\mathbf p&=\mathbf p-\widehat{\mathbf p}_n.
\end{aligned}
\tag{10}
\]
</div>

The threshold is the 95th percentile of a chi-square distribution with three degrees of freedom. This region accounts for anisotropy and covariance correlations. Its nominal interpretation still depends on covariance calibration and an adequate local Gaussian approximation.

### 7.2 Archived simulations and five new paired checks

The archive contains 50 synthetic trials generated around the saved Case 1 trajectory, with channel-wise Gaussian perturbations. The generating trajectory is an earlier estimate, not external physical truth. Archived position RMSE is 3.6888 ± 0.4775 m; the scalar-radius-rule coverage is 41.64%. The latter is retained as a correctly labeled diagnostic rather than compared directly with a 95% three-dimensional nominal level.

For this revision, five new seeded trials use the same generating-trajectory basis and independently reconstructed forward measurements. Errors are scored from 1 to 10 s. Each trial evaluates both the old scalar rule and the full covariance ellipsoid on the same state errors and covariance matrices.

<div class="hy-model-table"><table><caption>Table 4. Five new synthetic trials with explicitly defined uncertainty regions.</caption><thead><tr><th scope="col">Trial</th><th scope="col">Position RMSE (m)</th><th scope="col">Scalar-radius coverage</th><th scope="col">Nominal 95% ellipsoid coverage</th></tr></thead><tbody>
<tr><td>1</td><td>3.526</td><td>42.51%</td><td>69.03%</td></tr>
<tr><td>2</td><td>3.627</td><td>49.61%</td><td>70.37%</td></tr>
<tr><td>3</td><td>3.780</td><td>49.39%</td><td>72.14%</td></tr>
<tr><td>4</td><td>3.320</td><td>40.73%</td><td>81.13%</td></tr>
<tr><td>5</td><td>2.649</td><td>67.04%</td><td>88.68%</td></tr>
<tr><td>Mean</td><td>3.380</td><td>49.86%</td><td>76.27%</td></tr>
</tbody></table></div>

Correcting the region definition substantially changes the interpretation, yet the properly defined ellipsoids still under-cover in these trials. The small five-trial set is an additional diagnostic, not a replacement estimate for the archived 50-trial distribution or a precise calibration certificate. Successive time errors are correlated, so thousands of scored samples should not be treated as independent repeated experiments.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/synthetic-calibration.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 8 at full size">
<img src="{{ '/assets/img/research/navigation/synthetic-calibration.svg' | relative_url }}" alt="Five new paired scalar-rule and full-ellipsoid coverage checks, alongside an archived bias-recovery example" width="1186" height="457" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 8.</span> Left: new paired region checks, with the 95% reference applying only to the covariance ellipsoid. Right: an archived injection example; different channel units are stated explicitly and are not compared as interchangeable magnitudes.</figcaption></figure>

Undercoverage in these simulations cannot simply be attributed to unknown correlation in the original measurements: the newly generated channel noises are independent by construction. Motion-model mismatch, nonlinear updates, initialization, and covariance approximation remain possible contributors, but these trials do not isolate their respective effects. A universal covariance inflation factor is therefore not inferred from the aggregate coverage alone.

<h2 id="detection">8. Detection versus accurate recovery</h2>

An archived Case 1 injection experiment biases only RSSI1 and RSSI3, yet the diagnostic flags five channels. It detects both injections but adds three false positives: precision is 0.40 and recall 1.00. This illustrates why finding every injected channel does not establish a specific fault classifier.

A separate offset-recovery example correctly identifies the two injected channels DFD12 and RSSI4. However, an injected RSSI4 offset of 8.0 dB is recovered as 7.9707 dB, while an injected DFD12 offset of +3.0 is assessed near −9.4010. The first has absolute recovery error about 0.0293 dB; the second has error −12.4010 in its stated unit. Detection membership is correct, but recovery quality is not uniformly successful.

<div class="hy-model-table"><table><caption>Table 5. Distinct archived synthetic outcomes.</caption><thead><tr><th scope="col">Experiment</th><th scope="col">Observed result</th><th scope="col">Supported interpretation</th></tr></thead><tbody>
<tr><td>Case 1 channel injection</td><td>2 true positives, 3 false positives</td><td>Full recall with limited specificity</td></tr>
<tr><td>Case 2 injection membership</td><td>2 true positives, 0 false positives</td><td>Correct identification in this example</td></tr>
<tr><td>RSSI4 offset recovery</td><td>8.0000 → 7.9707 dB</td><td>Close numerical recovery in this example</td></tr>
<tr><td>DFD12 offset recovery</td><td>+3.0000 → −9.4010</td><td>Large magnitude and sign error despite detection</td></tr>
</tbody></table></div>

The gate-sensitivity experiment aggregates ten seeds for each of twenty threshold/window combinations. Recall remains 1.00, while the best aggregate precision is 0.50. Longer windows or higher thresholds remove some additional flags, but reference-state leakage persists. These aggregate results are separate from the single archived injection example with precision 0.40.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/detection-specificity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 9 at full size">
<img src="{{ '/assets/img/research/navigation/detection-specificity.svg' | relative_url }}" alt="Aggregate detection precision across thresholds and windows, and true versus false positives in a separate injection example" width="1186" height="466" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 9.</span> Detection specificity from two distinct saved tests. A plateau at precision 0.50 is a limitation of the tested diagnostic, not a fully reliable operating region.</figcaption></figure>

<h2 id="sensitivity">9. Assumption sensitivity</h2>

### 9.1 Measurement covariance weighting

Scaling the measurement covariance from 0.5 to 2.0 yields recorded mean position shifts of up to 1.485 m relative to the baseline. This suggests limited response to that particular weighting perturbation. A common state bias or incorrect physical model can remain stable across the entire range, so this experiment cannot establish field accuracy.

### 9.2 Moving-source assumptions

Scaling the velocities of sources 3 and 4 together by −10% to +10% changes the timing-reference trajectory by up to 16.93 m in the saved mean-displacement calculation. The negative endpoint gives 14.45 m and the positive endpoint 16.93 m. This experiment acts on source geometry and uses the timing-core estimator; it is not directly comparable with every all-channel covariance-scale result.

### 9.3 Motion-prior assumptions

A constant-velocity process-scale sweep from 0.1 to 100 gives a maximum sampled mean position shift of 5.29 m relative to $q=5$. A constant-acceleration alternative differs by about 2.31 m under its own parameterization. These shifts describe response to priors, not errors against measured truth or evidence that one model is physically correct.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/assumption-sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 10 at full size">
<img src="{{ '/assets/img/research/navigation/assumption-sensitivity.svg' | relative_url }}" alt="Saved state sensitivity to measurement covariance, moving-source velocities, and motion-model process scale" width="1285" height="428" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 10.</span> Three assumption perturbations with their own recorded estimator and scoring conventions. A small covariance-weight response does not imply small sensitivity to source motion or trajectory priors.</figcaption></figure>

<h2 id="verification">10. Independent checks for this revision</h2>

Raw measurement dimensions and missing values were checked directly. First-difference scales were recomputed and exactly match the saved Case 1 scale vector. An independently vectorized forward model was compared with the archived channel functions at selected states in both cases; the maximum difference is approximately $2.85\times10^{-14}$. Saved state arrays and published workbooks agree to within $4.55\times10^{-13}$ in their numerical fields.

Trajectory ranges, speed norms, uncertainty summaries, estimator differences, sample-flag counts, and final offsets were recomputed from the stored arrays. This also prevents stale narrative summaries from overriding current numerical records. For example, the Case 1 maximum speed presented here is the recomputed 34.09 m/s rather than an older rounded report value.

<div class="hy-model-table"><table><caption>Table 6. Evidence types kept separate in the research note.</caption><thead><tr><th scope="col">Evidence</th><th scope="col">This revision checks</th><th scope="col">It does not establish</th></tr></thead><tbody>
<tr><td>Input and array consistency</td><td>Dimensions, missing values, scales, workbook agreement</td><td>Correct physical calibration</td></tr>
<tr><td>Independent forward equations</td><td>Selected-state agreement across both records</td><td>Uniquely identifiable trajectories</td></tr>
<tr><td>Archived real-record inference</td><td>State summaries, flags, offsets</td><td>Position RMSE without external truth</td></tr>
<tr><td>Archived synthetic experiments</td><td>Metric definitions and saved injection outcomes</td><td>Field performance or universally accurate bias recovery</td></tr>
<tr><td>Five new covariance-region trials</td><td>Proper 3D region definition and paired coverage</td><td>Large-sample calibration or an inflation-factor prescription</td></tr>
</tbody></table></div>

The new trials are deliberately distinct from a complete rerun of every archived sensitivity and diagnostic pipeline. Source documents and numerical records remain unchanged. The updated presentation corrects interpretation and adds reproducible selected checks without implying that all model weaknesses have been repaired.

<h2 id="discussion">11. Discussion</h2>

The strongest methodological contribution is the separation of signal physics, temporal inference, reference-based diagnostics, and uncertainty evaluation. Correct units and signs prevent avoidable numerical errors. Retaining moving-source terms prevents a stationary approximation from being mistaken for calibration. Distinguishing transient flags from persistent verdicts avoids contradictory reliability claims. Evaluating properly defined covariance regions prevents a one-dimensional threshold from becoming a misleading three-dimensional confidence statement.

Several limitations remain substantive. The timing reference is assumed reliable and may weakly identify some state directions. Tangent observations can be ill-conditioned. A received-power law is an assumed model rather than measured propagation truth. Baseline noise scales and persistent offsets use whole-record information, limiting real-time claims. A state–offset fit can hide errors by trading trajectory changes against channel corrections. The synthetic generating trajectory comes from an earlier estimate and does not test every physical failure mechanism.

A next-stage study should use an independent position reference, externally calibrated channel models, and a held-out trajectory set. It should evaluate accuracy, full covariance coverage, coordinate intervals, false positives, detection latency, and offset recovery together. Geometry perturbations and correlated-noise experiments would help isolate causes of undercoverage. Robust weighting or hierarchical bias models could then be assessed against those checks, rather than declared superior from smoother curves alone.

<h2 id="conclusions">12. Conclusions</h2>

Heterogeneous opportunity signals support a coherent computational chain from range and relative motion to trajectory estimates and channel diagnostics. The supplied cases demonstrate that different estimator assumptions can yield different smooth trajectories, and that a flagged channel is not necessarily a uniquely identified physical fault.

The uncertainty audit is equally consequential. The archived scalar-radius coverage is not a three-dimensional 95% confidence-region check. Five newly evaluated covariance-ellipsoid trials correct that definition and still show substantial undercoverage. Combined with false-positive and bias-recovery examples, the evidence supports a careful research account of inference under imperfect assumptions, while leaving physical accuracy and deployment reliability unestablished.

<p class="hy-source-note"><strong>Source and evidence basis.</strong> Supplied measurement tables, physical channel definitions, current saved state arrays and workbooks, sensitivity records, and archived simulation outputs. Eight new quantitative figures, input consistency checks, independent forward-model comparisons, and five covariance-ellipsoid trials were generated for this revision without changing original materials. The cover and overview are conceptual AI-generated images. This page is a computational research note, not a peer-reviewed publication, independently measured navigation benchmark, or validated deployment. No manuscript download is attached at this stage.</p>
