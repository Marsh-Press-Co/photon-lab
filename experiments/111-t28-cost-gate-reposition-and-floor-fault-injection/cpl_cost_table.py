"""exp-111 -- Panel Iteration 88: regenerates (does not hand-type,
mandatory-fix 4 of phase2_redteam_audit.md Sec 5 / R4 discipline) the
item-3 (PHOTONICS' cpl-refinement floor spot-check) deferral cost table
from exp-110's own real committed r=156/r=312 wall-time data, using the
proposal's own disclosed cpl_ratio**3 analogy (a disclosed estimate, not a
re-derived law -- distinct from the KAPPA_COST_EXPONENT re-derivation,
which concerns kappa=r/R_BASE, not cpl).

MATERIALS' own Phase-2 finding (adopted by Red Team, mandatory fix 4):
the proposal's own hand-typed cpl=30 "Both r" cell read "~6.5h" -- actually
the r=312-alone column's own figure, misplaced. Running this script
produces the correct table directly from arithmetic, checkable by anyone
re-running it.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

T156 = 752.2232966423035  # exp-110's own committed r=156 3-scene total wall time
T312 = 6938.207038640976  # exp-110's own committed r=312 3-scene total wall time
CPL_BASE = 20  # CPL_600 in exp-110's own run.py

CPL_TARGETS = (25, 30)


def table():
    rows = []
    for cpl in CPL_TARGETS:
        ratio = cpl / CPL_BASE
        t156_new = T156 * (ratio ** 3)
        t312_new = T312 * (ratio ** 3)
        both = t156_new + t312_new
        rows.append(dict(cpl=cpl, ratio=ratio,
                          r156_s=t156_new, r156_h=t156_new / 3600.0,
                          r312_s=t312_new, r312_h=t312_new / 3600.0,
                          both_s=both, both_h=both / 3600.0))
    return rows


if __name__ == "__main__":
    rows = table()
    for row in rows:
        print(f"cpl={row['cpl']} ratio={row['ratio']:.2f}x  "
              f"r156: {row['r156_s']:.2f}s ({row['r156_h']:.4f}h)  "
              f"r312: {row['r312_s']:.2f}s ({row['r312_h']:.4f}h)  "
              f"both: {row['both_s']:.2f}s ({row['both_h']:.4f}h)")
    out_path = os.path.join(HERE, "cpl_cost_table_output.json")
    with open(out_path, "w") as f:
        json.dump(rows, f, indent=2)
    print(f"Written: {out_path}")
