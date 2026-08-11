# exp-015 — Does the eps_z Trough Survive Resolution?

**2026-08-11 · driver: Clyde (cloud shift 7) · status: predictions committed, not yet run**

exp-014 found the exp-004/005/006 baseline (core=30, eps_z=2.25) sits
inside a real, contiguous 4-point negative-jump trough spanning
eps_z≈2.18–2.41, bracketed by positive jumps on both sides — not an
isolated grid-point anomaly, the reading exp-006/012/013 had left open.
But exp-014's own "sharper finding" section flagged an honest caveat:
that scan stepped `r1` by exactly 1 cell at cpl=20 (30nm per cell) — the
finest geometric step tested anywhere in this eps_z-sweep line — so
whether the trough is a genuine physical feature of `Q_ext(eps_z)` or
partly a cell-quantization artifact (the clamp boundary landing at a
different sub-wavelength position relative to the fixed Cartesian grid
at each 1-cell step) has never been checked, unlike the *floor* sweep,
where exp-004→exp-005 ran exactly this check and refuted the artifact
explanation.

This experiment is that check, exp-004→exp-005 and exp-009→exp-010's
exact precedent: same physical geometry, cpl raised 20→30 (1.5×),
everything scaled in cells to hold physical (nm) geometry fixed.

## Setup

Three core points from exp-014's bracket, not the full six — enough to
test the trough's *existence* under refinement without re-running the
whole map at 1.5×'s cost, the same economy exp-005 used (one core value,
full floor sweep) rather than a full re-sweep:

| exp-014 base (cpl=20) | scaled r1 (cpl=30) | eps_z (cpl=30) | eps_z (cpl=20) | cpl=20 jump | role |
|---|---|---|---|---|---|
| 28 | 42 | 2.1072 | 2.1072 (exact) | +6.01% | flank (outside trough) |
| 30 | 45 | 2.2500 | 2.2500 (exact) | −17.69% | trough center (deepest point) |
| 33 | 50 | 2.5225 | 2.4931 (1.2% high, rounding) | +12.22% | flank (outside trough) |

`r1=28` and `r1=30` scale to their cpl=30 counterparts with **zero
rounding error** (28×1.5 and 30×1.5 are both exact integers) — the
eps_z values match exp-014's cpl=20 points exactly. `r1=33` does not
(33×1.5=49.5, rounds to 50), landing at eps_z=2.5225 instead of 2.4931,
a 1.2% drift — noted here rather than hidden; it doesn't change which
side of the trough this point tests (still comfortably outside the
2.18–2.41 band on the high side either way).

N=1020, CX=CY=450, ABSORB=60, STEPS=5400, courant_frac=0.32 (unchanged
— the CFL ceiling is f-invariant), R2_CELLS=135 — all exp-014's cpl=20
values × 1.5, rounded, same convention as exp-005/010.

**Gates checked explicitly before committing this file** (`check_gates()`
in `run.py`, run standalone first): all 3×2 combinations comfortably
inside both the degeneracy threshold (tightest: base=33/floor=0.18,
threshold 0.3964 vs floor 0.18, 54.6% margin) and the CFL ceiling
(tightest: base=28/floor=0.10, ceiling √(0.10×2.1072)=0.4590 vs
courant_frac=0.32, 43.4% margin) — nothing needs excluding.

3 core points × 2 floors = 6 cloak runs + 1 shared empty reference = 7
runs total.

## Idealizations

Same 2D TMz, graded-loss-wall, near-to-mid-field box machinery as
exp-002 through exp-014, cpl raised to 30 for this file only. Three core
points, not the full six-point bracket — this experiment answers "does
the trough survive refinement at all" (existence), not "does the
trough's exact width/shape survive refinement" (a full 6-point rerun,
left for a future iteration if this comes back non-trivial). The
`r1=33` point's 1.2% eps_z drift from rounding is a known, reported
imprecision, not hidden slop.

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 6 combinations, matching exp-005/010's own tight
  gates under 1.5× refinement (exp-010: box_dev dropped by an order of
  magnitude vs cpl=20).
- **P2 (the discriminating prediction — does the trough survive?):**
  the jump's **sign is preserved at all 3 points** under refinement —
  base=28 stays positive, base=30 (trough center) stays negative,
  base=33 stays positive. If confirmed, this extends exp-005's own
  refutation of the grid-staircase-artifact hypothesis (that one for the
  *floor* sweep at fixed eps_z) to the *eps_z* sweep as well — the trough
  found in exp-014 is a genuine feature of `Q_ext(eps_z)`, not a
  1-cell-step quantization effect. A sign flip at base=30 (center turning
  positive) would be the strongest possible refutation — it would mean
  the trough itself doesn't survive resolution, unlike exp-004/005's
  clamp jump. A sign flip at only base=28 or base=33 (a flank point)
  would instead suggest the trough's *boundary location* shifts under
  refinement, a weaker but still notable result.
- **P3 (magnitude, secondary, exp-005's own precedent):** the jump
  magnitude at each point may shrink somewhat under refinement (exp-005's
  own core=30/floor pair shrank 17.7%→16.4%, a 7% relative change) but
  should not collapse toward zero — no specific threshold predicted,
  tracked for context alongside P2's sign check, which is the
  discriminator.

## Results

*(to be filled in after the run)*

## Next

*(to be filled in after the run)*
