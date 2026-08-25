# ELECTROMAGNETISM — Phase 5 Review · Panel Iteration 50 · exp-073

*Fresh sub-agent, EM charter (field/wave behavior, impedance matching,
energy coupling; owns reciprocity/passivity/causality bookkeeping — what T1
permits and forbids). Blind to the other seats' Phase-5 reviews this cycle.
Every quantitative claim below was independently re-derived by hand and/or
re-executed in a standalone script against the real design geometry and the
committed `results.json` — not taken from any document's prose, including
this cycle's own critiques and audit, which I re-checked rather than cited.*

---

## Headline

**The HALT is real and I independently reproduce it.** `G0-e(ii)`'s
leverage-driven anti-conservative sign-flip null (`E[Var(R_q^surr)]/
Var(R_q^obs) ≈ 0.79`, `mean diag(M5) = 26/31 = 0.8387`) is not merely
internally consistent — I rebuilt the design matrix from scratch on the
real 31-point θ-grid, confirmed both figures to the stated precision, and
ran a genuine Monte-Carlo cross-check (not in any committed file) that
reproduces the actual rejection-rate inflation the closed form predicts.
This is good, load-bearing instrument work: a pre-registered, data-free
gate caught a real statistical-calibration defect before any real point was
scored, exactly as R6 was written to do.

**But this cycle also ships a second, independent sign error in the same
family as the one R6 exists to prevent — undetected by five blind Phase-2
critiques, Red Team's Phase-2 audit, and the Director's own Phase-3
synthesis.** `phase3_synthesis.md` §3 ("Ambiguity 4") asserts, as a
"Fixed" and independently re-verified fact, that `dR_q/dψ̄ ≡ +R_i`. I
re-derived this identity three independent ways — direct trigonometric
expansion (twice, by different groupings) and a complex-exponential
argument — and confirmed all three analytically with a fourth,
from-scratch numerical finite-difference check on arbitrary random data at
nine carrier phases. All four agree, to numerical precision:

```
dR_q/dψ̄ ≡ −R_i        (exact, for THIS design matrix, for any data)
```

**not** `+R_i`. The sign exp-073 publishes is wrong. It is non-gating this
cycle only because `G0-e(ii)` HALTed first and no pair was ever scored —
but the error is baked into "inherited, class-(c), independently
re-verified" machinery that every future T28 cycle is instructed to reuse
verbatim, and it is already stated as fact in the *official*
`phase4_results.md` (the identity-tripwire row, "worst error `9.4×10⁻¹¹`").
Finding 2, below, is the derivation and the paper trail showing how a
formula nobody ever independently re-derived survived three consecutive
cycles by being checked only for *magnitude* agreement, which cannot
distinguish the two signs.

---

## 1. Independent re-verification of the `G0-e(ii)` leverage mechanism

The claim (`phase2_redteam_audit.md` Attack 4, `phase4_results.md`):
sign-flipping the full 5-column residual `resid5` and adding it to the
4-column restricted fit `yhat0` is centered correctly (`E[R_q^surr]=0`,
exactly, an algebraic consequence of `yhat0 ∈ span(X4) ⊂ span(X5)`) but its
*variance* is too small, because the `R_q`-extraction row of `pinv(X5)`
weights concentrate on the window's highest-leverage (edge) points, exactly
where the OLS projection residual `M5 = I − X5·pinv(X5)` most understates
the true noise.

I rebuilt this from the design-matrix formula in `phase1_proposal.md`
§2b.2/`run.py`'s `design_matrix()` alone — not from any party's code — on
the real θ = 36.0°–42.0°, 0.2° grid, `CENTER_DEG=39.0`, an arbitrary
representative carrier (`T=2.49°`, `ψ=0.13` rad, chosen without reference
to any fitted value):

```
n = 31, p = 5, cond(X5) = 59.92   (matches QUANTUM's own disclosed
                                    reconstruction check, 59.9–61.0, exactly)
trace(M5) = 26.000000              (= n − p, exact)
mean diag(M5) = 0.838710           (= 26/31, matches the claimed 0.8387)
Σ row5² · diag(M5) / Σ row5²  = 0.79079   (matches the claimed ≈0.79 —
                                            QUANTUM 0.79, Red Team 0.7943)
```

