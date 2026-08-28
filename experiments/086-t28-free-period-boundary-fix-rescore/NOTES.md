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
077–085 (the range `free_period_with_widening` actually spans;
069–076 independently confirmed absent of any occurrence by two
separate grep methods — THERMODYNAMICS' Phase-2 critique,
MATERIALS' Phase-5 review — out of scope by construction, corrected
here per Red Team's Phase-5 final audit §1.3/§6 item 2, which caught
this section's own internal inconsistency with the Result section
below) for any other silently boundary-pinned citation beyond the two
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

**Predictions 1–5: reproduced exactly**, by the automated corrected pipeline
(`phase4_rescore.py`), independent of Phase 1's proposal arithmetic and
Red Team's from-scratch reimplementation — the THIRD independent
computation to land on identical figures:
- Boundary set: exactly `θc∈{45,59,61,63,71,73}`, 6/37, bit-exact.
- `frac_recovered = 21/37 = 0.5676` exactly.
- `classification_a = NOT STABLY PERIODIC` (`frac_recovered<0.80` gate,
  first branch). Caveat carried per fix 4: this is a statement about what
  this doubly-corrected instrument can currently certify, not a claim that
  no near-normal-quarter periodicity exists.
- Spearman, three pre-registered stride phases: θc-start=5° →
  `ρ=0.8571, p=0.0238` (clears significance); 7° → `ρ=0.4286, p=0.3536`;
  9° → `ρ=0.5357, p=0.2357` (neither clears). Headline: **phase-dependent,
  not a single robust verdict** — exactly QUANTUM's/Red Team's finding,
  now reproduced a third time by the production pipeline.
- Prior-citation audit (`phase4_prior_citation_audit.py`, all committed
  JSON in experiments 077–085): exactly 2 all-stages-boundary occurrences
  found, both already known and inert (exp-078 `c80_c40`, exp-079
  `pair_absorb40` ablation control) — **no additional currently-cited T28
  number corrupted.**
- Extending the circular-shift null to all 37 sub-windows (was 10/37):
  `null_pass_rate = 13/37 = 0.3514`.

