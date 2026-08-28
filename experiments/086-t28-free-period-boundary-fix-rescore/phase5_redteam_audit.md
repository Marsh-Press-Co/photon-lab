# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 63 · exp-086

*Fresh context. Received: `phase1_proposal.md` → all five Phase-2 blind
critiques → `phase2_redteam_audit.md` → `phase3_synthesis.md` → all Phase-4
scripts/results (`phase4_rescore.py`+results,
`phase4_null_calibration_rerun.py`+results,
`phase4_null_calibration_controlled_comparison.py`+results,
`phase4_prior_citation_audit.py`+results,
`phase5_supplementary_multiseed_check.json`) → `NOTES.md` → all six Phase-5
blind reviews (PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM, VISION).
Read PANEL.md in full and LOGBOOK.md lines 1–380 (RULED OUT R1–R11) and
426–4117 (LIVE THREADS, the complete T28 arc Iterations 46–62 including both
Checkpoint 52/54 entries and the Iteration-61 Checkpoint in full, and every
prior Red Team Phase-5 final audit's own precedent reasoning for when
criterion 4 fires vs. not). Also read the actual source fix in both
`pad_round_trip_model.py` and `y_wall_prescreen.py`, and exp-085's own
`phase5_redteam_audit.md` as the format/rigor bar. Every load-bearing claim
below — the six reviews' own, and this audit's own — is independently
re-derived from primitives (source code, committed JSON, and fresh
from-scratch Python re-implementations run in this session), not adjudicated
by tallying seats.*

## 0. Scope note

Zero-FDTD, model-internal instrument-repair/re-score desk cycle on shared
period-search machinery (`free_period_with_widening`/`_quiet`, three call
sites across two files). No absorption mechanism is proposed and no
constraint-3 scene is touched anywhere in the record — confirmed directly
(the committed diff at `f256d70` touches only the post-loop `chosen`-selection
fallback in three functions; nothing else). Matches every T28 desk cycle
since exp-069. **Checkpoint criterion 2 (mechanism-class boundary) is N/A**
— see §4.

## 1. Independent primitive-level re-derivation performed

### 1.1 Baseline reproduction

