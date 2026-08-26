# VISION SCIENCE — Phase 5 Review · Panel Iteration 51 · exp-074

*Fresh sub-agent, VISION SCIENCE charter (PANEL.md: human perceptual
limits — contrast thresholds, luminance edge detection, spectral
sensitivity, adaptation, temporal sensitivity, saccadic/attentional
blindness. Central question: what would make a human eye FAIL to
register something physically present? Duty: pin numeric thresholds,
with sources, BEFORE any run that scores against them). Blind to every
other seat's Phase-5 review this cycle. I am also, unusually, this
cycle's own Phase-2 critic on this exact experiment (a different fresh
instance) — I do not treat my own prior critique's "not load-bearing"
verdict as still standing; Red Team's audit (§5) already explained why
it structurally could not survive being read alongside the other four
blind critiques, and I re-derive everything below from scratch rather
than defer to either version of myself.*

**Constraint-3 relevance:** none. This is a pure statistics/instrument
cycle (T1 escape route N/A, explicitly and correctly stated in
`phase1_proposal.md` §3) — no perceptual claim is made anywhere in this
thread, so my charter's substantive domain (contrast thresholds,
adaptation, etc.) has nothing to adjudicate here. What *is* squarely
inside my charter is the cross-domain duty stated in PANEL.md's own
one-sentence summary of my seat: **pin numeric thresholds, with sources,
before any run scores against them** — a duty this program has already
established (LOGBOOK R4/R6/R7) generalizes to any numeric bar in any
domain, not just perceptual ones. I apply it here to (a) the falsifiable
predictions' own pre-registration order, (b) the Monte-Carlo tolerance
formula's arithmetic, and (c) whether the write-up's own numeric claims
reproduce against the committed data — plus a legibility pass, per the
task brief.

---

## 1. Independent computational re-verification

Re-ran `desk_check_pricing.py` and `fit_and_calibrate.py` unmodified.
Both reproduce their own committed `*_results.json` bit-for-bit
(`CHECK0 pass=True worst_rel_err=0.00e+00`; `fit_and_calibrate`'s
`per_pair_fit`, `calibration`, and `combined_verdict` fields match the
committed JSON exactly). I additionally wrote independent scratch
verification (not committed — matching Red Team's own precedent of
short extensions rather than script changes) to check every headline
number in `phase4_results.md`/`NOTES.md` directly against
`fit_and_calibrate_results.json`, rather than trusting the prose. Results
below.

### 1a. `lev9_Rq` and `z9` — CONFIRMED, exact

`per_pair_fit` in the committed JSON: `lev9_Rq` = 0.5858 / 0.5932 / 0.5960
/ 0.5883 (C40–C60 / C60–C70 / C70–C80 / C40–C80) — matches the
pre-registered "0.586–0.596" in `phase3_synthesis.md` §4 exactly, and
`z9` = 0.843 / 5.033 / 1.634 / 0.345 matches `phase4_results.md`'s table
to the last printed digit. These are the two numbers the primary
prediction is built on; both check out.

### 1b. i.i.d.-leg inflation figures — CONFIRMED, exact

Recomputing `rate/alpha` directly from `calibration.<pair>.raw.iid_leg`
for every (sigma, alpha) cell and taking the max at α=0.01 per pair
gives 11.20× / 10.30× / 8.70× (C40–C60 / C60–C70 / C70–C80) — matches
`phase4_results.md`'s table exactly. The "8.7×–11.2×" headline figure is
correct.

### 1c. Circular-shift-leg figures — CONFIRMED, exact

Same check on `circ_leg` at α=0.01: 38.90× / 46.10× / 44.10× — matches
the table exactly. The "58–65%" raw rejection rate at α=0.10 also checks
out (57.9%/63.4%/64.9%, rounds to 58–65%).

### 1d. Monte-Carlo tolerance-band arithmetic — CONFIRMED, correctly the standard 3σ Bernoulli CI

