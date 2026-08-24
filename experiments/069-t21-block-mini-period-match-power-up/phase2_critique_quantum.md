# PHASE 2 — CRITIQUE · QUANTUM OPTICS · Panel Iteration 46 · exp-069

*Seat charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters, or Red Team strikes them. Fresh context,
blind to the other five Phase-2 critiques this cycle.*

## Steel-man (≤150 words)

This properly executes the sequence my own seat demanded and Red Team
silently dropped last cycle with no argued reason (exp-068
`phase5_redteam_audit.md` Finding 1c). `desk_check_settling_delta.py` runs
first, reads exp-066's real 36-row `closure_summary` (verified: C_1400/
C_2800/theta/lambda_nm present, 36 rows), and its `flips()` correctly
scores only true 1°-adjacent pairs within the positive/negative θ branches
separately — it never crosses the ±35° gap. §4's statistic is a genuine
advance over R5, not a repeat: instead of normalizing a locally-measured
zero-crossing offset by an approximate period (R5's fatal flaw — real
zero-crossings span 0.137P–1.279P, a 9.3× spread), it fits the exact,
analytically-derived global period `T=cpl/A` in `sinθ`, held fixed (zero
free period parameters), across a window spanning ~3.03 full periods — a
materially different, better-conditioned quantity. It also correctly
isolates the settling confound my own Phase-5 self-catch flagged at
exp-065 (a settling transient shares T21's own geometric clock) via a
dedicated 1400/2800/4200 gate (P-069-4) before trusting the period-match
result.

## Sharpest attack (≤150 words)

P-069's Combined Verdict overclaims. It controls exactly one confound —
settling, via P-069-4 — but not the other this exact geometry invites: the
`ABSORB` boundary is a Cartesian Yee-grid staircase realization of a
physical edge, and any staircase/numerical-dispersion ripple from that
edge generically carries the SAME characteristic angular scale as T21's
continuum Huygens period, since both derive from the identical edge the
grid discretizes. R3 is this program's own standing meta-rule ("any
surprising feature gets a resolution check before it gets a mechanism
debate — and 'artifact' claims need the check too"), yet exp-069 runs
`cpl=20` only, zero resolution sweep anywhere. A REFUTE+REFUTE result would
license "coherent-fringe perturbation, decisively established... not
settling" (§5) without ruling out "grid-discretization structure at the
T21 scale" — a live QUANTUM-charter distinction this design cannot make.
Secondarily: the desk check's "600nm cleanest, least-aliased" framing
(used to justify the 600nm-only scope) is backward — all three λ sit below
Nyquist (`samples_per_period<1` for all three in the desk-check output),
so 600nm's `flip_fraction=1.0` is the signature of *maximal* aliasing, not
clean resolution.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to full support

Add a minimal `cpl` resolution-check leg — e.g. rerun the two dense-sweep
peak/trough angles (or the 39.0°/40.0° cells already earmarked for Block
SETTLE-C80) at `cpl=30`, this program's own established R3 resolution-step
(exp-025 precedent) — before P-069-2's REFUTE band is allowed to license
the "coherent-fringe... not settling" language in §5's Combined Verdict.
Absent that, a REFUTE+REFUTE outcome should be reported as "period-locked
structure consistent with T21's formula, mechanism vs. grid-discretization
artifact undetermined" rather than "decisively established," and the
desk-check's "600nm least-aliased" justification for the single-λ scope
should be struck or reworded to state the correct fact (all three λ are
sub-Nyquist at 1° sampling; 600nm's clean alternation is not evidence of
better resolution).
