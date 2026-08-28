# PHASE 2 — RED TEAM AUDIT · Panel Iteration 62 · exp-085

*Fresh context. Received: `phase1_proposal.md` + all five blind Phase-2
critiques (EM, PHOTONICS, QUANTUM, THERMODYNAMICS, VISION). Every claim
below — the proposal's own, and each critique's own — is independently
re-derived from primitives (source code, `derivation_results.json`,
LOGBOOK.md's primary R10 text, `phase5_redteam_audit.md`'s R10 text), not
accepted on citation.*

## 0. Scope note

This is a model-internal, zero-FDTD desk cycle (`edge_diffraction_c_empty_
corrected` re-evaluated over a wider/denser domain by already-committed
period-search machinery). No mechanism/absorption claim is made anywhere in
the proposal, and no constraint-3 scene is touched. **All
`constraint-#N-violation` tags are N/A this cycle** — verified independently
against §3 and against the actual computed quantities (§2's parameter
table): nothing here scores against any of the four phenomenon constraints,
and Checkpoint criterion 2 is correctly ruled N/A, matching the standing
framing established at Iterations 59–61 (`LOGBOOK.md` lines ~3458, ~3804,
confirmed by direct read). Every attack below is therefore tagged
`inconsistency` or `unfalsifiable`.

## 1. Independent primitive-level verification performed

- **`edge_diffraction_c_empty_corrected`'s exact-hypot claim**: confirmed
  directly in `experiments/048-.../design_geometry.py::_geom_derived`/
  `field_and_h` — `r = sqrt(d_sp**2 + dy**2)` (exact), Green's function
  `G0 = exp(i(k·r − π/4))/√r`. No paraxial truncation anywhere. The
  mechanism narrative's central physical premise is real, not asserted.
