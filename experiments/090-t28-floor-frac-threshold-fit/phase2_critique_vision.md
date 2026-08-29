# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 67 · exp-090

## Independent verification performed before writing this critique

I recomputed the full n=7 Table 1 from the cited primitives myself,
independently of the proposal's own arithmetic, before trusting any of
it (R4/R9 discipline): `FLOOR = 0.10 × 1.91744×10⁻⁴`'s own components
from `experiments/089-.../results.json::r13_floor_gate`
(`rms_frac_contrast=0.0019174375118374476`, `floor=1.91744×10⁻⁴`,
bit-exact to the proposal), then divided each of the 7 `frac_contrast`
values pulled directly from `experiments/088/results.json` (36.0°,
38.4°, 38.8°, 41.8° — including the `retroactive_exp087_reclassification`
block) and `experiments/089/results.json` (37.2°, 40.2°, 41.4°). All
seven margins reproduce bit-for-bit: 3.8793 / 2.1709 / 7.4946 / 8.0187 /
1.4764 / 1.3095 / 6.5889, and the rank separation (both X-margins below
both flanking C-margins, no ties) holds exactly as claimed. The
"perfect rank separation" premise this entire method rests on is real,
not a transcription artifact — I confirm it independently rather than
taking the proposal's word for it.

## Steel-man (≤150 words)

This is exactly the caution-zone deliverable Red Team asked for at
Iteration 66, built honestly around a real statistical hazard (the
degenerate-MLE problem on perfectly-separated small-n data) rather than
glossing past it. The three-layer design — a parameter-free order
statistic as the primary deliverable, an exact (not simulated)
permutation test sized correctly for n=7, and Firth's bias-reduced
regression as a corroborating check rather than the headline — is the
right shape for this sample size, and every falsifiable prediction is
frozen against numbers that are, as I independently confirmed, already
committed and exact (zero new FDTD risk). The regressor-choice
discussion (§5) correctly re-applies R13/R14's own logic to explain why
`frac_p_abs` cannot be added without circularity. This is careful,
well-scoped instrument-calibration work.

## Sharpest attack (≤150 words)

The mandatory dual-section carried-idealizations banner — installed as
this exact sub-thread's own structural remedy at the Iteration-65
CHECKPOINT, specifically *because* a banner scoped to one section does
not propagate to another — is missing from this proposal's own
Predictions section. §3 states the constraint-1/2/3/4/NETD disclaimer
once; §6 Idealization 7 restates it once, at the very end. But §4
("Falsifiable predicted outcomes," this document's actual Predictions
section, the place a future citation will quote) never mentions
Idealizations 9/10, constraint-3, or NETD anywhere across P1–P6 — unlike
exp-089's own Predictions section one cycle ago, which cited "(NETD/
constraint-3 disclaimers apply, Idealizations 9-10)" inline, per-item.
`FLOOR`/`RMS` specificity (Idealization 16) *is* carried inline (the
parameter table's "Reuse convention" row, §5, §6 item 3) — only the
constraint-3/NETD half of the banner erodes, the identical asymmetric-
carry shape that fired Checkpoint 4 a fourth time one cycle ago. This
sits inside the exact document type (a T28 committed-predictions
document) the rule was written for.

## Verdict: **support-with-changes**

The method itself is sound and independently verified; the defect is a
cheap, mechanical omission, not a substantive flaw, and this cycle
makes no new NETD/constraint-3 measurement to misreport. But per the
Iteration-65 ruling's own text ("required at BOTH the Predictions
section AND the Result section of any future T28 committed-predictions
document"), this is not discretionary, and Phase 3 should not proceed
to freeze predictions without fixing it — a proposal that is Phase-2-
critiqued for the omission and ships to Phase 3 unfixed is squarely the
"known, named, ignored" shape that escalates a prior rule's non-firing
instance into a firing one on re-occurrence.

## Parameter change that would flip my verdict to plain support

Add, at the top of §4, an explicit one-line carried-idealizations
banner citing Idealizations 7/8/9 (NETD-not-human-eye,
constraint-1/2/3/4-not-tested, FLOOR/RMS material-and-wavelength
specificity) exactly as exp-089's Predictions section does, and cite it
parenthetically within at least P3–P6 (the predictions someone would
actually quote out of context) rather than only in §3 and §6.
