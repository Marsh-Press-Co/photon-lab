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
  human witness see the background still lit" (that conversion is the
  still-unbuilt T3 instrument, out of scope here). No perceptual threshold
  (`C_thr_lab`/`C_thr_field`) is invoked or scored this cycle.
- `sigma_abs + sigma_scat_downstream + sigma_scat_sourceward` is NOT an
  exact partition of `sigma_ext` — a lateral/diffuse remainder exits
  through the box's `y0`/`y1` faces.
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

## LOGBOOK.md RULED OUT registry / standing rules check

No item in LOGBOOK's RULED OUT registry (lines 8–877) or the T28 thread
narrative (lines 2572–6912) is re-proposed here — this is a zero-mechanism
instrument fix, explicitly commissioned by Iteration 77's own Reconciled
Iteration-78 queue, Tier 0. Standing-rule risk assessed and discharged per
Red Team's Phase-2 audit §4: R13/14/15 (fix 1), R17 (fix 4), and R21 (fix
3) were genuinely at risk of firing Checkpoint criterion 4 as originally
proposed; R20 was a contingent risk (fix 5). All four are discharged by
the six mandatory fixes above, implemented in code (not merely asserted in
prose) before this Phase-4 run. R4, R9, R11, R19 were not at risk (Red
Team's audit independently re-verified every cited figure this cycle).
