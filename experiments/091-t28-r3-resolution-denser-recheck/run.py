"""exp-091 -- T28 R3 Resolution & Denser Recheck: the still-overdue cpl 20->30
resolution check on the C40/G40 PAIR_PAD ambient channel, run jointly with a
tighter-settling (STEPS=4200, not 2800) native-cpl repeat, at the three T28
census angles (37.2/40.2/41.4deg), PLUS a dedicated R3_STEPS settling spot-
check at both angles and a two-point crossing-bracket leg at 40.4/41.6deg.
=============================================================================
Panel Iteration 68 (lead: MATERIALS & METAMATERIALS). Frozen spec:
phase3_synthesis.md (all 10 Phase-2 Red Team mandatory-fix-docket items
adopted, zero overridden). Predictions (NOTES.md a/a2/b/b2/c1/c2/d) committed
to git strictly BEFORE this file's first run (house discipline,
non-negotiable).

Reuses exp-088's own `_load()` chain (exp-088 -> exp-087 -> exp-083) VERBATIM,
UNMODIFIED for `dg`(=dg069)/`build_article`/`_run_sim`/`box_for`/`ref_for`/
`widths_direction_corrected`/`_label`/`classify_resolved`/`frac_contrast_of`/
`compute_floor` -- zero geometry retyped, zero `lab/` diff. Reuses exp-090's
own `find_zero_crossings` verbatim for prediction (a2).

NEW code this cycle (all additive, none of it touches `lab/` or any frozen
experiment file other than the single additive line in
experiments/069-.../design_geometry.py's own R3_CONFIGS, step 1 of this
cycle's task):

  * `box_for_r3`/`ref_for_r3` -- R3-scaled mirrors of exp-087's own
    `box_for`/`ref_for`. Those two functions close over NATIVE module-level
    constants (`R_OUT_CELLS=dg.R_OUT`, `REF_HALF_H=80`) that cannot be
    overridden by argument, so a literal call-through is impossible for the
    R3 leg; these two functions copy their exact 3-line formula, substituting
    the R3-scaled equivalents (`dg.R3_R_OUT`, `REF_HALF_H_R3=round(80*1.5)`)
    -- not a new formula, the same one at the other resolution.
  * `_run_sim_r3`/`build_article_r3` -- the first-ever R3-resolution FDTD
    call that also builds the PAIR_PAD article (every prior R3 leg in this
    program, exp-069/071, measured the EMPTY channel only). `_run_sim_r3`
    mirrors exp-083's own `_run_sim` structure exactly, substituting
    `dg.R3_CPL[600]` for the cpl and `dg.R3_TAPER` for the source edge taper
    (exp-069's own `_one_run_r3` convention). `build_article_r3` mirrors
    `build_article`'s own two calls (`materials.pec_disk` core +
    `materials.graded_black_shell` shell), scaling the PEC core radius
    (native 30 -> R3 `round(30*1.5)=45`) and the shell's `r_in`/`r_out`
    (30->45, `dg.R_OUT`(78)->`dg.R3_R_OUT`(117)) by the SAME R3_RATIO=1.5
    rule `dg069.r3_config()` already applies to every other geometric
    constant in this design (TAPER/W_OBJ/GUARD_OUT/W_FLANK/R_OUT itself).
    This exact scaling is not spelled out digit-by-digit in NOTES.md/
    phase1_proposal.md (only R_OUT's own R3 value is named there,
    Idealization 4: "same ~2.34um physical radius") -- but it is the only
    value consistent with that Idealization and with the one scaling rule
    this whole cycle's design already commits to; holding the article's
    core/shell radii at their NATIVE cell counts inside an R3-resolution grid
    would silently change the article's own physical size relative to the
    aperture, contaminating the resolution check with a geometry confound.
    Disclosed here and in the Result section, not a free design choice.
  * A generic `contrast_pair()` (parametrized window sizes) generalizing
    exp-083's own `contrast_pair` to accept either native (`dg.W_OBJ`/
    `dg.GUARD_OUT`/`dg.W_FLANK`) or R3-scaled (`dg.R3_W_OBJ`/
    `dg.R3_GUARD_OUT`/`dg.R3_W_FLANK`) window sizes -- same formula, same
    call to `amb.contrast_from_runs`, parametrized rather than duplicated.

Comparator convention (disclosed once, applied throughout): where a
"cpl=20" comparator is needed for a ratio test ((a), (b), (b2)), this run
uses Leg 1's own freshly-measured STEPS=4200 native-cpl remeasurement (this
cycle's own apples-to-apples same-methodology value), NOT exp-083/089's
older STEPS=2800 filed figure -- per the task brief's own explicit
instruction for (a). The filed STEPS=2800 values are still cited alongside,
as secondary disclosed context, and are the explicit subject of prediction
(c1) (the STEPS=4200-vs-2800 reproducibility question in its own right).
"""

import importlib.util
import json
import math
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078..090's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP083_DIR = os.path.join(ROOT, "experiments", "083-t28-pad-article-full-power-retest")
EXP083_RESULTS = os.path.join(EXP083_DIR, "results.json")
EXP088_DIR = os.path.join(ROOT, "experiments", "088-t28-node-bracket-r13-floor-gate")
EXP089_DIR = os.path.join(ROOT, "experiments", "089-t28-combined-angle-census")
EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP090_RESULTS = os.path.join(EXP090_DIR, "results.json")

