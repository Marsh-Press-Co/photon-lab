# exp-005 — Does the Clamp Jump Shrink With Resolution?

**2026-08-10 · driver: Clyde (cloud shift) · status: predictions committed, machinery pending**

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

*(pending — machinery not yet run)*
