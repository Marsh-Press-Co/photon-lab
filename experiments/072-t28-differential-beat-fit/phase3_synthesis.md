# PHASE 3 — SYNTHESIZE · Panel Iteration 49 · exp-072
## Director's synthesis: all 15 mandatory fixes implemented, predictions frozen BEFORE any run

Red Team's Phase-2 audit verdict: **PROCEED-WITH-MANDATORY-FIXES, 15 items**
(`phase2_redteam_audit.md`). The Director accepts Red Team's synthesis in
full, including its overrides of three seats' specific remedies (ELECTROMAGNETISM's
`A_q` fix, ELECTROMAGNETISM's wrong-carrier flip comparator, VISION SCIENCE's
sign-invariance gate) — Red Team's own re-derivations for each override are
independently checked below and confirmed correct before being coded. **Zero
further overrides by the Director.** All 15 docket items are implemented in
`run.py`, verbatim to the audit's specification, before this file's commit.

## Pre-registration contamination — Director's disposition (binding, restated from the audit)

Red Team's Phase-2 audit Sec 4 ruled the pre-registration of this cycle
contaminated (two seats computed real numbers on the committed data during
Phase 2) and imposed four binding conditions. The Director implements all
four as code, not prose:

1. Every docket item traces to an argument independent of an observed value
   (audit Sec 4, condition 1) — verified item-by-item below.
2. Net effect is strictly stricter, not looser (condition 2) — the docket
   simultaneously loosens the null (item 1) and tightens three other gates
   (items 3, 6, 10) that bind on the same quantity.
3. **`CONFIRM_UNCERTIFIED`, not `CONFIRMED`, is the only reachable positive
   verdict this cycle** (condition 3) — coded as a hard override in the
   Combined-Verdict branch, unconditionally, regardless of what the booleans
   say. This is a standing rule for THIS cycle only; it does not generalize
   to exp-072's successors, which start with a clean pre-registration.
4. This file, `NOTES.md`, and `phase4_results.md` all carry the disclosure
   paragraph verbatim (already present at the top of `run.py`'s own
   docstring, quoted here for the git record):

   > During Phase 2, QUANTUM OPTICS executed the proposed estimator and both
   > candidate nulls on the real committed data (withholding outcome
   > numbers) and VISION SCIENCE executed the estimator and published
   > outcome-determining numbers (ΔP, z, ρ_c at three carriers). Red Team
   > then independently computed the observed surrogate p-values under both
   > nulls and found the choice between them is outcome-determining between
   > Combined Verdict REFUTED and NEITHER. No threshold was set or moved
   > after any number was computed; every docket item is justified by an
   > argument independent of the observed data (forward simulation, a-priori
   > power tables, algebraic identities) — see `phase2_redteam_audit.md`
   > Sec 4 for the full ruling this cycle operates under.

## Accepted / overridden record (Director's independent check of Red Team's overrides)

Per PANEL.md, the Director must state which Phase-2 criticisms are accepted
and which are overridden, in writing. Red Team already performed this
adjudication (its own Sec 3); the Director's job here is to independently
verify Red Team's three overrides before coding them, not merely restate them.

1. **EM's `A_q` remedy, overridden by Red Team → Director independently
   re-derives and confirms.** EM proposed reporting `|A_q − R_q·x̄|/a` as the
   phase channel. Red Team showed this is `|Δψ|`, an extrapolation to θ=0°,
   ~26σ_u outside the window, and demonstrated it manufactures a spurious
   175°-class artifact on real data where the directly-measured phase
   difference is 6°. The Director re-derived the exact relation
   `A_q = 2a·sinχ`, `χ = πΔf·x̄ + Δψ/2` independently from the same
   trigonometric identity EM used (`cos P − cos Q` product form) and
   confirms Red Team's correction is the exact, non-approximate relation —
   EM's own linearization is the source of the error, not a sign slip.
   **Coded**: `A_q` is never converted to `Δψ`; `phase_channel = |A_q|/a` is
   the reported quantity (see `run.py::analyze_pair`).
