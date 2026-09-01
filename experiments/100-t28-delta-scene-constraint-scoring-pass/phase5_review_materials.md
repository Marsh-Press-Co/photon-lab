# Phase 5 Review — MATERIALS & METAMATERIALS

## Verdict: CONCUR-WITH-GAP(S)

## 1. Numbers independently re-verified

Read directly from `results.json`, not from NOTES.md/`disposition_memo.md`'s
prose:

- `tier1_item1`: `n_rows=75`, `n_by_family={"cpl20-native":3,"R3":33,
  "R4":35,"R5":4}`, `r_pooled=0.20650703941944507`, `p_pooled=0.0758`,
  `coupling_detected=false`; `by_family`: **R3** `n=33, r=0.4862068708642141,
  p=0.00415, coupling_detected=true`; **R4** `n=35, r=0.1102867253871392,
  p=0.5249, coupling_detected=false`; **R5** `n=4, r=0.9010050941024483,
  p=0.1644, coupling_detected=false`; `family_contradiction=true`;
  `outcome="ambiguous"`. All match NOTES.md's Result section and
  `disposition_memo.md` exactly, to full stored precision.
- `tier1_item2`: `{"branch":"ambiguous"}` — matches.
- `t1_label`: `"N/A, unresolved -- Tier 1's pooled/family-stratified results
  contradict each other (Idealization 70)..."` — matches NOTES.md's stated
  T1-label exactly.
- `run.py`'s `tier1_item1()`/`pearson_r()`/`permutation_test()` implement the
  joint rule (`p<0.05 AND |r|>=0.2`) and the family split exactly as
  described; `POOL_TABLE` sources each family tag from the *originating*
  file's own family-defining constant (documented inline, e.g.
  `cell_metrics_r4`→R4, `PAIR_KEYS_R5`→R5), not guessed from the pooled
  JSON — satisfying R4/R20 discipline. No arithmetic or provenance defect
  found.

## 2. Did fix 6 resolve the category error?

