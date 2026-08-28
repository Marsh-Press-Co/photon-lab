"""exp-087 -- T28 Energy-Interception Cross-Check: a purpose-built Poynting-
box measurement of PAIR_PAD's absorbed/extinguished power on the article-
loaded scene, discharging the Iteration-59 forward tripwire.
=============================================================================
Panel Iteration 64 (lead: THERMODYNAMICS, by rotation). Frozen spec:
phase3_synthesis.md (all 10 Phase-2 Red Team mandatory-fix-docket items
adopted, zero overridden). Predictions (NOTES.md P1-P8 + the non-negativity
gate) committed to git strictly BEFORE this file's first run (house
discipline, non-negotiable).

Reuses exp-083's own `_load()` idiom to import its `dg` (dg069, itself
dg065's re-export), `build_article`, and `_run_sim` VERBATIM, UNMODIFIED --
zero geometry retyped. Applies `lab.sections.widths()` (already stage-8-
gated Poynting-box machinery) to the article-loaded PAIR_PAD scene for the
first time in this sub-thread's history, at a disclosed, non-uniformly-
spaced 3-angle subset ({36.0, 38.6, 41.8} deg = dg069.DENSE_ANGLES[0,13,29])
chosen to break the aliasing risk (Phase-2 mandatory fix 2) the original
uniform 3.0deg spacing carried against P*=2.9474deg.

Zero new `lab/` machinery -- every primitive reused (Sim; materials.pec_disk/
graded_black_shell, stage 7; sections.full_capture/phasors/widths, stage 8;
ambient.contrast_from_runs, stage 9; thermo_sidecar.absorbed_power_
established_ratio/mixed_length_scale_regime/netd_disposition, stage 15) is
already gated.
"""

