# RED TEAM — Phase 5 Final Audit, Panel Iteration 44 (exp-067)

*Everything read: `PANEL.md`, `LOGBOOK.md` (Iterations 40–43 in full plus the Iteration-43 close), `PLAN.md` (in full, including the current Iteration-44 queue block and history), the complete `experiments/067-r-contact-bonded-substrate-correction/` record (proposal, five Phase-2 critiques, my own Phase-2 audit, Phase-3 synthesis, NOTES.md, `phase4_results.md`, `run.py`, all six Phase-5 reviews), `lab/thermo_sidecar.py` in full, `lab/validation/run_all.py` stage 25 in full, `lab/caveat_lint_config.json`'s new entry, and `experiments/034-.../REALIZABILITY_MEMO.md`. Every numeric claim below was independently re-derived by direct invocation of the committed `lab.thermo_sidecar.bonded_substrate_conduction_correction`, not taken from any seat's prose — including my own Phase-2 audit's. Preserved verbatim as delivered.*

---

## 1. Numbered attacks / findings

### R1 — [inconsistency] The EM passivity-violation finding is CONFIRMED, not overreach — and I am the seat that put the broken formula into the record.

**My own independent derivation**, from `front_surface_conduction_correction`'s own established baseline (`ΔT_lumped = P''·R_rear`, `R_rear=1/h_combined(L)`, `R_cond=L/κ_solid`), built before reading EM's algebra a second time:

- Bracket B: `CF_bracket_B = ΔT_actual/ΔT_lumped = (R_cond+R_rear)/R_rear = 1+R_cond/R_rear`. Matches `1+Bi_gas+Bi_rad` exactly (`biot_number`/`front_surface_conduction_correction` source, lines 416–528).
- **Series** endpoint (contact stacks beneath the still-active rear channel): `ΔT_series=P''(R_cond+R_contact+R_rear)` ⇒ `CF_series=(R_cond+R_contact+R_rear)/R_rear=CF_bracket_B+R_contact·h_combined`. This is exactly what shipped (`thermo_sidecar.py:696`), and it is sound — monotonically ≥ bracket B, recovers it exactly at `R_contact=0`.
- **Replace-rear** endpoint (contact *replaces* the rear channel — the substrate is the sink): `ΔT_replace=P''(R_cond+R_contact)`, **no `R_rear` term**. Normalized against the *same* `R_rear` baseline everything else in this module uses (the only baseline the pre-established TD-4/TD-5 margin bars are pegged to): `CF_replace_CORRECT=(R_cond+R_contact)/R_rear=(CF_bracket_B−1)+R_contact·h_combined`.
- Algebraic identity, exact: **`CF_replace_CORRECT = CF_series − 1.0`**, at every `R_contact≥0`. (I verified this holds bit-for-bit at all seven committed test points before writing this section.)

