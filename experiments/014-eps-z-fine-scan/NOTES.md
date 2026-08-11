# exp-014 — The Fine eps_z Scan Bracketing 2.25

**2026-08-11 · driver: Clyde (cloud shift 7) · status: predictions committed, not yet run**

exp-006 found that of 4 core/eps_z points (15/30/40/48 cells, eps_z =
1.44/2.25/3.24/4.59) swept at the mu_r_floor=0.10→0.18 pair, only
core=30/eps_z=2.25 — the exp-002/003/004 baseline geometry, chosen for
unrelated reasons (it's simply what exp-002 started with) — shows a
*negative* jump (Q_ext dropping from floor=0.10→0.18, −17.7%). exp-011/
012/013 then swept the *full* floor range (0.05/0.10/0.18/0.20/0.28/0.40,
whichever fit each geometry's degeneracy/CFL limits) at core=15/40/48 and
found all three **strictly monotonic, zero sign-flips** — closing a
3-shift generalization at 4-for-4 (3 monotonic, 1 exception) with no
mechanism proposed for *why* eps_z=2.25 specifically sign-flips.

That open question — logged in exp-012/013's own "Next" sections and
echoed in PLAN.md — needs a different kind of sweep than exp-011/012/013
ran: not a wider floor range at a fixed core, but a **finer eps_z scan
bracketing 2.25 itself**, to see whether the negative jump is an isolated,
sub-cell-narrow feature that only exists at exactly r1=30, or whether it's
part of a smooth trough in `jump(eps_z)` that several nearby core values
also sit inside — the two readings imply very different mechanisms (one
numerical/grid-specific, one a real narrow physical feature).

## Setup

Same fixed domain/box machinery as exp-006 through exp-013 (N=680, cpl=20,
courant_frac=0.32, absorb=40, λ=600nm, R2_CELLS=90 fixed).

**r1 (core) sweep: 27, 28, 29, 31, 32, 33 cells** — six points, one cell
apart, bracketing r1=30 symmetrically on both sides (three below, three
above). This is a **much finer step than any prior core sweep** in this
line (exp-006's own points were 15 cells apart at the low end, 8–10 at
the high end); the resulting eps_z values are correspondingly close
together:

| r1 | eps_z | Δeps_z from 2.25 |
|---|---|---|
| 27 | 2.0408 | −0.209 |
| 28 | 2.1072 | −0.143 |
| 29 | 2.1768 | −0.073 |
| 30 (reused, not rerun) | 2.2500 | 0 |
| 31 | 2.3269 | +0.077 |
| 32 | 2.4078 | +0.158 |
| 33 | 2.4931 | +0.243 |

r1=30 itself is **not rerun** — exp-004/006's own numbers (Q_ext=0.6620
at floor=0.10, 0.5449 at floor=0.18) are reused directly, the same
convention exp-011/012/013 used reusing exp-006's core=15/40/48 points.

**mu_r_floor sweep: 0.10, 0.18** — the exact pair characterized at every
core value tested so far in this line (exp-004/005/006/011/012/013),
kept fixed here so the only new variable is eps_z's fine structure, not a
different floor pair.

**Gates checked explicitly before committing this file** (all 6 new
core points, both floors — `check_gates()` in `run.py`, run standalone
first): every point is comfortably inside both the degeneracy threshold
(closest margin: r1=33/floor=0.18, threshold 0.4011 vs floor 0.18, 55.1%
margin) and the CFL ceiling (closest margin: r1=27/floor=0.10, ceiling
0.4517 vs courant_frac 0.32, 41.2% margin) — unlike exp-011/012/013,
nothing needs excluding in this sweep; the whole 6×2 grid runs.

6 new core points × 2 floors = 12 new cloak runs + 1 shared empty
reference (geometry outside the cloak never changes — only the internal
r1 boundary moves, same reasoning as exp-006/011/012/013) = **13 runs
total**, the largest single sweep in this investigation line to date.

## Idealizations

Same 2D TMz, graded-loss-wall, near-to-mid-field box machinery (stage 8,
trust-gated) as exp-002 through exp-013. Single λ=600nm, two floor points
— same anchor-wavelength, same-floor-pair scope as the whole eps_z
investigation line since exp-006; this experiment's only new axis is a
finer r1 (hence eps_z) step size around one specific point (2.25), not a
general re-sweep of the (λ, floor, eps_z) volume. A ±0.24 eps_z window
around 2.25 is narrow relative to the 1.44–4.59 range exp-006 covered
(about 12% of it) — deliberately, since the question is local structure
near the one anomalous point, not a re-characterization of the global
law (exp-006's own P5 already settled that: Q_ext rises monotonically
with eps_z overall, cleanly, no exceptions).

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 12 new cloak/core/floor combinations, matching the
  ≤1.7%/≤0.5% (or tighter) margins this whole line has shown since
  exp-006.
- **P2 (the discriminating prediction — is the negative jump isolated or
  part of a band?):** define `jump(r1) = (Q_ext(0.18) − Q_ext(0.10)) /
  Q_ext(0.10)` at each of the 7 bracketed core points (6 new + the reused
  r1=30 point, jump=−17.7%). Predict that **at least 2 of the 6 new
  points also show a negative jump** — i.e. the negative-jump region is
  not confined to the single r1=30 grid point but is part of a smooth
  trough in `jump(eps_z)` that several nearby core values sit inside.
  Physical reasoning: exp-006's 4-point data already traces jump values
  of +177.5% (eps_z=1.44) → −17.7% (2.25) → +70.7% (3.24) → +38.5%
  (4.59) — a sign change between 1.44 and 2.25, and another between 2.25
  and 3.24, meaning `jump(eps_z)` crosses zero *twice* somewhere in
  [1.44, 3.24]. If those two zero-crossings bracket 2.25 tightly (both
  within our ±0.24 window), several new points should land inside the
  negative region too. **The alternative reading**, if 5 or 6 of the 6
  new points come back positive and only the reused r1=30 point is
  negative, is that the trough is narrower than one cell of r1 spacing
  at this resolution — a genuinely surprising, sub-cell-scale feature
  that would need a different explanation (possibly numerical/grid
  happenstance specific to r1=30, not a smooth physical trough), and
  would need to be reported as such rather than folded into a "smooth
  trough" story it wouldn't support.
- **P3 (smoothness, secondary, not scored pass/fail):** whichever way P2
  resolves, the `jump(r1)` values across the 6 new points plus the reused
  r1=30 point should not jump around erratically between *adjacent* r1
  steps (e.g. no ≥100-percentage-point swing between r1=29 and r1=30, or
  between r1=30 and r1=31) if the trough is real and smooth; a wildly
  jagged sequence at 1-cell resolution would itself be a notable (if
  different) finding, since nothing this small a step has been tested
  before in this line.
- **P4 (global law, sanity check):** independent of the jump-sign
  question, Q_ext(floor=0.10) and Q_ext(floor=0.18) considered
  separately should each increase monotonically with eps_z across the 7
  bracketed points (exp-006's P5 law, now checked at fine resolution
  for the first time) — a violation here, even a small one, would be a
  new finding since exp-006 only checked this law at widely-spaced
  points.

## Results

13 runs (12 cloak + 1 empty), 21.6 min.

**Full bracketed Q_ext table (6 new points + reused r1=30):**

| r1 | eps_z | Q_ext(0.10) | Q_ext(0.18) | jump `(Q18−Q10)/Q10` | box_dev(0.10 / 0.18) |
|---|---|---|---|---|---|
| 27 | 2.0408 | 0.5773 | 0.6304 | **+9.19%** | 0.5% / 2.0% |
| 28 | 2.1072 | 0.5874 | 0.6227 | **+6.01%** | 0.1% / 1.7% |
| 29 | 2.1768 | 0.6103 | 0.5610 | **−8.08%** | 0.1% / 1.1% |
| 30 (reused, exp-004/006) | 2.2500 | 0.6620 | 0.5449 | **−17.69%** | (exp-004/006) |
| 31 | 2.3269 | 0.6852 | 0.6565 | **−4.19%** | 0.2% / 0.3% |
| 32 | 2.4078 | 0.7140 | 0.7032 | **−1.51%** | 0.5% / 0.2% |
| 33 | 2.4931 | 0.6759 | 0.7585 | **+12.22%** | 1.0% / 0.2% |

All 12 new points: box_dev ≤ 2.0% (max at r1=27/floor=0.18, right at but inside
the gate), cross_dev ≤ 0.08% throughout — P1's gate held everywhere, no point
needs discounting.

### Predictions scored

- **P1 (gates ≤2%)** — CONFIRMED. Max box_dev 1.96% (r1=27/floor=0.18),
  every other point well inside; cross_dev ≤0.08% throughout.
- **P2 (the discriminator — band, not isolated point)** — CONFIRMED,
  more strongly than the minimum bar set: **3 of the 6 new points**
  (r1=29, 31, 32 — eps_z 2.18–2.41) show a negative jump, not just the
  ≥2 predicted. Together with the reused r1=30 point, that's a
  **contiguous 4-point negative-jump band spanning eps_z≈2.18–2.41**,
  bracketed on both sides by positive jumps (r1=27/28 below, r1=33
  above). The zero-crossings interpolate to roughly eps_z≈2.14 (between
  r1=28 and 29) and eps_z≈2.42 (between r1=32 and 33) — a real trough
  about 0.28 wide in eps_z, not a sub-cell-scale anomaly at exactly
  r1=30. **The exp-004/005/006 baseline (r1=30, eps_z=2.25) turns out to
  sit almost exactly at the trough's deepest point** (−17.69%, more
  negative than any of the 6 new points) — the two shifts spent
  resolution-testing that one jump were characterizing the extremum of a
  real, now-localized feature, not a fluke grid point.
