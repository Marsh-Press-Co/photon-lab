# PHASE 5 — REVIEW · Panel Iteration 31 · Seat: MATERIALS & METAMATERIALS

*Fresh-context review, blind to the other six seats' current-cycle Phase-5
output. Charter: sub-wavelength structure and realizability — published /
plausible / unobtainium-with-parameters. Read: `PANEL.md`, `phase1_proposal.md`,
all five `phase2_critique_*.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `results.json`,
`lab/thermo_sidecar.py`, `REALIZABILITY_MEMO.md` (the live file, at
`experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`, not
top-level), `experiments/037-.../NOTES.md:815-838`, `LOGBOOK.md` excerpts on
Host A–D provenance, and this seat's own prior Phase-5 output at
`experiments/046-.../phase5_review_materials.md` for continuity. T1 escape
route: NONE — this cycle proposes no mechanism, so this review scores
realizability-bookkeeping fidelity, not a candidate mechanism.*

---

## What this cycle actually establishes (verified against live files, not prose)

**Mandatory fix 3 (my own Phase-2 critique's ask) is genuinely delivered in
code, not just promised.** I checked all four loci the task named:

1. `lab/thermo_sidecar.py::mixed_length_scale_regime` (lines 219–280)
   returns, in the same dict that carries `mass_kg` (line 244/258), two
   dedicated keys: `"material_provenance": "ASSUMED -- provenance
   terminates unsourced (T18); see REALIZABILITY_MEMO.md and
   exp-054/NOTES.md idealizations"` and `"mass_fill_fraction_assumption":
   "mass_kg assumes 100%-fill crystalline solid at l_geometric_m --
   undisclosed in the Iteration-31 Phase-1 draft, disclosed here per Red
   Team mandatory fix 3"` (lines 267–273). This is disclosure *at the
   computation site* in the sense that matters — the string travels in the
   same return value as the number, not bolted on downstream.