- **`_src_amp`'s phase convention**: confirmed — `phase = k·sin(θ)·(y_src −
  obj_y)`, a linear phase ramp applied across *source* points, swept while
  the observation reduction (`amb.window_means`) sits at one fixed
  near-field plane. This is a steering-angle sweep, not an
  observation-angle sweep — material to EM's disclosure point below.
- **Fraunhofer fraction 0.197%**: recomputed independently —
  `D_SP=223` (`experiments/065-.../design_geometry.py` line 131,
  `BASE_SRC_X - BASE_PLANE_X`), full aperture `A_full=2×752=1504` (line
  455, `"A": 752`), `λ=20`. `223/(1504²/20) = 223/113,100.8 = 0.19717%`.
  Matches. (Confirms THERMO's flag below: the table's own "A" — 752 — is
  the *half*-aperture; using it directly gives a wrong, 4×-different
  0.789%. No error propagates into exp-085 itself since it only cites the
  already-correct figure, but the collision is real.)
- **`center_deg=39.0` hardcode**: confirmed directly in
  `experiments/078-.../y_wall_prescreen.py::free_period_with_widening`
  line 346 — `_free_period_search(thetas, delta, center_deg=39.0, ...)`,
  unconditionally, for every call including every one of Method C's 37
  sub-window fits. Traced into `experiments/069-.../run.py::
  _free_period_search`: `cos_c = cos(radians(center_deg))`; `Tc =
  radians(p_star)·cos_c` is the period actually tested in `sin(θ)`-space.
  Algebra: for a truly θ-invariant local period `P0`, the code reports
  `P_local(θc) = P0·cos(θc)/cos(39°)`. Computed directly:
  `cos(5°)/cos(39°)=1.282`, `cos(77°)/cos(39°)=0.2895` — reproduces EM's
  cited `1.28`/`0.29` to 3 significant figures. **EM's attack is
  CONFIRMED, exactly, from the primitive source — not merely plausible.**
  Method A and Method B are each a *single* global number under the same
  fixed `center_deg=39.0` convention that `P_model_a`/`P_edge_A` already
  use — that usage is internally consistent with existing citations and is
  **not** broken by this bug. Only Method C's *cross-sub-window*
  comparison (`spread`, `ρ`, `frac_recovered`) is corrupted, because it
  compares locally-fit periods that should each be referenced to their own
  `θc` but are all forced through the same fixed reference angle.
- **`derivation_results.json::leg_a`**: re-read directly —
  `p_model_deg=2.533834586466165`, `r_squared=0.36965580905914364`,
  `p_edge_a=2.8421052631578947`. Matches every citation in the proposal and
  all five critiques to the printed digit.
- **Method B's period-conversion formula**: `degrees((1/f_peak)/
  cos(radians(39.0)))` is confirmed the exact algebraic inverse of
  `Tc=radians(p_star)·cos_c` — traced through the same code path as above.
  Correct, and (unlike Method C) not exposed to the reference-angle bug,
  since it is a single global conversion under the same fixed 39° the rest
  of the sub-thread already uses.
- **§4(b)'s outcome-band overlap/gap**, recomputed from scratch (not
  accepted from QUANTUM's write-up):
  - Overlap: `P_wide=2.60°, P_fft=3.10°` → `rel_dev(P_wide,P_edge_A)=
    0.08519≤0.10`, `rel_dev(P_fft,P_edge_A)=0.09074≤0.10` → band 1 fires;
    `rel_dev(P_wide,P_fft)` vs. mean `=0.50/2.85=0.17544>0.10` → band 4
    fires simultaneously. **Confirmed, exactly.**
  - Gap: `P_wide=2.55°, P_fft=2.70°` → band 2 fails (`rel_dev(P_fft,
    P_model_a)=0.06558>0.05`); band 1 fails (`rel_dev(P_wide,P_edge_A)=
    0.10278>0.10`); band 3 fails on its own first clause
    (`rel_dev(P_wide,P_model_a)=0.00638`, not `>0.05`); band 4 fails
    (`rel_dev(P_wide,P_fft)` vs. mean `=0.05714≤0.10`). **All four bands
    fail on an arithmetically ordinary pair of values. Confirmed,
    exactly.**
- **§4(a)'s Method C classification gap** (VISION's finding), checked as a
  truth table, not prose: `frac≥0.80 AND spread>0.50 AND |ρ|≥0.5` clears
  none of STABLE (`spread≤0.15` fails), DRIFTING (`spread≤0.50` fails), or
  NOT-STABLY-PERIODIC (`frac<0.80` false, and `spread>0.50 AND |ρ|<0.5`
  fails since `|ρ|≥0.5`). **Confirmed: a real, reachable, unclassified
  cell** — and it is precisely the "large coherent chirp" outcome §1's own
  narrative names as the mechanism's most distinctive possible finding.
- **R10's primary text**, read directly from two independent sources —
  `LOGBOOK.md` lines 275–331 (RULED OUT registry) and
  `experiments/084-.../phase5_redteam_audit.md` lines 399–457 (its
  source) — confirmed bit-identical between the two. The operative clauses:
  *"any future free-period-fit or free-phase-fit SUPPORT/CONFIRM verdict
  must clear a circular-shift-on-the-real-data null test — the mandatory
  default, always run and reported even when another surrogate is also
  tried — before it is reported as evidence"*; and, for a deterministic
  curve specifically, *"state explicitly that the circular-shift result
  answers a self-similarity/specificity question... not a literal
  measurement-noise question — both are legitimate uses of the same
  test"*; and *"a cycle that... omits the mandatory circular-shift
  baseline entirely, fires Checkpoint criterion 4 automatically."*
  **Nowhere does R10's text exempt a deterministic curve from running the
  test — it only re-labels what the result means.** The proposal's §4
  sentence — *"No circular-shift null is run on the wide curve — per
  R10's own explicit carve-out"* — is a direct misreading. This is doubly
  pointed because R10 was adopted, one cycle ago, using exactly this
  curve family (`edge_diffraction_c_empty_corrected`, the narrow window)
  as its worked example: the circular-shift null on that same function is
  what reversed the narrow window's own SUPPORT to INCONCLUSIVE
  (`R²=0.3697` met/exceeded by `15/30=50.0%` of the curve's own shifts —
  confirmed against `LOGBOOK.md` lines 284–288). Citing the rule that
  reversed the narrow-window verdict as license to skip the identical test
  on the same function's wide-window verdict is self-undermining on its
  face.

## 2. Numbered attacks

1. **[inconsistency]** §4's R10 citation misreads R10's own finalized
   text. Verified directly against both primary-source locations (§1
   above) — the deterministic-curve clause changes *interpretation*, never
   *whether the test runs*. The sentence must be struck or corrected.

2. **[unfalsifiable]** As designed, §4(b)'s STABLE and period-match
   verdicts (bands 1–3) are not falsifiable against the null R10 exists to
   rule out — "this curve's own smoothness alone explains an apparently
   good fit" — because the mandatory circular-shift/self-similarity null
   is never run on `c_wide(θ)`. Given the immediately-prior cycle
   demonstrated this exact function's narrow-window R²=0.3697 sits at the
   *median* of its own null distribution (not a rejection tail), a
   wide-window `R²_wide≥0.55` claim has, as specified, no way to be
   distinguished from the same smoothness artifact at a larger scale.

3. **[inconsistency]** Method C's `center_deg=39.0` hardcode mislabels
   every sub-window's locally-fit period by `cos(θc)/cos(39°)` — a
   monotonically decreasing factor from `1.28×` at `θc=5°` to `0.29×` at
   `θc=77°` for a genuinely non-chirping signal. This factor alone can
   mechanically clear DRIFTING's `spread>0.15`/`|ρ|≥0.5` bar (a strong,
   perfectly rank-monotone artifact) regardless of the model's true local
   period behavior. Confirmed from the primitive source, not merely
   plausible from the parameter table.

4. **[inconsistency]** §4(b)'s four outcome bands are neither mutually
   exclusive (an explicit overlap example fires bands 1 and 4
   simultaneously, opposite prescriptions, no priority stated) nor
   exhaustive (an explicit, arithmetically ordinary example fires none of
   the four). Both reproduced independently in §1 above, not merely
   asserted from QUANTUM's write-up.

5. **[inconsistency]** §4(a)'s three-way STABLE/DRIFTING/NOT-STABLY-
   PERIODIC classification for Method C's `frac_recovered`/`spread`/`ρ`
   omits the reachable cell `frac≥0.80 AND spread>0.50 AND |ρ|≥0.5` —
   independently confirmed as a truth-table gap in §1. This is not a
   marginal edge case: it is the specific outcome §1's own mechanism
   narrative calls out by name ("the finding IS the drift, not a number"),
   and as written it would have to be adjudicated post hoc, off the
   pre-registered table, at exactly the moment the proposal's central
   claim is most tested.

6. **[inconsistency]** Method B's zero-padded FFT is computed over a
   rectangular-truncated `sin(θ)` domain with no taper. A rectangular
   window convolves the true spectrum with a Dirichlet-kernel sinc,
   producing sidelobe leakage and peak broadening independent of any real
   underlying chirp — the identical spectral signature §4(a) reads as
   Method B's own chirp corroboration (`FWHM/f_peak`). This confound is
   undisclosed anywhere in the parameter table or idealizations, for an
   instrument billed as "genuinely independent" of Method A specifically
   because it is unbounded and multi-peak-capable.

7. **[inconsistency]** §4(a)'s STABLE criterion states `frac_recovered ≥
   0.80 AND spread ≤ 0.15, corroborated by Method B (...)` without stating
   whether "corroborated by" is a strict AND-gate or a soft signal. The
   later disagreement clause ("both are reported side by side... flagged
   for reconciliation, not silently resolved") implies the latter, but
   this is never stated as an explicit decision rule. Left unresolved,
   Methods A/B's own inability to score well on a genuinely chirped signal
   (attack 6's underlying point, echoing PHOTONICS below) has no
   guaranteed non-veto over a clean Method C finding.

8. **[inconsistency]** *(non-blocking, disclose-only)* EM's near-field
   steering-vs-observation-angle point is independently confirmed from
   `_src_amp`'s own phase convention (§1 above): `sin(θ)` is exact for a
   transverse angular-spectrum decomposition at a fixed observation plane
   only in the far field, and θ here is a *source-steering* angle at
   fixed near-field range, not an observation angle. The proposal asserts
   `sin(θ)`-uniform sampling is the right choice because it is the
   established convention, never derives that the convention survives
   this near-field steering/observing distinction. Does not invalidate
   the proposal (no better a priori variable is offered by any critique
   either), but should be stated, not assumed.

9. **[inconsistency]** *(non-blocking, disclose-only)* The mnemonic "A" is
   overloaded: the parameter table's own citations use `A=752` (half-
   aperture) while the correctly-computed 0.197% Fraunhofer fraction
   requires the full aperture, `2A=1504`. No error propagates in this
   cycle (verified in §1: exp-085 only cites the already-correct 0.197%
   figure, never re-derives it from the table's own "A"), but the
   collision is a latent trap for the next cycle that tries to recompute
   this quantity from the parameter table alone (THERMO's flag,
   independently confirmed).

10. **[inconsistency]** *(non-blocking, disclose-only)* Idealization 4
    justifies part of the `θ>80°` exclusion with an unsourced claim about
    where "a physically swept flashlight beam would not plausibly operate"
    — a witness-scene assertion smuggled into an otherwise scene-free desk
    idealization, uncredited to any source (VISION's flag, confirmed:
    this proposal touches no constraint-3 scene anywhere else). It only
    narrows the domain (conservative in effect) and is not scored against
    anything, so it does not block the cycle — but it should either cite a
    source or be dropped; the vector/polarization-validity argument
    already fully justifies the same exclusion on its own.

## 3. Adjudication of the five critiques' own claims

**R10 misapplication (EM, PHOTONICS, QUANTUM, THERMODYNAMICS, VISION —
all five, not four of five as the assignment's own headcount states; see
below).** **CONFIRM**, independently, from R10's own primary text at both
its LOGBOOK and source locations (§1 above). Worth flagging precisely: the
task brief describes this as "four of five (VISION, THERMO, QUANTUM, EM)."
Independent read of all five files shows PHOTONICS's own "Flip" section
makes the identical claim, quoting the identical R10 language and drawing
the identical conclusion ("Running a circular-shift on Method A's
wide/dense fit... would flip my verdict to support outright"). This is a
minor point but the assignment's own framing under-counts by one — the
correct tally is five of five, unanimous, and I verified this myself
rather than trusting either count.

**EM's `center_deg=39.0` bug.** **CONFIRM**, exactly, reproduced from the
primitive source with matching numeric factors (§1 above). Not fatal to
Method C as specified — it is a one-line fix (`center_deg=θc` per
sub-window call, or an explicit `cos(θc)/cos(39°)` correction applied to
`P_local` before `spread`/`ρ` are scored) that leaves the rest of Method
C's design, and all of Methods A/B, untouched.

**EM's near-field steering/observing distinction.** **CONFIRM** as a real,
non-fatal disclosure gap (§1, attack 8 above).

**QUANTUM's two numeric counterexamples for §4(b)'s MECE gap.**
**CONFIRM**, both, recomputed independently from scratch in §1 above — the
overlap and gap cases both reproduce QUANTUM's claimed values to within
rounding.

**PHOTONICS's claim that Methods A/B can't distinguish "no periodicity"
from "genuine broadband chirp," leaving only Method C as a real probe of
the chirp hypothesis.** **CONFIRM as a real, fair, fixable framing gap —
not fatal.** Both Method A (single global LSQ period) and Method B
(unwindowed global FFT) are stationarity-assuming instruments; a
genuinely chirped signal degrades performance on both regardless of
whether real near-field structure exists, so a weak A/B result is
uninformative between the two readings. This does not sink the proposal:
Method C's `ρ`/`spread` trend test is a genuinely different, local
instrument that does probe the chirp hypothesis directly, and is not
itself compromised by this framing gap (once attack 3's `center_deg` bug
is fixed). The fix is procedural, not structural: state explicitly, before
Phase 4 runs, that Method C's local trend is primary for question (a) and
Methods A/B corroborate but do not veto it (closes attack 7 above too).
PHOTONICS's own FFT-leakage/windowing point is independently confirmed as
real (attack 6).

**THERMODYNAMICS's arithmetic re-verification (grid counts, Fraunhofer
fraction, evaluation-count rounding, Method B conversion formula).**
**CONFIRM**, every figure, independently recomputed in §1 above from the
same primitives THERMO cites, not merely re-executed from THERMO's own
code. The one non-load-bearing rounding slip (`37,816` true vs. `"≈37,800"`
stated, a 0.04% difference) is real but immaterial.

**VISION's traced R10 quotation and the §4(a) MECE gap.** **CONFIRM**,
both, independently — the R10 quotation matches the primary source
verbatim (checked directly, not merely trusted as "traced"), and the
missing classification cell is a genuine truth-table gap (§1 above),
correctly identified as the single most physically distinctive outcome
the mechanism narrative names.

## 4. Ruling: **PROCEED-WITH-MANDATORY-FIXES**

None of the defects found — by any critique or independently by this audit
— are structural. Every one is a cheap, fully expressible correction (a
missing null run, a one-line parameter fix, an added decision-table clause,
a taper, a sentence of scope discipline) to an otherwise sound,
well-motivated, correctly-scoped desk cycle. `constraint-#N-violation` is
N/A throughout (§0). Nothing here is overridden — every mandatory item
below was independently reproduced from primitives, not merely counted from
the critiques.

