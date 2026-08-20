# exp-051 — The Alias-Lattice Difficulty Predictor, Tested Out-of-Sample

*Panel Iteration 28. Lead: ELECTROMAGNETISM (rotation), executing Red Team's
Iteration-27 Phase-5 ranked #1 item. Instrument/model-fidelity cycle,
Iteration-20/22/23/26/27 class. **T1 escape route: NONE.** No constraint-3/4
verdict is issued or implied at either tier.*

**The design below is the Phase-3-corrected design, not the Phase-1
proposal.** The Phase-1 crux quantity (θ₀'s phase offset from the fringe's
own zero-crossing) was refuted at the desk by four independent blind seats
before Phase 4; the corrected crux quantity is QUANTUM OPTICS' alias-lattice
term, adopted on Red Team's ruling. `phase1_proposal.md` stands unedited as
the historical record per this program's "flag, don't rewrite" convention.
Full reasoning: `phase3_synthesis.md`.

## Hypothesis

exp-050 (Iteration 27) found that both `beam_divergence_incoherent` and
`beam_divergence_incoherent_corrected` execute a genuine, fast-settling
destructive-interference null of the same FWHM=20° angular integral at
several GEOM78 coordinates, and that **which convention's n=41→81 refinement
step crosses the fixed `ABS_TOL=5×10⁻⁴` gate is a reproducible ~1.9–2.3×
magnitude coincidence, unexplained.**

**Hypothesis (QUANTUM OPTICS, Phase 2; independently re-derived by Red
Team):** the n=41 quadrature residual is the **Poisson-alias term of the
underlying single-angle T21 fringe, referenced to the quadrature node
lattice** of spacing

    h = 2 · half_width_factor · FWHM / (n − 1)

(= 2.5° at n=41, FWHM=20°, `half_width_factor=2.5`, read from the committed
`gaussian_angle_weights`), **not** to the fringe's own period
`P(θ)=λ/(A·cosθ)`. At FWHM=20° the node spacing gives 0.59–1.03
samples/fringe-period — 1.9–3.4× below Nyquist at every in-scope
combination — so the fringe aliases, and the residual's size is set by the
fringe's angular spectral amplitude at the alias frequency `1/h`.

Two consequences, both testable:
1. **Tier instability is predictable** from `|E_pred|` against the
   pre-existing, unfitted `ABS_TOL` line — no fitted parameter.
2. **The ~1.9–2.3× convention asymmetry is the ratio of the two
   conventions' spectral amplitude at that one alias frequency** — a
   geometric fact about the two propagator conventions, not a coincidence.

## Setup

**Zero new FDTD calls. Pure numpy.** New module
`experiments/051-.../design_geometry.py`, reusing already-committed,
already-gated code: `_geom_derived`, `_G_for_g`, `_src_amp`,
`beam_divergence_{incoherent,incoherent_corrected,coherent}` (exp-050),
`gaussian_angle_weights`, `aperture_profile` (exp-042), `amb.window_means`,
`amb.weber` (`lab/ambient.py`). No `lab/` file is modified; no new trust-suite
stage is warranted (desk work on already-gated machinery — Iteration-26/27
precedent). Bench re-verified 41/41 immediately before the run.

**Reused verbatim from exp-049/050, unchanged:** `N_SERIES` =
(41,81,161,321,641,1281,2561,5121); `C_THR`=0.005; `ABS_TOL`=5×10⁻⁴;
`REL_TOL`=1.0%; the exemption convergence criterion; `nstar`/tier
definitions; `GEOM78` (A=724) and `GEOM_EXP042_OLD` (A=752). **No tuning
parameter is introduced or changed anywhere in this cycle.**

**The crux quantity (corrected, Phase 3).** For a combination
(θ₀, FWHM, λ, geometry g, convention):

    h            = 2 · half_width_factor · FWHM / (n − 1)
    alias_coeff(m) = ∫ w(θ) · c(θ) · exp(−2πi·m·θ/h) dθ  /  ∫ w(θ) dθ
    E_pred       = 2·Re[alias_coeff(1)] + 2·Re[alias_coeff(2)]

