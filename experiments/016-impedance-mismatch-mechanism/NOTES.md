# exp-016 — Mechanism candidate 1: outer-boundary impedance mismatch

## Hypothesis

exp-014/015 confirmed a grid-independent, contiguous trough in
`Q_ext(eps_z)` near eps_z≈2.18–2.41 (core=30, r1=29–32) — the
`mu_r_floor=0.10→0.18` jump sign-flips there and nowhere else in
exp-006/011/012/013's four core/eps_z points. Two mechanism candidates
were queued in exp-015's Next section. This file tests the first: does
the shell's local impedance mismatch at the **outer** boundary (r=r2,
the wall the wave actually exits through) have a feature coincident with
the trough?

This revisits exp-006's P3, which used a *different* impedance-mismatch
story (√(mu_r/eps_z) with `mu_r` read as the *floor* value near the
*inner* wall) and refuted it for magnitude trend across a coarse 4-point
sweep. exp-016 is a distinct, sharper test: the outer-boundary mismatch,
at the trough's specific fine-grained location.

## Setup

Pure derivation from the exact code path used by every cloak run in this
lab (`schurig_reduced_cloak_tm`, `lab/materials.py`):

- `mu_phi` is hardcoded to 1 everywhere in the shell (`inv_phi = 1.0`),
  never clamped, never touched by `mu_r_floor`.
- `mu_r(r) = clip(((r-r1)/r)^2, mu_r_floor, None)` rises monotonically
  with `r` inside the shell (its r-derivative is positive throughout),
  so its **maximum** over the shell sits at `r=r2`:
  `mu_r(r2) = ((r2-r1)/r2)^2`. Since the same builder defines
  `eps_z = (r2/(r2-r1))^2`, this is **exactly `1/eps_z`** — *unless*
  `mu_r_floor` exceeds that value, in which case the outer wall itself
  clamps to the floor.

For a radially outgoing wave the relevant impedance ratio is
`eta_shell/eta_vacuum = sqrt(mu_phi/eps_z) = 1/sqrt(eps_z)` whenever
`mu_r_floor < 1/eps_z` (the unclamped case) — a function of **eps_z
alone**, with no floor dependence at all in that regime.

**Verification, not re-derivation** (house "verify-before-claim" rule):
rather than trust the algebra blind, built a bare `Sim`, called the
actual production `schurig_reduced_cloak_tm` builder, and read the real
`inv_mu["xx"]` tensor array at theta≈0 (the hx-grid row nearest y=cy,
0.5-cell offset → negligible angle at r2=90 cells) for the outermost
shell cell. No FDTD time-stepping anywhere in this file — pure material-
array inspection, near-zero compute (`run.py` finishes in ~1s, not
minutes).

Core points: the trough bracket (r1=27–33, exp-014/015) plus exp-006's
three other core/eps_z corner points (15, 40, 48), each probed at
floor=0.10, 0.18 (the trough's own pair) and 0.40 (deliberately above
`1/eps_z` for the high-eps_z corners, to expose clamping if it occurs).

## Idealizations

Static-array probe only — no wave propagation, no gates (box_dev/
cross_dev don't apply; there's no scattered field to measure). This
file establishes what the *material itself* looks like at the boundary,
not what the *fields* do there; it can rule a mechanism in or out on
smoothness/floor-dependence grounds but can't independently confirm the
resulting reflection actually behaves as the simple normal-incidence
`Gamma` formula predicts for a curved, graded, anisotropic boundary —
that would need an actual FDTD run (a genuinely different, heavier
follow-up if this candidate survives).

## Predictions — committed before the run

- **P1 (formula match):** the numeric `mu_r(r2)` read from the real
  solver arrays matches the analytic `1/eps_z` value to within a few
  percent (grid-quantization error — the outermost shell cell's true
  radius is slightly less than exactly 90 cells) for every core point at
  floor=0.10 and floor=0.18, confirming unclamped operation at r2
  throughout the range this investigation actually uses.
- **P2 (floor-independence in the trough's regime, floor-dependence
  above it):** `mu_r(r2)` is numerically **identical** between
  floor=0.10 and floor=0.40 for the trough-relevant core points
  (r1≤33, eps_z≤2.49, where `1/eps_z` stays above 0.40) — but
  **diverges** at floor=0.40 for r1=40/48 (eps_z=3.24/4.59, where
  `1/eps_z` = 0.309/0.218 is *below* 0.40), where the outer wall itself
  should clamp to 0.40 instead of the analytic value.
- **P3 (the discriminator — no local feature, and a structural
  disqualifier):** the resulting `|Gamma(eps_z)|^2` curve is smooth and
  monotonically increasing across the trough's bracket (2.04–2.49), with
  no local extremum near eps_z≈2.25–2.4. Combined with P2's floor-
  independence in this exact regime, this candidate mechanism **cannot**
  explain the floor=0.10→0.18 **sign flip** that defines the trough — a
  quantity with zero floor-dependence structurally cannot produce a
  floor-dependent sign change. A confirmed P3 refutes outer-boundary
  impedance mismatch as the trough's mechanism, on both magnitude
  (no local feature) and structural (no floor-dependence) grounds at
  once.

## Results

Probe complete in 0.5s (no FDTD stepping — pure array read).

