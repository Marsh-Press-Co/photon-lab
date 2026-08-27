# PHASE 5 — REVIEW · QUANTUM OPTICS (blind) · Panel Iteration 55 · exp-078

*Fresh sub-agent, QUANTUM OPTICS charter (PANEL.md seat 5): non-classical
absorption, state-dependent or coherent interactions; mechanisms enter the
bench only as effective classical parameters — σ(I), σ(x,t), dispersive
ε(ω), gain — or Red Team strikes them. Fresh context: I do not see any
other seat's Phase-5 review this cycle, including my own Phase-2 critique
from earlier in this cycle (re-read here only as a historical document to
verify against, not as a source of unexamined authority).*

---

## 1. Verdict: **PARTIAL** (concurring with the record)

Test-A-only reading, 0/3 SUPPORT, 0/3 REFUTE, under the geometrically
correct angle — INCONCLUSIVE, and not desk-closed. This is a genuine
narrowing (both of the as-filed document's apparent SUPPORT verdicts were
entirely an angle-convention artifact, independently confirmed five ways
in the record and by my own re-derivation below), not a null result and
not a positive finding either. Nothing here rules out the y-wall echo
mechanism class, but nothing here earns building the full y-mirrored
coherent propagator. I have no basis to overturn the Combined result.

On the narrower question this task actually assigns my seat — does the
fresh 20,000-trial null-calibration control (`phase4_null_calibration_
corrected.py`) hold up, and is there a smarter statistic available for
this specific all-INCONCLUSIVE outcome — my answer is **qualified yes: the
control as executed is sound and its headline numbers reproduce exactly,
but its own joint statistic is closer to vacuous than informative for a
0-of-3 observed outcome, and a smarter, already-computable omnibus
statistic (below) tells a materially better-supported version of the same
story.**

---

## 2. Independent verification of the fresh 20,000-trial control

### 2a. Source-read: R4-clean, imports rather than reimplements

Read `phase4_null_calibration_corrected.py` directly, not merely its
output. It loads `y_wall_prescreen.py` via `importlib` and calls
`ywp._free_period_search` (line 59) — the identical vetted search function
`y_wall_prescreen.py`'s own real-data primary model uses, not a
reimplementation. The staged-widening harness (`STAGES`, lines 94–98;
`staged_free_period_quiet`, lines 101–119) copies the three-stage list
(`narrow[1,4]`→`wide[1,15]`→`widest[1,60]`) as a plain data structure —
only the stage-stepping loop is authored locally, matching the identical
pattern `phase2_quantum_null_check.py` (my own Phase-2 script) and
`pad_round_trip_model.py` (exp-077) both already established as this
program's house idiom for null-generation harnesses. This satisfies R4 as
the task brief asks me to confirm.

It is also, correctly, a **separate file** from my own Phase-2 script
rather than a mutated retarget of it (the file's own header states this
explicitly) — `phase2_quantum_null_check.py` stays a historical,
already-cited artifact (Red Team's Phase-2 audit cross-checked its output
line by line against its JSON); this file is Phase 4's own fresh
instrument at `n_trials=20000` reading the now-corrected
`y_wall_prescreen_results.json`. Correct discipline: it does not silently
overwrite what a prior phase already verified.

### 2b. Cross-check against the committed JSON, done myself, two levels deep

I read `y_wall_prescreen_results.json` directly (not `phase4_results.md`'s
summary) and independently confirmed the corrected primary-model numbers
the null control targets:

```
pair_pad:       p_model=3.218045112781955°  rel_dev=0.3021377337354387  R²=0.1563466153324431
c80_c40:        p_model=4.0°                rel_dev=0.40740740740740744
pair_absorb40:  p_model=2.8045112781954886° rel_dev=0.32844323144245247
```

These match `phase4_null_calibration_corrected_results.json`'s own
`"observed"` block exactly, to the same number of digits, and both match
`phase4_results.md`'s reported table. I then re-read the null-calibration
JSON itself and reproduced the headline numbers the task brief cites
directly from source: per-target `P(null rel_dev≤observed)` =
`0.39595`/`0.1258`/`0.17435` for `c80_c40`/`pair_pad`/`pair_absorb40`;
`P(null R²≥observed)` = `0.2126`/`0.64655`/`0.8344`; joint
`P(≤0 of 3 SUPPORT under null) = 0.54265`, distribution
`{0: 0.54265, 1: 0.37365, 2: 0.0788, 3: 0.0049}` — every figure reproduces
bit-for-bit against the committed `phase4_null_calibration_corrected_
results.json` I read directly. **Independently confirmed, two ways
(source-code audit + direct JSON cross-check), not merely restated from
`phase4_results.md`'s own table.**

### 2c. Methodological check: no residual-autocorrelation trap here

