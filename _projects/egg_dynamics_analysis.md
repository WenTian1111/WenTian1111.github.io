---
layout: han-project
title: Egg Rolling Analysis & Risk Sorting
description: An undergraduate thesis and provincial innovation project connecting egg morphology, rolling experiments, interpretable risk grading, and an interactive prediction application.
img: assets/img/projects/egg/experiment_platform.png
importance: 1
category: research
discipline: Machine vision
period: 2025–2026
question: Can a still image of an egg help anticipate its rolling instability?
role: Thesis author and innovation-project lead
methods: Controlled experiments, machine vision, statistical analysis, machine learning
outcome: Undergraduate thesis, provincial-level innovation & entrepreneurship training project, risk-grading framework, and companion web application
card_summary: A study of 90 eggs and 270 repeated rolling trials, linking visual morphology to instability and translating the analysis into an interactive application.
image_alt: Illustration of the paired static-imaging and inclined rolling experiment platforms
demo: https://egg-rsi-app.streamlit.app
source_code: https://github.com/WenTian1111/egg-rsi-app
contents:
  - label: Abstract
    id: abstract
  - label: Question & contribution
    id: question
  - label: Experimental design
    id: experiment
  - label: Image measurement
    id: measurement
  - label: Motion descriptors
    id: motion
  - label: Shape–motion coupling
    id: coupling
  - label: RSI construction
    id: risk
  - label: Prediction & errors
    id: results
  - label: Application
    id: application
  - label: Discussion & next steps
    id: limitations
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

Can the outline of an egg help anticipate how it will roll? This study connects **static visual morphology** with **measured rolling behavior** through a paired experiment involving 90 eggs and 270 repeated rolling trials. A controlled imaging pipeline extracts shape descriptors; video tracking summarizes centroid displacement, orientation variation, and speed irregularity. The analysis finds that asymmetry and selected higher-order contour moments carry information about motion that simple size descriptors do not capture well in this batch. A principal-component-based Rolling Stability Index (RSI) converts the dynamic measurements into three relative risk grades. Four classifiers then predict those grades from static morphology. The final thesis reports a best accuracy of **74.07%** and macro F1 of **81.64%** for the support vector machine. The work culminates in an interactive image-analysis application. Its contribution is a connected measurement–analysis–prediction workflow; the reported evaluation concerns repeated trial records under one experimental setup, with specimen-independent and damage-based validation remaining open.

<h2 id="question">1. The question: from visible shape to motion</h2>

A photograph describes the geometry of an egg at rest. Handling and transport expose a different set of properties: how the egg changes orientation, whether its path shifts, and how evenly it moves. The central question is whether the first kind of information can help explain and anticipate the second.

The study therefore treats morphology as more than a length-to-width ratio. Two eggs with similar overall proportions may differ in end fullness, outline asymmetry, and the distribution of their contour. Those differences provide a plausible route from shape to contact behavior, but the route needs to be examined through paired measurements rather than inferred from appearance alone.

I developed the research through my undergraduate thesis, _Coupling Analysis of Static-Dynamic Characteristics and Sorting Research of Eggs Based on Machine Vision_, and a Chongqing municipal-level innovation training project. Under academic supervision, I built the experimental setup, collected and processed the images and videos, developed the feature-extraction and analysis pipelines, compared prediction models, and implemented the companion application. The innovation project ran from July 2025 to May 2026; the thesis was defended in May 2026. Both records describe the same experimental series.

The research proceeds through four linked tasks: establish a paired dataset; check the image measurement; identify shape–motion associations and construct a dynamic index; then examine how far static features can predict the resulting grades. This sequence keeps the experimental observation separate from the proposed physical explanation and the subsequent classifier.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/study-design.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 1 at full size">
    <img src="{{ '/assets/img/research/egg-study/study-design.svg' | relative_url }}" alt="Data flow showing 90 static records joined to 270 rolling trials by EggID" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 1.</span> Paired study design. Dynamic measurements define the RSI target; static morphology supplies the prediction inputs.</figcaption>
</figure>

<h2 id="experiment">2. A paired static–dynamic experiment</h2>

The experimental material consisted of **90 intact, cleaned eggs from one batch**. Each egg received a specimen identifier, one standardized static image, and three rolling trials. The dataset therefore contains 90 physical specimens and 270 trial records. The repetitions capture variation in motion for the same shape; they do not create additional independent eggs.

