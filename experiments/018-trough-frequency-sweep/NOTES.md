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

*(to be filled in after the run)*

## Next

*(to be filled in after the run)*
