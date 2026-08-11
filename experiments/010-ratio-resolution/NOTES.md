# exp-010 — Does the Below-Eight Bump Survive Resolution?

## Hypothesis

exp-009 found two things needing separation: (1) the box-independence
gate failed at core=4 (3.5%) and core=5 (2.3%), passed borderline at
core=6 (2.0%), and passed cleanly at core=7 (1.8%) — bare-disk gates
stayed clean throughout, so the failure is specific to the cloak's
graded material profile at small core; (2) the cloaked Q_ext curve
itself was non-monotonic across core=4–7 (a bump peaking near core=5),
where exp-006/007's established law (thicker shell, i.e. smaller core,
monotonically better cloak) predicted a smooth continuation. exp-009
could not tell whether the bump is real physics in a regime not
explored before, or a resolution artifact riding on the same
degradation that broke the gate.

This is exp-004→exp-005's exact precedent: an anomaly found at fixed
resolution, checked immediately by rerunning the same points at higher
cells-per-wavelength with physical geometry held fixed. If the bump and
the box_dev failures both shrink at cpl=30, exp-009's finding was a
grid artifact specific to very-thin-shell (r1 approaching 0) geometries
at cpl=20. If the bump survives — exp-005's own precedent showed a
smaller anomaly *can* survive resolution refinement almost unchanged —
it's a real regime below core~8 worth its own follow-up.

## Setup

Same 4 core points as exp-009 (r1_base ∈ {4, 5, 6, 7} cells at cpl=20),
rescaled to **cpl=30** (1.5×) exactly as exp-005 rescaled exp-004's
geometry: physical size held fixed, cell counts scaled by 1.5 and
rounded.

    N=1020, CX=CY=450, ABSORB=60, STEPS=5400, SRC_X=96,
    REF_HALF_H=90, MIN_MARGIN=90, BOX_A_HALF=165, BOX_B_HALF=202,
    R2_CELLS=135 (90*1.5), courant_frac=0.32 (unchanged — eps_z-based
    CFL ceiling is f-invariant per exp-004/005/007's derivation)

Core cell counts at cpl=30: r1_base 4→6, 5→8 (7.5 rounds to 8, nearest
even), 6→9, 7→10 (10.5 rounds to 10, nearest even) — Python's
round-half-to-even, same convention exp-005 used implicitly via
`int(round(...))`. This means the four points are not at *exactly*
1.5× their cpl=20 radii (r1_base=5 and 7 pick up small rounding drift:
factor 1.6 and 1.43 respectively instead of 1.5), which shifts `eps_z`
slightly off the cpl=20 values for those two points (1.1300 vs 1.1211,
1.1664 vs 1.1758) — a restated idealization, not a new one; exp-005
carried the same rounding drift silently and it didn't matter there.

CFL margins, checked before running (same discipline as exp-009):

| core (cpl=30 cells) | eps_z | cfl_ceiling | margin |
|---|---|---|---|
| 6 | 1.0952 | 0.3309 | 3.42% |
| 8 | 1.1300 | 0.3361 | 5.05% |
| 9 | 1.1480 | 0.3388 | 5.88% |
| 10 | 1.1664 | 0.3415 | 6.73% |

All stable at the unchanged `courant_frac=0.32`, no frac cut needed.

Both bare and cloaked runs repeated at cpl=30 (bare gates were already
clean at cpl=20, but rerunning keeps the ratio comparison apples-to-
apples at matched resolution, same convention as exp-009 itself) + one
shared empty reference = 9 runs total.

## Idealizations

Same 2D TMz, absorbing-boundary bench as every experiment in this line.
Single λ=600nm, single floor=0.10, single resolution step (cpl=20→30,
exp-005's exact ratio) — this is a targeted convergence check on one
already-identified anomaly, not a general resolution sweep. A single
higher-cpl point can show the bump/gate-failure shrinking or not; it
cannot by itself establish a convergence *rate* (a third cpl point would
be needed for that, logged as a follow-up only if this result is
ambiguous, exactly as exp-005 flagged for its own single-step check).

## Predictions — committed before the run

- **P1 (the gate itself improves):** box_dev at the cpl=30 cloaked
  core=6-cells point (the r1_base=4 analog) drops below 2%, and ideally
  below exp-009's core=7-cells 1.8% floor — if cpl=20's box_dev failure
  was a resolution artifact of the graded-profile discretization, a 1.5×
  finer grid should visibly shrink it, mirroring exp-005's P1 (which
  found the tightest gate margins of any experiment in that line).
- **P2 (rough reproduction):** cpl=30's Q_ext values are in the same
  ballpark as exp-009's cpl=20 values at matched physical core size —
  within ±20% (looser than exp-005's ±15% band, since exp-009's own
  numbers carry more resolution uncertainty going in than exp-004's
  did) — not exact agreement, a genuine resolution change is expected to
  move the numbers somewhat.
- **P3 (the core test — does the bump shrink?):** the non-monotonicity
  itself — Q_ext(core=8 cells, the r1_base=5 analog) exceeding
  Q_ext(core=6 cells, the r1_base=4 analog) — either disappears (cpl=30
  curve becomes monotonic, matching exp-006/007's established law) or
  shrinks substantially in relative size (mirroring exp-005's own
  finding of "real but small," e.g. <10% of the cpl=20 bump's relative
  size). A bump of comparable or larger relative size at cpl=30 refutes
  this and means the effect is not primarily a grid artifact of this
  kind.
- **P4 (ratio trend direction holds regardless):** independent of
  whether the cloaked-Q_ext bump itself is real, the ratio
  cloaked/bare at cpl=30 still breaks above exp-008's ~0.193 plateau by
  core=7-cells-equivalent (r1_base=4) — i.e. the qualitative finding
  that the plateau does not extend flat below core=8 survives the
  resolution check even if the exact bump shape does not.

## Results

*(pending)*

## Next

*(pending)*
