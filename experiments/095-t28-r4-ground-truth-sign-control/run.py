"""exp-095 -- T28 R4 Ground-Truth Sign Control, cpl=50 (R5) Third Resolution
Point, sigma/38.4deg Comparability Closes: Panel Iteration 72. Lead seat
(rotation): VISION SCIENCE. Frozen spec: NOTES.md (Predictions committed to
git strictly BEFORE this file's first run, house discipline). Change
rationale: phase2_redteam_audit.md (9 Red-Team-mandatory fixes, all
adopted, zero overridden -- see NOTES.md's own "Changes from Phase 1"
section for the item-by-item mapping).

Four ranks, run in this exact order:

  Rank 1  (16 calls, FIRST, unconditional) -- combined go/no-go gate on the
            `R4` (cpl=40) family: Rank 1a (sign check, 8 calls, 39.2/39.4deg)
            + Rank 1c (node-bracketing recovery check, 8 calls, NEW,
            38.49/38.69deg around the established cpl=20 null 38.590deg).
  Rank 4  (4 calls, SECOND, unconditional -- independent of Rank 1's
            verdict) -- 38.4deg at corrected sigma, `R3` (cpl=30) family.
  Rank 2  (36 calls, THIRD, gated on Rank 1 PROCEED) -- `R5` (cpl=50)
            family: Rank 2a (settling precondition, 8 calls) -> Rank 2b
            (interior six-angle sweep, 24 calls, gated on 2a not HALTing)
            + Rank 2b-native (native-sigma comparator leg, 4 calls, NEW,
            41.825/41.850deg, article-only, empty legs reused in-memory
            from Rank 2b itself).
  Rank 3  (30 calls, FOURTH, gated on Rank 1 PROCEED) -- `R4` (cpl=40)
            sigma-comparability: Rank 3a (41.6deg, native+corrected sigma,
            6 calls) + Rank 3b (six interior angles, native sigma, 24
            calls -- corrected count, see module docstring disclosure (iv)
            below).

Total: 86 FDTD calls if Rank 1 gate PASSES (16+36+30+4); 20 calls if it
FAILS (16+4, Ranks 2/3 skipped). See NOTES.md's own "Disclosed
spec-resolution note" for why these totals differ from the Phase-1/
Red-Team-stated 72/18 (Rank 3b 12->24, Rank 4 2->4 -- a call-accounting
correction, not a design change).

Reuses experiments/094-.../run.py's own `dg`/`PAIR_KEYS_R3`/`PAIR_KEYS_R4`/
`STEPS_R3`/`SIGMA_NATIVE`/`SIGMA_R3_CORRECTED`/`SIGMA_R4_CORRECTED`/
`cell_metrics`/`cell_metrics_full`/`cell_metrics_r4`/`pair_metrics`/
`pair_metrics_full`/`one_call`/`one_call_r4`/`run_block`/`run_block_r4`/
`compute_floor`/`XI_TOL`/`NOISE_MULT`/`RATIO_LOW`/`RATIO_HIGH`/
`NETD_BAND_K`/`find_zero_crossings`/`ratio_sign_verdict`/
`classification_word`/`compute_zone`/`VERDICT_RANK`/`netd_row`/
`box_for_r3`/`ref_for_r3`/`build_article_r3_sigma`/`_run_sim_r3_sigma`/
`box_for_r4`/`ref_for_r4`/`build_article_r4_sigma`/`_run_sim_r4_sigma`/
`PEC_R_R3`/`PEC_R_R4`/`BOX_CLEARANCE_A_R3`/`BOX_CLEARANCE_B_R3`/
`BOX_CLEARANCE_A_R4`/`BOX_CLEARANCE_B_R4`/`REF_HALF_H_R3`/`REF_HALF_H_R4`/
`DX_M_R3`/`DX_M_R4`/`L_GEOMETRIC_M_R3`/`L_GEOMETRIC_M_R4`/`L_GEOMETRIC_M`/
`widths_direction_corrected`/`_profile`/`contrast_pair`/
`IRR_CENTRAL_W_CM2`/`K_AIR`/`DENSITY_SI_KG_M3`/`C_P_SI_J_KGK`/
`EMISSIVITY`/`T_AMBIENT_K` VERBATIM, UNMODIFIED, by loading
experiments/094-.../run.py as a module (which itself already loads
093->092->091->090 the same way) -- zero `lab/` diff, zero diff to any
frozen experiment file.

NEW code this cycle (all additive; experiments/069-.../design_geometry.py
already gained an appended-only `R5` block prior to this Phase -- read
directly, not re-derived, see that file's own "R5 family" comment header):

  * `box_for_r5`/`ref_for_r5` -- R5-scaled mirrors of `box_for_r4`/
    `ref_for_r4`.
  * `build_article_r5_sigma(sim, cx, cy, sigma_max)` -- R5-scaled mirror of
    `build_article_r4_sigma`.
  * `_run_sim_r5_sigma(cfg, theta, steps, with_article, sigma_max)` --
    mirrors `_run_sim_r4_sigma` exactly, including the mandatory Gate 5
    runtime `sigma_e`/`sigma_max` check from this function's FIRST commit
    (Red Team mandatory-fix docket, item under "Also write..." -- Gate 5
    for R5, per phase2_redteam_audit.md's own confirmation this is
    correctly planned).
  * `one_call_r5`/`run_block_r5` -- module-level (picklable) worker /
    thin execution-plumbing mirror of `one_call_r4`/`run_block_r4`,
    dispatching to `dg.R5_CONFIGS`.
  * `cell_metrics_r5` -- THERMODYNAMICS' own R16-risk catch (mandatory fix
    #7): explicit line-for-line mirror of `cell_metrics_r4`, substituting
    every R4-scoped constant/function for its R5 equivalent. Its
    `netd_row()` merge is wired into every Rank-2/Rank-2a report dict in
    the SAME diff that adds this function (not added later).

DISCLOSED SPEC-RESOLUTION NOTES (frozen-spec ambiguities resolved
conservatively toward the spec's own stated, load-bearing intent, per this
phase's own instructions -- each repeated in NOTES.md and the Phase-4
final report):

  (i) Rank 1's combined go/no-go criterion ("PROCEED to Rank 2/3 only if
      Rank 1a is PASS ... AND Rank 1c is PASS or INCONCLUSIVE") is
      implemented as a single boolean `proceed_gate`, computed once, after
      both Rank 1a and Rank 1c have both run (Rank 1's own 16 calls are
      unconditional and always both execute in full, per the Director's
      own spec -- only Rank 2/3's spend is gated, never Rank 1's own).

  (ii) Rank 2a's own settling precondition, and Rank 1a's own settling
      precedent from exp-094 -- "at both/either config" -- is read
      identically to exp-094's own module docstring disclosure (ii): ONE
      settling check per angle (delta_scene is, throughout this program, a
      PAIRED quantity needing both configs simultaneously), not two
      independent per-config numbers. Mandatory fix #8's NEW p_abs_w
      settling check is implemented the same way: one p_abs_w-channel
      settling check (reusing the G/C `p_abs_w` ratio quantity's own rel_
      dev across the two STEPS values), not per-config.

  (iii) Mandatory fix #5's companion desk bound ("if Rank 2b's
      classification at any of the six angles DIFFERS from exp-094's own
      already-filed Rank 1b (cpl=40) classification at the corresponding
      angle") is read as comparing Rank 2b's per-angle `classification`
      field (CONSISTENT/ENERGY-DOMINANT/ENERGY-DECOUPLED/NODE-UNRESOLVABLE,
      exp-094's own established taxonomy) directly against exp-094's own
      filed `rank1b.per_theta[theta]['classification']` at the identical
      angle -- both already use this exact taxonomy, no re-derivation
      needed.

  (iv) Rank 3b's and Rank 4's own call-count language ("empty legs already
      filed... article-only") describes CROSS-PROCESS reuse using language
      that, on independent verification this Phase, only correctly
      describes exp-093's own Item 3 SAME-PROCESS reuse idiom (an
      in-memory captures dict populated earlier in that same script's own
      execution). This codebase's `results.json` convention never
      persists raw field captures, only derived scalar metrics (confirmed
      by reading experiments/093/094-.../results.json directly this
      session); `delta_scene = C_g - C_c`, and each config's own `C`
      requires BOTH its empty-scene AND article-scene captures
      (`contrast_pair`, confirmed by reading experiments/091-.../run.py
      directly). A genuinely NEW sigma-branch reading therefore
      structurally requires a FRESH empty-scene capture alongside the
      fresh article capture -- there is no raw-capture object left over
      from exp-094's own, separate, already-closed process to reuse.
      Resolved identically to how exp-094's own Rank 2 handled an
      analogous cross-process comparison: the "already filed" side is a
      pulled SCALAR comparator (zero new calls), and the new side spends
      its full empty+article pair. This raises Rank 3b from the Phase-1
      draft's stated 12 calls to **24**, and Rank 4 from 2 to **4** (both
      configs x both legs) -- see NOTES.md's own "Disclosed
      spec-resolution note" for the full reasoning. Nothing about angles,
      sigma choices, gating logic, or outcome taxonomy changes.

  (v) Rank 2b-native's own empty-leg reuse (mandatory fix #3) is, by
      contrast, genuinely SAME-PROCESS (Rank 2b and Rank 2b-native both
      run inside this exact script execution, same R5 family, same
      angles, same STEPS) -- implemented as a literal in-memory dict
      lookup into `captures_r2b`, mirroring exp-093's own Item 3 idiom
      exactly, zero new empty-leg calls, matching the Director's own
      stated 4-call figure for this item without correction.
"""

import importlib.util
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..094's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP090_RESULTS = os.path.join(EXP090_DIR, "results.json")
EXP092_DIR = os.path.join(ROOT, "experiments", "092-t28-crossing-relocation-caution-zone-rebuild")
EXP092_RESULTS = os.path.join(EXP092_DIR, "results.json")
EXP083_DIR = os.path.join(ROOT, "experiments", "083-t28-pad-article-full-power-retest")
EXP083_RESULTS = os.path.join(EXP083_DIR, "results.json")
EXP094_DIR = os.path.join(ROOT, "experiments", "094-t28-cpl40-resolution-sigma-r3-census")
EXP094_RESULTS = os.path.join(EXP094_DIR, "results.json")