Static acquisition used fixed viewing geometry and controlled illumination against a contrasting background. Dynamic acquisition used a rolling surface inclined at **2.87°**, with a blue flexible towel providing both segmentation contrast and a consistent contact interface. Release position, inclination, surface, lighting, and camera arrangement were controlled so that the analysis could focus on variation between eggs within this setting.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/projects/egg/experiment_platform.png' | relative_url }}" target="_blank" rel="noopener" aria-label="View experimental platform at full size">
    <img src="{{ '/assets/img/projects/egg/experiment_platform.png' | relative_url }}" alt="Schematic of the paired static-imaging platform and 2.87-degree inclined rolling platform" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 2.</span> Experimental platform schematic reproduced from the thesis. It illustrates the acquisition arrangement; it is not a photograph of a production sorting line.</figcaption>
</figure>

The static database stores one feature record per egg. Video processing produces frame-level centroid, orientation, and speed records, which are summarized into one row per trial. Joining the two databases by **EggID** creates a one-to-three structure: one static description is associated with three independently recorded rolling responses. The archived fusion workbook contains 270 matched rows, 90 unique egg identifiers, and no unmatched specimens.

This organization is important for both interpretation and evaluation. Between-egg variation describes morphology; within-egg variation describes repeatability of the rolling response. A model trained on individual rows can encounter the same egg's static vector more than once, so row-level separation alone does not establish generalization to unseen specimens.

<h2 id="measurement">3. Making shape measurable</h2>

<h3>Segmentation and contour extraction</h3>

The thesis pipeline begins with brightness correction and suppression of misleading highlights. It then uses the blue background's color contrast in HSV space to isolate the egg. Morphological opening, closing, hole filling, and connected-component selection remove scattered noise and repair the candidate mask. The retained contour is smoothed and resampled before extracting descriptors that are sensitive to boundary detail.

This ordering matters: a small segmentation defect may have little effect on overall area but a much larger effect on higher-order moments. Showing the mask and contour alongside the measurements makes the source of each feature inspectable.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/static-measurement.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 3 at full size">
    <img src="{{ '/assets/img/research/egg-study/static-measurement.webp' | relative_url }}" alt="Four processing stages for one study egg: original photograph, grayscale image, binary mask, and contour with centroid" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 3.</span> Static image measurement, using the original panels from thesis Figure 2.3 with English stage labels.</figcaption>
</figure>

<h3>Complementary feature families</h3>

The feature set combines gross dimensions with outline structure. For fitted major- and minor-axis lengths $L$ and $B$, the egg shape index and eccentricity are:

<div class="hy-equation">
\[
\begin{aligned}
\mathrm{ESI}&=100\,\frac{B}{L},\\
e&=\sqrt{1-\left(\frac{B}{L}\right)^2}.
\end{aligned} \tag{1}
\]
</div>

ESI is expressed as a percentage here; some source tables store the equivalent ratio on a 0–1 scale. Keeping that convention explicit avoids a hundredfold mismatch when moving between tables and application inputs.

<div class="hy-model-table">
<table>
<caption>Static descriptor families and their purpose</caption>
<thead><tr><th>Family</th><th>Examples</th><th>Information represented</th></tr></thead>
<tbody>
<tr><td>Dimensions</td><td>Area, perimeter, major and minor axes, equivalent diameter</td><td>Overall size in the acquisition image</td></tr>
<tr><td>Global proportions</td><td>ESI, eccentricity, circularity</td><td>Elongation and departure from a circular outline</td></tr>
<tr><td>Boundary occupancy</td><td>Solidity and extent</td><td>How the mask fills its convex hull and bounding region</td></tr>
<tr><td>Asymmetry and offset</td><td>Asymmetry descriptor, major-axis offset ratio</td><td>Uneven distribution of the silhouette</td></tr>
<tr><td>Higher-order structure</td><td>Hu1–Hu7</td><td>Moment-based information beyond basic dimensions</td></tr>
</tbody></table>
</div>

The companion application's saved schema contains 19 static features. The thesis also discusses a centroid-based interpretation of asymmetry. The archived extraction code and the application use implementation-specific area-balance and offset calculations; these definitions must be aligned before treating the application as an exact implementation of the manuscript. A silhouette centroid is a geometric quantity, not a measured physical center of mass.

