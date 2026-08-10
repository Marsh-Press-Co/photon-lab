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

8 runs (7 bare-disk cores + 1 empty), 5.1 min.

**Bare-disk Q_ext vs cloaked Q_ext (exp-006/007) at the same 7 core radii,
λ=600nm, both normalized by the same fixed `2·R2_CELLS=180`:**

| core (r1, cells) | Q_ext (bare) | Q_ext (cloaked) | ratio cloaked/bare | box_dev | cross_dev |
|---|---|---|---|---|---|
| 8 | 0.2211 | 0.0429 | **0.194** | 0.013 | 0.002 |
| 10 | 0.2679 | 0.0520 | 0.194 | 0.012 | 0.002 |
| 12 | 0.3061 | 0.0591 | 0.193 | 0.010 | 0.001 |
| 15 | 0.3752 | 0.0934 | 0.249 | 0.002 | 0.001 |
| 20 | 0.4911 | 0.2592 | 0.528 | 0.009 | 0.001 |
| 25 | 0.6189 | 0.4913 | 0.794 | 0.011 | 0.001 |
| 30 | 0.7356 | 0.6620 | **0.900** | 0.004 | 0.001 |

box_dev ≤ 1.3%, cross_dev ≤ 0.2% at every point — the tightest gates of
any experiment in this line so far.

### Predictions scored

- **P1 (gates) — CONFIRMED, and tighter than predicted.** box_dev ≤ 1.3%,
  cross_dev ≤ 0.2% at all 7 points — cross_dev in particular is roughly
  5–10× tighter than the cloaked runs' typical ≤1% (a bare PEC disk is a
  simpler scatterer than a graded anisotropic shell, as expected).
- **P2 (bare Q_ext also rises with radius) — CONFIRMED.** Strictly
  monotonic: 0.2211 → 0.2679 → 0.3061 → 0.3752 → 0.4911 → 0.6189 →
  0.7356. Ordinary physics, exactly as expected, and — as flagged going
  in — not itself evidence about the cloak.
- **P3 (ratio rises as core shrinks) — REFUTED, and the refutation is
  good news.** The ratio does the opposite of what was predicted: it
  *falls* as core shrinks, from 0.900 at core=30 down to a plateau of
  ~0.193 at core=8–12 (with a small, likely-within-noise dip from 0.194
  to 0.193 between core=10 and 12, well inside the 1.3% box_dev floor).
  The pre-registered fallback interpretation for exactly this outcome
  said it plainly: *"A flat or falling ratio as r1 shrinks... [means]
  the thin shell is doing more, not less, relative suppression at small
  core — strengthening exp-007's design-lead claim rather than
  undercutting it."* That is the honest reading here. At the best
  design point (core=8), the shell suppresses scattering to ~19% of
  what the same-size bare PEC disk would produce; at the exp-002–005
  baseline geometry (core=30), the shell only gets it down to ~90% of
  bare — the cloak there is barely doing anything relative to the
  object it's hiding. exp-007's ~15× absolute Q_ext improvement is
  **not** primarily "there's less object to hide" — the relative
  cloaking effectiveness itself is ~4.6× better at core=8 than at
  core=30 (ratio 0.194 vs 0.900).
- **P4 (magnitude floor, no crossover) — CONFIRMED.** Bare Q_ext exceeds
  cloaked Q_ext at all 7 points, including the closest approach at
  core=30 (0.7356 vs 0.6620, bare still 11% higher). No crossover
  anywhere in the sweep — the shell is doing *some* real suppression
  work at every scale tested, consistent with P4's framing, and the
  margin widens sharply as core shrinks (P3's finding).

### Reframed headline

exp-007's caveat is resolved, and resolved in the design lead's favor:
the core=8 result is not a trivial "small object scatters less" artifact
dressed up as a cloak improvement. The bare-disk control shows the
*opposite* structure — the shell's own relative effectiveness improves
sharply as it thickens (small core, large eps_z-ish geometry), fully
consistent with exp-006's independent finding that thinner shells are
worse. Two separate measurements (exp-006's fixed-r2 eps_z sweep, and
this bare-vs-cloaked ratio) now agree: **a thicker shell is a genuinely
better cloak**, not just a smaller hidden object. core=8/floor=0.10
stands as the lab's best-characterized cloak design, with its caveat now
closed rather than open.

## Next

- The ratio's own shape is interesting and untraced: near-flat
  (~0.193–0.194) across core=8–12, then a real rise starting at
  core=15. Worth knowing whether that plateau continues below core=8 or
  the ratio keeps falling — natural continuation of exp-007's
  downward-core exploration, now with the control in hand to interpret
  it correctly as it goes.
- exp-007's own queued follow-up stands: check whether the core=8 design
  lead (and now, its genuine relative-effectiveness advantage) survives
  across λ (exp-002/003's broadband-wall line), not just the single
  600nm anchor point every experiment in this thread has used.
- exp-006's still-open candidate B (rerun exp-004's full floor sweep at
  a non-baseline core, e.g. core=15 or 40) remains queued and untouched
  by this experiment.
