# PHASE 2 — QUANTUM OPTICS CRITIQUE · Panel Iteration 63 · exp-086

*Fresh context. This cycle is instrument-repair/statistics work, not a
mechanism proposal — per this seat's T28-desk-cycle precedent (exp-085
Phase 5), critique focuses on statistical-significance soundness: the
overlap-corrected Spearman test this proposal builds to fix the exact
defect this seat found and confirmed at exp-085 Phase 5 (§1.8/§1.9 of
`phase5_redteam_audit.md`).*

## Independent re-derivation (grounding, not restatement — R4 discipline)

Loaded `experiments/085-.../derivation_results.json::method_c.sub_results`
directly (37 rows) and recomputed, from the raw `p_local_corrected`/
`r2_local`/`p_local_reported_at_39` fields, not from any prose:

- **Recovered-set arithmetic confirmed independently.** Applying the
  proposal's own criterion (`converged==True` ∧ `p_local_corrected≤6.0°` ∧
  `r2_local≥0.30`) to the 37 rows gives exactly **21/37=0.568** (r² never
  binds; the sole difference from the audit's naive 22/37 is `θc=45°`,
  correctly excluded here as an all-stage boundary pin whose corrected
  period happens to fall under 6° by coincidence) — the proposal's own
  §4-1 arithmetic reproduces exactly.
- **The stride-3 non-overlap claim is arithmetically correct.** Sub-windows
  are 6°-wide at a 2° center step; stride-3 in index units = 6° center
  separation = window width, i.e. edge-touching, zero overlap — confirmed
  by direct construction, matching the audit's own §1.8 `n=13` figure
  exactly (θc=5°,11°,…,77°).
- **The critical gap: stride-3 admits THREE valid phase offsets
  (θc starting at 5°, 7°, or 9°), and the proposal names none of them.**
  Restricting each phase's ~12–13 points to the recovered-only set and
  recomputing Spearman directly from the committed JSON:

  | Phase (start θc) | Recovered n | ρ | p (t-approx) | p (exact permutation) |
  |---|---|---|---|---|
  | 5° | 7 | **0.857** | 0.014 | **0.024** |
  | 7° | 7 | 0.429 | 0.337 | — |
  | 9° | 7 | 0.536 | 0.215 | — |

  Phase-5° — the SAME alignment the cited audit §1.8 uses, and the one a
  literal `array[::3]` slice of the θc-ordered array produces by
  default — clears **both** of the proposal's own falsification
  thresholds (`|ρ|>0.75` AND `p<0.05`, exact-permutation-confirmed at
  n=7, hand-verified: `Σd²=8 ⇒ ρ=1−6·8/(7·48)=0.8571`). The other two
  phases support the proposal's prediction. **The choice of phase is
  outcome-determining and is not pre-registered.**
- **n at the recovered-only, non-overlapping resolution is a hard 7**, not
  the proposal's stated "roughly 7–9" — all three phases give exactly 7,
  independently confirmed; the band is not wrong in direction but is
  looser than the data supports.

## Steel-man (≤150 words)

The R11 fix itself is precise and minimal: scoped exactly to the
post-loop fallback (the search/`at_boundary` logic untouched), and its
"recovered" criterion is a genuine improvement over the audit's own crude
`>6°` proxy — it correctly catches `θc=45°`'s boundary-pinned-but-
coincidentally-short-period case, a subtlety this seat's own
re-derivation confirms the naive filter misses. The stride-3
non-overlap construction is arithmetically exact (6°=window width,
independently reproduced) and reuses this seat's own audit-verified §1.8
method rather than inventing an untested statistic. Framing the predicted
null as "not decisively refuting" rather than "closing" the near-normal
periodicity question is properly hedged, falsifiable, pre-registered
before any code exists — the right discipline for a permanent-record
significance claim, matching R6/R10's own standard.

## Sharpest attack (≤150 words)

The overlap fix trades one significance defect for a hidden one. Stride-3
non-overlap admits three equally valid phase offsets (θc=5°/7°/9°) over
the same domain; restricted to the recovered-only set, they give
qualitatively opposite answers — ρ=0.857 (exact-permutation p=0.024,
clearing the proposal's own `|ρ|>0.75`+`p<0.05` falsification band) at
phase 5°, versus ρ=0.43/p=0.34 and ρ=0.54/p=0.22 at the other two, all
independently recomputed from the committed JSON, not asserted. Phase 5°
is not a fringe case — it is the SAME alignment the cited audit §1.8
uses and what a default `array[::3]` slice produces. An unstated,
outcome-determining researcher degree of freedom is exactly the R5
look-elsewhere shape this program already has a standing rule against —
now hiding inside the fix built to correct a related significance
overstatement.

## Verdict: **support-with-changes**

## Flip-to-support change

Pre-register and report **all three** stride-phase alignments (or adopt
the audit's own alternative, an explicit phase-invariant block/
effective-N correction — offered but not used) and require the headline
"not independently significant" claim to hold across all of them, not
one arbitrarily-selected phase, before it is cited as a T28 permanent
record.