# chain: exp088 -> exp087 -> exp083 (exactly exp-089/090's own idiom)
exp088 = _load(os.path.join(EXP088_DIR, "run.py"), "_exp091_exp088")
exp087 = exp088.exp087
exp083 = exp087.exp083
# exp-090's own desk-only script -- reused ONLY for `find_zero_crossings`
# (prediction (a2)'s exact interpolation formula, not re-derived by hand).
exp090 = _load(os.path.join(EXP090_DIR, "run.py"), "_exp091_exp090")

dg = exp088.dg
build_article = exp088.build_article
_run_sim = exp088._run_sim
box_for = exp088.box_for
ref_for = exp088.ref_for
widths_direction_corrected = exp088.widths_direction_corrected
_label = exp088._label
classify_resolved = exp088.classify_resolved
frac_contrast_of = exp088.frac_contrast_of
compute_floor = exp088.compute_floor
_profile = exp083._profile
find_zero_crossings = exp090.find_zero_crossings

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts, materials  # noqa: E402

# ---------------------------------------------------------------- Step 1 sanity
assert "G40_R3" in dg.R3_CONFIGS, "design_geometry.py's G40_R3 addition missing"
assert dg.R3_CONFIGS["G40_R3"]["nx"] == dg.R3_CONFIGS["C80_R3"]["nx"] == 660
assert dg.R3_CONFIGS["G40_R3"]["ny"] == dg.R3_CONFIGS["C80_R3"]["ny"] == 2496
assert dg.R3_CONFIGS["G40_R3"]["A"] == dg.R3_CONFIGS["C40_R3"]["A"] == round(752 * 1.5) == 1128

PAIR_KEYS = ("C40", "G40")
PAIR_KEYS_R3 = ("C40_R3", "G40_R3")

ANGLES = [dg.DENSE_ANGLES[6], dg.DENSE_ANGLES[21], dg.DENSE_ANGLES[27]]
assert ANGLES == [37.2, 40.2, 41.4], f"angle grid drifted: {ANGLES}"
SETTLE_ANGLES = [ANGLES[1], ANGLES[2]]
assert SETTLE_ANGLES == [40.2, 41.4]

assert 40.4 in dg.DENSE_ANGLES and 41.6 in dg.DENSE_ANGLES
BRACKET_ANGLES = [dg.DENSE_ANGLES[dg.DENSE_ANGLES.index(40.4)],
                  dg.DENSE_ANGLES[dg.DENSE_ANGLES.index(41.6)]]
assert BRACKET_ANGLES == [40.4, 41.6], f"bracket angle grid drifted: {BRACKET_ANGLES}"

STEPS_LEG1 = dg.STEPS_STRESS                     # 4200, native cpl=20
assert STEPS_LEG1 == 4200
STEPS_LEG2 = dg.R3_STEPS                         # 4200, cpl=30 (R3_STEPS)
assert STEPS_LEG2 == 4200
STEPS_LEG3 = round(dg.R3_STEPS * 1.5)            # 6300, cpl=30 settling spot-check
assert STEPS_LEG3 == 6300
STEPS_LEG4 = dg.R3_STEPS                         # 4200, cpl=30, bracket leg

BOX_CLEARANCE_A = exp087.BOX_CLEARANCE_A         # 12
BOX_CLEARANCE_B = exp087.BOX_CLEARANCE_B         # 24
REF_HALF_H = exp087.REF_HALF_H                   # 80

BOX_CLEARANCE_A_R3 = round(BOX_CLEARANCE_A * dg.R3_RATIO)   # 18
BOX_CLEARANCE_B_R3 = round(BOX_CLEARANCE_B * dg.R3_RATIO)   # 36
REF_HALF_H_R3 = round(REF_HALF_H * dg.R3_RATIO)             # 120
assert (BOX_CLEARANCE_A_R3, BOX_CLEARANCE_B_R3, REF_HALF_H_R3) == (18, 36, 120), \
    "R3 clearance/ref scaling drifted from phase1_proposal.md Sec 2b (12->18, 24->36, 80->120)"

R_OUT_CELLS = dg.R_OUT             # 78
R3_R_OUT_CELLS = dg.R3_R_OUT       # 117

DX_M = exp087.DX_M
L_GEOMETRIC_M = exp087.L_GEOMETRIC_M
IRR_CENTRAL_W_CM2 = exp087.IRR_CENTRAL_W_CM2
K_AIR = exp087.K_AIR
DENSITY_SI_KG_M3, C_P_SI_J_KGK = exp087.DENSITY_SI_KG_M3, exp087.C_P_SI_J_KGK
EMISSIVITY = exp087.EMISSIVITY
T_AMBIENT_K = exp087.T_AMBIENT_K
NETD_BAND_K = exp087.NETD_BAND_K

DX_M_R3 = 600.0e-9 / dg.R3_CPL[600]                # 20e-9 m
L_GEOMETRIC_M_R3 = R3_R_OUT_CELLS * DX_M_R3
assert abs(L_GEOMETRIC_M_R3 - L_GEOMETRIC_M) < 1e-12, \
    "R3 physical radius does not match native (Idealization 4 sanity check)"

XI_TOL = exp087.XI_TOL
NOISE_MULT = exp087.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp087.RATIO_LOW, exp087.RATIO_HIGH
FLOOR_FRAC = exp088.FLOOR_FRAC

# ---------------------------------------------------------------- R3 article geometry (NEW)
PEC_R_NATIVE = 30
PEC_R_R3 = round(PEC_R_NATIVE * dg.R3_RATIO)       # 45
assert PEC_R_R3 == 45


