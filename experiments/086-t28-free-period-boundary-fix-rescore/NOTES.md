# exp-086 — T28 `free_period_with_widening` Boundary-Pinning Fix + Re-score

Panel Iteration 63. Lead: ELECTROMAGNETISM (rotation). Zero-FDTD instrument-
repair desk cycle, executing exp-085's own Red Team Phase-5 final audit's
§7 reconciled ranking (LOGBOOK.md Iteration 62), items 1–3 of its flat,
un-Tiered six-item list, folded with two cosmetic fixes (its items 4–5) into
one batch. Full phase record: `phase1_proposal.md` → five blind Phase-2
critiques → `phase2_redteam_audit.md` (PROCEED-WITH-MANDATORY-FIXES, 6
items, zero overridden) → `phase3_synthesis.md` (this cycle's frozen spec).

## Hypothesis

`free_period_with_widening` (shared machinery, reused across ~15 T28
experiments since exp-077) has a confirmed bug (new standing rule **R11**,
LOGBOOK.md RULED OUT registry): when every widening stage of its
staged-search fails to find an interior optimum, it silently returns the
NARROWEST stage's own (worst-fitting, most constrained) value instead of
flagging non-convergence. exp-085's own Phase-5 review found this corrupts
15 of Method C's 37 sub-window fits (6 of them the literal all-stage-
boundary case this cycle fixes), dropping the corrected `frac_recovered`
from the as-filed 1.000 to 0.595 by the audit's own hand computation.
Hypothesis: fixing the defect at the SOURCE (both files carrying the logic,
plus the identical-shape `_quiet` sibling) and re-running the full pipeline
(not a hand audit) reproduces that hand-computed collapse via the
automated, now-permanently-correct machinery, and closes the standing
audit-coverage gap on `free_period_with_widening_quiet` without disturbing
any currently-cited T28 REFUTE/INCONCLUSIVE verdict (which, independently
re-derived this cycle — see `phase3_synthesis.md` §2 item 2 — rests on a
shape-correlation statistic the bug never touches).

## Setup

Two source-code fixes: `free_period_with_widening` in
`experiments/077-t28-pad-round-trip-echo-model/pad_round_trip_model.py`
and `experiments/078-t28-y-wall-echo-prescreen/y_wall_prescreen.py`, plus
`free_period_with_widening_quiet` in the former — all three get the same
post-loop correction: if every stage stayed `at_boundary`, return the
WIDEST stage's own record with explicit `converged=False`/
`no_interior_optimum=True`, never the narrowest silently.

`experiments/086-.../phase4_rescore.py` (new): (1) re-runs exp-085's Method
C 37-sub-window fit on the corrected machinery, reusing the bit-identical-
verified `FastEval` (unchanged formula) to regenerate the 37 sub-window
curves; (2) extends the circular-shift null to all 37 sub-windows; (3)
computes the overlap-corrected Spearman test at all three pre-registered
non-overlapping stride phases (θc-start = 5°/7°/9°); (4) persists
`ss_tot_full`/`ptp` per sub-window; (5) re-runs `null_calibration_appendix`
in full (60,001 calls, corrected count) on the corrected quiet function
against exp-077's own committed real data, diffing every cited statistic;
(6) a bounded grep/re-derive audit of committed JSON in experiments
069–085 for any other silently boundary-pinned citation beyond the two
already-known-inert instances (exp-078, exp-079); (7) the two cosmetic
fixes (the `rd_wide_fft` "vs mean" mislabel in exp-085's own
`phase4_derivation.py` print statement, and NOTES.md's "62.8%" citation
corrected to the true mean-relative 91.6%).

## Idealizations

Single λ=600nm only (unchanged from every T28 desk cycle). Zero new FDTD —
every number is a closed-form/desk recomputation reusing already-validated,
bit-identical-verified machinery. The R11 fix changes ONLY the non-
convergent-search selection/flagging logic; `_free_period_search`/
`_fixed_period_fit`'s own grid-search and least-squares math is untouched.
The grazing-incidence amplitude blow-up PHOTONICS found (~5,444×–6,631×
`ptp` growth across the sub-windows) is disclosed, not resolved: it raises
an open question about whether `edge_diffraction_c_empty_corrected` remains
inside its own valid near-field regime there. The joint EM/THERMO energy-
interception cross-check is structurally exempt this cycle — no
article-loaded FDTD scene exists anywhere in its scope (matching
exp-084/085's own established exemption language).

## Predictions (frozen, committed BEFORE any Phase-4 code runs — see
`phase3_synthesis.md` §3 for full derivation and falsifiers)

1. Boundary set under corrected machinery: exactly 6/37 sub-windows
   (`θc∈{45,59,61,63,71,73}`).
2. `frac_recovered` = **21/37 = 0.5676** exactly.
3. `classification_a` = **NOT STABLY PERIODIC** — carrying forward, every
   place this label is reported, exp-085's own instrument-reliability
   caveat: a statement about what this doubly-corrected instrument can
   currently certify, NOT a claim that no near-normal-quarter periodicity
   exists.
4. Spearman at three pre-registered stride phases: θc-start=5° →
   ρ=0.8571, p=0.0238 (clears p<0.05); θc-start=7° → ρ=0.4286, p≈0.35
   (does not); θc-start=9° → ρ=0.5357, p≈0.24 (does not). Headline:
   phase-dependent, not a single robust verdict.
5. Prior-citation audit: no additional currently-cited T28 headline number
   found corrupted beyond the two already-known-inert instances.
6. Corrected `null_calibration_appendix` (quiet-variant, full 60,001
   calls): `p_r2_ge_070` ≤ 0.02 (up from currently-cited 0.0);
   `max_r2_over_trials` inside `[0.56, 0.78]` (up from currently-cited
   0.5609, staying below both real interior-optimum R² values, 0.8165 and
   0.7156). **Falsifier, pre-registered, Checkpoint-4-relevant**: if
   `p_r2_ge_070` corrected exceeds 0.05, OR `max_r2_over_trials` corrected
   meets/exceeds 0.7156, that materially threatens the significance-of-
   the-real-signal framing exp-077's REFUTE-adjacent record currently
   carries and must be escalated at Phase 5, not absorbed quietly.
   Bootstrap-recovery stats predicted to shift <0.01° absolute (the
   bootstrap fits a signal dominated by the real, already-interior-optimum
   `yhat`, essentially never boundary-pins).

## Result

*(filled after Phase 4 runs)*

## Learned

*(filled after Phase 5)*

## Next

*(filled after Phase 5)*
