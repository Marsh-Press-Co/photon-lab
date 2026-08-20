# PHASE 5 — REVIEW · VISION SCIENCE (fresh context, blind) · exp-049, Panel Iteration 26

*Charter: human perceptual limits — contrast thresholds, luminance edge
detection, spectral sensitivity, adaptation, temporal sensitivity. Duty: pin
numeric thresholds, with sources, BEFORE any run that scores against them.
This cycle pins none — it reuses my own frozen T2 bar (C_THR=0.005) as a
fixed comparator and issues no perceptual verdict (idealization 9). My review
therefore checks (a) whether my own Phase-2 mandatory fix was actually
delivered, and where; (b) whether the Results section keeps the category
distinction its own text promises; (c) the program's own most-repeated
failure mode (constraint-3/4, Tier-W/Tier-A, "invisible" language slipping in
uninvited); (d) whether C_THR is ever used as anything other than a fixed
pre-existing comparator. Every claim below was checked directly against
`NOTES.md`, `results.json`, `phase2_redteam_audit.md`, and `phase3_synthesis.md`
— not taken on trust.*

---

## (a) Is my own Attack-6 inline caveat actually present?

**Yes, in substance and largely verbatim, attached to the prediction text —
but at only one of the two loci that matter going forward.**

`NOTES.md`'s predictions table, P-NCONV26-5 row, carries:

> "**Disclosure (Attack 6, inline): this cell is FDTD-unvalidated by this
> audit — LOGBOOK's live thread T24 measured a real +0.0070 ABSORB-boundary
> systematic at this identical (λ,θ,FWHM) triple, untested here; this
> prediction concerns only this audit's own n-convergence arithmetic at the
> cell, not T24's separate systematic.**"

That is my own proposed sentence, delivered where Red Team's mandatory-fix
docket item 6 required it — inline with the *prediction* text (line 84), not
buried in idealization 5 alone. This satisfies the letter of Attack 6 exactly
as adjudicated at Phase 3.

**But it does not propagate to the two loci a future cycle will actually
cite.** I checked both directly:

- `NOTES.md`'s own **Results** table, P-NCONV26-5 row (line 177): *"the
  sharpest-stakes cell is converged already AT n=41 (n\*=41, relative move
  0.0% across the whole doubling range) — no flip, nowhere close."* Zero
  mention of T24. A reader who reads only the Results table (this program's
  own named citation pathway — see exp-046 Phase-5, V1) sees an unqualified
  "no flip, nowhere close" with no pointer back to the caveat two sections
  above it.
- `results.json`'s `predictions.P_NCONV26_5` record (grepped the whole file
  for `T24`: **zero hits**, anywhere in `results.json`). The canonical
  machine-readable record — the one a future cycle would actually query —
  carries `c41`, `converged_value`, `nstar`, `relative_move_pct`,
  `flips_C_THR`, `margin_ratio`, `margin_headroom_pct`, `outcome`: eight
  numeric/boolean fields, no disclosure string of any kind.

This is the same shape of gap my own seat caught at Iteration 23 (A1's
"withheld" disposition living in exactly one NOTES.md prose paragraph, absent
from `results.json`) and named again at Iteration 25 (`phase5_review_vision.md`
for exp-046, finding V1) — the mandatory fix reaches the locus it was
literally scoped to and not the two that get cited. Non-load-bearing here
(see (b) below — Red Team already closed the substantive question), but it
is a real, cheap, currently-open propagation gap.

**Fix (two minutes, zero new evaluations):** add a `t24_caveat` string field
to `results.json`'s `P_NCONV26_5` record, and append one clause to the
Results-table row: *"— T24's separate ABSORB systematic at this cell remains
untested by this audit (see Idealization/prediction disclosure)."*

---

## (b) Is the outcome characterized honestly — does the category distinction survive into the Results section?

**The distinction is correctly drawn in the machinery that adjudicates it
(Red Team's Attack 6 disposition, and the prediction's own falsification
band), but NOT restated where the Results section reports the outcome —
exactly the gap named in (a).**

