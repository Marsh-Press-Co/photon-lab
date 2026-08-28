# PHASE 2 — CRITIQUE · ELECTROMAGNETISM · Panel Iteration 60 · exp-083

**Seat: ELECTROMAGNETISM.** Fresh sub-agent, zero memory of any prior
session. Charter: field/wave behavior, impedance matching, energy coupling —
owns the reciprocity/passivity/causality bookkeeping, formalizing what T1
permits and forbids for each proposal. Read PANEL.md, AGENTS.md, LOGBOOK.md
(RULED OUT R1–R9, ESTABLISHED, LIVE THREADS — T28's complete history through
Iteration 57's own record, plus PLAN.md's Iteration-60 queue text, which
carries the Iteration 58/59 record LOGBOOK.md's own append had not yet
reached at read time), the complete `experiments/083-.../` record
(`phase1_proposal.md`, `NOTES.md`, `run.py`, `results.json`, `run_output.txt`,
`null_permutation_control.json`), and my own predecessor seat's Iteration-59
review (`experiments/082-.../phase5_review_em.md`) — the field-difference
decomposition proposal this cycle claims to have run and corroborated Branch
B with. Blind to all other Phase-2 critiques this cycle.

---

## 1. Independent re-verification — every headline number reproduces

Not taken on faith. Reimplemented from `results.json`'s raw arrays, in a
session-local scratch script, using an independently-coded **vectorized
closed-form OLS projection** over the exact `[1,4]°, n_grid=400` grid
`_free_period_search` uses (different code path than `run.py`'s own loop
form — cross-checked against the real fits first, then trusted on
permutations):

| Claim | Reported | My independent recomputation | Match |
|---|---|---|---|
| Reproduction precondition `max_dev` | `0.0` (31/31 angles) | Recomputed from `per_theta` vs `experiments/076-.../results.json::headline` directly: `0.0` | exact |
| Settling precondition `rel_dev` | `9.812710×10⁻⁵` | `9.812710053540249×10⁻⁵` | exact |
| `delta_scene` free fit | `P*=2.9474°, R²=0.8582` | `P*=2.9473684210526314°, R²=0.858195125110302` | exact |
| `ΔΔE_obj_article_PAD` free fit | `P*=2.5865°, R²=0.4582` | `P*=2.5864661654135337°, R²=0.4582418630801467` | exact |
| `r(delta_scene,delta_empty)` @ n=31 | `r=0.3949, p=0.02806` | `r=0.39494101, p=0.027825` (200,000-trial, independent seed) | exact / matches (MC) |
| `delta_scene` null-permutation (20,000-trial) | mean=0.192, p95=0.335, max=0.632, p=0.0 | 20,000-trial, independent seed/code: mean=0.1923, p95=0.3365, max=0.6024, p=0.0 | matches (MC tolerance) |
| `em_pair` null-permutation | mean=0.190, p95=0.325, max=0.560, p=0.00185 | mean=0.1897, p95=0.3242, max=0.5400, p=0.00195 | matches (MC tolerance) |

**Everything reproduces.** The two preconditions are genuinely sound for
what they are pre-registered to gate — reproduction is harness correctness
on the vacuum leg (bit-exact, not merely `<1e-9`), settling is numerical
convergence at the article-loaded cell it checks (three orders of magnitude
inside the established `STEPS=2800` margin). Neither claims more than that,
and this cycle does not overclaim either.

## 2. The null-permutation control: sound method, real pre-registration gap

