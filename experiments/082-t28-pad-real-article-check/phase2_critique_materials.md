# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 59 · exp-082

**Seat: MATERIALS & METAMATERIALS.** Fresh sub-agent, zero memory of any
prior session. Blind to all other Phase-2 critiques of this cycle.

## Steel-man (≤150 words)

Both charter-relevant claims independently verify cleanly. **Tier-0 item 1
(x-wall refit):** `x_wall_realizable_refit.py` reuses exp-077's/exp-080's own
committed functions unmodified (`load_pair_geometries`,
`predicted_c_empty[_two_wall]`, `free_period_with_widening`,
`reflection_coefficient_vec_realizable`) and its `score()` thresholds
(period ≤0.30/>1.00, shape ≥0.30/≤0.05) are bit-identical to
`pad_round_trip_model.py::score_pair()` — no new scoring convention
invented. `x_wall_realizable_refit_results.json::verdict_flips` contains
exactly 2 entries (`single_wall/pair_absorb40` INCONCLUSIVE→REFUTE;
`two_wall/pair_pad` REFUTE→INCONCLUSIVE); neither lands on SUPPORT — "2 of 4
cells flip, none to SUPPORT" is accurate, checked against the JSON directly,
not the prose summary. **Primary article claim:** `run.py::build_article`
(`pec_disk(...,30)` + `graded_black_shell(...,30,dg.R_OUT=78)`) is
byte-identical to `exp-024/run.py::build("absorber")`'s own "stage-7 config
verbatim" branch (same R_OUT=78) — genuinely the ESTABLISHED flagship, not a
relabeled variant. The cross-cycle governance gap I flagged last cycle is
honestly restored and closed, not swept past.

## Sharpest attack (≤150 words)

The SURVIVES verdict (`ratio=0.6573`, `A_scene/C_thr=0.68`) rests on exactly
one article: the flagship `graded_black_shell`, whose own baseline
`C≈−0.55` is already ~100× past `C_thr` by design — it's *meant* to be a
deep silhouette; whether it's "visible" was never in question. Comparing the
PAD-wobble's own amplitude to `C_thr` borrows threshold language from the
regime where it's actually diagnostic — near-null σ(I) OFF-state articles,
the specific class `REALIZABILITY_MEMO.md`'s UNOBTANIUM-WITH-PARAMETERS
verdict addresses — and applies it here without evidence the confound's
*relative* weight is article-independent. Idealization 5 names this gap and
defers it as a "natural next comparison," but from my charter's angle it is
the load-bearing test, not a follow-up: nothing here shows a weak,
near-threshold article would see the same 0.68× reading rather than a
qualitatively different one. Until run, "SURVIVES at material amplitude"
should be read as bearing on this one strong absorber's own citations only —
not on any σ(I)-realizability question.

## Verdict: **support-with-changes**

Both audited claims (x-wall refit count, article identity) are correct and
should stand as reported. Change requested: the write-up's own framing
("every future ambient-contrast citation... should now disclose this as a
named, quantified... confound") should be scoped explicitly to
strongly-absorbing/flagship-class articles until the near-null article case
is tested — it currently reads as a general finding about the channel,
which my charter's evidence does not yet support.

## Single parameter change that would flip my verdict

Rerun the identical `PAIR_PAD`/C40–G40 harness with `build_article`
replaced by the near-null σ(I) OFF-state construction (`off_pass`,
`τ_off≈0.0065`, exp-032/exp-034) in place of `graded_black_shell`. If
`ratio` and `A_scene/C_thr` there land in a comparable range to this cycle's
0.66/0.68 reading, the article-independence gap closes and I'd move to full
support.
