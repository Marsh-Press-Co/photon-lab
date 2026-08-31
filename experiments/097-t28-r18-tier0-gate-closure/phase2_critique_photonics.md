# Phase 2 Critique — PHOTONICS (exp-097, Panel Iteration 74)

*Blind critique. Charter: is the proposal's optical response coherent as
stated, across wavelength and angle? Verified against source, not taken on
the proposal's own word.*

## Steel-man (148 words)

Check 7 is the one item in this docket squarely inside PHOTONICS' own
domain, and it is sound. I read `lab/fdtd2d.py:160–164` directly:
`taper_expected()` reproduces the raised-cosine window (`0.5*(1-cos(π·i/
edge))`, mirrored at both ends) bit-for-bit against the actual
`add_line_source` construction — not a paraphrase. The amplitude taper sets
the aperture's illumination function, which is the physical input to T21's
own Huygens-Fresnel model governing every sidelobe/near-null angular
feature this sub-thread has fought over for nineteen cycles; until now that
axis was entirely unaudited. Check 7 runs across all 16 representative
points (both C/G pair members), correctly re-exercising the pad-arithmetic
risk Checks 3/4 already established, and FI-D is well-designed: it corrupts
only `edge`, leaving `phase`/`sim.lam`/placement untouched, so its
"Checks 1–6 stay CLEAN" prediction is a genuine specificity test, not a
redundant re-catch. Closes a real gap in the gate's own name.

## Sharpest attack (146 words)

Every T28 document since at least Iteration 64 has closed with a "Standing,
unranked, carried forward unchanged" line naming PHOTONICS' own
grazing-incidence validity check and the x-wall wavelength-generality leg —
ten and twenty-two consecutive cycles undischarged respectively, per
exp-096's own Next section and `phase5_redteam_audit.md` §6. I grepped
exp-097's full text for "grazing" and "wavelength-generality": zero hits,
either one. This is the first T28 document in that entire span to drop the
bookkeeping line silently rather than restate it — in a cycle whose own §5
item names itself a "documentation-correction bundle" and whose own R18
compliance header is otherwise meticulous about scope claims surviving
contact with source. A proposal built specifically to close R18-style
"claimed coverage exceeds actual coverage" gaps just committed the same
class of gap against its own standing-items ledger — on the two items that
are literally PHOTONICS' angular- and wavelength-coherence charter.

## Verdict

**support-with-changes.**

## Flip condition

Restore the standing-items line (grazing-incidence + x-wall
wavelength-generality, verbatim) to §9 before Phase 3 freeze. Cheap,
zero-FDTD, one paragraph — but until it's there, this cycle's own
"documentation bundle" claim to close bookkeeping gaps is itself
unverified against its own text, the identical failure shape R4/R18 exist
to police.
