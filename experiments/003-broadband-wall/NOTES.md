# exp-003 — The Broadband Wall, Redesigned

**2026-08-10 · driver: Clyde (cloud shift) · status: predictions committed, machinery pending**

exp-002 found the reduced cloak's Q_ext improving monotonically toward red
(0.515 → 0.384 → 0.303 at 450/600/750 nm) and logged a working hypothesis:
the cloak's fixed-size fabrication defects (the mu_r clamp band, the
staircase discretization of its circular walls) become electrically
smaller — smaller relative to λ — as wavelength grows, predicting
degradation ∝ (defect/λ)². But that sweep left grid resolution
**confounded** with wavelength: cells-per-λ (cpl) ran 15/20/25 across the
same 450/600/750 sweep, so a coarser grid at blue and a finer grid at red
could have produced the same trend for a purely numerical reason (more
staircase/dispersion error where cpl is small) — nothing to do with the
cloak's physics. exp-001 flagged this explicitly before exp-003 was named:
*"grid resolution co-varies with wavelength in this sweep ... exp-003 must
separate them (fixed cells-per-λ with scaled geometry) before the
asymmetry is claimed as material physics."* This experiment is that
separation.

## Method

**Hold cells-per-λ fixed at 20 for every run in the sweep** (the
resolution knob, previously varying 15→25, is now a constant — numerical
dispersion/staircase error per wavelength-cycle is identical at every
sweep point). To still vary the cloak's *electrical* size relative to λ,
**scale the geometry** (in cells) so its *physical* size (nm) stays fixed
as λ changes — exactly mirroring a real fabrication defect of fixed
physical dimension viewed at different colors.

Anchor: exp-002's λ=600nm/cpl=20 point used a 30nm cell (dx = 600/20) and
geometry R_core/R_coat/R_clk = 30/78/90 cells → 900/2340/2700 nm. exp-003
keeps those physical sizes fixed and recomputes cell counts from a single
scale factor `f(λ) = 600nm / λ`:

    R_core(λ) = round(30 · f),  R_coat(λ) = round(78 · f),  R_clk(λ) = round(90 · f)
    box_A_half(λ) = round(110 · f),  box_B_half(λ) = round(135 · f)

with cpl = 20 fixed at every λ. **The λ=600nm point is geometrically
identical to exp-002's λ=600/cpl=20 run** (f=1, same integer radii) — a
built-in reproduction check on the new harness before trusting the new
points. Domain (N=560, absorb=40), source position (x=64), step count
(3200), and courant fraction (0.32) are unchanged from exp-001/002 — all
six sweep geometries were checked by hand to fit inside the absorbing
boundary with the same margins as the exp-002 baseline (worst case,
λ=420nm: box_B half=193 cells, 59–445 in x, 87–473 in y, inside the
40–520 usable window).

Sweep: λ ∈ {420, 480, 540, 600, 660, 750} nm (6 points; 600 is the
cross-check anchor). Same three dressings + empty reference as exp-002,
same `lab.sections` machinery (already trust-gated, stage 8), same two
boxes for independence.

**Electrical size** reported per scene = 2·R_outer(nm) / λ(nm), where
R_outer(nm) is the *fixed* physical outer radius (900/2340/2700 nm for
reflector/absorber/cloak) — this ratio now varies *only* because λ
changes, not because of any change in grid fidelity.

## Idealizations

Same 2D TMz, graded-loss-wall (not PML), near-to-mid-field box machinery
as exp-002; "electrical size" collapses several distinct fixed-scale
defects (mu_r clamp band width, staircase step) into one nm-scale number
even though they don't necessarily share the same (defect/λ)² exponent —
this sweep tests the aggregate trend, not a first-principles derivation of
the exponent. Six points is enough to see a trend and a rough slope, not
enough to pin an exponent precisely — a stated limit, not a claim we don't
have data for.

## Predictions — committed before the run

- **P1 (gates, reused from stage 8):** box independence ≤ 2% and the two
  extinction routes (face-flux vs cross-term) agree ≤ 2% at every scene
  and wavelength, matching exp-002's demonstrated ~0.2–1% margins at
  varied geometry sizes.
