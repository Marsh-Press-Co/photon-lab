#### VISION SCIENCE — verdict: **CONFIRM-WITH-GAPS**

**Independent recomputation (R4/R9/R20 discipline)**

`kappa_window` (exact match to reported value, recomputed from raw article.mean/empty.mean), window-spanning span mean and ratio (exact), floor-gate RMS (matches to precision of manual arithmetic), one settling-independence relative change spot-check at x=356 (exact), and confirmed the 16-point `kappa_region` sequence is strictly increasing at every step (zero reversals). No arithmetic defect found anywhere I recomputed.

**Line-by-line disclaimer-propagation check (Result/Learned sections), per this cycle's own Phase-2 fix 8**

`grep`-verified locations of the mandated sentence ("kappa_window/kappa_region are raw physical intensity ratios; no Weber-contrast or C_thr(L) perceptual scoring is performed this cycle") in `NOTES.md`: **Setup** and **Idealizations** only. Zero occurrences in the **Predictions** section or anywhere in the **Result**, **Learned**, or **Next** sections. `run.py`/`run_output.txt` do carry the disclaimer as the very first printed block (good), but that is a separate artifact from `NOTES.md`'s own prose.

This is the exact, named, repeatedly-fired failure shape in this program's own history. `LOGBOOK.md` documents a T28 sub-thread ("disclaimer erosion") that fired Checkpoint criterion 4 on its fourth instance (Iteration 53/T16, exp-086, exp-087, exp-088/Iteration 65), resolved with an escalated standing rule: "the 'carried idealizations' banner is now required at BOTH the Predictions section AND the Result section of any future T28 committed-predictions document, since this cycle is direct, first-hand proof that a banner scoped to one section does not propagate to the other."

`experiments/103-t28-gateb-footprint-aperture-match/` is explicitly a T28 document with a committed-Predictions section under this program's house discipline. By the program's own standing rule, this cycle's perceptual-scoring disclaimer was required in **both** Predictions and Result. It appears in **neither**.

Per this program's own unbroken precedent (no arithmetic wrong, no gate bypassed, fixed same-shift), this does not undermine the physics result itself, and I found no place in Result/Learned where a perceptual claim is actually asserted (see below) — but the omission is squarely inside my seat's charter and this cycle's own named Checkpoint-4 exposure, and should be fixed same-shift rather than carried forward as a further instance.

**Findings**

1. **[load-bearing — program-integrity/Checkpoint-4, not physics]** The Phase-2 mandatory-fix-8 perceptual-scoring disclaimer is present only in Setup/Idealizations; it is absent from both the Predictions section and the Result section of `NOTES.md`, in direct tension with the standing "banner required at BOTH Predictions and Result" rule this program adopted specifically to close this recurrence pattern (LOGBOOK Iteration 65). Recommend the same one-sentence disclaimer be added inline to the Predictions section header and as the opening line of the Result section, same-shift, per house precedent.

2. **[non-load-bearing]** Close read of the Result and Learned prose for perceptual-adjacent language: "the clean Fresnel-fill-in signature," "fringe-limited near-field null," and "Gate B is now genuinely, honestly reproduced — not force-fixed" are all optics/instrumentation vocabulary describing a physical intensity-ratio trend and this program's own honesty-about-confounds convention, not human-visibility claims. I do not find an actual perceptual overclaim in Result/Learned. This is a genuine improvement over the Phase-1 proposal's original "shadow fills in"/"floor" language that Phase 2 correctly flagged — only the *placement* of the disclaimer (finding 1) did not follow through.

3. **[non-load-bearing — terminology-collision caution]** `floor_gate`/`FLOOR_FRAC` in this cycle is an FDTD denominator-conditioning/SNR gate, sourced only to internal "R13/R14 lineage, house style" convention — unrelated to this program's separate, sourced perceptual "δ_C floor" gating Weber-contrast measurements in the T3/ambient-appearance line. `NOTES.md` itself never conflates them, but a future citation skimming for "floor" language in a T28 vs. T3 context could. Worth a one-clause disambiguation if this figure is ever cited outside this document.

4. **[non-load-bearing]** No predicted band, tolerance, or threshold in this cycle rests on any assumed human detectability figure — all four are internal numerical/physical-consistency criteria with their own provenance. Nothing needed pinning under my charter that wasn't already either sourced to program precedent or explicitly disclaimed as absent.

**Argued next change:** Same-shift, add the exact mandatory-fix-8 disclaimer sentence as the first line of the `## Predictions` section and as the opening line of the `## Result` section of `NOTES.md` (mirroring `run_output.txt`'s own already-correct placement) — the cheapest possible fix, directly discharges the recurring T28 disclaimer-carry-forward pattern this program has now named a standing rule against.
