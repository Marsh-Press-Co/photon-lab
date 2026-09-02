# Phase-5 Review — THERMODYNAMICS seat, Panel Iteration 79 (exp-102)

Fresh sub-agent for this Phase-5 pass (I filed `phase2_critique_thermodynamics.md`
this cycle, which flagged the R21 third-strike risk as the packet's top
priority). Nothing below is taken on `NOTES.md`'s word — every load-bearing
claim is re-derived from `run.py`'s actual source or `results.json`'s raw
fields.

## 0. Verdict

**CONFIRM-WITH-GAPS** on the cycle's Combined Verdict candidate (Predictions
1/3/4/5 CONFIRMED, Prediction 2 CONFIRMED-after-a-disclosed-sign-correction,
Gate B a genuine, honestly-diagnosed FAIL). My own charter's top-priority
concern from Phase 2 — the R21 third-strike risk — is cleanly discharged
(§1). I independently found one new, non-load-bearing numeric citation
defect in Result prose (§2) and one disclosure gap worth naming for the
record (§3), neither of which changes any scored verdict.

## 1. R21 third-strike risk — verified by reading `run.py` myself, not `NOTES.md`'s claim

Grepped `run.py` directly for `netd_row`, `cell_metrics_r4`, and
`pair_metrics_full`: all three hits are in **comments/docstring text**
(lines 9-10, 107-108) explaining why they are *not* imported — zero
executable `import`/call sites. Confirmed the file's only cross-experiment
load is one `_load()` call (line 113), targeting
`experiments/069-.../design_geometry.py` — a pure-constants module
(`R4_CONFIGS`, `PEC_R_R4`, `R4_R_OUT`, `SIGMA_R4_CORRECTED`, `R4_TAPER`,
`R4_STEPS`, `R4_CPL`, `COURANT_FRAC`, `BOX_CLEARANCE_A_R4`, `REF_HALF_H_R4`)
that itself contains no `netd`/`thermo`/`cell_metrics`/`pair_metrics`
symbols (grepped that file too). `run.py` never loads exp-094's or
exp-101's `run.py` module chain — the actual pipeline Red Team's own
Phase-2 audit confirmed (by reading `experiments/101-.../run.py` line-by-line:
`netd_row = exp095.netd_row` at line 78, `cell_metrics_r4(...)` called
unconditionally in the sweep loop at line 222, `pair_metrics_full`/
`netd_row(pm)` asserted present at lines 251-254) would have pulled in
unconditionally. `run_output.txt` also contains zero occurrences of
`netd`/`thermo`/`cell_metrics_r4`/`pair_metrics_full`.

**This closes my own Phase-2 top-priority risk cleanly, at the code level,
not merely by NOTES.md's assertion.** `NOTES.md`'s Setup/Result claim ("does
NOT import `netd_row`/`cell_metrics_r4`/`pair_metrics_full`... no thermal
byproduct can be silently persisted") is independently reproduced exactly.
Live Thread T5 (the thermo ledger) correctly stays untouched and open —
this cycle introduces no new absorbed-power regime, so no `netd_row()`
disposition is owed, and none is claimed.

## 2. Defect found: the on-axis `κ(θ)` region range stated in Result does not match its own `results.json`

`NOTES.md` Result states: "on-axis coherent intensity ratio `κ(θ)`
(region-averaged) ranges `3.68×10⁻³`–`7.29×10⁻³` across all 12
(angle,config) cells." I pulled all 12 `kappa_region` values from
`results.json['primary_rows']` directly:

| Cell | `kappa_region` |
|---|---|
| C40_R4@41.460901 | **0.0034800** ← true minimum |
| C40_R4@38.590230 | 0.0036815 |
| G40_R4@39.200000 | 0.0038228 |
| C40_R4@39.200000 | 0.0038510 |
| … (8 more, ascending) | … |
| C40_R4@42.960901 | **0.0072898** ← matches stated max |

The true minimum is `3.48×10⁻³` (`C40_R4@41.460901°`), not `3.68×10⁻³`.
`3.68×10⁻³` is real — it is the pool's *second*-smallest value
(`C40_R4@38.590230°`) — but it is not the minimum, and the cell it actually
belongs to is not the cell the stated range implies. The maximum
(`7.29×10⁻³`) is correct and reproduces exactly. **This is a genuine,
independently-verified numeric restatement defect in Result prose, the
same shape as this program's R20 lineage** (a stated range that is
actually a subset of the true pool, mirroring exp-101's own
`observer_article_norm` finding one cycle ago) — though on a different
channel (the primary κ instrument, not a thermal or normalization one)
and non-load-bearing: `3.48×10⁻³` is still comfortably inside `[0, 0.10]`,
so Prediction 1's CONFIRMED verdict is unaffected either way. Flagging for
Red Team's own tally since citation-hygiene density across a cycle, not
any single instance's severity, is what R20 was built to track.

## 3. Disclosure gap, not a defect: `I0_corrected`/`i_abs` remain dimensionless — the witness-wattage pin still gates any thermal use

