# PHASE 5 — REVIEW · Panel Iteration 26 · Seat: MATERIALS & METAMATERIALS

*Fresh-context review, blind to the other six seats' current-cycle Phase-5
output. Charter: sub-wavelength structure and realizability — published /
plausible / unobtainium-with-parameters. Read: PANEL.md, LOGBOOK.md in full
(RULED OUT, ESTABLISHED, T1–T24), `phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json`, `REALIZABILITY_MEMO.md` in full, and
PLAN.md's Current-state section. This cycle proposes no mechanism (T1
escape route: NONE) — it is a pure instrument-fidelity characterization, so
almost nothing here is optics/materials content proper. This review is
scored on the three questions the Director's brief actually assigned:
whether my own Phase-2 finding survived intact, whether any
`REALIZABILITY_MEMO.md` tier is at risk, and independent re-verification of
a sample of `results.json`'s numbers.*

---

## (a) Did my own Phase-2 Attack 1 survive Phase 3/4 honestly, not just get acknowledged and dropped?

**Yes — traced end to end, not taken on the write-up's word.**

My blind Phase-2 critique (`phase2_critique_materials.md`) flagged that
idealization 7 scoped this audit to exp-042/046's own `A=752, NY=1584`
geometry, explicitly excluding exp-048's re-parameterized `A=724, NY=1528`
fallback geometry — the geometry any *actual* near-boundary constraint-3 or
realizability-adjacent citation would use — and required a committed
follow-up trigger before any future citation could silently generalize an
A=752-measured n* to A=724. Red Team's audit (`phase2_redteam_audit.md`,
Attack 1) independently re-verified the code fact I cited
(`GEOM78 = dict(NY=1528, OBJ_Y=764, ABSORB=40,...)` ⇒ `A=724`, confirmed
directly against `experiments/048-.../design_geometry.py:145-149`) and
affirmed the attack as mandatory, correctly characterizing it as *not*
scope creep (it did not ask for a same-cycle A=724 re-run) — exactly what I
asked for.

