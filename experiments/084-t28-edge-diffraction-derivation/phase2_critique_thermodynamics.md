# PHASE 2 — CRITIQUE · THERMODYNAMICS · Panel Iteration 61 · exp-084

## Steel-man (≤150 words)

Idealization 4 ("no absorbing/lossy medium anywhere in this derivation") is
the *correct* idealization for leg (a): the source aperture's tapered
amplitude profile is a soft-source weighting, not lossy material, so
ignoring absorption there is a true statement about the geometry, not an
energy omission. The proposal is honest about scope: it keeps leg (a)
("zero realizability content," no lossy medium at all) structurally
separate from leg (b) (the disk's real `graded_black_shell` rim), rather
than conflating a vacuum calculation with a lossy one. Idealization 7
discloses that the disk's curved-surface re-radiation between the two rim
points is dropped. Best of all, Anchor 2's self-check — the two-stage
composition mismatches the one-stage identity by a *stable* factor of
~2.89× across a 1×–8× convergence sweep, ruled out as discretization — is
exactly the kind of instrument-validation rigor that caught a real defect
before an energy-adjacent number (leg b) could be asserted as fact.

## Sharpest attack (≤150 words)

The proposal never performs, or even names, an energy check. `phase1_
proposal.md` contains zero occurrences of "Poynting," "interception," or
"cross-check" — the twice-deferred joint EM/THERMO energy-interception
item (LOGBOOK Iteration 59→60, flagged as approaching the R8-family
tripwire, "a third consecutive deferral without an explicit reason would
fire it") goes unmentioned, not deferred-with-reason, despite leg (b)
sitting exactly on the question it names: the article rim, where a real
lossy absorber lives. Leg (b) models that rim as a 100%-opaque hard-edge
mask, discarding the one split (absorbed vs. reflected power) the
deferred check exists to bound. The bench's own ESTABLISHED figure for
that absorber is R≤0.2% (0.10% @600nm) — a genuine reflection-echo could
only ever produce a signal bounded near that scale, while leg (b) reports
`ptp_b=8.21×10⁻²`, an order of magnitude larger, with no comparison to
that ceiling anywhere in the file. Only period (R²/rel_dev) was scored;
amplitude/energy scale — the one lever that actually discriminates
"lossless diffraction" from "reflection-echo in disguise" — was never
checked, and the cross-check's own silence should not be read as "not
applicable."

## Verdict: support-with-changes

Leg (a)'s result stands on its own terms — no lossy medium is involved,
so no energy bookkeeping is owed there, and the self-scoring (Anchor 1,
Anchor 2, R5 specificity at 8.3%, honest withholding of leg (b) after
Anchor 2 failed) is genuinely careful work I have no discipline-specific
objection to. But leg (b) is the one place this program's central
energy-vs-mechanism question (T28's "diffractor or reflector?" tension,
and Iteration 60's own "Branch B potentially reopens the absorbed-power
question") actually lives, and this cycle's construction there
structurally cannot answer it: an opaque-mask Kirchhoff idealization
assumes away the absorbed/reflected split rather than testing it, and no
amplitude-vs-reflectance-bound comparison was run. The named
energy-interception cross-check should have been explicitly addressed or
explicitly deferred-with-reason here, not silently absent — on LOGBOOK's
own stated terms this is the third consecutive cycle it goes undischarged.

## Parameter change that would flip my verdict to plain support

Add a mandatory, pre-registered "Anchor 3": compare each leg's predicted
fringe amplitude (`ptp_a`, and `ptp_b` once Anchor 2 is fixed) against the
`graded_black_shell`'s own established reflectance ceiling (R≤0.2%,
0.10% @600nm, LOGBOOK's ESTABLISHED section) as an explicit upper bound on
what a reflection-echo mechanism could produce — and state, one way or the
other, the disposition of the named energy-interception cross-check
(addressed here / genuinely orthogonal, with the reason why) rather than
leaving it unmentioned.
