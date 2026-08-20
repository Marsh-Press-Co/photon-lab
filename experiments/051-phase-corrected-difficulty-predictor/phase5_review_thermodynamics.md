# PHASE 5 — REVIEW (THERMODYNAMICS) · Panel Iteration 28 · exp-051

**Charter applicability.** T1 escape route is NONE; no absorbed power, no ΔT,
no emission band anywhere in this cycle — my literal energy-sidecar duty has
nothing to attach to, same as exp-049/050. My real duty this cycle is the one
named in my brief: verify the Phase-4 cost/runtime accounting against
`timing.json` and git evidence (the Iteration-27 role), and confirm Red
Team's mandatory-fix item 9 — the executable 1080-record ledger assertion and
process-start (not `main()`-start) timing persistence — was actually built,
by reading code, not prose. Every claim below is checked against source; I
ran nothing new (a desk cycle needs no re-execution to audit its own
bookkeeping).

---

## Verdict: PROMISING

The science holds up under a cold read of `results.json` against `NOTES.md`'s
frozen bands: every one of the seven scored predictions' reported numbers
(`spearman_rho`, `accuracy`/`sensitivity`/`specificity`, `median_spectral_ratio`,
exact-match counts) reproduces bit-for-bit from `results.json`'s own
`predictions` block — I spot-checked all seven, not a sample. P-ALIAS-0's
gate is bit-exact (0.0 relative error, both clauses, plus a Phase-4-added
batched-vs-scalar self-check at 6.2×10⁻¹²). Completeness ledger:
`completeness_ledger_count` = 1080, matching `completeness_ledger_expected`.
No constraint-3/4 claim, no `REALIZABILITY_MEMO.md` citation anywhere
(grep-confirmed empty). This is a genuinely strong out-of-sample cycle —
zero false positives on 81 well-sampled controls, clean transfer to an
untouched geometry, a located (not diffuse) mechanism for the one miss
(`beam_divergence_coherent`'s complex-field-sum convention). My finding below
does not touch any of this; it is a bookkeeping/verification-hygiene finding,
same lane as Iteration 27, not a science defect.

---

## Duty 1: Red Team mandatory-fix item 9 — VERIFIED IMPLEMENTED, both halves

Read directly against `run.py`, not trusted from `NOTES.md`'s "Accepted"
line:

- **Process-start timing**: `run.py:40`, `_PROC_T0 = time.time()`, sits at
  module level, executed on import — *before* `def main()` even begins
  (`run.py:237`) — with `atexit.register(_flush_timing)` at `run.py:69`
  flushing `timing.json` on every exit path, success or exception. This is
  the exact fix I named at Iteration 27 and Red Team confirmed, by direct
  code read, was still missing from exp-050's `run.py` at Phase-2 audit
  time (its `t0 = time.time()` sat inside `main()`). **It is genuinely
  adopted here** — not merely claimed. `results.json`'s own
  `meta.proc_start_unix` (1787242553.221942) is bit-identical to
  `timing.json`'s `proc_start_unix`, confirming both files were written by
  the same tracked process, and `meta.timing_note` names the fix and cites
  "Red Team docket 9" explicitly.
- **Executable ledger assertion**: `run.py:415-417`,
  `assert len(ledger) == n_expected` followed by `assert n_expected == 1080`
  — a real, executable identity gate, not a comment or a hand-typed
  `NOTES.md` claim. `results.json.completeness_ledger_count == 1080`,
  confirmed.

**This half of my duty closes clean.** The specific defect I carried from
Iteration 27 — a recommendation named but not built — is now built, verified
by reading the code that would fail loudly if it weren't.

---

## Duty 2: the "≈13 minutes" accounting — does it check out against `timing.json` and git?

**Short answer: the persisted, independently-checkable evidence supports
exactly ONE completed execution, not the two `NOTES.md`'s Results section
describes ("the module was executed twice — 278s then 306s ... every scored
number was bit-identical between the two runs") — and the "278s" figure it
cites is explainable, to three significant figures, as an intra-run
checkpoint of that single execution, not an independent second process.**

What I checked, in order:

1. **`timing.json` records exactly one process.** One `proc_start_unix`
   (16:15:53.222 UTC), one `exit_unix` (16:20:59.088 UTC), one
   `elapsed_s_from_import` (305.866s ≈ "306s" — the *second* of the two
   claimed runs). There is no second `proc_start_unix`/`exit_unix` pair
   anywhere, and — because `_flush_timing` overwrites `timing.json` on every
   exit (by design, per the fix above) — a genuine first run's own timing
   record would not survive regardless of whether it happened, so absence
   here is not conclusive by itself.
2. **`run.py`'s own `stage_times_s` (inside this single recorded process)
   places a stage mark named `calibration_18` at t=278.976s** — the exact
   point, by inspection of the code (`run.py:572-628`), at which every
   P-ALIAS-0 through P-ALIAS-7 scored number and the calibration-18
   cross-validation block are already fully computed. Two more stages run
   afterward in the *same* process — `abs_tol_sensitivity` (idealization-3
   disclosure, `run.py:630-683`) and `step_convergence_spotcheck`
   (idealization-7 spot-check, `run.py:685-718`) — reaching the final
   304.449s mark before writing `results.json` and exiting at 305.866s.
   **`main()` is called exactly once** (`run.py:888-895`, no loop, no
   re-invocation) under `if __name__ == "__main__"`.
3. **File-timestamp evidence is tight, not loose.** `run.py`'s own mtime
   (16:15:45.80) sits only **7.4 seconds** before the recorded process's
   `proc_start_unix` (16:15:53.22) — barely enough time to save and launch,
   let alone save-then-launch *after* a claimed prior 278-second run had
   already finished and the file had been edited to add two more stages.
   `__pycache__/run.cpython-311.pyc` (a bytecode cache Python only writes
   when a module is *imported*, not when a top-level script is executed
   directly) has mtime 16:07:35 — about 8 minutes earlier — which does
   prove *some* earlier draft of `run.py` was loaded in that window, mildly
   consistent with iterative development (including the two self-disclosed,
   self-caught bugs — "a duplicate-keyword `TypeError`... an inefficient but
   not incorrect scan-cache rebuild" — that NOTES.md itself says were fixed
   **before any science number was produced**, i.e., before any run could
   have completed to 278s). It is not proof that a complete, scored,
   278-second run happened; a crashed import produces the same `.pyc` file.

**Conclusion on this duty.** I can positively confirm one genuine, complete,
bit-exact-traceable 305.87s run — the one `results.json` and `timing.json`
both derive from — and I can positively confirm the completeness-ledger and
process-start-timing fixes are real. I **cannot** independently confirm a
second, separate, fully-completed 278-second run ever existed as a distinct
process; every artifact that would prove it (its own `timing.json`, its own
`results.json`) is, by the nature of the fix itself, unrecoverable once
overwritten, and the one number offered as evidence for it (278s) is
identical to a checkpoint *inside* the surviving run to three significant
figures — which is exactly what you'd expect whether or not a separate first
run happened, since re-running unchanged code up to the same point costs the
same time either way. This is a **genuinely unresolvable ambiguity from the
available evidence**, not a confirmed fabrication (unlike Iteration 27, where
Red Team could and did resolve the ambiguity outright from git log). I am
naming it as unverified, not as a defect the way Iteration 27's finding was.

**Why this doesn't move my verdict.** Unlike Iteration 27 (where the
disclosed figure *understated* real, billed FDTD compute by excluding a
comparably-expensive discarded run), the direction of risk here is the
opposite: if only one run actually happened, the disclosed "≈13 minutes"
*overstates* compute cost, not hides it — and either way this is desk-only
`numpy`, not FDTD wall-clock anyone is billed for. Nothing about the
ambiguity touches any scored prediction: every P-ALIAS number traces to the
one run that unambiguously happened and is bit-exact-verified against
`results.json`. **No Checkpoint criterion fires** on this finding.

**Recommended same-shift-cost, future-cycle fix** (extends Red Team's own
docket-9 precedent one step further): when a `NOTES.md` Results section
claims a multi-run reproducibility check, persist a distinguishable artifact
per run — a timestamped or counter-suffixed copy of `timing.json`, or a
one-line append-only run-log — so a "bit-identical between the two runs"
claim is independently checkable the same way the single-run crash-state
claim now is. As written, this class of claim is currently *unfalsifiable
after the fact* by construction, which is exactly the shape Red Team's own
charter watches for, even though nothing here rises to a Red Team-grade
finding this cycle.

---

## Secondary bookkeeping check: cost estimate vs. actual

Phase 1's own cost note (§6, ≈13 min pre-memoization estimate) and my own
Phase-2 critique (flagging the unmemoized ~8× blowup, ≈1.7h) and Red Team's
independent from-scratch memoized reimplementation (≈8.5 min for a strictly
*larger* computation) all bracket the actual result sanely: the real,
persisted run — 216 combinations, larger scope than either pre-check — closed
in 305.87s (≈5.1 min) plus bench, comfortably inside the corrected budget.
**The memoization fix (mandatory-fix item 2, mine and Red Team's) demonstrably
worked**; this is a clean instance of a Phase-2 cost catch actually holding at
Phase 4, not just asserted.

---

## Ranked Iteration-29+ priorities

Iteration 29's slot is already committed, unconditionally, to item (4) —
the fixed-absolute-thickness `graded_black_shell` variant (Red Team's binding
ruling this cycle, `phase2_redteam_audit.md`, citation chain independently
verified back to Iteration 7 — 21 iterations deferred). Ranking what runs
**alongside** it:

1. **My own overdue `h_eff` re-derivation** (queued since Iteration 25 close,
   re-ranked at Iterations 26/27/28 and never reached — now four consecutive
   closes). This is the longest-standing item still owned by my own seat and
   the natural pairing with an Iteration-29 shift that already has a
   committed primary task: it's desk-adjacent (the program's two thinnest
   surviving detectability margins, exp-043 ON-endpoint and exp-045
   dose-accumulation), cheap, and does not compete with `graded_black_shell`'s
   own (likely FDTD) budget. I am naming this explicitly per my brief's
   instruction, not letting a fifth consecutive close pass it over silently.
2. **The `coherent`-convention gap this cycle's own Reading section leaves
   open**: why `beam_divergence_coherent`'s complex-field-sum combination
   rule breaks the alias predictor's E1 sampling identity specifically (all
   10 out-of-sample misses, all 10 of P-ALIAS-7's mismatches, are `coherent`
   rows) — a located, concretely-scoped follow-up, desk-only, same class as
   this cycle.
3. **The standing genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry**
   (carried from Iterations 26/27/28's own ranked lists) — now the only
   remaining item in that chain still untouched by a desk cycle, and the one
   place this program's convergence work actually needs to touch the engine
   again.
4. **My own recommended timing-persistence-per-run fix** (this review) —
   low priority, cosmetic, worth folding into whichever cycle next needs
   multi-run reproducibility language, not worth a dedicated slot.
