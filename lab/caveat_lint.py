"""lab/caveat_lint.py — the mechanical caveat-propagation-check tool.
=====================================================================
Panel Iteration 38 (MATERIALS, lead-by-lock), executing the co-mandatory
rider authorized at Red Team's Iteration-36/37 rulings and first proposed
by VISION SCIENCE at Iteration 15 ("a lint-style or verbatim-reuse
enforcement mechanism"). Exact spec as authorized (Iteration 37 close,
LOGBOOK.md): "a lint-style, grep-every-caveat-across-every-touched-file
tool." The identical caveat-propagation-failure defect class has fired or
nearly fired Checkpoint criterion 4 at Iterations 17, 24, 32, 33, 34, 35,
twice at 36, and again at 37 — six prior hand-patches, each missing a
site the next cycle then found.

WHAT THIS IS NOT: a physics gate. It reads text files and reports whether
a string pattern appears where a Phase-5 mandatory-fix docket says it
must. It has no opinion on whether any measurement is correct. It is
therefore NOT wired into `lab/validation/run_all.py` as a numbered stage
(reasoning, for Red Team to check): (1) `run_all.py`'s stages certify
FDTD/engine physical-identity claims against hard expected numbers —
every existing stage (1-22) either re-runs a simulation or checks a
closed-form/regression identity against measured data. A "does this
substring appear in this file" check is a categorically different kind
of assertion — a documentation-completeness check, not a measurement
gate — and folding it into the same suite would blur the suite's own
"trust status" semantics (VALIDATION.md's whole point: stage N passing
means an engine-physics claim is verified). (2) It needs zero FDTD, zero
numpy, zero network — bundling it with the trust suite would make the
suite's cheap stages (currently the ones you can run in seconds) contend
with a job that greps the whole repo, for no shared benefit. (3) Most
importantly: this tool's registry (`caveat_lint_config.json`) must be
hand-curated per mandatory-fix docket — a Director decides which new
caveats need tracking, same as a Director decides which new machinery
needs a trust-suite stage. Auto-running it inside `run_all.py` would
either (a) silently skip newly-introduced undocketed caveats (false
confidence) or (b) require every run_all.py invocation to also load and
validate a caveat registry that has nothing to do with engine trust.
Keep the concerns separate: `run_all.py` answers "is the engine's physics
trustworthy"; `caveat_lint.py` answers "did a documented caveat actually
propagate to every site a Phase-5 docket named."

WHAT A "CAVEAT" IS, OPERATIONALLY (this tool's own definition, per the
Iteration-38 mandate): a short key phrase or clause, explicitly named in
a Phase-3/Phase-5 mandatory-fix docket entry, that must appear (in some
recognizable paraphrase — see PHRASE MATCHING below) at N named sites.
The docket entry is the source of truth; this tool is the check that the
docket's own "propagate to sites X, Y, Z" promise was kept, plus a lead
on undocketed sites that may also need it.

REGISTRY. `lab/caveat_lint_config.json` (checked in, hand-curated) is a
JSON list of caveat entries:

  {
    "id":               short slug, unique
    "description":      one line, human-readable, cites the docket entry
    "source":           where this caveat was authorized (LOGBOOK.md
                         iteration / NOTES.md section), for provenance
    "phrase_patterns":  list of regexes (any ONE matching a site's
                         whitespace-normalized text counts as "present" —
                         a caveat is rarely restated verbatim at every
                         site, so this is deliberately an ANY-OF list of
                         acceptable paraphrases, not a single exact string)
    "required_sites":   list of repo-relative file paths that MUST match
                         one of phrase_patterns — a FAIL here is what
                         gates the tool's exit code
    "trigger_terms":    list of substrings/regexes that indicate a file is
                         citing the SAME claim/number/module (e.g. a
                         function name, a specific number like "60nm") —
                         used only to discover NEW candidate sites, never
                         gates the exit code
    "candidate_globs":  optional list of glob patterns (repo-relative) to
                         search for trigger_terms; defaults to
                         DEFAULT_CANDIDATE_GLOBS below if omitted
  }

PHRASE MATCHING. Each file's text is whitespace-normalized (runs of
whitespace, including newlines, collapsed to a single space) before
matching, so a phrase that is prose-wrapped across lines in a .md file
still matches a plain-substring-style regex. Matching is
case-insensitive. This is deliberately loose (a lint tool, not a proof
checker) — false negatives (missed real propagation) are the risk this
tool exists to eliminate; a human still reads the report.

USAGE (both a config-driven mode and an ad-hoc mode, per the mandate):

  # run every caveat in the registry, exit 1 if any required site fails
  python3 lab/caveat_lint.py

  # run just one registry entry
  python3 lab/caveat_lint.py --only exp060-p10-fresnel-not-diffraction

  # one-off check, no registry edit needed (a Director verifying a
  # same-shift Phase-5 fix before committing it to the registry)
  python3 lab/caveat_lint.py --adhoc \\
      --phrase "one disclosed convention among possible others" \\
      --sites experiments/060-sharp-uniform-lossy-disk-control/NOTES.md \\
      --trigger sigma_flat

  # self-test: prove the tool retroactively catches a REAL historical
  # near-miss (Iteration 37's own run_all.py stage-22 docstring gap) by
  # checking the exact pre-fix and post-fix git revisions
  python3 lab/caveat_lint.py --selftest

Exit code: 0 iff every required_site of every SELECTED caveat matches at
least one of its phrase_patterns. Candidate-site findings (undocketed
files that mention a trigger term but not the phrase) are printed as
WARN and never affect the exit code — they are a lead for a human to
triage, not a failure (an undocketed passing mention is not itself a
defect; see reasoning above).
"""

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(HERE, ".."))
DEFAULT_CONFIG = os.path.join(HERE, "caveat_lint_config.json")