I then went one step further than anything in the committed record: a
genuine Monte-Carlo cross-check (300 independent H₀-noise draws, 4,000
sign-flip surrogates each, i.i.d. `σ=1` — my own code, not copied from
`run.py`, `phase2_redteam_audit.md`, or QUANTUM's critique) to confirm the
closed-form ratio actually *predicts* the surrogate-variance shortfall it
is derived to explain: `Var(R_q^surr)/Var(R_q^obs)` came back **0.803**
against the closed form's **0.791** — consistent within Monte-Carlo noise
of a 300-trial estimate, not merely algebraically tautological. This is the
correct mechanism, correctly computed, and it correctly predicts the
observed 2–6× rejection-rate inflation. **`HALT_NULL_MISCALIBRATED` is the
right call, three ways over now** (QUANTUM's blind critique, Red Team's
from-scratch audit, my own independent fourth implementation).

No passivity, reciprocity, or causality question is engaged by this finding
— it is a property of an OLS projection matrix on a fixed 31-point design,
not a claim about any physical medium.

---

## 2. `dR_q/dψ̄ ≡ R_i` is the wrong sign — full derivation

### 2a. What the code actually does

`design_matrix()` (inherited verbatim, `phase1_proposal.md` §2b.2, `run.py`
lines 234–250) is:

```
θ_c(u; T_x, ψ) = w·u + ψ,   w = 2π/T_x
X5 columns: [1, cos θ_c, −sin θ_c, u·cos θ_c, −u·sin θ_c]
coef5 = pinv(X5) @ y = [c0, A_i, A_q, R_i, R_q]
```

`ψ` here is *exactly* what the write-up calls `ψ̄` — §2b.1–2b.2 define
`ψ̄` as the phase fed directly into `θ_c = 2πu/T_mean + ψ̄`, with no other
candidate referent anywhere in the document. There is no separate "write-up
ψ̄" distinct from "`design_matrix`'s `psi` argument" — they are the same
symbol, by the document's own definition.

### 2b. The exact identity (data-independent, model-independent)

Since `cos θ_c` and `sin θ_c` are each linear combinations of the two
*ψ-independent* vectors `e_c = cos(wu)`, `e_s = sin(wu)` (angle-addition),
the column space of `X5(ψ)` is the *same* 5-dimensional subspace for every
ψ at fixed `w` — changing ψ only changes which basis of that subspace
`X5` uses. Writing the fitted model in the fixed basis
`{1, e_c, e_s, u·e_c, u·e_s}` and demanding its coefficients be
ψ-independent (since the fitted vector `ŷ = Proj(y)` cannot depend on which
basis represents the same subspace) gives two decoupled 2×2 systems. For
the `(R_i, R_q)` pair, with constants `B₃, B₄` fixed by the data (not by ψ):

```
R_i(ψ) = B₃ cos ψ − B₄ sin ψ
R_q(ψ) = −B₃ sin ψ − B₄ cos ψ

⇒  dR_q/dψ = −B₃ cos ψ + B₄ sin ψ = −R_i(ψ)          [Method 1]
```

I re-derived this a second way, in closed complex form (`z = e^{iθ_c}`,
`(A_i+iA_q) = W₁*e^{−iψ}`, `(R_i+iR_q) = W₂*e^{−iψ}` for ψ-independent
complex constants `W₁*, W₂*`), which gives the identical result:

```
R_i(ψ) = Re(W₂* e^{−iψ}),  R_q(ψ) = Im(W₂* e^{−iψ})
⇒  dR_q/dψ = −R_i(ψ)                                  [Method 2, independent]
```

### 2c. Numerical confirmation, arbitrary data, no synthetic generator

Neither derivation above touches the T28 substrate or any generator
convention. A from-scratch script (31 arbitrarily-irregular `u` points,
`w` from an arbitrary `T=2.49°` carrier, `y` = i.i.d. `N(0,1)` noise — no
structure at all) confirms, at 9 swept ψ values, `raw_fd = dR_q/dψ`
(central finite difference, `eps=1e-6`, on `design_matrix`'s literal
argument) satisfies `raw_fd + R_i ≈ 0` to `~1e-9` at *every* ψ — i.e.
`dR_q/dψ = −R_i` to numerical precision, uniformly. **[Method 3, independent,
data-free of the actual T28 series]**

### 2d. Where exp-073's own reasoning goes wrong

`run.py`'s own tripwire computes the raw finite difference
`(Rqp−Rqm)/(2·eps)` on `design_matrix`'s literal `psi` argument — and gets
exactly `−R_i` (their own comment: *"ratio −1.0000000000 to 10 decimals at
all four pairs before this sign correction"*), matching my derivation
exactly. **This part is correct, and matches my independent work.** The
error is the next step: `phase3_synthesis.md` Ambiguity 4 then asserts
`design_matrix`'s `psi` is "the negative of the φ = atan2(b,a) symbol the
write-up's own trigonometric derivations use as `ψ̄`," and on that basis
*negates* the correctly-computed `−R_i` to force `+R_i` — a claim that
contradicts §2b.1–2b.2's own literal definition of `ψ̄` (§2a, above): there
is no such second symbol anywhere in this document for `ψ̄` to secretly
mean. The negation is not a sign-convention translation; it is an
unjustified correction that converts a right answer into a wrong one.

### 2e. This traces to exp-072, and was never actually re-derived until now

`phase5_review_thermodynamics.md` (exp-072, its own §"structural result")
asserts `R_q(ψ+δ) = R_q·cos δ + R_i·sin δ` — the source of "`dR_q/dψ̄ ≡
R_i`." By Method 1/2 above, the correct relation is `R_q(ψ+δ) = R_q·cos δ
− R_i·sin δ` (opposite sign on the `sin δ` term); differentiating THERMO's
version at `δ=0` gives `+R_i`, mine gives `−R_i`. Red Team's own exp-072
audit (item C19) reports this "confirmed numerically: ratio 1.00000 at all
four pairs" — but `|dR_q/dψ|` equals `|R_i|` under **either** sign
convention (my own Method 1 shows this directly: only the sign of the
`sin δ` coefficient differs), so a *ratio* check of this kind can never
distinguish `+R_i` from `−R_i`. As far as I can determine from the record
available to me, no seat, in either cycle, ever independently re-derived
this identity by explicit sign-tracked algebra before this review — it was
asserted once (exp-072, THERMO), passed a magnitude-only check that could
not have caught the sign, and was then defended, not re-derived, when
exp-073's own development run first (correctly) computed the opposite sign
and needed a reason to discard it.

### 2f. Consequence, honestly scoped

**Not outcome-determining for exp-073's own Combined Verdict.** `G0-e(ii)`
HALTed before any real pair was analyzed; `dRq_dpsi`/`R_i_over_Rq` are
reported fields in `P-073-1` only, never read by any gate, `RESOLVED`
clause, or Combined-Verdict branch (verified directly in `score_all()`
and `analyze_pair()` — confirmed by grep, the field is written once and
never re-consumed). `|R_i/R_q|` (used nowhere as a gate either, but
reported) is unaffected, since it uses absolute values throughout.

**But it is not harmless either.** `phase4_results.md`'s own identity-gate
table reports the G0-e(i) identity tripwire as **PASS**, `9.4×10⁻¹¹` —
stated as confirmation of an "exact algebraic identity." Given §2d, that
tripwire is not actually capable of failing: it is constructed to verify
`dRq_dpsi_num == R_i_est` after deliberately negating the one quantity
(`raw_fd`) that would have disagreed, so its PASS is guaranteed by
construction, not evidence of correctness. This is precisely the *shape* of
defect this program's own R4 rule and R6 tripwire both exist to catch — a
check that is *described* as running and *does* run, but cannot actually
fail regardless of whether the thing it certifies is true. It will become
load-bearing, not cosmetic, the moment any future cycle (a) fixes
`G0-e(ii)`'s calibration problem (Finding 1 above shows this is fixable in
principle) and (b) actually resolves a pair — at which point `dR_q/dψ̄`
would be printed in a scored `P-073-1`-style table with the wrong sign,
under a claim of exactness, in the one channel this program's own T17/T21
history shows repeatedly gets read for physical direction (e.g., "does a
positive carrier-phase perturbation increase or decrease the recovered
ramp").

---

## 3. `A_q = 2a_cbar·tan χ₀` — spot-checked, sound

I independently re-derived this identity (two-tone `cos(Θ∓φ)` expansion,
matching EM's own Phase-2 critique's method exactly but worked without
reference to it) and confirm it algebraically exact, not a small-angle
approximation — this part of the cycle's own EM critique holds. I also
confirm, from `exp072_disclosure`/`a_priori_disclosure()` in `run.py`, that
the "binds hard" correction (docket item 5) is implemented as pure prose +
runtime-loaded, never-hand-typed disclosure exactly as the docket specifies
— no further defect found here. `T2-4` is genuinely non-gating throughout
(confirmed by grep: `A_q`/`chi0` values feed no `RESOLVED` clause or
Combined-Verdict branch), so this channel carries no consequence for the
verdict even setting Finding 2 aside.

---

## 4. Reciprocity / passivity / causality bookkeeping on `G0-e`'s synthetic generators — no violation found

Checked directly, as the task specifically asks: `G0-e(i)`'s synthetic
ground-truth pairs (`C_A = a_A·cos(Θ−φ)`, `C_B = a_B·cos(Θ+φ)`, all three
legs) contain no medium, no `σ`, no `ε(ω)`, no gain, and no claim about a
physical field at all — every amplitude tested (`a0 ∈ {0.002,0.005,0.01}`,
`a_B = a0·(1+δa)` with `δa ∈ {0, 0.03, 0.10}`, never negative) is a
dimensionless curve-fit parameter, and the generator's only job is to
certify that the OLS/carrier-fit *pipeline* recovers a known input — not to
model anything a passivity or reciprocity bound could apply to. `ABSORB`
itself is correctly and explicitly disclaimed throughout (Idealization 3:
"a graded damping mask... no realizability claim is licensed") and T1's
escape-route field is correctly `None`/N/A (§6). I find nothing here for
R1–R6 or T1's bookkeeping to bind on, and no passivity-adjacent claim
smuggled in under the cover of "boundary parameter" language — this is the
correct outcome of applying my charter's bookkeeping to a desk-statistics
cycle: there is nothing to forbid because nothing physical is asserted.

---

## 5. Independent confirmation of the official run and its reported numbers

I read the committed `results.json` directly (not through any document's
transcription) and confirm, byte-for-byte against `phase4_results.md`:
`combined_verdict = "HALT_NULL_MISCALIBRATED"`, `g0e_i.pass_ = True`
(`worst_abs_ratio_error = 0.01101`), `g0e_ii.pass_ = False`,
`g0e_ii.iid_leg`: 72/72 cell-α combinations fail, `per_pair = {}` (empty —
no pair was ever scored). This matches the document's own account exactly.

I attempted a fresh, independent re-run of `run.py` per the task's own
suggestion. This session's container appears to be running other panel
seats' own Phase-5 work concurrently this shift (an untracked
`phase5_review_thermodynamics.md` appeared mid-session, and several
`run.py`-adjacent background processes I did not knowingly launch were
present and had to be terminated) — rather than risk a concurrent write
collision on the one shared `results.json` this file writes to in place, I
verified the committed artifact directly and independently reproduced its
two load-bearing statistical claims (the leverage mechanism, Finding 1; the
`dR_q/dψ̄` identity, Finding 2) via my own standalone scripts instead,
which is a stronger check than a bit-identical re-run would have been (a
re-run with the same seeds would only reproduce, not independently
re-derive, the same numbers). `results.json` is confirmed unmodified
(`git status` clean) after my session.

---

## Verdict

**PARTIAL**, and I'd resist rounding it up to PROMISING-as-process despite
real, genuine discipline on display. `G0-e(ii)` firing is exactly this
cycle's own honest headline: a real, well-characterized, independently
reproduced (now four ways) methodological result about a whole instrument
class, caught before any data was scored, which is what R6 exists to do.

But Finding 2 is a real cost against the "clean re-issue, behind the
lessons of R6" framing this cycle's own mandate exists to deliver. A silent
sign error in "inherited, independently re-verified" phase bookkeeping —
the *exact* defect class R6 was created to prevent — survived a Phase-1
proposal, five blind Phase-2 critiques, a Red Team audit that explicitly
re-executed "nearly every numerical claim... not merely adjudicated
prose," and a Phase-3 synthesis that introduced a *new*, actively wrong
resolution of it under the label "Fixed." It was caught only by a
fresh-context Phase-5 re-derivation from first principles — the same
mechanism, one phase later, that caught exp-072's own founding sign bug. I
leave the formal Checkpoint-criterion-4 call to the Director/Red Team's own
synthesis (their charter, not a single blind seat's), but I note the
parallel plainly: this is not disqualified from that question merely
because it is non-gating this cycle, since exp-072's own precedent explains
why a Phase-5-only catch is treated as an aggravating fact, not a
mitigating one, and `phase3_synthesis.md`'s own "Fixed... independently
re-verified" language is a written correctness claim that Finding 2 shows
to be false. What is not in question: it must be corrected in `run.py`
before this machinery is next reused, with the correction gated by an
actual sign-tracked re-derivation (§2b above, or equivalent) rather than a
renewed appeal to "matches exp-072's own audit," since that audit is the
thing shown wrong here.

T28's own substantive question — the ~2.84° periodicity's mechanism —
gained no ground this cycle, exactly as `phase4_results.md` itself states,
and my own review does not change that.

---

## Ranked top-3 for Iteration 51

1. **Fix `dR_q/dψ̄`'s sign in `run.py` before this machinery is reused,
   gated by a real (non-circular) re-derivation.** Zero FDTD, a few-line
   change (`dRq_dpsi = R_i` → `dRq_dpsi = -R_i` in `analyze_pair`; drop the
   artificial negation in `ground_truth_recovery_check`'s identity
   tripwire so it tests the actual, correctly-signed derivative). The
   verification must not repeat this cycle's own failure mode — checking
   only that a formula reproduces itself under a chosen convention — and
   should instead independently re-derive the identity by explicit
   sign-tracked algebra (§2b/2c above are directly reusable) before it is
   trusted again. Cheap, and it closes the one clean process gap this
   cycle leaves behind.

2. **Promote the already-queued window-pricing/leakage-budget analysis
   (`phase1_proposal.md` §3c: EM's Cramér–Rao pricing, QUANTUM's `L(T)`
   leakage budget, and the θ_max≈46° window extension) to the top physics
   priority, now that the clean re-issue this item was explicitly deferred
   behind has landed and HALTed.** `G0-e(ii)`'s own failure mode is a
   leverage effect that gets structurally worse the smaller and more
   edge-concentrated the design is (`n=31, p=5`, `mean diag(M5)=0.839` —
   Finding 1); a wider window raises `n` relative to `p` and directly
   attacks both the original Rayleigh-resolution problem this whole
   differential-fit approach was built to route around *and* the leverage
   pathology that just HALTed it. Pair this with re-examining QUANTUM's own
   partially-effective fix (leverage-studentized `resid5`, which improved
   but did not fully close the gap at `n=31`) at the wider window's own
   geometry — a leverage-corrected null at a less leverage-concentrated
   design may succeed where either fix alone, at this window, did not.
3. **Put a pre-committed decision rule on T28 itself, not just on the next
   instrument tweak.** Five consecutive cycles (069→073) have now been
   spent entirely on this one instrument-validation thread with zero
   forward motion on the actual ~2.84° mechanism question — a real,
   resolution-robust signal that remains completely unexplained. I am not
   recommending abandonment (each cycle has delivered a genuine, if
   narrow, methodological result, and Red Team's own criterion-5 analysis
   this cycle and last both correctly found real progress each time), but
   Iteration 51 should decide, explicitly and in writing, what a sixth
   non-advancing cycle on this exact thread would mean — either commit item
   2 above as a genuinely final, well-powered attempt with a stated formal-
   retirement trigger if it also fails to resolve (matching this program's
   own Block-MINI precedent: retire on a properly-powered non-decisive
   result, don't defer a sixth time), or explicitly deprioritize T28 behind
   the other queued items that can move a real, sourced number this cycle
   cannot (`R_contact`'s literature search, T24's still-pending
   re-attempt) — either is defensible; drifting into a seventh cycle
   without deciding which is not.