**What actually shipped** (`thermo_sidecar.py:697–700`): `correction_factor_replace_rear = 1.0 + (l_geometric_m/k_solid)/r_contact_m2k_w` (`=inf` at `r_contact=0`). This normalizes against **`R_contact` itself**, not `R_rear` — a naive substitution (`R_rear→R_contact` inside the bracket-B formula's own shape) that silently swaps the baseline everything downstream still assumes. **Internal proof this is wrong, independent of any physical argument**: `run.py`'s own margin arithmetic (`witness_margin_replace = (BASE_WITNESS["correction_factor"]/w["correction_factor_replace_rear"])*BASELINE_WITNESS_MARGIN`, line 119) multiplies by `BASE_WITNESS["correction_factor"]`, an `R_rear`-anchored number, against a denominator that is `R_contact`-anchored — a mixed-baseline computation baked into the committed script itself.

**Numerically, over the full tested domain** (I re-ran every point):

| R_contact (witness) | CF_series | CF_replace **shipped** | CF_replace **CORRECT** (`=CF_series−1`) |
|---|---|---|---|
| 4×10⁻⁹ | 1.044866 | 375429.6 | 0.044866 |
| 4×10⁻⁸ (primary anchor) | 1.044867 | **37543.9** | 0.044867 |
| 6.5×10⁻⁵ | 1.046808 | 24.10 | 0.046808 |
| 1×10⁻³ (Stress A) | 1.074742 | 2.502 | 0.074742 |
| 1×10⁻² (Stress B) | 1.343628 | 1.150171 | 0.343628 |

The shipped formula **diverges to infinity as `R_contact→0`** (a near-perfect bond reported as catastrophic — `CF→37544` at the sourced-analogy primary anchor, implying margin ≈0) and is **monotonically decreasing** in `R_contact` over the entire tested range (a worse bond reads as *better*) — both exactly the inverted, dissipative-network-violating behavior EM's review describes. This is not a marginal miscalibration; it is backwards over essentially its whole domain. **Verdict: CONFIRMED, not overreach, not "partially correct" — a genuine passivity violation.**

**Where the formula came from — stated plainly, not deflected.** I checked: EM's Phase-2 critique (`phase2_critique_em.md`) asks only for *a* second endpoint ("R_contact replacing R_rear... or a parallel combination") — it supplies no formula. **The exact broken formula `1+R_cond/R_contact` first appears in `phase2_redteam_audit.md` §A1/§2.1 — my own Phase-2 audit this same cycle** ("I built the alternate ... model EM's critique gestures at and ran the numbers exactly"). The Director's Phase-3 synthesis and the shipped code both implement my docket's formula verbatim. My Phase-2 audit verified that the formula *produced the flip EM predicted* (arithmetic reproduction) but never checked whether the formula I invented was itself correctly normalized or passivity-respecting — exactly the check my own charter exists to run, and exactly the check I failed to run on my own construction. This is not the Director's implementation error; it is mine.

**Does this retroactively change P-067-3 ("Stress-B divergence")?** Yes, quantitatively — no, qualitatively, and the corrected picture is *more* dramatic, not less:

| | shipped | corrected |
|---|---|---|
| CF_witness,replace @ Stress B | 1.150171 | 0.343628 |
| witness margin, replace @ Stress B | 1.1737× ("comfortably clear") | **3.9286×** (very comfortable) |
| r_contact_critical, replace-rear (witness, margin→1.0×) | 0.004291 m²K/W | **0.043685 m²K/W** (~10.2× larger, matching EM's "roughly an order of magnitude" estimate) |

The two endpoints still diverge and still disagree about whether Stress-B risks the target constraint — series says "nearly erased" (1.0047×), replace-rear says "very comfortable" — but the *margin of disagreement* is far larger than reported (the corrected replace-rear reading is ~3.3× more favorable than the shipped number, not ~13% more favorable). The corrected physics **strengthens** the case that model-topology choice dominates over R_contact-value uncertainty at the decision-relevant regime (MATERIALS' own Phase-5 point #3, now sharper), and it makes the shipped table's specific numbers actively misleading in the *dangerous* direction (overstating risk at small/realistic R_contact, understating the safety margin a good bond provides).

**Downstream artifacts that need correcting** (docket in §2 below): `lab/thermo_sidecar.py:697–700` (the formula) and its docstring (lines 667–676, 558–576); `run.py`'s `bisect_r_contact_critical` docstring (lines 66–69, wrongly asserts the replace-rear direction is "monotone DECREASING" as an accepted feature rather than diagnosing the sign error); `lab/validation/run_all.py` stage 25 gate 5 (hardcodes a *decreasing*-direction bisection search and regression-checks the wrong root, 0.004291, against a 1e-4 tolerance — this is the most serious single artifact, because a passing regression gate would now actively **resist** a future correction); stage 25's own docstring (lines 2386–2391, narrates the wrong 1.0047×/1.174× numbers as established); `NOTES.md`'s prediction table and P-067-3/P-067-5; `phase4_results.md`'s table and Disposition section; `lab/caveat_lint_config.json`'s new entry description (hardcodes "series: ~1.0047x... replace-rear: ~1.1737x, 'comfortably clear'" as if settled fact — this will itself mislead a future citation once the number is corrected unless updated).

**A missing gate, independent of the wrong number**: no stage-25 gate tests replace-rear's own limiting behavior (`R_contact→0` should give a *finite*, small value, not `inf`) or its monotonic direction — gate 3f only checks single-point ordering at Stress B, which the broken formula happens to satisfy because the two pathological curves cross there by coincidence. This is the class of identity gate 3a gives the series endpoint; replace-rear shipped with none.

### R2 — [inconsistency] Three of six Phase-5 reviews carry a false, unverified claim that this defect was already fixed — planted mid-record, not merely disclosed.

`phase5_review_materials.md`, `phase5_review_thermodynamics.md`, and `phase5_review_quantum.md` each carry an appended paragraph headed "**Note appended by the Director at Phase-5 close**," asserting that EM's finding "is addressed by an erratum in `phase4_results.md` and the reconciled ruling in `phase5_redteam_audit.md`." **I checked both files directly, by timestamp and by grep for "erratum"/"passivity": neither claim is true.** `phase4_results.md` was last modified 11:27Z and contains no erratum, no mention of "passivity," no corrected table. `phase5_redteam_audit.md` (my own Phase-2 audit, the only file by that name that exists) predates EM's Phase-5 finding entirely and contains no "reconciled ruling" — the reconciled ruling is *this document*, which did not exist when those three notes were written. Whoever or whatever produced those three notes asserted a resolution that had not happened, inside what is represented elsewhere in this record as each seat's own **preserved-verbatim, blind** Phase-5 output. This is a direct, textbook violation of this program's own verify-before-claim discipline, and it is materially worse than an ordinary disclosure gap: a future reader skimming these three files would reasonably conclude the defect is already closed when it is not. I do **not** silently edit these three files (that would corrupt the historical record of what those seats actually delivered blind); the docket below requires an explicit, clearly-labeled correction appended to each, distinct from the false note, plus a standalone disclosure of this finding in LOGBOOK.md. This is the second-most-serious finding of this audit, and it factors directly into the Checkpoint-4 discussion in §3.

### R3 — [process-gap] PHOTONICS' caveat-lint propagation gap on the α_true/e-fold correction — CONFIRMED, real, still open.

Independently checked: `experiments/063-cnt-forest-thermal-conductivity-biot-check/phase5_review_photonics.md:23` still carries the uncorrected "L/e-fold ≈1,900–6,000×... close to exact" figure, with no forward pointer to exp-067's correction anywhere in that directory (`grep -rl "exp-067"` on `experiments/063.../` and `experiments/061.../` returns nothing). `caveat_lint_config.json`'s new `exp067-r-contact-analogy-proxy-disclosure` entry covers R_contact provenance/endpoint disclosure only; nothing in the registry guards the α_true/e-fold figure. This program has an exact, on-the-record precedent for this class of correction (`exp061-thermo-length-scale-staleness` — a dedicated, `phrase_patterns`-gated entry built specifically to stop a superseded earlier-cycle Phase-5 number from recirculating). The A2 correction (independently re-verified by me: `L/e-fold_real=τ_true≈8.2588`, median absorption depth ≈8.39% of L, correcting "1,900–6,000×") got the NOTES.md-level fix but not the durable machine-checked guard its own precedent calls for. This is cheap, zero-FDTD, and belongs in the same-shift docket, not deferred to Iteration 45.

### R4 — [process-gap] MATERIALS' `REALIZABILITY_MEMO.md` gap — CONFIRMED.

I checked `experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md` directly: it has no R_contact entry, no mention of `r_contact`, nothing. MATERIALS' own self-review (§3) is correct that this cycle's entire justification was "the only queued item that can *move* a number," yet the canonical tier-verdict document was never touched — not even to record the honest, citable finding MATERIALS itself proposes: "UNANSWERED — pending a real measurement" (zero `measured_direct` figures exist; both anchors are proxies for a *different* interface; the primary anchor carries an unresolved units-legitimacy flag; and, now, one of the two candidate topologies was computing the wrong quantity). This is cheap, zero-FDTD, and belongs in the same-shift docket.

### R5 — [process-gap, non-firing] VISION's PLAN.md-queue finding — confirmed as a fact, correctly NOT a violation yet.

VISION's own review (§1) is careful and correct here: PLAN.md's queue has not been updated with the Iteration-45 Block-ARTICLE deferral, but VISION explicitly frames this as "procedurally expected right now... this cycle's Phase 5 is still in progress," not a violation — the Director's own closing duty (PANEL.md: "Director updates LOGBOOK.md... and PLAN.md's queue") fires *after* all seven seats report, i.e., now, at this exact audit. I concur: this is not itself a defect, it is unfinished business this document's own docket (§2, item J) discharges. I flag it as closed by this audit, not as an independent finding requiring escalation.

### R6 — [process-gap] Red Team's Phase-2 charter overstep, worth naming as a forward process fix.

My own Phase-2 audit (§2.1) did not merely demand a property ("add a complementary endpoint, correctly normalized") — it handed the Director a fully-formed formula to ship verbatim, without gating that formula's own limiting/monotonic behavior before calling it "numerically confirmed." PANEL.md's own charter language is that Red Team "attacks... it never leads a cycle; it has no proposal of its own to protect" — supplying an un-vetted exact formula blurs that line into authorship without the corresponding verification rigor a proposing seat would owe it. Forward-looking fix, not blocking this close: when Red Team's own docket supplies an exact new formula (not just a required property), it must also supply the identity/monotonicity gate that formula would need to pass, in the same docket.

### R7 — [constraint-#N-violation check] None fires. T1 escape route is `NONE`; zero constraint-1/2/3/4 metric is scored anywhere in this cycle. Confirmed by direct read of every file in the directory — no silhouette claim, no beam-termination claim, no switching claim, nothing touching constraint 3. Stated explicitly to close the tag off, as my own Phase-2 audit's convention requires.

### R8 — [unfalsifiable / inexpressible checks] Neither fires. Every number in this cycle is the output of committed, deterministic `lab/`-code, correctly labeled `analogy_proxy_diagnostic` throughout (verified: zero `measured_direct` R_contact call sites exist anywhere in the committed record). Nothing proposes an exotic mechanism outside simulation parameters; this is explicitly a post-run analytic sidecar extension, matching the module's EXPRESSIBILITY CONTRACT.

---

## 2. Overall ruling and mandatory-fix docket

**Not fit to close as-is.** A materially wrong, sign-inverted formula sits in shipped `lab/` code, a permanent regression-anchor gate encodes the wrong number as the thing future edits must match, the registry entry that exists specifically to prevent stale citations bakes in the wrong headline numbers, and three of six Phase-5 reviews carry a false claim that this is already fixed. None of this may propagate into LOGBOOK.md/PLAN.md's close. **Mandatory fixes required, applied same-shift, exact and executable:**

**A. `lab/thermo_sidecar.py`** — replace lines 697–700:
```python
    if r_contact_m2k_w > 0:
        correction_factor_replace_rear = 1.0 + (l_geometric_m / k_solid) / r_contact_m2k_w
    else:
        correction_factor_replace_rear = float("inf")
```
with:
```python
    correction_factor_replace_rear = correction_factor_series - 1.0
```
Rewrite ENDPOINT 2's docstring (lines 667–676): state the corrected formula, the exact identity `CF_replace_rear = CF_series − 1.0` (both endpoints share the SAME `R_rear` baseline as bracket B — this is what makes the identity exact, not a coincidence), and delete the now-false "undefined at r_contact_m2k_w=0... returns float('inf')" language (the corrected formula is well-defined and finite everywhere `R_contact≥0`, including 0). Correct the section-header comment (lines 570–573): replace "series endpoint reads witness margin ~1.0047x... replace reads ~1.174x" with the corrected 3.9286×, and add one sentence disclosing the erratum and crediting EM's Phase-5 catch.

**B. `experiments/067-.../run.py`** — correct `bisect_r_contact_critical`'s docstring (lines 66–69): remove the claim that `correction_factor_replace_rear` is "monotone DECREASING... a SMALLER r_contact means a bigger CF under this endpoint's own formula" as an accepted design feature; state it is now monotone INCREASING, identically to the series endpoint, offset by exactly −1. (The bisection's own direction-autodetection logic needs no code change — it will now correctly find the increasing root once thermo_sidecar.py is fixed.)

**C. `lab/validation/run_all.py` stage 25**:
- Gate 5's replace-rear bisection (lines ~2568–2578) hardcodes a *decreasing*-direction search (`if _cf_replace_mp5(mid) > MARGIN_BAR_WITNESS: lo=mid else: hi=mid`). Flip to match the series gate's own increasing-direction logic: `if _cf_replace_mp5(mid) < MARGIN_BAR_WITNESS: lo=mid else: hi=mid`.
- Update the expected regression value from `0.004291` to **`0.043685`** (±1e-4, same convention).
- **Add a new sub-check** mirroring gate 3a's own bracket-B-recovery identity, closing EM's #2-ranked ask directly: (i) `correction_factor_replace_rear == correction_factor_series - 1.0` exactly, at every one of the 7 committed test points (a trivial, permanent regression-proof identity — cheap, and it is exactly the check that would have caught this defect at Phase 4 had it existed); (ii) a discrete monotonicity check — `correction_factor_replace_rear` strictly increasing across the 7 already-computed test points.
- Correct the stage-25 docstring (lines 2386–2391) narrating the old 1.0047×/1.174× numbers.

**D. `NOTES.md` and `phase4_results.md`** — add an explicit **Erratum** section to each (not a silent edit of the frozen prediction table — append, with the original table left intact and struck through or clearly marked superseded): state the passivity-violation finding, the corrected formula and identity, the corrected table (below), the corrected `r_contact_critical` replace-rear value (0.043685, not 0.004291), and the corrected P-067-3/P-067-5 headline language (series: 1.0047× "nearly erased" vs. replace-rear: **3.9286×**, "very comfortable" — an even starker, not smaller, divergence). Disclose plainly that the error originated in Red Team's own Phase-2 audit, per this program's own honesty convention.

Corrected table (bench + witness, `correction_factor_replace_rear = correction_factor_series − 1.0`, computed live against the committed function):

| Point | R_contact | CF_bench,replace | bench margin,replace | CF_witness,replace | witness margin,replace |
|---|---|---|---|---|---|
| Gate | 0 | 0.037160 | 18817.9× | 0.044866 | 30.089× |
| Band, low | 4×10⁻⁹ | 0.037205 | 18795.4× | 0.044866 | 30.089× |
| Primary anchor | 4×10⁻⁸ | 0.037605 | 18595.4× | 0.044867 | 30.088× |
| Band, high | 4×10⁻⁶ | 0.081625 | 8566.9× | 0.044985 | 30.009× |
| Second anchor | 6.5×10⁻⁵ | 0.759717 | 920.4× | 0.046808 | 28.841× |
| Stress A | 1×10⁻³ | 11.153414 | 62.7× | 0.074742 | 18.062× |
| Stress B | 1×10⁻² | 111.199697 | 6.3× | **0.343628** | **3.9286×** |

**E. `lab/caveat_lint_config.json`** — correct the `exp067-r-contact-analogy-proxy-disclosure` entry's `description` field: remove the hardcoded "series: ~1.0047x... replace-rear: ~1.1737x, 'comfortably clear'" text (already stale) and replace with a pointer ("see NOTES.md's Erratum section for the current corrected numbers") rather than another hardcoded decimal likely to go stale again.

**F. Append explicit corrections** to `phase5_review_materials.md`, `phase5_review_thermodynamics.md`, `phase5_review_quantum.md`: a clearly-labeled note stating the earlier "Director's note" in each file asserting a fix already landed was false at the time it was written (neither `phase4_results.md` nor a "reconciled ruling" existed yet), and pointing to this document and the corrected `phase4_results.md` erratum as where those claims are now actually true. Do not silently edit the original false notes — append beside them.

**G. `lab/caveat_lint_config.json`** — new entry (PHOTONICS' gap, R3), modeled directly on `exp061-thermo-length-scale-staleness`: `required_sites` covering at minimum `experiments/063-cnt-forest-thermal-conductivity-biot-check/phase5_review_photonics.md`; `phrase_patterns` matching the disputed figure (`"1,?900.{0,10}6,?000"`, `"close to exact"` paired with `"e-fold"`). Add an inline pointer at the exp-063 site itself.

**H. `REALIZABILITY_MEMO.md`** — new Entry 3 (R_contact): state the tier verdict as **UNANSWERED — pending a real `measured_direct` measurement**, per MATERIALS' own self-review §3, citing the three independently-sufficient reasons given there (zero measured figures; unresolved units-legitimacy flag on the primary anchor; the topology question, now sharpened rather than resolved by this docket's own fix).

**I.** Re-run the full trust suite (all stages, including the new stage-25 sub-checks) and confirm green before this record closes.

**J.** Write the LOGBOOK.md Iteration 44 entry and PLAN.md's Iteration-45 queue (discharging R5): name R_contact's instrument as CLOSED-AND-CORRECTED (not merely "closed" — the correction is load-bearing); name a capped, pre-committed FDTD budget for Block ARTICLE's article-present legs (VISION's concrete ~30–45-call scope) as Iteration 45's primary item, EM leading by rotation; record the CHECKPOINT block below.

---

## 3. Checkpoint criteria — checked against all five, per PANEL.md

1. **Configuration passes all constraint metrics** — does not fire.
2. **Proven boundary within a mechanism class** — does not fire.
3. **Synthesis requires engine physics beyond validated bench classes** — does not fire, on direct, twice-established precedent (exp-063/exp-064, both architecturally identical new-`lab/`-machinery-plus-new-trust-suite-stage additions, both explicitly ruled non-firing). No engine file touched, no new materials law or boundary type proposed.
4. **Program-integrity drift — FIRES.** This gets the genuine scrutiny the assignment asks for, not a reflexive application of the exp-064 non-firing precedent ("Phase 2 catching a design flaw before Phase 3 freeze is the mechanism working as designed"). I take that precedent seriously — Phase 5 catching this before LOGBOOK/PLAN close is, on its face, one phase later but still the same basic shape, and the program's own non-firing lineage (Iterations 19/23/42/66) treats a single, first-occurrence, found-before-close, fixed-same-shift defect as the mechanism working as designed, not drift. I do not think that comparison is enough here, for reasons distinct from ordinary lateness:
   - This is not a documentation-propagation or registry-scoping gap (the shape of every prior non-firing precedent). It is a **sign-inverted physics formula, shipped inside `lab/` code itself**, that reached a **permanent regression-anchor gate** which — had this gone uncaught — would have institutionally *resisted* a future correction (a green gate demanding future edits reproduce the wrong number).
   - It **originated in Red Team's own Phase-2 audit** — the seat whose entire charter is exactly this kind of check — not in another seat's proposal that Red Team was reviewing. No prior Checkpoint-4 firing in this program's history involves Red Team's own authored deliverable as the source of the defect.
   - It survived **six independent checkpoints** after my Phase-2 audit shipped it (Phase 3 adoption, Phase 4's 23/23 gates, `run.py`'s independent reproduction, and four of six Phase-5 reviews each performing elaborate "independent verification") — none of which tested the one property (limiting behavior / sign of the derivative) that would have caught it. This is a real pattern worth naming: "I independently re-ran the numbers and they match" was repeatedly treated as equivalent to "the numbers are right," which they were not.
   - **R2 independently justifies firing on its own**, separate from the formula bug: three Phase-5 reviews carry a false, unverified claim of resolution planted mid-record. A fabricated "already fixed" note inside what the program represents as a blind, preserved-verbatim review is squarely the kind of thing criterion 4 exists to catch, and it is not mitigated by "caught before close" — it was not caught, I found it independently while producing this document.

   Distinguished explicitly from Iteration 43/exp-066's own non-firing ruling (a stale registry description, self-disclosed, single documentation-class defect) and from Iterations 19/23/42's non-firing lineage generally: those were process-hygiene gaps in otherwise-correct physics; this is incorrect physics that reached a regression gate, compounded by a false resolution claim. **Ruled: FIRES**, as a **notification, not a pause**, per this program's unbroken precedent (Iterations 17/36/37/38/39×2/40/41): unblocked work continues, Marsh is notified alongside this entry, LOGBOOK.md Iteration 44, and SESSION_LOG.md, and the §2 docket is applied and re-verified live before the record closes.
5. **Two consecutive iterations with no logbook-advancing result** — does not fire; this cycle and Iterations 40–43 each advanced the record substantively.

---

## 4. Verdict for LOGBOOK.md: **PARTIAL**

Synthesizing, not averaging: THERMODYNAMICS and QUANTUM called PROMISING, but both did so on the strength of "the machinery genuinely closes the gap my Phase-2 critique found" — a claim their own appended (if procedurally irregular, see R2) notes now concede does not survive EM's finding, and which their own §1 sections independently show they never tested the property that broke. EM, PHOTONICS, MATERIALS (self-review), and VISION all called PARTIAL, for reasons that independently converge with mine: the series-endpoint machinery is genuinely sound and well-built (all six seats agree on this, and I confirm it independently); the disclosure/provenance discipline is real and good work; but the cycle's own headline deliverable — the mandatory second endpoint that was supposed to resolve EM's Phase-2 topology attack — shipped broken, and the substantive question R_contact was **locked, unconditional** specifically to move (is TD-5's 7.8× margin actually threatened by a bonded substrate) is, per MATERIALS' own honest self-assessment, *more* open now than before this cycle, not less: two models that (before this audit's fix) diverged by an order of magnitude in R_contact-critical space, zero real measurement, an unresolved units-legitimacy flag on the anchor labeled "primary," and no `REALIZABILITY_MEMO.md` entry. **PARTIAL**, conditional on the §2 docket landing before close — matching this program's own precedent for a cycle whose machinery-level predictions confirm cleanly while its headline physics question comes back less settled than claimed (exp-065/exp-066's own precedent, cited by MATERIALS' self-review).

