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

*Predictions above committed to git before Phase 4's first new FDTD call,
per house discipline. Phase 4 (Results) and Phase 5 (Review) appended
below after the run.*