Traced the chain: `phase3_synthesis.md` item 5 adopts it verbatim ("A
committed follow-up trigger is added to PLAN.md's queue at shift
close-out..."), `NOTES.md` idealization 7 restates it with the same
language and cites "Attack 1, MATERIALS" by name, and the Results section's
closing paragraph repeats it a third time ("Per idealization 7 (MATERIALS'
Attack 1), this finding is scoped to A=752/NY=1584 only"). Three
independent loci, consistent wording, none softened or dropped — this is
the opposite of the R4 failure mode (a citation that degrades in precision
each time it's repeated).

**One open item, not a defect at this stage of the loop.** I checked
PLAN.md's "Current state" section directly: it is still headed "panel
Iteration 25" and its queued-item list for Iteration 26 is the pre-exp-049
list (item 1 is still "QUANTUM's `gaussian_angle_weights` n-convergence
audit," not yet marked done). **The A=724 follow-up trigger has not
actually been written into PLAN.md's queue yet** — consistent with the
Director's own promise ("added... at shift close-out"), which is a
close-out action that comes after all seven Phase-5 reviews, not before.
This is not a broken promise as of this reading, but it is the one
concrete, checkable action item my own charter's finding leaves open: **the
trigger must actually land in PLAN.md at close-out, or my Attack 1's win
this cycle is real only in the experiment record, not in the program's
forward-looking queue** — the exact distinction Iteration 21's
`REALIZABILITY_MEMO.md` "claimed but not delivered" defect turned on. I
flag this as my own top follow-up item below rather than as a finding
against this cycle, since the loop has not yet reached the step where it
would be delivered.

**A sharpening worth adding, from this cycle's own data.** P-NCONV26-2/3
show something my Phase-2 attack did not anticipate: the T21 A=752
fringe-period model, reused "by analogy" (idealization 3) to predict *which*
cells are hardest to converge, measured PARTIAL at all three functions
(ρ=0.45–0.48, none clearing the 0.70 confirm bar) and REFUTED at
P-NCONV26-3 (the FWHM=10° "genuinely marginal" story). That is independent,
same-cycle evidence that the analogy's *predictive* power at its own home
geometry (A=752) is weaker than the Phase-1 proposal's prior assumed — which
makes leaning on an A=752-measured n* to infer anything at all about the
A=724 geometry an even less safe move than a simple "~4% period shift"
framing would suggest. Idealization 7 already forbids that inference on
scope grounds; this cycle's own P-NCONV26-2/3 results independently reinforce
it on mechanistic grounds. Worth stating in the eventual A=724 follow-up's
own Phase-1 proposal.

## (b) Does anything move any `REALIZABILITY_MEMO.md` tier?

**No — verified by reading the memo directly, not by trusting §3's
disclaimer or MATERIALS'/Red Team's Phase-2 say-so.**

I read `experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md`
in full, including all five amendments and Entry 2. Every tier verdict in
the memo traces to one of two sources: (1) the RSA/TPA/photochromic/VO2/FCA/
ENZ/graphene/combined-media rows, each a literature D_req/irradiance
comparison (exp-036/037/038) that never calls `design_geometry.py` at all;
or (2) Entry 2's `graded_black_shell` UNOBTANIUM call, anchored to
`C = −0.7209`, computed via `edge_diffraction_c_empty[_corrected]` at a
single fixed θ (exp-030's own FDTD run) — a code path that shares
`_G_for`/`_src_amp` machinery with `gaussian_angle_weights` but calls neither
`gaussian_angle_weights` nor any `beam_divergence_*` function. Grepped
`REALIZABILITY_MEMO.md` for "beam_divergence" and "gaussian_angle_weights":
zero hits. `gaussian_angle_weights`/`beam_divergence_*` feed only the T21
contamination-risk / `C_THR` ambient-contrast channel (exp-042/046's own
Block BEAM lineage), a ledger the memo never reads from. §3's "no result
here can move any REALIZABILITY_MEMO.md tier" claim is correct, independently
confirmed against the live file, not merely the proposal's assertion of it.

## (c) Independent spot-checks of `results.json`, computed from source, not trusted

Ran the unmodified `experiments/042-t21-magnitude-bridge/design_geometry.py`
functions myself, independent of `run.py`, and reproduced:

- `beam_divergence_coherent(36, 20, CPL[450], n=41/81/401)` →
  C(41)=−0.965320384302972, C(81)=−0.9239752489621912,
  C(401)=−0.9239930504205042. Derived move(41→401) = **4.472688822027389%**
  — exact match, to the last printed digit, of `results.json`'s
  `P_NCONV26_0.measured_worst_move_pct` and `expected_worst_move_pct`, and of
  NOTES.md's committed P-NCONV26-0 CONFIRMED figure. Derived move(41→81) =
  **4.474701609942433%** — exact match to `P_NCONV26_8.worst_coherent_move_pct`.
- `beam_divergence_incoherent_corrected(38, 2, CPL[750], n=41)` →
  **−0.004006497410421138**, exact match to `results.json`'s
  `P_NCONV26_5.c41`. Margin ratio `0.005/|c41|` = **1.247972852046454**,
  headroom **24.79728520464539%** — exact match to `P_NCONV26_5.margin_ratio`/
  `margin_headroom_pct` (i.e., THERMO's Attack-3 arithmetic correction, which
  I independently re-derive here rather than take on THERMO's or Red Team's
  word).
- Read `REALIZABILITY_MEMO.md` in full directly (covered under (b), above) —
  a source-level check, not a reliance on `results.json`.
- Cross-checked the completeness ledger: `results.json.meta.n_ledger_records
  = 972`, matching `run.py`'s own `assert len(ledger) == 972` and the Phase-3
  synthesis's committed expectation (36 cells × 3 functions × 8 N_SERIES
  entries + 36×3 n=401 checks = 972). `elapsed_s = 2743.24s` = 45m43s,
  matching NOTES.md's reported "45m44s" (1s rounding) and landing inside Red
  Team's profiled ≈52-minute estimate, as claimed.

No arithmetic or code-description defect found in anything I independently
recomputed. One minor, non-load-bearing observation: `P_NCONV26_6.min_abs_c
= 0.029552524834875537` in `results.json` differs from the `~0.03227`
figure NOTES.md's own P-NCONV26-6 row cites as "Committed min|C|" from
exp-046 — this is not a discrepancy, it's the expected consequence of
scoring against *converged* values (8/9 FWHM=20° coherent cells have n*>41,
so their converged C differs from their n=41 citation); NOTES.md's own prose
correctly treats the two as different quantities and neither prediction's
scoring depends on them matching.

---

## Physical meaning

Nothing in this cycle changes what real material could realize the target
phenomenon, and nothing was expected to — §3's "T1 escape route: NONE" is
accurate and the memo is untouched (confirmed above, not assumed). What the
cycle actually establishes, from an instrument-trust angle adjacent to my
own charter: exp-042/046's silent `n=41` default is now known-safe for
100/108 cell-function combinations in their own (A=752) geometry, with the
two known exceptions (`coherent` at FWHM=20°, needing n*≥81; `incoherent_
corrected` needing up to n*=321 at 5/9 FWHM=20° cells) now measured, not
guessed. exp-046's own restored A4 mechanism (the coherent function's real,
bounded aliasing sensitivity) is CONFIRMED and sharpened, not overturned —
the central finding motivating this whole audit holds.

## Ranked top-3 directions for Iteration 27 (this seat's own ranking)

1. **Confirm the A=724/NY=1528 follow-up trigger actually lands in PLAN.md's
   queue at this shift's close-out, and run it before any future
   near-boundary constraint-3 or realizability citation leans on this
   cycle's n* findings.** My own charter's finding from this cycle; cheap
   (a re-parameterized re-run of the identical desk sweep, exp-048's own
   precedent for this exact kind of geometry re-scope); the correct next
   step to actually retire it, not just disclose it, and this cycle's own
   P-NCONV26-2/3 results (the fringe-analogy is a weaker predictor than
   assumed even at its home geometry) raise, not lower, the stakes of
   leaving it unclosed.
2. **Genuine FDTD `ABSORB` sweep at exp-048's own new geometry** (T21-vs-T24,
   already queued as Iteration-26 item 3 in PLAN.md, not yet run) — the
   only way to tell whether Block B's 5/27 near-boundary gate exceedances
   are a real edge fringe or T24's own uncharacterized boundary systematic;
   this bears directly on whether the desk propagator this audit just
   validated as internally self-convergent is also the right *physical*
   model at the geometry that matters, a question convergence alone cannot
   answer.
3. **Build and measure the fixed-absolute-thickness `graded_black_shell`
   variant's own C** (now a 9-iteration-deferred MATERIALS pick, four seats
   independently rank it, `REALIZABILITY_MEMO.md` Entry 2's own "Open" item).
   The one item squarely on my own charter's critical path left undone —
   Entry 2 formalized why the self-similar construction is the harder
   realizability ask; a real fixed-thickness measurement is the natural,
   still-missing companion that could move Entry 2 from informal UNOBTANIUM
   toward a formal, evidence-backed tier.

## Verdict

**PROMISING**, from this seat's charter specifically. This is a
well-executed instrument-fidelity cycle: my own Phase-2 finding was
affirmed by Red Team, adopted without dilution through Phase 3, and carried
honestly, word-for-word-consistent, through NOTES.md's idealizations and
Results — the follow-up commitment is real, only its delivery into PLAN.md's
queue is still pending at the point this review was written (expected,
since close-out follows all seven Phase-5 reviews, not this one alone).
`REALIZABILITY_MEMO.md` is confirmed untouched by reading the live file
directly, not by trusting the proposal's disclaimer. Every number I
independently recomputed from the unmodified source functions matched
`results.json` exactly, including the two Phase-2 arithmetic corrections
(THERMO's margin fix, the P-NCONV26-0/8 worst-move figures). The one
in-cycle self-caught defect (the sign-convention erratum in
`predicted_difficulty_rank()`) was disclosed inline, not smoothed over, with
both the buggy and corrected computations preserved in `results.json` — the
house discipline working as designed. No `REALIZABILITY_MEMO.md` tier moved,
none was claimed to, and no constraint was violated or quietly dropped.
