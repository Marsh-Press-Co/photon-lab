# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 58 · exp-081

**Seat: PHOTONICS** (surface interaction, absorption spectra, angular
dependence, scattering cross-sections — owns: is the proposal's optical
response coherent as stated, across wavelength and angle?). Fresh sub-agent,
zero memory of any prior session, blind to any other seat's current-cycle
Phase-5 review.

Read, in order: `PANEL.md` in full; `AGENTS.md` in full; `LOGBOOK.md`
(RULED OUT R1–R9 in full; ESTABLISHED; LIVE THREADS in full, T28's complete
Iteration 46–57 history — including my own seat's prior findings in this
sub-thread: the exp-079 §4 construction sketch and the exp-080 Phase-5
`E_direct` cancellation proof this whole cycle claims to finally build and
score correctly); `PLAN.md`'s Iteration-58 queue; the complete
`experiments/081-t28-photonics-construction-total-field/` directory in
order — `phase1_proposal.md`, `photonics_construction.py`,
`phase1_results.json`, `_output.txt`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`phase4_results.json`, `NOTES.md`.

**Independent verification performed, not merely re-argued.** I re-ran the
load-bearing numbers directly from the committed `phase1_results.json`/
`phase4_results.json` (not from any prose summary) via a short scratch
script reading the JSON in place — the same numbers below are printed
verbatim from that check, not copied from `NOTES.md`.

No RULED-OUT item (R1–R9) is re-proposed below.

---

## 1. Is the construction actually what my own seat specified, built and
## scored correctly, end to end?

**Yes.** I traced `dist_direct_cells`/`e_direct_curve` in
`photonics_construction.py` against my own exp-080 Phase-5 formula
(`E_direct(θ_beam) = ∫ amp(y_s)·exp(i[phase_drive(y_s,θ_beam)+K·hypot(D_SP,
OBJ_Y−y_s)]) dy_s`) and it is a faithful, character-for-character
transcription — differing from the already-gated `dist_image_cells` only by
the sign on `y_s`, exactly as the direct/mirrored distinction requires. The
total field `E_total = E_direct + r(90°−θ_beam;ABSORB)·W(θ_beam)` is both
terms, genuinely present, scored by `_free_period_search`/
`free_period_with_widening` against REAL T28 reference periods
(`experiments/076-.../results.json::headline`) — not the R²-against-a-
candidate-curve methodology exp-080 mistakenly used. This is the first time
in nine T28 y-wall cycles (exp-069 through exp-080) my own construction has
been built and scored the way I specified it. The claim that this cycle
"finally builds it correctly" is true, not overclaimed.

## 2. Re-derivation: does `C80−C40`'s SUPPORT really survive `r()=1` almost
## unchanged?

I pulled the ablation table directly from `phase4_results.json`
(`item1c_ablation_control.per_pair`), independently, not from any narrative
summary:

| pair | `rel_dev` real `r()` | `rel_dev` ablated (`r()=1`) | shift | ablated degenerate? |
|---|---|---|---|---|
| `pair_pad` | 0.5973 | 0.5647 | 0.150° | No |
| `pair_absorb40` | 0.5139 | 0.7605 | 1.030° | **Yes (`ss_tot=0.0` exactly)** |
| `c80_c40` | **0.2910** | **0.2937** | **0.0075°** | No |

**Confirmed, independently: `C80−C40`'s lone SUPPORT (`rel_dev=0.2910`)
survives total ablation of the wall's reflectance to `r()=1` at
`rel_dev=0.2937` — a shift of 0.0075°, both readings comfortably inside the
0.30 SUPPORT bar.** Setting `r(90°−θ_beam)→1` deletes 100% of the wall's
own optical response from the model and the recovered period barely moves.
This is the correct, decisive interpretation: **the one nominal SUPPORT
this construction produces carries no evidence that the wall's reflectance
matters at all** — it is driven by `W(θ_beam)`'s own aperture-diffraction
envelope alone (already known, from exp-078/079, to itself sit near T21's
1.9608° fringe by construction), not by `ABSORB`-dependent optical
response. `PAIR_ABSORB40`, by contrast, genuinely needs `r()` to produce
any signal at all (ablated `ss_tot` is bit-exact `0.0` — total
degeneracy) — but that pair's own recovered period (`rel_dev=0.5139`) is
nowhere close to T28's real target either way. So: the one pair with
genuine wall-optical content fails to match; the one pair that "matches"
has no wall-optical content. That is not a coherent partial confirmation
of a real y-wall echo — it is the cleanest possible demonstration that
this construction family's apparent near-hit is a look-elsewhere artifact,
exactly as `phase2_redteam_audit.md` §1 Attack 2 and `phase3_synthesis.md`
§2 item 2 state. My own re-derivation from the raw JSON matches their
prose to the printed digit.

