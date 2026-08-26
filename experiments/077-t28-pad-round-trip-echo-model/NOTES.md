# exp-077 — T28 `PAD` Round-Trip-Distance Echo Model Refit

**Panel Iteration 54.** Lead: VISION SCIENCE (by rotation). Director
synthesis post Phase 2 (five blind critiques + Red Team's Phase-2 audit,
verdict **PROCEED-WITH-MANDATORY-FIXES, 5-item docket, ALL 5 items
ADOPTED, ZERO overridden** — full record in `phase1_proposal.md`,
`phase2_critique_{em,materials,photonics,quantum,thermodynamics}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`).

## Mandate

LOGBOOK.md's Iteration-53 (exp-076) Tier-0 #1 queue item, ranked by Red
Team's Phase-5 final audit (EM's own #1 pick, seconded by THERMO): refit
exp-075's already passivity-gated (G-LOSSLESS, G-N1, G-PASSIVITY)
single-wall transfer-matrix echo model against `PAD`'s round-trip
distance instead of `ABSORB` depth — the ONLY mechanism class exp-076's
own lossless-vacuum proof (`PAD` is provably lossless vacuum, per
`lab/fdtd2d.py`'s damping-mask construction depending only on `absorb`,
never `nx`/`ny`/`pad`) leaves physically permitted for T28's dominant
`PAIR_PAD` signal (`amp_ratio=0.119`, HIGH). Zero new FDTD calls.

## Hypothesis

