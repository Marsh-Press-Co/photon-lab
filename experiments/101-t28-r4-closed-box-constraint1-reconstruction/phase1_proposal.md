# exp-101 Phase 1 Proposal — Panel Iteration 78

**Lead seat (rotation): VISION SCIENCE.** Tier-0 mandate only (Red Team's
Phase-5 final audit, exp-100, "Reconciled Iteration-78 queue," items 1-3).
Tiers 1-3 explicitly out of scope this cycle.

All facts below were independently recomputed from the repo, not taken from
the brief on faith: `lab/sections.py` read in full; `box_for_r4`/`ref_for_r4`/
`REF_HALF_H_R4`/`R4_R_OUT`/`R4_CONFIGS` traced through
`experiments/094-.../run.py` to `design_geometry.py`; `beam_behind_t28`/
`observer_record_t28`/`run_leg_b` read in full from `experiments/100-.../
run.py`, cross-checked against `phase5_redteam_audit.md`; `pool_rows()`
re-executed directly (`/tmp/.../verify_pool.py`, 75 rows, matches exp-100's
own stored count) to independently re-derive the angle re-selection and the
R4-family `ratio_abs_ext_raw` band cited below.

---

## 1. Mechanism/fix narrative (VISION SCIENCE seat)

Every downstream perceptual verdict this program renders on constraint 1 —
does the background stay lit behind the swept volume — is only as good as
the instrument measuring "how much light continues past the object." That
instrument came back UNINTERPRETABLE last cycle, diluted by a fixed line
window the shadow walks out of at oblique incidence. A witness's eye does
not sample a fixed 320-cell strip at one plane; it integrates light over an
extended field of view. A closed box is the correct idealization of that: it
cannot miss the shadow regardless of which way it walks, because Poynting's
theorem guarantees every watt the object diverts exits somewhere on the
box's own perimeter.