where `w(θ)` is the committed Gaussian angular weight and `c(θ)` the
committed single-angle Weber contrast for that convention, evaluated on a
dense grid over the same ±`half_width_factor`·FWHM support the quadrature
itself spans. **Both m=1 and m=2 are required** (m=1 alone is 6–16% off at
450nm — QUANTUM's E5, Red Team-confirmed). The predicted-unstable rule is
the **unfitted** `|E_pred| ≥ ABS_TOL`.

**Mandatory memoization (Red Team docket 2):** `_geom_derived(g)` and the
propagator matrices are hoisted once per `(geometry, λ)`. Not optional —
unmemoized the sweep costs hours (THERMODYNAMICS measured 168–269 ms per
single-angle evaluation vs 3.96/15.43 ms hoisted).

### Scope — and the calibration/out-of-sample split (Phase-3 Director ruling)

Full grid: θ₀∈{36,38,40}° × FWHM∈{2,5,10,20}° × λ∈{450,600,750}nm (36 cells)
× 3 functions × 2 geometries = **216 combinations.**

**CALIBRATION set — 18 combinations, REPORTED, SCORED AGAINST NOTHING:**
GEOM78 × FWHM=20° × {`incoherent`, `incoherent_corrected`} (7 unstable / 11
stable). QUANTUM and Red Team each computed `E_pred` on exactly these 18
during Phase 2, with the answers committed before this synthesis. Scoring a
prediction against them would be transcription, not prediction. Their
numbers are reported, and agreement with the two independent pre-checks is
reported as a three-way cross-validation — informational only.

**OUT-OF-SAMPLE set — 198 combinations, 22 unstable / 176 stable, where
every scored prediction below lives.** No seat and not the Director has
evaluated `E_pred` at any of these:

| Block | Combos | Unstable | Label source |
|---|---|---|---|
| GEOM78, `coherent`, FWHM=20° | 9 | 6 | exp-050 `results.json` |
| GEOM78, all functions, FWHM≤10° | 81 | 0 | exp-050 `results.json` |
| A=752, all functions, all FWHM | 108 | 16 | exp-049 `results.json` |
| **Total** | **198** | **22** | — |

Labels are already-committed public data from two prior experiments; they
cannot be tuned by this cycle. The threshold is unfitted.

**Completeness ledger:** one record per (combination, quantity) —
216 combinations × {`E_pred(m=1)`, `E_pred(m=2)`, `C(41)`, `C(81)`,
`nstar_pred`} = **1080 expected records**, asserted executably in code.

## Falsifiable predictions — FROZEN before any Phase-4 code is written

"Tier-unstable" = committed `n*≠41`. All bands are out-of-sample (N=198,
22 positives) unless stated.

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-ALIAS-0** | **Regression anchor, checked first.** (a) The geometry-parameterized single-angle functions at `g=GEOM_EXP042_OLD` reproduce exp-042's committed module-global `edge_diffraction_c_empty`/`_corrected` at all **18** spot points (9 cells × 2 conventions). (b) `beam_divergence_*` at n=41 reproduce exp-049's and exp-050's committed `c41` for all 216 rows | ≤10⁻⁹ relative on every value, both (a) and (b) | any mismatch beyond float noise ⇒ **no number in this cycle is trusted** until resolved |
| **P-ALIAS-1** | **Primary, continuous, out-of-sample.** Spearman ρ between `log10(\|E_pred\|)` and `log10(\|C(41)−C(81)\|)` across all 198 out-of-sample combinations | ρ ≥ **0.85** ⇒ CONFIRMED; 0.60–0.85 ⇒ PARTIAL; <0.60 ⇒ REFUTED | ρ < 0.40 |
| **P-ALIAS-2** | **Secondary, binary, out-of-sample, unfitted threshold.** Classifying the 198 by `\|E_pred\| ≥ ABS_TOL` against the committed `n*≠41` labels | accuracy ≥**0.90** AND sensitivity ≥**0.75** (≥17 of 22 positives) ⇒ CONFIRMED; accuracy 0.75–0.90 or sensitivity 0.50–0.75 ⇒ PARTIAL; below both ⇒ REFUTED. Must also beat the convention-identity null baseline (AUC≈0.79) | accuracy <0.70 or sensitivity <0.35 |
| **P-ALIAS-3** | **The sharpest falsifier: false positives on the 81 GEOM78 FWHM≤10° combinations**, every one of which is committed-stable. A predictor that fires in the well-sampled regime (where h≪P and no aliasing should occur) is worthless regardless of its performance elsewhere | ≥**95%** predicted stable (≤4 false positives of 81) | >12 false positives (>15%) |
| **P-ALIAS-4** | **Generalization across geometry.** P-ALIAS-2's accuracy on the A=752 block (108 combos, 16 positives) alone, using the identical unfitted threshold. MATERIALS' Phase-2 finding that 7 of 18 tier labels flip between the two geometries makes this a real transfer test, not a repeat | accuracy ≥**0.85** and sensitivity ≥**0.60** (≥10 of 16) | accuracy <0.70 |
| **P-ALIAS-5** | **The asymmetry explanation, out-of-sample half.** The alias-frequency spectral-amplitude ratio `\|ĝ_corrected(1/h)\|/\|ĝ_incoherent(1/h)\|` at the **9 A=752 FWHM=20° cells** (the GEOM78 half is calibration) tracks the measured `\|Δabs_corrected\|/\|Δabs_incoherent\|` at those same cells | Spearman ρ ≥ **0.70** across the 9 cells, AND median ratio in **[1.4, 2.6]** | ρ < 0.30, or median outside [1.1, 3.5] |
| **P-ALIAS-6** | **m=2 necessity, out-of-sample.** Dropping the m=2 term degrades P-ALIAS-1's ρ, and the degradation is concentrated at 450nm (the shortest λ, where the alias replica sits closest to a second lattice harmonic) | ρ(m=1 only) < ρ(m=1+2) by ≥**0.03**, and the median \|relative change in `E_pred`\| from adding m=2 is larger at 450nm than at 750nm | m=2 changes `E_pred` by <1% median at every λ (⇒ it was never needed; the mandatory-fix docket's item 1 over-specified) |
| **P-ALIAS-7** | **Direct `n*` prediction.** For each of the 198, predict `n*` by evaluating `\|E_pred(h(n))\|` against `ABS_TOL` down the same `N_SERIES` with the same two-consecutive-doublings rule, and compare to the committed `n*` | exact `n*` match on ≥**85%** of the 198 | <60% exact match |

