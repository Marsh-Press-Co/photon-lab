# PHASE 3 — SYNTHESIS · Panel Iteration 23 · Director

*All 24 of Red Team's mandatory-fix docket items (`phase2_redteam_audit.md`)
are ADOPTED. None overridden. This entry states, per PANEL.md's requirement,
which Phase-2 criticisms are accepted and why — the short answer is: all of
them, because Red Team's audit independently re-derived and, for the central
dispute, live-FDTD-verified everything it ruled on, and no seat's critique
survived Red Team's audit in a form that contradicts it.*

## What each of the five blind seats gets credited with, and what changes

- **PHOTONICS** correctly diagnosed the `w_y(450nm, FWHM 2°)=199.33` slip as a
  θ₀=36°-value-in-a-40°-column paste error (the only seat to get this right —
  MATERIALS' "impossible by construction" reasoning was itself wrong, per Red
  Team Attack 14). PHOTONICS' demand to strike the envelope formula entirely
  is **overridden** — Attack 1c shows §2.1's `w_y` formula is exactly correct
  once the source-width fix (item 1) lands; only the source argument was
  wrong, not the formula PHOTONICS attacked.
- **ELECTROMAGNETISM** and **QUANTUM OPTICS** are vindicated on the source-width
  fix (`width = w₀/cosθ₀`) — adopted verbatim, tie-broken by Red Team's own
  live FDTD measurement (Attack 1e: 80.47 measured vs 79.47 target, 1.3%).
  QUANTUM's own reversal of its Iteration-20 prediction is itself superseded:
  Red Team shows the underlying question (A1/A3) is not an experimental
  question at all but an algebraic identity of `beam_divergence_coherent`
  (Attack 2) — QUANTUM's Iteration-20 conjecture is recorded as **mis-posed**,
  not refuted or confirmed.
- **MATERIALS** is upheld on Block C's missing UNOBTANIUM points (item 16,
  binding), the unsourced silicon provenance chain (item 18), the fill-factor
  gap (item 19), and several small slips. MATERIALS' own arithmetic diagnosis
  of the `w_y=199.33` slip is corrected by Red Team, not by this synthesis
  independently — recorded so the record doesn't imply MATERIALS' verdict was
  simply accepted uncritically.
- **VISION SCIENCE** is upheld in full: the "eye-invisible" unfalsifiable
  perceptual leak (item 20, non-negotiable), idealization 9's locus gap (item
  21), the `C_THR` disclaimer-stripping (folded into item 5), and the
  Tier-W-sidecar tripwire's soft-vs-hard framing (item 24, adopted as a
  program-integrity instruction, not a work item this cycle).

## Director's own call on item 24

Red Team is right that carrying the VISION Tier-W sidecar tripwire in prose
("recommended as Iteration 24 Tier-1 #1") repeats the exact soft-form
mechanism this program closed for its sibling item (the aperture check) at
Iteration 22's own close, for the reason Red Team states: a cycle that
hardens the item it delivers and softens the item it defers is how the
fix-docket pattern reproduces itself. **Adopted as a hardened, unconditional
rule, stated here for LOGBOOK propagation at Phase 5 close:** if Iteration 24
closes without VISION's glare/adaptation Tier-W sidecar having been run (by
any lead seat, sourced via WebSearch-snippet-tier per the standing T18
adaptation, or with an explicit renewed-deferral reason that itself survives
a Phase-2 Red Team audit), Checkpoint criterion 4 fires automatically and
immediately — no further debate, no seat vote, no Director discretion,
mirroring the aperture-check rule's own wording exactly.

## Configuration adopted for Phase 4