# Files a caveat's own trigger terms are searched across when hunting for
# NEW, undocketed candidate sites. Deliberately text-only, deliberately
# excludes results.json (numeric data, not prose a caveat propagates
# into) and lab/ARTIFACTS.md / lab/viz.py (house hard limits — never
# touched, never scanned as a caveat SITE by this tool either, to avoid
# any temptation to "fix" something there).
DEFAULT_CANDIDATE_GLOBS = [
    "LOGBOOK.md",
    "PLAN.md",
    "SESSION_LOG.md",
    "PANEL.md",
    "experiments/*/NOTES.md",
    "experiments/*/REALIZABILITY_MEMO.md",
    "experiments/*/phase4_results.md",
    "experiments/*/phase*.md",
    "experiments/*/*.py",
    "lab/*.py",
    "lab/validation/run_all.py",
    "lab/validation/VALIDATION.md",
]

_WS_RE = re.compile(r"\s+")


def _normalize(text):
    return _WS_RE.sub(" ", text)


def _read(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except (FileNotFoundError, IsADirectoryError):
        return None


def _read_git(rev, relpath):
    """Read a file's content AT A GIVEN GIT REVISION, without touching
    the working tree — used only by --selftest. Returns None if the path
    did not exist at that revision."""
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


def _matches_any(text_norm, patterns):
    for pat in patterns:
        if re.search(pat, text_norm, re.IGNORECASE):
            return pat
    return None


def _iter_glob_files(globs):
    seen = set()
    for pattern in globs:
        if "*" in pattern:
            base_dir = REPO_ROOT
            for root, dirs, files in os.walk(REPO_ROOT):
                dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "node_modules")]
                rel_root = os.path.relpath(root, REPO_ROOT)
                for fn in files:
                    relpath = os.path.normpath(os.path.join(rel_root, fn)) if rel_root != "." else fn
                    relpath = relpath.replace(os.sep, "/")
                    if fnmatch.fnmatch(relpath, pattern):
                        if relpath not in seen:
                            seen.add(relpath)
                            yield relpath
        else:
            if os.path.isfile(os.path.join(REPO_ROOT, pattern)) and pattern not in seen:
                seen.add(pattern)
                yield pattern