`i_abs` (the absolute-intensity fraction, precondition (a) of the
proposal) is computed and persisted for all 12 cells
(`results.json['primary_rows'][...]['i_abs']`, range `3.49×10⁻³`–
`7.42×10⁻³` — independently computed by me, never stated in Result/Learned
prose at all). It is not itself a citation defect: `i_abs` was never
promised as a scored Prediction, and nothing in `NOTES.md` mis-describes
it. I name it because its *shape* — a persisted, un-narrated field — is
structurally the same pattern R21 exists to catch, even though R21's own
text scopes to the NETD/thermal-sidecar channel specifically and does not
literally fire here (this is an EM field-intensity fraction, not a
thermal quantity, and not on my charter's channel). Worth stating plainly
for the record, from my seat: **`i_abs`/`I0_corrected` are still
dimensionless ratios against the local FDTD source amplitude, not a
physical W/m² irradiance** — the witness-wattage pin (T5's own long-open
precondition, named at Tier 1 of exp-100's queue) still gates any future
citation that would treat `i_abs` as a real irradiance feeding a thermal
or detectability claim. This cycle correctly never makes that leap; a
future cycle citing `i_abs` for anything beyond a dimensionless
same-instrument comparison should re-state that gate explicitly.

Separately, the off-axis companion point reads mildly **brighter** than
the empty scene (`κ_off` up to 1.077, i.e. +7.7%) at several angles — from
my own charter, this is diffractive field redistribution (constructive
interference at the shadow edge), not a violation of, or contribution to,
any energy budget: total extinguished power is already fully accounted by
this article's own long-established `sigma_ext`/`sigma_abs` partition
(exp-094-101), and a coherent point/region intensity ratio cannot itself
add or remove energy from that ledger. No re-radiation or energy-bookkeeping
concern is raised by this reading, and none should be inferred from it in
a future citation — worth stating explicitly since "brighter than empty
scene" is the kind of phrase a future skim could misread as anomalous.

## 4. Independent recomputation — additional spot checks (all reproduced exactly)

- **Gate C max deviation (corrected formula):** recomputed
  `|I0_corrected·u_x − i_inc|/I0_corrected` from raw `mean_sx`/`mean_sy`/
  `i_inc`/`u_x` fields at `G40_R4@42.960901°` → `0.0091979...` = **0.92%**,
  exactly matching the stated max. Recomputed the *original erroneous*
  (sign-blind `cosθ`) formula at `G40_R4@37.127246°` → **159.78%**, exactly
  matching the stated max for the disclosed-but-superseded formula.
- **Gate D perturbation deviations:** `rel_dev_region` = 0.489511 (C40_R4)
  and 0.082417 (G40_R4) → **48.95%** / **8.24%**, both exactly matching
  Result prose.
- **Point-vs-region ratio band:** recomputed all 12 `kappa_point/
  kappa_region` ratios → range `1.230`–`1.559`, matching the stated
  "1.23–1.56×" exactly.
- **Off-axis / Δφ ranges:** recomputed → `κ_off∈[1.0406, 1.0766]` and
  `Δφ∈[0.209, 0.587]` rad, matching stated "1.041–1.077" / "+0.21–+0.59 rad"
  exactly.
- Minor, non-substantive: `wall_r4_s`(3180.66) + `wall_gate_b_s`(31.76) =
  3212.4s, vs. `total_wall_s`=3278.5s in `results.json` — a ~66s gap
  (setup/post-processing overhead, not a missing FDTD call; `n_fdtd_calls`
  and `n_fdtd_calls_actual_this_run` both correctly read 26). Not charted
  against any prediction; noted only for completeness.

## 5. Bottom line

- **R21 third-strike risk: DISCHARGED, verified from `run.py` source, not
  from NOTES.md's restatement.** No `netd_row`/`cell_metrics_r4`/
  `pair_metrics_full` import or call exists anywhere in the final `run.py`;
  the only cross-experiment load is a pure-constants file with no thermal
  symbols. Checkpoint criterion 4's R21 clause does not approach firing
  this cycle on my own channel.
- **One new, non-load-bearing Result-prose defect found**: the stated
  on-axis `κ(θ)` region range floor (`3.68×10⁻³`) is not the pool's true
  minimum (`3.48×10⁻³`, a different cell) — R20-lineage shape, does not
  change Prediction 1's verdict.
- **One disclosure recommendation, not a defect**: `i_abs`/`I0_corrected`
  remain dimensionless (no witness-wattage pin applied), and the off-axis
  brightening is diffractive redistribution, not an energy-bookkeeping
  anomaly — both worth a one-line explicit disclaimer if `i_abs` is ever
  cited by a future cycle.
- **Verdict: CONFIRM-WITH-GAPS.**

## 6. Ranked top-3 candidate directions for Iteration 80 (my seat's own priority)

1. **Pin the witness-scale absolute source wattage** (T5's own long-open
   precondition). This cycle is the first to produce a genuine
   phase-resolved, dimensionless absolute-intensity fraction (`i_abs(θ)`)
   at a physically meaningful downstream point — the natural next input to
   a real absorbed-irradiance/thermal-budget conversion, but only once a
   real Watts-scale is pinned to the source amplitude. Without it,
   `i_abs` cannot be cited as anything beyond a same-instrument ratio (§3).
2. **A properly-scoped Gate B**, matched to `beam_behind`'s own established
   spatial footprint rather than a rescaled point/region sample (NOTES.md's
   own Next item 1, Learned item 2) — needed before this instrument's
   on-axis reading can be cross-validated against the bench's oldest
   trusted figure; also the natural companion to item 1, since a correctly
   validated point/region reading is what any future thermal conversion
   would build on.
3. **The candidate standing rule from Learned item 4** (a vector-valued
   self-consistency identity's SIGN must be independently re-derived from
   the same convention governing that vector elsewhere in the same
   document, not merely its magnitude) — a real, generalizable process gap
   this cycle surfaced live (three independent reviewers checked magnitude
   and averaging order, none checked sign), worth Red Team's formal
   adoption call; cheap, and would have caught this cycle's own Gate-C
   defect before Phase 4 rather than during it.
