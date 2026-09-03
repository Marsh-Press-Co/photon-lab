"""exp-107 -- Formal Retirement of the `delta_scene` R3-vs-R4-vs-R5
Question (text-only, no code here), plus Three `kappa_window` Tier-1
Closeouts. Panel Iteration 84. Frozen spec: NOTES.md (Predictions
committed to git strictly BEFORE this file's first real run, house
discipline). Change rationale: phase2_redteam_audit.md (6 numbered
attacks; all five blind critiques disposed, verdict
PROCEED-WITH-MANDATORY-FIXES).

This file executes ONLY the Tier-1 `kappa_window` closeouts (Tier 0 is
a governance/text decision, recorded in NOTES.md, zero code):

  Item 1: hollow-vs-PEC-cored `radial_absorbed_power`/`sections.widths()`
          delta on the fixed-absolute-thickness family, r=156/312.
          4 new `Sim.run()` calls (empty+hollow-article at each r) --
          NOT 2, correcting the Phase-1 proposal's own cost undercount
          (NOTES.md Synthesis). The PEC-cored comparator side is
          exp-106's own already-committed `ledger_r156/r312['fixedabs']`
          -- reused verbatim, not re-run.
  Item 3: real, non-placeholder P5 thermal row for both families at
          r=156/312, using exp-106's own already-persisted, REAL
          ledger-measured sigma_ext/abs_ext_ratio (not the
          Q_ext-invariance placeholder exp-105 used). Zero marginal
          FDTD cost -- pure desk recomputation, reproducibility-gated
          against NOTES.md's own pre-registered table.
  Item 4: numerator noise-floor check, folded into item 1 at zero
          additional FDTD cost -- `floor_gate_window()` applied to the
          SAME new hollow-article captures item 1 already produces.

Geometry (`geom_fixedabs()`) is re-derived HERE, byte-for-byte, from
exp-106's own formula chain, then cross-checked (Gate P0) against
exp-106's own committed `geom_156_fixedabs`/`geom_312_fixedabs` BEFORE
any new `Sim.run()` call -- if the reproduction fails, this script halts
before spending any FDTD budget.

**Director's disclosed execution-methodology correction (mid-cycle, this
shift, NOT a change to any predicted band or gate above).** This file's
own `main()`/`item1_and_4_one_r()`/`_run_hollow()` below describe the
ORIGINALLY INTENDED single-process execution path and are kept for
documentation/formula reference, but were NOT how items 1/4 were
actually executed. This session's own backgrounded/nohup process
execution mode was found, this shift, to run this FDTD workload
pathologically slowly (an isolated A/B test: foreground execution
reproduces exp-106's own historical per-step rate; the identical code
launched in the background accrued CPU time at roughly 1/10-1/20 that
rate over a >90-minute wall-clock window with zero completed output,
then was killed -- a pure CPU-bound Python loop was NOT similarly
slowed in the background, isolating this to the sustained large-array
numpy FDTD workload specifically under this session's background-task
execution mode; the trust suite, run directly foreground, was green in
104s at this shift's start, confirming this is an environment/tooling
characteristic of this remote session, not a `lab/` engine defect).
Items 1/4 were actually executed via `chunk_runner.py` (checkpoint/
resume Sim-object pickling across sequential foreground Bash calls,
2200-step chunks for r=312) and `finalize.py` (the exact same
`sections.widths()`/`radial_absorbed_power()`/`floor_gate_window()`
formulas as `item1_and_4_one_r()` below, applied to the saved capture
pickles) -- both committed here, and independently re-run at Phase 3.5
to confirm bit-exact reproduction of the numbers in `results.json`
before this correction note was written. Gate P0 and Item 3
(`item3_thermal_row()`) DID run exactly as designed, in-process, no
substitution needed (their combined cost is seconds, not minutes).
"""

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from lab import Sim, materials                      # noqa: E402
from lab import sections as sc                       # noqa: E402
from lab import thermo_sidecar as ts                 # noqa: E402

EXP106_DIR = os.path.join(ROOT, "experiments", "106-t28-kappa-window-floor-fixedabs-control")
with open(os.path.join(EXP106_DIR, "results.json")) as f:
    EXP106_RESULTS = json.load(f)

# ================================================================ T8/exp-105/exp-106's own formula chain, reused byte-for-byte
DX_M = 30.0e-9
R_BASE = 78
N0, ABSORB, EDGE, TAPER = 560, 40, 40, 40
CX0, CY0, SRC_X0 = 252, 280, 64
R_CORE0 = 30
STEPS0 = 3200
SIGMA_MAX0 = 0.5
CPL_600 = 20
COURANT_FRAC = 0.32

DENSE_PITCH = 2
FLOOR_FRAC = 0.10

