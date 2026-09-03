# PHASE 2 — RED TEAM AUDIT · Panel Iteration 84 (candidate exp-107)
## "The Properly-Powered R5 Census, a Ground-Truth Recovery Gate, and Three Zero/Low-Marginal-Cost `kappa_window` Closeouts"

*Red Team seat, fresh context, receives everything: `phase1_proposal.md`
and all five blind Phase-2 critiques
(`phase2_critique_{photonics,materials,em,thermodynamics,quantum}.md`),
plus the mandatory-reading set (LOGBOOK.md in full — RULED OUT R1–R24,
ESTABLISHED, LIVE THREADS T1/T28's full history including the
`delta_scene` R3/R4/R5 sub-thread; PANEL.md; PLAN.md's Current state;
exp-106's `NOTES.md`/`phase5_redteam_audit.md`; exp-100's `NOTES.md`/
`disposition_memo.md`; exp-052's `design_geometry.py`; `lab/sections.py`;
`lab/thermo_sidecar.py`). Every numeric claim below that mattered to the
verdict was independently re-derived, not taken on any critique's word —
see §0.*

---

## 0. Independent re-verification from primitives

**0.1 QUANTUM's anchor-impossibility claim — re-derived from scratch,
CONFIRMED exactly, then generalized.**

```
crossings = [37.127246, 38.590230, 40.265420, 41.460901]   # exp-083, LOGBOOK
buf = 1.4
gaps = [1.462984, 1.675190, 1.195481]           # all < 2*buf = 2.8
exclusion intervals = [(35.727246, 38.527246), (37.190230, 39.990230),
                        (38.865420, 41.665420), (40.060901, 42.860901)]
merged union = (35.727246, 42.860901)           # continuous, width 7.134°
proposed grid = [36.0, 42.0], step 0.2          # 31 points
angles clearing the buffer from all 4 crossings: NONE (0 of 31)
```

Confirmed independently, digit-for-digit against the proposal's own §2
cited crossing values: the four exclusion intervals are pairwise
overlapping (each gap between consecutive crossings is smaller than
`2×1.4°`), so they merge into one continuous forbidden band
`[35.727°, 42.861°]` that fully contains the proposed `[36.0°, 42.0°]`
grid. **Zero of 31 grid points can serve as `θ_anchor`. Gate G0 has no
candidate to evaluate before any FDTD call runs.** QUANTUM's finding is
correct in every particular.

**0.2 Generalizing QUANTUM's finding: this is not a local defect of the
`[36°,42°]` window — the rule is close to globally unsatisfiable, because
the buffer (`≥1.4°`, "half the established 2.84–2.95° period") is itself
approximately half the period being tested.** Extending the crossing
lattice periodically in both directions (using each of the two live,
disputed period candidates on file, `P_edge_A=2.8421°` and `P*=2.9474°`)
and recomputing the same `±1.4°` exclusion union:

```
P=2.8421°: sliver width between consecutive exclusion zones = 0.0421°  (every period)
P=2.9474°: sliver width between consecutive exclusion zones = 0.1474°  (every period)
```

Both slivers are narrower than the proposed grid's own `0.2°` step. **A
buffer sized to half the period of a periodic signal, applied to a
lattice of crossings recurring at that period, structurally leaves almost
no angle anywhere on the real line clear of every crossing — this is a
property of the rule's own arithmetic (buffer ≈ half-period), not an
accident of where `[36°,42°]` happens to sit.** Widening or re-centering
the census window does not fix this; it only relocates which sliver (if
any) a coarse `0.2°`-step grid might get lucky enough to land inside. This
generalizes QUANTUM's local finding into a structural indictment of the
selection rule itself. (§1, Attack 2, below.)

**0.3 Testing QUANTUM's own proposed rescue** ("redefine clause (b) to
'the grid angle maximizing distance-to-nearest-crossing'"): computed the
actual best-achievable point on the proposed 31-point grid.

