# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 71 · exp-094

*Fresh sub-agent, RED TEAM charter (PANEL.md, verbatim): attacks every
proposal, speaks last and hardest; standard is not textbook-physics
compliance but internal consistency, falsifiability, expressibility as
simulation parameters, and non-violation of a target constraint. Read in
full, this session: `PANEL.md`; `LOGBOOK.md` (RULED OUT R1–R15 verbatim,
ESTABLISHED, LIVE THREADS T1–T28 in full — read sequentially from line 1
through the complete T28 sub-thread, Iterations 46–70); `PLAN.md`'s Current
state section; the complete exp-094 record (`phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md` in full, `run.py`, `results.json`, `run_output.txt`); all six
Phase-5 reviews (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS,
QUANTUM OPTICS self-review, VISION SCIENCE); `gate5_wiring_defect_
verification.py`. Every load-bearing figure below was independently
re-pulled from `results.json`/`run.py`/`design_geometry.py` source this
session — none taken on any prior document's word — and
`gate5_wiring_defect_verification.py` was independently re-executed
(`python3 gate5_wiring_defect_verification.py`), not merely read.*

## 0. Independent re-verification ledger (bit-exact reproductions this session)

| Claim | Source | Independently reproduced |
|---|---|---|
| Rank 2: `ds_ratio=1.0766`, `fc_ratio=1.0856` | `results.json::rank2` | ✅ bit-exact |
| Rank 3: 36.0°/38.8° CONSISTENT, 38.4° FLIPPED (`0.9075→16.9967`) | `results.json::rank3.per_theta` | ✅ bit-exact |
| Rank 1a: `rel_dev=0.1297%` | `results.json::rank1a` | ✅ consistent with printed value |
| Rank 1b: all six `delta_scene>0` (`3.90e-4`–`4.22e-4`), all `floor_pass=True`, `ratio_k` 3.67–7.13 | `results.json::rank1b.per_theta` | ✅ pulled directly, matches PHOTONICS/EM/QUANTUM citations |
| exp-093 item1 same six angles: all `delta_scene<0` (`-1.17e-4`..`-4.3e-5`) | `experiments/093-.../results.json::item1.per_theta` | ✅ pulled directly — confirms a **complete** sign-and-classification reversal, not partial |
| Gate 5 (`n_article_calls_checked=16`, `pass_=True`) | `results.json::gates.gate5_runtime_sigma_array` | ✅ present, and job-table count independently recomputed (4+12=16) |
| Gate 5 genuinely discriminates | `gate5_wiring_defect_verification.py` | ✅ **re-executed this session** — control call completes silently, injected-defect call raises `AssertionError` exactly as claimed |
| `R4_BASE_OBJ_Y=1584` (not the NOTES.md table's literal `1504`) | `experiments/069-.../design_geometry.py:255` | ✅ confirmed committed value is the correct, self-consistent one |
| `rank3_report` fields | `run.py:545-550` | ✅ confirmed: `delta_scene, frac_contrast, ratio_k, floor_pass, ratio_k_cpl20, y_cpl20, y_cpl30, outcome` only — **no `p_abs_w`/`frac_p_abs`/NETD field anywhere** |
| `netd_row()` defined but never called in exp-094 | `experiments/093-.../run.py:185-196`; `grep netd_row experiments/094-.../run.py` | ✅ confirmed zero call sites |
| `cell_metrics_r4` computes NETD fields | `run.py:295-342` (`ts.netd_disposition`, `dt_ss_full_K`) | ✅ confirmed computed, confirmed never threaded into any Rank output dict |
| "larger absolute swing" (38.4° vs 41.4°) | `results.json` (exp-094) + `experiments/091-.../results.json::b.per_theta["41.4"]` | ✅ recomputed: 38.4° raw diff **16.089**, fold **18.73×**; 41.4° raw diff **19.596**, fold **3.13×** — raw-magnitude claim is backwards, fold-change claim is correct |
| Rank 3-ext zone unchanged, `n=11` non-inverted | `results.json::rank3_ext` | ✅ bit-exact, `zone=[4.1083,5.4287]` unchanged, `firth_m50` shifts `4.6934→4.3832` |

No load-bearing figure in `NOTES.md` failed independent reproduction. The
science is sound; every finding below is about the record's own honesty
about itself, or about gaps in what was checked — exactly Red Team's
charter.

## 1. Adjudication of all six Phase-5 findings

### 1.1 The Gate-5-verification-claim gap (PHOTONICS + MATERIALS + QUANTUM
self-review, three-seat-convergent)

