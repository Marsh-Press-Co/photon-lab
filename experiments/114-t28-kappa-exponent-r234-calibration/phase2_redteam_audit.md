# Phase 2 Red Team Audit — exp-114 (Panel Iteration 91)

**Fresh sub-agent, full-visibility seat.** Read `PANEL.md` in full; `LOGBOOK.md`
in full, end to end (RULED OUT registry R1–R32; LIVE THREADS, T1 and T28's
full history from Iteration 46 through the Iteration-90/exp-113 close).
Read `phase1_proposal.md`, `run114.py`, `chunk_runner114.py` in full, and all
five Phase-2 critiques in full. Read `experiments/113-.../phase2_redteam_audit.md`
and `experiments/113-.../NOTES.md`/`run113.py`/`chunk_runner113.py` and
`experiments/112-.../analyze.py` for house-style/grounding. Unlike the five
blind seats, I see everything, including their outputs — and I did not take
a single number, from the proposal OR from any critique, on faith. Every
figure below was independently recomputed this session (Python one-liners
against the actual committed functions, and, where a critique's claim
concerned committed code, direct reads of that code) or confirmed by actual
re-execution of the literal production dispatch path — never by re-reading
prose.

**T1/constraint status, confirmed independently, not asserted:** N/A
throughout. I read `run114.py` and `chunk_runner114.py` end to end myself;
neither contains any σ(I)/σ(x,t)/angular-selectivity/sub-threshold content,
any `graded_black_shell`/`pec_disk` parameter change, or any constraint-1/2/
3/4 scoring. This is pure T28 instrument-calibration/cost-gate work, matching
every T28 desk/instrument cycle since Iteration 46. No attack below is
tagged constraint-#N-violation for that reason — all five blind critiques
and I independently agree on this, by six different routes.

---

## 0. Trust suite (re-run this session, methodology disclosed)

A single `python3 lab/validation/run_all.py --only 12346789` was attempted
from the repo root and killed at the 580s wall-clock ceiling with **zero**
stdout produced — no `[PASS]`/`[FAIL]` line, no traceback. `ps aux` during
the attempt showed 6–9 concurrent copies of this same command (three
distinct invocation shapes) already running under this session's own
`nproc=4` sandbox, `/proc/loadavg` reading 17–22 throughout — other panel
seats' own sessions sharing this same container, exactly the contention
THERMODYNAMICS' own Phase-2 critique already disclosed for this cycle. This
is external resource contention, not a `lab/` regression: `git diff --stat
-- lab/` was empty throughout.

Falling back to individual stages, matching THERMODYNAMICS' own disclosed
methodology exactly: `--only 1` through `--only 9` (skipping 5, which is not
part of the `12346789` set). Stage 4 alone required three attempts (killed
at 110s and again at 300s under the same contention before completing at a
590s ceiling). Results:

| Stage | Checks | Result |
|---|---|---|
| 1 | 3 | PASS |
| 2 | 3 | PASS |
| 3 | 4 | PASS |
| 4 | 3 | PASS |
| 6 | 5 | PASS |
| 7 | 5 | PASS |
| 8 | 6 | PASS |
| 9 | 13 | PASS |

Tally: 3+3+4+3+5+5+6+13 = **41**, all `[PASS]` — matching this program's own
already-established `--only 12346789` figure exactly, independently
reconstructed from its own parts under the same disclosed methodological
substitution THERMODYNAMICS used. **41/41 green, confirmed, zero `lab/`
diff.**

Additionally, and beyond what any of the five blind critiques did: I
executed the **literal production dispatch path** itself —
`python3 experiments/114-.../chunk_runner114.py 234 25 empty` — with no
`r31_control.json` on file (the actual state of this cycle's scratch
directory). It raised `RuntimeError: R31: run --control before evaluating
the cost gate...` immediately, at the `check_cost_gate_for_r234` call inside
`chunk_runner114.py`'s own `__main__` dispatch, **before any `Sim(...)` was
constructed** — the scratch directory remained empty (no checkpoint, no
walltime log) both before and after. This is the same check exp-113's own
Phase-5 Red Team audit found necessary to run for real, by name (a
commit-message-vs-review-body gap that cycle), rather than trust a
code-reading argument about it — done here, for exp-114, at Phase 2, before
any seat's own review needed correcting for it. **R28 upstream-position
compliance for `r=234`, confirmed by actual execution, not by grep.**