```
midpoint of the largest interior gap (38.590230°, 40.265420°) = 39.42773°,
  theoretical best margin = 0.8376°
best ON-GRID (0.2° step) point: θ=39.4°, margin = min(|39.4-38.590230|,
  |39.4-40.265420|) = 0.8098°  (next-best: θ=39.6°, margin=0.6654°)
```

This confirms QUANTUM's own claim that a repaired rule can find *a*
candidate, and that `0.81°` clears the established `~0.19°–0.38°`
cross-resolution crossing-shift magnitude R17 already put on file (a
real, relevant comparison). **But this candidate sits at θ≈39.2°–39.4°
— precisely the interval LOGBOOK's own record (Iteration 72, exp-095)
already found is NOT a clean "robust, far-from-null" point.** Exp-095's
own Phase-2/Red-Team layer tested control angles 39.2°/39.8° for exactly
this purpose (a robust ground-truth-sign anchor for the R4 family),
found 39.8° compromised, corrected to 39.2°/39.4°, and then found — at
Red Team's own Phase-2 audit, checked against the *full* six-crossing
null set, not just the nearest one — that 39.2° itself sits only 0.610°
from a genuine null, and that the "obvious" further fix (39.0°/39.4°)
was **not uniformly safe either** ("39.0° remained nearly as compromised
as the original 39.8°"). The best achievable point under QUANTUM's own
repaired rule is not a fresh, independently-robust anchor — it is the
same fragile neighborhood this program has already, on the record,
struggled to find a genuinely safe point inside. See §1, Attack 3.

**0.4 PHOTONICS' commensurability claim — re-derived independently,
CONFIRMED, with the exact discrepancy factor computed.**

```
peak = 3.1495e-3   (exp-100 Tier-2 Leg A / exp-095, θ=39.2°, R4/cpl=40)
C_thr_lab = 0.005
peak / C_thr_lab = 0.6299   →  63.0% of the bar
proposal's cited figure: 0.08–0.12×
discrepancy: 0.6299/0.12 = 5.25×   ...   0.6299/0.08 = 7.87×
```

Confirmed: the proposal's own §1 central safety sentence ("`delta_scene`'s
established magnitude, R9-corrected, is ≈0.08–0.12× ... C_thr=0.005") cites
T16/R9's `amp_ratio`-normalized, fitted-sinusoid figure for a **different
measurement construction** — `PAIR_PAD`/`PAIR_ABSORB40` (exp-076/077's
G40/PAD-decorrelation build) — not `delta_scene`'s own raw peak on the
36°–43° window this census extends. The directly on-point precedent,
already sitting in this cycle's own cited source pool (`experiments/100-
t28-delta-scene-constraint-scoring-pass/NOTES.md`, Tier-2 Leg A, which I
independently re-read and confirmed states exactly this number), computed
the raw peak against the identical `C_thr_lab` and got **63% of the bar**,
a **5.25×–7.87× discrepancy** ("~5–6×" in PHOTONICS' critique is a fair,
slightly conservative characterization). This is an R9-shaped
commensurability defect (two operands of nominally the same signal,
normalized differently, treated as interchangeable) sitting in the
Phase-1 proposal's own governing narrative — not merely a critique's
finding, a defect this document's own author should have caught applying
this program's own standing rule to its own text. It does **not** reverse
exp-100's own PASS verdict (63% is still `<100%` of the bar either way),
but it materially weakens the "no verdict is at risk either way, whichever
family is right" framing this proposal leans on to justify treating the
census as low-stakes housekeeping.

**0.5 MATERIALS' ceiling claim — independently re-read from
`disposition_memo.md` at the source, CONFIRMED unconditional.** The
memo's own text: *"Under NO branch of this memo's own per-outcome
conditional does a genuine new realizability question ever open."* Branch
(i) "no tier applies"; branch (ii), even the strongest possible
confirmed-coupling case, "published, no new material or structure
required"; branch (iii) "disposition deferred, no realizability claim
made." This is exhaustive over the three-way outcome space the census
itself also uses (R3-CORROBORATED / R4-CORROBORATED / NEITHER) — every
one of the census's own possible outcomes maps onto a branch this memo
already closed, at zero cost, one cycle ago. Independently confirmed, not
merely trusted from MATERIALS' critique.

**0.6 EM's "shared systematic" claim — independently confirmed against
LOGBOOK's own R15/exp-076 record.** `PAD` is proven lossless vacuum
(Iteration 53, exp-076 — the graded-loss damping array is a pure function
of `absorb` alone, zero dependence on `pad`/`nx`/`ny`) and R3/R4/R5 are
explicitly, textually "one mechanical recipe" (Idealization 17, carried
in every cycle since exp-094) — confirming EM's claim that all three
resolution families share the identical `ABSORB=40/PAD=40` boundary
construction and PML/truncation environment on a signal independently
proven to carry zero absorbed-power content. Agreement among three
non-independent measurements of a shared-systematic-prone signal is
weaker evidence of "real diffraction, not shared numerical residual"
than the proposal's "ground-truth-recovery gate" framing implies.

---

## 1. Numbered attacks

**Attack 1 [unfalsifiable].** Gate G0 — described in §4 as "MANDATORY...
must PASS before ANY correlation reading... counts as evidence" — cannot
be evaluated at all over the proposed `θ ∈ [36.0°,42.0°]`, 0.2°-step grid.
§0.1 confirms: the four native-grid zero-crossings' `±1.4°` exclusion
zones merge into one continuous band `[35.727°,42.861°]` that fully
swallows the grid. No angle satisfies the selection rule's own clause (b).
The census's central gate, the mechanism the whole design relies on to
keep a null result from being over-read, has an empty domain — the
proposal is unfalsifiable in the specific sense that its own mandatory
falsification/confirmation gate can never fire, for or against, over the
grid it was written against.

**Attack 2 [inconsistency].** The defect in Attack 1 is not a
window-placement accident, fixable by shifting or widening the census
grid. §0.2 shows the `≥1.4°` buffer (justified as "half the established
2.84–2.95° period") is close to exactly half the period of the very
signal being tested — so periodic recurrence of crossings at that period
tiles the ENTIRE angular axis with exclusion zones, leaving only
`0.042°`–`0.147°`-wide safe slivers recurring every period, each narrower
than the proposal's own `0.2°` grid step. A design that reasons "half the
period is a safe distance from every null" while sampling a *periodic*
signal on a grid coarser than the resulting safe-sliver width has built a
selection rule that is nearly self-defeating by construction, independent
of which specific window is chosen. This is an internal inconsistency
between the buffer's own stated justification (half-period is "safe") and
its actual mathematical consequence (near-total exclusion, grid-scale
slivers) — the design reasoning and the design's own arithmetic disagree.

**Attack 3 [inconsistency].** Even granting QUANTUM's own proposed
rescue (redefine clause (b) to "maximize achievable margin," §0.3), the
best point the 31-point grid can produce (`θ≈39.4°`, margin `≈0.81°`) is
not a fresh, independently-robust anchor — it sits inside the exact
39.0°–39.8° neighborhood LOGBOOK's own record (Iteration 72, exp-095)
already, on real data, found could not be made into a clean "robust,
far-from-null" ground-truth control point without repeated correction,
and where even the corrected choice was shown to be only "less
compromised," never clean. A repaired selection rule that lands on a
point this program has already flagged as fragile does not deliver what
R15's addendum (which this proposal's own §2 explicitly invokes as its
authority: *"the new family must... reproduce the ALREADY-KNOWN-CORRECT
sign at a robust, far-from-null angle"*) actually requires — it produces
an anchor that passes the letter of a relaxed rule while failing the
substance the rule exists to guarantee. This is a second, independent
reason the "just widen the buffer or grid" fix does not by itself rescue
G0 into a scientifically meaningful gate.

**Attack 4 [unfalsifiable].** Gate G0 is billed (§0, §2, §7) as
"R15 addendum's own text, operationalized" and a "ground-truth-recovery
gate," but by its own construction it cannot recover independent ground
truth. `θ_anchor`'s own selection clause (a) requires "R3 AND R4 already
agree in sign" — so the anchor is *chosen* specifically because R3 and R4
agree there. G0's own sign test then checks `sign(R5)==sign(R3)==
sign(R4)` at that same point: two of the three equalities are guaranteed
true by the selection procedure itself, before any new data exists;
only R5's agreement is genuinely new information. Per §0.6, all three
families additionally share the identical construction recipe and a
signal independently proven to carry zero absorbed-power content — so
even R5's agreement, on its own, cannot distinguish "all three converge
on real diffraction" from "all three inherit the same shared, resolution-
independent systematic," exactly the failure mode R15's own addendum was
written to guard against ("two such points cannot, on their own,
distinguish genuine continuum convergence from a persistent recipe-level
artifact"). A gate that is largely guaranteed to pass by its own selection
rule, on a signal known to share a common systematic origin across every
family being compared, cannot license the confidence the "ground-truth-
recovery" label implies — whatever G0 reports, R3-CORROBORATED,
R4-CORROBORATED, or NEITHER, that reading is compatible with a shared
artifact story the gate never actually tests against.

**Attack 5 [inconsistency].** The G0 amplitude-ratio band `[0.5,2.0]` and
the `1.4°` buffer are asserted with no independent derivation from this
program's own on-file cross-resolution data for `delta_scene` itself.
`[0.5,2.0]` is imported by exact numerical analogy from exp-106's own
`abs_ratio` band — a factor-of-2 convention built for a *different*
physical channel (`kappa_window`'s cross-family absolute-intensity ratio
on an entirely different geometry/bridge family) — reused here for a
three-way, mutually-disputed `delta_scene` comparison without
re-justification. This is exactly the failure R17 (RULED OUT registry)
was adopted to prevent: "a tolerance/bracket/window sized to test whether
a feature is present... must be justified... against the largest
already-established cross-resolution... shift magnitude on file for a
comparable transition" — not adopted as a round, borrowed number. R17's
text applies to this exact situation and was not applied.

**Attack 6 [inconsistency].** §1's central risk-framing sentence
("sub-threshold whichever family is right") rests on the 0.08–0.12×
figure independently shown in §0.4 to be the wrong statistic by a
5.25×–7.87× margin; the directly on-point, already-filed number (this
program's own exp-100 Leg A) is 63% of the bar — still sub-threshold, but
a materially thinner margin than the proposal's own framing conveys. This
does not reverse any scored verdict, but it means the proposal's stated
premise for treating the census's downside as low-stakes is built on a
citation defect, discovered here rather than caught before Phase 2 by the
proposal's own author, applying this program's own R9 house rule to its
own text.

**No constraint-#N-violation found.** T1 is correctly, repeatedly N/A
(no σ(I)/σ(x,t)/dispersive/gain term anywhere in the census or the three
bundled `kappa_window` items — confirmed against `design_geometry.py`
and the bundled items' own reuse of already-gated, static-`σ(x)`
machinery); constraint-3 is not engaged by any branch of this cycle
(§1's own text, independently confirmed correct); no constraint is
quietly dropped or scored on an unfalsifiable claim outside G0 itself.
This is a governance/instrumentation-trust cycle exactly as scoped, and
none of Attacks 1–6 implicate any constraint verdict on file.

---

## 2. Disposition of the five blind Phase-2 critiques

**PHOTONICS — ADOPT, in full, unconditionally.** §0.4 independently
reproduces the 5.25×–7.87× discrepancy exactly. Folded into the mandatory
fix list as: whatever text closes this question (this audit recommends
formal retirement, §4) must state `delta_scene`'s peak as **63% of
`C_thr_lab`**, not 8–12%, and must not re-cite T16's `amp_ratio` figure as
if it answered a raw-magnitude question it was never computed for. I do
not adopt PHOTONICS' own conditional framing ("if the census runs, require
Phase 3 to re-derive the G0 band...") as a live action item, since this
audit's overall recommendation (§4) is to not run the census at all — the
substance of PHOTONICS' finding survives into the retirement text instead
of into a G0 band re-derivation that would otherwise become moot work.

**MATERIALS — ADOPT, in full, and elevated to the deciding argument.**
§0.5 independently confirms the disposition memo's ceiling is exhaustive
and unconditional, not a soft lean. Combined with Attacks 1–4 (the census
cannot even execute its own mandatory gate as designed, and a repaired
gate would land on an already-flagged-fragile anchor without delivering
genuine ground-truth recovery), MATERIALS' economic argument stops being
merely "not worth the cost" and becomes the correct call on the merits:
there is no version of this census — patched anchor rule or not — whose
outcome could ever change a realizability tier or a constraint verdict,
and the specific patch available (§0.3) does not even deliver a
scientifically clean measurement. **ADOPT MATERIALS' recommendation:
Tier 0 should formally retire the `delta_scene` R3-vs-R4-vs-R5 question
this cycle, citing `disposition_memo.md` directly, corrected per
PHOTONICS' fix (§0.4).** ADOPT MATERIALS' support for bundled Tier-1
items 1, 3, 4 of the Phase-1 proposal's §5 without reservation — MATERIALS'
own realizability-bound reasoning (item 1's hollow-vs-PEC-cored test does
not extrapolate past the already-locked thickness bound; it tests
`sections.radial_absorbed_power`'s own "core is energetically incidental"
null at ratios never before exercised) is independently confirmed sound
against `lab/sections.py`'s actual `radial_absorbed_power` implementation,
which I read directly — the instrument exists, is already validated
(suite stage 10), and the test as scoped is cheap and expressible.

**ELECTROMAGNETISM — ADOPT the diagnostic finding; OVERRIDE the proposed
remedy as a live Phase-3 action.** EM's finding (§0.6, Attack 4) that G0
tests mutual agreement among non-independent, shared-systematic families
rather than genuine ground truth is correct and independently confirmed
from the R15/exp-076 record — ADOPTED, folded into the retirement
rationale (§4): even a version of G0 that could be evaluated would not
deliver the "ground-truth-recovery" standard its own name claims. I
**OVERRIDE** EM's own prescribed remedy (add a Richardson-style
convergence-shrinking test, `|Δ(R4,R3)|` vs. `|Δ(R5,R4)|`, before trusting
the census's outcome branches) as a live fix for this cycle — not because
the remedy is unsound in principle (it would be a genuine improvement to
G0's own diagnostic power on a future occasion), but because it presumes
a repaired G0 is worth building and evaluating at all, and Attacks 1–3
plus MATERIALS' ceiling (§0.5) show that even a version of G0 that both
(a) has a non-empty domain and (b) tests genuine convergence rather than
mere agreement would still spend real FDTD budget on a question this
program's own founding memo has already closed at zero cost. EM's own
steel-man (T1 correctly N/A, the cost-scaling law is right, "FAIL is a
reported outcome") stands unaffected — none of it depended on the census
actually running.

**THERMODYNAMICS — ADOPT, in full, unconditionally, and this is the one
fix that MUST be wired into whatever survives to Phase 3.** §0.4 of
exp-106's own Red Team audit (independently re-read, not re-derived here
since the arithmetic is already on file and correctly attributed) confirms
the physically-correct `p_abs_w ∝ σ_ext·σ_abs` proxy applied to exp-105's
established margins gives `≈267×` at r=156 and `≈120×` at r=312 for the
fixed-abs family — not the blanket "≥100×, matching every prior cycle"
the Phase-1 proposal's Item 3 predicts. **Mandatory fix, folded into the
Tier-1 kappa_window closeouts this audit recommends proceeding with (§4):**
replace the blanket prediction with the per-cell number, explicitly
naming `(fixedabs, r=312)≈120×` as the fragile cell (only 20% above the
proposal's own stated floor, not comparable to the other three cells'
267×–700× headroom), tighten the falsification band so a genuine further
order-of-magnitude erosion at that one cell would actually be caught
(the proposal's own `<10×` band cannot register a drop from ~700× to
~120×, let alone a further one), and add the R21 narration commitment
THERMODYNAMICS names (this channel already carries two non-firing R21
founding instances with a live three-strike auto-fire clause — exp-099,
exp-100 — a third silent non-narration would fire Checkpoint criterion 4
automatically).

**QUANTUM — ADOPT the core finding in full (independently re-derived
bit-exact, §0.1); OVERRIDE the recommended verdict-flip-to-support.**
QUANTUM's arithmetic is airtight and its diagnosis (an unsatisfiable
selection rule, discovered exactly where its own proposal's §7 asked Red
Team to check) is this cycle's single most consequential finding — ADOPT
in full, and credit it as the finding that, combined with MATERIALS' and
PHOTONICS' independent findings, tips this audit toward recommending
retirement rather than a redesign. I **OVERRIDE** QUANTUM's own proposed
remedy as sufficient to move to a plain "support": §0.3 (this audit's own
extension of QUANTUM's fix) shows the repaired rule's best achievable
point is not the clean, independently-robust anchor R15's addendum
requires — it lands inside a neighborhood this program's own record has
already shown is not safely characterizable at this grid density. QUANTUM
correctly diagnosed that the rule as written has an empty domain; its own
proposed patch produces a non-empty but scientifically thin one, and
Attack 3 explains why that thinness matters, not merely as a formality.

---

## 3. New defect none of the five caught

**The generalized, buffer-vs-period structural argument (§0.2/Attack 2)
and its consequence for QUANTUM's own proposed fix (§0.3/Attack 3).** All
five blind critiques and QUANTUM's own diagnosis treat the anchor-rule
failure as a property of the specific `[36°,42°]` window and the specific
four cited crossings — true as far as it goes, but incomplete. Extending
the crossing lattice periodically (§0.2) shows the rule's own buffer
(`≈half-period`) makes near-total exclusion a property of the rule
applied to ANY window of this signal, not an artifact of where this
census happened to draw its grid — so "widen the grid" or "re-center the
window," the natural first response to QUANTUM's finding, does not
generically rescue a scientifically meaningful anchor; it can, at best,
get lucky and land inside one of the `0.04°–0.15°`-wide periodic slivers,
narrower than this census's own `0.2°` grid step. Separately, testing
QUANTUM's own concretely-proposed repair against LOGBOOK's own
exp-095 record (§0.3) shows the repair's best output is not merely
"thinner-margin than intended" but specifically re-lands inside a
neighborhood this program has already, on real data, found could not be
made into a clean far-from-null control point — a fact none of the five
critiques nor QUANTUM's own proposed flip condition checked against this
program's own prior history on the identical angular band.

---

## 4. Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

This verdict applies to Iteration 84 as a whole, not to the R5 census in
isolation — the cycle bundles two structurally independent pieces of
work (§0 of the Phase-1 proposal states this explicitly), and they do not
share a fate.

**On the R5 census (Tier 0): do not execute it, in any repaired form,
this cycle. Formally retire the `delta_scene` R3-vs-R4-vs-R5 question
instead, discharging the standing (now eight-cycle, per exp-106's own
NOTES.md) deferral obligation by retirement rather than execution —
matching this program's own Iteration-51 precedent (a standing item may
be discharged by a reasoned written retirement, not only by one more data
point).** The case for this is cumulative, not any single attack alone:

1. The census as literally specified cannot execute its own mandatory
   gate — G0's domain is empty over the proposed grid (Attack 1,
   independently confirmed exact).
2. This is not a local, easily-patched defect: the buffer-vs-period
   relationship makes the rule close to universally unsatisfiable for
   this periodic signal at this grid density (Attack 2).
3. The best available patch (QUANTUM's own proposed fix) produces an
   anchor inside a neighborhood this program's own record already shows
   cannot be cleanly characterized as "robust, far-from-null" (Attack 3)
   — so even a "fixed" G0 would not deliver the standard its own
   authority (R15's addendum) requires.
4. Independent of all of the above, G0 as designed is not a genuine
   ground-truth-recovery gate even where it CAN be evaluated — its
   selection rule is partly self-fulfilling and all three compared
   families share a common systematic-error origin on a signal proven to
   carry zero absorbed-power content (Attack 4).
5. Even a hypothetically well-posed, genuinely convergence-testing G0
   evaluated on a genuinely robust anchor would still spend ~66 FDTD
   calls / 3.3–4.0h wall to resolve a question MATERIALS' own founding
   memo has already, unconditionally, shown cannot change any
   realizability tier or constraint-1/2/3/4 verdict under any branch
   (§0.5) — the census's own best-case outcome is a citation-attribution
   relabeling, not new evidence about the phenomenon program.
6. The proposal's own stated safety net for running it anyway ("sub-
   threshold whichever family is right") itself rests on a citation
   defect that materially understates how close to threshold the signal
   actually sits (Attacks 5–6).

No single one of these is dispositive by itself (MATERIALS' economic
argument alone was already strong before this audit; QUANTUM's structural
finding alone might have been read as "patch the buffer and proceed"), but
together they leave no version of "fix and run" that is both executable
and worth executing. **Retirement, not redesign, is this audit's
recommendation for Phase 3.**

Retirement is scoped precisely, not total: it closes the
resolution-family-attribution question (does R3 or R4 read `delta_scene`
correctly, and would a third point disambiguate) as economically closed,
per MATERIALS' own single stated flip condition (a future proposal
identifying a live realizability question that genuinely depends on which
family is correct would reopen it — none exists today). It does **not**
foreclose T28's own still-open, larger mechanism question (the
~2.84–2.95° periodicity's ultimate physical origin remains genuinely
unexplained on LOGBOOK's own record) and does **not** touch any of the
other standing T28 deferred items (the 750/450nm leg, the `G40` full-width
leg, the x-wall admittance refit, `PAD`-with-article survival at other
wavelengths) — all remain open, unaffected.

**On the three bundled `kappa_window` Tier-1 closeouts (§5 items 1, 3,
4): PROCEED, with THERMODYNAMICS' mandatory fix applied.** These share no
machinery with the census, are near-unanimously supported (MATERIALS
explicitly, EM/QUANTUM/PHOTONICS by not attacking them), cheap
(≈75–90 minutes new FDTD for item 1; items 3–4 are zero-marginal-cost
desk work on already-persisted `results.json` fields), and each closes a
real, previously-identified gap (Red Team's own founding Attack 9 concern
for item 1; a genuine per-cell fragile-margin risk for item 3, per
THERMODYNAMICS; the numerator-side floor-gate gap PHOTONICS named at
exp-106's own Phase 5 for item 4). **Mandatory fixes required before Phase
4 runs on these items:**

- Item 3 (P5 thermal row): replace the blanket "≥100×, matching every
  prior cycle" prediction with the per-cell number, explicitly flagging
  `(fixedabs, r=312)≈120×` as the fragile cell, and tighten the
  falsification band accordingly (THERMODYNAMICS' fix, §2, ADOPTED in
  full). Add the R21 narration commitment.
- Item 1 (hollow-vs-PEC-cored delta): no defect found; proceed as
  designed (independently confirmed expressible against `lab/sections.py`
  `radial_absorbed_power`, §2/MATERIALS).
- Item 4 (numerator noise-floor check): no defect found; proceed as
  designed.

**Governance bookkeeping (no live action):** R24 was already ratified at
Iteration 83's own close — this cycle's own §6 note is correctly a
confirmation, not a re-opened question; nothing further is required of
Phase 3 on this point.

**What Phase 3 should NOT do:** attempt a minimal patch to G0's anchor
rule (relax the buffer, widen the grid, or both) and proceed with the
census under a belief that this discharges the standing deferral more
thoroughly than retirement would. Attacks 2–4 show that patch does not
produce a scientifically meaningful test, only a nominally-executable
one, and MATERIALS' ceiling means even a scientifically clean version
would not be worth the spend. If a future cycle identifies a genuine new
reason the R3-vs-R4-vs-R5 attribution matters (the one flip condition
this audit and MATERIALS both name), a properly-powered census should be
redesigned from scratch against a window and buffer independently
justified by R17's own discipline — not by patching this cycle's grid.
