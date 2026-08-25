# PHASE 4 — RESULTS · Panel Iteration 50 · exp-073
## Official run of the corrected differential/beat-fit re-issue (T28), behind `G0-e`

*Official Phase-4 run: `run.py`, unmodified, executed after Phase 3's
git-frozen predictions (commit `c771a7e`). Deterministic — fixed seeds
throughout (`SIGN_FLIP_SEED`/`G0E_SEED`/etc., unchanged from Phase 3); this
run reproduces, bit-for-bit on every reported quantity, the development
run disclosed and bounded in `phase3_synthesis.md` §4. Elapsed: 128.7s,
single-core, zero FDTD, zero `lab/` diff. Full data: `results.json`.*

---

## Bottom line

**Combined Verdict: `HALT_NULL_MISCALIBRATED`.** `G0-e(ii)` — the null-
calibration gate mandated by Red Team's Phase-2 audit specifically to
pre-emptively test whether T2-3's sign-flip null is correctly sized before
any real data is touched — fires on **both** legs, at **every** grid cell
tested. **No real pair (`C40–C60`, `C60–C70`, `C70–C80`, `C40–C80`) was
scored.** `p073_2`/`p073_3`/`p073_4` are all `None`; `per_pair` is empty.

This is not a defect discovered post hoc. It is the design's own safety
net (`G0-e`, LOGBOOK R6) doing exactly the job it was built and mandated to
do, exactly as Red Team's Phase-2 audit forecast in its own §6 ("the most
likely Phase-4 outcome... is `HALT_NULL_MISCALIBRATED`"), independently
reproducing that audit's own Attack-4 finding — a genuinely anti-
conservative sign-flip null on this exact `n=31, p=5` leverage-concentrated
design — for a third time, now on the real design's own official run.

---

## Identity / integrity gates — all upstream gates PASS

| Gate | Result | Detail |
|---|---|---|
| **G0-a** (grid identity) | **PASS** | θ arrays from `experiments/069`, `071`, `072`'s own `results.json` files bit-identical, 31 points, all three checked equal |
| **G0-b** (telescoping identity) | **PASS** | `delta_40_60+delta_60_70+delta_70_80−delta_40_80`, max abs residual `0.0` exactly |
| **G0-c** (column provenance) | **PASS** | exp-069's committed `delta` column ≡ `C_empty_C80−C_empty_C40`, max abs Δ `0.0` exactly |
| **G0-d** (conditioning) | not reached as a per-pair exclusion — no pair was scored (see below) | `cond(X5)` was not computed for any pair since `G0-e` HALTed first, per the pre-registered gate order (§7, `phase1_proposal.md`: identity/integrity gates evaluated first, in order) |
| **G0-e(i)** (recovery accuracy) | **PASS** | worst-cell `\|ΔP_est/ΔP_true−1\| = 1.10%` over the full widened 5,760-cell synthetic sweep (docket items 1–2), inside the 2% bar. Both tripwires clean: identity tripwire (`dR_q/dψ̄≡R_i`) worst error `9.4×10⁻¹¹`; `A_i` tripwire, now genuinely live (768 qualifying cells via the `δa`/`Δψ` legs, docket item 1), 0 failures at 1% tolerance. |
| **G0-e(ii)** (null calibration) | **FAIL → HALT** | see below |

**`G0-e(i)`'s own per-leg breakdown** (all inside the 2% bar):

| Leg | Cells | Worst recovery-ratio error | Worst identity error | `A_i` checked / failed |
|---|---|---|---|---|
| Primary (original `T_A`/`ΔP`/`ψ₀` sweep) | 3,456 | 0.35% | `9.4×10⁻¹¹` | 0 / 0 (vacuous by construction — `δa≡0`) |
| `δa` leg (new, docket item 1) | 768 | 0.28% | `5.7×10⁻¹¹` | 768 / 0 |
| `Δψ` leg (new, docket item 1) | 1,536 | 1.10% | `4.3×10⁻¹¹` | 0 / 0 (vacuous — `δa≡0` on this leg) |