exp094 = _load(os.path.join(EXP094_DIR, "run.py"), "_exp095_exp094")
exp093 = exp094.exp093    # exp-094's own module already loaded exp-093 this way
exp092 = exp094.exp092    # ...and exp-092, same chain
exp091 = exp094.exp091    # ...and exp-091, same chain
exp090 = exp094.exp090    # ...and exp-090, same chain

dg = exp094.dg
PAIR_KEYS_R3 = exp094.PAIR_KEYS_R3
PAIR_KEYS_R4 = exp094.PAIR_KEYS_R4
STEPS_R3 = exp094.STEPS_R3
assert STEPS_R3 == 4200
SIGMA_NATIVE = exp094.SIGMA_NATIVE
SIGMA_R3_CORRECTED = exp094.SIGMA_R3_CORRECTED
SIGMA_R4_CORRECTED = exp094.SIGMA_R4_CORRECTED
assert SIGMA_NATIVE == 0.5
assert abs(SIGMA_R3_CORRECTED - 1.0 / 3.0) < 1e-12
assert abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12

cell_metrics = exp094.cell_metrics
cell_metrics_full = exp094.cell_metrics_full
cell_metrics_r4 = exp094.cell_metrics_r4
pair_metrics = exp094.pair_metrics
pair_metrics_full = exp094.pair_metrics_full
one_call = exp094.one_call
one_call_r4 = exp094.one_call_r4
run_block = exp094.run_block
run_block_r4 = exp094.run_block_r4
compute_floor = exp094.compute_floor
XI_TOL = exp094.XI_TOL
NOISE_MULT = exp094.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp094.RATIO_LOW, exp094.RATIO_HIGH
NETD_BAND_K = exp094.NETD_BAND_K
find_zero_crossings = exp094.find_zero_crossings
ratio_sign_verdict = exp094.ratio_sign_verdict
classification_word = exp094.classification_word
compute_zone = exp094.compute_zone
VERDICT_RANK = exp094.VERDICT_RANK
netd_row = exp094.netd_row

# R3-family plumbing, pulled through exp-094's own module scope (which
# itself pulled these through exp-092/exp-091 -- see exp-094's own module
# docstring for the exact provenance chain).
box_for_r3 = exp094.box_for_r3
ref_for_r3 = exp094.ref_for_r3
build_article_r3_sigma = exp094.build_article_r3_sigma
_run_sim_r3_sigma = exp094._run_sim_r3_sigma
PEC_R_R3 = exp094.PEC_R_R3
BOX_CLEARANCE_A_R3 = exp094.BOX_CLEARANCE_A_R3
BOX_CLEARANCE_B_R3 = exp094.BOX_CLEARANCE_B_R3
DX_M_R3 = exp094.DX_M_R3
L_GEOMETRIC_M_R3 = exp094.L_GEOMETRIC_M_R3
REF_HALF_H_R3 = exp094.REF_HALF_H_R3
widths_direction_corrected = exp094.widths_direction_corrected
_profile = exp094._profile
contrast_pair = exp094.contrast_pair
IRR_CENTRAL_W_CM2 = exp094.IRR_CENTRAL_W_CM2
K_AIR = exp094.K_AIR
DENSITY_SI_KG_M3, C_P_SI_J_KGK = exp094.DENSITY_SI_KG_M3, exp094.C_P_SI_J_KGK
EMISSIVITY = exp094.EMISSIVITY
T_AMBIENT_K = exp094.T_AMBIENT_K
L_GEOMETRIC_M = exp094.L_GEOMETRIC_M

# R4-family plumbing, defined directly at exp-094's own module scope.
box_for_r4 = exp094.box_for_r4
ref_for_r4 = exp094.ref_for_r4
build_article_r4_sigma = exp094.build_article_r4_sigma
_run_sim_r4_sigma = exp094._run_sim_r4_sigma
PEC_R_R4 = exp094.PEC_R_R4
BOX_CLEARANCE_A_R4 = exp094.BOX_CLEARANCE_A_R4
BOX_CLEARANCE_B_R4 = exp094.BOX_CLEARANCE_B_R4
REF_HALF_H_R4 = exp094.REF_HALF_H_R4
DX_M_R4 = exp094.DX_M_R4
L_GEOMETRIC_M_R4 = exp094.L_GEOMETRIC_M_R4

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts, materials  # noqa: E402

# ---------------------------------------------------------------- R5 family constants
PEC_R_R5 = dg.PEC_R_R5
BOX_CLEARANCE_A_R5 = dg.BOX_CLEARANCE_A_R5
BOX_CLEARANCE_B_R5 = dg.BOX_CLEARANCE_B_R5
REF_HALF_H_R5 = dg.REF_HALF_H_R5
SIGMA_R5_CORRECTED = dg.SIGMA_R5_CORRECTED
DX_M_R5 = dg.DX_M_R5
L_GEOMETRIC_M_R5 = dg.L_GEOMETRIC_M_R5
assert abs(SIGMA_R5_CORRECTED - 0.2) < 1e-12
PAIR_KEYS_R5 = ("C40_R5", "G40_R5")

# ---------------------------------------------------------------- angles
RANK1A_ANGLES = [39.2, 39.4]                 # sign check (mandatory fix #1)
RANK1C_ANGLES = [38.49, 38.69]               # node-bracketing (mandatory fix #2)
RANK2A_ANGLE = 41.825                        # R5 settling precondition
RANK2B_ANGLES = [41.750, 41.775, 41.825, 41.850, 41.875, 41.900]
RANK2B_NATIVE_ANGLES = [41.825, 41.850]      # mandatory fix #3
RANK3A_ANGLE = 41.6
RANK3B_ANGLES = [41.750, 41.775, 41.825, 41.850, 41.875, 41.900]  # same 6 as Rank 2b/exp-094 Rank 1b
RANK4_ANGLE = 38.4

for _a in RANK2B_NATIVE_ANGLES:
    assert _a in RANK2B_ANGLES
assert RANK3B_ANGLES == RANK2B_ANGLES == exp094.RANK1B_ANGLES


# ================================================================== R5 layer
def box_for_r5(cfg, clearance):
    ox, oy = cfg["obj_x"], cfg["obj_y"]
    r = dg.R5_R_OUT + clearance
    return (ox - r, ox + r, oy - r, oy + r)


def ref_for_r5(cfg):
    return (cfg["obj_x"], cfg["obj_y"], REF_HALF_H_R5)


def build_article_r5_sigma(sim, cx, cy, sigma_max):
    """R5-scaled mirror of `build_article_r4_sigma` -- same two calls
    (pec_disk core + graded_black_shell), radii scaled by R5_RATIO=2.5."""
    materials.pec_disk(sim, cx, cy, PEC_R_R5)
    materials.graded_black_shell(sim, cx, cy, PEC_R_R5, dg.R5_R_OUT, sigma_max=sigma_max)


def _run_sim_r5_sigma(cfg, theta, steps, with_article, sigma_max):
    """Mirrors `_run_sim_r4_sigma` exactly, calling `build_article_r5_sigma`.
    Carries this cycle's own mandatory Gate 5 (Red Team, "Also write..."
    item): immediately after building the article, BEFORE `sim.run()`,
    verify the actual value landing in the constructed Sim's own `sigma_e`
    array at the article's shell cells -- not a Python constant -- matches
    `sigma_max`. `shell_mask` below is read directly off
    `lab/materials.py::graded_black_shell`'s own indexing (rr from the
    ez-point radius/angle grid centered at (cx,cy), `r_in <= rr <= r_out`),
    mirroring `_run_sim_r4_sigma`'s own indexing exactly, R5 constants
    substituted -- wired from this function's FIRST commit, not
    retrofitted."""
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R5_CPL[600],
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    if with_article:
        cx, cy = cfg["obj_x"], cfg["obj_y"]
        build_article_r5_sigma(sim, cx, cy, sigma_max)
        rr, _ = materials._grids(sim, cx, cy)["ez"]
        shell_mask = (rr >= PEC_R_R5) & (rr <= dg.R5_R_OUT)
        actual_sigma_max = float(sim.sigma_e[shell_mask].max())
        assert np.isclose(actual_sigma_max, sigma_max, atol=1e-9), (
            f"GATE 5 FAILED -- runtime sigma_e/sigma_max mismatch: "
            f"sim.sigma_e[shell_mask].max()={actual_sigma_max!r} vs "
            f"sigma_max={sigma_max!r} passed at (cx={cx},cy={cy})")
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta, amplitude=1.0,
                         profile="plane", edge=dg.R5_TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def one_call_r5(args):
    """Module-level (picklable) worker for the new R5 keys. args = (key,
    theta, with_article, steps, sigma_max)."""
    key, th, art, steps, sigma_max = args
    cfg = dg.R5_CONFIGS[key]
    cap = _run_sim_r5_sigma(cfg, th, steps, art, sigma_max)
    return (key, th, art, steps, sigma_max, cap)


def run_block_r5(jobs):
    """Thin, mechanical copy of `run_block_r4`, dispatching to
    `one_call_r5` instead -- pure execution plumbing, identical structure,
    no metric/formula touched. Returns (captures_dict, wall_seconds)."""
    t0 = time.time()
    captures = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, sigma_max, cap) in enumerate(ex.map(one_call_r5, jobs), 1):
            captures[(key, th, art, steps)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key:8s} theta={th:+06.3f} "
                  f"article={art} steps={steps} sigma_max={sigma_max}", flush=True)
    wall = time.time() - t0
    return captures, wall


