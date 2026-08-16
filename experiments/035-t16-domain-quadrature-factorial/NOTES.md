# exp-035 — Closing the R156/N17_156 Domain × Quadrature Factorial, Rebuilding N17_NATIVE, and Reconciling T15

Panel Iteration 12 · Runner: cloud panel shift · Lead: QUANTUM OPTICS (rotation)

## Hypothesis

Iteration 11 (exp-034) closed one live thread (T1's cpl=40 floor/currency
convergence) but opened a new one, **T16**: two stacked, unresolved
instrument confounds — a domain-construction effect (3.552×10⁻⁴) and an
angular-quadrature effect (4.2485×10⁻⁴) — sit directly under this program's
only-ever constraint-3 PASS citation at r=156, and neither the r=78-native
N17 rebuild (Red Team's own mandatory fix 5) nor a formal reconciliation of
T15 (g₀'s chord-model deficit) was completed cleanly. This cycle tests
whether the domain and quadrature effects are additive or interact (the
missing cell of a 2×2 factorial), rebuilds the r=78-native N17 domain by the
construction method that actually backs the PASS citation, and reconciles
T15 using a corrected, code-verified desk computation. No new mechanism, no
new σ law — this is instrument-hygiene work, continuing the pattern of
Iterations 9–11.

## Phase 1 — Proposal (QUANTUM OPTICS, abridged)

Full verbatim proposal text: this file's git history / LOGBOOK.md
Iteration 12. Summary: three blocks. **Block T16_CLOSE** — the missing
cell of the r=156 domain×quadrature 2×2 (N17 angles on exp-034's own
R156 domain, verbatim, GUARD_OUT=336), 34 new calls. **Block
N17_NATIVE_V2** — the r=78-native/cpl=30 N17 rebuild, this time on
exp-033's own actual domain (RATIO=1.5 method, GUARD_OUT=278), not
exp-034's ad-hoc `_coverage_geometry()` formula, 34 new calls. **Block
T15_RECONCILE** — zero-FDTD-cost reconciliation of the three
"zero-free-parameter" g₀ chord-model numbers this program has produced,
using the one that is actually reusable code (`chord_model_g0`), across
cpl=20/30/40 at r=78/117/156. QUANTUM OPTICS corrected Red Team's own
Iteration-11 cost estimate for priority 1 (≤17 calls → 34 calls) after
verifying the raw per-angle profile data needed to "top up" an existing
9-angle reading to 17 angles does not survive anywhere in the repo —
`results.json` only ever persists aggregated contrasts.

## Phase 2 — Critique (five blind, then Red Team) — summary

Full verbatim critiques: LOGBOOK.md Iteration 12. All five blind seats
(PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE)
independently verified the proposal's geometry/σ/call-count arithmetic
against the actual code — every field checked out. Each returned
**support-with-changes**:

- **PHOTONICS** found the single most consequential defect in the packet:
  Block T15_RECONCILE's cpl=40 "measured g0/A" cell (0.687124) does not
  exist anywhere in the codebase — `block_cpl40()` never computes a g0/A
  ratio, and the stated number matches, to 7 significant figures, the
  r=117 chord-model value one column over — a copy/paste, not a
  measurement. Under the correct number the gap is GROWING, the
  **opposite** of the proposal's central "T15 closes" prediction.
- **MATERIALS** found the entire 68-call budget refines a C-reading whose
  realizability verdict is algebraically orthogonal to it, and that the
  proposal silently drops the literature-check condition PLAN.md names for
  escalating the realizability memo toward Checkpoint-2.
- **ELECTROMAGNETISM** found Block T16_CLOSE's interaction verdict is
  gated only by an aggregate empty-scene check, while R156's domain has
  never been angle-tested past ±35° and the two new N17 angles most
  responsible for the N9→N17 delta are exactly ±40° — the historically
  artifact-prone span (exp-024/T7) that survived margin-widening before.
- **THERMODYNAMICS** found the proposal never mentions the THERMO sidecar
  at all (silent, not explicit — the same failure mode that caused
  exp-034's own real regression), and that Block C's "T15 reconciliation"
  ignores the parallel, LOGBOOK-named unreconciled amplitude pair
  (`chord_absorptance()`'s π/4 vs `chord_model_g0()`).
- **VISION SCIENCE** found N9 and N17 are still only two points on an
  angular-convergence sequence (N9 a strict code-asserted subset of N17),
  and that the proposal's own framing ("does the corrected delta still
  exceed the margin, using N17 as reference") silently promotes N17 from
  "next sample" to "ground truth" rather than closing VISION's own
  Iteration-11 concern (a genuine N9→N17→N33 sequence).

**Red Team (PROCEED-WITH-MANDATORY-FIXES).** Independently re-derived every
load-bearing number in the packet, including all five critiques' own
claims. Confirmed PHOTONICS' cpl=40 catch to the digit, and went one step
further: even PHOTONICS' own literal fix ("a genuine, correctly-signed
C_empty(cpl=40) derivation") is not actually zero-cost — `block_cpl40()`
discards its signed C_empty and never persists per-angle arrays, so that
fix would cost ~9 new FDTD calls. Red Team supplied a genuinely zero-cost
alternative instead: raw g=|C|/τ at all three resolutions (all already
published), independently confirming PHOTONICS' GROWING direction by a
second route. Accepted THERMODYNAMICS' π/4-amplitude extension as
mandatory (zero cost). Accepted ELECTROMAGNETISM's per-angle ±40°
check as mandatory (zero additional cost — reuses data already captured
inside `block_n17`'s own `scenes` dict). **Rejected** MATERIALS' "silently
violated" framing (the PLAN.md clause is explicitly conditional and the
condition never fires) but kept the one-sentence disclosure as harmless
hygiene. **Rejected** VISION's proposed fix as specified (N9 is a
zero-marginal-cost byproduct of the N17 run, not a separate 17-call leg —
swapping it for a genuine N33 leg would grow the cycle's budget from 68 to
~100 calls, +47%, not a free substitution) but accepted the substance:
NOTES.md must state N17 is still only the second point of an eventual
three-point sequence and queue N33 as Iteration-13's top-ranked item, not
defer it uncredited.

## Phase 3 — Synthesis (Director)

**All of Red Team's mandatory fixes accepted**, none overridden:

1. **[ACCEPT, MODIFIED per Red Team's own recipe]** PHOTONICS' cpl=40
   catch is real and load-bearing. Fixed not as PHOTONICS literally
   specified (which would have cost ~9 new calls, breaking the zero-cost
   claim) but per Red Team's own zero-cost alternative: `block_t15_reconcile()`
   now uses raw g=|C_off_pass|/τ at cpl=20/30/40 (0.692743 / 0.705609 /
   0.707928 — all three already published in exp-032/033/034's own
   `results.json`), each against `chord_model_g0()` evaluated at that
   resolution's own geometry. Independently re-verified in
   `design_geometry.py`'s own module self-check before being trusted:
   gaps 1.025% / 2.690% / 3.067% — monotonically **GROWING**, confirming
   PHOTONICS' and Red Team's shared correction.
2. **[ACCEPT]** THERMODYNAMICS' π/4-vs-chord-model-amplitude extension
   added to Block T15_RECONCILE — zero cost, `chord_absorptance()` is a
   pure function of τ.
3. **[ACCEPT]** ELECTROMAGNETISM's per-angle ±40° empty-scene check added
   to `block_n17()` for BOTH Block T16_CLOSE and Block N17_NATIVE_V2 (the
   risk EM named for R156's un-widened domain applies equally to
   N17_NATIVE_V2's un-widened exp-033 domain) — computed from data already
   captured in the `scenes` dict, zero additional FDTD cost. Explicitly
   labeled **advisory**, not a previously-validated gate (bound: 0.04,
   this program's own established single-oblique-angle precedent, stage
   9's own ±15° empty-window-balance gate — the loosest analog available,
   disclosed as an extrapolation, not a matched precedent).
4. **[ACCEPT, hygiene]** MATERIALS' disclosure sentence added inline to
   `results.json`'s `meta` block and restated here: this cycle's T15 work
   does not address, and is not a substitute for, the REALIZABILITY_MEMO's
   still-open literature check.
5. **[ACCEPT substance, REJECT literal fix]** VISION's N9→N17→N33 concern
   is correct and unresolved by this cycle — but literally swapping the
   (free) N9 leg for a (34-call) N33 leg would grow this cycle's budget by
   47%, which Red Team ruled out on the same budget-discipline grounds it
   applied to its own Iteration-11 close. NOTES.md (this document, Idealizations
   and Next sections) states explicitly that N17 is the second, not final,
   point of the convergence sequence; N33 is queued as Iteration-13's
   top-ranked item.

**No criticism was overridden.** Every mandatory fix landed at zero or
near-zero marginal FDTD cost; total budget stays **68 new FDTD calls**,
unchanged from the Phase-1 proposal (34 + 34 + 0).

**Predictions P-T16-1/2/3, P-N17V2-1/2/3/4, and the (already-computed,
desk-only) T15_RECONCILE disposition are committed below, in this file,
BEFORE any new FDTD call runs** (house discipline, non-negotiable).

## Parameter tables

### Block T16_CLOSE (34 new calls)

| Field | Value |
|---|---|
| Domain source | exp-034's own Block R156, **verbatim** (not rebuilt) |
| R_OUT | 156 cells |
| PLANE_DX | 15 cells |
| GUARD_OUT | 336 |
| FLANK | (336, 492) |
| NY / NX | 2480 / 660 |
| CPL | 20 |
| STEPS_AMBIENT | 2706 (reused, settling-validated in exp-034) |
| Angle set | N17 (17 angles, 5° step, ±40°) |
| Article | off_pass only, τ_center=0.0065, σ=2.083333×10⁻⁵ |
| Reuses | 3 of the 4 cells of the domain×quadrature 2×2 (exp-034's own `results.json`); this block runs the 4th |

### Block N17_NATIVE_V2 (34 new calls)

| Field | Value |
|---|---|
| Domain source | exp-033's own domain, **verbatim** (RATIO=1.5 method) |
| R_OUT | 117 cells (=78×1.5) |
| PLANE_DX | 22 cells (=15×1.5, exp-033's own rounding) |
| GUARD_OUT | 278 (=185×1.5, exp-033's own rounding — NOT exp-034's ad-hoc 295) |
| FLANK | (278, 395) |
| NY / NX | 2376 / 540 |
| CPL | 30 |
| STEPS_AMBIENT | 2100 (reused verbatim from exp-033) |
| Angle set | N17 (17 angles, 5° step, ±40°) |
| Article | off_pass only, τ_center=0.0065, σ=2.777778×10⁻⁵ |
| Established comparator | C(N9)=−0.004586460833023719 (exp-033), margin=4.1354×10⁻⁴ |

### Block T15_RECONCILE (0 new calls)

| cpl | r_out | g_raw (published) | source |
|---|---|---|---|
| 20 | 78 | 0.692743113607875 | exp-032 `results.json::g_values["off_pass/600"]` |
| 30 | 117 | 0.705609358926726 | exp-033 `results.json::g_raw["off_pass"]` |
| 40 | 156 | 0.707928 (=0.004601531803829529/0.0065) | exp-034 `results.json::block_cpl40.C_off_pass_cpl40` |

Each compared against `chord_model_g0()` (reused verbatim from exp-034)
at its own resolution's geometry, plus THERMO's π/4=0.785398 amplitude
comparison at the same three geometries.

## T1 escape-route statement

Exclusively **σ(I) intensity gating**, OFF-state (low-intensity) branch.
Every article in this cycle is off_pass at τ_center=0.0065 — the same
OFF-state operating point already claimed (exp-032) as the program's
only-ever constraint-3 PASS. Nothing here touches σ(x,t) switching,
angular selectivity, or sub-threshold operation.

## Predicted outcomes (falsifiable bands, committed BEFORE the scored run)

**P-T16-1 (interaction verdict, the load-bearing prediction of this
cycle).** interaction = [C(N17,R156dom) − C(N9,R156dom)] −
[C(N17,N17_156dom) − C(N9,N17_156dom)], where the second bracket
(+4.2485×10⁻⁴) is already known from exp-034. |interaction| ≤ 1×10⁻⁴ →
CONFIRMED-ADDITIVE; |interaction| ≥ 2×10⁻⁴ → REAL INTERACTION; between →
INCONCLUSIVE. **Central estimate: CONFIRMED-ADDITIVE**, C(N17,R156dom) ≈
−0.005335 (additive prediction), staying **MARGINAL** — the historical
MARGINAL headline on the program's actually-precedented domain survives,
and N17_156's own PASS reading is substantially a domain-choice artifact.

**P-T16-2 (aggregate coverage gate).** Central estimate: PASS, C_empty in
[0.0005, 0.003]. If FAILS (>0.005): P-T16-1's decomposition becomes
untrustworthy — R156's own established domain cannot support angular
convergence testing without first being widened.

**P-T16-3 (per-angle ±40° advisory, NEW instrumentation, mandatory fix
3).** Central estimate: PASS at both ±40° individually (|C_empty|≤0.04),
but genuinely uncertain (directional confidence ~55–65%, not high) —
this is the first time this program has looked at a single-angle empty
reading at exactly this span on this domain. A FAIL here does not
invalidate P-T16-1's arithmetic but downgrades confidence in its
interaction verdict, per EM's own mandatory-fix intent.

**P-N17V2-1 (N9 leg, free byproduct of the N17 run).** Predict exact
reproduction of exp-033's own established C_off_pass(cpl=30,N9) =
−0.004586460833023719 (bit-identical, |Δ|<10⁻⁹).

**P-N17V2-2 (N17 leg — the actual rebuild).** exp-034's own ad-hoc
N17_NATIVE reading is NOT carried forward as a point estimate (its own N9
leg missed the true established citation by 2.32×10⁻³, over half the
entire off_pass signal — strong evidence that domain sampled different
near-field structure altogether, not merely a differently-margined
version of the correct one). **Falsifiable band:** |ΔC(N9→N17)| on
exp-033's own correctly-rescaled domain lands in **[3×10⁻⁴, 2×10⁻³]**
(bracketing r=156's clean 4.2×10⁻⁴ on the low end and the uninformative
ad-hoc reading's 1.5×10⁻³ on the high end). **Central-direction
prediction:** quadrature convergence moves |C| toward zero (PASS-ward),
matching the r=156 pattern. **Central prediction: the corrected delta
still exceeds N17_NATIVE_V2_MARGIN (4.1354×10⁻⁴) → YES** — reconfirming
(on now-trustworthy footing) that N9 is inadequate at r=78-native, while
retiring exp-034's own untrustworthy ad-hoc number.

**P-N17V2-3 (coverage gate).** Central estimate: PASS, C_empty in
[0.0006, 0.002].

**P-N17V2-4 (per-angle ±40° advisory).** Central estimate: PASS at both
±40° individually, same confidence caveat as P-T16-3.

**T15_RECONCILE disposition (already computed, desk-only, disclosed here
as a pre-run correction, not a falsifiable prediction subject to a future
measurement — the Phase-1 proposal's original central estimate is
**WITHDRAWN** as based on a fabricated number).** Corrected computation:
gaps 1.025% (cpl=20) / 2.690% (cpl=30) / 3.067% (cpl=40) →
**GROWING** (gap(40)=3.067% > 1.5×gap(20)=1.538%) → **T15 modestly
REOPENS**, not closes — a real, resolution-persistent ~2–3× gap growth
survives across every resolution this program has measured the OFF-state
calibration at, though still far smaller in absolute terms than
Iteration-10's original ~15% claim (already independently refuted at
r=78-native, 0.56%, by exp-034's own committed chord model). THERMO's π/4
amplitude sits a stable ~14.3–14.5% above `chord_model_g0()` at all three
resolutions — a SEPARATE, larger, apparently resolution-independent gap
between the two chord-idiom amplitudes this program has committed to
code, unexplained, newly disclosed as its own open question (not
conflated with the g0-vs-g_raw gap above).

## Idealizations (lab convention, stated in full)

1. ε_r≡1 (gas/aerosol host, n−1≲10⁻⁵) throughout — restated per headline,
   fifth recurrence of this program's own mandatory fix (see
   `results.json::meta.eps_r_idealization_note`).
2. `lab.ambient`'s incoherent multi-angle sum is a linear-medium proxy for
   the σ(I) OFF state specifically (a fixed, disabled scatterer) — not a
   measurement of a full nonlinear switching cycle.
3. `chord_model_g0()` is a zero-free-parameter ray-optics null with its
   own O(1/r_out) discretization floor (named in exp-034/Iteration 11) —
   a comparator, not ground truth.
4. The per-angle ±40° empty-scene advisory bound (0.04) is a NEW,
   informally-extrapolated threshold (this program's own ±15°
   single-oblique-angle precedent, stage 9), not a previously-validated
   N=1/±40°-specific gate. A pass or fail here should be read as
   informative, not dispositive, until this program builds a real
   per-angle floor characterization.
5. STEPS_AMBIENT reused unchanged from each block's source geometry
   (settling-validated there, not re-verified fresh here).
6. **N17 is the second, not the final, point of an eventual three-point
   (N9→N17→N33) angular-convergence sequence.** Nothing in this cycle
   distinguishes "N17 has converged" from "N17 is still meaningfully short
   of N33, the same way N9 was short of N17" — VISION's own Iteration-11
   and Iteration-12 finding, not resolved here on cost grounds (Red
   Team's ruling), queued as Iteration-13's top-ranked item.
7. This cycle's T15 reconciliation does not address, and is not a
   substitute for, REALIZABILITY_MEMO.md's still-open literature check —
   D_req and the TPA irradiance gap are algebraically orthogonal to the
   ambient-contrast readings refined here.
8. THERMO's sidecar constants (`THERMO_ABSORBED_FRACTION`,
   `THERMO_DT_STEADY_K`, transient-ΔT machinery) for τ_center=0.0065 carry
   forward UNCHANGED from exp-034 — cited, not recomputed, since Blocks
   T16_CLOSE/N17_NATIVE_V2 hold τ_center fixed and every sidecar quantity
   is a pure function of τ_center (r_out cancels via σ=τ/(2·r_out)).

---

*Predictions above committed to git before Phase 4's first new FDTD call
(`ed6d007`), per house discipline.*

## Phase 4 — Results

68 new FDTD calls, 2724.3s (~45.4 min) — above the 25.5-min estimate
(Block T16_CLOSE alone ran 1816.6s vs its own ~1019s estimate, ~1.8×; Block
N17_NATIVE_V2 ran 907.6s vs its own ~513s estimate, ~1.8×; a consistent
per-call underestimate, not a divergent one — flagged honestly, not
material to any gate). Trust suite re-verified 46/46 green immediately
before and after the run, no `lab/` diff. No new suite stage needed (no new
engine machinery this cycle).

**Block T16_CLOSE.** Coverage gate: **PASS** (C_empty=7.092×10⁻⁴, inside
predicted [0.0005,0.003] — **P-T16-2 CONFIRMED**). Per-angle ±40° advisory:
**PASS** at both angles (−1.050×10⁻³, −6.942×10⁻⁴, both ≪0.04 —
**P-T16-3 CONFIRMED**). C(N9,thisdomain)=−0.005759806872194646 — exact
bit-identical reproduction of exp-034's own R156 off_pass reading (free
determinism check, as this program's own P-R156-4 precedent predicted).
**C(N17,R156dom)=−0.005124028047369093.** Additive prediction was
−0.005335; **interaction = +2.109×10⁻⁴ — at the REAL-INTERACTION boundary
(≥2×10⁻⁴) — P-T16-1's central estimate (CONFIRMED-ADDITIVE) is REFUTED.**
The domain-construction and angular-quadrature confounds disclosed at
Iteration 11 are **not independent** — this is the falsifiable band's own
named alternate outcome, pre-registered as "diagnostic of the near-field-
fringe hypothesis T10/T12," not an unanticipated surprise. The practical
bucket verdict still matches the qualitative central prediction: C(N17,
R156dom) stays **MARGINAL**, not PASS — the interaction is real but not
large enough to flip the ladder bucket at this geometry.

**Block N17_NATIVE_V2.** Coverage gate: **PASS** (C_empty=9.266×10⁻⁴,
inside predicted [0.0006,0.002] — **P-N17V2-3 CONFIRMED**). Per-angle ±40°
advisory: **PASS** at both angles, but an order of magnitude larger in
magnitude (−1.229×10⁻², −1.271×10⁻²) than Block T16_CLOSE's own
(−1.050×10⁻³, −6.942×10⁻⁴) — both still ≪0.04, so the advisory itself does
not fail, but this asymmetry is a new, unscored observation (below).
C(N9,thisdomain)=−0.004586460833023719 — **exact bit-identical
reproduction of exp-033's own established citation, delta=0.0 exactly —
P-N17V2-1 CONFIRMED to the last printed digit.** **C(N17)=
−0.005238648461746709.** delta(N9→N17)=6.522×10⁻⁴, inside the predicted
falsifiable band [3×10⁻⁴,2×10⁻³] — **P-N17V2-2's band CONFIRMED.** The
delta exceeds N17_NATIVE_V2_MARGIN (4.135×10⁻⁴) — **P-N17V2-2's central
"exceeds margin" prediction CONFIRMED.** But the **directional**
sub-prediction (quadrature convergence moves |C| toward zero, PASS-ward,
matching the r=156 pattern) is **REFUTED**: |C| moved AWAY from zero, the
same direction exp-034's own untrustworthy ad-hoc reading showed, not the
opposite. **Consequence: this program's own headline, first-ever
constraint-3 σ(I) OFF-state PASS (exp-032, Iteration 9, reconfirmed at
cpl=30 by exp-033) downgrades from PASS to MARGINAL** the moment N9 is
replaced by N17 on a correctly-constructed domain — the FIRST time this
downgrade has been shown cleanly, without a domain-construction confound
riding underneath it (exp-034's own N17_NATIVE attempt could not
distinguish domain artifact from quadrature effect; this block can, and
the domain gate here is clean).

**Block T15_RECONCILE** (0 new calls, desk-only, disposition already
computed and disclosed in Phase 3 as a pre-run correction): gaps 1.025% /
2.690% / 3.067% at cpl=20/30/40, **GROWING** — T15 modestly reopens. π/4
peak-chord amplitude sits a stable 14.30–14.55% above `chord_model_g0()`
at all three resolutions, a separate, apparently resolution-independent
gap, unexplained, newly disclosed as its own open question.

**New, unscored observation (not pre-registered, flagged not overclaimed):**
the per-angle ±40° empty-scene bias is ~12–18× larger in magnitude at
r=78-native (N17_NATIVE_V2, ~−0.0123 to −0.0127) than at r=156
(T16_CLOSE, ~−0.0007 to −0.0010), even though both pass the same loose
advisory bound. This tracks the same direction as T16/T10/T12's own
standing finding that r=78-native's instrument uncertainty exceeds
r=156's (e.g. the N5-vs-N9 quadrature bound was 3.2× at r=78-native vs
0.88× at r=156) — consistent with, not yet proof of, PHOTONICS' own
Iteration-11 suggestion connecting the angular-quadrature sensitivity to
the standing near-field-fringe hypothesis (T10/T12). Not folded into any
scored verdict here; a candidate target for a future dedicated per-angle
floor characterization (T11's own still-open item, extended to this
channel).

## Learned

1. **The two disclosed Iteration-11 confounds (domain, quadrature) are not
   additive at r=156 — they interact** (+2.109×10⁻⁴ interaction, at the
   REAL-INTERACTION threshold). This program's first genuine 2×2
   factorial on an instrument-uncertainty question came back non-trivial:
   the confounds compound in a way a linear correction would have
   mis-predicted, even though the practical PASS/MARGINAL bucket happened
   not to flip this time. A future cycle should not assume additivity of
   stacked instrument confounds without testing it, per this result.
2. **This program's only-ever constraint-3 PASS does not survive proper
   N17 correction at EITHER geometry it has ever been measured at.**
   r=156 was already shown fragile at Iteration 11 (with a domain
   confound riding underneath); this cycle shows the SAME downgrade at
   r=78-native — the geometry the PASS citation actually originates from
   — cleanly, with the domain confound resolved (bit-identical N9
   reproduction proves the domain is correctly built). VISION's own
   Iteration-11/12 concern ("a 9-angle discrete sum is NOT adequate for
   this program's own bar") is now confirmed at the ONE geometry that
   matters most for the headline citation, not just at r=156.
3. **T15 does not close as a discretization artifact — it modestly
   reopens**, once the original proposal's fabricated cpl=40 comparator
   is corrected. The gap (raw g vs `chord_model_g0`) grows monotonically
   with resolution across all three points this program has ever
   measured (1.03%→2.69%→3.07%), a real, small, resolution-persistent
   effect, un-mechanism-explained. This is 5–8× smaller than Iteration
   10's original, already-refuted ~15% claim, so it does not resurrect
   that number — but it is not zero, and not shrinking.
4. **A newly-disclosed, separate ~14.3–14.5% gap exists between THERMO's
   π/4 peak-chord amplitude and every `chord_model_g0()` value** — stable
   across all three resolutions (unlike the g_raw-vs-chord-model gap,
   which grows). Two different chord-idiom amplitudes this program has
   committed to code disagree by a roughly constant amount; not yet
   understood, not yet connected to any live thread beyond T15's own
   "two extinction amplitudes...unreconciled" language.
5. **This cycle's own compute estimate undershot by ~1.8× uniformly** (both
   34-call blocks, not just one) — worth a standing note for future
   budget estimates on this exact per-call/per-angle harness shape,
   though not large enough to be a Checkpoint-3 "major build" trigger.
6. Red Team's own zero-cost correction to a Phase-1 proposal error (raw g
   comparison instead of a nonexistent floor-corrected cpl=40 number) held
   up under the real run: the desk-computed GROWING disposition needed no
   revision once real FDTD data existed alongside it (Block T15_RECONCILE
   is desk-only and was already final at Phase 3).

## Phase 5 — Review (seven fresh seats: six blind, Red Team last) — abridged

Full verbatim text: LOGBOOK.md Iteration 12.

**All six blind seats independently returned PARTIAL** (a program first for
unanimity-without-Red-Team-needing-to-decide-a-split, matching Iteration
11's own unanimous pattern). **PHOTONICS** and **ELECTROMAGNETISM**
independently proposed the SAME physical mechanism for the T16_CLOSE
interaction (near-field Fresnel-fringe sampling coupling domain placement
and angle offset) — PHOTONICS additionally computed Fresnel numbers and
found the two blocks are NOT geometrically self-similar (PLANE_DX/R_OUT
differs ~2×), so the fringe hypothesis stays plausible, not proven.
**Three seats** (PHOTONICS, EM, QUANTUM OPTICS) independently flagged that
the interaction clears its own ≥2×10⁻⁴ threshold by only ~5%. **VISION
SCIENCE** made the cycle's sharpest epistemic catch: bit-identical N9
reproduction does NOT prove N17_NATIVE_V2's domain is confound-free at
N17, because T16_CLOSE's own result (domain × quadrature interact) proves
a domain's effect on C is itself angle-dependent — no second,
independently-built r=78-native N17 domain exists to cross-check against.
**THERMODYNAMICS** independently derived that the π/4-vs-`chord_model_g0`
gap is fully explained as a definitional mismatch (θ=0-only vs
N9-oblique-averaged) and found a real, previously-uncaught numeric bug in
`OFF_STATE_DETECTABILITY_NOTE` (stated "5.9–49.8×", true range
5.0×–132.4×, carried unfixed through two prior experiments). **MATERIALS**
argued the PASS-downgrade sharpens, not weakens, the realizability memo's
verdict (D_req should be read as a lower bound, not an achieved figure).
**QUANTUM OPTICS** argued σ(I)'s empirical privilege (its one supporting
PASS) is now gone, though the mechanism class itself remains
theoretically permitted and untouched.

**Red Team (audit, verdict: PARTIAL, affirms all six blind seats,
does not overrule).** Independently re-verified every load-bearing number
across all six reviews, including THERMODYNAMICS' bug (confirmed exactly:
true range 5.0×–132.4× steady / 5.94×–156.3× transient). Corrected the
"noise" framing three seats used for the ~5% margin concern: this engine
is deterministic (this cycle's own bit-identical reproductions prove it)
— the real, legitimate risk is discretization/domain-construction
sensitivity, which this exact channel has repeatedly shown at magnitudes
(3.55×10⁻⁴, 4.25×10⁻⁴) comparable to the margin in question. Sided with
PHOTONICS over EM on the fringe mechanism's confidence level (plausible,
not yet an accepted explanation, given the non-self-similarity confound).
**Checkpoint ruling, explicit**: criteria 1/3/4/5 do not fire. **Criterion
2 does NOT fire** — this cycle shows one calibration point (τ_off=0.0065)
fails a correctly-instrumented measurement at both geometries checked,
NOT that σ(I) as a mechanism class is jointly unsatisfiable; that proof
still requires MATERIALS' own still-deferred rigorous literature check.
**Program-health observation (not a criterion firing)**: Iterations 7–12
— six consecutive cycles — have all closed PARTIAL, all instrument-hygiene
or reconciliation work, not mechanism-testing work; worth weighing in
Iteration 13's sequencing. **Mandatory corrections before close**: fix
THERMODYNAMICS' detectability-note bug in live code (not the historical
NOTES.md/results.json prose), computed not hand-typed — done, this shift,
`experiments/034-floor-convergence-scale-bridge/design_geometry.py`.
Recaption REALIZABILITY_MEMO.md's D_req as a lower bound — done, this
shift. Document the unsigned-delta convention — done, this section.
**Ranked Iteration-13 priorities**: (1) the rigorous RSA/TPA/third-class
literature check (zero cost, could fire or definitively not-fire
Checkpoint-2, three-iteration overdue); (2) N33 at r=78-native (the
geometry the headline citation actually originates from); (3) persist
per-angle scene data and retroactively check ±10/20/30° at r=78-native,
folded into the N33 run; (4) [already done this shift] fix the
detectability note, formally close the π/4 sub-thread.

**Documentation note (MATERIALS' catch, confirmed by Red Team):**
`delta_N9_vs_N17_same_domain` in `results.json` (both blocks) is stored as
an **unsigned magnitude** (`abs(C_N17 - C_N9)`), even though the two
blocks move in OPPOSITE directions (r=156: toward zero; r=78-native: away
from zero). Not a bug — correctly computed as specified — but a footgun
for any future programmatic query that assumes sign is preserved. Flagged
here for any future cycle reading this file's numbers directly.

## Director's close

**VERDICT: PARTIAL** — Red Team affirms all six blind seats unanimously;
no override. Every pre-committed prediction was either confirmed or
cleanly refuted with real numbers (P-T16-1's additive central estimate
refuted — REAL INTERACTION instead, the falsifiable band's own
pre-registered alternate outcome; P-N17V2-2's directional sub-prediction
refuted, its band and margin-exceeded central prediction both confirmed;
everything else confirmed). Budget discipline held (68 calls, unchanged
from the Phase-1 proposal through close). A real historical bug
(THERMODYNAMICS' detectability-note catch) was found and corrected in
live code this same shift, not deferred or smoothed over.

**Checkpoint criterion 2 does NOT fire** — Red Team's explicit ruling,
adopted without qualification: this cycle shows one calibration point
fails correctly-instrumented measurement at both geometries checked, not
that σ(I) as a mechanism class is jointly unsatisfiable. No other
criterion fires.

**The honest headline**: this program's only-ever constraint-3 σ(I)
OFF-state PASS no longer survives at either geometry it has ever been
measured at, once angular quadrature is corrected on a
domain-confound-free basis — for the first time shown cleanly at
r=78-native, the geometry the citation actually originates from. This
does not rule out σ(I) as a mechanism class (a smaller τ_off could still
clear the bar, at the cost of an even larger, not yet bounded, D_req), and
it does not by itself sharpen MATERIALS' realizability verdict beyond a
documentation-level reframing — but it does mean the program's own
"leading candidate" status for σ(I) now rests on zero surviving bench
evidence, not one. Two, not one, independently-proposed physical
mechanisms (PHOTONICS, EM — near-field fringe sampling) exist for WHY the
domain and quadrature confounds interact, but neither is yet
distinguished from a standoff-ratio confound PHOTONICS itself found in
the two blocks' geometry. Six consecutive iterations (7–12) have now been
instrument-hygiene or reconciliation work — a real, disclosed pattern,
not a violation of any rule, but a signal Iteration 13 should weigh
(Red Team's own program-health observation).

Corrections applied this shift, disclosed not smoothed over: THERMO's
detectability-note bug fixed in live code
(`experiments/034-floor-convergence-scale-bridge/design_geometry.py`,
computed not hand-typed, erratum comment added); REALIZABILITY_MEMO.md's
D_req figure recaptioned as a lower bound; the unsigned-delta convention
documented. `75f3626` (results) committed prior shift; `f604f2d`
(LOGBOOK Phases 1–4) committed this shift; mandatory corrections and this
close committed same-shift. Next lead per rotation: **VISION SCIENCE**
(Iteration 13) — cycling back to the seat that opened this program's
first iteration.

Open questions carried forward: the rigorous RSA/TPA/third-mechanism-class
literature check (Iteration-13 top priority, three-cycle-plus deferral);
N33 at r=78-native (Iteration-13 #2); per-angle ±10/20/30° checks at
r=78-native, folded into N33 (Iteration-13 #3); the fringe-sampling
mechanism for T16's interaction (plausible, not proven — the
non-self-similarity confound between T16_CLOSE and N17_NATIVE_V2 needs
resolving before it's trusted); a genuine 3-λ sweep of the N9→N17
angular-convergence readings (never done on this channel); T11's box-
ledger trust stage; T14's cored-absorber r-sweep; T12's PEC r-family
ripple test; QUANTUM's incoherent-ensemble idiom (re-scoped as
contingent-only, not queued-by-default, per QUANTUM OPTICS' own Phase-5
argument, unopposed); EM's reciprocity check.

## Next

See PLAN.md's Next-work queue (updated this shift) for the authoritative,
ranked Iteration-13 priority list.
