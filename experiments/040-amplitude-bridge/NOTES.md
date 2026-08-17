# exp-040 — The Amplitude Bridge

Panel Iteration 17 · Runner: cloud panel shift · Lead: THERMODYNAMICS (rotation)

Full seven-seat cycle: Phase 1 proposal (THERMODYNAMICS) → 5 blind parallel
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM OPTICS, VISION
SCIENCE — unanimous **support-with-changes**, the densest, least-overlapping
fix-set this program has produced in one cycle) → Red Team last with
everything (verdict: **proceed-with-mandatory-fixes**, 16 numbered attacks,
independent recomputation of every load-bearing number in the packet,
explicit adjudication into 12 load-bearing / 10 correctable-with-disclosure /
5 overreach-rejected) → Phase 3 synthesis (this file) → predictions committed
here, before any run → Phase 4 build + run. Full verbatim panel transcript:
this shift's session record (LOGBOOK.md Iteration 17 carries the complete
text of all seven outputs).

## Pre-flight (this shift)

Fresh container, deps installed per the recorded wrinkle (numpy/scipy/
matplotlib/pillow/autograd/fdtd via pip, then `ceviche --no-deps`). Bench
trust suite reconfirmed green before any panel work: `--only 12346789`
41/41, matching Iteration 16's own committed record to the printed digit.
Iteration 16 found fully closed out on arrival (predictions/results/
LOGBOOK/PLAN/SESSION_LOG all present and consistent).

## Hypothesis

Iteration 16 closed with a Red-Team-adjudicated, unanimously-ranked-#1
Iteration-17 priority: **build the n(t)→ε(ω,t)/σ_abs(t) causality/passivity
-checked amplitude bridge** — the single piece of missing machinery that
lets any T3-provisional timing classification (exp-039) become an actual
scored constraint-3 amplitude verdict against T2's already-pinned C_thr(L).
THERMODYNAMICS (this cycle's rotation lead) proposed executing this
priority directly, per program precedent that the rotation lead defaults to
the ranked-#1 queue item.

Pre-registered hypothesis: (a) a bounded linear interpolation between
exp-026's two already-measured, real static articles (off_lab, τ=0.008; on,
τ=3.9) gives a causal, unconditionally-passive σ_e(n) with no engine change
needed (Checkpoint-3 avoided); (b) the saturating ray-chord transfer
`chord_contrast(τ)`, a genuine generalization of exp-034's committed
`chord_model_g0`, extends cleanly from the two established anchor points
(τ≤0.10, τ=3.9) into the never-before-measured saturation shoulder
(τ∈[0.3,2]) — exactly where both of T2's Tier-W night-lab decision bars
sit; (c) T2's own ±0.3-log vertical threshold uncertainty, inert at every
prior photopic (Tier-A) citation because the `max[1,·]` clamp kills it
there, becomes the DOMINANT uncertainty term the moment a cycle scores
against the L-scaled Tier-W rows — as this cycle is the first to do.

## Phase 1 — Proposal (THERMODYNAMICS, abridged)

Full verbatim: this shift's session record. Proposed `lab/amplitude_bridge.py`
+ suite stage 14: σ_e(n) = σ_off + n·(σ_on−σ_off) (exp-026's off_lab/on
endpoints, ε_r≡1 exactly at every n); `chord_contrast(τ)` (the saturating
generalization of `chord_model_g0`); scoring against C_thr(L) both tiers.
Desk/analytic, not FDTD-coupled (τ_kinetics ≥ 1ns vs a ~2fs optical period
is ≥5×10⁵ periods — the static reading at instantaneous σ is the correct
adiabatic physics). Block V (2 new FDTD articles, τ placed AT the Tier-W
p=0.4/p=0.5 bars, 27 runs @600nm) + Block R (R3 check, 18 runs @cpl=30).
Headline forward product: an n_ss ceiling table (D→∞ idealization) — the
largest at-rest switched population a material can carry without breaching
each constraint-3 bar, independent of the material's own dynamic range D.

## Phase 2 — Critique (five blind, then Red Team) — summary

All five blind seats independently returned **support-with-changes**, each
finding real, non-overlapping, numerically-verified defects (every claim
below independently re-derived by the Director from source before
adoption):

- **PHOTONICS**: u_C's angular-quadrature term (T16) was carried
  *additively* (7.8×10⁻⁴, calibrated at |C|≈0.005) then applied at
  |C|=0.21–0.65 — a 43–130× extrapolation in the wrong shape; at the one
  geometry where an N9→N17 measurement exists, the shift is 14.2% of |C|,
  fractional not absolute. Also: λ-flatness inherited into the shoulder
  from a 750−450 *endpoint* difference, not the interior-600nm extremum
  the OFF-lab article actually shows (true spread 1.8× the quoted bound).
