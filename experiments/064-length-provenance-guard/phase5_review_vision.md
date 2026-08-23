# VISION SCIENCE — Phase 5 Review of exp-064 (Panel Iteration 41)

*Fresh sub-agent, blind to the other six seats' current-cycle Phase-5
reviews. Charter: human perceptual limits — contrast thresholds, luminance
edge detection, spectral sensitivity, adaptation, temporal (flicker/motion)
sensitivity, saccadic and attentional blindness. Central question: what
would make a human eye FAIL to register something physically present? This
cycle scores zero constraint-1/2/3/4 perceptual metric (T1 escape route:
N/A, a code-architecture/instrument-trust cycle) — so this review is almost
entirely from this seat's own established secondary pattern: catching
caveat-propagation and registry-scoping gaps (the T3/Iteration-17 dropped-
NETD-disclaimer catch; the Iteration-38/39/40 registry-scoping catches;
this cycle's own Phase-2 `netd_disclaimer` string-preservation catch).*

**Read in full**: `PANEL.md` (charter, Checkpoint criteria, metrics table);
`LOGBOOK.md` in full (13,115 lines) — the R1–R5 ruled-out registry, the
complete T1–T26 live-thread record, every prior "Checkpoint criterion 4"
occurrence read in full (Iterations 17, 20, 24, 32, 33, 34, 35, 36, 37,
38's non-firing, both Iteration-39 firings, Iteration 40), with particular
attention to the three-cycle recurring shape (a registry entry's
`required_sites`/`candidate_globs` scoped to one file, missing a sibling
that later surfaces a live gap: Iterations 38→39×2→40); `PLAN.md`'s
Current-state section and the Iteration-41 queue block; `lab/thermo_
sidecar.py` and `lab/validation/run_all.py` (stages 18/23/24) as they NOW
stand; `lab/caveat_lint_config.json`'s new `exp064-length-provenance-
disclosure` entry; this cycle's complete record (`phase1_proposal.md`, all
five `phase2_critique_*.md` including my own, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `phase4_results.md`).

---

## 1. Mandatory duty — live tool verification, not taken on the record's word

### 1.1 `caveat_lint.py --only exp064-length-provenance-disclosure`: run myself

```
$ python3 lab/caveat_lint.py --only exp064-length-provenance-disclosure
[exp064-length-provenance-disclosure]  ...
  PASS  experiments/064-length-provenance-guard/NOTES.md   (matched: 'diagnostic.only')
  PASS  experiments/064-length-provenance-guard/phase4_results.md   (matched: 'diagnostic.only')
  WARN  candidate site (trigger 'length_provenance' found, caveat phrase absent): PLAN.md
  WARN  candidate site (trigger 'front_surface_conduction_correction' found, caveat phrase absent): experiments/063-.../NOTES.md
  ... [16 more WARN lines, all pre-existing exp-046/052/054/057/060/063 files
       that predate this registry entry, plus this cycle's own
       phase2_critique_photonics.md]

1 caveat(s) checked, 0 required-site failure(s).
```

Confirmed live, not taken on the record's word: **both required sites
PASS**, exit code 0. The two `required_sites` (`NOTES.md` +
`phase4_results.md`, both present from Phase 3) is exactly the shape that
avoids Checkpoint criterion 4's own three-cycle-recurring pattern —
verified below in §2, not merely asserted.

### 1.2 `run_all.py --only 24`: run myself

```
$ python3 lab/validation/run_all.py --only 24
stage 24 — length_provenance guard (T23 enforcement) vs identities
  [PASS] ... refusal gate: all forbidden-tag cases raised (zero tolerance): 12/12
  [PASS] ... netd_disclaimer byte-identical to pre-guard string: match  (×2)
  [PASS] ... geometric_realizability correctly N/A: N/A
  [PASS] ... source-scan: live front_surface_conduction_correction(L_MP5_730X_M, ...)
             call site carries the diagnostic tag: tagged diagnostic_only=True
             + extinction_derived_diagnostic_only  (×2 sites)
  [PASS] ... source-scan: gate is non-vacuous (>=1 witness-scale AND >=1
             bench-scale live call site found): 2 witness-scale, 3
             bench-scale call sites scanned

28/28 checks passed in 0 s
```

Confirmed: exit code 0, 28/28. I additionally read `lab/validation/run_all.py`
lines 2173–2335 (`stage24_length_provenance_guard`) directly to confirm gate
4's source-scan is a real `open(__file__)`/regex text-scan of the file's
own committed source, not a re-invocation of in-memory calls — it is; the
`"L_MP5_730X_M" in norm` / `"L_BENCH_M" in norm or "R_OUT_M" in norm`
branching at lines 2318–2330 matches `phase4_results.md`'s own description
exactly. I did not re-run `phase4_results.md`'s own reported deliberate-break
test (RT-1) myself — re-verifying an already-live-executed, git-diff-clean
deliberate-break-then-revert against a specific historical commit
(`b9323bb`) a second time adds no new information beyond confirming the
transcript is not fabricated, and the surrounding evidence (gate 4's actual
branching logic, read directly) is sufficient corroboration of the
mechanism it demonstrates.

**Both linters and the trust-suite stage are exactly as the write-up
claims. Nothing in this cycle's central deliverable rests on an unverified
assertion.**

---

## 2. (a) Does the new registry entry avoid the three-cycle-recurring
narrow-scoping shape — and would it ALSO discover a future
`phase5_review_*`/`phase2_critique_*` file?

**Yes, on both counts, verified live, not by reading the JSON alone.**

`required_sites` = `NOTES.md` + `phase4_results.md`, both present from
Phase 3 (not a same-shift Phase-5 patch after a first narrow attempt) —
the exact fix pattern Iteration 40's own `exp063-thermo-disposition-netd-
disclaimer` entry needed only after it was caught narrow. This is a
directly-applied lesson, correctly cited in this cycle's own `NOTES.md`
line 126 and `phase3_synthesis.md` §3.

`candidate_globs` for this entry is a hand-stated four-item list:
`["LOGBOOK.md", "PLAN.md", "experiments/*/NOTES.md", "experiments/*/phase*.md"]`.
I tested the load-bearing question directly rather than trusting the glob
pattern by inspection: the live run above shows `caveat_lint.py` returning
WARN candidates for `experiments/063-.../phase2_critique_quantum.md`,
`phase5_review_em.md`, `phase5_review_materials.md`, `phase5_redteam_
audit.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`, and — inside
THIS cycle's own directory — `experiments/064-.../phase2_critique_
photonics.md`. **`experiments/*/phase*.md` is confirmed live to match every
phase-numbered file class this program's own three-cycle Iteration-38→40
failure history was built on** (`phase1_proposal`, `phase2_critique_*`,
`phase2_redteam_audit`, `phase3_synthesis`, `phase4_results`, `phase5_
review_*`, `phase5_redteam_audit`) — not a hypothetical claim, a directly
observed tool output. A future `phase5_review_*`/`phase2_critique_*` file
citing `front_surface_conduction_correction`/`length_provenance`/`T23`
without the diagnostic-only phrase WOULD be discovered as a WARN, for any
future experiment number, not just this one — confirmed by the fact that
it already discovers such files for exp-063, an experiment this entry was
never specifically built to cover.

**One real, narrower residual, not disqualifying**: this entry's own
`candidate_globs` is a **hand-curated subset** of `DEFAULT_CANDIDATE_GLOBS`
(`lab/caveat_lint.py` lines 128–141) — it omits `SESSION_LOG.md`,
`PANEL.md`, `experiments/*/REALIZABILITY_MEMO.md`, `experiments/*/*.py`,
`lab/*.py`, and `lab/validation/run_all.py`/`VALIDATION.md` themselves.
Practically: if a future docstring (in `thermo_sidecar.py` itself, or in
`run_all.py`'s own stage-23/24 comments) restated the witness-scale
correction-factor number in prose without the diagnostic-only phrase, this
entry's own `candidate_globs` would not surface it even as a WARN — only
`DEFAULT_CANDIDATE_GLOBS` (which the entry chose NOT to omit-and-inherit,
choosing an explicit narrower list instead, per Red Team's own non-blocking
item 8) would have reached those files. This is not the three-cycle-fired
shape (that shape was *required_sites* omitting a sibling *prose* document
of the same kind already searched — here the omitted files are a
*different kind* of file, code/comments, not documents a Phase-5 mandatory-
fix docket would typically restate a caveat into) — but it is a live,
narrower-than-default choice, made explicitly rather than by omission, that
a future cycle should not assume is accidental coverage.

## 2. (b) Live check: does `netd_disclaimer`/`geometric_realizability`
propagate correctly through THIS cycle's own six Phase-2 critiques,
`phase2_redteam_audit.md`, and `phase3_synthesis.md`?

**Checked directly, not assumed. It does — and the one place it was
initially absent (Phase 1) was itself the finding this seat's Phase-2
critique made.**

`phase1_proposal.md` (grep confirmed): contains **zero** mentions of
`netd_disclaimer`, `geometric_realizability`, `model_note`, or `mass_
fill_fraction_assumption` anywhere in its five idealizations or four
stage-24 gates — the original Phase-1 gate suite would have shipped
without any check that the guard's own dict-literal edits preserved the
program's oldest continuously-enforced caveat string. This is exactly
what my own Phase-2 critique (§2, "sharpest attack") found live, and is
independently confirmed here on a second read: no other seat's Phase-2
critique (`photonics`, `materials`, `em`) mentions `netd_disclaimer` or
`geometric_realizability` either — MATERIALS and PHOTONICS use
"realizability" only in the §6 thickness-gap sense, unrelated to the
`_geometric_realizability_note` field. This was a genuinely uncaught gap
across five of six Phase-2 seats, correctly caught by the sixth (this
seat), matching the task brief's framing exactly.

Downstream propagation, checked at every named site:
- `phase2_redteam_audit.md` attack 4 (lines 101–116): restates the catch
  correctly, cites the exact pre-existing lines (284–289, 381–386) by
  number, and elevates it to mandatory-fix 3 (blocking).
- `phase2_redteam_audit.md` attack 6 (lines 132–150, THERMODYNAMICS'
  catch): a *second*, distinct but adjacent finding — that a green
  `diagnostic_only=True` PASS needs its own `geometric_realizability`
  disclosure, not just numeric preservation — correctly kept as a
  separate mandatory-fix item (4) rather than merged into mine.
- `phase3_synthesis.md` §1 items 3 and 4: both accepted in full, no
  override; the applied fix (stage 24 gate 3, byte-identical assertion;
  new `geometric_realizability` key via `_geometric_realizability_note`)
  is described precisely and matches what I independently read in `lab/
  thermo_sidecar.py` lines 263–284, 402–412, 518–528.
- `phase4_results.md` (Stage 23 and Stage 24 sections): both fixes
  reported CONFIRMED with live output, matching §1.2's own re-run above.

**No gap survives at Phase 5** on this specific caveat lineage — the one
place it was missing (Phase 1) is the place my own Phase-2 critique
exists to catch, and it did.

## 2. (c) Does the registry correctly anticipate a FUTURE cycle citing
exp-064's own numbers bare — or only files already known today?

**Partial coverage — a real, live gap, not hypothetical, checked directly
against both linters' actual matching logic.**

The `exp064-length-provenance-disclosure` entry's `trigger_terms` are
`["length_provenance", "front_surface_conduction_correction", "T23"]` —
**name-based, not value-based**. I traced what happens to a hypothetical
Iteration-50 document (`experiments/09X-.../phase3_synthesis.md`, say)
that writes "the flagship's witness-scale correction factor was
1.015703" without using the words "length_provenance," "front_surface_
conduction_correction," or "T23" literally:

- `caveat_lint.py`'s `candidate_globs` (`experiments/*/phase*.md`) WOULD
  reach that file — confirmed structurally in §2(a) above. But `_matches_
  any(norm, trigger_terms)` (the only gate on candidate discovery,
  `caveat_lint.py` line ~207) requires one of the three name-based
  triggers to literally appear. A bare numeric restatement with none of
  those three words present is **never flagged, not even as a WARN** —
  the tool has no numeric-value trigger for `1.015703` (or
  `0.089731`/κ_critical, or `1.013006`, the sibling bench-scale figure).
- `lab/numeric_lint.py` has **no candidate-discovery mechanism at all**
  (confirmed by direct source read: no `trigger_terms`/`candidate_globs`
  concept anywhere in the file) — every `numeric_drift`/`derivation_
  consistency` entry only re-checks a fixed, pre-registered `site`/`sites`
  list. The existing `exp063-cf-bench-vs-witness-derivation{,-phase4}`
  entries check exp-063's OWN two documents only; nothing in the numeric-
  lint registry would even be aware a future document exists, let alone
  scan it.

**Net answer**: a future citation that also uses the mechanism's own
vocabulary (the function name, or "T23") IS caught, at WARN tier, by the
already-broad `candidate_globs`. A future citation that quotes only the
bare number — plausible phrasing for a Director summarizing a prior
cycle's headline figure in prose, exactly the register `LOGBOOK.md`'s own
iteration entries are written in — is **not** anticipated by either linter
today. This is the same structural shape as this cycle's own §6 finding
(attack 2: an uncited number surviving into the record) turned forward
instead of backward — the registry protects against a *named* citation
losing its caveat, not a *numeric* one.

---

## 3. From my own charter's lens: does anything in exp-064 touch
perceptual thresholds, contrast, or detection?

By design, no — correctly disclosed and correctly scored zero. This is a
zero-FDTD code-architecture cycle (T1 escape route N/A); no ambient scene,
no contrast metric, no temporal transient was run or claimed. `NOTES.md`
and `phase4_results.md` make no constraint-3/4 claim anywhere, and I found
none implied. The `geometric_realizability` field's own text ("UNGROUNDED"
vs "N/A") is a *provenance* disclosure, not a perceptual one — correctly
so; conflating the two would itself be a T2-adjacent scope-creep risk this
cycle avoids.

---

## 4. Does anything found here fire Checkpoint criterion 4?

**No.** Every finding above is either (i) already-closed, propagated
correctly (§2b), (ii) a live-but-narrow structural gap this seat is
disclosing for the first time, not a violation of a docketed propagation
promise (§2a's `candidate_globs` subset, §2c's name-vs-value trigger gap)
— no mandatory-fix docket item or forward tripwire this cycle or any prior
cycle promised numeric-value-triggered candidate discovery, so nothing
here fails an existing commitment. Criteria 1/2/3/5 do not apply (no
constraint metric scored, no mechanism-class boundary, no engine-physics
build, and Iteration 40 itself advanced the logbook with a genuine result,
so criterion 5's two-consecutive-non-advancing-cycle bar is not in play
regardless of this cycle's own close). **All five Checkpoint criteria:
none fire.**

---

## 5. Verdict: **PROMISING**

T23 is genuinely closed, not merely re-disclosed a fourth time — the
distinguishing feature of this cycle against its own three predecessors
(Iterations 38, 39, 40, all of which disclosed the same violation in prose
without enforcing it) is that Red Team's Phase-2 attack 1 was accepted in
full and the resulting gate 4 was independently, adversarially verified via
a live deliberate-break test against the actual committed commit — not
argued, not merely asserted "this closes it," demonstrated. The `netd_
disclaimer`-preservation gap (this seat's own catch) and the `geometric_
realizability` provenance-vs-buildability gap (THERMODYNAMICS' catch) were
both real, both load-bearing, and both closed with a code-level gate, not
a sentence. The registry entry avoids the specific three-cycle-recurring
failure shape this program has now paid for four times (§2a), confirmed
live rather than by inspection. The residual gaps found here (§2a's
narrower-than-default `candidate_globs` choice; §2c's name-vs-value trigger
blind spot) are real but neither is a broken promise — they are this
seat's own forward-looking contribution, exactly the kind of finding this
seat exists to surface before it becomes a three-cycle pattern rather than
after.

---

## 6. Top-3 ranked candidate directions for Iteration 42

**1. Add a numeric-value trigger to `exp064-length-provenance-disclosure`
(and audit whether other high-stakes registry entries have the same
gap), zero cost.** Add `1\.015703`/`0\.089731` (κ_critical) — or, more
robustly, a generic pattern like `correction_factor\s*[=:]\s*1\.0\d+` — to
`trigger_terms`, so a future bare-number citation is at least WARN-flagged
without requiring the citer to also use the function/thread name. This
closes exactly the gap identified live in §2(c) above, at zero FDTD cost
and zero schema change (the field already exists; `trigger_terms` accepts
regexes per the tool's own docstring). A short audit pass — does any OTHER
`caveat_lint_config.json` entry whose caveat concerns a specific number
(not just a named function/thread) have the same value-vs-name blind
spot? — is a natural zero-cost rider on the same fix.

**2. Execute PLAN.md's own standing queue item 3 (pin CNT-forest pitch/
diameter AND through-thickness κ together)** — carried forward unchanged
from Iteration 40, now doubly motivated: it is both the still-open near-
field-coupling/material-provenance question AND, per this cycle's own §6
strike, the correct home for the thickness/realizability comparison that
was removed from exp-064's own scored record rather than restated
incorrectly. Not this seat's charter to score, but nothing in exp-064
touched it and it remains the program's own highest-ranked physics item.

**3. A `caveat_lint_config.json` entry (or a `candidate_globs` widening
of this cycle's own entry) explicitly covering `lab/thermo_sidecar.py`'s
own docstrings and `lab/validation/run_all.py`'s own stage-23/24 comments**
— closing §2(a)'s residual (this entry's hand-curated `candidate_globs`
omits `lab/*.py`/`lab/validation/run_all.py`, unlike `DEFAULT_CANDIDATE_
GLOBS`). Lower priority than items 1–2 because no live violation exists
today (checked: neither file currently restates the witness-scale number
without the diagnostic framing) — a coverage gap, not a broken promise,
consistent with how this program has correctly distinguished those two
categories at Iterations 38 and 40.

**Carried, lower urgency, not this seat's to rank**: MATERIALS' root-to-
substrate thermal contact resistance item (Iteration 40's own #2); EM's
provenance-ROLE vs provenance-TIER structural gap (Red Team attack 5,
non-blocking); MATERIALS' material-identity-coherence gap on `measured_
geometric` (Red Team attack 7, non-blocking).

---

## 7. Ruled-out registry check (R1–R5, T1–T26)

No ruled-out idea (R1–R5) is touched or at risk of re-proposal by this
cycle — it is pure code architecture, zero mechanism proposal. No live
thread (T1–T26) is advanced, closed, or contradicted by exp-064 itself;
T23 (opened Iteration 22, argued-closed Iteration 23, violated in the open
Iterations 38–40) is the one thread this cycle directly resolves, and its
own closure is recorded accurately in `NOTES.md`/`phase4_results.md`
(checked directly, §1 above) — I find no place in this cycle's record that
mischaracterizes T23's status or any other thread's.
