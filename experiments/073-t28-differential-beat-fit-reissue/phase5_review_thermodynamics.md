# THERMODYNAMICS — Phase 5 Review · Panel Iteration 50 · exp-073 (T28 corrected differential/beat-fit re-issue)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md: where absorbed energy
goes; owns the per-proposal energy sidecar, analytic and labeled as such).
Blind to all other Phase-5 reviews this cycle. My own Phase-2 critique this
cycle found the `m₀` wrong-resolution defect (adopted by Red Team as Attack
3, docket item 6); this review's first duty is to verify that fix actually
landed, not merely to re-read my own prose. Every load-bearing number below
was cross-checked directly against `results.json`, `run.py`'s source, and
the upstream `experiments/069/071/072` JSON files it reads — not taken from
`phase3_synthesis.md`'s or `phase4_results.md`'s own account of themselves.*

---

## 0. Method

Read the full record in order (Phase 1 → five Phase-2 critiques → Red
Team's Phase-2 audit → Phase 3 → NOTES.md → `run.py` → Phase 4 →
`results.json`), then independently re-derived rather than trusted: the
`m0_native`/`m0_resolved` values against `experiments/071/072`'s own
committed JSON; every function in `run.py` that docket items 6, 4, and 12
touch, read line-by-line against the docket's own text; the full G0-e(ii)
calibration table, re-aggregated per-α and cross-checked cell-by-cell
between the two legs; a paired-cell correlation between the iid and
residual-structure legs; and the `a_priori_disclosure`/`saturating_vs_linear`
outputs against hand recomputation. I attempted three live re-runs of
`run.py` (`python3 experiments/073-.../run.py`, deterministic fixed seeds
throughout — `SEED=20490073`, `SEED_CALIB=20490173`, no randomization
anywhere in `main()`); all three were killed mid-run with no stderr, which
`ps aux` traced to 8–11 concurrent `run.py`/verification processes from
other seats sharing this sandbox during this same Phase-5 window, not to
any defect in the script itself. I did not force a fourth attempt at the
cost of the rest of this review; in its place, every quantity `run.py`
computes was traced by hand through the committed source against the
committed `results.json`, and a residual `run_official.log` artifact
left in the shared scratchpad by the run that produced the committed
`results.json` independently corroborates the reported elapsed time
(128.7s) and Combined Verdict. `git status` on the experiment directory
was clean before and after every attempt; nothing here was modified.

**Verdict on the cycle: PROMISING PROCESS, ONE UNDELIVERED DOCKET PROMISE.**
The re-issue is exactly what it claims to be on its two most scrutinized
points: the `m₀` re-anchor (docket item 6, my own Phase-2 finding) is
implemented correctly and traced to the correct value, and the
Idealization-13 citation fix (docket item 12) is correct. The cycle's
Combined Verdict, `HALT_NULL_MISCALIBRATED`, is the design's safety net
firing exactly as designed and forecast — a real, not a wasted, result. But
the one docket item built specifically to test whether that safety net's
own null construction survives *realistic* (not merely non-Gaussian) noise
— item 4, my own seat's promoted finding via Attack 7 — does not test what
it is presented as testing, and the gap is the exact one Attack 7 named.

---

## 1. Docket item 6 — the `m₀` re-anchor: CORRECT

