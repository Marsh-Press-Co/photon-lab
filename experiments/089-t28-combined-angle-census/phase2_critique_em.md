# PHASE 2 — CRITIQUE · ELECTROMAGNETISM (blind) · exp-089

## Steel-man (≤150 words)

The desk-computable half of this proposal is genuinely clean. I recomputed
all three R13 margins directly from the cited `FLOOR=1.91744×10⁻⁴` and
exp-083's committed `frac_contrast` values: 4.162655×10⁻⁴/FLOOR=2.171,
2.830881×10⁻⁴/FLOOR=1.476, 2.510967×10⁻⁴/FLOOR=1.310 — all three PASS
calls reproduce exactly, at zero new FDTD cost, before a single new field
is computed. `frac_contrast`, `p_abs_w`, and the P1/P2/P4/non-negativity
preconditions are unchanged from exp-087/088's already-validated
machinery, so nothing new is asked of the solver's own energy bookkeeping.
R14(a)'s parent-smoothness check and (b)'s shared-config-pair disclosure
are both honestly deferred to Phase 4 rather than assumed away. Q5
correctly reframes a possible `ratio_k>10` reading as evidence about
`FLOOR_FRAC`'s own adequacy rather than new physics — the right
instrument-skepticism default for a floor-gate this thin.

## Sharpest attack (≤150 words)

R14(c)'s "half of the established period" is not an EM linewidth — it's
a Nyquist-style sampling bound borrowed from `delta_scene`'s single-tone
fit, applied to a different quantity (`frac_p_abs`) whose only directly
measured feature to date is a **3.07× swing across a single 0.2° step**
(38.4°→38.6°, exp-088/R14). Nyquist safety at P/2-spacing presumes the
signal is well-approximated by its fundamental tone; this program's own
founding R14 evidence says the opposite for `frac_p_abs` specifically.
The proposal's own tightest-margin gap, 1.4° (38.8°→40.2°), is exactly
**7.0×** the already-demonstrated 0.2° feature width, clearing the
half-period bound by only 0.02°–0.075° while sitting nowhere near the
scale where structure is already known to exist. Separately: Q4's two
"recurrence" pairs are spaced at Δθ=3.0°, which PHOTONICS/Red Team
already flagged (exp-087, Iter. 64) as within 1.8% of exact aliasing
against `P*=2.9474°` — sampling almost exactly one period apart makes
recurrence near-tautological for any curve with fundamental-tone power,
independent of whether the mechanism is genuine energy-coupling
continuity or the still-causally-unattributed domain artifact this
sub-thread has chased for 14+ cycles.

## Verdict: support-with-changes

## Parameter change that would flip toward unqualified support

Replace R14(c)'s bound with the empirically-demonstrated scale: require
interior checks denser than the already-observed ~0.2°-wide feature
(not half of an unrelated interference period), and add one Q4 control
angle at a non-period-aliased offset (e.g. Δθ≈1.5° from 37.2° or 38.4°,
away from the 3.0° grid) so a REFUTE-vs-CONFIRM read at 40.2°/41.4°
can't be explained by sampling-interval aliasing alone. Absent either
fix, Q4's "CONFIRM" signature is compatible with a pure sampling
artifact and cannot itself close Q5's floor-gate-adequacy question the
way §6 implies it can.
