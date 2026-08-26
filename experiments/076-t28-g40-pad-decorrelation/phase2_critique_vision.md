# Phase 2 Critique — VISION SCIENCE

**Panel Iteration 53. Seat: VISION SCIENCE (blind, fresh context).** Note on
scope: this cycle is a pure T28 instrument build (constraint-3 not engaged,
§3); my charter's duty to pin numeric perceptual thresholds "before any run
that scores against them" therefore applies here mainly as a *boundary*
check — does this instrument stay out of perceptual-scoring territory, and
does it correctly inherit my own prior cycle's (Iteration 42, exp-065)
settling-time findings for the geometry family it reuses.

## Steel-man (147 words)

This proposal's cleanest virtue, from my charter, is discipline about what
it is *not*. §3 explicitly disclaims constraint-3 engagement; §4's closing
line states none of (a)/(b)/(c) is a "RESOLVED/CONFIRMED-class significance
claim"; `C_thr`, `GATE_HARD`, "photopic," and "contrast" never appear in the
document (verified by grep — zero matches). That is exactly correct:
`amp_ratio` and `delta_P_obs` are fit-conditioning statistics on `C_empty`
deltas — a dimensionless field ratio, per exp-072's own Idealization 8
("`C_empty` is a dimensionless field ratio, not a Michelson/Weber perceptual
contrast... never photometric," a finding VISION SCIENCE itself forced into
exp-072's record at Phase 5) — and this cycle never scores them as if they
were perceptual. It also confines the new `G40` legs to the 36°–42° dense
window, avoiding `FALLBACK_ANGLES`/±35°, the angle set my own Iteration-42
cycle showed sign-flips under settling correction. Staying this quiet about
perceptual claims when it has none to make is my charter's job done
correctly, by omission.

## Sharpest attack (150 words)

The `STEPS=2800` "established settled floor for this channel" claim (§2b)
does not cover `G40`'s own geometry, and I verified this against source, not
prose. Every T27 settling re-check landed on: `C40` unpadded (exp-066, `grep
CONFIGS` → `CFG = dg065.CONFIGS["C40"]` only, 18 cells) and `C40`+`C80`
(exp-068, `grep` confirms `CONFIGS = {"C40":..., "C80":...}` only — "both
padding configs" means PAD∈{0,40} with ABSORB=PAD+40 in lockstep). `G40`
appears in FDTD exactly once anywhere in this repo — exp-065's Block PAD, at
`STEPS=1400` — and never at 2800 (confirmed: `grep -rl G40` across
experiments 066/068/069 hits only a pass-through `CONFIGS` reference in
exp-069, never executed there). `G40` decouples domain size (matches C80,
the point where the settling shift shrank to 59.8%) from band thickness
(matches C40's thin 40-cell band, the point with the *largest* shift,
74.4%) — exactly the untested corner. §5 idealization 4 discloses `G40` is
"genuinely fresh" but never flags this specific settling-transfer risk, and
no `G40`-specific 1400-vs-2800 differential (a P-VIS42-11-style check) runs
before Phase 4 trusts `STEPS=2800` against the pre-registered §4 bands.

## Secondary finding, same charter (not the sharpest attack, flagged for completeness)

`amp`, the Cbar carrier amplitude `amp_ratio` is normalized by, is itself an
averaged `C_empty` reading — I recomputed it directly from
`experiments/072-.../results.json` (`amp = 0.0052760/0.0057246/0.0057029/
0.0052452` for the four baseline pairs) and it sits almost exactly at
VISION's own lab bar `C_thr = 0.005`. That is a coincidence of what
`C_empty` happens to measure at this geometry, not evidence `amp_ratio` is
a contrast — but exp-072's Idealization 8 exists precisely to block that
reading, and this proposal's own idealizations list (§5, items 1–7) does not
carry an equivalent disclaimer forward for `amp_ratio`/`delta_P_obs`, despite
§2c reusing exp-072's machinery "identically." Given the magnitude
coincidence, a future reader skimming `amp_ratio(PAIR_ABSORB40) ≥ 0.116`
language without reading run.py could plausibly misread it as a
contrast-scale statement. Cheap fix, not gating: add a ninth idealization
line restating exp-072's Idealization 8 for this cycle's own readouts.

## Verdict: **support-with-changes**

The instrument design, R6/`G0-e` discipline, and pre-registered bands are
sound, and the proposal is unusually careful about NOT smuggling a
perceptual claim into an instrument cycle. But it inherits my own
Iteration-42 settling-time finding by citation ("T27's own established
settled floor") rather than by verification at the one geometry — `G40` —
that combines a domain size and a boundary thickness never jointly tested
for settling before. That is the same failure shape T27 itself was opened
to correct (a settling standard established on one geometry silently
assumed portable to an adjacent one).

**Single parameter change that would flip this to full support**: add one
`G40`-specific settling differential before Phase 4 scores §4's bands —
`|C_empty(G40, θ=39°, 600nm, STEPS=2800) − C_empty(G40, θ=39°, 600nm,
STEPS=1400)|`, relative, scored against T27's own established REFUTE bar
(>1% relative ⇒ settling is a live confound requiring disclosure, matching
P-VIS42-11's own bar exactly). One extra FDTD call. If it REFUTEs, §4's
bands should be reported bounded by that uncertainty, not read as clean.
