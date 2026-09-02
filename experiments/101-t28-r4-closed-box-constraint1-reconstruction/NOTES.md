# exp-101 — Closed-Box (4-Face Poynting) Reconstruction of `beam_behind_t28`

**Panel Iteration 78. Lead seat (rotation): VISION SCIENCE. Director: Clyde
(photonlab-shift, cloud panel shift).** Tier-0 mandate only (Red Team's
Phase-5 final audit, exp-100, "Reconciled Iteration-78 queue," items 1–3).
Tiers 1–3 explicitly out of scope this cycle.

Full record: `phase1_proposal.md` (VISION SCIENCE), `phase2_critique_
{photonics,materials,em,thermodynamics,quantum}.md` (five blind critiques,
all support-with-changes), `phase2_redteam_audit.md` (7 numbered attacks,
6 mandatory fixes, PROCEED-WITH-MANDATORY-FIXES, 0 overridden).

## Hypothesis

Iteration 77 (exp-100) found `beam_behind_t28` uninterpretable — a fixed
line window at the downstream plane mostly misses the object's own shadow
at oblique incidence, since the shadow walks 125.7–154.6 cells laterally
while the window's half-width is only 160 cells. `lab/sections.py::widths()`
(trust-suite stage 8, already gated) has no lateral-centering assumption at
all: it sums flux over the FULL four-face box perimeter, so it cannot miss
the shadow regardless of which way it walks. Hypothesis: replacing
`beam_behind_t28` with a closed-box reconstruction, on the already-gated
`box_for_r4`/`ref_for_r4`/`widths_direction_corrected` machinery, produces
an interpretable constraint-1 reading where the line-window instrument
failed — without touching constraint 2 (`observer_record_t28`, already
passed cleanly) or requiring any new mechanism, material, or `lab/` change.

## Setup

- **Article**: unchanged from exp-100 — `pec_disk`(r=`PEC_R_R4`=60) +
  `graded_black_shell`(r_in=60, r_out=`R4_R_OUT`=156, `sigma_max=
  SIGMA_R4_CORRECTED`=0.25), `R4_CONFIGS["C40_R4"]`/`["G40_R4"]`, 600nm,
  oblique plane-line source (`profile="plane"`, `edge=R4_TAPER`=80).
- **Angles (corrected)**: `sorted([37.127246, 38.590230, 39.200000,
  40.265420, 41.460901, 42.960901])` — the four established cpl=20
  zero-crossings, plus the TRUE two pool-wide-largest-magnitude
  `|delta_scene(θ)|` points (re-verified this cycle by re-executing
  `pool_rows()` against the live 75-row pool: 39.200000°, exp-095, R4,
  `-3.149521e-3`, the single largest value in the entire pool; 42.960901°,
  exp-099, R4, `+2.778079e-3`, second-largest) — replacing exp-100's own
  `40.960901°`, which only searched exp-099's own local subset and is
  actually the pool's 10th-largest (`2.471869e-3`).
- **The fix**: `sigma_scat_partition()` (this file) calls
  `widths_direction_corrected(cap_article, cap_empty, box, ref)` on
  `BOX_A` (`box_for_r4(cfg, BOX_CLEARANCE_A_R4=24)`, unchanged from
  exp-094/exp-100) and computes `sigma_scat_downstream = back_frac *
  sigma_scat`, `sigma_scat_sourceward = fwd_frac * sigma_scat` — the
  low-x face convention independently re-derived this cycle from
  `_face_flux`'s raw `Sx = -0.5·Re{Ez·conj(Hy)}` density (Phase-2 EM
  critique + Red Team audit attack #1), matching this bench's own
  established `plane_x_behind()` convention (low-x = downstream, for
  `src_x>obj_x>plane_x`) — **not** by analogy to `widths_direction_
  corrected` (Phase-1's original, FALSE citation: that function only
  rescales `sigma_scat/abs/ext/ext_cross` by `sign(i_inc)` and never
  touches `back_frac`/`fwd_frac` at all — corrected per mandatory fix 2).
