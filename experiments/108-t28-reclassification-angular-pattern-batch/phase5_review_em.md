# PHASE 5 — ELECTROMAGNETISM REVIEW · Panel Iteration 85 (exp-108)

## 0. Scope and independence note

Fresh context, blind to the other six seats' Phase-5 reviews. I raised the
box-independence attack at Phase 2 (`phase2_critique_em.md`); Red Team
combined it with QUANTUM's item-ii attack into one "unified fix" (§3,
`phase2_redteam_audit.md`), adopted by the Director in NOTES.md's
Phase 2→3 synthesis. This review checks whether that fix, AS
IMPLEMENTED and AS RUN, actually closes the attack — not whether it
was described correctly (it was; that much I confirm below).

**T1 escape-route: N/A, confirmed independently.** No σ(I)/σ(x,t)/
angular-selectivity/sub-threshold mechanism is built, varied, or scored
anywhere in this cycle's code (`grep -n "C_thr\|ambient\|Weber"
experiments/108-.../*.py` returns nothing). `materials.graded_black_shell`
and `materials.pec_disk` are reused unchanged, already-established passive
(real, non-negative σ) constructions — no new passivity/reciprocity claim
is made this cycle, so my charter's bookkeeping duty reduces here to the
one real EM quantity this cycle does compute fresh: the `closure`
absorbed-power identity (§3, below).

## 1. Independent re-verification from primitives

All three specified zero/low-cost re-derivations were run fresh, this
session, against the checked-in artifacts and the raw pickled phasor
captures still on disk in scratch:

- **`reclassify_106.py`**: reproduces exactly — `THREE-WAY-AMBIGUOUS
  (REFUTES-... nominally ... p_abs_frac_diff=0.1231(r156)/0.1796(r312)
  exceeds 0.10) (NOT-TRUSTED -- r=312 MARGINAL/unsettled)`, all other
  fields (`shape_ratio_fixedabs=18.228333...`, `noise_dominated=False`,
  `trusted=False`) bit-identical to committed `results.json`. Matches
  NOTES.md verbatim.
- **`analyze.py`**, re-run from the raw `chunk_runner.py` pickles still
  present in scratch (not from `results.json`): reproduces every
  headline number exactly — `item_i verdict=CONFIRM` (both r),
  `item_ii verdict=CONFIRM, residual_std=2.8972e-06`/`2.1022e-06`,
  `item_iii frac_unresolved=0.1827`/`0.2525`, `closure
  hollow=0.000196/0.000563, peccored=0.000160/0.000581`. All match
  `results.json`/NOTES.md exactly — this is a genuine from-primitives
  reproduction (fresh capture reload → fresh `sections.widths()`/
  `radial_absorbed_power()`/`angular_scattered_pattern()` calls), not a
  re-read of the same committed JSON.
- **`lab/validation/run_all.py --only 26`**: `2/2 checks passed`,
  positive control `max|diff|=0.000e+00`, negative control relative
  deviation `2.000` — exact match to NOTES.md.

No arithmetic or reporting defect found anywhere in this pass. The
substantive findings below are about what the numbers mean, not whether
they were computed or transcribed correctly.

## 2. Does the unified fix correctly formalize what box radius means for a near/mid-field angular quantity?

**Partially — the model choice is physically motivated; its application
is not fully gated by its own diagnostics, and NOTES.md's narration
overclaims what the numbers show.**

**The model itself is defensible, not arbitrary curve-fitting.** At
these box radii (`box_a` at margin=32 sits `r_box≈220` cells `=11λ` from
center at r=156, `kr≈2π·11≈69`), the boxes are deep enough in the
oscillatory regime that a leading-order `1/(kr)` correction — which is
exactly what `A + B/margin` models, since `margin` scales linearly with
`r_box` at fixed `k` — is the right functional form for the leading
near-to-far-field correction to a cylindrical-wave amplitude (the
`1/√(kr)` envelope of `H_l^(1)(kr)` plus its own `O(1/kr)` phase/amplitude
corrections). This is a real physical justification, not merely "a
smooth curve happened to fit" — I checked this from the geometry myself,
independently of anything either critique states.

**But `linear_fit_1_over_margin()` computes its own smoothness
diagnostic (`is_monotonic`, `r_squared`, `smooth = is_monotonic or
r_squared>=0.90`) and `classify_item_ii()` never reads it.** Read
directly, `run.py` lines 187–193: `classify_item_ii(r, residual_std)`
takes only the scalar `residual_std` and applies the CONFIRM/AMBIGUOUS/
REFUTE thresholds unconditionally. Contrast `classify_item_i()`, which
DOES gate its REFUTE branch on `fit["smooth"]` before trusting a
candidate run as physical (line 240, `if fit["smooth"]:
smooth_run_found = True`). The unified fix's own stated logic (NOTES.md:
"a genuine anisotropy signature should ... show smooth ... MIGRATION ...
distinguishable from noise by whether ... points trace a smooth curve or
scatter randomly") is applied to item i but silently dropped for item ii
— an internal double standard between the two halves of what Red Team
itself called "a single defect wearing two costumes."

**The numbers this cycle actually produced expose exactly why that
matters.** From `results.json`'s own `tier1.r156/r312.item_ii.fit`:

| r | `r_squared` | `is_monotonic` | `smooth` | raw std (recomputed) | `residual_std` (used) |
|---|---|---|---|---|---|
| 156 | 0.665 | False | **False** | 5.008e-6 | 2.897e-6 |
| 312 | **0.021** | False | **False** | 2.124e-6 | 2.102e-6 |

At r=312 the fit explains essentially none of the variance (`R²=0.02`)
— by the framework's OWN "smooth" criterion, defined for exactly this
purpose, this fit is not smooth (`smooth=False`, same as r=156). A
near-vacuous fit is expected to do almost nothing to the residual
variance, and it does almost nothing: raw std 2.124e-6 → residual_std
2.102e-6, a 1% reduction, not the "genuine near-field-convergence trend
removed" the Result narration claims. At r=156 the fit is somewhat
better (`R²=0.665`) but still fails the framework's own `is_monotonic`
test and its own `R²≥0.90` bar — `smooth=False` there too. **NOTES.md's
Result section calls both of these "the genuine, detrended floor ...
not merely informally decisive," language the code's own diagnostics do
not support at either r** — nowhere in NOTES.md's Result section is
`r_squared` or `smooth` for item ii even mentioned, despite both being
computed and persisted.

**This does not overturn item ii's CONFIRM verdict as a number** — I
checked: even the UN-detrended raw std at r=312 (2.124e-6) still clears
the CONFIRM bar (`≤1.234e-5`) by ~5.8×, so the substantive conclusion
("the box-placement floor is comfortably tighter than the signal") is
robust to whether the detrend did anything real. What it undercuts is
the specific claim that the detrend step made the number MORE
trustworthy or MORE "genuine" than the raw statistic QUANTUM's original
attack criticized — at r=312 the two are nearly identical, and at
neither r does the fit clear the bar the framework itself set for
trusting a fitted trend as physically real rather than noise.

**A second, related gap: item i's own smooth-migration REFUTE path —
the part of the unified fix that most directly answers my own Phase-2
attack — was never exercised.** `results.json`: `max(rel32)` = 0.000148
(r=156) / 0.000153 (r=312), roughly **300× below** even the 5% CONFIRM
bar and 1000× below the 15% REFUTE bar. No bin ever came remotely close
to triggering a candidate run, so `linear_fit_1_over_margin` was never
called on a real angular feature, and the smooth-vs-noise discriminator
Red Team specified — the actual mechanism that would resolve a genuine
Fresnel-zone-migration signature from a spurious single-radius
artifact — has zero empirical exercise this cycle, positive or negative.
Item iv got a proper R18-style fault-injection negative control for its
own new machinery; item i's more consequential new machinery (multi-
margin smooth-migration discrimination) got none. This is not a defect
in this cycle's result (the null is clean and, on its own numbers,
extremely clean — 0.015% max deviation, nowhere near ambiguous), but it
means the discriminator remains unvalidated for the failure mode it
exists to catch, should a future cycle at a different geometry produce
a genuine near-15%-threshold candidate.

## 3. `closure` — energy-bookkeeping meaning and physical soundness

`closure_for()` (`analyze.py`) computes `|radial_total − p_abs_box| /
|p_abs_box|`, where `radial_total` comes from `radial_absorbed_power()`
— a direct spatial integral of `0.5·σ_e·|Ez|²` over the lossy medium,
the true microscopic Joule-dissipation route — and `p_abs_box =
σ_abs·I_inc` comes from `widths()`'s box-ledger flux route (Poynting
flux through a closed contour). These are two genuinely independent
measurement routes to the same physical quantity (absorbed power); a
small residual between them is a legitimate FDTD-discretization
self-consistency check, not a tautology — this is exactly `ledger_check`'s
established meaning (`lab/sections.py::radial_absorbed_power`'s own
docstring, which explicitly calls this an "EMPIRICAL closure," not an
exact identity, because of staircasing and two-snapshot quadrature
phasor-extraction error).

Reported values (0.0160%–0.0581%) are physically sound: they sit
comfortably tighter than the trust suite's own general-purpose stage
10/11 baseline (`≤1.5%` gate, measured baseline `1.11%`/`1.13%` on the
canonical bench scene), which is plausible rather than suspicious — this
cycle's shells are large (`R_COAT`=156–312 cells) and well-resolved
(`cells_per_lambda=20`), so the discretization error this identity is
sensitive to is expected to be smaller here than on the trust suite's
smaller canonical scene. They also match exp-106's own precedent range
(0.02%–0.06%) almost exactly. No inconsistency found; independently
reproduced from primitives (§1). NOTES.md's citation of "0.02–0.06%
precedent" is accurate.

## 4. `stage26`'s negative control — does 1200-vs-900 steps test what it claims?

**Yes, and it is a real (not tautological) test of `chunk_runner.py`'s
actual risk surface — with one asymmetry worth naming.**

`chunk_runner.py::step_once()` reads `steps_done` from the pickled
checkpoint dict (`state["steps_done"]`) and computes `remaining =
g["STEPS"] - steps_done`. The stage-26 negative control corrupts exactly
this field (`corrupted_steps_done = 0` after a real 300 steps have
already run), which is a faithful model of the actual bug class this
mechanism could suffer (a mis-read or mis-written `steps_done`), not an
arbitrary or unrelated fault injection.

I checked whether the observed 200% deviation is a meaningful
demonstration or a trivial "any different step count differs" artifact:
the 900-step reference reuses stage 8's own canonical bench scene, which
has been the trust suite's validated convergence point for this exact
construction for many iterations (box_a/box_b agreement, lossless-object
zero check, etc. all pass at 900 steps) — so the comparison is not
against an undercooked transient. `radial_absorbed_power`'s own docstring
confirms phasor extraction here is a "two-snapshot quadrature" scheme,
which is phase-sensitive to the exact final step count; adding steps not
equal to an integer number of full optical periods (300 steps at
`cells_per_lambda=20`/`courant_frac=0.99` is not obviously an integer
period count) genuinely perturbs the extracted phasor. So the 200%
divergence is a real, physically meaningful demonstration that a
`steps_done` bookkeeping error silently corrupts every downstream number
— exactly the risk this control exists to catch, not a tautology.

**Gap, not a refutation:** the control only tests the "resume runs MORE
total physical steps than intended" direction (`steps_done`
under-reported → over-run). The symmetric direction — `steps_done`
OVER-reported, causing early truncation (fewer than the intended total
steps, e.g. a resumed run that stops at 600 instead of 900) — is the
same underlying bug class and is equally plausible in practice, but is
untested by this cycle's Gate 2. Worth a one-line addition next time
`stage26` is touched; not blocking, since both directions are covered by
the SAME `steps_done`-integrity risk this gate demonstrably catches in
one direction already.

## 5. Disposition of my own Phase-2 attack

**Closed correctly for item i, only partially for item ii.** My Phase-2
attack was that the original 2-point `box_a`/`box_b` REFUTE bar
conflates box-independence of a scalar Poynting-conserved quantity
(`sigma_scat`/`sigma_ext`, genuinely box-radius-independent by
conservation) with box-independence of its ANGULAR distribution (not
conserved at fixed near/mid-field radii). The unified fix's replacement
— require stability across all 6 margins for CONFIRM, and a genuine
smooth-vs-noise discriminator across 6 margins before trusting a REFUTE
— is the structurally correct answer to that attack for item i, and I
confirm it is implemented as specified (§2). It happens not to have been
exercised on its REFUTE branch this cycle because the null came back
extremely clean, not because the machinery is untested-and-passing.

For item ii, the SAME underlying defect (box radius treated as an
exchangeable nuisance dimension) is only nominally fixed: the detrend
model is computed, but its own fit-quality gate is not applied before
the residual is reported as a "genuine floor," and NOTES.md's narration
states more physical confidence in the detrend than the code's own
diagnostics (`r_squared=0.02` at r=312) support. This is a documentation/
rigor gap on top of an otherwise-correct implementation, not a wrong
number.

## Verdict

**CONFIRM-WITH-GAPS.**

All headline numbers independently reproduce exactly from primitives
(reclassify_106.py, analyze.py re-run against raw scratch pickles,
stage26). T1/constraint scoring is correctly N/A throughout — no
mechanism claim to bookkeep. `closure`'s energy identity is sound,
correctly computed, and consistent with stage 8/10's own established
convention and exp-106's own precedent. `stage26`'s negative control
genuinely tests `chunk_runner.py`'s real risk surface (one direction of
it). The unified EM+QUANTUM fix is a real, physically-motivated
improvement over the original 2-point box comparison for item i, and I
confirm its function-level correctness. **The gap:** `classify_item_ii`
does not gate on the smoothness diagnostic the same fix's own logic
defines and computes, so item ii's CONFIRM is narrated as resting on a
"genuine, detrended" trend that, by the code's own `r_squared`/`smooth`
output, was not actually established at either r (most starkly at
r=312, `R²=0.02`) — and item i's own REFUTE-path discriminator, the
piece of the fix that most directly answers my Phase-2 attack, was never
empirically exercised this cycle. Neither gap changes any verdict filed
this cycle, and both are cheap, well-scoped fixes for whichever future
cycle next touches this instrument: gate `classify_item_ii` on
`fit["smooth"]` (or explicitly document why it deliberately isn't
gated), and note in NOTES.md's own Idealizations that the REFUTE-path
discriminator remains empirically unexercised.
