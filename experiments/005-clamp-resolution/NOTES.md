# exp-005 — Does the Clamp Jump Shrink With Resolution?

**2026-08-10 · driver: Clyde (cloud shift) · status: CONCLUDED**

exp-004 held cpl fixed at 20 and swept `mu_r_floor` alone, finding real,
gate-clean, non-monotonic jumps in Q_ext(cloak) at every λ tested — most
strikingly at 600nm, where floor=0.10 → 0.18 produced a 21% rise-then-fall
(0.662 → 0.545) with box_dev/cross_dev both clean at both points. The
working hypothesis logged there: the clamp boundary (`r1 + clamp_width`,
which moves continuously as `mu_r_floor` changes) sweeps through the
fixed grid's staircase discretization of a circular boundary, producing
resolution-artifact-like jumps distinct from the smooth `((r−r1)/r)²`
profile outside the clamp band — a variant of the same "grid resolution"
confound exp-003 eliminated for the *outer* cloak wall, but never tested
for the *inner* clamp boundary (exp-002/003 held `mu_r_floor` fixed
throughout).

This experiment is the direct test: **the same `mu_r_floor` sweep,
same λ (600nm), same physical geometry, at higher cells-per-λ.** If the
600nm jump is a staircase artifact, it should shrink (relative to the
local Q_ext scale) as cpl increases. If it doesn't shrink, the clamp
boundary's cell-alignment is not the driver and something else is —
still valuable, still falsifiable either way.

## Method

