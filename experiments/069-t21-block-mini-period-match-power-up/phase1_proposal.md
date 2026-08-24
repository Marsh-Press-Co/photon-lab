# PHASE 1 — PROPOSAL · Panel Iteration 46 · Lead seat: THERMODYNAMICS

*Fresh sub-agent, THERMODYNAMICS charter, per PANEL.md's independence
mechanics. Preserved verbatim as delivered.*

## Candidate exp-069 — Block MINI's Period-Match Test, Powered Up (T21 mechanism-vs-artifact, LOCKED item #1)

### 1. Mechanism narrative (≤300 words)

This is not a new mechanism proposal — it is the LOCKED, unconditional
Iteration-46 mandate (PLAN.md's Iteration-46 queue, item 1; LOGBOOK.md
Iteration 45's CHECKPOINT-4 finding). Block MINI's period-match test
(`P-VIS42-10`, exp-065) is the only instrument this program has ever built
that could distinguish T21's coherent edge-diffraction fringe from a
settling-transient artifact underneath T24's non-monotone `ABSORB`-boundary
systematic — and it has been underpowered on two independent axes since it
was built. First, it sampled only 5 points at 0.5° spacing over ~1.0 T21
period (`P(40°,600nm)=1.989°`) — too sparse to fit a period distinctly from
noise (QUANTUM's own Phase-5 finding, exp-065). Second, it ran at
`STEPS=1400`, which exp-066 later proved unsettled at this exact channel and
these exact angles by 59.8–74.4% — comparable to or larger than the
mini-sweep's own measured peak-to-trough (QUANTUM's own Phase-5 self-catch:
the settling artifact and the T21 fringe share the same geometric clock, so
an unsettled reading cannot discriminate them even in principle). Third, the
code only ever tested the amplitude half of its own pre-registered,
conjunctive REFUTE clause — the period-match half was never implemented
(Red Team's Phase-5 final-audit catch).

This cycle fixes all three at once: a 31-point, 0.2°-step angular scan
spanning 6.0° (≈3.0 T21 periods) at **settled** `STEPS=2800`, on the exact
`C40`/`C80` configs `P-VIS42-10` differences, plus a genuinely-coded,
zero-free-parameter period-match statistic (§4). If `dC_empty(θ) =
C_empty(C80,θ) − C_empty(C40,θ)` is flat, the additive-systematic framing
this program has leaned on since T24 stands confirmed at the power this
program actually owes it. If it oscillates **and** phase-locks to the exact
array-factor period the T21 mechanism predicts, that is a genuine,
decisive finding — not settling noise, since settling is now controlled —
with consequences for every near-threshold constraint-3 citation issued
since Iteration 18. Either outcome closes the LOCKED item for good.

### 2. T1 escape route

**N/A — instrument/model-fidelity re-verification class**, identical in
kind to exp-041 (Iteration 18), exp-065 (Iteration 42), exp-066 (Iteration
43), and exp-068 (Iteration 45). No mechanism is proposed; no σ(I), σ(x,t),
angular-selectivity, or sub-threshold claim is made, touched, or advanced.
Constraint 3 is not directly at stake this cycle.

### 3. Parameter table

**Reused verbatim, zero new code** — exp-065's own `design_geometry.py`
(`CONFIGS["C40"]`, `CONFIGS["C80"]`, `MINI_SWEEP_*` precedent) and `run.py`
(`_one_run`, `_c_empty`, `_sweep_one`, `ProcessPoolExecutor(max_workers=4)`
idiom). **Zero `lab/` diff** — same no-new-machinery position as every T21/
T24/T27 cycle since Iteration 20.

| Knob | Value | Basis |
|---|---|---|
| Configs | `C40` (ABSORB=40, pad=0 — exp-041 geometry verbatim), `C80` (ABSORB=80, pad=40, congruent) | `design_geometry.CONFIGS`, unmodified |
| Wavelength | 600 nm only (`cpl=20`) | matches original `P-VIS42-10`'s own scope; the desk check (exp-069's own `desk_check_settling_delta.py`) found 600nm the cleanest, least-aliased channel of the three (flip-fraction 1.0 vs 0.6/0.8) — the decisive wavelength to power up first, not scope creep into a 3λ redesign |
| θ center / half-span / step | **39.0° / 3.0° / 0.2°** | centered on the original test's own peak-signal region (exp-065 `MINI_SWEEP_CENTER=39.0`); span 6.0° ÷ mean `P(θ)`≈1.98° across the window ≈ **3.03 T21 periods** — an order of magnitude denser than the original 0.5° step |
| θ values (31 points) | 36.0, 36.2, 36.4, …, 41.8, 42.0 | `center + i·step`, `i∈[-15,15]` — includes θ=38.0/39.0/40.0 exactly (existing citable anchors, §5) |
| STEPS | **2800** (settled floor — exp-065's own 4-point convergence trend is flat by 2800; exp-066's P-066-3a/3b independently confirmed generalization along both λ and θ) | not 1400 |
| Block DENSE calls | 31 θ × 2 configs (C40, C80) × 1 λ | **62 new FDTD calls** |
| Block SETTLE-C80 | θ∈{39.0°, 40.0°}, C80, 600nm, **STEPS=4200** | **2 new FDTD calls** — closes the one gap in T27's own settling evidence: `C80` has never had a 3-point convergence check (1400→2800→4200) at any angle, only a single 1400-vs-2800 pair (exp-065's `block_settle`, the 59.8% shift that opened T27). θ=39.0/40.0 chosen because both already have committed `STEPS=1400` values (exp-065 `block_mini`), so this closes the gap at zero extra design cost. |
| **Total** | | **64 new FDTD calls** |

