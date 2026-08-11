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