<h3>Measurement agreement with calipers</h3>

Before relating shape to motion, I compared vision-derived ESI with manual caliper measurements for the same 90 eggs. Absolute relative error was calculated as:

<div class="hy-equation">
\[
\varepsilon_i=\frac{|\mathrm{ESI}_{v,i}-\mathrm{ESI}_{m,i}|}
{\mathrm{ESI}_{m,i}}\times100\%. \tag{2}
\]
</div>

The paired measurements give a **mean absolute relative error of 0.788%** and a **maximum of 3.108%**. The figure below is redrawn from the archived validation workbook. This check supports the ESI measurement under the study's acquisition conditions; it does not validate every contour descriptor or arbitrary photographs taken at different scales and viewpoints.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/esi-agreement.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 4 at full size">
    <img src="{{ '/assets/img/research/egg-study/esi-agreement.svg' | relative_url }}" alt="Scatter plot of caliper versus vision ESI and histogram of relative errors for 90 eggs" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 4.</span> Agreement with manual caliper measurement. Replotted from the 90 paired records in the ESI validation workbook.</figcaption>
</figure>

<h2 id="motion">4. Describing each rolling trial</h2>

Each video is segmented frame by frame. Image moments locate the egg's centroid, while the major-axis direction of the fitted silhouette describes its orientation. Successive centroids provide displacement and image-space speed:

<div class="hy-equation">
\[
v_t=\frac{\sqrt{(x_t-x_{t-1})^2+(y_t-y_{t-1})^2}}{\Delta t}. \tag{3}
\]
</div>

The analysis summarizes three aspects of the motion. **Signed Y displacement**, $\Delta Y=y_T-y_1$, records the change in the image's transverse coordinate. **Orientation variance**, $\operatorname{Var}(\theta)$, describes variation in the major-axis angle over the sequence. **Speed coefficient of variation**, $\mathrm{CV}_v=s_v/\bar v$, measures speed irregularity relative to the trial's mean speed. The thesis describes temporal smoothing of orientation and speed to reduce tracking noise and artifacts amplified by differencing.

These quantities answer different questions. Endpoint displacement does not describe every local bend in a trajectory; orientation variance does not measure lateral deviation; and speed CV summarizes rhythm rather than absolute velocity. In the archived outputs, displacement is in pixels and orientation is in degrees. The signed Y coordinate should not be silently converted into millimetres, an absolute deviation magnitude, or a calibrated conveyor error.

The mean speed CV is approximately **0.201**, with a between-trial standard deviation of **0.111**. The three outcomes are not interchangeable: orientation variance is negatively associated with both signed Y displacement and speed CV in this dataset, while the latter two have little linear association with one another. This motivates examining their joint structure instead of declaring every larger measurement to be uniformly worse.

<h2 id="coupling">5. What connects morphology and motion?</h2>

<h3>Size alone explains little of the observed variation</h3>

The static measurements vary unevenly within this batch. Major-axis length has a coefficient of variation of about 0.374%, whereas the asymmetry descriptor varies by approximately 33.2%. Selected higher-order moments vary more strongly still. These differences explain why a narrowly distributed size measure may carry less information here than a descriptor of outline structure; they do not establish that size is irrelevant across breeds or batches.

Pearson analysis identifies several moderate associations with speed irregularity. **Hu3 has $r=0.497$ with speed CV**, and the **asymmetry descriptor has $r=0.476$**. Hu4, Hu6, and Hu5 also show positive associations. The corresponding linear relationships for basic axis lengths and ESI are weak in this dataset. The comparisons concern repeated trial records; their inferential uncertainty should be reassessed with the egg-level dependence accounted for.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/shape-motion.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 5 at full size">
    <img src="{{ '/assets/img/research/egg-study/shape-motion.svg' | relative_url }}" alt="Selected correlations with speed CV and mean speed CV across asymmetry thirds" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 5.</span> Selected shape–motion associations. Values come from the archived correlation and one-factor analysis tables; the observations are repeated trials.</figcaption>
</figure>

<h3>Asymmetry changes the pattern of the response</h3>

Grouping the asymmetry descriptor into lower, middle, and upper thirds gives mean speed CV values of **0.155, 0.175, and 0.272**, respectively. Each third represents 30 eggs and their 90 trials. The archived one-factor analysis attributes an effect size of approximately $\eta^2=0.215$ to the grouping for speed CV. Meanwhile, mean orientation variance decreases across these thirds rather than increasing.

