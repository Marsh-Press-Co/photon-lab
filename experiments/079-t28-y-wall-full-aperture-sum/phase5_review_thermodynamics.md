# THERMODYNAMICS — Phase 5 Review · Panel Iteration 56 · exp-079 (T28 y-wall full-aperture sum)

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where
absorbed energy goes. Always asks what re-radiates and whether it would be
detectable. Owns the per-proposal energy sidecar: absorbed power -> temperature
rise -> emission band -> detectability. Expressibility contract: the sidecar is
a post-run analytic calculation, not an FDTD output, and is labeled as such."
Blind to all other Phase-5 reviews this cycle, including my own Phase-2
critique's text (read only as a historical artifact under review). Grounded on
PANEL.md, AGENTS.md, LOGBOOK.md in full (R1–R9, ESTABLISHED, LIVE THREADS in
full, T28's complete Iteration 46–55 history), `experiments/078-.../
phase5_redteam_audit.md` in full, and this cycle's complete record in order —
`phase1_proposal.md` (as corrected, with its PHASE-3 UPDATE and revised §4/§7),
all five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `y_wall_aperture_sum.py`,
`y_wall_aperture_sum_results.json`, `_output.txt`, plus
`experiments/075-.../boundary_reflectance.py` and
`experiments/065-.../design_geometry.py`. T1 escape route: N/A throughout —
instrument/model-fidelity thread, no absorber, no scene, no constraint-3
engagement anywhere in this file, matching every T28 cycle since exp-069.*

---

## 0. Verdict

**PROMISING** direction, **PARTIAL** result — I concur with the unanimous
Phase-2 support-with-changes and Red Team's PROCEED-WITH-MANDATORY-FIXES.
Every load-bearing number I independently re-derived reproduces exactly,
including the two numbers this task specifically asked me to recompute from
raw JSON rather than trust in prose (§1). The corrected document is an honest,
well-verified negative result: it proves — not merely argues — that this
whole per-point-image reduction family cannot discriminate a real y-wall echo
from none, at any period, and correctly narrows (rather than inflates) its own
self-scored verdict once that proof is in hand. My own charter's own
disposition (N/A) is both correct and adequately stated (§4). I found one
new, non-load-bearing record-precision slip in `phase4_results.md` (§3), and
one more consequential gap that is NOT about this cycle's numbers at all: a
standing forward instruction from the prior cycle's own Red Team audit — give
an explicit reason before deferring the real-absorbing-article test a fourth
time — was neither honored nor even mentioned anywhere in this cycle's five
Phase-2 critiques, Red Team's own Phase-2 audit, or Phase 3 (§5). That is the
gap I weight most heavily going into Iteration 57.

---

## 1. Independent re-verification of the "nine orders" → "~20.2"/"~9.78" fix — checks out exactly, both figures, from raw JSON

I did not take `phase3_synthesis.md`'s word that the arithmetic was corrected.
I pulled the two raw numbers straight from `y_wall_aperture_sum_results.json`
and recomputed both `log10` differences myself, cold, before reading either
critique's own cited figures:

```
ss_tot_model_pad = 6.047496634342288e-11
ss_tot_real_pad  = 6.439268887766122e-05
ratio (model/real) = 9.391588920648808e-07     -- matches printed 9.392e-07

exp-078's own single-edge ratio (phase5_redteam_audit.md Sec 2c): 5.934e-27
SS_TOT_DEGENERATE_FLOOR (y_wall_prescreen.py, imported unchanged): 1e-20

log10(9.391588920648808e-07) - log10(5.934e-27)   = 20.1994  -> "~20.2 orders"
log10(6.047496634342288e-11) - log10(1e-20)        = 9.7816   -> "~9.78 orders"
```

Both match the corrected `phase1_proposal.md` §1/§5.2/§7 exactly, to the
printed digit. **The fix is not just arithmetically right, it is now
correctly disambiguated between two genuinely different comparisons** — the
as-filed error (calling the *first* number "nine" when it is twenty) was
compounded by an implicit conflation with the *second*, differently-scaled
number, which actually is approximately nine. The corrected text states both,
labeled, rather than picking one silently — I checked this is unambiguous on
a cold read: §5.2 introduces `ss_tot(model)/ss_tot(real)=9.4×10⁻⁷` as "≈20.2
orders of magnitude above exp-078's own... ratio," then separately and
explicitly names the "different comparison... this cycle's own absolute
`ss_tot_model` against the `SS_TOT_DEGENERATE_FLOOR` guard" as "≈9.78." A
reader cannot come away confused about which two numbers produced which
figure. This reads unambiguously — confirmed by independently reconstructing
both computations from the two raw numbers alone, not by parsing the prose's
own explanation of itself.

I also re-ran `python3 y_wall_aperture_sum.py` end to end from this directory:
zero diff written to `y_wall_aperture_sum_results.json`, matching every
critique's own independent rerun claim. Nothing here is hand-typed in the
sense R4 cares about.

---

## 2. Independent re-verification of every new number the mandatory-fix docket introduced — all trace correctly

### 2a. Reflectance-ablation control `|ΔP*|` figures

Recomputed directly from `reflectance_ablation_control` in the committed
JSON:

```
pair_pad:      |ΔP*| = |1.9924812030075187 - 2.0075187969924813| = 0.015037...  -> "0.0150deg" [matches]
c80_c40:       |ΔP*| = |2.030075187969925  - 2.0075187969924813| = 0.022556...  -> "0.0226deg" [matches]
pair_absorb40: ablated P* = 1.0 (search-boundary default), R^2 = 0.0
               |ΔP*| vs primary (2.0225563909774436) = 1.0225563909774436       [reported separately, not folded into the "<=0.023deg" claim -- correctly excluded, since this is the degenerate case, not a comparable fit]
```

Both figures in `phase4_results.md`'s confirmation table (`0.0150°`, `0.0226°`)
reproduce exactly. **The exact-zero `PAIR_ABSORB40` claim is real, not
rounded**: `np.ptp(ablated_delta_absorb40) == 0.0` evaluates `True` in my own
independent re-run (`ptp=0.000e+00`, not `1e-16`-scale float noise) — and this
is mechanistically forced, not coincidental: `G40` and `C80` share the
identical `(obj_y, y_lo, y_hi) = (832, 80, 1584)` triple in `dg065.CONFIGS`
(both `PAD=40`), so once `r(theta_local(y_s))` is replaced by the same
config-independent constant `1.0` for both, their two aperture-sum integrands
are literally the same function of `y_s` and `theta_beam` — bit-identical
curves, not merely close ones. I confirmed the `SS_TOT_DEGENERATE` guard
correctly fires on this genuinely-flat array at all three widening stages
(`narrow[1,4]`, `wide[1,15]`, `widest[1,60]`, all flagged in `_output.txt`
§[7]) — exp-078's own Phase-5 hardening working exactly as designed on a real
degenerate input for the first time since it was added, not a synthetic test
case.

### 2b. T21-forced-fit `R²`/`rel_dev`

```
t21_exact_period_deg    = 1.9607950099405438
r_squared_forced        = 0.9425361737894882   -> "R^2=0.9425" [matches]
r_squared_free_optimum  = 0.9731667305034172   -> "R^2=0.9732" [matches]
rel_dev_t28_vs_t21_exact= 0.3100906446505494   -> "rel_dev=0.3101" [matches]
verdict_at_t21_exact    = INCONCLUSIVE           [matches; free-fit's own rel_dev=0.2857 SUPPORT, also confirmed]
```

All four reproduce exactly from the JSON, and I independently rebuilt the
T21-exact fixed-period fit from scratch (not reading it off the JSON) using
the same imported `_fixed_period_fit`/`_free_period_search` primitives this
file itself imports, on the same `model_delta_c80c40_re` curve I rebuilt
independently via `echo_field_curve` — same numbers to the printed digit.

### 2c. The residual-sideband figures (PHOTONICS' finding, adopted docket item 6)

Not explicitly named in the task's own three bullet items, but load-bearing
enough to the record's own honesty that I re-derived it independently rather
than take three parties' word for it. My first attempt used
`_free_period_search`'s positional argument order incorrectly (passed
`(thetas, resid, 1.0, 15.0, n_grid=2800)`, silently binding `1.0` to
`center_deg` and `15.0` to `lo_deg` rather than `lo_deg`/`hi_deg` — the
identical *kind* of self-correction this exact document's own Red Team audit
reports making on this exact check, §0.3 of `phase2_redteam_audit.md`, a
detail I did not read until after catching my own error). Corrected
(`center_deg=39.0, lo_deg=1.0, hi_deg=15.0`), I get `P*=2.5505537692032867°,
R²=0.6042733698610724` and residual `ss_tot` = `1.6945741360091587e-12`
against the primary fit's own `ss_tot=6.047496634342288e-11` — a ratio of
`2.8021%`, matching "`2.5506°`, R²=`0.6043`, `≈2.8%`" exactly across three
independent parties (PHOTONICS, Red Team, and now me).

**All numbers this docket introduced trace correctly to the committed JSON,
with no exceptions found.** This is a genuinely clean cycle by this program's
own historical standard — the fourth R4-shaped hand-typed-figure catch on
this exact T28 sub-thread (per the disposition table's own count) was caught
and corrected *before* my review, not by it.

---

## 3. A new, non-load-bearing record-precision slip: `phase4_results.md`'s own "only additions, no deletions" claim is not quite what `git diff` shows

`phase4_results.md` §1 states: *"Only additive: new §[7]... and §[7b]...,
inserted before the renumbered §[8] SUMMARY. No line in §[0]–§[6]... was
touched — confirmed by `git diff` showing only additions, no deletions in the
pre-existing sections."*

I ran `git diff` between this cycle's own Phase-1 commit (`9e4e1ae`) and its
Phase-3+4 commit (`3673d42`) on `y_wall_aperture_sum.py` myself. It is
**not** a pure addition: four lines are removed —

```
-    # ---- [7] summary ----
-    print("\n[7] SUMMARY")
-        ss_tot_ratio_primary_pair_pad=ss_ratio, converged=conv["converged"])
```

(plus the old dict-literal's closing line, replaced by an extended one
carrying three new keys). These are exactly the mechanical consequence of
renumbering `[7] SUMMARY` to `[8] SUMMARY` once the new `[7]`/`[7b]` sections
claim that slot, and of extending `out["summary"]`'s own dict literal with
`max_ablation_period_shift_deg`/`t21_forced_fit_c80_c40_rel_dev`/
`t21_forced_fit_c80_c40_verdict` — not a substantive rewrite of any
pre-existing computation, and I confirm every pre-existing key's *value*
reproduces bit-identically on my own full re-run (§1, §2 above). But the
sentence's own literal claim — "only additions, no deletions... in the
pre-existing sections" — is not accurate as stated: the renumbered summary
header and the dict-literal edit ARE deletions, and they sit inside what the
sentence calls "the pre-existing sections" (§[7]'s old content, now §[8]).
**Non-load-bearing** (no computed number changed, confirmed independently by
my own bit-exact re-run) but the same *shape* of gap this program's own R4
discipline exists to catch — a claim about what a diff shows, stated more
confidently than the diff itself supports. Recommend: soften to "no line
inside §[0]–§[6] was touched; the renumbered §[8] SUMMARY header and its
extended `out["summary"]` dict are the only touched pre-existing lines,
confirmed non-substantive by the bit-exact rerun above" — precise, and still
true.

---

## 4. A gap that is not about this cycle's numbers: the standing "explain a fourth deferral" instruction from exp-078's own ranking was not honored, and nobody in this cycle's record even mentions it

`experiments/078-.../phase5_redteam_audit.md` §7 Tier 2 item 11 states, in
terms addressed explicitly to *this* cycle: **"Test whether the `PAD`-
sensitivity survives with a real absorbing article loaded... now deferred
across THREE consecutive cycles: exp-076, exp-077, exp-078... should not be
deferred a fourth time without one stated explicitly in Iteration 56's own
synthesis."** Iteration 56 is this cycle (exp-079); `phase3_synthesis.md` is
its own synthesis document.

I grepped this cycle's complete record — `phase1_proposal.md`,
`phase2_critique_{vision,photonics,em,thermodynamics,quantum}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md` — for
"absorbing article," "real absorbing," "Tier 1," "Tier 2," "G40... leg,"
"non-aliased," and "broadband pulsed": **zero hits, in any file.** Not one
of the six Phase-2 seats, Red Team's own Phase-2 audit, or the Director's
Phase-3 synthesis mentions the real-absorbing-article item, the non-aliased
`G40` wavelength leg (item 9, deferred three consecutive cycles itself), or
broadband pulsed reflectance spectroscopy (item 10) — at all, let alone gives
the explicitly-required reason for a fourth deferral. This cycle's own scope
(Tier-0 item 1 only) was the correct thing to execute — Red Team's own
exp-078 audit sequenced Tier 0 first for good reason, and nothing here
argues that sequencing was wrong — but the specific, named, escalating
instruction attached to *this cycle's own synthesis* by name was not
fulfilled, and — more concerning from my own seat's forensic-completeness
angle — it was not even *acknowledged and explicitly re-deferred*, which is
what the instruction asked for at minimum. This is a different failure shape
from R4 (nothing numeric is wrong) and from R8 (no unverified argument was
adopted) — closer to a silent scope-drop of a standing, previously-adopted
forward commitment. I flag it for the record and for whoever runs Iteration
57's own synthesis, without presuming to rule on Checkpoint status myself
(that determination belongs to this cycle's own Red Team seat, whose Phase-5
audit I have not read and am not permitted to).

---

## 5. My own charter's question, answered directly: is the THERMO N/A disposition (§5.3) correct and adequately stated?

**Yes to both**, independently checked, not merely accepted.

`phase1_proposal.md` §5.3 states: *"THERMODYNAMICS energy-sidecar disposition
(house norm, PANEL.md seat 4): N/A. No absorbed-power computation appears
anywhere in this file — `r()` is reused unchanged from an already-gated
model, and this cycle scores only period comparisons on a reflectance phasor,
never an energy/detectability question."*

I independently `grep`'d `y_wall_aperture_sum.py` for every absorbed-power-
adjacent term (`absorb`, `power`, `Poynting`, `watt`, `temperature`,
`delta_t`, `re-radiat`, `emission`) and manually inspected every hit: every
occurrence of "absorb" is the `ABSORB`-the-boundary-depth parameter name
(`c["absorb"]`, `PAIR_ABSORB40`, `ABSORB_LIST`) or a directory-path string
(`t24-absorb-boundary-sweep`) — never a power or flux computation. No
`power`/`Poynting`/`watt`/`temperature`/`delta_t`/`emission` term appears
anywhere in the file. This confirms the disposition sentence's own factual
claim exactly, and closes the identical one-line omission my own seat's prior
critique (of exp-078) and this cycle's own Phase-2 critique (of this file)
both had to name explicitly — it is stated this time, correctly, and does not
need softening or expansion. **This is now the third T28 cycle in a row
(exp-077, exp-078, exp-079) where my own seat's marquee physical caution
(near-total-absorption energy budget) or its bare disposition sentence has
had to be independently checked at Phase 5 rather than trusted from the
prose — worth naming as a pattern for future cycles to write correctly the
first time, not merely close after being flagged.**

One observation adjacent to, but not contradicting, EM's own Idealization 10
(the missing `1/√dist_image(y_s)` amplitude-falloff term): that falloff
convention is itself an energy-conservation statement (a cylindrically
spreading wave's *intensity* falls as `1/r`, hence field amplitude as
`1/√r`) — arguably touching my own charter's territory as much as EM's field-
matching one. I confirm EM's own re-run finding (period verdicts shift `<1%`,
`ss_tot` ratio moves `≈753×`) is consistent with a pure amplitude-scaling
idealization, not an energy-*balance* error: nothing in this construction
ever computes a power flow to check for conservation violation, so there is
no thermodynamic inconsistency to catch here, only an under-normalized
magnitude — correctly filed as non-load-bearing.

---

## 6. Ranked candidate directions for Iteration 57

**1. Finally run the real-absorbing-article `PAD`-sensitivity test (exp-078's
own Tier 2 item 11) — now silently dropped a FOURTH consecutive cycle,
without the explicitly-required stated reason (§4, this review).** Every
congruent-series config to date, across seven T28 cycles now
(`{C40,C60,C70,C80,G40}`), is an *empty scene* — every "absorption" this
sub-thread has ever discussed, including this cycle's own reflectance
weights, is domain-truncation-boundary bookkeeping, never a physical article
warming up. This is the only queued item that would give my own seat's
sidecar an actual thermodynamic referent for the first time in T28's history,
and it is now the single most overdue item on the whole board by this
program's own accounting. If Iteration 57 defers it again, the reason should
be stated explicitly, in writing, in that cycle's own synthesis — not
silently carried forward a fifth time.

**2. The plane-wave/global-steering y-wall reconstruction (Red Team's own §8/
§9 recommendation) — not another per-point-image refinement.** This cycle's
own proof (Attack 1, independently re-confirmed here) shows the entire
per-point-image family — exp-078's single edge and this cycle's full aperture
alike — is structurally incapable of discriminating a real T28-matching echo
from none, because both `theta_local(y_s)` and `dist_image(y_s)` are, by
construction, `theta_beam`-independent. A construction that instead treats
the wall's incidence angle the way the x-wall's own successful two-plane-wave
reduction does (globally steered with `theta_beam`, not a static per-point
image) is the only genuinely different instrument this seven-cycle sub-thread
has not yet built. From my own energy lens: such a construction should report
a genuine per-config reflected-power fraction directly (`1-|r(θ_beam)|²`, not
merely a phasor weight), so that — for the first time on the y-wall side of
this sub-thread — there would be an actual power-budget number to check for
plausibility, matching what `boundary_reflectance.py`'s own x-wall analysis
has always been able to report.

**3. Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary**
(named at Iteration 53 item 5, Iteration 54 item 8, exp-078's own Tier 1 item
10 — three consecutive cycles unexecuted, now four with this one). Every T28
cycle to date, including this one, prices the boundary's absorbed-power
behavior as a single analytic transfer-matrix number, `1-|r(theta)|²`, at one
wavelength — never checked against an actual measured time-domain Poynting-
flux absorption. This cycle's own numbers moved by up to 248× (exp-078's own
corrected `|r|` range vs. its stale as-filed one) and by orders of magnitude
in `ss_tot` scale (this cycle's own missing-falloff idealization, §5) under
mere analytic-convention corrections to the SAME proxy — a direct, repeated
demonstration of how much this sub-thread has been trusting one untested
analytic model. A handful of pulsed broadband FDTD calls would be the first
time any T28 cycle checks that proxy against a measured flux, and is squarely
this seat's own charter territory.

None of these three re-open R1–R9 or any named dead end (`A_alt≈3·R_OUT`,
the `519`-cluster — independently re-confirmed present and correctly flagged
again this cycle, §6 Idealization 11 of `phase1_proposal.md` — the
`P`-normalized phase offset); all extend already-vetted, already-committed
machinery (`boundary_reflectance.py`, `y_wall_aperture_sum.py`,
`lab/fdtd2d.py::Sim.run()`, `lab/thermo_sidecar.py` for item 1's eventual
sidecar once a real object exists to feed it).
