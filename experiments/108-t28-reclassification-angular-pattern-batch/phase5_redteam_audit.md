# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 85 (exp-108)
## "The Two-Cycle-Old Reclassification Fix, R25/R23 Governance Rulings, and a Bundled `angular_scattered_pattern`/Absolute-Floor/Suite-Stage Batch"

Red Team seat, fresh context. Received: PANEL.md, LOGBOOK.md in full
(RULED OUT R1–R25 verbatim, ESTABLISHED, LIVE THREADS), PLAN.md's
Vision/Current-state, this cycle's complete record (`phase1_proposal.md`,
all five `phase2_critique_*.md`, `phase2_redteam_audit.md`, `NOTES.md`,
`results.json`, `run_output.txt`, `run.py`, `chunk_runner.py`,
`analyze.py`, `reclassify_106.py`, the patch to
`experiments/106-.../run.py`, `lab/validation/run_all.py`'s new
`stage26_chunked_run_identity()`), and all six blind Phase-5 reviews. Every
load-bearing claim below was re-derived from primitives myself — not
trusted from any seat's restatement, including my own Phase-2 self's.

---

## 0. Independent re-verification from primitives

**0.1 The three named zero-FDTD scripts, re-run fresh this shift, against
the raw pickled captures still on disk in this session's scratch
directory (not merely re-read from `results.json`).**

```
$ python3 reclassify_106.py
NEW: THREE-WAY-AMBIGUOUS (REFUTES-electrical-thickness-growth-hypothesis
nominally per shape_ratio_fixedabs bands; p_abs_frac_diff=0.1231(r156)/
0.1796(r312) exceeds 0.10) (NOT-TRUSTED -- r=312 MARGINAL/unsettled)
```
Bit-exact match to NOTES.md's Result section and `results.json`. All other
fields (`shape_ratio_fixedabs=18.228333623646076`, `noise_dominated=
False`, `trusted=False`) bit-identical to exp-106's own committed
`results.json`, confirmed by direct diff.

```
$ python3 analyze.py
r156: item_i=CONFIRM, item_ii=CONFIRM residual_std=2.8972e-06, item_iii=0.1827 pass
r312: item_i=CONFIRM, item_ii=CONFIRM residual_std=2.1022e-06, item_iii=0.2525 pass
```
Exact match, both r, all fields, against `run_output.txt`/`analyze_output.json`.

```
$ python3 lab/validation/run_all.py --only 26
2/2 checks passed: positive control max|diff|=0.000e+00, negative control
relative deviation 2.000
$ python3 lab/validation/run_all.py --only 12346789
41/41 checks passed
```
Both exact matches; trust suite green, confirmed fresh, not accepted from
the transcript.

**0.2 `git show` on the actual commit (`fdfa6c6`) diffing
`experiments/106-.../run.py`.** The patch is real, substantive, and
matches the specified shape exactly: `classify_shape_ratio_fixedabs()` is
extracted as a standalone, importable, module-level function (Attack 1's
own remedy, option (a)), called both by the file's own inline
classification block and imported directly by `reclassify_106.py` — one
function, one name, zero duplicated logic. `git show fdfa6c6 --stat`
confirms exp-106's own `results.json` is byte-unchanged (11 files touched,
none of them `experiments/106-.../results.json` or
`experiments/106-.../NOTES.md`) — **this is genuine, git-tracked,
independently-diffable evidence that R25's own tripwire fix was actually
executed, not merely described a third time.**

**0.3 PHOTONICS' own low-cross-section local-normalization finding,
independently re-derived from the raw phasor captures myself (not
accepted from the review's own numbers).** Wrote a standalone script
against the six retained `.pkl` captures, recomputing
`angular_scattered_pattern` at margin=32 for both articles at both r and
comparing local- vs. global-normalized deviation:

```
r=156: 30/48 bins (62.5%) carry <1% of peak scattered power.
       local-rel-deviation max = 9.88% (at bin -146.25 deg)
       global-normalized max(rel32) = 1.476e-4  (matches results.json exactly)
r=312: 30/48 bins (62.5%) carry <1% of peak scattered power.
       local-rel-deviation max = 10.88% (at bin +168.75 deg)
       global-normalized max(rel32) = 1.527e-4  (matches results.json exactly)
```

**Exact match to PHOTONICS' own self-review figures (62.5%/62.5%,
9.88%/10.88%), independently reconstructed from primitives, not merely
re-read.** This is the single most consequential number in this cycle's
own record and I confirm it is real, not a restatement error.