NETD_BAND_K = (0.020, 0.050)
K_AIR = 0.026
DENSITY_SI, C_P_SI = 2330.0, 700.0
EMISSIVITY = 0.9
T_AMBIENT_K = 293.15

ABS_THICKNESS = 48          # cells, HELD CONSTANT across r (exp-052's own established value)
SIGMA_MAX_FIXED = 0.5       # HELD CONSTANT across r

BOX_A_MARGIN0 = 32
BOX_B_MARGIN0 = 57
REF_HH0 = 60

# item-1 cost gate (NOTES.md, disclosed): abort r=312 leg if projected total exceeds this
COST_GATE_TOTAL_S = 150 * 60


def kappa_of(r):
    return r / R_BASE


def geom(r):
    """Self-similar family, T8's own formula chain -- BYTE-FOR-BYTE reused
    from exp-105/exp-106's `geom()`. Only the fields item 1/4 actually need
    are kept; `geom_fixedabs()` below overrides R_CORE/sigma_max/tau_shell."""
    k = kappa_of(r)
    N = round(N0 * k)
    CX = round(CX0 * k)
    CY = round(CY0 * k)
    SRC_X = round(SRC_X0 * k)
    STEPS = round(STEPS0 * k)
    R_CORE = round(R_CORE0 * k)
    R_COAT = r
    sigma_max = SIGMA_MAX0 / k
    tau_shell = sigma_max * (R_COAT - R_CORE)
    behind_x_lo = CX + R_COAT + 27
    behind_x_hi = CX + R_COAT + 127
    behind_y_lo = CY - 20
    behind_y_hi = CY + 20
    box_a_hw = R_COAT + round(BOX_A_MARGIN0 * k)
    box_b_hw = R_COAT + round(BOX_B_MARGIN0 * k)
    box_a = (CX - box_a_hw, CX + box_a_hw, CY - box_a_hw, CY + box_a_hw)
    box_b = (CX - box_b_hw, CX + box_b_hw, CY - box_b_hw, CY + box_b_hw)
    ref = (CX, CY, round(REF_HH0 * k))
    return dict(r=r, k=k, N=N, CX=CX, CY=CY, SRC_X=SRC_X, STEPS=STEPS,
                R_CORE=R_CORE, R_COAT=R_COAT, sigma_max=sigma_max,
                tau_shell=tau_shell,
                behind=(behind_x_lo, behind_x_hi, behind_y_lo, behind_y_hi),
                box_a=box_a, box_b=box_b, ref=ref, family="selfsim")


def geom_fixedabs(r):
    """Fixed-absolute-thickness family -- exp-106's own `geom_fixedabs()`,
    re-derived here byte-for-byte (R4: reused formula, not hand-copied
    numbers -- cross-checked against exp-106's own committed geom below,
    Gate P0)."""
    g = dict(geom(r))
    r_core = r - ABS_THICKNESS
    sigma_max = SIGMA_MAX_FIXED
    g.update(R_CORE=r_core, sigma_max=sigma_max,
              tau_shell=sigma_max * (r - r_core), family="fixedabs")
    return g


def gate_p0():
    """Ground-truth reproduction: this file's locally re-derived
    geom_fixedabs(156)/(312) must match exp-106's own committed
    geom_156_fixedabs/geom_312_fixedabs exactly on every shared field.
    HALTS (raises) before any Sim.run() call if this fails."""
    shared_fields = ["N", "CX", "CY", "SRC_X", "STEPS", "R_CORE", "R_COAT",
                      "sigma_max", "tau_shell", "behind", "box_a", "box_b", "ref"]
    ok = {}
    for r, key in ((156, "geom_156_fixedabs"), (312, "geom_312_fixedabs")):
        g_local = geom_fixedabs(r)
        g_committed = EXP106_RESULTS[key]
        mism = []
        for f in shared_fields:
            lv, cv = g_local[f], g_committed[f]
            if isinstance(lv, (list, tuple)):
                lv, cv = list(lv), list(cv)
            if isinstance(lv, float) or isinstance(cv, float):
                same = abs(float(lv) - float(cv)) < 1e-9
            else:
                same = lv == cv
            if not same:
                mism.append((f, lv, cv))
        ok[r] = dict(pass_=(len(mism) == 0), mismatches=mism)
        print(f"  [Gate P0] r={r}  reproduces exp-106 geom_{r}_fixedabs exactly: "
              f"{ok[r]['pass_']}" + ("" if ok[r]['pass_'] else f"  MISMATCHES={mism}"))
    return ok


