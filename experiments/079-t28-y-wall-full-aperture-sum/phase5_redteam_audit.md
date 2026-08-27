# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 56 · exp-079
## Adjudicating all six blind Phase-5 reviews of the full, non-edge-reduced y-mirrored aperture sum: reconciling MATERIALS' and QUANTUM's convergent-but-distinct findings on Idealization 9's scope, weighing EM's near-field challenge to Red Team's own recommended next instrument against PHOTONICS' concrete build sketch, and closing three still-open record-hygiene gaps this cycle's own prior corrections missed

**Seat: RED TEAM.** Read, in order: `PANEL.md` in full (seat 7's own
charter, the target phenomenon + four constraints, the five-phase loop,
the Checkpoints section, criteria 1–5); `AGENTS.md` in full; `LOGBOOK.md`
in full (~17,080 lines — RULED OUT R1–R9 in full; ESTABLISHED; LIVE
THREADS in full, close attention to T28, Iterations 46–55);
`experiments/078-.../phase5_redteam_audit.md` in full (this cycle's own
direct ancestor and format model — not copied); this cycle's complete
record in order — `phase1_proposal.md` (as corrected, carrying the
PHASE-3 UPDATE and revised §4/§7), all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md` (including §4b),
`phase4_results.md` (including its corrected §1), `y_wall_aperture_sum.py`,
`y_wall_aperture_sum_results.json`, `_output.txt`, and all six blind
`phase5_review_{vision,photonics,materials,em,thermodynamics,quantum}.md`;
`experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`,
`experiments/048-.../design_geometry.py`, and `lab/fdtd2d.py::
Sim.add_line_source`. I alone see the complete corrected record AND all
six blind Phase-5 reviews, and speak last.

Own owned verification: independent Python re-derivations, this session's
scratchpad (`/tmp/.../rt_check1.py`, `rt_check2.py`), plus a bit-exact
re-run of `y_wall_aperture_sum.py` itself and a `git diff` re-check — see
§0.

---

## 0. What I independently verified this cycle, from primitives, before ruling on anything

1. **Re-ran `y_wall_aperture_sum.py` end to end.** Bit-identical to the
   committed JSON and to every number in `phase1_proposal.md`/
   `phase4_results.md` (`C80−C40 rel_dev=0.2857` SUPPORT; `PAIR_PAD
   rel_dev=0.5679`/`PAIR_ABSORB40 rel_dev=0.5157` both INCONCLUSIVE;
   `ss_tot` ratio `9.392×10⁻⁷`; convergence `2.431×10⁻⁴`→`1.496×10⁻⁵`;
   ablation `|ΔP*|≤0.023°`, `PAIR_ABSORB40` ablated `ptp=0.000e+00`;
   T21-forced-fit `R²=0.9425`/`rel_dev=0.3101`; gates at `[4.77°,15.50°]`
   clean). No diff written to disk on re-run (`git status --porcelain` on
   the directory returned nothing before my own edits below).
2. **MATERIALS' collapsed-Pearson-r claim (§2a of its review) —
   INDEPENDENTLY REPRODUCED, exactly, digit for digit**, without needing
   any tooling correction of my own this time (unlike exp-078's own final
   audit, which caught a wrap-around bug in its first attempt at a
   similar check — I built the realizable `μ_r=1` admittance and swept
   both formulas across the actual `[4.77°,15.50°]` envelope with
   `np.unwrap` applied before correlating from the start, informed by
   that precedent): `ABSORB∈{40,60,70,80}` → Pearson `r(arg(r_matched),
   arg(r_realizable)) = 0.873191 / 0.878742 / −0.630059 / 0.743649` —
   **matches MATERIALS' table to six decimal places at every depth,
   including the sign of the negative case.** MATERIALS' finding is real.
3. **MATERIALS' §2b end-to-end Test-A recomputation under the realizable
   admittance — INDEPENDENTLY REPRODUCED**, built fresh from
   `y_wall_aperture_sum.py`'s own imported primitives (not copied):
   `PAIR_PAD` P*=`2.0075°` (rel_dev vs T28 `0.5647`, INCONCLUSIVE),
   `PAIR_ABSORB40` P*=`2.0075°` (rel_dev `0.5193`, INCONCLUSIVE),
   `C80−C40` P*=`2.0150°` (rel_dev `0.2910`, SUPPORT — unchanged,
   non-informative per the ablation control) — **matches MATERIALS'
   table exactly**, and every period shift from the committed
   matched-admittance model is `≤0.0151°`, confirming the "at most
   `0.015°`" claim. **MATERIALS' central practical finding is real,
   independently re-derived, not accepted on its word.**
4. **THERMODYNAMICS' "3, not 4, deletions" recount (§3 of its review,
   already corrected in `phase4_results.md` before this audit) —
   INDEPENDENTLY RE-CONFIRMED from raw git history.** `git diff 9e4e1ae
   3673d42 -- y_wall_aperture_sum.py | grep -c '^-[^-]'` = **3**, matching
   the corrected `phase4_results.md` §1 exactly, not the as-first-written
   "4" THERMODYNAMICS' own review cites as the Director's pre-audit slip.
   The three deleted lines are exactly the renumbered `[7] SUMMARY`
   header and the old dict-literal's own closing line — cosmetic, not a
   removed computation, confirmed by my own bit-exact rerun (item 1).
5. **VISION's stale-§4-paragraph finding (§2c of its review) —
   INDEPENDENTLY CONFIRMED STILL PRESENT, UNCORRECTED, in the record I
   was handed.** Read `phase1_proposal.md` §4 as filed for this audit:
   the "Phase 2 may still reasonably require a formal look-elsewhere
   control" sentence VISION quotes is there verbatim, with no
   cross-reference to §5.3's ablation-control resolution anywhere in the
   paragraph. **Unlike the two THERMODYNAMICS-flagged gaps (item 4 above,
   and the PAD-deferral-reason gap, confirmed present and correctly
   resolved at `phase3_synthesis.md` §4b), this one was NOT actually
   applied before this audit began** — the task's framing that "both"
   gaps were "already corrected same-shift by the Director" is accurate
   for THERMODYNAMICS' two but was not yet true for VISION's one. Closed
   in this audit's own docket, §6 below (not merely flagged) — see the
   diff to `phase1_proposal.md` §4.
6. **MATERIALS' own recommended same-shift fix to Idealization 1 (§4
   item 2 of its review) — also independently confirmed NOT yet
   applied**, checked directly against the file: Idealization 1 still
   cited the bare, uncorrected "Pearson `r>0.9997`... near
   period-invariant" figure with no disclosure that it fails to
   generalize to this file's own envelope. Closed in this audit's own
   docket, §6 below.
7. **EM's Fraunhofer-distance and `theta_local` spread figures —
   INDEPENDENTLY RE-DERIVED from the committed geometry.**
   `W²/λ = 1504²/20 = 113,100.8` cells; `dist_image` range for C40
   `[861,2347]` cells → `861/113100.8=0.76%`, `2347/113100.8=2.075%` —
   matches EM's cited "`0.8%–2.1%`" range. `theta_local` envelope
   `[5.27°,15.00°]` for C40 → `15.00/5.27=2.85×` — matches EM's cited
   "`2.8×` range" to the printed digit. **EM's near-field claim is
   arithmetically real, not overstated.**
8. **The x-wall's own `c_empty_with_wall` construction — independently
   read from `boundary_reflectance.py` lines 273–299** (not taken from
   EM's or PHOTONICS' own description): `E = E_d + r_coeff * E_i`, a
   single scalar `r_coeff` multiplying the ENTIRE image field — confirms
   both EM's §4a and PHOTONICS' §4 characterization of why the x-wall's
   reduction has a genuine closed form the y-wall's does not.

No critique across the six reviews overreaches; every load-bearing
numeric claim independently reproduces. All six seats converged on
**PARTIAL**; I concur, with the adjudications below.

---

## 1. Adjudication of the six Phase-5 reviews

| # | Seat | Finding | Verified? | Load-bearing? | Disposition |
|---|---|---|---|---|---|
| F1 | VISION SCIENCE | Full reproduction clean, R9-clean; §4's R5-disclosure paragraph was never updated after §5.3/§7 resolved the exact gap it names — a stale in-place inconsistency, smaller in degree than exp-078's own stale table but the same failure shape | **CONFIRMED — and confirmed still UNFIXED at the start of this audit** (§0.5). | Yes — non-load-bearing but real, and (unusually) not yet closed by any prior phase. | **ADOPT AND CLOSE** (§6 item 1, applied this audit). |
| F2 | PHOTONICS | Structural finding re-derived a third independent way (reading the actual function signatures); the residual-sideband "sidelobe" mechanistic story is plausible but never derived from first principles, though the magnitude argument alone is decisive regardless; a concrete, buildable derivation route for Red Team's recommended next instrument, plus a fresh feasibility probe predicting a still-T21-proximate carrier as the likely first-pass result | **CONFIRMED.** T21 period, `theta_local`, `A_eff`, and the orders-of-magnitude figure all independently reproduce; the feasibility-probe numbers (`arg(r(90°−θ_beam))` phase swing, natural period 15°–29°) are internally consistent with EM's own separately-derived near-field concern (§2, below). | Yes — real, and directly load-bearing to the Iteration-57 ranking's own most consequential item. | **ADOPT IN FULL.** See §3, §7. |
| F3 | MATERIALS | Idealization 1's inherited Pearson-`r>0.9997` "near-invariant" citation does NOT generalize from exp-078's narrow `48°–54°` envelope to this cycle's own `4.77°–15.50°` envelope (collapses to `0.74–0.88`, goes negative at one depth); but a fresh end-to-end recomputation of this cycle's own Test A under the realizable substitution shows every period shift `≤0.015°`, every verdict unchanged, for Attack 1's structural reason, not the fragile correlation | **CONFIRMED, both halves, independently reproduced bit-for-bit** (§0.2–0.3). | Yes — the task's own central adjudication item. | **ADOPT IN FULL, adjudicated at §2.** Citation fix applied (§6 item 2). |
| F4 | ELECTROMAGNETISM | Red Team's own recommended plane-wave/global-steering y-wall construction is not "the same trick, rotated 90°" — the x-wall's reduction is an exact algebraic cancellation at any range; the y-wall has no such symmetry, and this bench's own geometry puts the aperture at `0.8%–2.1%` of its Fraunhofer distance from the wall (deep Fresnel zone), with a `2.8×` spread in per-point bounce angle already measured — direct evidence no single global angle characterizes the interaction | **CONFIRMED, all figures independently re-derived from raw geometry** (§0.7). | Yes — the task's own second central adjudication item. | **ADOPT IN FULL, adjudicated at §3.** |
| F5 | THERMODYNAMICS | `phase4_results.md`'s "only additive" diff claim is not quite accurate (3 deletions, not zero) — already corrected before this audit; a standing, explicitly-worded prior-cycle instruction (state a reason before a fourth PAD-sensitivity deferral) was not honored anywhere in this cycle's own Phase 1–4 record, only surfacing at Phase 5 | **CONFIRMED — both halves, and both confirmed ALREADY CORRECTED** (§0.4, `phase3_synthesis.md` §4b) before this audit began. | Yes, but already closed. | **ADOPT — no further action owed**, both gaps independently verified closed. |
| F6 | QUANTUM OPTICS | The ablation control proves the FT argument is unconditionally true (algebraic identity), but the STRONGER "at ANY period, from no echo at all" reading of Idealization 9 is proven only for `r(θ)` that stays slowly-varying across the sampled envelope — confirmed for the one smooth matched-admittance model actually tested, never independently re-checked for a hypothetically sharp/resonant `r(θ)`, including a not-yet-re-tested realizable-admittance substitution at THIS cycle's own wider envelope | **CONFIRMED as a scope point — and, per MATERIALS' own §2b (F3, above), independently reproduced here, the "not-yet-re-tested" gap QUANTUM names is now closed for the realizable admittance specifically** (it stays smooth enough at this envelope to leave the practical conclusion unmoved — see §2). | Yes — the task's own central adjudication item, resolved jointly with F3. | **ADOPT the scope point; the specific gap QUANTUM names is now empirically closed by F3.** Idealization 9 scoped accordingly (§6 item 3). |

Nothing across the six reviews is overridden. Every load-bearing claim
independently reproduces. Two reviews (F1, F3-half-of-it) named gaps that
the record I was handed had not yet actually closed, despite the task's
framing that they had — closed in this audit's own docket, §6.

---

## 2. Central adjudication #1: does Idealization 9 need narrowing, or is MATERIALS' own re-run enough to settle it?

**The task's own question, answered precisely: BOTH readings are correct,
because they answer two different questions, and conflating them is the
mistake to avoid.**

**QUANTUM is right that the argument's own literal scope is narrower than
the adopted prose states.** The mathematical content of Attack 1
(`E_echo(theta_beam)` is *exactly* the spatial Fourier transform of a
`theta_beam`-independent envelope `w(y_s)`, evaluated at `k·sinθ_beam`) is
an unconditional algebraic identity — true for *any* function `r(θ)`
plugged into `w(y_s)`, resonant or smooth, realizable or not. But the
*practical* conclusion Idealization 9 draws from that identity — "this
construction is structurally incapable of discriminating a real y-wall
echo, **at ANY period**, from no echo at all" — is a claim about the
FT's own *dominant spectral content*, and that claim is only as strong as
the assumption that `w(y_s)`'s dominant Fourier content is set by the
shared aperture window rather than by fine structure in `r(theta_local
(y_s))` itself. A sufficiently sharp resonant feature in `r(θ)` inside
the narrow `4.77°–15.50°` range — a guided-mode coupling feature, say —
would, via the monotonic `theta_local(y_s)` map, inject a spatially
localized feature into `w(y_s)`, and a localized feature superimposed on
a wide window is the textbook recipe for genuinely new spectral content
this construction's own machinery could represent. **This was checked for
exactly one `r(θ)` family (the matched-admittance model) before Phase 5.**
QUANTUM's point that the unqualified "at ANY period" phrasing over-states
what one tested family can establish is correct, and is a genuinely new,
previously-unstated finding — not a re-litigation of Attack 1 itself.

**MATERIALS' own re-run does not make QUANTUM's point moot as a matter of
LOGIC — it closes the specific, concrete instance QUANTUM's own review
flags as the live open case.** QUANTUM's review names one and only one
concrete un-tested case as the reason the gap matters practically (§3.2 of
its review, quoted directly): "a *realizable* (`μ_r=1`) admittance whose
transfer function is not guaranteed to inherit the matched-admittance
model's smoothness at this specific, never-before-sampled-this-widely
`[4.77°,15.50°]` envelope... Nobody this cycle re-ran that Pearson-r check
at the actual envelope this file uses." **That is exactly what MATERIALS'
own §2a/§2b independently did, in the same Phase-5 batch, without either
seat seeing the other's work** — and the answer is decisive on the
practical question: the realizable substitution is NOT smooth by the
narrow Pearson-r metric alone (`0.74–0.88`, negative at one depth — §0.2,
independently reproduced), yet plugged all the way through the actual
end-to-end construction, it moves every scored period by at most `0.015°`
and flips no verdict (§0.3, independently reproduced). **This means the
specific concrete case QUANTUM's own review poses as the reason to doubt
Idealization 9's unqualified reading is now tested, and the "at ANY
period" reading survives it** — a second independent `r(θ)` family,
substantially LESS correlated with the matched model than MATERIALS'
exp-078-era citation implied, still lands in the same place.

**Ruling: Idealization 9 is empirically moot, for both admittance
families anyone has actually tested, but QUANTUM's point about the
argument's own literal scope remains correct and should be recorded as a
scoping condition, not retracted.** This is not a contradiction — it is
the same discipline this program's own R8 rule enforces elsewhere: a
robustness argument (here, "any r(θ) works") is not established merely
because the ONE argued-for consequence (the FT identity) is true; it must
be independently checked against the concrete alternative that would
break it, and once checked, disclosed as scoped-and-confirmed rather than
either unconditionally true or merely "probably fine." **I have applied
this fix directly** (§6 item 3): Idealization 9 now states the claim is
proven for `r(θ)` slowly-varying relative to the aperture window, backed
by TWO independently-tested families (not one), and explicitly notes it
has not been checked against a hypothetically sharp/resonant `r(θ)` and
should not be read as ruling one out a priori. **This does not change the
Combined Verdict, the Test-A numbers, or the ablation control's own
conclusion** — it sharpens the record's own honesty about what has
actually been established versus what an algebraic identity alone
guarantees, exactly the distinction this cycle's own central finding
(Attack 1) already drew between "the data is right" and "the
characterization of what the data proves is too broad."

---

## 3. Central adjudication #2: does EM's near-field challenge change the Iteration-57 ranking, or does PHOTONICS' build sketch mean the construction is worth building regardless?

**Ruling: EM's finding does not argue against building the recommended
construction — it argues for sequencing a specific, cheap, already-named
validity check BEFORE it, which four of six seats (EM, VISION,
THERMODYNAMICS by implication, and PHOTONICS' own probe) converge on
independently even though only EM frames it as a formal precondition.**

**What EM actually established, weighed on its own terms.** The x-wall's
own two-plane-wave reduction is not a plane-wave *approximation* at all —
it is an exact cancellation, valid at any propagation distance, because
mirroring through the `x=0` wall leaves the aperture's own `y_s`-dependent
driven phase and taper completely untouched (independently re-confirmed,
§0.8, by reading `c_empty_with_wall` directly). The y-wall has no such
symmetry: mirroring through `y=0` flips the very coordinate the driven
phase and taper both depend on, so a "plane-wave/global-steering" y-wall
construction, built by analogy, would be a genuinely NEW physical
approximation standing on its own merits — and this bench's own committed
geometry (independently re-derived, §0.7) puts the aperture at `0.8%–
2.1%` of its own Fraunhofer distance from the wall, with a measured
`2.8×` spread in the per-point angle different aperture points present to
the wall — direct, already-in-hand evidence that no single global
incidence angle characterizes how this aperture actually meets this wall.
**This is a real, quantified, independently-reproduced physical concern,
not a hedge.**

**What PHOTONICS' probe actually established, and how it relates.**
PHOTONICS' feasibility probe answers a DIFFERENT question than EM's:
given that the construction IS built exactly as specified (`r(90°−
θ_beam)` applied globally), does the reflectance term vary fast enough
across the real `36°–42°` sweep to produce a T28-matching period on its
own? Answer: no — `arg(r(90°−θ_beam))`'s own natural period is `15°–29°`,
4–15× longer than the `6°` sampled window can resolve, so the most likely
first-pass outcome is still a T21-proximate carrier with an
`ABSORB`-dependent AM-sideband modulation, not a clean new frequency.
**These two findings are complementary, not competing**: EM's question is
whether the construction is a physically VALID approximation of the real
multi-point aperture-wall interaction at all (a precondition on the
model's own legitimacy); PHOTONICS' question is what result the
construction would report IF built exactly as specified (a prediction
about its output, conditional on validity). A construction can fail EM's
validity test and still produce PHOTONICS' predicted T21-proximate
result for an entirely different, spurious reason — which is precisely
why EM's check should run first: if the construction is not a valid
representation of the real interaction, PHOTONICS' own pre-registered
prediction (T21-proximate carrier, AM-sideband) becomes a prediction
about an invalid model's artifact, not about the wall's physics, exactly
the same category error Attack 1 found in the per-point-image family this
cycle already retired.

**This is not a reason to abandon the construction — three seats (EM,
VISION, THERMODYNAMICS-via-its-own-power-fraction-suggestion) and
PHOTONICS' own probe converge that it is the only remaining construction
in this seven-cycle sub-thread not structurally guaranteed to fail by
Attack 1's own mechanism, and it should be built.** The ranking question
is purely sequencing: run EM's own named, already-specified, zero-FDTD
validity check (the Fraunhofer margin, already computed; and the
"does any single effective angle reproduce the full per-point coherent
sum's own envelope structure to a stated tolerance" test, not yet run)
**before** spending the construction effort, rather than building first
and discovering — a third time on this exact sub-thread, after the
as-filed `theta_beam` bug and the "corrected" `90−theta_beam` bug — that
the headline result was never capable of answering the question it was
built for. PHOTONICS' own concrete derivation route (§4 of its review) is
not wasted by this sequencing — it is the thing to build once EM's own
pre-check clears, using PHOTONICS' pre-registered prediction as the
falsifiable target. **Reconciled ruling, adopted into the Iteration-57
ranking (§7): promote EM's cheap desk pre-check to run FIRST, immediately
followed by (not gated behind a separate cycle) PHOTONICS' own concrete
build if the pre-check does not foreclose it** — a single Tier-0 batch,
not two competing priorities.

---

## 4. R1–R9 registry, checked against this cycle

- **R1–R3, R6, R7**: N/A, as Red Team's own Phase-2 audit already ruled
  and I independently re-confirm — no constraint-1 claim, no
  shell-thickness claim, no resolution-convergence question (zero-FDTD
  desk model; the numerical-integration convergence check is a distinct,
  non-R3 concept), no fitted carrier/phase coefficient, no un-fit
  conditioning-only closure claim anywhere in this cycle.
- **R4** (hand-typed / not-independently-reproduced figures): **the
  "nine orders of magnitude" arithmetic slip (Phase 2, Attack 2) —
  correctly caught and corrected before Phase 3 froze anything, the
  earliest-possible R4 catch this sub-thread has managed on this exact
  failure shape (the fifth instance overall — exp-076, -077, -078, and
  now -079's own as-filed slip, caught at Phase 2 rather than Phase 5
  this time).** Separately, this audit found and closed two further
  small record-hygiene gaps that ARE R4-adjacent (a claim about a diff's
  own contents — "only additive" — overstated what the diff literally
  showed) but were already independently caught and corrected
  (THERMODYNAMICS, §0.4) before this audit began.
- **R5** (null-permutation control mandatory for a dense search):
  **correctly, and more rigorously than R5's own letter requires,
  discharged by the reflectance-ablation control**, as Phase 2's own
  audit already ruled and I independently re-confirm — this file makes
  one primary model, not a search, and the ablation answers the question
  that actually matters (does the recovered period depend on the wall
  physics) more decisively than a generic permutation control would.
  Clean.
- **R8** (unverified robustness/independence argument filed non-blocking
  when an affordable named check exists): **the live rule for this
  audit's own §2 finding, and correctly discharged, not triggered.**
  MATERIALS' own review did not merely argue the smoothness gap was
  probably fine — it computed the concrete alternative case (the
  realizable admittance, end to end through the actual construction).
  QUANTUM's own review did not merely assert Idealization 9 needed
  narrowing — it named the specific untested case and I independently
  confirmed (§0.2–0.3) that MATERIALS' own computation happens to answer
  exactly that case. This audit's own obligation under R8 was not to
  leave either finding as an unverified argument, and I met it by
  independently reproducing both from primitives before adjudicating
  §2, rather than accepting either seat's own framing.
- **R9** (operand commensurability): checked independently by VISION at
  Phase 2 and Phase 5, both clean; I re-derived the `rel_dev`/`ss_tot`
  commensurability argument myself (same units throughout) — no
  T16/`amp_ratio`-shaped defect anywhere in this file's scoring.

---

## 5. Checkpoint ruling — reasoning through all five criteria explicitly

The task specifically asks me to weigh this given the density of
corrections this cycle required across BOTH Phase 2 AND Phase 5 — more
layers of correction than any single prior T28 cycle except exp-078
itself (which fired non-firing on a comparable multi-layer structure).

**Criterion 1 (a configuration passes all constraint metrics):** N/A.
Zero constraint-3 engagement anywhere in this cycle, correctly and
consistently disengaged throughout, independently re-confirmed.

**Criterion 2 (a proven mechanism-class boundary):** **NOT YET RIPE**,
matching Phase 2's own ruling and every prior T28 cycle on this
sub-thread. The coherent-echo mechanism class has TWO reductions now
foreclosed by structural argument (the single-edge model, exp-078; the
full-aperture-sum model, this cycle), but the plane-wave/global-steering
construction remains genuinely untested, and both MATERIALS' x-wall
realizable-admittance refit and the wavelength-generality leg remain
open. At least three concrete, unpriced items remain (§7).

**Criterion 3 (engine physics beyond validated bench classes):** N/A.
Zero new FDTD, zero `lab/` diff, confirmed by `git status` before and
after this audit's own docket (my own edits touch only `.md` prose, no
`lab/`, no `.py`).

**Criterion 4 (program-integrity drift) — the one requiring explicit
reasoning, given this cycle's own layered correction history.** The
task's own framing is right to press on this: Phase 2 caught and fixed a
genuine, self-scored over-claim (the "closer to REFUTE" framing) BEFORE
freeze; Phase 4 caught and corrected the Director's own pre-audit
"nine orders" and "only additive" slips; Phase 5 then produced not one
but effectively FOUR further, distinct findings — MATERIALS' collapsed
citation, QUANTUM's scope narrowing, EM's near-field challenge to the
recommended next step, and (smaller) VISION's stale paragraph. **My
ruling: does NOT fire — but this is a closer call than exp-078's own
Phase-5 non-firing ruling, for a reason worth stating precisely, not
waved through by pattern-matching alone.**

Matching this program's own non-firing shape: every one of these findings
is **genuinely new information surfaced by an independent seat, not a
false claim actively defended past a freeze point.** The frozen Test-A
numbers, the ablation control, the gates, and the convergence check are
untouched by anything found this cycle (§0.1) — nothing computed is
wrong. MATERIALS' and QUANTUM's findings are a REFINEMENT of Idealization
9's own stated scope, not a reversal of it (§2) — the practical
conclusion survives independent testing against exactly the concrete
alternative QUANTUM names. EM's finding is a caution about a FUTURE
instrument not yet built, not a defect in this cycle's own computed
result (§3).

**Distinguishing from this program's own firing precedents, explicitly**:
unlike Iterations 49/50/52/54 (a verifiably false claim, or an unverified
robustness argument, actively defended across a freeze point, surfacing
only a full cycle later or after LOGBOOK had already recorded it), every
finding here was caught and independently verified WITHIN this cycle's
own Phase-5 layer, before anything reached LOGBOOK, and none required
defending a wrong number — matching Iterations 51/53's own non-firing
shape (exp-078's precedent for this exact sub-thread) more closely than
any firing one.

**The one genuine wrinkle, weighed honestly rather than smoothed over**:
two of the "already corrected same-shift" claims this cycle's own record
carried into Phase 5 (VISION's §2c finding, and MATERIALS' own
Idealization-1 fix) had, on independent re-verification, actually NOT
been applied before this audit began (§0.5–0.6) — meaning a "corrected"
label was attached to something not yet true, a shape this program's own
R4 rule exists to catch (a claim about what has been fixed is itself a
claim that needs independent verification, not merely trust). This is
smaller in stakes than any of R4's own named triggers (a non-load-bearing
documentation paragraph and a citation footnote, not a scored number or a
verdict), and it was caught and closed within this same audit, not left
to survive into LOGBOOK unexamined — but it is exactly the R4-shaped
gap this cycle's own task brief anticipated when it told me to verify
these corrections myself rather than trust that they were applied. **Had
this audit not independently re-checked both and simply repeated the
"already corrected" framing, THAT would have been the firing shape** —
matching exp-078's own §4 reasoning about why its own non-firing ruling
depended on this audit actually running its own check rather than
declining to. The reason it doesn't fire here is the same reason it
didn't fire there: the check was actually run, and both gaps are closed
below, not merely re-flagged.

**Ruling: criterion 4 does not fire.** Genuinely new information,
independently verified, none surviving unexamined to this document; the
one near-miss (stale "corrected" labels) was itself caught and closed by
this audit's own required verification pass, not by luck.

**Criterion 5 (two consecutive non-advancing iterations):** Not at risk.
This cycle genuinely narrows the T28 board a second consecutive time
(exp-078: single-edge model foreclosed; exp-079: full-aperture-sum model
foreclosed, for a precisely-scoped reason now independently confirmed
against two admittance families) — a real, cumulative advance in what
this sub-thread's per-point-image construction family can and cannot
answer, even though the underlying mechanism question remains open.

---

## 6. Mandatory-fix docket (same-shift, zero new FDTD, applied this audit)

1. **[VISION §2c, F1]** `phase1_proposal.md` §4's R5-disclosure paragraph
   — confirmed still stale at the start of this audit (§0.5) — corrected
   in place: now states the gap is RESOLVED, cross-referencing §5.3's
   ablation control, not merely disclosed. **Applied.**
2. **[MATERIALS §4 item 2, F3]** `phase1_proposal.md` Idealization 1 —
   confirmed still citing the uncorrected exp-078 Pearson-`r>0.9997`
   figure with no disclosure that it fails to generalize — corrected in
   place: states the collapse at this cycle's own envelope, and that the
   practical conclusion survives independently anyway, for Attack 1's own
   structural reason. **Applied.**
3. **[QUANTUM §3, F6, adjudicated §2 above]** `phase1_proposal.md`
   Idealization 9 — appended a scoping clause: the "at ANY period" claim
   is proven for `r(θ)` slowly-varying relative to the aperture window,
   confirmed for TWO independently-tested admittance families (matched
   and, per MATERIALS' §2b, realizable), not verified against a
   hypothetically sharp/resonant `r(θ)`. **Applied.**
4. **[F4/F5, already closed before this audit, independently
   re-verified]** THERMODYNAMICS' "3, not 4, deletions" fix
   (`phase4_results.md` §1) and the PAD-sensitivity fourth-deferral
   reason (`phase3_synthesis.md` §4b) — both confirmed correctly applied
   by this audit's own independent recomputation (§0.4). **No action
   needed.**
5. **[PHOTONICS §3, F2]** No fix owed to this cycle's own committed
   files — PHOTONICS' own request (derive the taper's own diffraction
   overtone and check it against the 2.55° residual) is correctly scoped
   as a low-priority, cheap Iteration-57 item, not a defect in this
   cycle's record (the residual is already disclosed and correctly ruled
   non-load-bearing on magnitude grounds alone). Folded into §7.

None of these five items touch `y_wall_aperture_sum.py`'s own frozen
Test-A numbers, `lab/`, or the official Combined Verdict — all are
record-completeness and scoping-precision fixes to `phase1_proposal.md`
prose only. No re-run of `y_wall_aperture_sum.py` is required (confirmed
by `git status`: only `phase1_proposal.md` is modified this audit, and
none of its cited numbers changed — every edit is additive prose around
already-correct figures).

---

## 7. Reconciled Iteration-57 ranking (all six seats + this audit)

### Tier 0 — zero FDTD, desk-only, run as one batch

1. **EM's cheap validity pre-check of the plane-wave/global-steering
   y-wall construction, run BEFORE building it, immediately followed by
   PHOTONICS' own concrete build (§3, this audit) if the pre-check does
   not foreclose it — a single sequenced batch, not two competing
   priorities.** Merges EM #1, VISION #2's own pre-registration guard,
   QUANTUM #2's "apply the Fourier argument to the proposed construction
   first," and PHOTONICS #1's own build sketch + pre-registered
   prediction. Concretely: (a) the Fraunhofer-margin/`theta_local`-spread
   calculation (already computed, §0.7/§3 above — a stated, disclosed
   validity gate, not a fresh computation); (b) test whether any single
   "effective angle" summary reproduces the full per-point coherent sum's
   own envelope structure to a stated tolerance (EM's own named check,
   not yet run); (c) if (a)/(b) do not foreclose it, build PHOTONICS'
   own sketched construction (§4 of its review — one new glue function,
   reusing `reflection_coefficient_vec`/`aperture_profile`/`G0`
   unchanged), pre-registering PHOTONICS' own prediction (dominant period
   likely still T21-proximate; the informative result is the offset from
   T21 and whether it tracks `ABSORB`/`PAD`) and THERMODYNAMICS' own
   suggestion (report `1−|r(θ_beam)|²` as an actual reflected-power
   fraction, the first real power-budget number on the y-wall side of
   this sub-thread) before scoring it. This is the single highest-value
   item on the board: the only construction in this seven-cycle sub-
   thread not structurally guaranteed by Attack 1's own mechanism to
   fail, sequenced so a third consecutive convention-scope bug (after
   the as-filed `theta_beam` bug and the "corrected" `90−θ_beam` bug)
   is caught before a build, not after one.
2. **Re-run PHOTONICS' own dense-sweep smoothness check (Phase-2 §3(c)
   idiom, zero new FDTD) against the realizable-admittance substitution
   at THIS cycle's own full `[4.77°,15.50°]` envelope, specifically —
   not merely the Pearson-r correlation MATERIALS/this audit already
   computed (§0.2/§2).** QUANTUM's own #1 pick, sharpened: this is a
   narrower, cheaper, more targeted completion of the exact gap §2
   adjudicates — an absolute smoothness check (does `arg(r_realizable
   (θ))` itself have resonant structure inside this envelope, independent
   of correlation with the matched model) is a genuinely different, and
   stronger, test than the correlation-with-the-matched-model check
   MATERIALS' §2a already ran. Cheap: the vectorized `r()` machinery
   already exists.
3. **Execute the still-unexecuted x-wall realizable-admittance (`μ_r=1`)
   refit** (MATERIALS #1 — now the single oldest-deferred MATERIALS item
   on the whole T28 board, carried unexecuted across exp-078 AND
   exp-079, three cycles running) — the only place on the whole board
   this substitution could still plausibly move a verdict (the x-wall's
   own marginal Test-B numbers, `r²=0.0001–0.0418`), independently
   reconfirmed by §2's own finding that the y-wall side is now robust to
   admittance choice by two tested families.
4. **Quantify a period confidence band for this cycle's own T21-proximity
   claim** (QUANTUM #3, cheap — reuse `desk_check_pricing.py`'s existing
   Cramér–Rao machinery or a residual bootstrap on `P*_model(PAIR_PAD/
   C80−C40)`), closing a real, disclosed, non-load-bearing precision gap
   under a number this cycle's own record states to three-significant-
   figure precision without ever bounding its own uncertainty.
5. **Independently derive the taper's own near-edge diffraction overtone
   and check it against PHOTONICS' 2.55° residual sideband** (PHOTONICS
   #3) — low priority (the residual is five orders of magnitude too
   small to matter to T28's real signal regardless of which story is
   right), a standard slit-diffraction calculation that would make this
   cycle's own record fully earned on this one point rather than merely
   plausible.
6. This audit's own five-item record-hygiene docket (§6, done).

### Tier 1 — cheap FDTD, next

7. **The full-width, non-aliased second-wavelength (`G40`) leg** (VISION
   #3, EM #3, QUANTUM's own standing charter item — now deferred across
   FOUR consecutive cycles: exp-076, -077, -078, -079). The cheapest
   remaining FDTD test of whether T28's periodicity is a real,
   wavelength-scaling-consistent physical effect at all, independent of
   which mechanism is being chased.
8. **Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary**
   (THERMODYNAMICS #3, carried from Iteration 53, now deferred four
   consecutive cycles).
9. **The 750nm x-wall two-wall spot-check** (EM #3 — the single
   oldest-unexecuted item on the whole T28 board).

### Tier 2 — the standing charter-relevant test, now the single most overdue item on the board

10. **Test whether the empty-scene T28 signature — and specifically the
    `PAD`-sensitivity axis — survives with a real absorbing article
    loaded** (VISION #1, THERMODYNAMICS #1 — near-unanimous top pick
    between the two seats with the most direct charter stake — now
    deferred across FOUR consecutive cycles: exp-076, -077, -078, -079,
    each cycle's own ranking naming it explicitly and each declining to
    run it; this cycle's own Phase 3 finally supplied the explicit
    scheduling reason exp-078's own ranking demanded, §0.4, but the
    underlying deferral itself continues). Every congruent-series config
    to date, across seven T28 cycles, is an EMPTY scene — every
    "absorption" this sub-thread has ever discussed, including this
    cycle's own reflectance weights, is domain-truncation-boundary
    bookkeeping, never a physical article warming up. This is the only
    queued item that would tell the program, directly, whether ANY of
    this eleven-cycle sub-thread has downstream relevance to constraint
    3 at all — a fundamentally different kind of information than
    another period-matching exercise, however well-instrumented, can
    supply. Weighed against Tier-0 item 1 (whether the y-wall mechanism
    question can be advanced at the desk level first): both are
    legitimate top candidates: this cycle's own Tier-0 items are cheaper
    and gate whether continued y-wall mechanism-hunting is worth the
    spend at all; this item is the one that would tell the program
    whether the seven-cycle sub-thread matters to the actual phenomenon
    program regardless of mechanism. **If Iteration 57 defers this a
    fifth time, the reason should be stated explicitly in that cycle's
    own synthesis, not carried forward by inertia** — this program's own
    now-well-established standard for this exact item.

### Tier 3 — governance

11. **Explicit ruling on whether the coherent-echo mechanism-class board
    is exhausted.** Ruled here: **NOT YET RIPE** — Checkpoint criterion 2
    does not fire (§5). Two reductions (single-edge, full-aperture-sum)
    are now foreclosed by structural argument, independently confirmed
    against two admittance families; the plane-wave/global-steering
    construction, the x-wall realizable-admittance refit, and the
    wavelength-generality leg remain genuinely open.

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9);
`A_eff≈518.81` is correctly re-flagged (not re-chased) throughout this
cycle's own record and this audit's own review of it.

---

## 8. Bottom line

**Combined Verdict: PARTIAL** — unanimous across all six blind Phase-5
reviews and this final audit. The corrected Test-A record stands,
verified bit-exact (§0.1): 1/3 nominal SUPPORT (non-informative, per the
committed reflectance-ablation control), 0/3 REFUTE, 2/3 INCONCLUSIVE
(primary proxy); 0/3 SUPPORT (secondary proxy). This cycle's own central
finding — a coherent aperture sum whose only `theta_beam`-dependent
ingredient is the shared driven-phase ramp is structurally incapable of
discriminating a real y-wall echo, at any period a slowly-varying `r(θ)`
could produce, from no echo at all — is independently re-confirmed
against a SECOND admittance family this audit did not have going in
(MATERIALS' realizable-admittance recomputation, §0.2–0.3), closing the
concrete gap QUANTUM's own Phase-5 review correctly identified as the
live scope question (§2). **This does not close the y-wall coherent-echo
mechanism class** — Checkpoint criterion 2 remains NOT YET RIPE (§5,
§7 Tier 3) — but it forecloses a second consecutive construction family
(single-edge, exp-078; full-aperture-sum, this cycle) for a
precisely-scoped, now doubly-verified reason, the cleanest negative
result this exact sub-thread has produced since exp-076's own
lossless-vacuum proof.

**Checkpoint criterion 4 does not fire** (§5) — every finding this cycle
produced, across both Phase 2 and Phase 5, is genuine new information
independently verified within this cycle's own review layer, none
surviving unexamined into a defended headline claim; the one genuine near
miss (two "already corrected" claims that had not actually been applied
before this audit) was itself caught and closed by this audit's own
required independent verification, the discipline whose absence would
have been the firing shape.

**The single most consequential finding I adjudicated**: MATERIALS' and
QUANTUM's Phase-5 findings, though each seat computed them independently
and neither saw the other's work, resolve into a single coherent
picture once combined — QUANTUM correctly identifies that Idealization
9's "at ANY period" language over-states what the algebraic FT argument
alone can prove (true only for slowly-varying `r(θ)`), and names the one
concrete untested case (the realizable admittance at this cycle's own
wide envelope) that would matter if it broke; MATERIALS, working from a
completely different starting question (does the inherited realizability
citation generalize?), happens to have already run exactly that test,
end to end, through the real construction — and it does not break the
practical conclusion, despite the underlying correlation collapsing far
more than the inherited citation implied. Neither finding alone would
have closed the question as cleanly: QUANTUM's point without MATERIALS'
recomputation would have left a real, unresolved scope gap in the
permanent record; MATERIALS' recomputation without QUANTUM's framing
would have been filed as a realizability footnote, its relevance to
Idealization 9's own logical scope never connected. Reconciling them
required recognizing they were answering the same underlying question
from opposite directions — exactly the kind of cross-seat synthesis this
audit exists to perform that no single blind Phase-5 review, working
alone, could have delivered.
