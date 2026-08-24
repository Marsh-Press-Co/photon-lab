# PHASE 1 — PROPOSAL · Panel Iteration 42 · Lead seat: VISION SCIENCE
## exp-065 — "The T24 `ABSORB` Boundary Sweep, on the Channel That Scores Constraint 3"

*Runner: cloud panel shift. Lead: VISION SCIENCE, by rotation. Executes live
thread **T24**'s own never-run design — opened Iteration 23 (exp-046 Phase-5
docket item 19), designed at Iteration 24 (Tier-2 #4), re-ranked at Iterations
25 (#3), 26 (#2) and 28, never run in nineteen iterations. All arithmetic in
this document is produced by `python3 design_geometry.py` (output captured in
`design_geometry_output.txt`); nothing is hand-typed (house rules R4/R5).*

---

## 0. Engaging the Director's framing, on the record

Red Team's Iteration-41 Phase-5 §9 issued a **recommendation**: Iteration 42's
lead should scope its item to close into, or directly feed, an actual
constraint-scored FDTD run, after four consecutive zero-FDTD cycles.

**This proposal satisfies it directly, not by argument.** It is 119 FDTD
calls; its Block ARTICLE scores a real σ(I) OFF-state article's Weber contrast
against VISION's own frozen constraint-3 ladder; and its headline product is
the missing uncertainty term on the instrument that every constraint-3 verdict
this program has ever issued depends on. PLAN.md's three queued items (CNT
`R_contact`, `length_provenance` hardening, the CNT query bundle) are all
zero-FDTD desk/analytic work in THERMO's and MATERIALS' charters; they remain
valid backlog and nothing here narrows them.

**Why this item and not one of those, stated so Red Team can attack it.**
T24 is the only long-deferred item on the board that is simultaneously (a) in
VISION's charter — it is a threshold-comparison question, its own headline
number is quoted as "1.39× VISION's own C_thr", (b) FDTD-native, (c)
constraint-3-bearing, and (d) *upstream of every future near-threshold
constraint-3 verdict*. T24's own text says its systematic is "inherited
unexamined by every T21/T16 reading since exp-041, including all 30 Block MAIN
rows T21's fringe mechanism was fitted to and every N9/N17 quadrature delta
T16 scores." Until it is measured, no future constraint-3 run's margin against
0.005 can be believed, because the instrument's own floor budget is unknown to
within 1.4× that bar. This is the same class of debt as T11, and this program's
own record (r=156, `h_eff`, `graded_black_shell_flagship`, the absorptivity
check) shows that debts of this class are only ever paid when a lock or a
rotation forces them.

---

## 1. Mechanism narrative (≤300 words)

**ONE change: `absorb` — the graded-loss band thickness in
`lab/fdtd2d.py::Sim._damping` — stops being an inherited constant and becomes
a controlled variable, swept at *congruent* scene geometry.**

This is an instrument/model-fidelity cycle, not a mechanism proposal. No new
physics, no `lab/` edit, no new material law.

The trap that has kept T24 unrun is that `absorb` is not one knob. Raising it
in a fixed domain simultaneously (i) thickens the band, (ii) moves the band's
inner edge toward the measurement plane, and (iii) — because
`add_line_source`'s default span is `[absorb, ny-absorb]` — **shrinks the
source aperture**, dragging the half-aperture `A` that sets T21's entire
edge-diffraction fringe. `A` is *defined* as `OBJ_Y − ABSORB` in
`experiments/042-t21-magnitude-bridge/design_geometry.py:135-137`.

The construction: pad the domain by exactly `PAD = ABSORB − 40` on every side
and shift every scene coordinate by the same amount. Then `A = 752`,
plane-to-band clearance `= 37`, source-to-band clearance `= 20`, `D_SP = 223`,
lever `= 93` and aperture `= 1504` cells are all held **identically** across
`ABSORB ∈ {40, 60, 80}` (verified by assertion in `design_geometry.py` §1).
Independently confirmed: exp-048's committed, boundary-free desk propagator
`edge_diffraction_c_empty_corrected` returns **bit-identical** `C_empty` for
all three configurations (`max |Δ| = 0.000e+00`, §2) — so every difference the
FDTD returns is boundary physics *by construction*.

Two controls ride alongside: **G40** (pad only, band unchanged) isolates the
padding itself; **N60** (the naive same-domain bump, `A` → 732) quantifies
what the protocol T24 warned against would have added. The question VISION
actually needs answered: does T24's systematic transfer to the scored channel
as an **absolute** 0.002–0.007 (catastrophic against `C_thr = 0.005`) or as a
**relative** 2–5% (negligible)?

---

## 2. Parameter table

### 2.1 Base geometry — copied verbatim, not recomputed

Every constant below is `experiments/041-t20-angle-audit/design_geometry.py`
(itself verbatim from exp-024), and is re-asserted in
`design_geometry.py:69-89`.

| Knob | Value | Provenance |
|---|---|---|
| `BASE_NX` / `BASE_NY` | 360 / 1584 | exp-041 `design_geometry.py:123,159-160` |
| `BASE_ABSORB` | 40 | exp-041 `:124` |
| `SRC_X` / `PLANE_X` / `OBJ_X` | 300 / 77 / 170 | exp-041 `:126,131,130` |
| `OBJ_Y` | 792 (`NY//2`) | exp-042 `design_geometry.py:133` |
| `TAPER` (source edge) | 40 | exp-041 `:127` |
| `R_OUT` / `W_OBJ` / `GUARD_OUT` / `W_FLANK` | 78 / 78 / 185 / 78 | exp-041 `:128,133-136` |
| `CPL` | {450: 15, 600: 20, 750: 25} | exp-041 `:125` |
| `STEPS` / `courant_frac` | 1400 / 0.99 | exp-041 `:146`; `lab/fdtd2d.py:73` |
| `D_SP` / `LEVER` | 223 / 93 | derived, exp-041 `:143-144` |
| `FALLBACK_ANGLES` | (−35,−25,−15,−5,0,5,15,25,35) | exp-024 `design_geometry.py:51` |
| `A` (half-aperture) | 752 | `OBJ_Y − y_lo`, exp-042 `:137` |

### 2.2 The five configurations (produced by `design_geometry.py` §1)

```
  cfg   ABS  PAD    NX    NY  SRC_X PLANE_X  OBJ_Y  y_lo  y_hi     A  aper  clrPl clrSrc clrSpan  D_SP
  C40    40    0   360  1584    300      77    792    40  1544   752  1504     37     20       0   223
  C60    60   20   400  1624    320      97    812    60  1564   752  1504     37     20       0   223
  C80    80   40   440  1664    340     117    832    80  1584   752  1504     37     20       0   223
  G40    40   40   440  1664    340     117    832    80  1584   752  1504     77     60      40   223
  N60    60    0   360  1584    300      77    792    60  1524   732  1464     17      0       0   223
```

- **C40** is exp-041's geometry **verbatim** (identity anchor).
- **C40/C60/C80** = the congruent `ABSORB` series. Asserted in code to hold
  `A`, `clrPl`, `clrSrc`, `clrSpan`, `D_SP`, `LEVER`, `aper` constant.
- **G40** = pad-only control (band unchanged; every clearance +40).
- **N60** = the naive protocol: `A` drops 752 → 732 (−2.66%), aperture 1504 →
  1464, plane clearance 37 → 17, and the source now sits *on* the +x band's
  innermost cell. Run deliberately and labelled, as a diagnostic.

### 2.3 Source, article, reduction

| Knob | Value | Note |
|---|---|---|
| Source | `add_line_source(SRC_X, y_lo=…, y_hi=…, angle_deg=θ, edge=40, amplitude=1.0)` | span passed **explicitly** in every non-naive leg — the fix T24's own design note demanded |
| Beam legs (Block BEAM) | `profile="gauss"`, `width = w₀/cosθ₀`, `w₀ = C·λ/Δθ`, `C = 2√(2ln2)/2π` | exp-046 `run.py::w_line_cells` reused verbatim (trust-suite stage 16) |
| Article (Block ARTICLE) | uniform-σ disk, r = 78, `σ_e = 4.1666666666666665e-05` | `τ_center = 0.0065 = off_pass` (exp-032/033/034/056); `σ = τ/(2·r_out)`, this lab's convention |
| Reduction | `sections.phasors` → `ambient.observer_profile` → `ambient.window_means` → `ambient.weber` | unchanged; the only route from a profile to a number |
| Angular sum | `ambient.incoherent_sum`, equal weights | incoherent pipeline only. **No coherent joint injection anywhere** — T26's artifact is structurally out of scope |
| Sweep angles | θ ∈ {−40, −38, −35, +35, +38, +40}° | ±40/±38 = T24/T21's own window and exp-041's own rows; ±35 = the scored `FALLBACK` extreme |
| Wavelengths | 450 / 600 / 750 nm, all blocks except ARTICLE (600 nm) | 3-λ house sweep |

### 2.4 Desk-propagator predictions (zero FDTD, computed §2 of the script)

Using exp-048's committed `edge_diffraction_c_empty_corrected` — a
boundary-free coherent Huygens–Fresnel sum, zero free parameters:

| quantity | value |
|---|---|
| `max │desk(C60/C80) − desk(C40)│`, 9 cells | **0.000e+00** (exact degeneracy) |
| `max │desk(G40) − desk(C40)│`, 9 cells | **0.000e+00** (exact degeneracy) |
| `│desk(N60) − desk(C40)│`, 9 cells | min **1.301e−03**, median **5.286e−03**, max **1.898e−02** |
| T21 period `P(40°)` at A=752 / A=732 | 1.492/1.533° (450 nm), 1.989/2.044° (600), 2.487/2.554° (750) |
| fringe phase shift at θ=40° from A 752→732 | **0.857 / 0.643 / 0.514 cycles** at 450/600/750 nm |

**This is the load-bearing new fact this proposal contributes.** A naive
in-domain `ABSORB` 40→60 bump re-phases T21's own edge-diffraction fringe by
**half a period or more**, and exp-048's own committed propagator predicts that
this alone produces a `C_empty` shift of median 5.3×10⁻³ — *larger than the
entire 0.002–0.007 systematic T24 attributes to the boundary.* Whether
`rt_absorb.py` held the span is unknowable: **the file was never committed**
(`find . -name rt_absorb.py` → zero hits, checked this shift); the four legs
behind T24's headline exist only as a prose table in
`experiments/046-…/phase5_redteam_audit.md:617-624`.

*Scoping this honestly:* T24's own legs were **Gaussian-beam** legs
(`profile="gauss"`, FWHM = 2°, w₀ ≈ 28–56 cells). For a Gaussian source the
span change truncates wings at ≈10⁻¹⁴⁵ of peak, so the aperture confound is
**negligible there** and T24's beam-channel numbers are almost certainly a
genuine boundary effect. The confound bites on the **plane/tapered** source —
i.e. on exactly the channel T24 claims its systematic is *inherited by*, and
on which it has never been measured. This proposal does not claim T24 is
wrong; it claims T24's **inheritance** claim is untested and would be
mis-measured by the obvious protocol.

---

## 3. The T1 escape route taken

**N/A — instrument/model-fidelity class.** Class named: *ambient-contrast
instrument boundary-systematic characterization* (the exp-024 / 029 / 033 /
034 / 035 / 041 / 049 / 050 / 055 / 056 lineage). Precedent for an explicit
N/A: Iterations 20, 22, 23, 26, 27, 41.

No new mechanism is proposed; no σ(I), σ(x,t), angular-selectivity or
sub-threshold claim is made or advanced. Block ARTICLE re-scores an
**already-existing** article class (the `off_pass` OFF-state τ = 0.0065
sponge disk) in order to place an instrument-uncertainty bar on it — it does
not propose that article as a solution and issues no Tier-W/Tier-A verdict.

Per T17's standing requirement, self-classification of the article: it is a
**static, linear, time-invariant** uniform-σ disk — the frozen OFF endpoint of
a memoryless σ(I) law, not a hysteretic one. No `k_f`/`k_r` are involved
because no kinetics is simulated; the disk is an LTI stand-in and is labelled
as such.

---

## 4. Pre-registered predictions, with falsifiable bands

Scoring currency, stated once: **empty-scene rows are scored against
`GATE_HARD = 0.001`** (exp-024/041's own committed instrument-floor gate), NOT
against a perceptual bar — repeating exp-041's mandatory fix 1 (VISION's own
catch: an instrument floor scored against `C_thr` conflates instrument
characterization with a perceptual verdict). `C_thr = 0.005` appears only where
the *comparison to a perceptual threshold is itself the question*, and is
labelled there.

| ID | Claim | CONFIRM band | REFUTE band |
|---|---|---|---|
| **P-VIS42-1** | **Anchor identity (absolute gate).** All 12 C40 rows at θ∈{±38,±40}×{450,600,750} reproduce `experiments/041-t20-angle-audit/results.json::block_main` `C_empty` **exactly**. | ΔC = 0.0 for all 12 (float64 equality) | any nonzero Δ. Nothing else in this experiment is read until this passes. *Status: 1 of 12 already verified pre-freeze this shift — θ=+40, 600 nm, reproduced `−0.010964794540566314` bit-identically.* |
| **P-VIS42-1b** | **Pad-construction causal identity (absolute gate).** At step `n = 359` (computed by `causal_identity_step`, §4 of the script: binding path = 2·20+223 = 263 cells at S = 0.700036 cells/step, minus a 16-step guard), the C40 and G40 observer-plane rows, aligned by the (+40,+40) shift and restricted to the scored object∪flank window cells, are identical. | `max│ΔEz│ = 0.0` exactly | any nonzero value ⇒ the padded domain is not a pure vacuum extension and §1's congruence argument fails; Phase 4 halts and diagnoses before any sweep number is read. |
| **P-VIS42-2** | **HEADLINE — the boundary systematic on the scored (plane-source) channel.** Over the 18 SWEEP cells, `ΔC_empty(C80 − C40)`. | median ≤ **1.0×10⁻³** AND max ≤ **3.0×10⁻³** ⇒ *relative transfer*. Central estimate: median **4×10⁻⁴** (= 4% of the anchor rows' own median │C_empty│ = 1.04×10⁻²). | median ≥ **2.0×10⁻³** OR max ≥ **7.0×10⁻³** ⇒ *absolute transfer*: T24's beam-channel 0.002–0.007 carries over intact, the ambient instrument's floor budget is ≥ 0.4× VISION's lab bar, and every near-threshold constraint-3 citation in this program is un-decidable at its own stated margin. Anything between = PARTIAL. |
| **P-VIS42-3** | **Scaling discriminator.** Spearman ρ between `│ΔC_empty(C80−C40)│` and `│C_empty(C40)│` over the 18 cells. | ρ ≥ **+0.50** (systematic scales with the reading ⇒ relative) | ρ ≤ **0.0** (systematic is additive and reading-independent ⇒ absolute) |
| **P-VIS42-4** | **The naive protocol dominates the effect it was meant to measure.** Compare `│C_empty(N60)−C_empty(C40)│` against `│C_empty(C60)−C_empty(C40)│`, per cell. | N60 exceeds C60 at **≥ 13 of 18** cells, and median `│ΔC(N60−C40)│` ∈ **[1×10⁻³, 2×10⁻²]** (the desk propagator's own zero-FDTD prediction: min 1.301×10⁻³, median 5.286×10⁻³, max 1.898×10⁻²) | ≤ 9 of 18, OR median outside **[3×10⁻⁴, 4×10⁻²]** ⇒ the aperture/clearance re-phasing is not the dominant term and the naive protocol would have been adequate. |
| **P-VIS42-5** | **Pad-only null.** `│C_empty(G40) − C_empty(C40)│` over G40's 9 cells (θ∈{−35,+35,+40}×3λ). Desk model predicts exactly 0. | all 9 ≤ **5×10⁻⁴** | any cell ≥ **2×10⁻³** ⇒ the instrument is sensitive to domain padding *per se* — a second, previously unnamed systematic on the same channel, larger news than T24 itself. |
| **P-VIS42-6** | **The scored N9 decision floor.** Aggregate N9 (`FALLBACK_ANGLES`, equal weights) `C_empty` at 600 nm. | `│C_empty,N9│ ≤ GATE_HARD = 0.001` at **both** C40 and C80, and `│Δ(C80−C40)│ ≤ 5×10⁻⁴` (≤ 0.1 × the frozen lab bar) | either configuration breaches `GATE_HARD`, or `│Δ│ > 1×10⁻³` |
| **P-VIS42-7** | **The constraint-scored article row.** `off_pass`-analog disk (τ_center = 0.0065), N9/600 nm, C40 vs C80. Ladder: lab bar 0.005, MARGINAL band [0.5, 2.0]× (exp-048 Block C, `lab/glare_sidecar.py::tier_w_verdict`). | `│ΔC(C80−C40)│ ≤ 1.0×10⁻³` **and** identical PASS/MARGINAL/FAIL bucket at both configurations | bucket differs between configurations, OR `│ΔC│ > 2.5×10⁻³` (half the lab bar). Descriptive-only central estimate for │C│ itself: **0.00449** (= g·τ at T1's g ≈ 0.69) — reported, **not scored**, because g is geometry-specific (T15). |
| **P-VIS42-8** | **T24 beam-channel provenance closure.** Block BEAM reproduces `phase5_redteam_audit.md`'s §7 table from committed code for the first time. | `C(A-v4, ABSORB=40) = +0.154376` and `C(A-v1, ABSORB=40) = −0.125698` to ≤ **1%** relative; `ΔC(40→60)` within **±25%** relative of +0.00696 / −0.00220 | outside either ⇒ T24's headline figures do not reproduce from the committed geometry — an R4-class finding, since `rt_absorb.py` was never committed. |
| **P-VIS42-9** | **Cross-channel transfer (the synthesis).** ratio = median`│ΔC_empty(C60−C40)│` (plane channel, Block SWEEP) ÷ median`│ΔC(C60−C40)│` (beam channel, Block BEAM). | ratio ∈ **[0.02, 0.30]** — the plane channel's *absolute* systematic is 3–50× smaller because its │C│ is 10–25× smaller | ratio ≥ **0.6** (absolute transfer, T24 inherits at full size) or ≤ **0.005** (the channels are unrelated and T24's inheritance claim is void in the opposite direction) |

**What would make this cycle a Checkpoint-criterion-2 candidate:** nothing.
No mechanism class is bounded here. What it *can* produce is a
criterion-4-adjacent finding — if P-VIS42-2 REFUTES, this program's own
near-threshold constraint-3 margins are not decidable at their stated
precision, and that must be propagated to T16, T21 and every `C` citation, not
absorbed as a footnote.

---

## 5. Charter duty discharged — the numeric perceptual thresholds, before any run

**These are the ALREADY-FROZEN T2 thresholds. I am reusing, not re-deriving,
them.** Frozen at Iteration 1 Phase 1 §3 (LOGBOOK.md lines 1718–1726), corrected
at Phase 3 per Red Team attack #2 (crossover re-derived from the committed
function), re-committed in `experiments/020-ambient-baseline/NOTES.md`, and
implemented as code in `lab/glare_sidecar.py::c_thr` (trust-suite stage 17).
**Every number below was produced by invoking that committed function**
(`design_geometry.py` §5), not hand-typed:

| Quantity | Value | Source |
|---|---|---|
| Lab (cued) bar, photopic | `c_thr(3.0, 0.4, bar="lab")` = **0.005000** | Blackwell 1946, *JOSA* 36:624 (121-arcmin asymptote 0.003–0.005 at ≥3 cd/m²); corroborated van Nes & Bouman 1967, *JOSA* 57:401; Campbell & Robson 1968, *J. Physiol.* 197:551 |
| Field (uncued) bar | `c_thr(3.0, 0.4, bar="field")` = **0.020000** (×4) | CIE Pub. 19/2 (1981); Adrian 1989, *Light. Res. Technol.* 21:181 |
| Threshold function | `C_thr(L) = 0.005·max[1,(L/3 cd·m⁻²)^−p]`, clipped at 1, p ∈ [0.4, 0.5], ±0.3 log vertical | Rose 1948, *JOSA* 38:196 (Rose–de Vries L^−0.5); absolute rod limit Hecht, Shlaer & Pirenne 1942, *J. Gen. Physiol.* 25:819 |
| Night-ambient table (lab bar, p = 0.4 … 0.5) | L=10⁻¹: **0.0195 … 0.0274**; 10⁻²: **0.0490 … 0.0866**; 10⁻³: **0.1230 … 0.2739**; 10⁻⁴: **0.3089 … 0.8660** | invoked from `c_thr` |
| MARGINAL band convention | **[0.5, 2.0] × bar** | `lab/glare_sidecar.py::tier_w_verdict`; sourced/retained at exp-048 Block C (P-C1/C2/C3 CONFIRMED) |
| Instrument-floor gate | **`GATE_HARD` = 0.001** | exp-024 `run.py:40-44`, exp-041 `design_geometry.py:175-177` — **not a perceptual bar** |

**Are these the right currency for what I propose to measure? Partly, and I
state the split explicitly, because getting this wrong is exactly the error
exp-041's mandatory fix 1 corrected:**

1. **Blocks SWEEP / PAD / ANCHOR measure an *instrument floor*, not a
   percept.** Their scoring bar is `GATE_HARD = 0.001`. `C_thr = 0.005` enters
   these blocks in exactly one licensed role — as the yardstick T24's own
   headline ("1.39× VISION's own C_thr") is quoted in, so that P-VIS42-2's
   verdict can be stated in the same units the thread was opened in. It is
   labelled `GATE_PERCEPTUAL_CONTEXT` in code, never "the gate".
2. **Block ARTICLE alone scores a percept.** Its bar is the **lab (cued)**
   bar 0.005, per Red Team's Iteration-24 mandatory fix 4: Tier-W's observer
   is PANEL.md's "flashlight holder", the maximally *cued* case, so the cued
   bar is the default; the field bar is computed and reported as disclosed
   context and never substituted into a headline.
3. **The scotopic table is carried, not scored, this cycle.** Nothing here
   varies ambient luminance, so `C_thr(L)`'s low-L branch is recorded for
   continuity (and because a boundary systematic of ≥2×10⁻³ would be
   *irrelevant* at L ≤ 10⁻³ cd/m², where `C_thr ≥ 0.12 — 24×` larger — a
   Tier-W-vs-Tier-A asymmetry the Phase-5 reading must state).
4. **No Tier-W or Tier-A verdict is issued by this cycle, in either
   direction.** Block ARTICLE's output carries exp-047's mandatory
   `TIER_W_HEADLINE_LABEL` discipline verbatim: a bench-scale r = 78 surrogate
   reading, pending the T8/T13/T14 near-field→witness-scale bridge, **not** a
   witness-scale constraint-3 verdict.
5. **Known threshold-side limits, restated so they are not smuggled:**
   `C_thr` is a *static-target* threshold applied here to a static scene (fine)
   — but T3's temporal instrument still does not exist, so nothing here bears
   on constraint 4; and `C_thr`'s Blackwell/Rose calibration has never been
   verified for localized/near-field glare geometry (Red Team, Iteration 24
   fix 6) — not invoked this cycle, since no glare term appears.

---

## 6. Idealizations, plainly

1. **2D TMz, one polarization.** Rods and cones are polarization-blind; the
   article is dielectric-only, so this is benign for it — but the *boundary*
   under study is a numerical construct with no 3D analogue at all. Any
   number here is a property of this engine, not of nature.
2. **The absorbing boundary is graded loss, not PML.** That is the object of
   study, not a defect — but a PML would have a different systematic, and no
   result here transfers to a PML bench.
3. **`STEPS = 1400` held everywhere.** Licensed by EM's exp-046 settling
   check (1400→2800→4200 moved C by 0.083%/0.036%) — measured on the **beam**
   channel at the **unpadded** domain only. Not re-verified on the plane
   channel or in the padded domains. A stated gap.
4. **The padded domains (C60/C80/G40) are geometries this program has never
   run.** Their only licenses are (a) the congruence assertions in
   `design_geometry.py` §1, (b) the desk propagator's exact degeneracy (§2),
   and (c) P-VIS42-1b's causal identity gate. If (c) fails, the cycle stops.
5. **Incoherent post-hoc angular summation** (`lab/ambient.py`'s own
   linear-media idiom). T25 is closed at flux level; T26's coherent-injection
   artifact is structurally absent because no coherent joint injection occurs.
6. **N9 angular quadrature is not converged** (T16/T21: N9 samples a real
   sub-N17-spacing fringe at effectively uncorrelated phase points). Every
   *absolute* N9 number here inherits that. **This is why the headline is a
   DELTA between configurations at matched angles, not an absolute C** —
   matched-angle differencing cancels the quadrature phase error to first
   order; the absolute N9 values in P-VIS42-6/7 are reported with the T16
   caveat inline.
7. **Bench scale only** (r = 78 cells ≈ 2.34 µm at 600 nm). T8/T13/T14's
   bridge is unclosed and wrong-signed for this article family; nothing here
   is a witness-scale number.
8. **Block ARTICLE's article is an *analog*, not a re-measurement.** It is a
   τ_center = 0.0065 uniform-σ disk at *exp-041's* geometry, not exp-032's own
   domain. It shares τ and construction idiom with `off_pass`; it does not
   share the domain, so it cannot and does not re-adjudicate exp-032's own
   PASS→MARGINAL history.
9. **Block BEAM inherits exp-046's own disclosed limits** — including
   QUANTUM's Iteration-23 Phase-5 grating-lobe finding, which applies at
   FWHM = 20° cells; both BEAM cells here are FWHM = 2°, outside that regime.
10. **Equal-weight angular sum** (`w = 1`), not `cos θ`; the cos-weighted
    re-read is a free post-hoc re-weight of the same runs and will be
    reported, not scored.

---

## 7. FDTD budget — call count, cost basis, wall clock, de-scope order

### 7.1 Call count (computed by `design_geometry.py::fdtd_budget`)

| Block | C40 | C60 | C80 | G40 | N60 | total |
|---|---|---|---|---|---|---|
| SWEEP (6θ × 3λ, empty) | 18 | 18 | 18 | — | 18 | 72 |
| PAD (3θ × 3λ, empty) | — | — | — | 9 | — | 9 |
| ARTICLE (N9 @600: 9 article + 7 new empty) | 16 | — | 16 | — | — | 32 |
| BEAM (2 T24 cells) | 2 | 2 | — | — | 2 | 6 |
| **per configuration** | **36** | **20** | **34** | **9** | **20** | **119** |

(±35°@600 nm empty legs are shared between SWEEP and ARTICLE — counted once.
P-VIS42-1b's two 359-step runs are ≈0.26 of a full call each and are absorbed
inside the G40 allocation.)

### 7.2 Cost basis — **measured on this container this shift, not cited**

Four concurrent calls per domain under `ProcessPoolExecutor(max_workers=4)`,
cpl = 20, `STEPS = 1400`, `sections.full_capture`, i.e. with the real
memory contention:

| domain | per-call CPU (4 measurements) | used |
|---|---|---|
| 360×1584 (C40, N60) | 24.48 / 25.53 / 24.26 / 25.33 s | **25.0 s** |
| 400×1624 (C60) | 29.48 / 30.95 / 32.58 / 31.30 s | **31.1 s** |
| 440×1664 (C80, G40) | 34.55 / 34.08 / 35.49 / 35.17 s | **34.8 s** |

Wall for 4 concurrent calls at 440×1664 = **35.51 s** ⇒ parallel efficiency
**0.981** (`nproc` = 4). Capture footprint **35.1 MB/sim**, 14 GB free — no
memory risk at 4 workers. Cross-check, single process, smallest domain:
**20.651 s**, and that call reproduced exp-041's committed `C_empty`
bit-identically.

Cost scales *worse* than cell count on this box (C80/C40 = 1.39× for a 1.28×
cell ratio); the measured per-domain figures are used, not an extrapolation.

### 7.3 Wall-clock

```
projected CPU  = 3518 s = 58.6 min
projected WALL = 1032 s = 17.2 min   (4 workers @ 98%, ×1.15 reduction/JSON overhead)
3× safety envelope   = 51.6 min
```

Compare the program's largest timing miss (exp-030's r = 312 leg, 3.87 h): that
domain is ~16× this one in area. This cycle sits two orders of magnitude
inside that failure mode. **Hard stop: if wall-clock passes 90 minutes, the
de-scope order below fires without further deliberation.**

### 7.4 Pre-registered de-scope order (fires in this order, on overrun)

1. **D1 — Block SWEEP, N60 at 450 and 750 nm** (−12 calls). P-VIS42-4 then
   scores at 600 nm only (6 cells); disclosed as single-λ.
2. **D2 — Block BEAM's C60 leg** (−2 calls). P-VIS42-8 (provenance) survives
   intact on C40/N60; P-VIS42-9 is withdrawn and reported as not-run.
3. **D3 — Block SWEEP, C60 at 450 and 750 nm** (−12 calls). The three-point
   monotonicity read collapses to 600 nm; P-VIS42-2/3 still score on C80−C40
   at all 18 cells.
4. **D4 — Block ARTICLE, N9 → N5** (θ ∈ {0, ±15, ±35}) at both configurations
   (−16 calls). P-VIS42-6/7 rescored at N5 with exp-020's own N5-vs-N9
   convergence bound stated inline as an added uncertainty.
5. **D5 — Block SWEEP, C80 at 450 and 750 nm** (−12 calls). P-VIS42-2 becomes
   single-λ; if D5 fires, the cycle's verdict is capped at PARTIAL by
   construction and said so in NOTES.md.

**Never dropped, at any overrun:** Block SWEEP C40 (the anchor and its
12-row bit-identity gate), Block PAD's causal-identity pair, and Block
ARTICLE's C40-vs-C80 comparison in at least N5 form. If those cannot complete,
the cycle is abandoned and reported as abandoned, not partially reported.

---

## 8. Gates

### 8.1 Trust-suite stages that bind this result

`lab/validation/run_all.py` — **full bench before and after, no number read
until green**: `--only 12346789,10,11,18,19,20,21,22,23,24` → the 107/107 the
Director verified this shift.

Specifically binding:
- **stage 1** — `angle_deg = 0` bit-exactness / engine regression (the source
  path this cycle drives at five different `absorb` values).
- **stage 6** — observer record / phasor conventions (`sections.phasors`,
  the phasor-bug lesson).
- **stage 9** — the ambient instrument itself: oblique wavelength λ/cos θ,
  empty window balance, `│C_empty│ ≤ 0.005` through the full incoherent
  pipeline, ±15° mirror symmetry, the Beer–Lambert slab absolute anchor, and
  the oblique closed-box energy identities.
- **stage 16** — `profile="gauss"` pointing chain (Block BEAM only).
- **stage 17** — `lab/glare_sidecar.py::c_thr`, the frozen threshold function
  §5's numbers are invoked from.

### 8.2 Is this new machinery? — the PANEL.md Phase-4 rule, engaged

**Position: no new machinery, therefore no new suite stage; instead two
pre-registered *absolute-identity* gates local to the experiment.** The
argument, and the counter-argument, both on the record:

- **Zero `lab/` diff.** `run.py` will assert `git diff --stat lab/` is empty
  before results are read. `absorb` is an existing, no-default-changed
  constructor argument of `Sim`, already exercised in this repo at **10, 20,
  30, 36 and 40** (grep: `lab/validation/run_all.py` uses 20/30/36/40 across
  stages 1–24; `experiments/016` uses 10). Nothing is added to the engine.
- **The padded domain is a re-parameterization, not new physics** — the exact
  shape exp-048 handled with a *local regression gate* rather than a new
  stage, on the house convention Red Team accepted there ("a
  re-parameterization of an already-committed desk propagator, reusing
  `lab.ambient` unmodified, is not new physics machinery").
- **Honest counter-argument, disclosed rather than waited for:** no
  trust-suite stage has *ever* varied `absorb` as a controlled variable — each
  stage pins one value. So this cycle is the first time the parameter is
  swept, and a reviewer could fairly call the sweep itself a new
  configuration class.
- **Therefore the two local gates are built to *absolute* standard, not to a
  tolerance**, which is what the Phase-4 rule actually demands:
  - **G-1 = P-VIS42-1**: 12 committed exp-041 rows reproduced by float64
    equality (Δ = 0.0), values loaded programmatically from
    `experiments/041-t20-angle-audit/results.json` — never re-typed.
  - **G-2 = P-VIS42-1b**: the padded-domain causal field identity,
    `max│ΔEz│ = 0.0` exactly over the scored windows at the causally derived
    step 359.
  Both are absolute identities, both are pre-registered here, and both gate
  every other number in the experiment.
- **If Red Team rules otherwise at Phase 2**, the minimal correct remedy is a
  new suite stage wrapping exactly G-2 (a padded-vs-unpadded vacuum identity
  at the causal step) plus a two-`absorb`-value empty-scene regression anchor;
  I will build it at Phase 3 rather than argue. I do not propose it now
  because I do not believe a stage should be added for a parameter the engine
  has always supported — but I state the fallback so the deferral cannot be
  read as an evasion.

### 8.3 House gates

- Predictions committed to git **before** `run.py`'s first execution
  (P-VIS42-1 … -9 verbatim in `NOTES.md`, structurally printed by `run.py`
  before any FDTD call — exp-046's own structural-freeze precedent).
- Evidence Gate on artifacts (`save_run`), per AGENTS.md.
- R3 meta-rule stands: any surprising feature gets a resolution check before a
  mechanism debate. **Not budgeted this cycle** — a cpl 20→30 companion at one
  cell is the named Iteration-43 follow-up if P-VIS42-2 lands near either
  band edge.
- R4/R5: every figure in this document is produced by
  `python3 design_geometry.py` (output committed as
  `design_geometry_output.txt`) or read programmatically from a committed
  `results.json`. The only figures transcribed from prose are T24's own
  published beam-channel numbers, which are transcribed **specifically in
  order to be tested** by P-VIS42-8, and are stored in `T24_BEAM` with their
  source line range.
- Iteration 41's new forward tripwire (`length_provenance` gate-4 evasion):
  **not applicable** — this cycle adds and edits **zero** guarded call sites;
  `lab/thermo_sidecar.py` is not imported anywhere in this experiment. Stated
  explicitly so the tripwire's "undetected" clause cannot later be read as
  silence.
- Bonnie's lanes untouched: no `absorber_shell_stub`, no `lab/viz.py`.
  `lab/ARTIFACTS.md`, `lab/artifacts.py`, `AGENTS.md` unmodified.

---

## 9. LOGBOOK read disclosure

**Read in full, this shift, with the Read tool:**
- `PANEL.md` — complete (199 lines).
- `LOGBOOK.md` **lines 1–1671** — complete: RULED OUT R1–R5, ESTABLISHED,
  LIVE THREADS T1–T26, PARKED, ITERATION TEMPLATE.
- `LOGBOOK.md` **Iteration 23** (8818–9074), **Iteration 24** (9074–9476),
  **Iteration 25** (9476–9690), **Iteration 26** (9690–9911) — complete.
- `LOGBOOK.md` **Iteration 41** (13117–13283) — complete.
- `LOGBOOK.md` **Iteration 19** (7883–8164) — complete (VISION-led).
- `LOGBOOK.md` **Iteration 1** lines 1674–1873 — the Phase-1 proposal in full
  (including §3, the frozen threshold table), all five Phase-2 critiques, Red
  Team's seven numbered attacks, and the Director's 9-item mandatory-fix
  docket. **Lines 1874–2036 (Iteration 1's Phase 3–5 record) NOT read** —
  the file's own line budget forced a split read; I read the half that
  contains the threshold provenance my charter duty needs.
- `PLAN.md` **lines 2195–2345** — the current top-of-queue ranked block and
  the two superseded blocks below it.

**Read partially / by targeted query, disclosed as such:**
- `LOGBOOK.md` **Iteration 7** (4136–4868), **Iteration 13** (6185–6481),
  **Iteration 33** (11151–11428) — VISION-led cycles I was directed to read
  in full. I read Iteration 33's header and headline (11151–11175) only, and
  did **not** read Iterations 7 and 13 at all. Mitigation, stated rather than
  glossed: their substance reaches this proposal through the LIVE THREADS
  section, which I read in full and which carries T11/T12/T13/T14 (Iteration
  7), T17/exp-036 (Iteration 13) and T26's Iteration-33 update verbatim. This
  is a real gap in my read and I flag it rather than let a Phase-2 seat find
  it.
- `LOGBOOK.md` Iterations 2–6, 8–18, 20–22, 27–32, 34–40 — **not read**;
  reached only through LIVE THREADS, PLAN.md, and targeted greps.
- `experiments/046-…/phase5_redteam_audit.md` — §7 (the T24 boundary table,
  lines 600–640) and §8/§9 (docket, lines 800–970) read directly; the rest by
  grep.

**Code read directly:** `lab/ambient.py` (complete), `lab/fdtd2d.py`
(complete), `lab/validation/run_all.py` stage 9 (534–690) and the `absorb=`
call-site census, `lab/glare_sidecar.py::c_thr`,
`experiments/041-…/design_geometry.py` (complete) and `run.py` (1–200),
`experiments/042-…/design_geometry.py` (geometry constants),
`experiments/046-…/run.py` (`ABSORB_SYSTEMATIC_NOTE` and `fdtd_leg`),
`experiments/048-…/design_geometry.py` (100–247, the generalized propagator).
`lab/sections.py` was **not** read in full — used only through
`full_capture`/`phasors`, already exercised bit-identically this shift.

**Ruled-out check.** Nothing here resurrects R1 (no refractive/TO cloak; no
real-Δε mechanism — no mechanism at all), R2 (no shell-thickness or
integer-λ claim), R3 (the meta-rule is *invoked*, and its non-budgeting is
disclosed in §8.3), R4/R5 (every figure code-produced; no `P`-normalized phase
offset appears — the periodicity cited in §2.4 is the **aperture** half-length
`A`, which is a geometric length, not R5's ruled-out difficulty regressor).

---

*Prepared by VISION SCIENCE, panel Iteration 42, Phase 1. Every number in this
document is reproducible by `python3 experiments/065-t24-absorb-boundary-sweep/design_geometry.py`.*
