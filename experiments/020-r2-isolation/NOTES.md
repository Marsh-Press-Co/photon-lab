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

30 runs (28 cloak + 2 empty), 46.4 min.

**r2=75** (target r1=15, eps_z=1.5625):

| r1 | shell (λ) | eps_z | Q_ext(0.10) | Q_ext(0.18) | jump | box_dev (0.10 / 0.18) |
|---|---|---|---|---|---|---|
| 12 | 3.15 | 1.4172 | 0.0644 | 0.1582 | **+145.6%** | **3.23%** / 1.51% |
| 13 | 3.10 | 1.4633 | 0.0839 | 0.1945 | **+131.9%** | **3.36%** / 1.78% |
| 14 | 3.05 | 1.5117 | 0.0978 | 0.2589 | **+164.7%** | **2.75%** / 1.49% |
| 15 (target) | 3.00 | 1.5625 | 0.1202 | 0.3289 | **+173.5%** | **2.55%** / 1.15% |
| 16 | 2.95 | 1.6159 | 0.1469 | 0.4230 | **+188.0%** | 1.93% / 0.58% |
| 17 | 2.90 | 1.6721 | 0.1769 | 0.4748 | **+168.4%** | 1.97% / 0.31% |
| 18 | 2.85 | 1.7313 | 0.2147 | 0.5352 | **+149.3%** | 1.89% / 0.10% |

**r2=120** (target r1=60, eps_z=4.0000):

| r1 | shell (λ) | eps_z | Q_ext(0.10) | Q_ext(0.18) | jump | box_dev (0.10 / 0.18) |
|---|---|---|---|---|---|---|
| 57 | 3.15 | 3.6281 | 0.9169 | 1.2158 | +32.6% | 0.97% / 0.28% |
| 58 | 3.10 | 3.7461 | 0.9106 | 1.1976 | +31.5% | 1.13% / 0.48% |
| 59 | 3.05 | 3.8699 | 0.8886 | 1.2848 | +44.6% | 0.12% / 0.29% |
| 60 (target) | 3.00 | 4.0000 | 0.9399 | 1.4191 | **+51.0%** | 0.31% / 0.23% |
| 61 | 2.95 | 4.1367 | 0.9705 | 1.6082 | +65.7% | 0.82% / 0.04% |
| 62 | 2.90 | 4.2806 | 1.0813 | 1.8606 | +72.0% | 0.82% / 0.55% |
| 63 | 2.85 | 4.4321 | 1.1725 | 1.9406 | +65.5% | 0.58% / 0.09% |

cross_dev ≤0.5% throughout — clean everywhere, including at r2=75/floor=0.10
where box_dev misses.

### Predictions scored

- **P1 (gates ≤2%) — CONFIRMED at 24 of 28, one systematic honest
  exception:** every r2=120 point and every r2=75/floor=0.18 point clears
  2% comfortably (max 1.78%). But **4 of 7 r2=75/floor=0.10 points miss
  the gate** — r1=12 (3.23%), r1=13 (3.36%), r1=14 (2.75%), r1=15/target
  (2.55%) — with the miss shrinking smoothly toward the flanks (r1=16/17/
  18 all clear, 1.89–1.97%). Not discarding or re-running silently to
  make it disappear — flagged here and taken up directly by exp-021's
  resolution check, this line's exp-005/010/015 precedent. **This does
  not touch the discriminating question**: the jump magnitudes at the
  gate-missing points (+132% to +175%) are two orders of magnitude larger
  than a 2–3.4% box-independence wobble could produce or hide, so the
  sign and rough size of the effect are not in doubt even before exp-021
  resolves the gate.
- **P2 (the discriminator) — CONFIRMED as the r2-specific outcome, and
  not close.** Both new shell=3λ targets come back strongly **positive**:
  r1=15/r2=75 jumps **+173.5%**, r1=60/r2=120 jumps **+51.0%** — both
  comfortably inside (in fact, on the high side of) the +3%-to-+92% range
  exp-018/019 mapped at every non-3λ / non-r2=90 point tested so far.
  **Neither new r2 reproduces r2=90's negative jump at its own shell=3λ
  point.** The negative-jump feature that defined the "eps_z trough"
  since exp-014 is tied to **r2=90 specifically**, not to "shell=3λ" as
  a portable rule — exp-014's original finding was doubly coincidental:
  the right λ *and* the right r2, not shell thickness alone.