This control draws fresh i.i.d. `N(0,1)` noise per trial — it is a
pure-noise null, not a residual-resampling bootstrap. exp-077's own Phase-5
QUANTUM review (my seat, prior cycle) found a real defect in a
*structurally different* instrument — a bootstrap that resampled REAL
residuals with `replace=True`, discarding their measured lag-1
autocorrelation of 0.63 (the R6-addendum/`G0-e(ii)` failure shape). That
concern does not transfer here: there are no real residuals being resampled
anywhere in this file: every one of the 20,000×3 noise curves is freshly
synthetic `N(0,1)`, independent by construction, with nothing to
autocorrelate. **No R6/R6-addendum-shaped gap in this control.** I checked
for it specifically because it is the nearest precedent in this exact
sub-thread and confirmed it does not apply.

---

## 3. A real design gap: the joint statistic degenerates for a 0-of-3
observed outcome; a smarter, already-computable omnibus statistic exists

This is the task's own explicit question ("is there a smarter statistic
than the raw SUPPORT-count for an all-INCONCLUSIVE observed outcome?") and
the answer is yes, demonstrated below, not merely argued.

**The problem, in the script's own words.** `phase4_null_calibration_
corrected.py`'s own runtime print (lines 148–150, reproduced verbatim in
the committed output) says of its own joint check: *"a LOW value here
would mean the corrected model clears SUPPORT unusually RARELY vs noise —
not evidence for the mechanism either way; this metric mainly documents
that 0-of-3 is, as expected, an unremarkable outcome."* This is an honest,
self-aware disclosure — but it is also an admission that the one joint
statistic this control reports (`P(≤0 of 3 SUPPORT)=0.5426`) carries
essentially no discriminating information for this cycle's actual observed
outcome. The binary `rel_dev≤0.30` threshold that made the joint
SUPPORT-count meaningful in QUANTUM's own Phase-2 control (where observed
was 2-of-3, a genuinely rare-under-null count worth asking about) is
exactly the wrong lens once every comparison lands just over that
threshold (`rel_dev=0.30`–`0.41`) rather than clearly under or over it —
thresholding throws away the graded information the per-target continuous
p-values already carry.

**A combinable, already-available alternative: Fisher's method on the
per-target continuous p-values the control already computes.** The control
reports, per target, `P(null rel_dev≤observed)` — a valid one-sided
p-value under the pure-noise null (independent noise draws per target, by
construction of the script's own loop structure) — but never combines the
three into a single omnibus statistic. I computed this myself, directly
from the three committed p-values, independent of anything in the record:

```
p-values (P(null rel_dev<=observed)): [0.39595, 0.1258, 0.17435]
Fisher X² = -2*sum(ln p_i) = 9.4924, df=6
combined p-value = 1 - chi2.cdf(9.4924, 6) = 0.1477

