# PHASE 2 — RED TEAM AUDIT · Panel Iteration 51 · exp-074
## "Price the window": Cramér–Rao/conditioning + `L(T)` leakage — closure claim adjudicated

*Fresh sub-agent, RED TEAM charter (PANEL.md: attacks every proposal, speaks
last and hardest; standard is not textbook-physics compliance — it kills
internal inconsistency, unfalsifiable claims, mechanisms inexpressible as
simulation parameters, and quiet constraint-N violations, especially #3).
Receives everything: `phase1_proposal.md`, `desk_check_pricing.py` +
results, and all five blind Phase-2 critiques (PHOTONICS, MATERIALS,
THERMODYNAMICS, QUANTUM, VISION). Every load-bearing claim below —
including every claim made **by** the five critiques — was independently
re-derived by invoking or extending the actual committed code, not taken
on any seat's word (LOGBOOK R4).*

---

## 0. What I ran

All commands below were executed against the unmodified committed
`desk_check_pricing.py` and its own functions, or short extensions of it
(scratch scripts, not committed — the committed script itself needed no
change to expose every defect below):

1. `python3 desk_check_pricing.py` — reproduces `desk_check_pricing_results.json`
   bit-for-bit. `CHECK0 pass=True worst_rel_err=0.00e+00`. Confirms every
   seat's own baseline reproduction claim; the underlying numbers in
   `phase1_proposal.md` §2b–2f are real, not hand-typed.
2. A contaminant-period scan, `T ∈ [1.8°, 5.0°]` step 0.1°, calling
   `price_pair(..., T_fringe_deg=T)` unmodified at all four pairs, scoring
   the exact pre-registered CLOSURE-CONFIRM predicate
   (`cond9≥300 ∧ VIF_Rq≥15 ∧ z_joint_optimistic<1.5`, all 4 pairs) —
   PHOTONICS' attack, independently re-run.
3. A direct fit of the real, committed 9-column `X9` to real `delta_ab`
   data at all four pairs (`coef9 = pinv(X9) @ delta_ab`, real residuals,
   real `z9`) — THERMODYNAMICS' attack, independently re-run.
4. The actual, currently-committed exp-072 `results.json` bootstrap/OLS
   `SE_Rq` ratios (not the superseded Phase-5-draft figures either
   Phase-5 review of exp-072 quoted), chained onto the 51° `z_joint`
   figures — QUANTUM's attack, independently re-run and re-sourced.
5. Direct arithmetic on the θ-grid point counts at each widened-window
   candidate in `WIDENED_CANDIDATES` — MATERIALS' cost-citation attack.
6. A curvature-augmented design (`X6`/`X10`, the disclosed-but-unfitted
   6th column) at baseline, to check PHOTONICS' steel-man claim that it
   is not load-bearing.
7. A textual/logical audit of §5's five gate formulas against the
   document's own citations — VISION's attack.

Every one of the five critiques' central computational claims reproduced
independently, to the precision each critique itself reported. None was
taken on say-so.

---

## 1. Adjudication of PHOTONICS' attack — CONFIRMED, in full, strengthened

**Claim:** CLOSURE-CONFIRM and §6's "independent of which null eventually
gates it" language are false — scanning the assumed contaminant period
across `L(T)`'s own claimed danger band (1.8°–5.0°) breaks the closure
result starting around 3.6°–3.7°.

**My independent re-run** (identical script, `T_fringe_deg` swept, all four
pairs, exact pre-registered predicate):

| T (deg) | min VIF_Rq | max z_joint(opt.) | min cond9 | CLOSURE-CONFIRM holds (all 4 pairs)? |
|---|---|---|---|---|
| 1.9608 (proposal's choice) | 31.1 | 0.81 | 478 | **YES** |
| 3.60 | 15.4 | 1.25 | 644 | YES (barely — `VIF` is 3% above its own 15 floor) |
| 3.70 | 13.0 | 1.36 | 610 | **NO** |
| 4.00 | 8.9 | 1.64 | 551 | **NO** — `z_joint` exceeds the 1.5 "closed" ceiling |
| 4.60 | 5.8 | 2.03 | 524 | **NO** — clears 2σ itself, in the *current, unwidened* window |
| 5.00 | 5.0 | 2.20 | 537 | **NO** |

Confirmed to the last significant figure against PHOTONICS' own table. I
also independently reproduced the mechanism claim: `L(T)` (leakage into an
*unmodeled* contaminant) and `VIF_Rq`/`cond9` (collinearity when that same
contaminant is *modeled*) are different linear-algebra objects and do not
covary monotonically — my own scan additionally surfaces a region
(`T≈2.0°–2.5°`, near-degeneracy with the primary carrier's own `T_x≈2.49°`)
where `VIF` explodes to `10²–10⁸` for an unrelated reason (near-collinearity
with the *carrier itself*, not a genuine second contaminant), which is a
useful additional caution PHOTONICS did not need for its argument but which
independently corroborates that this design's conditioning surface is
highly non-monotonic and any single-`T` calculation is fragile evidence for
a program-wide claim.

**Verdict on this attack: CONFIRMED, no override.** Idealization 4 already
named the gap in one sentence; §6's binding prose does not carry the hedge
forward. This is a real **[inconsistency]** between the document's own
Idealization 4 and its own §6 decision-rule language, not a new physics
claim PHOTONICS invented.

---

## 2. Adjudication of THERMODYNAMICS' attack — CONFIRMED, in full, mechanism identified

**Claim:** actually fitting the real 9-column design to real `delta_ab`
data gives a true `z9` that exceeds the "optimistic upper bound"
`z_joint_optimistic` at 3 of 4 pairs, by up to 9.3× at C60–C70.

**My independent re-fit** (`coef9 = pinv(X9) @ delta_ab`, real `resid9`,
real `SE9`, all four pairs, baseline window):

| Pair | `z_ols` (5-col) | `z_joint` (optimistic) | `z9` (real fit, mine) | `RSS9/RSS5` |
|---|---|---|---|---|
| C40–C60 | 4.904 | 0.811 | **0.843** | 0.501 |
| C60–C70 | 3.037 | 0.540 | **5.033** | 0.193 |
| C70–C80 | 4.254 | 0.762 | **1.634** | 0.059 |
| C40–C80 | 4.657 | 0.775 | **0.345** | 0.345 |

Matches THERMODYNAMICS' table to three decimal places. At C60–C70 the real
`z9=5.03` doesn't just beat the `1.5` "closed" ceiling — it beats the
**properly-sourced 2σ bar itself**, in the *baseline, unwidened* window.

**I went one step further and identified the structural reason** (not just
confirmed the number): with `cond9≈480–530` and only `n−p9=22` residual
degrees of freedom, the four added, highly-correlated columns can absorb
real sum-of-squares from `delta_ab` far faster than the `(n−p)` bookkeeping
alone predicts (`RSS9/RSS5` as low as 0.06–0.50). `z_joint_optimistic`'s
entire validity rests on Idealization 6's claim that the two-tone fit
"cannot do better than [the naive extrapolation] even in principle" — that
claim is **false as a matter of linear algebra**, not merely unlucky: a
collinear design's realized residual variance is not bounded below by a
VIF-only rescaling of the single-carrier residual variance. This is the
single most important finding in the whole cycle, because it invalidates
the *epistemic method* (pricing the Gram matrix without ever fitting)
independent of whether C60–C70's `z9=5.03` reflects a real second
contributor or `cond9≈500`-driven overfitting — which is exactly the
open question THERMODYNAMICS itself named and correctly declined to
resolve without a null-calibration test.

**Verdict on this attack: CONFIRMED, no override, and elevated** to a
program-level methodological finding (§5 below), because the same defect
shape (a conditioning-based bound presented as decisive without ever
fitting the actual design) is exactly the kind of "look-elsewhere"
failure R5's addendum and R6 already exist to police in adjacent
instrument classes, per LOGBOOK's own generalization pattern.

---

## 3. Adjudication of QUANTUM's attack — CONFIRMED, in full, and independently STRENGTHENED

**Claim:** the 51°-window "4/4 pairs clear 2σ" figure never applies the
naive-OLS-vs-design-respecting-bootstrap SE-inflation this exact record
(exp-072 Phase-5) already established (QUANTUM cited 1.56–4.70×); applying
even the smallest factor drops the pass count to as few as 1/4.

**Provenance check, before reusing QUANTUM's numbers:** QUANTUM's cited
1.56–2.31× figures trace to **its own predecessor's** exp-072 Phase-5
review (`phase5_review_quantum.md` D4, a residual-bootstrap variant), and
the 2.27–4.70× figures trace to **EM's** exp-072 Phase-5 review
(`phase5_review_em.md` D3, a different residual-bootstrap variant) — two
different Phase-5 reviews of the *same* cycle, computing two different
numbers for a nominally similar quantity, neither of which is what
actually ended up in the currently-committed `exp-072/results.json`.
I recomputed the **real, currently-committed, final** bootstrap/OLS ratio
directly from that file:

| Pair | `SE_Rq_ols` | `SE_Rq_bootstrap` (committed) | ratio |
|---|---|---|---|
| C40–C60 | 0.005616 | 0.012303 | **2.19×** |
| C60–C70 | 0.001161 | 0.005136 | **4.42×** |
| C70–C80 | 0.000833 | 0.002482 | **2.98×** |
| C40–C80 | 0.005622 | 0.016507 | **2.94×** |

Chaining these — the record's actual, current, authoritative figures, not
either superseded Phase-5 draft — onto the reported 51°-window `z_joint`
values (dividing by the median VIF-based `SE_inflation=1.20`, then by the
pair's own real bootstrap ratio):

| Pair | `z_ols` | `z_joint`@51° (VIF-only) | ÷ real bootstrap ratio | clears 2σ? |
|---|---|---|---|---|
| C40–C60 | 4.90 | 4.09 | **1.87** | No |
| C60–C70 | 3.04 | 2.53 | **0.57** | No |
| C70–C80 | 4.25 | 3.55 | **1.19** | No |
| C40–C80 | 4.66 | 3.88 | **1.32** | No |

**0 of 4 pairs clear 2σ** — worse than QUANTUM's own conservative estimate
of "as few as 1/4." The WIDENED-WINDOW-LICENSES-FURTHER-SPEND finding does
not survive at all once the record's own already-published, already-final
SE correction is applied honestly.

**Verdict on this attack: CONFIRMED and strengthened.** I note, but do not
treat as load-bearing against QUANTUM's verdict, the citation-provenance
issue (QUANTUM cited a superseded draft number rather than the final
committed one) — the qualitative conclusion QUANTUM reached is *right* and
if anything undersold; flagged in the docket (§6, item 9) as its own small
R4-shaped correction, since a wrong number attached to a correct
conclusion is still the pattern R4 exists to police.

---

## 4. Adjudication of MATERIALS' attack — CONFIRMED, exact arithmetic

**Claim:** §6/§7's "≈45 new FDTD calls for a two-config extension" at 51°
is a 4× understatement; the real cost is ~90 calls (2-config) or ~180
calls (4-config, actually needed to score all four pairs as §5's own
tables do).

**Independent check**, directly from the committed script's own window
grids: baseline (36–42°) has 31 points; the 51° candidate has 76 points
(`theta_max_51.0.n=76` in `desk_check_pricing_results.json`). New points =
76−31 = **45 points per config**, not 45 calls. A two-config (C40/C80)
extension is therefore 45×2 = **90 calls**; scoring all four pairs (the
only way to reproduce §5's own four-pair CLOSURE-CONFIRM/WIDENED-WINDOW
tables) requires all four configs extended: 45×4 = **180 calls**. I also
checked the citation EM's own §6.2 costing is drawn from — the 46°
candidate (`n=51`, 51−31=20 new points/config, 20×2=40 calls) — and that
figure is EM's own correct, self-consistent number *for the 46° window*.
The exp-074 proposal took EM's per-config figure for a **different, closer**
window and mis-cited it as the total-call figure for a **different,
farther** window.

**Verdict on this attack: CONFIRMED, no override.** This is now doubly
moot given §3 above already withdraws the recommendation this cost figure
was meant to justify, but it must still be corrected in the record per R4,
since some future cycle could resurrect the widened-window idea on
narrower, more defensible grounds and inherit the wrong cost.

---

## 5. Adjudication of VISION's attack — CONFIRMED (textual), correctly scoped as non-load-bearing at original margins, now potentially load-bearing

**Claim:** three of five §5 bars (`cond9≥300`, `VIF_Rq≥15`, `lev_ratio≥0.90`)
are asserted, not derived from any stated formula connecting them to an
achieved error rate; only the `z_joint<1.5`/`≥2.0` bars are properly
sourced (to EM's own exp-072 2σ statement).

**Independent textual audit:** confirmed. §0 cites "the `cond≤100`/
`(n−p)/n` machinery already standing in `run.py`" as the source for
`cond9≥300`, but `run.py`'s own `ill_conditioned = cond5 > 100.0` gate is
stated for the **5-column** design; no formula anywhere in `phase1_proposal.md`
or `desk_check_pricing.py` scales that to a **9-column** design's condition
number (an implicit ×3, never named as such, let alone justified from
first principles — e.g. from an actual achieved-variance-inflation
argument). `VIF_Rq≥15` and `lev_ratio≥0.90` similarly have no stated link
to a false-negative/false-positive rate. VISION is also correct that this
is exactly the "see the answer, then set a comfortable bar" shape R5/R6
exist to police for *stochastic* thresholds, softened only by §0's
(defensible, but merely argued, not gated) claim that a deterministic
instrument-pricing calculation is a different category.

**Where I diverge from VISION's own scoping:** VISION judged this
non-load-bearing because the observed baseline margins (`z_joint=0.81` at
worst) were wide relative to the properly-sourced `2.0` bar alone. That
judgment was correct **at the time VISION wrote it, blind to the other
four critiques**. Once §§1–3 above are applied, the entire premise
VISION's "not load-bearing" conclusion depended on — that CLOSURE-CONFIRM
and the 51° recommendation are decisively true and only these three
cosmetic bars are undischarged — no longer holds. I do not fault VISION
for this: its charter is bar-sourcing, and blind-Phase-2 protocol forbids
it from seeing PHOTONICS'/THERMODYNAMICS'/QUANTUM's attacks. But Phase 3
must not read VISION's "non-load-bearing" verdict as still applying once
the headline claims it was scoped against are withdrawn.

**Verdict on this attack: CONFIRMED**, scope-corrected as above (**not an
override of VISION's finding — an update of its situational premise**,
which VISION structurally could not have had).

---

## 6. A sixth attack, mine, not present in any of the five blind critiques

**[inconsistency] The proposal's own stated epistemic method — price the
design's Gram-matrix conditioning, never fit it — cannot, in principle,
certify a null result, and §2's finding shows it can be actively
misleading in either direction.** `desk_check_pricing.py`'s own docstring
states it "does NOT run a null-calibration test itself... it prices the
DESIGN's own information content, which is a precondition for any null
being calibratable." That framing is careful and correct as a *necessary*
condition — the proposal never overclaims sufficiency in its own code
comments. But §5/§6's prose does overclaim sufficiency: CLOSURE-CONFIRM is
presented as answering "can *any* correctly-calibrated null ever work
here" without ever fitting the model the null would be calibrated against.
§2 above shows this is not a hypothetical risk: the real fit's residual
variance can shrink far more than VIF-only scaling predicts under
`cond9≈500`, so a conditioning-only bound is not a valid substitute for
actually fitting plus null-calibrating — in **either** direction (it could
equally have hidden a real detection or manufactured a false one; C60–C70
is a live instance of the former possibility, unresolved without a null
test).

This is the same failure *shape*, in a new instrument class, as two
already-generalized house rules:
- **R5's addendum** (Iteration 47): a raw deviation/match, however tight,
  is not evidence without a null-permutation control.
- **R6, generalized** (Iteration 50): any significance claim needs its own
  calibration, not just point-estimate machinery.

**Recommended new standing rule (candidate "R7," Phase 3's to name and
adopt or reject):** *A conditioning/VIF-based "pricing" of an un-fit
multi-tone or multi-parameter design must not be treated as a decisive
substitute for actually fitting that design to real data and running a
null-calibration test on the fit — collinearity can make the realized
standard error either larger OR smaller than a naive Gram-matrix-only
extrapolation predicts, so a design-only bound is necessary, not
sufficient, evidence for either a closure or a detection claim.* This
generalizes R6 one level further upstream: R6 already requires a
null-calibration test before a *fitted* coefficient's significance is
trusted; this closes the loophole of never fitting the coefficient at all
and pricing the design instead, then treating that price as if it were
the fit's own calibrated significance.

---

## 7. What survives — the underlying machinery is sound and should be kept

Every one of the five critiques independently reached this same
conclusion, and my own re-runs confirm it structurally: the **defect is in
the interpretive claims of §5/§6, not in the instrument.**

**Confirmed sound, reusable, keep as-is:**
- `check0_basis_identity()` — real, byte-exact, machine-precision agreement
  with exp-072's committed basis. The single best piece of house
  discipline in this cycle.
- `carrier_fit`/`design_matrix`/`tone_cols` — verified byte-identical to
  exp-073's committed `run.py` (independently diffed by three of five
  critics; I re-confirmed on the two functions most load-bearing to my
  own re-fits).
- `cond5`/`cond9`/`VIF_Rq`/`SE_inflation` computation — correct linear
  algebra, correctly generalized from EM's one-pair exp-072 Phase-5 note
  to all four pairs.
- `lev_ratio` and its connection to `mean diag(M5)=(n−p)/n` — a genuine,
  correct generalization of exp-073's own `G0-e(ii)` mechanism; the exact
  quantity driving that gate's anti-conservatism is now expressed as a
  reusable design-time function, at every window width, not just the one
  exp-073 measured on real data.
- `L(T)` leakage function — correctly, completely re-derived from its
  original exp-072 Phase-5 definition (confirmed independently by QUANTUM
  and by me); its own table is what exposed §6's overreach (PHOTONICS'
  attack used it directly), which is a point in its favor, not against it.
- The widened-window phase-sweep discipline (8×8, min/median/max, not a
  cherry-picked phase; `cond5` asserted and verified phase-invariant
  in-script) — the right robustness posture for a data-free extrapolation.
- The curvature-column caveat (Idealization 7) is real but, checked
  independently (§0.6 above), not decisive on its own: adding it moves
  `VIF_Rq` by only ~1.0–1.2× at baseline. It remains a live caveat for any
  future *widened-window* run (curvature grows with window width, per the
  proposal's own §2e reasoning) but is not what breaks CLOSURE-CONFIRM —
  PHOTONICS' and THERMODYNAMICS' attacks are what break it.

**Does not survive, withdraw or rewrite:**
- §5 CLOSURE-CONFIRM (baseline window) — not decisively established
  either way; correct status is **NOT_EVALUABLE pending an actual
  null-calibrated 9-column fit**, not CONFIRM.
- §5 WIDENED-WINDOW-LICENSES-FURTHER-SPEND (~51°) — REFUTED by the
  record's own already-published SE correction (0/4, not 4/4, clear 2σ).
  No FDTD spend should be authorized on this basis.
- §6's binding, program-wide formal-retirement decision rule — withdrawn
  as written; it rests on both §5 claims above.
- §7's "≈45 calls" cost estimate for the (now-moot, but still
  record-corrupting-if-uncorrected) widened-window proposal.

---

## 8. Checkpoint check

**Criterion 4 (program-integrity drift) does NOT fire this cycle** — this
is the R6/exp-073-`HALT_NULL_MISCALIBRATED` shape, not the Iteration-50
sign-error shape: two of five blind Phase-2 critics caught the defect
*before* Phase 3 synthesis, by two independent methods, and Red Team
(this audit) confirms both computationally before any of it reaches
LOGBOOK.md or PLAN.md. The house discipline worked as designed, at the
earliest possible gate. **This finding is conditional**: if Phase 3 adopts
§6 as originally written — over two blind Phase-2 oppose verdicts and
this Red Team audit's independent confirmation of both — that specific
act would fire Checkpoint criterion 4 retroactively, matching this
program's own Iteration-50 precedent exactly (a claim defended rather
than re-derived against contradicting evidence already on the table).

**Criterion 5 (two consecutive non-advancing iterations) does NOT fire.**
This cycle delivers genuine narrowing even after §5/§6 are withdrawn: a
new, generalizable standing-rule candidate (§6 above), a corrected and
much cheaper concrete next test (§9 below), and a materially strengthened
understanding of exactly why conditioning-only pricing cannot substitute
for a fit — itself a real, citable methodological result for the program,
independent of T28's own mechanism question.

---

## 9. Numbered docket for Phase 3 (mandatory)

1. **[inconsistency]** Withdraw §5's CLOSURE-CONFIRM verdict and §6's
   "independent of which null eventually gates it" language for the
   36°–42° baseline window. Confirmed: the same committed script, scanning
   the contaminant period across `L(T)`'s own claimed 1.8°–5.0° danger
   band, fails the CLOSURE-CONFIRM predicate from `T≈3.7°` onward, and
   `z_joint` clears 2σ itself at `T≈4.6°–5.0°`, in this same unwidened
   window (PHOTONICS, confirmed §1).
2. **[inconsistency]** Withdraw Idealization 6's "cannot do better than
   [the optimistic bound] even in principle" claim. Confirmed false by an
   actual fit of the committed `X9` to real `delta_ab`: true `z9` exceeds
   `z_joint_optimistic` at 3 of 4 pairs, by up to 9.3× at C60–C70, itself
   clearing the properly-sourced 2σ bar in the *baseline* window
   (THERMODYNAMICS, confirmed and mechanistically explained, §2).
3. **[inconsistency]** Withdraw or heavily caveat §5's WIDENED-WINDOW-
   LICENSES-FURTHER-SPEND finding (~51°, "4/4 clear 2σ"). Confirmed: using
   the record's own currently-committed (not superseded-draft) bootstrap/
   OLS SE-inflation ratios, 0 of 4 pairs clear 2σ at 51° (QUANTUM,
   confirmed and strengthened, §3). No FDTD spend should be authorized on
   this recommendation as written.
4. **[process]** Correct the ~51°-window FDTD cost citation: the real
   figure is ~90 calls (2-config preliminary check) or ~180 calls
   (4-config, needed to actually populate all four pairs' worth of §5's
   own tables), not "≈45" (MATERIALS, confirmed, §4).
5. **[process]** Either derive `cond9≥300`, `VIF_Rq≥15`, and
   `lev_ratio≥0.90` from a stated formula linking them to an achieved
   error rate, or explicitly relabel them as precedent-anchored heuristic
   margins in any successor document — not first-principles bars (VISION,
   confirmed, §5). Given items 1–3, these bars can no longer be assumed
   non-load-bearing by default in a future cycle; they must be justified
   or dropped before reuse.
6. **[new standing rule, Phase 3/Director to adopt or reject explicitly]**
   Generalize R6 one level further upstream (candidate name "R7," per §6
   above): a conditioning/VIF-based pricing of an *un-fit* multi-tone
   design is necessary, not sufficient, evidence for a closure or
   detection claim; the design must actually be fit to real data and
   null-calibrated before either verdict is drawn.
7. **[concrete next step, zero new FDTD, cheapest available]** Before any
   widened-window spend is even considered: run the actual 9-column
   two-tone fit (already written, in this audit's own scratch extension of
   the committed script, ~20 lines) on the **current** 36°–42° real data,
   with a proper null-calibration test on the second tone's phase/
   coefficient (sign-flip or permutation, matching R6/`G0-e(ii)`'s own
   standard) — to determine whether C60–C70's `z9=5.03` is a real second
   contributor or `cond9≈500`-driven overfitting. This is the single
   highest-information, lowest-cost action available to the program right
   now on this sub-thread.
8. **[house-discipline, binding per PLAN.md queue item 5]** Restate, in
   writing, the "sixth non-advancing cycle" decision rule PLAN.md already
   required Iteration 51 to state: with this audit's overrides applied,
   Iterations 46–51 are now six consecutive non-decisive T28
   differential/two-tone cycles. Phase 3 must state explicitly what a
   **seventh** non-decisive cycle — after item 7's cheap null-calibration
   test is actually run at the current window — would mean, matching the
   Block-MINI precedent (a formal, pre-committed non-decisive-outcome
   trigger), rather than let the requirement lapse a second time on a
   decision rule (§6, this proposal) that turned out to rest on false
   premises.
9. **[R4-shaped, minor, non-outcome-determining]** Two small citation
   corrections for the record: (a) QUANTUM's exp-074 critique cited a
   superseded pre-final-audit Phase-5 draft bootstrap-ratio range
   (1.56–4.70×) rather than the currently-committed `exp-072/results.json`
   figures (2.19–4.42×) — the qualitative conclusion is unaffected and, as
   shown in §3, actually strengthened, but the citation should point to
   the final number the next time this is written up; (b) §2f's claim
   that the ≈4–5% gap between this cycle's `L(1.9608°)` figures and
   QUANTUM's exp-072 predecessor's is due to "a slightly different...
   second-tone phase convention" is wrong (`L(T)` never references a
   second tone) — the real cause, independently confirmed by QUANTUM this
   cycle, is corrected (exp-073) vs. uncorrected (exp-072) primary-carrier
   sign convention.
10. **[disclosed, out-of-scope, not chargeable to this cycle]**
    THERMODYNAMICS flagged a three-document-old mislabeled "house
    precedent, Iteration 5, exp-027" citation (exp-027 is actually
    Iteration 4, per LOGBOOK.md's own section headers) living in
    exp-072's Phase-2 critique, Red Team audit, and Phase-5 materials
    review. exp-074 does not repeat the error and is not required to fix
    it, but the next cycle that touches any of those three documents
    should.

---

## 10. My own recommendation for this cycle's Combined Verdict

**Overall Red Team verdict: PROCEED-WITH-MANDATORY-FIXES.** The instrument
is real, correctly engineered, and worth keeping; the two headline claims
built on top of it (§5's CLOSURE-CONFIRM, §6's formal-retirement decision
rule) are independently falsified, by two different methods, both
confirmed here by a third. Phase 3 may not adopt §5/§6 as written under
any circumstances — doing so would fire Checkpoint criterion 4
retroactively (§8).

**What I recommend the Combined Verdict actually state, once Phase 3
resolves the docket:**

- **CLOSURE-CONFIRM (baseline, 36°–42°): OVERRIDDEN → `NOT_EVALUABLE`.**
  Neither closed nor open on the evidence in hand; a real fit exists
  (`z9`) but is not null-calibrated, so it cannot be scored either way
  without docket item 7.
- **WIDENED-WINDOW-LICENSES-FURTHER-SPEND (~51°): OVERRIDDEN →
  `REFUTED`.** 0/4 pairs clear 2σ under the record's own established SE
  correction. Do not authorize the 90–180-call FDTD extension on this
  basis.
- **INTERMEDIATE (~46°): unchanged, `NEITHER`** — this band's own
  pre-registered predicate was already "neither of the other two bands,"
  and both of those now fail even more clearly, so 46° remains
  uninformative by construction, not newly so.
- **§6 pre-committed decision rule: WITHDRAWN**, replaced by docket items
  6–8 (a new standing rule, a concrete next test, and a corrected
  seventh-cycle framing).
- **The underlying instrument (`CHECK0`, `cond5`/`cond9`/`VIF_Rq`,
  `lev_ratio`, `L(T)`, the widened-window phase-sweep code): CONFIRMED,
  KEEP**, retasked toward docket item 7 rather than retired alongside the
  claims it was misused to support.
- **T28 program status: this is the sixth consecutive non-decisive cycle
  on the differential/two-tone sub-thread** (Iterations 46–51), but one
  that delivers real narrowing (a new generalized house rule; a corrected,
  far cheaper concrete next step; the closure question re-opened on
  defensible terms rather than false ones). Not a "no logbook-advancing
  result" cycle under PANEL.md's own stop-condition language —
  Checkpoint criterion 5 does not fire — but the program is now obligated,
  in writing (docket item 8), to state what a seventh non-decisive cycle
  would mean, since this cycle's own attempt to discharge that obligation
  rested on premises this audit overrides.

**Bottom line for the Director:** ship the machinery, not the claims.
Everything in `desk_check_pricing.py` earns its place in the record.
Nothing in §5 or §6 does, as written.
