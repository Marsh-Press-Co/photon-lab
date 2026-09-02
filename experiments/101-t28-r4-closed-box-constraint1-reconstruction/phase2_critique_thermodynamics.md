# Phase 2 Critique — THERMODYNAMICS seat, Panel Iteration 78 (exp-101)

## Steel-man (≤150 words)

The proposal correctly treats the thermo sidecar as inert this cycle: no
material, geometry, or `sigma_max` changes, so `sigma_abs`/`p_abs_w`'s
*physics* is unchanged from T9's established ~0.51 anchor, and the proposal
never leans on a re-radiation claim it hasn't earned. It is honest that
`sigma_abs` is "THERMO's route to a re-radiation risk against constraint 3"
without scoring anything against my charter's thresholds — the right
discipline for an instrument-fidelity cycle. `box_dev_scat_downstream`'s
reuse of the already-justified `XI_TOL` bound (R17) is the correct
conservatism, and predicting `ratio_abs_ext_raw` stays in [0.505, 0.520] is
a real, falsifiable, independently-recomputed band (0.5121–0.5149 measured
this cycle) rather than a restated round number. Zero `lab/` diff and
reused, gated machinery (`box_for_r4`/`ref_for_r4`/`widths_direction_
corrected`) is exactly the right footprint for a Tier-0 instrument fix.

## Sharpest attack (≤150 words)

§2.4/§2.5 commit this cycle to calling `cell_metrics_r4` on all 24 fresh
captures ("same captures already needed for `cell_metrics_r4`"), and
`cell_metrics_r4` (exp-094 `run.py:305-345`) unconditionally computes
`p_abs_w`/`dt_ss_full_K`/`netd_classification` via `netd_row()` for every
(theta, config) cell — 6 angles × 2 configs = 12 fresh cells, the *identical
shape* ("all 12 `netd_row()` classifications") as R21's second founding
instance (exp-100, Iteration 77). Four of the six angles have never been
run through the R4 thermo sidecar before (cpl20-native family only). Yet
§6's entire R16/R21 compliance paragraph commits to narrating in Result
prose only for `sigma_scat_downstream` — it names `p_abs_w` nowhere in that
paragraph, and §4's four predictions never mention `p_abs_w`/`dt_ss_full_K`/
`netd_classification` at all. R21's text is explicit: a third occurrence
"fires Checkpoint criterion 4 automatically, no further deliberation." This
proposal's own committed pipeline will regenerate the exact artifact that
fired twice before, with no written commitment to narrate it.

## Verdict: support-with-changes

## Parameter change that would flip to full support

Add one explicit line to §6's R16/R21 bullet (and a matching Phase-3
NOTES.md commitment) binding this cycle's own fresh `netd_row()` output —
`p_abs_w`, `dt_ss_full_K`, `netd_classification`, for all 12 (theta, config)
cells — to inline Result-section narration, not merely persistence to
`results.json`, with the same code-enforced-assert treatment §2.4 already
gives `sigma_scat_downstream`'s call/row counts (R19). Absent that explicit
commitment in writing before Phase 4 runs, this cycle carries a live,
concrete, verified risk of auto-firing Checkpoint criterion 4 on its own
third-strike NETD/thermal-sidecar channel — a structural risk to the whole
cycle's disposition, not a stylistic nit, and one my seat is chartered to
flag before the run rather than after.
