# Phase 2 Critique — VISION SCIENCE (Panel Iteration 91, exp-114)

## Charter-fit finding (independently confirmed, not assumed)

My charter is human perceptual limits — contrast thresholds, luminance
edge detection, spectral sensitivity, adaptation, temporal sensitivity,
attentional blindness — with the duty to pin numeric thresholds, cited,
BEFORE any run that scores against them. I confirmed independently,
rather than accepted on the proposal's own say-so, that **none of this
binds here**:

- Read `run114.py` and `chunk_runner114.py` in full, plus a targeted
  grep across the whole experiment directory for
  `Weber|C_thr|photopic|scotopic|Check A|Check B|Check C|named-bin|
  perceptual`. The only hits are inside `run114.py`'s own `DISCLAIMER`
  string, and every one of them is a *negation* ("no Weber-contrast or
  `C_thr(L)` perceptual scoring is performed anywhere in this
  document"; "not a named-bin classification"). No Check A/B/C
  classification machinery (`classify_resolution_check`,
  `neighbor_correlation_check`, or any successor) is imported, defined,
  or invoked anywhere in `run114.py` or `chunk_runner114.py` — §3's
  claim that this leg builds none of that machinery is true of the
  actual committed code, not merely asserted in prose.
- No `angular_scattered_pattern`/per-bin capture code exists in either
  file; `chunk_runner114.py::step_budgeted` persists only `cap`,
  `sigma_e`, and `ez` per scene. Idealization 3's "reproduction
  precondition" in §5 is correctly hedged as conditional
  ("if...invoked at all this cycle") rather than stated as a thing
  this leg will do — it will not, on the code as committed.
- No `photopic`/`scotopic` ambient regime, no `lab/ambient.py` call, no
  Tier-W/Tier-A constraint-3 language anywhere. T1/T2/T3 (my seat's own
  pinned thresholds and the switching-transient thread) are untouched;
  this cycle produces a wall-time exponent and two geometry-derived
  re-verifications, nothing a human eye could register or fail to
  register.

Verdict on charter-fit: **confirmed N/A**, independently, per the task's
own instruction not to assume it.

## Verification of the §5 falsifiable-band citation

The proposal's CONFIRM bound (≤0.15) is justified by: "matches R28's
own already-tolerated founding miss magnitude (the ORIGINAL hardcoded
exponent, 3.0, missed the real measured r=312/r=156 ratio by ≈15%
before `KAPPA_COST_EXPONENT` was fit at all)." I checked this against
LOGBOOK.md's own R28 entry directly, not the proposal's paraphrase of
it: *"`cost_gate_check()`'s own `kappa_ratio**3` term underestimated the
measured r=312/r=156 wall-time ratio by ~15% (measured 9.224×, per-scene
8.93×–9.42×, vs. projected 8.0×; effective exponent ≈3.21, not 3.00)."*
The citation reproduces this correctly — the ~15% figure is real and
correctly attributed. See "Sharpest attack," below, for what this
citation does and does not license.

## Verification of the R4-correction against Iteration 90's own queue

The proposal (§2.0, and `run114.py`'s own `DISCLAIMER`) states MATERIALS'
Iteration-90 Phase-5 review estimated the r=234 leg's cost at "~32%" of
the refused r=312 leg, and that the true, invoked figure is ≈39.8%. I
checked this against LOGBOOK.md's own Iteration-90 entry, not just the
cited review file: the **Reconciled Iteration-91 queue**, written by
Red Team, states item 3 verbatim as "a cheaper intermediate-`r` (`r=234`,
**~32%** of this cycle's own refused-leg cost) calibration point" — so
the "~32%" figure genuinely reached a permanent record, not merely one
seat's own review draft. Independently invoking the actual formula
(`(1.5**3.2053299988171697)/(2.0**3.2053299988171697)`) gives
`0.397677`, i.e. ≈39.8%, not ≈32% — I recomputed this myself rather than
trusting `run114.py`'s own printed figure, and it matches. This is a
real, disclosed R4-class citation discrepancy, correctly caught and
non-outcome-reversing (r=234 remains the cheaper option either way).

## Phase 2 — required format

**Steel-man (≤150 words).** This cycle is honestly and narrowly scoped:
instrument-calibration/cost-gate work, with T1 confirmed N/A by direct
code inspection, not by trusting its own disclaimer — no σ(I)/σ(x,t)/
angular-selectivity/sub-threshold content, no Weber-contrast or
`C_thr(L)` scoring, and no Check A/B/C classification machinery
anywhere in the committed `run114.py`/`chunk_runner114.py`. It correctly
keeps the cost exponent (`KAPPA_COST_EXPONENT`) separated from the
unrelated `shape_ratio_fixedabs` physics exponent (Idealization 4) and
from R5's own unrelated ruled-out `r≈234` coincidence (Idealization 5).
It stays R31-gated — `chunk_runner114.py::check_cost_gate_for_r234`
raises rather than proceeding without a fresh same-session control,
exactly the discipline that caught a real would-have-been overspend in
exp-113. Its own R4-correction of MATERIALS' Iteration-90 estimate
(32%→39.8%) is independently invoked, not hand-typed, and traces to a
real figure in the permanent Iteration-91 queue text, not a straw
citation.

**Sharpest attack (≤150 words).** The 0.15/0.30 CONFIRM/REFUTE bands for
the kappa-ratio-generalization check are justified by citing R28's own
~15% figure — a citation I verified is accurate. But the *inference*
built on it is not: R28's 15% measures how far an **un-fit, round-number
guess** (`exponent=3.0`, chosen before any data existed) missed the
**single** data point `KAPPA_COST_EXPONENT` was later fit from. Using
that number to bound how far the **properly-fit** exponent
(`3.2053...`, fit specifically to minimize error at that one point) may
now miss a **different** point (a new kappa_ratio) conflates a prior-guess
error with a fitted-model generalization error — two different
quantities that happen to share a "~15%" label. The 0.15/0.30 split may
still be a reasonable convention, but it is not "not an arbitrary round
number" for the reason stated; it should be disclosed as a house
convention (R5/R30's own "disclosed, not derived" standard), not
implied to be principled by the R28 citation.

**Verdict: support-with-changes.**

**Parameter change that would flip to unqualified support:** reword
§5's justification of the 0.15/0.30 bands to state plainly that they
are a disclosed house convention carried over from an unrelated
quantity's (the un-fit exponent's) historical miss magnitude — not a
statistically derived bound on `KAPPA_COST_EXPONENT`'s own cross-ratio
generalization error. No numeric change to the bands themselves is
needed; only the framing. This does not gate Phase 4 (the cost-gate/R31
machinery is unaffected) and does not touch any constraint-3/4 verdict,
so it is non-blocking, but it is a real, checkable defect in how the
falsifiable bands are justified, distinguishing "this citation is
accurate" from "this citation licenses this specific bound."

## Trust suite

See the report to the Director for the confirmed result (run
independently in this session).
