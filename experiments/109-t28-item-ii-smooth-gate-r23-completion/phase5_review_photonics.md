# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 86 (exp-109)

Fresh sub-agent, blind to every other seat's Phase-5 review this cycle. Read
PANEL.md in full, LOGBOOK.md in full (RULED OUT registry R1–R25 read in
full, plus the Iteration-85/exp-108 record and CHECKPOINT block), PLAN.md
lines 25–260, the complete exp-109 record (`phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`,
`results.json`, `run_output.txt`), the actual patched
`experiments/108-.../run.py` and `.../analyze.py`, the new
`reclassify_108.py`, and `git log`/`git show` for the commit sequence.
Independently re-derived every load-bearing number from primitives with a
from-scratch script (not trusted from any seat's — including this cycle's
own — restatement).

## 0. Independent re-derivation from primitives

Re-loaded `experiments/108-.../results.json`'s own `tier1.r{r}.item_ii`
block directly and, from the raw `delta_values` arrays alone, independently
recomputed (a) `np.std(delta_values, ddof=0)`, (b) a from-scratch OLS fit
of `Δ = A + B/margin` by normal equations (not by calling
`linear_fit_1_over_margin`), and (c) `is_monotonic`/`r_squared`/`smooth`:

| r | `raw_std` (mine) | `residual_std` (mine) | `r_squared` (mine) | `smooth` (mine) | matches `results.json`? |
|---|---|---|---|---|---|
| 156 | 5.008327900579266e-06 | 2.89716280726349e-06 | 0.6653735294260243 | False | exact, every digit |
| 312 | 2.1240857290489e-06 | 2.102199273342035e-06 | 0.020501712361515212 | False | exact, every digit |

Both `smooth=False` — the branch this cycle's whole point rests on
genuinely fires at both r, not merely as claimed. `raw_std <= 0.5·|Δ_boxA|`
at both r (margins 2.964× at r=156, 5.810× at r=312) — **CONFIRM/CONFIRM
independently reproduced exactly**, matching `phase1_proposal.md`'s own
frozen table, all five Phase-2 critiques, Red Team's Phase-2 audit, and
`results.json`'s own `item_ii_reclassified` block to <1e-9 relative. The
`raw_over_residual_ratio` figures (1.72870088.../1.010411218...) also
reproduce exactly (1.729×/1.010× as reported).

**The OLS inequality itself** (`residual_std <= raw_std` for any OLS fit
with an intercept column) is a genuine, general linear-algebra fact, not
merely true on these two points: `A_mat=[1,1/margin]` carries an intercept,
so the constant model `ŷ=mean(y)` is a feasible point in the same
least-squares search space, forcing `RSS_opt <= RSS_constant`, hence
(dividing both by the same `n`, `ddof=0` throughout) `residual_std <=
raw_std` always. Confirmed airtight independently, not merely re-typed from
the proposal.

**`classify_item_i()`'s CONFIRM branch, re-traced against
`experiments/108-.../run.py` lines 234–289**: `linear_fit_1_over_margin` is
called exactly once, inside `for (i0,j0) in runs:` (line 276) — unreached
when `runs` is empty. `verdict="CONFIRM"` requires `confirm_all_margins and
not runs` (line 281) — i.e. CONFIRM is only reachable in exactly the case
where the fit/smoothness code path is never entered. Independently confirms
the PHOTONICS-Phase-2-critique/Red-Team finding that the original §4
"item-i's CONFIRM branch is deliberately unconditional on smoothness"
framing misdescribes the sibling code: it is structurally incapable of
facing a smoothness question there, not exempted from one by design.

