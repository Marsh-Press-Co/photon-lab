"""THERMODYNAMICS' energy sidecar, promoted to reusable code (panel Iteration
20, exp-043 — docket #7 + this module's own re-scoping).

Panel Iteration 31 (exp-054) adds `gas_conduction_h_eff`,
`lumped_cube_mass_kg`, and `mixed_length_scale_regime` -- the corrected,
length-scale-consistent h_eff/mass/area chain replacing exp-045's own
one-off `self_consistent_regime` script pattern with reusable, trust-suite-
gated (stage 18) code. See `mixed_length_scale_regime`'s own docstring.

Panel Iteration 40 (exp-063) adds `biot_number` and
`front_surface_conduction_correction` -- promoting the informal Biot-
number arithmetic run by hand at Iteration 22 (Attack 6) and Iteration 23
(the Maxwell-Garnett fill-fraction table) to trust-suite-gated code
(stage 23), and sourcing kappa_solid for the actual candidate material
class (CNT-forest/Vantablack-type) for the first time -- every prior Biot
check used silicon's kappa=148 W/(m*K), ASSUMED/unsourced since Iteration
25. See `front_surface_conduction_correction`'s own docstring for the
worst-case model and its disclosed, unresolved caveats.

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


# -------------------------------------------- length-scale-consistent chain
def gas_conduction_h_eff(k_air: float, l_geometric: float) -> float:
    """Quiescent gas-phase conduction heat-transfer coefficient (Nu=2
    limit), h_eff = k_air / l_geometric.

    `l_geometric` MUST be a real geometric length of the conducting/
    radiating SOLID body (e.g. the bench's own r_out) -- NEVER an optical/
    extinction-derived length (e.g. w_on = sigma_ext_cells*dx_m). Panel
    Iteration 22 (exp-045) found this module's original chain silently
    mixed the two; Panel Iteration 31 (exp-054) argues the physical case to
    a conclusion and promotes the corrected pair of helpers here. See
    `mixed_length_scale_regime` for the caller-facing entry point."""
    if l_geometric <= 0:
        raise ValueError("l_geometric must be > 0")
    return k_air / l_geometric


def lumped_cube_mass_kg(density_kg_m3: float, l_geometric: float) -> float:
    """Lumped-capacitance cube-shaped thermal mass, mass = density *
    l_geometric**3 (mirrors exp-045's own `self_consistent_regime`
    convention -- a stated idealization, not the module's own true-disk
    geometric_disk_area_m2 convention used elsewhere for the weak-tau
    branch; see exp-054/NOTES.md idealizations).

    `l_geometric` MUST be the SAME geometric length passed to
    `gas_conduction_h_eff` for the same object -- mixing lengths across the
    h_eff/mass/area chain is the exact historical bug this pair of
    functions exists to prevent."""
    if density_kg_m3 <= 0 or l_geometric <= 0:
        raise ValueError("density_kg_m3 and l_geometric must be > 0")
    return density_kg_m3 * l_geometric ** 3


def mixed_length_scale_regime(p_abs_w: float, l_geometric_m: float,
                               k_air: float, density_kg_m3: float,
                               c_p_j_kgk: float, emissivity: float,
                               t_ambient_k: float = 293.15) -> dict:
    """The Iteration-31/exp-054 corrected thermal chain: `p_abs_w` stays
    whatever an UPSTREAM optical measurement produced it as (typically
    `absorbed_power_established_ratio`'s w_on-based p_abs_w, UNCHANGED --
    that function is not touched by this cycle), while h_eff, thermal
    mass, and radiating/convecting area ALL derive from `l_geometric_m`
    alone (the object's real geometric length, e.g. r_out) -- never from
    whatever optical length p_abs_w happened to be measured at. The chain
    is MIXED BY DESIGN (p_abs_w and the h_eff/mass/area triple can use
    different lengths), not a bug to eliminate: they answer different
    physical questions (how much power is absorbed, measured optically;
    how fast the resulting heat leaves the solid, geometric). See
    `lab/thermo_sidecar.py` module docstring and
    `experiments/054-heff-length-scale-rederivation/phase3_synthesis.md`
    for the full argument and Phase-2 panel debate.

    `area_m2 = l_geometric_m**2` (the iso-sq convention
    `absorbed_power_established_ratio`'s own area already uses, anchored
    at a different length here -- NOT claimed to be more "real" bench
    geometry than that convention; only the LENGTH differs, exp-054 Phase-2
    Red Team attack 5's corrected wording)."""
    h_eff = gas_conduction_h_eff(k_air, l_geometric_m)
    mass_kg = lumped_cube_mass_kg(density_kg_m3, l_geometric_m)
    area_m2 = l_geometric_m ** 2
    dp_dt = area_m2 * (4.0 * emissivity * SIGMA_SB * t_ambient_k ** 3 + h_eff)
    if dp_dt <= 0:
        raise ValueError("area_m2, emissivity, h_eff must give dP/dT > 0")
    dt_ss_full = p_abs_w / dp_dt
    tau_thermal_s = mass_kg * c_p_j_kgk / dp_dt
    return {
        "length_convention": "mixed (p_abs on its own optical length; "
                              "h_eff/mass/area on l_geometric_m)",
        "l_geometric_m": l_geometric_m,
        "p_abs_w": p_abs_w,
        "h_eff_w_m2k": h_eff,
        "mass_kg": mass_kg,
        "area_m2": area_m2,
        "dp_dt_w_k": dp_dt,
        "dt_ss_full_K": dt_ss_full,
        "tau_thermal_s": tau_thermal_s,
        "k_air": k_air,
        "density_kg_m3": density_kg_m3,
        "c_p_j_kgk": c_p_j_kgk,
        "emissivity": emissivity,
        "t_ambient_k": t_ambient_k,
        "material_provenance": "ASSUMED -- provenance terminates unsourced "
                                "(T18); see REALIZABILITY_MEMO.md and "
                                "exp-054/NOTES.md idealizations",
        "mass_fill_fraction_assumption": (
            "mass_kg assumes 100%-fill crystalline solid at l_geometric_m "
            "-- undisclosed in the Iteration-31 Phase-1 draft, disclosed "
            "here per Red Team mandatory fix 3"),
        "netd_disclaimer": ("NETD is an instrument/detector threshold, not "
                             "a human perceptual one -- any classification "
                             "derived from this dict's dt_ss_full_K does "
                             "NOT bear on constraint-3/4's human-eye "
                             "verdict (panel Iteration 20 origin, "
                             "reaffirmed Iteration 31)"),
    }


# --------------------------------------- front-surface conduction correction
def biot_number(k_air: float, k_solid: float) -> float:
    """Biot number for gas-phase-conduction-limited vs. solid-conduction-
    limited heat transport, Bi = k_air / k_solid (dimensionless).

    Panel Iteration 40 (exp-063), promoting the informal Iteration-22
    Attack-6 / Iteration-23 desk arithmetic to trust-suite-gated code.
    Bi << 1: the solid conducts heat internally much faster than gas
    removes it externally -- the LUMPED (uniform-temperature) assumption
    every `mixed_length_scale_regime` call to date has silently made is
    self-consistent. Bi ~ 1 or larger: internal conduction is the
    bottleneck, not external gas/radiative loss -- a lumped-capacitance
    dT UNDERSTATES the true peak (front-surface) temperature rise. This
    function returns the bare ratio; `front_surface_conduction_correction`
    below turns it into an actual dT correction factor."""
    if k_air <= 0 or k_solid <= 0:
        raise ValueError("k_air and k_solid must be > 0")
    return k_air / k_solid


def front_surface_conduction_correction(k_air: float, l_geometric_m: float,
                                         k_solid: float, emissivity: float,
                                         t_ambient_k: float = 293.15) -> dict:
    """Worst-case front-surface conduction correction factor for a lumped
    steady-state dT estimate, panel Iteration 40 (exp-063).

    MODEL (deliberately worst-case, an idealization every caller must
    disclose): absorbed power enters uniformly over the illuminated FRONT
    surface (area = l_geometric_m**2, matching `mixed_length_scale_regime`'s
    own area convention) and must conduct across the full l_geometric_m
    through k_solid before it can leave via the already-established
    combined gas-conduction + radiation channel, idealized as acting ONLY
    at the far (rear) boundary. This is an UPPER BOUND on the true
    front-vs-lumped gap, not a measurement -- a real object loses some
    heat locally near the front too (exp-063 NOTES.md's own front-
    colocated-loss bracket endpoint is exactly `mixed_length_scale_regime`'s
    own unmodified `dt_ss_full_K`, i.e. correction_factor=1 identically --
    not a separate function here, since it needs none).

    correction_factor = 1 + Bi_gas + Bi_rad(l_geometric_m), where
    Bi_gas = k_air/k_solid (length-invariant) and
    Bi_rad(L) = 4*emissivity*SIGMA_SB*t_ambient_k**3 * L / k_solid
    (length-dependent -- negligible at bench scale, non-negligible at
    witness scale, exp-063 Section 4).

    ABSOLUTE IDENTITY (trust-suite gate, stage 23): as k_solid -> infinity,
    both Bi terms -> 0 and correction_factor -> 1 exactly, recovering
    `mixed_length_scale_regime`'s own dt_ss_full_K unmodified -- an
    infinitely-conductive solid is, by construction, indistinguishable
    from the lumped-capacitance idealization every prior call implicitly
    assumed.

    CAVEATS THIS FUNCTION DOES NOT RESOLVE, disclosed at every call site
    per exp-063's own mandatory-fix docket (NOT internal to this function):
    (1) `l_geometric_m` here plays a generation-side role (front-surface
    absorption) `mixed_length_scale_regime`'s own docstring never licenses
    for the bench-scale flagship, whose established radial absorption
    profile peaks near r_in, not r_out (T9); (2) the rear-only-loss
    boundary condition is asserted, not derived, as this geometry's worst
    case -- a real coating-on-substrate deployment may lose heat closer to
    the front, which would push correction_factor toward 1, not away from
    it; (3) at witness scale, `l_geometric_m` may be an optical-extinction-
    derived length (t=tau_true/alpha), which `gas_conduction_h_eff`'s own
    docstring explicitly bars from a conduction-length role -- unresolved,
    T23-adjacent (see exp-063 NOTES.md)."""
    if k_air <= 0 or l_geometric_m <= 0 or k_solid <= 0 or emissivity <= 0:
        raise ValueError(
            "k_air, l_geometric_m, k_solid, emissivity must be > 0")
    bi_gas = biot_number(k_air, k_solid)
    bi_rad = (4.0 * emissivity * SIGMA_SB * t_ambient_k ** 3
              * l_geometric_m / k_solid)
    correction_factor = 1.0 + bi_gas + bi_rad
    return {
        "correction_factor": correction_factor,
        "bi_gas": bi_gas,
        "bi_rad": bi_rad,
        "k_air": k_air,
        "l_geometric_m": l_geometric_m,
        "k_solid": k_solid,
        "emissivity": emissivity,
        "t_ambient_k": t_ambient_k,
        "model_note": (
            "worst-case, rear-only-loss, front-surface-generation 1D "
            "planar conduction resistance -- an UPPER BOUND on the true "
            "correction, not a measurement; see exp-063 NOTES.md for the "
            "front-colocated-loss bracket endpoint (correction_factor=1, "
            "mixed_length_scale_regime's own dt_ss_full_K unmodified) and "
            "the generation-geometry / length-legitimacy caveats"),
        "netd_disclaimer": (
            "NETD is an instrument/detector threshold, not a human "
            "perceptual one -- any classification derived from "
            "correction_factor * dt_ss_full_K does NOT bear on "
            "constraint-3/4's human-eye verdict (panel Iteration 20 "
            "origin, reaffirmed Iteration 40)"),
    }


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
