"""exp-092 -- T28 Crossing Relocation & Caution-Zone Rebuild: Panel Iteration
69. Combines exp-091's own reconciled Rank 1-3 queue into one build, run in
Red Team's own mandated order (Rank 3 first, gating Rank 1's sigma_max):

  Rank 3 (FIRST, 12 calls) -- does an R3-rescale-corrected sigma_max
    (0.5 -> 1/3, holding cpl=30 fixed) contaminate the PRIMARY delta_scene/
    frac_contrast channel, not only p_abs_w/frac_p_abs (MATERIALS' own
    exp-091 Phase-5 self-review checked only the latter)? Verdict gates
    Rank 1's own sigma_max choice (see NOTES.md's branch rule).
  Rank 1 (SECOND, 28 calls) -- a data-justified wider net (seven new
    DENSE_ANGLES points) to locate the true cpl=30 delta_scene
    zero-crossings exp-091's own +-0.2deg bracket failed to bracket.
  Rank 2 (zero FDTD) -- rebuilds exp-090's own caution-zone/Firth fit under
    two counterfactual treatments of its n=7 dataset (DROP 41.4deg;
    RELABEL 41.4deg->Y=0), reusing exp-090's own committed functions
    verbatim.

Frozen spec: phase3_synthesis.md (Red Team's 7-item mandatory-fix docket,
all adopted, plus one Director-caught addition -- Rank 3's empty leg is
re-run fresh, not "reused," since no T28-family experiment persists raw
FDTD captures to disk; see phase3_synthesis.md Sec.2). Predictions
(NOTES.md R3/R3b/R1a/R1b/R1c/R2) committed to git strictly BEFORE this
file's first run (house discipline, non-negotiable).

Reuses experiments/091-.../run.py's own `dg`(=dg069)/`box_for_r3`/
`ref_for_r3`/`_run_sim_r3`/`build_article_r3`/`widths_direction_corrected`/
`_label`/`compute_floor`/`_profile`/`contrast_pair`/`ratio_sign_verdict`/
`classification_word`/`PEC_R_R3`/`R3_R_OUT_CELLS` VERBATIM, UNMODIFIED --
zero geometry retyped, zero `lab/` diff, zero diff to any frozen experiment
file. Reuses experiments/090-.../run.py's own `find_zero_crossings`/
`firth_logistic`/`naive_mle_diverges`/`auc` VERBATIM for Rank 2.

NEW code this cycle (all additive):
  * `build_article_r3_sigma(sim, cx, cy, sigma_max)` -- generalizes exp-091's
    own `build_article_r3` to accept an explicit `sigma_max`, passed through
    to `materials.graded_black_shell`. Identical geometry (PEC core radius,
    shell r_in/r_out) -- only the shell's own conductivity parameter is
    exposed.
  * `_run_sim_r3_sigma(cfg, theta, steps, with_article, sigma_max)` --
    mirrors exp-091's own `_run_sim_r3` structure exactly, calling
    `build_article_r3_sigma` instead of the hardcoded-sigma `build_article_r3`.
    When `with_article=False`, `sigma_max` is never read (no article call of
    any kind touches the Sim object) -- the empty-leg field is therefore
    bit-independent of `sigma_max`, exactly as exp-091's own `_run_sim_r3`
    is (independently re-verified by this cycle's Red Team, phase2_redteam_
    audit.md Sec.0).
  * A generic `pair_metrics()` (module-level, parametrized by floor),
    generalizing the same-named function exp-091 defined INSIDE its own
    `main()` (not importable) -- identical formula, reusable.
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
    """House `_load()` pattern (exp-078..091's own idiom for cross-
    experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP090_DIR = os.path.join(ROOT, "experiments", "090-t28-floor-frac-threshold-fit")
EXP091_DIR = os.path.join(ROOT, "experiments", "091-t28-r3-resolution-denser-recheck")
EXP091_RESULTS = os.path.join(EXP091_DIR, "results.json")

exp091 = _load(os.path.join(EXP091_DIR, "run.py"), "_exp092_exp091")
exp090 = _load(os.path.join(EXP090_DIR, "run.py"), "_exp092_exp090")

dg = exp091.dg
box_for_r3 = exp091.box_for_r3
ref_for_r3 = exp091.ref_for_r3
widths_direction_corrected = exp091.widths_direction_corrected
_label = exp091._label
compute_floor = exp091.compute_floor
_profile = exp091._profile
contrast_pair = exp091.contrast_pair
ratio_sign_verdict = exp091.ratio_sign_verdict
classification_word = exp091.classification_word
find_zero_crossings = exp091.find_zero_crossings
PEC_R_R3 = exp091.PEC_R_R3
R3_R_OUT_CELLS = exp091.R3_R_OUT_CELLS
BOX_CLEARANCE_A_R3 = exp091.BOX_CLEARANCE_A_R3
BOX_CLEARANCE_B_R3 = exp091.BOX_CLEARANCE_B_R3
DX_M_R3 = exp091.DX_M_R3
L_GEOMETRIC_M_R3 = exp091.L_GEOMETRIC_M_R3
IRR_CENTRAL_W_CM2 = exp091.IRR_CENTRAL_W_CM2
K_AIR = exp091.K_AIR
DENSITY_SI_KG_M3, C_P_SI_J_KGK = exp091.DENSITY_SI_KG_M3, exp091.C_P_SI_J_KGK
EMISSIVITY = exp091.EMISSIVITY
T_AMBIENT_K = exp091.T_AMBIENT_K
NETD_BAND_K = exp091.NETD_BAND_K
XI_TOL = exp091.XI_TOL
NOISE_MULT = exp091.NOISE_MULT
RATIO_LOW, RATIO_HIGH = exp091.RATIO_LOW, exp091.RATIO_HIGH

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts, materials  # noqa: E402

PAIR_KEYS_R3 = ("C40_R3", "G40_R3")
STEPS_R3 = dg.R3_STEPS
assert STEPS_R3 == 4200

RANK3_ANGLES = [37.2, 40.2, 41.4]
assert RANK3_ANGLES == [dg.DENSE_ANGLES[6], dg.DENSE_ANGLES[21], dg.DENSE_ANGLES[27]]
SIGMA_NATIVE = 0.5
SIGMA_R3_CORRECTED = 78.0 / (2 * 117)
assert abs(SIGMA_R3_CORRECTED - 1.0 / 3.0) < 1e-12

RANK1_ANGLES = [39.2, 39.4, 39.6, 39.8, 40.0, 41.8, 42.0]
for _a in RANK1_ANGLES:
    assert _a in dg.DENSE_ANGLES, f"{_a} not on DENSE_ANGLES grid"

# ---------------------------------------------------------------- NEW code
def build_article_r3_sigma(sim, cx, cy, sigma_max):
    """Generalizes exp-091's own `build_article_r3` to accept an explicit
    `sigma_max` -- same two calls (pec_disk core + graded_black_shell),
    identical geometry, only the shell's conductivity parameter exposed."""
    materials.pec_disk(sim, cx, cy, PEC_R_R3)
    materials.graded_black_shell(sim, cx, cy, PEC_R_R3, R3_R_OUT_CELLS, sigma_max=sigma_max)


def _run_sim_r3_sigma(cfg, theta, steps, with_article, sigma_max):
    """Mirrors exp-091's own `_run_sim_r3` exactly; calls
    `build_article_r3_sigma` instead of the hardcoded-sigma
    `build_article_r3`. `sigma_max` is never read when `with_article=False`
    -- the empty-leg field is bit-independent of it, by construction."""
    sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.R3_CPL[600],
              courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
    if with_article:
        build_article_r3_sigma(sim, cfg["obj_x"], cfg["obj_y"], sigma_max)
    sim.add_line_source(cfg["src_x"], y_lo=cfg["y_lo"], y_hi=cfg["y_hi"],
                         angle_deg=theta, amplitude=1.0,
                         profile="plane", edge=dg.R3_TAPER)
    sim.run(steps)
    return sc.full_capture(sim)


def one_call(args):
    """Module-level (picklable) worker. args = (key, theta, with_article,
    steps, sigma_max) -- sigma_max is ignored when with_article=False."""
    key, th, art, steps, sigma_max = args
    cfg = dg.R3_CONFIGS[key]
    cap = _run_sim_r3_sigma(cfg, th, steps, art, sigma_max)
    return (key, th, art, steps, sigma_max, cap)


def cell_metrics(key, th, steps, cap_empty, cap_article):
    """Per-(config,angle,steps) primitives: widths (BOX_A/BOX_B, xi_ext),
    thermo (p_abs_w, ratio_abs_ext_raw), contrast (C, C_empty). Mirrors
    exp-091's own main()-inlined per-cell loop, generalized to a reusable
    function (this cycle's own architecture requires calling it twice --
    once for Rank 3, once for Rank 1 -- exp-091 never needed to)."""
    cfg = dg.R3_CONFIGS[key]
    box_a = box_for_r3(cfg, BOX_CLEARANCE_A_R3)
    box_b = box_for_r3(cfg, BOX_CLEARANCE_B_R3)
    ref = ref_for_r3(cfg)

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
        IRR_CENTRAL_W_CM2, sigma_ext_cells, DX_M_R3, ratio_abs_ext_clamped)
    regime = ts.mixed_length_scale_regime(
        p_abs_w=p["p_abs_w"], l_geometric_m=L_GEOMETRIC_M_R3,
        k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
        emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
        length_provenance="bench_construction")
    netd = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
    thermo = dict(sigma_ext_cells=sigma_ext_cells, ratio_abs_ext_raw=ratio_abs_ext_raw,
                  p_abs_w=p["p_abs_w"], dt_ss_full_K=regime["dt_ss_full_K"],
                  netd_classification=netd["classification"])

    empty_p = _profile(cap_empty, cfg)
    scene_p = _profile(cap_article, cfg)
    C, C_empty = contrast_pair(cfg, empty_p, scene_p, dg.R3_W_OBJ, dg.R3_GUARD_OUT, dg.R3_W_FLANK)

    return dict(xi_ext=xi_ext, box_dev=box_dev, thermo=thermo, C=C, C_empty=C_empty,
                sigma_abs_nonneg=bool(ba["sigma_abs"] >= 0))


