"""exp-082 -- Tier 0 item 1: the x-wall realizable-admittance refit.
=============================================================================
PLAN.md Iteration-59 queue, Tier 0 item 1 (MATERIALS' restored item, exp-081
phase5_redteam_audit.md Sec 0.8/Sec 4/Sec 6): "restore or explicitly retire
the x-wall realizable-admittance refit (reuse
`d80.reflection_coefficient_vec_realizable` against the already-built
exp-075/exp-077 x-wall models, or state why their already-wide REFUTE
margins make that unnecessary)."

ZERO new FDTD calls. Reuses, does not reimplement:
  - experiments/077-.../pad_round_trip_model.py (the two-wall model, this
    sub-thread's own PRIMARY x-wall result): load_pair_geometries(),
    predicted_c_empty() [single-wall], predicted_c_empty_two_wall()
    [two-wall, primary], free_period_with_widening(), the real
    C40/G40/C80 dense-sweep data it already loads from
    experiments/076-.../results.json::headline.
  - experiments/080-.../validity_precheck.py (d80):
    reflection_coefficient_vec_realizable (mu_r=1, the realizable
    ordinary-dielectric family).

Substitutes ONLY the r(theta;ABSORB) profile source (matched -> realizable)
into the ALREADY-BUILT single-wall and two-wall predicted_c_empty
pipelines, and re-scores Test A (free-period rel_dev) / Test B (Pearson r^2)
exactly as exp-077's own main() does -- reporting whether either REFUTE
margin narrows enough to matter, not merely whether it "changes."
"""

import importlib.util
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP077_DIR = os.path.join(ROOT, "experiments", "077-t28-pad-round-trip-echo-model")
EXP080_DIR = os.path.join(ROOT, "experiments", "080-t28-y-wall-planewave-validity-precheck")

prm = _load(os.path.join(EXP077_DIR, "pad_round_trip_model.py"), "_exp082_prm")
d80 = _load(os.path.join(EXP080_DIR, "validity_precheck.py"), "_exp082_d80")

br = prm.br
CPL = prm.CPL


def compute_r_profiles_realizable(thetas):
    """SAME structure as prm.compute_r_profiles, only the admittance family
    differs: d80.reflection_coefficient_vec_realizable (mu_r=1) in place of
    br.reflection_coefficient (mu_r=ni, matched/unobtainium)."""
    omega600 = 2.0 * math.pi / CPL[600]
    n40 = br.n_profile_exact(br.nu_profile(br.damp_e_profile(40)), omega600)
    n80 = br.n_profile_exact(br.nu_profile(br.damp_e_profile(80)), omega600)
    r40 = d80.reflection_coefficient_vec_realizable(n40, thetas, CPL[600])
    r80 = d80.reflection_coefficient_vec_realizable(n80, thetas, CPL[600])
    return n40, n80, r40, r80


def score(thetas, real_delta, pred_delta, label):
    real_free = prm.free_period_with_widening(thetas, real_delta, f"real {label}")
    pred_free = prm.free_period_with_widening(thetas, pred_delta, f"model {label}")
    p_real = real_free["chosen"]["p_star_deg"]
    p_model = pred_free["chosen"]["p_star_deg"]
    rel_dev = abs(p_model - p_real) / p_real
    corr = float(np.corrcoef(pred_delta, real_delta)[0, 1])
    r2 = corr ** 2
    period_support = rel_dev <= 0.30
    period_refute = rel_dev > 1.00
    shape_support = r2 >= 0.30
    shape_refute = r2 <= 0.05
    if period_support and shape_support:
        combined = "SUPPORT"
    elif period_refute or shape_refute:
        combined = "REFUTE"
    else:
        combined = "INCONCLUSIVE"
    return dict(p_real_deg=p_real, p_model_deg=p_model, rel_dev=rel_dev,
                pearson_r=corr, r_squared=r2, combined=combined)


