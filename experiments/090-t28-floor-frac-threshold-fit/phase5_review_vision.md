# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 67 · exp-090

## 0. Independent verification performed before writing this review

I did not take any prior party's "reproduced bit-exact" claim on faith,
including my own cycle-2 self's. From `results.json` and the three source
experiments (`experiments/087,088,089/.../results.json`), I:

- Recomputed all 7 `margin`/`ratio_k` triples from `frac_contrast` against
  `FLOOR=1.91744×10⁻⁴` — bit-exact to Table 1: sorted margins
  `1.3095(X), 1.4764(X), 2.1709(C), 3.8793(C), 6.5889(C), 7.4946(C),
  8.0187(C)`, `AUC=1.0`, no ties.
- Re-implemented, from scratch, in a throwaway Python/NumPy script (no
  reuse of `run.py`): (a) Firth's modified-score Newton–Raphson fit —
  converged in 20 iterations to `β=(1.78058954, −5.63151961)`,
  `m₅₀=2.0710128`, bit-exact to `results.json::q4`; (b) the naive
  unpenalized MLE — after 2000 iterations mine ran to
  `β≈(92.9,−366.9)`, still diverging (the exact endpoint differs from the
  committed `(26.1,−103.0)` because unregularized divergence is
  step-size/damping-sensitive by nature — the qualitative fact both
  confirm, non-convergence to a finite optimum, is what P1/Q1 actually
  claims, and it holds under my independent implementation too); (c) the
  exact `C(7,2)=21` permutation enumeration — `p=1/21=0.047619047619...`,
  bit-exact.
- Independently traced the "1.046× thinnest-ever" superlative (Q7) to its
  origin: `experiments/089-t28-combined-angle-census/NOTES.md` line 283/288
  states this figure verbatim ("1.046× (thinnest ever)" in the Q3 table;
  "the thinnest noise-floor resolved-margin (1.046×) this sub-thread has
  ever accepted as `resolved=True`" in prose), and LOGBOOK.md's own
  Iteration-66 entry independently restates the identical figure
  ("37.2° (thinnest resolved-margin, 1.046×, this sub-thread has ever
  accepted)"). exp-090 neither invents nor inflates this claim — it
  correctly attributes it, recomputes it independently
  (`1.045659×`, matching to printed precision), and correctly labels it as
  a *different* quantity from R13's own `frac_contrast`-based `margin`
  (the ordinary `resolved`-gate noise-floor test vs. the floor-fraction
  gate this cycle's zone is built on). I did not attempt to independently
  re-derive whether 1.046× is truly the thinnest margin ever accepted
  across the *entire* T28 record back to exp-069 (that would require
  re-auditing every resolved-margin computation in ~15 prior experiments,
  disproportionate to what this specific superlative's provenance chain
  already establishes) — but the chain of custody from exp-089 through
  LOGBOOK to exp-090 is clean, consistent, and correctly scoped as a
  carried citation, not a fresh claim. No inflation found.
- Cross-checked all nine of Red Team's Phase-2 mandatory-fix docket items
  against `phase3_synthesis.md` and the final `NOTES.md`, item by item
  (§1, below) — not merely trusting the Director's own "all nine adopted"
  line.

## 1. Docket-by-docket verification (Red Team's nine mandatory-fix items)

I read `phase2_redteam_audit.md`'s docket independently and checked each
item against the artifact that should carry it, rather than trusting
`phase3_synthesis.md`'s own one-line dispositions.

1. **Dual-section banner** — LANDED, with a caveat (see §2, below — a
   real, narrower gap survives inside this fix, not caught by Phase 2 or
   Phase 3). The literal top-level requirement (a banner present at both
   the Predictions and Result sections) is satisfied: both sections carry
   an explicit "Carried idealizations banner" paragraph.
2. **R3 spatial-resolution disclosure (MATERIALS)** — LANDED. Idealization
   9 states it in full, explicitly naming 40.2°/41.4° as the zone's
   load-bearing lower-edge points and citing the already-queued exp-089
   Tier-1 item 3 as the discharge path. Correctly tied to Q3 in the
   Predictions section ("Idealizations 6/7/13, 9-11 apply").
3. **Forward-sampling-bias disclosure (THERMODYNAMICS)** — LANDED, as
   Idealization 10, verbatim to the fix's own request (CAUTION-zone
   angles should be oversampled, not deprioritized, for any future
   `σ_abs(θ)` build).
4. **Reword P2/Q2's evidentiary claim (EM)** — LANDED. Q2 in both
   Predictions and Result explicitly states the permutation test
   "confirms internal pipeline/arithmetic correctness only — it is NOT
   independent evidence," with the mechanistic reason (exp-089's own
   ~90%-denominator decomposition) stated inline both times.