`tol = 3·√(α(1−α)/K)`, `calibration_pass()` line: `tol = 3 *
math.sqrt(a * (1 - a) / K_CAL)`. At α=0.01, K=1000: `tol =
3·√(0.01·0.99/1000) = 3·√(9.9e-6) = 3·0.0031464 = 0.009439`, giving band
`[0.00056, 0.01944]` — I independently recomputed this by hand and by
script; it matches the code's own printed band (`[0.0006,0.0194]`)
exactly. This IS the standard normal (Wald) approximation to the sampling
distribution of a Bernoulli-rate estimator under H₀: true rate = α,
estimated over K i.i.d. draws, SE = √(α(1−α)/K), 3σ ≈ 99.7% coverage.
The formula is correctly sourced (it is a textbook identity, not an
invented threshold) and correctly implemented — no defect here, and no
new derivation is owed the way `phase1_proposal.md`'s three unsourced
bars (`cond9≥300`, `VIF_Rq≥15`, `lev_ratio≥0.90` — my own Phase-2
finding, confirmed by Red Team §5 and correctly relabeled as heuristic in
`phase3_synthesis.md` §5) were owed one. One caveat worth naming
explicitly, not previously stated anywhere in this thread: at α=0.01,
K=1000, the expected count under H₀ is only 10 — the normal approximation
to a Binomial(1000, 0.01) is workably accurate there (Binomial exact 3σ
one-sided tail sits within ~15% of the Wald figure at this n·p) but is
not exact; this is a second-order concern given the observed rates
(39–112 per 1000, 4–11× outside even a generously exact band) and does
not affect this cycle's verdict, but a future cycle running this
calibration at a smaller `K_CAL` or more extreme `α` should use an exact
(Clopper–Pearson) or Wilson interval rather than Wald at that point —
flagged for the record, not gating.

**Finding 1 [CONFIRMED, not new]:** the Monte-Carlo tolerance band is
correctly sourced and correctly computed. My own Phase-2 critique's
"three of five bars unsourced" finding does NOT apply to this cycle's
actual gating mechanism — `phase3_synthesis.md` §5 explicitly stops using
`cond9`/`VIF_Rq`/`lev_ratio` as gates and uses only the first-principles
tolerance band, exactly per my own docket item 5 and Red Team's
confirmation of it. This is the discipline working as intended one cycle
later.

---

## 2. Pre-registration order — verified against actual git history, not prose

The task specifically asks me not to trust the documents' own ordering
claims. I ran the check directly:

```
git log --follow --format='%H %ai %s' -- .../phase3_synthesis.md
  3aaae38  2026-08-26 03:36:25 +0000  Phase 3: Director synthesis ... (predictions frozen)

git log --follow --format='%H %ai %s' -- .../fit_and_calibrate.py
  3aaae38  2026-08-26 03:36:25 +0000  (same commit)

git log --follow --format='%H %ai %s' -- .../fit_and_calibrate_results.json
  af2f381  2026-08-26 03:38:00 +0000  Phase 4: official run -- HALT_NULL_MISCALIBRATED_9COL
```

`git show 3aaae38 --stat` confirms that commit contains exactly
`NOTES.md`, `fit_and_calibrate.py`, `phase3_synthesis.md` — **not**
`fit_and_calibrate_results.json`. `git show af2f381 --stat` confirms the
results file, `phase4_results.md`, and the `NOTES.md` update land in a
separate, later commit, 95 seconds after. **Finding 2 [CONFIRMED]:** the
committed git history independently corroborates the claimed ordering —
the script and the frozen predictions were committed as a unit, with no
results artifact present, before a second commit added the actual run
output. This is a real, verifiable pre-registration, not merely an
assertion the prose makes about itself, and it is the strongest form of
evidence this program's own tooling can produce (a commit that
structurally cannot contain a result it depends on).