**CONFIRMED, independently, a fourth way.** `NOTES.md`'s Result section and
Learned #4 assert Gate 5 was "independently confirmed... by injecting a
simulated R15-style wiring defect into a standalone test harness during
Phase 4 (correctly raised `AssertionError`)." I grepped `run.py`,
`run_output.txt`, `results.json` for "harness"/"inject"/"simulated" — zero
hits, matching all three reviewers. `git log` was not separately re-run
here (three independent seats already did this and found nothing); I take
their convergent negative result as sufficiently corroborated given my own
independent confirmation of every other part of this finding.

**The underlying scientific claim is true, confirmed a fourth time.** I
executed `gate5_wiring_defect_verification.py` myself:

```
[control] correct-sigma call completed without raising -- OK (Gate 5 is silent on genuinely correct wiring)
[injected defect] Gate 5 correctly raised AssertionError:
  GATE 5 FAILED -- runtime sigma_e/sigma_max mismatch: sim.sigma_e[shell_mask].max()=0.5 vs sigma_max=0.25
VERIFIED: Gate 5 is a genuine discriminator...
```

Gate 5 is genuinely discriminating. This is now independently confirmed by
**four** separate parties (PHOTONICS, MATERIALS, QUANTUM's self-review, and
this audit), each from the real, committed `run.py` machinery.

