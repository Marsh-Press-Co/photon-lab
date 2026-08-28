# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 62 · exp-085

*Fresh context, blind to any other seat's current-cycle Phase-5 review and to
the fact that a different fresh MATERIALS instance proposed this cycle at
Phase 1. Read in full: PANEL.md, `experiments/084-.../NOTES.md`, and the
complete exp-085 record (phase1_proposal, all five Phase-2 critiques, the
Phase-2 Red Team audit, phase3_synthesis, phase4_derivation.py,
derivation_results.json, NOTES.md). Read from LOGBOOK.md: RULED OUT R1–R10
in full, the ESTABLISHED preamble, and the complete T28 live-thread entry
(Iterations 46–61 in full) plus the Iteration-61 CHECKPOINT entry.*

## Verdict: **PARTIAL**

The cycle's own stated goal — pin leg (a)'s asymptotic period with certainty
— was not achieved, and could not have been: the honest result is that no
such single period exists to pin (Method A/B both read as noise-scale over
the wide domain). That negative finding is real and worth having. But the
positive finding this cycle ships in its place (Method C's "STRONG COHERENT
CHIRP," `ρ=0.882`, `spread=9.26`) is compromised by two things, only one of
which the cycle's own record discloses: the self-disclosed 4/10 null-
contamination pattern (Fix 2's own reliability flag, fired but not acted on
for this classification cell — a real gap in the frozen spec, correctly
flagged in NOTES.md), and a **second, undisclosed defect this review found
independently** (below) that specifically inflates the same headline
numbers. Process discipline this cycle is excellent — seven Red-Team-
mandated fixes, all correctly implemented and independently checked here
against the actual code, not just the prose. The substance is a genuine but
incompletely-characterized negative/boundary result, not a promising lead
and not a clean ruled-out either.

## Independent verification performed

Re-ran pieces of `phase4_derivation.py`'s own logic from the committed
primitives (not accepted from the JSON or the write-up on faith):

1. **Recomputed Method C's `frac_recovered`, `spread`, and `ρ` directly from
   `derivation_results.json::method_c.sub_results`** (37 rows) — reproduces
   `1.000`, `9.2587`, `0.8817` exactly, matching the shipped numbers.
2. **Re-derived Method A's classification inputs**: `P_wide=3.2556°`,
   `R²_wide=0.0128`, circular-shift `45.4%`, R5 specificity `0/60` — all
   confirmed from the JSON, all consistent with "noise-scale, not a real
   tone" as NOTES.md states.
3. **Rebuilt Method C's actual sub-window fits from the raw geometry**
   (loaded `dg048`/`dg065`/`free_period_with_widening` the same way
   `phase4_derivation.py` does, re-evaluated `FastEval` at all 37 `θc`
   centers) and inspected the **`window`/`at_boundary` fields the shipped
   JSON does not carry per-stage** — this is the substantive new finding
   below.

## New finding this review adds: a second, undisclosed source of inflation in the STRONG COHERENT CHIRP numbers

`free_period_with_widening`'s own staged search (`narrow[1,4]→wide[1,15]→
widest[1,60]`, reused verbatim from exp-078, unmodified by this cycle) has a
`chosen`-selection rule: if a stage's fit sits at its own upper/lower
boundary, the loop widens; if **every** stage ends up at boundary, `chosen`
silently reverts to the **first** (narrowest) stage's own boundary value —
not the widest stage's, and with no flag distinguishing "genuinely
converged" from "search exhausted its full [1°,60°] range and still wants
more." I re-ran the raw three-stage search for the ten θc's Method C
null-sampled and found **five of them (θc = 59°, 61°, 63°, 71°, 73°) hit the
boundary at all three stages, including the widest** — e.g. at θc=61°:
`narrow[1,4]→P*=4.0000 (boundary)`, `wide[1,15]→P*=15.0000 (boundary)`,
`widest[1,60]→P*=60.0000, R²=0.9868 (still boundary)`. The function reports
`P*=4.0000°` for this sub-window — the *least*-widened, least-informative
of the three readings — as if it were the converged local period, because
none of the three ever found an interior optimum. After Fix 3's own
`cos(θc)/cos(39°)` re-referencing, these five windows' reported periods
inflate to 6.41°–10.63°, and they cluster at the high-`θc` end that
dominates both `spread` (max/min) and much of `ρ`'s rank correlation. The
other high-`θc` windows that *did* reach an interior optimum (θc=53°,69°,
77°, periods 11.2°–35.0° after correction) are physically real fits, but
each is fit from data spanning **less than one full cycle of its own fitted
period inside a 6°-wide sub-window** — consistent with the fit locking onto
partial-arc curvature of a smoothly rolling-off, non-oscillating segment
(exactly what a scalar diffraction envelope does approaching grazing
incidence) rather than a resolved multi-cycle tone. Both effects point the
same direction: near grazing incidence, the local "period" this machinery
reports is not measuring a real short-scale oscillation at all, it is
measuring how large a period is needed before a straight-ish curve segment
stops looking like it's "at the edge of the search range" — and that
number, not real periodic structure, is what is driving most of `spread=
9.26` and a meaningful share of `ρ=0.882`. This is a **parameter-space**
explanation the proposal/synthesis never considered: it isn't a flaw in
this cycle's own new code (Methods A/B/C are all correctly implemented
per the frozen spec, and Fix 3's `cos(θc)/cos(39°)` correction is applied
exactly as specified) — it's a boundary-search fallback defect in shared
machinery this sub-thread has reused unchanged since exp-078, first
exposed because this cycle is the first to push the widening search hard
into a regime (`θc→80°`, sub-windows with no real oscillation left in
them) where "every stage saturates" actually happens.

## Realizability-scope check (my seat's specific duty this cycle)

Confirmed, by reading `phase1_proposal.md`, `phase3_synthesis.md`, and all
of `phase4_derivation.py` line by line: no material law, permittivity,
admittance, reflectance, or absorption parameter of any kind appears
anywhere in this cycle's own machinery. Methods A/B/C only resample and
refit `edge_diffraction_c_empty_corrected` — a vacuum-only Kirchhoff sum
over the source aperture's own geometric edges, already true of exp-084's
leg (a) and unchanged here. **"Zero realizability content" is correct for
this cycle, verified independently on its own merits, not merely cited.**

One citation-precision issue, not disqualifying but worth correcting before
a future cycle inherits it uncritically: §6 (and exp-084's own T1 section)
cites the framing as "established Iteration 59/60." Iteration 59 did adopt
a "zero realizability content" finding — but for a *different* question
(the PAD-sensitivity confound being a pure scene/domain-geometry fact).
Iteration 60's own MATERIALS seat explicitly **declined to auto-reinstate**
that rule for `P_edge_A`'s causal-origin question, citing genuine
realizability ambiguity between "inherited artifact" and "genuine article-
rim diffraction." Citing "59/60" together reads as if both iterations
endorsed a blanket rule; Iteration 60 in fact pulled back from exactly
that generalization. Not load-bearing here (this cycle's own scope
independently clears the bar), but the next cycle that cites this shorthand
should not assume Iteration 60 blanket-endorsed it — and the trigger
condition for my seat to actually re-engage is worth stating explicitly:
**if any future T28 cycle concludes `P_edge_A` originates from genuine
diffraction/reflection off real (not vacuum) material — the article rim,
the graded-loss boundary, anything with a material law — that is the
moment the realizability bound re-engages**, and it should not be waved
through as "matching the empty-scene precedent" the way the energy-
interception cross-check was silently waved through three cycles running.

## Steel-man

This is a disciplined, honest instrument-fidelity cycle that did exactly
what it set out to do: ask whether a 6°-window null result (exp-084) was a
sampling artifact or a real absence of periodic structure, at zero marginal
FDTD cost. All seven Red-Team-mandated fixes are implemented correctly, not
just claimed — I independently reproduced the Fix-2 null pattern, the Fix-3
`center_deg` correction, and the Fix-5 classification logic straight from
the committed code and they match the write-up exactly. The cycle does not
oversell: NOTES.md states plainly that the STRONG COHERENT CHIRP reading is
contested by its own reliability check and that the spec itself has a
documented gap (no downgrade rule for a non-STABLE classification hit by
the Fix-2 flag). Method A/B's negative result (`R²_wide=0.013`, `45.4%`
null pass) is a genuine, informative finding on its own: it closes off any
hope that "wider and denser" alone rescues a single-tone period-match claim
for leg (a) — a real narrowing of the search space, cheaply bought.

## Sharpest critique

The cycle correctly built in a reliability check for Method C (Fix 2) but
never checked whether the *underlying fitting machinery itself* behaves
sensibly at the extreme end of the domain it was pushed into for the first
time. Five of ten null-sampled sub-windows near grazing incidence never
converge to an interior optimum at any of the three widening stages — the
search wants a period beyond the widest tested range (`>60°`) — yet the
shared `free_period_with_widening` code silently reports the *narrowest*
stage's boundary value as if it were a real answer, with no flag. This is
not a discretization or convention bug like Fix 3's; it's a genuine
non-convergence case masquerading as a converged fit, and it specifically
inflates the two summary statistics (`spread`, `ρ`) that produced this
cycle's headline classification. Given how much weight the classification
places on those two numbers, and given this defect sits in machinery this
sub-thread has reused unmodified since exp-078, it should have been
checked — the `at_boundary`/`window` fields needed for the check are
already computed by every call, just never surfaced past the `chosen`
selection.

## Ranked top-3 candidate directions for Iteration 63's queue

1. **Fix `free_period_with_widening`'s boundary-fallback selection and
   re-score Method C.** When every stage lands at boundary, report the
   *widest* stage's own value with an explicit `NOT CONVERGED (search
   range exhausted)` flag, not the narrowest stage's silently. Re-run
   Method C's 37-window fit under the corrected selection (cheap — this
   cycle's own NOTES.md already timed the full 37-window pass at ~30s) and
   re-score `spread`/`ρ`/classification (a). This is the single highest-
   information, lowest-cost next step: it directly tests whether the
   STRONG COHERENT CHIRP reading survives once the non-convergence
   artifact this review found is removed, or whether it was substantially
   driven by it.
2. **Extend the circular-shift null to all 37 Method C sub-windows**
   (already named in this cycle's own NOTES.md item 2, now known cheap) —
   combine with fix #1, in the same batch, before either number is trusted
   as evidence. Together these two items fully discharge Phase 5's own
   first-named job (the contested classification) rather than leaving it
   as a named-but-unresolved gap a second cycle running.
3. **The joint EM/THERMO energy-interception cross-check, if — and only
   if — Iteration 63 carries a real article-loaded scene.** This cycle's
   own scope-mismatch carve-out (no FDTD, no article) correctly exempted
   it here, per the Iteration-61 CHECKPOINT ruling — but that carve-out
   will not apply again to a scene-bearing cycle. The item is now three
   consecutive T28 cycles named-and-not-run (59, 60 discretionary; 61/62
   structurally exempt); a fourth pass on a scene-bearing cycle without
   running it would be the first *non*-exempt silent deferral since the
   tripwire was written and should be treated accordingly.
