# PHASE 4 — RESULTS · Panel Iteration 42 · exp-065

144 FDTD calls, 16.7 min wall (well inside the 90-min hard stop). Both
absolute-identity gates **PASSED before any other result was read**, per
the frozen halt discipline.

---

## Gates

**G-1 (P-VIS42-1, anchor identity)**: all 12 C40 rows at θ∈{±38,±40}×
{450,600,750} reproduce `experiments/041-t20-angle-audit/results.json::
block_main` **exactly** — `Δ = 0.0` (float64) at all 12, loaded
programmatically. **PASSED.**

**G-2 (P-VIS42-1b, static construction identity — the replacement for the
Phase-3-voided dynamic causal gate)**: `damp_e`/`damp_hx` bit-identical at
all six scored-window×array combinations between C40 and G40, offset by
`pad=40`; scored window confirmed pure vacuum. **PASSED at 0.000e+00**
(verified pre-freeze, re-confirmed at Phase 4 launch).

---

## Scored predictions, as frozen (STEPS=1400 throughout, per the committed design)

| ID | Verdict | Key number(s) |
|---|---|---|
| P-VIS42-2 (HEADLINE) | **REFUTED** (absolute transfer) | median 0.00279, max 0.00836 (bands: confirm ≤1.0e-3/≤3.0e-3; refute ≥2.0e-3/≥7.0e-3) |
| P-VIS42-2a (aliasing) | CONFIRMED (smooth, non-aliased) | 0/6 cells depart >2× the C60/C80 interpolant |
| P-VIS42-3 (scaling) | CONFIRMED (scales with reading) | Spearman ρ = 0.562 |
| P-VIS42-4 (naive dominates) | CONFIRMED | N60 exceeds C60 at 16/18 cells, median\|Δ(N60−C40)\| = 0.00395 |
| P-VIS42-5 (pad-only null) | **REFUTED** | max abs_dev = 0.01358 (750nm/+40°); bar was ≤5e-4 |
| P-VIS42-6 (N9 floor) | CONFIRMED | C_empty,N9 = −3.3e-5 (C40) / −1.3e-4 (C80), both ≪ GATE_HARD |
| P-VIS42-7 (article row) | CONFIRMED | C = −0.00450 (C40) / −0.00460 (C80), both bucket **MARGINAL**, Δ=1.0e-4 |
| P-VIS42-8 (T24 provenance) | CONFIRMED | both cells reproduce to ≤1% (C40) and ≤25% (Δ40→60) |
| P-VIS42-9 (cross-channel ratio) | PARTIAL | ratio 0.364 (bands: confirm [0.02,0.30], refute ≥0.6 or ≤0.005) |
| P-VIS42-10 (mini-sweep, falsifies "cancels to first order") | **REFUTED** | peak-to-trough/mean = 11.9 (bar: confirm ≤2× as flat) |
| P-VIS42-11 (settling) | **REFUTED, LOAD-BEARING** | STEPS 1400→2800 moves C80/40°/600nm by **59.8%** relative (bar: confirm ≤0.15%) |

**These verdicts are reported exactly as scored against the pre-registered
bands, per house discipline — nothing here is adjusted after the fact.**
But P-VIS42-11's REFUTE reopens every other prediction's interpretation,
below.

---

## THE LOAD-BEARING FINDING: STEPS=1400 is not settled on this channel, and it dominates the headline

P-VIS42-11 was designed as one confirmatory check (Red Team attack 7 / the
T10 precedent). It came back a REFUTE nearly **400× past its own bar**
(59.8% vs a 0.15% confirm threshold) — large enough that it cannot be
dismissed as a minor caveat. **Following it up, rather than reporting it as
a footnote, is the single most important thing this cycle did.**

### Diagnostic 1 — is it padding-specific, or general?

Two extra legs (unscored, disclosed as a Director follow-up), same cell
(θ=40°, 600nm), STEPS 1400 vs 2800:

| config | C_empty(1400) | C_empty(2800) | rel Δ |
|---|---|---|---|
| C40 (unpadded, the 19-iteration anchor geometry) | −0.010965 | −0.002802 | **74.4%** |
| C60 (padded) | −0.007721 | −0.002442 | 68.4% |

**Not padding-specific.** The unpadded C40 geometry — the exact geometry
`experiments/041-t20-angle-audit` (Iteration 18) established this program's
±40° angle standard on, and every T21/T24 citation since has inherited —
shows the *larger* relative shift of the two. This is a property of the
**plane/tapered-source empty-scene channel at near-grazing angles
(±38°/±40°)**, not of this cycle's padding construction.

