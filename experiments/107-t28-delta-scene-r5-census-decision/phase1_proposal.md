# PHASE 1 — PROPOSAL · Panel Iteration 84 (candidate exp-107)
## Lead seat: VISION SCIENCE (rotation lead)
## "The Properly-Powered R5 Census, a Ground-Truth Recovery Gate, and Three Zero/Low-Marginal-Cost `kappa_window` Closeouts"

### 0. What kind of cycle this is

This is an **instrument-extension / governance cycle, not a new mechanism
proposal** — matching exp-101/104/106's own precedent. **T1 escape route:
N/A.** No σ(I)/σ(x,t)/angular-selectivity machinery is built or varied;
no new material is proposed. The two things this cycle changes are (a)
whether the `delta_scene` R3-vs-R4 resolution disagreement gets a properly-
powered third data point or gets formally retired, and (b) three already-
scoped, low/zero-marginal-cost closeouts on the unrelated `kappa_window`
r-family bridge left open by exp-106.

### 1. Narrative (≤300 words)

Tier 0 is a governance call, not a VISION SCIENCE call, and I say so
plainly: whether `delta_scene`'s ~2.84–2.95° periodicity is genuine
PAD-diffraction physics (R3's reading) or a resolution-family artifact
(R4's reading) is PHOTONICS'/MATERIALS' mechanism-attribution question,
and whether it is worth further FDTD spend is Red Team's governance
question — my charter (perceptual thresholds) does not adjudicate either.
What I *can* certify, and do: **this split cannot change any constraint-3
verdict I own.** `delta_scene`'s established magnitude, R9-corrected, is
≈0.08–0.12× VISION's own pinned lab bar `C_thr=0.005` (LOGBOOK T16) —
sub-threshold whichever family is right. MATERIALS' own disposition memo
(exp-100) proves a second, independent ceiling: no branch of the R3/R4/R5
question ever opens a new realizability question — at best it re-attributes
an already-published, already-measured structure's own diffraction.

Given that, my recommendation as rotation lead is procedural, not
substantive: **execute** a single-provenance, properly-powered R5 census
(n=31, matching R3/R4 density) rather than retire the question outright
this cycle, because Red Team's own text forecloses a silent eighth
deferral and a scoped-but-unrun plan does not discharge that mandate — but
I build in the exact off-ramp MATERIALS/PHOTONICS need: a mandatory
ground-truth-recovery gate (R15 addendum's own text) that must PASS before
R5's correlation reading counts as a tiebreaker at all, and an explicit
three-way outcome table whose "neither" branch is a **pre-committed formal
retirement**, not another open question. If Phase 2's MATERIALS/PHOTONICS
seats judge the ceiling makes even this bounded spend not worth it, that is
their call to override at Phase 2 — I name the process, not the verdict.

Bundled at zero/low marginal cost: three exp-106 Tier-1 closeouts sharing
no machinery with the census (separate proposal §5).

### 2. Parameter table — the R5 census

| Knob | Value | Source / formula |
|---|---|---|
| Config pair | `C40` (ABSORB=40,PAD=0), `G40` (ABSORB=40,PAD=40) | `experiments/065-t24-absorb-boundary-sweep/design_geometry.py::CONFIGS` — the identical pair `delta_scene≡c_g−c_c` is defined from throughout T28 (confirmed in `experiments/091-.../run.py:441`) |
| λ / native cpl | 600 nm / cpl=20 | `CPL={450:15,600:20,750:25}`, dg065 |
| Resolution ratio | `R5_RATIO = 50/20 = 2.5` | generalizes `R3_RATIO=1.5`→`R3_R_OUT=117`, `R4_RATIO=2.0`→`R4_R_OUT=156` (both `dg.R3_R_OUT`/exp-094 precedent) by the SAME rule |
| `R_OUT` (R5) | `round(78·2.5) = 195` (illustrative — Phase 3 must derive via the actual `_rescaled_geom(2.5)`-style function, not hand-typed, per R4) | scales `R_OUT=78` (dg065) by `R5_RATIO` |
| `TAPER`, `NX`, `NY`, `STEPS`, all other lengths | scale by `R5_RATIO` from `dg065`'s `BASE_*`/`TAPER=40` fields, identical rule already used for R3/R4 | `dg065.geometry()`/its R3/R4 generalizations |
| Angle grid | **θ ∈ [36.0°, 42.0°], 0.2° step, n=31** — reproduces exp-069's own original Block MINI grid exactly (`experiments/069-.../` Iteration 46), not a patchwork | chosen deliberately: R3 (n=33) and R4 (n=35) are each *pooled across several experiments' differently-scoped sub-windows* (exp-091/094/098/099/100 for R3; exp-094/098/099/100 for R4) — a genuine, disclosed design improvement, not merely density-matching |
| Settling precondition | STEPS doubled at 2 angles (grid ends, 36.0°/42.0°), both configs, `STABILITY_TOL=0.20` | exp-069/exp-103's own established settling-leg convention |
| Ground-truth anchor `θ_anchor` | the θ *within this 31-point grid* with (a) largest pooled \|`delta_scene`\| where R3 **and** R4 already agree in sign, AND (b) ≥1.4° (half the established 2.84–2.95° period) from every native-grid zero-crossing (37.127°/38.590°/40.265°/41.461°, exp-083, LOGBOOK) | R15 addendum's own text, operationalized as a pre-registered selection rule computed from already-filed data, not hand-picked |
| Null-permutation control | 20,000 trials, identical methodology to `disposition_memo.md`'s own pooled/per-family test | exp-100 precedent |
| Cost gate | pilot the first empty-scene call; abort/replan (fall back to a 16-point half-density grid, disclosed as reduced-power) if projected total exceeds 6h wall | exp-105/106's own pilot-and-abort precedent |
| **Estimated cost** | ≈62 primary calls (31×2 configs) + 4 settling calls = **66 calls**, ≈**3.3–4.0h wall** (extrapolated from exp-094's own measured cpl=40 rate, ≈95s/call, scaled ×(2.5/2.0)³≈1.95 for cpl=50 — an *estimate from a stated scaling law*, not a precisely-recomputed figure; the cost gate above bounds the downside) | exp-094 NOTES.md (3033.7s/32 calls); cost-scaling assumption: cells∝ratio², steps∝ratio ⇒ cost∝ratio³ |

### 3. T1 escape-route statement

**N/A.** Diagnostic/governance work only — identical scope statement to
exp-101/102/103/104/105/106.

### 4. Predictions — falsifiable, numeric, gated in order

**Gate G0 (MANDATORY, R15 addendum's own text — must PASS before ANY
correlation reading below counts as evidence):**
`sign(delta_scene_R5(θ_anchor)) == sign(delta_scene_R3(θ_anchor)) ==
sign(delta_scene_R4(θ_anchor))` **AND**
`|delta_scene_R5(θ_anchor)| / mean(|delta_scene_R3(θ_anchor)|,
|delta_scene_R4(θ_anchor)|) ∈ [0.5, 2.0]`.
— **FAIL → HALT**: the census is reported as a genuinely new, standalone
finding (a third mutually-disagreeing resolution family) and escalated to
Red Team; no R3-vs-R4 adjudication is drawn from it this cycle.

**Given G0 PASSES, the correlation test** (joint rule identical to
`disposition_memo.md`: `coupling_detected` iff `p<0.05 AND |r|≥0.20`,
20,000-trial permutation):

| Outcome | Numeric band on R5's own `(r,p)` | Reading |
|---|---|---|
| R3-CORROBORATED | `r∈[0.35,1.0]`, `p<0.05` (matches R3's 0.486/0.004) | R4 (n=35) is the likely under-resolved/artifact family; R3's reading governs future citations |
| R4-CORROBORATED | `r∈[−0.20,0.20]`, `p>0.10` (matches R4's 0.110/0.525) | R3 (n=33) is the likely artifact; R4's reading governs |
| **NEITHER (formal retirement trigger)** | any other `(r,p)` combination, or R5 itself unstable under its own settling/G0 checks | Per R15 addendum's own text ("neither resolution's reading is individually trustworthy... a genuinely non-convergent oscillation" is an admissible outcome) combined with `disposition_memo.md`'s own "ceiling" finding (no branch ever opens new realizability content) — **this branch is a pre-committed formal retirement of the R3-vs-R4-vs-R5 question as economically closed**, not a further-deferred open item. Constraint-3 scoring is unaffected either way (§1). |

Secondary, descriptive only (not gated): does R5's own zero-crossing count/
location pattern track R3's, R4's, or neither, using the identical
linear-interpolation method exp-083 used.

### 5. Bundled zero/low-marginal-cost Tier-1 items (exp-106's own queue)

Included — share no machinery with the census, cost disclosed separately:

- **Item 3, P5 thermal row (zero marginal FDTD)**: `thermo_sidecar.
  netd_disposition()` applied to both families' already-persisted
  `sigma_ext`/`sigma_abs` at r=156/312 from exp-106's own `results.json`.
  Prediction: UNDETECTABLE at all 4 (family,r) cells, ≥100× margin,
  matching every prior T28-bridge cycle. Falsified by any cell reading
  DETECTABLE or margin <10×.
- **Item 4, numerator noise-floor check (zero marginal FDTD)**:
  `floor_gate()`'s own convention (`FLOOR_FRAC=0.10`) applied to the
  ARTICLE-scene window mean (not merely the empty-scene denominator
  exp-106's item 1 tested), reusing exp-106's own persisted
  `r312_selfsim`/`r156` raw arrays. Prediction: PASS at r=156 (mirrors
  item 1's own clean result); genuinely uncertain at r=312 given the
  ~200,000× article-scene collapse PHOTONICS flagged — a real open
  question, not a foregone conclusion. Falsified (in the informative
  direction) if `frac_unresolved>0.10` at r=312, meaning P3's own
  "accelerating collapse" headline partly reflects the solver's noise
  floor, not physics.
- **Item 1, hollow-vs-PEC-cored `radial_absorbed_power` delta on the
  fixed-abs family, r=156/312 (modest new FDTD — 2 new article-scene
  calls, empty scenes reused from exp-106)**: mirrors exp-027's original
  T9 test. Prediction: `|Δ(sigma_abs/sigma_ext)|` between hollow and
  PEC-cored fixed-abs stays at the same near-zero order of magnitude as
  T9's established anchors (exp-027: +1.56×10⁻⁶; exp-031: 6.8×10⁻⁶),
  i.e. `≤2×10⁻⁵`, even at these higher `R_CORE/R_COAT` ratios
  (0.692/0.846, past T9's only-validated 0.385). Falsified if
  `|Δ|>2×10⁻⁴` (10× the established near-zero band) — would mean
  core-presence is NOT energetically incidental at these ratios, and
  Red Team's founding Attack 9 concern (core-reflection leakage driving
  fixed-abs's own falling `abs_ext_ratio`) is real, not merely
  disclosed. Estimated cost: ≈75–90 min (r=156 article call ~15 min,
  r=312 article call ~60 min, extrapolated from exp-105/106's own r=312
  per-call timings).

**Deferred, with reason**: exp-106's own Tier-1 item 2 (complete the
r=312 settling leg on `kappa_window`). Its own empty-scene pilot already
blew the 90-min abort gate once (103.28 min) *before either article call
would have run*; re-attempting it without a design change risks a second
aborted leg on top of this cycle's own disclosed ≈4.5–5.5h combined budget
(R5 census + item 1). §0.2 of exp-106's own audit already confirms this
leg can never move `p3_trusted` to True at r=312 regardless of its
outcome — diagnostically valuable, not blocking. Sequencing it into
Iteration 85, once this cycle's two committed spends land cleanly, is the
honest call, not a silent drop (explicitly bound forward here).

### 6. Idealizations

- 2D TMz, λ=600nm only (both the census and the bundled items) — unchanged
  program-wide scope.
- The R5 census's own geometry constants above are illustrative (hand-
  derived from the stated `RATIO` rule for THIS proposal's own cost/
  parameter-table purposes); Phase 3 must compute them from an actual
  committed function before freezing, per R4/R20.
- `θ_anchor`'s literal value is NOT pre-committed in this document — the
  SELECTION RULE is (§2), evaluated against already-filed R3/R4 data at
  Phase 3, before any FDTD call, so the anchor cannot be chosen
  post-hoc from R5's own new data.
- The cost estimate (§2) is a scaling-law extrapolation, disclosed as
  such, bounded by a hard pilot-and-abort gate, not a precise
  pre-computed figure.
- Item 1's fixed-abs hollow construction is a single-variable factorial
  (core fill only) — it does not re-test box-independence at a third
  box family; it reuses exp-106's own already-validated `box_a`/`box_b`.
- **R24 governance note**: R24 was already ratified by the Director at
  Iteration 83's own close (LOGBOOK RULED OUT registry, full text
  present) — this cycle has no live ratify-or-reject action to take on
  it; the Tier-0 queue's own phrasing is a bookkeeping confirmation, not
  a re-opened question. Noted here so Phase 2 does not spend cycles
  re-litigating an already-closed governance item.
- Whichever way the R3-vs-R4-vs-R5 census resolves, no constraint-1/2/3/4
  verdict on file changes — this is a resolution-family/instrument-trust
  question, not a phenomenon-reproduction one.

### 7. What would falsify this cycle's own framing, and what Red Team
should look for

- **If MATERIALS/PHOTONICS' Phase-2 critiques argue the ceiling (§1)
  makes even this bounded, gated spend not worth it**, that is a valid
  override — Red Team should weigh a formal retirement-without-a-census
  case on its merits, not treat "VISION proposed executing" as binding.
- **If the G0 ground-truth gate cannot be satisfied by any angle in the
  chosen grid** (i.e., no angle simultaneously has R3/R4 agreement AND
  clears the 1.4° null-exclusion buffer), the whole census design is
  broken before Phase 4 — Red Team should check this against the actual
  pooled data BEFORE freezing, not discover it at Phase 4.
- **If the cost estimate is off by more than the stated scaling law's own
  honest uncertainty** (e.g., cpl=50's STEPS requirement turns out
  super-linear in ratio, not linear), the pilot-and-abort gate is the
  safety net — Red Team should confirm it is wired to fire BEFORE the
  62-call primary sweep commits, not only before the whole cycle starts.
- **If the "NEITHER" retirement branch fires**, Red Team should confirm
  the retirement text is written into LOGBOOK as a closed question, not
  as yet another "queued for next cycle" item — that would repeat this
  exact deferral pattern one level up.
