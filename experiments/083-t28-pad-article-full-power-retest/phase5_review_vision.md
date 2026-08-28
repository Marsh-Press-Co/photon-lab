# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 60 · exp-083

**Seat: VISION SCIENCE.** Fresh sub-agent, zero memory of any prior session
— including my own predecessor seat's Phase-1 lead on this exact cycle. Read
PANEL.md, AGENTS.md, LOGBOOK.md (RULED OUT R1–R9, ESTABLISHED, LIVE THREADS
in full, T28's complete history through Iteration 59/exp-082's close),
PLAN.md's Iteration-60 queue, and the complete `experiments/083-.../` record
in the specified order (`phase1_proposal.md`, `NOTES.md`, `run.py`,
`results.json` spot-checked, `run_output.txt`,
`null_permutation_control.json`, all five Phase-2 critiques,
`phase2_redteam_audit.md`). Blind to all other Phase-5 reviews of this cycle,
per PANEL.md's Phase-5 independence rule.

**Task, per the seat charter's own duty ("pin numeric thresholds... before
any run that scores against them") and the specific brief this cycle**:
independently verify the git-provenance restoration my own predecessor
seat's build was tasked with (frozen predictions committed BEFORE the run, at
`06cb96b`), and audit record hygiene — NOTES.md completeness, verdict-field
population, T1:N/A consistency, and whether any perceptual-threshold
language is misapplied anywhere in the corrected record, given this cycle
scores zero `C_thr` comparisons.

---

## 1. Git-provenance restoration — independently confirmed genuine, at the source

I did not take `NOTES.md`'s own claim ("frozen... strictly before `run.py`
was written or any FDTD call executed") on the write-up's word, and I did not
take Red Team's `phase2_redteam_audit.md` §0e on its word either — this
program's own R4/R9 standard requires re-deriving a "confirmed" claim, not
merely re-reading it. I ran the same class of check independently, from the
raw repository history:

```
$ git log --format='%H %ai %s' | grep 06cb96b
06cb96b798f82ef9cb9c28f2e7aac07d11728811 2026-08-28 00:05:22 +0000
  exp-083 Iteration 60 Phase 1: FROZEN PREDICTIONS for the full
  31-point/0.2deg PAIR_PAD-with-article re-test

$ git log --oneline -- experiments/083-t28-pad-article-full-power-retest/
e81c95e Phase 3/4: synthesis
df3c183 Phase 2: Red Team audit
99fadd2 Phase 2: ELECTROMAGNETISM blind critique
9a4830f Phase 2: QUANTUM blind critique
2f27521 Phase 2: PHOTONICS blind critique
1b90733 Phase 2: MATERIALS + THERMODYNAMICS blind critiques
556c185 Phase 1: self-scored PHASE 1 RESULTS + NOTES.md
4859940 Phase 1 WIP: full 31-point FDTD run complete, self-scoring in progress
cd99047 Phase 1 WIP: run.py script committed (predictions already frozen
  in 06cb96b, before this file existed); run actively in progress
06cb96b Phase 1: FROZEN PREDICTIONS for the full 31-point/0.2deg
  PAIR_PAD-with-article re-test

$ git show --stat 06cb96b
  Author: Clyde <clyde-colab@users.noreply.github.com>
  Date:   Fri Aug 28 00:05:22 2026 +0000
  [commit body: pre-registers the three-branch discriminator verbatim,
   states "This commit contains phase1_proposal.md ONLY -- predictions
   frozen before run.py is executed"]
```

`git show --stat 06cb96b` confirms the commit touches only
`phase1_proposal.md`. `cd99047`, the commit that first introduces `run.py`,
is timestamped `00:06:14` — 52 seconds after `06cb96b`'s `00:05:22`, and
strictly later in `git log`'s own commit order — and its own message states
explicitly that predictions were "already frozen in `06cb96b`, before this
file existed." The FDTD run itself only begins after that (the 125-call
sequence in `run_output.txt`, `1829.5s` total wall time, committed in
`4859940` after completion). **The chain is genuine and unbroken: predictions
→ run.py/run start → run complete → self-scoring → NOTES.md. No step is out
of order, and no commit bundles predictions with any result.**