**What would make this cycle a failure, stated plainly.** If P-ALIAS-1 AND
P-ALIAS-2 both land REFUTED, the alias-lattice mechanism — which scored
AUC 1.000 and r=0.999998 in-sample under two independent Phase-2
implementations — does not generalize off the 18 rows it was found on, and
this cycle's honest deliverable is an overfitting lesson plus a
still-unexplained exp-050 residual. If P-ALIAS-3 fails, the mechanism is
worse than useless: it fires where no aliasing can occur. Both are real,
pre-registered ways for this cycle to lose.

**A prediction this cycle deliberately does NOT make.** No prediction is
offered about the calibration 18. Their numbers are already known to two
seats and are reported, not scored — the disclosure is the point.

## Idealizations

1. **Scope: the 216-combination grid exp-049/050 already established**, with
   the 18/198 calibration/out-of-sample split fixed in §Setup before any
   code runs. No cell outside that grid is examined.
2. **`N_SERIES`, `ABS_TOL`, `REL_TOL`, `C_THR` and the exemption criterion
   are unchanged from exp-049/050.** No re-tuning of the convergence
   machinery is in scope.
3. **`ABS_TOL = 0.1·C_THR` makes every in-scope tier label reduce to a
   single continuum cut** (`Δabs > 0.1·C_THR`) — VISION SCIENCE's Phase-2
   finding, since the `|C(2n)|≥C_THR` clause never fires anywhere in scope.
   The label is stable only over `ABS_TOL ∈ [0.08,0.10]·C_THR`. Disclosed,
   and a sensitivity ledger row is committed at 0.05/0.08/0.10/0.13/0.20·
   C_THR — reported, **not** re-tuned. This is why P-ALIAS-1 (continuous) is
   primary and P-ALIAS-2 (binary) secondary.
4. **The alias model is an analytic model of the quadrature's own error, not
   of the physics.** It predicts how badly a finite-n Gaussian quadrature
   resolves an already-committed analytic fringe. It makes no claim about
   whether that fringe is itself physically correct — T21's own
   magnitude-level validation was performed at A=752 only (exp-042) and is
   carried to A=724 by analogy, exactly as exp-049/050 carried it.
5. **`P(θ)=λ/(A·cosθ)` is used only descriptively** (the samples-per-period
   diagnostic), never as the crux quantity — that was the Phase-1 design's
   error. `A = g["OBJ_Y"] − g["ABSORB"]`.
