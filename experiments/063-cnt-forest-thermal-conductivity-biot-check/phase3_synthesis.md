# exp-063 — Phase 3 Synthesis (Director)

**Panel Iteration 40.** Director resolves Phase 2 into one testable
configuration, states accepted/overridden criticisms, and applies Red
Team's mandatory-fix docket. Predictions are committed to git in
`NOTES.md`, this same commit, BEFORE any Phase 4 search runs (house
discipline, non-negotiable).

---

## 1. Criticisms accepted / overridden

**All Phase-2 criticism is accepted; none is overridden.** Five blind
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS, VISION
SCIENCE), all support-with-changes, and Red Team's audit (PROCEED-WITH-
MANDATORY-FIXES) converge on a proposal that is arithmetically sound at
its core (Section 4's Biot/conduction-resistance algebra, independently
re-derived twice now — EM's critique, Red Team's audit — and confirmed to
the printed digit, including κ_critical=0.0897) but under-examined on the
physical MODEL its formula is applied to: three independent seats
(PHOTONICS, MATERIALS, ELECTROMAGNETISM) each attacked a different
variable in that model — generation-side geometry, loss-side geometry,
and length legitimacy respectively — and Red Team's own audit confirmed
these triangulate rather than duplicate (`phase2_redteam_audit.md` §2).
As Director I accept all eight mandatory-fix items and the central
Checkpoint ruling (no criterion fires) with no override.

**Why no override.** Every attack is scoped, concrete, and cheap to apply
without re-scoping the cycle's THERMODYNAMICS lead or returning to Phase
1 — the standard this program applies before accepting a mandatory-fix
docket wholesale (exp-060/061/062 precedent). None of the five critiques
opposed outright. Red Team independently re-verified every disputed
number and traced every disputed dependency through source code and
LOGBOOK.md directly (not merely relaying a critique) — running both
`lab/caveat_lint.py` and `lab/numeric_lint.py` live rather than trusting
VISION's prose, re-deriving the T9 radial-absorption ledger from
`materials.py` directly rather than trusting PHOTONICS' claim, and
grepping `REALIZABILITY_MEMO.md`/exp-061/062 directly to correct
MATERIALS' own citation (a paraphrase presented as a quote, substance
unaffected — see below). There is no case here for Director override of
a ruling reached with that level of independent verification.