### Diagnostic 2 — convergence trend

C40/40°/600nm across four step counts:

| STEPS | C_empty |
|---|---|
| 1400 | −0.010965 |
| 2800 | −0.002802 |
| 4200 | −0.002801 |
| 5600 | −0.002802 |

**Clean, decisive convergence by 2800 steps** (flat to 4 significant
figures through 5600). This is real, well-behaved transient decay — not
noise, not instability, not a bug. STEPS=1400 catches this cell at
roughly **3.9× its own converged magnitude**. This is not the tiny
settling correction exp-046's own check (0.083%/0.036%) found and this
program has cited as reassurance since Iteration 23 — that check was run
on the **Gaussian-beam channel** (a focused, on-axis source, settles fast)
at the **same angles**, and does not transfer to the **plane/tapered
source, empty-scene, near-grazing-angle channel** this cycle actually
measured. NOTES.md's own idealization 3 flagged this exact gap before the
run; it turned out to be the cycle's real finding.

### Diagnostic 3 — does the headline survive settling correction?

The full 90-call Block SWEEP re-run at STEPS=2800 (all 5 configs × 6θ ×
3λ, disclosed as an R3-class same-shift follow-up, this program's own
standing precedent — exp-004→005, exp-022→023):

| | STEPS=1400 (frozen, scored) | STEPS=2800 (settled, disclosed) |
|---|---|---|
| median\|Δ(C80−C40)\| | 0.00279 | **0.00052** (5.4× smaller) |
| max\|Δ(C80−C40)\| | 0.00836 | **0.00383** (2.2× smaller) |
| Spearman ρ (scaling) | 0.562 | 0.595 (essentially unchanged) |

At STEPS=2800, the headline's **median now clears its own CONFIRM band**
(0.00052 ≤ 1.0e-3) — it would score CONFIRMED, not REFUTED. The **max**
still exceeds the CONFIRM band (0.00383 > 3.0e-3) but is now far from the
REFUTE band (≥7.0e-3) — landing in PARTIAL territory, not the clear
absolute-transfer REFUTE the frozen (unsettled) data reported.

**Where the residual max lives**: overwhelmingly 750nm (cpl=25). At
STEPS=2800, C80's own 750nm cells still show visibly larger deltas
(0.0032–0.0038) than 600nm's (≤0.0006) — see the full per-cell table in
`/tmp` scratchpad, reproduced below for the record:

```
lam  theta   C40        C60        C70        C80        N60      | d80=C80-C40
450  -40.0  -0.009529  -0.009283  -0.009123  -0.009080  +0.005177 | +0.000449
450  +40.0  -0.009217  -0.008934  -0.008786  -0.008758  +0.004115 | +0.000459
600  -40.0  -0.003559  -0.003216  -0.003147  -0.003368  -0.008441 | +0.000191
600  +40.0  -0.002802  -0.002442  -0.002397  -0.002635  -0.008808 | +0.000167
750  -40.0  -0.008888  -0.008831  -0.006449  -0.005282  +0.004204 | +0.003605
750  +40.0  -0.009360  -0.009027  -0.006645  -0.005534  +0.003610 | +0.003826
```
(full 18-cell table in the scratchpad JSON; ±35°/±38° cells follow the
same pattern — 750nm carries most of the residual)

**Candidate mechanism for the residual, disclosed not resolved**: source
ramp length is `ramp_periods * lam_cells / S` (`lab/fdtd2d.py::
add_line_source`) — at fixed `ramp_periods=3.0`, 750nm's `cpl=25` gives a
**67% longer ramp**, in steps, than 450nm's `cpl=15`. STEPS=2800 may
simply not be enough steps at 750nm specifically, compounding with the
larger padded domains' own longer settling path. **Not verified this
cycle** — the convergence trend (Diagnostic 2) was only run at 600nm/C40;
a matching trend check at 750nm/C80 is the obvious next confirmatory step
and is queued for Phase 5/Iteration 43, not run here (budget and scope
discipline: this cycle's own follow-up work is already well beyond its
frozen design, and further speculation without a matching diagnostic
would repeat the R4/R5 mistake this program's house rules exist to
prevent).

### What this means for P-VIS42-3/4/5/9/10

- **P-VIS42-3** (scaling, ρ): essentially unchanged (0.562 → 0.595) —
  this discriminator is robust to the settling confound, both readings
  point the same direction (scales with reading ⇒ relative-transfer
  leaning), and its CONFIRM already held under both.