def build_article_r3(sim, cx, cy):
    """R3-scaled mirror of `build_article` -- same two calls
    (pec_disk core + graded_black_shell), radii scaled by R3_RATIO=1.5
    (see module docstring)."""
    materials.pec_disk(sim, cx, cy, PEC_R_R3)
    materials.graded_black_shell(sim, cx, cy, PEC_R_R3, R3_R_OUT_CELLS)


def box_for_r3(cfg, clearance):
    ox, oy = cfg["obj_x"], cfg["obj_y"]
    r = R3_R_OUT_CELLS + clearance
    return (ox - r, ox + r, oy - r, oy + r)


def ref_for_r3(cfg):
    return (cfg["obj_x"], cfg["obj_y"], REF_HALF_H_R3)


def _run_sim_r3(cfg, theta, steps, with_article):
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R3_CPL[600],
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    if with_article:
        build_article_r3(sim, cfg["obj_x"], cfg["obj_y"])
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta, amplitude=1.0,
                         profile="plane", edge=dg.R3_TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def is_r3(key):
    return key.endswith("_R3")


def cfg_for(key):
    return dg.R3_CONFIGS[key] if is_r3(key) else dg.CONFIGS[key]


def contrast_pair(cfg, empty_p, scene_p, w_obj, guard_out, w_flank):
    """Generalizes exp-083's own `contrast_pair` (native window sizes
    hand-fixed there) to accept either native or R3-scaled window sizes --
    same formula, same `amb.contrast_from_runs` call, parametrized."""
    r = amb.contrast_from_runs([scene_p], [empty_p], [1.0],
                                cfg["y_lo"], cfg["obj_y"], w_obj, guard_out, w_flank)
    return r["C"], r["C_empty"]


def one_call(args):
    """Module-level (picklable) worker, dispatching on the "_R3" key suffix
    -- matches exp-087/088/089's own `one_call` idiom, extended for the two
    resolution branches."""
    key, th, art, steps = args
    if is_r3(key):
        cfg = dg.R3_CONFIGS[key]
        cap = _run_sim_r3(cfg, th, steps, art)
    else:
        cfg = dg.CONFIGS[key]
        cap = _run_sim(cfg, th, steps, art)
    return (key, th, art, steps, cap)


def crossing_shift_verdict(shift_deg):
    return "CONFIRM" if shift_deg <= 0.1 else "REFUTE"


def ratio_sign_verdict(cells):
    """cells: list of (ratio, sign_match). Shared verdict logic for (a) and
    (b2) -- same [0.3,3.0] CONFIRM / [0.1,10] REFUTE bands, any sign flip is
    an outright REFUTE."""
    if any(not sm for _, sm in cells):
        return "REFUTE"
    if any(r < 0.1 or r > 10.0 for r, _ in cells):
        return "REFUTE"
    if all(0.3 <= r <= 3.0 for r, _ in cells):
        return "CONFIRM"
    return "NEITHER"


def rel_dev_verdict(rel_dev):
    if rel_dev <= 0.01:
        return "CONFIRM"
    if rel_dev >= 0.05:
        return "REFUTE"
    return "NEITHER"


def classification_word(ratio):
    return {"X": "ENERGY-DOMINANT", "D": "ENERGY-DECOUPLED", "C": "CONSISTENT"}[_label(ratio)]