p-values (P(null R²>=observed)): [0.2126, 0.64655, 0.8344]
Fisher X² = 4.3310, df=6
combined p-value = 0.6320
```

**This is a materially more informative number than the degenerate joint
SUPPORT-count.** It answers the actual question a reader of this cycle
wants answered — "taking all three comparisons together, is there any
overall hint of a coherent signal, even one too weak for any single
comparison to individually clear a bar?" — in a way `P(≤0 of 3 SUPPORT)
=0.5426` cannot (that statistic is blind to *how close* each near-miss was,
collapsing `rel_dev=0.302` and `rel_dev=0.41` to the identical "not
SUPPORT" bucket). The omnibus answer on the period leg (`p=0.148`) is
closer to interesting than the joint SUPPORT-count's `p=0.543` makes it
look, but still comfortably above the conventional `0.05` bar — **it does
not change the INCONCLUSIVE verdict**, and the R² leg (`p=0.632`) is
unambiguous in the same direction the per-target numbers already show. The
finding is about the control's own reporting completeness, not about the
substantive result: the corrected model is not distinguishable from noise
either way, but the *evidence for that* is stronger and more precisely
characterized by the omnibus number than by the joint count the control
currently ships.

**Why the joint SUPPORT-count was the wrong axis to keep from QUANTUM's own
Phase-2 script in the first place.** It was the right statistic when
Phase-2's own control (targeting the wrong, as-filed model) had a genuinely
surprising observed count (2 of 3, `p=0.080`) worth asking "how often does
noise do this well" about. Retargeting the same statistic at a
structurally different observed outcome (0 of 3) without also adding a
graded companion statistic is the specific gap: the fix that mattered for
Phase 2's question (raise the trial count to house standard) was executed
correctly; the fix this new question needed (a statistic that does not
degenerate when the observed count itself is the null's own modal outcome)
was not identified, because the file's own author correctly noticed the
problem in prose (the runtime-print caveat quoted above) but did not build
around it. This is a real, if non-load-bearing, completeness gap —
matching this sub-thread's own established pattern (my own exp-077 review
found an analogous "narrowed the disclosed half" gap in a different null
appendix) — not a defect that changes today's verdict.

**Recommended same-shift fix**, in the spirit of my own exp-077-cycle
precedent (harden the appendix before it is leaned on again): add the
Fisher-combined (or equivalent, e.g. a Stouffer's Z) omnibus p-value on
`p_null_rel_dev_le_observed` and on `p_null_r2_ge_observed` as two new
fields in `phase4_null_calibration_corrected_results.json`, computed from
the three per-target p-values the file already produces — zero new Monte
Carlo trials required, this is a closed-form combination of numbers
already in hand.

---

## 4. Charter-applicability check: still not applicable, for the same
structural reason as last cycle

I looked specifically for whether any non-classical (σ(I), σ(x,t),
dispersive ε(ω), gain) parameter class could still be in play for the
y-wall pre-screen, the same check my seat ran on exp-077's x-wall model
last cycle. The answer is unchanged and for the identical reason: this
model reuses `boundary_reflectance.py`'s `reflection_coefficient` verbatim
(confirmed, §3.4 of `phase1_proposal.md`, independently re-verified by
three critics and Red Team this cycle) — a fixed, static, per-config
transfer-matrix reflectance with no intensity argument, no time
dependence, and no atom/molecule/real absorbing material anywhere in the
instrument. `σ(I)` and `σ(x,t)` require inputs this construction does not
have; dispersive `ε(ω)` is already the entire content of the mechanism
being scored (a frequency/angle-dependent `r(θ)`); coherent interference is
the full content of the "edge-image echo" being tested and is already
completely captured by classical Maxwell's equations at these field
strengths. Manufacturing a quantum-flavored variant here would fail my own
charter's expressibility contract on arrival — there is no missing
physical input of the kind quantum optics supplies. Stated as "not
applicable" rather than manufactured, per this program's own stated
preference (matching my own exp-077 Phase-5 finding, independently
re-reached here rather than merely carried forward).

---

## 5. Ranked top-3 candidate directions for Iteration 56 (my own seat's lens)

Checked against RULED OUT R1–R9 and PLAN.md's own Iteration-55 queue —
none of the below re-proposes a dead end; items 3/4/5 below are PLAN.md's
own still-open Tier-0/Tier-1 items, re-ranked from my seat's own
statistical-rigor lens, not new candidates.

1. **Wire the Fisher-combined omnibus statistic (§3) into the committed
   null-calibration record before anyone cites the joint SUPPORT-count as
   this cycle's own summary number.** Zero new Monte Carlo trials, desk-only,
   directly on my own charter (I proposed and ran the Phase-2 predecessor of
   this exact appendix). Prevents a future reader from reading
   `P(≤0 of 3 SUPPORT)=0.5426` as "nothing here is even mildly close to a
   signal" when the honest omnibus answer (`p≈0.15` on period,
   `p≈0.63` on R²) is a materially more precise, still-non-significant,
   characterization of the same true INCONCLUSIVE result.

2. **PLAN.md's own standing, twice-deferred Tier-1 item 7: the full-width,
   non-aliased second-wavelength (`G40`) leg.** With BOTH the x-wall
   (exp-075/077) and now the y-wall (this cycle) coherent-echo mechanism
   classes landing non-supporting once properly corrected and
   null-calibrated, this is now the cheapest remaining FDTD test of whether
   T28's ~2.84°-family periodicity is a real, wavelength-scaling-consistent
   physical effect AT ALL — independent of which named mechanism is being
   chased. Ranked above the mechanism-class items below because a negative
   result here would be the single most information-dense next result on
   the whole board: it would suggest the underlying signal itself, not
   just each mechanism guess for it, needs re-examining.

3. **An explicit ruling (Red Team's own reckoning, PLAN.md's Tier-0 item 3
   adjacent) on whether the coherent-echo mechanism-class board is
   effectively exhausted.** Two independently-derived, independently
   null-calibrated instantiations (x-normal unrealizable-admittance,
   y-normal edge-image self-echo) have now both been tested and both land
   non-supporting on their own pre-registered bands. This is close to
   PANEL.md's own "honest alternative product" stop-condition language (a
   mapped constraint/mechanism boundary) for this specific mechanism class,
   even though MATERIALS' realizable-admittance variant (PLAN.md item 3)
   and VISION's Yee-grid-dispersion correction (item 5) remain genuinely
   untested and could still move the picture. I rank this third, not first,
   for the same reason I ranked it third last cycle: it is a
   bookkeeping/governance question, not a new falsifiable test, and should
   not be allowed to substitute for item 2's own cheap, decisive spend.
