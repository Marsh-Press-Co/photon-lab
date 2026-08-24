"""exp-067 Phase 4 — R_contact bonded-substrate conduction correction.

Panel Iteration 44, MATERIALS lead. Desk-analytic only, zero FDTD (T1
escape route: N/A), per Red Team's Phase-2 reconciled docket
(`phase2_redteam_audit.md` SS2.1) applied verbatim at Phase 3.

R4 discipline: every number in this script's printed table is produced by
invoking the actual committed `lab.thermo_sidecar.bonded_substrate_
conduction_correction` — nothing here is hand-recomputed or hand-typed.
This is the same script (same constants, same call shape) stage 25's own
gates 4/5 in `lab/validation/run_all.py` reproduce independently.
"""
from lab import thermo_sidecar as ts

K_AIR = 0.026
EMISSIVITY = 0.9
L_BENCH_M = 2.34e-6
L_MP5_730X_M = 1051.2e-6
KAPPA_WORST_SOURCED = 0.70  # exp-063's own worst sourced kappa_solid

# Baselines (bracket B, R_contact=0) for margin context.
BASE_BENCH = ts.front_surface_conduction_correction(
    K_AIR, L_BENCH_M, KAPPA_WORST_SOURCED, EMISSIVITY,
    length_provenance="bench_construction")
BASE_WITNESS = ts.front_surface_conduction_correction(
    K_AIR, L_MP5_730X_M, KAPPA_WORST_SOURCED, EMISSIVITY,
    length_provenance="extinction_derived_diagnostic_only", diagnostic_only=True)

BENCH_MARGIN_BAR = 100.0     # TD-4
WITNESS_MARGIN_BAR = 1.0     # TD-5
# Baselines' own margins (bracket B), per exp-063's own committed record.
BASELINE_BENCH_MARGIN = 674.22
BASELINE_WITNESS_MARGIN = 1.2920


def call(l_m, length_prov, diag, r_contact, r_contact_prov, r_contact_diag):
    return ts.bonded_substrate_conduction_correction(
        K_AIR, l_m, KAPPA_WORST_SOURCED, EMISSIVITY, r_contact,
        length_provenance=length_prov, diagnostic_only=diag,
        r_contact_provenance=r_contact_prov,
        r_contact_diagnostic_only=r_contact_diag)


def bench(r_contact, r_contact_prov="analogy_proxy_diagnostic", r_contact_diag=True):
    return call(L_BENCH_M, "bench_construction", False,
                r_contact, r_contact_prov, r_contact_diag)


def witness(r_contact, r_contact_prov="analogy_proxy_diagnostic", r_contact_diag=True):
    return call(L_MP5_730X_M, "extinction_derived_diagnostic_only", True,
                r_contact, r_contact_prov, r_contact_diag)


def bisect_r_contact_critical(endpoint_key, target, lo, hi, tol=1e-12, iters=200):
    """Bisection for the witness-scale R_contact that drives `endpoint_key`
    (`correction_factor_series` or `correction_factor_replace_rear`) to
    `target`. Both endpoints are monotone increasing in r_contact_m2k_w."""
    def f(r):
        d = witness(r)
        return d[endpoint_key] - target
    flo, fhi = f(lo), f(hi)
    assert flo < 0 < fhi, (flo, fhi)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if abs(fm) < tol:
            return mid
        if fm < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


TEST_POINTS = [
    ("Gate", 0.0, "n/a (identity check)"),
    ("Primary band, low", 4.0e-9, "analogy_proxy_diagnostic (query 10, -1 OOM)"),
    ("Primary anchor", 4.0e-8, "analogy_proxy_diagnostic (query 10, inter-tube vdW)"),
    ("Primary band, high", 4.0e-6, "analogy_proxy_diagnostic (query 10, +2 OOM)"),
    ("Second anchor", 6.5e-5, "analogy_proxy_diagnostic (query 2, forest/TIM interfacial)"),
    ("Stress A", 1.0e-3, "analogy_proxy_diagnostic, flagged speculative"),
    ("Stress B", 1.0e-2, "analogy_proxy_diagnostic, flagged speculative"),
]


