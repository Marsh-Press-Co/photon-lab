# PHASE 4 — RESULTS · Panel Iteration 55 · exp-078

Checked against `phase3_synthesis.md` §3's frozen predictions, committed
BEFORE the corrected `y_wall_prescreen.py` was executed.

## 1. Corrected script re-run — every frozen number CONFIRMED

`y_wall_prescreen.py` (mandatory-fix docket items 1–3 folded in) was
executed end to end (`y_wall_prescreen_output_phase4.txt`,
`y_wall_prescreen_results.json`).

| Frozen prediction | Actual (Phase 4) | Status |
|---|---|---|
| `C80−C40`: `P*≈4.0000°` (at search boundary, every widened stage to 60°), `rel_dev≈0.4074` → INCONCLUSIVE | `P*=4.0000°` (at boundary: `narrow[1,4]→wide[1,15]` `R²=0.9535`, `→widest[1,60]` `R²=0.9693`), `rel_dev=0.4074` → INCONCLUSIVE | **CONFIRMED, exact** |
| `PAIR_ABSORB40`: `P*≈2.8045°`, `rel_dev≈0.3284` → INCONCLUSIVE | `P*=2.8045°`, `rel_dev=0.3284` → INCONCLUSIVE | **CONFIRMED, exact** |
| `PAIR_PAD`: `P*≈3.2180°`, `rel_dev≈0.3021` → INCONCLUSIVE, essentially unmoved | `P*=3.2180°`, `rel_dev=0.3021` → INCONCLUSIVE | **CONFIRMED, exact** |
| Corrected summary: 0/3 SUPPORT, 0/3 REFUTE | `0/3 comparisons REFUTE; 0/3 SUPPORT` | **CONFIRMED, exact** |
| Gate re-run at 48°–54°: all three PASS, worst `|r|=0.0386` | `G-LOSSLESS` worst `3.331e-16` PASS; `G-N1` worst `2.701e-15` PASS; `G-PASSIVITY` worst `|r|=0.038583` PASS | **CONFIRMED, exact** |
| `x_wall_rederivation_validation`/`shared_damping_formula_check`: unchanged, bit-exact | `C40` `|dev|=1.776e-15°`, `C80` `|dev|=0.000e+00°`; `worst_abs_diff=0.0` | **CONFIRMED, exact — unaffected by the fix, as predicted** |

**A fifth independent computation** (after EM's/MATERIALS'/THERMODYNAMICS'
own spot-checks and Red Team's own from-scratch
`phase2_redteam_angle_correction_check.py`) — the single committed
`y_wall_prescreen.py`, now permanently folded-in — reproduces every
number exactly. No disagreement; per §3's own house discipline, the
frozen numbers were a check on this run's arithmetic, and the check
passes cleanly across the board.

## 2. Fresh 20,000-trial null-calibration (mandatory-fix docket item 6) —
directional prediction CONFIRMED

`phase4_null_calibration_corrected.py`, targeting the now-corrected
`y_wall_prescreen_results.json` at the house 20,000-trial standard (not
QUANTUM's own Phase-2 2,000-trial reduction, and not targeting the
as-filed, wrong-angle model QUANTUM's control tested):

| Per-target | `P(null rel_dev≤0.30)` | `P(null rel_dev≤observed)` | `P(null R²≥observed)` |
|---|---|---|---|
| `c80_c40` (observed `rel_dev=0.4074`) | `0.2635` | `0.3960` | `0.2126` |
| `pair_pad` (observed `rel_dev=0.3021`) | `0.1242` | `0.1258` | `0.6465` |
| `pair_absorb40` (observed `rel_dev=0.3284`) | `0.1542` | `0.1744` | `0.8344` |

None of the three corrected comparisons' own `rel_dev`/R² are
distinguishable from pure i.i.d. noise at the conventional 0.05
significance level — every `P(null ≤ observed)` and `P(null R²≥observed)`
value is far above `0.05`.

**Joint check**: distribution of #SUPPORT-out-of-3 (`rel_dev≤0.30`) under
pure noise: `{0: 0.5426, 1: 0.3737, 2: 0.0788, 3: 0.0049}`. `P(≤0 of 3
SUPPORT under null) = 0.5426` — the observed corrected-model outcome
(0 of 3) is, itself, an entirely unremarkable result under a null with no
relationship to reality (it is the single most common outcome, occurring
in over half of pure-noise trials).

**Prediction match**: `phase3_synthesis.md` §3 predicted (as a directional
call, explicitly not a precise number, since this was genuinely new
information) that the fresh control would show the corrected numbers "not
statistically distinguishable from pure noise... reinforcing, not
undermining, the corrected 0/3-SUPPORT INCONCLUSIVE reading." **CONFIRMED
in direction and magnitude** — nothing in this control moves the verdict
toward REFUTE or SUPPORT; it closes the one open question Red Team's audit
flagged as "not yet run" (whether the corrected numbers are themselves
informative, independent of the period-band threshold alone).

## 3. Remaining docket items

- **Item 5** (rewrite `phase1_proposal.md` §5.2/§5.3/§7 around the
  corrected numbers): applied directly to `phase1_proposal.md` — original
  text retained, struck through/labeled superseded, corrected replacement
  text added inline, per house convention for a Phase-3-fix-driven
  rebuild (exp-077's own precedent).
- **Item 7** (QUANTUM's docstring/print `n_trials` mismatch): applied to
  `phase2_quantum_null_check.py` (three spots corrected: module docstring
  ×2, one runtime print header; the disclosed runtime NOTE was already
  correct and untouched).

**All seven mandatory-fix docket items are now closed.**

## 4. Combined result for this cycle

**exp-078's own official result: the y-direction (transverse-normal) wall
echo mechanism's closed-form period pre-screen is INCONCLUSIVE, Test-A-only
reading — 0/3 comparisons SUPPORT, 0/3 REFUTE, under the geometrically
correct angle.** The as-filed document's apparent partial support (2/3
SUPPORT) was entirely an angle-convention artifact, caught and closed
before it could be cited past Phase 2. A fresh, house-standard
null-calibration control confirms the corrected numbers carry no
statistically distinguishable signal in either direction. `PAIR_PAD`
(T28's own actual dominant empirical target) was never close to SUPPORT
under either angle convention and is the cycle's most load-bearing single
number: `rel_dev=0.3021`, just barely over the 0.30 SUPPORT bar, and not
distinguishable from chance (`p=0.13`).

**This does not close the y-wall echo mechanism class** (no comparison
reaches REFUTE either), but it substantially lowers the case the as-filed
Phase-1 document made for building the full y-mirrored coherent
propagator — the honest reading is that a period-only pre-screen of this
mechanism class, done correctly, finds nothing encouraging enough to
justify that build, not "survives with caveats." Full record: this
directory; Phase 5 (six blind reviews + Red Team's final audit) next.