`PAIR_PAD ≡ (C40,G40)` holds `ABSORB` fixed at 40 for both configs, so
`r(theta;ABSORB=40)` is identical for both — any predicted difference
from exp-075's coherent single-wall echo model must come purely from the
image-source round-trip DISTANCE changing (`PLANE_X` 77→117, the literal
meaning of "PAD's round-trip distance"). If this specific mechanism
explains the dominant `PAIR_PAD` signal, the model's predicted `delta
(theta)` should match the real one in period and shape. `PAIR_ABSORB40 ≡
(G40,C80)` is the geometry-fixed control (same `PLANE_X`, different
`ABSORB`).

## Setup

Reuses committed machinery programmatically throughout (R4 discipline):

- **Geometry**: `experiments/065-.../design_geometry.py::CONFIGS["C40"/
  "G40"/"C80"]`.
- **Reflectance/gates**: `experiments/075-.../boundary_reflectance.py`
  (`n_profile_exact`, `reflection_coefficient`, `gate_lossless_
  unimodular`, `gate_single_layer_identity`, `gate_passivity`).
- **Two-wall extension** (mandatory fix 1): `experiments/075-.../
  two_wall_cavity.py::image_geometry_right`/`c_empty_two_wall`.
- **Period fitting**: `experiments/069-.../run.py::_free_period_search`/
  `_fixed_period_fit`.
- **Real data**: `experiments/076-.../results.json::headline` (31 angles,
  36–42°, 0.2° step, 600 nm, settled `STEPS=2800`, already-collected FDTD
  data — no new run needed).
- **Pre-registered bands**: reused verbatim from exp-075's own
  `phase1_proposal.md` §5 (period `rel_dev` ≤0.30 SUPPORT />1.00 REFUTE;
  shape `r²` ≥0.30 SUPPORT/≤0.05 REFUTE).

## Result

**Combined REFUTE for BOTH `PAIR_PAD` and `PAIR_ABSORB40`, on the complete
(two-wall) instrument — confirmed four independent ways** (PHOTONICS' and
ELECTROMAGNETISM's Phase-2 from-scratch retargets, Red Team's Phase-2
audit, this Phase-4 re-run; all agree to 4 decimal places):

| | `PAIR_PAD` | `PAIR_ABSORB40` |
|---|---|---|
| Single-wall Test A | `rel_dev=1.8798` REFUTE | `rel_dev=0.9642` INCONCLUSIVE |
| Single-wall Test B | `r²=0.0444` REFUTE | `r²=0.1997` INCONCLUSIVE |
| Single-wall Combined | REFUTE (period-driven) | INCONCLUSIVE |
| Two-wall Test A | `rel_dev=0.8797` INCONCLUSIVE | `rel_dev=0.6851` INCONCLUSIVE |
| Two-wall Test B | `r²=0.0001` REFUTE | `r²=0.0418` REFUTE |
| **Two-wall Combined (final)** | **REFUTE** (shape-driven) | **REFUTE** (flipped) |

Gates re-verified: G-LOSSLESS `2.220e-16`, G-N1 `1.404e-15`, G-PASSIVITY
worst `|r|=0.006423` — all PASS, bit-identical single- vs. two-wall (the
gates test the transfer-matrix code itself, independent of wall count).

Null-calibration appendix (mandatory fix 5, 20,000-trial pure-noise null +
20,000-trial bootstrap ground-truth recovery on `PAIR_PAD`'s real curve):
`P(R²≥0.70)=0.00000` under pure noise (max `R²=0.5609` over 20,000
trials) vs. real `R²=0.8165` — the REFUTE verdict is not a look-elsewhere
artifact; the real data's own fitted period is stable under realistic
bootstrap noise (100% of resamples land within 20% of the true period).

## Learned

**CORRECTED (Phase-5 Red Team final audit, §2a/§4 item 1) — the claim
below originally read "the coherent-echo mechanism class now doubly
excluded... no known mechanism class remains untested." That overstated
what this cycle actually showed. The scoped, correct statement:**

**The x-normal (near + far wall) coherent-echo mechanism, instantiated
with the unrealizable matched-`eps=mu` admittance, is REFUTEd against
T28's dominant `PAD`-tied signal — on both the single-wall and complete
two-wall cuts.** This is exp-076's own lossless-vacuum proof's one
mechanism class this SPECIFIC instantiation was permitted for, now tested
on its most complete cut and killed. The REFUTE is more robust, not less,
for resting on different tests in each cut (single-wall: period;
two-wall: shape) — two structurally different failure modes, not one
repeated finding. Materials realizability (verified in code,
`verify_symmetric_damping`): the `+x` wall shares the `-x` wall's
identical unrealizable matched-`eps=mu` admittance class — a two-wall
SUPPORT, had it occurred, would not have been materials progress either.

**Four concrete, unpriced candidates remain, per the Phase-5 final
audit's own independent confirmation** — the coherent-echo mechanism
CLASS is not closed, only this one instantiation of it: (1) a **y-direction
(transverse) wall echo** — a structurally distinct boundary configuration
whose standoff (`clear_span_y`: 0/40/0 for C40/G40/C80) tracks `PAD`
exactly, invisible to this cycle's own 7-field geometry-congruence
assertion, never modeled by exp-075 or exp-077; (2) a **realizable**
(`mu_r=1`) admittance instantiation of the SAME x-wall mechanism —
confirmed to move `|r|`/`arg(r)` by 15–40%/15–24°, never fit against
Test A/B; (3) a **Yee-grid numerical-dispersion-corrected** version of the
same x-wall model (vacuum `c` was used for the round-trip phase; the
engine's own discretized phase velocity never substituted in); (4) the
two-wall's own 600nm REFUTE does **not** survive unchanged at 750nm (a
spot-check flips it to INCONCLUSIVE, though without its own
null-calibration control — see below). **A Checkpoint-2 "mechanism board
exhausted" reading is explicitly NOT yet ripe** (Phase-5 Red Team final
audit, ruled directly, criterion 2 does not fire).

**T28's own substantive mechanism question — the ~2.84° periodicity's
ultimate origin — remains open**, narrowed this cycle toward "not an
x-normal, unrealizable-admittance echo" specifically, not toward "no
mechanism remains."

## Next

Reconciled Iteration-55 ranking (Phase-5 Red Team final audit §6, all six
seats + audit, 4 tiers, 10 items — full detail `phase5_redteam_audit.md`
§6). **Tier 0, zero FDTD, run as one batch:** (1) correct LOGBOOK's T16
"24×" framing (trivial, two cycles overdue — see the Checkpoint-4 entry
this cycle fires); (2) a closed-form period pre-screen of the y-direction
wall echo (PHOTONICS/EM's independently-convergent #1, with EM's own
caution that its natural reference length matches T21's already-refuted
fringe — may desk-close in under an hour); (3) the realizable-admittance
refit using `graded_black_shell`'s real profile (MATERIALS #1, the only
pending test that can move the realizability bound); (4) gate the
already-collected 750nm two-wall spot-check with its own properly-sized
null and decide; (5) the Yee-grid-dispersion-corrected re-score (VISION's
new candidate); (6) harden the null-calibration appendix further per any
remaining gaps. **Tier 1, cheap FDTD:** (7) the full-width non-aliased
second-wavelength `G40` leg (the standing precondition, deferred twice
now); (8) broadband pulsed reflectance spectroscopy. **Tier 2:** (9) test
whether `PAD`-sensitivity survives with a real absorbing article loaded
(deferred twice, should not be deferred a third time without an explicit
reason). **Tier 3:** (10) this cycle's own 7-item record-hygiene docket
(`phase5_redteam_audit.md` §4).
