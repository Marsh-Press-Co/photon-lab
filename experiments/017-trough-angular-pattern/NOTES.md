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

## Results

4 runs (3 cloak + 1 empty), 5.1 min.

| r1 | eps_z | Q_ext | box_dev | cross_dev | self_consistency_dev | back_frac | fwd_frac |
|---|---|---|---|---|---|---|---|
| 27 (flank) | 2.0408 | 0.5773 | 0.46% | 0.08% | 0.00e+00 | 0.1526 | 0.6117 |
| 30 (trough) | 2.2500 | 0.6620 | 0.01% | 0.07% | 1.21e-16 | 0.1761 | 0.6270 |
| 33 (flank) | 2.4931 | 0.6759 | 1.01% | 0.07% | 1.19e-16 | 0.1802 | 0.5856 |

Shape correlations (Pearson, patterns normalized to their own total
before comparing):

| pair | correlation |
|---|---|
| flank27 vs trough30 | 0.9688 |
| flank33 vs trough30 | 0.9717 |
| flank27 vs flank33 | 0.9383 |

### Predictions scored

- **P1 (gates + self-consistency) — CONFIRMED, comfortably.** All
  box_dev ≤1.01%, all cross_dev ≤0.08% — well inside the 2% band and
  matching exp-014/015's own tightness at this geometry. The self-
  consistency identity landed at machine epsilon (0/1.2e-16), not just
  under the 0.1% bar — as expected for an exact re-partition of the same
  numbers, and a clean confirmation the new binning code has no sign or
  double-counting bug.
- **P2 (reproduction) — CONFIRMED, exactly.** core=30/floor=0.10 gives
  Q_ext=0.6620, bit-identical to exp-014/015's own reused number — same
  geometry, same code path, same precedent exp-006's P2 set.
- **P3 (the discriminator) — CONFIRMED as the magnitude-only outcome,
  with an honest asymmetry worth flagging.** Both trough correlations
  (0.9688, 0.9717) land within the predicted 0.05 band of the flank-
  flank correlation (0.9383) — satisfying the literal magnitude-only
  criterion. But the direction is notable: the trough correlates **more**
  strongly with *each* flank than the flanks correlate with *each
  other*, not less. This has a mundane explanation that doesn't require
  a new mechanism: r1=30 sits exactly 3 cells from each flank in this
  bracket, while the two flanks sit 6 cells apart from each other — if
  scattering shape varies smoothly and continuously with eps_z (no
  anomaly), nearer points should correlate better than farther ones,
  which is exactly the ordering observed. The asymmetry is consistent
  with smooth continuous shape variation, not evidence of anything
  discontinuous at the trough.

  A secondary, non-predicted observation, reported for honesty rather
  than folded into the scored claim: a simple local-maxima count
  (bins exceeding 5% of that pattern's peak) found 13 peaks at the
  trough vs 10 at each flank — the trough's pattern has a couple of
  extra small side-lobes the flanks don't show as distinctly. This is
  the kind of thing worth another look (finer angular bins, or comparing
  against a smoother reference like an uncloaked bare disk at the same
  radii) before treating it as a real feature rather than binning noise
  right at a shoulder — flagged as an open thread, not claimed as a
  finding.

### Headline

**The angular-pattern probe also points toward magnitude-only — the
trough is not a new scattering mode.** Shape correlation places the
trough cleanly inside the same family as both flanks, and the one
notable asymmetry (trough correlating *better* with each flank than
they correlate with each other) is fully explained by ordinary distance
in eps_z-space, not by anything anomalous. Combined with exp-016's
independent refutation of outer-boundary impedance mismatch, **both
mechanism candidates queued after exp-014/015 are now closed, and
neither found the mechanism.** Two independent instruments — the
shell's static boundary properties (exp-016) and the propagating field's
angular distribution (exp-017) — agree the trough is real (exp-014/015),
grid-independent (exp-015), and a magnitude-only effect (exp-017), but
*why* `Q_ext(eps_z)` specifically dips near eps_z≈2.25–2.4 remains
unexplained by either candidate tested so far.

## Next

- **[open]** Both queued mechanism candidates are closed without
  success. The trough's actual cause is still unknown. A genuinely new
  candidate worth considering: a frequency-domain view (does `eps_z`
  tune something resonance-like relative to the fixed λ=600nm/cpl=20
  grid — e.g. an internal standing-wave condition in the shell's radial
  extent — that a single-λ time-domain run can't distinguish from a
  smooth trend without sweeping λ *at fixed eps_z* across the trough
  point, the mirror experiment to exp-003's λ sweep but held at
  core=30). That's a real new investigation, not a quick bolt-on —
  worth a dedicated future shift rather than squeezing it into this
  one's remaining time.
- The 13-vs-10 peak-count observation (secondary, unscored) is a loose
  thread: worth revisiting with finer angular bins or a bare-disk
  reference if a future shift returns to this mechanism question.
- `lab.sections.angular_scattered_pattern` is now available for any
  future experiment wanting angle-resolved scattering (not just this
  mechanism line) — e.g. the parking lot's "black-lined cloak hybrid"
  or "near-to-far transform" items could reuse it directly.
