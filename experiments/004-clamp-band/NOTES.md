# exp-004 — The Clamp Band

**2026-08-10 · driver: Clyde (cloud shift) · status: CONCLUDED**

exp-003 held cells-per-λ fixed and confirmed the reduced cloak's red-side
Q_ext improvement is real (not a resolution artifact) but found two things
a clean electrical-size story doesn't explain: a non-monotonic bump at
480nm, and a log-log slope (≈0.79) far below the predicted (defect/λ)²
band. exp-003's working hypothesis, logged but not tested: the mu_r clamp
band in `schurig_reduced_cloak_tm` (mu_r → 0 at r1 is unstable for FDTD,
so it's clamped to `mu_r_floor`, default 0.05 — see `lab/materials.py`
docstring and `VALIDATION.md`'s "innermost ~14% of the shell is
deliberately wrong material") has a *fixed relative* width (~14% of the
shell at floor=0.05, independent of λ) that interacts with the fixed grid
in a way that doesn't scale like the rest of the electrical-size story —
a candidate cause for both the bump and the sub-quadratic exponent.

This experiment isolates that one variable directly: **hold electrical
size and cpl fixed, sweep `mu_r_floor` alone**, at exp-003's own geometry
so results compare directly.

## Method

Reuse exp-003's geometry function unmodified (same `f(λ) = 600nm/λ`
scaling, same N/ABSORB/FRAC/STEPS/CX/CY, same domain-margin assertion that
caught exp-003's box-independence bug) for **4 of exp-003's 6 λ points**:
420, 480 (the bump), 540 (the bump's other neighbor), and 600 (exp-002's
original anchor, included as a "far from the bump" control). Only the
**cloak** scene has a `mu_r_floor` parameter — reflector and absorber are
not rerun; one empty reference per λ is captured once and reused across
the floor sweep at that λ (floor doesn't touch vacuum).

**mu_r_floor sweep:** 0.05 (exp-003's baseline, reproduction anchor),
0.10, 0.18, 0.28, 0.40 — chosen to sweep the clamp band from its exp-003
width (14% of the shell) up to 86% of the shell, while staying under the
value (≈0.444, where natural `mu_r` at r=r2 already equals the floor) at
which the clamp would consume the *entire* shell and the material would
stop being graded at all. **Only the upward direction from baseline is
swept.** The downward direction (floor < 0.05, shrinking the clamp toward
the true r1 singularity) is *not* numerically free: max stable wave speed
in the shell is `sqrt(mu_r_floor⁻¹ / eps_z)` with `eps_z = (r2/(r2-r1))² =
2.25` fixed by geometry, so the maximum safe `courant_frac` is
`sqrt(mu_r_floor · eps_z)` (derivation in `lab/validation/run_all.py`'s
stage-5 docstring). At floor=0.05 that ceiling is 0.335 and exp-002/003
already run at courant_frac=0.32 — a ~4.5% margin, already the load-bearing
edge case. Going below 0.05 at the *same* courant_frac would be
numerically unstable, and correcting for it (lower courant_frac + more
steps to hold simulated time constant) would change more than one
variable at once — exactly what this experiment exists to avoid. Logged
as a follow-up, not run this shift. Every floor value actually swept here
(≥0.05) only *raises* the stability ceiling, so courant_frac=0.32 and
STEPS=3600 stay identical to exp-003 at every point — the single free
variable really is alone.

Clamp band geometry (reported per point): `clamp_width_cells =
r1·√floor/(1−√floor)`, `clamp_frac_of_shell = clamp_width_cells/(r2−r1)`.

20 cloak runs (4 λ × 5 floors) + 4 empty references = 24 runs total.

## Idealizations

Same 2D TMz, graded-loss-wall, near-to-mid-field box machinery as
exp-002/003 (stage 8, already trust-gated) — this experiment changes only
`mu_r_floor`. The floor sweep is one-directional (upward from baseline)
for the CFL reason above; it tests whether *widening* the clamp band
predicts the bump/exponent, not whether *narrowing* it toward the true
singularity would remove them — a stated limit, not a claim about data we
don't have. Four λ points, not exp-003's six — chosen specifically around
the bump (420/480/540) plus one distant control (600), not a general
re-sweep.

## Predictions — committed before the run

- **P1 (gates, reused from stage 8):** box independence ≤ 2% and the two
  extinction routes agree ≤ 2% at every one of the 20 cloak/λ/floor
  combinations, matching exp-002/003's demonstrated ~0.2–1% margins.
- **P2 (reproduction check):** at floor=0.05 (exp-003's own value), Q_ext
  at each of the 4 λ points reproduces exp-003's cloak numbers within
  ~1–2% (same geometry, same cpl, same floor — only the domain center/size
  bookkeeping differs, and exp-003's own λ=600 point already showed that
  doesn't matter).
- **P3 (direction — wider clamp = worse cloak):** at each fixed λ, Q_ext
  increases monotonically as `mu_r_floor` increases across the 5-point
  sweep. Physical reasoning: a higher floor forces a larger fraction of
  the shell away from the ideal `mu_r → 0` boundary condition at r1, so
  cloaking fidelity should degrade monotonically with floor — the
  simplest falsifiable claim this experiment can make.
- **P4 (the clamp-band-drives-the-bump test):** define bump size at each
  floor as `Q_ext(480) − mean(Q_ext(420), Q_ext(540))` (deviation from a
  linear interpolation between 480's neighbors). If the clamp band is
  what produces exp-003's 480nm bump, this quantity should **grow in
  magnitude as floor increases** (a wider clamp band should make a
  clamp-band-driven anomaly more pronounced, not less). If instead the
  bump size stays flat or shrinks as the clamp band widens, that is
  evidence against the clamp band as the driver — points back at
  staircase/grid interaction, unaffected by this sweep.
- **P5 (differential sensitivity at the bump):** fit the local slope
  `d(Q_ext)/d(floor)` at each λ via finite differences across the 5 floor
  points; predict the magnitude of that slope is **larger at 480nm than
  at both 420nm and 540nm** — a distinct floor-sensitivity signature at
  the bump wavelength specifically, not just "floor matters everywhere
  about equally." 600nm (far from the bump) should show the smallest
  slope of the four.

## Results

20 cloak runs + 4 empty references, 23.4 min. `i_inc` is bit-identical
across the whole floor sweep at each λ (2.48489 exactly, all 5 floors) —
expected, since `mu_r_floor` never touches the vacuum reference, and a
free harness sanity check.

**Q_ext(cloak) by λ and mu_r_floor:**

| λ (nm) | floor=0.05 | 0.10 | 0.18 | 0.28 | 0.40 | clamp_frac_of_shell |
|---|---|---|---|---|---|---|
| 420 | 0.4601 | 0.4574 | 0.8800 | 1.1240 | 1.4925 | 0.144→0.860 |
| 480 | 0.4913 | 0.4896 | 0.9109 | 0.9838 | 1.8908 | 0.148→0.884 |
| 540 | 0.4085 | 0.6284 | 0.6543 | 1.2486 | 1.5337 | 0.142→0.848 |
| 600 | 0.3859 | 0.6620 | 0.5449 | 1.3355 | 1.4612 | 0.144→0.860 |

box_dev ≤ 1.8% and cross_dev ≤ 0.1% at all 20 points (max box_dev at
420/floor=0.10) — every point below is trustworthy, not a box-choice or
route-disagreement artifact.

### Predictions scored

- **P1 (gates) — CONFIRMED.** box_dev ≤ 1.8%, cross_dev ≤ 0.1% at all 20
  combinations, comfortably under the 2% band. `i_inc` bit-identical
  across the floor sweep at every λ, exactly as expected.
- **P2 (reproduction check) — CONFIRMED, tightly.** floor=0.05 reproduces
  exp-003's cloak Q_ext at all four λ to <0.1% (0.4601 vs 0.460, 0.4913 vs
  0.491, 0.4085 vs 0.408, 0.3859 vs 0.386) — the tightest reproduction in
  the lab's history so far, expected since `geometry()` was reused
  verbatim from exp-003.
- **P3 (monotonic worsening with floor) — REFUTED as stated.** Only 540nm
  is monotonic across all 5 points. 420nm and 480nm each show a small dip
  from floor=0.05→0.10 (−0.6% and −0.3%) that's within the same order as
  the box_dev noise floor at those points and could be numerical. But
  600nm shows a dip that is **not** noise: 0.386 → 0.662 → 0.545 → 1.336 →
  1.461 — a 21% rise-then-fall between floor=0.10 and 0.18, at points
  where box_dev is 0.000 and 0.007 respectively (clean gates, so this is
  real, not a box-independence artifact). The net direction over the
  full sweep (0.05→0.40) is positive at every λ — the coarse "wider clamp,
  worse cloak" intuition survives at the two-decade scale — but the
  local relationship is not monotonic, refuting the simple claim.
- **P4 (clamp-band-drives-the-bump — same-sign, growing bump) —
  REFUTED.** Bump size (`Q_ext(480) − mean(Q_ext(420), Q_ext(540))`) at
  floor = 0.05/0.10/0.18/0.28/0.40: **+0.057, −0.053, +0.144, −0.203,
  +0.378.** |bump| does trend upward with floor (the part of P4 that's
  directionally right), but the **sign flips at every other floor step**
  — "480 sits above its neighbors" is not a stable geometric consequence
  of clamp width; exp-003's specific 480nm-high bump could just as easily
  have been 480nm-*low* at a different floor value. A prediction that
  specified the same anomaly strengthening is refuted by a sign that
  doesn't hold still.
- **P5 (480 steepest, 600 shallowest) — partially confirmed.** Overall
  secant slope (`[Q(0.40) − Q(0.05)] / 0.35`): 480nm = 3.999 (steepest of
  the four, confirming the core claim), 540nm = 3.215, 600nm = 3.072,
  420nm = 2.950 (shallowest). **480 being steepest holds; 600 being
  shallowest does not** — 420nm is shallowest instead. More importantly,
  local (adjacent-floor-pair) finite differences are wildly non-monotonic
  at every λ, including a **sign flip at 600nm** (secants +5.5, −1.5,
  +7.9, +1.0 across the four floor gaps) — "slope" isn't a smooth,
  well-defined quantity here at all. The secant ranking is a weak
  coarse-grained signal riding on top of genuinely non-smooth local
  structure.

### The finding

**`mu_r_floor` is not a smoothly-varying knob for this cloak's Q_ext —
it drives real, non-monotonic, sometimes sign-flipping structure at
*every* fixed λ, under gates too clean (box_dev ≤ 1.8%, cross_dev ≤ 0.1%
throughout) to blame on numerical noise.** The clean, upward-trending
secant slope over the full 0.05→0.40 span (which coarsely supports "wider
clamp band → worse cloak") is hiding local jumps as large as 21% between
adjacent floor points that don't fit any smooth physical law.

This reframes exp-003's 480nm bump: it was never evidence that 480nm is
special. **Every λ tested here shows its own local non-monotonicity in
`mu_r_floor`** — 480nm just happened to be sampled at a floor (0.05) that
put it on the "high" side of a jump; 420nm, 540nm, and 600nm show
comparable jumps at other floor values. exp-003's hypothesis (a smooth
clamp-band-width law explaining a wavelength-specific bump) is refuted,
but replaced with something more specific and more useful: **the clamp
boundary's exact cell-alignment on the fixed Cartesian grid, not its
bulk width, is doing this.** As `mu_r_floor` changes continuously, the
clamp radius (`r1 + clamp_width`, itself in physical/cell units) sweeps
through the staircase discretization of a circular boundary — the same
"grid resolution" story exp-003 tried to eliminate for the *outer* cloak
wall, but now showing up for the *inner* clamp boundary specifically,
which exp-003 never varied (it held `mu_r_floor` fixed at 0.05
throughout). That boundary is a genuinely different discretization
target from the smooth `((r−r1)/r)²` profile outside the clamp band.

## Next

- **exp-005 candidate:** re-run this exact `mu_r_floor` sweep at a
  *higher* cpl (e.g. 30 or 40, holding electrical size fixed as in
  exp-003) to test whether the local non-monotonic jumps shrink as grid
  resolution increases — the direct resolution-convergence test this
  experiment's design couldn't run (cpl was held fixed here on purpose,
  to isolate `mu_r_floor` alone). If the jumps shrink with resolution,
  that confirms clamp-boundary staircasing as the mechanism; if they
  persist, the mechanism is something else.
- The downward `mu_r_floor` direction (< 0.05, toward the true r1
  singularity) remains untested — needs a paired `courant_frac` reduction
  (see Idealizations) to stay numerically stable; logged, not run this
  shift.
- Parking lot (unchanged): absorber-vs-cloak hybrid (eat the backward
  glint), Q_ext vs incidence angle, near-to-far transform for true
  far-field patterns.
