---
layout: han-project
title: Geometric Simulation & Evidence Discipline
description: A non-operational methodological study of computational evidence, including a fresh archive-integrity audit, independent benign numerical
  examples and explicit limits of model validation.
permalink: /projects/modeling/constrained-simulation/
discipline: Numerical research · Verification practice
period: 2025 study
question: How can a simulation research artifact distinguish reproducible calculations from validated claims about the world?
role: AI-assisted modeling, numerical analysis, and research synthesis
methods: Evidence contracts, provenance auditing, independent reference calculations, refinement and conditional uncertainty analysis
outcome: 36 hash-linked artifacts checked · benign numerical demonstrations · a transparent evidence ledger
parent_url: /projects/math_modeling_series/
parent_label: All modeling studies
contents:
  - label: Abstract
    id: abstract
  - label: 1. Research question and scope
    id: introduction
  - label: 2. Archived evidence and versions
    id: archive
  - label: 3. An explicit evidence contract
    id: assumptions
  - label: 4. Comparable references
    id: baselines
  - label: 5. Independent verification
    id: checks
  - label: 6. A benign exact-reference experiment
    id: convergence
  - label: 7. Conditional uncertainty
    id: sensitivity
  - label: 8. Review automated diagnostics
    id: diagnostics
  - label: 9. Trace claims through artifacts
    id: reproducibility
  - label: 10. Checks completed in this revision
    id: verification
  - label: 11. Discussion and conclusions
    id: discussion
---

<link rel="stylesheet" href="{{ '/assets/css/modeling-notes.css' | relative_url }}">

<h2 id="abstract">Abstract</h2>

A simulation can be internally consistent, reproducible and carefully formatted while remaining unvalidated outside its assumptions. This methodological note examines that distinction through an archived 2025 geometric-simulation research package. The public presentation concerns documentation, reference comparisons, independent checks, uncertainty interpretation and provenance. It does not reproduce operational decision procedures, deployment settings or strategy diagrams from the source scenario.

A fresh audit recalculates hashes for all 36 manifest-linked artifacts: eleven source files, three inputs, ten result records, eleven figures and one manuscript. Every hash matches and all files are present. That establishes version agreement with the saved manifest, not a new scientific acceptance test. Two separately constructed, benign examples then show what independent numerical verification and conditional noise propagation can establish. A unit-semicircle integration experiment exposes refinement behavior against an exact reference, while a dimensionless scale-noise experiment illustrates that Monte Carlo distributions inherit their input assumptions. The note concludes with an evidence ledger that separates archived review, checks performed for this revision and further validation that remains necessary.

<h2 id="introduction">1. Research question and scope</h2>

A numerical research project begins by deciding which features of a setting become state variables, fixed inputs, constraints or omissions. That decision makes a question calculable. It also limits the claim a result can support. A solver returns a value for the encoded problem; it does not independently establish that the encoded problem is an adequate description of an observed system.

The source package is useful here because it contains more than a polished manuscript. It includes implementation files, stored outputs, figure sources, a version manifest and a review report that records corrections. The publication task is therefore not simply to restyle its conclusion, but to show how the supporting evidence is organized and where its scope ends.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/cover.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 1 at full size"><img src="{{ '/assets/img/research/constrained-simulation/cover.webp' | relative_url }}" alt="Unquantified fictional thematic illustration retained from the supplied project. It is not performance evidence or a deployment plan." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 1.</span> Unquantified fictional thematic illustration retained from the supplied project. It is not performance evidence or a deployment plan.</figcaption></figure>

This public note treats the archive as a case in research practice. The numerical examples introduced below are independently created benign demonstrations, not recovered source-scenario performance. This allows the article to explain verification without confusing an illustrative calculation with a new execution of the original study.

The central question is consequently an evidence question: what must be present for a computational conclusion to be traceable, and what additional observation would be required before that conclusion can describe reality?

<h2 id="archive">2. Archived evidence and versions</h2>

### 2.1 The saved research package

The manifest identifies one recorded run and links several artifact types by SHA-256. A fresh file-by-file audit confirms 36 matches, zero missing files and zero hash mismatches. The check reads the existing material; it does not rewrite the source project or regenerate its results.

