"""
lab.temporal_csf — the T3 temporal-contrast screen.
====================================================
A standalone, zero-FDTD-cost frequency-domain screen for T17's own
standing gap (LOGBOOK.md live thread T3 / T17, Panel Iteration 16 /
exp-039): does a σ(I)-with-memory switching transient (`lab.kinetics`,
exp-038) sit inside a band the human visual system's TEMPORAL contrast
sensitivity is sensitive to, or clear of it?

`lab.kinetics`'s rate equation dn/dt = k_f(1-n) - k_r*n is, for constant
(k_f,k_r), exactly a single-pole linear relaxation with time constant
tau = 1/(k_f+k_r) (`kinetics.tau_exact`, stage-12-gated) and corner
frequency f_c = 1/(2*pi*tau) = (k_f+k_r)/(2*pi). This module reads that
pole against pinned temporal-CSF landmark frequencies (de Lange 1958;
Kelly 1961; Ferry-Porter law; Hecht & Verrijp 1933), separately for
photopic and scotopic regimes (PANEL.md's dual-regime requirement).

IDEALIZATION, stated up front and load-bearing (Panel Iteration 16 Phase 2,
QUANTUM OPTICS' attack, Red Team's adjudication -- see exp-039/NOTES.md):
comparing a ONE-SHOT relaxation's pole location to landmarks measured under
PERIODIC flicker is not a rigorous spectral-overlap calculation. It is a
legitimate order-of-magnitude proxy ONLY for the crude question "is this
transient's timescale entirely on one side of the eye's temporal cutoff" --
NOT a precise sub-threshold contrast claim. Every classification this
module produces is TIMING-ONLY and NECESSARY-NOT-SUFFICIENT for any scored
constraint-3/4 verdict -- T3-provisional; not a scored perceptual verdict.
The amplitude side (does the resulting contrast clear a Weber-contrast
threshold) needs the still-unbuilt n(t)->eps(omega,t)/sigma_abs(t) bridge
(Iteration 16 queued priority #3).

Second idealization: the classifier does not know whether a given host's
absorption CHANGE is spectrally broadband (achromatic -- the de Lange/Kelly
achromatic-luminance curves cited below apply as-is) or narrowband
(chromatic -- a materially lower-bandwidth TCSF would apply instead, per
Panel Iteration 16 Phase 2, PHOTONICS' attack). No host-specific spectral
data exists in this program to resolve that question this cycle; it is
disclosed, not silently assumed away -- see exp-039/NOTES.md Idealizations.

Trust gates: suite stage 13 (pole-identity vs `kinetics.tau_exact`,
classifier zone-ordering self-consistency, anchor-value regression) --
green before any classification is believed.
"""

import numpy as np

# --- pinned temporal-CSF landmarks -----------------------------------
# WebSearch-snippet-sourced (T18: WebFetch egress-blocked, primary-source
# curves not retrievable this cycle) -- literature-consensus landmark
# frequencies, NOT a digitized continuous curve. Every value here is
# order-of-magnitude, pending primary-source verification (T18's own
# established disclosure convention).

PHOTOPIC_LOW_CORNER_HZ = 2.0
"""Photopic (cone-driven, band-pass) TCSF low-frequency corner. Kelly 1961
(J. Opt. Soc. Am. 51:422, "Visual responses to time-dependent stimuli. I.");
de Lange 1958."""

PHOTOPIC_CFF_BAND_HZ = (50.0, 90.0)
"""Photopic critical flicker fusion (upper cutoff), canonical ~60 Hz.
Ferry-Porter law (CFF = a*log10(L) + b, slope a~8.5-20 Hz/log-unit,
saturating at high photopic L; slope per Tyler & Hamer 1990)."""

SCOTOPIC_LOW_CORNER_BAND_HZ = (0.8, 1.1)
"""Scotopic (rod-driven, low-pass) TCSF low-frequency corner, derived from
rod integration time-to-peak (~150-200 ms => corner ~1/(2*pi*0.15-0.2s)).
Panel Iteration 16 Phase 2, Red Team mandatory-fix #2: this is the
FORMULA-DERIVED value, adopted over the Phase-1 proposal's separate,
unreconciled "~2-3 Hz cited range" cell -- the two conflicted in the same
table row; this is the one carried into all gates and classifications
below. de Lange 1958 (bandpass->lowpass transition with falling luminance)."""

SCOTOPIC_CFF_BAND_HZ = (15.0, 25.0)
"""Scotopic critical flicker fusion -- rods cap far below cones' ~100 Hz.
Hecht & Verrijp 1933 (CFF vs. luminance, rod branch)."""


def corner_frequency(k_f, k_r):
    """f_c = (k_f + k_r) / (2*pi) [Hz] -- the single-pole corner frequency
    of the constant-(k_f,k_r) relaxation. Deliberately re-derived from
    (k_f, k_r) directly, NOT by calling `lab.kinetics.tau_exact` and
    inverting -- so suite stage 13's pole-identity gate is a genuine
    cross-check against independently-written code, not a tautology."""
    k_f = np.asarray(k_f, dtype=float)
    k_r = np.asarray(k_r, dtype=float)
    return (k_f + k_r) / (2.0 * np.pi)


