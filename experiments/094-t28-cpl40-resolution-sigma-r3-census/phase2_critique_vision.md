# Phase 2 Critique — VISION SCIENCE (blind, independent)

**Scope check (my charter only):** human perceptual limits, contrast/luminance
thresholds, spectral/temporal sensitivity, and the discipline of pinning
numeric thresholds *before* any run scores against them. I do not evaluate
FDTD mechanics, resolution methodology, or sequencing — those are other
seats' ground.

## Steel-man (149 words)

This proposal is disciplined about exactly the hazard my seat owns. A full
search of §4 (falsifiable predictions) finds zero occurrences of
"detectable," "undetectable," "visible," or "human eye" — no implicit
perceptual claim is smuggled in anywhere. Idealization 3 states plainly
"NETD ≠ human-eye threshold — N/A this cycle, no NETD backfill is run," T1
route and Realizability are both correctly N/A, and the mandatory carried-
idealizations banner appears at the Idealizations/Predictions boundary in
the same place, citing the same style of consolidated list, that exp-093's
own Phase-1 proposal used and that Iteration 70 closed without a criterion-4
firing. Rather than requiring a disclaimer to travel correctly alongside a
perceptual claim — the mechanism that has failed repeatedly on this exact
sub-thread — this document avoids the hazard by never making the claim in
the first place. Every §4 outcome carries a pre-committed numeric or
categorical band, not description dressed as prediction.

## Sharpest attack (147 words)

§2.2's reused-verbatim inventory lists `cell_metrics_full`, `pair_metrics_
full`, and `netd_row` alongside the plain `cell_metrics`/`pair_metrics` —
the exact "_full"/NETD machinery that surfaces `dt_ss_full_K`/
`netd_classification` per cell. Idealization 3 asserts "no NETD backfill is
run," and §2.3's new R4 functions explicitly mirror the plain (non-NETD)
`cell_metrics`, but nothing in §2.1 or §2.2 states whether Rank 2/Rank 3
(the R3-family items, which reuse the *existing* R3 layer unmodified) call
`pair_metrics` or `pair_metrics_full`. If the "_full" variant fires as a
byproduct of loading the whole prior module — plausible, since it's
imported either way — NETD/detectability-adjacent fields land in
`results.json` with no pre-committed disclaimer convention for how they'd
be reported. This is the identical "computed-but-never-reported" shape
Iteration 70's own Phase-5 THERMODYNAMICS self-review just caught in
exp-093's item 5b, one cycle ago on this same thread.

## Verdict: **support-with-changes**

The physics/instrument work is outside my charter to judge, and the
perceptual-claim hygiene here is genuinely good — better than several
recent T28 cycles. The one live risk is forward-looking, not a defect
already committed to git: pin, before Phase 3 freezes, whether Rank 2/3
invoke the NETD-surfacing "_full" functions, and if there is any chance
they do (even as an unused-but-computed byproduct), commit now to the exact
NETD-not-human-eye disclaimer that will accompany any such field if it
ever appears in `results.json` or a future NOTES.md Result section — rather
than leaving that determination for Phase 4/5 to discover after the fact.

## Single change that would flip me to unconditional support

Add one sentence to §2.1 (or §4) stating explicitly which cell/pair-metrics
variant (plain vs. "_full") Rank 2 and Rank 3 actually invoke, and, if
"_full" is used for any reason, the disclaimer that will govern any
NETD field it produces. That closes the ambiguity before Phase 4 runs,
consistent with my seat's standing duty to pin thresholds and their
scope before a run, not after.
