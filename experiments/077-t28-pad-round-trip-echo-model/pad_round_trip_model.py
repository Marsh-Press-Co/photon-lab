"""
experiments/077-t28-pad-round-trip-echo-model/pad_round_trip_model.py
============================================================================
Panel Iteration 54 (exp-077). Lead: VISION SCIENCE, by rotation. Executes
LOGBOOK.md's Iteration-53 (exp-076) Tier-0 #1 queue item: refit exp-075's
own already passivity-gated (G-LOSSLESS, G-N1, G-PASSIVITY) transfer-matrix
echo model against `PAD`'s round-trip distance instead of `ABSORB` depth --
the ONLY mechanism class exp-076's own lossless-vacuum proof leaves
physically permitted for T28's dominant PAIR_PAD signal (amp_ratio=0.119,
HIGH).

ZERO new FDTD calls. Every piece of machinery below is IMPORTED from
already-committed, already-vetted files -- none reimplemented (house rule
R4 / this program's own "follow the house `_load()` pattern" convention,
`two_wall_cavity.py`'s own precedent):

  - `boundary_reflectance.py` (exp-075): `damp_e_profile`, `nu_profile`,
    `n_profile_exact`, `reflection_coefficient`, `c_empty_with_wall`,
    `c_empty_boundary_free`, `image_geometry`, the three sanity/passivity
    gates (`gate_lossless_unimodular`, `gate_single_layer_identity`,
    `gate_passivity`), `CPL`, `dg065`, `dg048`.
  - `experiments/065-.../design_geometry.py` (`dg065`): `CONFIGS["C40"]`,
    `CONFIGS["G40"]`, `CONFIGS["C80"]`, `propagator_geom`.
  - `experiments/069-.../run.py`: `_free_period_search`, `_fixed_period_fit`
    -- the SAME period-fitting methodology this entire T28 sub-thread has
    used since Iteration 46, imported here verbatim, not reimplemented.
  - `experiments/076-.../results.json::headline`: the REAL, already-
    collected `C40`/`G40`/`C80` dense-sweep arrays (31 points, 36-42deg,
    0.2deg step, 600nm, settled STEPS=2800) -- read, never hand-typed (R4).

THE PHYSICAL LOGIC (verified against code below, not merely asserted):
`PAIR_PAD = (C40, G40)` holds `ABSORB` fixed at 40 for BOTH configs, so
`n(x; ABSORB=40)` -- and therefore `r(theta; ABSORB=40)` -- is IDENTICAL
for `C40` and `G40` (same profile, same function call). The ONLY thing
that differs between the two configs' geometry is `PLANE_X`/`SRC_X`/`nx`
(exp-065's PAD trick: `PLANE_X = BASE_PLANE_X + pad`, 77 for `C40`'s
`pad=0`, 117 for `G40`'s `pad=40`; `SRC_X` shifts identically). So the
single-wall echo model's ENTIRE predicted `C40`-vs-`G40` difference is the
image-source round-trip DISTANCE to the near (`-x`) wall changing -- the
literal meaning of "PAD's round-trip distance" -- with zero change to the
band's own reflectivity. `PAIR_ABSORB40 = (G40, C80)` is the complementary
control: `G40` and `C80` share IDENTICAL geometry (both `PAD=40`,
`plane_x=117`, `src_x=340`, `nx=440` -- verified by assertion below) but
different `ABSORB` (40 vs 80), so this pair isolates the reflectivity-
magnitude/phase axis at FIXED round-trip distance -- the mirror-image
control to `PAIR_PAD`.

Run: `python3 pad_round_trip_model.py` from this directory (or anywhere --
paths resolve from `__file__`). Writes `pad_round_trip_results.json` and
prints every table below; every number in `phase1_proposal.md` is copied
from that JSON/stdout, never hand-typed (R4).
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
    """Load a module from an explicit path under a unique name -- the house
    pattern `two_wall_cavity.py`/`boundary_reflectance.py` use for filename
    collisions across experiment directories (`design_geometry.py`,
    `run.py` are reused names throughout this program)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")

