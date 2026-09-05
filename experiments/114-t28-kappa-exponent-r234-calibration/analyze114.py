"""exp-114 Phase 4 analysis (Phase-3 synthesis, Red Team's Phase-2 audit
Fix 3): loads chunk_runner114.py's own r=234/cpl=25 captures (empty/
hollow/peccored) once real, computes the energy ledger (sigma_scat/
sigma_abs/sigma_ext/sigma_ext_cross, via lab.sections.widths() --
THERMODYNAMICS' Phase-2 critique), and scores the kappa_exponent
generalization check (refit_kappa_exponent()/classify_kappa_exponent_
check(), run114.py -- this cycle's own stated falsifiable heart, which
Red Team's audit found defined but never invoked by any committed
script through Phase 2).

This leg does NOT invoke the angular-pattern/named-bin classification
machinery (declined by scope, phase1_proposal.md Sec 3/Idealization 3) --
no sigma_scat_per_bin reproduction check is computed, and the
"reproduction/self-consistency precondition" in build_predictions_text()
is reported N/A for that reason, stated explicitly in result_text, not
silently omitted.

Mirrors analyze113.py's own structure (load -> widths() -> ledger ->
result_text -> results.json, with the same R23 DISCLAIMER-assert
discipline and the same "gate-refused, zero real data" branch), narrowed
to what this cycle's own scope actually needs.

Not executed at Phase 3 synthesis (no real r=234 data exists yet) --
committed so Phase 4 can run it unchanged against real captures, exactly
matching this family's own Phase-1/Phase-4 discipline.
"""
import json
import os
import pickle
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "113-t28-r312-cpl25-plus168-bin"))

import run as R110               # noqa: E402
import run112 as R112            # noqa: E402
import run113 as R113            # noqa: E402
import run114 as R               # noqa: E402
import chunk_runner114 as CR     # noqa: E402
from lab import sections as sc   # noqa: E402

# R29 (LOGBOOK.md, founding instance exp-112): executed identity assertions.
assert R is not R110 and R is not R112 and R is not R113, (
    "R29: run114 (R) must be distinct from run110/run112/run113")
EXP_DIR_NAME = os.path.basename(HERE)
assert os.path.basename(os.path.dirname(CR.__file__)) == EXP_DIR_NAME, (
    "R29 (2nd-instance shape, guarded pre-emptively): chunk_runner114 (CR) must be "
    "THIS directory's own module")


def load(r, cpl, which):
    path = os.path.join(CR.SCRATCH, f"r{r}_cpl{cpl}_{which}_done.pkl")
    with open(path, "rb") as f:
        return pickle.load(f)


def have(r, cpl, which):
    return os.path.exists(os.path.join(CR.SCRATCH, f"r{r}_cpl{cpl}_{which}_done.pkl"))


def analyze_r234_cpl25():
    de = load(234, R.CPL_TARGET, "empty")
    dh = load(234, R.CPL_TARGET, "hollow")
    dp = load(234, R.CPL_TARGET, "peccored")
    g = de["g"]
    cap_e, cap_h, cap_p = de["cap"], dh["cap"], dp["cap"]
    box_a, ref = g["box_a"], g["ref"]

    # THERMODYNAMICS' Phase-2 finding / Red Team's Fix 3(a): persist the
    # energy ledger -- real, non-zero absorbed power WILL be produced
    # (graded_black_shell, tau_shell=24, genuinely absorptive), and this is
    # computable at zero marginal FDTD cost from the captures alone.
    w_p = sc.widths(cap_p, cap_e, box_a, ref)
    w_h = sc.widths(cap_h, cap_e, box_a, ref)
    energy_ledger = dict(
        peccored=dict(sigma_scat=w_p["sigma_scat"], sigma_abs=w_p["sigma_abs"],
                      sigma_ext=w_p["sigma_ext"], sigma_ext_cross=w_p["sigma_ext_cross"]),
        hollow=dict(sigma_scat=w_h["sigma_scat"], sigma_abs=w_h["sigma_abs"],
                    sigma_ext=w_h["sigma_ext"], sigma_ext_cross=w_h["sigma_ext_cross"]))

    total_wall_s_by_scene = dict(
        empty=CR.total_wall_time(234, R.CPL_TARGET, "empty"),
        hollow=CR.total_wall_time(234, R.CPL_TARGET, "hollow"),
        peccored=CR.total_wall_time(234, R.CPL_TARGET, "peccored"))
    t234_cpl25 = sum(total_wall_s_by_scene.values())

    # Fix 3(b): this cycle's own stated falsifiable heart -- defined in
    # run114.py through Phase 2 but never invoked by any committed script.
    exponent_234 = R.refit_kappa_exponent(R.HISTORICAL_R156_CPL25_TOTAL_S, t234_cpl25)
    kappa_exponent_result = R.classify_kappa_exponent_check(exponent_234)

    return dict(r=234, cpl=R.CPL_TARGET, geom=g,
                energy_ledger=energy_ledger,
                total_wall_s_by_scene=total_wall_s_by_scene,
                t234_cpl25=t234_cpl25,
                kappa_exponent_result=kappa_exponent_result)


