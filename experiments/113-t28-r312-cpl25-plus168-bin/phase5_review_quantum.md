# Phase 5 Review — QUANTUM OPTICS (exp-113, Panel Iteration 90)

**Fresh sub-agent, blind context.** I have not seen and did not seek out any
other seat's Phase-5 output this cycle. Charter (verbatim, PANEL.md):
"non-classical absorption, state-dependent or coherent interactions.
Expressibility contract: mechanisms enter the bench only as effective
classical parameters." Read `PANEL.md` in full; `LOGBOOK.md`'s RULED OUT
registry lines 1–1400 (R1–R31 in full; R32 does not yet appear in
`LOGBOOK.md` itself — it is recorded, pending, in this experiment's own
`phase2_redteam_audit.md`/`NOTES.md`, not yet transcribed into the
registry), the T28 opening (`sed -n '3094,3200p'`), and the full Iteration
89 entry (`sed -n '24215,24415p'`). Read `phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md` in full,
`run113.py`, `chunk_runner113.py`, `analyze113.py`, and `results.json` in
full. **No real FDTD was run by me — Phase 4 has not been re-attempted,
and my own charter's synthetic tests below are zero-FDTD Python
one-liners against already-committed code, not simulation calls.**

I am auditing my own seat's own prior-cycle work here more than any other
seat could: QUANTUM OPTICS' own Phase-2 critique this cycle is what caught
the Check-C direction-inversion defect (Fix 5/R32) in the first place, and
this document's job is to check whether the FIX that critique produced is
itself correct and unambiguous for a future cycle — the same self-auditing
posture this seat owes after founding R30 last cycle.

## Verdict: **CONFIRM-WITH-GAPS**

The core arithmetic Fix 5 ships is correct — I independently re-derived it
with eight synthetic constructions below and it behaves exactly as
specified in every case I could construct. Nothing in `NOTES.md` or
`results.json` overclaims what happened this cycle: the zero-real-r=312-
data outcome is reported accurately everywhere I checked. But I found
three genuine, previously-uncaught contract ambiguities in how
`direction_validated`/`low_percentile_outlier`/`high_percentile_outlier`
compose — gaps that did not matter this cycle (because no real data ever
reached the code) but WILL matter the moment a future cycle's crosstab
runs on real data, and nothing currently in the code or the DISCLAIMER
text closes them. That combination — correct core logic, real residual
interpretive risk for the next cycle that actually gets data — is what
"CONFIRM-WITH-GAPS" is for.

## 1. Is Fix 5b's own implementation actually correct? (tested, not read)

I did not trust the code by inspection alone. I imported `run113.py`
directly and ran eight synthetic constructions against
`resolved_unresolved_crosstab` and `classify_resolution_check`, covering
every branch I could identify in the source:

1. **Basic low-direction recovery** (resolved bins given lower mean corr):
   `direction_supported == "low"` — correct.
2. **Basic high-direction recovery** (resolved bins given higher mean
   corr): `direction_supported == "high"` — correct, and confirms the
   function is genuinely undirected in its own logic, not silently
   hard-coded toward "low" (a plausible failure mode given the function's
   name and purpose is specifically to check whether "low" is right).
3. **Degenerate split** (all-resolved mask): returns
   `n_unresolved=0`, `direction_supported=None`, with the documented
   `note` — correct, no crash, no silent divide-by-zero.
4. **`None` filtering** (synthetic zero-variance windows mixed in):
   correctly excluded from both populations before the mean/direction
   comparison — correct.
5. **Exact tie** (identical means): `direction_supported=None` — correct,
   neither tail wins by construction.
