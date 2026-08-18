"""exp-042 ERRATUM (Panel Iteration 19 Phase 5, Red Team + ELECTROMAGNETISM).
=============================================================================
Mandatory same-shift correction (Red Team's Tier-0 ruling, Phase 5): the
committed PRIMARY convention (`edge_diffraction_c_empty(...,obliquity=True)`)
applies the Rayleigh-Sommerfeld obliquity factor to each Huygens wavelet's
FIELD before the coherent sum -- the correct recipe for a Kirchhoff/RS
fixed-field APERTURE SCREEN, not for this bench's actual source
(`add_line_source` is a soft, ADDITIVE array of independently-driven line
currents, verified against `lab/fdtd2d.py:132-172,235-237`). The physically
correct recipe for that source model applies obliquity ONCE, via H
(Faraday's law), not squared via |E|^2 -- `edge_diffraction_c_empty_corrected`
and friends in `design_geometry.py`, added this erratum.

This script recomputes Block MAGNITUDE and Block BEAM under the corrected
convention and APPENDS the results to `results.json` under a new
"phase5_erratum" key -- the original "block_magnitude"/"block_beam" keys
and NOTES.md's own Phase 1-4 text are left UNMODIFIED (house convention,
T10's own precedent: flag and correct, never silently rewrite).

Zero new FDTD calls -- same already-committed exp-041 data, same engine-
verified geometry, a corrected reduction formula only.
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
RESULTS_PATH = os.path.join(HERE, "results.json")
C_THR = 0.005


def corrected_magnitude():
    with open(EXP041_RESULTS) as f:
        d041 = json.load(f)
    rows = d041["block_main"]["rows"]
    preds, meas, per_row = [], [], []
    for row in rows:
        th, lam = row["theta"], row["lambda_nm"]
        pred = dg.edge_diffraction_c_empty_corrected(th, dg.CPL[lam])
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
    per_lambda = {}
    for lam in dg.CPL:
        sub = [r for r in per_row if r["lambda_nm"] == lam]
        sa = sum(1 for r in sub if r["sign_match"])
        misses = [r["theta"] for r in sub if not r["sign_match"]]
        per_lambda[str(lam)] = {"sign_agree": sa, "n": len(sub), "miss_thetas": misses}
    return {"sign_agree": sign_agree, "n": 30, "r2_c1": r2_c1,
            "c_star": c_star, "r2_cstar": r2_cstar,
            "per_lambda": per_lambda, "rows": per_row}


def corrected_beam():
    rows = []
    for lam in (450, 600, 750):
        for theta0 in (36, 38, 40):
            for fwhm in (2, 5, 10, 20):
                ci = dg.beam_divergence_incoherent_corrected(theta0, fwhm, dg.CPL[lam])
                rows.append({"lambda_nm": lam, "theta0": theta0, "fwhm_deg": fwhm,
                             "C_incoherent": ci,
                             "incoherent_above_thr": bool(abs(ci) > C_THR)})
    n_above = sum(1 for r in rows if r["incoherent_above_thr"])
    worst = max(rows, key=lambda r: abs(r["C_incoherent"]))
    return {"rows": rows, "n": len(rows), "n_incoherent_above_thr_at_c1": n_above,
            "worst_cell": worst}


def cross_check_flip_counts(mag_committed_c_star, mag_corrected_c_star, beam_committed, beam_corrected):
    """How many of Block BEAM's 36 cells flip above C_thr when each
    convention's own best-fit c* is applied to its own self-consistent
    reading (Red Team's finding 3 cross-check)."""
    n_committed_flip = sum(1 for r in beam_committed["rows"]
                            if abs(r["C_incoherent"] * mag_committed_c_star) > C_THR)
    n_corrected_flip = sum(1 for r in beam_corrected["rows"]
                            if abs(r["C_incoherent"] * mag_corrected_c_star) > C_THR)
    return n_committed_flip, n_corrected_flip


def main():
    t0 = time.time()
    print("=== exp-042 ERRATUM: corrected single-obliquity-via-H convention ===")
    mag = corrected_magnitude()
    print(f"Block MAGNITUDE (corrected): sign={mag['sign_agree']}/30  "
          f"R2(c=1)={mag['r2_c1']:.4f}  c*={mag['c_star']:.4f}  R2(c*)={mag['r2_cstar']:.4f}")
    for lam, v in mag["per_lambda"].items():
        print(f"  {lam}nm: sign={v['sign_agree']}/{v['n']}  misses at theta={v['miss_thetas']}")

    beam = corrected_beam()
    print(f"\nBlock BEAM (corrected, incoherent, c=1): "
          f"{beam['n_incoherent_above_thr_at_c1']}/{beam['n']} above C_thr={C_THR}")
    print(f"  worst cell: {beam['worst_cell']}")

    worst_c1 = beam["worst_cell"]["C_incoherent"]
    flipped = worst_c1 * mag["c_star"]
    print(f"\n  worst cell x corrected c*={mag['c_star']:.4f} -> {flipped:+.6f}  "
          f"(|.|>{C_THR}: {abs(flipped) > C_THR})")

    # cross-check against the ORIGINAL (committed) convention's own numbers,
    # loaded from the already-committed results.json
    with open(RESULTS_PATH) as f:
        committed = json.load(f)
    mag_committed_c_star = committed["block_magnitude"]["conventions"]["flux_primary"]["c_star"]
    beam_committed_rows = committed["block_beam"]["rows"]
    committed_worst = max(beam_committed_rows, key=lambda r: abs(r["C_incoherent"]))
    committed_flipped = committed_worst["C_incoherent"] * mag_committed_c_star
    print(f"\n  [cross-check] committed convention worst cell "
          f"{committed_worst['C_incoherent']:+.6f} x its own c*={mag_committed_c_star:.4f} "
          f"-> {committed_flipped:+.6f}  (|.|>{C_THR}: {abs(committed_flipped) > C_THR})")

    n_committed_flip = sum(1 for r in beam_committed_rows
                            if abs(r["C_incoherent"] * mag_committed_c_star) > C_THR)
    n_corrected_flip = sum(1 for r in beam["rows"]
                            if abs(r["C_incoherent"] * mag["c_star"]) > C_THR)
    print(f"\n  full-grid flip count, c* applied to own convention: "
          f"committed={n_committed_flip}/36  corrected={n_corrected_flip}/36")

    erratum = {
        "panel_iteration": 19,
        "phase": 5,
        "author": "Red Team (numeric claim by ELECTROMAGNETISM, independently re-derived by Red Team and the Director)",
        "reason": "The committed PRIMARY convention (obliquity applied to E before |E|^2) "
                  "is the Kirchhoff/Rayleigh-Sommerfeld fixed-field-screen recipe, misapplied "
                  "to this bench's actual soft, additive current-array source. Faraday's law "
                  "for an array of independently-driven line currents gives Hy=cos(psi)*Ez/eta "
                  "-- obliquity enters ONCE, via H, not squared via E. See NOTES.md erratum "
                  "section and design_geometry.py's edge_diffraction_c_empty_corrected docstring.",
        "block_magnitude_corrected": mag,
        "block_beam_corrected": beam,
        "cross_check": {
            "committed_convention_worst_cell_x_own_c_star": committed_flipped,
            "corrected_convention_worst_cell_x_own_c_star": flipped,
            "committed_convention_full_grid_flip_count": n_committed_flip,
            "corrected_convention_full_grid_flip_count": n_corrected_flip,
            "note": "Both conventions, self-consistently applied (own c* to own c=1 reading), "
                    "flip at least the worst cell above C_thr. Only a cross-convention shortcut "
                    "(committed c=1 reading x corrected c*, or vice versa) avoids a flip -- not "
                    "a methodologically legitimate combination.",
        },
        "elapsed_s": time.time() - t0,
    }
    committed["phase5_erratum"] = erratum
    with open(RESULTS_PATH, "w") as f:
        json.dump(committed, f, indent=2)
    print(f"\nAppended phase5_erratum to {RESULTS_PATH} ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