Two-factor analyses combine asymmetry with ESI or eccentricity. The archived tables show interaction effects for displacement and speed CV, with smaller interaction effect sizes than the principal asymmetry effect on speed regularity. This is evidence of a more complicated statistical relationship than a single proportional rule. It is not a direct measurement of contact force or an experimentally isolated causal interaction.

<h3>A physical interpretation to test</h3>

The proposed explanation links uneven end geometry and local contour structure to changes in contact-point migration and effective rolling radius. Those changes could alter the motion's rhythm and favor a biased orientation pattern. This interpretation is consistent with the observed associations, including the combination of greater speed irregularity and lower orientation variance.

The experiment did not directly measure contact-point trajectories, forces, mass distribution, or shell damage. The mechanism therefore remains a hypothesis supported by the shape–motion analysis. Direct contact imaging or a validated mechanical model would be needed to test the intermediate steps.

<h2 id="risk">6. Constructing a study-specific Rolling Stability Index</h2>

<h3>Standardization and principal components</h3>

The three dynamic outcomes have different units and spreads. Each is standardized before PCA using $z_{ij}=(d_{ij}-\mu_j)/s_j$. The first component explains **47.531%** of the standardized variance; the second explains **34.220%**, giving **81.751% cumulatively**. The third retains the remaining 18.249%.

The final thesis defines the raw RSI from **PC1 alone**, using the following sign convention:

<div class="hy-equation">
\[
\begin{aligned}
q_i={}&0.510424\,z_{\Delta Y,i}\\
&-0.717726\,z_{\operatorname{Var}(\theta),i}\\
&+0.473641\,z_{\mathrm{CV}_v,i}.
\end{aligned} \tag{4}
\]
</div>

It then rescales the score within the experimental dataset:

<div class="hy-equation">
\[
\mathrm{RSI}_i=100\,\frac{q_i-q_{\min}}{q_{\max}-q_{\min}}. \tag{5}
\]
</div>

Higher RSI corresponds to greater signed Y displacement and speed irregularity together with lower orientation variance in this fitted direction. It is a relative motion-based index. It is not a probability of breakage, a shell-strength measurement, or an absolute egg-quality grade. Because its endpoints come from the observed sample, the 0–100 scale is tied to this study's distribution.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/rsi-construction.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 6 at full size">
    <img src="{{ '/assets/img/research/egg-study/rsi-construction.svg' | relative_url }}" alt="PC1 loadings and distribution of the three RSI grades" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 6.</span> RSI construction and grade distribution. PC1 is the raw score, rescaled to 0–100; cumulative two-component variance is reported separately.</figcaption>
</figure>

<h3>From continuous scores to three grades</h3>

K-means clustering of the one-dimensional RSI scores produces three groups, ordered by their centers. The observed grade composition is strongly imbalanced:

<div class="hy-model-table">
<table>
<caption>RSI groups in the 270 recorded trials; ranges describe observed scores, not universal thresholds</caption>
<thead><tr><th>Relative grade</th><th>Trials</th><th>Mean RSI</th><th>Observed range</th></tr></thead>
<tbody><tr><td>Lower</td><td>12</td><td>29.760</td><td>0–46.637</td></tr>
<tr><td>Middle</td><td>127</td><td>70.482</td><td>55.832–78.990</td></tr>
<tr><td>Higher</td><td>131</td><td>87.936</td><td>79.447–100</td></tr></tbody>
</table></div>

The group profiles clarify the meaning of the score. Mean speed CV rises from about 0.100 to 0.141 to 0.268 across the three grades, while mean orientation variance falls from approximately 3,228 to 1,834 to 1,109 degrees squared. Lower-RSI trials have much smaller mean signed Y displacement than the other groups. These separations show how the index organizes its input measurements; because the grades are constructed from those same measurements, the separation is an internal consistency check rather than independent validation of real-world damage risk.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/risk-profiles.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 7 at full size">
    <img src="{{ '/assets/img/research/egg-study/risk-profiles.svg' | relative_url }}" alt="Distributions of signed displacement, orientation variance, and speed CV by RSI grade" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 7.</span> Dynamic profiles of the data-derived grades. Replotted from the archived RSI workbook; separation is an internal consistency check.</figcaption>