**Does the Director's `gate5_wiring_defect_verification.py` close the gap?
Scientifically, yes. As a *record*, only half of it.** The script is a
genuine, permanent, reproducible artifact — I confirm it discharges the
underlying scientific uncertainty completely. But this house's own R4
discipline (invoked explicitly by all three finding seats) requires BOTH
the artifact AND a corrected citation in the permanent prose — and the
second half was never done. As it stands right now, `NOTES.md`'s Result
section and Learned #4 **still assert a false event**: a "standalone test
harness during Phase 4," authored and run by nobody named, leaving no
trace — when the actual, real artifact was written and run by the
**Director**, **mid-Phase-5** (per the script's own docstring: "closing a
real gap two independent Phase-5 seats caught blind... This script IS that
artifact"), specifically in response to QUANTUM's self-review and
MATERIALS' Phase-5 review. The prose was never updated to match the
artifact that now exists beside it. This is precisely this house's own
precedent (Iteration 70, exp-093: "the caption defect UPHELD, real,
non-load-bearing, one mandatory same-shift fix required" for an equally
non-load-bearing but factually-wrong sentence) — a true underlying claim
does not excuse a false description of how it was verified.

**Ruling: MANDATORY same-shift text fix (Fix #1, below).** Non-firing on
Checkpoint criterion 4 in isolation (see §3).

### 1.2 MATERIALS' proposed R15 addendum

**ADOPTED.** I independently re-derived the case for it from primary
source (§0 above: the reversal is complete — 6/6 points, not a
boundary-adjacent single point) and find MATERIALS' framing exactly
matches PHOTONICS' independently-converged Attack (§ of its own review):
"a monotonic node-migration story, an oscillating-with-`cpl` story, and a
genuinely non-convergent-at-any-affordable-`cpl` story are all equally
consistent with the data." Two Phase-5 seats independently converged on
the identical structural point without seeing each other's work — that is
the standard this program has used to promote a finding to a standing-rule
addendum before (R1's ENZ addendum, R10's founding text, R11's addendum).
I adopt the addendum verbatim, below (§4).

### 1.3 MATERIALS' `R4_BASE_OBJ_Y` near-miss on my own prior Phase-2 audit

**CONFIRMED, an R9-shape near-miss, correctly ruled non-load-bearing.**
Independently re-derived: `phase2_redteam_audit.md`'s own "Documentation
completeness" item verified only that `R4_BASE_NY//2 − R4_BASE_ABSORB =
1504` reproduces the *target number* — it never checked whether
substituting that same formula's value, 1504, as `R4_BASE_OBJ_Y` itself and
threading it through `r4_config()`'s own `A = obj_y − y_lo` (which
subtracts `ABSORB` a *second* time) reproduces 1504 downstream. It does
not — it gives 1424, would have failed Gate 2 loudly. MATERIALS is
correct that this is the same *shape* of gap R9 names (verifying a number
reproduces is not the same as verifying it is the correct quantity to
substitute downstream), now caught in a spec-ambiguity-resolution context
rather than a unit-comparability context. I confirm the committed value
(`R4_BASE_OBJ_Y = R4_BASE_NY//2 = 1584`) is correct and self-consistent,
confirm Gate 2 would have caught the wrong formula loudly and pre-FDTD (so
this was never a live risk to any delivered number), and confirm this does
not warrant a new standing rule on its own (a single self-defended
near-miss, immediately caught and correctly resolved, is not the "known,
named, ignored" shape R9 itself required two instances to establish). Logged
for the record; no fix required beyond this entry.

### 1.4 THERMODYNAMICS' zero-cost Rank-3 `p_abs_w` gap + the NETD-byproduct-
dropped pattern

**Both CONFIRMED, independently, from source** (§0 above: `rank3_report`
fields traced directly; `netd_row()` confirmed defined in the loaded module
and confirmed never called). Full disposition in §3 (Checkpoint ruling) and
§4 (mandatory fixes) below — this is the cycle's single most consequential
adjudication and gets its own section.

### 1.5 QUANTUM's "no far-from-null control point" self-attack

**CONFIRMED, and I rate it more urgent than a routine forward tripwire.**
Independently traced: every one of this cycle's 32 `R4`-family calls (Rank
1a's 8 + Rank 1b's 24) sampled only the 41.750°–41.900° interior band.
Gates 1–6 verify geometry and sigma-wiring; nothing verifies the `R4`
family's own coordinate/phase-reference construction reproduces a
**known-correct** sign anywhere. QUANTUM's own analogy to R6 (a synthetic
ground-truth recovery test, generalized from a new *estimator* to a new
*resolution family*) is apt and, on my own independent reading of R6's
text, not a strained extension — R6's underlying principle ("a check that
would pass regardless of correctness is not a check") is exactly what is
missing here, and the failure mode QUANTUM names (a uniform, full-window,
entirely convincing-looking reversal is *exactly* the shape a systematic
registration defect would also produce) is not hypothetical color — this
cycle's own headline finding IS a uniform, full-window, convincing-looking
reversal. See §3/§5 for disposition (not a same-shift fix, but ranked
above the already-queued `cpl=50` check for Iteration 72, matching
QUANTUM's own ranking, which I independently endorse rather than merely
adopt).

### 1.6 PHOTONICS' "absolute swing" wording

**CONFIRMED, independently recomputed** (§0 above: 41.4°'s raw swing 19.60
`>` 38.4°'s raw swing 16.09 — the literal-reading claim is backwards; the
fold-factor reading, 18.73× vs. 3.13×, is almost certainly what was meant
and is correct). Non-load-bearing narrative color, but this house's R4/R9
discipline does not grant a pass for stakes — see Fix #4, below.

## 2. Does the `cpl=40` reversal quietly violate a target constraint?

No. Independently re-verified against my own charter's own standard
(constraint-3 especially): this cycle takes no T1-route position, makes no
phenomenon-mechanism claim, and touches `REALIZABILITY_MEMO.md` nowhere —
correctly, matching every T28 desk/instrument cycle since exp-069. EM's own
passivity/causality/reciprocity bookkeeping (independently spot-checked
here against `lab/fdtd2d.py`'s own E-update and `lab/materials.py`'s own
smoothstep profile) is clean: every `sigma_max` value used (0.5, 1/3, 0.25)
is non-negative, `ca∈(0,1)` throughout, no gain, no dispersive term
introduced. Constraint bookkeeping: not engaged, correctly.

## 3. Checkpoint ruling — all five criteria

1. **Configuration passes all constraint metrics** — N/A, no constraint
   metric is scored this cycle. **Does not fire.**
2. **Proven mechanism-class boundary** — N/A, no mechanism claim (T1 route
   N/A throughout, independently reconfirmed). **Does not fire.**
3. **Engine physics beyond validated bench classes** — No; this cycle is a
   mechanical, additive congruent-geometry rescale of already-validated
   machinery. **Does not fire.**
4. **Program-integrity drift (unfalsifiable claims, a constraint quietly
   dropped)** — the criterion the task brief and this cycle's own record
   both demand real scrutiny on. See detailed ruling below. **Does not
   fire, but this is the closest non-firing call in this sub-thread's
   history, closer than Iteration 68's "non-firing only by a hair" and
   Iteration 70's own discharge — named explicitly as such, with a
   forward-elevating clause.**
5. **Two consecutive non-advancing iterations** — Iteration 70 (exp-093)
   delivered the R8 dispersion-tripwire discharge and the NETD backfill;
   Iteration 71 (exp-094) delivered a dramatic, independently-verified new
   result (R15's own concern empirically realized on its own founding
   sub-thread). Both iterations genuinely advanced the record. **Does not
   fire, not close.**

### Criterion 4 — the detailed ruling the task requires

This cycle's record contains **two independent unverifiable/overclaimed
statements** in `NOTES.md`'s own permanent Result section — not one:

- The Gate-5 "standalone test harness during Phase 4" claim (§1.1) — caught
  blind by **three** Phase-5 seats (PHOTONICS, MATERIALS, QUANTUM
  self-review), independently, in the same cycle.
- The Rank 1b "UNDETECTABLE... is directly confirmed to extend to
  `cpl=40`" claim (§1.4, detailed below) — caught blind by **one** Phase-5
  seat (VISION), independently, in the same cycle.

Both were caught **before** this document existed, **before** any citation
to either claim reached `LOGBOOK.md` or a future cycle, and **before**
either was relied upon for any scored verdict — the core condition this
program has used, repeatedly and as recently as last cycle (Iteration 70:
"this turns on being caught before *this phase's own* freeze/citation
point, not on preceding the run"), to rule a defect non-firing. I apply
that precedent here and rule **non-firing** on both, individually.

**But I decline to apply it by inertia, and I name explicitly why this is
close.** Three facts distinguish this cycle from a routine "caught blind,
same cycle" discharge:

1. **This is not one overclaim — it is two, independently arising, in the
   same document's Result section.** A pattern that recurs *within* a
   cycle, in two unrelated places, is weaker evidence of "an isolated
   slip" than a single instance would be.
2. **The NETD-persistence code gap underlying the second overclaim is
   itself a recurrence of a pattern `LOGBOOK.md`'s own Iteration-70 entry
   had just, one cycle ago, declared "genuinely closed"** ("criterion 4 in
   particular... does NOT fire: VISION's own structural fix from exp-092
   genuinely closed that class of gap"). That belief is now shown wrong,
   one cycle later, in new code.
3. **This cycle's own Phase-2 process had explicit, specific, on-the-record
   advance knowledge of exactly this risk, and still shipped an incomplete
   remedy.** I independently re-read `phase2_redteam_audit.md`'s own RT-4:
   it names, by iteration number, that "this exact shape of gap... has
   fired Checkpoint criterion 4 four times in this program's history
   (Iterations 53/63/64/65)," confirms Rank 2/Rank 3 will "almost
   certainly" surface NETD byproducts via the `_full` variant — and then
   mandates only that a disclaimer travel with any such field, not that
   the field itself be *persisted* using `netd_row()`, the exact,
   already-built, already-proven fix `experiments/093-.../run.py` shipped
   one cycle earlier for this precise purpose (its own docstring: "matching
   Iteration-69 LOGBOOK's own named truncation defect... not repeating it
   here"). RT-4's own mandate additionally never considered **Rank 1** at
   all — the cycle's largest, most novel item, whose own `cell_metrics_r4`
   computes the identical fields "IN FULL" per its own inline comment (VISION's
   independently-confirmed finding). The gap that actually materialized is
   broader than the one RT-4 anticipated and narrower than the one RT-4
   could have closed by simply requiring `netd_row()`'s reuse.

**I rule this does NOT meet the strict "known, named, ignored" bar this
program's R6/R11 lineage reserves for automatic firing** — that bar has, in
every prior instance, involved *literally reusing the same already-fixed
machinery unfixed* (R11: "any future call to this machinery... A cycle
that reuses this machinery unfixed... fires Checkpoint criterion 4
automatically"). Here, the code path that dropped the data (`cell_metrics_r4`
plus Rank 2/3's own result-assembly dicts) is genuinely new this cycle; it
never called `netd_row()` at all, rather than calling it and then
discarding its output, or calling an old, already-patched function in its
unpatched form. That is a materially different — and less culpable —
failure shape than R11's own founding instance.

**But I am not willing to let this slide as a bare forward tripwire
either**, given points 1–3 above. **New standing-rule text, proposed here
for Director/panel adoption** (in the R6–R15 lineage, closing the specific
loophole RT-4's own narrower mandate left open): see §4, new rule proposal,
below. Until that rule is adopted, I state explicitly, with the same force
this program's other tripwires carry: **a third occurrence of "a
disclaimer travels but the field it is meant to cover is never persisted"
on this or any T28-adjacent channel, in any form, fires Checkpoint
criterion 4 automatically, no further deliberation** — matching this
program's own established elevation language, and explicitly naming this
cycle's occurrence (not exp-092's) as the second, since exp-093 broke the
chain with a working fix that this cycle simply failed to reuse in new
code.

## 4. Same-shift mandatory fixes (ranked)

All of the below are zero-or-near-zero marginal cost (deterministic
reruns or text-only) and, per this house's own standing discipline, must
land before this document is treated as closed.

1. **[Text-only, zero cost] Correct the Gate-5 verification claim.**
   Strike "by injecting a simulated R15-style wiring defect into a
   standalone test harness during Phase 4 (correctly raised
   `AssertionError`)" from both the Result section and Learned #4. Replace
   with an accurate description citing the actual artifact and its actual
   provenance, e.g.: *"independently confirmed a genuine discriminator by
   `gate5_wiring_defect_verification.py` (Director, written and run
   mid-Phase-5, closing a gap three Phase-5 seats — QUANTUM's self-review,
   MATERIALS, and this audit — independently caught: the original claim of
   a 'standalone test harness during Phase 4' had no corresponding
   artifact anywhere in the committed record)."* This is R4's own standard
   applied to itself — the correction must name what actually happened,
   including that it happened later and differently than first claimed.

2. **[Rerun, 12 calls, deterministic] Extract `p_abs_w`/`frac_p_abs`
   (and, matching Rank 1b's own precedent, the full `netd_row()` sidecar)
   for Rank 3's three census angles**, especially 38.4° — this cycle's own
   newest, largest reversal, with currently zero energy-channel check at
   any resolution. `pair_metrics_full` already computes these values in
   memory during the existing Rank-3 calls; only the extraction into
   `rank3_report` is missing. This bench's determinism (independently
   confirmed by the settled-suite record cited throughout `NOTES.md`, and
   by Rank 3-ext's own bit-exact base-table reproduction, §0) makes a rerun
   a reproduction, not new information. THERMODYNAMICS' own charter (owns
   the per-proposal energy sidecar) makes this the single most
   charter-central fix on the docket.

3. **[Rerun, 4+24 calls already executed — additive persistence only,
   zero-cost re-derivation] Retrofit `netd_row()` into Rank 2/Rank 1a/1b's
   own result-assembly dicts.** The `_full` machinery already computed
   `dt_ss_full_K`/`netd_classification` for every one of this cycle's 20
   article-bearing cells; persist it, matching `experiments/093-.../
   results.json`'s own item1/item3 precedent, rather than leaving the
   top-level `netd_disclaimer` covering an empty set.

4. **[Text-only, zero cost] Correct Rank 1b's "directly confirmed"
   overclaim.** Replace "exp-093's own energy-flatness/UNDETECTABLE
   finding... is directly confirmed to extend to `cpl=40`" with an
   accurate two-part statement: the `p_abs_w` energy-flatness *ratio* is
   confirmed at `cpl=40` (true, independently reproduced, §0); the
   UNDETECTABLE/NETD *classification* itself remains `cpl≤30`-verified only
   **unless** Fix #3 above is applied and confirms it — in which case cite
   the actual `dt_ss_full_K`/`netd_classification` values directly, not by
   inference from the energy-flatness ratio.

5. **[Text-only, zero cost] Correct PHOTONICS' "larger absolute swing"
   wording** (§0/§1.6) — replace with "larger fold-change" or drop the
   raw-magnitude comparison entirely.

None of these five fixes changes any gate, band, or the Combined Verdict
below — all are independently confirmed non-load-bearing, matching every
finding seat's own disposition.

## 5. New standing-rule proposal (for Director/panel adoption)

**R15, Addendum (Iteration 71, exp-094):** *A cross-resolution check that
reverses an ENTIRE sampled span — every point flipping sign and
classification together, not a partial drift at some points and stability
at others — must be read as evidence that NEITHER resolution's reading is
individually trustworthy, and must specifically not be resolved by
defaulting to the finer grid as automatically more correct. A finer-grid
family built by mechanically substituting a new ratio into an
already-validated congruent-construction recipe (as `R4` was built from
`R3`) inherits any resolution-*independent* systematic the recipe itself
carries; two such points cannot, on their own, distinguish genuine
continuum convergence from a persistent recipe-level artifact or a
genuinely non-convergent oscillation. A third, differently-ratioed
resolution point is the minimum required to distinguish these — and,
before that point is trusted, the new family must additionally be shown to
reproduce the ALREADY-KNOWN-CORRECT sign at a robust, far-from-null angle
on the same channel (a synthetic ground-truth-recovery discipline,
generalized from R6's own estimator-conditioned form to a new resolution
family), since a uniform full-window reversal is indistinguishable, from
pointwise data alone, from a systematic registration/phase-reference
defect in the new family's own construction.* — Founding instance:
exp-094 (this cycle). Matching R5/R6/R9/R10/R11/R12/R13/R14/R15's own
founding-instance precedent, **does not fire on its own founding
instance.**

**New standing-rule proposal, NETD-persistence lineage (candidate R16, for
Director/panel adoption, not unilaterally adopted by this audit):** *Any
cycle whose code invokes a `_full`/NETD-surfacing metrics function (or any
future function computing a byproduct value this program has designated
for mandatory disclaimer coverage) must persist that byproduct via the
already-established extraction convention (`netd_row()` or its successor)
into its own output for every cell/angle where it is computed — a
top-level disclaimer key traveling unconditionally is necessary but not
sufficient; it must not be allowed to cover an empty set by construction.
A cycle that computes such a byproduct, in any function, and does not
persist it, is the trigger — reusing an old, unpatched code path is not a
precondition.* This closes the specific loophole RT-4's own narrower
mandate left open this cycle (a disclaimer-travels requirement without a
persistence requirement). Not adopted by fiat here — flagged for the
Director's and panel's formal ratification, per this program's own
practice that Red Team names, and the Director/panel ratifies, a new
standing rule.

## 6. Combined Verdict: **PARTIAL**

Matching this sub-thread's own established vocabulary (Iterations 69, 70).

**Confirmed, cleanly, independently re-derived from primary source:** Rank
2's sigma-comparability CONFIRM at 41.6°; Rank 3's census result (two
CONSISTENT, one FLIPPED at 38.4° — a real, well-resolved, floor-clearing
reversal, not a measurement artifact); Rank 1a's clean settling PASS; Rank
3-ext's non-inverted, bit-exact zone reproduction; and, most
consequentially, **Rank 1b's complete sign-and-classification reversal at
`cpl=40`** — independently confirmed to be a genuine, full-window
phenomenon (all six points, not a boundary-adjacent subset), physically
coherent with this program's own established R13/R14 mechanism
(coherent-channel/incoherent-channel decoupling, `p_abs_w` flat to ≤0.6%
throughout) and, per EM's own prior-cycle dispersion-integral work
(independently re-applied here, correctly, and confirmed too large by
32×–96× at the smaller effect it was built to explain, let alone this
larger one), too large to be explained by smooth Yee-grid dispersion —
consistent with curved-boundary staircasing as the better-supported
mechanism, a genuinely new, correctly-drawn cross-reference this cycle's
own EM review adds to the permanent record.

**Genuinely new, open, not resolved by this cycle and not overclaimed as
such:** the 41.6°–42.0° window's status across `cpl∈{20,30,40}` is now
three-way unresolved, and — per the newly-adopted R15 addendum and
QUANTUM's own self-attack — cannot yet be told apart from a persistent
`R3`/`R4`-recipe-level artifact or a registration defect in the new family,
absent a third resolution point and a far-from-null ground-truth control
this cycle did not run. Two independently-caught, now-corrected-by-mandate
overclaims (Gate-5's provenance; the NETD "directly confirmed" language)
and one recurrence of a named, previously-declared-closed pattern
(NETD-byproduct persistence) leave Checkpoint criterion 4 as the closest
non-firing call in this sub-thread's history — logged accordingly, with a
forward-elevating clause and a candidate new standing rule, rather than
allowed to pass as routine.

## 7. Ranked candidate queue for Iteration 72

Reconciling all six Phase-5 seats' own rankings against this audit's own
independent findings — not a simple vote-count, weighted by what this
audit independently confirms is most load-bearing:

1. **A ground-truth sign-recovery control for the `R4` family** (QUANTUM's
   own #1, independently endorsed here as more urgent than the
   already-queued `cpl=50` check): 2–4 calls at an already-robust,
   far-from-null point (37.2°, 39.2°, or 39.8°), confirming `delta_scene`'s
   sign matches the known `cpl=20`/`cpl=30` answer, **before** any further
   `R4`-family spend. If this fails, every `R4` reading this cycle produced
   needs re-examination; if it passes, the `cpl=50` check below is
   trustworthy to run.
2. **A third resolution point (`cpl=50`, or per MATERIALS' own
   non-clean-multiple suggestion, `cpl=45`) at the same six interior
   angles** — the single test that distinguishes converging, oscillating,
   and genuinely non-convergent behavior in this window, per the newly
   adopted R15 addendum's own minimum-discharge requirement. Gated on (1).
3. **Close the sigma-comparability gap at both window edges**: 41.6° at
   `cpl=40`, and the interior sweep at native sigma — EM+QUANTUM's
   convergent pick, still open, so the window's full comparability chain
   (not just its interior) sits on one consistent resolution/sigma basis
   before any convergence-vs-divergence claim is drawn.
4. **38.4°'s flip at corrected sigma** (2 calls, QUANTUM's own
   self-falsified-Idealization-21 finding) — this cycle's own data show
   38.4° is near-null-adjacent by the identical R13/R14 signature that
   already made 41.8°/42.0° sigma-sensitive; the premise that licensed
   native-sigma-only measurement there no longer holds.
5. Same-shift Fixes #2–#3 above (Rank-3 `p_abs_w`/NETD extraction,
   `netd_row()` retrofit) should land before any of 1–4 are cited forward,
   not deferred to a later cycle — they are cheaper than any FDTD item on
   this list and directly close this cycle's own weakest evidentiary spot.
6. Retrofit Gate 5's runtime `sigma_e`-array check onto the `R3` family's
   own existing sigma-branch call sites (exp-091/092/093), which have
   never had an equivalent runtime check — MATERIALS' own #2, genuinely
   new, cheap, closes a gap this cycle's own Learned #4 named but did not
   execute.
7. PHOTONICS' own long-standing grazing-incidence validity check — still
   the single most-repeated undischarged item on the whole T28 board
   (named at Iterations 64/65/67/68/69/70/71).
8. Recalibrate (or explicitly re-justify) R13's `FLOOR` at each new `cpl`
   family before it gates another near-boundary classification —
   PHOTONICS' own new finding this cycle, non-load-bearing here (margins
   wide) but an unclosed comparability gap specific to cross-resolution
   work.
9. The unbiased margin-vs-distance rebuild on the full 31-point window
   (open since exp-090); the x-wall wavelength-generality leg (now
   **NINETEEN** consecutive cycles deferred, 076–094); the ritualization
   governance question (Iteration 61) — all still standing, unchanged in
   priority by this cycle's own findings.

Full record: `experiments/094-t28-cpl40-resolution-sigma-r3-census/` —
`phase1_proposal.md`, five Phase-2 blind critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`run.py`/`results.json`/`run_output.txt`, six Phase-5 blind reviews,
`gate5_wiring_defect_verification.py`, this audit.
