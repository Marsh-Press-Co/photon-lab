# PHASE 5 — REVIEW · QUANTUM OPTICS · Panel Iteration 50 · exp-073

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5: non-classical
absorption, state-dependent or coherent interactions; expressibility
contract — mechanisms enter the bench only as effective classical
parameters or Red Team strikes them). Blind to the other six seats'
Phase-5 reviews this cycle. T1 N/A throughout, constraint 3 not engaged —
this is instrument/statistics re-verification work, identical in kind to
Iterations 46–49. My own charter duty this cycle is narrower and sharper
than usual: this cycle's headline finding (`G0-e(ii)`'s sign-flip-null
miscalibration, Attack 4) is a re-verification of a claim my own Phase-2
critique first raised — so my job here is to independently re-derive it a
further time, on my own, with zero reference to my own Phase-2 code or
QUANTUM's other artifacts beyond the algebra as published, and to audit
whether the cycle handled the resulting HALT with discipline or tried to
route around it.*

---

## 0. Verification method, disclosed up front

Everything numerically load-bearing below was computed, not read from
prose. Three checks:

1. **A fresh, from-scratch Monte Carlo** (new code, written for this
   review, with no reference to `run.py`'s `null_calibration_check` or to
   my own Phase-2 script) built from `phase1_proposal.md` §3b's prose and
   the `design_matrix` formula alone: real 31-point 36.0°–42.0° θ grid,
   `CENTER_DEG=39.0`, the 5-column frozen basis, a fixed carrier
   `T=2.49°` (matching `G0-e(ii)`'s own construction, confirmed by reading
   `null_calibration_check` *after* writing my own independent version, to
   check consistency without contaminating it), pure H₀ Gaussian noise,
   sign-flip `resid5` → `yhat0`, refit, empirical rejection rate at
   α∈{0.01,0.05,0.10}, `K=200` synthetic draws × `N=5,000` surrogates per
   draw (smaller than the official `K=500`/`N=20,000`, so noisier, by
   design — a genuinely independent, lower-powered instrument should still
   land in the same regime if the effect is real).
2. **Direct inspection of the committed `results.json`** and cross-checks
   against `phase4_results.md`'s own tables.
3. **A live re-execution of the actual committed `run.py`.** The shared
   execution environment this cycle is under heavy concurrent load — other
   seats' own Phase-5 sub-agents appear to be active in the same container
   (an untracked `phase5_review_thermodynamics.md` and several
   `analyze_pair()`-probing processes I did not author were observed
   running alongside mine), which cost several failed/contended attempts —
   but one clean, isolated run completed: 149.7s wall-clock (slower than
   the committed 128.7s, consistent with contention), `git`-diffable
   `results.json` before/after. **The rewritten file is bit-for-bit
   identical to the git-committed version already in the repo** (same
   `elapsed_s=128.68052124977112` internally — the pipeline's own fixed
   seeds make every numerical output, timing arithmetic included,
   reproduce exactly; only my own wall-clock observation of *this*
   invocation, printed separately, differed). Restored via `git checkout --
   results.json` immediately after (no net diff; verified). This is the
   strongest form of the requested check: not an independent derivation
   landing in the same regime, but the actual official artifact,
   regenerated from a live execution, matching to the last digit.

---

## 1. Findings

### Finding 1 — Attack 4 independently reproduced a fourth time. The official run's 5.4×/2.3×/1.7× figures are confirmed, both numerically and mechanistically.

Direct read of `results.json`: `scored.g0e_ii.pass_ = false`; the i.i.d.
leg's 24 cells give mean empirical rejection rates **0.0543 / 0.1143 /
0.1709** at nominal α = 0.01/0.05/0.10 — **5.43× / 2.29× / 1.71×** nominal,
matching `phase4_results.md`'s published 5.4×/2.3×/1.7× to the printed
digit, with the residual-structure leg (0.0566/0.1131/0.1707 — 5.66×/2.26×/
1.71×) reading the same, as Attack 7 predicted. Both legs fail all 72 of
their own cell-α combinations (144/144 total).