</figure>

Repeated motion also matters: a check of the archived RSI table finds that **32 of the 90 eggs receive more than one grade across their three trials**. The same static shape can therefore lead to different trial outcomes. A future egg-level target could summarize repeated responses or predict their distribution, instead of treating the grade of one roll as an immutable property of the specimen.

<h2 id="results">7. Predicting the grade from a still image</h2>

<h3>Training and reported evaluation</h3>

The prediction task maps static morphology to the dynamic RSI grade. The final thesis describes an **80:20 stratified trial-level split**, with 216 training and 54 test records. Five-fold cross-validation within the training portion is used for hyperparameter selection, primarily on macro F1.

The four model families provide complementary comparisons: regularized logistic regression as a linear baseline; a radial-basis-function support vector machine for nonlinear boundaries; a bagged tree ensemble reported as random forest; and a one-versus-rest LogitBoost tree ensemble reported as GBDT. Their manuscript implementations and tuning ranges differ from those in the Python demonstration application.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/model-benchmark.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 8 at full size">
    <img src="{{ '/assets/img/research/egg-study/model-benchmark.svg' | relative_url }}" alt="Reported accuracy, macro F1, and macro AUC for LR, SVM, RF and GBDT" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 8.</span> Final-thesis Table 2.15, redrawn with a common 0–100% scale. These are reported trial-level scores.</figcaption>
</figure>

<div class="hy-model-table">
<table>
<caption>Reported final-thesis benchmark, Table 2.15; all values are percentages</caption>
<thead><tr><th>Model</th><th>Accuracy</th><th>Macro precision</th><th>Macro recall</th><th>Macro F1</th><th>Macro AUC</th></tr></thead>
<tbody><tr><td>LR</td><td>59.26</td><td>63.59</td><td>71.13</td><td>66.57</td><td>79.67</td></tr>
<tr><td>SVM</td><td><strong>74.07</strong></td><td>82.08</td><td>81.79</td><td><strong>81.64</strong></td><td>85.85</td></tr>
<tr><td>RF</td><td>72.22</td><td>80.59</td><td>80.46</td><td>80.36</td><td>86.19</td></tr>
<tr><td>GBDT</td><td>72.22</td><td>80.59</td><td>80.46</td><td>80.36</td><td><strong>86.65</strong></td></tr></tbody>
</table></div>

**SVM leads on accuracy and macro F1; GBDT leads on macro AUC.** Accuracy measures the fraction of correct labels. Macro F1 gives equal weight to each class's precision–recall balance, and macro AUC assesses one-versus-rest score ranking. These answer different questions, especially when the smallest class contributes few test records.

These values are the final manuscript's reported results, not a new training run. Earlier MATLAB exports, the saved application models, and some archived AUC outputs differ. They are kept as separate versions rather than pooled into a single benchmark. Exact computational reproduction requires reconciling the manuscript with the matching model, split, preprocessing, and score export.

<h3>Where the SVM still makes mistakes</h3>

The SVM classifies **40 of 54** test records correctly. All three lower-RSI records are correct, as are 20 of 25 middle-RSI and 17 of 26 higher-RSI records. Five middle-grade trials move upward to the higher grade, while nine higher-grade trials move downward to the middle grade. The remaining errors therefore concentrate at the middle–higher boundary.

<figure class="hy-research-figure">
  <a class="hy-model-zoom" href="{{ '/assets/img/research/egg-study/svm-errors.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="View Figure 9 at full size">
    <img src="{{ '/assets/img/research/egg-study/svm-errors.svg' | relative_url }}" alt="SVM confusion matrix with class supports 3, 25, and 26, and recalls 100%, 80%, and 65.38%" loading="lazy">
    <span class="hy-model-zoom-label">View full-size figure ↗</span>
  </a>
  <figcaption><span>Figure 9.</span> SVM errors and class-specific recall, redrawn from thesis Figure 2.18 and Table 2.16. The smaller grade has only three test records.</figcaption>
</figure>

Higher-grade recall is **65.38%**, and higher-grade precision is **77.27%**. This class-specific view is more informative for a proposed handling decision than an aggregate score alone. The 100% recall for the lower grade rests on only three observations and should not be interpreted as reliable identification of all low-risk eggs.

