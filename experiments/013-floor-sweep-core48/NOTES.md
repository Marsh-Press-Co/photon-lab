# exp-013 — The Floor Sweep at core=48 (exp-006's Candidate D, fourth and last generalization point)

## Hypothesis

exp-006 characterized 4 core/eps_z points (15/30/40/48 → eps_z
1.44/2.25/3.24/4.59) at floor=0.10/0.18, finding only core=30
(eps_z=2.25, the original exp-002/003 baseline) shows a *negative*
0.10→0.18 jump — the other three all point the "naive" direction (wider
clamp, worse cloak). exp-011 swept core=15's full floor range and found
it strictly monotonic. exp-012 (this shift, immediately prior) swept
core=40's floor range as far as its degeneracy threshold allows and
found it strictly monotonic too — **3-for-3** against core=30's
non-monotonic curve.

exp-012's own logged follow-up: core=48/eps_z=4.59, exp-006's fourth and
last core point, is the one remaining geometry without a full floor-range
sweep. This experiment closes that out — if it's monotonic too, that's
4-for-4, about as complete a generalization as this particular
investigation line can produce without opening a new experimental axis
(e.g. finer eps_z scanning near 2.25, logged as a separate, larger
follow-up in exp-012).

## Setup

Same fixed domain/box machinery as exp-006 through exp-012 (N=680,
cpl=20, courant_frac=0.32, absorb=40, λ=600nm, R2_CELLS=90 fixed).
**core=48 fixed** (eps_z=(90/(90−48))² = 4.5918, exp-006's thinnest-shell
point — also its own tightest-margin geometry, `clamp_frac_of_shell`
topping out at 0.842 there).

exp-006 already ran core=48 at **floor=0.10** (Q_ext=1.20959) and
**floor=0.18** (Q_ext=1.67510) — reused directly, not rerun. This
experiment adds **floor=0.05** (new low-end point) and **floor=0.20**
(new point, as close to the degeneracy threshold as this geometry
allows — see below).

**core=48's degeneracy threshold is the tightest of the four core
points tested in this whole investigation line:**
`((90−48)/90)² = 0.2178` — well below core=40's 0.3086 (exp-012) and
core=15's 0.6944 (exp-011). That rules out floor=0.28 and floor=0.40 entirely at this
geometry (both exceed 0.2178, both fully degenerate) — this experiment's
upper new point is floor=0.20, sitting inside the threshold by only
8.2%, the tightest margin used anywhere in this series (exp-006's own
core=48/floor=0.18 point was the previous tightest, at 17.5%).

Checked explicitly before committing this file:

| floor | degeneracy threshold | margin | CFL ceiling `√(floor·eps_z)` | CFL margin |
|---|---|---|---|---|
| 0.05 | 0.2178 | 77.0% (graded) | 0.4792 | 49.7% (stable) |
| 0.10 (reused) | 0.2178 | 54.1% (graded) | 0.6778 | 111.8% (stable) |
| 0.18 (reused) | 0.2178 | 17.3% (graded, tight) | 0.9095 | 184.2% (stable) |
| 0.20 | 0.2178 | **8.2% (graded, tightest yet)** | 0.9584 | 199.5% (stable) |
| 0.28 | 0.2178 | **−28.6% (degenerate — excluded)** | — | n/a |
| 0.40 | 0.2178 | **−83.7% (degenerate — excluded)** | — | n/a |

CFL is not the binding constraint anywhere in this sweep (core=48's
large eps_z keeps every ceiling far above `courant_frac`) — same pattern
as exp-012, opposite of exp-011 where CFL was the excluded reason. The
degeneracy threshold alone shapes this experiment's range, and it shapes
it tightly: only a narrow band (0.05–0.20) is testable at this core at
all.

3 runs total: 1 fresh empty reference (self-contained per this
experiment file, same convention as exp-006 through exp-012) + 2 new
cloak runs (floor=0.05, floor=0.20).

## Idealizations

Same 2D TMz bench as this whole investigation line. Single core, single
λ=600nm, same anchor-wavelength scope as exp-006/007/008/011/012. The
tested floor range here (0.05–0.20) is narrower than any prior core
point in this series purely because core=48's shell is thin enough that
the degeneracy threshold bites early — this is reported as a geometric
fact about this core value, not a choice to limit scope.

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at both new points, matching exp-006's own gates at this
  exact geometry (≤1.7%/≤0.4%) and exp-012's (≤0.5%/≤0.1%).
- **P2 (the discriminating prediction — completes the 4-point
  generalization):** the floor curve at core=48 does **not** sign-flip
  anywhere across the tested range — Q_ext rises monotonically through
  0.05→0.10→0.18→0.20 (i.e. `Q_ext(0.05) < Q_ext(0.10) < Q_ext(0.18) <
  Q_ext(0.20)`), mirroring exp-011 (core=15) and exp-012 (core=40) and
  extending the "naive" direction already visible in core=48's own
  existing 0.10→0.18 jump (+38.5%). If confirmed, all 4 of exp-006's
  core/eps_z points have now been checked across their full available
  floor range, and exactly 1 of 4 (core=30/eps_z=2.25) shows
  non-monotonic structure — a real, specific, still-unexplained
  exception rather than "every eps_z sign-flips somewhere." A sign-flip
  here would instead make it 2 of 4, reopening the generalization
  question exp-011/012 looked to be closing.
- **P3 (magnitude, secondary, not scored):** the two new jumps
  (`(Q10−Q05)/Q05` and `(Q20−Q18)/Q18`) are both positive; no specific
  magnitude predicted (exp-006's own P3 already found jump magnitude
  doesn't track eps_z monotonically, and exp-012 confirmed a case where
  a jump can be small — +2.3% — without breaking monotonicity).

## Results

*(pending — filled in after the run)*

## Next

*(pending)*
