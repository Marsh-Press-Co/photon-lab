# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 51 · exp-074

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (PANEL.md: sub-wavelength
structure; what could physically realize the proposed optical behavior;
owns the realizability bound — published / plausible /
unobtainium-with-parameters). Blind to every other seat's Phase-5 review
this cycle. Everything below was independently re-run against the actual
committed code, not taken on any document's word (LOGBOOK R4).*

---

## 0. What I ran

- `python3 desk_check_pricing.py` (unmodified) — reproduced
  `desk_check_pricing_results.json` bit-for-bit (`CHECK0 worst_rel_err=0.00e+00`,
  every per-pair/widened-window figure matched to the printed digit).
- `python3 fit_and_calibrate.py` (unmodified) — reproduced
  `fit_and_calibrate_results.json` exactly: `combined_verdict =
  HALT_NULL_MISCALIBRATED_9COL`, every one of 72 cell combinations FAIL,
  i.i.d. worst 8.7×–11.2× nominal at α=0.01, circular-shift 38.9×/46.1×/44.1×
  nominal at α=0.01 for C40–C60/C60–C70/C70–C80 respectively — matches
  `phase4_results.md` to the last reported digit.
- A grep sweep of every document and script in this directory for
  "material", "ABSORB", "medium", "permittiv", "realiz", "absorber" —
  full results below (§1).
- Independent re-derivation, from the committed `fit_and_calibrate_results.json`,
  of every circular-shift-vs-i.i.d. inflation ratio reported in
  `phase4_results.md`/`NOTES.md` (§3 finds a defect here).
- Cross-checked exp-074's citations of exp-073's own figures
  (`5.4×`/`5.7×` at α=0.01; `1.7×`/`5.7×` at α=0.10/0.01) directly against
  `experiments/073-t28-differential-beat-fit-reissue/phase4_results.md`'s
  own table — both citations are correct, verbatim.
- Read `phase2_redteam_audit.md` §6/§9 side-by-side with `phase3_synthesis.md`
  §2 to check R7 was adopted without drift.
- Grepped the full record for the erroneous "~45 calls" figure to confirm
  where it does and does not still appear (§2).

---

## 1. Finding — no smuggled `ABSORB` realizability claim; idealization discipline intact

**Clean.** `ABSORB`/`material`/`medium`/`permittiv`/`absorber` appear in
`fit_and_calibrate.py`, `phase4_results.md`, and `NOTES.md` **only** as: (a)
config-name components (`C40`, `C60`, …, never asserted as a material
parameter), and (b) the single, correct carry-forward reference in
`phase3_synthesis.md` §7 ("`ABSORB` not a material" — Idealization 2,
explicitly listed as still binding, unchanged). `fit_and_calibrate.py`'s
own docstring and code never compute an `ε(ω)`, an S-parameter, an
absorbed-power quantity, or any passivity/reciprocity comparison — exactly
the same disclaimed scope `phase1_proposal.md` §3 stated for
`desk_check_pricing.py`, correctly inherited rather than silently
re-litigated or dropped. **This is the specific failure my charter would
be first to catch — a boundary-condition sweep's statistical properties
quietly read back as evidence about a real material — and it does not
occur anywhere in this cycle's Phase 3/4 work.** Idealization-carry-forward
discipline is also intact more generally: `NOTES.md`'s "Idealizations"
section correctly points to all nine of `phase1_proposal.md` §4's items
(one, `z_joint(optimistic)`, correctly marked withdrawn rather than
idealized) plus `phase3_synthesis.md` §7's three new items — nothing was
silently dropped in the Phase 1→3→NOTES chain.

## 2. Finding — the `~45`-calls citation error is correctly and permanently resolved; no residual trace found

Grepped the entire record (`grep -rn "45 new\|≈45\|~45\|45 calls\|45-call"`
across this directory, `PLAN.md`, `LOGBOOK.md`). Result: the wrong figure
appears exactly where it should — `phase1_proposal.md`'s own original text
(kept, per house convention, as the as-written historical record) and the
critiques that caught it (my own seat's Phase-2 critique,
`phase2_critique_materials.md`; Red Team's audit,
`phase2_redteam_audit.md` §4/§9.4). `phase3_synthesis.md`'s docket
resolution (§1, item 4) explicitly corrects it to "~90/~180 calls, not
~45" and marks it "moot but recorded" since the widened-window
recommendation it would have justified was itself withdrawn the same
document. **Neither `NOTES.md` nor `phase4_results.md` — the two documents
a future cycle is most likely to cite from — repeats the wrong figure
anywhere.** This is the record working as R4 intends: the error is
preserved in its original location (not rewritten out of the historical
record), corrected exactly once at the point of synthesis, and does not
propagate forward into the documents downstream cycles will actually read.
Nothing further needs correcting here.

