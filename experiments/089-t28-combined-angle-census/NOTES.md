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

**Carried idealizations banner** (Phase-2 fix item 1, MANDATORY dual-
section requirement per the Iteration-65 CHECKPOINT): every finding
restated below is governed by Idealizations 9-10 (NETD is not a
human-eye threshold; this cycle does not test constraint 1/2/3/4) and
Idealization 16 (FLOOR/RMS are `graded_black_shell`/600nm-specific).
This is the second consecutive T28 cycle (after exp-088) to carry this
banner independently at both the Predictions and Result sections — the
exact discipline the Iteration-65 CHECKPOINT existed to install.

All house gates PASS. **P1 (vacuum footprint): PASS**, both configs.
**P2 (reproduction): PASS**, `max_dev=0.0` exactly. **P4 (`xi_ext`):
PASS**, `≤3.69×10⁻⁴` everywhere (well inside `≤0.12`). **Non-negativity
gate: PASS**, `sigma_abs≥0` at all 12 cells. **R14(a) smoothness gate:
PASS** — `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)` are each strictly
non-decreasing across the entire combined 8-point sorted angle list
(36.0°→41.8°), with no step failing its own noise-floor tolerance — the
parent-quantity smoothness R14(a) requires is confirmed, not merely
assumed. 12 FDTD calls, 150.4s wall time — matches the frozen budget
exactly.