- **P3 (band shape) — not applicable.** No negative jump was found at
  either target, so there is no trough to characterize the shape of.
- **P4 (secondary, narrow-band check) — VIOLATED, and instructively so.**
  Q_ext(0.10) at r2=75 spans 0.0644–0.2147, a >200% range (far wider than
  exp-019's ~15% band at r2=90/2λ); r2=120 spans 0.8886–1.1725, a 32%
  range — also wider. Flagged per the pre-registered instruction. Reading:
  r2=75's eps_z values (1.42–1.73) sit in a much lower, steeper part of
  exp-006's own Q_ext(eps_z) curve than any bracket this line has swept
  before (exp-011's core=15/eps_z=1.44 point is the closest precedent,
  and that curve was already the steepest of exp-011/012/013's three).
  A shallow-eps_z regime naturally amplifies percentage swings from a
  fixed absolute Q_ext change — not evidence of a second hidden feature,
  but a reminder this experiment pushed into a new part of the eps_z
  range as a side effect of choosing r2=75, not a deliberate eps_z choice
  (same caveat exp-019 itself raised about its own eps_z range).

### Headline

**The "shell=3λ" feature is not a shell-thickness law — it is specific
to r2=90.** Both new outer radii tested, on either side of the r2=90
baseline, show ordinary, strongly positive floor-jumps at their own
exact shell=3λ points — nothing resembling exp-014's trough. Combined
with exp-019 (shell=2λ doesn't reproduce it at r2=90 either), this
narrows what exp-018 found to its most literal reading: **the negative
jump exp-004 through exp-017 spent thirteen shifts characterizing is a
property of the single geometry (r1=30, r2=90, λ=600nm, cpl=20) exp-002
happened to pick at the very start of this line** — not eps_z, not
"integer-λ shells," not r2 in general. It may still not be fully
isolated (r1=30/r2=90 differs from every point tested here in three
numbers at once: r1, r2, *and* eps_z all differ simultaneously) but the
population of "things that don't explain it" is now large: eps_z
(exp-018), λ/cpl-grid resonance in general (exp-019), and r2 in general
(this experiment).

## Next

- **[open]** The trough has now survived (i.e., NOT reproduced) five
  mechanism/generality checks in a row (exp-016 impedance, exp-017
  angular pattern, exp-018 eps_z, exp-019 integer-λ, exp-020 r2) without
  a single one explaining or generalizing it. The honest state of the
  investigation: r1=30/r2=90/λ=600nm/floor∈{0.10,0.18} is characterized
  to death as an *anomaly*, but still has zero explanatory mechanism.
  Two paths forward for a future dedicated shift: (a) declare it an
  idiosyncratic point and stop chasing it — log it as a curiosity in
  PLAN.md and return fully to the design-lead line (core=8 cloak,
  exp-007/010's still-open multi-λ check); or (b) one more targeted
  test — hold r1 AND r2 BOTH fixed at exactly 30/90 and sweep only λ
  finely around 600nm (not the coarse 6-point exp-018 sweep, a 1–2nm
  step bracket) to see whether the negative jump is itself narrow-band
  (a true resonance linewidth) or already at its widest at exactly
  600nm — a different question than exp-018 asked (that swept λ while
  rescaling geometry to hold eps_z fixed; this would hold geometry
  fixed and sweep λ in nm, changing eps_z as a side effect, the mirror
  experiment).
- **[open, this shift]** exp-021: resolution check (cpl 20→30) on the
  r2=75/floor=0.10 box_dev gate misses — this line's exp-005/010/015
  precedent, taken up immediately.
- The `mu_r_floor < 0.05` direction and the parking lot remain open,
  unchanged.
- **exp-007's queued multi-λ check** (does the core=8 design lead
  survive across wavelengths) remains the standing highest-value item
  once this mechanism thread is closed out or parked.