def pair_metrics(c_cell, g_cell, floor):
    """Generalizes exp-091's own main()-inlined `pair_metrics` (not
    importable there) into a reusable, floor-parametrized function --
    identical formula."""
    p_c = c_cell["thermo"]["p_abs_w"]
    p_g = g_cell["thermo"]["p_abs_w"]
    frac_p_abs = abs(p_g - p_c) / p_c if p_c != 0 else float("inf")
    delta_scene = g_cell["C"] - c_cell["C"]
    frac_contrast = abs(delta_scene) / abs(c_cell["C"])
    ratio_k = frac_p_abs / frac_contrast if frac_contrast != 0 else float("inf")
    floor_pass = bool(frac_contrast >= floor)
    box_dev_max = max(c_cell["box_dev"]["ext"], c_cell["box_dev"]["abs"],
                       g_cell["box_dev"]["ext"], g_cell["box_dev"]["abs"])
    noise_floor = NOISE_MULT * box_dev_max * p_c
    delta_p_abs = abs(p_g - p_c)
    resolved = bool((delta_p_abs > noise_floor) and floor_pass)
    margin = (delta_p_abs / noise_floor) if noise_floor != 0 else float("inf")
    return dict(p_c=p_c, p_g=p_g, frac_p_abs=frac_p_abs, delta_scene=delta_scene,
                frac_contrast=frac_contrast, ratio_k=ratio_k, floor_pass=floor_pass,
                resolved=resolved, noise_floor=noise_floor, margin=margin,
                ratio_abs_ext_raw_c=c_cell["thermo"]["ratio_abs_ext_raw"],
                # Phase-5 fix (Red Team's final audit, THERMODYNAMICS' Phase-5
                # finding, also present unfixed in exp-091's own record):
                # netd_disposition is computed per cell above but was
                # previously dropped before reaching rank3_report/rank1_report
                # -- dt_ss_full_K_c is new here (netd_classification_c already
                # existed in this dict but was likewise never threaded onward).
                dt_ss_full_K_c=c_cell["thermo"]["dt_ss_full_K"],
                netd_classification_c=c_cell["thermo"]["netd_classification"])


