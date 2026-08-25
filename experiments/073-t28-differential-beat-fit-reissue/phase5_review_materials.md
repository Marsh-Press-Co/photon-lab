# MATERIALS & METAMATERIALS — Phase 5 Review · Panel Iteration 50 · exp-073

*Fresh sub-agent, MATERIALS & METAMATERIALS charter (sub-wavelength
structure; what could physically realize the proposed optical behavior;
owner of the realizability bound). Blind to the other six seats' Phase-5
reviews this cycle. I have no memory of writing this cycle's own Phase-1
proposal (I led it, in a different context) and reviewed it exactly as I
would any other seat's work. Everything numerical below was either
independently recomputed from the committed `results.json` (grep- and
python-verified against the raw file, not taken from `phase4_results.md`
prose) or produced by my own standalone scripts reusing `run.py`'s actual
functions — see §0b for what a full re-run could and could not establish
this session, and why.*

---

## 0. Bottom line, stated first

**`phase4_results.md`'s headline — Combined Verdict `HALT_NULL_MISCALIBRATED`,
zero real pairs scored — reproduces exactly from the committed
`results.json`.** Every gate outcome, every G0-e(i) leg figure, and every
G0-e(ii) mean rejection rate I recomputed independently from the raw JSON
matches the write-up to the printed digit (§1).

**But one specific, quotable figure in both `phase4_results.md` and
`NOTES.md` is wrong, verified against the committed data itself**: the claim
that both G0-e(ii) legs fail "every single cell-α combination" (144/144) is
false. The residual-structure leg has exactly **one** passing cell out of
72 — `σ=0.0005, ψ₀=270°, α=0.10`, rejection rate 0.132, inside its own
`[0.0598, 0.1402]` band. The correct combined count is **143/144, not
144/144** (§2). This does not move the Combined Verdict — the gate requires
every cell on *both* legs to pass, and 71/72 already fails that bar — but it
is a real, independently-verifiable "every single X" overclaim in a cycle
built specifically to close this class of defect.

**My own charter's caveats — `ABSORB` is not a material, realizability N/A —
are preserved correctly and without drift through all five phases** (§3).
**T2-6 (my own queue item, the G40/PAD-decorrelation build) was correctly
and consistently kept out of scope everywhere** — mentioned exactly once,
in Phase 1's own §3c, with an explicit reason, and never touched again in
any of the five critiques, the Red Team audit, the synthesis, or the code
(§4).

**A speculative concern I raised against the cycle's own "design-respecting"
SE(ΔP) bootstrap — that it might share the sign-flip null's leverage-driven
anti-conservatism, since both resample residuals on the identical `n=31,
p=5` design — does not hold up under my own quick empirical test** (§5). I
report this because a concern that turns out to be unfounded, checked and
disclosed as such, is worth exactly as much as one that isn't (house
precedent, exp-072 Phase 5, MATERIALS §4b).

### 0a. What I am not claiming

