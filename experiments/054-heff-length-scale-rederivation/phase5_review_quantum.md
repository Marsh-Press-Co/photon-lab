# exp-054 Phase 5 Review — QUANTUM OPTICS (blind, independent)

Panel Iteration 31. Reviewing the completed cycle: `phase1_proposal.md`,
all five `phase2_critique_*.md`, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `results.json`, plus
`lab/kinetics.py` and `lab/thermo_sidecar.py` directly.

## What this cycle establishes, from this discipline's lens

Nothing here touches a quantum-optics mechanism — correctly so. T1 escape
route "NONE" is accurate: zero σ(I), σ(x,t), dispersive ε(ω), or gain
parameters are introduced or modified; `lab/kinetics.py` is used exactly as
before (bare exogenous `k_f`, `k_r`, piecewise-constant segments). What the
cycle *does* establish, and I independently re-verified rather than took on
faith:

- **The kinetics math is right.** I hand-integrated `r1e-01_5tau`
  (`k_f_on=1.0`, `k_r=10.0`, `tau_k=1/11 s`, `dwell=10/150 s`,
  `dt_gap=5·tau_k`) through five ON/OFF cycles by closed-form
  `relax_exact` and got `n_first≈0.047245`, `n_periodic≈0.047482` —
  matching `results.json::part_b_block_c_rerun::block_c_points.r1e-01_5tau`
  (`n_first_pulse=0.04724497262820006`, `n_periodic=0.0474870906494751`) to
  4-5 significant figures.
