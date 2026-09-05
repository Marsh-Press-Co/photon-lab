"""exp-112 Phase 4 analysis: loads chunk_runner.py's own r=156/cpl=25
captures, verifies the implementation self-consistency identity
(sum(sigma_scat_per_bin) == sigma_scat, angular_scattered_pattern's own
docstring identity, reused unmodified), recomputes the named bin
(-146.25deg, margin=32) via classify_item_i_local (imported from
experiments/110-.../run.py, UNMODIFIED -- the same K=3/median
mirror-pooled-floor instrument that read this bin UNRESOLVED-BY-
CONSTRUCTION at cpl=20), and applies this cycle's own pre-registered
classify_resolution_check() (run.py, this directory) to the result.

Zero new machinery beyond what run.py/chunk_runner.py declare. NOT
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

import run as R110  # noqa: E402  (experiments/110-.../run.py -- classify_item_i_local, etc.)
import run112 as R  # noqa: E402  (this directory's own run112.py)
import chunk_runner112 as CR  # noqa: E402  (this directory's own chunk_runner112.py)
from lab import sections as sc  # noqa: E402

# Phase-2 Red Team audit Docket Fix 1 (R29): see chunk_runner112.py's own
# identical comment for the run.py/run.py collision this addresses.
assert R is not R110, "R29: run112 (R) must be a distinct module object from exp-110's run (R110)"
assert hasattr(R, "geom_fixedabs_cpl"), "R29: R must be exp-112's own run112.py, not exp-110's run.py"

# SECOND INSTANCE of the identical R29 collision shape, found at Phase 4
# (not Phase 2): experiments/110-.../ ALSO has its own chunk_runner.py, and
# this file's own sys.path insertion order (HERE inserted before ROOT before
# the exp-110 dir, each via insert(0, ...), so exp-110's dir ends up FIRST)
# made a bare `import chunk_runner as CR` resolve to exp-110's own module,
# not this directory's -- CR.SCRATCH silently pointed at exp-110's own
# scratch dir, which never received this cycle's real cpl=25 captures, so
# `have(...)` returned False even after all three scenes genuinely
# completed. Confirmed by direct execution: `python3 analyze.py` printed
# the correct-looking-but-wrong "captures not yet complete" message with
# all three done.pkl files genuinely present at exp-112's own SCRATCH.
# Fixed identically to Fix 1: renamed this directory's own chunk_runner.py
# -> chunk_runner112.py (no cross-directory basename collision possible),
# executed identity assertion added below. Recorded in NOTES.md's own
# Result section for Phase 5 to adjudicate whether this constitutes R29's
# own "second instance, fires Checkpoint 4" clause or is the SAME founding
# instance's own second, previously-undiscovered manifestation (this
# cycle's own Phase-1 draft introduced BOTH collisions; Phase 2 only
# exercised as far as the first one before crashing) -- not decided here.
EXP110_DIR_NAME = "110-t28-item-i-local-norm-and-controls"
assert EXP110_DIR_NAME not in os.path.dirname(CR.__file__), (
    "R29 (2nd instance): chunk_runner112 (CR) must be THIS directory's own "
    "module, not exp-110's chunk_runner.py")


def load(r, cpl, which):
    path = os.path.join(CR.SCRATCH, f"r{r}_cpl{cpl}_{which}_done.pkl")
    with open(path, "rb") as f:
        import pickle
        return pickle.load(f)


def have(r, cpl, which):
    return os.path.exists(os.path.join(CR.SCRATCH, f"r{r}_cpl{cpl}_{which}_done.pkl"))


def analyze_r156_cpl25():
    de = load(156, R.CPL_TARGET, "empty")
    dh = load(156, R.CPL_TARGET, "hollow")
    dp = load(156, R.CPL_TARGET, "peccored")
    g = de["g"]
    cap_e = de["cap"]
    cap_h = dh["cap"]
    cap_p = dp["cap"]
    box_a = g["box_a"]
    ref = g["ref"]

    # ---- implementation self-consistency identity (must PASS before the
    # named-bin comparison is trusted -- angular_scattered_pattern's own
    # docstring identity, reused unmodified, both articles)
    w_p = sc.widths(cap_p, cap_e, box_a, ref)
    w_h = sc.widths(cap_h, cap_e, box_a, ref)
    centers_p, pat_p = sc.angular_scattered_pattern(cap_p, cap_e, box_a, ref)
    centers_h, pat_h = sc.angular_scattered_pattern(cap_h, cap_e, box_a, ref)
    rel_dev_p = abs(float(np.sum(pat_p)) - w_p["sigma_scat"]) / abs(w_p["sigma_scat"])
    rel_dev_h = abs(float(np.sum(pat_h)) - w_h["sigma_scat"]) / abs(w_h["sigma_scat"])
    repro_ok = bool(rel_dev_p < 1e-9 and rel_dev_h < 1e-9)

    bin_centers_deg = centers_p.tolist()
    named_idx = int(np.argmin(np.abs(np.array(bin_centers_deg) - R.NAMED_BIN_DEG)))

    pat_delta = pat_p - pat_h
    local_diag = R110.classify_item_i_local(156, R.MARGIN, pat_p, pat_h, pat_delta)

    named_at_idx = dict(
        deg=bin_centers_deg[named_idx],
        peccored=float(pat_p[named_idx]),
        hollow=float(pat_h[named_idx]),
        delta=float(pat_delta[named_idx]),
        resolved=local_diag["resolved"][named_idx],
        local_snr_peccored=local_diag["local_snr_peccored"][named_idx],
        local_snr_hollow=local_diag["local_snr_hollow"][named_idx],
        floor=local_diag["floor"],
    )

    resolution_check = R.classify_resolution_check(
        pat_delta, named_at_idx["peccored"], named_at_idx["hollow"], named_at_idx)

    # Phase-2 Red Team audit Docket Fix 6 (recommended, THERMODYNAMICS' own
    # finding): persist sigma_abs/sigma_ext for both captures -- already
    # computed above via sc.widths(), previously discarded. Not load-bearing
    # for this cycle's own scored checks (T1 N/A); needed by any future
    # cycle attempting a genuinely physical, not merely statistical,
    # interpretation of the named bin's own deviation.
    energy_ledger = dict(
        peccored=dict(sigma_scat=w_p["sigma_scat"], sigma_abs=w_p["sigma_abs"], sigma_ext=w_p["sigma_ext"]),
        hollow=dict(sigma_scat=w_h["sigma_scat"], sigma_abs=w_h["sigma_abs"], sigma_ext=w_h["sigma_ext"]))

    return dict(
        r=156, cpl=R.CPL_TARGET,
        geom=g,
        repro_ok=repro_ok, rel_dev_peccored=rel_dev_p, rel_dev_hollow=rel_dev_h,
        bin_centers_deg=bin_centers_deg, named_idx=named_idx,
        named_bin=named_at_idx, local_diag_margin32=local_diag,
        resolution_check=resolution_check, energy_ledger=energy_ledger,
        pattern_peccored=pat_p.tolist(), pattern_hollow=pat_h.tolist(), pattern_delta=pat_delta.tolist(),
        baseline=dict(peccored=R.BASELINE_PECCORED, hollow=R.BASELINE_HOLLOW,
                      delta=R.BASELINE_DELTA, floor=R.BASELINE_FLOOR,
                      local_snr_peccored=R.BASELINE_SNR_PECCORED,
                      local_snr_hollow=R.BASELINE_SNR_HOLLOW,
                      resolved=R.BASELINE_RESOLVED, local_rel=R.BASELINE_LOCAL_REL),
        total_wall_s=dict(empty=CR.total_wall_time(156, R.CPL_TARGET, "empty"),
                           hollow=CR.total_wall_time(156, R.CPL_TARGET, "hollow"),
                           peccored=CR.total_wall_time(156, R.CPL_TARGET, "peccored")))


if __name__ == "__main__":
    geom_check = R.verify_geometry_identity()
    print(f"verify_geometry_identity: pass_={geom_check['pass_']}")
    if not geom_check["pass_"]:
        print(json.dumps(geom_check, indent=2))
        raise SystemExit("HALT: geom_fixedabs_cpl does not reduce to R.geom_fixedabs at cpl==20")

    if not (have(156, R.CPL_TARGET, "empty") and have(156, R.CPL_TARGET, "hollow")
            and have(156, R.CPL_TARGET, "peccored")):
        print("r=156/cpl=25 captures not yet complete; run chunk_runner.py for "
              "empty/hollow/peccored at r=156, cpl=25 first.")
        raise SystemExit(0)

    row = analyze_r156_cpl25()
    n_fdtd_calls = 3
    total_wall_s = sum(row["total_wall_s"].values())

    print(json.dumps({k: v for k, v in row.items() if k not in ("geom", "local_diag_margin32")},
                      indent=2, default=str))
    print(f"\nreproduction/self-consistency precondition: {'PASS' if row['repro_ok'] else 'FAIL'}")
    print(f"named bin resolution check: {row['resolution_check']}")

    predictions_text = R.build_predictions_text()
    assert R.DISCLAIMER in predictions_text

    named_bin_summary = (
        f"deg={row['named_bin']['deg']}, cpl=25 peccored={row['named_bin']['peccored']:.6e}, "
        f"hollow={row['named_bin']['hollow']:.6e}, delta={row['named_bin']['delta']:.6e}, "
        f"resolved={row['named_bin']['resolved']}, "
        f"local_snr_peccored={row['named_bin']['local_snr_peccored']}, "
        f"local_snr_hollow={row['named_bin']['local_snr_hollow']} -- "
        f"Check A: {row['resolution_check']['check_a']}; "
        f"Check B: {row['resolution_check']['check_b']}; "
        f"Check C (neighbor corr): {row['resolution_check']['check_c']}")
    result_text = R.build_result_text(
        n_fdtd_calls=n_fdtd_calls, total_wall_s=total_wall_s,
        geom_ok=geom_check["pass_"], repro_ok=row["repro_ok"],
        named_bin_result=named_bin_summary,
        wall_time_source="exp-112's own genuinely new r=156/cpl=25 spend, zero r=312 calls this cycle")
    assert R.DISCLAIMER in result_text

    out = dict(row, n_fdtd_calls=n_fdtd_calls, total_wall_s=total_wall_s,
               geom_identity=geom_check,
               predictions_text=predictions_text, result_text=result_text)
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWritten: {out_path}")