This matters to my seat specifically because constraint 1 is a
*precondition* beneath constraint 3 — my own hardest constraint, the one my
charter exists to police ("not a black silhouette at rest... only the swept
beam reveals it"). I cannot apply a Weber-contrast threshold to a beam-behind
reading that is measurement noise, and a plausible-looking-but-wrong
0.42-0.46 could get compared against `C_thr` as if it meant something.
Fixing the instrument is not new physics; it is the difference between "we
don't know if constraint 1 held" and "we do."

The three-way partition also feeds my own downstream question, even though I
score none of it this cycle: `sigma_abs` is THERMO's route to a
re-radiation risk against constraint 3; `sigma_scat` split by direction
tells me whether residual light exits toward the observer (glint, constraint
2 — already correctly measured) or laterally (a possible ambient cue at
rest, constraint 3's own concern, unscored here). I am not certifying any of
that today. I am certifying the instrument that will eventually feed it is
no longer broken.

---

## 2. Parameter table

### 2.1 Geometry — reused verbatim, zero new constants

Box and reference, as functions of `cfg["obj_x"]`/`cfg["obj_y"]`, `R4_R_OUT`
(=156) and a stated clearance — **identical to `box_for_r4`/`ref_for_r4`**
(`experiments/094-.../run.py:235-242`), called fresh in exp-101, imported not
modified:

```
BOX_A(cfg) = (obj_x - 180, obj_x + 180, obj_y - 180, obj_y + 180)   # clearance=BOX_CLEARANCE_A_R4=24, r=180
BOX_B(cfg) = (obj_x - 204, obj_x + 204, obj_y - 204, obj_y + 204)   # clearance=BOX_CLEARANCE_B_R4=48, r=204 (box-independence cross-check only)
ref(cfg)   = (obj_x, obj_y, 160)                                    # REF_HALF_H_R4=160
```

Concrete numbers (both `R4_CONFIGS` keys, `pad` differs by construction, `A`
identical=1504):

| cfg | obj_x | obj_y | BOX_A | BOX_B | ref |
|---|---|---|---|---|---|
| `C40_R4` (pad=0) | 340 | 1584 | (160,520,1404,1764) | (136,544,1380,1788) | (340,1584,160) |
| `G40_R4` (pad=80) | 420 | 1664 | (240,600,1484,1844) | (216,624,1460,1868) | (420,1664,160) |

Gate 1 (vacuum-footprint precondition on exactly these two boxes, both
configs) already passed in exp-094 — reused, not rerun.

### 2.2 The fix itself

Replace `beam_behind_t28`'s fixed-line-window read with a caller-side
recognition, **not a new formula**: `sc.widths()` already returns
`back_frac = max(p_back,0)/max(p_scat,1e-30)`, computed from the box's
low-`x` face. In T28/R4's own geometry (`src_x>obj_x>plane_x`, propagation
in `-x`, established by `widths_direction_corrected`'s own docstring and
independently re-derived from `_face_flux`'s `Sx` convention this cycle),
the low-`x` face is the **downstream** face — the direction a witness stands
in to see the background stay lit. `back_frac`'s own `max(p_back,0)` clamp
already reads exactly zero whenever the scattered field is a net downstream
*deficit* (a true shadow) rather than a net downstream *excess* (diffraction
refilling it) — precisely constraint 1's own distinction, already built into
gated code nobody has pointed at this question before.

```
w      = widths_direction_corrected(cap_article, cap_empty, BOX_A(cfg), ref(cfg))   # exp-091/exp-094's own wrapper, unmodified
sigma_scat_downstream  = w["back_frac"] * w["sigma_scat"]     # REPLACES beam_behind_t28 (forward-continuing)
sigma_scat_sourceward  = w["fwd_frac"]  * w["sigma_scat"]     # informal cross-check vs. observer_article_norm, not a replacement for it
xi_ext                 = |w["sigma_ext_cross"] - w["sigma_ext"]| / |w["sigma_ext"]|   # existing route-agreement check, gate ≤ XI_TOL=0.12
```

`lab/sections.py` diff: **zero.** `box_for_r4`/`ref_for_r4`/
`widths_direction_corrected`: **zero diff**, called fresh. All new code
lives in `experiments/101-.../run.py`.

### 2.3 Corrected `LEG_B_ANGLES` (6 angles, sorted, 6 decimals)

Independently re-executed `pool_rows()` (75 rows, 7 source directories,
matches exp-100's own stored `n_rows`) and re-sorted by `|delta_scene|`,
confirming the brief's claim to the digit:

| θ (deg) | delta_scene | family | source |
|---|---|---|---|
| 37.127246 | (cpl20 zero-crossing) | cpl20-native | exp-090 `j090["q8"]["crossings_deg"][0]` |
| 38.590230 | (cpl20 zero-crossing) | cpl20-native | exp-090, `[1]` |
| **39.200000** | **-3.149521e-3** | **R4** | **exp-095, `rank1.rank1a.per_theta["39.2"]` — pool-largest-magnitude, confirmed by independent re-run of `pool_rows()`** |
| 40.265420 | (cpl20 zero-crossing) | cpl20-native | exp-090, `[2]` |
| 41.460901 | (cpl20 zero-crossing) | cpl20-native | exp-090, `[3]` |
| **42.960901** | **+2.778079e-3** | **R4** | **exp-099, `item_1.combined_report["42.960901"]` — pool 2nd-largest-magnitude, confirmed** |

`LEG_B_ANGLES = sorted([37.127246, 38.590230, 39.200000, 40.265420,
41.460901, 42.960901])` — already ascending. Exp-100's own
`EXTREMA_ANGLES=[40.960901, 42.960901]` is confirmed WRONG for the first
entry: independently reproduced rank in my own full-pool sort:
40.960901 → 10th-largest (2.471869e-3), not top-2; 39.200000 is the single
largest value in the entire 75-row pool.

### 2.4 Call budget (R19-compliant)

Unchanged structure and count from exp-100's own Leg B — same captures
already needed for `cell_metrics_r4`/`observer_record_t28`, the closed-box
reconstruction is derived from them at **zero marginal FDTD cost**:

```
jobs = [(key, theta, article, dg.R4_STEPS, sigma_max)
        for theta in LEG_B_ANGLES for key in ("C40_R4","G40_R4")
        for article, sigma_max in [(False,None), (True, SIGMA_R4_CORRECTED)]]
assert len(LEG_B_ANGLES) == 6 and len(set(LEG_B_ANGLES)) == 6
assert len(jobs) == 24, f"R19 call-count assert: expected 24 jobs, got {len(jobs)}"
captures, wall = run_block_r4(jobs)
assert len(captures) == 24, f"R19: expected 24 captures, got {len(captures)}"
...
assert len(report) == 6, f"R19 row-count assert: 6 angle-rows, DISTINCT from the 24-call budget above"
```
6 angles x 2 configs x 2 conditions = 24 real `sim.run()` calls, producing 6
report rows (one per angle) — call-count and row-count asserted separately
and explicitly distinguished, per R19.

### 2.5 The three-way energy-partition table (per angle, per config)

Matches THERMODYNAMICS' own Phase-5 framing (absorbed / observer-direction
return / forward-continuing), expressed in `sc.widths()`'s own field names:

| Field | Meaning | Source (already-gated unless noted) |
|---|---|---|
| `sigma_abs` | **absorbed** — Joule dissipation inside BOX_A, normalized by `i_inc` | `widths_direction_corrected` (existing) |
| `p_abs_w` | absorbed, Watts (thermo sidecar, already filed by `cell_metrics_r4`) | reused, unchanged |
| `observer_article_norm` | **observer-direction return** — specular return toward the flashlight holder | `observer_record_t28`, UNCHANGED (constraint 2 already passed cleanly) |
| `sigma_scat_downstream` | **forward-continuing** — THE fix, replaces `beam_behind_t28` | NEW caller, zero lab/ diff |
| `sigma_scat` | total scattered outflow, all directions | `widths_direction_corrected` (existing) |
| `sigma_ext` (`=sigma_scat+sigma_abs`) | total extinction | existing |
| `sigma_ext_cross` | independent optical-theorem route, consistency check | existing |
| `xi_ext` | route-agreement, gate ≤0.12 (`XI_TOL`) | existing |
| `back_frac` / `fwd_frac` | fractional split of `sigma_scat` (downstream / sourceward) | existing, never before applied to T28/R4 |
| `sigma_scat_sourceward` | informal cross-check vs. `observer_article_norm` (not a replacement) | derived, new |
| `box_dev_scat_downstream` | BOX_A vs BOX_B agreement on the ONE genuinely new derived scalar (`sigma_scat_downstream`) | NEW due-diligence check, gated at ≤0.12 (R17: reusing the one already-justified numeric bound in this exact machinery family, `XI_TOL`, rather than inventing an illustrative round number) |

`sigma_abs + sigma_scat_downstream + sigma_scat_sourceward ≤ sigma_ext`
(strict, not an identity) — the shortfall is lateral/diffuse exit through
the box's `y0`/`y1` faces, disclosed in §5, not claimed as a clean 3-way sum.

---

## 3. T1 escape route

**N/A, explicitly.** This is pure instrument fidelity on an already-committed
LTI, passive, unmodified article (`graded_black_shell` + `pec_disk`, same
`sigma_max`, same geometry). No mechanism parameter (σ(I), σ(x,t), angular
selectivity, sub-threshold operation) is proposed, varied, or tested. T1's
central tension concerns which *mechanism class* can jointly satisfy
constraints 1-3; this cycle changes no mechanism, only how correctly
constraint 1 is *measured* on the mechanism already on file.

---

## 4. Falsifiable predicted outcomes

1. **`sigma_abs / sigma_ext` (BOX_A) ∈ [0.505, 0.520] at all 6 angles, both
   configs.** Grounded in my own independent recomputation of the R4-family
   pool this cycle (`ratio_abs_ext_raw_c`, n=35, min/max/mean =
   0.5121/0.5149/0.5135), itself within <1% of the T9 anchor (0.51,
   established exp-002 broadside, native geometry; first reconfirmed
   obliquely in exp-087, 0.5128-0.5138). **Falsified** if any angle/config
   falls outside this band, or if `sigma_abs<0` (existing non-negativity
   gate), or if `xi_ext>0.12` (existing route-agreement gate) at any cell.

2. **`back_frac > 0.5` at all 6 angles, both configs** — i.e., of whatever
   power the object scatters rather than absorbs, MORE than half exits
   downstream rather than sourceward. Motivated by the established
   extinction-paradox mechanism (T9/LOGBOOK: an optically-thick, near-
   zero-reflectance absorber's residual scattering is dominated by forward
   diffraction, not backscatter) but **genuinely untested at this bench's
   own near-field box distance** — T8's own open caveat is that this
   program's box sits deep in the shadow's Rayleigh range (z/z_R≈0.04-0.06)
   where the far-field diffraction relation need not yet hold. **Falsified**
   if `back_frac<0.5` at any angle — a real, surprising finding (most
   residual light returning sourceward from a graded, near-zero-reflectance
   shell) that would itself be worth a dedicated Phase-5 flag.

3. **`sigma_scat_downstream` stays a small fraction of `2*R4_R_OUT`=312
   cells (the geometric-optics forward-diffraction ceiling) — I predict
   `sigma_scat_downstream/312 < 0.15` at all 6 angles.** No prior
   measurement of this SPECIFIC derived quantity exists on this bench
   (first use); this is a genuinely new, falsifiable number, not a
   restatement. **Falsified** if any angle exceeds 0.15 — meaning a
   non-trivial forward-diffraction lobe is already refilling the shadow at
   this box radius, a real finding for constraint 1.

4. **`box_dev_scat_downstream ≤ 0.12` (reused `XI_TOL`) at all 6 angles** —
   the new derived quantity is at least as box-independent as the existing,
   already-gated channels it is built from. **Falsified** if it exceeds
   0.12 anywhere, flagging `back_frac*sigma_scat` as a more fragile
   quantity than `sigma_ext`/`sigma_abs` themselves — a real, reportable
   instrument-limitation finding, not swept under a wider tolerance
   post-hoc.

---

## 5. Idealizations

- **This is a cross-section/energy-partition measurement, not a
  downstream-intensity-ratio measurement.** `sigma_scat_downstream` answers
  "how much power, normalized by incident intensity and box geometry,
  exits the box downstream" — it does NOT answer "would a human witness
  standing behind the object see the background still lit," which requires
  converting this into an actual downstream irradiance at a witness-scale
  standoff and comparing it to ambient via a Weber contrast. That
  conversion is exactly the still-unbuilt T3 instrument (VISION's own
  standing Iteration-78 recommendation, Tier 2 of the reconciled queue) —
  out of scope here. My own charter's numeric thresholds (`C_thr_lab=0.005`,
  `C_thr_field=0.02`) are NOT invoked or scored this cycle; nothing in this
  proposal is compared against a perceptual threshold, so nothing new needs
  pinning beyond citing the existing, unchanged, already-established
  values for continuity.
- `sigma_abs + sigma_scat_downstream + sigma_scat_sourceward` is NOT an
  exact partition of `sigma_ext` — a lateral/diffuse remainder exits through
  the box's `y0`/`y1` faces and is not attributed to any of the three named
  channels. "Three-way" is a witness-relevant grouping, not a claimed
  algebraic identity.
- `back_frac`/`fwd_frac`'s downstream/sourceward relabeling is a caller-side
  reinterpretation of already-gated fields for THIS bench's own reversed
  propagation direction (`src_x>obj_x>plane_x`) — the same reinterpretation
  already established for `sigma_scat/abs/ext` (`widths_direction_corrected`)
  and for `observer_record_t28`'s own scalar swap. It has never before been
  applied to `back_frac`/`fwd_frac` specifically; §2.5's box-independence
  check is the corresponding new due-diligence, not a claim these fields
  were previously wrong.
- Near-field box convention only (`sections.py`'s own stated scope, not a
  far-field diffraction pattern) — T8's caveat about z/z_R applies to this
  measurement as much as to the original `beam_behind_t28`.
- Single wavelength (600nm), the two already-committed `R4_CONFIGS`
  (`C40_R4`/`G40_R4`) only — no new wavelength or article geometry.
- Does not address Tier 1's own open `delta_scene`-realizability question,
  the R3-vs-R4 split, or T3 — explicitly out of scope (Tier 0 only).

---

## 6. LOGBOOK.md RULED OUT registry check

Read the RULED OUT registry in full (lines 8-877) before drafting. This
proposal re-proposes nothing on that list — it is a zero-mechanism
instrument fix. Standing house-discipline rules bearing on it, each
verified verbatim at its cited line before citing:

- **R4** (line ~38): the pool-largest-magnitude claim and the R4-family
  `ratio_abs_ext_raw` band above were produced by actually re-executing
  `pool_rows()` (`/tmp/.../verify_pool.py`), never hand-typed from the
  brief.
- **R9**: the `ratio_abs_ext_raw` vs. T9's 0.51 anchor comparison is
  confirmed commensurable — both are `sigma_abs/sigma_ext` from the SAME
  `sc.widths()` normalization convention (incident intensity at a fixed
  central strip in the empty run), not two differently-normalized ratios.
- **R11**: not applicable — no period-search/widening machinery is touched
  this cycle.
- **R13/R14/R15**: `back_frac`'s own `max(p_back,0)`/`max(p_scat,1e-30)`
  denominator is already floor-gated by construction (clamped away from a
  literal zero); no new ratio denominator is introduced without an
  analogous floor.
- **R16/R21**: the new field (`sigma_scat_downstream`) and its box-
  independence check are proposed to be BOTH persisted to `results.json`
  AND stated inline in the eventual NOTES.md Result section (not left to
  Setup/Predictions only) — planned compliance, not yet fired (no run yet).
- **R17**: the new tolerance (`box_dev_scat_downstream ≤0.12`) reuses
  `XI_TOL`, the one already-established, already-justified numeric bound
  for this exact `sc.widths()` output family — not an invented round
  number.
- **R19**: call-count (24) vs. row-count (6) asserted separately and
  explicitly in §2.4, matching exp-100's own precedent.
- **R20**: every citation above (T9's 0.51, the `pool_rows()` re-derivation,
  the 4 cpl20 crossings, `box_for_r4`/`ref_for_r4`'s exact code) was
  independently reproduced from source this cycle, not restated from the
  brief — zero R4/R20-class defects intended to survive into Phase 3.

No item above, or elsewhere in the T28 thread narrative (lines 2572-6912),
rules out a closed-box reconstruction of `beam_behind_t28` — to the
contrary, it is this cycle's own commissioned Tier-0 mandate, and PHOTONICS'
and EM's Phase-5 preference for exactly this fix (over a re-centered line
window) is the basis for it being selected here.
