# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 82 (exp-105)
## "The T8 r=78/156/312 Bridge, Extended to the Coherent Point/Region-Intensity Channel"

*Red Team seat, fresh context, goes last, receives everything: `PANEL.md`,
`LOGBOOK.md` in full (RULED OUT R1–R23; Live Threads T1, T8, T9, T13, T14,
T28), the complete exp-105 record (`phase1_proposal.md`, all five
`phase2_critique_*.md`, this seat's own `phase2_redteam_audit.md`,
`NOTES.md`, `run.py`, `results.json`), and all six Phase-5 reviews
(`phase5_review_{photonics,materials,em,quantum,vision,thermodynamics}.md`).
Every load-bearing claim below was independently re-derived from primitives
— source code, `results.json` fields, and hand arithmetic — not merely
trusted from the six reviews' own summaries, per this seat's charter.*

## 0. Independent re-verification from primitives

**0.1 The `shape_ratio≡2^n` identity (PHOTONICS' finding).** Re-derived
independently, not merely checked against PHOTONICS' algebra. For a
two-parameter power law `κ(x)=κ_∞+B·x^n` evaluated at the forced geometry
`x(78):x(156):x(312)=4X:2X:X` (confirmed exact: `results.json::geom_78/
156/312.z_over_zr` give `x` ratios 2.0000/2.0000, `x78=0.503113`,
`x156=0.251557`, `x312=0.125778` — bit-exact 2:1 steps):

```
shape_ratio = [κ(4X)-κ(2X)]/[κ(2X)-κ(X)] = (4^n-2^n)/(2^n-1) = 2^n
```

independent of `κ_∞`, `B`, and the intercept fit method (holdout vs.
in-sample) — confirmed by direct symbolic expansion, not merely by the
sanity check at n=1,2. Solving the measured `shape_ratio=19.787847024468125`
(`results.json::p3.shape_ratio`, independently re-verified against
`(k78-k156)/(k156-k312)` using the raw `kappa_windows` triple, exact to
every printed digit): **n = log₂(19.787847…) = 4.306543**, and
`2^4.306543 = 19.7878…` closes the loop. **ADOPTED, independently
reconfirmed exactly.** This is the correct, sharper characterization of
what NOTES.md's own "nearly 5× past the linear-law band" language leaves
implicit, and PHOTONICS' physical argument (τ_shell=24 held fixed kills
direct shell transmission identically at every r, so the r-dependent
signal must ride on edge diffraction, whose standard scalar asymptotic
motivates the tested n≈1–2 range; n≈4.3 is roughly double the steeper of
the two candidates and, for an *apodized* graded shell specifically, in
the wrong direction — apodization suppresses ripple/diffractive leakage,
which should shallow the falloff, not steepen it) survives this seat's own
scrutiny: I can find no error in the physical reasoning, and the geometric
identity itself is airtight algebra, not an approximation.

**0.2 The dominance-ratio citation — re-derived from the raw constants,
independent of `mixed_length_scale_regime`.** Using the exact constants
`phase1_proposal.md`'s own Appendix declares (`K_AIR=0.026`, `DX_M=30e-9`,
`EMISSIVITY=0.9`, `T_AMBIENT_K=293.15`, `SIGMA_SB=5.670374419e-8`,
matching `lab/thermo_sidecar.py:82` exactly):

```
h_eff(r)  = K_AIR/(r*DX_M)
rad_term  = 4*EMISSIVITY*SIGMA_SB*T_AMBIENT_K**3 = 5.142614061152997 W/m^2K
r=78:  h_eff=11111.111...  ratio = 2160.595949644324   (NOT 1949x)
r=156: h_eff=5555.556...   ratio = 1080.297974822162
r=312: h_eff=2777.778...   ratio = 540.148987411081    (NOT 487x)
```

**Confirmed independently, bit-consistent with THERMODYNAMICS' own Phase-5
self-review §3: the correct dominance ratios are ≈2160.6× at r=78 and
≈540.1× at r=312, not the 1949×/487× `phase1_proposal.md` §6 and
`phase2_redteam_audit.md` §4/attack-4 both cite.** I went one step further
than THERMODYNAMICS' own review to identify the likely mechanism, since
the "source of the substitution is not recoverable" note in that review
invites a check: computing the SAME ratio with the emissivity factor
OMITTED (`4·σ·T³` instead of `4·ε·σ·T³`) gives 1944.5×/486.1× at r=78/312
— within 0.25% of the cited 1949×/487×, strongly suggestive (though not
bit-exact, so not certain) that the error is a dropped `ε=0.9` factor in
one hand-evaluated sentence, nowhere else in either document. **This does
not change the finding's severity** (non-load-bearing either way — see
§2 below) but is offered as a small, disclosed forward-clue for whoever
corrects the sentence.

