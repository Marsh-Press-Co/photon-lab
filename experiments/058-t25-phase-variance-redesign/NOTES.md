# exp-058 — QUANTUM OPTICS' Phase-Variance Redesign (T25)

Panel Iteration 35. Lead: **QUANTUM OPTICS**, LOCKED, unconditional,
breaking rotation (Red Team's Iteration-33 Phase-5 ruling: "if not built
at Iteration 34, it becomes a LOCKED, unconditional, non-competing
trigger for Iteration 35" — fired at Iteration 34's close since that
cycle was consumed by the separately-LOCKED `graded_black_shell_flagship`
fix). Full seven-seat cycle: Phase 1 proposal (QUANTUM OPTICS, second
dispatch — the first attempt was independently terminated mid-read by
the same upstream `[bio]`-tagged content-policy false positive this
program has now hit five times, Iterations 30/34/35; retried once,
unreworded, per Iteration-30's own precedent, and completed cleanly) →
five blind parallel critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, VISION SCIENCE — all support-with-changes, zero opposes,
though EM's and THERMODYNAMICS' fixes were each explicitly conditional
— "would move to/toward oppose without the fix") → Red Team last with
everything (verdict: PROCEED-WITH-MANDATORY-FIXES, 5-item docket,
load-bearing catch: `_STAGE_IDS` was never bumped for stage 20 — the
identical bug species this program has hit three times before,
Iterations 15/17/23 — caught before first light) → this Phase-3
synthesis, which also carries a Director's-own catch (below) discovered
by direct execution, not by reading.

## Hypothesis