def check_caveat(entry, repo_root=REPO_ROOT):
    """Check one caveat entry against the LIVE working tree. Returns:
        {"id", "site_results": [(path, ok, matched_pattern_or_None)],
         "candidates": [(path, trigger_matched)]}
    (--selftest checks specific git revisions directly, via `_read_git`,
    rather than through this function -- see `run_selftest`.)"""
    patterns = entry["phrase_patterns"]
    site_results = []
    for relpath in entry["required_sites"]:
        text = _read(os.path.join(repo_root, relpath))
        if text is None:
            site_results.append((relpath, False, "FILE NOT FOUND"))
            continue
        norm = _normalize(text)
        matched = _matches_any(norm, patterns)
        site_results.append((relpath, matched is not None, matched))

    candidates = []
    trigger_terms = entry.get("trigger_terms", [])
    if trigger_terms:
        required_set = set(entry["required_sites"])
        globs = entry.get("candidate_globs", DEFAULT_CANDIDATE_GLOBS)
        for relpath in _iter_glob_files(globs):
            if relpath in required_set:
                continue
            text = _read(os.path.join(repo_root, relpath))
            if text is None:
                continue
            norm = _normalize(text)
            trig = _matches_any(norm, trigger_terms)
            if trig is None:
                continue
            if _matches_any(norm, patterns) is not None:
                continue  # already carries the caveat -- not a gap
            candidates.append((relpath, trig))

    return {"id": entry["id"], "site_results": site_results, "candidates": candidates}


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _print_report(result, entry):
    print(f"\n[{result['id']}]  {entry.get('description', '')}")
    if entry.get("source"):
        print(f"  source: {entry['source']}")
    ok_all = True
    for path, ok, matched in result["site_results"]:
        status = "PASS" if ok else "FAIL"
        if not ok:
            ok_all = False
        detail = f"matched: {matched!r}" if ok else (matched or "no phrase_patterns matched")
        print(f"  {status}  {path}   ({detail})")
    for path, trig in result["candidates"]:
        print(f"  WARN  candidate site (trigger {trig!r} found, caveat phrase absent): {path}")
    return ok_all


def run_registry(config_path, only=None):
    entries = load_config(config_path)
    if only:
        entries = [e for e in entries if e["id"] == only]
        if not entries:
            print(f"No caveat with id={only!r} in {config_path}", file=sys.stderr)
            return 2
    all_ok = True
    n_fail = 0
    for entry in entries:
        result = check_caveat(entry)
        ok = _print_report(result, entry)
        all_ok = all_ok and ok
        n_fail += sum(1 for (_, site_ok, _) in result["site_results"] if not site_ok)
    print(f"\n{len(entries)} caveat(s) checked, {n_fail} required-site failure(s).")
    return 0 if all_ok else 1


def run_adhoc(phrase, sites, triggers):
    entry = {
        "id": "adhoc",
        "description": "one-off check (--adhoc)",
        "phrase_patterns": [re.escape(phrase)],
        "required_sites": sites,
        "trigger_terms": triggers or [],
    }
    result = check_caveat(entry)
    ok = _print_report(result, entry)
    return 0 if ok else 1