## 3. Finding (new, independently discovered this review) — the "3.5×–5.9× worse at every α" claim in `phase4_results.md`/`NOTES.md` does not reproduce from the committed data

Both documents state, verbatim and identically: "the circular-shift leg
is **not** indistinguishable from its own i.i.d. leg — it is **3.5×–5.9×
worse at every α**" (`phase4_results.md` line 45, `NOTES.md` line 103).
I computed the circular-shift/i.i.d. rejection-rate ratio directly from
the committed `fit_and_calibrate_results.json` every way I could construe
"worse... at every α" to mean:

| Method (iid comparator) | α=0.01 range | α=0.05 range | α=0.10 range | Overall |
|---|---|---|---|---|
| worst iid (max over 3 σ) | 3.47–5.07× | 2.74–3.30× | 2.24–2.66× | 2.24–5.07× |
| best iid (min over 3 σ, σ=0.008) | 4.48–5.40× | 3.22–4.02× | 2.63–3.00× | 2.63–5.40× |
| mean iid (avg over 3 σ) | 4.34–5.31× | 3.17–3.42× | 2.56–2.77× | 2.56–5.31× |
| fixed σ=0.0005 | 3.47–6.68× | 2.74–3.65× | 2.24–2.95× | 2.24–6.68× |
| every individual (pair, α, σ) cell (27 combos) | — | — | — | **2.24×–6.68×** |

**Under every one of these five constructions, the ratio at α=0.10 never
reaches 3.5× (it tops out at 2.95×–3.00×), and under two constructions the
ratio at α=0.01 exceeds 5.9× (up to 6.68×, at C60–C70/σ=0.0005).** The
claim "3.5×–5.9× worse at every α" is not reproducible from the script's
own committed output by any comparison method I could construct — it
appears to have been computed once (most likely from the single
α=0.01 row of the pair-level table two paragraphs above it in the same
document, which does fall in `[3.47, 5.07]`≈"3.5–5.1") and then generalized
to "every α" without re-checking the α=0.05/0.10 cells, where the true
ratio is materially smaller. **Non-outcome-determining** — the qualitative
claim it supports (circular-shift leg fails "far worse" than i.i.d., a
genuinely new and correctly-directioned finding) is not in doubt, and
nothing in the Combined Verdict depends on this specific numeric range —
but it is exactly the shape LOGBOOK R4 exists to catch: a range cited as
holding universally ("at every α") that a two-line independent
recomputation, from data already sitting in the same directory, shows does
not hold at one of the three stated α values. It sits in the **official
Phase-4 results document**, not a superseded draft, and is now duplicated
verbatim in `NOTES.md` — exactly the "survives into a second document"
pattern R4's own history (exp-048, exp-072/073) flags as the point past
which a figure should be caught. **Recommended correction:** replace with
either the honest full range (`2.2×–6.7×` over all 27 cells) or a
per-α breakdown (α=0.01: 3.5×–5.1×; α=0.05: 2.7×–3.4×; α=0.10: 2.2×–3.0×) —
the qualitative "circular-shift leg is worse at every α, and much worse at
tight α" conclusion survives either correction intact.

## 4. Finding — R7 was adopted without drift from Red Team's proposed text

