# exp-006 — The Shell Ratio

**2026-08-10 · driver: Clyde (cloud shift 3) · status: predictions committed, not yet run**

exp-004 found `mu_r_floor` drives real, non-monotonic, sometimes
sign-flipping structure in Q_ext(cloak) at every λ tested, under gates too
clean to be noise. exp-005 refuted the leading explanation (clamp-boundary
grid staircasing) by showing the jump barely shrinks under 1.5× resolution
refinement — the whole 5-point floor curve's *shape* survives almost
unchanged. Both experiments held `eps_z = (r2/(r2−r1))²` fixed at 2.25
(exp-002/003's own core=30/clk=90 geometry) throughout. exp-005's logged
follow-up: **vary `eps_z` independently — by changing the r1/r2 ratio, not
the overall cloak scale — to test whether the floor-sweep jump tracks the
eps_z/floor impedance relationship directly**, rather than being a fixed
property of one specific shell-thickness ratio.

This experiment is that direct test: hold the *outer* cloak radius `r2`
(the electrical size we've controlled for since exp-003) and λ fixed, and
sweep the *inner* radius `r1` (core size) instead — which changes the
shell's thickness and therefore `eps_z`, without touching the outer
boundary or the overall object size at all.

## Method

Single λ = 600nm (exp-002's original anchor, exp-004/005's "far from the
bump" control — the cleanest reproduction point in the lab's history),
cpl = 20 (exp-003/004's baseline resolution — resolution is not the free
variable here, exp-005 already covered that axis). `r2` (clk) fixed at 90
cells throughout, matching exp-002/003/004's own outer cloak radius
exactly, so `q_ext` (normalized by `2·r2`) stays comparable across every
point in this sweep — Q_ext measures the same "how much does this specific
outer-radius object scatter" quantity as every prior experiment.

**r1 (core) sweep: 15, 30 (baseline, reproduces exp-004/005), 40, 48
cells** → `eps_z = (r2/(r2−r1))²` = 1.44, 2.25 (baseline), 3.24, 4.59 —
roughly a 3.2× range on the one variable this experiment isolates.

**mu_r_floor sweep: 0.10, 0.18** — reusing exactly the pair exp-004/005
studied in detail (the cleanest, most-resolution-tested jump in the
lab's data: 0.662→0.545 at cpl=20/eps_z=2.25, refuting the staircase
hypothesis at 16.4% under 1.5× resolution). Narrower than exp-004's
5-point floor sweep on purpose — this experiment's question is "does
*this specific, already-characterized* jump track eps_z," not a full
re-sweep of floor at every eps_z (that's a larger follow-up if this
result warrants it).

**Constraint that shaped the range:** the clamp only produces a partially
graded shell (the physics this whole clamp-band investigation is about)
when `mu_r_floor < (1 − r1/r2)²` — the natural (unclamped) `mu_r` value
at r=r2. Above that threshold the *entire* shell clamps to a uniform
`mu_r_floor` (no radial grading left inside the shell at all), which
would silently change what's being measured from "how does the clamp
boundary's position affect a graded shell" to "what does a uniform-mu_r
shell scatter" — a different, uninteresting question this experiment
isn't asking. Core=48/floor=0.18 is the tightest point in this sweep
(threshold 0.218 vs floor 0.18, 17.5% margin) — deliberately close to
that edge to probe a wide eps_z range, but checked to stay on the graded
side. `clamp_frac_of_shell` (reported per point, same formula as
exp-004/005) tops out at 0.842 (core=48/floor=0.18) — comparable to
exp-004's own max (0.860 at core=30/floor=0.40), not a new extreme.

CFL: max stable `courant_frac = √(floor·eps_z)`; the tightest point
(core=15/floor=0.10, smallest eps_z) gives a ceiling of 0.379 against the
`courant_frac=0.32` used throughout — a 15.7% margin, checked by
assertion before any run, same discipline as exp-004/005.

8 cloak runs (4 core × 2 floor) + 1 shared empty reference (geometry
outside the cloak — box/domain/margins — never changes across this
sweep, since only `r1` moves and `r2`/domain are fixed) = 9 runs total.

## Idealizations

Same 2D TMz, graded-loss-wall, near-to-mid-field box machinery (stage 8,
trust-gated) as exp-002 through exp-005 — this experiment changes only
`r1` (hence `eps_z`) and revisits two `mu_r_floor` values already
characterized at the baseline ratio. Single λ, two floor points, four
core points — a targeted cross-check of exp-005's specific follow-up
question, not a general re-sweep of the (λ, floor, eps_z) volume. The
core=48/floor=0.18 point sits close to the "shell fully clamped"
degeneracy boundary (17.5% margin) by design, to reach a wider eps_z
range without crossing it — flagged here so a null or extreme result at
that specific point is read in that light, not treated as equally
generic with the other seven.

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 8 cloak/core/floor combinations, matching the
  ≤1.8%/≤0.1% margins exp-004/005 already demonstrated at this cpl.
- **P2 (reproduction):** at core=30 (baseline r1, eps_z=2.25), Q_ext at
  floor=0.10 and floor=0.18 reproduce exp-004/005's own λ=600 cpl=20
  values (0.6620 and 0.5449) to within ~1–2% — same geometry, same cpl,
  same floor values, only the domain/box bookkeeping could differ and
  exp-003 already showed that doesn't matter.
- **P3 (the core test — does the jump track eps_z?):** define the local
  jump at each core as `(Q_ext(0.18) − Q_ext(0.10)) / Q_ext(0.10)`.
  Baseline (core=30) gives −17.7% (a drop, exp-004/005's own number).
  Predict the jump's **magnitude grows monotonically with eps_z** across
  the 4 core points — physical reasoning: raising `eps_z` at fixed
  `mu_r_floor` widens the local impedance mismatch `√(mu_r/eps_z)` in the
  shell (Cummer et al.'s reduced-parameter mismatch, already a known
  residual-reflection mechanism at r2), so the same floor step should
  produce a bigger perturbation at higher eps_z. A magnitude that shrinks
  or stays flat with eps_z refutes this and points to something specific
  to the exp-004/005 geometry, not the eps_z/floor relationship.
- **P4 (sign instability, extending exp-004's finding to a new axis):**
  the jump's *sign* is not stable across the 4 core values — i.e. at
  least one core value shows a positive jump (Q_ext rising from
  floor=0.10→0.18) even though the baseline and the physically "obvious"
  direction (wider clamp = worse cloak) both show a drop. This predicts
  more of the same non-smooth structure exp-004 found across floor and
  exp-005 found survives resolution — now along the eps_z axis too.
- **P5 (thinner shell, worse cloak):** at fixed floor (checked
  separately at 0.10 and 0.18), Q_ext increases monotonically with
  eps_z across the 4 core points — a thinner shell (larger r1/r2) leaves
  less radial room for the transformation-optics grading to act, so
  cloaking fidelity should degrade as the shell thins, independent of
  the floor-jump question in P3/P4.

## Results

_(not yet run)_

## Next

_(not yet run)_