`phase4_rescore_results.json` re-read and independently re-executed (not
accepted from NOTES.md's prose): `classification_a="NOT STABLY PERIODIC"`,
`method_c_rescore.frac_recovered=21/37=0.5675675675675675`, boundary set
`θc∈{45.0,59.0,61.0,63.0,71.0,73.0}` (6/37), `spearman_stride_phases` =
phase 5°→`ρ=0.8571428571428573, p=0.023809523809523808`; phase 7°→
`ρ=0.42857142857142866, p=0.3535714285714286`; phase 9°→
`ρ=0.5357142857142858, p=0.2357142857142857`; `null_pass_rate=13/37=0.3514`.
All match NOTES.md and every seat's own citation exactly. This is now (at
minimum) the **fifth** independent computation of these figures (Phase 1,
Red Team's Phase-2 from-scratch reimplementation, the committed Phase-4
pipeline, four of six Phase-5 reviews' own re-derivations, and this audit).

### 1.2 The R11 fix itself — re-verified correct at all three sites, from source

Read `pad_round_trip_model.py` lines 353–440 (`free_period_with_widening_quiet`
and `free_period_with_widening`) and `y_wall_prescreen.py` lines 322–378
directly, not any seat's paraphrase. All three use the identical, correct
Python `for...else` idiom: the `else` clause (resetting `chosen` to the
**last** stage's own record, `converged=False`/`no_interior_optimum=True`)
fires if and only if the loop completes without ever executing `break` — i.e.
exactly when every stage was `at_boundary`. A genuine interior optimum still
wins as soon as found (`break` after tagging `converged=True`), unchanged
from before the fix. **Confirmed algebraically sound and minimal, matching
R11's own text and every seat's independent claim** — this is now at least
the sixth independent trace of this same logic across this cycle's record
(Phase 1, all five Phase-2 critiques, Red Team's Phase-2 audit, four Phase-5
reviews, this audit).

Git history independently confirms process discipline: `55fe35e` (Phase-1
proposal) precedes `f256d70` (the Phase-4 source fix + Method C re-score +
prior-citation audit commit) in `git log`, and `39363f3` (Phase-3 synthesis
with frozen predictions) sits strictly between the two — predictions
committed before the corrected code ran, as claimed.

### 1.3 Finding (a) — PHOTONICS: amplitude heterogeneity in the recovered set + audit scope-description mismatch. **INDEPENDENTLY CONFIRMED, both halves, exactly.**

Recomputed directly from `phase4_rescore_results.json::method_c_rescore.
sub_results` (not from any seat's prose): applying the frozen "recovered"
criterion (`converged==True ∧ p_local_corrected≤6.0° ∧ r2_local≥0.30`) to
all 37 rows reproduces the 21-window set exactly, and its `ptp` field spans
`2.5577×10⁻⁴` (θc=5°) to `0.125762` (θc=57°):

```
ratio = 0.125762 / 0.00025577 = 491.70576939657576
```

**Confirmed to the printed digit** against PHOTONICS'/Red Team's own
"491.7×"/"~5000×" figures (the latter is the full-37-window figure, not the
recovered-only one — both are independently correct, different
denominators). Twenty of the 21 recovered windows sit in a contiguous
near-normal cluster (θc=5°–43°); the sole exception, θc=57°, sits flanked on
both sides by confirmed boundary-pinned windows (59°/61°/63°), at an
amplitude three orders of magnitude above the near-normal bulk. The uniform
`r2_local≥0.30` bar cannot and does not distinguish these two physical
regimes — a real, previously-undetected (because `ptp` was not persisted
until this cycle's own mandatory fix 5 delivered it) heterogeneity inside
what the classification code treats as one homogeneous "recovered" set.
Does not change `classification_a` (`frac_recovered=0.568` fails the
`≥0.80` gate regardless of internal homogeneity) — correctly assessed by
PHOTONICS as non-outcome-determining, forward guidance rather than a
correction.

**Scope-description mismatch, independently re-verified by direct execution,
not by reading any seat's claim about it.** I ran the committed glob
myself:

```python
glob.glob("experiments/07[7-9]-*/*.json") + glob.glob("experiments/08[0-5]-*/*.json")
# -> 18 files, spanning experiments 077-085 exactly
```

`phase4_prior_citation_audit_results.json::files_scanned=18` — bit-exact
match. But `phase1_proposal.md`'s own table (§2, "Prior-citation audit
scope" row) explicitly names **21 files across 069–085**, including named
069–076 files; `phase4_rescore.py`'s own docstring (line 23) repeats
"experiments 069-085"; and `NOTES.md`'s own **Setup** section (line 51)
states "committed JSON in experiments 069–085" while its own **Result**
section, four paragraphs later, correctly states "experiments 077–085" —
**NOTES.md is internally self-contradictory on its own audit's scope**,
independently of any external claim. The actually-implemented script
(`phase4_prior_citation_audit.py`)'s own docstring correctly and
consistently states "077-085," matching what it executes — the discrepancy
is entirely a Phase-1/Phase-4-driver-docstring/NOTES.md-Setup framing
artifact, not a defect in the audit script itself. **The narrower actual
scope is substantively justified**: `free_period_with_widening` is
independently confirmed absent from experiments 069–076 by TWO separate
methods from TWO separate seats — THERMODYNAMICS' Phase-2 function-name
grep (`grep -rl "free_period_with_widening" experiments/069-076/` → zero
files) and MATERIALS' Phase-5 direct-JSON `at_boundary`-key grep across all
13 committed JSON files in that range → zero occurrences — independently
re-run by me a third time with the identical zero result. **No citation is
at risk from this gap**; it is a self-citation/documentation-precision
defect (the same class as this cycle's own Red Team-caught "Tier-1 items
(1)–(5)" title mislabel at Phase 2 — that one was caught and fixed before
Phase 4 ran; this one was not caught until Phase 5, independently by
PHOTONICS, MATERIALS, and THERMODYNAMICS all three).

### 1.4 Finding (b) — MATERIALS: bit-identical controlled comparison, 10/201 mechanism trace, 069–076 scope confirmation. **INDEPENDENTLY CONFIRMED, all three parts, via a fourth, from-scratch reimplementation.**

Wrote my own independent Python reimplementation of both the pre-R11
`free_period_with_widening_quiet` (old-buggy) and the corrected version,
loading `_free_period_search` directly from `experiments/069-.../run.py`
(a different import path than either of exp-086's own two scripts or
MATERIALS' own reimplementation), and ran both against the real
`pad_round_trip_results.json::real_delta_pad`/σ at N=3000/seed=7:

```
n_boundary_pinned:            201        (matches 201/3000=6.70% exactly)
n_diff (old vs new r² differ): 10        (matches MATERIALS' "only 10" exactly)
max abs diff among differing:  0.19385
old_max_r2:                    0.5179691995509128
new_max_r2:                    0.5179691995509128   (bit-identical)
```

**Confirmed exactly, digit for digit, on max_r2_over_trials, and confirmed
the mechanism MATERIALS traced**: of 201 all-stage-boundary trials, only 10
report a different R² between the narrowest and widest stage at all — the
other 191 pure-noise curves converge to the identical low-`p` edge fit at
both the `[1,4]°` and `[1,15]°` windows, so the bug is frequently a
no-op even when it technically fires. The largest differing value found
(my own independent trace: the pairwise |Δ|, not MATERIALS' own "largest
value on either side" framing — the two are different quantities, both
correct) is nowhere near the 0.518 ceiling set by a genuinely-converged,
non-boundary trial. **This is now the fourth independent confirmation of
the "negligible effect" finding at seed=7/N=3000** (the committed script,
MATERIALS' own from-scratch reimplementation, PHOTONICS' independent
re-execution, and this audit).

069–076 exclusion re-confirmed a third time (see §1.3 above) — MATERIALS'
own claim stands exactly.

### 1.5 Finding (c) — EM: `shape_r_squared_*` independence, `period_refute`/`shape_refute` table, passivity untouched. **INDEPENDENTLY CONFIRMED from raw JSON.**

Read `pad_round_trip_results.json::verdict_pad`/`verdict_absorb40`/
`verdict_two_wall_pad`/`verdict_two_wall_absorb40` directly:

```
verdict_pad:            period_refute=True,  shape_refute=True,  REFUTE
verdict_absorb40:       period_refute=False, shape_refute=False, INCONCLUSIVE
verdict_two_wall_pad:   period_refute=False, shape_refute=True,  REFUTE
verdict_two_wall_absorb40: period_refute=False, shape_refute=True, REFUTE
```

**Bit-exact match to EM's own table.** Two of the three cited REFUTEs
(`two_wall_pair_pad`, `two_wall_pair_absorb40`) are driven by `shape_refute`
alone (`period_refute=False` in both); `pair_pad` has both true, but since
`shape_refute` alone suffices for REFUTE, the R11 bug — confirmed absent
from the `shape_r_squared_*` call chain by EM's own direct source trace,
and confirmed never fired historically on any of these four citations'
`chosen` records (all `at_boundary:false`, per EM's own read) — could not
have altered any of the three currently-cited REFUTE verdicts even had it
never been fixed. Director's Phase-3 clarifying finding under fix 2 stands,
independently re-derived from the primary JSON, not merely re-read from the
synthesis document. The committed diff (`git show f256d70`) touches only
the two functions' post-loop fallback — `reflection_coefficient`,
`n_profile_exact`, `verify_symmetric_damping`, and all three
passivity/lossless/reciprocity gates are untouched, confirmed by direct
diff inspection.

### 1.6 Finding (d) — THERMODYNAMICS: exemption sentence, timing figures, understated bit-identity, two minor findings. **INDEPENDENTLY CONFIRMED, including the precision-understatement.**

Grepped `NOTES.md` directly: the energy-interception exemption sentence
appears twice (Idealizations and Next), matching the frozen Phase-3
language. Re-parsed `phase4_null_calibration_controlled_comparison_results.
json::old_buggy.max_r2_over_trials` and `::corrected.max_r2_over_trials` as
Python floats and compared them directly: **`0.5179691995509128 ==
0.5179691995509128`** — Python's `==` on the raw floats returns `True`,
confirming bit-for-bit (not merely 4-decimal) identity, exactly as
THERMODYNAMICS found. The script's own `conclusion` field text ("IDENTICAL
to 4 decimal places") is read directly from
`phase4_null_calibration_controlled_comparison.py` line 124 — confirmed
verbatim, a genuine, if harmless, understatement of the script's own result.

The two minor findings (the broken "see Idealizations" cross-reference —
independently re-read, `NOTES.md`'s Idealizations section indeed never
mentions the N=3000-vs-60,001 scope reduction anywhere; the scope-mismatch
already covered in §1.3) are both confirmed present and both correctly
rated non-blocking by THERMODYNAMICS.

### 1.7 Finding (e) — QUANTUM: stride-phase reproduction + single-seed gap, closed by an 8-seed replication and a Director-run 2-seed follow-up. **INDEPENDENTLY CONFIRMED, all parts.**

Re-derived the stride-phase table from raw `sub_results` via a from-scratch
Python re-implementation of the recovered-set filter and an exact
permutation test at phase 5° (7!=5040 permutations enumerated,
rank-permutation method, a *third* independently-coded method after the
script's own and QUANTUM's own value-permutation method):
`ρ=0.8571428571428573`, `120/5040` permutations meet `|ρ|≥0.8571-1e-12` →
`p=0.023809523809523808` — **bit-exact** match to both the committed script
and QUANTUM's own independent enumeration. Confirmed: phase 5° clears the
proposal's own falsification band (`|ρ|>0.75` AND `p<0.05`); phases 7°/9°
do not; the choice among the three pre-registered, equally-valid phases is
genuinely outcome-determining, correctly disclosed as such
("PHASE-DEPENDENT — not a single robust verdict"), not resolved by picking
one.

**The single-seed gap, independently assessed as real.** NOTES.md's Result
section (written before QUANTUM's Phase-5 review) states the fix has
"negligible" effect based on ONE seed=7/N=3000 comparison. QUANTUM's own
8-seed/N=1200 replication (9,600 total pure-noise trials, ~591 boundary
instances) found `max_r2_over_trials` bit-identical between old and
corrected logic at every one of 8 seeds, with the single largest observed
boundary-pinned R² jump (0.188, seed 11) still far below the ~0.50–0.53
ceiling set by genuinely-converged trials. I additionally read the
**Director-run supplementary check** (`phase5_supplementary_
multiseed_check.json`, timestamped after all six Phase-5 reviews per the
git log) that ran two further seeds (13, 42): both bit-identical between
`old_buggy`/`corrected` (`0.682874857872476` and `0.4611874862210992`
respectively, matched at both seeds to full float precision). **The
substantive "negligible effect" conclusion is now corroborated across 10
independent seeds by two independently-coded implementations (this cycle's
own script, QUANTUM's reimplementation) plus a Director-run follow-up — a
genuine structural fact, not a one-seed coincidence.** But — and this is
the point QUANTUM's own review makes and this audit independently
agrees with — **the record as filed at Phase 4 asserted this as settled on
one seed**, and the multi-seed corroboration that actually earns the
"negligible"/"cleaner, more decisive" language did not exist until Phase 5.
This is a genuine, real gap between what NOTES.md claimed and what the
committed record at the time supported — closed, but only by this Phase-5
layer, not by the cycle that made the claim.

### 1.8 Finding (f) — VISION: caveat carry-forward correct; Learned-section scope erosion confirmed, unresolved as of this record. **INDEPENDENTLY CONFIRMED, both halves.**

Grepped the shipped `NOTES.md` directly for the instrument-reliability
caveat: present twice (Predictions §3, Result), both bound directly to the
`classification_a` line, not floated separately — confirmed correctly
delivered, matching VISION's own finding.

**The Learned-section erosion, re-read verbatim from the committed file**:

> "the boundary-pinning bug, despite firing at a real 6.70% rate, has
> negligible effect on the specific statistics that underwrite 'the real
> oscillation is not noise'"

Cross-checked against `phase4_null_calibration_rerun.py` lines 54–58 (its
own top-of-file comment, read directly): *"Only pair_pad: exp-077's own
committed `null_calibration_appendix` is a single top-level key, computed
once against `real_delta_pad`, not per-pair."* **Confirmed: this leg's
null was computed only against `pair_pad`'s own noise floor; `pair_absorb40`
is never touched by any Phase-4 script in this cycle** (grep-confirmed:
zero occurrences of `real_delta_absorb40` in any of the three Phase-4
Python files). The Learned section's unqualified "the real oscillation"
therefore reads, to a reader who has not opened the Python source comment,
as covering the REFUTE-cited oscillation family broadly (`pair_pad`,
`two_wall_pair_pad`, `two_wall_pair_absorb40`) — one level of generalization
beyond what was actually tested, the exact R9/T16 shape (a scope qualifier
that lives only in code, silently widened one level up in prose). **As of
the record I was handed, this has NOT yet been corrected** — unlike
PHOTONICS'/MATERIALS' findings (both already resolved by the persisted
`ptp`/`ss_tot_full` fields and the multi-seed replications respectively,
requiring no further NOTES.md edit), this one requires an actual prose
change that has not happened yet. See §6 for the exact fix, applied as part
of this audit's own mandatory-fix docket.

### 1.9 New finding, this audit's own — Method A's promised re-fit was never executed; the resulting NOTES.md claim is correct but unverified in this cycle's own record

`phase1_proposal.md`'s own §6 Phase-4 plan states step (e): *"re-fit Method
A's persisted curve through the corrected function (curve unchanged, fit
re-run)."* Checked `phase4_rescore_results.json`'s own top-level keys
directly: `['fast_eval_verification', 'method_c_rescore', 'classification_a',
'circular_shift_null_all37', 'spearman_stride_phases', 'elapsed_s']` — **no
`method_a` key, no re-fit `P_wide`/`R²_wide`, anywhere.** Grepped all three
committed Phase-4 scripts for `method_a`/`classification_b`/`P_wide`/
`c_wide`: **zero occurrences in any of them.** The promised step was
silently never implemented. `NOTES.md` line 158 nonetheless states
*"`classification_b` unaffected either way, confirmed"* — a claim this
cycle's own record does not actually substantiate by any re-run.

**Independently checked whether the claim is nonetheless true.** Read
exp-085's own `derivation_results.json::method_a.stages` directly: a
**single-element** array, `window="narrow[1,4]", at_boundary=False` — Method
A's own fit found an interior optimum at the very first stage and never
widened. Since the R11 fix only changes behavior in the `else` branch that
fires *only* when the loop exhausts every stage without breaking, and
Method A's loop broke at stage 1, **the fix is a mathematical no-op on
Method A's own P_wide by construction — re-running it would reproduce
`P_wide=3.2556390977443606°` bit-identically, not merely "probably."**
Method B (`P_fft`) is a separate FFT computation that never calls
`free_period_with_widening` at all. So `classification_b` (built by
comparing these two) is provably, not merely plausibly, unaffected —
**the underlying claim is correct**, but it was never independently
re-verified inside this cycle's own committed record; it is asserted, not
shown.

This is exactly the same failure shape as LOGBOOK's own Iteration-53/exp-076
precedent (a promised inline re-confirmation step never actually invoked by
`run.py`, "retroactively confirmed harmless" because the check is
provably data-independent) — ruled non-firing there for the identical
reason this finding should be ruled non-firing here (§3, below): the gap is
real, was not caught by any of the five blind Phase-2 critiques, Red Team's
own Phase-2 audit, or any of the six Phase-5 reviews, but the claim it
concerns is independently verifiable as true from already-committed data,
and is being caught and closed in this very document, before LOGBOOK.

## 2. Reconciling the six readings

All six Phase-5 verdicts are **PARTIAL**, and every load-bearing claim in
every review is independently confirmed above, not merely tallied. No
review's finding is overridden. Three genuinely new items surfaced this
cycle that no earlier phase caught (PHOTONICS' amplitude-heterogeneity +
scope-description mismatch; QUANTUM's single-seed gap, since closed by
replication; VISION's Learned-section scope erosion, not yet closed) plus
one this audit adds (§1.9, Method A's unexecuted re-fit). None of the four
changes `classification_a`, the Combined Verdict, or any currently-cited
T28 headline number outside this cycle's own scope. The one item still
**open** at the moment this audit is written is VISION's finding (§1.8) —
every other new finding is either non-actionable forward guidance
(PHOTONICS' amplitude-heterogeneity check, this audit's own Method-A trace)
or already closed by within-cycle replication (QUANTUM's gap, closed by its
own 8-seed check plus the Director's 2-seed follow-up).

## 3. Checkpoint criterion 4 — does anything here fire it?

**Ruling: does NOT fire — a close call, reasoned through explicitly against
this program's own established distinguishing test, conditioned on the
mandatory-fix docket (§6) actually landing before/alongside this entry.**

This program's own pattern, re-derived from the 13 prior firings
(Iterations 49, 50, 52, 54, 61) versus the non-firing precedents
(Iterations 51, 53, 55, 58, 59, 60, 62 — exp-085 itself), is whether a
defect **enters a defended, committed, permanent record uncaught by that
cycle's own review layers**, later requiring a subsequent cycle to reverse
a citation already resting on it, versus being **caught and corrected
within the same cycle's own review process, before the Director writes the
LOGBOOK entry**.

Applying that test to each of this cycle's four findings:

1. **The scope-description mismatch (§1.3, PHOTONICS/MATERIALS/
   THERMODYNAMICS).** A real, undisclosed inconsistency (NOTES.md
   contradicts itself between its own Setup and Result sections). Not
   caught by five blind Phase-2 critiques or Red Team's own Phase-2 audit
   despite both reading the target scripts closely (Red Team's Phase-2
   audit even caught an analogous, smaller self-citation defect — the
   "Tier-1 items (1)–(5)" title mislabel — in the same document). Caught,
   independently, by three blind Phase-5 seats before any LOGBOOK entry
   exists. **No citation is corrupted** — the actual executed scope
   (077–085, 18 files) is substantively correct, confirmed by two
   independent 069–076 exclusion checks. Matches the non-firing shape
   exactly: real defect, first-time, blind-caught, same-cycle,
   non-load-bearing, before LOGBOOK.

2. **The single-seed gap in the null-calibration comparison (§1.7,
   QUANTUM).** NOTES.md's "negligible"/"cleaner, more decisive" language
   was written on one seed's evidence — genuinely under-supported at the
   moment it was filed. But it was caught, independently, by QUANTUM's own
   blind Phase-5 review, which itself supplied an 8-seed replication
   before this audit ever ran, and a Director-run supplementary 2-seed
   check landed on top of that — all still inside Phase 5, before any
   LOGBOOK entry. The corrected, multi-seed-corroborated conclusion is the
   SAME conclusion NOTES.md filed (negligible effect) — unlike several
   prior T28 firings (e.g. Iteration 61's leg (a), which reversed from
   SUPPORT to INCONCLUSIVE), nothing here needs reversing, only
   re-evidencing. This is arguably an *easier* non-firing case than
   exp-085's own precedent (Iteration 62), where the filed classification
   ("STRONG COHERENT CHIRP") was flatly wrong and had to be overturned by
   the audit, yet still did not fire.

3. **Method A's unexecuted promised re-fit (§1.9, this audit's own
   finding).** A real promise-vs-delivery gap in the Phase-1 proposal's own
   Phase-4 plan, undetected through Phase 2, Phase 3, Phase 4, and all six
   Phase-5 reviews — caught only by this final audit. This is the single
   least-caught finding this cycle (caught later in the process than any
   of the other three), which weighs toward the firing side of the
   ledger. But it is directly, provably non-outcome-determining: Method
   A's own committed `stages` array shows a single-stage, non-boundary
   optimum, making the R11 fix a mathematical no-op on this exact quantity
   by construction, independently verified in §1.9 from already-committed
   exp-085 data, not argued informally. This matches LOGBOOK's own
   Iteration-53/exp-076 precedent precisely (a promised-but-unexecuted
   inline check, "retroactively confirmed harmless" because
   provably data-independent) — a named, on-point non-firing precedent for
   this exact shape, not merely a general pattern-match.

4. **VISION's Learned-section scope erosion (§1.8).** The one finding this
   cycle that is **not yet closed** as of the record handed to this audit
   — caught blind at Phase 5, but the one-line NOTES.md correction it
   calls for has not been applied. This is the closest any finding this
   cycle comes to the T16/R9 firing shape (a scope caveat silently
   widened one level up in prose) — the distinguishing fact that keeps it
   on the non-firing side is that **T16/R9 fired because the flawed
   comparison had already been written into a permanent LOGBOOK entry and
   survived a full cycle boundary before a second seat caught it**; here,
   the erosion lives only in this cycle's own NOTES.md, has not yet
   reached LOGBOOK, and is being caught and closed in this very document.
   **This condition is not automatically satisfied — it requires the
   mandatory fix in §6 item 1 to actually be applied to NOTES.md, and the
   Iteration-63 LOGBOOK entry to carry the corrected, `pair_pad`-scoped
   language, not the as-filed sweeping claim.** If either of those does not
   happen, this finding converts from a close non-firing call into a clean
   T16/R9-shaped firing on the next Phase-5 audit that catches it — the
   same conditional structure exp-085's own audit used for its own
   corrected classification (a).

**Net ruling**: none of the four findings, individually or combined, rises
to Checkpoint criterion 4 — each is caught within this same cycle's own
review layers before any LOGBOOK entry exists, matching this program's own
established non-firing pattern, PROVIDED the §6 mandatory-fix docket
(the NOTES.md one-line correction, the scope-description reconciliation, and
a Method-A closing note) is applied before or alongside this entry, and the
Iteration-63 LOGBOOK text itself carries the corrected framing rather than
the as-filed one — exactly the same conditioning language exp-085's own
audit used for its own corrected reading of classification (a).

**A governance observation, not a new rule**: this is the fourth
consecutive T28 cycle (exp-081, 082, 083 gave the git-provenance/causal-label
family of close calls; now exp-086) where multiple genuinely independent
near-misses are caught and closed inside a single cycle's own Phase-5 layer
without any one of them individually clearing the firing bar. The pattern
itself is healthy (PANEL.md's own design working at high sensitivity, per
Iteration 53's own language) but is now dense enough, four cycles running,
that a future cycle stacking five or six such near-misses simultaneously
should not assume non-firing follows automatically from this precedent —
each case must still be reasoned through on its own facts, as done here, not
pattern-matched from the count of prior non-firings alone.

## 4. Checkpoint criterion 2 — mechanism-class boundary

**Ruling: N/A, reasoned explicitly, matching exp-085's own §4 ruling and
every T28 desk cycle since exp-069.** This is instrument-repair/record-
hygiene work on already-committed, model-internal search machinery — no
absorption mechanism is proposed, no constraint-3 scene exists anywhere in
this cycle's own scope (confirmed: zero article-loaded FDTD calls anywhere
in any of the three Phase-4 scripts), and nothing bears on T1's escape-route
taxonomy. Widening criterion 2 to cover instrument-quality findings would
blur it into criterion 4's own territory (R11's own precedent for this
exact reasoning) and is not warranted by anything in this cycle's record.

## 5. Combined Verdict

**PARTIAL** — unanimous across all six blind Phase-5 seats and this final
audit, matching every T28 desk cycle since exp-069. The R11 repair is
genuine, correctly and minimally applied at all three affected call sites,
and is now independently re-verified at least six separate times across this
cycle's own record. exp-085's own filed "STRONG COHERENT CHIRP"
classification is reconfirmed, by the automated corrected pipeline itself
(not a hand audit), to not survive — `frac_recovered=21/37=0.5676` fails the
shared `≥0.80` gate cleanly, `classification_a="NOT STABLY PERIODIC"`,
correctly carrying exp-085's own instrument-reliability caveat forward. The
overlap-corrected Spearman test correctly surfaces (not resolves) a genuine
phase-dependence in the near-normal-quarter significance question — one of
three pre-registered, equally valid alignments clears significance, the
other two do not; reporting all three, rather than any single one, is the
correct discipline. The quiet-variant sibling's bug is now fixed at the
source (not merely audited) and its "negligible effect on exp-077's
null-calibration statistics" conclusion, under-evidenced at one seed when
first filed, is now genuinely, robustly corroborated across 10 independent
seeds by two independently-coded implementations plus a Director-run
follow-up. No currently-cited T28 headline number is corrupted (the prior-
citation audit finds only the same two already-known-inert instances,
exp-078/exp-079). T28's own founding substantive mechanism question — the
`P_edge_A`/`~2.84°`-family periodicity's ultimate physical origin — is
untouched by this cycle, exactly as intended (Checkpoint criterion 2
correctly N/A). Checkpoint criterion 4 does not fire, conditioned explicitly
on the §6 docket landing before/alongside this entry.

## 6. Mandatory-fix docket for close-out (before/alongside this entry —
binds the Checkpoint-4 ruling in §3)

1. **Correct `NOTES.md`'s Learned-section scope erosion (VISION's finding,
   §1.8) — the single highest-priority item, should happen this cycle, not
   be queued.** Replace:

   > "has negligible effect on the specific statistics that underwrite 'the
   > real oscillation is not noise'"

   with (materially equivalent wording acceptable):

   > "has negligible effect on the specific statistics that underwrite 'the
   > real **pair_pad** oscillation is not noise' — this leg's null was
   > computed only against `pair_pad`'s own `real_delta_pad`/σ
   > (`phase4_null_calibration_rerun.py`'s own explicit scope comment);
   > `pair_absorb40`'s own noise floor was never recomputed at any N this
   > cycle."

2. **Reconcile the "21 files, experiments 069–085" vs. "18 files,
   experiments 077–085" scope-description mismatch (§1.3, PHOTONICS/
   MATERIALS/THERMODYNAMICS).** Correct `phase1_proposal.md`'s §2 table
   row, `phase4_rescore.py`'s docstring line 23, and `NOTES.md`'s Setup
   section (line 51) to state the actually-executed scope — "experiments
   077–085, 18 files; experiments 069–076 independently confirmed absent
   of `free_period_with_widening` occurrences by two separate grep methods
   (THERMODYNAMICS' Phase-2 critique, MATERIALS' Phase-5 review), out of
   scope by construction" — matching what `phase4_prior_citation_audit.py`'s
   own docstring already correctly states. House convention: flag/correct
   this cycle's own still-open documents; do not rewrite exp-085's own
   closed file.

3. **Add one closing sentence on Method A (this audit's own finding,
   §1.9).** State in `NOTES.md` (Result or a new "Verified, not re-run"
   note) that Method A's own promised re-fit through the corrected machinery
   was not executed this cycle, and that `classification_b`'s
   "unaffected either way" claim rests on a direct, independently-verifiable
   structural fact — exp-085's own committed `derivation_results.json::
   method_a.stages` shows a single-stage, non-boundary (`at_boundary:
   False`) interior optimum, meaning the R11 fix cannot alter `P_wide` by
   construction, and Method B (`P_fft`) never calls the fixed function at
   all — rather than leaving the bare word "confirmed" unqualified.

4. **Persist, or explicitly disclaim, the 10-of-201-differ mechanism trace
   (MATERIALS'/this audit's own finding, §1.4) somewhere in the committed
   record** — currently exists only in two Phase-5 reviews' own prose and
   this audit, not in any JSON. Cheap, non-blocking, but the kind of number
   a future cycle citing "negligible effect" should be able to re-derive
   from committed data rather than re-run from scratch a third time.

None of these four changes any frozen prediction, `classification_a`, the
Combined Verdict, or any currently-cited T28 headline number outside this
cycle's own scope.

## 7. Reconciled ranked priority list — ALL open items across all six
reviews plus this audit's own findings, for LOGBOOK's Iteration-64 queue

**Tier 0 — close out THIS cycle, zero cost, before the LOGBOOK entry is
written** (not an Iteration-64 item; a precondition for it):

0. The four-item mandatory-fix docket, §6 above.

**Tier 1 — zero-FDTD, near-unanimous across all six seats, Iteration 64's
own top priority**:

1. **A dedicated, cheap, zero-FDTD validity check of
   `edge_diffraction_c_empty_corrected` at grazing incidence (θc≳45°)** —
   ranked #1 or #2 by PHOTONICS, MATERIALS, EM, THERMODYNAMICS, QUANTUM,
   and named by VISION: does the bare Kirchhoff-Huygens sum (traced by
   PHOTONICS to its defining primitives, `design_geometry.py::field_and_h`/
   `_src_amp`/`_geom_derived` — no Fresnel-transition or UTD-style
   shadow-boundary correction term anywhere in the chain) remain inside its
   own valid near-field regime where `ptp` grows 5,444×–6,631×? This is the
   single most consequential open item this cycle's own data surfaces: it
   gates whether ANY future classification built on Method C's
   grazing-angle sub-windows (including the sole recovered θc=57° point,
   itself amplitude-comparable to the confirmed blow-up) is physically
   meaningful at all — not merely a fit-quality question.

2. **Adopt a formal multi-seed replicate requirement for "negligible
   effect on a tail/order statistic" claims** (QUANTUM's own proposal,
   §1.7, closing the exact gap this cycle's own Prediction-6 language
   exposed at one seed) — recommend as a new standing rule, **R12**,
   in the spirit of R6/R6-addendum's own "one run is not a proof" lineage,
   extended here from significance tests against a constructed null to
   comparisons of a code fix's effect on an order statistic: *before a
   claim that a fix/change has "negligible"/"materially unchanged" effect
   on a tail statistic (max, min, an extreme percentile) computed from a
   finite noise sample is reported as settled, it must be corroborated
   across multiple (≥5–8) independent seeds/draws, not a single matched-seed
   comparison however exact.* This cycle's own 10-seed corroboration
   (QUANTUM's 8 + the Director's 2) already satisfies what this rule would
   require — transcribe both the rule text and this cycle's own compliance
   into LOGBOOK at Iteration 64.

3. **Complete the still-queued full-scale (60,001-call) `null_calibration_
   appendix` re-run** — named by every seat, substantially de-risked (bug
   and fix bit-identical across 10 seeds so far) but not yet executed at
   the scale exp-077's own cited REFUTE framing used. **Reconciliation, this
   audit's own synthesis**: run it in two parts, not one — (a) a single
   N=60,001 run at the SAME seed exp-077's own citation implicitly used (for
   an apples-to-apples update of the exact cited figure), AND (b) fold it
   into the R12 multi-seed protocol above rather than treating one large-N
   run as sufficient evidence on its own — a large single N does not by
   itself satisfy the multi-seed requirement R12 names, since it is still
   one draw of the order statistic.

**Tier 2 — the board's most overdue standing items, strongest cross-seat
consensus of any single item this cycle**:

4. **The joint EM/THERMO energy-interception cross-check** — now FOUR
   consecutive cycles deferred/exempt (083/084/085/086), SEVEN cycles since
   first named (Iteration 59), per THERMODYNAMICS' own sharper accounting
   (§8 of her review). Every deferral so far has been legitimately
   scene-less-exempt and correctly documented as such — but the "next
   scene-bearing cycle" scheduling mechanism has, as THERMODYNAMICS notes,
   quietly become no mechanism at all, since every other queued T28 item is
   also currently zero-FDTD. **Forward tripwire, adopted by this audit,
   extending THERMODYNAMICS' own recommendation**: Iteration 64 must either
   (i) make a minimal, purpose-built article-loaded scene the explicit
   Tier-0 item specifically to discharge this check, or (ii) if judged
   genuinely low-value until a substantive mechanism candidate exists,
   retire the "next scene-bearing cycle" framing explicitly and say so. **A
   fifth consecutive deferral without one of these two actions fires
   Checkpoint criterion 4 automatically**, matching R6–R11's own "known,
   named, ignored" escalation format — this audit names the tripwire now,
   consistent with how R11 itself was pre-announced one cycle before it
   would have applied.

5. **The x-wall wavelength-generality leg** — now ELEVEN consecutive cycles
   deferred (076–086, independently reproduced by VISION and this audit:
   `086−076+1=11`), the single oldest item on the whole T28 board.

**Tier 3 — standing, lower-priority items, carried forward unchanged**:

6. PHOTONICS' domain-truncation test for leg (b)'s Anchor 2, and/or EM's
   matrix-valued RS/Kirchhoff kernel rebuild.
7. The near-null σ(I) article follow-up, still not run.
8. QUANTUM's lossless-PEC-only-disk control, still not run.
9. The ritualization governance question named at Iteration 61 (does the
   R6–R10/R11 escalating-tripwire format need a scope-applicability
   clause?) — still not resolved, not urgent.

**Tier 4 — governance, this cycle's own**:

10. Checkpoint criterion 2 ruled N/A, reasoned explicitly (§4).
11. Checkpoint criterion 4 ruled non-firing on all four matters adjudicated
    (§3), conditioned explicitly on the Tier-0 docket (item 0 above) landing
    before/alongside this LOGBOOK entry.
12. This is the fourth consecutive T28 cycle with multiple dense,
    individually-non-firing Phase-5 near-misses (§3's governance
    observation) — named, not yet a pattern requiring a new rule, but worth
    tracking if a fifth cycle recurs.
