# PHASE 2 — RED TEAM AUDIT · Panel Iteration 83 · exp-106
## "Floor-Gating, Settling, Risk-Propagation, and the Fixed-Absolute-Thickness Control for `kappa_window`"

*Last seat. Blind-critique inputs, `phase1_proposal.md`, `experiments/105-.../run.py`+`NOTES.md`,
`experiments/052-.../design_geometry.py`+`NOTES.md`, and `lab/sections.py` all read directly
before writing this — every load-bearing number below re-derived from primitives, not
restated from a seat's own prose (R4/R8 discipline). No `run.py` exists yet for exp-106 —
this is a pre-freeze audit of the Phase-1 design only.*

## 0. Housekeeping verification (positive control)

Before attacking anything, the proposal's own arithmetic was independently re-run:

- §2a's table (nyquist_margin 4.936/2.468/1.234, z/z_R 0.253123/0.063281/0.015820,
  R_CORE 30/60/120, tau_shell=24.0 throughout) reproduces `experiments/105-.../
  NOTES.md`'s own committed `geom(r)` output digit-for-digit. **R4-clean — no hand-typo
  detected**, unlike this exact sub-thread's own history (two prior incidents cited in
  the proposal's own §2a preamble).
- §2b's fixed-abs table: `r_in_fixedabs(r) = r-48` → 30/108/264 at r=78/156/312 ✓;
  `tau_shell = 0.5*48 = 24.0` constant ✓; coincidence with self-similar at r=78
  (R_CORE=30, sigma_max=0.5 both) ✓ — matches `experiments/052-.../design_geometry.py`'s
  own printed assertions exactly. **Clean.**
- FDTD call budget: 4 legs × 2 calls (self-similar) + 4 legs × 2 calls (fixed-abs) = 16,
  r=78 contributing 0 to both — arithmetic checks. **Clean.**
- `results.json` growth estimate (≈128,000 floats ≈1MB): 4000 cells × 2 scenes × 2
  STEPS-legs × 2 families × 2 new r-points = 128,000 — checks. **Clean.**

T1 is correctly N/A (no σ(I)/σ(x,t)/angular-selectivity machinery touched; only
`R_CORE`/`sigma_max` vary at fixed `r_out`, reusing exp-052's already-audited, passive
`graded_black_shell` verbatim).

## 1. Numbered attacks

### Attack 1 — [unfalsifiable] PHOTONICS: no falsifiable band on the sharper, cheaper cross-family absolute-ratio prediction

**Verification.** `tau_shell=24.0` and `R_COAT=r` are identical between families at
every r (confirmed §0). Near-opacity (`exp(-24)≈4e-11` direct transmission) means the
window signal is dominated by near-field diffraction around the (identical) outer
boundary; a pure geometric-window mechanism predicts `kappa_window_fixedabs(r) ≈
kappa_window_selfsim(r)` in **absolute** magnitude, not merely in **shape** (`shape_ratio`).
The proposal's own §4 commits only to scoring `shape_ratio_fixedabs`, never the raw
per-r ratio `kappa_window_fixedabs(r)/kappa_window_selfsim(r)` — a strictly weaker
statistic (3 points, one of which — r=78 — is literally shared data between arms) that
both families' fresh captures already produce for free. As written, a diffraction-
dominant world and a some-other-effect world could both land inside the CONFIRM/REFUTE
shape_ratio bands without this sharper, already-free discriminator ever being reported.

**Verdict: ADOPT.** Zero marginal FDTD cost (both scalars already captured at r=156/312
in both families). Concrete fix specified in §3.2 below.

### Attack 2 — [inconsistency] PHOTONICS: the CONFIRM band itself doesn't reconcile with cited diffraction theory

