---
layout: han-project
title: Multi-Source Navigation under Uncertain Signals
description:
  A progression from multi-channel position estimation to bias diagnostics, with synthetic checks exposing the difference between confidence
  and accuracy.
permalink: /projects/modeling/navigation/
discipline: Statistical estimation · Sensor fusion
period: 2024 study
question: What can heterogeneous signals reveal about motion when measurement channels can be biased?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Iterated Kalman filtering, timing-based reference estimates, residual analysis, synthetic checks
outcome: Causal estimation · channel diagnostics · explicit uncertainty limits
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: "1. Background: heterogeneous evidence for one trajectory"
    id: background
  - label: 2. Study roadmap
    id: roadmap
  - label: "3. Stage A: normalize and model each channel"
    id: measurement
  - label: "4. Stage B: connect estimates through time"
    id: temporal
  - label: "5. Stage C: distinguish channel bias from weak geometry"
    id: diagnostics
  - label: "6. Stage D: separate state variation from persistent bias"
    id: bias
  - label: "7. Synthetic checks: accuracy and calibration are separate"
    id: validation
  - label: 8. Discussion and evidence boundary
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Position estimation from opportunity signals combines measurements that have different units, geometries, and error mechanisms. This study uses supplied multi-channel records to estimate a moving receiver, examine the uncertainty of those estimates, and distinguish unreliable channels from channels whose geometry is simply weak. It progresses from pointwise nonlinear estimation to causal filtering, offline smoothing, residual-based channel diagnostics, and joint state–bias estimation.

Because the supplied trajectories have no independent ground truth, posterior uncertainty and agreement between estimators cannot be presented as field accuracy. Synthetic tests provide a separate check. In 50 archived simulations, the nominal 95% position region covers truth only about 41.6% of the evaluated samples, despite a mean position RMSE of 3.69 m. That result is central to the presentation: a precise-looking covariance estimate can be substantially overconfident.

<h2 id="background">1. Background: heterogeneous evidence for one trajectory</h2>

The measurement set combines time of arrival, time difference of arrival, differential frequency information, angle of arrival, and received signal strength. Known transmitter positions and velocities supply the reference geometry. Two datasets contain 1,001 time samples over ten seconds, with ten measurement channels per sample.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size">
<img src="{{ '/assets/img/research/navigation/cover.webp' | relative_url }}" alt="Conceptual multi-source positioning environment" width="1647" height="955" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 1.</span> Conceptual multi-source positioning environment. The illustration explains the signal-fusion setting and is not a depiction of the actual transmitter geometry or a demonstrated navigation deployment.</figcaption></figure>

The channels do not offer interchangeable evidence. Timing depends on range, Doppler-related measurements on range rate, bearing on angular geometry, and received power on propagation assumptions. A channel can be informative in one direction and nearly uninformative in another. Simply increasing the number of measurements does not guarantee an observable or well-conditioned position estimate.

The study therefore separates the measurement model, temporal motion prior, and reliability diagnostic. It does not assume that the two supplied cases follow the same physical trajectory, nor that consistency between them supplies missing ground truth.

<h2 id="roadmap">2. Study roadmap</h2>

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/workflow.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size">
<img src="{{ '/assets/img/research/navigation/workflow.webp' | relative_url }}" alt="Overview of estimation, uncertainty, channel diagnostics, and synthetic checks" width="1672" height="941" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 2.</span> Overview of estimation, uncertainty, channel diagnostics, and synthetic checks. The timing-based diagnostic core uses TOA and TDOA channels only; angle measurements are not treated as trusted core evidence. The diagram is explanatory rather than a record of measured accuracy.</figcaption></figure>

<h2 id="measurement">3. Stage A: normalize and model each channel</h2>

For receiver position $\mathbf p$ and transmitter position $\mathbf s_i$, geometric range is the starting point. Arrival-time differences compare two ranges and remove a shared timing reference under the stated synchronization assumptions.

