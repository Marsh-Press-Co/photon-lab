# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's Phase-5 review this cycle.
Read PANEL.md, LOGBOOK.md in full (RULED OUT registry R1–R25, esp.
R13/R14/R18/R22/R24/R25 read in full), PLAN.md's Current-state block, the
full exp-109 record in order (`phase1_proposal.md`, all five
`phase2_critique_*.md` including my own prior-cycle
`phase2_critique_em.md`, `phase2_redteam_audit.md`, `NOTES.md`,
`results.json`, `run_output.txt`), and the actual patched code
(`experiments/108-.../run.py`, `.../analyze.py`,
`experiments/109-.../reclassify_108.py`) before writing this review.

## 1. Did my own prior-cycle mandatory fix actually land — in the code, not just the prose?

My Phase-2 critique (`phase2_critique_em.md`) required: replace "raw std
is more conservative... in every case" with an accurate **two-sided**
statement — conservative against false CONFIRM, simultaneously
liberal/anti-conservative against false REFUTE — **"in §4(a) and in
`stat_source`'s non-smooth-branch string"**, i.e. not merely NOTES.md
prose.

Checked the literal committed strings, not the surrounding narration:

- **`experiments/109-.../results.json`**, `item_ii_reclassified.r156.stat_source`
  and `.r312.stat_source` (machine-generated, written by
  `reclassify_108.py` at run time, not hand-typed): both contain, verbatim,
  *"conservative against a false CONFIRM; liberal/anti-conservative
  against a false REFUTE, since inflating the statistic only ever makes
  stat>=boxA easier to satisfy -- NOT 'conservative in every case'"*.
- **`experiments/108-t28-.../run.py`**, `classify_item_ii()`'s own
  non-smooth-branch `stat_source` f-string (the source that generates the
  above at run time) — read directly at lines 212–222 — carries the
  identical two-sided clause, and the function's own docstring (lines
  187–204) restates it a second time in prose form.