Not a mechanism proposal — pure diagnostic/instrumentation work, same
register as Iterations 2/4/5/6/20/22/25/26/27/29/31/32/33. **T25**
(opened Iteration 29, sharpened Iteration 32/33 into **T26**): every
constraint-3 `C` citation this program has ever issued rests on
`lab/ambient.py`'s INCOHERENT sum — 9 separate single-source runs
combined post-hoc as intensities. Iteration 6 proved analytically that
the TRUE random-phase incoherent-ensemble limit has exactly zero mean
cross-term, but the only real-instrument test of the actual coherent
joint-injection apparatus (exp-055/056, T26) measured exactly **one**
realization — fixed, all-zero relative phase — and found a large
artifact (11.1–11.6× VISION's T2 photopic `C_thr`) on `off_pass`/
`off_bracket`, this program's only-ever constraint-3 PASS/near-PASS
territory. This cycle finally measures the **variance** across genuine
random-phase draws — is that one fixed-phase draw typical, or an
outlier? — via new disk-persisted per-angle machinery that makes N=2000
draws per article cost zero marginal FDTD.

## Setup

**Native geometry (r=78)**: exp-024/032/055/056's own fallback bench,
reused verbatim — NX=360, NY=1584, OBJ=(170,792), SRC_X=300,
ABSORB=TAPER=40, W_OBJ=GUARD_OUT=W_FLANK=78/185/78, PLANE_X=77 (dx=15),
cpl=20, λ=600nm, courant=0.99, STEPS=1400. **Articles**: `off_pass`
(τ=0.0065, this program's only-ever constraint-3 PASS), `off_bracket`
(τ=0.003) — exp-032/033's own construction, no PEC core, unchanged.

**20 NEW native FDTD calls**: 9 individual-angle legs × 2 articles = 18
(each captured, persisted to disk via `lab/phase_lines.py`, reloaded) +
1 noise-floor validation leg × 2 articles = 2 (a fixed, seeded nonzero
relative-phase joint run, Director's own Phase-3 addition — see below).
Full design: `design_geometry.py`.

## New suite machinery (built and validated this cycle, before exp-058's
own run.py)

`lab/fdtd2d.py`'s `Sim.add_line_source` gains `rel_phase` (radians,
default 0.0): a constant additive phase offset on top of the existing
`angle_deg` geometric ramp. Backward-compatible at every existing call
site (`rel_phase=0.0` is bit-exact identical to pre-Iteration-35
behavior — confirmed by the full trust suite staying 61/61 green,
including all 59 pre-existing checks unchanged). New module
`lab/phase_lines.py`: persists a single-source leg's Ez/Hy phasor on a
fixed observation line (pre-interpolated, matching
`sections.flux_profile_x`'s own convention), and reconstructs ANY
relative-phase draw across N legs post-hoc via
`F(δ)=F(0)·e^{+iδ}` (independently re-derived THREE separate ways at
Phase 2 — PHOTONICS, ELECTROMAGNETISM, Red Team — identical sign/factor
every time, from `emit._phasor`'s stated `f(n)=Re{Fe^{-iωn}}`
convention). New trust-suite **stage 20**
(`stage20_disk_persisted_phase_reconstruction`), small canonical bench
(reusing stage 19's own geometry): **Q7** (zero relative phase,
disk-persisted 9-leg reconstruction vs a real joint Sim call) measured
**1.84×10⁻¹⁵** against a ≤1e-6 bar — a pure additivity identity, same
species as stage 11/19, exact regardless of settling. **Q8** (an
arbitrary nonzero relative-phase draw, same comparison, with `rel_phase`
genuinely injected into the reference joint Sim) measured **1.45×10⁻⁵**
— NOT machine-epsilon like Q7, because the `e^{+iδ}` law is exact only
for the periodic steady-state part of the response (proven via an exact
real-quadrature decomposition, `sin(ωn−φ−δ)=cos(δ)·sin(ωn−φ)−sin(δ)·
cos(ωn−φ)`, itself exact at every step including the turn-on transient
— but the single captured phasor this reconstruction actually uses
implicitly assumes a never-separately-measured companion cosine-drive
response has ALSO already reached steady state). Gate recalibrated,
first-light convention: **≤3e-5**, ~2× margin above the measured value.
Full existing bench reverified **61/61** (`--only
12346789,10,11,18,19,20`) before this cycle's own experiment run.

### Director's own Phase-3 catch (not raised by any Phase-2 seat or Red Team)

Stage 20's canonical bench uses a STRONGLY lossy object (`sigma_max=0.5`)
— material loss is what damps a source's turn-on transient, and Q8's
residual is exactly that undecayed transient leaking through. Direct
measurement on `off_pass`'s own native geometry (τ=0.0065, ~10,000×
less lossy than stage 20's bench) at STEPS=1400, one representative
nonzero-δ draw, found the SAME reconstruction technique's field-relative
RMS residual is **~100× larger** than on stage 20's bench at a
comparable step count (1.06×10⁻³ field-relative vs stage 20's 1.45×10⁻⁵)
— consistent with the mechanism (weaker material loss ⇒ slower transient
decay), not a new bug (confirmed by an independent N=1, single-source
check on the SAME canonical bench, which shows the identical geometric
convergence with settling: 5.08e-5/1.37e-5/3.56e-6 at 900/1800/3600
steps). **But translated into the units that actually matter — Weber
`C`, not raw field RMS — the same one-draw check measured only
1.24×10⁻⁴ absolute `C`-units of reconstruction error** (window-averaging
over 78–156 cells substantially, though not perfectly, damps the
field-level residual) — **2.5% of `C_thr`=0.005**, small relative to the
predicted `C` spread. Rather than brute-force ~40× more FDTD steps (a
multi-hour cost, extrapolated from the observed geometric convergence
rate, this cycle does not need) or silently trust an untested
assumption, this is measured directly, disclosed, and gated: **exp-058
carries its own empirical noise-floor validation leg per article** (one
extra native FDTD call each, `NOISE_FLOOR_SEED`), scored against
**P-058-NF** below. STEPS is kept at exp-056's established 1400 (not
increased) — the Director's Phase-3 call, contingent on P-058-NF's own
disposition. New "Measurement lesson" line queued for
`lab/validation/VALIDATION.md` at Phase 5 close (not touched here — see
Next).

## Phase 3 — accepted / overridden (Director's synthesis)

Red Team's verdict: **PROCEED-WITH-MANDATORY-FIXES**, 5-item docket, all
five accepted in full (no overrides):

1. **[Red Team, load-bearing catch]** `_STAGE_IDS` bumped to
   `range(1,21)` in `lab/validation/run_all.py` BEFORE stage 20 was
   wired — verified directly: `_stage_selected(2, "20")` would otherwise
   have silently also fired stage 2 (the identical bug species this
   program has hit three times before, Iterations 15/17/23). Confirmed
   fixed by the full 61/61 bench run using `--only
   12346789,10,11,18,19,20` as its own token.
2. **[Red Team]** The Phase-2 docket is tiered explicitly, not flattened:
   **MANDATORY** — EM's per-draw flank-denominator diagnostic (item 3
   below) and THERMODYNAMICS' `p_abs_naive` anchor (item 4 below), both
   of which their own authoring seats stated would otherwise move their
   verdict toward OPPOSE. **RECOMMENDED** — PHOTONICS' percentile-rank
   report (item 1), MATERIALS' coherence-length citation (item 2),
   VISION's caveat-forward language (item 5) — all still implemented in
   full below, but genuinely optional quality improvements, not
   verdict-changing.
3. **[EM, MANDATORY]** A per-draw flank-denominator diagnostic
   (`flank_ratio_draws[k] = b_flank_k / EMPTY_JOINT_FLANK_RAW_NATIVE_
   ESTABLISHED`, flagged if `<0.20`) computed for every one of the
   N_DRAWS=2000 reconstructions per article, not only the established
   δ=0 case — Cauchy-Schwarz bounds raw flux, not the Weber ratio `C`,
   which has no finite passivity ceiling; a large `|C(δ)|` alone cannot
   distinguish genuine unsuppressed interference from a draw landing near
   a flank-window node. **Disclosed per Red Team's own item 3**: the
   0.20 threshold is REUSED UNMODIFIED from its single-realization
   (exp-056) calibration, not re-derived for the N=2000 ensemble.
4. **[THERMODYNAMICS, MANDATORY]** `p_abs_naive = Σᵢ p_abs_leg[i]`
   (`sc.radial_absorbed_power` on each of the 9 already-captured legs,
   zero marginal FDTD cost) computed and reported alongside exp-056's
   established `p_abs_joint_measured`, for both articles — closes
   THERMODYNAMICS' own Iteration-33 mandatory fix (previously scoped
   down at exp-056 for lack of a naive-incoherent anchor; the 18 legs
   this cycle needs anyway make it free).
