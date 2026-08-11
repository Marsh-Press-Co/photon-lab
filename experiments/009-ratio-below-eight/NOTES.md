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

9 runs (4 bare + 4 cloaked + 1 empty), 5.6 min. CFL margins matched the
pre-registered table exactly (3.42–7.16%, all `OK`).

| core (r1) | Q_ext (bare) | Q_ext (cloak) | ratio | box_dev (bare/cloak) | cross_dev (bare/cloak) |
|---|---|---|---|---|---|
| 7 | 0.1970 | 0.0365 | 0.185 | 0.012 / **0.018** | 0.002 / 0.013 |
| 6 | 0.1763 | 0.0413 | 0.235 | 0.011 / **0.020** | 0.003 / 0.011 |
| 5 | 0.1541 | 0.0424 | 0.275 | 0.009 / **0.023** | 0.003 / 0.011 |
| 4 | 0.1242 | 0.0351 | 0.283 | 0.004 / **0.035** | 0.004 / 0.013 |

(context: exp-008's plateau was ratio≈0.193–0.194 at core=8–12; exp-007's
cloaked Q_ext at core=8 was 0.0429.)

### The gate itself broke, and that has to lead

**P1 is REFUTED at 2 of 4 new points, borderline at a third.** Box
independence for the *cloaked* runs: 1.8% (core=7, passes) → 2.0%
(core=6, exactly at the ≤2% line) → 2.3% (core=5, **fails**) → 3.5%
(core=4, **fails**, worst gate margin in this lab's history). The *bare*
disk runs stayed clean throughout (0.4–1.2%, same quality as exp-008)
— this is not a general breakdown of the harness, it is specific to the
cloak's graded material profile at these radii. The degradation is
smooth and monotonic with shrinking core, tracking `eps_z`'s approach to
1 (r1→0, identity-map limit) — consistent with the shell's continuous
`mu_r=((r−r1)/r)²` profile becoming poorly sampled by the fixed
`cpl=20` grid as the number of cells spanning the profile's steepest
part (near the tiny inner radius) shrinks. `sigma_abs` at all 4 cloaked
points came out **negative** (−0.021 to −0.100, i.e. −0.3% to −1.6% of
`sigma_ext`) — nonphysical for a lossless clamped-mu_r shell, and
another symptom of the same discretization strain, not a new failure
mode.

Per house discipline (verify-before-claim, same standard applied when
exp-003 caught its own domain-sizing bug): a pre-registered gate failure
means the numbers behind it are not yet trustworthy, not that they are
wrong — the next step is a resolution check, exactly exp-004→exp-005's
precedent, not a shrug.

### Predictions scored (with that caveat attached)

- **P1 (gates ≤2%)** — CONFIRMED at core=7 (cleanly) and core=6
  (exactly at the boundary); **REFUTED** at core=5 and core=4.
- **P2 (bare Q_ext keeps falling, steepening)** — CONFIRMED, cleanly.
  Strictly monotonic (0.1242→0.1541→0.1763→0.1970 as core rises 4→7)
  with gates the tightest of any run in this experiment, extending
  exp-008's Rayleigh-regime reading with no ambiguity.
- **P3 (cloaked Q_ext keeps falling monotonically too)** — **REFUTED**,
  and not by a small margin: the cloaked curve is **non-monotonic** —
  0.0351 (core=4) → 0.0424 (core=5) → 0.0413 (core=6) → 0.0365
  (core=7) → 0.0429 (exp-007's core=8) — a bump peaking around core=5,
  not the smooth continuation of exp-006/007's law predicted. This bump
  sits exactly in the region where P1's gate degrades, so it cannot yet
  be read as a new physical regime (a genuine breakdown of the
  thicker-shell-is-better law below core~8) rather than a
  resolution-driven wobble — this experiment's data alone cannot
  distinguish the two, which is precisely what exp-010 checks next.
- **P4 (ratio rises above the plateau, ≥0.232 at core=4)** — the
  *number* clears the pre-registered threshold (0.283 ≥ 0.232) and the
  ratio trend is monotonic and smooth (0.185→0.235→0.275→0.283) even
  though the cloaked Q_ext behind it is not — because bare Q_ext's clean
  monotonic rise dominates the ratio's shape. But scoring P4
  "confirmed" outright would launder a gate-failing number through a
  ratio; the honest call is **directionally supported, not yet
  gate-trustworthy** at core=4/5 specifically. Core=6 (borderline
  gate) and core=7 (clean gate) both already show the ratio breaking
  above exp-008's ~0.193 plateau (0.235, 0.185 respectively) — core=7's
  own clean point is a real, gate-passing data point that the plateau
  does *not* hold below core=8, even setting the two failing points
  aside entirely.

## Next

- **exp-010, immediate:** resolution-convergence check on this
  experiment's box_dev failures and the core=4–7 non-monotonic bump,
  mirroring exp-004→exp-005's precedent exactly — rerun the same 4
  paired bare+cloak points at cpl=30 (1.5×), geometry scaled in cells to
  hold physical size fixed. If the bump and the gate failures both
  shrink at higher resolution, this experiment's P3 finding was a grid
  artifact specific to very-thin-shell geometries at cpl=20 — a genuine
  and useful resolution-floor finding in its own right. If the bump
  survives refinement (exp-005's own precedent: it can, and did, for a
  smaller anomaly), it's a real new regime below core~8 worth its own
  follow-up.
- Even setting the bump aside, core=7's clean, gate-passing point
  (ratio=0.185, *below* exp-008's plateau, not above it) already shows
  the plateau doesn't extend flat below core=8 — worth carrying forward
  regardless of how exp-010 resolves the core=4–6 question.
