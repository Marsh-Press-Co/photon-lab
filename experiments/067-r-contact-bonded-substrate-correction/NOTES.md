# exp-067 — R_contact: CNT-Forest Root-to-Substrate Thermal Contact Resistance

**Panel Iteration 44.** Lead: MATERIALS & METAMATERIALS, by rotation. T1
escape route: **N/A** — desk-analytic, zero-FDTD instrument-extension
cycle, the exp-054/060/063/064 class. Executes Red Team's Iteration-43
Phase-5 final audit ruling: R_contact is **LOCKED, unconditional**, for
this iteration (granting THERMODYNAMICS' escalation after three
consecutive deferrals — Iterations 41→42→43 — this program's own
lowest-ever 3-deferral lock precedent, matching exp-059/Q_ext(x)). Full
process record: `phase1_proposal.md` (MATERIALS), `phase2_critique_
{photonics,em,thermodynamics,quantum,vision}.md` (five blind critiques,
all support-with-changes), `phase2_redteam_audit.md`
(PROCEED-WITH-MANDATORY-FIXES, no Checkpoint criterion fires),
`phase3_synthesis.md` (this cycle's Director synthesis, all in this
directory).

---

## ERRATUM (Panel Iteration 44 Phase 5, applied at close)

**The `correction_factor_replace_rear` formula shipped at Phase 4 was
wrong — a passivity violation, not a defensible normalization choice.**
Caught by ELECTROMAGNETISM's blind Phase-5 review, confirmed by Red
Team's Phase-5 final audit (`phase5_redteam_audit.md` R1), which also
identified that the broken formula originated in Red Team's own Phase-2
audit (`phase2_redteam_audit.md` §A1/§2.1) and shipped unquestioned
through Phase 3, Phase 4's 23/23 stage-25 gates, `run.py`'s own
independent reproduction, and four of six Phase-5 reviews' own
"independent verification" — none of which tested the one property
(limiting behavior as `R_contact→0`, sign of the derivative) that would
have caught it.

**What was wrong**: the first shipped formula, `correction_factor_
replace_rear = 1 + (l_geometric_m/k_solid)/r_contact_m2k_w`, normalized
against `R_contact` itself rather than the SAME `R_rear` baseline every
other `correction_factor_*` field in this module uses. It diverged to
infinity as `R_contact→0` (reporting a near-perfect bond as
catastrophic) and DECREASED as `R_contact` increased (reporting a worse
bond as better) — the opposite of physically sound, dissipative-network
behavior.

**The fix**: both endpoints share the same `R_rear` baseline as bracket
B, giving the exact identity `correction_factor_replace_rear =
correction_factor_series - 1.0`. Well-defined and finite everywhere
`R_contact≥0`, including exactly 0 (where it now correctly recovers
`correction_factor_bracket_b_only - 1.0`, a small finite floor, not
`inf`). Applied to `lab/thermo_sidecar.py`; two new stage-25 gates
((3g) the exact identity at all 7 test points/both scales, (3h) a
strict-monotonicity check) permanently guard against this regression
class; the falsification-boundary bisection's search direction and
frozen literal were corrected (`0.004291` → `0.043685` m²K/W — the
corrected value is ~10× larger, since a correctly-normalized good bond
is far more forgiving than the first formula reported). Full docket:
`phase5_redteam_audit.md` §2.

**Corrected prediction table** (replaces the "Falsifiable predictions"
table below for `correction_factor_replace_rear` and every margin/
r_contact_critical figure derived from it; `correction_factor_series`
and everything derived from it is UNCHANGED and was never wrong):

| Point | R_contact (m²K/W) | CF_bench,replace | bench margin,replace | CF_witness,replace | witness margin,replace |
|---|---|---|---|---|---|
| Gate | 0 | 0.037160 | 18817.9× | 0.044866 | 30.089× |
| Band, low | 4×10⁻⁹ | 0.037205 | 18795.4× | 0.044866 | 30.089× |
| **Primary anchor** | **4×10⁻⁸** | 0.037605 | 18595.4× | 0.044867 | 30.088× |
| Band, high | 4×10⁻⁶ | 0.081625 | 8566.9× | 0.044985 | 30.009× |
| Second anchor | 6.5×10⁻⁵ | 0.759717 | 920.4× | 0.046808 | 28.841× |
| Stress A | 1×10⁻³ | 11.153414 | 62.7× | 0.074742 | 18.062× |
| **Stress B** | **1×10⁻²** | 111.199697 | 6.3× | **0.343628** | **3.9286×** |