- **NOTES.md** (`fix 2`, both in the "six mandatory fixes" summary and in
  the `classify_item_ii()` code block's own docstring quoted inline)
  carries the same corrected two-sided language.

**Confirmed: the fix reached all three layers — the executed
`run.py` source, the machine-generated `stat_source` string actually
persisted in committed `results.json`, and the human-authored NOTES.md
prose.** This is not a "described but not wired" gap of the kind R24
exists to catch — I traced the string from its generating f-string in
`run.py` through to its literal appearance in the committed JSON, not
merely from NOTES.md's own restatement of it.

## 2. Independent re-derivation from primitives

Re-derived `linear_fit_1_over_margin`'s OLS fit **from scratch** in a
fresh Python process, using only `MARGINS = (24, 32, 40, 48, 57, 65)` and
the six raw `delta_values` pulled from `experiments/108-.../results.json`
— not from any cited figure in NOTES.md, the Phase-1 proposal, or the
Red Team audit:

| r | A (indep.) | B (indep.) | `residual_std` (indep.) | `r_squared` (indep.) | `is_monotonic` | `smooth` |
|---|---|---|---|---|---|---|
| 156 | −1.29691522×10⁻⁵ | −4.55906814×10⁻⁴ | 2.897162807×10⁻⁶ | 0.6653735294 | False | **False** |
| 312 | −2.63551522×10⁻⁵ | −3.39404564×10⁻⁵ | 2.102199273×10⁻⁶ | 0.0205017124 | False | **False** |

Every one of these independently-recomputed values matches the committed
`results.json` `fit` block **exactly** (full float precision, not merely
to a stated tolerance). `raw_std = np.std(delta_values)` independently
recomputed: **5.008327900579266×10⁻⁶** (r=156), **2.1240857290489×10⁻⁶**
(r=312) — exact match to `stat_used`/`raw_std` in
`experiments/109-.../results.json`. `raw_over_residual_ratio` independently
recomputed: **1.72870088...** (r=156), **1.010411218...** (r=312) — exact
match to the committed `1.7287`/`1.0104`. Feeding these through the actual
branch logic (`smooth=False` at both r ⇒ `stat=raw_std`) reproduces
**CONFIRM/CONFIRM** at both r against the CONFIRM bars (1.4845×10⁻⁵ /
1.234×10⁻⁵), independent of any code in the repository — a from-scratch
re-implementation, not a re-run of the same code.

**The OLS inequality itself** (`residual_std ≤ raw_std` always, for any
OLS fit with an intercept column): formally re-checked. Both statistics
are population (`ddof=0`) standard deviations over the same n=6 points —
`residual_std = sqrt(RSS_fit/n)`, `raw_std = sqrt(RSS_constant/n)` where
`RSS_constant = Σ(y−ȳ)²`. Because the constant model `ŷ=A, B=0` is a
feasible point in `linear_fit_1_over_margin`'s own least-squares search
space, `RSS_fit ≤ RSS_constant` always, hence `residual_std ≤ raw_std`
always, with no normalization mismatch between the two statistics (same
divisor, same n) that could hide a violation. Holds generally, not merely
at the two tested r — reconfirmed exact at both: 2.897×10⁻⁶ ≤ 5.008×10⁻⁶
(r=156), 2.102×10⁻⁶ ≤ 2.124×10⁻⁶ (r=312, a near-degenerate case at
ratio 1.010×, the closest this data comes to equality — appropriately
flagged by NOTES.md's own Tier-2 note that r=624 should be checked against
*both* bars, not assumed safe).

## 3. Formal correctness of the fallback logic / silent unit-sign check

- `DELTA_BOXA[r]` stores `|Δ_boxA|` (an already-unsigned magnitude — the
  Predictions text states this explicitly: `|Delta_boxA| = 2.969e-05
  (r=156) / 2.468e-05 (r=312)`), and `stat` (`raw_std` or `residual_std`)
  is always `np.std(...)` — non-negative by construction. No sign or
  magnitude/signed-value confusion in the CONFIRM/AMBIGUOUS/REFUTE
  comparison; `delta_values` themselves are signed (all negative in this
  data) but never compared directly against `boxA` — only their `std` is.
- `ratio = raw_std / fit["residual_std"] if fit["residual_std"] else
  float("inf")` — correctly guards the one edge case (a perfect zero-noise
  fit) without raising; not triggered by this data (`residual_std` nonzero
  at both r) but structurally sound for the case it exists to catch.
- The smooth-branch code path is byte-identical to exp-108's own original
  logic (`stat = fit["residual_std"]`); only the non-smooth branch is new.
  This is the same shape of change QUANTUM's/PHOTONICS' own Phase-5
  reviews of exp-108 (LOGBOOK.md Iteration 85) demanded — verified here as
  genuinely, not merely nominally, satisfied: `classify_item_ii()` now
  reads `fit["smooth"]` before choosing a statistic, mirroring
  `classify_item_i`'s own sibling gate.
- Verdict thresholds (`stat <= 0.5*boxA` / `stat >= boxA`) are unchanged
  from exp-108's frozen predictions and were not touched by this cycle —
  confirmed by diffing the Predictions text quoted in both `results.json`
  files, byte-identical.

**No new sign, unit, or normalization defect found in
`classify_item_ii()`, `linear_fit_1_over_margin`, or the `analyze.py`
companion call site** (traced the actual patched `analyze.py:80-92`, not
merely NOTES.md's quoted diff of it — the live file matches the diff
NOTES.md shows verbatim).

## 4. A new documentation-fidelity defect, found this cycle (minor, non-load-bearing)

NOTES.md's own Setup section quotes `build_result_text()`'s source with
**double-braced** f-string placeholders:

```
**Gate P0: {{'PASS' if gate_p0_pass else 'FAIL'}}.**
```

The actual committed `experiments/108-.../run.py:361` has **single**
braces (correct f-string interpolation):

```
**Gate P0: {'PASS' if gate_p0_pass else 'FAIL'}.**
```

Verified this is a NOTES.md documentation-quoting slip, not a real code
defect: the executed `result_text` (both in `run_output.txt` and
`results.json['result_text']`) correctly renders `**Gate P0: PASS.**` —
if the double-brace text had actually been in the executed f-string, it
would render the literal string `{'PASS' if gate_p0_pass else 'FAIL'}`
instead of `PASS`, which it does not. Low severity, does not affect any
scored outcome or the actually-executed code — flagged because NOTES.md's
own Setup section presents this block as "the exact new body" in the same
register the R24/R23 discipline treats as load-bearing documentation.

## 5. A second new gap: the trust-suite claim is not backed by the artifact NOTES.md itself cites

NOTES.md's Result section states: *"trust suite green before and after
(41/41, `--only 12346789`, 100s/102s). Full console record:
`run_output.txt`."* I read the complete, committed `run_output.txt`
(81 lines) — it contains **only** `reclassify_108.py`'s own console
capture (the OLD-vs-NEW item_ii comparison, `predictions_text`,
`result_text`); it contains **zero** trust-suite output (no `[PASS]`
lines, no `41/41`, no `--only` invocation, no timing). The specific,
high-precision figures quoted (41/41, 100s/102s) are not traceable to any
committed artifact in `experiments/109-.../` — the document cites
`run_output.txt` as its evidentiary record in the same sentence that makes
a claim that file does not contain.

I independently re-ran the trust suite this review (`python3
lab/validation/run_all.py --only 12346789`, foreground): **41/41 checks
passed in 106 s** — consistent with, though not numerically identical to
(100s/102s vs. 106s, ordinary run-to-run wall-clock variance), the claimed
figures. This corroborates that the underlying claim is true, but does not
retroactively make it *evidenced* — the gap is in what the committed
record can independently support, not in whether the claim happens to be
correct. `git diff --stat -- lab/` for exp-109's own commit independently
confirms zero `lab/` files touched (six files changed, all inside
`experiments/108-.../` and `experiments/109-.../`), so the "zero `lab/`
diff" half of the same sentence is fully verifiable and correct.

This is a citation-completeness gap in the same lineage as R23's own
"human-readable-citation" half (a real number asserted in Result prose
without the artifact that would let a reader check it) — not a fresh
R-rule instance (no prior cycle carries this exact shape on this exact
channel), and **not outcome-reversing**: the claim is independently
verified true by my own re-run. Recorded as a gap for Phase-3/NOTES.md
discipline going forward, not as a defect in the classification logic
itself.

## Verdict: **CONFIRM-WITH-GAPS**

**What is genuinely, verifiably confirmed:**
- My own prior-cycle mandatory fix (the two-sided
  conservative-against-false-CONFIRM /
  liberal-against-false-REFUTE correction) reached the actually-executed
  `run.py` source, the machine-generated `stat_source` string literally
  committed in `results.json`, and NOTES.md's human-authored prose — all
  three layers, independently traced from primitives, not merely restated.
- The OLS inequality (`residual_std ≤ raw_std` for any OLS fit with an
  intercept) is formally correct and independently re-derived exact at
  both r, including the near-degenerate r=312 case (ratio 1.010×).
- A full from-scratch re-derivation of both r's fit (`A`, `B`,
  `residual_std`, `r_squared`, `is_monotonic`, `smooth`), `raw_std`, and
  `raw_over_residual_ratio` reproduces every committed value exactly,
  independent of any code already in the repository.
- No sign, unit, or normalization defect found in the fallback logic; the
  R24 second-instance fix is genuinely wired into the executed
  classification path (confirmed by reading `analyze.py`'s actual patched
  call site, not NOTES.md's description of it).
- `git diff --stat -- lab/` independently confirms zero `lab/` diff.

**Gaps found this review, both new, neither outcome-reversing:**
1. A documentation-fidelity slip in NOTES.md's own quoted
   `build_result_text()` source (double-braced placeholders vs. the
   actual single-braced, correctly-interpolating committed code) —
   cosmetic, does not reflect the real executed behavior.
2. NOTES.md's Result-section trust-suite claim (41/41, 100s/102s) is not
   evidenced by `run_output.txt`, the console record the same sentence
   cites — independently re-verified true by re-running the suite this
   review (41/41, 106 s), but not verifiable from the committed record
   alone.

Most important finding: **the prior-cycle EM mandatory fix was genuinely
applied to the machine-generated `stat_source` string committed in
`results.json`, not only to NOTES.md's human-authored prose** — traced
end-to-end from the generating f-string in the patched `run.py` through to
the literal committed JSON text, closing the exact gap this review was
charged to check.