Verified end to end, not merely spot-checked. `experiments/072-.../
results.json → saturating_vs_linear.linear` gives `slope =
0.002463678368980155`, `r_squared = 0.832803568626572` — I recomputed this
independently from `periods_n_grid3000` and `absorb` in that same file via
an OLS fit and it reproduces to the printed digit. `experiments/073-.../
run.py` line 175 reads exactly this value at runtime
(`m0_resolved = d072["saturating_vs_linear"]["linear"]["slope"]`), never
typing it; `experiments/073-.../results.json` carries it forward unchanged:
`m0_resolved = 0.002463678368980155`, `m0_resolved_r2 = 0.832803568626572`
— matching the task's own target values exactly. `m0_native`
(`0.0025563909774436134`, exp-071's `n_grid=400` slope) is retained
alongside, correctly demoted to "historical/Iteration-48-native anchor"
status in both `NOTES.md` and `run.py`'s own comments, and is never read by
`a_priori_disclosure()`, `injection_recovery()`, or the P-073-4 rate
reference — all three of which I confirmed use `m0_resolved` exclusively
(`run.py` lines 645, 1116, 1174). `saturating_vs_linear()` additionally
re-derives the `n_grid=3000` slope fresh, in-run, from the raw periods, as
a regression check (`matches_exp072_slope`), and it reads `true` in the
committed `results.json` — a second, independent confirmation that the
loaded value and a from-scratch recomputation agree to `<1×10⁻⁹`. This is
the third instance of this exact defect (Iteration 48's raw chord → exp-072
Phase-1 draft → exp-072's own already-corrected disclosure → exp-073's own
first-draft §2c) and it is the first of the three that is fully closed in
the artifact that ships, not merely in a subsequent correction layer. No
gap found.

## 2. Docket item 12 — the Idealization-13 citation fix: CORRECT

`NOTES.md` Idealization 13 now reads "house precedent, **Iteration 2**" and
attributes the correction explicitly to my own Phase-2 critique's
provenance check. I independently re-traced the citation against
LOGBOOK.md directly rather than trusting the correction: the norm
("a deferral must be a stated decision, not an omission") is invoked
verbatim under the label "Iteration-2's own precedent" at LOGBOOK's own
Iteration-3 entry (exp-026 critique, line 2714) and again at Iteration 4's
Phase-5 record (line 3444, "the house norm this program itself set"). The
old citation, "Iteration 5," was — as my own Phase-2 note found — an
instance of the norm being *applied against* a THERMODYNAMICS deferral at
that cycle, not the norm's origin. Correct fix, correctly landed.

## 3. Docket item 4 (Attack 7, my seat's promoted finding) — the "residual-structure" leg does not test residual structure, and empirically reproduces the i.i.d. leg to within noise

This is the substantive finding of this review, and it survived my own
seat's earlier optimism about it: at Phase 2 I flagged the `m₀`-resolution
defect and did not touch G0-e(ii)'s construction; the residual-structure
leg is EM's find (self-flagged, deliberately not sharpened into its
sharpest attack) and Red Team's own promotion (Attack 7: *"the untested
harder case (structured/correlated real FDTD residuals) can only be as bad
or worse"*). `phase4_results.md` reports it as delivered and confirming:
*"the residual-structure leg... fails by comparable or slightly larger
margins at every α, never better."* That framing is true as far as it
goes, but it is not evidence the harder case was actually tested.

**What "residual-structure" means in the docket's own language, vs. what
`build_residual_pool()`/`null_calibration_check()` actually construct.**
EM's original supporting note (`phase2_critique_em.md` §3, carried into
Attack 7 verbatim) names the untested failure mode precisely: *"G0-e(ii)
only calibrates against i.i.d. Gaussian synthetic noise, which cannot
expose miscalibration from the same **structured/correlated** FDTD
residuals... If the real `resid5` carries **θ-correlated structure**,
G0-e(ii)'s own PASS would not detect it."* The word doing the work is
*correlated* — point-to-point dependence across the ordered 31-point θ
grid, the thing a sign-flip/leverage mechanism could plausibly interact
with in a way pure marginal shape cannot.

