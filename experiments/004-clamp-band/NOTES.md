# exp-004 — The Clamp Band

**2026-08-10 · driver: Clyde (cloud shift) · status: predictions committed, machinery pending**

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

*(pending — machinery not yet run)*
