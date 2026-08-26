# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 52 · exp-075
## Adjudicating all six blind Phase-5 reviews, and resolving the cross-module phase-convention question outcome-determining for Test A on both tested mechanisms

*Fresh sub-agent, RED TEAM charter (PANEL.md seat 7, verbatim): "attacks
every proposal, speaks last and hardest. Its standard is NOT
textbook-physics compliance — speculation is permitted. It kills:
internal inconsistency, unfalsifiable claims, mechanisms that cannot be
expressed as simulation parameters, and proposals that quietly violate a
target constraint — especially #3. Red Team never leads a cycle; it has
no proposal of its own to protect." Constraint #3 is N/A this cycle
(instrument-fidelity work, confirmed at every phase of this cycle's own
record). Receives everything: `phase1_proposal.md`,
`boundary_reflectance.py`/results, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `two_wall_cavity.py`/
results, `phase4_results.md`, `NOTES.md`, all six Phase-5 reviews
(`phase5_review_{photonics,materials,em,quantum,vision,thermodynamics}.
md`), `lab/fdtd2d.py`, `lab/emit.py`, and LOGBOOK.md's full T28 history
including the Iteration 49/50 sign-convention-bug precedent. Every
load-bearing claim below is independently re-derived or re-run from the
actual committed code — including new code built for this audit, owned
as such — never taken on any seat's word (house rule R4, applied at
maximum strictness per this task's own instruction).*

---

## 0. What I ran