def run_selftest():
    """Retroactive validation against a REAL historical near-miss: the
    Iteration-37 Checkpoint-4 finding (VISION SCIENCE's catch, LOGBOOK.md
    Iteration 37 Phase-5) that `lab/validation/run_all.py`'s own
    `stage22_uniform_lossy_shell` docstring still stated the pre-run
    "disentangle...diffraction" framing after exp-060's own P-10 result
    refuted it (the mechanism is Fresnel reflectance at a sharp
    discontinuity, not edge/grazing diffraction) -- and the fix that
    landed same-shift.

    Pre-fix commit: d5b4844 (Iteration 37 Phase 3 -- new machinery
    committed BEFORE the run; the docstring at this revision only has
    the pre-run framing).
    Post-fix commit: 4f29982 (Iteration 37 Phase 5 -- six blind reviews +
    Red Team audit; the docstring is corrected in this commit, same
    shift the finding was made).

    PREDICTION (committed before running this selftest): checking for
    the phrase "Fresnel-type reflectance at the sharp conductivity
    discontinuity" (the corrected framing) at
    lab/validation/run_all.py::stage22's docstring --
      - at d5b4844 (pre-fix): FAIL (the phrase does not exist yet)
      - at 4f29982 (post-fix, == current HEAD content): PASS
    This demonstrates the tool WOULD have caught the Checkpoint-4 gap,
    had it existed and been pointed at this docket entry, before Phase-5
    review had to catch it by hand.
    """
    relpath = "lab/validation/run_all.py"
    phrase_patterns = [
        r"Fresnel-type reflectance at the sharp conductivity\s*\n?\s*discontinuity",
    ]
    entry = {
        "id": "selftest-exp060-stage22-docstring",
        "description": (
            "Historical replay: does run_all.py's stage22 docstring carry "
            "exp-060's own P-10 correction (Fresnel reflectance, not "
            "diffraction)? Iteration-37 Checkpoint-4 finding."
        ),
        "phrase_patterns": phrase_patterns,
        "required_sites": [relpath],
    }
    print("Self-test: replaying Iteration-37's own stage-22-docstring "
          "Checkpoint-4 finding against two real git revisions.\n")

    results = {}
    for label, rev, expect_pass in (
        ("PRE-FIX  (d5b4844, Phase 3, before the run)", "d5b4844", False),
        ("POST-FIX (4f29982, Phase 5, same-shift fix)", "4f29982", True),
    ):
        text = _read_git(rev, relpath)
        if text is None:
            print(f"  [{rev}] could not read {relpath} from git history "
                  f"(shallow clone / rev not present) -- skipping this leg.")
            results[rev] = None
            continue
        norm = _normalize(text)
        matched = _matches_any(norm, phrase_patterns)
        got_pass = matched is not None
        verdict = "PASS" if got_pass == expect_pass else "UNEXPECTED"
        print(f"  {label}: caveat phrase {'FOUND' if got_pass else 'ABSENT'} "
              f"-- expected {'FOUND' if expect_pass else 'ABSENT'} -> {verdict}")
        results[rev] = got_pass

    ok = (results.get("d5b4844") is False) and (results.get("4f29982") is True)
    print(f"\nSelf-test {'PASSED' if ok else 'FAILED'}: the tool "
          f"{'correctly' if ok else 'did NOT correctly'} discriminates the "
          f"pre-fix (gap present) from the post-fix (gap closed) revision.")

    print("\nFor comparison, running the SAME check against the live "
          "registry entry (current working tree):")
    live = run_registry(DEFAULT_CONFIG, only="exp060-p10-fresnel-not-diffraction")
    return 0 if (ok and live == 0) else 1


def main():
    ap = argparse.ArgumentParser(
        description="Grep-every-caveat-across-every-touched-file lint tool. "
                     "No network, no FDTD, no numpy -- pure text scanning.")
    ap.add_argument("--config", default=DEFAULT_CONFIG,
                     help=f"caveat registry JSON (default: {DEFAULT_CONFIG})")
    ap.add_argument("--only", default=None, help="run a single registry entry by id")
    ap.add_argument("--adhoc", action="store_true",
                     help="one-off check, bypassing the registry")
    ap.add_argument("--phrase", default=None, help="--adhoc: the phrase/regex to require")
    ap.add_argument("--sites", default=None,
                     help="--adhoc: comma-separated repo-relative file paths")
    ap.add_argument("--trigger", action="append", default=None,
                     help="--adhoc: a trigger term for candidate-site discovery "
                          "(repeatable)")
    ap.add_argument("--selftest", action="store_true",
                     help="replay the Iteration-37 stage-22-docstring finding "
                          "against real git history as a validation check")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(run_selftest())
    if args.adhoc:
        if not args.phrase or not args.sites:
            ap.error("--adhoc requires --phrase and --sites")
        sites = [s.strip() for s in args.sites.split(",") if s.strip()]
        sys.exit(run_adhoc(args.phrase, sites, args.trigger))
    sys.exit(run_registry(args.config, only=args.only))


if __name__ == "__main__":
    main()
