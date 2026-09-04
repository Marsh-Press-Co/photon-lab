# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 87 (exp-110)

*Fresh sub-agent, blind to every other seat's Phase-5 review this cycle.
Charter: human perceptual limits — contrast thresholds, luminance edge
detection, spectral sensitivity, adaptation, temporal sensitivity,
saccadic/attentional blindness; central question: what would make a human
eye FAIL to register something physically present? Duty: pin numeric
thresholds, with sources, BEFORE any run that scores against them. Note
from the Director's brief: in recent T28 governance cycles this seat's
highest-value contribution has repeatedly been auditing R23
DISCLAIMER-discipline and claimed-vs-actual code execution paths — that is
the primary lens applied below. This is a T1-N/A governance/instrumentation
cycle; my charter's substantive perceptual-threshold duty is not engaged
(confirmed below, §0), and correctly not engaged, matching every T28
governance cycle since Iteration 84.*

All verification below is independently re-derived from primitives —
direct source reads, live re-execution of committed code, and direct
`results.json` inspection — not taken on the Phase-1/2/3 documents' own
say-so.

---

## 0. Charter-duty check — clean, as expected for this cycle type

No implicit perceptual-relevance framing found anywhere in NOTES.md (no
"notice"/"visible"/"reader would" language misapplied to a governance
claim). T1 is genuinely N/A: item 1 is angular-pattern floor-gating
arithmetic, item 2 a numpy curve-fit diagnostic, item 3 a checkpoint/resume
identity gate — none touches σ(I)/σ(x,t)/angular-selectivity/sub-threshold
machinery, confirmed by direct read of `run.py`/`analyze.py`/
`chunk_runner.py`/`finalize.py` in full. No constraint-1/2/3/4 verdict is
scored or moved anywhere in this document. Correctly, plainly stated as
such — the correct discharge of this duty clause this cycle, exactly as in
exp-107/108/109.

## 1. THE critical check — Fix 7 / R23: genuinely landed, not dead code

**(a) The asserts are real and both fire on the actual execution path.**
Read `finalize.py` directly (not summarized): lines 78–91 compute
`predictions_text = R.build_predictions_text()` and `result_text =
R.build_result_text(...)` by calling the real, committed functions (not
hand-typed prose), then at module level, unconditionally on every
invocation:

```python
assert R.DISCLAIMER in predictions_text, "R23: disclaimer missing from Predictions block"
assert R.DISCLAIMER in result_text, "R23: disclaimer missing from Result block"
```

This is the operative Phase-4 finalize script (not `run.py`'s own
`--predictions-only` block, which asserts only the predictions half — a
narrower, secondary entry point). Both `DISCLAIMER` occurrences are
injected into `build_predictions_text()`/`build_result_text()` via a
literal `{DISCLAIMER}` f-string interpolation (`run.py` lines 390, 439) —
single source of truth, exactly R23's founding pattern (exp-104). **Not
dead code**: `results.json`'s top-level keys include
`predictions_text`, `result_text`, and `r27_cost_gate_founding_instance`
(confirmed by direct read) — the latter is written only after both asserts
pass (`finalize.py` line 92, after the asserts at lines 86–87) — so the
persisted file is itself evidence the asserts executed and passed, not
merely that they exist in source. I did not stop at that indirect
evidence: I independently re-ran `linear_fit_control.py` live this review
(reproduces all four cases bit-exact, matches `linear_fit_control_output.
json` exactly, `git status` clean afterward) and re-ran `lab/validation/
run_all.py --only 26` live (3/3, `rel_diff_truncated=1.999` exactly as
cited) and the full standard suite `--only 12346789` live (**41/41, 79s** —
matches NOTES.md's own 77s/80s citations to within normal run-to-run
variance) — confirming this document's claimed-vs-actual execution paths
hold up under independent re-execution, not merely a source-code read.

**(b) Byte-for-byte verbatim check — EXACT MATCH, both fields.** I wrote a
direct comparison script: extracted `results.json["predictions_text"]`/
`["result_text"]` and NOTES.md's own two fenced code blocks (Predictions,
Result), and diffed them programmatically.