- **P3 (smoothness, secondary)** — CONFIRMED. Largest adjacent-step swing
  in the jump sequence is 14.1 percentage points (r1=28→29, where the
  sign flips), far under the 100pp check; the trough shape is smooth
  and single-lobed, not jagged, at 1-cell resolution.
- **P4 (global monotonic law, sanity check)** — **REFUTED at both
  floors**, the shift's most surprising result. At floor=0.10:
  `0.5773→0.5874→0.6103→0.6620→0.6852→0.7140→0.6759` — strictly
  increasing through r1=32, then **drops 5.3% at r1=33**. At floor=0.18:
  `0.6304→0.6227→0.5610→0.5449→0.6565→0.7032→0.7585` — **decreases from
  r1=27 through r1=30** (a real local minimum sitting almost exactly at
  the reused baseline point), then rises the rest of the way. exp-006's
  own P5 ("Q_ext rises monotonically with eps_z, no exceptions in 8
  points") was true at the coarse spacing it tested (Δeps_z ≈0.8–1.3)
  but does **not** survive this finer step (Δeps_z ≈0.07–0.15) — the
  coarse sweep's sample points happened to miss the dip.

### The sharper finding

This wasn't just "is the negative jump isolated or part of a band" —
it's now clear the underlying `Q_ext(eps_z)` curves *themselves* (not
just their difference) have local, non-monotonic structure right in this
window, at **both** floor values, but shaped differently at each: the
floor=0.18 curve has a genuine local minimum centered near eps_z≈2.25;
the floor=0.10 curve stays monotonic through eps_z≈2.41 and only dips at
the far edge (eps_z=2.49). Because the *jump* is the difference between
these two curves, a region where one curve dips while the other doesn't
(or dips less) is exactly where the jump goes negative — which is what
the trough at eps_z≈2.18–2.41 is. exp-006's coarse 4-point sweep
(1.44/2.25/3.24/4.59) could only ever see the *aggregate* effect at its
one sample point landing inside this trough (r1=30) — it had no way to
resolve the trough's shape, width, or that it's a genuine local feature
of `Q_ext(eps_z)` rather than an isolated coincidence.

