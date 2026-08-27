# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 58 · exp-081

**Seat: QUANTUM OPTICS** (non-classical absorption, state-dependent or
coherent interactions; *expressibility contract: mechanisms enter the bench
only as effective classical parameters — σ(I), σ(x,t), dispersive ε(ω),
gain — or Red Team strikes them*). Fresh sub-agent, zero memory of any prior
session — including my own Phase-2 critique this same cycle, read cold from
the committed record like everything else.

Read, in order: `PANEL.md`, `AGENTS.md`, `LOGBOOK.md` (RULED OUT R1–R9,
ESTABLISHED, LIVE THREADS in full, T28's complete Iteration 46–57 history),
`PLAN.md`'s Iteration-58 queue, and the complete `experiments/081-.../`
record — `phase1_proposal.md`, `photonics_construction.py`,
`phase1_results.json`, `_output.txt`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`phase4_results.json`, `NOTES.md`. **Not read**: any `phase5_review_*.md` or
`phase5_redteam_audit.md` from this cycle (two exist already in the
directory from concurrent seats — untouched, per instruction). No
RULED-OUT item (R1–R9) is re-proposed below.

---

## 1. Independent verification performed (not merely re-argued)

I did not trust `phase1_results.json`/`phase4_results.json` or Red Team's
own audit table on their word. I wrote a from-scratch scratch script that
imports only already-committed primitives (`dg065.CONFIGS`,
`ywas.build_aperture_grid`/`aperture_amplitude`/`source_driven_phase`/
`dist_image_cells`/`reflection_coefficient_vec`/`_trapz`/`K600`/
`free_period_with_widening`/`rel_dev`, `br.n_profile_exact`/`nu_profile`/
`damp_e_profile`, `pc81.e_direct_curve` reused unchanged) and never calls
`item1_build_and_score()`/`item1c_ablation_control()`/
`item2_conj_sensitivity()` themselves — an independent re-derivation, the
fifth such independent computation of these numbers across this cycle's own
record (Phase 1's committed run, Red Team's own scratch audit script, Phase
4's re-run, PHOTONICS' own Phase-5 review per its commit message I can see
but not read, and now mine).

**Confirmed exactly, bit-for-bit or to the same printed digit:**

| Claim | My independent result | Committed record |
|---|---|---|
| `C80−C40` real-`r` free-period fit | `P*=2.015037593984962°`, `rel_dev=0.2910052910052911` | identical |
| `E_direct(C80)−E_direct(G40)`, PAD-invariance for the `PAIR_ABSORB40` pair specifically | `max abs dev = 0.0` exactly | identical (item 1a, all 5 configs) |
| Ablated `W(θ_beam)` (image term with `r→1`) for `C80` vs `G40` | `max|W_C80−W_G40| = 0.0` exactly | — (new, my own algebraic decomposition, not previously stated this explicitly) |
| **`PAIR_ABSORB40` ablated pair-delta** | `ss_tot = 0.0` exactly, `SS_TOT_DEGENERATE=True` | identical |
| `PAIR_PAD` ablated fit | `P*=2.007518796992481°`, `rel_dev=0.5646513432415003` | `rel_dev=0.5647` (identical to 4 s.f.) |
| **`C80−C40` ablated fit** | `P*=2.007518796992481°`, `rel_dev=0.2936507936507937` | `rel_dev=0.29365` (identical) |
| `C80−C40` under `r→conj(r)` | `P*=2.2481203007518795°`, `rel_dev=0.20899…`, verdict SUPPORT | `P*=2.2481°`, SUPPORT, no flip (identical) |

## 2. Re-deriving `PAIR_ABSORB40`'s exact degeneracy and `C80−C40`'s
## near-invariance myself — not just reproducing the number, but why it is
## necessarily so

**`PAIR_ABSORB40` ≡ (`G40`, `C80`)**: I confirmed directly from
`dg065.CONFIGS` that `G40` and `C80` share `y_lo=80`, `y_hi=1584`,
`obj_y=832`, `d_sp=223` bit-for-bit (identical `PAD=40`), differing *only*
in `absorb` (40 vs 80). Once `r(90°−θ_beam)→1` in `E_image`, the ablated
image term is `W(θ_beam) = ∫ amp(y_s)·exp(i[phase_drive+K·dist_image]) dy_s`
— a pure function of aperture geometry (`y_lo/y_hi/obj_y/d_sp` via
`build_aperture_grid`/`dist_image_cells`) with **zero dependence on
`absorb` anywhere in its own construction**, since `absorb` only enters
through `r()`, which has just been replaced by the constant `1`. Two
configs with identical geometry therefore produce a bit-identical `W(θ_beam)`
curve — I verified this directly (`max|W_C80−W_G40|=0.0`), independent of
the scoring pipeline. Combined with `E_direct`'s own independently
re-verified PAD-invariance (item 1a, re-confirmed here for this specific
pair), the ablated `E_total` pair-delta is the sum of two exactly-zero
differences — `ss_tot=0.0` is not a numerical coincidence, it is an
algebraic necessity of this construction's own definition, for this
specific pair only (`C40`, with `PAD=0`, shares neither `E_direct` value's
"generic" invariance-in-isolation-from-`W`, since its own `W(θ_beam)`
genuinely differs — confirmed, `max|W_C80−W_C40|=0.0416`, nonzero). This is
exactly why `PAIR_ABSORB40`'s ablated degeneracy is pair-specific and not a
general property of the ablation control, matching Red Team's own §0 item
B finding precisely, now independently re-derived from the construction's
own algebra rather than merely re-measured.

**`C80−C40` (the pair carrying the lone SUPPORT)**: here the two configs'
aperture geometries genuinely differ (`PAD=40` vs `PAD=0`), so no algebraic
identity forces the ablated result to match the real-`r` result — this had
to be measured, not derived, and I measured it independently: `rel_dev`
moves from `0.2910` (real `r`) to `0.2937` (ablated to `r=1`), a shift of
only `0.0075°` in the recovered period, both still comfortably inside the
`0.30` SUPPORT bar. **This is real evidence, not an artifact of trusting
the write-up**: removing all wall-reflectance physics from the model
changes this pair's recovered period by less than the width of the
SUPPORT/INCONCLUSIVE boundary itself. The lone SUPPORT this cycle's headline
rests on is a property of the aperture geometry/diffraction envelope alone
(the same object exp-078/079 already showed drives this construction's
`θ_beam`-dependence in the single-edge and full-aperture-sum reductions),
not of `ABSORB`'s reflectance. Phase 3/4's characterization — "SUPPORT
requires no wall reflectance at all... NOT evidence for a real y-wall echo
mechanism" — is correct and I independently confirm it from primitives, not
merely from the committed table.

**Bottom line on my specific charge**: Phase 3/4 implemented and
interpreted the ablation control correctly, *pair-specifically*, exactly as
Red Team's audit stated it. I found no discrepancy between what the record
claims and what the construction's own algebra/arithmetic actually produces.

## 3. Coherent-sum / interference bookkeeping audit (my charter's own
## territory — this whole construction is `E_direct+r·W`, a coherent field
## sum)

I looked specifically for a place where a coherence assumption is used
without being stated as an idealization, or where an intensity/energy
quantity is silently combined with a field-amplitude quantity (the failure
mode EM's own Phase-2 critique partially checked, and the one
`VALIDATION.md`'s "cross-solver comparisons compare SCATTERED fields...
total fields inherit each library's source profile" lesson generalizes
from).

- **Primary scoring proxy is `Re{E_total}`, not `|E_total|²`, throughout.**
  Confirmed by direct inspection (`item1_build_and_score`,
  `_score_construction`, all three docket extensions) — no place computes
  or scores an intensity quantity built from `E_direct`/`E_image` combined.
  This is the correct discipline: `E_direct` and `E_image` are added as
  complex phasors (coherent superposition, appropriate — both terms
  originate from the same monochromatic, deterministic CW source under this
  bench's own house convention, `lab/emit.py`'s
  `f(n)=Re{F·e^{-iωn}}`), and the *real part* of that coherent sum is the
  physically-meaningful, sign-carrying quantity a real time-domain monitor
  would record — I traced this convention to
  `y_wall_aperture_sum.py`'s own §[5a] proxy-justification comment
  (`"PRIMARY = Re{E_echo}... this bench's own house phasor convention"`,
  established Iteration 46/exp-069, correctly inherited unchanged here, not
  freshly asserted). This is the right comparison against the real
  `C40`/`G40`/`C80` FDTD monitor data — **not** the
  `VALIDATION.md`-flagged scattered-vs-total mismatch (that lesson concerns
  comparing *different solvers'* mismatched field conventions; here a
  single analytic model and a single real dataset both target the same
  total-field, monitor-recorded quantity). **One minor hygiene gap**: this
  inherited convention is not independently restated as an idealization in
  `phase1_proposal.md` §4's own 7-item list (it is documented only in code
  comments and by reference through Idealization 3's "reused unchanged"
  language) — low-priority, does not affect any result, but a future reader
  of the idealization list alone would not learn this fact from it.