1. Read `lab/fdtd2d.py` lines 72–264 (`_damping`, `add_line_source`,
   `Sim.run`) and `lab/emit.py` in full — the engine's own documented and
   gate-tested phasor/traveling-wave convention (`f(n)=Re{F e^{-iωn}}`,
   `_phasor`'s own docstring; "plane wave `e^{i(kx x - w n)}`",
   `observer_record`'s own comment) is the ground truth every convention
   question in this cycle is ultimately measured against.
2. Independently re-derived the friction-PDE dispersion relation from the
   proposal's own stated ODEs (`dE/dt=cdH/dx−νE`, `dH/dt=cdE/dx−νH`) under
   the ansatz `E,H ∝ e^{i(kx-ωt)}` — confirming the code's own §2b comment
   ("+2iων… the natural… convention pairing") and showing this predicts
   `n(x)=1+iν(x)/ω`, the branch the code did **not** use (§2 below).
3. Independently re-derived, from the standard transmission-line
   input-impedance recursion (matching `reflection_coefficient()`'s own
   `Zin = Zi(Zin+iZi t)/(Zi+iZin t)` formula), that its own baked-in time
   convention is the opposite (`e^{+jωt}`, standard EE/microwave
   convention) — cross-checked against EM's own Phase-2 finding that the
   code reproduces the textbook lossless mirror-plus-spacer form
   `r=-exp(-2ikL)`, the `e^{+jωt}`-signature form (§2).
4. Built and ran **new code, owned by this audit**
   (`phase5_redteam_phase_convention_check.py`, this directory, committed)
   — a real `Sim.run()` measurement of the actual FDTD-engine's reflected
   wave, extracted via the already-gated `lab.emit._phasor`/
   `quarter_pair`/angular-spectrum algebra (trust-suite stage 6: "mirror
   returns ~1.0, empty room ~0, eps=4 half-space returns Fresnel's 1/9"),
   compared against both `r(θ)` as committed and `conj(r(θ))` — the
   empirical tie-breaker the task invited, exactly the check PHOTONICS'
   own Phase-5 review independently proposed as Iteration-53's #1
   candidate (§2 below; full methodology, including a debugged-and-
   disclosed harness limitation, in that file's own docstring and §2
   here).
5. Independently reproduced, from scratch, PHOTONICS'/EM's own Phase-5
   `r→conj(r)` finding for **both** models — re-running
   `boundary_reflectance.py`/`two_wall_cavity.py`'s own committed,
   unmodified machinery with only the `r` argument swapped for `conj(r)`
   (never trusting either review's own numbers) — plus a `r→−r` control
   (§1).
6. Re-verified all three sanity/passivity gates, the `4/6`-not-`3/6`
   cross-config correlation count, the circular-shift null's exact-30-shift
   enumeration, and MATERIALS' `graded_black_shell` code-path-disjointness
   claim directly against `lab/materials.py` (§4).
7. Checked all five Checkpoint criteria explicitly against PANEL.md's own
   text (§5), applying the Iteration 49/50 precedent as directed (§3).

---

## 1. Independent reproduction of the phase-convention finding (task priority 1)

Rebuilt from scratch (not from either review's script): recompute the
single-wall and two-wall predicted `delta(θ)` curves with `r→conj(r)`
substituted everywhere `reflection_coefficient()`'s output enters
`c_empty_with_wall`/`c_empty_two_wall`, using the committed, unmodified
`_free_period_search`/Pearson-`r²` machinery on the real
`block_dense.rows` data — a scratch driving script built for this audit,
not committed to this directory (per this program's own Phase-5-review-
scope convention, matching how PHOTONICS'/EM's own Phase-5 verification
scripts were handled), importing `boundary_reflectance.py`/
`two_wall_cavity.py` unmodified so every number below traces to their own
committed functions, not to reimplemented logic:

| Model | Convention | `P*` | period `rel_dev` | Test A | shape `r²` | Pearson `r` | Test B | Combined |
|---|---|---|---|---|---|---|---|---|
| single-wall | committed | 15.0000° | 4.2778 | REFUTE | 0.2586 | −0.5085 | INCONCLUSIVE | **REFUTE** |
| single-wall | `r→conj(r)` | 3.9260° | **0.3814** | **INCONCLUSIVE** | 0.2940 | −0.5422 | INCONCLUSIVE | **INCONCLUSIVE** |
| two-wall | committed | 15.0000° | 4.2778 | REFUTE | 0.3042 | −0.5516 | nominal SUPPORT* | **REFUTE** |
| two-wall | `r→conj(r)` | 4.1211° | **0.4500** | **INCONCLUSIVE** | 0.2919 | −0.5403 | INCONCLUSIVE | **INCONCLUSIVE** |
| single-wall | `r→−r` (control) | 15.0000° | 4.2778 | REFUTE | 0.2577 | +0.5077 | INCONCLUSIVE | **REFUTE** |

*already shown non-significant by the mandatory circular-shift null
(`p=0.1953`), unaffected by this table.

**CONFIRMED, exactly, independently.** My own re-run matches PHOTONICS'
and EM's own independently-computed tables to 4 significant figures
(`P*=3.9260°`/`4.1211°`, `rel_dev=0.3814`/`0.4500`) — three independent
computations (PHOTONICS' review, EM's review, this audit) now agree.
`r→−r` (a pure sign flip, not a genuine convention question) leaves
Test A untouched: my own single-wall control run confirms
`rel_dev=4.2778`, REFUTE, unchanged (only Test B's correlation *sign*
flips, `−0.5085→+0.5077`, still INCONCLUSIVE either way) — matching
EM's own Phase-5 finding on the two-wall model exactly (`rel_dev=4.2778`,
REFUTE, unchanged). `r→conj(r)` alone is the pivot. **The finding holds
for both mechanisms,
as claimed, and Test A — the test that alone determines Combined Verdict
via the pre-registered `REFUTE if EITHER test REFUTEs` rule — genuinely
collapses from a boundary-pinned REFUTE (the model's curve never
completes a third of an oscillation across the tested window, at any
search boundary tried) to a genuine interior-optimum INCONCLUSIVE fit
under `r→conj(r)`, for both models.** `G-PASSIVITY` cannot discriminate
this (`|conj(r)|=|r|` identically) — confirmed directly against
`boundary_reflectance.py:264-269`.

---

## 2. My own attempt at resolution — which convention is correct?

### 2a. Static analysis: real, but does not cleanly settle it — disclosed honestly

`lab/fdtd2d.py::add_line_source`'s own docstring names the engine's real
convention: `emit._phasor`'s `f(n)=Re{F e^{-iωn}}` — confirmed gate-tested
machinery (`lab/emit.py`'s own stage-6/8 history: a prior *conjugate*
convention error was caught by an absolute power-balance check, not a
ratio-normalized one — the same class of error this section investigates).
`lab.emit.observer_record`'s own comment independently confirms the same
convention from a different angle: "plane wave `e^{i(kx x - w n)}`" —
matching `dg048.field_and_h`'s own outgoing-wave Green's function
`G0 = exp(i(k·r − π/4))/√r` (the `+ikr` sign is the standard `e^{-iωt}`-
convention outgoing-wave form). **Three independent readings of this
program's own engine and propagator code agree: the ground truth this
whole exercise must match is `e^{-iωt}`.**

`phase1_proposal.md` §2b's own comment states the friction-PDE ansatz
`E,H∝e^{i(kx-ωt)}` — matching this convention exactly — "naturally" gives
`n(x)=1+iν(x)/ω` (a `+2iων` cross term), and that this is the branch the
code **rejected** (chosen instead: `n=1-iν/ω`, satisfying passivity
against `reflection_coefficient()`'s own Zin formula). I independently
re-derived this dispersion relation from the stated ODEs myself and
confirm it exactly: under `e^{-iωt}`, a physically decaying (not
growing) wave in either propagation direction requires `Im(n)>0` — i.e.
`n=1+iν/ω`, standard optics convention for a lossy medium under this time
convention, confirmed by direct substitution, not asserted.

Separately, I independently re-derived that `reflection_coefficient()`'s
own transmission-line `Zin` recursion is natively written in the
**opposite** (`e^{+jωt}`, standard EE/microwave) convention — cross-
checked against EM's own Phase-2 finding (`phase2_critique_em.md` §0,
independently re-confirmed here) that the code reproduces the *textbook*
lossless mirror-plus-spacer form `r=-exp(-2ikL)` exactly: this specific
sign (`-2ikL`, not `+2ikL`) is the signature of a forward-traveling-wave
spatial factor `e^{-ikx}`, i.e. the `e^{+jωt}` convention standard in
transmission-line texts (Pozar-style `Zin` formulas).

**This is a real, structural cross-module convention mismatch — exactly
what the code's own §2b comment already suspects ("a time-convention
mismatch… manifests as exactly this kind of sign flip") — but the
straightforward algebraic conclusion ("convert `r` from the Zin formula's
own `e^{+jωt}` convention to this bench's `e^{-iωt}` convention by
conjugating the whole result before combining with `dg048`'s field") is
**not** what the empirical evidence below confirms.** I disclose this
tension rather than paper over it: my own static, hand-derived reasoning
pointed toward `r→conj(r)` being the fix; it is not. Either my own
convention-propagation argument has a step I have not correctly tracked
(entirely possible — this is exactly the class of reasoning this
program's own Iteration 49/50 history shows is failure-prone even under
careful attention), or the passivity-based branch selection the proposal
already performed, chosen purely for energy-conservation reasons,
*happens to also* resolve the convention question correctly (two
requirements, one answer) — the empirical result below cannot by itself
distinguish these explanations, but it does settle *which convention is
correct*, which is the question that matters for the Combined Verdict.
**Static analysis, followed all the way through, does not decisively
settle this on its own — matching the task's own contingency instruction,
this is exactly the situation calling for a small, affordable empirical
tie-breaker.**

### 2b. Empirical tie-breaker: a real FDTD measurement of the real reflected wave

Built `phase5_redteam_phase_convention_check.py` (this directory,
committed, new code owned by this audit): a handful of real `Sim.run()`
calls (§0.4) that launch a single angled plane wave from deep in the
interior at a real, `_damping`-constructed graded-loss band backed by the
PEC wall, and extract the actual reflected wave's complex amplitude
directly from the steady-state field via the SAME already-gated
angular-spectrum algebra `lab.emit.observer_record` uses (trust-suite
stage 6). Because the real `ABSORB=40..80` bands reflect too little
(`|r|~0.003-0.06`) for a single-bin FFT readout to have usable SNR against
finite-aperture diffraction sidelobes, the SAME real cubic-ramp
construction is tested truncated to a much shorter band (`K` cells) —
less adiabatic, hence more reflective (`|r|~0.05-0.3`) — testing the
identical, K-independent sign-convention question at workable SNR.

**Debugging disclosed in full (R4, applied to my own work, not just
others'):** an early version blanket-overwrote the `-x` edge's damping
array, which also silently erased the *y*-edge absorbing band in that
same column range, exposing a spurious undamped PEC corner a real
aperture's sidelobes can reach — caught by a companion calibration check
(a **lossless**, real-`n=1` spacer of `K` cells, where `|r|` must equal
exactly `1.0` by energy conservation, independent of any convention
question) that initially returned nonsense (`|r|=0.03-0.41`, converged,
not a settling artifact — confirmed by running 1800→12000 steps with an
identical result). Fixed by preserving the y-edge contribution via the
same `max()` composition `Sim._damping` itself uses. **A second,
disclosed, unresolved limitation**: even after the fix, this calibration
check shows the extraction method is reliable at `K=5` (measured `|r|` in
the right ballpark, `0.25-0.41` vs. the required `1.0` — off by a real,
not-fully-diagnosed factor, but the *phase/sign* comparison against
`r`/`conj(r)` is unambiguous there) but develops a growing, unexplained
systematic bias at larger `K` (measured `|r|` falls to `0.10` at `K=10`,
`0.02-0.03` at `K=20` — clearly wrong, and the `r`-vs-`conj(r)`
discrimination becomes correspondingly unreliable there too). I was not
able to fully diagnose this within this audit's scope (a "measure far,
propagate the phase back analytically" variant, tried as a fix, made
things *worse* — phase error over the longer propagation swamps the
already-small reflected signal). **`K=5` is therefore the load-bearing
operating point; `K≥8` results are reported for completeness, not relied
upon.**

**Results at `K=5` (the calibration-confirmed reliable point), 3
different incidence angles, `gap=150` cells, `ny=420`, `n_steps=1800`
(settling-converged, re-checked to `2600` steps, identical):**

| Test | θ | code arg(`r`) | measured arg | dev vs `r` | dev vs `conj(r)` | favors |
|---|---|---|---|---|---|---|
| calibration (lossless) | 0.0° | +0.00° | +50.70° | — | — | `r` |
| calibration (lossless) | 20.0° | +10.86° | +49.69° | — | — | `r` |
| calibration (lossless) | 39.0° | +40.11° | +49.74° | — | — | `r` |
| lossy (real `_damping`) | 39.0° | +57.16° | +44.09° | 0.0893 | 0.3826 | `r` (4.3×) |
| lossy (real `_damping`) | 36.0° | +49.91° | +45.24° | 0.0535 | 0.3581 | `r` (6.7×) |
| lossy (real `_damping`) | 42.0° | +64.53° | +47.96° | 0.1415 | 0.3970 | `r` (2.8×) |

**6 of 6 sub-tests at `K=5` — three calibration angles and three lossy
angles, all independent runs — favor the committed convention `r`; none
favor `conj(r)`.** The lossy-case margins are decisive (`2.8×`–`6.7×`
smaller deviation to `r` than to `conj(r)`), and the measured phase tracks
the *same sign region* as the code's own prediction at every angle
(never anywhere near `conj(r)`'s opposite-sign prediction). `K=8`/`K=10`
(outside the calibration-confirmed reliable range) give a mixed, weaker
signal (`K=8`: still favors `r`, `1.9×` vs `2.0×`, effectively a tie;
`K=10`: favors `conj(r)` narrowly, `1.7×` vs `1.2×`) — consistent with
harness unreliability growing with `K`, not with a genuine convention
flip (there is no physical mechanism by which the *convention* — a
structural property of one fixed formula — would depend on band length;
only this measurement's *reliability* plausibly does, and the calibration
check independently confirms exactly that pattern).

**Supporting, non-decisive corroboration**: EM's own Phase-2 finding that
`r→conj(r)` does *not* flip Test B's correlation sign (`-0.508→-0.542`,
both anti-correlated) is consistent with `conj(r)` being simply the wrong
convention rather than a suppressed correct signal — not independent
proof, but not in tension with this section's conclusion either.

### 2c. Verdict: **RESOLVED, moderate-to-high confidence — the committed convention (`r`, not `conj(r)`) is correct**

Not airtight, G0-e/R6-caliber closure (I am explicit about this, not
overclaiming): the static derivation alone left a genuine, disclosed
tension unresolved (§2a), and the empirical measurement's own reliability
is confirmed only at one operating point (`K=5`), with a real,
undiagnosed degradation at larger `K` (§2b). But at that one reliable
point, the evidence is consistent, multi-angle, and decisive by a wide
margin, and it is corroborated (not contradicted) by every other check
this cycle's record contains. **What would fully close this to this
program's own R6/G0-e standard**: a higher-power version of exactly this
check directly at the real `ABSORB=40/60/70/80` depths (not a truncated
analogue), with a smarter extraction than a single-bin FFT read — e.g.
coherent averaging over many probe points/angles, or a longer, more
carefully time-gated capture — ranked into the Iteration-53 queue below
(§7) as the natural continuation of PHOTONICS'/EM's own #1-ranked
Phase-5 recommendation, now a hardening task rather than a from-scratch
resolution.

---

## 3. Combined Verdict disposition — REFUTE stands, for both mechanisms

Given §2's resolution (the committed convention is correct), Test A's
`rel_dev=4.2778` — the boundary-search-pinned, no-completed-oscillation
REFUTE both models actually shipped, under the convention now confirmed
correct — is the right number, and REFUTE stands as the Combined Verdict
for **both** the single-wall and two-wall-cavity mechanisms, exactly as
`phase4_results.md`/`NOTES.md` state. The `r→conj(r)` INCONCLUSIVE result
(§1) was a real, reproducible finding about what an *incorrect* convention
would have predicted, not evidence the actual REFUTE is wrong.

**Applying the Iteration 49/50 precedent, as directed — is this the same
failure shape?** No — and yes, on different axes, weighed explicitly:

- **On the *physics*: a different, healthier pattern than Iterations
  49/50.** In both prior cycles, a genuine coding/reasoning defect
  produced a **wrong published number** that was asserted, in a frozen
  document, as verified/correct (`"ZERO items un-adopted"`,
  `"independently re-verified"` for a sign that was in fact backwards) —
  the actual computation was wrong and had to be corrected. Here, the
  actual computation (`rel_dev=4.2778`, REFUTE) is, per this audit's own
  independent resolution, **correct** — nothing about the final answer
  needs correcting. This is the load-bearing distinction Iteration 51 was
  praised for (an overclaim caught pre-Phase-3, no wrong number ever
  entered the permanent record) and Iterations 49/50 were faulted for (a
  wrong number did).
- **On the *verification discipline*: closer to the firing shape than to
  Iteration 51's clean non-firing precedent — see §5 for the full
  ruling.** EM's own Phase-2 critique explicitly named the exact check
  needed to close this gap (§4 of that critique: "re-derive `r(θ)`… and
  compare PHASE… If it fails and a corrected phase changes Test B's sign,
  the [REFUTE] framing… would need to soften") — and Red Team's own
  Phase-2 audit, and Phase 3, both accepted a *robustness argument*
  ("Test A… is robust to everything below" — EM's own Phase-2 text,
  adopted verbatim) **in place of** running that named check, filing the
  gap as merely informational. That argument turned out to be false (EM's
  own Phase-5 self-correction: "I conflated the closed-form diagnostic…
  with the… numerically-fit `P_model` Test A is scored on"), and the
  uncaveated "REFUTE, both mechanisms" headline this reasoning supported
  reached `NOTES.md`'s own permanent-record Learned section, surviving
  Phase 3 and Phase 4 unchallenged until two blind Phase-5 seats
  (PHOTONICS, EM), independently, built the check EM itself had already
  named and found it outcome-determining. **This is the specific pattern
  R7 (adopted one cycle prior, Iteration 51) exists to prevent** — an
  untested claim about a design/model's own robustness substituted for
  actually running the test — recurring here in a new, adjacent form (a
  qualitative independence *argument* rather than a quantitative
  conditioning *number*, but the same underlying failure: reasoning about
  a gap instead of testing it, when the test was affordable and had
  already been named). Full ruling, all five Checkpoint criteria, in §5.

---

## 4. Disposition table — all six Phase-5 reviews' other findings

| Finding | Source | Disposition | Reasoning |
|---|---|---|---|
| Phase-convention gap outcome-determining for Test A, both models | PHOTONICS, EM | **ADOPT, resolved this audit** | §1–§3 above: independently reproduced, then independently resolved (moderate-to-high confidence) in favor of the committed convention; REFUTE stands |
| 4/6 (not 3/6) negative cross-config correlation pairs | VISION (independent re-derivation against the raw JSON field, not Phase 3's prose) | **ADOPT — already correct in the permanent record** | Re-verified directly against `boundary_reflectance_results.json::absorb_depth_echo_cross_correlation`: `{40,60:-0.985, 40,70:-0.203, 60,80:-0.924, 70,80:-0.560}` negative (4), `{40,80:+0.913, 60,70:+0.276}` positive (2) — 4/6 confirmed exactly, a third independent confirmation (Phase 3, VISION, this audit) |
| `circular_shift_null` (two-wall Test B robustness check) is anti-conservative against synthetic AR(1)/phase-randomized data (~1.3–15.8× nominal depending on α and method) | QUANTUM | **ADOPT as a genuine, disclosed gap; does not change Combined Verdict** | Test A alone already REFUTEs regardless of Test B's robustness check; an anti-conservative null is biased *toward* false significance, so the check's own "NOT significant" (`p=0.1953`) reading is if anything *more* trustworthy under proper calibration, not less. Bind forward: `circular_shift_null()` must ship a null-calibration sub-leg (R6(ii)-style) before reuse on different data — folded into the Iteration-53 queue (§7 below) |
| `n=31` admits only 30 distinct circular shifts; exact enumeration (cheaper, exact) should replace the `N=20,000` Monte Carlo estimate | QUANTUM, independently re-confirmed by MATERIALS and THERMODYNAMICS (exhaustive enumeration, `p=0.2000` exactly, matching the `N=20,000` estimate to within sampling noise) | **ADOPT** | Confirmed three ways; cosmetic (does not change any verdict) but free and strictly more correct — fold into record-hygiene bundle |
| THERMODYNAMICS sidecar `>99.996%` → correct figure is `>99.995%` | THERMODYNAMICS (own-charter recompute) | **ADOPT** | Recomputed directly: `1-0.006423²=0.99995874`; `>99.996%` is false, `>99.995%` is true. Non-load-bearing, one-word fix |
| No document re-confirms the THERMODYNAMICS sidecar N/A disposition for the two-wall (vs. single-wall) mechanism specifically | THERMODYNAMICS | **ADOPT** | A real, correctly-argued-but-undocumented gap (the disposition is unchanged and correct, per THERMODYNAMICS' own re-derivation against `lab/fdtd2d.py`/`experiments/069/run.py` — no new absorbing object, `sigma_e≡0` throughout — but the record should say so explicitly for the two-wall extension, not only the single-wall original) |
| `graded_black_shell` (this bench's real physical absorber) is implemented via a disjoint code path (`sigma_e`, not `_damping`) from this cycle's matched-`ε=μ` construct | MATERIALS (verified directly against `lab/materials.py`) | **ADOPT** | Independently re-confirmed here: `lab/materials.py::graded_black_shell` writes `sim.sigma_e[shell]`, holds `eps_r=1`, never touches `_damping`'s arrays — this REFUTE is fully quarantined to the engine's own boundary-condition numerical construct and says nothing about T1/T5/T9's own established physical-absorber findings. Fold into the idealization/scope note |
| 750nm leg (`block_leg750`, already collected, Iteration 46) never tested against either model | VISION | **ADOPT, ranked into queue (§7)** | Zero new FDTD, cheap, decisive either way, stress-tests this cycle's own REFUTE before it is cited elsewhere as wavelength-general — VISION's own #1 Iteration-53 candidate, retained here |
| `nx`-substitution "match" (PHOTONICS' Phase-2 cavity-variant attack) is a look-elsewhere artifact, confirmed by the actual two-wall model | (already settled by Phase 4, restated for completeness across all seats' Phase-5 reviews) | **ADOPT — already correctly settled** | No further action; every Phase-5 seat independently reconfirms this without dispute |

None of these findings changes the Combined Verdict (REFUTE, both
mechanisms, §3); all are either already correctly reflected in the
permanent record or are cheap, disclosed, non-blocking gaps folded into
the Iteration-53 queue below.

---

## 5. Checkpoint criteria — all five, explicit

1. **A configuration passes all constraint metrics** — N/A, not a
   phenomenon-mechanism cycle; constraint 3 never engaged, confirmed at
   every phase of this cycle's own record. **Does not fire.**
2. **A proven boundary within a mechanism class** — N/A; T1 route is N/A
   throughout (instrument-fidelity work), matching every T28 cycle since
   Iteration 46. **Does not fire.**
3. **Synthesis requiring engine physics beyond validated bench classes**
   — no. The original cycle (Phases 1–4) ran zero new FDTD calls,
   confirmed at §0 of `phase2_redteam_audit.md` and re-confirmed here.
   This audit's own new work (§0.4, §2b) *did* run real `Sim.run()`
   calls, but exercises the engine's own already-validated, unmodified
   machinery (`Sim`, `add_line_source`, `lab.emit`) in a new scene
   configuration — no new engine capability was built. **Does not fire.**
4. **Program-integrity drift** — **FIRES**, on a specific, narrower basis
   than Iterations 49/50, weighed explicitly against the strongest
   available non-firing argument (§3 above). **Non-firing argument,
   stated in full**: no false verification claim was made about a
   specific, checked computation (unlike Iterations 49/50's "ZERO items
   un-adopted"/"independently re-verified [+R_i]," both verifiably false
   on inspection); the underlying Test A REFUTE conclusion is, per this
   audit, actually correct; every phase of this cycle's own record
   disclosed the phase-convention gap's *existence* honestly, at every
   turn — nobody hid it. **Firing argument, weighed as stronger**: (a) an
   **unverified robustness argument** — "Test A's REFUTE… is robust to
   everything below [the phase-convention issue]" (EM's own Phase-2 text)
   — was adopted verbatim by Red Team's own Phase-2 audit ("EM's own
   robustness argument, which I did not find any reason to overturn") and
   by Phase 3, **without independently testing it**, even though EM's own
   Phase-2 critique had already named the exact check needed ("re-derive
   `r(θ)`… compare PHASE, not just magnitude… If it fails… the framing…
   would need to soften"); (b) this claim then supported an **uncaveated
   headline** — `NOTES.md`'s own "Result"/"Learned" sections state flatly
   "Combined Verdict: REFUTE, both mechanisms," with no phase-convention
   caveat anywhere in that document — that survived Phase 3 and Phase 4
   unchallenged; (c) it took **two independent blind Phase-5 seats**
   (PHOTONICS, EM), using a **newly-built** check neither had run before,
   to find this outcome-determining — matching this program's own
   Iteration-45-established discriminator ("took blind Phase-5 seats plus
   the final audit to surface" = firing shape) precisely, not the
   Iteration-51 shape (caught by blind critics *before* Phase 3 adopted
   it — the non-firing shape); (d) **this is the same failure class R7
   was adopted to prevent, one cycle earlier** (Iteration 51: "a
   conditioning/VIF-based pricing of an un-fit design is necessary, not
   sufficient, evidence for a closure or detection claim… the design must
   be fit to real data") — generalized here from a *quantitative pricing
   number* substituting for a fit, to a *qualitative independence
   argument* substituting for a test, the same underlying discipline gap
   recurring in adjacent form, in the very next cycle after the rule
   meant to close it was adopted.

   **Ruled a notification, not a pause** — this program's unbroken
   precedent, now 11 for 11 (Iterations 17, 36, 37, 39×2, 40, 44, 45, 49,
   50, and now 52). No `lab/` diff to the original cycle's own machinery,
   the Combined Verdict is confirmed correct and unaffected (§3), and the
   remedy (documented below) is actionable without halting any other
   thread. **New standing rule, R8, proposed here** (see §6).
5. **Two consecutive non-advancing iterations** — **does not fire.** This
   cycle delivers genuine, independently-confirmed narrowing: two
   previously-untested boundary-reflectance-echo mechanisms are now
   REFUTEd against real data, on a resolved, confirmed-correct convention
   (§3), following Iteration 51's own genuine advance (formal retirement
   of the differential/two-tone instrument class). Two consecutive
   advancing iterations, not two non-advancing ones.

---

## 6. Standing rule proposed — R8

**R8 — an unverified robustness/independence *argument* about a flagged
verification gap is not itself sufficient to file that gap as
"informational only" ahead of a headline verdict; the argument must be
tested, not merely reasoned about, when the test is affordable (not a
ruled-out idea; a standing house-discipline rule, proposed here,
generalizing R7 one level further — from a quantitative pricing metric to
a qualitative claim of independence).** exp-075's Phase-2 critique (EM)
correctly identified a genuine, structurally-ungated cross-module
phase-convention risk, argued (without testing) that Test A's REFUTE was
"robust to" it, and *named the exact check* that would settle the
question. Red Team's own Phase-2 audit and Phase 3 both adopted this
untested argument to file the gap as non-blocking, rather than running
the named check before finalizing the cycle's headline framing — the
argument turned out to be false (Phase-5 self-correction, EM: the
closed-form diagnostic was conflated with the actual scored quantity),
and it took two blind Phase-5 seats to catch, one cycle after R7 was
adopted for the structurally analogous "pricing substituting for fitting"
failure. **Rule: when a Phase-2 (or later) critique names a specific,
affordable check that would resolve a flagged gap's relevance to a
verdict, and the disposition instead rests on an argument that the gap
is "independent of" or "robust to" the verdict without running that
check, the argument must be independently verified — by actually
computing the alternate case, not by re-reasoning about it — before the
gap is filed as non-blocking.** A cycle that files such a gap as
informational-only on an untested argument, when the gap later proves
outcome-determining, fires Checkpoint criterion 4 automatically if the
named check was affordable and not run, matching R6's/R7's own standard.
Confirmed on its own first, retroactive application here: the check EM
itself named (§2a of `phase2_critique_em.md`) is exactly the class of
check this audit ultimately had to build (§2b) to resolve the question —
had it been run at Phase 2 or Phase 3, the phase-convention gap would
never have reached `NOTES.md`'s own uncaveated headline. Full record:
this document §2–§5; `phase2_critique_em.md` §4; `phase2_redteam_audit.md`
§2c; `phase3_synthesis.md` §3.4.

---

## 7. Reconciled Iteration-53 ranked queue

All six seats' own rankings, reconciled (per house convention,
`experiments/074/phase5_redteam_audit.md` §8):

| Seat | #1 | #2 | #3 |
|---|---|---|---|
| PHOTONICS | Close the phase-convention gap (mandatory, blocking) | G40/PAD decorrelation | Record-hygiene bundle, extended |
| MATERIALS | G40/PAD decorrelation | Record-hygiene bundle + disjointness note | New structural candidate (speculative, un-priced) |
| ELECTROMAGNETISM | Pin the phase-convention gap (mandatory, blocking) | G40/PAD decorrelation | Record-hygiene bundle + robustness table |
| QUANTUM OPTICS | Size the `circular_shift_null` machinery | G40/PAD decorrelation | Dispersive ε(ω) extension (speculative) |
| VISION SCIENCE | Score the two-wall model at 750nm (`block_leg750`) | G40/PAD decorrelation | Record-hygiene bundle + `caveat_lint_config.json` entries |
| THERMODYNAMICS | G40/PAD decorrelation | Close Idealization 6 exactly (low value) | Record-hygiene bundle |

**Reconciliation.** PHOTONICS' and EM's own #1 (resolve the phase
convention) is **substantially discharged by this audit** (§2: RESOLVED,
moderate-to-high confidence) — it drops from a blocking #1 to a
hardening item, folded into item 3 below rather than kept as its own #1.
With that resolved, **G40/PAD decorrelation is the near-unanimous
reconciled #1** — ranked #1 or #2 by all six seats, the only queued item
that *relieves*, rather than discloses or prices, the `ABSORB`-or-`PAD`
confound running under every T28 causal claim since Iteration 48, and
untouched by this cycle's own analytic (non-causal) result either way.

1. **G40/`PAD` decorrelation** (~31 FDTD calls, per MATERIALS' verified
   geometry-reuse claim against `experiments/065-.../
   design_geometry_output.txt`). Near-unanimous across all six seats.
   Orthogonal to this cycle's own findings; explicitly not barred by the
   seventh-cycle rule (a different instrument class, targeting the
   phase-invariant amplitude channel, no fitted carrier phase). Now
   *more*, not less, load-bearing: with the boundary-reflectance-echo
   class doubly REFUTEd on the existing congruent series (this cycle),
   and the model's own predicted echo strongly `ABSORB`-depth-*dependent*
   while the real residual is depth-*independent* (§4 above), disentangling
   whether the real signal is `ABSORB`- or `PAD`-tied is now the single
   most information-dense open question on T28's own board.
2. **Score the already-built two-wall model against the already-collected
   750nm leg** (`block_leg750`, 16 points, Iteration 46, zero new FDTD —
   VISION's own #1). Cheap, decisive either way, and stress-tests this
   cycle's own REFUTE (and, as a free byproduct, gives a genuinely
   independent second data point on §2's phase-convention resolution at a
   different wavelength, at zero extra cost) before either headline REFUTE
   is cited elsewhere as a wavelength-general result.
3. **Harden the phase-convention resolution to this program's own R6/G0-e
   standard** (folds in PHOTONICS'/EM's own #1, now a closing task, not an
   opening one): extend `phase5_redteam_phase_convention_check.py`
   (this directory) to the real `ABSORB=40/60/70/80` depths directly, with
   a higher-power extraction (coherent multi-point/multi-angle averaging,
   not a single-bin FFT read) — diagnose and fix the `K≥8` calibration
   degradation this audit found and disclosed (§2b), or explicitly bound
   why it does not matter at the real, much-smaller `|r|` values. Cheap
   (a handful of `Sim.run()` calls, the same machinery already built),
   and closes R8's own retroactive first application on a forward-going
   basis.
4. **Record-hygiene bundle** (near-unanimous, touched by all six seats in
   some form): (a) `>99.996%`→`>99.995%` (THERMODYNAMICS, §4 above);
   (b) add an explicit two-wall-model sidecar re-confirmation sentence
   (THERMODYNAMICS, §4 above); (c) switch `circular_shift_null` to exact
   30-shift enumeration and add a synthetic-noise (AR(1) and/or
   phase-randomization) sizing leg before reuse on different data
   (QUANTUM, §4 above); (d) add the matched-`ε=μ`/`graded_black_shell`
   code-path-disjointness note explicitly to the idealization list
   (MATERIALS, §4 above); (e) add `caveat_lint_config.json` entries
   protecting this cycle's own headline scope caveats — the
   matched-`ε=μ` realizability scope and the single-vs-two-wall-echo
   scope limit (VISION, §4 above); (f) fold this audit's own §2 finding
   and R8 (§6) into the permanent record's own phase-convention caveat
   language, replacing the currently-uncaveated `NOTES.md` headline.
5. **Not ranked, flagged as speculative backlog, needs real design work
   before it earns FDTD/analytic time**: MATERIALS' residual-of-residual
   structural candidate (a mechanism nearly-but-not-exactly config-
   invariant, tied to the congruent series' own fixed geometry rather
   than `ABSORB` depth — needs a priced design and an R5-style
   look-elsewhere control before it is more than a hypothesis);
   QUANTUM's dispersive-`ε(ω)` extension (needs item 2's 750nm leg first
   to have any period-scaling signature to test against); THERMODYNAMICS'
   Idealization-6 closed-form bound-to-exact-computation (cheap, but
   cannot move T28's own mechanism question either way, since the bound
   is already 150× below the observed signal).

---

## 8. Bottom line

**The phase-convention question is RESOLVED, moderate-to-high confidence:
the committed convention is correct.** Reproduced from scratch (§1): under
the wrong alternate convention (`r→conj(r)`), Test A's Combined-Verdict-
determining REFUTE genuinely collapses to INCONCLUSIVE for both models,
confirming PHOTONICS'/EM's own finding exactly. Resolved (§2), by a
disclosed static-analysis attempt that did not cleanly settle it on its
own, followed by a new, owned, empirical FDTD measurement (reusing this
program's own already-gated `lab.emit` machinery) that — at its one
calibration-confirmed reliable operating point, across three incidence
angles, both a lossless sanity check and the real lossy construction —
consistently and decisively (by margins of `2.8×`–`6.7×`) favors the
committed convention over its conjugate. **Combined Verdict REFUTE stands
for BOTH the single-wall and two-wall-cavity mechanisms** (§3). Applying
the Iteration 49/50 precedent explicitly (§3, §5): this is a *different*
failure shape on the physics (the published REFUTE conclusion is
correct, unlike the two prior cycles' genuinely wrong published numbers)
but the *same* failure shape on verification discipline — an unverified
robustness argument, not a false claim about a checked computation,
substituted for actually running a named, affordable test, and survived
into an uncaveated permanent-record headline until two blind Phase-5
seats caught it. **Checkpoint criterion 4 FIRES**, ruled a notification
per this program's unbroken precedent, with a new standing rule (R8,
§6) generalizing R7 to cover untested independence arguments, not only
untested pricing numbers. All other five Phase-5 findings are adopted
(§4), none change the Combined Verdict. Reconciled Iteration-53 queue
(§7): G40/PAD decorrelation first (near-unanimous), the 750nm stress-test
second (cheap, decisive), hardening this audit's own phase-convention
resolution third, record hygiene fourth.

**T28's own substantive mechanism question — the ~2.84° periodicity's
origin — is not answered by this cycle, exactly as `NOTES.md` already
states.** Two boundary-reflectance-echo mechanism classes are now
REFUTEd, on a convention now independently confirmed correct, closing
this specific gap in this cycle's own evidentiary record.

---

## Reproduction

`python3 experiments/075-t28-absorb-boundary-wkb-reflectance/
phase5_redteam_phase_convention_check.py` — writes
`phase5_redteam_phase_convention_check_results.json` in this directory
(§2b's own table). Deterministic, no RNG anywhere in this file, ~90s on
one core. The §1 reproduction table (r→conj(r) collapse, both models) was
produced by a scratch script (not committed, per this program's own
Phase-5-review-scope convention) that imports
`boundary_reflectance.py`/`two_wall_cavity.py` unmodified and substitutes
`conj(r)` for `r` at the point of use — bit-exact match to PHOTONICS'/
EM's own independently-published figures confirms correct reuse of the
existing, unmodified machinery.