---

## 1. Independent re-derivation of each Phase-2 critique's own numeric claims

### 1.1 EM / VISION / QUANTUM (convergent) — the 0.15/0.30 band's own R28 citation

**Task-mandated check (a).** All three seats independently flag the same
defect: `KAPPA_EXPONENT_CONFIRM_REL=0.15` is justified in `run114.py` (and
§5 of the proposal) as matching "R28's own already-tolerated founding miss
magnitude (~15%)" — but `classify_kappa_exponent_check()` actually scores
`rel_dev = |exponent_234 − 3.2053...| / 3.2053...`, an EXPONENT-space
quantity, while R28's own cited ~15% is a RATIO-space quantity (the
projected wall-time multiplier miss). I re-derived this from primitives
myself, independent of all three:

```
kappa_ratio (r=312/r=156)     = 2.0
KAPPA_COST_EXPONENT (fitted)  = 3.2053299988171697
measured ratio  = 2.0 ** 3.2053299988171697 = 9.223600318696624  (bit-exact
                  to exp-110/111/113's own committed figure)
old-guess ratio = 2.0 ** 3.0 = 8.0
ratio-space deviation   = (9.2236 − 8.0)/8.0        = 0.152950  (≈15.3%,
                          matches R28's own cited "~15%")
exponent-space deviation = (3.20533 − 3.0)/3.0      = 0.068443  (≈6.84%)
```

**Confirmed: the true exponent-space deviation implied by R28's own founding
episode is ≈6.84%, not ≈15% — the citation conflates two different spaces,
exactly as EM/VISION independently found**, and EM's/VISION's own stated
range ("6.4–6.8%") brackets my own precise recomputation (6.84%) correctly.
**QUANTUM's own point figure ("only 6.4%") is itself slightly imprecise** —
the true value is 6.84%, about 7% relatively higher than QUANTUM's own
cited number — a small, non-outcome-reversing but genuine numerical
inaccuracy in QUANTUM's own critique, caught the same way this program's
Red Team has caught a reviewer's own error before (Iteration 90's audit
correcting PHOTONICS' own Finding F4, cited in this cycle's own briefing).

**QUANTUM's own further point is the sharpest and most consequential form
of this defect, and I independently re-verified it exactly:**

```
ratio-space stringency implied by a 0.15 EXPONENT-space band, at kappa_ratio=1.5
    (this leg's own ratio):  1.5**(0.15*k) − 1 = 0.2152   (21.52%)
same, at kappa_ratio=2.0 (the only ratio KAPPA_COST_EXPONENT is fit from):
                             2.0**(0.15*k) − 1 = 0.3955   (39.55%)
```