2. `run.py`'s `MATERIAL_PROVENANCE_NOTE` (lines 69–78) restates the same
   provenance trace verbatim, cites the exact dead end
   (`experiments/037-.../NOTES.md:828-829`, "standard *cited* thermal
   constants," no DOI/handbook), and is written into `results.json` twice:
   once inside `part_a_on_endpoint_mixed_regime.material_provenance_note`
   and once at the root as `material_provenance_note_ALL_CLAIMS`. Confirmed
   by direct read of the live `results.json`.
3. `NOTES.md`'s idealizations list carries the identical flag as "NEW
   (mandatory fix 3, MATERIALS)" (lines 73–78).
4. `REALIZABILITY_MEMO.md` (the real file, `experiments/034-.../
   REALIZABILITY_MEMO.md:206-224`) already carried this exact downgrade
   from Iteration 25 — exp-054 restores it rather than re-deriving it, and
   the restoration is the correct move (this is a citation trace, not a new
   measurement).

So: the specific defect the task asked me to hunt for (fix 3 "only promised
in synthesis, not delivered in code/results") **did not happen this
cycle**. That is a genuine, checkable improvement over the Phase-1 draft,
which had silently dropped the flag (confirmed independently by both my own
blind Phase-2 critique and Red Team's audit, attack 3).

**The physics argument itself is sound and is this seat's own prior
reasoning, now formalized.** `P_abs` (an optical measurement, legitimately
larger than the object) stays on `w_on`; `h_eff`, `mass_kg`, and radiating
area (properties of the physical solid, which cannot exceed its own
footprint) move to `r_out`. That is the correct materials distinction, and
nothing in this cycle's code contradicts it.

## Load-bearing defects found (my own charter, not a restatement of Phase 2)

**1. The "reusable" primitive itself carries no fill-fraction disclosure or
parameter — a capability regression relative to the precedent it replaces.**
`lumped_cube_mass_kg(density_kg_m3, l_geometric)` (`lab/thermo_sidecar.py:203-216`)
computes `mass = density * l_geometric**3` with **no fill-fraction argument
at all**, and its own docstring says nothing about the 100%-fill assumption
— that disclosure exists only one layer up, in `mixed_length_scale_regime`'s
returned dict. A future caller who invokes `lumped_cube_mass_kg` directly
(exactly the "future host at some other article" scenario Red Team's own
attack 4 names) gets a bare density×L³ number with no ASSUMED/fill-fraction
flag traveling with it. This matters materially because
`REALIZABILITY_MEMO.md:225-232` (Amendment 5(b), Iteration 23 Phase-5
close, THERMODYNAMICS' own upheld validity condition) already established
that fill fraction is not a free scaling knob on this model: a fill
fraction below unity *also* lowers κ_eff (Maxwell–Garnett:
κ_eff=k_air(1+2φ)/(1−φ)), which raises Bi=k_air/κ_eff toward 1 and
**invalidates the lumped single-τ model the sensitivity numbers themselves
come from** — "the reassurance is largest precisely where the model is
most invalid" (memo's own words). exp-045/046's informal script explored
this (`dwell/τ_thermal`=97×–19,418× across disclosed shape/fill,
`experiments/046-.../NOTES.md:459,576-599`); the new promoted module
provides **no parameter through which a future cycle could even attempt
that sweep** on the corrected mixed chain. The reusable code this cycle
ships is, on this one axis, less expressive than the one-off script it is
meant to supersede.

**2. `mixed_length_scale_regime` silently drops the graybody-idealization
warning the function it effectively replaces still carries.**
`steady_state_delta_T` (`lab/thermo_sidecar.py:152-164`) carries this
docstring warning verbatim: *"Graybody radiative-equilibrium is itself a
questioned idealization for a dilute vapor/aerosol host (Red Team's exp-033
attack 11) — carried forward unresolved, not fixed by this module."*
`mixed_length_scale_regime` (lines 219-280) does **not** call
`steady_state_delta_T` — it re-implements the identical
`dp_dt = area*(4·ε·σ·T³ + h)` formula inline at line 246, with the same
fixed `emissivity=0.9`, and carries no equivalent warning anywhere in its
own docstring or return dict. This is exactly the "disclosed in prose
elsewhere, not at the point of computation" failure pattern the task asked
me to check for on the fill-fraction axis — it recurs here on the
emissivity/graybody axis, one function away from where fix 3 actually
closed it. Compounding: `netd_disposition`'s `emissivity_correction`
parameter (declared since panel Iteration 20) is still called at its
default 1.0 everywhere in this cycle's `run.py` — the same gap my own prior
seat (`experiments/046-.../phase5_review_materials.md`, ranked-#1 argued
next change) flagged as "a zero-cost, one-line check that removes a
standing 'carried forward unresolved' flag" four cycles ago (Iteration 23
→ 31). It remains unaddressed, and this cycle's own re-implementation of
the formula makes it slightly *less* visible than before, not more.

**3. A quantitative overclaim risk in how this cycle's result will likely
get cited going forward.** The corrected dose-accumulation headline margin
(P-054-4, exact chain) is **8,954.6×** (`results.json`,
`part_b_block_c_rerun.netd_lo_margin_exact`) — this is *smaller*, not
larger, than exp-045's own previously-published headline of **27,080.2×**
(`0.020/7.385465974827066e-7`). The "2–3 orders of magnitude
larger/safer" framing that P-054-6/this cycle's own narrative repeats is
true **only relative to Iteration 25's informal, never-computed guess**
(~38–42×) — not relative to the real, already-committed exp-045 headline,
which this correction actually *shrinks* by roughly 3×. Both figures sit
so far above the 5× UNDETECTABLE floor that no classification moves, and
Red Team's own attack 1 / mandatory fix 1 already forced the scope
correction that makes this distinction possible to see at all — but the
scope-corrected prediction table (P-054-6) states only that the informal
guess comparison doesn't apply; it does not flag that the real committed
headline number went down. A future cycle citing "exp-054 confirmed the
margins are even safer" without checking the actual number would be wrong
in the dose-accumulation case specifically (right in the ON-endpoint case,
where 607× vs. the informally-computed-but-never-labeled 607× is unchanged).
Worth a one-line correction in the LOGBOOK Iteration 31 entry so this
doesn't propagate.

## Does the margin correction change anything about program realizability?

**No — and this cycle does not claim otherwise (T1: NONE).** Thermal
detectability margins, in either direction (607×–8,955× here, or the
previously published 607×–27,080×), have never been the axis on which any
realizability tier in `REALIZABILITY_MEMO.md` was set. The
published/plausible/unobtainium tiers there are set by geometric/optical
parameter ratios (the σ(I)/σ(x,t) mechanism's own r, host, and dwell
parameters), not by whether a resulting thermal signature clears an NETD
band by 600× or by 9,000× or by 27,000× — all three are "so far above the
floor that no realizic host choice would change the classification." This
cycle is exactly what it says it is: an instrument-fidelity correction to a
post-run bookkeeping chain, with zero bearing on which materials could
realize σ(I) or σ(x,t). I independently confirm the proposal's own T1
disposition and find no smuggled realizability claim anywhere in
`run.py`/`results.json` (no `realizability_tier`, no `UNOBTANIUM`/
`PUBLISHED`/`PLAUSIBLE` string appears anywhere in this cycle's output).

## Ranked top candidate directions for Iteration 32+ (this seat's own ranking)

1. **Parametrize fill fraction (and the associated κ_eff/Bi validity check)
   into the promoted `lumped_cube_mass_kg`/`mixed_length_scale_regime`
   code**, restoring the sensitivity-sweep capability the informal
   Iteration-23 script had and the new reusable module lost — this closes
   Amendment 5(b)'s still-open validity condition using code that will
   actually be reused, rather than a one-off script whose numbers cannot be
   regenerated from the new API. Highest priority because it is this
   seat's own charter (what a real, non-idealized solid host can actually
   provide) and because the gap is now inside code explicitly billed as
   reusable/trust-suite-gated.
2. **Route the graybody dp/dt formula through one shared implementation**
   (have `mixed_length_scale_regime` call `steady_state_delta_T`, or hoist
   the warning docstring into both) and **actually compute** the
   `emissivity_correction` sensitivity row this seat scoped as a one-line
   check at Iteration 23 (back-of-envelope: `emissivity_correction=0.1`
   inflates `dt_ss_full` by ≤4× at the mixed regime, dominated by
   `h_conv` since Bi≪1 — comfortably short of threatening even the smaller
   8,955× dose margin, but four cycles of "stated, not computed" is enough).
3. **A genuine sourced citation for the silicon ρ/C_p/κ identity**, closing
   the T18 provenance gap this cycle correctly restores the flag for but
   does not resolve. Lowest priority: the values are physically plausible
   for bulk crystalline Si and no verdict rests on the third decimal place;
   worth doing only because it is now the last unsourced load-bearing
   citation in this program's thermal chain, and T18's WebFetch block
   should not be assumed permanent without periodically re-testing it.
4. (Non-blocking, PHOTONICS-adjacent) Red Team's own non-mandatory
   recommendation — a closed-form Q_ext(x) cylinder check bounding how much
   of `w_on`'s excess over `r_out` is genuine diffraction vs. the
   `iso_xsec_sq` convention artifact — remains queued and untouched;
   relevant to this seat only insofar as it would sharpen what "the
   object's real footprint" means for a sub-wavelength scatterer, which is
   this seat's own recurring question across Iterations 20–31.

## Verdict

**PROMISING.** The core deliverable this task asked me to verify — the
ASSUMED-provenance restoration and 100%-fill disclosure at the `mass_kg`
computation site — is genuinely present in code and results, not merely
promised in the synthesis document, at every one of the four loci checked.
The underlying physics argument (mixed chain: `P_abs` on the optical
length, `h_eff`/mass/area on the geometric length) is correct and is this
seat's own reasoning now formalized into reusable, trust-suite-gated code
for the first time. The margin correction itself has zero bearing on this
program's realizability picture and the cycle correctly claims none (T1:
NONE). Not scored higher than PROMISING because of two real, specific
defects this review adds beyond Phase 2: the promoted primitive functions
carry the fill-fraction disclosure one layer away from where they'd need
it to protect a future caller (a capability regression relative to the
script they replace), and the graybody/emissivity idealization warning
present in the sibling function `steady_state_delta_T` does not carry over
to the new `mixed_length_scale_regime`, silently re-opening a gap this same
seat closed rhetorically at Iteration 23 and that has now gone unaddressed
for four cycles. Neither defect threatens this cycle's own predictions or
any standing classification; both are cheap, well-scoped fixes for
Iteration 32+, not reasons to distrust the numbers delivered here.