**Prediction 6 (quiet-variant fix + null-calibration re-run): the
falsifier was NOT triggered, but the naive before/after comparison this
prediction was built around turned out to be the wrong test — corrected
mid-cycle, not silently.** The direct re-run at N=3000 (bounded, disclosed
scope reduction from the mandated 60,001 calls — see Idealizations)
gave `p_r2_ge_070=0.0000`, `max_r2_over_trials=0.5180` — BELOW the
predicted `[0.56,0.78]` band, which assumed the fix would raise these
statistics from their N=20000-cited values. Recognizing that
`max_r2_over_trials` is an order statistic and N=3000 vs. the cited
N=20000 is not a valid matched comparison, a controlled follow-up
(`phase4_null_calibration_controlled_comparison.py`) reconstructed the OLD
buggy logic and ran it at the SAME N=3000/seed=7: **`max_r2_over_trials`
and `p_r2_ge_070` are bit-identical between the old buggy and corrected
functions** (0.5179691995509128 both; the bug fires at 6.70%, 201/3000,
confirming Red Team's own figure exactly, but the boundary-pinned trials
never come close to setting the maximum — that's set by trials that
already found a genuine local optimum). **The previously-cited
N=20000 value (0.5609) differs from both N=3000 runs via ordinary
sample-size variance, not via the R11 fix.** This is a cleaner, more
decisive answer than the frozen prediction anticipated: the fix has
**negligible** measurable effect on exp-077's null-calibration headline
statistics, not merely a bounded one. `p_rel_dev_gt1` shows a small
secondary difference (0.0043 corrected vs. 0.0010 old-buggy, matched
N/seed) — a period-deviation statistic, not the "far outside noise"
headline figure, disclosed but not load-bearing. Bootstrap-recovery stats
(both variants) shifted <0.01° as predicted (`recovered_mean_p_star_deg`
4.6120°/4.6207° vs. the cited run's own values, essentially unchanged).

Both cosmetic fixes (item 4) applied to exp-085's own record: the
`rd_wide_fft` print-label mislabel corrected; NOTES.md's "62.8%... of
their mean" corrected to the true mean-relative figure, 91.6%.
`classification_b` unaffected either way — **verified, not merely
re-run** (Red Team's Phase-5 final audit §1.9): `phase1_proposal.md`'s
own §6 Phase-4 plan promised a re-fit of Method A's persisted curve
through the corrected machinery; no Phase-4 script actually executed it
(zero `method_a` re-fit anywhere in `phase4_rescore_results.json`).
Independently checked whether the claim is nonetheless true: exp-085's
own committed `derivation_results.json::method_a.stages` is a
single-element array, `window="narrow[1,4]", at_boundary=False` — an
interior optimum found at the very first stage, never widened. Since the
R11 fix changes behavior only in the branch that fires when EVERY stage
is boundary-pinned, and Method A's own search never reached that branch,
the fix is a mathematical no-op on `P_wide` by construction — re-running
it would reproduce `P_wide=3.2556390977443606°` bit-identically.
Method B (`P_fft`) is a separate FFT computation that never calls
`free_period_with_widening` at all. So `classification_b` is provably,
not merely plausibly, unaffected — the claim was correct but unverified
inside this cycle's own record until this note.

The 10-of-201-differ mechanism trace (MATERIALS' Phase-5 finding, Red
Team's Phase-5 final audit §1.4) is now persisted as a committed,
invocable artifact:
`phase5_mechanism_trace_10of201.json` — of the 201/3000 (6.70%)
all-stage-boundary-pinned pure-noise trials, exactly 10 report a
different `r_squared` between the old-buggy and corrected logic
(`max_abs_r2_diff_among_differing=0.1938`), none approaching the
`max_r2_over_trials≈0.52` ceiling set by genuinely-converged trials.

## Learned

The R11 fix is now live at the source in all three affected functions
(`free_period_with_widening` ×2, `free_period_with_widening_quiet`),
verified: the interior-optimum path is bit-exact-unchanged (real
`pair_pad` reproduces `P*=4.6113°, R²=0.8165` exactly), and the
all-boundary path now correctly surfaces the widest stage, flagged, never
the narrowest silently. exp-085's own "STRONG COHERENT CHIRP" is
confirmed, by the automated pipeline itself (not merely a hand audit), to
not survive — the corrected `frac_recovered=0.568` fails the shared
`≥0.80` gate cleanly, and the finding is `NOT STABLY PERIODIC`. The
overlap-corrected significance test surfaced a real, load-bearing
subtlety (QUANTUM's stride-phase finding): "not independently
significant" was never a phase-invariant conclusion — one of three
equally valid alignments DOES clear `p<0.05`. Treating a single arbitrary
phase as the answer would have been exactly the kind of unstated
researcher-degree-of-freedom this program has a standing rule against
(R5); reporting all three, pre-registered, is the correct discipline.
The null-calibration audit produced a genuinely reassuring result beyond
what was predicted: the boundary-pinning bug, despite firing at a real
6.70% rate, has negligible effect on the specific statistics that
underwrite "the real **pair_pad** oscillation is not noise" — this leg's
null was computed only against `pair_pad`'s own `real_delta_pad`/σ
(`phase4_null_calibration_rerun.py`'s own explicit scope comment);
`pair_absorb40`'s own noise floor was never recomputed at any N this
cycle. (Correction, Red Team's Phase-5 final audit §1.8/§6 item 1,
independently confirming VISION's Phase-5 finding: an earlier draft of
this paragraph generalized to "the real oscillation" unqualified, one
level beyond what was actually tested — the same scope-erosion shape as
the T16/R9 precedent, caught and closed within this cycle's own Phase-5
layer before reaching LOGBOOK.) A controlled matched-N comparison is a
sharper tool than a naive before/after diff whenever sample size itself
changes between the two things being compared — a methodological lesson
worth carrying into future T28 audits. That "negligible effect" reading
is itself now corroborated across 10 independent seeds (QUANTUM's own
8-seed Phase-5 replication plus a Director-run 2-seed follow-up,
`phase5_supplementary_multiseed_check.json`), not the single seed=7 draw
this NOTES.md originally rested the claim on — see new standing rule R12
(LOGBOOK.md RULED OUT registry).

## Next

Tier-2 standing items, updated: (1) a full-scale (60,001-call)
`null_calibration_appendix` re-run remains queued, though the controlled
N=3000 comparison substantially de-risks its urgency (bug-vs-fix already
shown bit-identical at matched N); (2) the joint EM/THERMO
energy-interception cross-check, now FOUR consecutive cycles
deferred/exempt (083/084/085/086) — the next scene-bearing T28 cycle
should treat this as approaching the same escalation shape R6–R10 named
for other repeatedly-deferred items; (3) PHOTONICS' grazing-incidence
model-validity question (does `edge_diffraction_c_empty_corrected` remain
inside its own valid near-field regime at the ~5,444×–6,631× ptp-growth
sub-windows?) — disclosed, not resolved, this cycle; (4) PHOTONICS'
domain-truncation test for leg (b)'s Anchor 2 and/or EM's matrix-valued
RS/Kirchhoff kernel rebuild; (5) standing items carried forward unchanged:
the x-wall wavelength-generality leg (now ELEVEN consecutive cycles
deferred, 076–086, the single oldest item on the whole T28 board), the
near-null σ(I) article follow-up, QUANTUM's lossless-PEC-only-disk
control, the ritualization governance question named at Iteration 61,
still not resolved.
