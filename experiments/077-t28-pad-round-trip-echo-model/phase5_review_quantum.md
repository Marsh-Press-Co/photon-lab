# PHASE 5 — REVIEW · QUANTUM OPTICS (blind) · Panel Iteration 54 · exp-077

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions; mechanisms enter the
bench only as effective classical parameters — σ(I), σ(x,t), dispersive
ε(ω), gain — or Red Team strikes them. Fresh context: I do not see any
other seat's Phase-5 review this cycle, including my own Phase-2 critique
from earlier in this cycle (re-read here only as a historical document to
verify against, not as a source of unexamined authority).*

---

## 1. Verdict: **PARTIAL** (concurring with the record) — on the *mechanism
question* T28 poses. On the narrower question this task actually assigns
me — does the committed null-calibration appendix hold up — my answer is
**qualified yes, with one real completeness gap and one real, previously
uncaught methodological soft spot**, detailed in §2.

The physics conclusion this cycle reaches — Combined REFUTE for `PAIR_PAD`
(T28's dominant, HIGH-tier signal) and, once the two-wall term is correctly
included, Combined REFUTE for `PAIR_ABSORB40` too — is not in dispute here.
It is independently confirmed four ways in the record (PHOTONICS' and
ELECTROMAGNETISM's Phase-2 from-scratch two-wall retargets, Red Team's
Phase-2 audit re-derivation, this cycle's own Phase-4 re-run, all agreeing
to 4 decimal places), and my own spot-checks below add a fifth and sixth
independent confirmation of the pieces that matter to my own charter. I
have no basis to overturn it.

---

## 2. Independent verification of the committed null-calibration appendix

I read `null_calibration_appendix`/`free_period_with_widening_quiet` in
`pad_round_trip_model.py` directly (lines 266–334), re-ran the actual
committed `_free_period_search`/`_fixed_period_fit` machinery myself
(imported, not reimplemented) at reduced scale, and read the primary output
(`pad_round_trip_results.json::null_calibration_appendix`) rather than
trusting `phase4_results.md`'s summary line.

### 2a. What the committed code actually does, verified against source

- **(a) Pure-noise null**: draws `n_trials` i.i.d. `N(0, σ)` curves, where
  `σ = std(real_delta_pad) = 1.4412e-3` (verified: `pad_round_trip_model.py`
  line 277), fits each with the real staged-widening search, and reports
  only `P(R²≥0.70)`, `max_r2_over_trials`, `mean_r2_over_trials`. **Committed
  result** (`pad_round_trip_results.json`, read directly):
  `p_r2_ge_070=0.0`, `max_r2_over_trials=0.5608835`, `n_trials=20000`. My own
  independent re-run at reduced scale (`n=2000`, same imported functions,
  fresh seed): `P(R²≥0.70)=0.0`, `max R²=0.5121` — same qualitative result,
  same order of magnitude on the ceiling. **This part is real and
  reproduces.**
- **(b) Bootstrap ground-truth recovery**: fits `real_delta_pad`'s own best
  sinusoid (`P*=4.6126°`, matches `phase1_proposal.md` to the digit),
  computes residuals against that fit, then resamples those residuals
  **i.i.d. with replacement** (`rng.choice(resid, size=n, replace=True)`,
  line 304) onto the fitted curve, 20,000 times, and refits each resample.
  Committed result: `frac_within_20pct_of_true=1.0000`,
  `recovered_std_p_star_deg=0.1409°`. I independently reconstructed the
  exact same residual array from the committed functions (bit-identical
  `P*`/`R²` to the record) as a precondition check before assessing the
  resampling step itself (§2c).

### 2b. A real, previously-uncaught completeness gap: half of my own
proposed pure-noise check was silently dropped

My own Phase-2 critique (`phase2_critique_quantum.md` §3(a)) computed
**three** quantities under a pure-noise null on this exact grid/window, not
one: `P(rel_dev>1.00)=0.214`, `P(R²≥0.70)=0/40,000`, and
`P(shape r²≤0.05)=0.778`. Red Team's own Phase-2 audit (Attack 5) reproduced
the same three-quantity table at reduced scale (`0.225`, `0/800`, and
implicitly the same qualitative point) and explicitly ruled: **"add
QUANTUM's null-calibration appendix (both checks, at their full 20,000-trial
scale...)."** `phase3_synthesis.md`'s own frozen prediction for fix 5 then
narrowed the expected content to a single sentence about R² alone ("both
curves' fitted R² values are far outside what 20,000 pure-noise trials
produce").

Reading the actual committed function, that narrowing became a real
omission, not just a prose simplification: `null_calibration_appendix`'s
`pure_noise_null` branch declares a variable `rel_dev_gt1 = 0` (line 280)
that is **never incremented and never included in `out_a`** — dead code,
direct in-source evidence that a rel-dev-under-null statistic was started
and then dropped before being wired up. Neither `pad_round_trip_results.json`
nor `pad_round_trip_output.txt` nor `phase4_results.md`/`NOTES.md` contains
`P(rel_dev>1.00)` or `P(shape r²≤0.05)` anywhere.

I reconstructed the dropped statistic myself, at reduced scale (`n=2000`,
two independent `N(0,1)` 31-point curves per trial, same imported
`free_period_with_widening_quiet`, same staged window):
`P(rel_dev>1.00)=0.151`, `P(shape r²≤0.05)=0.769`. These are in the same
qualitative range as my own original Phase-2 numbers (0.214/0.778) and Red
Team's spot-check (0.225) — **confirming the dropped statistic was real and
non-negligible, not a rounding artifact that vanished on correction.**

**Why this matters, precisely**: the point of the three-quantity table was
never "R² alone proves REFUTE" — it was the two-part argument that (1) the
bare threshold-crossing rules (`rel_dev>1.00`, `r²≤0.05`) are, on their own,
reachable by chance 15–23%/77–78% of the time respectively, so citing
REFUTE by threshold-crossing alone overstates the evidence, **but** (2) the
actual R² each real/model curve achieves at its own optimum is essentially
unreachable by chance, which is the fact that rescues the REFUTE from being
a look-elsewhere artifact. The committed appendix keeps only the rescuing
half. It does not change the verdict — the R² separation is real and I
reproduce it — but a future reader of the committed record alone, without
this critique's own text, would not know that the REFUTE thresholds
themselves are this soft in isolation, which is exactly the caveat R8's own
standard (Iteration 52) says must not be quietly dropped once a specific,
affordable, already-named check has been priced. **This is a real, if
non-load-bearing, fidelity gap between what Red Team's audit mandated and
what the committed function delivers** — recommend closing it same-shift
(wire up `rel_dev_gt1` or delete the dead variable and state explicitly
that this half of the original check was consciously narrowed, not
overlooked).

### 2c. A genuine, independently-found methodological soft spot in the
bootstrap: the i.i.d. residual-resampling assumption is not obviously safe
here, and was not checked

The task specifically asked me to check "whether the bootstrap's
residual-resampling procedure is sound." I computed the lag-1
autocorrelation of the actual residual array the committed bootstrap
resamples from (`real_delta_pad` minus its own best-fit sinusoid at
`Tc` derived from `P*=4.6126°`):

**`lag-1 autocorrelation = 0.6307`.**

This is not negligible. It is smaller than but the same *kind* of finding
as exp-074's own Phase-5 discovery (Iteration 51, LOGBOOK) that the
`{C40,C60,C70,C80}` series' residuals were "strongly θ-autocorrelated
(lag-1≈0.92–0.94) — a shared curvature misspecification, not
`ABSORB`-differential noise" — and it is exactly the shape of defect R6's
own addendum (Iteration 50, `G0-e(ii)`) was adopted to force a check for: an
i.i.d.-resampling or sign-flip null run on a design whose actual residuals
carry real serial structure is systematically anti-conservative (that
addendum's own confirmed case was 2–6× nominal on a comparably-sized
design). The committed bootstrap here resamples `resid` **with
`rng.choice(..., replace=True)`** — order-discarding, i.i.d. by
construction — on a residual array whose own lag-1 correlation is 0.63.
That is very likely to **understate** the true sampling variability of the
recovered period, which would make `frac_within_20pct_of_true=1.0000` look
more airtight than the same check would look under a resampling scheme
that preserves the residuals' own serial structure (a block bootstrap or a
circular-shift bootstrap, the same fix class the exp-073/exp-074 sub-thread
eventually adopted for its own null).

