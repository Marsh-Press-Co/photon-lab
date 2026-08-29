# PHASE 2 — CRITIQUE (ELECTROMAGNETISM) · Panel Iteration 67 · exp-090

## Steel-man (≤150 words)

The three-layer design correctly quarantines a real hazard: with AUC=1.0 on
n=7, an unpenalized MLE has no interior optimum, so anchoring the primary
deliverable to an assumption-light order-statistic zone (computed, not
fit), and demoting Firth's finite point estimate to a corroborating
cross-check with an explicit non-blocking fallback (§7), is the correct
epistemic ordering — it cannot fail in a way that blocks the deliverable.
The exhaustive (not bootstrapped) LOO jackknife honestly reports how far
each zone edge moves rather than asserting false precision at n=7. Every
number in Table 1 — `frac_contrast`, `margin`, `ratio_k` for all seven
angles — I independently recomputed from `results.json::frac_contrast` in
exp-087/088/089 and it reproduces bit-for-bit, including `FLOOR=
1.91744×10⁻⁴` from exp-083's own 31-point RMS. The refusal to add
`frac_p_abs` or raw θ as a second regressor is correctly reasoned and
independently checkable from the ratio's own algebra, not asserted.

## Sharpest attack (≤150 words)

The exact permutation test's null is not exchangeable with the actual
generative mechanism, so `p=1/21` is largely a restatement of an
already-known fact, not fresh evidence. `Y=1` is a deterministic
decade-threshold on `ratio_k=frac_p_abs/frac_contrast`, and `margin` IS
`frac_contrast` (rescaled) — one of the ratio's own two terms, not an
independent covariate. Rearranging: `Y=1 ⟺ margin < frac_p_abs/(10·FLOOR)`.
I computed this implied per-angle threshold from `results.json` at all 7
points: it spans 0.680 (38.4°) to 3.772 (41.4°) — a 5.55× range,
comparable to `margin`'s own 6.12× range (1.31–8.02) — and confirmed the
inequality holds exactly at every point. Given exp-089's own five-way
decomposition already established the classification is ~90%
denominator-driven at the X points, "permute `Y` across fixed margins"
imagines a counterfactual where nature reshuffles labels independently of
the very quantity (`frac_contrast`) that mechanically sets them — the
same "regressor and label aren't actually exchangeable" failure shape R10
was adopted to catch, applied here to a label-permutation null instead of
a circular-shift one. The p-value measures how orderly R13's own algebra
is, not how surprising a genuine floor-gate inadequacy is.

## Verdict

**support-with-changes**

## Parameter change that would flip verdict

Replace or supplement the label-permutation null (§Method component 2)
with a null built from each point's own already-recorded measurement
uncertainty (`box_dev` on `frac_p_abs`/`frac_contrast`, propagated
through the `ratio_k`/`RATIO_HIGH` decision rule) — testing whether the
observed rank-concordance is still near-certain once the already-
established ~90%-denominator-dominance mechanism is taken as given, or
requires something beyond it. Absent that, P2's language should be
downgraded from "certify the separation is not a 7-point coincidence" to
purely descriptive (the caution zone, P3, does not depend on P2 and is
unaffected either way).