Tree-model feature rankings provide a complementary perspective. The final thesis places the asymmetry descriptor and major-axis length among the leading random-forest predictors, while GBDT assigns its largest reported importance to major-axis length, followed by asymmetry and Hu3. A feature can be weakly associated with motion on its own and still help a nonlinear classifier in combination with others. These rankings are model-dependent, are not causal attribution, and do not explain the SVM's internal decisions.

<h2 id="application">8. Translating the workflow into an application</h2>

**Egg_RSI_App** connects the experimental analysis with an inspectable interface. Its dataset view lets a user explore example eggs and their descriptors. Its upload pathway shows the original image, grayscale view, segmentation mask, and extracted contour, then reports a static feature vector and a selected model's predicted risk class and probabilities.

The code includes OpenCV-based segmentation and alternative strategies for difficult backgrounds. The intended research workflow is to inspect the extracted shape before interpreting the prediction: a plausible-looking class output cannot compensate for an incorrect mask or a photograph far outside the acquisition conditions.

The application is a research demonstration with its own saved model artifacts and feature definitions. In particular, asymmetry calculation and image-scale-dependent dimensions need to be harmonized with the experimental pipeline before a new photograph can be regarded as a comparable measurement. Model probabilities are classifier outputs, not calibrated probabilities of damage.

[Open the application](https://egg-rsi-app.streamlit.app) · [Explore the public code](https://github.com/WenTian1111/egg-rsi-app)

One proposed use is differentiated handling: routine transport for relatively stable motion profiles, gentler acceleration or additional cushioning for intermediate profiles, and review or a separate handling path for higher-risk profiles. These are engineering proposals. The study did not implement and measure a production controller, demonstrate reduced breakage, or establish economic savings.

<h2 id="limitations">9. Discussion and the next experiment</h2>

The project contributes a paired experimental database, a transparent route from image masks to descriptors, a statistical account of shape–motion relationships, and a prototype that exposes the measurement stages. Its strongest evidence concerns what can be observed and associated under the controlled experiment. Extending it to dependable sorting requires several further tests.

**Hold out physical eggs and batches.** The reported split separates trial records, while each specimen contributes three identical static descriptions. Future evaluation should keep all trials of a given egg together and reserve entirely new batches. Correlation and group comparisons should likewise account for repeated measurements rather than relying on 270 independent specimens.

**Fix the complete pipeline before testing.** Segmentation, descriptor definitions, scaling, PCA direction and endpoints, risk-grade construction, and model selection must be specified together. Learned preprocessing should be fitted using development data, then frozen for the held-out evaluation. A clean classifier split does not by itself remove information used earlier in global label construction.

**Broaden conditions and check repeatability.** The current data come from one batch, one 2.87° inclination, one contact surface, and one acquisition arrangement. New lighting, camera distance, egg varieties, release orientations, surfaces, and transport speeds could change both the extracted features and the dynamics. Repeated trials should establish whether a specimen-level profile is stable enough to support a decision.

**Validate the engineering outcome.** A rolling index must be related to calibrated path deviation, allowable handling constraints, and directly observed damage before it can support claims about breakage reduction. Contact measurements would also test the proposed mechanism, rather than relying on correlations to establish the intervening physical processes.

**Preserve version traceability.** The manuscript benchmark and demonstration models should be tied to explicit data, preprocessing, split, and software versions. Reconciling the existing archives is the next reproducibility step; adding a more complex model without doing so would not resolve the present uncertainty.

The practical next study is a multi-batch, multi-condition experiment with specimen-level holdouts, a frozen image-to-prediction pipeline, repeated-response targets, and direct measurements of handling outcomes. That design would test whether the observed relation between silhouette structure and motion remains useful beyond this particular setup.

<h2 id="record">Research record</h2>

This account is based on the archived final undergraduate thesis, the related 2026 innovation-project research and completion materials, the measurement and statistical workbooks, and the companion application's local source and saved-result records. The original thesis and administrative documents are retained locally. The figures on this page reproduce research illustrations or redraw archived measurements; the web update does not introduce a new classifier training experiment.

<p class="hy-source-note">Principal evidence: thesis Tables 2.5, 2.8–2.17 and Figures 2.2–2.3, 2.18; archived ESI validation, static–dynamic coupling, and RSI workbooks. All 270 rolling records belong to 90 physical eggs. The thesis and innovation report are linked outputs of one experimental series.</p>
