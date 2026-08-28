# PHASE 5 — REVIEW · QUANTUM OPTICS (blind, fresh) · Panel Iteration 61 · exp-084

*Seat charter: non-classical absorption, state-dependent/coherent interactions;
in practice on this panel, house statistician for T28's period-fitting/
null-control machinery. This is a genuinely fresh instance — no memory of
any prior-cycle critique, including my own Phase-2 pass this same cycle.*

## 1. Verdict: **PARTIAL**

Leg (a): **INCONCLUSIVE** on the period-match (does not clear a null-under-
noise test), with a real, independently-surviving **positive shape-
correlation finding** that I re-checked with a test nobody had run on it
yet (§2.3) and which comes out *stronger*, not weaker. Leg (b): **NO
VERDICT** (instrument-validation failure, correctly self-caught). I concur
with the Combined Verdict already on record — this is not a rubber stamp;
I rebuilt the decisive number from two independent angles before agreeing
with it (§2.1–§2.2).

## 2. What I independently re-verified, with numbers

### 2.1 Bit-exact reproduction of the production circular-shift null

I wrote my own script (not copied from `phase3_fix_docket_checks.py` or
`phase2_redteam_audit.md`) that imports the actual committed
`free_period_with_widening` (from `experiments/078-.../y_wall_prescreen.py`)
and runs it on the raw `leg_a.curve` array read directly from
`derivation_results.json`. Result, run from scratch by me:

```
Observed: P*=2.533835 deg  R^2=0.369656  window=narrow[1,4]
30 circular shifts -> n_meet_or_exceed = 15/30 = 50.0%
null distribution: mean=0.4594  max=0.7302  min=0.2892
```

This is bit-exact against Red Team's and the Director's own figures. **This
is now the fourth independent reproduction of 15/30=50.0%** (after Phase 1's
implicit setup that never ran this test, QUANTUM's own Phase-2 critique at
the narrower fixed-window reading of 14/30=46.7%, Red Team's Phase-2 audit
on the full pipeline, and the Director's Phase-3 script) — and mine is the
fifth party to touch this number, all agreeing.

### 2.2 A second, fully independent statistical instrument (different code, different fit convention)

To satisfy the "without reading anyone else's null-test code" instruction
properly, I also built a free-standing sinusoid-regression instrument from
first principles — no import of `_free_period_search`, `_fixed_period_fit`,
or `free_period_with_widening` at all: ordinary least-squares fit of
`c(θ) = a + b·cos(2πθ/P) + c·sin(2πθ/P)` directly in θ-space, dense grid
search over P with the same staged-widening logic ([1,4]→[1,15]→[1,60]°),
applied to the identical raw curve.

```
My own OLS-in-theta fit:  P*=2.5116 deg  R^2=0.3358  (vs production's 2.5338/0.3697)
My own circular-shift null: n_meet_or_exceed = 17/30 = 56.7%
```

The exact numbers differ slightly from production because the production
pipeline (`_free_period_search`) fits in **sin θ space**, referenced to
cos(39°) at the window center — a physically-motivated grating-type
convention — while mine fits directly in θ; over this narrow 6° window the
two nearly coincide, which is why the numbers are close but not identical.
**The substantive conclusion is unchanged, and if anything reads slightly
more damaging under my independent instrument** (56.7% vs 50.0% — the
observed fit is, if anything, less distinguishable from its own null under
a second, differently-coded method). Two structurally different fitting
conventions, two independently written pieces of code, the same verdict:
`R²=0.37` for leg (a) is unremarkable relative to the curve's own smoothness.

### 2.3 A check nobody had run yet: circular-shift null on the shape-correlation claim itself

The surviving positive finding is `corr(leg_a_curve, real C80(θ)) = 0.958`,
checked in the record only against three unrelated control curves (leg (b)'s
own output, a linear ramp, a quadratic). It had never been put through the
program's own circular-shift discipline. I ran it:

```
observed r = 0.958186
30 circular shifts of leg_a vs the FIXED real C80(theta):
  mean=-0.032  max=0.9629 (at shift=+1, i.e. +0.2 deg)  min=-0.6806
  n_shifts with |r| >= |r_obs| = 1/30 = 3.3%
```

**This is a genuinely sharper, more specific result than the period-match
question** (3.3% vs. 50.0%) — the shape correlation sits at roughly the
96.7th percentile of its own null distribution, not the median. This is
real, independent support for treating the shape correlation as the
cycle's honest positive finding, exactly as Phase 3 concluded. **One
honest caveat I found that the record does not currently state**: the
single shift that exceeds the observed correlation is not some distant,
unrelated lag — it's the *adjacent* one-sample shift (+0.2°), at
`r=0.9629`, only ~0.5% higher than the zero-lag value. So the claim "far
above any control" is correct against unrelated-shape controls, but the
zero-lag alignment is not the single best possible registration among all
31 circular positions — it is effectively tied for best with its immediate
neighbor. That is consistent with genuine, spatially coherent structure
(neighboring lags of a real correlated signal should score similarly), not
a red flag, but it should be stated precisely rather than implied to be an
untouchable global optimum.

## 3. Scrutiny of R10 (the new standing rule)

**Confirmed absent from LOGBOOK.md's own registry.** I grepped the full
18,400-line file for "R10" — zero matches anywhere. The rule currently
exists only in `phase3_synthesis.md`'s "New standing rule — R10" section;
it has not yet been transcribed into LOGBOOK's `## RULED OUT` list. Given
PANEL.md's own Phase-5 protocol ("Director updates LOGBOOK.md" as the last
step of Phase 5), this is expected at this point in the cycle, not itself a
defect — but it means R10 is not yet load-bearing house discipline anywhere
outside this one experiment folder, and whoever transcribes it should fix
the gaps below rather than copy the current draft verbatim.

