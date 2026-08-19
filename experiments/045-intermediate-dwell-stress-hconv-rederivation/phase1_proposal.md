**SUPERSEDED — see `NOTES.md` Phase 3 (`phase2_redteam_audit.md` Attack 4):
Block B's material identity below (PMMA) was found wrong for what Block A's
own grid models AND its citation fabricated (no PMMA mention anywhere else
in this repo) — corrected to silicon in the actually-committed
`run.py`/`results.json`. Block B's `h_eff`/`mass_kg` length-scale pairing
below also mixed two different characteristic lengths (Attacks 1–2) —
corrected to two genuinely self-consistent regimes. This file is preserved
UNEDITED below as the historical record of what Phase 1 actually proposed
and Phase 2 actually critiqued (T10's "flag, don't rewrite" convention,
extended here to a Phase-1 draft for the first time — see NOTES.md's
explicit override statement).**

# Phase 1 proposal — "The Intermediate-Dwell Coupled Kinetics-Thermal Stress Sweep + h_conv/mass_kg Re-derivation" (candidate exp-045)

# PHASE 1 — PROPOSAL · Panel Iteration 22 · Lead seat: ELECTROMAGNETISM

## Scope decision (stated up front)

Two blocks, bundled under exp-034's own precedent for "tightly-related,
all-zero-cost, all-desk/analytic items": both consume the SAME two inputs
(exp-044's 16-point host/ratio grid; the witness-scenario `dt_ss_full`/
`tau_thermal_s` reference pair) and produce the SAME output shape (a
`tau_thermal_s`-dependent stress test), not two independent charters
stapled together.

- **Block A — Priority #1** (EM+THERMO+PHOTONICS convergent Iteration-21
  pick, this seat's own native T22/coupled-ODE charge): sweep
  `coupled_kinetics_thermal_dT` across dwell/τ ratios spanning 0.1×–10× of
  BOTH τ_kinetics and τ_thermal, all 16 host/ratio points, including
  Host D's own under-converged corner explicitly.
- **Block B — Priority #2** (THERMODYNAMICS' own self-imposed floor, now
  due; bundled with this seat's own T22 area-table obligation): re-derive
  `h_conv` (gas-phase conduction) and `mass_kg` (density × the
  `iso_xsec_sq` idealized volume) from first principles, and commit the
  geometric-disk-vs-`iso_xsec_sq` area comparison table.