**Does this defect survive into `NOTES.md`'s frozen Result/Learned
sections?** Grepped `NOTES.md` and `results.json` directly for "1949" and
"487": **zero hits in either.** Confirmed: the wrong figures live ONLY in
`phase1_proposal.md` §6 and this seat's own `phase2_redteam_audit.md`
§0.2/attack 4 — both pre-freeze documents. `NOTES.md`'s own Setup and P5
sections use only the vaguer, still-true "~3 orders of magnitude"/
"gas-conduction loss dominates... by ~3 orders of magnitude" phrasing,
which remains correct at the corrected figures (540×–2160× still spans
2–3 orders of magnitude). **THERMODYNAMICS' own ruling — that this does
not, on the most natural reading, meet R20's specific "survived Phase-3
freeze into Result/Learned" trigger — is independently confirmed correct
here by direct grep, not merely trusted.** See §3 for the R20 tally this
feeds.

**0.3 `kappa_window` floor-gate status — confirmed never gated, at any
r, by direct code trace.** `floor_gate()` (`run.py:238`) is called exactly
three times in the file: lines 586/587 (`i_e_wide156`, `i_e_point156`) and
675 (`i_e_wide312`). **It is never called on `win_e156`, `win_a156`,
`win_e312`, or `win_a312`** — the four `window_stats()` outputs that
directly construct `kappa_window_156`/`kappa_window_312`
(`run.py:571-573, 666-668`), the two values that alone produce P2's
monotonicity verdict and P3's `shape_ratio=19.79` headline. `window_stats()`
itself computes `min`/`max`/`std` alongside `mean` (`run.py:233-235`); none
of the three unused fields is ever read, printed, or persisted at any r.
**Confirmed independently, matching PHOTONICS/EM/THERMODYNAMICS exactly —
zero disagreement across four independent traces of the identical code
(three Phase-5 seats plus this one).**