5. **Reword P5/Q5's falsifiability claim (QUANTUM)** — LANDED. Q5 in both
   sections explicitly states this is "a deterministic illustration of
   point-sensitivity, not a live stress test," crediting QUANTUM's own
   order-statistics argument by name in the Result section.
6. **Reclassify Q2/Q5 from falsifiable to diagnostic (Red Team's
   compounding finding)** — LANDED. Both are explicitly labeled
   "diagnostic sanity check" in the Predictions section headers, the
   `run.py` print banners ("DIAGNOSTIC SANITY CHECK ONLY"), and
   `results.json`'s own key names (`q2_diagnostic_only`,
   `q5_diagnostic_only`) — the fix reaches the code, not just the prose,
   which is more thorough than the docket strictly required.
7. **37.2°'s pre-existing fragility (Red Team RT-1)** — LANDED, as new Q7,
   in both Predictions and Result, with the "drop 37.2°" LOO row
   explicitly named as "the operationally primary sensitivity reading."
   I independently recomputed the cited `1.045659×` figure myself from
   `results.json::q7_disclosure`'s own persisted primitives
   (`p_abs_w_c40=2.8127×10⁻¹²`, `p_abs_w_g40=2.8087×10⁻¹²`,
   `box_dev_max=4.569×10⁻⁴`) via
   `|p_abs_w_c40−p_abs_w_g40|/(3×box_dev_max×p_abs_w_c40)` and confirm
   **1.0456×** — matches.
8. **Compute (not argue) the distance-to-crossing comparator (Red Team
   RT-3)** — LANDED as new Q8, run inside `run.py` itself (not left as
   Director scratch work, an improvement over the minimum the docket
   asked for). `AUC(distance)=1.0`, gap ratio `1.1121` vs. margin's
   `1.4704` — I recomputed the four zero-crossing locations myself by
   linear interpolation on exp-083's own 31-point `delta_scene` window and
   independently confirm `37.127°/38.590°/40.265°/41.461°`.
9. **Crossing-proximity-enriched-sample disclosure (Red Team RT-2)** —
   LANDED, as Idealization 11, naming exactly which 5 of 7 angles were
   selected for crossing-proximity and which 2 were not, matching
   `phase2_redteam_audit.md`'s own text closely.

**All nine items are substantively and correctly applied — this is not a
rubber-stamped "all adopted" claim; I find no gap between what the docket
asked for and what the document delivers, on any of the nine, except the
one described next.**

## 2. A genuine, previously-uncaught disclaimer-carry gap (my seat's own duty)

The mandatory dual-section banner (item 1, above) is present in both
sections — but its *scope* is not equal across them, and the narrower
scope in the Result section drops exactly the idealizations that the
Predictions section itself ties to specific, named items.

**The facts, checked directly against the file:**

- Predictions section, per-item citations: Q1/Q2/Q4/Q5/Q6/Q8 each cite
  "Idealizations 6/7/13"; **Q3 additionally cites "9-11"**; **Q7
  additionally cites "9"**.
- Result section's own banner (stated once, at the top, "governing every
  finding below"): **"Idealizations 6/7/13"** only — 9, 10, and 11 do not
  appear anywhere in the Result section, not in the banner and not in
  the Q3, Q7, or Q8 bullets individually.