**Mandatory fixes — precisely, for the Director to specify into the
committed proposal / Phase-3 build before Phase 4 runs:**

1. **Strike §4's R10 sentence** ("No circular-shift null is run on the
   wide curve — per R10's own explicit carve-out..."). Add a mandatory
   order-preserving circular-shift null, run on Method A's wide/dense
   `c_wide(θ)` array using the same staged-widening `free_period_with_
   widening` machinery exp-084 used, as a required co-gate before any
   STABLE, DRIFTING, or §4(b) period-match band (1–3) is reported as
   evidence. Interpret the result per R10's own deterministic-curve clause
   — a self-similarity/specificity reading, not a noise-significance one
   — and state that explicitly in the writeup (this reinterpretation is
   fine; only the omission was wrong).

2. **Extend the same null discipline to Method C's `frac_recovered`
   gate.** Because `frac_recovered≥0.80` depends on 37 independent local
   R²≥0.30 clearances, and the narrow-window precedent showed this exact
   R²≥0.30 bar is cleared by ~50% of a smooth curve's own circular shifts,
   run the circular-shift null on at least a representative sample of
   Method C's sub-window fits (or provide an explicit, quantitative
   argument for why the sub-window scale is not exposed to the same
   self-similarity risk) before `frac_recovered`/`spread`/`ρ` are trusted.