**0.4 EM's and QUANTUM's `classify_item_ii()` finding, independently
re-derived.** `run.py:187-193`:

```python
def classify_item_ii(r, residual_std):
    boxA = DELTA_BOXA[r]
    if residual_std <= 0.5 * boxA: return "CONFIRM", boxA
    if residual_std >= boxA: return "REFUTE", boxA
    return "AMBIGUOUS", boxA
```

Confirmed by direct read: the function's own signature takes only `(r,
residual_std)` — no `fit` dict, no `smooth`, no `r_squared` anywhere in
its body or its two call sites (`analyze.py:85`). `results.json`'s own
persisted `fit` objects: r=156 `r_squared=0.6654, is_monotonic=False,
smooth=False`; r=312 `r_squared=0.0205, is_monotonic=False, smooth=False`
— **at neither r does the fit clear the file's own `R2_SMOOTH_THRESHOLD
= 0.90` bar or the monotonicity test**, confirmed by direct constant
read (`run.py:70`). Contrast `classify_item_i()` (`run.py:196-250`),
which explicitly gates its REFUTE branch on `fit["smooth"]`
(`run.py:240`, `if fit["smooth"]: smooth_run_found = True`) — the
identical diagnostic, computed by the identical function
(`linear_fit_1_over_margin`), applied to one sibling classifier and not
the other, in code built together in the same Phase-3 synthesis.

**0.5 QUANTUM's/PHOTONICS' "floor-cleared bin" finding, independently
re-derived.** `grep -n "floor" run.py analyze.py` returns exactly one
functional hit: `sc_floor_gate_window()` in `analyze.py`, used only for
item iii's numerator floor-gate on `g["behind"]` — a completely different
quantity (RMS-normalized grid-cell intensity in a downstream window) from
item i's per-bin `σ_scat_per_bin` array. `analyze.py:73`
(`item_i = R.classify_item_i(pattern_delta, pattern_peccored, r)`) passes
the raw, unmasked 48-bin arrays straight from `angular_scattered_pattern()`
into the classifier. `classify_item_i`'s own docstring
(`run.py:198`, "floor-cleared mask applied upstream") describes a step
that does not exist anywhere in the call chain. Confirmed independently.

**0.6 The "annotated, not overwritten" claim re: exp-106's own
`NOTES.md`.** `grep -n "108\|Iteration 85\|THREE-WAY-AMBIGUOUS"
experiments/106-t28-kappa-window-floor-fixedabs-control/NOTES.md` returns
**zero hits**. `git show fdfa6c6 --stat` confirms `experiments/106-.../
NOTES.md` is not in the commit's changed-file list at all. NOTES.md's own
Idealizations claims "historical `results.json`/`NOTES.md` there are
annotated, not overwritten" — `results.json` is correctly, accurately
untouched (the true half); `NOTES.md` was **neither annotated nor
overwritten** — only `run.py` received the three disclosed comment
blocks. QUANTUM independently found the identical gap; I confirm it from
source myself.

**0.7 R25/R23/R24 registry text, re-grepped directly against
LOGBOOK.md.** R25's entry (~997–1038) opens exactly "proposed and
ratified by Red Team's own Phase-5 final audit, Iteration 84" — confirmed;
this cycle's "ratify" line is correctly bookkeeping. R23's entry (908–944)
and R24's entry (945–996) match every quotation this cycle's documents
attribute to them. Confirmed structurally, independent of any seat's
restatement.

**Constraint-3 structural check, independent of the proposal/critiques/
prior audit's own claim.** `grep -rniE "C_thr|ambient|Weber|coherent|
entangle|nonclassical" experiments/108-.../*.py lab/validation/run_all.py`
(the new stage26 addition) returns zero hits outside seat-name labels.
**T1/constraint-3 is N/A throughout, confirmed structurally, independent
of every prior layer's own claim.**

---

## 1. Adjudication of the six Phase-5 reviews