| r1 | eps_z | analytic mu_r(r2)=1/eps_z | numeric[0.10] | numeric[0.18] | numeric[0.40] | \|Γ\|² |
|---|---|---|---|---|---|---|
| 15 | 1.4400 | 0.6944 | 0.6913 | 0.6913 | 0.6913 | 0.00826 |
| 27 | 2.0408 | 0.4900 | 0.4853 | 0.4853 | 0.4853 | 0.03114 |
| 28 | 2.1072 | 0.4746 | 0.4698 | 0.4698 | 0.4698 | 0.03393 |
| 29 | 2.1768 | 0.4594 | 0.4545 | 0.4545 | 0.4545 | 0.03688 |
| 30 (trough center) | 2.2500 | 0.4444 | 0.4395 | 0.4395 | 0.4395 | 0.04000 |
| 31 | 2.3269 | 0.4298 | 0.4247 | 0.4247 | 0.4247 | 0.04329 |
| 32 | 2.4078 | 0.4153 | 0.4102 | 0.4102 | 0.4102 | 0.04675 |
| 33 | 2.4931 | 0.4011 | 0.3959 | 0.3959 | 0.4000\* | 0.05040 |
| 40 | 3.2400 | 0.3086 | 0.3031 | 0.3031 | 0.4000 (clamped) | 0.08163 |
| 48 | 4.5918 | 0.2178 | 0.2122 | 0.2122 | 0.4000 (clamped) | 0.13223 |

\*r1=33's floor=0.40 column is a genuine, honest surprise (see below) —
not a bug.

### Predictions scored

- **P1 (formula match) — CONFIRMED.** Numeric mu_r(r2) matches the
  analytic 1/eps_z formula to within 1.0–1.4% at every point (e.g.
  core=30: 0.4395 vs 0.4444, 1.1% low) — the small, consistent gap is
  grid quantization (the outermost shell cell's true radius is 89.001,
  not exactly r2=90), exactly as expected, not a discrepancy in the
  formula itself.
- **P2 (floor-independence in the trough regime, clamping above it) —
  CONFIRMED, plus one honest surprise.** floor=0.10 and floor=0.18 give
  *bit-identical* mu_r(r2) at all 10 points including every trough
  point — full confirmation that in this file's regime, the outer-wall
  material is completely insensitive to which of the trough's two floor
  values is used. At floor=0.40: r1=40/48 clamp exactly to 0.4000 as
  predicted (analytic values 0.3086/0.2178 sit well below 0.40). The
  surprise is r1=33: analytic mu_r(r2)=0.4011 sits *just* above
  floor=0.40 (continuous formula predicts unclamped), but the actual
  grid cell's quantized value (0.3959, from P1's 1.4% grid-rounding gap)
  falls *below* 0.40 — so the real solver clamps this point even though
  the idealized continuous formula wouldn't. Flagged honestly: grid
  quantization can flip a point from "just unclamped" to "just clamped"
  right at the boundary of the two regimes P2 predicted — a real, small
  effect the analytic derivation alone would have missed, caught only
  because this file probed the actual arrays instead of trusting algebra.
  Doesn't touch the trough bracket itself (r1=27–33 at floor=0.10/0.18,
  the pair that actually matters here) — all of those stay cleanly
  unclamped and floor-identical.
- **P3 (the discriminator) — CONFIRMED, decisively.** `|Gamma|^2` rises
  smoothly and strictly monotonically from 0.00826 (eps_z=1.44) to
  0.13223 (eps_z=4.59) with **zero local extremum anywhere**, including
  a clean, featureless rise straight through the trough's bracket
  (0.03114→0.05040 across r1=27→33, no dip, no plateau, no sign change
  in the slope). Combined with P2's exact floor-independence at every
  trough point, this mechanism is doubly disqualified: it has no local
  feature to coincide with the trough's location, and it structurally
  cannot produce a floor-dependent sign flip in the first place, since
  its value doesn't depend on floor at all in this regime.

### Headline

**Outer-boundary impedance mismatch is refuted as the trough's
mechanism — cleanly, and for two independent reasons at once.**
`|Gamma(eps_z)|²` is smooth and monotonic with no feature near
eps_z≈2.25–2.4 (rules it out on magnitude), and it is exactly
floor-identical at every trough-bracket point (rules it out
structurally — a floor-independent quantity cannot explain the
floor-dependent sign flip that *defines* the trough). This is the
outer-wall analogue of exp-006's P3, which refuted the *inner-wall*
version of the same impedance-mismatch story for magnitude trend across
a coarser sweep; exp-016 closes the outer-wall version too, more
sharply, without needing a single FDTD run. One candidate mechanism
down; exp-015's other candidate (a scattered-field angular-pattern
comparison — does a new backscatter lobe appear inside the trough?)
remains open and is now the stronger lead, since it probes the actual
radiated field rather than the material's static boundary properties.

## Next

- **[open]** The angular-pattern candidate from exp-015's Next section:
  compare the scattered field's angular distribution across the trough
  (r1=29–32) vs its flanks (r1=27/28/33) to see whether the mechanism is
  a *shape* change (a new lobe) or a pure magnitude effect. This needs
  new instrumentation — `lab/sections.py` currently only reports a
  two-way forward/backward split (`fwd_frac`/`back_frac`) through the
  box faces, not a full angle-resolved pattern — so it's a genuine new
  capability, not a bolt-on to this file. Worth a dedicated follow-up.
- The r1=33/floor=0.40 grid-quantization surprise (P2) is a small,
  self-contained finding worth a one-line addendum to `materials.py`'s
  docstring if a future shift touches that file: continuous-formula
  clamp predictions can be off by one regime right at threshold points,
  due to the discrete grid never landing exactly on r2.
