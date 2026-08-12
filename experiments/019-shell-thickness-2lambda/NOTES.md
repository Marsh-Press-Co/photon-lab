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

13 runs (12 cloak + 1 empty), 15.6 min.

| r1 | shell (λ) | eps_z | Q_ext(0.10) | Q_ext(0.18) | jump | box_dev (0.10 / 0.18) |
|---|---|---|---|---|---|---|
| 47 | 2.15 | 4.3807 | 1.2160 | 1.7762 | **+46.07%** | 0.34% / **2.17%** |
| 48 | 2.10 | 4.5918 | 1.2096 | 1.6751 | **+38.49%** | 0.33% / 1.72% |
| 49 | 2.05 | 4.8186 | 1.2265 | 1.6424 | **+33.92%** | 0.74% / 0.24% |
| 50 (2.00λ target) | 2.00 | 5.0625 | 1.1424 | 1.6249 | **+42.24%** | 0.40% / 0.36% |
| 51 | 1.95 | 5.3254 | 1.2219 | 1.7081 | **+39.79%** | 0.84% / 0.55% |
| 52 | 1.90 | 5.6094 | 1.1700 | — (excluded) | — | 0.49% / — |
| 53 | 1.85 | 5.9167 | 1.3404 | — (excluded) | — | 1.50% / — |

cross_dev ≤0.04% throughout — clean everywhere.

### Predictions scored

- **P1 (gates ≤2%) — CONFIRMED at 11 of 12 points, one honest exception:**
  r1=47/floor=0.18 comes in at box_dev=2.17%, just over the 2% band
  (the next-largest, r1=48/floor=0.18, is 1.72%, comfortably inside).
  Not discarding or re-running to make it disappear — flagged here as a
  gate miss. It does not touch this experiment's discriminating
  question: r1=47 sits at the far edge of the bracket, not r1=50 (the
  target point, box_dev 0.40%/0.36%, among the cleanest in the set), and
  the qualitative result (a large positive jump) is not the kind of
  conclusion a 2.17%-vs-2% box-independence wobble could flip.
- **P2 (reproduction) — CONFIRMED, exactly.** r1=48 gives
  Q_ext(0.10)=1.2096, Q_ext(0.18)=1.6751 — matching exp-006/013's
  1.20959/1.67510 to 4 decimal places (rounding only).
- **P3 (the discriminator) — CONFIRMED as the 3λ-specific outcome.**
  All 5 points with both floors (r1=47–51) show **positive** jumps
  (+33.9% to +46.1%) — none negative, no band, no hint of a dip near
  r1=50. The negative-jump feature exp-014 mapped at 3λ (shell=60
  cells) does **not** reappear at 2λ (shell=40 cells). Whatever produces
  the 3λ feature is not a generic "shell = integer × λ" resonance rule
  — at minimum, 2λ and 3λ behave differently, so "any integer" is ruled
  out as the mechanism.
- **P4 (secondary, monotonic law) — roughly holds, not exactly.**
  Q_ext(0.10) across r1=47→53 (eps_z 4.38→5.92): 1.2160, 1.2096, 1.2265,
  1.1424, 1.2219, 1.1700, 1.3404 — not strictly monotonic (a dip at
  r1=50, a rise at r1=53), but stays in a narrow 1.14–1.34 band, far
  tamer than exp-014's own fine-scan swings near the 3λ point. Read
  together with P3, this band looks like ordinary point-to-point wobble
  around a roughly flat trend, not another hidden trough — consistent
  with 2λ being an unremarkable point on the Q_ext(eps_z) surface.

### Headline

**The shell-thickness standing-wave hypothesis from exp-018 does not
generalize to 2λ.** The magnitude of the positive jumps here (+34% to
+46%) sits right in the middle of the range exp-018 found at its own
non-3λ points (+3% to +92%) — 2λ looks exactly like an ordinary point on
that curve, not a second resonance. This narrows, rather than confirms,
exp-018's hypothesis: **3λ specifically produces the negative-jump
feature; 2λ does not.** Two readings remain open: (a) only odd integers
(or specifically 3, not integers generally) set up whatever standing-wave
condition matters, or (b) the "integer λ" framing itself was a
coincidence of this one data point and the real mechanism is still
unidentified — exp-018's own single sampled integer (3λ) is not enough
evidence to have concluded a general rule from, and this experiment is
the honest correction to that overreach before it went further.

## Next

- **[open]** The integer-λ hypothesis is now narrowed to "maybe just
  3λ," which is much less interesting mechanistically than "any
  integer" would have been — closer to exp-018's original "one
  coincidental geometry" framing than a discovered law. Before chasing
  parity (odd vs even) with a 3rd or 4th data point (1λ, 4λ — both would
  need very different core/shell geometry, 1λ pushing r1 to 70 cells,
  deep into an eps_z regime not characterized at all yet), it's worth
  asking whether the 3λ feature is reproducible at a genuinely different
  r2 (fixed outer radius has been 90 cells for the entire eps_z/shell
  line since exp-006 — every point tested so far, including this
  experiment's, shares that one r2). A trough at shell=3λ that only
  shows up at r2=90 specifically (not at, say, r2=60 or r2=120 with
  their own shell=3λ points) would point at something about r2 itself,
  not shell thickness in isolation — an un-isolated variable this whole
  line has never varied.
- **[open, lower priority]** If a future shift does chase the parity
  question, 1λ (r1=70, eps_z=(90/20)²=20.25) and 4λ (r1=10, eps_z=
  (90/80)²=1.2656) bracket this experiment and exp-018's 3λ point
  reasonably evenly — but both need fresh CFL/degeneracy gate checks
  before committing (1λ's shell=20 cells is thin enough it may hit the
  same degeneracy wall this experiment saw at its own thin-shell edge;
  4λ's eps_z=1.27 is close to exp-011's core=15/eps_z=1.44 point, which
  is already known monotonic).
- The `mu_r_floor < 0.05` direction and the parking lot remain open,
  unchanged.
