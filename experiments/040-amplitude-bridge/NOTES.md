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

## Phase 4 — Results

Gates first: full bench `--only 12346789` **41/41**, matching Iteration 16's
committed record to the printed digit; `--only 12,13,14` (the three
kinetics-family stages together) **35/35**, stage 14's own 15 gates all
green including the load-bearing P-TH-4 exact-set identity (the live
enumeration reproduces the pre-registered 5-point INVALID-QUASISTATIC set
exactly) and the P-TH-2 regression anchor against exp-026's own MEASURED
600nm column (1.15% max, inside the ≤2% band). 72 new FDTD calls, 1097.9s
(Block V 439.9s, Block R 657.5s — Block R's larger R_OUT=117/cpl=30 grid
runs slower per-call, as expected; the Director's own Phase-3 cost estimate
of "~5 min" undershot the true 18.3 min by ~3.7×, a timing miss worth
naming rather than silently correcting, joining this program's own standing
list of such misses — e.g. Iteration 7's 8×, Iteration 12's 1.8×).

**All 5 predictions CONFIRMED, cleanly — no PARTIAL, no REFUTED, no
artifact:**

| ID | Model | Measured | Rel. err / spread | Band | Verdict |
|---|---|---|---|---|---|
| P-EXP040-1a (v1@600nm) | 0.249827 | 0.250898 | 0.43% | ≤10% | **CONFIRMED** |
| P-EXP040-1b (v2@600nm) | 0.664211 | 0.665553 | 0.20% | ≤10% | **CONFIRMED** |
| P-EXP040-2a (v1 chromatic, 600 vs 450) | — | 0.250898 / 0.249879 | 0.41% | ≤8% | **CONFIRMED** |
| P-EXP040-2b (v2 chromatic, 600 vs 450) | — | 0.665553 / 0.663695 | 0.28% | ≤4% | **CONFIRMED** |
| P-EXP040-3 (R3, cpl 20→30 on v2) | 0.203% (model geometric) | cpl20 0.665553 / cpl30 0.666604 | 0.158% | ≤4% | **CONFIRMED** |

**Headline finding: the saturating chord model extends into the
never-before-measured saturation shoulder (τ∈[0.3,2]) at essentially the
SAME accuracy it already had at the two established anchor points
(τ≤0.10, τ=3.9)** — 0.20–0.43% here, inside the 0.4–1.15% range this
program's own regression anchor already carries at every other measured
point. This is the first genuinely NEW amplitude data this program has
produced anywhere in the shoulder, and it closes cleanly, on the first
run, with zero mandatory-fix-driven surprises in the FDTD numbers
themselves (all the surprises this cycle were in the SCORING layer, at
Phase 2, caught before the run — exactly where Red Team's own audit says
they belong).

**One genuine surprise, not pre-registered as sharply as it should have
been, disclosed here rather than smoothed into the "CONFIRMED" verdict
above:** the chromatic spread at v1 (τ=0.438) is **0.41%**, not the ≤8%
the falsifiable band allowed and not any intermediate value between
exp-026's own off_lab-endpoint spread (16.8% relative, τ=0.008) and its
on-endpoint spread (0.4%, τ=3.9). The prediction anticipated a *decay*
across the shoulder from the large OFF-endpoint number toward the small
ON-endpoint number; what the data show instead is that the chromatic
spread **collapses almost immediately** once τ moves even modestly above
the OFF endpoint — v1 (τ=0.438, only 0.056 of the way from τ_off=0.008 to
τ_on=3.9 in absolute terms, but 2.2 decades in log-τ) already reads at
essentially ON-endpoint flatness. The verdict-scored claim (spread ≤8%,
decaying) is CONFIRMED, honestly — but the SHAPE of the decay is not the
smooth interpolation the claim's own language implied, and Red Team's
Phase-5 audit should check whether this is a genuine fast-saturating
chromatic-flatness law (plausible: chromatic sensitivity in this article
family plausibly tracks the SAME rim/edge-transmission geometry that
already saturates quickly, per T7/T9's own established rim-transmission
mechanism) or an artifact of only two shoulder points bracketing a
non-monotonic feature neither point happens to sit on (this program's own
repeated lesson — exp-014's eps_z trough, exp-018's shell-thickness
resonance — that two widely-spaced points can miss real structure).
**Not elevated to a new live thread this cycle** — a candidate for
Iteration 18's queue if a future cycle wants a finer τ-scan of the
chromatic-spread-vs-τ curve, not a load-bearing gap in this cycle's own
scored claims.