def _run_hollow(with_article, steps, g, capture_ez=False):
    """Same construction as exp-106's `_run()` EXCEPT no `materials.pec_disk()`
    call -- the interior (r<R_CORE) stays vacuum (HOLLOW), the exact
    construction difference T9's original test (exp-027/031) used."""
    sim = Sim(g["N"], g["N"], cells_per_lambda=CPL_600, courant_frac=COURANT_FRAC, absorb=ABSORB)
    if with_article:
        materials.graded_black_shell(sim, g["CX"], g["CY"], g["R_CORE"], g["R_COAT"],
                                      sigma_max=g["sigma_max"])
    sim.add_line_source(g["SRC_X"], angle_deg=0.0, profile="plane", edge=EDGE)
    sim.run(steps)
    cap = sc.full_capture(sim)
    sigma_e = sim.sigma_e.copy() if with_article else None
    ez = sc.phasors(cap)["ez"] if capture_ez else None
    return cap, sigma_e, ez


def floor_gate(pool_values, label, floor_frac=FLOOR_FRAC):
    arr = np.asarray(pool_values, dtype=float)
    rms = float(np.sqrt(np.mean(np.square(arr))))
    floor = floor_frac * rms
    passes = [bool(v >= floor) for v in arr]
    n_unresolved = sum(1 for p in passes if not p)
    return dict(rms=rms, floor=floor, n_unresolved=n_unresolved,
                frac_unresolved=n_unresolved / len(arr))


def floor_gate_window(ez_field, x_lo, x_hi, y_lo, y_hi, label, floor_frac=FLOOR_FRAC):
    block = np.abs(ez_field[x_lo:x_hi, y_lo:y_hi]) ** 2
    return floor_gate(block.ravel().tolist(), label, floor_frac=floor_frac)


def item1_and_4_one_r(r):
    g = geom_fixedabs(r)
    t0 = time.time()
    cap_e, _, ez_e = _run_hollow(False, g["STEPS"], g, capture_ez=True)
    t_e = time.time() - t0
    t1 = time.time()
    cap_a, sigma_e_a, ez_a = _run_hollow(True, g["STEPS"], g, capture_ez=True)
    t_a = time.time() - t1

    wa = sc.widths(cap_a, cap_e, g["box_a"], g["ref"])
    wb = sc.widths(cap_a, cap_e, g["box_b"], g["ref"])
    box_dev = abs(wa["sigma_ext"] - wb["sigma_ext"]) / abs(wa["sigma_ext"])
    _, _, radial_total = sc.radial_absorbed_power(cap_a, sigma_e_a, g["CX"], g["CY"], g["R_COAT"])
    _, _, core_total = sc.radial_absorbed_power(cap_a, sigma_e_a, g["CX"], g["CY"], g["R_CORE"])
    core_frac = core_total / radial_total if radial_total else float("nan")
    abs_ext_ratio_hollow = wa["sigma_abs"] / wa["sigma_ext"]

    pec_key = "ledger_r156" if r == 156 else "ledger_r312"
    abs_ext_ratio_pec = EXP106_RESULTS[pec_key]["fixedabs"]["abs_ext_ratio"]
    delta_abs_ext_ratio = abs_ext_ratio_hollow - abs_ext_ratio_pec

    fg_article = floor_gate_window(ez_a, *g["behind"], f"r={r} window (hollow article, numerator)")

    row = dict(r=r, sigma_abs=wa["sigma_abs"], sigma_ext=wa["sigma_ext"],
               abs_ext_ratio_hollow=abs_ext_ratio_hollow,
               abs_ext_ratio_pec_cored_exp106=abs_ext_ratio_pec,
               delta_abs_ext_ratio=delta_abs_ext_ratio,
               box_dev=box_dev, core_frac=core_frac, core_power=core_total,
               radial_total=radial_total,
               item1_pass=bool(abs(delta_abs_ext_ratio) <= 2e-4) and bool(box_dev <= 0.12),
               item1_confirms_band=bool(abs(delta_abs_ext_ratio) <= 2e-5),
               floor_gate_article_numerator=fg_article,
               wall_empty_s=t_e, wall_article_s=t_a, wall_total_s=t_e + t_a)
    print(f"[item1/4] r={r}  delta_abs_ext_ratio={delta_abs_ext_ratio:.3e}  "
          f"box_dev={box_dev:.4f}  core_frac={core_frac:.3e}  "
          f"floor_frac_unresolved(article)={fg_article['frac_unresolved']:.4f}  "
          f"wall={t_e + t_a:.1f}s")
    return row


