"""exp-020 — The Ambient-Appearance Baseline: measurement harness.
==================================================================
Geometry comes from design_geometry.py (the committed ray-trace design
calculation) — single source of truth; predictions P1–P7 are frozen in
NOTES.md (commit precedes this file's first run, house discipline).

124 runs: 4 articles × 9 angles × 3 λ + 16 convergence (empty+PEC @600 nm,
8 extra angles). Each (θ, λ) group runs its own empty reference first;
per-run ledger rows (σ_abs / σ_ext both routes / i_inc / box net flux /
source amplitude) land in results.json alongside the contrast table.
LINEAR-MEDIA idiom throughout (see lab/ambient.py docstring).
"""

import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..")))
sys.path.insert(0, HERE)

import design_geometry as dg
from lab import Sim, materials, ambient as amb, sections as sc

LAMBDAS = ((450, 15), (600, 20), (750, 25))       # (nm, cells per lambda)
STEPS = 1400
BOX = (80, 260, 510, 690)                          # widths box around object
REF = (dg.OBJ[0], dg.OBJ[1], 80)                   # i_inc strip (empty run)
W_EQ = "equal"
ARTICLES = ("empty", "absorber", "pec", "sponge")
V_PHOT = {450: 0.038, 600: 0.631, 750: 0.00012}    # CIE 1924 V(λ)
V_SCOT = {450: 0.455, 600: 0.033, 750: 1e-6}       # CIE 1951 V'(λ)


def build(article, sim):
    cx, cy = dg.OBJ
    if article == "empty":
        return
    if article == "absorber":                      # stage-7 config verbatim
        materials.pec_disk(sim, cx, cy, 30)
        materials.graded_black_shell(sim, cx, cy, 30, dg.R_OUT)
    elif article == "pec":
        materials.pec_disk(sim, cx, cy, dg.R_OUT)
    elif article == "sponge":                      # dilute calibration article
        x = np.arange(sim.nx)[:, None]
        y = np.arange(sim.ny)[None, :]
        mask = (x - cx) ** 2 + (y - cy) ** 2 <= dg.R_OUT ** 2
        sim.sigma_e[mask] += dg.SIGMA_SPONGE
        sim.objects.append({"type": "uniform_sponge_disk",
                            "params": {"cx": cx, "cy": cy, "r": dg.R_OUT,
                                       "sigma": dg.SIGMA_SPONGE}})


def one_run(article, theta, cpl):
    sim = Sim(dg.NX, dg.NY, cells_per_lambda=cpl, courant_frac=0.99,
              absorb=dg.ABSORB)
    build(article, sim)
    sim.add_line_source(dg.SRC_X, angle_deg=theta, edge=dg.TAPER, amplitude=1.0)
    sim.run(STEPS)
    return sc.full_capture(sim)


def run_group(args):
    """One (λ, θ) group: empty first, then the requested articles measured
    against that empty. Returns per-article profiles + ledger rows."""
    lam_nm, cpl, theta, articles = args
    t0 = time.time()
    out = {}
    cap_e = one_run("empty", theta, cpl)
    ph_e = sc.phasors(cap_e)
    prof_e = {d: amb.observer_profile(ph_e, dg.OBJ[0] - dg.R_OUT - d,
                                      dg.ABSORB, dg.NY - dg.ABSORB)
              for d in dg.SENS_PLANES}
    # empty-box bookkeeping: net outward flux of the empty total field
    net_e = sc._face_flux(ph_e["ez"], ph_e["hx"], ph_e["hy"], BOX)
    # i_inc at the object position (widths' own idiom)
    rs = slice(REF[1] - REF[2], REF[1] + REF[2] + 1)
    hy_i = 0.5 * (ph_e["hy"][REF[0] - 1, rs] + ph_e["hy"][REF[0], rs])
    i_inc = float(np.mean(-0.5 * np.real(ph_e["ez"][REF[0], rs] * np.conj(hy_i))))
    out["empty"] = {"profiles": {d: prof_e[d].tolist() for d in dg.SENS_PLANES},
                    "net_box_flux": float(net_e), "i_inc": i_inc}
    for art in articles:
        if art == "empty":
            continue
        cap = one_run(art, theta, cpl)
        ph = sc.phasors(cap)
        profs = {d: amb.observer_profile(ph, dg.OBJ[0] - dg.R_OUT - d,
                                         dg.ABSORB, dg.NY - dg.ABSORB)
                 for d in dg.SENS_PLANES}
        wd = sc.widths(cap, cap_e, BOX, REF)
        out[art] = {"profiles": {d: profs[d].tolist() for d in dg.SENS_PLANES},
                    "sigma_abs": wd["sigma_abs"], "sigma_ext": wd["sigma_ext"],
                    "sigma_ext_cross": wd["sigma_ext_cross"],
                    "back_frac": wd["back_frac"], "i_inc": wd["i_inc"]}
    return (lam_nm, theta, out, time.time() - t0)