**One correction to a critique's own sourcing, not its substance
(MATERIALS, attack 4):** Red Team found MATERIALS' quoted phrase ("front
tips exposed to air/light, root bonded to whatever it blacks out")
attributed to `REALIZABILITY_MEMO.md`/exp-061/062 does not appear
verbatim in either file. This is MATERIALS' own reasonable physical
elaboration of an established program convention ("coating" is used
throughout both files for this candidate class), not a fabricated
citation — `NOTES.md` states the deployment-geometry argument as
MATERIALS' own reasoning, corrected accordingly. The underlying attack
(the rear-only-loss boundary condition is asserted, not derived, as this
geometry's worst case) stands regardless and is fully accepted.

---

## 2. The Checkpoint-4 question — Director's disposition

**Accepted, not overridden: does not fire.** VISION's Phase-2 critique
found this cycle's own new machinery (`biot_number`, `front_surface_
conduction_correction`, κ_critical=0.0897) has no `lab/caveat_lint_
config.json` or `lab/numeric_lint_config.json` registry entry yet, and
raised — but explicitly deferred to the Director/Red Team — whether this
fires Checkpoint criterion 4, given the program's two same-iteration
firings one cycle earlier (Iteration 39).

Red Team's audit (`phase2_redteam_audit.md` §3) argues this against the
closer precedent directly: Iteration 38, where a caveat-lint gap found in
a tool built THAT SAME cycle was explicitly ruled "a self-caught,
pre-freeze registration gap, not a docketed propagation promise broken by
hand-review," and did NOT fire — only a forward tripwire was set. I
independently re-checked the two facts this ruling turns on: (1)
`lab/numeric_lint.py` (commit `2d6e5e7`) was built the commit immediately
before this proposal's own Phase-1 commit (`9c60b05`) — there was no
prior point at which an exp-063 entry could have existed to register; (2)
`lab/caveat_lint_config.json`'s six existing entries never covered these
brand-new numbers, which is categorically different from the Iteration-39
firings (a gap in an ALREADY-HARDENED tripwire — `exp061-t18-
evidentiary-tier-propagation` — that had explicitly stripped its own
phase-based safe harbor after two prior self-catches). No such hardened,
grace-spent tripwire exists for anything in exp-063's own new machinery.
I accept this ruling without override: extending the Iteration-39
firings' zero-tolerance language to every unrelated Phase-2 registry gap
by analogy would itself be the kind of unargued extension Iteration 39's
own ruling (on the sibling `exp061-thermo-length-scale-staleness` gap)
explicitly declined to make even within the same cycle.

**Forward tripwire adopted, matching program precedent (Iterations 23,
37, 38):** if either new registry entry (below) is not added at this
Phase 3, or if a materially similar gap in either of THESE specific new
entries is found again at Phase 5 or a later iteration, that DOES fire
Checkpoint criterion 4 without further deliberation.

**Not convened.** No Checkpoint criterion fires this cycle
(`phase2_redteam_audit.md` §5, all five explicitly checked). No entry in
`PLAN.md`'s Current-state section beyond the ordinary Iteration-40
summary; Marsh is not notified.

---

## 3. Mandatory-fix docket — applied

1. **NETD/human-eye disclaimer** added verbatim at TD-3, TD-4, and TD-5's
   own table rows in `NOTES.md` (not only in the generic setup section) —
   VISION's flip condition. The disclaimer's own registry entry (Red
   Team's secondary ask, "not blocking this cycle") is queued in `PLAN.md`
   as a standing, non-blocking item — closing the 20-iteration-old gap in
   the rule's OWN mechanical propagation coverage is a separate, larger
   undertaking than this cycle's own scope.
2. **`lab/caveat_lint_config.json` gains `exp063-biot-correction-
   machinery`**: `trigger_terms` for `biot_number`, `front_surface_
   conduction_correction`, `κ_critical`, `0.0897`; `phrase_patterns`
   requiring the NETD disclaimer; `required_sites` = this cycle's
   `NOTES.md` and (once written) `phase4_results.md`. Verified live below.
3. **`lab/numeric_lint_config.json` gains `exp063-cf-bench-vs-witness-
   derivation`** (`derivation_consistency` kind): the module's own
   docstring names exp-062's EM-6/EM-7 R-vs-T drop as its structural
   regression case; this document's own bench-vs-witness dual application
   of one `front_surface_conduction_correction` formula at two length
   scales is a live twin of that exact shape — VISION's flip condition,
   applied.
4. **Generation-side geometry disclosure** added (`NOTES.md`, new
   Idealization 9): `l_geometric_m`'s bench-scale reuse in a role its own
   docstring never licenses, contradicting T9's radial ledger — PHOTONICS'
   flip condition. Confirmed numerically inert for TD-3/TD-4 by Red Team's
   own recomputation; disclosed regardless, per the docket.
5. **Front-colocated-loss bracket endpoint added**, reported alongside
   the rear-only endpoint at every TD-3/4/5 cell (`NOTES.md`, "The
   closed-form front-surface correction") — MATERIALS' flip condition.
   Needs no new code: it is exactly `mixed_length_scale_regime`'s own
   unmodified `dt_ss_full_K`, correction_factor≡1 identically.
6. **Length-legitimacy disclosure** added (`NOTES.md`, new Idealization
   10): witness-scale `L=τ_true/α` has never been run through
   `gas_conduction_h_eff`'s own licensing test, flagged and deferred at
   both Iteration 38 and 39 on this identical lineage — EM's flip
   condition. TD-5's rear-only bracket endpoint is stated as conditional
   on this, not a clean finding.
7. **η_thermal≡1 idealization** added (`NOTES.md`, new Idealization 8) —
   QUANTUM's flip condition.
8. **TD-5's escalation language relabeled**: "Checkpoint-1/2-adjacent,
   requiring escalation" → "a significant realizability-margin finding
   warranting Director/Marsh attention... NOT a Checkpoint-criterion-1/2
   target-constraint result" — Red Team's own new finding (attack 7, not
   raised by any blind seat). Checkpoint criteria 1/2 concern the four
   numbered phenomenon constraints; this instrument cycle scores none of
   them.

---

## 4. Registry entries — verified live

`lab/caveat_lint_config.json`'s new `exp063-biot-correction-machinery`
entry currently FAILs on `phase4_results.md` (does not exist yet — this
is expected and matches exp-061/062's own precedent for a required site
added at Phase 3 before Phase 4 writes it) and is expected to PASS on
`NOTES.md` (the disclaimer is present at TD-3/4/5, verified by direct
grep before this commit). `lab/numeric_lint_config.json`'s new
`exp063-cf-bench-vs-witness-derivation` entry is verified against the
live `NOTES.md` text below. Both re-run and confirmed clean before this
cycle closes (Phase 5, or sooner if Phase 4 lands first).

---

## 5. Final configuration for Phase 4

One item, as the proposal itself scoped (a single literature/analytic
cycle, no co-scored second item unlike exp-062): source κ_CNT-forest
(through-thickness/axial) via the ten committed queries, unchanged from
`phase1_proposal.md` §6. No change to the THERMODYNAMICS-led scope, no
return to Phase 1. `NOTES.md` carries the frozen, amended TD-1..TD-5
bracketed predictions table. Phase 4 executes next: WebSearch only (T18
re-confirmed blocked, standing), scored against the frozen bands.
