# PHASE 1 — PROPOSAL · Panel Iteration 26 · Lead seat: PHOTONICS

## "The `gaussian_angle_weights` n-Convergence Audit" (candidate exp-049)

*Runner: cloud panel shift · rotation: VISION→**PHOTONICS**→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→repeat. Protocol: PANEL.md.
Memory: LOGBOOK.md (RULED OUT R1/R2/R3 checked — nothing here resurrects a
ruled-out idea; this cycle proposes no mechanism at all).*

**Executing a queued item, not a fresh PHOTONICS mechanism proposal**, per
PANEL.md's Iteration-24/25 precedent (VISION led exp-047 on THERMO's own
queued sidecar item; VISION led exp-048 on its own Iteration-24 queue) and
Red Team's own explicit Iteration-25 Phase-5 ranking (LOGBOOK.md, Iteration
25 close; PLAN.md "Current state," panel-Iteration-26 queue entry): **item
(1), non-negotiable — "QUANTUM's `gaussian_angle_weights` n-convergence
audit ... a third consecutive deferral would repeat this program's own named
r=156 anti-pattern; already has a documented effect size (n=41→401 moved
scored `C_empty` by up to 4.47%, Iteration 23)."** First queued Iteration 24
(#3), carried Iteration 25 (#1 of the standing queue, LOGBOOK Iteration 24
close), now Iteration 26's own Red-Team-ranked #1. This is an
instrument/model-fidelity characterization cycle, in the Iteration-20/22/23
precedent, **not** a T1 mechanism proposal.

---

## 1. Mechanism / test narrative (≤300 words)

**This is NOT a T1 mechanism proposal.** No material law, no escape route,
no constraint-3/4 verdict. **T1 escape route: NONE.**