3. **Fix Method C's reference-angle bug.** Call `_free_period_search`/
   `free_period_with_widening` with `center_deg=θc` (the sub-window's own
   center) for each of the 37 sub-windows, not the hardcoded `39.0` — or
   apply an explicit, documented `P_local_corrected(θc) =
   P_local_reported(θc)·cos(39°)/cos(θc)` correction before `spread` and
   `ρ` are computed. Methods A and B's own single global `center_deg=39°`
   convention is unaffected and needs no change.

4. **Add an explicit precedence rule to §4(b)'s four outcome bands** (e.g.,
   evaluate band 4 — method disagreement — first; a lower-numbered band is
   entered only if no higher-priority band's conditions are also met), and
   close the demonstrated gap (redefine band 3 to also check `P_fft`, or
   add an explicit fifth catch-all band) so every reachable `(P_wide,
   P_fft, R²_wide)` triple lands in exactly one bucket. Pre-register before
   Phase 4, not adjudicated after seeing the numbers.

5. **Extend §4(a)'s three-way Method C classification** to explicitly
   cover `frac_recovered≥0.80 AND spread>0.50 AND |ρ|≥0.5` — fold it into
   DRIFTING as a named strong-chirp sub-case, or add a fourth named band —
   before any code runs.

6. **Apply a Hann or Tukey taper** to the `sin(θ)`-uniform samples before
   Method B's FFT, and disclose the choice; state explicitly that an
   unwindowed rectangular-truncated FFT can itself present sidelobe
   leakage as a "smeared/broadened peak," so Method B's `P2/P1`/`FWHM`
   readings must be interpreted with this taper applied, not on the raw
   rectangular transform.

