# Phase 2 critique — MATERIALS & METAMATERIALS (blind, independent)

Panel Iteration 31. Critiquing `phase1_proposal.md` (THERMODYNAMICS' lead,
locked-rotation cycle).

## Steel-man

The material-identity reasoning is coherent as far as it reaches: silicon
(doped Si/Ge FCA) is the correct host for Hosts A-D -- already established
over the Iteration-22 PMMA mis-citation, independently confirmed by two
seats -- so reusing that identity rather than re-deriving it is the right
materials move. The core physical intuition is sound: thermal mass,
conducting area, and radiating area are properties of the real solid and
cannot exceed its physical footprint, whereas an extinction cross-section
is an optical measurement that can legitimately exceed geometric size for
a sub-wavelength scatterer. Categorically separating P_abs (an
already-calibrated, separately-measured optical quantity, left on w_on)
from h_eff/mass/area (properties of the physical body, moved to r_out) is
the correct move, and it formalizes a figure (T23's 3.293e-5K) the record
already computed once informally.

## Sharpest attack

The silicon identity this proposal treats as flatly settled was explicitly
downgraded by `REALIZABILITY_MEMO.md`'s own Iteration-25 entry (Red Team
Attack 13 / MATERIALS M3) from "sourced" to "ASSUMED -- provenance
terminates unsourced (T18)": exp-037's cited line reads only "standard
cited thermal constants," and no DOI, handbook, or reference exists
anywhere in exp-037's grep-verified record. The proposal's parameter table
restates ρ/C_p/κ as plain citations with no ASSUMED flag, silently
reverting a load-bearing provenance caveat this exact discipline already
filed one cycle ago. The same memo entry also flags that
`mass_kg=ρ_Si·L³` assigns 100%-fill crystalline silicon to a host the
sidecar elsewhere calls "dilute vapour/aerosol" -- undercutting the
proposal's own claim that r_out is "the one length that is actually a
physical property of the conducting, radiating solid": absent a stated
fill fraction, r_out is a bench EM/geometric radius, not a verified solid
footprint either.

## Verdict

**support-with-changes**

## Parameter change that would flip to full support

Restore the "ASSUMED -- provenance terminates unsourced (T18)" label on
ρ/C_p/κ at every table and results.json key this cycle touches (or
actually source them against a real handbook/DOI before the corrected
chain is treated as load-bearing), and disclose the fill fraction (100%,
as used) at the point of the `mass_kg=ρ·r_out³` claim rather than only in
`REALIZABILITY_MEMO.md`. With that provenance re-flagged in place, the
r_out-vs-w_on bifurcation argument stands on its own physical logic
without silently re-importing a gap this discipline already closed once.