<div class="hy-model-table"><table><caption>Table 1. Fresh audit of manifest-linked artifacts.</caption><thead><tr><th scope="col">Artifact category</th><th scope="col">Entries</th><th scope="col">Current hash matches</th></tr></thead><tbody><tr><td>Executable source</td><td>11</td><td>11</td></tr><tr><td>Inputs</td><td>3</td><td>3</td></tr><tr><td>Results</td><td>10</td><td>10</td></tr><tr><td>Figures</td><td>11</td><td>11</td></tr><tr><td>Manuscript</td><td>1</td><td>1</td></tr><tr><td>Total</td><td>36</td><td>36</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/artifact-integrity.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 2 at full size"><img src="{{ '/assets/img/research/constrained-simulation/artifact-integrity.svg' | relative_url }}" alt="Fresh manifest audit. Matching hashes establish that current files agree with the recorded versions; they do not verify the scientific interpretation of those files." width="1046" height="389" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 2.</span> Fresh manifest audit. Matching hashes establish that current files agree with the recorded versions; they do not verify the scientific interpretation of those files.</figcaption></figure>

An unchanged checksum is strong evidence against unnoticed file replacement. It is weaker evidence about provenance: a hash cannot show whether an input was measured, simulated or manually transcribed, nor whether its source definition was appropriate. Those facts need an accompanying description.

### 2.2 Archived review versus current review

The saved review report describes corrections to statistical reporting, reference consistency, symbols, figure labels and manuscript layout. It also records both automatic diagnostics and subsequent manual interpretation. These are historical review claims, not checks automatically renewed by displaying the material on a website.

This revision verifies manifest integrity and constructs separate general numerical examples. It does not replay the original optimization or assert that every archived science and visual gate has been independently rerun. The distinction prevents a newly designed article from silently acquiring the status of a newly validated experiment.

<h2 id="assumptions">3. An explicit evidence contract</h2>

An evidence contract identifies four things before results: the question, the data, the assumptions and the acceptance criterion. A missing item often reveals why a claim is broader than the calculation.

Given quantities should be distinguished from calibrated parameters and convenient constants. An assumption justified by a mechanism differs from an assumption introduced because measurement is unavailable. The second remains an uncertainty even if it helps a solver produce a unique answer.

<div class="hy-model-table"><table><caption>Table 2. An inspectable evidence contract.</caption><thead><tr><th scope="col">Element</th><th scope="col">Required record</th><th scope="col">Common ambiguity</th></tr></thead><tbody><tr><td>Question</td><td>Observable or mathematical target</td><td>A broad aspiration substitutes for a testable claim</td></tr><tr><td>Input</td><td>Source, units, time and data type</td><td>Synthetic values are read as observations</td></tr><tr><td>Assumption</td><td>Reason and consequence of simplification</td><td>Omitted effects become invisible certainty</td></tr><tr><td>Method</td><td>Equations, constraints and implementation</td><td>A success flag replaces method description</td></tr><tr><td>Acceptance</td><td>Reference, tolerance and scope</td><td>Formatting pass is read as science pass</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/workflow.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 3 at full size"><img src="{{ '/assets/img/research/constrained-simulation/workflow.svg' | relative_url }}" alt="General verification workflow retained from the public note. It concerns assumptions and evidence assessment, not the source scenario’s operational procedure." loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 3.</span> General verification workflow retained from the public note. It concerns assumptions and evidence assessment, not the source scenario’s operational procedure.</figcaption></figure>

A useful mathematical summary writes the calculation as an output conditional on inputs and a model:

<div class="hy-equation">
\[
\hat q=\mathcal A(D;\mathcal M,\eta),
\tag{1}
\]
</div>

D denotes the available data, M the modeling assumptions and η the numerical settings. Repeatability asks whether the same record reproduces the same output. Model adequacy asks a different question: whether the output remains useful when compared with independent observations or when assumptions are relaxed. These questions should have different tests.

<h2 id="baselines">4. Comparable references</h2>

A reported improvement requires a declared reference evaluated under the same conventions. The objective definition, input scope, feasibility rules and accounting method must remain aligned. Otherwise the difference can reflect a changed problem rather than a better solution.

Three references are especially easy to confuse. A simple feasible construction supplies a practical baseline. Another implemented method supplies an algorithmic comparison. A mathematical bound supplies a certificate for a particular objective and feasible set. Each answers a different question.

