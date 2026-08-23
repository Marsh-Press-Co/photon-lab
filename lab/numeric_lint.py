"""lab/numeric_lint.py — the numeric/derivation-consistency-check tool.
=======================================================================
Panel Iteration 40, Director's mandatory zero-cost rider (declined by
ELECTROMAGNETISM at Iteration 39 Phase 1 as charter-mismatched scope for an
EM-led cycle, flagged rather than decided unilaterally; Red Team's
Iteration-39 Phase-2 audit re-filed it with a named owner — the Director, at
Iteration 40, regardless of that cycle's lead seat, per Red Team's
Iteration-38 mandatory-fix item 6). Widened per EM's own Iteration-39 Phase-5
recommendation: catch not just a NUMBER drifting unreconciled across sibling
files, but the SAME derivation methodology applied two inconsistent ways
within one document — exp-062's own EM-6/EM-7 R-vs-T drop (a live, ready
regression test case, closed by Iteration 39 Phase-5 mandatory fix 5) is the
tool's own self-test.

RELATIONSHIP TO lab/caveat_lint.py: siblings, not the same tool.
caveat_lint.py answers "did a documented caveat's exact phrase propagate to
every site a Phase-5 docket named" — an unconditional per-site check. This
tool answers two different questions, neither of which caveat_lint.py can
express:

  1. NUMERIC DRIFT — does a specific number, cited at N sibling sites
     (LOGBOOK.md, PLAN.md, NOTES.md, phase*.md, SESSION_LOG.md), read the
     SAME value everywhere, or has an edit silently drifted one site without
     the others?  (Red Team's Iteration-38 mandatory-fix item 6's original
     framing: "a NUMBER drifting unreconciled across sibling files.")

  2. DERIVATION CONSISTENCY — when a document applies ONE formula/convention
     in two places, does it apply the SAME variant of that formula
     consistently, or does a condition that should trigger a different
     variant (e.g. "this figure is reflectance-based, so the physically
     correct treatment halves the exponent") go unflagged at one site while
     correctly handled at another? This is a CONDITIONAL check: "wherever
     condition Z is stated, disclosure/treatment Y must appear nearby" — not
     "does phrase X exist everywhere" (that's caveat_lint.py's job) and not
     "is number X the same everywhere" (that's numeric-drift, above). This is
     exactly the shape of exp-062's EM-6/EM-7 defect: the "R above is a
     reflectance figure ⇒ the physically consistent treatment halves the
     exponent" condition held for both EM-6 and EM-7, but neither disclosed
     it at Phase 4 — caught only by two independent Phase-5 reviews.

WHAT THIS IS NOT (same disclaimer as caveat_lint.py, for the same reasons):
a physics gate. Pure text/regex scanning, zero FDTD, zero numpy, zero
network — not wired into lab/validation/run_all.py, for identical reasoning
to caveat_lint.py's own (see its module docstring): a "does this document
apply its own stated methodology consistently" check is a documentation-
completeness assertion, not an engine-physics measurement, and belongs in
its own registry curated by the Director per mandatory-fix docket, not
auto-loaded by the trust suite.

REGISTRY. `lab/numeric_lint_config.json` (checked in, hand-curated), a JSON
list of entries. Two entry kinds, discriminated by "kind":

  {"kind": "numeric_drift",
   "id": ..., "description": ..., "source": ...,
   "sites": [{"path": ..., "pattern": <regex, ONE capture group>}, ...],
   "tolerance_rel": <float, default 1e-9>}

    Each site's pattern is matched (first hit) against the file's own
    whitespace-normalized text; the captured group is parsed as a float
    (after stripping thousands separators). All sites' values must agree
    pairwise within tolerance_rel of the FIRST successfully-matched site's
    value, else FAIL.

  {"kind": "derivation_consistency",
   "id": ..., "description": ..., "source": ...,
   "site": <path>,
   "window_patterns": [<regex, multiline, matches a section-start line>],
   "basis_pattern": <regex — condition that, if present in the window,
                     requires "requires_pattern" to ALSO be present>,
   "requires_pattern": <regex — the disclosure/correct-treatment marker>,
   "window_chars": <int, default 4000, hard cap on window length>}

    For each match of ANY window_pattern (scanning the RAW file, multiline),
    the window runs from the match start to the next markdown heading line
    (`^#{1,6}\\s`) or `^---\\s*$` or end-of-file, capped at window_chars.
    Within that window (whitespace-normalized before matching), IF
    basis_pattern matches, THEN requires_pattern MUST also match — else
    FAIL. If basis_pattern does not match, the window is not applicable
    (skipped, reported as N/A, never gates the exit code).

USAGE (same conventions as caveat_lint.py):

  python3 lab/numeric_lint.py                        # whole registry
  python3 lab/numeric_lint.py --only <id>             # one entry
  python3 lab/numeric_lint.py --selftest              # replay the exp-062
                                                       # EM-6/EM-7 R-vs-T
                                                       # near-miss against
                                                       # real git history

Exit code: 0 iff every check in scope passes (numeric_drift: all sites
agree within tolerance; derivation_consistency: every basis-triggered
window carries its required disclosure). N/A windows/entries never fail.
"""