**Verification.** `shape_ratio_fixedabs ≤ 8.0` ⟺ (by the `shape_ratio≡2^n` identity
`exp-105` derived and Red Team independently re-verified from the forced x(78:156:312)
= 4:2:1 geometry) an implied exponent `n = log2(8.0) = 3.0` exactly. `NOTES.md`'s own
cited edge-diffraction asymptotic range is n≈1–2. So even the "pure geometric window
diffraction wins" branch of item 4's own pre-registered CONFIRM band sits at n≤3.0 —
above the theory-motivated range, not inside it. Neither pre-registered outcome
(CONFIRM *or* REFUTE) actually connects the fixed-abs result to a coherent optical
mechanism; the control can only arbitrate between two program-internal hypotheses.

**Verdict: ADOPT as a disclosure requirement, not a redesign trigger.** This is a scope
statement missing from §4, not a design defect — item 4 was never sold as reconciling
with theory, only as discriminating two internal hypotheses. Phase 3 must say this
explicitly in the predictions text (see mandatory fix 6).

### Attack 3 — [inconsistency] EM: `p3_trusted`-equivalent reasoning transplants a point-sampling diagnostic onto a box-averaged statistic without argument

**Verification.** Confirmed directly in `run.py::geom()`: `nyquist_margin = predicted_
ripple_period/(2*DENSE_PITCH)`, a function of `DENSE_PITCH`-sampled aliasing risk along
`dense_x` — nothing about it references `window_stats()`'s own 100×40-cell spatial mean.
A box integral of a periodic near-field ripple is a low-pass filter on exactly the
spatial frequency `DENSE_PITCH`-aliasing concerns; if anything it *suppresses* the risk,
it doesn't inherit it unchanged. The ≥2.0 TRUSTED threshold was calibrated for the
point channel, and item 3 imports it onto `kappa_window` with no independent
justification. This does not make the forced-False r=312 read *wrong* (a MARGINAL-tier
domain is still a legitimately elevated-risk domain for any statistic drawn from the
same underdetermined FDTD run) — but the "symmetric to `p4_156_trusted`" framing
overstates how apples-to-apples the two gates are.

**Verdict: ADOPT.** Cheap fix: state explicitly, wherever `p3_trusted` is reported,
that the Nyquist-margin gate is a reused proxy risk flag (same underlying MARGINAL FDTD
capture, not a re-derived box-integral aliasing bound), not a channel-native diagnostic.
No new machinery required — a one-sentence scope correction.

### Attack 4 — [inconsistency] EM/THERMODYNAMICS (converged): fixed-abs family exceeds the only-ever-validated core-fill ratio, no absorbed/reflected/transmitted ledger check proposed

**Verification (independently re-derived, not restated).**
`R_CORE/R_COAT` fixed-abs: r=156 → 108/156 = **0.69231** (rounds to 0.692 ✓ EM's
figure); r=312 → 264/312 = **0.84615** (rounds to 0.846 ✓). T9's only-validated
"core energetically incidental" anchor: r_in/r_out = 30/78 = **0.38462** (0.385 ✓,
confirmed against `design_geometry.py`'s own printed comparison line "T9's own
established point: 0.3846"). Both new ratios sit **1.8× and 2.2× past** the only point
this program has ever validated a PEC core's energetic incidence at. THERMODYNAMICS
independently converges from a different mechanism (gradient steepness, not core-fill):
confirmed via `geom()` that self-similar's `sigma_max` falls to 0.25/0.125 at r=156/312
while fixed-abs holds 0.5 fixed at every r — a real, verified 2×/4× steepness gap
between families at identical `tau_shell=24`, unrelated to (but structurally parallel
to) the core-fill concern.

**No ledger check exists anywhere in the Phase-1 proposal** — item 4's own bands treat
`shape_ratio_fixedabs` as a clean two-way discriminator (geometric-window vs. growing-
electrical-thickness) with no check on whether a third channel (core reflection leakage,
or gradient-steepness-driven absorbed/diffracted-power split) contaminates the reading.

**Verdict: ADOPT (both seats' flip conditions), with one correction to how "zero
marginal cost" is characterized** — see Attack 8, and concrete implementation in
mandatory fix 1.

### Attack 5 — [inconsistency] VISION: R23 disclaimer-erosion risk, real and specific to this design

**Verification.** §3 of the proposal states the DISCLAIMER "is reused verbatim" and is
"asserted present in both `PREDICTIONS_TEXT` and `RESULT_TEXT`" — but that claim
describes only the *existing* string's presence, not whether items 1/2/4's own **new**
verdict text (floor-gate `frac_unresolved`, `settling_pass_window`, `shape_ratio_
fixedabs` CONFIRM/REFUTE/AMBIGUOUS) gets concatenated into the same two strings the
`assert DISCLAIMER in ...` lines actually check. Cross-checked against `experiments/
105-.../run.py`: that file's own history (its docstring claiming two asserts while
shipping only one at execution time, caught only at Phase 5) is a real, code-level
precedent for exactly this failure mode in this exact sub-thread. §2c/§2d/§4 of the
exp-106 proposal describe the new fields as additions to the **persisted record**
(`results.json`) — never as prose folded into `build_predictions_text()`/
`build_result_text()`. Nothing in the proposal pins which function assembles this.

**Verdict: ADOPT.** Concrete code-enforcement fix in mandatory fix 5 below — this is
exactly the kind of gap R23 exists to catch, and it would be a third instance in this
sub-thread's own disclaimer-erosion lineage if it lands uncaught.

### Attack 6 — [inconsistency, MAJOR — partial OVERRIDE] MATERIALS: the critique's own factual premise is stale; the program already resolved this axis, and the proposal's own §5 sentence contradicts that resolution

**Verification.** MATERIALS' critique states the absorptivity-realism question (implied
~60nm e-fold length, "~3× too high vs real CNT-black") is exp-052's own Phase-5 #1 open
item, "never executed since." **This is false.** Independently re-verified by reading
`experiments/034-floor-convergence-scale-bridge/REALIZABILITY_MEMO.md` directly:

- **AMENDMENT 6** (Iteration 38, exp-061, LOCKED unconditional after an 8-cycle
  deferral) closed exactly this question with a sourced literature check. It found the
  α≈1/60nm figure MATERIALS cites is itself **wrong** — "a peak-conductivity×thickness
  bookkeeping artifact," corrected to **α≈1/174nm** (5.74×10⁴ cm⁻¹, an Im(n)-weighted
  figure). Final verdict: **UNOBTANIUM-WITH-PARAMETERS, overdetermined by the
  THICKNESS axis, not the rate axis** — real CNT-forest/Vantablack coatings run
  **100–500µm**, 70–350× this construction's own 1.44µm shell, "for every well-
  corroborated visible-band figure — this gap alone decides the tier and does not
  depend on which of two candidate α anchors is used." The rate axis itself is also
  reported unhealthy (best sourced CNT-forest α misses the corrected target by >25×),
  contradicting MATERIALS' specific "~3×" figure on both counts: the number MATERIALS
  computed no longer represents the program's own current best estimate, and the real
  gap (by either citation) is far larger than 3×.
- **AMENDMENT 7** (Iteration 39, exp-062) closed the remaining candidate-material
  search (NiP-black, graphene-aerogel) — neither clears a joint 2× band on rate+
  thickness together.

This is a genuinely load-bearing verification-layer failure in MATERIALS' Phase-2
critique for exp-106: it cites exp-052's Phase-5 open item without checking whether a
*later* cycle (Iteration 38/39, both antecedent to this one) already closed it. R8
discipline (verify before claim) was not honored by the critique itself here.

**Compounding this**, re-reading the exp-106 proposal's own §5 sentence against the
now-confirmed record: "the fixed-abs family's own constant 2.4λ absolute thickness is,
if anything, **closer to the µm-scale real-CNT-black range**" is backwards at bench
scale. The established range is 100–500µm; fixed-abs holds 1.44µm at every r (gap
69–347×, constant). Self-similar's absolute thickness *grows* with r (1.44µm → 2.88µm
→ 5.76µm at r=78/156/312, computed from the proposal's own table: 48/96/192 cells ×
30nm), so at r=312 self-similar's gap to the real range (100/5.76 ≈ 17.4×) is actually
**smaller** than fixed-abs's constant 69.4× gap — the opposite of what §5 claims. (The
established witness-scale divergence argument against self-similar — 0.31–0.92m coatings
at 45m viewing distance — is real, but is a *different* axis than this cycle's own
disclaimed "no witness-scale extrapolation attempted" scope, and §5 does not distinguish
the two.)

