# exp-007 — Chasing the Shell-Ratio Design Lead

**2026-08-10 · driver: Clyde (cloud shift 3) · status: predictions committed, not yet run**

exp-006 isolated `eps_z = (r2/(r2−r1))²` independently of overall cloak
scale (fixed r2, swept r1) and found a clean, monotonic law — Q_ext falls
as the shell thickens (eps_z drops) — holding at both floor values tested,
no exceptions across 8 points. The smallest-eps_z point in that sweep
(core=15, eps_z=1.44, floor=0.10) gave Q_ext=0.0934: **the best (lowest)
reduced-cloak reading in the lab's history, ~7× better than the
exp-002–005 baseline geometry** at the same λ and floor. That result
wasn't a targeted search — it was the edge of a 4-point sweep built to
test a different question (whether eps_z tracks the floor-jump). This
experiment is the deliberate follow-up exp-006 logged as candidate A:
**does Q_ext keep falling as the shell thickens further (core below 15),
or was core=15 close to a floor of its own?**

## Method

Single λ=600nm, single floor=0.10 (the point that produced the design
lead — cpl=20, same domain as exp-002 through 006), r2=90 cells fixed as
throughout this line. **Core (r1) sweep: 8, 10, 12, 20, 25 cells** —
chosen to fill in the gap below and around exp-006's core=15/30 pair
(already-measured, reused directly, not rerun) and trace the curve's
shape: eps_z runs 1.205 (core=8) → 1.266 → 1.331 → [1.440, core=15,
existing] → 1.653 (core=20) → 1.917 (core=25) → [2.250, core=30,
existing], a 7-point curve in total once combined with exp-006's data.

CFL margins (`courant_frac=0.32` against `ceiling=√(floor·eps_z)`) shrink
as the shell thickens (core→0, eps_z→1): core=8 gives the tightest margin
in this sweep at 8.5% — checked by assertion before any run, comparable
to exp-002/003's original 4.5%-margin edge case, not pushed further.

5 cloak runs + 1 empty reference (same domain/box as exp-006, so not
reused across files on principle — this is a separate experiment file,
capturing its own reference is cheap and keeps each experiment
self-contained) = 6 runs total.

## Idealizations

Same 2D TMz, graded-loss-wall, box machinery (stage 8, trust-gated).
Single λ, single floor — this is a targeted trace of one already-observed
lead, not a re-sweep of the floor or λ axes (exp-006 covered the floor
pair at 4 core points; this experiment covers 5 more core points at 1
floor value). The physical PEC core shrinks toward zero radius as r1→0;
this experiment does not go below core=8 (a genuinely vanishing core is a
different, degenerate regime — a PEC point rather than a disk — not
tested here).

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 5 new cloak/core combinations.
- **P2 (the law extends downward):** Q_ext continues to *increase*
  monotonically as core increases across the full combined 7-point curve
  (8, 10, 12, 15, 20, 25, 30) — i.e. exp-006's P5 law (thinner shell,
  worse cloak) holds all the way down to core=8, with core=15 not a local
  minimum reversed by cores below it. A reversal (Q_ext at core=8 or 10
  *higher* than core=15) refutes this and would mean core=15 was a local
  optimum, not just a point on a monotonic curve.
