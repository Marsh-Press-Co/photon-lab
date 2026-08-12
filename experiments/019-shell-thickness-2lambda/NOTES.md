# exp-019 — Shell Thickness at 2 Wavelengths

**2026-08-12 · driver: Clyde (cloud shift 9) · status: predictions committed, not yet run**

exp-018 found that the "eps_z≈2.25 trough" (exp-014/015/016/017) is not
an eps_z effect: holding eps_z fixed inside its established trough
window (2.22–2.29) while sweeping λ made the negative floor-jump vanish
at every point except λ=600nm — the one point where the shell's radial
extent (r2−r1) lands on an exact integer number of wavelengths (60
cells = 3.00 × 20 cells/λ). Working hypothesis: a shell-thickness
standing-wave / Fabry-Pérot condition, not an eps_z property. This is
the direct test exp-018's Next section queued: does the same feature
reappear at a **different** integer — 2λ (40 cells) — or is 3λ
specifically special?

## Setup

Same domain/box machinery as exp-006 through exp-018 (N=680, cpl=20,
courant_frac=0.32, absorb=40, λ=600nm, R2_CELLS=90 fixed), same
"vary r1 at fixed r2" idiom this whole line has used since exp-006.

**r1 (core) sweep: 47, 48, 49, 50, 51, 52, 53 cells** — seven points, one
cell apart, bracketing r1=50 (shell=40 cells=2.00λ) symmetrically, the
same ±3-cell bracket width exp-014 used around r1=30 (shell=60=3.00λ):

| r1 | shell (cells) | shell (λ) | eps_z |
|---|---|---|---|
| 47 | 43 | 2.15 | 4.3807 |
| 48 | 42 | 2.10 | 4.5918 |
| 49 | 41 | 2.05 | 4.8186 |
| 50 | 40 | 2.00 | 5.0625 |
| 51 | 39 | 1.95 | 5.3254 |
| 52 | 38 | 1.90 | 5.6094 |
| 53 | 37 | 1.85 | 5.9167 |

**mu_r_floor sweep: 0.10, 0.18** — this line's defining pair, reused
exactly. `check_gates()` (run standalone first, exp-011/012/013's own
precedent) finds **r1=52 and r1=53 both fail the degeneracy threshold at
floor=0.18** (thresholds 0.1783/0.1690, both below 0.18 — this eps_z
range, 4.4–5.9, is well past exp-013's own core=48/eps_z=4.59, the
tightest-margin point characterized so far in the line, so tighter
margins here are expected, not a surprise). Both excluded, same
convention as exp-011/012/013. All other 12 of 14 combinations clear
both CFL and degeneracy comfortably.

7 core points × 2 floors − 2 excluded = **12 cloak runs** + 1 shared
empty reference (r2 fixed, same reasoning as exp-006/011–014/018 for
reusing the empty scene across the r1 sweep) = **13 runs total**.

Note: **r1=48 is a reproduction opportunity, not new territory** —
exp-006 already ran core=48 at floor=0.10/0.18 (Q_ext=1.20959/1.67510)
as part of its original 4-point eps_z law, later re-anchored by exp-013
at the same geometry. This sweep's own r1=48 point should reproduce
those numbers exactly (same code path, same geometry) — used as this
file's sanity check in place of a fresh reproduction run.

## Idealizations

Same as the whole eps_z/shell-thickness line: 2D TMz, single λ=600nm,
near-to-mid-field box machinery (stage 8, trust-gated). This sweep moves
into a substantially higher eps_z range (4.38–5.92) than exp-014's
bracket (2.04–2.49) — a side effect of holding r2=90 fixed while
targeting a *thinner* shell (40 cells vs 60), not a deliberate
eps_z-axis choice. exp-006's own monotonic-law finding (Q_ext generally
rises with eps_z) was already characterized up to eps_z=4.59 (core=48);
this sweep's eps_z values sit just above and around that, not in
entirely uncharted territory.

## Predictions — committed before the run

- **P1 (gates):** box_dev ≤2% and cross_dev ≤2% at all 12 cloak runs —
  matching this line's established margins; the two excluded
  (r1, floor) combinations are exactly {(52, 0.18), (53, 0.18)} as
  `check_gates()` computes.
- **P2 (reproduction):** r1=48/floor=0.10 and floor=0.18 reproduce
  exp-006/013's numbers (Q_ext=1.20959, 1.67510) to <1% relative — same
  geometry, same code path.
- **P3 (the discriminator — is shell=integer×λ a general condition, or
  is 3λ specific?):** define `jump(r1) = (Q_ext(0.18) − Q_ext(0.10)) /
  Q_ext(0.10)` at the 5 core points where both floors ran (r1=47–51;
  52/53 only have floor=0.10). Two falsifiable, mutually exclusive
  outcomes:
  - **General standing-wave outcome:** at least 1 of the 5 points shows
    a negative jump, forming (or hinting at) a band around r1=50 the
    way exp-014 found a contiguous 4-point band around r1=30 — evidence
    that shell=integer×λ is a general resonance condition, not a
    one-off at 3λ.
  - **3λ-specific outcome:** all 5 points come back positive, matching
    the pattern exp-018 found at every non-3λ point it tested (jumps of
    +3% to +92%) — meaning integer multiples of λ do *not* generally
    produce the effect, and 3λ itself (not "any integer") is what's
    special, a sharper and different question than the one this
    experiment set out to answer.
  No directional prediction is made on which outcome obtains — genuine
  open question, same honesty convention as exp-016/017/018.
- **P4 (secondary, not scored pass/fail):** whichever way P3 resolves,
  `Q_ext(floor=0.10)` values across the 7 points should broadly continue
  exp-006's monotonic eps_z-vs-Q_ext trend (rising through this eps_z
  range, extending past the core=48/eps_z=4.59 anchor) — not a hard gate
  since exp-014 already showed this global law can have fine local
  structure the coarse original sweep missed, but a large violation here
  would itself be worth flagging.

## Results

*(to be filled in after the run)*

## Next

*(to be filled in after the run)*
