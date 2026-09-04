# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's critique this cycle. Read
PANEL.md, LOGBOOK.md in full, PLAN.md's Current state, the Phase 1
proposal (`phase1_proposal.md`), and its subject code
(`experiments/108-.../run.py`, `analyze.py`, `results.json`,
`phase5_redteam_audit.md`, `NOTES.md`; `reclassify_106.py`;
`experiments/104-.../run.py`) before critiquing.

**Steel-man (≤150 words):** The fix is a genuine, non-vacuous test of a
real gate, not cosmetic paperwork. I independently re-derived
`fit["r_squared"]` from `results.json`: 0.6654 (r=156) and 0.0205
(r=312) — both fail the 0.90 smoothness bar, so the fallback branch
actually fires at both points rather than sitting dead. And the
fallback's own math is airtight: for any OLS fit with an intercept
(`A_mat=[1,1/margin]`), the mean model is a feasible fit point, so
`residual_std ≤ raw_std` always (population ddof=0 on both sides,
verified). That means the fallback cannot manufacture the exact defect
that created the R24 second instance — an unlicensed detrend inflating
confidence in a small "floor." My own re-derivation confirms CONFIRM
survives honestly at both r (2.96×/5.81× inside bar), not by omission of
the smoothness check.

**Sharpest attack (≤150 words):** §4's rejection of alternative (b)
(force AMBIGUOUS) leans on "`classify_item_i()`'s own CONFIRM branch is
unconditional on smoothness" as precedent for choosing a raw-std
fallback over forced-AMBIGUOUS. I traced `classify_item_i()` directly:
`linear_fit_1_over_margin` is called *only* inside the loop over `runs`,
which is populated only when contiguous REFUTE-bar-clearing bins exist.
Item_i's CONFIRM path (`confirm_all_margins and not runs`) never invokes
the fit at all — it isn't "deliberately unconditional on a smoothness
judgment," it is structurally incapable of ever facing one, because it
does no cross-margin trend fit in that branch. Item_ii's CONFIRM, by
contrast, is inherently a spread-across-margins statistic that must make
exactly the trend/noise call item_i's CONFIRM never makes. The "same
kind of null claim" analogy doesn't structurally hold — it's the
proposal's own load-bearing justification for this cycle's most novel
logic, and it's built on a misdescription of sibling code.

**Verdict:** support-with-changes

**Change that would flip to support:** Replace the item_i-CONFIRM-
unconditional analogy in §4's rejection of alternative (b) with a
rationale resting solely on the OLS-inequality proof (which is genuinely
sound and sufficient on its own) — or explicitly correct the description
to state item_i's CONFIRM never reaches the fit machinery at all, rather
than characterizing it as a smoothness-gate precedent it doesn't
actually set.
