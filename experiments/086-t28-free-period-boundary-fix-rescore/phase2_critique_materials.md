# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 63 · exp-086

*Fresh context, blind to all other seats' current-cycle critiques. Read in
full: PANEL.md; LOGBOOK.md RULED OUT (R1–R11) and the complete T28 live-thread
entry, Iterations 46–62; `experiments/085-.../phase5_redteam_audit.md` in
full; my own seat's prior finding, `experiments/085-.../
phase5_review_materials.md`; `phase1_proposal.md` (this cycle); and both
target source files, read line-by-line, not taken on the proposal's word.*

## Charter applicability

**The realizability bound does not engage this cycle.** Independently
verified by reading `pad_round_trip_model.py::free_period_with_widening` and
`y_wall_prescreen.py::free_period_with_widening` in full: neither function
(nor anything in the proposed fix) contains a permittivity, admittance,
reflectance, or absorption parameter — this is a pure post-loop selection-
logic repair to a curve-fitting search, operating on an already-existing,
unmodified vacuum-only Kirchhoff sum. "Zero realizability content," same
finding I reached independently at exp-085's own Phase 5, for the same
reason, still true here — my seat has nothing to bound. Per this cycle's own
instruction, I apply my seat's rigor instead to the re-scoring methodology
and the underlying model's physical grounding.

## Independent verification performed

Read both `free_period_with_widening` implementations directly (not the
proposal's description of them). Confirmed exactly, by hand-tracing the
`chosen`-update loop: `chosen is None or (chosen["at_boundary"] and not
at_boundary)` fires once, at stage 1, and never updates again once every
subsequent stage is also `at_boundary` — algebraically, `chosen["at_boundary"]`
survives the full loop **iff every stage was boundary-pinned**, exactly the
detection condition the proposal's fix logic claims (I re-derived this
truth-table myself rather than accepting the claim). Confirmed the call-path
trace (`phase4_derivation.py`→exp-084's `phase1_derivation.py`→
`ywp=_load(EXP078_DIR/y_wall_prescreen.py)`) is accurate — this is genuinely
the version exp-085's Method C calls.

Independently recomputed the θc=45° edge case from `experiments/085-.../
derivation_results.json::method_c.sub_results` directly (not the proposal's
table): `p_local_reported_at_39=4.0` exactly (a boundary value), `p_local_
corrected=4.396°` — under the audit's 6° proxy filter by coincidence, even
though θc=45° is one of the six confirmed all-stage-boundary windows. This
reproduces the proposal's own claimed 21/37=0.568 vs. 22/37=0.595 split
exactly, from raw data, not from the proposal's arithmetic.

## Steel-man (≤150 words)

This is exactly the disciplined, narrowly-scoped repair R11 calls for, and I
verified its two load-bearing claims from source myself rather than trusting
the write-up: the bug trace is correct, and the fix's detection condition
(`chosen["at_boundary"]` after the loop ⟺ all stages pinned) is algebraically
sound, not a heuristic. The proposal goes a genuine step further than the
audit it executes: it caught that the audit's own `>6°` period proxy and a
`converged`-flag criterion disagree at exactly one window (θc=45°) for a
reason (narrow-stage boundary value happening to fall under 6° by
coincidence) neither of exp-085's own Phase-5 reviews named — and
pre-registered both possible counts (21 vs. 22 of 37) with an explained
tolerance band rather than picking one after running. Scope discipline
(explicit idealizations, house-convention flag-not-rewrite on exp-085's own
file) matches this sub-thread's own hard-won standards.

## Sharpest attack (≤150 words)

Prediction (4) claims "no currently-cited T28 headline number is corrupted,"
but the audit scope backing that claim explicitly excludes
`free_period_with_widening_quiet` — the 2-stage sibling with the **identical**
`chosen is None or (chosen["at_boundary"] and not at_boundary)` bug shape,
which I traced directly to `null_calibration_appendix` (`pad_round_trip_
model.py` lines 274–350): it is called **40,000 times** (20,000 pure-noise +
20,000 bootstrap trials, `n_trials=20000`) feeding exp-077's own null-
calibration appendix, the evidentiary basis for the x-normal/unrealizable-
admittance REFUTE that every T28 cycle since Iteration 54 cites as settled.
That is a far higher-volume, more consequential use of this exact defect
shape than the 37-window case this cycle fixes, yet it receives no bounded
firing-rate check at all — only a disclosed idealization, not a caveat on
Prediction (4) itself, which reads more sweeping than what was actually
audited.

## Verdict: **support-with-changes**

## Parameter/design change that would flip verdict to plain support

Scope Prediction (4)'s language explicitly to the non-quiet
`free_period_with_widening` citation set it actually audits, **and** add one
cheap, bounded sanity check on `free_period_with_widening_quiet`'s own
historical firing rate inside the already-persisted 20,000-trial null/
bootstrap arrays it feeds (a distribution-shape check, e.g. what fraction of
`p_star_deg` values sit at the `{1.0,4.0,15.0}°` stage boundaries — no new
FDTD, comparable cost to this cycle's own §2 prior-citation grep) before this
cycle's own record asserts no currently-cited number is corrupted.