**Block A** — geometry per docket items 1-4 (`width = w₀/cosθ₀` at every
oblique call; `w_y` formula unchanged, slip corrected to 210.54; table
re-issued per Attack 16 — `N_F` range 0.40-67.5, aperture ratio 2.15×-35.8×;
band-setter replaced by a numerical desk propagation through exp-042's own
`_G0_for`/`field_and_h` Huygens-Fresnel propagator, not the closed form,
which is retained only as a disclosed, measured-accuracy sanity anchor).
Predictions per items 5-12 (A1 re-scoped to a pointing/estimator reading,
`C_THR`'s disclaiming comment carried verbatim; A3 re-scoped to a
desk-verifiable identity check of `beam_divergence_coherent`'s own
synthesised aperture, target-convention mismatch disclosed; A4 dropped, its
premise is false under the fix; A2 re-banded from the numerical propagation;
A7 dropped — conditioning factor 77-300× makes it unusable as a scored
check; the 3-λ sweep's own "no material wavelength dependence beyond fixed
cell geometry" stated explicitly, not left implicit). Gates per items 13-15
(new stage-16 oblique-width gate, 600nm/θ₀=40°/`width`=56.063, target 79.47
cells ≤5%, reference platform named; S16-c's tolerance restated relative;
the sign-convention guard on `B(y)` comparisons recorded as a standing rule
for this block, not merely a one-shift note).

**Block B** — the mixed regime as originally proposed (`dwell/τ_thermal` =
194.176815×, `dt_ss_full` = 3.2930761×10⁻⁵ K), with items 18-19 applied
(silicon identity relabelled `ASSUMED — provenance terminates unsourced
(T18)`, not "sourced"; fill-factor idealization disclosed with a ρC_P
sensitivity row; §2.3's "decided by the conduction length alone" corrected
to the full `ρ C_P L²/(4εσT³L + k_air)` dependence) and item 20 (the
"eye-invisible" claim struck from every locus, replaced with the disclaimed
NETD/detectability language `lab/thermo_sidecar.py` already provides).

**Block C** — extended per item 16 (Host E and r=1.0 added — the full
5-host × 5-ratio, 25-point exp-038 grid, minus Host D's 4 already-committed
exp-045 points = 21 new points, not 24 — see note below), item 17 (C3's
scanned parameter is `dt_sweep`, the ON dwell; C3/C6 relabelled
*verification*, not *test*, of C2's own closed form), and item 22
(`REALIZABILITY_MEMO.md` Amendment 5, recording C2's memory-onset criterion
and the silicon-provenance downgrade).

**Note on item 16's point count.** Red Team's docket text says "+18
closed-form points" for Host E + r=1.0; re-deriving from the actual grid:
adding Host E (4 new r-values already in C1's set, since r=1.0 isn't in C1's
{1e-9,1e-5,1e-3,1e-1}) gives 4 new points at Host E, and adding the r=1.0
column across the 4 existing hosts (A,B,C,D) gives 4 more, plus Host E at
r=1.0 itself (1 point) = **9** new points beyond C1's original 12 (Hosts
A/B/C × 4 ratios), for a corrected-grid total of 12+9 = 21 new points (Host
D's 4 points at r∈{1e-9,1e-5,1e-3,1e-1} were already committed at exp-045 and
are not re-run; Host D at r=1.0 is new). This is computed explicitly in
Phase 4's own code and printed, not asserted here — if it disagrees with
this hand-count the code's own number is authoritative (this synthesis note
is a sanity check, not the source of truth, per this program's own
"computed, not hand-typed" discipline).

All 23 substantive docket items (1-23) are load-bearing for Phase 4's own
code; item 24 is a standing rule recorded for Phase 5/LOGBOOK. Predictions
below are committed to git before any Block-A run executes.

## Falsifiable predictions committed BEFORE any run

Numeric predictions for the corrected configuration are computed in
`run.py` itself (per item 4's "computed once, committed to git" instruction)
rather than hand-typed here a second time and risking a transcription drift
between this document and the code — the exact failure class this program's
own fix-docket-delivery pattern (LOGBOOK.md, recurring across Iterations 13,
14, 15, 17, 20, 21, 22) has caught repeatedly. **House discipline is
satisfied by the commit ORDER, not by hand-duplicating numbers**: `run.py`
computes and prints every P-TH23-* band from the corrected geometry before
Block A's FDTD legs execute, that printed/committed state IS the frozen
prediction, and this file's own commit (predictions, zero FDTD run yet) will
land in the same commit as `run.py`, strictly before Phase 4's FDTD calls
are made — verified explicitly in the shift's own command history.

Qualitative predictions, stated here for the record: (1) Block A's stage-16
gates pass, including the new oblique-width gate at ≤5% (Red Team's own
FDTD run measured 1.3%, so a clean pass is expected, not hoped for); (2) the
numerically-propagated A1/A3/A5 bands are self-consistent by construction
(computed from the same propagator the FDTD legs are validated against) —
the genuine falsifiable content is the FDTD-vs-propagator agreement at the
four new Fresnel numbers (A5), not yet measured beyond Red Team's own two
spot checks; (3) Block B's mixed regime reproduces Red Team's/THERMODYNAMICS'
own hand-verified numbers exactly (194.176815×, 3.2930761×10⁻⁵ K) — a
reproduction, not a fresh finding; (4) Block C's extended grid shows real,
nonzero memory buildup at Host E (unlike C1's all-negative-control original
scope) — Red Team's own Attack 9 predicts Host E at r≤1e-3 sits at
D/τ_k≈0.067, deep inside the C2 memory criterion (D/τ_k<2.54), so a
`ratio>1.05` result at Host E is expected, not a null.

Full setup, cost note, and idealizations: inherited from `phase1_proposal.md`
except where this synthesis and Red Team's docket amend them explicitly, as
enumerated above.
