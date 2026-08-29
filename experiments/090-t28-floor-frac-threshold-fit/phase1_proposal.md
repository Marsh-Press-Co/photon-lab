# PHASE 1 — PROPOSAL · Panel Iteration 67 · exp-090 · Lead seat: PHOTONICS

## "Floor-Frac Threshold Fit" — a rank-separation caution-zone method for R13's denominator floor gate, fit against all 7 now-resolved (θ, margin, ratio_k) points

### 1. Mechanism/method narrative (≤300 words)

exp-089 closed with a clean but tiny fact: across the n=7 angles where
`ratio_k`'s denominator (`frac_contrast`) clears R13's existing
`FLOOR_FRAC=0.10` gate, the two misclassified (ENERGY-DOMINANT) points sit
at floor-margins 1.3095×/1.4764×, and every correctly-classified
(CONSISTENT) point sits at 2.1709× or above — a perfect rank separation,
which I independently re-derive from raw `frac_contrast` in
`results.json` below (Table 1). Red Team ruled a single re-tuned
threshold premature and asked for a graduated caution zone instead. A
perfectly-separable n=7 sample is exactly the regime where an ordinary
maximum-likelihood logistic fit is *degenerate*: the likelihood is
maximized by driving the slope to infinity, pinning a knife-edge boundary
inside the gap with no notion of confidence — I demonstrate this
numerically below (naive MLE diverges to |β|~10³ on this exact data) and
treat it as a hazard to be neutralized, not glossed over.

My method has three layers, all zero-FDTD, all deterministic given the 7
committed numbers: (1) a **non-parametric caution zone** — the closed
margin interval between the largest misclassified margin and the smallest
correctly-classified margin — as the primary, assumption-free deliverable
Red Team asked for; (2) an **exact permutation test** on the margin's rank
concordance with outcome, to certify the separation is not a 7-point
coincidence; (3) **Firth's penalized (bias-reduced) logistic regression**
of outcome on log₁₀(margin) as a finite, corroborating point-estimate and
sensitivity check, replacing the divergent naive MLE. A 7-fold leave-one-
out jackknife stress-tests how much the zone moves under held-out data.
The regressor is `margin` alone — not θ, not `frac_p_abs` — for reasons
stated in §5.

### 2. Parameter table

**The n=7 resolved dataset** (independently recomputed by me, this cycle,
directly from each experiment's committed `results.json::frac_contrast`
fields — not copied from any prose figure — against `FLOOR =
FLOOR_FRAC(0.10) × RMS[frac_contrast] = 1.91744×10⁻⁴`, itself unchanged
since exp-088, computed over exp-083's own 31-point window,
`RMS=1.917438×10⁻³`):

| θ | source | `frac_contrast(θ)` | `margin = frac_contrast/FLOOR` | `ratio_k(θ)` | label (outcome Y) |
|---|---|---|---|---|---|
| 36.0° | exp-087 | 7.438280×10⁻⁴ | 3.8793 | 2.6424 | C (Y=0) |
| 37.2° | exp-089 | 4.162655×10⁻⁴ | 2.1709 | 3.4433 | C (Y=0) |
| 38.4° | exp-088 | 1.437049×10⁻³ | 7.4946 | 0.9075 | C (Y=0) |
| 38.8° | exp-088 | 1.537528×10⁻³ | 8.0187 | 3.8733 | C (Y=0) |
| 40.2° | exp-089 | 2.830881×10⁻⁴ | 1.4764 | 25.0820 | **X** (Y=1) |
| 41.4° | exp-089 | 2.510967×10⁻⁴ | 1.3095 | 28.8072 | **X** (Y=1) |
| 41.8° | exp-087 | 1.263381×10⁻³ | 6.5889 | 5.7102 | C (Y=0) |

*(excluded from the n=7 fit, out-of-sample check only)* 38.6°, exp-087:
`frac_contrast=7.410063×10⁻⁵`, margin=0.3865 (fails the existing
`FLOOR_FRAC=0.10` gate itself, `NODE-UNRESOLVABLE` per R13/exp-088), true
`ratio_k=53.988`.

