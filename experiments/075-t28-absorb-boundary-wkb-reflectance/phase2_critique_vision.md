# PHASE 2 — CRITIQUE · VISION SCIENCE · Panel Iteration 52 (exp-075)

*Fresh sub-agent, blind to the other five seats' critiques this cycle.*

**Charter note, stated plainly per this cycle's own framing:** T28 is
instrument-fidelity work — no absorber, no switch, no ambient scene, no
constraint-3 claim anywhere in this file. My charter (contrast thresholds,
luminance edge detection, spectral sensitivity, adaptation, temporal
sensitivity, saccadic/attentional blindness — "what would make a human eye
FAIL to register something physically present") has no direct purchase
here: there is no perceptual quantity to pin a threshold on. I have nothing
domain-specific to add on that axis. What follows is a rigor/internal-
consistency read instead, which every seat owes every proposal regardless
of specialty fit.

**R4 reproduction (independent):** ran
`python3 experiments/075-t28-absorb-boundary-wkb-reflectance/boundary_reflectance.py`
myself. Every cited number reproduces exactly: `rel_period_dev=4.2778`
(Test A REFUTE), `shape_r²=0.2586`, `pearson_r=-0.5085` (Test B
INCONCLUSIVE, wrong-signed), `combined_verdict=REFUTE`, all three gates
(G-LOSSLESS 2.2e-16, G-N1 1.4e-15, G-PASSIVITY worst |r|=0.0064) pass. The
[1b] exact-vs-linearized identity, the closed-form periods (7.78–11.82°),
and the ~5x amplitude shortfall all check out bit-for-bit against the
write-up. No hand-typed number found.

## Steel-man (≤150 words)

This is the cleanest T28 cycle in the six-plus this thread has run. The
physics is done honestly: a genuine sign ambiguity in the friction-PDE
bridge was resolved by an unambiguous physical requirement (passivity),
not by trying signs until the data looked better, and that correction is
disclosed in full rather than smoothed over. The choice to skip a
single-pass WKB/Born integral in favor of an exact recursive
transmission-line transform is correctly justified by the file's own
diagnostic (the band is only 2–4λ thick, adiabaticity marginal) — the
proposal doesn't force the WKB label the task invited just because it was
named first. Three zero-data sanity gates bound the machinery before any
number is trusted. The comparison against real data happens exactly once,
scored in code, and the result (REFUTE) is reported without softening —
including a mechanism the model's own construction predicts should be
five times bigger than what's observed. This is what "verify before
claim" looks like when the verification doesn't cooperate.

## Sharpest attack (≤150 words) — rigor/internal-consistency, not perceptual

The proposal never checks its own model against exp-074's most relevant
prior finding, despite the cycle's own queue language crediting that
finding as part of why this model was worth running. Iteration 51 found
the four `ABSORB` configs' own best-fit residuals are near-identical in
*shape* across depths (r=0.992–1.000) — evidence favoring a
depth-independent origin. This model's own §2d table gives `|r(θ;ABSORB)|`
falling ~40–70× from `ABSORB=40` to `ABSORB=80` — a mechanism that
predicts strongly depth-*dependent* echo strength. The proposal computes
exactly the numbers needed to state whether its own REFUTE is
reinforced or complicated by that prior finding, and never does the
arithmetic. (Caveat: Pearson r is scale-invariant, so exp-074's r=0.992
alone doesn't prove comparable *amplitude* — but that's exactly why this
model's own table should have been used to settle it, not left silent.)
Section 5's "narrowing, not closing" reading is honest but incomplete
without this check.

## Verdict: **support-with-changes**

The derivation, gates, and R4 discipline are sound; the REFUTE is real
and correctly scored against its own pre-registered bands. But two things
should be fixed before this enters the permanent record as this cycle's
closing word on the wall-echo class:

1. **Do the ABSORB-depth-scaling cross-check against exp-074's residual
   finding** (above) — either it sharpens REFUTE into a second,
   independent line of evidence, or it surfaces a tension worth flagging,
   but leaving it undone is a real gap in an otherwise careful document.
2. **Sharpen the pre-registration disclosure in §0/§5.** The claim "no
   falsifiable band below was chosen after seeing the comparison in §5" is
   true to the letter — but the closed-form period estimate (7.8–11.8°,
   known before the bands were written) already implies `rel_dev` ≈
   1.7–3.2, past the REFUTE line, before Test A's exact number existed.
   That doesn't look like gamed thresholds (30%/100% are the program's own
   ordinary round-number convention, not obviously reverse-fit to this
   result), and the disclosure itself is honest and matches house
   precedent (exp-070's "disclosed reconnaissance, not smuggled into the
   bands") — but Test A specifically was not a blind test in the way a
   reader skimming §0's framing would assume. Say that plainly rather
   than let the literal-but-narrow "not chosen after seeing §5" phrasing
   carry more than it should. Test B (shape) does look genuinely blind —
   nothing in the closed-form estimate predicts its sign or magnitude.

**What would flip this to outright SUPPORT:** run and report the
ABSORB-depth amplitude-scaling cross-check against exp-074's residual
finding (item 1 above) — a same-data, zero-FDTD addition to the existing
script, not a new derivation.

**What would flip this to OPPOSE:** evidence that the 30%/100% bands were
actually tuned after knowing the closed-form estimate's number, not just
its qualitative direction — nothing in the record suggests this, and I am
not making that claim, only naming what would.