br = _load(os.path.join(EXP075_DIR, "boundary_reflectance.py"), "_exp077_boundary_reflectance")
dg065 = br.dg065
dg048 = br.dg048
CPL = br.CPL

run69 = _load(br.RUN69_PATH, "_exp077_run69")
_fixed_period_fit = run69._fixed_period_fit
_free_period_search = run69._free_period_search


# =========================================================== [1] geometry
def load_pair_geometries():
    """The three configs this cycle touches, and the static geometric
    congruence checks that make the "round-trip distance, not reflectance"
    framing correct -- verified here, not assumed."""
    c40 = dg065.CONFIGS["C40"]
    g40 = dg065.CONFIGS["G40"]
    c80 = dg065.CONFIGS["C80"]

    # PAIR_PAD's premise: C40 and G40 share ABSORB (so share n(x), r(theta))
    # but differ in PLANE_X/SRC_X/nx.
    assert c40["absorb"] == g40["absorb"] == 40, "PAIR_PAD must hold ABSORB fixed at 40"
    assert c40["plane_x"] != g40["plane_x"], "PAIR_PAD must have a real PLANE_X shift"

    # PAIR_ABSORB40's premise: G40 and C80 share IDENTICAL geometry (both
    # PAD=40) but differ in ABSORB.
    for key in ("nx", "ny", "src_x", "plane_x", "obj_x", "obj_y", "d_sp"):
        assert g40[key] == c80[key], f"G40/C80 geometry mismatch at {key}: {g40[key]} vs {c80[key]}"
    assert g40["absorb"] != c80["absorb"], "PAIR_ABSORB40 must have a real ABSORB difference"

    geoms = dict(
        C40=dict(cfg=c40, g=dg065.propagator_geom(c40)),
        G40=dict(cfg=g40, g=dg065.propagator_geom(g40)),
        C80=dict(cfg=c80, g=dg065.propagator_geom(c80)),
    )
    return geoms


# ========================================================== [2] r(theta)
def compute_r_profiles(thetas):
    """r(theta; ABSORB=40) and r(theta; ABSORB=80) on the real dense grid,
    via `boundary_reflectance.py`'s own already-vetted `n_profile_exact` +
    `reflection_coefficient` -- imported, not reimplemented."""
    omega600 = 2.0 * math.pi / CPL[600]
    n40 = br.n_profile_exact(br.nu_profile(br.damp_e_profile(40)), omega600)
    n80 = br.n_profile_exact(br.nu_profile(br.damp_e_profile(80)), omega600)
    r40 = np.array([br.reflection_coefficient(n40, float(t), CPL[600]) for t in thetas])
    r80 = np.array([br.reflection_coefficient(n80, float(t), CPL[600]) for t in thetas])
    return n40, n80, r40, r80


# =========================================================== [3] gates
def run_gates(thetas, r40, r80):
    """Re-run and re-print the three sanity/passivity gates on THIS file's
    own computed r(theta) values before trusting any downstream number
    (house rule -- must ALL pass or the analysis halts). G-LOSSLESS and
    G-N1 are generic identities of the transfer-matrix code itself
    (independent of which ABSORB/theta values this cycle happens to use);
    G-PASSIVITY is re-run HERE, on THIS cycle's own (absorb, theta) pairs
    -- not merely cited from exp-075's own run."""
    g_lossless = br.gate_lossless_unimodular()
    g_single = br.gate_single_layer_identity()
    all_r_flat = {}
    for t, rv in zip(thetas, r40):
        all_r_flat[(40, float(t))] = rv
    for t, rv in zip(thetas, r80):
        all_r_flat[(80, float(t))] = rv
    g_pass = br.gate_passivity(all_r_flat)

    print("\n[GATES] re-run on THIS cycle's own r(theta) values")
    print(f"    G-LOSSLESS  worst ||r|-1| over {len(g_lossless['checks'])} random real "
          f"profiles/angles = {g_lossless['worst_dev']:.3e}  PASS={g_lossless['pass_']}")
    print(f"    G-N1        worst |r_loop - r_direct| over 8 random single layers "
          f"= {g_single['worst_dev']:.3e}  PASS={g_single['pass_']}")
    print(f"    G-PASSIVITY worst |r| over {len(all_r_flat)} (ABSORB,theta) pairs "
          f"= {g_pass['worst_abs_r']:.6f}  PASS={g_pass['pass_']}")
    assert g_lossless["pass_"], "G-LOSSLESS FAILED -- halting, transfer matrix code has a bug"
    assert g_single["pass_"], "G-N1 FAILED -- halting, transfer matrix code has a bug"
    assert g_pass["pass_"], "G-PASSIVITY FAILED -- halting, |r|>1 somewhere"
    return dict(gate_lossless_unimodular=g_lossless,
                gate_single_layer_identity=g_single,
                gate_passivity=g_pass)


