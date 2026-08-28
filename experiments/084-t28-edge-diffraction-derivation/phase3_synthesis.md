# PHASE 3 — SYNTHESIS · Panel Iteration 61 · exp-084

*Director (shift agent driving this cycle). Synthesizes but does not vote
in Phase 2, per PANEL.md. States which criticisms are accepted/overridden
and why.*

## Disposition of the Phase-2 record

Five blind critiques (MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM
OPTICS, VISION SCIENCE), all **support-with-changes**; Red Team's audit
(`phase2_redteam_audit.md`), **PROCEED-WITH-MANDATORY-FIXES**, 6 items.

**All 6 fix-docket items are ADOPTED IN FULL. Nothing is overridden.** Red
Team's audit independently re-derived every load-bearing number from
committed files (not from the five critiques' prose), and this Director
independently re-ran the two most consequential checks from scratch a
*third* time (`phase3_fix_docket_checks.py`, bit-exact match to Red Team's
own figures) before adopting them. There is no daylight between what the
critics found, what Red Team verified, and what this synthesis adopts.

1. **Downgrade leg (a)'s FINAL VERDICT from SUPPORT to INCONCLUSIVE.**
   ADOPTED. Two independent lines of evidence, both independently
   reproduced by this Director:
   - Red Team's circular-shift null test (this program's own established
     "harder companion," LOGBOOK Iteration 60's own precedent for
     reversing exp-083's two-tone claim): `R²=0.36965580905914364` is met
     or exceeded by **15/30 = 50.0%** of the real curve's order-preserving
     circular shifts, run against the *literal production pipeline*
     (`free_period_with_widening`, full staged widening) — sitting at the
     null distribution's own median (`mean=0.4594`), not a rejection tail.
   - VISION's own pre-registered T21-decorrelation escape clause, run to
     its actual conclusion: `R²_fixed(leg_a, T21's period)=0.27096` vs.
     `R²_fixed(real C80, T21's period)=0.26453` — a 2.4% relative
     difference, "comparable," not "near-zero." VISION's own rule requires
     the downgrade on this basis alone, independent of the null test.
   Both routes agree. The R5 specificity-over-targets control (`5/60`)
   is not wrong, but answers a different question (how many OTHER target
   periods would this SAME fitted curve also match) than the decisive one
   (is this curve's own R² distinguishable from noise at all). Confirmed:
   **leg (a) is recorded as INCONCLUSIVE**, not SUPPORT, matching
   Iteration 60/exp-083's own "do not soften a real finding" standard.
2. **Log Checkpoint criterion 4 as FIRING.** ADOPTED, after direct
   Director review of the precommitment text (see the CHECKPOINT section
   below for the full reasoning — this is not a rubber stamp of Red Team's
   ruling; the Director considered and rejected an alternative reading
   before agreeing).
3. **Do not adopt "missing Rayleigh–Sommerfeld boundary term" as settled
   cause for leg (b)'s Anchor-2 failure.** ADOPTED. `NOTES.md` (below)
   states both EM's alternative (a missing phase-carrying obliquity
   factor — the more likely cause per EM's own non-smoothness evidence)
   and the original write-up's RS-term guess as open, undischarged
   hypotheses. The discriminating test EM named (re-weight leg (b)'s
   stage-2 secondary sources by `field_and_h`'s own driven-current
   obliquity convention) is queued for Iteration 62+, not run this cycle
   — running it well requires care not to just patch leg (b) into a new
   untested construction under time pressure; better to scope it as its
   own small proposal next cycle.
4. **Add THERMODYNAMICS' Anchor 3 (fringe amplitude vs. the
   `graded_black_shell`'s established `R≤0.2%` ceiling) as mandatory
   before any future leg (b) re-attempt.** ADOPTED as a standing
   requirement, logged in `NOTES.md`'s Next section and PLAN.md's queue.
   This cycle's own `~41×` finding (leg (b)'s raw `ptp_b=8.21×10⁻²`
   against the `R≤0.2%` ceiling) is logged as the reason it is needed.
5. **Log the shape-correlation finding explicitly, separate from the
   period-match downgrade.** ADOPTED and re-verified a third time (see
   `phase3_fix_docket_checks.py`/`phase3_fix_docket_results.json`):
   `corr(leg_a_curve, real FDTD C80(θ)) = +0.958186`, against three
   controls sampled at the identical 31-point grid — leg (b)'s own real
   (masked) output (`r=−0.104597`), a bare linear ramp (`r=−0.334705`),
   a bare quadratic (`r=−0.553409`). This is real, independently
   triple-confirmed signal and survives the period-match downgrade
   intact — it says the zero-FDTD diffraction integral's raw *shape*
   tracks the real FDTD curve; it says nothing about whether its
   *best-fit period specifically* is meaningful at this sample size
   (Adopted finding 1 above shows it is not).
6. **Flag the R5-specificity-vs-null-test divergence as a candidate new
   standing house rule.** ADOPTED — see new rule **R10** below.

## New standing rule — R10 (adopted this cycle)

Per Red Team's own recommendation (§3, last bullet of
`phase2_redteam_audit.md`) and this program's own R6/R7/R8/R9 lineage
(generalizing a real, twice-outcome-determining gap rather than treating
it as a one-off): **a specificity-over-candidate-targets sweep (R5's own
original form: "how many OTHER targets would this same fitted curve also
match") is not a substitute for an order-preserving null-under-noise test
(circular-shift or equivalent: "is this curve's own best fit
distinguishable from noise at all"). Both are legitimate R5-family
look-elsewhere controls, but they answer different questions and can
disagree sharply on the identical data** — confirmed twice now
(exp-083/Iteration 60: the phase-shift admixture claim; exp-084/Iteration
61: leg (a)'s period-match SUPPORT), both times with the null-under-noise
test being the decisive, correct one and the specificity-over-targets
sweep alone reading as falsely reassuring. **Rule: any future free-period-
fit or free-phase-fit SUPPORT/CONFIRM verdict must clear an
order-preserving null-under-noise test (circular-shift on the real data,
or an equivalent structurally-matched surrogate — see R10's own open
question below) BEFORE it is reported as evidence, not merely a
specificity-over-candidate-targets sweep.** This is logged in LOGBOOK's
RULED OUT registry as **R10**, in the R6/R7/R8/R9 house-discipline
lineage (not a ruled-out idea; a standing procedural rule).

**Open question this rule does not yet resolve** (flagged, not solved,
this cycle): Iteration 60's own Phase-5 record found that circular-shift
is not always the best-suited null either (EM's AR(1)-parametric
surrogate attempt, which itself failed to reproduce under Red Team's own
scrutiny). R10 requires *an* order-preserving null-under-noise test, not
specifically circular-shift — which family is correct for which class of
residual structure (i.i.d., AR(1), or otherwise) remains an open,
case-by-case judgment for the seat proposing the test, exactly as
Iteration 60 left it.

## Checkpoint criterion 4 — Director's own reasoning (not a rubber stamp)

Before adopting Red Team's ruling, the Director considered the strongest
available non-firing argument: at Iteration 58/exp-081, a comparable
compliance gap (VISION's finding that a required "state an explicit
reason" instruction was not met) was caught **within the same shift**
(that cycle's own Phase 5) and ruled **non-firing**, precisely because it
was found and closed before LOGBOOK was written, not defended past a
freeze point. This cycle's gap (the energy-interception cross-check's
third silent absence) was likewise caught within the same shift — earlier,
in fact, at Phase 2, before Phase 3 even began.

**But Iteration 60's own precommitment is written in stronger, more
specific language than the generic "same-shift catch" pattern**: *"a third
consecutive deferral without an explicit reason fires it"* — echoing the
identical escalating-tripwire phrasing this program has used exactly to
foreclose a Director's own future latitude to defuse it with a same-shift
save ("would no longer be a close call... fire outright, not weighed as a
close call again," Iteration 58's own language for a *different* item).
The entire point of a pre-committed, numbered-cycle tripwire is that it
fires ON SCHEDULE, not subject to fresh Phase-3 argument each time it
arrives — otherwise no such tripwire could ever function as a real
commitment device. The Director could supply an explicit reason for
deferral right now, in this document, and that would arguably prevent the
LITERAL condition ("without an explicit reason") from being true of the
final record — but doing so *specifically to avoid the pre-committed
firing*, rather than because Iteration 62 has a genuine, independent
reason to defer again, would be exactly the kind of after-the-fact
rationalization this program's own culture (R8: "an unverified argument…
is not sufficient… before a flagged gap is filed as non-blocking") exists
to catch. The honest reading is that this item's own three-cycle pattern
(exp-082, exp-083, exp-084) is real, the tripwire was written to fire on
it, and it should be allowed to do exactly that.

**Checkpoint criterion 4 FIRES — the 13th time in this program.** Per
this program's unbroken 12-for-12 precedent, ruled a **notification, not a
pause**: nothing in this cycle's own `lab/` state or Combined Verdict is
touched; the energy-interception cross-check itself is queued as a
high-priority Iteration-62 item (not run this cycle — the Director judged
retrofitting it into exp-084's own zero-FDTD diffraction-geometry scope,
under time pressure, purely to avoid the firing, would itself be a form of
the box-checking R8 exists to prevent; it belongs to a future cycle with
a genuine article-loaded scene to reuse, as it was originally scoped at
Iteration 59). See the CHECKPOINT entry in LOGBOOK.md for the full record
Marsh is convened on.

## Combined Verdict

**PARTIAL.** Leg (a): INCONCLUSIVE on the period-match question (does not
clear the program's own correct null test), but a genuine, independently
triple-confirmed positive finding on the shape-correlation question
(`r=0.958`) — the first time a zero-FDTD, vacuum-only diffraction
construction has reproduced ~92% of a real FDTD curve's variance in this
nine-cycle-plus T28 sub-thread. Leg (b): NO VERDICT, an instrument-
validation failure correctly caught by its own pre-registered anchor
before any false conclusion was drawn — a genuinely new, real, still-open
methodological gap (two competing causal explanations, EM's phase-factor
hypothesis favored but undischarged). T28's own substantive mechanism
question (`P_edge_A`'s ultimate physical origin) remains open — narrowed,
not answered: this cycle is the first to show the underlying oscillation
has a genuine physical kinship to real near-field diffraction physics
(the shape correlation), even though its specific period cannot yet be
distinguished from chance at this window's own sample size.

No FROZEN-PREDICTIONS git-freeze cycle is needed for Phase 4: every fix
above is a prose/verdict correction to already-computed numbers (each
independently reproduced three times over: Phase 1's own code, Red Team's
from-scratch re-implementation, this Director's own third re-run), not a
fresh, unverified prediction. Phase 4 is therefore: confirm the trust
suite is still green and `lab/` untouched (done, see NOTES.md), and treat
the corrected `phase1_proposal.md` + this document + the fix-docket script
as the official record.