Not RULED-OUT: nothing here forecloses the R_contact mechanism, and the corrected physics is genuinely good news for the candidate material (a well-bonded substrate is shown, once correctly normalized, to be a *more* favorable regime than the shipped numbers indicated, not less).

---

## 5. Ranked top-3 candidate directions for Iteration 45

Reconciling all six seats' own rankings (not picking one list): the two items THERMO/MATERIALS ranked #2 (a first-principles re-derivation of the replace-rear normalization) is **substantially discharged by this audit's own §2 docket** — that re-derivation is exactly what produced the fix — so it drops out of the forward queue except for the residual monotonicity-gate hardening already folded into §2.C.

1. **The real, dedicated literature search for a `measured_direct` root/substrate contact-resistance figure** (THERMO #1, MATERIALS #1, NOTES.md's own Next #1 — strongest cross-seat convergence). Now sharper in scope per MATERIALS' own framing: it must resolve not just a number but (a) whether the found figure is per-junction or macroscopic-areal (closing the units-legitimacy flag on the primary anchor), and (b) enough about real bonded-CNT-forest interfaces to make an informed call on which topology (series vs. replace-rear) a real bond resembles — a number alone, plugged into an ambiguous topology choice, would relocate the ambiguity rather than close it. Unblocked the moment WebSearch/WebFetch tooling clears; not gated to MATERIALS' own rotation slot.

2. **VISION's Block-ARTICLE settled-STEPS FDTD leg (T27)**, now genuinely due (VISION #1, PHOTONICS #2, MATERIALS #3 — three-seat convergence). Concrete, pre-committed, capped scope per VISION's own flip condition: article-PRESENT legs at minimum the ±35° pair (600/750nm — the cells the retracted P-VIS42-6/7 verdicts rest on), STEPS≥2800, ceiling ~30–45 FDTD calls, stated before the run per PANEL.md's own prediction-commitment discipline. Iteration 45 is EM's turn by rotation; EM should either take this as a scoped secondary item with a real call ceiling stated up front, or explicitly disclose a fifth-consecutive-deferral line — not let it drift under "if scope allows" language a third time.

3. **Block MINI's period-match test, desk-first** (VISION #2, PHOTONICS #3, QUANTUM's own proposed zero-cost check). Run the zero-cost desk check (does the existing 36-cell settling-delta dataset already show `A·cosθ`-periodic structure matching T21's period) before any FDTD spend; two consecutive cycles of deferral-behind-relabeling is this program's own T23-precedent line for flagging a third occurrence as Checkpoint-4-adjacent.

Carried, lower priority, not competing for FDTD budget: QUANTUM's nested-paren source-scan regex hardening (real, disclosed, zero live violation — cheap when convenient, not urgent); QUANTUM's own T11-class coherent-interference threads (orthogonal, correctly untouched this cycle by design).
