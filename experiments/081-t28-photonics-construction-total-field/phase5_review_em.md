# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 58 · exp-081

**Seat: ELECTROMAGNETISM** (field/wave behavior, impedance matching, energy
coupling — owns the reciprocity/passivity/causality bookkeeping, formalizes
what T1 permits and forbids). Fresh sub-agent, zero memory of any prior
session. Blind to any other seat's current-cycle Phase-5 review.

Read, in order: `PANEL.md` in full, `AGENTS.md` in full, `LOGBOOK.md`
(RULED OUT R1–R9, ESTABLISHED, LIVE THREADS in full including T28's complete
Iteration 46–57 history), `PLAN.md`'s Iteration-58 queue, and the complete
`experiments/081-.../` directory (`phase1_proposal.md`,
`photonics_construction.py`, `phase1_results.json`, `_output.txt`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`/`.json`, `NOTES.md`). This cycle's Phase-2 EM critique
(reproduced above the fold in this record, not authored by me) flagged that
item 2's gate re-run is magnitude-only and cannot resolve the `r` vs
`conj(r)` phase-convention ambiguity — I independently re-verify below that
Phase 3/4 disclosed this honestly rather than quietly dropping it, and I ran
my own checks beyond re-reading the record. No RULED-OUT item (R1–R9) is
re-proposed.

---

## 1. Did Phase 3/4 honestly disclose the `r`-vs-`conj(r)` gap, or overclaim resolution?

**Honestly disclosed, correctly queued — confirmed by independent
re-reading and by my own from-scratch re-execution of the script.**

- `phase3_synthesis.md` §2 item 3 states plainly: item 2's magnitude-only
  gates "do NOT resolve the `r` vs `conj(r)` phase-convention ambiguity,"
  corrects `NOTES.md`'s pre-audit "can be trusted going forward" language to
  state precisely what a magnitude-only battery establishes (algebraic
  self-consistency, `|r|≤1`) and does not establish (the sign/phase
  convention the period-recovery result is actually driven by), and states
  the `conj(r)` sensitivity result (no verdict flips) is **"reassuring, not
  resolving."**
- The real fix — extending `phase5_redteam_phase_convention_check.py`'s
  empirical FDTD tie-breaker to 2–3 angles inside `[47.5°,54.5°]`, mirroring
  exp-075's own `[0°,20°,39°]` precedent — is **explicitly queued for
  Iteration 59**, not run this cycle (Idealization 7, zero new FDTD), in
  `phase3_synthesis.md` §2 item 3, `phase2_redteam_audit.md`'s fix-docket
  item 3 and its §5 "Note for Iteration 59," and `NOTES.md`'s own Phase-3/
  Phase-4 sections (which state the phase-convention question "remains
  genuinely open... but is shown not to be outcome-determining for this
  cycle's own verdict").
- This is exactly the discipline R8 exists to require (a named, affordable
  check either run or explicitly queued, not silently dropped) and is the
  correct application of it: unlike exp-075's own R8-triggering precedent
  (where an *untested* robustness argument was adopted and later proved
  outcome-determining), this cycle actually **ran** the convention-flip
  sensitivity test (a cheap, zero-FDTD substitution, not the full empirical
  resolution) and reports its result as bounding, not closing, the question.
  That is a materially different — and correct — disposition, not a repeat
  of R8's failure shape.

**No quiet dropping anywhere in the chain.** I checked `git log` for
exp-081: `522e9fb` (Phase-3 FROZEN PREDICTIONS) precedes `c2bd9c2` (Phase-4
run) as two genuinely separate commits, restoring exp-080's own two-commit
standard per the fix docket — so the "queued for Iteration 59" commitment is
itself pre-registered in git, not merely asserted in prose after the fact.

## 2. Independent check: does `conj(r)` really produce zero verdict flips?

**Yes — independently reproduced from a clean re-run of the committed
script**, not merely re-read from `phase4_results.json`. I executed
`photonics_construction.py` myself against the current repo state
(`main()` + `main_phase4()`) and obtained, bit-for-bit, the same numbers
already on record:

| pair | `P*` matched | `P*` conj(r) | verdict matched | verdict conj(r) | flip? |
|---|---|---|---|---|---|
| `PAIR_PAD` | 1.8571° | 2.1278° | INCONCLUSIVE | INCONCLUSIVE | No |
| `PAIR_ABSORB40` | 2.0301° | 2.4887° | INCONCLUSIVE | INCONCLUSIVE | No |
| `C80−C40` | 2.0150° | 2.2481° | SUPPORT | SUPPORT | No |

I hand-checked the two most consequential entries against the reported
reference periods (`4.6113°`/`4.1761°`/`2.8421°`): `PAIR_PAD`
`rel_dev=|4.6113−2.1278|/4.6113=0.5385` (>0.30, ≤1.00 → INCONCLUSIVE,
consistent with the printed table); `C80−C40`
`rel_dev=|2.8421−2.2481|/2.8421=0.2090` (≤0.30 → SUPPORT survives,
consistent). **Confirmed: the `conj(r)` substitution genuinely produces zero
verdict flips across all three pairs**, and the script's own internal
reproduction check (`item1_original_run_reproduces_committed`) — which I
also re-ran fresh rather than trusting — is bit-exact against the committed
`phase1_results.json`.

**One qualification worth recording for Iteration 59, not raised in the
existing record**: `C80−C40`'s insensitivity to `conj(r)` is largely a
**restatement** of Attack 2's ablation finding (that pair survives `r()→1`
almost unchanged, `0.2937` vs `0.2910`), not an independent data point —
a pair whose recovered period barely depends on `r()`'s value at all cannot,
almost by construction, be very sensitive to which *sign* of `r()` is used
either. The genuinely informative instances are `PAIR_PAD`/`PAIR_ABSORB40`,
which the ablation control shows really do depend on `r()`, and which
*also* show no verdict flip under `conj(r)` — that is the actual evidence
that the sign ambiguity is (for this cycle's Combined Verdict specifically)
not outcome-determining. Both docket items are correctly reported as
separate findings, but a reader should understand they are not three fully
independent confirmations — closer to two, with the third partly implied by
one of the other two.

## 3. Is `E_direct`+echo combined in an energy/passivity-consistent way?

**Yes, throughout Phase 3/4's additions, confirmed by direct code
inspection.** Every scoring path in this cycle — `item1_build_and_score`,
and the shared `_score_construction` underlying all three Phase-3
extensions (`item1_admittance_family_rescore`, `item1c_ablation_control`,
`item2_conj_sensitivity`) — forms pair-deltas on `Re{E_total}` only, a
**coherent field (amplitude) superposition**, and never elevates `E_total`
to an intensity/power quantity (`|E_total|²`) anywhere. `item3_energy_budget`
is a fully separate code path that prices `|r(θ)|²` alone and never
references `E_direct`'s magnitude. This matters specifically because
`|E_direct|≈89–111` is 4–5 orders of magnitude larger than
`|E_image|≈1.3×10⁻⁴`–`3.5×10⁻³` (item 1b's own finding): had any quantity in
this cycle formed `|E_total|²` directly, the cross term
`2·Re{E_direct*·E_image}` would be ~10²–10⁵× larger than `|E_image|²`
itself and could trivially fake an `E_image`-driven signal that is actually
carried by `E_direct`'s own beat against itself across configs — exactly the
kind of energy-bookkeeping trap this seat's charter exists to catch. This
cycle avoids it entirely, correctly, by construction (linear superposition,
scored linearly, never squared) — not by luck.

The dominance ratio itself is why `E_direct` cancels to `~10⁻¹⁴` rather than
literally `0.0` in item 1b (floating-point subtraction of two `O(100)`
analytically-equal numbers) — a fact this cycle traces and discloses
correctly (Phase-2 EM critique's steel-man already credits this; I confirm
it independently: `10²×2.2×10⁻¹⁶≈2×10⁻¹⁴`, matching the observed residual
to within a factor of ~1.5, consistent with accumulated rounding across the
aperture integral rather than a single subtraction).

## 4. Is the `r()→1` ablation control a physically sound diagnostic?

**Sound, and I found it to be more robust than the record currently shows —
this is new information, run independently this Phase-5 cycle.**

`|r|=1` sits exactly on the boundary of the passive set (`|r|≤1`), not
outside it — it is not a passivity violation. It represents an idealized,
lossless, fully-reflecting boundary with **zero intrinsic phase shift**, and
functions as a "material-response-off" null control: it strips `r(θ)`'s own
angle/`ABSORB`-dependence entirely while preserving the coherent propagation
phase (`K·dist_img`) and the aperture geometry (`W(θ_beam)`) untouched. This
is the same idealization *class* as item 3's interception-factor-of-1 bound
(a deliberately extreme, diagnostic idealization, not a physical claim about
the real boundary) and is not this cycle's own invention — it is inherited,
unchanged, from `y_wall_aperture_sum.py` §[7], itself a Phase-2
mandatory-fix item from exp-079 (Iteration 56), already reviewed once.

**The question I checked that nobody in this cycle's record raised**: is
the specific *phase* of the ablation constant (`+1`, i.e. zero phase) itself
a hidden convention choice that could bias the diagnostic's own conclusions,
the same way `r`'s own sign convention biases item 1's headline result? I
tested this directly (not committed to the repo — a scratch check, reused
only already-committed, already-gated primitives, same discipline Red
Team's own audit script used) by re-running the ablation with the constant
set to `−1`, `i`, and `e^{iπ/4}` instead of `+1`:

| pair | `φ=0°` (`r=+1`) | `φ=90°` (`r=i`) | `φ=45°` | `φ=180°` (`r=−1`) |
|---|---|---|---|---|
| `PAIR_PAD` | `P*=2.0075°`, INCONCLUSIVE | `P*=2.0150°`, INCONCLUSIVE | `P*=2.0150°`, INCONCLUSIVE | `P*=2.0075°`, INCONCLUSIVE |
| `PAIR_ABSORB40` | `P*=1.0000°` (degenerate) | same | same | same |
| `C80−C40` | `P*=2.0075°`, SUPPORT | `P*=2.0150°`, SUPPORT | `P*=2.0150°`, SUPPORT | `P*=2.0075°`, SUPPORT |

Real constants (`±1`) give bit-identical periods (an overall real sign flip
does not change a real curve's periodicity, only inverts its crests and
troughs — this is why the `±1` check alone would have told nobody anything).
A genuine complex phase (`i`, `45°`) does shift the recovered periods
slightly (`≤0.0075°`, the same order of magnitude as the matched-vs-
realizable-admittance shift item 1 already treats as "not
outcome-determining") — **but produces zero verdict flips and leaves
`PAIR_ABSORB40`'s exact degeneracy untouched at every phase tested**
(`PAIR_ABSORB40`'s degeneracy is in fact *guaranteed* independent of the
ablation constant's phase by construction: `G40`/`C80` share identical
`(obj_y,y_lo,y_hi)` geometry under `PAD=40`, so ANY config-shared constant —
real or complex — makes their image terms identical, a purely geometric fact
this cycle's own record already states for the `r=1` case but had not
generalized). **This strengthens, not undermines, the ablation control's
own conclusions**: the pair-specific finding (`PAIR_ABSORB40` genuinely
`r()`-dependent, `C80−C40`'s SUPPORT nearly `r()`-independent) is robust to
the convention question I raised, not merely correct for the one phase
choice that happened to be tested.

## 5. Verdict

**PARTIAL** — matching this cycle's own Combined Verdict and this
nine-cycle T28 y-wall sub-thread's own established disposition, independently
reconfirmed here, not merely inherited.

This cycle delivers a genuine, load-bearing advance: PHOTONICS' construction
built and scored exactly as originally specified, for the first time, with
an honestly-disclosed literal self-falsification (item 1b) and a
Red-Team-run set of completeness checks (admittance family, ablation
control, phase-convention sensitivity) that sharpen the result rather than
merely re-arguing it. From this seat's own charter: the energy/passivity
bookkeeping is clean throughout — no incoherent combination of `E_direct`
and `E_image` anywhere, the dominance-ratio-driven `~10⁻¹⁴` residual is
correctly traced rather than smoothed, the `r`-vs-`conj(r)` gap is disclosed
honestly and queued rather than dropped, and the `r()→1` ablation control is
a sound diagnostic that — checked here independently — turns out to be
robust to a convention question nobody had yet posed. None of this reaches
"promising" (T1 escape route is explicitly N/A; zero constraint-3
engagement; this is instrument-fidelity work on an unexplained numerical
periodicity, not a phenomenon-program mechanism). None of it is "ruled out"
either, at the cycle level: no claim in the record fails independent
re-derivation, and Checkpoint criterion 2 is correctly left NOT YET RIPE —
this is a single result, on one construction, one wavelength, one
(still only partially convention-verified) angle range, on an empty scene.

## 6. Ranked top-3 candidate directions for Iteration 59

1. **Run the actual FDTD phase-convention extension now, before it becomes
   a second lapsed cycle.** `phase5_redteam_phase_convention_check.py`
   already exists, is cheap (exp-075's own battery ran in ~90s), and this
   cycle's own record (Phase 3, Red Team's fix docket, and my own
   independent re-confirmation above) all name the exact extension needed:
   2–3 angles inside `[47.5°,54.5°]`, calibrated the same way as the
   `[0°,20°,39°]` precedent. This is the highest-value item specifically
   because it is the one open question this cycle's own sensitivity checks
   (mine included) can bound but cannot close — every convention-robustness
   result so far is reassuring, and reassuring is not resolving.
2. **The PAD-loaded real-article check** (PLAN.md's Tier-2 item, now six
   consecutive T28 cycles deferred as of this iteration). This cycle's own
   REFUTE-leaning finding for the plane-wave/global-steering construction
   was obtained entirely on an empty scene — every congruent-series config
   across all nine T28 y-wall cycles has been. If Iteration 59 defers this a
   seventh time, PLAN.md's own standing rule requires the reason be stated
   explicitly, not by inertia; from this seat's charter, an empty-scene
   result cannot itself certify a passivity/energy argument extends to a
   loaded scene, and this is now the single most information-dense
   untested axis on the whole T28 board.
3. **The 750/450nm wavelength-generality x-wall leg**, now six consecutive
   cycles deferred. Every quantitative finding this cycle produced —
   the admittance-family insensitivity, the ablation-control pair
   specificity, the phase-convention insensitivity I re-confirmed above —
   is a single-wavelength (600nm) result. A construction whose own author
   predicted its dominant recovered period would track T21's established
   fringe (itself only established at 600nm in this exact form) deserves
   the same 3-λ scrutiny every other T28/T21 finding in this program has
   received before Checkpoint criterion 2 is asked to weigh in.

No RULED-OUT item (R1–R9) is re-proposed by this review or by any ranked
item above.
