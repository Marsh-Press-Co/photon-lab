# PHASE 5 — REVIEW · VISION SCIENCE seat · exp-097

*Constraint-3 perceptual metrics N/A this cycle (zero-FDTD code/documentation
verification, no ambient/contrast claim anywhere in scope). Per this cycle's
charge, discipline applied to procedural/documentation compliance: the
carried-idealizations banner's presence in the Result section (my own
Phase-2 critique's own demand), the standing-items ledger update in §9, and
any other structural gap (missing sections, word-cap overruns, citation
errors). Reviewed blind — no other seat's Phase-5 review read or consulted,
though four now sit alongside this one in the working directory (EM,
MATERIALS, QUANTUM, THERMODYNAMICS); none opened.*

## 1. The banner check (my own Phase-2 demand, verified by name)

**PASS, independently confirmed by direct `grep`/read of the committed
`NOTES.md`, not taken on the document's own word.**

- **Result section** (line 301): *"Carried idealizations banner (per §6's
  own governance ruling — placed here AND at Predictions, closing the
  verification gap VISION found in Phase 1's own draft): every result below
  is governed by Idealizations 1/7/17/38/39 plus this cycle's own 40–45."*
  Present, as the first paragraph of `## Result`, before any scored claim.
- **Predictions section** (line 258): the identical banner sentence,
  present.