**This does not overturn the REFUTE verdict.** The gap this bootstrap
closes (§2a's rescuing R² argument) does not depend on the bootstrap at
all — it depends on the pure-noise null, which is a separate, unaffected
calculation. And the model-vs-real period mismatch (4.61° vs 8.67–13.28°,
a factor of 1.9–2.9×) is large enough relative to `recovered_std_p_star_deg
=0.14°` (real-data bootstrap) that even a several-fold underestimate of
that spread would not close the gap. But the specific claim
**"100.0% of resamples land within 20% of the true fitted period"** is a
tighter, more load-bearing-sounding number than the underlying resampling
scheme can currently support without a check for exactly the failure mode
this program has now found, named, and fixed twice before in adjacent
instruments (R6/R6-addendum). **Verdict on the appendix: the pure-noise
half (§2a) is sound and independently reproduces; the bootstrap half (§2c)
answers a real question correctly in direction but is calibrated by an
unverified i.i.d. assumption that this program's own house rules would
normally require checking before the "100%" figure is treated as a
precise number rather than "very close to 100%."**

### 2d. Everything else I checked reproduces cleanly

- Noise scaling (`σ=std(real_delta_pad)` vs. my own critique's implicit
  unit-variance framing): immaterial. `R²` for this least-squares sinusoid
  fit is scale-invariant under a positive rescaling of the data (the fit
  includes an offset and amplitude terms that absorb any constant scale
  factor identically in numerator and denominator of the variance-explained
  ratio) — the choice of `σ` changes nothing about the `P(R²≥0.70)`
  statistic's distribution. Not a defect.
- `Tc`/`x_sin` construction in the bootstrap (line 297–300) matches
  `_fixed_period_fit`'s own established `x=sinθ` convention, the same one
  this entire T28 sub-thread has used since exp-069 — no convention error
  found.
- The geometry-congruence assertions (`load_pair_geometries`), the
  `verify_symmetric_damping` check (worst diff `0.000e+00`, both edges
  bit-identical), and the thermo-sidecar reasoning (`r_for["C40"] is
  r_for["G40"]`, common-mode by object identity) all independently
  re-verify exactly as `phase4_results.md` states.

**Bottom line on the task's own question**: the Director's implementation
faithfully captures the load-bearing half of what I proposed (the R²
separation, which is genuinely the piece that rescues REFUTE from being a
look-elsewhere artifact) but silently narrows the disclosed half (the raw
threshold-crossing rates), leaving dead code as the tell, and it applies an
unexamined i.i.d. assumption in the bootstrap that this exact program has
twice before found to matter on residuals of comparable or even smaller
autocorrelation. Neither gap changes today's REFUTE verdict on independent
re-derivation. Both are cheap, same-shift fixes.

---

## 3. A new, independent quantum-optics-flavored angle on T28 — or an
honest "not applicable"

**Not applicable, stated plainly rather than manufactured.**

My charter's domain is non-classical absorption, state-dependent
interactions, and coherent effects that go beyond what a classical,
deterministic wave equation already predicts — expressible only as
effective classical parameters (σ(I), σ(x,t), dispersive ε(ω), gain) that
the bench can actually run. I looked specifically for whether any such
parameter class could still be in play for T28's unidentified ~2.8°-family
periodicity, now that exp-076 proved `PAD` is lossless vacuum and this
cycle REFUTEd the one mechanism class (single- and two-wall coherent
boundary echo) that proof left standing. I find none, for a structural
reason, not a lack of imagination:

**Both configs in every pair this cycle scores (`C40`, `G40`, `C80`) are
empty vacuum scenes with a classical, static, graded-loss numerical
boundary condition — there is no atom, molecule, two-level system, real
absorbing material, or time-varying element anywhere in the instrument.**
`σ(I)` requires an intensity-dependent medium; none exists here (the
`ABSORB` band's `r(theta;ABSORB)` is fixed per config, independent of field
amplitude — confirmed by inspection, `boundary_reflectance.py`'s
`n_profile_exact`/`reflection_coefficient` take no intensity argument).
`σ(x,t)` requires a time-switched medium; nothing in `lab/fdtd2d.py`'s
`_damping` construction depends on simulation time. Dispersive `ε(ω)` is
already the ENTIRE content of the mechanism just REFUTEd (`r(theta;ABSORB)`
IS a frequency/angle-dependent reflection coefficient) — there is no
further quantum-specific refinement to propose on top of a passive,
already-gated, already-tested transfer-matrix result; adding, say, a
Lorentz-oscillator resonance to `ε(ω)` would just be a different classical
dispersion model, already inside PHOTONICS'/ELECTROMAGNETISM's charter, not
a new quantum-optics contribution. Gain is inapplicable — nothing amplifies
here. Coherent interference is already the full content of the mechanism
just tested (the "coherent echo" model IS a classical coherent-superposition
calculation; classical Maxwell's equations already capture single- and
multi-path interference completely at these field strengths — coherence
alone is not the same thing as *non-classicality*, and conflating the two
would be exactly the kind of padded claim this program's culture polices).

The honest reading of exp-076 + this cycle, from my own seat: the
remaining candidate space for T28's periodicity is a **classical
numerical-instrument** question (Yee-grid dispersion/anisotropy in the
graded-loss cubic-ramp boundary construction itself, a PML-like
discretization artifact, or a genuine but still-unmodeled geometric
resonance) — squarely PHOTONICS/ELECTROMAGNETISM/MATERIALS territory (and
R3's own "grid-artifact" discipline), not mine. Manufacturing a
quantum-flavored mechanism here — e.g. invoking vacuum-fluctuation or
Casimir-type language for a static, classical FDTD boundary with no time
dependence and no real material at either wall — would be exactly the
kind of unfalsifiable, inexpressible speculation Red Team exists to strike,
and would fail my own charter's expressibility contract on arrival: there
is no effective classical parameter such an idea would even correspond to
tuning, since the instrument being probed is already 100% classical field
theory with no missing physical input of the kind quantum optics supplies.

I say this is "not applicable" rather than force a candidate, per the
task's own instruction and this program's stated preference for an honest
null over a padded one.

---

## 4. Ranked top candidate directions for Iteration 55 (my own top 3)

1. **Harden the null-calibration appendix itself before it is leaned on
   again** (zero new FDTD, same-shift-sized, directly on my own charter
   since I proposed the appendix): (a) wire up or explicitly delete the
   dead `rel_dev_gt1` statistic and report the full three-quantity
   pure-noise table (§2b) so a future reader does not have to reconstruct
   it from a Phase-2 critique to see the threshold-crossing caveat; (b)
   re-run the bootstrap ground-truth-recovery check with a block or
   circular-shift resampling scheme that preserves the residuals' own
   lag-1≈0.63 autocorrelation (§2c), alongside the existing i.i.d. version,
   and report both — matching the exact fix pattern (`G0-e(ii)`,
   Iteration 50) this program has already built and adopted once for a
   structurally similar problem. This closes the one open methodological
   question my own charter is positioned to raise, before anyone treats
   "100% within 20%" as a precise rather than approximate number.
2. **The standing, near-unanimous Iteration-53 queue item 6: the
   full-width non-aliased second-wavelength (`G40`) leg.** With the
   coherent-echo mechanism class now REFUTEd on both cuts (this cycle) and
   the `ABSORB`-boundary-reflectance class REFUTEd on a resolved phase
   convention (exp-075), this is now the cheapest remaining FDTD test of
   whether T28's periodicity is a real, wavelength-scaling-consistent
   physical effect at all, independent of any named mechanism candidate —
   the right next spend given that no named mechanism currently survives.
3. **Red Team's own flagged reckoning (`NOTES.md`'s "Next" section,
   this cycle): an explicit ruling on whether the mechanism-class board is
   now exhausted.** Two independently-tested mechanism classes
   (boundary-reflectance echo, single- and two-wall) are now REFUTEd for
   the two axes (`ABSORB`, `PAD`) that dominate T28's history. That is
   close to, if not already, the "honest alternative product" PANEL.md's
   own stop-condition language anticipates (a mapped constraint/mechanism
   boundary) rather than a mid-thread partial. I rank this third, not
   first, because it is a bookkeeping/governance question rather than a
   new falsifiable test — but it should not wait indefinitely while cheap
   FDTD (item 2) keeps being deferred in its favor, cycle after cycle, as
   it already has been since Iteration 53.
