"""
experiments/078-t28-y-wall-echo-prescreen/phase2_redteam_angle_correction_check.py
============================================================================
RED TEAM's own independent verification script, Panel Iteration 55 Phase-2
audit (exp-078). Written and run by Red Team -- NOT copied from any of the
three critiques (EM/MATERIALS/THERMODYNAMICS) that flagged the angle-
convention defect; this is a fourth, independent re-derivation and, unlike
the critiques' scratch checks, is committed to the record with its own
output file (R4 discipline: no hand-typed numbers in the audit prose).

WHAT THIS FILE DOES

  [A] Re-derive, from first principles (Snell/phase-matching on the
      propagation direction (-cos(theta), sin(theta)) that
      `y_wall_prescreen.py` itself states as this bench's convention,
      `phase1_proposal.md` Sec 3.1), what angle argument a y-normal wall's
      transfer-matrix reflectance must be evaluated at, independent of
      reading any critique's stated conclusion first.
  [B] Confirm this against `boundary_reflectance.py::reflection_coefficient`'s
      own docstring and body (read directly, not quoted from a critique).
  [C] Recompute r(theta;ABSORB) both ways (as-implemented: raw theta_deg;
      corrected: 90-theta_deg) at the three critiques' own spot-checked
      angles, to confirm their numeric tables independently.
  [D] Re-run `y_wall_prescreen.py`'s OWN full primary-model pipeline with
      ONLY the `reflection_coefficient` call's angle argument corrected
      (nothing else touched -- same fixed_offset, same free-period search,
      same staged widening, same scoring bands) and report the corrected
      P*_model / rel_dev / verdict for all three primary comparisons,
      side-by-side with the as-filed numbers.
  [E] Re-run the three sanity/passivity gates (`gate_lossless_unimodular`,
      `gate_single_layer_identity`, `gate_passivity`) at random angles drawn
      from the CORRECTED y-wall envelope (48-54 deg, the transform of the
      real 36-42deg sweep), since the originally committed gates only
      sampled +-44deg and never touched this range -- the "affordable named
      check" EM's critique named but did not itself run to completion as a
      committed artifact.

ZERO new FDTD calls. Reuses `boundary_reflectance.py`, `design_geometry.py`,
`run.py`'s `_free_period_search`, and `y_wall_prescreen.py`'s own
`edge_image_curve`/`free_period_with_widening` pattern -- imported, not
reimplemented, except for the one corrected line this file exists to test.
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


EXP065_DIR = os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep")
EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")

dg065 = _load(os.path.join(EXP065_DIR, "design_geometry.py"), "_rt078_dg065")
br = _load(os.path.join(EXP075_DIR, "boundary_reflectance.py"), "_rt078_boundary_reflectance")
CPL = br.CPL
run69 = _load(br.RUN69_PATH, "_rt078_run69")
_free_period_search = run69._free_period_search

CONGRUENT_KEYS = ("C40", "C60", "C70", "C80", "G40")


def main():
    out = {}
    print("=" * 78)
    print("RED TEAM independent check -- y-wall angle-convention correction (exp-078)")
    print("=" * 78)

    # ---- [A] first-principles re-derivation, from the propagation direction ----
    print("\n[A] FIRST-PRINCIPLES RE-DERIVATION (independent of any critique's prose)")
    print("""
    y_wall_prescreen.py Sec[1b] / phase1_proposal.md Sec 3.1 both state the
    bench's own convention: the direct wave travels in direction
    (-cos(theta), +sin(theta)) (add_line_source's own docstring). The
    x-wall's normal is x-hat=(1,0); the y-wall's normal is y-hat=(0,1).

    The angle of incidence measured FROM A WALL'S OWN NORMAL, alpha, is
    defined by cos(alpha) = |direction . normal|.

      x-wall: cos(alpha_x) = |-cos(theta)| = cos(theta)  =>  alpha_x = theta
      y-wall: cos(alpha_y) = |sin(theta)|                =>  alpha_y = 90-theta
              (theta in [36,42]deg, so sin(theta)>0, cos is even/positive
               branch on [0,90], alpha_y = 90-theta unambiguously)

    So the x-wall's own incidence angle (measured from ITS normal) equals
    the sweep theta directly -- confirming reflection_coefficient's
    docstring convention is self-consistent for the x-wall as used
    throughout exp-075/077. For the y-wall, the angle from ITS normal is
    90-theta, NOT theta. This is re-derived here from the propagation
    direction alone, not read off EM's or MATERIALS' stated conclusion.
    """)
    thetas_check = [36.0, 39.0, 42.0]
    alpha_y = [90.0 - t for t in thetas_check]
    print(f"    theta (sweep, from x-normal): {thetas_check}")
    print(f"    alpha_y (from y-normal, re-derived): {alpha_y}")
    out["rederivation"] = dict(theta_sweep=thetas_check, alpha_y_from_normal=alpha_y)

    # ---- [B] confirm against reflection_coefficient's own contract ----
    print("\n[B] boundary_reflectance.py::reflection_coefficient -- read directly")
    import inspect
    doc = br.reflection_coefficient.__doc__
    print("    docstring (verbatim, first 2 lines):")
    for line in doc.strip().splitlines()[:2]:
        print(f"      {line.strip()}")
    src = inspect.getsource(br.reflection_coefficient)
    assert "sin(theta)" in src.replace(" ", ""), "s2 no longer built from sin(theta) -- re-check"
    print("    body: s2 = sin(radians(theta_deg))**2 -- theta_deg enters ONLY as sin(),")
    print("    confirming theta_deg IS the angle from whichever wall's normal is being")
    print("    modeled (sin(angle-from-normal) = tangential-component/k0, standard")
    print("    oblique-incidence form). This matches [A]'s conclusion independently.")
    out["docstring_first_two_lines"] = [l.strip() for l in doc.strip().splitlines()[:2]]

    # ---- [C] spot-check the critiques' own numeric tables ----
    print("\n[C] SPOT-CHECK: r(theta;ABSORB) both ways, at critiques' own angles")
    spot = {}
    for absorb in (40, 80):
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb)),
                                     2.0 * math.pi / CPL[600])
        spot[absorb] = {}
        for t in thetas_check:
            r_impl = br.reflection_coefficient(n_prof, t, CPL[600])
            r_corr = br.reflection_coefficient(n_prof, 90.0 - t, CPL[600])
            row = dict(
                theta=t,
                abs_r_impl=float(abs(r_impl)), arg_r_impl_deg=math.degrees(float(np.angle(r_impl))),
                abs_r_corr=float(abs(r_corr)), arg_r_corr_deg=math.degrees(float(np.angle(r_corr))),
                ratio=float(abs(r_corr) / abs(r_impl)),
            )
            spot[absorb][t] = row
            print(f"    ABSORB={absorb:3d} theta={t:5.1f}: |r|impl={row['abs_r_impl']:.6f} "
                  f"|r|corr={row['abs_r_corr']:.6f} ratio={row['ratio']:6.2f}x  "
                  f"arg impl={row['arg_r_impl_deg']:+8.2f}deg arg corr={row['arg_r_corr_deg']:+8.2f}deg")
    out["spot_check_r_both_conventions"] = spot

    # ---- [D] full corrected re-score of the primary model ----
    print("\n[D] FULL CORRECTED RE-SCORE of y_wall_prescreen.py's primary model")
    print("    (ONLY the reflection_coefficient angle argument is changed: "
          "theta_deg -> 90.0-theta_deg. fixed_offset, free-period search, "
          "staged widening, and scoring bands are all untouched/reused.)")

    def edge_image_phase_difference_corrected(theta_deg, lam_cells, cfg, absorb_for_r):
        k = 2.0 * math.pi / lam_cells
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb_for_r)),
                                     2.0 * math.pi / CPL[600])
        r = br.reflection_coefficient(n_prof, 90.0 - theta_deg, lam_cells)  # <-- the fix
        d_sp = cfg["d_sp"]
        a = cfg["A"]
        y_lo = cfg["y_lo"]
        obj_y = cfg["obj_y"]
        dist_real = float(np.hypot(d_sp, a))
        dist_image = float(np.hypot(d_sp, obj_y + y_lo))
        fixed_offset = dist_image - dist_real
        delta_phi = float(np.angle(r)) + k * fixed_offset
        return dict(delta_phi_rad=delta_phi, abs_r=float(abs(r)))

    def edge_image_curve_corrected(thetas, lam_cells, cfg, absorb_for_r):
        dphis, absr = [], []
        for t in thetas:
            d = edge_image_phase_difference_corrected(float(t), lam_cells, cfg, absorb_for_r)
            dphis.append(d["delta_phi_rad"])
            absr.append(d["abs_r"])
        dphis = np.array(dphis)
        return dict(delta_phi_rad=dphis, abs_r=np.array(absr), cos_delta_phi=np.cos(dphis),
                    ptp_delta_phi_deg=float(np.degrees(np.ptp(dphis))))

    def free_period_with_widening(thetas, delta, label):
        stages = [
            dict(name="narrow[1,4]", lo_deg=1.0, hi_deg=4.0, n_grid=400),
            dict(name="wide[1,15]", lo_deg=1.0, hi_deg=15.0, n_grid=2800),
            dict(name="widest[1,60]", lo_deg=1.0, hi_deg=60.0, n_grid=6000),
        ]
        chosen = None
        for st in stages:
            fit = _free_period_search(thetas, delta, center_deg=39.0,
                                       lo_deg=st["lo_deg"], hi_deg=st["hi_deg"], n_grid=st["n_grid"])
            p = fit["p_star_deg"]
            at_boundary = bool(p <= st["lo_deg"] * 1.005 or p >= st["hi_deg"] * 0.995)
            print(f"    [{label}] {st['name']:>12}: P*={p:9.4f}deg  R^2={fit['r_squared']:.4f}"
                  f"{'  [AT BOUNDARY]' if at_boundary else '  [interior]'}")
            if chosen is None or (chosen["at_boundary"] and not at_boundary):
                chosen = dict(window=st["name"], p_star_deg=p, r_squared=fit["r_squared"],
                               at_boundary=at_boundary)
            if not at_boundary:
                break
        return chosen

    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    headline = res76["headline"]
    thetas = np.array(headline["theta"])

    edge_curves_corr = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        edge_curves_corr[key] = edge_image_curve_corrected(thetas, CPL[600], c, c["absorb"])
        print(f"    {key}: |r| range corrected "
              f"[{edge_curves_corr[key]['abs_r'].min():.6f},{edge_curves_corr[key]['abs_r'].max():.6f}] "
              f"ptp(Delta_phi)={edge_curves_corr[key]['ptp_delta_phi_deg']:.4f}deg")

    REFERENCE_PERIODS = dict(
        c80_c40_deg=2.8421052631578947,
        pair_pad_deg=4.611289746337977,
        pair_absorb40_deg=4.176134333690603,
    )
    model_delta_pad = edge_curves_corr["G40"]["cos_delta_phi"] - edge_curves_corr["C40"]["cos_delta_phi"]
    model_delta_absorb40 = edge_curves_corr["C80"]["cos_delta_phi"] - edge_curves_corr["G40"]["cos_delta_phi"]
    model_delta_c80c40 = edge_curves_corr["C80"]["cos_delta_phi"] - edge_curves_corr["C40"]["cos_delta_phi"]

    print("\n    corrected free-period search on each PAIR_* delta curve:")
    corr_pad = free_period_with_widening(thetas, model_delta_pad, "corrected PAIR_PAD delta")
    corr_absorb40 = free_period_with_widening(thetas, model_delta_absorb40, "corrected PAIR_ABSORB40 delta")
    corr_c80c40 = free_period_with_widening(thetas, model_delta_c80c40, "corrected C80-C40 delta")

    def rel_dev(p_real, p_model):
        return abs(p_model - p_real) / p_real

    def score(rd):
        if rd <= 0.30:
            return "SUPPORT"
        elif rd > 1.00:
            return "REFUTE"
        return "INCONCLUSIVE"

    print("\n    AS-FILED vs CORRECTED, side by side:")
    as_filed = dict(
        c80_c40=dict(p_model=3.2105263157894735, rel_dev=0.12962962962962957, r2=0.1530097869774515, verdict="SUPPORT"),
        pair_pad=dict(p_model=3.1654135338345863, rel_dev=0.31355136893135443, r2=0.1331180760669618, verdict="INCONCLUSIVE"),
        pair_absorb40=dict(p_model=3.2030075187969924, rel_dev=0.23302095601738534, r2=0.1493191248004927, verdict="SUPPORT"),
    )
    corrected = {}
    for name, ref, chosen in (
        ("c80_c40", REFERENCE_PERIODS["c80_c40_deg"], corr_c80c40),
        ("pair_pad", REFERENCE_PERIODS["pair_pad_deg"], corr_pad),
        ("pair_absorb40", REFERENCE_PERIODS["pair_absorb40_deg"], corr_absorb40),
    ):
        rd = rel_dev(ref, chosen["p_star_deg"])
        v = score(rd)
        corrected[name] = dict(p_real=ref, p_model=chosen["p_star_deg"], rel_dev=rd,
                                r2=chosen["r_squared"], verdict=v, window=chosen["window"],
                                at_boundary=chosen["at_boundary"])
        af = as_filed[name]
        print(f"    {name:15s}  AS-FILED   P*={af['p_model']:8.4f}deg rel_dev={af['rel_dev']:.4f} "
              f"R2={af['r2']:.4f} -> {af['verdict']}")
        print(f"    {'':15s}  CORRECTED  P*={chosen['p_star_deg']:8.4f}deg rel_dev={rd:.4f} "
              f"R2={chosen['r_squared']:.4f} -> {v}  (window={chosen['window']}, "
              f"at_boundary={chosen['at_boundary']})")
    out["as_filed"] = as_filed
    out["corrected"] = corrected

    n_support_corr = sum(1 for v in corrected.values() if v["verdict"] == "SUPPORT")
    n_refute_corr = sum(1 for v in corrected.values() if v["verdict"] == "REFUTE")
    print(f"\n    CORRECTED summary: {n_support_corr}/3 SUPPORT, {n_refute_corr}/3 REFUTE "
          f"(as-filed was 2/3 SUPPORT, 0/3 REFUTE)")
    out["corrected_summary"] = dict(n_support=n_support_corr, n_refute=n_refute_corr)

    # ---- [E] re-run the three gates at the CORRECTED y-wall angle envelope ----
    print("\n[E] RE-RUN GATES at the corrected y-wall envelope (48-54deg), "
          "never sampled by the originally committed +-44deg gates")

    def gate_lossless_unimodular_range(lo, hi, n_trials=2000, seed=11):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for _ in range(n_trials):
            length = int(rng.integers(5, 60))
            n_prof = 1.0 + 0.6 * rng.random(length)
            theta_deg = float(rng.uniform(lo, hi))
            r = br.reflection_coefficient(n_prof.astype(complex), theta_deg, 20.0)
            worst = max(worst, abs(abs(r) - 1.0))
        return worst

    def gate_single_layer_identity_range(lo, hi, n_trials=2000, seed=13):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for _ in range(n_trials):
            n1 = complex(rng.uniform(0.5, 2.0), rng.uniform(0.0, 1.5))
            theta_deg = float(rng.uniform(lo, hi))
            lam = float(rng.uniform(10.0, 30.0))
            theta = math.radians(theta_deg)
            s2 = math.sin(theta) ** 2
            k0 = 2.0 * math.pi / lam
            kx1 = k0 * np.sqrt(n1 ** 2 - s2)
            Z1 = n1 / np.sqrt(n1 ** 2 - s2)
            Zin_direct = 1j * Z1 * np.tan(kx1 * 1.0)
            Zvac = 1.0 / math.cos(theta)
            r_direct = (Zin_direct - Zvac) / (Zin_direct + Zvac)
            r_loop = br.reflection_coefficient(np.array([n1]), theta_deg, lam)
            worst = max(worst, abs(r_direct - r_loop))
        return worst

    def gate_passivity_range(lo, hi, n_trials=2000, seed=17):
        rng = np.random.default_rng(seed)
        worst = 0.0
        for absorb in br.ABSORB_LIST:
            damp = br.damp_e_profile(absorb)
            nu = br.nu_profile(damp)
            n_exact = br.n_profile_exact(nu, 2.0 * math.pi / CPL[600])
            for _ in range(n_trials // len(br.ABSORB_LIST)):
                theta_deg = float(rng.uniform(lo, hi))
                r = br.reflection_coefficient(n_exact, theta_deg, CPL[600])
                worst = max(worst, abs(r))
        return worst

    g_lossless_new = gate_lossless_unimodular_range(48.0, 54.0)
    g_n1_new = gate_single_layer_identity_range(48.0, 54.0)
    g_pass_new = gate_passivity_range(48.0, 54.0)
    print(f"    G-LOSSLESS (48-54deg, 2000 trials): worst ||r|-1| = {g_lossless_new:.3e}  "
          f"PASS={g_lossless_new < 1e-9}")
    print(f"    G-N1       (48-54deg, 2000 trials): worst |r_loop-r_direct| = {g_n1_new:.3e}  "
          f"PASS={g_n1_new < 1e-12}")
    print(f"    G-PASSIVITY(48-54deg, 2000 trials/depth): worst |r| = {g_pass_new:.6f}  "
          f"PASS={g_pass_new <= 1.0 + 1e-9}")
    out["gates_at_corrected_envelope_48_54deg"] = dict(
        g_lossless_worst_dev=g_lossless_new, g_lossless_pass=bool(g_lossless_new < 1e-9),
        g_n1_worst_dev=g_n1_new, g_n1_pass=bool(g_n1_new < 1e-12),
        g_passivity_worst_abs_r=g_pass_new, g_passivity_pass=bool(g_pass_new <= 1.0 + 1e-9),
    )

    def _json_default(o):
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(f"not JSON serializable: {type(o)}")

    out_path = os.path.join(HERE, "phase2_redteam_angle_correction_check_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