- **P-VIS42-5** (pad-only null): its REFUTE is dominated by the same
  750nm/+40° cell (abs_dev 0.0136, by far the largest of the 9) — the
  same settling-affected cell class. Not re-run at STEPS=2800 this cycle;
  flagged as very likely to shrink substantially under the same
  correction that shrank the headline, not confirmed.
- **P-VIS42-9** (cross-channel ratio): computed from the unsettled plane
  median (0.00279) against the beam-channel median (which settles fast,
  per exp-046 — not itself suspect). Under the settled plane median
  (0.00052), the ratio becomes 0.00052/0.004725 ≈ **0.11** — squarely
  inside the CONFIRM band [0.02, 0.30], not PARTIAL.
- **P-VIS42-10** (mini-sweep oscillation): NOT re-run at STEPS=2800.
  This is the least certain of the group — an oscillating delta at
  STEPS=1400 could be (a) genuine coherent-fringe perturbation (the
  hypothesis it was built to test), (b) an artifact of comparing two
  differently-unsettled configurations at slightly different angles, or
  some mixture. **Genuinely open**, not resolved by this cycle's
  follow-up work, and the single most important item for Iteration 43.

---

## Honest bottom line

**T24's own inheritance question — does its beam-channel boundary
systematic transfer to the plane/ambient channel as absolute or relative
— is NOT decided by this cycle, for a different reason than either
hypothesis it was built to test.** The frozen (STEPS=1400) data would say
"absolute transfer, alarming" (P-VIS42-2 REFUTED); a same-shift settling
correction says "mostly relative transfer, unalarming, with a real but
smaller and not-yet-fully-characterized residual, concentrated at 750nm"
(P-VIS42-2 would score CONFIRMED-to-PARTIAL). **Both readings cannot be
right, and the settling evidence (a clean, four-point, 2.2×10⁻⁵-precision
convergence series) is far stronger than the single-STEPS-value headline
it corrects.**

**The bigger finding is not about T24 at all.** `experiments/041-t20-
angle-audit` (Iteration 18) established this program's own ±38°/±40°
angle standard, at STEPS=1400, on the identical plane/empty-scene channel
this cycle just showed is ~3.9× off from its converged value at that step
count. `experiments/042-t21-magnitude-bridge` (Iteration 19) fitted T21's
entire edge-diffraction fringe model to those same MAIN-block rows.
**Every citation of those numbers since Iteration 18 — nineteen iterations
— may rest on an unsettled transient reading, not steady-state physics.**
This cycle did not set out to find that, found it by chance via a
mandatory-fix docket item (Red Team attack 7) that could easily have been
treated as a minor caveat, and confirmed it is real, large, and
(at 600nm at least) cleanly resolved by doubling STEPS.

**This is squarely Phase-5/Red-Team territory to rule on** — whether it
constitutes a Checkpoint-criterion-4 finding (a load-bearing instrument
gap silently inherited across a large fraction of this program's
constraint-3-adjacent record, discovered but not disclosed until now),
and what the correct remediation scope is (a single re-verification of
the ±38°/±40° MAIN-block anchor at STEPS≥2800, or a broader audit of every
citation built on it). The Director does not pre-empt that ruling here.

---

## Phase-5 corrections (applied same-shift, before Red Team's final audit)

Six blind Phase-5 reviews found three real gaps in this document's own
completeness. Applied here rather than left silent:

