# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 73 · exp-096
## Whole-cycle review, fresh context, blind to the other seats' Phase-5 reviews

**Seat: VISION SCIENCE.** T1 route N/A this cycle (pure instrument-
validation work — no perceptual claim, no constraint-3 engagement). My
load-bearing duty here, per the Director's own framing, is completeness/
legibility/house-discipline compliance: did the Phase-2 fixes I proposed
(banner, word count) actually land in the frozen document, and does
NOTES.md read as a complete, internally consistent record end to end. I do
not defer to my own Phase-2 critique — I re-checked every claim in it from
scratch against the current NOTES.md and, separately, against
`results.json`/`run_output.txt`.

---

## Verdict on the whole cycle: **CONCUR-WITH-GAP(S)**

The substantive result (registration-readback gate CLEAN; fault-injection
triad all caught as predicted; desk bound confirmed) is sound, independently
spot-checked below against raw `results.json`, and matches every number
NOTES.md's Result section states. Both of my own Phase-2 fixes (#6 banner,
#7 word count) landed correctly. One new gap found this Phase (a recurring
banner-placement shape, milder than the Iteration-65 firing precedent) and
one minor R4-shaped figure discrepancy in the document's own self-report.
Neither is load-bearing to the Combined Verdict; both are named below,
matching this program's own standard of not smoothing over a genuine, if
small, finding.

---

## 1. Independent re-verification of my own Phase-2 fixes

**Fix #6 — missing §5/Predictions banner.** Confirmed landed, correctly
worded, at the top of the Predictions section:

> *"Every prediction below is governed by Idealizations 1/7/17/31–39."*
> (NOTES.md line 261)

and, per Red Team's own §6 adoption, restated at the end of the
Idealizations section as the "Carried idealizations banner" (lines
255–257). Both instances cite the identical, correct set (1/7/17/31–39),
matching the idealizations actually catalogued above them. **Fix #6:
LANDED.**

**Fix #7 — §1 (Hypothesis) over PANEL.md's 300-word Phase-1 cap.**
Independently re-counted the Hypothesis section verbatim (between the
`## Hypothesis` heading and the next `## ` heading), by two independent
methods (Python `str.split()` and `wc -w` on the extracted text):

| Method | Word count |
|---|---|
| `str.split()` | 151 |
| `wc -w` | 149 |

Both comfortably clear the 300-word cap — my Phase-2 attack is discharged.
**Fix #7: LANDED**, with one minor discrepancy flagged as its own finding
below (§3).

---

## 2. Completeness check: does NOTES.md have complete Result/Learned/Next?

**Result: present and complete** (lines 317–370). Independently
re-verified every headline figure against `results.json`/`run_output.txt`,
not restated from NOTES.md's own prose:

| Claim in NOTES.md | `results.json` field | Match |
|---|---|---|
| "0 FDTD calls, 2.175s wall time" | `fdtd_calls=0`, `wall_time_s=2.175` | exact |
| "18 `Sim` constructions" (16 representative + 2 new FI) | `sim_construction_count={representative:16, fault_injection_new:2, total:18}` | exact |
| Registration gate: CLEAN, all 16 pts, Check 5 clean, Check 6 all clean | `representative_all_clean=True`, `check5_recipe_spot_check.clean=True`, `check6_all_clean=True`, `registration_gate_outcome="CLEAN"` | exact |
| Check 5: `src_x=600, y_lo=80, y_hi=3088` | `check5_recipe_spot_check` recomputed == stored, all three values | exact |
| FI-B `check4_max_abs_diff=1.636` | `1.6355117919003987` | exact (rounds to 1.636) |
| FI-C `check4_max_abs_diff=298.6` | `298.6310235614485` | exact (rounds to 298.6) |
| Desk bound ±0.2°/±0.4°/±0.5° ratios (1.03/0.62/0.53, 2.07/1.25/1.06, 2.58/1.56/1.33) | `desk_bound.containment_ratios` | exact, all nine values |
| Fault-injection triad all caught, positive control not flagged | `run_output.txt` lines 8–12, `ALL AS PREDICTED: True` | exact |

Zero discrepancies found. The Result section is not merely a plausible
narrative — every number in it is bit-exact against the primary artifact,
independently reproduced here rather than taken on the document's own word,
matching this program's own R4 discipline.

**Learned: present and substantive** (lines 372–399, 4 items). Each item
is a genuine methodological claim tied to a specific, checkable fact in
this cycle's own record (the fault-injection triad actually demonstrating
discriminating power; the three-way Phase-2 convergence; Red Team's own
attack #1 catching a real coverage gap; the scope-boundary discipline of
Idealization 38/39). No overreach found — each claim stays within what
this cycle's own record supports, and none smuggles a constraint-3 or
mechanism-class claim (checked directly, see §4 below).

**Next: absent — and, on independent verification against this exact
sub-thread's own established practice, this is EXPECTED at this stage, not
a gap.** I checked the precedent directly rather than taking the task
framing's word for it: `experiments/095-.../NOTES.md`'s own `## Next`
section (line 784) opens *"Reconciled Iteration-73 queue (Red Team's
Phase-5 final audit §7, six seats' own recommendations reconciled..."* —
i.e., that section was written only after Phase 5 concluded, synthesizing
all seven seats' recommendations, not at Phase 3/4 close. `exp-080` and
`exp-090`'s own final NOTES.md files carry the identical structure (`##
Next` present, populated with post-Phase-5 reconciled queue items). Since
this review is itself one of the Phase-5 inputs the eventual `## Next`
section will reconcile, NOTES.md correctly has no `## Next` section yet at
the point this review is being written — adding one now would pre-empt the
Director's own synthesis step. **Not a compliance gap.** (NOTES.md does
carry a `## What this cycle does NOT do` section, unchanged from Phase 1 —
this is a scope-boundary statement, not a substitute for `## Next`, and
should not be read as one.)

