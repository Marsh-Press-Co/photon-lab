# exp-011 — The Floor Sweep at core=15 (exp-006's Candidate B)

## Hypothesis

exp-006 found the exp-004/005 floor-jump investigation's baseline
geometry (core=30, eps_z=2.25) is the *only* one of 4 eps_z points
tested that shows a *negative* jump at floor=0.10→0.18 — the other
three (eps_z=1.44/3.24/4.59) all show the "naive" positive direction
(wider clamp, worse cloak), with core=15/eps_z=1.44 showing the
*strongest* positive jump of the four (+177.5%). exp-006 logged this
open (its own "candidate B"): does core=15 show the *same kind* of
non-monotonic, sign-flipping floor structure exp-004 characterized at
core=30 across the *full* floor range, or was core=30's specific
jumpiness (dip at 0.18, then rise through 0.28/0.40) an eps_z=2.25
peculiarity that doesn't generalize?

This experiment is that direct test — the exact candidate B queued in
PLAN.md.

## Setup

Same fixed domain/box machinery as exp-006/007/008/009 (N=680, cpl=20,
courant_frac=0.32, absorb=40, λ=600nm, R2_CELLS=90). **core=15 fixed**
(eps_z=1.44, exp-006's own "thickest-shell" tested point and the
geometry behind exp-007's design-lead chase).

exp-006 already ran core=15 at **floor=0.10** (Q_ext=0.09336) and
**floor=0.18** (Q_ext=0.25916) as part of its own 4-eps_z × 2-floor
grid — those numbers are reused directly, not rerun (same convention
exp-005 used reusing exp-004's cpl=20 baseline). This experiment adds
the two floor points exp-004's original 5-point sweep covered that
core=15 has never been run at: **floor=0.28 and floor=0.40**.

**floor=0.05 is excluded, and this matters:** the CFL ceiling
`sqrt(floor·eps_z)` depends on eps_z as well as floor — exp-004's own
floor=0.05 point was only stable at its core=30/eps_z=2.25 geometry
(ceiling 0.335 against courant_frac=0.32, a slim 4.5% margin already
flagged as the edge of what's tested). At core=15's smaller eps_z=1.44,
that same floor=0.05 point's ceiling drops to **0.268 — below
courant_frac=0.32**, i.e. genuinely unstable, not just tight. Checked
explicitly before committing this file:

| floor | eps_z=1.44 ceiling | margin |
|---|---|---|
| 0.05 | 0.2683 | **−16.1% (unstable)** |
| 0.10 | 0.3795 | 18.6% |
| 0.18 | 0.5091 | 59.1% |
| 0.28 | 0.6350 | 98.4% |
| 0.40 | 0.7589 | 137.2% |

This sharpens the standing PLAN.md item ("`mu_r_floor < 0.05` remains
untested, needs a paired `courant_frac` cut") — it is not only the
region *below* 0.05 that needs a frac cut at low-eps_z geometries;
floor=0.05 *itself* already crosses into instability once the shell is
thick enough (core=15 vs core=30). Not chased further this shift (a
deliberate frac cut for this one point is a small, separate, well-
scoped follow-up, not bundled into this sweep) — the 4 stable points
(0.10/0.18/0.28/0.40) are enough to test the discriminating question.

3 runs total: 1 fresh empty reference (self-contained per this
experiment file, same convention as exp-006/007/008/009) + 2 new cloak
runs (floor=0.28, 0.40).

## Idealizations

Same 2D TMz bench as this whole investigation line. Single core, single
λ=600nm — not a re-run of exp-004's full 4-λ sweep, matching
exp-006/007/008's single-anchor-wavelength scope.

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at both new points (matching exp-006's own tight gates at
  this geometry, ≤1.7%/≤0.5%).
- **P2 (the discriminating prediction):** the floor curve at core=15
  does **not** sign-flip again after 0.18 — Q_ext rises monotonically
  through 0.18→0.28→0.40 (i.e. `Q_ext(0.28) > Q_ext(0.18)` and
  `Q_ext(0.40) > Q_ext(0.28)`), mirroring exp-004/005's own core=30
  finding that the *back half* of its floor sweep (0.18→0.28→0.40) was
  monotonically rising even though the *front half* (0.05→0.10→0.18)
  wasn't. If core=15 also rises monotonically through this same back
  half with no further dip, that supports exp-006's reframe — core=30's
  full-range non-monotonicity (specifically its 0.10→0.18 dip) may be
  the eps_z=2.25-specific peculiarity, not evidence that "every eps_z
  has its own independent sign-flipping structure." A second dip
  anywhere in 0.18→0.28→0.40 would refute this and support the opposite
  reading — non-monotonic floor structure recurring at a different
  location for a different eps_z, strengthening "every eps_z sign-flips
  somewhere" over "core=30 was the outlier."

## Results

*(pending)*

## Next

*(pending)*
