# exp-044 — The Realistic-Host ON-Endpoint Kinetics Gate + `REALIZABILITY_MEMO.md` Amendment 4 + PHOTONICS' 3λ Achromatic Check

Panel Iteration 21. Lead: MATERIALS (rotation). Runner: cloud panel shift,
2026-08-18. Executing Red Team's Iteration-20 top-ranked priority
("the single most consequential open item," QUANTUM's own native charge,
non-native lead per Iteration-18/20 precedent).

## PHASE 1 — PROPOSAL (MATERIALS, lead)

Full text kept verbatim, per this program's flag-don't-rewrite convention
(T10 precedent): `phase1_proposal.md`. Superseded in load-bearing respects
below.

Scope: two blocks, bundled per exp-034's own "tightly-related, all-zero-
cost, all-desk/analytic items" precedent — **Block A** (Red Team's
Iteration-20 priority #1): rerun the σ(I) ON-endpoint kinetics gate
against `lab/kinetics.py`'s real PUBLISHED/PLAUSIBLE-tier grid (Hosts A–D
× RATIOS excluding r=1.0 — 16 points), not exp-043's two r=1 UNOBTANIUM
boundary probes. **Block B** (native, priority #4): `REALIZABILITY_MEMO.md`
Amendment 4 — three citation corrections triggered by exp-043's
newly-sourced witness irradiance. Deferred with reasons: #2 (THERMO's
h_conv/mass_kg re-derivation), #3 (EM's `iso_xsec_sq`-vs-geometric-disk
table entry, T22), #5 (PHOTONICS' 3λ achromatic check).

## PHASE 2 — CRITIQUE (five seats blind, then Red Team with everything)

All five seats independently landed **support-with-changes**. Full text:
compiled critique record (not committed as a separate file — condensed
here per house convention; every claim below was independently re-derived
by Red Team, see its own audit).

