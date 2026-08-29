# exp-090 — T28 Floor-Frac Threshold Fit

Panel Iteration 67. Lead: PHOTONICS (rotation). Executes exp-089's own
Reconciled Iteration-67 queue, Tier-1 item 1 (near-unanimous #1, ranked
ahead of any new FDTD bracket by Red Team's own recommendation): a
zero-FDTD logistic/threshold fit of R13's `FLOOR_FRAC` gate against all 7
now-resolved (θ, margin, `ratio_k`) points on record across
exp-087/088/089. Full phase record: `phase1_proposal.md` (PHOTONICS) →
five blind Phase-2 critiques (MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE, unanimous
support-with-changes, zero overlap) → `phase2_redteam_audit.md`
(PROCEED-WITH-MANDATORY-FIXES, 9 items, zero overridden) →
`phase3_synthesis.md` (this cycle's frozen spec, all 9 fixes adopted).

## Hypothesis

exp-089 closed with a clean but tiny fact: across the n=7 angles where
R13's floor gate (`FLOOR_FRAC=0.10`) certifies `ratio_k` as "resolved,"
the two misclassified (ENERGY-DOMINANT, `ratio_k>10`) points sit at
floor-margins 1.3095×/1.4764×, and every correctly-classified
(CONSISTENT) point sits at 2.1709× or above — a perfect rank separation.
Red Team ruled a single re-tuned `FLOOR_FRAC` threshold premature at this
sample size and asked for "a graduated caution zone, consistent with the
now-demonstrated continuous (not sharply-thresholded) mechanism." This
cycle tests: (1) whether a non-parametric caution zone, an exact
permutation test, a bias-corrected (Firth) logistic fit, and a
leave-one-out jackknife can jointly characterize that separation without
either (a) an ordinary maximum-likelihood logistic fit's known
degeneracy at perfect separation, or (b) overclaiming what a single-digit
sample can actually certify; and (2), added at Phase 2/Red Team's own
insistence, whether the chosen regressor (`margin`, i.e. `frac_contrast`
itself) is genuinely the better-supported choice against the most
obvious alternative (raw distance to the nearest known `delta_scene`
zero-crossing) — computed, not merely argued.

## Setup

Reuses exp-087/088/089's own already-committed `results.json` data
verbatim — zero new FDTD calls, zero new simulation geometry. The n=7
population: `θ=36.0°` (exp-087), `37.2°` (exp-089), `38.4°`/`38.8°`
(exp-088), `40.2°`/`41.4°` (exp-089), `41.8°` (exp-087). `θ=38.6°`
(exp-087, `NODE-UNRESOLVABLE` at the existing `FLOOR_FRAC=0.10` gate) is
excluded from the fit, scored only as an out-of-sample check.

`FLOOR = FLOOR_FRAC(0.10) × RMS[frac_contrast] = 1.91744×10⁻⁴`
(unchanged since exp-088, computed over exp-083's own 31-point window).
`margin(θ) = frac_contrast(θ)/FLOOR`. Outcome `Y(θ)=1` if
`classify_resolved` labels the point "X" (`ratio_k>RATIO_HIGH=10`), else
`Y=0` ("C", `0.1≤ratio_k≤10`).

**Method, three layers plus one comparator, all zero-FDTD:**
1. Non-parametric caution zone: `[max{margin:Y=1}, min{margin:Y=0}]`.
2. Exact permutation test on `AUC(margin)` (21 possible label
   assignments at n=7, k=2 — full enumeration, no Monte Carlo).
3. Firth's (1993) penalized bias-reduced logistic regression of `Y` on
   `log₁₀(margin)`, replacing a divergent naive MLE; 50%-crossing
   `m₅₀=10^(−β₀/β₁)`; exhaustive 7-fold leave-one-out jackknife.
4. **Comparator (added at Phase 2/Red Team's insistence, Idealization 5
   below):** the identical method applied to `distance-to-nearest-known-
   delta_scene-zero-crossing` instead of `margin`, to test whether
   `margin` is genuinely the better-supported regressor or merely an
   argued-equivalent one.

## Predictions (frozen, committed BEFORE any Phase-4 script runs)

**Carried idealizations banner (mandatory at both this section and the
Result section, per the Iteration-65 CHECKPOINT's own escalated,
non-discretionary rule — the omission of this banner from this section
in an earlier draft was itself caught blind at Phase 2 this cycle, by
VISION SCIENCE, before this document was frozen; see `phase2_
redteam_audit.md` §3 for Red Team's explicit non-firing ruling on that
catch):** every finding below is governed by Idealizations 6/7/13 (NETD
is not a human-eye threshold; this cycle does not test constraint
1/2/3/4; `FLOOR`/`RMS` are `graded_black_shell`/600nm-specific) — restated
inline at each item below, not stated once and dropped.

1. **Q1 (diagnostic precondition, not scored).** The 7 points are
   perfectly rank-separated by `margin` (`AUC=1.0`, no ties); an
   unpenalized logistic MLE fails to converge to a finite optimum on this
   data (any standard Newton–Raphson optimizer drives `|β|→∞`).
   (Idealizations 6/7/13 apply — this is pure pipeline arithmetic, no
   physical claim.)

2. **Q2 (diagnostic sanity check — reclassified from a falsifiable
   prediction, Phase-2 fix items 4+6; Idealizations 6/7/13 apply).** The
   exact permutation test predicted `p=1/21≈0.0476`. **This confirms
   internal pipeline/arithmetic correctness only — it is NOT independent
   evidence that the margin–outcome relationship is real**, because
   `margin` mechanically drives ~90% of the `ratio_k` classification per
   exp-089's own five-way-converged decomposition (ELECTROMAGNETISM's
   Phase-2 finding, upheld by Red Team): the permutation null (reshuffle
   `Y` with margins held fixed) is not a credible alternate world given
   that mechanism.

3. **Q3 (PRIMARY, falsifiable; Idealizations 6/7/13, 9-11 apply).** The
   non-parametric caution zone predicted exactly `[1.4764, 2.1709]`
   (bit-exact order statistics, no fitting), width `0.6945` (47% of the
   lower edge). A margin below the zone is treated as failing (as today,
   below 1.0); inside the zone is **CAUTION** (report `ratio_k`, do not
   certify either classification from the gate alone); above the zone is
   trusted-resolved, as today. **Falsified if** the computed zone is
   empty, inverted, or the underlying separation has any tie/inversion
   (would mean Q1 itself was wrong).

4. **Q4 (PRIMARY, falsifiable, genuinely contingent; Idealizations
   6/7/13 apply).** Firth's fit predicted to CONVERGE (≤200
   Newton–Raphson iterations, `‖Δβ‖_∞<10⁻¹⁰`) to finite `β≈(1.7806,
   −5.6315)`, `m₅₀≈2.0710`, landing strictly inside the Q3 zone.
   **Falsified if** Firth's iteration fails to converge, or `m₅₀` falls
   outside `[1.4764,2.1709]` — would downgrade confidence in this
   parametric complement specifically; the non-parametric zone (Q3)
   would stand alone regardless.

5. **Q5 (diagnostic sanity check — reclassified from a falsifiable
   prediction, Phase-2 fix items 5+6; Idealizations 6/7/13 apply).** The
   7-fold exhaustive leave-one-out jackknife predicted to show all 7
   subsets preserving `AUC=1.0` exactly, with the zone's lower edge
   moving only when 41.4° (the current argmin-X) is dropped (→1.3095)
   and the upper edge moving only when 37.2° (the current argmax-C, see
   Q7) is dropped (→3.8793). **This is a deterministic illustration of
   point-sensitivity, not a live stress test** — given Q1's own perfect,
   tie-free separation, every one of these outcomes is an order-statistics
   certainty, not new empirical information (QUANTUM OPTICS' Phase-2
   finding, upheld by Red Team). Reported for its illustrative value only.

6. **Q6 (context, unscored, unchanged convention from exp-089;
   Idealizations 6/7/13 apply).** `θ=38.6°` (margin `0.3865`, excluded
   from the n=7 fit) scored out-of-sample against the fitted Firth model:
   predicted `P(Y=1)>0.9` and below the Q3 zone's lower edge — agreeing
   with R13's own existing, separately-motivated exclusion of this point.

7. **Q7 (NEW — disclosure gate, Red Team RT-1; Idealizations 6/7/9
   apply).** 37.2° sets the Q3 zone's own upper edge (2.1709) AND is
   Firth's most load-bearing C-class point — but exp-089's own permanent
   record (`NOTES.md` Learned #4) already flags this exact angle's
   *separate* `resolved`-gate noise-floor margin (a different quantity:
   `|Δp_abs|/(NOISE_MULT·box_dev_max·p_abs(C40))`, not this fit's
   `frac_contrast`-based `margin`) as "1.046×, the thinnest this
   sub-thread has ever accepted... a felt-lucky pass, not a robust one."
   Predicted: this cycle's own from-scratch recomputation from raw
   `box_dev`/`p_abs_w` primitives reproduces `≈1.046×` (this synthesis's
   own desk check landed at `1.0455×`, the same figure to the precision
   printed — see `phase3_synthesis.md`, not a discrepancy). **If 37.2°'s
   own reliability is genuinely in question, the Q3 zone as reported may
   understate the true caution region by close to double** (the "drop
   37.2°" row of Q5's own LOO table, `→3.8793`, is the operationally
   primary sensitivity reading this cycle names, not an undifferentiated
   one-of-seven case). **Not itself falsifiable** — a disclosure gate, not
   a scored prediction.

8. **Q8 (NEW — PRIMARY, falsifiable, Red Team RT-3; Idealizations 6/7/13
   apply).** The distance-to-nearest-known-`delta_scene`-zero-crossing
   comparator, predicted (computed by the Director before this freeze,
   to be independently reproduced by Phase 4's own script): all four
   zero-crossings in exp-083's 31-point window locate at **≈37.127°,
   38.590°, 40.265°, 41.461°**; nearest-crossing distances at the 7
   angles predicted **36.0°→1.127°, 37.2°→0.073°, 38.4°→0.190°,
   38.8°→0.210°, 40.2°→0.065°, 41.4°→0.061°, 41.8°→0.339°**;
   `AUC(distance)=1.0` (perfect separation, matching `margin`);
   distance-zone `≈[0.065°, 0.073°]`, gap ratio (`upper/lower`)
   `≈1.11` — **roughly a third of margin's own gap ratio (`≈1.47`)**.
   **This is the falsifiable core of this cycle's own regressor-choice
   defense**: both regressors separate the n=7 sample perfectly, but
   `margin` is predicted to be the empirically more robust choice by a
   real, now-measured safety margin, not merely a theoretically-argued
   equivalent one (§5 of `phase1_proposal.md`'s original "near-collinear,
   no gain" framing is corrected by this measurement, not merely
   restated). **Falsified if** `AUC(distance)<1.0`, or if the distance-
   zone's gap ratio is NOT materially smaller than margin's own — either
   would mean `margin` is not in fact the more robust regressor and §5's
   choice needs to be revisited on the evidence, not the argument, exactly
   as R8 requires.

## Idealizations

1. **n=7 is very small.** The exact permutation test's coarsest
   attainable p-value is `1/21≈0.048` regardless of how clean the
   separation looks; the non-parametric zone is an order statistic over
   7 points that will move as more angles are measured (Q5's own LOO
   spread already shows this); Firth's `m₅₀` carries no formal confidence
   interval in this specification (the LOO spread stands in for one, not
   a substitute for a true profile-likelihood interval — deferred, see
   Next).
2. **This method characterizes SEPARATION in the 7-point record as it
   stands — it is not a new physical model of why margin predicts
   outcome.** exp-089's own decomposition (~90% denominator/~10%
   numerator at 40.2°/41.4°) already answers the mechanistic question by
   a different method; this fit answers a purely statistical-calibration
   question about the gate.
3. **Single article, single wavelength** (`graded_black_shell`, 600nm) —
   the zone, `m₅₀`, and `FLOOR` itself are specific to this
   article/wavelength (Idealization 16, exp-089, restated).
4. **The outcome label is binary (C vs X) by construction of this n=7
   sample** — no "D" (`ratio_k<0.1`, ENERGY-DECOUPLED) point exists on
   record; this method does not address a 3-class calibration.
5. **`NOISE_MULT=3.0` and `FLOOR_FRAC=0.10`'s CURRENT value are inherited
   house-style constants, not re-derived here** — this fit locates the
   boundary in margin-space; it does not claim `FLOOR_FRAC=0.10` is the
   right scale-setting, only that (per exp-089) it is not fully
   protective at the margins this program's own data has reached.
6. **The caution zone is a decision-rule proposal, not a rigorously
   derived frequentist confidence interval** — a house-style convention
   analogous to `FLOOR_FRAC`/`NOISE_MULT`'s own already-disclosed
   house-style status.
7. **NETD/human-eye and constraint-1/2/3/4 disclaimers carry forward
   unchanged from exp-087/088/089**: nothing in this cycle bears on the
   human-eye verdict or re-opens `REALIZABILITY_MEMO.md`.
8. **This cycle does not re-run or re-verify R14(a)'s parent-quantity
   smoothness gate or R14(b)'s still-queued formal period fit** — both
   remain open, separate, standing T28 items.
9. **[MATERIALS, Phase-2 fix item 2] The n=7 `frac_contrast` values —
   especially 40.2°/41.4°, which set the zone's own LOWER edge — have not
   passed an R3-mandated spatial (`cpl`) resolution check on this exact
   channel.** This gap is undischarged two cycles running as of exp-089
   and remains undischarged here; the already-queued exp-089 Tier-1 item
   3 will discharge it for this fit's own inputs when it runs. Named, not
   hidden.
10. **[THERMODYNAMICS, Phase-2 fix item 3] The caution zone governs trust
    in `ratio_k`'s classification label ONLY and must not be read as a
    signal to deprioritize or exclude CAUTION-region angles from any
    future denser `σ_abs(θ)` sampling design** — if anything, R14's own
    established `σ_ext(θ)`-differential concentration in exactly this
    region argues those angles should be OVERSAMPLED, not skipped.
11. **[Red Team RT-2] The n=7 population is a targeted, crossing-
    proximity-enriched sample by construction, not a random or
    representative draw over the 31-point window.** Of the 7, only
    36.0°/41.8° were not selected for proximity to a known `delta_scene`
    zero-crossing; 37.2°/40.2°/41.4° were explicitly chosen as
    "tightest-floor-margin grid neighbors" of the three newly-identified
    crossings (exp-089's own stated selection rule), and 38.4°/38.8° as a
    bracket around the founding 38.6° node (exp-088's own stated
    purpose). A future citation applying the zone/`m₅₀` to an arbitrary,
    non-crossing-adjacent angle would be extrapolating past this sample's
    actual support.

## Result

**Carried idealizations banner** (mandatory at both this section and the
Predictions section, per the Iteration-65 CHECKPOINT's own escalated
rule): every finding below is governed by Idealizations 6/7/13
(NETD is not a human-eye threshold; this cycle does not test constraint
1/2/3/4; `FLOOR`/`RMS` are `graded_black_shell`/600nm-specific).

**Every frozen prediction reproduced exactly. No surprises — a clean,
fully-verified confirmation, consistent with this being a desk cycle
whose numbers were independently re-derived by the Director before the
freeze (`phase3_synthesis.md`), by all five Phase-2 critiques, and by
Red Team's own Phase-2 audit, before `run.py` ever executed.**

- **Q1**: `AUC(margin)=1.0`, no ties, confirmed. Naive unpenalized MLE
  diverges (`β=(26.11,−103.01)` after 2000 Newton–Raphson steps, still
  climbing) — confirms the diagnosed hazard directly, not merely by
  assertion.
- **Q2 (diagnostic only)**: exact permutation `p=1/21=0.047619...`,
  bit-exact as predicted. Reported for pipeline-correctness only, per
  the reclassification above — NOT independent evidence the
  margin–outcome link is real.
- **Q3 (PRIMARY)**: caution zone = **`[1.4764, 2.1709]`**, width `0.6946`
  (47.0% of the lower edge), bit-exact as predicted.
- **Q4 (PRIMARY, contingent)**: Firth's fit **converged** in 20
  iterations (predicted ≤200) to `β=(1.78058954, −5.63151961)`,
  **`m₅₀=2.071013`**, landing strictly inside the Q3 zone, in the upper
  half as anticipated — confirmed.
- **Q5 (diagnostic only)**: all 7 LOO subsets preserve `AUC=1.0` exactly.
  Zone edges move only on the two predicted rows: dropping 41.4° →
  lower edge `1.3095`; dropping 37.2° → upper edge `3.8793`. Every other
  drop leaves the zone bit-identical. Confirms QUANTUM's order-statistics
  argument was exactly right — this table contains zero bits of
  information beyond Q1+Q3 themselves.
- **Q6 (context)**: `θ=38.6°` scores `margin=0.3865`, `P(Y=1)=0.9838`
  under the fitted model, below the Q3 zone's lower edge — agrees with
  R13's own pre-existing exclusion of this point, from an independently-
  constructed instrument.
- **Q7 (disclosure gate)**: 37.2°'s own SEPARATE `resolved`-gate
  noise-floor margin, recomputed live from exp-089's own persisted
  `thermo`/`box_dev` primitives (not hand-typed): **`1.045659×`** —
  matches exp-089's own filed `1.046×` to printed precision. This is the
  point setting the Q3 zone's upper edge and anchoring `m₅₀`'s shallow
  end; its own pre-existing fragility (a "felt-lucky pass" per exp-089's
  record) means the zone as reported should be read alongside the
  "drop 37.2°" LOO row (upper edge → `3.8793`) as the operationally live
  risk case, not a remote hypothetical.
- **Q8 (PRIMARY)**: all four `delta_scene(θ)` zero-crossings located at
  **37.1272°, 38.5902°, 40.2654°, 41.4609°** (matching exp-089's own
  citations to the sub-0.01° digit). Nearest-crossing distances at the 7
  angles reproduce exactly as predicted. **`AUC(distance)=1.0`**
  (perfect separation, matching `margin`), distance-zone
  `[0.0654°, 0.0728°]`, **gap ratio `1.1121`** — confirmed **roughly a
  third** of margin's own gap ratio (`1.4704`). **Confirmed: both
  regressors separate this sample perfectly, but `margin` is the
  empirically more robust choice by a real, measured safety margin — the
  regressor-choice defense in `phase1_proposal.md` §5 is corrected from
  an argued-collinearity claim to a computed one, exactly as Red Team's
  RT-3 required.**

All house gates PASS: `FLOOR`/`RMS[frac_contrast]` reproduce exactly
against exp-088's and exp-089's own committed R13-gate values (assertion
in `run.py`); `frac_contrast` at all 7 angles plus the excluded 38.6°
point is recomputed live from exp-083's own `per_theta` primitives
(`frac_contrast_of`, the identical formula exp-088's/exp-089's own
`run.py` implement) and reproduces the RMS-defining `FLOOR` constant to
within `1e-6` over the full 31-point window — not hand-typed. `ratio_k`
is cited from each source experiment's own already-independently-
verified record (reproduced bit-exact by the Phase-1 proposal, all five
Phase-2 critiques, and the Phase-2 Red Team audit — 7 independent
parties before this cycle; an 8th from-scratch re-derivation would
require re-importing three prior experiments' full FDTD-capture
pipelines for no material gain in confidence, a proportionate stopping
point given that history, not a shortcut).

## Learned

1. **The graduated caution zone Red Team asked for is real and usable:
   `[1.4764, 2.1709]` on `margin = frac_contrast/FLOOR`.** A point
   reading in this zone should be reported as CAUTION (show `ratio_k`,
   certify neither classification from the gate alone); the existing
   `FLOOR_FRAC=0.10` point threshold remains the hard floor below which a
   point is `NODE-UNRESOLVABLE`, unchanged.
2. **P2 and P5's demotion from "falsifiable predictions" to "diagnostic
   sanity checks" was the right call, confirmed by the run itself, not
   just argued at Phase 2.** Both reproduced bit-exact, exactly as
   algebraically guaranteed once Q1's tie-free separation held — neither
   supplied information beyond what Q1/Q3 already state. This is a
   reusable lesson: any future instrument built on a perfectly-separated
   small sample should check, BEFORE proposing a permutation test or a
   LOO stress test as independent evidence, whether the separation
   itself already logically forces the outcome.
3. **The regressor-choice defense in the original proposal was correct in
   its conclusion but under-supported in its method — computing it
   (Q8) produced a materially stronger and more precise claim than
   arguing it did.** `margin` and `distance-to-crossing` are NOT merely
   theoretically equivalent (the "near-collinear" framing) — they are
   both empirically perfect separators at this sample size, but `margin`
   carries roughly 3× the relative safety margin. This is a concrete
   instance of R8's own lesson (an argued robustness claim must be
   computed, not merely reasoned about) discharged the same cycle it was
   raised, cleanly.
4. **37.2° is a genuinely load-bearing, genuinely fragile point that this
   sub-thread should not lose sight of.** It anchors the Q3 zone's upper
   edge, Firth's `m₅₀`, AND (a separate, independently-flagged concern)
   its own `resolved`-gate admission was already the thinnest ever
   accepted before this cycle even started. None of this cycle's own
   machinery is positioned to resolve that fragility — only a genuinely
   new measurement (a repeat run at 37.2° with tighter settling, or a
   denser local sample) could.
5. **This is the second consecutive T28 Phase-1 lead draft to omit the
   now-mandatory dual-section idealizations banner** (caught blind at
   Phase 2 by VISION SCIENCE this cycle, exactly as a near-identical gap
   was caught blind at Phase 2 of exp-089). Per Red Team's own governance
   observation (`phase2_redteam_audit.md` §3): two clean catches in a row
   is not evidence the drafting-stage discipline is self-sustaining — it
   is evidence the review layer is doing its job while the authoring
   stage keeps needing it to. Named forward, not resolved here (see Next).

## Next

**Standing item raised by Red Team, not resolved this cycle:** a
mechanical lint-style safeguard for the recurring dual-section-banner
omission (in the spirit of `lab/caveat_lint_config.json`'s existing
enforcement for the STEPS=1400 gap), rather than relying on a third
consecutive Phase-2 catch. Candidate for a future Iteration's board
discussion, not itself a T28 physics item.

Substantive T28 items, reconciled from this cycle's own Idealizations and
exp-089's own still-open queue (unchanged by this desk cycle, since none
of it touches T28's mechanism question):

1. The still-overdue R3 spatial (`cpl`) resolution check on the
   `frac_p_abs`/`ratio_k`/`frac_contrast` channel — undischarged three
   cycles running as of this document (exp-088, exp-089, exp-090), and
   the one item this cycle's own Idealization 9 names as bearing directly
   on this fit's own inputs (40.2°/41.4°, which set the zone's lower
   edge).
2. PHOTONICS' grazing-incidence validity check — still near-unanimous #1
   on the whole T28 board, still not run.
3. The x-wall wavelength-generality (450/750nm) leg — now **SIXTEEN**
   consecutive cycles deferred (076–090).
4. The still-queued R14(b) formal null-controlled period fit against the
   raw signed `p_abs(G40,θ)−p_abs(C40,θ)` difference.
5. A repeat/denser measurement at or near 37.2° specifically, given this
   cycle's own Q7 finding that it is simultaneously the Q3 zone's
   load-bearing upper-edge point AND a pre-existing "felt-lucky pass" —
   the single most concrete, well-motivated next FDTD call this
   sub-thread's own record now points to.
6. A retargeted bracket at 40.2°/41.4°'s own far-side "second-ring"
   neighbors (exp-089's own Next item, still open, unaffected by this
   cycle's calibration work).