Sorted by margin, the separation is exact and visible by inspection:
`1.3095(X), 1.4764(X), 2.1709(C), 3.8793(C), 6.5889(C), 7.4946(C),
8.0187(C)` — every X-margin is strictly below every C-margin; no ties.

| Method component | Exact specification |
|---|---|
| Population | The 7 angles above where `resolved=True` at `FLOOR_FRAC=0.10` (θ=38.6° excluded by construction, scored separately as an out-of-sample check, §4 item 5). |
| Outcome `Y(θ)` | 1 if `classify_resolved` label is "X" (`ratio_k>RATIO_HIGH=10`); 0 if label is "C" (`0.1≤ratio_k≤10`). No "D" (`ratio_k<0.1`) label occurs in this set — the method as specified below is a 2-class (not 3-class) classifier; extending to "D" is out of scope until a "D" point exists on record. |
| Regressor `x(θ)` | `log₁₀(margin(θ))`, `margin(θ) = frac_contrast(θ)/FLOOR`, `FLOOR` fixed at its current committed value (1.91744×10⁻⁴) for this fit — the fit calibrates where in *margin space* the boundary sits, not a new `FLOOR_FRAC` number directly (§5). |
| (1) Non-parametric caution zone | `zone = [max{margin(θ): Y=1}, min{margin(θ): Y=0}]` = **[1.4764, 2.1709]** (computed, not fit — an order-statistic construction, no free parameters). A margin below the zone's lower edge is treated as failing (matches existing behavior below 1.0); inside the zone is **CAUTION** (report `ratio_k` but do not certify CONSISTENT or ENERGY-DOMINANT from the gate alone); above the zone's upper edge is trusted-resolved, as today. |
| (2) Exact permutation test | Statistic: AUC of `margin` as a (lower-margin-is-positive) classifier of `Y`, i.e. Mann–Whitney concordance. Null: all `C(7,2)=21` equally-likely assignments of which 2 of the 7 angles carry `Y=1`, margins held fixed. `p = #{permutations: AUC_perm ≥ AUC_obs} / 21`, computed exactly (n small enough for full enumeration — no Monte Carlo, no seed dependency). |
| (3) Firth logistic fit | Standard Firth (1993) bias-reduced binomial logistic regression of `Y` on `[1, x]` (intercept + `log₁₀(margin)`), fit by the modified score equation `U*(β) = Xᵀ(y − p + h∘(0.5 − p))`, `h` = diagonal of the weighted hat matrix `H = W^{1/2}X(XᵀWX)⁻¹XᵀW^{1/2}`, `W=diag(p(1−p))`, iterated by Newton–Raphson (`β ← β + (XᵀWX)⁻¹U*(β)`) to `‖Δβ‖_∞<10⁻¹⁰`, ≤200 iterations. Reports: converged finite `(β₀,β₁)`, the 50%-crossing margin `m₅₀=10^(−β₀/β₁)`, and fitted `P(Y=1∣margin)` at all 8 angles (7 fit + 1 out-of-sample). |
| (4) Leave-one-out (LOO) jackknife | 7 exhaustive refits of (1)+(3), each holding out one of the 7 angles; report how far the caution-zone edges and `m₅₀` move. Exhaustive (not resampled with replacement) — n=7 permits full enumeration, avoiding any bootstrap-on-7-points instability. |
| (5) Out-of-sample check | Score θ=38.6° (margin=0.3865, excluded from the fit) through the fitted Firth model and against the caution zone; report `P(Y=1)` and whether 38.6° falls below the zone's lower edge (consistency check against R13's own existing, separate exclusion of this point). |
| Software | Pure Python + NumPy (Newton–Raphson, closed-form hat matrix) — no external logistic-regression library required; a SciPy cross-check of the naive (unpenalized) MLE's divergence is diagnostic only, not part of the certified method. |
| Reuse convention | `FLOOR`/`RMS` remain `graded_black_shell`/600nm-specific (Idealization 16, exp-089); this fit's outputs (the zone, `m₅₀`) inherit that same scope and must be restated, not silently reused, for any other article/wavelength. |

