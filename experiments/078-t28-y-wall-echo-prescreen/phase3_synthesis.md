# PHASE 3 — SYNTHESIS · Panel Iteration 55 · exp-078

**Director's synthesis.** Per PANEL.md, the Director does not vote in Phase
2 and states here which criticisms are accepted and which are overridden.

## 1. Disposition of Phase 2

Five blind Phase-2 critiques (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS,
QUANTUM OPTICS, VISION SCIENCE — PHOTONICS correctly absent as this cycle's
rotation lead), all `support-with-changes`. Red Team's Phase-2 audit
(`phase2_redteam_audit.md`): **PROCEED-WITH-MANDATORY-FIXES, 7 items, zero
overridden.** Red Team independently re-derived the load-bearing defect
from first principles (the bench's own stated propagation direction and
`reflection_coefficient`'s own docstring, not from any critique's stated
conclusion), then went beyond all three critics that found it by running a
full corrected re-score of the entire primary model and a gate re-run at
the corrected angle envelope — neither of which any of the three critiques
committed to the record themselves.

**Accepted, in full — nothing overridden.** Red Team's audit independently
re-verified every load-bearing claim from all five critiques (the
angle-convention defect, three ways; VISION's precision-recomputation
claim, reimplemented from scratch in `mpmath`, not merely re-checked;
QUANTUM's null-calibration figures, cross-checked script-to-JSON-to-output)
before ruling, and found no critique overreached. The Director has no basis
to override anything Red Team already checked by hand.

## 2. The seven mandatory fixes, as executed

1. **Folded the angle correction into `y_wall_prescreen.py` itself**, as
   the primary, pre-registered computation. Added `y_wall_incidence_angle
   (theta_deg) = 90.0 - theta_deg`, and threaded a `use_corrected_angle`
   flag (default `True`) through `edge_image_phase_difference`/
   `edge_image_curve` so every downstream primary-model computation (Sec
   [4]–[5]) now uses the corrected angle by construction. Reused Red
   Team's already-verified `phase2_redteam_angle_correction_check.py`
   pipeline as the reference implementation rather than re-deriving a
   fifth time. [Attack 1]
2. **Kept the as-originally-filed (incorrect) numbers as an explicitly
   labeled audit-trail row**, not deleted: new Sec [5b],
   `use_corrected_angle=False`, printed side-by-side against the
   corrected primary scores, captured in
   `out["as_filed_incorrect_audit_trail"]`. [Attack 1, docket item 2]
3. **Added the gate re-run at the corrected 48°–54° envelope** as new Sec
   [7] (`gate_lossless_unimodular_range`/`gate_single_layer_identity_range`/
   `gate_passivity_range`, reused near-verbatim from Red Team's own
   already-run, already-clean check) — now a hard `assert` in the script
   itself (a corrected-angle result is not trusted unless this passes
   every run, not merely once in an audit file). [Attack 2]
4. **Correcting the "near-noise-floor"/"float noise" framing**: confirmed
   this language exists only in `phase1_proposal.md` prose (§5.2/§7), not
   in the script itself — no script fix needed here; the prose fix lands
   in fix 5's rewrite below. [Attacks 3–4]
5. **`phase1_proposal.md` §5.2/§5.3/§7 rewritten** around the corrected
   numbers as primary, the as-filed numbers demoted to an explicitly
   labeled comparison row, and the false "near-noise-floor" framing
   replaced with THERMODYNAMICS' physical (not numerical) caution — see
   §3 below for the frozen replacement language, applied to the write-up
   after Phase 4 confirms the corrected script reproduces it. [Attacks
   3–4]
6. **A fresh 20,000-trial null-calibration control against the corrected
   model** — `phase2_quantum_null_check.py`'s structure retargeted at the
   corrected `rel_dev`/R² values (which Phase 4 will produce), at the
   house standard trial count (QUANTUM's own Phase-2 pass used 2,000 as a
   disclosed time-budget reduction; this is new information the as-filed
   control could not answer, since it targeted the wrong model). Runs as
   part of Phase 4, after the corrected numbers exist. [Attack 6]
7. **One-line fix**: `phase2_quantum_null_check.py`'s module docstring
   ("20,000-trial") corrected to match its actually-executed
   `n_trials=2000`, bundled as record hygiene. [Attack 5]

## 3. FROZEN PREDICTIONS — committed before Phase 4's re-run of the
corrected script

Red Team's own `phase2_redteam_angle_correction_check.py` already computed
the fully corrected primary-model pipeline independently (a fourth
from-scratch implementation, after EM's/MATERIALS'/THERMODYNAMICS' own
spot-checks). Per house discipline (predictions committed BEFORE any run),
the Director states here the expected outcome of the now-folded-in fix
(§2 item 1) as it will run inside the single committed `y_wall_
prescreen.py`, BEFORE executing it as Phase 4, so that Phase 4 is a
confirmation, not a first look:

- **`C80−C40`**: as-filed `P*=3.2105°, rel_dev=0.1296` → **SUPPORT**;
  corrected `P*=4.0000°` (at the search boundary at every widened stage,
  `narrow[1,4]→wide[1,15]→widest[1,60]`, R² climbing to an implausible
  `0.95`–`0.97` — the "no well-constrained period" diagnostic this file's
  own `free_period_with_widening` already flags), `rel_dev≈0.4074` →
  **INCONCLUSIVE**. This comparison's corrected model has **no interior-
  optimum period** in the window this instrument can resolve at all.
- **`PAIR_ABSORB40`**: as-filed `P*=3.2030°, rel_dev=0.2330` → **SUPPORT**;
  corrected `P*≈2.8045°, rel_dev≈0.3284` → **INCONCLUSIVE**.
- **`PAIR_PAD`** (T28's own actual dominant empirical target): as-filed
  `P*=3.1654°, rel_dev=0.3136` → INCONCLUSIVE; corrected `P*≈3.2180°,
  rel_dev≈0.3021` → **INCONCLUSIVE, essentially unmoved** — expected,
  since `C40`/`G40` share `ABSORB=40` and hence the identical `r(θ;40)`
  value enters both terms of the difference under either angle
  convention, so this comparison cannot (and does not) move materially.
- **Corrected summary: 0/3 SUPPORT, 0/3 REFUTE** (down from the as-filed
  document's 2/3 SUPPORT). **Both nominal SUPPORT verdicts were entirely
  an angle-convention artifact.**
- **Gate re-run at 48°–54°** (new Sec [7]): expected to PASS cleanly on
  all three (G-LOSSLESS, G-N1, G-PASSIVITY) — the gates test the
  transfer-matrix code itself, not which angle it is queried at, and Red
  Team's own audit already ran this exact check (worst `||r|-1|=3.3e-16`,
  worst `|r_loop-r_direct|=2.7e-15`, worst `|r|=0.0386`, all well inside
  their pass bars).
- **`x_wall_rederivation_validation` (Sec [2]) and `shared_damping_formula_
  check` (Sec [0])**: unaffected by this fix (neither calls
  `reflection_coefficient` with a config-swept angle argument in the
  affected code path) — expected to reproduce bit-exact, unchanged from
  the as-filed run (`|dev|≤1.8e-15°`, `worst_abs_diff=0.0`).

**If Phase 4's actual re-run of the corrected, single committed script
disagrees with any number above by more than rounding, that disagreement
itself becomes the headline finding of this cycle** (a fifth independent
computation — after EM, MATERIALS, THERMODYNAMICS' spot-checks and Red
Team's own from-scratch script — disagreeing with all four prior ones
would be far more newsworthy than another confirmation) — the frozen
numbers are not a target to reach, they are a check on Phase 4's own
arithmetic.

**Fresh null-calibration (fix 6, house 20,000-trial standard) — directional
prediction, not a precise number** (this is genuinely new information;
Red Team's audit explicitly scoped it as "not yet run"): the corrected
`rel_dev` values (`0.30`–`0.41`) are, if anything, *slightly worse*
(farther from zero) than the as-filed values that already scored `p=0.080`
under a 2,000-trial null (QUANTUM's Phase-2 control, targeting the WRONG,
as-filed model). Expect the corrected model's own null-calibration to show
these `rel_dev`/R² values are **not** statistically distinguishable from
pure noise at the conventional 0.05 level either — i.e., this check is
expected to *reinforce*, not undermine, the corrected 0/3-SUPPORT
INCONCLUSIVE reading, not manufacture a REFUTE or SUPPORT that the period
band itself does not already show. If the fresh 20,000-trial run instead
shows the corrected numbers ARE distinguishable from chance in either
direction, that is itself the more informative result and will be reported
as such, not fitted to this prediction.

## 4. T1 / Checkpoint disposition, carried from Phase 2

**T1 escape route: N/A**, unchanged — instrument/model-fidelity thread,
constraint 3 not engaged throughout (Red Team's audit confirms this
explicitly; re-confirmed here). **No Checkpoint criterion fires at Phase
3**: Red Team's audit ruled, and this synthesis independently agrees, that
criterion 4 does not fire — every gap Phase 2 raised was caught and a
correction computed before this freeze, matching the program's own
established non-firing pattern (exp-076/077 precedent, both cited by Red
Team). **Should Phase 4 fail to reproduce any frozen number above, or
should any future write-up (this cycle's own corrected `phase1_
proposal.md`, a future LOGBOOK entry, or Iteration-56's own ranking) repeat
the as-filed "2 of 3 SUPPORT" framing after this synthesis and Red Team's
audit both exist, that would be a fresh, squarely-on-point Criterion-4
firing** — the entire point of writing the correction and the prediction
down now, in the same place, before either could quietly diverge.

## 5. What Phase 4 will do

Execute the now-corrected, single committed `y_wall_prescreen.py` end to
end; compare every number against §3's frozen predictions; run the fresh
20,000-trial null-calibration control (fix 6) against the corrected
`rel_dev`/R² values it produces; apply the one-line docstring fix (fix 7)
to `phase2_quantum_null_check.py`; write `phase4_results.md` stating
CONFIRMED/NOT CONFIRMED per prediction; and rewrite `phase1_proposal.md`
§5.2/§5.3/§7 (fix 5) with the corrected numbers as primary and the
as-filed numbers demoted to an explicitly labeled comparison row, per
house convention for a Phase-3-fix-driven rebuild (exp-077's own
precedent for this exact situation).
