# exp-008 — The Bare-Disk Control

**2026-08-10 · driver: Clyde (cloud shift 4) · status: predictions committed, not yet run**

exp-007 traced Q_ext(cloak) down to core=8 and found a strictly
monotonic, still-improving curve (new best Q_ext=0.0429, ~15× better
than the exp-002–005 baseline), but flagged an honest caveat it did not
resolve: shrinking `core` (r1) while holding `r2=90` fixed changes *two*
things at once — (a) the physical size of the hidden PEC object, which
trivially scatters less on its own the smaller it is, and (b) the shell
thickness / `eps_z`, which exp-006 already showed is its own genuine,
monotonic knob on Q_ext (thinner shell, worse cloak) *independent* of
core size. exp-006/007's sweep conflates the two because both ride on
the same `r1`. This experiment isolates (a) alone: strip the cloak shell
entirely and measure the *bare* PEC disk's own Q_ext across the same
core radii, so the cloaked-vs-bare comparison can show how much of
exp-007's "design lead" is real transformation-optics work versus
"there's simply less object left to hide."

## Method

Reuses exp-006/007/003's exact domain (N=680, cpl=20, λ=600nm,
courant_frac=0.32, absorb=40, box_a/box_b at half=110/135, same source
line and cross-section machinery — `sc.full_capture` / `sc.widths`) so
every gate and normalization convention lines up point-for-point with
the existing cloaked data. The only change: `materials.pec_disk(sim, cx,
cy, r1)` alone, no `schurig_reduced_cloak_tm` call — no shell, no
`mu_r_floor`, nothing else in the domain.

**Core sweep: the full 7-point set exp-006/007 already characterized
with a cloak** — r1 ∈ {8, 10, 12, 15, 20, 25, 30} cells — so every bare
point has an exact cloaked counterpart to divide against. All 7 rather
than the "3–7" minimum floated in exp-007's NOTES: the full curve is the
same handful of extra runs and gives a complete ratio curve instead of
three isolated samples, which matters for P3 below (a trend claim needs
more than 3 points to be convincing).

`q_ext` uses the **same normalization as exp-006/007**:
`sigma_ext / (2·R2_CELLS)` with `R2_CELLS=90` fixed throughout, even
though there is no shell here and no literal "r2" — this keeps every
bare-disk number on the identical fixed-footprint scale as its cloaked
counterpart, so `Q_ext(cloaked)/Q_ext(bare)` at matched `r1` is a
dimensionless, directly comparable ratio.

## Idealizations (same bench, restated for this experiment)

- 2D TMz, hand-rolled FDTD, absorbing boundary (not a true PML) — same
  caveats as every prior experiment in this lab.
- The PEC disk is ideal (zero-field, no loss) — same idealization as
  exp-001's reflector object and every cloak's hidden core.
- Single λ=600nm only — this control does not attempt the multi-λ story;
  if it changes the headline, checking whether the ratio trend holds
  across λ is a natural follow-up (exp-002/003's line).

## Predictions — committed before the run

- **P1 (gates):** box independence ≤ 2% and the two extinction routes
  agree ≤ 2% at all 7 bare-disk points. (Expect *tighter* than the
  cloaked runs, if anything — a bare PEC disk is a simpler, more
  isotropic scatterer than a graded anisotropic shell.)
- **P2 (bare Q_ext also rises with radius — the trivial baseline):** the
  bare disk's `Q_ext` increases monotonically with `r1` across all 7
  points, same qualitative direction as the cloaked curve. This is
  expected, ordinary Mie-regime physics (a bigger PEC cylinder scatters
  more) and is *not* by itself evidence about the cloak — it is the
  effect this experiment exists to separate out.
- **P3 (the discriminating prediction — does the shell do real work?):**
  the ratio `Q_ext(cloaked, r1) / Q_ext(bare, r1)` — computed at the 7
  matched `r1` values from exp-006/007's data and this experiment's data
  — is **not flat** across the sweep. Specifically, given exp-006's
  independent finding that thinner-shell (`eps_z` closer to 1, i.e.
  smaller `r1` at fixed `r2`) is a genuine, monotonic knob that makes
  the shell scatter *more* relative to a thicker shell, we predict the
  ratio **rises** as `r1` shrinks (i.e. the cloak's *relative*
  suppression is weakest exactly where exp-007's absolute numbers look
  best) — meaning at least part of exp-007's "design lead" is the
  trivial smaller-object effect, not the shell working harder. A flat or
  falling ratio as `r1` shrinks would refute this and mean the thin
  shell is doing *more*, not less, relative suppression at small core —
  strengthening exp-007's design-lead claim rather than undercutting it.
- **P4 (magnitude floor):** at every core radius tested, including the
  smallest (`r1=8`), the bare disk's `Q_ext` is *larger* than the
  matched cloaked `Q_ext` — i.e. the shell is doing *some* real
  suppression work at every scale in this sweep, even if P3's ratio
  trend shows that work is proportionally uneven. A crossover (bare
  disk scattering *less* than the "cloaked" object at any point) would
  be a red flag worth stopping to understand before trusting either
  number.

## Results

_pending — run not yet executed._

## Next

_pending._