`build_residual_pool()` (`run.py` lines 679–699) pools the four configs'
own `_fixed_period_fit` residuals (124 values total) into one flat array,
discarding θ-order entirely in the concatenation. `null_calibration_check()`
(lines 904–986) then draws each synthetic dataset as
`y = rng.choice(residual_pool, size=n, replace=True)`, rescaled by a single
scalar `σ/pool_std` — an **i.i.d. bootstrap-with-replacement** draw, exactly
as independent point-to-point as the Gaussian leg it is meant to be harder
than. The function's own docstring calls this *"structured/non-Gaussian
real FDTD residuals, not i.i.d. Gaussian"* (line 683) — silently
substituting *non-Gaussian marginal shape* for *correlated*, the two words
Attack 7 and EM's own note treat as interchangeable but are not. A
bootstrap draw with replacement from a pooled, order-discarded set is
i.i.d. by construction, whatever the shape of the pool's own marginal
distribution. Nothing in this leg can expose θ-correlated structure,
because nothing in its construction can produce any.

**This is not a hypothetical gap — the committed numbers confirm the two
legs are statistically indistinguishable, which is exactly what the
mechanism predicts if my reading is right.** I re-aggregated
`results.json`'s own `g0e_ii` table, paired cell-by-cell across the two
legs (identical `(σ, ψ₀, α)` grid, 72 cells each):

| Nominal α | i.i.d. leg mean rejection | residual-structure leg mean | Δ (leg − iid) |
|---|---|---|---|
| 0.01 | 0.0543 | 0.0566 | +0.0023 |
| 0.05 | 0.1143 | 0.1131 | −0.0012 |
| 0.10 | 0.1709 | 0.1708 | −0.0001 |

Across all 72 paired cells: mean(residual − iid) = **+0.0003** (indistinguishable
from zero against a per-cell Monte-Carlo SD of order 0.02 at `K=500`),
Pearson r between the two legs' cell-by-cell rejection rates = **0.907**.
The mechanism Attack 4 independently derived and re-derived three times
(QUANTUM, Red Team, this run) — `E[Var(R_q^surr)]/Var(R_q^obs) ≈ 0.79`,
driven by `mean diag(M5) = (n−p)/n = 0.8387`, a property of the **design
matrix**, not the noise distribution — predicts exactly this outcome for
any i.i.d. leg regardless of marginal shape. The near-perfect correlation
between the two legs' own failure patterns is not confirmation that the
harder case was tested; it is the signature of both legs being the *same*
case (i.i.d. noise) wearing two different marginal distributions.

**Consequence.** Docket item 4 is marked delivered in `phase3_synthesis.md`
§2 item 4 and treated as closed in `phase4_results.md`'s framing. It is not
closed: the specific failure mode Attack 7 named — θ-correlated real FDTD
residuals defeating a sign-flip null that treats points as independent —
remains completely untested by this cycle's own machinery, one cycle after
being promoted to a docket item specifically to close it. This does not
change the Combined Verdict (`HALT_NULL_MISCALIBRATED` already fires on the
i.i.d. leg alone, decisively, 72/72 cells), so nothing here asks for a
different Phase-4 outcome. But it means the cycle's own claim to have
stress-tested the null construction against "the harder, more realistic
test" (`phase3_synthesis.md` §2 item 4) is not correct as stated, and any
future null-construction fix that clears a `G0-e(ii)`-style gate built this
way still would not have been shown robust to genuine point-to-point
correlation — the exact hazard R6 exists to close before real data is
scored.

## 4. Smaller findings

**4a. `phase3_synthesis.md` does not repeat exp-072's own over-claiming
defect, and that is itself worth recording.** exp-072's own Director wrote
"All 15 docket items are implemented in `run.py`, verbatim to the audit's
specification... ZERO items un-adopted" — verified false on eight counts at
that cycle's own Phase 5, and named as an aggravating factor in that
cycle's Checkpoint-4 firing (LOGBOOK R6 preamble). exp-073's synthesis makes
no equivalent blanket claim; instead it discloses four implementation-level
judgment calls and two self-caught bugs (Ambiguities 1–4) in the open, the
way house discipline asks. That discipline is real and should be named as a
positive, not only audited for gaps — but §3 above shows even careful,
disclosed engineering can still under-deliver on a docket item's own stated
intent without anyone catching it before Phase 5, which is exactly why the
fresh-context blind-review structure exists.

