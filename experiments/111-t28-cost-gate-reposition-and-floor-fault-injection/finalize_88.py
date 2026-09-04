"""exp-111 -- Panel Iteration 88: Phase-5 Red Team final-audit fix (mandatory
fix 5's own genuine completion). Loads the four real `*_output.json` control
files this cycle produced, calls `build_predictions_text_88()`/
`build_result_text_88()` from `predictions_result_88.py` with them (the
latter supplied the real `wall_time_source` string, matching what actually
produced `results.json["result_text"]` -- independently confirmed by three
of six blind Phase-5 reviews, and re-confirmed here), asserts
`DISCLAIMER_88 in` both (now enforced INSIDE both functions themselves, see
`predictions_result_88.py`'s own Phase-5 fix), and verifies byte-for-byte
against the already-committed `results.json`.

This is the missing "actually-invoked, re-runnable script path" four of six
blind Phase-5 reviews (MATERIALS, PHOTONICS, VISION, THERMODYNAMICS) found
absent -- before this fix, `results.json["result_text"]` was genuinely
correct content but reproducible only via an ad hoc, uncaptured invocation
this session never committed as code (THERMODYNAMICS' own Phase-5 finding,
independently re-confirmed by this audit). Mirrors exp-110's own
`finalize.py` naming/role precedent (LOGBOOK Iteration 87).

Zero Sim.run() calls. Zero new FDTD. Reads already-committed JSON only.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "experiments", "110-t28-item-i-local-norm-and-controls"))

from predictions_result_88 import (  # noqa: E402
    build_predictions_text_88,
    build_result_text_88,
    DISCLAIMER_88,
)

WALL_TIME_SOURCE = (
    "zero new FDTD this cycle; all figures from exp-110's own "
    "already-committed results.json plus this cycle's own synthetic/formula "
    "controls"
)


def load(name):
    with open(os.path.join(HERE, name)) as f:
        return json.load(f)


def main():
    fi_results = load("floor_fault_injection_control_output.json")
    gate_results = load("gate_reposition_control_output.json")
    formula_results = load("cost_gate_formula_control_output.json")
    cpl_table_rows = load("cpl_cost_table_output.json")

    predictions_text = build_predictions_text_88()
    assert DISCLAIMER_88 in predictions_text, "R23: disclaimer missing from Predictions block"

    result_text = build_result_text_88(fi_results, gate_results, formula_results,
                                        cpl_table_rows, wall_time_source=WALL_TIME_SOURCE)
    assert DISCLAIMER_88 in result_text, "R23: disclaimer missing from Result block"

    with open(os.path.join(HERE, "results.json")) as f:
        frozen = json.load(f)

    # VISION's own Phase-5 finding (independently re-confirmed here): the
    # committed `results.json["predictions_text"]`/`predictions_text_88.txt`
    # carry one harmless extra trailing "\n" versus the bare function
    # return -- `print(predictions_text)` under `--predictions-only` (see
    # this file's own __main__ block) appends it; not a content defect.
    # `result_text` was never round-tripped through `print()` the same way,
    # so it compares exactly with no adjustment.
    predictions_match = (predictions_text + "\n") == frozen["predictions_text"]
    result_match = result_text == frozen["result_text"]

    print(f"predictions_text byte-exact match against results.json "
          f"(modulo one harmless print()-appended trailing newline, VISION's "
          f"own Phase-5 finding): {predictions_match}")
    print(f"result_text byte-exact match against results.json: {result_match}")
    print(f"DISCLAIMER_88 in predictions_text: {DISCLAIMER_88 in predictions_text}")
    print(f"DISCLAIMER_88 in result_text: {DISCLAIMER_88 in result_text}")

    all_ok = predictions_match and result_match
    print(f"\nALL CHECKS PASS: {all_ok}")
    assert all_ok, ("finalize_88: build_predictions_text_88()/build_result_text_88() do not "
                     "reproduce the committed results.json text fields")
    return 0


if __name__ == "__main__":
    sys.exit(main())
