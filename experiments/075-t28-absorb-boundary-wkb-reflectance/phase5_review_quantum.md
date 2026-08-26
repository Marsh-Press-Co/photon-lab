# PHASE 5 — REVIEW · QUANTUM OPTICS seat · Panel Iteration 52 (exp-075)

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5: non-classical
absorption, state-dependent/coherent interactions; expressibility contract —
mechanisms enter the bench only as effective classical parameters — σ(I),
σ(x,t), dispersive ε(ω), gain — or Red Team strikes them). Blind to the
other five Phase-5 seats and to Red Team's own Phase-5 final audit. This
cycle is fully classical (T1/constraint-3 not engaged); per the task brief,
my sharpest tool here is statistical/methodological rigor, as in prior T28
cycles — this review leans on that, plus one genuinely charter-relevant
point in §4.*

---

## 1. Verdict: **PARTIAL**

Both boundary-reflectance-echo mechanisms — the single-`-x`-wall echo
(`phase1_proposal.md`) and the correctly-derived two-wall cavity
(`two_wall_cavity.py`/`phase4_results.md`) — are REFUTEd on real data by a
test (Test A, period match) whose Combined-Verdict-determining conclusion I
find sound and reproducible. This is genuine, decisive, honestly-run work:
zero-FDTD, an exact (not linearized) transfer-matrix derivation with real
passivity gates, a pre-registered prediction that could have gone either way
and was scored against real data without retroactive threshold-tuning, and
a same-cycle correction of Red Team's own restated figure (3/6 → 4/6
negative pairs) — R4 applied one level further than usual, exactly as the
rule intends. That is PROMISING-caliber process discipline for an
instrument-fidelity cycle.

It stays PARTIAL, not PROMISING, for two reasons, one already disclosed in
the record and one new here:

- **Disclosed:** T28's own substantive mechanism question (the ~2.84°
  periodicity's origin) is not answered — two mechanism classes are ruled
  out, the phenomenon itself remains open. Consistent with every prior T28
  cycle's own PARTIAL pattern (Iterations 46-51).