1. **[PHOTONICS' catch, R4-class]** Diagnostic 2's four-point convergence
   series (1400/2800/4200/5600) existed only as prose above — the one
   figure in this experiment not produced by committed code, exactly the
   defect class R4 exists to police. **Fixed**: `settling_trend_
   diagnostic.py` now reproduces it exactly (`settling_trend_diagnostic_
   output.txt`, committed) — `-0.010965 / -0.002802 / -0.002801 /
   -0.002802`, bit-for-bit what was reported.

2. **[MATERIALS' and VISION SCIENCE's catch, independently converged, more
   severe than this document's own original framing]** This document's
   "What this means for P-VIS42-3/4/5/9/10" section implied the settling
   confound is concentrated at the grazing ±38°/±40° angles and that Block
   ARTICLE (scored via `FALLBACK_ANGLES`, which includes ±35° but is
   mostly interior angles) might be comparatively insulated. **That is
   wrong, checked directly against `settled_sweep_steps2800_diagnostic.
   json`**: the ±35° legs — themselves inside `FALLBACK_ANGLES`, feeding
   Block ARTICLE's own N9 aggregate directly — **sign-flip** between
   STEPS=1400 and 2800, not just shift in magnitude:

   | cell | C_empty(1400) | C_empty(2800) |
   |---|---|---|
   | C40, θ=−35°, 600nm | **+0.00112** | **−0.00440** |
   | C40, θ=−35°, 750nm | **−0.00095** | **+0.00552** |
   | C80, θ=−35°, 600nm | (n/a, not independently checked at 1400 outside frozen SWEEP) | −0.00302 |
   | C80, θ=−35°, 750nm | (n/a) | +0.00615 |

   **Block ARTICLE's own P-VIS42-6/7 CONFIRMED verdicts are NOT insulated
   from the settling confound.** They were scored entirely from STEPS=1400
   inputs at exactly the angle (±35°) now shown to sign-flip under
   correction. Neither P-VIS42-6 (the N9 empty floor) nor P-VIS42-7 (the
   article row's MARGINAL bucket) has been re-verified at a settled STEPS
   value. **Both should be treated as unconfirmed pending that re-run**,
   not as this document's original text stated. The four purely-interior
   `FALLBACK_ANGLES` (0°, ±5°, ±15°, ±25°) remain untested at any STEPS
   beyond 1400 — the scope of the settling gap across angle is not fully
   mapped even now.

3. **[THERMODYNAMICS' catch]** Red Team's Phase-2 mandatory-fix item 8
   ("name explicitly what is being traded off by choosing this item over
   PLAN.md's top-ranked CNT `R_contact` term") was recorded as "Applied" in
   `phase3_synthesis.md`'s disposition table but the sentence was never
   actually written into any document — a real delivery failure, not a
   disclosure choice. **Stated here, now**: this cycle spent its FDTD
   budget on the T24 `ABSORB` boundary question and its own unplanned
   settling follow-up, not on sourcing the CNT-forest root-to-substrate
   thermal contact resistance (PLAN.md's #1 ranked item, THERMODYNAMICS'
   own charter, the only carried item that can move TD-5's 7.8× margin).
   That item is unmoved by this cycle in either direction and remains
   ranked #1 for a future THERMODYNAMICS-led cycle, independent of
   anything found here.

## Idealizations realized during Phase 4 (beyond NOTES.md's pre-registered list)

12. **STEPS=1400 is confirmed NOT settled** for the plane/tapered-source,
    empty-scene channel at ±38°/±40° — general to this channel/angle
    class, not specific to this cycle's padding construction (Diagnostic
    1). Every number in this experiment computed at STEPS=1400 (i.e.
    everything except the disclosed STEPS=2800 follow-up sweep) inherits
    this uncertainty.
13. The STEPS=2800 follow-up sweep is itself **not proven fully converged
    at 750nm** — only 600nm/C40 received the 4-point trend check. 750nm's
    residual delta may still include an unresolved settling component.

## Result

See "Honest bottom line" above. In one sentence: **this cycle's headline
question is undecided, and it uncovered a larger, program-wide settling
gap in the ±38°/±40° angle standard that has stood since Iteration 18.**

## Learned

1. A mandatory-fix docket item added almost as due diligence (Red Team
   attack 7, itself citing this program's own T10 precedent) surfaced the
   cycle's real finding — the discipline of never skipping a "boring"
   robustness check, even under time pressure, paid for itself decisively
   here.
2. STEPS calibrated on one channel (Gaussian beam, exp-046) does not
   transfer to a structurally different channel (tapered plane source,
   empty scene) at the same angles — a settling check is per-channel, not
   per-geometry.
3. The desk propagator's exact degeneracy (§2.4/§2 of `design_geometry.py`)
   proves the STEADY-STATE target is identical across the congruent
   series — it says nothing about whether STEPS is enough to REACH that
   target, and cannot be used as a substitute for a settling check. This
   was stated as a caveat in the proposal (§8.3 discussion) and turned out
   to be exactly right.

## Next

Ranked for Phase 5 to weigh, not a ruling:
1. Re-verify `experiments/041-t20-angle-audit`'s own MAIN-block ±38°/±40°
   rows at STEPS≥2800, and determine how many downstream citations (T21,
   T24, any near-threshold constraint-3 number built on them) are
   affected.
2. A matching 4-point convergence trend check at 750nm/C80 (or another
   large-padding/high-cpl cell) to determine whether STEPS=2800 is
   actually sufficient there, or whether the residual seen in Diagnostic 3
   is itself unsettled.
3. If confirmed, T24's own original inheritance question should be
   re-scored cleanly at a verified-settled STEPS value — this cycle's own
   construction (the congruent ABSORB series, the C70 non-aliased point,
   the static construction identity gate) is reusable as-is; only STEPS
   needs correcting.