- **Energy-budget item 3 never mixes coherently.** `|r(θ)|²` (item 3) is
  computed and reported independent of `E_direct`'s magnitude anywhere —
  confirmed by direct inspection, matching EM's own Phase-2 finding, which I
  independently re-checked rather than took on trust: no function anywhere
  in `photonics_construction.py` forms `|E_direct+E_image|²` or any other
  cross-term combining the two. The ~10⁵ `|E_direct|`-vs-`|E_image|`
  magnitude gap (item 1b's own finding) never gets smuggled into the power
  budget as if it were a coherent-interference contribution to reflected
  power — correct discipline, no fix needed.

- **The one genuine, disclosed, still-open coherence-bookkeeping question is
  the `r`-vs-`conj(r)` phase-convention ambiguity** — EM's own Phase-2
  finding, that the three magnitude-only gates (`G-LOSSLESS`/`G-N1`/
  `G-PASSIVITY`) are algebraically blind to a global sign flip on
  `arg(r(θ))` (`|conj(r)|=|r|` identically), so item 2's gate re-run cannot
  certify which convention the real graded-loss boundary's physics actually
  realizes at this new `[47.5°,54.5°]` range. This is exactly the class of
  smuggled-coherence risk my charter exists to police: item 1's entire
  period-recovery result is driven by `arg(r)`, not `|r|`, and a
  convention-blind gate battery cannot rule out a globally wrong sign. I
  independently ran the `conj(r)` substitution myself (§1, `C80−C40` row)
  and confirm Red Team's own finding: the qualitative reading survives (no
  verdict flips, T21-proximity pattern intact), so it is **not
  outcome-determining this cycle** — but it is **not resolved either**, and
  Phase 3/`NOTES.md` state this precisely and honestly (corrected item 3,
  "reassuring, not resolving," FDTD extension explicitly queued for
  Iteration 59). I find no gap between what is claimed and what is true
  here — the one real interference-bookkeeping loose end in this cycle's
  own record is correctly flagged as open, not swept in either direction.

