# PHASE 5 — REVIEW · ELECTROMAGNETISM · Panel Iteration 59 · exp-082

**Seat: ELECTROMAGNETISM.** Fresh sub-agent, zero memory of any prior
session. Charter: field/wave behavior, impedance matching, energy coupling —
owns the reciprocity/passivity/causality bookkeeping, formalizing what T1
permits and forbids for each proposal. Read PANEL.md, AGENTS.md, LOGBOOK.md
(RULED OUT R1–R9, ESTABLISHED, LIVE THREADS T28's complete Iteration 46–58
history), PLAN.md's Iteration-59 queue, and the complete `experiments/082-.../`
record in the specified order (`phase1_proposal.md`, `NOTES.md`, `run.py`,
`results.json`, `run_output.txt`, `x_wall_realizable_refit.py`/`_results.md`/
`_results.json`, `x_wall_output.txt`, `phase_convention_extension.py`/
`_results.md`/`_results.json`, `phase_convention_output.txt`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`).
Blind to any `phase5_review_*.md`/`phase5_redteam_audit.md` from this cycle.

---

## 1. Independent re-verification of Red Team's Phase-2 statistical findings

Red Team's audit (`phase2_redteam_audit.md` §0d–0k) is this cycle's own
most consequential document — it is what converts the pre-audit
"mechanism reaches the channel" overclaim into the corrected "SURVIVES
stands mechanically; mechanism-identity is unresolvable at this power"
finding Phase 3 adopted. I did not take its prose on faith. I rebuilt each
of its four statistical claims from the raw `delta_scene`/`delta_empty`
arrays in `results.json` myself, in a session-local scratch script, reusing
only the already-committed `_fixed_period_fit`/`_free_period_search`
machinery (`experiments/069-.../run.py`) via direct re-implementation
checked bit-exact against a sanity call, never trusting a copied number.

| Claim | Red Team's figure | My independent recomputation | Match |
|---|---|---|---|
| Pearson r | 0.0306 | `0.03057312042619495` | exact |
| Exact 7!-permutation p-value | 0.953 | `4803/5040 = 0.952976...` | exact |
| Exact critical `\|r\|` at α=0.05, n=7 | 0.746 | `0.7455597751517089` | exact |
| `delta_scene` free period / R² | P*=2.940°, R²=0.858 | `P*=2.9398496...°`, `R²=0.8582517841998007` | exact |
| `delta_empty` (7pt) free period / R² | P*=1.015°, R²=0.864 | `P*=1.0150375939849625°`, `R²=0.863715005946011` | exact |
| Relative divergence between the two periods | 190% (`rel_dev=1.896`) | `1.896296296296296` | exact |
| True 31-point `PAIR_PAD` period (ground truth) | `4.611289746337977°` | Re-ran `free_period_with_widening` on exp-076's own committed 31-point `headline` series (independently reproduced, not copied): `4.611289746337977°`, `R²=0.8165`, `wide[1,15]` stage | exact |
| 7-point miss vs. ground truth | ~78% | `\|4.6113-1.0150\|/4.6113 = 0.77988` | exact |
| Null-permutation, `P(R²≥0.858 \| noise, σ_scene)` | 0.272 | 200,000-trial Monte Carlo, independently coded (vectorized closed-form OLS projection, not the loop form, cross-checked to reproduce the two real-data R² values bit-exact before trusting it): `0.27283` | matches (MC noise) |
| Null-permutation, `P(R²≥0.864 \| noise, σ_empty)` | 0.257 | Same run: `0.25982` | matches (MC noise) |

**All eight numbers independently reproduce.** Six exactly (deterministic
computations); two (the 200,000-trial null-permutation rates) within Monte
Carlo tolerance of Red Team's own figures, using an independently-coded
vectorized estimator I first validated reproduces the two *real* R² values
bit-exact before trusting it on synthetic noise. I found no arithmetic
slip, no cherry-picked window, no undisclosed degree of freedom. Red
Team's Attack 1 is not merely plausible prose — it is a correct, exact
result, and I can now certify that as an independent second computation,
not a re-reading of the first.

One thing worth stating in my own charter's terms, not just confirming
Red Team's: this null-permutation result is not a curiosity about
statistics — it is the same information-theoretic fact reciprocity/
passivity bookkeeping runs into constantly at low SNR. A 3-parameter
sinusoid fit (`c0, a, b`) maximized over a 400-point period grid, applied
to only 7 data points, has enough effective degrees of freedom relative
to the data that "R²≈0.86" is not evidence of anything by itself — this
is the identical look-elsewhere shape R5 was built to catch, now shown to
apply to this program's own free-period machinery at reduced power for
the first time. That generalization (Red Team's own §"flagging for Phase
5" note) is real and, in my view, warrants exactly the standing house note
Red Team proposes: a minimum-window/degrees-of-freedom caution before this
machinery is trusted below ~15-20 points, the same way R5 itself
generalized from one cycle's own finding.

---

## 2. The charter question: are reproduction + settling sufficient EM rigor?

**No — and this is not a criticism of what this cycle did, which is
methodologically clean; it is a statement about what those two
preconditions can and cannot establish, read against what my own charter
actually owns.**

**What the reproduction precondition establishes.** `max_dev=0.0` at all 7
shared angles against `experiments/076-.../results.json::headline` proves
the harness's `with_article=False` code path is byte-identical to a
six-cycle-old committed computation. This is real, valuable, and correctly
gates trust in the *empty* leg. But — as EM's own Phase-2 critique already
flagged, and I independently confirm by direct inspection of `run.py`: the
genuinely new code this cycle adds, `build_article()`, materializing
`obj_x`/`obj_y` as a physical PEC-core + `graded_black_shell` object for
the first time in nine T28 cycles, is exercised by **neither** the
reproduction check **nor any other independent gate**. There is no analog
of the ESTABLISHED absorber invariants (wall reflection ≤0.2%, observer
return = camera floor) verified for this specific embedding at this
specific geometry. The reproduction precondition is a harness-correctness
gate for the vacuum/boundary-only code path; it says nothing about the
article-loaded physics this cycle actually measures.

**What the settling precondition establishes.** Two independent spot
checks — the committed `G40, θ=39°, STEPS 2800 vs 1400` (`rel_dev=9.81×10⁻⁵`)
and my predecessor's own second check, `C40, θ=38°, STEPS 2800 vs 4200`
(`rel_dev=2.84×10⁻⁷`, three orders of magnitude tighter still) — both
confirm the FDTD's own time-domain integration has converged with the
article present, at the geometry's own established step count. This is a
**numerical-convergence** gate: it rules out an unsettled transient
contaminating the primary metric. It is not, and cannot be read as, a
statement about the article's own physical effect on the coherent
round-trip path's *energy content* — settling and energy-flow are
orthogonal questions. A perfectly settled field can still carry a
qualitatively different energy budget than an unsettled one; settling
answers "has the simulation finished," not "what happened physically once
it did."

**Neither precondition touches my own charter's actual question.**
Iteration 53's `PAIR_PAD` losslessness proof (`lab/fdtd2d.py`'s damping
mask is a pure function of `absorb`, zero dependence on `pad`/`nx`/`ny`) is
a fact about the **absorbing boundary's own construction** — a
code-primitive-level, empty-scene-only statement about where reflectance
comes from. It says nothing about the *field amplitude actually reaching
that boundary and returning to the observer window*, once a strongly
absorbing scatterer (the flagship article, whose own ESTABLISHED behavior
extinguishes essentially all incident flux: wall reflection ≤0.2%,
observer return = camera floor, beam-behind 1.5–1.8%) physically occupies
part of that round-trip path. The boundary's own reflectance magnitude is
unchanged by the article's presence — that much genuinely does follow from
the proof, since the article sits inside the domain, not on the boundary.
But whether the *coherent flux reaching the boundary* is still the full,
unperturbed PAD-tied interference pattern, or a partially
absorption-filtered remnant of it, is a genuinely separate, unresolved
question — one about energy flow along a path, which is squarely
reciprocity/passivity/causality bookkeeping, not boundary-construction
bookkeeping. **This is exactly THERMODYNAMICS' own Phase-2 attack, adopted
by Red Team as Attack 3 and merged with the shape-evidence finding into
Phase 3's own Item 4 "mechanism-identity: open" note — and I concur it is
genuinely open, not merely under-checked, and that neither precondition in
this cycle's own record bears on it.**

**So: the reproduction + settling preconditions are sufficient rigor for
what they are pre-registered to gate** (harness correctness on the empty
leg; numerical convergence on the article-loaded leg) **— but they are not,
and were never claimed by Phase 3 to be, sufficient rigor for the
passivity/energy-flow question my own charter would need answered before
"mechanism-identity: open" could become "mechanism-identity: resolved."**
Phase 3's own corrected framing (§4, "Corrected headline framing") gets
this exactly right — it explicitly declines to claim mechanism continuity
and states the question is open. I have no correction to file against
Phase 3; I am formalizing, in my own charter's terms, *why* that
conclusion is the correct one to have drawn, and naming the specific check
that would actually close it (§3, below).

**A qualitative passivity bound, for the record.** No hard numeric bound
is computable post-hoc here (Weber contrast is a nonlinear ratio; the
PAD-tied artifact carries no absorbed-power budget of its own to bound via
Poynting's theorem the way the article's own extinction does — EM's own
Phase-2 critique already stated this correctly, and I concur). But
passivity does license one qualitative check, which the measured result
passes cleanly: since the article is passive (it cannot amplify), the
ratio 0.657 sitting strictly between 0 (clean cancellation) and ~1
(complete survival, physically implausible for a near-total absorber
occupying the shared object window) is *consistent with* passivity — not
positive evidence for any specific mechanism, but not in tension with the
bench's own established physics either. This is a necessary condition the
result satisfies, not a sufficient one for the mechanism-identity
question — worth stating explicitly so a future reader does not read
"passivity-consistent" as "passivity-confirmed-the-mechanism."

---

## 3. What would actually resolve the open question — a concrete, cheap diagnostic

Both blind Phase-2 shape critiques (PHOTONICS, EM) and THERMODYNAMICS
independently converged on "the right next test is more statistical power
at the existing ratio-based instrument" (the full 31-point window). I
agree that is necessary, but from my own charter's angle it is not
sufficient by itself, and there is a genuinely different, EM-native
diagnostic nobody in this cycle's record proposes: **this bench is fully
linear** (confirmed directly: no `σ(I)`, no time-varying `ε` anywhere in
this construction — `run.py`'s own `build_article`/`_run_sim` use only
static `materials.pec_disk`/`graded_black_shell`). Linearity licenses an
**exact** superposition decomposition, not an approximation:

```
E_total(θ) ≡ E_no-article(θ) + ΔE_article(θ)
```

where `ΔE_article(θ)` is *everything* caused by the article's presence,
including all multiply-scattered article↔boundary contributions. Both
`E_total` and `E_no-article` are already computed by this cycle's own
harness (the `with_article=True`/`False` legs) — `run.py`'s own
`one_call()` already returns the raw `amb.observer_profile()` array (a
spatial field profile at the observation plane) for both legs, before it
is ever reduced to the scalar, nonlinear `C` ratio. **A direct,
field-level subtraction `ΔE_article(θ, y) = profile_with(θ,y) −
profile_without(θ,y)`, then applying the sub-thread's own
`free_period_with_widening` machinery to `ΔE_article`'s own period, and
comparing that directly against `delta_empty(θ)`'s shape, is a
reciprocity/passivity-clean, linearity-licensed instrument that never
passes through the nonlinear Weber-contrast ratio `C=(B_obj−B_flank)/
B_flank` at all** — the exact ratio EM's own Phase-2 critique (§2, this
cycle) named as the likely reason `ptp` amplitude "survives" while
point-wise correlation collapses (a large, near-constant "shadow" term
dominates the denominator and can scramble phase while roughly preserving
peak-to-peak span). Isolating `ΔE_article` directly removes that
confound structurally, rather than fighting it with more points at the
same ratio-based instrument. It is cheap: the raw profile arrays already
exist inside `run.py`'s own `results` dict at run time — they are simply
not persisted to `results.json` (only the reduced `C`/`C_empty` scalars
are saved). A future cycle needs only to add one line persisting `prof` per
leg (or re-run the same 28 calls, unchanged) — zero new physics, zero new
`lab/` machinery, and directly answers the passivity/energy-flow question
my own charter owns, rather than only the shape/statistics question the
existing instrument was built to ask.

---

## Verdict

**PARTIAL** — matching this sub-thread's own established convention for
a cycle that delivers genuine, independently-verified narrowing without
touching constraint 3 (T1: N/A throughout, correctly and consistently
stated). This cycle earns real credit on its own terms: it correctly
discharges PLAN.md's six-cycle tripwire, delivers the sub-thread's
first-ever article-loaded FDTD measurement in nine T28 cycles, and — via
Red Team's own audit, which I have now independently reproduced from
primitives at every one of its eight load-bearing numbers — converts a
low-power correlation coefficient into a rigorously demonstrated,
general instrument-limitation finding (this program's own free-period
machinery cannot recover a known-correct period, and achieves
"significant-looking" R² on pure noise roughly a quarter of the time, at
n=7). That is genuine, reusable knowledge beyond this one cycle's own
verdict. But the actual substantive question my charter is asked to
adjudicate — whether the PAD-tied boundary echo's proven-lossless status
survives, in energy content, once a real absorber sits in its round-trip
path — is not resolved by anything in this cycle's record, and could not
have been: neither the reproduction precondition (harness correctness,
vacuum leg only) nor the settling precondition (numerical convergence)
bears on it. Phase 3's own corrected framing states this honestly and
does not overclaim. Not RULED OUT (nothing here forecloses a mechanism
class); not PROMISING in the constraint-3 sense (zero engagement, by
design).

## Top-3 ranked candidate next directions for Iteration 60

1. **The linear field-difference decomposition (§3, new this review) —
   run together with the full 31-point/`PAIR_PAD` window, not as a
   separate follow-up.** Persist the raw `observer_profile` arrays for
   both legs (one-line change to the existing, already-specified harness),
   compute `ΔE_article(θ) = E_with − E_without` directly, and apply the
   sub-thread's own free-period-search machinery to `ΔE_article` and
   `delta_empty` on equal footing. This is the single test that actually
   engages my own charter's passivity/causality bookkeeping directly (a
   reciprocity/superposition-licensed decomposition, not a statistical
   power increase on the existing nonlinear-ratio instrument) and removes,
   rather than out-powers, the shadow-term confound both blind shape
   critiques this cycle independently flagged. Doing it at the same time
   as the (separately near-unanimous) full-width window costs no extra
   FDTD calls beyond what that window already requires.

2. **A cheap, zero-FDTD Poynting/interception energy bound on how much of
   `delta_empty`'s own amplitude the article's own established extinction
   could possibly let survive.** The flagship article's own ESTABLISHED
   cross-section (beam-behind 1.5–1.8%, σ_abs/σ_ext=0.51) already bounds,
   analytically, an upper limit on the coherent flux reaching the boundary
   through the article's own shadow — a THERMODYNAMICS-sidecar-convention
   desk calculation (post-run analytic, zero FDTD, exactly the discipline
   this sub-thread's own Tier-0 items have repeatedly delivered the most
   information per dollar with) would turn "genuinely open" into a
   concrete, falsifiable numeric band before any further FDTD spend, and
   is a natural joint item with THERMODYNAMICS' own charter.

3. **MATERIALS' own near-null σ(I) article follow-up** (already named as a
   standing "Next" item this cycle, Attack 2's own fix) — re-run the
   identical harness with `off_pass` in place of `graded_black_shell`.
   I rank this third from my own charter's vantage specifically because it
   answers a *different* question (article-generality) than items 1–2
   above (mechanism-identity/energy-flow) — both are real, but a weak
   near-null article's own extremely low extinction would make the §3
   field-difference decomposition even more diagnostic there (a smaller
   `ΔE_article` term against the same PAD-tied background), so sequencing
   item 1 first, on the flagship article, actually sharpens what this item
   would show, rather than the two being independent competing priorities.