**Format/consistency gaps versus R6–R9, checked line by line:**

1. **Structural mismatch.** R6–R9 are each a single `- **R<N> — ...**` bullet
   inside the registry list. R10 is currently written as a separate `##`
   markdown section in `phase3_synthesis.md` — it will need re-casting into
   the bullet format, not pasted in as a header, to sit consistently among
   R6–R9.
2. **Missing the standard escalation clause — the most substantive gap.**
   R6, R7, R8, and R9 *each* explicitly state, in near-identical language,
   that a cycle violating the rule "fires Checkpoint criterion 4
   automatically" (R6: "no further deliberation"; R7: "if it survives to
   Phase 3 unchanged"; R8: "if the named check was affordable and not run";
   R9: "when the comparison later proves incommensurable"). **R10's current
   text has no such clause at all** — it states the rule but not its
   consequence. As drafted, R10 is the only member of this four-rule
   lineage with no teeth. This should be fixed before it is trusted as a
   peer of R6–R9.
3. **Missing a trailing "Full record:" citation** (expected once written
   into LOGBOOK; every R6–R9 entry ends with one pointing to the specific
   experiment file(s) and section).
4. **The substantive open question is real and, as the task asked me to
   check, under-specified.** R10's own text says: *"any future
   free-period-fit... verdict must clear an order-preserving
   null-under-noise test (circular-shift on the real data, or an
   equivalent structurally-matched surrogate — see R10's own open question
   below)"* and then explicitly flags that Iteration 60's EM/Red-Team
   episode (an AR(1)-parametric surrogate that Red Team's own from-scratch
   rebuild **could not reproduce**, `p≈0.09–0.10` vs. EM's claimed `0.766`)
   already shows a non-circular-shift "surrogate" can itself be wrong. R10
   names this as an open question but sets **no bar at all** for when a
   non-circular-shift surrogate may be trusted over circular-shift. As
   written, a future cycle could reach for any self-labeled "structurally-
   matched" surrogate and cite its own unverified number — exactly the
   failure mode that just happened one cycle before R10 was adopted.

**Proposed sharper formulation** (to replace the "open question" paragraph,
keeping the rest of R10 intact):

> Circular-shift-on-the-real-data is the **mandatory default** null-under-
> noise test for any finite, order-preserving free-period or free-phase
> fit, and must always be run and reported even when another surrogate is
> also tried. A non-circular-shift "equivalent structurally-matched
> surrogate" (AR(1)-parametric, phase-randomized/IAAFT, wavelet-matched,
> or other) may **supplement but never replace** the circular-shift
> verdict unless (a) the choice of surrogate family is justified, *before*
> the surrogate is run, by a stated diagnostic of the observed data's own
> dependency structure (e.g. its measured autocorrelation or periodogram)
> — not selected after seeing which surrogate gives the more favorable
> answer — and (b) the surrogate's own null-generating code is
> independently re-implemented from scratch by a second seat and its
> headline figure reproduces, matching this program's existing R4/R6
> reproduction standard, before it is cited in a permanent record. If a
> validated alternative surrogate and circular-shift disagree, both
> numbers are reported side by side and the more conservative one governs
> the verdict. **A cycle that ships a free-period/free-phase SUPPORT
> verdict backed only by an unreproduced surrogate, or that omits the
> mandatory circular-shift baseline entirely, fires Checkpoint criterion 4
> automatically** — closing the one gap where R10 alone, among the
> R6–R9 lineage, currently carries no escalation consequence.