def main():
    print(f"Baselines (bracket B, R_contact=0): CF_bench={BASE_BENCH['correction_factor']:.6f} "
          f"(margin {BASELINE_BENCH_MARGIN}x vs bar {BENCH_MARGIN_BAR}x); "
          f"CF_witness={BASE_WITNESS['correction_factor']:.6f} "
          f"(margin {BASELINE_WITNESS_MARGIN}x vs bar {WITNESS_MARGIN_BAR}x)\n")

    header = (f"{'Point':<20}{'R_contact':>12}  {'CF_b,series':>12}{'CF_b,replace':>13}"
              f"{'bench margin (series)':>24}{'bench margin (replace)':>25}  "
              f"{'CF_w,series':>12}{'CF_w,replace':>13}{'witness margin (series)':>25}"
              f"{'witness margin (replace)':>26}")
    print(header)
    rows = []
    for label, r, basis in TEST_POINTS:
        b = bench(r)
        w = witness(r)
        bench_margin_series = (BASE_BENCH["correction_factor"] / b["correction_factor_series"]) * BASELINE_BENCH_MARGIN
        bench_margin_replace = (BASE_BENCH["correction_factor"] / b["correction_factor_replace_rear"]) * BASELINE_BENCH_MARGIN \
            if r > 0 else float("inf")
        witness_margin_series = (BASE_WITNESS["correction_factor"] / w["correction_factor_series"]) * BASELINE_WITNESS_MARGIN
        witness_margin_replace = (BASE_WITNESS["correction_factor"] / w["correction_factor_replace_rear"]) * BASELINE_WITNESS_MARGIN \
            if r > 0 else float("inf")
        row = (label, r, b["correction_factor_series"], b["correction_factor_replace_rear"],
               bench_margin_series, bench_margin_replace,
               w["correction_factor_series"], w["correction_factor_replace_rear"],
               witness_margin_series, witness_margin_replace, basis)
        rows.append(row)
        print(f"{label:<20}{r:>12.2e}  {b['correction_factor_series']:>12.6f}"
              f"{b['correction_factor_replace_rear']:>13.6f}"
              f"{bench_margin_series:>24.3f}{bench_margin_replace:>25.3f}  "
              f"{w['correction_factor_series']:>12.6f}{w['correction_factor_replace_rear']:>13.6f}"
              f"{witness_margin_series:>25.4f}{witness_margin_replace:>26.4f}")

    print()
    # Falsification-boundary bisections (witness scale, kappa=0.70), both endpoints.
    r_crit_series = bisect_r_contact_critical(
        "correction_factor_series", BASELINE_WITNESS_MARGIN, 1e-12, 1.0)
    r_crit_replace = bisect_r_contact_critical(
        "correction_factor_replace_rear", BASELINE_WITNESS_MARGIN, 1e-12, 1.0)
    print(f"r_contact_critical, series endpoint (witness margin -> 1.0x): {r_crit_series:.6f} m^2K/W")
    print(f"r_contact_critical, replace-rear endpoint (witness margin -> 1.0x): {r_crit_replace:.6f} m^2K/W")

    print()
    # EM/Red Team's Stress-B divergence check, both endpoints named explicitly.
    wb = witness(1.0e-2)
    print(f"Stress B (witness, r_contact=1e-2): correction_factor_series={wb['correction_factor_series']:.10f}, "
          f"correction_factor_replace_rear={wb['correction_factor_replace_rear']:.10f}")
    margin_series = BASELINE_WITNESS_MARGIN * BASE_WITNESS["correction_factor"] / wb["correction_factor_series"]
    margin_replace = BASELINE_WITNESS_MARGIN * BASE_WITNESS["correction_factor"] / wb["correction_factor_replace_rear"]
    print(f"  -> witness margin_series={margin_series:.4f}x, margin_replace_rear={margin_replace:.4f}x")

    print()
    # Anchor scale-legitimacy check: primary vs second anchor, both endpoints, both scales.
    for label, r in [("primary anchor 4e-8", 4.0e-8), ("second anchor 6.5e-5", 6.5e-5)]:
        b = bench(r)
        w = witness(r)
        print(f"{label}: CF_bench_series={b['correction_factor_series']:.6f}  "
              f"CF_witness_series={w['correction_factor_series']:.6f}")

    return rows


if __name__ == "__main__":
    main()