5. **[PHOTONICS, recommended]** `percentile_rank_of_delta0_within_abs_c`
   — where the established δ=0 point (`off_pass`=−0.058149,
   `off_bracket`=−0.055609) sits within the empirical `|C(δ)|`
   distribution, since `FALLBACK_ANGLES`' mirror symmetry (confirmed:
   `(-35,-25,-15,-5,0,5,15,25,35)`, and both the object and flank windows
   are functions of `|y−y0|`) makes δ=0 a stationary point of the
   window-integrated intensity in the 8-dim relative-phase space —
   plausibly non-generic, direction (max or min) not resolved by Phase 2.
6. **[MATERIALS, recommended]** Idealization on the ambient-light-analog
   caveat quantified with real numbers (coherence length vs
   inter-component path-length spread), below.
7. **[VISION, recommended]** The ambient-light-analog caveat is pulled
   forward into the SAME sentence as every headline/falsifiable claim
   about the N=2000 draw statistics, not left one section away in
   Idealizations alone.
8. **[Red Team, item 4]** Stage 20's object-loaded-branch-only scope is
   stated explicitly in its own docstring (persistence fidelity is
   scene-content-independent; the harder physics case — PEC-cored,
   inhomogeneous σ_e — subsumes the vacuum case stage 19 already
   separately covers), mirroring the Director's own Iteration-33
   phantom-disk precedent, not left implicit.
9. **[Red Team, item 5]** The `rel_phase`/`lab.artifacts` question is
   marked **CLOSED**, not open — confirmed harmless directly against
   `artifacts.py::validate_groups`'s source-key validation (only missing
   required keys are rejected; unknown extra keys are never checked for
   `sources`, unlike the stricter per-object param check four lines
   later).

## T1 escape route

**NONE.** Same register as Iterations 26/29/31/32/33 — instrument/
model-fidelity work (characterizing an existing artifact's statistics),
not a phenomenon-mechanism proposal; takes no position on
σ(I)/σ(x,t)/angular-selectivity/sub-threshold, touches no constraint
directly.

## Realizability bound (Materials' seat duty)

**Not applicable to `off_pass`/`off_bracket` themselves** — reused
verbatim from exp-032/033 (published-tier ordinary lossy media, ka≈24.5,
unchanged). **Applicable to the ambient-light-analog caveat below**,
quantified per MATERIALS' Phase-2 fix, **corrected at Phase 5 close**
(Red Team mandatory fix 5 — MATERIALS' own original arithmetic mislabeled
this program's established `dx=30 nm/cell` as "2.3 μm/cell," inflating
the operative distance ~77× and producing an internally inconsistent
"~180 μm... tens of micrometers" claim in the same sentence): real
broadband sources (sunlight, incandescent/LED flashlights) have
coherence lengths of order 1–10 μm; the physically operative baseline
for this scene's N=9 angular components is the FULL illuminated source
aperture (`NY−2·ABSORB` = 1504 cells ≈ 45.1 μm at 30 nm/cell — path-
length differences between angular components accumulate across the
*launching* aperture, not the object's own much smaller 4.68 μm
diameter, which alone would sit inside the 1–10 μm range and not support
this caveat at all), giving a maximum inter-component path difference of
≈45.1 μm·sin(35°) ≈ 26 μm — **roughly one order of magnitude** beyond
any real broadband source's coherence length (revised down from the
original, arithmetically-unsupported "one to two orders of magnitude").
The qualitative conclusion is unchanged and standard-optics-robust to
which reasonable baseline is chosen (even the loosest, ambient-window-
span baseline gives ≈6–12 μm, still beyond 1 μm). This is the physical
reason no real ambient illuminant can lock to one frozen relative phase
across all 9 directions the way this diagnostic does, for even one draw,
let alone reconstruct a stable ensemble of them — not merely an
assertion (Iteration-32/33's own
recurring caveat-strength failure, closed here with a derived bound).