- **New (§2, below):** the cycle's own new circular-shift null-calibration
  robustness check on Test B — the piece of machinery Red Team's Phase-2
  audit made mandatory specifically to keep a nominal `r²≥0.30` "SUPPORT"
  reading honest — is itself demonstrably anti-conservative when I size it
  against synthetic null data, by roughly the same mechanism and a
  comparable order of magnitude to this program's own already-logged R6(ii)
  finding on a *different* T28 instrument one cycle ago (LOGBOOK.md,
  Iteration 50/51). This does not change the Combined Verdict — Test A
  alone REFUTEs regardless — but it means the specific narrative claim
  built on this check ("not distinguishable from the autocorrelation-driven
  chance level," `phase4_results.md` §3) is *directionally* fine but rests
  on an uncalibrated instrument, not a validated one, and should not be
  cited forward as such.

---

## 2. Independent re-verification: the circular-shift null-calibration check, sized against synthetic data

*Task instruction to this seat, verbatim: "independently scrutinize this
NEW robustness check's own construction and result — is N=20,000 circular
shifts with a fixed seed=42 actually a sound, unbiased null-calibration
methodology here, or does it have its own gaps." Everything below is code
I ran this review, reading only `two_wall_cavity_results.json` and
`two_wall_cavity.py`'s own `circular_shift_null()` function — none
hand-typed.*

### 2.1 Reproduction — the headline number itself is right

`two_wall_cavity_results.json` reports Test B `r²=0.3042`, `r=-0.5516`
(recomputed bit-exact from the committed `predicted_delta_two_wall`/
`real_delta` arrays), and a circular-shift null-calibration `p=0.19525`
(printed as `p=0.1953` in `phase4_results.md`), null `mean|r|=0.2989`,
95th-pct `|r|=0.6800`, `N=20,000` trials, `seed=42`.

### 2.2 The construction: N=31 admits only 30 distinct circular shifts — "N=20,000" overstates the test's real resolution

`real_delta` has `n=31` points (the dense θ∈[36°,42°] sweep, 0.2° step).
A circular shift of a length-31 array by any `k∈{1,...,30}` is the
*complete* set of non-identity cyclic shifts — `np.roll` by `k` and by
`k+31` are identical, so **there are exactly 30 distinct null values this
test can ever produce**, not 20,000. I confirmed this directly: drawing
`rng.integers(1, 31)` 20,000 times (the script's own RNG call) hits all 30
possible shift values, each ≈610-723 times — pure resampling-with-massive-
replacement from a 30-point population.

I recomputed the **exact, exhaustive** p-value (enumerate all 30 shifts
once, no randomness) and it matches the reported Monte Carlo estimate
closely:

```
exact p (6 of 30 shifts have |r| >= observed)  = 0.200000
reported N=20,000 Monte Carlo p                = 0.19525
exact null mean|r|  (n=30)                     = 0.3006   (reported: 0.2989)
exact null 95th-pct |r| (n=30)                 = 0.656    (reported: 0.680)
```

So the reported number is **not wrong** — it is a good Monte Carlo estimate
of the true discrete population value. But the "N=20,000" framing is
misleading about what this test can resolve: its real granularity is
`1/30 ≈ 3.3%`, not `1/20,000`. The exhaustive enumeration is exact, ~700×
cheaper, and has zero seed-dependence — it should have been the reported
number, not a resampled approximation to it. This alone is a minor,
non-outcome-determining instance of this program's own R4 pattern (a
figure presented with more apparent precision/power than the underlying
population actually carries) — worth a one-line fix, not a rule violation.

### 2.3 The deeper question: is this null correctly SIZED? — No, measurably anti-conservative

Getting the arithmetic right is necessary but not sufficient. The real
question — the one this program's own standing rule (**R6(ii)**, adopted
Iteration 50 on `exp-073`, generalized to circular-shift nulls specifically
at Iteration 51 on `exp-074`, LOGBOOK.md) requires an answer to before any
significance test against a constructed null is trusted: **under a TRUE
null (no real relationship between the model curve and the data), how
often does this exact procedure falsely report significance?** That check
was never run this cycle. I ran it, two independent ways.

**Method 1 — AR(1) synthetic noise matched to `real_delta`'s own fitted
autocorrelation.** Fit AR(1) to the real curve: `rho_hat=0.870` (Yule-Walker
lag-1 estimate on the actual `real_delta` array — notably *not* the
0.92-0.94 figure `phase3_synthesis.md` §3.5 cites from exp-074's own,
different quantity, see §2.4 below). Generated 8,000 independent fresh
AR(1) realizations (zero true relationship to `pred_delta_two` by
construction — a fresh random seed each time) and ran the *exact* (30-shift,
not resampled) circular-shift test on each against the SAME fixed model
curve:

```
alpha=0.05   empirical false-positive rate = 0.1496   (2.99x nominal)
alpha=0.01   empirical false-positive rate = 0.1155   (11.55x nominal)
alpha=1/30 (test's own floor) = 0.1496
```

