# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 60 · exp-083
## Adjudicating all six blind Phase-5 reviews of the full-power `PAIR_PAD`-with-article re-test — independently verifying EM's new AR(1)-parametric surrogate null (does NOT reproduce as claimed), PHOTONICS' empty-scene-provenance finding (independently confirmed at the source), MATERIALS' realizability caution, THERMODYNAMICS' energy-interception urgency ruling, and a cross-cutting attack on the six-way consensus around MATERIALS' R_OUT discriminator; Checkpoint criteria 1–5; reconciling Iteration 61's queue

**Seat: RED TEAM.** Fresh sub-agent, zero memory of any prior session. Read,
in order: `PANEL.md` in full, `AGENTS.md` in full, `LOGBOOK.md` (RULED OUT
R1–R9 in full, ESTABLISHED, LIVE THREADS in full — T28's complete Iteration
46–59 history including T28's own opening at Iteration 46, the CHECKPOINT
blocks at Iterations 52/54, and standing house rules R4/R5/R6/R8/R9 in
particular), `PLAN.md`'s Iteration-60 queue, `experiments/082-t28-pad-real-
article-check/phase5_redteam_audit.md` (the direct ancestor's Phase-5 final
audit, format model, not copied), then the complete `experiments/083-.../`
directory in the order specified: `phase1_proposal.md`, `NOTES.md`, `run.py`,
`results.json` (spot-checked), `run_output.txt`,
`null_permutation_control.json`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, then all six Phase-5
reviews (`phase5_review_{materials,vision,photonics,thermodynamics,em,
quantum}.md`). I alone see the complete record and all six blind Phase-5
reviews, and speak last.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document
or by anything it adjudicates.** Independently re-confirmed by my own fresh
grep of the complete `experiments/083-.../` directory for constraint-3/
witness/T1 language — every instance reads "N/A," matching all five blind
Phase-2 critics, Red Team's own Phase-2 audit, Phase 3, and all six Phase-5
seats.

---

## 0. What I independently verified

Per the task's own instruction and this program's own established practice
(exp-082's audit, §0): this cycle already carries the primary statistic
(`R²=0.858`, Branch B) independently reproduced at minimum five times
(committed run, QUANTUM's/EM's Phase-2 critiques, Red Team's Phase-2 audit,
and — for the two-tone construction specifically — a sixth-and-seventh time
across the six Phase-5 reviews). I did not re-re-derive that. I spent my own
effort on what is genuinely NEW or DISPUTED this cycle: (1) the deterministic
core, spot-checked once more as a floor; (2) the circular-shift result,
reproduced a fourth time from primitives; (3) EM's new AR(1)-parametric
surrogate null, rebuilt from scratch — this is the one figure in this
cycle's entire record that had been independently checked by **zero** other
seats before this audit; (4) PHOTONICS' new empty-scene-provenance claim,
verified at the source against `experiments/069-.../run.py` itself, not
merely against its own results file; (5) the git-provenance restoration,
independently re-confirmed a third time, from the raw history myself.

### 0.1 Deterministic core — reconfirmed

| Claim | Committed figure | My independent check | Match |
|---|---|---|---|
| `P*`, `R²` (delta_scene, Branch B) | 2.9474°, 0.8582 | `results.json::primary_period_discriminator`: bit-identical | exact |
| `em_pair` fit | P*=2.5865°, R²=0.4582 | bit-identical from `results.json` | exact |
| Null-permutation controls | `delta_scene`: p=0.0, null_max=0.6324; `em_pair`: p=0.00185, null_max=0.5599 | `null_permutation_control.json`: bit-identical | exact |
| `git diff --stat -- lab/` | clean | re-run at HEAD: empty | exact |
| Reproduction precondition | `max_dev=0.0` | `results.json::reproduction_precondition`: `0.0` at all 31 angles | exact |

Not re-derived further — six-plus prior independent computations already
stand (per the task's own instruction to concentrate effort on what is new).

### 0.2 The circular-shift reversal — reconfirmed a fourth time, bit-exact

Independent, from-scratch closed-form OLS (own design matrices for
`P_edge_A`/`P_continuity`, own `np.linalg.lstsq`, own residual-shift loop —
no code shared with any prior document):

```
single-tone R2 (P_edge_A fixed) = 0.8430958569830254   [reported 0.843096 -- exact]
two-tone R2 (both fixed)         = 0.9560323462892163   [reported 0.956032 -- exact]
F(2,26)                          = 33.392147114286225   [reported 33.392   -- exact]
lag-1 autocorr of single-tone residuals = 0.9508355827712788   [reported 0.9508 -- exact]
circular-shift null (residual rotation, all 31 shifts): median=39.2038  p=0.5806 (18/31)
   [Red Team Phase-2: p=0.5806; EM Phase-5: p=0.5806; QUANTUM Phase-5: p=0.5806 -- all exact]