def cell_metrics_r5(key, th, steps, cap_empty, cap_article):
    """Explicit line-for-line mirror of `cell_metrics_r4` (mandatory fix
    #7, THERMODYNAMICS' own R16-risk catch), substituting every R4-scoped
    constant/function for its R5 equivalent. Its returned dict's `thermo`
    sub-dict already carries sigma_ext_cells/ratio_abs_ext_raw/p_abs_w/
    dt_ss_full_K/netd_classification IN FULL -- `pair_metrics`/
    `pair_metrics_full` are called on this output UNMODIFIED, exactly as
    NOTES.md specifies. Its netd_row() merge happens downstream, wherever
    `pair_metrics_full` is called on this function's C/G outputs (same
    diff as this function, per mandatory fix #7)."""
    cfg = dg.R5_CONFIGS[key]
    box_a = box_for_r5(cfg, BOX_CLEARANCE_A_R5)
    box_b = box_for_r5(cfg, BOX_CLEARANCE_B_R5)
    ref = ref_for_r5(cfg)

    widths = {}
    xi_ext = {}
    for box_name, box in (("BOX_A", box_a), ("BOX_B", box_b)):
        w = widths_direction_corrected(cap_article, cap_empty, box, ref)
        widths[box_name] = w
        xi = abs(w["sigma_ext_cross"] - w["sigma_ext"]) / abs(w["sigma_ext"])
        xi_ext[box_name] = xi

    ba, bb = widths["BOX_A"], widths["BOX_B"]
    box_dev = dict(
        ext=abs(ba["sigma_ext"] - bb["sigma_ext"]) / abs(ba["sigma_ext"]),
        abs=abs(ba["sigma_abs"] - bb["sigma_abs"]) / abs(ba["sigma_abs"]),
    )

    sigma_ext_cells = ba["sigma_ext"]
    ratio_abs_ext_raw = ba["sigma_abs"] / ba["sigma_ext"] if ba["sigma_ext"] != 0 else 0.0
    ratio_abs_ext_clamped = min(max(ratio_abs_ext_raw, 0.0), 1.0)
    p = ts.absorbed_power_established_ratio(
        IRR_CENTRAL_W_CM2, sigma_ext_cells, DX_M_R5, ratio_abs_ext_clamped)
    regime = ts.mixed_length_scale_regime(
        p_abs_w=p["p_abs_w"], l_geometric_m=L_GEOMETRIC_M_R5,
        k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
        length_provenance="bench_construction")
    netd = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
    thermo = dict(sigma_ext_cells=sigma_ext_cells, ratio_abs_ext_raw=ratio_abs_ext_raw,
                  p_abs_w=p["p_abs_w"], dt_ss_full_K=regime["dt_ss_full_K"],
                  netd_classification=netd["classification"])

    empty_p = _profile(cap_empty, cfg)
    scene_p = _profile(cap_article, cfg)
    C, C_empty = contrast_pair(cfg, empty_p, scene_p, dg.R5_W_OBJ, dg.R5_GUARD_OUT, dg.R5_W_FLANK)

    return dict(xi_ext=xi_ext, box_dev=box_dev, thermo=thermo, C=C, C_empty=C_empty,
                sigma_abs_nonneg=bool(ba["sigma_abs"] >= 0))


R2B_NO_DISCHARGE_SENTENCE = (
    "This outcome alone does NOT discharge R15's Iteration-71 addendum -- "
    "R5 is drawn from the identical r{n}_config() mechanical recipe as "
    "R3/R4 (only Gate-3-exact ratios, i.e. cpl a multiple of 10, are "
    "reachable), so a recipe-level systematic would reproduce identically "
    "at this ratio too. See Idealization 17/28/29."
)


