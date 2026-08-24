# exp-065 — The T24 `ABSORB` Boundary Sweep, on the Channel That Scores Constraint 3

*Panel Iteration 42. Lead seat: VISION SCIENCE (rotation). Runner: cloud
panel shift, 2026-08-24. Executes live thread **T24**'s own never-run design
— opened Iteration 23 (exp-046 Phase-5 docket item 19), designed at
Iteration 24 (Tier-2 #4), re-ranked at Iterations 25 (#3), 26 (#2) and 28,
never run in nineteen iterations.*

**Full phase record**: `phase1_proposal.md` · five `phase2_critique_*.md` ·
`phase2_redteam_audit.md` · `phase3_synthesis.md` · this file ·
`phase4_results.md` · six `phase5_review_*.md` · `phase5_redteam_audit.md`.

---

## Hypothesis

T24 established, from four FDTD legs at Iteration 23, that the ambient-
contrast instrument's `C_empty` channel carries an uncharacterized
absorbing-boundary systematic: `ABSORB` 40→60 moved `C` by **+0.0070** at
one beam-channel leg and **−0.0022** at another (real at both, *not* a
monotone convergence) — 0.4–1.4× VISION's own perceptual `C_thr = 0.005`.
T24's own text claims this systematic is "inherited unexamined by every
T21/T16 reading since exp-041."

**That inheritance claim has never been tested.** T24's legs were
Gaussian-beam legs; the channel that actually scores constraint 3 is the
plane/tapered-source ambient channel, where `|C_empty| ~ 0.01` — 10–25×
smaller than the beam channel's `|C| ~ 0.12–0.15`.

**The question this cycle answers:** does T24's systematic transfer to the
scored channel as an **ABSOLUTE** 0.002–0.007 (catastrophic — the
instrument's own floor budget would then be ≥0.4× the lab bar, and every
near-threshold constraint-3 margin this program has ever published would be
undecidable at its stated precision), or as a **RELATIVE** 2–5%
(negligible)? The two hypotheses differ by ~30× on a `|C_empty| ~ 0.01` row.

## Setup

**ONE change**: `absorb` — the graded-loss band thickness in
`lab/fdtd2d.py::Sim._damping` — stops being an inherited constant and
becomes a controlled variable, swept at **congruent** scene geometry.

The trap that kept T24 unrun: `absorb` is not one knob. Raising it in a
fixed domain also moves the band's inner edge toward the measurement plane
and — because `add_line_source`'s default span is `[absorb, ny-absorb]` —
**shrinks the source aperture**, dragging the half-aperture `A` that sets
T21's entire edge-diffraction fringe. The construction: pad the domain by
`PAD = ABSORB − 40` on every side and shift every scene coordinate by the
same amount, holding `A = 752`, plane clearance 37, source clearance 20,
`D_SP = 223`, lever 93 and aperture 1504 identical across the series.

| cfg | ABSORB | PAD | NX×NY | A | role |
|---|---|---|---|---|---|
| C40 | 40 | 0 | 360×1584 | 752 | exp-041's geometry **verbatim** — identity anchor |
| C60 | 60 | 20 | 400×1624 | 752 | congruent |
| **C70** | **70** | **30** | **420×1644** | **752** | congruent — **the non-aliased point** (Phase-3 fix 1) |
| C80 | 80 | 40 | 440×1664 | 752 | congruent |
| G40 | 40 | 40 | 440×1664 | 752 | pad-only control (band unchanged, clearances +40) |
| N60 | 60 | 0 | 360×1584 | **732** | the **naive** protocol, run deliberately as a diagnostic |

Blocks: **SWEEP** (6θ × 3λ empty, at C40/C60/C70/C80/N60) · **PAD** (G40,
3θ × 3λ) · **ARTICLE** (N9 `FALLBACK_ANGLES` @600nm, article + empty, at
C40 and C80) · **BEAM** (T24's own 2 cells, at C40/C60/N60) · **MINI**
(0.5°-step dense angular scan @600nm, C40/C80) · **SETTLE** (`STEPS=2800`
at C80/40°/600nm).

**144 FDTD calls**, projected wall **21.3 min** at the measured 4-worker
cost basis, 3× envelope 64.0 min, **90-minute hard stop** with the
pre-registered de-scope order D0→D5 (`phase3_synthesis.md`).

**T1 escape route: N/A — instrument/model-fidelity class** (*ambient-
contrast instrument boundary-systematic characterization*; precedent
Iterations 20/22/23/26/27/41). No mechanism is proposed; no σ(I), σ(x,t),
angular-selectivity or sub-threshold claim is made or advanced.

## Idealizations

1. **2D TMz, one polarization.** The *boundary* under study is a numerical
   construct with no 3D analogue at all — any number here is a property of
   this engine, not of nature.
2. **The absorbing boundary is graded loss, not PML.** That is the object
   of study, not a defect; no result here transfers to a PML bench.
3. **`STEPS = 1400` held everywhere**, licensed by EM's exp-046 settling
   check measured on the *beam* channel at the *unpadded* domain only.
   Partially closed this cycle by P-VIS42-11 (one padded-domain point), not
   fully.
4. **The padded domains (C60/C70/C80/G40) are geometries this program has
   never run.** Licenses: the congruence assertions in `design_geometry.py`
   §1, the desk propagator's exact degeneracy (§2), and P-VIS42-1b's static
   construction identity (§4b) — which **passed pre-freeze at 0.000e+00**.
5. **Incoherent post-hoc angular summation** (`lab/ambient.py`'s own
   linear-media idiom). T25 is closed at flux level; T26's coherent-
   injection artifact is structurally absent — no coherent joint injection
   occurs anywhere (independently verified against `lab/phase_lines.py`,
   never imported here).
6. **N9 angular quadrature is not converged** (T16/T21). This is why the
   headline is a **delta between configurations at matched angles**, not an
   absolute `C`. The premise that matched-angle differencing cancels the
   quadrature phase error is **no longer assumed** — P-VIS42-10 tests it
   directly (Red Team attack 5 / QUANTUM's catch).
7. **Bench scale only** (r = 78 cells ≈ 2.34 µm at 600 nm). T8/T13/T14's
   witness-scale bridge is unclosed and wrong-signed for this article
   family; nothing here is a witness-scale number.
8. **Block ARTICLE's article is an *analog*, not a re-measurement** — a
   τ_center = 0.0065 uniform-σ disk at *exp-041's* geometry, not exp-032's
   domain. It shares τ and construction idiom with `off_pass`; it does not
   share the domain, so it cannot and does not re-adjudicate exp-032's own
   PASS→MARGINAL history.
9. **Block BEAM inherits exp-046's own disclosed limits**, including
   QUANTUM's Iteration-23 grating-lobe finding (applies at FWHM = 20°
   cells; both BEAM cells here are FWHM = 2°, outside that regime).
10. **Equal-weight angular sum** (`w = 1`), not `cos θ`; the cos-weighted
    re-read is reported, not scored.
11. **(Phase-3 fix 10)** No prior committed `±35°×3λ` `C_empty` figure
    exists anywhere in this program's record at a directly comparable
    geometry — `experiments/041-.../results.json::block_main` covers
    `{-40..-36, 36..40}` only. P-VIS42-1's absolute-identity anchor is
    therefore **silent on the ±35° legs** that Block SWEEP's headline and
    Block ARTICLE's N9 aggregate both use. Disclosed as a real gap, not
    closed.

## Scoring currency — stated once, before any run

**Empty-scene rows are scored against `GATE_HARD = 0.001`** (exp-024/041's
committed instrument-floor gate), **NOT** against a perceptual bar —
repeating exp-041's mandatory fix 1. `C_thr = 0.005` enters the empty-scene
blocks in exactly one licensed role: as the yardstick T24's own headline
("1.39× VISION's own `C_thr`") is quoted in. **Block ARTICLE alone scores a
percept**, against the **lab (cued)** bar 0.005 (Tier-W's observer is the
flashlight holder — the maximally cued case), MARGINAL band [0.5, 2.0]×.

Frozen T2 thresholds, **invoked from `lab/glare_sidecar.py::c_thr`**, not
hand-typed: lab bar **0.005000** (Blackwell 1946 *JOSA* 36:624; van Nes &
Bouman 1967; Campbell & Robson 1968), field bar **0.020000** (CIE 19/2
1981; Adrian 1989), `C_thr(L) = 0.005·max[1,(L/3)^−p]`, p ∈ [0.4, 0.5]
(Rose 1948 *JOSA* 38:196; Hecht/Shlaer/Pirenne 1942).

**No Tier-W or Tier-A verdict is issued by this cycle, in either
direction.** Block ARTICLE's output carries exp-047's mandatory
`TIER_W_HEADLINE_LABEL` discipline: a bench-scale r=78 surrogate reading,
pending the T8/T13/T14 bridge.

**Carried caveats (Phase-3 fixes 4/5/6), code-constants in
`design_geometry.py`, not prose:**
- `REALIZABILITY_MEMO_CAVEAT` — τ=0.0065 is the basis of the memo's
  UNOBTANIUM-WITH-PARAMETERS verdict (D_req≈540–600×), and its own
  Amendment states this τ *no longer clears the bar at either geometry
  checked*; D_req is a LOWER bound, not an achieved PASS. Block ARTICLE
  reuses this τ as an instrument-uncertainty probe ONLY.
- `G_TRANSFER_T15_CAVEAT` — g=0.69 is not portable across geometries
  (T15); the central estimate is descriptive, never scored.
- `T5_THERMAL_CAVEAT` — this article class reads UNDETECTABLE (T5/
  Iteration 20, exp-043, >100× below sourced NETD); that disposition is
  inherited unchanged, no new thermal question is opened.

---

## PREDICTIONS — committed to git BEFORE the run (house discipline, non-negotiable)

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| **P-VIS42-1** | **Anchor identity (absolute gate).** All 12 C40 rows at θ∈{±38,±40}×{450,600,750} reproduce `experiments/041-t20-angle-audit/results.json::block_main` `C_empty` exactly, loaded programmatically. | ΔC = 0.0 for all 12 (float64 equality) | any nonzero Δ. Nothing else is read until this passes. |
| **P-VIS42-1b** | **Static construction identity (absolute gate, REPLACES the voided causal gate).** `static_construction_identity(C40, G40, pad=40)`: `damp_e`/`damp_hx` compared bit-for-bit at scored-window cells. | `max_diff == 0.0` exactly AND `all_vacuum == True` | any nonzero diff ⇒ the padded domain is not a pure vacuum extension; cycle halts. **PASSED pre-freeze at 0.000e+00.** |
| **P-VIS42-2** | **HEADLINE.** Over the 24 SWEEP cells (4 ABSORB pts × 6θ × 3λ, C40-referenced), `ΔC_empty(C80 − C40)`. | median ≤ **1.0×10⁻³** AND max ≤ **3.0×10⁻³** ⇒ *relative transfer*. Central estimate: median **4×10⁻⁴**. | median ≥ **2.0×10⁻³** OR max ≥ **7.0×10⁻³** ⇒ *absolute transfer*: every near-threshold constraint-3 citation in this program is undecidable at its stated margin. Between = PARTIAL. |
| **P-VIS42-2a** | **Aliasing discriminator** (Red Team attack 1). At 600nm, C70 (`ABSORB/λ = 3.5`) vs the C60(3λ)/C80(4λ) linear interpolant. | C70 within **±40%** of the interpolant at all 6 cells ⇒ smooth, non-aliased trend | C70 departs by **>2×** at ≥3 of 6 cells, or falls outside the [C60, C80] bracket ⇒ headline is aliasing-bounded, verdict capped at PARTIAL |
| **P-VIS42-3** | **Scaling discriminator.** Spearman ρ between `\|ΔC_empty(C80−C40)\|` and `\|C_empty(C40)\|`. | ρ ≥ **+0.50** (scales with the reading ⇒ relative) | ρ ≤ **0.0** (additive, reading-independent ⇒ absolute) |
| **P-VIS42-4** | **The naive protocol dominates the effect it was meant to measure.** `\|ΔC(N60−C40)\|` vs `\|ΔC(C60−C40)\|`, per cell. | N60 exceeds C60 at **≥13 of 18** cells, median `\|ΔC(N60−C40)\|` ∈ **[1×10⁻³, 2×10⁻²]** (desk prediction: min 1.301×10⁻³, median 5.286×10⁻³, max 1.898×10⁻²) | ≤9 of 18, OR median outside **[3×10⁻⁴, 4×10⁻²]** |
| **P-VIS42-5** | **Pad-only null.** `\|C_empty(G40) − C_empty(C40)\|` over G40's 9 cells. Desk model predicts exactly 0. | all 9 ≤ **5×10⁻⁴** | any cell ≥ **2×10⁻³** ⇒ the instrument is sensitive to domain padding per se — a second, unnamed systematic, larger news than T24 itself |
| **P-VIS42-6** | **The scored N9 decision floor.** Aggregate N9 `C_empty` @600nm. | `\|C_empty,N9\| ≤ GATE_HARD = 0.001` at **both** C40 and C80, and `\|Δ(C80−C40)\| ≤ 5×10⁻⁴` | either breaches `GATE_HARD`, or `\|Δ\| > 1×10⁻³` |
| **P-VIS42-7** | **The constraint-scored article row.** `off_pass`-analog disk (τ=0.0065), N9/600nm, C40 vs C80. | `\|ΔC(C80−C40)\| ≤ 1.0×10⁻³` AND identical PASS/MARGINAL/FAIL bucket at both | bucket differs, OR `\|ΔC\| > 2.5×10⁻³`. Descriptive-only central estimate **0.00448** (code-produced; carries all three caveats above) |
| **P-VIS42-8** | **T24 beam-channel provenance closure.** Block BEAM reproduces `phase5_redteam_audit.md` §7 from committed code for the first time (`rt_absorb.py` was never committed). | `C(A-v4,40) = +0.154376` and `C(A-v1,40) = −0.125698` to ≤**1%** relative; `ΔC(40→60)` within **±25%** of +0.00696/−0.00220 | outside either ⇒ T24's headline figures do not reproduce from committed geometry — an R4-class finding |
| **P-VIS42-9** | **Cross-channel transfer.** median`\|ΔC_empty(C60−C40)\|` (plane) ÷ median`\|ΔC(C60−C40)\|` (beam). | ratio ∈ **[0.02, 0.30]** | ratio ≥ **0.6** (absolute transfer) or ≤ **0.005** (channels unrelated, inheritance claim void in the opposite direction) |
| **P-VIS42-10** | **Falsifies the "cancels to first order" premise** (Red Team attack 5). `ΔC_empty(θ) = C_empty(C80,θ) − C_empty(C40,θ)` over θ ∈ {38, 38.5, 39, 39.5, 40}° @600nm (≥1 full T21 period, `P(40°)=1.989°`). | delta stays within **±30%** of its own mean across the span (flat ⇒ additive-systematic framing holds) | peak-to-trough range **>2×** its own mean at a period matching `P(θ)` to within 20% ⇒ coherent-fringe perturbation, not an additive systematic |
| **P-VIS42-11** | **Settling robustness** (Red Team attack 7 / T10 precedent). `\|C_empty(C80, 2800) − C_empty(C80, 1400)\|` at θ=40°, 600nm. | ≤**0.15%** relative (comparable to exp-046's 0.083%/0.036%) | >**1%** relative ⇒ settling is a live confound on P-VIS42-2's headline, which must then be reported as bounded by this uncertainty |

**Checkpoint-criterion-2 candidacy: none.** No mechanism class is bounded
here. What this cycle *can* produce is a criterion-4-adjacent finding — if
P-VIS42-2 REFUTES, this program's own near-threshold constraint-3 margins
are not decidable at their stated precision, and that must be propagated to
T16, T21 and every `C` citation, not absorbed as a footnote.

## Gates

Full bench (`--only 12346789,10,11,18,19,20,21,22,23,24`) green before and
after — **107/107 verified this shift before any panel work began**. No new
trust-suite stage (zero `lab/` diff; `run.py` asserts this before results
are read). Binding stages: 1 (angle_deg=0 bit-exactness), 6 (phasor
conventions), 9 (the ambient instrument itself), 16 (gauss pointing chain,
Block BEAM), 17 (`c_thr`). Two local **absolute-identity** gates, G-1
(P-VIS42-1) and G-2 (P-VIS42-1b), gate every other number.

---

## Result

Both absolute-identity gates PASSED. Of 11 scored predictions, 4 REFUTED
(P-VIS42-2 headline, -5, -10, -11), 5 CONFIRMED, 1 PARTIAL, 1 (2a)
CONFIRMED. **But P-VIS42-11's REFUTE (a 59.8% settling shift at STEPS=1400
vs 2800, ~400× past its own bar) reopens the whole cycle**: a same-shift
follow-up (4-point convergence trend + a full settled STEPS=2800 re-sweep,
disclosed and unscored) shows STEPS=1400 is not settled on this program's
plane/empty-scene channel at ±38°/±40°, general to the channel (confirmed
on the UNPADDED C40 anchor geometry too, not padding-specific), and that
correcting for it shrinks the headline median 5.4× (0.00279→0.00052, now
clearing its own CONFIRM band) with a residual concentrated at 750nm, not
yet shown fully converged. **Phase 5 (MATERIALS, VISION SCIENCE) found the
gap is wider than first reported: ±35° — inside Block ARTICLE's own N9
angle set — sign-flips under the same correction, so P-VIS42-6/7's
CONFIRMED verdicts are also unconfirmed, not just the headline.** T24's
own inheritance question is undecided by this cycle. Full record, all
numbers: `phase4_results.md`.

## Learned

**The cycle's real finding is not about T24.** `experiments/041-t20-angle-
audit` (Iteration 18) established this program's ±38°/±40° angle standard
at STEPS=1400 on this identical channel — the same channel just shown to
read ~3.9× off its converged value at that step count. Every T21/T24
citation since Iteration 18 (nineteen iterations) may rest on an unsettled
transient. A settling check calibrated on one channel (exp-046's Gaussian
beam) does not transfer to a structurally different channel (tapered
plane source, empty scene) at the same angles — settling is per-channel,
not per-geometry. The desk propagator's exact degeneracy proves steady-
state identity, not that STEPS reaches it. Full discussion:
`phase4_results.md`.

## Next

Not a ruling — for Phase 5 to weigh:
1. Re-verify exp-041's own MAIN-block ±38°/±40° rows at STEPS≥2800 and
   scope how many downstream citations (T21, T24, near-threshold
   constraint-3 numbers) are affected.
2. A matching 4-point convergence trend at 750nm/C80 (or another high-cpl,
   large-padding cell) — Diagnostic 3's residual may itself be unsettled,
   not yet shown otherwise.
3. Re-score T24's own inheritance question cleanly at a verified-settled
   STEPS value — this cycle's construction (congruent ABSORB series, the
   C70 non-aliased point, the static construction identity gate) is
   reusable as-is; only STEPS needs correcting.

Whether this constitutes a Checkpoint-criterion-4 finding is explicitly
left to Phase 5 / Red Team's ruling, not pre-empted here (see
`phase4_results.md`'s closing section).