My own from-scratch Monte Carlo (method §0.1) reproduces the same regime
independently: **5.13× / 2.56× / 1.71×** at α=0.01/0.05/0.10 — different
code, different seed, a third of the surrogate count, and it still lands
inside the same 1.6–6× band every other implementation found. I also
independently re-derived the leverage mechanism in closed form on the real
design: `mean diag(M5) = 0.838710`, exactly `(n−p)/n = 26/31`; the
leverage-weighted variance ratio `Σᵢ row5ᵢ²·(M5)ᵢᵢ / Σᵢ row5ᵢ²` = **0.7908**,
matching QUANTUM's Phase-2 0.79 and Red Team's Phase-2 0.7943 to three
digits. This is not a coincidence of one lucky seed — the mechanism is
structural (a fixed property of the 31-point design and the 5-column
basis's own row-5 leverage weighting), which is exactly why every
independent implementation, mine included, lands in the same place.

**Tally**: three mutually independent from-scratch derivations — QUANTUM's
Phase-2 scratch code, Red Team's Phase-2 scratch code, and this Phase-5
review's fresh scratch code — converge on the same 2–6× anti-conservative
miscalibration, uniform across noise level, carrier phase, and residual
structure (i.i.d. vs. real captured FDTD residuals, per Attack 7/docket
item 4); a fourth check, a live re-execution of the official `run.py`
itself (§0.3), reproduces the git-committed `phase4_results.md`/
`results.json` figures bit-for-bit from a fresh run. I am not aware of
another finding in this program's history with more independent
corroboration behind it. **The reported figures are correct and
reproducible, both by independent derivation and by direct
re-execution; this is not in doubt.**

### Finding 2 — The cycle respected the Phase-2 hedge. It did not sneak in a fix.

My own Phase-2 critique this cycle closed with: *"Neither fully closes the
gap at this `n=31,p=5` design in my testing, so whichever is adopted,
`G0-e(ii)` must stay a binding, non-relaxable HALT — pre-register it now,
not as a discovery to explain away if it fires on the real (not just
synthetic) calibration sweep."* Red Team's audit (Attack 4) independently
tested both candidate fixes I had flagged (Freedman–Lane on `resid0`;
leverage-studentized `resid5`) and found **neither reliably clears
`G0-e(ii)`'s own bands either** (22 of 216 cell-α combinations still fail
for `resid0` in Red Team's own wider sweep) — and ruled explicitly against
mandating either as a same-cycle patch, instead hardening `G0-e(ii)`'s own
reporting requirements (docket item 3). `phase3_synthesis.md` implements
this verbatim: *"`G0-e(ii)` kept as a binding, non-relaxable HALT,
construction unmodified. Neither QUANTUM's candidate fix is adopted."* The
official run then legitimately HALTed, exactly as Red Team's own §6
forecast ("the most likely Phase-4 outcome... is `HALT_NULL_MISCALIBRATED`")
predicted before Phase 4 ran.

This is the correct outcome and a credit to the process, not a process
failure. Critically, docket item 3(a) also required the full calibration
table to be persisted **regardless of whether the cycle HALTs** — and it
was (both legs, all 144 cells, in `results.json`) — converting what could
have been a silent, uninformative dead end into a genuine, quantified,
reusable finding about this whole instrument class (small-`n`,
leverage-concentrated, carrier-conditioned ramp-coefficient sign-flip
nulls). That is R6/`G0-e` working exactly as designed, on the second try,
this time against a statistical-calibration defect rather than a sign bug.

### Finding 3 — Second consecutive T28 cycle with zero real pairs scored; the resolution question is untouched, and a Checkpoint-5 read deserves the Director's explicit ruling, not an assumed non-firing.

exp-072 (Iteration 49) scored all four pairs — none `RESOLVED`, Combined
Verdict `NEITHER`, but real `T_mean`, `R_q`, `ΔP`, and `p` values exist for
every pair. exp-073 scored **zero** — `per_pair` is empty; `G0-e(ii)` HALTed
upstream of `analyze_pair()` entirely. The differential/beat-fit
instrument's basic question — can this 6°/31-point window ever resolve
`R_q` for the two 10-cell `ABSORB` steps — sits exactly where exp-071's
Rayleigh-resolution finding (Iteration 48) left it three cycles ago. Two
full panel cycles of real work (a sign-bug fix and its verification in
exp-072, a null-calibration build and its verification in exp-073) have
advanced process discipline substantially and T28's own substantive
question not at all.

I checked this against LOGBOOK Checkpoint criterion 5 (two consecutive
non-advancing iterations). This program's own precedent (Iteration 48's
ruling on T28's third consecutive PARTIAL) held that criterion 5 does not
fire as long as each cycle delivers "independently verifiable, load-bearing
narrowing" — and exp-073 clearly does, in the same sense exp-069/070/071
did (Finding 1's leverage-mechanism characterization generalizes well
beyond T28). By that precedent, criterion 5 likely does **not** fire here
either. But I flag this as a genuine judgment call, not a self-evident
non-firing: this is now the **fifth** consecutive non-decisive T28 cycle
(46/47/48/72/73), and the last two specifically have alternated between
"scored every pair, resolved none" and "scored no pair at all" — a pattern
that is starting to look less like fresh process learning each time and
more like a route that keeps teaching the same two lessons (the window is
under-resolved; the statistics built to work around that are hard to
calibrate on this design) in slightly different packaging. That reading
does not, on its own, license a criterion-5 firing — the packaging changes
have each been real and non-trivial — but the Director should rule on it
explicitly rather than let the "narrowing" precedent apply itself by
inertia a fifth time.

### Finding 4 — Two of exp-072's own three deferred fixes (T2-1, T2-4) were never actually exercised against real data this cycle.

Only T2-3 (the null) was tested against a real gate on the real design
geometry — the calibration sweep uses the real θ grid and real 5-column
basis, and it failed. T2-1's admissibility logic and T2-4's coefficient
relabeling were validated only via (a) a stubbed dev-exercise explicitly
flagged *"not a result"* in `phase3_synthesis.md` §4, and (b) formula-level
correctness checks (T2-4 requires no code change at all; it is a
re-labelling of an existing coefficient) — never against a real,
gate-passing pair, because `G0-e(ii)` HALTed the official pipeline before
any real pair reached `analyze_pair()`'s scoring stage. The dev-stub *did*
reproduce Red Team's own Attack 5b prediction (`T_wrong` excluded at all
four pairs, `T_delta` admitted at three of four) — a genuinely good sign
for whichever future cycle finally reaches real scoring — but it is
disclosed by the cycle's own documents as non-authoritative, and a reader
of `phase4_results.md` alone, without cross-referencing
`phase3_synthesis.md` §4, could easily come away believing this cycle
validated three new pieces of machinery on real T28 data. It validated
one (T2-3, and only enough to learn it fails); the other two remain
paper-only one full re-issue cycle after being proposed.