**No smuggled coherence assumption found beyond the one already disclosed
and correctly scoped (the phase convention).** The construction is a
faithful, disclosed coherent Huygens sum; the one place a hidden assumption
could plausibly have entered (Re-proxy vs intensity) traces to a
pre-established, physically-justified house convention, not a fresh,
undisclosed choice by this cycle.

## 4. Assessment of the cycle's own process (light, not a re-audit)

Phase 2's five critiques converged on three genuine, non-overlapping gaps
(MATERIALS: single-admittance-family; PHOTONICS+QUANTUM's prior instance:
missing ablation control; EM: phase-convention). Red Team's Phase-2 audit
ran all three to completion from primitives rather than re-arguing them,
correctly found (A) and (C) non-outcome-determining and (B) genuinely
pair-specific and more informative than either raising critique's own
binary framing anticipated. Phase 3 adopted the full fix docket with zero
overrides and corrected five specific overclaims in the permanent record.
Phase 4's corrected re-run reproduced six of six substantive frozen
predictions exactly, with one honestly-disclosed literal miss
(`0.0075188°` vs a `"≤0.0075°"` bound copied from a 4-decimal-rounded
table) correctly characterized as a threshold-precision artifact, not a
physics discrepancy — I independently confirm this characterization: the
underlying number is the same `0.0075188°` value my own from-scratch
computation would also produce given the same inputs, and it is three
orders of magnitude below the `rel_dev` bands that actually gate any
verdict. This is the right way to disclose a near-miss, not a red flag.