**Verbatim-quotation requirement (VISION's mandatory fix 6)**: programmatically
diffed the `predictions_text`/`result_text` strings inside NOTES.md's fenced
code blocks against the literal `results.json["predictions_text"]`/
`["result_text"]` values — **byte-for-byte identical** (only difference is
the markdown fence's own stripped trailing newline). Genuinely, not
nominally, satisfied — the strongest of this cycle's six fixes.

**`grep -c assert`**: `experiments/108-.../run.py` = 1 (the restored
`--predictions-only` assert, line 374); `reclassify_108.py` = 3 (module
docstring mention + two live asserts, lines 81/131) — matches NOTES.md's
own claimed counts (≥1/≥2) exactly.

**`analyze.py`'s companion call site** (lines 84–92): the actual file on
disk matches the "exact diff" NOTES.md's own Setup section shows,
verbatim — a real patch, not merely described.

**Zero `lab/` diff**: confirmed via `git diff --stat HEAD -- lab/` (empty)
and clean working tree. Partial independent spot-check of the trust-suite
claim: ran `lab/validation/run_all.py --only 12346789` myself; stages 1–3
passed exactly as this program's baseline expects before I terminated it
for time (no regression signal, consistent with the claimed 41/41, though
I did not reproduce the specific "100s/102s before-and-after" timing
figures from any committed artifact — see §2 below).

## 1. Does `results.json` actually contain everything NOTES.md's Result
section claims?

**Yes, exactly**, at both r: `stat_used`, `raw_over_residual_ratio`,
`old_verdict`/`new_verdict`, and the full `fit` passthrough are all present
in `item_ii_reclassified.r156`/`.r312` and match the quoted `result_text`
prose to the digit. `gate_p0_pass`/`repro_pass`/`n_fdtd_calls`/
`total_wall_s` are genuine top-level keys, independently confirmed against
`experiments/108-.../results.json`'s own `n_fdtd_calls=6`/
`total_wall_s=7712.0` and the four per-r `pass_` booleans (all `True`).
`source_results_json_sha` is a real git blob hash, present. Nothing in
NOTES.md's Result section overstates what `results.json` actually holds.

## 2. Were all six Red Team mandatory fixes actually incorporated in the
executed artifact — not just described? Checked line-by-line.

| # | Owner | Requirement | Verified in code/`stat_source` | Verified in NOTES.md prose |
|---|---|---|---|---|
| 1 | PHOTONICS+RT | Correct §4's item-i-CONFIRM-branch analogy; rest the (b)-rejection on the OLS proof + the original fix's own text | **NOT present** — `classify_item_ii()`'s docstring contains only the OLS proof and the one-sided note (fix 2's content); no mention of `classify_item_i`, its CONFIRM branch, or the original fix's cited line range | **NOT present** — see below |
| 2 | EM | Replace "conservative in every case" with the two-sided statement, in prose AND `stat_source` | ✅ verbatim in the else-branch `stat_source` string | ✅ verbatim in NOTES.md §"six mandatory fixes" item 2 |
| 3 | QUANTUM | Persist + narrate the raw/residual ratio | ✅ `raw_over_residual_ratio` in the return dict and in `stat_source` | ✅ in Result-section prose and the quoted `result_text` |
| 4 | THERMO | State the `gate_p0_pass`/`repro_pass` AND-reduction explicitly, in code AND docstring | Code is an explicit `and` (self-evident) but carries **no comment/docstring** naming it as such — a narrower gap than the literal fix text asked for | ✅ stated explicitly ("explicit AND, fix 4") |
| 5 | THERMO | Add a `wall_time_source` attribution note to `result_text` | ✅ `wall_time_note` threaded through `build_result_text()`, present in the quoted `result_text` | ✅ |
| 6 | VISION | NOTES.md Result section quotes `result_text`/`predictions_text` verbatim, in full | n/a (a NOTES.md-level requirement) | ✅ confirmed byte-for-byte, §0 above |

**Fix 1 is the exception, and it is a genuine, freshly-discovered defect.**
NOTES.md's own "six mandatory fixes" section (lines 56–67) states the
correction will appear "Corrected below (§ 'Why raw std, not forced
AMBIGUOUS')" — **no such section exists anywhere in NOTES.md.** I grepped
the entire document for `AMBIGUOUS`, `structurally incapable`,
`340-347`/`340–347`, and `non-smooth default`: every one of those strings
appears **only inside the mandatory-fixes-summary paragraph itself** (the
promise), never in a body section that actually delivers the corrected
discussion. The `classify_item_ii()` docstring — the one place a reader
would look for it — implements fix 2's content (the one-sided-inequality
correction) but never mentions `classify_item_i`, its CONFIRM branch, "not
a deliberate design choice," or cites `phase2_redteam_audit.md:340-347` as
Red Team's own stronger ground required. The underlying misdescription
this fix exists to correct (in `phase1_proposal.md`'s own §4, a frozen,
unmodified Phase-1 document per this program's "annotated, not
overwritten" convention) is therefore **never actually superseded anywhere
in the executed record** — only promised to be, in a self-reference that
does not resolve to real content.

This is not outcome-reversing (the underlying code change — gating on
`fit["smooth"]`, falling back to raw std — was never justified by the
flawed item-i analogy in the first place; the analogy lived only in
explanatory prose, not in the executed classification logic), and Red
Team's Phase-2 audit itself independently supplied a strictly stronger,
sufficient ground for the same design choice (§0.3 of
`phase2_redteam_audit.md`, the original Iteration-85 mandatory fix's own
text) — so nothing computational is at risk. But it is exactly the shape
this program's own R4/R16/R19/R21/R23/R24/R25 lineage exists to catch: **a
mandatory fix that Phase 3 explicitly claims to have incorporated
("Corrected below") was not, in fact, incorporated anywhere in the frozen
document** — caught here, at Phase 5, not before. Five of six mandatory
fixes are genuinely, verifiably discharged; the sixth is claimed but
absent.

## 3. Any new defect surviving Phase 2 uncaught?

**Yes — the Fix-1 gap above is the headline finding**, freshly discovered
at Phase 5 (not flagged by any of the five blind Phase-2 critiques or Red
Team's own Phase-2 audit, since it is a Phase-3-authorship defect that
postdates all of Phase 2).

**A second, minor process observation**: `git log` shows NOTES.md was
committed for the first and only time in commit `7783f95` — the *same*
commit as `results.json`/`run_output.txt` (Phase 4's own outputs) — not in
an earlier, separate commit establishing the Predictions section before
the run, as PANEL.md's Phase-3 discipline ("predictions committed to git
BEFORE the run — house discipline, non-negotiable") literally asks for.
Substantively low-risk here: the actual falsifiable numeric predictions
(item 4's CONFIRM/CONFIRM table, `stat_used` to <1e-9, ratios to <1e-3)
were already independently pinned in `phase1_proposal.md` (commit
`1a11850`) and re-derived by all five Phase-2 critiques plus Red Team's own
audit — all genuinely committed before Phase 4 — so no post-hoc curve
fitting is plausible for a deterministic, zero-FDTD reclassification of
already-committed arrays. But NOTES.md's own git history does not, by
itself, independently corroborate its "Predictions — committed BEFORE any
Phase 4 execution" section header the way the discipline is meant to
guarantee; a cleaner future cycle would commit the Phase-3 synthesis
(through Predictions/Idealizations) in its own commit before executing
`reclassify_108.py`.

**Fix 4's docstring gap** (§2 above) is minor and non-blocking — the code
itself is unambiguous (`and`), it merely lacks the specific inline
comment/docstring Red Team's fix literally asked for.

## 4. Is VISION's binding "quote verbatim" requirement genuinely
satisfied, or only nominally?

**Genuinely.** Confirmed by direct programmatic diff (§0), not by
eyeballing: the fenced blocks in NOTES.md's Result section are
byte-for-byte identical to `results.json["predictions_text"]`/
`["result_text"]`. This is the strongest-discharged of the six fixes and
closes the specific "human-readable-citation" gap exp-108's own Phase-5
VISION review (§2d) found still open. No paraphrase, no truncation, no
drift between what was asserted-and-persisted and what a reader would
actually see.

## 5. Constraint/T1 scope check

Independently confirmed: every function this cycle touches or adds
(`classify_item_ii()`'s new body, the `--predictions-only` block,
`reclassify_108.py`) is a classification-statistic gate or a
text/persistence pipeline over already-committed scalars — none reads or
writes σ(I), σ(x,t), ε(ω), or a perceptual/Weber-contrast quantity. T1 =
N/A is correctly, structurally true; no constraint-1/2/3/4 verdict is
scored or moved anywhere in this document.

## Verdict: **CONFIRM-WITH-GAPS**

The substantive fix (gating `classify_item_ii()` on `fit["smooth"]`,
falling back to the provably-conservative-against-false-CONFIRM raw `std`)
is real, correctly wired into the executed classification path, and
reproduces exactly from primitives — the R24 second instance is genuinely
discharged, not merely re-narrated a third time. R23's human-readable-
citation half is genuinely, verifiably closed (§4). Five of the six Phase-2
mandatory fixes are truly incorporated, not merely claimed. **The gap**: fix
1 (PHOTONICS + Red Team's own correction of the misdescribed
`classify_item_i` analogy) is asserted as done ("Corrected below") but the
promised corrected section does not exist anywhere in NOTES.md or in the
code — non-outcome-reversing (Red Team's own audit independently supplies
a sufficient alternate ground), but a genuine instance of a mandatory fix
claimed-incorporated-but-absent, caught only now, at Phase 5 — precisely
the failure shape this program's own governance-rule lineage (R4 lineage
generalized: a "corrected below" pointer that does not resolve to real
content) exists to name. A secondary, lower-severity process note: NOTES.md
itself was git-committed in the same commit as Phase 4's own results, not
in a separate prior commit, though the substantive numeric predictions were
independently pre-registered earlier via `phase1_proposal.md` and the
Phase-2 layer.

**Single most important finding**: Red Team's own Phase-2 mandatory fix 1
— correcting a misdescribed sibling-code analogy — was never actually
written into NOTES.md despite being explicitly claimed as "Corrected below
(§ 'Why raw std, not forced AMBIGUOUS')"; no such section exists anywhere
in the document, and the code docstring doesn't contain it either. Five of
six mandatory fixes are genuinely discharged; this one is claimed but
absent — non-outcome-reversing only because Red Team's own audit
independently supplied a sufficient alternate justification for the same
design choice.
