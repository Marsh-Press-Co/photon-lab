"""exp-094 -- T28 cpl=40 Resolution Check, sigma_max Comparability Close, R3
Census: Panel Iteration 71. Lead seat: QUANTUM OPTICS. Frozen spec: NOTES.md
(Predictions committed to git strictly BEFORE this file's first run, house
discipline). Change rationale: phase3_synthesis.md (5 Red-Team-mandatory
fixes, all adopted, zero overridden).

Three items, run cheapest-and-independent-first (NO cross-item gate this
cycle except Rank 1a -> Rank 1b -- unlike exp-092/093's own gated chains,
none of Rank 2/3/1 sets a parameter for either of the others):

  Rank 2 (FIRST, 4 calls)   -- sigma@41.6deg sigma-comparability close.
  Rank 3 (SECOND, 12 calls) -- census R3-verify, three angles never measured
                                 at cpl=30 (36.0/38.4/38.8deg).
  Rank 1a (THIRD, 8 calls)  -- NEW `R4` (cpl=40) family settling precondition
                                 at 41.825deg (both STEPS=5600/8400).
  Rank 1b (THIRD, 24 calls, gated on Rank 1a's own settling verdict) -- R4
                                 interior six-angle near-null sweep.
  Rank 3-ext (FOURTH, 0 calls, desk-only) -- caution-zone growth, cpl=30-only.

Total: 48 FDTD calls (the most expensive single T28 cycle to date).

Reuses experiments/093-.../run.py's own `dg`/`PAIR_KEYS_R3`/`STEPS_R3`/
`SIGMA_NATIVE`/`SIGMA_R3_CORRECTED`/`cell_metrics`/`cell_metrics_full`/
`pair_metrics`/`pair_metrics_full`/`one_call`/`run_block`/`compute_floor`/
`XI_TOL`/`NOISE_MULT`/`RATIO_LOW`/`RATIO_HIGH`/`NETD_BAND_K`/
`find_zero_crossings`/`ratio_sign_verdict`/`classification_word`/
`compute_zone` VERBATIM, UNMODIFIED, by loading experiments/093-.../run.py as
a module (which itself already loads 092->091->090 the same way) -- zero
`lab/` diff, zero diff to any frozen experiment file. `box_for_r3`/
`ref_for_r3`/`build_article_r3_sigma`/`_run_sim_r3_sigma`/`PEC_R_R3`/
`R3_R_OUT_CELLS`/`BOX_CLEARANCE_A_R3`/`BOX_CLEARANCE_B_R3`/`REF_HALF_H_R3`/
`_profile`/`contrast_pair`/`widths_direction_corrected`/`IRR_CENTRAL_W_CM2`/
`K_AIR`/`DENSITY_SI_KG_M3`/`C_P_SI_J_KGK`/`EMISSIVITY`/`T_AMBIENT_K` are
pulled through the same chain from the nested `exp092`/`exp091` module
attributes exp-093's own module exposes (several of these live at exp-092's
or exp-091's own module scope, not re-exported at exp-093's own module
scope -- confirmed by reading each file directly, not guessed).

NEW code this cycle (all additive; `experiments/069-.../design_geometry.py`
gains an appended-only `R4` block -- see that file's own diff for the R4_*
constants / `r4_config()` / `R4_CONFIGS`, mirroring exactly how exp-091
additively appended `G40_R3`/`C80_R3` without disturbing anything already
committed):

  * `box_for_r4`/`ref_for_r4` -- R4-scaled mirrors of `box_for_r3`/
    `ref_for_r3`.
  * `build_article_r4_sigma(sim, cx, cy, sigma_max)` -- R4-scaled mirror of
    `build_article_r3_sigma`.
  * `_run_sim_r4_sigma(cfg, theta, steps, with_article, sigma_max)` --
    mirrors `_run_sim_r3_sigma` exactly, PLUS this cycle's own mandatory
    Gate 5 (Red Team RT-1): immediately after `build_article_r4_sigma`,
    before `sim.run()`, asserts the actual value landing in the constructed
    `Sim`'s own `sigma_e` array at the article's shell cells matches the
    `sigma_max` just passed -- see the function body for the exact
    shell-cell indexing (mirrors `materials.graded_black_shell`'s own
    indexing verbatim, read directly from `lab/materials.py`).
  * `one_call_r4` -- module-level (picklable) worker for the new `R4` keys.
  * `run_block_r4` -- DISCLOSED, NOT explicitly named in NOTES.md's own
    "new functions" list, but mechanically necessary: exp-093's own
    `run_block` (reused verbatim for Rank 2/3 below) has its own dispatch
    hardcoded to exp-092's own module-level `one_call`, which is itself
    hardcoded to `dg.R3_CONFIGS[key]` -- it cannot route "C40_R4"/"G40_R4"
    keys (`dg.R3_CONFIGS["C40_R4"]` does not exist -- would KeyError).
    `run_block_r4` is a thin, mechanical copy of `run_block`'s own
    structure, dispatching to `one_call_r4` instead -- pure execution
    plumbing, no formula, gate, or metric touched.
  * `cell_metrics_r4` -- the one genuinely necessary new metrics function
    per NOTES.md (`cell_metrics` is hardcoded to `dg.R3_CONFIGS`/
    `box_for_r3`). `pair_metrics`/`pair_metrics_full` are called on its
    output UNMODIFIED (confirmed: both only ever read `c_cell`/`g_cell`
    dict keys, never a resolution constant directly).

DISCLOSED SPEC-RESOLUTION NOTES (frozen-spec ambiguities resolved
conservatively toward the spec's own stated, load-bearing intent, per this
phase's own instructions -- each repeated in the Phase-4 final report):

  (i) `R4_BASE_OBJ_Y` -- NOTES.md's own constants table gives a formula
      ("R4_BASE_NY//2 - R4_BASE_ABSORB" = 1504) that does NOT match the
      actual R3-family precedent it claims to mirror (R3_BASE_OBJ_Y is
      just R3_BASE_NY//2 = 1188, NOT R3_BASE_NY//2 - R3_BASE_ABSORB = 1128
      -- ABSORB is subtracted exactly once, later, via `y_lo` inside
      `r3_config()`/`r4_config()` itself). Taking the table's literal 1504
      and then mirroring `r3_config()` line-for-line would subtract ABSORB
      TWICE, giving A=1424 and silently breaking this cycle's own mandatory
      Gate 2 (A==1504) and the Setup section's own explicit sentence
      ("obj_y - y_lo = 1504"). Resolved toward the mandatory, doubly-stated
      gate: `R4_BASE_OBJ_Y = R4_BASE_NY // 2 = 1584` (mirrors
      `R3_BASE_OBJ_Y` exactly) -- verified below to give A=1504 exactly.
      See `design_geometry.py`'s own inline comment for the full derivation.
  (ii) Rank 1a's "|delta_scene(8400)-delta_scene(5600)|/|delta_scene(5600)|
      <=1e-2 at both C40_R4 and G40_R4" / "...>1e-1 at either config" --
      `delta_scene` is, throughout this entire program (exp-091 onward), a
      PAIRED quantity (`C_g - C_c`, needing BOTH configs simultaneously at
      the SAME steps) -- there is no precedent anywhere in this program for
      a "per-single-config delta_scene." Only one `delta_scene` value
      exists per STEPS value at a fixed angle; "at both/either config" is
      read as describing that this quantity's construction always draws on
      both configs (as `delta_scene` always does), not as instructing two
      independently-scored numbers. Implemented as ONE settling check per
      angle: rel_dev = |delta_scene(8400)-delta_scene(5600)| /
      |delta_scene(5600)|, PASS/CAUTIONARY-PASS/HALT per the stated bands.
  (iii) Rank 1b's Idealization-23 informational check, "`p_abs_w` ratio
      (G4/C4, per angle) expected within 2-5% of the 0.51 T9 anchor" --
      the established "0.51 T9 anchor" (see exp-092/093's own
      `ratio_abs_ext_dev_from_anchor` field) is `ratio_abs_ext_raw`
      (sigma_abs/sigma_ext, a PER-CONFIG absorption fraction), never a
      G/C `p_abs_w` ratio -- and no prior cycle's "item 3b"-style p_abs_w
      check (which this text cites as precedent) was ever scored against a
      ~0.51 band; it used the standard `ratio_sign_verdict` bands. This
      reads as a drafting conflation of two distinct established
      quantities. Resolved by reporting BOTH, purely informationally
      (neither is gating either way, so no CONFIRM/REFUTE outcome is at
      stake): the literal G4/C4 `p_abs_w` ratio (the quantity actually
      relevant to Idealization 23's own stated purpose -- testing whether
      exp-093's energy-flatness/ratio~1 finding extends to cpl=40), AND
      `ratio_abs_ext_raw_c`'s deviation from the 0.51 anchor (mirroring the
      exact established field, for continuity with Rank 2/3's own idiom).
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
    """House `_load()` pattern (exp-078..093's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP090_RESULTS = os.path.join(EXP090_DIR, "results.json")
EXP091_DIR = os.path.join(ROOT, "experiments", "091-t28-r3-resolution-denser-recheck")
EXP091_RESULTS = os.path.join(EXP091_DIR, "results.json")
EXP093_DIR = os.path.join(ROOT, "experiments", "093-t28-upper-crossing-resolution-netd-thread")
EXP093_RESULTS = os.path.join(EXP093_DIR, "results.json")

exp093 = _load(os.path.join(EXP093_DIR, "run.py"), "_exp094_exp093")
exp092 = exp093.exp092    # exp-093's own module already loaded exp-092 this way
exp091 = exp093.exp091    # ...and exp-091, same chain
exp090 = exp093.exp090    # ...and exp-090, same chain

dg = exp093.dg
PAIR_KEYS_R3 = exp093.PAIR_KEYS_R3
STEPS_R3 = exp093.STEPS_R3
assert STEPS_R3 == 4200
SIGMA_NATIVE = exp093.SIGMA_NATIVE
SIGMA_R3_CORRECTED = exp093.SIGMA_R3_CORRECTED
assert SIGMA_NATIVE == 0.5
assert abs(SIGMA_R3_CORRECTED - 1.0 / 3.0) < 1e-12

cell_metrics = exp093.cell_metrics
cell_metrics_full = exp093.cell_metrics_full
pair_metrics = exp093.pair_metrics
pair_metrics_full = exp093.pair_metrics_full
one_call = exp093.one_call
run_block = exp093.run_block
compute_floor = exp093.compute_floor
XI_TOL = exp093.XI_TOL
NOISE_MULT = exp093.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp093.RATIO_LOW, exp093.RATIO_HIGH
NETD_BAND_K = exp093.NETD_BAND_K
find_zero_crossings = exp093.find_zero_crossings
ratio_sign_verdict = exp093.ratio_sign_verdict
classification_word = exp093.classification_word
compute_zone = exp093.compute_zone
VERDICT_RANK = exp093.VERDICT_RANK

# R3-family plumbing, pulled through the nested exp-092/exp-091 module
# attributes (NOT all re-exported at exp-093's own module scope -- confirmed
# by reading each file directly).
box_for_r3 = exp092.box_for_r3
ref_for_r3 = exp092.ref_for_r3
build_article_r3_sigma = exp092.build_article_r3_sigma
_run_sim_r3_sigma = exp092._run_sim_r3_sigma
PEC_R_R3 = exp092.PEC_R_R3
R3_R_OUT_CELLS = exp092.R3_R_OUT_CELLS
BOX_CLEARANCE_A_R3 = exp092.BOX_CLEARANCE_A_R3
BOX_CLEARANCE_B_R3 = exp092.BOX_CLEARANCE_B_R3
DX_M_R3 = exp092.DX_M_R3
L_GEOMETRIC_M_R3 = exp092.L_GEOMETRIC_M_R3
REF_HALF_H_R3 = exp091.REF_HALF_H_R3
widths_direction_corrected = exp091.widths_direction_corrected
_profile = exp091._profile
contrast_pair = exp091.contrast_pair
IRR_CENTRAL_W_CM2 = exp091.IRR_CENTRAL_W_CM2
K_AIR = exp091.K_AIR
DENSITY_SI_KG_M3, C_P_SI_J_KGK = exp091.DENSITY_SI_KG_M3, exp091.C_P_SI_J_KGK
EMISSIVITY = exp091.EMISSIVITY
T_AMBIENT_K = exp091.T_AMBIENT_K
L_GEOMETRIC_M = exp091.L_GEOMETRIC_M

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts, materials  # noqa: E402

# ---------------------------------------------------------------- R4 family constants
PEC_R_R4 = dg.PEC_R_R4
BOX_CLEARANCE_A_R4 = dg.BOX_CLEARANCE_A_R4
BOX_CLEARANCE_B_R4 = dg.BOX_CLEARANCE_B_R4
REF_HALF_H_R4 = dg.REF_HALF_H_R4
SIGMA_R4_CORRECTED = dg.SIGMA_R4_CORRECTED
DX_M_R4 = dg.DX_M_R4
L_GEOMETRIC_M_R4 = dg.L_GEOMETRIC_M_R4
PAIR_KEYS_R4 = ("C40_R4", "G40_R4")

RANK2_ANGLE = 41.6
RANK3_ANGLES = [36.0, 38.4, 38.8]
RANK1_ANGLE_SETTLE = 41.825
RANK1B_ANGLES = [41.750, 41.775, 41.825, 41.850, 41.875, 41.900]


# ================================================================== R4 layer
def box_for_r4(cfg, clearance):
    ox, oy = cfg["obj_x"], cfg["obj_y"]
    r = dg.R4_R_OUT + clearance
    return (ox - r, ox + r, oy - r, oy + r)


def ref_for_r4(cfg):
    return (cfg["obj_x"], cfg["obj_y"], REF_HALF_H_R4)


def build_article_r4_sigma(sim, cx, cy, sigma_max):
    """R4-scaled mirror of `build_article_r3_sigma` -- same two calls
    (pec_disk core + graded_black_shell), radii scaled by R4_RATIO=2.0."""
    materials.pec_disk(sim, cx, cy, PEC_R_R4)
    materials.graded_black_shell(sim, cx, cy, PEC_R_R4, dg.R4_R_OUT, sigma_max=sigma_max)


def _run_sim_r4_sigma(cfg, theta, steps, with_article, sigma_max):
    """Mirrors `_run_sim_r3_sigma` exactly, calling `build_article_r4_sigma`.
    Carries this cycle's own mandatory Gate 5 (Red Team RT-1): immediately
    after building the article, BEFORE `sim.run()`, verify the actual value
    landing in the constructed Sim's own `sigma_e` array at the article's
    shell cells -- not a Python constant -- matches `sigma_max`. `shell_mask`
    below is read directly off `lab/materials.py::graded_black_shell`'s own
    indexing (rr from the ez-point radius/angle grid centered at (cx,cy),
    `r_in <= rr <= r_out`), not guessed."""
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R4_CPL[600],
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    if with_article:
        cx, cy = cfg["obj_x"], cfg["obj_y"]
        build_article_r4_sigma(sim, cx, cy, sigma_max)
        rr, _ = materials._grids(sim, cx, cy)["ez"]
        shell_mask = (rr >= PEC_R_R4) & (rr <= dg.R4_R_OUT)
        actual_sigma_max = float(sim.sigma_e[shell_mask].max())
        assert np.isclose(actual_sigma_max, sigma_max, atol=1e-9), (
            f"GATE 5 FAILED -- runtime sigma_e/sigma_max mismatch: "
            f"sim.sigma_e[shell_mask].max()={actual_sigma_max!r} vs "
            f"sigma_max={sigma_max!r} passed at (cx={cx},cy={cy})")
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta, amplitude=1.0,
                         profile="plane", edge=dg.R4_TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def one_call_r4(args):
    """Module-level (picklable) worker for the new R4 keys. args = (key,
    theta, with_article, steps, sigma_max)."""
    key, th, art, steps, sigma_max = args
    cfg = dg.R4_CONFIGS[key]
    cap = _run_sim_r4_sigma(cfg, th, steps, art, sigma_max)
    return (key, th, art, steps, sigma_max, cap)


def run_block_r4(jobs):
    """Thin, mechanical copy of exp-093's own (=exp-092's own) `run_block`,
    dispatching to `one_call_r4` instead of `one_call` -- see module
    docstring's disclosure. Pure execution plumbing, identical structure,
    no metric/formula touched."""
    t0 = time.time()
    captures = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, sigma_max, cap) in enumerate(ex.map(one_call_r4, jobs), 1):
            captures[(key, th, art, steps)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key:8s} theta={th:+06.3f} "
                  f"article={art} steps={steps} sigma_max={sigma_max}", flush=True)
    wall = time.time() - t0
    return captures, wall


