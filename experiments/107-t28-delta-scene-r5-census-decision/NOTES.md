# exp-107 — Formally Retiring the `delta_scene` R3-vs-R4-vs-R5 Question, and Three `kappa_window` Tier-1 Closeouts

**Panel Iteration 84. Lead seat (rotation): VISION SCIENCE. Director:
Clyde (photonlab-shift, cloud panel shift).** Executes exp-106's own
Reconciled Iteration-84 queue: Tier 0 (governance — execute or formally
retire the `delta_scene` R3-vs-R4 split) and Tier 1 items 1/3/4 (the
`kappa_window` closeouts), per Red Team's own final tiered ranking
(`phase5_redteam_audit.md` §5 of exp-106). Two structurally independent
pieces of work, bundled for shared setup cost — they do not share a fate
and are scored separately.

Full record: `phase1_proposal.md` (VISION SCIENCE), `phase2_critique_
{photonics,materials,em,thermodynamics,quantum}.md` (five blind
critiques, all support-with-changes), `phase2_redteam_audit.md` (6
numbered attacks, all five critiques disposed — 4 ADOPTED in full, 2
core-finding-ADOPTED/remedy-OVERRIDDEN — verdict PROCEED-WITH-MANDATORY-
FIXES).

## Hypothesis

**Tier 0 (governance, no FDTD):** the `delta_scene` R3-vs-R4 resolution-
family disagreement (LOGBOOK, first framed exp-100 Iteration 77) has now
been deferred eight consecutive cycles (Iterations 77–84). exp-107's
Phase 1 proposed resolving it by executing a properly-powered R5 (cpl=50)
census, gated on a mandatory ground-truth-recovery check. **This
hypothesis does not survive Phase 2.** Five independent lines of
adversarial review (§Synthesis, below) show the census as designed
cannot execute (its own gate has an empty domain over any reasonably-
sized window of this periodic signal), that a repaired gate would not
deliver genuine ground truth even where it could run, and that — independent
of both — MATERIALS' own founding disposition memo (exp-100) already
proves no outcome of the question can ever change a realizability tier or
a constraint-1/2/3/4 verdict. The corrected hypothesis this cycle actually
tests: **the question can be formally retired today, at zero FDTD cost,
by citing already-committed program record — not by one more data point.**

