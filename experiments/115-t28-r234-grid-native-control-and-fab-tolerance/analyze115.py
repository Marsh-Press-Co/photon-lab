"""exp-115 Phase-4 analysis (Phase-3 synthesis) -- Panel Iteration 92.

Runner: bench panel shift (T5820) -- Director Clyde, live session.

Reads `data/readings.json` (written one reading at a time by
`chunk_runner115.py --run-cg`), computes every scored and not-scored
quantity this cycle pre-registered, and writes `results.json` in this
experiment's own directory. `lab/ARTIFACTS.md` reserves `artifacts/` for
scene bundles, so this cycle's data lives under `data/` and its verdicts
in `results.json`, exactly as exp-114 did.

Zero FDTD: nothing here builds a Sim or calls Sim.run(). Every number is
either read from `data/readings.json` or recomputed from committed JSON
and committed source.

What it computes:
  M1 G_short = per_step(S234)/per_step(S156)
  M2 G_sustained = MEAN of the two pairwise G under ABBA (MF-6a/6b);
     BOTH pairwise values persisted
  MF-6(c) same-grid drift as a RATE PER UNIT ELAPSED TIME (ABBA makes the
     two same-grid lags unequal, a+2b vs b, so a bare difference is not
     comparable between grids)
  M3 d_dur, mechanism-neutral (MF-9)
  M4 d_rep, drift+noise under ABBA (MF-6d), MARGINAL split at 0.03 and
     R_DEG/2 so the label carries its own consequence (MF-9)
  M5 PRIMARY, through exponent_B = ln(1.5 G)/ln(1.5) (MF-5), with
     MF-7(a)'s two-point protocol-mismatch interval; BOUNDED-REPLICATION
     rather than a movable verdict whenever the interval spans a band edge
  M6 T = G/G_E, directional-only unless M3 reads G-DURATION-INVARIANT
     (MF-9 inverts the Phase-1 1-of-4-state rule)
  M7 two-sided labels (MF-9/RT-14) plus the explicitly-underpowered model
     comparison
  M8 the persisted, NOT-scored sensitivities (Tier-1 item 2 + MF-8/OV-1)
  M9 the fabrication-tolerance ANALYTIC SIDECAR (Tier-1 item 5), corrected
     per MF-1..MF-4/MF-11/MF-13/MF-15, with HALT semantics: any failed
     reproduction check reports NOT-REPRODUCED and WITHHOLDS the bound

CERTIFIED-RESOLUTION WORDING (MF-14, and the phrase this cycle's own
`caveat_lint_config.json` entry gates on at every site the bound is
stated). The fabrication-tolerance bound's tight per-bin figure is
CERTIFIED AT MARGIN=32 ONLY -- the other five margins in exp-108's
MARGINS=(24,32,40,48,57,65) are certified by one boolean against
ITEM_I_CONFIRM_REL = 0.05, a DECISION BAR 330x looser, and only the
margin-32 array is persisted. Per-bin evidence exists at cpl=20 only and
aggregate evidence at cpl=25 only, so CHANNEL AND RESOLUTION ARE FULLY
CONFOUNDED; r=234 contributes aggregate channels only; and the
instrument is a near-to-mid-field box ledger, not a far-field pattern.
The per-bin half of any "better than 1.6e-04" reading is WITHDRAWN.

R23 First Addendum: `DISCLAIMER_115` is asserted present in BOTH
`predictions_text` and `result_text` here, and both builder functions
carry their own internal assert in `run115.py` -- two committed,
re-invocable call sites in this same cycle (`run115.py --selftest` runs
the result-side one with synthetic operands at Phase 3, before any bench
data exists).

T18 evidentiary tier: the realizability tier this cycle's sidecar cites
is inherited from exp-061's WebSearch-snippet synthesis, not
primary-source-verified; no new literature search is attempted.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "112-t28-cpl25-floor-spot-check"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "113-t28-r312-cpl25-plus168-bin"))
sys.path.insert(0, os.path.join(ROOT, "experiments", "114-t28-kappa-exponent-r234-calibration"))

import run as R110               # noqa: E402
import run112 as R112            # noqa: E402
import run113 as R113            # noqa: E402
import run114 as R114            # noqa: E402
import run115 as R               # noqa: E402

# R29: executed identity assertions.
assert len({id(R110), id(R112), id(R113), id(R114), id(R)}) == 5, (
    "R29: run110/run112/run113/run114/run115 must be five distinct module objects")
assert os.path.basename(os.path.dirname(os.path.abspath(R.__file__))) == os.path.basename(HERE), (
    "R29: run115 (R) must be THIS directory's own module")

READINGS_PATH = os.path.join(R.DATA_DIR, "readings.json")
RESULTS_PATH = os.path.join(HERE, "results.json")


def _mean(vals):
    vals = [v for v in vals if v is not None]
    return sum(vals) / float(len(vals)) if vals else None


def drift_rate(read_a, read_b):
    """MF-6(c). Same-grid drift expressed as a RATE PER UNIT ELAPSED
    TIME, using each reading's MIDPOINT as its sampling time. Under ABBA
    the two same-grid lags are unequal (a+2b on one grid, b on the
    other), so a bare per-step difference between the two same-grid
    readings is NOT comparable across grids; a rate is."""
    if read_a is None or read_b is None:
        return None
    lag_s = read_b["mid_epoch_s"] - read_a["mid_epoch_s"]
    d_per_step = read_b["per_step_s"] - read_a["per_step_s"]
    if lag_s <= 0:
        return None
    return dict(lag_s=lag_s,
                delta_per_step_s=d_per_step,
                rate_s_per_step_per_s=d_per_step / lag_s,
                relative_rate_per_s=(d_per_step / read_a["per_step_s"]) / lag_s,
                relative_rate_per_hour=3600.0 * (d_per_step / read_a["per_step_s"]) / lag_s)


def analyze(doc):
    rd = doc["readings"]
    repeat_skipped = bool(doc.get("repeat_skipped"))
    sustained_steps = int(doc.get("sustained_steps_used", R.SUSTAINED_CONTROL_STEPS))

    s156, s234 = rd["S156"], rd["S234"]
    u156, u234 = rd["U156"], rd["U234"]
    u234b, u156b = rd.get("U234b"), rd.get("U156b")

    # ---- M1 / M2 ----------------------------------------------------------
    g_short = s234["per_step_s"] / s156["per_step_s"]
    g_pair1 = u234["per_step_s"] / u156["per_step_s"]
    g_pair2 = (u234b["per_step_s"] / u156b["per_step_s"]) if (u234b and u156b) else None
    # MF-6(a): score M2/M5 on the MEAN of the two pairwise G values -- under
    # ABBA that mean is unbiased to first order in a linear drift without
    # needing to ESTIMATE the drift, which is the more robust construction.
    g_sustained = _mean([g_pair1, g_pair2])

    # ---- MF-6(c) drift rates ---------------------------------------------
    drift = dict(r156=drift_rate(u156, u156b), r234=drift_rate(u234, u234b),
                 note=("Rates, not differences: ABBA gives the r=156 pair a lag of a+2b and "
                       "the r=234 pair a lag of b (~2.4x apart), so only a rate per unit "
                       "elapsed time is comparable between grids. This is the equal-lag "
                       "same-grid comparison ABAB would have provided and ABBA does not; "
                       "reporting it as a rate is the substitute (MF-6c)."))

    # ---- M3 / M4 and the MF-9 booleans -----------------------------------
    m3 = R.classify_m3(g_short, g_sustained)
    m4 = R.classify_m4(g_pair1, g_pair2, repeat_skipped=repeat_skipped)
    d_rep = m4["d_rep"]
    m3_scored = bool((not repeat_skipped) and d_rep is not None
                     and d_rep <= R.M3_INVARIANT_BAR)
    m7_underpowered = bool(repeat_skipped or d_rep is None or d_rep > R.M7_POWER_BAR)

    # ---- M5 + MF-7(a) protocol-mismatch interval --------------------------
    m5 = R.classify_m5(g_sustained)
    p156_sust = _mean([u156["per_step_s"], u156b["per_step_s"] if u156b else None])
    p234_sust = _mean([u234["per_step_s"], u234b["per_step_s"] if u234b else None])
    interval = R.protocol_mismatch_interval(
        s156["per_step_s"], p156_sust, s234["per_step_s"], p234_sust,
        n_short=R.SHORT_CONTROL_STEPS, n_sustained=sustained_steps)
    interval["note"] = (
        "Two-point p(n) = p_inf + C_g/n per grid, exactly determined by the S and U readings "
        "already scheduled -- it BOUNDS, it does not fit (R7). The sustained per-step rate "
        "used on each grid is the MEAN over that grid's sustained readings; a mean of ratios "
        "is not a ratio of means, but this is a bound, and the endpoint spread is what the "
        "caveat consumes. Endpoints: the measured burst protocol, the production protocol "
        "(8000/12000 steps/scene -- exp-114's own numerator and denominator step counts), and "
        "the amortized limit n -> inf.")
    m5_protocol_caveat = bool(interval["m5_protocol_caveat"])
    m5["m5_protocol_caveat"] = m5_protocol_caveat
    m5["reported_verdict"] = (R.M5_BOUNDED_REPLICATION if m5_protocol_caveat
                              else m5["verdict"])
    m5["may_move_logbook_verdict"] = bool(not m5_protocol_caveat and m3_scored)
    m5["power_limit"] = (
        "Pure N^2 (cell-count) scaling gives G = 2.25 exactly, i.e. k = 3.0 EXACTLY -- the "
        "pre-R28 hardcoded exponent -- with rel_dev = %.4f, INSIDE the CONFIRM band. A CONFIRM "
        "therefore does NOT distinguish k = %.4f from k = 3.0."
        % (abs(R.KAPPA_RATIO * R.G_N2 - R.REFERENCE_RATIO) / R.REFERENCE_RATIO,
           R.KAPPA_COST_EXPONENT))
    m5["preregistered_protocol_models"] = dict(
        drift_degradation_G=R.PROTOCOL_MODEL_DRIFT_G,
        warmup_amortization_G_scene_matched=R.PROTOCOL_MODEL_WARMUP_G_SCENE_MATCHED,
        warmup_amortization_G_blend=R.PROTOCOL_MODEL_WARMUP_G_BLEND,
        confirm_ceiling_G=R.G_CONFIRM_HI,
        note=("Pre-registered at Phase 3, before any bench reading. The two models sit on "
              "OPPOSITE sides of the CONFIRM ceiling; their inputs include exp-114's three "
              "r=234 chunk times, which survive only as quotations and are NOT independently "
              "re-derivable -- directional, cited."))

    # ---- M6 / M7 ----------------------------------------------------------
    m6 = R.classify_m6(g_sustained, m3["verdict"])
    m7 = R.classify_m7(g_sustained, m7_underpowered)

    # ---- M8 sensitivities, none scored ------------------------------------
    sens = R.sensitivities_do_not_score(g_sustained)

    # ---- M9 analytic sidecar, with HALT semantics -------------------------
    sidecar = R.sidecar_m9()

    readings_summary = {k: dict(r=v["r"], control_steps=v["control_steps"],
                                total_wall_s=v["total_wall_s"], per_step_s=v["per_step_s"],
                                start_utc=v["start_utc"], end_utc=v["end_utc"])
                        for k, v in rd.items()}

    return dict(
        cycle="exp-115", iteration=92,
        runner="bench panel shift (T5820) -- Director Clyde, live session",
        readings=rd, readings_summary=readings_summary,
        identity_gate=doc.get("identity_gate"),
        machine_state=doc.get("machine_state"),
        machine_state_end=doc.get("machine_state_end"),
        gates=doc.get("gates"),
        repeat_skipped=repeat_skipped, repeat_skip_reason=doc.get("repeat_skip_reason"),
        sustained_steps_used=sustained_steps,
        sustained_stepped_down=bool(doc.get("sustained_stepped_down")),
        n_sim_run_calls=doc.get("n_sim_run_calls"),
        n_sim_run_calls_expected=doc.get("n_sim_run_calls_expected"),
        total_wall_s=doc.get("total_wall_s"),
        G_short=g_short, G_pair1=g_pair1, G_pair2=g_pair2, G_sustained=g_sustained,
        G_E=R.G_E, G_ref=R.G_REF, R_DEG=R.R_DEG,
        drift=drift,
        m3=m3, m4=m4, m5=m5, m6=m6, m7=m7,
        protocol_mismatch_interval=interval,
        m3_scored=m3_scored, m5_protocol_caveat=m5_protocol_caveat,
        m6_directional_only=m6["m6_directional_only"], m7_underpowered=m7_underpowered,
        sensitivities=sens, decline_8=R.DECLINE_8,
        sidecar_m9=sidecar)


def main():
    geom = R.verify_geometry_identity()
    print("verify_geometry_identity: pass_=%s" % geom["pass_"])
    if not geom["pass_"]:
        print(json.dumps(geom, indent=2))
        raise SystemExit("HALT: geom_fixedabs_cpl does not reduce to R110.geom_fixedabs at cpl==20")

    if not os.path.exists(READINGS_PATH):
        print("\nNo bench readings on file yet.")
        print("  expected: %s" % READINGS_PATH)
        print("  Phase 4 order (bench, exclusive use):")
        print("    1. python run115.py --verify-geometry")
        print("    2. python chunk_runner115.py --identity-gate")
        print("    3. .venv311/bin/python lab/validation/run_all.py --only 12346789   "
              "(commit the console record -- MF-12)")
        print("    4. python chunk_runner115.py --machine-state")
        print("    5. python chunk_runner115.py --run-cg --post-ticker")
        print("    6. python analyze115.py")
        print("\nNothing analysed, nothing written. Exiting cleanly (Phase-3 verification "
              "path -- this module is committed ready-to-run, not executed against real data "
              "this phase).")
        raise SystemExit(0)

    with open(READINGS_PATH) as f:
        doc = json.load(f)

    missing = [k for k in R.PRIMARY_READINGS if k not in doc.get("readings", {})]
    if missing:
        print("\nIncomplete readings on file: missing %s. Re-run "
              "`chunk_runner115.py --run-cg`; nothing analysed." % ", ".join(missing))
        raise SystemExit(0)

    row = analyze(doc)

    predictions_text = R.build_predictions_text()
    assert R.DISCLAIMER_115 in predictions_text, "R23 First Addendum: predictions-side assert"

    result_text = R.build_result_text(
        readings_summary=row["readings_summary"],
        n_sim_run_calls=row["n_sim_run_calls"] or 0,
        total_wall_s=row["total_wall_s"] or 0.0,
        geom_ok=geom["pass_"],
        identity_gate_ok=bool((row["identity_gate"] or {}).get("pass_")),
        m1=row["G_short"], m2=row["G_sustained"], m3=row["m3"], m4=row["m4"],
        m5=row["m5"], m6=row["m6"], m7=row["m7"],
        protocol_interval=row["protocol_mismatch_interval"], drift=row["drift"],
        sidecar=row["sidecar_m9"], repeat_skipped=row["repeat_skipped"],
        sustained_steps_used=row["sustained_steps_used"],
        machine_state=dict(hostname=(row["machine_state"] or {}).get("hostname"),
                           numpy=(row["machine_state"] or {}).get("numpy_version"),
                           python=(row["machine_state"] or {}).get("python_version"),
                           loadavg_start=(row["machine_state"] or {}).get("loadavg"),
                           loadavg_end=(row["machine_state_end"] or {}).get("loadavg")))
    assert R.DISCLAIMER_115 in result_text, "R23 First Addendum: result-side assert"

    out = dict(row, geom_identity=geom,
               predictions_text=predictions_text, result_text=result_text)
    with open(RESULTS_PATH, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(result_text)
    print("\nWritten: %s" % RESULTS_PATH)


if __name__ == "__main__":
    main()
