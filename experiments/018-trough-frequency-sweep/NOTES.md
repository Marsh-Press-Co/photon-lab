# exp-018 — The Trough Frequency Sweep

**2026-08-12 · driver: Clyde (cloud shift 9) · status: predictions committed, not yet run**

exp-016 (outer-boundary impedance mismatch) and exp-017 (angular-pattern
shape) were both queued mechanism candidates for the eps_z≈2.25–2.4
trough (exp-014, confirmed grid-independent by exp-015) and both were
refuted this shift's predecessor. exp-017's Next section proposed a
genuinely new candidate, not yet tested by anything in this line: is the
trough tied to a **resonance-like condition at the fixed λ=600nm/cpl=20
grid** — e.g. an internal standing-wave condition set by the shell's
radial extent measured in wavelengths — rather than being a pure
function of eps_z (the r1/r2 ratio) alone?

## Setup

The mirror experiment to exp-003's λ sweep, exactly as exp-017 proposed:
exp-003's own frequency-scaling machinery (cells-per-λ held FIXED at 20,
geometry scaled in cells so physical size in nm stays fixed as λ varies,
same `f(λ) = 600nm/λ` convention, same 6-point sweep 420/480/540/600/
660/750nm, same domain fix — N=680, CX=CY=300, STEPS=3600 — that
resolved exp-003's own box-independence bug), but anchored at the
**trough's own geometry** (r1=30, r2=90 cells at f=1, i.e. eps_z=2.25
exactly at λ=600nm — exp-002/003/004's original baseline and exp-014/
015's trough center) instead of exp-002's original core/coat/clk triple.
Only the cloak scene is built (no reflector/absorber — this is a
single-scene mechanism probe, not a repeat of exp-003's own broadband
question), at the trough's own defining `mu_r_floor` pair (0.10, 0.18).

Because r1 and r2 scale by the same factor `f(λ)`, their ratio — and
therefore `eps_z = (r2/(r2-r1))²` — stays close to 2.25 at every λ after
integer-cell rounding:

| λ (nm) | r1 (cells) | r2 (cells) | shell (cells) | shell (λ) | eps_z |
|---|---|---|---|---|---|
| 420 | 43 | 129 | 86 | 4.30 | 2.2500 |
| 480 | 38 | 112 | 74 | 3.70 | 2.2907 |
| 540 | 33 | 100 | 67 | 3.35 | 2.2277 |
| 600 | 30 | 90 | 60 | 3.00 | 2.2500 |
| 660 | 27 | 82 | 55 | 2.75 | 2.2228 |
| 750 | 24 | 72 | 48 | 2.40 | 2.2500 |

All 6 eps_z values (2.2228–2.2907) sit comfortably inside exp-014's
characterized trough window (~2.18–2.41) — this sweep never leaves the
trough on the eps_z axis. But the shell's radial extent **measured in
wavelengths** (which is what an internal standing-wave condition would
actually depend on) varies substantially across the same sweep: 2.40λ
at 750nm up to 4.30λ at 420nm, a 79% range, with λ=600nm sitting almost
exactly at 3.00λ. This is the discriminator: eps_z is (deliberately) held
almost constant while electrical size / shell-radial-extent-in-λ is
swept — the opposite of exp-014's own design, which held λ fixed and
swept eps_z. If the trough survives here, it's an eps_z effect, not a
λ/grid effect; if it doesn't, the reverse.

`check_gates()` (run standalone first, matching exp-011/012/013/014's
own precedent) confirms every point clears both the degeneracy threshold
(closest margin: λ=480nm/floor=0.18, threshold 0.4365 vs floor 0.18,
58.8% margin) and the CFL ceiling (closest margin: λ=660nm/floor=0.10,
ceiling 0.4715 vs courant_frac 0.32, 32.1% margin) — nothing needs
excluding, the full 6×2 grid runs.

6 λ points × 2 floors = 12 cloak runs + 6 empty references (one per λ,
box geometry scales with λ so the empty reference isn't reusable across
λ points — same reasoning as exp-003) = **18 runs total**.

## Idealizations

Same 2D TMz, single-core cloak-only scene, near-to-mid-field box
machinery (stage 8, trust-gated) as the whole eps_z investigation line.
Reusing exp-003's exact geometry-scaling convention means this sweep
inherits its idealization too: "λ" here means a fixed physical defect
size viewed at different colors with resolution (cpl) held constant, not
a literal single-frequency-source sweep at fixed geometry — the FDTD
engine has no independent frequency knob at fixed cell geometry (cpl
alone sets "cells per wavelength"; nm is bookkeeping laid on top for
real-unit reporting and this scaling). Because the source is a single
narrowband pulse at each run's own λ, all normal single-λ caveats from
exp-002/003 apply per point.

