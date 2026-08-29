# PHASE 5 — REVIEW · Seat: THERMODYNAMICS · Panel Iteration 66 · exp-089

Fresh sub-agent, blind to any other seat's current-cycle Phase-5 review. Read
in full: PANEL.md; LOGBOOK.md's RULED OUT (R1–R14) and ESTABLISHED sections;
LIVE THREADS/T28 through Iteration 65/exp-088 (both CHECKPOINT entries); the
complete exp-089 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `results.json`,
`run.py`); exp-088's `phase5_review_thermodynamics.md` for house-style
calibration (its own σ_ext-differential decomposition method is reused and
extended here, not merely cited); `lab/thermo_sidecar.py` source directly.

## Verdict

**CONCUR with PARTIAL, on the energy-ledger axis, with one load-bearing
mechanistic clarification this cycle's own record does not yet state
explicitly.** Every number in NOTES.md's Result section that touches my
charter — Q1's floor margins, Q3's `ratio_k` readings, Q6's combined
classification, Q7's NETD/T9-anchor chain, the R14(a) smoothness gate —
independently reproduces exactly from raw primitives (below). The
Combined Verdict's own headline claim ("the single-node-artifact reading
does not survive") is correct as far as it goes, but the record as filed
never asks *which half of `ratio_k` is doing the work* at the two new
ENERGY-DOMINANT angles, even though this is squarely my seat's own
territory (`frac_p_abs`, the numerator, is an absorbed-power quantity) and
the task this cycle exists to answer per R14 discharge. I answer it below:
**the jump is overwhelmingly a denominator (ambient-contrast) effect, not
a numerator (absorbed-power) effect** — roughly 90%/10% in log terms, at
both angles, independently and reproducibly. This matters for Q5: R13's
floor gate was defending against the *right* quantity, just with too loose
a threshold — not a wrong-target diagnosis. I also find one genuine,
fixable disclaimer-scoping gap (Q7 vs. Q3) that this sub-thread's own
four-times-fired erosion pattern makes worth closing before it becomes a
fifth instance.

## Independent recomputation

### A. Primitives reproduce exactly

Pulling `results.json::thermo`/`frac_p_abs`/`frac_contrast_new_angles`/
`ratio_k_new_angles` directly and recomputing from the raw `sigma_ext_cells`/
`ratio_abs_ext_raw`/`p_abs_w` fields (not trusting the persisted derived
keys):

| θ | `p_abs_w`(C40) | `p_abs_w`(G40) | `frac_p_abs` (recomputed) | file value |
|---|---|---|---|---|
| 37.2° | 2.812704×10⁻¹² | 2.808673×10⁻¹² | 1.43333×10⁻³ | 1.43333×10⁻³ ✓ |
| 40.2° | 3.077251×10⁻¹² | 3.055402×10⁻¹² | 7.10042×10⁻³ | 7.10042×10⁻³ ✓ |
| 41.4° | 3.164949×10⁻¹² | 3.187843×10⁻¹² | 7.23339×10⁻³ | 7.23339×10⁻³ ✓ |

All three bit-exact. `ratio_k = frac_p_abs/frac_contrast` reproduces exactly
at all three angles (3.4433, 25.0820, 28.8072). Q7's NETD margins
independently recomputed from `dt_ss_full_K` against `NETD_BAND_K=(0.020,
0.050)` (traced to `experiments/087-.../run.py`, unchanged, reused verbatim
through the `exp088→exp089` import chain — confirmed by direct read of both
files' `L_GEOMETRIC_M`/`IRR_CENTRAL_W_CM2`/`NETD_BAND_K` re-exports): margins
**382.8×–433.4×** — matches NOTES.md's cited "382×–434×" exactly. `ratio_abs_ext`
0.51264–0.51509 across all 6 cells, within 0.5–1.0% of T9's 0.51 anchor —
confirmed. R14(a) smoothness gate: independently re-verified from
`r14a_smoothness_gate::steps` that both `p_abs_w(C40,θ)` and `p_abs_w(G40,θ)`
are strictly non-decreasing across all 7 consecutive steps of the sorted
8-point angle list — genuinely PASS, not merely asserted.

### B. The load-bearing decomposition: numerator vs. denominator

Extending exp-088's own established method (my seat's Taylor decomposition of
`frac_p_abs` through `p_abs_w = ratio_abs_ext × I × (σ_ext_cells·dx_m)²`,
confirmed from `lab/thermo_sidecar.py::absorbed_power_established_ratio`
directly — quadratic in σ_ext) across the full, now 8-point, combined set:

