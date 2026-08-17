"""
exp-039 — The T3 Temporal-CSF Screen. Panel Iteration 16.
==========================================================
Applies `lab.temporal_csf` to exp-038's own (k_f, k_r) host/ratio grid and
scores every pre-registered prediction (NOTES.md's Phase-3 synthesis)
against the measured classification. Zero FDTD calls -- this experiment's
own "run" is a frequency-domain post-hoc screen of numbers exp-038 already
produced, not a Maxwell-solver scene.

Run: python3 experiments/039-t3-temporal-csf-screen/run.py
"""
import json
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from lab import temporal_csf as tcsf

HERE = os.path.dirname(os.path.abspath(__file__))

# Identical to exp-038's own stage-12 grid (NOTES.md, Final parameter table).
HOSTS = {"A": 1e9, "B": 1e6, "C": 1e3, "D": 1e1, "E": 1e0}
RATIOS = [1e-9, 1e-5, 1e-3, 1e-1, 1.0]

def realizability_tier(host, r):
    """Identical to exp-038's own run.py::realizability_tier (NOTES.md's
    Realizability bound section restates, does not re-derive, this)."""
    if host == "E":
        return "UNOBTANIUM-WITH-PARAMETERS"
    if r >= 1.0:
        return "UNOBTANIUM-WITH-PARAMETERS"
    if r <= 1e-3:
        return "PUBLISHED" if host in ("A", "B") else "PLAUSIBLE"
    return "PLAUSIBLE"