- **MATERIALS**: P-TH-6's "third, independent bar" is algebraically
  n_ss,max ≡ 1/D_req — the same three inputs as `REALIZABILITY_MEMO.md`'s
  own D_req≈537, inverted, not a new axis. Also: the primary OFF endpoint
  (τ_off=0.008, D=487.5) fails the Tier-A-lab bar at **n=0** — the article
  pair does not span enough range even at rest.
- **ELECTROMAGNETISM**: the proposal's own adiabaticity gate (P-TH-4, "100
  optical periods") uses the wrong clock — the governing parameter for a
  CW phasor read after a fixed settling-step budget is t_settle/τ, not
  1/(ωτ); re-referenced, the INVALID-QUASISTATIC count is 5, not 2.
- **QUANTUM OPTICS**: ε_r≡1 exactly at every n is Kramers-Kronig-forbidden
  — the ON endpoint's own Im ε=0.0796 forces a computable Δε_real, hence a
  real (if small) glint channel the proposal had deleted by construction
  rather than measured, an exposure specifically at constraint 2.
- **VISION SCIENCE** (gatekeeper duty): six defects in the scoring layer —
  most consequential, T2's own committed ±0.3-log vertical threshold
  uncertainty (dormant at every prior photopic citation) is the dominant,
  omitted uncertainty term the moment a cycle scores Tier-W rows, flipping
  2 of 4 headline classifications inside VISION's own committed band; and
  the row labelled "Tier W" is a bare dark-adapted-bystander bar, 12–80×
  stricter than PANEL.md's actual Tier W (the flashlight holder's own
  self-glare sidecar, pinned at Iteration 1).

**Red Team** (16 numbered attacks, verdict **proceed-with-mandatory-fixes**):
independently re-derived every headline number in the proposal AND all five
critiques from source (not trusted as summarized) — confirmed every one of
the five seats' central claims, corrected several of their supporting
numbers, and found two load-bearing defects **no blind seat caught**:
(A1) the proposal's own "cleared with 9.4× margin" irradiance-ratio claim
silently evaluated A_req at f_peak=0.5 (14.2% beam-behind), far short of
the proposal's own τ_peak≥3.9 requirement — A_req *diverges* as f_peak→1,
and against the correctly-evaluated ratio the claim inverts to 1.04×
margin-to-8.6×-short depending on which OFF endpoint anchors it; (A2) Block
R's σ, if copied as a bare number from Block V's τ=2.0632 without
recomputing at Block R's own r_out=117, silently drifts τ by +50% —
exp-027's own published T10 erratum class, and would have fired P-TH-5's
own R3 gate as a false ARTIFACT. Red Team also found (A16) that the
bridge's own transfer function predicts the N9→N17 angular shift is
fractional and −3.3% at this geometry, while the one real measurement is
+14.2% — opposite sign — meaning PHOTONICS' proposed remedy (fractionally
extrapolating the measured shift into the shoulder) is licensed no better
than the additive form it correctly criticizes; both are superseded by
carrying both established g values (N9 0.70562, N17 0.80600) side by side
and disclosing the sign disagreement as open (T16), at zero added cost.

Explicit adjudication (Red Team's own routing ruling, this program's
established precedent since Iteration 16): of the ~15 distinct fixes filed
across five support-with-changes verdicts, **12 are load-bearing** (all
zero-FDTD-cost except one), **10 are correctable-with-disclosure**, and
**5 are overreach, rejected** — most consequentially PHOTONICS' proposed
N17-at-the-shoulder FDTD leg (costed by Red Team at ~78 real calls plus a
new domain build and coverage gate, not the proposed "24 runs, 70s", AND
measuring a quantity the model's own transfer function contradicts in
sign) and QUANTUM OPTICS' proposed KK-endpoint FDTD leg (predicted signal
≈ the established camera floor, SNR≈1). Rejecting these keeps the cycle at
72 FDTD runs (~5 min) instead of the ~195-run, two-new-domain version a
literal fix-count sum would have produced — Red Team's own explicit
program-health point: ten consecutive PARTIAL cycles (Iterations 7–16)
argue for shipping one clean, honest, band-reported forward product this
cycle, not turning the first mechanism-scoring cycle in eight into an
eleventh instrument-hygiene cycle.

