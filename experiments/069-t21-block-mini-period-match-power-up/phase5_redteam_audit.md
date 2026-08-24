# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 46 · exp-069 (Block MINI's period-match test, powered up)

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7). Receives the full
cycle record — Phase 1–4, `results.json`, code, and all six blind Phase-5
reviews — and goes last. Standard: not textbook-physics compliance —
internal consistency, falsifiability, expressibility as simulation
parameters, non-violation of a target constraint, and — the specific
charge of this audit — whether the program-integrity finding that opened
this cycle (Iteration 45's CHECKPOINT) was actually closed, not merely
relabeled one level down.*

## 0. What this audit independently re-verified, not merely read

Every load-bearing numeric claim below was recomputed directly from
`results.json`'s raw per-block rows and the committed code
(`run.py::_fixed_period_fit`/`_free_period_search`/`score()`,
`design_geometry.py`), not taken from any seat's prose:

- P-069-1/2/3/4/5/6 all reproduce bit-exact against `results.json`'s
  `scored` block (matches all six seats' own independent reproductions).
- **PHOTONICS' λ-scaled-aperture claim, independently recomputed from
  scratch**: back-solving `A_eff = cpl/(radians(P*)·cos39°)` from the
  600nm free-fit (`P*=2.8421°`) gives `A_eff≈518.81` cells; fitting the
  750nm `block_leg750` delta series (16 points) against the λ-scaled
  period `T=CPL[750]/A_eff=25/518.81` gives **R²=0.7666**, against
  **R²=0.3480** for T21's own model (`A=752`) on the identical 750nm data
  — both numbers match PHOTONICS' review exactly. **Real, confirmed.**
- **EM's same-frequency-superposition argument**, checked directly against
  `design_geometry.py`: `A_HALF_APERTURE=752` is asserted bit-identical
  for `C40`/`C80` at import time (line 114, a live `assert`, not a
  comment), independently re-confirmed by P-069-G1's bit-exact
  reproduction of both configs' pre-existing `C_empty` values. The
  addition formula for cosines at a shared frequency is exact; a
  best-fit period 45% away from T21's own `P(39°)` therefore cannot be
  explained as "T21's fringe, differently weighted between configs" —
  **the logic is sound and independently verified**, not merely
  plausible-sounding.
- **MATERIALS' stale-registry claim**, checked directly against
  `lab/caveat_lint_config.json` (pre-fix): the
  `exp065-steps1400-unsettled-plane-channel` entry's description read, in
  its own committed text, "...Block MINI's period-match test (P-VIS42-10)
  remains untouched by exp-068... and STILL UNDECIDED" — **true, this was
  stale** as of this cycle's own close (exp-069 formally retired
  `P-VIS42-10`). Independently ran `lab/caveat_lint.py`: 0 required-site
  failures, confirming MATERIALS' diagnosis that this is a false-negative
  (a coincidental `"0.827"` substring match suppresses the tool's WARN for
  exp-069's own files, which were never in `required_sites` to begin
  with) — a substring checker cannot catch a *stale description*, only a
  missing phrase. **Real, confirmed, and — see §5 — fixed as part of this
  audit's own same-shift docket.**
- **VISION's "escape hatch closed" claim**, checked directly in
  `run.py::score()` lines 420–444: a strict `if coherent / elif additive /
  else` with exactly three string outcomes
  (`COHERENT_FRINGE_FULLY_CORROBORATED`, `ADDITIVE_SYSTEMATIC_VINDICATED`,
  `FORMAL_RETIREMENT_NON_DECISIVE`). No `PARTIAL` string is reachable from
  any branch. Traced the actual boolean inputs
  (`p1.refute=True, p2.refute=False, p3.within_tolerance=False,
  p4.confirm=True, p5.confirm=True`) through the gate by hand: `coherent`
  is `False` (p2 fails), `additive` is `False` (p1 fails CONFIRM), so the
  `else` branch is the *only* reachable outcome given this cycle's real
  data. **Confirmed exactly as VISION reported, independently.**
- **QUANTUM's R3-margin-vs-precedent claim**, cross-checked against
  LOGBOOK's own record (read directly, not from QUANTUM's citation):
  exp-005's `mu_r_floor` jump shrank 17.7%→16.4% (7% relative) under cpl
  20→30; exp-015's eps_z trough shrank 17.69%→16.42% (7.2% relative) under
  the identical step — both LOGBOOK entries state these figures verbatim.
  This cycle's own P-069-5 ratios (1.97×, 2.50×, i.e. +97%/+150%) are
  correctly characterized as an order of magnitude outside that precedent
  band. **Confirmed.**