**Caveat, not a defect, worth naming for the record:** this checks that
*something calling itself the prediction* was committed before *something
calling itself the result*. It cannot rule out that the same author, in
the same continuous authoring session, had already executed an
uncommitted "dev run" of the identical script before writing the
prediction narrative — `phase3_synthesis.md` §8 itself discloses "runs in
~25s ... measured, this cycle's dev run," which describes timing a run of
the full pipeline (necessarily including the calibration Monte Carlo) at
some point before the officially-dated commit. Because the script is
**deterministic with fixed, frozen seeds** (`SIGN_FLIP_SEED=74051`,
`CAL_SEED=74052`, stated as "frozen at Phase-3 commit" in both the code
comments and `phase3_synthesis.md` §3) and no seed or parameter changed
between that dev run and the official Phase-4 run (confirmed:
`phase4_results.md`'s own header states this run "reproduces, bit-for-bit
on every reported quantity except `elapsed_s`, the development run
disclosed and bounded in `phase3_synthesis.md` §4"), the numeric
prediction (`HALT`, and the specific `lev9_Rq` figures) was in fact known
to whoever wrote the "frozen" prediction narrative at the time they wrote
it — the qualitative HALT direction was disclosed as a *design-time*
computation (correct: `lev9_Rq` requires no calibration Monte Carlo,
only the fitted `X9`, and this is genuinely computable before running
`calibrate_null` at all), but the specific inflation *magnitudes* quoted
in the same prediction paragraph (the "comparable-or-larger... 1.7×-5.7×"
framing) read as informed by having already seen the answer. This is a
structural limitation of this program's own single-continuous-session
Director model (one agent designs the test, states the prediction, and
executes it, all without an air gap) rather than an exp-074-specific
violation — no house rule currently requires a temporal air-gap between
writing a script and running it once for development purposes, only that
the *committed, scored* run be the one that follows the *committed*
prediction, which git confirms happened here. I flag this as a candidate
gap in R6/R7's own text (neither currently addresses same-session
dev-run contamination of a "frozen" qualitative prediction) rather than a
finding against this specific cycle, which followed every currently-
written rule.

---

## 3. New findings this Phase-5 pass surfaces (not caught in Phase 2, since Phase 2 pre-dates Phase 4)

Phase 2's five critiques and Red Team's audit all reviewed
`phase1_proposal.md`/`desk_check_pricing.py` — none of them, structurally,
could have checked `phase4_results.md`'s own arithmetic, since it did not
exist yet. I checked it against the committed JSON directly.

### Finding 3 — `phase4_results.md`'s "72 cell combinations" is an arithmetic error; the true count is 36

`phase4_results.md` line 20: *"the 9-column null-calibration gate fails
at every one of 72 cell combinations (3 free pairs × 24 cells: 3 sigmas
× 3 alphas for the i.i.d. leg, plus 3 alphas for the circular-shift
leg)."* Arithmetic check: 3 sigmas × 3 alphas = 9 i.i.d. cells + 3
circular-shift cells = **12 cells per pair**, not 24; 3 pairs × 12 = **36
total cells**, not 72. I confirmed this directly by counting the actual
`detail` dictionaries in the committed JSON:

```
C40-C60: n_cells=12, n_fail=12
C60-C70: n_cells=12, n_fail=12
C70-C80: n_cells=12, n_fail=12
total cells across all pairs: 36
```

