# Phase 5 review — MATERIALS & METAMATERIALS

Panel Iteration 22 · exp-045 · fresh context, independent of this cycle's own
Phase-2 critique (`phase2_critique_materials.md`) — this review re-verifies
the fix from scratch rather than recalling the catch.

## Charge (1) — is the silicon citation fix actually correct this time?

**CONFIRMED, exactly.** `run.py` defines:

```
DENSITY_SI_KG_M3 = 2330.0
C_P_SI = 700.0
K_SI_W_MK = 148.0
```

with the source comment pointing at `experiments/037-fca-combined-media-
literature-check/NOTES.md` line 828–829. I read that passage directly
(not taken on trust from `run.py`'s own comment or from NOTES.md's
retelling): exp-037's THERMODYNAMICS capped estimate states, verbatim,
*"Using silicon's standard cited thermal constants (ρ≈2330 kg/m³, c_p≈700
J/(kg·K), κ≈148 W/(m·K))..."* — all three numbers match `run.py`'s constants
digit-for-digit. `results.json` confirms the same three values propagate
into `block_b...material_identity` unchanged. This is a real fix, not a
relabeling with new numbers pasted in — the source passage genuinely
supports exactly what's coded.

One inherited caveat, disclosed already and not new to this cycle: exp-037's
own figures are themselves "standard cited" textbook constants, not
independently re-sourced against a primary reference this cycle (T18's
WebFetch block, still standing, ninth-plus consecutive shift). The fix
closes the *fabrication* problem; it does not (and does not claim to) close
the *primary-source* evidentiary-tier ceiling T18 names program-wide.

## Charge (2) — is the fabricated PMMA citation actually gone?

**Gone from every load-bearing / live path. Traces remain only as disclosed
history, correctly framed.** Specifics:

- `run.py` (the executed script): no `DENSITY_PMMA`/`C_P` PMMA constant
  exists anywhere in the live computation. Every `PMMA` string I found (11
  hits) is inside a docstring, a code comment, or a `results.json` output
  field explicitly labeled `superseded_material` / `phase1_defect_note` /
  `biot_disclaimer` — i.e. text that names PMMA specifically to explain
  *why it was replaced and that its citation didn't check out*, not text
  that relies on it. This is the correct pattern, not a residual bug.
- `results.json` (the committed numeric record): same pattern — PMMA
  appears three times, all inside disclosure fields carrying forward the
  same superseded-material framing. No numeric field is computed from a
  PMMA constant.