```
frac_p_abs(θ) ≈ 2·[σ_ext(G40,θ)−σ_ext(C40,θ)]/σ_ext(C40,θ) + [ratio(G40,θ)−ratio(C40,θ)]/ratio(C40,θ)
```

| θ | fracΔσ_ext (%) | fracΔratio_abs_ext (%) | 2·t1+t2 | exact `frac_p_abs` (signed) |
|---|---|---|---|---|
| 36.0° | +0.0696 | +0.0573 | +0.001964 | +1.9655×10⁻³ |
| 37.2° | **−0.0370** | **−0.0693** | −0.001434 | −1.4333×10⁻³ |
| 38.4° | +0.0263 | +0.0777 | +0.001304 | +1.3041×10⁻³ |
| 38.6° | +0.1703 | +0.0589 | +0.003996 | +4.0006×10⁻³ |
| 38.8° | +0.2844 | +0.0257 | +0.005946 | +5.9552×10⁻³ |
| 40.2° | **−0.3532** | −0.0049 | −0.007113 | **−7.1004×10⁻³** |
| 41.4° | +0.3453 | +0.0313 | +0.007219 | +7.2334×10⁻³ |
| 41.8° | +0.3732 | −0.0261 | +0.007202 | +7.2142×10⁻³ |

Decomposition reproduces exact `frac_p_abs` to <0.2% relative at both new
angles (0.18% at 40.2°, 0.20% at 41.4° — consistent with exp-088's own
<0.5% figure). Three findings from this table, all new this cycle:

1. **The σ_ext-differential term is the dominant driver of `frac_p_abs` at
   both new angles**, exactly as it was at 38.4°/38.8° (my seat's own
   exp-088 finding) — `ratio_abs_ext`'s own differential term stays a small,
   T9-flat-consistent residual (0.005–0.031%) throughout, never the leading
   term at these two angles. Nothing anomalous in the absorption/scattering
   partition.
2. **The raw signed `p_abs_w(G40,θ)−p_abs_w(C40,θ)` difference flips sign
   FOUR times across the 8-point set** (+ at 36.0°, − at 37.2°, + at 38.4°
   through 38.8°, − at 40.2°, + at 41.4° through 41.8°) — genuinely new
   information not reported anywhere in NOTES.md, which reports only the
   R14(a)-required parent-curve monotonicity (a different, and correctly
   PASSing, check — R14(a) tests the *parents*, not the *difference*, and
   is not violated by this). Interpolating zero-crossings of the signed
   difference gives spacings of ≈1.13°, 1.60°, 1.37° between successive
   flips — order-of-magnitude consistent with half of T28's own
   established ~2.84–2.95° period ([1.42°,1.475°]), though from only 4
   sparse crossings, not a formal fit. This is exactly the raw,
   zero-FDTD, descriptive-only kind of observation Q4 itself models for
   `frac_p_abs` proper (Idealization 13) — I report it in that same spirit,
   as a concrete, quantified motivation for R14(b)'s still-queued formal
   period fit (Idealization 14), not as a periodicity claim in its own
   right.
3. **The magnitude of the σ_ext-differential term at 40.2°/41.4° (0.35%)
   is NOT anomalously large** — it sits squarely inside the smooth,
   monotonically-growing envelope already established at 38.8° (0.28%) and
   41.8° (0.37%). `frac_p_abs`'s own modest growth from 38.8°→40.2°/41.4°
   (19–21%, not a spike) is the ordinary continuation of an
   already-established trend, further confirmed against NOTES.md's own Q4
   desk estimate (6.543×10⁻³/7.046×10⁻³ predicted vs. 7.100×10⁻³/7.233×10⁻³
   measured — 8.5%/2.6% off, unremarkable).

### C. The log-ratio attribution — the direct answer to the task

Using 38.8° (the last previously-established point) as baseline:

| θ | `frac_p_abs` ratio vs 38.8° | `frac_contrast` ratio vs 38.8° | `ratio_k` ratio vs 38.8° | numerator's log-share | denominator's log-share |
|---|---|---|---|---|---|
| 40.2° | 1.1923× | 0.18414× (a **5.43× collapse**) | 6.477× | **9.4%** | **90.6%** |
| 41.4° | 1.2146× | 0.16331× (a **6.12× collapse**) | 7.439× | **9.7%** | **90.3%** |