Both bit-exact to QUANTUM's own cited 0.2152/0.3955. This means the current
band is not merely mis-cited — it is **internally incoherent as a test of
"does this exponent generalize across kappa_ratio"**: its own real-world
(ratio-space) stringency changes by nearly 2× depending on which
`kappa_ratio` it is evaluated at, so a fixed exponent-space threshold cannot
by itself answer the portability question it was built to test. Scoring in
ratio-space directly (QUANTUM's proposed fix) is the only one of the three
seats' proposed remedies that removes this second-order defect, not just
the citation error.

**[inconsistency]** The pre-registered CONFIRM/AMBIGUOUS/REFUTE bands for
"the falsifiable heart of this cycle" (§5, `run114.py::classify_kappa_
exponent_check`) rest on a citation that conflates an exponent-space
deviation with a ratio-space deviation (true precedent ≈6.84%, not ≈15%),
and — independent of the citation error — the exponent-space form's own
real-world stringency is itself `kappa_ratio`-dependent, undermining the
portability test it exists to run. **Non-blocking for Phase 4's own FDTD
spend** (the geometry, cost gate, and R31 control are all independently
verified correct and unaffected) but **MANDATORY before Phase 4's real
`(t156,t234)` data is scored against it** — a CONFIRM/AMBIGUOUS/REFUTE label
frozen into NOTES.md/LOGBOOK under this citation would misstate its own
justification and, per the ratio-space finding, would apply a stringency
this leg's own data cannot be meaningfully compared against a future
`kappa_ratio=2.0` re-check under the same nominal number.

### 1.2 MATERIALS — the disputed cost-multiplier citation, and the deeper LOGBOOK-propagation gap QUANTUM found underneath it

**Independently reproduced, bit-exact:**

```
1.5 ** 3.2053299988171697 = 3.6680107109370383   (not MATERIALS' Iter-90 "≈2.98")
2.0 ** 3.2053299988171697 = 9.223600318696624
ratio = 0.39767667550618246  (≈39.8%, not MATERIALS' Iter-90 "~32%")
```

`run114.py`'s own R4 correction of this figure is right, and its own scope
is honestly stated (it corrects `phase5_review_materials.md`'s citation,
not silently). **But QUANTUM's own critique goes one level further and I
independently confirmed it**: the erroneous "~32%" figure did not stay
contained to one seat's own review file — it propagated **verbatim into
LOGBOOK.md's own frozen Iteration-90 entry**, the "Reconciled Iteration-91
queue" text itself:

```
LOGBOOK.md:24638 — "(3) a cheaper intermediate-`r` (`r=234`, ~32% of this
cycle's own refused-leg cost) calibration point..."
```

I grepped and read this line directly, in context (§ excerpted above in my
own reading of LOGBOOK.md). `run114.py`'s own DISCLAIMER/R4-correction text
names and corrects MATERIALS' *review file* citation but does **not** name
or correct the *LOGBOOK entry* itself, which is the more permanent of the
two records and is the one a future cycle is more likely to cite verbatim
without re-deriving. This program's own convention (confirmed by reading
every prior R4 addendum) is to never retroactively edit a frozen LOGBOOK
entry, but to disclose the correction going forward in the next entry that
touches the same figure.

**[inconsistency]** A real, disclosed-by-neither-document R4-class citation
error (`1.5**3.2≈2.98`/`~32%`, the correct figures being `3.668`/`≈39.8%`)
survives, uncorrected, inside `LOGBOOK.md`'s own frozen Iteration-90 entry —
a citation this document's own R4 correction reaches only one level
upstream of (the review file), not the permanent record itself. **Not
blocking Phase 4** (the qualitative conclusion — r=234 is the cheaper leg —
is unaffected either way, and nothing about the cost-gate arithmetic uses
the "~32%" figure operationally). **MANDATORY**: this cycle's own NOTES.md/
the Iteration-91 LOGBOOK entry must explicitly flag, in prose, that
Iteration-90's own "~32%" figure was arithmetically wrong (true: ≈39.8%) —
a disclosed forward correction, not a retroactive edit, matching this
program's own established practice for every prior R4 instance.

### 1.3 THERMODYNAMICS — the missing energy-ledger capture, confirmed and found broader than framed

**Task-mandated check (b).** I independently confirmed, by direct code read
of `run114.py` and `chunk_runner114.py` in full, and by grep:

- `chunk_runner114.py::step_budgeted()`'s own completion branch (line
  142–154) calls `sc.full_capture(sim)` and persists `cap`, `sigma_e`, `ez`,
  `g`, `total_wall_s` to a pickle — for all three real scenes (empty,
  hollow, peccored) — but never calls `sc.widths()`, and no `sigma_abs`/
  `sigma_ext`/`sigma_ext_cross`/`energy_ledger` string appears anywhere in
  `run114.py` or `chunk_runner114.py` (grep-confirmed, zero hits beyond the
  word "thermo" in the seat-rotation line).
