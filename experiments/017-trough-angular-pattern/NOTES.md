# exp-017 — Mechanism candidate 2: angular-pattern comparison, trough vs flanks

## Hypothesis

exp-016 refuted outer-boundary impedance mismatch as the eps_z trough's
mechanism, on both magnitude (smooth `|Gamma(eps_z)|²`, no local
extremum) and structural (exactly floor-independent where the trough
lives, so it can't produce the floor-dependent sign flip that defines
the trough) grounds. exp-015's Next section queued a second, independent
candidate: does the trough (r1=30, eps_z=2.25) scatter into a
qualitatively **different angular shape** than its flanks (r1=27, r1=33)
— a new lobe, a shifted peak — or is it the same shape at a different
**magnitude**?

## Setup

New instrumentation, added this shift: `lab.sections.angular_scattered_
pattern` (`lab/sections.py`). It reuses the exact same per-cell
scattered-outflow terms `widths()` already sums to one `sigma_scat`
number, but keeps them per-cell, tags each perimeter cell with its angle
from the box center, and bins into `n_bins` angular sectors. Convention:
0° = toward the source (backward), ±180° = downstream (forward) — same
sign convention as the existing `back_frac`/`fwd_frac` split, just
angle-resolved instead of two-way.

Stage 8 (the existing cross-section trust gates) reruns clean after this
addition (6/6, unchanged from before this shift's edit — the new
function is purely additive, no existing code path touched):

    .venv/bin/python lab/validation/run_all.py --only 8

Same domain and geometry as exp-014/015/016's r1=27/30/33 bracket points
(N=680, CX=CY=300, cpl=20, R2_CELLS=90, λ=600nm), `mu_r_floor=0.10` only
(one of the trough's own defining pair — keeps this file to 4 runs: 3
cloak + 1 shared empty reference). `BOX_A_HALF=110` is the box the
angular pattern is drawn from; `BOX_B_HALF=135` is kept purely for the
usual box-independence gate on `sigma_ext`, not used for the pattern
itself.

`N_BINS=48` (7.5° bins) — fine enough to distinguish a genuine extra
lobe from noise, coarse enough that each bin still averages several
perimeter cells.

## Idealizations

The angular pattern is sampled on a **square path** (the box perimeter),
not a true circle — the same near-to-mid-field-box idealization
`sigma_scat` itself already rests on (documented in `sections.py`'s
module docstring and `VALIDATION.md`), not a new approximation
introduced here. `sum(sigma_scat_per_bin) == widths().sigma_scat` is an
**implementation identity** (the binning is an exact re-partition of the
same numbers, not an independent physical measurement) — checked per run
before any pattern is trusted for shape comparisons, to catch
implementation bugs (angle-tagging errors, sign mistakes, double-counted
corner cells) rather than to validate physics.

Shape is compared via Pearson correlation of each pattern normalized to
its own total (removing the magnitude difference exp-006/014 already
established, isolating shape alone).

## Predictions — committed before the run

- **P1 (gates + self-consistency):** the usual box_dev/cross_dev gates
  stay ≤2% at all 3 core points (matching exp-014/015's own numbers at
  this geometry), and `angular_scattered_pattern`'s binned sum matches
  `widths()`'s own `sigma_scat` to <0.1% relative at every point — an
  implementation-correctness check, not itself the mechanism question.
- **P2 (reproduction):** core=30/floor=0.10's `Q_ext` from this file's
  own `widths()` call reproduces exp-014's reused number (0.6620) to
  <1% — same geometry, same code path, exp-006's own precedent for this
  kind of cross-file reproduction (there, bit-identical).
- **P3 (the discriminator):** compare `corr(flank27, trough30)` and
  `corr(flank33, trough30)` against `corr(flank27, flank33)` (all on
  shape-normalized patterns). Two falsifiable outcomes, both
  informative:
  - **Shape-change outcome:** either trough correlation sits **≥0.05
    lower** than the flank-flank correlation — the trough's pattern is
    measurably less "the same family" as its neighbors than they are to
    each other, consistent with a new lobe or resonance-like mode
    appearing inside the trough.
  - **Magnitude-only outcome:** both trough correlations sit **within
    0.05** of the flank-flank correlation — the trough interpolates
    smoothly in shape between its flanks, meaning exp-014/015's trough is
    a pure magnitude effect (same scattering pattern, less/more of it),
    and this candidate is refuted the same way exp-016's was — cleanly,
    just via a different probe.
  No directional prediction is made on *which* outcome — this is a
  genuine open question, not a foregone conclusion dressed as a
  prediction.