**PHOTONICS (self-review) — ADOPT in full.** Every reproduction claim
independently re-verified (§0.1–0.3, §0.6 above). §3a (floor-clearing
never implemented), §3b (global-max normalization structurally blind to
62.5% of bins), §3c (item ii's detrend ungated for fit quality), §3d
(the smooth-migration discriminator itself has zero positive control)
are all confirmed from source, independently, by me. §2c's own citation
self-correction (exp-016/017, not exp-059/060) is confirmed by direct
LOGBOOK grep — I checked all four instances the review names and they
match. This is the most load-bearing review of the six and I adopt every
finding without qualification.

**MATERIALS — ADOPT in full.** The T9-anchor citation-fix survival check
(§3) and item-ii/Babinet-ceiling consistency check (§4) both
independently re-derive cleanly. The core finding (§2 — item i's CONFIRM
is a real, appropriately-scoped fabrication-tolerance finding that was
never translated into MATERIALS' own charter language) is correct,
non-load-bearing to any verdict, genuinely additive. I note explicitly:
MATERIALS' own three scope caveats (scale/regime/profile-specificity, §2
items 1–3) do not name the observer-angle concern I raise independently
below (§2, this document) — a gap in MATERIALS' own review, not a wrong
finding, folded into my own new attacks.

**ELECTROMAGNETISM — ADOPT in full.** §2's `classify_item_ii` gap and
§4's stage26 negative-control asymmetry (only the under-reported-
`steps_done`/over-run direction is tested, not the over-reported/
truncation direction) are both independently confirmed (§0.4 above for
the first). The `closure` energy-bookkeeping analysis (§3) is sound and
matches my own independent read of `radial_absorbed_power`'s docstring
("EMPIRICAL closure," not an exact identity).

**QUANTUM OPTICS — ADOPT in full.** Independently reproduces
`classify_item_ii`'s gap by an entirely independent from-scratch
re-implementation of `linear_fit_1_over_margin` (normal equations, not
`numpy.linalg.lstsq`) — I re-checked this arithmetic myself and it is
correct. The item-i floor-clearing gap (§2, second finding) is confirmed
independently (§0.5 above). Both are ruled correctly non-outcome-
reversing (the raw, undetrended statistic also clears item ii's CONFIRM
bar at both r; testing all 48 bins is a superset of a floor-cleared
subset for item i) — I re-verified both of these secondary claims myself
and they hold.

**THERMODYNAMICS — ADOPT in full; no override.** The cleanest of the six
reviews — CONFIRM, not CONFIRM-WITH-GAPS. I independently re-derived the
30.9%/46.3%/≥117× figures from `experiments/107-.../results.json`'s own
`item3_rows` by the review's own two independent methods (direct
percentage; the quadratic-`σ_ext`-scaling cross-check) and both reproduce
exactly. §5's own process observation (the figure lives only in prose,
never wired to an assert) is correctly ruled non-load-bearing given
triple independent re-derivation on record. No finding of mine
contradicts or extends this review.

**VISION SCIENCE — ADOPT in full; this is this cycle's second
most-consequential review.** §2b's `build_result_text()`-never-called
finding and §2c's zero-`assert` finding are both independently
reconfirmed by me: `grep -rn "build_result_text" .` (excluding
`__pycache__`) returns exactly one functional hit — the definition at
`run.py:312` — plus prose mentions in NOTES.md/phase1_proposal.md/this
review; zero call sites. `grep -n "assert" run.py analyze.py
chunk_runner.py reclassify_106.py` returns **nothing**, confirmed. `grep
-c "predictions_text\|result_text" results.json` returns **0** — no such
field exists, confirmed. VISION's own §4 non-firing ruling (this is a new
sub-shape of the standing R23 gap, not a repeat of any prior named
instance) is correct and I adopt it without modification — but see §3
below for how this interacts with NOTES.md's own Result-section language.

**No review is overridden. All six are independently re-verified from
primitives and adopted in full — a genuinely clean six-of-six this
cycle, unlike several recent cycles that required a partial override.**

---

## 2. New defects, beyond what the six reviews found

