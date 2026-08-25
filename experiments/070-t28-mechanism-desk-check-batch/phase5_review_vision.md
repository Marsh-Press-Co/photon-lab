# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 47 · exp-070

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md seat 6). Blind to any
other seat's Phase-5 review this cycle. This batch contains no perceptual-
threshold question (T1 route N/A, Checkpoint-2 declined throughout), so
this review applies the seat's secondary, track-record strength named in
this cycle's brief: PROCESS-INTEGRITY scrutiny — specifically, auditing
whether my own Phase-2 finding (the gray-zone/HARKing gap, independently
ranked by Red Team "this cycle's single highest-priority fix") was closed
in substance, not merely in appearance, by Phase 3/4.*

## 0. What I verified directly, and how

- Re-ran `python3 desk_check_mechanism.py` from a clean checkout of
  `results.json` (backed up first). **Output is bit-identical to the
  committed `results.json`** — the deterministic-seed claim in
  `phase4_results.md` ("re-running reproduces every number bit-for-bit")
  holds.
- Read `desk_check_mechanism.py` and `design_geometry.py` line-by-line
  against the Phase-2 Red Team audit's 10-item docket and Phase-3's
  "what changed" table. Every docket item traces to a specific function:
  `item_a_per_config_decomposition` scores the recovered period (fix 1,
  Attack 1); `null_percentile`/`closest_matches` implement the
  `N=20,000`, `T~Uniform(100,1600)` permutation control with full tie
  reporting (fixes 2/3, Attacks 2/3/4); every `*_confirms`/`*_refutes`
  pair leaves an explicit residual `neither` (fix 4, Attack 5); the
  module docstring maps all ten items to their implementation (fix 8).
  No gap between the audit's ruling and the shipped code.
- Grepped every sentence in `NOTES.md` and `phase4_results.md` that
  cites `A_alt`, `A_eff`, `233`/`234`, `519`/`518`, or `0.7663`/`0.7666`
  (the two numbers a soft-CONFIRM narration would most likely lean on).

## 1. Primary check: is the gray-zone catch-all real, and is it honestly exercised?

**Yes, cleanly, on both counts.**

`results.json` shows `p_070_2_beat_frequency.neither = true` and
`p_070_4_aeff.neither = true`, produced by code, not narrated into
existence — I reproduced this myself. Both are driven by `null_p` values
(0.2039 and 0.8055 for the two P-070-2 branches; 0.4969 for P-070-4) that
sit nowhere near the `p≤0.05` gate the Phase-2 audit specified, so the
`NEITHER` classification is not a boundary judgment call — it is not
close.

Every sentence discussing P-070-2/4's raw numbers keeps the `null_p`
context in the same sentence or the immediate next clause:

- NOTES.md: *"both beat-frequency branches find a sub-1% named-constant
  match (…), **but** neither clears the null-permutation gate (`p=0.806`,
  `p=0.204`…)"* — one sentence.
- NOTES.md: *"`A_eff=518.81` matches `519` … and the candidate's 750nm
  cross-validation R²=0.7663 clears the 0.70 bar, **but** `null_p=0.497`
  — statistically indistinguishable from a coin flip, decisively failing
  the null-controlled gate despite passing every raw-threshold
  component."* — one sentence.
