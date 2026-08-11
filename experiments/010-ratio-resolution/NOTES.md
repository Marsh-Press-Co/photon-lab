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

9 runs (4 bare + 4 cloaked + 1 empty), 19.4 min. CFL margins matched the
pre-registered table exactly (3.42–6.73%, all `OK`).

| base (cpl=20) | r1 (cpl=30 cells) | Q_ext bare (30 / 20) | Q_ext cloak (30 / 20) | ratio (30 / 20) | box_dev cloak (30 / 20) |
|---|---|---|---|---|---|
| 4 | 6 | 0.1309 / 0.1242 | 0.0373 / 0.0351 | 0.285 / 0.283 | **0.005** / 0.035 |
| 5 | 8 | 0.1640 / 0.1541 | 0.0377 / 0.0424 | 0.230 / 0.275 | **0.002** / 0.023 |
| 6 | 9 | 0.1810 / 0.1763 | 0.0392 / 0.0413 | 0.217 / 0.235 | **0.000** / 0.020 |
| 7 | 10 | 0.1982 / 0.1970 | 0.0423 / 0.0365 | 0.213 / 0.185 | **0.003** / 0.018 |

### Predictions scored

- **P1 (the gate itself improves) — CONFIRMED, strongly.** Cloak
  box_dev drops from 3.5%/2.3%/2.0%/1.8% at cpl=20 to
  **0.5%/0.2%/0.0%/0.3%** at cpl=30 — an order of magnitude improvement,
  now tighter than exp-005's own "cleanest gate margins" record (base=6
  literally hits 0.04%). `sigma_abs` also shrinks toward zero in
  relative terms at every point (e.g. base=4: −1.6% of `sigma_ext` at
  cpl=20 → −0.41% at cpl=30). This confirms exp-009's read: the gate
  failure was cpl=20 under-resolving the graded `mu_r` profile near a
  very small inner radius, not a sign of anything wrong with the
  physics or the harness.
- **P2 (rough reproduction, ±20%) — CONFIRMED.** Largest single drift is
  base=7's cloaked point at +15.9% (0.0365→0.0423); every other point
  is within ±11%, most within ±7%. Notably, base=7's point is exactly
  the one that carried the *worst* distortion at cpl=20 (the bump's
  dip) — the point with the most resolution bias to begin with drifted
  the most under refinement, consistent with the bump being an artifact
  rather than noise.
- **P3 (does the bump shrink or vanish?) — CONFIRMED, and the bump
  vanishes essentially completely.** cpl=20's non-monotonic curve
  (0.0351→0.0424→0.0413→0.0365, peak-then-dip) becomes **cleanly
  monotonic** at cpl=30 (0.0373→0.0377→0.0392→0.0423, strictly
  increasing with core, exactly the direction exp-006/007's law
  predicts). The base=4→5 step is nearly flat (+1.1%, plausibly within
  remaining discretization noise) rather than the sharp +20.8% rise
  cpl=20 showed — the "bump" was cpl=20's own resolution artifact on
  this very-thin-shell geometry, not a new physical regime below
  core~8. exp-006/007's monotonic law now extends cleanly through the
  full explored range, r1=6 cells up through core=30.
- **P4 (ratio still breaks above the plateau) — CONFIRMED, and more
  cleanly than at cpl=20.** All four cpl=30 ratios (0.213–0.285) sit
  well above exp-008's ~0.193–0.194 plateau, with a clean **monotonic**
  trend (ratio rises as core shrinks, base=7→4) — unlike cpl=20, where
  the same claim was true but the curve itself wasn't smooth. Worth
  flagging explicitly: cpl=20's base=7 point (ratio=0.185) had
  *undershot* the plateau, which read at the time as "the plateau does
  break, just not uniformly" — the resolved cpl=30 number (0.213) shows
  that undershoot was itself resolution bias, not a real dip below the
  plateau. The corrected, gate-clean picture is simpler than exp-009
  could establish alone: the ratio rises smoothly and monotonically as
  core shrinks below 8, no exceptions.

### Headline

exp-009's anomaly is resolved cleanly in both directions predicted:
**the gate failure and the non-monotonic bump were the same resolution
artifact**, both essentially gone at 1.5× cells-per-λ. What survives,
now on solid footing: exp-006/007's monotonic Q_ext(core) law extends
without exception down to r1=6 cells (the smallest core tested in this
lab to date), and the cloaked/bare ratio — flat at ~0.193–0.194 across
core=8–12 (exp-008) — **rises smoothly below core=8**, reaching ~0.28 at
the equivalent of core=4. Read together with exp-007's own finding that
absolute Q_ext improvement *slows* below core~15: the shell's *relative*
suppression effectiveness also degrades once the hidden core shrinks
past ~8, not just the rate of absolute improvement. Shrinking the core
further keeps helping in absolute terms, but buys proportionally less
each step — two independent signs of the same diminishing-returns
regime, not one.

## Next

- The lab's best-characterized cloak design remains core=8/floor=0.10
  (exp-007/008) — this experiment does not unseat it (Q_ext continues
  falling below core=8 in absolute terms, per the confirmed monotonic
  law), but sharpens the picture: below core=8, further shrinking helps
  the raw number while the shell does proportionally less of the work,
  useful context for any future design read of "how small should the
  core be."
- exp-009's flagged multi-λ follow-up (does the core=8 design lead
  survive across λ, exp-002/003's line) remains open and unstarted,
  now a good candidate for a dedicated shift.
- General lesson for this whole floor/eps_z investigation line: cpl=20
  is evidently *not* uniformly trustworthy for very-thin-shell
  geometries (small r1 relative to r2) — any future work exploring core
  radii below ~8 cells at cpl=20 should budget for a cpl=30 confirmation
  pass before treating the numbers as final, exactly as done here.