(`log₁₀` decomposition: e.g. at 40.2°, `log₁₀(1.1923)=0.0764` vs.
`log₁₀(1/0.18414)=0.7349`, sum `0.8112 ≈ log₁₀(6.477)=0.8112` — checks
exactly; same method at 41.4°.)

**This is the load-bearing recomputation this review contributes.**
`frac_p_abs` (the numerator, absorbed-power quantity, my seat's own
territory) grew by only ~19–21% from 38.8° to the two new angles — an
ordinary, trend-consistent increment, independently confirmed non-anomalous
by the σ_ext decomposition above. `frac_contrast` (the denominator,
ambient-contrast quantity, PHOTONICS'/VISION's territory) collapsed by
5.4×–6.1× over the same span — mechanistically unsurprising once you note
that 40.2° and 41.4° each sit within ≈0.06–0.07° of `delta_scene`'s own
independently-established, null-controlled real zero-crossings (40.265°,
41.461° — reproduced from `experiments/083-.../results.json` exactly,
matching all five Phase-2 critiques and Red Team's own audit). At both
angles, roughly nine parts in ten of the `ratio_k` jump (in log terms) is
the denominator falling toward its own zero, not the numerator doing
anything the established absorbed-power trend didn't already predict.

## Seat-specific analysis: does this change the Q5 floor-gate-adequacy
reading?

**No — it sharpens and confirms it, rather than reversing it.** The task
brief asks whether R13's floor gate (built on `frac_contrast`, the
denominator) was "defending against the wrong half of the ratio." My
recomputation answers this directly: **no, the gate is aimed at the correct
half.** The denominator genuinely is the dominant driver — R13's own design
premise (a ratio classifier with a real-zero-crossing-capable denominator
needs a floor gate on that denominator specifically) is *confirmed*, not
undermined, by this cycle's own data. What failed is not the *target* of
the gate but its *calibration*: `FLOOR_FRAC=0.10` let through two points
(1.31×, 1.48× margin) whose denominator was still close enough to its own
zero to produce a >6× collapse relative to the immediately preceding
sampled point. NOTES.md's own Learned item 2 ("FLOOR_FRAC=0.10 looks
materially too permissive") is directionally correct; this review supplies
the missing mechanistic confirmation for *why* — the gate's own target
quantity really is responsible for essentially all of the alarming signal,
so tightening it (or replacing it with a graduated caution zone, as Q5
itself proposes) is the right class of fix, not a change of target.

**A second, distinct finding: the Q7/Q3 disclaimer gap.** Q7's NETD chain
is correctly computed (§A) and correctly disclaimed against constraint-3/4's
human-eye verdict (Idealization 9). But nothing in NOTES.md decouples Q7's
calm UNDETECTABLE reading from Q3's alarming ENERGY-DOMINANT reading on
the *other* axis that actually matters here — the T28 confound-mechanism
question Idealization 10 itself names as this cross-check's real scope.
Both derive from the identical `p_abs_w(C40/G40,θ)` values, and this
review's own §B/§C show precisely why a calm Q7 is not informative about
Q3: Q7 tests the *absolute* magnitude of `p_abs_w` against a fixed detector
noise floor (and passes trivially — `p_abs_w` is femtowatt-scale everywhere,
nothing about the two new angles is special there); Q3's alarm comes almost
entirely from the *denominator*, a completely different, unrelated
ambient-contrast channel that Q7 never touches. Unlike Q4 — where Red
Team's own §7.1 finding and Idealization 13 explicitly, in writing, forbid
reading Q4's report as evidence about Q3 either way — no equivalent
sentence exists anywhere in this document for Q7 vs. Q3. Given this
sub-thread's own record (four independently-confirmed disclaimer-erosion
instances, CHECKPOINT criterion 4 fired at Iteration 65 on the fourth), a
future citation that reads "Q7 confirms nothing alarming was actually
absorbed" beside "Q3 found ENERGY-DOMINANT at two angles" is exactly the
muddled-narrative risk this sub-thread has now paid a firing for once
already. This is the same class of gap Red Team's own §7.1 attack
identified for Q4 — it was simply never asked of Q7, because Q7 is my
seat's own extension and nobody else's charter looks for it.

## Sharpest finding

