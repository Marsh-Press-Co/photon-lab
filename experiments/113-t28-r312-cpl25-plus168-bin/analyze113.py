"""exp-113 Phase 4 analysis: loads chunk_runner113.py's own r=312/cpl=25
captures, verifies the implementation self-consistency identity
(sum(sigma_scat_per_bin) == sigma_scat, reused unmodified), recomputes the
named bin (168.75deg, margin=32) via classify_item_i_local (imported from
experiments/110-.../run.py, UNMODIFIED), and applies this cycle's own
pre-registered classify_resolution_check() (run113.py) -- Check A
unmodified, Check B normalized by CPL_RATIO (Item 4), Check C R30
null-calibrated (Item 3).

Zero new machinery beyond what run113.py/chunk_runner113.py declare. NOT
executed this phase (Phase 1 is proposal-only) -- committed so Phase 4
can run it unchanged against real captures.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check"))

import run as R110               # noqa: E402
import run112 as R112            # noqa: E402
import run113 as R               # noqa: E402
import chunk_runner113 as CR     # noqa: E402
from lab import sections as sc   # noqa: E402

assert R is not R110 and R is not R112, "R29: run113 (R) must be distinct from run110/run112"
EXP_DIR_NAME = os.path.basename(HERE)
assert os.path.basename(os.path.dirname(CR.__file__)) == EXP_DIR_NAME, (
    "R29 (2nd-instance shape, guarded pre-emptively): chunk_runner113 (CR) must be "
    "THIS directory's own module")


def load(r, cpl, which):
    path = os.path.join(CR.SCRATCH, f"r{r}_cpl{cpl}_{which}_done.pkl")
    with open(path, "rb") as f:
        import pickle
        return pickle.load(f)


def have(r, cpl, which):
    return os.path.exists(os.path.join(CR.SCRATCH, f"r{r}_cpl{cpl}_{which}_done.pkl"))


def analyze_r312_cpl25(baseline_delta_48):
    de = load(312, R.CPL_TARGET, "empty")
    dh = load(312, R.CPL_TARGET, "hollow")
    dp = load(312, R.CPL_TARGET, "peccored")
    g = de["g"]
    cap_e, cap_h, cap_p = de["cap"], dh["cap"], dp["cap"]
    box_a, ref = g["box_a"], g["ref"]

    w_p = sc.widths(cap_p, cap_e, box_a, ref)
    w_h = sc.widths(cap_h, cap_e, box_a, ref)
    centers_p, pat_p = sc.angular_scattered_pattern(cap_p, cap_e, box_a, ref)
    centers_h, pat_h = sc.angular_scattered_pattern(cap_h, cap_e, box_a, ref)
    rel_dev_p = abs(float(np.sum(pat_p)) - w_p["sigma_scat"]) / abs(w_p["sigma_scat"])
    rel_dev_h = abs(float(np.sum(pat_h)) - w_h["sigma_scat"]) / abs(w_h["sigma_scat"])
    repro_ok = bool(rel_dev_p < 1e-9 and rel_dev_h < 1e-9)

    bin_centers_deg = centers_p.tolist()
    named_idx = int(np.argmin(np.abs(np.array(bin_centers_deg) - R.NAMED_BIN_DEG)))
    assert named_idx == R.NAMED_BIN_IDX

    pat_delta = pat_p - pat_h
    local_diag = R110.classify_item_i_local(312, R.MARGIN, pat_p, pat_h, pat_delta)

    named_at_idx = dict(
        deg=bin_centers_deg[named_idx],
        peccored=float(pat_p[named_idx]), hollow=float(pat_h[named_idx]),
        delta=float(pat_delta[named_idx]), resolved=local_diag["resolved"][named_idx],
        local_snr_peccored=local_diag["local_snr_peccored"][named_idx],
        local_snr_hollow=local_diag["local_snr_hollow"][named_idx],
        floor=local_diag["floor"])

    resolution_check = R.classify_resolution_check(
        pat_delta, named_at_idx["peccored"], named_at_idx["hollow"], named_at_idx,
        np.asarray(baseline_delta_48))

    energy_ledger = dict(
        peccored=dict(sigma_scat=w_p["sigma_scat"], sigma_abs=w_p["sigma_abs"],
                      sigma_ext=w_p["sigma_ext"], sigma_ext_cross=w_p["sigma_ext_cross"]),
        hollow=dict(sigma_scat=w_h["sigma_scat"], sigma_abs=w_h["sigma_abs"],
                    sigma_ext=w_h["sigma_ext"], sigma_ext_cross=w_h["sigma_ext_cross"]))

    # R31/completeness fix (this cycle's own NOTES.md finding: exp-112's own
    # results.json clobbered its per-scene total_wall_s dict via a
    # `dict(row, total_wall_s=scalar)` merge that silently overwrote row's
    # own per-scene breakdown with the scalar sum) -- persisted under a
    # DIFFERENT key name here (`total_wall_s_by_scene`) so the same merge
    # pattern cannot recur.
    total_wall_s_by_scene = dict(
        empty=CR.total_wall_time(312, R.CPL_TARGET, "empty"),
        hollow=CR.total_wall_time(312, R.CPL_TARGET, "hollow"),
        peccored=CR.total_wall_time(312, R.CPL_TARGET, "peccored"))

    return dict(
        r=312, cpl=R.CPL_TARGET, geom=g,
        repro_ok=repro_ok, rel_dev_peccored=rel_dev_p, rel_dev_hollow=rel_dev_h,
        bin_centers_deg=bin_centers_deg, named_idx=named_idx,
        named_bin=named_at_idx, local_diag_margin32=local_diag,
        resolution_check=resolution_check, energy_ledger=energy_ledger,
        pattern_peccored=pat_p.tolist(), pattern_hollow=pat_h.tolist(),
        pattern_delta=pat_delta.tolist(),
        baseline=dict(peccored=R.BASELINE_PECCORED, hollow=R.BASELINE_HOLLOW,
                      delta=R.BASELINE_DELTA, floor=R.BASELINE_FLOOR,
                      local_snr_peccored=R.BASELINE_SNR_PECCORED,
                      local_snr_hollow=R.BASELINE_SNR_HOLLOW,
                      resolved=R.BASELINE_RESOLVED, local_rel=R.BASELINE_LOCAL_REL),
        total_wall_s_by_scene=total_wall_s_by_scene)


if __name__ == "__main__":
    geom_check = R.verify_geometry_identity()
    print(f"verify_geometry_identity: pass_={geom_check['pass_']}")
    if not geom_check["pass_"]:
        print(json.dumps(geom_check, indent=2))
        raise SystemExit("HALT: geom_fixedabs_cpl does not reduce to R.geom_fixedabs at cpl==20")

    if not (have(312, R.CPL_TARGET, "empty") and have(312, R.CPL_TARGET, "hollow")
            and have(312, R.CPL_TARGET, "peccored")):
        print("r=312/cpl=25 captures not yet complete; run chunk_runner113.py for "
              "empty/hollow/peccored at r=312, cpl=25 first.")
        raise SystemExit(0)

    baseline_delta_48 = R._BASELINE_R312["raw_patterns"][str(R.MARGIN)]["delta"]

    row = analyze_r312_cpl25(baseline_delta_48)
    n_fdtd_calls = 3
    total_wall_s = sum(row["total_wall_s_by_scene"].values())

    control_path = os.path.join(CR.SCRATCH, "r31_control.json")
    with open(control_path) as f:
        control = json.load(f)
    gate_path = os.path.join(CR.SCRATCH, f"r312_cpl{R.CPL_TARGET}_costgate.json")
    with open(gate_path) as f:
        gate = json.load(f)

    print(json.dumps({k: v for k, v in row.items() if k not in ("geom", "local_diag_margin32")},
                      indent=2, default=str))
    print(f"\nreproduction/self-consistency precondition: {'PASS' if row['repro_ok'] else 'FAIL'}")
    print(f"named bin resolution check: {row['resolution_check']}")

    predictions_text = R.build_predictions_text(control=control, gate=gate)
    assert R.DISCLAIMER in predictions_text

    rc = row["resolution_check"]
    named_bin_summary = (
        f"deg={row['named_bin']['deg']}, cpl=25 peccored={row['named_bin']['peccored']:.6e}, "
        f"hollow={row['named_bin']['hollow']:.6e}, delta={row['named_bin']['delta']:.6e}, "
        f"resolved={row['named_bin']['resolved']}, "
        f"local_snr_peccored={row['named_bin']['local_snr_peccored']}, "
        f"local_snr_hollow={row['named_bin']['local_snr_hollow']} -- "
        f"Check A: {rc['check_a']}; "
        f"Check B-normalized: {rc['check_b_normalized']['verdict']}; "
        f"Check B-raw: {rc['check_b_raw']['verdict']}; "
        f"Check C: corr={rc['check_c']['corr']}, "
        f"percentile_in_null={rc['check_c']['percentile_in_null']}, "
        f"supports_real_structure={rc['check_c']['supports_real_structure']}")
    result_text = R.build_result_text(
        n_fdtd_calls=n_fdtd_calls, total_wall_s=total_wall_s,
        geom_ok=geom_check["pass_"], repro_ok=row["repro_ok"],
        named_bin_result=named_bin_summary,
        wall_time_source="exp-113's own genuinely new r=312/cpl=25 spend, "
                          "R31-gated by a same-session control")
    assert R.DISCLAIMER in result_text

    out = dict(row, n_fdtd_calls=n_fdtd_calls, total_wall_s_all_scenes=total_wall_s,
               geom_identity=geom_check, r31_control=control, cost_gate=gate,
               predictions_text=predictions_text, result_text=result_text)
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWritten: {out_path}")