The **substantive claim survives** — every one of the 36 real cells does
fail, so "fails at every cell" is true; only the total count cited (72
vs. 36, and the "24 cells" sub-total, vs. 12) is wrong, by a clean factor
of 2. This is exactly the class of hand-typed, not-invoked figure R4
exists to catch (the code prints per-cell pass/fail but never prints or
computes a 72 or 24 anywhere — these numbers exist only in the prose,
not the script's own output), and it is a fresh instance, in the very
document meant to be this cycle's authoritative record, one cycle after
R4 was extended specifically to Phase-5-reviewer re-checking (LOGBOOK
Iteration 50). Non-load-bearing (doesn't change the Combined Verdict)
but should be corrected in place per house convention.

### Finding 4 — the "3.5×–5.9× worse than the i.i.d. leg at every α" claim does not hold at α=0.10 under any consistent, reproducible reading

`phase4_results.md` (and, propagated identically, `NOTES.md`): *"this
one measurably is not [indistinguishable from i.i.d.] — it is 3.5×–5.9×
worse than the i.i.d. leg at every α."* I computed, directly from the
committed JSON, the ratio of the circular-shift rejection rate to the
i.i.d. leg's own worst (max-over-sigma) rejection rate, matched at the
**same** α — the only reading consistent with how the immediately
preceding sentence defines "the i.i.d. leg's worst inflation... at
α=0.01":

| Pair | ratio @ α=0.01 | ratio @ α=0.05 | ratio @ α=0.10 |
|---|---|---|---|
| C40–C60 | 3.47× | 2.74× | 2.24× |
| C60–C70 | 4.48× | 3.30× | 2.63× |
| C70–C80 | 5.07× | 3.22× | 2.66× |

At α=0.10, the ratio is 2.2×–2.7× across pairs — clearly below the
claimed 3.5× floor, at every pair, not a rounding-margin miss. I tried
three other plausible conventions (matching the i.i.d. leg's *median* or
*minimum* sigma at each α instead of its *max*) and none produces a
range that (a) reproduces "3.5×–5.9×" exactly and (b) holds "at every
α" simultaneously — the ratio decreases monotonically and substantially
as α grows from 0.01 to 0.10 under every convention I tested, which is
also the physically sensible direction (an anti-conservative null's
excess-rejection-rate multiplier shrinks as the nominal rate rises toward
the actual rejection rate's own ceiling). My best reconstruction is that
"3.5×–5.9×" was computed only at α=0.01 (where the max-over-sigma
convention gives 3.47×–5.07×, closest to the quoted range) and the
qualifier "at every α" was added in prose without re-checking the other
two alphas against the same computation. **This is not load-bearing** —
the substantive point (circular-shift leg fails far worse than i.i.d.,
at every pair and every α individually, just not by a *uniform*
multiplicative factor) is still true and is actually the more important
half of the claim; only the specific numeric range attached to "at every
α" is unsupported as stated. Recommend either restricting the range
claim to α=0.01 explicitly, or computing and reporting the true
per-alpha range (approximately 2.2×–6.7× depending on which sigma
convention is used, itself worth stating explicitly since the ratio is
sigma-convention-dependent in a way the prose does not disclose).

Both findings are numeric-legibility defects of exactly the shape my
charter is chartered to catch (a number in prose that a reader is
invited to trust without it being reproduced from the committed
artifact) — I flag them because nobody else in this cycle's process
could have: Phase 2's five critiques and Red Team's audit all predate
`phase4_results.md`'s existence.

---

## 4. Legibility pass on `phase4_results.md` / `NOTES.md`

Task-specified question: could a reader unfamiliar with this thread
follow why "the null used to test z9=5.03 is itself miscalibrated" means
the mechanism question stays open rather than resolved either way?

**Yes, and it is explicitly, correctly guarded against the most likely
misreading.** `phase4_results.md` §"The real fit" states it plainly: *"is
`z9=5.03`... real, or an artifact... ? The answer, from this run: we
still do not know, and — this is the substantive finding — we now know
why we cannot know with this instrument: the null construction that
would answer it is itself badly miscalibrated... `z9=5.03`'s own naive
OLS SE cannot be trusted as a significance statement in either
direction."* This correctly forecloses the tempting but wrong inference
that "anti-conservative null ⇒ the observed z9 is probably a false
positive" — an anti-conservative null means H₀-true data gets rejected
too often, which says nothing about whether *this particular* z9=5.03
reflects a real effect or noise; it only says the significance threshold
z9 was compared against cannot be trusted, in either direction. The
document states this explicit disjunction rather than leaving it
implicit, which is the correct discipline and better than several prior
T28 cycles' write-ups (e.g., exp-073's own "144/144" overclaim, R4's
addendum) on this exact axis. NOTES.md's "Learned" section repeats the
same framing consistently. I found no place where the two documents
imply a directional lean the calibration failure does not license.

One legibility gap, minor: neither document states, in one sentence, WHY
an anti-conservative null (over-rejects under true H₀) is the *specific*
failure mode that makes the test uninformative in *both* directions
rather than just conservative-in-one-direction — a reader who knows
"anti-conservative" only as jargon for "too eager to reject" could
reasonably (if incorrectly) conclude "then a low p-value is even less
trustworthy as evidence of a real effect, but a HIGH p-value would still
mean no effect" — which is false (the calibration failure says nothing
about the null's behavior when H₀ is false, only when H₀ is true, so
absence of significance under this exact null is equally uninformative).
This asymmetry is never stated. Not a correctness defect in what IS
written, but an omission a fully unfamiliar reader could trip on;
cheap to add one clause.

---

## 5. Cross-reference resolution check (this program's own repeated defect pattern)

Checked every load-bearing citation in this cycle's chain that a prior
seat's review had not already verified:

- `exp-072/phase5_review_em.md` §6 ("Ranked candidate directions") —
  confirmed contains `cond = 529`, `36.6×` VIF, `6.0× SE inflation`,
  `4.9/3.0/4.3/4.7` z-ratios, "cannot reach 2σ" language, verbatim.
- `exp-072/phase5_review_quantum.md` §3 — confirmed contains `|L|` values
  including `26.8`, peak `35.7–36.7` at `T=3.49–3.55°`, verbatim.
- `exp-073/phase5_redteam_audit.md` §6.2 — confirmed titled "Ranked queue
  for Iteration 51," under §6 "For the Director's LOGBOOK entry."
- `exp-073`'s own committed `5.4×/2.3×/1.7×` figures (α=0.01/0.05/0.10,
  i.i.d. leg) — confirmed present, independently re-derived and
  reproduced four times over inside exp-073's own record
  (`phase2_redteam_audit.md`, `phase4_results.md`,
  `phase5_review_quantum.md`) — exp-074's citation of "5.4× worst, at the
  same α" (`phase4_results.md` line 23) is accurate.
