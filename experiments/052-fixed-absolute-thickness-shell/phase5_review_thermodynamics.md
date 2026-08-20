# PHASE 5 — REVIEW · THERMODYNAMICS (fresh cold read) · Panel Iteration 29 (exp-052)

*Fresh sub-agent. No memory of Phase 1/3 (this cycle's own lead seat was
THERMODYNAMICS, but that context does not carry forward — this review is
built entirely from the committed record: PANEL.md, LOGBOOK.md's Ruled Out
+ Live Threads (T5, T22, T23, T24 read in full), PLAN.md's Current-state
and LOCKED Iteration-29 entry, and the complete exp-052 record.*

## Reading

exp-052 executes PLAN.md's unconditional Iteration-29 trigger: build the
fixed-absolute-thickness `graded_black_shell` variant (`r_in = r_out − 48`,
`sigma_max = 0.5` fixed, not rescaled) and measure its own ambient contrast
`C`, as the direct test of MATERIALS' 21-iteration-old realizability claim
(fixed-thickness coatings vs. the self-similar family's divergent
0.31–0.92m witness-scale thickness). Phase 2 returned five independent
support-with-changes critiques; Red Team verified all five real and
load-bearing, added three new findings (the reused self-similar comparator
was silently HOLLOW-core — the exact defect exp-031 fixed elsewhere but
never propagated back — plus a transcription error and an R-gate-scope
disclosure), and issued PROCEED-WITH-MANDATORY-FIXES with a 9-item docket.
Phase 3 accepted all nine, with one Director-level redesign: Red Team's
own item 3 (a `radial_absorbed_power` ledger check testing whether T9's
"core is energetically incidental" null survives at this construction's
much larger `r_in/r_out` ratios, 0.692/0.846 vs. the only-ever-tested
0.385) was replaced with a cheaper substitute — a direct PEC-cored-vs-
hollow **ambient-contrast** comparison at θ=0, because exp-031's own
`run_thermo` carries a live `NotImplementedError` for this scene class.

**The load-bearing catch for this review, verified directly against the
repo, not assumed from the task framing:** the Phase-1 proposal's own
§8 P-5 was explicitly the THERMO sidecar — `lab/thermo_sidecar.py`'s
established-ratio branch, `ΔT_ss` vs. the sourced 8.6–100mK NETD band,
predicted UNDETECTABLE, "falsified if... closes to within 10× of NETD."
Red Team's Phase-2 audit (Attack 8) evaluated that *exact* P-5 and found
it near-unfalsifiable — every prior sidecar verdict cleared NETD by
>100×, this construction changes only geometry at fixed already-tiny
irradiance, "nothing plausibly closes even one order of magnitude" —
ruling REAL, MINOR, and recommending (not blocking) that P-5 be
relabeled as an expected, low-information confirmation rather than run
as a genuine test.

**That recommendation was never acted on, in either direction — because
Phase 3 silently reused the P-5 label for something else entirely.**
`phase3_synthesis.md` item 3 replaces Red Team's *radial-ledger* proposal
(a different, new item, not P-5) with the core-fill ambient-C check; that
substitute check is then written into `NOTES.md` **as P-5** ("P-5
(core-fill check, fix 3, θ=0 only)"), with no sentence anywhere stating
that the original THERMO-sidecar P-5 was dropped, deferred, or
disposed of. `phase3_synthesis.md` even asserts "predictions P-0 through
P-5" as if the set were unchanged. I grepped `run.py`, `design_geometry.py`,
`results.json`, and every phase*.md file for `thermo_sidecar`/`ΔT`/`NETD`:
**zero hits outside `phase1_proposal.md` and the Red Team audit.**
`results.json::fit` contains `C_fixedabs`, `C_selfsim`,
`core_fill_delta_theta0`, and the P-1/P-2/P-3 verdicts — no `dt_ss`, no
NETD comparison, nothing from `lab/thermo_sidecar.py` at all. **No energy
sidecar was computed for this cycle's headline result.** This is not a
disagreement about interpretation; it is a verifiable absence in the
committed artifacts, and it is exactly the failure mode PANEL.md's
"flag, don't silently rewrite" convention and house rule R4 exist to
catch — a charter deliverable (mine) disappeared under a label that
still reads as if it were honored.

## Physical meaning

The question worth asking is not just "was the sidecar run" but "does
the established UNDETECTABLE pattern obviously survive," since a
missing check is only urgent if the physics plausibly moves.

**T22's own algebraic result is the right lens, and it argues the
verdict most likely survives — but not "obviously," and not for the
reason the missing check would have needed to confirm.**
`steady_state_delta_T = I·ratio/(4εσT³+h)` is provably **area-
independent** (PHOTONICS, T22): it depends on the absorbed-vs-incident
power *ratio* and the effective heat-loss coefficient, not on the
object's total absorbing area or total absorbed power. A larger
fixed-absolute-thickness object at r=312 intercepts more absolute
watts than at r=78 (consistent with the observed deepening
−0.72087→−0.84032), but its radiating/convecting surface also grows in
step — in the lumped-capacitance model, the two scale together and
`ΔT_ss` stays flat. **If that were the whole story, growing absolute
absorbed power would not, by itself, threaten any prior UNDETECTABLE
verdict**, and a THERMO seat could plausibly wave this cycle through
without a new number.

**But the ratio T22's formula treats as an input — `σ_abs/σ_ext = 0.51`
— is exactly the quantity this cycle's own Idealization 4 flags as
*unverified for this geometry*, and Red Team's own Attack 3/6a
sharpens why that matters here specifically.** Every prior sidecar
citation (exp-043/044/045) used hosts at or near the self-similar
family's fixed `r_in/r_out = 0.3846` — the one ratio T9 ever actually
measured the "core is energetically incidental" null at
(`Δσ_abs/σ_ext = 1.56×10⁻⁶`). This cycle is, in Red Team's own words,
"the first proposal in this program's history to build an object above
that ratio at all" — 0.692 at r=156, 0.846 at r=312. **The core-fill
check that WAS run (the redefined P-5) does not close this gap**: it
measures whether a PEC core vs. a hollow interior changes the
*ambient-contrast appearance* `C` (found negligible, ~10⁻⁶) — a
scattered-field/visibility question. It says nothing about whether the
*fraction of incident power the shell absorbs vs. lets through to
whatever fills the core* — the energy-partition ratio the thermal
sidecar's `ratio` input actually needs — still sits near 0.51 at these
much thinner shell-to-radius fractions (30.8% at r=156, down from
61.5% at r=78). A thin shell wrapped around a much larger core is a
different absorption/leakage regime than the one T9 characterized; the
appearance check and the energy-partition check are correlated but not
the same measurement, and only the appearance one was run.

**So: the area-invariance argument is a real reason to expect the
verdict survives, not a reason to assume it does.** The one input that
would make the argument airtight (the ratio, at this specific
r_in/r_out) is the same parameter this program has never tested past
0.385 — and this cycle deliberately pushed past it for every other
purpose (the whole point was testing new geometric territory) while
implicitly assuming, by omission, that the thermal input carries over
unchanged. That is an inconsistency in how much scrutiny different
quantities got this cycle, not a physics argument that the pattern
must hold.

## Argued next change

**Run the existing, already-trust-suite-gated `lab/thermo_sidecar.py` on
exp-052's own fixed-absolute-thickness object at r=156 and r=312,
honestly, before this cycle's own thread entry closes.** This is
analytic, zero-FDTD, cheap by this program's own cost conventions (the
same class of check PANEL.md's expressibility contract designed to be
free), and restores a charter deliverable that silently went missing
under a label collision rather than a disclosed scope cut. Two parts:

1. **Immediate, minimal:** compute `ΔT_ss` at r=156/312 using the
   T23-adopted mixed `h_eff` convention (power on `w_on`, conduction/mass
   on `r_out`) and the inherited 0.51 ratio, **explicitly flagged in the
   output** — exactly as Idealization 4 already discloses — as carrying
   an untested ratio at this geometry. This at minimum puts a number on
   the record instead of a silent absence, and lets a reader see how much
   margin (if any) exists before the ratio-validity question would
   actually matter.
2. **The harder, correctly-deferred follow-on:** Red Team's *original*
   item-3 proposal — a `radial_absorbed_power`-style ledger check that
   actually measures σ_abs/σ_ext at r_in/r_out=0.692/0.846 rather than
   inheriting T9's 0.385-only figure — was right to defer this cycle (no
   validated `box`/`ref` convention exists for the ambient/line-source
   scene class; building one under time pressure risks reproducing
   exp-031's own diagnosed failure mode) but it should not be dropped
   permanently. It is the one measurement that would make part 1's
   flagged input an actual verified number instead of a carried-over
   assumption, and it is the natural THERMO-owned instrument gap this
   cycle's own new geometric regime exposes.

This is not a claim that the UNDETECTABLE pattern is in danger — the
T22 area-invariance argument is a legitimate reason to expect it
survives. It is a claim that a charter-owned, cheap, already-built
check was silently substituted rather than disclosed as skipped, and
that the substitute (an appearance check) does not answer the question
the sidecar exists to answer (an energy-partition question) at a ratio
this program has never independently verified.

## Ranked top-3 (Iteration 31+ — Iteration 30 already LOCKED to VISION's stage-10 instrument)

1. **Complete exp-052's own THERMO sidecar** (this review's proposed next
   change, above) — closes a real, verifiable gap in THIS cycle's own
   record, cheap (analytic, no FDTD for part 1), and the one item that
   makes the "does the UNDETECTABLE pattern survive" question answered
   rather than argued.