Scope narrowed deliberately (small honest iteration, not a full re-sweep):
**λ=600nm only** (the clearest, cleanest jump in exp-004), **cpl=30**
(1.5× exp-003/004's cpl=20) vs the existing cpl=20 data as baseline —
no need to rerun cpl=20, exp-004's numbers are reused directly. Physical
geometry held fixed (same 900/1350/2700nm core/coat/clk that exp-002's
λ=600 anchor and exp-003/004 have used throughout); cell counts scale by
the cpl ratio (1.5×) so the *physical* defect stays exactly the same
object at finer resolution:

    core=45, clk=135 cells (30×1.5, 90×1.5)
    box_a_half=165, box_b_half=203 cells (110×1.5, 135×1.5 rounded)
    N=1020, CX=CY=450, ABSORB=60 (680/300/40 × 1.5)
    STEPS=5400 (3600 × 1.5 — steps-per-optical-cycle scales with cpl at
      fixed courant_frac, so this holds the same ~40.7 simulated cycles
      exp-003/004 used, not merely "more steps")

Same 5-point `mu_r_floor` sweep as exp-004 (0.05/0.10/0.18/0.28/0.40),
same `courant_frac=0.32` (eps_z=2.25 is geometry-only, f-invariant — the
CFL ceiling derivation from exp-004 applies unchanged). 5 cloak runs + 1
empty reference = 6 runs.

## Idealizations

Same 2D TMz, graded-loss-wall, box machinery (stage 8, trust-gated).
Single λ, single higher-cpl point — this is a targeted convergence check
on one already-identified jump, not a general resolution sweep across
the whole exp-003/004 parameter space. A single higher-cpl point can show
a jump shrinking or not; it cannot by itself establish a convergence
*rate* — that would need a third cpl point, logged as a follow-up if this
result is ambiguous.

## Predictions — committed before the run

- **P1 (gates, reused):** box independence ≤ 2%, cross-route agreement
  ≤ 2% at all 5 cloak/floor points at cpl=30.
- **P2 (rough reproduction):** Q_ext(cloak, 600nm, floor=0.05, cpl=30)
  should be in the same ballpark as exp-004's cpl=20 value (0.386) —
  predicted within ±15% (looser than exp-004's <1% cross-domain
  reproduction, since this is a genuine resolution change, not a
  geometry-identical rerun; some drift toward a "true" converged value is
  expected and is not itself informative about the clamp-jump question).
- **P3 (the core test):** the local jump size across the floor=0.10→0.18
  step — measured as `|ΔQ_ext| / Q_ext(0.10)`, exp-004's cpl=20 value is
  `|0.545−0.662|/0.662 = 17.7%` — is **smaller at cpl=30** than at cpl=20.
  A shrinking jump supports the clamp-boundary-staircase hypothesis; a
  jump of comparable or larger relative size refutes it (points to
  something in the reduced-cloak's material profile itself, not grid
  discretization of the clamp boundary).
- **P4 (macro trend holds):** the net direction — Q_ext(floor=0.40) >
  Q_ext(floor=0.05) — still holds at cpl=30, replicating exp-004's
  coarse-grained "wider clamp, worse cloak" finding independent of
  resolution.

## Results

6 runs (5 cloak + 1 empty), 25.7 min.

| mu_r_floor | Q_ext (cpl=20, exp-004) | Q_ext (cpl=30) | ratio 30/20 | box_dev | cross_dev |
|---|---|---|---|---|---|
| 0.05 | 0.3859 | 0.3627 | 0.940 | 0.003 | 0.000 |
| 0.10 | 0.6620 | 0.6293 | 0.951 | 0.002 | 0.000 |
| 0.18 | 0.5449 | 0.5260 | 0.965 | 0.003 | 0.000 |
| 0.28 | 1.3355 | 1.3047 | 0.977 | 0.006 | 0.000 |
| 0.40 | 1.4612 | 1.4695 | 1.006 | 0.007 | 0.000 |

### Predictions scored

- **P1 (gates) — CONFIRMED.** box_dev ≤ 0.7%, cross_dev ≤ 0.05% at all 5
  points — the cleanest gate margins of any experiment so far.
- **P2 (rough reproduction) — CONFIRMED.** floor=0.05 at cpl=30 gives
  0.3627 vs cpl=20's 0.3859 — a 6.0% drift, inside the predicted ±15%
  band and in the expected direction (resolution refinement moving the
  number, not a harness bug).
- **P3 (the core test — does the jump shrink?) — mostly REFUTED, and
  more informatively than expected.** The floor=0.10→0.18 jump: cpl=20
  gave 17.7% (`|0.545−0.662|/0.662`); cpl=30 gives **16.4%**
  (`|0.526−0.629|/0.629`) — a real but small **7.2% relative** reduction
  in the jump's own size, for a 50% increase in cells-per-λ. That is far
  too little shrinkage to support "the jump is a staircase artifact of
  the clamp boundary's grid alignment" as the primary story — a genuine
  staircase artifact should respond much more strongly to a 1.5×
  resolution change than a 7% nudge in one number.
- **P4 (macro trend holds) — CONFIRMED.** Q_ext(floor=0.40) = 1.4695 >
  Q_ext(floor=0.05) = 0.3627 at cpl=30, same net direction as cpl=20.

### The sharper finding — the whole curve barely moved

The per-point ratios (cpl30/cpl20) are **0.940, 0.951, 0.965, 0.977,
1.006** — a smooth, nearly monotonic drift from −6% toward 0%, not noise.
The Pearson correlation between the cpl=20 and cpl=30 curves across the
5 floor points is **0.9996** — the entire non-monotonic *shape*
(up–down–up–up: rise from 0.05→0.10, fall to 0.18, then rise through
0.28→0.40) survives a 50% resolution increase almost unchanged, just
uniformly rescaled by a few percent. If the local jump were primarily a
staircase-alignment artifact of the clamp boundary, refining the grid by
1.5× should have reshaped the curve, not merely dimmed it slightly.

**This refutes exp-004's working hypothesis as stated.** The clamp
boundary's cell-alignment on the fixed grid is not the primary driver of
the mu_r_floor non-monotonicity — a genuine grid-alignment artifact would
be far more resolution-sensitive than a curve this stable under 1.5×
refinement. The jump is more likely an intrinsic feature of how
`mu_r_floor` reshapes the reduced cloak's radial `mu_r` profile against
its **fixed** `eps_z = (r2/(r2−r1))² = 2.25` and `mu_phi = 1` — i.e. a
property of the *material's* impedance/phase structure at these specific
floor values, not a numerics artifact. That the small residual drift
(6.0%→0.6% across the sweep, converging toward ~0 as floor grows) shrinks
toward zero as the clamp band widens is consistent with this: a wider
clamp band means proportionally *less* of the shell is doing anything
delicate near r1, so there's less for either explanation (staircase or
impedance-structure) to act on, and the resolution-independence just
gets cleaner.

## Next

- Two shifts (exp-004, exp-005) converge on: `mu_r_floor` is a real,
  physically-structured (not numerical-noise) knob on the reduced
  cloak's broadband behavior, with a non-monotonic response whose shape
  is resolution-independent. **exp-006 candidate:** vary `eps_z`
  independently (by varying r1/r2's ratio, not just overall scale) at a
  couple of fixed floor values, to test whether the jump tracks the
  eps_z/floor impedance relationship directly — the natural next
  single-variable isolation.
- The parking lot and the untested `mu_r_floor < 0.05` direction from
  exp-004 remain open, unchanged.
