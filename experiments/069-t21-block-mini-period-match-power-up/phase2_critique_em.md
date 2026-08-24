# Phase 2 — Critique · ELECTROMAGNETISM · Panel Iteration 46 (exp-069)

*Fresh sub-agent, ELECTROMAGNETISM charter. Blind to other seats' Phase-2
critiques this cycle, per PANEL.md independence mechanics.*

## Steel-man (≤150 words)

This is disciplined, correctly-scoped instrument closure, in exactly the
T27/T24 idiom that has repeatedly caught this program's own errors. It fixes
all three real defects in `P-VIS42-10` at once: settled `STEPS=2800`
(avoiding the exact transient-vs-fringe confound T27 identified — an
unsettled reading cannot discriminate a real fringe from a settling
artifact even in principle, since both share the same geometric clock), 31
points over ≈3 periods instead of 5 over ≈1 (adequately powered to resolve
periodicity, not just amplitude), and a genuinely pre-registered,
non-overfit period-match statistic (fixed-`T` linear least squares — no
nonlinear-fit convergence risk, no post-hoc period tuning). G-1 correctly
gates every downstream number on bit-exact reproduction of already-committed
data before anything new is trusted, and P-069-4 closes the one real
settling gap left in T27's own record — `C80` has never had a 3-point
convergence check at any angle. A legitimate, falsifiable test of my own
seat's mechanism against the null it was purpose-built to distinguish.

## Sharpest attack (≤150 words)

§4's claim that `Δ(sinθ)=cpl/A` is the "exact global period," "not a new
idealization," doesn't survive scrutiny. exp-042's own NOTES.md (Phase 1,
lines 20-27) states `P(θ)=λ/(A·cosθ)` is "the [full Huygens–Fresnel aperture
integral] model's own **stationary-phase limit**" — a leading-order
asymptotic, not an exact closed form — and it was fitted, never to R²=1.0
(0.7852 at Iteration 19, 0.8271 after Iteration 43's refit): 17-23% of
variance stays unexplained, origin never identified. The source is a
raised-cosine (Tukey) taper, `edge=40` cells (5.3% of A=752), not a sharp
two-point edge; nothing here bounds how apodization shifts the effective
diffracting-edge location, hence `T`, away from `cpl/A` exactly.
Differentiating a *local* formula only fixes `T` uniquely if that formula
holds identically at every θ in the window — never independently verified;
it's a self-consistency check, not a re-derivation. Over the proposal's own
3-period span, even a few-percent `T` error accumulates real phase drift,
degrading the FIXED-`T` primary gate's R² — risking a false CONFIRM
("additive-systematic vindicated") even where a real, slightly-detuned
coherent fringe exists — while P-069-3, the one instrument built to catch
exactly that, is explicitly diagnostic-only, non-gating.

## Supporting notes (not counted against the caps)

- **On idealization 7 (`A=752` "fixed and unverified anew"):** `A` is a pure
  geometric constant (`obj_y − y_lo`, `design_geometry.py:276`) fixed by the
  `C40`/`C80` construction, independent of `STEPS` by construction — `STEPS`
  controls only wall-clock time-stepping, not cell geometry, so it cannot
  shift `A` directly. The genuine STEPS-dependence is different and more
  interesting: at `STEPS=1400` the causal wavefront from the far aperture
  rim (offset A=752 cells) may not yet have reached the observation window
  and rung down, so the *effective* (transient, not geometric) radiating
  aperture is smaller than the full 2A until settling completes — this is
  T27's confound exactly, and P-069-4 is the right (if narrowly-scoped —
  2 of 31 angles, `C80` only) direct test of it. Idealization 7 is safe as
  stated; the STEPS risk is already handled elsewhere in the design, not
  smuggled in unexamined.
- **On P-069-1's `ptp/|mean|` statistic:** worth a disclosed caveat, not a
  blocking objection. `delta(θ)` alternates sign at every adjacent 1°
  sample in the existing 600nm settling-delta dataset (desk_check output,
  `flip_fraction=1.0`) — a genuinely oscillatory signal centered near zero
  mean is exactly what a real coherent fringe riding on a small or zero
  additive offset should look like, but it also makes `ptp/|mean|`
  ill-conditioned: as `mean(delta)→0`, the ratio diverges regardless of
  physical amplitude, and the reverse (a real large-amplitude fringe with an
  accidentally large mean over this particular 31-point window) could
  understate it. The CONFIRM/REFUTE dichotomy (≤1.5 / >2.5) is not obviously
  passivity-violating — `delta` is a bounded difference of two Weber
  contrasts, itself Cauchy–Schwarz-bounded per T26 — but its numerical
  robustness near mean≈0 is not discussed anywhere in §5's table.

## Verdict

**Support-with-changes.**

## Single parameter change that would flip my verdict to unconditional support

Promote §4's secondary floating-period statistic (P-069-3) from
diagnostic-only to **co-gating** with P-069-2 — i.e., require the primary
fixed-`T` fit to clear its REFUTE band *and* the free-period search to land
within a disclosed tolerance of `T=cpl/A` — before the Combined-verdict row
reports "coherent-fringe perturbation, decisively established" or
"additive-systematic framing vindicated." As written, a real but
slightly-detuned T21 fringe (taper-shifted effective A, or higher-order
stationary-phase corrections neither this cycle nor Iteration 19/43 ever
bounded) could fail the rigid P-069-2 gate and be reported as vindicating
the null it was built to test against — exactly the false-negative failure
mode this LOCKED, four-cycle-deferred instrument cannot afford to reproduce.