- **`cell_metrics_r4`/`pair_metrics_full`/`netd_row`/`observer_record_t28`**
  are reused completely unmodified — constraint 2 and the thermo/
  `delta_scene`/`frac_contrast` channel are not broken and are out of scope.
- **`lab/` diff: zero.** All new code lives in this experiment's `run.py`.
- **Call budget**: 24 real `sim.run()` calls (6 angles × 2 configs × 2
  conditions), identical to exp-100's own Leg B — call-count (24) and
  row-count (6) asserted separately and explicitly (R19).

## Changes from Phase 1 (Red Team's Phase-2 audit, 6 mandatory fixes, all
## adopted, 0 overridden — Director's synthesis)

1. **[R13 compliance] Real amplitude floor on `sigma_scat`, replacing the
   proposal's over-claimed `1e-30` anti-division-by-zero epsilon.**
   `FLOOR_FRAC_SCAT=0.10` (exp-088's own R13-founding house-style constant,
   reused for the SAME kind of amplitude-normalized floor, applied to a
   quantity — `sigma_scat` on the R4 family via `back_frac`/`fwd_frac` —
   that has no larger established cross-cycle dataset yet, so the floor is
   drawn from THIS cycle's own 12-cell RMS, disclosed as an idealization,
   not an externally-anchored bound). A cell whose `|sigma_scat|` fails
   this floor is reported `UNRESOLVED-BY-CONSTRUCTION` and excluded from
   Predictions 2–4's scoring, per R13's own prescribed remedy — never
   silently scored. *(Red Team attacks #1, #2; EM's critique.)*
2. **[citation correction] `widths_direction_corrected` dropped as the
   stated warrant** for the `back_frac`/`fwd_frac` downstream/sourceward
   reading; replaced with the actual warrant (`_face_flux`'s raw Sx-face
   correspondence + `plane_x_behind`'s own low-x="downstream" convention).
   *(Red Team attack #1; EM's critique.)*
3. **[R21 compliance] Explicit, code-enforced commitment**: all 12 fresh
   `netd_row()`-shaped outputs (`p_abs_w`, `dt_ss_full_K`,
   `netd_classification`, 6 angles × 2 configs) are persisted (unchanged
   `netd_row()`/`NETD_ROW_KEYS` assert, matching exp-100's own precedent)
   **and** narrated below in Result — see "Thermal sidecar" paragraph.
   This is R21's own third-strike channel (Iteration 76/exp-099, Iteration
   77/exp-100 are the first two founding instances); a third silent
   occurrence fires Checkpoint criterion 4 automatically. *(Red Team
   attack #6; THERMODYNAMICS' critique — the single highest-priority fix
   in the packet.)*
4. **[R17 compliance] Per-config `BOX_CROSS` clearance for the NEW
   box-independence due-diligence check** (`sigma_scat_downstream` only —
   the pre-existing `cell_metrics_r4` `BOX_A`/`BOX_B` pair, its own
   `xi_ext`/`box_dev`/thermo channel, is UNCHANGED and out of scope).
   `C40_R4`'s domain (`nx=720`, `pad=0`) cannot support the uniform
   `BOX_CLEARANCE_B_R4=48` clearance exp-100's own thermo channel already
   uses without margin dropping to 56 cells — below exp-003's own
   established ≥60-cell threshold, and this bench's `ABSORB=80` (2× exp-
   003's 40) means 60 cells is a floor, not a target. Fix: `BOX_CROSS_
   CLEARANCE={"C40_R4":14, "G40_R4":48}` → margins `{90, 136}` cells,
   verified directly from the real `Sim` geometry (`_verify_box_margins()`,
   asserted ≥90 before any FDTD call) rather than re-derived by hand.
   **Disclosed asymmetry (Idealization)**: for `C40_R4` only, `BOX_CROSS`
   (r=170) is now SMALLER than `BOX_A` (r=180) — a weaker, ~6%-size-
   difference independence check than `G40_R4`'s own (~13%), because
   `C40_R4`'s fixed domain (no new FDTD this cycle) does not admit a
   wider-spread pair while clearing the 90-cell margin. *(Red Team attack
   #5; QUANTUM's critique.)*
5. **[R20 risk discharged] The R3-vs-R4 "coupling asymmetry" is not carried
   forward as settled.** Red Team's own Phase-2 audit found `exp-100`'s
   `pool_rows()` pool contains undisclosed duplicate (citation-republished)
   rows: 12 of R3's 33 rows and 6 of R4's 35 rows are byte-identical
   duplicates. Deduplicating flips R3's "significant coupling" (`r=0.486,
   p=0.0042`) to **non-significant** (`r=0.360, p=0.107`) — this does not
   change either angle this cycle selects (neither `39.200000°` nor
   `42.960901°` is a duplicated row), but PHOTONICS' own comparator ("a
   real, significant coupling at R3") must not be cited as settled without
   this caveat. Stated here, not carried into Result as fact. *(Red Team
   attack #3, this seat's own finding; extends PHOTONICS' critique.)*
6. **[R9/T9 disclaimer restored] T9's own disclaimer travels with the 0.51
   anchor everywhere it is cited below**: `sigma_abs/sigma_ext ≈ 0.51`
   **exceeds the idealized geometric-optics ceiling (≤0.5, a Babinet/
   shadow-formation bound for any perfectly-black object, independent of
   interior structure) and is NOT an asymptotic material constant** —
   attributed (T8/T9, LOGBOOK.md line ~1161) to this bench's box sitting
   deep in the near/Rayleigh zone, not to real material absorptivity.
   *(Red Team attack #7; MATERIALS' critique.)*

## Predictions (committed to git BEFORE Phase 4 runs any FDTD call — house
## discipline, non-negotiable)

All four bands below apply only to cells that clear the Fix-1 amplitude
floor (`floor_pass=True`); a cell failing it is reported
`UNRESOLVED-BY-CONSTRUCTION` and is not scored against any band.

1. **`sigma_abs/sigma_ext` (BOX_A) ∈ [0.505, 0.520] at all 6 angles, both
   configs** — grounded in this cycle's own re-derived R4-pool band
   (`ratio_abs_ext_raw_c`, n=35 as-pooled, min/max/mean = 0.5121/0.5149/
   0.5135). **T9's disclaimer applies in full** (change 6, above): if
   confirmed, this reads as a near-field box-geometry effect (the box
   sits at z/z_R≈0.04–0.06, T8), NOT as evidence the article itself
   absorbs more than half of extinguished power in any asymptotic sense.
   Falsified if any resolved angle/config falls outside this band, or if
   `sigma_abs<0` (existing gate), or if `xi_ext>0.12` (existing gate).
2. **`back_frac > 0.5` at all 6 angles, both configs** among resolved
   cells — i.e., more than half of whatever the object scatters (rather
   than absorbs) exits downstream rather than sourceward. Motivated by the
   established extinction-paradox mechanism (T9) but genuinely untested at
   this bench's own near-field box distance (T8's open caveat). Falsified
   if `back_frac<0.5` at any resolved angle/config.
3. **`sigma_scat_downstream / (2·R4_R_OUT=312 cells) < 0.15`** at all
   resolved angles/configs — first use of this specific derived quantity
   on this bench. **Per PHOTONICS' fix (change 5's companion): the two
   pool-extremal angles (39.200000°, 42.960901°) carry NO established
   correlation between `delta_scene` and the article's own absorbed-power
   fraction for the R4 family (`r=0.1103, p=0.5249`, exp-100's own Tier-1
   test, confirmed this cycle) — a result at those two angles is reported
   as instrument-behavior data on the fixed R4 article, not as evidence of
   angle-dependent optical engagement, pending Tier 1's own future
   resolution of the R3-vs-R4 split.** Falsified if any resolved
   angle/config exceeds 0.15.
4. **`box_dev_scat_downstream ≤ 0.12` (`XI_TOL`)** at all 6 angles, both
   configs, using the per-config `BOX_CROSS` pair (change 4) — the new
   derived quantity is at least as box-independent as the channels it is
   built from. Falsified if it exceeds 0.12 anywhere; a `C40_R4` failure is
   read against the disclosed weaker-independence-check caveat (change 4),
   not automatically as a `back_frac`-fragility finding.

## T1 escape route

**N/A.** Pure instrument fidelity on an already-committed LTI, passive,
unmodified article. No mechanism parameter is proposed, varied, or tested.

## Idealizations

- This is a cross-section/energy-partition measurement, not a
  downstream-intensity-ratio measurement — it does not answer "would a
  human witness see the background still lit" (that conversion is
  constraint 1's own still-missing instrument, per PANEL.md's metric
  table — out of scope here). No perceptual threshold (`C_thr_lab`/
  `C_thr_field`) is invoked or scored this cycle. **Correction (Phase-5
  VISION/Red Team finding)**: this document's first draft mislabeled this
  future instrument "T3" (both here and in Next item 1) — T3 is
  specifically LOGBOOK's temporal-contrast/switching-transient instrument
  (constraint 3/4 joint), an unrelated construction; the reference is
  dropped.
- `sigma_abs + sigma_scat_downstream + sigma_scat_sourceward` is NOT an
  exact partition of `sigma_ext` — the remainder exits through the box's
  `y0`/`y1` faces. **Quantified (Phase-5 EM finding, first draft said only
  "a lateral/diffuse remainder")**: this lateral share is substantial and
  itself grows with angle — 34.6% of `sigma_scat` at θ=37.13° to 46.7% at
  θ=42.96° (exceeding `back_frac` itself at the largest angle) — very
  likely the same fixed-lab-frame-box effect as `back_frac`'s own decline
  (Result item 2, above), not a small correction term.
- The Fix-1 `sigma_scat` amplitude floor is self-referential (drawn from
  this cycle's own 12-cell RMS, not a larger established dataset) — this
  bench's first use of `back_frac`/`fwd_frac` on the R4 family.
- The Fix-4 `BOX_CROSS` pair is asymmetric across configs: `C40_R4`'s own
  independence check (r=170 vs r=180, ~6% size difference) is weaker than
  `G40_R4`'s (r=204 vs r=180, ~13%) — `C40_R4`'s fixed domain (no new FDTD
  this cycle) does not admit a wider-spread pair while clearing the
  90-cell absorb-boundary margin.
- Near-field box convention only (T8's z/z_R caveat applies as much to
  this measurement as to the original `beam_behind_t28`).
- Single wavelength (600nm), the two already-committed `R4_CONFIGS` only.
- Does not address Tier 1 (`delta_scene`-realizability, the R3-vs-R4
  split), Tier 2 (T3), or Tier 3 (standing deferred items) — explicitly
  out of scope this cycle.
- The R3-vs-R4 pool-duplication finding (change 5) is disclosed as a
  caveat on citing exp-100's own Tier-1 result, not re-litigated or
  re-scored here — that is Tier 1's own future work.
- **[Phase-5 EM finding, flagged for future reuse, not required this
  cycle]** The Fix-1 `sigma_scat` amplitude floor (`scat_floor_pass`) is
  wired only into `partition_forward_continuing` (Prediction 3);
  `partition_absorbed`, the raw `sigma_scat_downstream`/
  `sigma_scat_sourceward` fields feeding `back_frac`/Prediction 2, and
  `box_dev_scat_downstream`/Prediction 4 are all computed unconditionally.
  Moot this run (0/12 cells failed the floor), but a latent gap if this
  exact `run_leg_b_fixed()` pattern is reused on data where a cell
  genuinely fails the floor.

## Result (self-scored, run.py's own committed output, `results.json`)

**24 real FDTD calls, wall_s=1961.6 (32.7 min), trust suite green before and
after (41/41, zero `lab/` diff), `xi_pass=True`, `nonneg_pass=True`, R18
validation gate `True` (all 12 empty-scene observer self-ratios <0.02).
Registration preflight clean. Box-margin gates (Fix 4) all passed as
pre-registered before any FDTD call ran. All 12 (θ,config) cells cleared
the Fix-1 `sigma_scat` amplitude floor — `n_unresolved_by_construction=0`.**

1. **`sigma_abs/sigma_ext` ∈ [0.505, 0.520] — CONFIRMED at all 12 cells**,
   range `[0.5129, 0.5145]`, comfortably inside the band and tightly
   clustered (spread 0.0016). **T9's disclaimer applies as pre-registered
   (change 6)**: this exceeds the Babinet/shadow-formation ≤0.5 ceiling and
   is read as a near-field box-geometry effect (z/z_R≈0.04–0.06, T8), not
   an asymptotic material-absorptivity constant. **Extension (MATERIALS'
   Phase-5 finding)**: the same disclaimer applies more sharply to the
   RAW `sigma_abs` values themselves — `Q_abs=sigma_abs/(2·R4_R_OUT=312)`
   exceeds the elementary `Q_abs≤1` geometric-optics ceiling (any passive
   object's true absorption efficiency, a sharper bound than the ratio's
   Babinet ceiling since it needs no forward-diffraction companion lobe)
   at 10 of 12 cells, up to 8.6% over unity at θ=42.96° — the same
   near-field box-geometry effect, not evidence of super-unity absorption
   in any real coating.
2. **`back_frac > 0.5` — CONFIRMED at all 12 cells**, with a real, clean,
   monotonic angular trend the pre-registered band did not predict:
   `0.6536→0.5324` (C40_R4) and `0.6529→0.5340` (G40_R4) as θ rises
   37.13°→42.96°, the two configs agreeing to within 0.0007–0.0016 across
   the sweep (**correction, Phase-5 Red Team final audit**: NOT "tracking
   to 3 decimal places at every angle" as first drafted here — independent
   digit-by-digit recomputation shows the third decimal actually matches
   at only 1 of 6 angles; the agreement is real and close, just not that
   close). **Likely shares one root cause with Prediction 3's own
   falsification below, not two separate findings (PHOTONICS' Phase-5
   finding)**: the lateral (y-face) share of `sigma_scat` grows from 34.6%
   to 46.7% across the same sweep, tracking `tan θ`'s own 23% growth — a
   fixed lab-frame box measuring an increasingly oblique forward lobe is
   the best-supported explanation (not proven with certainty; see Next).
   Confirmed-with-margin, but the flat ">0.5" framing under-describes a
   genuinely angle-dependent quantity — flagged for Phase 5, not rescored
   here (this cycle's own predictions did not pre-register a slope).
3. **`sigma_scat_downstream/(2·R4_R_OUT)` < 0.15 — FALSIFIED at all 12
   cells, by a wide margin.** Measured range `[0.5457, 0.6159]` — roughly
   4× the predicted ceiling, not a near-miss. **Self-diagnosed cause, same
   shift**: the predicted 0.15 ceiling assumed a "geometric-optics
   forward-diffraction ceiling" small relative to the object's own
   diameter — but this ignores the SAME extinction-paradox physics T9's
   own disclaimer (change 6, above) already establishes on this exact
   bench: an optically large absorbing disk's extinction efficiency
   approaches a large fraction of the theoretical PEC ceiling in the
   geometric-optics limit specifically *because* it must radiate a
   forward-diffracted wave of cross-section comparable to its own
   geometric width — the same forward lobe that destructively interferes
   with the incident wave to CREATE the geometric shadow in the first
   place (Babinet's principle), a far-field asymptotic statement subject
   to the SAME T8 near-field caveat (box at z/z_R≈0.04–0.06) already
   invoked for Prediction 2. **Correction (Phase-5 QUANTUM OPTICS/Red Team
   finding)**: this document's first draft cited the raw, uncorrected
   `sigma_ext/(2·R4_R_OUT)≈1.94–2.11` as "approaching `Q_ext→2`" — this
   number is itself an artifact. `sc.widths()`'s `i_inc` measures only the
   x-projected component of the incident Poynting flux
   (`lab/fdtd2d.py::add_line_source`'s own documented oblique-launch
   direction `(−cosθ,+sinθ)`), inflating every ABSOLUTE (non-ratio)
   `sc.widths()` output by `1/cosθ` at oblique incidence — an R9
   commensurability gap, not previously surfaced on this bench because
   every prior use of these outputs (T9's anchor, exp-087's oblique
   reconfirmation, this cycle's own Predictions 1/2/4) was a RATIO of two
   such quantities, which cancels the factor exactly. Applying the `cosθ`
   correction collapses the raw values to **1.539–1.556**, matching this
   bench's own already-locked normal-incidence anchor
   (`lab/qext_theory.py`/exp-059, `Q_ext=1.5385`) to ~1% — confirming the
   mechanism, not merely correcting a display digit. The qualitative
   Babinet/extinction-paradox argument stands; only the "`→2`" magnitude
   was wrong. **This does not change the falsification**: the same
   correction applied to `sigma_scat_downstream` itself gives
   0.399–0.491 — still 2.7×–3.3× over the 0.15 ceiling. A large
   `sigma_scat_downstream` is therefore the mathematically expected
   companion of a real shadow, not evidence against one — this prediction
   band was wrong about the physics, not merely mis-calibrated, and the
   falsification is the more informative outcome: it heads off a future
   cycle mis-reading a large downstream-scattered cross-section as "the
   beam is not terminated" without first accounting for coherent
   destructive interference. **This is a POWER/cross-section quantity
   (incoherent bookkeeping across scattered-field flux), not the coherent
   total-field irradiance a witness would observe at a point downstream —
   `sigma_scat_downstream` cannot, by construction, distinguish "forward
   diffraction that cancels the beam in shadow" from "forward diffraction
   that refills it," because that distinction requires the field's PHASE,
   which a Poynting-flux magnitude integral discards.** This is a load-
   bearing idealization this cycle's own Phase-1 proposal disclosed in
   general terms (§5, "cross-section measurement, not downstream-
   intensity-ratio measurement") but did not connect specifically to why
   Prediction 3 itself was mis-calibrated — stated explicitly here rather
   than left implicit. **A further, separate scope caveat (MATERIALS'
   Phase-5 finding)**: this extinction-paradox magnitude describes the
   article AS SIMULATED — `graded_black_shell`'s own 1.44 µm shell
   thickness (`(R4_R_OUT−PEC_R_R4)·DX_M_R4`) is the identical construction
   `experiments/034-.../REALIZABILITY_MEMO.md` Amendments 6–7 already lock
   **UNOBTANIUM-WITH-PARAMETERS**, overdetermined by thickness (every real
   comparator class 6.9×–3472× thicker). A real, buildable coating at this
   thickness would be far less optically black and would show a
   correspondingly smaller forward-diffracted lobe by the same physics —
   this cycle's own falsification magnitude is a property of a
   locked-unrealizable article, not one a real coating at this thickness
   would reproduce.
4. **`box_dev_scat_downstream ≤ 0.12` — CONFIRMED at all 12 cells**, range
   `[0.0057, 0.0454]`, 2.6×–21× inside the bar even with the Fix-4
   disclosed weaker `C40_R4` cross-check (~6% box-size spread) — the
   derived quantity is genuinely box-independent at both configs, despite
   the asymmetric independence-check power.

**Constraint 2** (`observer_article_norm`, unchanged `observer_record_t28`)
stays clean this cycle: `[1.1543e-4, 3.9490e-4]` across all 12 cells
(**correction, Phase-5 VISION/EM finding**: the range as first drafted
here, `2.26e-4`–`3.95e-4`, was actually only `C40_R4`'s own subset — the
true 12-cell minimum, `G40_R4` @ 37.127°, is less than half that figure),
≥173× inside the R18 validation-gate bar (`<0.02`), matching Iteration
77's own finding that this instrument was never broken.

**Thermal sidecar (Fix 3, R21 compliance — narrated per the mandatory
commitment, not merely persisted).** All 12 fresh `netd_row()`
classifications (`p_abs_w`, `dt_ss_full_K`, `netd_classification`) are
code-enforced present in `results.json` (`NETD_ROW_KEYS` assert). Their
headline finding: **every one of the 12 cells classifies UNDETECTABLE**
(consistent with every prior R4-family NETD reading on this bench, exp-095
through exp-100), 368× below `NETD_BAND_K`'s lower edge at the largest
measured `dt_ss_full_K` (5.4347e-5 K). **Correction (Phase-5
THERMODYNAMICS finding)**: this document's first draft claimed `p_abs_w`/
`dt_ss_full_K` "track the same smooth, monotonic-with-θ trend as
`sigma_abs`" — false, independently reproduced: `sigma_abs` rises +8.96%
across the sweep while `p_abs_w`/`dt_ss_full_K` rise +18.71%, a 2.09×
divergence with an exact mechanical cause (`lab/thermo_sidecar.py`'s
`iso_xsec_sq` convention makes `p_abs_w ∝ sigma_ext_cells²`, quadratic,
while `sigma_abs ∝ sigma_ext_cells`, linear, at a nearly flat
`ratio_abs_ext_raw`) — confirmed to 5 significant figures at all 6
angles, not noise. `sigma_abs` is cited in its native cross-section units
(cells); `p_abs_w` in Watts — no shared unit exists between them, so
"tracking the same trend" was never a well-formed comparison. Neither
this divergence nor Prediction 3's own falsified forward-scattered
residual (**disclaimer, THERMODYNAMICS' Phase-5 finding**: an elastic,
source-wavelength [600nm] scattering channel, mechanically disjoint from
this sidecar's thermal-IR re-radiation chain — `cell_metrics_r4`'s call
to `absorbed_power_established_ratio` never references
`back_frac`/`fwd_frac`/`sigma_scat_downstream`) raises any constraint-3
re-radiation risk this cycle.

## Learned

- The closed-box reconstruction is interpretable where `beam_behind_t28`
  was not: every one of the 12 cells resolved cleanly, with tight,
  physically coherent cross-config agreement (`C40_R4`/`G40_R4` agree to
  within 0.0007–0.0016 on `back_frac` across the sweep — **correction,
  Phase-5 Red Team final audit**: not "3 decimal places at every angle" as
  first drafted, which fails at 5 of 6 angles under direct digit-by-digit
  comparison) — a genuinely higher-quality instrument than its
  predecessor, not merely a different number.
- `sigma_scat_downstream` (POWER crossing the box's downstream face in the
  scattered field) is NOT a proxy for "does the shadow stay dark" — the
  extinction paradox means a real, near-total shadow REQUIRES a
  comparably large forward-scattered cross-section, not a small one. Any
  future constraint-1 instrument that wants "does light reach the far
  side" must measure coherent TOTAL-field amplitude/phase at a point (or
  small region) downstream, not an incoherent power integral over a
  box face — this is a structurally different measurement, not a
  refinement of this one. This is this cycle's own single most important,
  disclosed finding, and the correct next step for constraint 1 on this
  bench (see Next).
- `back_frac`'s real, monotonic decline with θ (0.65→0.53 across a 5.8°
  sweep) is a genuine, reproducibly-measured trend, un-pre-registered —
  but (per PHOTONICS' Phase-5 finding, Result item 2 above) very likely a
  fixed-lab-frame-box artifact rather than confirmed article physics;
  worth a future cycle's attention (an orientation-sensitivity test, not
  a T1 mechanism claim) if this article class is ever revisited.
- Every mandatory Phase-2 fix discharged as designed: R13/14/15 (no cell
  needed the `UNRESOLVED-BY-CONSTRUCTION` escape valve, but the gate was a
  real, executed check, not merely asserted), R17 (both configs' box
  margins verified ≥90 cells before any FDTD call), R21 (narrated above,
  not merely persisted), R9/T9 (disclaimer carried through Result).

## Next (candidate directions, not this cycle's scope)

1. **Build a coherent, phase-resolved downstream point-intensity
   instrument** (total-field amplitude at a witness-scale standoff,
   compared coherently against the empty-scene reference) — the
   structurally correct successor to both `beam_behind_t28` and this
   cycle's own `sigma_scat_downstream`, and the only route to actually
   answering constraint 1's witness question ("does the background stay
   lit") rather than an energy-partition proxy for it. **(Correction,
   Phase-5 VISION finding: this is constraint 1's own missing
   conversion, NOT "T3" as first drafted here — T3 is LOGBOOK's unrelated
   temporal-contrast/switching instrument; dropped.)** Two binding
   preconditions this cycle's own Phase-5 layer surfaced: (a) correctly
   normalize the incident reference for oblique incidence (fix or
   explicitly correct the `i_inc`/`cosθ` artifact, Result item 3) — this
   instrument will need a genuinely absolute intensity, not a ratio; (b)
   use a beam-aligned or beam-rotating reference frame, not a fixed
   lab-frame box (Result item 2) — inheriting either artifact unmodified
   would compromise the new instrument from first light.
2. Investigate `back_frac`'s angular trend (0.65→0.53) — an
   orientation-sensitivity test on the box itself, not a T1 mechanism
   claim — if a future cycle returns to this article class.
3. Tier 1 (the R3-vs-R4 `delta_scene`-realizability split, PHOTONICS'
   zero-FDTD physical-hypothesis check first) remains queued, unchanged,
   per exp-100's own Reconciled Iteration-78 ranking — untouched this
   cycle by design.

## LOGBOOK.md RULED OUT registry / standing rules check

No item in LOGBOOK's RULED OUT registry (lines 8–877) or the T28 thread
narrative (lines 2572–6912) is re-proposed here — this is a zero-mechanism
instrument fix, explicitly commissioned by Iteration 77's own Reconciled
Iteration-78 queue, Tier 0. Pre-Phase-4 standing-rule risk was assessed
and discharged per Red Team's Phase-2 audit §4: R13/14/15 (fix 1), R17
(fix 4), and R21 (fix 3) were genuinely at risk of firing Checkpoint
criterion 4 as originally proposed; R20 was flagged as a contingent risk
via the R3-vs-R4 pool-duplication finding (fix 5) — that specific,
anticipated R20 exposure WAS discharged as designed (neither selected
angle is a duplicated row, and the caveat is carried, not settled fact).

**R20 fired anyway, at Phase 5, via three unanticipated instances — the
first time in this program's history R20's own automatic clause has
actually triggered a Checkpoint.** Red Team's Phase-5 final audit
independently confirmed three genuine R4-class citation/coincidence
defects in this document's own Result prose (the `observer_article_norm`
range, the `back_frac` "3-decimal-place" claim, the thermal-sidecar
"same trend" claim — see the corrections marked above), each caught only
at Phase 5, none load-bearing to any scored verdict, meeting R20's
"three or more" bar under the most conservative valid counting.
Checkpoint criterion 4 therefore FIRES this cycle — see the CHECKPOINT
entry in LOGBOOK.md/SESSION_LOG.md (Director's action, Iteration 78
close). R4, R9 (aside from the `i_inc`/`cosθ` finding, ruled R9-shaped
not R20-shaped — see Result item 3), R11, R19 were not at risk.
