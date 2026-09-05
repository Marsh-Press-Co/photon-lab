# exp-112 — Panel Iteration 89 (candidate)

**Lead seat: QUANTUM OPTICS (rotation lead, PHOTONICS→MATERIALS→
ELECTROMAGNETISM→THERMODYNAMICS→QUANTUM OPTICS→VISION SCIENCE).**
Governance/instrumentation cycle continuing the T28 sub-thread. Executes
the Reconciled Iteration-89 queue's own headline Tier-1 item (LOGBOOK.md
Iteration 88 / `experiments/111-t28-cost-gate-reposition-and-floor-
fault-injection/phase5_redteam_audit.md` §8, quoted verbatim in PLAN.md
Current-state): **PHOTONICS' own independent, non-differencing floor
check (a `cpl`-refinement spot check) at the two named bins, protected by
this cycle's own repositioned, safety-margined cost gate — `cpl=25`,
r=156-alone-first — deferred twice now, executed here for the first
time.** Tier-0 item 0 (ruling on the Iteration-85 Checkpoint-4/R24 firing)
and Tier-0 item 0b (ratifying the R23 First Addendum) are Marsh's call,
explicitly out of scope, not attempted.

## 1. Mechanism/execution narrative (≤300 words)

Execute the twice-deferred spot check: a genuine, single new-physics FDTD
leg testing whether the **−146.25° bin** (r=156, margin=32/`box_a`, bin
index 4 of 48) — which sits **below even this thread's own K=1
mirror-pooled floor** at the established `cpl=20` resolution
(`local_snr_peccored=0.0965`, `local_snr_hollow=0.1061`;
UNRESOLVED-BY-CONSTRUCTION, exp-110's own committed `results.json`) yet
reads a superficially large **~9.88%** local fractional deviation between
the hollow and PEC-cored angular-scattering patterns — reflects genuine,
deterministic sub-wavelength field structure the boundary-condition
difference (PEC core vs. hollow) imprints on the scattered field, or is
itself an artifact of representing a curved shell boundary on a fixed
Cartesian Yee grid at `cpl=20`.

This is QUANTUM OPTICS' own stake, not a borrowed one: distinguishing a
genuine deterministic near-field signature from instrument/quantization
noise at a detection floor is exactly this seat's charter question —
"what counts as a genuine signal vs. instrument artifact at/near a
detection floor" — independent of whether the underlying physics is
classical or quantum. **Nothing in this document proposes, varies, or
requires any σ(I)/σ(x,t)/coherent-state/non-classical-absorption
content**; "coherent" here means spatially deterministic classical field
structure, not quantum coherence, and this seat's own expressibility
contract (mechanisms enter the bench only as effective classical
parameters, or Red Team strikes them) is trivially satisfied by there
being no mechanism at all in this document.

The instrument is a genuine, **congruent** grid-resolution refinement
(`cpl` 20→25, ratio 1.25×) of the IDENTICAL fixedabs geometry
(empty/hollow/PEC-cored, r=156 only this cycle), reusing every existing
classification function (`mirror_pooled_floor`, `classify_item_i_local`)
unmodified, so the SAME K=3 floor instrument reads the SAME named bin at
finer resolution: if the bin's own individual magnitudes shrink in
lock-step with the floor, the reading is noise; if the signal stays put
(or moves toward RESOLVED) while the floor itself shrinks, that is
evidence of real structure.

## 2. Parameter table

### 2.0 Grounding-fact verification (independently re-derived this session, before proposing anything — R4 discipline)

| Claim | Checked | Result |
|---|---|---|
| The named bin's own cpl=20 baseline figures | `python3 -c "..."` against exp-110's own committed `experiments/110-t28-item-i-local-norm-and-controls/results.json` (not hand-typed — `run.py` reads these back programmatically, see `NAMED_BIN_IDX`/`BASELINE_*`) | Bin index **4** of 48 sits exactly on −146.25° (`abs(BIN_CENTERS_DEG[4] - (-146.25)) < 1e-9`). `peccored[4]=1.0869903329739812e-4`, `hollow[4]=1.1943830960599575e-4`, `delta[4]=-1.0739276308597632e-05` (⇒ local relative deviation `|delta|/|peccored|=9.880%`, re-derived, matching exp-108's own Phase-5-corrected "9.88%" figure). Mirror-pooled floor (K=3, median) = `1.1261666e-3`; `local_snr_peccored=0.09652`, `local_snr_hollow=0.10606` — **both individually ~10× below even the unmultiplied (K=1) floor**, confirming PHOTONICS' own exp-110 Phase-5 finding that no bin near this reading sits anywhere close to the K=3 cutoff. |
| `geom_fixedabs_cpl(r, cpl)`'s own correctness (a genuinely new instrument for this family — R6-style ground-truth-recovery discipline, applied to a construction, not a fitted estimator) | `python3 experiments/112-.../run.py --verify-geometry` (real, executed, zero-FDTD — pure arithmetic, no `Sim.run()` call) | `{"pass_": true, "mismatches": []}` at BOTH r=156 and r=312: `geom_fixedabs_cpl(r, cpl=20)` reproduces `R.geom_fixedabs(r)` (`experiments/110-.../run.py`) field-for-field, including the two NEW fields (`absorb`, `edge`) this generalization adds, which are module constants (`R.ABSORB=40`, `R.EDGE=40`) in the cpl=20-only original. |
| Cost estimate for the recommended option (`cpl=25`, r=156 alone) | `python3 experiments/111-.../cpl_cost_table.py` (re-run fresh this cycle, not re-typed from exp-111's own committed output) | `cpl=25 ratio=1.25x  r156: 1469.19s (0.4081h)  r312: 13551.19s (3.7642h)  both: 15020.37s (4.1723h)` — matches exp-111's own committed `cpl_cost_table_output.json` exactly (bit-identical, confirming that file has not silently drifted). |
| Whether the EXISTING R27/R28 cost gate (`R.cost_gate_check`, reused unmodified — it is `cpl`-agnostic, reading only a `kappa_ratio=r312/r156` and the empirically-fit wall-time exponent) would clear a FUTURE r=156→r=312 expansion AT `cpl=25`, using the cost table's own `cpl=25`/r=156 total (`1469.186126254499s`) as the projected pilot | `python3 -c "..."` invoking `R.cost_gate_check(1469.186.../3.0, 1469.186...)` directly (the real committed function, not a hand-derived formula) | `{"pilot_empty_wall_s": 489.729, "pilot_total_wall_s": 1469.186, "pilot_pass": true, "kappa_ratio": 2.0, "kappa_exponent": 3.2053299988171697, "safety_margin": 1.1, "projected_312_total_s": 14906.304, "total_pass": **false**, "proceed_to_r312": **false**}` — the existing gate, AS CURRENTLY BOUNDED (`COST_GATE_TOTAL_S=10800s`/3h), would **REFUSE** an r=312 expansion at `cpl=25` projected from this pilot (`14906.3s` ≈ 4.14h > 3h bound). This is a real, disclosed, code-derived reason (not merely a scheduling preference) to keep this cycle's own committed spend to r=156 alone — see §3. |

### 2.1 Geometry — congruent `cpl=20→25` refinement, r=156, fixedabs family

Every cell-count quantity scales by `ratio = cpl/CPL_600 = 1.25`; `sigma_max`
scales by `1/ratio` (holds `tau_shell` — the shell's optical thickness —
exactly constant, `24.0` at both resolutions). This is the SAME
congruent-construction convention this program already uses for the
T21/Block-MINI family's own `R3_RATIO`/`R4_RATIO` cpl refinements
(`experiments/069-t21-block-mini-period-match-power-up/design_geometry.py`),
generalized here to the fixedabs family for the first time (`geom_fixedabs_cpl`,
`experiments/112-.../run.py`) — **not** a "hold geometry-in-cells fixed,
change `cpl` alone" construction, which would silently shrink the object's
electrical size rather than refine its grid resolution.

| Quantity | `cpl=20` (baseline, exp-108/110, unchanged) | `cpl=25` (this cycle) |
|---|---|---|
| Domain `N` (cells, square) | 1120 | **1400** |
| `CX`, `CY` | 504, 560 | **630, 700** |
| `SRC_X` | 128 | **160** |
| `STEPS` | 6400 | **8000** |
| `R_CORE` | 108 | **135** |
| `R_COAT` | 156 | **195** |
| `sigma_max` | 0.5 | **0.4** |
| `tau_shell` (invariant, by construction) | 24.0 | 24.0 |
| `ABSORB` (PML-taper thickness, cells) | 40 | **50** |
| `EDGE` (source cosine-taper, cells) | 40 | **50** |
| `box_a` (margin=32) | (284, 724, 340, 780) | **(355, 905, 425, 975)** |
| `ref` (incident-intensity strip) | (504, 560, 120) | **(630, 700, 150)** |

**Physical-consistency check (disclosed, verified, not assumed):** total
simulated optical periods = `STEPS·S/lam` (`S=courant_frac/√2` fixed,
`lam=cpl`). At `cpl=20`: `6400·S/20 = 320·S`. At `cpl=25`:
`8000·S/25 = 320·S` — **identical**, confirming the congruent-scaling
recipe preserves the exact number of optical periods simulated (hence the
same settling behavior), not merely the same geometry ratios.

**Domain-clearance check (verified, not assumed):** `box_a` at `cpl=25`
spans `x∈[355,905]`, `y∈[425,975]`, inside `N=1400`'s valid interior
`[ABSORB, N−ABSORB] = [50, 1350]` with **305-cell clearance on every
side** — comfortably inside, matching this program's own established
domain-clearance-verification discipline (e.g. exp-108's own margin=65
check).

**FDTD calls this cycle: 3** (empty, hollow-article, PEC-cored-article,
r=156 only). **Predicted wall time: 1469.19s (24.49 min)**, from the
regenerated `cpl_cost_table.py` (§2.0) — well under `COST_GATE_PILOT_S`
(5400s/90min); no r=312 call is attempted or gated this cycle.

### 2.2 Target bin and falsification bands

**Target: bin index 4 (−146.25°), margin=32 (`box_a`), r=156 only.** The
`+168.75°` bin at r=312 is explicitly **not** tested this cycle (§3).

Two independent, complementary checks (`classify_resolution_check`,
`experiments/112-.../run.py`) — neither alone is decisive, both reuse
already-existing code:

**Check A (primary — reuses `classify_item_i_local`, UNMODIFIED, at the
new resolution).** Does the named bin's own `local_snr` improve enough to
newly clear even the K=1 floor — the bar PHOTONICS' own exp-110 Phase-5
review found cleanly separates the RESOLVED population (`snr≥1.32`
everywhere) from the UNRESOLVED one (`snr≤0.79` everywhere), with no bin
anywhere near the K=3 cutoff?

| Outcome | Condition | Reading |
|---|---|---|
| **SURVIVES** ("the feature survives resolution refinement") | `local_snr_peccored≥1.0` **AND** `local_snr_hollow≥1.0` at `cpl=25` | candidate real structure — the coarser grid's own floor was masking a genuine signal |
| **COLLAPSES** ("is a grid artifact") | neither `local_snr` improves over its `cpl=20` value (`0.0965`/`0.1061`) | the signal tracks the floor — consistent with pure discretization noise |
| **AMBIGUOUS/inconclusive** | some improvement, still `<1.0` | genuinely unresolved by this one check |

**Check B (supplementary — this program's own founding T28 R3 standard,
exp-069: "sign-flip/order-of-magnitude collapse").**

| Outcome | Condition |
|---|---|
| **SURVIVES** | `delta[idx]` keeps the same sign as `cpl=20` (`−1.073928×10⁻⁵`) AND `0.1 ≤ \|delta_new/delta_old\| ≤ 10` |
| **COLLAPSES** | sign flip, OR `\|delta_new/delta_old\| < 0.1` |
| **AMBIGUOUS** | neither band cleanly applies |

**Reproduction/self-consistency precondition (must PASS before either
check is trusted):** `sum(sigma_scat_per_bin) == sigma_scat` (from
`sections.widths()`, same box — `angular_scattered_pattern`'s own
docstring identity) to `<1e-9` relative, both peccored and hollow, at
`cpl=25`. **Geometry-identity precondition (already verified, §2.0):**
`geom_fixedabs_cpl(r, 20) == R.geom_fixedabs(r)` — HALTs Phase 4 before
any `Sim.run()` call if this ever regresses.

## 3. Scope decision: r=156 alone, zero Tier-1 bundling this cycle

**r=156-alone, not both r.** Matches exp-111's own explicit recommendation
and is reinforced, not merely repeated, by §2.0's own fresh finding: the
existing R27/R28 cost gate, projected from the `cpl=25` cost table's own
r=156 pilot figure, would **REFUSE** an r=312 expansion under the current
`COST_GATE_TOTAL_S` bound (`14906.3s` projected vs. `10800s` bound) — so
"r=156 first, expand only if decisive" is not merely the cheaper option,
it is very likely the ONLY option this cycle's own gate would currently
clear. Expanding to r=312 at `cpl=25` in a future cycle would require
either a genuinely decisive r=156 result justifying an explicit,
named decision to raise `COST_GATE_TOTAL_S` (disclosed, not silently
overridden), or accepting a longer multi-chunk spend across sessions —
named here as an open question for that future cycle, not resolved now.

**Zero Tier-1 bundling this cycle — deliberate, considered, not merely
"kept simple."** I considered bundling item (0b) — hardening
`classify_item_i_local`'s `floor<=0.0` guard to an amplitude/epsilon-scaled
magnitude test (QUANTUM's own finding, originally raised at exp-111
Phase 5: the current test is a bit-exact-zero check, not
floating-point-robust) — since it is self-motivated by direct relevance
to correctly interpreting THIS cycle's own new floor readings. I decline
it anyway, for two independently sufficient reasons: (1) **it is not
actually load-bearing here** — every one of the 12 real committed cells
across both exp-110 and this family reads a floor strictly in
`[2.3×10⁻⁴, 2.1×10⁻³]`, orders of magnitude from float-epsilon; the
original defect was demonstrated only on a CONSTRUCTED adversarial
synthetic input, not a realistic concern for genuine FDTD noise (which is
essentially never floating-point-exact mirror-symmetric); (2) **density
risk** — this cycle is already the first genuinely new-FDTD spend on this
sub-thread in many cycles (twice deferred specifically so it would not be
run "alongside its own [gate] repair"); bundling a second, unrelated
code-hardening item onto the SAME cycle that finally executes the
long-deferred physics question repeats exactly the density pattern this
exact governance sub-thread has landed on PARTIAL under, every cycle
since Iteration 82. I decline (0a) (the `gate_reposition_control.py`
checkpoint-resume case — EM's own item, orthogonal to interpreting this
cycle's own data, its underlying property already independently confirmed
to hold per Iteration-88's own Phase-5 audit), (0c) (a non-sinusoidal
FI-D successor — a construction-validation item for a DIFFERENT
instrument's phase robustness, not load-bearing here), (2) (the
`R2_SMOOTH_THRESHOLD=0.90` re-derivation — irrelevant, this cycle fits no
smoothness model), and (3) (MATERIALS' own fabrication-tolerance bound —
explicitly MATERIALS' own charter question, about physically achievable
manufacturing tolerance, a different question from this cycle's own
purely-numerical grid-resolution question). **If this cycle's own real
`cpl=25` data comes back with a floor anywhere near float-epsilon scale
(which would make the (0b) hardening newly load-bearing), that finding
itself licenses a same-shift fix at Phase 3/Result time — this proposal
does not pre-register that as expected.**

## 4. T1 escape route: N/A

Confirmed structurally against exactly what this cycle changes: a
congruent geometry-scaling function, a checkpoint/resume capture driver,
and a comparison of two already-existing classification functions'
readings across two resolutions. No σ(I)/σ(x,t)/angular-selectivity/
sub-threshold content is expressible in a grid-resolution parameter or a
floor-comparison classifier. No constraint-1/2/3/4 verdict is scored or
moved anywhere in this document — matching every T28 desk/instrument
cycle since Iteration 46.

## 5. Idealizations — what this leg does and does not establish

- **Does establish**: a real, executed, congruent `cpl=20→25` refinement
  of the fixedabs family's own r=156 geometry, applying the SAME,
  unmodified mirror-pooled-floor instrument to the SAME named bin, with a
  pre-registered, falsifiable verdict on whether that bin's reading
  survives or collapses under this one resolution step — the first actual
  data this specific near-null bin has ever received beyond its single
  `cpl=20` reading.
- **Does NOT establish**: full continuum convergence. A single new
  resolution point relative to the `cpl=20` baseline is, per this
  program's own R15 discipline (two points cannot on their own distinguish
  genuine continuum convergence from a persistent recipe-level artifact or
  a genuinely non-convergent oscillation), sufficient only to rule out (or
  fail to rule out) a sign-flip/order-of-magnitude collapse — the SAME,
  deliberately modest standard T28's own founding R3 check (exp-069) used
  at its first application. A third, differently-scaled resolution point
  (e.g. `cpl=30`, already costed at `2538.75s`/r=156 in `cpl_cost_table.py`)
  would be the minimum needed for a stronger convergence claim, not
  proposed this cycle.
- Does NOT test the `+168.75°` bin at r=312 — deferred, per §3's own
  disclosed cost-gate finding.
- Does NOT re-derive `R2_SMOOTH_THRESHOLD=0.90`, MATERIALS' own
  fabrication-tolerance bound, the `gate_reposition_control.py`
  checkpoint-resume case, or a non-sinusoidal FI-D successor — all
  explicitly declined this cycle, §3.
- `geom_fixedabs_cpl`'s own `ABSORB`/`EDGE` scaling (40→50 cells) is a
  disclosed, first-use choice for this family, following the T21/
  Block-MINI family's own established convention (`R3_TAPER`/`R4_TAPER`
  etc. all scale with the same ratio) — not independently re-derived from
  a PML-reflectance or taper-adequacy bound specific to THIS geometry.
- If Check A and Check B disagree (e.g. A says SURVIVES, B says
  AMBIGUOUS), both are reported side by side, per this program's own
  established "when instruments disagree, report both, the more
  conservative one governs" discipline (R10) — no verdict is manufactured
  by picking whichever check reads more favorably.
- 2D TMz, λ=600nm only — unchanged program-wide scope.