**Cost basis** (exp-065's own measured `design_geometry.CPU_S_PER_CALL`,
4-worker `ProcessPoolExecutor` contention included, linear-in-STEPS scaling
— independently corroborated this cycle by exp-066's own `block_g1ext`
(STEPS=1400) vs `block_main2800` (STEPS=2800) wall-clock ratio, 2.02×,
matching the assumed 2.00× almost exactly):

| Config | 1400-cost | 2800-cost (×2) | 4200-cost (×3) |
|---|---|---|---|
| C40 | 25.0 s | 50.0 s | — |
| C80 | 34.8 s | 69.6 s | 104.4 s |

- Block DENSE CPU: 31×(50.0+69.6) = **3707.6 s**
- Block SETTLE-C80 CPU: 2×104.4 = **208.8 s**
- **Total CPU: 3916.4 s**
- Wall = `OVERHEAD_FACTOR(1.15) × CPU / (N_WORKERS(4) × PARALLEL_EFFICIENCY(0.98))` (exp-065's own formula, `design_geometry.fdtd_budget`) = **1148.9 s ≈ 19.15 min**
- 3× envelope (this program's own budgeting convention): **≈ 57.4 min**
- **Hard stop: 75 min**, with de-scope order if breached: drop Block SETTLE-C80 first (2 calls, cheapest, least load-bearing to the headline), then thin Block DENSE's outer flanks (36.0–37.0° and 41.0–42.0°) to 0.4° step before touching the core 37.0–41.0° window that carries the headline periodicity test.

**Source spec**: `add_line_source(profile="plane", edge=TAPER=40, amplitude=1.0)`,
identical to every prior cycle on this channel — no beam/Gaussian source is
used (Block MINI has never used one; T24's Block BEAM is a separate,
already-closed leg).

### 4. The period-match statistic — committed in advance, not post-hoc

The original `P-VIS42-10`'s REFUTE clause was conjunctive (amplitude AND
period-match) but the code only ever tested amplitude (QUANTUM's Phase-5
catch, exp-065 `run.py:562-604`). This cycle implements the missing half
properly, using the **exact** periodicity T21's own array-factor mechanism
predicts rather than a locally-approximated constant:

For a two-edge/aperture Huygens diffraction pattern, the physically correct
periodic variable is **`sin θ`**, not `θ` linearly — path-length difference
across the half-aperture `A` is `A·sinθ`, so the fringe repeats exactly
every `Δ(sinθ) = λ_cells/A = cpl/A` (a **known constant**, `20/752 =
0.0265957`, not fit). This is not a new idealization: differentiating
`P(θ)=λ/(A·cosθ)` (T21's own established formula, LIVE THREADS) confirms
`d(sinθ)/dθ = cosθ` reproduces `P(θ)` exactly as the local, first-order
approximation of this exact global period — i.e. §4's statistic is a
strictly more rigorous version of the same, already-established quantity,
not a different one.

**Primary, pre-registered statistic**: fit
`delta(x) = c₀ + a·cos(2πx/T) + b·sin(2πx/T)`, `x = sinθ`, `T = cpl/A =
0.0265957` **fixed** (zero free period parameters — an ordinary 3-parameter
linear least-squares fit, always well-posed, no nonlinear-fit convergence
risk), against the 31-point `delta(θ) = C_empty(C80,θ) − C_empty(C40,θ)`
series. Report `R²` of this fit against the flat-null (`delta = c₀` alone).

**Secondary, diagnostic-only cross-check** (reported, not gating — avoids
citing an unconstrained nonlinear fit as if it were a pre-registered band,
the R4-adjacent risk QUANTUM's own critique flagged): grid-search the
best-fit period `P*` over `θ∈[1.0°,4.0°]` and report `|P*−P(39°)|/P(39°)`.

### 5. Predictions — to be committed to git BEFORE the run (house discipline)

| ID | Claim | CONFIRM | REFUTE |
|---|---|---|---|
| **P-069-G1** | Absolute identity gate. θ∈{38.0°,40.0°}×{C40,C80}×600nm×STEPS=2800 reproduce `experiments/065-.../settled_sweep_steps2800_diagnostic.json` exactly (all 4 already-committed values, loaded programmatically). | `ΔC = 0.0` for all 4 (float64 equality) | any nonzero Δ — halts the cycle before anything else is trusted |
| **P-069-1 (HEADLINE)** | Amplitude clause. `ptp/\|mean\|` of `delta(θ)` over the 31-point window. | `ptp/\|mean\| ≤ 1.5` | `ptp/\|mean\| > 2.5` |
| **P-069-2 (HEADLINE)** | Period-match clause (§4 primary statistic), fixed T=0.0265957 in `sinθ`. | `R² ≤ 0.15` (no locked periodic structure) | `R² ≥ 0.50` |
| **Combined verdict** | Both P-069-1 and P-069-2 REFUTE together ⇒ **coherent-fringe perturbation, decisively established at settled STEPS** — T24's boundary systematic is real physics, not additive noise, and not settling. Both CONFIRM together ⇒ **additive-systematic framing vindicated at proper power** — the "cancels to first order" premise stands. Any other combination (including either alone crossing REFUTE without the other) ⇒ **PARTIAL**, reported as such, not forced into either mechanism claim — this is the honest resolution of a conjunctive test, not a weaker version of it. | | |
| **P-069-3 (secondary, diagnostic)** | §4 secondary statistic. | `\|P*−P(39°)\|/P(39°) ≤ 20%` | `≥ 50%`, or no `P*` in `[1.0°,4.0°]` clears `R²≥0.30` |
| **P-069-4** | Settling closure for `C80`/600nm (Block SETTLE-C80), mirroring exp-066's own P-066-3a/3b convention. `\|ΔC(4200−2800)\|` at θ∈{39.0°,40.0°}, relative to `\|ΔC(2800−1400)\|` at the same cells (1400 values reused from exp-065's committed `block_mini`). | ≤ **1%** at both cells (STEPS=2800 is genuinely settled for `C80`, not just "less unsettled than 1400") | ≥ **5%** at either cell — STEPS=2800 is not settled for `C80` either, and P-069-1/2's own 2800-STEPS data must then be reported as bounded by this uncertainty, not trusted outright |

**Checkpoint-criterion-2 candidacy: none.** No mechanism class is bounded
here — this is instrument closure. What this cycle *can* produce, per its
own LOCKED status, is the retirement of a three-(or-four)-cycle-old
citation-tripwire-only treatment, in either direction.

### 6. Idealizations

1. **2D TMz, single polarization** — inherited from every prior cycle on
   this channel.
2. **600 nm only.** The original `P-VIS42-10` was also 600nm-only; the desk
   check (exp-069, zero-cost, already committed) found 600nm the least
   aliasing-prone of the three established wavelengths at 1° sampling
   (flip-fraction 1.0 vs 0.6/0.8). A 450/750nm generalization of this same
   design is a disclosed, natural follow-up — not run this cycle, to avoid
   scope-creep into a 3× cost redesign of an already-locked, narrowly-scoped
   item.
3. **Positive θ branch only (36°–42°)**, matching Block MINI's own original
   scope — not a symmetry test. `±θ` magnitude asymmetry is a live,
   separate T21 sub-finding (staircasing contribution), not this cycle's
   question.
4. **`C40`/`C80` only** — the two configs `P-VIS42-10` was built to
   difference. `C60`/`C70`/`N60` (T24's own aliasing/naive-protocol
   diagnostics) are not re-run; nothing here re-opens T24's own headline,
   which is a separate, already-scored question (exp-065 P-VIS42-2).
5. **The period-match statistic (§4) treats T21's established
   `P(θ)=λ/(A·cosθ)` mechanism as the null hypothesis being tested**, not
   as ground truth — a REFUTE-band pass confirms consistency with that
   specific, pre-existing, independently-derived mechanism (T21, Iteration
   18, EM's zero-free-parameter model), not an arbitrary "some periodicity
   exists" claim. A different, unmodeled periodic mechanism at a different
   period would show up as a low `R²` here and require separate
   investigation — disclosed, not claimed to be ruled out by this design.
6. **Bench scale only** (r=78 cells) — no witness-scale claim.
7. **`A=752` is held fixed and unverified anew this cycle** — inherited
   from exp-065's own congruent-construction identity (G-2, already passed
   at 0.000e+00); not re-gated here since neither `C40` nor `C80`'s geometry
   changes.
8. **Incoherent post-hoc angular summation** — N/A this cycle; every row is
   a single-angle `C_empty`, not an N9/N17 aggregate. T25/T26 do not apply.

### 7. Gates

Full bench (`lab/validation/run_all.py`, the same stage set exp-065/066/068
verified — no new `lab/` diff, `run.py`'s own `assert_lab_clean()` idiom
reused verbatim) green before and after. Binding stages: 1 (angle_deg=0
bit-exactness), 6 (phasor conventions), 9 (the ambient instrument itself),
17 (`c_thr`, cited but not scored — this cycle scores no percept). One
local absolute-identity gate, **G-1 (P-069-G1)**, gates every other number
— the same "nothing downstream is trusted until the harness reproduces a
prior committed value bit-exact" discipline as exp-065's G-1/exp-066's
G-1′.
