"""
experiments/086-t28-free-period-boundary-fix-rescore/phase4_null_calibration_rerun.py
============================================================================
Panel Iteration 63 (exp-086), Phase 4 continued -- mandatory fix 2
(Red Team's Phase-2 audit, adopted in full by phase3_synthesis.md).

SCOPE DISCLOSURE (deviation from the frozen spec, disclosed here and in
NOTES.md, not silently absorbed): Red Team's mandatory fix 2 called for
the FULL 60,001-call `null_calibration_appendix` re-run. A timing probe
(500 pure-noise trials, measured 82.2s -> ~0.164s/call) puts the full
60,001-call run at ~2.7 hours wall-clock -- impractical for one shift.
This script instead runs `n_trials=3000` per leg (9,001 calls total: 3000
pure-noise + 3000 bootstrap-iid + 3000 bootstrap-circular + 1 `best` call),
matching Red Team's OWN precedent sample size for its bounded probe (it
also used exactly 3,000 trials for the pure-noise leg). This is a
disclosed, bounded sample, NOT a claim of exhaustive 60,001-call coverage
-- a full-scale run is queued (see NOTES.md Next / LOGBOOK entry) as a
Tier-2 standing item, the same status every other T28 "run at full scale"
item on the board carries.
"""

import json
import os
import sys
import time
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


import numpy as np

pad = _load(os.path.join(ROOT, "experiments", "077-t28-pad-round-trip-echo-model",
                          "pad_round_trip_model.py"), "_exp086_pad_null")

EXP077_DIR = os.path.join(ROOT, "experiments", "077-t28-pad-round-trip-echo-model")
d = json.load(open(os.path.join(EXP077_DIR, "pad_round_trip_results.json")))
thetas = np.array(d["thetas"])

N_TRIALS = 3000
SEED = 7

out = {}
# Only pair_pad: exp-077's own committed `null_calibration_appendix` is a
# single top-level key, computed once against `real_delta_pad` -- not
# per-pair. Re-running an appendix for pair_absorb40 would be new scope
# beyond what this audit is checking (was the CITED appendix corrupted?),
# so it is intentionally not done here.
for label, key in [("pair_pad", "real_delta_pad")]:
    real_delta = np.array(d[key])
    p_star_real = d[f"test_a_{label}"]["real"]["chosen"]["p_star_deg"]
    print(f"\n=== {label} (n_trials={N_TRIALS}, corrected quiet function) ===")
    t0 = time.time()
    res = pad.null_calibration_appendix(thetas, real_delta, p_star_real,
                                         n_trials=N_TRIALS, seed=SEED)
    elapsed = time.time() - t0
    print(f"    elapsed = {elapsed:.1f}s")
    print(f"    pure_noise_null: {json.dumps(res['pure_noise_null'], indent=6)}")
    print(f"    bootstrap iid recovered_mean_p_star_deg="
          f"{res['bootstrap_recovery']['iid']['recovered_mean_p_star_deg']:.4f} "
          f"std={res['bootstrap_recovery']['iid']['recovered_std_p_star_deg']:.4f}")
    print(f"    bootstrap circular recovered_mean_p_star_deg="
          f"{res['bootstrap_recovery']['circular_shift']['recovered_mean_p_star_deg']:.4f} "
          f"std={res['bootstrap_recovery']['circular_shift']['recovered_std_p_star_deg']:.4f}")
    out[label] = dict(n_trials=N_TRIALS, seed=SEED, elapsed_s=elapsed,
                       corrected=res, p_star_real_deg=p_star_real)

out_path = os.path.join(HERE, "phase4_null_calibration_rerun_results.json")
json.dump(out, open(out_path, "w"), indent=2)
print(f"\nwritten to {out_path}")