def run_block(jobs):
    t0 = time.time()
    captures = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, sigma_max, cap) in enumerate(ex.map(one_call, jobs), 1):
            captures[(key, th, art, steps)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key:8s} theta={th:+06.2f} "
                  f"article={art} steps={steps} sigma_max={sigma_max}", flush=True)
    wall = time.time() - t0
    return captures, wall


def main():
    print("=" * 78)
    print("exp-092 -- T28 crossing relocation & caution-zone rebuild")
    print("=" * 78)

    # ---------------------------------------------------------------- R13 floor gate (desk, zero FDTD, unchanged)
    floor, rms, n83, per_theta_83_full = compute_floor()
    print(f"\n[R13 floor gate] RMS[frac_contrast], n={n83}: {rms:.6e}  "
          f"FLOOR={floor:.6e}  (unchanged, applied unrecomputed -- Idealization 6)")

    # ---------------------------------------------------------------- P1: vacuum footprint precondition
    vac_report = {}
    vac_pass = True
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
    print(f"\n[P1] vacuum-footprint precondition: PASS={vac_pass}")
    assert vac_pass, "P1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # =================================================================
    # RANK 3 -- FIRST, gates Rank 1's sigma_max (mandatory resequencing,
    # phase2_redteam_audit.md Sec.2 / phase3_synthesis.md Sec.3 item 1)
    # =================================================================
    print("\n" + "=" * 78)
    print("RANK 3 -- sigma_max PRIMARY-channel check (runs first)")
    print("=" * 78)

    rank3_jobs = []
    for key in PAIR_KEYS_R3:
        for th in RANK3_ANGLES:
            rank3_jobs.append((key, th, False, STEPS_R3, None))                    # empty (re-run fresh)
            rank3_jobs.append((key, th, True, STEPS_R3, SIGMA_R3_CORRECTED))       # article, sigma-corrected
    assert len(rank3_jobs) == 12
    print(f"\n{len(rank3_jobs)} FDTD calls queued (Rank 3)")
    rank3_captures, rank3_wall = run_block(rank3_jobs)
    print(f"Rank 3 wall time: {rank3_wall:.1f}s ({rank3_wall/60.0:.2f} min)")

    with open(EXP091_RESULTS) as f:
        j091 = json.load(f)
    filed_r3_leg2 = j091["raw"]["r3_leg2_cpl30_steps4200"]

    rank3_cells = {}
    empty_consistency = {}
    xi_pass = True
    nonneg_pass = True
    for key in PAIR_KEYS_R3:
        for th in RANK3_ANGLES:
            cap_empty = rank3_captures[(key, th, False, STEPS_R3)]
            cap_article = rank3_captures[(key, th, True, STEPS_R3)]
            cell = cell_metrics(key, th, STEPS_R3, cap_empty, cap_article)
            rank3_cells[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[Rank 3] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 3 FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 3] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 3 FAILED -- non-negativity gate; HALT"

    # empty-leg consistency check (Director fix #8) -- compare freshly
    # re-run C_empty against exp-091's own filed value at the same
    # (key, theta, cpl=30, STEPS=4200) cell.
    for key in PAIR_KEYS_R3:
        for th in RANK3_ANGLES:
            fresh_c_empty = rank3_cells[(key, th)]["C_empty"]
            filed_row = filed_r3_leg2[str(th)]
            filed_field = "C_empty_c" if key == "C40_R3" else "C_empty_g"
            filed_c_empty = filed_row[filed_field]
            match = bool(fresh_c_empty == filed_c_empty)
            empty_consistency[f"{key}_{th}"] = dict(
                fresh=fresh_c_empty, filed=filed_c_empty, bit_exact_match=match)
            flag = "" if match else "  <<< MISMATCH -- see NOTES.md consistency check"
            print(f"  [empty-leg consistency] {key} theta={th}: fresh={fresh_c_empty:.10e}  "
                  f"filed={filed_c_empty:.10e}{flag}")
    empty_consistency_all_match = all(v["bit_exact_match"] for v in empty_consistency.values())
    print(f"[Rank 3] empty-leg bit-exact reproduction of exp-091's own filed values: "
          f"ALL MATCH={empty_consistency_all_match}")

    # Rank 3 pair metrics (sigma-corrected) vs exp-091's own filed (sigma=0.5) values
    rank3_report = {}
    rank3_cells_for_verdict = []       # (ratio, sign_match) for delta_scene
    rank3_fc_cells_for_verdict = []    # (ratio, True) for frac_contrast
    rank3_pabs_cells = []              # (ratio, sign_match) for p_abs_w (R3b)
    for th in RANK3_ANGLES:
        c_cell = rank3_cells[("C40_R3", th)]
        g_cell = rank3_cells[("G40_R3", th)]
        pm = pair_metrics(c_cell, g_cell, floor)
        filed = filed_r3_leg2[str(th)]

        ds_ratio = pm["delta_scene"] / filed["delta_scene"] if filed["delta_scene"] != 0 else float("inf")
        ds_sign_match = (pm["delta_scene"] > 0) == (filed["delta_scene"] > 0)
        fc_ratio = pm["frac_contrast"] / filed["frac_contrast"] if filed["frac_contrast"] != 0 else float("inf")
        pabs_ratio = pm["p_c"] / filed["p_c"] if filed["p_c"] != 0 else float("inf")
        pabs_sign_match = (pm["p_g"] - pm["p_c"] > 0) == (filed["p_g"] - filed["p_c"] > 0)

        rank3_cells_for_verdict.append((ds_ratio, ds_sign_match))
        rank3_fc_cells_for_verdict.append((fc_ratio, True))
        rank3_pabs_cells.append((pabs_ratio, pabs_sign_match))

        rank3_report[th] = dict(
            sigma_corrected_delta_scene=pm["delta_scene"], filed_delta_scene=filed["delta_scene"],
            delta_scene_ratio=ds_ratio, delta_scene_sign_match=ds_sign_match,
            sigma_corrected_frac_contrast=pm["frac_contrast"], filed_frac_contrast=filed["frac_contrast"],
            frac_contrast_ratio=fc_ratio,
            sigma_corrected_p_abs_w_c=pm["p_c"], filed_p_abs_w_c=filed["p_c"],
            p_abs_w_ratio=pabs_ratio, p_abs_w_sign_match=pabs_sign_match,
            sigma_corrected_ratio_abs_ext_raw=pm["ratio_abs_ext_raw_c"],
            ratio_abs_ext_dev_from_anchor=abs(pm["ratio_abs_ext_raw_c"] - 0.51) / 0.51,
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"],
            sigma_corrected_dt_ss_full_K=pm["dt_ss_full_K_c"],
            sigma_corrected_netd_classification=pm["netd_classification_c"],
        )
    print("\n[Rank 3] sigma-corrected (1/3) vs as-filed (0.5) exp-091 comparison:")
    for th, r in sorted(rank3_report.items()):
        print(f"  theta={th}: delta_scene ratio={r['delta_scene_ratio']:.4f} "
              f"sign_match={r['delta_scene_sign_match']}  "
              f"frac_contrast ratio={r['frac_contrast_ratio']:.4f}  "
              f"p_abs_w ratio={r['p_abs_w_ratio']:.4f} sign_match={r['p_abs_w_sign_match']}  "
              f"ratio_abs_ext={r['sigma_corrected_ratio_abs_ext_raw']:.4f} "
              f"(dev from 0.51 anchor: {r['ratio_abs_ext_dev_from_anchor']:.2%})")

    # ---- (R3) verdict: worst-case across delta_scene + frac_contrast, all 3 angles
    ds_verdict = ratio_sign_verdict(rank3_cells_for_verdict)
    fc_verdict = ratio_sign_verdict(rank3_fc_cells_for_verdict)
    verdict_rank = {"REFUTE": 0, "NEITHER": 1, "CONFIRM": 2}
    r3_verdict = min([ds_verdict, fc_verdict], key=lambda v: verdict_rank[v])
    print(f"\n[R3 PRIMARY] delta_scene sub-verdict={ds_verdict}  frac_contrast sub-verdict={fc_verdict}  "
          f"OVERALL R3 VERDICT={r3_verdict}")

    # ---- (R3b) verdict: p_abs_w, non-gating
    r3b_verdict = ratio_sign_verdict(rank3_pabs_cells)
    print(f"[R3b PRIMARY, non-gating] p_abs_w verdict={r3b_verdict}")

    # ---- sigma_max branch rule for Rank 1 (pre-registered, NOTES.md)
    if r3_verdict == "CONFIRM":
        sigma_rank1 = SIGMA_NATIVE
        branch_reason = "R3 CONFIRM -> Rank 1 runs at sigma_max=0.5 (exp-091's own as-filed convention)"
    else:
        sigma_rank1 = SIGMA_R3_CORRECTED
        branch_reason = (f"R3 {r3_verdict} -> Rank 1 runs at sigma_max=1/3 (corrected"
                          f"{' -- REFUTE, material contamination confirmed' if r3_verdict == 'REFUTE' else ' -- NEITHER-triggered conservative default, disclosed as such, not a CONFIRM-level finding'})")
    print(f"\n[Sigma branch] {branch_reason}")

    # =================================================================
    # RANK 1 -- SECOND, wider-net crossing search at Rank-3-licensed sigma_max
    # =================================================================
    print("\n" + "=" * 78)
    print(f"RANK 1 -- wider-net crossing search (sigma_max={sigma_rank1:.6f})")
    print("=" * 78)

    rank1_jobs = []
    for key in PAIR_KEYS_R3:
        for th in RANK1_ANGLES:
            rank1_jobs.append((key, th, False, STEPS_R3, None))
            rank1_jobs.append((key, th, True, STEPS_R3, sigma_rank1))
    assert len(rank1_jobs) == 28
    print(f"\n{len(rank1_jobs)} FDTD calls queued (Rank 1)")
    rank1_captures, rank1_wall = run_block(rank1_jobs)
    print(f"Rank 1 wall time: {rank1_wall:.1f}s ({rank1_wall/60.0:.2f} min)")

    total_wall = rank3_wall + rank1_wall
    print(f"\ntotal wall time (Rank 3 + Rank 1): {total_wall:.1f}s ({total_wall/60.0:.2f} min)")

    rank1_cells = {}
    for key in PAIR_KEYS_R3:
        for th in RANK1_ANGLES:
            cap_empty = rank1_captures[(key, th, False, STEPS_R3)]
            cap_article = rank1_captures[(key, th, True, STEPS_R3)]
            cell = cell_metrics(key, th, STEPS_R3, cap_empty, cap_article)
            rank1_cells[(key, th)] = cell
            for xi in cell["xi_ext"].values():
                if xi > XI_TOL:
                    xi_pass = False
            if not cell["sigma_abs_nonneg"]:
                nonneg_pass = False
    print(f"\n[Rank 1] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "Rank 1 FAILED -- extinction-routes disagreement; HALT"
    print(f"[Rank 1] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "Rank 1 FAILED -- non-negativity gate; HALT"

    rank1_report = {}
    for th in RANK1_ANGLES:
        c_cell = rank1_cells[("C40_R3", th)]
        g_cell = rank1_cells[("G40_R3", th)]
        pm = pair_metrics(c_cell, g_cell, floor)
        rank1_report[th] = dict(
            delta_scene=pm["delta_scene"], frac_contrast=pm["frac_contrast"],
            ratio_k=pm["ratio_k"], floor_pass=pm["floor_pass"], resolved=pm["resolved"],
            frac_p_abs=pm["frac_p_abs"],
            classification=("NODE-UNRESOLVABLE" if not pm["floor_pass"] else classification_word(pm["ratio_k"])),
            dt_ss_full_K_c=pm["dt_ss_full_K_c"],
            netd_classification_c=pm["netd_classification_c"],
        )
    print("\n[Rank 1] per-angle results:")
    for th, r in sorted(rank1_report.items()):
        print(f"  theta={th}: delta_scene={r['delta_scene']:+.6e}  frac_contrast={r['frac_contrast']:.6e}  "
              f"ratio_k={r['ratio_k']:.4f}  class={r['classification']}  floor_pass={r['floor_pass']}")

    # ---- (R1a/R1b) crossing search: combine Rank-1's 7 new points with
    # exp-091's own 4 already-committed cpl=30 points (40.2,40.4,41.4,41.6)
    filed_r3_leg4 = j091["raw"]["r3_leg4_cpl30_steps4200_bracket"]
    combined = {}
    for th in RANK1_ANGLES:
        combined[th] = rank1_report[th]["delta_scene"]
    for th in RANK3_ANGLES:
        combined[th] = rank3_report[th]["sigma_corrected_delta_scene"] if sigma_rank1 == SIGMA_R3_CORRECTED else filed_r3_leg2[str(th)]["delta_scene"]
    for th_str, row in filed_r3_leg4.items():
        combined[float(th_str)] = row["delta_scene"]

    lower_window = sorted(t for t in combined if 39.0 <= t <= 40.6)
    upper_window = sorted(t for t in combined if 41.2 <= t <= 42.2)
    lower_vals = [combined[t] for t in lower_window]
    upper_vals = [combined[t] for t in upper_window]
    lower_crossings = find_zero_crossings(lower_window, lower_vals)
    upper_crossings = find_zero_crossings(upper_window, upper_vals)
    print(f"\n[R1a/R1b] lower window {lower_window}")
    print(f"          values {[f'{v:+.4e}' for v in lower_vals]}")
    print(f"          crossings found: {lower_crossings.tolist()}")
    print(f"[R1a/R1b] upper window {upper_window}")
    print(f"          values {[f'{v:+.4e}' for v in upper_vals]}")
    print(f"          crossings found: {upper_crossings.tolist()}")

    # Per NOTES.md's pre-registered (R1a): CONFIRM = a sign change in EITHER
    # window (AND/OR), each with at most one crossing (monotonic, not an
    # interior oscillation); NEITHER = a crossing found but either window
    # shows >1 (non-monotonic); REFUTE = no crossing anywhere.
    if len(lower_crossings) <= 1 and len(upper_crossings) <= 1:
        r1a_verdict = "CONFIRM" if (len(lower_crossings) + len(upper_crossings) >= 1) else "REFUTE"
    else:
        r1a_verdict = "NEITHER"
    print(f"\n[R1a PRIMARY] VERDICT={r1a_verdict}  "
          f"(lower crossings: {len(lower_crossings)}, upper crossings: {len(upper_crossings)})")

    known_40, known_41 = 40.26541960305772, 41.46090139413461
    # Phase-5 fix (Red Team's final audit, MATERIALS' Phase-5 finding):
    # persist the FULL per-window crossing list, not only crossings[0] --
    # find_zero_crossings can return more than one root per window (as it
    # does here, in the upper window), and a singular field silently drops
    # every crossing after the first from results.json even though it is
    # correctly counted (len(upper_crossings)) and printed above.
    r1b_report = dict(
        lower_crossing_cpl30=(float(lower_crossings[0]) if len(lower_crossings) else None),
        upper_crossing_cpl30=(float(upper_crossings[0]) if len(upper_crossings) else None),
        lower_crossings_cpl30_all=[float(x) for x in lower_crossings],
        upper_crossings_cpl30_all=[float(x) for x in upper_crossings],
        naive_extrapolation_lower=40.04, naive_extrapolation_upper=41.69,
        known_cpl20_lower=known_40, known_cpl20_upper=known_41,
    )
    if r1b_report["lower_crossing_cpl30"] is not None:
        r1b_report["shift_vs_cpl20_lower"] = r1b_report["lower_crossing_cpl30"] - known_40
        r1b_report["shift_vs_naive_lower"] = r1b_report["lower_crossing_cpl30"] - 40.04
    if r1b_report["upper_crossing_cpl30"] is not None:
        r1b_report["shift_vs_cpl20_upper"] = r1b_report["upper_crossing_cpl30"] - known_41
        r1b_report["shift_vs_naive_upper"] = r1b_report["upper_crossing_cpl30"] - 41.69
    print(f"[R1b diagnostic] {json.dumps(r1b_report, indent=2)}")

    # =================================================================
    # RANK 2 -- zero-FDTD caution-zone rebuild (desk only)
    # =================================================================
    print("\n" + "=" * 78)
    print("RANK 2 -- caution-zone rebuild under DROP/RELABEL treatments (zero FDTD)")
    print("=" * 78)

    j083_path = os.path.join(ROOT, "experiments", "083-t28-pad-article-full-power-retest", "results.json")
    with open(j083_path) as f:
        j083 = json.load(f)
    per_theta_83 = j083["per_theta"]

    def frac_contrast_of_83(key_th):
        row = per_theta_83[key_th]
        return abs(row["delta_scene"]) / abs(row["C40_C"])

    dataset = [
        (36.0, 2.642368e0), (37.2, 3.443295e0), (38.4, 9.075118e-1),
        (38.8, 3.873254e0), (40.2, 2.508201e1), (41.4, 2.880719e1), (41.8, 5.710203e0),
    ]
    FLOOR_090 = exp090.FLOOR
    rows = []
    for th, rk in dataset:
        fc = frac_contrast_of_83(f"{th:.1f}")
        m = fc / FLOOR_090
        y = 1 if rk > exp090.RATIO_HIGH else 0
        rows.append(dict(theta=th, margin=m, y=y))
    rows.sort(key=lambda r: r["margin"])

    def compute_zone(rows_subset):
        margins = np.array([r["margin"] for r in rows_subset])
        Y = np.array([r["y"] for r in rows_subset])
        n = len(rows_subset)
        pos_m, neg_m = margins[Y == 1], margins[Y == 0]
        zone_lo = float(np.max(pos_m)) if len(pos_m) else None
        zone_hi = float(np.min(neg_m)) if len(neg_m) else None
        a = exp090.auc(-pos_m, -neg_m) if len(pos_m) and len(neg_m) else None
        x = np.log10(margins)
        X = np.column_stack([np.ones(n), x])
        beta, n_iter, converged = exp090.firth_logistic(X, Y)
        m50 = (10 ** (-beta[0] / beta[1])) if converged else float("nan")
        naive_beta, diverged = exp090.naive_mle_diverges(X, Y)
        return dict(n=n, pos=int(Y.sum()), auc=a, zone=[zone_lo, zone_hi],
                    inverted=bool(zone_lo is not None and zone_hi is not None and zone_lo > zone_hi),
                    firth_beta=beta.tolist(), firth_converged=bool(converged), firth_m50=float(m50),
                    naive_mle_diverges=bool(diverged))

    rank2_original = compute_zone(rows)
    rank2_drop = compute_zone([r for r in rows if r["theta"] != 41.4])
    relabel_rows = [dict(r) for r in rows]
    for r in relabel_rows:
        if r["theta"] == 41.4:
            r["y"] = 0
    rank2_relabel = compute_zone(relabel_rows)

    print("\n[R2 PRIMARY] caution-zone rebuild:")
    for label, r in (("ORIGINAL", rank2_original), ("(i) DROP 41.4", rank2_drop),
                      ("(ii) RELABEL 41.4->0", rank2_relabel)):
        print(f"  {label}: n={r['n']} pos={r['pos']} AUC={r['auc']} zone={r['zone']} "
              f"inverted={r['inverted']} m50={r['firth_m50']:.6f} "
              f"naive_diverges={r['naive_mle_diverges']}")

    frozen_table = {
        "ORIGINAL": dict(n=7, pos=2, auc=1.0000, zone=[1.4764, 2.1709], inverted=False,
                          firth_m50=2.071013, naive_mle_diverges=True),
        "DROP": dict(n=6, pos=1, auc=1.0000, zone=[1.4764, 2.1709], inverted=False,
                     firth_m50=1.818061, naive_mle_diverges=True),
        "RELABEL": dict(n=7, pos=1, auc=0.8333, zone=[1.4764, 1.3095], inverted=True,
                        firth_m50=1.031717, naive_mle_diverges=False),
    }

    def sig4(x):
        return round(x, 4) if isinstance(x, float) else x

    r2_confirm = True
    for label, computed in (("ORIGINAL", rank2_original), ("DROP", rank2_drop), ("RELABEL", rank2_relabel)):
        frozen = frozen_table[label]
        if abs(computed["auc"] - frozen["auc"]) > 5e-4:
            r2_confirm = False
        if abs(computed["firth_m50"] - frozen["firth_m50"]) > 5e-4:
            r2_confirm = False
        if computed["inverted"] != frozen["inverted"]:
            r2_confirm = False
        if computed["naive_mle_diverges"] != frozen["naive_mle_diverges"]:
            r2_confirm = False
    r2_verdict = "CONFIRM" if r2_confirm else "REFUTE"
    print(f"\n[R2 PRIMARY] VERDICT={r2_verdict} (live recomputation vs. five-times-pre-verified frozen table)")

    # ---------------------------------------------------------------- persist
    out = dict(
        rank3_calls=12, rank1_calls=28, total_fdtd_calls=40,
        rank3_wall_s=rank3_wall, rank1_wall_s=rank1_wall, total_wall_time_s=total_wall,
        sigma_native=SIGMA_NATIVE, sigma_r3_corrected=SIGMA_R3_CORRECTED,
        r13_floor_gate=dict(floor=floor, rms_frac_contrast=rms, n_window_points=n83),
        vacuum_footprint_check=vac_report, vac_pass=vac_pass,
        xi_pass=xi_pass, nonneg_pass=nonneg_pass,
        empty_leg_consistency_check=empty_consistency,
        empty_leg_consistency_all_match=empty_consistency_all_match,
        rank3=dict(per_theta={str(k): v for k, v in rank3_report.items()},
                   delta_scene_sub_verdict=ds_verdict, frac_contrast_sub_verdict=fc_verdict,
                   verdict=r3_verdict, r3b_verdict=r3b_verdict),
        sigma_branch=dict(chosen_sigma_max=sigma_rank1, reason=branch_reason),
        rank1=dict(angles=RANK1_ANGLES, per_theta={str(k): v for k, v in rank1_report.items()},
                   verdict=r1a_verdict, crossing_report=r1b_report,
                   lower_window=lower_window, upper_window=upper_window),
        rank2=dict(original=rank2_original, drop_41_4=rank2_drop, relabel_41_4=rank2_relabel,
                   verdict=r2_verdict, frozen_comparator_table=frozen_table),
        netd_disclaimer=("NETD is an instrument/detector threshold, not a human "
                          "perceptual one -- does NOT bear on constraint-3/4's "
                          "human-eye verdict. (Idealization 3)"),
        scope_note=("This cycle is pure instrument recalibration (T1 route N/A, "
                     "Checkpoint criterion 2 N/A) -- no phenomenon-mechanism claim, "
                     "REALIZABILITY_MEMO.md untouched. (Idealization 7)"),
        sigma_branch_disclaimer=("A Rank-3 REFUTE or NEITHER-default reopens Rank 1's "
                                  "own net-placement logic as provisional for a future "
                                  "cycle -- resequencing fixes which article Rank 1 "
                                  "measures, not whether the net's own location is still "
                                  "correctly aimed under a corrected article. "
                                  "(Idealization 11)"),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")

    # ---- print-parity fix (mandatory-fix docket item 7): the three
    # disclosure fields above are also PRINTED here, not only written to
    # the results.json-bound dict -- closing exp-091's own never-printed
    # gap in the very cycle that names it.
    print(f"\n[disclosure] netd_disclaimer: {out['netd_disclaimer']}")
    print(f"[disclosure] scope_note: {out['scope_note']}")
    print(f"[disclosure] sigma_branch_disclaimer: {out['sigma_branch_disclaimer']}")

    return out


if __name__ == "__main__":
    main()