**Procedurally, yes — genuinely, not merely on paper.** My Phase-2 critique
found Tier-1 item 2 as originally scoped ("formalize the split already
drafted") could only ever produce a fourth restatement of the Iteration
59/60 ambiguity, because neither of `delta_scene`'s two candidate identities
(PAD/domain artifact, or diffraction off the already-published
`graded_black_shell` rim) opens a genuine published/plausible/unobtainium
question for a *new* structure — my charter's tier system does not attach to
either pole. The rescoped per-outcome conditional (fix 6) turned that into a
falsifiable structure, and this cycle is the first real test of it: the
pooled and family-stratified results genuinely disagreed, and the
pre-registered rule (Idealization 70) routed the outcome to branch (iii)
without any post-hoc discretion. Learned #3 is correct that this is the
clearest evidence the RT-3 mechanism (pre-committing the T1 label before the
run) works on real, not merely hypothetical, data. That part of my Phase-2
finding is closed.

**But the branch (iii) text itself under-uses a directly on-point piece of
this program's own house history that is MATERIALS' own province, and that
is the gap.** `disposition_memo.md`'s branch (iii) reasoning — "a real
cross-term should recur across families (R15's own addendum discipline); a
family-specific-only signal is evidence for a family-specific recipe
artifact, not genuine coupling" — cites R15 only in its most generic form.
It does not connect this specific split to the *specific*, already-adopted
R15 addendum (Iteration 71, exp-094, itself a MATERIALS finding,
independently reproduced by PHOTONICS/QUANTUM/Red Team) that this exact
resolution pair — **R3 (`cpl=30`) vs. R4 (`cpl=40`)**, on this exact
`delta_scene` signal — is already on record as capable of a *full-window
sign/classification reversal that is indistinguishable, from pointwise data
alone, from a systematic registration/phase-reference defect in the newer
family's own construction*, and that such a reversal must specifically
**not** be resolved by defaulting to the finer grid (R4) as automatically
correct. exp-100's own split — significant coupling at R3 (`n=33,
r=0.486`), null at R4 (`n=35, r=0.110`, despite *more* rows, not fewer) — is
not a fresh, unprecedented ambiguity; it is a named instance of a failure
mode this sub-thread already has a rule for, and that rule already
specifies the remedy: a **third, differently-ratioed resolution point**
(R5, `cpl=50` — literally what exp-099 built as "the third point," per its
own directory name) is required before either the R3 or the R4 reading can
be trusted, and that third point must first reproduce a known-robust,
far-from-null sign on the same channel (a ground-truth-recovery check)
before its own near-null reading is trusted. R5's current `n=4` in this
pool is nowhere close to serving that role — it is a small bracket
construction (exp-099's own Richardson-style step-3 report), not a survey
at anything like R3/R4's ~33–35-point density across the same 36°–43°
window, so it cannot yet distinguish "R3-specific artifact" from "R4-specific
artifact" from "genuine coupling numerically fragile near a null." The
memo's own framing ("family-specific-only signal is evidence for a
family-specific recipe artifact") is directionally reasonable but
overstates the confidence a bare disagreement licenses — R15's addendum
explicitly rejects the symmetric-looking alternative reading, too ("neither
resolution's reading is individually trustworthy" is the actual standard,
not "R3 is probably the artifact").

**Also missing, and worth stating explicitly for future cycles**: under
*none* of item 2's three branches does a genuine new realizability question
ever open. Branch (i) is "no tier applies." Branch (ii) — even in the
strongest possible confirmed-coupling case — is "published, no new material
required," because `delta_scene`'s own periodicity is either an inherited
domain artifact or diffraction off the *already-built, already-measured*
`graded_black_shell` geometry (PEC core, quintic-smoothstep graded
absorptive coat — a structure this program has fabricated in simulation and
characterized since early iterations, σ_abs/σ_ext=0.51 at the established
r_out, LOGBOOK ESTABLISHED). There is no reading of `delta_scene`, confirmed
or not, that proposes a *new* structure for MATERIALS to bound as
plausible or unobtainium. The conditional's ceiling was always "published,"
never higher. This should be stated once, plainly, in the memo, so a future
cycle that eventually resolves the R3/R4/R5 contradiction does not misread
"coupling confirmed" as reopening a live new-material realizability
question — it would only ever re-attribute an already-published structure's
own diffraction, not certify a new one.

## 3. Is "disposition deferred" the right call?

**Yes, as a matter of not overclaiming — but it should have been "disposition
deferred, for a specific, already-diagnosed reason, with an already-specified
remedy," not a generic deferral.** The honest, zero-content-invented answer
this cycle is entitled to is exactly what fix 6 produced: no realizability
claim, because the evidence genuinely disagrees with itself. Where I dispute
the framing (not the verdict) is that "deferred" reads as if this were a
fresh, structurally unexplained puzzle, when this program's own R15 addendum
already explains *why* a two-resolution-family split like this one is
inherently untrustworthy in either direction, and already prescribes the
specific next diagnostic (a third, differently-ratioed, properly-powered
point with a ground-truth-recovery precondition) rather than "more data of
whichever kind is convenient." NOTES.md's own §Next queue proposes "a fresh,
small R3-family spend at a few more angles, to see if the R3-specific signal
replicates" — this is not the diagnostic R15's addendum calls for. More R3
points can only confirm what R3 already reads; per the addendum, that alone
cannot distinguish a real, family-independent effect from a
recipe-level artifact specific to the R3 construction, because R15's own
founding and addendum instances show the failure mode lives in
*comparisons between* resolution families, not in additional density within
one. The correctly-targeted next step is a properly-powered R5 build, not a
bigger R3 build.

## 4. Ranked top-3 candidate directions for Iteration 78

1. **A properly-powered R5 (`cpl=50`) census at R3/R4 density (~30+ points)
   across the same 36°–43° window, gated by R15's own addendum
   ground-truth-recovery precondition** (first reproduce a known-robust,
   far-from-null `delta_scene` sign on the R5 channel, before trusting any
   near-null R5 reading) **— the specifically-indicated diagnostic for this
   cycle's own family contradiction**, not the "more R3 data" direction
   currently queued. This is the only path that can actually promote item
   2 off branch (iii) with real confidence, in either direction, and it is
   this sub-thread's own established remedy for exactly this failure shape,
   not a fresh proposal.
2. **The Tier-0 `beam_behind_t28` window-centering fix** (NOTES.md's own
   top queue item): constraint-1 is currently UNINTERPRETABLE on all 6
   angles due to a diagnosed, quantified lateral-shift miscentering, not a
   physics finding. This blocks any future MATERIALS reading of whether
   `delta_scene`'s magnitude poses genuine beam-termination risk once
   Tier-1 item 1 is eventually resolved, and it is cheap (a post-processing
   correction on already-spent captures, per the cycle's own Next section).
3. **A one-line, zero-FDTD addition to `disposition_memo.md`/Idealization
   70 stating the fixed ceiling explicitly**: no branch of MATERIALS' own
   per-outcome conditional can ever produce anything above "published" —
   confirmed coupling re-attributes an already-realized structure's
   diffraction, it does not certify a new one. Costs nothing, forecloses a
   plausible future misreading of a coupling-confirmed result as reopening
   a live plausible/unobtainium question, and keeps this cycle's own
   genuine contribution (fix 6 actually working, on real data) from being
   undersold by a still-generic deferral statement.

## Discipline note

Nothing in this review re-proposes a ruled-out idea. R15 (adopted Iteration
68) and its Iteration-71 addendum are cited as already-adopted house
discipline, not new rules; no new mechanism, structure, or realizability
tier is proposed here.