`gaussian_angle_weights(theta0_deg, fwhm_deg, n=41, half_width_factor=2.5)`
(`experiments/042-t21-magnitude-bridge/design_geometry.py:310-318`) is the
angular-quadrature kernel behind every beam-divergence reading this program
has ever cited: `beam_divergence_incoherent` (`:321-334`, VISION's own
Iteration-19 check, exp-042's PRIMARY `Block BEAM` reading — the "0/36 cells
exceed C_THR" contamination-risk headline, LOGBOOK T21 entry), the
erratum-corrected sibling `beam_divergence_incoherent_corrected` (`:279-295`,
`erratum.py`'s own scored reading), and `beam_divergence_coherent`
(`:337-355`, QUANTUM's mandatory coherent cross-check, exp-046 Block A's
own re-scoring target). `n=41` has been the silent default in every one of
these calls since Iteration 19 (`experiments/042-.../run.py:92-93`) — **never
convergence-tested until exp-046's own Phase-5 audit spot-checked ONE jump,
n=41→n=401, at ONE metric (the coherent reading only) and found a 4.473%
move at the worst of the 36 committed cells** (`results.json`
`block_a_aperture_consistent_beam.angular_sampling_convergence`, exp-046).
That spot-check never touched the incoherent readings, never checked whether
n=401 itself is converged, and never established a formal, falsifiable
definition of "converged" — three gaps this audit closes.

**Design: a desk-only, zero-new-FDTD-call, geometric n-doubling sweep** of
all three functions, unmodified, at the exact 36-cell grid (θ₀∈{36,38,40}°,
FWHM∈{2,5,10,20}°, λ∈{450,600,750}nm) exp-042/046 already committed —
varying only `n`. A physical aliasing mechanism, derived below from
LOGBOOK's own T21 fringe model, predicts *where* on that grid n=41 should
fail and *why* — a falsifiable account this proposal tests, not assumes.

*(281 words)*

---

## 2. Parameter tables

Every number below is either copied from a cited repo line or computed from
cited repo constants by a formula stated in full.

### 2.0 Geometry and functions — inherited VERBATIM, not rebuilt

| Constant / function | Value / signature | Source |
|---|---|---|
| `NX`, `NY` | 360, 1584 | `experiments/042-t21-magnitude-bridge/design_geometry.py:119-120` |
| `ABSORB`, `TAPER` | 40, 40 | ibid. `:121-122` |
| `SRC_X`, `PLANE_X` | 300, 77 | ibid. `:123-124` |
| `D_SP = SRC_X - PLANE_X` | 223 | ibid. `:134` |
| `OBJ_Y` | 792 | ibid. `:133` |
| `A = OBJ_Y - Y_LO` | 752 (edge-to-window-center offset) | ibid. `:137` |
| `CPL` (λ→λ_cells) | {450:15, 600:20, 750:25} | ibid. `:129` |
| `C_THR` | 0.005 (VISION's T2 photopic bar) | `experiments/042-.../run.py:41` |
| `GATE_HARD` | 0.001 (exp-024's own committed hard gate — cited for context, not scored here) | `experiments/041-t20-angle-audit/design_geometry.py:175` |
| `gaussian_angle_weights(θ₀,fwhm,n=41,half_width_factor=2.5)` | thetas=linspace(θ₀−2.5·fwhm, θ₀+2.5·fwhm, n); w=Gaussian(σ=fwhm/2.3548), normalized to sum 1 | `experiments/042-.../design_geometry.py:310-318` |
| `beam_divergence_incoherent(θ₀,fwhm,λ,n=41)` | n independent `\|G@amp\|²` profiles, `amb.incoherent_sum`, `amb.weber` | ibid. `:321-334` |
| `beam_divergence_incoherent_corrected(θ₀,fwhm,λ,n=41)` | same, single-obliquity-via-H (erratum convention) | ibid. `:279-295` |
| `beam_divergence_coherent(θ₀,fwhm,λ,n=41)` | n `√w`-scaled complex fields summed BEFORE `\|·\|²` | ibid. `:337-355` |
| The 36-cell grid | θ₀∈{36,38,40}°, FWHM∈{2,5,10,20}°, λ∈{450,600,750}nm | `experiments/042-.../run.py:89-91`; reused verbatim `experiments/046-.../run.py:218-220` |

**Nothing above is modified.** This audit imports `design_geometry` from
`experiments/042-t21-magnitude-bridge/` exactly as exp-046 did
(`experiments/046-.../run.py:101,106,108`) and calls the three functions
with every argument identical to their committed call sites except `n`.

### 2.1 The n-sweep series and its ceiling — Richardson-doubling reasoning

**Series:** N_SERIES = (41, 81, 161, 321, 641, 1281, 2561, 5121) — each term
= 2·(previous) − 1, so every sample set stays symmetric about θ₀ with a
sample landing exactly on θ₀ (matches `linspace`'s own endpoint-inclusive
convention). **41 is the committed baseline (unmodified); 5121 is 125× the
committed default.** A ninth, off-series point, **n=401**, is evaluated at
every cell/function purely as a **regression/reproduction check** against
exp-046's own recorded numbers (§4, P-NCONV26-0) — it does not participate
in the doubling-convergence test itself.

**Why 5121 and not fewer:** derived from LOGBOOK's own T21 fringe-period
model (Iteration 18, exp-041; ELECTROMAGNETISM's zero-free-parameter,
Red-Team-verified mechanism), reused here as the comparison scale for
`gaussian_angle_weights`'s own angular sampling step — both operate on the
*same* aperture (`A=752`, the raised-cosine taper `aperture_profile`,
`design_geometry.py:148-157`), so the same fringe should appear in the
θ-dependent quantity each function integrates over.

> **T21 fringe period:** P(θ) = λ_cells/(A·cosθ) **radians**
> (LOGBOOK.md, T21 entry — "period P(θ)=λ/(A·cosθ), A=752 cells,
> predicted periods 1.4°/1.9°/2.4° at 450/600/750nm"). Evaluated here at
> the 9 committed (λ,θ₀) pairs (formula applied to cited A=752, CPL, in
> degrees = P(θ)·180/π):

| λ (nm) | θ₀=36° | θ₀=38° | θ₀=40° |
|---|---|---|---|
| 450 | 1.4127° | 1.4503° | 1.4919° |
| 600 | 1.8836° | 1.9337° | 1.9893° |
| 750 | 2.3546° | 2.4171° | 2.4866° |

> **`gaussian_angle_weights`'s own sampling step:**
> Δθ_sample(n,fwhm) = 2·half_width_factor·fwhm/(n−1) = **5·fwhm/(n−1)
> degrees** (from `linspace(θ₀−2.5fwhm, θ₀+2.5fwhm, n)`,
> `design_geometry.py:314-315`). At the committed n=41:
> Δθ_sample(41,2°)=0.250°, Δθ_sample(41,5°)=0.625°,
> Δθ_sample(41,10°)=1.250°, Δθ_sample(41,20°)=2.500°.

**Samples-per-period at n=41** (= P(θ)/Δθ_sample(41,fwhm), pooled across the
9 (λ,θ₀) period values above — bare Nyquist requires ≥2 for the fringe to be
resolvable *at all*; ≥10 is this program's own informal "well-resolved"
margin, the same order of headroom T7's floor sits below GATE_HARD (≈9×) and
T11's channel checks use elsewhere):

| FWHM | Δθ_sample(n=41) | samples/period range | vs Nyquist (2) |
|---|---|---|---|
| 2° | 0.250° | **5.65 – 9.95** | 2.8×–5.0× above — comfortably resolved |
| 5° | 0.625° | **2.26 – 3.98** | 1.1×–2.0× above — thin margin |
| 10° | 1.250° | **1.13 – 1.99** | **at or just below Nyquist everywhere** |
| 20° | 2.500° | **0.57 – 0.99** | **below Nyquist everywhere — structurally aliased** |

This is the physical basis for §2.2's ranking predictions, and it already
sharpens exp-046's own finding: FWHM=20° should alias by construction at
n=41 (matches the observed 4.47% move), but **FWHM=10° sits at the Nyquist
line, not comfortably above it** — a genuinely open question exp-046's
single 41-vs-401 jump (which found only 2/36 cells above 1%, `results.json`
`angular_sampling_convergence.n_cells_above_1pct_committed`) may have masked
rather than settled (§4, P-NCONV26-3).

**Ceiling derivation.** Requiring the "well-resolved" bar (10 samples/period)
at the single worst period in the grid (P=1.4127°, 450nm/36°) at the widest
window (FWHM=20°, span=100°): Δθ_req = 1.4127/10 = 0.14127°,
n_req = 100/0.14127 + 1 ≈ **709**. This falls between series entries 641
and 1281 — so **n=1281 already clears the well-resolved bar by ≈1.8×** at
the single hardest cell in the grid, and **n=2561 clears it by ≈3.6×**
(Δθ=0.0391°, ≈36 samples/period at the worst case). The series' top two
entries (2561, 5121) are the Richardson-style pair used to certify
convergence (§2.2): if 1281→2561 AND 2561→5121 both pass tolerance, that is
strong evidence of true asymptotic convergence, not a lucky mid-alias
plateau — the single-doubling risk named directly below.

### 2.2 Convergence criterion — stated formally, before any run

For function f ∈ {`incoherent`, `incoherent_corrected`, `coherent`} and cell
c=(θ₀,fwhm,λ), let C_f,c(n) be `beam_divergence_*`'s scored `C_empty` (Weber
contrast) at quadrature order n. Define, for a doubling step n→2n:

> Δabs(n) = \|C(2n) − C(n)\|   ,   Δrel(n) = 100·\|C(2n) − C(n)\| / \|C(2n)\|
> (Δrel matches exp-046's own reported convention exactly)

**A doubling step is CONVERGED iff Δabs(n) ≤ ABS_TOL=5×10⁻⁴ (0.1·C_THR — an
order of magnitude below the threshold these readings are scored against,
the same margin convention T7's `δ_C ≤ 0.00089` sits below GATE_HARD) AND
Δrel(n) ≤ REL_TOL=1.0%.**

**A cell/function's trustworthy order n\* is the smallest N_SERIES entry
such that BOTH the n\*→2n\* step AND the following 2n\*→4n\* step are
converged** — two consecutive passes, not one. A single pass is not trusted
here because aliasing convergence is not guaranteed monotonic: a doubling
step can coincidentally land near a zero-crossing of the aliasing error
and pass by accident, only to diverge again at the next doubling (exactly
the failure mode a bare single-jump check like exp-046's 41-vs-401 cannot
detect). **n=41 is declared "already converged" for a cell/function iff
n\*=41**, i.e. both 41→81 and 81→161 pass. **If no N_SERIES entry satisfies
the two-consecutive-pass test up to 2561→5121, the cell/function is flagged
NOT CONVERGED WITHIN RANGE** — an explicit, reportable outcome in its own
right, not silently extended.

---

## 3. T1 escape-route statement

**NONE.** This cycle proposes no material law, no σ(I), no σ(x,t), no
angular selectivity, no sub-threshold operation, and no new mechanism class.
It characterizes the numerical convergence of one quadrature kernel already
committed inside the ambient-contrast instrument. Per PANEL.md's Latitude
rule there is nothing exotic to bound; per the Iteration-20/22/23 precedent
an instrument cycle states NONE rather than manufacturing an escape-route
claim. No constraint-3 or constraint-4 verdict is issued, at either tier,
and no result here can move any `REALIZABILITY_MEMO.md` tier.

---

## 4. Falsifiable predicted outcomes — committed BEFORE any run

Nothing below has been computed; every band is derived from the cited
formulas in §2, not pre-run. "Converged value" always means: the value at
the smallest n\* satisfying §2.2's two-consecutive-pass test (or, for cells
flagged NOT CONVERGED WITHIN RANGE, the n=5121 reading, labelled as such).

| ID | Prediction | Committed band | Hard falsification |
|---|---|---|---|
| **P-NCONV26-0** | **Regression gate, checked first.** This audit's own n=41 and n=401 readings reproduce exp-046's committed `angular_sampling_convergence_n41_vs_n401` numbers (both conventions, all 36 cells) | ≤0.1% relative deviation from exp-046's recorded values (worst cell 450nm/36°/FWHM=20°: 4.472688822027389% committed-convention, 3.1838964320070553% corrected-convention) at 36/36 cells | any cell deviates >0.5% ⇒ **no new number in this audit is trusted until the discrepancy is resolved** |
| **P-NCONV26-1a** | **n=41 is NOT already converged for the coherent function** at the FWHM=20° regime | n\*>41 (fails the two-consecutive-pass test at 41) at **≥6 of 9** FWHM=20° cells, central estimate 8/9 | ≤2/9 fail (n=41 already adequate — the aliasing story is wrong at the regime exp-046 itself flagged) |
| **P-NCONV26-1b** | The two incoherent functions are LESS sensitive than the coherent one at FWHM=20° (no coherent grating-lobe construction — quadrature-vs-fringe undersampling only, a weaker effect) | n\*>41 at **≤4 of 9** FWHM=20° cells for EACH of `incoherent`/`incoherent_corrected`, central estimate 1–3/9 | >6/9 fail for either incoherent function (comparable severity to coherent, contradicting the mechanism split) |
| **P-NCONV26-1c** | FWHM≤10° cells are mostly, not universally, converged at n=41 (§2.1's own Nyquist table shows FWHM=10° sits AT the Nyquist line, not clear of it) | n\*=41 (converged already) at **≥70%** of the 27 FWHM≤10° cells, pooled across all 3 functions (≥57/81 cell-function combinations); FWHM=2° alone converged at ≥90% | <50% converged pooled, or FWHM=2° itself <70% converged (would mean even the deepest-oversampled regime is unreliable — a materially worse finding than believed) |
| **P-NCONV26-2** | **Exact predicted difficulty ordering within the 9 FWHM=20° cells**, from §2.1's samples-per-period table: hardest→easiest = (450,36) > (450,38) > (450,40) > (600,36) > (600,38) > (600,40) > (750,36) > (750,38) > (750,40) — monotonic in λ (primary) and θ₀ (secondary), no crossovers | Spearman rank correlation between this predicted order and the measured Δrel(41) magnitudes ≥ **0.70** | correlation < 0.30, or negative sign |
| **P-NCONV26-3** | **FWHM=10° is a genuinely open regime the single 41-vs-401 jump under-reported** (Nyquist ratio 1.13–1.99, i.e. marginal, not the ≥2.8× margin FWHM=2° enjoys) — the incremental doubling series will find FWHM=10° cells with material intermediate movement that a bare 41-vs-401 comparison would mask (non-monotonic convergence, §2.2) | **≥3** of the 12 FWHM=10° cell-function combinations (3λ×3θ₀×any function) show \|Δrel(41)\| > 1% at SOME intermediate doubling step even though their net 41-vs-401 move (recomputed by this audit) is <1% | 0 such cells found (convergence at FWHM=10° is clean and monotonic everywhere) |
| **P-NCONV26-4** | **n=401 is a safe blanket choice for most, not all, of the grid.** n\* ≤ 401 at the large majority of cell-function combinations; the single hardest cell (450nm/36°/FWHM=20°, coherent) needs more | n\* ≤ 401 at **≥85 of 108** cell-function combinations (36 cells × 3 functions); n\* ∈ {641, 1281} at the (450,36,20°) coherent cell specifically | n\* > 401 at more than 25/108 combinations (n=401 is not a safe default anywhere near as broadly as believed), **or** any combination is flagged NOT CONVERGED WITHIN RANGE (a genuinely open-ended failure this program has not seen before) |
| **P-NCONV26-5** | **Sharpest stakes test: exp-042's own committed "zero contamination risk" `incoherent_corrected` near-boundary cell does NOT flip.** Worst cell (750nm, θ₀=38°, FWHM=2°), committed C=−0.004006497410421138 (`experiments/042-.../results.json` `phase5_erratum.block_beam_corrected.worst_cell`), margin ratio 1.2483× below C_THR=0.005. FWHM=2° is the best-converged regime (§2.1) | converged-value relative move at this cell ≤ **1%** (an order of magnitude below the 24.83% headroom needed to cross C_THR) | converged \|C\| exceeds 0.005 (an actual flip — the sharpest possible falsifier this audit can produce), OR the relative move exceeds 5% (still no flip, but contradicts the "small-FWHM already converged" mechanism story) |
| **P-NCONV26-6** | **P-TH23-A1's "36/36 above C_THR" clause survives**; its "35/36 at ≥20× incoherent" sub-clause is AT RISK. Committed min\|C\|=0.03227 (`experiments/046-.../NOTES.md` A1 row) is 6.45×C_THR — far outside plausible single-digit-% movement | 36/36 remain above C_THR at converged n; **1 to 3** of the 36 cells cross below the 20×-incoherent line once BOTH the coherent numerator and incoherent denominator are independently re-evaluated at converged n (errors need not cancel) | all 36 remain ≥20× (sub-clause fully survives), or ≥6 cross (a much larger effect than the aliasing story predicts) |
| **P-NCONV26-7** | **P-TH23-A3 (effective-aperture central-lobe half-width identity) is UNCHANGED** — it measures the coherent sum's central-lobe shape, not the far grating-lobe replica this audit targets, a different sensitivity axis (exp-046 `NOTES.md` A3 row: ≤0.78%/≤3.25% residual bands) | committed residual bands shift by **≤0.5 percentage points** absolute between n=41 and converged n, at all 27/9 cells respectively | any cell's residual shifts >2pp absolute |
| **P-NCONV26-8** | **P-TH23-A4's restored mechanism is CONFIRMED and sharpened, not overturned** — this audit is the direct, full-grid, multi-metric follow-through exp-046 Phase 5 named as the open item | the coherent-function worst-cell relative move at n\*'s converged value remains **within a factor of 2** of exp-046's own recorded 4.473% (i.e. 2.2%–8.9%) | converged move at that cell is <0.5% (mechanism was a one-off, not real) or >15% (exp-046's own figure was itself far from converged) |

**What would make this cycle a failure, stated plainly:** if P-NCONV26-1a
falls the way the null hypothesis predicts (n=41 already adequate
everywhere), the entire aliasing account motivating this audit — and by
extension exp-046's own restored A4 mechanism — is wrong, and the
"documented effect size" Red Team cited to justify this cycle's priority
would itself need re-explaining. That is a real, pre-registered way for this
proposal to lose.

---

## 5. Idealizations (lab convention — stated, not buried)

1. **Scope: `n` only.** `half_width_factor=2.5` (the ±2.5·FWHM truncation,
   >99.9% Gaussian mass per the function's own docstring,
   `design_geometry.py:311`) is held fixed, per the Director's brief. A
   separate truncation-error question exists and is not tested here.
2. **The convergence criterion (ABS_TOL, REL_TOL, two-consecutive-doublings)
   is a modelling choice, disclosed as such, not a law of nature.** A
   different tolerance pair would shift which cells are labelled "converged
   at n=41" without changing any underlying number this audit reports.
3. **The T21 fringe-period model is reused by analogy, not re-derived for
   this exact construction.** T21's period was measured for
   `edge_diffraction_c_empty` (a single-angle, hard-edged-taper C_empty(θ)
   sweep); `beam_divergence_*` integrates a closely related but not
   identical quantity (`field_profile`/coherent-sum values driven by the
   same aperture and propagator). The §2.1 table is therefore this
   proposal's own **prior**, stated to be falsifiable — the sweep itself,
   not the heuristic, is the actual test (P-NCONV26-2's own hard
   falsification band exists precisely because the analogy could be wrong).
4. **Two distinct mechanisms are pooled under one "aliasing" label, disclosed
   as separate.** The coherent function's own sensitivity is a literal
   discrete-Fourier grating-lobe replica (exp-046's own
   `effective_aperture_lobe_census`, `results.json`); the incoherent
   functions' sensitivity, if any, is ordinary weighted-quadrature error
   against an oscillatory integrand. Both are predicted to track FWHM/λ/θ₀
   similarly (§2.1's period-vs-window argument applies to each), but by
   different physical routes — P-NCONV26-1b is the test that keeps them
   from being conflated.
5. **Desk-only; zero new FDTD.** This audit tests whether the ANALYTIC desk
   propagator's own internal angular-quadrature series is self-converged —
   it says nothing about whether the desk propagator matches FDTD (already
   separately validated at exp-046's Block A5, N_F≈0.54–65.6, 0.03–5.68%).
   `lab.ambient.window_means`/`weber`/`incoherent_sum` are reused unmodified,
   as committed.
6. **Floating-point accumulation is negligible.** At n=5121, double-precision
   summation error accumulates to at most ≈5121×2⁻⁵² ≈ 1.1×10⁻¹² relative —
   nine orders of magnitude below ABS_TOL=5×10⁻⁴. Not a competing error
   source at any n in this series.
7. **Scope is exp-042/046's own geometry exactly** (`A=752`, `NY=1584`,
   `D_SP=223`) — not exp-048's re-parameterized `GEOM[78]` domain
   (`A=724`, `NY=1528`). This audit says nothing about whether n=41 is
   converged at that separate geometry; a follow-up would need its own,
   cheap, re-run of the same sweep against exp-048's module.
8. **`n=401` is a single extra evaluation, not a doubling-series member** — it
   exists only to reproduce exp-046's own committed comparison (§4,
   P-NCONV26-0) and is excluded from the two-consecutive-pass convergence
   test, which requires the geometric-doubling structure to be meaningful.
9. **No perceptual claim.** C_THR=0.005 is cited only as the pre-existing
   decision line these readings are already scored against (VISION's T2
   bar) — this cycle issues no new perceptual verdict and pins no new
   threshold.

---

## 6. Cost note

**New FDTD calls: 0.** Pure `numpy`/`math`, reusing `experiments/042-.../
design_geometry.py` unmodified, exactly as exp-046 imported it
(`experiments/046-.../run.py:101,106,108`).

**Scale:** Σ(N_SERIES) + n=401 = 41+81+161+321+641+1281+2561+5121+401 =
**10,609** angle-sample evaluations per (cell, function) combination ×
36 cells × 3 functions = **1,145,772** total angle-sample evaluations. Each
is one cached-matrix `G@amp` product (coherent/incoherent field builds,
`_G_for`/`_G0_for`, `design_geometry.py:194-244`) against the shared
(Y_OBS×Y_SRC)≈1504×1504 propagator, already cached per-λ by the committed
code (`_Gcache`/`_G0cache`) — no new caching needed. Order-of-magnitude
estimate (not yet profiled; this is a Phase-1 proposal, nothing has been
run): low-single-digit minutes to ~20 minutes wall-clock, single-threaded,
zero FDTD, zero engine-file changes.

**Code footprint:** `experiments/049-.../run.py` (new). **No `lab/` file
and no `experiments/042-.../design_geometry.py` line is modified** — the
three functions under test are called, never edited. No new trust-suite
stage is proposed (house convention, exp-048's own precedent: a pure
re-evaluation of an already-committed desk function at different arguments
is not new physics machinery); P-NCONV26-0's regression gate against
exp-046's own recorded numbers plays the equivalent role for this cycle.
