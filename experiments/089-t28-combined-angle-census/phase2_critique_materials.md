# PHASE 2 — BLIND CRITIQUE · MATERIALS & METAMATERIALS · exp-089

## Steel-man (≤150 words)

A well-verified, cheap, correctly-scoped instrument extension. I independently
reproduced its load-bearing numbers rather than trusting the prose: `dg069.
DENSE_ANGLES[6]/[21]/[27]` = 37.2/40.2/41.4° exactly; `STEPS_SETTLED=2800`,
`CPL[600]=20` (⇒ `dx_m=30nm`) confirmed by import; `delta_scene(θ)`/`C40_C(θ)`
at all three new angles reproduce bit-for-bit from `experiments/083-.../
results.json`; recomputing `FLOOR_FRAC=0.10 × RMS[frac_contrast]` over the
full 31-point exp-083 window gives `1.91744×10⁻⁴`, matching the cited FLOOR
exactly — and all three margin ratios (2.17×/1.48×/1.31×) reproduce from
those primitives. The article, config pair, and wavelength are genuinely
unchanged (verified against the `run.py` chain), so reusing FLOOR verbatim is
legitimate under exp-088's own Idealization 13 rule, not a violation of it.
R13/R14 are both engaged with concrete, falsifiable, disclosed-low-confidence
bands rather than hedged prose.

## Sharpest attack (≤150 words)

Iteration 65's own CHECKPOINT (exp-088, this exact sub-thread, one cycle ago)
escalated the "carried idealizations" banner to **mandatory at both the
Predictions section and the Result section of any future T28 committed-
predictions document** — precisely because a disclaimer scoped to one section
silently failed to propagate to another, the *fourth* instance of a pattern
whose adoption text carries no discharge clause for further recurrences.
exp-089's own §6 Predictions section — a committed-before-Phase-4 document by
its own admission — carries no such banner. Concretely: MY seat's own
blocking Idealization 13 (FLOOR/RMS are `graded_black_shell`/600nm-specific)
is never restated here, even though FLOOR is reused verbatim and is
load-bearing for Q1 and for Q5, this cycle's own "sharpest test." Material/λ
being genuinely unchanged means this isn't yet outcome-determining — but it
is a live instance of the exact shape the checkpoint just escalated to
automatic firing.

## Verdict: support-with-changes

## Single change that would flip to support

Add an explicit "Carried idealizations" banner at the top of §6, naming by
number: idealization 2 (λ unchanged), the article-fixity claim in §2,
idealization 7 (`FLOOR_FRAC` house-style), idealization 8 (NETD, already
present), and a restated (or new) idealization giving exp-088's own
Idealization 13 verbatim — "FLOOR/RMS are specific to `graded_black_shell`/
600nm and must be independently recomputed, not reused numerically, for any
other absorber article or wavelength" — stating explicitly that it is
satisfied, not silently dropped, because this cycle changes neither. With
that banner in place at the Predictions section (and pre-committed to also
appear at the Result section per the CHECKPOINT's own mandate), this
proposal has no open items in my charter's lane.