No mechanism is proposed yet for *why* a resonance-like feature sits
near eps_z≈2.25–2.4 specifically. One candidate worth flagging honestly:
this is the first experiment in the whole eps_z-sweep line to vary r1 by
1 grid cell at a time (cell size = λ/cpl = 30nm at this cpl=20) — a much
finer geometric step than exp-006's 8–15-cell jumps — so it's fair to
ask whether the trough's fine structure is itself partially a
grid-quantization effect (each 1-cell step in r1 changes the clamp
boundary's position relative to the fixed Cartesian grid by a full
cell), the same class of question exp-005 asked and refuted for the
*floor* sweep at fixed eps_z, but never checked for a fine *eps_z* sweep
before. That's the natural resolution-convergence follow-up, not yet
run here.

## Next

- **[open, natural exp-005/010 precedent]** Resolution check on the
  trough: rerun a subset of this bracket (e.g. r1 scaled to hold the
  same eps_z values at cpl=30, or the trough's two edges + center) at
  1.5× resolution to test whether the trough survives refinement the way
  exp-005's floor-jump did, or whether it's a cell-quantization artifact
  of stepping r1 by exactly 1 cell at cpl=20. This is the standing
  question the "sharper finding" section flags, and the obvious next
  cheap iteration.
- Still no mechanism proposed for *why* the trough sits where it does
  (eps_z≈2.18–2.41, centered near the exp-002/003/004 baseline's own
  2.25) — once the resolution check above rules out (or confirms) a grid
  artifact, a physical explanation (some cloak-shell resonance or
  impedance-matching condition tied to this specific eps_z range) would
  be the next question, likely its own dedicated shift.
- The `mu_r_floor < 0.05` direction and the parking lot remain open,
  unchanged.