6. **Desk-only.** No FDTD cross-check exists at GEOM78 at any n (exp-046's
   A5 desk-vs-FDTD check was performed at A=752 only); T24's ABSORB-boundary
   systematic (~+0.0070) was measured at A=752 and is carried by analogy.
   Identical status to exp-050's own idealizations 5/6.
7. **The dense-grid integration step for `alias_coeff` is a resolution
   choice**, set to 0.01° and held fixed across all 216 combinations; a
   convergence spot-check at 0.005° is reported for a sample of cells.
8. **Committed labels are taken as ground truth.** exp-049's and exp-050's
   `n*` values are used as-is; this cycle does not re-derive them (P-ALIAS-0b
   verifies only that `c41` reproduces, confirming the same machinery is
   being driven).
9. **No perceptual claim.** `C_THR`/`ABS_TOL` are cited only as the
   pre-existing decision lines already governing `nstar`. No constraint-3/4
   verdict at either tier; nothing here moves `REALIZABILITY_MEMO.md`.
10. **The Phase-2 pre-checks by QUANTUM and Red Team are disclosed in full
    and are the reason the calibration set is unscored** (§Setup, and
    `phase3_synthesis.md` §2). Phase 4's implementation is written
    independently from this frozen NOTES.md, not copied from either seat's
    scratch code; agreement on the calibration 18 is reported as
    cross-validation.

## Cost