The control itself is methodologically clean — my independently-coded
implementation (different algorithm, different RNG seed) reproduces its
summary statistics within Monte Carlo tolerance on both series, and the
observed `R²` values sit outside or at the extreme tail of 20,000 pure-noise
draws either way. **But its own disclosure — "post-hoc due diligence...
not pre-registered" — undersells a real gap against this program's own
standing law.** R5's generalized addendum (Iteration 47) binds *"any future
proposal that searches a named-constant/parameter space of more than a
handful of combinations for a match to a target value MUST include a
pre-registered null-permutation... control before a match counts as
evidence."* `free_period_with_widening` grid-searches 400 candidate periods
and matches the winner against three named target bands — squarely that
shape, and freshly, directly on point: Red Team's own exp-082 audit found
this SAME instrument clears `R²≈0.86` on pure noise ~27% of the time at
n=7, a look-elsewhere finding this cycle's own §3b cites but does not
convert into a pre-registered gate at n=31. §4a's actual pre-registered
band is `R²≥0.30 AND rel_dev≤0.20` only — the null-permutation appears for
the first time in the RESULTS section. The margin here is large enough
(`R²=0.858` beats the null's own *max*, not just its 95th percentile) that
this gap is not outcome-determining this cycle, but the standing rule reads
as violated in substance, not merely in spirit, and Phase 3 should log it
against R5 explicitly rather than accept "disclosed as post-hoc" as
sufficient closure.

## 3. The two-tone question — a real EM reason, and I ran it

**Yes — there is a first-principles reason to expect genuine superposition,
not merely leakage, and it is not speculative: this bench is proven
linear** (`run.py`'s `build_article`/`_run_sim` use only static
`materials.pec_disk`/`graded_black_shell` — no `σ(I)`, no time-varying `ε`,
confirmed by direct inspection, matching my predecessor seat's own
Iteration-59 finding). Under linearity, if the PAD-tied boundary echo
(period `P_continuity=4.611°`, proven lossless, Iteration 53) and an
article-edge diffraction term (period `P_edge_A=2.842°`) are BOTH real,
simultaneously-present physical channels in the same domain — which they
are, by this sub-thread's own established physics — their sum in the field
is not a hypothesis, it is a reciprocity/superposition *fact*. The open
question is only whether the `P_continuity` component's amplitude in
`delta_scene` is large enough to be distinguishable from noise once the
dominant `P_edge_A` component is accounted for.

**I ran the test, zero new FDTD, reusing exactly the committed
`delta_scene` and `em_field_difference_decomposition.delta_delta_e_obj_
article_pad` arrays.** First attempt (full-data reshuffle, comparing
`R²`(two-tone) − `R²`(single-tone) under total permutation of `y`) gave a
misleadingly null result (`p=0.19`) — the wrong null: shuffling the whole
series destroys the real, already-established `P_edge_A` signal too, so the
"noise" baseline is inflated by that lost structure. **The correct test is
this program's own already-established convention** (R6's Iteration-50
addendum names it directly: *"a Freedman–Lane-style sign-flip/
residual-permutation null"*) — fit the reduced (single-tone,
`P_edge_A`-only) model, permute **only its residuals**, add them back to the
reduced model's own fitted values, and refit both models to that surrogate
series. This isolates whether the RESIDUAL after removing the established
dominant tone carries real structure at `P_continuity`, without erasing the
dominant tone itself.

**Result, three independent checks, 100,000–200,000 trials each:**

| Base tone | Series | R²(single)→R²(two-tone) | F(2,26) | Freedman–Lane p | parametric F p |
|---|---|---|---|---|---|
| `P_edge_A` (fixed) | `delta_scene` | 0.845→0.957 | 34.32 | **0/200,000 (p<5×10⁻⁶)** | 5.1×10⁻⁸ |
| reported free `P*=2.947°` | `delta_scene` | 0.858→0.921 | 10.37 | **98/100,000 (p=0.00098)** | — |
| own free `P*=2.586°` | `ΔΔE_obj_article_PAD` (EM's field companion) | 0.458→0.726 | 12.70 | **18/100,000 (p=0.00018)** | — |

Robust to which baseline period is used, and — critically — **corroborated
independently in EM's own linear, reciprocity-clean field-difference
instrument**, not just the nonlinear Weber-contrast series. The recovered
`P_continuity`-tone amplitude sits at 34–77% of the dominant tone's own
amplitude depending on instrument/baseline (largest, 77%, in the linear
field channel my own charter's instrument measures — arguably the more
trustworthy reading, since it isn't filtered through the nonlinear contrast
ratio's shadow-term confound my predecessor's own Phase-5 review named).

**This is a genuine finding, not a restatement of the correlation figure.**
NOTES.md's own honest-discussion caution #3 offers a "data-free leakage
argument" (two moderately-different-frequency sinusoids over a short window
are not fully orthogonal) as a *plausible, charter-neutral* explanation for
`r=0.395`. That argument is no longer the best available account: a
properly null-calibrated nested-model test, using this program's own
established residual-permutation convention, shows the `P_continuity`
component explains significantly more variance than a leakage-only account
predicts, in two structurally independent instruments. **The correlation
tension is not merely "real and unresolved" — it now has a concrete,
quantified, statistically confirmed source: genuine partial admixture of
QUANTUM's mechanism-continuity branch underneath PHOTONICS' dominant
article-edge-diffraction branch**, exactly the possibility Idealization 7
flagged as open and NOTES.md's own "Next" section speculated about.