2. **Re-validate the coherent-vs-incoherent ambient-sum bridge gate at
   shell-fraction 30.8%** (exp-052's own Accepted-Fix item 7, explicitly
   left open by the Director as "genuinely open, not resolved this
   cycle," QUANTUM's Phase-2 finding, Red-Team-confirmed REAL and
   LOAD-BEARING). This bears directly on whether the incoherent-sum
   instrument that produced this cycle's own headline CONFIRMED P-1/P-2
   results is even validated at the geometry it was scored on — the
   bridge gate has only ever been checked at 61.5% (where the two
   families coincide by construction), never at the 30.8%/15.4% this
   cycle's own mandatory result depends on. A trust gap on the
   measurement instrument itself outranks most content questions.
3. **The genuine FDTD `ABSORB` sweep at GEOM78** (PLAN.md's own queued
   item 1, near-unanimous across four seats, carried unrun across
   Iterations 26–28, flagged as "approaching unconditional-trigger
   territory if deferred again"). Not specific to exp-052, but the
   longest-standing, most broadly-supported open item in the current
   queue, and this cycle did nothing to advance or displace it.

Also noted, not ranked: Red Team's Attack 6a in exp-052 (the self-similar
comparator's own hollow-core history, only PARTIALLY closed here via a
fresh N9-ambient PEC-cored re-run — Attack 6a's broader point, that the
comparator side of every P-1/P-2 delta carried an unresolved question
until this cycle fixed it, is now closed for r=156/312 but was never
closed for exp-030's own originally-published `results.json`, which
other threads may still cite uncorrected).