**Idealization 15 self-check bug, disclosed rather than silently
corrected:** the printed `back_frac/fwd_frac read in this file: True`
line is a **false positive** — direct inspection (not the naive
in-file substring search `run.py` actually ran) shows the only three
occurrences of the strings `"back_frac"`/`"fwd_frac"` in `run.py` are
the check's own comment, its own print statement, and its own
persisted-key name — none is an actual read of `w["back_frac"]` or
`w["fwd_frac"]` off any `widths_direction_corrected()` return value.
The substantive Idealization-15 claim ("not read anywhere in this
cycle's own scored quantities") is confirmed true by manual grep for
the subscript patterns `back_frac"]`/`fwd_frac"]`/`.back_frac`/
`.fwd_frac`, which find zero matches — but the automated check that
was supposed to verify this (Phase-2 fix item 9) is itself buggy
(a naive self-referential string search), and its printed `True` must
not be read as confirming the hazard it claims to check. Flagged for
Phase 5.

**Q1 (desk, R13 floor gate): CONFIRMED exactly as predicted, no
surprise.** All three new angles clear: 37.2° (2.1709× FLOOR), 40.2°
(1.4764× FLOOR), 41.4° (1.3095× FLOOR) — bit-exact to the frozen desk
prediction, as they must (zero new FDTD needed to score this).

**Q2 (preconditions): CONFIRMED.** All PASS, as predicted.

**Q3 (PRIMARY, `ratio_k` at the three new census angles): the
predicted CONSISTENT lean CONFIRMED at 37.2°, DECISIVELY MISSED at
40.2° and 41.4° — the single most consequential possible outcome this
document named, materializing at BOTH lowest-confidence angles at
once (Idealizations 9-10, 16 apply).**

| θ | frac_p_abs | frac_contrast | ratio_k | resolved margin | outcome |
|---|---|---|---|---|---|
| 37.2° | 1.433×10⁻³ | 4.163×10⁻⁴ | **3.443** | 1.046× (thinnest ever) | CONSISTENT — in predicted [1.5,9.0] band |
| 40.2° | 7.100×10⁻³ | 2.831×10⁻⁴ | **25.08** | 2.087× | **ENERGY-DOMINANT** — `>RATIO_HIGH=10` |
| 41.4° | 7.233×10⁻³ | 2.511×10⁻⁴ | **28.81** | 4.685× | **ENERGY-DOMINANT** — `>RATIO_HIGH=10` |

37.2° lands within its predicted band, but with the thinnest
noise-floor resolved-margin (1.046×) this sub-thread has ever accepted
as `resolved=True` — barely above the gate's own pass line, disclosed
here rather than glossed over as a clean confirmation. **40.2° and
41.4° both read `ratio_k≫10` while formally clearing R13's floor gate**
at 1.4764× and 1.3095× FLOOR respectively — exactly the outcome §6's
own Q3 text named as "the single most consequential possible outcome
of this cycle," now realized at both angles simultaneously, not one.

**Q4 (periodicity-recurrence REPORT, descriptive only — not scored,
per Idealization 13): the raw numbers do not resemble a recurring dip.**
`frac_p_abs(40.2°)=7.100×10⁻³` sits close to (moderately above) the
"smooth trend" desk estimate (`6.543×10⁻³`) that Idealization 13 named
as unreliable — not near `frac_p_abs(38.4°)=1.304×10⁻³`'s own dip.
`frac_p_abs(41.4°)=7.233×10⁻³` likewise sits close to its own smooth-
trend estimate (`7.046×10⁻³`), not near `frac_p_abs(38.8°)=5.955×10⁻³`.
Correctly not scored as CONFIRM/REFUTE (the decision this document made
before seeing this data) — reported here only as description: whatever
drove Q3's ENERGY-DOMINANT reading at these two angles, it does not
present as the periodicity-inheritance dip PHOTONICS hypothesized at
exp-088. **Per Idealization 13, this report is NOT evidence about
whether Q3's ENERGY-DOMINANT finding at the same angles is real physics
or an artifact — the two questions remain logically decoupled.**

**Q5 (the floor-gate-adequacy prediction — the sharpest test this
cycle registered): CONFIRMED — the gate is not fully protective at
this margin.** Both 40.2° (1.4764× FLOOR) and 41.4° (1.3095× FLOOR)
read `ratio_k>RATIO_HIGH=10` while floor-clearing. This is a genuinely
new instrument-calibration finding: `FLOOR_FRAC=0.10`, adopted one
cycle ago (R13, Iteration 64) and applied here for the first time to
points below 2× margin, does not reliably exclude ENERGY-DOMINANT
misclassification down to at least 1.31× FLOOR. **Whether the correct
fix is tightening `FLOOR_FRAC`, a graduated caution zone instead of a
binary gate, or something else is explicitly left to Phase 5 — this
document does not pre-judge it** (Idealization 16).

**Q6 (combined 8-point classification): the predicted CONSISTENT
reading FLIPS to ENERGY-DOMINANT.** `n_resolved=7/8` (38.6° excluded
`NODE-UNRESOLVABLE` by construction), combined ratios `[2.642, 3.443,
0.908, 3.873, 25.08, 28.81, 5.71]` — two angles (40.2°, 41.4°) trigger
`classify_resolved`'s own any-X veto priority, exactly the mechanism
that drove exp-087's original filed ENERGY-DOMINANT result. **This is a
SECOND and THIRD floor-clearing ENERGY-DOMINANT angle — not one isolated
node (38.6°, already excluded by R13) but two more, both sitting within
0.061–0.065° of a real `delta_scene` zero-crossing (the closest available
grid point to each, by this cycle's own design). The swing is,
quantitatively, ~90% attributable to the denominator continuing to
shrink toward that crossing and only ~10% to the numerator's own
ordinary, on-trend growth (decomposition below) — mechanistically an R13
(denominator, zero-crossing-proximity) story, not a new R14 numerator
anomaly and not evidence of a phenomenon distributed independently of
node proximity.** *(Corrected same-shift, Tier-0 fix item 1, Red Team's
Phase-5 final audit §2/§6 — the original text here asserted "non-
artifactual" and "away from any previously-known zero-crossing's
immediate neighborhood," which independent re-derivation from primitives
showed to be factually false: both angles are the closest grid point to
a real, already-known crossing, chosen for exactly that reason by
`phase1_proposal.md` §1's own selection rule.)* Scoped explicitly to
these 8 sampled angles only (Idealizations 9-10; not a channel-general
claim — 23 of the 31 grid angles remain FDTD-unsampled for `ratio_k`).

**Numerator/denominator decomposition (Tier-0 fix item 3, filed into the
permanent record — independently reproduced five separate ways: by
PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, and QUANTUM OPTICS' own
Phase-5 reviews, and by Red Team's Phase-5 final audit, each via a
structurally different method, agreeing to 3+ significant figures):**
holding the actual measured numerator fixed and substituting a
"typical" non-crossing-adjacent `frac_contrast` (mean of the two nearest
established CONSISTENT points, 38.8°/41.8° → 1.4005×10⁻³) collapses both
points to squarely CONSISTENT (`ratio_k`=5.07/5.17); substituting the
numerator's own pre-registered smooth-trend desk estimate while holding
the actual measured denominator fixed leaves the classification
ENERGY-DOMINANT either way (23.11 vs. actual 25.08, 7.9% off; 28.06 vs.
actual 28.81, 2.6% off). A log-decomposition against the last previously
-established point (38.8°) gives the same answer in closed form: the
`ratio_k` swing at 40.2°/41.4° is 90.6%/90.3% attributable to the
denominator's own collapse toward its zero-crossing and 9.4%/9.7% to the
numerator's own ordinary continuation.

**Q7-vs-Q3 decoupling (Tier-0 fix item 6, THERMODYNAMICS' Phase-5
finding, mirroring Idealization 13's existing Q4-vs-Q3 disclaimer):**
Q7's NETD/T9-anchor readings at these same angles (below) are computed
from the same `p_abs_w` primitives as Q3/Q6 but answer a different,
decoupled question (instrument-detectability, not energy-partition
classification) — a reader must not treat Q7's UNDETECTABLE/on-anchor
readings as corroborating or undercutting Q6's ENERGY-DOMINANT finding
at the same angles.

**Q7 (NETD/T9-anchor extension): CONFIRMED, zero marginal cost.** All
6 cells UNDETECTABLE (`dt_ss_full_K`≈4.61×10⁻⁵–5.24×10⁻⁵ K, margin
≈382×–434× against the 0.020K NETD band) — consistent with exp-087/088's
own range. `ratio_abs_ext`=0.5126–0.5151 across all 6 cells, within
0.5–1.0% of T9's established 0.51 anchor — informal context, not a
scored falsifier, as predicted. **NETD is an instrument/detector
threshold, not a human-eye one — this does NOT bear on constraint-3/4's
human-eye verdict** (Idealization 9).

## Learned (Director's own read, before Phase 5 — subject to revision)

1. **The "single-node-artifact" reading is dead — but stated correctly,
   the pattern is a node-proximity story, not evidence against one.**
   *(Corrected same-shift, Tier-0 fix item 2, Red Team's Phase-5 final
   audit §4/§6 — VISION's and PHOTONICS' independently-reached Phase-5
   finding: as originally drafted this item overclaimed. The
   margin/outcome record is a clean separation — every point at ≥2.17×
   FLOOR margin reads CONSISTENT; every point at ≤2.17× either fails the
   gate (38.6°) or reads ENERGY-DOMINANT/barely-resolved (37.2°, 40.2°,
   41.4°) — which is fully consistent with a node-proximity/floor-gate-
   calibration story at three locations, not a phenomenon distributed
   independently of zero-crossing proximity.)* exp-088 closed believing
   exactly one point (38.6°) drove ENERGY-DOMINANT and every floor-
   clearing point was CONSISTENT. This cycle's own 3 new points put two
   MORE floor-clearing points at `ratio_k` 2.5–2.9× above `RATIO_HIGH`,
   at angles that (per the decomposition above) are ~90% explained by
   the exact same R13-class denominator mechanism, now demonstrated at
   three near-crossing locations instead of one.
2. **R13's `FLOOR_FRAC=0.10` looks materially too permissive, not just
   imperfect.** Both misses happened well inside the "clears" region
   (1.31×, 1.48×) — not at the ragged edge near 1.0× where some slop
   would be expected. This is the first real evidence the gate's
   calibration, not merely its existence, needs revisiting.
3. **The proposal's own distrusted, unscored naive interpolation
   (`ratio_k≈20–28`, explicitly NOT pre-registered as a committed
   band because of documented bias) landed closer to the real measured
   values (25.08, 28.81) than the qualitative CONSISTENT lean the
   document DID commit to.** Worth Phase 5 scrutiny: was declining a
   numeric band at exactly the two angles that most needed one the
   right call, or did it (correctly) avoid a biased number while still
   under-weighting what the same biased method's DIRECTION was saying?
4. **37.2°'s own resolved-margin (1.046×) is the thinnest this
   sub-thread has ever accepted as `resolved=True`.** It happened to
   land in-band, but on a noise-floor test with almost no room to
   spare — a felt-lucky pass, not a robust one, and worth its own
   scrutiny independent of the 40.2°/41.4° story.
5. **The Idealization-15 self-check (Phase-2 fix item 9) is itself
   broken** — a naive in-file string search that matches its own
   diagnostic text. The underlying claim it was meant to verify still
   holds (manually confirmed), but the automated check should not be
   trusted or reused as written.
6. Q4's decision to report raw numbers rather than a scored
   CONFIRM/REFUTE verdict (Phase-3 synthesis, Director's choice) held
   up under real data — the raw numbers show no resemblance to the
   periodicity-inheritance dip PHOTONICS hypothesized, so a labeled
   verdict would have had to report REFUTE, but on a comparator this
   same cycle's own idealizations already flagged as unreliable. Good
   that no falsifiable claim was staked on it.

**R4/R9 registry note (Tier-0 fix item 4, record hygiene, Red Team's
Phase-5 final audit §3.4/§6):** the corrected Q6/Learned-item-1 language
above replaces an unverified absence/negation claim ("away from any
previously-known zero-crossing's immediate neighborhood," "non-
artifactual") that entered this document's own Phase-4/Result-stage
record and was independently proven false by direct re-derivation from
primitives — one placement-step more serious than the precedent this
same seat (QUANTUM OPTICS) set one cycle earlier at exp-088 (a false
"no fourth instance found" claim caught at the Phase-5-review stage,
before reaching `NOTES.md` itself). Both are logged as instances of the
same R4/R9 ("verify-before-claim," including claims of absence) registry
item; neither fired Checkpoint criterion 4 (this cycle's ruling: LOGBOOK.md
Iteration 66; exp-088's: LOGBOOK.md Iteration 65).

**MATERIALS' `FLOOR_FRAC` scoping note (Tier-0 fix item 5, before any
future recalibration is filed):** `FLOOR`/`RMS[frac_contrast]` — and any
future re-tuned `FLOOR_FRAC` value — remain specific to
`graded_black_shell`/600nm; a bare module constant carried forward by
direct-import reference, without restating this scope, risks silently
becoming a future cycle's inherited default for a different article or
wavelength.

## Next

The clearest, cheapest, most decisive follow-up this cycle's own data
demands, **retargeted per PHOTONICS' and Red Team's own Phase-5
correction**: not "isolated spike vs. broader elevated region" in
`frac_p_abs` (the decomposition above already shows the numerator is
unremarkable at both new angles) but whether `ratio_k` tracks
`1/frac_contrast` smoothly toward the true crossings (40.265°, 41.461°)
— sampling the "second-ring" ≈0.19–0.21° far-side neighbors, mirroring
38.4°/38.8°'s own comfortable-margin relationship to 38.590°. Second
priority, now backed by a clean n=7 margin/outcome separation
(misclassifications at ≤1.48× FLOOR, correct classifications at ≥2.17×):
a zero-FDTD logistic/threshold fit of `FLOOR_FRAC` against all 7 resolved
points on record (PHOTONICS' proposal, Red Team-endorsed as the single
highest-value next step) — ranked ahead of any new FDTD bracket because
it should inform how one is designed, and because Red Team's own audit
found this cycle's own suggested 0.20–0.30 replacement range is only
half-supported: 0.20 separates cleanly, but 0.30 would incorrectly
exclude 37.2°, a point this cycle's own data shows is genuinely
CONSISTENT. A binary re-tuned threshold is itself judged premature at
n=7 near-boundary points — a graduated caution zone, consistent with the
now-demonstrated continuous (not sharply-thresholded) mechanism, is the
better-supported direction. Also still open: both a temporal AND, for
the first time on this channel, a spatial (`cpl`) resolution check at
38.4° (R3's own standing meta-rule, undischarged two cycles running); the
still-queued formal null-controlled period fit against the raw signed
difference `p_abs(G40,θ)−p_abs(C40,θ)` (R14(b)); the 23 still-FDTD-
unsampled grid angles; PHOTONICS' grazing-incidence validity check; the
x-wall wavelength-generality leg (now 15 cycles deferred); `run.py`'s
R14(a) gate proxy-tolerance mismatch (EM's Phase-5 finding, non-blocking
this cycle, a real fix before third reuse).