def main():
    groups = []
    for lam_nm, cpl in LAMBDAS:
        for th in dg.ANGLES:
            groups.append((lam_nm, cpl, float(th), list(ARTICLES)))
    for th in dg.N17_EXTRA:                        # convergence set @600 nm
        groups.append((600, 20, float(th), ["empty", "pec"]))

    n_runs = sum(len(g[3]) for g in groups)
    print(f"exp-020: {len(groups)} groups, {n_runs} runs, "
          f"{os.cpu_count()} cpus")
    t0 = time.time()
    results = {}
    with ProcessPoolExecutor(max_workers=4) as ex:
        for lam_nm, theta, out, dt in ex.map(run_group, groups):
            results[(lam_nm, theta)] = out
            done = len(results)
            print(f"  [{done:2d}/{len(groups)}] λ={lam_nm} θ={theta:+05.1f}° "
                  f"({dt:5.1f} s)", flush=True)

    # ---------------- assemble contrasts (per article, λ, weighting) ------
    def contrast(article, lam_nm, angles, weights, plane=15):
        profs, e_profs = [], []
        for th in angles:
            grp = results[(lam_nm, float(th))]
            profs.append(np.array(grp[article]["profiles"][plane]))
            e_profs.append(np.array(grp["empty"]["profiles"][plane]))
        return amb.contrast_from_runs(
            profs, e_profs, weights, dg.ABSORB, dg.OBJ[1],
            dg.W_OBJ, dg.GUARD_OUT, dg.W_FLANK)

    def wts(name, angles):
        return ([1.0] * len(angles) if name == "equal"
                else [float(np.cos(np.radians(t))) for t in angles])

    table, floors = {}, {}
    for art in ARTICLES:
        for lam_nm, _ in LAMBDAS:
            for wname in ("equal", "cos"):
                r = contrast(art, lam_nm, dg.ANGLES, wts(wname, dg.ANGLES))
                table[f"{art}/{lam_nm}/{wname}"] = {
                    "C": r["C"], "C_empty": r["C_empty"],
                    "b_obj": r["b_obj"], "b_flank": r["b_flank"]}
                if art == "empty":
                    floors[f"{lam_nm}/{wname}"] = abs(r["C_empty"])

    # plane sensitivity (absorber & sponge @600, equal weights)
    planes = {}
    for art in ("absorber", "sponge", "pec"):
        planes[art] = {d: contrast(art, 600, dg.ANGLES,
                                   wts("equal", dg.ANGLES), plane=d)["C"]
                       for d in dg.SENS_PLANES}

    # convergence @600: N5 subset, N9, N17 (empty + pec)
    conv = {}
    a5 = [-40, -20, 0, 20, 40]
    a17 = sorted(list(dg.ANGLES) + list(dg.N17_EXTRA))
    for art in ("empty", "pec"):
        cN = {}
        for label, aa in (("N5", a5), ("N9", list(dg.ANGLES)), ("N17", a17)):
            cN[label] = contrast(art, 600, aa, wts("equal", aa))["C"]
        conv[art] = cN

    # luminance-weighted combos (V photopic, V' scotopic), equal weights
    lum = {}
    for art in ARTICLES:
        for vname, vmap in (("V", V_PHOT), ("Vp", V_SCOT)):
            num, den = 0.0, 0.0
            for lam_nm, _ in LAMBDAS:
                r = table[f"{art}/{lam_nm}/equal"]
                num += vmap[lam_nm] * r["b_obj"]
                den += vmap[lam_nm] * r["b_flank"]
            lum[f"{art}/{vname}"] = num / den - 1.0

    # ---------------- harness gates (P1b, P6) -----------------------------
    gates = {}
    for lam_nm, _ in LAMBDAS:
        for th in (40.0, -40.0):
            b = np.array(results[(lam_nm, th)]["empty"]["profiles"][15])
            y = np.arange(dg.ABSORB, dg.ABSORB + b.size)
            span = (y >= dg.OBJ[1] - dg.FLANK[1]) & (y <= dg.OBJ[1] + dg.FLANK[1])
            seg = b[span]
            gates[f"P1b/{lam_nm}/{th:+.0f}"] = float(seg.min() / np.median(seg))
    for lam_nm, _ in LAMBDAS:
        for th in dg.ANGLES:
            grp = results[(lam_nm, float(th))]
            scale = abs(grp["absorber"]["sigma_abs"] * grp["absorber"]["i_inc"])
            gates[f"P6-emptybox/{lam_nm}/{th:+.0f}"] = (
                abs(grp["empty"]["net_box_flux"]) / max(scale, 1e-30))
            xr = abs(grp["absorber"]["sigma_ext_cross"] - grp["absorber"]["sigma_ext"]) \
                / abs(grp["absorber"]["sigma_ext"])
            gates[f"P6-routes-absorber/{lam_nm}/{th:+.0f}"] = xr

    out = {
        "meta": {"geometry": {k: getattr(dg, k) for k in
                              ("NX", "NY", "ABSORB", "SRC_X", "OBJ", "R_OUT",
                               "PLANE_X", "W_OBJ", "GUARD_OUT", "W_FLANK",
                               "SIGMA_SPONGE", "TAPER")},
                 "steps": STEPS, "box": BOX, "ref": REF,
                 "lambdas": LAMBDAS, "angles": list(dg.ANGLES),
                 "n17_extra": list(dg.N17_EXTRA),
                 "amplitude": 1.0,
                 "note": ("sigma values are per-(theta,lambda) normalized by "
                          "that component's own i_inc — identity gates only, "
                          "not cross-theta physics claims; linear-media idiom "
                          "throughout (lab/ambient.py)"),
                 "elapsed_s": time.time() - t0},
        "contrasts": table, "luminance_weighted": lum,
        "plane_sensitivity": planes, "convergence": conv,
        "decision_floors": floors, "gates": gates,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)

    # ---------------- console summary -------------------------------------
    print(f"\ntotal {time.time() - t0:.0f} s")
    print("\ndecision floors δ_C (summed |C_empty|):")
    for k, v in floors.items():
        print(f"  {k}: {v:.5f}")
    print("\nWeber contrast C (plane 15, equal weights):")
    for art in ARTICLES:
        row = "  ".join(f"{lam}nm {table[f'{art}/{lam}/equal']['C']:+.4f}"
                        for lam, _ in LAMBDAS)
        print(f"  {art:9s} {row}")
    print("\nluminance-weighted:", {k: round(v, 4) for k, v in lum.items()})
    print("\nconvergence:", {a: {k: round(v, 4) for k, v in c.items()}
                             for a, c in conv.items()})
    print("\nplane sensitivity:", {a: {d: round(c, 4) for d, c in p.items()}
                                   for a, p in planes.items()})
    worst_p1b = min(v for k, v in gates.items() if k.startswith("P1b"))
    worst_box = max(v for k, v in gates.items() if k.startswith("P6-emptybox"))
    worst_rt = max(v for k, v in gates.items() if k.startswith("P6-routes"))
    print(f"\nP1b worst min/median: {worst_p1b:.3f} (gate >= 0.8)")
    print(f"P6 empty-box worst: {worst_box:.4f} (gate <= 0.02)")
    print(f"P6 two-route worst (absorber): {worst_rt:.4f} (gate <= 0.12)")

    # ---------------- figure ----------------------------------------------
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BGC, INK = "#0d1117", "#e6edf3"
    plt.rcParams.update({"figure.facecolor": BGC, "axes.facecolor": BGC,
                         "savefig.facecolor": BGC, "text.color": INK,
                         "axes.edgecolor": "#9198a1", "axes.labelcolor": "#9198a1",
                         "xtick.color": "#9198a1", "ytick.color": "#9198a1"})
    fig, ax = plt.subplots(figsize=(9.6, 4.2), dpi=150)
    yy = np.arange(dg.ABSORB, dg.NY - dg.ABSORB)
    colors = {"empty": "#9198a1", "absorber": "#f85149",
              "pec": "#58a6ff", "sponge": "#3fb950"}
    for art in ARTICLES:
        r = contrast(art, 600, dg.ANGLES, wts("equal", dg.ANGLES))
        ax.plot(yy, r["scene_sum"], color=colors[art], lw=1.1,
                label=f"{art}  C={r['C']:+.3f}")
    for lo, hi, c in [(dg.OBJ[1] - dg.W_OBJ, dg.OBJ[1] + dg.W_OBJ, "#d29922"),
                      (dg.OBJ[1] - dg.FLANK[1], dg.OBJ[1] - dg.FLANK[0], "#3fb950"),
                      (dg.OBJ[1] + dg.FLANK[0], dg.OBJ[1] + dg.FLANK[1], "#3fb950")]:
        ax.axvspan(lo, hi, color=c, alpha=0.10)
    ax.set_xlabel("y (cells) — object window amber, flanks green")
    ax.set_ylabel("B(y), incoherent sum (empty-flank = 1)")
    ax.legend(loc="lower left", fontsize=8, framealpha=0.2)
    ax.set_title("exp-020 — what the ambient sees: back-lit silhouettes, 600 nm",
                 loc="left", fontsize=11)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "silhouettes.png"))
    plt.close(fig)
    print("\nresults.json + silhouettes.png written")


if __name__ == "__main__":
    main()