**Verdict: PARTIAL OVERRIDE.** ADOPT the underlying procedural instinct (§5 needs a
corrective sentence, thickness-realism and absorptivity-realism are separable claims).
**OVERRIDE the specific content MATERIALS proposes** — restating an uncited, since-
superseded "~3×, never executed" claim would itself be a fresh R4/R8 violation, not a
fix. Concrete replacement text specified in mandatory fix 4.

## 2. New attacks (none of the five critiques caught these)

### Attack 7 — [inconsistency, R13/R14-flavored] Inconsistent trust-gating rigor between `p3_trusted` (self-similar) and `shape_ratio_fixedabs`'s own r=312 reading

The proposal *forces* `p3_trusted=False` at r=312 (self-similar) via a hard boolean
gate and states this explicitly. But `shape_ratio_fixedabs` shares the **identical**
r=312 domain construction (§2b: "Domain construction ... is identical to §2a at the
same r") — so `nyquist_margin(312)=1.234` (MARGINAL) applies to the fixed-abs family's
r=312 leg too, forced by the same domain-geometry argument. Yet §4 only commits to the
weaker language "scored only if `p3_trusted`-equivalent ... is at least evaluated and
disclosed" — a soft prose caveat, not a hard suppressor of the CONFIRM/REFUTE/AMBIGUOUS
classification the way `p4_156_trusted` actually suppresses P4's own verdict trust
elsewhere in this exact codebase. This is an R13/R14-shaped hazard: `shape_ratio` is a
difference-of-differences ratio (`(κ78−κ156)/(κ156−κ312)`); if noise from the never-
floor-gated, MARGINAL-tier r=312 capture pushes `(κ156−κ312)` toward zero without
literally reaching it, `run.py`'s own existing guard (`... if denom != 0 else inf`)
does not fire, and an artifact-dominated blowup lands silently inside whichever band
its sign happens to match — plausibly REFUTES, misread as a genuine finding.

**Recommendation: mandatory fix 3, below** (a hard `shape_ratio_fixedabs_trusted` flag,
symmetric in kind — not just in name — to `p3_trusted`/`p4_156_trusted`, plus an
explicit near-zero-denominator floor check).

### Attack 8 — [inconsistency] EM/THERMODYNAMICS' "zero marginal cost" framing for the `radial_absorbed_power` ledger check is imprecise: the required input isn't actually captured yet

**Verification.** `sections.radial_absorbed_power(cap_scene, sigma_e, cx, cy, r_max,
n_bins=26)` requires `sigma_e` as a **full spatial array** (`p_j = 0.5*sigma_e*|Ez|**2`,
elementwise) — confirmed directly in `lab/sections.py`. `sigma_e` lives on the `Sim`
object (`sim.sigma_e`, written by `materials.graded_black_shell`/`pec_disk`, confirmed
in `lab/materials.py`). But `sc.full_capture(sim)` — the function `_run()` actually
returns — captures only `ez_a/hx_a/hy_a/ez_b/hx_b/hy_b/off/omega`; it does **not**
capture `sigma_e`. `_run()` as written in `experiments/105-.../run.py` (reused verbatim
per the proposal's own convention) discards `sim` on return. So EM's "reusing the
article-scene fields already captured for `kappa_window`" and THERMODYNAMICS' "same
captures, an extra reduction pass" both slightly overstate the true cost: **no new
`Sim.run()` call is needed** (that part is correct and the load-bearing claim), but
a small code change to `_run()`'s own return value (or an equivalent capture) IS
needed before `radial_absorbed_power` can be called at all.

**Verdict: ADOPT the underlying fix (Attack 4), CORRECT the cost characterization.**
Concrete change specified in mandatory fix 1.

### Attack 9 — [inexpressible-as-currently-scoped] `radial_absorbed_power` alone does not reproduce exp-052's own "core energetically incidental" test methodology

exp-052's own T9-generalization check (its Accepted Fix 3, later Director-redesigned to
a hollow-vs-PEC-cored `C` comparison specifically *because* no validated box/ref
convention existed for its own ambient scene class) compares a PEC-cored construction
against a **hollow** one and takes a delta in `sigma_abs/sigma_ext`. `radial_absorbed_
power` alone gives only the **absolute** radially-binned absorbed power of the
already-built PEC-cored object — since the PEC core forces `Ez=0` there, absorbed power
inside the core disk is trivially ~0 regardless of whether the core is "incidental" in
the T9 sense; the function cannot by itself detect a core that has become non-incidental
via reflection/diffraction leaking into the forward window instead of via anomalous
core absorption. `lab/sections.py::widths()` (already validated for this exact
beam-scene class — line-source + object, exp-028's own lineage, unlike exp-052's
ambient/N9 scene) is the function that actually yields `sigma_abs/sigma_ext` from the
scene/empty pair already captured, with no new FDTD call either. A genuine hollow-vs-
PEC-cored delta (the literal T9 methodology) would need a **third**, new FDTD capture
per (r, family) — real, undisclosed cost the proposal does not budget for.

**Recommendation:** run *both* `radial_absorbed_power` (spatial sanity: is absorption
physically concentrated in the shell annulus, no NaN/negative bins) and `widths()`
(the actual `sigma_abs/sigma_ext` ratio) on the already-captured pairs — both zero new
FDTD calls once the `_run()`/`sigma_e` and `box`/`ref` plumbing exist — and disclose
explicitly that this is **not** a literal re-run of exp-052's own hollow-core delta
test, which would cost real new calls and is not mandatory this cycle (Tier-2 item).

## 3. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.**

No attack rises to HALT-REDESIGN: every gap found is a concrete, cheap, well-specified
code addition or disclosure correction that leaves the cycle's own disclosed 16-call
budget, its cost-gating sequence, and its T1:N/A scope entirely intact. Nothing here
resembles an internally-inconsistent premise, an unfixable inexpressibility, or a
quietly-dropped constraint (see §5).

### 3.1 Mandatory fixes for Phase 3 — prioritized, concrete

**1. [Highest priority — converged EM/THERMODYNAMICS finding, corrected per Attacks 4/8/9]
Add an absorbed/extinguished-power ledger check on the fixed-abs family at r=156 and
r=312 — the two points where `R_CORE/R_COAT` (0.692, 0.846) first exceeds T9's only-
validated anchor (0.385).**

- Change `_run(with_article, steps, g)` to also return the material grid, e.g.:
  `return sc.full_capture(sim), (sim.sigma_e.copy() if with_article else None)`
  (only the article-scene sigma_e is needed; the empty scene has no object).
- Call `centers, bins, p_abs_total = sc.radial_absorbed_power(cap_article, sigma_e,
  g["CX"], g["CY"], r_max=g["R_COAT"])` for fixed-abs at r=156/312. Report
  `p_abs_total` and confirm no anomalous concentration outside the shell annulus
  (bins inside `r < R_CORE` should read ~0, per PEC).
- Additionally call `sc.widths(cap_article, cap_empty, box, ref)` with `box` a
  four-face Poynting rectangle clear of `ABSORB` enclosing `R_COAT` (reuse exp-028/030's
  own box-construction convention verbatim) and `ref=(g["SRC_X"], g["CY"], hh)`, to get
  `sigma_abs/sigma_ext` directly — the one quantity actually comparable to T9's
  established Δ(sigma_abs/sigma_ext)=1.56e-6 anchor.
- **Explicitly disclose**: this is *not* a re-run of exp-052's own hollow-vs-PEC-cored
  delta methodology (Attack 9) — no hollow-core capture is added this cycle (that is a
  real, new-FDTD-call cost, a Tier-2 item, not mandatory here). This ledger establishes
  only whether `sigma_abs/sigma_ext` is physically sane and small at these new ratios,
  not a validated delta against the 0.385 anchor.
- Flip/interpretation rule (THERMODYNAMICS' own offered threshold, reused): if fixed-abs
  and self-similar's `p_abs`/`sigma_ext` fractions land within ~10% of each other at
  matched r, treat item 4's two-hypothesis framing as adequately clean; if they diverge
  materially, report `shape_ratio_fixedabs`'s CONFIRM/REFUTE bands as **three-way
  ambiguous** (thickness-law vs. core-reflection/gradient-steepness vs. both), not a
  clean binary.
- **Cost: zero new `Sim.run()` calls** (reuses the article/empty-scene captures already
  scheduled for the floor-gate/kappa_window work at r=156/312, both families) — but
  requires the small `_run()`-return code change above plus a `box`/`ref` definition;
  state this precisely rather than calling it "free."

**2. [PHOTONICS] Add the raw per-r cross-family absolute ratio.**
`abs_ratio(r) = kappa_window_fixedabs(r) / kappa_window_selfsim(r)` at r=156 and r=312.
Pre-registered band: within a factor of ~2 of 1.0 → geometric-window dominance
strongly corroborated at the absolute-magnitude level (not just in shape); outside a
factor of ~2 → the thickness/electrical-thickness or core-fill effect is real at the
absolute-magnitude level, not merely in the shape statistic. Zero marginal cost — both
scalars are already captured by items 1/4's own budget.

**3. [Red Team, Attack 7] Make the fixed-abs family's own r=312 trust status a hard
gate on `shape_ratio_fixedabs`'s classification, not a soft caveat.**
```python
shape_ratio_fixedabs_trusted = (
    settling_pass_window_312_fixedabs
    and (nyquist_trust_tier(g312["nyquist_margin"]) == "TRUSTED")
)
```
— structurally forced False at r=312 for the identical reason `p3_trusted` is (fixed
domain geometry), disclosed the same way. When False, the reported classification must
read e.g. `"REFUTES (NOT-TRUSTED — r=312 MARGINAL/unsettled)"`, never a bare `REFUTES`.
Additionally, before classifying, check the denominator against the r=312 floor-gate's
own RMS: if `abs(kappa_window_156_fixedabs - kappa_window_312_fixedabs) < 3 *
window_floor_gate_312_fixedabs["rms"]`, flag the ratio `NOISE-DOMINATED-UNRELIABLE`
regardless of which side of 8.0/14.8 it lands on (R13/R14 near-zero-denominator
discipline).

**4. [Red Team, Attack 6 — corrects MATERIALS' proposed fix] Replace §5's realizability
sentence with a citation-grounded one, not a restated stale claim.**
Do not write "closer to the µm-scale real-CNT-black range." Replace with, e.g.: *"Both
families' r=78 anchor sits at the same 1.44µm absolute shell thickness whose
realizability tier is already CLOSED at `experiments/034-.../REALIZABILITY_MEMO.md`
AMENDMENT 6/7 (Iteration 38/39): UNOBTANIUM-WITH-PARAMETERS, overdetermined by the
THICKNESS axis (real CNT-forest/Vantablack coatings run 100–500µm, a 70–350× gap) —
not the absorption-rate axis, which was also re-derived there (α≈1/174nm, not the
~1/60nm bookkeeping artifact this program once cited) and found comparably unhealthy.
Fixed-abs holds this same 69–347× thickness gap at every r; self-similar's absolute
thickness grows with r (2.88µm/5.76µm at r=156/312) and is therefore marginally, not
substantially, closer to the real range at larger r — the opposite of a naive 'fixed-
abs is more realistic' reading. Neither family's realizability tier changes this
cycle; this sentence exists only to prevent a stale re-assertion of the pre-Iteration-38
claim."* This is a one-paragraph desk correction, zero new cost.

**5. [VISION, Attack 5] Code-enforce R23 concatenation for every new verdict this cycle
introduces.**
The floor-gate `frac_unresolved`/window-floor verdict (item 1), `settling_pass_window`
(item 2), `p3_trusted` (item 3), and `shape_ratio_fixedabs`'s CONFIRM/REFUTE/AMBIGUOUS
text (item 4, including the `shape_ratio_fixedabs_trusted` qualifier from fix 3 above)
must be string-concatenated into the *same* `build_predictions_text()`/
`build_result_text()`-equivalent functions the two `assert DISCLAIMER in ...` lines
already check — never printed or persisted only via a separate, unasserted
`results.json` field. Before freeze, grep `run.py` to confirm exactly two `assert
DISCLAIMER in` sites exist (matching exp-105's own corrected pattern) and that both
fire against the actual concatenated string containing all four new verdicts, not a
docstring's claim about it.

**6. [PHOTONICS, Attack 2 — recommended, zero cost] State in the predictions text that
even the CONFIRM band (`shape_ratio_fixedabs≤8.0`, implied n≤3.0) sits above this
program's own cited edge-diffraction theory range (n≈1–2)** — so a CONFIRM verdict
discriminates only between this program's own two internal hypotheses, and does not by
itself reconcile the finding with known diffraction physics. Prose-only, no code.

**7. [Attack 3 — recommended, zero cost] One-sentence scope correction wherever
`p3_trusted`/`shape_ratio_fixedabs_trusted` are reported**: the Nyquist-margin gate is
a reused risk-flag proxy (built for `dense_x` point-sampling aliasing), not an
independently-derived box-integral aliasing bound for `window_stats()`.

None of fixes 2–7 changes the disclosed FDTD call budget (still 16 calls). Fix 1 adds
zero new `Sim.run()` calls but does require the `_run()`/`sigma_e`/`box`-`ref` code
addition disclosed above — Phase 3 should say so plainly rather than characterizing it
as entirely free, per Attack 8.

## 4. Checkpoint criterion 4 — explicit ruling

**Does NOT fire.**

- **Unfalsifiable claims:** none found. Every scored prediction (Gate P0′ reproduction,
  floor-gate bands, settling tolerance, `p3_trusted`, `shape_ratio_fixedabs` CONFIRM/
  REFUTE/AMBIGUOUS bands) carries a pre-registered numeric threshold. Attack 7's gating-
  rigor gap is a *rigor* defect (a soft caveat where a hard suppressor belongs), not an
  unfalsifiable claim — the band itself is still falsifiable; only its trust-qualifier
  is currently under-enforced, and mandatory fix 3 closes that before any run.
- **A constraint quietly dropped, especially #3:** none found. T1 is correctly,
  repeatedly N/A (no mechanism introduced or varied). Constraint-3 (the hard one) is
  out of scope for this entire T28 sub-thread by explicit, numbers-backed precedent
  (`kappa_window` is a coherent on-axis transmission diagnostic, structurally distinct
  from the ambient/Weber-contrast instrument constraint-3 is scored against — exp-105's
  own VISION-authored scope-boundary note, ΔC≈0.018 at saturation, inherited unchanged
  here) — this cycle's own `DISCLAIMER` and T1 statement both name this explicitly, not
  silently. No section of the Phase-1 proposal claims or implies constraint-1/2/3/4
  progress.
- **Everything this audit found is a catchable, disclosed, fixable defect at exactly
  the pipeline stage designed to catch it** (Phase 2, before freeze) — including the
  one MAJOR item (Attack 6, MATERIALS' stale factual premise), which this audit itself
  caught and corrected rather than let pass into Phase 3 uncaught. That is the
  Red-Team/Checkpoint backstop working as intended, not evidence it is failing.

**One standing caution flagged forward, not fired:** Attack 6 is a first-of-its-kind
instance of a Phase-2 critique citing a prior experiment's "still open" item without
checking whether a *later* cycle already closed it (Iterations 38/39 postdate exp-052's
own Phase-5 close but predate this cycle). This is structurally analogous to exp-105's
own "Red-Team-repeats-a-wrong-figure" pattern (one instance, flagged forward, not yet a
rule) — logged here as a second, different-shaped data point in the same general
category (a seat's "independent re-check" not actually checking the full, current
program record) for a future cycle to watch, not yet a rule.
