# Phase 2 Critique — PHOTONICS (blind, independent)

*exp-094, Panel Iteration 71. Written without reading any other seat's
Phase-2 critique.*

## Steel-man (≤150 words)

The `R4` (`cpl=40`) geometry family is built with real rigor, not asserted.
I independently re-derived every listed `R4` constant from
`design_geometry.py`'s own `R3` formulas — `NX`, `NY`, `ABSORB`,
`SRC_X`, `PLANE_X`, `OBJ_X`, `TAPER`, `R_OUT`, `W_OBJ`, `GUARD_OUT`,
`W_FLANK`, `STEPS`, `PEC_R`, both box clearances, `REF_HALF_H` — all match
exactly by mechanical substitution of `R4_RATIO=2.0` for `R3_RATIO=1.5`.
The physical-length-invariance gate is genuinely an absolute identity, not
a hand-wave: `L_GEOMETRIC_M_R4 = 156·1.5e-8 = 2.34e-6` m is bit-identical
to native (`78·3e-8`) and `R3` (`117·2e-8`). `SIGMA_R4_CORRECTED =
SIGMA_NATIVE/R4_RATIO = 0.25` is the exact algebraic generalization of the
already-validated `SIGMA_R3_CORRECTED=1/3` τ_center-preservation formula.
The three census angles' predictions are honestly hedged, explicitly
citing 41.4°'s own resolution-flip history against over-trusting
"comfortable" margins rather than assuming resolution-robustness by
extrapolation.

## Sharpest attack (≤150 words)

Rank 2's comparability argument for 41.6° reads `ratio_k` backwards.
It argues 41.6° is safely "inside the curve's own positive lobe, not
adjacent to a near-total destructive-interference null" because
`ratio_k=25.9` "is not small." But `ratio_k = frac_p_abs/frac_contrast`,
and `frac_p_abs` is independently established as nearly flat across θ (this
cycle's own items 3b/5b). A LARGE `ratio_k` therefore signals a SMALL
`frac_contrast`/`delta_scene` — proximity to a null, exactly R13's own
established denominator-blowup mechanism. By the proposal's own n=8 table,
the genuinely far-from-null CONSISTENT population (37.2°, 39.2°–39.8°) has
`ratio_k` 0.08–3.8, while 41.6°'s 25.9 sits inside the *same* 20–30× band
as the interior near-null sweep's own floor-clearing points (20.5–29.6×,
called "a deep near-total-null trough" two sections later in the same
document). So 41.6° is evidentially closer to the fragile,
sigma-contaminated population than to the safe one — the CONFIRM lean
isn't merely unconfident, it points the wrong direction, invoking R13/R14
to support a reading those rules' own numbers contradict.

## Verdict: **support-with-changes**

The FDTD design itself (call budget, gates, settling precondition, the
mandatory `R4` identity asserts) is sound and independently verifiable —
none of that is in dispute. The defect is confined to the narrative
"informed lean" for Rank 2, which does not gate any falsifiable band or
call sequencing, so it is non-load-bearing to what actually gets measured.
But this house's own R4/R9 discipline (recompute, don't hand-reason, and
verify commensurability before trusting a comparison) applies here: a
wrong physical justification should not enter the permanent record even
when non-binding, especially since a REFUTE at 41.6° — which the numbers
above suggest is at least as likely as the document's stated CONFIRM lean
— would otherwise read as a foreseeable-but-mislabeled "genuine surprise."

## Parameter change that would flip my verdict

Strike or correct the Rank 2 "informed lean" paragraph — either drop the
directional claim entirely, or replace the `ratio_k`-based justification
with the correct one: 41.6° sits in the *same* high-`ratio_k` population as
the confirmed-fragile interior sweep, so REFUTE is at least as plausible as
CONFIRM there. With that one paragraph corrected pre-freeze, I move to full
**support** — everything else in the proposal, independently checked,
holds up.
