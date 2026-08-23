# Phase 5 — MATERIALS & METAMATERIALS blind review (exp-061 / Iteration 38)

*Fresh sub-agent (was Phase-1 lead; no memory of that carried into this
review), blind to the other five Phase-5 reviews and to Red Team.*

## Independent numeric re-derivation (3 conversions, all confirmed)

- **Black-matrix (MP-3 headline):** OD=3.0 → τ=3.0·ln10=6.9078 →
  α=6.9078/(1×10⁻⁴cm)=**6.908×10⁴ cm⁻¹**. Matches the document's
  6.91×10⁴ exactly.
- **300–500µm CNT forest, R=1–2%:** OD range 1.70–2.00 → τ 3.91–4.61;
  α = τ/thickness → **78–154 cm⁻¹**. Matches.
- **n_eff=1.04+0.01i:** α=4πk/λ, λ=550nm → 2.28×10³ cm⁻¹. Matches.
- **τ_true anchor**, independently recomputed: 2·(2π/20)·48·0.273840 =
  8.2588; α=5.735×10⁴ cm⁻¹; e-fold=174.4nm; OD=3.587. All confirmed.

No arithmetic defects found in phase4_results.md's conversions.

## The MP-4 mechanism-class exclusion — argued both ways

**For the exclusion:** the "graded near-ε=1 absorber" qualifier was
written into the falsification condition BEFORE any search ran
(Phase-2 mandatory fix 3), for an unrelated worry (coherence/
localization framing), and applying it now is mechanical, not
retrofitted. `graded_black_shell`'s charter-relevant property is a
genuinely radially-graded ε(r); a discrete-pigment Beer-Lambert film has
none. Matching aggregate (OD, thickness) numbers is not the same as
realizing the coded mechanism.

**Against it:** this exclusion is NOT symmetric with how the program
treats its accepted comparison class. CNT forests are themselves not a
literal continuous index gradient — MP-1's own caveats concede real CNT
blackness is "structural light-trapping/multiple scattering... not
homogeneous bulk absorption," i.e., a discrete-scatterer ensemble
treated as effective-medium-graded by convention. If a discrete-pigment
film is excluded for not being "index-graded," a discrete-tube-tip
forest should face the same scrutiny by the same literal standard — it
isn't. Compounding this: this same cycle ALSO excludes black
silicon/moth-eye (Idealization 4) for being "index-grading-dominant"
rather than conductive-loss-dominant — the OPPOSITE ground. One cycle
excludes a real candidate for being "not graded enough" and a different
real candidate for being "too graded" — and both exclusions happen to
preserve the predicted UNOBTANIUM-WITH-PARAMETERS tier. Each exclusion
is individually defensible on its own stated terms, but the pattern is
exactly the shape this program's own Iteration-26 standing rule warns
against.

**My call:** the exclusion stands — procedurally it follows a
pre-registered condition, not a post-hoc rationalization, and there's no
better bright line to offer. But it should ship as a FLAGGED, not clean,
exclusion, and the "not rate" framing in Next item 1 needs correcting:
rate is close to target ONLY for the excluded candidate. For the actual
in-class comparator (CNT-forest), rate is also a hard miss — best
in-class visible-band α (2.28×10³) is >25× below the 2× threshold;
nothing in-class is within an order of magnitude of target. "Thickness,
not rate" is true only if the excluded candidate is allowed to stand in
for the rate axis — which is the very move under dispute.

## Search-plan gap

The five ranked source classes (CNT-forest/Vantablack + one
index-grading cross-check) miss a real third family: **graded-porosity
ultra-black metal coatings** — electroless nickel-phosphorus black (NiP
black), a published aerospace/optical-baffle coating with a genuinely
graded, dendritic/columnar porous surface producing a continuous
air-to-bulk effective-index gradient (much closer in SPIRIT to
`graded_black_shell`'s coded ε(r) than either CNT-forest or the pigment
film), typically sub-micron to few-µm thick. None of the 15+3 queries
mention "nickel-phosphorus," "electroless black," or "black chrome."
**Carbon aerogel / graphene-aerogel absorbers** (density-graded,
genuinely index-graded by construction) are a second miss. Both should
be queried before this axis is called closed.

## Verdict: **PARTIAL**

The UNOBTANIUM-WITH-PARAMETERS tier itself is not overturned — no
numeric defect found that flips it. But this cycle's own flagged open
question (the mechanism-class judgment call, explicitly kicked to Phase
5) does not close as cleanly as MP-4/Next presents it: the exclusion is
defensible but asymmetric with a same-cycle exclusion running the
opposite direction, and the proposed memo language overstates how
settled the rate axis is.

## Defects found

- **[MEDIUM]** Next item 1's proposed `REALIZABILITY_MEMO.md` update
  ("driven by thickness, not rate") is an over-simplification — rate is
  only non-damning for the excluded candidate; for the true in-class
  comparator, rate independently misses by >18–25×. Fix before the memo
  update ships.
- **[MEDIUM]** No cross-check disclosure that this cycle's two
  mechanism-class exclusions (black-matrix film excluded as "not
  graded"; black-silicon/moth-eye excluded as "too graded") run in
  opposite directions yet both protect the predicted tier — should be
  named explicitly as a risk, not left implicit.
- **[LOW]** Search plan's five source classes miss NiP-black-class and
  aerogel-class absorbers — a real, nameable gap, not fully "exhaustive"
  as the query count implies.
- **[LOW]** `caveat_lint.py` — confirmed PASS independently,
  `5 caveat(s) checked, 0 required-site failure(s)`, exit 0.

## Top-3 candidate directions, Iteration 39

1. Run 4–6 targeted queries on NiP-black/electroless-nickel-black and
   graphene/carbon-aerogel (α, thickness) — closes the search-plan gap
   directly.
2. Add a caveat-lint registry entry for the mechanism-class-exclusion
   judgment call — including the asymmetry noted above, not just the
   exclusion's existence.
3. A primary-source-verified pin of the n_eff=1.04+0.01i figure — it's
   MP-1's single strongest in-band point and currently untraceable.