**Deferred, stated reason:** **Block C**, QUANTUM's repeated-sweep/dose-
accumulation kinetics test (`pulse_train_segments`, Iteration-22 priority
#3) — QUANTUM OPTICS' own native charge. This cycle already delivers two
substantial, well-developed analytic blocks (A: a 4-regime × 2-axis ×
16-point dwell sweep, 1664 points; B: a from-first-principles re-
derivation). Choosing a physically-motivated sweep-rate/inter-pulse
interval for Block C is a QUANTUM-native judgment call, not an
EM-appropriable arithmetic swap — the same reasoning MATERIALS gave
Iteration 21 for deferring items #2/#3 (this cycle's own A/B) to their
native seats. The Iteration-18/20/21 non-native-lead precedent covers a
seat's own **#1**-ranked item being run non-natively; it does not
mechanically extend to ALSO absorbing a **#3** item onto an
already-two-block cycle. QUANTUM OPTICS leads again at Iteration 24, two
cycles away — not an open-ended deferral, and QUANTUM's own separate
Checkpoint-4 tripwire (the aperture-consistent beam check, a THIRD
deferral) is untouched by this decision either way.

---

## 1. Mechanism / instrument-fidelity narrative (≤300 words)

**This is an INSTRUMENT-CHARACTERIZATION cycle, not a new material
mechanism proposal — T1 escape route: NONE, per Iteration-20's own
precedent for docket #7/`thermo_sidecar.py`.** Neither block proposes,
tests, or revises a σ(I)/σ(x,t)/angular/sub-threshold escape route; both
correct or stress-test the analytic thermal/kinetics bookkeeping already
attached to the existing σ(I) ON-endpoint article.

**Block A.** exp-044 answered "does the decoupled two-stage shortcut
(ceiling × n_at_dwell) match the exact coupled kinetics-thermal ODE?" at
exactly ONE dwell — the witness central value, 66.7 ms — against all 16
grid points. Because τ_kinetics spans 11 orders of magnitude across the
grid (10⁻⁹ s at Host A to ~0.1 s at Host D) while τ_thermal is
essentially fixed (~1.4 ms), that single dwell landed deep in comfortable
clearance (dwell/τ_kinetics ≥ 66×) for Hosts A/B/C, and only barely
inside the untested corner for Host D (dwell/τ_kinetics ≈ 0.67–0.73×) —
never a deliberately swept regime. This block sweeps dwell itself, as
R×τ_kinetics and (separately) R×τ_thermal for R∈[0.1,10], reusing
`coupled_kinetics_thermal_dT` (Red Team's already-verified closed form)
unmodified — no new engine, no new physics, only a finer grid over an
input the existing machinery already accepts.

**Block B.** `h_conv=5.0 W/(m²K)` (macroscopic natural convection) and
`mass_kg=1.0×10⁻¹⁵ kg` (an arbitrary placeholder since exp-032) are
replaced with values derived from the object's own bench geometry:
gas-phase conduction (`h_eff=k_air/r_out`) and density×volume, using the
SAME `iso_xsec_sq` compactness idealization the module already applies to
area, extended to a volume for the first time.

## 2. Parameter table

### Block A — intermediate-dwell coupled-ODE sweep

| Input | Value | Source |
|---|---|---|
| Host/ratio grid (reused verbatim) | Hosts A(k_r=1e9)/B(1e6)/C(1e3)/D(1e1) × RATIOS {1e-9,1e-5,1e-3,1e-1} = 16 points | `experiments/044/run.py::HOSTS,RATIOS` |
| Dwell sweep axis K | dwell = R × τ_kinetics(host,r), R ∈ 13-pt log grid [0.1, 10] (6 pts/decade) | new this cycle |
| Dwell sweep axis T | dwell = R × τ_thermal(regime), same R grid | new this cycle |
| τ_thermal regimes (4, run in parallel) | (i) uncorrected, 1.3772×10⁻³ s; (ii) T22-area-only ×2.9; (iii) T22-area-only ×3.0; (iv) Block B's fully-corrected (h_conv+mass+area), 5.260×10⁻⁴ s | exp-043/044 (i–iii); this cycle (iv) |
| Reference ceiling `dt_ss_full` | 3.9436×10⁻³ K (regimes i–iii) / 3.598×10⁻⁶ K (regime iv, h_conv-corrected) | exp-043/044; this cycle |
| Sweep size | 16 pts × 4 regimes × 2 axes × 13 R = 1664 points | — |
| Coupled-ODE solver | `coupled_kinetics_thermal_dT` (Red Team, Iteration-21 Phase 2), reused **verbatim** | `experiments/044/run.py` |
| NETD band | (0.020, 0.050) K | exp-043 P-D7-4 |

### Block B — h_conv / mass_kg re-derivation + T22 area table

| Quantity | Old (placeholder) | New (derived) | Formula / source |
|---|---|---|---|
| `h_conv` | 5.0 W/(m²K) (macroscopic natural convection) | **11,111.1 W/(m²K)** | h_eff = k_air/r_out, k_air=0.026 W/(m·K) (textbook, room temp), r_out=R_OUT_CELLS×dx=78×30nm=2.34µm |
| `mass_kg` | 1.0×10⁻¹⁵ kg (arbitrary) | **4.186×10⁻¹³ kg** (PMMA) / 3.547×10⁻¹³ kg (water, disclosed bound) | density × w³, w=σ_ext,ON×dx=7.079µm (iso_xsec_sq width, extended to a cube — NEW idealization, see §5); density_PMMA=1180 kg/m³ (stated assumption) |
| Geometric-disk area | — | 1.7202×10⁻¹¹ m² | π×(78×30nm)² |
| `iso_xsec_sq` area, ON endpoint | — | 5.0112×10⁻¹¹ m² | (σ_ext,ON×dx)², σ_ext,ON=235.967 cells |
| `iso_xsec_sq` area, flagship absorber | — | 5.1843×10⁻¹¹ m² | (σ_ext,ABS×dx)², σ_ext,ABS=240.007 cells |
| Area ratio, ON endpoint | — | **2.9131×** | matches T22's established 2.9–3.0× |
| Area ratio, flagship absorber | — | **3.0138×** | matches T22's established 2.9–3.0× |
| `dt_ss_full` (h_conv corrected only) | 3.9436×10⁻³ K | **3.598×10⁻⁶ K** (1096× drop) | mass-invariant (PHOTONICS' proof, reused) |
| `tau_thermal_s` (h_conv + mass fully corrected) | 1.3772×10⁻³ s | **5.260×10⁻⁴ s** (0.382× — SHRINKS) | see §4 for why |

## 3. T1 escape-route statement

**None — pure instrument/model-fidelity characterization.** Per
Iteration-20's own precedent for docket #7/`thermo_sidecar.py`, neither
block proposes, tests, or revises a T1 escape-route mechanism. Both
stress-test or correct analytic bookkeeping already attached to the
existing, unmodified σ(I) ON-endpoint article.

## 4. Falsifiable predicted outcomes

All numbers below are computed from the closed-form algebra of
`coupled_kinetics_thermal_dT` (verified by hand-deriving the same bracket
identity independently and cross-checking against ~1600 points of
pure-Python arithmetic before this proposal was written — not fabricated
after the fact) — `run.py`'s own independent evaluation of the SAME
already-verified function must reproduce them to displayed precision.

- **P-EM45-A1 (global UNDETECTABLE survives the whole swept regime):**
  the maximum `exact_coupled_dT_K` anywhere across all 1664 points is
  **3.585×10⁻⁴ K**, occurring at the LARGE-R end of axis T for Hosts
  A/B/C (regimes i–iii, all three converge to the same n_ss=0.0909
  ceiling there; Host D does not reach it on axis T — its own τ_kinetics
  is too slow relative to R×τ_thermal at R≤10) — **55.8× below
  `netd_lo`=0.020K**, identical to
  exp-044's own already-published worst-case margin. **No point in this
  sweep reads DETECTABLE or MARGINAL.** This follows from a structural
  bound, not luck: the coupled system is a cascade of two real-pole
  (non-oscillatory) first-order relaxations, so `DT(t)` approaches its
  ceiling `dt_ss_full×n_ss` monotonically from below with no overshoot —
  intermediate dwell can only produce LESS ΔT than the already-published
  ceiling, never more. **Falsification condition:** any point exceeding
  `dt_ss_full(regime)×n_ss_max` (n_ss_max=0.0909 at r=1e-1) by more than
  10⁻⁹ relative would mean this monotonicity argument is wrong — a real
  surprise, not a rounding matter.
- **P-EM45-A2 (Host D axis-K curve, the genuinely new headline):** for
  Host D (all 4 ratios), relative difference on axis K **decreases
  monotonically** from **15.3–17.1%** at R=0.1 through **1.44–1.50%** at
  R≈0.67–0.73 (reproducing exp-044's own single published point) down to
  **≤7×10⁻⁷** at R=10. Predicted band at R=0.1: [0.10, 0.25]; at R=1:
  [0.006, 0.012]; at R=10: [1×10⁻⁸, 1×10⁻⁵].
- **P-EM45-A3 (Host-D witness-dwell consistency check):** the sweep's own
  axis-K point nearest R=0.667–0.733 must reproduce exp-044's published
  1.44–1.50% figure at all 4 Host-D ratios (an internal-consistency
  regression, not a new physics claim) — **CONFIRMED if all 4 land in
  [0.0144, 0.0150]**, else a real regression in either this cycle's or
  exp-044's own arithmetic.
- **P-EM45-A4 (axis-K short-dwell blowup for Hosts A/B/C is a benign
  artifact, not new physics):** at R=0.1 on axis K, relative difference
  will read **≥10× (1000%)** for Hosts A, B, and C — orders of magnitude
  apparently "worse" than Host D's own worst point — while the
  ABSOLUTE ΔT there stays ≤10⁻⁵ K, itself ≥2000× below `netd_lo`. This is
  predicted and disclosed in advance specifically so it is not later
  mistaken for a stress-test failure: it is the well-known relative-error
  divergence of comparing an O(t) approximation against an O(t²) exact
  solution as both vanish. **Falsification condition:** if the ABSOLUTE
  ΔT at these points is NOT comfortably sub-NETD, that changes the
  read entirely — P-EM45-A1 already commits to checking this globally.
- **P-EM45-A5 (T22-area-only correction, extended beyond Host C for the
  first time):** applying the established 2.9–3.0× inflation factor to
  τ_thermal alone (regimes ii/iii), holding `dt_ss_full` fixed, changes
  the worst-case rel_diff on axis T by **≤10% relative** at every host
  (a mild, not qualitative, shift) — the area convention alone does not
  flip any UNDETECTABLE verdict, extending exp-044's own Host-C-only
  finding to Hosts A/B/D for the first time.
- **P-EM45-A6 (Block A × Block B interaction — the headline synthesis):**
  Block B's FULLY-corrected τ_thermal (5.260×10⁻⁴ s) is **SHORTER**, not
  longer, than the uncorrected value (1.3772×10⁻³ s) — factor **0.382×**
  — despite mass_kg growing ~419×, because `h_eff`'s ~2222× nominal
  growth is damped to an actual ~1096× `dp_dt` growth (the radiative term,
  ~5.1 W/(m²K), is comparable in size to the old placeholder h_conv=5.0,
  not negligible next to it) and this dominates the mass increase. Net
  effect: dwell/τ_thermal(fully-corrected) = **126.7×**, MORE comfortable
  than both the uncorrected (48.4×) and the T22-area-only-corrected
  figure exp-044 reported (16.1–16.7×, the one that dropped BELOW
  `N_TRANSIENT_TAU`=25). **The properly-derived correction relieves, not
  worsens, T22's own remaining concern** — the isolated area-inflation
  reading exp-044 flagged as pushing convergence margin below 25× turns
  out not to survive contact with a correctly-derived `h_conv`.
  **Falsification condition:** landing outside [100×, 160×] for the
  fully-corrected dwell/τ_thermal ratio would mean this interaction
  doesn't hold as cleanly as predicted.

## 5. Idealizations

- **Block A** reuses `coupled_kinetics_thermal_dT` verbatim from
  `experiments/044/run.py` — not re-derived, not re-verified against
  `scipy.integrate.odeint` this cycle (exp-044's own <4×10⁻⁴
  relative-error check against that reference, at its 16 tested points,
  is the standing verification; this cycle's 1664 points are NOT
  independently checked against `scipy` — a disclosed gap, not hidden).
  No new trust-suite stage is added (see run.py's own docstring for the
  explicit scope justification, mirroring exp-044's own precedent for the
  same function) — three lightweight in-script identity assertions
  (h_eff×r_out=k_air; mass=density×volume; the monotone-ceiling bound)
  substitute for a formal gate this cycle. Reopening that scope choice is
  fair game at Phase 2.
- The short-dwell relative-error blowup (P-EM45-A4) is flagged explicitly
  as an artifact of the metric, not the physics — a judgment call this
  seat is making before the run, open to Phase-2 challenge if Red Team
  reads it differently.
- **Block B**'s `k_air=0.026 W/(m·K)` is a textbook room-temperature air
  value, not independently re-sourced this cycle — T18's WebFetch
  blockage (still confirmed, per every prior cycle since Iteration 13)
  means this is carried, not verified, exactly like exp-044's own
  H_CONV_KNOWN_CORRECTION_NOTE already disclosed.
- **`density_PMMA`=1180 kg/m³ is a STATED assumption, not sourced this
  cycle** — chosen because PMMA is the most commonly cited photochromic-
  dye host polymer in this program's own prior literature surveys
  (T17/T18, exp-036/037), not because any witness-scenario material has
  been identified. Water (1000 kg/m³) is reported alongside as a
  disclosed lower-density bound — the two differ by only 18%, small next
  to every other uncertainty in this chain.
- **The volume convention `w³` (cube) is a NEW idealization this cycle**,
  not inherited from any prior committed code — it extends
  `iso_xsec_sq`'s own area convention (`w²`, "compact, not infinite rod")
  to a volume by assuming the SAME compactness along the invariant axis.
  A finite-rod-length convention (volume = w²×L for some stated L≠w)
  would scale `mass_kg`, and hence `tau_thermal_s`, linearly in L/w — not
  tested here, a candidate follow-up if this convention is challenged.
- The area-convention recommendation in Block B's table ("keep both,
  scoped per-branch") is a judgment call, not a proof — Red Team or any
  seat may argue for a single winner at Phase 2.
- `h_eff=k_air/r_out` is itself an idealization (a simple conduction
  estimate through a shell of thickness ~r_out, not a solved boundary-
  value problem, no Knudsen-number/mean-free-path correction at this
  ~µm scale, disclosed as "the correct REGIME, not a converged number,"
  matching exp-044's own H_CONV_KNOWN_CORRECTION_NOTE framing).
- Both blocks add **zero new FDTD calls** and **zero new engine code** —
  pure reuse of already-gated (`lab.kinetics` stage 12, `lab.thermo_sidecar`
  stage 15) and already-verified (exp-044's closed form) machinery.
- NETD is an instrument/detector threshold, not a human perceptual one
  (VISION's standing mandatory disclaimer) — nothing in either block
  bears on constraint-3/4's human-eye verdict.

---

**Files read to ground this proposal:** `PANEL.md`, `LOGBOOK.md` (full),
`PLAN.md` ("Current state" section), `lab/kinetics.py`,
`lab/thermo_sidecar.py`, `experiments/043-docket7-thermo-sidecar/
{NOTES.md,run.py,results.json}`, `experiments/044-realistic-host-
kinetics-realizability-amendment4/{NOTES.md,phase1_proposal.md,run.py,
results.json}`.