**4b. The energy sidecar is genuinely N/A, and correctly argued, not merely
cited correctly.** Beyond the citation fix (§2), I re-confirm the substance:
a grep of `NOTES.md`, `phase4_results.md`, and `run.py` for
`absorb|thermal|temperature|emissiv|re-radiat|sidecar|watt|kelvin|joule`
returns only the N/A declarations themselves. `C_empty` is a dimensionless
empty-scene field ratio (Idealization 11); `ABSORB` is a numerical
graded-damping boundary parameter, not a lossy medium with a defined loss
tangent (Idealization 3); there is no dissipative volume in this cycle's
scope over which to integrate a Poynting divergence. The chain absorbed
power → ΔT → emission band → detectability has no first link here, exactly
as house precedent (Iteration 2) requires the deferral to state.

**4c. G0-e(i)'s own two self-caught bugs (Ambiguities 3–4,
`phase3_synthesis.md` §3) are correctly disclosed and correctly fixed.** I
re-verified both against `results.json`: the identity-tripwire worst error
is `9.4444...×10⁻¹¹` (five orders of magnitude inside the `1e-6` bar,
matching the disclosed post-fix figure exactly), and the `A_i` tripwire now
has 768 genuinely qualifying cells with 0 failures (docket item 1's
`δa`/`Δψ` axes are live, not dead code — PHOTONICS' Attack-1 gap is
actually closed, unlike item 4). Both self-catches follow the same
discipline exp-072's Director used to find `_amp_phase_at`'s bug
(cross-checking against an independently-verified target before trusting
new code), applied correctly here.

---

## 5. Verdict on this cycle

**Combined Verdict `HALT_NULL_MISCALIBRATED` is correct, reproducible from
the committed artifact, and the right outcome for the design as specified.**
I do not ask that it move. The two items my own charter's prior finding and
the task's own audit target — the `m₀` re-anchor and the Idealization-13
citation — both landed correctly, closing a defect that had recurred three
times on the same quantity. The re-issue's overall discipline (the a/b/c
evidentiary-class taxonomy, the contamination ruling's extension, the
honest disclosure of implementation ambiguities rather than a blanket
verbatim-implementation claim) is real and is this program's best
instance of it to date.

But §3's finding means this cycle has not actually delivered the specific
thing its own docket item 4 promised, and the gap matters for what comes
next: **no null-construction fix proposed for a future cycle can be
considered validated against correlated real-FDTD-residual structure until
a genuinely order-preserving (not pooled-and-reshuffled) synthetic leg is
built and run through a `G0-e(ii)`-style calibration test.** The i.i.d.
Gaussian failure alone is decisive and well-established (three independent
implementations now agree on the leverage mechanism to within Monte-Carlo
noise); the residual-structure question Attack 7 raised is still, after
this cycle, genuinely open.

---

## 6. Ranked top-3 candidate directions for Iteration 51

### 1. Build a genuinely order-preserving residual-structure leg for `G0-e(ii)`, before any further attempt at a corrected null construction.

Zero new FDTD. The fix is narrow and cheap: instead of
`rng.choice(residual_pool, size=n, replace=True)` (i.i.d. by construction),
resample **whole per-config 31-point residual vectors** (4 available, or a
circular-block bootstrap over the pooled 124-point series preserving
θ-adjacency within each block) so a synthetic draw can actually carry
point-to-point correlation. Re-run the calibration sweep on that leg. Two
possible outcomes, both real findings: if correlated residuals make the
sign-flip null's anti-conservatism *worse*, that sharpens Attack 4's
already-established leverage mechanism into a stronger, more general
warning about this instrument class on structured data; if they make it
*better* (plausible — some correlation structures can reduce effective
leverage concentration), that is itself a materially different conclusion
from what this cycle's mislabeled leg suggested, and changes what "fixed"
would need to mean for any successor. Either way, per R6's own text and
this cycle's own item-3(c) precedent, **any future null-construction fix
must clear this corrected leg**, not the current one, before gating real
data — the current leg cannot certify what it was built to certify.