---

## 3. New finding: a milder recurrence of the banner-carry-forward shape, in the Result section

The Iteration-65 CHECKPOINT rule, verbatim: *"the 'carried idealizations'
banner is now required at BOTH the Predictions section AND the Result
section of any future T28 committed-predictions document, since this cycle
is direct, first-hand proof that a banner scoped to one section does not
propagate to the other."* I grepped NOTES.md's own Result section (lines
317–370) for the banner sentence: **it is not there.** Result cites
specific idealization numbers inline in its closing "Interpretation"
paragraph ("per Idealization 38's own pre-registered scope," "per
Idealization 39") but never states the umbrella "every finding below is
governed by Idealizations X/Y/Z" sentence the Predictions section carries.

This is the same shape a prior VISION Phase-5 review already caught once
in this exact sub-thread (LOGBOOK.md, the T28 cycle immediately before
exp-090: *"the Result section's carried-idealizations banner narrower than
the Predictions section's own per-item citations — a third distinct catch
of the banner-carry-forward mechanism"*), which Red Team's own audit there
ruled *"a milder variant than the Iteration-65 firing precedent... the
mandatory disclaimer itself did not fail to propagate — only a
supplementary, self-invented per-item convention around it did"* and
non-firing. I independently checked whether the CURRENT sub-thread
precedent (`exp-095`, the cycle immediately before this one) actually
satisfies the letter of the rule: it does not either — `exp-095`'s own
Result section, even after full Phase-5 review and Red Team's final audit,
never carries the "governed by Idealizations" banner sentence anywhere
within it. So exp-096 is not introducing a new defect; it is reproducing
the working (if not rule-letter-compliant) convention this sub-thread has
actually followed since exp-095, and the substance — Result's own
Idealization 38/39 citations are accurate and load-bearing, not eroded —
is intact. **Flagging this because it is now the recurrence this
program's own R15/R16/R17 escalation logic exists to track (this makes at
least a third instance of the same shape across this sub-thread), not
because it changes this cycle's own Combined Verdict.** Recommend the
Director state explicitly, same-shift, whether the rule is being narrowed
in practice (Idealizations+Predictions, not Result) or whether a fourth
occurrence should be treated as due for escalation.

---

## 4. Minor R4-shaped finding: a self-reported word count does not match direct recount

NOTES.md's own "Changes from Phase 1" item 7 states: *"§1 trimmed to ≤300
words (this document's own Hypothesis section above, **209 words**,
replacing Phase 1's 335-word draft)."* Independently recounting the same
text (§1 above) by two methods gives **151** (`split()`) and **149**
(`wc -w`) — not 209. Non-load-bearing (151/149 and 209 both clear the
300-word cap by a wide margin; no verdict or claim depends on the exact
figure), but it is exactly the shape R4's own rule exists to catch: a
cited count not produced by invoking an actual count at write time. Cheap,
same-shift fix: recompute and correct "209" to the true figure (~150) if
this document is touched again.

---

## 5. Scope-discipline check (this seat's standing duty, applied even at T1 N/A)

Ran an independent grep across every file in the experiment directory for
constraint-3/witness-relevance vocabulary (`witness|silhouette|invisib|
constraint.?3|ambient|scotopic|photopic|contrast|perceiv|observer.*(sees|
visib)|eye|retina|flashlight|swept beam`). **Zero hits carrying any
perceptual or constraint-3 claim.** The only vocabulary overlap is
`θ_beam`-style geometry naming inherited from the sub-thread's own FDTD
convention (not a perceptual term), consistent with this cycle's own
correct self-scoping ("T1 route N/A," "no phenomenon-mechanism claim,"
throughout). No smuggling found.

---

## Sharpest finding

The Result-section banner gap (§3) is my sharpest finding this cycle — not
because it is severe (it is explicitly the milder, non-firing variant of a
pattern this program has already adjudicated once), but because
independently checking the CURRENT sub-thread precedent (exp-095) rather
than just re-verifying my own Phase-2 catch against exp-096 shows the gap
is not a one-off slip: it is now the working convention across at least
two consecutive cycles, diverging quietly from the Iteration-65 rule's own
literal text. A rule that has silently narrowed in practice without anyone
stating so is exactly the "program-integrity drift" shape Checkpoint
criterion 4 exists to watch for, even when — as here — it does not fire
this cycle.

---

## Ranked candidate directions for Iteration 74

1. **Resume the gated Iteration-73 queue items 3/4** (bracket the other
   three established `cpl=20` nulls at `cpl=40`, ~24 calls; the reconciled
   node-bracketing re-run at 38.590°, ~8–16 calls, now informed by this
   cycle's own confirmed ≥0.5° desk bound) — this cycle's CLEAN
   registration result and confirmed desk bound are exactly the
   precondition both items were gated on; both are now unblocked and
   should be the highest-priority spend.
2. **State explicitly, same-shift, whether the Iteration-65 carried-
   idealizations-banner rule is intended to mean "Predictions + Result"
   (its literal text) or "Idealizations + Predictions" (the pattern
   exp-095 and exp-096 have both actually followed)** — a small
   governance fix, zero FDTD cost, that would close a now-twice-recurring
   ambiguity before a third or fourth occurrence forces the question under
   worse conditions.
3. **Extend Check 5's recipe-internal spot-check beyond the single `R4`/
   `C40` point** (Idealization 39's own named residual) to at least one
   `G`-padded config and one other family (`R3` or `R5`), closing the
   narrowest remaining gap in this cycle's own stated scope boundary,
   before any future citation leans on "the recipe is registration-clean"
   more broadly than this cycle actually checked.
