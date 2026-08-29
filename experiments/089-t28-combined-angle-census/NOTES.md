# exp-089 — T28 Combined Angle Census

Panel Iteration 66. Lead: VISION SCIENCE (rotation). Executes exp-088's own
Reconciled Iteration-66 queue, Tier 1 item 1 (near-unanimous #1 across
exp-088's six Phase-5 reviews): a single combined 3-angle FDTD census
answering both the denominator-side node census (the three `delta_scene`
zero-crossings never before FDTD-sampled for `ratio_k`) and the
numerator-side gap census (subdividing the two large unsampled interior
spans) at once. Full phase record: `phase1_proposal.md` (VISION SCIENCE) →
five blind Phase-2 critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS, unanimous support-with-changes, zero
overlap, two genuinely convergent pairs) → `phase2_redteam_audit.md`
(PROCEED-WITH-MANDATORY-FIXES, 9 items, zero overridden) →
`phase3_synthesis.md` (this cycle's frozen spec, all 9 fixes adopted).

## Hypothesis

exp-088 floor-gated `ratio_k` at 5 angles and found the node itself
(38.6°) NODE-UNRESOLVABLE, while 36.0°/38.4°/38.8°/41.8° all clear R13's
floor gate — but θ=38.4°'s own reading (`ratio_k=0.908`) missed its
pre-registered `[1.5,5.0]` band, revealing `frac_p_abs(θ)` is genuinely
non-monotonic in a way this sub-thread had never sampled densely enough
to see coming. `delta_scene(θ)` has three OTHER zero-crossings
(≈37.13°, ≈40.27°, ≈41.46°) that have never been FDTD-sampled for
`ratio_k` at all — only desk-derived from exp-083's scalar sweep, which
never ran the Poynting-box `widths()` machinery `ratio_k` needs. This
cycle tests: (1) whether `ratio_k` stays CONSISTENT (not
ENERGY-DOMINANT) at the three thinnest-margin points this sub-thread has
ever sent to FDTD for this metric (1.31×–2.17× FLOOR, all below any
previously-tested floor-clearing point's own 3.88× minimum); (2) whether
R13's `FLOOR_FRAC=0.10` threshold is adequately protective this close to
a crossing, or whether a floor-clearing point can still misclassify —
the sharpest test this instrument has faced since R13 was adopted.

## Setup

Reuses exp-088's own machinery (itself chaining through exp-087's and
exp-083's `run.py`) verbatim, zero geometry retyped: `_load()`/`dg`/
`build_article`/`_run_sim`, `box_for`/`ref_for`, `widths_direction_
corrected()`, `_label`/`classify_resolved()`, `frac_contrast_of`/
`compute_floor()` (R13's floor gate, unchanged — `FLOOR=1.91744×10⁻⁴`,
computed once from exp-083's own committed 31-point window, not
recomputed this cycle). New code: three new angles (θ=37.2°,40.2°,41.4°
= `dg069.DENSE_ANGLES[6]`,`[21]`,`[27]`), the NETD/T9-anchor extension at
the three new angles (Phase-2 fix item 5, reusing `p_abs_w` already
mandatory for `frac_p_abs` itself), a concrete code-executable R14(a)
parent-quantity smoothness assertion (Phase-2 fix item 8), and a raw-
number-only (not CONFIRM/REFUTE-labeled) periodicity-recurrence report
(Phase-2 fix item 4, Director's chosen path — see Idealization 13).

## Idealizations

**Carried idealizations banner** (Phase-2 fix item 1, MANDATORY dual-
section requirement per the Iteration-65 CHECKPOINT): every prediction
below is governed by Idealizations 9-10 (NETD is not a human-eye
threshold; this cycle does not test constraint 1/2/3/4) and Idealization
16 (FLOOR/RMS are `graded_black_shell`/600nm-specific) — restated inline
at each restatement below, not stated once and dropped. This same banner
opens the Result section once Phase 4 runs.

1. 3 new angles (37.2°, 40.2°, 41.4°), not the full remaining 26
   unsampled grid points — a targeted census by design (exp-088's
   Idealization 1).
2. Single λ=600nm, matching the rest of the T28 window (exp-088's
   Idealization 2, unchanged).
3. `iso_xsec_sq` area convention — object treated as compact, not an
   infinite rod (exp-087's Idealization 3, cited not re-litigated).
4. Silicon thermal constants (ρ, c_p) ASSUMED, provenance unsourced (T18)
   — reused verbatim from exp-057/087/088.
5. WitnessScenario irradiance/distance/candela WebSearch snippet-tier
   (T18), reused verbatim, not re-searched this cycle.
6. `ratio_k`'s decade tiers (0.1×/10×) remain a deliberately wide,
   first-of-its-kind falsification band, not a rigorously derived
   confidence interval (exp-088's Idealization 6, unchanged).
7. **Settling is NOT independently re-verified at 37.2°/40.2°/41.4°
   specifically.** Inherits exp-087's own STEPS=1400-vs-2800 spot-check
   at the adjacent 38.6° angle (`rel_dev(sigma_abs)=7.9×10⁻⁵`) and
   exp-083's dense-grid settling precondition at nearby angles as
   evidence STEPS=2800 is adequate — no dedicated new spot-check runs.
8. `NOISE_MULT=3.0` and `FLOOR_FRAC=0.10` remain house-style, disclosed
   choices, not formally derived statistical thresholds.
9. **NETD is an instrument/detector threshold, not a human-eye one** —
   any classification derived from `dt_ss_full_K` does NOT bear on
   constraint-3/4's human-eye verdict.
10. **This cross-check bears only on T28's own confound-mechanism
    question and constraint-3's energy-ledger bookkeeping.** It does not
    test constraints 1/2/4, and does not re-open or re-score
    `REALIZABILITY_MEMO.md`'s verdict.
11. **R14(a)'s parent-quantity smoothness check is given a concrete,
    code-executable criterion, owned by `run.py`/Phase 4 (Phase-2 fix
    item 8), not left to Phase-5 prose judgment:** `p_abs_w(C40,θ)` and
    `p_abs_w(G40,θ)` are each asserted non-decreasing across the
    combined 8-point sorted angle list, within each point's own
    `box_dev` noise floor — printed as an explicit pass/fail line.
12. **R14(c)'s half-period interior-check bound is cleared by every
    combined-set gap, but the tightest (38.8°→40.2°, 1.4°) clears it by
    only 0.02°–0.075°, AND — Phase-2 fix item 3 — this gap is NOT
    protected against a feature at `frac_p_abs`'s own demonstrated
    sub-0.4° native scale.** The only directly-measured evidence of that
    quantity's own angular structure (exp-088's 38.4°→38.6° step, a
    3.07× swing across 0.2°) argues the reverse of what the borrowed
    `delta_scene`-period yardstick implies. Named explicitly as a
    residual open span for a future cycle to further subdivide, not
    hidden inside a passing aggregate check.
13. **Q4 (periodicity-recurrence check) reports RAW `frac_p_abs` numbers
    only — NOT a CONFIRM/REFUTE-labeled periodicity-inheritance verdict**
    (Phase-2 fix item 4, Director's chosen path over Red Team's
    alternative bias-correction-plus-control-angle path — see
    `phase3_synthesis.md`). Dropped because: (a) its own naive "smooth
    trend" comparator is independently shown biased by 3.17× at the one
    point ground truth exists (QUANTUM's Phase-2 finding, confirmed and
    strengthened by Red Team — the bias-corrected null-continuation
    estimate lands INSIDE the originally-drafted CONFIRM zone at both
    angles); (b) its recurrence-pair spacing (Δθ=3.0°) sits within 1.8%
    of exact aliasing against T28's established ~2.84–2.95° period
    (EM's Phase-2 finding), so any curve carrying real fundamental-tone
    power would show apparent "recurrence" regardless of mechanism.
    **Whatever Q4 reports at a given angle is explicitly NOT evidence
    about whether any Q3 finding at the same angle is real physics or an
    artifact** (Red Team's own new §7.1 finding, adopted) — the two
    questions are logically decoupled and must not be read as mutually
    corroborating.
14. Not this cycle's mandate: Red Team's Iteration-65 ranking item 2 (the
    ~124-call full/denser individual-`σ_abs(C40,θ)`/`σ_abs(G40,θ)`
    build) remains queued, not folded in. PHOTONICS' grazing-incidence
    validity check (still near-unanimous #1 on the whole T28 board) and
    the x-wall wavelength-generality leg (now FIFTEEN consecutive cycles
    deferred, 076–089, this cycle included) remain real, overdue,
    out-of-scope items. The still-queued formal null-controlled period
    fit against the raw signed difference `p_abs(G40,θ)−p_abs(C40,θ)`
    (R14(b), Red Team's Iteration-65 Tier-2 item) also remains queued —
    Q4's raw-number report (Idealization 13) is explicitly not a
    substitute for it.
15. **The inverted `back_frac`/`fwd_frac` labels in
    `sections.py::widths()`** (flagged forward by exp-087, non-blocking)
    are re-verified by direct grep against this cycle's own committed
    `run.py`, not carried forward as an inherited assumption about
    not-yet-written code (Phase-2 fix item 9) — see Result.
16. **`FLOOR`/`RMS[frac_contrast(θ)]` are specific to
    `graded_black_shell`/600nm and must be independently recomputed, not
    numerically reused, for any other absorber article or wavelength
    this gate is later applied to** (restated from exp-088's own
    Idealization 13, MATERIALS' Phase-2 finding this cycle echoed).

## Predictions (frozen, committed BEFORE any Phase-4 code runs)

1. **Q1 (desk, zero-FDTD, R13 floor gate).** All three new angles
   predicted to **PASS**: 37.2° (2.1709× FLOOR), 40.2° (1.4764× FLOOR),
   41.4° (1.3095× FLOOR) — entirely desk-computable from already-
   committed exp-083 data, independently re-derived and confirmed exact
   by all five Phase-2 critiques and Red Team's own audit. **None is a
   comfortable margin** — all three sit below every previously-tested
   floor-*clearing* point's own range (36.0°: 3.88×; 38.4°: 7.49×;
   38.8°: 8.02×; 41.8°: 6.59°) (Idealizations 8, 16).

2. **Q2 (P1/P2/P4/non-negativity preconditions).** Predicted PASS at all
   3 new angles, both configs, both legs (12 cells total across
   BOX_A/BOX_B) — identical construction to exp-087/088's own cells,
   which cleared at margins of 5–2,500× their own tolerances. HALT if
   any precondition fails.

3. **Q3 (PRIMARY per-angle `ratio_k`, genuinely contingent on new FDTD;
   NETD/constraint-3 disclaimers apply, Idealizations 9-10; the 1.4° gap
   caveat applies, Idealization 12).**
   - **θ=37.2° — CONSISTENT, band `[1.5, 9.0]`, moderate confidence.**
   - **θ=40.2° and θ=41.4° — qualitative CONSISTENT lean only, no tight
     numeric band committed** (naive linear-interpolation central
     estimates of `ratio_k≈20–28` are explicitly distrusted, per Q4's
     own documented interpolation bias, Idealization 13). 4 of the 5
     already-measured angles read CONSISTENT; both new points sit at
     1.3–1.5× FLOOR, clear of 38.6°'s own failing 0.39×. **This is the
     lowest-confidence call in this document — a miss here (either point
     reading `ratio_k>10`) is the single most consequential possible
     outcome of this cycle** (Q5).

4. **Q4 (periodicity-recurrence report — DESCRIPTIVE ONLY, not scored;
   Idealization 13 applies in full).** `frac_p_abs(37.2°)`,
   `frac_p_abs(40.2°)`, `frac_p_abs(41.4°)` are reported as raw
   measured numbers alongside the already-filed values at 36.0°,
   38.4°, 38.8°, 41.8°. No CONFIRM/REFUTE verdict is scored against
   any threshold. **Whatever this reports is NOT evidence about
   whether Q3's finding at the same angle is real physics or an
   artifact** (Idealization 13).

5. **Q5 (the floor-gate-adequacy prediction — the sharpest test this
   cycle registers; Idealizations 9-10, 16 apply).** If either 40.2° or
   41.4° reads `ratio_k>10` despite formally clearing R13's floor gate
   at only 1.31–1.48× FLOOR, that is evidence `FLOOR_FRAC=0.10` is not
   fully protective near a zero-crossing and should be tightened or
   replaced with a graduated caution zone — a genuinely new instrument-
   calibration finding. **CONFIRM signature (gate inadequate):** any new
   angle reads `>10` while floor-clearing. **REFUTE signature (gate
   adequate at this margin):** all three new angles read `≤10`.

6. **Q6 (combined 8-point classification, contingent on Q3;
   Idealizations 9-10, 12 apply — scoped explicitly to these 8 sampled
   angles only, NOT a channel-general claim).** If Q3's CONSISTENT lean
   holds at all three new angles, the combined floor-gated `resolved`
   set across all 8 now-measured angles (36.0°, 37.2°, 38.4°, 38.8°,
   40.2°, 41.4°, 41.8° cleared; 38.6° excluded as `NODE-UNRESOLVABLE`)
   is predicted to classify **CONSISTENT** overall — extending exp-088's
   own Q5 CONSISTENT reading from 4 to 7 resolved angles. If any new
   angle reads `>10`, the combined classification flips to
   **ENERGY-DOMINANT** by `classify_resolved`'s own any-X veto priority
   — a second, floor-clearing, non-artifactual ENERGY-DOMINANT angle,
   materially undermining the single-node-artifact reading this
   sub-thread has held since exp-088.

7. **Q7 (NETD/T9-anchor extension, new angles — zero marginal cost,
   Phase-2 fix item 5; Idealization 9 applies).** `netd_disposition`
   predicted UNDETECTABLE at all three new angles, both configs —
   reusing the already-required `p_abs_w` values. `ratio_abs_ext`
   predicted in the same `0.51–0.52` band exp-087/088 measured, within
   ~1% of T9's established broadside anchor (0.51) — informal context,
   not a scored falsifier. **NETD is an instrument/detector threshold,
   not a human-eye one — this does NOT bear on constraint-3/4's
   human-eye verdict** (Idealization 9).

**R14(a) smoothness gate (hard assertion, Idealization 11 — Phase-2 fix
item 8).** `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` each predicted
non-decreasing across the combined 8-point sorted angle list, within
`box_dev` noise floor. Reported PASS/FAIL explicitly, not silently
checked.

**Non-negativity gate (hard assertion, not a scored prediction, unchanged
from exp-087/088):** `sigma_abs≥0`, `p_abs_w≥0` everywhere. HALT if
violated.

## Result