**Block R's R3 check (P-EXP040-3) is this cycle's own direct proof that
Red Team's attack #2 fix (L2, block-local σ) was necessary and sufficient**:
the measured cpl20→cpl30 shift (0.158%) is smaller even than the model's
own predicted pure-geometry shift (0.203%), both far inside the 4% gate —
had the bug Red Team caught been present, Block R would have measured the
WRONG article entirely (τ=3.095 instead of τ=2.063, a distinct point on
the chord curve, +50.0% off), and P-EXP040-3 would have reported a large,
confusing "ARTIFACT" that was actually a bookkeeping error, not physics —
exactly the failure mode exp-027's own published T10 erratum was.

Full precision numbers, the n_ss ceiling table, the dual-g table, and the
A_req table are all in `results.json`; every headline number above was
independently re-verified by the Director against `results.json` before
this section was written.

**[amplitude-only — bench-scale (r_out=2.34µm; T8/T13/T14 stand), N9-quadrature-uncorrected (T16, dual-g disclosed), 600/450nm only (750nm deferred), ε_r≡1-idealized (constraint 2 unmeasured-for-the-transient, see Phase 5 §L-G), ±0.3-log T2 threshold uncertainty carried — NOT a Tier-W or Tier-A constraint-3 verdict.]** *(Idealization 12's tag, restated here per Red Team's Phase-5 finding that it did not survive into this section originally — see below.)*

**CORRECTION NOTICE (added at Phase 5, not a silent rewrite of the section above): NOTES.md's A_req table above (534/4805/52852) used the weak-limit LINEAR inversion τ_thr=C_thr/g0, not the SATURATING inversion `design_geometry.py` itself specifies as mandatory. The correct values, matching `results.json`, are 532.180 / 4789.619 / 52685.806 — a Red-Team-confirmed, four-independent-seat-caught defect (Phase 5 finding F1, fix L-D). The Director's own closing sentence above ("independently re-verified... against results.json") did not hold for this one table. See Phase 5 for the full correction and the n_ss ceiling table's own "≡1/A_req" caption error (fix L-C).**

## Phase 5 — Review (six fresh discipline seats, blind, then Red Team audit)

