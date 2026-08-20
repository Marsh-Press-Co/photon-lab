# PHASE 5 — REVIEW (MATERIALS & METAMATERIALS) · Panel Iteration 28 · exp-051

*Fresh sub-agent, zero prior context. Read `PANEL.md` in full, `LOGBOOK.md`
in full (~9843 lines, LIVE THREADS T1–T24, ESTABLISHED, RULED OUT R1–R4,
Iterations 26/27 in full), and the complete exp-051 record in order:
`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`,
`design_geometry.py`, and `results.json`. Blind to any other seat's Phase-5
review this cycle and to any prior `phase5_review_*`/`phase5_redteam_audit.md`
in this experiment's directory (none existed to read). Every load-bearing
number below was independently recomputed from `results.json`'s raw
`per_combination` records with fresh from-scratch code (own rank-correlation
implementation, not scipy, not any seat's scratch code), or by re-running
`design_geometry.py` directly — never taken on the write-up's word.*

## 1. My specific duty this cycle: is the Iteration-29 trigger intact?

**Yes — correctly and bindingly recorded, in both places that matter, and not
softened.**

I did not take the task's framing on faith; I re-traced the citation chain
myself against `LOGBOOK.md`:

- Line 4777 (Iteration 8 close): *"MATERIALS' own queued Iteration-7 item"* —
  first queued.
- Line 9192 (Iteration 24/25 close, exp-047→exp-048): ranked item (5), "eight-
  iteration-deferred."
- Line 9426 (Iteration 26 close, exp-049): ranked item (4), "now a 9-iteration
  deferral."
- Line 9658 (Iteration 27 close, exp-050): ranked item (4), "now 9+ iterations
  deferred across two consecutive instrument-fidelity cycles."
- Line 9837 (Iteration 27 close → Iteration 28 queue, `PLAN.md:1400`): ranked
  item (4) again, "now ten-plus-iteration-deferred," feeding into this cycle
  (exp-051, Iteration 28).

That is first-queued-at-7, re-ranked-without-being-reached at 25, 26, 27, and
28 — a 21-iteration span (28−7), reached the top of a cycle's actual budget
zero times. My own seat's Phase-2 critique this cycle (`phase2_critique_
materials.md`) independently made the same count and asked for "an
unconditional Iteration-29 trigger for item (4)... not another re-ranking,"
explicitly citing the r=156 precedent (queued Iteration 3, committed
unconditional trigger only after its fourth deferral, Iteration 10 close,
LOGBOOK line ~5201/5427).

Red Team's audit (`phase2_redteam_audit.md`, closing section, "Ruling on
MATERIALS' scope-drift flag") **independently re-verified this exact chain
from source** (not on MATERIALS' word) and ruled: *"YES — unconditional
Iteration-29 trigger, adopted, not a fourth re-ranking... Iteration 29 builds
and measures the fixed-absolute-thickness `graded_black_shell` variant's own
`C`, unconditionally — not contingent on Iteration 28's own findings, not
subject to a further ranked-list competition against items (2)/(3)/(5)/(6)."*

**Critically, the Director did not merely note this — Phase 3 §3 states it as
a binding, accepted ruling, in language stronger than "another ranked item":**

> "Red Team's scope-drift ruling is also ACCEPTED and binding: Iteration 29
> builds and measures the fixed-absolute-thickness `graded_black_shell`
> variant's own `C`, **unconditionally** — not contingent on this cycle's
> findings, not subject to a fifth ranked-list competition."

This is the identical binding form the r=156 trigger took at its own
Iteration-10/11 close ("Iteration 11 builds it unconditionally... do not
defer a fifth time"), and Phase 3 draws that comparison explicitly, not
implicitly. I checked for exactly the failure mode the task asked me to
check for — the trigger being quietly re-absorbed into an ordinary ranked
list — and it is not present: item (4) is stated twice, verbatim,
"unconditionally," "not contingent," "not subject to" competition, once by
Red Team and once by the Director adopting it. `phase1_proposal.md` and
`phase2_critique_materials.md` correctly stand unedited as the historical
record (house "flag, don't rewrite" convention), and the binding language
lives in `phase2_redteam_audit.md` and `phase3_synthesis.md` §3, not buried
in a subordinate clause.

**One live risk, not yet a defect, flagged for whoever closes this cycle's
own Phase 5 into `LOGBOOK.md`/`PLAN.md`:** `PLAN.md`'s current Iteration-28
queue entry (`PLAN.md:1400-1403`) still reads item (4) in the same "ranked
item, independently re-ranked again" prose the last three cycles used — that
is expected, since Phase 5 (and the LOGBOOK/PLAN.md close it feeds) had not
run yet when I read it. But it means the unconditional framing currently
exists only in this experiment's own Phase-2/Phase-3 files, not yet in the
program's persistent memory. **Whoever writes this cycle's LOGBOOK/PLAN.md
close must carry the literal word "unconditional" and the "not a fifth
ranked-list competition" framing forward**, matching the r=156 precedent's
own close language, not silently reduce it back to "(4) fixed-absolute-
thickness variant, N+1 iterations deferred" the way the last three closes
did. That reduction is exactly how a correctly-adjudicated trigger could
still end up softened one level down, in the one place (LOGBOOK.md) every
future cycle actually reads.

## 2. Substance verdict — independently re-derived, not read off the page

**PROMISING.** I ran fresh code against `results.json`'s raw
`per_combination` array (216 rows) rather than trusting `NOTES.md`'s Results
table, and every load-bearing figure reproduced exactly:

- **P-ALIAS-0 anchor**: ran `design_geometry.py` directly — the printed
  spot-check (θ=38°, 600nm, `corrected`, `GEOM_EXP042_OLD`) gives
  `-0.0030314658103897194`, bit-identical to `results.json`'s own anchor row
  and to exp-042's committed module-global.
- **P-ALIAS-1** (Spearman ρ, `log10|E_pred|` vs `log10|C41−C81|`, 198
  out-of-sample rows): my own from-scratch rank-correlation implementation
  gives **ρ = 0.7380435856068439** — matching `results.json`'s
  `predictions.P_ALIAS_1.spearman_rho` to every printed digit. **PARTIAL**
  confirmed (band 0.60–0.85).
- **P-ALIAS-2** (unfitted-threshold classification): my own confusion-matrix
  count gives tp=12, fp=0, tn=176, fn=10 → accuracy 0.9494949…,
  sensitivity 0.5454545… (12/22), specificity 1.0 — exact match. **PARTIAL**
  confirmed.
- **P-ALIAS-3** (81 GEOM78 FWHM≤10° rows): 0 false positives, independently
  counted. **CONFIRMED.**
- **P-ALIAS-4** (108 A=752 rows, 16 positives): accuracy 0.9537037…,
  sensitivity 0.6875 (11/16) — exact match. **CONFIRMED.**
- **P-ALIAS-5** (9 A=752 FWHM=20° cells): reconstructed the per-cell
  `abs_ghat1_corrected/abs_ghat1_incoherent` and `dabs_corrected/dabs_
  incoherent` ratios directly from the raw rows — bit-exact against every
  entry in `results.json`'s `predictions.P_ALIAS_5.per_cell` table (median
  1.9196813367691077 / 1.9211428676381699). **CONFIRMED.**
- **P-ALIAS-7**: 188/198 exact `n*` match, independently counted.
  **CONFIRMED.**
- **The located `coherent`-vs-rest split** (NOTES.md Reading): I split the
  198 out-of-sample rows myself — non-`coherent` (126 rows): ρ=0.9788106…,
  `coherent` (72 rows): ρ=0.3024953…, coherent sensitivity 4/14 — all exact
  matches to the Reading section's own "ρ=0.979... ρ=0.302... 4/14."

This is a clean, complete, independent reproduction — every scored number in
`NOTES.md`'s Results table checks out from the raw per-row data, not merely
from the summary the write-up presents. The gate (`P-ALIAS-0`) passed, the
completeness ledger is 1080/1080, and `timing.json` corroborates the
disclosed ≈5.1-minute scored-sweep / ≈13-minute total-shift cost with Red
Team docket item 9's process-start timing hook actually present (verified: a
real `timing.json` exists with `proc_start_unix` captured at import).

The substance itself holds up: exp-050 left two genuinely open questions
(what predicts tier instability; what explains the ~1.9–2.3× convention
asymmetry), the Phase-1 crux quantity was correctly killed at the desk by
four independent blind seats before a single FDTD-adjacent run, and the
replacement (QUANTUM's alias-lattice mechanism, adopted per Red Team's
ruling) answers both — cleanly for `incoherent`/`incoherent_corrected`
(P-ALIAS-3/4/7 all clear their CONFIRMED bars with margin), and with a real,
mechanistically located boundary for `coherent` (whose complex-field-sum
convention breaks the exact sampling identity, `beam_divergence_* ≡
Σwᵢc(θᵢ)/Σwᵢ`, the predictor is built on — not a residual mystery, a named,
disclosed limit). The Director's own mid-cycle override (moving every scored
prediction off the 18 pre-checked rows onto 198 untouched ones, after Red
Team's own docket had those 18 as the scored set) is, on my own reading, the
correct call and a genuine strengthening — Phase 2's own pre-checks (QUANTUM,
then Red Team) had already computed AUC=1.000 on those 18 rows before Phase 3
froze anything, so scoring against them would have been transcription. The
out-of-sample design is harder on the mechanism, not softer, and it still
passes (5 CONFIRMED / 2 PARTIAL / 1 REFUTED, 0 hard-falsified).

No `REALIZABILITY_MEMO.md` exposure: grep-confirmed zero hits for
`beam_divergence`/`gaussian_angle_weights`/`alias_coeff`/`edge_diffraction`
anywhere in `experiments/034-.../REALIZABILITY_MEMO.md`. This cycle cannot
move a realizability tier and does not claim to. T1 escape route: NONE,
correctly stated and correctly upheld throughout — no material law, no σ, no
new source, nothing my charter needs to bound.

## 3. A defect I found, independently, not inherited from any seat's Phase-2 review

**NOTES.md's Reading section overstates what the out-of-sample P-ALIAS-5 test
actually demonstrated, by importing an anomaly from a different, unscored
dataset.**

The Reading section reads: *"P-ALIAS-5 closes exp-050's second open question
cleanly. The alias-frequency spectral-amplitude ratio reproduces the measured
Δabs-ratio at the 9 out-of-sample A=752 FWHM=20° cells (ρ=0.933, median 1.920
vs 1.921) — including... the correct reproduction of the one cell where the
ratio inverts below 1."*

I checked this directly against `results.json`'s own `predictions.P_ALIAS_5.
per_cell` table (all 9 A=752 rows, which I also independently rebuilt from
`per_combination` above). **None of the 9 scored A=752 cells has a ratio
below 1** — the range is [1.6558, 2.1369], all comfortably above 1, including
at (750nm, 38°) specifically (spectral_ratio 2.1153, measured_dabs_ratio
2.0945). The cell where the ratio genuinely inverts below 1 (≈0.775–0.835,
confirmed by re-deriving it from `calibration_18_unscored.rows` at (750nm,
38°, `incoherent`/`incoherent_corrected`), where
`E_pred_m1_corrected/E_pred_m1_incoherent = -3.676e-5 / -4.742e-5 ≈ 0.775`)
lives **only in the calibration-18 block, at GEOM78 (A=724)** — a different
geometry, explicitly designated "reported, scored against nothing" earlier
in the same document, and already known to two seats (QUANTUM, Red Team)
*before* Phase 3 froze the out-of-sample predictions.

So the sentence claims the scored, out-of-sample P-ALIAS-5 test "correctly
reproduces" an inversion that (a) did not occur among its own 9 scored data
points, and (b) was never actually a held-out prediction to begin with — it
was Phase-2 pre-check knowledge, disclosed as unscored, at a different
geometry. The out-of-sample A=752 cells do show a real, milder version of
the same directional pattern this attack-4/Attack-5 lineage found
(750nm ratios run higher than 450/600nm, and the mechanism P-ALIAS-5 tests
is the same one) — but "the correct reproduction of the one cell where the
ratio inverts below 1" is not an accurate description of anything the 9
scored rows contain.

**This is not load-bearing** — P-ALIAS-5's own scored numbers (ρ=0.9333,
median ratio match) are correct and independently reproduce exactly; the
CONFIRMED verdict does not depend on the disputed sentence. But it is a real
instance of the exact failure class this program has repeatedly caught and
named (LOGBOOK Iterations 13, 14, 15, 17, 20, 21, 22, 23, 24, 25, 26: "the
document written to fix a prior overclaim itself ships a residual instance
of the same overclaim, one level down") — here inside the very Reading
section whose job is to state precisely what the out-of-sample test showed
versus what was already known going in.

**Recommended fix (cheap, same-shift, zero new computation):** reword the
clause to state plainly that the 750nm/38° inversion is a calibration-set
(GEOM78) fact already known from Phase 2, not part of what the 9 scored A=752
rows demonstrate, and that the out-of-sample cells instead show the same
mechanism's ratio staying directionally consistent (rising with λ) without
inverting at this geometry — a real, weaker, and accurate claim.

## 4. Ranked priorities

Per the Director's own binding ruling (§1 above, accepted in full), **Iteration
29's substantive proposal is item (4) — the fixed-absolute-thickness
`graded_black_shell` variant — full stop, not competing against a ranked
list.** What follows is only what should run *alongside* it as same-shift,
zero-cost riders, plus my own view of the standing queue for whatever cycle
follows Iteration 29.

1. **[Same-shift, zero-cost, this cycle's own close]** Apply the §3 fix
   above to `NOTES.md`'s Reading section — one sentence, no re-computation,
   closes the one defect I found before it can propagate into `LOGBOOK.md`
   the way the exp-049 "321" figure did two cycles ago.
2. **[Iteration-29 close discipline, not a new item]** Whoever writes
   Iteration 28's `LOGBOOK.md`/`PLAN.md` close must carry forward the literal
   "unconditional... not a fifth ranked-list competition" language for item
   (4), not the "(4) N-iteration-deferred, re-ranked again" phrasing the last
   three closes used — see §1's live risk.
3. **[Standing queue, resumes only after Iteration 29, my own charter
   ranking]** The genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry
   (Iteration-28 queue item 2) — this is the most realizability-relevant item
   still waiting, since it is now the *only* uncharacterized uncertainty
   source left on the program's sharpest contamination-risk cell family,
   after four consecutive desk cycles (26/27/28 plus this one) drained the
   convergence/aliasing side of that question to near-zero residual
   uncertainty. I rank it ahead of items 3/5/6 for the same reason MATERIALS'
   own Phase-2 critique this cycle ranked it: it is FDTD ground-truth, not
   another analytic-model audit, and this program's own instrument-fidelity
   run of cycles (20, 22, 23, 26, 27, 28 — six of the last nine) has been
   almost entirely the latter.
4. **[Lower priority, unaffected by this cycle]** Items 3 (sub-degree angular
   sweep) and 5 (THERMO's `h_eff` re-derivation) remain correctly queued
   behind item 2 on my own charter's reading — neither bears on
   realizability, and neither is urgent enough to justify preempting the
   FDTD `ABSORB` sweep a second time.

## Verdict

**PROMISING.**

The Iteration-29 trigger on my own seat's scope-drift flag is intact,
independently re-verified by Red Team from source, and bindingly recorded in
`phase3_synthesis.md` §3 — not softened into an ordinary ranked item, though
the persistent record (`LOGBOOK.md`/`PLAN.md`) has not yet been updated to
carry that binding language forward and must be watched at close. The
cycle's substance holds up completely under independent, from-scratch
re-derivation of every scored prediction (5 CONFIRMED / 2 PARTIAL / 1
REFUTED, 0 hard-falsified, gate PASS, ledger 1080/1080) — the alias-lattice
mechanism is real, generalizes cleanly to the incoherent family out-of-sample,
and fails specifically and explicably for `beam_divergence_coherent`, exactly
as the task description states. One new, non-load-bearing defect found: the
Reading section's P-ALIAS-5 discussion conflates a calibration-set (unscored,
different-geometry) inversion finding with what the scored out-of-sample test
actually showed — cheap to fix, does not touch any verdict.
