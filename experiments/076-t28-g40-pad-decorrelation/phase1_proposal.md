# exp-076 Phase 1 — G40/`PAD` Decorrelation

**Panel Iteration 53. Lead seat: QUANTUM OPTICS, by rotation.** Executes
PLAN.md's Iteration-53 queue item 1 (near-unanimous #1 across all six of
exp-075's Phase-5 seats, `experiments/075-t28-absorb-boundary-wkb-
reflectance/phase5_redteam_audit.md` §7): the G40/`PAD` decorrelation build.

---

## 1. Mechanism/instrument narrative (≤300 words)

Since Iteration 48 (exp-071), every T28 causal claim on the congruent
`ABSORB`-depth series `{C40,C60,C70,C80}` has been confounded:
`PAD = ABSORB − 40` exactly, by construction, at all four configs (padding
was added to keep other geometry parameters — `A`, plane/source clearances,
aperture, `D_SP` — congruent as `ABSORB` grew). No result on this series
can be cleanly attributed to `ABSORB` depth, `PAD` depth, or the domain
geometry the padding drags along with it.

This is not a mechanism proposal. It is an *instrument* build: a fifth
FDTD configuration, `G40` (`ABSORB=40, PAD=40`), already fully specified
in `experiments/065-t24-absorb-boundary-sweep/design_geometry.py` but never
run at T28's own dense (31-angle, settled-STEPS) window. `G40` shares C80's
*entire* padded domain, clearances, and aperture (`A=752`, identical to
every congruent config) but reverts `ABSORB` to 40 cells. Because
`PAD=ABSORB−40` no longer holds for the pair `(G40, C80)` (both have
`PAD=40`, only `ABSORB` differs) or for the pair `(C40, G40)` (both have
`ABSORB=40`, only `PAD` differs), these two new differences isolate the two
axes the congruent series entangles: `C80 − G40` is a pure-`ABSORB` effect
at fixed `PAD=40`; `G40 − C40` is a pure-`PAD` effect at fixed `ABSORB=40`.

What is decorrelated: whether T28's ~2.84° amplitude-mismatch signal (the
`√(A_i²+A_q²)/amp` channel, exp-072's own instrument, baseline
0.161/0.041/0.020/0.166 on the confounded series) tracks `ABSORB` depth or
the padded-domain geometry `PAD` drags along with it. Why: this is the
single most information-dense open question left on T28's board after
exp-075 REFUTEd both boundary-reflectance-echo mechanism classes and found
the model's own predicted echo `ABSORB`-depth-*dependent* while the real
residual is depth-*independent* — a prior hint toward PAD/geometry, not yet
tested directly. How: 31 new FDTD calls (`G40` at the exact `block_dense`
grid), scored with the identical formula already applied to the confounded
series, so the new numbers sit on the same axis as the existing baseline.

---

## 2. Parameter table

### 2a. G40 geometry (reproduced verbatim by
`experiments/065-t24-absorb-boundary-sweep/design_geometry.py`, re-run this
cycle to confirm — not hand-typed, R4)

| cfg | ABS | PAD | NX | NY | SRC_X | PLANE_X | OBJ_Y | y_lo | y_hi | A | aper | clrPl | clrSrc | clrSpan | D_SP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C40 | 40 | 0 | 360 | 1584 | 300 | 77 | 792 | 40 | 1544 | 752 | 1504 | 37 | 20 | 0 | 223 |
| C80 | 80 | 40 | 440 | 1664 | 340 | 117 | 832 | 80 | 1584 | 752 | 1504 | 37 | 20 | 0 | 223 |
| **G40** | **40** | **40** | **440** | **1664** | **340** | **117** | **832** | **80** | **1584** | **752** | **1504** | **77** | **60** | **40** | **223** |

`G40` is bit-identical to `C80` in every scene coordinate (`NX`, `NY`,
`SRC_X`, `PLANE_X`, `OBJ_Y`, `y_lo`, `y_hi`, `A`, aperture, `D_SP`) — the
*only* difference is the absorbing-boundary band thickness (`ABSORB=40`
cells fed to `Sim(..., absorb=40)`, vs C80's `absorb=80`), which is exactly
why `clear_plane` (37→77) and `clear_src` (20→60) differ: those clearances
are measured *from* the band edge, so a thinner band at the same domain
size opens more clear space, not less. `clear_span_y=40` (vs the congruent
series' `0`) is likewise mechanical: `y_lo=BASE_ABSORB+pad=80` while
`absorb=40`, so `clear_span_y=y_lo−absorb=40` — disclosed already in
`design_geometry.py`'s own construction, not a new finding.

`Sim.__init__`'s static `damp_e`/`damp_hx` arrays at every scored-window
cell (obj/flank_lo/flank_hi, offset by `pad=40`) were bit-identical between
`C40` and `G40` in exp-065's own `static_construction_identity()` gate
(`max_diff=0.0`, re-verifiable, zero FDTD steps) — the construction is
sound; this cycle spends the FDTD budget only where the boundary itself
(not the static array construction) is what's under test.

### 2b. Angle/wavelength grid for the new FDTD calls

Identical to `experiments/069-.../design_geometry.py::DENSE_ANGLES` (Block
DENSE), reused verbatim, never re-derived:

- 31 angles, θ ∈ [36.0°, 42.0°], 0.2° step, centered at 39.0°
- 600 nm only (`cpl=20`)
- `STEPS=2800` (T27's own established settled floor for this channel,
  exp-066/069 — **not** exp-065's own `Block PAD` `STEPS=1400` reading of
  `G40`, which is a different, unsettled instrument reading of the same
  config and is not reused here)
- `profile="plane"`, `edge=TAPER=40`, `amplitude=1.0` — the same
  `_one_run`/`block_dense` call idiom exp-069 used for C40/C80, reused
  verbatim (see §2d)

31 calls total (1 config × 31 angles × 1 wavelength). This *is* the ~31-call
budget cited by MATERIALS' verified estimate (PLAN.md, `phase5_redteam_
audit.md` §7) — no other new FDTD spend this cycle. C40's and C80's own 31
dense-sweep points are already committed
(`experiments/069-.../results.json::block_dense`) and are **reused, not
re-run**.

### 2c. Scoring formula/carrier — phase-invariant amplitude channel

Reused **identically** from `experiments/072-t28-differential-beat-fit/
run.py` (verified directly by re-invoking it against the committed
`C40`/`C60`/`C70`/`C80` arrays and reproducing 0.161/0.041/0.020/0.166 to
6 significant figures — see §7):

1. Per pair `(X, Y)`: `delta = Y − X` over the 31 dense angles, `x=sinθ`,
   `u = x − mean(x)`, `Cbar = (X+Y)/2`.
2. **Carrier fit** (`carrier_fit`, `exp072_run.carrier_fit`): a free-period
   grid search (`N_GRID_CARRIER=3000`, `P* ∈ [1.0,4.0]°`, `center_deg=39.0`)
   on `Cbar`, giving `T_x` (period in `sinθ` units) and `amp` (`Cbar`'s own
   fitted amplitude at that period); then `psi = −atan2(b,a)` from
   `_amp_phase_at(theta, Cbar, T_x, xbar)`.
3. **5-column ramped OLS fit** (`design_matrix`, at the FIXED `(T_x, psi)`
   from step 2): `delta ~ [1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]`,
   `θ_c = (2π/T_x)·u + psi`. Coefficients `(c0, A_i, A_q, R_i, R_q)`.
4. **Headline statistic**: `amp_ratio = √(A_i² + A_q²) / amp` — the
   envelope-amplitude mismatch between the two series at the common-mode
   carrier, normalized by that carrier's own amplitude. This is the
   fractional-envelope-amplitude channel; `R_i`, `R_q` (the ramp/period-shift
   columns) are NOT part of this statistic and are not used for any
   significance claim this cycle (see §7 for why this sidesteps the
   seventh-cycle retirement).

Applied to the two new pairs:

- **`PAIR_PAD ≡ (C40, G40)`**, `delta = G40 − C40` — isolates `PAD` alone
  (`ABSORB` fixed at 40, `PAD` 0→40).
- **`PAIR_ABSORB40 ≡ (G40, C80)`**, `delta = C80 − G40` — isolates `ABSORB`
  alone (`PAD` fixed at 40, `ABSORB` 40→80).

Both reported as `amp_ratio(PAIR_PAD)` and `amp_ratio(PAIR_ABSORB40)`,
directly comparable to the existing baseline `amp_ratio(C40,C60)=0.161`,
`amp_ratio(C60,C70)=0.041`, `amp_ratio(C70,C80)=0.020`,
`amp_ratio(C40,C80)=0.166` (the last being the *confounded, combined*
`ΔABSORB=40 & ΔPAD=40` effect these two new pairs decompose).

**Secondary, disclosed-only diagnostic (not gating)**: `delta_P_obs`, the
same fitted-period-shift readout exp-072 already computes and reports for
every pair (`delta_P_obs(C40,C80) = 0.06684°`, loaded from
`experiments/072-.../results.json`, not re-fit) — used only for the
additivity check in §4(c), never as a significance/detection claim (that
route is the formally-retired instrument class, §7).

### 2d. FDTD budget

| Item | Calls |
|---|---|
| `G40` × 31 angles × 600 nm × STEPS=2800 | 31 |
| **Total new FDTD calls** | **31** |

Projected cost: `G40` shares `C80`'s domain, whose measured per-call CPU
basis is 34.8 s at `STEPS=1400` (exp-065's own measured basis, 4-way
`ProcessPoolExecutor` contention included); at `STEPS=2800` that scales
linearly to 69.6 s/call CPU. At `N_WORKERS=4`, `PARALLEL_EFFICIENCY≈0.98`,
`OVERHEAD_FACTOR=1.15` (exp-065's own measured constants): wall ≈
`1.15 × 31 × 69.6 / (4×0.98)` ≈ **630 s ≈ 10.5 min**. Cross-checked against
exp-069's own committed `block_dense` wall-clock (62 calls, C40+C80 mixed,
428.4 s total, 6.9 s/call amortized under 4-way parallelism) — a 31-call,
single (more expensive) config run is expected to land in the same
ballpark, consistent with this estimate. No other FDTD spend this cycle:
`block_leg750` (16 points, 750 nm) is PLAN.md's separately-queued item #2,
explicitly out of scope here.

---

## 3. T1 escape route

**N/A, instrument/model-fidelity class.** This cycle does not propose or
score a T1 mechanism (σ(I), σ(x,t), angular selectivity, or sub-threshold
operation); it decorrelates a construction confound inside the T28
measurement instrument itself. Per program convention for this cycle type
(exp-069/Iteration 46, exp-065/Iteration 42, and VISION SCIENCE's
purely-instrumental Iteration 42/exp-065 precedent cited in this cycle's
own brief), constraint 3 is not engaged and Checkpoint criterion 2
(mechanism-class boundary) does not apply.

---

## 4. Predicted outcomes — falsifiable, pre-registered bands

All bands below are computed from the already-committed baseline (`amp_
ratio(C40,C80)=0.166`, the confounded combined effect these two new pairs
decompose) and fixed **before** any G40 FDTD call runs. No threshold below
is adjusted after seeing real G40 data.

**(a) Confound relieved — T28 reads as genuinely `ABSORB`-tied.**

- `amp_ratio(PAIR_ABSORB40) ≥ 0.116` (≥ 0.7×0.166 — the pure-`ABSORB`
  effect at fixed `PAD` reproduces most of the combined signal) **AND**
- `amp_ratio(PAIR_PAD) ≤ 0.050` (≤ 0.3×0.166, at or below the size of the
  smallest already-established adjacent-pair reading, `C70–C80=0.020` —
  the pure-`PAD` effect is small/near-noise-floor).

If both hold: every prior T28 CONFIRM-shaped reading on the congruent
series can be re-read as substantively `ABSORB`-depth-tied, not an
artifact of the padding construction — a real narrowing, though it does
not itself identify a mechanism (T28's substantive "why" stays open).

**(b) PAD-or-geometry-tied — the confound is NOT relieved in the
reassuring direction.**

- `amp_ratio(PAIR_PAD) ≥ amp_ratio(PAIR_ABSORB40)` **OR**
- `amp_ratio(PAIR_PAD) ≥ 0.116` (≥ 0.7×0.166 on its own — padding alone,
  at fixed `ABSORB`, reproduces most or more of the combined signal).

If either holds: five iterations of T28 causal claims on the `ABSORB`
series (46–52, including exp-071's own monotonic-period-vs-`ABSORB` trend
and exp-075's own cross-config-correlation reading) must be re-read as
possibly padding/domain-geometry-tied, not physically tied to the graded
boundary's absorption depth — a real, load-bearing correction to how this
whole sub-thread's prior findings should be cited going forward, consistent
with the prior hint noted in §7 of exp-075's audit (WKB echo strongly
`ABSORB`-depth-dependent; real residual depth-independent — cited here as
a prior, not a new finding of this cycle).

**(c) Other decision-relevant outcomes.**

- **(c1) Both small.** `amp_ratio(PAIR_PAD) < 0.050` **AND**
  `amp_ratio(PAIR_ABSORB40) < 0.050` (neither pure-axis effect individually
  clears the smallest established baseline reading), while the combined
  `amp_ratio(C40,C80)=0.166` is 3.3× larger than either. This is a
  detectable signature that the amplitude-mismatch metric does not
  decompose additively across the two axes — informative about additivity
  itself (see (c2)) even though it does not, on its own, identify which
  axis is "responsible."
- **(c2) Aggregate non-additivity, via the period-shift channel (the
  quantity the Director asked to identify: what IS detectable even though
  the true interaction term at the missing 4th corner,
  `config(ABSORB=80,PAD=0)`, is not identifiable).** Define
  `rho_pad_absorb = |delta_P_obs(PAIR_PAD) + delta_P_obs(PAIR_ABSORB40) −
  delta_P_obs(C40,C80)| / max(|delta_P_obs(C40,C80)|, 0.005)`, mirroring
  exp-072's own `rho_c` convention (identical 0.005 floor, same
  denominator-degeneracy protection) applied to the fitted period-shift
  read at each pair's own carrier. `delta_P_obs(C40,C80) = 0.06684°`,
  loaded from `experiments/072-.../results.json`, not re-fit.
    - `rho_pad_absorb ≤ 0.30`: the period-shift channel is reasonably
      additive — consistent with (though not proof of) the additivity
      assumption §5 states is otherwise unverifiable at this design size.
    - `rho_pad_absorb ≥ 1.00`: a genuine, detectable aggregate
      non-additivity signature — real evidence an `ABSORB×PAD` interaction
      exists in the amplitude/period structure, even though its actual
      value (what would be measured at the geometrically-invalid 4th
      corner) remains permanently unidentified by this design. This
      outcome does NOT adjudicate (a) vs (b); it is orthogonal, disclosed
      regardless of which of (a)/(b) the headline bands land in.
  Values strictly between 0.30 and 1.00: reported, not adjudicated
  (matches this program's own convention for a middle band with no
  pre-committed verdict — see exp-071/072's own precedent of leaving a
  genuine "NEITHER" zone rather than forcing a call).

None of (a)/(b)/(c) constitutes a RESOLVED/CONFIRMED-class significance
claim on `R_q` or any carrier/phase-conditioned coefficient — see §7. All
three read directly off `amp_ratio` and `delta_P_obs`, both fixed-formula
readouts already computed for the confounded series.

---

## 5. Idealizations

1. **600 nm only.** No new `G40` leg at 450 nm or 750 nm this cycle;
   `block_leg750` (16 points, 750 nm, C40/C80 only) is PLAN.md's separately
   queued item #2, explicitly not folded in here.
2. **The 2×2 (`ABSORB`×`PAD`) factorial is not completable.**
   `config(ABSORB=80, PAD=0)` gives `clear_span_y = −40` (geometrically
   invalid — re-verified directly this cycle by calling
   `dg065.config(80, 0)`: `y_lo = BASE_ABSORB + pad = 40 + 0 = 40`,
   `clear_span_y = y_lo − absorb = 40 − 80 = −40`; `clear_plane` and
   `clear_src` go negative too, −3 and −20 respectively). Main
   effects (pure-`ABSORB`-at-fixed-`PAD`, pure-`PAD`-at-fixed-`ABSORB`) are
   identifiable from `{C40, C80, G40}` only **under an additivity
   assumption** (no `ABSORB×PAD` interaction) — the interaction term itself
   is not identifiable at all with this 3-point design, at any `ABSORB`/
   `PAD` combination. §4(c2)'s `rho_pad_absorb` diagnostic can detect that
   additivity fails in aggregate; it cannot say by how much, in which
   direction, or attribute the failure to a specific interaction value.
3. **Different pairs use independently-fit carriers.** `PAIR_PAD` and
   `PAIR_ABSORB40` each get their own `(T_x, psi)` from a free-period search
   on their own `Cbar` — matching exp-072's convention exactly (needed for
   direct comparability to the 0.161/0.041/0.020/0.166 baseline, all of
   which use this same per-pair convention), but meaning `amp_ratio`
   values are magnitudes computed in different local bases, not components
   of one shared vector. `amp_ratio(PAIR_PAD) + amp_ratio(PAIR_ABSORB40)`
   is **not** expected to equal `amp_ratio(C40,C80)` even under perfect
   additivity of the underlying physics (amplitude magnitudes of
   different-phase/near-but-not-identical-frequency signals do not add
   linearly) — this is why §4(c2)'s additivity check uses `delta_P_obs`
   (a signed, per-carrier quantity with its own established `rho_c`
   convention, exp-072) rather than `amp_ratio` itself.
4. **`G40` has never been run at settled `STEPS=2800` or at T28's dense
   window before.** exp-065's own `Block PAD` `G40` legs (3 angles ×
   3 wavelengths, `STEPS=1400`) are a distinct, unsettled-STEPS,
   sparse-angle reading of the same config — not reused as data here (T27
   established `STEPS=1400` is not settled on this channel at
   near-grazing angles); this cycle is a genuinely fresh FDTD build for
   `G40`, built on exp-069's own settled-STEPS `block_dense` machinery.
5. **`amp_ratio`'s carrier is fitted from data, not parameter-free** — see
   §7's R6 disposition. A dedicated, zero-FDTD synthetic ground-truth
   recovery check was run this cycle (not merely asserted) before any real
   `G40` data is scored.
6. **cpl=20 (native resolution) only.** No R3 resolution check on the new
   `G40` legs this cycle — a natural Iteration-54+ follow-up if either new
   `amp_ratio` reading comes back large enough to be load-bearing for a
   future headline claim.
7. **`amp_ratio` and `delta_P_obs` are fixed-formula readouts, not
   significance tests.** No p-value, null-calibration, or `RESOLVED`-class
   claim is made this cycle on either new pair — the (a)/(b)/(c) bands in
   §4 are magnitude comparisons only, deliberately outside the formally-
   retired differential/two-tone significance-testing instrument class
   (§7).

---

## 6. LOGBOOK.md / rule-compliance confirmation

**(i) LOGBOOK.md read in full, this seat, before writing this proposal**,
in sequential chunks (offset/limit) covering the full RULED OUT registry
(R1–R8), the full ESTABLISHED section, every LIVE THREAD (T1–T28) in full,
and the complete Iteration 42/46–52 narrative bodies (exp-065, exp-069
through exp-075) — cross-checked directly against the underlying committed
files (`experiments/065-.../design_geometry.py` + its own printed output,
`experiments/069-.../run.py`/`design_geometry.py`, `experiments/072-.../
run.py`/`results.json`, `experiments/075-.../phase5_redteam_audit.md`) not
merely read as prose. **The independently-prepared digest supplied to this
cycle agrees with this seat's own reading on every load-bearing point** —
no discrepancy found between the digest and LOGBOOK.md itself. One
precision note, not a digest/LOGBOOK.md disagreement: PLAN.md's own
Iteration-53 queue text (and the digest, following it) characterizes the
amplitude channel as having "no fitted carrier phase." Reading
`experiments/072-.../run.py::carrier_fit`/`_amp_phase_at` directly (not
taking PLAN.md's phrase at face value — R8) shows the carrier's period
`T_x` (a free-period grid search) **and** its phase `psi` (`−atan2(b,a)`)
are both fit from data; what is true, and presumably what the phrase
means, is that `amp_ratio` is *invariant* to the specific carrier-phase
rotation that caused exp-072's own Iteration-49 sign bug (the same
property exp-073's own `‖R‖=√(R_i²+R_q²)` was shown to have) — a narrower,
verified claim, not "carrier-free." See §7 for how this is handled.

**(ii) Nothing in this proposal re-proposes a ruled-out idea.** This is not
the `P`-normalized-fringe-phase-offset regressor (R5), not a dense
named-constant search (R5 addendum), not a re-litigation of R1/R2/R3's
mechanism-class rulings (out of scope for an instrument cycle), and not a
resumption of the differential/two-tone `R_q`-significance-testing
instrument class formally retired at Iteration 51 (R7's own trigger cycle)
— see §7 for why the amplitude channel is a different instrument class,
not a seventh cycle on the retired one.

**(iii) Standing rules and disposition:**

- **R4** — every number in §2 is produced by re-running the actual
  committed script (`design_geometry.py`, this cycle) or loaded
  programmatically from a committed `results.json` (never hand-typed);
  the baseline 0.161/0.041/0.020/0.166 figures were independently
  reproduced by re-invoking `experiments/072-.../run.py`'s own functions
  against the committed data (§2c), not copied from prose.
- **R5** — the pre-registered bands in §4 exist precisely so a single
  numeric coincidence (e.g. `amp_ratio(PAIR_PAD)` happening to land near
  `amp_ratio(C40,C80)`) cannot be over-read without clearing a stated
  threshold; no named-constant search is performed this cycle.
- **R6/`G0-e` — directly engaged, resolved this cycle, not deferred.**
  `amp_ratio` conditions on a fitted carrier (`T_x`, `psi`) per R6's own
  literal text ("any future estimator that conditions on a fitted carrier
  **or** phase parameter"). Rather than assert exemption on the strength
  of `‖R‖`'s prior good behavior in a *different* pair of coefficients
  (`R_i`/`R_q`, not `A_i`/`A_q`) — the exact shape of argument R8 forbids
  filing as sufficient — this cycle built and ran a dedicated `G0-e`-style
  synthetic ground-truth recovery check,
  `g0e_amplitude_channel_check.py` (zero FDTD, reuses `carrier_fit`/
  `design_matrix`/`_amp_phase_at` from `experiments/072-.../run.py`
  verbatim): inject a KNOWN envelope-amplitude mismatch fraction at 16
  swept carrier phases × 14 magnitudes (±2% to ±160%, spanning and
  exceeding the observed baseline range) with a matched period (Case 1,
  224 cells) and, as a cross-talk stress test, the same sweep with a
  simultaneous small period mismatch injected too (Case 2, 8×8×6=384
  cells, `dP_true ∈ {±0.01,±0.04,±0.08}°`). **Result: Case 1 worst
  `|recovered/true − 1| = 1.03×10⁻⁴` (PASS, ≤2%, R6's own bar); Case 2
  worst `|recovered/true − 1| = 8.35×10⁻³` (PASS, ≤5%, relaxed only for
  the disclosed first-order-in-`u` term present exclusively in the mixed
  case). `G0-e OVERALL: PASS`.** This is a Phase-1 precondition check, not
  a substitute for re-verifying it holds once real `G40` data is in hand —
  it will be re-confirmed unchanged (not merely cited forward) before any
  real-data `amp_ratio` is reported as a headline number, matching
  exp-072's own `g0_pass` precondition structure.
- **R7** — not directly triggered (no conditioning/VIF number is used to
  certify a closure or detection claim here); its spirit is respected: the
  actual fitted `amp_ratio` from real `G40` FDTD data, not the geometric
  congruence table alone, is what will decide (a) vs (b) vs (c).
- **R8** — see (i) above: the "no fitted carrier phase" characterization
  was independently checked against the actual code rather than repeated,
  and where it proved imprecise, the narrower true claim (rotation-
  invariance to the specific R6-triggering bug, not carrier-freedom) is
  stated explicitly rather than left to stand uncorrected.
- **R1/R2/R3** — not engaged; no mechanism-class claim is made this cycle
  (§3).

---

## 7. Why this is not a seventh cycle on the retired instrument class

Exp-074's seventh-cycle rule (LOGBOOK.md, Iteration 51) retires "a
sign-flip/permutation null on this ramped-quadrature OLS basis, at any
window width, single- or multi-tone" — i.e., using `R_q` (or a null
constructed around it) to certify a `RESOLVED`/significant detection. This
cycle's `amp_ratio = √(A_i²+A_q²)/amp` uses the *same* 5-column ramped
basis and the *same* per-pair carrier fit (deliberately, for
comparability — §2c), but reads off `A_i`/`A_q` (the non-ramping envelope
columns), not `R_i`/`R_q` (the ramp/period-shift columns), and attaches no
null-calibration or significance claim to it at all — it is scored purely
against the pre-registered magnitude bands in §4, exactly as the
0.161/0.041/0.020/0.166 baseline already was in exp-072's own record
(computed and reported there, independent of that cycle's own `RESOLVED`
gate, which used `R_q`/`p_restricted_holm` exclusively). PLAN.md's own
queue text states this explicitly ("inherits neither the window-resolution
problem nor any sign-flip calibration problem... explicitly NOT barred by
exp-074's own seventh-cycle rule") — independently confirmed here by
reading `experiments/072-.../run.py` line by line (§2c) rather than
accepted on citation alone.

---

## 8. Files

- `g0e_amplitude_channel_check.py` / `g0e_amplitude_channel_check_output.json`
  — the R6/`G0-e` synthetic ground-truth recovery check (§6), zero FDTD,
  already run.
- This document.

No `lab/` diff. No FDTD calls yet (Phase 1, house discipline — predictions
are committed before any run).