The eps_z values are not bit-identical to 2.25 at every λ (integer-cell
rounding perturbs the ratio slightly, 2.2228–2.2907) — this is expected
and stated up front, not adjusted for; it mirrors exp-014's own r1
rounding to the nearest cell.

## Predictions — committed before the run

- **P1 (gates):** box_dev ≤2% and cross_dev ≤2% at all 12 cloak runs —
  matching exp-003/014's own margins on this identical domain machinery.
- **P2 (reproduction):** the λ=600nm points reproduce exp-014's reused
  core=30/eps_z=2.25 numbers (Q_ext=0.6620 at floor=0.10, Q_ext=0.5449
  at floor=0.18, jump=−17.69%) to <1% relative — same geometry, same
  code path, same precedent exp-003's own P2 and exp-017's P2 set for
  this kind of cross-file reproduction check.
- **P3 (the discriminator — does the trough track eps_z or λ?):**
  compute `jump(λ) = (Q_ext(0.18) − Q_ext(0.10)) / Q_ext(0.10)` at each
  of the 6 λ points. Two falsifiable, mutually exclusive outcomes:
  - **eps_z-only outcome:** `jump(λ)` stays negative at **4 or more of
    the 6 λ points** (including λ=600nm) — the trough persists across a
    79% range of shell-radial-extent-in-wavelengths (2.40λ–4.30λ) as
    long as eps_z stays in its established window, meaning the trough is
    a property of eps_z alone, not tied to any particular electrical
    size or standing-wave condition.
  - **λ/grid-resonance outcome:** `jump(λ)` is negative at λ=600nm (near
    shell≈3.00λ) but flips non-negative at **2 or more of the other 5**
    points — the trough weakens or disappears as the shell's electrical
    size moves away from whatever condition λ=600nm/cpl=20 sets up,
    meaning eps_z alone doesn't determine the trough and a resonance-like
    mechanism is back in play.
  No directional prediction is made on which outcome obtains — this is a
  genuine open question, the same honesty convention exp-016/017 used.
- **P4 (secondary, not scored pass/fail):** if the eps_z-only outcome
  holds, `jump(λ)` magnitude should correlate more closely with each
  point's own small eps_z variation (2.2228–2.2907, following exp-014's
  established local trough shape) than with λ or shell-radial-extent —
  worth checking qualitatively against exp-014's own 7-point curve, not
  a hard pass/fail gate given only 6 points here.

## Results

18 runs (12 cloak + 6 empty references), 17.6 min.

| λ (nm) | shell (λ) | Q_ext(0.10) | Q_ext(0.18) | jump `(Q18−Q10)/Q10` | box_dev (0.10 / 0.18) |
|---|---|---|---|---|---|
| 420 | 4.30 | 0.4574 | 0.8800 | **+92.39%** | 1.81% / 0.37% |
| 480 | 3.70 | 0.4896 | 0.9109 | **+86.04%** | 0.41% / 0.08% |
| 540 | 3.35 | 0.6284 | 0.6543 | **+4.13%** | 0.66% / 1.12% |
| 600 | 3.00 | 0.6620 | 0.5449 | **−17.69%** | 0.01% / 0.69% |
| 660 | 2.75 | 0.6201 | 0.6391 | **+3.06%** | 1.02% / 1.16% |
| 750 | 2.40 | 0.6810 | 0.7082 | **+3.99%** | 0.98% / 1.70% |

All 12 points: box_dev ≤1.81% (max at λ=420/floor=0.10), cross_dev
≤0.085% throughout — well inside the gate.

### Predictions scored

- **P1 (gates ≤2%) — CONFIRMED.** Max box_dev 1.81%, max cross_dev
  0.085%, comfortably inside the 2% band at all 12 points.
- **P2 (reproduction) — CONFIRMED, exactly.** λ=600nm gives
  Q_ext(0.10)=0.6620, Q_ext(0.18)=0.5449, jump=−17.69% — bit-identical
  to exp-014's reused core=30 numbers. Same geometry, same code path.
- **P3 (the discriminator) — CONFIRMED as the λ/grid-resonance outcome,
  and more decisively than the falsification bar required.** The
  negative jump appears at **exactly one** of the 6 λ points (λ=600nm)
  — not just 2+ of the other 5 flipping non-negative as the minimum bar
  set, but **all 5** of the other points come back positive, two of
  them (420nm, 480nm) by huge margins (+86–92%, not small positive
  numbers near zero). eps_z barely moves across the sweep (2.2228–
  2.2907, a 0.068 range — see the P4 discussion below) while the jump
  swings from −17.69% to +92.39%, a ~110-percentage-point range. eps_z
  alone clearly does **not** determine the trough; something tied to λ
  itself — or to whatever λ=600nm/cpl=20 sets up geometrically — does.

### The sharper finding: shell thickness in exact wavelengths