- `lab/sections.py::widths(cap_scene, cap_empty, box, ref)` needs exactly
  the fields `step_budgeted()` already persists (`cap`, plus `g["box_a"]`/
  `g["ref"]`) — I read `widths()`'s own signature and body directly (lines
  114–154) to confirm this: the real absorbed-power data THERMODYNAMICS
  says will exist is not a hypothetical, it is computable at zero marginal
  FDTD cost from data this leg already plans to capture, exactly as
  THERMODYNAMICS claims.
- `graded_black_shell(sigma_max=0.4, tau_shell=24.0)` is a genuinely
  absorptive coating (confirmed identical to the already-validated
  `fixedabs` family by MATERIALS' own independent geometry check) — so this
  is not a case like exp-113's (gate-refused pre-capture, the omission
  moot); real absorbed power will exist in the captured fields if this leg
  proceeds.

**THERMODYNAMICS' claim is confirmed exactly as stated.** My own read finds
the gap is **broader than THERMODYNAMICS' own framing**: **no `analyze114.py`
exists at all** — unlike every predecessor in this exact family
(`analyze.py`/exp-112, `analyze113.py`/exp-113), which both compute the
`energy_ledger` AND carry the actual R23 disclaimer-asserts AND assemble
`results.json`. Checked directly: `refit_kappa_exponent()` and
`classify_kappa_exponent_check()` — **the falsifiable heart of this
cycle** — are defined in `run114.py` but are **never invoked anywhere in
the committed code** (grep-confirmed: zero call sites). `build_result_text()`
is likewise defined but never called. No script anywhere in this cycle's
directory ever writes a `results.json`. This means, as currently committed,
even if Phase 4 runs cleanly, **nothing in the repository would ever
actually compute this cycle's own CONFIRM/AMBIGUOUS/REFUTE verdict, or
persist the energy ledger, or exercise R23's code-level assert for this
cycle's own new `DISCLAIMER` string** — all of which live, for this family,
in the analyze script that has not yet been written.

**Is this a MANDATORY-before-`Sim.run()` blocker, per the task's own
question?** No — `chunk_runner114.py`'s own `step_budgeted()` can execute
and checkpoint all three real FDTD scenes with zero dependency on
`analyze114.py` existing; the raw FDTD spend is not gated by this gap.
**It is MANDATORY before Phase 4's results are treated as complete, scored,
or cited** — without an `analyze114.py` (mirroring `analyze.py`/
`analyze113.py`'s own committed pattern: `sc.widths()` → `energy_ledger`;
`refit_kappa_exponent()`/`classify_kappa_exponent_check()` → the actual
verdict; `R.DISCLAIMER in {predictions,result}_text` asserts; `results.json`
assembly), this cycle cannot produce a scoreable NOTES.md Result section at
all, let alone one that satisfies R16/R21's own established persistence-
and-narration discipline for a real absorptive byproduct.