## Phase 3 — Synthesis (Director)

**Accepted in full** (all twelve of Red Team's ranked load-bearing fixes,
L1–L12 — see Red Team's full numbered list in the session record; applied
below and in `lab/amplitude_bridge.py`/`design_geometry.py`/suite stage 14):
the amplitude-scope tag at every point of amplitude claim (L1); block-local
σ with a runtime assert per block (L2, live-tested this cycle as
prediction P-EXP040-3's own gate); A_req reframed as a function of
τ_peak/τ_on with the divergence stated, the witness ratio labelled
unsourced (L3); all margins in contrast units, no margin-ratio language
inside u_C (L4); the n_ss ceiling table carrying both D→∞ and finite-D
(τ_off∈{0.0065,0.008}) columns (L5); the n_ss,max≡1/D_req≡1/A_req identity
stated in the table caption, "third independent bar" language struck (L6);
every Tier-W ceiling row reported as a ±0.3-log band, not a point value,
with the p=0.5-hi row correctly reported as NO BAR — above the chord
model's own 0.835810 saturation asymptote (L7); "Tier W" relabelled
"night-ambient dark-adapted-bystander bar (Tier-W-adjacent, glare-free)" —
true Tier W stays unscored pending docket #7 (L8); P-TH-4 re-referenced to
`amplitude_bridge.settling_time_s` (computed from instrument parameters,
never hand-typed) with the exact 5-point INVALID-QUASISTATIC set checked
as an identity, not a count (L9); the dual-g (N9/N17) table with the
sign-disagreement disclosure superseding both PHOTONICS' and EM's
separate proposed fixes at zero cost (L10); suite stage 14 anchored to
exp-026's MEASURED 600nm column,
P-TH-2 relabelled a regression anchor, not an independent cross-check
(L11); Block V run at 450nm as well as 600nm — the one run-adding fix
approved (+27 runs) — since Tier-W is a scotopic bar and V′(450)/V′(600)
=13.8 (L12).

**Accepted with disclosure** (Red Team's C1–C10; applied as text/comments
in code and in this file, not as new runs): constraint 2 relabelled
UNMEASURED-FOR-THE-TRANSIENT with Red Team's corrected KK numbers (R≈1.0×
10⁻⁴, ΔC_ambient≈−2.0×10⁻⁴, non-conservative direction, moves no
classification) rather than QUANTUM OPTICS' wider band; P-TH-4's
dephasing-margin relationship corrected to "subsumes," not "additional
to"; the sidebands sentence replaced with EM's wording (envelope captured
exactly under the quasi-static approximation; only unresolvable optical-
sideband structure omitted); the legacy series' error at τ=1.95 corrected
to 65.2% low, not 8%, and its falsification clause noted as deterministic
algebra rather than an empirical prediction; the T17 ε/path-length/
geometry link explicitly NOT claimed closed (τ comes from exp-026's bench
sponge, not spiropyran's own molecular constants); VISION's third clause
(re: T2's field crossover) ruled STALE by Red Team — that inconsistency
was Red Team's OWN Iteration-1 attack #2, already corrected
(L*_field∈[1.7×10⁻⁴,1.2×10⁻³], the committed band), not reopened here; the
"Tier W night field clipped at 1" language corrected to cite the
0.835810 saturation asymptote as the real reason, not an arithmetic clip;
realizability tier label corrected to exp-038's own literal range
(r∈[10⁻³,10⁻¹], not "r≤10⁻¹"); cost estimate corrected to ~5 min for 72
runs, not "~2.5 min for 45."

**Rejected as overreach** (Red Team's O1–O5, with reasons preserved for
the record, not silently dropped): PHOTONICS' N17-at-the-shoulder FDTD leg
(O1 — wrong cost estimate, sign-contradicted by the model, superseded by
the zero-cost dual-g disclosure); QUANTUM OPTICS' KK-endpoint FDTD leg
(O2 — SNR≈1 against the established camera floor); VISION's stale T2
field-crossover reopening (O3); PHOTONICS' second λ leg at 750nm (O4 —
trimmed to 450nm only, the scotopically-dominant wavelength; 750nm
deferred); any reopening of the frozen 0.005/0.02 photopic ladder (O5 —
disclose the Blackwell 0.003–0.005 provenance in a footnote, its own
cycle if pursued further).

### Idealizations (stated, not smuggled)

1. **Desk/analytic bridge, not FDTD-coupled.** `lab/fdtd2d.py` computes its
   update coefficients ONCE, outside the step loop (verified from source,
   Red Team) — a genuinely time-varying medium is Checkpoint-3 territory
   and is NOT attempted this cycle. Static FDTD physics evaluated at the
   instantaneous σ; valid to error O(t_settle/τ) ≤10⁻⁵ at every
   HEADLINE-SCORED point (Hosts C/D, r≤10⁻¹) under the re-referenced gate.
2. **ε_r≡1 exactly at every n — Kramers-Kronig-forbidden in the strict
   sense** (QUANTUM OPTICS' load-bearing catch). Constraint 2 is
   UNMEASURED-FOR-THE-TRANSIENT, not inherited from exp-026 (whose
   observer-return was measured on an article with ε_r=1 imposed by
   fiat). Red Team's corrected estimate: R≈1.0×10⁻⁴, non-conservative
   direction, moves no classification this cycle, disclosed not measured.
3. `lab.kinetics`'s own idealizations inherited verbatim (two-state
   single-pole, k_f independent of n, temperature-independent rates,
   coherence adiabatically eliminated — QUANTUM OPTICS' Iteration-15
   dephasing margin independently confirmed SUBSUMED by the re-referenced
   quasi-static gate this cycle, not merely satisfied alongside it).
4. **σ_e uniform over the disk; n a single 0D population** — no spatial
   structuring of the switching front. Not modeled; first follow-up.
5. **Bench scale only** (r_out=78 cells=2.34µm for Block V). T8/T13/T14
   stand: no witness-scale C claim; T14's own wrong-direction asymptote
   means bench |C| is NOT a safe lower bound.
6. **Ray-optical chord transfer, no diffraction.** T15's own resolution-
   growing 1.0→3.1% gap (chord model vs measured g) is a SEPARATE,
   already-disclosed open question from this cycle's own N9-vs-N17
   dual-g disagreement (T16) — not conflated.
7. **N9 ±35° angular quadrature**, T16's budget carried via the disclosed
   dual-g table, not resolved this cycle (Red Team's L10, superseding
   both PHOTONICS' and EM's separately-proposed remedies).
8. **450nm + 600nm only this cycle**; 750nm deferred (O4) — the least
   scotopically-weighted of the three, and the smallest known chromatic
   excursion in this article family (exp-026's own established spread).
9. **2D TMz, back-lit channel only.**
10. **σ(n) is λ-independent by construction** (PHOTONICS' disclosed
    observation) — a real physical simplification for any dispersive
    material; not modeled, an outstanding ask, not required this cycle.
11. **Unsourced inputs still unsourced**: T3's 10ms–1s window, the
    flashlight irradiance ratio I_beam/I_ambient≈5×10³ (docket #7 — used
    NOWHERE in this cycle's scored A_req language, per Red Team's L3);
    T2's p∈[0.4,0.5] exponent band; the Blackwell 0.003–0.005 asymptote
    vs. the frozen 0.005 lab bar (disclosed footnote, O5, not re-litigated).
12. **Scoring-cap discipline, mandatory tag** at every point of amplitude
    claim in this file, `results.json`, and the Phase-4 results section:
    *bench-scale (r_out=2.34µm; T8/T13/T14 stand), N9-quadrature-
    uncorrected (T16, dual-g disclosed), 600/450nm only (750nm deferred),
    ε_r≡1-idealized (constraint 2 unmeasured-for-the-transient), ±0.3-log
    T2 threshold uncertainty carried — amplitude-only; NOT a Tier-W or
    Tier-A constraint-3 verdict.* The timing half (exp-039) stays
    separately T3-provisional and T19-model-dependent; a joint
    constraint-3/4 verdict needs both halves, and only the amplitude half
    lands this cycle.

### Predictions (committed before any FDTD run — house discipline)

Five falsifiable predictions score the two new FDTD blocks (72 runs) that
are this cycle's actual NEW measurements. All other quantities in this
section (the n_ss ceiling table, the dual-g table, the A_req table) are
desk-computed, pre-registered CORRECTIONS to the Phase-1 proposal's own
numbers, algebraically pinned by `lab/amplitude_bridge.py` — not
falsifiable "predictions" in the run-scored sense, but committed here,
before the run, exactly as Red Team's fix list requires.

Desk values (from `lab/amplitude_bridge.py`, reproduced independently by
the Director to 10 significant figures against every Red-Team-cited
number): g0 (chord model, τ→0)=0.6857163680; τ_V1=0.437985 (the Tier-W
p=0.4 bar, C_thr=0.249827); τ_V2=2.063172 (the Tier-W p=0.5 bar,
C_thr=0.664211); chord-model saturation asymptote=0.835810; σ_V1=
2.80760×10⁻³, σ_V2=1.32255×10⁻² (both at Block V's own r_out=78); σ_V2 at
Block R's own r_out=117 = 8.81698×10⁻³ (NOT the r_out=78 value carried
over — that would silently give τ=3.094759, a +50.0% drift, Red Team's A2).

| ID | Claim | Central (model) | Band | Falsified if |
|---|---|---|---|---|
| P-EXP040-1a | Block V, v1@600nm: chord model reproduces measured &#124;C&#124; at τ_V1 (never-measured shoulder) | 0.249827 | ≤10% rel err → CONFIRMED; ≤20% → PARTIAL | >20% rel err |
| P-EXP040-1b | Block V, v2@600nm: chord model reproduces measured &#124;C&#124; at τ_V2 | 0.664211 | ≤10% rel err → CONFIRMED; ≤20% → PARTIAL | >20% rel err |
| P-EXP040-2a | Chromatic spread at v1 (450 vs 600nm) is smaller than exp-026's off_lab endpoint (~16.8% relative) | ≤8% relative spread | ≤8% CONFIRMED; ≤16.8% PARTIAL | spread reproduces or exceeds the off_lab endpoint's own 16.8% |
| P-EXP040-2b | Chromatic spread at v2 (deeper in shoulder) smaller still | ≤4% relative spread | ≤4% CONFIRMED; ≤10% PARTIAL | >10% |
| P-EXP040-3 | R3 check (cpl 20→30) on v2, Red Team's L2 fix live-tested | ~2% shift (informed by this bench's own established g_raw cpl-sensitivity, off_pass 0.6927→0.7056≈1.9%) | ≤4% (Phase-1's own gate, preserved) | >4% → ARTIFACT-CANDIDATE, new T15/T16-relevant thread |

**Idealization-12 tag applies to every prediction above and every table
below without exception.**

**n_ss ceiling table** (D→∞ idealization AND finite-D at τ_off∈{0.0065,
0.008}, ±0.3-log band on every L-scaled row):

| Bar | C_thr (center) | τ_thr | n_ss,max (D→∞) | n_ss,max (finite-D, τ_off=0.008) | ±0.3-log band (finite-D) |
|---|---|---|---|---|---|
| Tier-A lab | 0.005 | 0.007315 | 1.876×10⁻³ | **−1.76×10⁻⁴ (EMPTY — off_lab article fails this bar at n=0)** | p-independent (clamp) |
| Tier-A field | 0.02 | 0.029543 | 7.575×10⁻³ | 5.535×10⁻³ | p-independent (clamp) |
| Tier-W-adjacent p=0.4 bystander bar | 0.249827 | 0.437985 | 0.112304 | 0.110479 | [0.04904, 0.29176] |
| Tier-W-adjacent p=0.5 bystander bar | 0.664211 | 2.063172 | 0.529019 | 0.528050 | [0.15982, **NO BAR** (hi exceeds 0.835810 asymptote)] |

**Dual-g table** (Red Team L10, superseding PHOTONICS' additive-N17 leg and
EM's fractional-scaling proposal at zero cost): chord model g0=0.685716;
measured g(N9, r=78-native, cpl=30)=0.705609 (exp-035, bit-identical
reproduction of exp-033's own citation); measured g(N17, same
geometry)=0.805946 (exp-035). The model PREDICTS a −3.3% N9→N17 shift
(fractional, confirmed across a 317× τ span); the ONE real measurement at
this geometry shows +14.2% — opposite sign. Disclosed as open (T16); not
extrapolated into the shoulder in either direction this cycle.

**A_req table** (Red Team L3 — reframed as a function of f_peak=τ_peak/τ_on,
diverging as f_peak→1; the witness's I_beam/I_ambient≈5×10³ is UNSOURCED
per idealization 11 and is NOT reported as "cleared" at any row):

| f_peak | τ_peak | beam-behind at peak | A_req (D→∞, Tier-A-lab n_ss ceiling) |
|---|---|---|---|
| 0.5 | 1.95 | 14.2% | 534 |
| 0.9 | 3.51 | 3.0% | 4805 |
| 0.99 | 3.861 | 2.1% | 52852 |
| 1.0 | 3.9 (this program's own constraint-1 requirement) | 2.0% | **∞** |

Full precision, all code, gates, and the run harness: `lab/amplitude_bridge.py`,
`lab/validation/run_all.py::stage14_amplitude_bridge`, `design_geometry.py`,
`run.py` (this directory).
