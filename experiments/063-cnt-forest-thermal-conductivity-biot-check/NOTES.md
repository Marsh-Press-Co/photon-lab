# exp-063 — The Real Candidate Material's Own Thermal Conductivity, and
# Whether It Still Licenses a Lumped-Capacitance ΔT

**Panel Iteration 40.** Lead: THERMODYNAMICS, by rotation. T1 escape
route: **N/A** — a literature/analytic realizability-and-instrument
continuation, the exp-036/037/054/060/061/062 class: zero constraint-
1/2/3/4 metric scored, zero FDTD. Full five-phase panel cycle: Phase 1
proposal → five blind Phase-2 critiques (all support-with-changes,
PHOTONICS/MATERIALS/ELECTROMAGNETISM independently triangulating on
Section 4's boundary-condition/length-scale model) + Red Team audit
(PROCEED-WITH-MANDATORY-FIXES; **no Checkpoint criterion fires** — see
`phase2_redteam_audit.md` §3/§5) → this Phase-3 synthesis, predictions
frozen before Phase 4 → Phase 4 (WebSearch) → Phase 5. Full process
record: `phase1_proposal.md`, `phase2_critique_{photonics,materials,em,
quantum,vision}.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`
(this cycle's Director synthesis, all in this directory).

Also this cycle, as a mandatory-fix docket item: `lab/thermo_sidecar.py`
gains `biot_number` and `front_surface_conduction_correction`, promoting
the informal Iteration-22/23 Biot arithmetic to trust-suite-gated code
(stage 23, 4/4 green — see `lab/validation/VALIDATION.md`). Full bench
78/78 unaffected by anything else.

---

## Hypothesis

Every THERMO-sidecar UNDETECTABLE verdict this program has ever issued —
`graded_black_shell_flagship`'s bench-scale 699.27× margin (exp-057) and
exp-061's own freshest, thinnest-ever witness-scale margins (1.35×–3.79×,
MP-5's found thickness range) — computes steady-state ΔT from a **lumped**
(uniform-temperature) model whose internal SOLID thermal conductivity
`κ_solid` never enters the sidecar's own committed code at all. Every
informal Biot-number check this program has run to gauge whether "uniform
temperature" is even valid (Iteration 22 Attack 6, Iteration 23's own
Maxwell-Garnett table) used silicon's κ=148 W/(m·K) — flagged `ASSUMED`,
unsourced (T18), since Iteration 25 — a generic placeholder chosen before
this program's own realizability line (exp-052→061→062) pinned the actual
candidate material class: a CNT-forest/Vantablack-type coating, well
documented as a POOR through-thickness conductor (weak inter-tube
contacts).

**Hypothesis, stated for falsification:** does the *correct* material's
κ still license the lumped assumption every committed margin rests on, or
does absorbed power pile up at the illuminated surface faster than a poor
conductor can spread it — producing a peak surface ΔT above the sidecar's
own uniform-body estimate? Section 4 (below) derives a closed-form answer
at zero new FDTD cost; Phase 4 sources κ_CNT-forest for the first time to
evaluate it.

---

## Setup — parameter table (unchanged from Phase 1; EM independently
re-derived and confirmed every number to the printed digit, no defect
found)