**0.4 r=312 raw window/point-channel data — confirmed discarded, by direct
dict-key comparison.** `results.json::r312` (when `r312_committed=True`)
carries only `p2, p2_reversals, p4, nyquist_tier, quintiles, committed`
(`run.py:853-855`) — no `wide_channel`, `point_channel`, `delta_phi_wide/
point`, `floor_gate_wide/point`, and no `win_e312`/`win_a312` means at all,
unlike r=156's explicit `wide_channel=wide156, point_channel=point156,
...` (`run.py:845-852`). Line 673 (`k_p, _, _ = kappa_region_point(...)`)
throws away the two raw intensities with underscores. **Confirmed
independently, matching PHOTONICS and QUANTUM exactly.**

**0.5 P3b — confirmed silently dropped, by direct grep of all three
governing documents.** `grep -in "P3b"` across `NOTES.md` and `run.py`:
**zero hits in either.** `phase1_proposal.md` pre-registers P3b explicitly
(§4: "this cycle's own genuinely new prediction, not in T8's own
structure... materially informative for T13 either way") with a stated
falsifiable sign test (`B>0` = right-direction, non-replication of T14;
`B<0` = replication of T14's wrong-direction pathology). The underlying
number **is** computed and persisted: `results.json::p3.model_A_B =
0.007011298903800396` — positive. **Confirmed independently, matching
PHOTONICS exactly: a pre-registered, self-described "genuinely new"
falsifiable prediction disappeared between Phase 1 and the frozen
Predictions/Result text, with its own answer sitting unstated in the
persisted record.**

## 1. Ruling on each Phase-5 review's findings

**PHOTONICS (CONFIRM-WITH-GAPS) — ADOPT in full.** The `shape_ratio≡2^n`
identity and its n≈4.31 implication (§0.1), the never-floor-gated
`kappa_window` finding (§0.3), the discarded r=312 raw intensities (§0.4),
and the silently-dropped P3b (§0.5) all independently reconfirm exactly.
No override.

**MATERIALS (CONFIRM-WITH-GAPS) — ADOPT in full.** The geometry/thermal
table re-derivation is airtight (independently reconfirmed in §0.2 above
for the one figure that doesn't hold). The growing-electrical-thickness
alternative mechanism (2.4λ→9.6λ at fixed `τ_shell`) is a genuine,
previously-unnamed candidate for P3's own collapse, distinct from and
additive to the geometric z/z_R hypothesis NOTES.md's own Next item 1
already names — and MATERIALS is correct that an already-built control
(exp-052's fixed-absolute-thickness variant, the SAME article T14's own
Iteration-29 finding already used to distinguish self-similar-scaling
pathology from absorber-family-general behavior) directly discriminates
the two hypotheses at near-zero marginal cost. The blanket-UNOBTANIUM
precision gap (bench-scale 1.44–5.76µm vs. the scaling law) is real and
correctly scoped as a documentation gap, not a wrong conclusion. No
override.

**ELECTROMAGNETISM (CONFIRM-WITH-GAPS) — ADOPT in full.** Independently
re-hand-verified the settling-leg margin claim myself against
`results.json::r156.settling` (5-point spot check, x=682/708/734/760/786):
`rel_change` and `phase_diff` reproduce the stored values to the last
printed digit at every point checked, confirming EM's own full-53-point
statistics (max 1.380e-2 vs 0.20 tolerance, max 6.73e-3 rad vs 0.20 rad) —
a landslide pass, not a narrow one, matching PHOTONICS' independent
confirmation. **The sharpest finding in this cycle's entire Phase-5 layer
is EM's own §4**: `p4_156_trusted` (`run.py:632`) is real, working
risk-propagation machinery, gating P4's r=156 verdict on both the settling
leg AND the Nyquist tier — but `p3_result["verdict"]` is unconditionally
`"SCORED"` whenever `r312_committed` (`run.py:696-718`), with no reference
anywhere to `nyq312` or any settling flag, even though P3's own headline
number, `kappa_window_312`, is a RAWER, LESS-residualized read of the
identical r=312 capture than P4's `residual_point=point−wide` construction
(which partially self-cancels a slowly-varying transient by subtraction).
Confirmed directly: `results.json::p3` carries no `nyquist_tier` field,
while `results.json::r312.nyquist_tier` is populated one level up and
simply never read by the P3 scoring path. **ADOPT — this asymmetry is
real, independently reconfirmed, and is this cycle's single most
consequential code-level gap**: a reader of `NOTES.md`'s own Result
section sees P3 reported as "SCORED — the headline, genuinely surprising
finding" with zero qualification, three paragraphs before the
structurally-analogous P4 r=312 reading is correctly flagged
reduced-confidence. No override.

**QUANTUM OPTICS (CONFIRM-WITH-GAPS) — ADOPT in full.** The T1:N/A
disposition is airtight — re-confirmed independently by direct read of
`_run()` (two static `materials.*` calls, one source, one `sim.run`,
nothing intensity- or time-dependent anywhere in the path) — nothing
non-classical could have entered this cycle's pipeline regardless of how
extreme `kappa_window(312)=4.79e-6` looks. The `predicted_ripple_period`/
`nyquist_margin` re-derivation (§1) reproduces exactly, and the
fails-conservative argument against two concrete alternative aliasing
mechanisms (a fixed λ/2 standing wave; a domain-boundary echo scaling
with N(r)∝r) is sound — I could not construct a third alternative whose
period shrinks faster than 1/r either. The r=312 data-completeness gap
(§5, overlapping §0.4 above) is correctly scoped as non-load-bearing
(P4 at r=312 is already reported reduced-confidence regardless). No
override.

**VISION SCIENCE (CONFIRM-WITH-GAPS) — ADOPT in full, with one
classification refinement.** Independently confirmed the docstring/assert
mismatch by the identical grep (`run.py:40-45` claims "asserted present in
both PREDICTIONS_TEXT and RESULT_TEXT"; only one `assert DISCLAIMER in
result_text` exists, `run.py:831`). VISION frames this as a documentation/
code-enforcement gap against R23's own two-assert founding pattern
(exp-104's `run.py` had both); I add: this is also a real, if modest,
SECOND data point in the disclaimer-erosion lineage R23 itself was built
to close — a code-level regression from R23's own founding implementation,
not merely an unfinished scope extension the way R23's own founding-cycle
gap (Iteration 81) was. R23 carries no forward-elevating clause of its own
(unlike R16/R21/R22), so this does not auto-fire anything, but it is worth
naming for the Director: a third R23-lineage erosion instance, of any
shape, should prompt considering whether R23 needs one. VISION's κ↔C
scope-boundary arithmetic (§3: C=κ−1 saturates to |C|>0.98 already at
r=78, so the ~1,100× total `kappa_window` collapse buys only ΔC≈0.018 —
saturating, threshold-irrelevant) is independently sound: Weber contrast
is bounded in [−1,0], and once κ≪1 the loosest possible C-mapping is
already deep in the saturated regime, so no reading of this cycle's result
bears on constraint-3 even under the most generous unit conflation. No
override.

**THERMODYNAMICS self-review (CONFIRM-WITH-GAPS + one self-found defect)
— ADOPT in full, including the finding against this seat's own prior
work.** §0.2 above independently reconfirms the dominance-ratio citation
error exactly, confirms it does not survive into `NOTES.md`, and confirms
THERMODYNAMICS' own re-derivation of the r=156 row and the `ΔT_ss∝r_out`
claim (both hold to <0.2%, correctly re-phrased). **THERMODYNAMICS' §4
finding — that P3's collapse is a legitimate reason to raise, not lower,
confidence in the `Q_ext`-invariance placeholder, for a specific
construction-level reason (a fixed-offset window vs. a self-similarly
SCALED extinction box), not a blanket "a nearby channel misbehaved"
argument — is the most substantive physics contribution across all six
reviews and is adopted whole**, including the previously-uncited
exp-030 T11 `Q_ext` two-point precedent (+0.58% drift under an actual
κ=2 measurement on a self-similarly-scaled box, corroborating but not
proving invariance for this cycle's own `graded_black_shell` construction).
No override.

**Does this seat's own §3 finding hold against MY prior work?** Directly
verified against `phase2_redteam_audit.md` §0.2/attack 4 (quoted in full
above, §0.2): my own text states *"I independently re-derived the
underlying physics... 1949× at r=78, 487× at r=312, per the proposal's
own Appendix output, independently re-checked against the function's own
`dp_dt` formula"* — and reproduces the identical wrong digits. **Confirmed:
THERMODYNAMICS' claim against my own prior audit is correct. My own
Phase-2 audit's stated verification did not actually recover the correct
number, despite claiming to.** This is disclosed plainly in §2 below,
not minimized.

## 2. New defect none of the six caught: Gate P1 never touches the actual
## headline-metric anchor, `kappa_window_78`

Traced independently, not prompted by any of the six reviews. `run.py`'s
Gate P0/P1 pair is this cycle's own stated "ground-truth-recovery
precondition" — the Grounding Note and §4/Gate-P1 text both frame it as
covering "every one of exp-103/104's own established constants" before
any r=156/312 reading is trusted. Traced exactly what each gate touches:

- **Gate P0** (`run.py:494-510`) compares `geom(78)`'s **geometric**
  constants only (`N, CX, CY, SRC_X, STEPS, R_CORE, sigma_max, behind
  window bounds, dense_x`) against `exp104["geometry"]` — dimensions, not
  measured field values.
- **Gate P1, rescoped** (`run.py:536-547`) recomputes `kappa_region_wide`
  at all 16 `all_x_78` points from `exp104`'s own persisted
  `i_e_wide78`/`i_a_wide78` scalars and checks the division against the
  stored `wide78` values — this is the **wide-channel** self-consistency
  check the mandatory-fix-3 rescoping (Red Team's own Phase-2 finding)
  correctly narrowed the evidentiary claim for.

**`kappa_window_78 = exp103["kappa_window"]["value"]`** (`run.py:529`) —
loaded directly from a **different experiment's** `results.json`
(exp-103, not exp-104) and used, completely unverified by any gate this
cycle runs, as: (a) the r=78 anchor for P2's monotonicity test
(`kappa_window_78 > kappa_window_156 > kappa_window_312`), and (b) the
held-out validation point BOTH candidate models in P3 are scored against
(`missA`/`missB` in `run.py:706,711`, and `shape_ratio` itself,
`run.py:712-713`). **Neither Gate P0 nor Gate P1 recomputes, cross-checks,
or even re-reads `kappa_window_78` from raw fields — it is the single
scalar this cycle's own two headline metrics (P2, P3) depend on most
directly, and it is the one scalar this cycle's own "ground-truth-recovery
precondition" machinery never touches.**

I confirmed the underlying construction is legitimate — `window_stats()`
in exp-105 (`np.abs(ez)**2` mean over the BEHIND box) is byte-identical to
exp-103's own `window_stats()` (`experiments/103-.../run.py:167`,
`win_article["mean"]/win_empty["mean"]`), and the Phase-1 proposal's own
window-anchor re-parameterization is verified algebraically identical to
exp-103/104's window at r=78 — so `kappa_window_78=0.018336958179764707`
is very likely correct. **The gap is not that the number is wrong; it is
that this cycle's own stated "every reused constant is ground-truth-
verified before being trusted" discipline (Gate P0/P1, R6/R15 lineage)
does not, in fact, extend to the one reused scalar the headline findings
depend on most.** This is a genuine, previously-uncaught precondition gap,
not a restatement of any of the six reviews' findings (none discusses
Gate P1's actual coverage boundary relative to `kappa_window_78`
specifically) — flagged forward as Tier 1 material, §5 below.

## 3. R20 tally — explicit count and ruling

Per R20's own text: fires automatically on **three or more independent
R4-class defects** (a claimed-exact figure, citation, label, or
coincidence that does not reproduce from its own cited source) **surviving
a document's own Phase-3 prediction-freeze into its Result/Learned
sections**, each caught only at Phase 5.

Every candidate this cycle's six reviews and this audit surfaced, sorted
by whether it is (a) R4-shaped at all, and (b) present in `NOTES.md`'s own
frozen Result/Learned sections:

| Candidate | R4-shaped? | In NOTES.md Result/Learned? | Counts toward R20? |
|---|---|---|---|
| `z_over_zr` doubly-wrong hand-typed figure (Phase-1 §5) | Yes | No — caught blind at Phase 2, corrected before Phase 3 froze | No (pre-freeze) |
| Dominance-ratio 1949×/487× (Phase-1 §6, repeated in this seat's own Phase-2 audit §0.2) | Yes | No — confirmed by direct grep, §0.2 above | No (pre-freeze) |
| Docstring claims two-assert coverage; only one exists (VISION) | Arguably R18-shaped (a check's claimed scope vs. actual code), not R4-shaped (no numeric figure/citation) | No — lives in `run.py`'s docstring, not NOTES.md prose | No (wrong location + wrong class) |
| P3b silently dropped (PHOTONICS) | No — R21-shaped (a finding never stated in prose), not a wrong-number citation | Absent from NOTES.md by omission, not misstatement | No (wrong class) |
| `kappa_window` never floor-gated (PHOTONICS/EM/THERMODYNAMICS) | No — an instrumentation-completeness gap | N/A | No (wrong class) |
| r=312 raw data discarded (PHOTONICS/QUANTUM) | No — data-completeness gap | N/A | No (wrong class) |
| P3 lacks P4's risk-propagation gate (EM) | No — a code-symmetry gap | N/A | No (wrong class) |
| Gate P1 never touches `kappa_window_78` (this audit, §2) | No — a precondition-coverage gap | N/A | No (wrong class) |

**R20 tally: 0 defects meet both the R4-shape test AND the
survived-Phase-3-freeze-into-Result/Learned test.** THERMODYNAMICS' own
ruling on its own defect is independently confirmed correct by direct
grep (§0.2). **R20's three-or-more bar is not met — not close, by the
strict, correct reading of its own text: the count is zero, not one.**

**On the "does it count once or twice" question, reasoned explicitly.**
The dominance-ratio error is ONE root-cause numeric mistake (one wrong
computed ratio, most likely a single dropped `ε` factor, §0.2) that
appears in TWO documents: `phase1_proposal.md` (where it was authored)
and `phase2_redteam_audit.md` (where this same seat, one phase later,
restated it while explicitly claiming an independent re-check). For R20's
own counting purpose — which tallies **distinct erroneous claims/figures**,
not documents repeating them (consistent with the R4 Iteration-50
addendum's own precedent, where two Phase-5 seats independently repeating
the identical false "144/144" figure was treated as one recurring failure
SHAPE justifying a rule tightening, not as two separate R4 instances) — I
rule this **counts once** as a content-level defect. It does NOT count
twice toward any tally, including R20's. But the fact that it appears
TWICE, in two independent documents, is itself informative in a different
way: it is not merely an authoring slip, it is a **verification-layer
failure** — the specific duty the R4 Iteration-50 addendum imposes
("an aggregate flag... is not sufficient... independently checked, by the
cycle that first publishes the claim AND by any later Phase-5 reviewer
re-verifying it") was extended by this program's own convention to Phase-5
reviewers explicitly; this is, as far as this audit can determine, the
**first known instance of a Phase-2 Red Team audit's own "independently
re-derived"/"independently re-checked" language failing the identical
way** the Iteration-50 addendum was built to catch in Phase-5 reviewers.
Recommend, as a forward note (not a firing, not a new numbered rule this
cycle — one instance does not yet meet this program's own
recurrence-before-ratification bar): a future Red Team Phase-2 audit
whose own "independently re-derived" language is later found, at Phase 5,
to have reproduced rather than caught a Phase-1 error should be logged
explicitly against this same pattern, and a second instance would be
grounds for extending the R4/Iteration-50 addendum's text to name Phase-2
Red Team audits alongside Phase-5 reviewers.

## 4. Checkpoint criterion 4 — explicit ruling

**Does NOT fire.** Reasoned against each live sub-question:

1. **R20's own bar**: not met (§3 above) — zero, not three, R4-class
   defects survive Phase-3 freeze into Result/Learned.
2. **T1/constraint-3 quietly dropped?** No. T1 is correctly, repeatedly
   N/A (independently reconfirmed, QUANTUM's §4 and my own read of `_run()`
   agree exactly — nothing non-classical is expressible in this pipeline
   regardless of outcome magnitude). Constraint-3/4 scoring is explicitly
   declined in three separate sections (T1 statement, Idealizations,
   DISCLAIMER), and VISION's own §3 goes further than any prior cycle on
   this sub-thread by *quantifying* why P3's own dramatic collapse carries
   ~zero constraint-3 information under even the loosest unit mapping —
   the opposite of a quiet drop; a proactive scope-boundary finding.
3. **Unfalsifiable claims presented as decisive?** No. P5's own numeric
   bands were pre-demoted to descriptive-only at Phase 3 (mandatory fix 9,
   MATERIALS' independent Phase-5 confirmation that only the two SCORED
   booleans — classification-stays-UNDETECTABLE, margin-monotonic-decline —
   ever gate anything in `run.py`'s own logic). P3's own SCORED verdict is
   a real number against real pre-registered bands (85.55%/75.93% miss,
   catastrophically outside 25%/60%) — a clean FALSIFIED-against-both-
   candidates result, not an unfalsifiable one; the gap EM found is a
   missing *confidence qualifier* on an otherwise falsifiable, already-
   scored claim, not an unfalsifiable claim standing unflagged.
4. **R16/R21/R22's own forward-elevating clauses** — checked each
   explicitly. R16 (disclaimer-travels-but-field-not-persisted): does not
   apply — this cycle's data-completeness gap (§0.4) is a genuinely
   different shape (data never computed-and-persisted at all for a
   channel with no disclaimer obligation attached, not a disclaimer
   outrunning an uncaptured NETD field). R21 (persisted-sidecar-finding-
   never-narrated, two founding instances on the NETD channel already on
   record): does NOT fire a third time — P5's own NETD classification
   and margin-decline finding ARE stated inline in `NOTES.md`'s Result
   section this cycle (independently confirmed by both MATERIALS and this
   audit's own read), the channel R21 is specifically scoped to. P3b's
   disappearance is R21-*shaped* one level upstream (a whole
   pre-registered prediction rather than a persisted sidecar byproduct)
   but is not a third instance of R21's own specifically-scoped clause —
   PHOTONICS is correct not to assert this fires anything, and I concur.
   R22 (frozen vector sign): not engaged this cycle — no vector
   self-consistency identity of that kind exists in this document.
5. **All findings caught blind, within this cycle's own six-seat-plus-
   Red-Team review layers, before this LOGBOOK entry** — matching every
   prior rule's own unbroken non-firing precedent for a same-cycle catch
   (R4 through R23, all of them). No defect here was inherited unfixed
   from a prior cycle's own already-fixed machinery (the strict "known,
   named, ignored" bar R6/R11's lineage reserves for automatic firing).

**Standing forward caution, named explicitly rather than left implicit**
(matching this program's own convention for "closest non-firing call"
rulings): two independent process signals this cycle are each, on their
own, below any firing threshold, but worth the Director's attention
together: (a) the Red-Team-Phase-2-audit-repeats-a-wrong-figure pattern
(§3) — a first-of-its-kind instance, one data point, not yet a recurrence;
(b) R23's own two-assert founding pattern lost one assert this cycle
(§1/VISION) — a second data point in the disclaimer-erosion lineage,
code-level this time rather than prose-level, R23 itself carrying no
forward-elevating clause yet. Neither fires anything now; a further
instance of either should be logged explicitly against these patterns.

## 5. Combined Verdict: PARTIAL

**Not RULED OUT** — no mechanism class is foreclosed (T1:N/A throughout,
correctly), and the substantive science this cycle delivers is real and
non-trivial: the r=78→156 leg is genuinely clean (Gate P0 exact, Gate P1
rescoped exact, settling PASS with 14.5×/30× margin, Nyquist TRUSTED, P4
TRUSTED), P5's thermal-detectability finding independently reproduces
exactly and correctly narrates through to Result prose, and P3's own
accelerating-collapse discovery — whatever its ultimate explanation turns
out to be — is a genuine, previously-unasked, disclosed cross-channel
non-replication finding of real forward value (§0.1's `shape_ratio≡2^n`
sharpening only strengthens its status as a real, falsifiable anomaly
worth chasing, not a wash).

**Not PROMISING.** This program's own precedent on this exact
instrumentation lineage (exp-102, Iteration 79: PROMISING, one
non-load-bearing citation slip, R20 did not fire; exp-104, Iteration 81:
PARTIAL despite R20 tallying **zero** — "the substantive science is
strong... weighed against a real, same-shift-fixed cluster of framing/
evidentiary-strength/rule-scope gaps a clean CONFIRM would not carry")
draws the PROMISING/PARTIAL line at whether the cycle's own delivered
result is clean enough, net of its own gaps, to stand as this program's
next confirmed instrument reading — not merely at whether any single rule
fires. exp-105's own cluster is denser and more consequential than
either precedent: **the cycle's own headline, most-surprising finding
(P3, shape_ratio=19.79) is — by NOTES.md's own correct, R3-meta-rule-
compliant choice not to interpret it yet — explicitly unresolved, and
Phase 5 now shows it rests on zero floor-gating, no risk-propagation gate
symmetric to its sibling P4's, a Gate P1 that never touches its own r=78
anchor, and at least one genuine unconsidered alternative mechanism
(MATERIALS' growing-electrical-thickness hypothesis) with an
already-built, unused discriminating control.** None of this overturns
any of this cycle's four OTHER scored verdicts (P0, P1-rescoped, P2, P4
at r=78/156, P5 all independently reproduce clean, with wide margins where
margins were checked) — but the one result this cycle itself calls "the
headline, genuinely surprising finding" cannot yet be told apart from a
floor/dynamic-range artifact by this cycle's own instrumentation, which is
a materially different situation from exp-102's single cosmetic citation
defect. Six independent CONFIRM-WITH-GAPS verdicts (not one clean CONFIRM
among them, unlike exp-104's own THERMODYNAMICS-clean-CONFIRM outlier)
corroborate this reading. **PARTIAL**, for the same reason exp-104 earned
it: real, logbook-advancing science, correctly and honestly not
oversold, wrapped in a real cluster of gaps a clean CONFIRM would not
carry — here concentrated specifically on whether the cycle's own
headline number means anything yet.

## 6. Mandatory same-shift documentation fixes (Tier 0 — zero re-run, zero
## verdict change, apply before this cycle closes)

1. **Correct the dominance-ratio citation** in `phase1_proposal.md` §6 and
   `phase2_redteam_audit.md` §0.2/attack 4: `1949×`→`≈2160.6×`,
   `487×`→`≈540.1×` (or append a correction note to both, since they are
   historical Phase-1/Phase-2 documents — do not silently rewrite history;
   annotate). Non-load-bearing, does not touch `NOTES.md` or any scored
   verdict.
2. **Score P3b explicitly in `NOTES.md`**: state `model_A_B=+0.00701`
   (positive — the "right-direction" reading, a non-replication of T14's
   own wrong-direction-shallowing pathology on this structurally different
   coherent-intensity channel) in the Result and/or Learned section.
   Zero-cost, pure post-processing of an already-persisted field.
3. **Add PHOTONICS' `shape_ratio≡2^n`/`n≈4.31` characterization** to
   NOTES.md's Result or Next section, alongside the existing miss
   percentages — sharper, falsifiable, and a reusable diagnostic for any
   future doubling in this same bridge (κ=8, r=624, etc.).
4. **Add an explicit r=312 confidence caveat to P3's own Result-prose
   paragraph**, symmetric to P4's already-present one: state plainly that
   `kappa_window_312` (and therefore `shape_ratio`) shares r=312's
   MARGINAL-REDUCED-CONFIDENCE Nyquist tier and complete absence of a
   settling leg — the same disclosed risk P4's paragraph three lines later
   already carries for the identical underlying capture.
5. **Add a Gate-P1-scope note**: state explicitly that Gate P1 (rescoped)
   verifies only `kappa_region_wide`'s r=78 self-consistency, not
   `kappa_window_78` — the actual anchor P2 and P3 both score against —
   so a future reader does not credit "Gate P0/P1 PASS" with more coverage
   than this cycle's own code provides (this audit's own §2 finding).
6. **Add VISION's constraint-3 scope-boundary note**: state plainly, once,
   near P3's own Result-prose paragraph, that `kappa_window`'s collapse —
   however dramatic in raw-ratio terms — corresponds to only ΔC≈0.018 under
   even the loosest naive `C=κ−1` mapping (already saturated past
   photopic threshold at r=78), and therefore carries no information
   bearing on constraint-3; cross-reference from T13/T14 if convenient.
7. **Restore R23's two-assert founding pattern**: add
   `assert DISCLAIMER in build_predictions_text(g78, g156, g312)` (or
   equivalent on the persisted `predictions_text` variable) alongside the
   existing `result_text` assert, and correct the module docstring's
   overclaim to match what the code actually enforces.
8. **Either write the required re-justification for the `delta_scene`
   R3-vs-R4 split, or execute it, at Iteration 83** — this cycle leaves it
   at SIX consecutive deferrals (NOTES.md's own Next item 5, quoting
   exp-104's own written warning); Iteration 83 is the point NOTES.md's
   own text already names as requiring explicit written re-justification
   or execution, not a silent seventh deferral.

## 7. Reconciled Iteration-83 queue

**Tier 0 — same-shift, zero-FDTD, apply now.** Items 1–8, §6 above.

**Tier 1 — highest priority, cheap-to-moderate FDTD, real cross-seat
convergence.** Independently ranked #1 or #2 by PHOTONICS, EM, and
THERMODYNAMICS, and cited as the load-bearing precondition by QUANTUM —
four of six seats converge on the same core action:

1. **Floor-gate `kappa_window`/`window_stats()`'s own output at every
   already-captured r (156, 312), using the identical `FLOOR_FRAC=0.10`-
   of-RMS convention already applied to the wide/point channels, and stop
   discarding the r=312 point-channel raw intensities (persist
   `wide_channel`/`point_channel`/`win_e`/`win_a` means for r=312 the same
   way r=156 already does).** Zero marginal FDTD cost if the r=312 field
   arrays are still available this shift; otherwise one re-run of the
   already-inexpensive (1867.5s pilot) r=312 pair. This is the single
   load-bearing precondition for trusting or refuting P3's own
   accelerating-collapse finding as physics rather than partly a
   floor/dynamic-range artifact — NOTES.md's own top-ranked Next item,
   now given a concrete, already-available mechanism to close it with.
2. **A settling-independence leg on `kappa_window` itself** (not merely
   `kappa_region_point`, already done) **at r=156, and — more urgently,
   given the MARGINAL Nyquist tier already there — at r=312.**
   `kappa_window` has never been settling-tested at any r in this
   program's history; this cycle's own mandatory-fix-3 leg tested a
   structurally different (residual, partially self-cancelling) channel.
3. **Gate P3's own scored verdict on r=312's Nyquist/settling status,
   symmetric to the already-built `p4_156_trusted` pattern** — a cheap,
   mechanical code fix (one boolean, propagated into the `p3` dict and
   `result_text`'s own P3 paragraph) closing the risk-propagation
   asymmetry this audit and EM both independently found.
4. **Re-run the `kappa_window`/P3 bridge on exp-052's existing
   fixed-absolute-thickness `graded_black_shell` variant at r=156/312** —
   MATERIALS' own newly-identified, already-built, zero-new-mechanism
   discriminator between the geometric-window (z/z_R) hypothesis and the
   growing-electrical-thickness materials hypothesis for the accelerating
   collapse. Should reuse items 1–3's own machinery (floor-gated, settling-
   checked, risk-gated) from the start, not retrofit it after.

**Tier 2 — important, sequenced after Tier 1 resolves whether P3's
collapse is trustworthy.**

1. A fourth r-point (e.g. κ=2.83, r≈221, the geometric mean of 156/312) to
   break the two-point degeneracy in the shape fit and test whether the
   implied n≈4.3 exponent is stable (a genuine, if unexpectedly steep,
   near-field law) or itself compounding (a regime transition or
   accumulating artifact) — PHOTONICS' own top-3 pick, correctly ranked
   behind the floor/settling preconditions.
2. A real, measured `sections.widths()` σ_ext(r) trend, replacing the
   `Q_ext`-invariance placeholder — re-ranked to THERMODYNAMICS' own #1
   given P3's finding sharpens (not just the realizability reason MATERIALS
   originally gave) the case for verifying rather than assuming this
   invariance; build with a genuinely self-similarly-scaled box (per T8's
   own `beam_geometry(r)` convention, not a fixed offset), cross-check
   against exp-030's own T11 `Q_ext≈1.51→1.52` two-point precedent, and
   floor-gate the result before trusting it.
3. Split the blanket "UNOBTANIUM-WITH-PARAMETERS at every r" tag into two
   explicit sentences — the r-family's own scaling law (genuinely
   unobtainium as κ grows toward witness scale) vs. each committed
   geometry's own absolute-thickness realizability (1.44–5.76µm, plausibly
   within this program's already-cited µm–mm real-coating range) —
   MATERIALS' cheap, zero-FDTD precision fix against future over-reading.
4. Pin VISION's κ↔C scope-boundary finding (§1/§6 item 6 above) as a
   standing, cited note or LOGBOOK T13/T14 cross-reference, not merely a
   one-off review paragraph — preventing any future citation of
   "shape_ratio=19.79" from being misread as constraint-3-relevant.

**Tier 3 — standing, deferred, unchanged this cycle.**

1. The oblique-angle extension of this same θ=0°-validated bridge
   (deferred explicitly at Phase 1, still open).
2. **The `delta_scene` R3-vs-R4 split — now SIX consecutive deferrals;
   per NOTES.md's own already-committed text, Iteration 83 is the point
   requiring explicit written re-justification or execution**, not a
   silent seventh deferral (Tier-0 item 8, §6, restated here for queue
   visibility).
3. The other two Reconciled Iteration-82 Tier-1 items still open (R23's
   own scope decision — genericize vs. formally ratify single-disclaimer
   scope, now sharpened by this cycle's own second erosion data point,
   §1/§4; the near-null-exclusion raw-bin-identity refinement).
4. A doubled-STEPS settling spot-check at r=312's own near-field-closest
   `DENSE_X` point on the wide/point channels specifically (distinct from,
   and largely superseded in priority by, Tier 1 item 2's broader
   `kappa_window` settling leg, which should be built first and may make
   this item's own narrower scope moot).
