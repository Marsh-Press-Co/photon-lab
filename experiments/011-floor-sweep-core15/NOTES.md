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

3 runs (2 cloak + 1 empty), 2.5 min. CFL check matched the pre-registered
table exactly (floor=0.05 unstable as predicted, 0.28/0.40 both stable
with large margins).

Full core=15 floor curve, combining exp-006's existing points with this
experiment's two new ones:

| mu_r_floor | Q_ext | box_dev | cross_dev |
|---|---|---|---|
| 0.05 | — (CFL-unstable, not run) | — | — |
| 0.10 | 0.0934 (exp-006) | 0.013 | 0.005 |
| 0.18 | 0.2592 (exp-006) | 0.003 | 0.002 |
| 0.28 | **0.5242** (new) | 0.011 | 0.001 |
| 0.40 | **0.7818** (new) | 0.011 | 0.001 |

### Predictions scored

- **P1 (gates ≤2%)** — CONFIRMED. box_dev 1.1% at both new points,
  cross_dev 0.1% at both — comfortably inside the threshold and
  consistent with exp-006's own clean gates at this geometry.
- **P2 (no further sign-flip past 0.18)** — CONFIRMED, cleanly. The full
  4-point curve (0.0934 → 0.2592 → 0.5242 → 0.7818) is **strictly
  monotonically increasing** with no exceptions anywhere — not just the
  0.18→0.28→0.40 back half this experiment tested, but the *entire*
  tested range including the 0.10→0.18 jump exp-006 already
  characterized. core=15/eps_z=1.44 shows **zero sign-flipping
  structure** across every floor value tested at this geometry.

### Headline — the reframe holds, sharpened

exp-006's candidate B is answered: core=15 does **not** replicate
exp-004/005's core=30 non-monotonic floor curve (which rose 0.05→0.10,
dipped at 0.18, then rose again through 0.28→0.40). At core=15, the
relationship is exactly the "naive" one — wider clamp (`mu_r_floor`
value approaching 1, closer to no clamp at all), worse cloak, no
exceptions. Two independent core/eps_z values have now been swept
across most of the floor range (core=30 in exp-004/005: non-monotonic;
core=15 here: fully monotonic) — this strengthens exp-006's reframe
from "possibly atypical" to a working conclusion: **the exp-004/005
non-monotonic floor-jump was a property of the specific eps_z=2.25
baseline geometry, not a general feature of the `mu_r_floor` knob.**
Two shifts' worth of careful resolution-convergence work on that jump
(exp-004→exp-005) characterized something real but geometry-specific,
not the norm this investigation line initially took it for.

## Next

- One core/eps_z point (core=40, exp-006's other suggested candidate)
  would make this a 3-point generalization rather than 2 — worth a
  cheap follow-up if this reframe needs further confirmation before
  being treated as settled.
- The floor=0.05 CFL-instability found here (not just below 0.05, but
  the value itself, at low-eps_z/thick-shell geometries) is a genuine
  addition to the standing `mu_r_floor < 0.05` PLAN.md item — any future
  work sweeping floor at core values below ~20 or so should check the
  CFL ceiling per-point rather than assuming exp-004's core=30 margin
  carries over.
- This shift's three-experiment arc (009→010→011) is a complete,
  self-contained unit: a design-lead follow-up that failed its own
  gate, a resolution check that resolved the failure and the physics
  question together, and a cheap closeout of a previously-logged open
  item. All three commits are gated, honest, and build on each other —
  a good shift to end on.