---

## Steel-man (150 words)

This cycle does exactly what it set out to do, cleanly. Both preconditions
are sound and independently reproduce bit-exact. The pre-registered primary
discriminator resolves decisively (`R²=0.858`, 3.7% from `P_edge_A`,
beating the *maximum* of 20,000 null draws, confirmed by my own
independently-coded reimplementation to the fourth decimal). The bundled
EM companion — proposed by my own predecessor seat last cycle — is run for
the first time, at zero marginal FDTD cost, and independently corroborates
the same branch through a structurally different, linear, reciprocity-clean
channel, itself clearing its own fresh null control. That two differently-
constructed instruments (one nonlinear/Weber-contrast, one linear/
field-difference) converge on the same dominant period family is
materially stronger evidence than either alone, and the write-up discloses
its own correlation tension honestly rather than suppressing it — the
correct instinct, even though (§3, above) the tension turns out to have
more structure than "leakage" credits it with.

## Sharpest attack (150 words)

The "Combined self-score"'s own language — Branch B, "not Branch A... and
not Branch C" — overclaims exclusivity the pre-registered single-dominant-
period discriminator was never built to test. §3's Freedman–Lane
residual-permutation test (this program's own established convention,
R6 Iteration-50 addendum, zero new FDTD) shows the `P_continuity` tone
explains significantly more of `delta_scene`'s variance than a
leakage-only account predicts (`p<0.001`, three independent baselines),
**and independently confirms in EM's own linear field companion**
(`p=0.00018`) — a genuine second mechanism, not noise. The write-up's own
NOTES.md "Next" section treats this as an open, un-investigated
speculation; it is neither open nor merely speculative — it is a cheap,
already-answerable question this cycle's own committed data resolves. Filing
it as "unresolved" when a same-session, zero-FDTD test settles it
undersells the cycle's own evidence and risks the record understating a
real finding, the same shape (an available, cheap, un-run check) R8
generalizes against.

## Verdict: **SUPPORT-WITH-CHANGES**

The primary branch classification (B, article-edge diffraction dominant)
stands — my own independent recomputation confirms it decisively, and
nothing in §3 overturns it as the *dominant* family. But two changes belong
in Phase 3, not deferred to a future cycle: (1) fold in the two-tone
Freedman–Lane result (§3) as a resolved, quantified finding — genuine
partial admixture of the `P_continuity` mechanism at a real, non-trivial
relative amplitude (34–77% of the dominant tone, instrument-dependent) —
correcting NOTES.md's "leakage, not resolved" framing of the correlation
tension; (2) log the null-permutation pre-registration gap (§2) against
R5 explicitly, even though it is not outcome-determining this cycle.

**Single parameter change that would flip this verdict to SUPPORT
outright:** if `phase1_proposal.md` had pre-registered the null-permutation
control as part of §4a's own gating criteria (not merely disclosed post-hoc)
— since every substantive number already clears it with enormous margin,
that single procedural fix removes my one house-discipline objection
without changing any finding.
