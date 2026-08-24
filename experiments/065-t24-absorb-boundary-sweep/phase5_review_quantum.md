# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 42 · exp-065

*Seat charter: non-classical absorption, state-dependent or coherent
interactions. Expressibility contract: mechanisms enter the bench only as
effective classical parameters. Fresh context, reviewing exp-065's full
record blind to the other six Phase-5 seats.*

---

## 1. My own Phase-2 worry, against the Phase-4 data

At Phase 2 (`phase2_critique_quantum.md`) I attacked idealization 6's
"cancels the quadrature phase error to first order" premise as unfalsifiable
and argued the two already-existing T24 legs (`+0.0070` / `−0.0022`,
opposite sign) were at least as consistent with a **boundary-perturbed
re-phasing of T21's own coherent edge-diffraction fringe** as with a clean
additive boundary-loss systematic. Red Team adopted the fix (attack 5); the
Director built it as **P-VIS42-10**, the dense 0.5°-step mini-sweep, with a
pre-registered REFUTE band requiring both (a) peak-to-trough/mean > 2× *and*
(b) a period matching `P(θ)=λ/(A·cosθ)` to within 20%.

**Two things need to be kept separate, and the record currently conflates
them.**

**First — as coded, P-VIS42-10 only tests half of its own pre-registered
claim.** `run.py:562-576` computes `ptp_over_mean` and calls it REFUTED at
`>2.0`; it never computes or checks the period-match-to-`P(θ)`-within-20%
clause that both `NOTES.md` and `phase3_synthesis.md` state as the second,
conjunctive REFUTE condition. `ptp_over_mean = 11.86` is real and large, but
the implemented gate cannot certify that this is a `P(θ)`-locked oscillation
as opposed to some other large, non-flat, non-periodic behavior. The verdict
string ("REFUTED (oscillating — coherent-fringe perturbation)") asserts a
mechanism the code does not test. This is a genuine gap in the falsifier I
myself proposed, and I did not catch it at Phase 2 because the band text was
never checked against the implementation until now.

**Second, and more consequential: even setting the coding gap aside, the
oscillation cannot currently be attributed to physics rather than to
settling, and the data available make this a live, unresolved ambiguity, not
a closed question either way.** The chain:

- P-VIS42-11 (my own seat's due-diligence check, via Red Team attack 7)
  REFUTED at **400× its own bar**: `STEPS=1400` vs `2800` moves
  `C_empty(C80, 40°, 600nm)` by **59.8%** relative. Diagnostics 1–2 in
  `phase4_results.md` generalize this: the *unpadded, 19-iteration-anchor*
  geometry (C40, the exact geometry the mini-sweep's own "clean" endpoints
  are drawn from) shows an even larger relative shift (**74.4%**), with
  `C_empty` moving from **−0.010965 → −0.002802** between 1400 and 2800
  steps at that one cell — an **absolute** shift of **0.0082**.
- The MINI block's own raw, unsettled (`STEPS=1400`) `C_empty_C40(θ)` values
  across the five 0.5°-spaced angles are **−0.00730, +0.00161, +0.01244,
  +0.00202, −0.01096** — swinging through two sign changes and a factor of
  ~7 in magnitude over a 2° span. This is not a mild wobble on top of a
  stable reading; it is a magnitude and non-monotonicity fully consistent
  with each angle catching a *different phase of an incompletely-decayed
  ringing transient*, independent of whether any real steady-state
  boundary-fringe perturbation exists underneath it.
- **The scale comparison is decisive for my own verdict on this point:** the
  independently-confirmed settling artifact at one single angle (0.0082
  absolute) is *comparable to or larger than* P-VIS42-10's own measured
  peak-to-trough (**0.00817**). A null hypothesis of "zero real
  θ-dependent coherent perturbation, 100% settling-transient sampling
  noise" is not excluded by anything in this record — it would require the
  settling artifact to vary by less than a factor of ~1 across a 2° span to
  fail to explain the observed oscillation, and nothing here measures how
  the settling artifact itself varies with θ at fixed `STEPS`.
- Worse for disentangling the two: **the physical clock governing both
  candidate mechanisms is the same variable.** T21's fringe period
  `P(θ)=λ/(A·cosθ)` and any settling-transient ring-down phase at fixed
  `STEPS` are both set by path-length differences that scale with `θ` through
  essentially the same geometric factors (`A·cosθ`, `D_SP·tanθ`). A
  settling-transient-driven θ-dependence would therefore be expected, on
  physical grounds, to show variation on a *similar order of period* to a
  genuine coherent-fringe perturbation — so even a correctly-implemented
  period-match check (which this cycle did not run) would not, by itself,
  cleanly discriminate the two hypotheses. Ruling this out needs the
  settling-corrected mini-sweep itself, not a sharper test of the unsettled
  one.

**My answer to the Director's question, stated plainly from this charter's
own standard:** No, P-VIS42-10's REFUTE does **not** confirm my Phase-2
worry. It is equally well explained, on the data given, by "differently
unsettled transients at closely-spaced angles" as by "genuine coherent-fringe
perturbation" — and the quantitative comparison above (settling artifact
magnitude ≈ observed peak-to-trough) makes the settling explanation at least
as plausible as the physics explanation, not a remote alternative. This
question was **never controlled for** in Block MINI, which ran at
`STEPS=1400` like every other cell in Blocks SWEEP/MINI — exactly the value
independently shown, by this same cycle's own P-VIS42-11/Diagnostics 1–2, to
be grossly unsettled on this channel at these angles. My own falsifier is
therefore uninformative as currently run, not falsified-and-standing.