**`ratio_k`'s ENERGY-DOMINANT jump at 40.2°/41.4° is, quantitatively and
reproducibly (~90%/10% in log terms at both angles), a denominator
(`frac_contrast`, ambient-contrast) effect, not a numerator (`frac_p_abs`,
absorbed-power) effect — `frac_p_abs` grew only ~19–21% along its
already-established, σ_ext-differential-driven trend, while `frac_contrast`
collapsed 5.4×–6.1× approaching its own two independently pre-established
zero-crossings.** This is the direct, load-bearing answer to this cycle's
own R14-framed question, and it settles Q5 the same direction NOTES.md's
own Learned section already leans (the gate's calibration, not its target,
is the problem) — but with an actual mechanistic number behind it rather
than an inference from two floor-margin readings. Nothing in the filed
record currently states this attribution explicitly, even though the
record's own R14(a) gate (confirmed PASS, independently re-verified above)
was the exact machinery needed to make the check possible.

## Ranked top-3 for the Iteration-67 queue

1. **Add the Q7-vs-Q3 decoupling disclaimer, mirroring Idealization 13's
   Q4-vs-Q3 treatment, before this cycle's own Q7 UNDETECTABLE finding is
   cited anywhere else.** Zero-FDTD, one sentence: Q7's calm reading bears
   on absolute detectability against a fixed instrument floor, not on
   whether Q3's `ratio_k` finding is real or an artifact — the two draw on
   the same `p_abs_w` inputs but answer unrelated questions, and this
   cycle's own §C decomposition shows precisely why. This closes the
   procedural gap before it becomes this sub-thread's fifth
   disclaimer-erosion instance in a shape nobody has yet named for Q7
   specifically.
2. **Recalibrate `FLOOR_FRAC` (or replace the binary gate with a graduated
   caution zone), now backed by a mechanistic confirmation that the gate's
   target — not merely its threshold — is correct.** This review's §B/§C
   removes the antecedent uncertainty Q5 itself flagged (whether the gate
   might be defending the wrong quantity): it is not. A revised threshold
   or caution-zone design can proceed directly against `frac_contrast`
   without first re-litigating whether `frac_p_abs` needs its own floor
   gate too (it does not show zero-crossing-capable behavior anywhere in
   this 8-point record).
3. **Run the still-queued formal null-controlled period fit against the
   raw signed `p_abs(G40,θ)−p_abs(C40,θ)` difference (R14(b)/Idealization
   14).** Now concretely motivated, not merely named: this review's own
   zero-FDTD desk finding (§B.2) shows the signed difference already flips
   sign four times across the 8 sampled points, at spacings loosely
   consistent with half of T28's established period — exactly the kind of
   evidence that should be formally, null-controlled-ly tested (R5/R10
   discipline) rather than left as a suggestive but unfit observation.

## Files consulted (read/executed directly)

- `/home/user/photon-lab/PANEL.md`, `/home/user/photon-lab/LOGBOOK.md`
  (RULED OUT R1–R14 in full, ESTABLISHED, LIVE THREADS/T28 through
  Iteration 65/exp-088 in full, both CHECKPOINT entries)
- `/home/user/photon-lab/experiments/089-t28-combined-angle-census/`
  `phase1_proposal.md`, `phase2_critique_{photonics,materials,em,quantum,
  thermodynamics}.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
  `NOTES.md`, `results.json`, `run.py`
- `/home/user/photon-lab/experiments/088-t28-node-bracket-r13-floor-gate/
  results.json` (`thermo`, `frac_p_abs`, `frac_contrast_new_angles`,
  `retroactive_exp087_reclassification`) and `phase5_review_thermodynamics.md`
  (house-style calibration — decomposition method reused and extended, not
  deferred to)
- `/home/user/photon-lab/experiments/087-t28-energy-interception-poynting-check/
  results.json` (`thermo` for 36.0°/38.6°/41.8°) and `run.py` (source of
  `NETD_BAND_K`/`L_GEOMETRIC_M`/`IRR_CENTRAL_W_CM2`, traced through the
  exp088→exp089 import chain)
- `/home/user/photon-lab/experiments/083-.../results.json::per_theta`
  (zero-crossing/`delta_scene` cross-check)
- `/home/user/photon-lab/lab/thermo_sidecar.py`
  (`absorbed_power_established_ratio`, `netd_disposition` read directly)