Concretely: Q3's Result bullet reports the caution zone
(`[1.4764, 2.1709]`) as "bit-exact as predicted" with no restatement that
this exact number's own load-bearing lower-edge inputs (40.2°/41.4°) have
never passed an R3 spatial-resolution check (Idealization 9) — a caveat
the SAME document's own Predictions section explicitly, deliberately
attaches to this SAME item, three sections earlier. Q7's Result bullet
likewise omits Idealization 9 even though Q7 exists specifically to
disclose a fragility question about the same zone. This is not a
hypothetical risk: it is the identical shape as the lineage that fired
Checkpoint 4 at Iteration 65 (a caveat present correctly in one part of a
document failing to propagate into an adjacent prose restatement of the
finding it governs) — here, Predictions→Result rather than
`results.json`→prose, but the same "known, named, ignored-in-one-place"
structure.

**Is this a new, sixth-or-so instance of the recurring lineage, and does
it fire Checkpoint 4?** Applying this program's own standing discharge
test exactly as `phase2_redteam_audit.md` §3 applied it to VISION's own
Phase-2 catch this same cycle: this gap is caught here, blind, at Phase 5,
**before any LOGBOOK entry exists for this cycle** — matching the
"caught blind, same cycle, before LOGBOOK" non-firing condition every
prior instance of this lineage (including this cycle's own first
instance, caught by my Phase-2 counterpart) has been measured against.
Red Team's own Phase-2 audit this cycle explicitly found no text
generalizing Iteration 65's unconditional "fires automatically" language
for the fourth instance forward to any future instance of any kind — so
I do not rule this fires Checkpoint 4. **But it is a mandatory fix, not
a discretionary one**, per the Iteration-65 CHECKPOINT's own text, and I
flag it as such: the Result section's banner should be widened, or
carry per-item citations mirroring the Predictions section's own (at
minimum restating "9-11" beside Q3 and "9" beside Q7), before this
document is treated as a fully-closed, citable record.

**A governance point I add, not merely repeat:** this is now the
**third** distinct catch of this exact banner-carry-forward mechanism
inside two consecutive T28 cycles — exp-089's own in-cycle Phase-5
self-catch (a different but adjacent failure), exp-090's own Phase-2
VISION critique (banner missing from Predictions entirely), and now this
Phase-5 catch (banner present in both sections but narrower in Result
than in Predictions). Red Team's own Phase-2 audit this cycle already
named a mechanical lint-style safeguard as a standing item for
Iteration 68's board rather than a fourth bet on vigilance; this finding
is a direct, same-cycle data point in favor of building it, not deferring
it again. A hand-checked banner is evidently not sufficient even when the
Phase-1 lead is told, in writing, at Phase 2, exactly what the rule
requires and applies it in good faith — the failure mode is scope drift
within a correctly-attempted fix, not authorial neglect.

## 3. Steel-man of the cycle overall