Swept `rho ∈ {0.75, 0.85, 0.92, 0.94}` (bracketing both my directly-measured
value and the cycle's own cited 0.92-0.94 figure) — the miscalibration
**gets worse, not better, at the higher end of that cited range**:

```
rho=0.75:  FP(alpha=0.05)=2.26x nominal   FP(alpha=0.01)= 8.17x nominal
rho=0.85:  FP(alpha=0.05)=2.90x nominal   FP(alpha=0.01)=11.15x nominal
rho=0.92:  FP(alpha=0.05)=3.46x nominal   FP(alpha=0.01)=13.83x nominal
rho=0.94:  FP(alpha=0.05)=3.83x nominal   FP(alpha=0.01)=15.77x nominal
```

**Method 2 — FFT phase-randomization surrogates** (assumption-light,
standard "surrogate data" technique: preserves the real curve's *exact*
power spectrum/autocorrelation function by construction, no parametric AR(1)
assumption). 6,000 surrogates of `real_delta` itself, same exact-30-shift
test against the fixed model curve:

```
alpha=0.05   empirical false-positive rate = 0.0655   (1.31x nominal)
alpha=0.01   empirical false-positive rate = 0.0335   (3.35x nominal)
```

Both independent methods agree in **direction** (anti-conservative — this
null under-reports how often chance alone produces `|r|` this large) though
differ in magnitude (AR(1): ~3-4x at α=0.05; phase-randomization, the more
rigorous of the two: ~1.3x at α=0.05, ~3.3x at α=0.01). This is the same
failure shape, and a comparable-to-modest fraction of the severity, of this
program's own already-logged finding one cycle ago on a *structurally
different* T28 instrument: R6(ii)'s original catch (`exp-073`, a
Freedman-Lane sign-flip null, ~2-6× nominal) and its own circular-shift
addendum (`exp-074`, ~38.9-46.1× nominal, on a regression-coefficient
significance test using per-config residual shifts). The common driver in
all three cases, confirmed independently each time: **strong short-window
autocorrelation makes circularly-shifted surrogates of a smooth curve
resemble each other's phase more than genuine independence would predict**,
narrowing the achievable null spread relative to what a correctly-sized test
needs.

### 2.4 A smaller, related gap: the cited autocorrelation figure is reused, not re-measured, for this specific array

`phase3_synthesis.md` §3.5 justifies the whole circular-shift design by
citing "T28's own real residuals are known θ-autocorrelated, lag-1≈0.92-0.94,
exp-074 Iteration 51." That figure is real, but it characterizes a
*different* quantity — the four `ABSORB` configs' own per-config C(θ)
fit-residuals from `fit_and_calibrate.py` (LOGBOOK.md Iteration 51). The
quantity actually null-tested here is the raw *difference* `C80(θ)-C40(θ)`
(`real_delta`), which I measured directly: **lag-1 autocorrelation = 0.848**
(simple demeaned-series estimate) to **0.870** (AR(1) fit) — real and
strong, but a genuine, unverified ~0.05-0.09 gap from the cited figure,
reused across a differencing operation without re-checking it survives.
Not load-bearing on its own (§2.3's sizing check sweeps this exact range and
finds anti-conservative bias throughout it, worsening toward the cited
higher end), but it is the same "a figure from elsewhere in the record is
cited as characterizing the quantity at hand without independently
re-measuring it" shape this program's R4 addenda exist to catch — flagged
here so it doesn't quietly become a second, compounding instance.

### 2.5 What this does and does not change

**Does not change:** the Combined Verdict. `phase3_synthesis.md` §3.5's own
combining rule scores Test B under the *bare* pre-registered band for the
verdict, not the robustness check — Test A alone REFUTEs, cleanly, and
nothing above touches Test A. It also does not overturn Test B's own
"NOT significant" reading in the direction that matters: an anti-conservative
null is biased *toward* finding significance, so a null shown to be
too-easily-beaten that *still* failed to reach nominal significance
(`p=0.1953` against a ceiling this cycle's own reported `alpha` checks would
put comfortably outside any of the ranges I tested) is, if anything,
slightly *more* trustworthy as "not significant" under a properly-calibrated
null, not less.