### 3. T1 escape route

**N/A (T28 desk instrument-calibration work), stated plainly, matching
exp-070's and exp-085 leg-a's own precedent.** This is a zero-FDTD
statistical re-analysis of the panel's own energy-interception floor
gate (R13), not a phenomenon-mechanism proposal. It makes no claim about
constraints 1–4, does not touch `REALIZABILITY_MEMO.md`, and Checkpoint
criterion 2 is N/A — matching every T28 desk/instrument cycle since
exp-069.

### 4. Falsifiable predicted outcomes (committed before any script runs)

I computed the numbers below myself, once, in a throwaway desk script,
to verify the method is actually implementable and well-behaved before
proposing it (exactly as exp-089's own Phase-1 desk-computed floor
margins were disclosed as pre-Phase-4 numbers) — they are stated here as
the exact, falsifiable predictions a Phase-4 script must reproduce
bit-for-bit from the 7 committed data points, with no new FDTD and no
free choices left to the implementer.

1. **P1 (separation, hence naive-MLE hazard) — CONFIRM predicted.** The 7
   points are perfectly rank-separated by margin (AUC=1.0 exactly);
   an unpenalized logistic MLE on this data fails to converge to a finite
   optimum (any standard optimizer will drive `|β|→∞`, log-likelihood
   → 0). **Falsified if** the Phase-4 script finds even one margin-tie or
   rank-inversion between an X and a C point (i.e. AUC<1.0) — this would
   mean the "clean separation" premise motivating Firth's method here is
   itself wrong, and the non-parametric zone (P3) would need to move to a
   possibly-empty or overlapping interval instead.

2. **P2 (exact permutation test) — predicted `p = 1/21 = 0.047619` (to
   6 s.f.), AUC_obs=1.0.** Pre-committed pass bar: `p≤0.05` — note this
   sits just inside the bar at n=7's own coarsest possible resolution
   (the smallest attainable non-zero p-value at this n,k is 1/21); this
   is disclosed as a real, structural limit of what n=7 can certify, not
   hidden. **Falsified if** the computed exact p exceeds 0.05, which at
   this n can only happen if P1 is also violated.

3. **P3 (non-parametric caution zone) — predicted exactly `[1.4764,
   2.1709]`** (bit-exact to the values in Table 1, a computed order
   statistic, no fitting). Width predicted **0.6945** (47% of the lower
   edge) — a genuinely wide zone at this sample size, not a
   knife-edge. **Falsified if** the computed zone is empty or inverted
   (upper<lower) — would mean P1 was violated.