**P-067-3, corrected**: at Stress B, `correction_factor_replace_rear`
(0.343628) is still `<` `correction_factor_series` (1.343628) — EM's
Phase-2 topology attack still holds, and the corrected divergence is
LARGER than first reported, not smaller: series reads witness margin
1.0047× ("margin nearly erased"); replace-rear reads **3.9286×** ("very
comfortable"), not the first-reported 1.1737×. The two endpoints still
disagree about whether the target constraint is even at risk at
Stress B — the corrected physics strengthens, not weakens, the case that
model-topology choice (not R_contact-value uncertainty) dominates at the
decision-relevant regime.

**P-067-5, corrected**: `r_contact_critical`, replace-rear endpoint
(witness scale, κ=0.70) = **0.043685 m²K/W** (not 0.004291 — the
corrected crossing is ~10× larger, matching the corrected formula's own
far-more-forgiving behavior at small R_contact).

**Checkpoint criterion 4 (program-integrity drift) FIRES** on this
finding, per Red Team's Phase-5 final audit §3 — as a notification, not
a pause (this program's standing precedent). See LOGBOOK.md Iteration 44
and SESSION_LOG.md for the full disclosure.

---

**Operational disclosure, stated up front**: this cycle ran without
WebSearch/WebFetch. The dedicated literature-query dispatch Red Team's
own Iteration-40 audit specified as the correct remedy for sourcing a
directly-measured root/substrate contact-resistance figure was **not
attempted**. Every R_contact value tested this cycle is an
**analogy-based proxy** (`analogy_proxy_diagnostic`), not a direct
measurement. A real dedicated search remains a queued follow-up (see
Next).

---

## Hypothesis

`front_surface_conduction_correction`'s own 1D series network (front-
surface generation → solid conduction → rear-boundary loss to quiescent
air + radiation, `CF = 1 + Bi_gas + Bi_rad`) does not model a CNT
forest's actual mounting condition: a real forest is grown or transferred
onto a substrate, with a genuine root-to-substrate thermal contact
resistance (`R_contact`) at the interface — mechanistically plausible as
governed by the same weak, sparse van-der-Waals-type contact physics
already measured for inter-tube junctions (MATERIALS' own Iteration-40
Phase-5 finding).

**Hypothesis**: adding `R_contact` as a genuinely new thermal-resistance
term — via TWO complementary endpoints, not one — will (1) recover
bracket B exactly at `R_contact→0`, (2) show the bench-scale margin
(TD-4, 100× bar) is structurally more R_contact-sensitive than the
witness-scale margin (TD-5, 1.0× bar), because `Bi_contact ∝ h_combined(L)
∝ 1/L` inherits the same bench-dominant scaling `Bi_gas` already has, and
(3) — the mandatory-fix addition, per EM's Phase-2 topology attack (A1)
— reveal that the SERIES (worst-case, stacked) and REPLACE-REAR (contact
replaces the free-air channel entirely) endpoints diverge materially at
high R_contact, to the point of flipping the witness-margin verdict at
the proposal's own Stress-B test point.

---

## Setup — parameter table

| Knob | Value / spec |
|---|---|
| `LICENSED_R_CONTACT_PROVENANCE` | `frozenset({"measured_direct"})` |
| `DIAGNOSTIC_ONLY_R_CONTACT_PROVENANCE` | `frozenset({"analogy_proxy_diagnostic"})` |
| `_validate_r_contact_provenance(...)` | raises `ValueError` unless licensed or (diagnostic-tagged AND `r_contact_diagnostic_only=True`) |
| `_r_contact_realizability_note(...)` | `"UNGROUNDED..."` when diagnostic, `"N/A..."` when licensed |
| `bonded_substrate_conduction_correction` | composes `front_surface_conduction_correction`; new args `r_contact_m2k_w`, `*, r_contact_provenance, r_contact_diagnostic_only=False`; returns BOTH `correction_factor_series` and `correction_factor_replace_rear`, plus `bi_contact`, `h_combined_w_m2k`, `r_contact_provenance`, `r_contact_diagnostic_only`, `r_contact_realizability`, a rewritten two-endpoint `model_note`, and `netd_disclaimer` (unchanged) |
| `K_AIR` / `EMISSIVITY` | 0.026 W/(m·K) / 0.9 (unchanged from stages 23/24) |
| `L_BENCH_M` | 2.34×10⁻⁶ m (`bench_construction`, unchanged) |
| `L_MP5_730X_M` | 1051.2×10⁻⁶ m (`extinction_derived_diagnostic_only`, `diagnostic_only=True`, T23-governed, unchanged) |
| `κ_solid` | 0.70 W/(m·K) — TD-1's worst sourced figure (unchanged) |
| `lab/validation/run_all.py` stage 25 | 6 gates: refusal identity (3 forbidden `r_contact_provenance` cases), `inspect.signature` identity, 6-part return-dict correctness (bracket-B recovery, `model_note`/`netd_disclaimer` correctness, both realizability/endpoint-divergence checks), regression anchor, dual-endpoint falsification-boundary bisection, source-inspection scan |

**Formulas** (both share the SAME `h_combined(L) = k_air/L +
4·ε·σ_SB·T_amb³` and `R_cond = L/κ_solid`; both apply against the SAME
free-air-lumped ΔT baseline TD-4/TD-5 already use, per Red Team's own
reconciled docket — this is a normalization CONVENTION this cycle adopts
for both endpoints, not independently re-derived from a first-principles
two-network solve; see Idealization 6):

```
Bi_contact                       = R_contact · h_combined(L)
correction_factor_series         = CF_bracket_B + Bi_contact          (worst case: contact stacks IN SERIES beneath the rear-loss channel)
correction_factor_replace_rear   = 1 + R_cond / R_contact             (contact REPLACES the rear-loss channel entirely; -> inf as R_contact->0)
```

`R_contact→0 ⇒ correction_factor_series → CF_bracket_B` exactly, by
construction — the required absolute identity.

---

## Falsifiable predictions — committed BEFORE Phase 4's official run

Every cell below is the OUTPUT of direct invocation of the actual
committed `bonded_substrate_conduction_correction`
(`K_AIR=0.026, κ_solid=0.70, EMISSIVITY=0.9`) — never hand-typed (R4
discipline) — reproduced independently by `run.py` and by stage 25's own
regression-anchor/bisection gates in `lab/validation/run_all.py`.
Baselines (bracket B, `R_contact=0`): `CF_bench=1.037160` (margin
674.22× vs. TD-4's 100× bar); `CF_witness=1.044866` (margin 1.2920× vs.
TD-5's 1.0× bar).

| Point | R_contact (m²K/W) | CF_bench,series | CF_bench,replace | bench margin,series | bench margin,replace | CF_witness,series | CF_witness,replace | witness margin,series | witness margin,replace |
|---|---|---|---|---|---|---|---|---|---|
| Gate | 0 | 1.037160 | ∞ | 674.220× | 0× | 1.044866 | ∞ | 1.2920× | 0× |
| Band, low | 4×10⁻⁹ | 1.037205 | 836.71 | 674.191× | 0.836× | 1.044866 | 375430 | 1.2920× | ~0× |
| **Primary anchor** | **4×10⁻⁸** | **1.037605** | 84.571 | 673.931× | 8.268× | **1.044867** | 37544 | 1.2920× | ~0× |
| Band, high | 4×10⁻⁶ | 1.081625 | 1.836 | 646.503× | 380.927× | 1.044985 | 376.43 | 1.2919× | 0.004× |
| Second anchor | 6.5×10⁻⁵ | 1.759717 | 1.051 | 397.379× | 665.070× | 1.046808 | 24.10 | 1.2896× | 0.056× |
| Stress A | 1×10⁻³ | 12.153414 | 1.0033 | 57.537× | 696.944× | 1.074742 | 2.502 | 1.2561× | 0.540× |
| **Stress B** | **1×10⁻²** | 112.199697 | 1.0003 | 6.232× | 699.040× | **1.343628** | **1.150171** | **1.0047×** | **1.1737×** |

**r_contact_critical** (witness scale, κ=0.70, the R_contact that drives
the witness-scale margin to exactly TD-5's 1.0× bar — i.e.
`correction_factor → 1.35`, since `1.044866 × 1.2920 ≈ 1.34996 ≈ 1.35`):
**series endpoint = 0.010213 m²K/W; replace-rear endpoint = 0.004291
m²K/W.**

**Headline predictions, falsifiable:**

1. **P-067-1 (bracket-B recovery)**: `bonded_substrate_conduction_
   correction(r_contact_m2k_w=0, r_contact_provenance="measured_direct",
   ...)['correction_factor_series']` equals `front_surface_conduction_
   correction(...)['correction_factor']` bit-for-bit, at both bench and
   witness scale.
2. **P-067-2 (bench-more-sensitive corollary)**: at the primary and
   second anchors, the bench-scale margin (series endpoint) moves
   measurably (674.22×→673.93×, then →397.38× at the second anchor)
   while the witness-scale margin barely moves (1.2920×→1.2920×→
   1.2896×) — confirming `Bi_contact`'s bench-dominant `1/L` scaling,
   the same structural reason `Bi_gas` dominates `Bi_rad` at bench scale
   (already on the record since Iteration 40; **not** claimed here as a
   novel surprise — THERMODYNAMICS' Phase-2 correction, accepted).
3. **P-067-3 (EM/A1's endpoint divergence, the mandatory-fix
   deliverable)**: at Stress B, `correction_factor_replace_rear
   (1.150171) < correction_factor_series (1.343628)` strictly, and the
   two witness margins disagree about whether the target constraint is
   even at risk (1.0047× "nearly erased" vs. 1.1737× "comfortably
   clear"). Both numbers must be reported together; neither may be cited
   alone as "the" R_contact-corrected margin.
4. **P-067-4 (regression anchor)**: at the primary anchor (R_contact=
   4×10⁻⁸, κ=0.70), `correction_factor_series` = 1.037605 (bench, 6dp)
   / 1.044867 (witness, 6dp).
5. **P-067-5 (falsification boundary, dual)**: `r_contact_critical` =
   0.010213 m²K/W (series endpoint) / 0.004291 m²K/W (replace-rear
   endpoint) at witness scale, κ=0.70.
6. **P-067-6 (gate completeness)**: all 6 stage-25 gates (refusal
   identity ×3, `inspect.signature` identity, 6-part return-dict
   correctness, regression anchor, dual bisection, source-scan) pass;
   full bench (all pre-existing stages) unaffected.

**Neither anchor "wins" on relevance without qualification (A7,
disclosed, not adjudicated)**: query 10's figure (4×10⁻⁸ m²K/W,
inter-tube van der Waals) describes an internal forest microstructure
interface (nanoscale, tube-to-tube). Query 2's figure (0.6–0.7 cm²K/W =
**6×10⁻⁵–7×10⁻⁵ m²K/W**, corrected from the Phase-1 draft's
arithmetically-wrong "6×10⁻⁵–6.5×10⁻⁵") is a forest-to-external-surface
contact resistance from a thermal-interface-material context —
architecturally the CLOSER analogy to a root bonded to a mounting
substrate. Both are honestly `analogy_proxy_diagnostic`; the second
anchor is treated here as the more physically relevant of the two,
stated explicitly rather than left to the "primary"/"second" labeling to
imply an unearned ranking.

---

## Idealizations (stated explicitly)

1. **Every R_contact value this cycle is an analogy-based proxy, not a
   directly-sourced root/substrate figure.** WebSearch/WebFetch were
   barred this cycle (disclosed in `phase1_proposal.md`'s operational
   disclosure). A real dedicated literature search (the 3–5 query
   dispatch Red Team's own Iteration-40 audit specified) remains a
   queued follow-up — not resolved, not silently closed by this cycle's
   analogy.
2. **The series-insertion model is a genuine worst-case bound, correctly
   labeled as such** — not the true deployment physics, and not the ONLY
   endpoint computed (EM's Phase-2 topology attack, accepted as
   mandatory). The replace-rear endpoint is equally a modeling choice
   (an idealized infinite-heat-sink substrate beyond the contact
   resistance), not independently validated against a real bonded
   sample.
3. **`l_geometric_m` is the SAME length already used by
   `front_surface_conduction_correction`** — no new length parameter.
   `length_provenance` tags carry forward unchanged: `bench_construction`
   for `L_BENCH_M`; `extinction_derived_diagnostic_only` +
   `diagnostic_only=True` for `L_MP5_730X_M`, per T23's existing,
   code-enforced contract.
4. **The vdW-mechanism analogy assumes the root/substrate interface is
   dominated by the same weak, sparse contact physics as the measured
   tube-tube junction** — plausible, not proven. Catalyst-mediated CVD
   growth could produce genuine chemical bonding at the root (better
   than assumed); the macroscopic root footprint could be sparser than
   nm-scale tube-tube contact (worse) — exactly why the direct search
   stays queued rather than treated as answered by analogy.
5. **Both `correction_factor_series` and `correction_factor_replace_
   rear` are applied against the SAME free-air-lumped ΔT baseline TD-4/
   TD-5 already use, as a normalization CONVENTION Red Team's docket
   adopts for both endpoints** — this is a Director-level modeling
   choice carried forward from Red Team's own reconciled formula, not
   independently re-derived here from a first-principles two-resistor-
   network solve with its own baseline. A future cycle wanting to
   re-derive the replace-rear endpoint's normalization from first
   principles is not blocked by anything here; flagged for Phase-5
   scrutiny.
6. **PHOTONICS' α_true/e-fold correction (A2) is a documentation fix,
   not an R_contact physics change**: `L/e-fold_real = τ_true ≈ 8.26`
   (median absorption depth ≈8–12% of `L`), correcting the
   "1,900–6,000×"/"close to exact" framing this program's own record
   previously carried (exp-063 Phase-5). Does not alter any number in
   the predictions table above.
7. **T1 escape route: N/A** — desk/analytic-only, zero-FDTD, matching
   exp-063/064's own scope discipline.
8. **NETD disclaimer carried forward unchanged**: nothing here bears on
   constraint-3/4's human-eye verdict — R_contact is a thermal-
   detectability (instrument) question only.
9. **VISION SCIENCE's Secondary-scope item (Block ARTICLE settled-STEPS
   FDTD leg) is explicitly DEFERRED to Iteration 45**, not folded into
   this cycle (Director's Phase-3 choice, per Red Team's own offered
   options — see `phase3_synthesis.md`). Named here as a disclosed
   deferral, not a silent drop: this is now the FOURTH consecutive
   cycle (Iterations 42→43→44) this item has not been the cycle's
   primary FDTD work, though Iterations 42/43 were each fully dedicated
   to it and still didn't finish it — this cycle never attempted it at
   all, by design, given the primary item's own real code weight.

---

## Registry (mandatory-fix docket item, `caveat_lint_config.json`)

New entry `exp067-r-contact-analogy-proxy-disclosure`: any document
restating this cycle's R_contact-corrected numbers must disclose (a)
"analogy-based proxy, not a directly-measured root/substrate figure,"
and (b) which endpoint (series vs. replace-rear) is being cited, since
the two disagree materially at Stress-B-class R_contact values.
`required_sites` = this file + `phase4_results.md`, both from the start.

---

## Result

See `phase4_results.md` for the full transcript.

## Learned

See `phase4_results.md` / Phase 5 reviews (to follow).

## Next

Ranked, carried from this cycle's own record:

1. **A real dedicated literature search for a directly-measured
   root/substrate contact-resistance figure** (this cycle's own
   Idealization 1; Red Team's Iteration-40 audit's original ask,
   still not attempted) — first priority once WebSearch/WebFetch
   tooling is available in a future cycle.
2. **VISION SCIENCE's Block-ARTICLE settled-STEPS FDTD leg** (T27,
   deferred explicitly this cycle per Idealization 9) — Red Team's own
   Iteration-43 rank #2, now a FOURTH consecutive cycle without being
   the cycle's primary FDTD work; the natural Iteration-45 lead
   candidate, with a pre-committed capped FDTD budget scoped to Block
   ARTICLE's article-present legs only (not FALLBACK_ANGLES/Block MINI),
   per VISION's own Phase-2 flip condition.
3. **A first-principles re-derivation of `correction_factor_replace_
   rear`'s normalization** (Idealization 5) — non-blocking, flagged for
   Phase-5 scrutiny this cycle; a future cycle may want to derive it
   from a genuine two-resistor-network solve rather than adopt the
   convention here.
