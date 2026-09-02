# Phase-5 Review — THERMODYNAMICS seat, Panel Iteration 78 (exp-101)

Fresh sub-agent for this Phase-5 pass (I am the same seat that filed
`phase2_critique_thermodynamics.md` this cycle, which found the R21
third-strike risk — the single highest-priority fix in that packet, per
Red Team's own §4 tally). This review re-derives everything from
`results.json` directly; nothing below is taken on NOTES.md's word.

## 0. Verdict

**Support.** The Tier-0 closed-box fix is sound and correctly executed; my
own mandatory fix (R21 narration) landed and is discharged — see §1. One
genuine, previously-uncaught defect remains, confined entirely to my own
charter's territory (§3): NOTES.md's Thermal-sidecar paragraph mislabels a
cross-section quantity as "absorbed power" and overstates how closely it
tracks the real `p_abs_w`/`dt_ss_full_K` trend. It does not change the
UNDETECTABLE classification (the margin is enormous — see §1) and does not
block this cycle, but it is a correctness defect in Result prose that none
of the five Phase-2 critiques, the Red Team audit, or NOTES.md's own
Learned section caught, because none of them existed after the run (Phase-2
predates Phase 4) and NOTES.md is the interested party.

## 1. R21 third-strike risk — independently re-verified against raw `results.json`

I grepped `results.json` directly (not NOTES.md's prose) for every one of
the 6 angle rows' `netd_classification_c`/`netd_classification_g`,
`p_abs_w_c`/`p_abs_w_g`, and `dt_ss_full_K_c`/`dt_ss_full_K_g` fields:

| θ (deg) | `p_abs_w_c` | `p_abs_w_g` | `dt_ss_full_K_c` | `dt_ss_full_K_g` | `netd_c` | `netd_g` |
|---|---|---|---|---|---|---|
| 37.127246 | 2.7866e-12 | 2.7751e-12 | 4.5780e-05 | 4.5592e-05 | UNDETECTABLE | UNDETECTABLE |
| 38.590230 | 2.9136e-12 | 2.9367e-12 | 4.7867e-05 | 4.8248e-05 | UNDETECTABLE | UNDETECTABLE |
| 39.200000 | 2.9625e-12 | 2.9714e-12 | 4.8671e-05 | 4.8817e-05 | UNDETECTABLE | UNDETECTABLE |
| 40.265420 | 3.0641e-12 | 3.0433e-12 | 5.0339e-05 | 4.9998e-05 | UNDETECTABLE | UNDETECTABLE |
| 41.460901 | 3.1589e-12 | 3.1885e-12 | 5.1898e-05 | 5.2384e-05 | UNDETECTABLE | UNDETECTABLE |
| 42.960901 | 3.3080e-12 | 3.2813e-12 | 5.4347e-05 | 5.3909e-05 | UNDETECTABLE | UNDETECTABLE |

**All 12 of 12 cells classify UNDETECTABLE — literally confirmed from the
raw data, not restated from NOTES.md.** `netd_disposition()`'s band is
`NETD_BAND_K=(0.020, 0.050)` K (`lab/thermo_sidecar.py`, traced to its
origin `experiments/034-.../design_geometry.py:422`); the largest of all 24
`dt_ss_full_K` values (37.13°/42.96° extremes, both configs) is
`5.4347e-05` K — **368× below the band's own lower edge**, not a near
miss. NOTES.md's "no cell approaching the `NETD_BAND_K` detectability
threshold" is true, though it under-states the margin by leaving the
368× figure unstated (a minor precision gap, not a defect: R4's own
"recompute, don't restate" spirit would prefer the number be given, but
nothing here is wrong).

NOTES.md's "Thermal sidecar" paragraph does what Red Team's mandatory fix 3
required: it states the headline classification in Result prose (not just
`results.json`), cites the code-enforced `NETD_ROW_KEYS` presence assert,
and explicitly frames the sentence as satisfying R21 rather than merely
R16. **R21's third-strike risk on this exact NETD channel is DISCHARGED for
this cycle** — the gap that fired at Iteration 76/exp-099 and Iteration
77/exp-100 did not recur a third time here. Four of the six angles
(the cpl20 crossings) are genuinely new to the R4 thermo sidecar and their
classifications are narrated, not silently persisted.

## 2. The one thing R21 compliance does NOT cover, and NOTES.md gets subtly wrong

R21 asks whether the headline *classification* is narrated — it is, and
correctly. But I independently checked whether the *quantitative claim*
built around that narration is itself accurate, and it is not, in one
specific respect (§3 below). This is a genuinely new finding: I checked it
by recomputing every ratio from `results.json`'s raw fields via script,
not by re-reading NOTES.md's own arithmetic.

## 3. Defect: NOTES.md conflates `sigma_abs`'s trend with `p_abs_w`/`dt_ss_full_K`'s trend — they are NOT "the same trend"

NOTES.md's Result, "Thermal sidecar" paragraph, states:

> `p_abs_w`/`dt_ss_full_K` track the same smooth, monotonic-with-θ trend as
> `sigma_abs` above (absorbed power rising 310→339 W-equivalent-cells as θ
> increases)

I recomputed both trends directly from `results.json` (C40_R4 config,
37.127246°→42.960901°, the full angular span):

| Quantity | value at 37.13° | value at 42.96° | relative growth |
|---|---|---|---|
| `partition_C40_R4_sigma_abs` | 310.928 | 338.789 | **+8.96%** |
| `sigma_ext_cells_c` | 604.939 | 659.086 | +8.95% |
| `p_abs_w_c` | 2.7866e-12 | 3.3080e-12 | **+18.71%** |
| `dt_ss_full_K_c` | 4.5780e-05 | 5.4347e-05 | **+18.71%** |

`sigma_abs` and `p_abs_w`/`dt_ss_full_K` are both monotonically rising with
θ, but their *relative* growth rates differ by a factor of **2.09×** —
this is not "the same trend," and the difference is not noise: it is an
exact, mechanically-derivable consequence of how `p_abs_w` is built.
`lab/thermo_sidecar.py::absorbed_power_established_ratio()` (the function
`cell_metrics_r4` calls) computes

```
width_m = sigma_ext_cells * dx_m
area_m2 = width_m ** 2          # "iso_xsec_sq" convention — SQUARE of the
                                 # extinction width, not width times a rod
                                 # length (the function's own docstring)
p_abs_w = i_incident_w_cm2 * (area_m2 * 1e4) * ratio_abs_ext_clamped
```

i.e. `p_abs_w ∝ sigma_ext_cells² × ratio_abs_ext_clamped`, while `sigma_abs
= sigma_ext_cells × ratio_abs_ext_raw` is only *linear* in `sigma_ext_cells`.
Since `ratio_abs_ext_raw` is itself nearly flat across this sweep
(0.5129–0.5145, a 0.3% range — this is Prediction 1's own confirmed
tight-clustering result), the entire growth of `p_abs_w` traces to
`sigma_ext_cells²`, which grows at roughly twice `sigma_abs`'s own percentage
rate. I verified this is not merely "roughly" true but *exact*: computing
`p_abs_w_c / (sigma_ext_cells_c² × ratio_abs_ext_raw_c)` at all 6 angles
gives the identical constant `1.4815e-17` to 5 significant figures at every
single point — the quadratic model is exact, not an approximation, on this
bench's own numbers.

**Consequences, scoped honestly:**
- This does **not** change the UNDETECTABLE classification anywhere — the
  368× margin (§1) absorbs a 2× discrepancy in growth-rate framing many
  times over. No re-scoring is warranted this cycle.
- It **is** a mislabeling: `sigma_abs` (310→339) is a cross-section
  quantity carrying units of length (`sigma_ext_cells`, "cells," times a
  ratio) — it is not power, and NOTES.md's own parenthetical
  "W-equivalent-cells" invents a unit that does not correspond to any
  quantity `thermo_sidecar.py` actually returns. Citing it under the
  heading "absorbed power" in the same sentence that discusses the real
  `p_abs_w`/`dt_ss_full_K` values is exactly the kind of loose
  cross-quantity citation this bench's own R9 (commensurability) rule
  exists to catch elsewhere — R9 itself doesn't technically fire here
  (no ratio is being compared), but the underlying discipline it protects
  — never treat two quantities from the same normalization family as
  interchangeable without checking — is what's being skipped.
- **Forward risk, not a live one today**: if a future cycle ever pushes
  this article to a more extreme angle range and tries to eyeball how close
  `dt_ss_full_K` is getting to `NETD_BAND_K` by extrapolating from
  `sigma_abs`'s own reported percentage growth, they will underestimate
  `p_abs_w`'s actual sensitivity to θ by roughly 2×, because of the squared
  `iso_xsec_sq` area convention baked into `absorbed_power_established_ratio`.
  At the current 368× margin this is academic; at a hypothetical future
  angle sweep that gets within, say, 10× of the band, it would not be.

**Recommended fix (does not require a re-run):** in NOTES.md's Result
section, replace "track the same smooth, monotonic-with-θ trend as
`sigma_abs` above" with something that does not claim rate-equivalence —
e.g., "`p_abs_w`/`dt_ss_full_K` also rise monotonically with θ (+18.7% over
the sweep, C40_R4), a steeper relative climb than `sigma_abs`'s own +9.0%
because `p_abs_w ∝ sigma_ext_cells²` (`iso_xsec_sq` convention,
`lab/thermo_sidecar.py`) while `sigma_abs ∝ sigma_ext_cells` at a nearly
flat `ratio_abs_ext_raw`" — and drop the invented "W-equivalent-cells" unit
entirely; `sigma_abs` should be cited in its own native units (a
normalized cross-section in cells) if cited at all in this paragraph, not
folded into a sentence about Watts.

## 4. The measured `sigma_abs` trend and falsified Prediction 3 — energy-detectability read, from this seat's charter only

**`sigma_abs` trend (310→339, confirmed monotonic in both configs):** no
detectability implication beyond what's in §3 above — the trend is real,
correctly measured, and its thermal consequence (`p_abs_w`/`dt_ss_full_K`)
is already computed and safely UNDETECTABLE with enormous margin. The only
issue is the narration imprecision already flagged.

**Falsified Prediction 3 (`sigma_scat_downstream` 4× over its predicted
ceiling, attributed to the extinction paradox/Babinet forward-diffraction
lobe):** **this has zero mechanical bearing on my charter's own
`p_abs_w`→`dt_ss_full_K`→NETD chain, and I want that stated explicitly
because NOTES.md does not rule it out and a future reader might wrongly
infer one.** I traced `cell_metrics_r4`'s call to
`absorbed_power_established_ratio(IRR_CENTRAL_W_CM2, sigma_ext_cells,
DX_M_R4, ratio_abs_ext_clamped)` — its only inputs are `sigma_ext_cells`
(=`sigma_ext`, box-A total extinction) and `ratio_abs_ext_clamped`
(=`sigma_abs/sigma_ext`). Neither `back_frac`, `fwd_frac`,
`sigma_scat_downstream`, nor `sigma_scat_sourceward` appears anywhere in
that call or anywhere upstream of it. The large forward-scattered residual
Prediction 3 measures is **elastically scattered power at the source
wavelength (600nm)** — coherent redirection of the incident field — not
absorbed energy converted to heat. It is a completely different physical
channel from the blackbody/graybody re-radiation my charter's sidecar
tracks (which would appear in the thermal-IR band commensurate with
`dt_ss_full_K`'s modest rise above `T_AMBIENT_K`, not at 600nm). A cell
could in principle have an enormous `sigma_scat_downstream` and an
unchanged `p_abs_w` — exactly the case here (both C40_R4 and G40_R4 show
this) — precisely because these two channels only share a common
upstream input (`sigma_ext`) and are otherwise independent. **No
constraint-3 re-radiation risk is raised by Prediction 3's falsification,
and none should be inferred from it in a future citation** — the "energy
that didn't get absorbed" is not energy that "went somewhere thermally
interesting"; it is energy that never entered my charter's channel at all.
This is worth stating explicitly precisely because NOTES.md's own
Idealizations section already distinguishes `sigma_scat_downstream` from a
witness-relevant irradiance measurement on other grounds (coherent
phase-blindness) but does not separately disclaim the *thermal* read of a
large scattered residual — a reader skimming "4× over predicted, biggest
finding of the cycle" next to "energy budget" language could conflate the
two without this note.

## 5. What I checked and found clean (charter-scoped, not re-litigating other seats' territory)

- `cell_metrics_r4`/`netd_row`/`pair_metrics_full` are confirmed, by reading
  `run.py`, called completely unmodified from exp-095/exp-100 — no new
  thermo-sidecar code was introduced this cycle beyond the (Prediction-3-
  irrelevant, per §4) `sigma_scat_partition()` function, consistent with
  NOTES.md's own "zero `lab/` diff" and "reused completely unmodified"
  claims.
- The `NETD_ROW_KEYS` coverage assert (`run.py` line ~253) is a real,
  executed gate (`HALT before results.json` on failure), not merely
  asserted in prose — matches Red Team's own read of mandatory fix 3's
  requirement ("implemented in code... not merely asserted").
- Expressibility-contract compliance (PANEL.md charter #4: "the sidecar is
  a post-run analytic calculation, not an FDTD output, and is labeled as
  such"): confirmed — `absorbed_power_established_ratio`'s own returned
  dict carries an explicit `idealization_note` ("bench-scale, not
  witness-scale... `iso_xsec_sq` area convention"), unchanged from prior
  cycles, and NOTES.md does not claim this sidecar as an FDTD-measured
  quantity anywhere.
- I did not find any second, independent thermo-charter defect beyond §3;
  the R13/R17/R20/R9(T9-disclaimer) fixes documented in NOTES.md's "Changes
  from Phase 1" are outside my own charter's lane (EM/QUANTUM/MATERIALS'
  territory respectively) and I did not re-audit them beyond confirming
  they do not touch the thermo sidecar's own inputs (they don't —
  `FLOOR_FRAC_SCAT`, `BOX_CROSS_CLEARANCE`, and the T9 disclaimer all
  attach to `sigma_scat`/`back_frac`/`ratio_abs_ext` reporting, never to
  `cell_metrics_r4`'s own call chain).

## 6. Bottom line

- **R21 third-strike risk: DISCHARGED.** All 12 cells' `netd_row()` outputs
  are both code-enforced-present and narrated in Result prose with the
  correct headline classification (UNDETECTABLE, unanimous), independently
  re-verified against raw `results.json`, not NOTES.md's restatement of it.
- **One real, previously-uncaught defect**, confined to my own charter:
  NOTES.md's Thermal-sidecar paragraph mislabels `sigma_abs` as "absorbed
  power" and claims it "tracks the same trend" as `p_abs_w`/`dt_ss_full_K`
  when the latter grows at 2.09× the former's relative rate — an exact,
  mechanically-derived consequence of `absorbed_power_established_ratio`'s
  quadratic (`iso_xsec_sq`) area convention, confirmed to 5 significant
  figures against every one of the 12 cells. Non-blocking (368× NETD
  margin absorbs it completely) but should be corrected in NOTES.md's
  prose per §3's suggested rewrite before this paragraph is cited by a
  future cycle.
- **Prediction 3's falsification carries no thermal-detectability
  implication** — explicitly confirmed by tracing `cell_metrics_r4`'s
  actual call chain, which never references `sigma_scat_downstream`/
  `back_frac`/`fwd_frac`. Worth a one-line disclaimer in NOTES.md so a
  future cycle does not conflate "large forward-scattered residual" with
  "re-radiation risk."