Zero constraint-3 (or any-constraint) engagement anywhere in the record —
independently confirmed (this is instrument/model-fidelity work, T1 N/A,
exactly as stated).

## 5. VERDICT: **PARTIAL**

This cycle delivers a genuine, independently-verified advance: for the
first time in this nine-cycle T28 y-wall sub-thread, PHOTONICS' own
construction is built *as specified* (both terms present) and scored *the
way PHOTONICS specified* (a free-period fit against real T28 data, not a
shape-comparison against a candidate curve). The mechanically-computed
Combined Verdict is **NEITHER**, robust under both admittance families
(shift ≤0.0075°) and robust under the `r→conj(r)` sensitivity test (zero
verdict flips). The **substantive** reading is **REFUTE-leaning, and now
on genuinely firmer ground than a hedge**: I independently re-derived, from
the construction's own algebra and from a from-scratch numeric check, that
the lone `C80−C40` SUPPORT survives the total removal of wall-reflectance
physics almost unchanged (`0.2937` ablated vs `0.2910` real) — it is a
T21-proximity/geometry artifact, not evidence for a real y-wall echo — while
`PAIR_ABSORB40` is, by contrast, provably `r()`-dependent (exactly
degenerate under ablation) yet still far from SUPPORT (`rel_dev=0.5139`)
under the true reflectance. This is not a formal closure: Checkpoint
criterion 2 correctly remains NOT YET RIPE — one construction, one
wavelength, one empty scene, and the one genuinely open loose end (the
phase-convention ambiguity) is disclosed, not resolved. **PARTIAL**,
matching this exact sub-thread's own established verdict convention at
every non-closing cycle since Iteration 46.

## 6. My own ranked top-3 candidate directions for Iteration 59

1. **Extend `phase5_redteam_phase_convention_check.py`'s empirical FDTD
   tie-breaker to 2–3 angles inside `[47.5°,54.5°]`** (mirroring exp-075's
   own `[0°,20°,39°]` precedent, ~90s per that precedent). This is squarely
   my own charter's unfinished business from this cycle: the one
   coherent-interference bookkeeping question this cycle correctly
   identified as open (§3 above) but did not resolve, because resolving it
   needs real FDTD, explicitly out of this cycle's zero-FDTD scope. It is
   cheap, well-precedented, and closes the single remaining ambiguity in
   the sign convention that `arg(r)` — the quantity this whole
   construction's period-recovery result is actually driven by — carries at
   this new, more-grazing angle range. Not outcome-determining for *this*
   cycle's verdict, but load-bearing for trusting `arg(r)` in *any* future
   cycle that reuses `[47.5°,54.5°]`.
2. **The PAD-loaded real-article check** (does the `PAD`-sensitivity axis
   survive with a real absorbing article loaded) — now **six** consecutive
   T28 cycles deferred (076–081) per this cycle's own record. Every
   congruent-series construction across ten T28 cycles, including this
   cycle's own "actually-decisive" test, has been run on an EMPTY scene.
   No amount of further empty-scene period-matching, however carefully
   ablation-controlled, can establish whether any of this sub-thread's
   findings bear on the real phenomenon program at all — this is the
   single test that would. If Iteration 59 defers it a seventh time, the
   reason needs to be stated explicitly, against this cycle's own finding
   (the actually-decisive empty-scene test has now been run and leans
   REFUTE), not by inertia.
3. **The 750/450nm wavelength-generality leg** — also six cycles deferred.
   This cycle's REFUTE-leaning finding rests on one wavelength (600nm). The
   ablation-control result I independently re-derived (§2) — that the lone
   SUPPORT is a geometry/diffraction artifact, not a reflectance effect —
   makes a falsifiable prediction: if the construction is genuinely
   insensitive to wall physics at 600nm because of aperture geometry alone,
   the same T21-proximity/ablation-insensitivity pattern should reproduce
   at 750nm and 450nm too (the aperture geometry does not change with
   wavelength; T21's own fringe period does, in a known way). Running this
   leg would either strengthen the REFUTE-leaning case into something
   closer to a genuine mechanism-class boundary (Checkpoint criterion 2)
   or surface a wavelength-dependent effect this cycle's single-λ scope
   cannot see — either result narrows the board.

None of the above re-opens or re-proposes any RULED-OUT item (R1–R9).