def score_predictions(rows_photopic, rows_scotopic):
    """Check every P-EM-* prediction from NOTES.md against the measured
    rows. Returns a list of {id, claim, measured, verdict} dicts."""
    verdicts = []

    def find(rows, host, r):
        for row in rows:
            if row["host"] == host and row["r"] == r:
                return row
        raise KeyError((host, r))

    # P-EM-1 (pole-identity) is gated in the trust suite (stage 13), not
    # re-checked here -- this script only scores the science predictions.

    # P-EM-2: Host D f_c in [1.55, 3.25] Hz, monotonically increasing with r.
    d_fcs = [find(rows_photopic, "D", r)["f_c_hz"] for r in RATIOS]
    p2_band_ok = all(1.55 <= f <= 3.25 for f in d_fcs)
    p2_mono_ok = all(d_fcs[i] <= d_fcs[i + 1] for i in range(len(d_fcs) - 1))
    verdicts.append({
        "id": "P-EM-2", "claim": "Host D f_c in [1.55,3.25] Hz, monotonic in r",
        "measured": d_fcs, "verdict": "CONFIRMED" if (p2_band_ok and p2_mono_ok) else "REFUTED",
    })

    # P-EM-3: Host E f_c in [0.155, 0.325] Hz, monotonically increasing with r.
    e_fcs = [find(rows_photopic, "E", r)["f_c_hz"] for r in RATIOS]
    p3_band_ok = all(0.155 <= f <= 0.325 for f in e_fcs)
    p3_mono_ok = all(e_fcs[i] <= e_fcs[i + 1] for i in range(len(e_fcs) - 1))
    verdicts.append({
        "id": "P-EM-3", "claim": "Host E f_c in [0.155,0.325] Hz, monotonic in r",
        "measured": e_fcs, "verdict": "CONFIRMED" if (p3_band_ok and p3_mono_ok) else "REFUTED",
    })

    # P-EM-4 (photopic, T3-provisional): Host D r<=0.1 sub_passband, r=1
    # in_passband; all Host E sub_passband; no boundary_dependent anywhere.
    d_zones_photopic = [find(rows_photopic, "D", r)["zone"] for r in RATIOS]
    e_zones_photopic = [find(rows_photopic, "E", r)["zone"] for r in RATIOS]
    p4_d_ok = (d_zones_photopic[:4] == ["sub_passband"] * 4
               and d_zones_photopic[4] == "in_passband")
    p4_e_ok = all(z == "sub_passband" for z in e_zones_photopic)
    p4_no_boundary = "boundary_dependent" not in d_zones_photopic + e_zones_photopic
    verdicts.append({
        "id": "P-EM-4 [T3-provisional; not a scored perceptual verdict]",
        "claim": "photopic: Host D r<=0.1 sub_passband/r=1 in_passband, Host E always sub_passband",
        "measured": {"host_D_zones": d_zones_photopic, "host_E_zones": e_zones_photopic},
        "verdict": "CONFIRMED" if (p4_d_ok and p4_e_ok and p4_no_boundary) else "REFUTED",
    })

    # P-EM-5 (scotopic, T3-provisional, CORRECTED at Phase 3, then FLAGGED
    # at Phase 5): Host D always in_passband, Host E always sub_passband,
    # no boundary_dependent -- under classify_zone's BANDPASS model.
    #
    # Iteration 16 Phase 5, Red Team mandatory fix #1 (load-bearing,
    # independently reconfirmed by the Director): classify_zone applies a
    # bandpass (low-frequency-exclusion) decision structure to the
    # scotopic regime, but that regime's own cited source (de Lange 1958,
    # see temporal_csf.py's SCOTOPIC_LOW_CORNER_BAND_HZ docstring)
    # describes it as LOW-PASS -- a shape with NO low-frequency exclusion,
    # sensitivity maximal near DC. Under the TRUE low-pass alternative
    # (classify_zone_lowpass, no low_corner), BOTH hosts classify
    # in_passband, and Host E -- read as "favorable in both regimes" under
    # the bandpass model -- has MORE of its spectral power concentrated in
    # the sensitive near-DC zone than Host D (Director's independent
    # recomputation: Host D ~87-96% of spectral power below CFF, Host E
    # ~99% below CFF, under the pure-lowpass reading) -- the OPPOSITE
    # direction from the bandpass model's "Host E is the good one" story.
    # BOTH readings are reported below; NEITHER is treated as the settled
    # answer -- which model actually governs a ONE-SHOT scotopic transient
    # is unresolved (T18 blocks the primary-source check that would decide
    # it).
    d_zones_scotopic = [find(rows_scotopic, "D", r)["zone"] for r in RATIOS]
    e_zones_scotopic = [find(rows_scotopic, "E", r)["zone"] for r in RATIOS]
    d_zones_scotopic_lp = [find(rows_scotopic, "D", r)["zone_lowpass_alt"] for r in RATIOS]
    e_zones_scotopic_lp = [find(rows_scotopic, "E", r)["zone_lowpass_alt"] for r in RATIOS]
    p5_d_ok = all(z == "in_passband" for z in d_zones_scotopic)
    p5_e_ok = all(z == "sub_passband" for z in e_zones_scotopic)
    p5_no_boundary = "boundary_dependent" not in d_zones_scotopic + e_zones_scotopic
    bandpass_confirmed = p5_d_ok and p5_e_ok and p5_no_boundary
    verdicts.append({
        "id": "P-EM-5 [T3-provisional; not a scored perceptual verdict; "
              "CONTESTED-MODEL -- see model_dependence below]",
        "claim": "scotopic, BANDPASS model (classify_zone, as originally run): "
                 "Host D always in_passband, Host E always sub_passband",
        "measured": {"host_D_zones": d_zones_scotopic, "host_E_zones": e_zones_scotopic},
        "verdict": "CONFIRMED-UNDER-BANDPASS-MODEL-ONLY" if bandpass_confirmed else "REFUTED",
        "model_dependence": {
            "bandpass_model_reading": {
                "host_D": d_zones_scotopic, "host_E": e_zones_scotopic,
                "note": "the model originally run; requires a low-frequency exclusion "
                        "zone that this regime's own cited source (de Lange 1958) "
                        "describes as NOT PRESENT (scotopic TCSF is low-pass, not "
                        "band-pass) -- Red Team mandatory fix #1, Iteration 16 Phase 5.",
            },
            "true_lowpass_model_reading": {
                "host_D": d_zones_scotopic_lp, "host_E": e_zones_scotopic_lp,
                "note": "the alternative consistent with this regime's own cited "
                        "source: no low-frequency exclusion. Under this model BOTH "
                        "hosts classify in_passband, and Host E is MORE concentrated "
                        "in the sensitive near-DC zone than Host D (~99% vs ~87-96% "
                        "of spectral power below CFF) -- the OPPOSITE of the "
                        "bandpass reading's 'Host E is favorable' direction.",
            },
            "unresolved": "which model actually governs a ONE-SHOT (non-periodic) "
                           "scotopic transient is NOT decided by this experiment -- "
                           "needs a primary-source check T18 (WebFetch egress block) "
                           "currently prevents.",
        },
        "spectral_overlap_asymmetry_note": (
            "Iteration 16 Phase 5, QUANTUM OPTICS: under the bandpass model, Host D's "
            "in_passband label captures only ~55-76% of its actual one-shot spectral "
            "power inside the nominal passband (24-45% falls outside), while Host E's "
            "sub_passband label is well-supported (~76-91% of power genuinely outside "
            "the passband). The two hosts' bandpass-model classifications are not "
            "equally trustworthy in degree, independent of the model-choice question "
            "above."
        ),
        "realizability_caveat": {
            "host_D_r1": realizability_tier("D", 1.0),
            "host_E_all": [realizability_tier("E", r) for r in RATIOS],
            "note": "6 of the 10 P-EM-5 points (Host D r=1 + all 5 Host E points) "
                    "are independently UNOBTANIUM-WITH-PARAMETERS on the realizability "
                    "axis alone (Red Team fix #5/#6, Director-reconfirmed) -- this "
                    "timing-screen finding describes a mechanism class with zero "
                    "demonstrated realizable instances in this program's own grid, "
                    "under EITHER model.",
        },
    })

    # P-EM-6 (sanity, T3-provisional): Hosts A/B/C always supra_cff, both
    # regimes.
    abc_zones = []
    for host in ("A", "B", "C"):
        for regime_rows in (rows_photopic, rows_scotopic):
            for r in RATIOS:
                abc_zones.append(find(regime_rows, host, r)["zone"])
    p6_ok = all(z == "supra_cff" for z in abc_zones)
    verdicts.append({
        "id": "P-EM-6 [T3-provisional; not a scored perceptual verdict]",
        "claim": "Hosts A/B/C always supra_cff, both regimes (sanity check)",
        "measured": {"n_points": len(abc_zones), "n_supra_cff": sum(1 for z in abc_zones if z == "supra_cff")},
        "verdict": "CONFIRMED" if p6_ok else "REFUTED",
    })

    return verdicts