import argparse
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, ".."))
DEFAULT_CONFIG = os.path.join(HERE, "numeric_lint_config.json")

_WS_RE = re.compile(r"\s+")
_HEADING_RE = re.compile(r"^#{1,6}\s|^---\s*$", re.MULTILINE)


def _normalize(text):
    return _WS_RE.sub(" ", text)


def _read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return None


def _read_git(rev, relpath):
    try:
        out = subprocess.run(
            ["git", "show", f"{rev}:{relpath}"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=False,
        )
    except FileNotFoundError:
        return None
    if out.returncode != 0:
        return None
    return out.stdout


def _parse_number(raw):
    cleaned = raw.replace(",", "").strip()
    return float(cleaned)


# ---------------------------------------------------------------- numeric_drift

def check_numeric_drift(entry, repo_root=REPO_ROOT):
    tol = entry.get("tolerance_rel", 1e-9)
    readings = []  # (path, value_or_None, raw_or_reason)
    for site in entry["sites"]:
        path = site["path"]
        text = _read(os.path.join(repo_root, path))
        if text is None:
            readings.append((path, None, "FILE NOT FOUND"))
            continue
        norm = _normalize(text)
        m = re.search(site["pattern"], norm)
        if m is None:
            readings.append((path, None, "pattern not found"))
            continue
        try:
            val = _parse_number(m.group(1))
        except (ValueError, IndexError):
            readings.append((path, None, f"could not parse {m.group(0)!r}"))
            continue
        readings.append((path, val, m.group(0)))

    found = [(p, v, r) for (p, v, r) in readings if v is not None]
    ok = True
    ref = found[0][1] if found else None
    for path, val, raw in readings:
        if val is None:
            ok = False
            continue
        if ref is not None and ref != 0:
            rel = abs(val - ref) / abs(ref)
        elif ref is not None:
            rel = abs(val - ref)
        else:
            rel = 0.0
        if rel > tol:
            ok = False

    return {"id": entry["id"], "kind": "numeric_drift", "readings": readings,
            "ref": ref, "tolerance_rel": tol, "ok": ok}


def _print_numeric_drift(result, entry):
    print(f"\n[{result['id']}]  {entry.get('description', '')}")
    if entry.get("source"):
        print(f"  source: {entry['source']}")
    ref = result["ref"]
    for path, val, raw in result["readings"]:
        if val is None:
            print(f"  FAIL  {path}   ({raw})")
            continue
        if ref is not None and ref != 0:
            rel = abs(val - ref) / abs(ref)
        elif ref is not None:
            rel = abs(val - ref)
        else:
            rel = 0.0
        status = "PASS" if rel <= result["tolerance_rel"] else "FAIL"
        print(f"  {status}  {path}   (matched: {raw!r} -> {val}"
              f"{'' if ref is None else f', rel dev from ref={rel:.2e}'})")
    return result["ok"]


# ----------------------------------------------------------- derivation_consistency

def _iter_windows(text, window_patterns, window_chars):
    anchors = []
    for pat in window_patterns:
        for m in re.finditer(pat, text, re.MULTILINE):
            anchors.append(m.start())
    anchors = sorted(set(anchors))
    windows = []
    for start in anchors:
        rest = text[start:]
        first_nl = rest.find("\n")
        search_from = first_nl + 1 if first_nl != -1 else len(rest)
        next_heading = None
        for hm in _HEADING_RE.finditer(rest[search_from:]):  # skip the anchor's own heading line
            next_heading = hm.start() + search_from
            break
        end = len(rest) if next_heading is None else next_heading
        end = min(end, window_chars)
        windows.append((start, text[start:start + end]))
    return windows


def check_derivation_consistency(entry, repo_root=REPO_ROOT):
    path = entry["site"]
    text = _read(os.path.join(repo_root, path))
    if text is None:
        return {"id": entry["id"], "kind": "derivation_consistency",
                "site": path, "ok": False, "windows": [],
                "error": "FILE NOT FOUND"}
    window_chars = entry.get("window_chars", 4000)
    windows = _iter_windows(text, entry["window_patterns"], window_chars)
    basis_pat = entry["basis_pattern"]
    req_pat = entry["requires_pattern"]
    results = []
    ok = True
    for start, raw_window in windows:
        norm = _normalize(raw_window)
        heading_line = raw_window.splitlines()[0].strip() if raw_window else ""
        basis_hit = re.search(basis_pat, norm, re.IGNORECASE)
        if basis_hit is None:
            results.append((heading_line, "N/A", None))
            continue
        req_hit = re.search(req_pat, norm, re.IGNORECASE)
        if req_hit is None:
            ok = False
            results.append((heading_line, "FAIL", None))
        else:
            results.append((heading_line, "PASS", req_hit.group(0)))
    return {"id": entry["id"], "kind": "derivation_consistency", "site": path,
            "ok": ok, "windows": results}


def _print_derivation_consistency(result, entry):
    print(f"\n[{result['id']}]  {entry.get('description', '')}")
    if entry.get("source"):
        print(f"  source: {entry['source']}")
    if result.get("error"):
        print(f"  FAIL  {result['site']}   ({result['error']})")
        return False
    if not result["windows"]:
        print(f"  WARN  {result['site']}   (no window_patterns matched -- "
              f"nothing to check; verify window_patterns still match this "
              f"document's headings)")
        return True
    for heading, status, matched in result["windows"]:
        if status == "N/A":
            print(f"  N/A   {result['site']} :: {heading!r}   "
                  f"(basis condition not present in this window)")
        elif status == "PASS":
            print(f"  PASS  {result['site']} :: {heading!r}   "
                  f"(basis present, required disclosure matched: {matched!r})")
        else:
            print(f"  FAIL  {result['site']} :: {heading!r}   "
                  f"(basis condition present, required disclosure MISSING)")
    return result["ok"]


# --------------------------------------------------------------------- driver

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _run_entry(entry):
    kind = entry.get("kind")
    if kind == "numeric_drift":
        result = check_numeric_drift(entry)
        return _print_numeric_drift(result, entry)
    if kind == "derivation_consistency":
        result = check_derivation_consistency(entry)
        return _print_derivation_consistency(result, entry)
    print(f"\n[{entry.get('id', '?')}]  unknown kind {kind!r} -- skipped", file=sys.stderr)
    return False


def run_registry(config_path, only=None):
    entries = load_config(config_path)
    if only:
        entries = [e for e in entries if e["id"] == only]
        if not entries:
            print(f"No entry with id={only!r} in {config_path}", file=sys.stderr)
            return 2
    all_ok = True
    for entry in entries:
        ok = _run_entry(entry)
        all_ok = all_ok and ok
    print(f"\n{len(entries)} entry(ies) checked -- "
          f"{'all PASS' if all_ok else 'at least one FAIL'}.")
    return 0 if all_ok else 1


def run_selftest():
    """Retroactive validation against a REAL historical near-miss: exp-062's
    own EM-6/EM-7 R-vs-T disclosure gap (Iteration 39 Phase-5 mandatory fix
    5) -- independently caught by two blind Phase-5 reviews (PHOTONICS, EM)
    after Phase 4 shipped both sections silently applying the undivided
    tau=OD*ln10 formula to figures both sections' own query citations state
    are REFLECTANCE readings, without the halving Section 4.2's own R-vs-T
    analysis says a reflectance basis requires.

    Pre-fix commit: 4fb7f95 (Phase 4 -- phase4_results.md as first
    committed, EM-6/EM-7 sections present, R-vs-T disclosure absent).
    Post-fix commit: 967a726 (Phase 5 mandatory fixes 1,5,6,7,10 -- the
    R-vs-T disclosure paragraph added to both EM-6 and EM-7).

    PREDICTION (committed before running this selftest): both windows
    apply the undivided formula to an R=<percent>-labeled figure in BOTH
    revisions (the trigger condition -- "this section computes alpha from
    a reflectance-percent reading" -- is present in the calculation itself,
    pre-fix and post-fix alike). What differs is whether the window ALSO
    discloses the reflectance basis and its required halving treatment:
      - at 4fb7f95 (pre-fix): FAIL at both EM-6 and EM-7 windows (the
        R=<percent> figure is fed straight into the alpha calculation with
        no "reflectance figure" / halving disclosure anywhere in the
        window)
      - at 967a726 (post-fix, == current HEAD content): PASS at both (the
        mandatory-fix paragraph adds the disclosure to the same window)
    This demonstrates the tool would have caught the gap at Phase 4, before
    two independent Phase-5 reviews had to catch it by hand.
    """
    relpath = "experiments/062-thin-film-interference-and-near-field-coupling-bound/phase4_results.md"
    entry = {
        "id": "selftest-exp062-em6-em7-r-vs-t",
        "description": (
            "Historical replay: do EM-6/EM-7's own windows in "
            "phase4_results.md disclose the reflectance-basis-requires-"
            "halving condition where the undivided formula is actually "
            "applied? Iteration 39 Phase-5 mandatory fix 5."
        ),
        "site": relpath,
        "window_patterns": [r"^## EM-6", r"^## EM-7"],
        "basis_pattern": r"R\s*[=≈<]\s*[\d.]+%",
        "requires_pattern": r"reflectance\)?\s*figure|halv(ed|ing)|"
                             r"(no|without)\s+(the\s+)?(÷|/)?\s*2\s*correction",
        "window_chars": 3000,
    }
    print("Self-test: replaying Iteration-39's own exp-062 EM-6/EM-7 "
          "R-vs-T-disclosure Checkpoint-adjacent finding against two real "
          "git revisions.\n")

    all_ok = True
    for label, rev, expect_pass in (
        ("PRE-FIX  (4fb7f95, Phase 4, before the mandatory-fix docket)", "4fb7f95", False),
        ("POST-FIX (967a726, Phase 5, same-shift fix)", "967a726", True),
    ):
        text = _read_git(rev, relpath)
        if text is None:
            print(f"  [{rev}] could not read {relpath} from git history "
                  f"(shallow clone / rev not present) -- skipping this leg.")
            continue
        window_chars = entry["window_chars"]
        windows = _iter_windows(text, entry["window_patterns"], window_chars)
        got_pass = True
        details = []
        for start, raw_window in windows:
            norm = _normalize(raw_window)
            heading = raw_window.splitlines()[0].strip() if raw_window else ""
            if re.search(entry["basis_pattern"], norm, re.IGNORECASE) is None:
                details.append(f"{heading}: N/A (basis absent)")
                continue
            if re.search(entry["requires_pattern"], norm, re.IGNORECASE) is None:
                got_pass = False
                details.append(f"{heading}: FAIL (disclosure absent)")
            else:
                details.append(f"{heading}: PASS (disclosure present)")
        verdict = "PASS" if got_pass == expect_pass else "UNEXPECTED"
        print(f"  {label}:")
        for d in details:
            print(f"    {d}")
        print(f"    -> {'FOUND-consistent' if got_pass else 'GAP-present'}, "
              f"expected {'FOUND-consistent' if expect_pass else 'GAP-present'} "
              f"=> {verdict}")
        if verdict == "UNEXPECTED":
            all_ok = False

    print(f"\nSelf-test {'PASSED' if all_ok else 'FAILED'}: the tool "
          f"{'correctly' if all_ok else 'did NOT correctly'} discriminates "
          f"the pre-fix (gap present) from the post-fix (gap closed) "
          f"revision.")

    print("\nFor comparison, running the SAME check against the live "
          "registry entry (current working tree):")
    live = run_registry(DEFAULT_CONFIG, only="exp062-em6-em7-r-vs-t-methodology")
    return 0 if (all_ok and live == 0) else 1


def main():
    ap = argparse.ArgumentParser(
        description="Numeric-drift + derivation-methodology-consistency "
                     "lint tool. No network, no FDTD, no numpy -- pure text "
                     "and regex scanning.")
    ap.add_argument("--config", default=DEFAULT_CONFIG,
                     help=f"registry JSON (default: {DEFAULT_CONFIG})")
    ap.add_argument("--only", default=None, help="run a single registry entry by id")
    ap.add_argument("--selftest", action="store_true",
                     help="replay the Iteration-39 exp-062 EM-6/EM-7 "
                          "R-vs-T-disclosure finding against real git history")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(run_selftest())
    sys.exit(run_registry(args.config, only=args.only))


if __name__ == "__main__":
    main()