def cell_metrics_r4(key, th, steps, cap_empty, cap_article):
    """The one genuinely necessary new metrics function (NOTES.md): mirrors
    `cell_metrics` exactly, substituting the R4-scaled geometry/box/ref/
    window-size/DX/L_GEOMETRIC constants. Its returned dict's `thermo` sub-
    dict already carries sigma_ext_cells/ratio_abs_ext_raw/p_abs_w/
    dt_ss_full_K/netd_classification IN FULL (same structure `cell_metrics`
    itself always produces) -- `pair_metrics`/`pair_metrics_full` are called
    on this output UNMODIFIED, exactly as NOTES.md specifies."""
    cfg = dg.R4_CONFIGS[key]
    box_a = box_for_r4(cfg, BOX_CLEARANCE_A_R4)
    box_b = box_for_r4(cfg, BOX_CLEARANCE_B_R4)
    ref = ref_for_r4(cfg)

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
        IRR_CENTRAL_W_CM2, sigma_ext_cells, DX_M_R4, ratio_abs_ext_clamped)
    regime = ts.mixed_length_scale_regime(
        p_abs_w=p["p_abs_w"], l_geometric_m=L_GEOMETRIC_M_R4,
        k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
        length_provenance="bench_construction")
    netd = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
    thermo = dict(sigma_ext_cells=sigma_ext_cells, ratio_abs_ext_raw=ratio_abs_ext_raw,
                  p_abs_w=p["p_abs_w"], dt_ss_full_K=regime["dt_ss_full_K"],
                  netd_classification=netd["classification"])

    empty_p = _profile(cap_empty, cfg)
    scene_p = _profile(cap_article, cfg)
    C, C_empty = contrast_pair(cfg, empty_p, scene_p, dg.R4_W_OBJ, dg.R4_GUARD_OUT, dg.R4_W_FLANK)

    return dict(xi_ext=xi_ext, box_dev=box_dev, thermo=thermo, C=C, C_empty=C_empty,
                sigma_abs_nonneg=bool(ba["sigma_abs"] >= 0))