This is careful, well-scoped, and unusually well cross-verified
instrument-calibration work. The three-layer method (non-parametric
zone, exact permutation test, Firth's bias-reduced fit) correctly
diagnoses and avoids the degenerate-MLE hazard at perfect separation
rather than reporting a false-confidence knife-edge; every load-bearing
number was independently reproduced by at least three parties before
this review (Phase-1 proposal, up to five Phase-2 critiques, Red Team's
Phase-2 audit, the Director's own synthesis-stage check, and now me) —
by my count, Q4's `m₅₀` alone has been independently re-derived from
scratch **five** separate times (proposal, EM, THERMODYNAMICS, QUANTUM,
Red Team, Director, me — actually seven) before this document was
committed, an unusually deep verification stack for a single number. The
Phase-2/Red-Team layer's own methodological correction — demoting Q2 and
Q5 from "falsifiable predictions" to "diagnostic sanity checks" once
QUANTUM proved P5's stated falsifier is an order-statistics tautology
given P1 — is exactly the kind of self-correcting rigor this program is
supposed to produce, and it reached the code (`results.json` key names,
`run.py` print banners), not just the prose. Q8's comparator (computing,
not arguing, that `margin` beats raw crossing-distance by a real,
measured ~3× robustness margin) converts an R8-shape gap into a genuinely
new, falsifiable, and confirmed finding — a real improvement over the
Phase-1 proposal's own original argued-only framing.

## 4. Sharpest attack (beyond §2)

Beyond the disclaimer-carry gap, I have no substantive attack on the
statistics themselves — every seat that touched this cycle's numbers,
including me, got the same answer. My sharpest remaining concern is
scope-adjacent to THERMODYNAMICS' own Phase-2 point (adopted as
Idealization 10): the caution zone is being handed to the rest of the
program as a clean, closed deliverable ("real and usable," per NOTES.md's
own Learned #1), but its own upper edge rests on exactly one point
(37.2°) that is *simultaneously* (a) the sample's most load-bearing
C-class point, (b) a pre-existing "felt-lucky pass" on an unrelated gate,
and (c) never resolution-checked. Three independent fragility findings
converging on one point is a stronger reason for caution than the
document's own Learned #1 framing ("real and usable") fully conveys —
Q7's own disclosure is honest and thorough, but it sits four bullets
below the headline framing, not beside it. A future citation skimming
this document for "the T28 caution zone is `[1.4764, 2.1709]`" is one
paragraph away from the caveat that number needs.

## 5. Verdict: PARTIAL

Concur with the substantive statistical work and with Phase 3's
disposition of Red Team's nine-item docket — all nine genuinely,
correctly, and in most cases thoroughly landed, several with more rigor
than the docket strictly demanded (item 6 reaching code, item 8 reaching
a fully reproducible script). This is not RULED OUT (no mechanism claim
is made; T1 route N/A, matching every T28 desk cycle since exp-069) and
not PROMISING (no constraint-metric progress, correctly, by this cycle's
own scope) — a genuine, logbook-advancing calibration result, consistent
with every other T28 desk-cycle verdict this program has issued. But my
own seat's specific charter duty — catching disclaimer erosion before it
becomes a settled record — finds one real, mandatory-fix-worthy gap (§2)
that Phase 2 and Phase 3 did not catch: the Result section's carried-
idealizations banner is narrower in scope than the Predictions section's
own per-item citations for the two items (Q3, Q7) that most need it. I
do not find this fires Checkpoint 4 (caught blind, same cycle, before
LOGBOOK, matching this program's own standing discharge test), but I do
not concur without qualification either — hence PARTIAL, not CONCUR.

## 6. Ranked top-3 candidate directions for Iteration 68

1. **The R3 spatial (`cpl` 20→30) resolution check on the
   `frac_p_abs`/`frac_contrast`/`ratio_k` channel — now undischarged
   THREE consecutive cycles (exp-088, exp-089, exp-090) and directly
   load-bearing for this cycle's own new deliverable.** This is not a
   generic backlog item: the caution zone's *lower* edge (40.2°/41.4°)
   sits nearest a real `delta_scene` zero-crossing, exactly the regime
   `VALIDATION.md` already documents as most exposed to this bench's own
   grid-staircasing error. Cheap (already queued, exp-089's own Tier-1
   item 3) and would retroactively validate or revise the single most
   load-bearing pair of numbers this fit produced.
2. **A repeat/denser measurement at or near 37.2°, specifically.** This
   cycle's own Q7 finding (independently confirmed by me, §1 item 7,
   above) shows this one angle simultaneously anchors the caution zone's
   upper edge, Firth's `m₅₀`, and carries a pre-existing, separately-
   documented "thinnest-ever" noise-floor pass. It is the single point
   whose own reliability, if it moves, would most change what this
   cycle's headline zone communicates to future citations — a direct,
   VISION-charter-relevant question (how much confidence does a
   threshold-adjacent measurement actually carry?).
3. **PHOTONICS' grazing-incidence validity check for the underlying
   `edge_diffraction`/R13-R14 measurement regime — still the
   near-unanimous #1 item on the whole T28 board, still not run.** Every
   angle this cycle's n=7 table draws from (36°–42°) sits in the
   aperture's own deep near-field/grazing-incidence regime; a validity
   check here would bear on whether the entire floor-gate/caution-zone
   apparatus this cycle refined is even being applied in a regime where
   its own underlying assumptions hold.

**Honorable mention, not scored as a physics direction:** build the
mechanical lint-style safeguard for the dual-section banner
(Red Team's own named, not-yet-adjudicated Iteration-68 board item) —
this review's own §2 finding is the third independent data point inside
two cycles that hand-checking this requirement is not fully reliable even
under good-faith, well-informed effort.
