# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 53 · exp-076

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md: non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters (σ(I), σ(x,t), dispersive ε(ω), gain), or Red Team strikes
them). No memory of Phase 1–4 of this cycle, including having been this
cycle's own lead seat. Blind to every other seat's Phase-5 review and to
`phase5_redteam_audit.md`. Task brief: verify the R6/`G0-e` check's
disposition still holds for the real `G40` data (not just the synthetic
test); assess `rho_pad_absorb=0.2108`'s forward miscitation risk from the
expressibility-contract standpoint; propose a genuinely different, cheap
instrument for Iteration 54.*

---

## 0. What I checked, independently

Read `LOGBOOK.md` in full (RULED OUT R1–R8; LIVE THREADS T1–T28, with
T21/T24/T27/T28 read closely, including T28's full Iteration-46-through-52
narrative). Read the complete exp-076 record: `phase1_proposal.md`, all
five `phase2_critique_*.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `phase4_results.md`,
`results.json`, `g0e_amplitude_channel_check.py`/`_output.json`. Independent
computation performed, not taken on prose: recomputed baseline
`carrier_r_squared`/`T_mean_deg`/`amplitude`/`cond5` for all four
exp-072 pairs directly from `experiments/072-.../results.json`; extracted
the full swept `psi0`/`m_true` grids from `g0e_amplitude_channel_check_
output.json`'s raw `rows`; grepped `run.py`/`run_output.txt`/
`phase4_results.md` for any G0-e re-invocation at Phase 4; read
`experiments/072-.../run.py` lines 682–716 directly (the `rho_c`
docstring Red Team's audit quotes) to confirm the quotation is exact; cross-
checked `results.json::settling_gate` against `phase4_results.md`'s cited
`frac_39`/`frac_40` figures.

---

## 1. R6/`G0-e` disposition on the REAL `G40` data — holds, with one
confirmed process gap between what was promised and what `run.py` actually
executed

**The physics check: no sign of carrier-fit instability.** I compared the
real fitted carrier parameters for both new pairs against (a) the
synthetic sweep's own tested envelope and (b) the four baseline pairs'
historical range (recomputed independently from `experiments/072-.../
results.json`, not copied):

| Quantity | `PAIR_PAD` (real) | `PAIR_ABSORB40` (real) | Baseline range (C40–C60 … C40–C80) | `G0-e` synthetic sweep |
|---|---|---|---|---|
| `T_mean_deg` | 2.4075° | 2.4575° | 2.4865°–2.5325° | fixed generator period 2.49° (Case 1/2) |
| `amplitude` | 0.005155 | 0.005514 | 0.005245–0.005725 | n/a (synthetic `a0` swept separately) |
| `psi` (rad) | −1.6323 | −1.7245 | (not separately tabulated; psi is per-pair) | `psi0` swept 0→2π in 16 steps (π/8 grid) |
| `carrier_r_squared` | 0.4381 | 0.4323 | 0.4308–0.4451 | n/a (noiseless synthetic, R² not meaningful) |
| `cond5` | 62.84 | 61.11 | 59.90–60.99 | n/a |
| headline magnitude | `x=0.1194` (11.9%) | `y=0.0716` (7.2%) | `amp_ratio` 0.020–0.166 | `m_true` swept −160%→+160% |

Every real fitted quantity lands inside the range this program has
already characterized as ordinary for this exact 5-column ramped-carrier
instrument — `T_mean_deg` within 3% of the established 2.44–2.53° family
(not a new period, not an extrapolation), `carrier_r_squared`/`cond5`
statistically indistinguishable from the four baseline pairs. Mapping the
real `psi` values onto the synthetic sweep: `−1.6323 rad ≡ 4.651 rad (mod
2π)` and `−1.7245 rad ≡ 4.559 rad (mod 2π)`, both interior to the tested
grid (nearest swept nodes `4.3197`/`4.7124` rad) — not at an edge, not
outside the swept circle. The real headline magnitudes (11.9%/7.2%) sit
well inside the tested `±2%…±160%` range, an order of magnitude from
either boundary. **Conclusion: nothing about the real `G40` recovery
exercises `G0-e`'s validated envelope near an edge or outside it — the
disposition (`PASS`, worst-case `1.03×10⁻⁴`/`8.35×10⁻³`, both orders of
magnitude below the observed 7–12% effect sizes) transfers cleanly to this
cycle's actual data.** This directly confirms the specific concern R6 was
adopted to catch (a carrier/phase-conditioned fit rotating a real signal
into a spurious value) is not silently in play here.

**The process check, independently caught, not in the prior record.**
`phase1_proposal.md` §6 and `NOTES.md` Idealization 5 both state, in
near-identical language, that `G0-e` "will be re-confirmed unchanged (not
merely cited forward) before any real-data `amp_ratio` is reported,
matching exp-072's own `g0_pass` precondition structure." I checked what
`g0_pass` actually means in exp-072: `run.py` line 733 calls
`ground_truth_recovery_check(data["theta"])` **inline, inside the same
script that scores real data**, and gates `combined_verdict` on it
(`g0_pass=..., g0e=g0e` in the committed record) — an executable,
in-line precondition, not a citation. **exp-076's own `run.py` does not do
this.** `run.py` imports only two *functions* from
`g0e_amplitude_channel_check.py` (`exp072_run`, `_amp_ratio_recover`,
lines 116–119) to build its own scoring pipeline; it never calls
`g0e.main()` or re-executes Case 1/Case 2. `results.json` has no `g0e`/
`g0_pass` key anywhere (checked directly, full top-level key list);
`phase4_results.md` and `run_output.txt` both have zero occurrences of
"G0-e"/"g0e" (grepped). The synthetic check that exists is exclusively the
Phase-1 artifact (`g0e_amplitude_channel_check_output.json`, timestamped
before `run.py`'s first execution), never re-invoked at Phase 4.

**Severity, honestly scoped, not overstated.** This is a real gap between
a specific written claim and what the code does — precisely the class of
thing R4 exists to catch, now caught in a fresh Phase-5 pass rather than
carried forward unverified. But it is low-stakes, for a structural reason:
`g0e_amplitude_channel_check.py`'s synthetic generator (`P_true=2.49°`
fixed, `DENSE_ANGLES` fixed, `psi0`/`m_true` swept) takes **no input from
the real `G40` FDTD data at all** — unlike exp-072's `g0_pass`, which is
computed from the same `data["theta"]` the real fit uses and therefore
could in principle change run-to-run, exp-076's check is a pure,
data-independent code-correctness test. Re-running it at Phase 4 would
have reproduced the identical `PASS`/`1.03×10⁻⁴`/`8.35×10⁻³` figures
bit-for-bit — there is no scenario in which the real `G40` data could have
invalidated a check that never reads it. So: the *documentation* overpromises
a procedural rigor ("matching exp-072's own `g0_pass` precondition
structure") that was not literally implemented, but the *disposition
itself* — G0-e PASS, and the real data sitting safely inside its validated
envelope (§1 above, independently confirmed) — is not actually at risk.
**Non-load-bearing this cycle; a documentation/implementation-fidelity gap
worth a one-line correction, not a Checkpoint-4-shaped finding** (no false
verification claim about a *computation that was performed*; the claim
was about a *step that wasn't taken*, and the step's absence provably
couldn't have changed the answer given the check's own data-independence).

---

## 2. `rho_pad_absorb=0.2108` — the disclosed, non-gating disposition is
correctly held this cycle; the forward risk is real and belongs on the
LOGBOOK as a standing requirement, not a live problem

Independently re-verified `phase4_results.md`'s framing against
`results.json`: `rho_pad_absorb=0.2108` (`dp_pad=-0.05013°`,
`dp_absorb40=+0.13105°`, `dp_c40_c80=+0.06684°`), correctly reported as
"an uncalibrated magnitude signal, not distinguishable from a carrier-
choice artifact... no interaction claim is drawn from this value" — this
matches Red Team's Phase-2 downgrade (Attack 2) exactly, and I confirm
independently, against `experiments/072-.../run.py` lines 687–690
(quoted verbatim by Red Team, verified character-for-character against
source myself), that `rho_c`'s own documented disposition really is "NOT a
basis-stability check... entirely an artifact of each pair choosing its
own `T_mean`," and that `rho_c` has genuinely never been evaluated on real
data anywhere in this program's history (`rho_c=None`,
`p072_3="NOT_EVALUABLE"` in the committed exp-072 record — confirmed).
This cycle's handling is correct and disciplined: the number is reported,
labeled uncalibrated, and never used to certify anything.

**The forward risk, from my charter's own R6/`G0-e`-ownership standpoint.**
R6's literal text mandates a pre-registered synthetic ground-truth recovery
test for "any future estimator that conditions on a fitted carrier or
phase parameter" *before real data is scored against it*. `delta_P_obs`
(and therefore `rho_pad_absorb`, built from it) is exactly such an
estimator — it is `R_q`-derived, carrier-conditioned, per-pair-refit — yet
**no `G0-e`-style synthetic recovery test exists for `delta_P_obs`'s
telescoping behavior anywhere in this program.** This cycle's own
`G0-e` check (§1, `g0e_amplitude_channel_check.py`) validates only
`amp_ratio`'s `A_i`/`A_q` recovery; it says nothing about whether
`delta_P_obs`'s own additive telescoping (`S` vs `D` in the `rho_c`/
`rho_pad_absorb` formula) recovers a *known* injected non-additivity
correctly, or how a genuine interaction would be distinguished numerically
from ordinary independent-carrier-fit sensitivity. This is not a defect in
what exp-076 built — R6 does not require validating a quantity that is
never used to gate anything, and this cycle's own disposition (§4 of
`phase3_synthesis.md`) explicitly and correctly refuses to gate on
`rho_pad_absorb` — but it means the number's *only* current protection
against future over-reading is disclosure text, not machinery. A future
cycle that wants to *use* `rho_pad_absorb` (or `rho_c`) as an actual
interaction test — the natural next move once this quantity is sitting in
the record with a specific numeric value — would need to build exactly the
kind of dedicated `G0-e`-style synthetic ground-truth recovery test (inject
a KNOWN interaction, sweep the two pairs' independently-fit carriers,
confirm recovery) that R6 already requires and that does not yet exist for
this specific estimator. **This is the standing forward requirement I am
flagging for the LOGBOOK**: `rho_pad_absorb`/`rho_c` promotion from
disclosed diagnostic to any calibration or gating role must clear its own
`G0-e`-class check first — the identical rule this program has now applied
to `amp_ratio`, `R_q` (exp-072/073), and the 9-column design (exp-074),
never yet applied to this specific carrier-telescoping construction.
Nothing about this cycle's own use of `0.2108` violates that rule (it
never gates); the risk is entirely in how a *later* cycle might cite the
number once it exists in `results.json` with an eye-catching value well
above the retroactive baseline figure (`≈0.041`, Red Team's own Phase-2
side computation) — exactly the kind of number that looks more meaningful
out of context than the record currently licenses it to be.

---

## 3. A genuinely different, cheap instrument for Iteration 54 — resolving
the 600nm/750nm ordering-flip tension without the retired differential/
two-tone class or another fringe-fitting leg

The 750nm advisory leg's ordering flip (`x>y` at 600nm vs `x<y` at 750nm,
`phase4_results.md`) and PHOTONICS' own Phase-2 aliasing attack (every
config this cycle runs sits at an exact integer multiple of λ at 600nm:
`ABSORB=40→2.000λ`, `ABSORB=80→4.000λ`) point at the same underlying
question: is the `PAD_TIED` reading a wavelength-dependent *resonance*
feature of the graded-loss boundary's own reflectance spectrum, or a
genuine broadband domain-construction effect? Every instrument this
sub-thread has ever built to ask a question like this — `amp_ratio`,
`R_q`/`delta_P_obs`, `rho_c` — answers it by fitting a carrier to a narrow
angular window at ONE wavelength at a time, then comparing across separate
FDTD legs. That is expensive per data point (a fresh 16–31-call sweep per
wavelength) and, per Attack 4 (Red Team, this cycle), the existing 750nm
leg is itself narrower/less-powered than the 600nm one — comparing two
differently-conditioned instruments, not a clean apples-to-apples
spectral read.

**Proposed instrument: single-shot broadband reflectance spectroscopy of
the `ABSORB` boundary — a pulsed (not CW) source, one run per config, FFT
of the time-domain reflected-field record at the measurement plane.**
This is standard FDTD practice (a short Gaussian/Ricker pulse injected
along the source's existing line-current geometry, `lab/fdtd2d.py`'s own
CW machinery swapped for a single broadband excitation), reuses the
already-validated `Sim` engine with zero new physics, and answers the
aliasing/resonance question directly and continuously across wavelength —
in perhaps 3 runs (one per config: `C40`, `G40`, `C80`), not 3×31 angle-λ
combinations. Read off the reflected-power spectrum `R(λ)` (or, at
fixed θ near the dense window's own center, the reflected-field spectrum)
for each config; a genuine resonance tied to `ABSORB`'s electrical
thickness (2λ, 4λ at 600nm specifically) would show as a spectral feature
localized near those wavelengths, present in `C80`'s spectrum but shifted
or absent in `G40`'s (same `ABSORB=40` as `C40`, different domain) — a
directly falsifiable, single-run-per-config signature, orthogonal to the
entire carrier-fit/angular-fringe family this sub-thread has used since
Iteration 46, and squarely inside my own charter's expressibility
contract: it treats `ABSORB` exactly as what it structurally is, an
effective classical σ(x) absorption profile, and asks a first-principles
question (does its reflectance depend resonantly on λ/thickness) about
that profile directly, rather than inferring it indirectly through a
near-field angular envelope-mismatch statistic several processing steps
removed from the boundary's own optical response.

This is NOT the retired instrument class — no sign-flip/permutation null,
no `R_q`-conditioned significance test, no carrier-fit at all; it is a
direct spectral read of a passive boundary's reflectance, the same
zero-FDTD-adjacent idiom PHOTONICS' own WKB/adiabatic transfer-matrix model
(exp-075) already computes analytically but has never been cross-checked
against a genuine broadband FDTD measurement — this closes that gap too.

---

## 4. Verdict

**PARTIAL** — the instrument (`G40`, the `amp_ratio`/9-cell scheme, the
settling precondition, the R6/`G0-e` discipline) is soundly built and its
headline result (`PAD_TIED`) is real and independently reproducible; I
confirm every load-bearing number in `phase4_results.md` against
`results.json` and find no arithmetic or physics defect. But (a) the
settling gate and R6/`G0-e` disposition, while both genuinely PASS on
independent re-verification, carry one confirmed process gap each — the
G0-e re-confirmation NOTES.md promised was not literally executed at Phase
4 (§1, non-load-bearing but real), and (b) the cycle's own headline finding
is explicitly not wavelength-general (the 750nm leg flips the ordering,
narrower window, advisory-only) — T28's substantive mechanism question is
narrowed, not answered, exactly as `phase4_results.md`'s own Bottom Line
states.

No Checkpoint criterion fires from this seat. The G0-e re-confirmation gap
(§1) does not rise to criterion 4 — it is a documentation/implementation-
fidelity discrepancy about a step whose absence provably could not have
changed the answer (the check is data-independent), not a false claim
about a computation that was performed and trusted. Flagging it for the
Director's record rather than for a Checkpoint firing.

---

## 5. Ranked top-3 candidate directions for Iteration 54

1. **Broadband pulsed reflectance spectroscopy of `C40`/`G40`/`C80`'s
   `ABSORB` boundary** (§3 above) — ~3 FDTD calls, genuinely orthogonal
   instrument class, directly and continuously tests the resonance-vs-
   broadband question the 600nm/750nm ordering flip only hints at
   discretely, and cross-validates PHOTONICS' already-built (exp-075) but
   never-FDTD-checked analytic transfer-matrix reflectance model against a
   real spectrum for the first time.
2. **A `G0-e`-class synthetic ground-truth recovery/telescoping check for
   `delta_P_obs`/`rho_c`**, built and run BEFORE any future cycle attempts
   to use `rho_pad_absorb` as an actual calibration or interaction test
   (§2 above) — cheap (zero FDTD, reuses the same synthetic-injection
   idiom this cycle's own `g0e_amplitude_channel_check.py` already
   established), and closes the one R6-shaped gap this cycle correctly
   avoided triggering but did not close.
3. **The already-flagged full-width (6°/31-point) non-aliased `G40` leg at
   a genuinely non-integer-λ wavelength** (`phase4_results.md`'s own
   stated precondition for any wavelength-general citation of `PAD_TIED`)
   — not a new instrument class, the natural, disciplined completion of
   this cycle's own explicitly-scoped idealization (§5, Idealization 1),
   ranked third because it is confirmatory rather than orthogonal: it
   would settle whether `PAD_TIED` generalizes, but (unlike #1) cannot by
   itself explain *why* the ordering flips.

---

## 6. Flags for the Director's LOGBOOK.md/PLAN.md update

- **T28 update**: `OUTCOME=PAD_TIED` at 600nm (`x=0.1194` HIGH,
  `y=0.0716` MED) is a real, load-bearing correction to how Iterations
  48–52's congruent-series `ABSORB`-depth causal claims should be cited —
  independently confirmed here, not just carried forward from Phase 4.
  The 750nm advisory leg's ordering flip means this is NOT yet a
  wavelength-general finding — cite with that caveat until a full-width
  non-aliased leg lands (item 3 above).
- **New standing forward requirement (R6-adjacent, not a new rule
  number — an application of R6's existing text)**: `rho_c`/
  `rho_pad_absorb` (the `R_q`-derived carrier-telescoping diagnostic) has
  never been validated by a `G0-e`-class synthetic recovery test and must
  clear one before any future cycle promotes it from disclosed-only to a
  gating or interaction-calibration role (§2 above).
- **Process note, not a Checkpoint firing**: `NOTES.md` Idealization 5 and
  `phase1_proposal.md` §6's claim that `G0-e` would be "re-confirmed
  unchanged... before any real-data `amp_ratio` is reported, matching
  exp-072's own `g0_pass` precondition structure" was not literally
  implemented in `run.py` — no `g0e.main()` call, no `g0e`/`g0_pass` key
  in `results.json`, zero mentions in `phase4_results.md`/`run_output.txt`
  (all confirmed by direct grep/read). Non-load-bearing because the check
  is provably data-independent (§1), but the phrasing should be corrected
  in any future citation of this cycle's own precondition discipline, and
  future cycles that promise an in-line re-confirmation gate (as exp-072
  actually built) should implement it as an executable call, not a
  documentation-only claim.