**[documentation/data-capture-completeness — not one of the four formal
tags, per this program's own recognized fifth category]** `analyze114.py`
does not exist; the energy ledger, the falsifiable-heart classification, and
this cycle's own R23 disclaimer-assert all currently have zero code path to
ever execute. **MANDATORY, Tier 1**: author `analyze114.py` before Phase 4's
real captures are treated as final, mirroring `analyze113.py`'s own
structure — `sc.widths()` on the real hollow/peccored captures →
`energy_ledger` (THERMODYNAMICS' fix); `refit_kappa_exponent()`/
`classify_kappa_exponent_check()` on the real `(t156,t234)` pair →
`results.json`; the R23 asserts on `R.DISCLAIMER` in both text builders.

### 1.4 MATERIALS — the fabrication-tolerance debt omission

**Task-mandated check (c).** Independently confirmed via direct grep of
LOGBOOK.md and every predecessor's own `phase1_proposal.md`:

```
experiments/111-.../phase1_proposal.md:289 — "...fabrication-tolerance bound
    (Tier 2, now a fourth consecutive cycle)."
experiments/112-.../phase1_proposal.md:194 — "...(MATERIALS' own
    fabrication-tolerance bound — ..."
experiments/113-.../phase1_proposal.md:136 — "...fabrication-tolerance bound
    (fifth consecutive cycle undone — explicitly..."
experiments/114-.../phase1_proposal.md, run114.py — grep "fabrication":
    ZERO hits.
LOGBOOK.md:24247-24248 (Iteration-89 queue, Tier 2) — "...MATERIALS' own
    fabrication-tolerance quantitative bound (fourth consecutive cycle)."
LOGBOOK.md:24453-24454 (Iteration-90 queue, Tier 2) — "...MATERIALS' own
    fabrication-tolerance bound (fifth consecutive cycle)."
LOGBOOK.md:24652 (Iteration-91 queue) — "Tier 2/3 — unchanged (see
    LOGBOOK.md Iteration 89 for full text)" — i.e. the item remains a live,
    carried Tier-2 queue line for Iteration 91, not dropped from the queue
    itself.
```

**MATERIALS' claim is confirmed exactly**: this specific item has been
independently, explicitly restated in every one of exp-111/112/113's own
Idealizations/declined-items sections for (at least) three consecutive
cycles running — and exp-114 is the first cycle in that run to omit it
entirely from its own document, even though the Iteration-91 queue itself
(which exp-114's own §3 otherwise engages with closely, naming four other
Tier-1/declined items by cross-reference) still carries it live in Tier 2.

**[documentation-completeness]** `phase1_proposal.md`'s §3 names four other
declined items as "real, named, undropped debt" but omits the one named
debt that is this seat's own charter item, breaking an unbroken
three-cycle restatement chain. **Non-blocking** (Tier 2, no code/geometry
dependency) but should be added — one sentence, per MATERIALS' own proposed
fix — before Phase 3 freezes, both to preserve the restatement convention
and because a sixth silent cycle would be a meaningfully worse record than
a fifth.

---

## 2. What the five critiques collectively missed — my own adversarial read

I read `run114.py` (445 lines) and `chunk_runner114.py` (233 lines) line by
line myself, independent of all five critiques, checking specifically for
what this program's own Red Team has historically found sitting underneath
five clean blind reviews (R18, R19, R22, R24's second instance).

**Findings, beyond §1 above:**

- **R29 compliance**: confirmed directly — `assert R110 is not R112 and
  R110 is not R113 and R112 is not R113` (`run114.py`) and `assert R is not
  R110 and R is not R112 and R is not R113` (`chunk_runner114.py`), both
  present, both would fire on a collision. No R29 defect found.
- **Cost-gate formula parity**: `cost_gate_check_r234()`'s structure
  (`pilot_pass`, `kappa_ratio ** kappa_exponent`, `total_pass`, `proceed`)
  is byte-structurally identical to `R110.cost_gate_check()` (confirmed by
  direct diff-by-eye of both function bodies, `run.py` lines 380-406 vs.
  `run114.py` lines 169-186) except for the one disclosed line
  (`kappa_ratio` now parameterized). No undisclosed deviation found.
- **The literal dispatch path** (§0, above): actually executed, not merely
  read — confirms the R28-upstream claim beyond what any of the five blind
  seats did (each verified the gate exists and branches correctly under
  fed-in synthetic values, or read the dispatch order in source; none ran
  `chunk_runner114.py 234 25 <scene>` for real with no control file on
  file, the exact gap exp-113's own Phase-5 audit found and closed for
  that cycle).
- **The `_SPONGE_LOG_ATTEN_CPL25 = 17.242357` reuse**: traced this back
  three cycles — genuinely, independently derived at exp-112's own Phase-2
  critique (MATERIALS reimplementing `lab/fdtd2d.py::_damping()`'s own ramp
  formula from scratch, `phase2_redteam_audit.md` line 29, exp-112) — not
  a hand-typed number invented at exp-113 or exp-114. Reuse across
  r=156/234/312 is legitimate: it depends only on `ABSORB`/`cpl` (asserted
  identical at all three r in `run114.py` itself, line 266), never on `r`.
  **No R4 defect found here** — flagged as a candidate concern, checked,
  and cleared.
- **No bug found in `refit_kappa_exponent()`'s own direction/base**:
  `ln(t234/t156)/ln(1.5)` matches the founding derivation's own construction
  (`ln(t312/t156)/ln(2.0)`) exactly in form; QUANTUM independently confirmed
  this and I re-checked it against `R110`'s own comment. No sign/base error.
- **R31 gate-flip property, re-verified with my own fresh synthetic values**
  (not reused from THERMODYNAMICS' own critique): fed `cost_gate_check_r31_
  r234` a synthetic slow session (`short speed_ratio=0.1676`,
  `sustained speed_ratio=0.1397`) — `combine_control_readings` correctly
  selected the LOWER (`sustained`, more conservative) reading, and the gate
  correctly flipped `raw proceed_to_r234=True` (uncontrolled) to
  `scaled proceed_to_r234=False` (R31-controlled) at this synthetic
  throughput. The "R31 can and does refuse" property survives the
  `kappa_ratio`-substitution from `R113`'s r=312 gate to `run114`'s own
  r=234 gate, independently confirmed a second way.

**No new inconsistency, unfalsifiable claim, or inexpressible mechanism
was found beyond what §1 already covers.** This cycle's own code is, in the
main, unusually clean — every one of the five blind critiques independently
verified the headline arithmetic bit-exact, and I could not break any of
it either. The defects that survive to this audit are all in the
**falsifiable-band justification** and the **completeness of the
capture-to-verdict pipeline**, not in any executed arithmetic.

---

## 3. MANDATORY-FIX docket

All fixes below are applied by the Director at Phase 3, before Phase 4's
real data is treated as final. None requires new FDTD data to implement,
and none blocks the raw `Sim.run()` calls `chunk_runner114.py` is already
free to make.

**Fix 1 [EM/VISION/QUANTUM, consolidated — inconsistency]**: Correct
`KAPPA_EXPONENT_CONFIRM_REL`'s own justification. Two acceptable routes,
either sufficient: (a) re-derive the band directly in ratio-space
(QUANTUM's own proposed fix — `rel_dev = |kappa_ratio**exponent_234 −
kappa_ratio**KAPPA_COST_EXPONENT| / kappa_ratio**KAPPA_COST_EXPONENT`
against 0.15/0.30, which genuinely matches the founding ~15% miss at any
`kappa_ratio`, closing the second-order kappa_ratio-dependent-stringency
defect as well as the citation error); or (b) keep the exponent-space form
but correct `KAPPA_EXPONENT_CONFIRM_REL`/`_REFUTE_REL` to their true
exponent-space equivalents (≈0.068/≈0.137) and drop the now-false "not an
arbitrary round number" framing, disclosing the choice as a house
convention if a looser number is deliberately kept. Must land before real
`t234` data is scored.

**Fix 2 [QUANTUM's own finding, independently confirmed — inconsistency]**:
This cycle's own NOTES.md (or the Iteration-91 LOGBOOK entry) must
explicitly disclose that Iteration-90's own frozen "Reconciled
Iteration-91 queue" text (`LOGBOOK.md:24638`, "~32%") is arithmetically
wrong — true figure ≈39.8% (`1.5**3.2053... / 2.0**3.2053... = 0.397677`)
— as a forward correction, not a retroactive edit, matching this program's
own established R4 practice. Non-blocking for Phase 4 (the qualitative
conclusion is unaffected) but must be disclosed before this cycle's own
record is frozen.

**Fix 3 [THERMODYNAMICS, confirmed and broadened — data-capture/
documentation-completeness]**: Author `analyze114.py` before Phase 4's real
r=234 captures are treated as final, mirroring `analyze113.py`'s own
structure exactly: (a) `sc.widths()` on the real hollow/peccored captures
→ persist `sigma_scat`/`sigma_abs`/`sigma_ext`/`sigma_ext_cross` as
`energy_ledger`; (b) invoke `refit_kappa_exponent()`/
`classify_kappa_exponent_check()` on the real `(t156,t234)` pair and
persist the verdict — currently dead code, and this cycle's own stated
falsifiable heart; (c) the R23 code-level asserts (`R.DISCLAIMER in
predictions_text`, `R.DISCLAIMER in result_text`), which for this family
live in the analyze script, not `run*.py`'s own bare CLI path — currently
absent because the file that would house them does not exist. Must land
before Phase 4's results are scored, cited, or frozen into NOTES.md/
LOGBOOK — not before the FDTD captures themselves, which do not depend on
it.

**Fix 4 [MATERIALS, confirmed — documentation-completeness]**: Add one
sentence to §3 (or the Idealizations) explicitly naming MATERIALS' own
fabrication-tolerance quantitative bound as a declined, not-silently-dropped
item carried forward to Iteration 92 — restoring the three-cycle
restatement chain exp-111/112/113 each maintained. No code or geometry
change needed.

**Mandatory vs. optional, explicitly.** All four fixes are MANDATORY in the
sense that this program's own R4/R16/R21/R25 lineage requires: none may be
silently dropped from the Iteration-92 queue if not applied here. But they
are not equally load-bearing, and the task's own question ("mandatory
before any Phase-4 `Sim.run()` call" vs. lower-priority) has a real,
non-uniform answer per fix:

- **Fix 3 — hard-mandatory, but gates *scoring*, not the FDTD spend itself.**
  `chunk_runner114.py`'s own `Sim.run()` calls need nothing from
  `analyze114.py` to execute correctly (confirmed by direct code read: no
  import, no call). But without it, Phase 4 can run to completion and
  still leave this cycle unable to report a verdict, an energy ledger, or
  an R23-compliant DISCLAIMER — so it must land before Phase 4's captures
  are treated as final, even though it need not land before the captures
  are taken.
- **Fix 1 — mandatory before any real `t234` is scored** against the
  CONFIRM/AMBIGUOUS/REFUTE bands (i.e., mandatory as part of Fix 3's own
  `analyze114.py`, not before the FDTD spend either).
- **Fix 2 / Fix 4 — mandatory as document hygiene, genuinely lower stakes.**
  Neither touches any code, geometry, or verdict arithmetic; both are pure
  disclosure corrections this program's own house discipline (R4 for Fix 2,
  the established declined-items convention for Fix 4) requires before
  Phase 3 freezes this cycle's own record, but neither would change any
  number Phase 4 produces if, hypothetically, deferred by one more cycle —
  the reason they rank last, not the reason they could be dropped.

**Ranking**: Fix 3 > Fix 1 > Fix 2 > Fix 4. None of the four rises to a
disclosed-override candidate — all are cheap, concrete, code/doc-
expressible, and (Fix 3 especially) genuinely load-bearing for whether this
cycle can produce a citable result at all. **Zero fixes block the raw
`Sim.run()` calls `chunk_runner114.py` is already free to make** — this is
the one clean finding across all four: nothing found here is a reason to
withhold the FDTD spend itself, only reasons to withhold treating its
output as scored/final without further, already-scoped, cheap work.

---

## 4. New standing rule? — declined, named as a watched risk instead

I considered proposing a new rule generalizing Fix 3's own shape ("a
falsifiable check's own scoring function must be invoked by committed code,
not merely defined, before real data can be trusted against it") to the
R16/R21 lineage (byproduct persistence/narration). I decline to mint one
this cycle, on the same ground Red Team's own exp-113 audit used to decline
ratifying VISION's R23-forward-risk: **this is a zero-instance, purely
prospective finding relative to any FROZEN record** — Phase 4 has not run,
nothing has been scored incorrectly yet, and the gap is caught here, at
Phase 2, before any real data exists to be mis-scored. Minting a rule
against a risk with no founding instance (a cycle that actually shipped a
frozen verdict from an uninvoked classifier) would cheapen this registry's
own single-instance-ratified convention. **Named as a watched risk instead,
its exact trigger stated plainly**: if any future T28 cycle freezes a
Result/NOTES.md verdict citing a classification function that is never
actually called by any committed script, that is this risk's founding
instance, ripe for ratification as an R33 candidate under the existing
R16/R21 "persisted-but-not-narrated" / "narrated-but-not-computed" lineage.

Similarly, the R23-enforcement gap (Fix 3(c), above) is not itself a new
R23 violation on the books today — no `DISCLAIMER` string has been frozen
into a Result section without its assert, because no result has been
produced. It is the SAME zero-instance/prospective shape, folded into Fix
3 rather than argued as independently rule-worthy.

---

## 5. Verdict

**PROCEED-WITH-MANDATORY-FIXES.**

Numbered attacks (tags per the required scheme; T1/constraint-3 correctly
N/A throughout — no attack below is a constraint-#N violation):

1. [inconsistency] The 0.15/0.30 CONFIRM/REFUTE band for
   `classify_kappa_exponent_check()` is justified by a citation that
   conflates an exponent-space deviation (true value ≈6.84%) with a
   ratio-space deviation (R28's own genuine ≈15.3%) — independently
   re-derived, confirming EM/VISION/QUANTUM's convergent finding — and,
   independent of the citation, the exponent-space band's own real-world
   stringency is itself `kappa_ratio`-dependent (21.5% at kr=1.5, 39.6% at
   kr=2.0), undermining the cross-ratio-portability question it exists to
   test — Fix 1.
2. [inconsistency] A propagated arithmetic error (`1.5**3.2≈2.98`/"~32%",
   true value `3.668`/"≈39.8%") survives uncorrected inside `LOGBOOK.md`'s
   own frozen Iteration-90 entry — this document's own R4 correction
   reaches the originating review file but not the more permanent LOGBOOK
   record itself — Fix 2.
3. [data-capture/documentation-completeness — not a formal tag] No
   `analyze114.py` exists: the real absorbed-power data THERMODYNAMICS
   correctly flags will exist in captured fields has no code path to
   `sc.widths()`; more consequentially, this cycle's own stated falsifiable
   heart (`refit_kappa_exponent`/`classify_kappa_exponent_check`) is
   defined but never invoked anywhere in committed code, and this cycle's
   own new `DISCLAIMER` string has no R23 code-level assert anywhere
   (absent because the file that would house it, per this family's own
   established pattern, does not exist) — Fix 3.
4. [documentation-completeness] MATERIALS' own fabrication-tolerance
   quantitative bound, independently confirmed restated in every one of
   exp-111/112/113's own declined-items sections and still a live Tier-2
   queue item for Iteration 91, is entirely absent from this cycle's own
   document — Fix 4.

**Everything independently re-executed — the geometry-identity check at
r=156/234/312, the cost-multiplier arithmetic, the R31 control-reuse
direction, the literal no-control-file dispatch path, and the 41/41 trust
suite — reproduced correctly.** No constraint-#N violation, no
unfalsifiable claim, and no inexpressible mechanism exists anywhere in this
cycle (there is no mechanism here to be inexpressible). The defects found
are real but narrow: a falsifiable band's own justification, a permanent-
record citation, and — the most consequential — a not-yet-written analysis
script without which this cycle's own central question cannot be answered
even after Phase 4 runs cleanly. All four are cheap, disclosed, and fixable
before any real data is scored. This cycle should proceed to Phase 3
synthesis with all four fixes applied as part of that synthesis (Fix 3
before Phase 4's captures are treated as final; Fixes 1/2/4 as document
corrections), matching exp-113's own immediately-preceding house precedent
for a PROCEED-WITH-MANDATORY-FIXES cycle with zero Checkpoint criteria
firing.

**Checkpoint criteria**: none fire. This is a clean, narrowly-scoped
instrument-calibration cycle whose own defects were all caught blind, at
Phase 2, before any freeze — matching every prior R16–R32 founding-instance
non-firing precedent this registry has established.
