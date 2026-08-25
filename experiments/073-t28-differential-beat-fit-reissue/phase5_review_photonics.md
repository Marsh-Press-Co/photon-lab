# PHOTONICS — Phase 5 Review · Panel Iteration 50 · exp-073 (T28 corrected differential/beat-fit re-issue)

*Fresh sub-agent, PHOTONICS charter (surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle?). Blind
to the other seats' Phase-5 reviews. Everything numeric below was
re-executed independently — `run.py` re-run end-to-end, `results.json`
diffed bit-for-bit against the re-run, G0-a/b/c re-derived from the raw
source JSONs in a clean script, and the sign-flip null's leverage
mechanism re-derived in closed form from scratch, not copied from any
seat's or Red Team's own numbers.*

---

## 0. Headline

**This cycle did exactly what it was pre-registered to do, and its own
safety machinery (`G0-e`, LOGBOOK R6) fired correctly, for a documented,
independently-reproducible reason, before any real data was touched.**
`Combined Verdict: HALT_NULL_MISCALIBRATED` is accurate: the corrected
sign-flip null (T2-3) that this cycle exists to install is itself
anti-conservative by ~2–6× nominal on this exact `n=31, p=5` design — a
leverage effect I re-derived independently in closed form (§2, below) and
confirm to the same value QUANTUM's Phase-2 critique and Red Team's Phase-2
audit each found by Monte Carlo. Four independent implementations now
agree on one number. T28's own substantive mechanism question is untouched
by this cycle, exactly as `phase4_results.md` states.

Re-running `run.py` reproduces `results.json` **bit-for-bit** (md5 match,
zero diff) — the cycle is genuinely deterministic and its own claimed
128.7s runtime is accurate on this machine. G0-a/b/c (grid identity,
telescoping, provenance) all re-derive to exact-zero residuals from the
raw source JSONs independently of `run.py`. The five-phase process itself
is the strongest I have read in this program's record: every one of five
blind Phase-2 critiques found a real, load-bearing defect with a workable
remedy, Red Team's audit independently re-implemented and confirmed every
one of them from scratch (not adjudicated from prose), and Phase 3
disclosed four further self-caught implementation bugs in the open. I have
one small, genuinely new, non-load-bearing finding this process did not
catch (§1), and one documentation-trail gap in how a self-caught
arithmetic slip was disclosed (§3). Neither moves the verdict.

---

## 1. F1 — [MINOR, independently found] `phase4_results.md` and `NOTES.md` both overstate the residual-structure leg's own failure count: 71/72, not 72/72 — 143/144, not 144/144

`phase4_results.md`'s own bottom line states: *"Result: both legs fail
every single cell-α combination — 72/72 (i.i.d.) and 72/72
(residual-structure)."* `NOTES.md`'s Result section repeats it: *"at
**every** one of 72 cell-α combinations per leg (144/144 fail)."*

I pulled `results["scored"]["g0e_ii"]["residual_structure_leg"]["table"]`
directly from the committed `results.json` and counted `pass_` flags:

```
n_fail_iid      = 72 of 72   (matches the claim)
n_fail_residual = 71 of 72   (does NOT match the claim of 72/72)
```

The one passing cell: `sigma=0.0005, psi0=4.71238898038469 rad (270°),
alpha=0.10, rejection_rate=0.132`, inside its own band
`[0.05975, 0.14025]` — `pass_=True`, verified directly against
`null_calibration_check`'s own `pass_=bool(lo <= rate <= hi)` construction
in `run.py`. The overall gate result is unaffected — `g0e_ii["pass_"] =
iid_pass AND pool_pass`, and `pool_pass = all(...)` is correctly `False`
regardless of whether 71 or 72 of 72 cells fail — so `HALT_NULL_
MISCALIBRATED` is the correct verdict either way, and this does not touch
the Combined Verdict, the leverage-mechanism finding, or any docket item.
But it is a factually wrong count in two committed deliverables, in a
cycle whose entire purpose is fixing exactly this class of unverified
numeric claim (the R4/verify-before-claim discipline this program adopted
after three straight cycles of hand-typed figures that did not reproduce
from the committed function). `phase4_results.md`'s own table of means and
ranges for the residual-structure leg (0.0566/0.036–0.076 at α=0.01, etc.)
is correct — I independently recomputed all six mean/range cells from the
raw table and they match to the printed digit — so this is narrowly the
"72/72" pass-count sentence, not the underlying data.

**Recommended fix, zero cost:** correct "72/72 (residual-structure)" to
"71/72" and "144/144 fail" to "143/144 fail" in both files, with a
one-clause note identifying the passing cell and confirming it does not
change the gate outcome (`pool_pass` still `False`).

---

## 2. Independent re-derivation of the leverage mechanism (a fourth confirmation, from scratch)