- `phase4_results.md` P-070-4 section goes further, spending its own
  emphasis sentence ("**Every raw-threshold component of this prediction
  passes.**") specifically to pre-empt a reader skimming only the
  raw-threshold columns — then attaches the `null_p=0.497` verdict
  immediately after, in the same paragraph.

I found no sentence anywhere in either file where the sub-1% match or the
R²=0.7663 figure appears without its `null_p` in the same breath. This is
a materially stronger discipline than the minimum my Phase-2 critique
asked for (I asked for a "does not count toward narrowing" rule; what
shipped also enforces same-sentence attachment everywhere the number
recurs, including in the search-space-provenance correction section,
which restates the `233`/`519` figures a second time without ever
dropping the caveat that null-context already governs their status).

## 2. "Learned"/"Next": does either section quietly over-credit a NEITHER?

**No overreach found.** `NOTES.md`'s "Learned" §2 ("the named-constant
search has essentially zero power to discriminate… the single clearest
demonstration in this program's own history that [the look-elsewhere
worry] was not theoretical") is a claim about *methodology* — the search
architecture's discriminating power — not a claim about T28's mechanism.
It does not smuggle the null result in as informative about the physical
question; if anything it states the opposite (the search told us nothing
about T28, and told us something true about the tool). "Learned" §1's
narrowing claim ("the class of viable [mechanisms] toward something
present in both configs' shared geometry") is correctly sourced to
**P-070-1's CONFIRM**, not to either NEITHER — a different, adjacent
prediction that did clear its own null-free gate (period recovered
independently in both configs). The two are kept properly separated.

## 3. Docket item 10: is queue-item-2 narrowing honestly scoped?

**Honored as written, not sidestepped.** Docket item 10's own text
explicitly permits narrowing by "item (a)'s corrected config-invariant
CONFIRM/REFUTE" in addition to a `p≤0.05` CONFIRM — so P-070-1 is a
licensed narrowing source by the docket's own rule, not an exception to
it. NOTES.md's "Next" section narrows *only* on P-070-1's CONFIRM and
states affirmatively that items (b)/(d)/(e) "contribute no surviving
candidate length scale to narrow a re-run's own target period toward" —
a correct, negative statement about the NEITHER items, not a positive
narrowing drawn from them. I checked for wording that might quietly use
P-070-2/4's raw closeness (0.08%, 0.04%) as a soft tiebreaker for *which*
FDTD re-run to prefer, and found none — the "Next" text's reasoning for
preferring EM's `C60`/`C70` test over PHOTONICS' re-run rests entirely on
P-070-1's ABSORB-disfavoring result, never on the retired named-constant
candidates.

## 4. Secondary finding — real, minor, not load-bearing (my own catch this cycle)

**Idealization 4's degenerate-constant disclosure is incomplete.** It
states only one numeric coincidence among the 14 `NAMED` constants
(`R_OUT=W_OBJ=78`). The committed `results.json` shows this undercounts
by a second cluster that is *already visible in the same document's own
NAMED-constant table*:

- `R_OUT=W_OBJ=W_FLANK=78` — a **three**-way tie, not two. This is not
  hypothetical: `phase4_results.md`'s own P-070-2 "plus"-branch row
  correctly lists the resulting 3-way tie (`R_OUT`/`W_FLANK`/`W_OBJ`
  interchangeable) — but that correction lives only in the Phase-4
  results table, never fed back to widen Idealization 4 itself.
- `TAPER=ABSORB40=PAD80=40` — an entirely separate, undisclosed
  three-way numeric coincidence. It is the direct arithmetic cause of
  three of the six ties in P-070-4's headline `519` match
  (`3·LEVER+6·ABSORB40`, `3·LEVER+6·PAD80`, `6·TAPER+3·LEVER` are one
  underlying coincidence, not three independent near-hits, since
  substituting any of `{TAPER, ABSORB40, PAD80}` for another leaves the
  expression's value unchanged by construction).
- A structural note, not a numeric coincidence: `aperture_cells=1504 =
  2·A`. Any single-term match against `aperture_cells` is algebraically
  reachable via `A` alone at double the coefficient — the two named
  constants are not independent dimensions of the search space, only of
  its bookkeeping.

None of this changes any CONFIRM/REFUTE/NEITHER verdict — the
null-permutation control marginalizes over the *entire* search space
(duplicates included) for both the real target and all 20,000 null
draws equally, so the `p`-values are unbiased by this. What it affects is
narrative color: a reader skimming "a six-way tie" or "a three-way tie"
in `phase4_results.md` without this context could read those numbers as
six (or three) independent corroborating near-misses, when three of the
six (and all three of the "3-way tie") are one coincidence counted
multiple times because of how this bench's own construction code reuses
the value 40 (and 78) across unrelated named quantities. This is exactly
the caveat-completeness failure shape this program's own LOGBOOK/PLAN.md
record has repeatedly flagged elsewhere (an idealization stated, but
incompletely) — here caught within the same cycle, before close, with no
downstream claim resting on it.

**Proposed fix (cheap, non-blocking):** widen Idealization 4 to name both
degenerate clusters (`{R_OUT, W_OBJ, W_FLANK}=78`; `{TAPER, ABSORB40,
PAD80}=40`) and the `aperture_cells=2·A` structural redundancy, and add
one clause to the P-070-2/4 tie tables in `phase4_results.md` noting that
some listed "N-way ties" collapse to fewer independent coincidences once
bookkeeping-constant degeneracy is accounted for. Two sentences, zero
code change, zero re-run required.

## 5. Checkpoint criterion 4 — does this cycle rise to the program's own bar?

**No, and it is a clean cycle, not merely a non-firing one.** Weighing
against the full CHECKPOINT history now on record (Iterations 37, 38,
39×2, 40, 45):

- Every prior firing this program's LOGBOOK/PLAN.md records shares one
  of two aggravating facts: a violated pre-committed tripwire (Iteration
  39's `candidate_globs` recurrence after a "no further deliberation"
  clause), or survival through most/all of a cycle's own five-phase
  process undetected (Iteration 37's docstring gap, Iteration 40's
  registry-scope gap found only at Phase 5, Iteration 44's sign-inverted
  formula surviving Phase 3/4/four-of-six Phase-5 reviews).
- This cycle's own gray-zone gap — the closest analog on record, since
  it is the identical failure shape to exp-069's own mandatory-fix-4 — was
  caught at **Phase 2** (my own blind critique, independently
  reconfirmed and *proven* rather than merely argued by Red Team's own
  executed code), fixed at **Phase 3**, before predictions were committed
  to git, and I have now independently verified at Phase 5 that the fix
  is real, correctly coded, and honestly narrated in every place it
  recurs. That is an earlier catch-point than the "found-before-close,
  fixed-same-shift" non-firing precedent this program has applied
  repeatedly (Iterations 19/23/38/42) — those were mostly Phase-5
  self-catches; this is a Phase-2 catch, closed before the house's own
  "predictions committed to git BEFORE the run" discipline even applied.
- My own secondary finding above (the degenerate-constant disclosure gap)
  is real but cosmetic: non-load-bearing, caught within the same review
  pass that also confirms the primary defect closed, changes no verdict.

Nothing in this record approaches criterion 4's own bar. This is, on the
process-integrity axis my seat is charged with this cycle, one of the
cleaner cycles in the program's history: a serious, independently-proven
Phase-2 finding (not a style nit — Red Team's own executed diagnostics
showed the *un*fixed design would have produced a false CONFIRM on item
(a) and a statistically powerless search on items b/d/e) was closed in
full, verified by direct re-execution rather than by trusting the prose,
and the resulting NEITHER verdicts are reported as NEITHER everywhere I
checked.

## Ranked top-3 candidate next directions

1. **PLAN.md queue item 2, EM's `C60`/`C70` `ABSORB`-varying falsification
   test** (already the Iteration-47 queue's own item 2, and now correctly
   the *only* unretired branch of it per NOTES.md's own "Next" section —
   P-070-1's CONFIRM positively disfavors nothing about the `ABSORB`-tied
   hypothesis being wrong, it disfavors it being the *only* explanation,
   so EM's direct manipulation of `ABSORB` while holding the
   config-invariant geometry fixed is the actual causal test this cycle's
   correlational desk work cannot substitute for). Reuses already-built
   congruent configs, zero new `lab/` diff — the cheapest real next FDTD
   step on record for T28.
2. **A geometry-breaking follow-up cell for the `R_OUT`≠`W_OBJ`≠`W_FLANK`
   degeneracy** (Idealization 4, this batch, now shown by my own Finding
   4 above to be a *three*-way degeneracy, not two) — a single new
   congruent-pair FDTD config where these three named quantities are
   pulled apart would let a future desk-check batch actually distinguish
   "object radius," "measurement-window half-width," and "flank
   clearance" as physically loaded candidates instead of leaving all
   three permanently indistinguishable by this bench's own construction.
   Not urgent, but cheap to fold into whichever future cycle next touches
   Block MINI's geometry.
3. **R_contact's `measured_direct` literature search** — unchanged from
   Iteration 46/45's own queue, still the only item on record that can
   move a real materials number (`REALIZABILITY_MEMO.md` Entry 3, TD-5's
   7.8× margin, UNANSWERED across five cycles now), orthogonal to items 1
   and 2 above (zero FDTD/rotation-slot competition), blocked only on
   WebSearch/WebFetch tooling availability.
