# PHASE 2 — RED TEAM AUDIT · Panel Iteration 58 · exp-081
## Adjudicating THERMODYNAMICS' total-field construction (item 1), the EM gate re-run (item 2), the energy budget (item 3), the MATERIALS hygiene fix (item 4), and all five blind Phase-2 critiques — with each of the three consequential "missing check" findings actually run, not merely re-argued

**Seat: RED TEAM.** Read, in order: `PANEL.md` in full (charter, phenomenon +
four constraints, five-phase loop, Checkpoints §1–5); `AGENTS.md` in full;
`LOGBOOK.md` (RULED OUT R1–R9 in full, ESTABLISHED, LIVE THREADS in full —
T28's complete Iteration 46–57 history, R4/R6/R8/R9 in particular);
`PLAN.md`'s Iteration-58 queue; `experiments/080-.../phase2_redteam_audit.md`
(format model); the complete `experiments/081-.../` directory in order
(`phase1_proposal.md`, `photonics_construction.py`, `phase1_results.json`,
`_output.txt`, `NOTES.md`, all five blind Phase-2 critiques);
`experiments/079-.../y_wall_aperture_sum.py` §[7]/§[7b] (the reflectance-
ablation idiom); `lab/validation/run_all.py`'s gate pattern (confirmed: no
`gate_*` functions of this T28 sub-thread's kind live there — the
G-LOSSLESS/G-N1/G-PASSIVITY battery is experiment-local self-consistency
machinery, not a house trust-suite stage, exactly the algebraic-not-empirical
distinction EM's critique turns on). I alone see the complete record and all
five blind critiques, and speak last.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document
or by anything it adjudicates.**

**Independent verification performed, not merely re-argued.** I wrote my own
verification artifact, `/tmp/claude-0/.../scratchpad/redteam_verify_081.py`
(session-local scratch, clearly marked as Red Team's own audit tool — does
NOT modify anything under `experiments/081-.../`), that reuses ONLY
already-committed, already-gated primitives (`dg065.CONFIGS`,
`ywas.build_aperture_grid`/`aperture_amplitude`/`source_driven_phase`/
`dist_image_cells`/`reflection_coefficient_vec`/`_trapz`/`K600`/
`free_period_with_widening`/`score_period`/`rel_dev`,
`d80.reflection_coefficient_vec_realizable`/`photonics_image_term_curve`,
`pc81.e_direct_curve` — this cycle's own committed function, reused
unchanged) — never copied from any critique's own prose, never taken on
trust. First step: reproduce exp-081's own committed item-1 result
independently, from scratch, in this script, as a wiring check before
trusting any variant built on top of it.

| # | Claim checked | Source | My result | Reproduced / resolved? |
|---|---|---|---|---|
| 0 | Item 1's own committed result: `P*_model`=1.8571°/2.0301°/2.0150°, `rel_dev`=0.5973/0.5139/0.2910, verdicts INCONCLUSIVE/INCONCLUSIVE/SUPPORT, Combined NEITHER | `phase1_results.json` | Bit-identical, all three pairs, from a from-scratch script that imports `pc81.e_direct_curve` and `d80.photonics_image_term_curve` directly, not `photonics_construction.py`'s own `item1_build_and_score()` | **YES, exact** — wiring confirmed correct before trusting variants (A)/(B)/(C) below |
| A | **MATERIALS' finding**: item 1 never scored under the realizable (`μ_r=1`) admittance | MATERIALS | Re-scored `E_image` under `d80.reflection_coefficient_vec_realizable` at the SAME `90°−θ_beam` range, everything else unchanged. Periods: 1.8647°/2.0301°/2.0226° (shifts of 0.0075°/0.0000°/0.0075° vs matched). Verdicts: INCONCLUSIVE/INCONCLUSIVE/SUPPORT — **identical**. Combined Verdict: **NEITHER, unchanged** | **YES, gap confirmed real — and NOT outcome-determining** (§1, Attack 1) |
| B | **PHOTONICS'/QUANTUM's convergent finding**: item 1c's "REFUTE-leaning" reading has no reflectance-ablation control | PHOTONICS, QUANTUM | Ablated `r(90°−θ_beam;ABSORB)→1.0` (exact `y_wall_aperture_sum.py` §[7] convention) in `E_image`, rescored. **Pair-specific, not uniform**: `PAIR_ABSORB40`'s ablated delta is `ss_tot=0.0` EXACTLY (`SS_TOT_DEGENERATE`, no signal at all) vs. its real, non-degenerate `rel_dev=0.5139` under true `r()` — genuinely `r()`-dependent. `C80−C40` (the ONE pair carrying the lone SUPPORT) shifts only 0.0075° under ablation (`rel_dev=0.2937` ablated vs `0.2910` real) — SUPPORT **survives ablation to zero wall physics almost unchanged**. `PAIR_PAD` shifts 0.15° (partial dependence) | **YES, gap confirmed real, control run — result is a genuinely NEW, pair-specific finding neither critique anticipated** (§1, Attack 2) |
| C | **EM's finding**: item 2's magnitude-only gate re-run cannot resolve the `r` vs `conj(r)` phase-convention ambiguity R8 exists to guard against | EM | Substituted `r(90°−θ_beam)→conj(r(90°−θ_beam))` in `E_image`, rescored. Periods: 2.1278°/2.4887°/2.2481° — shift, but **zero verdict flips** (INCONCLUSIVE/INCONCLUSIVE/SUPPORT survive identically), and the T21-proximity/REFUTE-leaning qualitative reading survives (`rel_dev_vs_T21`=0.0852/0.2692/0.1465, still `<` `rel_dev_vs_T28` at all 3 pairs) | **YES, EM's factual claim confirmed exact — AND independently shown NOT outcome-determining this cycle** (§1, Attack 3) |
| D | Phase-divergence explanation for why (A) barely moves anything, unlike exp-080's own part(b) (same substitution: `INCONCLUSIVE mean R²=0.7345`→`REFUTE mean R²=0.4305`) | new, this audit | At `θ∈[5°,15°]` (part(b)'s own near-normal range), matched-vs-realizable `arg(r)` diverges **54.0°–83.6°**. At `θ∈[48°,54°]` (item 1's actual grazing `90°−θ_beam` range), the SAME two families diverge only **8.4°–10.6°** — an order-of-magnitude-smaller phase gap, at ABSORB=40, computed directly from `br.n_profile_exact`/`ywas.reflection_coefficient_vec`/`d80.reflection_coefficient_vec_realizable` | **New finding, independently derived, explains (A) rather than merely reporting it** |
| E | **VISION's finding**: `experiments/081-.../` is untracked, no dedicated pre-registration commit exists | VISION | `git log --oneline -- experiments/081-.../phase1_proposal.md` → **one commit, `ff73016`**, containing `phase1_proposal.md` (predictions AND results together), `photonics_construction.py`, `phase1_results.json`, `_output.txt`, and the exp-080 docstring fix, all at once — confirmed. Compared against `exp-080`'s genuinely separate `6fb6b99` (predictions only, 15:06:19) → `23203cc` (run, 15:08:40, 2m21s later) | **YES, core claim confirmed exact** — but VISION's historical generalization is overstated, see §1 Attack 4 |
| F | R9 self-check: item 3's `~116,000×` ratio (`1.4943×10⁻³`/`1.2886×10⁻⁸`) is commensurable (same `|r|²` operation, same units) | proposal §"House-discipline applicability" | `1.4943e-3 / 1.2886e-8 = 115,980`, matches the reported `1.1597×10⁵` to 4 significant figures; both operands are `reflected_power_fraction=|r(θ)|²`, dimensionless, differing only in which `θ` array is passed — commensurable by construction | **YES, confirmed** — no R9 issue |

**Summary: every load-bearing arithmetic claim across `phase1_results.json`
and all five blind critiques independently reproduces exactly.** Unlike
exp-080's own audit, this cycle's disagreements are not merely about scope
and framing of already-correct numbers — three genuinely NEW numeric results
(A, B, C above) had to be computed to adjudicate whether the critiques'
concerns are outcome-determining, and the answer differs by finding: (A) and
(C) are real gaps that turn out NOT to move the Combined Verdict; (B) is a
real gap whose resolution is more informative, and more nuanced, than either
raising critique's own binary framing anticipated.

---

## 1. Numbered attacks

### Attack 1 — `[inconsistency]` item 1's single-admittance-family headline, now resolved rather than merely flagged

MATERIALS is correct that `photonics_image_term_curve()` (reused unchanged
from exp-080) calls `ywas.reflection_coefficient_vec` (matched, unobtainium)
exclusively, and that item 3's own energy budget is the only place this
cycle invokes the realizable function — at a *different* angle range
(`theta_local≈5–15°`, not item 1's `90°−θ_beam≈48–54°`). This is exactly the
gap exp-080's own part (b) showed CAN be outcome-determining (mean
`R²` `0.7345→0.4305`, INCONCLUSIVE→REFUTE). My own re-score of item 1 under
the identical substitution (§0 item A) finds the Combined Verdict, all three
per-pair verdicts, and the T21-proximity pattern **survive unchanged**
(shifts of `0.0075°`/`0.0000°`/`0.0075°`, orders of magnitude smaller than
the `rel_dev` bands' own 0.30/1.00 gates). I traced why (§0 item D): item 1
operates in a materially different, more-grazing angular regime than
part (b)'s own near-normal one, where the two admittance families happen to
diverge in phase by an order of magnitude less (`8.4–10.6°` vs `54.0–83.6°`
at ABSORB=40). **This is a real completeness gap that should have been
checked before the record cited a single-family headline** (matching this
program's own R8-family discipline: a named, affordable check, not run) —
but, having now run it, the gap is confirmed NOT outcome-determining, a
materially different disposition than its part(b) analog. **Fix**: append
the realizable-admittance re-score and the phase-divergence explanation to
the permanent record (§4 docket item 1).

### Attack 2 — `[inconsistency]` item 1c's "REFUTE-leaning" reading is missing this sub-thread's own established look-elsewhere control — now run, revealing pair-specific structure the record does not currently state

PHOTONICS and QUANTUM converge, independently, on the same gap: item 1c's
T21-proximity diagnostic cannot by itself distinguish "the wall's
reflectance disfavors T28" from "this test, like its two predecessors, is
structurally insensitive to `r(θ)`'s value" — the exact ambiguity
`y_wall_aperture_sum.py` §[7]/§[7b] was built to resolve for a structurally
similar object. Running the control (§0 item B) does NOT deliver either
critique's own hypothesized clean outcome ("no shift → full insensitivity
finding" per PHOTONICS; "shift → vindicated as-is" per PHOTONICS/QUANTUM).
It delivers a **third, pair-specific answer neither anticipated**:

- `PAIR_ABSORB40`'s ablated delta is `ss_tot=0.0` **exactly** (the shared-
  geometry-under-ablation identity `y_wall_aperture_sum.py` already
  established for `G40`/`C80` — both share `PAD=40`, so once `r()` carries
  no `ABSORB`-dependence, their image terms are geometrically identical) —
  meaning the real, non-degenerate `2.0301°` period this pair recovers under
  the TRUE `r()` genuinely requires wall reflectance to exist at all. This
  pair's own INCONCLUSIVE verdict is honest evidence about real wall physics,
  not a look-elsewhere artifact.
- `C80−C40` — the ONE pair item 1's Combined Verdict ever scored SUPPORT,
  and the pair item 1c's "REFUTE-leaning... not independent confirmation"
  language most needs to discredit — shifts only `0.0075°` under total
  ablation to `r()=1` (`rel_dev=0.2937` ablated vs. `0.2910` real, both
  still clear the 0.30 SUPPORT bar). **The lone SUPPORT survives with zero
  wall physics present at all** — decisively confirming PHOTONICS'/QUANTUM's
  suspicion for exactly the pair that matters most to the headline reading.
- `PAIR_PAD` sits between the two (`0.15°` shift, qualitatively similar
  either way).

**NOTES.md's own "the sole SUPPORT is the same compromise-fit pattern...
not independent evidence" conclusion is correct on its bottom line and is
now, for the first time, actually PROVEN rather than argued by analogy to
PHOTONICS' own pre-registered feasibility-probe language** — but the write-up
asserts this uniformly across all three pairs when the underlying evidence,
once computed, is genuinely asymmetric: `PAIR_ABSORB40` carries real
wall-physics content this framing does not credit it with. **Fix**: append
the pair-specific ablation table to the permanent record and revise item 1c's
prose to cite the ablation result as its actual evidentiary basis for
`C80−C40` specifically, rather than resting on the T21-distance comparison
alone (§4 docket item 2).

### Attack 3 — `[inconsistency]` item 2's gate re-run is magnitude-only and NOTES.md's "can be trusted going forward" overclaims what it establishes — the sensitivity to the flagged gap is now resolved, the true convention is not

EM's factual claim reproduces exactly: `G-LOSSLESS`/`G-N1`/`G-PASSIVITY` are
algebraically blind to `r→conj(r)` by construction (`|conj(r)|=|r|`
identically; a direct-formula-vs-loop-formula comparison sharing the same
assumed sign convention cannot catch a globally wrong one), and the ONLY
check that ever empirically resolved this class of ambiguity
(`phase5_redteam_phase_convention_check.py`, exp-075's own R8-originating
tie-breaker) was calibrated at `0°/20°/39°`, nowhere near `[47.5°,54.5°]`,
and was never re-run here. `NOTES.md`'s "item 1's own construction can be
trusted at this range going forward" therefore overclaims: the three
committed gates establish algebraic self-consistency, not the sign
convention item 1's entire period-recovery result is driven by (`arg(r)`,
not `|r|`, per EM's own correct framing).

**This is exactly the shape R8 was adopted to catch — a named, affordable
check, not run, ahead of a headline claim.** Per R8's own text, the
distinguishing factor between firing and non-firing is whether the flagged
gap "later proves outcome-determining." I ran the sensitivity test EM's own
critique stopped short of (§0 item C, zero new FDTD — a convention-flip
substitution, not an empirical resolution): under `conj(r)`, **no verdict
flips** across all 3 pairs, and the REFUTE-leaning/T21-proximity qualitative
reading survives. This is the OPPOSITE disposition from R8's own triggering
precedent (exp-075: the identical substitution flipped REFUTE to
INCONCLUSIVE, outcome-determining). **The true empirical question — which
convention the real graded-loss boundary's physics actually realizes at this
NEW, more-grazing angle range — remains genuinely open and requires new
FDTD** (extending `phase5_redteam_phase_convention_check.py` to 2–3 angles
inside `[47.5°,54.5°]`, EM's own suggested fix, cheap — exp-075's own
battery ran in ~90s — but explicitly outside this cycle's zero-FDTD scope,
Idealization 7). **Fix**: correct `NOTES.md`'s overclaim to state precisely
what the gates do and do not establish, append this audit's own sensitivity
result (reassuring but not resolving), and queue the actual FDTD extension
for Iteration 59 rather than let it lapse silently a second time (§4 docket
item 3).

### Attack 4 — `[inconsistency]`, minor and procedural: VISION's git-provenance finding is real, but its historical generalization overstates the precedent

`git log --oneline -- experiments/081-.../phase1_proposal.md` confirms
VISION's core finding exactly: **one commit** (`ff73016`), predictions and
results together, no separately-verifiable pre-registration-before-run
commit — unlike exp-080's genuine `6fb6b99`→`23203cc` split (2m21s apart).
**But VISION's framing — "every T28 cycle since exp-076, including this
cycle's own direct ancestor exp-080, committed the frozen-predictions text...
before the run commit" — does not hold up under my own independent check**:
`git log --oneline -- experiments/079-.../phase1_proposal.md` shows exp-079's
own Phase 1 (`9e4e1ae`) ALSO combined proposal and run into a single commit,
with no Red Team or Phase-5 objection raised in that cycle's own record;
`experiments/076-.../` and `experiments/077-.../` predate this repository's
visible git history entirely (the earliest commit in `git log` is an exp-078
Phase-4-WIP commit — there is no git record to check for exp-076/077 at
all). **The two-commit split is exp-080's own individual practice, not an
established multi-cycle norm this cycle regressed from.** This does not
change VISION's own correct, self-limiting ruling: PANEL.md's literal text
binds the non-negotiable git-before-run mandate to **Phase 3**'s FROZEN
PREDICTIONS commit specifically — "the Director resolves the debate into ONE
testable configuration... predictions committed to git BEFORE the run
(house discipline, non-negotiable)" — which for exp-081 has not yet
happened. This is a genuine, disclosed regression in auditability relative
to the *best* (not the *median*) precedent this sub-thread has shown, not a
rules violation of anything binding at this phase. **Fix**: correct the
historical claim in the permanent record and bind Phase 3 explicitly to
restore exp-080's own two-commit standard for its own FROZEN PREDICTIONS,
not repeat this cycle's combined-commit pattern a second time running (§4
docket items 4–5).

**No `[unfalsifiable]` or `[inexpressible]` attacks found.** This cycle makes
no mechanism claim beyond "does this construction recover T28's real
periodicity" and proposes no new physics — every function this cycle adds
(`dist_direct_cells`, `e_direct_curve`, the two gate functions, the energy-
budget integral) is pure desk arithmetic on already-gated primitives, and
every prediction was pre-registered with falsifiable numeric bands (verified
by direct code inspection of `phase1_proposal.md`'s ordering: the PRE-
REGISTERED section precedes the PHASE 1 RESULTS section in the same
document, and the compliance note discloses the single-commit git limitation
Attack 4 addresses). **No `[constraint-#N-violation]` attacks found.** Zero
constraint-3 (or any-constraint) engagement anywhere in this cycle's
record — independently confirmed by my own `grep -il` search of every `.md`
file in `experiments/081-.../` for
witness/silhouette/ambient/scotopic/photopic/`C_thr` language: only
`phase1_proposal.md`'s own explicit N/A disposition and VISION's own audit
of that same disposition surface, and the one apparent hit
("ambient-contrast channel") is the T28 signal's inherited location name
(`lab/ambient.py`'s channel), never a perceptual comparison — matching
VISION's own finding exactly.

---

## 2. Disposition of the five blind critiques

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| PHOTONICS | support-with-changes | Ablation control run (§0 item B); neither of PHOTONICS' own two hypothesized clean outcomes obtained — the real result is pair-specific | **ADOPT the attack and the request in full; EXTEND the conclusion.** The ablation control is now run, not merely requested — fold the pair-specific table into the record (§4 item 2). PHOTONICS' own binary flip-condition framing ("if no shift, full support; if shift, vindicated as-is") does not cleanly resolve the mixed result, but the substantive direction PHOTONICS argued for (the SUPPORT is not trustworthy evidence) is now proven, not merely suspected, for the pair that actually matters. |
| MATERIALS | support-with-changes | Realizable-admittance re-score run (§0 item A); Combined Verdict/verdicts/T21-pattern unchanged, contrary to the implicit urgency of MATERIALS' own part(b) analogy | **ADOPT the methodological point (the check should have been run) in full; PARTIALLY OVERRIDE the implied urgency.** MATERIALS is right the gap existed and should be closed before item 1 is cited as settled — done, this audit. But MATERIALS' own sharpest attack draws a direct analogy to exp-080's part(b), where the identical substitution flipped INCONCLUSIVE→REFUTE; my own computation shows item 1's situation is NOT analogous in outcome (§0 item D explains why: an order-of-magnitude-smaller phase divergence at item 1's actual angle range). MATERIALS could not have known this without running the check — which is exactly why it needed running, not merely re-argued. |
| ELECTROMAGNETISM | support-with-changes | Conjugate-convention sensitivity test run (§0 item C); EM's factual claim (gates are magnitude-only, phase-convention untested) confirmed exact; outcome-determinacy resolved (no) | **ADOPT IN FULL, and answer EM's own stated flip condition directly.** EM's critique names the exact affordable check (extend the FDTD tie-breaker) but does not itself distinguish "genuinely open" from "outcome-determining" — this audit does: the true convention remains open (needs new FDTD, queued), but is shown NOT outcome-determining for THIS cycle's Combined Verdict, which is the more decision-relevant question Phase 3 actually needs answered now. |
| QUANTUM | support-with-changes | Same ablation control as PHOTONICS (§0 item B) — QUANTUM's own independent verification (import-chain trace, `rel_dev` robustness check) is itself sound and reproduces | **ADOPT IN FULL, and EXTEND identically to PHOTONICS' disposition above.** QUANTUM's own pre-registered flip condition ("if the ablated periods are statistically distinguishable... that sharpens... I would support fully") is PARTIALLY met: `PAIR_ABSORB40`'s ablated/real periods ARE distinguishable (one is literally degenerate, the other real) — sharpening the finding exactly as QUANTUM predicted for that pair — while `C80−C40`'s are NOT distinguishable, the opposite direction, for the pair that drives the headline reading. |
| VISION | support-with-changes | Git history independently reproduced exact (§0 item E); historical generalization checked and found overstated | **ADOPT the core finding and required fix in full; CORRECT the historical framing.** The git-provenance gap is real and the required same-shift-or-Phase-3 remedy is right. The "every cycle since exp-076" claim does not survive independent check (exp-079 shows the identical single-commit pattern with no objection raised) — corrected in §1 Attack 4, does not change VISION's own verdict or required fix. |

**No blind critique's verdict is overridden** — all five filed
support-with-changes and I concur with support-with-changes for all five.
**Two factual sub-claims are corrected** (MATERIALS' implied outcome-urgency,
VISION's historical generalization), both disclosed explicitly above with
the independent computation that produced the correction, per this program's
own R4/R9 standard for how a reviewer's "confirmation" must be earned, not
merely asserted.

---

## 3. Overall ruling: **PROCEED-WITH-MANDATORY-FIXES**

Not PROCEED-AS-IS: three of the four Phase-1 items (1, 2, 3) carry a
disclosed-but-unresolved-until-this-audit gap that a reader of
`phase1_results.json`/`NOTES.md` alone could not have distinguished from a
closed question, and item 1's own headline language ("REFUTE-leaning," "can
be trusted going forward") needs revision to state precisely what this
audit's own new computations show, not merely what was originally argued.
Not HALT-AND-REDESIGN: no false claim survives independent re-derivation
(§0 — every existing number reproduces exactly; every newly-computed number
is disclosed as new, not retrofitted as if always known), no RULED-OUT item
is re-proposed, zero new FDTD anywhere in this cycle's own record or in this
audit's own verification, and none of the three resolved gaps turned out to
threaten the Combined Verdict — this is a record-completeness and precision
correction, landable same-shift, exactly the shape this program's own
established PROCEED-WITH-MANDATORY-FIXES precedent (exp-080's own audit,
among many others) exists for.

### Fix docket, prioritized, for Phase 3 synthesis

1. **[HIGH]** Append this audit's realizable-admittance re-score of item 1
   (§0 item A, §1 Attack 1) to `phase1_results.json`/`NOTES.md`: Combined
   Verdict unchanged (NEITHER), per-pair verdicts identical, periods shift
   `≤0.0075°` — **not outcome-determining**, with the phase-divergence
   explanation (§0 item D: `8.4–10.6°` at item 1's `48–54°` range vs.
   `54.0–83.6°` at part(b)'s `5–15°` range, ABSORB=40) folded in so future
   readers do not need to re-derive why this differs from exp-080's own
   part(b) precedent.
2. **[HIGH]** Append this audit's reflectance-ablation control (§0 item B,
   §1 Attack 2) to the permanent record, stated pair-specifically, not
   uniformly: `PAIR_ABSORB40` is genuinely `r()`-dependent (ablated signal
   exactly degenerate; real signal non-degenerate, `rel_dev=0.5139`);
   `C80−C40` — the pair carrying the lone SUPPORT — is (nearly)
   `r()`-independent (SUPPORT survives ablation to `r()=1` almost unchanged,
   `0.2937` vs `0.2910`); `PAIR_PAD` is partially dependent (`0.15°` shift).
   Revise item 1c's "not independent confirmation" language to cite this
   control as its actual evidentiary basis for `C80−C40` specifically.
3. **[MEDIUM]** Correct `NOTES.md` item 2's "item 1's own construction can be
   trusted at `[47.5°,54.5°]` going forward" to state precisely what the
   magnitude-only gates do and do not establish (§0 item C, §1 Attack 3).
   Append this audit's `r→conj(r)` sensitivity result (no verdict flips,
   reading survives) as reassuring-but-not-resolving, and queue the actual
   FDTD-based phase-convention extension (2–3 angles inside
   `[47.5°,54.5°]`, mirroring `phase5_redteam_phase_convention_check.py`)
   explicitly for Iteration 59 — an affordable, cheap check, not a resolved
   one this cycle.
4. **[MEDIUM]** Correct the historical claim implicit in citing this cycle's
   single-commit pattern as a "regression from an established norm since
   exp-076" (§1 Attack 4): the two-commit split is exp-080's own individual
   practice (confirmed against exp-079's own single-commit Phase 1, and
   exp-076/077 predate this repo's visible git history). Restate the
   binding fact precisely: PANEL.md's non-negotiable git-before-run mandate
   applies to Phase 3's FROZEN PREDICTIONS specifically, which has not yet
   occurred for exp-081.
5. **[MEDIUM]** Bind Phase 3 explicitly, in writing, in `NOTES.md` or the
   Phase 3 synthesis document itself: exp-081's FROZEN PREDICTIONS for its
   corrected re-run (folding in items 1–3 above) MUST be committed to git in
   a commit genuinely separate from, and strictly before, the commit that
   executes the corrected script and records results — restoring exp-080's
   own standard, not repeating this cycle's combined-commit pattern a second
   consecutive time.
6. **[LOW]** EM's secondary point: item 3's "negligible... under either
   angle convention" headline conflates the tight `theta_local`-based bound
   (a bound on a construction item 1 never built or period-tested) with the
   looser `90°−θ_beam`-based bound (the bound on item 1's own actually-tested
   object). Both are legitimately small in absolute terms (`0.15%` is
   negligible too), but state explicitly which bound covers which tested
   object.
7. **[LOW]** No fix required, noted for completeness: item 1b's own honest
   self-falsification of its literal "bit-identical" prediction (technically
   REFUTED at `~10⁻¹⁴`, substantively CONFIRMED to 11+ orders of magnitude
   below signal scale — independently re-derivable from `|E_direct|≈89–111`
   vs `|E_image|≈1.3×10⁻⁴–3.5×10⁻³`, a genuine `O(100)`-vs-`O(10⁻³)` scale
   gap) is exactly the disclosure standard R4 requires and needs no
   correction.

---

## 4. Checkpoint ruling

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 or any-constraint engagement anywhere in this cycle,
independently confirmed (§1, closing paragraph), matching VISION's own
finding.

**Criterion 2** (a proven mechanism-class boundary): **NOT YET RIPE.** This
cycle runs, for the first time in this nine-cycle T28 y-wall sub-thread, the
actually-decisive test (total field, real-data free-period fit) against
PHOTONICS' own construction as specified — and this audit's own ablation
control sharpens the result further than the committed record alone: the
lone SUPPORT is now *proven*, not merely argued, to require no wall physics
at all, while `PAIR_ABSORB40` is shown to carry genuine, if still
non-matching, wall-reflectance content. This is real, cumulative narrowing —
but it remains a single result on the `-90°−θ_beam` global-steering
construction specifically, at one wavelength (600nm), on an empty scene. The
board's own oldest-overdue items (the 750/450nm wavelength-generality leg,
the PAD-loaded real-article check, both deferred six consecutive cycles per
PLAN.md's own Iteration-58 queue) remain untouched by this cycle's Tier-0
scope and are the natural next tests before any mechanism-class boundary is
declared. **Ruling: does not fire**, matching this sub-thread's own
established non-firing pattern for single-cycle, single-construction,
single-wavelength results.

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
Zero new FDTD anywhere in this cycle's own record (`photonics_construction.py`
imports only `dg065`/`br`/`ywas`/`d80`, confirmed by direct inspection) or in
this audit's own verification script (identical import set, confirmed by
direct inspection of my own file).

**Criterion 4** (program-integrity drift): **Reasoned through explicitly,
does not fire — conditioned on Phase 3 adopting this audit's fix docket, the
SAME condition exp-080's own Iteration-57 audit attached to its own
comparable near-miss.** Three flagged gaps (items 1, 2, item 2's own gate
scope) each carried language in the committed record that, read alone,
overstates what was established (item 1's single-family headline; item 1c's
uniform REFUTE-leaning framing; item 2's "can be trusted going forward").
None is a **false** claim about a specific checked computation (every
existing number in `phase1_results.json` reproduces exactly, §0) — the risk
is incompleteness and overclaim, not fabrication, and this audit resolves
all three WITHIN this same Phase-2 review layer, before Phase 3 has had any
opportunity to carry an unqualified claim forward — matching the established
non-firing shape (exp-079 Iteration 56, exp-080 Iteration 57: genuinely new
information, surfaced and reconciled inside the review layer itself, not a
defended wrong claim surviving to the next phase). **The distinguishing
condition, stated plainly, exactly as exp-080's own audit stated it one
cycle earlier**: if Phase 3 synthesis repeats `NOTES.md`'s pre-audit
"REFUTE-leaning" / "can be trusted going forward" language verbatim, without
folding in this audit's own realizable-admittance, ablation, and
phase-convention-sensitivity results, THAT would be the firing shape one
phase later — criterion 4 continuing not to fire is conditioned explicitly
on the fix docket (§3) being adopted, not on this audit's existence alone.

**Criterion 5** (two consecutive non-advancing iterations): **Not at risk.**
This cycle delivers the sub-thread's own actually-decisive test for the
first time (nine cycles in), sharpened by three independently-run
verification checks this audit adds — a substantive, cumulative result
regardless of which way Iteration 59 ultimately weighs it for Checkpoint 2.

---

## 5. Note for Iteration 59

Not a full reconciled ranking (Phase 3/4/5 have not yet run for exp-081 —
that synthesis belongs to this cycle's own Phase 5, not this Phase-2 audit),
but three items this audit's own findings bear on directly, for whoever
next ranks the board: (1) the pair-specific ablation finding (§1 Attack 2)
means any future scrutiny of this construction should treat `PAIR_ABSORB40`
and `C80−C40` as carrying different evidentiary weight, not as
interchangeable instances of the same REFUTE-leaning reading; (2) the
phase-convention sensitivity result (§1 Attack 3) means the FDTD extension
of `phase5_redteam_phase_convention_check.py` to `[47.5°,54.5°]` is
affordable, cheap, and disclosed-but-not-yet-run — it should not be allowed
to lapse silently a second cycle running, even though this audit shows it is
not this cycle's own outcome-determining gap; (3) PLAN.md's own
wavelength-generality and PAD-loaded-real-article items — each already FIVE
consecutive deferred cycles (076–080) per PLAN.md's own Iteration-58 count,
and neither addressed by this cycle's Tier-0-only scope, so both become SIX
consecutive as of Iteration 59 — remain the board's most overdue items and
the natural test of whether this cycle's REFUTE-leaning finding (now
sharpened, not merely asserted) generalizes at all.

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
