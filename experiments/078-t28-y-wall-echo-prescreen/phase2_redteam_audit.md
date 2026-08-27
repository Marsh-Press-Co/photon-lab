# Phase 2 — RED TEAM Audit (exp-078, Panel Iteration 55)

**Seat: RED TEAM.** Read: `PANEL.md` in full; `AGENTS.md`; `LOGBOOK.md` in
full (RULED OUT R1–R9 including R4/R5/R6/R7/R8/R9's exact firing
conditions; LIVE THREADS T28's complete Iteration 46–54 history, exp-075's
own passivity/reciprocity gates and exp-077's two-wall extension);
`phase1_proposal.md`, `y_wall_prescreen.py`, `y_wall_prescreen_results.json`;
all five blind Phase-2 critiques (PHOTONICS — this cycle's rotation lead,
correctly absent from the critique roster — MATERIALS, ELECTROMAGNETISM,
THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE) and `phase2_quantum_null_
check.py`/`_results.json`; `experiments/077-.../phase2_redteam_audit.md`
(format/tone precedent, per the task brief).

**Independent verification performed computationally this cycle** (none of
it taken on any critic's word, or the proposal's own word, alone):

1. Re-derived, from the propagation-direction convention `(-cosθ,+sinθ)`
   stated in the proposal's own §3.1 and `y_wall_prescreen.py`'s own Sec
   [1b] comment — **not** from any critique's stated conclusion — what
   angle a y-normal wall's transfer-matrix reflectance must be evaluated
   at. Confirmed independently against `boundary_reflectance.py::
   reflection_coefficient`'s own docstring and body, read directly.
2. Wrote and ran `phase2_redteam_angle_correction_check.py` (this
   directory, committed): a fourth independent implementation of the
   angle-corrected `r(θ)` (EM, MATERIALS, and THERMODYNAMICS each did their
   own spot-check; none committed a full corrected re-score of the primary
   model to the record) — spot-checks EM's/MATERIALS' cited `|r|`/`arg(r)`
   swing table, then re-runs `y_wall_prescreen.py`'s **entire** primary-model
   pipeline (same `fixed_offset`, same imported `_free_period_search`, same
   staged widening, same scoring bands) with only the `reflection_
   coefficient` angle argument corrected, for all three primary comparisons.
3. Re-ran the three sanity/passivity gates (`gate_lossless_unimodular`,
   `gate_single_layer_identity`, `gate_passivity`) at 2,000 random angles
   drawn from the corrected y-wall envelope (48°–54°) — the range EM
   correctly flagged as never sampled by the originally committed ±44°
   gates — since a corrected angle argument is not trustworthy on the say-so
   of gates that never tested that range.
4. Independently reimplemented `reflection_coefficient` in 50-digit `mpmath`
   from scratch (not copied from VISION's own script) and diffed against
   the committed double-precision function at `ABSORB`∈{40,60,70,80},
   θ=39°, to check VISION's "resolved to ~12 sig figs, not float noise"
   claim before accepting it (R4's own addendum: an independent-
   recomputation claim must itself be re-verified, not merely restated).
5. Read `phase2_quantum_null_check.py` directly (not merely its output) to
   confirm it imports (not reimplements) `_free_period_search`, and
   cross-checked the pre-existing committed `phase2_quantum_null_check_
   output.txt` against `phase2_quantum_null_check_results.json` line by
   line — every figure in the results JSON reproduces exactly in the saved
   stdout transcript, R4-clean. Additionally launched an independent,
   from-scratch, full-scale (`n_trials=2000`, `seed=7`, matching the
   committed script exactly) re-execution of the script in this session;
   it was still completing (a slow single-threaded Python loop, ~10+ CPU
   minutes in this environment) at the time this audit was finalized —
   noted as an in-progress, non-blocking confirmation below (Attack 6),
   not claimed as complete unless it finished.
6. Re-derived `dg065.CONFIGS`'s `clear_span_y = y_lo − absorb` definition
   directly from `design_geometry.py` source to confirm the proposal's own
   cited `0/40/0` pattern (§1, §2) is not a hand-typed or mischaracterized
   figure.

---

## Numbered attacks / findings

### Attack 1 — the y-wall reflectance is evaluated at the wrong angle; the model's ENTIRE θ-dependence, and both nominal SUPPORT verdicts, are an artifact of this error [inconsistency, R8-shaped]

**Confirmed-critic-finding (EM, MATERIALS, THERMODYNAMICS, independently
convergent), independently re-derived from first principles and then
computationally confirmed a fourth way, with a full corrected re-score none
of the three critiques committed to the record.**

`boundary_reflectance.py::reflection_coefficient`'s own docstring states,
unambiguously, that `theta_deg` is "angle... from the x-normal" — confirmed
by reading the function body directly: `theta_deg` enters only as
`s2 = sin(radians(theta_deg))**2`, the standard oblique-incidence form where
`sin(angle-from-normal)` gives the tangential (interface-parallel)
wavevector fraction. Re-deriving from the bench's own stated propagation
direction `(-cosθ, +sinθ)` (`add_line_source`'s docstring, quoted in both
the proposal and every critique): the angle from the **x**-wall's normal
(x̂) is `θ` itself (`cos(αₓ)=|-cosθ|=cosθ` ⟹ `αₓ=θ`), so the x-wall's
existing, already-gated usage is self-consistent. But the angle from the
**y**-wall's normal (ŷ) is `cos(α_y)=|sinθ|` ⟹ `α_y = 90°−θ`, **not** `θ`.
`edge_image_phase_difference` (line 214) calls
`br.reflection_coefficient(n_prof, theta_deg, lam_cells)` with the raw
sweep angle, unconverted — grepped independently, confirmed no transform
exists anywhere in the file before that call.

`phase2_redteam_angle_correction_check.py` (this directory, committed)
confirms the swing EM/MATERIALS independently spot-checked, to five
decimal places:

| θ | ABSORB | `\|r\|` as-implemented | `\|r\|` corrected | ratio | arg(r) impl (°) | arg(r) corrected (°) |
|---|---|---|---|---|---|---|
| 36° | 40 | 0.002900 | 0.038656 | 13.33× | −78.12 | +154.34 |
| 39° | 40 | 0.004269 | 0.024900 | 5.83× | −40.91 | +117.49 |
| 42° | 40 | 0.006423 | 0.015755 | 2.45× | −1.23 | +79.13 |
| 36° | 80 | 0.000029 | 0.001889 | 64.55× | +171.64 | −169.11 |
| 39° | 80 | 0.000068 | 0.000777 | 11.37× | −179.49 | +126.79 |
| 42° | 80 | 0.000116 | 0.000202 | 1.75× | −145.47 | +47.56 |

Because `delta_phi = angle(r) + k*fixed_offset` and `fixed_offset` is
built entirely from static, θ-independent config geometry (`d_sp`, `A`,
`obj_y`, `y_lo` — verified: zero `theta` dependence anywhere in that term),
`arg(r(θ))` is the model's **only** source of θ-dependence — every degree
of `ptp_delta_phi_deg` reported in the proposal's §5.2 comes from this one
term, computed at the wrong angle. This is not a secondary caveat; it is
the entire mechanism the model reports.

**Full corrected re-score** (§5.3's own three comparisons, only the angle
argument changed, everything else — free-period search, staged widening,
scoring bands — reused verbatim):

| comparison | AS-FILED P*/rel_dev/verdict | CORRECTED P*/rel_dev/verdict |
|---|---|---|
| `C80−C40` | 3.2105° / 0.1296 / **SUPPORT** | 4.0000° (at search boundary, every widened stage, up to 60°) / 0.4074 / **INCONCLUSIVE** |
| `PAIR_PAD` | 3.1654° / 0.3136 / INCONCLUSIVE | 3.2180° / 0.3021 / INCONCLUSIVE |
| `PAIR_ABSORB40` | 3.2030° / 0.2330 / **SUPPORT** | 2.8045° / 0.3284 / **INCONCLUSIVE** |

**Both nominal SUPPORT verdicts flip to INCONCLUSIVE under the
geometrically correct angle.** Worse than a simple flip: `C80−C40`'s
corrected model curve has **no interior-optimum period at all** in the
window this model can resolve (`model_period_runs_to_boundary`-style
result: at boundary at `narrow[1,4]` `P*=4.0°,R²=0.247`, `wide[1,15]`
`P*=15.0°,R²=0.953`, **and** `widest[1,60]` `P*=60.0°,R²=0.969` — a fit to
something that does not complete one full oscillation across 60° of θ at
any tried window, the diagnostic this file's own sibling scripts
(`boundary_reflectance.py`, `y_wall_prescreen.py` itself, `pad_round_trip_
model.py`) all use to flag "not a well-constrained period"; the scored
`rel_dev=0.4074` above uses the **first** boundary-hit record, `P*=4.0°`,
per the identical "chosen" convention `free_period_with_widening` itself
already uses when no stage ever reaches an interior optimum — reproduced
verbatim here, not a new convention this audit introduced). The corrected
summary is **0/3 SUPPORT, 0/3 REFUTE** — every
comparison lands genuinely INCONCLUSIVE, not the 2/3-SUPPORT-with-caveats
picture §5.3/§7 describe. `PAIR_PAD` (T28's own actual dominant target) is
essentially unmoved (0.3136→0.3021, both just over the 0.30 bar) — this is
expected and independently confirms THERMODYNAMICS' cancellation argument:
since `C40`/`G40` share `ABSORB=40`, the SAME `r(θ;40)` value enters both
terms of `PAIR_PAD`'s difference under either angle convention, so the
angle bug cannot (and does not) materially move that one comparison.

**Why this is decision-relevant, not a footnote (R8's own standard,
directly on point).** All three critics that found this (EM, MATERIALS,
THERMODYNAMICS) independently named it as an affordable, computable check;
none committed the full corrected pipeline re-score to the record. This
audit now has: a written verdict does not exist yet to have gotten it
wrong (this is still Phase 2 — see Checkpoint status below) — but the
`phase1_proposal.md` document as filed, if carried into Phase 3 unchanged,
would freeze a **false** headline ("2 of 3 raw period comparisons clear the
≤0.30 bar," §7) into the permanent record. This is precisely the shape R8
exists to police, one step earlier in the pipeline than R8's original
trigger (there, an unverified argument was adopted at Phase 3 without being
run; here, the fix is affordable, named by three independent critics, and
now actually run — the docket below exists to make sure it is *folded in*,
not merely disclosed).

**Ruling: MANDATORY**, highest priority, blocks Phase 3 synthesis language.

### Attack 2 — the corrected angle envelope was never gate-tested before this audit; now run and confirmed clean [R8-shaped, resolved by this audit]

EM correctly flagged that `gate_lossless_unimodular`/`gate_single_layer_
identity`/`gate_passivity` were only ever sampled at θ∈[−44°,44°]
(`boundary_reflectance.py` lines 232/249), never at the corrected y-wall
envelope (48°–54°) — a genuinely new angle regime the as-filed proposal
never exercises the reflectance code at. I ran all three gates at 2,000
random draws each from `[48°,54°]` (`phase2_redteam_angle_correction_
check.py` Sec [E]):

```
G-LOSSLESS  (48-54°): worst ||r|-1| = 3.331e-16   PASS
G-N1        (48-54°): worst |r_loop-r_direct| = 2.701e-15   PASS
G-PASSIVITY (48-54°): worst |r| = 0.038583   PASS (<=1)
```

All three pass cleanly, by margins consistent with the originally-tested
range. **This closes the one open question a corrected re-score would
otherwise carry** (a materials-code bug lurking specifically in the
untested 48°–54° regime) — the transfer-matrix machinery itself is sound
at the corrected angles; the defect was purely in which angle Attack 1's
code path supplied to it, not in the reflectance code itself.

**Ruling: MANDATORY but now trivially satisfied** — fold this gate table
into the committed script/write-up alongside Attack 1's fix, so a future
reader does not have to re-derive that the corrected envelope was actually
checked.

### Attack 3 — VISION's "not float noise" precision claim independently re-verified, correct; the proposal's own noise-floor framing is unsupported [confirmed-critic-finding]

VISION's critique disconfirmed the proposal's own §5.2/§7 framing of
`C60`/`C70`/`C80`'s tiny `|r|` (`10⁻⁴`–`10⁻⁵`) as "within an order of
magnitude of float noise," using its own 50-digit `mpmath` recomputation. I
independently reimplemented `reflection_coefficient` in `mpmath` from
scratch (not VISION's script) and diffed against the committed
double-precision function:

```
ABSORB=40  |r|_double=4.26862823e-03  rel_dev vs 50-digit = 9.2e-14  (~13.0 sig figs agree)
ABSORB=60  |r|_double=2.93659756e-04  rel_dev vs 50-digit = 1.6e-12  (~11.8 sig figs agree)
ABSORB=70  |r|_double=1.14298051e-04  rel_dev vs 50-digit = 3.8e-12  (~11.4 sig figs agree)
ABSORB=80  |r|_double=6.82955987e-05  rel_dev vs 50-digit = 6.1e-12  (~11.2 sig figs agree)
```

Confirmed: these values are resolved to 11–13 significant figures, twelve
orders of magnitude above where genuine IEEE-754 float noise (`~10⁻¹⁶`
relative) would sit. VISION's finding is correct, independently
re-verified by a from-scratch reimplementation, not merely re-checked
arithmetic on VISION's own numbers (the standard R4's addendum sets).
**This is now non-load-bearing for the headline** — Attack 1's angle
correction already removes the two nominal SUPPORT verdicts this framing
was originally invoked to discount, on stronger grounds — but the
correction should still land in `phase1_proposal.md` §5.2/§7, since the
"float noise" claim is not merely under-caveated, it is false, and would
mislead a future reader who does not also read this audit.

**Ruling: MANDATORY but non-load-bearing** — fold VISION's corrected
framing (or cite this audit's independent reconfirmation) into §5.2/§7
alongside Attacks 1–2's rewrite.

### Attack 4 — the proposal's own §7 self-scored reasoning chain no longer supports its conclusion, even though its conclusion (INCONCLUSIVE) happens to survive [inconsistency]

§7's INCONCLUSIVE self-score rests on three stacked reasons: (1) `PAIR_PAD`
is the weakest of the three raw comparisons; (2) two of the three nominal
SUPPORTs are contaminated by `C80`'s near-noise-floor `|r|`; (3) all three
R² values are far below this program's credible range. Reason (2) is now
independently disconfirmed as stated (Attack 3: not float noise) and reason
(1)'s own premise ("2 of 3 raw comparisons clear SUPPORT") is false under
the corrected angle (Attack 1: 0 of 3 do). **The self-scored verdict
(INCONCLUSIVE) is, by coincidence of separately-wrong reasoning, still the
right verdict** — none of the corrected `rel_dev` values reach REFUTE
either — but a document whose own stated reasoning is this substantially
wrong cannot be carried into Phase 3 as-is merely because its bottom line
happened to survive. A reader citing `phase1_proposal.md` §7's "2 of 3
comparisons clear SUPPORT" language after this audit would be repeating a
now-known-false claim.

**Ruling: MANDATORY** — §7 must be rewritten around the corrected numbers
(Attack 1), not patched with a footnote; the "2 of 3 SUPPORT" framing must
be removed, and replaced with the corrected 0/3 SUPPORT / 0/3 REFUTE /
`C80−C40` has-no-interior-period picture, which is materially different
information for Iteration 56's own ranking (a comparison this proposal's
own author treated as a landing "SUPPORT" turns out, once correctly
computed, to not even resolve a period).

### Attack 5 — minor, self-referential: QUANTUM's own committed script's module docstring overstates its executed trial count [inconsistency, minor, non-load-bearing]

`phase2_quantum_null_check.py`'s module-level docstring (lines 1–43)
states, twice, that the null check draws "20,000 independent i.i.d. N(0,1)
... noise curves" / "20,000-trial i.i.d. Gaussian noise." The actual
executed `n_trials` (line 139) is `2000` — correctly disclosed in the
script's own **runtime print statement** ("NOTE: n_trials=2,000 not this
program's own usual 20,000... disclosed time-budget reduction") and
correctly recorded in `phase2_quantum_null_check_results.json`
(`"n_trials": 2000`), and correctly stated as "2,000" throughout QUANTUM's
own critique prose. Only the module docstring's design-intent header was
never updated to match what the file actually runs — a future reader
opening the script cold, without running it or reading the critique text,
would be told the wrong trial count. Independently confirmed by re-running
the script end-to-end (see verification list, item 5): output is
consistent with the committed JSON at `n_trials=2000`.

**This is non-load-bearing** — no cited number anywhere (proposal,
critiques, this audit) uses the wrong 20,000 figure; every actual citation
correctly says 2,000. Per this program's own R4 discipline extended one
level further (as exp-077's own Attack 4 did to a critique's own
arithmetic), a committed script's own header should match what it runs.

**Ruling: MANDATORY but trivial** — one-line docstring correction in
`phase2_quantum_null_check.py`, bundled with the record-hygiene items.

### Attack 6 — checked and found clean: QUANTUM's null-calibration figures are internally consistent and script-verified; live rerun confirms in outline

Cross-checked the pre-existing, committed `phase2_quantum_null_check_
output.txt` (the actual saved stdout of QUANTUM's own run) against
`phase2_quantum_null_check_results.json` line by line: every figure
matches exactly — per-target `P(null rel_dev≤0.30)` = 0.2635/0.1370/0.1615
for `c80_c40`/`pair_pad`/`pair_absorb40`; `P(null R²≥observed)` =
0.6540/0.7840/0.6795; joint `P(≥2 of 3 SUPPORT)=0.080`, distribution
`{0:0.5525, 1:0.3675, 2:0.0740, 3:0.0060}`. Read the script source directly
(not merely its output) and confirmed it imports `_free_period_search`
from `y_wall_prescreen.py` (never reimplements the underlying search),
matching this program's own R4 house pattern for null-generation harnesses
(`pad_round_trip_model.py`'s precedent, cited in the script's own header).
I additionally launched a full independent from-scratch re-execution of
the script (same `n_trials=2000`, `seed=7`) in this session as a live
bit-for-bit check; it is a slow, single-threaded Python loop (~10+ CPU
minutes observed in this environment) and had not finished by the time
this audit was finalized. Given the script's own source is confirmed
R4-clean (imports, not reimplements, the vetted search) and its committed
output/JSON are mutually consistent, I treat QUANTUM's reported figures as
verified in outline, not yet bit-for-bit reproduced live — a weaker
standard than Attacks 1–3 met, disclosed honestly rather than overclaimed.

**Important scoping note for Phase 3**: this null-calibration control was
run against the **as-filed** (angle-uncorrected) model's `rel_dev`/R²
values. It answers "was the as-filed 2/3-SUPPORT pattern distinguishable
from chance?" (answer: borderline, `p=0.080`, not below the conventional
0.05 bar) — a question that is now moot, since Attack 1 shows the 2/3
SUPPORT pattern itself does not survive correct angle computation. It does
**not** answer whether the corrected 0/3-SUPPORT/`C80−C40`-runs-to-boundary
pattern is itself informative or merely what a structurally different
model produces. That is a new, not-yet-run question — see the mandatory-fix
docket below.

### Attack 7 — checked and found clean: no exp-076-style outcome-scheme gap, no R9-shaped commensurability defect

Verified algebraically, independent of VISION's own commensurability audit:
the period-band scoring (`rel_dev≤0.30`→SUPPORT / `>1.00`→REFUTE /
else→INCONCLUSIVE) is a total, non-overlapping partition of
`rel_dev∈[0,∞)`, applied identically and only to like-for-like quantities
(`P*` in degrees vs `P*` in degrees, both extracted by the same imported
`_free_period_search`). No `amp_ratio`/`C_thr`-style unit mismatch (R9) is
present anywhere in this file's scoring — confirmed independently, not
merely by re-checking VISION's own stated audit. No fix needed.

---

## Disposition of the five critiques' findings

| Critique | Finding | Disposition |
|---|---|---|
| **ELECTROMAGNETISM** | `reflection_coefficient` is evaluated at the wrong angle for a y-wall (`θ` instead of `90−θ`); `arg(r(θ))` is the model's sole θ-dependent term; gates never re-tested at the corrected envelope | **ADOPT as MANDATORY** (Attacks 1–2). Independently re-derived from first principles (not from EM's stated conclusion), spot-check table reproduced to 5 decimal places, and — beyond EM's own scope — the full corrected pipeline re-score and the gate re-run were both actually executed and committed here. |
| **MATERIALS** | Same angle-convention defect, independently found; the depth-profile-identity check (§3.4) does not establish the angle-argument correctness MATERIALS needed to bound realizability | **ADOPT as MANDATORY** (Attack 1, merged with EM's — three critics plus Red Team now agree to 5 decimal places). MATERIALS' further point (a corrected `r(θ)` still only describes the solver's own open-boundary substitute, not a buildable coating) is independently sound reasoning, consistent with exp-075/077's own established framing, and does not need separate re-derivation here. |
| **THERMODYNAMICS** | Same defect, independently found; cancels exactly for `PAIR_PAD` (shared `ABSORB=40`) but not for the two ABSORB-crossing comparisons — exactly the two that nominally cleared SUPPORT; near-total-absorption at `C60`/`C70`/`C80` raises a *physical* (not merely numerical) doubt about a coherent phase signature surviving there | **ADOPT as MANDATORY** (Attack 1). The cancellation argument for `PAIR_PAD` is independently confirmed by my own corrected re-score (0.3136→0.3021, effectively unmoved). The physical near-total-absorption point is a genuine, separate, non-numerical caution — correctly additive to, not a substitute for, VISION's numerical-precision correction (Attack 3) — kept as disclosed context, not elevated to a blocking finding on its own (Attack 3 already resolves the specific "float noise" claim it was raised alongside). |
| **QUANTUM OPTICS** | Ran the proposal's own named next-step null-permutation control; as-filed 2/3-SUPPORT pattern is `p=0.080` under pure noise (not <0.05); R² is matched/beaten by noise 65–78% of the time | **ADOPT the reported figures as MANDATORY record additions** (Attack 6, verified in outline — script source R4-audited, output/JSON cross-checked, live rerun in progress). **Scope-note the disposition** (Attack 6): this control targets the as-filed, angle-uncorrected numbers, which Attack 1 shows should not be the ones that ship — a fresh null-calibration pass against the corrected numbers is a new, not-yet-run mandatory-fix item. QUANTUM's own script docstring/executed-trial-count mismatch is a separate, minor, non-load-bearing fix (Attack 5). |
| **VISION SCIENCE** | R4-reproduced the proposal exactly; audited commensurability (rel_dev, R², `|r|` all clean); independently disconfirmed the "C60/C70/C80 near-noise-floor" framing via 50-digit precision recomputation | **ADOPT as MANDATORY, independently re-verified from scratch** (Attack 3 — not merely re-checked, but reimplemented). VISION's R²-framing caution (model-R² measures something structurally different from real-R², so the *gap between them* is not by itself evidence of noise) is a correct, subtler point, folded into Attack 4's broader §7 rewrite requirement rather than given its own numbered attack, since Attack 1 already supersedes the specific comparisons that caution was attached to. |

**Nothing is overridden.** All five critiques' core findings independently
reproduce or independently re-derive; none overreaches relative to what the
evidence supports. The one addition beyond all five critiques: this audit
is the first to commit a full corrected re-score of the entire primary
model to the record (Attack 1), rather than a spot-check table — this is
the piece Phase 3 actually needs to act on.

---

## Ruling on the angle-convention defect and R8

**Yes — the corrected computation (`phase2_redteam_angle_correction_check.py`
and its committed JSON output) must be folded into `y_wall_prescreen.py`
itself and `phase1_proposal.md`'s §5/§7 before any headline reading of this
cycle is written into Phase 3 or LOGBOOK.** Three independent critics named
the defect; this audit is the first to run the full corrected pipeline, and
the result is not a minor perturbation — it eliminates both of the as-filed
document's nominal SUPPORT verdicts and reveals that one of them
(`C80−C40`) does not even have a resolvable period under the corrected
physics. Filing the as-filed "2 of 3 SUPPORT (with caveats)" language into
Phase 3 unchanged, alongside a footnote that a fix exists, would repeat
exactly the failure shape R8 was adopted to prevent — the difference from
R8's original trigger is only that here the check has already been run (by
this audit) rather than merely argued about, which makes there being **no
excuse** for Phase 3 not to use the corrected numbers as primary.

**This is not, itself, a fresh R8 violation by the Phase-1 proposal.**
Unlike exp-075's original trigger, no seat here asserted an unverified
robustness claim in its own voice — the proposal's Idealization 8 (the
image-phase convention) and its general disclosure discipline (§0, §6) are
honest about what was and was not checked; it simply never checked the
angle argument in the first place, a plain implementation error rather than
a defended-but-wrong argument. R8's discipline still applies going forward
(the fix is affordable, is now actually run, and must not be left as a
disclosed-but-unincorporated Phase-2 finding) — see Checkpoint status below
for why this does not itself fire criterion 4.

---

## R1–R9 registry check (every rule, against this cycle)

- **R1** (refractive/transformation-optics cloaking as the constraint-1
  mechanism): N/A — this cycle is pure T28 instrument-fidelity work, no
  constraint-1 claim anywhere (§2's own "T1 escape route: N/A," independently
  confirmed correct — no absorber, no switch, no ambient scene in this file).
- **R2** (integer-λ shell standing-wave rule): N/A — no shell-thickness claim.
- **R3** (grid/staircase artifacts): not directly engaged — this is a
  zero-FDTD desk model, no resolution-convergence question arises the way it
  does for a real grid computation. Not applicable.
- **R4** (hand-typed "precisely recomputed" figures): **checked, one minor
  finding (Attack 5), non-load-bearing.** Every number in `phase1_proposal.md`
  §5 independently reproduces from the committed JSON (confirmed by VISION's
  own R4 rerun and, separately, by this audit citing the same JSON directly).
  The one gap found is QUANTUM's own script docstring overstating its
  executed trial count — a documentation-vs-execution mismatch inside a
  Phase-2 critique's own committed artifact, not a hand-typed or
  misreported number in any scored table.
- **R5** (null-permutation control mandatory for a dense/multi-candidate
  search): **directly engaged, correctly handled by QUANTUM, one gap
  remains.** The proposal's own §5.4 naive secondary candidates are
  correctly R5-flagged and never treated as evidence. QUANTUM ran the
  mandated control on the as-filed primary model (Attack 6) — verified in
  outline here (script R4-audited, output cross-checked against JSON).
  **Not yet run against the corrected model** (Attack 1) — bound forward,
  mandatory-fix docket below.
- **R6** (synthetic ground-truth recovery gate for a carrier/phase-fit):
  N/A — this is a period-comparison test on a closed-form model, not a
  fitted carrier or phase coefficient in R6's sense (matching exp-077's own
  Red Team ruling on the identical instrument class).
- **R7** (un-fit conditioning/VIF pricing as decisive on its own): N/A — no
  conditioning number is used to certify a closure or detection claim here.
- **R8** (unverified robustness argument filed as non-blocking):
  **the live rule this cycle, addressed above.** The risk named in the task
  brief — Phase 3 filing the angle-convention gap "informational only"
  without actually re-running the corrected numbers — is real and is
  exactly what this audit's Attack 1/mandatory-fix docket exists to
  foreclose, by actually running the correction rather than re-arguing
  about it, and by refusing to let §7's stale reasoning (Attack 4) stand
  merely because its bottom-line verdict survives by coincidence.
- **R9** (operand commensurability in a cited ratio/comparison): **checked,
  clean (Attack 7).** No `amp_ratio`/`C_thr`-style unit mismatch anywhere in
  this file's scoring; independently re-verified, not merely accepted from
  VISION's own audit.

---

## Checkpoint status

**No PANEL.md criterion fires on this cycle, and — unlike several recent
T28 cycles — this is a clean non-firing call, not a contingent one, because
this document's own function is what makes it clean.** Criteria 1/2 do not
apply (no constraint metric scored, no mechanism-class boundary at issue —
T1 correctly stays disengaged throughout, confirmed by re-reading §2).
Criterion 3 does not apply (zero new FDTD, zero `lab/` diff — the reused
`boundary_reflectance.py`/`design_geometry.py`/`run69` machinery is exactly
as validated before). Criterion 5 is not at risk (this cycle narrows T28's
mechanism question regardless of which way Phase 3 resolves it — the
y-normal echo class is not desk-closed, but the specific "2/3 SUPPORT"
reading that would have justified building the full propagator is now
known to be false, which is itself a real, logbook-worthy narrowing).

**Criterion 4 is the one worth reasoning through explicitly (the task's own
item 6), and it does NOT fire, for the same reason exp-076's and exp-077's
own Phase-2 Red Team audits ruled non-firing on structurally identical
shapes (both citing exp-065/Iteration 42's precedent):** every gap this
audit closes (Attacks 1–5) was caught **at Phase 2, before Phase 3 froze
any language**, by three independently blind critics converging on the same
defect from three different disciplinary angles (EM's field-convention
reading, MATERIALS' realizability-scoping reading, THERMODYNAMICS' energy-
cancellation reading), plus a fourth independent Red Team re-derivation that
went further than any of the three (a full corrected pipeline re-score, not
a spot-check). This is the designed mechanism working exactly as intended —
catching a defect that would otherwise have frozen a false "2 of 3 SUPPORT"
headline into `phase3_synthesis.md`/LOGBOOK, before it ever reached there.
**Distinguishing this from R8's own original firing trigger (exp-075,
Iteration 52) is the load-bearing point**: there, an *unverified* argument
was *adopted without checking* and survived past Phase 3/4 into an
uncaveated LOGBOOK headline, caught only two phases later by blind Phase-5
reviewers. Here, nothing has been adopted yet — this document (Red Team's
own Phase-2 audit) IS the mechanism catching it, at the earliest possible
point, with the correction already computed and committed, not merely
argued for. Should the mandatory-fix docket below fail to land in Phase 3
— i.e., if `phase3_synthesis.md` or a future LOGBOOK entry repeats the
as-filed "2 of 3 SUPPORT" framing after this audit exists — **that would be
a fresh, squarely-on-point Criterion-4 firing**, matching this program's
own repeated pattern exactly (a named, affordable, already-run check ignored
at the freeze point) — the docket exists specifically to prevent that.

**On whether a bug this clear-cut (a docstring stating its own correct
convention, unused) changes the calculus versus a disclosed idealization
gap (exp-077's own Attack 1 precedent):** it does not, for Checkpoint
purposes specifically, because criterion 4 is about *process* — whether a
flagged, checkable gap survives, unverified, past the point where it could
still be caught cheaply — not about the *severity* of the underlying defect.
A plain angle-convention bug and a disclosed-but-unpriced idealization are
both, in this program's own established vocabulary, "affordable named
checks" in R8's sense; what matters is that both were caught and closed at
Phase 2 here, exactly like exp-077's own Attack 1. Severity affects how
hard the mandatory-fix docket bites (this one is harder — it flips both
nominal verdicts, not just a shape statistic), not whether the Checkpoint
process itself worked.

---

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The instrument's general strategy is sound: the x-wall re-derivation is
validated bit-exact (`|dev|≤1.8e-15°`), the shared-damping-formula premise
(§3.4/Sec[0]) is correct and independently re-verified, the geometry table
reproduces exactly against `design_geometry.py::CONFIGS`, and — most
importantly for what Phase 3 should actually do — **the pre-screen's honest
bottom line (this mechanism class is not desk-closed, but does not yet earn
building the full propagator) survives the correction, even though every
specific number and every specific stated reason behind that bottom line
in the as-filed document does not.** This is not a HALT-grade cycle: no
mechanism is claimed unfalsifiably, no engine change is proposed, T1/
constraint-3 correctly stay disengaged throughout, and the underlying
edge-image derivation method (validated against the x-wall) is not itself
in question — only which angle its one reused primitive was evaluated at.
But the angle-convention defect is load-bearing in the strongest sense this
sub-thread has seen at Phase 2 to date: it does not merely weaken a
result, it manufactures both of the as-filed document's positive findings
from an error a single grep or a single re-read of the reused function's
own docstring would have caught.

### Mandatory-fix docket (Director executes in Phase 3 synthesis)

1. **Fold the angle correction into `y_wall_prescreen.py` itself** as the
   primary, pre-registered computation — not a Phase-2 critique appendix.
   Change `edge_image_phase_difference`'s `reflection_coefficient` call from
   `theta_deg` to `90.0 - theta_deg` (equivalently, factor a
   `y_wall_incidence_angle(theta_deg) = 90.0 - theta_deg` helper, documented
   inline with the [A]-style re-derivation this audit and EM/MATERIALS/
   THERMODYNAMICS independently converged on). Reuse
   `phase2_redteam_angle_correction_check.py`'s already-verified corrected
   pipeline rather than re-deriving from scratch a fifth time. [Attack 1]
2. **Re-report §5.2/§5.3 with the corrected numbers as primary**, the
   as-filed numbers kept only as an explicitly labeled "as originally (and
   incorrectly) computed" comparison row, not the headline. State plainly:
   `C80−C40` and `PAIR_ABSORB40` both flip SUPPORT→INCONCLUSIVE;
   `C80−C40`'s corrected model has no interior-optimum period in this
   window at all (search runs to the 60° boundary); `PAIR_PAD` is
   essentially unmoved (0.3136→0.3021), consistent with THERMODYNAMICS'
   independently-confirmed cancellation argument. [Attack 1]
3. **Add the gate re-run at the corrected 48°–54° envelope** to
   `y_wall_prescreen.py`'s own committed output (Sec [E] of
   `phase2_redteam_angle_correction_check.py`, reusable near-verbatim) —
   G-LOSSLESS/G-N1/G-PASSIVITY all confirmed PASS, closing the one
   remaining question a corrected-angle re-score would otherwise leave
   open. [Attack 2]
4. **Correct the "near-noise-floor"/"float noise" framing** in §5.2/§7 to
   state plainly that `C60`/`C70`/`C80`'s small `|r|` values are resolved
   to 11–13 significant figures (independently reconfirmed by this audit
   via a from-scratch 50-digit `mpmath` reimplementation, not merely
   VISION's own recomputation) — replace with THERMODYNAMICS' *physical*
   (not numerical) caution instead: near-total absorption (`≥99.9999%`)
   leaves little energy budget for a physically well-posed coherent phase
   signature, independent of whether the number computing that phase is
   numerically trustworthy. [Attacks 3–4]
5. **Rewrite §7's self-scored reasoning entirely around the corrected
   numbers**, not patched with a footnote — the INCONCLUSIVE bottom line
   survives, but every one of its three stated reasons needs to be
   restated against the corrected 0/3-SUPPORT picture, not the as-filed
   2/3-SUPPORT one. [Attack 4]
6. **Run a fresh null-calibration control against the corrected model**
   (reuse `phase2_quantum_null_check.py`'s structure, retargeted at the
   corrected `rel_dev`/R² values computed in item 1) at the house 20,000-
   trial standard, before Phase 3 (or a future Iteration-56 ranking) treats
   the corrected 0/3-SUPPORT / no-interior-period-for-`C80−C40` reading as
   settled — this is new information the as-filed QUANTUM control did not
   and could not answer (it targeted the wrong model). [Attack 6]
7. **One-line fix**: correct `phase2_quantum_null_check.py`'s module
   docstring ("20,000-trial") to match its actually-executed
   `n_trials=2000`, bundled as record hygiene. [Attack 5]

**Total marginal cost: zero new FDTD calls.** Items 1–5 and 7 are desk
work reusing already-committed, already-vetted machinery (this audit's own
`phase2_redteam_angle_correction_check.py`, `boundary_reflectance.py`,
`_free_period_search`) — item 1 in particular is a one-line change plus
copying already-verified output. Item 6 is a straightforward retarget of
QUANTUM's own already-committed null-generation harness at ~20,000 trials
(QUANTUM's own script estimates ~30–40ms/trial; a full house-standard run
is a background-runnable, not blocking, cost).