<div class="hy-model-table"><table><caption>Table 3. Reference types and the claims they support.</caption><thead><tr><th scope="col">Reference</th><th scope="col">Useful comparison</th><th scope="col">Unsupported shortcut</th></tr></thead><tbody><tr><td>Simple feasible construction</td><td>Improvement over a transparent starting point</td><td>Global optimality</td></tr><tr><td>Alternative implementation</td><td>Agreement or relative behavior on a common test</td><td>Independence if both share the same error</td></tr><tr><td>Analytic exact case</td><td>Correctness in a controlled limit</td><td>Validity of the full physical model</td></tr><tr><td>Theoretical bound</td><td>Objective gap in a stated feasible family</td><td>Optimality under another family or metric</td></tr><tr><td>Independent observations</td><td>Model adequacy in the observed conditions</td><td>Unlimited future generalization</td></tr></tbody></table></div>

Feasibility belongs in every comparison. A lower objective value obtained by violating a constraint is not a better feasible answer. Likewise, the reference should not be artificially weakened by a different evaluator, a reduced search budget or missing preprocessing that the candidate receives.

A research article should state an improvement's denominator and units, retain enough digits to reproduce its accounting, and explain whether uncertainty or random restarts could change the ordering. Those details make a comparative claim reviewable even when a global certificate is unavailable.

<h2 id="checks">5. Independent verification</h2>

Independent verification approaches an artifact from a direction that can expose a shared error. Recomputing a reported quantity from saved coordinates, deriving a limit analytically, changing the numerical scheme or evaluating a constraint from its mathematical definition all provide useful alternatives.

Merely running the same code again is narrower: it demonstrates repeatability but can preserve a shared wrong sign, unit conversion or clipping rule. A second program can also repeat the same mistake if it copies the first implementation too directly. Method independence therefore matters more than the number of files named “verify.”

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/evidence-layers.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 4 at full size"><img src="{{ '/assets/img/research/constrained-simulation/evidence-layers.svg' | relative_url }}" alt="Conceptual evidence ladder. Higher-level claims require additional checks; this diagram is not a pass/fail score assigned to the source project." width="1047" height="334" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 4.</span> Conceptual evidence ladder. Higher-level claims require additional checks; this diagram is not a pass/fail score assigned to the source project.</figcaption></figure>

An implementation check should record both absolute and scaled discrepancies. A generic normalized discrepancy is

<div class="hy-equation">
\[
e_{\rm scaled}=\frac{|q_{\rm candidate}-q_{\rm reference}|}{a+r\,|q_{\rm reference}|},
\tag{2}
\]
</div>

with declared absolute scale a and relative scale r. A tolerance should be linked to numerical behavior and the application’s measurement resolution, rather than chosen after seeing a desired result.

The research collection contains examples of why this distinction matters: a corrected covariance definition changes coverage interpretation, a continuous spline can exceed a node-only bound, and a greedy feasible construction does not prove an optimization upper bound. Those are failures of the evidence relation, even when the calculation itself produces an orderly table.

<h2 id="convergence">6. A benign exact-reference experiment</h2>

### 6.1 A deliberately benign exact case

To make numerical verification concrete, this revision constructs a new unit-semicircle example. Its arc-length parameter runs from zero to π, and its exact position and tangent are

<div class="hy-equation">
\[
\mathbf r(s)=(\sin s,\ 1-\cos s),\qquad \mathbf r'(s)=(\cos s,\ \sin s).
\tag{3}
\]
</div>

The endpoint is exactly (0,2). The experiment approximates the tangent integral by the composite trapezoid rule using 8, 16, 32, 64, 128 and 256 intervals. It compares the computed endpoint with the analytic one. All quantities are dimensionless and unrelated to the source scenario.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/reference-experiment.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 5 at full size"><img src="{{ '/assets/img/research/constrained-simulation/reference-experiment.svg' | relative_url }}" alt="New benign exact-reference example. The refinement curve describes composite trapezoid integration of a unit semicircle, not archived source-scenario performance." width="954" height="394" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 5.</span> New benign exact-reference example. The refinement curve describes composite trapezoid integration of a unit semicircle, not archived source-scenario performance.</figcaption></figure>

### 6.2 What refinement establishes

The error declines under interval doubling, and the expected second-order behavior can be checked through adjacent rates:

<div class="hy-equation">
\[
p_N=\frac{\log(E_N/E_{2N})}{\log 2}.
\tag{4}
\]
</div>

An analytic reference makes it possible to detect incorrect integration or endpoint handling. The observed trend is useful because both the geometry and the error criterion are explicit. Its conclusion remains narrow: the chosen quadrature behaves correctly on this smooth exact test.

