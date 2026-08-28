# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 64 · exp-087
## "Measuring the Energy-Interception Cross-Check for Real"

Charter (verbatim): attacks every proposal, speaks last and hardest.
Standard is NOT textbook-physics compliance — speculation is permitted. It
kills internal inconsistency, unfalsifiable claims, mechanisms that cannot
be expressed as simulation parameters, and proposals that quietly violate a
target constraint — especially #3. Red Team never leads a cycle; it has no
proposal of its own to protect.

Fresh context, no memory of any other seat's current-cycle output or of any
prior Red Team instance. Everything below is independently re-derived from
source (`lab/sections.py`, `run.py`, `results.json`, `run_output.txt`,
`experiments/024-.../design_geometry.py`+`run.py`, `experiments/002-.../
run.py`, LOGBOOK.md) — not accepted from any Phase-2/Phase-5 seat's own
prose, per this program's own R4/R9 discipline. Read in full: PANEL.md,
LOGBOOK.md (all 19,110 lines, with targeted deep re-reads of the RULED OUT
registry R1–R12 and the complete T28 live-thread, Iterations 46–63), this
cycle's entire record (Phase 1 → `phase2_redteam_audit.md` → Phase 3 →
NOTES.md → `run.py`/`results.json`/`run_output.txt` → all six Phase-5
reviews), `lab/sections.py` in full, and `experiments/024-.../run.py` in
full.

**Checkpoint criterion 2 is N/A this cycle** (§7) — no phenomenon-mechanism
claim, no T1 escape-route framing. This audit accordingly weighs
measurement validity, historical-accuracy, and constraint-3-bookkeeping
honesty — matching what the cycle itself claims to be.

---

## 0. Housekeeping re-verification

Independently re-ran/re-read the primary chain rather than trusting any
prose summary:

- `run_output.txt` confirms 13 FDTD calls, matching `results.json::
  total_new_fdtd_calls=13`. P1 (vacuum footprint), P2 (reproduction,
  `max_dev=0.0` exactly), P4 (`xi_ext`, max `4.82×10⁻⁴`, well inside the
  `≤0.12` gate), P5 (synthetic recovery, 14/14 cases), and the
  non-negativity gate (post-correction) all PASS, confirmed directly from
  `results.json`, not from NOTES.md's restatement of them.
- Primary table reproduces exactly: `ratio_k` = 2.6423677612294223 (36.0°),
  53.988397675546146 (38.6°), 5.710203290428644 (41.8°) — hand-recomputed
  from `frac_p_abs`/`frac_contrast` and matching to the last printed digit.
  `p7_classification=ENERGY-DOMINANT` is the literal, correct output of
  `classify_resolved()`'s own "any angle over `RATIO_HIGH`" priority rule
  applied to these three numbers, confirmed by tracing the function itself,
  not merely trusting the label.