### Finding 5 — R5/look-elsewhere risk: audited specifically, found clean.

Given my charter's standing duty to watch for R5's failure shape (a result
that looks decisive only because it was mined from a large, unconstrained
search), I checked `G0-e(ii)`'s own 144-cell-α calibration sweep against
it directly. It is not vulnerable to a look-elsewhere read: the failure is
**uniform**, 144/144, at every tested cell, by a margin of at least 1.6×
even at the single least-egregious point (α=0.10, best case). A
look-elsewhere concern applies to a result that could plausibly arise from
noise at some sub-fraction of a large search space (exactly R5's own
history, and the Addendum's `A_alt≈3·R_OUT`/`A_eff≈519` near-misses); a
null construction that is wrong at every single point it was tested is the
opposite pattern — it is what a real, structural effect looks like, not
what a look-elsewhere artifact looks like. Separately, I confirm Red Team's
own Attack 8: no LOGBOOK R5 ruled-out named-constant search reappears
anywhere in this cycle's document set. Clean on both counts.

### Finding 6 (minor, disclosure) — "three independent implementations" in `phase4_results.md` conflates two different kinds of check; this review adds a genuine fourth of the first kind.

`phase4_results.md` groups QUANTUM's Phase-2 scratch code, Red Team's
Phase-2 scratch code, and "this file's committed `run.py`" as "three
independent implementations." The first two are genuinely independent
*derivations* of the same claim from the algebra; the third is the actual
production code under test, not an independent re-derivation — its role is
to confirm the shipped pipeline behaves as the two scratch derivations
predicted, a different and equally valuable check, but not a third
instance of the same kind of evidence. Not load-bearing (the finding holds
either way, and is now even better supported), but worth stating precisely
for any future LOGBOOK citation of "three independent implementations":
this review's own from-scratch build (Finding 1) is the genuine fourth
instance of the *derivation* kind, and the fourth confirmation overall.

---

## 2. Verdict on this cycle

**PARTIAL**, consistent with Red Team's own §6 forecast and the pattern of
Iterations 46–49.

Process discipline is exemplary and should be recorded as such: a 12-item
mandatory-fix docket implemented with zero overrides, a real dead-tripwire
gap closed (Attack 1/PHOTONICS), a real specification gap in a flagship new
safeguard closed (Attack 5/VISION), a third recurrence of the same
stale-reference-slope defect finally closed (Attack 3/THERMODYNAMICS), a
structurally new contamination question named, bounded, and disclosed
rather than argued away (Attack 6, this cycle's own contribution) — and,
most consequential for my own charter, the cycle's single most important
finding (Attack 4's calibration failure) was neither downplayed nor
patched around under schedule pressure. It was pre-registered as a binding
HALT before Phase 4, and it was allowed to fire.

Substantively, T28's own question gained no ground, for the second
consecutive cycle (Finding 3), and the differential-fit instrument — the
actual deliverable this three-cycle sub-thread (071→072→073) exists to
build — has never yet produced a single scored real pair. No Checkpoint
criterion fires on the physics (T1 N/A throughout, as it has been since
Iteration 46). Criterion 4 (program-integrity drift) correctly does not
fire either: this is the textbook non-firing shape, the mechanism designed
to catch exactly this kind of defect working as intended, before any real
data was touched. Criterion 5 is a genuine judgment call (Finding 3), not
a settled non-firing, and I recommend the Director rule on it explicitly
rather than let precedent apply itself unexamined a fifth time.

---

## 3. Ranked top-3 candidate directions for Iteration 51

**1. Price the window before any further estimator or FDTD spend.**
PLAN.md's own Iteration-50 queue already ranked this second, right behind
this cycle's re-issue, unanimously across all six of exp-072's Phase-5
seats — and now that the re-issue has landed as a clean HALT rather than a
resolution, this item is *more* urgent, not less. EM's already-computed
Cramér–Rao/conditioning pricing (a 9-column two-tone design gives
`cond=529` and a 6.0× SE inflation on `R_q`, against a corrected
`|R_q|/SE_OLS` of 4.9/3.0/4.3/4.7) and my own `L(T)` leakage-function
budget (already established, exp-072 Iteration 49: `R_q` is
non-identifiable against essentially any periodic contributor from
~1.8°–5.0°, leakage 15–36 per unit amplitude) are both zero-FDTD, decisive
calculations that answer a question logically prior to "is the null
calibrated": can 36°–42° ever support a carrier-conditioned discriminator
at any achievable SNR, for *any* correctly-calibrated null? If the answer
is no — which EM's own number already suggests — that is a real, citable
closing bound on the differential-fit route in this window, worth more
than a sixth non-decisive cycle. This is the standing requirement my own
Phase-2 critique's methodology (the `L(T)` calculation) exists to satisfy,
and it should not wait behind further estimator engineering.

**2. G40/`PAD` decorrelation.** The cheapest FDTD build on the board
(~31 calls if MATERIALS' geometry-reuse claim verifies) and the only
currently-queued item whose own readout — the phase-invariant amplitude
channel `√(A_i²+A_q²)/a`, baseline 0.161/0.041/0.020/0.166 from exp-072 —
conditions on no carrier at all, meaning it is hostage to neither the
window-resolution problem (item 1, above) nor the null-calibration problem
this cycle just characterized. It relieves the `ABSORB`-or-`PAD` confound
that has bound every T28 deliverable under every verdict since Iteration
48, and it can run in parallel with item 1's own desk calculation since
neither depends on the other's outcome — a genuinely orthogonal source of
information while the differential-fit question is being priced.

**3. A properly pre-registered, freshly-calibrated null construction for
the ramp coefficient — explicitly gated on item 1's result, not built in
parallel with it.** This cycle characterized the failure mode exactly
(leverage-driven, `mean diag(M5)=(n−p)/n`) but deliberately declined to
ship a fix (Finding 2) — correctly, per Red Team's own reasoning that a
hasty second-generation fix risks shipping a second miscalibrated null
under false confidence. Building one properly (an exact small-sample
permutation test respecting the design's leverage structure, or a
finite-sample-corrected variance estimator, each requiring its own fresh
`G0-e(ii)`-style calibration test before gating anything, per docket item
3(c)) is real, worthwhile instrument-building — but only if item 1 shows
the window can support a discriminator at all. Building a better-calibrated
null for a window that cannot resolve the target signal at any achievable
SNR is solving the wrong stage of the problem; rank this third and
contingent, not second and parallel.

`R_contact`'s literature search remains orthogonal and unchanged in
ranking (11 consecutive cycles now, tooling-permitting) — not part of this
seat's own top-3 since it touches no live thread this charter owns, but
worth the Director's standing note that it has now outlasted every T28
sub-thread discussed above.
