# exp-025 — Chromatic Finding: Resolution Check (panel Iteration 2 close-out)

**2026-08-12 · driver: Clyde as panel Director · status: predictions
committed, instrument not yet run**

Direct follow-up to exp-024's Phase 5, not a new panel cycle — this lab's
established precedent (exp-005/010/015/023: cpl×1.5, geometry rescaled to
hold physical size fixed, run before any mechanism claim is trusted)
applied to a specific Red Team finding: exp-024's Phase-5 audit judged the
iteration's own conduct "MINOR ISSUES" and flagged one real, unaddressed
gap — the panel's own R3 meta-rule ("any surprising feature gets a
resolution check before it gets a mechanism debate — and 'artifact' claims
need the check too") was not applied before exp-024 scored its new
chromatic finding (a real, δ_C-clear, ~1.5–1.9% growth of |C| toward red in
the two hard-edged articles, absent in the soft-edged sponge) "CONFIRMED"
and handed it to Phase 5 as a standing result. Director's ruling: accepted
in full, per the same discipline this lab has always applied to exactly
this situation (exp-005, -010, -015, -023 — every prior "surprising
feature" got a same-shift resolution check before any mechanism thread
opened on it).

## What's being checked

exp-024's fallback (±35°) geometry: absorber Δ|C(750)−C(450)| = 0.0114,
PEC Δ = 0.0166, sponge Δ = 0.0003 (noise). EM's own Phase-5 review named
the leading candidate mechanism for the *separate* ±40°-specific floor
anomaly — numerical-dispersion anisotropy, worst at coarse
cells-per-wavelength (cpl) and steep angle — and Red Team's audit connects
the same concern to the chromatic finding: this bench holds Δ = 30 nm fixed
across its 3-λ quadrature, so cpl varies by design (15/20/25 @
450/600/750 nm) and 450 nm is this bench's least-resolved wavelength. A
chromatic C-difference measured between the two worst- and best-resolved
wavelengths in the set is exactly the shape of thing a numerical-dispersion
artifact would produce, and no Δx/cpl convergence check has ever been run
anywhere in the ambient-instrument family (exp-020 or exp-024) — only
angle-count (N5/N9/N17) and plane-distance convergence exist.

## Setup

Rerun absorber + PEC (empty as reference) at the FALLBACK_ANGLES set
(±35°, N=9 — the geometry the chromatic finding was measured on), at
450 nm and 750 nm only — the two ends of the claimed spread. 600 nm is the
unmoved control, already on record from exp-024
(`results_fallback.json`). cpl scaled ×1.5 (this lab's standing factor):
450 nm 15→22 (ratio 1.4667, rounding), 750 nm 25→38 (ratio 1.5200); every
cell-based geometry constant (NX, NY, OBJ, R_OUT, PLANE_X, windows, BOX,
taper, absorb) rescaled by the same per-λ ratio to hold physical (nm)
geometry identical to exp-024's fallback configuration
(`design_geometry.py`, verified: coverage clean at both targets, worst
margin 429/444 cells — enormous headroom, this check was never at risk of
an instrument-margin problem of its own). 54 runs (2 λ × 9 angles ×
3 articles), ≈8–9 min estimated at this bench's per-cell-count scaling.

## Predictions — committed before this experiment's first run

- **P-R1 (coverage/geometry sanity):** both rescaled geometries pass their
  own coverage check with large margin (already verified analytically
  above — this predicts the FDTD run reproduces that, no P1b-style
  surprise expected at this scale of headroom).
- **P-R2 (the resolution-check verdict, two-sided, falsifiable both ways):**
  - **If the chromatic effect is REAL** (this lab's prior, stated honestly:
    every previous "surprising feature vs. grid artifact" question in this
    program — exp-005, -010, -015, -023 — resolved in favor of the real
    effect surviving refinement, not the artifact hypothesis): predict
    Δ|C(750)−C(450)| at the fine resolution stays within **±40% relative**
    of the coarse values (absorber 0.0114 → band [0.0068, 0.0160]; PEC
    0.0166 → band [0.0100, 0.0232]), same sign (|C| still larger at
    750 nm), individual C values shifting by no more than the fine/coarse
    gaps this lab has seen before (exp-005's clearest jump shrank only 7%
    under 1.5× refinement; exp-015's eps_z trough shrank ~7% too — a
    ~10–30% relative change from finer resolution, not zero, is the
    typical size of a genuine small residual grid effect riding on a real
    physical trend, and is compatible with "real effect confirmed").
  - **If the chromatic effect is a numerical-dispersion ARTIFACT**:
    predict Δ|C(750)−C(450)| collapses by **≥70% relative** toward zero at
    the finer resolution (absorber Δ → ≤0.0034; PEC Δ → ≤0.0050) — the
    signature this lab's R3 rule exists to catch, mirroring how a genuine
    staircase/grid artifact is expected to behave under refinement (though
    note: this specific signature has never actually been observed in this
    program's R3 history — R3 has refuted the *artifact* hypothesis every
    time it's been tested here, which is itself relevant context, not a
    predetermined outcome).
- **P-R3 (sponge-control cross-check, no new runs needed):** if P-R2 lands
  on "real," the existing sponge Δ=0.0003 (noise-level, no rerun needed —
  it was never implicated) should remain the honest null comparator: a
  real chromatic effect specific to hard-edged articles, not a global
  instrument artifact that would have shown up in the sponge too.

## Idealizations

Same 2D TMz, linear-media idiom as exp-024; this check isolates
resolution/dispersion sensitivity only — it does not re-examine the
separate ±40°-specific floor anomaly (a different, already-triaged-by-EM
open question, not this script's job) and does not touch angle count,
object composition, or perceptual scoring. Absorber core radius scales
with the same per-λ ratio as the shell (30 cells at exp-024's resolution →
proportionally larger at finer resolution) to hold the physical core size
fixed, per `materials.graded_black_shell`'s own scaling convention
(exp-004's precedent).

## Results

*(Appended after the run — everything above was committed first.)*
