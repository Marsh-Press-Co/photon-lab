# PHASE 2 — PHOTONICS CRITIQUE · Panel Iteration 63 · exp-086

*Blind, fresh context. No other seat's critique seen.*

## Steel-man (≤150 words)

The bug trace is exact, not restated: I re-read `pad_round_trip_model.py`
374–407 and `y_wall_prescreen.py` 325–361 directly. The `chosen`-update rule
`if chosen is None or (chosen["at_boundary"] and not at_boundary)` only ever
updates away from the first (narrowest) record when a later stage is
*not* boundary-pinned; if all three stages pin, `chosen["at_boundary"]`
stays `True` for the entire loop, so testing it post-loop is a correct,
sufficient detector — exactly R11's condition, no new heuristic. The
proposal also catches something Red Team's own §1.4 hand table missed:
`θc=45°` is a confirmed all-stage-boundary case whose *narrow-stage*
`p_local_corrected=4.397°` happens to sit under the 6° proxy filter by
coincidence, so a flag-based (`converged==True`) criterion is strictly more
correct than the width-proxy filter alone — a genuine independent
improvement, not a restatement.

## Sharpest attack (≤150 words)

I recomputed `c_sub` (the actual `edge_diffraction_c_empty_corrected`
curve fed to Method C) at the six flagged θc via `FastEval`, bit-identical
to exp-085's own verification. Signal amplitude (`ptp`) grows **~5000×**
from θc=5° (ptp=2.6e-4) to θc=63° (ptp=1.39) before falling again at
71–73° — a real, large, angle-dependent feature of the model's own optical
response the proposal never inspects. The narrow-stage R² at grazing angles
is high (0.75–0.99) precisely because the amplitude there is enormous, not
because a period is well-resolved — yet the proposal's uniform
`r2≥0.30`-plus-`converged` bar treats a θc=5° fit (ptp~1e-4, plausibly
noise-floor) as equally "recovered" as a θc=63° fit sitting on a
signal four orders of magnitude larger. Worse: this amplitude blow-up
approaching grazing incidence is the textbook signature of an edge-wave/
shadow-boundary singularity in geometric diffraction theory — the proposal
never asks whether `edge_diffraction_c_empty_corrected` even remains
physically valid there, treating the whole grazing region as merely
"unresolvable by this window" when it may not be periodic in the assumed
sense at all. `ss_tot`/`ptp` per sub-window is already computed (inside
`free_period_with_widening`'s own `rec`) and silently discarded, exactly
the pattern R11 was adopted to stop.

## Verdict: support-with-changes

The fix itself is correct, minimal, and precisely scoped — I independently
re-derived the detection condition and confirmed it matches R11's own text.
But the batch should not ship a "NOT STABLY PERIODIC" (or any) headline
without persisting and reporting the per-sub-window amplitude scale
(`ss_tot`/`ptp`, already computed, currently thrown away exactly like
`at_boundary` was before R11) alongside `r2_local` — a scale-blind R²
threshold cannot distinguish "genuinely resolved small oscillation" from
"noise-floor fit" at one end, or "real large-amplitude structure, window
too narrow" from "formula leaving its valid regime" at the other.

## Flip parameter

Add one field — `ss_tot_full` (or `ptp`) per sub-window — to
`phase4_rescore_results.json`, already computed inside
`free_period_with_widening`'s own `rec` dict and currently discarded. That
alone would let this and future cycles check whether "recovered" windows
span a coherent amplitude scale before any classification is drawn from
them; its absence is the only thing keeping this from a plain SUPPORT.