- `phase1_proposal.md`: still contains the original fabricated citation
  string verbatim ("the most commonly cited photochromic-dye host polymer
  in this program's own literature surveys, T17/T18, exp-036/037"). This is
  **intentional, not an oversight** — `NOTES.md`'s Phase-3 synthesis states
  explicitly that the Phase-1 draft is "left unedited as the historical
  record of what Phase 1 proposed and Phase 2 critiqued," consistent with
  this program's T10 "flag, don't rewrite" convention for pre-run fixes.
  I independently re-verified via `grep -rl PMMA` across the full repo
  (matching Red Team's own Attack 4 check): zero hits outside exp-045's own
  five files, and zero hits in exp-036/037/038 themselves — the citation
  was fabricated, confirmed a second time, independently.

**One small process flag, not a defect:** `phase1_proposal.md` itself
carries no in-file marker that it is superseded — a reader who opens only
that file (e.g. arriving via a search hit on "PMMA" or "density_PMMA")
would see the fabricated citation presented as live, without the
superseding context that lives one file over in `NOTES.md`. Given the
severity class here (a fabricated citation, not an ordinary revision), a
one-line "SUPERSEDED — see NOTES.md Phase 3" banner at the top of a Phase-1
draft would be a cheap, worthwhile addition to this program's own
convention whenever Phase 2/3 finds a fabricated source, not just a wrong
number. Not mandatory for this cycle's own verdict — the historical-record
framing is defensible as written and clearly stated in NOTES.md — but worth
adopting going forward.

## Charge (3) — does this cycle's re-derivation move any REALIZABILITY_MEMO.md verdict?

**No, independently confirmed by reading the full memo file myself, not by
trusting NOTES.md's or my own Phase-2 critique's restatement of the claim.**
`REALIZABILITY_MEMO.md`'s verdict section, its Amendment 2 consolidated
table, and its Amendments 1/3/4 are built entirely from two axes:
**D_req** (σ_on/σ_off dynamic range) and **operating irradiance** against
published nonlinear-absorber figures. I searched the memo end-to-end for
`mass_kg`, `tau_thermal`, `h_conv`, `NETD`, and `Biot` — none of these
strings, or their underlying concepts, appear anywhere in the file. Every
UNOBTANIUM-WITH-PARAMETERS verdict (RSA, TPA, photochromic, VO2,
TPA-cascade FCA, linearly-pumped FCA, ENZ, graphene's disqualification,
combined SA+RSA media) rests on dynamic-range or irradiance gaps 1–14
orders of magnitude wide. exp-045's Blocks A/B re-derive a thermal *time
constant* and a detectability *margin* for an article this memo already
rates unobtainium on a completely different axis — even a 10×, 100×, or
1000× shift in `tau_thermal_s` cannot touch a verdict that isn't a function
of it. The claim holds, verified from the primary document, not asserted
because two other files already say so.

## Charge (4) — a realizability angle in Block C worth flagging

**Yes — one genuinely new observation, not raised by this cycle's own
Phase 1–4 record as a realizability finding, though the raw number is
right there in `results.json`.**

Block C tested population-memory dose accumulation at **Host D only**, all
4 ratios, at the real *witness* dwell (`dwell_central` = 66.7 ms — the
actual flashlight-sweep duration this program has used since exp-043, not
an arbitrary round number). Result: `max_periodic_over_first_ratio_0.5tau =
1.4509`, comfortably inside the predicted [1.2, 1.8] band and
order-of-magnitude consistent with exp-038's own 1.4–1.6 finding — but
exp-038's finding used a *different*, admittedly arbitrary pulse duration
(0.1 s). `REALIZABILITY_MEMO.md`'s Amendment 3 already flags Host D (along
with Host E) as exactly the pair this memo's own tier labels call
least-realizable on the D_req axis — but Amendment 3, per Red Team's own
Iteration-15 tempering, characterizes the memory-buildup finding as
*"substantially a near-mechanical consequence of exp-038's own fixed
pulse-duration parameter... landing inside the same decade as this memo's
own host-lifetime grid — not a fully independent empirical discovery."*

exp-045's Block C is, functionally, the independent re-test that tempering
called for and Amendment 3 never got: a **second, physically-motivated**
(not decade-matched-by-construction) pulse duration, at the **same** host,
reproducing **comparable-magnitude** memory buildup. That weakens the
"constructed, not surprising" reading Amendment 3 currently carries — two
different, independently-chosen dwell timescales both show real Host-D
memory buildup, which starts to look like a property of Host D's own slow
`k_r`, not an artifact of matching exp-038's particular 0.1 s choice to the
host-lifetime grid's own scale.

**Flag for a future cycle (candidate REALIZABILITY_MEMO Amendment 5,
MATERIALS- or QUANTUM-appropriate depending on lead rotation):** run Block
C's own check across the **full** 16-point host/ratio grid (not Host D
alone) at the witness dwell, and ask whether memory-buildup magnitude
correlates with each host's own D_req/irradiance realizability tier. If it
does — i.e. if the hosts that are *already* least realizable on the
dynamic-range axis are *also* the ones most prone to accumulate dose across
repeated sweeps — that would be a structural, not coincidental, coupling
between two axes this memo currently treats as independent, and it would
sharpen (not create) the UNOBTANIUM-WITH-PARAMETERS verdict rather than
open a new escape route: it closes off the "maybe a slower, more
realizable host avoids the memory problem" hope by showing the two
problems point the same direction. This does not itself move any verdict
today — Block C never touches D_req or irradiance, per charge (3)'s own
answer — it is a candidate *next* check, not a finding this cycle already
delivered. Still bounded by the same NETD-is-not-a-human-threshold caveat
this whole program carries: nothing here bears on constraint 3/4 directly.

