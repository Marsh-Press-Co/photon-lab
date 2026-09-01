# Phase 2 Critique — ELECTROMAGNETISM

## Steel-man

Tier 2 Leg B correctly treats `observer_record`/beam-behind as never
validated on this bench's actual source geometry rather than assuming
continuity, invoking R8 explicitly (an unverified independence argument
is insufficient when an affordable check exists). It follows this
program's own established discipline for exactly this defect class:
`widths_direction_corrected` (exp-087/091) already required a
caller-side correction, not a `lab/` edit, when a flux primitive's
internal directional convention didn't match a bench's real propagation
sense — this generalizes that precedent to `emit.observer_record`.
Crucially it does not merely assert the fix works: it pre-registers a
mandatory, same-cycle, zero-marginal-cost empty-scene validation gate
(R18's "new territory needs its own control") before any article-loaded
reading is trusted, and it names the correctness of the mirror as an
open question for Phase 2 rather than burying it (§7, item 2).

## Sharpest attack

§2 Leg B (ii): `observer_record_t28` "flip[s] the captured Ez/Hy arrays
along x (`a[::-1,:]`)" — identically for both fields, no separate sign
correction. Checked against `emit.py`'s stated relation
(`Ez=a++a-`, `Hy=-(Skx/w)(a+-a-)`): Ez is the TMz true-vector
component, mirrored correctly by bare index reversal; Hy is the
pseudovector partner — a valid mirror needs Hy ALSO sign-flipped, not
just re-indexed. `Hy(x)→+Hy(nx-1-x)` keeps the wrong impedance sign.
Working this through `observer_record`'s own algebra for a bare
-x-travelling wave (the empty-scene beam) gives `a_fwd=0`, `a_bwd`=full
beam — the §4 "PASS... reads near the camera floor" prediction will
instead read near the FULL beam as spurious backscatter, and
`p_forward_total`≈0 will likely blow up the normalization rather than
pass quietly. This program's precedent for this defect class
(`widths_direction_corrected`; `observer_profile`'s `-flux_profile_x`)
is a scalar sign/label correction, never an array mirror —
`observer_record_t28` should match it: run unmirrored, swap which of
`p_fwd`/`p_bwd` is called "return," sidestepping the pseudovector risk.

## Verdict

**Support-with-changes.** The design is sound and the mandatory
empty-scene gate (§4, item 2) is very likely to catch this defect and
correctly HALT per the proposal's own contingency — so this is not a
silent-corruption risk to the program. But it is a foreseeable, cheap,
zero-FDTD fix that should be made before Phase 3 freeze rather than
discovered by burning the HALT: it directly answers §7's own open
question 2 (the mirror as specified is not a correct fix; a direct
re-derivation — the fwd/bwd label swap on unmirrored data, exactly
`widths_direction_corrected`'s own idiom applied here — is required
instead).

## Parameter change that would flip the verdict

Replace `observer_record_t28`'s array-mirror with: call
`observer_record` unmirrored at the real `plane_x`, then read the
"return" signal from `aux["p_forward_total"]`/the `a_fwd`-built flux
(not `a_bwd`) and the "reference/forward" power from `p_bwd`'s own
total — a pure label swap, no field-array edits. With that one change
committed, verdict → **support**.
