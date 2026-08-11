# exp-009 — The Ratio Below Eight

## Hypothesis

exp-008's bare-disk control found the cloaked/bare Q_ext ratio falling
from 0.900 at core=30 down to a ~0.193 plateau across core=8–12, then
flagged as open: does that plateau continue below core=8, or does the
ratio move again once the PEC core is deeply subwavelength?

This experiment traces both curves (bare and cloaked, paired) at four
new core radii below exp-006/007/008's floor of 8 — the exact "2–4 new
core values" PLAN.md queued as exp-009 — with the CFL margin checked
explicitly first, per the standing discipline flagged in exp-007's
NOTES and carried into PLAN.md's open item.

## Setup

Same 2D TMz bench, same fixed domain as exp-003/004/006/007/008
(N=680, cpl=20, courant_frac=0.32, absorb=40, λ=600nm, R2_CELLS=90
fixed outer cloak radius / footprint denominator, same box-pair
cross-section machinery). `mu_r_floor=0.10` fixed throughout — the
value that produced exp-006/007's design lead and exp-008's control.

**Core sweep: r1 ∈ {4, 5, 6, 7} cells** — the four points immediately
below exp-006/007/008's smallest tested core (8), each run **paired**
(bare PEC disk + cloaked) in this one file, unlike exp-008 which reused
exp-006/007's already-gated cloaked numbers. New territory needs its
own cloaked runs, not an extrapolation.

**CFL margin, checked explicitly before any run** (the item PLAN.md
flagged as exp-009's precondition): margin = `sqrt(floor·eps_z)/courant_frac
− 1`, same formula exp-007 used. As core shrinks, `eps_z = (r2/(r2−r1))²`
falls toward 1 and the margin shrinks *with* it — this is not a free
lunch below core=8. Computed ahead of committing this file:

| core | eps_z | cfl_ceiling | margin |
|---|---|---|---|
| 8 (exp-007 ref) | 1.2046 | 0.3471 | 8.46% |
| 7 | 1.1758 | 0.3429 | 7.16% |
| 6 | 1.1480 | 0.3388 | 5.88% |
| 5 | 1.1211 | 0.3348 | 4.63% |
| 4 | 1.0952 | 0.3309 | 3.42% |
| 3 | 1.0702 | 0.3271 | 2.23% |
| 2 | 1.0460 | 0.3234 | 1.07% |
| 1 | 1.0226 | 0.3198 | **−0.07% (unstable)** |

All four chosen cores (4–7) stay stable at the existing `courant_frac=0.32`
with no paired frac cut needed — but core=4's 3.4% margin is the
tightest run in this lab's history (vs. exp-007's previous tightest,
8.5% at core=8), so this experiment stops at 4 rather than continuing
toward core=1–2, where the margin turns negative before the shell
geometry itself does anything interesting. Pushing further is exactly
the still-open PLAN.md item that needs a deliberate `courant_frac` cut,
not a target for this shift.

8 runs total (4 bare + 4 cloaked) + 1 shared empty reference = 9 runs.

## Idealizations

Same 2D TMz, hand-rolled FDTD, absorbing (not true PML) boundary as
every experiment in this line. Single λ=600nm, single floor=0.10 — this
does not attempt the multi-λ story (still queued, exp-007's own
follow-up). At core=4 cells, the PEC disk's diameter is 0.4 cells ×
2 = 8 cells ≈ 0.4λ (cpl=20) — deeply subwavelength, well into the
Rayleigh-scattering regime for the bare disk, which is exactly the
physical reason P3 below predicts the ratio won't stay flat.

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 8 new points (4 bare, 4 cloaked).
- **P2 (bare Q_ext keeps falling):** the bare disk's Q_ext continues
  decreasing monotonically as core shrinks from 8 → 4, extending
  exp-008's P2 finding into deeper subwavelength territory. Expect the
  *rate* of decrease to steepen relative to the 8–30 range, consistent
  with entering the Rayleigh regime (bare PEC cylinder scattering
  cross-section falls faster than linearly with radius once the object
  is well below λ/2).
- **P3 (cloaked Q_ext keeps falling too, but more slowly):** the cloaked
  Q_ext also continues decreasing monotonically from core=8 → 4,
  extending exp-006/007's law, but at an even shallower per-cell slope
  than the already-slowed core=8–15 range (exp-007's finding) —
  consistent with Q_ext(cloaked) approaching a positive residual floor
  as the shell approaches its r1→0 identity-map limit (eps_z→1).
- **P4 (the discriminating prediction — does the plateau hold?):** the
  cloaked/bare ratio does **not** stay flat at exp-008's ~0.193 plateau;
  it **rises** as core shrinks from 8 to 4. Mechanism: P2 predicts bare
  Q_ext falls through the steep Rayleigh regime, while P3 predicts
  cloaked Q_ext's descent is already slowing — if bare falls faster than
  cloaked in this range, the ratio (cloaked/bare) must rise. Specific,
  falsifiable threshold: ratio(core=4) ≥ 0.193 × 1.2 ≈ 0.232, at least
  20% above exp-008's plateau value. A ratio that stays within ~5% of
  0.193 all the way to core=4 would refute this and mean the plateau is
  a genuine floor, not a Rayleigh-regime artifact about to break.

## Results

*(pending)*

## Next

*(pending)*