The pipeline recovers known synthetic `ΔP` cleanly across amplitude,
carrier, effect-size, phase, **and now amplitude-difference and
independent-phase-offset** axes — PHOTONICS' own Attack-1 gap (the phase-
dominated regime was previously unreachable, the `A_i` tripwire previously
dead code) is closed and confirmed live.

---

## `G0-e(ii)` — the HALT, in full

**Construction** (docket items 3–4, `phase2_redteam_audit.md` §5): pure
H₀ noise (`y=ε`, `ΔP_true=0` identically) pushed through the real T2-3
sign-flip null (`N=20,000` surrogates/draw, `K=500` independent synthetic
datasets/cell), on two legs — **i.i.d.** Gaussian noise (`σ∈{0.0005,
0.002, 0.008}`) and a **residual-structure** leg (bootstrap-resampled,
rescaled real per-config free-period-fit residuals from exp-069/071,
docket item 4) — each swept over `ψ₀` (8 phases) × `σ`-grid (24 cells/leg)
× `α∈{0.01,0.05,0.10}` (72 cell-α combinations/leg, 144 total). Tolerance:
empirical rejection rate inside `α±3√(α(1−α)/K)` (a 3σ Monte-Carlo band at
`K=500`).

**Result: both legs fail every single cell-α combination — 72/72 (i.i.d.)
and 72/72 (residual-structure).**

| Nominal α | i.i.d. leg: mean rejection rate | i.i.d. range | ×nominal | Residual-structure leg: mean | range | ×nominal |
|---|---|---|---|---|---|---|
| 0.01 | 0.0543 | 0.030–0.078 | **5.4×** | 0.0566 | 0.036–0.076 | **5.7×** |
| 0.05 | 0.1143 | 0.086–0.146 | **2.3×** | 0.1131 | 0.092–0.150 | **2.3×** |
| 0.10 | 0.1709 | 0.148–0.218 | **1.7×** | 0.1707 | 0.132–0.210 | **1.7×** |

Worst single cell: i.i.d. leg, `σ=0.008, ψ₀=225°, α=0.10` → rejection rate
0.218 (band `[0.0598, 0.1402]`, deviation +0.118, **2.18× nominal**).
Residual-structure leg worst: `σ=0.008, ψ₀=0°, α=0.10` → 0.210 (**2.10×
nominal**).

**Reads exactly as Attack 7's own "can only be as bad or worse" argument
predicted, and as this cycle's own conjunctive requirement (docket item 4)
demands**: the i.i.d. leg — the *easier* of the two cases, and the only
one `phase1_proposal.md`'s own original design specified — already fails
uniformly; the residual-structure leg (the *harder*, more realistic case,
using real captured FDTD residuals rather than idealized Gaussian noise)
fails by comparable or slightly larger margins at every `α`, never better.
Neither leg passes, so `G0-e(ii)` fails on either the disjunctive OR the
conjunctive reading of "both legs must pass" — the outcome is not sensitive
to that construction choice.

**This independently reproduces, for a third time, on the real design's
own official run**: (1) Red Team's Phase-2 audit's own from-scratch Monte
Carlo (`phase2_redteam_audit.md` Attack 4: 5.5×/2.3×/1.7× at α=0.01/0.05/
0.10); (2) QUANTUM OPTICS' original Phase-2 critique (5–6×/2.2–2.6×/1.6–
1.9×); (3) this cycle's own Phase-3 development run (`phase3_synthesis.md`
§4). Three independent implementations (QUANTUM's own from-scratch code,
Red Team's own separate from-scratch code, and this file's committed
`run.py`) now converge on the same leverage-driven miscalibration, to
within Monte-Carlo noise, at `N=20,000`/`K=500`. The mechanism, independently
re-derived twice (QUANTUM, Red Team): `E[Var(R_q^surr)]/Var(R_q^obs) ≈
0.79`, driven by `mean diag(M5) = 26/31 = 0.8387` — the sign-flip
surrogate's own hat-matrix leverage on this small (`n=31, p=5`) design,
not a coding defect in any of the three independent implementations.