I would also flag, as a distinct nuance worth one added sentence in R10
(not a blocking gap, but relevant to exactly this cycle's own leg (a)):
when the "observed curve" is itself a **deterministic, zero-measurement-
noise** desk quantity (a closed-form Huygens-sum evaluation, as here) —
rather than real FDTD output with genuine physical noise — a circular-shift
test is answering a *self-similarity/specificity* question ("how much does
this curve's own smoothness alone explain an apparently good fit"), not a
literal measurement-noise question. Both are legitimate uses of the same
machinery, but the record should say which one is being asked, because it
changes what "distinguishable from noise" even means for a curve that has
no noise in it at all. See §4 below for the sharper alternative this
distinction points to.

## 4. Is there a sharper null test QUANTUM's charter would reach for here?

Yes, and it's cheaper than more null-testing. `leg_a_curve()` is a **zero-
FDTD, deterministic, arbitrarily-re-evaluable function of θ** — Phase 1's
own cost note says exactly this ("zero new FDTD calls... pure Python desk
calculation"). The entire circular-shift exercise is needed *only* because
the model was evaluated on the same cramped 31-point/6° window the real
FDTD data happened to use. But nothing forces that constraint on the
*model* — only on the real curve it's compared to. The sharper move: **hold
the real target period fixed and re-evaluate the model over a much wider
angular span (tens of periods, thousands of points, still zero marginal
cost)** to pin down `P_model_a`'s own asymptotic period to near machine
precision, entirely independent of any 31-point sampling window or null
distribution. Two clean outcomes follow directly, no significance test
needed: if the wide-window period converges to something near 2.53° (or
converges to something markedly different from the narrow-window fit's
2.53°, which would itself be diagnostic of a finite-window artifact), that
answers the P_edge_A question with certainty rather than a p-value; if it
converges to a value nowhere near `P_edge_A=2.8421°`, leg (a)'s period
question is settled REFUTE outright, no null test debate required. This
uses the one genuine advantage a deterministic desk model has over real
noisy FDTD data — free, unlimited "more data" — instead of squeezing more
significance-testing machinery out of a fixed 31-point sample. I did not
run this myself (it requires re-deriving/re-evaluating
`edge_diffraction_c_empty_corrected` at new angles, which is Iteration-62
scope, not a from-scratch reimplementation I could responsibly improvise
without the exact `dg048`/`dg065` geometry conventions in hand), but I flag
it as the single most directly actionable, cheap, and sharper-than-circular-
shift next step.

## 5. Ranked top-3 candidate next directions (Iteration 62+, QUANTUM's vantage)

1. **Fix and formally adopt R10.** Zero FDTD, highest priority: transcribe
   R10 into LOGBOOK.md's registry in the correct bullet format, add the
   missing Checkpoint-4 escalation clause, and replace the open "equivalent
   structurally-matched surrogate" language with the concrete
   surrogate-validation bar proposed in §3. This closes a real, currently-
   exploitable gap in the program's own newest rule before a future cycle
   hits it the way Iteration 60 already did once.
2. **Wide-window zero-FDTD re-evaluation of leg (a)'s own model period**
   (§4) — the sharpest, cheapest available test, decisively resolving
   whether `P_model_a≈2.53°` is a genuine asymptotic property of the
   source-aperture Huygens sum or a narrow-window fitting artifact, without
   needing any null-significance machinery at all.
3. **Extend the same circular-shift scrutiny already applied to the
   period-match to the shape-correlation finding** (§2.3, which I ran
   myself this cycle) as a standing, pre-registered check for Iteration 62
   — the correlation claim is currently the strongest surviving result
   (96.7th percentile vs. its own null, far sharper than the period
   match's 50th), but the near-tied adjacent-lag result (shift=+1 at
   r=0.9629) deserves a principled explanation (why zero-lag specifically,
   physically) rather than being left as an observed near-tie.