if __name__ == "__main__":
    geom_check = R.verify_geometry_identity()
    print(f"verify_geometry_identity: pass_={geom_check['pass_']}")
    if not geom_check["pass_"]:
        print(json.dumps(geom_check, indent=2))
        raise SystemExit("HALT: geom_fixedabs_cpl does not reduce to R.geom_fixedabs at cpl==20")

    if not (have(234, R.CPL_TARGET, "empty") and have(234, R.CPL_TARGET, "hollow")
            and have(234, R.CPL_TARGET, "peccored")):
        control_path = os.path.join(CR.SCRATCH, "r31_control.json")
        gate_path = os.path.join(CR.SCRATCH, f"r234_cpl{R.CPL_TARGET}_costgate.json")
        if os.path.exists(control_path) and os.path.exists(gate_path):
            # R23/R31 (exp-113's own precedent): the R31-gated cost decision
            # is itself a genuine, committed-worthy result -- persist the
            # refusal and the control readings, rather than exit silently.
            with open(control_path) as f:
                control = json.load(f)
            with open(gate_path) as f:
                gate = json.load(f)
            predictions_text = R.build_predictions_text(control=control, gate=gate)
            assert R.DISCLAIMER in predictions_text
            n_control_calls = (control["short"]["n_scenes"] + control["sustained"]["n_scenes"])
            control_wall_s = (control["short"]["control_wall_s"]
                               + control["sustained"]["control_wall_s"])
            result_text = R.build_result_text(
                n_fdtd_calls=n_control_calls, total_wall_s=control_wall_s,
                geom_ok=geom_check["pass_"], repro_ok=None,
                cost_gate_result=gate,
                wall_time_source=(f"{n_control_calls} real FDTD calls this cycle, ALL at "
                                   f"r=156/cpl=25 (R31 same-session control, short+sustained "
                                   f"3-scene blends) -- ZERO real r=234 scoring Sim.run() calls "
                                   f"were made; the gate refused upstream of all of them."))
            assert R.DISCLAIMER in result_text
            out = dict(r=234, cpl=R.CPL_TARGET, geom_identity=geom_check,
                       r31_control=control, cost_gate=gate,
                       n_fdtd_calls=n_control_calls, total_wall_s_all_scenes=control_wall_s,
                       kappa_exponent_reached=False, gate_refused=True,
                       predictions_text=predictions_text, result_text=result_text)
            out_path = os.path.join(HERE, "results.json")
            with open(out_path, "w") as f:
                json.dump(out, f, indent=2, default=str)
            print(result_text)
            print(f"\nWritten: {out_path}")
            raise SystemExit(0)
        print("r=234/cpl=25 captures not yet complete; run chunk_runner114.py for "
              "empty/hollow/peccored at r=234, cpl=25 first.")
        raise SystemExit(0)

    row = analyze_r234_cpl25()

    control_path = os.path.join(CR.SCRATCH, "r31_control.json")
    with open(control_path) as f:
        control = json.load(f)
    gate_path = os.path.join(CR.SCRATCH, f"r234_cpl{R.CPL_TARGET}_costgate.json")
    with open(gate_path) as f:
        gate = json.load(f)

    print(json.dumps({k: v for k, v in row.items() if k != "geom"}, indent=2, default=str))

    predictions_text = R.build_predictions_text(control=control, gate=gate)
    assert R.DISCLAIMER in predictions_text

    n_fdtd_calls = 3
    result_text = R.build_result_text(
        n_fdtd_calls=n_fdtd_calls, total_wall_s=row["t234_cpl25"],
        geom_ok=geom_check["pass_"], repro_ok=None, cost_gate_result=gate,
        kappa_exponent_result=row["kappa_exponent_result"],
        wall_time_source="exp-114's own genuinely new r=234/cpl=25 spend, "
                          "R31-gated by a same-session control. Reproduction/"
                          "self-consistency precondition: N/A -- this leg does "
                          "not invoke the angular-pattern instrument (declined "
                          "by scope, Idealization 3).")
    assert R.DISCLAIMER in result_text

    out = dict(row, n_fdtd_calls=n_fdtd_calls, total_wall_s_all_scenes=row["t234_cpl25"],
               geom_identity=geom_check, r31_control=control, cost_gate=gate,
               kappa_exponent_reached=True, gate_refused=False,
               predictions_text=predictions_text, result_text=result_text)
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nWritten: {out_path}")