# ================================================ [4] predicted C_empty
def predicted_c_empty(thetas, geoms, r40, r80):
    """Single-wall (near -x wall only) predicted C_empty for each of the
    three configs, via `boundary_reflectance.py::c_empty_with_wall`
    (exp-048's Huygens-Fresnel propagator + a mirror-image source through
    the x=0 wall, weighted by r(theta;ABSORB)) -- imported, not
    reimplemented. C40/G40 use r40 (ABSORB=40 for both, PAIR_PAD's own
    premise); C80 uses r80."""
    pred = {"C40": [], "G40": [], "C80": []}
    bfree = {"C40": [], "G40": [], "C80": []}
    r_for = {"C40": r40, "G40": r40, "C80": r80}
    for key in ("C40", "G40", "C80"):
        g = geoms[key]["g"]
        rs = r_for[key]
        for t, r in zip(thetas, rs):
            pred[key].append(br.c_empty_with_wall(float(t), CPL[600], g, r))
            bfree[key].append(br.c_empty_boundary_free(float(t), CPL[600], g))
        pred[key] = np.array(pred[key])
        bfree[key] = np.array(bfree[key])
    return pred, bfree


def free_period_with_widening(thetas, delta, label):
    """Test A helper: the established narrow [1,4]deg window first
    (exp-069's own default, the window that produced the P*=2.8421deg
    citation); if the free-period search runs to EITHER boundary of that
    window, widen to [1,15]deg (the single-wall model's own closed-form
    period range, boundary_reflectance.py Sec[6]'s own choice for the
    model curve) and, if THAT also hits boundary, to [1,60]deg -- exactly
    boundary_reflectance.py's own Sec[6] staged-widening pattern, applied
    here to whichever curve (real or predicted) needs it, not assumed in
    advance which one will."""
    stages = [
        dict(name="narrow[1,4]", lo_deg=1.0, hi_deg=4.0, n_grid=400),
        dict(name="wide[1,15]", lo_deg=1.0, hi_deg=15.0, n_grid=2800),
        dict(name="widest[1,60]", lo_deg=1.0, hi_deg=60.0, n_grid=6000),
    ]
    results = []
    chosen = None
    for st in stages:
        fit = _free_period_search(thetas, delta, center_deg=39.0,
                                   lo_deg=st["lo_deg"], hi_deg=st["hi_deg"], n_grid=st["n_grid"])
        p = fit["p_star_deg"]
        at_lo = p <= st["lo_deg"] * 1.005
        at_hi = p >= st["hi_deg"] * 0.995
        at_boundary = bool(at_lo or at_hi)
        rec = dict(window=st["name"], lo_deg=st["lo_deg"], hi_deg=st["hi_deg"],
                   p_star_deg=p, r_squared=fit["r_squared"], at_boundary=at_boundary)
        results.append(rec)
        print(f"    [{label}] {st['name']:>12}: P*={p:8.4f}deg  R^2={fit['r_squared']:.4f}"
              f"{'  [AT BOUNDARY -- widening]' if at_boundary else '  [interior optimum]'}")
        if chosen is None or (chosen["at_boundary"] and not at_boundary):
            chosen = rec
        if not at_boundary:
            break
    return dict(stages=results, chosen=chosen)