**PHOTONICS.** Steel-man: the reading-(a) host/r-insensitivity claim
(P-MAT21-A1) is a forced consequence of `relax_exact`'s own formula, not
an unverified assertion — verified by hand. Sharpest attack: `RATIO_ON`/
`SIGMA_EXT_ON` are a single-wavelength (600nm) number applied uniformly
across the 16-point grid as if broadband-representative, contradicting
T18's own narrowband finding for real nonlinear-absorption mechanisms.
Flip: fold in the deferred 3λ check (#5) before treating the UNDETECTABLE
headline as informative about a realistic host.

**ELECTROMAGNETISM.** Steel-man: architecturally sound on energy-coupling
grounds — the reused steady-state ΔT is provably area-invariant, and the
kinetics ratio is bounded in [0,1] by construction, so neither reading can
exceed the calibrated ceiling. Sharpest attack, load-bearing: reading (a)
(ΔT_ss×n_at_dwell/n_ss) is not a physical temperature — it silently
substitutes n_ss for 1 in the ceiling's own n=1 calibration, overstating
ΔT by exactly 1/n_ss at every point where n_ss<1 (reaches ~10⁹× at
r=1e-9). Also: the proposal's own T22 idealization sentence has it
backwards — the area convention is PROVEN to cancel, not merely "would
rescale." Flip: relabel reading (a) as diagnostic-only, correct the T22
sentence.

**THERMODYNAMICS.** Steel-man: correctly inherits the area-invariance
identity, so scaling by a dimensionless kinetics fraction cannot
reintroduce an area artifact. Sharpest attack, load-bearing (converges
with QUANTUM): Host C (k_r=1e3) sits in the "kinetics τ≈thermal τ"
intermediate regime the decoupled two-stage shortcut is unvalidated for
in general (T22) — lumped in with Hosts A/B unflagged. Also: the reused
ceiling is already KNOWN, not merely feared, to be ~3 OOM too high
(Iteration-20's own h_conv finding) — the proposal's deferral of item #2
treats this as hypothetical, not already-quantified. Flip: exclude Host C
from the trustworthy grouping, or state the known correction magnitude.

**QUANTUM OPTICS.** Steel-man: executes exactly what QUANTUM's own
Iteration-20 Phase-5 review demanded; independently re-derived all seven
P-MAT21-A predictions from `relax_exact`/`n_eq_exact` in closed form, all
check out. Sharpest attack, load-bearing (converges with EM): reading (a)
is not a defensible alternative convention — physically consistent scaling
gives ΔT(t)=ΔT_ss·n(t) (reading b); reading (a) equals the correct answer
only when n_ss=1, never reached on this grid. Also independently flags
Host C's intermediate-regime gap. Flip: demote reading (a) to
artifact-demonstration only; disclose the Host-C coupling-validity gap.

**VISION SCIENCE.** Steel-man: correctly disciplined — never touches a
perceptual quantity, names the NETD/human-eye distinction as an
idealization. Sharpest attack, load-bearing: the disclaimer is stated once
in Idealizations but absent at all three points of claim in Section 4
(P-MAT21-A3/A6/A7's "UNDETECTABLE" language) — the exact recurrence
pattern that fired Checkpoint criterion 4 at Iteration 17 and nearly
recurred at Iteration 20. Flip: propagate the disclaimer to every point of
claim.

**RED TEAM (final audit, everything).** Independently re-derived the
coupled kinetics→thermal ODE in closed form (a check none of the five
blind seats nor the original T22 finding had done) and **upgraded** the
EM/QUANTUM catch: reading (a) doesn't merely mislabel a convention — it
**solves no physical model this codebase has ever stated**, at any grid
point except the unreached edge case n_ss=1. Separately **sharpened**
THERMO/QUANTUM's Host-C concern into a *resolved* question rather than a
standing caveat: since `dwell/τ_kinetics≥66` and `dwell/τ_thermal≈48` both
comfortably clear this codebase's own `N_TRANSIENT_TAU=25` convergence
bar, the coupled-ODE endpoint should match the decoupled shortcut to
extremely high precision at this specific dwell — a claim Red Team
recommended TESTING with the closed form rather than asserting either way.
Found one load-bearing defect no blind seat caught: the proposal's own
Scope Decision section (which explicitly itemizes and gives reasons for
deferring priorities #2/#3/#5) never mentions Iteration-20's own Tier-2
priority — "EM's kinetics-thermal coupling test at an intermediate rate
constant (T17 extension)" — despite it being the item most directly
implicated by Block A's own Host-C points. Also corrected a terminology
imprecision (QUANTUM's "dimensionally wrong" — both readings are in
Kelvin; the defect is a scaling/normalization error, not a dimensional
one) and confirmed EM's T22-idealization-sentence catch by direct code
read (`thermo_sidecar.py:146-158`).

**Ruling: PROCEED-WITH-MANDATORY-FIXES.** Arithmetic clean throughout
(Red Team independently reproduced every Block A/B number, no numeric
errors found — unusually clean for this program's typical Phase-2 catch
rate). Seven mandatory fixes:

1. Drop reading (a) from headline/NETD classification; score UNDETECTABLE
   on reading (b) alone; retain reading (a) only as a labeled artifact
   demonstration, explicitly stated to solve no physical model on this
   grid.
2. Correct the T22 idealization sentence: the area convention is PROVEN
   invariant for `steady_state_delta_T` — Block A's numbers do NOT rescale
   under a future T22 revision.
3. Run the closed-form coupled kinetics-thermal ODE check for Host C's 4
   points specifically (zero FDTD) and report the actual number, rather
   than including it unflagged or excluding it on suspicion.
4. Add THERMO's caveat (known direction/magnitude of the h_conv
   correction, ~3 OOM high) to every predicted band.
5. Either run PHOTONICS' 3λ re-derivation this same cycle, or state
   explicitly why it is deferred a third consecutive time.
6. Propagate the NETD disclaimer to every point of claim in Section 4 and
   into this NOTES.md's own prose / `run.py`'s console output.
7. Add one sentence to the Scope Decision acknowledging the Iteration-20
   Tier-2 kinetics-thermal-coupling item was not separately itemized.

No constraint-3 risk (this cycle touches no ambient-silhouette scene at
all — Block A is a thermal/IR sidecar, Block B a citation memo); no
resemblance to any RULED OUT entry (R1/R2/R3 concern the closed
cloak-mechanism line, untouched here).

## PHASE 3 — SYNTHESIZE (Director)

**All seven mandatory fixes adopted in full, no overrides.**

Fix 5 resolved by actually running the check, not deferring a third time:
**Block C**, PHOTONICS' 3λ achromatic-idealization check, using data
already committed to this repo — exp-026's `beam_scene` block measured the
ON-endpoint article's own `sigma_abs`/`sigma_ext` at all three sweep
wavelengths (450/600/750nm) as part of a different measurement, and was
never previously read for ratio-flatness. Zero new cost. This directly
answers PHOTONICS' Iteration-20/21 concern for THIS bench article's own
idealization, though — stated explicitly, not smoothed over — it does not
resolve the separate, deeper T18/`REALIZABILITY_MEMO.md` question of
whether a REAL physical σ(I) mechanism achieving this dynamic range would
itself be broadband (this bench article is a scalar σ_e bump by
construction, achromatic by declared idealization, not a dispersive real
material).

Fix 7: the Iteration-20 Tier-2 kinetics-thermal-coupling item (EM's own
proposed test "at an intermediate rate constant") is squarely what Fix 3's
Host-C closed-form check answers for THIS cycle's specific dwell — stated
here as the resolution of that specific gap, not a general closure of the
Tier-2 item (a coupling test at a DIFFERENT dwell, e.g. much shorter than
either time constant, remains untested and is not claimed to be answered
by this cycle).

**Final configuration:**

- **Block A**: 16-point grid (Hosts A–D × RATIOS∈{1e-9,1e-5,1e-3,1e-1},
  Host E and r=1.0 excluded per `lab/kinetics.py`'s own
  `realizability_tier`). Reading (b) (ΔT_ss_full × n_at_dwell) is the
  SOLE scored reading for NETD classification. Reading (a) is computed and
  reported, labeled explicitly as an artifact solving no physical model on
  this grid, excluded from falsification scoring. Host C's 4 points get an
  explicit closed-form coupled kinetics-thermal ODE evaluation
  (`coupled_kinetics_thermal_dT`, Red Team's own derivation, independently
  verified by the Director against `scipy.integrate.odeint` to
  <4×10⁻⁴ relative error before committing) compared against the decoupled
  shortcut.
- **Block B**: RSA subclass reversal, TPA OOM recompute, 45m↔50yd
  cross-reference — arithmetic only, no new search this cycle.
- **Block C**: 3λ ratio-flatness check on exp-026's already-committed
  `beam_scene` data.

### Idealizations (stated explicitly, before any run)

- Block A reuses exp-043's reference ceiling (ΔT_ss_full — computed from
  the same irradiance/σ_ext/ratio/area chain), witness irradiance, and
  dwell **verbatim, not re-derived**. Any future correction to those
  upstream numbers propagates directly into Block A's absolute numbers.
- The known h_conv under-correction (~3 OOM, THERMO's Iteration-20
  finding, reused not re-derived this cycle) means every steady-state ΔT
  and NETD classification below is an **upper bound** — a corrected
  h_conv would push every UNDETECTABLE margin further from threshold, not
  closer. Iteration-21 priority #2 (the actual re-derivation) stays
  deferred, THERMO's own judgment call on the correct gas-conduction
  correlation.
- The `iso_xsec_sq` area convention is **proven area-invariant** for
  `steady_state_delta_T` (corrected per mandatory fix 2) — Block A's
  numbers do not depend on, and will not rescale under, a future T22
  area-convention revision. (They WOULD depend on a revision to the
  underlying σ_ext/ratio measurement itself, a different question.)
- Host lifetimes (the k_r grid) are inherited from exp-038/exp-037's own
  citations (Soref & Bennett 1987) plus two MATERIALS-owned tier
  boundaries — not re-sourced this cycle.
- `theta_beam`=10° (feeding `dwell_central`) is exp-043's own flagged
  lower-confidence, not independently WebSearch-confirmed figure —
  inherited uncertainty, not resolved here.
- Block C confirms the BENCH ARTICLE's own achromatic-by-construction
  idealization is self-consistent as measured (0.45% relative spread); it
  does NOT establish that a real physical σ(I) mechanism reaching this
  dynamic range would itself be broadband — T18's own narrowband finding
  for real mechanisms stands, unresolved by this cycle, and Block A's
  UNDETECTABLE headline should be read with that caveat for any reader
  translating it toward a REAL material's expected behavior.
- **NETD is an instrument/detector threshold, not a human perceptual
  one.** No prediction in this experiment bears on constraint-3/4's
  human-eye verdict — restated at every point of claim below, per
  mandatory fix 6.
- Block B is citation-correction-only; performs no new literature search
  this cycle (T18's WebFetch blockage is not separately reconfirmed here
  since no search was attempted).
- Zero new trust-suite gates, zero new code beyond this experiment's own
  `run.py` — pure reuse of already-gated (`lab/kinetics.py` stage 12,
  `lab/thermo_sidecar.py` stage 15) machinery plus one new, independently-
  verified closed-form function (`coupled_kinetics_thermal_dT`) that
  computes no FDTD field and is checked against a second independent
  method (`scipy.integrate.odeint`) before being trusted, in lieu of a
  full trust-suite stage for a single-cycle desk derivation (proportionate
  to PANEL.md's own "new machinery ⇒ new stage" rule, which this program
  has applied to reusable multi-cycle modules, not one-off closed-form
  checks — flagged here as a scope judgment, not silently assumed).

### Per-metric predictions, falsifiable, committed BEFORE any run

| ID | Prediction | Band |
|---|---|---|
| P-IT21-A1 | Reading-(b) ΔT spans ≥7 orders of magnitude across the 16-point grid | min ∈ [1×10⁻¹³, 1×10⁻¹¹] K (Host A/B, r=1e-9); max ∈ [3×10⁻⁴, 4.5×10⁻⁴] K (Host A/B, r=1e-1) |
| P-IT21-A2 | Every one of 16 points classifies UNDETECTABLE (reading b, netd_lo=0.020K) — **NETD is an instrument/detector threshold, not a human perceptual one; this does NOT bear on constraint-3/4's human-eye verdict** | worst-case margin (netd_lo/max_dT) ∈ [30×, 80×] |
| P-IT21-A3 | Host C's exact coupled-ODE solution matches the decoupled shortcut (reading b) at all 4 points, given dwell clears both τ_kinetics and τ_thermal by ≳45× (comfortably past this codebase's own 25× convergence bar) | relative difference ≤ 1×10⁻² at every point; hard falsification if any point exceeds 1×10⁻¹ (would mean the intermediate-regime concern is real at this specific dwell, not just in general) |
| P-IT21-A4 | Reading (a) exceeds reading (b) by orders of magnitude at every PUBLISHED-tier point (Hosts A/B × r≤1e-3), demonstrating it is an artifact, not a comparably-legitimate alternative | ratio ≥ 100× at every PUBLISHED point; central expectation ≥ 1000× |
| P-IT21-B1 | RSA subclass onset/witness ratio reverses sign relative to the old (unsourced) framing | onset/witness-central ∈ [13, 17]; onset/witness-hi ∈ [1.8, 2.6] — both >1, i.e. onset now sits ABOVE the witness range |
| P-IT21-B2 | TPA OOM gap recomputed at the new witness irradiance | central range ∈ [10.0, 15.0] OOM (widened from the original 9–12) |
| P-IT21-B3 | 50 yards matches the carried, unsourced 45.0m witness distance | relative difference ≤ 3% |
| P-IT21-C1 | ON-endpoint article's σ_abs/σ_ext ratio is near-flat across 450/600/750nm (already-committed exp-026 data) | relative spread ≤ 1.5% across the 3λ sweep |

Predictions committed to git in this same commit, before Block A/B/C's
`run.py` is executed (house discipline, non-negotiable).

## PHASE 4 — TEST (run 2026-08-18)

Bench reverified 41/41 (no `lab/` change this cycle). Zero new FDTD calls,
<1s. Results committed alongside this section.

**Block A** (16-point grid, reading b scored): min ΔT = 1.919×10⁻¹² K
(Host D, r=1e-9 — the slowest-kinetics host, not Host A/B as first
guessed by hand, because Host D's own τ_kinetics≈0.1s is comparable to
the 66.7ms dwell, so it never fully relaxes even toward its own tiny
n_ss); max ΔT = 3.585×10⁻⁴ K (Hosts A/B/C all converge to
near-identical values at r=1e-1, effectively a three-way tie — Host C's
own point edges out A's by floating-point noise, not a real difference).
**P-IT21-A1 CONFIRMED** (min inside [1e-13,1e-11]K, max inside
[3e-4,4.5e-4]K). **P-IT21-A2 CONFIRMED**: all 16 points UNDETECTABLE,
worst-case margin 55.8× below netd_lo — **NETD is an instrument/detector
threshold, not a human perceptual one; this does NOT bear on
constraint-3/4's human-eye verdict.** **P-IT21-A3 CONFIRMED, exceeded**:
Host C's exact coupled-ODE solution and the decoupled shortcut agree to
0.00e+00 relative difference at every one of the 4 points (displayed
precision) — the intermediate-regime concern (τ_kinetics/τ_thermal≈
0.66–0.73) does not translate into any measurable endpoint discrepancy AT
THIS DWELL, because dwell clears both time constants by ≳45×, far past
the codebase's own 25× convergence bar. **This is a resolution, not a
dismissal, of the T22-flagged concern** — the shortcut is validated at
this specific dwell, not proven valid in general for any future
shorter-dwell scenario. **P-IT21-A4 CONFIRMED**: reading (a) exceeds
reading (b) by exactly 1001× at the tightest PUBLISHED-tier point (r=1e-3,
Hosts A/B) and by up to 10⁹× at r=1e-9 — Red Team's "solves no physical
model" characterization holds quantitatively, not just qualitatively.

**Block B**: RSA onset/witness-central = 15.2× [predicted 13–17],
onset/witness-hi = 2.27× [predicted 1.8–2.6] — **P-IT21-B1 CONFIRMED**.
TPA OOM central range [11.2, 14.2] [predicted 10.0–15.0] — **P-IT21-B2
CONFIRMED**, widened from the original 9–12 as MATERIALS' Phase-1
reasoning predicted. 50 yards = 45.72m, 1.6% from the carried 45.0m
[predicted ≤3%] — **P-IT21-B3 CONFIRMED**.

**Block C**: per-λ ratio 0.6056/0.6075/0.6083 at 450/600/750nm, spread
0.271 percentage points / 0.447% relative [predicted ≤1.5%] — **P-IT21-C1
CONFIRMED**.

**Full predictions scorecard: 8 of 8 CONFIRMED** (`results.json::
predictions_scorecard`) — unusually clean, but honestly explainable
rather than suspicious: every Block A/B number was already independently
re-derived by hand by at least two of the five Phase-2 seats plus Red
Team before this run, so Phase 4 mostly re-confirms closed-form
arithmetic already checked three ways, not a fresh empirical surprise.

**Explicit disposition on items not touched this cycle** (house
discipline — state a deferral, don't let it go silent): Iteration-21
priority #2 (THERMO's h_conv/mass_kg re-derivation) and #3 (EM's
geometric-disk-vs-`iso_xsec_sq` table entry, T22) remain deferred, exactly
as scoped at Phase 1/3 — this cycle's Block A caveat states the KNOWN
direction of #2's correction but does not apply it. T21's contamination-
risk question and QUANTUM's aperture-consistent beam check
(Iteration-19/20 carryovers) are untouched this cycle, not silently
dropped.
