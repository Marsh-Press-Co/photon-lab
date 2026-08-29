# PHASE 2 — CRITIQUE · ELECTROMAGNETISM (blind) · exp-088

## Steel-man (≤150 words)

Cheap (8 calls), fully pre-registered, and the zero-FDTD gate is
independently verifiable today — I recomputed RMS[frac_contrast] over
exp-083's 31-point window, FLOOR, and all five margins directly from
`experiments/083-.../results.json::per_theta` and match the table exactly
(3.879×/0.386×/6.589×/7.495×/8.019× FLOOR at 36.0/38.6/41.8/38.4/38.8°).
`widths_direction_corrected()` is reused soundly: its sign flip is derived
per-call from the actual computed `i_inc`, not hardcoded to a geometric
assumption, and `design_geometry.py` confirms `src_x`/`obj_x`/`plane_x`
are fixed per config — only `angle_deg` varies with θ — so there is no
mechanism by which the -x-propagation convention could differ between
36.0/38.6/41.8° and the two new angles. `xi_ext` (P4) is a same-run
Poynting-box self-consistency check, algebraically unrelated to
`delta_scene`'s ambient-contrast null, and already measured cleanly
AT 38.6° itself (≤3.5×10⁻⁴, exp-087) with no node-proximity degradation —
no reason to expect new failure at ±0.2°.

## Sharpest attack (≤150 words)

R13's floor gate resolves the θ=38.6° question by *exclusion*, not by
*determination* — it retires the single most physically interesting point
rather than testing it. The ±0.2° bracket only bounds "is there a feature
broader than ~0.4° centered on the node"; nothing in §4/§6 argues why a
genuine localized energy-coupling anomaly (as opposed to a pure
denominator artifact) must be that broad. A critical-coupling/impedance-
match condition is exactly the EM effect class where a reference channel
(ambient Weber contrast) passes through a null while a physically
distinct absorption channel peaks sharply — the two channels need not
share a linewidth, and `frac_p_abs(38.6°)` reading smooth (exp-087,
PHOTONICS) rules out a *coincident* zero, not a narrower one on the
absorbed-power side alone. The proposal never invokes T28's own
established ~2.84–2.95° periodicity as a physically-motivated resolution
floor that would license treating a 0.4°-wide test as decisive. As
written, "both neighbors read CONSISTENT" gets treated (Q5) as closing
the *broad*-feature version of the question, which is honestly scoped —
but the write-up's own framing ("decisive resolution of the node-artifact
question," §6 intro to Q4) oversells that scope by omission.

## Verdict: support-with-changes

## Parameter change that would flip toward unqualified support

Add one sentence in §4 or §6 explicitly bounding the claim: state that
this bracket only rules out a feature ≳0.4° wide, cite T28's own
~2.84–2.95° established periodicity as the physical justification for
why a narrower one would itself be a new, separately-flagged anomaly, and
strike "decisive" from the §1 framing. (A stronger fix — an additional
θ=38.5° tighter bracket point, floor-clearing by the same §4 arithmetic
— would resolve it outright, but is not required to flip my verdict; the
scope caveat is.) This does not rise to oppose: R13-compliance,
`widths_direction_corrected()` reuse, and the `xi_ext` precondition are
all sound, and Q5 already declines to adjudicate the node's own physics
either way — the gap is in how tightly the surrounding prose claims that
non-adjudication actually closes.