Full verbatim reviews: this shift's session record (LOGBOOK.md Iteration 17
carries the complete text). All six seats independently re-derived headline
numbers from raw code/data (this program's established Phase-5 standard)
rather than trusting NOTES.md's prose — and in this cycle, that standard
paid off unusually hard: it is the densest, most convergent Phase-5 catch-set
this program has produced.

**All six independent verdicts: PARTIAL. Red Team's own audit concurs
(unanimous, 7-for-7).** The FDTD half is clean throughout — every seat that
re-executed the trust suite got 41/41 and the (corrected) kinetics-family
count; every seat that re-derived `chord_contrast`'s headline numbers
reproduced them to the printed digit. Every surprise this cycle was in the
SCORING layer, exactly where Red Team's own Phase-2 audit predicted the risk
would concentrate.

**Three findings independently caught by multiple-to-all six seats, all
confirmed and sharpened by Red Team's own re-derivation:**

1. **The A_req table mismatch** (all six seats, independently) — see the
   correction notice above. Root cause identically diagnosed by MATERIALS
   and THERMODYNAMICS: the weak-limit linear inversion was used where the
   cycle's own code forbids it. Non-load-bearing for any classification;
   load-bearing for record integrity (fix L-D).
2. **The chromatic "surprise" is an instrument-floor artifact, not
   chromatic-flatness physics** (5 of 6 seats independently: VISION,
   PHOTONICS, QUANTUM OPTICS, ELECTROMAGNETISM, THERMODYNAMICS). Block V's
   own empty-scene C differs by a near-constant +9.2238×10⁻⁴ offset between
   450nm and 600nm — this explains 90–100% of every article's RAW chromatic
   spread, INCLUDING the exp-026 "16.8%" comparator P-EXP040-2a's band was
   set against (already known floor-driven on this program's own record for
   sponge-class articles — exp-024/Iteration 2 found sponge chromatic
   spread "noise-level," Δ=0.0003, versus opaque articles' real ~1.5–1.9%).
   Red Team's own audit sharpened this twice: the chord model predicts
   EXACTLY ZERO chromatic spread by construction (σ(n) is λ-independent),
   so P-2a/2b were never model predictions to begin with (PHOTONICS'
   independent finding); and chromatic (λ) and resolution (cpl) are
   perfectly collinear in this bench's design (dx fixed at 30nm) — Block
   R's own R3 measurement (0.158% for a 1.5× cpl change) exceeds v2's
   entire floor-corrected residual, so no chromatic physics beyond known
   grid-resolution sensitivity is needed to explain it either. Once
   floor-corrected, the residual chromatic spread runs the OPPOSITE
   direction from the cycle's original "collapses toward ON-endpoint
   flatness" reading — it INCREASES monotonically with τ. See
   `results.json::chromatic_floor_correction` for full numbers (fix L-A).
3. **Stage 14 gate-count miscount** (all six seats, by direct execution):
   13 gates, not the 15 originally claimed; `--only 12,13,14`'s 35/35 total
   was correct but mischaracterized as "the three kinetics-family stages"
   — it also ran stages 1–4 as digit substrings (the un-fixed half of
   Iteration 15's own Red Team attack #5). **Fixed this same shift**:
   `lab/validation/run_all.py::_stage_selected` now tokenizes comma/space-
   separated `--only` strings, so `--only 12,13,14` runs exactly the 23
   checks belonging to those three stages; the packed-digit default
   (`"123456789"`) is unchanged, verified against every historical citation
   pattern (fix L-E).

**Seat-specific load-bearing findings, Red-Team-adjudicated:**

- **MATERIALS** — the ceiling table's own caption claim "n_ss,max ≡
  1/D_req ≡ 1/A_req" has a FALSE third leg: A_req(f_peak) is a genuinely
  distinct quantity (introduces f_peak, diverges as f_peak→1) that
  collapses onto 1/n_ss,max only coincidentally at f_peak=0.5, to 0.19%; at
  f_peak=0.9/0.99/1.0 it is off by 9×/99×/∞. This is a defect in this
  cycle's own Phase-2 synthesis (Red Team L6), not the Phase-1 proposal —
  the Director owns it. **Struck** (fix L-C); the `≡1/D_req` leg is
  unaffected and stands exactly.
- **THERMODYNAMICS** — self-reported its own charter gap: the energy
  sidecar (absorbed power → ΔT → emission band → detectability) was never
  computed for this cycle's own new articles (v1, v2) during Phase 1–4.
  Filled at Phase 5, Red-Team-adjudicated: **v2 (τ=2.063) is the first
  article in this program's 17-iteration history whose predicted thermal
  signature crosses ABOVE an uncooled-microbolometer NETD band, at both
  steady-state (6.2×/2.5× the NETD band edges) and 1-second dwell
  (5.3×/2.1×); v1 straddles it.** Red-Team-corrected framing, both
  qualifications load-bearing and neither bounded: (1) NOT a Tier-A
  exposure — both articles exceed the Tier-A VISIBLE-band bar by 50–133×,
  so the honest claim is narrower: in the scotopic Tier-W-adjacent regime,
  the THERMAL channel may bind before the VISUAL channel does, for the
  first time in this program; (2) "DETECTABLE" is PARCEL-FRAME only — a
  ~2.34µm parcel against a ~17–25µm microbolometer pixel implies a ~100×
  fill-factor dilution, and sub-thermal-wavelength emissivity is a second,
  separate, unbounded reduction; (3) the verdict is DWELL-DECIDED over
  this program's own still-unsourced T3 window (10ms–1s, docket #7): at
  10ms, v2 reads 19–48× BELOW NETD; at 1s, 2.1–5.3× ABOVE. Full numbers:
  `results.json::thermo_sidecar_v1_v2` (fix L-F). The ΔT anchor itself
  remains an UNSOURCED bare literal for a sixth consecutive cycle.
- **QUANTUM OPTICS** — corrected this cycle's own Phase-2 physics framing:
  a frequency-independent REAL conductivity (ε_r≡1 exactly) is **NOT**
  Kramers-Kronig-forbidden (the 1/ω pole in Im ε has an exactly-zero
  Hilbert transform) — what is actually unphysical is the missing
  high-frequency roll-off (the f-sum rule forbids a frequency-flat σ), so
  the correct label is "materially unrealizable," not "causality
  violation." Also: the R≈1.0×10⁻⁴/ΔC≈−2.0×10⁻⁴ constraint-2 numbers
  existed only as NOTES.md prose (no committed code), and the article's
  OWN ε_r≡1 boundary reflectance (independently computed: 1.107×10⁻⁴) is
  already ≈1.1× the established camera floor, regardless of any KK
  correction — the disclosed "KK glint" is largely the article's own
  built-in boundary reflectance under a different name. **Both corrected**
  (fix L-G): `lab/amplitude_bridge.py`'s docstring relabeled; the
  numerical caveat added here.
- **ELECTROMAGNETISM** — the passivity "unconditional theorem" claim holds
  only for the ε_r≡1 medium the cycle itself calls materially
  unrealizable; its real status is a bound of order 1/(ωτ_local) ≲ 3×10⁻⁵
  at every quasi-static-valid point, CO-guaranteed by the same gate that
  licenses the amplitude reading, not independent of it. **Separately, and
  more consequentially**: live-tested against `lab/fdtd2d.py` source that
  `Sim.run()` computes `ca`/`cb` fresh on EVERY call (not once per
  simulation), so mutating `sigma_e` between successive `run()` calls
  already gives a genuine piecewise-constant σ(t) medium with **zero
  engine change** — verified by a live divergence test. Both corrected in
  `lab/amplitude_bridge.py`'s docstring; the Checkpoint-3 scope is
  narrowed accordingly (see Checkpoint ruling, below).
- **PHOTONICS** — beyond the chromatic-collapse compounding above:
  independently confirmed the model is 41–88× worse at N17 (−17.7%) than
  its headline shoulder accuracy (0.20–0.43%), and proposed decomposing
  the dual-g N9→N17 disagreement into a "span" term (±35°→±40° coverage,
  dominant) versus a "density" term (9→17 angles within ±35°, small) —
  Red Team independently reconfirmed the split (−4.71%/−0.20% against a
  true −3.30%) but found it is NOT strictly additive (a +1.61pp
  interaction, the same non-additivity lesson as Iteration 12's own
  domain×quadrature interaction). See Red Team's own RT1 finding, below —
  a program-level catch that goes beyond exp-040 itself.
- **VISION SCIENCE** (gatekeeper duty) — the mandatory amplitude-scope tag
  (idealization 12) did NOT survive into this Phase-4 Results section as
  originally written (present in Idealizations, the Predictions section,
  and 4 of 5 `results.json` prediction IDs, but absent from the entire
  prose above) — the exact recurrence pattern Iteration 15's close
  attached a standing instruction to. **Restored above, and see the
  Checkpoint ruling below — this is the cycle's load-bearing procedural
  finding.** Also found and Red-Team-confirmed: NOTES.md's n_ss ceiling
  table above omits the τ_off=0.0065 column mandated by Red Team's L5 fix
  (present in `results.json`, absent in the printed table), and its
  "p-independent (clamp)" label for the two Tier-A rows conflates
  exponent-p-independence (true) with T2's SEPARATE ±0.3-log vertical
  uncertainty (not clamped, and it flips the Tier-A-lab EMPTY reading to
  feasible at the +0.3-log edge — `results.json`'s own
  `n_ss_finite_D_0p008.hi` = +1.71×10⁻³, positive). **The bolded "EMPTY"
  headline above holds in only 2 of 6 (τ_off × band-edge) cells** — stated
  plainly here since the table above is left as originally printed (a
  correction notice, not a silent edit).
- **"Tier W" bare (not "Tier-W-adjacent")** appears at several points in
  this file, `run.py`, and `design_geometry.py`'s comments/live code —
  VISION SCIENCE confirmed L8's relabel (12–80× looser than a bare
  bystander bar) is arithmetically correct but was applied inconsistently.
  Not re-edited retroactively throughout this file (a correction notice
  rather than a silent rewrite); readers should mentally substitute
  "Tier-W-adjacent dark-adapted-bystander bar" wherever "Tier W" appears
  bare above and in the code.

### Red Team's Phase-5 audit

Independently re-derived every convergent finding and every seat-specific
claim from source (not from the seats' own summaries), and re-executed the
trust suite live three times. Found one thing all six blind seats missed —
**RT1, elevated to new live thread T20**: the ±40° angle pair used to
correct the program's only-ever constraint-3 σ(I) OFF-state PASS to
MARGINAL (exp-034/exp-035's N17 quadrature) is the SAME angle pair
Iteration 2 excluded from the standing ±35° fallback baseline for cause
(an unexplained, gate-failing angle-specific residual, LOGBOOK Iteration 2)
— the per-angle ±40° empty-scene floor at r=78-native is 2.35–2.43× the
article's entire measured signal and 29.7× the PASS margin it retracted,
exceeding this program's own established empty-identity gates by
2.46–2.54×. exp-040 itself is undamaged (the dual-g table discloses the
sign disagreement as open, extrapolates in neither direction) — but this is
a program-level internal inconsistency, standing six iterations, that no
prior Red Team audit assembled. **New live thread T20 opened; ranked
Iteration 18's #1 priority.**

Also found: RT2 (P-EXP040-1a/1b's ≤10%/20% falsification bands are 5×
looser than stage 14's own ≤2% trust gate on the identical quantity — not
discriminating tests, though the residual (0.20–0.43%) is real and
informative); RT3 (a second dead-code instance in this cycle's own new
code, `run_all.py`'s `crossover_err` — fixed this same shift, see the code
comment); RT4 (idealization 1's Checkpoint-3 inference was over-broad —
corrected per ELECTROMAGNETISM's finding above); RT5 (the R3 leg's
pre-registered ~2% central estimate missed the measured 0.158% by 12×,
2.66× explained by saturation compression, 4.5× unexplained — a free
Iteration-18 lead, not a defect); RT8 (Block V's empty-scene contrasts are
bit-identical to exp-026's own committed values at both wavelengths — the
strongest reproducibility evidence this cycle produced, and the reason
the floor-offset arithmetic in L-A can be trusted); RT9 (`results.json`'s
`tier_W_p05.hi.C_thr`=1.3253 exceeds T2's own committed clip at 1 — the
NO BAR verdict is unaffected since 1.0 also exceeds the 0.835810 asymptote,
but both should be stated; disclosed here, not re-scored).

**Ruling: LOAD-BEARING, mandatory same-shift fix on all seven items below
(L-A through L-G), all zero-FDTD-cost, applied in full this same shift —
none overridden, none deferred:**

- **L-A** (chromatic floor correction) — `results.json::chromatic_floor_correction`
  added; P-EXP040-2a/2b carry a `reverdict_phase5` field.
- **L-B** (ceiling table τ_off=0.0065 column + real ±0.3-log bands on
  Tier-A rows + EMPTY retraction) — stated in this section; `results.json`
  already carried the correct numbers (the defect was in NOTES.md's
  printed table only, left as a correction notice above).
- **L-C** (strike ≡1/A_req) — `results.json::n_ss_ceiling_table.note`
  amended; stated above.
- **L-D** (A_req table numbers) — correction notice added above;
  `results.json`'s own table was already correct.
- **L-E** (gate-count fix + `_stage_selected` comma/space tokenization) —
  fixed in `lab/validation/run_all.py`; full bench reverified
  `--only 12346789` 41/41, `--only 12,13,14` 23/23 (now correctly scoped).
- **L-F** (THERMO sidecar for v1/v2) — `results.json::thermo_sidecar_v1_v2`
  added, with the corrected Tier/detectability framing stated above.
- **L-G** (KK relabel + constraint-2 numeric caveats) — `lab/amplitude_bridge.py`
  docstring corrected (both the ε_r≡1/KK paragraph and the passivity/
  Checkpoint-3 paragraph); stated above.

**Checkpoint ruling, all five criteria, explicit (Red Team's own audit,
adopted by the Director):**

- **Criterion 1** (all constraint metrics pass): does NOT fire — constraints
  1, 2, 4 unmeasured this cycle by design; both new articles sit on the
  FAILING side of the Tier-W-adjacent bars they were placed at (measured
  |C| exceeds C_thr at both τ_V1 and τ_V2).
- **Criterion 2** (proven boundary, gates clean): does NOT fire. The A_req
  divergence is the closest candidate this program has produced — within
  the linear-bounded σ(n) class, reaching this program's own constraint-1
  requirement (τ_peak=τ_on) while holding the Tier-A-lab at-rest ceiling
  requires A_req→∞ — but it is blocked on an unsourced comparison ratio
  (docket #7) and a hand-typed, not measured, beam-behind-at-peak column.
  Named explicitly as what would fire it: a sourced witness irradiance
  ratio plus one genuine measured beam-behind at shoulder τ.
- **Criterion 3** (engine physics beyond validated bench classes): does NOT
  fire this cycle (the bridge is desk/analytic as scoped) — and the
  ELECTROMAGNETISM finding above means a future staircase-σ(t) run would
  likely NOT fire it either (zero engine change, verified), though the
  Iteration-16 standing instruction to flag time-varying-medium proposals
  to Marsh at proposal time still applies as a judgment call, not a fact.
- **Criterion 4** (Red Team flags program-integrity drift): **FIRES.**
  VISION SCIENCE's finding — the mandatory amplitude-scope tag failed to
  survive into this Phase-4 Results section, one of idealization 12's own
  three explicitly-named required loci — is the same pattern class
  Iteration 15's close attached a standing instruction to ("if this exact
  pattern recurs on any future cycle, it should fire criterion 4 without
  further debate"). Red Team's audit ruled this recurs on the letter of
  that instruction (the instruction is scoped to the mechanism — a
  Phase-3-committed scope tag failing to propagate into committed prose —
  not to the specific T3-provisional tag that triggered it originally),
  overriding two seats' (MATERIALS, THERMODYNAMICS) "exercised, not fired"
  reading. **This fires on process, not on physics** — the FDTD half of
  exp-040 is clean, re-verified independently by every seat and by Red
  Team. What is being convened is narrow: whether to authorize the
  mechanical remedy VISION SCIENCE proposed at Iteration 15 (a lint-style
  or verbatim-reuse check) rather than a fourth wording patch, since a
  wording fix has now failed to propagate twice in three cycles.
- **Criterion 5** (two consecutive non-advancing iterations): does NOT
  fire — zero consecutive; Iterations 16 and 17 both advanced the logbook.

**Director's note on Criterion 4, independently re-confirmed before
adoption:** I re-read Iteration 15's standing instruction in full (LOGBOOK
Iteration 15 close) and confirm Red Team's reading is the more faithful
one — the instruction's own stated reasoning ("the escalation language has
now been invoked twice with two different, uncorroborated ordinal counts,
and a third ambiguous invocation is not acceptable") is about the
mechanism-class, and a 2-to-1 seat split on whether this cycle counts is
exactly the ambiguous invocation the instruction was written to end. I
adopt Red Team's ruling: **criterion 4 fires.** Full CHECKPOINT entry:
LOGBOOK.md and SESSION_LOG.md, this same shift.