<div class="hy-equation">
\[
d_i=\|\mathbf p-\mathbf s_i\|,\qquad z_i^{\mathrm{TOA}}=\frac{d_i}{c},\qquad z_{ij}^{\mathrm{TDOA}}=\frac{d_i-d_j}{c}.
\tag{1}
\]
</div>

Timing residuals are converted into distance units before weighting. Range-rate differences describe the corresponding differential-frequency observation; bearing residuals require angular wrapping; received power uses an assumed range-dependent attenuation relationship. Each residual must be scaled by its own uncertainty, rather than summed in raw incompatible units.

<div class="hy-equation">
\[
Q(\mathbf x)=\sum_k\frac{[z_k-h_k(\mathbf x)]^2}{\sigma_k^2}.
\tag{2}
\]
</div>

The weighting model is a substantive assumption. If channel errors are correlated, biased, or non-Gaussian, diagonal variance weights may overstate information. Near-coplanar source geometry can also leave the vertical direction weakly constrained even when horizontal coordinates appear stable.

<h2 id="temporal">4. Stage B: connect estimates through time</h2>

Pointwise nonlinear least squares provides a reference with no trajectory prior. A six-dimensional position–velocity state then uses a constant-velocity transition and an iterated extended Kalman filter. The filter combines the current measurements with the state predicted from preceding samples:

<div class="hy-equation">
\[
\mathbf p_{t+1}=\mathbf p_t+\mathbf v_t\Delta t,\qquad \mathbf v_{t+1}=\mathbf v_t+\mathbf w_t.
\tag{3}
\]
</div>

The transition does not assert that physical acceleration is exactly zero. Process noise permits departures from constant velocity; its magnitude controls how much the estimator smooths those departures. Iteration updates the local measurement linearization at each observation.

An RTS smoother adds future observations to refine earlier states. This is an offline result, whereas the forward filter is causal. It should not be described as an equivalent real-time estimator. The saved median difference from pointwise estimates is about 18.8 m for the filtering comparison and 3.7 m for the smoothing comparison; neither is an error against observed truth.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/estimation.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size">
<img src="{{ '/assets/img/research/navigation/estimation.svg' | relative_url }}" alt="Archived altitude estimates from pointwise nonlinear least squares, causal filtering, and offline smoothing, with posterior position uncertainty shown separately" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 3.</span> Archived altitude estimates from pointwise nonlinear least squares, causal filtering, and offline smoothing, with posterior position uncertainty shown separately. Differences among curves are not ground-truth errors.</figcaption></figure>

The posterior standard deviation falls after initialization, with saved post-warmup summaries around 1.32 m median and 1.5 m maximum. These describe the estimator's own uncertainty model. They cannot support a claim of meter-level physical accuracy without an independent reference trajectory.

<h2 id="diagnostics">5. Stage C: distinguish channel bias from weak geometry</h2>

A time-channel reference core is used to examine candidate channels through residual means, autocorrelation, and uncertainty adjustments. A persistent residual can suggest bias, but it may also arise from a weakly identified state component. In particular, a vertical-state error can leak into angle and power residuals.

The archived diagnostic identifies strong discrepancies in two received-power channels, while some angle and other power flags are less specific. This is why the page distinguishes a suspect-channel list from proof that every listed channel is physically biased. The reference core itself also depends on timing assumptions and source geometry.

Window averages require care because filtered residuals are temporally correlated. Treating 1,001 samples as 1,001 independent pieces of evidence can produce unrealistically small standard errors. The project accounts for correlation in the diagnostic calculation, but the synthetic precision results below still reveal false alarms.

<h2 id="bias">6. Stage D: separate state variation from persistent bias</h2>

The extended analysis introduces persistent channel offsets alongside the moving state and alternates between trajectory and bias estimation. A random fluctuation should not be handled identically to a constant offset: the former affects dispersion, while the latter can displace an otherwise smooth estimate.

However, adding bias parameters increases the identifiability burden. Several combinations of position and measurement offsets can produce similar residuals under weak geometry. Good fit is therefore insufficient evidence of correct bias recovery.