The example does not validate a separate simulation with discontinuities, uncertain inputs or different geometry. It also demonstrates why an error plot should disclose what is refined. Sampling density, integration steps, interpolation rules and solver stopping criteria can each produce a convergence-like curve while measuring different error sources.

<h2 id="sensitivity">7. Conditional uncertainty</h2>

A sensitivity study is conditional on what is perturbed and what is allowed to change. Fixed-design sensitivity asks how one saved construction responds to new inputs. Re-solving after perturbation asks what an adaptive model can recover. The second may hide fragility of the first if reported without distinction.

Structural alternatives are different again. Replacing a sign convention, coordinate interpretation or assignment rule changes the model family; it is not simply another draw from sensor noise. These experiments should remain separately labeled.

<div class="hy-model-table"><table><caption>Table 4. Uncertainty questions that should not be merged.</caption><thead><tr><th scope="col">Experiment</th><th scope="col">Held fixed</th><th scope="col">Interpretation</th></tr></thead><tbody><tr><td>Input perturbation</td><td>Model and saved decision</td><td>Conditional margin of that decision</td></tr><tr><td>Re-solving</td><td>Model family, revised input</td><td>Adaptability under a new solve</td></tr><tr><td>Model reconfiguration</td><td>Selected alternative assumptions</td><td>Structural sensitivity</td></tr><tr><td>Empirical repeated measurements</td><td>Observed data-generation process</td><td>Measured variability</td></tr><tr><td>Assumed-distribution Monte Carlo</td><td>Declared sampling distribution</td><td>Propagation under that distribution</td></tr></tbody></table></div>

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/conditional-uncertainty.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 6 at full size"><img src="{{ '/assets/img/research/constrained-simulation/conditional-uncertainty.svg' | relative_url }}" alt="New dimensionless toy experiment: derived length π/(1+ε) under assumed Gaussian scale noise. The distribution is imposed for explanation, not estimated from the source project." width="1046" height="389" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 6.</span> New dimensionless toy experiment: derived length π/(1+ε) under assumed Gaussian scale noise. The distribution is imposed for explanation, not estimated from the source project.</figcaption></figure>

In the benign example, ε is independent Gaussian relative noise with standard deviation 0.02, and a derived quantity is ℓ=π/(1+ε). For small noise, first-order propagation gives approximately

<div class="hy-equation">
\[
\operatorname{sd}(\ell)\approx\pi\,\operatorname{sd}(\varepsilon).
\tag{5}
\]
</div>

Five thousand fixed-seed draws visualize that declared assumption. Their histogram is a simulation output, not empirical field uncertainty. Choosing a different variance or distribution changes the result; a visually plausible histogram does not calibrate either choice.

For a research package, the corresponding uncertainty record should retain distributional assumptions, parameter sources, dependence structure, sample counts and seeds. Sensitivity can then expose fragility without being overstated as a probability of real-world success.

<h2 id="diagnostics">8. Review automated diagnostics</h2>

Automatic checks are valuable precisely when their scope is recorded. A parser can find an undefined reference; a hash audit can detect changed bytes; a geometric evaluator can detect a constraint violation within its model. None of these by itself supplies evidence that the physical model is correct.

The archived report illustrates another distinction: a machine diagnostic can identify a visual risk that manual inspection later classifies as a false positive. Such a classification requires its own evidence. It should not be silently replaced with a blanket pass or copied forward after document reflow.

<div class="hy-model-table"><table><caption>Table 5. How to interpret automated diagnostics.</caption><thead><tr><th scope="col">Diagnostic</th><th scope="col">Direct evidence</th><th scope="col">Additional review needed</th></tr></thead><tbody><tr><td>File-integrity audit</td><td>Matches recorded bytes</td><td>Input origin and scientific meaning</td></tr><tr><td>Reference checker</td><td>Keys and citations align</td><td>Source supports the associated statement</td></tr><tr><td>Figure or page geometry</td><td>Potential clipping or overlap</td><td>Rendered readability and semantic accuracy</td></tr><tr><td>Constraint evaluator</td><td>Declared formulas satisfied</td><td>Formulas adequately describe the intended system</td></tr><tr><td>Solver termination</td><td>A stopping rule was reached</td><td>Solution quality and independent evaluation</td></tr></tbody></table></div>

When a diagnostic conflicts with inspection, both should be retained: the original signal, the examination used to resolve it, and the document version examined. A manual exception should be specific to the actual issue rather than a reusable excuse for future failures.

