# Phase 2 Critique — THERMODYNAMICS

**Panel Iteration 79, exp-102 ("The Coherent, Phase-Resolved Downstream
Point-Intensity Instrument"). Blind, parallel critique — no access to any
other seat's Phase-2 output this cycle.**

## Steel-man

The proposal correctly scopes itself as diagnostic-only on an article whose
absorbed-power regime is already exhaustively characterized from my seat's
own history. The reused R4-family configs/angles (C40_R4/G40_R4, 600 nm, the
same 6 angles) were `netd_row()`-scored UNDETECTABLE at exp-101 (368× margin,
R21-compliant — narrated, not merely persisted), and the new Gate-B θ=0° leg
reuses the ORIGINAL flagship article (`graded_black_shell`, r_out=78,
σ_max=0.5) whose thermal margin was independently re-derived three times
(exp-043/054/057) and LOCKED at 699.27× UNDETECTABLE through the corrected
`mixed_length_scale_regime`/`Q_ext(x)` chain — this program's most heavily
audited thermal number. No wavelength, incident power, or geometry anywhere
in this proposal falls outside either already-scored regime. If Phase 3
confirms no new `netd_row()`-eligible construction is introduced, my seat can
honestly certify zero new thermal work is owed this cycle — a legitimate,
disciplined scope call, not an omission by neglect.

## Sharpest attack

The proposal is completely silent about the thermal sidecar — zero mention
of `netd_row`/`cell_metrics_r4`/`thermo_sidecar`/UNDETECTABLE anywhere, not
even a one-line "N/A, see exp-101/exp-057" disposition — despite PANEL.md's
own metrics table binding "every run" to record "Joule accounting + THERMO
sidecar." That silence is not idle: exp-101's own `run.py` imports `netd_row
= exp095.netd_row` directly and calls it inside the shared R4-family
`cell_metrics_r4`/`pair_metrics_full` pipeline that this proposal's own
geometry (`box_for_r4`, `ref_for_r4`, `R4_CONFIGS`) is drawn from — and this
codebase has an established, documented pattern of experiments importing
prior `run.py` modules wholesale for that shared machinery (the exp-098
`sys.modules` collision, Iteration 78). If Phase-3's implementation reuses
that pipeline for convenience — plausible, since it is the fastest path to
the already-gated `phasors`/`full_capture` calls this proposal wants — a
sidecar row is persisted as an unplanned byproduct with zero Phase-1
acknowledgment it could even happen: exactly the un-narrated-persistence
shape R21 exists to catch, on the same article family that produced R21's
own two founding instances one and two cycles ago. Silence is not a stated
N/A.

## Verdict

**Support-with-changes.**

## Parameter change that would flip to plain support

Add one explicit sentence — a "Thermal sidecar" line in Idealizations or a
new subsection — stating whether `netd_row()`/`cell_metrics_r4` will be
invoked at all this cycle. If not invoked: cite exp-101 (R4-family
configs/angles, UNDETECTABLE, 368× margin) and exp-057 (flagship θ=0°,
LOCKED 699.27× margin) as the standing disposition covering every
configuration this proposal touches, and state plainly that no new
absorbed-power regime is introduced. If invoked (even incidentally, via
reused R4-family machinery): commit up front, in Phase 1, to narrating the
result in Result per R21 — not merely persisting it — before any FDTD call
runs.

## RULED OUT / Live Thread re-tread check (my discipline only)

None found. Nothing in this proposal re-treads a RULED OUT item from a
thermodynamics angle — no mechanism parameter (σ(I), σ(x,t), or otherwise)
touching absorbed power is proposed at all, consistent with its own
diagnostic-only framing. Live Thread **T5** (the thermo ledger) is not
closed and this proposal does not claim to close it — correctly left
untouched. T8's near-field caveat and T9's Babinet-ceiling disclaimer are
correctly restated, not contested. The one real risk is not a re-tread of a
closed item but the live, still-open R21 exposure described above.
