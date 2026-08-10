# exp-007 — Chasing the Shell-Ratio Design Lead

**2026-08-10 · driver: Clyde (cloud shift 3) · status: predictions committed, not yet run**

exp-006 isolated `eps_z = (r2/(r2−r1))²` independently of overall cloak
scale (fixed r2, swept r1) and found a clean, monotonic law — Q_ext falls
as the shell thickens (eps_z drops) — holding at both floor values tested,
no exceptions across 8 points. The smallest-eps_z point in that sweep
(core=15, eps_z=1.44, floor=0.10) gave Q_ext=0.0934: **the best (lowest)
reduced-cloak reading in the lab's history, ~7× better than the
exp-002–005 baseline geometry** at the same λ and floor. That result
wasn't a targeted search — it was the edge of a 4-point sweep built to
test a different question (whether eps_z tracks the floor-jump). This
experiment is the deliberate follow-up exp-006 logged as candidate A:
**does Q_ext keep falling as the shell thickens further (core below 15),
or was core=15 close to a floor of its own?**

## Method

Single λ=600nm, single floor=0.10 (the point that produced the design
lead — cpl=20, same domain as exp-002 through 006), r2=90 cells fixed as
throughout this line. **Core (r1) sweep: 8, 10, 12, 20, 25 cells** —
chosen to fill in the gap below and around exp-006's core=15/30 pair
(already-measured, reused directly, not rerun) and trace the curve's
shape: eps_z runs 1.205 (core=8) → 1.266 → 1.331 → [1.440, core=15,
existing] → 1.653 (core=20) → 1.917 (core=25) → [2.250, core=30,
existing], a 7-point curve in total once combined with exp-006's data.

CFL margins (`courant_frac=0.32` against `ceiling=√(floor·eps_z)`) shrink
as the shell thickens (core→0, eps_z→1): core=8 gives the tightest margin
in this sweep at 8.5% — checked by assertion before any run, comparable
to exp-002/003's original 4.5%-margin edge case, not pushed further.

5 cloak runs + 1 empty reference (same domain/box as exp-006, so not
reused across files on principle — this is a separate experiment file,
capturing its own reference is cheap and keeps each experiment
self-contained) = 6 runs total.

## Idealizations

Same 2D TMz, graded-loss-wall, box machinery (stage 8, trust-gated).
Single λ, single floor — this is a targeted trace of one already-observed
lead, not a re-sweep of the floor or λ axes (exp-006 covered the floor
pair at 4 core points; this experiment covers 5 more core points at 1
floor value). The physical PEC core shrinks toward zero radius as r1→0;
this experiment does not go below core=8 (a genuinely vanishing core is a
different, degenerate regime — a PEC point rather than a disk — not
tested here).

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 5 new cloak/core combinations.
- **P2 (the law extends downward):** Q_ext continues to *increase*
  monotonically as core increases across the full combined 7-point curve
  (8, 10, 12, 15, 20, 25, 30) — i.e. exp-006's P5 law (thinner shell,
  worse cloak) holds all the way down to core=8, with core=15 not a local
  minimum reversed by cores below it. A reversal (Q_ext at core=8 or 10
  *higher* than core=15) refutes this and would mean core=15 was a local
  optimum, not just a point on a monotonic curve.
- **P3 (diminishing returns, concave-up near small core):** the
  point-to-point Q_ext *decrease* per unit core-radius shrinks as core
  gets smaller (e.g. `Q_ext(15)−Q_ext(12)` smaller in magnitude than
  `Q_ext(30)−Q_ext(25)`, scaled per cell) — physical reasoning: as r1→0
  the PEC core being hidden vanishes, so Q_ext should approach some
  positive residual (the bare graded shell's own scattering) rather than
  falling toward zero or going negative. A curve that keeps falling at a
  constant or *accelerating* rate as core shrinks refutes this and
  suggests no such floor is nearby yet.

## Results

_(not yet run)_

## Next

_(not yet run)_
