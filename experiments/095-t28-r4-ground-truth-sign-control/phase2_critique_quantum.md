# Phase 2 Critique — QUANTUM OPTICS (blind, independent)

*Panel Iteration 72, exp-095. Charter: non-classical absorption,
state-dependent or coherent interactions; mechanisms enter the bench only
as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω), gain —
or Red Team strikes them. This critique is written blind to all other
seats' Phase-2 output.*

## Steel-man (≤150 words)

This is a faithful, disciplined execution of the demand Red Team's own
Iteration-71 audit ranked #1 — a synthetic ground-truth-recovery gate
generalized (R6-style) to a new resolution family, run *before* further
`R4`-family spend, not after. The sequencing is right: 8 cheap calls gate
60 expensive ones, and the go/no-go criterion is committed, numeric, and
pre-registered before any FDTD call. The angle choice is principled, not
arbitrary — 37.2° is excluded by name, citing its own documented
thin-margin history (2.17×→1.046× floor margin across resolutions), rather
than cherry-picked after seeing data. Rank 3 is gated on Rank 1 by an
honest, argued extension of Red Team's literal text, not a loophole taken.
R13/R14/R16 compliance and Gate 5's fault-injection verification are
built in from first draft, correcting exactly the two overclaim shapes
exp-094 shipped. It does not overclaim: PASS licenses further spend, it
does not certify every prior `R4` reading (Idealization 24).

## Sharpest attack (≤150 words)

The control angles were chosen *because* they sit far from any null —
the proposal's own stated rationale ("no ambiguity about the correct
answer"). But `delta_scene(θ)` is independently established, across
R13/R14/R15's own three-cycle lineage, as a genuinely oscillatory,
coherent-interference quantity (period ≈2.84–2.95°, a real zero-crossing
near θ₀≈38.59°). Near a node, sign is set by the *relative phase* between
two coherent contributions being differenced; far from a node — exactly
where 39.2°/39.8° sit — the total is amplitude-dominated and comparatively
phase-insensitive. A coordinate/registration defect in the new family
perturbs phase, not amplitude. So a sign check at antinode-like points has
near-zero statistical power against precisely the defect class this gate
exists to catch — one that would manifest *only* near a node, which is
exactly where every substantive `R4` finding this cycle lives (the
41.75–41.9° reversal, the 38.4° flip). Idealization 24 names this gap in
one sentence but the gate design does nothing to mitigate it.

## Verdict: **support-with-changes**

The sequencing, cost discipline, angle-exclusion reasoning, and R13–R16
compliance are sound and represent real, disclosed improvement over
exp-094. But the go/no-go gate as designed is structurally blind to the
one failure mode (phase/registration error) most likely to hide precisely
where this cycle's headline findings live. That is a real gap in the
control's power, not merely an idealization footnote — it should be closed
before the finding is trusted, not merely disclosed and carried forward a
fifth time in this sub-thread's idealization list.

## Single parameter change that would flip this to full support

Replace one of the two off-node control angles (39.8°, the weaker-margin
of the two: `ratio_k`=3.84 vs. 39.2°'s 0.92) with a **node-location
recovery check**: verify `delta_scene(R4)` brackets zero near the
already-established θ₀≈38.59° crossing (from `cpl=20`/`cpl=30`) within a
stated tolerance (e.g. ±0.1°), rather than testing a second off-node sign.
A node-location test is phase-sensitive by construction — it is powered
against exactly the registration-defect class an off-node sign check
cannot see — at no meaningful addition to the call budget already
committed.