def main():
    t0 = time.time()
    rows_photopic = tcsf.score_grid(HOSTS, RATIOS, "photopic")
    rows_scotopic = tcsf.score_grid(HOSTS, RATIOS, "scotopic")

    verdicts = score_predictions(rows_photopic, rows_scotopic)

    out = {
        "experiment": "exp-039-t3-temporal-csf-screen",
        "panel_iteration": 16,
        "lead": "ELECTROMAGNETISM",
        "landmarks": {
            "photopic": {"low_corner_hz": tcsf.PHOTOPIC_LOW_CORNER_HZ,
                         "cff_hz_band": tcsf.PHOTOPIC_CFF_BAND_HZ},
            "scotopic": {"low_corner_hz_band": tcsf.SCOTOPIC_LOW_CORNER_BAND_HZ,
                         "cff_hz_band": tcsf.SCOTOPIC_CFF_BAND_HZ},
        },
        "rows_photopic": rows_photopic,
        "rows_scotopic": rows_scotopic,
        "predictions": verdicts,
        "elapsed_s": time.time() - t0,
    }

    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=2)

    n_confirmed = sum(1 for v in verdicts if v["verdict"] == "CONFIRMED")
    print(f"exp-039: {n_confirmed}/{len(verdicts)} predictions CONFIRMED")
    for v in verdicts:
        print(f"  [{v['verdict']}] {v['id']}: {v['claim']}")
    print(f"elapsed: {out['elapsed_s']:.2f}s")


if __name__ == "__main__":
    main()
