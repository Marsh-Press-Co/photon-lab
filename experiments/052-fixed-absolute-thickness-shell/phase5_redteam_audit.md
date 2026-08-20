# RED TEAM — Phase 5 Audit, Panel Iteration 29 (exp-052)

*Fresh sub-agent, last to read, everything in hand: `PANEL.md` in full;
`LOGBOOK.md`'s RULED OUT (R1–R5), LIVE THREADS T1–T24 in full, and the
complete Iteration 7, 8, and 28 entries verbatim; `PLAN.md`'s Current-state
section and the LOCKED Iteration-29/30 entries; and the complete exp-052
record — `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`design_geometry.py`, `run.py`, `results.json`, and all six
`phase5_review_*.md` files. Every load-bearing number below was
independently recomputed from `results.json` or from the cited source file
by direct execution/grep, not copied from any seat's prose — per this
program's own verify-before-claim discipline.*

## 0. What this cycle is, and what it is not

exp-052 executes `PLAN.md`'s unconditional, 21-iteration-deferred
Iteration-29 trigger: build the fixed-absolute-thickness `graded_black_shell`
variant (`r_in = r_out − 48`, `sigma_max = 0.5` held fixed, not rescaled) and
measure its own ambient contrast `C`, as the first direct measurement (not
argument) of MATERIALS' Iteration-7 realizability claim against T13/T14's
"wrong-direction asymptote." T1 escape route: **None**, correctly declared
and honored throughout — no constraint-3/4 PASS/MARGINAL/FAIL language
appears anywhere in the record, and none should. Nothing here is scored
against Checkpoint criterion 1 or 2's "constraint metric" language for that
reason, stated up front.

Phase 2 returned five independent support-with-changes verdicts; Red Team's
own Phase-2 audit found all five real and load-bearing, added three more
(most consequentially: the reused self-similar comparator was silently
HOLLOW-core, the exact defect exp-031 fixed for a different diagnostic and
never propagated back), and issued PROCEED-WITH-MANDATORY-FIXES with a
9-item docket. Phase 3 accepted all nine — eight as specified or via Red
Team's own offered cheaper alternative, one (item 7, the coherent-vs-
incoherent bridge gate) explicitly disclosed as an **open, unresolved scope
limitation**, not silently cleared. That single disclosed gap is the seed of
two of this Phase 5's most consequential findings, below.

## 1. Independent verification of the six seats' convergent findings

Each finding is restated, independently re-derived against the actual repo
(not any seat's prose), and ruled real/load-bearing, real/minor, or
overstated — per this task's own standard.

### 1a. PHOTONICS — the deepening rate is decelerating

**Claim:** the `1+C` residual-removal ratio is 0.69 at r=78→156 and only
0.83 at r=156→312 — the same qualitative signature (a deepening step that
flattens with scale) that historically preceded T14's own discovery.

**Independently recomputed** from `results.json::fit` directly:

```
1+C(78)  = 0.27913153395504553
1+C(156) = 0.19331823272437
1+C(312) = 0.15968387873004997
residual removed 78→156:  0.08581330123067554
residual removed 156→312: 0.03363435399432002
ratio 156/78  = 0.6925703806561108   (≈0.69)
ratio 312/156 = 0.8260156141491561   (≈0.83)
```

Exact match to the cited figures. A naive "fixed-width leak channel becomes
a shrinking 1/r_out fraction" argument predicts each doubling should roughly
*halve* the residual; the first step (0.693) comes close, the second
(0.826) falls well short. This is a real, reproducible deceleration, on only
three points.

**Ruling: REAL, LOAD-BEARING as a coherence caveat, NOT as a falsification.**
None of P-1/P-2/P-3's own pre-registered thresholds are threatened — the
measured deepening clears them by 17–21× — but PHOTONICS is correct that a
2–3-point family scored only against inequality thresholds cannot
distinguish "converges to −1" from "converges to a C_∞ closer to −1 than the
self-similar family's, but still short of it." See 1b, immediately below,
for the quantitative version of exactly this concern.

### 1b. ELECTROMAGNETISM — the sqrt-law fit's C_∞ still falls short of −1 by 0.12–0.16

**Claim:** fitting `C = C_∞ + B·√(z/z_R)` to the fixed-absolute family's own
three points gives `C_∞ ≈ −0.87` to `−0.88`, still short of the −1
geometric-shadow ceiling by 0.12–0.16 — T14's puzzle is relocated, not
resolved.

**Independently re-derived**, using exp-030's own established idiom (exact
2-point solve on 156/312, r=78 held out as validation; and a 3-point
least-squares check), against `design_geometry.py`'s own `GEOM` z/z_R
values:

```
2-point fit (156,312):  B=+0.6056  C_inf=-0.8739   |C_pred(78)-C(78)|=0.0186
3-point least squares:  C_inf=-0.8832  B=+0.7251   (residuals up to 0.0040)
free-exponent 3-param:  C_inf≈-0.862 (per EM's own review)
```

Exact match to EM's cited −0.874/−0.883 and the stated 0.12–0.16 shortfall
from −1. The held-out miss (0.0186) clears exp-030's own pre-registered
`≤0.03` "sqrt-law validated" bar — a genuinely stronger fit than the
self-similar family's own (whose slope sign was wrong, per T14). But the
sign being correct is not the same as the asymptote being reached: **B is
positive** (structurally correct direction, unlike the self-similar
family's B<0) and the ceiling is still short by an amount that dwarfs the
fit's own residuals.

**Ruling: REAL, LOAD-BEARING.** This is the correct framing, and it directly
supersedes the "resolves T14" reading a casual summary of P-1/P-2/P-3's
clean CONFIRMED verdicts would invite. T14's original defect (self-similar
family) was *structural* — a wrong-signed slope that cannot reach −1 at any
finite distance. The fixed-absolute family does not share that defect, and
that is real progress. But an ad hoc, not-yet-committed fit (mine and EM's
both, computed for Phase-5 review, not run through this program's own
house discipline of predictions-before-computation) is not a licensed
witness-scale claim, and none of P-1/P-2/P-3's own falsifiable bands ever
asked whether C_∞ reaches −1 — only whether deepening continues and by how
much. No live thread currently owns this specific, sharper question for the
fixed-absolute family; see §3 below.

### 1c. QUANTUM OPTICS — the bridge gate validated a structurally different configuration

**Claim:** exp-029's own coherent-vs-incoherent bridge gate validated a
structurally different, asymmetric weak-probe configuration (amp_rel=2×10⁻⁴)
from `lab/ambient.py`'s actual equal-amplitude N9 instrument.

**Independently verified by direct read of both files:**

`experiments/029-coherent-superposition-bridge-gate/run.py` injects, in one
`Sim`, a strong on-axis beam (`amplitude=1.0`, θ=0°) **plus one weak
off-axis probe** (`amplitude=sqrt(AMP_REL)`, `AMP_REL=2e-4` ⇒ amplitude
≈0.01414, θ=30°) **simultaneously**, on exp-028's own beam-scene Cell-B
article — a fundamentally different scene class (a directed-beam scene with
a dominant source and a weak interferer) from the ambient instrument
entirely.

`experiments/052-fixed-absolute-thickness-shell/run.py:138` (identical to
every other `lab/ambient.py`-based experiment in this program, verified by
grep across the codebase) calls `sim.add_line_source(..., amplitude=1.0)`
**once per angle, in nine separate single-source runs**, summed *post hoc*
as intensities by `lab.ambient.contrast_from_runs`. There is no
"dominant beam + weak probe" structure anywhere in this instrument — every
one of the nine sources carries the identical, full amplitude.

QUANTUM's own Cauchy–Schwarz-ceiling point checks out algebraically:
exp-029's own cross-term ceiling (2√amp_rel ≈ 2.83%) is small *because of*
the amplitude asymmetry, a property of that specific two-source
construction — it places no bound whatsoever on the cross-term between two
(or nine) **equal-amplitude** sources, which is the actual object this
program's entire `C`-metric family is built from.

**Ruling: REAL, LOAD-BEARING — and larger in scope than exp-052's own
disclosure states.** `phase3_synthesis.md` item 7 and `design_geometry.py`'s
own fix-7 comment both frame the open gap as "validated at shell-fraction
61.5% (r=78)... untested at 30.8%/15.4% (r=156/312)" — language that implies
r=78 **was** validated. It was not, in the sense that matters: exp-029 never
ran the equal-amplitude N9 configuration at *any* geometry, including r=78.
**No geometry this program has run, across 29 iterations, has ever had the
actual instrument this program uses for every constraint-3 `C` citation
empirically bridge-gated.** This is not a critique of exp-052's own
disclosure quality — the Director's Phase-3 note is honest about what it
did *not* close — but the gap it describes is narrower than the gap that
actually exists. See §3 for why this deserves elevation beyond an
exp-052-scoped follow-up.

*(Caveat, stated for completeness, not to soften the finding: Iteration 6's
own analytically-derived result — "the incoherent-ensemble limit is exactly
zero mean cross-term, independent of Δk·r_out or object radius" — is a
statement about an ensemble/phase-averaged limit, not a finite-sample bound
on any one specific 9-angle set at one specific geometry. It does not
substitute for an empirical bound on the actual finite instrument, and
should not be read as already answering QUANTUM's concern.)*

### 1d. THERMODYNAMICS — P-5's silent relabeling

**Claim:** the Phase-1 proposal's own original P-5 (a THERMO energy
sidecar) was silently overwritten at Phase 3 by an unrelated "core-fill
check" reusing the same P-5 label, with no explicit disclosure that the
original charter deliverable was dropped.

**Independently verified, exhaustively, against every file in the
directory:**

`phase1_proposal.md` §8 states P-5 explicitly: *"P-5 (THERMO sidecar,
analytic, post-run...). Using `lab/thermo_sidecar.py`'s established-ratio
branch... predicted `ΔT_ss` at r_out=156 remains UNDETECTABLE... Falsified
if the computed `ΔT_ss` closes to within 10× of the NETD band."* Red Team's
own Phase-2 audit (Attack 8) evaluated this *exact* prediction, ruled it
REAL, MINOR (near-unfalsifiable given every prior sidecar verdict's >100×
margin), and *recommended, not blocking*, that it be relabeled as an
expected low-information confirmation.

`phase3_synthesis.md` item 3 (a **different** docket item — Red Team's own
new Phase-2 proposal for a `radial_absorbed_power` ledger check, itself a
Director-level redesign into a "core-fill check") is written into
`NOTES.md`'s Predictions section as **"P-5 (core-fill check, fix 3, θ=0
only)"** — reusing the P-5 label from an entirely different, unrelated
Phase-1 prediction. `phase3_synthesis.md` §2 even states "predictions P-0
through P-5" as if the set of six were unchanged in kind, not just in
content.

Grepped every file in the directory for `thermo_sidecar`, `ΔT`, `dt_ss`,
`NETD`: **zero hits outside `phase1_proposal.md` and
`phase2_redteam_audit.md`.** Confirmed directly against `results.json`
(`python3 -c "import json; print(list(json.load(open('results.json')).keys()))"`
→ `['meta', 'rgate', 'block', 'fit', 'block_312_pilot_s',
'block_312_pilot_est_min']`) — **no `thermo` key, no `dt_ss`, nothing from
`lab/thermo_sidecar.py` anywhere in the committed record.** `run.py` and
`design_geometry.py` contain no import of, or reference to,
`lab.thermo_sidecar` at all.

**Ruling: REAL, LOAD-BEARING.** This is not a wording nit. Three things make
it more serious than an ordinary citation slip: (1) it is not a *number*
that drifted, it is an entire **deliverable that was never computed** —
`PANEL.md`'s own metrics table lists "Absorbed energy budget + predicted
re-radiation | ledger | Joule accounting + THERMO sidecar" as recorded
*every run*, not conditionally; (2) it is the lead seat's *own charter
item* — THERMODYNAMICS led this cycle by rotation, and its own Phase-1
proposal's own energy-sidecar deliverable is the one thing that silently
did not survive to NOTES.md; (3) nobody in the loop that actually produced
this cycle's committed record — not Phase 3, not Phase 4 — caught it. It
took a *fresh* Phase-5 THERMODYNAMICS sub-agent, with no memory of having
been the lead, reading the artifacts cold, to notice the absence. That is
precisely the failure mode `PANEL.md`'s "flag, don't silently rewrite"
convention and this program's own house rule R4 (three-recurrence,
Iteration 25) exist to prevent — here applied to a dropped measurement
rather than a mistyped number, a genuinely new instance of the pattern, not
a repeat of R4 itself.

**Not load-bearing to the scored physics**, however: P-1/P-2/P-3/P-4
(the actual falsifiable, gated claims this cycle scores) do not depend on
the THERMO sidecar in any way — the omission does not put any confirmed
verdict at risk. THERMODYNAMICS' own Phase-5 review is correct that the
T22 area-invariance argument gives good reason to expect the UNDETECTABLE
pattern survives, while correctly noting the one input (`σ_abs/σ_ext=0.51`)
that argument depends on is itself unverified at this cycle's own new
`r_in/r_out` ratios (0.692/0.846, both above the only-ever-tested 0.385) —
so "probably fine" is not the same as "verified."

### 1e. VISION SCIENCE — the aggregate `C` metric cannot distinguish deeper shadow from wider complete-shadow

**Claim:** the aggregate `C` metric can't distinguish "deeper shadow" from
"larger angular extent of complete shadow" — the QUANTUM bridge-gate
concern should be ELEVATED given the size of the confirmed effect.

**Independently verified** against `lab/ambient.py`: `contrast_from_runs`
→ `window_means` averages flux over the *entire* object window
(`w_obj` cells) into one scalar `obj` value before computing `weber()`; no
radial or angular profile is ever produced or stored anywhere in this
instrument's output path. This is a structural property of the instrument,
confirmed by reading the code, not an inference from results: the
mechanism narrative in `phase1_proposal.md` §1/§3 ("a fixed-width rim-leak
channel becomes a shrinking fraction of a growing silhouette") is a claim
about spatial structure the scored `C` value is, by construction, unable to
verify or falsify on its own.

**Ruling: REAL, LOAD-BEARING as a mechanism-attribution caveat** (does not
touch P-1/P-2/P-3's own falsifiable claims, which are about the aggregate
number and are correctly scored as such) **and the elevation argument for
the bridge-gate concern is independently sound**, verified by the same
arithmetic every seat used: this cycle's own confirmed deepening (0.086 at
r=156, a further 0.034 at r=312) is 100–1000× larger than the only
cross-term this program has ever measured (+0.0224%) — decisive against a
coherence artifact *of that specific measured kind and scale*, but (per
§1c) that measured artifact is not evidence about the untested,
structurally different, unbounded-by-anything-measured equal-amplitude
configuration this cycle's own result actually runs on. VISION's
"elevated stakes, not elevated measured probability" framing is the
correct way to state this, and Red Team adopts it.

### 1f. MATERIALS & METAMATERIALS — realizability stays PLAUSIBLE-not-PUBLISHED; 60nm e-folding length uncited

**Claim:** the realizability tier stays PLAUSIBLE-not-PUBLISHED, and the
60nm absorption e-folding length is still uncited.

**Independently verified**: `grep -n "60nm\|e-fold\|absorption coefficient\|CNT" experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`
finds only thickness-precedent lines (442, 480: "few-µm to sub-mm," "tens of
nm to ~1mm") and one unrelated cm-scale e-folding reference (line 461, a
different mechanism class, RSA/TPA) — **no absorption-coefficient or
optical-density citation for CNT-forest/Vantablack-class coatings exists
anywhere in this program's record.** `design_geometry.py`'s own computed
figure (`ALPHA_PER_NM=1/60nm`) is correct arithmetic (`τ_shell/thickness =
24/1440nm`) but has no comparator to check it against — exactly as
MATERIALS states.

**Ruling: REAL, MINOR** as an exp-052-specific finding (this cycle correctly
computed and disclosed the number as "thickness-only, absorptivity
unchecked" per fix 6, exactly per the accepted docket item) but **carries
forward as a real, un-closed programmatic gap** whose root cause (T18's
WebFetch block, unaddressed since Iteration 13) this cycle did not and
could not touch. MATERIALS' own finding that this is now the program's
*favored, better-performing, easier-to-build* design lead — not merely an
argued alternative — sharpens the priority of closing this gap without
changing the tier call itself, which is correctly held at PLAUSIBLE.

## 2. Findings caught by none of the six blind Phase-5 seats

### 2a. [inconsistency] The bridge-gate gap is program-wide, not exp-052-local — none of the other five seats independently derived the mechanism, only QUANTUM did

Covered in full in §1c. Worth restating the scope explicitly, since five of
the six Phase-5 seats (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS,
VISION, MATERIALS) each independently *named* the open item ("re-validate
the bridge gate") in their own top-3 lists, but only QUANTUM went back to
`experiments/029/run.py` and `lab/ambient.py` to establish *why* the
existing gate cannot bound the actual instrument — a structural mismatch,
not merely an untested-geometry gap. This means every one of this program's
constraint-3 `C` citations since Iteration 1 — every PASS/MARGINAL/FAIL
verdict this program has ever issued, not just this cycle's — rests on an
approximation whose only cited empirical license tested a different
physical configuration. **Ruling: REAL, LOAD-BEARING, and the single most
consequential finding of this Phase 5.**

### 2b. [inconsistency, disclosure] P-5's relabeling is compounded by an un-actioned Red Team recommendation

Not caught by any of the six: Red Team's own Phase-2 audit (Attack 8)
explicitly recommended (not blocking) that the *original* P-5 be relabeled
as an expected, low-information confirmation. `phase3_synthesis.md` never
states whether this recommendation was accepted, rejected, or simply
superseded by the label being reused for something else — it is not
mentioned at all in the "Nothing rejected as unfounded" closing sentence,
which is itself now shown to be imprecise: something *was* dropped, just
not "rejected as unfounded" in the sense that sentence intends. This is a
process gap on top of the content gap already identified in §1d — the one
recommendation that, if honored, would have prevented the silent drop
entirely (by keeping P-5 as a named, disclosed, low-information item rather
than letting its label be repurposed) went unaddressed without comment.

### 2c. Nothing else rises to a new numbered finding

I looked specifically for: (i) further R4-class transcription drift beyond
the one already self-caught and disclosed in `run.py::run_fit`'s own
comment (the stale −0.7350/−0.7305 bands, non-load-bearing, correctly fixed
before the shipped scoring ran — confirmed by reading the live code, not
just the comment); (ii) whether the r=312 leg's cost-gating decision
(pilot ≈77 min vs. exp-030's own 232-min/37-run precedent) was honored
correctly — it was, and proceeding was the right call given the more
favorable extrapolation; (iii) whether `run_block`'s angle-set union logic
correctly produces the claimed 28-run cost (9 empty + 9 fixedabs + 9
selfsim + 1 hollow-θ0) — verified directly in code, correct. None of these
rise above "process working as designed."

## 3. Overall verdict: **PROMISING**

This cycle's own central, pre-registered question — does removing the
self-similar family's growing-absolute-thickness confound eliminate T14's
wrong-direction shallowing? — is answered cleanly, not ambiguously: P-1,
P-2, and P-3 all read CONFIRMED, independently re-derived here to full
float precision from `results.json`, with margins (17–21× the required
thresholds) far outside any plausible instrument-noise band this program
has ever characterized (T16's own 7.80×10⁻⁴ angular-quadrature+domain
budget is 55–100× smaller than the deltas being scored). This is real
progress on a 21-iteration-deferred, unconditionally-triggered commitment,
and MATERIALS' seat is right that it converts an argued realizability
claim into a measured one, in the direction that favors realism (the
fixed-absolute construction is both easier to build *and* now shown to be
optically better at scale than the alternative this program has cited for
21 iterations).

This is not, however, an unqualified success, and the gap between "P-1/P-2/
P-3 CONFIRMED" and "T14 resolved" is real and must not be elided in any
future citation. Two things keep this from PROMISING-clean: (1) EM's C_∞
shortfall (0.12–0.16 from −1, §1b) means the fixed-absolute family's own
asymptotic behavior is not yet shown to reach the physically-expected
ceiling — a genuinely open, sharper question this cycle did not commit
falsifiable bands against; (2) the bridge-gate finding (§1c/§2a) means the
instrument that produced every number in this cycle's headline has never
been empirically validated in the configuration it is actually used in, at
any geometry this program has run — a foundational-trust gap this cycle's
own large, clean result raises the stakes on without changing the measured
probability of contamination.

Neither of these threatens the SCORED verdicts (P-0 through P-4 all pass
their own pre-registered bands by wide margins); both are real, disclosed
(if incompletely, per §1d/§2b), and squarely this program's own next
priorities. This is the same class of "real deliverable, real open
caveats, no falsified prediction" pattern this program has called PROMISING
before (Iteration 28) rather than PARTIAL (Iterations 7/8, where the
cycle's own *central* question itself came back genuinely unresolved) —
the distinguishing fact here is that exp-052's own stated falsifiable
claims resolved cleanly; what remains open are adjacent, real, and now
better-characterized questions, not an unresolved primary deliverable.

## 4. Checkpoint criteria — all five checked explicitly, per this program's own standing practice

1. **"A configuration passes ALL constraint metrics (candidate
   reproduction)."** **Does NOT fire.** No constraint-1–4 claim is made or
   scored this cycle; T1 escape route is correctly declared `None`
   throughout, and no PASS/MARGINAL/FAIL language appears anywhere in the
   record. This criterion requires a constraint-metric claim to exist
   before it can be evaluated; none does.

2. **"A proven boundary: a constraint subset shown jointly unsatisfiable
   within a whole mechanism class, gates clean."** **Does NOT fire.**
   Considered explicitly, per the task's own instruction, against the
   realizability finding: this cycle does not prove a boundary in either
   direction. MATERIALS' own tier call (§1f) stays PLAUSIBLE-not-PUBLISHED
   — the absorptivity axis remains genuinely unresolved, not closed as
   either realizable or unobtainium. If anything, this cycle's finding
   moves *away* from a boundary-proof reading: the construction that was
   already known to be the easier realizability ask is now also shown to
   be optically better, which argues against ruling out this mechanism
   class, not toward proving it jointly unsatisfiable. Separately, even a
   boundary claim attempted on this record would fail the "gates clean"
   precondition — the bridge-gate validity gap (§1c/§2a) is an open,
   unresolved instrument-trust question, not a clean gate.

3. **"A synthesis requires engine physics beyond the validated bench
   classes (major build — other live threads continue meanwhile)."**
   **Does NOT fire.** exp-052 reuses, unmodified, the existing PEC/
   dielectric graded-absorber material law (`lab/materials.py`), the
   existing ambient/N9 instrument (`lab/ambient.py`), and the existing
   flat-wall R-gate idiom — all already-validated bench classes. Nothing
   in this cycle's design, critique, or results calls for new engine
   machinery.

4. **"Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped — especially #3)."** **Does NOT fire on the
   letter, this cycle** — considered explicitly and carefully against both
   the THERMODYNAMICS P-5 finding (§1d) and the bridge-gate finding
   (§1c/§2a), per the task's own instruction. Neither is, strictly, "a
   constraint quietly dropped" in the T1–4 numbered sense the criterion
   names, and neither is an unfalsifiable claim being actively asserted —
   the P-5 gap is an absent measurement under a reused label, not a false
   claim; the bridge-gate gap is an inherited, disclosed (if
   under-scoped) open assumption, not a claim of validation being made
   where none exists. Both are also, critically, **being caught and
   surfaced now, within this same Phase-5 audit, before LOGBOOK.md or
   PLAN.md ever record this cycle as closed** — consistent with this
   program's own repeated practice (Iterations 7, 8, 27, 28) of treating
   disclosure gaps caught before final close as findings requiring a fix
   docket, not automatic Checkpoint triggers.

   **But both are real, and both are more serious than this program's
   recent disclosure-defect precedents** (Iteration 27/28's narrative
   misattributions, which were pure prose errors touching no measurement).
   The P-5 gap is an entire missing measurement, of the lead seat's own
   charter deliverable, that a "predictions P-0 through P-5" sentence
   papers over. The bridge-gate gap means a foundational instrument-trust
   assumption this program's own prose has treated as settled since
   Iteration 6/7 was never actually tested in the form it is used. **Two
   new tripwires are adopted here, binding for future shifts, in this
   program's own established style (cf. Iteration 7's e2 tripwire):**
   (i) any future LOGBOOK/PLAN citation of exp-052 that states or implies
   a THERMO energy sidecar was computed for this cycle, without the
   correction in §1d/the docket below being applied first, is a
   retroactive criterion-4 trigger; (ii) any future citation of *any*
   `lab/ambient.py`-derived `C` value that asserts or implies the
   incoherent-sum approximation is "empirically bridge-gated" without
   naming the amp_rel/equal-amplitude distinction in §1c/§2a is also a
   retroactive criterion-4 trigger.

5. **"Two consecutive iterations with no logbook-advancing result."**
   **Does NOT fire.** This cycle clearly advances the logbook: it
   discharges a 21-iteration-deferred unconditional trigger, produces a
   genuine, independently-verified, falsifiable, wide-margin result
   (T14's puzzle relocated to a sharper, better-characterized question,
   not left where it was), and converts an argued realizability claim
   into a measured one.

## 5. Must land before this cycle closes — prioritized docket

1. **[Attack 2a/§1d, load-bearing]** Add an explicit, unambiguous sentence
   to `NOTES.md` (not buried in `phase3_synthesis.md` alone) stating that
   the Phase-1 proposal's original P-5 (THERMO energy sidecar, `ΔT_ss` vs.
   NETD) was **not computed** this cycle, and that the "P-5" label in the
   final Predictions section refers to an unrelated core-fill check
   (Red Team's own Phase-2 item 3, Director-redesigned). Do not let
   "predictions P-0 through P-5" stand as if the set were unchanged in
   kind.
2. **[Attack 2a/§1d, should-do, cheap]** Actually run
   `lab/thermo_sidecar.py`'s established-ratio branch on the
   `absorber_fixedabs` object at r=156/312, per THERMODYNAMICS' own
   Phase-5 "argued next change" — analytic, zero-FDTD, restores the
   `PANEL.md`-mandated per-run energy ledger, and turns a silent absence
   into an honest, explicitly-flagged-as-`σ_abs/σ_ext`-unverified number.
3. **[§1c/§2a, load-bearing, must be stated in the LOGBOOK Iteration-29
   entry]** State explicitly, at program level, that the coherent-vs-
   incoherent ambient-sum bridge gate has never validated the actual
   equal-amplitude N9 configuration `lab/ambient.py` uses, at any geometry
   this program has ever run — not merely "untested at 30.8%/15.4% shell
   fraction," the framing currently on record. Open or expand a live
   thread to track this at program scope, not as an exp-052-local item.
4. **[§1b, should-do before any future witness-scale citation of this
   family]** Do not let any future LOGBOOK/PLAN citation of exp-052 read as
   "T14 resolved" — carry EM's own C_∞ shortfall (0.12–0.16 from −1) and
   the fact that no formal, pre-registered `C(z/z_R)` extrapolation fit
   exists yet for the fixed-absolute family (T8's own standing requirement,
   still unexecuted for this family) into the closing language.
5. **[Attack 2b, cheap, disclosure-only]** Note in the LOGBOOK entry that
   Red Team's own Phase-2 recommendation (relabel the original P-5 as
   low-information rather than let its label be reused) was never
   explicitly actioned — closes the process gap identified in §2b so a
   future audit does not need to re-discover it.
6. **[§1f, low priority, bookkeeping]** Action MATERIALS' own recommended
   `REALIZABILITY_MEMO.md` Amendment: mark Entry 2's "Open" line (build and
   measure the fixed-absolute variant) as closed by this experiment, and
   fold in the sharpened absorptivity/mechanism question as the entry's own
   next open item.

## 6. Ranked candidate directions, Iteration 31+ (Iteration 30 is LOCKED to VISION's stage-10 instrument — not re-ranked here)

**A standing-bar flag, ahead of the ranked list, per this program's own
established precedent language:** `PLAN.md`'s existing queue already states
that THERMODYNAMICS' `h_eff` re-derivation (exp-043 ON-endpoint, exp-045
dose-accumulation) was "named at four consecutive closes (25, 26, 27, 28)
without being reached... a fifth deferral meets this program's established
bar for an unconditional trigger and must not pass as an ordinary
re-ranking." **This cycle (29) is that fifth deferral** — exp-052 executed
a different, also-unconditional trigger and did not touch `h_eff`. Per this
program's own explicit prior ruling, this is no longer a competitive
ranked item: **it should be locked as an unconditional Iteration-31 build
trigger**, on the same terms as the two slots already locked at Iterations
29 and 30.

Reconciling all six seats' own ranked lists (near-unanimous convergence
noted explicitly where it occurs):

1. **The coherent-vs-incoherent bridge-gate revalidation, built against the
   actual equal-amplitude N9 configuration** (not exp-029's weak-probe
   idiom) — ranked #1 or #2 by five of six seats (PHOTONICS #3,
   ELECTROMAGNETISM #2, QUANTUM #1, THERMODYNAMICS #2, VISION #1) and
   elevated here beyond any single seat's framing by §1c/§2a's finding
   that the gap is program-wide, not exp-052-local. QUANTUM's own
   redesigned instrument (joint equal-amplitude injection, reusing suite
   stage 11's existing field-identity gates) is the concretely scoped,
   cheapest correct next build.
2. **The λ-generalization run** (450nm + 750nm, r=156, both families) —
   ranked by three of six seats (PHOTONICS #1, VISION #3, MATERIALS #2).
   Cheap (reuses all existing domain machinery), and directly closes
   whether P-3's T14 reframe is a general property of fixed-absolute-
   thickness shells or a 600nm/2.4λ-specific coincidence — this program has
   three independent, on-the-record precedents (R2's `r2=90`-specific
   feature; T21's non-monotonic λ-ordering; Iteration 19's `c*(λ)` finding)
   for treating single-wavelength near-field results with exactly this
   suspicion.
3. **A formally committed `C(z/z_R)` extrapolation fit for the
   fixed-absolute family** — pre-registered falsifiable bands on `C_∞` vs.
   −1, ideally with a 4th r-point — executing T8's own long-standing
   "committed extrapolation model before any near-threshold verdict is
   believed" requirement for the first time on a family whose slope is
   correctly signed (EM #1, PHOTONICS #2). Directly resolves whether §1b's
   0.12–0.16 shortfall is real or a 3-point-fit artifact, and gives the
   standing, unsourced |C|≈0.98 figure its first actual derivation to be
   checked against.
4. **The genuine FDTD `ABSORB` sweep at GEOM78** — carried unrun across
   Iterations 26–29 (four straight cycles now, since this one also did not
   touch it), near-unanimous historically, already flagged by Red Team at
   Iteration 28 as "approaching unconditional-trigger territory if
   deferred again." One more deferral away from meeting the same bar just
   applied to `h_eff` above.
5. **MATERIALS' absorptivity/mechanism literature check** (T18-dependent,
   zero-FDTD either way) — the one remaining unchecked axis standing
   between "PLAUSIBLE" and a tier change on this program's own now-favored
   design lead (MATERIALS #1).
6. **A targeted N9-vs-N17 angular-quadrature check on the opaque-absorber
   article class** (VISION #2, new this cycle) — T16's entire angular-
   sampling uncertainty budget has only ever been measured on a near-null
   σ(I) article; never on the deep-shadow class this program's constraint-3
   citations, including this cycle's own headline, actually are. Cheap,
   reuses the already-built `absorber_fixedabs` r=156 object.
7. **Extend the core-fill check (P-5/fix 3) to the full N9 sweep**, not
   just θ=0 (MATERIALS #3) — the θ=0 null is decisive at boresight but T9's
   own established mechanism is a grazing/tangential-chord effect; the
   ±25°/±35° angles that actually feed the deepening headline have never
   been core-fill-tested at these ratios. Trivial marginal cost, reuses
   already-built machinery.
8. **QUANTUM's grating-lobe/array-factor n\* criterion for
   `beam_divergence_coherent`** (carried unchanged from Iteration 28's own
   queue, item 2) — unaffected by this cycle, still open.

Not re-ranked, carried forward per Iteration 28's own close: T8/T13/T14's
sensitivity-band minimum bar (dormant 20+ iterations); the
`_geom_derived`/`_G_for_g` hoisting pattern (low priority).