- Six Phase-5 reviews, zero overlap in their headline findings (aliasing
  residual (PHOTONICS' own §4 follow-up), T9-generalization confirmation
  (MATERIALS), the `back_frac`/`fwd_frac` defect + the false "first-ever"
  claim (EM), the denominator-fragility structural defect (QUANTUM), the
  third disclaimer-erosion instance + two provenance gaps (VISION), and the
  swing-specific NETD/`iso_xsec_sq`-sensitivity checks (THERMODYNAMICS) —
  matching this sub-thread's own recent "N different defects, zero overlap"
  precedent (exp-086 Phase 2).

---

## 1. EM's claim: exp-024/Iteration 2 has the SAME `src_x>obj_x>plane_x`
geometry and already defensively guards the sign issue — CONFIRMED,
independently, from source

Read `experiments/024-ambient-margin-adjudication/design_geometry.py`
directly, not via any critique's citation: `SRC_X=300`, `OBJ_X=170`,
`PLANE_X = OBJ_X − R_OUT − PLANE_DX = 77`. This is `src_x(300) >
obj_x(170) > plane_x(77)` — the **identical** directional relationship
`PAIR_PAD` has (`src_x>obj_x>plane_x`, wave travels in −x). `lab/
fdtd2d.py::Sim.add_line_source`'s own docstring ("The −x-going wave then
travels along...") confirms exp-024's source at `SRC_X=300` is genuinely
−x-propagating toward the object at `OBJ_X=170`.

Read `experiments/024-.../run.py` directly: line 101 calls `sc.widths(cap,
cap_e, dg.BOX, REF)` on this exact −x-propagating scene, and lines 195–199
compute
```
scale = abs(grp["absorber"]["sigma_abs"] * grp["absorber"]["i_inc"])
gates[f"P6-emptybox/{lam_nm}/{th:+.0f}"] = abs(grp["empty"]["net_box_flux"]) / max(scale, 1e-30)
```
— `abs()` wrapped around both `sigma_abs*i_inc` (recovering the signed raw
power, made non-negative) and `net_box_flux`, exactly as EM states. **EM's
claim is CONFIRMED exactly, independently, from source — not merely
re-stated.**

**A second, independent fact this audit adds, not raised by any Phase-2/5
document**: `run.py`'s own `widths_direction_corrected()` docstring and
NOTES.md's Result section both state: *"Every PRIOR caller of `widths()`
(exp-002/024's absorber bench) had `src_x<obj_x`, propagating in +x."* I
checked `experiments/002-cross-sections/run.py` independently: `SRC_X=64`,
`CX=252` ⇒ `src_x<obj_x`, genuinely +x-propagating — this part of the claim
is TRUE for exp-002. But it is **directly, factually false for exp-024** —
verified above, `SRC_X=300 > OBJ_X=170`. This is not merely a NOTES.md
prose overclaim; it is a **materially incorrect factual assertion embedded
in `run.py`'s own shipped code comment**, naming exp-024 explicitly as an
example of the pattern it is the counterexample to.

**Bit-exact confirmation is not possible, and this audit does not overclaim
it.** `experiments/024-.../results.json` was checked directly (`json.load`,
top-level keys): it persists only `contrasts`, `luminance_weighted`,
`plane_sensitivity`, `convergence`, `decision_floors`, and `gates` — the
raw per-`(lambda,theta,article)` `sigma_abs`/`i_inc` dict built in `main()`
is held only in memory, never written to disk. So whether exp-024's own raw
`sigma_abs` actually came out negative cannot be checked to the same
bit-exact standard EM's own review correctly declines to claim. What CAN be
confirmed, and is sufficient: (a) the geometry is identical in propagation
direction; (b) `widths()`'s `i_inc` computation is the same code, unchanged
since exp-002; (c) exp-024's own gate code defensively wraps `abs()` around
exactly the two quantities (`sigma_abs*i_inc`, `net_box_flux`) that this
cycle's own diagnosis shows are sign-flipped together. Three independent
facts pointing the same direction, none individually dispositive, together
make "the same defect, present and silently absorbed at Iteration 2, never
diagnosed" the better-supported reading — the standard EM's own review
already applied correctly.

**Should this have been caught before the run — a Phase-2 miss?** No. I
checked `phase1_proposal.md` directly: the "first-ever `src_x>obj_x`"
framing does not appear anywhere in it — the sentence and the diagnosis it
rests on were only written during Phase 4, inside `run.py` itself, after
the negative-`sigma_abs` bug was found and fixed. Phase 1, all five Phase-2
critiques, and my own predecessor's `phase2_redteam_audit.md` could not
have caught a claim that did not yet exist at the time they were written.
This is correctly a Phase-4-authored claim, correctly caught at Phase 5 (by
EM) — matching the R4 lineage's own standard that a "first"/"precisely
reproduced"-shaped claim must be independently verified wherever it
appears, regardless of which phase produced it.

**Does this change how novel this cycle's own "fix" actually is?** Partly,
and precisely: the underlying **defect** (a signed +x-flux `i_inc` silently
mis-normalizing a −x-propagating scene) is not novel to this cycle — it was
already latent, unexercised-to-diagnosis, in exp-024, 62 iterations and 63
experiments earlier. What IS genuinely novel this cycle is the
**diagnosis**: the first time this sign-convention hazard has been named,
traced to `sections.py::widths()`'s own `sx()` convention, confirmed via an
independent invariance argument (EM's Phase-5 §1, itself independently
re-derived and confirmed here), and fixed with a documented, zero-`lab/`-
diff caller-side wrapper. The historical-accuracy correction belongs in the
permanent record; it does not diminish the value of the diagnosis or the
fix, both of which are genuinely this cycle's own contribution.

**Ruling: CONFIRMED. Correct same-shift**: `run.py`'s docstring and
NOTES.md's Result section should read "first *diagnosed* here — likely
present and silently worked around, undiagnosed, since Iteration 2
(exp-024)," not "first `widths()` application with this geometry." **Does
not fire Checkpoint criterion 4**: non-load-bearing (P7's classification
never depended on the historical-novelty framing, only on the direction
correction itself, which is independently confirmed sound), caught blind,
same cycle, before LOGBOOK — matching this program's own established
non-firing test.

---

## 2. QUANTUM's proposed reclassification of θ=38.6° — independently
re-derived, CONFIRMED quantitatively; does NOT change the headline label
this cycle, but materially changes its confidence

Re-derived from `experiments/083-.../results.json::per_theta` directly
(not via any Phase-5 citation): `delta_scene` at 38.4°=+8.083×10⁻⁴,
38.6°=−4.151×10⁻⁵. Linear interpolation for the true zero-crossing:

```
θ0 = 38.4 + 0.2 * (8.083e-4) / (8.083e-4 + 4.151e-5) = 38.5902°
```

— independently reproduces QUANTUM's own `θ₀≈38.590°` to 4 significant
figures. The sampled point sits `|38.6−38.590|≈0.010°` from the curve's
true zero, and — solving `ratio_k(θ)=RATIO_HIGH=10` locally, holding
`frac_p_abs≈4×10⁻³` and `|C40_C|≈0.56` fixed (both true in this narrow
window, confirmed from the same table) — the decade-boundary crossing
itself sits `|θ−θ₀|≈0.053°` from the node, a quarter of this cycle's own
0.2° grid step. Both figures independently re-derived here match QUANTUM's
own arithmetic exactly, not merely re-stated.

**Corroborating evidence, independently re-checked**: `frac_p_abs(38.6°)
=4.001×10⁻³` sits 7.4% BELOW a linear interpolation of its own two flanking
measured points (predicted 4.318×10⁻³ if the true trend is smooth) — the
numerator shows no compensating anomaly whatsoever, ruling out a genuine
energy-domain spike coinciding by chance with the node. QUANTUM's own
interpolated bracketing estimate (`ratio_k(38.4°)≈2.8`, `ratio_k(38.8°)≈
2.6`, both CONSISTENT) is suggestive, not dispositive (it uses an
interpolated, not measured, `frac_p_abs` at the neighbors) — correctly
flagged as such by QUANTUM itself, and I do not treat it as more than that
here.

**Is this a genuinely new failure mode, distinct from R5/R10?** Yes,
independently assessed on its own merits, not merely because QUANTUM says
so. R5's family and R10 both concern whether an observed match, period, or
fit is *statistically* distinguishable from a null/noise process — a
look-elsewhere or specificity problem that exists because of finite,
noisy sampling. QUANTUM's finding here is different in kind: `ratio_k`'s
denominator is built from a quantity (`delta_scene`) independently
established to be a genuine, smooth, low-noise, `p=0.0`-null-controlled
periodic curve — the instability is not statistical, it is **algebraic**:
any smooth, non-vanishing numerator divided by a denominator with a real
zero produces an unbounded ratio near that zero, with or without
measurement noise. A perfect, infinite-SNR measurement of `frac_p_abs`
would still produce this exact blowup at 38.6°. This is a structural
defect in the *classification scheme's own construction*, not a
statistical-power problem R5/R10's existing machinery addresses. Confirmed
independently — see §8 (new standing rule) below.

**Does this change the Combined Verdict's own headline classification, or
just its confidence/caveats?** **Ruling: confidence/caveats, not the filed
label.** Two considerations, weighed against each other:

- The pre-registered, frozen (`phase3_synthesis.md`, committed before any
  Phase-4 code ran) classification scheme states its own rule in full:
  ENERGY-DOMINANT fires on "`ratio_k(θ)>10` at ANY resolved angle," with
  explicit veto priority over the other three labels. θ=38.6° cleared the
  ONE noise-floor gate the frozen spec actually specifies (the numerator-
  side, `box_dev`-scaled gate) with real margin (4.49× over the floor,
  independently confirmed by THERMODYNAMICS' Phase-5 review and
  re-verified here) — it is `resolved=True` by the pipeline's own written,
  pre-committed rule, not a borderline or degenerate case the DEGENERATE
  carve-out was ever meant to catch.
- Retroactively re-labeling this cycle's own already-computed,
  pre-registered classification based on a NEW gate (the denominator floor
  gate QUANTUM proposes, §8) that did not exist in the frozen Phase-3 spec
  would be exactly the kind of after-the-fact rule-bending this program's
  own house discipline exists to prevent (Iteration 60's Director
  explicitly declined an analogous move: "retrofit a rushed
  energy-interception check ... purely to avoid the firing ... itself the
  kind of after-the-fact rationalization R8 exists to catch"). The correct
  discipline is the one this cycle's own six Phase-5 reviews converge on
  without exception: report ENERGY-DOMINANT exactly as the frozen pipeline
  computed it, attach the node-artifact finding as a prominent,
  independently-verified caveat, and resolve it with a cheap, decisive,
  **pre-registered** follow-up (§4/§6 below) — not a silent post-hoc
  relabeling.

**The falsification itself is label-independent and is not weakened by any
of this.** Confirmed independently, a fourth time (after PHOTONICS,
QUANTUM, EM, THERMODYNAMICS all did so separately): excluding θ=38.6°
entirely, the two remaining angles (`ratio_k`=2.64, 5.71) land squarely
CONSISTENT — not the predicted ENERGY-DECOUPLED (`<0.1`) under either
reading. **P7 is genuinely FALSIFIED regardless of how the 38.6° dispute
resolves.**

**Ruling**: the filed classification (ENERGY-DOMINANT) stands as the
official record of what the pre-registered pipeline computed. NOTES.md's
own "disclosed, not adopted" framing for the node-artifact explanation was
already correct; this audit ADDS the ruling that the framing should now be
elevated from a disclosed caveat to a flagged, near-unanimous, Tier-1
mandatory follow-up (the 8-call bracketing test, §6 below) before any
future citation of "ENERGY-DOMINANT" from this cycle is read as settled,
undisputed physics rather than a classification the pipeline's own
construction cannot yet distinguish from an artifact at this one point.

---

## 3. VISION's finding: the NETD/constraint-3 disclaimer eroded a THIRD
time — CONFIRMED directly from NOTES.md; ruling on Checkpoint criterion 4

Re-read the committed `NOTES.md` directly, not via VISION's citation.
Confirmed exactly:

- Idealization 9 (lines ~81–83): carries the full disclaimer.
- Predictions §8 (lines ~125–129): **no inline disclaimer** — "predicted
  UNDETECTABLE at every (cfg,θ) cell. Pre-committed triage rule: ..."
- Result, P8 paragraph (lines ~234–239): **no inline disclaimer** —
  "predicted UNDETECTABLE, confirmed at all 6 (cfg,θ) cells ... NETD margin
  ... ranges ≈374×–442× ... No triage-rule trigger."

Both restatements are exactly the two places Red Team's own Phase-2 audit
mandatory fix 8 named ("every restatement of P6/constraint-3 language...
not filed once in frozen Phase-1 text and then compressed later"), and
Phase 3 adopted this fix in full, zero override, repeating the same
"carried inline, every restatement" language in its own text. **Confirmed:
the mandatory fix was NOT implemented in NOTES.md's prose**, even though
`results.json` itself is clean (the disclaimer string IS carried verbatim
at every `thermo` cell and in the top-level `netd_disclaimer`/`scope_note`
fields — confirmed directly). The data pipeline complied; the prose a
future LOGBOOK/PLAN.md citation would actually quote did not.

**Is this the third instance of this identical shape?** Confirmed,
independently, against LOGBOOK's own text (not VISION's citation of it):
T16/Iteration 53 (the `amp_ratio`-vs-`C_thr` unit-mismatch, R9's founding
instance) and R12/Iteration 63 (exp-086's own Learned section silently
widening a `pair_pad`-scoped finding into an unqualified claim) are both
real, independently-recorded prior instances of a scoped, disclaimer-
qualified finding losing its qualifier in later prose within this exact
sub-thread. This is genuinely the third.

**Ruling on Checkpoint criterion 4: does NOT fire, confirmed independently.**
Non-load-bearing (no scored verdict — P7, P8's actual classification and
margin figures — depends on the disclaimer's prose placement), caught
blind, same cycle, before LOGBOOK, matching this program's own established
non-firing test (Iteration 58's compliance gap, Iteration 63's own
Learned-section erosion — both closed same-shift, neither fired).

**Is "wait for a fourth instance" the right call, or does a third instance
of an identical, named, previously-flagged shape warrant firing now?**
Independently weighed against this program's own precedent, not merely
deferred to VISION's own recommendation:

The R4 lineage is the closest precedent for exactly this shape (a
disclosure/citation-hygiene defect, caught blind at Phase 5, non-load-
bearing, corrected same-shift). R4's own history: the FIRST addendum
(Iteration 50) fired on the SECOND instance of its specific sub-pattern
("144/144" claim) with a "tightened requirement," not a hard firing rule.
The SECOND addendum (Iteration 51) fired on a **THIRD** instance of the
identical shape ("aggregate figure not independently recomputed") and Red
Team's own ruling at that time was explicit: *"not yet a fresh rule, but
the existing... language is evidently not sufficient on its own —
tightened requirement."* That is the direct precedent for a THIRD instance
of a disclosure-hygiene failure, and this program's own Red Team declined
to fire Checkpoint 4 even then, choosing instead to sharpen the standing
rule's text. R9, R11, and R12 were all similarly adopted or tightened on
their OWN founding/consolidating instance without retroactively firing
criterion 4 on that instance itself — the escalation clause is set FOR THE
FUTURE, not applied backward.

**Ruling: VISION's call is correct, and independently confirmed against
the closest precedent (R4's second addendum) rather than merely accepted.**
Does not fire. Adopt VISION's proposed forward tripwire, sharpened slightly
using this audit's own reading of the failure's mechanism (VISION's own
observation: this instance is narrower and more mechanical than the first
two — a `Predictions`/`Result` prose restatement gap, not a conceptual
scope misunderstanding, since the correct string was typed once, correctly,
into the code's own JSON output and simply not pasted twice more):

> **Forward tripwire, adopted this audit**: a fourth instance of the
> identical inline-disclaimer-erosion shape (a disclaimer or scope
> qualifier correctly stated once in a document's own frozen/Idealizations
> text, or correctly persisted in a run's own `results.json`, but absent
> from one or more later prose restatements of the same finding, on any
> T28/constraint-3-adjacent cycle) fires Checkpoint criterion 4
> automatically, no further deliberation — matching the R4/R9/R11/R12
> "known, named, ignored" escalation convention exactly.

---

## 4. VISION's other two findings — both CONFIRMED independently; the
Phase-2-miss pattern is a recurrence of an existing shape, not a new one

**(a) The vanished informal T9-anchor comparison.** Confirmed directly:
Phase 1 §4-P4 promised "σ_abs(cfg,θ)/σ_ext(cfg,θ) at `BOX_A`, compared
informally to T9's broadside anchor (0.51)... reported, not pre-scored."
Phase 3's renumbering (inserting two new Tier-0 gates as P4/P5) overwrote
this slot; I independently grepped `phase3_synthesis.md`, `run.py`, and
`run_output.txt` for "T9"/"broadside"/"0.51" myself — the only hit is
NOTES.md's own Hypothesis paragraph, cited as motivation, never as a
reported result. Confirmed: dropped without an explicit retirement note.

**(b) The false "reproduced bit-exact this cycle" provenance claim.**
Read `phase1_proposal.md`'s own parameter table directly: the "T9 broadside
anchor" row cites `experiments/057-.../run.py — independently reproduced
bit-exact this cycle by direct invocation of lab.thermo_sidecar (R4)`. The
four cited figures (`sigma_ext_cells=240.0073740162445`,
`p_abs_w=1.7409069740390205e-12`, `dt_ss=2.8601275372385233e-05`,
`699.27×`) match `experiments/057-.../results.json` exactly — but I
searched `run.py` and `run_output.txt` myself for any invocation
reproducing them this cycle: **none exists.** `run.py`'s only
`thermo_sidecar` calls operate on this cycle's own freshly-measured
`sigma_ext_cells`/`ratio_abs_ext` at `BOX_A`, never on exp-057's cited
figures. **Confirmed: these numbers are cited verbatim from exp-057, not
recomputed by anything in this experiment's directory** — exactly the
shape R4 exists to catch.

**A meta-observation this audit adds, not raised by VISION or anyone
else**: the citation's own trailing parenthetical, "(R4)," invokes the very
rule it violates — asserting compliance with R4's independent-verification
standard as the justification for trusting the citation, without the
verification R4 actually requires having been performed. This is worth
naming explicitly: citing a house rule's name is not the same as satisfying
it, and a future reviewer should not treat a bare "(R4)"/"(R9)"-style
citation tag as itself evidence of compliance — it is exactly as checkable,
and exactly as easy to get wrong, as the claim it is attached to.

**Does the "Phase-2-miss, Phase-5-catch" pattern match an existing rule, or
is it new?** Independently assessed: this is NOT a new pattern. It is a
recurrence of the exact shape underlying R4's own addenda (the "144/144"
and "72 cell combinations" instances both survived their own cycle's five
blind Phase-2 critiques before a later re-verification caught them) and
R9's own founding instance (the T16 unit-mismatch "survived one full cycle
as settled fact... until a second, independent blind Phase-5 seat...
caught" it) — in both cases, a Phase-2 layer, Red Team's own Phase-2 audit
included, read past an unverified "reproduced"/"confirmed" claim without
independently invoking the cited function or checking the citation's own
truth, and a later, independent layer (a subsequent cycle's Phase 5, or —
here — the SAME cycle's Phase 5) caught it. **Candor required by this
seat's own charter**: my own predecessor's `phase2_redteam_audit.md` §0
("Housekeeping verification") independently re-checked several other
citations in this cycle's parameter table (`BOX` arithmetic, `DENSE_ANGLES`
indices, `REF`, the FDTD call count) to exactly this standard, but did
**not** check the T9-anchor row's "reproduced bit-exact this cycle" claim
— a real, scoped miss in that audit's own §0 coverage, not a wrong
conclusion about anything it did check. This reconfirms, rather than
supersedes, the existing R4 discipline: Phase 5's genuinely independent
re-verification layer is doing real work even over Red Team's own Phase-2
audit, exactly as this program's layered-review design intends. **Ruling:
no new rule needed — logged here as a fresh, concrete instance
strengthening R4's own existing text, worth citing alongside R4's addenda
the next time this exact citation-hygiene shape recurs.** Neither (a) nor
(b) rises to Checkpoint criterion 4 (both non-load-bearing — the "context
only" row never feeds P7/P8 — and caught blind, same cycle, before
LOGBOOK).

---

## 5. EM's `back_frac`/`fwd_frac` finding — CONFIRMED from source; does
NOT touch this cycle's own scored conclusions

Read `lab/sections.py::widths()` directly. `p_back` is computed at the
box's `x0` face and the function's own comment labels it "backward ...
toward the source" — an assumption baked into the box-face convention that
`x0` (upstream in a +x-propagating scene) is the source-facing side. For
`PAIR_PAD` (`src_x>obj_x`), the source sits on the `x1` side, not `x0` —
confirmed, the labels are inverted for this geometry.

Confirmed also that `back_frac`/`fwd_frac` are **not** touched by
`widths_direction_corrected()`: reading `run.py` directly, the wrapper's
loop only reassigns `sigma_scat`/`sigma_abs`/`sigma_ext`/`sigma_ext_cross`;
`out = dict(w)` copies `back_frac`/`fwd_frac` through unmodified. Confirmed
from `results.json`: both fields ARE persisted at every one of the 12
`(cfg,θ,box)` cells (e.g. `C40_36.0_BOX_A: back_frac=0.6756,
fwd_frac=8.5×10⁻⁵`).

**Does this cycle's own scored conclusion depend on it?** No — confirmed
directly by reading `run.py`'s `main()` in full: P7 (the PRIMARY
classification) and P8 (NETD) are built exclusively from `sigma_ext`/
`sigma_abs` via the `thermo` chain; `back_frac`/`fwd_frac` are read nowhere
in any gate, classification, or reported prediction. **This is a
flagged-forward latent defect in `lab/sections.py` itself, not a defect in
any of this cycle's own scored numbers** — correctly non-blocking, and
correctly named as a forward risk (any future consumer reading
`back_frac`/`fwd_frac` at face value on a −x-propagating scene, especially
for a constraint-2 "no specular return" question, would get the physically
backward answer).

**Ruling: CONFIRMED, non-blocking, log forward.** Does not fire Checkpoint
criterion 4 (no scored claim depends on it; flagged same-shift).

---

## 6. The forward tripwire — independently re-read from LOGBOOK, ruled
genuinely discharged

Located and quoted the literal text myself, LOGBOOK.md Iteration 63 (the
same passage THERMODYNAMICS' Phase-5 review cites — independently
re-located, not taken on trust):

> "now FOUR consecutive cycles deferred/exempt (083–086), SEVEN since
> first named (Iteration 59) — a fifth consecutive deferral without either
> building a purpose-built scene or explicitly retiring the 'next
> scene-bearing cycle' framing fires Checkpoint criterion 4 automatically,
> pre-announced now on the R11 precedent."

Read on its own terms: the condition is disjunctive over **process**
("building... or explicitly retiring the framing"), with no clause
anywhere conditioning on the classification a measurement returns. exp-087
ran 13 real FDTD calls on the already-validated, article-loaded `PAIR_PAD`
(`C40`/`G40`) geometry, at genuine oblique incidence, computing a real
Poynting-box ledger (`sections.widths()`) never before applied to this
scene — confirmed a non-degenerate, well-powered measurement (`n_resolved=
3/3`, noise-floor margins 3.2×–10.7× over the floor). **This unambiguously
satisfies the tripwire's literal condition.** No sixth-deferral concern.

**On the argument that a falsified prediction is MORE credible evidence of
a genuine discharge than a confirming one would be — assessed on its own
merits, not merely endorsed.** The argument is sound, for a specific,
statable reason: the tripwire exists because this cross-check was silently
skipped four times running, precisely the "a program quietly avoiding a
measurement that might embarrass its own prior" failure shape Checkpoint
criterion 4 is chartered to catch (PANEL.md §Checkpoints, item 4:
"unfalsifiable claims, a constraint quietly dropped"). This cycle's own
lead seat (THERMODYNAMICS, by rotation) pre-registered ENERGY-DECOUPLED
with only "moderate confidence," built the real instrument, and reported
the opposite of its own preferred hypothesis. A cycle that predicts X,
"discharges" a tripwire, and finds X is cheap to game (run something
thin, report the comfortable answer, move on); a cycle that predicts X,
builds a genuinely gated instrument (P1/P2/P4/P5/non-negativity, all HALT
points), and reports a well-powered, robust NOT-X against its own leading
hypothesis is hard to fake and costly to fabricate. This is a real,
generalizable epistemic point about incentive structure, not merely a
comfortable post-hoc reading of this one favorable case — I adopt it as
sound.

**Ruling: the tripwire is genuinely discharged, both letter and intent.**
No Checkpoint-4 concern from this matter.

---

## 7. Checkpoint criterion 2 — confirmed N/A

Independently confirmed: no phenomenon-mechanism claim anywhere in this
cycle's record (Phase 1 §3, Phase 3, NOTES.md all state this explicitly and
correctly), no T1 escape-route framing, and the cycle's own scope note
(persisted verbatim in `results.json`) states it touches no constraint
1/2/4 and does not re-score `REALIZABILITY_MEMO.md`. This matches every
T28 instrument/desk cycle since exp-069 (Iterations 59–63 all ruled N/A on
the identical grounds). **Confirmed N/A, not merely not-yet-ripe** — this
is instrument/confound bookkeeping internal to T28's own sub-thread; no
mechanism-class boundary is proposed, tested, or implicated anywhere in
this record.

---

## 8. QUANTUM's candidate standing rule — ADOPTED as new standing rule R13

Independently assessed on its own merits (§2 above re-derives the
underlying arithmetic from scratch). QUANTUM's proposed rule targets a
genuinely distinct failure mode from the existing R5/R10 lineage: R5 (and
its own addendum) and R10 both concern whether an observed match, fit, or
period is *statistically* distinguishable from a null/noise process — a
look-elsewhere or specificity problem that exists because sampling is
finite and noisy. This cycle's own defect exists even at zero measurement
noise: a ratio's denominator, independently established to be a genuine,
smooth, oscillatory, low-noise curve, has real zero-crossings by
construction, and any nonzero numerator divided by a quantity passing
through zero produces an unbounded ratio near that crossing — an algebraic
fact about the ratio's own construction, not a statistical inference about
noise. R5/R10's own machinery (null-permutation controls, circular-shift
tests) targets exactly the wrong failure mode here: a null-permutation
control on `frac_p_abs`'s own noise would not, and could not, catch a
denominator blowing up near its own known zero. This is a genuinely new
failure shape, correctly not folded into R5's family. **Adopted, full text
below, matching the style and rigor of R1–R12.**

> **R13 — a ratio classifier whose denominator is built from a quantity
> independently known (or knowable, zero-FDTD, from already-committed
> data) to have real zero-crossings must be floor-gated on that quantity's
> own absolute or amplitude-normalized magnitude — not merely on the
> numerator's own measurement-noise floor — before a decade/threshold
> classification built on it is trusted at any single sampled point (not a
> ruled-out idea; a standing house-discipline rule, adopted Iteration 64,
> a genuinely new failure mode distinct from the R5/R10 look-elsewhere/
> null-under-noise lineage: R5/R10 concern whether a fitted period, phase,
> or match is statistically distinguishable from noise; this concerns
> whether a pointwise ratio between two independently-sourced curves is
> well-defined at all near a point where one curve is known to pass
> through zero — a problem that exists even at zero measurement noise,
> given only that the reference curve is genuinely oscillatory).**
> exp-087's own pre-registered PRIMARY classification
> (`ratio_k(θ)=frac_p_abs(θ)/frac_contrast(θ)`, ENERGY-DECOUPLED/
> CONSISTENT/ENERGY-DOMINANT/MIXED/DEGENERATE) cleared its own
> noise-floor gate (guarding only the numerator, `p_abs_w`'s own
> `box_dev`-scaled uncertainty) at all 3 sampled angles, including
> `θ=38.6°` — a well-powered, non-degenerate measurement by that gate's
> own standard, margin 4.49× over the floor. But `frac_contrast(θ)`'s own
> denominator, `delta_scene(θ)` (exp-083's own independently-established,
> `p=0.0`-null-controlled, genuinely oscillatory confound curve, period
> ≈2.84–2.95°), crosses zero at `θ₀≈38.590°` — independently re-derived
> twice over (QUANTUM's Phase-5 review; this audit, §2) by linear
> interpolation between the two flanking exp-083 dense-grid points
> (`38.4°→+8.083×10⁻⁴, 38.6°→−4.151×10⁻⁵`) — placing the sampled angle
> `38.6°` a mere `≈0.01°` from the true zero and within `≈0.053°` of the
> point where `ratio_k` itself crosses the classifier's own
> `RATIO_HIGH=10` decade boundary, a quarter of this cycle's own `0.2°`
> grid step. `frac_p_abs(38.6°)` itself showed no compensating anomaly —
> it read 7.4% BELOW its own smooth interpolated trend — ruling out a
> genuine numerator-side spike coinciding by chance with the node. The
> `ratio_k=53.99` reading that alone drove this cycle's ENERGY-DOMINANT
> classification (under the pre-registered "any resolved angle over
> `RATIO_HIGH`" veto priority) is, on the balance of this quantitative
> evidence, better explained as a mathematically near-inevitable
> consequence of sampling within a quarter-grid-step of a known
> denominator zero than as new physics — disclosed, not adopted, by
> NOTES.md itself, and independently confirmed sufficient by three
> separate seats (PHOTONICS, QUANTUM, THERMODYNAMICS) plus this audit.
> **Rule: before a decade/threshold classification is built on a ratio
> whose denominator derives from a quantity with known or knowable real
> zero-crossings, the pipeline must apply a floor gate on that
> denominator's own absolute or amplitude-normalized size (a house-style
> convention, disclosed as such — matching this program's own existing
> `3×box_dev`/`0.1×`/`10×` precedent for undisclosed-rigor thresholds
> elsewhere) — an angle failing this gate is reported as its own outcome
> (e.g. `UNRESOLVED-BY-CONSTRUCTION`/`NODE-UNRESOLVABLE`), excluded from
> classification, never silently scored alongside angles that cleared
> it.** A cycle that ships a ratio-classifier decade/threshold verdict
> built on a real-zero-crossing-capable denominator without this floor
> gate, when the denominator's own zero-crossing later proves
> outcome-determining, fires Checkpoint criterion 4 automatically, no
> further deliberation — matching R6–R12's own "known, named, ignored"
> standard, once this rule's text has been logged. **Does not fire on its
> own founding instance** (exp-087) — matching R5/R6/R9/R10/R11/R12's own
> precedent that a rule's founding/consolidating cycle establishes the
> standard rather than retroactively violating it. Full record:
> `experiments/087-t28-energy-interception-poynting-check/
> phase5_review_quantum.md` §1–§5, `phase5_redteam_audit.md` §2/§8,
> LOGBOOK.md Iteration 64.

---

## 9. Checkpoint rulings, consolidated

- **Criterion 2: N/A**, confirmed independently (§7).
- **Criterion 4: does NOT fire** on any of the five matters this audit and
  the six Phase-5 reviews found (the "first-ever `src_x>obj_x`" historical
  error, §1; the third disclaimer-erosion instance, §3; the vanished
  T9-comparison and the false "reproduced bit-exact" citation, §4; the
  `back_frac`/`fwd_frac` inverted-label defect, §5; the θ=38.6° denominator-
  fragility finding, §2/§8) — every one is non-load-bearing to this
  cycle's own scored PRIMARY/detectability verdicts, and every one was
  caught blind, independently, before this LOGBOOK entry, matching this
  program's own established non-firing test.
- **The tripwire (Iteration 63, energy-interception cross-check): genuinely
  discharged**, letter and intent (§6).
- **New forward tripwire, adopted (§3)**: a fourth instance of the
  inline-disclaimer-erosion shape fires Checkpoint criterion 4
  automatically.
- **New standing rule R13, adopted (§8)**: full text above.

---

## Combined Verdict: **PARTIAL**

Unanimous across all six blind Phase-5 seats and this final audit. The
tripwire is genuinely discharged with a real, purpose-built, well-powered,
gated FDTD measurement (§6) — the honest kind of discharge, not a thin
substitute, and the falsified prediction is itself evidence of that
honesty rather than a weakness of the result. The PRIMARY metric is
genuinely FALSIFIED: the pre-registered ENERGY-DECOUPLED hypothesis fails
at the two aliasing/node-clean angles alone (CONSISTENT, `ratio_k`∈
{2.64,5.71}), and fails more strongly if the disputed `θ=38.6°` reading is
credited at face value (ENERGY-DOMINANT, the filed classification, correct
per the frozen pre-registered pipeline). This is a materially new,
robust finding that updates this sub-thread's own ten-plus-cycle
phase/interference-only prior — bulk-integrated absorbed power and
localized Weber contrast are, at minimum, comparable-order-of-magnitude
coupled at this bench geometry, not decoupled as ten-plus cycles of
convergent phase evidence had made the corroborative, moderate-confidence
default assumption. Checkpoint criterion 2 is correctly N/A — this is
instrument/confound bookkeeping internal to T28, not phenomenon-mechanism
work, and touches no constraint directly. Checkpoint criterion 4 does not
fire on any of five independently-found gaps, all non-load-bearing, all
caught same-cycle before LOGBOOK — genuinely the layered-review process
working as designed, at real density (a fourth consecutive T28 cycle where
several near-misses close inside one cycle's own Phase-5 layer without any
individually clearing the firing bar, matching Iteration 63's own named
governance observation). Not RULED OUT (no mechanism class foreclosed by
anything here) and not PROMISING (this cycle makes no constraint-3 ledger
progress toward the phenomenon target by its own explicit, correctly-kept
scope) — PARTIAL is the correct, precedented label for genuinely new,
informative, non-conclusive instrument-fidelity work on this sub-thread
(matching exp-082/083/085/086's own convention).

---

## Reconciled, tiered ranking of candidate directions for Iteration 65
(synthesizing all six Phase-5 reviews' own rankings)

**Tier 0 — zero FDTD, same-shift corrections, before this record is cited
elsewhere:**

1. Insert idealization 9's NETD disclaimer inline at NOTES.md's Predictions
   §8 and Result P8 restatements (VISION, §3) — and log the new forward
   tripwire (§3) in PLAN.md/LOGBOOK alongside it.
2. Correct or re-caption the T9 "reproduced bit-exact this cycle" citation
   in `phase1_proposal.md`'s parameter table (VISION/this audit, §4) —
   either actually invoke `lab.thermo_sidecar` on exp-057's own inputs, or
   correct the caption to "cited verbatim from exp-057, not re-invoked."
3. Restore the dropped informal T9-anchor comparison as an explicit
   disclosed-context line — the values (`ratio_abs_ext`≈0.5128–0.5138,
   within 0.55%–0.75% of T9's 0.51 broadside anchor) already sit in
   `results.json`, computed for free (VISION §4a; MATERIALS §0, §3 item 3).
4. Correct the "first-ever `src_x>obj_x`" claim in `run.py`'s docstring and
   NOTES.md's Result section (this audit, §1; EM) — log that exp-024
   (Iteration 2) most likely carried the identical defect, silently
   defended by ad hoc `abs()` wrapping, never diagnosed.
5. Disclose the `back_frac`/`fwd_frac` inverted-label defect inline
   wherever this cycle's `widths` data is next cited (EM, §5).
6. Formalize THERMODYNAMICS' swing-specific NETD recomputation (§7 of its
   review) as a named, committed check, and log the `iso_xsec_sq`-vs-rod-
   convention sensitivity (~1.5–2× on `ratio_k`'s numeric value, not its
   classification) as a standing citable caveat wherever this cycle's
   exact `ratio_k` figures are next quoted.
7. Transcribe R13's finalized text into LOGBOOK's RULED OUT registry (this
   audit, §8).

**Tier 1 — cheap FDTD, near-unanimous next, bundle together:**

1. **The decisive 8-call bracketing follow-up at θ=38.4°/38.8°**
   (QUANTUM, §4 of its review) — cheapest, fastest, single most decisive
   next step: resolves whether `θ=38.6°`'s ENERGY-DOMINANT reading is a
   node artifact or genuine sharply-localized physics, pre-registered
   falsification criterion already stated (both neighbors land
   `[0.1,10]` ⇒ artifact confirmed; either neighbor also reads
   ENERGY-DOMINANT ⇒ artifact explanation refuted, a major finding).
2. **Extend the energy-interception channel to the full (or
   substantially denser) 31-point/0.2° `PAIR_PAD` window at 600nm**
   (near-universal top pick: PHOTONICS #1, THERMODYNAMICS #1/#3, VISION
   #2/#3), computing `σ_abs(C40,θ)` and `σ_abs(G40,θ)` **individually**,
   not merely their PAD-difference (MATERIALS' §1/§3 "passive transducer,
   not resonant source" falsifiable test — does each series alone stay
   smooth while their difference reproduces the oscillation), reusing
   `sc.widths()`/`BOX_A` verbatim and re-applying the corrected
   classification pipeline (including R13's new denominator floor gate)
   across the dense grid.
3. Apply R13's denominator floor gate to this cycle's own already-
   collected 3-angle data and report the corrected classification (zero
   new FDTD) — a permanent instrument improvement independent of how
   item 1 above resolves (QUANTUM §7 item 2).

**Tier 2 — cheap FDTD/instrument generalization, standing:**

1. Institutionalize the newly-validated extinction-routes-agreement
   identity for `graded_black_shell`, obliquely, as a permanent stage-8
   suite row (`xi_k`, matching the existing `xi_p`/`xr`/`xi_u` rows) —
   PHOTONICS §Ranked-directions item 2, a real new fact this cycle proved,
   currently a one-off P4 check the next `graded_black_shell`-oblique
   cycle would have to re-earn from scratch.
2. Extend the validated energy-interception measurement to
   `PAIR_ABSORB40`/`C80−C40` and to 450/750nm (EM item 4; MATERIALS item
   1's own generalization) — the CONSISTENT/ENERGY-DOMINANT coupling this
   cycle found needs a second config/wavelength before it generalizes past
   one geometry.
3. Extend the same measurement to the near-null σ(I) article (`off_pass`,
   τ_off≈0.0065) — MATERIALS item 2: the article class that actually
   matters for constraint-3 realizability, unlike the flagship absorber
   this cycle correctly scoped as a T28 confound-diagnostic geometry only.
4. A bounded audit of whether any OTHER cited T28 ratio construction
   (`amp_ratio`, `frac_contrast` itself, others) shares R13's real-zero-
   crossing-denominator hazard, unguarded — QUANTUM §7 item 3, in the
   spirit of R11's own bounded historical scan.

**Tier 3 — standing, overdue board items, unaffected by this cycle, carried
forward unchanged:**

1. PHOTONICS' grazing-incidence validity check on
   `edge_diffraction_c_empty_corrected` — still the single highest-ranked
   standing item on the whole T28 board (near-unanimous #1 across six of
   seven seats at Iteration 63's own close; VISION's Phase-5 review
   reconfirms it unaffected and still top-ranked).
2. The x-wall wavelength-generality leg — now **TWELVE** consecutive
   cycles deferred (076–087), the single oldest item on the whole board.
3. The still-queued full-scale (60,001-call) null-calibration re-run (2 of
   3 parts done per Iteration 63).
4. R12-into-standard-practice (multi-seed corroboration for any future
   "negligible effect" claim on a tail statistic).
5. PHOTONICS' domain-truncation test for leg (b)'s Anchor 2 / EM's
   matrix-valued RS/Kirchhoff kernel rebuild.
6. QUANTUM's lossless-PEC-only-disk control.
7. Consider hardening `lab/sections.py::widths()` itself to normalize by
   `abs(i_inc)` internally, with a new stage-8 gate on a synthetic
   −x-propagating scene (EM item 5) — now TWO independent instances
   (exp-024, exp-087) of this exact geometry tripping the same latent
   issue; scope as its own small, gated `lab/`-change proposal, not a
   same-shift patch.
8. The still-unresolved ritualization governance question (named
   Iteration 61: does the R6–R12 escalating-tripwire format need a
   scope-applicability clause before further firings dilute the signal?).

**Tier 4 — governance:**

1. Checkpoint criterion 2 ruled N/A, confirmed independently (§7).
2. Checkpoint criterion 4 ruled non-firing on all five matters adjudicated
   this cycle (§9); one new forward tripwire set (a fourth
   disclaimer-erosion instance, §3).
3. New standing rule **R13** adopted (§8) — a genuinely new failure mode
   (denominator zero-crossing ratio fragility), distinct from R5/R10.
4. The historical-accuracy correction to the "first-ever `src_x>obj_x`"
   framing (§1), and the meta-observation that a bare rule-name citation
   ("(R4)") is not itself evidence of compliance (§4) — both logged as
   reinforcing existing R4 discipline, not requiring a new rule.