- PLAN.md lines 2764–2840 (Iteration-51 queue) and LOGBOOK.md's T28
  thread / Iteration-50 entry — read in full; exp-074's own framing of
  "queue item 1," "queue item 5," R6/R4 addenda, all match the source
  documents' actual content and section structure.

**Finding 5 [no defect found]:** every cross-reference I checked resolves
correctly to real content matching the citing document's description —
a clean result, consistent with the fact that this cycle's Red Team audit
already ran an unusually thorough independent-reproduction pass on every
Phase-1/Phase-2 claim before Phase 3 was written. The two arithmetic
slips I found (§3, Findings 3–4) are self-contained numeric claims about
this cycle's own JSON, not broken cross-references to other documents.

---

## 6. Verdict

**PROMISING** (as a methodological/instrument result, not as a T28
mechanism finding — matching every prior cycle's own correct scoping).

Reasoning: the primary and secondary falsifiable predictions were
genuinely pre-registered in the strongest sense this program's tooling
can demonstrate (§2: a git commit containing the script and the
prediction, provably absent the results file, followed 95 seconds later
by a second commit adding only the results). Both predictions were
confirmed, with wide margin, on independently-reproduced numbers (§1).
The underlying instrument (`CHECK0`, `cond9`/`VIF_Rq`/`lev9_Rq`
machinery, the two-leg calibration gate, the Monte-Carlo tolerance band)
is correctly engineered and correctly sourced where it needs to be
(§1d). R7 is a genuine, well-motivated generalization, and this cycle is
a real demonstration of the panel's own self-correction machinery working
across a Phase boundary: two blind Phase-2 critics caught a real defect
in the pricing-only method, Red Team independently reconfirmed both by a
third method and found a mechanism-level generalization neither critic
stated, and the Director adopted 100% of the docket without override —
this is the cleanest single-cycle self-correction sequence in this
sub-thread's six-cycle history. The two numeric slips I found (§3) are
real but non-load-bearing, and — this matters for classifying the
verdict — they occurred in the one document class (`phase4_results.md`,
written after Phase 2 closed) that no other seat has yet had the
opportunity to check; they are not evidence the docket process failed,
they are evidence the docket process's own coverage window (Phase 1→2)
does not extend to Phase 4's own write-up, which is exactly what Phase 5
exists to close.

This is **not** RULED-OUT-worthy: the underlying differential/two-tone
instrument itself is explicitly kept, not retired (`phase3_synthesis.md`
§6, `phase4_results.md` §"What this means for R7"), and the T28
mechanism question (`z9=5.03` at C60–C70) remains genuinely open, a
real, well-characterized unresolved finding rather than a dead end. It is
**not fully PARTIAL** either in the sense of "half the claims survive
scrutiny" — every claim I independently checked in this cycle's own
governing documents (`phase3_synthesis.md`, `fit_and_calibrate.py`, the
committed JSON) reproduces correctly; the only defects are two isolated,
non-gating arithmetic slips in the post-hoc narrative layer, of a kind
this program has a standing, working process (R4, extended twice now) for
catching and correcting without re-litigating the substance.

---

## 7. My ranked top-3 candidate directions for Iteration 52

1. **Correct the two numeric slips (§3) in place, per R4, before anything
   else touches this record.** Cheapest possible action (a text edit,
   zero computation), and this program's own house discipline requires it
   be done before the next cycle inherits either wrong figure. Explicitly
   NOT worth a full cycle's lead — bundle as a same-shift correction the
   way exp-070's Iteration-47 R4 instance was handled.

2. **PHOTONICS' queued WKB/adiabatic boundary-reflectance analytic
   model for the graded-loss `ABSORB` band** (PLAN.md Iteration-51 queue
   item 4, explicitly named in `phase3_synthesis.md` §6 as one of the
   qualitatively-different strategies that WOULD authorize a further
   attempt on this sub-thread). Queued and dropped twice already
   (Iterations 46/47) without execution — the seventh-cycle decision
   rule this cycle commits to (§6, `phase3_synthesis.md`) explicitly
   requires exactly this kind of "qualitatively different" approach
   (no fit, no null, a from-first-principles reflectance-phase model) if
   T28's mechanism question is to move at all. Zero FDTD, engages a
   seat's own charter physics directly rather than re-deriving statistics
   a sixth time — this program's own stated preference (Red Team's
   Phase-5 final audit on exp-073 already flagged this as "the first
   candidate in this five-cycle sub-thread to engage a seat's own
   charter physics directly").

3. **G40/`PAD` decorrelation** (PLAN.md Iteration-51 queue item 2,
   ~31 FDTD calls). This remains the only queued item on the board that
   actually *relieves* — rather than merely diagnoses or prices — the
   `ABSORB`-or-`PAD` confound that has bound every T28 deliverable since
   Iteration 48, and it is orthogonal to both this cycle's own
   null-calibration finding and to item 2 above, so it can run in
   parallel without waiting on either. Given this cycle's own binding
   seventh-cycle rule (no further sign-flip/permutation-null attempt on
   this ramped-quadrature basis without a qualitatively different
   strategy), G40/PAD's amplitude-channel readout
   (`√(A_i²+A_q²)/a`, phase-invariant, fits no carrier phase at all) is
   *not* blocked by that rule — it is a genuinely different instrument
   class, worth stating explicitly in Iteration 52's own entry so a
   future cycle does not misread the seventh-cycle rule as blocking it.

I would NOT rank a further widened-window or re-null-calibrated attempt
on the differential/two-tone basis itself — that is precisely what this
cycle's own pre-committed, binding decision rule forecloses without a
qualitatively different calibration strategy, and nothing in my
independent re-verification gives any reason to relitigate that rule.
