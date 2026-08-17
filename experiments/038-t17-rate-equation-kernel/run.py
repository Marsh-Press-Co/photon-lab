"""
exp-038 — The T17 Rate-Equation Kernel. Panel Iteration 15.
============================================================
Runs the pre-registered Test A (at-rest reach time) and Test B (repeated
beam-transit pulses) sweeps against `lab.kinetics`, per
NOTES.md's Phase-3 synthesis. Zero FDTD calls -- this experiment's own
"run" is a 0D kinetics sweep, not a Maxwell-solver scene. Produces
results.json with every predicted-vs-measured pair.

Run: python3 experiments/038-t17-rate-equation-kernel/run.py
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np

from lab import kinetics as kin

HERE = os.path.dirname(os.path.abspath(__file__))

HOSTS = [("A", 1e9), ("B", 1e6), ("C", 1e3), ("D", 1e1), ("E", 1e0)]
RATIOS = [1e-9, 1e-5, 1e-3, 1e-1, 1.0]
T_PULSE = 0.1          # 100 ms, T3-provisional anchor
A_VALUES = [10.0, 1e3, 1e6]
N_PULSES = 5
T3_WINDOW = (0.010, 1.0)   # 10ms-1s, provisional (unsourced), per house discipline

TIER = {
    ("A",): "PUBLISHED", ("B",): "PUBLISHED",
    ("C",): "PLAUSIBLE", ("D",): "PLAUSIBLE",
    ("E",): "UNOBTANIUM-WITH-PARAMETERS",
}


def realizability_tier(host, r):
    if host == "E":
        return "UNOBTANIUM-WITH-PARAMETERS"
    if r >= 1.0:
        return "UNOBTANIUM-WITH-PARAMETERS"
    if r <= 1e-3:
        return "PUBLISHED" if host in ("A", "B") else "PLAUSIBLE"
    return "PLAUSIBLE"


def test_a():
    """At-rest reach time: n0=0, constant I=I_ambient, t99 to 99% of n_ss.
    Reports BOTH P-MAT-4's original per-host approximation (t99 ~=
    4.605*tau_r, using the host's own k_r-only lifetime as a stand-in for
    tau) and the exact tau=1/(k_f+k_r) formula -- these coincide only in
    the r<<1 limit; at r=0.1 they differ by ~10%, and at r=1 by a full
    factor of 2 (tau_exact = tau_r/2 there). Neither the Phase-1 proposal
    nor any of the six Phase-2 reviewing seats flagged this distinction;
    caught during this Phase-4 run. Both numbers are reported, not just
    the exact one, so the discrepancy is visible rather than silently
    corrected out of the record."""
    rows = []
    for host, k_r in HOSTS:
        for r in RATIOS:
            k_f = r * k_r
            tau_r = 1.0 / k_r                    # host lifetime alone (P-MAT-4's stand-in)
            tau_exact = float(kin.tau_exact(k_f, k_r))   # true relaxation time
            t99_naive = 4.605170185988091 * tau_r
            t99_exact = float(kin.t99(k_f, k_r))
            n_ss = float(kin.n_eq_exact(k_f, k_r))
            # cross-check: integrate to t99_exact, should land at 0.99*n_ss
            n_at_t99 = kin.integrate_two_state(k_f, k_r, (0.0, t99_exact), n0=0.0, method="exp")
            rows.append({
                "host": host, "r": r, "k_f": k_f, "k_r": k_r,
                "n_ss": n_ss, "tier": realizability_tier(host, r),
                "tau_r_s": tau_r, "tau_exact_s": tau_exact,
                "t99_naive_pred_s": t99_naive, "t99_exact_s": t99_exact,
                "naive_vs_exact_rel_discrepancy": abs(t99_naive - t99_exact) / t99_exact,
                "n_at_t99_over_n_ss": n_at_t99 / n_ss if n_ss > 0 else None,
                "in_t3_window": T3_WINDOW[0] <= t99_exact <= T3_WINDOW[1],
            })
    return rows


def test_b():
    """Repeated beam-transit pulses. Reports periodic/first-pulse peak-n
    ratio at both Delta_t_sweep settings (5*tau, 0.5*tau, per-point tau =
    1/(k_f_ambient+k_r), NOT the host-only tau_r) x 3 enhancement factors A.
    """
    rows = []
    for host, k_r in HOSTS:
        for r in RATIOS:
            k_f = r * k_r
            tau = float(kin.tau_exact(k_f, k_r))
            for dt_name, dt_sweep in (("5tau", 5.0 * tau), ("0.5tau", 0.5 * tau)):
                for A in A_VALUES:
                    segs = kin.pulse_train_segments(k_f, k_r, A, T_PULSE, dt_sweep, N_PULSES)
                    _, t_arr, n_arr = kin.integrate_segments(segs, n0=0.0, method="exp", record=True)
                    # segment boundaries alternate: ambient, pulse-end, ambient, pulse-end, ...
                    # pulse-end (peak) indices are 2, 4, 6, 8, 10 (1-indexed boundary list
                    # starting at t=0); with 11 segments total there are 5 pulse-end points.
                    pulse_end_idx = [2 * k for k in range(1, N_PULSES + 1)]
                    peaks = n_arr[pulse_end_idx]
                    first_peak = float(peaks[0])
                    periodic_peak = float(peaks[-1])
                    ratio = periodic_peak / first_peak if first_peak > 0 else None
                    # RK4 cross-check on this exact trajectory (gate 4's own grid,
                    # reused here to attach a convergence figure to each science row)
                    _, _, n_rk4 = kin.integrate_segments(segs, n0=0.0, method="rk4", record=True)
                    rk4_rel_diff = float(np.sqrt(np.mean((n_arr - n_rk4) ** 2))) / \
                        max(float(np.sqrt(np.mean(n_arr ** 2))), 1e-300)
                    rows.append({
                        "host": host, "r": r, "A": A, "dt_sweep": dt_name,
                        "tau_s": tau, "first_pulse_peak_n": first_peak,
                        "periodic_pulse_peak_n": periodic_peak,
                        "periodic_over_first_ratio": ratio,
                        "converged_by_pulse_3": bool(
                            abs(peaks[2] - periodic_peak) / periodic_peak < 0.01
                        ) if periodic_peak > 0 else None,
                        "rk4_cross_check_rms_rel_diff": rk4_rel_diff,
                    })
    return rows


def main():
    t0 = time.time()
    rows_a = test_a()
    rows_b = test_b()
    elapsed = time.time() - t0

    # --- pre-registered prediction checks (against exp-038/NOTES.md, corrected) ---
    checks = []

    # P-MAT-4: only Host D lands inside/near T3's window; A-C sit below, E above.
    by_host_in_window = {}
    for row in rows_a:
        by_host_in_window.setdefault(row["host"], []).append(row["in_t3_window"])
    p_mat_4 = {h: any(v) for h, v in by_host_in_window.items()}
    checks.append({
        "id": "P-MAT-4", "claim": "only Host D lands inside/near T3's 10ms-1s window",
        "measured_by_host": p_mat_4,
        "confirmed": (not p_mat_4["A"] and not p_mat_4["B"] and not p_mat_4["C"]
                      and p_mat_4["D"] and not p_mat_4["E"]),
    })

    # P-MAT-5: 5tau -> ratio <=1.02 (T3-provisional, not a scored perceptual verdict);
    # 0.5tau -> ratio ~1.4-1.6, measurable mainly at Hosts D/E.
    ratios_5tau = [r for r in rows_b if r["dt_sweep"] == "5tau" and r["periodic_over_first_ratio"] is not None]
    ratios_05tau = [r for r in rows_b if r["dt_sweep"] == "0.5tau" and r["periodic_over_first_ratio"] is not None]
    max_5tau = max(r["periodic_over_first_ratio"] for r in ratios_5tau)
    band_05tau = [r["periodic_over_first_ratio"] for r in ratios_05tau]
    measurable_05tau_hosts = sorted({r["host"] for r in ratios_05tau
                                      if r["periodic_over_first_ratio"] > 1.05})
    checks.append({
        "id": "P-MAT-5a", "claim": "5*tau: periodic/first-pulse ratio <= 1.02 everywhere",
        "max_measured_ratio": max_5tau, "confirmed": max_5tau <= 1.02,
    })
    checks.append({
        "id": "P-MAT-5b",
        "claim": "0.5*tau: ratio ~1.4-1.6, measurable (>1.05) only at Hosts D/E",
        "measured_ratio_range": [min(band_05tau), max(band_05tau)],
        "measurable_hosts": measurable_05tau_hosts,
        "confirmed_range": (1.3 <= min(band_05tau)) and (max(band_05tau) <= 1.7),
        "confirmed_hosts_co_locate": measurable_05tau_hosts == ["D", "E"],
    })

    out = {
        "experiment": "exp-038-t17-rate-equation-kernel",
        "panel_iteration": 15,
        "elapsed_s": elapsed,
        "n_fdtd_calls": 0,
        "test_a_rows": rows_a,
        "test_b_rows": rows_b,
        "prediction_checks": checks,
    }
    out_path = os.path.join(HERE, "results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {out_path} ({len(rows_a)} Test-A rows, {len(rows_b)} Test-B rows, "
          f"{elapsed:.3f}s)")
    for c in checks:
        print(f"  {c['id']}: {c.get('confirmed', c.get('confirmed_range'))}  -- {c['claim']}")


if __name__ == "__main__":
    main()