- **The `pulse_train_segments` role-inversion is used correctly and
  consistently with exp-045's own precedent.** `run.py:137-139` passes
  `k_f_ambient=k_f_on` (the ON rate) with duration `DWELL_CENTRAL`, and
  `A=0.0`/`T_pulse=dt_gap` for the OFF/relaxation gap — the same inverted
  mapping exp-045/run.py:534-547 discloses in its own comment ("`ambient`
  slot = ON rate...`pulse` slot (A=0.0) = OFF/relaxation gap"). The
  `on_end_idx=[1,3,5,7,9,11]` indexing correctly picks out post-ON-segment
  boundaries in the 12-entry `t_arr`/`n_arr` record for the 11-segment
  train. All 8 Block C points (4 ratios × {5τ,0.5τ}) are present, correctly
  computed, and internally consistent with the `exact_vs_decoupled_ratio`
  values (all in [0.9964,0.9987], all ≤1.0 — P-054-3a's conservativeness
  claim holds as reported).
- **The trust-suite stage 18 gate is a real discriminator**, not a
  tautology: it pins the literal `r_out_m` value into the regression check
  (Red Team's mandatory fix 4, `lab/validation/run_all.py:1586-1609`),
  verified present.
- **Forward-pointers exist** in both exp-043 and exp-045's own `NOTES.md`
  (SUPERSEDED banners dated 2026-08-21, citing exp-054), verified present —
  mandatory fix 7 fulfilled.

## Load-bearing and non-load-bearing defects found

### 1. Mandatory fix 5 (my own Phase-2 finding) is only half-implemented — a propagation gap, not a content error

`NOTES.md:67-72` carries the caveat:

> **NEW (mandatory fix 5, QUANTUM):** the Block-C `n(t)`-independence claim
> (P-054-3) holds only while `k_f`/`k_r` remain exogenous rate-constant grid
> parameters...

The *content* is correct and was accurately re-verified by Red Team
(`phase2_redteam_audit.md` attack 7). But `phase3_synthesis.md`'s own
disposition of the fix states it would be "added to the (renumbered)
`n(t)`-independence prediction and to the idealizations list" (item 5) —
i.e., **two loci**. Checking `NOTES.md`'s actual prediction table
(lines 90-100): P-054-3 was split at Phase 3 into **P-054-3a** (the
exact≤decoupled conservativeness check) and **P-054-3b** (the worst-case
`dT_periodic_decoupled` figure — the direct descendant of the original
`n(t)`-independence rescaling argument). Neither row's "Basis" column
carries the caveat sentence or even a pointer to it. The caveat exists
*only* in the idealizations list, not at the prediction locus Red Team and
the Director both said it would go. This is the same species of
"disclaimer propagation" gap VISION's own mandatory fix 6 was created to
close for the NETD disclaimer (which *is* correctly propagated to every
P-054-2/4/5 row) — mandatory fix 5 did not get the same treatment.
Compounding this: the caveat still cites "(P-054-3)" — a stale ID that no
longer exists as a single row in this same file after the 3a/3b split,
evidence the sentence was carried forward from the Phase-1 draft without
being re-synced to the Phase-3 renumbering.

This is not load-bearing to any *number* in `results.json` — it's a
documentation-completeness gap in a docket item my own seat raised. Cheap
to fix: attach one clause to P-054-3b's Basis column and correct
"P-054-3" → "P-054-3a/3b."

### 2. The caveat's specific code citation is slightly imprecise

`NOTES.md`'s caveat cites `lab/kinetics.py::integrate_two_state`'s
`I_profile=NotImplementedError` boundary as the enforcement point. Verified
directly (`lab/kinetics.py:172-189`): that function exists and does refuse
a time-varying `I_profile`. But Block C never calls `integrate_two_state`
— it calls `kin.pulse_train_segments` + `kin.integrate_segments` directly
(`run.py:137-140`), which accept plain per-segment scalar `k_f`/`k_r` with
no enforcement mechanism of their own (nothing there would stop a future
caller from feeding it already-intensity-derived rate constants). The
underlying claim — nowhere in `lab/kinetics.py` is `k_f` computed *from* a
measured/simulated intensity via a cross-section conversion — is still
correct as a description of the whole module's standing idealization, so
this doesn't change the caveat's substance. But the citation points at a
function that isn't actually in this code path's call stack, which could
mislead a future reader checking "where is this enforced" for Block C
specifically. Minor, non-blocking.

### 3. The un-stated direction of the correction: margins got *smaller*, not larger, relative to the standing headline record

This is the more consequential finding, and it bears directly on the
task's second question (does this instrument-fidelity cycle touch any live
σ(I)/σ(x,t) mechanism thread, even indirectly).

Compare `results.json`'s own reference values:
- ON-endpoint: mixed-chain `dt_ss_full_K` = 3.293076e-5 K (margin **607×**)
  vs. the `w_on`-consistent reference **still cited in the same dict**
  (`w_on_consistent_reference_dt_ss_full_K` = 1.0875e-5 K, margin
  **1839×**).
- Dose-accumulation: mixed-chain exact worst-case margin **≈8,955×**
  (`netd_lo_margin_exact`) vs. the pre-correction headline **27,080×**
  that `phase1_proposal.md:84` itself cites as "current headline" and that
  exp-045's own `results.json` still carries verbatim (only flagged
  SUPERSEDED by exp-054's own forward-pointer, not overwritten).

Both corrections shrink the reported margin by essentially the same factor
(≈3.03×, exactly `dp_dt(w_on)/dp_dt(r_out)`'s inverse — the same ratio
P-054-3b's linear-scaling argument uses). That is: **this cycle's
corrected, presumably-more-physically-licensed numbers report the
candidate as closer to detectable than the numbers currently standing in
the record**, not farther. Nowhere in `NOTES.md`'s prose, `results.json`'s
text keys, or `phase1_proposal.md`'s own framing is this direction stated
plainly — P-054-6's scope statement (mandatory fix 1) carefully
disambiguates from the *unrelated* T8/T13 witness-scale estimate
(`~5.1×→~2.6×`), but never states, in the same forthright terms, that the
new bench-scale numbers are themselves ~3× below the still-standing
`w_on`-consistent headline they supersede. A future cycle skimming for "did
exp-054 make things safer or riskier" would have to notice this by
computing the ratio itself, as I did — it isn't handed to them.

**Does this bear on any live σ(I)/σ(x,t) mechanism candidate looking more
attractive?** No — and the direction of the effect, if anything, argues the
opposite of the task's framing. The margin moved ~3× toward detectable, not
away from it, and even at its new, smaller value (607×/~8,900×) it remains
2-3 orders of magnitude above the 5× floor this program has used as its own
inductive UNDETECTABLE threshold (P-054-5's own basis). I checked
`LOGBOOK.md` for other live threads scored against a margin that could sit
close enough to be moved by a 3× shift (the `graded_black_shell` /
Tier-W "MARGINAL band" thread, e.g. around Iteration 24's C_thr(L) work) —
that thread is scored against a *different* instrument entirely
(Blackwell/Rose photon-shot-noise contrast threshold, not NETD thermal
detectability), so exp-054's correction has no numeric contact with it.
There is currently no σ(I)/σ(x,t) candidate in this program's record whose
live viability sits within 2-3 orders of magnitude of a thermal-NETD
threshold, so this cycle's real, verified ~3× margin shrinkage has no
practical bearing on any current mechanism thread's attractiveness — but a
future cycle should not casually cite exp-054 as having "grown" the
UNDETECTABLE margin, because it did not.

## Ranked candidate next directions (QUANTUM OPTICS lens, Iteration 32+)

1. **Close the propagation gap on my own mandatory fix 5** — one sentence
   at P-054-3b's Basis column (and fix the stale "P-054-3" → "P-054-3a/3b"
   reference), matching the treatment VISION's NETD disclaimer already
   got. Trivial cost, closes a docket item this cycle claimed complete but
   only half-delivered.
2. **The natural next QUANTUM-led proposal this cycle's own logic sets
   up**: re-derive Host D's `k_f` from absorbed intensity `I` (closing the
   `integrate_two_state` `I_profile` idealization for real) — but decide
   the length question *before* writing code, not after. exp-054's own
   argument (`P_abs` stays on the optically-measured `w_on`, never
   `r_out`, because it's an optical/extinction quantity, not a solid-body
   geometric one) is directly informative here: `k_f(I)` is driven by
   absorbed intensity, an optical quantity, so the naive expectation is
   that it should inherit the `w_on`-style convention, not `r_out` — the
   opposite assignment from `h_eff`/mass/area. A future cycle that
   mechanically reuses `r_out` for `k_f(I)`'s intensity normalization
   would be re-importing the exact r_out/w_on chain-mixing bug class this
   whole cycle existed to kill, just relocated into the kinetics rate
   instead of the thermal admittance. State the length choice as a
   pre-registered idealization before any run.
3. **State the margin-shrinkage direction explicitly** as a one-line
   addendum wherever exp-054 is cited going forward (LOGBOOK Iteration 31
   entry is the natural place) — not a code change, a bookkeeping
   correction to prevent a future cycle from citing exp-054 as having
   "confirmed a larger safety margin," which the numbers do not support.
4. **PHOTONICS' queued Q_ext(x) closed-form check** (non-mandatory this
   cycle, deferred to Iteration 32+ per Red Team) also indirectly bears on
   direction 2 above: bounding how much of `w_on`'s excess over `r_out` is
   genuine diffraction vs. an `iso_xsec_sq` convention artifact would
   sharpen whatever future `k_f(I)` re-derivation inherits from `w_on`.
   Not my seat's own charter to run, but worth flagging as a dependency
   for direction 2.

## Verdict

**PARTIAL.**

As pure instrument-fidelity work (T1 "NONE", correctly disposed, no
mechanism claim), the core re-derivation is sound: I independently
verified the kinetics arithmetic, the role-inversion convention, the
exact≤decoupled conservativeness result, and the trust-suite gate's
discriminating power, and found no numeric defect. But my own Phase-2
scope-boundary concern (Red Team's mandatory fix 5) was accepted "in full"
at Phase 3 and then only partially delivered — present in the idealizations
list, absent from the prediction row it was supposed to also reach, with a
stale ID reference as a symptom. And the cycle's own headline framing omits
the single most decision-relevant fact about its own result: the corrected
margins are smaller, not larger, than the record they supersede. Neither
defect threatens the program's phenomenon-level conclusions (both margins
stay 2-3 orders of magnitude clear of the UNDETECTABLE floor, and no live
σ(I)/σ(x,t) thread sits close enough to be moved by this), which is why
this is PARTIAL rather than a program-integrity RULED-OUT finding — but
neither should be waved through as "mandatory fix 5: done."