## Predictions — committed before this experiment's `run.py` first run

**P-058-1 (zero-phase reconstruction vs exp-056's established
`C_joint`, both articles).** Band: ≤0.01% relative. Central estimate:
≤0.001% (informed by a Director diagnostic pre-run on `off_pass`:
2.4×10⁻⁷ relative). Disposition: inside band → CONFIRMED, the
disk-persisted zero-phase reconstruction is a faithful substitute for a
direct joint call on the real science geometry, not only on stage 20's
canonical bench.

**P-058-NF (noise-floor validation leg, both articles, Director's own
addition).** Band: absolute `C`-error in [1e-6, 2e-3]; central estimate
≈1×10⁻⁴ (informed by the same `off_pass` diagnostic: 1.24×10⁻⁴,
NOTE — a different, informal RNG draw than `run.py`'s own seeded
`NOISE_FLOOR_SEED` output, so informative, not a duplicate). Disposition:
`noise_floor_over_c_thr` ≤0.5 → PASS, the N_DRAWS=2000 ensemble
statistics below are trustworthy at face value; 0.5–2.0 → FLAG, treat
draws within ~1 noise-floor-width of `C_thr` as uncertain, otherwise
trust the bulk statistic; >2.0 → the ensemble statistics are NOT
trustworthy without more settling — a follow-on cycle (increase STEPS)
would be required before citing them further, and this cycle's own N=2000
results would be reported as measured-but-unvalidated, not as a
constraint-3-relevant finding.

**P-058-2 (N=2000 draw mean, both articles).** Band: `C_naive_established`
± 20% relative (`off_pass`: [−0.0054,−0.0036]; `off_bracket`:
[−0.0025,−0.0017]) — Iteration 6's zero-mean cross-term result is an
infinite-ensemble limit, not an exact finite-N=2000 bound, so this band
is itself an informal, low-confidence check, not a strict identity.
Disposition: inside band → CONFIRMED, the empirical mean tracks the
established naive-incoherent value even at finite N; outside band but
same sign/order of magnitude → NOTED, a finite-sample deviation, not
necessarily a refutation; wrong sign or order-of-magnitude different →
a genuine new finding, worth a dedicated thread.