## 2. Verdict

**PARTIAL.**

The cycle discharged real, disciplined work: both absolute-identity gates
passed cleanly (G-1 at float64 equality, G-2 at 0.000e+00 after the
Phase-3 causal-step correction voided and replaced the original gate); the
Red Team's Phase-2 docket (11 items, including my own attack 5) was applied
in full with no overrides; and the settling discovery (P-VIS42-11, followed
up rather than filed as a footnote) is a genuinely valuable, well-diagnosed,
program-wide finding that stands on its own regardless of what happens to
T24's headline. But the cycle's own advertised question — does T24's
boundary systematic transfer to the scored channel as absolute or relative —
is explicitly undecided by the cycle's own final accounting, and the
QUANTUM-specific sub-question I am charged with (coherent-fringe
perturbation vs. clean additive systematic) is *more* undecided than that,
because its own dedicated test (P-VIS42-10) was run entirely inside the
newly-discovered unsettled regime and never re-verified outside it. Nothing
here is RULED OUT — the coherent-perturbation hypothesis remains a live,
plausible reading of T24's original non-monotone legs — but nothing is
PROMISING either, since the one purpose-built test of it returned a result
that cannot yet be trusted.

## 3. Ranked next directions

1. **Re-run Block MINI (P-VIS42-10) at `STEPS=2800`, all five angles** —
   the single highest-priority, cheapest (5 calls) fix that directly closes
   my own seat's open question. If the oscillation survives at comparable
   amplitude under settled conditions, that is real evidence favoring
   coherent-fringe perturbation; if it collapses toward flat (as the
   headline SWEEP delta did, 5.4× shrinkage), the settling explanation wins
   and idealization 6's "cancels to first order" premise is *not* refuted
   after all. **Yes — the mini-sweep must be re-run at STEPS≥2800 before
   P-VIS42-10's REFUTE is trusted in either direction; the current REFUTE
   should not be cited as established until this runs.**
2. **Implement the period-match check that was pre-registered but never
   coded** (cross-correlate the settled `Δ(θ)` against `P(θ)`'s predicted
   phase, not just amplitude), applied to whichever of (1)'s two outcomes
   obtains — needed regardless of direction, since amplitude alone cannot
   distinguish the two hypotheses even after settling is controlled, given
   both share the same geometric clock (§1, last bullet).
3. **Re-verify exp-041's own MAIN-block ±38°/±40° rows at STEPS≥2800**
   (Phase-4's own #1 priority) — my seat has a direct stake in this since
   T21's fringe model, which the coherent-perturbation hypothesis leans on
   entirely, was fitted to exactly those rows.
4. **The 750nm/C80 four-point convergence trend** (Phase-4's #2) — lower
   priority for this seat specifically, but a precondition for trusting any
   future 750nm-inclusive re-run of P-VIS42-10 at other wavelengths.

## 4. Checkpoint opinion (my own, seat-specific)

**None of the five criteria fire, in my reading, but criterion 4 is a live
near-miss specific to my own thread, not a comfortable non-fire.** The
verdict string this cycle shipped in `results.json`
(`"REFUTED (oscillating -- coherent-fringe perturbation)"`) names a causal
mechanism the implemented gate does not test and the settling confound
actively undermines — but the ambiguity IS disclosed, prominently and
correctly, in `phase4_results.md`'s own text ("Genuinely open... the single
most important item for Iteration 43"). Nothing has yet been asserted into
LOGBOOK.md as settled physics. My own forward tripwire, to be set at this
Phase 5's close if adopted: **if a future cycle cites P-VIS42-10's REFUTE as
"confirmed coherent-fringe perturbation" without carrying the settling
caveat in the same sentence, that is a retroactive criterion-4 finding** —
the identical documentation-gap pattern this program's own Red Team has
caught repeatedly (Iterations 24, 32, 33, 35) applied here pre-emptively,
before it has a chance to recur an (n+1)-th time on my own seat's own
finding.

---

*Prepared by QUANTUM OPTICS, panel Iteration 42, Phase 5. Fresh context;
read `PANEL.md`, `LOGBOOK.md` lines 1–1671 and Iterations 23/35/41 in full,
and the complete exp-065 record (Phase 1 proposal, all five Phase-2
critiques including my own, the Phase-2 Red Team audit, Phase-3 synthesis,
NOTES.md, phase4_results.md, results.json, run.py) before writing this
review.*