The `shell (λ)` column makes the mechanism visible. λ=600nm is the
*only* sweep point where the shell's radial extent lands on an **exact
integer number of wavelengths**: `r2 − r1 = 60 cells = 3.00 × 20 cells
= 3.00λ` exactly (60 and 20 are both exact integers by construction —
`R1_BASE`/`R2_BASE`/`CPL` — so this isn't a rounding coincidence at this
one point, unlike every other λ in the sweep, where rounding r1 and r2
independently to integer cells leaves `shell/λ` at an irrational-looking
fraction: 4.30, 3.70, 3.35, 2.75, 2.40). The negative jump sits at
precisely the one point with a **clean standing-wave condition**
(shell thickness = integer × λ) — the classic signature of a
Fabry-Pérot-like resonance across the shell's radial extent, not a
smooth function of eps_z. This reframes exp-017's "resonance tied to
the λ=600nm/cpl=20 grid" candidate from a vague possibility into a
sharp, testable hypothesis: **the trough is a standing-wave condition
set by shell-thickness-in-wavelengths landing on (or near) an integer,
not a property of eps_z at all** — eps_z=2.25 only ever looked special
because exp-002 happened to choose r1=30/r2=90 (shell=60 cells=3.00λ
exactly) as its original baseline geometry, for reasons unrelated to
eps_z.

This single sweep can't yet distinguish "any integer works" from
"specifically 3λ is special" (only one integer point was sampled), nor
rule out that the effect is graded rather than a sharp resonance (540nm
at 3.35λ and 660nm at 2.75λ — the two nearest-neighbor points — both
show small *positive* jumps, not near-zero ones sitting on a smooth
ramp toward the 3.00λ dip, which is itself informative: whatever this
is, it looks localized near 3.00λ rather than a wide, gentle trough in
`shell/λ` space).

- **P4 (secondary, eps_z correlation) — clearly not supported, worth
  saying plainly rather than silently dropping.** Predicted (as an
  unscored secondary) that if eps_z-only held, jump magnitude would
  track each point's own small eps_z wobble. It doesn't — eps_z is
  *flattest* exactly where jump swings most (420nm and 600nm both sit
  at eps_z=2.2500, identical to 4 decimal places, yet jump is +92.39%
  at one and −17.69% at the other). The data points unambiguously at
  shell-thickness-in-λ, not eps_z, as the operative variable.

### Headline

**The eps_z trough is not an eps_z effect.** Holding eps_z within its
established trough window (2.22–2.29) while sweeping the shell's
electrical size across a 79% range (2.40λ–4.30λ) makes the negative
floor-jump vanish at every point except λ=600nm — the one point where
shell thickness lands on an exact integer number of wavelengths (3.00λ).
This overturns the working frame this whole line has carried since
exp-014: the "eps_z≈2.25 trough" language in exp-006/011–017 was
tracking a coincidence of exp-002's original geometry choice (shell=60
cells=3.00λ at cpl=20), not a real feature of `Q_ext(eps_z)`. The real
candidate mechanism is a shell-radial-extent standing-wave / Fabry-Pérot
condition — new, sharper, and not yet directly tested (this experiment
found the clue by varying λ at fixed eps_z; the natural next step is
the reverse: fix λ and sweep shell thickness in cells finely enough to
resolve whether the dip really peaks at exactly 3.00λ or nearby, the
same resolution-vs-coarse-sweep lesson exp-005/010/015 already taught
this lab three times over).

## Next

- **[open, high priority]** Directly test the standing-wave hypothesis:
  at fixed λ=600nm/cpl=20 (so 1 cell = λ/20 exactly), sweep shell
  thickness (`r2 − r1`, holding one of r1/r2 fixed) finely around
  multiples of λ (e.g. bracket both 2λ=40 cells and 3λ=60 cells,
  stepping 1 cell at a time as exp-014 did for eps_z) and check whether
  the negative-jump feature re-appears at 40 cells (2λ) too, or is
  unique to 3λ. A positive result at 2λ as well would confirm a general
  "shell = integer × λ" resonance law; a null result at 2λ would mean
  3λ specifically (not integers generally) is special, a different and
  more interesting question.
- **[open]** This experiment varied shell thickness by changing r1 *and*
  r2 together (proportional scaling, holding eps_z fixed) — the natural
  companion is a sweep that changes shell thickness while holding eps_z
  *deliberately off* the trough window, to check the standing-wave
  effect isn't itself entangled with eps_z after all (this experiment
  is suggestive, not yet a clean single-variable isolation — eps_z did
  wobble by 0.068 across the sweep, small but not exactly zero).
- exp-014/015/016/017's "eps_z trough" framing should be considered
  superseded pending the follow-up above — PLAN.md updated to reflect
  this as an open reframe, not a settled renaming, until the 2λ check
  either confirms or narrows the new hypothesis.
- The `mu_r_floor < 0.05` direction and the parking lot remain open,
  unchanged.
