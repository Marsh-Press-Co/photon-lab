"""Consolidates item 1 (hollow-vs-PEC-cored radial_absorbed_power delta)
and item 4 (article-scene numerator noise-floor check) from the
empty/article capture pickles `chunk_runner.py` produces. Panel
Iteration 84."""
import json
import os
import pickle
import sys

sys.path.insert(0, "/home/user/photon-lab/experiments/107-t28-delta-scene-r5-census-decision")
sys.path.insert(0, "/home/user/photon-lab")
import run as R  # noqa: E402
from lab import sections as sc  # noqa: E402

SCRATCH = "/tmp/claude-0/-home-user-photon-lab/6cf0c183-8ce9-5c5c-af14-ff173a23cef4/scratchpad/exp107"


def finalize_r(r):
    empty_path, article_path = (os.path.join(SCRATCH, f"r{r}_empty_done.pkl"),
                                 os.path.join(SCRATCH, f"r{r}_article_done.pkl"))
    with open(empty_path, "rb") as f:
        de = pickle.load(f)
    with open(article_path, "rb") as f:
        da = pickle.load(f)
    g = de["g"]
    cap_e, ez_e = de["cap"], de["ez"]
    cap_a, sigma_e_a, ez_a = da["cap"], da["sigma_e"], da["ez"]

    wa = sc.widths(cap_a, cap_e, g["box_a"], g["ref"])
    wb = sc.widths(cap_a, cap_e, g["box_b"], g["ref"])
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
    _, _, radial_total = sc.radial_absorbed_power(cap_a, sigma_e_a, g["CX"], g["CY"], g["R_COAT"])
    _, _, core_total = sc.radial_absorbed_power(cap_a, sigma_e_a, g["CX"], g["CY"], g["R_CORE"])
    core_frac = core_total / radial_total if radial_total else float("nan")
    abs_ext_ratio_hollow = wa["sigma_abs"] / wa["sigma_ext"]

    ledger_key = f"ledger_r{r}"
    abs_ext_ratio_pec = R.EXP106_RESULTS[ledger_key]["fixedabs"]["abs_ext_ratio"]
    delta = abs_ext_ratio_hollow - abs_ext_ratio_pec

    fg_article = R.floor_gate_window(ez_a, *g["behind"], f"r={r} window (hollow article, numerator)")

    return dict(r=r, sigma_abs=wa["sigma_abs"], sigma_ext=wa["sigma_ext"],
                abs_ext_ratio_hollow=abs_ext_ratio_hollow,
                abs_ext_ratio_pec_cored_exp106=abs_ext_ratio_pec,
                delta_abs_ext_ratio=delta, box_dev=box_dev,
                core_frac=core_frac, core_power=core_total, radial_total=radial_total,
                item1_pass=bool(abs(delta) <= 2e-4) and bool(box_dev <= 0.12),
                item1_confirms_band=bool(abs(delta) <= 2e-5),
                floor_gate_article_numerator=fg_article)


if __name__ == "__main__":
    for r in (156, 312):
        row = finalize_r(r)
        print(json.dumps(row, indent=2, default=str))
