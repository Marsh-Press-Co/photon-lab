# PHASE 2 — CRITIQUE (ELECTROMAGNETISM) · Panel Iteration 27 · exp-050

## Steel-man (≤150 words)

The regression anchor and geometry table are the strongest parts of this
proposal. Every algebraic quantity — `A`, `R_EDGE`, the Y-domain length, the
nine fringe-period figures in §2.4 — is independently re-derivable from the
two already-committed geometry dicts (`GEOM_EXP042_OLD`, `GEOM78`) and checks
out exactly (the 752/724 = 1.038674 period-growth ratio reproduces to 6 sig
figs at every one of the 9 λ,θ cells I recomputed). The proposed
generalization of `beam_divergence_incoherent`/`coherent` is a literal,
verifiable transcription of `_G_for`'s already-committed formula onto
`_geom_derived`'s output — `D_SP` is unchanged between the two geometries, so
no new obliquity-range physics is being introduced, only re-evaluated on a
smaller `A`. The mandatory regression anchor (§2.3) is executable exactly as
stated, closing precisely the defect (an unexecutable regression gate) that
undermined exp-049's own P-NCONV26-0. Zero T1 exposure, zero mechanism claim.

## Sharpest attack (≤150 words)

§2.4's grounding for P-NCONV27-2 ("period grows monotonically ⇒ no cell needs
a *stricter* n\*") is a MAGNITUDE-only argument being used to predict an
ALIASING outcome, and this program's own T21 record (Iteration 18-19, this
seat's own finding) already shows that's the wrong axis: fringe-sampling
quality is governed by *proximity to the Nyquist-critical ratio*, not raw
period size — 600nm (period nearest 2°, the sampling grid) showed the
*cleanest* sign-alternation while 450/750nm (period *further* from Nyquist)
showed *messier, aliased* behavior. A uniform 3.87% period stretch does not
move every cell uniformly away from its own local near-integer aliasing
boundary — it can push individual cells closer to one even while the mean
period grows. P-NCONV27-2's binary falsification framing ("any cell moving to
a larger N_SERIES tier ⇒ the period-growth argument is wrong") therefore
risks mistaking an expected, isolated aliasing artifact — which this
program's own record predicts can occur even when the underlying mechanism is
intact — for a refutation of the whole directional claim.

## Verdict: support-with-changes

Two fixable gaps, one disclosure-only, one framing:

1. **Disclosure gap (cheap).** `beam_divergence_incoherent` and
   `beam_divergence_coherent` retain the obliquity-on-E convention exp-042's
   own module docstring (mandatory fix 1, Iteration 19) explicitly calls "the
   correct recipe for a boundary-value screen problem, **not this engine's
   source**" — i.e., not merely uncorrected, actively flagged wrong for
   `add_line_source`'s real line-current physics. §2.2 correctly labels it
   "original/committed" (not "corrected"), but nowhere restates *why* it was
   superseded. Calling the generalization "algebraically trivial" is true as
   a code-transcription claim (I verified the formula match against both
   `_G_for` and `_geom_derived`) but says nothing about whether the result is
   physically the right answer — and the proposal's own audience (future
   citations of GEOM78 numbers) is exactly the population this bench's
   Iteration-23 recurrence showed will not re-derive that history unprompted.
   A one-line caveat field in `results.json` plus a NOTES.md sentence closes
   this at zero cost.

2. **P-NCONV27-2's falsification framing is too rigid**, per the sharpest
   attack above. It should allow 1-2 isolated tier increases, attributed to
   near-Nyquist aliasing crossings, without declaring the period-growth
   argument itself wrong — only a systematic/majority pattern of increases
   should falsify it.

Neither gap is load-bearing to any constraint-3/4 claim or
`REALIZABILITY_MEMO.md` tier (none is at stake here); both are cheap,
same-shift fixes consistent with this program's own mandatory-fix-docket
convention.

## Parameter change that would flip to support

Amend P-NCONV27-2's hard-falsification band from "any combination moves to a
larger tier" to "more than 2 of 108 combinations move to a larger tier, **or**
any such move is not traceable to a near-Nyquist-boundary crossing at that
specific cell's own period/Δθ_sample ratio" — and add the one-sentence
obliquity-on-E provenance caveat to §2.2's table. Both are zero-FDTD,
zero-new-computation changes to the already-frozen prediction text.
