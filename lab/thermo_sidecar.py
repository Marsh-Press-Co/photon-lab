"""THERMODYNAMICS' energy sidecar, promoted to reusable code (panel Iteration
20, exp-043 — docket #7 + this module's own re-scoping).

EXPRESSIBILITY CONTRACT (PANEL.md): every function here is a POST-RUN
ANALYTIC calculation, not an FDTD output. Nothing in this module runs a
field solve; every input is either a pre-measured bench quantity (sigma_ext,
an absorption ratio, ...) or a sourced witness-scenario parameter
(WitnessScenario). Labeled as such in every results.json this module feeds.

History (panel Iteration 20, Phase 2/3 record — see
`experiments/043-docket7-thermo-sidecar/NOTES.md` for the full debate):
this module replaces THREE independently-inconsistent inline
`thermo_sidecar_analytic` dicts (exp-032/033/034/035 -- not one dict
copy-pasted four ways, Red Team's own Phase-2 desk audit correction; only
exp-033/034 actually shared a formula, and it was never called at the ON
endpoint in any of them -- that number was always hand-typed).

Two regimes, dispatched explicitly -- conflating them was the historical
bug class this module exists to close:

  * WEAK-TAU (tau <= TAU_WEAK_LIMIT): reuses
    `lab.amplitude_bridge.chord_absorptance_exact`, already trust-suite
    gated (stage 14, P-TH-5) against its own now-retired weak-tau series.
    This is a THEORETICAL ray-chord model of the fraction of power
    incident on the object's OWN geometric cross-section that gets
    absorbed -- valid only where T15's own established boundary says the
    chord idiom tracks measurement (tau<=0.032).

  * ESTABLISHED-RATIO (near-saturating / measured articles, e.g. the
    sigma(I) ON endpoint tau=3.9, and `graded_black_shell`): uses a
    MEASURED sigma_abs/sigma_ext ratio directly, NOT the chord model --
    T9 already shows both established ratios (0.51, 0.6075) EXCEED the
    chord model's own <=0.5 geometric-optics ceiling, so applying the
    ray-chord idiom there would be physically wrong, not just imprecise.
    Computing absorbed WATTS from a bare ratio is under-determined (Red
    Team's Iteration-20 Phase-2 attack 1, caught by no blind seat): sigma_
    abs/sigma_ext is dimensionless: the ratio alone cannot fix an absolute
    power without sigma_ext (extinction cross-section) as a SEPARATE
    input. `absorbed_power_established_ratio` therefore takes sigma_ext
    (in grid cells) and the grid spacing explicitly, and states its own
    area-idealization (`iso_xsec_sq`) rather than silently assuming
    sigma_ext == geometric area (Q_ext=1 -- exactly the assumption T9
    already refutes for both established articles here).
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from lab.amplitude_bridge import chord_absorptance_exact

# ---------------------------------------------------------------- constants
WIEN_B_UM_K = 2897.77  # Wien displacement constant, um*K (exact SI-linked)
SIGMA_SB = 5.670374419e-8  # Stefan-Boltzmann, W/(m^2 K^4), exact SI-linked
TAU_WEAK_LIMIT = 0.032  # panel Iteration 20 Phase-2/3: EM's fix, NOT 0.5 --
# the weak-tau series this bench used to use is 5-sig-fig-accurate only to
# tau<=0.032 (chord_absorptance_exact's own docstring); this module refuses
# to call itself "weak-tau-valid" past that, on pain of a ValueError.


# --------------------------------------------------------------- weak-tau
def absorbed_fraction_weak_tau(tau: float) -> float:
    """Fraction of power incident on the object's OWN geometric
    cross-section that gets absorbed, valid only for tau<=TAU_WEAK_LIMIT.
    Reuses the already-gated `chord_absorptance_exact` (stage 14) rather
    than re-deriving the weak-tau series this module's own history shows
    was misapplied past its validated boundary (panel Iteration 20 Phase
    2, ELECTROMAGNETISM's load-bearing catch)."""
    if tau < 0:
        raise ValueError(f"tau must be >= 0, got {tau}")
    if tau > TAU_WEAK_LIMIT:
        raise ValueError(
            f"tau={tau} exceeds TAU_WEAK_LIMIT={TAU_WEAK_LIMIT} -- use "
            "absorbed_power_established_ratio with a MEASURED sigma_abs/"
            "sigma_ext ratio instead (T9: the chord model cannot exceed "
            "its own <=0.5 ceiling; near-saturating articles measure "
            "above it)")
    return chord_absorptance_exact(tau)


def absorbed_power_weak_tau(i_incident_w_cm2: float, r_out_cells: float,
                             dx_m: float, tau: float) -> float:
    """Absorbed power (W) for a weak-tau article, using the object's own
    GEOMETRIC disk area (pi*r_out^2) -- unambiguous for this branch,
    unlike the established-ratio branch below (Red Team attack 1 applies
    only there, not here, precisely because chord_absorptance_exact is
    already normalized against the geometric cross-section by
    construction)."""
    frac = absorbed_fraction_weak_tau(tau)
    area_m2 = math.pi * (r_out_cells * dx_m) ** 2
    area_cm2 = area_m2 * 1.0e4
    return i_incident_w_cm2 * area_cm2 * frac


# --------------------------------------------------------- established-ratio
def absorbed_power_established_ratio(i_incident_w_cm2: float,
                                      sigma_ext_cells: float, dx_m: float,
                                      ratio_abs_ext: float,
                                      area_convention: str = "iso_xsec_sq"
                                      ) -> dict:
    """Absorbed power (W) for a near-saturating / measured article, from a
    MEASURED sigma_abs/sigma_ext ratio and a SEPARATE sigma_ext input (Red
    Team's Iteration-20 Phase-2 attack 1 -- the ratio alone cannot fix a
    watt value).

    `area_convention="iso_xsec_sq"` (the only one implemented, disclosed
    explicitly, not defaulted-silently): the object's real absorbing area
    is taken as the SQUARE of its measured 2D extinction WIDTH
    (w = sigma_ext_cells * dx_m) -- i.e. the object is treated as compact
    (as extended along the simulation's invariant axis as across it), not
    as an infinite rod. This is a stated idealization, not a measurement:
    a finite-rod-length convention would scale P_abs linearly instead.

    Returns a dict (not a bare float) so the idealization travels with the
    number into every results.json that uses it -- never a silent float."""
    if not 0.0 <= ratio_abs_ext <= 1.0:
        raise ValueError(f"ratio_abs_ext must be in [0,1], got {ratio_abs_ext}")
    if area_convention != "iso_xsec_sq":
        raise NotImplementedError(
            f"area_convention={area_convention!r} not implemented; only "
            "'iso_xsec_sq' exists (panel Iteration 20 scope)")
    width_m = sigma_ext_cells * dx_m
    area_m2 = width_m ** 2
    area_cm2 = area_m2 * 1.0e4
    p_ext_w = i_incident_w_cm2 * area_cm2  # power "extinguished" (removed
    # from the beam), at ratio_abs_ext=1 this equals p_abs_w exactly
    p_abs_w = p_ext_w * ratio_abs_ext
    return {
        "p_abs_w": p_abs_w,
        "p_ext_w": p_ext_w,
        "area_convention": area_convention,
        "width_m": width_m,
        "area_m2": area_m2,
        "ratio_abs_ext": ratio_abs_ext,
        "sigma_ext_cells": sigma_ext_cells,
        "dx_m": dx_m,
        "i_incident_w_cm2": i_incident_w_cm2,
        "idealization_note": (
            "bench-scale, not witness-scale (T8/T13 near-field->witness "
            "bridge unresolved); iso_xsec_sq area convention (compact "
            "object, not infinite rod) -- see module docstring"),
    }


# --------------------------------------------------------------- thermal
def steady_state_delta_T(p_abs_w: float, area_m2: float, emissivity: float,
                          h_conv: float, t_ambient_k: float = 293.15) -> float:
    """Steady-state temperature rise (K) for a graybody radiating +
    convecting to an ambient at t_ambient_k, LINEARIZED about t_ambient_k
    (small-signal: dP/dT = area*(4*emissivity*SIGMA_SB*T_amb^3 + h_conv)).
    Graybody radiative-equilibrium is itself a questioned idealization for
    a dilute vapor/aerosol host (Red Team's exp-033 attack 11) -- carried
    forward unresolved, not fixed by this module (panel Iteration 20 Phase
    3, attack 3)."""
    dp_dt = area_m2 * (4.0 * emissivity * SIGMA_SB * t_ambient_k ** 3 + h_conv)
    if dp_dt <= 0:
        raise ValueError("area_m2, emissivity, h_conv must give dP/dT > 0")
    return p_abs_w / dp_dt


def transient_delta_T(p_abs_w: float, mass_kg: float, c_p: float,
                       dwell_s: float, thermal_tau_s: float | None = None,
                       delta_t_steady_k: float | None = None) -> float:
    """Temperature rise (K) after a finite dwell_s of absorption, lumped-
    capacitance, spatially uniform (ignores exp-028's own measured radial
    absorbed-power profile -- a stated, unresolved simplification).

    Two modes: (a) adiabatic linear ramp (thermal_tau_s=None) --
    dwell_s << the object's own thermal time constant, appropriate for the
    short (~10s-100s ms) dwells this program's constraint-4 (swept beam)
    scenario implies; (b) exponential approach to delta_t_steady_k, when
    both thermal_tau_s and delta_t_steady_k are supplied."""
    if thermal_tau_s is None:
        return p_abs_w * dwell_s / (mass_kg * c_p)
    if delta_t_steady_k is None:
        raise ValueError("delta_t_steady_k required when thermal_tau_s is given")
    return delta_t_steady_k * (1.0 - math.exp(-dwell_s / thermal_tau_s))


def wien_peak_wavelength_um(t_k: float) -> float:
    """Wien's displacement law: peak blackbody emission wavelength (um)."""
    if t_k <= 0:
        raise ValueError("t_k must be > 0")
    return WIEN_B_UM_K / t_k


def netd_disposition(delta_t_k: float, netd_band_k: tuple[float, float],
                      fill_factor: float = 1.0,
                      emissivity_correction: float = 1.0) -> dict:
    """Compare a computed delta_t_k against a sourced microbolometer NETD
    band. fill_factor and emissivity_correction are explicit multipliers
    on delta_t_k (never silently folded into the caller's own number).

    NETD IS AN INSTRUMENT/DETECTOR THRESHOLD, NOT A HUMAN PERCEPTUAL ONE
    (panel Iteration 20 Phase 2/3, VISION SCIENCE's mandatory fix, Red
    Team attack 7 -- elevated to load-bearing): the classification this
    function returns bears on whether a thermal camera would register the
    signature, NOT on constraint-3/4's human-eye verdict. No caller should
    read "DETECTABLE" from this function as a constraint-3 finding."""
    effective_dt = delta_t_k * fill_factor * emissivity_correction
    lo, hi = netd_band_k
    if effective_dt < lo:
        cls = "UNDETECTABLE"
    elif effective_dt < hi:
        cls = "MARGINAL"
    else:
        cls = "DETECTABLE"
    return {
        "classification": cls,
        "effective_delta_t_k": effective_dt,
        "raw_delta_t_k": delta_t_k,
        "netd_band_k": list(netd_band_k),
        "fill_factor": fill_factor,
        "emissivity_correction": emissivity_correction,
        "disclaimer": ("NETD is an instrument/detector threshold, not a "
                       "human perceptual one -- this classification does "
                       "NOT bear on constraint-3/4's human-eye verdict "
                       "(panel Iteration 20, VISION SCIENCE's mandatory "
                       "fix, Red Team attack 7)"),
    }


# ------------------------------------------------------------- witness data
@dataclass
class WitnessScenario:
    """Docket #7's sourced witness-scenario parameters. Every field carries
    its own source_refs entry -- no bare numbers (panel Iteration 20 Phase
    3). WebSearch snippet-level sourcing only (T18: WebFetch confirmed
    EGRESS_BLOCKED for scholarly domains across >=6 consecutive shift-
    confirmations, including this one)."""
    candela_range: tuple[float, float]
    candela_source_refs: list[str]
    luminous_efficacy_radiation_lm_w: float
    luminous_efficacy_note: str
    distance_m: float
    distance_source_note: str
    irradiance_w_cm2_range: tuple[float, float]
    irradiance_derivation_note: str
    dwell_s_range: tuple[float, float]
    dwell_source_refs: list[str]
    netd_k_range: tuple[float, float]
    netd_source_refs: list[str]
    extra: dict = field(default_factory=dict)