This revision does not claim to renew the source report's full visual review. Its current visual checks concern the published article, formula rendering, image loading, section navigation and mobile overflow. The manuscript remains an archived artifact with a separately documented review history.

<h2 id="reproducibility">9. Trace claims through artifacts</h2>

A provenance chain links input, executable implementation, output, figure and manuscript interpretation. Each transformation should retain a version and enough information to regenerate or inspect its product. A PDF or webpage alone often cannot distinguish several revised result files.

<figure class="hy-research-figure hy-model-figure"><a class="hy-model-zoom" href="{{ '/assets/img/research/constrained-simulation/provenance-chain.svg' | relative_url }}" target="_blank" rel="noopener" aria-label="Open Figure 7 at full size"><img src="{{ '/assets/img/research/constrained-simulation/provenance-chain.svg' | relative_url }}" alt="Conceptual transformation chain. Each edge needs a version, transformation and evidence record; a link alone is not proof that the interpretation follows." width="1046" height="343" loading="lazy"><span class="hy-model-zoom-label">View full size ↗</span></a><figcaption><span>Figure 7.</span> Conceptual transformation chain. Each edge needs a version, transformation and evidence record; a link alone is not proof that the interpretation follows.</figcaption></figure>

Manifest integrity is the starting point. The next step is semantic alignment: the number in a paragraph must refer to the intended output, use the same accounting convention and retain the relevant assumptions. This is especially important when drafts coexist with revised artifacts.

Old and new files should not be averaged into a convenient narrative. A revised value should replace an earlier one only after its version and interpretation are resolved. If that resolution is unavailable, the disagreement itself belongs in the evidence record.

For website publication, scientific plots should be stored in the repository with their article, while conceptual covers should be labeled as illustrations. Figure captions should name the data or demonstration being shown. This keeps a visually compelling image from implying measurements or validation that were never performed.

<h2 id="verification">10. Checks completed in this revision</h2>

The current revision performs three concrete tasks: it audits the recorded artifact hashes, constructs two benign examples independently of the original scenario, and checks the resulting public article. The source folder is preserved, and no source optimization is rerun.

<div class="hy-model-table"><table><caption>Table 6. Evidence ledger for this revision.</caption><thead><tr><th scope="col">Item</th><th scope="col">Current evidence</th><th scope="col">Limit</th></tr></thead><tbody><tr><td>36 manifest-linked files</td><td>All present, all hashes match</td><td>Integrity rather than scientific validation</td></tr><tr><td>Archived review history</td><td>Read and distinguished from current checks</td><td>Not a fresh rerun of every gate</td></tr><tr><td>Semicircle experiment</td><td>New analytic endpoint and refinement calculation</td><td>Benign exact case only</td></tr><tr><td>Scale-noise example</td><td>Declared fixed-seed distribution and propagation</td><td>Illustrative, not empirically calibrated</td></tr><tr><td>Published article</td><td>Formula, image, anchor and viewport checks</td><td>Web presentation rather than manuscript revalidation</td></tr></tbody></table></div>

These results make the article more inspectable without implying that a broader scenario claim has been proved. The new examples have their own assumptions and output records. The archive audit has a different purpose and result type. Keeping them separate is the practical evidence discipline the page advocates.

No full-source or operational-results download is attached. The public research contribution is an account of verification, traceability and interpretation that can be applied to benign geometry, sensing, service planning and numerical analysis.

<h2 id="discussion">11. Discussion and conclusions</h2>

A computational artifact becomes scientifically useful when another reader can identify its question, reproduce its accounting, examine its assumptions and understand what has not been validated. More figures or more decimal places do not substitute for those relationships.

The archive’s complete hash agreement supports a narrow but important conclusion: the recorded research package is internally version-consistent at the time of this review. The new exact-reference example shows how a controlled calculation can expose numerical behavior. The noise example shows why uncertainty claims must stay conditional on their sampling assumptions.

The remaining distinction is between checking the computation and checking its model. Independent observations, calibrated inputs, relevant omitted mechanisms and out-of-sample tests are needed before a simulation can support a real-world claim. Where those are absent, a transparent methodological result can still be valuable.

This note therefore treats reproducibility as a foundation, verification as a set of explicit tests, and validation as an additional evidential task. Its contribution to the collection is a concrete account of that hierarchy, with current checks separated from archived review and new illustrations separated from source results.
