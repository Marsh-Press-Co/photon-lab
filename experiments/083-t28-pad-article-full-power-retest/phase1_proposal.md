# PHASE 1 — PROPOSAL · Panel Iteration 60 · exp-083
## The full 31-point/0.2° `PAIR_PAD`-with-article re-test at 600nm — resolving the mechanism-identity question exp-082 showed was UNRESOLVABLE at reduced power

**Lead: VISION SCIENCE** (by rotation; Iteration 58=THERMO, 59=QUANTUM,
60=VISION, per PANEL.md's lead-rotation table). Executes PLAN.md's own
Iteration-60 queue Tier 1 item 5 (`experiments/082-.../
phase5_redteam_audit.md` §10, reconciled ranking) — the near-unanimous
single highest-value item on the board (ranked #1 by PHOTONICS,
THERMODYNAMICS, QUANTUM at Iteration 59's own Phase 5; a top-2 precondition
by MATERIALS, VISION; paired by EM).

---

## 0. What this cycle is and is not

exp-082 (Iteration 59, QUANTUM lead) discharged PLAN.md's own six-cycle
tripwire on the PAD-loaded real-article check at a **disclosed, reduced-power
7-point/1°-step** subset of T28's established dense window. Its primary
amplitude-ratio metric (`ratio=A_scene/A_empty=0.6573`) landed decisively
inside the pre-registered `[0.5,2.0]` SURVIVES band — that computation is
settled, bit-exact, and not re-litigated here. But Red Team's own Phase-2
and Phase-5 audits, independently and by four/five separate methods, proved
the SUBSTANTIVE question — whether this is the SAME lossless PAD-tied
phase mechanism Iteration 53 characterized on the empty scene, or a
qualitatively different, article-mediated interaction of similar scale —
is **demonstrated, not merely left open, to be unresolvable at 7-point
power**: the free-period-search machinery this whole sub-thread relies on
is proven, via a ground-truth check, to recover the WRONG period (78% off)
for a signal of independently-known period at n=7; a 200,000-trial
null-permutation control shows the observed shape-correlation `R²≈0.86` is
what ~26–27% of pure noise clears at this sample size; the two series' own
best-fit periods diverge 190%; an exact permutation test on the observed
correlation gives `p=0.953`. This cycle exists to remove that power
deficiency, not to re-derive anything already settled.

**This cycle also inherits two genuinely distinct, falsifiable hypotheses**
from exp-082's own Phase-5 layer for what the full-power fit should recover,
both independently confirmed sound by Red Team's own Phase-5 final audit
(`phase5_redteam_audit.md` §4): PHOTONICS' article-edge-diffraction
hypothesis (the flagship article's own `R_OUT/λ=78/20=3.9λ` radius at 600nm
is large enough to present its own diffracting rim, an independent source of
angular structure unrelated to the domain-boundary echo) and QUANTUM's
same-mechanism-phase-shifted hypothesis (the `PAD`-tied wall echo persists,
merely phase-rotated by the article's added path length). Red Team's own
audit ruled these "genuinely distinct and mutually exclusive at the level
that matters — each predicts a DIFFERENT true period... while being
operationally complementary: the SAME already-near-unanimous next experiment
(the full 31-point window) cleanly discriminates between them," and framed
the pre-registration explicitly as a **two- (or three-, including a null
'neither established family' outcome) branch prediction** (§4 of that
audit, verbatim). This cycle pre-registers exactly that three-branch
prediction, verbatim in substance, before running anything.

---

## 1. Mechanism narrative (≤300 words)

T28's `PAIR_PAD` axis (`C40` vs `G40`: identical `ABSORB=40` boundary,
identical geometry, differing only in vacuum-padding round-trip distance)
carries a proven-lossless (Iteration 53), phase-only oscillation on the
**empty** scene with an independently-established true period,
`P=4.611289746337977°` (the full 31-point/0.2° fit, `experiments/077-.../
pad_round_trip_results.json`). exp-082 showed a comparable-scale oscillation
reaches the real, article-loaded Weber-contrast channel
(`ratio=0.6573`, SURVIVES) but could not determine, at 7-point power,
*which* physical story explains it. Two candidate stories, both grounded in
established charter physics from this exact sub-thread, make opposite
predictions about the TRUE period a properly-powered fit should recover:

**(A) Mechanism continuity (QUANTUM, exp-082 Phase 5).** The article
occupies the object window and adds its own scattered field to the
pre-existing PAD-tied boundary echo. Under this bench's confirmed linearity,
the SAME `4.611°`-period wall-echo term is still present in the total field;
observing it through the nonlinear Weber-contrast ratio (which depends on
the *intensity* cross-term between the echo field and the article's own
scattered field) can rotate its apparent phase without changing its period.
Predicts: true `delta_scene(θ)` period near `4.611°`.

**(B) Article-edge diffraction (PHOTONICS, exp-082 Phase 5).** The
flagship article spans `78/20=3.9λ` at 600nm — large enough that its own
rim is a second, independent diffracting edge, structurally unrelated to
the domain's PEC-wall round-trip distance. Predicts: true `delta_scene(θ)`
period near the `≈2.84°` (T28's own original `C80−C40` empty-scene period,
exp-069) or `≈1.9608°` (T21's own established source-taper fringe at 39°)
family — periods with an independent diffractive origin elsewhere in this
program, unrelated to `PAIR_PAD`'s own round-trip distance.

**(C) Neither established family.** The true period lands outside both
20%-tolerance bands — a genuinely new, uncharacterized oscillatory
contributor, not reducible to either known mechanism.

This is instrument-fidelity/generalization work (T1: N/A, §3). Running the
full window is the single experiment that discriminates all three.

---

## 2. Parameter table

| Parameter | Value | Source / justification |
|---|---|---|
| Configs | `C40` (ABSORB=40, PAD=0), `G40` (ABSORB=40, PAD=40) | `dg065.CONFIGS` — `PAIR_PAD`, identical to exp-082's own pair, no new construction |
| Article | `materials.pec_disk(sim, obj_x, obj_y, 30)` + `materials.graded_black_shell(sim, obj_x, obj_y, 30, R_OUT)` | The established flagship absorber — bit-identical to `exp-024/run.py::build("absorber")` and to exp-082's own `build_article()`. Reused verbatim, zero new construction. |
| Article location | `(obj_x, obj_y)` per config — `170,792` (C40) / `210,832` (G40) | `dg065.CONFIGS[key]["obj_x"/"obj_y"]` — same as exp-082 |
| Article radius | `R_OUT=78` cells (`dg065.R_OUT`) | Established bench radius; `78/20=3.9λ` at 600nm (PHOTONICS' own branch-B figure, §1) |
| Wavelength / cpl | 600 nm / 20 | This sub-thread's own established single-λ scope (every T28 cycle since exp-069); the 750/450nm leg is a separately-tracked, seven-cycles-deferred item (Tier 2 item 9, `phase5_redteam_audit.md` §10) — not this cycle's job |
| Angles (full dense window) | `dg069.DENSE_ANGLES` — θ∈{36.0,36.2,...,42.0}°, 31 points, 0.2° step | T28's own established, properly-powered dense window (exp-069 Block DENSE) — ~3.0 periods of the `P≈2.8421°` T28-family fringe, ~6.5 periods of the `P=4.611°` PAD period; the SAME grid exp-076's committed empty-scene `results.json::headline` already covers at all 31 points, enabling a bit-level reproduction check |
| STEPS | 2800 | T28's own established settled value for this exact dense-window geometry at C40/G40 (exp-069 Block DENSE/SETTLE, `dg.STEPS_SETTLE`) — reused, not re-derived; already spot-checked with the article present at STEPS 1400 vs 2800 (exp-082, `rel_dev=9.8×10⁻⁵`) |
| Settling precondition (this cycle) | G40 + article, θ=39°, STEPS 1400 vs 2800 | Repeats exp-082's own single directional spot-check at full-window STEPS — disclosed, not a full R3-grade study (§5) |
| Total new FDTD calls | **125** | 2 configs × 31 angles × 2 legs (empty, scene-with-article) = 124, + 1 settling-precondition call. Budget reasoning: §0a below. |
| Perceptual bar (context only, not gating T1) | `C_thr = gs.c_thr(3.0,0.4,bar="lab") = 0.005` | T2's frozen photopic lab bar, already used throughout this bench |
| EM's companion instrument (new this cycle, zero marginal FDTD) | Persist raw `observer_profile` arrays for both legs, both configs, all 31 angles; `ΔE_article(θ,y) = profile_with(θ,y) − profile_without(θ,y)` | EM's own Phase-5 review (`phase5_review_em.md` §3), adopted by Red Team's audit (§3) as a genuinely new, sound, board-worthy Tier-1 companion instrument — bundled here at zero marginal cost since the profiles are already computed by the same 124 calls |

### 0a. FDTD call budget — full 31-point window chosen, not a coarser compromise

**125 calls, full 31-point/0.2° window, run as originally specified — not
shrunk.** The task brief flagged that 124+ calls at ~60–120s each could run
2–4+ hours if executed serially, and asked for an explicit, disclosed
decision. exp-082's own committed `run_output.txt` gives a direct empirical
basis for this cycle's actual expected wall time, not a guess: 29 calls
(28 main + 1 settling) at `ProcessPoolExecutor(max_workers=4)` completed in
**609.2s total wall time** — i.e. ≈84s of compute per call, but only ≈21s of
*wall time* per call once 4-way parallelism is accounted for
(`609.2s/29≈21s`). This machine has 4 CPUs (`nproc`), matching exp-082's own
`max_workers=4` exactly — no re-tuning needed. Extrapolating linearly:
`125 calls × 21s/call ≈ 2625s ≈ 44 minutes` wall time. That is comfortably
inside a single build, not a multi-hour run — the "2–4+ hours" concern
assumed serial execution, which this harness (inherited unchanged from
exp-082) does not do. **Decision: run the full, properly-powered 31-point/
0.2° window exactly as T28's own established convention (exp-069 Block
DENSE) defines it — no coarsening, no disclosed scope reduction needed.**
This also directly satisfies the task brief's own default preference
("this is genuinely new FDTD... at T28's own established full statistical
power") without trading off against a time budget that, empirically, isn't
binding.

---

## 3. T1 escape route

**N/A.** Matches every T28 cycle's own disposition since exp-069: this is
instrument-fidelity/generalization work on an already-characterized
boundary-artifact channel, not a constraint-3 mechanism candidate. No
scored contrast in this cycle is presented as evidence for or against any
phenomenon-program escape route.

## 3b. R6 applicability (synthetic ground-truth recovery gate)

**Does not apply — reasoned through for this specific use, not cited by
precedent alone.** R6's text binds "any future estimator that conditions on
a fitted carrier- or phase-conditioned coefficient" — adopted at Iteration
49 specifically because exp-072's differential/beat-fit estimator fit a
carrier phase (`_amp_phase_at`) and then used THAT fitted phase to rotate a
DOWNSTREAM coefficient (`R_q`), a construction where a sign/rotation bug in
the phase step silently corrupted every published number and was invisible
to every rotation-invariant check the cycle ran. Three structural reasons
this cycle's own use of `_free_period_search`/`free_period_with_widening`
does not match that shape, not merely that the code is old:

1. **No downstream conditioned coefficient.** This cycle's free-period fit
   produces exactly two numbers per series — `P*` (the recovered period)
   and `R²` (the fit quality) — and BOTH are the final, directly-reported,
   directly-compared-to-pre-registered-bands quantities. Nothing further is
   computed FROM `P*` that could silently inherit a hidden sign/rotation
   error the way `R_q` inherited exp-072's carrier-phase bug. There is no
   analog of R6's specific failure mode (a nuisance parameter silently
   rotating a *different*, load-bearing coefficient) here.
2. **Not new machinery.** `_free_period_search`/`_fixed_period_fit`
   (exp-069) and `free_period_with_widening` (exp-077, wrapping the same
   core fit with staged-widening) are the SAME functions this entire T28
   sub-thread has used, unmodified, as its primary period-scoring
   instrument since Iteration 46 — including as the instrument that
   PRODUCED T28's own original discovery period (`P*=2.8421°`, exp-069) and
   `PAIR_PAD`'s own established period (`P=4.611°`, exp-077). If this
   machinery needed an R6-style ground-truth gate, that gap would have
   applied retroactively to every headline period this program has ever
   cited from it — it was not flagged at Iteration 49, 50, or since,
   because it is not the failure class R6 targets.
3. **A ground-truth check has, in fact, already been run on this exact
   machinery** — a stronger due-diligence step than R6 itself requires, and
   one that already produced this cycle's own operative caution. Red Team's
   Phase-2 audit of exp-082 (`phase2_redteam_audit.md` §0j) fed this SAME
   `free_period_with_widening` function a signal of independently-known
   true period (`delta_empty`'s own 7-point reduction, ground truth
   `P=4.611°` from the full 31-point fit) and found it recovers `P=1.015°`
   — an *instrument-power* finding (the machinery needs more points to
   resolve a period correctly), not a *sign/coefficient-conditioning* defect
   R6 exists to catch. Running the SAME machinery at n=31 — the window
   width it has always been calibrated and validated against (exp-069's own
   original 31-point/0.2° design, ~3 periods of the target fringe) — is
   exactly the regime the ground-truth check already showed this instrument
   needs, not an under-tested regime requiring a fresh synthetic gate.

**Conclusion: R6 does not apply.** The gate that DOES apply and IS run this
cycle is the reproduction precondition (§4) — the R4-family discipline this
whole program uses in place of a synthetic-recovery gate whenever the
underlying machinery, not a newly-fitted coefficient, is what's being
re-exercised on new data.

## 3c. New machinery / trust-suite gate

**None added.** Every primitive reused is already gated: `lab.Sim` (core
engine, suite stages 1-6), `lab.materials.graded_black_shell`/`pec_disk`
(stage 7), `lab.ambient.observer_profile`/`contrast_from_runs`/
`window_means` (stage 9), `lab.sections.full_capture`/`phasors` (core).
`dg065.CONFIGS`/`dg069.DENSE_ANGLES` are established, reused geometry and
angle grids — zero new construction. `_free_period_search`/
`free_period_with_widening` (exp-069/exp-077) are reused verbatim, not
modified. `git diff --stat -- lab/` is verified empty both before and after
this cycle's work (confirmed §0, run script; re-confirmed post-run, §7).
No new suite stage is added; none is required.

---

## 4. Predictions — pre-registered falsifiable bands (committed BEFORE the run)

### 4a. PRIMARY: the three-branch period discriminator (PHOTONICS' own spec, verbatim in substance)

For each of the 31 angles, compute real Weber contrast `C(G40;θ) −
C(C40;θ)` (scene, article present) — `delta_scene(θ)`. Apply
`free_period_with_widening(thetas, delta_scene, label)` (exp-077's own
staged-widening wrapper around `_free_period_search`, center_deg=39.0,
stages `[1,4]→[1,15]→[1,60]°`, unmodified) to recover the TRUE free period
`P*` and its `R²`. Reference periods, each sourced from an already-committed
full-power fit (never hand-typed, copied from the cited JSON fields):

- `P_continuity = 4.611289746337977°` (`experiments/077-.../
  pad_round_trip_results.json::test_a_pair_pad.real.chosen.p_star_deg` —
  `PAIR_PAD`'s own true, full 31-point/0.2° empty-scene period)
- `P_edge_A = 2.8421052631578947°` (`experiments/069-.../results.json::
  scored.p3.p_star_deg` — T28's own original `C80−C40` full-power period)
- `P_edge_B = 1.9607950099405438°` (`experiments/069-.../results.json::
  scored.p3.P39_600` — T21's own established source-taper fringe at 39°)

Classification (the sub-thread's own established `rel_dev≤0.20` AND
`R²≥0.30` "within tolerance" convention — exp-069 P-069-3, exp-077 Test A,
unmodified). *(Phase 3 note: branch (B)'s original working name,
"ARTICLE-EDGE DIFFRACTION," is retained below only as the classification
bucket's label; see the "PHASE 1 RESULTS" section for the Phase 2/3-corrected
reading of what a match to this bucket does and does not establish.)*

- **(A) MECHANISM CONTINUITY**: `|P*−P_continuity|/P_continuity ≤ 0.20` AND
  `R² ≥ 0.30`.
- **(B) ARTICLE-EDGE DIFFRACTION** *(bucket label; see Phase 3 correction
  below)*: `R² ≥ 0.30` AND (`|P*−P_edge_A|/P_edge_A
  ≤ 0.20` OR `|P*−P_edge_B|/P_edge_B ≤ 0.20`) — either member of the
  established T21/T28 family counts as this branch (PHOTONICS' own
  Phase-5 framing groups them as one family, not two separate hypotheses).
- **(C) NEITHER ESTABLISHED FAMILY**: `R² < 0.30`, OR `R² ≥ 0.30` but `P*`
  clears none of the three 20%-tolerance bands above.

(The three ±20% bands around `4.611°`/`2.842°`/`1.961°` are mutually
non-overlapping with branch (A) — the closest gap, `2.842°`'s upper band
edge `3.411°` to `4.611°`'s lower band edge `3.689°`, has a clean 0.278°
margin — so no angle assignment ambiguity between (A) and (B) is possible
by construction.)

### 4b. Companion: EM's field-difference decomposition (bundled, complementary — not a substitute)

Persist the raw `observer_profile(θ,y)` array for BOTH legs (`with_article`,
`without_article`) at BOTH configs (`C40`, `G40`), all 31 angles — a
one-line harness change, zero marginal FDTD cost (EM's own proposal,
`phase5_review_em.md` §3; adopted by Red Team's audit §3). This bench is
confirmed fully linear at 600nm (no `σ(I)`, no time-varying `ε` anywhere in
`build_article`/`Sim` — reused unchanged from exp-082), licensing an EXACT
field-level decomposition `E_total(θ) ≡ E_no-article(θ) + ΔE_article(θ)`.
Compute, per config `k∈{C40,G40}`:

```
ΔE_article_k(θ, y) = profile_with(k,θ,y) − profile_without(k,θ,y)
ΔE_obj_article_k(θ) = window_means(ΔE_article_k(θ,·), y_lo, obj_y, W_OBJ, GUARD_OUT, W_FLANK)[0]   # object-window mean
```

then apply the SAME `free_period_with_widening` to `ΔE_obj_article_C40(θ)`,
`ΔE_obj_article_G40(θ)`, and their cross-config pair
`ΔΔE_obj_article_PAD(θ) = ΔE_obj_article_G40(θ) − ΔE_obj_article_C40(θ)`
(the field-level analog of `delta_scene`), reporting `P*`/`R²` for all
three against the same reference periods (§4a). **No pre-registered
pass/fail band for this companion instrument** — Red Team's own audit
(§3) ruled it "asymmetrically informative": a clean negative (no period
near `4.611°` in `ΔE_article`) does NOT by itself settle the
intensity-level question (the nonlinear cross-term `2·Re(E_no-article·
E_scattered*)` can still carry PAD-tied structure through `E_no-article`'s
own phase even if `ΔE_article` alone does not), while a clean positive
WOULD be strong, direct evidence for continuity. Logged explicitly,
per that ruling, as complementary to §4a's own primary test, never a
substitute for it — disclosed, not gating.

### 4c. Secondary, disclosed-not-gating diagnostics (recomputed at full power)

- **Amplitude-ratio consistency check**: `ratio = A_scene/A_empty` (same
  construction as exp-082's own primary metric, now over all 31 points) —
  reported for direct comparability to exp-082's own `0.6573`, not
  re-gated (that verdict is already settled).
- **Shape correlation** `r(delta_scene, delta_empty)` at n=31, with an
  exact-or-large-sample permutation test — the same diagnostic Red Team's
  audit showed was structurally underpowered at n=7 (`p=0.953` there);
  reported here with real statistical power for the first time, context
  only, not a gating threshold (the branch-A/B/C classification in §4a is
  the pre-registered discriminator).
- `A_scene / C_thr` (context only, mirrors exp-082's own R9-corrected
  convention: compare only like-normalized quantities).

### 4d. Reproduction precondition (must PASS before any new-leg number is trusted)

This cycle's own freshly-run empty leg at all 31 `dg069.DENSE_ANGLES` must
reproduce `experiments/076-.../results.json::headline`'s `C40`/`G40` values
at those same angles to float precision (`max|Δ| < 1e-9`) — the identical
R4-discipline bar exp-082 already cleared at 7 points (`max_dev=0.0`), now
extended to the full 31-point grid.

### 4e. Settling precondition (disclosed, not gating)

`|C(G40, θ=39°, article, STEPS=2800) − C(G40, θ=39°, article, STEPS=1400)|`
reported for context — repeats exp-082's own spot-check exactly (which read
`rel_dev=9.8×10⁻⁵` there); no new pre-registered threshold, since this
remains a single directional check, not the full R3-grade convergence study
(Tier 2 item 12, still open, not this cycle's job — disclosed limitation,
§5).

---

## 5. Idealizations

1. **Single wavelength (600 nm)** — matches this entire sub-thread's own
   scope since exp-069; the 750/450nm x-wall leg is separately tracked,
   now seven cycles deferred (Tier 2 item 9), not this cycle's job.
2. **One pair only (`PAIR_PAD`, C40 vs G40)** — the dominant, headline
   confound. `PAIR_ABSORB40`/`C80−C40` extension (Tier 1 item 8) is not
   re-tested this cycle.
3. **Single settling-precondition spot-check, not a full R3-grade
   convergence study** — repeats, not extends, exp-082's own disclosed
   limitation (Tier 2 item 12, 2 of 14 config×angle cells tested to date
   across both cycles combined).
4. **The established flagship absorber only** — the near-null σ(I) article
   follow-up (`off_pass`, Tier 1 item 6) is not re-tested here; a separate,
   already-queued board item.
5. **EM's field-difference decomposition is a companion, not a substitute**
   — explicitly disclosed, §4b; a clean null on `ΔE_article` does not by
   itself resolve the mechanism-identity question the way a positive result
   would (Red Team's own asymmetry ruling, adopted verbatim).
6. **Interception/energy-budget accounting remains out of scope** — this
   cycle measures the OBSERVED contrast/field delta directly (an FDTD
   measurement); THERMODYNAMICS'/EM's own joint energy-interception
   cross-check (Tier 0 item 2, zero-FDTD, post-run analytic) is a separate,
   already-queued board item, not folded into this build. **Phase 2/3
   re-scope (Red Team's Attack 4, adopted in full):** `P_edge_A`'s own
   physical origin — under ANY reading, article-intrinsic (Branch B, per
   this cycle) or a pre-existing domain/source artifact — has never been
   shown non-dissipative. This is a pre-existing, broader gap in the
   founding periodicity's own characterization; this cycle's own Branch-B
   language doesn't specifically create or worsen it, only makes it newly
   live because it is, for the first time, scored on a channel with a real
   absorbing article present.
7. **The three-branch classification assumes the true period is
   well-separated and single-valued** — if the recovered `P*` reflects a
   genuine SUPERPOSITION of both mechanisms (a real possibility PHOTONICS'
   own review does not rule out), a single dominant `P*` from one free-period
   fit may not cleanly separate them; disclosed here, not solved — a
   two-tone fit is a natural but out-of-scope follow-up if branch (C) fires
   with a high-`R²`-but-unstable-`P*` signature.

---

## PHASE 1 RESULTS (self-scored, numbers copied from `results.json`/`run_output.txt`/`null_permutation_control.json`, never hand-typed)

**125/125 FDTD calls completed, 1829.5s wall time** (≈30.5 min — faster than
the §0a estimate of ≈44 min; 4-way parallelism held throughout).

### Preconditions

- **Reproduction precondition: PASSED, bit-exact.** Fresh 31-point empty leg
  vs `experiments/076-.../results.json::headline` — `max_dev = 0.0` at every
  one of the 31 shared angles (not merely `<1e-9`; literally exact). The
  article-loaded leg is trusted.
- **Settling precondition (disclosed, not gating): `rel_dev = 9.81×10⁻⁵`** —
  bit-identical to exp-082's own reading at the same cell (`G40, θ=39°`),
  since this is the same STEPS=2800-vs-1400 comparison, now re-confirmed at
  the full window's own settled step count. No evidence STEPS=2800 is
  insufficient with the article present.

### PRIMARY: the three-branch period discriminator — **BRANCH B: matches T28's own long-standing, unexplained `P_edge_A` family**

```
delta_scene(theta) free-period fit (narrow[1,4]deg stage, interior optimum):
  P* = 2.9474 deg    R^2 = 0.8582
  rel_dev vs P_continuity (4.6113deg) = 0.361   [outside 20% band]
  rel_dev vs P_edge_A     (2.8421deg) = 0.037   [WELL INSIDE 20% band]
  rel_dev vs P_edge_B     (1.9608deg) = 0.503   [outside 20% band]
BRANCH: B_ARTICLE_EDGE_DIFFRACTION
```

This is not a close call: `P*` sits at 3.7% relative deviation from
`P_edge_A`, an order of magnitude inside the pre-registered 20% tolerance,
and 36%/50% away from the other two bands — no boundary ambiguity. `R²=0.858`
clears the pre-registered `≥0.30` floor by a wide margin.

**Post-hoc due diligence, run at self-scoring time (not pre-registered,
disclosed as such): a 20,000-trial null-permutation control**, shuffling
`delta_scene`'s own 31 values and re-running the identical
`_free_period_search` on each shuffle (zero new FDTD, pure desk compute,
reusing the sub-thread's own established null-control idiom, exp-069/072/077
precedent):

```
null-permutation control on delta_scene, n_trials=20000:
  R^2_observed = 0.8582
  null distribution: mean=0.192  p95=0.335  p99=0.420  MAX=0.632
  p_value = 0.0  (0/20000 permutations reached R^2>=0.8582)
```

**The observed `R²=0.858` exceeds the MAXIMUM achieved by 20,000 pure-noise
permutations of this exact data on this exact instrument** — not merely a
significant p-value, but entirely outside the null distribution's own
observed range. This directly answers the look-elsewhere concern R5's own
family of house rules exists to raise (a free-period search over ~400
candidate periods CAN inflate apparent fit quality by chance): here it
demonstrably does not explain this result. Separately: the pre-registered
`R²≥0.30` floor itself sits close to this null distribution's own 90–95th
percentile (`p95=0.335`) — a real, disclosed finding that the inherited
threshold is only moderately conservative in isolation, which is exactly why
this post-hoc null control matters and is not redundant with the
pre-registered gate.

**PHASE 2/3 CORRECTION (Red Team's Attack 1, adopted in full — replaces
every "ARTICLE-EDGE DIFFRACTION, confirmed/decisively" reading below and
elsewhere in this cycle's record).** The period-family match above is a
real, decisive, null-controlled statistical finding and is NOT retracted —
independently reproduced at minimum four times (this committed run,
QUANTUM's blind critique, EM's blind critique, Red Team's own audit). But
"ARTICLE-EDGE DIFFRACTION, confirmed" overstates what a period-family match
demonstrates. The corrected reading:

**Branch B matches T28's own long-standing, unexplained `P_edge_A`
family — period-family membership, statistically decisive and
null-controlled (`R²=0.858`, clears a 20,000-trial null with `p=0.0`), NOT
yet demonstrated to be article-intrinsic.**

Two lines of evidence, both independently computed by Red Team's own
Phase-2 audit (`phase2_redteam_audit.md` §0c–0d), drive this correction:

1. PHOTONICS' own far-field two-rim-edge estimate (`Δy=2·R_OUT=156` cells,
   `λ=20` cells at 600nm, `θ=39°`) gives `Δθ=λ/(Δy·cosθ)=9.4520°` —
   independently reconfirmed by Red Team to the same figure — a **3.3×
   miss** against the recovered period (`9.45°` vs `P_edge_A=2.84°`).
2. This aperture's own Fresnel number is `N_F=Δy²/(λ·lever)=156²/(20·93)
   ≈13.08` — deep in the near-field/Fresnel regime, not the far-field
   regime the two-slit formula assumes (independently established
   elsewhere in this sub-thread, Iteration 56/exp-079). So the miss is not
   simply "the mechanism predicts the wrong number" — the formula applied
   is not even the correct one for this geometry's regime. This makes the
   causal question an **untested regime**, not a clean refutation of a
   rim-diffraction origin — but equally, no correct first-principles
   derivation of `P_edge_A` from the article's own geometry exists yet, for
   either candidate story.

`P_edge_A=2.8421°` is T28's own founding, still-unexplained periodicity
from the empty scene (exp-069) — nine-plus dedicated mechanism-search
cycles have tested and refuted or structurally foreclosed every domain-echo
candidate for it, and nobody has ever derived it from geometry. Landing on
it specifically therefore most plausibly means the article-loaded channel
inherited the SAME unexplained artifact the empty scene already produces —
not that a new article-rim mechanism was discovered and confirmed.

**MATERIALS' article-radius discriminator — an `R_OUT` sweep at fixed
`PAD`, re-running the identical `PAIR_PAD` harness at an alternate article
radius and checking whether `P*` tracks `R_OUT/λ` (genuine article-rim
origin) or stays pinned (pre-existing domain/source artifact merely
becoming visible) — is now this sub-thread's single highest-priority item
for Iteration 61**, sharpened by this correction: it is the only test that
can move Branch B from a period-family match to a demonstrated causal
claim, in either direction.

### COMPANION: EM's field-difference decomposition — independently corroborates the SAME period family (Branch B bucket)

```
DeltaE_obj_article_C40 (article - no-article, C40 alone):  P*=3.0226deg R^2=0.1977  -> below R^2 floor, C (uninformative alone)
DeltaE_obj_article_G40 (article - no-article, G40 alone):  P*=2.9098deg R^2=0.2550  -> below R^2 floor, C (uninformative alone)
DeltaDeltaE_obj_article_PAD (G40-C40, the field-level PAIR_PAD analog):
  P*=2.5865deg  R^2=0.4582  rel_dev vs P_edge_A=0.090 [inside 20% band]  -> BRANCH B
```

Each single-config field-level decomposition, alone, is too weak to classify
(`R²<0.30`) — a real, disclosed limitation, not swept aside. But the
**cross-config pair** — the field-level construction that mirrors T28's own
established practice of always scoring `PAIR_PAD` as a *difference*, never a
single config, because that is what cancels the shared, non-PAD-dependent
`E_direct` term (PHOTONICS' own exp-080 Phase-5 proof) — independently
recovers a period in the SAME family as the primary test (`2.59°` vs the
primary's `2.95°`, both within 20% of `P_edge_A=2.84°`, though not identical
to each other; disclosed, §5 idealization 7's own caveat about
superposition/precision remains open). **A second null-permutation control on
this exact series**: `R²_observed=0.4582`, null distribution
`mean=0.190, p95=0.325, p99=0.399, max=0.560`, **p=0.00185** (37/20,000) —
also decisively clears its own null, though with less extreme margin than
the primary test's `p=0.0`.

**Two structurally different instruments — the established nonlinear
Weber-contrast pair-fit (delta_scene) and EM's new linear field-difference
pair-fit (DeltaDeltaE_obj_article_PAD) — independently land in the SAME
branch, each clearing its own fresh null-permutation control.** This is
materially stronger corroboration than either alone, and is new evidence
this cycle produced, not assumed.

### Secondary, disclosed-not-gating diagnostics

```
Amplitude-ratio consistency: A_scene=3.811e-3  A_empty=5.262e-3  ratio=0.7243  SURVIVES
  (same direction/magnitude as exp-082's own n=7 reading, ratio=0.6573 -- consistent, not re-litigated)
A_scene / C_thr = 0.7622  (C_thr=0.005; context only, R9-consistent normalization)
delta_empty own free-period fit (context): P* = 4.611289746337977deg, R^2=0.8165
  -- IDENTICAL to P_continuity to full float precision. This is a NECESSARY
  consequence of the reproduction precondition (this leg is bit-exact to
  exp-076's own committed data, from which P_continuity was itself derived
  via the identical fitting function) -- a harness-correctness confirmation,
  not new independent evidence. Correctly read as a sanity check, not a
  finding.
Pearson r(delta_scene, delta_empty) @ n=31: r_obs = 0.3949, p = 0.02806 (200,000-trial permutation)
```

**Honest discussion of the correlation figure, since it is the one number
this cycle produced that is in some tension with the primary branch
classification.** At n=7 (exp-082), `r≈0.031, p=0.953` was read as
uninformative. At n=31, `r=0.395` is a real, MODEST, nominally-significant
positive correlation between `delta_scene` and `delta_empty` — a genuinely
different reading, not merely "more of the same." Two honest cautions
against over-reading it as evidence for mechanism continuity, weighed
against the primary result:

1. **This was pre-registered explicitly as disclosed-not-gating context**
   (§4c), decided BEFORE the run — the correct discipline, since the
   primary, gating discriminator (the free-period fit, §4a) is a sharper,
   pre-committed test of the same underlying question and it resolves
   cleanly in favor of Branch B.
2. **Multiple-comparisons caution, stated explicitly, not smoothed over.**
   This cycle computed several non-trivial statistics (the primary 3-branch
   classification, this correlation/p-value, and three EM-companion branch
   classifications). Read in isolation at the nominal `α=0.05`, `p=0.02806`
   looks significant; under even a simple Bonferroni correction across this
   cycle's ~5 headline-adjacent tests (`α_corrected≈0.01`), it would NOT
   clear the bar. Since it was pre-registered as non-gating precisely to
   avoid leaning on it either way, this is disclosed as an open, unresolved
   tension, not adjudicated here.
3. **A plausible, charter-neutral explanation for a modest nonzero
   correlation between two DIFFERENT-period series over a short window**:
   `delta_scene`'s `P*=2.95°` and `delta_empty`'s `P*=4.61°` are not harmonics
   of each other, but over a 6°-wide window (≈2.0 and ≈1.3 periods
   respectively) two moderately-different-frequency sinusoids are not fully
   orthogonal — a data-free leakage argument in the same family as this
   sub-thread's own established `L(T)` leakage-budget finding (exp-072/074).
   A modest correlation between two now-independently-well-determined but
   DIFFERENT periods is not, by itself, evidence they share a mechanism.

**This tension is real and not resolved by this cycle** — flagged
explicitly as an open item for Phase 2/5, not swept into either the SUPPORT
or REFUTE column.

### PHASE 2/3 UPDATE — the two-tone admixture question: tested, and reversed under the correct null (Red Team's Attack 2, adopted in full)

This tension did not stay unexamined through Phase 2. QUANTUM's and EM's
blind critiques both independently built a two-tone fit (`delta_scene`
against BOTH `P_edge_A` and `P_continuity` simultaneously, periods FIXED,
no free search — correctly avoiding R5's look-elsewhere concern) and found
a large, apparently significant improvement over the single-tone model:
`R²: 0.845→0.958` (QUANTUM), and, using this program's own established
Freedman-Lane residual-permutation convention (R6's Iteration-50 addendum),
`p<0.001` across three baselines (EM), corroborated in EM's own linear
field-difference companion (`p=0.00018`). Read at face value this looked
like a resolved, quantified finding: genuine partial admixture of the
`P_continuity` mechanism at 34–77% relative amplitude, riding underneath
the dominant `P_edge_A` term.

**It is NOT resolved, and this record does not adopt that reading.** Red
Team's own Phase-2 audit found that both critiques share a genuine,
independently-demonstrated methodological blind spot: the Freedman-Lane
test assumes exchangeable residuals, and the single-tone residuals
underlying this exact construction are highly autocorrelated — lag-1
`r≈0.9508` (`delta_scene`), `r≈0.9355` (EM's own field-difference pair) —
matching a previously-documented exp-074 pattern ("shared curvature
misspecification," Iteration 51), not i.i.d. noise. A from-scratch
synthetic Monte Carlo confirmed the Freedman-Lane method is correctly
calibrated WHEN residuals are genuinely i.i.d. (empirical false-positive
rate matches the nominal `α` almost exactly at every level tested) — the
method itself is sound in the abstract; it is misapplied here. Running the
order-preserving circular-shift companion — the harder, autocorrelation-
respecting null this program's own R6/R7 addenda establish for exactly this
situation — **reverses the verdict**: for `delta_scene`, the observed
`F=33.39` sits BELOW the median of its own 31 possible circular shifts
(`p=0.581`); for EM's own field-difference companion, `p=0.097` — neither
significant at any conventional threshold.

**The corrected reading, replacing "resolved... genuine partial admixture,
p<0.001" wherever it would otherwise be inherited:** the two-tone
correlation tension (`r=0.395, p=0.028` raw, at n=31) is a real, disclosed
question that is NOT yet resolved, in either direction. The naive
Freedman-Lane full-permutation test found it highly significant
(`p<0.001`); the correct, order-preserving circular-shift companion test
reverses that finding (`p=0.581` for the primary `delta_scene` series,
`p=0.097` for EM's own field-difference companion) once the residuals' own
extreme autocorrelation is respected instead of destroyed by full
permutation. This is now an open question requiring a properly
PRE-REGISTERED null-calibration test (matching R6's own Iteration-50
addendum standard — a synthetic-recovery gate run BEFORE the test is
trusted, not after) at Iteration 61, not a settled finding either way.

### Combined self-score (Phase 3 corrected, Iteration 60 synthesis)

**The pre-registered PRIMARY discriminator resolves decisively to BRANCH B
— a period-family match to T28's own long-standing, unexplained `P_edge_A`
family, statistically decisive and null-controlled — not Branch A
(QUANTUM's mechanism-continuity hypothesis) and not Branch C (neither
family).** This is the single test PHOTONICS' and Red Team's own Phase-5
audit of exp-082 specified as decisive, and it decides cleanly, with a
freshly-run null-permutation control (not merely the inherited threshold)
showing the result is far outside what pure noise produces on this exact
instrument. EM's own field-difference companion, run at zero marginal FDTD
cost, independently corroborates the SAME period family via a structurally
different (linear, not Weber-contrast) construction, itself passing its own
fresh null-permutation control. **This resolves, for the first time in this
nine-cycle-plus T28 sub-thread, WHICH established period family the
article-loaded channel's dominant periodicity belongs to** — not by
asserting more statistical power in the abstract, but by actually running
the pre-specified discriminating test and getting an unambiguous,
doubly-corroborated, null-controlled answer. **It does NOT resolve WHETHER
that period family is caused by the article's own rim** (Red Team's Attack
1): PHOTONICS' own far-field two-rim estimate misses the recovered period
by 3.3× (`9.45°` vs `2.84°`), and this aperture's own Fresnel number
(`≈13`) means the far-field formula PHOTONICS applied is not even the right
one for this near-field geometry — an untested regime, not a demonstrated
rim-diffraction mechanism. MATERIALS' article-radius discriminator is the
single highest-priority Iteration-61 item to close this gap.

**What this does NOT establish, stated explicitly, not overclaimed:**
Branch B being selected does not mean `PAD`'s own empty-scene mechanism
(Iteration 53's proven-lossless phase effect) is irrelevant to the
article-loaded channel. The correlation tension (`r=0.395, p=0.028`) is a
real, disclosed, NOT-yet-resolved question — Phase 2's own two-tone tests
(QUANTUM, EM) found an apparently significant `PAD`-continuity admixture
under a full-permutation Freedman-Lane null (`p<0.001`), but Red Team's own
independent verification found the underlying residuals are highly
autocorrelated (lag-1 `r≈0.93–0.95`), invalidating that null's own
exchangeability assumption, and the correct order-preserving circular-shift
companion test REVERSES the finding (`p=0.581` primary series, `p=0.097` EM
field-difference companion). This is now an open question requiring a
properly pre-registered null-calibration test (R6's own Iteration-50-
addendum standard) at Iteration 61, not settled either way by this cycle.
The two individually-inconclusive EM single-config fits (`R²<0.30` each)
mean this cycle cannot yet say HOW MUCH of each config's own field response
the `P_edge_A`-family term explains in isolation — only that the
cross-config difference, which is what T28's own scoring has always used,
carries a `2.84°`-family signature that survives a null control. `T1: N/A`
throughout — no constraint-3 claim is made or implied by any number in this
section.