## 3. Re-derivation: the realizable-vs-matched admittance stability claim

Also pulled directly from `phase4_results.json`
(`item1_admittance_family_rescore`): period shifts
`{pair_pad: 0.007519°, pair_absorb40: 0.0°, c80_c40: 0.007519°}`,
`verdict_flips: False`, Combined Verdict `NEITHER` under **both** matched
and realizable (`μ_r=1`) admittance families. **Confirmed**: this is a
genuinely small, non-outcome-determining shift — three orders of magnitude
below the `rel_dev` bands' own 0.30/1.00 gates. The one literal miss
(`0.0075188°` vs. the frozen `"≤0.0075°"` bound, by `1.88×10⁻⁵°`) is
disclosed honestly in `phase4_results.md` and is a rounding-precision
artifact of how the bound was stated from a 4-decimal-rounded table, not a
physics discrepancy — I agree with that characterization; the substantive
claim (not outcome-determining) is what matters and it holds. The
phase-divergence explanation (8.4–10.6° at this cycle's `[48°,54°]` range
vs. 54.0–83.6° at exp-080 part(b)'s `[5°,15°]` range, both at ABSORB=40)
is a real, correctly-derived physical reason this cycle's result differs
from that precedent, not an unexplained coincidence — an order of
magnitude less admittance-family sensitivity precisely because item 1
operates in a much more grazing regime where the matched and realizable
boundary conditions happen to converge in phase.

## 4. Is there a coherent optical-response story here at all, across the
## swept angle range?

**Yes — and that is exactly what makes the negative result trustworthy
rather than merely inconclusive.** The pieces this cycle assembles are each
individually well-behaved across the swept `θ_beam∈[36°,42°]` (mapping to
`r()`'s own evaluated range `90°−θ_beam∈[48°,54°]`):

- `r(90°−θ_beam;ABSORB)` is a physically-grounded, exact recursive
  transfer-matrix reflectance (inherited from exp-075's own graded-loss
  boundary model), now formally gated at this exact angle range for the
  first time (item 2: G-LOSSLESS `2.22×10⁻¹⁶`, G-N1 `3.14×10⁻¹⁵`,
  G-PASSIVITY worst `|r|=0.0414` — all comfortably inside their bars,
  independently reproduced by me from `phase1_results.json`).
- `E_direct`, the direct source-to-observer term, is bit-exact
  config-invariant (item 1a: `0.0` deviation across all 5 configs, all 31
  angles) — a clean, closed-form consequence of the congruent series' own
  symmetric geometry, now the fourth independent confirmation of my own
  proof.
- The two terms combine coherently and cancel exactly (to float precision,
  `~10⁻¹⁴` against an `O(100)` carrier) in every pair-delta a real
  discriminating test needs — I checked `|E_direct|≈89–111` vs.
  `|E_image|≈1.3×10⁻⁴`–`3.5×10⁻³` directly in `phase1_results.json` and the
  four-to-five-order-of-magnitude gap is exactly what predicts a
  `10⁻¹⁴`-scale floating-point residual, not a bug.

Given all of that is verified and gate-clean, the angle-dependence story
this construction tells is internally consistent: `r()`'s magnitude and
phase vary smoothly and passively across the swept range, `W(θ_beam)`
contributes its own known aperture-diffraction structure, and the sum is
well-defined at every angle tested. **The construction is optically
coherent; it simply does not reproduce T28's real periodicity when
correctly built and honestly scored against real data** — a genuine,
well-supported negative result about this specific mechanism, not a
symptom of an incoherent or under-specified optical model. That
distinction matters for how Iteration 59 should read this cycle: this is
not "the test was too crude to tell," it is "the test was finally built
right, and it says no."

One residual gap I flag as still open, from my own charter's own angle+
wavelength duty specifically: the `r` vs. `conj(r)` sign-convention
question is shown **not outcome-determining this cycle** (zero verdict
flips under the substitution, independently confirmed by me against
`phase4_results.json::item2_conj_sensitivity`), but it remains genuinely
**empirically unresolved** at this new, more-grazing `[47.5°,54.5°]`
range — the only check that has ever settled this class of ambiguity
(`phase5_redteam_phase_convention_check.py`, exp-075's FDTD tie-breaker)
was calibrated at `0°/20°/39°` and has never been extended here. I concur
with `phase3_synthesis.md`'s disposition (queued, not resolved, correctly
labeled "reassuring not resolving") rather than treating it as closed.

## 5. Steel-man (what this cycle got right)

This is the strongest single cycle in this nine-cycle sub-thread on
process discipline: Phase 1 pre-registered a directional-but-honest
prediction ("NEITHER, leaning REFUTE") and then *disclosed* when its own
literal item-1b prediction (`0.0` bit-identical) technically failed rather
than rounding it to a pass. Five blind Phase-2 critiques converged,
independently, on the same three real gaps (admittance-family scope,
missing ablation control, phase-convention-untested gate), and Red Team's
audit did not merely re-argue them — it computed all three to completion
from primitives, producing the pair-specific ablation finding that is more
precise and more damaging to the lone SUPPORT than any single blind
critique's own binary framing anticipated. I independently re-derived the
two load-bearing numeric claims above from the raw JSON and both match to
the printed digit. This is R4/R8/R9 discipline working as designed, not
merely invoked.

## 6. Sharpest gap I would press on

The Combined Verdict mechanism (`NEITHER` unless all three pairs agree) is
this sub-thread's own longstanding convention, but it is worth naming
plainly for Iteration 59: **on the substantive, ablation-informed reading,
this cycle's result is functionally a REFUTE for the y-wall echo mechanism
as PHOTONICS specified it** — the one pair with real optical content
(`PAIR_ABSORB40`) misses badly, and the one pair that superficially matches
(`C80−C40`) is now *proven* to carry none. `phase3_synthesis.md`/
`NOTES.md` already say this in prose ("REFUTE-leaning... now on firmer
ground"), and I agree with that reading — but Iteration 59 should not
under-weight it relative to the mechanically-computed "NEITHER" label
just because the formal band structure never scores a REFUTE without all
three pairs agreeing. The evidence this cycle produced is stronger than
the label alone conveys.

---

## VERDICT: **PARTIAL**

This cycle is not "ruled out" — it does not close a mechanism class by
formal rule (Checkpoint criterion 2 correctly stays NOT YET RIPE: this is
one construction, one wavelength, one empty-scene geometry), and it is
certainly not "promising" — it produced no positive evidence for a real
T28 echo. It is a genuine, independently-verified narrowing: for the first
time in nine cycles, PHOTONICS' own coherent-echo construction was built
exactly as specified and scored against real data, and the honest,
ablation-sharpened reading is REFUTE-leaning, joining exp-078's and
exp-079's own structural forecloses as a third independent negative
finding against the plane-wave/global-steering y-wall echo class
specifically. Every load-bearing number I re-checked against the raw JSON
matches the write-up exactly. `T28`'s own ~2.84°-family periodicity origin
remains unexplained.

---

## Ranked top-3 candidate directions for Iteration 59

**#1 — The wavelength-generality leg (750nm/450nm), now SIX consecutive
cycles deferred (076–081).** This sits most squarely in my own charter
(angular dependence AND wavelength dependence, jointly). Every substantive
finding this cycle produced — the REFUTE-leaning reading, the admittance-
family stability, the phase-divergence explanation — has been established
at exactly one wavelength (600nm). This sub-thread has repeatedly found
that integer-λ boundary-thickness aliasing matters (T28's own C70 config
was added specifically to guard against a 600nm aliasing coincidence); a
finding this clean at 600nm deserves to be checked for whether it survives
a genuinely different λ before it is treated as settled evidence toward
closing the mechanism class. This is also the single most overdue item on
the whole board and cheap (reuses the already-built `photonics_
construction.py` unchanged, new θ_beam/λ inputs only, zero new FDTD if the
750nm leg's data is already collected as `block_leg750`, or a bounded new
FDTD spend if a fresh dense sweep is needed at 450nm).

**#2 — Extend `phase5_redteam_phase_convention_check.py`'s empirical FDTD
tie-breaker to 2–3 angles inside `[47.5°,54.5°]`.** This is the one
genuinely open verification gap this cycle's own record leaves
unresolved (queued explicitly in `phase3_synthesis.md` §2 item 3, not run,
Idealization 7). It is cheap (exp-075's own battery ran in ~90 seconds)
and directly closes the last piece of "is the optical response coherent
as stated" that remains unverified for this specific angle range — even
though this cycle's own `conj(r)` sensitivity check shows it is not
outcome-determining for the current result, a future construction at a
different angle range could reopen the ambiguity, and the check is cheap
enough that leaving it unresolved a second cycle running has no good
justification.

**#3 — The PAD-loaded real-article check, now SIX consecutive cycles
deferred (076–081).** Every result in this entire T28 sub-thread, this
cycle included, is on an empty scene. Given this cycle's own finding that
the y-wall echo construction — the most physically motivated mechanism
candidate this sub-thread has produced — is REFUTE-leaning, the next
highest-value question is whether the underlying `PAD`-sensitivity axis
that has dominated T28's history (exp-076's `PAD_TIED` finding) is even a
real-world-relevant signal once a physical absorbing object occupies the
aperture, or whether it is entirely an artifact of the empty-domain
boundary-condition geometry this whole sub-thread has probed. This is a
different instrument class from items #1/#2 (real FDTD, a genuinely new
scene) and is overdue enough that PLAN.md's own standing instruction (state
an explicit reason before deferring a seventh time) should bind.
