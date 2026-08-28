# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 60 · exp-083

*Fresh sub-agent, blind to any other seat's current-cycle critique.*

## Steel-man (≤150 words)

Construction verified clean: `run.py::build_article` is `pec_disk(...,30)` +
`graded_black_shell(...,30,dg.R_OUT=78)`, byte-identical to `exp-024`'s
"stage-7 config verbatim" branch and to `exp-082`'s own `build_article` —
the flagship absorber, unchanged, not a new variant. The Branch-B
classification is decisively powered (`R²=0.858` exceeds the max of 20,000
null-permutation trials; EM's independent linear field-difference pair
corroborates the same family with its own clean null control), which
matters for MY charter specifically: whatever this confound turns out to
be, it is not a look-elsewhere artifact I'd have to discount before asking
what could realize it. And on the substantive question my Iteration-59 rule
addressed: **neither reading of Branch B implicates a material property.**
Article-rim diffraction is geometric-optics of a finite aperture — realizable
by any opaque disk of this electrical size, no ε(ω)/σ(I)/metamaterial
engineering required. My rule's core claim — no material is implicated —
survives, whichever causal story is correct.

## Sharpest attack (≤150 words)

"Article-edge diffraction" is a causal label pinned onto a period MATCH, not
independently verified as article-INTRINSIC. `P_edge_A=2.8421°` and
`P_edge_B=1.9608°` were both established in EARLIER, article-FREE studies —
`C80−C40` (differing `ABSORB` boundary depth, exp-069) and T21's own
source-taper fringe. This cycle never varied the article's own size; `R_OUT`
is fixed at 78 in every config, exactly as in exp-082. So the period match
cannot yet distinguish genuine article-rim diffraction (period should track
`R_OUT/λ`) from the SAME pre-existing, non-article domain/source artifact
merely becoming visible once a strong absorber sits in the object window
(period is article-size-independent). These have opposite realizability
readings: the first is trivially realizable by any macroscopic object
(materials-charter-trivial, published-tier); the second extends my own
Iteration-59 rule unchanged (zero realizability content, still a pure
scene-geometry fact). This cycle's own record cannot tell them apart —
nobody ran the discriminator.

## Verdict: **support-with-changes**

The construction-identity check and the branch classification itself both
hold up under independent re-derivation. Change requested: retire the bare
"article-edge diffraction" label until an article-radius discriminator has
run; until then, state explicitly that Branch B is a period-family match
consistent with, but not proven to require, genuine article-rim geometry.
My Iteration-59 "zero realizability content" framing rule should be
**extended, not reversed**, with this addendum: *if* Branch B is confirmed
article-intrinsic, it sits at the trivial end of my own published/plausible/
unobtainium scale (any macroscopic edge of comparable size produces it, no
special material) and is real-world-relevant rather than a pure simulation
artifact — but that "if" is currently untested, and until it is, the rule's
original scope (no material implicated, treat as scene/domain geometry)
should be read to cover this finding too, not silently superseded by a
label neither of this cycle's two instruments actually tested for.

## Single parameter change that would flip my verdict to full support

Re-run the identical `PAIR_PAD` (C40/G40) harness at one alternate article
radius (e.g. `R_OUT=50` or `100`, holding PAD and every other geometry
parameter fixed) and re-apply the same free-period fit to `delta_scene`. If
`P*` shifts with `R_OUT/λ` in the direction genuine rim diffraction
predicts, Branch B's causal label is earned and I'd support the write-up
as-is; if `P*` stays pinned near `2.84°`/`1.96°` regardless of article size,
that confirms the pre-existing domain/source-artifact reading and my
original rule needs no addendum at all — either outcome resolves the
ambiguity this cycle leaves open.
