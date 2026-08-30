# PHASE 2 — RED TEAM AUDIT · Panel Iteration 70 · exp-093

*Fresh sub-agent, RED TEAM charter (PANEL.md, verbatim: attacks every
proposal, speaks last and hardest; standard is not textbook-physics
compliance; kills internal inconsistency, unfalsifiable claims, mechanisms
that cannot be expressed as simulation parameters, and quiet constraint
violations — especially #3). Received: `phase1_proposal.md` in full; all
five blind Phase-2 critiques in full; LOGBOOK.md in full (R1–R15,
ESTABLISHED, LIVE THREADS, the complete T28 record through Iteration 69);
exp-092 in full (predecessor cycle); exp-090's `run.py` (source of
`auc`/`firth_logistic`/`find_zero_crossings`); exp-077 in full (source of
`pad_round_trip_echo_model`); exp-091's and exp-092's own EM Phase-5
reviews (source of the aperture-length mandate). Every disputed number
below was independently recomputed in this session, from primary source,
via Bash/Python — not taken on any party's word, including the proposal's
own pre-verification and the critiques' own recomputations.*

## 0. Scope note

This cycle is pure instrument/calibration work: T1 route N/A, no
phenomenon-mechanism claim, `REALIZABILITY_MEMO.md` untouched — verified
directly against §12's own grep-based check, which is itself correct
(every T28 entry from Iteration 46 through 69 does state "T1 route N/A").
Constraints 1–4 are not engaged by this cycle's *substance*. The attacks
below are about internal consistency and claim-scoping, not phenomenon
compliance — exactly this seat's charter for a desk/instrument cycle.

---

## RT-1 — [inconsistency] Item 2's "AUC/direction reversal" is a
sign-convention artifact, not a finding (Dispute A — QUANTUM's attack,
UPHELD, independently re-derived from raw source)

**Independently verified, not merely re-checked.** `experiments/090-.../
run.py` defines `auc(scores_pos, scores_neg)` as the raw Mann-Whitney
concordance (fraction of pairs where `pos > neg`), and its own `main()`
calls it **exactly once**, at the one line that produced the filed
`AUC=1.0000`:

```
auc_margin = auc(-pos_m, -neg_m)  # lower margin => more likely X
```

— confirmed at `run.py:197`, and confirmed against the committed
`results.json::q1.auc_margin=1.0`. This convention is not incidental
window-dressing; the comment states outright what question it answers
("lower margin ⇒ more likely X").

Running the *identical* Python function, with the *identical* negated
calling convention, against the proposal's own §6 n=8 table
(`pos={2.3005,4.1083}`, `neg={5.4287,9.1877,11.2790,15.6474,20.6530,
23.1785}`):

```
auc(-pos, -neg)  ->  1.0000   # exp-090's own calling convention
auc( pos,  neg)  ->  0.0000   # the proposal's own reported "reversed" figure
```

Both computed live in this session, byte-identical to QUANTUM's own
figures. **The 0.0000 the proposal reports as evidence of reversal exists
only because item 2 dropped the negation exp-090 itself used to produce
the number it is being compared against — a different, silently
substituted question ("does higher margin predict Y=1?", trivially no in
both datasets), not independent corroboration of a real reversal.**

Two further independent checks, both run live this session, both confirm
no reversal exists:

- **Firth's fit.** Re-implementing `firth_logistic` from source and
  fitting `X=[1,log10(margin)]` against the n=8 table reproduces the
  proposal's own `β=[3.76504788,-5.60700572]`, `m₅₀=4.693425526`, 15
  iterations — bit-exact. exp-090's own filed fit is `β=[1.7805895,
  -5.6315196]`. **Both slopes are negative** — the algebraic signature of
  "lower margin predicts Y=1" in *both* datasets, not a sign flip between
  them.
- **The zone formula.** exp-090's own committed code (`run.py:222-223`)
  is literally `zone_lo=max(pos_m)`, `zone_hi=min(neg_m)` — unconditional,
  no branch on direction. Applied unmodified to the n=8 table it gives
  `[4.1083,5.4287]` directly. The proposal's own §6 text ("the roles of
  `max`/`min` swapped to match the reversed direction") describes a
  modification that was never actually needed or made — the formula is
  identical in both datasets.

**Ruling: no real reversal exists. This is a sign-convention artifact,
confirmed three independent ways (AUC under the matching convention,
Firth's slope sign, the unmodified zone formula) against exp-090's own
committed source, not a re-derivation of QUANTUM's own claim by a
different route — I built each check from `run.py` myself.** The genuine,
disclosable finding item 2 actually supports is the one QUANTUM names:
the n=8 `cpl=30`-only sample preserves the **same** lower-margin-predicts-
`Y=1` relationship as the original n=7 `cpl=20` sample, on a
non-contradictory but numerically different zone. This is a real,
independently valuable finding — the proposal does not need a false
"reversal" headline to be worth reporting, and asserting one would corrupt
the very Idealization (15) built to carry it forward and the Phase-4
bit-exact reproduction gate (§11) that would faithfully certify the wrong
claim if run unmodified.

---

## RT-2 — [inconsistency] Item 4's chosen length scale substitutes a
different, already-refuted mechanism for the actually-named mandate; §13's
R8-discharge claim does not survive as scoped (Dispute B — EM's attack,
UPHELD, independently re-derived from primary source, with a supplementary
computation of my own)

**The mandate, verified from its own two prior citations, not from this
proposal's characterization of them.** `experiments/091-.../
phase5_review_em.md` §4(i) (grep-verified, lines 165-166): *"...the
interference is generated by path-length differences accumulated across a
large fraction of the aperture's own half-width (`A=752` cells native,
`1128` cells at R3, i.e. tens of wavelengths)"* — and names, as its own
Rank-1 recommendation, computing "the predicted Yee-grid dispersion phase
accumulation for this exact aperture/propagation geometry." Restated a
second time, `experiments/092-.../phase5_review_em.md` line 325 (this same
seat's own self-review, one cycle later): *"a desk calculation using this
bench's own established Yee-dispersion relation and the aperture's own
known geometry (`A=1128` cells at R3)."* **Both of the two prior citations
this cycle's own §7 opening line claims to finally discharge name the
aperture length `A≈752–1128` cells — not `PAD`.**

Item 4 instead computes `ℓ=2×PAD` (80 cells native, 120 at R3) — roughly
**9.4× shorter** than the actually-named length scale, with no
reconciliation anywhere in §7 or §13.

**Worse, the supporting citation is itself backwards.** §7 cites "this
bench's own established `pad_round_trip_echo_model`, exp-077" as physical
grounding for the PAD choice. Independently read from exp-077's own
`NOTES.md::Result` (not from any later summary): exp-077's own Mandate
section states its purpose was to test the coherent-echo mechanism
"against `PAD`'s round-trip distance" — the identical length scale item 4
now reuses — and its own Result table gives, for the complete two-wall
instrument (exp-077's own final, most-complete cut):

| | `PAIR_PAD` |
|---|---|
| Two-wall Test B (shape) | **`r²=0.0001`** REFUTE |
| Two-wall Combined (final) | **REFUTE** (shape-driven) |

**`pad_round_trip_echo_model` is not "established" support for the PAD
length scale — it is this program's own prior REFUTE of exactly that
mechanism**, independently confirmed at the time four separate ways
(PHOTONICS' and EM's own Phase-2 retargets, Red Team's Phase-2 audit, and
the Phase-4 re-run all agreeing to 4 decimal places, per exp-077's own
`NOTES.md`). Citing a refuted mechanism as unqualified grounding for a
new, unrelated computation (the dispersion integral) is a citation-shape
error this program's own R9 lineage exists to catch — the two uses of
"PAD round-trip distance" are not interchangeable just because they share
a name; one is a reflectance-model claim (refuted), the other is a
numerical-dispersion claim (item 4's own, novel), and item 4's prose
conflates them into false mutual support.

**Consequence for §13's R8 claim.** §13 states: "item 4 directly
discharges the standing tripwire (§7): the named, affordable check is now
actually run, not argued a third time." **This is false as scoped.** The
named check — dispersion accumulated over the aperture propagation
length — has still never been run. What was run is a different,
plausible-sounding but non-mandated candidate, at a length scale roughly
an order of magnitude shorter, supported by a citation that is itself a
refutation of a different mechanism sharing the same name. If this stands
uncorrected into Phase 3, the actual mandate (`ℓ=A`) will have been cited,
substituted-around, and left unrun a **third** time in substance — the
exact outcome R8's own third-citation tripwire (named explicitly at
exp-092's Red Team audit) exists to prevent, even though something with
the right shape was computed.

**Supplementary check, my own, disclosed as approximate and non-load-
bearing.** Using item 4's own dispersion formula and Brent-solved
`k(θ,cpl)` (independently reimplemented and verified to reproduce every
figure in §7's own table to the stated precision), substituting `ℓ=A`
(752 cells native / 1128 at R3) for `ℓ=2×PAD`:

| θ | observed Δθ | ratio at `ℓ=2×PAD` (proposal's own) | ratio at `ℓ=A` (mine, approximate) |
|---|---|---|---|
| 40.0718° (lower) | −0.194° | ~303× | ~32× |
| 41.7811° (upper 1) | +0.320° | ~762× | ~80× |
| 41.8377° (upper 2) | +0.377° | ~898× | ~96× |

At the mandated length scale the mismatch shrinks by roughly the `A/PAD`
ratio (~9.4×), as expected — still a genuine, order-of-magnitude REFUTE at
all three points, but the lower crossing (~32×) would **not** clear the
proposal's own pre-registered "at least two clear orders of magnitude, not
a near-miss" REFUTE band (its own stated `100×–1000×` range, §11). I have
not traced `A` to `design_geometry.py`'s own exact defining formula myself
(I used the two literal figures EM's own reviews cite) — this table is a
directional cross-check, not a substitute for a properly sourced Phase-4
computation, and is reported with that caveat. It does, however, mean the
R8-discharge outcome is not a foregone conclusion at the correct length
scale, and the wide, clean 300×–900× margin item 4 currently reports may
be an artifact of testing the *wrong*, shorter length scale rather than
evidence the mandate itself would refute as cleanly.

**Ruling: item 4, as currently written, does not discharge the R8
tripwire on the aperture-propagation mandate. It must be re-run (or, at
minimum, computed a second way and reported side by side, per EM's own
offered fix) using `ℓ=A` sourced directly from `design_geometry.py`,
before §13 may claim R8 is discharged.** The PAD-length computation itself
is not worthless — it is a real, correctly-computed REFUTE of a
*different*, previously-refuted candidate — but it must be relabeled as
such, not substituted for the mandate.

---

## RT-3 — [inconsistency] §13's R15-"completion" claim is not supported by
this cycle's own data; item 1's off-grid sweep is angular-only and does
not itself constitute an R15-grade cross-resolution check (PHOTONICS' and
MATERIALS' attacks, UPHELD, both, as complementary not competing findings)

**MATERIALS' attack, independently checked against R15's own founding
text (LOGBOOK.md, above).** R15's minimum discharge, per its own founding
language, requires the underlying feature's resolution-sensitivity to be
"independently R3-verified" before a calibration boundary built near it is
trusted. MATERIALS' own exp-091 §5 named two live discharge paths: (a) all
seven of exp-090's original caution-zone points R3-verified, or (b) a
resolution-aware regressor replacing FLOOR-margin outright. **Neither is
met here.** Three of exp-090's seven original points (36.0°, 38.4°, 38.8°)
still have zero `cpl=30` measurement — this proposal's own §9 discloses
this explicitly ("Tier 3... still deferred") — and item 2's zone
construction reuses the identical FLOOR-margin/Firth machinery unmodified,
never itself validated stable across resolutions, since a `cpl=40`
comparison point is explicitly declined this cycle on budget grounds (§9).
Nothing in this cycle establishes that `cpl=30` is the *converged*
resolution rather than merely *a different single resolution* from
`cpl=20` — the identical epistemic gap R15 was founded to close between
`cpl=20` and `cpl=30` now reopens one level up, unacknowledged by §13's
own "direct completion" framing.

**PHOTONICS' attack, independently checked against item 1's own
design.** §5's own text is explicit that item 1's six new points are
"off-grid," "0.025° step," at fixed `cpl=30` — a purely **angular**
refinement. Nothing in item 1 tests spatial (`cpl`) resolution in the
disputed 41.75°–41.90° window itself; the only `cpl=40` item this cycle
even considers (§9, "Tier 2 — a third `cpl=40` resolution point") targets
the *original three census angles*, not this window. A "TWO-NODE
CONFIRMED" verdict from item 1 would genuinely rule out a 3-point
linear-interpolation artifact across a single trough — a real result — but
it says nothing about whether the double-crossing itself is a
`cpl=30`-specific discretization artifact, exactly the R15 failure shape
this sub-thread's own parent cycle (exp-091) established by a genuine
`cpl 20→30` check, not by denser angular sampling at one fixed
resolution. §6's own gate table, however, is written to consume a
TWO-NODE CONFIRMED result as if it were R15-qualified evidence extending
the zone — no idealization anywhere flags this angular/spatial
distinction.

**Both attacks land on the same underlying gap from different angles
(MATERIALS: the zone-level completeness claim; PHOTONICS: the specific
mechanism by which item 1's own output could be mistaken for an R15-grade
check) — not a duplicate finding, a converging one, exactly the shape this
program's own record treats as strengthening, not discounting, both.**

**Ruling: UPHOLD both, in full.** §13's R15 bullet must be reworded (per
MATERIALS' own offered fix, essentially verbatim) to state this cycle is a
further, `cpl=30`-verified *step* toward R15's founding mandate, not its
completion. Additionally (PHOTONICS' own offered fix), a new, explicit
idealization must state that item 1's three-way outcome is angular-only
and not itself an R15-grade cross-resolution finding, and item 2's gate
(§6) must be worded so that a TWO-NODE CONFIRMED or SINGLE-NULL result
from item 1 extends the table as *provisional pending a future spatial
check*, not as a settled R15-closing input. This costs zero FDTD and no
schedule change — pure wording and one added idealization.

---

## RT-4 — [inconsistency] §1's bare "detectability" language repeats a
disclaimer-erosion shape this sub-thread has fired Checkpoint 4 on four
times before; §10's carried-idealizations banner drops two live items
(VISION's attack, UPHELD on substance, ruled non-firing on discharge —
same reasoning as VISION's own Phase-2 self-assessment)

Independently re-read §1 against VISION's citation. Lines 33-34 and 40-41,
verbatim: THERMODYNAMICS' reading of the upper window "for
detectability: **nothing, either way**" and the energy channel staying
"smooth and undetectable regardless" — **zero inline qualifier at either
occurrence** distinguishing NETD/instrument detectability from constraint-
3's human-eye detectability. The disambiguating text (Idealization 3)
first appears roughly 470 lines later, in §10. This is, independently
confirmed against LOGBOOK's own record (grep against the T28 thread), the
same *shape* of gap that fired Checkpoint criterion 4 at Iterations 53,
63, 64, and 65 — a claim's disclaimer separated from its point of use, not
merely absent.

Independently re-read §10 against exp-092's own `NOTES.md` Idealizations
section (11 numbered items, read directly, not from this proposal's
citation of them). §10 cites 3/6/7/11 — each individually accurate, no
misquote — but silently drops **Idealization 1** (2D TMz, single
λ=600nm, no chromatic sweep), which every one of this cycle's 56 new FDTD
calls is subject to and which a bare "undetectable" claim needs precisely
to stay scoped, and **Idealization 8** (the still-open unbiased
margin-vs-distance rebuild), which §9 restates in prose but never folds
back into the numbered banner it belongs in — the identical drop shape
this same numbered idealization was already caught missing from
exp-092's own Phase-1 draft one cycle earlier (Iteration 69, LOGBOOK).

**Ruling: UPHOLD on substance — this is a real, textually verifiable
gap, not a stretch.** Ruled **non-firing on the Checkpoint-4 discharge
test**, for the same reason this program's own precedent treats an
identical shape as non-firing when caught here: this is being caught blind
at Phase 2, before Phase 3 freezes any language, by the seat whose own
charter duty is exactly this check (PANEL.md's own text: "pin numeric
thresholds... BEFORE any run that scores against them" — here, before any
*prose* freezes ahead of any run). If this exact language survives
unfixed into `NOTES.md`, that reopens the firing question at Phase 5 on a
fifth instance in this sub-thread — a fact that should weigh toward
treating this as load-bearing in the mandatory-fix docket below, not a
stylistic nit, even though it does not fire today.

---

## Minor findings, folded into the docket, not separately numbered attacks

- **MATERIALS' process gap**: the one-sentence `sigma_max=1/3`
  disambiguating note (numerical rescaling, not `REALIZABILITY_MEMO.md`
  Entry 2's unrelated real-object formula) that MATERIALS' own exp-092
  review recommended for future citations is not carried forward here.
  Independently confirmed real, zero-cost to add.
- **VISION's minor gap**: `NETD_BAND_K=(0.020,0.050)` cited in §11 without
  its inline Iteration-20/exp-043 provenance pointer, unlike this
  proposal's otherwise consistent sourcing practice elsewhere. Confirmed,
  zero-cost.
- **QUANTUM's R14-discharge note**: §13's R14 bullet is narrowly true
  (the NETD fields themselves are non-gating) but sits adjacent to §6
  prose that blurs which fields item 5 reproduces (40.0°, bit-exact,
  already-scored) versus adds (the NETD sidecar itself) for a reader not
  tracing carefully. A one-sentence tightening, not a mandatory
  restructuring — folded into the docket for completeness, not
  independently escalated.

None of these three, individually or together, changes the overall
verdict; all are additive, zero-FDTD, zero-schedule-impact wording fixes.

---

## Working through PANEL.md's five Checkpoint criteria explicitly (not
asserted by precedent — checked against this cycle's own record)

1. **A configuration passes all constraint metrics.** Not applicable —
   this cycle makes no constraint-metric claim (T1 route N/A, verified
   §12, independently re-confirmed by my own grep against LOGBOOK.md's own
   T28 entries). Does not fire.
2. **A proven boundary — mechanism class jointly unsatisfiable.** Not
   applicable — no mechanism-class claim is made or resolved; this is
   pure instrument calibration. Does not fire.
3. **Synthesis requires engine physics beyond the validated bench
   classes.** Not applicable — every item reuses committed `lab/`
   functions verbatim (`materials.graded_black_shell`,
   `ambient.contrast_from_runs`, exp-090's own statistics module); zero
   new `lab/` diff proposed anywhere in this document. Does not fire.
4. **Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped).** **This is the one requiring real
   judgment, not a reflexive no.** RT-1 and RT-2 above are exactly the
   *shape* of defect (a false "reversed" headline; a mandate substituted
   with a strawman and a backwards-refuted citation) that has fired
   Checkpoint 4 eleven times in this program's history when it reached
   Phase 3/LOGBOOK undetected. **It has not reached that point here** — I
   am catching both, independently re-derived from primary source, at
   Phase 2, before any synthesis exists, matching this program's own
   established non-firing pattern (Iterations 51, 53, 55, 66/67: "caught
   blind, at Phase 2/5, before Phase 3 froze anything or before a LOGBOOK
   entry existed" is this program's own repeatedly-applied discharge
   test, not a Red-Team invention for this cycle). **Ruling: does not
   fire, PROVIDED the mandatory fixes below are actually applied before
   Phase 3 freeze** — if RT-1's or RT-2's language survives into
   `phase3_synthesis.md`/`NOTES.md` unfixed, that reopens this question
   at Phase 5 on a record that would then show the defect was named,
   specific, and affordable to fix, and was not fixed — the exact
   "known, named, ignored" shape R6–R12 all fire on. This is not a
   discretionary caveat; it is the actual condition of the non-firing
   ruling.
5. **Two consecutive iterations with no logbook-advancing result.**
   Iteration 68 (exp-091, R15 adopted, materially revised the caution
   zone) and Iteration 69 (exp-092, the sigma confound resolved cleanly,
   the lower crossing located) were both independently confirmed
   logbook-advancing PARTIAL verdicts in LOGBOOK's own record — not two
   non-advancing cycles. Does not fire, regardless of how this cycle
   itself ultimately scores.

**None of the five criteria fire**, matching the task brief's own
expectation for a desk/instrument cycle — but criterion 4's non-firing is
conditional on the docket below being adopted, not unconditional, and that
distinction is itself the point: an unverified argument that a gap is
"probably fine" is exactly what R8 forbids; this ruling rests on having
actually recomputed both disputed numbers from source, not on reasoning
about them.

---

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The underlying instrument design — sequencing (item 5 → 3 → 1 → 2 → 4),
the determinism argument for item 5's backfill, the branch-gating logic
between items 3 and 1, R13's floor gate applied consistently to every new
point, the desk-only Yee-dispersion *arithmetic* (verified independently,
correct) — is sound, and every one of the six mandatory fixes below is a
zero-FDTD, zero-schedule wording/computation correction, fixable entirely
before Phase 3 freeze at no cost to the 56 already-budgeted FDTD calls.

**Mandatory fixes (six, none overridden, none discretionary):**

1. **(RT-1 / Dispute A.)** Recompute item 2's `AUC(margin)` using
   exp-090's own `auc(-pos_m,-neg_m)` calling convention. Strike
   "REVERSED"/"opposite decision rule"/"roles of max/min swapped"
   language from §6 and §11. Restate the correct finding: the n=8
   `cpl=30`-only sample preserves the SAME lower-margin-predicts-`Y=1`
   relationship as the original n=7 `cpl=20` sample, with zone
   `[4.1083,5.4287]` — a real, non-contradictory, independently valuable
   finding on its own terms. Update Idealization 15 and the Phase-4
   bit-exact reproduction gate to certify the corrected direction.
2. **(RT-2 / Dispute B.)** Recompute §7's dispersion-integral table a
   second way using `ℓ=A` (the aperture propagation length, ≈752/1128
   cells, sourced directly from `design_geometry.py`, not approximated),
   report both length scales side by side. Strike or heavily qualify the
   `pad_round_trip_echo_model`/exp-077 citation as unqualified support —
   disclose explicitly that exp-077's own Result REFUTEd that exact
   mechanism (two-wall `r²=0.0001` for `PAIR_PAD`). Reword §13's R8
   bullet to not claim discharge until the `ℓ=A` computation exists;
   if `ℓ=A` also refutes cleanly, the R8 tripwire is genuinely
   discharged with a stronger, correctly-scoped result; if it does not,
   that is itself the more important finding this mandatory check was
   meant to surface (EM's own offered flip condition, adopted verbatim).
3. **(RT-3 / R15-completion overclaim.)** Reword §13's R15 bullet from
   "direct completion" to a further, `cpl=30`-verified *step* — name both
   still-open discharge conditions (Tier-3 points, no `cpl=40`
   comparator) explicitly, per MATERIALS' own offered fix.
4. **(RT-3 / angular-vs-spatial conflation.)** Add a new, explicit
   idealization stating item 1's three-way outcome is angular-only
   (fixed `cpl=30`) and not itself an R15-grade cross-resolution
   finding; reword item 2's gate (§6) so a TWO-NODE CONFIRMED or
   SINGLE-NULL extension is reported as provisional pending a future
   spatial (`cpl=40`) check at the interior near-null angles specifically,
   per PHOTONICS' own offered fix.
5. **(RT-4 / disclaimer erosion.)** Add an inline
   `(NETD/instrument, not human-eye)` qualifier at both bare
   "detectability"/"undetectable" occurrences in §1 (the two sentences
   quoted above). Add Idealization 1 (2D TMz, single λ=600nm) and
   Idealization 8 (the still-open unbiased margin-vs-distance rebuild) to
   §10's carried-idealizations banner, which currently cites only 3/6/7/11.
6. **(Minor items, batched.)** Carry forward MATERIALS' `sigma_max=1/3`
   disambiguating note; add VISION's inline `NETD_BAND_K` provenance
   pointer (Iteration-20/exp-043); tighten §13's R14 bullet per QUANTUM's
   note distinguishing item 5's reproduced vs. newly-added fields.

**Zero items overridden.** All six fixes are additive wording/desk-
computation changes; none require re-sequencing, re-budgeting, or
touching any of the 56 already-designed FDTD calls. Phase 3 should
independently re-verify RT-1's and RT-2's own recomputed figures a further
time before freezing predictions, matching this sub-thread's own
established practice (the Director independently re-verifying Red Team's
own requested numbers before freeze, exp-090/091/092 precedent) — not
adopting this audit's own numbers as a substitute for that step.
