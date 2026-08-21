# exp-054 Phase 5 — RED TEAM audit (last, with everything)

Panel Iteration 31. Reviewed: `PANEL.md`, `phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `results.json`, all six Phase-5 reviews,
`lab/thermo_sidecar.py`, `lab/validation/run_all.py::stage18_length_scale_chain`,
`experiments/043-.../NOTES.md` + `results.json::graded_black_shell_flagship`,
`experiments/045-.../NOTES.md` (both SUPERSEDED notices), and
`experiments/034-.../REALIZABILITY_MEMO.md:206-232`. Every finding below was
re-derived from source, not trusted from any seat's prose — the same
standard applied to Red Team's own Phase-2 audit.

## Verdicts on the six seats' Phase-5 findings

**PHOTONICS (PARTIAL) — CONFIRMED, load-bearing.** Grep-verified:
`NOTES.md:18` states `w_on (the ON-endpoint's measured, diffraction-
inflated extinction-cross-section width)` with no caveat, and no
`results.json` key or idealization bullet flags the word as
asserted-not-established, even though this program's own Phase-2 record
(this seat's critique + my own Phase-2 attack 6) already established that.
The downgrade-to-non-mandatory call was correct (it doesn't change the
mixed-chain's conclusion, as attack 6 found); the disclosure gap is real —
a reader citing `NOTES.md` alone inherits an unqualified claim. Genuinely
load-bearing for future citation hygiene, not for this cycle's numbers.
The achromatic-scope citation imprecision (exp-045's kinetics-flatness
result cited in place of exp-044's Block-C thermal-magnitude flatness
result) is also confirmed by direct read of `NOTES.md:64` — real, but
correctly scoped by PHOTONICS itself as "the substance is very likely
fine," not a numeric threat.

**MATERIALS (PROMISING) — CONFIRMED, all three load-bearing.**
1. `lumped_cube_mass_kg` (`lab/thermo_sidecar.py:203-216`) verified to take
   no fill-fraction parameter — a caller invoking it directly gets a bare
   density×L³ number with no ASSUMED/fill flag attached to it, only one
   layer up at `mixed_length_scale_regime`. Real capability regression
   against `REALIZABILITY_MEMO.md`'s own Amendment 5(b) validity
   condition, verified in the memo directly.
2. `mixed_length_scale_regime` (`lab/thermo_sidecar.py:219-280`) confirmed
   to re-implement `dp_dt = area*(4εσT³+h)` inline (line 246) rather than
   calling `steady_state_delta_T`, and drops that function's graybody
   idealization-warning docstring. Confirmed by direct read of both
   functions.
3. **Confirmed by independent computation**: `netd_lo_margin_exact` =
   8954.619× (`results.json::part_b_block_c_rerun`) vs. the still-standing
   published headline 27,080.214× (`0.020/7.385465974827066e-7`, cited
   verbatim at `phase1_proposal.md:84` and still uncorrected in
   `experiments/045-.../results.json` itself, only flagged not overwritten
   per T10). The corrected figure is **3.0243× smaller**, not larger. This
   is real and is the single most consequential *interpretive* finding in
   this cycle's own Phase-5 record (see next section).

**ELECTROMAGNETISM (PROMISING) — CONFIRMED, both findings real.**
Re-derived the algebra myself: `coupled_segment_general` reducing to
`coupled_kinetics_thermal_dT` at `n0=dT0=0` is a general identity for
*any* `(k_f,k_r,dt_ss,tau_th,dt)` — the assertion at `run.py:170-171` is
mathematically guaranteed to pass independent of correctness at nonzero
initial conditions, and I confirm `lab/validation/run_all.py`'s stage 18
(lines 1563-1611) covers only `gas_conduction_h_eff`, `lumped_cube_mass_kg`,
and the ON-endpoint regression — `coupled_segment_general` is grep-confirmed
absent from `lab/validation/run_all.py` entirely, despite being the
machinery P-054-3a's headline number depends on. EM's own RK4 closure
(reported, not committed to the codebase) is exactly right procedurally but
leaves the actual repo with zero regression protection on that function —
a real, currently-open gap, not merely a "nice to have."

**THERMODYNAMICS (PARTIAL) — CONFIRMED, and the flagship-margin catch is
real, independently reproduced with the exact number.**
`experiments/043-.../results.json::graded_black_shell_flagship`:
`area_convention="iso_xsec_sq"` with `sigma_ext_cells=240.0073740162445`
(the `w_on`-equivalent length) driving area for **both** the absorbed-power
computation *and* (via `absorber_area_m2 = absorber_central["area_m2"]`,
confirmed at `experiments/043-.../run.py:295`) the `steady_state_delta_T`
call, at `H_CONV=5.0` (confirmed at `run.py:184`, the unreplaced
macroscopic placeholder) — and `MASS_KG=1.0e-15` kg is a hardcoded literal
(`run.py:103`), not even derived from any geometric length. This is
actually a *worse* instance of the historical bug class than what exp-054
formally repudiates: not merely the wrong length, but a mass decoupled from
geometry entirely. I independently computed the margin from the committed
figure: `steady_state_dT_K_central = 0.0033108079151108792` K →
`0.020/0.0033108079151108792 = 6.0407×` — confirming THERMODYNAMICS'
"~6.04×" to 4 significant figures. This is the thinnest margin anywhere in
the thermal-detectability record by 2–3 orders of magnitude, confirmed by
grep across every `experiments/*/results.json` for a `graded_black_shell`
+ thermal-figure combination (only this one entry exists), and it is
**closer to the [0.020, 0.050] K NETD band than to zero** — `0.0033` K sits
roughly a sixth of the band's own lower edge away, not a comfortable
margin by the standard this program otherwise uses (every other article
sits 500×–27,000× clear). `stage18_length_scale_chain`'s three gates,
confirmed by direct read, touch only the ON-endpoint call site — none
would fire if `graded_black_shell`'s own thermal figure were re-run through
the still-uncorrected chain today. This is real, load-bearing, and — per
Red Team's own charter standard ("proposals that quietly violate a target
constraint") — is close enough to a program-integrity concern that I treat
it specially below (Checkpoint criterion 4).
The other two THERMODYNAMICS findings (unconditioned provenance string in
a "reusable" function; ~0.07% transcription slip in exp-045's SUPERSEDED
note, `2.235×10⁻⁶` vs. the actual `2.233484…×10⁻⁶` K) are both confirmed
directly, both real, both correctly triaged as non-load-bearing to any
standing classification.

**QUANTUM OPTICS (PARTIAL) — CONFIRMED, both findings real; the margin-
direction finding is the sharper one and converges with MATERIALS'.**
Mandatory fix 5's caveat confirmed present only in `NOTES.md`'s
idealizations list (lines 67-72), absent from P-054-3a/3b's own "Basis"
column (`NOTES.md:94-95`), and confirmed still citing the stale
`"P-054-3"` ID after the Phase-3 3a/3b split. Cheap, real, non-load-bearing
gap. The margin-direction finding (§ below) independently reproduces
QUANTUM's own arithmetic: `w_on_consistent_reference_dt_ss_full_K` (still
carried in `results.json::part_a`) implies an ON-endpoint margin of
`0.020/1.0875240683859519e-05 = 1839×`, vs. the mixed chain's 607× — same
3.03× shrink direction confirmed at the ON-endpoint reference pair as well,
independent of the dose-accumulation pair MATERIALS flagged.

**VISION SCIENCE (PROMISING) — CONFIRMED, all three findings real, none
load-bearing to numbers.** `run.py:266-275`'s six print statements,
confirmed by direct read, carry no disclaimer text or "NETD" instrument
qualifier. `NOTES.md` confirmed to end at line 107, at the frozen
predictions table, with no Results/Learned section. `LOGBOOK.md` confirmed
to carry no Iteration 31 / exp-054 entry (`grep` returns nothing). All
three are exactly as VISION describes — genuine but low-stakes gaps in an
otherwise unusually thorough disclaimer-propagation cycle (17
classification objects in `results.json`, each independently carrying its
own `disclaimer` field, confirmed by direct read).

## What all six missed

1. **`graded_black_shell`'s margin is not merely "uncorrected" — it sits
   close enough to the NETD band that a future, still-uncorrected citation
   of it (e.g., in a Checkpoint-1 candidate-reproduction claim) would be
   citing a number that could plausibly move classification if the
   mass/h_eff bug were fixed in the *unfavorable* direction.** THERMODYNAMICS
   frames the expected outcome of fixing it as "I'd expect the margin to
   clear the detectability floor comfortably once corrected" — but MATERIALS
   and QUANTUM's own convergent finding this same cycle (fixing the length
   scale on an already-gas-conduction-corrected chain *shrinks* the margin
   by ~3×) is direct evidence against that expectation being safe to assume.
   `graded_black_shell` never had its `H_CONV` placeholder replaced at all
   (unlike the ON-endpoint, which jumped 5.07×→607× on the placeholder fix
   alone), so its correction is dominated by a different, larger effect
   (H_CONV=5.0 → ~11,111 W/m²K is a ~2200× conductance jump) that will very
   likely dwarf the ~3× length-scale shrink — so THERMODYNAMICS' expectation
   is probably right in direction, but "probably right" is exactly the
   epistemic state this program's own house discipline (verify-before-claim)
   says should not be left standing at a Phase-5 close. This is not a new
   defect beyond THERMODYNAMICS' own finding 4, but it sharpens why finding
   4 is this cycle's single highest-priority follow-up rather than one
   entry among five roughly-equal ones (see ranked list below).
2. **No seat checked whether `stage18_length_scale_chain`'s gate 3 would
   have caught the `graded_black_shell` bug if it existed today at the
   ON-endpoint call site rather than a separate, unvisited one.** Confirmed
   directly: it would not — gate 3 pins one literal call site
   (`R_OUT_M` for the ON-endpoint only). This is the same point
   THERMODYNAMICS' finding 3 makes but stated here as a general property of
   the trust-suite design, not specific to `graded_black_shell`: **any**
   future article using the old chain is invisible to stage 18, not just
   this one. Confirms Red Team's own Phase-2 attack 4 hypothetical was
   right to flag this as a structural gap, not a one-off.
3. **`run.py`'s Part A `p_054_1_band` regression check (`[2.8e-5, 3.6e-5]`)
   and stage 18's regression anchor (`3.293076e-5 ± 1e-9`) are both anchored
   to the *same single* prior number (LOGBOOK Iteration 23's informal
   side-computation)** — meaning the trust suite's one "discriminating"
   gate and this cycle's own headline prediction pass/fail are not
   independent checks of correctness, only mutual consistency checks against
   one historical figure that was itself never independently re-derived by
   a second method until EM's Phase-5 RK4 closure (which covered
   Part B, not Part A). Low-stakes since EM's own from-scratch
   `dt_ss_full` re-derivation (Phase-5 review) matches to the last digit —
   but worth naming as a gap in independence, not just coverage.
4. **The exp-045 SUPERSEDED note (mandatory fix 7) actually states the
   margin-shrinkage direction correctly** ("by a margin ~3× narrower than
   this experiment's own original ~27,080× figure," `experiments/045-.../
   NOTES.md:501-503`) — this is a real, already-present partial mitigation
   of the MATERIALS/QUANTUM framing-risk finding that none of the six Phase-5
   reviews credited. The gap both seats correctly identify is that exp-054's
   *own* `NOTES.md`/`results.json` never states this directly (P-054-6's
   scope statement disambiguates only against the *unrelated* T8/T13
   witness-scale guess) — but a future cycle that reads the exp-045
   SUPERSEDED note itself (as this program's own T10 convention expects
   citers to do) would not be misled. The risk is specifically that a
   future cycle cites exp-054's *own* files without following the
   forward-pointer back to exp-045 — narrower than "this program's
   committed prose gets it backwards everywhere," which is not the case.

## Constraint-3/4 and T1 discipline at cycle end

Grepped every file in `experiments/054-heff-length-scale-rederivation/`
(all `.md`, `run.py`, `results.json`) for "constraint" and for T1-adjacent
language. Every occurrence of "constraint-3/4" is inside the standard
disclaimer sentence ("does NOT bear on constraint-3/4's human-eye
verdict") or a citation of that disclaimer requirement — zero
free-standing constraint-3/4 claims anywhere. `T1 escape route: NONE` is
stated in `phase1_proposal.md`, `NOTES.md`, and `results.json::meta`
identically, and is accurate: zero σ(I)/σ(x,t)/angular/sub-threshold
parameters are introduced or touched anywhere in this cycle's own code.
**Both hold clean at the end of the full cycle, independently confirmed,
not just carried forward from Phase 2.**

## PANEL.md Checkpoint criteria — explicit ruling on all five

1. **A configuration passes ALL constraint metrics.** Does not apply. This
   cycle proposes no mechanism and touches no constraint metric. **Does
   not fire.**
2. **A proven boundary — a constraint subset shown jointly unsatisfiable
   within a whole mechanism class.** Does not apply; no mechanism class is
   examined. **Does not fire.**
3. **Synthesis requires engine physics beyond the validated bench
   classes.** Zero new FDTD calls, confirmed (`results.json::meta.
   new_fdtd_calls: 0`, and independently: no scene/materials/emit call
   appears anywhere in `run.py`). **Does not fire.**
4. **Red Team flags program-integrity drift (unfalsifiable claims, a
   constraint quietly dropped — especially #3).** Scrutinized directly.
   No constraint is quietly dropped: constraint-3/4 language is disciplined
   throughout (above), and every NETD classification carries its own
   disclaimer at the point of computation. No claim in P-054-1 through
   P-054-8 is unfalsifiable — each carries a numeric band or exact
   identity a real run could (and in this case, did) test against. The
   closest candidate for a criterion-4 trigger is the convergent MATERIALS/
   QUANTUM finding that this cycle's own two headline articles report
   *smaller* margins than the record they supersede, without exp-054's own
   files stating that direction plainly — but this is a documentation
   completeness gap, not a dropped constraint or an unfalsifiable claim,
   and the correct direction *is* stated in the exp-045 SUPERSEDED note
   (finding 4 above). **Does not fire, but flagged as the nearest miss this
   cycle produced** — worth a same-shift, one-sentence fix (docket below)
   precisely so it never approaches this bar in a future cycle's citation
   chain. `graded_black_shell`'s thin, uncorrected margin (THERMODYNAMICS'
   finding) is a real program-integrity-adjacent concern but is not, itself,
   something this cycle's own record misrepresents — it is a *pre-existing*
   gap this cycle's scope correctly declined to expand into (T1: NONE,
   two named articles only), surfaced by contrast rather than created here.
   **Does not fire against exp-054 itself; recorded as a standing
   program-level flag for Iteration 32+ regardless.**
5. **Two consecutive iterations with no logbook-advancing result.** Does
   not apply — this cycle produces a real, code-committed, trust-suite-
   gated correction to a five-cycle-deferred tripwire, with two concrete
   headline numbers re-derived. **Does not fire.**

**No checkpoint criterion fires.** The program continues without
convening Marsh.

## Same-shift mandatory fixes (cheap, before this cycle is recorded closed)

These are all one-sentence-to-one-paragraph, zero-new-computation
corrections to already-written files — the program's own established
"same-shift disclosure fix" practice (distinct from Iteration 32+'s ranked
queue, which is for anything requiring new code or a new run).

1. **State the margin-shrinkage direction plainly in exp-054's own
   `NOTES.md`** (e.g., one sentence after P-054-6's scope statement): the
   corrected mixed-chain margins (607× ON-endpoint, ~8,955× dose-
   accumulation) are smaller than the `w_on`-consistent figures they
   replace (1,839× and 27,080× respectively) by ~3.03×, not larger — the
   safety improvement over the *pre-Iteration-20* placeholder-h_conv
   baseline is real and large, but the *length-scale* correction alone,
   in isolation, moves the dose-accumulation article toward detectable,
   not away. (MATERIALS finding 3 / QUANTUM finding 3, converged.)
2. **Add the same one-sentence caveat to `NOTES.md`'s P-054-6 row or a
   new idealization bullet**, cross-referencing the exp-045 SUPERSEDED
   note's own correct framing so the direction is stated at the locus
   future cycles are most likely to read first (this cycle's own frozen
   `NOTES.md`, not only exp-045's).
3. **Qualify `NOTES.md:18`'s "diffraction-inflated" phrase** with a
   footnote or parenthetical ("asserted, not independently bounded against
   the `iso_xsec_sq` convention artifact — see PHOTONICS Phase-2/Phase-5;
   does not affect this cycle's conclusion either way") at the hypothesis
   statement itself, not only buried in Phase-2/Phase-5 files. (PHOTONICS
   finding 1.)
4. **Fix P-054-3a/3b's "Basis" column** to carry mandatory-fix-5's caveat
   sentence (currently only in the idealizations list) and correct the
   stale `"P-054-3"` → `"P-054-3a/3b"` reference. (QUANTUM finding 1.)
5. **Append the NETD disclaimer (or a one-line pointer to it) after
   `run.py`'s six summary print statements** (lines 266-275). (VISION
   finding 1.)
6. **Correct exp-045's SUPERSEDED note**: `≈2.235×10⁻⁶ K` →
   `≈2.233×10⁻⁶ K` (or state to more decimal places to remove the
   ambiguity). (THERMODYNAMICS finding 2.)
7. **Write `NOTES.md`'s Results/Learned section and the LOGBOOK Iteration
   31 entry** (the two loci VISION found not-yet-written) — carrying the
   NETD disclaimer, and, per fix 1 above, the margin-direction statement.
   This is expected Director close-out work, not a defect, but is listed
   here since it is same-shift and mandatory-fix-6/1 both terminate at it.
8. **Flag `graded_black_shell_flagship` in the LOGBOOK Iteration 31 entry
   as a known, uncorrected, thin-margin (~6.04×) article still on the
   pre-Iteration-31 chain** — a one-paragraph disclosure, not a fix (the
   fix itself, replacing `H_CONV=5.0`/hardcoded `MASS_KG`/`w_on`-based area
   with the mixed chain, is real work and correctly belongs on the
   Iteration 32+ ranked queue, ranked #1 — see below). Recording the flag
   itself, however, costs one paragraph and should not wait for that
   cycle to run.

None of the above changes any `results.json` number, any pass/fail
verdict, or this cycle's own predictions — all are disclosure-completeness
corrections to prose, matching this program's own precedent (Iterations
17/21/23/29) for same-shift fixes that don't require re-running anything.

## Deferred to Iteration 32+ (requires new code or a new run — correctly NOT same-shift)

- Re-running `graded_black_shell` through the corrected mixed chain (real
  work: new `run.py` logic, a new results.json entry, likely a stage-18
  extension or a new trust-suite gate).
- Parameterizing `lumped_cube_mass_kg`/`mixed_length_scale_regime`'s
  fill-fraction and material-provenance strings (real code change).
- Promoting `coupled_segment_general` into a real trust-suite stage with a
  nonzero-IC numerical cross-check (real code change).
- The Q_ext(x) closed-form check, the 3λ mixed-chain sweep, T8/T13's
  witness-scale bridge, and the sourced-citation search for the silicon
  identity — all require new analysis or a new search, not prose edits.

## Overall verdict: **PROMISING**

The core physics argument (mixed chain: absorbed power stays on the
calibrated optical length `w_on`; thermal mass, convective conductance, and
radiating area move to the geometric length `r_out`) is sound, was
independently re-derived by three seats (EM algebraically, THERMODYNAMICS
numerically, PHOTONICS via direct code execution) and by this audit, and is
now real, trust-suite-gated, reusable code — not a one-off script or a
hand-typed number. All seven of Phase 2's mandatory fixes were genuinely
implemented in code and results, not merely asserted; all eight
pre-registered predictions passed on their own committed bands; T1 and
constraint-3/4 discipline hold clean throughout. This is not RULED OUT —
nothing found here, by any seat or this audit, contradicts the mixed-chain
argument or invalidates either of its two completed results.

It stops short of an unqualified PROMISING-with-no-reservations for three
convergent reasons, none of which threatens a currently-standing number:
(a) the corrected margins are smaller, not larger, than the record they
supersede, and that direction is not yet stated plainly at every locus a
future citer is likely to read (same-shift fix, above); (b) the trust
suite protects only the two call sites this cycle actually touches, and
the one pre-existing article sitting closest to the detectability floor in
this program's entire record — `graded_black_shell` — remains on the
repudiated chain, unflagged until this review; (c) several disclosure
loci (NOTES.md prose, LOGBOOK entry, run.py console output) are genuinely
incomplete, independently confirmed by three different seats reaching the
same class of finding from different angles. None of (a)-(c) is a
correctness defect in the numbers delivered; all three are cheap to close.
**PROMISING**, contingent on the mandatory-fix docket above landing before
this cycle is recorded in LOGBOOK.md as closed.

## Ranked candidate directions for Iteration 32+ (reconciling all six seats + this audit)

1. **Re-run `graded_black_shell` through `mixed_length_scale_regime`**,
   replacing its hardcoded `MASS_KG=1e-15`, `H_CONV=5.0`, and
   `w_on`-based area with the corrected chain. (THERMODYNAMICS #1; this
   audit's own top priority — the program's flagship article, at the
   record's thinnest margin, on a chain this program has now formally
   repudiated twice, and the one place a future Checkpoint-1 claim would
   most likely cite a stale number.) Cheapest same-pattern desk-analytic
   work available; one afternoon.
2. **Promote `coupled_segment_general` into a real trust-suite stage**
   with a numerical-integrator cross-check at nonzero `(n0, dT0)` — EM's
   Phase-5 RK4 closure already did the verification work once; this only
   needs to be committed as a permanent gate. (EM #1.)
3. **Parameterize `mixed_length_scale_regime`'s fill-fraction and
   material-provenance strings** so a future caller with a genuinely
   different or sourced material doesn't inherit exp-054's own
   silicon/ASSUMED-T18 citation, and so a future sensitivity sweep on
   fill fraction is possible against the new module (not just the old
   script it replaces). (MATERIALS #1, THERMODYNAMICS #2, converged.)
4. **The desk closed-form `Q_ext(x)` cylinder/disk check** — bounds how
   much of `w_on`'s ~3.03× excess over `r_out` is genuine diffraction vs.
   an `iso_xsec_sq` convention artifact. Named by four of six seats
   (PHOTONICS #1, EM #2, THERMODYNAMICS #3, QUANTUM #4) as informative for
   the load-bearing premise the whole `r_out`-vs-`w_on` split rests on,
   and Red Team's own Phase-2 audit already queued it. Zero new FDTD,
   closed-form only.
5. **Run the mixed chain (ON-endpoint + Block C) across the standard
   450/600/750nm sweep**, reusing exp-026/044's already-committed per-λ
   `sigma_ext`/`sigma_abs` values — converts PHOTONICS' own back-of-
   envelope "~4% shift, probably fine" into a checked number at zero new
   FDTD cost. (PHOTONICS #2.)
6. **T8/T13/T14's near-field→witness-scale `h_eff` bridge.** The largest
   standing gap in the thread, correctly and explicitly left open again
   this cycle (P-054-6). Named by every seat that discussed scope as the
   natural next link. Ranked lower only because it is the biggest build
   of the six, not because it matters less — LOGBOOK.md should keep it
   live as this program's own oldest unclosed sidecar thread.