## Independent spot-check of the numbers behind this review

I re-ran the derivation chain by hand from `run.py`'s own literal
constants and cross-checked against the values Red Team's audit reported
(without simply copying Red Team's table): `w_on`-consistent
`dwell/τ_thermal` = 21.24× (silicon, `w_on`-consistent) and `Bi(silicon) =
1.757×10⁻⁴` at both length regimes (confirming the algebraic
length-invariance Red Team's Attack 6 proved). Both match `results.json`
to displayed precision. I did not find any new arithmetic defect beyond
what the committed record already discloses.

## Verdict for the cycle

**PROMISING.** The panel process did exactly the job it exists to do: a
real, load-bearing defect (fabricated citation + mixed length scales) was
caught pre-run by five blind critiques and confirmed/extended by Red Team,
fixed before any commit, and the corrected numbers were actually re-run
into `results.json` rather than merely described in prose (closing the
exact "claimed-fixed-but-not-delivered" pattern Red Team flagged as a
program-integrity risk). The headline physics conclusion — the
intermediate-dwell coupled-kinetics-thermal regime does not threaten any
UNDETECTABLE verdict this program has issued, across 2080 sweep points and
a genuine population-memory check — survives every correction intact.
The one disclosed cost (dwell/τ_thermal at the primary regime, 21.2×, sits
below the informal `N_TRANSIENT_TAU=25` comfort heuristic, weaker than the
Phase-1 draft's own buggy 126.7× headline) is real but does not flip any
actual classification, since Block A always uses the exact closed form,
never the heuristic. Nothing in this cycle touches `REALIZABILITY_MEMO.md`'s
governing axes, so it neither strengthens nor weakens this program's
central UNOBTANIUM-WITH-PARAMETERS finding — it is, correctly, scoped as
pure instrument-fidelity work on an article already known not to cloak
anything.

## Ranked top-3 candidate directions for Iteration 23 (my own picks)

1. **QUANTUM's aperture-consistent single-coherent-mode beam check.** This
   is a *self-imposed* Checkpoint-4 tripwire, already deferred twice
   (Iterations 19→20→21) and explicitly flagged in this cycle's own
   NOTES.md as becoming a **third** deferral — an automatic Checkpoint-4
   firing under this program's own rules — if not run at Iteration 23.
   Highest-priority pick on process grounds alone, independent of my own
   discipline: program-integrity tripwires that fire automatically should
   not be allowed to fire through inattention.
2. **Move the RSA/TPA/FCA literature check from WebSearch-snippet
   synthesis to primary-source verification (T18).** This is the single
   standing item most load-bearing for MY OWN charter: every
   UNOBTANIUM-WITH-PARAMETERS verdict in `REALIZABILITY_MEMO.md` — the
   central materials-realizability finding of the whole program — still
   rests on an evidentiary tier this memo itself names as the reason it
   has not escalated to a Checkpoint-2 finding (a proven mechanism-class
   boundary). T18's WebFetch block has now stood 9+ consecutive shifts;
   worth a dedicated push (alternate egress route, a different search
   tool, or an explicit escalation to Marsh) rather than another cycle of
   re-confirming the block exists.
3. **Extend Block C's dose-accumulation check to the full 16-point
   host/ratio grid at the witness dwell, scored against
   `REALIZABILITY_MEMO.md`'s own per-host tier labels** (this review's
   charge-4 finding, above). Cheap — reuses Block C's own code path,
   already gated, zero new FDTD — and directly tests whether
   memory-buildup risk and dynamic-range shortfall are structurally
   coupled or genuinely independent axes, closing a real open question
   Amendment 3 left tempered-but-unresolved.

Deferred but still live, not forgotten: T21's contamination-risk re-score;
VISION's Iteration-23 glare/adaptation Tier-W tripwire; PHOTONICS' R3
recheck of Block C's (exp-043's, not this cycle's) 0.45% flatness claim;
the `realizability_tier` de-duplication housekeeping item.