- **P2 (reproduction check):** the λ=600nm point reproduces exp-002's
  λ=600/cpl=20 numbers closely (same geometry, same cpl, deterministic
  solver → expect agreement within ~1%, not just "roughly the same").
- **P3 (the core test — cloak):** with resolution now held fixed, Q_ext
  for the cloak still decreases monotonically as λ increases across all 6
  points (matching exp-002's direction). If the trend **flattens or
  reverses** once resolution is controlled, that refutes (defect/λ)² as
  the dominant driver and points at grid resolution as the real cause of
  exp-002's asymmetry.
- **P4 (rough exponent):** on a log-log plot of Q_ext(cloak) vs electrical
  size (2·R_clk/λ), the fitted slope falls in **[1.5, 3.0]** — a wide but
  falsifiable band consistent with a (defect/λ)²-type power law, not a
  precise claim given 6 points and 2D FDTD noise.
- **P5 (controls — reflector, absorber):** both should stay close to
  exp-002's flat baselines regardless of the geometry-scaling harness:
  reflector Q_ext within ±10% of ~2.2 at every λ (extinction paradox,
  scale-invariant for a scaled PEC disk); absorber abs/ext ≈ 0.5 and
  back_frac ≤ 10⁻³ at every λ (broadband-black character, unaffected by
  the scaling exercise). A control that drifts would mean the scaling
  harness itself has a bug, not new physics.

## Method amendment — a domain-sizing bug, caught before trusting the data

First run (N=560, box halves scaled from exp-002's CX=252 center, same
formula as everything else) blew up **box independence** at the largest
scale factor (λ=420nm, f=1.4286): box_dev 2–6 (200–600%!) vs 0.003–0.009
at every other sweep point, uniformly across all three scenes — a
same-sized failure on the plain PEC reflector as on the cloak, which
ruled out "cloak physics" as the cause immediately. Root cause: box_b's
edge sat only 19 cells from the absorbing boundary at that factor (margin
shrinks as `212 − box_half·f`, unnoticed when the margin was eyeballed
only at f=1 during design). Patching only the broken point would have
introduced exactly the domain-size confound this experiment exists to
eliminate, so the whole domain was grown instead (N 560→680, CX/CY
252/280→300/300, STEPS 3200→3600, plus an explicit ≥60-cell margin
assertion) and the **full sweep was rerun** — nothing from the first run
is in the numbers below. Post-fix: box_dev ≤ 1.1%, cross-route agreement
≤ 0.2%, at all 6×3 = 18 scene/λ combinations.

## Results

18 scene/λ combinations, 21 min (24 runs incl. empty references).

| λ (nm) | elec (cloak) | Q_ext refl | Q_ext abs | abs/ext | back (abs) | **Q_ext cloak** | abs/ext (cloak) | back_frac (cloak) | box_dev max |
|---|---|---|---|---|---|---|---|---|---|
| 420 | 12.86 | 2.134 | 1.571 | 0.514 | 5e-8 | **0.460** | −0.003 | 0.235 | 0.004 |
| 480 | 11.25 | 2.132 | 1.558 | 0.514 | 2e-7 | **0.491** | 0.010 | 0.196 | 0.003 |
| 540 | 10.00 | 2.176 | 1.543 | 0.513 | 7e-7 | **0.408** | −0.001 | 0.220 | 0.001 |
| 600 | 9.00 | 2.207 | 1.539 | 0.512 | 2e-6 | **0.386** | 0.006 | 0.256 | 0.003 |
| 660 | 8.18 | 2.240 | 1.527 | 0.512 | 6e-6 | **0.323** | 0.010 | 0.305 | 0.011 |
| 750 | 7.20 | 2.240 | 1.514 | 0.513 | 4e-5 | **0.318** | 0.001 | 0.285 | 0.007 |

(elec = 2·R_outer(fixed nm) / λ, the object's electrical size; box_dev =
|σ_ext(box A) − σ_ext(box B)| / σ_ext(box A); i_inc = 2.4849 identically
at every λ, as expected — cpl fixed means the empty-room physics genuinely
does not know which nm label we attached to it, a free consistency check
on the harness.)

### Predictions scored

- **P1 (gates) — CONFIRMED**, after the domain fix above: box_dev ≤ 1.1%
  and cross-route agreement ≤ 0.2% at every point, both comfortably under
  the 2% band.
- **P2 (reproduction check) — CONFIRMED.** The λ=600 point (same cpl,
  same integer radii/box halves as exp-002's λ=600 run, different domain
  center/size) reproduces exp-002 tightly: Q_ext reflector 2.207 vs
  2.208 (0.03%), absorber 1.539 vs 1.539 (0.02%), cloak 0.386 vs 0.384
  (0.5%). The new harness is trustworthy before trusting its new points.
- **P3 (the core test) — partially confirmed, partially refuted.** With
  resolution now held fixed, the cloak's Q_ext still falls net across the
  sweep — 0.460 at 420nm to 0.318 at 750nm, a 31% drop — confirming the
  red-side improvement is not purely a resolution artifact: exp-002's
  finer grid at long λ was not manufacturing the trend. But the sequence
  is **not monotonic**: 480nm (0.491) sits *above* both 420nm (0.460) and
  540nm (0.408) — a bump exp-002's 3-point sweep could not have shown.
  Something structural happens between elec ≈ 11–13 that a clean
  (defect/λ)ⁿ story doesn't predict.
- **P4 (rough exponent) — REFUTED.** Log-log fit of Q_ext(cloak) vs
  electrical size across all 6 points: **slope ≈ 0.79 (R² = 0.87)**,
  well below the predicted [1.5, 3.0] band. Whatever is driving the
  red-side improvement, it is far shallower than a (defect/λ)² law —
  closer to linear-in-electrical-size than quadratic. The 480nm bump
  drags the fit down further (a slope fit to the 4 monotonic points
  540→750 alone is closer to ~0.9, still nowhere near 2) — this isn't
  just noise from one outlier point.
- **P5 (controls) — CONFIRMED.** Reflector Q_ext stays in [2.13, 2.24]
  (< 5% spread, inside the predicted ±10% band) — same mild red-drift
  exp-002 saw, scale-invariant as predicted, so the scaling harness isn't
  itself introducing drift. Absorber abs/ext holds at 0.512–0.514 and
  back_frac stays ≤ 4×10⁻⁵ at every λ (three orders of magnitude inside
  the ≤10⁻³ ask) — broadband-black character survives the geometry
  rescaling exercise untouched.

### The finding

**The red-side improvement is real, not a resolution artifact — exp-001's
flagged confound is resolved — but it is not the clean (defect/λ)² story
exp-002 guessed at.** Holding cells-per-λ fixed removes the numerical
explanation cleanly (P2's reproduction + P3's confirmed net trend), so
whatever produces exp-002's asymmetry lives in the field's actual
interaction with the cloak's fixed-parameter shell, not in grid error.
But the relationship is shallower (~elec^0.8, not elec²) and has real
structure the 3-point sweep hid: a local rise at 480nm before the
familiar improvement resumes. One candidate explanation, not yet tested:
the mu_r clamp band (§ Method, `schurig_reduced_cloak_tm`'s
`mu_r_floor=0.05`) has a *fixed radial extent relative to r1* by
construction (~0.29·r1, see materials.py's derivation comment) — as the
whole cloak scales, that band's absolute cell-width scales too, but its
angular/staircase interaction with the fixed grid does not scale the same
way, which could produce exactly this kind of non-monotonic residual.
Distinguishing "clamp-band effect" from "staircase effect" would need a
sweep that varies `mu_r_floor` independently of geometry — logged below,
not run this shift.

## Next

- **exp-004 candidate:** hold electrical size and cpl both fixed, sweep
  `mu_r_floor` alone, to test whether the clamp band (not staircase) is
  responsible for the 480nm bump and the sub-quadratic exponent.
- exp-001 observer-table rerun post phasor fix — still queued.
- Parking lot (unchanged from exp-002): absorber-vs-cloak hybrid (eat the
  backward glint), Q_ext vs incidence angle, near-to-far transform for
  true far-field patterns.