Per docket item 3(b), the Combined Verdict emits the named branch
`HALT_NULL_MISCALIBRATED`, not a generic `HALT` — distinguishing this from
`HALT_GRID_MISMATCH`/`HALT_TELESCOPE_MISMATCH`/`HALT_PROVENANCE_MISMATCH`/
`HALT_RECOVERY_FAILED`, none of which fired.

---

## Contamination disclosure (docket items 9–11; not triggered this run, reported per standing requirement)

`results["scored"]["contamination"]["confirm_disclosure_required"] =
false` — no pair reached `RESOLVED`, so the CONFIRM-outcome disclosure
requirement (item 11) does not activate this run. The standing
pre-registration and forward-lock paragraphs (items 9–10, full text in
`NOTES.md` and `phase3_synthesis.md` §6) are computed unconditionally and
recorded in `results.json` regardless, per the same requirement that they
"cannot be omitted by oversight."

`exp072_disclosure` (real, closed, non-gating `A_q`/`χ0` values used only
for the docket-item-5 prose correction) is reported in full in
`results.json`, unchanged from the Phase-3 dev-time regression check
(`χ0`: −0.0197/−0.0203/−0.0062/−0.0434 rad; `tan/sin`: 1.0002–1.0009).
`m0_native` (exp-071's `n_grid=400` slope, `0.0025563909774436134`) and
`m0_resolved` (exp-072's `n_grid=3000`-resolved slope,
`0.002463678368980155`, `R²=0.8328`) both loaded at runtime, matching the
Phase-3 regression check exactly (docket item 6).

---

## What this cycle actually establishes

**Not a T28 physics finding — a genuine, quantified, reusable
methodological result about this instrument class**, per `phase2_
redteam_audit.md` §6's own framing, confirmed correct by this run: **on a
small (`n=31`), leverage-concentrated angular-sweep design fitting a
carrier-conditioned ramp coefficient, a sign-flip/residual-permutation
null built by flipping the full-model (5-column) residual and adding it
to the null-model (4-column) prediction is anti-conservative by roughly
2–6× nominal across the practically relevant α range (0.01–0.10),
independent of noise level, carrier phase, or whether the noise is i.i.d.
or drawn from real captured FDTD residuals.** The mechanism (leverage,
`mean diag(M5)=(n−p)/n=0.8387`) is exact, not data-dependent, and
generalizes to any comparably-sized carrier/phase-conditioned fit — a
direct, load-bearing instance of exactly the class of finding LOGBOOK's
R6 house rule (`G0-e`, adopted on the exp-072 sign-bug precedent) exists to
surface, this time catching a statistical-calibration defect rather than a
sign bug, before any real data was scored.

**T28's own substantive question — what produces the ~2.84° family
periodicity in the `C80−C40` padding delta — is exactly where exp-072 left
it: bounded by window identifiability (the ~1.8°–5.0° leakage band, exp-072
Iteration 49), not advanced and not narrowed by this cycle.** This cycle's
honest contribution is closing three of exp-072's own same-shift-deferred
process gaps (T2-1, T2-3, T2-4) and, in the course of doing so, finding
that the specific null-construction fix (T2-3) those very same seats
proposed does not clear its own pre-registered bar — a real result about
the *method*, not the phenomenon.

---

## Idealizations, unchanged from `NOTES.md`

No idealization changes; nothing here alters constraint-3 scope, T1
applicability (still N/A), or engine trust (still zero FDTD, inherited
from exp-069/071's own already-passed gates). See `NOTES.md` for the full,
unchanged 13-item list.