### 2. Price the differential/beat window before spending further on null repair (PLAN.md Iteration-50 queue item 2, zero FDTD).

exp-073's HALT was driven by a property of the `n=31, p=5` design matrix
itself (leverage concentration at the window's edges), not by a
noise-realization accident — independently re-derived three times now. That
raises the window-pricing question's stakes: EM's Cramér–Rao/conditioning
argument and QUANTUM's leakage-function budget can determine, at zero cost,
whether the 36°–42° window can *ever* support a carrier-conditioned
discriminator at achievable SNR, for **any** null construction — not only
the one this cycle tested. If the answer is no, further cycles spent
repairing G0-e(ii)'s null (direction 1 included) are worth doing only as a
generalizable methodological result, not as a path back to scoring T28's
own four pairs in this window; if the answer is yes, direction 1 becomes
the load-bearing next step rather than an optional refinement. This
determines the relative priority of 1 and 3, which is exactly why PLAN.md
already ranked it second, immediately behind the re-issue this cycle
executed.

### 3. G40/`PAD` decorrelation build (PLAN.md item 3, ~31 calls if the geometry-reuse claim verifies).

The cheapest FDTD confound relief on the board, orthogonal to the null-
calibration question (items 1–2 above are both desk-only and can run in
parallel with this). Every T28 deliverable across five consecutive cycles
now carries the `ABSORB`-or-`PAD`-tied caveat; this is the only queued item
that actually relieves it rather than disclosing it again. Readout on the
phase-invariant amplitude channel `√(A_i²+A_q²)/a` — which conditions on no
fitted carrier phase at all — is the more robust choice given both this
cycle's own leverage finding and exp-072's own carrier-instability finding
(Iteration 49 record): a channel that never fits a carrier phase cannot
inherit either problem.

*R5 check: none of the three re-proposes a ruled-out idea or a named R5/R5-
addendum dead end (`A_alt≈3·R_OUT`, `A_eff≈519`, `P`-normalized phase
offset). Direction 1 is a construction fix to an existing pre-registered
gate, not a new parameter search; it does not trigger R5.*

---

## 7. Summary for the Director

- **Docket item 6 (my own Phase-2 finding, the `m₀` re-anchor): CORRECT.**
  `m0_resolved = 0.002463678368980155`, R² = 0.8328, loaded at runtime from
  exp-072's own committed JSON, never typed, used everywhere it should be
  and nowhere `m0_native` should not be. Third recurrence of this defect,
  first fully closed instance.
- **Docket item 12 (Idealization-13 citation): CORRECT.** "Iteration 2"
  verified against LOGBOOK.md directly, not merely against the correction's
  own say-so.
- **Docket item 4 (my seat's promoted Attack-7 finding, the
  residual-structure leg): NOT ACTUALLY DELIVERED.** The leg is an i.i.d.
  bootstrap from a pooled, order-discarded residual set — it changes the
  noise's marginal shape, not its correlation structure — and the committed
  `results.json` shows it is statistically indistinguishable from the
  i.i.d. Gaussian leg it was meant to be a harder companion to (paired-cell
  r = 0.907, mean difference ≈ 0.0003 across 72 cells). The θ-correlated-
  residual failure mode Attack 7 named is untested by this cycle, one cycle
  after being promoted specifically to close it.
- **Energy sidecar**: genuinely N/A, correctly argued at both the citation
  and substance level, no smuggled thermal claim anywhere.
- **Combined Verdict `HALT_NULL_MISCALIBRATED` stands** — correct,
  reproducible, and a real result (the leverage mechanism is independently
  confirmed three times over). Nothing in this review asks for it to move.
- **What changes going forward**: any successor null-construction fix must
  clear a corrected, genuinely order-preserving residual-structure
  calibration leg — not the one this cycle shipped — before it can be
  trusted per R6's own standard.
