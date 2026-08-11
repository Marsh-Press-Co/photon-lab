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

7 runs (6 cloak + 1 empty), 41.6 min.

| base (cpl=20 r1) | r1 (cpl=30) | eps_z | Q_ext(0.10) | Q_ext(0.18) | jump (cpl=30) | jump (cpl=20) | box_dev (0.10/0.18) |
|---|---|---|---|---|---|---|---|
| 28 | 42 | 2.1072 | 0.5664 | 0.6134 | **+8.31%** | +6.01% | 0.12% / 1.30% |
| 30 | 45 | 2.2500 | 0.6293 | 0.5260 | **−16.42%** | −17.69% | 0.16% / 0.28% |
| 33 | 50 | 2.5225 | 0.5982 | 0.8040 | **+34.41%** | +12.22% | 0.85% / 0.05% |

All box_dev ≤1.30%, cross_dev ≤0.0018% — the cleanest gates in this
whole eps_z investigation line (cross_dev four orders of magnitude below
its own 2% ceiling), confirming the higher resolution genuinely
tightened the measurement, not just changed the answer.

### Predictions scored

- **P1 (gates ≤2%)** — CONFIRMED, comfortably: max box_dev 1.30%
  (base=28/floor=0.18), max cross_dev 0.0018%.
- **P2 (the discriminator — sign preserved at all 3 points)** —
  **CONFIRMED, cleanly.** base=28 stays positive (+6.01%→+8.31%),
  base=30 (trough center) stays negative (−17.69%→−16.42%), base=33
  stays positive (+12.22%→+34.41%). No sign flips anywhere. The trough
  exp-014 found is not a cell-quantization artifact of stepping r1 by 1
  cell at cpl=20 — it survives 1.5× resolution refinement intact, at
  both the trough's center and both flanks, extending exp-005's own
  refutation of the grid-staircase-artifact hypothesis (there, for the
  floor sweep) to the eps_z axis.
- **P3 (magnitude, secondary)** — mixed, informative beyond what was
  scored. base=30's jump **shrank 7.2% relative** (−17.69%→−16.42%) —
  remarkably close to exp-005's own core=30/floor-pair refinement result
  (17.7%→16.4%, a 7% relative shrink) at the *same* geometry, just a
  different resolution axis being refined. base=28 grew modestly
  (+6.01%→+8.31%). base=33 grew substantially (+12.22%→+34.41%, nearly
  tripled) — but base=33 is also the point with the largest eps_z
  rounding drift (2.4931→2.5225 cpl=20→30, a 1.2% shift from 33×1.5 not
  landing on an integer cell), so part of that growth may reflect
  probing a genuinely different, slightly-further-out eps_z point rather
  than a pure resolution effect. Flagged honestly rather than folded
  into a clean "magnitude grows near this flank" claim.

### Headline

**The trough is real, not a grid artifact.** All three signs survive
1.5× resolution refinement exactly as predicted — the deepest point
stays deeply negative with almost the identical relative shrink exp-005
found for the *floor* jump at this same geometry, and both flanks stay
positive. exp-014's own honest caveat (never having tested whether a
1-cell eps_z step is fine enough to trust) is now closed: `Q_ext(eps_z)`
has a genuine local, non-monotonic feature near eps_z≈2.25 that a
transformation-optics reduced-cloak shell's extinction cross-section
actually possesses, independent of grid resolution. No mechanism for
*why* is proposed yet.

## Next

- **[open]** The mechanism question, now on solid footing: why does a
  reduced-cloak shell's Q_ext(eps_z) have a local resonance-like feature
  near eps_z≈2.25–2.4, confirmed grid-independent? Candidates worth
  testing in a future shift: sweep the shell's local impedance mismatch
  `√(mu_r/eps_z)` at the outer boundary across this same eps_z range
  (Cummer et al.'s known reduced-parameter residual-reflection
  mechanism, already invoked as a candidate story back in exp-006's P3
  and refuted there for the *magnitude* trend — worth revisiting now
  that the feature's *location* is pinned down) — or a scattered-field
  angular-pattern comparison across the trough vs its flanks, to see if
  the mechanism is a shape change (a new backscatter lobe appearing) or
  a pure magnitude effect.
- base=33's 1.2% eps_z rounding drift is a small, known imprecision in
  this file (documented in Setup) — if the mechanism investigation above
  wants a clean base=33-equivalent point, re-deriving an exact-integer
  r1 pair at some other cpl (or picking a different cpl=20 anchor whose
  ×1.5 is exact) would remove it.
- The `mu_r_floor < 0.05` direction and the parking lot remain open,
  unchanged.