```

**This is now the fourth independent computation of the circular-shift
reversal** (Red Team's Phase-2 audit, originating; EM's Phase-5 review;
QUANTUM's Phase-5 review; this audit) — all four agree to the literal
permutation count. I found no discrepancy here. **The reversal itself is
solid, robust, and not implementation-dependent.**

### 0.3 EM's new AR(1)-parametric surrogate null — does NOT independently reproduce; a genuine R4-family gap

EM's Phase-5 review (§1c) reports a wrap-free alternative to the discrete
circular-shift null: fit an AR(1) model to the single-tone residuals'
measured serial structure (`φ̂=0.9508`, independently confirmed above),
generate 50,000 synthetic AR(1) noise realizations at that `φ̂`, add each to
the reduced (single-tone) model's fitted values, and refit both models —
reporting `F_obs=33.392`, `null median=78.44, p95=255.4, p99=356.0,
max=1275.0`, **`p=0.7663`** — read in the write-up, and in the task's own
brief, as an even more decisive non-significant result than the
circular-shift's own `p=0.581`.

**I rebuilt this construction from scratch, independently — the first
independent check anyone has run on this specific figure** (no other
Phase-5 seat reproduced it: VISION's own review explicitly declined to
re-run this Monte Carlo, checking only the underlying autocorrelation
number; QUANTUM's own review proposes a *different*, not-yet-run AR(1)
design for Iteration 61 rather than reproducing EM's own already-run one;
MATERIALS/PHOTONICS/THERMODYNAMICS do not touch it at all). Using the
identical measured `φ̂=0.9508`, `σ²_resid` from the same residuals, and the
standard stationary-variance-matched AR(1) generator (innovation variance
`σ²_ε = σ²_resid·(1−φ̂²)`, initial state drawn from the process's own
stationary distribution, `N_TRIALS=50,000`, independent seed):

```
My reconstruction: null median=7.54  p95=46.6  p99=86.5  max=337.1  p=0.0947
```

**This does not match EM's own figures — not closely.** The null median is
off by a factor of ~10.4×, and `p=0.095` is a materially different,
*weaker* non-significant result than either EM's own claimed `p=0.766` or
even the circular-shift's own `p=0.581` — it sits within a factor of two of
the conventional `α=0.05` line, not comfortably clear of it.

**I did not stop at one implementation.** I tried five variants to rule out
an innocuous convention difference before concluding this is a genuine,
unreproduced gap: (i) unscaled innovation variance (`σ²_ε=σ²_resid`
directly, no `(1−φ̂²)` correction); (ii) a fixed, real-data-derived
denominator instead of a per-synthetic-sample one; (iii) a zero-start
(non-stationary-seeded) AR(1) recursion; (iv) the alternate variance-ratio
lag-1 estimator EM's own §0 table flags (`φ̂=0.927` vs `0.951`); (v) a
unit-root (`φ=1.0`) random walk, as a stress test for whether some
indexing/bounding slip could push the true process toward non-stationarity.
**None reproduces EM's figures — all five variants land in the SAME
`p≈0.08–0.10`, `median≈6–9` range as my baseline reconstruction.** This is
not a coincidence: for this exact construction (`y_synth = fitted1 + η`,
with `fitted1` lying exactly in the column space of both the reduced and
full design matrices), the F-statistic is **algebraically invariant to any
uniform rescaling of `η`** — a nested-model F-test's residual sums of
squares depend only on the projection of `η` itself, and both projections
scale identically with `η`'s overall magnitude, so the ratio cancels
exactly. This rules out a variance-calibration convention as the source of
a ~10× discrepancy; the difference must be structural, not merely a scaling
choice — and I could not, across five reasonable structural variants,
reconstruct EM's reported distribution.

**Ruling: EM's own qualitative point is sound and independently confirmed —
circular-shift is not the best-suited null for this non-periodic,
non-wrapping angular sweep, for the physically concrete reason EM gives
(§1b: neither reference period divides the 6°-window evenly, so the wrap
manufactures a synthetic discontinuity, visible directly in the real
observation sitting below the shift-null's own median). But EM's own
SPECIFIC number — `p=0.7663`, "even more decisive" — is not independently
verified, and this audit's own from-scratch reconstruction, built under
several reasonable structural variants of the identical stated method,
converges instead on `p≈0.09–0.10`: still not significant at conventional
`α`, but a materially WEAKER, not stronger, non-significant result than the
circular-shift's own `p=0.581`.** This is precisely the shape R4's own
standing rule exists for: a headline figure attributed to a specific
computation, without committed, invokable code, that a later independent
check cannot reproduce. EM's own review supplies a results table and a
methods description, not a committed script — exactly the gap R4's
Iteration-25 origin (and its two addenda) was adopted to close. **Do not
adopt EM's specific `p=0.7663`/`median=78.44` figures into the permanent
record. The qualitative direction (both nulls agree: not significant) is
unaffected and independently confirmed twice over (circular-shift, four
times; my own AR(1) reconstruction, once, pending a committed script).**

---

## 1. Adjudication of the six Phase-5 reviews

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| MATERIALS | PARTIAL | R_OUT=78 fixed, confirmed at the source (`design_geometry.py`); the "genuine ambiguity remains" argument independently re-derived and correct (§4, below) | **ADOPT IN FULL** — the single most careful self-critique of this cycle's own five-review packet: MATERIALS declines to auto-apply its OWN prior rule to a case its own rule was not built for. |
| VISION | PARTIAL | Git-provenance restoration independently re-confirmed a third time (§7, below); record-hygiene claims spot-checked and correct | **ADOPT IN FULL.** |
| PHOTONICS | PARTIAL | Far-field/Fresnel-regime figures reproduce exactly (`Δθ=9.452°`, `N_F=13.08`); the empty-scene-provenance claim independently verified at the SOURCE (§3, below), not merely restated | **ADOPT IN FULL — the empty-scene-provenance finding is this cycle's single most consequential new Phase-5 finding, adopted and extended.** |
| THERMODYNAMICS | PARTIAL | Fix-docket item 4 landing independently re-traced through all three documents, confirmed clean; the urgency reasoning (§5, below) independently re-derived and largely correct, one caution added | **ADOPT IN FULL, one refinement** (§5). |
| ELECTROMAGNETISM | PARTIAL | Circular-shift reproduction confirmed exact (§0.2); the AR(1)-parametric figure does NOT independently reproduce (§0.3) | **ADOPT the qualitative critique of circular-shift IN FULL (§2, below); DO NOT adopt the specific AR(1) p-value/null distribution as verified — see §0.3.** |
| QUANTUM | PARTIAL | Fit reproduction exact; the sketched (not-yet-run) AR(1)-matched calibration DESIGN independently assessed as sound and, unlike EM's own already-run figure, correctly proposed as Iteration-61 build work rather than an already-established result | **ADOPT IN FULL** — QUANTUM's own restraint (proposing a design rather than claiming a result) is the correct posture, and turns out to matter: it is EM's own already-run number, not QUANTUM's own unrun design, that this audit finds unreproduced. |

**All six blind reviews filed PARTIAL — genuine, unforced unanimity, not a
default.** Every review independently re-derived at least one load-bearing
number from primitives before filing; none merely restated Phase 3's own
prose. **No review's overall verdict is overridden.** One review's own
specific new figure (EM's AR(1) null) is found, independently, not to
reproduce — disclosed and adjudicated in full above (§0.3), not smoothed
over, matching this program's own precedent for how a genuine, non-fatal
Phase-5-layer correction gets folded in without touching the Combined
Verdict any of the six reviews reached.

---

## 2. Task item 1 — does EM's circular-shift critique, and the AR(1) surrogate specifically, change the Phase-2 ruling, and should AR(1) become the standing null-construction recommendation?

**(a) Does it change Phase-2's own ruling?** No — and my own §0.3 finding
sharpens rather than weakens this answer. Phase 2's ruling was never "the
circular-shift `p=0.581` is the unique correct answer"; it was "the naive
full-permutation Freedman–Lane construction is invalid for these
autocorrelated residuals, and the order-preserving companion reverses its
conclusion." EM's own critique (independently confirmed correct on the
physics, §0.3 above: no periodic boundary condition exists in θ, and the
window/period mismatch manufactures a real wrap artifact, directly visible
in the null distribution's own shape) does not challenge that reversal — it
proposes a BETTER-MOTIVATED companion that, *when EM's own code is
eventually committed and independently verified*, may report a different
numeric confidence in the same direction. My own from-scratch
reconstruction of the identical stated method, tested under five
structural variants, agrees with the reversal's DIRECTION (`p≈0.09–0.10`,
not significant) while landing further from EM's own claimed magnitude than
even the circular-shift result does. **Every independently-checkable
construction run on this data so far — Freedman–Lane on i.i.d.-simulated
noise (correctly calibrated, Red Team §0i), the discrete circular-shift
(four-times reproduced, `p=0.581`), and now this audit's own AR(1)
reconstruction (`p≈0.10`) — agrees the two-tone admixture claim does NOT
survive a properly order-respecting null. Phase 2's ruling stands, and is
independently reconfirmed by a structurally different method this cycle.**

**(b) Should AR(1)-parametric replace circular-shift as this program's own
standing recommendation (a possible R6-family addendum)?** **Not yet — this
audit declines to adopt a new house rule on the strength of an unreproduced
figure.** The underlying PHYSICS argument for preferring a wrap-free,
AR(1)-matched construction over a discrete circular-shift is sound,
independently confirmed by this audit, and should be logged as forward
methodological guidance (§8, below) — a wrap-around null is the wrong tool
whenever the sampled window is not an integer multiple of either tested
period, which is a general, checkable, falsifiable condition future T28
cycles can test for before choosing a null. But adopting a SPECIFIC
construction as this program's own standing recommendation requires the
construction to be **committed, reviewable code, independently reproduced
by at least one other seat** — the exact bar every other headline figure in
this cycle's own record has already cleared (§0.1–0.2, five-to-seven-fold
independent reproduction each). EM's own figure has cleared none of that
bar yet; this audit is the first independent check, and it does not
reproduce. **Ruling: log the wrap-free/AR(1)-matched PRINCIPLE as
Iteration-61 forward guidance for any future T28 nested-model null
construction (a discipline note, not a fresh numbered rule — matching this
same cycle's own disposition of the R5 pre-registration gap, Fix-docket
item 5), but do NOT adopt EM's own specific `p=0.7663` figure, and do NOT
retire circular-shift as this sub-thread's own working companion until a
committed, independently-reproduced AR(1) implementation exists.** QUANTUM's
own §2 design (not yet run, fully specified, pre-registered pass/fail
bands) is the correct vehicle for this — Iteration 61 should build QUANTUM's
own sketch, checking explicitly against this audit's own §0.3 finding
before either EM's or this audit's own number is treated as final.

---

## 3. Task item 2 — PHOTONICS' empty-scene-provenance finding: sharpens the board's priors, and should PLAN.md state it explicitly?

**Independently verified at the source, not merely restated — and it is
decisive as an Occam's-razor argument, though not as a proof.** I read
`experiments/069-t21-block-mini-period-match-power-up/run.py` directly, in
full, the source of `P_edge_A` (`scored.p3.p_star_deg`, the `C80−C40`
period this cycle's Branch B matches). Its own FDTD call functions
(`_one_run`, `_one_run_r3`) construct a bare `Sim`, add a line source, and
`sim.run(steps)` — **there is no `materials.*` call anywhere in the file: no
`pec_disk`, no `graded_black_shell`, no article of any kind, confirmed by a
direct grep returning zero hits.** `P_edge_A` was established on a
completely empty scene — PEC walls and vacuum padding only, nine-plus
mechanism-search cycles all confirming the same (LOGBOOK's own T28 record,
Iterations 47–58, testing domain-echo candidates exclusively). PHOTONICS'
own argument, independently confirmed at the primitive level here for the
first time (PHOTONICS' own review cited the result but did not itself grep
`run.py`): if this cycle's own article-loaded channel produced a BRAND NEW
physical channel (a real article-rim diffraction term), it would be a
striking coincidence for that new channel's period to land, at 3.7%
relative deviation, on a number a completely unrelated, article-free
experiment already produced from an unrelated geometric axis (`ABSORB`
depth, not article radius). That is not impossible — but "the article-loaded
channel inherited a pre-existing artifact" is the more economical
explanation of the SAME evidence, independently of the 3.3×
far-field-formula miss (Attack 1, Phase 2) and on top of it, not merely
alongside it.

**Sharpens the board's prior: yes, explicitly and by name.** This finding
does not settle the causal question (§4, below) — it is a prior-shifting
argument, not a proof, and MATERIALS' own caution (§4) about not letting a
sharpened prior masquerade as a settled answer is correct and adopted in
full. But a prior is exactly what a pre-registered discriminator needs
before it is run, and "period tracks `R_OUT/λ`" vs. "period stays pinned"
should not enter Iteration 61 as a 50/50 coin flip when one reading is
independently supported by two convergent, primitive-level findings (the
wrong-regime far-field miss, and now the empty-scene provenance) and the
other by none.

**Should PLAN.md's Iteration-61 entry state this explicitly, as a
pre-registered expectation? Yes.** This is exactly what pre-registration is
for: naming a directional prior in writing, before the data arrives, so the
test remains falsifiable rather than becoming a post-hoc narrative either
way. **Ruling: PLAN.md's Iteration-61 entry, and the R_OUT sweep's own
Phase-1 proposal, should state explicitly: "period stays pinned near
`2.84°`/`1.96°` regardless of `R_OUT`" is the Occam's-razor-favored prior
(citing both the 3.3× far-field-formula miss under the wrong regime, and
this audit's own source-level confirmation that `P_edge_A` was established
on an article-free scene) — with the test still run and scored honestly
against BOTH directional outcomes, exactly as a real pre-registration
requires. This is a genuine sharpening, not a foreclosure: a "tracks
`R_OUT/λ`" result would be MORE surprising, and correspondingly more
informative, under this stated prior than under a coin-flip framing — which
is the correct scientific reason to state a prior, not a reason to avoid
stating one.**

---

## 4. Task item 3 — does MATERIALS' "zero realizability content" rule automatically re-apply, and does Attack 1 (plus §3, above) license leaning toward one reading?

**MATERIALS' caution is correct: the rule does NOT automatically re-apply.
Attack 1, sharpened by this audit's own §3 finding, licenses leaning the
PRIOR toward the rule's own original reading — without re-closing the
question as settled.** These are two different claims, and the distinction
matters for how Iteration 61 is written up.

MATERIALS' Iteration-59 rule was built for a 7-point cycle where NO causal
story had been distinguished from any other — "zero realizability content"
was true by elimination, not by evidence for a specific reading. This
cycle's own primary finding (Branch B, decisively) does not restore that
same epistemic state: it retracts the CAUSAL label while leaving intact a
decisive, doubly-corroborated STATISTICAL finding that two live,
opposite-realizability readings could each explain equally well as of Phase
3's own close. MATERIALS is right that treating the rule as automatically
reinstated — "the causal claim was walked back, so my rule already covers
this" — would repeat, one level up, the exact overclaim Attack 1 exists to
correct: treating a corrected, narrowed statistical finding as though it
settled a question (realizability, not period-family) it was never built to
answer.

**What changes with this audit's own §3 finding:** the two readings are no
longer symmetric. Before this audit, the record's own honest position was
"two live possibilities, no basis to prefer either." After this audit's own
independent source-level confirmation (P_edge_A's own article-free
provenance) — on top of Attack 1's already-established formula-regime
miss — the record's honest position is "two live possibilities, one now
independently better-supported by two convergent lines of evidence than the
other." **Ruling: MATERIALS' rule does not cleanly re-apply as settled fact
(genuine ambiguity remains, formally, until the `R_OUT` sweep runs — I concur
with MATERIALS' own §2 in full), but this cycle's own record, taken
together with this audit's own new finding, licenses stating the rule's
ORIGINAL reading as the directionally-favored current best guess, not a
symmetric open question — matching PHOTONICS' own Phase-5 language exactly
("period-pinned is the charter-favored prior, not a 50/50 split") and this
audit's own §3 ruling above. Iteration 61's record should carry BOTH
statements precisely: the rule is not yet re-confirmed (MATERIALS' own
correct caution stands), AND the current evidence leans toward its original
reading being right (this audit's own addition) — not a contradiction, a
prior under active test.**

---

## 5. Task item 4 — the joint EM/THERMO energy-interception cross-check: does this need an explicit stated reason this cycle, or is it still within scheduling discretion?

**Within normal scheduling discretion this cycle — a reason WAS stated,
adequately, though the pattern is now two cycles old and should not
continue past Iteration 61 without either running the check or restating
the reason explicitly, matching this program's own established discipline
for exactly this shape.**

Counted precisely: the item was NAMED for the first time at Iteration 59's
own close (exp-082's Phase-5 audit, Tier 0 item 2) — that is not itself a
deferral, it is the item's origin. This cycle (Iteration 60) is the FIRST
cycle boundary at which the item could have been run and was not —
Idealization 6 of `phase1_proposal.md` states the reason explicitly
("interception/energy-budget accounting remains out of scope... a separate,
already-queued board item, not folded into this build"), and this cycle's
own THERMODYNAMICS Phase-2 critique independently supplies the substantive
sequencing argument (running the branch-discriminator cleanly first, then
the energy check with the mechanism narrowed, is more disciplined than
bolting new analytic machinery onto an already-dense 125-call build) — a
real, disclosed, non-arbitrary reason, not silence. **This does not match
the shape that has fired Checkpoint criterion 4 in this program's history
(R8's own precedent): those firings involved an UNVERIFIED argument
substituting for a named, affordable, un-run check reaching the permanent
record as though the gap were closed. Here, nobody claims the energy
question is closed — Idealization 6 explicitly defers it, and every
document that cites it (fix-docket item 4, Attack 4) correctly re-scopes,
never resolves, it.**

**But THERMODYNAMICS' own Phase-5 review is correct that the check's own
target got sharper and its physical premise got stronger this cycle** (§2a–c
of that review, independently plausible and not disputed here: Branch A's
own free pass from Iteration 53's lossless-vacuum proof no longer applies,
and a genuinely lossy absorber now co-locates with the dominant confound for
the first time). **Ruling: does not fire Checkpoint criterion 4 — the
distinguishing condition is met (a real, stated, non-arbitrary scheduling
reason, not an unverified closure claim). But this is now a two-cycle-old
named-but-deferred pattern (Iteration 59's naming; this cycle's own
deferral), the identical shape this program logs explicitly as a forward
tripwire rather than letting recur silently (matching the git-provenance
convention, Iteration 59's close). Log it as such: if Iteration 61 defers
this a THIRD consecutive cycle boundary without an equally explicit,
cycle-specific reason, that WOULD cross into the R8-family firing pattern
THERMODYNAMICS' own review names, and should not be weighed as a close call
a second time.**

---

## 6. Task item 5 — cross-cutting: what is the panel collectively missing in its six-of-six convergence on MATERIALS' R_OUT discriminator?

**A real, concrete gap, not a vague caution: as specified by every one of
the six reviews that names it, the R_OUT sweep tests for only ONE alternate
radius — enough to distinguish "pinned" from "moved," but not enough to
establish that a moved period actually TRACKS `R_OUT/λ`, which is the
causal claim the discriminator is supposed to settle.**

Checked directly: MATERIALS' own proposal (§2, Phase-5 review, and its own
Phase-2 critique) specifies "one alternate article radius (e.g. `R_OUT=50`
or `100`)." VISION, EM, and QUANTUM each restate the identical single-radius
design. PHOTONICS' own review comes closest to naming the gap (recommending
the sweep be scored against a QUANTITATIVE prediction from its own §2.1
Fresnel-derivation proposal, "rather than a bare qualitative direction") but
does not itself flag that a single data point cannot establish a scaling
LAW even with a quantitative target in hand. **None of the six reviews
states explicitly that a two-point comparison (`R_OUT=78` vs. one
alternate) is, by itself, a binary read (moved/didn't-move), not a trend
confirmation — and that if `P*` DOES move at the one tested alternate
radius, that alone cannot yet distinguish "genuine `1/R_OUT`-type rim
scaling" from "moved for some other, unrelated reason coincident with
changing `R_OUT`" (e.g., a subtle interaction with the object window's own
edge geometry that happens to correlate with disk size in this one
instance).** This is the identical shape R5's own family of house rules was
built to catch one level up — not a look-elsewhere problem this time, but an
UNDER-POWERED-TREND problem: a scaling claim needs at least three points to
be distinguishable from a coincidence, the same logic that makes a two-point
"line" trivially perfect and uninformative about its own functional form.

I independently checked feasibility, since a valid attack on consensus
should also confirm the fix is affordable, not merely note the gap: loaded
`design_geometry.py`'s own `CONFIGS["C40"]`/`["G40"]` directly — `nx=360`/
`440`, `obj_x=170`/`210`, `y_lo=40`, `y_hi=1544`/`1664`, `R_OUT=78`. A second
alternate radius (e.g., `R_OUT=100`, alongside `R_OUT=50`) fits cleanly
inside both domains with wide margin in both `x` and `y` — no domain resize,
no other geometry parameter needs to move, matching MATERIALS' own
"holding every other geometry parameter fixed" framing exactly. **The fix is
cheap: doubling the sweep from one alternate radius to two (`R_OUT∈{50,100}`,
alongside the existing 78 baseline, giving three points total) costs one
more 31-call block (~31 more FDTD calls, well inside this sub-thread's own
established per-cycle budgets) and converts a qualitative pinned/moved read
into an actual trend test — fit `P*(R_OUT)` against a genuine scaling
hypothesis (linear in `1/R_OUT`, or whatever functional form PHOTONICS' own
Fresnel-diffraction desk derivation predicts, if built first per §3 of that
review) rather than eyeballing a two-point line.**

**Ruling: adopt the near-unanimous ranking of MATERIALS' discriminator as
Iteration 61's own top empirical item (confirmed independently, §3–4,
above), but UPGRADE its own scope before it runs: pre-register at least
TWO alternate radii, not one, so the outcome can distinguish a genuine
scaling relationship from a single coincidental shift — and pre-register the
directional prior named in §3, above, before running either point.** This
is exactly Red Team's own charter duty (attack consensus too, not only
individual claims) — the near-unanimous ranking itself is correct and not
overridden; its SPECIFICATION, as filed by all six reviews that name it, is
under-powered for the causal claim it is meant to establish, and is
corrected here before it reaches Iteration 61's own board.

---

## 7. Checkpoint ruling — all five criteria, reasoned through explicitly

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 engagement anywhere in this cycle's record or in any of
the six Phase-5 reviews — independently reconfirmed by my own fresh grep.

**Criterion 2** (a proven mechanism-class boundary): **N/A, not merely
not-yet-ripe — reasoned through explicitly, matching Phase 2's and Phase
3's own rulings, and re-confirmed here against this audit's own new
findings specifically.** Every finding this audit adds (the AR(1)
non-reproduction, the empty-scene-provenance confirmation, the R_OUT-sweep
under-specification) is about artifact attribution, null-construction
validity, and statistical-design adequacy inside this lab's own FDTD
instrument — none touches, or could be read as touching, any of the four
phenomenon constraints or their named escape routes. Criterion 2 stays N/A
on that basis, for a reason specific to this audit's own content, not
inherited by pattern-match.

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
`git diff --stat -- lab/` independently re-run by me at HEAD: empty. This
audit's own verification scripts are session-local scratch, touching
nothing under `experiments/083-.../` or `lab/`.

**Criterion 4** (program-integrity drift): **Reasoned through explicitly for
three distinct matters — does not fire on any of them, one closed, two
flagged forward.**

*7a. The fix-docket adoption (Phase 2 → Phase 3).* Independently reconfirmed
by every one of the six Phase-5 seats (each grepped for residual
"confirmed"/"resolved" language and found none) and by my own direct
reading of the corrected `NOTES.md`/`phase1_proposal.md` at task start.
**Does not fire — condition satisfied cleanly, matching exp-082's own
identical non-firing precedent for its own comparable near-miss.**

*7b. The git-provenance restoration.* Independently reconfirmed a THIRD
time, by me, from the raw history (`git log`, `git show --stat 06cb96b`,
`git show 06cb96b:.../run.py` → path does not exist at that commit) —
matching Red Team's own Phase-2 audit (§0e) and VISION's own Phase-5 review
exactly, using a third independent method. **The two-cycle-old tripwire
(exp-081, exp-082) is correctly, triply-verified discharged — this is the
correction, not a third strike. Does not fire.**

*7c. EM's own unreproduced AR(1) figure (§0.3, this audit).* This is caught
and corrected WITHIN this Phase-5 review layer, before LOGBOOK's own
Iteration-60 entry is written — matching this program's own established
non-firing shape (a gap found and closed inside the review process itself,
before it reaches the permanent record unqualified), not its firing one.
**Does not fire — conditioned explicitly, matching this sub-thread's own
established conditional-non-firing precedent (exp-082, exp-083's own Phase
2): if a future cycle cites EM's own `p=0.7663`/`median=78.44` figures as
settled without either an independent reproduction or this audit's own
correction, THAT would be the firing shape one phase later — not the
flagging of it here.**

**Criterion 5** (two consecutive non-advancing iterations): **Not at
risk.** This cycle resolves the period-family power deficiency exp-082 left
open (the first properly-powered article-loaded period discriminator in
nine-plus T28 cycles), and this audit's own layer adds two genuinely new,
independently-verified findings with forward implications beyond this one
result: a non-reproduction finding that tightens this program's own R4
discipline for Phase-5-review-native figures specifically, and a
source-level confirmation (empty-scene provenance) that materially sharpens
the board's own priors for Iteration 61's top-ranked test.

---

## 8. Same-shift mandatory-fix docket

1. **[EM's AR(1) figure]** Any future citation of the AR(1)-parametric
   surrogate null for this construction must state: EM's own Phase-5 figure
   (`p=0.7663`, `null median=78.44`) is NOT independently reproduced by this
   audit (`p≈0.09–0.10`, `null median≈7.5–8.6`, across five structural
   variants) — do not cite EM's specific numbers as settled. The
   QUALITATIVE point (circular-shift is not the best-suited null for this
   non-wrapping angular sweep; a wrap-free AR(1)-matched construction is
   better-motivated) is sound and adopted as forward guidance (§2, item 8
   below), independent of the unreproduced number.
2. **[PHOTONICS' empty-scene provenance]** Any future citation of Branch B's
   causal status should carry this audit's own §3 finding: `P_edge_A` was
   established (exp-069) on a scene independently confirmed, at the source,
   to contain zero materials/article calls of any kind — an Occam's-razor
   argument FOR the "inherited pre-existing artifact" reading, on top of
   (not merely alongside) the already-established 3.3× far-field-formula
   miss under the wrong (Fresnel, not far-field) regime.
3. **[MATERIALS' rule, precisely scoped]** State both halves together,
   whenever cited: the Iteration-59 "zero realizability content" rule does
   NOT automatically re-apply to Branch B (genuine ambiguity remains,
   formally open until the `R_OUT` sweep runs); AND the current evidence
   (item 2, above) leans the board's own prior toward the rule's original
   reading being correct, not a symmetric open question.
4. **[Energy-interception item, logged as a two-cycle-old pattern]** The
   joint EM/THERMO Poynting-bound cross-check does not fire Checkpoint
   criterion 4 this cycle (a real, stated, non-arbitrary scheduling reason
   was given) but is now named-then-deferred at two consecutive cycle
   boundaries (Iteration 59's close; this cycle's own Idealization 6) — a
   third consecutive deferral at Iteration 61 without an equally explicit,
   cycle-specific reason would cross into this program's own R8-family
   firing pattern.
5. **[R_OUT sweep, upgraded]** Iteration 61's own proposal for MATERIALS'
   article-radius discriminator must pre-register AT LEAST TWO alternate
   radii (not one), so the outcome can distinguish a genuine `R_OUT/λ`
   scaling relationship from a single coincidental shift, and must
   pre-register the directional prior named in item 2/§3, above, before
   running.
6. **[R5 pre-registration note, carried forward]** Restated from Phase 2's
   own fix docket item 5, unchanged: future T28 cycles using
   `free_period_with_widening`/`_free_period_search` should pre-register
   their own null-permutation control in the SAME freeze commit as the
   falsifiable bands — now a four-cycle-running pattern (exp-069, exp-070,
   exp-077, exp-083), a standing discipline note, not a fresh rule.

None of the above touches `lab/`, any frozen prediction, or any RULED-OUT
item. No new FDTD is run by this audit.

---

## 9. Combined Verdict for the record: **PARTIAL**

For LOGBOOK.md's Iteration 60 entry, verbatim in substance:

This cycle executed PLAN.md's own Iteration-60 top-ranked item — the full
31-point/0.2° `PAIR_PAD`-with-article re-test at 600nm, resolving the
mechanism-identity power deficiency exp-082 (Iteration 59) demonstrated was
unresolvable at 7-point power. **PRIMARY: the pre-registered three-branch
period discriminator resolves decisively to BRANCH B — `delta_scene`'s
dominant periodicity matches T28's own long-standing, unexplained
`P_edge_A` family (`P*=2.9474°`, `R²=0.8582`, 3.7% from `P_edge_A=2.8421°`,
clearing the MAXIMUM of a 20,000-trial null-permutation control), not
QUANTUM's mechanism-continuity hypothesis (`P_continuity=4.611°`, missed by
36%) — doubly instrument-corroborated by EM's independent linear
field-difference companion (`P*=2.5865°`, `R²=0.4582`, own null-controlled
`p=0.00185`).** This is the first time in this nine-cycle-plus T28
sub-thread the article-loaded channel's own dominant periodicity has been
statistically pinned with confidence. **Phase 2/3 correction (Red Team's
Phase-2 Attack 1, adopted in full): "ARTICLE-EDGE DIFFRACTION" is a
period-family MATCH, not a demonstrated causal mechanism** —
`P_edge_A=2.8421°` is T28's own founding, still-unexplained periodicity;
PHOTONICS' own far-field two-rim estimate misses the recovered period by
3.3×, and this aperture's own Fresnel number (`N_F≈13`) means the far-field
formula applied is not even the correct regime — an untested regime, not a
clean refutation of a rim origin either way. **This audit adds a new,
source-level finding sharpening that correction further: `P_edge_A` was
established (exp-069) on a scene independently confirmed to contain zero
article/materials calls of any kind — an Occam's-razor argument, on top of
the formula-regime miss, favoring "inherited pre-existing artifact" as the
current best-supported reading, without yet proving it.** MATERIALS'
article-radius (`R_OUT`) discriminator remains the single test that can
convert Branch B from a period-family match into a demonstrated causal
claim — now this sub-thread's own single highest-priority item, **upgraded
by this audit to at least two alternate radii** (not the one every review
that names it currently specifies), so the result can establish an actual
scaling trend rather than a binary pinned/moved read.

**The two-tone `PAD`-continuity admixture question, raised independently by
QUANTUM's and EM's own Phase-2 critiques under a full-permutation
Freedman–Lane null (`p<0.001`), is REVERSED by Red Team's own Phase-2 audit
under the correct, order-preserving circular-shift companion (`p=0.581`
primary series, `p=0.097` EM field-difference companion) — the single-tone
residuals underlying the construction are highly autocorrelated
(lag-1≈0.93–0.95), invalidating the naive null's exchangeability
assumption. Independently reconfirmed bit-exact a fourth time by this audit.
EM's own Phase-5 review correctly argues circular-shift is not the
best-suited null for this non-periodic angular sweep (a real, physically
concrete critique: the window is not an integer multiple of either tested
period, manufacturing a wrap discontinuity) and proposes a wrap-free
AR(1)-parametric alternative claiming an even more decisive `p=0.7663`.
**This audit independently rebuilt that construction from scratch, across
five structural variants, and could NOT reproduce EM's own figures — this
audit's own reconstruction lands instead at `p≈0.09–0.10`, a materially
WEAKER, not stronger, non-significant result. EM's qualitative critique of
circular-shift is adopted as sound forward guidance for Iteration 61's own
null-calibration build; EM's specific numeric figure is NOT adopted into
the permanent record pending independent, committed-code verification —
the first instance in this cycle's own record of a headline Phase-5 figure
failing this program's own R4 reproduction standard.** The two-tone
admixture question remains open in both directions, now on THREE
independently-run, mutually-agreeing not-significant constructions (naive
full-permutation excepted, itself shown invalid) rather than two.

**Combined Verdict: PARTIAL** (all six blind Phase-5 seats, unanimous, and
this audit). **Checkpoint criteria 1/3 N/A. Criterion 2 N/A, not merely
not-yet-ripe. Criterion 4 does not fire on any of three matters
adjudicated** (the fix-docket adoption, confirmed landed; the git-provenance
restoration, independently triple-verified genuine, closing the two-cycle-
old tripwire cleanly; EM's own unreproduced AR(1) figure, caught and
corrected within this review layer before reaching LOGBOOK). **The joint
EM/THERMO energy-interception cross-check is logged as a two-cycle-old
named-but-deferred pattern (Iteration 59's close; this cycle's own
Idealization 6) — a real, stated scheduling reason exists this cycle, so
criterion 4 does not fire, but a third consecutive deferral without an
equally explicit reason would.** **Criterion 5 not at risk.**

---

## 10. Reconciled ranking for Iteration 61's queue

### Tier 0 — zero FDTD, desk-only

1. **[This audit's own AR(1) non-reproduction finding, §0.3/§8 item 1]**
   Log explicitly, wherever the two-tone admixture question is next cited:
   EM's own `p=0.7663`/`median=78.44` AR(1)-parametric figures do not
   independently reproduce (this audit: `p≈0.09–0.10`); the qualitative
   critique of circular-shift is retained, the specific number is not.
2. **[PHOTONICS' empty-scene-provenance finding, §3/§8 item 2]** Log as a
   standing, source-verified fact for this sub-thread: `P_edge_A` was
   established on an article-free scene (`experiments/069-.../run.py`
   contains zero materials calls, independently confirmed) — an
   Occam's-razor argument for the "inherited artifact" reading, on top of
   the already-established formula-regime miss.
3. **[MATERIALS' rule, precisely scoped, §4/§8 item 3]** State both halves
   together: the Iteration-59 rule does not automatically re-apply (genuine
   ambiguity remains, formally open); the current evidence leans the prior
   toward its original reading, not a symmetric open question.
4. **[Energy-interception pattern, logged, §5/§8 item 4]** Log as a
   two-cycle-old named-but-deferred item; a third consecutive deferral
   without an explicit, cycle-specific reason would fire Checkpoint
   criterion 4, matching this program's own R8-family standard.
5. **[R5 pre-registration note, carried forward, §8 item 6]** Standing
   discipline note, now a four-cycle-running pattern — not a fresh rule.

### Tier 1 — cheap FDTD, near-unanimous next, upgraded per this audit

6. **MATERIALS' article-radius (`R_OUT`) discriminator — the single
   highest-value item on the board, ranked #1 or #2 by all six Phase-5
   seats — UPGRADED per §6/§8 item 5, above: pre-register AT LEAST TWO
   alternate radii (e.g. `R_OUT∈{50,100}`, alongside the existing `78`
   baseline — geometrically feasible in both `C40`/`G40` domains without
   resizing, independently confirmed this audit), not the single radius
   every review that names it currently specifies, so the outcome
   distinguishes a genuine scaling trend from a coincidental shift.
   Pre-register the directional prior (§3/§4, above: "period stays
   pinned" is the currently-favored reading) explicitly before running.
7. **PHOTONICS' own zero-FDTD Fresnel/Kirchhoff edge-diffraction desk
   derivation (§2.1 of its own Phase-5 review)** — applied FIRST to the
   empty-scene `C80−C40`/domain-or-source-edge geometry where `P_edge_A`
   actually originates, then to the article's own rim as a cheap second
   comparison. The single test that could finally derive T28's founding
   periodicity from first principles (nine-plus prior mechanism cycles all
   modeled boundaries as reflectors, never as diffractors) — if it succeeds
   on the empty scene, item 6's own sweep can be scored against a
   quantitative prediction, not a bare direction.
8. **A committed, independently-reproduced AR(1)-matched null-calibration
   test for the two-tone admixture question** — QUANTUM's own §2 design
   (fully specified: measure `φ̂`, generate synthetic H0 data, sweep `φ̂`,
   inject known admixture amplitudes to characterize power) is the correct
   vehicle; it MUST reconcile with, and either confirm or correct, this
   audit's own §0.3 non-reproduction of EM's earlier figure before either
   number is treated as final.

### Tier 2 — standing, increasingly overdue items

9. The near-null σ(I) article follow-up (`off_pass`, `τ_off≈0.0065`) — still
   standing from Iteration 59's own board, not run this cycle either.
10. QUANTUM's own lossless-PEC-only-disk control — still open.
11. The `PAIR_ABSORB40`/`C80−C40` extension — still open.
12. The x-wall wavelength-generality leg (750/450nm) — now **EIGHT**
    consecutive cycles deferred (076–083), exceeding every other item's own
    pre-tripwire streak on this board; should not be deferred again without
    an explicitly stated reason.
13. A proper R3-grade settling convergence study with the article present.

### Tier 3 — governance

14. Checkpoint criterion 2 ruled N/A this cycle (not merely not-yet-ripe) —
    artifact-attribution/statistical-methodology work, no mechanism-class
    claim made anywhere, including in this audit's own new findings.
15. Checkpoint criterion 4 ruled non-firing on all three matters this audit
    adjudicated (fix-docket adoption, confirmed landed; git-provenance
    restoration, triple-independently-verified genuine; EM's own AR(1)
    figure, caught and corrected within this review layer).
16. The energy-interception item's own two-cycle-old pattern, logged
    explicitly as approaching — not yet at — the R8-family tripwire.

---

## 11. Bottom line

**Combined Verdict: PARTIAL.** The period-family question exp-082 showed was
unresolvable at 7-point power is resolved, decisively and doubly
instrument-corroborated, at full power: Branch B, matching T28's own
long-standing `P_edge_A` family, not QUANTUM's mechanism-continuity
hypothesis. The causal question — what `P_edge_A` physically is, and
whether the article's own rim is genuinely responsible — remains open, and
this audit sharpens the board's own prior toward "inherited pre-existing
artifact" with a new, source-verified finding (`P_edge_A`'s own
article-free provenance) without yet proving it, correctly stopping short of
letting MATERIALS' own Iteration-59 rule re-apply as settled. The two-tone
`PAD`-continuity admixture question is REVERSED under the correct,
order-preserving null (independently reconfirmed a fourth time here) and
remains open in both directions; EM's own new AR(1)-parametric alternative
is methodologically sound in principle but its own specific reported figure
does NOT independently reproduce under this audit's own from-scratch,
five-variant reconstruction — logged explicitly, not adopted, matching this
program's own R4 discipline applied here for the first time to an
uncommitted Phase-5-review figure. The near-unanimous six-of-six ranking of
MATERIALS' article-radius discriminator as Iteration 61's own top item is
correct but under-specified as filed by every review that names it — upgraded
here to a genuine multi-radius trend test. The joint EM/THERMO
energy-interception cross-check is logged as a two-cycle-old
named-but-deferred pattern, not yet firing, approaching the tripwire.
Checkpoint criteria 1/3 N/A, criterion 2 N/A, criterion 4 does not fire on
any of three matters adjudicated, criterion 5 not at risk.

No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document or
by anything it recommends.