**New FDTD calls: 0.** Estimated ≈15–25 minutes single-threaded with the
mandatory memoization applied (Red Team's own from-scratch memoized
implementation covered 18 combinations including `C(161)` calls in ≈8.5
min; this cycle covers 216 combinations but needs only `C(41)`/`C(81)` plus
the alias integrals). Process-start timing is persisted from import, not
from `main()`, so a crash-state cost is recorded (Red Team docket 9 —
verified never adopted despite being recommended at Iteration 27's close).

---

## Results (Phase 4)

Bench re-verified 41/41 (`--only 12346789`) immediately before the run.
Total compute: ≈5.1 min for the scored sweep. `timing.json` records exactly
one completed process (`proc_start_unix`=1787242553.222, single
`exit_unix`); its own internal stage marks show every `P-ALIAS-0` through
`P-ALIAS-7` number, and the calibration-18 cross-validation block, complete
at t=278.976s, with the post-hoc block and the idealization-3 disclosure
(added in the same process) completing the run at t=305.866s (≈306s). An
earlier draft of this section described this as two separate executions
("278s then 306s"); **that was an error** — a misreading of these two
intra-run checkpoints as two runs. No second `proc_start_unix` exists
anywhere on record, and no independent evidence (git history, `__pycache__`
mtimes) supports a distinct second execution. Corrected at the Phase-5 Red
Team audit (THERMODYNAMICS' Phase-5 catch, independently resolved by Red
Team against source); no scored prediction is affected. Plus the bench and
pre-run helper checks, ≈13 minutes total. *(Separately, and after the
Phase-4 commit: a Phase-5 review seat re-executed `run.py` independently in
the course of its own verification, which overwrote the working-tree
artifacts with a fresh `proc_start_unix`; every science number reproduced
bit-identically, and the committed Phase-4 artifact was restored by the
Director. That reproduction is real but is not the "second run" the
erroneous sentence above claimed, which predated it.)* Two implementation bugs
self-caught and fixed **before** any science number was produced (a
duplicate-keyword `TypeError` in the confusion-matrix assembly; an
inefficient but not incorrect scan-cache rebuild) — zero runs were burned on
broken code. Completeness ledger: **1080/1080**, executable assertion
passed. `design_geometry.py`/`run.py` were written independently from this
frozen NOTES.md spec, without opening any Phase-2 seat's scratch code (idealization 10) — the agreement reported below is a genuine cross-validation, not a copy.

**P-ALIAS-0 (gate, checked first): CONFIRMED.** Both clauses bit-exact
(0.0 relative error): (a) 18 spot points of the geometry-parameterized
single-angle functions vs exp-042's committed module-globals; (b) all 216
`beam_divergence_*` n=41 values vs exp-049/050's committed `c41`. A third,
Phase-4-added self-check (batched-matmul `E_pred` path vs the scalar path
the frozen 0a doesn't exercise) also passed, 6.2×10⁻¹² relative — disclosed
as an addition to, not a substitute for, the frozen gate.

| ID | Measured (198 out-of-sample unless noted) | Band | Outcome |
|---|---|---|---|
| P-ALIAS-1 | Spearman ρ = **0.7380** (Pearson on log10 = 0.762) | ≥0.85 CONF / 0.60–0.85 PART | **PARTIAL** |
| P-ALIAS-2 | accuracy **0.9495**, sensitivity **0.5455** (12/22), specificity 1.000, AUC 0.9645 | acc≥0.90 ∧ sens≥0.75 CONF / sens 0.50–0.75 PART | **PARTIAL** |
| P-ALIAS-3 (81 FWHM≤10°) | **0 false positives**, 100% predicted stable | ≤4 FP CONF | **CONFIRMED** |
| P-ALIAS-4 (108, A=752) | accuracy 0.9537, sensitivity **0.6875** (11/16), specificity 1.000, AUC 0.9664 | acc≥0.85 ∧ sens≥0.60 | **CONFIRMED** |
| P-ALIAS-5 (9, A=752 FWHM=20°) | ρ = **0.9333**, median spectral ratio **1.920** (measured Δabs-ratio median 1.921) | ρ≥0.70 ∧ median∈[1.4,2.6] | **CONFIRMED** |
| P-ALIAS-6 | ρ(m=1) 0.7364 vs ρ(m=1+2) 0.7380, degradation 0.0017; 450nm NOT the largest m=2 contribution | drop≥0.03 ∧ 450nm>750nm | **REFUTED** |
| P-ALIAS-7 | **188/198 (94.95%)** exact `n*` match | ≥85% CONF | **CONFIRMED** |

**5 CONFIRMED, 2 PARTIAL, 1 REFUTED. 0 hard-falsified.** No prediction's
hard-falsification clause fired anywhere, including P-ALIAS-6's own escape
(m=2 changes `E_pred` by <1% median at every λ) — it does not escape; m=2 is
genuinely load-bearing (450nm: 0.08–3.4% depending on FWHM; 750nm up to
3.4%; FWHM=2° cells ~25% at every λ), just not concentrated at 450nm as
predicted.

**Calibration 18 — reported, scored against nothing, as designed.** AUC
1.0000, Pearson r = 0.9999985, max relative error 1.4453%, median 0.018% —
perfect separation at the unfitted threshold (min |E_pred| among unstable
5.263×10⁻⁴, max among stable 4.247×10⁻⁴, straddling ABS_TOL cleanly). This
is a **three-way cross-validation of three independently-written
implementations**: vs QUANTUM's Phase-2 figures (AUC 1.000, r=1.00000, ≤1.4%)
ΔAUC=0, Δr=−1.5×10⁻⁶; vs Red Team's Phase-2 figures (AUC 1.0000, r=0.999998,
≤1.445%) ΔAUC=0, Δr=+4.7×10⁻⁷, max relative error 1.4453% vs their 1.445%.
Every digit either seat quoted reproduces.

## Reading

**The mechanism generalizes.** P-ALIAS-3's zero-false-positive result on the
81 well-sampled FWHM≤10° combinations is the sharpest single fact this cycle
produces: a predictor that scored AUC 1.000 on 18 hand-picked rows could
easily have been an artifact that fires everywhere near |C|≈0 — it does not.
It correctly recognizes the regime (samples-per-period 1.17–10.3, comfortably
above Nyquist) where no aliasing should occur, and stays silent there,
**every time**. P-ALIAS-4's clean transfer to the untouched A=752 geometry
(accuracy 0.954, using labels that MATERIALS' own Phase-2 finding showed 7 of
18 flip against A=724) is the second: this is not a same-geometry repeat.

**But P-ALIAS-1/2's PARTIAL verdicts are real, not a rounding-distance miss,
and the reason is now identified, not just measured.** Splitting the 198 by
function: on the **126 non-`coherent`** rows the predictor is essentially
exact (ρ=0.979, accuracy 1.000, 8/8 sensitivity, 0 false positives/negatives)
— every miss lives in the **72 `coherent`** rows (ρ=0.302, sensitivity 4/14).
This is a genuine, mechanistically located finding, not a diffuse residual:
QUANTUM's E1 identity — `beam_divergence_* ≡ Σwᵢc(θᵢ)/Σwᵢ`, the exact
sampling relationship the alias model is built on — holds because
`incoherent`/`incoherent_corrected`'s per-component flank normalization makes
the quadrature a literal weighted sample of the single-angle Weber contrast
`c(θ)`. `beam_divergence_coherent` sums the **complex field** across angle
samples before computing a single Weber contrast on the sum — a materially
different, and for this predictor's purposes non-identical, combination rule
over the same single-angle building block (this is also *why* MATERIALS'
Phase-2 restoration of `coherent` as a "degenerate-x1 control" mattered: same
regressor, different label, and now a located reason the two diverge for
`coherent` specifically, not a mystery). All 10 of the 198 out-of-sample
false negatives, and all 10 of P-ALIAS-7's mismatches, are `coherent` rows —
disclosed in `results.json`'s `post_hoc_observations_unscored` block,
unscored (no frozen prediction singled out `coherent` separately, so nothing
is re-scored), but load-bearing for what Iteration 29+ should do with this
mechanism: **it is confirmed for the incoherent family the ~1.9–2.3×
asymmetry was actually measured on (exp-050's own scope), and open for the
coherent-sum convention specifically**, not open across the board.

**P-ALIAS-5 closes exp-050's second open question cleanly, on its own
scored data.** The alias-frequency spectral-amplitude ratio reproduces the
measured Δabs-ratio at the 9 out-of-sample A=752 FWHM=20° cells (ρ=0.933,
median 1.920 vs 1.921), with every one of the nine ratios sitting
comfortably above 1 (spectral range [1.656, 2.137], measured Δabs range
[1.550, 3.558]) — a real, directionally-consistent, weaker version of the
same mechanism (rising with λ) that does not invert at this geometry. The
one cell where the ratio genuinely inverts below 1 (750nm/38°, spectral
≈0.835, raw Δabs ≈0.775) is a **calibration-set fact at the *other*
geometry** (GEOM78, A=724) — found independently by QUANTUM, VISION, and Red
Team at Phase 2, reported here only in the unscored
`calibration_18_unscored` block, and explicitly **not** part of what the
scored A=752 P-ALIAS-5 test itself demonstrates. *(An earlier draft of this
paragraph misattributed that inversion to the scored block — caught
independently by PHOTONICS and MATERIALS at Phase 5, confirmed against
`results.json` by Red Team, corrected here same-shift.)* The ~1.9–2.3×
convention asymmetry exp-050 left
unexplained is now explained: it is the ratio of the two conventions'
spectral amplitude at the aliasing frequency `1/h`, a geometric property of
how each convention's obliquity term shapes the single-angle fringe, not a
coincidence.

**P-ALIAS-6's refutation is informative, not a defect.** m=2 is not
concentrated at 450nm as the shorter-wavelength-closer-to-a-second-harmonic
argument predicted — it is instead largest at 750nm and at the narrowest
beam widths (FWHM=2°, ~25% contribution at every λ), where `h` is smallest
relative to the window and a single alias term under-resolves the fringe
regardless of λ. The mechanism (aliasing against the node lattice) survives;
the specific λ-dependence hypothesis attached to it at Phase 3 does not.

**One idealization-3 correction, self-caught and disclosed, not
load-bearing:** VISION's Phase-2 finding that `ABS_TOL=0.1·C_THR` makes the
`|C(2n)|≥C_THR` relative-error clause "never fire anywhere in scope" was true
on the 18-row calibration set it was measured on, but **does fire at 75 of
the full 216 rows** (72 `coherent`, whose Weber contrast is order-unity, plus
3 others) once the grid widens to include `coherent` and FWHM≤10°. The
idealization's *conclusion* (every label reduces to one continuum cut) still
holds, because `drel` is automatically satisfied whenever `|C(2n)|` is large
— but its stated premise does not generalize past the rows it was checked
on. Recorded here per house discipline, non-load-bearing to any scored
prediction.

**What this changes going forward:** exp-050's two open questions both
close. (1) Tier instability at any future `beam_divergence_*` citation is
now predictable, zero-FDTD-cost, from `|E_pred|` against the unfitted
`ABS_TOL` line — CONFIRMED for `incoherent`/`incoherent_corrected` at every
FWHM and both geometries tested (P-ALIAS-3/4/7), open specifically for
`beam_divergence_coherent`, whose different angle-combination rule breaks
the sampling identity the predictor is built on. (2) The ~1.9–2.3×
convention asymmetry is explained as a spectral-amplitude ratio at the alias
frequency (P-ALIAS-5), including its one measured inversion. **Unresolved,
concretely scoped for a future cycle:** why `coherent`'s complex-field-sum
convention breaks the E1 sampling identity in a way that specifically
degrades the alias predictor (not merely "coherent is different" — the
mechanism is named, the consequence for this predictor is measured, the
reason the consequence takes this particular form is not yet derived).

**Sharpened, this same-shift Phase-5 audit (QUANTUM OPTICS, independently
re-derived by Red Team against `results.json` and exp-046's own
`NOTES.md`):** the gap is not merely "a different combination rule" — the
two functions operate at categorically different points (`coherent` median
`|C41|`=0.940, `incoherent` median `|C41|`=4.09×10⁻⁴, four orders of
magnitude apart), and at the FWHM=20° cells the n=41 error for `coherent` is
dominated by **discrete-aperture grating-lobe leakage** (a linearized
cross-term correction recovers at most 48% of the actual step, 0.1–1.0% at
every 450nm cell — the regime is non-perturbative, not a small correction on
a converged alias model), the identical mechanism this program already
measured independently at Iteration 22/23 (exp-046 Phase 5, LOGBOOK: "a
three-lobe comb whose grating-lobe replicas… carry 41.7–68.0% of the total
intensity outside ±3 aperture-widths"). This **connects, rather than
reopens**, a five-cycle-old finding to this cycle's residual — the
correctly-scoped Iteration-29+ follow-up is a grating-lobe/array-factor n\*
criterion for `coherent` specifically, not a bigger `m` or a linear
cross-term add-on to the existing alias model (both tested directly, both
insufficient).

ELECTROMAGNETISM's Phase-5 review independently derived the complementary
half of the same picture from `lab/ambient.py`'s own source: the E1
identity is *exact* (verified to 2.8–5.8×10⁻¹³ relative) for the incoherent
family, which is what licenses the aliasing framing as sampling bookkeeping
rather than analogy — and `coherent`'s complex-field sum is that identity's
structural negation (off-diagonal mutual-coherence terms the diagonal alias
model is blind to by construction), deviating by three orders of magnitude
on the same test. Both seats are correct and non-contradictory: EM shows why
the model cannot see the effect at all; QUANTUM shows why the natural
first-order fix would not rescue it.

## Phase 5 (six fresh blind seats, then Red Team audit)

**Six blind reviews: PROMISING, 6-for-6** (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE) — the
second unanimous-PROMISING panel verdict in the program's history. Every
seat independently reproduced the scored numbers from raw data or a full
re-execution; all agree to the displayed digit.

**Red Team's final audit (everything): PROMISING, no Checkpoint criterion
fires** (all five checked explicitly; criterion 4 scrutinized directly
against both disclosure defects and ruled non-firing — neither is an
unfalsifiable claim, no constraint is claimed or dropped, both are
same-shift narrative-only corrections leaving every scored number
untouched). Two real defects, both caught by multiple independent seats and
both fixed above same-shift: the P-ALIAS-5 misattribution (PHOTONICS +
MATERIALS, independently) and the "executed twice" cost error
(THERMODYNAMICS, resolved more decisively by Red Team than the seat itself
framed it). Red Team flagged this as the **twelfth recurrence** of the
program's "a document correcting a prior overclaim ships a residual instance
of the same overclaim" pattern, and recommended — as lightweight practice,
not a binding rule — that any Reading-section sentence naming a specific
numeric anomaly state in the same sentence which committed block, scored or
unscored, and at which geometry, the anomaly's numbers come from. Adopted.

**Two unconditional build triggers now bind future iterations:**
**Iteration 29** builds MATERIALS' fixed-absolute-thickness
`graded_black_shell` variant (granted at Phase 2, re-verified intact three
ways at Phase 5 — 21-iteration deferral). **Iteration 30** builds VISION's
stage-10 temporal instrument — the joint constraint-3/4 staircase-σ(t)
validation run composing exp-038's kinetics, exp-039's timing
classification, and exp-040's amplitude bridge — newly granted this audit on
a 27-iteration span, longer than the bar just applied to
`graded_black_shell`, and with a worse failure mode (silently dropped from
every ranked list for 10 consecutive iterations rather than actively
competing). Both are unconditional: not contingent on the prior cycle's
findings, not subject to further ranked-list competition.

Full record: `phase5_redteam_audit.md`; all six blind reviews at
`phase5_review_*.md`.

---

*Results below this line are written only after the run. Nothing above it is
edited after the freeze commit.*