```
predictions_text == NOTES.md's Predictions block:  EXACT MATCH (3605 bytes)
result_text       == NOTES.md's Result block:       EXACT MATCH (3931 bytes)
```

(A naive regex extraction of the fenced blocks appeared to show a 1-byte
discrepancy at each block's tail — traced to the extraction regex itself
consuming the newline immediately before the closing ` ``` ` fence as a
delimiter rather than content; restoring that trailing `\n` to the
extracted block yields an exact match. Not a real discrepancy — flagged
here only so this check's own methodology is auditable, per this program's
own R4 discipline of showing the work, not just the verdict.)

**This closes my own Phase-2 flip condition in full, and by the strongest
possible margin.** My Phase-2 critique asked for "NOTES.md must quote
`result_text` verbatim... reported pass/fail before the Combined Verdict is
written" — NOTES.md's Result section states "`finalize.py` asserted
`DISCLAIMER in` both `predictions_text` and `result_text` (both passed)"
immediately before the quoted block and the Combined Verdict, and the quote
itself is not merely "verbatim by inspection" (this sub-thread's prior
three-cycle standard, per LOGBOOK's R23 entry) but byte-identical to the
actual persisted field. This is the cleanest instance of this specific
check in the T28 governance sub-thread's recorded history — genuinely
closing the gap I flagged at exp-108 (`phase5_review_vision.md` there:
"the Result section's own prose never quotes the disclaimer text verbatim,
a two-cycle-consistent documentation gap") for the second time running,
now with byte-level rather than inspection-level confidence.

## 2. Fix table cross-check — all 8 mandatory fixes independently verified as genuinely implemented

Beyond the R23-specific Fix 7/8 above (both confirmed genuine), I
independently re-verified the remaining fixes against source/results, not
the disposition table's own say-so:

- **Fix 1** (pooled median floor, not single-point `max`): `run.py::
  mirror_pooled_floor()` computes `np.percentile(pairs, percentile)` over
  all `n//2` bin-pairs — a genuine pooled statistic, confirmed by direct
  read, not the raw single-bin `max()` construction Phase 1 originally
  proposed.
- **Fix 3** (R13-only, not R13+R14): `classify_item_i_local()`'s own
  docstring states "Discharges R13... ONLY -- NOT R14" — confirmed. Minor,
  non-substantive precision note: the fix-disposition table cites "this
  NOTES.md" as a second implementation location for the corrected language,
  but no restated "R13 only" sentence actually appears in NOTES.md's own
  Hypothesis/Setup prose outside the table and the function docstring —
  harmless, since the original overclaim ("discharges R13 and R14") also
  never appears anywhere in NOTES.md's substantive prose, so there is
  nothing left uncorrected; flagged only for completeness, not a defect.
- **Fix 4/2** (discretization-vs-fabrication-tolerance and common-mode-
  blindness disclaimers): both sentences are present, verbatim, inside
  `DISCLAIMER` (confirmed by direct string read) — see §3 below for a
  finding on how the common-mode clause is *applied* in the Interpretation
  prose, distinct from whether it is *present*.
- **Fix 5/R27** (cost gate wired as code): confirmed `analyze.py` actually
  branches on `R.cost_gate_check(...)["proceed_to_r312"]` (not merely
  defines it) — `results.json["cost_gate"]["proceed_to_r312"]=true`,
  `r312_deferred=false`, and r=312 data is genuinely present, consistent
  with the gate having fired and passed, not merely computed and ignored.
- **Fix 6** (fresh wall-time distinct from exp-108's historical figure):
  confirmed `results.json["total_wall_s"]=7690.43`, distinct from and
  correctly NOT equal to exp-108's own historical `7712.0` — and the
  per-scene breakdown in Result prose sums exactly to this total (752.2s
  r=156 + 6938.2s r=312 = 7690.4s, checked by hand).

All 8 fixes: genuinely implemented, not merely claimed. This is a
materially cleaner Phase-4 execution than several recent T28 governance
cycles this registry records (exp-106's own unwired mandatory-fix-1
consequence; exp-108's own second R24 instance).

## 3. THE finding — a directional misapplication of the common-mode-blindness disclaimer in the Interpretation prose

This is the substantive answer to task (c): checking whether the Result
section's own interpretation of the two named bins as UNRESOLVED correctly
reflects the DISCLAIMER's own stated limits.

**The DISCLAIMER's own stated mechanism, precisely** (and Red Team's own
§1.1 algebraic re-derivation, independently re-checked here): `mirror_
pooled_floor` is built by *differencing* mirror-paired bins,
`|pattern[i]-pattern[n-1-i]|/2`. Any bias component identical at both
paired bins (common-mode/even noise) cancels EXACTLY in this difference,
at any sample size. The direct, load-bearing consequence: **the floor
threshold itself is a structural UNDERESTIMATE of the true noise scale**
whenever common-mode contamination is present. An underestimated threshold
makes the RESOLVED test (`|pattern[bin]| >= floor`) *easier* to pass — the
natural risk this creates is a **false RESOLVED** (a bin clears an
artificially low bar and reads as "distinguishable from noise" when it
is not). It does not, by this mechanism, create a risk of **false
UNRESOLVED**: a bin that fails to clear an already too-low floor would fail
an even higher, common-mode-corrected floor by an even wider margin — if
anything, common-mode contamination in the floor's own construction makes
an UNRESOLVED call for that bin *more* certain, not less.

**The Result section's Interpretation paragraph applies this concern to
the wrong side.** Both PHOTONICS-named bins came out UNRESOLVED-BY-
CONSTRUCTION this cycle. The Result text states: "though PHOTONICS' own
unclosed common-mode-blindness concern (Idealizations) means this
instrument cannot rule out a real but common-mode-masked effect at either
bin." As a hedge on two UNRESOLVED calls specifically, this does not follow
from the mechanism the DISCLAIMER itself names (floor underestimation) —
that mechanism's own direction, worked through explicitly above, would if
anything *reinforce* confidence in an UNRESOLVED verdict, not undermine it.
A logically distinct, second mechanism — a common-mode-symmetric artifact
directly suppressing the bin's own raw magnitude reading (not the floor
estimate), which could in principle mask genuine small-amplitude signal at
that specific bin — could support the stated hedge, but this is a different
claim from the one the DISCLAIMER text actually makes (which speaks only to
the floor's own construction), and NOTES.md never states or derives this
second mechanism anywhere. As written, the Interpretation conflates "the
floor-estimation procedure cannot see common-mode noise" with "the bin's
own raw reading could be common-mode-suppressed" without bridging the two —
a real precision gap in exactly the load-bearing prose surrounding a
verbatim-quoted DISCLAIMER, which is squarely inside my charter's audit
lane this cycle.

**Severity, stated plainly:** non-outcome-reversing and non-fatal. Item
1c/1d is explicitly informational only (Fix 2's own reasoning, correctly
applied elsewhere in this document); no scored constraint or classifier
verdict depends on this specific sentence. The document's own bottom-line
finding — "PHOTONICS' own 'real shape structure' reading is not
corroborated by the one instrument built this cycle to test it, and the
honest disposition is genuinely open, not resolved either direction" — is
independently defensible on other grounds (the instrument's own disclosed
K=3/median house-style-convention status alone is sufficient to justify
"genuinely open," without needing the common-mode argument at all). But the
specific sentence invoking common-mode-blindness for these two UNRESOLVED
bins does not correctly track the mechanism the same document's own
DISCLAIMER names, and should not be repeated or cited forward without
correction — exactly the kind of gap this program's own "same-shift
annotation" convention (R4/R9-lineage) exists to fix cheaply, not a
Checkpoint-grade defect.

## 4. Other checks performed

- **Named-bin/bin-count arithmetic**: independently recomputed from
  `results.json` directly (not trusted from Result prose): r=156
  `n_resolved` sums to 203/288 (70.5%), r=312 to 222/288 (77.1%) — exact
  match to NOTES.md's own figures. Both named bins (`-146.25°`/`168.75°`,
  margin=32) confirmed `resolved: false` in `results.json["r*"]
  ["named_bin_status"]` directly — matches the Result prose exactly.
- **Reproduction figures** (item 1a): `results.json`'s own
  `reproduction_precondition.widths` at both r match the pre-registered
  279.6607/560.1989 (r=156) and 588.0218/1191.3259 (r=312) to <1e-4
  absolute — NOT FALSIFIED, confirmed from primitives.
- **Predictions-before-run house discipline**: `git log`/`git diff` between
  the Phase-3 synthesis commit (`cdca7fa`, 15:29:57) and the Phase-4-
  complete commit (`e59aa03`, 17:43:29) confirms the entire Predictions/
  Setup/Idealizations block is byte-identical across both commits — only
  the Result section and downstream files changed. Predictions were
  genuinely frozen before the first real `Sim.run()` call (`chunk_runner.
  py`'s own commit lands at 15:53:45, after the freeze).
- **R26 forward-cross-reference discipline** (adopted last cycle,
  exp-109): scanned every "below"/"above"/"see NOTES" forward reference in
  NOTES.md — all five resolve to real content at the point referenced
  (Idealizations' items (a)/(b); the Predictions/Result quoted blocks). No
  dangling promise found, unlike exp-109's own founding R26 instance.
- **RT-7 self-caught citation slip** (my own Phase-2 finding): confirmed
  folded into ordinary copy-editing as Red Team's audit specified —
  `analyze.py`'s real identifiers (`pattern_delta[m]`/`pattern_peccored[m]`/
  `pattern_hollow[m]`) now match what §0.5 of the (unrevised) Phase-1
  proposal should have said; no residual inconsistency found in the
  executed code.
- **Checkpoint status**: confirmed no new criterion fires. R24's own
  Iteration-85 firing remains open pending Marsh's ruling, correctly
  untouched by this document (Tier-0 item 0, explicitly out of scope).

## 5. Verdict on this cycle's Combined Verdict claim: **CONFIRM-WITH-GAPS**

Not a dispute, not PARTIAL. The substantive claims independently checked
above — all 8 mandatory fixes genuinely implemented, R23 discipline
genuinely (and now byte-exactly) honored, T1 correctly N/A, predictions
frozen before the run, the trust suite genuinely green (live re-confirmed,
41/41/79s), Checkpoint criteria correctly non-firing — all hold up under
independent re-derivation, several by live re-execution rather than source
reading alone. This is materially the cleanest R23/governance execution
this document family has produced. But "PROMISING," stated without
qualification, does not account for the real (if non-fatal) interpretive
gap in §3 — a hedge that invokes the DISCLAIMER's own named mechanism in a
direction that mechanism does not actually support. A Phase-5 finding that
survives independent re-derivation and concerns the prose immediately
surrounding a verbatim-quoted DISCLAIMER is squarely load-bearing for my
charter's audit duty this cycle, even though it does not touch any scored
verdict.

## 6. Ranked top-3 candidate directions for Iteration 88

1. **Same-shift-style annotation correcting §3's misapplied hedge**, plus —
   substantively — **execute the already-queued Idealizations item (b)**
   (the symmetric/common-mode synthetic fault-injection case for `mirror_
   pooled_floor`, Fix 2's own deferred half). This is the one instrument
   that would let a future cycle actually know whether RESOLVED calls under
   this floor are trustworthy (the mechanism §3 identifies as the real risk
   direction) — cheap, zero-FDTD, already scoped, and directly resolves the
   ambiguity my finding surfaces rather than merely re-wording it.
2. **PHOTONICS' own recommended independent, non-differencing floor check**
   (a `cpl`-refinement spot check) at the two specific named bins
   (`-146.25°` r=156, `168.75°` r=312) — the only instrument that can
   actually settle whether these two bins carry genuine angular-pattern
   structure or pure discretization noise, since this cycle's own
   mirror-floor diagnostic, even pooled, is structurally unable to answer
   that question either way (§3).
3. **Idealizations item (a)** (the asymmetric synthetic fault-injection
   case, already planned) run alongside item (b) above, completing the
   Iteration-88 fault-injection control R25's own discipline requires as a
   single, explicit, non-parenthetical queue line — both halves together,
   not one without the other, since Red Team's own §2 analysis established
   they close genuinely independent defects (a bias vs. a variance/
   correlation problem) that neither substitutes for the other.

No RULED OUT (R1–R26) idea is re-proposed or re-litigated above.
