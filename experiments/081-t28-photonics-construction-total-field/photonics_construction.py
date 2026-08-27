"""
experiments/081-t28-photonics-construction-total-field/photonics_construction.py
=============================================================================
Panel Iteration 58 (exp-081). Lead: THERMODYNAMICS, by rotation. Executes
PLAN.md's Iteration-58 Tier-0 batch, all four items, in order (Red Team's
exp-080 Phase-5 final audit, phase5_redteam_audit.md Sec 6/Sec 7):

  Item 1 (primary): build the construction PHOTONICS actually specified
  (experiments/079-.../phase5_review_photonics.md Sec 4) --
  E(theta_beam) = E_direct(theta_beam) + r(90-theta_beam;ABSORB)*W(theta_beam)
  -- and score its PAIR_PAD/PAIR_ABSORB40/C80-C40 pair-deltas via
  _free_period_search/staged-widening against the REAL T28 reference
  periods (experiments/076-.../results.json::headline), not an R^2
  shape-comparison against a candidate curve (exp-080's own mistake,
  photonics_image_term_curve()/part_d_photonics_construction()).

  Item 1b: does E_direct (config-invariant, PHOTONICS' own exp-080 Phase-5
  proof, cited verbatim not re-derived) change the pair-delta scores at
  all, or does it cancel out of them identically?

  Item 2 (EM, cheap precondition): re-run gate_lossless_unimodular_range /
  gate_single_layer_identity_range / gate_passivity_range over
  [47.5,54.5]deg -- the 90-theta_beam envelope this construction actually
  evaluates reflection_coefficient_vec at, currently only hand-checked in
  a Phase-5 review, never a committed gate.

  Item 3 (THERMODYNAMICS, own charter): price the geometric-interception x
  material-reflectivity energy budget -- what fraction of total scene power
  the echo path could carry, even a crude upper bound. Reproduces/checks
  PLAN.md's own "<=0.15% before any interception factor at ABSORB=40"
  anchor (d80.part_c_power_budget_at_true_angle(), the 90-theta_beam
  convention), then computes the SAME quantity at the physically-correct
  theta_local(y_s) angle convention (EM's own item-4 finding).

  Item 4 (MATERIALS, hygiene): docstring fix applied directly to
  experiments/080-.../validity_precheck.py (see that file's own diff,
  applied alongside this script -- not duplicated here).

ZERO new FDTD calls. Imports, never reimplements:
  - experiments/065-.../design_geometry.py (dg065): CONFIGS.
  - experiments/075-.../boundary_reflectance.py (br): CPL, ABSORB_LIST,
    damp_e_profile/nu_profile/n_profile_exact.
  - experiments/079-.../y_wall_aperture_sum.py (ywas): theta_local_deg,
    dist_image_cells, aperture_amplitude, source_driven_phase,
    reflection_coefficient_vec, build_aperture_grid, echo_field_curve,
    _trapz, K600, CONGRUENT_KEYS, rel_dev, score_period.
  - experiments/078-.../y_wall_prescreen.py (ywp, via ywas re-export):
    free_period_with_widening, _free_period_search, SS_TOT_DEGENERATE_FLOOR.
  - experiments/080-.../validity_precheck.py (d80): photonics_image_term_
    curve, reflection_coefficient_vec_realizable, part_c_power_budget_at_
    true_angle.
  - experiments/076-.../results.json::headline: the REAL, already-collected
    C40/G40/C80 dense 31-point/600nm/settled-STEPS=2800 sweep -- read
    (never hand-typed, R4) as the real reference data every period
    comparison is scored against.

Run: `python3 photonics_construction.py` from this directory (or anywhere --
paths resolve from __file__). Writes `phase1_results.json` and prints every
table below; every number appended to phase1_proposal.md's "PHASE 1 RESULTS"
section is copied from that JSON/stdout, never hand-typed (R4).
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
    """House `_load()` pattern (boundary_reflectance.py / y_wall_prescreen.py
    / y_wall_aperture_sum.py / validity_precheck.py's own convention) for
    filename collisions across experiment directories."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP065_DIR = os.path.join(ROOT, "experiments", "065-t24-absorb-boundary-sweep")
EXP075_DIR = os.path.join(ROOT, "experiments", "075-t28-absorb-boundary-wkb-reflectance")
EXP076_RESULTS = os.path.join(ROOT, "experiments", "076-t28-g40-pad-decorrelation", "results.json")
EXP079_DIR = os.path.join(ROOT, "experiments", "079-t28-y-wall-full-aperture-sum")
EXP080_DIR = os.path.join(ROOT, "experiments", "080-t28-y-wall-planewave-validity-precheck")

dg065 = _load(os.path.join(EXP065_DIR, "design_geometry.py"), "_exp081_dg065")
br = _load(os.path.join(EXP075_DIR, "boundary_reflectance.py"), "_exp081_br")
ywas = _load(os.path.join(EXP079_DIR, "y_wall_aperture_sum.py"), "_exp081_ywas")
d80 = _load(os.path.join(EXP080_DIR, "validity_precheck.py"), "_exp081_d80")

CONGRUENT_KEYS = ywas.CONGRUENT_KEYS  # ("C40","C60","C70","C80","G40")
LAM600 = br.CPL[600]
K600 = ywas.K600
score_period = ywas.score_period
rel_dev = ywas.rel_dev
free_period_with_widening = ywas.free_period_with_widening

with open(EXP076_RESULTS) as f:
    RES76 = json.load(f)
THETAS = np.array(RES76["headline"]["theta"])


# ============================================================ ITEM 1 / 1b
def dist_direct_cells(y_s, cfg):
    """PHOTONICS' own exp-080 Phase-5 formula (phase5_review_photonics.md
    Sec 4), cited verbatim, NOT re-derived: 'the SAME taper and driven-
    phase convention as the echo term, propagated over the DIRECT
    (non-mirrored) source-to-observer distance hypot(D_SP, OBJ_Y-y_s), no
    wall, no r()'. Distinguished from ywas.dist_image_cells (OBJ_Y+y_s,
    the MIRRORED/echo-path distance) only by the sign on y_s."""
    d_sp = cfg["d_sp"]
    return np.hypot(d_sp, cfg["obj_y"] - np.asarray(y_s, dtype=float))


def e_direct_curve(cfg, thetas_beam_deg, oversample=1):
    """E_direct(theta_beam) = integral over y_s of amp(y_s)*exp(i*[phase_
    drive(y_s,theta_beam) + K*dist_direct(y_s)]) dy_s -- the direct
    (unmirrored, no wall, no r()) Huygens sum from the real source aperture
    to the real observer, reusing ywas.aperture_amplitude/source_driven_
    phase/build_aperture_grid/_trapz unchanged; only dist_direct (above) is
    new to this file."""
    y_grid = ywas.build_aperture_grid(cfg, oversample)
    amp = ywas.aperture_amplitude(y_grid, cfg)
    dist_dir = dist_direct_cells(y_grid, cfg)
    curve = []
    for th_beam in thetas_beam_deg:
        phase_drive = ywas.source_driven_phase(y_grid, float(th_beam), cfg)
        integrand = amp * np.exp(1j * (phase_drive + K600 * dist_dir))
        re = float(ywas._trapz(integrand.real, y_grid))
        im = float(ywas._trapz(integrand.imag, y_grid))
        curve.append(complex(re, im))
    return np.array(curve, dtype=complex)


def e_total_curve(cfg, thetas_beam_deg):
    """E(theta_beam) = E_direct(theta_beam) + r(90-theta_beam;ABSORB)*
    W(theta_beam) -- PHOTONICS' own exp-079 Sec4 total-field construction,
    built in full for the first time in this nine-cycle T28 y-wall
    sub-thread. The second term is d80.photonics_image_term_curve(),
    reused UNCHANGED (already independently reproduced 3x in exp-080's own
    record) -- not reimplemented here."""
    e_dir = e_direct_curve(cfg, thetas_beam_deg)
    e_img = d80.photonics_image_term_curve(cfg, cfg["absorb"], thetas_beam_deg)
    return e_dir, e_img, e_dir + e_img


def item1_e_direct_pad_invariance():
    """Numerical re-verification (not a re-derivation) of PHOTONICS' own
    exp-080 Phase-5 proof: E_direct(theta_beam) is bit-identical across all
    5 congruent configs, at every theta_beam -- because D_SP/aperture_cells
    are congruent-series constants and the aperture is symmetric about
    OBJ_Y (0.5*(y_lo+y_hi)==obj_y), so substituting u=y_s-OBJ_Y makes every
    ingredient (amp, phase_drive, dist_direct) a function of u alone, with
    NO PAD or ABSORB dependence anywhere."""
    curves = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        mid = 0.5 * (c["y_lo"] + c["y_hi"])
        assert mid == c["obj_y"], (key, mid, c["obj_y"])
        curves[key] = e_direct_curve(c, THETAS)
    ref = curves["C40"]
    max_dev = {key: float(np.max(np.abs(curves[key] - ref))) for key in CONGRUENT_KEYS}
    all_zero = all(v == 0.0 for v in max_dev.values())
    return dict(max_abs_dev_vs_C40=max_dev, bit_identical_all_zero=bool(all_zero))


def item1_build_and_score():
    """Build E_total per config, form the 3 pair-deltas (PRIMARY proxy
    Re{E_total}, this sub-thread's own house convention), and score each
    via the SAME imported _free_period_search/staged-widening machinery
    against REAL T28 reference periods recomputed fresh from
    experiments/076-.../results.json::headline (never hand-typed, R4) --
    the SAME idiom y_wall_aperture_sum.py Sec[3] uses."""
    # ---- REAL reference periods, recomputed fresh (R4) ----
    real_c40 = np.array(RES76["headline"]["C40"])
    real_g40 = np.array(RES76["headline"]["G40"])
    real_c80 = np.array(RES76["headline"]["C80"])
    real_delta_pad = real_g40 - real_c40
    real_delta_absorb40 = real_c80 - real_g40
    real_delta_c80c40 = real_c80 - real_c40

    real_stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    real_free_pad = free_period_with_widening(THETAS, real_delta_pad, "real PAIR_PAD", real_stages["pair_pad"])
    real_free_absorb40 = free_period_with_widening(THETAS, real_delta_absorb40, "real PAIR_ABSORB40",
                                                    real_stages["pair_absorb40"])
    real_free_c80c40 = free_period_with_widening(THETAS, real_delta_c80c40, "real C80-C40", real_stages["c80_c40"])
    reference_periods = dict(pair_pad_deg=real_free_pad["p_star_deg"],
                              pair_absorb40_deg=real_free_absorb40["p_star_deg"],
                              c80_c40_deg=real_free_c80c40["p_star_deg"])

    # ---- build E_total per config ----
    e_dir = {}
    e_img = {}
    e_tot = {}
    for key in CONGRUENT_KEYS:
        c = dg065.CONFIGS[key]
        ed, ei, et = e_total_curve(c, THETAS)
        e_dir[key], e_img[key], e_tot[key] = ed, ei, et

    # ---- item 1b: does E_direct change the pair-delta scores at all? ----
    model_delta_pad_total = (e_tot["G40"] - e_tot["C40"]).real
    model_delta_absorb40_total = (e_tot["C80"] - e_tot["G40"]).real
    model_delta_c80c40_total = (e_tot["C80"] - e_tot["C40"]).real

    model_delta_pad_image_only = (e_img["G40"] - e_img["C40"]).real
    model_delta_absorb40_image_only = (e_img["C80"] - e_img["G40"]).real
    model_delta_c80c40_image_only = (e_img["C80"] - e_img["C40"]).real

    item1b = dict(
        max_abs_diff_pair_pad=float(np.max(np.abs(model_delta_pad_total - model_delta_pad_image_only))),
        max_abs_diff_pair_absorb40=float(np.max(np.abs(model_delta_absorb40_total - model_delta_absorb40_image_only))),
        max_abs_diff_c80_c40=float(np.max(np.abs(model_delta_c80c40_total - model_delta_c80c40_image_only))),
    )
    item1b["all_exactly_zero"] = bool(all(v == 0.0 for v in item1b.values()))

    # ---- score the (identical, per 1b) total-field pair-deltas ----
    stages = {"pair_pad": [], "pair_absorb40": [], "c80_c40": []}
    fp_pad = free_period_with_widening(THETAS, model_delta_pad_total, "model(total) PAIR_PAD", stages["pair_pad"])
    fp_absorb40 = free_period_with_widening(THETAS, model_delta_absorb40_total, "model(total) PAIR_ABSORB40",
                                             stages["pair_absorb40"])
    fp_c80c40 = free_period_with_widening(THETAS, model_delta_c80c40_total, "model(total) C80-C40",
                                           stages["c80_c40"])

    scores = {}
    scores["pair_pad"] = score_period("model(total) PAIR_PAD vs real", reference_periods["pair_pad_deg"],
                                       fp_pad["p_star_deg"])
    scores["pair_absorb40"] = score_period("model(total) PAIR_ABSORB40 vs real",
                                            reference_periods["pair_absorb40_deg"], fp_absorb40["p_star_deg"])
    scores["c80_c40"] = score_period("model(total) C80-C40 vs real", reference_periods["c80_c40_deg"],
                                      fp_c80c40["p_star_deg"])

    verdicts = [scores[k]["verdict"] for k in ("pair_pad", "pair_absorb40", "c80_c40")]
    if all(v == "SUPPORT" for v in verdicts):
        combined = "SUPPORT"
    elif all(v == "REFUTE" for v in verdicts):
        combined = "REFUTE"
    else:
        combined = "NEITHER"

    # ---- ss_tot sanity guard (exp-078/079's own SS_TOT_DEGENERATE hardening) ----
    ss_tot = {}
    for name, arr in (("pair_pad", model_delta_pad_total), ("pair_absorb40", model_delta_absorb40_total),
                       ("c80_c40", model_delta_c80c40_total)):
        ss_tot[name] = float(np.sum((arr - np.mean(arr)) ** 2))
        ss_tot[f"{name}_degenerate"] = bool(ss_tot[name] < ywas.SS_TOT_DEGENERATE_FLOOR)

    # ---- item 1c: T21-proximity diagnostic (this sub-thread's own
    # established look-elsewhere scrutiny -- y_wall_aperture_sum.py Sec
    # [6a]: how close are the model's own three periods to T21's OWN
    # established fringe (1.9608deg, A=752, 39deg, 600nm) vs to T28's own
    # real targets? A model landing closer to T21 than to its own scored
    # target is a disclosed look-elsewhere risk on any SUPPORT verdict --
    # not a new gate, a disclosed diagnostic, per R5's own house discipline.
    t21_ref = dg065.dg048.ripple_period_deg(752, LAM600, 39.0)
    vs_t21 = {}
    for name, fp in (("pair_pad", fp_pad), ("pair_absorb40", fp_absorb40), ("c80_c40", fp_c80c40)):
        p_model = fp["p_star_deg"]
        rd_t21 = rel_dev(t21_ref, p_model)
        rd_real = scores[name]["rel_dev"]
        vs_t21[name] = dict(p_model_deg=p_model, rel_dev_vs_t21_fringe=rd_t21,
                             rel_dev_vs_t28_real_target=rd_real,
                             closer_to_t21_than_to_t28=bool(rd_t21 < rd_real))

    return dict(
        reference_periods=reference_periods, real_stages=real_stages,
        model_free_periods=dict(pair_pad=fp_pad, pair_absorb40=fp_absorb40, c80_c40=fp_c80c40),
        model_stages=stages, scores=scores, verdicts=verdicts, combined_verdict=combined,
        item1b_e_direct_cancellation=item1b, ss_tot_sanity=ss_tot,
        item1c_t21_proximity_diagnostic=dict(t21_fringe_period_deg=t21_ref, per_pair=vs_t21),
    )


# ============================================================ ITEM 2 (EM)
def gate_lossless_unimodular_range(lo, hi, n_trials=2000, seed=53):
    """Same pattern as y_wall_aperture_sum.py::gate_lossless_unimodular_range
    (near-verbatim), applied at a NEW angle range -- not a new gate design."""
    rng = np.random.default_rng(seed)
    worst = 0.0
    for _ in range(n_trials):
        length = int(rng.integers(5, 60))
        n_prof = 1.0 + 0.6 * rng.random(length)
        theta_deg = float(rng.uniform(lo, hi))
        r = br.reflection_coefficient(n_prof.astype(complex), theta_deg, LAM600)
        worst = max(worst, abs(abs(r) - 1.0))
    return worst


def gate_single_layer_identity_range(lo, hi, n_trials=2000, seed=59):
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


def gate_passivity_range(lo, hi, n_trials=2000, seed=61):
    rng = np.random.default_rng(seed)
    worst = 0.0
    for absorb in br.ABSORB_LIST:
        damp = br.damp_e_profile(absorb)
        nu = br.nu_profile(damp)
        n_exact = br.n_profile_exact(nu, 2.0 * math.pi / LAM600)
        for _ in range(n_trials // len(br.ABSORB_LIST)):
            theta_deg = float(rng.uniform(lo, hi))
            r = br.reflection_coefficient(n_exact, theta_deg, LAM600)
            worst = max(worst, abs(r))
    return worst


def item2_gate_rerun(lo=47.5, hi=54.5):
    g_lossless = gate_lossless_unimodular_range(lo, hi)
    g_n1 = gate_single_layer_identity_range(lo, hi)
    g_pass = gate_passivity_range(lo, hi)
    out = dict(
        range_deg=[lo, hi],
        g_lossless_worst_dev=g_lossless, g_lossless_pass=bool(g_lossless < 1e-9),
        g_n1_worst_dev=g_n1, g_n1_pass=bool(g_n1 < 1e-12),
        g_passivity_worst_abs_r=g_pass, g_passivity_pass=bool(g_pass <= 1.0 + 1e-9),
    )
    out["all_pass"] = bool(out["g_lossless_pass"] and out["g_n1_pass"] and out["g_passivity_pass"])
    return out


# =================================================== ITEM 3 (THERMODYNAMICS)
def item3_energy_budget():
    """Price the geometric-interception x material-reflectivity energy
    budget: what fraction of total scene power the echo path could carry,
    even a crude upper bound. Two parts:

      (i) reproduce/check the already-committed PLAN.md anchor
          (<=0.15% at ABSORB=40, 90-theta_beam convention, matched
          admittance) by calling d80.part_c_power_budget_at_true_angle()
          directly -- never hand-typed.
      (ii) price the SAME quantity at the physically-correct
          theta_local(y_s) angle convention (EM's own item-4 finding: a
          valid global-angle y-wall construction needs an angle convention
          built from theta_local(y_s)'s own fixed-observer geometry, not
          the borrowed theta_beam-steering convention (i) uses) -- both
          admittance families (matched AND realizable, MATERIALS' own
          item-4 point: the realizable number is the only one that could
          ever describe a real material).

    Interception factor is upper-bounded at 1 throughout (idealization 5,
    phase1_proposal.md) -- the maximally generous assumption that ALL of
    the source's radiated power reaches the wall. This can only make the
    reported bound LOOSER (larger), never tighter -- a genuine upper bound
    on "what fraction of total scene power the echo path could carry",
    not a point estimate of the true (necessarily smaller) fraction.
    """
    # (i) reproduce the already-committed anchor, at the theta_beam convention
    part_c = d80.part_c_power_budget_at_true_angle()
    anchor_absorb40_max = part_c["absorb_40"]["reflected_power_fraction_max"]

    # (ii) price at the physically-correct theta_local(y_s) envelope, per
    # ABSORB depth, both admittance families -- max over the FULL observed
    # per-config theta_local envelope (the tightest defensible "worst case"
    # given the true fixed-observer geometry), interception factor = 1.
    out_true_angle = {}
    for absorb in br.ABSORB_LIST:
        n_prof = br.n_profile_exact(br.nu_profile(br.damp_e_profile(absorb)), 2.0 * math.pi / LAM600)
        # theta_local envelope across ALL 5 congruent configs at this ABSORB
        # depth's own config(s) -- reuse the per-config envelope exactly as
        # validity_precheck.py's part_a() computes it.
        envs = []
        for key in CONGRUENT_KEYS:
            c = dg065.CONFIGS[key]
            if c["absorb"] != absorb:
                continue
            y_edges = np.array([c["y_lo"], c["y_hi"]])
            th_edges = ywas.theta_local_deg(y_edges, c)
            envs.append(th_edges)
        envs = np.concatenate(envs)
        r_matched = ywas.reflection_coefficient_vec(n_prof, envs, LAM600)
        r_realizable = d80.reflection_coefficient_vec_realizable(n_prof, envs, LAM600)
        r2_matched = np.abs(r_matched) ** 2
        r2_realizable = np.abs(r_realizable) ** 2
        out_true_angle[f"absorb_{absorb}"] = dict(
            theta_local_envelope_deg=[float(envs.min()), float(envs.max())],
            reflected_power_fraction_matched_max=float(r2_matched.max()),
            reflected_power_fraction_matched_min=float(r2_matched.min()),
            reflected_power_fraction_realizable_max=float(r2_realizable.max()),
            reflected_power_fraction_realizable_min=float(r2_realizable.min()),
        )

    true_angle_absorb40_matched_max = out_true_angle["absorb_40"]["reflected_power_fraction_matched_max"]
    true_angle_absorb40_realizable_max = out_true_angle["absorb_40"]["reflected_power_fraction_realizable_max"]

    return dict(
        interception_factor_upper_bound=1.0,
        theta_beam_convention_anchor=dict(
            note="d80.part_c_power_budget_at_true_angle(), 90-theta_beam convention, "
                 "matched admittance -- reproduces PLAN.md's own <=0.15% anchor",
            per_absorb=part_c, absorb40_max=anchor_absorb40_max,
        ),
        theta_local_convention=dict(
            note="physically-correct fixed-observer angle (EM's own item-4 finding), "
                 "both admittance families, max over the FULL per-ABSORB theta_local envelope",
            per_absorb=out_true_angle,
            absorb40_matched_max=true_angle_absorb40_matched_max,
            absorb40_realizable_max=true_angle_absorb40_realizable_max,
        ),
        ratio_theta_beam_over_theta_local_matched_absorb40=(
            anchor_absorb40_max / true_angle_absorb40_matched_max
            if true_angle_absorb40_matched_max > 0 else float("inf")),
        theta_local_bound_is_smaller=bool(true_angle_absorb40_matched_max < anchor_absorb40_max),
    )


def main():
    print("=" * 78)
    print("exp-081 -- PHOTONICS' construction, AS ORIGINALLY SPECIFIED: total")
    print("field, scored via free-period fit against REAL T28 reference periods")
    print("=" * 78)

    print("\n[1a] E_direct PAD-invariance -- numerical re-verification of")
    print("     PHOTONICS' own exp-080 Phase-5 proof (cited, not re-derived)")
    inv = item1_e_direct_pad_invariance()
    for key, dev in inv["max_abs_dev_vs_C40"].items():
        print(f"    max|E_direct({key})-E_direct(C40)| = {dev:.3e}")
    print(f"    bit-identical across all 5 configs: {inv['bit_identical_all_zero']}")

    print("\n[1b/1] Build E_total = E_direct + E_image, form 3 pair-deltas,")
    print("       check E_direct's effect on the pair-delta scores, then score")
    print("       via _free_period_search against REAL T28 reference periods")
    res1 = item1_build_and_score()
    print(f"    REFERENCE_PERIODS (recomputed fresh from exp-076 headline): "
          f"{res1['reference_periods']}")
    print("    item 1b -- does E_direct change the pair-delta scores at all?")
    for k, v in res1["item1b_e_direct_cancellation"].items():
        print(f"      {k} = {v}")
    for name in ("pair_pad", "pair_absorb40", "c80_c40"):
        s = res1["scores"][name]
        print(f"    {name}: P*_real={s['p_real_deg']:.4f}deg  "
              f"P*_model={s['p_model_deg']:.4f}deg  rel_dev={s['rel_dev']:.4f} "
              f"-> {s['verdict']}")
    print(f"    Combined Verdict: {res1['combined_verdict']}")
    print(f"    ss_tot sanity: {res1['ss_tot_sanity']}")
    print("    [1c] T21-proximity diagnostic (look-elsewhere disclosure, "
          f"T21 fringe={res1['item1c_t21_proximity_diagnostic']['t21_fringe_period_deg']:.4f}deg):")
    for name, v in res1["item1c_t21_proximity_diagnostic"]["per_pair"].items():
        print(f"      {name}: P*_model={v['p_model_deg']:.4f}deg  "
              f"rel_dev_vs_T21={v['rel_dev_vs_t21_fringe']:.4f}  "
              f"rel_dev_vs_T28_real={v['rel_dev_vs_t28_real_target']:.4f}  "
              f"closer_to_T21={v['closer_to_t21_than_to_t28']}")

    print("\n[2] EM gate re-run at [47.5,54.5]deg")
    res2 = item2_gate_rerun()
    print(f"    G-LOSSLESS worst ||r|-1| = {res2['g_lossless_worst_dev']:.3e}  "
          f"PASS={res2['g_lossless_pass']}")
    print(f"    G-N1       worst |r_loop-r_direct| = {res2['g_n1_worst_dev']:.3e}  "
          f"PASS={res2['g_n1_pass']}")
    print(f"    G-PASSIVITY worst |r| = {res2['g_passivity_worst_abs_r']:.6f}  "
          f"PASS={res2['g_passivity_pass']}")
    print(f"    ALL PASS: {res2['all_pass']}")
    assert res2["all_pass"], "gate re-run at [47.5,54.5]deg FAILED -- do not trust item 1"

    print("\n[3] THERMODYNAMICS energy budget: geometric-interception x")
    print("    material-reflectivity upper bound")
    res3 = item3_energy_budget()
    print(f"    theta_beam-convention anchor (ABSORB=40, matched, max) = "
          f"{res3['theta_beam_convention_anchor']['absorb40_max']:.4e} "
          f"({res3['theta_beam_convention_anchor']['absorb40_max']*100:.4f}%)")
    print(f"    theta_local-convention (ABSORB=40, matched, max) = "
          f"{res3['theta_local_convention']['absorb40_matched_max']:.4e}")
    print(f"    theta_local-convention (ABSORB=40, realizable, max) = "
          f"{res3['theta_local_convention']['absorb40_realizable_max']:.4e}")
    print(f"    theta_local bound smaller than theta_beam anchor: "
          f"{res3['theta_local_bound_is_smaller']}")
    print(f"    ratio (theta_beam anchor / theta_local matched) = "
          f"{res3['ratio_theta_beam_over_theta_local_matched_absorb40']:.4e}")

    print("\n[4] MATERIALS hygiene: docstring fix applied directly to")
    print("    experiments/080-.../validity_precheck.py (see that file's diff)")

    out = dict(
        item1a_e_direct_pad_invariance=inv,
        item1_build_and_score=res1,
        item2_gate_rerun=res2,
        item3_energy_budget=res3,
        item4_note="docstring fix applied to experiments/080-.../validity_precheck.py "
                   "-- reflection_coefficient_vec_realizable(), mu_r=ni^2 -> mu_r=ni",
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
        if isinstance(o, complex):
            return dict(re=o.real, im=o.imag)
        raise TypeError(f"not JSON serializable: {type(o)}")

    out_path = os.path.join(HERE, "phase1_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=_json_default)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