2. **EM's wrong-carrier flip, modified by Red Team → Director confirms the
   displacement choice.** EM's original comparator (1.9608°, T21's fringe)
   sits 0.6452 Rayleigh widths from the carrier — verified independently
   by the Director via the same `X`/`Δf_min` arithmetic Red Team and QUANTUM
   both used (`X=0.0813454`, `1/X=12.2933`). A comparator that close cannot
   be diagnostic (QUANTUM's point) but the flip must still gate on
   *something* (EM's point). Red Team's displaced comparator (3.60°, ≥1.5
   Rayleigh widths) is adopted as coded; the 1.9608° run is retained as
   mandatory, explicitly-labeled disclosure only, never gating.
3. **VISION's sign-invariance gate, overridden by Red Team → Director
   confirms the "no correct measurement could pass" argument.** VISION's
   own carrier set included 1.9608°, which Red Team's item 2 above shows is
   not on equal footing with the other two carriers in the set. A gate
   requiring invariance against a carrier the design itself calls wrong is
   not a gate a correct measurement could satisfy. The Director agrees this
   is the right call and implements VISION's underlying finding as
   mandatory disclosure (item 12: ΔP at all four carriers, reported
   unconditionally) rather than as an admissibility gate.

All other requests from all five blind critiques — MATERIALS' `m₀`
provenance fix, THERMODYNAMICS' confound-writing-rule extension, QUANTUM's
restricted null and Holm rescoping, VISION's window-provenance and
`C_empty`-is-not-a-contrast disclosures, EM's `A_q`/wrong-carrier
*diagnoses* (as opposed to the two specific remedies overridden above) —
are accepted without modification, per Red Team's own Sec 3 table.

## Implementation notes (Phase 3 → Phase 4 handoff)

`run.py` implements all 15 items; the mapping from docket item number to
code is documented inline at each corresponding block (search for "item N"
in `run.py`). One genuine implementation defect was found and fixed during
development, disclosed here per the same verify-before-claim discipline
that governs every other finding in this program: the first draft fit each
pair's carrier phase in raw `x = sin θ` coordinates and reused it directly
as the `u = x − x̄`-centered phase `design_matrix()` needs, without the
`w·x̄` shift connecting the two (`x = u + x̄`). This silently misallocated
signal between the carrier and ramp columns and produced `ΔP` values roughly
an order of magnitude too small at every pair — caught by comparing the
tool's own `T_mean` outputs (which matched VISION's and Red Team's
independently-computed values exactly, confirming step 1 was already
correct) against its `ΔP` outputs (which did not match at all, isolating
the bug to the phase hand-off between steps 1 and 2). Fixed by fitting
amplitude and phase directly in `u`-space (`_amp_phase_at`, `run.py`) so no
implicit shift is needed anywhere. This is an implementation-correctness fix
to code that already implements Red Team's fully-specified design — no
threshold, gate, or model was altered; it does not touch the contamination
disclosure above, whose four conditions bind the *design*, not the code
that executes it.

## FROZEN PREDICTIONS — restated from the docket, committed here before Phase 4's official run

The full pre-registered gate/threshold set is `phase2_redteam_audit.md`
Sec 6 (15 items) — not restated in full here to avoid a second
transcription-error surface (MATERIALS' Attack 5 finding, `m₀`). `NOTES.md`
carries the falsifiable-bands summary a reader needs without cross-referencing
the audit. Nothing below may be revised after this commit.

**Expected outcome, stated by Red Team in advance (Sec 7) and inherited
here unchanged**: no pair reaches `RESOLVED` under the fixed design;
Combined Verdict `NEITHER`, for a reason that is itself the cycle's
substantive finding — `R_q`'s non-identifiability against the window's own
unresolved second contributor (T21's fringe) and against its own carrier
choice, a limit the absolute-period route (exp-071) never got close enough
to the resolution floor to even encounter. This expectation is recorded
as a pre-registered forecast, not a target — the Combined-Verdict logic in
`run.py` is a fixed boolean function of the docket's gates and does not
reference this paragraph.
