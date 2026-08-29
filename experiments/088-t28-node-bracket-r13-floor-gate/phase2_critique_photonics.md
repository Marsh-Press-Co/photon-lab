# PHASE 2 — CRITIQUE · PHOTONICS · exp-088

## Steel-man

The bracketing design is genuinely diagnostic, not decorative: sampling the
two established-grid neighbors immediately flanking the known `θ₀≈38.590°`
zero-crossing, with the pipeline unmodified, directly targets the
artifact-vs-physics question R13 exists to resolve. Gating on
`frac_contrast(θ)` itself — the ratio's literal denominator, not a proxy —
is the most defensible reading of R13's text. I independently reproduced
every cited number from `experiments/083-.../results.json::per_theta`
exactly: RMS over the 31-point window `=1.91744×10⁻³`, `FLOOR=1.91744×10⁻⁴`,
and every margin (3.88×, 0.39×, 6.59×, 7.50×, 8.02×) — no R4 slip found.
Scoping out Item 2 (the 124-call full sweep) is a defensible cost/decisiveness
call, not a dodge. Q4's falsification structure (states what a "X" or "D"
reading would mean) is genuinely testable, not hedge-everything.

## Sharpest attack

I swept all 31 committed `frac_contrast(θ)` points myself and found
`delta_scene` crosses zero not once but **at least four times** in
[36°,42°] — interpolated zero-crossings at ≈37.13°, 38.590° (matches the
filed value exactly), ≈40.27°, ≈41.46° — spaced ≈1.20°–1.68° apart, i.e.
consistent with half the established ≈2.84–2.95° period. Two of these
*other* near-node points sit uncomfortably close to this cycle's own
FLOOR: θ=40.2° clears by only **1.48×**, θ=41.4° by only **1.31×** —
tighter margins than 38.4°/38.8° (7.50×/8.02×) have to the node they
bracket. The proposal frames 38.6° as "the node" and Q5's 5-angle picture
as "the first fully R13-compliant classification... across the node's
immediate neighborhood" — but the channel's own periodicity guarantees
comparable near-zero structure recurs roughly every 1.4° across the whole
swept window. This 8-call test resolves exactly one of at least four such
features and cannot license Q5's broader framing. Compounding this: Q4's
linear-trend prediction for `frac_p_abs` spans 5.8° (≈2 periods of this
same established oscillation) and is corroborated by exactly one interior
point (38.6°, 7.9% miss) — no argument is offered for why `frac_p_abs`,
unlike its sibling `frac_contrast`, should be smooth here (the closest
available physical warrant — Iteration 53's finding that the periodicity's
dominant driver is a scattered-field/`PAD` phase effect, not absorbed
power — is never invoked).

## Verdict

**Support-with-changes.**

## Parameter change that would flip toward unqualified support

Before Phase 4: disclose, alongside §4's margins table, that
`frac_contrast` clears its own floor by only 1.3–1.5× at θ≈40.2°/41.4°
(zero new FDTD, same 31-point window) — and narrow Q5's claim from "the
first fully R13-compliant classification... across the node's immediate
neighborhood" to "...at the sampled points" specifically, not the channel
generally. Without that scoping correction, a future reader could cite Q5
as having closed the node question for this window, when three more
comparably-tight near-zero angles remain wholly unexamined by this cycle.