This matches, digit-for-digit, Red Team's own `phase2_redteam_audit.md` §0e
finding (`git show 06cb96b:experiments/083-.../run.py` → path does not exist
at that commit; `phase1_proposal.md` at that commit contains no "PHASE 1
RESULTS" text). Two independent checks, run at different phases by different
seats, using different git plumbing (`git log`/`git show --stat` here vs.
`git show <rev>:<path>` there), converge on the identical conclusion.

**Verdict on this specific duty: the two-cycle-old tripwire (exp-081's
Phase-1/Phase-3 split freeze, exp-082's "predictions committed after a run
already 27/29 complete") is correctly, verifiably discharged this cycle.**
Iteration 59's own forward-flagged consequence — "a third consecutive
recurrence at Iteration 60 fires Checkpoint criterion 4 outright" — does not
apply: this is not a third recurrence, it is the correction. I find no basis
to disagree with Red Team's own §0e ruling; I reach the same conclusion by
an independent method, which is the standard this exact class of claim is
held to (R4).

One secondary observation, not a defect: `cd99047`'s own commit message
states the run is "actively in progress" at commit time — i.e. `run.py` was
committed as a mid-run WIP checkpoint, not after completion. This is *more*
disclosure than the minimum the git-provenance instruction requires (which
only binds the predictions-vs-run ordering, not requiring a WIP commit at
all) and does not weaken the ordering claim — `run.py`'s content still
postdates the frozen predictions regardless of when between run-start and
run-completion it was committed.

---

## 2. Record hygiene audit

### 2a. NOTES.md completeness

`NOTES.md` carries every section this program's own template requires:
Hypothesis, Setup (including the git-provenance paragraph reviewed above),
Result, Learned (7 numbered items), Next (6 items). All are populated with
substantive content, not placeholders. The Result section correctly
distinguishes the pre-registered PRIMARY discriminator from the
Phase-2/3-corrected reading (Attack 1) and from the two-tone tension's own
reversal (Attack 2) — both corrections are stated in `NOTES.md` itself, not
left implicit in `phase2_redteam_audit.md` alone. I checked this directly:
`NOTES.md`'s "Result" section (lines 51–75 of that file) already carries the
corrected "matches T28's own long-standing, unexplained `P_edge_A` family...
NOT yet demonstrated to be article-intrinsic" language and the "It is NOT
resolved, and this record does not adopt that reading" language for the
two-tone claim — i.e., the fix-docket corrections are genuinely folded into
the primary record, not merely promised in `phase3_synthesis.md` and left
undone in the document a future cycle would actually read first.

### 2b. Verdict fields populated

All five Phase-2 critiques carry a filled `## Verdict:` line (all
support-with-changes) and a filled "single parameter change" field — none
left blank or deferred. `phase2_redteam_audit.md` carries a filled overall
ruling (PROCEED-WITH-MANDATORY-FIXES) and a filled Checkpoint ruling for all
five criteria (§4), each reasoned individually, not defaulted. This cycle's
own Combined Verdict is not yet stated as a single word by any document I was
handed to read (Phase 5 across all seats is what produces that, per PANEL.md
§Phase 5) — appropriately, since no Phase-5 review exists yet at the point
Phase 3 was written. I supply my own verdict below (§4).

### 2c. T1:N/A disposition — consistent throughout

Checked every document in the packet for T1 disposition language:
`phase1_proposal.md` §3 states "N/A" explicitly and gives the reason
(instrument-fidelity/generalization work, not a constraint-3 mechanism
candidate). `NOTES.md` does not restate T1 explicitly in its own prose but
makes no claim inconsistent with N/A anywhere — no sentence in its Result or
Learned sections is phrased as evidence for or against any of the four
phenomenon constraints or the T1 escape routes (σ(I), σ(x,t), angular
selectivity, sub-threshold). `phase2_redteam_audit.md` §4 (Criterion 1 and
Criterion 2 rulings) independently reasons through T1/constraint
non-engagement explicitly, not by precedent alone, and concludes N/A.
`phase3_synthesis.md` §6 restates the identical Criterion-1/2 N/A rulings.
**No document in this cycle's record states or implies a constraint-3 claim
anywhere I could find; the T1:N/A disposition is applied consistently across
every phase and every seat, including the two critiques (THERMODYNAMICS,
QUANTUM) that come closest to touching energy/mechanism questions — both
explicitly scope their own findings as pre-constraint instrument work, not
phenomenon-program evidence.**

### 2d. C_thr / perceptual-threshold language — confirmed not misapplied, and this is my own charter's specific duty

My charter's standing duty is to "pin numeric thresholds, with sources,
BEFORE any run that scores against them." I checked whether this cycle uses
`C_thr` — the one perceptual-threshold quantity it touches at all — as a
**scoring/gating** threshold anywhere, or only as disclosed context. Grepped
every occurrence across `phase1_proposal.md`, `run.py`, and `results.json`:

- `phase1_proposal.md` §2 (parameter table): `C_thr = gs.c_thr(3.0, 0.4,
  bar="lab") = 0.005`, labeled explicitly **"Perceptual bar (context only,
  not gating T1)"** — the same frozen photopic lab bar this bench has used
  since T2, sourced, not invented for this cycle.
- §4c: `A_scene / C_thr` listed under **"Secondary, disclosed-not-gating
  diagnostics"** — explicitly not part of the pre-registered §4a
  discriminator that actually decides the branch classification.
- `run.py` line 94 computes `C_THR_LAB` once, from the established
  `gs.c_thr()` function (not hand-typed); line 330 prints it as
  `[secondary]`, matching the disclosed-context labeling; line 400 stores it
  in `results.json` under the same non-gating key.
- The self-scored "PHASE 1 RESULTS" and `NOTES.md`'s "Result" section both
  report `A_scene/C_thr=0.7622` as context only — neither document uses this
  number to pass or fail anything, or to support or reject any branch of the
  three-branch discriminator.

**Confirmed: this cycle scores zero `C_thr` comparisons anywhere — the
quantity appears exactly once, in a disclosed, non-gating role, correctly
carrying forward the R9-corrected convention (same-units, same-normalization
discipline) exp-082 established for exactly this quantity.** This also means
my own charter's specific duty — pinning a perceptual threshold BEFORE any
run that *scores against it* — is trivially satisfied by non-engagement: no
run in this cycle scores against `C_thr`, so there is no gate for me to
audit for correctness or sourcing beyond confirming the bar itself
(`gs.c_thr(3.0, 0.4, bar="lab")`) is the same already-frozen T2 quantity this
bench has used unmodified for many prior cycles, not a fresh, unverified
number. I checked this is not a new definition: the call signature and the
resulting `0.005` figure match the value already cited in exp-082's own
record (`phase1_proposal.md` §2 here states it explicitly as reused, not
re-derived).

I also checked for any language elsewhere in the record that might silently
smuggle a perceptual-detection claim under a different name — e.g., any
sentence characterizing `delta_scene`'s amplitude, `ratio`, or the branch
classification as "visible," "detectable," "perceptible," or similar. I
found none. Every quantitative claim in this cycle is stated in the record's
own native units (Weber contrast, field amplitude, `R²`, `p`-values,
degrees) without perceptual-visibility language attached. This is correct
discipline for an instrument-fidelity cycle carrying T1:N/A — perceptual
claims are exactly the category R9 (LOGBOOK) exists to police for
unit-commensurability, and this cycle does not create a new instance of that
failure shape.

---

## 3. Independent spot-check of the Red Team's own most consequential finding (Attack 2)

Not required by my own duty above, but load-bearing enough to the cycle's
own Combined Verdict that I checked it rather than accepting it purely on
the strength of Red Team's write-up. I did not re-run the Monte Carlo
myself (that would duplicate, not add to, the four independent
reproductions already on record — Red Team's own audit, and this program's
own R4 "recompute, don't merely restate" standard applies to figures I cite,
not to re-deriving every already-independently-reproduced statistic a fourth
time). I did verify the **logical structure** of the reversal directly
against `results.json`'s own committed arrays: the lag-1 autocorrelation
claim (`r≈0.93–0.95`) is a property of the single-tone residuals, which are
deterministic given `delta_scene` and the fixed `P_edge_A` period — I
recomputed this specific number independently:

```python
resid = delta_scene - fitted_single_tone(P_edge_A)
np.corrcoef(resid[:-1], resid[1:])[0,1]  # -> 0.9508
```

This matches Red Team's §0h figure exactly. Given residuals this strongly
autocorrelated, a full-permutation (non-order-preserving) null is known,
independent of this specific dataset, to be anti-conservative — this is not
a new statistical principle invented for this cycle, it is the same
underlying fact R6's Iteration-50 addendum already established program-wide.
The reversal Red Team reports (`p=0.581` under the order-preserving
companion vs. `p<0.001` under the naive permutation) is the expected
consequence of that fact applied to this exact residual structure, not an
implausible or cherry-picked result. I find no reason to doubt Attack 2's
ruling.

---

## 4. VERDICT

**PARTIAL.**

The cycle delivers a genuine, hard-won, first-of-its-kind result for this
nine-cycle-plus T28 sub-thread: at full statistical power, `delta_scene`'s
dominant periodicity is pinned, decisively and doubly-instrument-
corroborated, to T28's own long-standing `P_edge_A` family rather than the
`PAD`-tied `P_continuity` family — resolving exp-082's own power deficiency
cleanly. The git-provenance restoration this cycle was specifically tasked
with is genuine, independently verified at the source by two different
seats using two different methods (mine here, Red Team's in Phase 2) — the
two-cycle-old tripwire is correctly closed, not merely claimed closed. The
record's own self-correction discipline is exemplary: Red Team's Phase-2
audit caught and reversed a materially consequential overclaim (the two-tone
"resolved... genuine partial admixture" reading, independently arrived at by
two of five blind critics) using a from-scratch synthetic calibration and an
order-preserving companion test neither raising critique ran, and Phase 3
adopted the correction in full, with zero overrides, folding it into the
primary record (`NOTES.md`) rather than leaving it stranded in the audit
document alone.

This is PARTIAL, not PROMISING, for the same reason Iteration 59's own
Combined Verdict was PARTIAL: the substantive question this whole sub-thread
exists to answer — what actually produces T28's oscillation, and whether the
article's own rim is a genuine causal contributor — remains open. This
cycle sharpens the open question rather than closing it: "Branch B" is now
correctly labeled a period-family match, not a demonstrated mechanism
(PHOTONICS'/MATERIALS' shared attack, independently confirmed by Red Team's
own Fresnel-number finding that the far-field formula PHOTONICS applied is
not even the right regime), and the two-tone admixture question is
explicitly left open pending a properly pre-registered null-calibration test
— a real, disclosed non-resolution, not a hidden one. Two governance notes,
neither outcome-determining: (1) EM's R5 pre-registration gap (the
null-permutation control is disclosed post-hoc, not in the same freeze
commit as the falsifiable bands) is now confirmed a recurring pattern across
four T28 cycles since R5's adoption — correctly logged as a discipline note,
not escalated to a fresh rule, and I concur with that disposition; (2) this
cycle's own record does not yet contain a Combined-Verdict line stated in
`NOTES.md` itself — appropriate, since Phase 5 (this layer) is what
produces it, not a gap in Phase 3/4's own completeness.

---

## 5. Ranked top-3 candidate directions for Iteration 61

1. **MATERIALS' article-radius discriminator (`R_OUT` sweep at fixed
   `PAD`).** Independently confirmed by every seat that touched this
   question this cycle (MATERIALS raised it, PHOTONICS converged on it from
   its own charter angle, Red Team's Attack 1/3 ruled it the single
   highest-priority item on the board) — and I concur, from my own charter's
   vantage: this is the only test that can determine whether Branch B's
   period-family match reflects a genuinely realizable, article-size-
   dependent geometric effect or a pre-existing domain artifact that would
   persist regardless of what physical object occupies the scene. That
   distinction matters directly for any future constraint-3 engagement this
   sub-thread's findings eventually feed into — a witness-scene article has
   a real, bounded size range; a domain-geometry artifact does not scale
   with it at all. Cheap (≈31 calls, one alternate radius, zero new
   machinery).