**P-058-3 (N=2000 draw std, both articles) — REVISED at Phase 3.**
Original Phase-1 central estimate (0.035–0.045, informed only by T26's
own four δ=0 point measurements) is flagged SUSPECT by a Director
diagnostic: one `off_pass` noise-floor validation draw (informal seed,
not `run.py`'s own) measured `|C|=0.248` — 5–6× the original std
estimate, inconsistent with that band under a normal approximation
unless it is itself a rare tail event. **Revised band: std ∈ [0.02,
0.30]**, central estimate widened to 0.08–0.15, both original and
revised bands reported at Phase 5 for comparison. This is exactly the
kind of self-correction PANEL.md's independence mechanics exist to catch
before a narrow, under-evidenced estimate ships as a headline.

**P-058-4 (fraction of 2000 draws with `|C|>C_thr=0.005`, both
articles).** Band: [50%, 95%], central estimate 80–90% (Phase 1,
unrevised — if P-058-3's wider std holds, this fraction likely sits
toward or above the upper end of this band, since a wider spread around
a near-zero mean saturates a small fixed threshold faster; not
pre-committed as a separate band to avoid double-counting the same
underlying uncertainty). **Every disposition branch below applies
Idealization 6's ambient-light-analog caveat in the SAME sentence (Red
Team/VISION's mandatory pattern, Iterations 24/32/33): this fraction
characterizes the reconstruction instrument's own coherent-artifact
statistics under a hypothetical illuminant no real ambient source
produces (coherence length argument, above); it is NOT an estimate of
the probability a human observer would perceive anything, since no such
observer-facing scenario exists for any individual draw, and no existing
Tier-W/Tier-A constraint-3 verdict moves regardless of outcome.**

**P-058-5 (fraction flagged for flank-denominator collapse, both
articles).** Band: <10%, informal, low confidence (off_pass/off_bracket
are near-null but not near-zero-flank scenes at this geometry — informed
by exp-056's own established `flank_ratio_vs_empty_joint`≈1.00
at δ=0). Disposition: informational — a high flagged fraction would mean
a meaningful share of the P-058-4 headline is denominator-artifact-
consistent, not scored as genuine coherent brightening.

**P-058-6 (percentile rank of `|C(δ=0)|` within the empirical `|C(δ)|`
distribution, both articles).** PHOTONICS' mirror-symmetry argument
predicts δ=0 is a stationary point (extremal), direction unresolved.
Falsifiable claim: percentile rank lands OUTSIDE [25,75] (i.e., in an
extreme decile, either tail) — NOT near the median. (Informal secondary
note, low confidence, from the Director's own single off-seed diagnostic:
`|C(0)|`≈0.058 was much SMALLER than that one random draw's 0.248,
weakly suggesting δ=0 may sit toward the LOW-percentile tail rather than
high — not pre-committed as a directional prediction, since it rests on
one point.)

**P-058-7 (`p_abs_naive` / `p_abs_joint_established` ratio, both
articles).** Band: [0.5, 2.0], informal, low confidence — informational,
not scored against a hard pass/fail (first measurement of this anchor;
THERMODYNAMICS' own expressibility contract treats this as a post-run
analytic comparison, not a gated identity).

## Idealizations

1. Reconstruction assumes the captured leg has reached true CW steady
   state; P-058-NF exists precisely because this is now known to be an
   imperfect assumption at this τ, characterized rather than assumed.
2. Line-only persistence scope (`lab/phase_lines.py`) — no
   radial-absorbed-power channel at that format; `p_abs_naive` is
   computed from the LIVE capture before line extraction, not from the
   persisted format.
3. Fixed, single measurement plane (`PLANE_X`), no window-position
   rescan across the 2000 draws (matches every other `C` citation in
   this program; a future cycle's item, not this one's).
4. `rel_phase` is spatially uniform (y-independent) only — no wavefront
   curvature/chirp, a different mechanism class, out of scope.
5. Single λ=600nm, native r=78 geometry only — no 450/750nm
   generalization this cycle (already separately queued).
6. **Ambient-light-analog caveat (binding, propagated to every
   disposition branch above, not only P-058-4's, per Red Team/VISION's
   own established pattern)**: every draw in this build is a mutually-
   coherent, single-frequency, 9-component injection with a coherence
   requirement 1–2 orders of magnitude beyond any real broadband
   illuminant (quantified above) — nothing sunlight/skylight/a flashlight
   sweep produces, for even one draw. The incoherent naive sum remains
   this program's actual model of real ambient light; no existing
   Tier-W/Tier-A verdict is at stake regardless of this cycle's outcome.
7. N_DRAWS=2000 is a finite sample, not the true continuous ensemble —
   mean/std/fraction statistics carry finite-sample uncertainty not
   separately quantified (no bootstrap/CI computed this cycle).

## Results

20 new FDTD calls, 427 s. Full data: `results.json`, persisted legs under
`artifacts/legs/`, raw 2000-draw arrays under `artifacts/draws_*.npz`.

| Prediction | Predicted | Measured (off_pass / off_bracket) | Verdict |
|---|---|---|---|
| P-058-1 (zero-phase reconstruction vs established) | ≤0.01% rel. | **2.4×10⁻⁷% / 4.7×10⁻⁶%** rel. | **CONFIRMED**, far inside band — `C(0)`=−0.058148985930206114/−0.055608736046099706 vs established −0.058149/−0.055609. |
| P-058-NF (noise-floor validation leg) | [1e-6,2e-3] abs., central ~1e-4 | **1.238×10⁻⁴ / 3.443×10⁻⁴** abs. (2.48% / 6.89% of `C_thr`) | **PASS** both — well under the 0.5 flag bar. The N=2000 ensemble statistics below are trustworthy at face value. |
| P-058-2 (draw mean vs `C_naive`±20%) | [−0.0054,−0.0036] / [−0.0025,−0.0017] | **+0.02994 / +0.04405** | **REFUTED — wrong sign AND ~6–20× the predicted magnitude.** Not a finite-sample fluctuation; see Headline. |
| P-058-3 (draw std, revised band) | [0.02, 0.30] | **0.2310 / 0.2412** | **CONFIRMED** inside the Phase-3-revised band — vindicates the revision (original Phase-1 0.035–0.045 estimate would have been refuted by 5–7×). |
| P-058-4 (fraction \|C\|>C_thr) | [50%,95%], central 80–90% | **98.7% / 98.35%** | **ABOVE the predicted band** — even more extreme than anticipated. See Headline for the mandatory ambient-light-analog caveat. |
| P-058-5 (fraction flank-denominator-flagged) | <10% | **0.0% / 0.0%** | **CONFIRMED** (band satisfied) — but see Headline: this does NOT mean the ratio-sensitivity mechanism EM flagged is absent, only that it doesn't manifest as the specific ≥80%-collapse EM's threshold checks for. |
| P-058-6 (percentile rank of \|C(0)\|, outside [25,75]) | outside [25,75] | **19.6% / 18.75%** | **CONFIRMED**, and directionally — the informal secondary note (δ=0 sits toward the LOW tail) is also borne out: ~80% of random draws are MORE extreme than the established δ=0 point. |
| P-058-7 (`p_abs_naive`/`p_abs_joint` ratio) | [0.5,2.0], informational | **0.784 / 0.784** | **CONFIRMED** (informational) — **corrected at Phase 5 close (Red Team mandatory fixes 3+4 — PHOTONICS caught the direction, THERMODYNAMICS independently caught the mechanism phrase; both needed, neither alone sufficient):** `p_abs_naive/p_abs_joint=0.784<1` means naive is LESS than joint, i.e. **coherent joint injection absorbs ~28% MORE power than the naive sum of independently-run legs at δ=0 — a real, moderate CONSTRUCTIVE-interference effect** (all 9 legs' angular phase ramps are anchored at the same y₀ as the object center, so at δ=0 all 9 are in-phase exactly at the object — synthetic focusing), not destructive as originally stated. Both articles agreeing to 4 significant figures (0.78407/0.78411) is genuine, but NOT because of "the same τ-to-R_OUT geometry ratio" (numerically false: 8.33×10⁻⁵ vs 3.85×10⁻⁵, differ >2×) — the real mechanism is **leading-order-in-τ field-pattern universality**: both articles are near-null-τ, so the disk barely perturbs the incident field (`Ez_i≈E_inc,i` for both), making the cross-term/self-term ratio a property of the fixed illumination geometry alone, independent of τ to leading order. |

### Headline (for LOGBOOK)

**[Ambient-light-analog caveat stated first, per this program's own
binding pattern (Red Team/VISION, Iterations 24/32/33, and this cycle's
own Idealization 6, quantified above): nothing below characterizes real
ambient-light appearance. Every draw is a mutually-coherent,
single-frequency, 9-component injection requiring a coherence length
1–2 orders of magnitude beyond any real broadband illuminant. No
existing Tier-W/Tier-A constraint-3 verdict moves.]**

With that framing fixed first: **T25's variance question is answered,
and the answer is sharper and more interesting than any seat's Phase-1
prediction anticipated.** The Weber-contrast ratio `C(δ)` across
N=2000 genuine random relative-phase draws is **heavy-tailed and
mean-unstable** — the empirical MEAN (+0.030/+0.044) is wildly
different in sign and magnitude from the naive-incoherent anchor
(−0.0045/−0.0021), but the **MEDIAN** (−0.0185/−0.0058) sits on the
SAME side of zero and within the same order of magnitude as that
anchor. This is not a contradiction: `C=(b_obj−b_flank)/b_flank` is a
RATIO of two flux-like quantities, and Iteration 6's own zero-mean
cross-term theorem is a statement about the (better-behaved, additive)
flux itself, not about this nonlinear ratio — exactly the distinction
EM's Iteration-32 finding drew (Cauchy-Schwarz bounds raw flux, never
the `C` ratio, which has no finite passivity ceiling) and now empirically
confirmed at scale: this build's own draw range spans −0.35 to +0.94,
and EM's own flank-denominator diagnostic (mandatory fix 3) recorded
**zero** of 2000 draws below its 0.20 collapse threshold for either
article — the extreme tail is NOT explained by near-total flank
cancellation in the narrow sense that diagnostic checks for, but by
milder, broader flank-flux variability multiplying through the ratio.
**A sharper, more complete version of T26's own finding**: exp-055/056's
one arbitrary δ=0 draw is not a special, unlucky outlier — it is MILDER
than 80% of random draws (percentile rank 19.6%/18.75% within `|C(δ)|`),
so the ~11× `C_thr` figure this program has cited since **Iteration 33**
(corrected at Phase 5 close, Red Team mandatory fix 7 — VISION's own
catch: Iteration 32/exp-055 measured a different, empty-scene-only
figure, not this one) is, if anything, an UNDERSTATEMENT of the
coherent-injection diagnostic's typical severity. Practically, **and
this entire paragraph carries the SAME ambient-light-analog caveat
stated at this Headline's own opening — no real ambient source ever
produces even one draw of this hypothetical mutually-coherent
illuminant, so nothing below is a claim about what a human observer
would actually experience**: 98.7%/98.35% of individual random-phase
realizations exceed `C_thr` under this program's own scoring convention
(a number-vs-threshold comparison, not a probabilistic detection
judgment), even though the ensemble's own median only loosely recovers
the naive-incoherent anchor's sign and rough scale — **corrected at
Phase 5 close (Red Team mandatory fix 6, QUANTUM's own precision
catch)**: the median/naive ratio is 4.10× for `off_pass` and 2.77× for
`off_bracket`, not the "roughly recovers"/"same order of magnitude"
tightness this paragraph originally implied. **What DOES track the
naive-incoherent anchor precisely, confirmed by a same-shift follow-up
test (`recompute_flux_signs.py`) that finally persists the raw
`b_obj`/`b_flank` flux draws QUANTUM's own Iteration-6 theorem needs
(previously computed then discarded)**: the theorem's actual claim —
that `E[b_obj]` and `E[b_flank]` over random relative phase equal the
naive-incoherent sum EXACTLY, a Kronecker-delta cross-term cancellation
re-derived N=2→N=9 at this cycle's own Phase 5 — is confirmed to
0.01–0.69% relative error across both articles and both quantities
(4 independent checks), consistent with pure Monte-Carlo sampling noise
at N=2000. **This is the real content behind the median's own loose
tracking**: the underlying FLUXES behave exactly as the theorem
predicts; the RATIO `C` built from them does not, precisely because
`E[X/Y]≠E[X]/E[Y]` for correlated random `X,Y` — not because the
theorem fails, but because it was never a claim about ratios in the
first place. `p_abs_naive`/`p_abs_joint`'s own clean 0.784/0.784
agreement (informational, THERMODYNAMICS' anchor, corrected direction —
see P-058-7) independently confirms the underlying interference physics
is real and consistent across both articles, not a numerical artifact of
one.

### On P-058-2's own refutation

Flagged, not buried: the original Phase-1 mean-band prediction rested on
an unstated, incorrect assumption (that a RATIO's empirical mean would
track the naive value the way its numerator/denominator fluxes
individually do) — no Phase-2 seat or Red Team caught this specific gap,
though EM's own general "C has no finite passivity ceiling" finding was
the exact tool that would have predicted it, had it been applied to the
MEAN prediction specifically rather than only to the per-draw flag. This
is this cycle's own genuine miss, disclosed rather than smoothed over
per house discipline — and the reason P-058-3's std revision (which DID
apply that lesson) survived while P-058-2 (frozen before the lesson was
internalized) did not.

