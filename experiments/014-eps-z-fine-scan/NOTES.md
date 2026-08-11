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

*(to be filled in after the run)*

## Next

*(to be filled in after the run)*
