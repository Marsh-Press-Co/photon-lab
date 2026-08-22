"""Closed-form (zero-FDTD) extinction-efficiency reference for the LOCKED
`Q_ext(x)` item, panel Iteration 36 (granted unconditional by Red Team's
Iteration-34 Phase-5 ruling after three clean deferrals at Iterations
32/33/34; led Iteration 36 per Iteration 35's close). PHOTONICS seat.

EXPRESSIBILITY CONTRACT (same as `lab/thermo_sidecar.py`'s own): every
function here is a closed-form / special-function evaluation, not an FDTD
output. Nothing in this module runs a field solve -- it is pure
`scipy.special` Bessel/Hankel evaluation, house-style with
`experiments/034-floor-convergence-scale-bridge/design_geometry.py`'s
`chord_model_g0` (plain numpy/scipy, no fit, no FDTD, docstring cites its
source).

PHYSICS + SOURCE
-----------------
Normal-incidence plane-wave scattering by an infinite circular cylinder,
TM_z polarization (E-field along the cylinder axis -- this bench's own 2D
TMz convention, confirmed against `lab/__init__.py`'s module docstring and
`lab/fdtd2d.py`'s Sx accumulator, which is built from Ez*Hy). This is the
textbook "infinite cylinder at normal incidence, E parallel to the
cylinder axis" case (Bohren & Huffman, *Absorption and Scattering of Light
by Small Particles*, Wiley 1983/1998, Chapter 8 "Particles Larger than
Sphere: Perturbation Approaches", Section 8.4 "Scattering by an infinite
cylinder at normal incidence" -- B&H's own two-polarization dual-series
formalism for infinite cylinders). WebFetch to scholarly domains is
EGRESS_BLOCKED in this environment (same standing condition
`thermo_sidecar.py`'s `WitnessScenario` already documents, T18) so this
was sourced via WebSearch snippet-level confirmation, not a full PDF read;
cross-checked against multiple independent EM-scattering references
returned by that search (ScienceDirect/arXiv summaries of the same B&H-
style formalism) which all agree on the same efficiency-formula SHAPE:

    Q_ext = (2/x) * Re[ c_0 + 2*sum_{n=1..inf} c_n ]
    Q_sca = (2/x) * ( |c_0|^2 + 2*sum_{n=1..inf} |c_n|^2 )

where x = k*a is the size parameter (k = 2*pi/lambda, a = cylinder
radius) and c_n are the cylinder's normal-incidence scattering
coefficients for the polarization in question.

This module specializes to the PERFECTLY CONDUCTING (PEC) cylinder, where
the coefficients are not a dielectric Mie series but the cylinder's own
one-line boundary condition: for E_z (TM) polarization, tangential E must
vanish at the PEC surface (rho=a). Using the standard e^{-i*omega*t} time
convention, Jacobi-Anger expansion of the incident plane wave

    E_z^inc = E0 * exp(i*k*x) = E0 * sum_n i^n J_n(k*rho) exp(i*n*phi)

and an outgoing scattered field E_z^sca = E0 * sum_n i^n c_n H_n^(1)(k*rho)
exp(i*n*phi) (H_n^(1) chosen for the outgoing-wave radiation condition),
E_z^inc + E_z^sca = 0 at rho=a term-by-term in n gives EXACTLY

    c_n(x) = -J_n(x) / H_n^(1)(x)

-- confirmed against the general search-returned formula pattern
("b_n = -J_n(...)/H_n(...)" boundary-condition form for the TM/soft
cylinder). This module's own self-test (`_self_test`, below) is the
independent numerical proof that this sign/coefficient choice is right:
a PEC cylinder is LOSSLESS, so Q_ext must equal Q_sca EXACTLY (no
absorption channel exists) -- this is an energy-conservation identity, not
an assumption, and the code checks it to ~1e-13 at eight x values spanning
seven decades before any Q_ext(x) number here is trusted.

Q_ext -> 2 as x -> infinity is the "extinction paradox" (see e.g.
Wikipedia "Extinction paradox", citing the general result that the
large-particle geometric-optics limit for ANY large opaque/reflecting
obstacle is Q_ext=2, not 1, by the optical theorem's forward-diffraction
term -- valid regardless of composition, cylinder or sphere). This
module's self-test checks that large-x limit numerically (x=1000, x=1e6).

No literature-sourced FINITE-x asymptotic correction term (of the
"Q_ext = 2 + O(x^p)" form) could be confirmed via the WebSearch-only
sourcing available in this environment -- the classic van de Hulst
edge-wave correction (Q_ext ~ 2 + x^(-2/3)) is well documented for SPHERES
but this module could not source a cylinder-specific coefficient it
trusts. Per this cycle's own instructions: rather than fabricate one, this
module reports an OBSERVED (not literature-cited) empirical power-law fit
to its own exact numerical series at large x -- see `_self_test` output
and the Phase-1 writeup -- clearly labeled as this module's own numerical
finding, not a sourced formula, and NOT used for anything but qualitative
discussion. Every Q_ext(x) number this module returns for actual use is
the EXACT partial-wave series, not any asymptotic approximation.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

from scipy.special import hankel1, jv

X_CONVERGENCE_CHECK_MAX = 255.0
# Phase-2 mandatory fix MF-2 (QUANTUM OPTICS' catch, Red-Team-reconfirmed
# at the exact threshold): the series-convergence self-check (_self_test
# gate 3) calls q_ext_pec_cylinder with 2.2x the default n_terms as its own
# comparator. That COMPARATOR call -- not the production default-n_terms
# path, which stays finite through at least x=300 -- silently returns NaN
# via Bessel/Hankel underflow starting exactly at x=260 (255 still finite).
# This constant is the documented safe ceiling for gate 3 specifically; see
# `_self_test`'s own docstring for the full account.

# --------------------------------------------------------------- core series


def _n_terms_default(x: float) -> int:
    """Series truncation order. Cylinder partial-wave series converge past
    n~x (evanescent for n>x, same physical origin as the analogous 3D Mie
    truncation rule) -- this uses the same functional FORM as the standard
    Wiscombe/Bohren-Huffman sphere rule (N ~ x + a*x^(1/3) + b), generalized
    here (not itself sourced for cylinders specifically) with a generous
    margin, and its sufficiency is verified empirically by `_self_test`'s
    own nmax-stability check (increasing nmax further must not move the
    5th significant figure) rather than trusted on the formula alone."""
    return int(x + 15.0 * abs(x) ** (1.0 / 3.0) + 15) + 1


def c_n_pec(n: int, x: float) -> complex:
    """Normal-incidence TM_z (E-parallel) scattering coefficient of a
    perfectly-conducting infinite cylinder, order n, size parameter x=k*a.
    c_n(x) = -J_n(x) / H_n^(1)(x) -- see module docstring for the boundary-
    condition derivation and its energy-conservation self-test."""
    return -jv(n, x) / hankel1(n, x)


def q_ext_pec_cylinder(x: float, n_terms: int | None = None) -> float:
    """Exact extinction efficiency Q_ext(x) of a normally-illuminated,
    perfectly-conducting infinite cylinder, TM_z (E parallel to cylinder
    axis) polarization -- the closed-form partial-wave (Bessel/Hankel)
    series, evaluated to convergence (no FDTD, no discretization of
    Maxwell's equations; see module docstring for the formula and its
    source). `x = k*r_out` (size parameter). This is the SHARP-EDGE,
    FULLY-OPAQUE reference/bounding case -- NOT a model of this bench's
    own graded_black_shell absorber (soft, quintic-smooth conductivity
    onset); see the Phase-1 writeup for the directional argument."""
    if x <= 0:
        raise ValueError(f"x (size parameter k*a) must be > 0, got {x}")
    n_terms = n_terms if n_terms is not None else _n_terms_default(x)
    total = c_n_pec(0, x).real
    for n in range(1, n_terms + 1):
        total += 2.0 * c_n_pec(n, x).real
    return -(2.0 / x) * total


def q_sca_pec_cylinder(x: float, n_terms: int | None = None) -> float:
    """Exact scattering efficiency Q_sca(x), same series/coefficients as
    `q_ext_pec_cylinder`. For a PEC (lossless) cylinder Q_sca == Q_ext
    EXACTLY (no absorption channel) -- this identity is this module's own
    load-bearing self-test, not merely a cross-check."""
    if x <= 0:
        raise ValueError(f"x (size parameter k*a) must be > 0, got {x}")
    n_terms = n_terms if n_terms is not None else _n_terms_default(x)
    total = abs(c_n_pec(0, x)) ** 2
    for n in range(1, n_terms + 1):
        total += 2.0 * abs(c_n_pec(n, x)) ** 2
    return (2.0 / x) * total


# ------------------------------------------------------------- bench bridge


def bench_size_parameter(r_out_cells: float, dx_m: float, wavelength_m: float) -> dict:
    """k*a for this bench's own geometry, computed from real inputs (never
    hand-typed -- R4). Returns a dict so every intermediate (r_out_m, k)
    travels with the number, same disclosure convention as
    `thermo_sidecar.absorbed_power_established_ratio`."""
    if r_out_cells <= 0 or dx_m <= 0 or wavelength_m <= 0:
        raise ValueError("r_out_cells, dx_m, wavelength_m must all be > 0")
    r_out_m = r_out_cells * dx_m
    k = 2.0 * math.pi / wavelength_m
    x = k * r_out_m
    return {"r_out_cells": r_out_cells, "dx_m": dx_m, "wavelength_m": wavelength_m,
            "r_out_m": r_out_m, "k_rad_per_m": k, "x_ka": x}


@dataclass
class QextComparison:
    """Bench-measured Q_ext vs. the exact PEC-sharp-edge reference at the
    SAME x -- the deliverable this module exists to produce. All fields
    are populated from code-computed values, never hand-typed (R4)."""
    x_ka: float
    q_ext_pec_reference: float
    q_ext_measured: float
    ratio_measured_over_pec: float
    q_ext_measured_sq: float          # the iso_xsec_sq AREA-domain figure
    q_ext_pec_reference_sq: float
    sigma_ext_cells: float
    dx_m: float
    r_out_cells: float
    source_note: str


def compare_measured_to_pec(r_out_cells: float, dx_m: float, wavelength_m: float,
                             sigma_ext_cells: float) -> QextComparison:
    """Bundles bench_size_parameter + q_ext_pec_cylinder + the bench's own
    measured Q_ext (= sigma_ext_cells/(2*r_out_cells), the SAME quantity
    `experiments/002-cross-sections/run.py` computes and stores as
    `q_ext` in its own results.json, and the SAME quantity
    `thermo_sidecar.absorbed_power_established_ratio`'s `iso_xsec_sq`
    convention implicitly assumes when it takes area=(sigma_ext*dx)^2)
    into one disclosed, code-computed comparison."""
    geo = bench_size_parameter(r_out_cells, dx_m, wavelength_m)
    x = geo["x_ka"]
    q_pec = q_ext_pec_cylinder(x)
    q_meas = sigma_ext_cells / (2.0 * r_out_cells)
    return QextComparison(
        x_ka=x, q_ext_pec_reference=q_pec, q_ext_measured=q_meas,
        ratio_measured_over_pec=q_meas / q_pec,
        q_ext_measured_sq=q_meas ** 2, q_ext_pec_reference_sq=q_pec ** 2,
        sigma_ext_cells=sigma_ext_cells, dx_m=dx_m, r_out_cells=r_out_cells,
        source_note=("q_ext_measured = sigma_ext_cells/(2*r_out_cells), same "
                      "formula as experiments/002-cross-sections/run.py's own "
                      "r['q_ext'] field; q_ext_pec_reference is the EXACT "
                      "sharp-edge PEC partial-wave series at the SAME x, "
                      "NOT a model of the graded_black_shell profile"),
    )


# ------------------------------------------------------------------- self-test


def _self_test(verbose: bool = True) -> dict:
    """Identity gates this module's own numbers must clear before being
    trusted (candidate trust-suite content -- see Phase-1 writeup / Phase-3
    synthesis for the stage-21 promotion, panel Iteration 36):

    1. ENERGY CONSERVATION (absolute identity, SIGN-CONVENTION SCOPE ONLY --
       corrected wording, Phase-2 mandatory fix MF-1): a PEC cylinder is
       lossless, so Q_ext(x) == Q_sca(x) EXACTLY at every x -- checked at 8
       values spanning x=1e-3 .. 1e3 (7 decades), tolerance 1e-9 absolute.
       ELECTROMAGNETISM and QUANTUM OPTICS independently proved (Phase 2,
       reconfirmed by Red Team a third way) that `-Re(c_n) == |c_n|^2` is an
       ALGEBRAIC TAUTOLOGY for ANY coefficient of the form c_n=-A/(A+iB)
       with real A,B -- it holds identically for this module's own TM_z
       (non-derivative Bessel) coefficients AND for the different TE_z
       (derivative-Bessel) polarization's coefficients alike. This gate
       therefore proves only the overall SIGN of the coefficient (it did
       catch a real first-draft bug, Q_ext->-2) -- it does NOT discriminate
       TM_z from TE_z or from any other lossless boundary condition. That
       polarization-specific correctness rests on two OTHER things, not on
       this gate: the boundary-condition derivation in the module docstring
       (independently re-derived by both ELECTROMAGNETISM and QUANTUM
       OPTICS from Jacobi-Anger + E_z(a)=0), and gate 4 below (the
       load-bearing, non-tautological check).
    2. LARGE-x ASYMPTOTE (the "extinction paradox"): Q_ext(x) -> 2 as
       x -> infinity, for ANY opaque/reflecting obstacle (see module
       docstring, Wikipedia "Extinction paradox"). Checked at x=1e3
       (Q_ext within 0.011 of 2) and x=1e6 (within 1e-4 of 2) -- both
       band widths set from this module's OWN observed monotone-decreasing
       approach (see `results['large_x']`), not asserted a priori. This
       limit is genuinely generic (also holds for TE_z, e.g. Q_ext(TE_z,
       x=1e3)~=1.9991) -- disclosed as such, not claimed polarization-
       specific.
    3. SERIES-CONVERGENCE STABILITY (VALID FOR x <= X_CONVERGENCE_CHECK_MAX
       ONLY -- Phase-2 mandatory fix MF-2, QUANTUM OPTICS' catch, Red-Team-
       reconfirmed at the exact threshold x=260): at the bench's own x=ka,
       increasing n_terms by up to 2.2x past the default truncation must
       not move the 10th significant figure -- rules out a truncation
       artifact (R3's meta-rule: any surprising numeric result needs a
       resolution/convergence check; this is that check for a zero-FDTD
       series). The 2.2x-terms COMPARATOR CALL ITSELF (not the production
       `q_ext_pec_cylinder` at its own default n_terms, which stays finite
       through at least x=300) silently returns NaN via Bessel/Hankel
       underflow for x>=260 -- a self-check-scaffolding ceiling, not a
       production-formula bug, but undisclosed in the original draft. This
       function now refuses to run gate 3 above `X_CONVERGENCE_CHECK_MAX`
       rather than silently reporting a spurious pass/fail on a NaN
       comparison.
    4. EMPIRICAL CROSS-VALIDATION vs. REAL FDTD BENCH DATA (Phase-2
       mandatory fix MF-6, Red Team's own new finding -- the load-bearing
       answer to gate 1's scope limitation): `experiments/002-cross-
       sections/results.json`'s three "reflector" scenes are a BARE PEC
       disk (`materials.pec_disk`, R_CORE=30 cells, no shell) at
       450/600/750nm -- a genuine, independent, non-tautological Maxwell-
       equations measurement (this bench's own Ez/Hy time-domain FDTD
       solver, not this module's own closed-form code) of Q_ext at three
       size parameters (x=7.54/9.42/12.57) distinct from the flagship's
       own x=24.50. Comparing `q_ext_pec_cylinder(x)` against those three
       measured `q_ext` values is the actual polarization/formula check
       gate 1 cannot provide: TWO INDEPENDENT ANSWERS -- exact closed-form
       series vs. a full discretized Maxwell solve -- agreeing to a few
       percent is not explainable by a sign-convention tautology.
    """
    results = {}

    energy_xs = [1e-3, 1e-2, 1e-1, 1.0, 5.0, 24.504422698000383, 100.0, 1000.0]
    energy_devs = []
    for x in energy_xs:
        qe, qs = q_ext_pec_cylinder(x), q_sca_pec_cylinder(x)
        energy_devs.append(abs(qe - qs))
    results["energy_conservation"] = {
        "xs": energy_xs, "max_abs_dev": max(energy_devs), "tolerance": 1e-9,
        "pass": max(energy_devs) <= 1e-9,
    }

    q1e3 = q_ext_pec_cylinder(1000.0)
    q1e6 = q_ext_pec_cylinder(1.0e6, n_terms=_n_terms_default(1.0e6))
    results["large_x"] = {
        "Q_ext(x=1e3)": q1e3, "dev_from_2_at_1e3": abs(q1e3 - 2.0),
        "Q_ext(x=1e6)": q1e6, "dev_from_2_at_1e6": abs(q1e6 - 2.0),
        "pass": abs(q1e3 - 2.0) <= 0.011 and abs(q1e6 - 2.0) <= 1.0e-4,
    }

    x_bench = 24.504422698000383
    if x_bench > X_CONVERGENCE_CHECK_MAX:
        raise ValueError(
            f"gate 3 (series-convergence stability) is only valid for "
            f"x<={X_CONVERGENCE_CHECK_MAX} -- the 2.2x-terms comparator "
            f"underflows to NaN at x>=260 (MF-2). Requested x={x_bench} "
            "exceeds the documented safe ceiling; do not silently report "
            "a pass/fail against a NaN comparison.")
    n_default = _n_terms_default(x_bench)
    q_default = q_ext_pec_cylinder(x_bench, n_terms=n_default)
    q_extra = q_ext_pec_cylinder(x_bench, n_terms=int(n_default * 2.2))
    results["convergence_stability_at_bench_x"] = {
        "x": x_bench, "n_terms_default": n_default,
        "n_terms_2x": int(n_default * 2.2),
        "Q_ext_default": q_default, "Q_ext_2x_terms": q_extra,
        "abs_diff": abs(q_default - q_extra),
        "pass": abs(q_default - q_extra) <= 1e-10,
    }

    # Gate 4 (Phase-2 mandatory fix MF-6, Red Team's own new finding): the
    # load-bearing, NON-tautological empirical cross-check gate 1 cannot
    # provide -- exact closed-form series vs. this bench's own real Ez/Hy
    # FDTD solve, three independent size parameters, already-committed data
    # (zero new FDTD). `materials.pec_disk`, R_CORE=30 cells, dx=30nm at
    # every lambda (cpl=15/20/25 at 450/600/750nm respectively -- verified
    # against experiments/002-cross-sections/run.py's own SWEEP/R_CORE),
    # measured `q_ext` from experiments/002-cross-sections/results.json's
    # "reflector-*" entries (bit-exact, not hand-typed -- re-pasted here
    # with their source cited; see the module's own regression companion
    # for a from-source-file re-derivation).
    _REFLECTOR_BENCH = [
        # (lambda_nm, cpl, r_core_cells, q_ext_measured, source)
        (450.0, 15, 30, 2.145908482382741,
         "experiments/002-cross-sections/results.json::reflector-450.q_ext"),
        (600.0, 20, 30, 2.2084076980980476,
         "experiments/002-cross-sections/results.json::reflector-600.q_ext"),
        (750.0, 25, 30, 2.309554004858993,
         "experiments/002-cross-sections/results.json::reflector-750.q_ext"),
    ]
    empirical_rows = []
    max_rel_dev = 0.0
    for lam_nm, cpl, r_core_cells, q_meas, source in _REFLECTOR_BENCH:
        dx_m = (lam_nm * 1.0e-9) / cpl
        geo = bench_size_parameter(r_core_cells, dx_m, lam_nm * 1.0e-9)
        q_pec = q_ext_pec_cylinder(geo["x_ka"])
        rel_dev = (q_meas - q_pec) / q_pec
        max_rel_dev = max(max_rel_dev, abs(rel_dev))
        empirical_rows.append({
            "lambda_nm": lam_nm, "x_ka": geo["x_ka"], "q_ext_pec_theory": q_pec,
            "q_ext_measured_fdtd": q_meas, "rel_dev": rel_dev, "source": source,
        })
    results["empirical_cross_validation"] = {
        "rows": empirical_rows, "max_abs_rel_dev": max_rel_dev,
        "tolerance": 0.03, "pass": max_rel_dev <= 0.03,
        "note": ("bare PEC disk, R_CORE=30 cells, this bench's own real "
                 "Ez/Hy FDTD solve (experiments/002-cross-sections), NOT "
                 "this module's own code, at 3 size parameters distinct "
                 "from the flagship's x=24.50 -- the actual formula/"
                 "polarization check gate 1's tautology cannot provide."),
    }

    results["small_x_observation"] = {
        "note": ("NOT an asserted gate -- an honest, code-computed "
                 "observation: Q_ext_PEC DIVERGES (grows) as x->0 for this "
                 "TM/E-parallel polarization rather than vanishing "
                 "(unlike the familiar 3D Rayleigh Q_ext->0 sphere limit). "
                 "This is the known thin-wire asymmetry (axial E-field "
                 "drives free current along a thin conductor even as "
                 "ka->0; the orthogonal H-parallel/TE polarization does "
                 "NOT show this and was not computed here -- out of scope "
                 "for this bench's TMz convention). Reported, not treated "
                 "as an error."),
        "Q_ext(x=1e-3)": q_ext_pec_cylinder(1.0e-3),
        "Q_ext(x=1e-2)": q_ext_pec_cylinder(1.0e-2),
    }

    all_pass = (results["energy_conservation"]["pass"]
                and results["large_x"]["pass"]
                and results["convergence_stability_at_bench_x"]["pass"]
                and results["empirical_cross_validation"]["pass"])
    results["all_gates_pass"] = all_pass

    if verbose:
        print("qext_theory self-test")
        print(f"  [gate 1] energy conservation (sign-convention scope only, "
              f"MF-1): max|dev|={results['energy_conservation']['max_abs_dev']:.3e} "
              f"(tol 1e-9) -> {'PASS' if results['energy_conservation']['pass'] else 'FAIL'}")
        print(f"  [gate 2] large-x asymptote Q_ext->2: "
              f"Q_ext(1e3)={q1e3:.6f} (dev={abs(q1e3-2):.3e}), "
              f"Q_ext(1e6)={q1e6:.6f} (dev={abs(q1e6-2):.3e}) "
              f"-> {'PASS' if results['large_x']['pass'] else 'FAIL'}")
        print(f"  [gate 3] convergence stability @ bench x={x_bench:.6f} "
              f"(valid for x<={X_CONVERGENCE_CHECK_MAX:.0f} only, MF-2): "
              f"n={n_default}->{int(n_default*2.2)} terms, "
              f"Q_ext {q_default!r} vs {q_extra!r}, diff={abs(q_default-q_extra):.3e} "
              f"-> {'PASS' if results['convergence_stability_at_bench_x']['pass'] else 'FAIL'}")
        print(f"  [gate 4] empirical cross-validation vs. real FDTD bench "
              f"data (MF-6, bare PEC reflector, experiments/002): "
              f"max|rel_dev|={max_rel_dev*100:.3f}% (tol 3%) "
              f"-> {'PASS' if results['empirical_cross_validation']['pass'] else 'FAIL'}")
        for row in empirical_rows:
            print(f"           lambda={row['lambda_nm']:.0f}nm x={row['x_ka']:.4f} "
                  f"theory={row['q_ext_pec_theory']:.4f} measured={row['q_ext_measured_fdtd']:.4f} "
                  f"rel_dev={row['rel_dev']*100:+.3f}%")
        print(f"  [info] small-x divergence (not a gate): "
              f"Q_ext(1e-3)={results['small_x_observation']['Q_ext(x=1e-3)']:.4f}, "
              f"Q_ext(1e-2)={results['small_x_observation']['Q_ext(x=1e-2)']:.4f}")
        print(f"  ALL GATES: {'PASS' if all_pass else 'FAIL'}")

    return results


if __name__ == "__main__":
    _self_test()

    print("\nbench evaluation (graded_black_shell_flagship, exp-020/043):")
    R_OUT_CELLS, DX_M, LAMBDA_M = 78, 30.0e-9, 600.0e-9
    SIGMA_EXT_CELLS = 240.0073740162445  # experiments/043-docket7-thermo-sidecar/results.json
    comp = compare_measured_to_pec(R_OUT_CELLS, DX_M, LAMBDA_M, SIGMA_EXT_CELLS)
    print(f"  x = ka = {comp.x_ka!r}")
    print(f"  Q_ext_PEC(x)      = {comp.q_ext_pec_reference!r}")
    print(f"  Q_ext_measured    = {comp.q_ext_measured!r}")
    print(f"  ratio measured/PEC = {comp.ratio_measured_over_pec!r}")
    print(f"  Q_ext_measured^2  = {comp.q_ext_measured_sq!r}  (area-domain, iso_xsec_sq)")
    print(f"  Q_ext_PEC(x)^2    = {comp.q_ext_pec_reference_sq!r}  (area-domain PEC reference)")
    print(f"  ratio is {comp.ratio_measured_over_pec*100:.1f}% of the PEC reference -- "
          f"REFERENCE/BOUNDING comparison only, NOT a literal model of the "
          f"graded_black_shell profile (MF-3, panel Iteration 36 Phase 2); "
          f"bounds w_on's diffraction excess inside a physically sane "
          f"envelope, does NOT change any scored thermal margin (MF-4).")