def _as_band(x):
    """Normalize a scalar or (lo, hi) tuple into a (lo, hi) tuple."""
    if isinstance(x, tuple):
        return x
    return (x, x)


def _classify_point(f_c, low_corner, cff):
    if f_c < low_corner:
        return "sub_passband"
    elif f_c <= cff:
        return "in_passband"
    else:
        return "supra_cff"


def classify_zone_lowpass(f_c, cff):
    """TRUE low-pass classification: NO low-frequency exclusion. A genuine
    low-pass sensitivity curve (de Lange 1958's own bandpass->lowpass
    transition, cited in SCOTOPIC_LOW_CORNER_BAND_HZ's docstring) is
    MAXIMAL at/near DC, not excluded there -- unlike photopic's genuine
    bandpass dip. Returns 'in_passband' if f_c sits at or below cff (the
    whole low-frequency range including DC counts as sensitive), else
    'supra_cff'. Band-robust: accepts a scalar or (lo, hi) cff band;
    returns 'boundary_dependent' if the endpoints disagree.

    Panel Iteration 16 Phase 5, Red Team mandatory fix #1 (load-bearing,
    independently reconfirmed by the Director): `classify_zone` applies a
    BANDPASS decision structure (a low-frequency exclusion zone) to BOTH
    regimes, but the scotopic regime's own cited source describes it as
    low-pass -- a system with no such exclusion. Under this corrected
    model, both Host D and Host E's one-shot relaxation transients sit
    almost entirely below any plausible CFF (spectral power fraction
    ~87-96% for Host D, ~99% for Host E, Director's independent
    recomputation of Red Team's own check) -- i.e. BOTH classify
    `in_passband` (sensitive), and Host E -- the point exp-039's original
    scotopic reading called "favorable in both regimes" -- is if anything
    MORE concentrated in the sensitive near-DC zone than Host D, the
    OPPOSITE of the original bandpass-model reading. This is reported
    ALONGSIDE, not instead of, `classify_zone`'s bandpass reading (see
    `score_grid`) -- which model actually governs scotopic vision for a
    ONE-SHOT transient specifically (as opposed to periodic flicker, where
    the classic curve shapes were measured) is not resolved by this
    program and needs a primary-source check T18 currently blocks."""
    cff_lo, cff_hi = _as_band(cff)
    results = {("in_passband" if f_c <= c else "supra_cff") for c in (cff_lo, cff_hi)}
    if len(results) == 1:
        return results.pop()
    return "boundary_dependent"


def classify_zone(f_c, low_corner, cff):
    """Classify f_c against a (possibly banded) low_corner/cff pair as one
    of 'sub_passband' / 'in_passband' / 'supra_cff'.

    `low_corner` and `cff` may each be a scalar or a (lo, hi) uncertainty
    band. If the classification is IDENTICAL across all four combinations
    of band endpoints, that classification is returned -- ROBUST to the
    band's own uncertainty. If the four combinations disagree, this
    returns 'boundary_dependent' EXPLICITLY rather than silently picking
    one endpoint (Panel Iteration 16 Phase 2, Red Team mandatory-fix #1:
    pin the exact decision procedure in code, handling a genuine
    uncertainty band honestly instead of an unstated point-value choice)."""
    corner_lo, corner_hi = _as_band(low_corner)
    cff_lo, cff_hi = _as_band(cff)
    results = {
        _classify_point(f_c, c, k)
        for c in (corner_lo, corner_hi)
        for k in (cff_lo, cff_hi)
    }
    if len(results) == 1:
        return results.pop()
    return "boundary_dependent"


def score_grid(hosts, ratios, regime):
    """Apply corner_frequency + classify_zone across a host/ratio grid.

    hosts: dict or list of (name, k_r) pairs (s^-1).
    ratios: iterable of r = k_f/k_r values.
    regime: "photopic" or "scotopic".

    Returns a list of dicts: {host, r, k_f, k_r, f_c_hz, zone}.
    """
    if regime == "photopic":
        low_corner, cff = PHOTOPIC_LOW_CORNER_HZ, PHOTOPIC_CFF_BAND_HZ
    elif regime == "scotopic":
        low_corner, cff = SCOTOPIC_LOW_CORNER_BAND_HZ, SCOTOPIC_CFF_BAND_HZ
    else:
        raise ValueError(f"unknown regime {regime!r}")

    items = hosts.items() if hasattr(hosts, "items") else hosts
    rows = []
    for host, k_r in items:
        for r in ratios:
            k_f = r * k_r
            f_c = float(corner_frequency(k_f, k_r))
            zone = classify_zone(f_c, low_corner, cff)
            row = {
                "host": host, "r": r, "k_f": k_f, "k_r": k_r,
                "f_c_hz": f_c, "regime": regime, "zone": zone,
            }
            # Red Team mandatory fix #1 (Iteration 16 Phase 5): scotopic
            # rows also carry the true-low-pass alternative reading
            # alongside the bandpass one, since which model actually
            # applies is unresolved (see classify_zone_lowpass docstring).
            if regime == "scotopic":
                row["zone_lowpass_alt"] = classify_zone_lowpass(f_c, cff)
            rows.append(row)
    return rows
