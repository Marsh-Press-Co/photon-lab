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

## Results

*(pending — machinery reused, no new trust-suite stage needed; running
next.)*