Compared `phase2_redteam_audit.md` §6/§9.6 (Red Team's candidate rule)
against `phase3_synthesis.md` §2 (the adopted rule) sentence-by-sentence.
Substance is identical: necessary-not-sufficient framing, the "either
larger OR smaller" collinearity mechanism, the explicit "generalizes R6
one level upstream" framing, and the requirement that the design be
**both** fit **and** null-calibrated before a closure or detection verdict
is scored. No softening, no scope-widening, no silent addition. This is
the correct, checkable form of "adopted verbatim in substance" the
synthesis document itself claims.

## 5. Finding — R7 is well-scoped for the failure it targets, but is silent on a distinct, adjacent claim type this exact cycle also made and had to walk back

R7 closes the "priced, never fit" loophole: a conditioning/VIF bound on an
**already-collected** dataset's design matrix cannot substitute for
actually fitting that matrix and null-calibrating the fit. That is the
precise and correctly-scoped fix for what THERMODYNAMICS' and Red Team's
Phase-2 attacks found (§5's real `z9` beating the "optimistic" bound at
3/4 pairs).

**But `phase1_proposal.md`'s WIDENED-WINDOW-LICENSES-FURTHER-SPEND claim
was a different kind of claim — a forward-looking forecast about a
window with NO data yet — and it failed by a different mechanism** (a
missing, already-published SE-inflation/bootstrap correction factor,
QUANTUM's Phase-2 attack, confirmed and strengthened by Red Team to 0/4
pairs clearing 2σ) that R7, as adopted, does not address at all: R7's own
remedy ("fit the design to real data") is structurally inapplicable to a
window where no real data exists yet. A future cycle could satisfy R7 to
the letter for a widened-window proposal (there is no un-fit multi-tone
design being priced-not-fit, because there is nothing to fit yet) while
still repeating exactly the failure mode QUANTUM caught here — forecasting
achieved significance from a naive-OLS SE extrapolation without applying
an already-known, same-record noise-inflation correction. **This is not a
defect in R7 as written — its scope (already-collected data, priced
instead of fit) is exactly what it says — but it is a real gap worth
naming explicitly**: R7 governs the "priced not fit" failure on existing
data; it does not, and was not designed to, govern a "naively
extrapolated, not correction-adjusted" failure on not-yet-collected data,
which is the OTHER way this exact cycle's own headline claims went wrong.
A future standing rule (not proposed here, since one demonstrated failure
is not yet the two-or-three-instance pattern this program requires before
generalizing per its own R5/R6/R7 lineage) may eventually be warranted for
that second failure shape; for now it is enough that Phase 3 correctly
withdrew the claim it broke (docket item 3, accepted) without needing R7
to cover it.

## 6. Finding — `phase3_synthesis.md` §6's forward-looking cost/feasibility language carries no new unstated cost assumption

Checked §6's three named alternatives for a future seventh-class attempt
("a fully Bayesian treatment with an informative, independently-sourced
prior"; "a genuinely different estimator class"; "PHOTONICS' own queued
WKB/adiabatic boundary-reflectance analytic model, which requires no fit
or null at all"). **None of the three carries a new FDTD-call or
compute-cost figure** — §6 deliberately does not price any of them, which
is itself the correct lesson learned from this exact cycle's own
`~45→~90/180`-call citation error (§2 above): rather than repeat a
confident-but-wrong cost number for a not-yet-designed future test, §6
states only that each is "qualitatively different," with no cost claim to
verify or falsify. The one arguably cost-adjacent phrase — the WKB model
"requires no fit or null at all" — is not a new assumption invented this
cycle; it restates PLAN.md's own already-standing Iteration-50 queue
description of that candidate ("zero FDTD, genuinely new... zero data"),
carried forward accurately, not freshly asserted. **No new unstated cost
assumption found in §6.**

## 7. Finding — the official Phase-4 run is faithfully and completely reported

Independently re-ran `fit_and_calibrate.py` end-to-end (§0). Every
reported number in `phase4_results.md`'s "Bottom line" and "The real fit"
sections reproduces exactly, including the per-pair `R_q9`/`SE9`/`z9`/
`lev9_Rq`/`cond9` table (matching THERMODYNAMICS' and Red Team's
independent Phase-2 hand-fits to 3+ decimals, as those documents
themselves report) and the seed-determinism claim (fixed
`SIGN_FLIP_SEED=74051`/`CAL_SEED=74052`, unchanged from Phase 3). The
`scored={}` / no-pair-ever-scored claim is correct — `combined_verdict`
is set to the `HALT` branch before the `else` branch that would populate
`scored` ever executes (`fit_and_calibrate.py` lines 275–296). No
overclaim, no cherry-picked cell, no silent renormalization found.

---

## Verdict

**PARTIAL.**

The T28 differential/two-tone-fit sub-thread's own substantive mechanism
question (is C60–C70's real `z9=5.03` a genuine second contributor or
`cond9≈500`-driven overfitting?) is **exactly where it was after Phase 2**
— this cycle establishes *why* it cannot currently be resolved with this
instrument (both calibration legs badly miscalibrated, the circular-shift
leg far worse than i.i.d.), not a resolution either way. Per the
pre-committed §6 rule, the HALT result correctly and automatically
triggers formal retirement of the same-instrument-class approach (a
sign-flip/permutation null on this ramped-quadrature OLS basis) at any
window width — a real, citable closing bound, honestly earned this time
(unlike Phase 1's withdrawn CLOSURE-CONFIRM, which claimed the same
outcome on a method Phase 2 showed does not support it).

Independent of T28's own mechanism question, this cycle delivers genuine,
verifiable program-level progress from my seat's own verification pass:
a correctly-scoped new standing rule (R7, adopted without drift), the
`~45`-calls error correctly and permanently resolved with no residual
trace, clean idealization-carry-forward and zero smuggled `ABSORB`
realizability claims (the two things my charter is explicitly tasked with
policing), and a reusable, bit-for-bit-reproducible instrument
(`desk_check_pricing.py` + `fit_and_calibrate.py`) that the record itself
correctly declines to retire alongside the claims it was misused to
support in Phase 1. Against that: one new, independently-discovered,
non-load-bearing numeric-citation defect (§3, the "3.5×–5.9× at every α"
claim) that should be corrected before a third document inherits it, and
one real, named scope gap in R7 (§5) worth flagging for whoever next
writes a forward-looking feasibility forecast, though not yet warranting
its own standing rule.

Not RULED-OUT-worthy: the underlying instrument and R7 are real,
positive, reusable additions to the program regardless of T28's own fate.
Not PROMISING: no mechanism was found, confirmed, or newly opened this
cycle — the honest outcome is a correctly-earned closing bound on one
instrument class, not a lead on the phenomenon.

---

## Ranked top-3 candidate directions for Iteration 52 (MATERIALS' own ranking)

1. **PHOTONICS' WKB/adiabatic boundary-reflectance analytic model for the
   graded-loss `ABSORB` band** (PLAN.md queue item 4; queued and dropped
   without execution at Iterations 46 and 47). This is my seat's own
   top pick, not merely a deference to the existing near-unanimous
   ranking: it is the first candidate in six T28 cycles to ask what
   sub-wavelength structure — the graded-loss boundary's own admittance
   profile as a function of depth and angle — actually predicts, rather
   than re-auditing statistics on an instrument this cycle has now shown
   (twice, on two legs) cannot resolve the question. Zero FDTD, zero
   data, and it answers the realizability question directly: if the
   ~2.5° family is the ordinary reflectance-phase signature of ANY
   graded-loss boundary of comparable depth, that is a **published**
   result (ordinary boundary electromagnetics, no exotic material
   needed) and closes T28's mechanism question outright; if it requires a
   depth/loss-profile combination outside what an ordinary PML-like
   graded absorber produces, that is itself informative — the first real
   evidence bearing on my charter's realizability bound for this specific
   phenomenon, rather than a statement about an OLS design matrix.

2. **`G40`/`PAD` decorrelation** (~31 FDTD calls, per my own seat's
   already-verified geometry-reuse claim against
   `experiments/065-.../design_geometry_output.txt`). Until `ABSORB` and
   `PAD` are decorrelated, no future finding on this thread can be
   attributed to a real material/geometric parameter (absorption depth)
   at all, since the causal variable is still confounded with a purely
   numerical one (domain-padding distance) — exactly the class of
   confound my charter exists to catch before any realizability
   statement is made. Cheapest remaining FDTD relief on the board,
   orthogonal to items 1 and 3.

3. **Two cheap record-hygiene corrections, bundled as a single
   near-zero-cost action before further T28 spend**: (a) correct the
   "3.5×–5.9× at every α" mis-citation this review independently found
   (§3, above) in `phase4_results.md`/`NOTES.md`, before a Phase-5 seat
   or a future cycle inherits it as ground truth; (b) finally correct the
   three-document-old "house precedent, Iteration 5, exp-027" mislabel
   (THERMODYNAMICS' Phase-2 finding this cycle, ruled correctly
   out-of-scope for exp-074 itself but still uncorrected in the record).
   Neither relieves a physical confound or advances the mechanism
   question, but both are on this exact sub-thread's own critical path
   for trustworthiness, cost nothing, and — per this program's own R4
   history — get more expensive to fix the longer they sit uncorrected
   across further documents.