6. **Mismatched-length arrays** (`resolved_mask` length 48,
   `all_window_corrs` length 44): `zip()` silently truncates to the
   shorter array with **no assertion anywhere in the function** — this
   does not fire at the one real call site today (both arrays are always
   48-element, same-pattern outputs by construction in
   `analyze113.py`), but it is a real, currently-latent robustness gap,
   the same "silent misalignment" shape this program has paid for before
   (R29's own founding instance). Cheap to close: one `assert
   len(resolved_mask_48) == len(all_window_corrs_48)` at the top of the
   function.
7. **Full synthetic end-to-end chain** (fake 48-bin cpl=20/cpl=25 delta
   patterns run through `classify_resolution_check`, then the resulting
   null-scan fed into `resolved_unresolved_crosstab`): the named bin
   correctly registered as a `low_percentile_outlier` (2.08th percentile,
   forced by construction) while the crosstab, on the SAME synthetic
   pattern, found `direction_supported == "high"` — i.e., population-level
   evidence pointed the OPPOSITE way from the named bin's own reading.
   `direction_validated` correctly read `False` in this case. This is the
   scenario Fix 5b exists to catch, and it caught it correctly.
8. **The scenario that exposes the real gap** (below).

## 2. The residual contract ambiguity — three related gaps

### 2a. `direction_validated` conflates three distinct future outcomes into one boolean

`analyze113.py` line 99–100: `direction_validated =
(crosstab["direction_supported"] == "low")`. This is `True` only for
"low validated." It is `False` for THREE qualitatively different states
that a future cycle's real crosstab could produce: (i) "high" validated
— i.e., the population-level evidence actually confirms the **original**
`neighbor_correlation_check` premise (high correlation = real structure),
the opposite tail from what this cycle's code currently treats as the
candidate reading; (ii) a genuine tie (`direction_supported=None`); (iii)
a degenerate split (one population empty). A future Director reading
`direction_validated=False` in isolation cannot tell which of these
happened without separately reading the nested
`check_c['resolved_unresolved_crosstab']['direction_supported']` string —
and case (i) is not "uninformative," it is **positive evidence for the
opposite tail**, which the code has no mechanism to act on: there is no
`high_direction_validated` field, and no code path anywhere upgrades
`high_percentile_outlier` to an evidentiary reading even when the
crosstab actively supports "high." I confirmed this concretely (Test 2,
§1 above): a synthetic crosstab with `direction_supported="high"` produces
exactly this silent asymmetry.

### 2b. Population-level `direction_validated` and the named bin's own tail are independent facts, and nothing enforces their conjunction

I constructed a synthetic case (Test 8) where `direction_validated=True`
(the crosstab genuinely confirms the "low" direction, population-wide)
while the **named bin itself** is a `high_percentile_outlier` (100th
percentile) — the opposite tail from the one just validated. Nothing in
`classify_resolution_check` or `analyze113.py` computes or names the
conjunction "the named bin's own reading is a low-percentile outlier AND
that direction is independently validated at this geometry" — a future
Director must manually AND two separately-nested booleans
(`check_c['low_percentile_outlier']` and `check_c['direction_validated']`)
before citing the named bin as "candidate real structure," and nothing in
the DISCLAIMER states this explicitly as a required conjunction rather
than either flag alone.

### 2c. `check_a`'s own returned string goes stale the moment the crosstab runs, and sits next to the correct raw fields in the same frozen text

`classify_resolution_check` (line 372) hard-codes, at the moment of a
K=1-clearing SURVIVES reading: *"Check C reported undirected per R32/Fix
5, **NOT yet upgraded** to 'candidate real structure'"* — this string is
generated and returned BEFORE `analyze113.py` computes the crosstab
(`classify_resolution_check` is called at line 82 of
`analyze_r312_cpl25`; the crosstab is computed afterward, at line 90, and
only `check_c`'s dict — not `check_a`'s string — is mutated to carry it).
**`check_a`'s text is never regenerated afterward.** So in a future cycle
where the crosstab genuinely validates the low direction AND the named
bin qualifies (§2b's conjunction, satisfied), `build_result_text`'s own
frozen `result_text` (see `analyze113.py` line 228,
`f"Check A: {rc['check_a']}; "`) will still literally assert "NOT yet
upgraded" — permanently false at that point, sitting in the same string
as the correct `direction_validated=True`/`low_percentile_outlier=True`
raw fields a few clauses later (line 233–237). The raw truth is present
and recoverable, but a future citation that quotes `check_a` alone (the
exact "citation-shortening" failure shape R4/R9 exist to catch) would
carry the stale claim forward.

**None of 2a–2c fired this cycle** — `results.json` confirms
`resolution_check` was never computed at all (the gate-refused branch at
`analyze113.py` lines 142–198 exits before `analyze_r312_cpl25` is ever
called), so no live instance of any of these three states exists yet.
These are forward risks, not this-cycle defects — but they sit exactly
where Fix 5/R32 promised to close the ambiguity, and none is mentioned in
`NOTES.md`'s own account of Fix 5, which states only that synthetic tests
"behave correctly" (confirmed true, narrowly) without noting that
correctness under the tested cases still leaves this composition gap
open for the first cycle that gets real data.

## 3. Confirming the headline claim: no false implication of real validation

Independently checked, per the task brief: `results.json` has **no
`resolution_check` key at all** — `analyze_r312_cpl25` (the only call
site of both `classify_resolution_check` and
`resolved_unresolved_crosstab`) never executed, because the gate-refused
early-exit branch returns before reaching it (`analyze113.py` lines
142–198, confirmed by direct reading and by `results.json`'s own
`gate_refused: true`/`named_bin_reached: false` fields). `NOTES.md`'s own
language is honest and precise throughout: "Synthetic zero-FDTD unit
tests of ... `resolved_unresolved_crosstab` all behave correctly ...
crosstab correctly recovers the injected direction **on synthetic
data**" (never claims real-data validation); the Result section states
plainly "NOT REACHED"; the DISCLAIMER's own text ("`direction_validated`
stays False until `analyze113.py`'s own ... cross-tabulation ... shows
which tail ... this geometry actually supports") is accurate as written,
if — per §2a — silent on what "False" means across its three possible
causes. **I found no place where `direction_validated` is silently
miscomputed, defaulted incorrectly, or where any document implies real
r=312 validation occurred.** This part of the headline concern is clean.

## 4. Minor loose end (not adjudicated)

`phase1_proposal.md` §7 (line 397) cites **43/43** trust-suite checks;
`NOTES.md` (lines 107, 242) cites **41/41** twice, at Phase 3 and Phase 4.
I did not run `lab/validation/run_all.py` myself to adjudicate this (it
runs real, if small, FDTD sanity calls, and my task brief instructed me
not to run any real FDTD) — flagging the discrepancy for the Director to
reconcile, not resolving it myself.

## 5. Ranked top-3 candidate directions for Iteration 91

1. **Close the `direction_validated`/`check_a` composition gap (§2a–2c)
   before any future cycle's crosstab runs on real data.** Concrete,
   zero-FDTD, cheap: (a) expose a tri-state
   `resolved_unresolved_crosstab['direction_supported']` value directly
   at the `check_c` top level (not only nested), or add an explicit
   `high_direction_validated` field alongside `direction_validated`; (b)
   add a single, explicit, top-level `named_bin_evidentiary_reading`
   field computed as the actual required conjunction (`low_percentile_
   outlier AND direction_validated`, or the symmetric `high` case) rather
   than requiring a future reader to AND two nested booleans themselves;
   (c) regenerate `check_a`'s own text (or replace it with a
   post-crosstab-aware string) so it cannot go stale the moment real data
   changes `direction_validated` out from under it; (d) add the missing
   `assert len(resolved_mask_48) == len(all_window_corrs_48)` to
   `resolved_unresolved_crosstab`. This is squarely a "before the next
   cycle that gets real data" item — cheaper now, while nothing is
   load-bearing, than after a future cycle's Phase-5 has to untangle a
   stale `check_a` string sitting next to a correct crosstab.
2. **Re-attempt the `+168.75°`/r=312 leg at the top of Iteration 91 with
   a fresh, same-session R31 control**, per the Reconciled queue's own
   still-standing highest-value item. This is now the THIRD consecutive
   deferral of the single most-cited outstanding question in the T28
   sub-thread (exp-111: sequencing; exp-112: cost/density choice;
   exp-113: genuine R31-scaled refusal, this session running at 0.406×
   the historical rate — the opposite direction from exp-112's own
   2.19×-faster session). Two sessions now bracket a roughly 5× total
   range around "normal" throughput on this environment; if a THIRD
   attempt is refused again, that itself becomes a namable finding (either
   `COST_GATE_TOTAL_S`=10800s is too tight for r=312 on this class of
   session, or this program's compute environment has a wider throughput
   variance than any single R31 control point can safely characterize) —
   worth flagging explicitly, not silently re-attempting a fourth time
   without naming the pattern.
3. **Attempt a mechanistic (not data-driven) derivation of which
   correlation direction genuine sub-wavelength PEC-boundary structure
   SHOULD imprint under grid refinement, independent of either r=156's or
   r=312's own data** — R32's own text explicitly permits validating a
   recalibrated statistic's direction via "a mechanistic argument stated
   before the recalibrating data is seen," as an alternative to the
   cross-tabulation route Fix 5b implements. Given the r=312 leg keeps
   getting cost-gated out, a zero-FDTD analytic argument (from first
   principles: how a fixed near-field boundary condition's spatial
   correlation structure should behave under a congruent grid refinement,
   versus how uncorrelated Yee-grid discretization noise should behave)
   would let R32 be satisfied on this front even if the r=312 leg is
   deferred a fourth time — squarely this seat's own charter territory
   (distinguishing genuine field structure from instrument artifact), and
   the cheapest of the three items to execute.
