# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 82

*Reviewing candidate exp-105, "The T8 r=78/156/312 Bridge, Extended to the
Coherent Point/Region-Intensity Channel" (Lead: THERMODYNAMICS). Blind to
all other seats' current-cycle critiques.*

## Steel-man (≤150 words)

The proposal correctly reproduces T8's own founding mandatory fix
(`sigma_max(κ)=0.5/κ`, holding τ_shell=24.0 exactly at every κ) — I
re-ran both appendix scripts myself (geometry/cost and thermal sidecar)
and every printed table value reproduces bit-for-bit, satisfying R4
discipline directly rather than by inspection. Its §5 framing —
"self-similar r=156/312 constructions are LARGER absolute idealized
coatings, not more realizable ones" — states my own seat's Iteration-7
finding in the correct direction: absolute shell thickness scales
linearly with κ (48→96→192 cells), the OPPOSITE of how real CNT-black
coatings scale (fixed absolute thickness, independent of substrate size),
so growing r_out narrows nothing about the UNOBTANIUM gap. It also
correctly executes my own flagged exp-103 Phase-5 hypothesis, re-anchoring
the window to `R_COAT` instead of the physically-arbitrary `R_CLK=90` —
verified algebraically identical to the old window at r=78. The R4-family
cross-check (σ_max=0.25 at κ=2) independently reproduces against
`experiments/069-.../design_geometry.py`.

## Sharpest attack (≤150 words)

§6's thermal sidecar builds its entire `ΔT_ss(r)∝r_out` finding on
`σ_ext(r)=Q_ext·2·r_out`, i.e. `Q_ext` held scale-invariant. But the
anchor, `σ_ext(78)=240.0`, is exp-057's *own* committed record's
"w_on"/diffraction-inflated width — explicitly disclosed there as
`~1.54× the real geometric diameter, "ASSERTED, NOT INDEPENDENTLY
BOUNDED"` — a near-field artifact of the identical z/z_R-dependent
physics this whole bridge exists to characterize, on a family whose own
Iteration-7 founding run found even the *optical* channel it was fitted
to does NOT obey a clean power law (P-VISION-1b REFUTED for both
articles). Nothing argues a diffraction-inflated width should scale
linearly with r_out rather than shrink relatively as z/z_R shrinks. §5
correctly tags `graded_black_shell` UNOBTANIUM at every r; §6 never
restates that tag inline, so its "genuine finding" (margin declines,
classification holds) risks future citation as evidence about how a real,
differently-scaling coating behaves thermally — the exact R21
caveat-loss failure mode this program has already paid for twice.

## Verdict

**Support-with-changes.**

The core geometric/optical-depth-preserving methodology is sound, R4-
verified by direct re-execution, and correctly carries forward — rather
than distorts — the realizability bound this seat set at T8's founding
cycle (exp-030, Iteration 7): PEC published/trivial, sponges
published-but-trivial, `graded_black_shell` SPLIT — UNOBTANIUM as
self-similarly constructed, plausible only via the opposite (fixed-
absolute-thickness) scaling law real CNT-black coatings use. The
proposal's §5 sentence under review states this correctly and is not a
re-litigation of anything ruled out. What is missing is that §6's own
Q_ext-invariance assumption — the single number every predicted margin in
its table depends on — inherits an unresolved diffraction-inflation
caveat from its own cited source (exp-057) without saying so, and never
reconnects to §5's UNOBTANIUM tag inline, where a future citation would
actually read it.

## Flip condition

Add one sentence in §6, immediately before the numeric table, stating
explicitly: *this table characterizes only the self-similar UNOBTANIUM
construction of §5, under an unverified Q_ext-invariance assumption whose
anchor (σ_ext(78)=240.0) carries its own disclosed, unresolved
diffraction-inflation caveat (exp-057's own `diffraction_inflation_
caveat` field); no inference about a real, fixed-absolute-thickness
coating's thermal scaling is licensed.* With that sentence present (or
the table scoped explicitly provisional pending Phase-4's real
`sections.widths()` measurement, already planned in §7 item 3), this
verdict flips cleanly to support.