**Tier 1 (kappa_window closeouts, real FDTD):** exp-106 left three gaps
open on the `kappa_window` r=78/156/312 bridge (Iteration 82/83's own
headline instrument). Hypothesis: each closes cleanly using either
already-persisted data (items 3, 4-as-corrected-below) or a small, cheap,
already-validated instrument (item 1) — none of the three is expected to
overturn exp-106's own `p3_trusted=False`/`shape_ratio_fixedabs_trusted=
False` structural ceiling at r=312 (unaffected by any of these items,
per exp-106's own audit), but each closes a real, previously-identified
gap independent of that ceiling.

## Phase 2 → Phase 3: synthesis of the debate

**Tier 0 — the case for retirement, cumulative across five independent
findings, all independently re-verified by Red Team from primitives
(`phase2_redteam_audit.md` §0, §1 Attacks 1–6):**

1. **[QUANTUM, ADOPTED in full]** Gate G0's `θ_anchor` selection rule (a
   candidate angle must sit `≥1.4°` from all four native-grid zero-
   crossings, 37.127°/38.590°/40.265°/41.461°) is **unsatisfiable over
   the proposed 36.0°–42.0° grid** — the four exclusion zones pairwise
   overlap and merge into one continuous forbidden band `[35.727°,
   42.861°]` that fully contains the grid. Zero of 31 candidate points
   clear the buffer. Red Team independently re-derived this bit-exact.
2. **[Red Team's own generalization, §0.2/Attack 2 — new, not in any
   blind critique]** This is not a window-placement accident: the `1.4°`
   buffer is itself close to half the `2.84–2.95°` period being tested,
   so extending the crossing lattice periodically shows the rule leaves
   only `0.04°–0.15°`-wide safe slivers recurring every period — narrower
   than the census's own `0.2°` grid step. No re-window or re-center of
   any grid at this density rescues a scientifically meaningful anchor.
3. **[Red Team's own extension of QUANTUM's proposed fix, §0.3/Attack 3]**
   Even granting QUANTUM's own proposed repair (redefine the rule to
   "maximize achievable margin"), the best point the grid can produce
   (`θ≈39.4°`, margin `0.81°`) lands inside the `39.0°–39.8°` neighborhood
   LOGBOOK's own record (exp-095, Iteration 72) already found, on real
   data, could not be made into a clean "robust, far-from-null" ground-
   truth control point without repeated correction — and the corrected
   choice there was only ever "less compromised," never clean.
4. **[EM, ADOPTED in full]** Gate G0, even where its domain is non-empty,
   is not a genuine ground-truth-recovery gate: its own selection clause
   requires choosing an angle where R3 and R4 *already agree*, so two of
   the three sign-equalities it "tests" are guaranteed by construction
   before any new data exists. All three resolution families additionally
   share the identical `ABSORB=40/PAD=40` construction and PML/truncation
   environment on a signal independently proven lossless-vacuum (`PAD`,
   Iteration 53/exp-076) — agreement there cannot distinguish real
   diffraction from a shared numerical residual, the exact failure R15's
   addendum was written to guard against.
5. **[MATERIALS, ADOPTED and elevated to the deciding argument]**
   `disposition_memo.md`'s own three-way outcome conditional is exhaustive
   and unconditional: *"Under NO branch of this memo's own per-outcome
   conditional does a genuine new realizability question ever open."*
   Every branch the census's own outcome table (R3-CORROBORATED / R4-
   CORROBORATED / NEITHER) could produce maps onto a branch this memo
   already closed, one cycle ago, at zero cost.

None of these five is individually dispositive (MATERIALS' economic
argument alone was already strong; QUANTUM's structural finding alone
might read as "patch the buffer and proceed") — together they leave no
version of "fix and run" that is both executable and worth executing.
**Director's ruling (adopting Red Team's Phase-2 recommendation in
full): Tier 0 is discharged by formal retirement, not redesign.**

**Corrected citation (PHOTONICS, ADOPTED in full; Attack 6).** The
Phase-1 proposal's own central risk-framing sentence ("`delta_scene` is
≈0.08–0.12× `C_thr_lab`, sub-threshold whichever family is right") cited
the wrong statistic — T16/R9's `amp_ratio` figure is for a *different*
measurement construction (exp-076/077's `PAIR_PAD`/`PAIR_ABSORB40` decor-
relation build), not `delta_scene`'s own raw peak. The directly on-point,
already-filed number (exp-100 NOTES.md, Tier-2 Leg A) is: **peak
`|delta_scene|=3.1495×10⁻³` at θ=39.2° against `C_thr_lab=0.005` is
63.0% of the bar**, a 5.25×–7.87× discrepancy from the proposal's cited
figure, independently reproduced by Red Team (`0.6299/0.12=5.25`,
`0.6299/0.08=7.87`). This does not reverse exp-100's own PASS verdict
(63% is still `<100%`), but the retirement text below states the
honest number, not the proposal's mistaken one.

**Scope of the retirement (precise, per MATERIALS' own stated flip
condition, Red Team-endorsed):** this closes the *resolution-family-
attribution* question — does R3 or R4 read `delta_scene` correctly, and
would a third point disambiguate — as **economically closed**, matching
this program's own Iteration-51 no-further-cycle precedent (a standing
item discharged by reasoned written retirement, not only by one more
data point). It does **not** foreclose T28's own larger, still-genuinely-
open mechanism question (the `~2.84–2.95°` periodicity's ultimate
physical origin remains unexplained on LOGBOOK's own record) and does
**not** touch any other standing T28 deferred item (the 750/450nm leg,
the `G40` full-width leg, the x-wall admittance refit, `PAD`-with-article
survival at other wavelengths) — all remain open, unaffected. The one
stated reopening condition: a future proposal that identifies a live
realizability question genuinely depending on which family is correct
would reopen it — none exists today (MATERIALS' own ceiling, §0.5 of the
audit, independently confirmed unconditional by Red Team).

**Governance bookkeeping (no live action, confirmed by all parties):**
R24 was already ratified at Iteration 83's own close (LOGBOOK RULED OUT
registry) — this cycle's queue phrasing ("ratify-or-reject disposition
already exercised for R24") is a bookkeeping confirmation, not a
re-opened question.

**Tier 1 — three `kappa_window` closeouts, PROCEED, with THERMODYNAMICS'
mandatory fix applied (Red Team ADOPTED in full, unconditionally):**

- **Item 3 (P5 thermal row).** THERMODYNAMICS found the Phase-1
  proposal's blanket "≥100×, matching every prior cycle" prediction hides
  a real per-cell number: the physically-correct `p_abs_w ∝
  σ_ext·σ_abs` proxy, applied to already-filed data, computes
  `(fixedabs, r=312)≈120×` — barely above the stated floor, not
  comparable to the other three cells' 267×–700× headroom. **Adopted as
  the pre-registered per-cell prediction below** (§Predictions), computed
  directly from exp-106's own already-persisted, real ledger-measured
  `sigma_ext`/`abs_ext_ratio` (NOT the Q_ext-invariance placeholder
  exp-105 used) — a genuine methodological improvement this cycle makes
  available for the first time, since exp-106 is the first cycle to have
  actually *measured* (not merely scaled) `sigma_ext(r)` for both
  families.
- **Item 1 (hollow-vs-PEC-cored `radial_absorbed_power` delta,
  fixed-abs family, r=156/312).** No Phase-2 defect found against the
  test's design (MATERIALS confirmed the ratios 0.692/0.846 do not
  extrapolate past the locked thickness-based UNOBTANIUM bound; the
  instrument itself, `sections.radial_absorbed_power`, is validated,
  suite stage 10). **Director's own cost correction (disclosed, R4-style,
  not silently accepted):** the Phase-1 proposal's "empty scenes reused
  from exp-106" is not literally executable — raw field arrays are never
  persisted across experiment directories (only scalar/summary fields
  survive in `results.json`), and `ledger_check()`'s own module docstring
  in exp-106's `run.py` says so explicitly: *"this is NOT a re-run of
  exp-052's own hollow-vs-PEC-cored delta methodology (that needs a
  third, new capture, a real cost, not mandatory this cycle)."* The
  correct accounting is **4 new `Sim.run()` calls** (empty+hollow-article
  at each of r=156, r=312), not 2 — extrapolated cost ≈100–130 min, not
  75–90 min (§Predictions, cost table). The PEC-cored comparator side of
  the delta is *not* re-run — it is exp-106's own already-committed,
  already-suite-gated `ledger_r156['fixedabs']`/`ledger_r312['fixedabs']`
  numbers, reused verbatim.
- **Item 4 (numerator noise-floor check), Director's own economical
  fold-in.** The proposal's plan to reuse "already-persisted
  `r312_selfsim`/`r156` raw arrays" is also not literally executable —
  those persisted arrays are the EMPTY-scene window channel only
  (`floor_gate_window()`'s own module docstring: *"called on the
  empty-scene reference only... the question is whether kappa_window's
  DENOMINATOR sits above the solver's own numerical noise floor"*); no
  ARTICLE-scene window array was ever persisted for any family. Rather
  than schedule a fifth/sixth new FDTD call, this cycle folds item 4 into
  item 1 at **zero additional FDTD cost**: `floor_gate_window()` is
  generic in which scene's `Ez` it receives, so it is called on the SAME
  new hollow-fixedabs article captures item 1 already produces, at both
  r. This is disclosed explicitly as a substitution, not silently
  presented as testing the PEC-cored primary article `kappa_window`'s own
  numerator — the physical scene is different (hollow, not PEC-cored),
  though the question being asked (does the solver's own numerical noise
  floor contaminate the article-scene window reading at all) is not
  expected to depend materially on that difference at these SNR levels
  (both scenes attenuate through the same shell; neither the hollow core
  nor a PEC core meaningfully re-radiates power back into the window).

## Setup

**Item 1 (real FDTD, ≈100–130 min wall, cost-gated).** Fixed-abs family
geometry (`geom_fixedabs(r)`, re-derived locally in `run.py` byte-for-byte
from exp-106's own formula chain — `ABS_THICKNESS=48` cells fixed,
`SIGMA_MAX_FIXED=0.5` fixed, domain construction identical to the
self-similar family at the same r) at r=156 (`R_CORE=108`) and r=312
(`R_CORE=264`). Build: `materials.graded_black_shell(CX,CY,R_CORE,R_COAT,
sigma_max)` **only** — no `materials.pec_disk()` call, so the interior
(r<R_CORE) stays vacuum (hollow), the exact construction difference T9's
original test (exp-027/031) used. Gate: recompute `geom_fixedabs(156)`/
`geom_fixedabs(312)` locally and assert every field matches exp-106's own
committed `geom_156_fixedabs`/`geom_312_fixedabs` exactly (a Gate-P0-style
ground-truth reproduction check) BEFORE any new `Sim.run()` call — if this
assertion fails, HALT before spending any FDTD budget. Metrics:
`sections.widths()` → `sigma_abs`/`sigma_ext`/`abs_ext_ratio` (box_a/box_b
cross-checked for box-independence, established `≤0.12` band);
`sections.radial_absorbed_power()` → `core_frac`/`core_power` sanity
(hollow core should show `core_power≈0`, matching `graded_black_shell`'s
own r<R_CORE-untouched convention — a different mechanism than PEC's
Ez=0 clamp, same near-zero numerical outcome expected). Cost gate: pilot
r=156 first (cheap, ≈6–12 min combined); if the observed per-call rate
scaled to r=312 projects total item-1 wall time beyond **150 min**,
abort the r=312 leg and report r=156-only (disclosed reduction, not a
silent drop), matching exp-105/106's own pilot-and-abort precedent.

**Item 3 (desk-only, zero marginal FDTD).** For each (family, r) in
{(selfsim,156), (fixedabs,156), (selfsim,312), (fixedabs,312)}: read
`sigma_ext`/`abs_ext_ratio` directly from exp-106's own committed
`ledger_r156`/`ledger_r312` (real measured values, not a scaled
placeholder). Held-fixed physical anchor (exp-057's established citation,
reused verbatim, unchanged by this cycle): `SIGMA_EXT_78=
240.0073740162445`, `P_ABS_78=1.7409069740390205e-12`,
`RATIO_ABS_EXT_78=0.51` → `i_incident = (P_ABS_78/RATIO_ABS_EXT_78) /
(width_m_78² · 1e4)` where `width_m_78 = SIGMA_EXT_78 · DX_M`,
`DX_M=30.0e-9`. Per (family,r): `width_m = sigma_ext_real · DX_M`,
`p_abs_w = i_incident · width_m² · 1e4 · abs_ext_ratio_real`,
`l_geometric_m = r · DX_M`, then
`thermo_sidecar.mixed_length_scale_regime(p_abs_w, l_geometric_m,
K_AIR=0.026, DENSITY_SI=2330.0, C_P_SI=700.0, EMISSIVITY=0.9,
T_AMBIENT_K=293.15, length_provenance="bench_construction")` →
`dt_ss_full_K`; `margin = NETD_BAND_K[0]/dt_ss` (`NETD_BAND_K=(0.020,
0.050)`); classification via `thermo_sidecar.netd_disposition(dt_ss,
NETD_BAND_K)`. **R21 commitment (THERMODYNAMICS' mandatory fix): the
headline number for each cell is narrated in this document's own Result
section below, not merely persisted in `results.json`** — this channel
already carries two non-firing R21 founding instances (exp-099, exp-100);
a third silent non-narration fires Checkpoint criterion 4 automatically.

**Item 4 (folded into item 1, zero additional FDTD).** `floor_gate_window
(ez_hollow_article, *g["behind"], label)` at r=156 and r=312, reusing the
identical `FLOOR_FRAC=0.10` convention and `g["behind"]` window box
exp-106 used for the empty-scene denominator check.

## Predictions — committed BEFORE any Phase 4 `Sim.run()` call

**Item 1 (genuine physical uncertainty — a new measurement):**

| Quantity | r | Predicted band | Falsified if |
|---|---|---|---|
| `\|Δ(abs_ext_ratio)\|` = `\|abs_ext_ratio_hollow − abs_ext_ratio_PECcored(exp-106)\|` | 156 | `≤2×10⁻⁵` (T9-established near-zero order: exp-027 `+1.56×10⁻⁶`, exp-031 `6.8×10⁻⁶`) | `>2×10⁻⁴` (10× the established near-zero band) |
| same | 312 | `≤2×10⁻⁵` | `>2×10⁻⁴` |
| `core_power` (hollow) | both | `≈0` (matches `graded_black_shell`'s own r<R_CORE-untouched convention) | `core_frac>0.01` |
| `box_dev` (box_a vs box_b) | both | `≤0.12` (established band) | `>0.12` |
| Item-1 cost gate | — | r=156 pilot ≤20 min; total (both r) ≤150 min | pilot alone exceeds 150 min run-rate projection → abort r=312, report r=156-only |

**Item 3 (deterministic post-processing of already-committed data — a
reproducibility check, not a physical-uncertainty prediction; computed
here with the exact formula chain `run.py` will execute, tolerance
±0.5% for floating-point path differences only):**

| Family | r | `sigma_ext` (real, exp-106) | Predicted `dt_ss_K` | Predicted margin | Classification |
|---|---|---|---|---|---|
| selfsim | 156 | 480.6881 | 5.824×10⁻⁵ | **343.4×** | UNDETECTABLE |
| fixedabs | 156 | 560.1989 | 7.623×10⁻⁵ | **262.4×** | UNDETECTABLE |
| selfsim | 312 | 960.4456 | 1.164×10⁻⁴ | **171.9×** | UNDETECTABLE |
| fixedabs | 312 | 1191.3259 | 1.703×10⁻⁴ | **117.5×** (THERMODYNAMICS' named **fragile cell**) | UNDETECTABLE |

Falsified (per THERMODYNAMICS' mandatory tightened band, replacing the
Phase-1 proposal's own too-loose `<10×` band) if: any cell classifies
DETECTABLE, **or** `(fixedabs, r=312)`'s margin computes below **50×**
(would catch a further order-of-magnitude erosion this program's own
`<10×` band could not), **or** any cell's computed value misses this
table's own value by more than the stated ±0.5% floating-point
tolerance (would mean `run.py`'s implementation does not match this
document's own pre-registered formula chain — an R4 violation, not a
physics finding).

**Item 4:**

| r | Predicted | Falsified if |
|---|---|---|
| 156 | `frac_unresolved=0.0` (mirrors item 1's own clean empty-scene result, exp-106) | `frac_unresolved>0.10` |
| 312 | **genuinely uncertain** — PHOTONICS flagged a `~200,000×` article-scene collapse at r=312 in exp-106's own Phase-5 review; this is an open question, not a foregone conclusion | (informative either way; scored descriptively) |

## Idealizations

- 2D TMz, λ=600nm only — unchanged program-wide scope.
- Item 1's fixed-abs hollow construction is a single-variable factorial
  (core fill only); it does not re-test box-independence at a third box
  family — it reuses exp-106's own already-validated `box_a`/`box_b`.
- Item 4's numerator floor-gate is measured on the HOLLOW article, not
  the PEC-cored primary article `kappa_window`'s shape_ratio was scored
  from — disclosed substitution (§Synthesis), not claimed identical.
- Item 3 is a deterministic recomputation from already-public,
  already-suite-gated data; its "prediction" is a reproducibility gate on
  `run.py`'s own implementation, not a physical-uncertainty forecast.
- The thermal sidecar chain (`mixed_length_scale_regime`) carries its own
  standing idealizations unchanged (100%-fill crystalline solid mass
  assumption, ASSUMED material provenance — see `REALIZABILITY_MEMO.md`
  and exp-054's own NOTES.md) — not re-litigated this cycle.
- Retirement of the `delta_scene` R3-vs-R4-vs-R5 attribution question is
  scoped precisely (§Synthesis) — it does not foreclose T28's larger,
  still-open mechanism question or any other standing T28 deferred item.
- `DISCLAIMER` text (exp-105/106's own standing perceptual/expressibility
  disclaimer, R23 code-enforced) applies unchanged: raw physical intensity
  ratios and an absorbed-power sanity ledger only — no Weber-contrast or
  `C_thr(L)` perceptual scoring is performed by items 1/3/4 this cycle;
  NETD is an instrument/detector threshold, not a human perceptual one.

## T1 escape-route statement

**N/A.** Instrument-extension/governance cycle — no σ(I)/σ(x,t)/angular-
selectivity/sub-threshold mechanism is built, varied, or claimed anywhere
in this document. Constraint-3 is not engaged by any branch of this
cycle (confirmed independently by Red Team, `phase2_redteam_audit.md`
§1, "No constraint-#N-violation found").

## Result

**Execution-methodology note (disclosed, does not change any predicted
band or gate above).** This session's own backgrounded/nohup process
execution was found, mid-cycle, to run this FDTD workload pathologically
slowly (isolated A/B test: foreground execution reproduces exp-106's own
historical per-step rate; the identical code launched in the background
accrued CPU time at ~1/10–1/20 that rate over a >90-minute wall-clock
window with zero completed output, then was killed — a pure CPU-bound
Python loop was NOT similarly slowed in the background, isolating this
to the sustained large-array numpy FDTD workload specifically; the trust
suite, run directly foreground, was green in 104s at this shift's start,
confirming an environment/tooling characteristic of this remote session,
not a `lab/` engine defect). Items 1/4 were executed via sequential
foreground Bash calls with Sim-object checkpoint/resume pickling
(`chunk_runner.py`, 2200-step chunks, 6 per scene at r=312) and
`finalize.py` (the identical formulas `run.py`'s own `item1_and_4_one_r()`
specifies) — independently re-run to confirm bit-exact reproduction of
every number below before this note was written. **4 real new `Sim.run()`
calls** (empty+hollow-article at r=156, r=312), as corrected in
§Synthesis (not the Phase-1 proposal's original miscount of 2). Gate P0
and Item 3 ran exactly as designed, in-process — no substitution needed.

**Gate P0 (ground-truth reproduction): PASS, exact, both r.** Locally
re-derived `geom_fixedabs(156)`/`geom_fixedabs(312)` matched exp-106's
own committed `geom_156_fixedabs`/`geom_312_fixedabs` on every shared
field, bit-exact.

**Item 3 (real, non-placeholder P5 thermal row): CONFIRMED, all four
cells reproduce the pre-registered table to full floating-point
precision** (deterministic recomputation, as expected — this item is a
reproducibility gate on `run.py`'s own implementation, not a physical-
uncertainty test, per §Predictions). **R21 narration, honored here, not
merely persisted:**

| Family | r | `dt_ss_K` | Margin | Classification |
|---|---|---|---|---|
| selfsim | 156 | 5.824×10⁻⁵ | **343.4×** | UNDETECTABLE |
| fixedabs | 156 | 7.623×10⁻⁵ | **262.4×** | UNDETECTABLE |
| selfsim | 312 | 1.164×10⁻⁴ | **171.9×** | UNDETECTABLE |
| fixedabs | 312 | 1.703×10⁻⁴ | **117.5×** | UNDETECTABLE (fragile cell, as named — 20% above the 100× naive floor, but clears the tightened 50× falsification bar with margin to spare) |

**Item 1 (hollow-vs-PEC-cored `radial_absorbed_power`/`sections.widths()`
delta): PASSES the falsification band at both r, but does NOT reach the
tighter "confirms" band — an honest partial, not a clean reproduction of
the T9-established anchor magnitude.**

| r | `abs_ext_ratio` hollow | `abs_ext_ratio` PEC-cored (exp-106) | `\|Δ\|` | vs. `≤2×10⁻⁵` (confirms) | vs. `≤2×10⁻⁴` (falsifies) | `core_frac` (hollow) | `box_dev` |
|---|---|---|---|---|---|---|---|
| 156 | 0.4991871 | 0.4992168 | **2.969×10⁻⁵** | fails (1.48×) | **PASS** | 8.65×10⁻⁷ | 0.00071 |
| 312 | 0.4935614 | 0.4935861 | **2.468×10⁻⁵** | fails (1.23×) | **PASS** | 2.88×10⁻⁷ | 0.00022 |

T9's own "core is energetically incidental" null generalizes to the
fixed-abs family's much higher `R_CORE/R_COAT` ratios (0.692 at r=156,
0.846 at r=312, past T9's only-previously-validated 0.385) — both deltas
clear the 10× falsification margin comfortably, and `core_frac` confirms
the hollow core itself carries a genuinely negligible share of absorbed
power at both r (order 10⁻⁷, consistent with `graded_black_shell`'s own
r<R_CORE-untouched convention). **Honestly flagged, not smoothed over:**
both deltas sit at roughly an order of magnitude above the original T9
anchors (exp-027: `+1.56×10⁻⁶`; exp-031: `6.8×10⁻⁶`) — same near-zero
order of magnitude, same qualitative conclusion (core-presence stays
energetically incidental), but this is a PASS at the loose band, not a
tight reproduction of the historical anchor scale. Red Team's founding
Attack 9 concern (core-reflection leakage driving fixed-abs's own falling
`abs_ext_ratio`) is discharged at both r: the hollow-vs-PEC-cored delta
is two-to-three orders of magnitude smaller than the `abs_ext_ratio`
values themselves (~0.49–0.50), too small to explain that trend.

**Item 4 (numerator noise-floor check): FALSIFIED at r=156, informative
at r=312 — a genuine, previously undetected finding, not a foregone
conclusion.**

| r | `frac_unresolved` (article numerator, hollow) | Predicted | Outcome |
|---|---|---|---|
| 156 | **0.18275** (731/4000 cells) | `≤0.10` (clean, mirroring the empty-scene denominator) | **FALSIFIED** — the article-scene numerator is NOT clean at r=156, unlike the empty-scene denominator exp-106's own Item 1 tested |
| 312 | **0.2675** (1070/4000 cells) | genuinely uncertain (PHOTONICS' own ~200,000× collapse flag) | Informative: contamination is real and WORSENS with r (18.3%→26.8%) |

This is this cycle's single most consequential finding, and it was not
anticipated by either the Phase-1 proposal or any Phase-2 critique:
exp-106's own Item 1 floor-gated only the EMPTY-scene window (the
`kappa_window` denominator) and found it clean at both r
(`frac_unresolved=0.0`) — but the ARTICLE-scene window (the numerator)
was never checked, and turns out to carry substantial noise-floor
contamination at BOTH r, worsening with r. **Scope caveat, stated
plainly (per NOTES.md Idealizations, above): this was measured on the
HOLLOW fixed-abs article, not the PEC-cored primary article
`kappa_window`'s own P2/P3 shape_ratio was scored from** — the physical
scene differs, so this result does not directly overturn P2/P3's own
trust status. It DOES mean the open question PHOTONICS flagged at
exp-106's own Phase 5 (a possible noise-floor component in P3's headline
"accelerating collapse") is real and worth checking directly on the
PEC-cored primary article next cycle, not merely plausible.

**Combined Verdict: PARTIAL.** Tier 0 is a clean governance win — the
`delta_scene` R3-vs-R4-vs-R5 question is formally retired, discharging
an eight-cycle-deferred standing obligation with a reasoned, cited,
zero-FDTD-cost written decision, not a silent ninth deferral. Tier 1 is
genuinely mixed: Item 3 CONFIRMED cleanly (a real methodological
improvement — real ledger-measured `sigma_ext(r)`, not a placeholder,
used for the first time); Item 1 PASSES but only at the loose band, an
honest partial; Item 4 FALSIFIED its own r=156 prediction and surfaced a
new, real, actionable gap in `kappa_window`'s own trust chain. No
mechanism proposed or varied; T1 correctly N/A throughout; constraint-3
not engaged.

## Next — candidate Iteration 85 directions (Director's own ranking,
pending Phase 5's ranked top-3)

1. **Check the numerator noise-floor on the PEC-cored PRIMARY article**
   (self-similar and fixed-abs, r=156/312) — item 4's own hollow-variant
   substitution should be closed with the real measurement P2/P3's
   shape_ratio was actually scored from. Low marginal cost if a captured-
   field checkpoint from a future r=156/312 primary re-run is saved.
2. **Widen Item 1's own "confirms" band, or re-derive it from a real
   R17-style cross-check**, rather than leaving both r sitting just
   outside a band nobody re-justified for these specific ratios (0.692,
   0.846) — the current `≤2×10⁻⁵` figure is inherited from T9's original
   two-anchor spread, not independently derived for this construction.
3. Standing T28 items unchanged from exp-106's own Tier 2/3 (a
   genuinely different bridge-family geometry; a fourth r-point; the
   oblique-angle extension; the near-null-exclusion refinement) — none
   touched this cycle.
