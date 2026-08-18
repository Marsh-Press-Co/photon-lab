"""exp-042 -- The Edge-Diffraction Magnitude Bridge (T21): measurement
harness.
=============================================================================
Panel Iteration 19 (lead: VISION SCIENCE, rotation; synthesis: Director,
post Red Team's PROCEED-WITH-MANDATORY-FIXES verdict -- see
design_geometry.py's module docstring and NOTES.md Phase 3 for the full
accepted/overridden record).

Two blocks, zero new FDTD calls (pure analytic/desk work over already-
committed data):

  Block MAGNITUDE  -- score `design_geometry.edge_diffraction_c_empty`
                      against all 30 of exp-041's Block MAIN rows
                      (results.json), under BOTH the naive (|E|^2) and
                      flux/obliquity (PRIMARY) reductions.
  Block BEAM       -- VISION's beam-divergence/contamination-risk check:
                      incoherent (PRIMARY) and coherent (mandatory cross-
                      check, QUANTUM) angular-spread readings across a
                      lambda x theta0 x FWHM grid.

Predictions committed in NOTES.md BEFORE this file's first run (house
discipline, non-negotiable). No `lab/` change -- suite stays fast-stage
green (re-verified before results are read).
"""

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg

EXP041_RESULTS = os.path.join(HERE, "..", "041-t20-angle-audit", "results.json")

C_THR = 0.005                      # VISION's T2 photopic C_thr -- context only,
                                    # this leg scores no perceptual pass/fail


# ===================================================== Block MAGNITUDE
def block_magnitude():
    t0 = time.time()
    with open(EXP041_RESULTS) as f:
        d041 = json.load(f)
    rows = d041["block_main"]["rows"]
    assert len(rows) == 30, f"exp-041 Block MAIN row count drift: {len(rows)}"

    out = {"conventions": {}, "per_lambda": {}}
    for obliquity, label in [(True, "flux_primary"), (False, "naive_secondary")]:
        preds, meas, per_row = [], [], []
        for row in rows:
            th, lam = row["theta"], row["lambda_nm"]
            pred = dg.edge_diffraction_c_empty(th, dg.CPL[lam], obliquity)
            preds.append(pred)
            meas.append(row["C_empty"])
            per_row.append({"theta": th, "lambda_nm": lam,
                             "measured": row["C_empty"], "predicted": pred,
                             "sign_match": bool(np.sign(pred) == np.sign(row["C_empty"]))})
        preds = np.array(preds)
        meas = np.array(meas)
        sign_agree = int(np.sum(np.sign(preds) == np.sign(meas)))
        ss_tot = float(np.sum((meas - meas.mean()) ** 2))
        r2_c1 = 1.0 - float(np.sum((meas - preds) ** 2)) / ss_tot
        c_star = float(np.sum(meas * preds) / np.sum(preds ** 2))
        r2_cstar = 1.0 - float(np.sum((meas - c_star * preds) ** 2)) / ss_tot
        out["conventions"][label] = {
            "sign_agree": sign_agree, "n": 30,
            "r2_c1": r2_c1, "c_star": c_star, "r2_cstar": r2_cstar,
            "rows": per_row,
        }
        if obliquity:
            for lam in dg.CPL:
                sub = [r for r in per_row if r["lambda_nm"] == lam]
                sa = sum(1 for r in sub if r["sign_match"])
                out["per_lambda"][str(lam)] = {"sign_agree": sa, "n": len(sub)}
    out["elapsed_s"] = time.time() - t0
    return out


# ===================================================== Block BEAM
def block_beam():
    t0 = time.time()
    rows = []
    for lam in (450, 600, 750):
        for theta0 in (36, 38, 40):
            for fwhm in (2, 5, 10, 20):
                ci = dg.beam_divergence_incoherent(theta0, fwhm, dg.CPL[lam])
                cc = dg.beam_divergence_coherent(theta0, fwhm, dg.CPL[lam])
                rows.append({
                    "lambda_nm": lam, "theta0": theta0, "fwhm_deg": fwhm,
                    "C_incoherent": ci, "C_coherent": cc,
                    "incoherent_above_thr": bool(abs(ci) > C_THR),
                    "coherent_above_thr": bool(abs(cc) > C_THR),
                })
    n_incoh_above = sum(1 for r in rows if r["incoherent_above_thr"])
    n_coh_above = sum(1 for r in rows if r["coherent_above_thr"])
    return {"rows": rows, "n": len(rows), "C_thr": C_THR,
            "n_incoherent_above_thr": n_incoh_above,
            "n_coherent_above_thr": n_coh_above,
            "elapsed_s": time.time() - t0}


# ===================================================== driver
def main():
    t0 = time.time()
    print("=== exp-042: The Edge-Diffraction Magnitude Bridge (T21) ===")
    print("Block MAGNITUDE: scoring against exp-041's own 30 Block MAIN rows...")
    mag = block_magnitude()
    for label, c in mag["conventions"].items():
        print(f"  [{label}] sign_agree={c['sign_agree']}/{c['n']}  "
              f"R2(c=1)={c['r2_c1']:.4f}  c*={c['c_star']:.4f}  R2(c*)={c['r2_cstar']:.4f}")
    for lam, v in mag["per_lambda"].items():
        print(f"    {lam}nm (flux): sign_agree={v['sign_agree']}/{v['n']}")

    print("\nBlock BEAM: incoherent vs coherent angular-spread readings "
          f"(C_thr={C_THR})...")
    beam = block_beam()
    print(f"  {beam['n']} (lambda,theta0,FWHM) cells: "
          f"{beam['n_incoherent_above_thr']} incoherent above C_thr, "
          f"{beam['n_coherent_above_thr']} coherent above C_thr")
    for r in beam["rows"]:
        flag_i = "  <-- INCOH ABOVE C_thr" if r["incoherent_above_thr"] else ""
        flag_c = "  <-- COH ABOVE C_thr" if r["coherent_above_thr"] else ""
        print(f"    lam={r['lambda_nm']} th0={r['theta0']} fwhm={r['fwhm_deg']:2d}: "
              f"incoh={r['C_incoherent']:+.5f}{flag_i}   coh={r['C_coherent']:+.5f}{flag_c}")

    results = {
        "experiment": "042-t21-magnitude-bridge",
        "panel_iteration": 19,
        "lead_seat": "VISION SCIENCE",
        "director_synthesis": "Red Team PROCEED-WITH-MANDATORY-FIXES, all 8 fixes adopted, none overridden",
        "geometry": {"NY": dg.NY, "ABSORB": dg.ABSORB, "SRC_X": dg.SRC_X,
                     "PLANE_X": dg.PLANE_X, "D_SP": dg.D_SP, "OBJ_Y": dg.OBJ_Y,
                     "A": dg.A, "R_EDGE": dg.R_EDGE, "R_OUT": dg.R_OUT},
        "obliquity_range": {"object_window": dg.OBLIQUITY_RANGE_OBJ,
                             "flank_window": dg.OBLIQUITY_RANGE_FLANK},
        "kr_validity": {str(lam): [dg._KR_MIN[lam], dg._KR_MAX[lam]] for lam in dg.CPL},
        "causal_transit_margin_periods": {str(lam): dg.MARGIN_PERIODS[lam] for lam in dg.CPL},
        "block_magnitude": mag,
        "block_beam": beam,
        "total_elapsed_s": time.time() - t0,
    }
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nWrote {out_path} ({time.time()-t0:.1f}s total)")


if __name__ == "__main__":
    main()
