# exp-020 — R2 Isolation: is shell=3λ special, or is r2=90 special?

**2026-08-12 · driver: Clyde (cloud shift 10) · status: predictions committed, not yet run**

exp-018 reframed the "eps_z≈2.25 trough" (exp-014/015/016/017) as a
shell-thickness effect: at r2=90 (fixed since exp-006), the negative
floor-jump (Q_ext(0.18) < Q_ext(0.10)) survives only at r1=30, the one
point where the shell's radial extent (r2−r1=60 cells) is an exact
integer number of wavelengths — 3.00λ at cpl=20. exp-019 tested whether
*any* integer produces the effect by bracketing 2λ (shell=40) at the
same r2=90, and found no dip there — narrowing the hypothesis to "maybe
just 3λ specifically."

But every single point in this entire investigation line (exp-006
through exp-019) shares one thing that has never been varied: **r2=90
cells.** "Shell=3λ is special" and "r2=90 is special" have never been
told apart — exp-019's own queued follow-up. This experiment moves r2
itself, for the first time in the line, while holding shell=3λ=60 cells
fixed (cpl=20, λ=600nm unchanged) at each new r2.

## Setup

Same domain/box *convention* as exp-006 through exp-019 (N=680, cpl=20,
courant_frac=0.32, absorb=40, λ=600nm, STEPS=3600), generalized so the
box half-widths track r2 by the same fixed offset the line has used all
along at r2=90 (box_a=110=r2+20, box_b=135=r2+45) rather than the fixed
absolute values — this keeps every new r2's boxes at the same *relative*
clearance from the cloak wall that r2=90's own boxes have always had.

**r2 sweep: 75 and 120 cells** — brackets the shared r2=90 baseline from
both sides (r2=75 below, r2=120 above; r2=60 was considered but rejected
up front, it forces r1=0 — no core left once shell=60 is subtracted).

At each r2, **r1 (core) sweep is a ±3-cell bracket around the point where
shell = 60 cells = 3.00λ exactly** — the same bracket-around-the-target
idiom exp-014 used for r2=90/r1=30 and exp-019 used for r2=90/r1=50:

| r2 | target r1 (shell=60=3.00λ) | bracket r1 | eps_z at target |
|---|---|---|---|
| 75 | 15 | 12–18 | 1.5625 |
| 120 | 60 | 57–63 | 4.0000 |

**mu_r_floor sweep: 0.10, 0.18** — this line's defining pair, reused
exactly, unchanged since exp-006. `check_gates()` (run standalone first,
exp-011–019's own precedent) finds **zero exclusions** at either r2 —
every one of the 14 (r1, floor) combinations at r2=75 and all 14 at
r2=120 clear both the CFL ceiling and the graded-clamp degeneracy
threshold comfortably (worst CFL margin: r2=75/r1=12/floor=0.10,
ceiling=0.3765 vs courant_frac=0.32, an 18% margin; worst degeneracy
margin: r2=120/r1=63/floor=0.18, threshold=0.2256 vs floor=0.18, a 20%
margin). This is the first sweep in the whole eps_z/shell line with a
clean 100% inclusion rate — every prior floor-pair sweep at a bracket
this wide (exp-011/012/013/019) hit at least one exclusion.

7 core points × 2 r2 values × 2 floors = 28 cloak runs + 2 empty
references (box geometry differs by r2, so the empty reference is rerun
per r2, exp-006+'s own convention) = **30 runs total**.

## Idealizations

Same as the whole eps_z/shell-thickness line: 2D TMz, single λ=600nm,
near-to-mid-field box machinery (stage 8, trust-gated), reduced-parameter
cloak (`schurig_reduced_cloak_tm`) with the same `mu_r_floor` clamp this
whole line studies. Unlike exp-006–019, this experiment does NOT hold r2
fixed — that is the entire point, but it means the two r2 values tested
carry genuinely different physical cloak sizes (37.5% smaller and 33%
larger radius than the r2=90 baseline), not a rescaled-geometry
comparison the way exp-003's λ sweep held physical size constant. box_a/
box_b half-widths and their absolute pixel positions differ between r2
values by construction (fixed *offset*, not fixed *size*) — the two
r2's box-independence gates are not directly comparable pixel-for-pixel,
only each internally (box_dev per r2).

## Predictions — committed before the run

- **P1 (gates):** box_dev ≤2% and cross_dev ≤2% at all 28 cloak runs —
  matching this line's established margins. `check_gates()` predicts
  zero CFL/degeneracy exclusions at either r2 (see Setup); this is a
  prediction about measurement quality, not material validity.
- **P2 (the discriminator — is r1=15/r2=75 and r1=60/r2=120's own
  shell=3λ point negative, matching r2=90's r1=30 point, or positive,
  matching every non-3λ point exp-018/019 has tested?):** define
  `jump(r1, r2) = (Q_ext(0.18) − Q_ext(0.10)) / Q_ext(0.10)`. Two
  falsifiable, mutually exclusive outcomes, genuinely open (same honesty
  convention as exp-016/017/018/019):
  - **r2-specific outcome:** `jump` at BOTH new targets (r1=15/r2=75 and
    r1=60/r2=120) comes back positive, in the same +3%-to-+92% range
    exp-018/019 found at every non-3λ (or, per exp-019, non-r2=90) point
    tested so far — meaning the negative-jump feature is tied to
    r2=90 specifically, not to "shell = 3λ" as a portable rule. This
    would mean exp-014's original finding was doubly coincidental: not
    just the right λ, but the right r2 too.
  - **shell=3λ-general outcome:** `jump` is negative at one or both new
    targets — meaning shell=3λ IS a real, r2-independent standing-wave
    condition, and r2=90 was simply the first (and so far only) place
    this line happened to sample it. This would resurrect exp-018's
    original hypothesis in a stronger form than exp-019 left it.
- **P3 (band shape, secondary — only scored if P2 finds a negative
  jump):** IF either target shows a negative jump, does it form a
  contiguous multi-point trough across the ±3-cell bracket (mirroring
  exp-014's 4-point trough at r2=90), or is it an isolated single point
  (mirroring nothing seen yet in this line)? No prediction ventured on
  shape without first knowing P2's outcome — logged as a follow-on
  question, not gated.
- **P4 (secondary, not scored pass/fail):** `Q_ext(floor=0.10)` at each
  r2's own 7-point bracket should sit in a similarly narrow band to
  exp-019's own r2=90/2λ bracket (1.14–1.34, a ~15% range) rather than
  swinging wildly — consistent with ordinary point-to-point variation
  rather than a second hidden feature riding along with the r2 change.

## Results

*(not yet run)*

## Next

*(not yet written — depends on results)*