- **P3 (diminishing returns, concave-up near small core):** the
  point-to-point Q_ext *decrease* per unit core-radius shrinks as core
  gets smaller (e.g. `Q_ext(15)−Q_ext(12)` smaller in magnitude than
  `Q_ext(30)−Q_ext(25)`, scaled per cell) — physical reasoning: as r1→0
  the PEC core being hidden vanishes, so Q_ext should approach some
  positive residual (the bare graded shell's own scattering) rather than
  falling toward zero or going negative. A curve that keeps falling at a
  constant or *accelerating* rate as core shrinks refutes this and
  suggests no such floor is nearby yet.

## Results

6 runs (5 cloak + 1 empty), 4.5 min.

**Full combined 7-point curve at λ=600nm, floor=0.10** (this experiment's
5 points + exp-006's core=15/30 reused, not rerun):

| core (r1, cells) | eps_z | Q_ext | box_dev | cross_dev |
|---|---|---|---|---|
| 8 | 1.2046 | **0.0429** | 0.010 | 0.011 |
| 10 | 1.2656 | 0.0520 | 0.002 | 0.009 |
| 12 | 1.3314 | 0.0591 | 0.014 | 0.008 |
| 15 (exp-006) | 1.440 | 0.0934 | 0.000 | 0.001 |
| 20 | 1.6531 | 0.2592 | 0.001 | 0.002 |
| 25 | 1.9172 | 0.4913 | 0.011 | 0.001 |
| 30 (exp-006) | 2.250 | 0.6620 | 0.000 | 0.001 |

box_dev ≤ 1.4% and cross_dev ≤ 1.1% at all 5 new points — both a bit
larger than exp-006's tightest margins but comfortably inside the 2%
gate at every point.

### Predictions scored

- **P1 (gates) — CONFIRMED.** box_dev ≤ 1.4%, cross_dev ≤ 1.1% at all 5
  points.
- **P2 (the law extends downward, no reversal) — CONFIRMED, cleanly.**
  The full 7-point curve is strictly monotonically increasing: 0.0429 →
  0.0520 → 0.0591 → 0.0934 → 0.2592 → 0.4913 → 0.6620. Core=15 was **not**
  a local minimum — Q_ext keeps falling all the way to core=8, the
  smallest tested. **New best: core=8/floor=0.10, Q_ext=0.0429** —
  ~15× better than the exp-002–005 baseline geometry (0.6620) at the
  same λ and floor, and better than exp-006's own design lead (core=15,
  0.0934) by more than half.
- **P3 (diminishing returns near small core) — CONFIRMED.** Per-cell
  slope `ΔQ_ext/Δcore`: 0.0341 (25→30), 0.0464 (20→25), 0.0332 (15→20),
  then dropping sharply to 0.0114 (12→15), 0.00355 (10→12), 0.00455
  (8→10) — the specific comparison predicted (`Q(15)−Q(12)` vs
  `Q(30)−Q(25)`, per cell: 0.0114 vs 0.0341) holds, and the whole
  low-core region (8–15) sits 3–10× shallower than the high-core region
  (20–30). Consistent with Q_ext approaching some positive residual
  rather than continuing to fall at a constant or accelerating rate.

### An honest caveat this experiment did not control for

This curve conflates two effects that this design hasn't separated: (a)
a **physically smaller hidden PEC core intrinsically scatters less**,
independent of any cloak; (b) the reduced-cloak's transformation-optics
grading may **genuinely work better** with a thicker shell relative to
r2. `q_ext` is normalized by the fixed outer radius `2·r2` throughout
(not by `r1`), so this isn't a normalization artifact — every point here
describes the same fixed-footprint (r2=90) device. But it does NOT by
itself show how much of the win is "the cloak is doing more work" versus
"there's simply less object left to hide." That comparison needs a bare
(uncloaked) PEC disk of the same small radius as a control — not run
this shift, logged below.

## Next

- **exp-008 candidate (the control this experiment is missing):** bare
  PEC disk, no cloak shell at all, at radius=8 (and maybe 15, 30 for the
  same three points already characterized with a cloak) — measure Q_ext
  of the *uncloaked* object at each radius, same λ/box/gates. If the bare
  disk's Q_ext already falls steeply with radius on its own, most of this
  experiment's "design lead" is the trivial "smaller object scatters
  less" effect, not real cloak improvement, and the honest headline
  changes. If the bare disk's Q_ext is comparatively flat or high across
  the same radius range while the cloaked numbers still fall steeply,
  that's real evidence the thicker shell is doing more of the
  transformation-optics work. Cheap (3–7 runs), directly resolves the
  caveat above, and is the correct next step before treating core=8 as an
  actual "better cloak design."
- If exp-008 confirms a real effect: worth testing whether the advantage
  generalizes across λ (exp-002/003's multi-wavelength story) — a
  thin-core cloak design that's genuinely better across the spectrum
  would be real news for the broadband-wall line.
- CFL margin shrinks as core shrinks further (core=8's margin was 8.5% at
  floor=0.10); pushing below core=8 needs the margin checked explicitly,
  same discipline as this and prior experiments.