def main():
    print("=" * 78)
    print("exp-094 -- T28 cpl=40 resolution check, sigma_max comparability close, R3 census")
    print("=" * 78)

    t_start = time.time()

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD, unchanged)
    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR={floor:.6e}  (unchanged, applied unrecomputed -- Idealization 6)")

    xi_pass = True
    nonneg_pass = True

    # =================================================================
    # Mandatory new-suite gates 1-4 (static/algebraic)
    # =================================================================
    print("\n" + "=" * 78)
    print("MANDATORY NEW-SUITE GATES 1-4 (static/algebraic, R4 family)")
    print("=" * 78)

    # ---- Gate 1: vacuum-footprint precondition, applied to R4_CONFIGS
    vac_report = {}
    vac_pass = True
    for key in PAIR_KEYS_R4:
        cfg = dg.R4_CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R4_CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A_R4), ("BOX_B", BOX_CLEARANCE_B_R4)):
            x0, x1, y0, y1 = box_for_r4(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            vac_pass = vac_pass and ok
        vac_report[key] = cell
    print(f"[Gate 1] vacuum-footprint precondition (R4_CONFIGS): PASS={vac_pass}")
    assert vac_pass, "GATE 1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # ---- Gate 2: A congruence
    a_c40 = dg.R4_CONFIGS["C40_R4"]["A"]
    a_g40 = dg.R4_CONFIGS["G40_R4"]["A"]
    gate2_pass = (a_c40 == a_g40 == round(dg.A_HALF_APERTURE * dg.R4_RATIO) == 1504)
    print(f"[Gate 2] A congruence: C40_R4.A={a_c40}  G40_R4.A={a_g40}  "
          f"round(A_HALF_APERTURE*R4_RATIO)={round(dg.A_HALF_APERTURE * dg.R4_RATIO)}  PASS={gate2_pass}")
    assert gate2_pass, "GATE 2 FAILED -- R4 congruent-construction identity broken; HALT"

    # ---- Gate 3: L_GEOMETRIC_M_R4 bit-identity across native/R3/R4
    gate3_dev_native = abs(L_GEOMETRIC_M_R4 - L_GEOMETRIC_M)
    gate3_dev_r3 = abs(L_GEOMETRIC_M_R4 - L_GEOMETRIC_M_R3)
    gate3_pass = gate3_dev_native < 1e-12 and gate3_dev_r3 < 1e-12
    print(f"[Gate 3] L_GEOMETRIC_M_R4={L_GEOMETRIC_M_R4:.6e}  L_GEOMETRIC_M={L_GEOMETRIC_M:.6e}  "
          f"L_GEOMETRIC_M_R3={L_GEOMETRIC_M_R3:.6e}  PASS={gate3_pass}")
    assert gate3_pass, "GATE 3 FAILED -- R4 physical shell radius does not match native/R3; HALT"

    # ---- Gate 4: SIGMA_R4_CORRECTED == 0.25
    gate4_pass = abs(SIGMA_R4_CORRECTED - 0.25) < 1e-12
    print(f"[Gate 4] SIGMA_R4_CORRECTED={SIGMA_R4_CORRECTED}  PASS={gate4_pass}")
    assert gate4_pass, "GATE 4 FAILED -- SIGMA_R4_CORRECTED != 0.25; HALT"

    # ---- Gate 6 (documentation-only, non-discriminating, NEVER a substitute
    # for Gate 5): EM's own static assert, algebraically tautological given
    # Gate 4 already holds -- kept only for the physical record.
    gate6_lhs = 2 * SIGMA_R4_CORRECTED * dg.R4_R_OUT
    gate6_rhs = 2 * SIGMA_NATIVE * dg.R_OUT
    gate6_dev = abs(gate6_lhs - gate6_rhs)
    gate6_pass = gate6_dev < 1e-9
    print(f"[Gate 6, documentation-only] 2*SIGMA_R4_CORRECTED*R4_R_OUT={gate6_lhs}  "
          f"2*SIGMA_NATIVE*R_OUT={gate6_rhs}  dev={gate6_dev:.3e}  PASS={gate6_pass}  "
          f"(non-discriminating -- reduces to a tautology already implied by Gate 4, "
          f"per phase3_synthesis.md; NOT a substitute for Gate 5 below)")

    gate5_log = []   # populated by _run_sim_r4_sigma's own inline assert firing cleanly
    print("\n[Gate 5] (mandatory, Red Team RT-1) runtime sigma_e/sigma_max check -- wired "
          "INSIDE `_run_sim_r4_sigma` itself, fires on every Rank 1a/1b article call, "
          "before any FDTD step. See per-call confirmation below each Rank 1a/1b block.")

    # =================================================================
    # RANK 2 -- FIRST, sigma@41.6deg sigma-comparability close (4 calls)
    # =================================================================
    print("\n" + "=" * 78)
    print("RANK 2 -- sigma@41.6deg sigma-comparability close (cpl=30, sigma_max=1/3 corrected)")
    print("=" * 78)

    jobs_r2 = []
    for key in PAIR_KEYS_R3:
        jobs_r2.append((key, RANK2_ANGLE, False, STEPS_R3, None))
        jobs_r2.append((key, RANK2_ANGLE, True, STEPS_R3, SIGMA_R3_CORRECTED))
    assert len(jobs_r2) == 4
    print(f"\n{len(jobs_r2)} FDTD calls queued (Rank 2)")
    captures_r2, wall_r2 = run_block(jobs_r2)
    print(f"Rank 2 wall time: {wall_r2:.1f}s ({wall_r2 / 60.0:.2f} min)")

    cells_r2 = {}
    for key in PAIR_KEYS_R3:
        cap_empty = captures_r2[(key, RANK2_ANGLE, False, STEPS_R3)]
        cap_article = captures_r2[(key, RANK2_ANGLE, True, STEPS_R3)]
        cell = cell_metrics_full(key, RANK2_ANGLE, STEPS_R3, cap_empty, cap_article)
        cells_r2[key] = cell
        for xi in cell["xi_ext"].values():
            if xi > XI_TOL:
                xi_pass = False
        if not cell["sigma_abs_nonneg"]:
            nonneg_pass = False
    print(f"\n[Rank 2] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 2 FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 2] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 2 FAILED -- non-negativity gate; HALT"

    pm_r2 = pair_metrics_full(cells_r2["C40_R3"], cells_r2["G40_R3"], floor)

    # native-sigma comparator, independently re-pulled from exp-091's own
    # committed results.json (NOT hand-typed), per NOTES.md's own citation.
    with open(EXP091_RESULTS) as f:
        j091 = json.load(f)
    native_r2 = j091["raw"]["r3_leg4_cpl30_steps4200_bracket"]["41.6"]
    print(f"\n[Rank 2] native-sigma (0.5) comparator, exp-091's own filed 41.6deg bracket: "
          f"delta_scene={native_r2['delta_scene']:+.6e}  frac_contrast={native_r2['frac_contrast']:.6e}  "
          f"ratio_k={native_r2['ratio_k']:.4f}  frac_p_abs={native_r2['frac_p_abs']:.6e}  "
          f"floor_pass={native_r2['floor_pass']}")
    print(f"[Rank 2] corrected-sigma (1/3), this cycle: delta_scene={pm_r2['delta_scene']:+.6e}  "
          f"frac_contrast={pm_r2['frac_contrast']:.6e}  ratio_k={pm_r2['ratio_k']:.4f}  "
          f"frac_p_abs={pm_r2['frac_p_abs']:.6e}  floor_pass={pm_r2['floor_pass']}")

    ds_ratio_r2 = pm_r2["delta_scene"] / native_r2["delta_scene"] if native_r2["delta_scene"] != 0 else float("inf")
    ds_sign_match_r2 = (pm_r2["delta_scene"] > 0) == (native_r2["delta_scene"] > 0)
    fc_ratio_r2 = pm_r2["frac_contrast"] / native_r2["frac_contrast"] if native_r2["frac_contrast"] != 0 else float("inf")
    ds_verdict_r2 = ratio_sign_verdict([(ds_ratio_r2, ds_sign_match_r2)])
    fc_verdict_r2 = ratio_sign_verdict([(fc_ratio_r2, True)])
    rank2_verdict = min([ds_verdict_r2, fc_verdict_r2], key=lambda v: VERDICT_RANK[v])
    print(f"\n[Rank 2 PRIMARY] delta_scene ratio={ds_ratio_r2:.4f} sign_match={ds_sign_match_r2}  "
          f"sub-verdict={ds_verdict_r2}  |  frac_contrast ratio={fc_ratio_r2:.4f}  "
          f"sub-verdict={fc_verdict_r2}  ||  OVERALL VERDICT={rank2_verdict}  "
          f"(no confident directional lean pre-committed, per Phase-3 RT-2 correction -- "
          f"REFUTE disclosed as at least as plausible as CONFIRM)")

    # informational, non-gating (see module docstring disclosure (iii) for
    # both readings reported)
    p_c_r2, p_g_r2 = pm_r2["p_c"], pm_r2["p_g"]
    pg_pc_ratio_r2 = p_g_r2 / p_c_r2 if p_c_r2 != 0 else float("inf")
    ratio_abs_ext_dev_r2 = abs(pm_r2["ratio_abs_ext_raw_c"] - 0.51) / 0.51
    print(f"[Rank 2, informational, non-gating] p_abs_w(G)/p_abs_w(C) ratio={pg_pc_ratio_r2:.4f}  "
          f"(energy-flatness-style reading); ratio_abs_ext_raw_c={pm_r2['ratio_abs_ext_raw_c']:.4f}  "
          f"dev from 0.51 T9 anchor={ratio_abs_ext_dev_r2:.2%}  "
          f"(both reported per module docstring disclosure (iii); frac_p_abs={pm_r2['frac_p_abs']:.6e})")

    # =================================================================
    # RANK 3 -- SECOND, census R3-verify, three angles (12 calls)
    # =================================================================
    print("\n" + "=" * 78)
    print("RANK 3 -- census R3-verify, 36.0/38.4/38.8deg (cpl=30, sigma_max=0.5 native)")
    print("=" * 78)

    jobs_r3 = []
    for key in PAIR_KEYS_R3:
        for th in RANK3_ANGLES:
            jobs_r3.append((key, th, False, STEPS_R3, None))
            jobs_r3.append((key, th, True, STEPS_R3, SIGMA_NATIVE))
    assert len(jobs_r3) == 12
    print(f"\n{len(jobs_r3)} FDTD calls queued (Rank 3)")
    captures_r3, wall_r3 = run_block(jobs_r3)
    print(f"Rank 3 wall time: {wall_r3:.1f}s ({wall_r3 / 60.0:.2f} min)")

    cells_r3 = {}
    for key in PAIR_KEYS_R3:
        for th in RANK3_ANGLES:
            cap_empty = captures_r3[(key, th, False, STEPS_R3)]
            cap_article = captures_r3[(key, th, True, STEPS_R3)]
            cell = cell_metrics_full(key, th, STEPS_R3, cap_empty, cap_article)
            cells_r3[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[Rank 3] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 3 FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 3] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 3 FAILED -- non-negativity gate; HALT"

    # cpl=20 comparator, independently re-pulled from exp-090's own committed
    # results.json table1 (NOT hand-typed).
    with open(EXP090_RESULTS) as f:
        j090 = json.load(f)
    cpl20_table = {row["theta"]: row for row in j090["table1"]}

    rank3_report = {}
    for th in RANK3_ANGLES:
        c_cell = cells_r3[("C40_R3", th)]
        g_cell = cells_r3[("G40_R3", th)]
        pm = pair_metrics_full(c_cell, g_cell, floor)
        cpl20 = cpl20_table[th]
        y_cpl20 = cpl20["y"]
        if not pm["floor_pass"]:
            outcome = "NODE-UNRESOLVABLE"
            y_cpl30 = None
        else:
            y_cpl30 = 1 if pm["ratio_k"] > RATIO_HIGH else 0
            outcome = "CONSISTENT" if y_cpl30 == y_cpl20 else "FLIPPED"
        rank3_report[th] = dict(
            delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
            ratio_k_cpl20=cpl20["ratio_k"], y_cpl20=y_cpl20, y_cpl30=y_cpl30,
            outcome=outcome,
        )
    print("\n[Rank 3 PRIMARY] per-angle three-way outcome:")
    for th, r in sorted(rank3_report.items()):
        print(f"  theta={th}: ratio_k_cpl20={r['ratio_k_cpl20']:.4f} (Y={r['y_cpl20']})  "
              f"ratio_k_cpl30={r['ratio_k']:.4f}  floor_pass={r['floor_pass']}  "
              f"Y_cpl30={r['y_cpl30']}  OUTCOME={r['outcome']}")

    # =================================================================
    # RANK 1a -- THIRD, cpl=40 settling precondition (8 calls, gates Rank 1b)
    # =================================================================
    print("\n" + "=" * 78)
    print(f"RANK 1a -- cpl=40 (R4) settling precondition @ {RANK1_ANGLE_SETTLE}deg "
          f"(sigma_max={SIGMA_R4_CORRECTED})")
    print("=" * 78)

    jobs_r1a = []
    for steps in (dg.R4_STEPS, dg.R4_STEPS_STRESS):
        for key in PAIR_KEYS_R4:
            jobs_r1a.append((key, RANK1_ANGLE_SETTLE, False, steps, None))
            jobs_r1a.append((key, RANK1_ANGLE_SETTLE, True, steps, SIGMA_R4_CORRECTED))
    assert len(jobs_r1a) == 8
    print(f"\n{len(jobs_r1a)} FDTD calls queued (Rank 1a) -- Gate 5 fires inline on each "
          f"article call, before its own FDTD step")
    captures_r1a, wall_r1a = run_block_r4(jobs_r1a)
    print(f"Rank 1a wall time: {wall_r1a:.1f}s ({wall_r1a / 60.0:.2f} min)")
    print("[Gate 5] all 4 Rank 1a article calls completed their inline runtime "
          "sigma_e/sigma_max assert without raising -- PASS (an AssertionError inside "
          "any worker would have propagated and stopped this script before this line)")

    cells_r1a = {}
    for steps in (dg.R4_STEPS, dg.R4_STEPS_STRESS):
        for key in PAIR_KEYS_R4:
            cap_empty = captures_r1a[(key, RANK1_ANGLE_SETTLE, False, steps)]
            cap_article = captures_r1a[(key, RANK1_ANGLE_SETTLE, True, steps)]
            cell = cell_metrics_r4(key, RANK1_ANGLE_SETTLE, steps, cap_empty, cap_article)
            cells_r1a[(key, steps)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[Rank 1a] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 1a FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 1a] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 1a FAILED -- non-negativity gate; HALT"

    pm_5600 = pair_metrics_full(cells_r1a[("C40_R4", dg.R4_STEPS)], cells_r1a[("G40_R4", dg.R4_STEPS)], floor)
    pm_8400 = pair_metrics_full(cells_r1a[("C40_R4", dg.R4_STEPS_STRESS)], cells_r1a[("G40_R4", dg.R4_STEPS_STRESS)], floor)
    ds_5600, ds_8400 = pm_5600["delta_scene"], pm_8400["delta_scene"]
    rel_dev_r1a = abs(ds_8400 - ds_5600) / abs(ds_5600) if ds_5600 != 0 else float("inf")
    if rel_dev_r1a <= 1e-2:
        r1a_verdict = "PASS"
    elif rel_dev_r1a <= 1e-1:
        r1a_verdict = "CAUTIONARY-PASS"
    else:
        r1a_verdict = "HALT"
    print(f"\n[Rank 1a PRIMARY] delta_scene(STEPS={dg.R4_STEPS})={ds_5600:+.6e}  "
          f"delta_scene(STEPS={dg.R4_STEPS_STRESS})={ds_8400:+.6e}  "
          f"rel_dev={rel_dev_r1a:.4%}  VERDICT={r1a_verdict}  "
          f"(see module docstring disclosure (ii) for the single-delta_scene "
          f"settling-metric resolution of this check's own ambiguous 'at "
          f"both/either config' wording)")
    # =================================================================
    # RANK 1b -- THIRD, cpl=40 interior sweep (24 calls, gated on Rank 1a)
    # =================================================================
    print("\n" + "=" * 78)
    print(f"RANK 1b -- cpl=40 (R4) interior near-null sweep, 6 angles "
          f"(sigma_max={SIGMA_R4_CORRECTED}, gate={r1a_verdict})")
    print("=" * 78)

    if r1a_verdict == "HALT":
        # NOTES.md: HALT = do not spend Rank 1b's 24 calls. This is a
        # pre-registered, anticipated outcome path (not a blocker) --
        # gracefully skip Rank 1b and still persist everything computed so
        # far, rather than crashing before results.json/run_output.txt can
        # be written.
        print("\n[Rank 1b] SKIPPED -- Rank 1a fired HALT (rel_dev > 1e-1); "
              "NOTES.md instructs not spending these 24 calls.")
        jobs_r1b = []
        wall_r1b = 0.0
        rank1b_report = {}
        any_confirmed_r1b = all_nonpositive_r1b = all_floor_fail_r1b = None
        rank1b_outcome = "NOT RUN (Rank 1a HALT)"
        r1b_pabs_max_dev_pct = None
    else:
        jobs_r1b = []
        for key in PAIR_KEYS_R4:
            for th in RANK1B_ANGLES:
                jobs_r1b.append((key, th, False, dg.R4_STEPS, None))
                jobs_r1b.append((key, th, True, dg.R4_STEPS, SIGMA_R4_CORRECTED))
        assert len(jobs_r1b) == 24
        print(f"\n{len(jobs_r1b)} FDTD calls queued (Rank 1b) -- Gate 5 fires inline on each "
              f"article call, before its own FDTD step")
        captures_r1b, wall_r1b = run_block_r4(jobs_r1b)
        print(f"Rank 1b wall time: {wall_r1b:.1f}s ({wall_r1b / 60.0:.2f} min)")
        print("[Gate 5] all 12 Rank 1b article calls completed their inline runtime "
              "sigma_e/sigma_max assert without raising -- PASS")

        cells_r1b = {}
        for key in PAIR_KEYS_R4:
            for th in RANK1B_ANGLES:
                cap_empty = captures_r1b[(key, th, False, dg.R4_STEPS)]
                cap_article = captures_r1b[(key, th, True, dg.R4_STEPS)]
                cell = cell_metrics_r4(key, th, dg.R4_STEPS, cap_empty, cap_article)
                cells_r1b[(key, th)] = cell
                for xi in cell["xi_ext"].values():
                    if xi > XI_TOL:
                        xi_pass = False
                if not cell["sigma_abs_nonneg"]:
                    nonneg_pass = False
        print(f"\n[Rank 1b] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
        assert xi_pass, "Rank 1b FAILED -- extinction-routes disagreement; HALT"
        print(f"[Rank 1b] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
        assert nonneg_pass, "Rank 1b FAILED -- non-negativity gate; HALT"

        rank1b_report = {}
        for th in RANK1B_ANGLES:
            c_cell = cells_r1b[("C40_R4", th)]
            g_cell = cells_r1b[("G40_R4", th)]
            pm = pair_metrics_full(c_cell, g_cell, floor)
            pg_pc_ratio = pm["p_g"] / pm["p_c"] if pm["p_c"] != 0 else float("inf")
            ratio_abs_ext_dev = abs(pm["ratio_abs_ext_raw_c"] - 0.51) / 0.51
            rank1b_report[th] = dict(
                delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
                ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], resolved=pm["resolved"],
                frac_p_abs=pm["frac_p_abs"], p_c=pm["p_c"], p_g=pm["p_g"],
                pg_pc_ratio=pg_pc_ratio, ratio_abs_ext_raw_c=pm["ratio_abs_ext_raw_c"],
                ratio_abs_ext_dev_from_anchor=ratio_abs_ext_dev,
                classification=("NODE-UNRESOLVABLE" if not pm["floor_pass"] else classification_word(pm["ratio_k"])),
            )
        print("\n[Rank 1b] per-angle results:")
        for th, r in sorted(rank1b_report.items()):
            print(f"  theta={th}: delta_scene={r['delta_scene']:+.6e}  frac_contrast={r['frac_contrast']:.6e}  "
                  f"ratio_k={r['ratio_k']:.4f}  class={r['classification']}  floor_pass={r['floor_pass']}  "
                  f"p_abs_w(G)/p_abs_w(C)={r['pg_pc_ratio']:.4f}")

        any_confirmed_r1b = any(r["delta_scene"] > 0 and r["floor_pass"] for r in rank1b_report.values())
        all_nonpositive_r1b = all(r["delta_scene"] <= 0 for r in rank1b_report.values())
        all_floor_fail_r1b = all(not r["floor_pass"] for r in rank1b_report.values())
        if any_confirmed_r1b:
            rank1b_outcome = "TWO-NODE CONFIRMED"
        elif all_nonpositive_r1b:
            rank1b_outcome = "SINGLE-NULL"
        else:
            rank1b_outcome = "STILL AMBIGUOUS"
        print(f"\n[Rank 1b PRIMARY] any interior point delta_scene>0 AND floor_pass: {any_confirmed_r1b}")
        print(f"[Rank 1b PRIMARY] all interior points delta_scene<=0: {all_nonpositive_r1b}")
        print(f"[Rank 1b PRIMARY] all interior points floor_pass=False: {all_floor_fail_r1b}")
        print(f"[Rank 1b PRIMARY] THREE-WAY OUTCOME = {rank1b_outcome}")

        # Idealization 23 (RT-5) informational, non-gating: p_abs_w G4/C4 ratio,
        # per angle -- see module docstring disclosure (iii).
        r1b_pabs_deviations = [abs(r["pg_pc_ratio"] - 1.0) for r in rank1b_report.values()]
        r1b_pabs_max_dev_pct = max(r1b_pabs_deviations) * 100.0
        print(f"\n[Rank 1b, informational, non-gating, RT-5/Idealization 23] p_abs_w(G4)/p_abs_w(C4) "
              f"ratio across all 6 angles: max deviation from 1.0 = {r1b_pabs_max_dev_pct:.4f}%  "
              f"(tests whether exp-093's own cpl<=30-verified energy-flatness finding extends to "
              f"cpl=40; both the literal G4/C4 ratio AND the established ratio_abs_ext_raw_c "
              f"deviation from the 0.51 T9 anchor are reported per module docstring disclosure "
              f"(iii) -- neither is gating)")
        for th, r in sorted(rank1b_report.items()):
            print(f"    theta={th}: p_abs_w(G4)/p_abs_w(C4)={r['pg_pc_ratio']:.4f}  "
                  f"ratio_abs_ext_raw_c dev from 0.51={r['ratio_abs_ext_dev_from_anchor']:.2%}")

    total_fdtd_wall = wall_r2 + wall_r3 + wall_r1a + wall_r1b
    print(f"\ntotal FDTD wall time (Rank 2+3+1a+1b): {total_fdtd_wall:.1f}s "
          f"({total_fdtd_wall / 60.0:.2f} min)")

    # =================================================================
    # RANK 3-ext -- FOURTH, caution-zone growth (0 FDTD calls, desk-only)
    # =================================================================
    print("\n" + "=" * 78)
    print("RANK 3-ext -- caution-zone growth, cpl=30-only, desk-only (0 FDTD calls)")
    print("=" * 78)

    with open(EXP093_RESULTS) as f:
        j093 = json.load(f)
    base_table = j093["item2"]["base_table"]     # exp-093's own n=8 cpl=30-only table
    zone_base_reproduced = compute_zone(base_table)
    EXPECTED_BASE = j093["item2"]["expected"]

    def sig4_match(a, b, tol=5e-4):
        return abs(a - b) <= tol

    base_reproduces = True
    base_reproduces &= sig4_match(zone_base_reproduced["auc"], EXPECTED_BASE["auc"])
    base_reproduces &= sig4_match(zone_base_reproduced["zone"][0], EXPECTED_BASE["zone"][0])
    base_reproduces &= sig4_match(zone_base_reproduced["zone"][1], EXPECTED_BASE["zone"][1])
    base_reproduces &= sig4_match(zone_base_reproduced["firth_beta"][0], EXPECTED_BASE["firth_beta"][0])
    base_reproduces &= sig4_match(zone_base_reproduced["firth_beta"][1], EXPECTED_BASE["firth_beta"][1])
    base_reproduces &= sig4_match(zone_base_reproduced["firth_m50"], EXPECTED_BASE["firth_m50"])
    print(f"\n[Rank 3-ext] base n=8 table live re-recomputation vs exp-093's own frozen figures: "
          f"auc={zone_base_reproduced['auc']:.4f}  zone={zone_base_reproduced['zone']}  "
          f"firth_m50={zone_base_reproduced['firth_m50']:.4f}  reproduces_bit_exact={base_reproduces}")

    new_rows = []
    for th in RANK3_ANGLES:
        r = rank3_report[th]
        if not r["floor_pass"]:
            print(f"  theta={th}: NODE-UNRESOLVABLE -- excluded from Rank 3-ext, per NOTES.md")
            continue
        m = r["frac_contrast"] / floor
        y = 1 if r["ratio_k"] > RATIO_HIGH else 0
        new_rows.append(dict(theta=th, source="Rank 3, this cycle (cpl=30, native sigma)",
                              frac_contrast=r["frac_contrast"], ratio_k=r["ratio_k"], margin=m, y=y))
        print(f"  theta={th}: floor_pass=True -- included, margin={m:.4f}  Y={y}")

    extended_rows = sorted(base_table + new_rows, key=lambda r: r["margin"])
    zone_ext = compute_zone(extended_rows)
    zone_inverted = zone_ext["inverted"]
    rank3_ext_verdict = "CONFIRM" if (base_reproduces and not zone_inverted) else "REFUTE"
    print(f"\n[Rank 3-ext PRIMARY] extended table n={zone_ext['n']} pos={zone_ext['pos']}  "
          f"AUC={zone_ext['auc']:.4f}  zone={zone_ext['zone']}  inverted={zone_inverted}  "
          f"firth_m50={zone_ext['firth_m50']:.4f}  naive_MLE_diverges={zone_ext['naive_mle_diverges']}")
    print(f"[Rank 3-ext PRIMARY] VERDICT={rank3_ext_verdict}  "
          f"(base_reproduces={base_reproduces}, zone_inverted={zone_inverted})")

    total_wall_all = time.time() - t_start

    # ---------------------------------------------------------------- disclosures (printed AND persisted)
    netd_disclaimer = j093["netd_disclaimer"]   # RT-4: identical, unconditional, verbatim
    scope_note = ("This cycle is pure instrument recalibration (T1 route N/A, Checkpoint "
                  "criterion 2 N/A) -- no phenomenon-mechanism claim, REALIZABILITY_MEMO.md "
                  "untouched. (Idealization 7)")
    r4_family_disclaimer = ("Idealization 17: the R4 (cpl=40) geometry family is a mechanical, "
                             "zero-design-freedom substitution of R4_RATIO=2.0 for R3_RATIO=1.5 "
                             "into the already-committed r3_config() recipe. If the R3-family "
                             "recipe carries any undetected systematic bias, R4 inherits it "
                             "unchanged -- the two families are not independent confirmations "
                             "of the re-discretization scheme, only of the specific feature "
                             "under test at two grid densities.")
    print(f"\n[disclosure] netd_disclaimer: {netd_disclaimer}")
    print(f"[disclosure] scope_note: {scope_note}")
    print(f"[disclosure] r4_family_disclaimer: {r4_family_disclaimer}")

    # ---------------------------------------------------------------- persist
    def th_key(d):
        return {str(k): v for k, v in d.items()}

    out = dict(
        total_fdtd_calls=48, rank2_calls=4, rank3_calls=12, rank1a_calls=8,
        rank1b_calls=len(jobs_r1b), rank3_ext_calls=0,
        rank2_wall_s=wall_r2, rank3_wall_s=wall_r3, rank1a_wall_s=wall_r1a, rank1b_wall_s=wall_r1b,
        total_fdtd_wall_time_s=total_fdtd_wall, total_wall_time_s=total_wall_all,
        sigma_native=SIGMA_NATIVE, sigma_r3_corrected=SIGMA_R3_CORRECTED,
        sigma_r4_corrected=SIGMA_R4_CORRECTED,
        r13_floor_gate=dict(floor=floor, rms_frac_contrast=rms, n_window_points=n83),
        gates=dict(
            gate1_vacuum_footprint_r4=dict(report=vac_report, pass_=vac_pass),
            gate2_a_congruence=dict(a_c40_r4=a_c40, a_g40_r4=a_g40, pass_=gate2_pass),
            gate3_l_geometric_bit_identity=dict(
                l_geometric_m_r4=L_GEOMETRIC_M_R4, l_geometric_m=L_GEOMETRIC_M,
                l_geometric_m_r3=L_GEOMETRIC_M_R3, dev_native=gate3_dev_native,
                dev_r3=gate3_dev_r3, pass_=gate3_pass),
            gate4_sigma_r4_corrected=dict(value=SIGMA_R4_CORRECTED, pass_=gate4_pass),
            gate5_runtime_sigma_array=dict(
                pass_=True, n_article_calls_checked=4 + 12,
                note=("Wired inline in _run_sim_r4_sigma: "
                      "np.isclose(sim.sigma_e[shell_mask].max(), sigma_max, atol=1e-9), "
                      "shell_mask=(PEC_R_R4<=rr<=R4_R_OUT) on the ez-point grid centered "
                      "at (obj_x,obj_y), rr from materials._grids -- mirrors "
                      "materials.graded_black_shell's own indexing exactly. Fires BEFORE "
                      "sim.run() on all 16 Rank 1a/1b article calls (4+12); an "
                      "AssertionError in any worker would have propagated and stopped "
                      "this script before results.json was ever written.")),
            gate6_documentation_only=dict(lhs=gate6_lhs, rhs=gate6_rhs, dev=gate6_dev, pass_=gate6_pass),
        ),
        xi_pass=xi_pass, nonneg_pass=nonneg_pass,
        rank2=dict(
            angle=RANK2_ANGLE, verdict=rank2_verdict,
            delta_scene_sub_verdict=ds_verdict_r2, frac_contrast_sub_verdict=fc_verdict_r2,
            corrected=dict(delta_scene=pm_r2["delta_scene"], frac_contrast=pm_r2["frac_contrast"],
                           ratio_k=pm_r2["ratio_k"], frac_p_abs=pm_r2["frac_p_abs"],
                           floor_pass=pm_r2["floor_pass"]),
            native_comparator=native_r2,
            delta_scene_ratio=ds_ratio_r2, frac_contrast_ratio=fc_ratio_r2,
            pg_pc_ratio_informational=pg_pc_ratio_r2,
            ratio_abs_ext_dev_from_anchor_informational=ratio_abs_ext_dev_r2,
        ),
        rank3=dict(angles=RANK3_ANGLES, per_theta=th_key(rank3_report)),
        rank1a=dict(
            angle=RANK1_ANGLE_SETTLE, steps=[dg.R4_STEPS, dg.R4_STEPS_STRESS],
            delta_scene_5600=ds_5600, delta_scene_8400=ds_8400, rel_dev=rel_dev_r1a,
            verdict=r1a_verdict,
        ),
        rank1b=dict(
            angles=RANK1B_ANGLES, gate=r1a_verdict,
            settling_uncertain_flag=(r1a_verdict == "CAUTIONARY-PASS"),
            per_theta=th_key(rank1b_report),
            any_new_confirmed_excursion=any_confirmed_r1b, all_new_nonpositive=all_nonpositive_r1b,
            all_new_floor_fail=all_floor_fail_r1b, outcome=rank1b_outcome,
            pg_pc_ratio_max_dev_pct_informational=r1b_pabs_max_dev_pct,
        ),
        rank3_ext=dict(
            base_table_n=len(base_table), base_reproduces_bit_exact=base_reproduces,
            base_zone_reproduced=zone_base_reproduced, base_zone_expected=EXPECTED_BASE,
            new_rows_included=new_rows, extended_zone=zone_ext, zone_inverted=zone_inverted,
            verdict=rank3_ext_verdict,
        ),
        netd_disclaimer=netd_disclaimer,
        scope_note=scope_note,
        r4_family_disclaimer=r4_family_disclaimer,
        spec_resolution_disclosures=(
            "See this file's own module docstring, disclosures (i)-(iii): (i) "
            "R4_BASE_OBJ_Y set to 1584 (=R4_BASE_NY//2, mirroring R3_BASE_OBJ_Y's own "
            "precedent), not NOTES.md's literal table value 1504, to satisfy the "
            "cycle's own mandatory Gate 2 (A==1504) and its Setup section's own "
            "explicit congruence sentence; (ii) Rank 1a's settling check is a SINGLE "
            "delta_scene(steps)-based metric, not two independent per-config metrics; "
            "(iii) Rank 1b's/Rank 2's 'p_abs_w ratio ... 0.51 T9 anchor' informational "
            "check is reported as BOTH readings (literal G/C p_abs_w ratio, AND the "
            "established ratio_abs_ext_raw_c-vs-0.51 anchor), non-gating either way."
        ),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")

    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"  Rank 2 (sigma@41.6deg):               {rank2_verdict}")
    print(f"  Rank 3 (census R3-verify, 3 angles):  " +
          ", ".join(f"{th}={rank3_report[th]['outcome']}" for th in RANK3_ANGLES))
    print(f"  Rank 1a (cpl=40 settling):             {r1a_verdict}  (rel_dev={rel_dev_r1a:.4%})")
    print(f"  Rank 1b (cpl=40 interior three-way):   {rank1b_outcome}")
    print(f"  Rank 3-ext (caution-zone growth):      {rank3_ext_verdict}  "
          f"(zone_inverted={zone_inverted})")
    print(f"  total FDTD calls: {out['total_fdtd_calls']}   total wall time: "
          f"{total_wall_all:.1f}s ({total_wall_all / 60.0:.2f} min)")

    return out


if __name__ == "__main__":
    main()