7. **State explicitly, before Phase 4, the decision-priority between
   Methods A/B and Method C.** Method C's local trend (`ρ`, `spread`) is
   primary for question (a) — whether the model curve is genuinely
   (quasi-)periodic; Methods A/B corroborate but do not veto a Method C
   finding when they disagree (matching the existing "flagged for
   reconciliation, not silently resolved" language, which should be made
   into an explicit rule rather than left implicit).

**Recommended, non-blocking (disclose, do not need to gate Phase 4):**
state the near-field steering-vs-observation-angle caveat for `sin(θ)`
(attack 8); disambiguate the "A" half-aperture/full-aperture mnemonic
collision in the parameter table (attack 9); either source or drop
Idealization 4's flashlight-beam clause (attack 10).

## Summary (≤250 words)

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** Every defect below was
independently re-derived from primitives — code, `derivation_results.json`,
and R10's own primary text at both its storage locations — not accepted
from any critique's paraphrase. All five critiques' R10-misreading claim is
CONFIRMED (the assignment briefed this as four of five; independent read
shows PHOTONICS makes the identical claim too — five of five, unanimous).
EM's `center_deg=39.0` hardcode bug is CONFIRMED exactly, algebra
reproduced from source: it mislabels Method C's 37 sub-window periods by
`cos(θc)/cos(39°)`, corrupting only the chirp-drift diagnostic, not
Methods A/B. QUANTUM's and VISION's outcome-band MECE gaps (§4(b) and
§4(a) respectively — two distinct gaps) are both CONFIRMED by direct
recomputation. PHOTONICS's Methods-A/B-can't-probe-chirp point is
CONFIRMED as real but fixable by a procedural precedence rule, not fatal.
This audit also independently found an undisclosed FFT-leakage confound in
Method B and an implicit, unstated A/B-vs-C precedence gap. Seven mandatory
fixes, all cheap and fully expressible in code/spec, zero new FDTD: (1)
strike the R10 sentence and run the circular-shift null on the wide curve;
(2) extend that null to a Method C sub-window sample; (3) fix the
`center_deg` reference bug; (4) add an explicit band-priority rule to
§4(b); (5) add the missing strong-chirp cell to §4(a); (6) taper Method
B's FFT; (7) state Method C as primary, A/B as corroborating-only. No
constraint-#N tags apply — model-internal desk cycle.
