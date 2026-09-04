"""Zero-FDTD analysis of exp-108's Tier-1 captures (chunk_runner.py's own
pickles): Gate P0, the reproduction precondition, items i/ii/iii, and the
ledger `closure` field. Panel Iteration 85."""
import json
import os
import pickle
import sys

import numpy as np

sys.path.insert(0, "/home/user/photon-lab/experiments/108-t28-reclassification-angular-pattern-batch")
sys.path.insert(0, "/home/user/photon-lab")
import run as R  # noqa: E402
from lab import sections as sc  # noqa: E402

SCRATCH = "/tmp/claude-0/-home-user-photon-lab/b3074561-e458-5939-8b7f-fe9684f9569f/scratchpad/exp108"


def load(r, which):
    path = os.path.join(SCRATCH, f"r{r}_{which}_done.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)


def closure_for(cap_article, cap_empty, sigma_e_article, g):
    """Same formula as exp-106's own ledger_check(): closure = |total -
    p_abs_box| / |p_abs_box|, at box_a."""
    w = sc.widths(cap_article, cap_empty, g["box_a"], g["ref"])
    _, _, total = sc.radial_absorbed_power(cap_article, sigma_e_article, g["CX"], g["CY"], g["R_COAT"])
    p_abs_box = w["sigma_abs"] * w["i_inc"]
    closure = abs(total - p_abs_box) / abs(p_abs_box) if p_abs_box else float("nan")
    return dict(sigma_abs=w["sigma_abs"], sigma_ext=w["sigma_ext"],
                abs_ext_ratio=w["sigma_abs"] / w["sigma_ext"],
                radial_total=total, p_abs_box=p_abs_box, closure=closure)


def analyze_r(r):
    de = load(r, "empty")
    dh = load(r, "hollow")
    dp = load(r, "peccored")
    g = de["g"]
    cap_e = de["cap"]
    cap_h, sigma_e_h, ez_h = dh["cap"], dh["sigma_e"], dh["ez"]
    cap_p, sigma_e_p, ez_p = dp["cap"], dp["sigma_e"], dp["ez"]

    gate_p0 = R.gate_p0(g)
    repro = R.reproduction_precondition(cap_p, cap_e, g)

    # ---------------------------------------------- item i: angular_scattered_pattern at 6 margins
    pattern_delta = {}
    pattern_peccored = {}
    pattern_hollow = {}
    sum_check = {}
    for m in R.MARGINS:
        box = g["margin_boxes"][m]
        centers_p, pat_p = sc.angular_scattered_pattern(cap_p, cap_e, box, g["ref"])
        centers_h, pat_h = sc.angular_scattered_pattern(cap_h, cap_e, box, g["ref"])
        w_p = sc.widths(cap_p, cap_e, box, g["ref"])
        w_h = sc.widths(cap_h, cap_e, box, g["ref"])
        sum_check[m] = dict(
            peccored=dict(sum_pattern=float(np.sum(pat_p)), sigma_scat=w_p["sigma_scat"],
                          rel_dev=abs(float(np.sum(pat_p)) - w_p["sigma_scat"]) / abs(w_p["sigma_scat"])),
            hollow=dict(sum_pattern=float(np.sum(pat_h)), sigma_scat=w_h["sigma_scat"],
                        rel_dev=abs(float(np.sum(pat_h)) - w_h["sigma_scat"]) / abs(w_h["sigma_scat"])),
        )
        pattern_peccored[m] = pat_p
        pattern_hollow[m] = pat_h
        pattern_delta[m] = pat_p - pat_h

    sum_check_pass = all(
        sum_check[m][fam]["rel_dev"] < 1e-9 for m in R.MARGINS for fam in ("peccored", "hollow"))

    item_i = R.classify_item_i(pattern_delta, pattern_peccored, r)
    item_i["sum_check_pass"] = sum_check_pass
    item_i["bin_centers_deg"] = sc.angular_scattered_pattern(cap_p, cap_e, g["margin_boxes"][32], g["ref"])[0].tolist()

    # ---------------------------------------------- item ii: absolute floor, 6-margin, detrended
    delta_values = []
    for m in R.MARGINS:
        box = g["margin_boxes"][m]
        w_p = sc.widths(cap_p, cap_e, box, g["ref"])
        w_h = sc.widths(cap_h, cap_e, box, g["ref"])
        delta_values.append(w_h["sigma_abs"] / w_h["sigma_ext"] - w_p["sigma_abs"] / w_p["sigma_ext"])
    fit = R.linear_fit_1_over_margin(R.MARGINS, delta_values)
    item_ii_verdict, boxA = R.classify_item_ii(r, fit["residual_std"])
    item_ii = dict(margins=list(R.MARGINS), delta_values=delta_values, fit=fit,
                   verdict=item_ii_verdict, delta_boxA=boxA)

    # ---------------------------------------------- item iii: numerator floor-gate, PEC-cored PRIMARY
    fg_article = sc_floor_gate_window(ez_p, *g["behind"], f"r={r} window (PEC-cored PRIMARY article, numerator)")
    hollow_reading = 0.18275 if r == 156 else 0.2675
    band = (hollow_reading - 0.05, hollow_reading + 0.05)
    item_iii = dict(frac_unresolved=fg_article["frac_unresolved"], band=band,
                    pass_=bool(band[0] <= fg_article["frac_unresolved"] <= band[1]),
                    floor_gate=fg_article)

    # ---------------------------------------------- closure, both articles
    closure_hollow = closure_for(cap_h, cap_e, sigma_e_h, g)
    closure_peccored = closure_for(cap_p, cap_e, sigma_e_p, g)

    return dict(r=r, gate_p0=gate_p0, reproduction_precondition=repro,
                item_i=item_i, item_ii=item_ii, item_iii=item_iii,
                closure_hollow=closure_hollow, closure_peccored=closure_peccored)


def sc_floor_gate_window(ez_scene, x_lo, x_hi, y_lo, y_hi, label, floor_frac=R.FLOOR_FRAC):
    """Byte-for-byte the same convention as exp-106/107's floor_gate_window()."""
    block = np.abs(ez_scene[x_lo:x_hi, y_lo:y_hi]) ** 2
    arr = block.ravel()
    rms = float(np.sqrt(np.mean(np.square(arr))))
    floor = floor_frac * rms
    n_unresolved = int(np.sum(arr < floor))
    print(f"  [floor gate: {label}] n={len(arr)} rms={rms:.6e} floor={floor:.6e} n_unresolved={n_unresolved}")
    return dict(rms=rms, floor=floor, n_unresolved=n_unresolved, frac_unresolved=n_unresolved / len(arr))


if __name__ == "__main__":
    results = {}
    for r in (156, 312):
        print(f"\n{'='*70}\nAnalyzing r={r}\n{'='*70}")
        row = analyze_r(r)
        results[f"r{r}"] = row
        print(f"gate_p0 pass={row['gate_p0']['pass_']}")
        print(f"reproduction_precondition pass={row['reproduction_precondition']['pass_']}")
        print(f"item_i verdict={row['item_i']['verdict']} sum_check_pass={row['item_i']['sum_check_pass']}")
        print(f"item_ii verdict={row['item_ii']['verdict']} residual_std={row['item_ii']['fit']['residual_std']:.4e} "
              f"|Delta_boxA|={row['item_ii']['delta_boxA']:.4e}")
        print(f"item_iii frac_unresolved={row['item_iii']['frac_unresolved']:.4f} pass={row['item_iii']['pass_']}")
        print(f"closure hollow={row['closure_hollow']['closure']:.6f} peccored={row['closure_peccored']['closure']:.6f}")

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analyze_output.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nWritten: {out_path}")