This is the load-bearing finding of the cycle (Attack 4 in
`phase2_redteam_audit.md`, QUANTUM's original Phase-2 critique), and it
deserved a fourth, fully independent check rather than a read-through — my
seat's own charter is angular dependence, and the mechanism QUANTUM
identified is precisely an angular-design property (where, across the
36°–42° window, the fitted design's own statistical leverage
concentrates), so I re-derived it exactly, in closed form, with zero
reference to any seat's code.

Using only the public window geometry (`theta` from `experiments/069-.../
results.json`, `CENTER_DEG=39.0`, `T_x = radians(2.49)·cos(39°)`) and the
frozen 5-column basis `[1, cosθ_c, −sinθ_c, u·cosθ_c, −u·sinθ_c]`:

```
cond(X5)              = 59.9167   (QUANTUM: ≈60; matches exactly)
mean diag(M5)          = 0.83871  (= (n-p)/n = 26/31 exactly, an algebraic
                                     identity independent of psi, verified)
E[Var(Rq_surr)]/Var(Rq_obs)
    at psi0 =   0°  =  0.7908
    at psi0 =  45°  =  0.7951
    at psi0 =  90°  =  0.8005
    at psi0 = 135°  =  0.7962
```

(psi0 = 180°/225°/270°/315° reproduce the first four exactly, by the
π-periodicity of `cos`/`sin` in this basis — an exact symmetry I did not
see stated anywhere in the record and note here as a small closed-form
consistency check.)

This is QUANTUM's own reported 0.79 and Red Team's own independently
re-derived 0.7943, confirmed a **fourth** time, from a fully independent,
zero-simulation, closed-form route (mine is exact linear algebra on the
population moments, not Monte Carlo — QUANTUM's and Red Team's own figures
are the Monte-Carlo estimate of the same exact quantity, so the ~0.001–0.01
spread between all four numbers is exactly what sampling noise on that
statistic predicts, not disagreement). **The mechanism is real, exact, and
robust across the entire carrier-phase range this cycle's own calibration
sweep covers — not an artifact of one seed or one implementation.**

One genuinely new, forward-looking observation from my own charter, not
raised elsewhere in the record: `mean diag(M5) = (n−p)/n` is an exact
algebraic identity of OLS (`trace(M5) = n−p` always), so it does **not**
depend on window width — extending the window (the still-standing PLAN.md
queue item 4, `θ_max≈46°`) will not, by itself, remove this floor. What
*can* change with a wider window is **where** leverage concentrates within
the design (my own closed-form check above shows the `R_q`-extraction
row's weighting is not uniform across θ, concentrating toward the window's
own extremes for this basis) — but that is a distinct, unverified claim
about the *shape* of leverage at a wider window, not the *size* of the
`(n−p)/n` floor. Any future adoption of this or a corrected null at an
extended window must re-run its own `G0-e(ii)`-style calibration on the
new design (already required by docket item 3(c) / `NOTES.md`'s standing
rule) — I flag this only to make explicit, from the angular-design side,
*why* that requirement cannot be waived on the assumption that a wider
window "obviously" fixes calibration: the exact `(n−p)/n` component of the
problem is a sample-size/parameter-count property, not an angular-span
property, and will persist at any window using this same 5-column basis.

---

## 3. F2 — [MINOR, documentation-trail gap] `phase1_proposal.md`'s own frozen G0-e(i) cell count is self-inconsistent, self-caught during implementation, but not listed among Phase 3's four disclosed "Ambiguity" items

`phase1_proposal.md` §4 G0-e(i) lists `ΔP ∈
{±0.005,±0.01,±0.02,±0.04,±0.08,±0.10}` — twelve explicit signed values —
then computes the sweep total as *"3×3×6×32 = 1,728 cells"*, treating the
ΔP axis as six values, not twelve. The two statements in the same
paragraph are inconsistent by exactly a factor of 2.

`run.py`'s own inline docstring for `ground_truth_recovery_check` catches
this directly and states it plainly: *"phase1_proposal.md's own
'3x3x6x32=1728' arithmetic undercounts by exactly 2x relative to its own
ΔP definition (six magnitudes, each signed = 12 values, not 6); this is
disclosed in phase3_synthesis.md as a self-caught issue, not a docket
item."* I checked: the implemented primary leg does correctly use 12
signed values (3,456 cells, matching `phase3_synthesis.md` §2 item 1's own
corrected total and `results.json`'s own `g0e_i.legs.primary.n_cells =
3456`), so the actual gate is unaffected and the widened total (5,760
cells across all three legs) is right. But `phase3_synthesis.md`'s own
explicit disclosure apparatus — the four numbered "Ambiguity" items in §3,
built precisely to record exactly this class of self-caught, in-code
correction — does not include this one. It is present only implicitly, as
the corrected "12 signed values" figure quietly appearing in §2 item 1's
recap, with no note that it corrects the frozen proposal's own stated
arithmetic. A reader comparing `phase1_proposal.md`'s "1,728" against
`phase3_synthesis.md`'s "5,760" without reading `run.py`'s code comments
would not find the reconciliation written down anywhere in the two
higher-level documents.

This is smaller than the four documented Ambiguities (none of it is
outcome-determining, and the fix was in fact made correctly) — I flag it
because this cycle's own explicit purpose is closing exactly this
category of defect (an unverified figure in a frozen document), and the
fix here lived only in a code comment rather than in the disclosure
document built to hold it.

**Recommended fix, zero cost:** add a fifth item to `phase3_synthesis.md`
§3 (or a footnote to item 1) stating plainly that `phase1_proposal.md`
§4's own "1,728 cells" figure undercounts its own stated 12-value ΔP list
by 2×, and that the implemented sweep (3,456 primary cells, 5,760 total)
is correct.

---

## 4. What checks out (per house discipline)

Recorded so the two minor findings above do not read as bigger than they
are — this is the most thoroughly self-audited cycle in the T28 thread's
five-cycle history, and independent re-verification confirms nearly all
of it:

- **Reproducibility, exact.** Re-ran `run.py` end-to-end (128.7s,
  single-core) with no code changes; `results.json` is byte-identical to
  the committed file (md5 `05767887c6dd7491fb83ef37e5a495da` both before
  and after). No `git checkout` was needed — the re-run produced zero
  diff.
- **G0-a/b/c re-derive to exact zero from the raw source JSONs**,
  independently of `run.py`: θ grids bit-identical across
  `experiments/069/071` (and, per `results.json`, `072`); telescoping
  residual `max|delta_40_60+delta_60_70+delta_70_80−delta_40_80| = 0.0`
  exactly; provenance `max|delta_col − (C80−C40)| = 0.0` exactly.
- **The gate order and HALT logic in `score_all()`** correctly stop
  execution at `G0-e(ii)` before any of the four real pairs is analyzed —
  `per_pair` is genuinely empty in the committed `results.json`, not
  populated-then-discarded. `p073_2/3/4` are `None`, matching the "no real
  pair was scored" claim exactly.
- **PHOTONICS' own Phase-2 catch this cycle** (`A_i` tripwire dead code;
  G0-e(i)'s original generator structurally unable to exercise a
  phase-dominated, as opposed to period-dominated, config-to-config
  difference — squarely an angular-optics point, since a graded-absorption
  boundary is at least as likely to shift reflection phase as spatial
  period) is correctly and completely fixed: the `δa`/`Δψ` legs are live
  in the committed run (768 `A_i` checks, 0 failures at 1% tolerance;
  worst-cell recovery error 1.10% across all three legs, inside the 2%
  bar).
- **EM's `A_q = 2a_cbar·tanχ₀` re-derivation and its own "binds hard"
  correction (docket item 5)** are both faithfully implemented:
  `exp072_disclosure` in `results.json` reproduces exp-072's real,
  closed `χ₀` values (−0.0197/−0.0203/−0.0062/−0.0434 rad) exactly, and
  the prose is corrected to state the tan/sin correction is expected to
  stay numerically inert on this substrate.
- **VISION's T2-1 non-emptiness floor (docket item 7b)** is implemented
  exactly as specified — `t21_not_evaluable=True` when both non-`T_mean`
  candidates are excluded, verified directly in the code (`run.py:497-501`)
  rather than merely claimed.
- **The contamination disclosure (docket items 9–11)** is computed
  unconditionally in `_contamination_block()` and correctly reports
  `confirm_disclosure_required=false` this run, since no pair reached
  `RESOLVED`.
- **Predictions were genuinely frozen before the official run**: commit
  `c771a7e` ("Phase 3... predictions frozen") precedes `b5c3bd7`
  ("Phase 4: official run"), and the dev run disclosed in
  `phase3_synthesis.md` §4 (which correctly forecast `HALT_NULL_
  MISCALIBRATED`) is explicitly marked non-official and its own
  `dev_results.json` was deleted, not smuggled in as the committed file.

---

## 5. Verdict

**PARTIAL — matching the process's own honest self-assessment, not a
downgrade.** This is not a T28 physics result (T1 N/A, constraint 3 not
engaged, exactly as pre-registered) and cannot be scored PROMISING on that
axis. It is not RULED-OUT-class either — nothing here bounds a mechanism
class or closes a constraint. What it delivers is a genuine, independently
reproducible, generalizable **methodological finding**: a sign-flip/
residual-permutation null built by flipping the full-model residual on a
small (`n=31, p=5`), leverage-concentrated, carrier-conditioned angular
design is anti-conservative by ~2–6× nominal, independent of noise level,
carrier phase, or whether the noise is i.i.d. or drawn from real captured
FDTD residuals — caught pre-emptively by a gate built for exactly this
purpose, at zero cost to the program's LOGBOOK.md, rather than surviving
to contaminate a real result. That is `G0-e`/R6 working exactly as
designed, for the first time tested against a real (not synthetic-only)
failure mode. My own findings (§1, §3) are both minor, non-load-bearing,
and consistent with — not a break from — that overall assessment.

---

## 6. Ranked candidate directions for Iteration 51

T28's substantive question (what produces the ~2.84°-family periodicity in
the `C80−C40` padding delta) is exactly where exp-072 left it. Two
consecutive cycles have now failed to extract an answer from the
differential-fit route on this exact 36°–42° window — first via a sign
bug (exp-072), now via a null-calibration failure (exp-073) — a pattern
that argues for stepping back from patching the estimator a third time and
instead answering the data-free question already queued in PLAN.md before
spending further panel cycles or FDTD budget on this window.

### 1. Price the window before spending in it again — zero FDTD, decisive either way (PLAN.md Iteration-50 queue item 2, unexecuted)

EM's Cramér–Rao/conditioning pricing (`cond=529`, ≈6× SE inflation on a
two-tone joint fit in the current window) and QUANTUM's `|L(T)|` leakage
budget are both computable today with zero new data, and directly answer
the question this cycle's own HALT sharpens: can `θ∈[36°,42°]` ever
support a carrier-conditioned discriminator at achievable SNR, under *any*
correctly-calibrated null, not just the two the panel has now tried? If
the answer is no, that is a real, honest, publishable finding — the
closing bound on the differential-fit-in-this-window route — and it
retires the question rather than inviting a third null-construction patch
cycle. If the answer is yes, it directly justifies the FDTD spend in item
3 below. Given this cycle's own leverage finding is a sample-size/
parameter-count property that a wider window does not automatically fix
(§2, above), pricing should explicitly report how `cond(X5)` and the
leverage-concentration pattern would change at the candidate extended
window, not only the Rayleigh-separation number the queue item currently
emphasizes.

### 2. G40/PAD decorrelation, read on the phase-invariant amplitude channel, not a significance test (PLAN.md Iteration-50 queue item 3)

The cheapest remaining real FDTD relief on the board (~31 calls if the
geometry-reuse claim verifies), and it is orthogonal to this cycle's own
null-calibration failure: PLAN.md's own proposed readout — `√(A_i²+A_q²)/a`
— conditions on no carrier and needs no `p`-value at all, so it does not
inherit the sign-flip null's own demonstrated miscalibration. This
directly closes the `ABSORB`-or-`PAD`-tied caveat that has bound every
T28 deliverable since Iteration 48, independent of whether item 1 above
licenses further differential-fit work on this window.

### 3. Execute the still-standing, never-run WKB/adiabatic boundary-reflectance model for the graded-loss `ABSORB` band — zero FDTD, genuinely new to this ranking

Queued at Iteration 46/47 (THERMODYNAMICS' own proposal, folded into the
Iteration-47 desk-check batch "if capacity allows") and confirmed dropped
without execution by QUANTUM's own Iteration-47 Phase-2 critique ("found
PLAN.md's own suggested WKB fold-in silently dropped") — it has not run in
any of the five T28 cycles since. This is the one candidate on the board
that engages my own charter directly rather than as a statistics
re-verification: an analytic (not fitted) model of the reflection phase a
graded-absorption boundary of varying depth produces as a function of
angle, computed from the boundary's own admittance profile, zero data. It
can do one of two useful things at zero FDTD cost: **explain** the
~2.5° family as an ordinary boundary-reflectance phase effect tied to
`ABSORB`/`PAD` depth (closing T28's own mechanism question outright,
without needing another statistical test on an under-resolved window), or
**rule it out** as a candidate mechanism, narrowing the remaining
candidate space for whatever item 1's pricing result licenses next. Either
outcome is a genuine physics finding, not a third re-run of the same
under-powered discriminator.

---

## 7. Recommendation to the Director

`phase4_results.md`'s Combined Verdict and its account of why the gate
fired both stand — this is the rare T28 cycle whose own five-phase process
correctly caught what it was built to catch, and my own independent
re-verification (bit-identical re-run, closed-form leverage confirmation,
raw-JSON G0-a/b/c re-derivation) finds nothing that changes the verdict.
The LOGBOOK.md Iteration 50 entry should record two small corrections
alongside the headline (the 71/72-vs-72/72 residual-leg count in
`phase4_results.md`/`NOTES.md`, and the frozen proposal's own 1,728-cell
arithmetic slip, both non-load-bearing) and should state plainly that this
cycle's own contribution is a generalizable null-construction finding
about small, leverage-concentrated carrier-conditioned designs — directly
reusable by any future cycle, on this window or a wider one, that fits a
similar coefficient.