def main():
    print("=" * 78)
    print("exp-091 -- T28 R3 resolution & denser recheck")
    print("=" * 78)

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD, unchanged)
    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR_FRAC={FLOOR_FRAC}  FLOOR={floor:.6e}  (unchanged from exp-088, applied "
          f"unrecomputed against the new cpl=30 numbers -- Idealization 6)")

    # ---------------------------------------------------------------- P1: vacuum footprint (native + R3)
    vac_report = {}
    vac_pass = True
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A), ("BOX_B", BOX_CLEARANCE_B)):
            x0, x1, y0, y1 = box_for(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            vac_pass = vac_pass and ok
        vac_report[key] = cell
    for key in PAIR_KEYS_R3:
        cfg = dg.R3_CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R3_CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A_R3), ("BOX_B", BOX_CLEARANCE_B_R3)):
            x0, x1, y0, y1 = box_for_r3(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            vac_pass = vac_pass and ok
        vac_report[key] = cell
    print(f"\n[P1] vacuum-footprint precondition (native + R3 geometry): PASS={vac_pass}")
    assert vac_pass, "P1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # ---------------------------------------------------------------- FDTD calls (40 total)
    jobs = []
    for key in PAIR_KEYS:
        for th in ANGLES:
            jobs.append((key, th, False, STEPS_LEG1))
            jobs.append((key, th, True, STEPS_LEG1))
    for key in PAIR_KEYS_R3:
        for th in ANGLES:
            jobs.append((key, th, False, STEPS_LEG2))
            jobs.append((key, th, True, STEPS_LEG2))
    for key in PAIR_KEYS_R3:
        for th in SETTLE_ANGLES:
            jobs.append((key, th, False, STEPS_LEG3))
            jobs.append((key, th, True, STEPS_LEG3))
    for key in PAIR_KEYS_R3:
        for th in BRACKET_ANGLES:
            jobs.append((key, th, False, STEPS_LEG4))
            jobs.append((key, th, True, STEPS_LEG4))
    assert len(jobs) == 40, f"call count drifted: {len(jobs)}"
    assert len(set(jobs)) == 40, "duplicate job detected"

    print(f"\n{len(jobs)} FDTD calls queued "
          f"(Leg1=12 native cpl=20 STEPS=4200, Leg2=12 R3 cpl=30 STEPS=4200, "
          f"Leg3=8 R3 settling STEPS=6300, Leg4=8 R3 bracket STEPS=4200)")
    t0 = time.time()
    captures = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, cap) in enumerate(ex.map(one_call, jobs), 1):
            captures[(key, th, art, steps)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key:8s} theta={th:+06.2f} "
                  f"article={art} steps={steps}", flush=True)
    total_wall = time.time() - t0
    print(f"\ntotal wall time: {total_wall:.1f}s ({total_wall/60.0:.2f} min)")

    # ---------------------------------------------------------------- per-cell analysis
    cells = []
    for key in PAIR_KEYS:
        for th in ANGLES:
            cells.append((key, th, STEPS_LEG1))
    for key in PAIR_KEYS_R3:
        for th in ANGLES:
            cells.append((key, th, STEPS_LEG2))
    for key in PAIR_KEYS_R3:
        for th in SETTLE_ANGLES:
            cells.append((key, th, STEPS_LEG3))
    for key in PAIR_KEYS_R3:
        for th in BRACKET_ANGLES:
            cells.append((key, th, STEPS_LEG4))
    assert len(cells) == 20

    widths_by_cell = {}   # (key, th, steps, box_name) -> widths dict
    box_dev = {}          # (key, th, steps) -> {ext, abs}
    xi_ext = {}           # (key, th, steps, box_name) -> value
    thermo = {}           # (key, th, steps) -> dict
    contrast = {}         # (key, th, steps) -> dict(C=.., C_empty=..)
    xi_pass = True
    nonneg_pass = True

    for (key, th, steps) in cells:
        cfg = cfg_for(key)
        r3 = is_r3(key)
        cap_empty = captures[(key, th, False, steps)]
        cap_article = captures[(key, th, True, steps)]

        box_a = box_for_r3(cfg, BOX_CLEARANCE_A_R3) if r3 else box_for(cfg, BOX_CLEARANCE_A)
        box_b = box_for_r3(cfg, BOX_CLEARANCE_B_R3) if r3 else box_for(cfg, BOX_CLEARANCE_B)
        ref = ref_for_r3(cfg) if r3 else ref_for(cfg)

        for box_name, box in (("BOX_A", box_a), ("BOX_B", box_b)):
            w = widths_direction_corrected(cap_article, cap_empty, box, ref)
            widths_by_cell[(key, th, steps, box_name)] = w
            xi = abs(w["sigma_ext_cross"] - w["sigma_ext"]) / abs(w["sigma_ext"])
            xi_ext[(key, th, steps, box_name)] = xi
            if xi > XI_TOL:
                xi_pass = False
            if w["sigma_abs"] < 0:
                nonneg_pass = False

        ba = widths_by_cell[(key, th, steps, "BOX_A")]
        bb = widths_by_cell[(key, th, steps, "BOX_B")]
        box_dev[(key, th, steps)] = dict(
            ext=abs(ba["sigma_ext"] - bb["sigma_ext"]) / abs(ba["sigma_ext"]),
            abs=abs(ba["sigma_abs"] - bb["sigma_abs"]) / abs(ba["sigma_abs"]),
        )

        sigma_ext_cells = ba["sigma_ext"]
        ratio_abs_ext_raw = ba["sigma_abs"] / ba["sigma_ext"] if ba["sigma_ext"] != 0 else 0.0
        ratio_abs_ext_clamped = min(max(ratio_abs_ext_raw, 0.0), 1.0)
        dx_m, l_geo_m = (DX_M_R3, L_GEOMETRIC_M_R3) if r3 else (DX_M, L_GEOMETRIC_M)
        p = ts.absorbed_power_established_ratio(
            IRR_CENTRAL_W_CM2, sigma_ext_cells, dx_m, ratio_abs_ext_clamped)
        assert p["p_abs_w"] >= 0, "non-negativity gate FAILED on p_abs_w; HALT"
        regime = ts.mixed_length_scale_regime(
            p_abs_w=p["p_abs_w"], l_geometric_m=l_geo_m,
            k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
            emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
            length_provenance="bench_construction")
        netd = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
        thermo[(key, th, steps)] = dict(
            sigma_ext_cells=sigma_ext_cells, ratio_abs_ext_raw=ratio_abs_ext_raw,
            p_abs_w=p["p_abs_w"], dt_ss_full_K=regime["dt_ss_full_K"],
            netd_classification=netd["classification"], netd_disclaimer=netd["disclaimer"])

        empty_p = _profile(cap_empty, cfg)
        scene_p = _profile(cap_article, cfg)
        w_obj, guard_out, w_flank = ((dg.R3_W_OBJ, dg.R3_GUARD_OUT, dg.R3_W_FLANK) if r3
                                      else (dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK))
        C, C_empty = contrast_pair(cfg, empty_p, scene_p, w_obj, guard_out, w_flank)
        contrast[(key, th, steps)] = dict(C=C, C_empty=C_empty)

    print(f"\n[P4] xi_ext (extinction-routes agreement) <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "P4 FAILED -- extinction-routes disagreement exceeds tolerance; HALT"
    print(f"[non-negativity gate] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "non-negativity gate FAILED; HALT"

    # ---------------------------------------------------------------- pair metrics (C-key vs G-key at fixed theta/steps)
    def pair_metrics(c_key, g_key, th, steps):
        p_c = thermo[(c_key, th, steps)]["p_abs_w"]
        p_g = thermo[(g_key, th, steps)]["p_abs_w"]
        frac_p_abs = abs(p_g - p_c) / p_c if p_c != 0 else float("inf")
        c_c = contrast[(c_key, th, steps)]["C"]
        c_g = contrast[(g_key, th, steps)]["C"]
        delta_scene = c_g - c_c
        frac_contrast = abs(delta_scene) / abs(c_c)
        ratio_k = frac_p_abs / frac_contrast if frac_contrast != 0 else float("inf")
        floor_pass = bool(frac_contrast >= floor)
        box_dev_max = max(box_dev[(c_key, th, steps)]["ext"], box_dev[(c_key, th, steps)]["abs"],
                           box_dev[(g_key, th, steps)]["ext"], box_dev[(g_key, th, steps)]["abs"])
        noise_floor = NOISE_MULT * box_dev_max * p_c
        delta_p_abs = abs(p_g - p_c)
        noise_resolved = bool(delta_p_abs > noise_floor)
        resolved = bool(noise_resolved and floor_pass)
        margin = (delta_p_abs / noise_floor) if noise_floor != 0 else float("inf")
        return dict(theta=th, steps=steps, p_c=p_c, p_g=p_g, frac_p_abs=frac_p_abs,
                    C_c=c_c, C_g=c_g, C_empty_c=contrast[(c_key, th, steps)]["C_empty"],
                    C_empty_g=contrast[(g_key, th, steps)]["C_empty"],
                    delta_scene=delta_scene, frac_contrast=frac_contrast, ratio_k=ratio_k,
                    floor_pass=floor_pass, resolved=resolved, noise_floor=noise_floor,
                    delta_p_abs=delta_p_abs, box_dev_max=box_dev_max, margin=margin)

    native_leg1 = {th: pair_metrics("C40", "G40", th, STEPS_LEG1) for th in ANGLES}
    r3_leg2 = {th: pair_metrics("C40_R3", "G40_R3", th, STEPS_LEG2) for th in ANGLES}
    r3_leg3 = {th: pair_metrics("C40_R3", "G40_R3", th, STEPS_LEG3) for th in SETTLE_ANGLES}
    r3_leg4 = {th: pair_metrics("C40_R3", "G40_R3", th, STEPS_LEG4) for th in BRACKET_ANGLES}

    print("\n[raw per-(config,angle,cpl) primitives]")
    for label, d in (("Leg1 native cpl=20 STEPS=4200", native_leg1),
                      ("Leg2 R3 cpl=30 STEPS=4200", r3_leg2),
                      ("Leg3 R3 cpl=30 STEPS=6300", r3_leg3),
                      ("Leg4 R3 cpl=30 STEPS=4200 (bracket)", r3_leg4)):
        print(f"  -- {label} --")
        for th, m in sorted(d.items()):
            print(f"    theta={th:5.1f}  C_empty(C)={m['C_empty_c']:.6e}  "
                  f"C_empty(G)={m['C_empty_g']:.6e}  delta_scene={m['delta_scene']:+.6e}  "
                  f"frac_contrast={m['frac_contrast']:.6e}  p_abs_w(C)={m['p_c']:.6e}  "
                  f"frac_p_abs={m['frac_p_abs']:.6e}  ratio_k={m['ratio_k']:.6e}  "
                  f"floor_pass={m['floor_pass']}  resolved={m['resolved']}")

    # ================================================================== (a)
    filed_cpl20 = {37.2: dict(frac_contrast=4.162655e-4, delta_scene=2.348254e-4, ratio_k=3.4433),
                   40.2: dict(frac_contrast=2.830881e-4, delta_scene=-1.540815e-4, ratio_k=25.0820),
                   41.4: dict(frac_contrast=2.510967e-4, delta_scene=1.337362e-4, ratio_k=28.8072)}

    a_cells = []
    a_report = {}
    for th in ANGLES:
        ratio = r3_leg2[th]["frac_contrast"] / native_leg1[th]["frac_contrast"]
        sign_match = (r3_leg2[th]["delta_scene"] > 0) == (native_leg1[th]["delta_scene"] > 0)
        a_cells.append((ratio, sign_match))
        a_report[th] = dict(
            frac_contrast_cpl20_leg1=native_leg1[th]["frac_contrast"],
            frac_contrast_cpl30=r3_leg2[th]["frac_contrast"],
            ratio=ratio, sign_match=sign_match,
            delta_scene_cpl20_leg1=native_leg1[th]["delta_scene"],
            delta_scene_cpl30=r3_leg2[th]["delta_scene"],
            frac_contrast_filed_cpl20_steps2800=filed_cpl20[th]["frac_contrast"],
            ratio_vs_filed=r3_leg2[th]["frac_contrast"] / filed_cpl20[th]["frac_contrast"],
        )
    a_verdict = ratio_sign_verdict(a_cells)
    print(f"\n[(a) PRIMARY] frac_contrast_R3/frac_contrast_cpl20(Leg1) ratio+sign, "
          f"three census angles: VERDICT={a_verdict}")
    for th in ANGLES:
        r = a_report[th]
        print(f"  theta={th}: ratio={r['ratio']:.4f}  sign_match={r['sign_match']}  "
              f"(vs filed STEPS=2800: ratio={r['ratio_vs_filed']:.4f})")

    # ================================================================== (a2)
    with open(EXP083_RESULTS) as f:
        j083 = json.load(f)
    thetas083 = np.array(j083["thetas"])
    delta083 = np.array(j083["delta_scene"])
    crossings_cpl20 = find_zero_crossings(thetas083, delta083)
    print(f"\n[(a2)] cpl=20 zero-crossings of delta_scene(theta), n=31 census "
          f"(re-derived, not hand-typed): {np.round(crossings_cpl20, 4).tolist()}")

    def nearest_crossing(target):
        idx = int(np.argmin(np.abs(crossings_cpl20 - target)))
        return float(crossings_cpl20[idx])

    known_40 = nearest_crossing(40.265)
    known_41 = nearest_crossing(41.461)
    assert abs(known_40 - 40.265) < 0.01, f"expected ~40.265 crossing, got {known_40}"
    assert abs(known_41 - 41.461) < 0.01, f"expected ~41.461 crossing, got {known_41}"

    a2_report = {}
    for pair_name, (th0, th1), known in (
        ("40.2-40.4", (40.2, 40.4), known_40),
        ("41.4-41.6", (41.4, 41.6), known_41),
    ):
        v0 = r3_leg2[th0]["delta_scene"] if th0 in r3_leg2 else r3_leg4[th0]["delta_scene"]
        v1 = r3_leg2[th1]["delta_scene"] if th1 in r3_leg2 else r3_leg4[th1]["delta_scene"]
        found = find_zero_crossings([th0, th1], [v0, v1])
        if len(found) == 0:
            a2_report[pair_name] = dict(
                theta0=th0, theta1=th1, v0=v0, v1=v1, crossing_cpl30=None,
                known_cpl20_crossing=known, shift_deg=None, verdict="REFUTE",
                note="no sign change between the bracket pair at cpl=30 -- cannot "
                     "interpolate a crossing; treated as REFUTE (crossing not "
                     "reproduced in this bracket).")
        else:
            crossing = float(found[0])
            shift = abs(crossing - known)
            a2_report[pair_name] = dict(
                theta0=th0, theta1=th1, v0=v0, v1=v1, crossing_cpl30=crossing,
                known_cpl20_crossing=known, shift_deg=shift,
                verdict=crossing_shift_verdict(shift))
    print("\n[(a2)] cpl=30 crossing interpolation vs known cpl=20 crossings:")
    for name, r in a2_report.items():
        print(f"  {name}: cpl30_crossing={r['crossing_cpl30']}  "
              f"known_cpl20={r['known_cpl20_crossing']:.4f}  shift={r['shift_deg']}  "
              f"VERDICT={r['verdict']}")

    # ================================================================== (b)
    b_report = {}
    for th in ANGLES:
        cpl30_m = r3_leg2[th]
        cpl20_leg1_m = native_leg1[th]
        cpl30_word = "NODE-UNRESOLVABLE" if not cpl30_m["floor_pass"] else classification_word(cpl30_m["ratio_k"])
        cpl20_leg1_word = "NODE-UNRESOLVABLE" if not cpl20_leg1_m["floor_pass"] else classification_word(cpl20_leg1_m["ratio_k"])
        cpl20_filed_word = classification_word(filed_cpl20[th]["ratio_k"])
        b_report[th] = dict(
            ratio_k_cpl30=cpl30_m["ratio_k"], class_cpl30=cpl30_word,
            ratio_k_cpl20_leg1=cpl20_leg1_m["ratio_k"], class_cpl20_leg1=cpl20_leg1_word,
            ratio_k_cpl20_filed=filed_cpl20[th]["ratio_k"], class_cpl20_filed=cpl20_filed_word,
            match_vs_leg1=bool(cpl30_word == cpl20_leg1_word),
            match_vs_filed=bool(cpl30_word == cpl20_filed_word),
        )
    print("\n[(b) PRIMARY] ratio_k classification, cpl=30 (Leg2) vs cpl=20 (primary "
          "comparator = Leg1 fresh STEPS=4200; filed exp-089/090 STEPS=2800 shown "
          "for context):")
    for th in ANGLES:
        r = b_report[th]
        print(f"  theta={th}: cpl30={r['class_cpl30']} (ratio_k={r['ratio_k_cpl30']:.4f})  "
              f"cpl20_leg1={r['class_cpl20_leg1']} (ratio_k={r['ratio_k_cpl20_leg1']:.4f})  "
              f"match_vs_leg1={r['match_vs_leg1']}  |  "
              f"cpl20_filed={r['class_cpl20_filed']} (ratio_k={r['ratio_k_cpl20_filed']:.4f})  "
              f"match_vs_filed={r['match_vs_filed']}")

    # ================================================================== (b2)
    b2_cells = []
    b2_report = {}
    for th in ANGLES:
        ratio = r3_leg2[th]["frac_p_abs"] / native_leg1[th]["frac_p_abs"]
        sign_r3 = r3_leg2[th]["p_g"] - r3_leg2[th]["p_c"] > 0
        sign_native = native_leg1[th]["p_g"] - native_leg1[th]["p_c"] > 0
        sign_match = sign_r3 == sign_native
        b2_cells.append((ratio, sign_match))
        b2_report[th] = dict(frac_p_abs_cpl20_leg1=native_leg1[th]["frac_p_abs"],
                              frac_p_abs_cpl30=r3_leg2[th]["frac_p_abs"],
                              ratio=ratio, sign_match=sign_match)
    b2_verdict = ratio_sign_verdict(b2_cells)
    print(f"\n[(b2) PRIMARY] frac_p_abs_R3/frac_p_abs_cpl20(Leg1) ratio+sign, "
          f"three census angles: VERDICT={b2_verdict}")
    for th in ANGLES:
        r = b2_report[th]
        print(f"  theta={th}: ratio={r['ratio']:.4f}  sign_match={r['sign_match']}")

    # ================================================================== (c1)
    c1_report = {}
    c1_all_confirm = True
    for key in PAIR_KEYS:
        for th in ANGLES:
            fresh = contrast[(key, th, STEPS_LEG1)]["C_empty"]
            ref_c_empty = per_theta_83_full[f"{th:.1f}"][f"{key}_Ce"]
            rel_dev = abs(fresh - ref_c_empty) / abs(ref_c_empty)
            verdict = rel_dev_verdict(rel_dev)
            c1_all_confirm = c1_all_confirm and (verdict == "CONFIRM")
            c1_report[f"{key}_{th}"] = dict(theta=th, key=key, fresh_steps4200=fresh,
                                             ref_steps2800=ref_c_empty, rel_dev=rel_dev,
                                             verdict=verdict)
    print(f"\n[(c1)] native-cpl STEPS=4200 vs exp-083's committed STEPS=2800 "
          f"C_empty, all 6 cells: all-CONFIRM={c1_all_confirm}")
    for k, r in sorted(c1_report.items()):
        print(f"  {k}: rel_dev={r['rel_dev']:.4%}  VERDICT={r['verdict']}")

    # ================================================================== (c2)
    c2_report = {}
    c2_all_confirm = True
    for key in PAIR_KEYS_R3:
        for th in SETTLE_ANGLES:
            c_6300 = contrast[(key, th, STEPS_LEG3)]["C"]
            c_4200 = contrast[(key, th, STEPS_LEG2)]["C"]
            ce_6300 = contrast[(key, th, STEPS_LEG3)]["C_empty"]
            ce_4200 = contrast[(key, th, STEPS_LEG2)]["C_empty"]
            rel_dev_C = abs(c_6300 - c_4200) / abs(c_4200)
            rel_dev_Ce = abs(ce_6300 - ce_4200) / abs(ce_4200)
            v_C = rel_dev_verdict(rel_dev_C)
            v_Ce = rel_dev_verdict(rel_dev_Ce)
            c2_all_confirm = c2_all_confirm and v_C == "CONFIRM" and v_Ce == "CONFIRM"
            c2_report[f"{key}_{th}"] = dict(
                theta=th, key=key, C_steps4200=c_4200, C_steps6300=c_6300,
                rel_dev_C=rel_dev_C, verdict_C=v_C,
                C_empty_steps4200=ce_4200, C_empty_steps6300=ce_6300,
                rel_dev_C_empty=rel_dev_Ce, verdict_C_empty=v_Ce)
    print(f"\n[(c2)] R3-resolution settling, STEPS=6300 vs 4200 at cpl=30, "
          f"both angles both configs (article leg C AND empty leg C_empty, "
          f"'both legs' per NOTES.md): all-CONFIRM={c2_all_confirm}")
    for k, r in sorted(c2_report.items()):
        print(f"  {k}: rel_dev(C)={r['rel_dev_C']:.4%} [{r['verdict_C']}]  "
              f"rel_dev(C_empty)={r['rel_dev_C_empty']:.4%} [{r['verdict_C_empty']}]")

    # ================================================================== (d)
    with open(EXP090_RESULTS) as f:
        j090 = json.load(f)
    q7 = j090["q7_disclosure"]
    margin_4200 = native_leg1[37.2]["margin"]
    print(f"\n[(d)] 37.2deg resolved-gate noise-floor margin at STEPS=4200 (Leg1, "
          f"freshly computed): {margin_4200:.6f}x")
    print(f"  cited STEPS=2800 figure: exp-090 results.json::q7_disclosure."
          f"recomputed_resolved_margin = {q7['recomputed_resolved_margin']:.6f}x "
          f"(prior_filed_resolved_margin_str={q7['prior_filed_resolved_margin_str']!r}, "
          f"itself computed by exp-090 from exp-089's own persisted thermo/box_dev "
          f"primitives -- exp-089's own results.json does not carry a precomputed "
          f"field for this quantity)")

    # R14(a)-style smoothness across the 5 cpl=30 angles (37.2,40.2,40.4,41.4,41.6)
    bracket_5pt = {
        37.2: (r3_leg2[37.2], STEPS_LEG2), 40.2: (r3_leg2[40.2], STEPS_LEG2),
        40.4: (r3_leg4[40.4], STEPS_LEG4), 41.4: (r3_leg2[41.4], STEPS_LEG2),
        41.6: (r3_leg4[41.6], STEPS_LEG4),
    }
    sorted_bracket_angles = sorted(bracket_5pt)
    smoothness = {"C40_R3": [], "G40_R3": []}
    r14a_pass = True
    for key, p_field in (("C40_R3", "p_c"), ("G40_R3", "p_g")):
        vals = [(th, bracket_5pt[th][0][p_field]) for th in sorted_bracket_angles]
        for i in range(1, len(vals)):
            th_prev, v_prev = vals[i - 1]
            th_cur, v_cur = vals[i]
            tol = NOISE_MULT * 0.02 * v_prev
            ok = bool(v_cur >= v_prev - tol)
            smoothness[key].append(dict(theta_prev=th_prev, theta_cur=th_cur,
                                         v_prev=v_prev, v_cur=v_cur, ok=ok))
            if not ok:
                r14a_pass = False
    print(f"\n[(d)] R14(a)-style smoothness gate, p_abs_w across 5 cpl=30 angles "
          f"(37.2,40.2,40.4,41.4,41.6): PASS={r14a_pass}")
    for key in ("C40_R3", "G40_R3"):
        for step in smoothness[key]:
            flag = "" if step["ok"] else "  <<< NON-MONOTONIC"
            print(f"  {key}: {step['theta_prev']}->{step['theta_cur']}  "
                  f"{step['v_prev']:.6e}->{step['v_cur']:.6e}{flag}")

    ordering_cpl20 = (native_leg1[37.2]["frac_contrast"] > native_leg1[40.2]["frac_contrast"]
                       > native_leg1[41.4]["frac_contrast"])
    ordering_cpl30 = (r3_leg2[37.2]["frac_contrast"] > r3_leg2[40.2]["frac_contrast"]
                       > r3_leg2[41.4]["frac_contrast"])
    print(f"\n[(d)] ordering check frac_contrast(37.2)>frac_contrast(40.2)>"
          f"frac_contrast(41.4): cpl20(Leg1)={ordering_cpl20}  cpl30(Leg2)={ordering_cpl30}")

    # cross-reference (mandatory fix 10): a2 shift vs c2 settling residual, by angle
    shift_402 = a2_report["40.2-40.4"]["shift_deg"]
    shift_414 = a2_report["41.4-41.6"]["shift_deg"]
    resid_402 = max(c2_report["C40_R3_40.2"]["rel_dev_C"], c2_report["G40_R3_40.2"]["rel_dev_C"])
    resid_414 = max(c2_report["C40_R3_41.4"]["rel_dev_C"], c2_report["G40_R3_41.4"]["rel_dev_C"])
    larger_shift_angle = None
    if shift_402 is not None and shift_414 is not None:
        larger_shift_angle = 40.2 if shift_402 > shift_414 else 41.4
    larger_resid_angle = 40.2 if resid_402 > resid_414 else 41.4
    cross_ref_consistent = (larger_shift_angle == larger_resid_angle) if larger_shift_angle else None
    print(f"\n[cross-reference, mandatory fix 10] larger (a2) crossing shift at "
          f"{larger_shift_angle}deg; larger (c2) settling residual (rel_dev(C), max "
          f"of both configs) at {larger_resid_angle}deg "
          f"(40.2:{resid_402:.4%}, 41.4:{resid_414:.4%}); "
          f"directionally consistent={cross_ref_consistent}")

    # ---------------------------------------------------------------- persist
    def m2j(m):
        return {k: v for k, v in m.items()}

    out = dict(
        total_fdtd_calls=len(jobs), total_wall_time_s=total_wall,
        pair_keys=PAIR_KEYS, pair_keys_r3=PAIR_KEYS_R3,
        angles=ANGLES, settle_angles=SETTLE_ANGLES, bracket_angles=BRACKET_ANGLES,
        steps=dict(leg1=STEPS_LEG1, leg2=STEPS_LEG2, leg3=STEPS_LEG3, leg4=STEPS_LEG4),
        r13_floor_gate=dict(floor_frac=FLOOR_FRAC, rms_frac_contrast=rms,
                             n_window_points=n83, floor=floor),
        vacuum_footprint_check=vac_report, vac_pass=vac_pass,
        xi_pass=xi_pass, nonneg_pass=nonneg_pass,
        raw=dict(
            native_leg1_cpl20_steps4200={str(k): m2j(v) for k, v in native_leg1.items()},
            r3_leg2_cpl30_steps4200={str(k): m2j(v) for k, v in r3_leg2.items()},
            r3_leg3_cpl30_steps6300={str(k): m2j(v) for k, v in r3_leg3.items()},
            r3_leg4_cpl30_steps4200_bracket={str(k): m2j(v) for k, v in r3_leg4.items()},
        ),
        filed_cpl20_comparators_steps2800=filed_cpl20,
        a=dict(verdict=a_verdict, per_theta={str(k): v for k, v in a_report.items()}),
        a2=dict(crossings_cpl20_31pt_census=crossings_cpl20.tolist(),
                known_crossing_40=known_40, known_crossing_41=known_41,
                per_pair=a2_report),
        b=dict(per_theta={str(k): v for k, v in b_report.items()}),
        b2=dict(verdict=b2_verdict, per_theta={str(k): v for k, v in b2_report.items()}),
        c1=dict(all_confirm=c1_all_confirm, per_cell=c1_report),
        c2=dict(all_confirm=c2_all_confirm, per_cell=c2_report),
        d=dict(
            resolved_margin_steps4200_leg1=margin_4200,
            cited_steps2800_margin=q7,
            r14a_smoothness=dict(passed=r14a_pass, steps=smoothness),
            ordering_check=dict(cpl20_leg1=ordering_cpl20, cpl30_leg2=ordering_cpl30),
            cross_reference_mandatory_fix_10=dict(
                shift_40_2_40_4=shift_402, shift_41_4_41_6=shift_414,
                larger_shift_angle=larger_shift_angle,
                settling_residual_40_2=resid_402, settling_residual_41_4=resid_414,
                larger_residual_angle=larger_resid_angle,
                directionally_consistent=cross_ref_consistent,
            ),
        ),
        netd_disclaimer=("NETD is an instrument/detector threshold, not a human "
                          "perceptual one -- does NOT bear on constraint-3/4's "
                          "human-eye verdict. (Idealization 3)"),
        scope_note=("This cycle is pure instrument recalibration (T1 route N/A, "
                     "Checkpoint criterion 2 N/A) -- no phenomenon-mechanism claim, "
                     "REALIZABILITY_MEMO.md untouched. (Idealization 7)"),
        r3_article_geometry_note=(
            "build_article_r3's PEC-core radius (45=round(30*1.5)) and "
            "graded_black_shell r_in/r_out (45/117) are NEW this cycle -- the "
            "first-ever R3-resolution FDTD call that also builds the PAIR_PAD "
            "article. Not spelled out digit-by-digit in NOTES.md/"
            "phase1_proposal.md (only R_OUT's own R3 value is named there, "
            "Idealization 4); uniquely determined by the single R3_RATIO=1.5 "
            "scaling rule this whole design already applies to every other "
            "geometric constant, and required by Idealization 4's own 'same "
            "~2.34um physical radius' statement. See module docstring."),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