The category question I raised at Phase 2 was: does the program conflate
*"this audit's own arithmetic doesn't move"* with *"this cell has no
perceptual/contamination significance"*? Tracing the record:

- **Red Team's Phase-2 audit got the category distinction exactly right**,
  and did the actual work to earn it — it ran the real n-sweep at this cell
  (`beam_divergence_incoherent_corrected(38,2,25,...)` across the full
  doubling series) and found the relative move is ≈7.7×10⁻⁹%, nine orders of
  magnitude inside the 1% confirm band. Its own words: *"VISION's fix is
  therefore correctly scoped as a **labeling** requirement, not a
  substantive one — the caveat matters for how a future reader interprets
  'does NOT flip' against a real, separate FDTD systematic, not for whether
  this cycle's own arithmetic is trustworthy."* That is the correct
  category boundary, stated precisely, and Phase 3 adopted it without
  edit.
- **The frozen prediction text (line 84) preserves that boundary** —
  its own last clause ("this prediction concerns only this audit's own
  n-convergence arithmetic at the cell, not T24's separate systematic")
  is the category distinction itself, in writing, before the run.
- **The measured outcome (`nstar=41`, `relative_move_pct=0.0`) is
  reported truthfully** — CONFIRMED is the correct verdict against
  P-NCONV26-5's own committed falsification band (≤1% converged move), and
  nothing in the Results table or `results.json` overstates what n-
  convergence alone establishes.
- **What is missing is the restatement of the boundary at the point where
  the outcome is reported.** "No flip, nowhere close" (Results table) is
  true of the convergence question and silent about the contamination
  question — accurate but incomplete at that locus, in a document whose
  own predictions text one section up states the boundary explicitly. A
  reader working from the Results table alone (not the predictions table)
  would not learn that a real, comparable-magnitude, independently-measured
  FDTD systematic (T24, +0.0070, ~7× this cell's headroom) sits on the
  identical cell, untouched by this audit.

**Net: the category distinction is honestly drawn where it is stated, and
nothing in this document actively asserts "this cell has no contamination
risk" — but the Results section does not re-earn or re-state the boundary
it inherited from the predictions table, leaving one locus (of three that
matter: prediction text ✓, Results table ✗, `results.json` ✗) exposed to
exactly the kind of headline-adjacent caveat-drop this program has now
named repeatedly (R4; Iteration 24's bare-"Tier-W" slip; Iteration 23's A1
withholding-disposition gap).** This is a real, actionable finding, not a
substantive defect in the science — Red Team's own independent verification
means no future correction to this arithmetic can move the outcome.

---

## (c) Scan for constraint-3/4, Tier-W/Tier-A, "invisible"/"eye-invisible" language not earned this cycle

**Clean. Nothing found, in either file.**

- `NOTES.md`: grepped for `invisible|eye-invisible|Tier-W|Tier-A`across the
  whole file — zero hits. Grepped for `constraint-3|constraint-4` — two
  hits, both correctly-scoped negations/disclaimers: the header's *"T1
  escape route: NONE. No constraint-3/4 verdict issued or implied"* and
  idealization 7's *"no future near-boundary constraint-3 ... citation may
  lean on an A=752-measured n\* as governing the A=724 geometry"* — a
  restriction on future misuse, not a verdict issued here.
- `results.json`: grepped the entire file for
  `invisible|Tier-W|Tier-A|constraint` — **zero hits, anywhere.**
- The "T1 escape route: NONE" declaration is honored throughout — no
  material law, no σ(I)/σ(x,t), no mechanism claim appears anywhere in
  either file, matching what Red Team's own Constraint check (§ of
  `phase2_redteam_audit.md`) already verified at Phase 2 and what I
  independently reconfirm at Phase 5.
- "Safe" appears three times in `NOTES.md` (lines 83, 198, 208) — every
  instance is scoped explicitly to numerical convergence ("n=41 is safe
  everywhere except the FWHM=20° regime," "n=401 is a safe blanket
  choice... for most... of the grid," "n=41... is now known-safe for
  100/108 cell-function combinations"). None of these reads as, or could be
  mistaken for, a perceptual or contamination-safety claim — the surrounding
  sentences are explicitly about `n*` and cell-function combinations, not
  eyes or ambient scenes. This is the correct, disciplined usage: a cycle
  that characterizes numerical convergence is allowed to say a quadrature
  order is "safe" for its own purpose without that word leaking into this
  program's perceptual vocabulary, and it does not leak here.

This is the cleanest exp-04x cycle I have reviewed on this specific axis —
in contrast to exp-046 (bare "Tier-W" surviving in a Phase-1 draft,
Iteration 23) and exp-047 (bare "Tier-W" surviving in NOTES.md's own
Hypothesis section, Iteration 24), exp-049 never introduces the vocabulary
at all, consistent with its own correctly-scoped "T1 escape route: NONE."

---

## (d) Is C_THR ever re-derived, re-interpreted, or used beyond "fixed pre-existing comparator"?

**No re-derivation anywhere. One disclosed, correctly-scoped secondary use
worth naming for the record, not flagging as a defect.**

Grepped every `C_THR` occurrence in both files (5 in `NOTES.md`, 1 in
`results.json`'s meta block plus its use inside `P_NCONV26_5.flips_C_THR`
and `P_NCONV26_6`'s band):

1. **The convergence criterion's exemption rule** (`|C(2n)|≥C_THR` gates
   whether the relative-error clause applies) borrows C_THR's *numeric
   value* as a conditioning scale — not its *perceptual meaning*. This is
   disclosed explicitly as a modelling choice: idealization 2 states the
   whole convergence criterion "is a disclosed modelling choice... not a
   law of nature," and idealization 9 states plainly "C_THR cited only as
   the pre-existing decision line already scored against — this cycle
   issues no new perceptual verdict and pins no new threshold." This
   secondary numeric reuse (as a magnitude floor to avoid dividing by a
   near-zero contrast) is the same kind of borrowed-scale convention this
   program has used before (T7's δ_C sitting an order of magnitude below
   GATE_HARD, cited as this cycle's own precedent) — a legitimate
   engineering reuse of a fixed number, not a re-interpretation of what
   C_THR *means*.
2. **P-NCONV26-5/6's margin/threshold comparisons** (`flips_C_THR`,
   "36/36 above C_THR") use C_THR exactly as VISION's T2 bar has always
   been used since Iteration 1 — a fixed line a measured `|C|` is compared
   against, no exponent, no luminance dependence, no re-fit.

No instance anywhere re-derives C_THR's value, re-fits its exponent,
extends it to a new ambient regime, or issues a new perceptual verdict with
it. Idealization 9's own promise is honored in full.

---

## Other observations (not part of the four scoped questions, checked because they surfaced during verification)

- **The disclosed sign-convention erratum is exactly the process discipline
  this program should want.** The buggy run scored P-NCONV26-2 REFUTED at
  all three functions (ρ=−0.45/−0.48/−0.47); the runner caught the sign
  inversion by checking against Phase 2's own informal citations before
  treating the run as final, preserved both computations in `results.json`
  under distinct keys, and disclosed it inline in `NOTES.md` rather than
  silently correcting it. This is the R4-adjacent discipline (produce the
  number from the actual committed function, don't hand-smooth a
  discrepancy) applied correctly, one cycle after R4 was adopted.
- **P-NCONV26-3's REFUTED outcome is reported as a real loss, not spun.**
  The Phase-1 prior ("FWHM=10° is a genuinely open regime") did not survive
  contact with the corrected criterion — 0/12 qualifying combinations,
  against a prediction that needed ≥1. NOTES.md's own "Reading" section
  states this plainly ("the 'genuinely open regime' prior was wrong") rather
  than reframing the miss.
- **The two-PARTIAL / one-REFUTED scorecard is consistent with what Red
  Team's Phase-2 audit already predicted would happen** (Attack 2's
  Spearman-split demonstration foretold P-NCONV26-2 would not clear 0.70 per
  function; Attack 5's ill-conditioning finding foretold P-NCONV26-1b/1c/3
  would need the corrected criterion to avoid spurious failures) — the
  mandatory-fix docket did the job it was adopted to do, and the Phase-4
  outcomes are not surprising given Phase 2's own work. That is evidence the
  Red Team audit was substantive, not decorative.
- **Idealization 7's geometry-scope discipline (A=752 vs. A=724) is honored
  in the Results section too** — the "What this changes going forward"
  paragraph explicitly restates the A=752/NY=1584 scope and names the
  PLAN.md follow-up trigger, rather than letting the finding drift toward
  governing exp-048's fallback geometry by omission.

---

## Ranked top-3 candidate next-steps

1. **Close the T24-caveat propagation gap found in (a)/(b) above — cheap,
   same-shift.** Add a `t24_caveat` string to `results.json`'s `P_NCONV26_5`
   record and one clause to the Results-table row. Non-load-bearing to any
   verdict (Red Team already independently re-verified the arithmetic), but
   it is exactly the caveat-drop pattern this program has now named enough
   times (R4 and its unnamed siblings) that leaving it open into the next
   cycle risks a future citation reading "no flip, nowhere close" as
   "contamination-clean," which it was never shown to be.
2. **Run the genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry** (still
   queued since Iteration 23, ranked #3 at Iteration 25's close). This
   audit sharpens, not weakens, the case for running it next: it just showed
   the near-boundary cell's own n-convergence uncertainty is
   ~7.7×10⁻⁹% — effectively zero — which means T24's ~0.0070 ABSORB
   systematic (0.4–1.4× the perceptual threshold) is now the *only*
   unresolved uncertainty source sitting on this program's own sharpest
   contamination-risk cell. Closing it directly answers the question
   P-NCONV26-5's own caveat leaves open.
3. **Honor MATERIALS' Attack-1 follow-up trigger**: re-run this identical
   n-doubling sweep at exp-048's `A=724/NY=1528` geometry before any future
   near-boundary contamination or realizability citation leans on an
   A=752-measured n\*. Cheap (this audit's own code, one new geometry
   import), and closes the one scope question this cycle correctly declined
   to answer itself.

*(Checked against RULED OUT: nothing in this cycle or in my review touches
R1, R2, or R3; no mechanism is proposed or re-proposed anywhere.)*

---

## Verdict

# PROMISING

**Why not RULED OUT.** Nothing here is a dead end — this is an
instrument-fidelity characterization cycle, not a mechanism test, and its
central hypothesis (P-NCONV26-1a: n=41 is genuinely under-converged for the
coherent function at FWHM=20°) held cleanly, confirming exp-046's own
restored A4 finding was real physics, not a fluke.

**Why not PARTIAL.** The cycle's own open questions closed honestly: two
PARTIALs and one pre-registered REFUTED are reported as real, disclosed
outcomes rather than reframed; the sign-convention erratum was self-caught
and disclosed inline, not smoothed over; Red Team's 8-item mandatory-fix
docket was delivered in substance at 7 of 8 items with no remaining
open question, and the 8th (my own Attack 6) was delivered correctly at
the locus it was scoped to (the frozen prediction text) even though it did
not propagate further. The program's own most-repeated failure mode
(constraint-3/4, Tier-W/Tier-A, "invisible" language) is entirely absent —
the cleanest showing on that specific axis of any cycle I have reviewed.
C_THR was used exactly as a fixed comparator throughout, with its one
secondary numeric reuse (the convergence criterion's exemption floor)
correctly disclosed as a modelling choice, not a perceptual re-derivation.

**The one real, actionable finding** — the T24 caveat reaching one locus
(the frozen prediction text) but not the two a future cycle will actually
query (the Results table, `results.json`) — is a genuine, currently-open
propagation gap, but Red Team already independently re-verified the
underlying arithmetic (~7.7×10⁻⁹% move) at Phase 2, so nothing about this
cycle's own substantive content is threatened by it. It is a cheap fix, not
a reason to withhold PROMISING.