def main():
    out = {}
    print("=" * 78)
    print("exp-077 -- PAD round-trip-distance refit of exp-075's single-wall echo model")
    print("=" * 78)

    # ---- [1] geometry ----
    print("\n[1] GEOMETRY CONGRUENCE (verified, not assumed)")
    geoms = load_pair_geometries()
    for key in ("C40", "G40", "C80"):
        c = geoms[key]["cfg"]
        print(f"    {key}: ABSORB={c['absorb']:3d}  PAD={c['pad']:3d}  nx={c['nx']:4d}  "
              f"src_x={c['src_x']:4d}  plane_x={c['plane_x']:4d}  d_sp={c['d_sp']:4d}")
    print("    PAIR_PAD  (C40,G40): SAME ABSORB=40 -> IDENTICAL r(theta); "
          f"PLANE_X {geoms['C40']['cfg']['plane_x']} -> {geoms['G40']['cfg']['plane_x']} "
          "(round-trip distance changes, reflectance does not)")
    print("    PAIR_ABSORB40 (G40,C80): SAME geometry "
          f"(plane_x={geoms['G40']['cfg']['plane_x']}=={geoms['C80']['cfg']['plane_x']}); "
          f"ABSORB {geoms['G40']['cfg']['absorb']} -> {geoms['C80']['cfg']['absorb']} "
          "(reflectance changes, round-trip distance does not)")
    out["geometry"] = {k: geoms[k]["cfg"] for k in ("C40", "G40", "C80")}

    # ---- real data ----
    with open(EXP076_RESULTS) as f:
        res76 = json.load(f)
    headline = res76["headline"]
    thetas = np.array(headline["theta"])
    real_c40 = np.array(headline["C40"])
    real_g40 = np.array(headline["G40"])
    real_c80 = np.array(headline["C80"])
    real_delta_pad = real_g40 - real_c40
    real_delta_absorb40 = real_c80 - real_g40
    print(f"\n[2] REAL DATA (experiments/076/results.json::headline, {len(thetas)} angles, "
          f"{thetas.min()}-{thetas.max()}deg, 600nm, settled STEPS=2800)")
    print(f"    real PAIR_PAD delta (G40-C40):      min={real_delta_pad.min():.6e}  "
          f"max={real_delta_pad.max():.6e}  ptp={np.ptp(real_delta_pad):.6e}")
    print(f"    real PAIR_ABSORB40 delta (C80-G40): min={real_delta_absorb40.min():.6e}  "
          f"max={real_delta_absorb40.max():.6e}  ptp={np.ptp(real_delta_absorb40):.6e}")
    print(f"    (established headline amp_ratio: PAIR_PAD={headline['x_amp_ratio_PAIR_PAD']:.6f} HIGH, "
          f"PAIR_ABSORB40={headline['y_amp_ratio_PAIR_ABSORB40']:.6f} MED)")
    out["thetas"] = thetas.tolist()
    out["real_delta_pad"] = real_delta_pad.tolist()
    out["real_delta_absorb40"] = real_delta_absorb40.tolist()
    out["real_amp_ratio_pad"] = headline["x_amp_ratio_PAIR_PAD"]
    out["real_amp_ratio_absorb40"] = headline["y_amp_ratio_PAIR_ABSORB40"]

    # ---- [2] r(theta;40) / r(theta;80) on this grid ----
    print(f"\n[3] r(theta;ABSORB) ON THE REAL DENSE GRID ({len(thetas)} angles)")
    n40, n80, r40, r80 = compute_r_profiles(thetas)
    for absorb, rs in (("40", r40), ("80", r80)):
        i0, imid, i1 = 0, len(thetas) // 2, len(thetas) - 1
        print(f"    ABSORB={absorb:>3}  theta={thetas[i0]:.1f}: |r|={abs(rs[i0]):.4f} "
              f"arg={math.degrees(np.angle(rs[i0])):+7.2f}deg   "
              f"theta={thetas[imid]:.1f}: |r|={abs(rs[imid]):.4f} "
              f"arg={math.degrees(np.angle(rs[imid])):+7.2f}deg   "
              f"theta={thetas[i1]:.1f}: |r|={abs(rs[i1]):.4f} "
              f"arg={math.degrees(np.angle(rs[i1])):+7.2f}deg")

    # ---- [3] gates, re-run on THIS cycle's own r(theta) values ----
    gates = run_gates(thetas, r40, r80)
    out.update(gates)

    # ---- [4] predicted C_empty, single-wall (near -x wall) model ----
    print("\n[4] PREDICTED C_empty (single-wall echo model, per config)")
    pred, bfree = predicted_c_empty(thetas, geoms, r40, r80)
    bfree_spread = max(
        float(np.max(np.abs(bfree[k] - bfree["C40"]))) for k in ("G40", "C80")
    )
    print(f"    internal check: max|C_boundary_free(k)-C_boundary_free(C40)| over "
          f"G40/C80, all angles = {bfree_spread:.3e}  (expect ~0 -- congruent geometry, "
          f"exp-065 Sec 2; the PAD trick holds D_SP fixed)")
    out["boundary_free_spread_internal_check"] = bfree_spread

    pred_delta_pad = pred["G40"] - pred["C40"]
    pred_delta_absorb40 = pred["C80"] - pred["G40"]
    print(f"    predicted PAIR_PAD delta (G40-C40):      min={pred_delta_pad.min():.6e}  "
          f"max={pred_delta_pad.max():.6e}  ptp={np.ptp(pred_delta_pad):.6e}")
    print(f"    predicted PAIR_ABSORB40 delta (C80-G40): min={pred_delta_absorb40.min():.6e}  "
          f"max={pred_delta_absorb40.max():.6e}  ptp={np.ptp(pred_delta_absorb40):.6e}")
    out["pred_delta_pad"] = pred_delta_pad.tolist()
    out["pred_delta_absorb40"] = pred_delta_absorb40.tolist()

    amp_ratio_ptp = {
        "pad": float(np.ptp(pred_delta_pad) / np.ptp(real_delta_pad)),
        "absorb40": float(np.ptp(pred_delta_absorb40) / np.ptp(real_delta_absorb40)),
    }
    print(f"    amplitude ratio (model ptp / real ptp): "
          f"PAIR_PAD={amp_ratio_ptp['pad']:.4f}  PAIR_ABSORB40={amp_ratio_ptp['absorb40']:.4f}")
    out["amplitude_ptp_ratio_model_over_real"] = amp_ratio_ptp

    # ---- [5] closed-form cross-check (per component, zero-order in r's phase) ----
    print("\n[5] CLOSED-FORM PER-WALL ROUND-TRIP PERIOD (cross-check, zero-order in r(theta)'s "
          "own phase; the actual DELTA of two different-period sinusoids is a beat, not this "
          "period directly -- see idealizations)")
    closed = {}
    for key in ("C40", "G40", "C80"):
        plane_x = geoms[key]["cfg"]["plane_x"]
        p = math.degrees(CPL[600] / (2.0 * plane_x * math.sin(math.radians(39.0))))
        closed[key] = dict(plane_x=plane_x, period_deg=p)
        print(f"    {key}: plane_x={plane_x:4d}  P_wall(39deg)={p:.3f}deg")
    out["closed_form_period_at_39deg"] = closed

    # ---- [6] Test A: free-period fit, staged widening ----
    print("\n[6] TEST A -- FREE-PERIOD FIT (exp-069's own methodology, imported not reimplemented)")
    print("  -- PAIR_PAD --")
    real_free_pad = free_period_with_widening(thetas, real_delta_pad, "real PAIR_PAD")
    pred_free_pad = free_period_with_widening(thetas, pred_delta_pad, "model PAIR_PAD")
    print("  -- PAIR_ABSORB40 --")
    real_free_absorb40 = free_period_with_widening(thetas, real_delta_absorb40, "real PAIR_ABSORB40")
    pred_free_absorb40 = free_period_with_widening(thetas, pred_delta_absorb40, "model PAIR_ABSORB40")
    out["test_a_pair_pad"] = dict(real=real_free_pad, model=pred_free_pad)
    out["test_a_pair_absorb40"] = dict(real=real_free_absorb40, model=pred_free_absorb40)

    def rel_dev(real_chosen, model_chosen):
        p_real = real_chosen["p_star_deg"]
        p_model = model_chosen["p_star_deg"]
        return abs(p_model - p_real) / p_real, p_real, p_model

    rd_pad, preal_pad, pmodel_pad = rel_dev(real_free_pad["chosen"], pred_free_pad["chosen"])
    rd_absorb40, preal_absorb40, pmodel_absorb40 = rel_dev(
        real_free_absorb40["chosen"], pred_free_absorb40["chosen"])
    print(f"\n    PAIR_PAD:      P*_real={preal_pad:.4f}deg  P*_model={pmodel_pad:.4f}deg  "
          f"rel_dev={rd_pad:.4f}")
    print(f"    PAIR_ABSORB40: P*_real={preal_absorb40:.4f}deg  P*_model={pmodel_absorb40:.4f}deg  "
          f"rel_dev={rd_absorb40:.4f}")
    out["rel_period_deviation_pad"] = rd_pad
    out["rel_period_deviation_absorb40"] = rd_absorb40

    # ---- [7] Test B: Pearson r^2 shape match ----
    print("\n[7] TEST B -- SHAPE MATCH: Pearson r^2(model predicted delta, real delta)")
    corr_pad = float(np.corrcoef(pred_delta_pad, real_delta_pad)[0, 1])
    corr_absorb40 = float(np.corrcoef(pred_delta_absorb40, real_delta_absorb40)[0, 1])
    r2_pad = corr_pad ** 2
    r2_absorb40 = corr_absorb40 ** 2
    print(f"    PAIR_PAD:      r={corr_pad:+.4f}  r^2={r2_pad:.4f}")
    print(f"    PAIR_ABSORB40: r={corr_absorb40:+.4f}  r^2={r2_absorb40:.4f}")
    out["shape_pearson_r_pad"] = corr_pad
    out["shape_r_squared_pad"] = r2_pad
    out["shape_pearson_r_absorb40"] = corr_absorb40
    out["shape_r_squared_absorb40"] = r2_absorb40

    # ---- [8] pre-registered bands, scored in code ----
    print("\n[8] PRE-REGISTERED FALSIFIABLE BANDS -- scored (reused verbatim from exp-075's "
          "phase1_proposal.md Sec 5)")

    def score_pair(name, rd, r2):
        period_support = rd <= 0.30
        period_refute = rd > 1.00
        shape_support = r2 >= 0.30
        shape_refute = r2 <= 0.05
        if period_support and shape_support:
            combined = "SUPPORT"
        elif period_refute or shape_refute:
            combined = "REFUTE"
        else:
            combined = "INCONCLUSIVE"
        print(f"    {name}: period band rel_dev={rd:.4f} -> "
              f"{'SUPPORT' if period_support else ('REFUTE' if period_refute else 'INCONCLUSIVE')}   "
              f"shape band r^2={r2:.4f} -> "
              f"{'SUPPORT' if shape_support else ('REFUTE' if shape_refute else 'INCONCLUSIVE')}   "
              f"COMBINED: {combined}")
        return dict(period_support=bool(period_support), period_refute=bool(period_refute),
                    shape_support=bool(shape_support), shape_refute=bool(shape_refute),
                    combined_verdict=combined)

    verdict_pad = score_pair("PAIR_PAD     ", rd_pad, r2_pad)
    verdict_absorb40 = score_pair("PAIR_ABSORB40", rd_absorb40, r2_absorb40)
    out["verdict_pad"] = verdict_pad
    out["verdict_absorb40"] = verdict_absorb40

    print(f"\n    PRIMARY TARGET (PAIR_PAD, the dominant signal this cycle was tasked to "
          f"explain): COMBINED = {verdict_pad['combined_verdict']}")
    print(f"    SECONDARY CHECK (PAIR_ABSORB40): COMBINED = {verdict_absorb40['combined_verdict']}")

    def _json_default(o):
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, complex):
            return dict(re=o.real, im=o.imag)
        raise TypeError(f"not JSON serializable: {type(o)}")

    out_path = os.path.join(HERE, "pad_round_trip_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