No fabrication, rounding game, or unverifiable claim found anywhere in
the six blind reviews. Every numbered attack below is built on this
independently-reproduced foundation, not on trusting the write-ups.

---

## 1. Reconciling the six blind Phase-5 verdicts — adjudicated, not counted

**Raw count: 5 PARTIAL (PHOTONICS, EM, QUANTUM, VISION, THERMODYNAMICS), 1
PROMISING (MATERIALS).** Per PANEL.md and this program's own standing
practice (e.g. Iteration 37, 43), a Red Team final audit does not average
or vote-count — it adjudicates the substance each seat actually found.

**MATERIALS' PROMISING is a *process* verdict, explicitly scoped as such —
"not 'promising' toward the phenomenon program's own constraints... but
promising as *process*."** This is not in tension with the other five
seats' PARTIAL; it is answering a narrower question well. MATERIALS'
own findings (the stale registry entry, the `fdtd_budget()` small-batch
defect) are real defects, independently confirmed above, that MATERIALS
itself flagged as needing a same-shift fix — a PROMISING-on-process
verdict that simultaneously files two concrete bug reports is not an
outlier data point to be argued away; it is the sharpest example this
cycle of the review process actually working, and its substance is folded
into this audit's own docket (§5) rather than discounted.

**The other five seats' PARTIAL is the correct read of the cycle as a
whole**, for a consistent reason each independently converges on: the
LOCKED, four-cycle-deferred process debt (does `run.py` actually retire
Block MINI cleanly, with no PARTIAL-and-defer escape hatch) is genuinely,
verifiably closed — PHOTONICS, EM, QUANTUM, and VISION all independently
re-derived the Combined-Verdict code and found it watertight — but the
*substantive optics question* this instrument exists to serve (is T21's
mechanism real, and is the boundary's behavior now better understood) is
**more open after this cycle, not less**: a new, unexplained, only
partially resolution-tested anomaly (T28) has replaced the old one, with
no mechanism yet identified. This is the correct verdict shape, matching
this program's own established pattern for a rigorous instrument result
that closes a citation-discipline debt while opening a better-
characterized question (T24's own opening at Iteration 23, T27's own
opening at Iteration 42 — EM's own citation, independently checked
against LOGBOOK and found accurate).

**Adjudication: PARTIAL is this cycle's correct verdict.** MATERIALS'
PROMISING is not overridden as wrong — it is a true statement about a
narrower question (process) folded into a synthesis that must also answer
the broader one (substance), where PARTIAL is what five independently-
reasoning seats, on five different lines of argument, converge on without
prompting each other (all Phase-5 reviews are blind).

---

## 2. The six questions this audit was charged to weigh, decisively

### 2.1 PHOTONICS' λ-scaled-aperture finding — real, and materially
under-reported

**Verified real (§0).** This is the single most significant substantive
finding of this cycle's Phase 5, and it was not run by the design, not
disclosed by `phase4_results.md` (which called the 750nm leg only
"suggestive of a shared mechanism," a materially weaker claim than R²=0.767
supports), and caught by only one of six blind seats. It does not change
this cycle's own Combined Verdict (P-069-6 was correctly scoped as
disclosed-only, non-gating, and the design's own pre-registered test of
T21's *own* period at 750nm correctly shows a weak fit) — but it
substantially reframes what the *retirement* actually leaves behind: not
an unexplained residual with no supporting cross-wavelength evidence, but
one with a specific, quantitatively strong (if post-hoc) candidate
signature of a genuine, single-mechanism, λ-scaling coherent effect. This
audit adopts PHOTONICS' finding as correct and material, and requires it
disclosed in the primary record (§5, mandatory fix — applied this shift).

**One caveat this audit adds, independently, that PHOTONICS' own review
does not fully foreground**: R²=0.767 is a *post-hoc* fit — the λ-scaled
period was derived from the same 600nm dataset it is partly validated
against (only the 16-point 750nm leg is a genuinely held-out test), and
the R4/house-discipline risk is real if a future cycle cites this number
as though it were pre-registered. PHOTONICS' own §2 discloses this
("not proof... a period derived from the same dataset being tested
against a second, independent (but power-limited) dataset") — correctly
hedged in the review itself, but the language must carry that hedge
forward into any primary-record citation, not just into the Phase-5
review that will eventually be superseded by a newer cycle's record.

### 2.2 QUANTUM's R3-margin critique of "not... Yee-grid discretization
structure" — the overclaim is real; this is not itself a Checkpoint-4
finding

**Verified real (§0): a genuine overclaim.** `phase4_results.md`'s
declarative "not a resolution artifact... a real physical feature, not
Yee-grid discretization structure" language is stronger than what a
2-of-31-angles, near-zero-crossing, order-of-magnitude-wider-than-
precedent R3 pass actually establishes. This audit independently
confirms QUANTUM's (and, convergently, PHOTONICS' and EM's) reasoning:
the correct, defensible claim is "rules out sign-flip/order-of-magnitude
collapse; does not establish resolution convergence of the fringe's
location/amplitude, nor separate T21's coherent mechanism from
Yee-grid discretization structure at the identical characteristic scale."

**Is this itself a Checkpoint-4-adjacent overclaim, or a defensible,
disclosed-scope finding?** **The latter — a defensible, disclosed-scope
finding, not a Checkpoint-4 firing, for four reasons, each independently
sufficient:**

1. **It does not change any scored verdict.** P-069-5 is correctly
   computed as CONFIRM by its own pre-registered band (`[0.3,3.0]`,
   fixed before the run); the overclaim lives entirely in the
   *prose characterizing* an already-correct computation, not in the
   computation, the gate, or the Combined Verdict (which is
   `FORMAL_RETIREMENT_NON_DECISIVE` regardless of how P-069-5's language
   is worded — P-069-2 alone already forces that branch).
2. **It was caught by the cycle's own process, at Phase 5, by three
   independent blind seats (QUANTUM, PHOTONICS, EM) — not by a later
   cycle, and not only by this final audit.** This is the textbook shape
   of Phase 5 working as designed, not failing. Compare Iteration 45's
   own firing, whose sharper aggravating fact was that the *mid-cycle
   Red Team Phase-2 audit itself* silently dropped a substantive fix with
   no argued reason — this cycle's mid-cycle audit (`phase2_redteam_
   audit.md`) did the opposite: ten items, all adopted, none dropped,
   independently re-verified by this final audit to have landed exactly
   as specified (§0's VISION cross-check).
3. **No hardened, self-catch-grace-spent forward tripwire attaches to
   this specific claim.** This program's recent firings (Iterations 37,
   39×2, 40) all involved either an explicit pre-committed "found again
   auto-fires" tripwire being triggered, or a defect surviving undetected
   through all five phases until a later cycle. Neither applies here.
4. **It is fixable, cheap, and non-load-bearing** — exactly the profile
   of this program's own non-firing precedents (Iterations 19, 23, 38,
   42, 43: found-and-fixable-before-close, no committed number wrong).

**Applied as a mandatory fix, same-shift (§5), not escalated as a
Checkpoint finding.** The correction is now live in `phase4_results.md`
(both the P-069-5 table row and the "What this DOES establish" §3 bullet
carry the corrected, hedged language, with the historical R3 precedent
numbers cited explicitly).

### 2.3 MATERIALS' `fdtd_budget()`/stale-registry findings — the registry
gap is real and is fixed this shift; it does NOT fire Checkpoint 4

**Both independently verified real (§0).** Taking them in order:

**(a) `fdtd_budget()`'s small-batch defect.** Confirmed by re-deriving
MATERIALS' own per-block table from `results.json`'s committed
`elapsed_s` fields: DENSE (62 calls) 2.54× faster than predicted, LEG750
(32 calls) 2.46× faster, R3 (4 calls = `n_workers`) 1.45× faster,
SETTLE-C80 (2 calls) *slower* than predicted (0.94×) — a monotonic
call-count dependence a uniform "lower contention" story cannot produce,
exactly as MATERIALS argues. This is a real, previously-uncaught process
gap (nobody — not Phase 1, not the Red Team Phase-2 audit, not
`phase4_results.md` — checked the block-level breakdown against the
aggregate "2.2× faster" explanation). It does not touch any physics
number, any gate, or the hard-stop discipline (14.76 min actual vs. a
100-min stop, nowhere close). **Ranked a real but low-urgency mandatory
fix (§5, item 5) — not applied same-shift (it is a documentation/formula
caveat in `design_geometry.py`, not a live citation risk), queued for
Iteration 47's docket alongside THERMODYNAMICS' independently-derived
cross-cycle pattern** (exp-065 1.28×, exp-066 2.70×, exp-069 2.20× —
this audit confirms THERMODYNAMICS' three-point table is internally
consistent with MATERIALS' single-cycle block-level finding: both point
to the same underlying defect, at two different granularities, and should
be fixed together, not as two separate items).

**(b) The stale `caveat_lint_config.json` entry.** Confirmed exactly as
MATERIALS describes (§0). **Given this program's history of firing
Checkpoint criterion 4 on this exact species of gap at Iterations 36–40,
does this fire?**

**No — this is a non-firing precedent, matching Iterations 19/23/38/42/43,
not the 37/39/40 firing pattern, for a reason this audit states
explicitly rather than by analogy alone:**

The Iterations-37/39/40 firings share one structural feature this gap
lacks: in each of those cases, the gap was either (i) a violation of an
explicit, pre-committed, Director-accepted forward tripwire that stated
"found again, this fires with no further deliberation" (the T18 lineage,
Iteration 39), or (ii) a defect that survived the *entire* five-phase
process of its *own* cycle undetected, discovered only by a later cycle
or Red Team's own final pass acting as the last line of defense
(Iteration 37's `run_all.py` docstring, three consecutive cycles of the
identical defect class recurring in the *same* document). **This gap has
neither property.** The `exp065-steps1400-unsettled-plane-channel` entry
has never received a hardened, self-catch-grace-spent tripwire the way
the T18 lineage did (compare the explicit non-firing ruling for the
sibling `exp061-thermo-length-scale-staleness` entry at Iteration 39,
LOGBOOK: "this entry has never received a hardened... tripwire the way
`exp061-t18-evidentiary-tier-propagation` has" — the identical logic
applies here). And it was caught cleanly by MATERIALS' own blind Phase-5
review, within this cycle's own Phase 5, before close — the process
working exactly as intended, not a defect that had to wait for a later
cycle or this final audit to surface.

**Ruled: does not fire Checkpoint criterion 4. Fixed same-shift as part
of this audit's own mandatory-fix docket (§5, item 1) — already applied
and independently re-verified live** (see §5's verification block): the
entry's description now records the retirement and points to T28; its
`required_sites`/`trigger_terms`/`candidate_globs` are widened to cover
exp-069's own `NOTES.md`/`phase4_results.md` and the new T28/`P-069-`
vocabulary; `lab/caveat_lint.py` reruns clean, 0 required-site failures,
after the fix.

### 2.4 EM's same-frequency-superposition argument — the logic is sound,
independently re-verified

**Confirmed sound (§0).** `A=752` is a live-asserted, bit-identical
invariant across `C40`/`C80` at import time — not a claim taken on faith.
The addition formula for two sinusoids at a shared angular frequency
producing a third sinusoid at that *same* frequency, regardless of
relative amplitude or phase, is an exact trigonometric identity, not an
approximation EM is leaning on loosely. A measured best-fit period 45%
away from T21's own `P(39°)`, at a solid `R²=0.63` (independently
confirmed by QUANTUM's own null-distribution test in §2.6 below to be
far outside what 20,000 draws of pure noise could produce, `p<5×10⁻⁵`),
is therefore genuine positive evidence against "T21's fringe,
differently weighted" and toward a second, physically distinct
oscillatory contributor — and EM correctly narrows the search to the one
thing that actually differs between the two configs (`ABSORB` depth,
40 vs. 80 cells, with `pad` translating everything else congruently).
This is a first-principles argument, not a curve-fitting coincidence, and
this audit finds no flaw in it. EM's own proposed falsification test
(C60/C70, already-built congruent configs, testing whether the period
tracks `ABSORB` depth) is correctly identified as the cheapest, most
direct next step and is folded into §6's ranked queue.

### 2.5 VISION's "PARTIAL escape hatch" confirmation — spot-checked and
confirmed closed

**Confirmed exactly (§0).** `run.py::score()`'s Combined Verdict is a
strict three-branch `if/elif/else` with no reachable `PARTIAL` string.
Independently traced by this audit, not merely re-read from VISION's
table. This is the single most important process finding of the cycle —
the specific failure shape that fired Iteration 45's own CHECKPOINT
(a conjunctive safeguard that existed on paper but didn't bind the
headline claim) is demonstrably, mechanically absent here.

### 2.6 The LOCKED mandate and the "one level removed" risk

**Does the cycle satisfy PLAN.md's LOCKED mandate text ("no further
relabeling, no further citation-tripwire-only treatment")?** **Yes, on
the letter — verified independently, not merely asserted**: 31 points
(mandate asked ≥2–3 periods at ~0.2°; delivered 3.06 periods, exactly
0.2°), settled STEPS=2800 (delivered, plus a first-ever C80 3-point
convergence closure beyond the mandate's own ask), desk-first (delivered
and actually run first this time — QUANTUM's own independent check
confirms the desk-check file predates the Phase-1 proposal's own text
referencing it). The test was built to the mandate's own spec and its
own pre-committed, code-executed rule fired the retirement branch
honestly on a genuinely non-decisive result, rather than being argued
into a fifth deferral.

**Does opening T28 risk becoming exactly that pattern one level removed?**
**Not yet a violation — VISION's own read is correct and this audit
adopts it — but the risk is real enough to warrant a pre-committed
tripwire now, before it needs one.** `phase4_results.md` correctly
declines Checkpoint-criterion-2 candidacy for T28, correctly scopes it
as "ordinary backlog, not locked," and offers disclosed, unproven
candidate mechanisms rather than an inflated claim. This is the right
weight. But this program's own five-thread lineage (T20→T21→T24→T27→T28,
Iterations 18 through 46) shows a structural tendency for exactly this
kind of "properly closed, immediately spins off a new open thread"
pattern to recur, and two of those threads (T21, T24) took upward of
twenty iterations each to reach a properly-powered test. **This audit
sets a forward tripwire, adopted below (§5, item 4): if T28 has not
received even a cheap, desk-only first move by the close of Iteration
48 (two cycles from now), that is itself a Checkpoint-4-adjacent finding
— matching this program's own established phrasing convention (cf.
Iteration 43's "a third occurrence would be worth flagging" language
that correctly anticipated and pre-committed to Iteration 45's own
firing).**

---

## 3. Overall verdict for this cycle

**PARTIAL.** Red Team's own synthesis, not a vote average, adopting the
five-of-six-seat convergent reasoning (§1) and independently confirming
its substance:

- **Real, load-bearing progress**: a four-cycle-deferred, Checkpoint-4-
  flagged process debt is genuinely closed — the specific mechanism that
  nearly let a citation-tripwire-only treatment slide one cycle ago
  (a conjunctive safeguard on paper, not in code) is demonstrably absent
  from this cycle's own design, independently verified by this audit at
  the code level, not the prose level.
- **The substantive optics question ends more open, not less**: T28 is
  real, resolution-robust-at-two-points, settled, and unexplained by
  T21's own model — a genuine new finding, not a null result, but a
  finding whose mechanism this cycle did not identify and whose
  resolution-robustness claim (in its published language) overstated
  what a near-null, 2-of-31-angle test actually shows.
- **Six real gaps found this Phase 5** (PHOTONICS' unreported λ-scaling
  fit; the R3-language overclaim, three-seat convergent; MATERIALS' two
  process defects; VISION's own residual-risk naming of T28) — none
  load-bearing to any scored verdict, all fixable same-shift or cheaply
  queued, which is the correct shape for PARTIAL rather than either
  extreme: not RULED OUT (nothing here forecloses a mechanism class or
  proves joint unsatisfiability — this cycle is explicitly T1-N/A,
  instrument-fidelity work), not PROMISING (the phenomenon program's own
  constraint-3 ledger gained zero ground this cycle, by design, and the
  new finding raises more questions than it answers).

---

## 4. Checkpoint determination

**No Checkpoint criterion fires this cycle.** Checked against all five,
explicitly:

1. *A configuration passes ALL constraint metrics.* N/A — no
   constraint-3 configuration was run or scored this cycle (T1 route
   explicitly N/A throughout, correctly disclaimed by every phase).
2. *A proven boundary — a constraint subset shown jointly unsatisfiable,
   gates clean.* N/A — `phase4_results.md` explicitly and correctly
   declines Checkpoint-criterion-2 candidacy for T28 ("a real, unresolved
   mechanism question, not yet a proven mechanism-class boundary");
   this audit independently confirms that framing is correct — no
   mechanism class has been bounded.
3. *A synthesis requires engine physics beyond the validated bench
   classes.* N/A — zero `lab/` diff, confirmed by `assert_lab_clean()`
   passing before every FDTD call and independently by this audit's own
   `git diff --stat -- lab/` check (clean).
4. *Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped — especially #3).* **Considered in depth,
   twice (§2.2, §2.3(b)) — does not fire.** The overclaimed R3 language
   and the stale registry entry are both real defects of exactly the
   *species* this program has fired criterion 4 on before, but neither
   carries the aggravating fact that distinguished those firings (a
   violated pre-committed tripwire, or a defect surviving an entire
   cycle's own five-phase process undetected). Both were caught within
   this cycle's own Phase 5, by its own blind review process, before
   close — the mechanism designed to catch exactly this working as
   intended, not failing. No constraint was dropped (none was engaged
   this cycle); no claim in the *scored, gated* record is unfalsifiable
   (only descriptive prose in `phase4_results.md`'s discussion sections
   overstated its own evidence, now corrected).
5. *Two consecutive iterations with no logbook-advancing result.* N/A —
   this cycle produced a genuine, verified new empirical fact (T28) and
   closed a standing process debt; Iteration 45 also advanced the record
   (Block ARTICLE's re-certification). No kill-criterion pattern.

**No pause/notification question arises — there is nothing to notify on.**
This is distinct from, and should not be conflated with, this program's
unbroken "notification, not pause" precedent for cycles where a criterion
*does* fire (Iterations 17, 36–40, 44, 45): this audit is not invoking
that precedent because no criterion fired, not because it is choosing
notification over pause. The mandatory-fix docket below is applied and
verified same-shift per this program's own standard practice for
Phase-5-caught, non-firing gaps (Iterations 19/23/38/42/43's pattern).

---

## 5. Mandatory-fix docket — itemized, numbered

**Items 1–2 already applied and independently re-verified live, this
shift, as part of this audit.** Items 3–5 are documentation-only, queued
for Iteration 47 (not blocking this cycle's close — none is load-bearing
to a scored verdict, gate, or the hard-stop discipline).

1. **[APPLIED] Fix `lab/caveat_lint_config.json`'s
   `exp065-steps1400-unsettled-plane-channel` entry.** Description
   updated to record Block MINI's formal retirement (`FORMAL_RETIREMENT_
   NON_DECISIVE`, exp-069/Iteration 46) and point forward to the new live
   thread T28, including the specific propagation risk (citing T28 as
   "confirmed real physics" without the R3-scope and mechanism-unidentified
   caveats). `required_sites` widened to add
   `experiments/069-t21-block-mini-period-match-power-up/{NOTES.md,
   phase4_results.md}`; `trigger_terms` widened to add `T28`, `Block
   MINI`, `P-069-`; `candidate_globs` widened to add
   `experiments/069-.../*.md`. **Verified**: `python3 -c "import json;
   json.load(open('lab/caveat_lint_config.json'))"` succeeds (valid
   JSON); `python3 lab/caveat_lint.py` reruns clean, 0 required-site
   failures, both new required sites pass (both files carry the `0.827`
   phrase-pattern match already, confirmed not a coincidental suppression
   this time since the description itself is now current).

2. **[APPLIED] Correct the overclaimed R3/resolution language in
   `experiments/069-.../phase4_results.md`.** Both the P-069-5 table row
   and the "What this DOES establish" §3 bullet now carry the corrected
   claim (rules out sign-flip/order-of-magnitude collapse at 2 of 31
   angles near a zero-crossing; does not establish resolution convergence
   of the fringe's location/amplitude, nor separate T21's mechanism from
   Yee-grid discretization structure at the same scale), with the
   historical R3 precedent figures (exp-005 7%, exp-015 7.2%, vs. this
   cycle's 97–150%) cited explicitly, and a pointer to the queued
   peak-cell recheck (item 3 below). The P-069-6 row also now discloses
   PHOTONICS' λ-scaled-aperture finding (R²=0.767 vs. R²=0.348) and the
   LEG750 free-search's own degenerate boundary-hit, both independently
   re-verified by this audit (§0/§2.1), with the R4-adjacent post-hoc-fit
   caveat carried forward explicitly. **Original committed numbers left
   unchanged** (P-069-5's own `confirm=True`/`ratio` values, P-069-6's own
   `r_squared_fixed=0.348`) — per this program's own erratum convention
   (flag and append, do not silently rewrite scored data); only the prose
   characterizing them is corrected.

3. **[Iteration 47, cheap, near-zero-cost — PHOTONICS' own §5 pick,
   independently endorsed]** Re-run the R3 (cpl 20→30) check at one or
   two peak cells of the DENSE sweep (θ≈37.2° or θ≈41.4°, `|delta|≈
   0.0019–0.0021`, an order of magnitude above the near-null cells
   already tested) — 2 additional FDTD calls, same harness, zero new
   `lab/` diff. This is the direct fix for item 2's own residual gap: it
   would either tighten P-069-5's CONFIRM into a genuinely strong
   resolution-convergence claim (ratio near 1.0 at a peak) or reveal a
   real phase-shift-driven artifact component, either of which is
   decisive and cheap.

4. **[Iteration 47/48, forward tripwire — this audit's own, per §2.6]**
   T28 must receive at least one cheap, desk-only first move (any of the
   five independently-converging seat proposals in §6 below) by the
   close of Iteration 48. If it has not, that is a Checkpoint-4-adjacent
   finding at whichever cycle notices — matching this program's own
   established phrasing and lock-trigger precedent (T23/Block MINI
   itself, `Q_ext(x)`/exp-059, `R_contact`/exp-067). This is *not* a lock
   on T28 itself (VISION's own read — correctly not locked this cycle,
   §2.6 — stands); it is a tripwire on the *scheduling gap*, the specific
   failure mode this program has now seen recur across five threads.

5. **[Iteration 47, cheap, documentation-only]** `design_geometry.py::
   fdtd_budget()`'s wall-clock formula (`total_cpu/(n_workers×efficiency)`)
   should carry a one-line docstring caveat: valid only for batches with
   `n_calls >> n_workers`; small legs (`n_calls ≤ n_workers`, e.g. this
   cycle's 2-call SETTLE-C80 block) are better estimated as roughly
   single-call CPU time. Fold in THERMODYNAMICS' independently-derived
   cross-cycle pattern (1.28×/2.70×/2.20× overestimate at exp-065/066/069)
   as a second sentence noting this is a recurring property of the
   formula's own contention assumption, not one-off variance — so a
   future cycle operating close to its own hard stop treats the
   predicted wall-clock as a conservative upper bound, not a point
   estimate, before pre-emptively de-scoping a marginal leg.

6. **R_contact — carried forward unchanged, correctly disclosed this
   cycle (verified, §0 was not needed here — MATERIALS' own Phase-5
   review independently confirmed three consistent, machine-readable
   disclosure sites).** Still blocked purely on WebSearch/WebFetch
   tooling; not gated to any rotation slot; the only queued item across
   five cycles now that can move a real materials number
   (`REALIZABILITY_MEMO.md` Entry 3, TD-5's 7.8× margin, UNANSWERED).

---

## 6. Ranked queue for Iteration 47 — adjudicated across all six seats

All six seats independently proposed some form of "characterize T28's
mechanism, desk-first" as a top priority — a genuine, unprompted
cross-seat convergence (blind Phase-5 reviews), not an artifact of one
seat's framing propagating to the others. This audit does not
concatenate the six lists; it merges the desk-only legs into one batch
(they test different, non-competing hypotheses against the same already-
committed data) and sequences the FDTD-cost items behind it.

**Priority 1 — a single, zero-FDTD-cost desk-check batch on T28's
mechanism, before any new FDTD spend (mirrors this program's own R3
meta-rule and the exact desk-first discipline this cycle itself modeled
on Block MINI).** Bundle, in one pass, since all four use only data
already sitting in `results.json`:
  - **QUANTUM's per-config decomposition**: does the ~2.84° signature
    already appear in `C40` alone or `C80` alone (fit each config's own
    `C_empty(θ)` series independently to T21's model), or does it emerge
    only in the difference? Directly tests EM's own hypothesis (§2.4) that
    the effect is `ABSORB`-depth-specific to one config.
  - **EM's own beat-frequency reconstruction**: solve `1/P_beat =
    |1/P_a − 1/P_b|` for a second period `P_b` given `P_a=P(39°,600nm)`
    and the measured `P_beat≈2.84°`, and check the two candidate `P_b`
    values (≈6.33°, ≈1.16°) against every named geometric length scale in
    `design_geometry.py` (`TAPER`, `ABSORB` depths, `pad`).
  - **MATERIALS' taper-as-second-aperture check**: does `TAPER=40` cells
    (the raised-cosine taper region, ~5.3% of `A`) alone, treated as its
    own diffracting sub-aperture, predict a period near 2.84°?
  - **PHOTONICS' A_eff≈519-cell trace**: cross-reference the already-
    computed effective offset against every named constant and simple
    combination in the committed geometry (already attempted informally
    by both PHOTONICS and EM in Phase 5, both coming up empty — worth one
    more systematic pass, including the beat-derived `P_b` candidates
    above, before concluding it is a genuinely new, unnamed length scale).

  This is the correct #1: cheapest possible (zero new FDTD, zero new
  `lab/` diff), tests four non-competing specific hypotheses rather than
  one vague "investigate further," and either narrows or kills T28's
  mechanism question before any FDTD design is committed — exactly the
  discipline this cycle itself was built to enforce on Block MINI, now
  applied to Block MINI's own successor.

**Priority 2 — EM's C60/C70 falsification test, or PHOTONICS' properly-
powered T28 re-run, whichever Priority 1's own result sharpens toward.**
If Priority 1's decomposition shows the signature isolated to one config,
EM's own falsification test (a dense `C60−C40`/`C70−C40` sweep at the
same 0.2°/31-point protocol, already-built congruent configs, zero new
`lab/` diff) is the direct, decisive follow-up. If Priority 1 is
inconclusive, PHOTONICS' own proposal (properly power T28 at 750nm/450nm
using the NEW ~2.84°-family period, not T21's, ≥3 periods, 0.2° step,
settled STEPS=2800) becomes the fallback — but should be *narrowed* by
whatever Priority 1 finds, not run as a blind full redesign. Fold in
item 5's cheap peak-cell R3 recheck (§5) here at near-zero marginal cost.

**Priority 3 — R_contact's `measured_direct` literature search.**
Unchanged ranking from Iteration 46's own queue: still the only item
across five cycles now that can move a real materials number, still
blocked purely on tooling, orthogonal to items 1–2 (desk/literature work
competes for zero FDTD budget or rotation slot). Every seat that ranked
it named the same reason; this audit adopts that convergence without
modification.

**Priority 4 (rider-level, apply whenever convenient, not worth a
dedicated cycle)**: THERMODYNAMICS' desk-only WKB/adiabatic
boundary-reflectance model for the graded-loss `ABSORB` band (an
energy-partition estimate of how much incident flux a σ(y) damping ramp
of given thickness reflects vs. absorbs, as a function of θ and `ABSORB`
depth) — a legitimate, cheap, THERMODYNAMICS-adjacent companion to
Priority 1's own EM/MATERIALS/QUANTUM checks, not competing with them for
resources, foldable into the same desk-check batch if capacity allows.

---

## 7. Closing statement

This cycle did what it was built to do: it took a four-cycle-deferred,
Checkpoint-4-flagged instrument and gave it the statistical power the
program's own mandate specified, wired a pre-committed non-decisive-
outcome rule into code rather than prose, and let that rule fire honestly
on a genuinely ambiguous result rather than arguing it into a fifth
deferral. That is real, verified, load-bearing process progress, and
this audit independently confirms it at the code level, not merely on
the strength of six seats' agreement. It also produced a genuine new
physics finding (T28) that the write-up under-reported in one direction
(a real λ-scaling cross-check that materially strengthens the "genuine
coherent effect" reading, never run) and over-reported in another (a
resolution check whose actual power was considerably weaker than its own
declarative language claimed) — both corrected in this shift, neither
rising to a Checkpoint firing, both landing squarely in this program's
own established non-firing pattern for gaps caught by its own process
before close. The registry gap MATERIALS found is now closed. Block
MINI's period-match test is retired, honestly, for good. T28 is real,
unexplained, and now carries an explicit forward tripwire so it does not
quietly become the next four-cycle deferral this program has to
Checkpoint its way out of.