2. **A properly pre-registered null-calibration test (`G0-e(ii)`-style) for
   the two-tone admixture construction, run BEFORE any future cycle treats
   the `PAD`-continuity component as resolved.** Red Team's own reversal
   (Attack 2) is itself only as trustworthy as its own order-preserving
   circular-shift null, which is coarse at `n=31` (minimum resolvable
   `p≈0.032`, as Red Team's own §0j discloses) — this is not the final word,
   it is the correctly-cautious current word. A dedicated, pre-registered
   synthetic-recovery-plus-calibration gate, built and frozen before it
   scores real data, is the only way to close this the way R6's own
   Iteration-50 addendum requires before a significance claim on this
   construction earns `RESOLVED`. Zero new FDTD, reuses committed arrays.

3. **The near-null σ(I) article follow-up (`off_pass`, Tier 1 item 6,
   still-standing from Iteration 59's own board).** From my own charter's
   angle specifically: every quantitative result this cycle produced was
   measured against the established flagship (strongly-absorbing) article
   only. A weakly-absorbing article changes the scattered-field amplitude
   this cycle's own EM companion instrument (§4b) depends on for its
   cross-term reasoning, and — germane to my own duty — would be the first
   opportunity in this sub-thread to check whether a near-null-absorption
   article brings the scored contrast anywhere close to a perceptual regime
   worth pinning a real gating threshold against, rather than the
   context-only role `C_thr` has played in every T28 cycle to date. Not
   urgent on T1 grounds (still N/A, still instrument work) but the next
   natural point at which a perceptual bar might need to stop being
   context-only.

Also still open, not re-ranked ahead of the above: QUANTUM's own
lossless-PEC-only-disk control (Tier 1 item 7), the `PAIR_ABSORB40`/
`C80−C40` extension (Tier 1 item 8), and the x-wall wavelength-generality leg
(Tier 2 item 9, now seven-plus consecutive cycles deferred) — none of these
bear as directly on this cycle's own two open findings (causal-label
attribution, two-tone admixture) as the three ranked above.

No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this review.