- **Governance ruling itself** (§6, re-verified independently this session
  against `LOGBOOK.md`'s own Iteration-65/exp-088 text): the literal rule —
  *"the 'carried idealizations' banner is now required at BOTH the
  Predictions section AND the Result section"* — is quoted verbatim and
  correctly, not paraphrased. I re-grepped the source line myself
  (`LOGBOOK.md` ~line 4968) rather than trusting the citation: it matches
  exactly.

Red Team's Phase-2 docket item 4 (adopted from my own Phase-2 critique)
required more than textual correctness — it required an attached
verification mechanism, discharged by naming that "Phase 5 is asked to
confirm this by name" (NOTES.md, Result section, closing line). **This
document is that confirmation, by name: PASS.** Two prior cycles
(exp-095, exp-096) each believed in real time they were complying with
the identical rule and were both wrong, caught only after the fact. This
is the first T28 cycle where the rule's own literal text was applied
correctly at first attempt, not merely re-diagnosed after the fact — a
genuine, structural improvement over the two-cycle drift, not a repeat of
it.

## 2. The standing-items ledger (§9, "What this cycle does NOT do")

**PASS, correctly incremented.** exp-096's own ledger read "NINE
consecutive cycles undischarged, Iterations 64–73" (grazing-incidence) and
"TWENTY-ONE consecutive cycles deferred, 076–096" (x-wall
wavelength-generality). exp-097's NOTES.md restores the line verbatim,
incremented by exactly one cycle each: **"now TEN consecutive cycles
undischarged, Iterations 64–74"** and **"now TWENTY-TWO consecutive cycles
deferred, 076–097."** Both figures are internally consistent with the
prior cycle's own filed numbers (9→10, 21→22, ranges each extended by
exactly one iteration/experiment). This closes the gap PHOTONICS' Phase-2
critique caught (the line's silent, first-time-in-the-cited-span drop from
Phase 1's own draft) — independently re-verified against Phase 1's actual
text: `phase1_proposal.md` §9 restates only Tier-1 items 6–9, never the
standing/unranked line, confirming the critique's own "zero hits" grep
claim. Restoring the line does not discharge either item (NOTES.md's own
Learned #4 says so explicitly) — it only prevents a second silent drop.

## 3. A structural gap this review newly finds: the ≤150-word Phase-2 cap

**Not previously flagged by any of the five blind critiques, the Red Team
Phase-2 audit, or NOTES.md itself.** PANEL.md's Phase 2 rule is explicit:
*"one steel-man (≤150 words), one sharpest attack (≤150 words)."*
Independently word-counted (Python, `str.split()`, section text only,
excluding headings) all five blind critiques' Sharpest-attack sections
this session:

| Seat | Steel-man | Sharpest attack | Cap compliance |
|---|---|---|---|
| PHOTONICS | 138 | 145 | within cap |
| ELECTROMAGNETISM | 99 | **156** | **6 words over** |
| QUANTUM OPTICS | 124 | **156** | **6 words over** |
| THERMODYNAMICS | 129 | **170** | **20 words over** |
| VISION SCIENCE (this seat, Phase 2) | 139 | **156** | **6 words over** |

Four of five blind critiques' Sharpest-attack sections exceed the
≤150-word cap, two of them (QUANTUM, VISION) self-labeled their own
section header "(≤150 words)" while running over it, and THERMODYNAMICS
labeled its header "(150 words)" while running 20 words over — a
self-reported figure that does not survive contact with an actual count,
the identical "claimed figure does not reproduce" shape R4/R9 exist to
police, now applied to a word-cap self-report rather than a numeric
result. None of this is disputed as *substance* — every attack reviewed
above (§0 of this document, and independently re-confirmed here) is a
real, load-bearing finding, correctly adopted into the fix docket. This is
a pure format-compliance gap, **non-load-bearing to any scored verdict**,
but genuine, previously uncaught, and notable precisely because this
cycle's own stated mandate (R18) is auditing claimed-vs-actual scope —
the Phase-2 layer that built that audit itself was not, this once, held to
its own word-count scope. Not a "known, named, ignored" recurrence (this
is the first time this specific gap-class has been named on this
sub-thread) — does not warrant Checkpoint escalation on its own founding
instance, matching this program's own unbroken precedent for R6/R11/R16/
R17/R18's founding cycles. Flagging here so a repeat, after this naming,
would be judged against a different bar.

## 4. Other structural/citation checks (no further gaps found)

- **`y_hi`/`R{n}_BASE_NY` mis-citation (EM+THERMODYNAMICS' Phase-2 catch,
  Red Team's own extension to §0):** independently re-verified the fix
  landed correctly in NOTES.md's own committed text (Setup, item 3): both
  `R3` and `R5` now correctly cite `R{3,5}_CONFIGS["C40_R{3,5}"]["y_hi"]`
  (2316/3860), never the domain-height constant `R{n}_BASE_NY`
  (2376/3960). Confirmed against `results.json`'s own
  `check5_extended` block, bit-exact (2316/3860 stored and recomputed
  values agree for all three families).
- **`design_geometry.py` citation path:** every citation in NOTES.md
  correctly names `experiments/069-t21-block-mini-period-match-power-up/`
  — no phantom T28 `069-...` path anywhere (independently grepped this
  session).
- **Predictions-before-run house discipline:** independently confirmed
  from `git log`, not merely asserted — `d8960f4` (Phase 3, NOTES.md
  frozen) precedes `29c8b17` (Phase 4, results committed); `git log
  --oneline -- lab/` shows the most recent `lab/` change predates this
  cycle by three iterations (exp-094), confirming "zero `lab/` diff" is
  literally true, not merely claimed.
- **Trust suite claim:** independently re-ran `python3
  lab/validation/run_all.py --only 12346789` this session — **41/41
  PASS**, matching NOTES.md's own cited figure exactly, not taken on the
  document's word.
- **All numeric Result claims (registration gate CLEAN, representative-set
  Checks 1–4/7, Check 5 3/3 families, Check 6-new 8/8, all nine
  fault-injection scenarios, 21-construction count):** independently
  re-derived from `results.json` this session, bit-exact against every
  figure NOTES.md's Result section states. No discrepancy found. (One
  cosmetic, non-substantive difference: NOTES.md's prose cites "2.305s
  wall," `results.json`'s currently-committed run shows 2.097s — a
  wall-clock timing field, explicitly the one class of figure this
  sub-thread's own precedent, Iteration 71/exp-094, rules legitimately
  variable between reruns and not evidence of a discrepancy.)
- **Missing artifact, minor:** exp-096 shipped a `run_output.txt`;
  exp-097 does not. Not a PANEL.md-mandated section, and NOTES.md's own
  Result section already restates every figure `run.py`'s own print
  block would have produced — a cosmetic completeness gap, not a
  documentation-discipline one.
- **Word-cap compliance elsewhere:** Phase 1's own §1 narrative
  independently recounted at 212 words (matches the proposal's and my own
  Phase-2 critique's cited figure), within the 300-word cap.
- **No missing Result/Learned/Next-class section on NOTES.md itself.**
  `## Result` and `## Learned` are both present and substantive. `##
  Next` is absent — consistent with this program's own established
  practice (the Reconciled-queue "Next" section is written once Red
  Team's Phase-5 final audit reconciles all blind reviews; four of six
  non-Red-Team Phase-5 reviews are filed as of this reading, including
  this one, but Red Team's own final audit has not yet run). Not a gap.

## Verdict: CONCUR-WITH-GAP(S)

The substantive core holds without qualification: all six of Red Team's
Phase-2 mandatory fixes are independently confirmed adopted and correctly
implemented, every numeric claim in Result independently reproduces
bit-exact against `results.json` and against a fresh trust-suite run, the
predictions-before-run discipline is independently confirmed from `git
log`, and both items this cycle's charge specifically assigned this seat
— the carried-idealizations banner's presence in Result, and the
standing-items ledger's correct 10/22 update — **both PASS, independently
verified by name.** The one gap this review newly finds (§3, the ≤150-word
Phase-2 sharpest-attack cap overrun on four of five blind critiques,
uncaught by the Red Team Phase-2 audit that itself exists to police
exactly this kind of claimed-vs-actual compliance) is real, non-load-
bearing to any scored result, and not a recurrence of a previously-named
pattern — it does not rise to DISPUTE.

## Ranked candidate directions for Iteration 75

1. **Tier 1 item 6 (EM's original Iteration-73 proposal, carried through
   exp-096's own Next section): bracket the other three established
   `cpl=20` nulls at `cpl=40`, ~24 calls.** Now the single highest-value
   real-FDTD step — the registration-readback gate is CLEAN under
   strictly more discriminating machinery than at exp-096 (7 checks, 9
   independently-verified fault-injection scenarios, a fixed
   non-tautological Check 6), so no further zero-FDTD work is needed
   before this spend is trustworthy. This is the decisive discriminator
   between a family-wide recipe defect and feature-dependent genuine node
   migration — the open question this whole two-cycle registration
   detour exists to answer.
2. **Tier 1 item 7: the re-centered, directionally-weighted
   node-bracketing re-run at θ₀≈38.590°, sized to the now-independently-
   confirmed ≥0.5° single-sided half-width, ~8–16 calls.** Sequenced
   after item 6 per exp-096's own stated rationale (a family-wide finding
   in item 6 would reprioritize this window's own re-run). The direct
   answer to the question that motivated exp-095/exp-096/exp-097 in the
   first place.
3. **Bundle THERMODYNAMICS' preventive item 8 (pre-wire
   `netd_row()`/`cell_metrics_r{3,4,5}` sidecar extraction, per R16) into
   whichever of items 1/2's `run.py` computes `delta_scene`/
   `frac_contrast`, from first commit — plus a one-line Director note in
   the LOGBOOK entry naming this cycle's §3 word-cap finding, so a
   repeat next cycle is judged against a named precedent rather than
   discovered fresh a second time.** Both are zero/near-zero marginal
   cost bundled with items 1–2's own real FDTD spend, closing two small,
   cheap, currently-open bookkeeping risks before they recur.