import importlib.util
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    """House `_load()` pattern (exp-078/079/080/081/082/083's own idiom for
    cross-experiment-directory imports)."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


EXP083_DIR = os.path.join(ROOT, "experiments", "083-t28-pad-article-full-power-retest")
EXP083_RESULTS = os.path.join(EXP083_DIR, "results.json")

# exp-083's own run.py: module-level code re-derives dg (=dg069), defines
# build_article()/_run_sim() -- reused verbatim, not retyped. Its own
# top-level asserts/JSON loads execute harmlessly on import (same idiom
# exp-083 itself used to load exp-077's pad_round_trip_model.py).
exp083 = _load(os.path.join(EXP083_DIR, "run.py"), "_exp087_exp083")
dg = exp083.dg
build_article = exp083.build_article
_run_sim = exp083._run_sim

from lab import Sim, sections as sc, ambient as amb, thermo_sidecar as ts  # noqa: E402

PAIR_KEYS = ("C40", "G40")
ANGLES = [dg.DENSE_ANGLES[0], dg.DENSE_ANGLES[13], dg.DENSE_ANGLES[29]]  # 36.0, 38.6, 41.8
assert ANGLES == [36.0, 38.6, 41.8], f"angle grid drifted: {ANGLES}"
STEPS_MAIN = dg.STEPS_SETTLED           # 2800, T28's own established settled value
STEPS_SETTLE_CHECK = 1400
SETTLE_CFG, SETTLE_THETA = "G40", 38.6

BOX_CLEARANCE_A = 12   # exp-024's established convention (R_OUT + 12)
BOX_CLEARANCE_B = 24   # box-independence companion (R_OUT + 24), Phase-2 P3
REF_HALF_H = 80        # exp-024's established REF=(OBJ_X,OBJ_Y,80) convention

DX_M = 30.0e-9
R_OUT_CELLS = dg.R_OUT                  # 78
L_GEOMETRIC_M = R_OUT_CELLS * DX_M      # 2.34e-6 m, length_provenance="bench_construction"

# exp-043's sourced WitnessScenario irradiance, exp-057's thermal constants --
# reused verbatim, not re-derived/re-searched this cycle (Idealizations 4-5).
IRR_CENTRAL_W_CM2 = 6.584362139917695e-06
K_AIR = 0.026
DENSITY_SI_KG_M3, C_P_SI_J_KGK = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15
NETD_BAND_K = (0.020, 0.050)

# Historical material-identity swing magnitudes (Phase-2 mandatory fix 6,
# MATERIALS' triage rule) -- cited, not recomputed.
BIOT_SWING_X = 780.0     # Iteration 22 / exp-045
H_CONV_SWING_X = 116.0   # Iteration 34 / exp-057

XI_TOL = 0.12             # stage 8's own extinction-routes-agreement tolerance
NOISE_MULT = 3.0          # box-dev noise-floor multiplier (house-style, disclosed)
RATIO_LOW, RATIO_HIGH = 0.1, 10.0

# T28's own two currently-cited confound periods (context for the aliasing-
# risk log, Phase-2 mandatory fix 10) -- cited from already-committed JSON,
# never hand-typed.
with open(os.path.join(ROOT, "experiments", "069-t21-block-mini-period-match-power-up",
                        "results.json")) as _f:
    P_EDGE_A = json.load(_f)["scored"]["p3"]["p_star_deg"]
# exp-083's own real, decisively-resolved 31-point fit on delta_scene(theta)
# (branch B_ARTICLE_EDGE_DIFFRACTION) -- NOT exp-077's older P_CONTINUITY
# reference band. This is the period Red Team's Phase-2 audit's aliasing
# attack (phase2_redteam_audit.md Sec 1c) is about.
with open(EXP083_RESULTS) as _f:
    P_STAR = json.load(_f)["primary_period_discriminator"]["p_star_deg"]
assert abs(P_STAR - 2.9473684210526314) < 1e-9, f"P_STAR citation drifted: {P_STAR}"


def box_for(cfg, clearance):
    ox, oy = cfg["obj_x"], cfg["obj_y"]
    r = R_OUT_CELLS + clearance
    return (ox - r, ox + r, oy - r, oy + r)


def ref_for(cfg):
    return (cfg["obj_x"], cfg["obj_y"], REF_HALF_H)


def widths_direction_corrected(cap_scene, cap_empty, box, ref):
    """Wraps `lab.sections.widths()` with a caller-side propagation-direction
    correction -- NOT a modification to lab/sections.py (zero lab/ diff this
    cycle, unchanged discipline).

    `widths()`'s own `i_inc` is a SIGNED +x-direction flux at the reference
    strip (lab/sections.py's own `sx()` convention). CORRECTED (Phase 5,
    EM's review + Red Team's final audit -- the original text here claimed
    this was the first `widths()` application with `src_x > obj_x >
    plane_x`; that is FALSE, independently confirmed from source):
    exp-002's absorber bench (`SRC_X=64 < CX=252`) does propagate in +x,
    but exp-024 (`experiments/024-ambient-margin-adjudication`, Panel
    Iteration 2) has `SRC_X=300 > OBJ_X=170 > PLANE_X=77` -- the IDENTICAL
    -x-propagating relationship T28's PAIR_PAD geometry has -- and its own
    `run.py` (lines 195-199) already defensively wraps `abs()` around
    `sigma_abs*i_inc` and `net_box_flux`, strong evidence the same sign
    issue was present, silently absorbed, and never diagnosed since
    Iteration 2. T28's PAIR_PAD geometry (`src_x > obj_x > plane_x`,
    confirmed from `dg069.CONFIGS`) is the first time this hazard has been
    NAMED and traced to source, not the first time the underlying geometry
    has existed -- the wave propagates in -x, so the SAME
    reference-strip flux measurement is, correctly, NEGATIVE. Since
    `sigma_scat`/`sigma_abs`/`sigma_ext`/`sigma_ext_cross` are each a power
    divided by this one signed i_inc, all four flip sign together (confirmed
    empirically this cycle: uniformly negative, at every (cfg,angle,box,leg)
    cell, both extinction routes agreeing on the same sign to <0.05% --
    i.e. NOT scattered noise, a single, consistent, explicable sign
    convention mismatch). The physically correct normalizer for a
    cross-section is the incident intensity's MAGNITUDE (always >=0 by
    definition), not a directionally-signed flux -- so this wrapper
    recovers each raw power (`p_X = sigma_X * i_inc`) and re-divides by
    `abs(i_inc)`, equivalent to multiplying every sigma_* field by
    `sign(i_inc)`. `xi_ext` and `box_dev_*` (both already-computed,
    already-gated ratios of differences to magnitudes) are provably
    invariant to this correction -- multiplying both operands of a ratio by
    the same -1 changes neither |numerator| nor |denominator| -- so P3/P4's
    results, computed before this wrapper existed, are unaffected and not
    recomputed."""
    w = sc.widths(cap_scene, cap_empty, box, ref)
    s = 1.0 if w["i_inc"] >= 0 else -1.0
    out = dict(w)
    for key in ("sigma_scat", "sigma_abs", "sigma_ext", "sigma_ext_cross"):
        out[key] = w[key] * s
    out["i_inc"] = abs(w["i_inc"])
    out["direction_correction_sign_applied"] = s
    return out


# ------------------------------------------------------------- P1: vacuum footprint
def vacuum_footprint_check():
    """Zero-FDTD precondition: BOX_A/BOX_B footprints sit in pure vacuum
    (damp_e==1.0) for both configs -- HALT before any FDTD call otherwise."""
    report = {}
    all_pass = True
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        sim = Sim(cfg["nx"], cfg["ny"], cells_per_lambda=dg.CPL[600],
                  courant_frac=dg.COURANT_FRAC, absorb=cfg["absorb"])
        cell = {}
        for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A), ("BOX_B", BOX_CLEARANCE_B)):
            x0, x1, y0, y1 = box_for(cfg, clearance)
            footprint = sim.damp_e[x0:x1 + 1, y0:y1 + 1]
            ok = bool(np.all(footprint == 1.0))
            cell[box_name] = dict(box=[x0, x1, y0, y1], all_vacuum=ok)
            all_pass = all_pass and ok
        report[key] = cell
    return report, all_pass


# ---------------------------------------------------- P5 (synthetic classifier recovery)
def _label(ratio):
    if ratio > RATIO_HIGH:
        return "X"
    if ratio < RATIO_LOW:
        return "D"
    return "C"


def classify_resolved(ratios):
    """ratios: ratio_k values at RESOLVED angles only.
    Priority (matches phase3_synthesis.md's literal text order): ANY angle
    over RATIO_HIGH => ENERGY-DOMINANT outright; else all-D =>
    ENERGY-DECOUPLED; else all-C => CONSISTENT; else (a D/C mix, no X) =>
    MIXED. <2 resolved angles => DEGENERATE (checked by the caller)."""
    labels = [_label(r) for r in ratios]
    if "X" in labels:
        return "ENERGY-DOMINANT"
    if all(l == "D" for l in labels):
        return "ENERGY-DECOUPLED"
    if all(l == "C" for l in labels):
        return "CONSISTENT"
    return "MIXED"


def synthetic_recovery_check():
    """P5: the classifier's own bucket logic recovers the intended label at
    each decade-boundary synthetic single-angle case. Zero FDTD."""
    eps = 1e-6
    cases = [
        (0.05, "D"), (RATIO_LOW - eps, "D"), (RATIO_LOW, "C"), (RATIO_LOW + eps, "C"),
        (1.0, "C"), (RATIO_HIGH - eps, "C"), (RATIO_HIGH, "C"), (RATIO_HIGH + eps, "X"),
        (20.0, "X"),
    ]
    results = []
    all_pass = True
    for ratio, expected in cases:
        got = _label(ratio)
        ok = got == expected
        all_pass = all_pass and ok
        results.append(dict(ratio=ratio, expected=expected, got=got, pass_=ok))
    # also the 3-angle bucket-level recovery (one representative case per bucket)
    bucket_cases = [
        ([0.01, 0.02, 0.05], "ENERGY-DECOUPLED"),
        ([1.0, 2.0, 5.0], "CONSISTENT"),
        ([15.0, 20.0, 30.0], "ENERGY-DOMINANT"),
        ([0.01, 1.0, 0.02], "MIXED"),
        ([0.01, 15.0, 1.0], "ENERGY-DOMINANT"),  # any-X priority
    ]
    for ratios, expected in bucket_cases:
        got = classify_resolved(ratios)
        ok = got == expected
        all_pass = all_pass and ok
        results.append(dict(ratios=ratios, expected=expected, got=got, pass_=ok))
    return results, all_pass


def one_call(args):
    """Module-level (picklable) worker: (cfg_key, theta, with_article, steps)
    -> full_capture dict. Geometry re-derived from dg.CONFIGS by key, matching
    exp-083's own `one_call` picklability idiom."""
    key, th, art, steps = args
    cfg = dg.CONFIGS[key]
    cap = _run_sim(cfg, th, steps, art)
    return (key, th, art, steps, cap)


def main():
    print("=" * 78)
    print("exp-087 -- T28 energy-interception Poynting-box cross-check")
    print("=" * 78)

    # ---------------------------------------------------------------- P1
    vac_report, vac_pass = vacuum_footprint_check()
    print(f"\n[P1] vacuum-footprint precondition: PASS={vac_pass}")
    for key, cell in vac_report.items():
        for box_name, d in cell.items():
            print(f"  {key} {box_name} box={d['box']} all_vacuum={d['all_vacuum']}")
    assert vac_pass, "P1 FAILED -- a BOX_A/BOX_B footprint is not pure vacuum; HALT"

    # ---------------------------------------------------------------- P5 (desk, zero FDTD)
    recov_results, recov_pass = synthetic_recovery_check()
    print(f"\n[P5] synthetic classifier-recovery check: PASS={recov_pass}")
    for r in recov_results:
        print(f"  {r}")
    assert recov_pass, "P5 FAILED -- classifier does not recover its own decade boundaries; HALT"

    # ---------------------------------------------------------------- FDTD calls
    jobs = []
    for key in PAIR_KEYS:
        for th in ANGLES:
            jobs.append((key, th, False, STEPS_MAIN))   # empty
            jobs.append((key, th, True, STEPS_MAIN))    # article
    jobs.append((SETTLE_CFG, SETTLE_THETA, True, STEPS_SETTLE_CHECK))  # settling spot-check

    print(f"\n{len(jobs)} FDTD calls queued "
          f"(2 configs x 3 angles x 2 legs = 12, + 1 settling-check call)")
    t0 = time.time()
    captures = {}

    with ProcessPoolExecutor(max_workers=4) as ex:
        for n, (key, th, art, steps, cap) in enumerate(ex.map(one_call, jobs), 1):
            captures[(key, th, art, steps)] = cap
            print(f"  [{n:2d}/{len(jobs)}] {key} theta={th:+06.2f} "
                  f"article={art} steps={steps}", flush=True)
    total_wall = time.time() - t0
    print(f"\ntotal wall time: {total_wall:.1f}s")

    # ---------------------------------------------------------------- P2
    with open(EXP083_RESULTS) as f:
        res83 = json.load(f)
    per_theta_83 = res83["per_theta"]

    repro = {}
    max_dev = 0.0
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        for th in ANGLES:
            cap_empty = captures[(key, th, False, STEPS_MAIN)]
            cap_article = captures[(key, th, True, STEPS_MAIN)]
            empty_p = exp083._profile(cap_empty, cfg)
            article_p = exp083._profile(cap_article, cfg)
            # C_empty depends only on empty_profiles (lab/ambient.py::
            # contrast_from_runs), so this reproduces exp-083's own
            # per-theta C_empty figure exactly -- the article-loaded profile
            # is passed for call-shape parity with exp-083's own idiom only.
            r = amb.contrast_from_runs([article_p], [empty_p], [1.0],
                                        cfg["y_lo"], cfg["obj_y"], dg.W_OBJ,
                                        dg.GUARD_OUT, dg.W_FLANK)
            key_th = f"{th:.1f}"
            ref_c_empty = per_theta_83[key_th][f"{key}_Ce"]
            dev = abs(r["C_empty"] - ref_c_empty)
            repro.setdefault(key, {})[key_th] = dict(fresh=r["C_empty"], ref=ref_c_empty, dev=dev)
            max_dev = max(max_dev, dev)
    repro_pass = bool(max_dev < 1e-9)
    print(f"\n[P2] reproduction precondition: max_dev={max_dev:.3e} PASS(<1e-9)={repro_pass}")
    assert repro_pass, "P2 FAILED -- fresh empty leg does not reproduce exp-083; HALT"

    # ---------------------------------------------------------------- widths() + xi_ext (P3, P4)
    widths_by_cell = {}   # (key, th, box_name) -> widths dict
    box_dev = {}          # (key, th) -> {ext:.., abs:..}
    xi_ext = {}           # (key, th, box_name) -> value
    xi_pass = True
    for key in PAIR_KEYS:
        cfg = dg.CONFIGS[key]
        ref = ref_for(cfg)
        for th in ANGLES:
            cap_empty = captures[(key, th, False, STEPS_MAIN)]
            cap_article = captures[(key, th, True, STEPS_MAIN)]
            for box_name, clearance in (("BOX_A", BOX_CLEARANCE_A), ("BOX_B", BOX_CLEARANCE_B)):
                box = box_for(cfg, clearance)
                w = widths_direction_corrected(cap_article, cap_empty, box, ref)
                widths_by_cell[(key, th, box_name)] = w
                xi = abs(w["sigma_ext_cross"] - w["sigma_ext"]) / abs(w["sigma_ext"])
                xi_ext[(key, th, box_name)] = xi
                if xi > XI_TOL:
                    xi_pass = False
            ba, bb = widths_by_cell[(key, th, "BOX_A")], widths_by_cell[(key, th, "BOX_B")]
            box_dev[(key, th)] = dict(
                ext=abs(ba["sigma_ext"] - bb["sigma_ext"]) / abs(ba["sigma_ext"]),
                abs=abs(ba["sigma_abs"] - bb["sigma_abs"]) / abs(ba["sigma_abs"]),
            )

    print(f"\n[P3] box independence (box_dev) and [P4] xi_ext (extinction-routes agreement):")
    for (key, th, box_name), xi in sorted(xi_ext.items()):
        print(f"  {key} theta={th} {box_name}: xi_ext={xi:.6f}")
    for (key, th), d in sorted(box_dev.items()):
        print(f"  {key} theta={th}: box_dev_ext={d['ext']:.6f} box_dev_abs={d['abs']:.6f}")
    print(f"  [P4] xi_ext <= {XI_TOL} everywhere: PASS={xi_pass}")
    assert xi_pass, "P4 FAILED -- extinction-routes disagreement exceeds tolerance; HALT"

    # ---------------------------------------------------------------- non-negativity gate
    nonneg_pass = True
    for (key, th, box_name), w in sorted(widths_by_cell.items()):
        flag = "" if w["sigma_abs"] >= 0 else "  <<< NEGATIVE"
        print(f"  [widths, direction-corrected] {key} theta={th} {box_name}: "
              f"sigma_abs={w['sigma_abs']:.6f} sigma_scat={w['sigma_scat']:.6f} "
              f"sigma_ext={w['sigma_ext']:.6f}{flag}")
        if w["sigma_abs"] < 0:
            nonneg_pass = False
    print(f"\n[non-negativity gate] sigma_abs>=0 everywhere: PASS={nonneg_pass}")
    assert nonneg_pass, "non-negativity gate FAILED -- sign/phasor-convention bug; HALT"

    # ---------------------------------------------------------------- P8: thermo chain
    thermo = {}
    for key in PAIR_KEYS:
        for th in ANGLES:
            w = widths_by_cell[(key, th, "BOX_A")]
            sigma_ext_cells = w["sigma_ext"]
            ratio_abs_ext = w["sigma_abs"] / w["sigma_ext"] if w["sigma_ext"] != 0 else 0.0
            ratio_abs_ext_clamped = min(max(ratio_abs_ext, 0.0), 1.0)
            p = ts.absorbed_power_established_ratio(
                IRR_CENTRAL_W_CM2, sigma_ext_cells, DX_M, ratio_abs_ext_clamped)
            assert p["p_abs_w"] >= 0, "non-negativity gate FAILED on p_abs_w; HALT"
            regime = ts.mixed_length_scale_regime(
                p_abs_w=p["p_abs_w"], l_geometric_m=L_GEOMETRIC_M,
                k_air=K_AIR, density_kg_m3=DENSITY_SI_KG_M3, c_p_j_kgk=C_P_SI_J_KGK,
                emissivity=EMISSIVITY, t_ambient_k=T_AMBIENT_K,
                length_provenance="bench_construction")
            netd = ts.netd_disposition(regime["dt_ss_full_K"], NETD_BAND_K)
            thermo[(key, th)] = dict(
                sigma_ext_cells=sigma_ext_cells, ratio_abs_ext_raw=ratio_abs_ext,
                ratio_abs_ext_clamped=ratio_abs_ext_clamped,
                p_abs_w=p["p_abs_w"], dt_ss_full_K=regime["dt_ss_full_K"],
                netd_classification=netd["classification"],
                netd_disclaimer=netd["disclaimer"],
            )

    print("\n[P8] scene-specific detectability (NETD is an instrument threshold, "
          "NOT a human-eye one -- does not bear on constraint-3/4's human-eye verdict):")
    p8_all_undetectable = True
    for (key, th), d in sorted(thermo.items()):
        print(f"  {key} theta={th}: p_abs_w={d['p_abs_w']:.6e} W  "
              f"dt_ss={d['dt_ss_full_K']:.6e} K  {d['netd_classification']}")
        if d["netd_classification"] != "UNDETECTABLE":
            p8_all_undetectable = False
    if not p8_all_undetectable:
        print("  *** P8 departs from UNDETECTABLE -- pre-committed triage rule applies: "
              f"check against material-identity swing magnitudes (~{BIOT_SWING_X:.0f}x Biot, "
              f"~{H_CONV_SWING_X:.0f}x H_CONV) before reading as new physics. ***")

    # ---------------------------------------------------------------- PRIMARY: P7
    frac_p_abs = {}
    frac_contrast = {}
    ratio_k = {}
    resolved = {}
    for th in ANGLES:
        p_c40 = thermo[("C40", th)]["p_abs_w"]
        p_g40 = thermo[("G40", th)]["p_abs_w"]
        frac_p_abs[th] = abs(p_g40 - p_c40) / p_c40 if p_c40 != 0 else float("inf")

        key_th = f"{th:.1f}"
        c40_c = per_theta_83[key_th]["C40_C"]
        delta_scene = per_theta_83[key_th]["delta_scene"]
        frac_contrast[th] = abs(delta_scene) / abs(c40_c)

        ratio_k[th] = frac_p_abs[th] / frac_contrast[th] if frac_contrast[th] != 0 else float("inf")

        box_dev_max = max(box_dev[("C40", th)]["ext"], box_dev[("C40", th)]["abs"],
                           box_dev[("G40", th)]["ext"], box_dev[("G40", th)]["abs"])
        noise_floor = NOISE_MULT * box_dev_max * p_c40
        resolved[th] = bool(abs(p_g40 - p_c40) > noise_floor)

    n_resolved = sum(resolved.values())
    resolved_ratios = [ratio_k[th] for th in ANGLES if resolved[th]]
    p7_classification = "DEGENERATE" if n_resolved < 2 else classify_resolved(resolved_ratios)

    print("\n[PRIMARY P7] energy-interception cross-check classification:")
    for th in ANGLES:
        print(f"  theta={th}: frac_p_abs={frac_p_abs[th]:.6e}  "
              f"frac_contrast={frac_contrast[th]:.6e}  ratio_k={ratio_k[th]:.6e}  "
              f"resolved={resolved[th]}")
    print(f"  n_resolved={n_resolved}/3  CLASSIFICATION = {p7_classification}")

    # Phase-2 mandatory fix 10: aliasing-risk-band membership at result time
    gaps = [ANGLES[1] - ANGLES[0], ANGLES[2] - ANGLES[1]]
    alias_report = []
    for gap in gaps:
        for name, period in (("P_edge_A", P_EDGE_A), ("P_star", P_STAR)):
            cycles = gap / period
            frac_from_int = abs(cycles - round(cycles))
            alias_report.append(dict(gap_deg=gap, period_name=name, period_deg=period,
                                      cycles_per_gap=cycles, frac_from_integer_resonance=frac_from_int))
    print("\n[aliasing-risk-band log, Phase-2 fix 10]")
    for r in alias_report:
        print(f"  gap={r['gap_deg']}deg vs {r['period_name']}={r['period_deg']:.4f}deg: "
              f"{r['cycles_per_gap']:.4f} cycles/gap "
              f"({r['frac_from_integer_resonance']*100:.2f}% from exact resonance)")

    # ---------------------------------------------------------------- settling spot-check (P6)
    cap_empty_settle = captures[(SETTLE_CFG, SETTLE_THETA, False, STEPS_MAIN)]
    cap_article_2800 = captures[(SETTLE_CFG, SETTLE_THETA, True, STEPS_MAIN)]
    cap_article_1400 = captures[(SETTLE_CFG, SETTLE_THETA, True, STEPS_SETTLE_CHECK)]
    cfg_settle = dg.CONFIGS[SETTLE_CFG]
    ref_settle = ref_for(cfg_settle)
    box_a_settle = box_for(cfg_settle, BOX_CLEARANCE_A)
    w_2800 = widths_direction_corrected(cap_article_2800, cap_empty_settle, box_a_settle, ref_settle)
    w_1400 = widths_direction_corrected(cap_article_1400, cap_empty_settle, box_a_settle, ref_settle)
    settle_rel_dev_abs = abs(w_2800["sigma_abs"] - w_1400["sigma_abs"]) / abs(w_2800["sigma_abs"])
    settle_rel_dev_ext = abs(w_2800["sigma_ext"] - w_1400["sigma_ext"]) / abs(w_2800["sigma_ext"])
    print(f"\n[P6] settling spot-check ({SETTLE_CFG}, theta={SETTLE_THETA}, BOX_A): "
          f"rel_dev(sigma_abs)={settle_rel_dev_abs:.4e}  rel_dev(sigma_ext)={settle_rel_dev_ext:.4e}")

    # ---------------------------------------------------------------- persist
    def keystr(k):
        return f"{k[0]}_{k[1]}" if isinstance(k, tuple) and len(k) == 2 else str(k)

    out = dict(
        angles=ANGLES,
        pair_keys=PAIR_KEYS,
        steps_main=STEPS_MAIN,
        total_new_fdtd_calls=len(jobs),
        total_wall_time_s=total_wall,
        vacuum_footprint_check=vac_report,
        synthetic_recovery_check=dict(results=recov_results, all_pass=recov_pass),
        reproduction_precondition=dict(per_cell=repro, max_dev=max_dev, passed=repro_pass),
        widths={f"{k[0]}_{k[1]}_{k[2]}": v for k, v in widths_by_cell.items()},
        box_dev={f"{k[0]}_{k[1]}": v for k, v in box_dev.items()},
        xi_ext={f"{k[0]}_{k[1]}_{k[2]}": v for k, v in xi_ext.items()},
        xi_pass=xi_pass,
        nonneg_pass=nonneg_pass,
        thermo={f"{k[0]}_{k[1]}": v for k, v in thermo.items()},
        p8_all_undetectable=p8_all_undetectable,
        biot_swing_x=BIOT_SWING_X, h_conv_swing_x=H_CONV_SWING_X,
        frac_p_abs={str(k): v for k, v in frac_p_abs.items()},
        frac_contrast={str(k): v for k, v in frac_contrast.items()},
        ratio_k={str(k): v for k, v in ratio_k.items()},
        resolved={str(k): v for k, v in resolved.items()},
        n_resolved=n_resolved,
        p7_classification=p7_classification,
        p_edge_a=P_EDGE_A, p_star=P_STAR,
        aliasing_risk_log=alias_report,
        settling_spot_check=dict(
            cfg=SETTLE_CFG, theta=SETTLE_THETA,
            sigma_abs_2800=w_2800["sigma_abs"], sigma_abs_1400=w_1400["sigma_abs"],
            sigma_ext_2800=w_2800["sigma_ext"], sigma_ext_1400=w_1400["sigma_ext"],
            rel_dev_abs=settle_rel_dev_abs, rel_dev_ext=settle_rel_dev_ext),
        netd_disclaimer=("NETD is an instrument/detector threshold, not a human "
                          "perceptual one -- does NOT bear on constraint-3/4's "
                          "human-eye verdict."),
        scope_note=("This cross-check bears only on T28's own confound-mechanism "
                     "question and constraint-3's energy-ledger bookkeeping. It does "
                     "not test constraints 1/2/4, and does not re-open or re-score "
                     "REALIZABILITY_MEMO.md's verdict."),
    )
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nwrote {out_path}")
    return out


if __name__ == "__main__":
    main()
