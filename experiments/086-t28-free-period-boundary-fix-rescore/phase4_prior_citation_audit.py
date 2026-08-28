"""
experiments/086-t28-free-period-boundary-fix-rescore/phase4_prior_citation_audit.py
============================================================================
Panel Iteration 63 (exp-086), Phase 4 -- mandatory fix docket item 3
(bounded audit of whether the R11 boundary-pinning defect silently
affected any OTHER prior T28 citation beyond the two already-known-inert
instances, exp-078/exp-079, that exp-085's own Phase-5 audit found).

Scope: `free_period_with_widening`/`_quiet` were introduced in exp-077 (R11
note, LOGBOOK.md); experiments 069-076 predate the function and are out of
scope by construction (grep-confirmed: zero `at_boundary` occurrences in
any committed JSON in that range). This script scans every committed JSON
in experiments 077-085 for a persisted per-stage list (any array of dicts
sharing a `window`+`at_boundary` shape, in the narrow[1,4]/wide[1,15]/
widest[1,60] or the 2-stage quiet order) and flags any case where EVERY
stage in the list is `at_boundary=True` -- the exact shape the OLD (buggy)
code would have silently mis-resolved to the FIRST (narrowest) stage's own
value instead of the last (widest)."""

import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

STAGE_KEYS = {"window", "at_boundary"}


def find_stage_lists(obj, path=""):
    """Yield (path, list_of_dicts) for every list whose elements are all
    dicts containing at least 'window' and 'at_boundary'."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from find_stage_lists(v, f"{path}/{k}")
    elif isinstance(obj, list):
        if obj and all(isinstance(e, dict) and STAGE_KEYS.issubset(e.keys()) for e in obj):
            yield (path, obj)
        else:
            for i, e in enumerate(obj):
                yield from find_stage_lists(e, f"{path}[{i}]")


def main():
    files = sorted(glob.glob(os.path.join(ROOT, "experiments", "0{7,8}[0-9]-*", "*.json")))
    # glob doesn't support brace expansion in Python's glob module; do it manually.
    files = sorted(set(
        glob.glob(os.path.join(ROOT, "experiments", "07[7-9]-*", "*.json")) +
        glob.glob(os.path.join(ROOT, "experiments", "08[0-5]-*", "*.json"))
    ))
    print(f"Scanning {len(files)} committed JSON files (experiments 077-085)")
    findings = []
    for f in files:
        try:
            d = json.load(open(f))
        except Exception as e:
            print(f"  [SKIP] {f}: {e}")
            continue
        for path, stages in find_stage_lists(d):
            if len(stages) >= 1 and all(s.get("at_boundary") is True for s in stages):
                rel = os.path.relpath(f, ROOT)
                findings.append(dict(file=rel, path=path,
                                      n_stages=len(stages),
                                      first_stage=stages[0],
                                      last_stage=stages[-1]))
    print(f"\n{len(findings)} all-stages-boundary occurrences found (candidate silent-fallback sites):\n")
    for finding in findings:
        print(f"  {finding['file']}{finding['path']}  ({finding['n_stages']} stages)")
        print(f"    first(narrowest, OLD BUGGY RETURN): window={finding['first_stage'].get('window')} "
              f"p_star_deg={finding['first_stage'].get('p_star_deg')} r_squared={finding['first_stage'].get('r_squared')}")
        print(f"    last (widest, CORRECTED RETURN):    window={finding['last_stage'].get('window')} "
              f"p_star_deg={finding['last_stage'].get('p_star_deg')} r_squared={finding['last_stage'].get('r_squared')}")

    out = dict(files_scanned=len(files), all_stage_boundary_occurrences=findings)
    out_path = os.path.join(HERE, "phase4_prior_citation_audit_results.json")
    json.dump(out, open(out_path, "w"), indent=2)
    print(f"\nwritten to {out_path}")


if __name__ == "__main__":
    main()