**Attack 1 — [inconsistency] Item i's own "floor-cleared bin" language
is not merely unimplemented (QUANTUM's finding) but dimensionally
INCOHERENT as specified — a future "fix" that literally builds the
described mask would be a category error.** Item ii's own "absolute
floor" is a single scalar per r: `residual_std` of a 6-point fit on
`Δ(abs_ext_ratio)`, a dimensionless-ratio quantity. Item i's own
per-bin quantity is `σ_scat_per_bin`, a cross-section-like array in
entirely different units, indexed by angle, not by margin. There is no
coherent way to use item ii's own scalar floor as a per-bin mask on
item i's angular array — PHOTONICS' review names this (§3a) but frames
it primarily as a missing wire-up; I rule it one level deeper: the
ORIGINAL Phase-1 proposal's own Predictions table (§4, "every one of the
48 bins that clears the item-ii absolute floor") is where this
incoherent cross-reference was first written, and it survived five blind
Phase-2 critiques and my own Phase-2 Red Team audit — none of which
caught that the two "floors" do not share units — into NOTES.md's frozen
Predictions table (Tier 1, item i) verbatim. **Non-load-bearing** (the
executed test, unmasked, is a strict superset and the CONFIRM survives),
but should be corrected in the record so no future cycle tries to build
the described mask as literally specified.

**Attack 2 — [inconsistency, R4-class] The Combined Verdict's own
self-description — "the cleanest cycle in the R20/R21/R23/R24/R25
lineage to date" — is contradicted by this document's own §3 ruling,
below.** Filed here as its own numbered attack because it is a claim
about THIS cycle's own place in a named historical lineage, frozen in
NOTES.md's Result section, that does not survive contact with the
governance ruling this same audit reaches two sections later. See §3/§4.

**Attack 3 — [constraint-#2/#3-adjacent risk, preventive, not a
violation this cycle commits] PHOTONICS' own normalization blind spot
(§0.3) sits precisely in the angular region constraints 2 and 3 care
about most, and no review names this explicitly.** Item i's CONFIRM is
structurally insensitive to shape differences in the 62.5%-of-bins
low-cross-section sectors — the side- and back-scatter directions. This
program's own phenomenon target cares specifically about those
directions: constraint 2 ("no specular return to the observer") and
constraint 3 ("not a black silhouette... only the swept beam reveals
it") both concern what an off-axis or ambient-lit observer sees, not the
forward-scatter lobe a beam continues into. **This cycle correctly makes
no constraint claim** (T1: N/A, confirmed §0.7) — nothing is quietly
dropped here. But MATERIALS' own recommended future citation ("the
backing/core material is angularly... optically free") could, if a later
cycle drops MATERIALS' own three explicit caveats (scale/regime/
profile), be misread as licensing a claim about observer-relevant angles
specifically — the one angular region this instrument cannot see by
construction. Filed as a forward-looking guard, matching Red Team's own
charter duty to watch for constraint 3 quietly slipping in a LATER
citation of a currently-honest finding, not as a defect this cycle
commits.

**Attack 4 — [minor, non-load-bearing, R4-class] A second wording
imprecision in the same Idealizations sentence QUANTUM already flagged
(§0.6): "annotated, not overwritten" implies action was taken on BOTH
named files; only one of two was touched.** Filed as its own numbered
attack (distinct from QUANTUM's own finding, which names the gap without
tagging it) to make explicit this is an R4-class citation defect
(a claim about what was done to a named source that does not reproduce
against `git show --stat`/direct grep) for the purposes of the R20 tally
in §3.

---

## 3. The EM/QUANTUM/PHOTONICS root-cause synthesis — one defect, or several?

**Ruling: two distinct root-cause defects, not one and not three — and
one of the two is a clean SECOND INSTANCE of an existing rule (R24),
firing Checkpoint criterion 4 automatically.**

**Defect A — the specification (not merely the code) for item i's own
normalization convention is structurally insensitive to the region of
the angular domain that matters most, and this was never stress-tested
against real data before Phase-3 freeze.** PHOTONICS' finding (§0.3):
`rel32 = |Δpattern| / max_bin(σ_scat_per_bin[PEC-cored])` — a GLOBAL,
not local, normalization — was correctly *implemented* exactly as
*specified*, at every phase (Phase-1 proposal, five Phase-2 critiques,
my own Phase-2 Red Team audit, Phase-3 synthesis). This is NOT a
code-vs-spec gap — the code faithfully executes the frozen formula. It
is a spec-level design choice, chosen at Phase 1 and never independently
checked against the actual per-bin power distribution by any of seven
reviewing layers (five critiques + Red Team's own Phase-2 audit +
Phase-3 Director synthesis) before freeze. This is closer in shape to
R17 (a tolerance/bracket/window not justified against comparable
established data before the run) than to R20/R24 — a different failure
species, correctly not counted toward either tally below.

**Defect B — item ii's own smoothness-gate is a clean second instance of
R24's own named pattern.** Re-read R24's operative text directly
(LOGBOOK.md ~945–996): *"a Phase-2 mandatory fix's own specified
consequence or decision rule, once a Phase-3 synthesis states it was
'adopted in full,' must be implemented as a binding element of whatever
classification or verdict string it was written to gate — not merely
computed and left as an unscored, disclosed observation... a future
cycle that ships a Phase-3 'adopted in full' claim whose own
mandatory-fix consequence later proves not to have been coded, when
that consequence's own trigger condition is met by the data, fires
Checkpoint criterion 4 automatically on a SECOND instance."*

Checked element-by-element, from primitives, not from either critique's
own framing:

1. **A Phase-2 mandatory fix specifies a consequence/decision rule.**
   `phase2_redteam_audit.md` §3, mandatory fix 4 (folded from EM+QUANTUM):
   *"Item ii's noise floor: before reporting raw std..., report whether
   the sequence is monotonic (or fits a smooth `1/margin`-type trend)...
   **If it is**, report the residual-from-fit std... as the genuine
   floor."* An explicit if/then consequence, textually on record.
2. **Phase-3 synthesis states it was adopted in full.** NOTES.md's own
   Phase 2→3 synthesis, verbatim: *"Disposition of the five blind
   critiques (Red Team's own ruling...): all five ADOPTED, unconditionally,
   none overridden... Director adopts this combination **in full**,
   below."* Confirmed by direct re-read, not paraphrase.
3. **The consequence was never coded — merely computed and left as an
   unscored, undisclosed observation.** Confirmed at §0.4 above:
   `classify_item_ii(r, residual_std)` never reads `fit["smooth"]` or
   `fit["r_squared"]`, anywhere. Worse than R24's own founding instance
   in one respect: there, the trigger field (`p_abs_frac_diff`) was at
   least *printed* to stdout even though unwired; here, `smooth`/
   `r_squared` for item ii are persisted in `results.json` but **never
   printed or mentioned anywhere in `run_output.txt` or NOTES.md's Result
   section at all** — not even as a disclosed, unscored observation.
4. **The consequence's own trigger condition is met by the data.**
   `smooth = is_monotonic OR r_squared ≥ 0.90`. At r=156: `is_monotonic=
   False`, `r_squared=0.665` — smooth=False. At r=312: `is_monotonic=
   False`, `r_squared=0.021` — smooth=False. **The "not smooth" trigger
   — which, on the mandatory fix's own "if it is [smooth], report the
   residual-from-fit as genuine" logic, should have withheld the
   "genuine floor" framing — is met at BOTH r, and the code ignores it
   at both.** NOTES.md's own Result section calls both r's readings
   "the genuine, detrended floor... not merely informally decisive" —
   language the fit's own persisted diagnostic does not support at
   either r, most starkly at r=312 where the fit explains 2% of the
   six-point sequence's variance.

**All four elements of R24's own text are satisfied, on a channel R24's
own founding instance never touched (`classify_shape_ratio_fixedabs`
vs. `classify_item_ii` — different functions, different documents,
same underlying failure shape: an "adopted in full" if/then consequence
never wired into the classification/verdict logic it was written to
gate).** R24's own forward-elevating clause is explicit and unconditional
on this point: a second instance "fires Checkpoint criterion 4
automatically" — it does not carry a materiality/load-bearing exception
(R24's own founding instance fired no exception for load-bearing-ness
either; it simply fell short of firing because it WAS the founding
instance). **I rule this a genuine second instance. See §4.**

**Does Defect A also combine into Defect B, making one root cause of
three findings?** No — I considered this carefully, as the task brief
invited. Defect A (item i's normalization) is a spec-level choice
correctly implemented; Defect B (item ii's gate) is a spec-level
promise NEVER implemented. These are the mirror image of each other,
not the same defect: one is "the code does what a flawed spec says";
the other is "the code does NOT do what a sound-on-its-face spec
promised." Grouping them as one defect would blur a distinction this
program's own rule taxonomy (R17 vs. R24) already exists to keep
separate. I decline to merge them, and file them as two named findings
above (§2 Attack 1 for a third, related-but-distinct incoherence issue
in item i's OTHER gap — the floor-clearing mask — which is itself a
third species again: a promise that is not merely unimplemented but
impossible as literally stated).

---

## 4. Ruling on Checkpoint criterion 4

**FIRES — via R24's own forward-elevating clause, second instance,
independent of R20's own tally.**

I evaluated all five relevant standing rules explicitly, not by
inertia:

- **R20** (three-or-more R4-class citation/figure defects surviving
  Phase-3 freeze into Result/Learned, each caught only at Phase 5):
  **tally = 2** — PHOTONICS' own exp-059/060 mis-citation (§1, adopted;
  survived into NOTES.md's frozen Hypothesis section) and the
  "annotated, not overwritten" inaccuracy re: exp-106's own `NOTES.md`
  (§0.6/Attack 4, this document). Both are clean R4-class instances
  (a citation/claim that does not reproduce from its own cited source).
  Short of "three or more" — **R20 does NOT fire on its own tally.**
  (Item ii's "genuine, detrended floor" narration and item i's "could
  have found a real angular signature and did not" overclaim are NOT
  counted toward this tally — neither is a wrong citation or figure;
  both are correctly-computed numbers given an unsupported interpretive
  label, a different failure shape, addressed under R24/Defect A above,
  consistent with this program's own "ruled once, not twice" counting
  discipline and with how R24 itself was distinguished from R20 at its
  own founding.)
- **R21** (a persisted byproduct field's own headline finding never
  stated in Result prose, third occurrence fires automatically): the
  `fit["smooth"]`/`fit["r_squared"]` fields ARE persisted-but-unnarrated
  in exactly R21's own shape. I considered firing R21's own forward
  clause here as well, and decline to: this is the identical underlying
  code gap R24 already fires on, and firing two separate rules'
  strike-counters on one code defect would double-count a single root
  cause — this program's own R20/Iteration-50 "ruled once, not twice"
  precedent governs here by direct analogy, even though it was written
  for a different rule. **R21 is not independently fired; the gap is
  fully accounted for under R24.**
- **R23** (disclaimer-erosion lineage): VISION's own finding (§1,
  adopted) is a genuinely new sub-shape (a claimed dual-pipeline
  compliance where only one half — `build_predictions_text()` — is
  ever exercised, while `build_result_text()` is dead code), not a
  repeat of any of R23's three prior named instances. R23 carries no
  forward-elevating clause at all (confirmed by direct re-read of its
  own text) — **there is no automatic-fire mechanism for R23 to trip,
  by construction.** This is a real, correctly-adopted finding that
  independently justifies a same-shift correction (§6) but cannot, on
  its own rule's own text, fire Checkpoint 4.
- **R24** (this section's own central finding): **fires, second
  instance, per §3 above.**
- **R25** (queue-item completeness): genuinely, robustly discharged
  this cycle (§0.2; §5 below) — no instance to count, does not fire.

**Checkpoint criterion 4 fires this cycle, via R24's own explicit,
unconditional second-instance clause — the first Checkpoint-4 firing
since Iteration 75 (R19's founding cycle, non-firing) / the last actual
firing in this program's record being Iteration 68 by my read of
LOGBOOK's own section headers, itself worth naming: this is a governance
cycle, purpose-built to demonstrate clean process discipline after
exp-106→107's own R25-founding failure, that itself ships a second
instance of a DIFFERENT named governance rule (R24) in the very same
document that discharges R25. This is not a contradiction in this
audit's own reasoning — it is the finding.**

---

## 5. Ruling on R25's own final status

**R25's founding instance (exp-106→107) is genuinely, robustly
discharged — not merely described a third time.** Independently
confirmed, not accepted from NOTES.md's own claim:

- `git show fdfa6c6 -- experiments/106-.../run.py` shows a real,
  git-tracked, 33-line-net diff extracting `classify_shape_ratio_
  fixedabs()` as a standalone function, exactly matching the patch
  specified in NOTES.md's own Setup section, character-for-character.
- I independently re-ran `reclassify_106.py` from a cold shell this
  shift and reproduced the exact `THREE-WAY-AMBIGUOUS(...)` string
  NOTES.md's Result section quotes inline, bit-exact.
- Every other persisted field (`shape_ratio_fixedabs`, `noise_dominated`,
  `trusted`) is confirmed bit-identical to exp-106's own committed
  `results.json` — the patch touched the classification string only, as
  required.
- NOTES.md's own Result section states, with the string quoted inline,
  that the patch was applied and its output checked — satisfying Red
  Team's own Phase-2 binding conditional (§4 of `phase2_redteam_audit.md`)
  exactly, not merely in spirit.

**R25 itself does not fire** — this is its own founding instance's
successful discharge, the intended, non-failure outcome; there is only
one instance on record (exp-106→107→[closed here]), not a second
violation of R25's own text. **Distinct and unrelated to the Checkpoint-4
firing above**: that firing is via R24 (a different rule, a different
channel — `classify_item_ii`, not `classify_shape_ratio_fixedabs`), and
does not diminish or complicate R25's own clean discharge in any way.
The two governance stories in this single document run in opposite
directions and neither one launders the other.

---

## 6. VISION's `build_result_text()` finding — does it overstate NOTES.md's own claims?

**Yes, confirmed independently (§0/§1 above), and the overstatement is
real, though non-load-bearing to any scored physics verdict.** NOTES.md's
Result section states: *"this cycle's own Tier-1 batch newly invokes the
code-generated pipeline and is genuinely R23-compliant, live-fire-
verified."* The Idealizations section: *"Live-fire-verified, not merely
asserted (§Result, Phase 4)."* Both are **true only for the predictions
half** of R23's own two-function founding contract
(`build_predictions_text()`/`build_result_text()`, exp-104's own
docstring) — `build_result_text()` has zero call sites anywhere in this
cycle's executed path, `results.json` persists no `predictions_text`/
`result_text` field (unlike exp-104's own founding precedent, which
persisted both specifically so the asserted string and the citable
string are the same object), and this cycle carries **zero `assert`
statements anywhere** — a regression below even exp-105's single missing
assert (R23's own second non-firing instance), since exp-105 at least
shipped one of the two founding asserts. The word "pipeline" (singular)
in NOTES.md's own prose does real, unearned work papering over the fact
that only one of its two named halves is ever exercised. This does not
touch R25's discharge (§5, a different subsystem entirely) but IS a real
overstatement of R23's own claimed compliance, correctly caught only by
VISION, and is folded into the same-shift annotations below.

---

## 7. Combined Verdict: **PARTIAL** (revised from NOTES.md's own "PROMISING")

**NOTES.md's own Combined Verdict — "PROMISING... the cleanest cycle in
the R20/R21/R23/R24/R25 lineage to date... no AMBIGUOUS, no FALSIFIED,
no NOT-TRUSTED qualifier anywhere in this cycle's own scored results" —
does not survive this audit and is revised to PARTIAL.** Not RULED OUT
(T1 correctly N/A throughout, no mechanism class foreclosed). Not
PROMISING: Checkpoint criterion 4 fires (§4, a second R24 instance, on a
new channel, inside the very document built to demonstrate clean
post-R25 governance); item i's CONFIRM is real but was overclaimed in
scope (the dominant forward lobe, not "the angular pattern" full stop —
62.5% of the angular domain, by bin count, is structurally untested by
this cycle's own normalization choice); item ii's "genuine, detrended
floor" language is unsupported by the fit's own persisted diagnostic at
either r; the R23 "genuinely... compliant" claim is true for only half
of its own named pipeline.

**Real, disclosed progress nonetheless, and it should be stated plainly
alongside the corrections:** R25's founding instance is genuinely,
verifiably discharged (§5) — a real governance win, the actual intended
outcome of this cycle's own Tier-0 work, and not undone by the Tier-1
findings above. The R23 scope ruling itself (ratify-as-scoped, not
genericize) stands on its own independent cost argument, unaffected by
VISION's finding (§6). Items iii, iv, and `closure` are clean, real,
independently-reproduced results with no gaps found by any of seven
reviewing layers (six Phase-5 seats plus this audit). Item i's CONFIRM
for the dominant, power-carrying part of the scattering pattern (deviations
~300× below the 5% bar) is a genuine, well-supported finding, not
merely salvaged. This is a cycle with real substance on both halves,
undercut by a governance-integrity defect this audit's own charter
exists specifically to catch — not a cycle that produced nothing.

---

## 8. Same-shift fixes applied directly to NOTES.md (annotated, not
silently rewritten — per this program's own exp-105/106/107 precedent)

Applied below, in NOTES.md, each blockquoted and attributed to this
audit, zero re-run, zero verdict-arithmetic change to any scored
CONFIRM/PASS result:

1. Combined Verdict corrected: PROMISING → **PARTIAL**, Checkpoint
   criterion 4 disclosed as firing (R24 second instance), full reasoning
   cross-referenced to this document.
2. Item ii's Result table annotated with `r_squared`/`smooth` values at
   both r and a correction that "the genuine, detrended floor" language
   is not supported by the fit's own diagnostic at either r (most
   starkly r=312, R²=0.02) — the CONFIRM verdict itself is UNCHANGED
   (the raw, undetrended statistic also clears the bar at both r).
3. Item i's Result paragraph annotated: CONFIRM re-scoped explicitly to
   the dominant/forward-scattering lobe; the "could have found a real
   angular signature and did not" sentence flagged as overclaimed
   relative to the global-max normalization's own structural blind spot
   (62.5% of bins by count; local deviations there reach 9.88%/10.88%,
   unassessed against any per-bin floor or REFUTE bar).
4. The R23 "genuinely... compliant, live-fire-verified" claims (Result
   and Idealizations) annotated: true for `build_predictions_text()`
   only; `build_result_text()` has zero call sites; zero `assert`
   statements exist anywhere in this cycle's code; no `predictions_text`/
   `result_text` field is persisted.
5. The "historical `results.json`/`NOTES.md` are annotated, not
   overwritten" sentence annotated: accurate for `run.py`/`results.json`;
   exp-106's own `NOTES.md` was neither annotated nor overwritten.
6. PHOTONICS' own citation corrected in the Hypothesis section:
   `angular_scattered_pattern` was built/gated at exp-016/017, reused
   (not built) at exp-059/060.

---

## 9. Reconciled Iteration-86 queue

**Tier 0 — zero FDTD, governance/closeout, mandatory:**
1. Rule on this audit's own Checkpoint-4 firing at the next convened
   checkpoint (per PANEL.md's continuous-mode protocol) — Marsh
   notification owed per Checkpoint criterion 4's own standing rule.
2. Wire `build_result_text()` into `analyze.py`'s own `__main__` (or an
   equivalent site), restore the two founding `assert DISCLAIMER in ...`
   calls (predictions AND result strings), and persist `predictions_text`/
   `result_text` into `results.json` — VISION's own §6 recommendation,
   adopted, closing this cycle's own R23 evidentiary gap.
3. Gate `classify_item_ii()` on `fit["smooth"]` (or explicitly document,
   in a code comment, why it deliberately is not gated) — the R24
   second-instance fix itself; zero new `Sim.run()` calls, data already
   captured.

**Tier 1 — cheap/adjacent, real physics value:**
1. Re-normalize (or floor-gate) item i's per-bin comparison against each
   bin's own LOCAL magnitude, not the global peak — PHOTONICS' own §6
   recommendation — zero new `Sim.run()` calls, all six margins' full
   48-bin arrays already committed in this cycle's own captures. This is
   the single highest-value item on this queue: it is the only way to
   learn whether the ~10% local deviations in the low-cross-section
   sectors are real shape structure or near-null relative-error blowup.
2. A synthetic positive/negative control for `linear_fit_1_over_margin`'s
   own smooth/noise discriminator (R18 discipline — new classification
   machinery joining an already-verified architecture needs its own
   fault-injection control the same cycle it is added; this cycle's own
   item iv got one, item i/ii's shared discriminator did not) — inject a
   known smooth-migration sequence and a known-noise sequence, confirm
   `smooth=True`/`False` falls out correctly.
3. Extend `stage26`'s own negative control to the symmetric direction
   (`steps_done` OVER-reported, causing early truncation) — EM's own
   finding, one-line addition.

**Tier 2:**
1. A fourth r-point (r=624) to test THERMODYNAMICS' own `r^-1.16`
   fixed-abs projection (~52.6× margin, just above the 50× `box_dev`
   floor) — still standing, unchanged by this cycle.
2. MATERIALS' own recommended one-sentence fabrication-tolerance framing
   for item i's CONFIRM, WITH this audit's own Attack 3 observer-angle
   caveat folded in explicitly (do not let a future citation drop
   MATERIALS' scale/regime/profile caveats or this audit's own
   angular-domain-coverage caveat).
3. Formalize the absolute-floor six-margin family from a
   resolution/aliasing bound (owed since this cycle's own Idealizations,
   not yet done).

**Tier 3 — long-standing, unchanged:**
The oblique-angle extension (now doubly motivated: both by
`angular_scattered_pattern`'s first validated application at r≠78 AND by
the still-open observer-angle question this audit names); the 750/450nm
leg; the `G40` full-width leg; the x-wall admittance refit;
`PAD`-with-article survival; `box_dev`'s own thinning margin (~9.0× at
r=312, a DIFFERENT quantity from this cycle's own noise-floor finding,
still unresolved).

Full record: `experiments/108-t28-reclassification-angular-pattern-batch/`
— Phase-1 proposal (PHOTONICS), five Phase-2 blind critiques
(`phase2_critique_{materials,em,thermodynamics,quantum,vision}.md`),
Phase-2 Red Team audit, Phase-3 synthesis (`NOTES.md`), Phase-4 results
(`results.json`, `run.py`, `chunk_runner.py`, `analyze.py`,
`reclassify_106.py`, `run_output.txt`), six Phase-5 blind reviews
(`phase5_review_{photonics,materials,em,thermodynamics,quantum,
vision}.md`), this Phase-5 Red Team final audit.