| Knob | Value | Source / status |
|---|---|---|
| `k_air` | 0.026 W/(m·K) | established bench constant (exp-045/run.py:194), unchanged |
| Radiative linearization | `4·ε·σ·T_amb³`, ε=0.9, T_amb=293.15K, σ=5.670374419×10⁻⁸ W/(m²K⁴) | established bench constants (`thermo_sidecar.SIGMA_SB`), unchanged |
| Silicon proxy (superseded, for comparison only) | ρ=2330 kg/m³, C_p=700 J/(kg·K), κ=148 W/(m·K) | `ASSUMED` — unsourced (T18); the object of this cycle's correction, not reused as ground truth |
| **κ_CNT-forest (through-thickness/axial)** | predicted band [0.1, 20] W/(m·K), central ≈2 W/(m·K) | **Phase-4 WebSearch target** — see Phase 1 §6 for the committed query list |
| Bench-scale geometry (`graded_black_shell_flagship`) | `L=l_geometric_m=r_out=78 cells × 30nm = 2.34×10⁻⁶ m`; `P_abs=1.7409×10⁻¹² W` (exp-057, unchanged) | exp-043/057, established, reused verbatim |
| Witness-scale geometry (exp-061's MP-5 disposition) | `L∈{331.2, 429.1, 538.6, 1051.2} µm` at MP-5 multiples {230×,298×,374×,730×}; margins {3.79×,2.98×,2.42×,1.35×} vs NETD-lo=0.020K | exp-061 THERMO disposition, established, reused verbatim |
| NETD band | (0.020, 0.050) K | exp-043 docket #7, sourced, unchanged |
| **New code, built this cycle** | `lab/thermo_sidecar.py::biot_number(k_air, k_solid)`, `front_surface_conduction_correction(k_air, l_geometric_m, k_solid, emissivity, t_ambient_k)` | trust-suite stage 23, 4/4 green (absolute identity, two regression anchors, the κ_critical falsification-boundary identity) |

**NETD/human-eye disclaimer (mandatory fix 1, applies to EVERY
classification-adjacent number in this document, stated here once at the
top of the predictions AND repeated inline at TD-3/TD-4/TD-5 below):**
NETD is an instrument/detector threshold, not a human perceptual one — no
classification in this document (UNDETECTABLE/MARGINAL/DETECTABLE) bears
on constraint-3/4's human-eye verdict (panel Iteration 20 origin,
`thermo_sidecar.netd_disposition`'s own hard-coded text, reaffirmed here).

---

## The closed-form front-surface correction — now a BRACKET, both
boundary conditions (mandatory fix 5, MATERIALS' flip condition)

Phase 1's Section 4 modeled absorbed power entering uniformly at the
illuminated front surface, conducting the full thickness `L` through
`κ_solid`, and leaving ONLY at the far (rear) boundary — asserted, not
derived, as the geometry's worst case. MATERIALS' Phase-2 critique
(independently confirmed by Red Team, `phase2_redteam_audit.md` attack 4)
found this may not be the true worst case for the program's own candidate
deployment: a real coating is grown ON a substrate (root-bonded), with
the growth axis exposed to ambient at the tip — a loss channel
co-located with the SAME front face where `α_true`'s ~174nm e-folding
means absorbed power actually lands (a real, thin-e-fold optical
absorption profile, not the geometric front/rear split Section 4's model
draws). A front-colocated-loss variant needs no new code: it is exactly
`mixed_length_scale_regime`'s own unmodified `dt_ss_full_K` —
**correction_factor ≡ 1 identically, for any κ_solid.**

Every TD-3/4/5 prediction below therefore reports a **bracket**:
`[front-colocated-loss endpoint (factor=1, = the ORIGINAL, unmodified
margin), rear-only-loss endpoint (Section 4's worst-case formula)]` — not
a single "the" corrected number, until the substrate-interface question
is resolved (queued, not resolved this cycle — see Next).

Two further disclosed, unresolved caveats on the rear-only endpoint
specifically (neither changes its arithmetic, both bound how literally to
read it):

- **Generation-side geometry (mandatory fix 4, PHOTONICS' flip
  condition, confirmed by Red Team attack 3):** at BENCH scale, `L=r_out`
  is reused for a role — the absorption-to-loss-surface conduction
  distance — that `gas_conduction_h_eff`'s own docstring never licenses,
  and it contradicts the established T9 radial-absorption ledger
  (`graded_black_shell`'s conductivity peaks at `r_in`, is zero at
  `r_out` — essentially all absorption lands deep in the shell, not at
  the "front surface" the model names). Numerically inert for TD-3/TD-4
  specifically (Red Team's own recomputation: `Bi_rad` is 3–4 orders of
  magnitude below `Bi_gas` at bench scale, at every κ in TD-1's band), so
  this caveat does not move the bench-scale bracket — but PHOTONICS'
  directional read (a corrected generation length would likely SHRINK,
  not grow, the correction) means it does not threaten TD-4 either.
- **Length legitimacy at witness scale (mandatory fix 6, EM's flip
  condition, confirmed by Red Team attack 5):** the witness-scale `L`
  values (331.2–1051.2µm) are exp-061's MP-5 figures — a thickness
  `t=τ_true/α` BACK-CALCULATED from a sourced optical absorption
  coefficient, not a directly measured geometric length. This is exactly
  the class of length `gas_conduction_h_eff`'s own docstring bars from a
  conduction-length role ("NEVER an optical/extinction-derived length"),
  flagged and explicitly deferred, unresolved, at both Iteration 38 and
  Iteration 39 on this identical `l_geometric_m` lineage. **TD-5's
  rear-only bracket endpoint is therefore conditional on that length
  being licensed — not yet a clean, self-contained finding.** The
  resistance-network algebra itself is agnostic to what `L` physically
  means (EM's own point); what is unresolved is whether 1051.2µm is the
  right `L` to plug in at all.

Computed by direct invocation, reproduced by `lab/validation/run_all.py`
stage 23 as a permanent regression anchor (4/4 green):

```
kappa=20.0 W/mK: Bi_gas=0.00130  CF(bench,L=2.34um)=1.0013  CF(MP5-730x,L=1051.2um)=1.0016
kappa=2.0  W/mK: Bi_gas=0.01300  CF(bench)=1.0130            CF(MP5-730x)=1.0157
kappa=0.5  W/mK: Bi_gas=0.05200  CF(bench)=1.0520            CF(MP5-730x)=1.0628
kappa=0.1  W/mK: Bi_gas=0.26000  CF(bench)=1.2601            CF(MP5-730x)=1.3141
```

`κ_solid` at which the rear-only bracket endpoint alone drives the
MP-5/730× margin to exactly 1.0×: **κ_critical ≈ 0.0897 W/(m·K)**
(stage 23 gate 3, bisection-verified) — just below TD-1's own predicted
band floor. **The front-colocated bracket endpoint never crosses 1.0×,
for any κ_solid** (correction_factor≡1 by construction) — the possible
DETECTABLE flip is a property of the rear-only worst-case boundary
condition specifically, not of both brackets.

---

## Falsifiable predictions — AMENDED, committed BEFORE Phase 4 search
runs (mandatory-fix docket items 1, 5, 7, 8 applied; items 2/3/4/6 are
disclosures/registry entries applied elsewhere in this record, not
predictions-table edits)

**η_thermal≡1 idealization (mandatory fix 7, QUANTUM's flip condition):**
every prediction below reuses `P_abs` (a classically-measured absorbed-
OPTICAL-power figure, exp-057/061, unchanged) as the lattice HEAT power
driving Section 4's conduction chain — i.e. assumes unity thermal-
conversion efficiency, zero radiative/photoluminescent loss channel. For
the CNT-forest/graphitic-carbon material class this cycle sources κ for,
this is standard and well-justified (sub-picosecond electron-phonon
relaxation, negligible photoluminescence quantum yield in graphitic/
semi-metallic carbon) — but it is a stated assumption, not a measured
quantity, and the first cycle to source any material-specific constant
for the actual candidate identity is the natural place it was owed.

| # | Claim | Predicted outcome | Falsification condition |
|---|---|---|---|
| **TD-1** | Sourced κ_CNT-forest (through-thickness/axial) | Band [0.1, 20] W/(m·K), central ≈2 W/(m·K) | Falsified if sourced figures cluster above 50 W/(m·K), or scored INCONCLUSIVE if no axial figure exists |
| **TD-2** | Bi_gas = k_air/κ_solid | Band [0.0013, 0.26], central ≈0.013 | Falsified if outside [0.0005, 1.0] |
| **TD-3** | Front-surface correction factor, flagship bench geometry (L=2.34µm) — **bracket, both boundary conditions; NETD is an instrument threshold, this table row bears on no human-eye/constraint-3 verdict** | **[1.0 (front-colocated-loss endpoint), 1.001–1.26 (rear-only-loss endpoint, across TD-1's κ band)]** | Rear-only endpoint falsified if it exceeds 2× (would mean the bench-scale UNDETECTABLE classification is genuinely at risk, not merely tightened) |
| **TD-4** | Corrected flagship margin (699.27× ÷ TD-3's bracket) — **NETD is an instrument threshold, this table row bears on no human-eye/constraint-3 verdict** | **[554.92×–698.36× (rear-only endpoint, across TD-1's κ band), 699.27× (front-colocated endpoint, = the ORIGINAL unmodified margin)]** — stays UNDETECTABLE at every point in the full bracket | Falsified (classification-relevant) only if the WORST-CASE (rear-only) bracket endpoint drops below 100× anywhere in the sourced κ range |
| **TD-5** | Corrected exp-061 witness-scale margin at the MP-5/730× point — **bracket; conditional on the length-legitimacy caveat above; NETD is an instrument threshold, this table row bears on no human-eye/constraint-3 verdict** | **[1.0274×–1.3479× (rear-only endpoint, across TD-1's κ band), 1.35× (front-colocated endpoint, = the ORIGINAL unmodified margin, which NEVER crosses 1.0× for any κ_solid)]** | The rear-only endpoint alone is falsified toward DETECTABLE if sourced κ_CNT-forest < **0.0897 W/(m·K)** (below TD-1's own predicted band floor) — **a significant realizability-margin finding warranting Director/Marsh attention, conditional on the rear-only boundary-condition and length-legitimacy caveats above, NOT a Checkpoint-criterion-1/2 target-constraint result** (mandatory fix 8, relabeled per Red Team attack 7 — criteria 1/2 concern the four numbered phenomenon constraints, none of which this instrument cycle scores) |

Search plan (queries 1–10) is unchanged from `phase1_proposal.md` §6,
committed there before this synthesis; not re-typed here.

---

## Idealizations (Phase 1's seven items stand except where amended below;
full list reproduced for a self-contained frozen record)

1. **1D planar, front-flux/rear-only-loss geometry — deliberately
   worst-case for the REAR-ONLY bracket endpoint only** (amended,
   mandatory fix 5): the front-colocated-loss bracket endpoint is the
   complementary, equally-disclosed alternative, not a straw man — see
   "The closed-form front-surface correction" above.
2. **Steady-state only.** Unchanged from Phase 1.
3. **κ_solid sourced from general VACNT/CNT-forest thermal-interface
   literature, not necessarily the SAME specific record-blackness/
   Vantablack-class geometry** this program's own α/n_eff figures cite.
   Unchanged from Phase 1.
4. **Isotropic κ_solid assumed for the 1D model.** Unchanged from Phase 1.
5. **Radiative linearization at ambient T, not front-surface T.**
   Unchanged from Phase 1.
6. **No double-dilution of an already-effective published κ.** Unchanged
   from Phase 1.
7. **T18 assumed still blocked**, re-confirmed at Phase 4. Unchanged from
   Phase 1.
8. **η_thermal≡1** (NEW, mandatory fix 7) — see "Falsifiable predictions"
   above.
9. **`L=l_geometric_m` reused at bench scale in a generation-side role
   its own docstring never licenses, contradicting T9's radial ledger**
   (NEW, mandatory fix 4) — numerically inert for TD-3/TD-4, disclosed
   for completeness. See "The closed-form front-surface correction"
   above.
10. **Witness-scale `L` is an optical-extinction-derived length, never
    run through the licensing test `gas_conduction_h_eff` itself
    requires** (NEW, mandatory fix 6) — TD-5's rear-only bracket
    endpoint is conditional on this being resolved favorably. See "The
    closed-form front-surface correction" above.

---

## Registry (mandatory-fix docket items 2/3)

`lab/caveat_lint_config.json` gains `exp063-biot-correction-machinery`
(κ_critical/biot_number/front_surface_conduction_correction disclosure,
NETD phrase pattern, required at this document + `phase4_results.md`
once written) and `exp063-thermo-disposition-netd-disclaimer` (the
NETD/human-eye disclaimer at classification-adjacent claim points,
required at this document). `lab/numeric_lint_config.json` gains
`exp063-cf-bench-vs-witness-derivation` (a `derivation_consistency`
check on this document's own bench-vs-witness dual application of one
`front_surface_conduction_correction` formula at two length scales —
the module's own docstring names exp-062's EM-6/EM-7 drop as its
structural regression case; this document's split is a live twin).
See `lab/caveat_lint_config.json` / `lab/numeric_lint_config.json`
directly for the entries; not reproduced here.

---

## Result

κ_CNT-forest sourced for the first time, geometry-class-dependent:
0.7–9.62 W/(m·K) for as-grown/bulk-aggregate forest forms (the program's
own actual candidate geometry class), ≈40–50 W/(m·K) for densified/
drawn-sheet forms (a different, better-contacted processing class,
flagged not scored as the primary figure). TD-1 through TD-5 all
CONFIRMED; the worst sourced κ (0.7 W/(m·K)) tightens the flagship bench
margin 699.27×→674.22× and exp-061's own thinnest witness margin
1.35×→1.2920×, both nowhere near their own falsification bars (100× and
1.0× respectively); κ_critical=0.0897 W/(m·K) sits 7.8× below the lowest
κ this cycle found. This program's "first-ever thermal-detectability
classification flip" scenario does not materialize against any real
figure sourced this cycle. Full record: `phase4_results.md`.

## Learned

(1) The correct candidate material's own κ does license the
lumped-capacitance idealization every prior THERMO-sidecar margin rests
on — a real, decisive, first-of-its-kind confirmation, not merely "not
yet falsified." (2) The correction is real and worth carrying forward (a
3.6–4.3% tightening at the worst sourced κ) but small next to either
margin's own remaining headroom. (3) Two structural questions this cycle
deliberately left open — which boundary condition (front-colocated vs.
rear-only loss) is physically real for the actual coating-on-substrate
deployment, and whether the witness-scale conduction length `L=τ_true/α`
is a licensed `h=k/L` input at all (T23, deferred three cycles running:
Iterations 38, 39, 40) — remain genuinely unresolved and are NOT closed
by how comfortably this cycle's own found κ values clear both brackets;
a future cycle finding a materially lower κ, a materially longer L, or
resolving either open question in the less favorable direction could
still move the picture even though nothing in this cycle's own data
does. (4) Phase 5 (six blind reviews + Red Team) surfaced two further,
genuinely new open items: MATERIALS' finding that the CNT-forest root's
own bond to a mounting substrate could itself be a third, worse-than-
either-bracket contact-resistance regime (TD-5's headroom on κ_solid
alone is only 7.8×, this program's thinnest safety factor on record);
and PHOTONICS' finding that TD-5 multiplies an optical constant
(α_true) and a thermal constant (κ_solid) sourced from different,
unconfirmed-common CNT-forest geometry classes. Neither is scored this
cycle; both are queued for Iteration 41+.

## Next

Phase 4 executed (see `phase4_results.md`); this cycle closes at Phase 5
(all six blind reviews PROMISING; Red Team's final audit: PARTIAL,
provisional-to-PROMISING, Checkpoint criterion 4 fires on this cycle's
own self-declared forward tripwire — see `phase5_redteam_audit.md` and
`LOGBOOK.md` Iteration 40). Ranked top-3 for Iteration 41 (Red Team's
reconciliation of all six reviews): (1) resolve T23's witness-scale
length-legitimacy question with a binding forward commitment — a fourth
deferral past Iteration 41 is to be treated as a program-integrity
finding; (2) source or formally model the CNT-forest root-to-substrate
thermal contact resistance as a third disclosed scenario; (3) pin the
record-blackness/Vantablack-class CNT forest's own pitch/diameter AND
through-thickness κ together, in one query set, closing both the
standing near-field-coupling question and the optical/thermal
material-provenance mismatch.