4. **P4 (Firth fit) — predicted to CONVERGE to finite coefficients**
   within 200 Newton–Raphson iterations to the stated tolerance
   (contrasted explicitly against the naive MLE's divergence, P1).
   Central prediction: `m₅₀` (the 50%-crossing margin) lands **strictly
   inside** the P3 zone, i.e. `1.4764 < m₅₀ < 2.1709`, most likely in the
   upper half of that interval (informal desk check, disclosed as
   informal: my own throwaway run landed at `m₅₀≈2.07`, near the zone's
   upper edge — reported for context, not pre-registered as a tight
   band; the pre-registered, falsifiable claim is only the interval
   membership). **Falsified if** Firth's iteration fails to converge
   inside 200 steps at the stated tolerance (a real method failure,
   triggering the fallback in §6), or if `m₅₀` falls outside the P3
   zone entirely (would mean the parametric and non-parametric readings
   materially disagree — reported, not hidden, and would downgrade this
   method's own recommended confidence).

5. **P5 (LOO jackknife stability) — predicted: the caution zone's LOWER
   edge stays at 1.4764 in 6 of 7 leave-one-out refits, moving only to
   1.3095 when 40.2° itself is held out (its own margin is then
   replaced by 41.4°'s 1.3095 as the new max-X); the UPPER edge stays at
   2.1709 in 6 of 7 refits, moving only to 3.8793 when 37.2° itself is
   held out.** All 7 LOO refits are predicted to preserve full rank
   separation (AUC_LOO=1.0 in every 6-point subset) — i.e. the
   separation is not an artifact of any single point. **Falsified if**
   any LOO subset loses full separation (AUC_LOO<1.0), which would mean
   the n=7 clean-separation finding is fragile to a single point and the
   zone should be reported with substantially lower confidence than P3
   alone conveys.

6. **P6 (out-of-sample check, 38.6°) — predicted `P(Y=1)>0.9` under the
   fitted Firth model** (informal desk check: my own run gives ≈0.984)
   **and margin(38.6°)=0.3865 falls below the P3 zone's lower edge** —
   i.e. the already-existing R13 exclusion of 38.6° and this new
   caution-zone construction agree on treating it as untrustworthy,
   from two independently-motivated constructions. This is context, not
   a scored pass/fail — 38.6° is not part of the n=7 population this
   method fits.

**What a "pass" of this whole method looks like, stated before any
Phase-4 run**: P1, P2, P3, and P5 must all land exactly as predicted
(they are computed, not estimated, from already-committed numbers — any
deviation signals either a transcription error in the 7-point table or a
misunderstanding of the separation structure) for the method to be
certified as correctly specified and implemented. P4's directional claim
(convergence + interval membership) is the one genuinely load-bearing
statistical prediction; a clean P4 pass (converges, `m₅₀` inside the
zone) certifies Firth's method as a sound *complement* to the
non-parametric zone at this sample size. **What "fail" looks like**: any
of P1/P2/P3/P5 not reproducing bit-exact from the 7 numbers is a
methodology bug, not a scientific finding, and blocks Phase 3 pending a
fix. A P4 failure (non-convergence, or `m₅₀` outside the zone) does NOT
block the deliverable — the non-parametric zone (P3) stands on its own
without Firth's corroboration — but must be reported as a disclosed
downgrade of confidence in the parametric complement specifically, per
§6's named fallback.

### 5. Regressor choice — margin alone, not θ, not `frac_p_abs` (required disclosure)

**Why `margin` and not raw θ or "distance from nearest known
`delta_scene` zero-crossing":** `frac_contrast(θ)` is, to leading order
near a simple zero of `delta_scene`, locally linear in `(θ−θ₀)` — so
`margin(θ)` already *is* a physically-grounded, dimensionless proxy for
crossing-proximity, without requiring a second model to first identify
"which crossing is nearest" and compute a signed angular distance to it
(a strictly worse, indirect, more assumption-laden regressor for the
identical underlying quantity). `margin` is also the literal object R13's
own floor gate thresholds on — fitting the gate's own native quantity
keeps the calibration interpretable as "what value of `FLOOR_FRAC` would
this imply," which a θ-distance regressor would not. Adding raw θ (or
crossing-distance) as a *second* regressor alongside `margin` in a 7-point,
2-event logistic fit would over-parameterize a design this small can't
support (the R5/R7 "small-sample multi-parameter fit" hazard this program
has repeatedly flagged) for no gain, since the two quantities are
near-collinear by the mechanism just stated. **I did not include it.**

**Why NOT `frac_p_abs` (the numerator) — required by the assignment's own
R14 cross-check, and the sharper reason:** including the numerator as a
regressor would not merely risk a "confound" in the loose sense — it
would defeat the floor gate's entire purpose. R13's floor gate exists
specifically so that a point's *trustworthiness* can be decided from the
denominator ALONE, before ever looking at `ratio_k` (equivalently, before
looking at `frac_p_abs`, since `ratio_k=frac_p_abs/frac_contrast`). A
gate that needs the numerator to decide whether to trust the numerator's
own ratio is circular by construction — it could never flag a point as
untrustworthy in advance of computing the very quantity it's supposed to
gate. Separately, R14 already names `frac_p_abs` its own
subtractive-cancellation hazard class (non-monotonic at 38.4°, per
exp-088/089) — smuggling that hazard into what is supposed to be a
denominator-only calibration would be exactly the defect the assignment
warns against. **I did not include it, and no version of this method may
be revised to include it without first re-litigating R13's own
floor-gate design, not merely this fit.**

### 6. Idealizations

1. **n=7 is very small.** Every inferential claim above is scoped to
   what n=7 can support: the exact permutation test's own coarsest
   attainable p-value is 1/21≈0.048 (there is no way to report a smaller
   p at this n without more data, regardless of how clean the separation
   looks); the non-parametric zone (P3) is an order statistic over 7
   points and will move noticeably as more angles are measured (P5's own
   LOO spread already shows this); Firth's `m₅₀` point estimate carries
   no formal confidence interval in this specification (a full penalized
   profile-likelihood interval is deferred, §7) — the LOO spread is used
   instead as an honest, assumption-light stand-in for estimation
   uncertainty, not a substitute for one.
2. **This method characterizes SEPARATION in the 7-point record as it
   currently stands — it is not a physical model of why margin predicts
   outcome**, and does not adjudicate between the competing physical
   readings already on record (R13's node-proximity story vs. any
   residual R14-adjacent numerator contribution) — Q6/exp-089's own
   decomposition (≈90% denominator / ≈10% numerator at 40.2°/41.4°)
   already answers that mechanistic question by a different method; this
   proposal answers a purely statistical-calibration question about the
   gate, not the mechanism question again.
3. **Single article, single wavelength (`graded_black_shell`, 600nm)** —
   the fit's outputs (the zone, `m₅₀`, `FLOOR` itself) are specific to
   this article/wavelength and must be independently recomputed, not
   numerically reused, for any other absorber or λ (Idealization 16,
   exp-089, restated here).
4. **The outcome label is binary (C vs X) by construction of this n=7
   sample** — no "D" (`ratio_k<0.1`, ENERGY-DECOUPLED) point exists in
   the current record; this method does not address a 3-class
   calibration and should not be silently extended to one without new
   data containing a "D" example.
5. **`NOISE_MULT=3.0` and `FLOOR_FRAC=0.10`'s CURRENT value are both
   inherited, house-style constants, not re-derived here** — this
   proposal fits where the boundary sits in margin-space; it does not
   re-derive `NOISE_MULT` or claim `FLOOR_FRAC=0.10` is "the" right
   scale-setting for `FLOOR`, only that (per exp-089) it is not fully
   protective at the margins this cycle's own data reached.
6. **The caution zone is a decision-rule proposal, not itself a physics
   claim** — a point landing inside `[1.4764, 2.1709]` is recommended to
   be reported as CAUTION (ratio_k shown, not certified either way), a
   house-style convention analogous to R13's own already-disclosed
   house-style choice of `FLOOR_FRAC`/`NOISE_MULT`, not a rigorously
   derived confidence interval in the frequentist sense.
7. **NETD/human-eye and constraint-1/2/3/4 disclaimers carry forward
   unchanged from exp-087/088/089** (Idealizations 9–10 in that
   numbering): nothing in this cycle bears on the human-eye verdict or
   re-opens `REALIZABILITY_MEMO.md`.
8. **This proposal does not re-run or re-verify R14(a)'s parent-quantity
   smoothness gate or R14(b)'s still-queued formal period fit** — both
   remain open, separate, standing T28 items (exp-089's own "Next"),
   untouched by this desk fit.

### 7. Explicitly out of scope, named forward (not silently dropped)

A full penalized profile-likelihood confidence interval for `m₅₀`
(sharper than the LOO-spread stand-in used here) is a cheap, zero-FDTD
follow-up if Phase 5 judges the LOO spread insufficient. If P4 fails
(Firth non-convergence, or `m₅₀` outside the P3 zone), the named fallback
is to report the non-parametric zone (P3) alone as the deliverable,
explicitly disclosing that the parametric complement did not corroborate
it — not to re-parameterize Firth's fit post-hoc until it does (which
would violate this program's own R8 "argument must be independently
verified, not re-reasoned" discipline in spirit). Any future
recalibration of `FLOOR_FRAC` itself (a house-style constant, not this
fit's own output) is a separate, subsequent decision this method
supplies evidence for but does not make unilaterally.