def item3_thermal_row():
    SIGMA_EXT_78 = 240.0073740162445
    P_ABS_78 = 1.7409069740390205e-12
    RATIO_ABS_EXT_78 = 0.51
    width_m_78 = SIGMA_EXT_78 * DX_M
    i_incident = (P_ABS_78 / RATIO_ABS_EXT_78) / (width_m_78 ** 2 * 1e4)

    rows = {}
    for r, ledger_key in ((156, "ledger_r156"), (312, "ledger_r312")):
        for family in ("selfsim", "fixedabs"):
            led = EXP106_RESULTS[ledger_key][family]
            sigma_ext_real = led["sigma_ext"]
            abs_ext_ratio_real = led["abs_ext_ratio"]
            width_m = sigma_ext_real * DX_M
            p_abs_w = i_incident * (width_m ** 2) * 1e4 * abs_ext_ratio_real
            r_out_m = r * DX_M
            regime = ts.mixed_length_scale_regime(
                p_abs_w=p_abs_w, l_geometric_m=r_out_m, k_air=K_AIR,
                density_kg_m3=DENSITY_SI, c_p_j_kgk=C_P_SI, emissivity=EMISSIVITY,
                t_ambient_k=T_AMBIENT_K, length_provenance="bench_construction")
            dt_ss = regime["dt_ss_full_K"]
            margin = NETD_BAND_K[0] / dt_ss
            disp = ts.netd_disposition(dt_ss, NETD_BAND_K)
            rows[f"{family}_{r}"] = dict(
                family=family, r=r, sigma_ext=sigma_ext_real,
                abs_ext_ratio=abs_ext_ratio_real, i_incident=i_incident,
                p_abs_w=p_abs_w, dt_ss_K=dt_ss, margin=margin,
                classification=disp["classification"])
            print(f"[item3] {family:9s} r={r:4d}  sigma_ext={sigma_ext_real:10.4f}  "
                  f"dt_ss_K={dt_ss:.6e}  margin={margin:9.3f}x  class={disp['classification']}")
    return rows, i_incident


def main():
    t_start = time.time()
    print("=" * 78)
    print("exp-107 Phase 4 -- Gate P0 (ground-truth reproduction)")
    print("=" * 78)
    gate_p0_result = gate_p0()
    if not all(v["pass_"] for v in gate_p0_result.values()):
        raise SystemExit("Gate P0 FAILED -- HALT before any Sim.run() call (see mismatches above)")

    print("\n" + "=" * 78)
    print("Item 3 -- real, non-placeholder P5 thermal row (zero marginal FDTD)")
    print("=" * 78)
    item3_rows, i_incident = item3_thermal_row()

    print("\n" + "=" * 78)
    print("Item 1/4 -- hollow-vs-PEC-cored radial_absorbed_power delta + numerator floor gate")
    print("=" * 78)
    n_fdtd_calls = 0
    item1_rows = {}

    # r=156 first (cheap pilot)
    row156 = item1_and_4_one_r(156)
    item1_rows[156] = row156
    n_fdtd_calls += 2
    # Cost projection: r=312 empty+article historically run several x longer than r=156;
    # use exp-106's own measured r=156-vs-r=312 wall-time ratio as the scaling factor.
    r156_ref_s = EXP106_RESULTS["wall_156_primary_s"] / 3.0   # ~1 call at r=156, exp-106's own primary leg
    r312_ref_s = EXP106_RESULTS["wall_312_article_s"] / 2.0 + EXP106_RESULTS["wall_312_empty_pilot_s"]
    scale_factor = r312_ref_s / max(r156_ref_s, 1e-9)
    projected_r312_s = row156["wall_total_s"] * scale_factor
    projected_total_s = row156["wall_total_s"] + projected_r312_s
    print(f"  [cost gate] r=156 actual wall={row156['wall_total_s']:.1f}s  "
          f"projected r=312 wall={projected_r312_s:.1f}s (scale={scale_factor:.2f}x, "
          f"exp-106 own r156:r312 wall-time ratio)  "
          f"projected total={projected_total_s:.1f}s (gate={COST_GATE_TOTAL_S}s)")

    r312_committed = projected_total_s <= COST_GATE_TOTAL_S
    if r312_committed:
        row312 = item1_and_4_one_r(312)
        item1_rows[312] = row312
        n_fdtd_calls += 2
    else:
        print(f"  [cost gate] ABORTING r=312 leg -- projected {projected_total_s:.1f}s exceeds "
              f"{COST_GATE_TOTAL_S}s gate. Reporting r=156-only (disclosed reduction).")

    total_wall = time.time() - t_start
    print(f"\nTotal wall time: {total_wall:.1f}s ({total_wall/60.0:.2f} min)")
    print(f"Real FDTD calls: {n_fdtd_calls}")

    results = dict(
        experiment="exp-107-t28-delta-scene-r5-census-decision",
        panel_iteration=84,
        tier0_disposition="FORMALLY RETIRED (text-only, see NOTES.md -- zero FDTD)",
        n_fdtd_calls=n_fdtd_calls,
        total_wall_s=total_wall,
        r312_committed=r312_committed,
        gate_p0={r: dict(pass_=v["pass_"]) for r, v in gate_p0_result.items()},
        item1_rows=item1_rows,
        item3_rows=item3_rows,
        item3_i_incident=i_incident,
    )
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(results, f, indent=2, default=str)
    print("\nWrote results.json")
    return results


if __name__ == "__main__":
    main()