def main():
    print("=" * 78)
    print("exp-095 -- T28 R4 ground-truth sign control, cpl=50 (R5) third "
          "resolution point, sigma/38.4deg comparability closes")
    print("=" * 78)

    t_start = time.time()

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD, unchanged)
    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR={floor:.6e}  (unchanged, applied unrecomputed -- Idealization 6)")

    xi_pass = True
    nonneg_pass = True

    # =================================================================
    # Mandatory new-suite gates 1-4, 6 (static/algebraic, R5 family)
    # =================================================================
    print("\n" + "=" * 78)
    print("MANDATORY NEW-SUITE GATES (static/algebraic, R5 family)")
    print("=" * 78)

    # ---- Gate 1: vacuum-footprint precondition, applied to R5_CONFIGS
    vac_report = {}
    vac_pass = True
    for key in PAIR_KEYS_R5:
        cfg = dg.R5_CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R5_CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A_R5), ("BOX_B", BOX_CLEARANCE_B_R5)):
            x0, x1, y0, y1 = box_for_r5(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            vac_pass = vac_pass and ok
        vac_report[key] = cell
    print(f"[Gate 1] vacuum-footprint precondition (R5_CONFIGS): PASS={vac_pass}")
    assert vac_pass, "GATE 1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # ---- Gate 2: A congruence
    a_c40 = dg.R5_CONFIGS["C40_R5"]["A"]
    a_g40 = dg.R5_CONFIGS["G40_R5"]["A"]
    gate2_pass = (a_c40 == a_g40 == round(dg.A_HALF_APERTURE * dg.R5_RATIO) == 1880)
    print(f"[Gate 2] A congruence: C40_R5.A={a_c40}  G40_R5.A={a_g40}  "
          f"round(A_HALF_APERTURE*R5_RATIO)={round(dg.A_HALF_APERTURE * dg.R5_RATIO)}  PASS={gate2_pass}")
    assert gate2_pass, "GATE 2 FAILED -- R5 congruent-construction identity broken; HALT"

    # ---- Gate 3: L_GEOMETRIC_M_R5 bit-identity across native/R3/R4/R5 (three-way, new family)
    gate3_dev_native = abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M)
    gate3_dev_r3 = abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R3)
    gate3_dev_r4 = abs(L_GEOMETRIC_M_R5 - L_GEOMETRIC_M_R4)
    gate3_pass = gate3_dev_native < 1e-12 and gate3_dev_r3 < 1e-12 and gate3_dev_r4 < 1e-12
    print(f"[Gate 3] L_GEOMETRIC_M_R5={L_GEOMETRIC_M_R5:.6e}  L_GEOMETRIC_M={L_GEOMETRIC_M:.6e}  "
          f"L_GEOMETRIC_M_R3={L_GEOMETRIC_M_R3:.6e}  L_GEOMETRIC_M_R4={L_GEOMETRIC_M_R4:.6e}  "
          f"PASS={gate3_pass}")
    assert gate3_pass, "GATE 3 FAILED -- R5 physical shell radius does not match native/R3/R4; HALT"

    # ---- Gate 4: SIGMA_R5_CORRECTED == 0.2
    gate4_pass = abs(SIGMA_R5_CORRECTED - 0.2) < 1e-12
    print(f"[Gate 4] SIGMA_R5_CORRECTED={SIGMA_R5_CORRECTED}  PASS={gate4_pass}")
    assert gate4_pass, "GATE 4 FAILED -- SIGMA_R5_CORRECTED != 0.2; HALT"

    # ---- Gate 6 (documentation-only, non-discriminating -- R4's own precedent; never a substitute for Gate 5)
    gate6_lhs = 2 * SIGMA_R5_CORRECTED * dg.R5_R_OUT
    gate6_rhs = 2 * SIGMA_NATIVE * dg.R_OUT
    gate6_dev = abs(gate6_lhs - gate6_rhs)
    gate6_pass = gate6_dev < 1e-9
    print(f"[Gate 6, documentation-only] 2*SIGMA_R5_CORRECTED*R5_R_OUT={gate6_lhs}  "
          f"2*SIGMA_NATIVE*R_OUT={gate6_rhs}  dev={gate6_dev:.3e}  PASS={gate6_pass}  "
          f"(non-discriminating -- reduces to a tautology already implied by Gate 4; "
          f"NOT a substitute for Gate 5 below)")

    print("\n[Gate 5] (mandatory, from this family's first commit) runtime sigma_e/sigma_max "
          "check -- wired INSIDE `_run_sim_r5_sigma` itself, fires on every Rank 2 article "
          "call at corrected sigma, before any FDTD step. See per-call confirmation below.")

    # =================================================================
    # RANK 1 -- FIRST, combined go/no-go gate on the R4 family (16 calls, UNCONDITIONAL)
    # =================================================================
    print("\n" + "=" * 78)
    print("RANK 1 -- combined go/no-go gate, R4 (cpl=40) family (16 calls, UNCONDITIONAL)")
    print("=" * 78)

    # -------- Rank 1a: sign check, 39.2/39.4deg (mandatory fix #1) --------
    print(f"\n[Rank 1a] sign check @ {RANK1A_ANGLES}deg (sigma_max={SIGMA_R4_CORRECTED} corrected)")

    jobs_r1a = []
    for th in RANK1A_ANGLES:
        for key in PAIR_KEYS_R4:
            jobs_r1a.append((key, th, False, dg.R4_STEPS, None))
            jobs_r1a.append((key, th, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
    assert len(jobs_r1a) == 8
    print(f"{len(jobs_r1a)} FDTD calls queued (Rank 1a) -- Gate 5 fires inline on each "
          f"article call, before its own FDTD step")
    captures_r1a, wall_r1a = run_block_r4(jobs_r1a)
    print(f"Rank 1a wall time: {wall_r1a:.1f}s ({wall_r1a / 60.0:.2f} min)")
    print("[Gate 5] all 4 Rank 1a article calls completed their inline runtime "
          "sigma_e/sigma_max assert without raising -- PASS")

    cells_r1a = {}
    for th in RANK1A_ANGLES:
        for key in PAIR_KEYS_R4:
            cap_empty = captures_r1a[(key, th, False, dg.R4_STEPS)]
            cap_article = captures_r1a[(key, th, True, dg.R4_STEPS)]
            cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)
            cells_r1a[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"[Rank 1a] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 1a FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 1a] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 1a FAILED -- non-negativity gate; HALT"

    # known-crossing set, independently re-pulled this session (not hand-typed)
    with open(EXP090_RESULTS) as f:
        j090 = json.load(f)
    with open(EXP092_RESULTS) as f:
        j092 = json.load(f)
    with open(EXP083_RESULTS) as f:
        j083 = json.load(f)

    crossings_cpl20 = j090["q8"]["crossings_deg"]
    cr92 = j092["rank1"]["crossing_report"]
    crossings_cpl30 = [cr92["lower_crossing_cpl30"], cr92["upper_crossing_cpl30"],
                        cr92["upper_crossing_cpl30_second"]]
    full_crossing_set = list(crossings_cpl20) + list(crossings_cpl30)
    print(f"\n[Rank 1a] full known-crossing set (re-pulled, not hand-typed): "
          f"cpl20={[round(c, 4) for c in crossings_cpl20]}  cpl30={[round(c, 4) for c in crossings_cpl30]}")

    theta83 = j083["thetas"]
    ds83 = j083["delta_scene"]
    ds83_map = {round(t, 4): d for t, d in zip(theta83, ds83)}
    pt92 = j092["rank1"]["per_theta"]

    rank1a_report = {}
    for th in RANK1A_ANGLES:
        c_cell = cells_r1a[("C40_R4", th)]
        g_cell = cells_r1a[("G40_R4", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        nearest = min(full_crossing_set, key=lambda c: abs(th - c))
        dist = abs(th - nearest)
        ds20 = ds83_map.get(round(th, 4))
        ds30 = pt92[str(th)]["delta_scene"]
        rank1a_report[th] = dict(
            delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
            nearest_known_null_deg=nearest, distance_to_nearest_null_deg=dist,
            comparator_cpl20_delta_scene=ds20, comparator_cpl30_delta_scene=ds30,
            **netd_row(pm),
        )
    print("\n[Rank 1a PRIMARY] per-angle sign check:")
    for th, r in sorted(rank1a_report.items()):
        print(f"  theta={th}: delta_scene(R4)={r['delta_scene']:+.6e}  floor_pass={r['floor_pass']}  "
              f"nearest_null={r['nearest_known_null_deg']:.4f} (dist={r['distance_to_nearest_null_deg']:.4f}deg)  "
              f"comparator(cpl20)={r['comparator_cpl20_delta_scene']:+.6e}  "
              f"comparator(cpl30)={r['comparator_cpl30_delta_scene']:+.6e}")

    rank1a_both_negative = all(rank1a_report[th]["delta_scene"] < 0 for th in RANK1A_ANGLES)
    rank1a_both_floor_pass = all(rank1a_report[th]["floor_pass"] for th in RANK1A_ANGLES)
    if rank1a_both_negative and rank1a_both_floor_pass:
        rank1a_verdict = "PASS"
    elif not rank1a_both_floor_pass:
        rank1a_verdict = "AMBIGUOUS"
    else:
        rank1a_verdict = "FAIL"
    print(f"\n[Rank 1a PRIMARY] both negative={rank1a_both_negative}  "
          f"both floor_pass={rank1a_both_floor_pass}  VERDICT={rank1a_verdict}")

    # -------- Rank 1c: node-bracketing recovery check, 38.49/38.69deg (mandatory fix #2) --------
    print(f"\n[Rank 1c] node-bracketing recovery check @ {RANK1C_ANGLES}deg "
          f"(around established cpl=20 null theta0~=38.590deg, sigma_max={SIGMA_R4_CORRECTED} corrected)")

    theta0_38590 = crossings_cpl20[1]   # 38.590230... -- the second of the four cpl=20 crossings
    print(f"[Rank 1c] established cpl=20 null theta0={theta0_38590:.6f}deg  "
          f"(re-pulled from experiments/090-.../results.json::q8.crossings_deg, not hand-typed)")
    for th in RANK1C_ANGLES:
        assert abs(th - theta0_38590) <= 0.15, f"{th} unexpectedly far from theta0={theta0_38590}"

    jobs_r1c = []
    for th in RANK1C_ANGLES:
        for key in PAIR_KEYS_R4:
            jobs_r1c.append((key, th, False, dg.R4_STEPS, None))
            jobs_r1c.append((key, th, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
    assert len(jobs_r1c) == 8
    print(f"{len(jobs_r1c)} FDTD calls queued (Rank 1c) -- Gate 5 fires inline on each "
          f"article call, before its own FDTD step")
    captures_r1c, wall_r1c = run_block_r4(jobs_r1c)
    print(f"Rank 1c wall time: {wall_r1c:.1f}s ({wall_r1c / 60.0:.2f} min)")
    print("[Gate 5] all 4 Rank 1c article calls completed their inline runtime "
          "sigma_e/sigma_max assert without raising -- PASS")

    cells_r1c = {}
    for th in RANK1C_ANGLES:
        for key in PAIR_KEYS_R4:
            cap_empty = captures_r1c[(key, th, False, dg.R4_STEPS)]
            cap_article = captures_r1c[(key, th, True, dg.R4_STEPS)]
            cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)
            cells_r1c[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"[Rank 1c] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 1c FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 1c] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 1c FAILED -- non-negativity gate; HALT"

    rank1c_report = {}
    for th in RANK1C_ANGLES:
        c_cell = cells_r1c[("C40_R4", th)]
        g_cell = cells_r1c[("G40_R4", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        rank1c_report[th] = dict(
            delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
            **netd_row(pm),
        )
    print("\n[Rank 1c PRIMARY] per-angle node-bracketing check:")
    for th, r in sorted(rank1c_report.items()):
        print(f"  theta={th}: delta_scene(R4)={r['delta_scene']:+.6e}  floor_pass={r['floor_pass']}")

    rank1c_both_floor_pass = all(rank1c_report[th]["floor_pass"] for th in RANK1C_ANGLES)
    if not rank1c_both_floor_pass:
        rank1c_verdict = "INCONCLUSIVE"
    else:
        signs = [rank1c_report[th]["delta_scene"] > 0 for th in RANK1C_ANGLES]
        rank1c_signs_differ = signs[0] != signs[1]
        rank1c_verdict = "PASS" if rank1c_signs_differ else "FAIL"
    print(f"\n[Rank 1c PRIMARY] both floor_pass={rank1c_both_floor_pass}  VERDICT={rank1c_verdict}")

    # -------- Combined Rank 1 go/no-go --------
    proceed_gate = (rank1a_verdict == "PASS") and (rank1c_verdict in ("PASS", "INCONCLUSIVE"))
    print(f"\n[RANK 1 COMBINED GO/NO-GO] Rank 1a={rank1a_verdict}  Rank 1c={rank1c_verdict}  "
          f"PROCEED to Rank 2/3={proceed_gate}")
    if not proceed_gate:
        print("[RANK 1 COMBINED GO/NO-GO] HALT before Rank 2/3 -- integrity finding, "
              "Checkpoint-4-relevant per Phase-1's own SS2 language. Rank 4 (independent, "
              "unconditional) still runs below. Ranks 2/3 SKIPPED, results.json/NOTES.md "
              "still written in full, per this program's 'a FAIL is a reported outcome, "
              "never a crash' discipline.")

    total_fdtd_wall_rank1 = wall_r1a + wall_r1c

    # =================================================================
    # RANK 4 -- SECOND, 38.4deg at corrected sigma, R3 family (4 calls, UNCONDITIONAL)
    # =================================================================
    print("\n" + "=" * 78)
    print(f"RANK 4 -- {RANK4_ANGLE}deg at corrected sigma ({SIGMA_R3_CORRECTED:.4f}), "
          f"R3 (cpl=30) family (4 calls, UNCONDITIONAL, independent of Rank 1's verdict)")
    print("=" * 78)

    jobs_r4 = []
    for key in PAIR_KEYS_R3:
        jobs_r4.append((key, RANK4_ANGLE, False, STEPS_R3, None))
        jobs_r4.append((key, RANK4_ANGLE, True, STEPS_R3, SIGMA_R3_CORRECTED))
    assert len(jobs_r4) == 4
    print(f"\n{len(jobs_r4)} FDTD calls queued (Rank 4) -- see module docstring disclosure "
          f"(iv): both legs spent fresh, cross-process reuse limited to a pulled scalar "
          f"comparator (exp-094's own already-filed native-sigma Rank-3 38.4deg reading)")
    captures_r4, wall_r4 = run_block(jobs_r4)
    print(f"Rank 4 wall time: {wall_r4:.1f}s ({wall_r4 / 60.0:.2f} min)")

    cells_r4 = {}
    for key in PAIR_KEYS_R3:
        cap_empty = captures_r4[(key, RANK4_ANGLE, False, STEPS_R3)]
        cap_article = captures_r4[(key, RANK4_ANGLE, True, STEPS_R3)]
        cell = cell_metrics_full(key, RANK4_ANGLE, STEPS_R3, cap_empty, cap_article)
        cells_r4[key] = cell
        for xi in cell["xi_ext"].values():
            if xi > XI_TOL:
                xi_pass = False
        if not cell["sigma_abs_nonneg"]:
            nonneg_pass = False
    print(f"\n[Rank 4] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 4 FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 4] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 4 FAILED -- non-negativity gate; HALT"

    pm_r4 = pair_metrics_full(cells_r4["C40_R3"], cells_r4["G40_R3"], floor)

    # native-sigma comparator, independently re-pulled from exp-094's own committed
    # results.json (NOT hand-typed).
    with open(EXP094_RESULTS) as f:
        j094 = json.load(f)
    native_r4 = j094["rank3"]["per_theta"][str(RANK4_ANGLE)]
    y_native_r4 = native_r4["y_cpl30"]
    y_r4 = 1 if (pm_r4["floor_pass"] and pm_r4["ratio_k"] > RATIO_HIGH) else (0 if pm_r4["floor_pass"] else None)
    if not pm_r4["floor_pass"]:
        rank4_verdict = "NEITHER"
    elif y_r4 == y_native_r4 == 1:
        rank4_verdict = "CONFIRM"
    elif y_r4 == 0:
        rank4_verdict = "REFUTE"
    else:
        rank4_verdict = "NEITHER"
    print(f"\n[Rank 4] native-sigma (0.5) comparator, exp-094's own filed 38.4deg Rank-3 reading: "
          f"ratio_k={native_r4['ratio_k']:.4f}  floor_pass={native_r4['floor_pass']}  Y={y_native_r4}")
    print(f"[Rank 4] corrected-sigma ({SIGMA_R3_CORRECTED:.4f}), this cycle: "
          f"delta_scene={pm_r4['delta_scene']:+.6e}  frac_contrast={pm_r4['frac_contrast']:.6e}  "
          f"ratio_k={pm_r4['ratio_k']:.4f}  floor_pass={pm_r4['floor_pass']}  Y={y_r4}")
    print(f"\n[Rank 4 PRIMARY] VERDICT={rank4_verdict}  (no confident lean pre-committed -- "
          f"38.4deg's own native-sigma-only premise self-falsified per exp-094's Idealization 21 finding)")

    netd_row_r4 = netd_row(pm_r4)

    total_fdtd_wall_rank4 = wall_r4

    # =================================================================
    # RANK 2 / RANK 3 -- gated on Rank 1's combined go/no-go
    # =================================================================
    if not proceed_gate:
        print("\n" + "=" * 78)
        print("RANK 2 / RANK 3 -- SKIPPED (Rank 1 combined gate did not PROCEED)")
        print("=" * 78)
        rank2a_verdict = rank2b_outcome = rank3a_verdict = rank3b_verdict = "NOT RUN (Rank 1 gate)"
        rank2 = dict(skipped=True, reason="Rank 1 combined go/no-go gate did not PROCEED")
        rank3 = dict(skipped=True, reason="Rank 1 combined go/no-go gate did not PROCEED")
        total_fdtd_wall_rank2 = 0.0
        total_fdtd_wall_rank3 = 0.0
    else:
        # =============================================================
        # RANK 2 -- THIRD, R5 (cpl=50) family, gated on Rank 1 PROCEED (36 calls)
        # =============================================================
        print("\n" + "=" * 78)
        print("RANK 2 -- R5 (cpl=50) family, gated on Rank 1 PROCEED (36 calls)")
        print("=" * 78)

        # -------- Rank 2a: settling precondition --------
        print(f"\n[Rank 2a] settling precondition @ {RANK2A_ANGLE}deg "
              f"(sigma_max={SIGMA_R5_CORRECTED} corrected, STEPS in "
              f"{{{dg.R5_STEPS},{dg.R5_STEPS_STRESS}}})")

        jobs_r2a = []
        for steps in (dg.R5_STEPS, dg.R5_STEPS_STRESS):
            for key in PAIR_KEYS_R5:
                jobs_r2a.append((key, RANK2A_ANGLE, False, steps, None))
                jobs_r2a.append((key, RANK2A_ANGLE, True, steps, SIGMA_R5_CORRECTED))
        assert len(jobs_r2a) == 8
        print(f"{len(jobs_r2a)} FDTD calls queued (Rank 2a) -- Gate 5 fires inline on each "
              f"article call, before its own FDTD step")
        captures_r2a, wall_r2a = run_block_r5(jobs_r2a)
        print(f"Rank 2a wall time: {wall_r2a:.1f}s ({wall_r2a / 60.0:.2f} min)")
        print("[Gate 5] all 4 Rank 2a article calls completed their inline runtime "
              "sigma_e/sigma_max assert without raising -- PASS")

        cells_r2a = {}
        for steps in (dg.R5_STEPS, dg.R5_STEPS_STRESS):
            for key in PAIR_KEYS_R5:
                cap_empty = captures_r2a[(key, RANK2A_ANGLE, False, steps)]
                cap_article = captures_r2a[(key, RANK2A_ANGLE, True, steps)]
                cell = cell_metrics_r5(key, RANK2A_ANGLE, steps, cap_empty, cap_article)
                cells_r2a[(key, steps)] = cell
                for xi in cell["xi_ext"].values():
                    if xi > XI_TOL:
                        xi_pass = False
                if not cell["sigma_abs_nonneg"]:
                    nonneg_pass = False
        print(f"[Rank 2a] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
        assert xi_pass, "Rank 2a FAILED -- extinction-routes disagreement; HALT"
        print(f"[Rank 2a] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
        assert nonneg_pass, "Rank 2a FAILED -- non-negativity gate; HALT"

        pm_r5_7000 = pair_metrics_full(cells_r2a[("C40_R5", dg.R5_STEPS)], cells_r2a[("G40_R5", dg.R5_STEPS)], floor)
        pm_r5_10500 = pair_metrics_full(cells_r2a[("C40_R5", dg.R5_STEPS_STRESS)], cells_r2a[("G40_R5", dg.R5_STEPS_STRESS)], floor)
        ds_7000, ds_10500 = pm_r5_7000["delta_scene"], pm_r5_10500["delta_scene"]
        rel_dev_r2a = abs(ds_10500 - ds_7000) / abs(ds_7000) if ds_7000 != 0 else float("inf")

        def settle_band(rel_dev):
            if rel_dev <= 1e-2:
                return "PASS"
            if rel_dev <= 1e-1:
                return "CAUTIONARY-PASS"
            return "HALT"

        rank2a_verdict = settle_band(rel_dev_r2a)
        print(f"\n[Rank 2a PRIMARY] delta_scene(STEPS={dg.R5_STEPS})={ds_7000:+.6e}  "
              f"delta_scene(STEPS={dg.R5_STEPS_STRESS})={ds_10500:+.6e}  "
              f"rel_dev={rel_dev_r2a:.4%}  VERDICT={rank2a_verdict}")

        # mandatory fix #8: p_abs_w settling band, informational, non-gating
        p_7000 = pm_r5_7000["p_c"]
        p_10500 = pm_r5_10500["p_c"]
        rel_dev_r2a_pabs = abs(p_10500 - p_7000) / abs(p_7000) if p_7000 != 0 else float("inf")
        rank2a_pabs_verdict = settle_band(rel_dev_r2a_pabs)
        print(f"[Rank 2a, informational, non-gating, mandatory fix #8] p_abs_w(C, STEPS={dg.R5_STEPS})={p_7000:.6e}  "
              f"p_abs_w(C, STEPS={dg.R5_STEPS_STRESS})={p_10500:.6e}  rel_dev={rel_dev_r2a_pabs:.4%}  "
              f"BAND={rank2a_pabs_verdict}  (informational only, never gates Rank 2b)")

        netd_row_r2a_7000 = netd_row(pm_r5_7000)
        netd_row_r2a_10500 = netd_row(pm_r5_10500)

        # -------- Rank 2b: interior sweep, gated on Rank 2a not HALTing --------
        print(f"\n[Rank 2b] interior sweep, R5 (cpl=50), {RANK2B_ANGLES}deg "
              f"(sigma_max={SIGMA_R5_CORRECTED} corrected, STEPS={dg.R5_STEPS}, gate={rank2a_verdict})")

        if rank2a_verdict == "HALT":
            print("\n[Rank 2b] SKIPPED -- Rank 2a fired HALT (rel_dev > 1e-1); "
                  "NOTES.md instructs not spending these 24 calls.")
            jobs_r2b = []
            jobs_r2b_native = []
            wall_r2b = 0.0
            wall_r2b_native = 0.0
            captures_r2b = {}
            rank2b_report = {}
            rank2b_outcome = "NOT RUN (Rank 2a HALT)"
            rank2b_native_report = {}
            rank2b_native_overall = "NOT RUN (Rank 2a HALT)"
            desk_bound_report = dict(triggered=False, reason="Rank 2b not run (Rank 2a HALT)")
        else:
            jobs_r2b = []
            for key in PAIR_KEYS_R5:
                for th in RANK2B_ANGLES:
                    jobs_r2b.append((key, th, False, dg.R5_STEPS, None))
                    jobs_r2b.append((key, th, True, dg.R5_STEPS, SIGMA_R5_CORRECTED))
            assert len(jobs_r2b) == 24
            print(f"{len(jobs_r2b)} FDTD calls queued (Rank 2b) -- Gate 5 fires inline on each "
                  f"article call, before its own FDTD step")
            captures_r2b, wall_r2b = run_block_r5(jobs_r2b)
            print(f"Rank 2b wall time: {wall_r2b:.1f}s ({wall_r2b / 60.0:.2f} min)")
            print("[Gate 5] all 12 Rank 2b article calls completed their inline runtime "
                  "sigma_e/sigma_max assert without raising -- PASS")

            cells_r2b = {}
            for key in PAIR_KEYS_R5:
                for th in RANK2B_ANGLES:
                    cap_empty = captures_r2b[(key, th, False, dg.R5_STEPS)]
                    cap_article = captures_r2b[(key, th, True, dg.R5_STEPS)]
                    cell = cell_metrics_r5(key, th, dg.R5_STEPS, cap_empty, cap_article)
                    cells_r2b[(key, th)] = cell
                    for xi in cell["xi_ext"].values():
                        if xi > XI_TOL:
                            xi_pass = False
                    if not cell["sigma_abs_nonneg"]:
                        nonneg_pass = False
            print(f"[Rank 2b] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
            assert xi_pass, "Rank 2b FAILED -- extinction-routes disagreement; HALT"
            print(f"[Rank 2b] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
            assert nonneg_pass, "Rank 2b FAILED -- non-negativity gate; HALT"

            rank2b_report = {}
            for th in RANK2B_ANGLES:
                c_cell = cells_r2b[("C40_R5", th)]
                g_cell = cells_r2b[("G40_R5", th)]
                pm = pair_metrics_full(c_cell, g_cell, floor)
                pg_pc_ratio = pm["p_g"] / pm["p_c"] if pm["p_c"] != 0 else float("inf")
                rank2b_report[th] = dict(
                    delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                    ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], resolved=pm["resolved"],
                    frac_p_abs=pm["frac_p_abs"], p_c=pm["p_c"], p_g=pm["p_g"], pg_pc_ratio=pg_pc_ratio,
                    classification=("NODE-UNRESOLVABLE" if not pm["floor_pass"] else classification_word(pm["ratio_k"])),
                    **netd_row(pm),
                )
            print("\n[Rank 2b PRIMARY] per-angle results:")
            for th, r in sorted(rank2b_report.items()):
                print(f"  theta={th}: delta_scene={r['delta_scene']:+.6e}  frac_contrast={r['frac_contrast']:.6e}  "
                      f"ratio_k={r['ratio_k']:.4f}  class={r['classification']}  floor_pass={r['floor_pass']}")

            any_confirmed_r2b = any(r["delta_scene"] > 0 and r["floor_pass"] for r in rank2b_report.values())
            all_nonpositive_r2b = all(r["delta_scene"] <= 0 for r in rank2b_report.values())
            if any_confirmed_r2b:
                rank2b_outcome = "TWO-NODE CONFIRMED"
            elif all_nonpositive_r2b:
                rank2b_outcome = "SINGLE-NULL"
            else:
                rank2b_outcome = "STILL AMBIGUOUS"
            print(f"\n[Rank 2b PRIMARY] THREE-WAY OUTCOME = {rank2b_outcome}")
            print(f"[Rank 2b PRIMARY, mandatory fix #4, non-buried disclosure] {R2B_NO_DISCHARGE_SENTENCE}")

            # -------- Rank 2b-native: native-sigma comparator leg (mandatory fix #3) --------
            print(f"\n[Rank 2b-native] native-sigma (0.5) comparator leg @ {RANK2B_NATIVE_ANGLES}deg "
                  f"(article-only, empty legs reused in-memory from Rank 2b -- see module docstring "
                  f"disclosure (v))")

            jobs_r2b_native = []
            for key in PAIR_KEYS_R5:
                for th in RANK2B_NATIVE_ANGLES:
                    jobs_r2b_native.append((key, th, True, dg.R5_STEPS, SIGMA_NATIVE))
            assert len(jobs_r2b_native) == 4
            print(f"{len(jobs_r2b_native)} FDTD calls queued (Rank 2b-native, article-only)")
            captures_r2b_native, wall_r2b_native = run_block_r5(jobs_r2b_native)
            print(f"Rank 2b-native wall time: {wall_r2b_native:.1f}s ({wall_r2b_native / 60.0:.2f} min)")

            cells_r2b_native = {}
            for key in PAIR_KEYS_R5:
                for th in RANK2B_NATIVE_ANGLES:
                    cap_empty = captures_r2b[(key, th, False, dg.R5_STEPS)]   # in-memory reuse (v)
                    cap_article = captures_r2b_native[(key, th, True, dg.R5_STEPS)]
                    cell = cell_metrics_r5(key, th, dg.R5_STEPS, cap_empty, cap_article)
                    cells_r2b_native[(key, th)] = cell
                    for xi in cell["xi_ext"].values():
                        if xi > XI_TOL:
                            xi_pass = False
                    if not cell["sigma_abs_nonneg"]:
                        nonneg_pass = False
            print(f"[Rank 2b-native] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
            assert xi_pass, "Rank 2b-native FAILED -- extinction-routes disagreement; HALT"
            print(f"[Rank 2b-native] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
            assert nonneg_pass, "Rank 2b-native FAILED -- non-negativity gate; HALT"

            rank2b_native_report = {}
            for th in RANK2B_NATIVE_ANGLES:
                c_cell = cells_r2b_native[("C40_R5", th)]
                g_cell = cells_r2b_native[("G40_R5", th)]
                pm = pair_metrics_full(c_cell, g_cell, floor)
                corrected = rank2b_report[th]
                sign_survives = (pm["delta_scene"] > 0) == (corrected["delta_scene"] > 0)
                class_survives = ("CONSISTENT" if pm["floor_pass"] and RATIO_LOW <= pm["ratio_k"] <= RATIO_HIGH
                                   else classification_word(pm["ratio_k"]) if pm["floor_pass"] else "NODE-UNRESOLVABLE") == corrected["classification"]
                leg_verdict = "CONFIRM" if (sign_survives and pm["floor_pass"]) else "REFUTE"
                rank2b_native_report[th] = dict(
                    delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                    ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
                    corrected_sigma_delta_scene=corrected["delta_scene"],
                    corrected_sigma_classification=corrected["classification"],
                    sign_survives=sign_survives, classification_survives=class_survives,
                    verdict=leg_verdict,
                    **netd_row(pm),
                )
            print("\n[Rank 2b-native PRIMARY] per-angle native-vs-corrected comparison:")
            for th, r in sorted(rank2b_native_report.items()):
                print(f"  theta={th}: native delta_scene={r['delta_scene']:+.6e}  "
                      f"corrected delta_scene={r['corrected_sigma_delta_scene']:+.6e}  "
                      f"sign_survives={r['sign_survives']}  VERDICT={r['verdict']}")

            rank2b_native_verdicts = [r["verdict"] for r in rank2b_native_report.values()]
            rank2b_native_overall = "CONFIRM" if all(v == "CONFIRM" for v in rank2b_native_verdicts) else "REFUTE"
            print(f"[Rank 2b-native PRIMARY] OVERALL VERDICT (both angles)={rank2b_native_overall}")

            # -------- mandatory fix #5: companion desk bound --------
            print("\n[Rank 2, mandatory fix #5] companion desk bound (radius-drift-scale check)")
            r5_diff_angles = []
            for th in RANK2B_ANGLES:
                r4_class = j094["rank1b"]["per_theta"][str(th)]["classification"]
                r5_class = rank2b_report[th]["classification"]
                if r4_class != r5_class:
                    r5_diff_angles.append(th)
            if not r5_diff_angles:
                desk_bound_report = dict(
                    triggered=False,
                    reason="not triggered -- no angle differs from exp-094's own cpl=40 classification")
                print("[Rank 2, mandatory fix #5] NOT TRIGGERED -- Rank 2b's own classification "
                      "matches exp-094's own filed cpl=40 classification at all six angles.")
            else:
                bound_rows = {}
                for th in r5_diff_angles:
                    ds_r4 = j094["rank1b"]["per_theta"][str(th)]["delta_scene"]
                    ds_r5 = rank2b_report[th]["delta_scene"]
                    observed_shift = abs(ds_r5 - ds_r4) / abs(ds_r4) if ds_r4 != 0 else float("inf")
                    radius_drift_bound = abs(175.5 - 176.0) / 176.0   # ~0.284%, Red Team's own cpl=45-scale figure
                    ratio_to_bound = observed_shift / radius_drift_bound if radius_drift_bound != 0 else float("inf")
                    bound_rows[th] = dict(observed_shift=observed_shift, radius_drift_bound=radius_drift_bound,
                                           ratio_to_bound=ratio_to_bound)
                    print(f"  theta={th}: observed cpl30->40->50 shift={observed_shift:.4%}  "
                          f"radius-drift-scale bound={radius_drift_bound:.4%}  ratio={ratio_to_bound:.1f}x")
                desk_bound_report = dict(triggered=True, diff_angles=r5_diff_angles, per_theta=bound_rows,
                                          note="Order-of-magnitude sanity check only (Idealization 29), not a "
                                               "rigorous alias-decomposition -- argues against, does not prove "
                                               "against, a pure radius-rounding origin for any reversal seen.")

            # -------- mandatory fix #6: cross-reference Rank 2b-native vs Rank 3b (deferred print below, after Rank 3b runs) --------

        # =============================================================
        # RANK 3 -- FOURTH, R4 (cpl=40) sigma-comparability, gated on Rank 1 PROCEED (30 calls, corrected count)
        # =============================================================
        print("\n" + "=" * 78)
        print("RANK 3 -- R4 (cpl=40) sigma-comparability, gated on Rank 1 PROCEED (30 calls, corrected count)")
        print("=" * 78)

        # -------- Rank 3a: 41.6deg, native+corrected sigma --------
        # NOTE: `run_block_r4`'s own captures dict is keyed (key,th,art,steps) -- sigma_max is
        # NOT part of that key. Two article legs at the SAME (key,th,steps) but DIFFERENT
        # sigma_max would silently collide (last-write-wins) if queued in a single
        # `run_block_r4` call. Split into two explicit sub-blocks instead -- mirrors
        # exp-093's own item5/item3 split (item5 computes the native leg; item3, a later,
        # separate `run_block` call, computes only the corrected leg and reuses item5's own
        # empty-leg captures in-memory) -- disambiguates cleanly, matches this program's own
        # established practice, zero call-count change (still 6 calls total).
        print(f"\n[Rank 3a] {RANK3A_ANGLE}deg, R4 (cpl=40), native (0.5) and corrected "
              f"({SIGMA_R4_CORRECTED}) sigma (6 calls, two sub-blocks to avoid a sigma-keying "
              f"collision in the shared captures dict)")

        jobs_r3a_native = []
        for key in PAIR_KEYS_R4:
            jobs_r3a_native.append((key, RANK3A_ANGLE, False, dg.R4_STEPS, None))
            jobs_r3a_native.append((key, RANK3A_ANGLE, True, dg.R4_STEPS, SIGMA_NATIVE))
        assert len(jobs_r3a_native) == 4
        print(f"{len(jobs_r3a_native)} FDTD calls queued (Rank 3a, native-sigma sub-block)")
        captures_r3a_native, wall_r3a_native = run_block_r4(jobs_r3a_native)
        print(f"Rank 3a native-sigma sub-block wall time: {wall_r3a_native:.1f}s "
              f"({wall_r3a_native / 60.0:.2f} min)")

        jobs_r3a_corrected = []
        for key in PAIR_KEYS_R4:
            jobs_r3a_corrected.append((key, RANK3A_ANGLE, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
        assert len(jobs_r3a_corrected) == 2
        print(f"{len(jobs_r3a_corrected)} FDTD calls queued (Rank 3a, corrected-sigma "
              f"sub-block, article-only, empty legs reused in-memory from the native sub-block)")
        captures_r3a_corrected, wall_r3a_corrected = run_block_r4(jobs_r3a_corrected)
        print(f"Rank 3a corrected-sigma sub-block wall time: {wall_r3a_corrected:.1f}s "
              f"({wall_r3a_corrected / 60.0:.2f} min)")
        wall_r3a = wall_r3a_native + wall_r3a_corrected

        cells_r3a_native = {}
        cells_r3a_corrected = {}
        for key in PAIR_KEYS_R4:
            cap_empty = captures_r3a_native[(key, RANK3A_ANGLE, False, dg.R4_STEPS)]
            cap_article_native = captures_r3a_native[(key, RANK3A_ANGLE, True, dg.R4_STEPS)]
            cap_article_corrected = captures_r3a_corrected[(key, RANK3A_ANGLE, True, dg.R4_STEPS)]
            cell_native = cell_metrics_r4(key, RANK3A_ANGLE, dg.R4_STEPS, cap_empty, cap_article_native)
            cell_corrected = cell_metrics_r4(key, RANK3A_ANGLE, dg.R4_STEPS, cap_empty, cap_article_corrected)
            cells_r3a_native[key] = cell_native
            cells_r3a_corrected[key] = cell_corrected
            for cell in (cell_native, cell_corrected):
                for xi in cell["xi_ext"].values():
                    if xi > XI_TOL:
                        xi_pass = False
                if not cell["sigma_abs_nonneg"]:
                    nonneg_pass = False
        print(f"\n[Rank 3a] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
        assert xi_pass, "Rank 3a FAILED -- extinction-routes disagreement; HALT"
        print(f"[Rank 3a] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
        assert nonneg_pass, "Rank 3a FAILED -- non-negativity gate; HALT"

        pm_r3a_native = pair_metrics_full(cells_r3a_native["C40_R4"], cells_r3a_native["G40_R4"], floor)
        pm_r3a_corrected = pair_metrics_full(cells_r3a_corrected["C40_R4"], cells_r3a_corrected["G40_R4"], floor)
        print(f"\n[Rank 3a] native (0.5): delta_scene={pm_r3a_native['delta_scene']:+.6e}  "
              f"frac_contrast={pm_r3a_native['frac_contrast']:.6e}  ratio_k={pm_r3a_native['ratio_k']:.4f}  "
              f"floor_pass={pm_r3a_native['floor_pass']}")
        print(f"[Rank 3a] corrected ({SIGMA_R4_CORRECTED}): delta_scene={pm_r3a_corrected['delta_scene']:+.6e}  "
              f"frac_contrast={pm_r3a_corrected['frac_contrast']:.6e}  ratio_k={pm_r3a_corrected['ratio_k']:.4f}  "
              f"floor_pass={pm_r3a_corrected['floor_pass']}")

        ds_ratio_r3a = (pm_r3a_corrected["delta_scene"] / pm_r3a_native["delta_scene"]
                        if pm_r3a_native["delta_scene"] != 0 else float("inf"))
        ds_sign_match_r3a = (pm_r3a_corrected["delta_scene"] > 0) == (pm_r3a_native["delta_scene"] > 0)
        fc_ratio_r3a = (pm_r3a_corrected["frac_contrast"] / pm_r3a_native["frac_contrast"]
                        if pm_r3a_native["frac_contrast"] != 0 else float("inf"))
        ds_verdict_r3a = ratio_sign_verdict([(ds_ratio_r3a, ds_sign_match_r3a)])
        fc_verdict_r3a = ratio_sign_verdict([(fc_ratio_r3a, True)])
        rank3a_verdict = min([ds_verdict_r3a, fc_verdict_r3a], key=lambda v: VERDICT_RANK[v])
        print(f"\n[Rank 3a PRIMARY] delta_scene ratio={ds_ratio_r3a:.4f} sign_match={ds_sign_match_r3a}  "
              f"sub-verdict={ds_verdict_r3a}  |  frac_contrast ratio={fc_ratio_r3a:.4f}  "
              f"sub-verdict={fc_verdict_r3a}  ||  OVERALL VERDICT={rank3a_verdict}  "
              f"(no confident directional lean pre-committed -- 41.6deg's own high ratio_k at "
              f"cpl=30-native sits in the same fragile, near-null-adjacent population as this "
              f"window's other sensitive points)")

        netd_row_r3a_native = netd_row(pm_r3a_native)
        netd_row_r3a_corrected = netd_row(pm_r3a_corrected)

        # -------- Rank 3b: confound-disentangling test, native-sigma at the six interior angles --------
        print(f"\n[Rank 3b] confound-disentangling test, R4 (cpl=40), native sigma (0.5), "
              f"{RANK3B_ANGLES}deg (24 calls -- see module docstring disclosure (iv): both legs "
              f"spent fresh, cross-process reuse limited to a pulled scalar comparator, "
              f"exp-094's own already-filed corrected-sigma Rank-1b reading)")

        jobs_r3b = []
        for key in PAIR_KEYS_R4:
            for th in RANK3B_ANGLES:
                jobs_r3b.append((key, th, False, dg.R4_STEPS, None))
                jobs_r3b.append((key, th, True, dg.R4_STEPS, SIGMA_NATIVE))
        assert len(jobs_r3b) == 24
        print(f"{len(jobs_r3b)} FDTD calls queued (Rank 3b)")
        captures_r3b, wall_r3b = run_block_r4(jobs_r3b)
        print(f"Rank 3b wall time: {wall_r3b:.1f}s ({wall_r3b / 60.0:.2f} min)")

        cells_r3b = {}
        for key in PAIR_KEYS_R4:
            for th in RANK3B_ANGLES:
                cap_empty = captures_r3b[(key, th, False, dg.R4_STEPS)]
                cap_article = captures_r3b[(key, th, True, dg.R4_STEPS)]
                cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)
                cells_r3b[(key, th)] = cell
                for xi in cell["xi_ext"].values():
                    if xi > XI_TOL:
                        xi_pass = False
                if not cell["sigma_abs_nonneg"]:
                    nonneg_pass = False
        print(f"\n[Rank 3b] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
        assert xi_pass, "Rank 3b FAILED -- extinction-routes disagreement; HALT"
        print(f"[Rank 3b] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
        assert nonneg_pass, "Rank 3b FAILED -- non-negativity gate; HALT"

        rank3b_report = {}
        for th in RANK3B_ANGLES:
            c_cell = cells_r3b[("C40_R4", th)]
            g_cell = cells_r3b[("G40_R4", th)]
            pm = pair_metrics_full(c_cell, g_cell, floor)
            corrected = j094["rank1b"]["per_theta"][str(th)]
            rank3b_report[th] = dict(
                delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
                classification=("NODE-UNRESOLVABLE" if not pm["floor_pass"] else classification_word(pm["ratio_k"])),
                corrected_sigma_delta_scene=corrected["delta_scene"],
                corrected_sigma_classification=corrected["classification"],
                **netd_row(pm),
            )
        print("\n[Rank 3b PRIMARY] per-angle native-sigma vs already-filed corrected-sigma:")
        for th, r in sorted(rank3b_report.items()):
            print(f"  theta={th}: native delta_scene={r['delta_scene']:+.6e}  class={r['classification']}  "
                  f"corrected(filed) delta_scene={r['corrected_sigma_delta_scene']:+.6e}  "
                  f"class(filed)={r['corrected_sigma_classification']}")

        n_positive_consistent = sum(1 for r in rank3b_report.values()
                                     if r["delta_scene"] > 0 and r["classification"] == "CONSISTENT")
        n_negative_dominant = sum(1 for r in rank3b_report.values()
                                   if r["delta_scene"] < 0 and r["classification"] == "ENERGY-DOMINANT")
        if n_positive_consistent == 6:
            rank3b_verdict = "CONFIRM"
        elif n_negative_dominant >= 4:
            rank3b_verdict = "REFUTE"
        else:
            rank3b_verdict = "MIXED"
        print(f"\n[Rank 3b PRIMARY] all-6-positive/CONSISTENT count={n_positive_consistent}  "
              f"negative/ENERGY-DOMINANT count={n_negative_dominant}  VERDICT={rank3b_verdict}  "
              f"(no confident lean pre-committed -- this test exists precisely because exp-094's "
              f"own design confounded sigma choice and cpl=40 refinement and never separated them)")

        # -------- mandatory fix #6: explicit cross-reference, Rank 2b-native vs Rank 3b --------
        print("\n[Mandatory fix #6] cross-reference: Rank 2b-native (cpl=50) vs Rank 3b (cpl=40) "
              "-- the same open question (is the sigma correction, not resolution refinement, "
              "the dominant driver of this window's reversals?) asked at two resolutions")
        r2b_native_says_robust = (rank2b_native_overall == "CONFIRM") if rank2b_native_overall in ("CONFIRM", "REFUTE") else None
        r3b_says_robust = (rank3b_verdict == "CONFIRM") if rank3b_verdict in ("CONFIRM", "REFUTE") else None
        if r2b_native_says_robust is None or r3b_says_robust is None:
            cross_reference_verdict = "NOT COMPARABLE (one or both items not run, or MIXED/inconclusive)"
        elif r2b_native_says_robust == r3b_says_robust:
            cross_reference_verdict = "AGREE"
        else:
            cross_reference_verdict = "DISAGREE"
        print(f"[Mandatory fix #6] Rank 2b-native says sigma-robust (CONFIRM)={r2b_native_says_robust}  "
              f"Rank 3b says sigma-robust (CONFIRM)={r3b_says_robust}  CROSS-REFERENCE={cross_reference_verdict}")

        total_fdtd_wall_rank2 = wall_r2a + wall_r2b + wall_r2b_native
        total_fdtd_wall_rank3 = wall_r3a + wall_r3b

        rank2 = dict(
            skipped=False,
            rank2a=dict(
                angle=RANK2A_ANGLE, steps=[dg.R5_STEPS, dg.R5_STEPS_STRESS],
                delta_scene_7000=ds_7000, delta_scene_10500=ds_10500, rel_dev=rel_dev_r2a,
                verdict=rank2a_verdict,
                p_abs_w_7000=p_7000, p_abs_w_10500=p_10500, rel_dev_p_abs_w=rel_dev_r2a_pabs,
                p_abs_w_band_informational=rank2a_pabs_verdict,
                netd_row_7000=netd_row_r2a_7000, netd_row_10500=netd_row_r2a_10500,
            ),
            rank2b=dict(
                angles=RANK2B_ANGLES, gate=rank2a_verdict,
                per_theta={str(k): v for k, v in rank2b_report.items()},
                outcome=rank2b_outcome,
                no_discharge_disclosure=R2B_NO_DISCHARGE_SENTENCE,
            ),
            rank2b_native=dict(
                angles=RANK2B_NATIVE_ANGLES,
                per_theta={str(k): v for k, v in rank2b_native_report.items()},
                overall_verdict=rank2b_native_overall,
            ),
            desk_bound_mandatory_fix_5=desk_bound_report,
            cross_reference_mandatory_fix_6=dict(
                rank2b_native_says_robust=r2b_native_says_robust,
                rank3b_says_robust=r3b_says_robust,
                verdict=cross_reference_verdict,
            ),
        )
        rank3 = dict(
            skipped=False,
            rank3a=dict(
                angle=RANK3A_ANGLE, verdict=rank3a_verdict,
                delta_scene_sub_verdict=ds_verdict_r3a, frac_contrast_sub_verdict=fc_verdict_r3a,
                native=dict(delta_scene=pm_r3a_native["delta_scene"], frac_contrast=pm_r3a_native["frac_contrast"],
                            ratio_k=pm_r3a_native["ratio_k"], floor_pass=pm_r3a_native["floor_pass"],
                            **netd_row_r3a_native),
                corrected=dict(delta_scene=pm_r3a_corrected["delta_scene"], frac_contrast=pm_r3a_corrected["frac_contrast"],
                               ratio_k=pm_r3a_corrected["ratio_k"], floor_pass=pm_r3a_corrected["floor_pass"],
                               **netd_row_r3a_corrected),
                delta_scene_ratio=ds_ratio_r3a, frac_contrast_ratio=fc_ratio_r3a,
            ),
            rank3b=dict(angles=RANK3B_ANGLES, verdict=rank3b_verdict,
                        per_theta={str(k): v for k, v in rank3b_report.items()}),
        )

    total_wall_all = time.time() - t_start

    # ---------------------------------------------------------------- disclosures (printed AND persisted)
    # `j094` was already loaded unconditionally in the Rank 4 block above (Rank 4 runs
    # regardless of proceed_gate, so this is always available here).
    netd_disclaimer = j094["netd_disclaimer"]
    scope_note = ("This cycle is pure instrument recalibration (T1 route N/A, Checkpoint "
                  "criterion 2 N/A) -- no phenomenon-mechanism claim, REALIZABILITY_MEMO.md "
                  "untouched. (Idealization 7)")
    r4_r5_family_disclaimer = (
        "Idealization 17: the R3/R4/R5 (cpl=30/40/50) geometry families are a single "
        "mechanical, zero-design-freedom construction recipe (r{n}_config()) applied at "
        "three ratios drawn from the same admissible set {1.5,2.0,2.5,...} -- not three "
        "independent re-derivations of the discretization scheme. If the recipe carries any "
        "undetected systematic bias, all three families inherit it unchanged. " + R2B_NO_DISCHARGE_SENTENCE
    )
    call_count_disclosure = (
        "Disclosed spec-resolution note (module docstring disclosure (iv), NOTES.md's own "
        "'Disclosed spec-resolution note' section): Rank 3b and Rank 4's own call counts are "
        "24 and 4 respectively (not the Phase-1/Red-Team-stated 12 and 2) -- both legs are "
        "spent fresh for the new sigma-branch reading in each item; only the OLD/comparator "
        "side (already-filed scalar metrics, zero new calls) is genuinely reused, mirroring "
        "exp-094's own Rank 2 precedent. PASS-path total is 86 calls (16+36+30+4), not the "
        "originally-stated 72; FAIL-path total is 20 (16+4), not 18. Angles/sigma choices/"
        "gating logic/outcome taxonomy are unaffected."
    )
    print(f"\n[disclosure] netd_disclaimer: {netd_disclaimer}")
    print(f"[disclosure] scope_note: {scope_note}")
    print(f"[disclosure] r4_r5_family_disclaimer: {r4_r5_family_disclaimer}")
    print(f"[disclosure] call_count_disclosure: {call_count_disclosure}")

    # ---------------------------------------------------------------- persist
    rank1_calls = len(jobs_r1a) + len(jobs_r1c)
    rank4_calls = len(jobs_r4)
    if proceed_gate:
        rank2_calls = len(jobs_r2a) + len(jobs_r2b) + len(jobs_r2b_native)
        rank3_calls = len(jobs_r3a_native) + len(jobs_r3a_corrected) + len(jobs_r3b)
    else:
        rank2_calls = 0
        rank3_calls = 0
    total_fdtd_calls = rank1_calls + rank4_calls + rank2_calls + rank3_calls

    out = dict(
        total_fdtd_calls=total_fdtd_calls,
        rank1_calls=rank1_calls, rank4_calls=rank4_calls,
        rank2_calls=rank2_calls, rank3_calls=rank3_calls,
        proceed_gate=proceed_gate,
        rank1a_wall_s=wall_r1a, rank1c_wall_s=wall_r1c, rank4_wall_s=wall_r4,
        rank2_wall_s=(total_fdtd_wall_rank2 if proceed_gate else 0.0),
        rank3_wall_s=(total_fdtd_wall_rank3 if proceed_gate else 0.0),
        total_fdtd_wall_time_s=total_fdtd_wall_rank1 + total_fdtd_wall_rank4 +
            ((total_fdtd_wall_rank2 + total_fdtd_wall_rank3) if proceed_gate else 0.0),
        total_wall_time_s=total_wall_all,
        sigma_native=SIGMA_NATIVE, sigma_r3_corrected=SIGMA_R3_CORRECTED,
        sigma_r4_corrected=SIGMA_R4_CORRECTED, sigma_r5_corrected=SIGMA_R5_CORRECTED,
        r13_floor_gate=dict(floor=floor, rms_frac_contrast=rms, n_window_points=n83),
        gates=dict(
            gate1_vacuum_footprint_r5=dict(report=vac_report, pass_=vac_pass),
            gate2_a_congruence=dict(a_c40_r5=a_c40, a_g40_r5=a_g40, pass_=gate2_pass),
            gate3_l_geometric_bit_identity=dict(
                l_geometric_m_r5=L_GEOMETRIC_M_R5, l_geometric_m=L_GEOMETRIC_M,
                l_geometric_m_r3=L_GEOMETRIC_M_R3, l_geometric_m_r4=L_GEOMETRIC_M_R4,
                dev_native=gate3_dev_native, dev_r3=gate3_dev_r3, dev_r4=gate3_dev_r4,
                pass_=gate3_pass),
            gate4_sigma_r5_corrected=dict(value=SIGMA_R5_CORRECTED, pass_=gate4_pass),
            gate5_runtime_sigma_array=dict(
                pass_=True,
                n_article_calls_checked=(8 if not proceed_gate else 8 + 4 + 12 + 4),
                note=("Wired inline in _run_sim_r5_sigma: "
                      "np.isclose(sim.sigma_e[shell_mask].max(), sigma_max, atol=1e-9), "
                      "shell_mask=(PEC_R_R5<=rr<=R5_R_OUT) on the ez-point grid centered "
                      "at (obj_x,obj_y). Also fires (R4 variant) on every Rank 1a/1c article "
                      "call regardless of gate outcome. An AssertionError in any worker would "
                      "have propagated and stopped this script before results.json was ever "
                      "written."),
            ),
            gate6_documentation_only=dict(lhs=gate6_lhs, rhs=gate6_rhs, dev=gate6_dev, pass_=gate6_pass),
        ),
        xi_pass=xi_pass, nonneg_pass=nonneg_pass,
        rank1=dict(
            rank1a=dict(angles=RANK1A_ANGLES, verdict=rank1a_verdict,
                        per_theta={str(k): v for k, v in rank1a_report.items()}),
            rank1c=dict(angles=RANK1C_ANGLES, verdict=rank1c_verdict, theta0=theta0_38590,
                        per_theta={str(k): v for k, v in rank1c_report.items()}),
            proceed_gate=proceed_gate,
        ),
        rank4=dict(
            angle=RANK4_ANGLE, verdict=rank4_verdict,
            corrected=dict(delta_scene=pm_r4["delta_scene"], frac_contrast=pm_r4["frac_contrast"],
                           ratio_k=pm_r4["ratio_k"], floor_pass=pm_r4["floor_pass"], y=y_r4,
                           **netd_row_r4),
            native_comparator=dict(ratio_k=native_r4["ratio_k"], floor_pass=native_r4["floor_pass"],
                                    y=y_native_r4),
        ),
        rank2=rank2,
        rank3=rank3,
        netd_disclaimer=netd_disclaimer,
        scope_note=scope_note,
        r4_r5_family_disclaimer=r4_r5_family_disclaimer,
        call_count_disclosure=call_count_disclosure,
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  Rank 1a (sign check, 39.2/39.4deg):     {rank1a_verdict}")
    print(f"  Rank 1c (node bracket, 38.49/38.69deg): {rank1c_verdict}")
    print(f"  RANK 1 COMBINED GO/NO-GO:               PROCEED={proceed_gate}")
    print(f"  Rank 4 (38.4deg corrected sigma):       {rank4_verdict}")
    if proceed_gate:
        print(f"  Rank 2a (R5 settling):                  {rank2a_verdict}")
        print(f"  Rank 2b (R5 interior three-way):        {rank2b_outcome}")
        print(f"  Rank 2b-native (sigma comparator):      {rank2b_native_overall}")
        print(f"  Rank 3a (41.6deg sigma-comparability):  {rank3a_verdict}")
        print(f"  Rank 3b (cpl=40 disentangling):         {rank3b_verdict}")
        print(f"  Cross-reference (mandatory fix #6):     {cross_reference_verdict}")
    else:
        print("  Rank 2/Rank 3: SKIPPED (Rank 1 gate did not PROCEED)")
    print(f"  total FDTD calls: {out['total_fdtd_calls']}   total wall time: "
          f"{total_wall_all:.1f}s ({total_wall_all / 60.0:.2f} min)")

    return out


if __name__ == "__main__":
    main()