The saved synthetic case correctly identifies two affected channels, but recovery quality differs. A received-power offset of 8 is recovered near 7.97; a frequency-channel offset of 3 is estimated near −9.40. Detecting that a channel is affected is plainly different from accurately recovering its offset. The latter discrepancy is retained rather than summarized as a uniformly successful bias-estimation experiment.

<h2 id="validation">7. Synthetic checks: accuracy and calibration are separate</h2>

Synthetic tests create known trajectories and injected errors so the estimation pipeline can be evaluated against truth. They are controlled self-consistency experiments within the chosen data-generating assumptions, not substitutes for an independent field dataset.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/validation.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size">
<img src="{{ '/assets/img/research/navigation/validation.svg' | relative_url }}" alt="Archived synthetic results: nominal interval coverage versus measured coverage, and precision versus recall in injected-bias detection" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 4.</span> Archived synthetic results: nominal interval coverage versus measured coverage, and precision versus recall in injected-bias detection. The test identifies all injected biased channels but also flags unaffected ones.</figcaption></figure>

<div class="hy-model-table"><table><caption>Different diagnostics answer different questions; no single score establishes reliability.</caption><thead><tr><th scope="col">Check</th><th scope="col">Archived result</th><th scope="col">Interpretation</th></tr></thead><tbody><tr><td>Position RMSE, 50 runs</td><td>3.69 ± 0.48 m</td><td>Synthetic error, not observed field accuracy</td></tr><tr><td>Nominal 95% region coverage</td><td>41.64%</td><td>Substantial undercoverage</td></tr><tr><td>Bias detection precision / recall</td><td>0.40 / 1.00</td><td>All injected channels found, with false positives</td></tr></tbody></table></div>

The coverage result is particularly important. Low average RMSE does not guarantee that confidence regions are calibrated. If uncertainty is used to decide whether an estimate is trustworthy, undercoverage can matter as much as the point estimate itself.

<figure class="hy-research-figure hy-model-figure">
<a class="hy-model-zoom" href="{{ '/assets/img/research/navigation/sensitivity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size">
<img src="{{ '/assets/img/research/navigation/sensitivity.svg' | relative_url }}" alt="Saved sensitivity of position estimates to measurement-covariance scaling" width="720" height="418" loading="lazy">
<span class="hy-model-zoom-label">View full size ↗</span></a>
<figcaption><span>Figure 5.</span> Saved sensitivity of position estimates to measurement-covariance scaling. Stability under this perturbation is an internal diagnostic, not evidence that the common estimate is correct.</figcaption></figure>

The covariance-scale comparison changes positions by at most about 1.5 m in the saved range. A stable estimator may still share a systematic modeling error across every setting. Sensitivity should therefore complement, not replace, truth-based validation.

<h2 id="discussion">8. Discussion and evidence boundary</h2>

The study provides a transparent chain from measurement equations to motion estimation and channel diagnostics. Its strongest lesson is that three claims must remain distinct: the trajectory is smooth, the estimator reports small uncertainty, and the physical position is accurate. Only the last requires an independent truth reference.

The current source records contain no such reference for the supplied measurements. Synthetic simulations establish limited behavior under specified assumptions and also expose shortcomings: overconfident uncertainty, false-positive channel flags, and an unrecovered frequency bias. These findings motivate a calibrated noise model and a stronger identifiability analysis rather than a deployment claim.

A next-stage evaluation would use independent position truth, test realistic synchronization and propagation departures, and report accuracy together with interval coverage and false alarms. The present page is a research account of sensor fusion and its diagnostic limits.

<p class="hy-source-note">Source basis: the supplied project manuscript, saved numerical outputs, and analysis scripts. This page summarizes archived calculations; it does not represent a new full model run, a peer-reviewed publication, or independent field validation. Cover and workflow illustrations are AI-generated; quantitative plots are redrawn from saved numerical records. No manuscript download is attached at this stage.</p>