def main():
    print("=" * 78)
    print("exp-082 Tier-0 item 1 -- x-wall realizable-admittance (mu_r=1) refit")
    print("=" * 78)

    geoms = prm.load_pair_geometries()
    with open(prm.EXP076_RESULTS) as f:
        res76 = json.load(f)
    headline = res76["headline"]
    thetas = np.array(headline["theta"])
    real_c40 = np.array(headline["C40"])
    real_g40 = np.array(headline["G40"])
    real_c80 = np.array(headline["C80"])
    real_delta_pad = real_g40 - real_c40
    real_delta_absorb40 = real_c80 - real_g40

    # ---- matched (existing) admittance, reproduced for the side-by-side table ----
    n40_m, n80_m, r40_m, r80_m = prm.compute_r_profiles(thetas)
    # ---- realizable admittance, this cycle's own new leg ----
    n40_r, n80_r, r40_r, r80_r = compute_r_profiles_realizable(thetas)

    dphi40 = np.degrees(np.angle(r40_m) - np.angle(r40_r))
    dphi40 = (dphi40 + 180.0) % 360.0 - 180.0
    dphi80 = np.degrees(np.angle(r80_m) - np.angle(r80_r))
    dphi80 = (dphi80 + 180.0) % 360.0 - 180.0
    print(f"\n[phase divergence] arg(r_matched)-arg(r_realizable), over theta in "
          f"[{thetas.min()},{thetas.max()}]deg:")
    print(f"    ABSORB=40: min={np.min(np.abs(dphi40)):.2f}deg  max={np.max(np.abs(dphi40)):.2f}deg")
    print(f"    ABSORB=80: min={np.min(np.abs(dphi80)):.2f}deg  max={np.max(np.abs(dphi80)):.2f}deg")

    results = {}
    for admit_name, r40, r80 in (("matched", r40_m, r80_m), ("realizable", r40_r, r80_r)):
        pred_sw, _ = prm.predicted_c_empty(thetas, geoms, r40, r80)
        pred_tw = prm.predicted_c_empty_two_wall(thetas, geoms, r40, r80)

        sw_delta_pad = pred_sw["G40"] - pred_sw["C40"]
        sw_delta_absorb40 = pred_sw["C80"] - pred_sw["G40"]
        tw_delta_pad = pred_tw["G40"] - pred_tw["C40"]
        tw_delta_absorb40 = pred_tw["C80"] - pred_tw["G40"]

        print(f"\n[{admit_name}] single-wall model")
        sw_pad = score(thetas, real_delta_pad, sw_delta_pad, f"{admit_name} SW PAIR_PAD")
        sw_abs = score(thetas, real_delta_absorb40, sw_delta_absorb40, f"{admit_name} SW PAIR_ABSORB40")
        print(f"    PAIR_PAD:      rel_dev={sw_pad['rel_dev']:.4f}  r^2={sw_pad['r_squared']:.4f}  "
              f"-> {sw_pad['combined']}")
        print(f"    PAIR_ABSORB40: rel_dev={sw_abs['rel_dev']:.4f}  r^2={sw_abs['r_squared']:.4f}  "
              f"-> {sw_abs['combined']}")

        print(f"\n[{admit_name}] two-wall model (PRIMARY, exp-077's own headline)")
        tw_pad = score(thetas, real_delta_pad, tw_delta_pad, f"{admit_name} TW PAIR_PAD")
        tw_abs = score(thetas, real_delta_absorb40, tw_delta_absorb40, f"{admit_name} TW PAIR_ABSORB40")
        print(f"    PAIR_PAD:      rel_dev={tw_pad['rel_dev']:.4f}  r^2={tw_pad['r_squared']:.4f}  "
              f"-> {tw_pad['combined']}")
        print(f"    PAIR_ABSORB40: rel_dev={tw_abs['rel_dev']:.4f}  r^2={tw_abs['r_squared']:.4f}  "
              f"-> {tw_abs['combined']}")

        results[admit_name] = dict(single_wall=dict(pair_pad=sw_pad, pair_absorb40=sw_abs),
                                    two_wall=dict(pair_pad=tw_pad, pair_absorb40=tw_abs))

    flips = []
    for model_key in ("single_wall", "two_wall"):
        for pair_key in ("pair_pad", "pair_absorb40"):
            m = results["matched"][model_key][pair_key]["combined"]
            r = results["realizable"][model_key][pair_key]["combined"]
            if m != r:
                flips.append((model_key, pair_key, m, r))
    print(f"\n[verdict comparison] matched vs realizable: {len(flips)} flip(s)")
    for f in flips:
        print(f"    {f}")
    if not flips:
        print("    NONE -- every REFUTE/INCONCLUSIVE verdict this sub-thread has published "
              "for the x-wall single- and two-wall models is unchanged under the realizable "
              "(mu_r=1) admittance family.")

    out = dict(
        phase_divergence_deg=dict(
            absorb40=dict(min=float(np.min(np.abs(dphi40))), max=float(np.max(np.abs(dphi40)))),
            absorb80=dict(min=float(np.min(np.abs(dphi80))), max=float(np.max(np.abs(dphi80)))),
        ),
        results=results, verdict_flips=flips, n_flips=len(flips),
    )
    out_path = os.path.join(HERE, "x_wall_realizable_refit_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
