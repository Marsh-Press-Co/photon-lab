# exp-012 — The Floor Sweep at core=40 (exp-006's Candidate C, third generalization point)

## Hypothesis

exp-006 found the exp-004/005 floor-jump investigation's baseline
geometry (core=30, eps_z=2.25) is the *only* one of 4 eps_z points
tested that shows a *negative* jump at floor=0.10→0.18 (−17.7%) — the
other three (eps_z=1.44/3.24/4.59, i.e. core=15/40/48) all show the
"naive" positive direction (wider clamp, worse cloak). exp-011 then
swept the *full* floor range at core=15 (0.10/0.18/0.28/0.40) and found
it **strictly monotonic, no sign-flip anywhere** — unlike core=30's
dip-then-rise shape — strengthening the reframe that core=30/eps_z=2.25
was the atypical geometry, not the norm, to a 2-point comparison
(core=30 non-monotonic vs core=15 monotonic).

exp-011's own logged follow-up, echoed in PLAN.md: a third core/eps_z
point would make this a proper generalization rather than a two-point
comparison. This experiment is that third point: **core=40
(eps_z=3.24)**, exp-006's other already-characterized geometry, whose
existing 0.10→0.18 jump (+70.7%) already points the same "naive"
direction as core=15's.

## Setup

Same fixed domain/box machinery as exp-006 through exp-011 (N=680,
cpl=20, courant_frac=0.32, absorb=40, λ=600nm, R2_CELLS=90 fixed).
**core=40 fixed** (eps_z=(90/(90−40))² = 3.24, exp-006's third-thinnest
shell point).

exp-006 already ran core=40 at **floor=0.10** (Q_ext=0.7540) and
**floor=0.18** (Q_ext=1.2871) — those numbers are reused directly, not
rerun (same convention exp-005/exp-011 used reusing prior points). This
experiment adds two floor points core=40 has never been run at:
**floor=0.05** and **floor=0.28**.

**floor=0.40 is excluded, and the reason is different from exp-011's
exclusion (that one was CFL instability).** Here it's the *degeneracy*
constraint exp-006 itself derived: the clamp only leaves a graded shell
when `mu_r_floor < ((r2−r1)/r2)²` (the natural, unclamped `mu_r` at
r=r2). At core=40, that threshold is `((90−40)/90)² = 0.3086`.
floor=0.40 exceeds it — the *entire* shell would clamp to a uniform
`mu_r_floor`, measuring a qualitatively different thing ("what does a
uniform-mu_r shell scatter") than the graded-clamp-boundary question
this whole investigation line is asking. floor=0.28 sits *just* inside
the threshold (9.3% margin) — deliberately close, to reach as far along
the sweep as the geometry allows without crossing into the degenerate
regime, the same design choice exp-006 made at its own core=48/floor=0.18
point (17.5% margin).

Checked explicitly before committing this file:

| floor | degeneracy threshold | margin | CFL ceiling `√(floor·eps_z)` | CFL margin |
|---|---|---|---|---|
| 0.05 | 0.3086 | 83.8% (graded) | 0.4025 | 25.8% (stable) |
| 0.10 (reused) | 0.3086 | 67.6% (graded) | 0.5692 | 77.9% (stable) |
| 0.18 (reused) | 0.3086 | 41.7% (graded) | 0.7649 | 139.0% (stable) |
| 0.28 | 0.3086 | **9.3% (graded, tight)** | 0.9525 | 197.6% (stable) |
| 0.40 | 0.3086 | **−29.6% (degenerate — excluded)** | 1.1379 | n/a |

Unlike core=15 (where floor=0.05 was the excluded point, on CFL
grounds), core=40's larger eps_z pushes the CFL ceiling comfortably
higher at every floor value tested — floor=0.05 is fine here. It's the
*opposite* end of the sweep (floor=0.40) that becomes unusable, and for
a geometric reason, not a numerical-stability one. Worth noting as its
own small addendum: which end of a floor sweep is excluded, and why,
depends on the specific (core, eps_z) point — not a fixed rule that
transfers between geometries.

3 runs total: 1 fresh empty reference (self-contained per this
experiment file, same convention as exp-006 through exp-011) + 2 new
cloak runs (floor=0.05, floor=0.28).

## Idealizations

Same 2D TMz bench as this whole investigation line. Single core, single
λ=600nm — not a re-run of exp-004's full 4-λ sweep, matching
exp-006/007/008/011's single-anchor-wavelength scope. floor=0.40 is
structurally excluded at this core by the degeneracy threshold (not a
choice made to save runs) — the resulting curve covers 0.05–0.28, a
narrower floor range than exp-004's (core=30) or exp-011's (core=15)
full sweeps, and that narrowing is itself part of what's being reported,
not hidden.

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at both new points, matching exp-006/exp-011's own tight
  gates at nearby geometries (≤1.7%/≤0.5% and ≤1.1%/≤0.1% respectively).
- **P2 (the discriminating prediction):** the floor curve at core=40
  does **not** sign-flip anywhere across the tested range — Q_ext rises
  monotonically through 0.05→0.10→0.18→0.28 (i.e.
  `Q_ext(0.05) < Q_ext(0.10) < Q_ext(0.18) < Q_ext(0.28)`), mirroring
  exp-011's core=15 finding and extending the "naive" direction already
  visible in core=40's own existing 0.10→0.18 jump (+70.7%). If
  confirmed, this makes the generalization a clean 3-for-3: only
  core=30/eps_z=2.25 (the original exp-002/003 baseline geometry) shows
  non-monotonic floor structure; every other core/eps_z point tested
  (15, 40, and by extension likely 48) is monotonic. A sign-flip
  anywhere in this range would refute this and instead support "every
  eps_z sign-flips somewhere, core=30 wasn't special" — reopening the
  question exp-011 looked to have closed.
- **P3 (magnitude, secondary):** the two new jumps
  (`(Q10−Q05)/Q05` and `(Q28−Q18)/Q18`) are both positive and, given
  exp-006's P3 finding that jump magnitude does *not* grow monotonically
  with eps_z, no specific magnitude is predicted — this is tracked for
  completeness, not scored pass/fail the way P2 is.

## Results

*(pending — filled in after the run)*

## Next

*(pending)*