**Does change:** the confidence this specific instrument's numbers — `p=
0.1953`, `mean|r|=0.2989`, `95th-pct=0.6800` — deserve if cited forward.
`phase4_results.md` §3 reads them as validated, load-bearing narrative
support ("real information... not evidence for the mechanism," "genuine
work, exactly as designed"). Per this program's own R6(ii) standing rule
("any future ... significance test against a constructed null ... must
ALSO ship a pre-registered null-calibration test ... before any real data
is scored" — LOGBOOK.md, Iteration 50, generalized to circular-shift nulls
specifically at Iteration 51), that sizing step was not run before this
p-value was trusted narratively. It is new information a prior phase could
not have seen (the `circular_shift_null` function did not exist before
Phase 4), non-outcome-determining, and — matching this program's own
`exp-074` precedent for an analogous finding — I do not read this as firing
Checkpoint criterion 4; it is a genuine, disclose-and-fix-forward gap, not a
defended wrong claim.

---

## 3. Ranked top-3 Iteration-53 candidates (this seat's own ranking, blind to the other five)

**(1) Size the circular-shift null-calibration machinery before it is reused — cheap, zero-FDTD, closes the gap §2 opens.** Concretely: (a) replace the
20,000-trial resampled estimate with the exact 30-shift enumeration
(§2.2 — free, exact, removes the seed-dependence question entirely); (b)
add a synthetic-noise sizing leg (AR(1) and/or phase-randomization
surrogate, both implemented and validated this review) to
`circular_shift_null()` or a shared utility, following the `G0-e(ii)`
template already proven out on `fit_and_calibrate.py`; (c) re-measure, not
re-cite, the lag-1 autocorrelation of whatever specific array a future
circular-shift null is built on (§2.4). This is a direct, load-bearing
strengthening of PLAN.md's own already-queued Iteration-52 item 3 ("add ...
lag-1 autocorrelation figures as committed, reproducible script output ...
and a documented coupled-shift ... alternative leg to `calibrate_null`
before this ... machinery is pointed at a future dataset") — that item was
written for `fit_and_calibrate.py` specifically; I am extending it to cover
`two_wall_cavity.py`'s own, separately-built `circular_shift_null()`, which
is a fresh instrument that never went through the same scrutiny. Near-zero
cost (all the code needed is in this review's own working notes), high
value: prevents a future cycle from citing `p=0.1953` as a validated,
correctly-sized figure, exactly the mistake R4/R6 exist to head off before
it compounds.

**(2) G40/`PAD` decorrelation (PLAN.md's own already-queued Iteration-52
item 2) — still sound, still worth running.** From this seat's own
expressibility-contract lens: this is the one queued item that *relieves*,
rather than merely disclosing or statistically re-litigating, an actual
confound (`ABSORB`≡`PAD`+40 across every congruent T28 config since
Iteration 48) — real new information a boundary-reflectance analytic model
cannot supply, since that model only explains what `ABSORB` predicts, not
whether `PAD` was ever separable from it in the real data. Explicitly not
barred by the seventh-cycle rule (it targets the phase-invariant amplitude
channel, conditioning on no fitted carrier phase — a different instrument
class from the retired differential/two-tone fit). Orthogonal to items (1)
and (3); nothing in this cycle's REFUTE changes its priority.

**(3) A dispersive-ε(ω) extension of the (now twice-REFUTEd) boundary-echo
model — the genuinely QUANTUM-charter-flavored open thread this cycle
correctly declined to touch.** Both tested mechanisms use a *frequency-flat*
effective loss (`nu(x)` independent of ω — a lossy-conductor-like medium,
not a resonant/dispersive one; my own Phase-2 critique flagged this as "out
of scope for this fully-classical cycle and correctly not attempted"). A
genuinely dispersive `ε(ω)` band (relaxation- or Lorentz-type `nu(ω)`)
would change `arg(r(θ;ABSORB))`'s frequency scaling and could shift the
predicted interference period *independent of the geometric length scale
`PLANE_X`/`D_right`* that pinned both this cycle's models to the same
7.8°-15.4° range — the one lever this cycle's own zero-free-parameter
models never had. Stays inside this seat's expressibility contract (an
effective dispersive ε(ω), a named parameter, not an unexpressed quantum
claim) and is zero-FDTD, reusing the same transfer-matrix/passivity-gate
machinery with `nu` promoted to `nu(omega)`. Lower priority than (1)/(2)
because it is speculative (no evidence yet that T28's real period has any
ω-dependence signature to explain) and would need the still-untouched
`block_leg750` confirmatory leg (`phase1_proposal.md` Idealization 8) to
even test against a second wavelength — but it is the first candidate this
six-cycle sub-thread has had that could move the *period*, not just the
amplitude/shape, of a boundary-echo prediction toward 2.84°.

---

## 4. Seat-specific finding a general-purpose read would miss

**The expressibility contract is honored correctly, and the passivity
resolution of the sign/branch ambiguity (`phase1_proposal.md` Idealization
2b) is exactly the right kind of physical reasoning for a coherent-optics
claim, worth naming explicitly.** This cycle's mechanism — a complex
effective index `n(x)=1-i·ν(x)/ω` derived from a friction-type PDE — hit a
genuine two-branch ambiguity (conjugate solutions of `k(x)²`), and resolved
it not by trying both and picking the one that "looked right" but by an
unambiguous passivity requirement (`|r|≤1` for any source-free, PEC-backed,
loss-only stack — energy conservation, nothing more exotic) checked at 124
independent `(ABSORB,θ)` pairs, with the *failing* branch's own catastrophic
numbers (`|r|~1.8×10¹⁶` at the worst point) disclosed rather than quietly
dropped. This is a Kramers-Kronig-adjacent causality/passivity discipline —
the same kind of bound that governs whether an effective ε(ω)/σ(x,t)
parameter this program might propose in a future *phenomenon*-mechanism
cycle is even physically admissible, not just numerically convenient — and
it was applied correctly here to a purely classical numerical-boundary
question. A general-purpose read would likely wave this through as "they
checked energy conservation, good"; from this seat's own charter (owning
whether a proposed coherent/effective-medium parameter is expressible and
physically sound, not merely fitted), it is worth stating plainly that this
is the correct standard, done right, and is the reason I find zero fault
with §2b-2c of the derivation itself — my entire critique in this review is
about the *statistical* instrument built on top of it (§2), not the physics
underneath it.

Separately, on the same charter: the matched-`ε=μ` idealization
(`phase1_proposal.md` Idealization 2, MATERIALS' Phase-2 catch) is correctly
scoped as "a statement about the engine's own numerical boundary-condition
artifact, not evidence about physically realizable graded-absorber coatings
generally." That caveat matters to this seat too, for a reason the record
doesn't quite spell out: a matched-admittance (`Z=1` at every `x`, any
`ν(x)`) medium by construction has **zero** normal-incidence reflection from
admittance mismatch at any point inside the graded region — meaning
everything this cycle's `r(θ;ABSORB)` measures is *pure obliquity-and-grading*
reflectance, not the interior multi-layer scattering a real (μ=1) dispersive
coating would also show. That the two-wall model's own predicted shape still
comes out wrong-signed and five-times-too-small in amplitude against a
matched-admittance idealization that structurally suppresses one whole class
of reflection is, if anything, a mildly *stronger* argument for REFUTE than
the write-up claims — a real (unmatched) admittance profile would add
reflection terms this model cannot produce, and the real data's amplitude is
already *larger*, not smaller, than what the (more reflective per bounce,
in principle) real coating's matched-medium stand-in predicts. Not scored
here (no new falsifiable band was pre-registered for it), but worth noting
as a one-directional robustness point in this cycle's own favor that its own
authors did not claim.

---

## Reproduction of this review's own numbers

Every number in §2 was computed against the committed
`two_wall_cavity_results.json` (for `real_delta`, `predicted_delta_two_wall`,
and the reported `circular_shift_null_check` fields) via short scripts run
in this review — exhaustive 30-shift enumeration, AR(1) Yule-Walker fit and
synthetic-noise sizing sweep (`rho∈{0.75,0.85,0.92,0.94}`, `n_reps=6000-8000`,
seeds 999/12345), and FFT phase-randomization surrogate sizing
(`n_reps=6000`, seed 2024). None hand-typed; none of this required a new
FDTD call or a `lab/` diff — same zero-cost discipline this cycle's own code
already established.