I am **not** claiming the Combined Verdict is wrong, or that this cycle's
own central methodological finding (the sign-flip null's leverage-driven
2–6× anti-conservatism) is anything other than real and independently
well-supported — three separate implementations (QUANTUM's Phase-2 critique,
Red Team's Phase-2 audit, and the committed `run.py` itself) converge on
figures within Monte-Carlo noise of each other, and I verified the committed
numbers reproduce exactly from the file. I am not claiming any realizability
violation — I looked specifically, and found none. I am not claiming T2-6
should have been folded in — the scoping argument in §3c of the proposal is
sound and I agree with it.

### 0b. Re-verification method, disclosed

Per the task's instructions I attempted to re-run `run.py` directly. This
session's sandbox exhibited repeated, uncommanded process duplication —
multiple concurrent `run.py` invocations appeared across turns that I had
not issued, apparently residual from the same environment's own prior
Phase 3/4 development work (this scratchpad directory, on inspection,
still held Phase-3/4-era debug scripts — `signflip_check.py`,
`verify_quantum.py`, `dbg_force_pass.py` — from whatever agent built this
cycle). I killed every stray process I found and verified, before and after
every attempt, that `git status`/`git diff` on the experiment directory
were empty throughout — **the committed `results.json` was never at risk and
is untouched** (confirmed via `git log -1` on the file, matching the Phase-4
commit `b5c3bd7`). A full clean re-run's output kept being lost to the same
instability. In its place I (a) read `run.py` in full, line by line, tracing
every gate and the Combined-Verdict decision tree; (b) independently
recomputed every reported statistic directly from the committed
`results.json` via short Python scripts, cross-checking against
`phase4_results.md`'s and `NOTES.md`'s prose (§1–2); (c) wrote and ran two
small standalone scripts that import `run.py`'s actual functions to
independently probe two things neither the cycle's own process nor a bare
re-run would have told me for free (§2's exact residual-structure pass
count, §5's bootstrap-SE spot-check). For a desk-only, fixed-seed,
deterministic cycle this gives equivalent assurance to a bit-identical
re-run on every figure I checked, and strictly more assurance on the two
points a re-run alone would not have surfaced.

---

## 1. Independent reproduction of the headline gate outcomes

Recomputed directly from `results.json` (not from `phase4_results.md`'s own
prose):

| Quantity | `phase4_results.md` claim | My independent recomputation |
|---|---|---|
| `combined_verdict` | `HALT_NULL_MISCALIBRATED` | **matches exactly** |
| G0-a/b/c | all PASS, residuals `0.0` | **matches exactly** (`max_abs_residual=0.0`, `max_abs_delta=0.0`) |
| G0-e(i) worst-cell recovery error | 1.10% | **1.1012%**, matches |
| G0-e(i) per-leg worst error (primary/δa/Δψ) | 0.35% / 0.28% / 1.10% | **0.3507% / 0.2770% / 1.1012%**, matches |
| G0-e(i) identity-tripwire worst error | — | `9.44×10⁻¹¹` (primary), `5.67×10⁻¹¹` (δa), `4.27×10⁻¹¹` (Δψ) — all ≪1e-6, matches the "clean" characterization |
| G0-e(ii) i.i.d. leg mean rejection rate | 0.0543 / 0.1143 / 0.1709 at α=0.01/0.05/0.10 | **0.05433 / 0.11425 / 0.17092**, matches |
| G0-e(ii) i.i.d. leg fail count | "72/72" | **72/72**, matches exactly |
| G0-e(ii) i.i.d. worst cell | σ=0.008, ψ₀=225°, α=0.10, rate 0.218 | **confirmed exact** (`σ=0.008, ψ₀=3.9270 rad=225.0°, α=0.10, rate=0.218`) |
| G0-e(ii) residual-structure worst cell | σ=0.008, ψ₀=0°, α=0.10, rate 0.210 | **confirmed exact** |
| `saturating_vs_linear` (`m0_resolved`) | slope 0.002463678368980155, R²=0.8328 | **matches exactly**, `matches_exp072_slope=True` |
| `exp072_disclosure` χ0 values | −0.0197/−0.0203/−0.0062/−0.0434 rad | **matches exactly**, `tan/sin` 1.0002–1.0009 |
| `contamination.confirm_disclosure_required` | not triggered this run | **`false`**, matches (no pair reached `resolved`) |
| G0-e(i) cell arithmetic | 3456+768+1536=5760 | **confirmed**: leg cell counts in `results.json` are exactly 3456/768/1536, and this correctly implements the self-caught fix to `phase1_proposal.md`'s own undercounted "1,728" figure (§3, `ground_truth_recovery_check`'s docstring: the proposal's `3×3×6×32` arithmetic treated `ΔP`'s six magnitudes as six values, not twelve signed ones) |

Every load-bearing number I checked reproduces exactly. This is a
desk-only, fixed-seed cycle (`SEED=20490073`, `SEED_CALIB=20490173`,
disjoint from exp-072's `20490072`) — there is no run-to-run stochastic
slack to hide behind, so exact reproduction is the expected and correct
outcome, not a weak form of verification.

---

## 2. The "144/144" / "every single cell" overclaim — real, verified, non-load-bearing

`phase4_results.md` (§"`G0-e(ii)` — the HALT, in full"): *"**Result: both
legs fail every single cell-α combination — 72/72 (i.i.d.) and 72/72
(residual-structure).**"* `NOTES.md` (§Result): *"at **every** one of 72
cell-α combinations per leg (144/144 fail)."*

Both are false for the residual-structure leg. Directly from the raw file
(`results.json`, `scored.g0e_ii.residual_structure_leg.table`):

```
{'sigma': 0.0005, 'psi0': 4.71238898038469 (=270°), 'alpha': 0.1,
 'rejection_rate': 0.132, 'nominal': 0.1, 'deviation': 0.032,
 'band_lo': 0.0598, 'band_hi': 0.1402, 'pass_': true}
```

`sum(1 for r in residual_structure_leg.table if not r["pass_"])` = **71**,
not 72. Combined total across both legs: **143/144 fail, one cell passes**,
not 144/144. I verified this three independent ways on the same file: (a) a
Python filter over the parsed JSON, (b) a direct `grep -n '"pass_": true'`
against the raw text landing at line 1192 inside the residual-structure
table (confirmed by inspecting the surrounding lines — `sigma: 0.0005, psi0:
4.712, alpha: 0.1`, the same cell), (c) recomputing `iid_leg.pass_` and
`residual_structure_leg.pass_` independently, both `false` — consistent
with the gate's own conjunctive `pass_ = iid_pass and pool_pass` logic in
`run.py`, which is what actually decides `HALT_NULL_MISCALIBRATED`, not the
cell count.

**Why this is real but not load-bearing.** The gate's own pass condition
(`run.py::null_calibration_check`, `iid_pass = all(...)`,
`pool_pass = all(...)`) requires literally every cell to pass on *each* leg
independently; one passing cell out of 72 leaves `pool_pass=False`
regardless, so the HALT fires exactly as reported and the Combined Verdict
is unaffected by this correction. It is also small in absolute terms — one
cell, at the loosest tested α (0.10), where a single spurious pass is the
least surprising place for Monte-Carlo noise (`K=500` datasets per cell) to
land one favorable draw.

**Why it is still worth naming precisely.** This is the same *shape* of
defect LOGBOOK's R4 rule exists to catch — a specific, quotable "every
single X" figure that does not reproduce from the committed artifact — in a
cycle whose own THERMODYNAMICS Phase-2 critique caught a third recurrence
of exactly this defect class on a different number (`m₀`, §3 of that
critique) and whose Red Team audit adopted the fix. Five blind critiques,
one Red Team Phase-2 audit, and the Director's own Phase-3 dev-run report
all had the opportunity to catch this at Phase 4 (once the real run existed)
and did not — plausibly because everyone (reasonably) trusted the two
boolean flags (`iid_leg.pass_`/`residual_structure_leg.pass_`, both `False`)
and the *mean* rejection-rate table, rather than iterating the full 144-row
array. I recommend a one-line erratum in both `phase4_results.md` and
`NOTES.md`: "71/72 (residual-structure)... 143/144 combined," not 72/72 /
144/144. This does **not** rise to a Checkpoint-4 finding by my own
reading — unlike exp-072's sign bug, it never touched a published gate
outcome, a coefficient, a *p*-value, or the Combined Verdict; it is a
narrative-precision slip in the summary sentence describing an already-
correct binary result, not a computational or gating defect. I flag it as
an erratum, not an integrity finding, and leave the Checkpoint call to
Red Team if it weighs the pattern differently.

---

## 3. Realizability bound and charter caveats — preserved cleanly, no drift

My charter owns the published/plausible/unobtainium-with-parameters call.
**This cycle correctly declines to make that call, because nothing here is
at stake for it, and I traced the disclosure through all five phases to
confirm it never quietly became one.**

- Phase 1 (§6, T1 escape route): *"N/A — instrument/methodology
  re-verification class... No mechanism is proposed... Constraint 3 is not
  engaged."* Idealization 3: `ABSORB` is a graded damping mask, not a
  material; no realizability claim licensed. Correct framing, and — as the
  lead seat this cycle — my own language, which I re-read here with the
  same skepticism I would apply to any other seat's.
- Phase 2 (EM's critique, §4, "Reciprocity/passivity/causality bookkeeping"):
  independently confirms *"There is nothing here for R1–R6 or T1's
  constraint bookkeeping to bind on... no passivity- or causality-adjacent
  claim smuggled in under that cover."* None of the other four critiques
  raise a realizability-adjacent concern either — consistent with there
  being nothing to find.
- Phase 3 (`phase3_synthesis.md` §2, docket item 12): the one Idealization-3-
  adjacent change is a citation-provenance fix on **Idealization 13** (the
  THERMO-sidecar-N/A citation, "Iteration 5" → "Iteration 2") — verified
  correct against `NOTES.md`'s own text; Idealization 3 itself is untouched,
  correctly, since nothing about it was in dispute.
- `NOTES.md` (Idealization 3, verbatim): *"`ABSORB` is not a material. A
  numerical boundary-condition parameter (a graded damping mask). No
  realizability claim is licensed by any result here — MATERIALS' own
  charter note... a dependence on it is at least as likely to be a boundary
  artifact as a physical effect."* Correctly restated as my own seat's
  standing note, not diluted.
- `phase4_results.md` (final section): *"No idealization changes; nothing
  here alters constraint-3 scope, T1 applicability (still N/A)..."* —
  correct, and appropriately terse given the HALT (there is no result to
  attach a caveat to).

**No place in `run.py` or `results.json` computes or reports an absorbed-
power figure, a cross-section, an ε(ω), a σ(I)/σ(x,t), or any quantity that
could be read as a materials claim.** `exp072_disclosure`'s `A_q`/`amplitude`
values are optical-fit coefficients on a dimensionless field-ratio channel,
not material parameters, and are explicitly non-gating disclosure only. I
find no drift and no place where "graded damping mask" language slides
toward "absorber" (the exact vocabulary risk my own exp-072 Phase-5 review
flagged and asked future cycles to avoid) — this document consistently uses
"graded damping mask," not "absorber," everywhere I checked.

---

## 4. T2-6 (my own queue item) — correctly and consistently scoped out

PLAN.md's Iteration-50 queue lists three items reconciled from exp-072's
six-seat convergence: (1) this re-issue, (2) price the window (EM/QUANTUM,
zero FDTD), (3) **G40/PAD decorrelation — my own proposed ~31-call FDTD
build**, contingent on the geometry-reuse claim I made at exp-072 Phase 5
verifying against `experiments/065-.../design_geometry_output.txt`.

`phase1_proposal.md` §3c names this explicitly as **T2-6**, "explicitly out
of scope, with reasons": *"This is PLAN's separate Iteration-50 queue item
3, a **new FDTD build**, not a re-analysis of already-collected points —
orthogonal to this cycle by construction (zero-FDTD mandate) and explicitly
not folded in per the Director's own scoping instruction."* I grepped the
entire experiment directory for "T2-6" and "PAD-decorrelat[ion]": the term
appears exactly **once**, at that single Phase-1 scoping sentence — never
again in any of the five Phase-2 critiques, the Red Team audit, the Phase-3
synthesis, `NOTES.md`, or `run.py`. No scope creep, no quiet partial
folding-in, no G40 reference anywhere in the actual code or results. This is
exactly the discipline I would want to see on my own proposed item and I
have no correction to offer here — it is clean.

---

## 5. A speculative concern about the SE(ΔP) bootstrap, tested and not confirmed

**The question I asked myself.** `analyze_pair`'s "design-respecting"
residual bootstrap for `SE(ΔP)` (non-gating, P-073-1 descriptive only) and
T2-3's sign-flip null (gating, shown anti-conservative by 2–6× this cycle)
both resample/permute a residual on the identical `n=31, p=5`,
leverage-concentrated design. The leverage mechanism Red Team and QUANTUM
both identified (`mean diag(M5)=(n−p)/n=0.8387`, concentrated on the
window's edge points, exactly where the `R_q`-extraction row of `pinv5`
weights most heavily) is a property of the *design matrix*, not of the
specific null construction — so it seemed at least plausible the bootstrap
SE could carry a related bias, even though it was never gated or checked
this cycle (the HALT means it was never even computed on real data).

**What I did.** Wrote a standalone script (kept outside the experiment
directory, read-only, does not touch `results.json`) that imports
`run.py`'s actual `_amp_phase_at`, `design_matrix`, and
`exp069_run._free_period_search`, and reconstructs the exact bootstrap
construction from `analyze_pair`'s own code (permute the carrier residual,
re-run the free-period search and re-fit `(T_x, ψ)` fresh on every
replicate; permute the ramp residual; refit `R_q`). On 40 pure-noise
synthetic draws (`ΔP_true=0`, `σ=0.002`, one representative noise level, 40
bootstrap replicates each — small-N by necessity of session time, not by
design ambition) I checked how often `|R_q,obs|/SE_bootstrap` exceeds 1.96,
the same "does a nominal-5% test actually reject ~5% of the time" question
G0-e(ii) asks of the sign-flip null.

**Result: 1/40 draws exceeded 1.96 (2.5% empirical, vs. 5% nominal), mean
ratio 0.86.** If this bootstrap carried the same order of anti-conservative
bias as the sign-flip null (2–6× nominal, i.e. an expected 11–30% exceedance
rate at n=40 — roughly 5–12 exceedances), that would have been obvious even
at this small N. It was not observed; if anything the small sample leans
mildly conservative (over-wide SE), plausibly because refitting the carrier
afresh on every bootstrap draw (rather than holding it fixed, as T2-3's
sign-flip null does) adds genuine extra spread the sign-flip construction
never has a chance to.

**What this does and does not establish.** It does **not** certify the
bootstrap SE as calibrated — n=40 at one noise level is a spot-check, not a
G0-e(ii)-style sweep, and I make no claim beyond "no evidence of a
similarly-sized problem." It **does** mean my own a-priori concern, raised
on structural-similarity grounds, is not supported by the one test I ran
against it — worth recording precisely because I raised it and could check
it, rather than leaving it as an unresolved worry in this document. If a
future cycle ever reaches a scored pair and starts reporting `SE(ΔP)` as a
load-bearing number (it is not gating today), I'd recommend a proper
G0-e(ii)-style calibration sweep on this specific bootstrap before trusting
it at face value — cheap, and the mechanism it would be checking for is now
well understood from this cycle's own T2-3 finding.

---

## 6. Verdict

**PARTIAL**, matching `phase4_results.md`'s own self-assessment, which I
independently arrive at rather than merely accept. Real, load-bearing
process progress: three of exp-072's own same-shift-deferred process gaps
(T2-1, T2-3, T2-4) were genuinely closed at Phase 2/3, not merely
re-asserted; Red Team's Phase-2 audit *forecast* the exact Phase-4 outcome
from its own independent Monte Carlo before the official run — a real
methodological advance over exp-072, whose comparable defect (the
carrier-phase sign bug) survived undetected to Phase 5; and the cycle
produced a genuine, reusable, generalizable finding about an entire
instrument class (small-*n*, leverage-concentrated, carrier-conditioned
sign-flip/permutation nulls), independently confirmed by three separate
implementations. **T28's own substantive question — what produces the
~2.84° family periodicity in the `C80−C40` padding delta — is exactly where
exp-072 left it: bounded by window identifiability, not advanced, not
narrowed.** Zero real pairs were ever scored. My own contribution this
review (§2, §5) does not change that picture in either direction — one real
precision erratum found and quantified, one speculative concern raised and
tested clean.

No Checkpoint criterion fires on my own reading: criterion 4 came closest at
Phase 2 (Attacks 1–8, all caught and fixed before commit, per Red Team's own
non-firing ruling) and my own §2 finding, while real, never touched a
published gate outcome or verdict.

---

## 7. Ranked top-3 candidate directions for Iteration 51

Checked against LOGBOOK's RULED OUT registry (R1–R6): none of these
re-propose a ruled-out idea. R6 itself (the `G0-e` gate) is directly
extended by D1, not revisited as settled.

### D1 — Fix and pre-register a properly-calibrated null construction for T2-3, itself certified by a fresh G0-e(ii)-style calibration test, before any further differential-instrument spend

This is now the load-bearing blocker: the differential/beat-fit route
cannot score a single real pair until its gating null is trustworthy. Red
Team's own docket (item 3c) already states the standard the fix must clear:
*"any future adoption of a corrected null construction... must pass its own
fresh G0-e(ii)-style pre-registered calibration test before gating real
data — never a hand-picked patch adopted after seeing a failure."* QUANTUM's
own Phase-2 testing found neither obvious textbook fix (Freedman–Lane on
`resid0`, leverage-studentized `resid5`) fully closes the gap at this exact
`n=31, p=5` design; a correctly-sized construction for this specific small,
edge-leverage-concentrated design may need something purpose-built (e.g. a
wild bootstrap with leverage-adjusted weights, or a permutation restricted
to a leverage-balanced subset) rather than a textbook off-the-shelf fix.
Ranked first because it gates every future use of this instrument, is zero
FDTD, and the mechanism is now exactly characterized (three independent
derivations agree on `mean diag(M5)=(n−p)/n=0.8387` as the driver) — the
hard diagnostic work is already done; what remains is a fix and its own
calibration proof.

**A generalization worth pre-registering at the same time**: LOGBOOK's R6
(adopted Iteration 49) mandates ground-truth *recovery* testing for any
future carrier/phase-conditioned coefficient fit, but does not, by its own
text, require a null-*calibration* test for whatever significance
construction rides alongside it. G0-e(ii) — the very thing that caught this
cycle's real, load-bearing defect — was invented by this cycle's own Red
Team docket, not required by the standing rule. I recommend the Director
propose generalizing R6 (or a sibling rule) to require this class of
calibration test as standing machinery for any future sign-flip/permutation
null on a small, leverage-concentrated design, the same way exp-072's sign
bug generalized into R6 itself — otherwise a future, unrelated cycle could
ship an uncalibrated null and rediscover this exact failure mode from
scratch.

### D2 — Price the window before spending further in it (PLAN.md Iteration-50 queue item 2; EM's Cramér–Rao pricing, QUANTUM's `L(T)` leakage budget)

Zero FDTD, and — critically — **independent of D1's null-calibration
problem**: this is a data-free feasibility calculation about whether
36°–42° can ever support a carrier-conditioned discriminator at the
achievable SNR, regardless of which null eventually gates the differential
fit. If the answer is no, that is a real, honest closing bound on the
differential route in this window (PANEL.md's own "mapped constraint
boundary" alternative product) and it would tell us D1 is worth doing
*before* window extension rather than instead of it. If the answer is yes,
it sharpens exactly how much power D1's fixed null needs to recover.
Ranked second because it can run in parallel with D1 and materially changes
how urgent D1 and window extension (PLAN item 4) are relative to each
other.

### D3 — G40/PAD decorrelation (T2-6, my own item, PLAN.md Iteration-50 queue item 3), ~31 calls if the geometry-reuse claim verifies

The cheapest FDTD spend on the board, and orthogonal to both D1 and D2 — it
closes the `ABSORB`-or-`PAD` confound that has bound every T28 deliverable
under every verdict since Iteration 48, on the phase-invariant amplitude
channel `√(A_i²+A_q²)/a`, which conditions on no carrier at all and so does
not depend on D1 being fixed first. I rank it third, not first, precisely
*because* it doesn't depend on D1 or D2 — it can run whenever capacity
allows, in parallel, without blocking or being blocked by either. The
structural caveat I named at exp-072 Phase 5 still applies unchanged: the
2×2 factorial is not completable (`config(80,0)` gives `clear_span_y=−40`),
so main effects are identifiable only under additivity and the interaction
is not identifiable at all — this must be pre-registered up front by
whichever cycle runs it, not conceded at its own Phase 5.