## Phase 5 — six fresh seats, then Red Team audit

**5 PROMISING (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS,
QUANTUM OPTICS), 1 PARTIAL (VISION SCIENCE)** — not unanimous. PHOTONICS
and ELECTROMAGNETISM independently (different routes: raw-data
reconstruction vs. algebraic cross-check) found the SAME real bug
(`phase_lines.flux_from_lines`'s sign contradicted its own docstring, a
false claim of matching `ambient.observer_profile`'s convention) and
proved it mathematically inert on every ratio-based number this cycle
reported. PHOTONICS separately found P-058-7's causal direction stated
backwards (constructive mislabeled destructive); THERMODYNAMICS
independently found the SAME row's mechanism justification numerically
false ("same τ-to-R_OUT ratio" — actually differ >2×) without catching
the direction error, requiring both fixes together. MATERIALS found the
Realizability-bound coherence-length arithmetic inflated the object's
scale ~77×. QUANTUM OPTICS found the "median tracks naive" framing
oversold its own precision and that raw flux draws needed for its own
Iteration-6 theorem test were computed then discarded. VISION SCIENCE's
PARTIAL rested on the Headline's own most-quotable sentence not
delivering this cycle's own Phase-3 promise (item 7) to embed the
ambient-light-analog caveat inline, not one section away — a real,
textually-confirmed, self-inflicted gap.

**Red Team's final audit: PROMISING, adopting 5-of-6 and explicitly
OVERRIDING VISION SCIENCE's PARTIAL** — independently re-verified every
finding above against source and raw persisted data a further time
(confirming the sign bug via a THIRD independent route, confirming the
0.784 direction error, confirming the coherence-length arithmetic).
Ruling on the override: VISION's finding is real and docketed as
mandatory, but the caveat's SUBSTANCE is correctly present elsewhere in
this same document (the Headline's own bracketed lead-in, Idealization
6, and P-058-4's pre-registered Predictions-section text) — the
identical same-shift-fixable documentation-gap class this program has
repeatedly and correctly resolved via mandatory fix rather than a
blocking verdict (direct Iteration-33 precedent, LOGBOOK ~11296-11324,
an arguably worse instance on an otherwise-unanimous 6-0 cycle). **New
binding tripwire**: this is the fourth prior instance of this caveat-
placement failure pattern (Iterations 24, 32, 33) PLUS a same-cycle
broken promise (this cycle's own Phase-3 item 7 not fully executed in
its own Headline) — a further recurrence after this ruling is a
retroactive Checkpoint-4 trigger, no further Red Team deliberation
required to establish it as drift. **All five Checkpoint criteria
checked explicitly: none fire** — criterion 4 scrutinized hardest given
this cycle produced two genuine bugs plus a caveat-placement gap; ruled
non-firing because every defect was CAUGHT by falsifiable, independently-
checkable claims (falsifiability is what caught them, not what they
lacked), the sign bug is proven mathematically inert and structurally
isolated from the real constraint-3 pipeline, and no constraint is
quietly dropped — the caveat's substantive conclusion (no Tier-W/Tier-A
verdict moves) is correct and stated in multiple places.

**Nine-item mandatory same-shift fix docket, all applied above/below,
none requiring any new FDTD call** (all corrections to reported numbers/
prose/persistence/suite-coverage against data already on disk): (1)
`phase_lines.flux_from_lines`'s sign, fixed. (2) A new stage-20 raw-flux
identity gate (Q9), added — measured 0.00e+00 (exact algebraic
identity), closing the layer-coverage gap that let (1) ship undetected
by machinery. (3)+(4) P-058-7's direction and mechanism corrected
together. (5) The coherence-length arithmetic corrected. (6) The
Headline's own numeric-claim sentence now carries its caveat inline,
with the median-tracking claim's precision corrected per QUANTUM's own
finding. (7) "Iteration 32"→"Iteration 33" citation fixed. (8)
`b_obj_draws`/`b_flank_draws` persisted via `recompute_flux_signs.py`
(zero new FDTD, reloads the already-persisted legs) — which also
directly tested QUANTUM's own Iteration-6 theorem at the flux level for
the first time (0.01–0.69% relative error, 4/4 checks, consistent with
N=2000 Monte-Carlo noise) and independently re-verified (1)'s fix is
provably inert on every `C(δ)` number already reported (bit-identical
before/after, `max|diff|=0.00e+00` across all 4000 draws — see
`sign_fix_verification.json`). (9) `lab/validation/VALIDATION.md`'s
queued "Measurement lesson" line, written at this Phase 5 close (below).

Bench reverified 61/61 (`--only 12346789,10,11,18,19,20`) after the
stage-20 Q9 addition, before this cycle's own commit. **Verdict:
PROMISING.**

## Next (pre-registered, for Phase 5)

(1) If P-058-NF's disposition is FLAG or FAIL for either article, a
follow-on cycle increasing STEPS for the affected article is queued
immediately, ranked above other backlog — NOT triggered this cycle
(both PASS). (2) `Q_ext(x)` — LOCKED for Iteration 36 (or a zero-cost
desk rider to this cycle, per Iteration 34's own ruling) — **Director's
call: NOT folded in here**, given this cycle's own scope (new machinery,
20 new FDTD calls, five tiered Phase-2/Red-Team fixes, a self-discovered
settling finding, and a nine-item Phase-5 fix docket) is already
substantial; explicitly deferred to Iteration 36, not silently dropped.
(3) R3-on-loaded-legs for exp-056's `off_pass_joint`/`off_bracket_joint`
(ranked #1 competitive priority at Iteration 34's close) stays queued,
unaffected by this cycle's different (phase-variance, not resolution)
axis. (4) MATERIALS' absorptivity/mechanism literature check — deferred
since Iteration 29, now SEVEN cycles running if not picked up next —
approaching this program's own escalation pattern, flagged explicitly by
both MATERIALS and Red Team this cycle. (5) The flank-denominator
diagnostic (EM's own mandatory fix) should be upgraded from a binary
`<0.20` flag to a reported distribution/correlation for a future cycle —
EM's own Phase-5 re-analysis found a real, moderate (`corr≈0.45-0.50`,
R²≈0.20-0.25) but only partially-explanatory correlation between flank
suppression and `|C|`, which the binary flag alone cannot show. (6) A
Geary-Hinkley (ratio-of-correlated-near-Gaussians) quantitative model of
`C(δ)`'s own tail shape, proposed by QUANTUM OPTICS' Phase-5 review as a
near-zero-cost follow-on now that `b_obj_draws`/`b_flank_draws` are
persisted (item 8, above) — not built this cycle.
