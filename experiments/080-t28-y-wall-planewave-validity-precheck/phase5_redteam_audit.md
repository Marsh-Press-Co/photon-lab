# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 57 · exp-080
## Adjudicating all six blind Phase-5 reviews of EM's plane-wave/global-steering validity pre-check: independently re-deriving PHOTONICS' E_direct-cancellation proof, EM's far-field-limit derivation, and QUANTUM's scoring-methodology finding from primitives; reasoning through whether the three, combined with the missing NOTES.md and the un-scored part_d verdict, fire Checkpoint criterion 4; and reconciling Iteration 58's queue

**Seat: RED TEAM.** Fresh sub-agent. Read, in order: `PANEL.md` in full,
`AGENTS.md` in full, this cycle's complete record —
`phase1_proposal.md` (incl. PHASE 1 RESULTS), `validity_precheck.py` as it
now stands post-Phase-3, `validity_precheck_results.json`, all five Phase-2
critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`phase4_results.md`, `_output.txt` — then all six Phase-5 reviews
(`phase5_review_{photonics,materials,em,thermodynamics,quantum,vision}.md`).
For background: `experiments/079-.../phase5_redteam_audit.md` (model, not
copied), `experiments/079-.../phase5_review_photonics.md` §4 (PHOTONICS'
original construction sketch), `y_wall_aperture_sum.py`,
`boundary_reflectance.py`, `design_geometry.py` directly, and
`LOGBOOK.md`'s RULED-OUT registry (R1–R9) and the T28 thread tail
(Iterations 46–56). I alone see the complete record and all six blind
Phase-5 reviews, and speak last.

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this
document or by anything it adjudicates.** Independently re-confirmed by my
own fresh grep (§0.7) — matching VISION's own Phase-2 and Phase-5 findings
a third time, on material neither of those documents could have seen in
full (this document itself).

---

## 0. What I independently verified

I was directed to re-verify, from primitives, the three findings most
consequential to what this record should say and what Iteration 58 should
do — PHOTONICS' `E_direct`-cancellation proof, EM's far-field-limit
derivation, and QUANTUM's "wrong scoring methodology entirely" claim —
before ruling on anything. I did not stop at those three; every numeric
table below was recomputed in a fresh scratch script
(`/tmp/.../scratchpad/`, session-local, never importing `validity_precheck.py`
itself except where noted), importing only the same already-gated
primitives the cycle's own record imports.

### 0.1 PHOTONICS' `E_direct(θ_beam)` cancellation proof — **VERIFIED, independently, from scratch**

PHOTONICS' claim: an `E_direct(θ_beam)` term built the one physically
natural way (the same taper/driven-phase convention as the echo term,
propagated over the **direct**, unmirrored source-to-observer distance
`hypot(D_SP, OBJ_Y−y_s)`, no wall, no `r()`) is **bit-identical across all
five congruent configs**, because `D_SP`, the aperture width, and the
taper are all congruent-series constants, and `OBJ_Y`/`y_lo` both shift by
the identical `PAD` — so substituting `u=y_s−OBJ_Y` makes every ingredient
of `E_direct` a function of `u` alone, with no `PAD` or `ABSORB`
dependence anywhere.

I re-implemented this from scratch (not calling PHOTONICS' own
description, only the same lower primitives `validity_precheck.py`
imports — `dg065.CONFIGS`, `ywas.build_aperture_grid`/
`aperture_amplitude`/`source_driven_phase`, `K600`) and swept 5 `θ_beam`
values:

```
max|E_direct(cfg) - E_direct(C40)| across the theta grid:
  C40: 0.0   C60: 0.0   C70: 0.0   C80: 0.0   G40: 0.0
```

**Exact match to PHOTONICS' own reported result — 0.0, not merely small.**
I also independently confirmed the *reason*, not just the number, by
reading `design_geometry.py` directly: `obj_y = BASE_OBJ_Y + pad`,
`y_lo = BASE_ABSORB + pad`, `d_sp` fixed at 223 cells for the whole
congruent series, `aperture_cells` fixed at 1504 — so `A = obj_y − y_lo =
752` is PAD-invariant by the congruent series' own design, exactly as
PHOTONICS' derivation states. This is a genuine, load-bearing, correct new
finding — not a restatement.

**One qualification I add, not present in PHOTONICS' own review**: this
proof is conditioned on `E_direct` being defined the one way consistent
with the x-wall's own established `E=E_d+r_coeff·E_i` convention — PHOTONICS
says this itself (§4, "Caveat, stated honestly"), and I agree it is the
*only* definition consistent with what "E_direct" is required to mean by
the method-of-images structure this whole y-wall program borrows from the
x-wall, not an arbitrary choice invented to make the proof work.

### 0.2 EM's far-field-limit derivation — **VERIFIED, independently, from scratch**

EM's claim: `theta_local(y_s)`'s own far-field limit, as `D_SP→∞` with
`OBJ_Y`/`y_lo`/`y_hi` fixed, is **~90° (grazing)**, uniformly, for every
`y_s` — never `90°−θ_beam`'s swept `48°–54°` range — because
`theta_local(y_s)=atan(D_SP/(OBJ_Y+y_s))` has **zero** `θ_beam`
dependence by construction, so it cannot converge to a `θ_beam`-tracking
quantity regardless of near/far-field regime.

I re-derived EM's own `D_SP`-scaling table from scratch, importing only
`dg065.CONFIGS` and `ywas.theta_local_deg` directly (not
`validity_precheck.py`):

| `D_SP` scale | my `theta_local` envelope | my spread ratio | EM's reported envelope/spread |
|---|---|---|---|
| 1× | `[5.4531°,15.0043°]` | `2.7515×` | `[5.45°,15.00°]` / `2.75×` — match |
| 10× | `[43.6701°,69.5397°]` | `1.5924×` | `[43.67°,69.54°]` / `1.59×` — match |
| 100× | `[84.0199°,87.8633°]` | `1.0457×` | `[84.02°,87.86°]` / `1.05×` — match |
| 1000× | `[89.3998°,89.7862°]` | `1.0043×` | `[89.40°,89.79°]` / `1.004×` — match |

**Exact match at every scale.** The mathematical point is elementary and
airtight once stated: `atan(x)→90°` as `x→∞`, for **any** fixed
`(OBJ_Y+y_s)` — a scalar limit that cannot depend on the unrelated,
independently-swept parameter `θ_beam`. Two constructions where one is
strictly parameter-independent (`theta_local`) and the other strictly
parameter-dependent (`90°−θ_beam`) cannot converge to each other in any
regime; EM's derivation is not merely plausible, it is a direct
consequence of `theta_local`'s own docstring-stated independence from
`θ_beam`, which every file in this sub-thread since exp-078 has already
established and never disputed.

**I also independently re-derived the adjacent claim** — that
`y_wall_aperture_sum.py`'s own G-LOSSLESS/G-N1/G-PASSIVITY gates were
validated only over `[global_lo,global_hi]`, computed as
`min(all_lo)−0.5, max(all_hi)+0.5` across the 5 configs' own
`theta_local` envelopes. Reading `y_wall_aperture_sum.py` lines 341–353,
402–404 directly: this is exactly what the code does, and from `part_a`'s
own committed numbers (`env_lo=5.2735°`, `env_hi=15.0043°`),
`global_lo=4.7735°`, `global_hi=15.5043°` — matching EM's cited
`[4.77°,15.50°]` to the printed digit. I confirmed independently, with a
fresh 200-point sweep of `reflection_coefficient_vec` at incidence angles
covering and extending past `[36°,60°]`, that `photonics_image_term_curve()`
and `part_c_power_budget_at_true_angle()` both evaluate this function at
`90°−θ_beam∈[48°,54°]` — **entirely outside** `[4.77°,15.50°]`. **This gap
is real, confirmed independently, not merely restated.**

### 0.3 QUANTUM's "wrong scoring methodology entirely" claim — **VERIFIED, independently, against the primary source**

QUANTUM's claim: `photonics_image_term_curve()` differs from PHOTONICS'
own original exp-079 §4 sketch in **two compounding ways**, not one —
missing `E_direct` (already known/flagged) **and** a wrong scoring
methodology, because the original sketch specified scoring the *total*
field against the **real T28 reference periods** via
`_free_period_search`/`score_period`, never an R²-shape-comparison
against exp-079's own per-point candidate curve.

I read `experiments/079-t28-y-wall-full-aperture-sum/phase5_review_photonics.md`
§4 directly (not from QUANTUM's quotation) and confirm the exact language,
step 4 of the "concrete derivation route":

> **Total field:** `E(θ_beam) = E_direct(θ_beam) + r(90°−θ_beam;ABSORB) ·
> E_image_unweighted(θ_beam)`, scored by the identical
> `_free_period_search`/`score_period` machinery every T28 cycle since
> Iteration 46 has used.

**Confirmed verbatim, at the primary source, not merely as QUANTUM
paraphrased it.** `photonics_image_term_curve()`/
`part_d_photonics_construction()`, as actually committed, does neither
half of this: it omits `E_direct` (already flagged) and scores by R²
against `y_wall_aperture_sum_results.json`'s own per-point curve — a
**different theoretical candidate model**, not real T28 data, and a
**different comparison methodology** (shape-fit R², not a free-period
fit) than PHOTONICS ever specified. QUANTUM's characterization
("compounding, not one gap") is accurate, and — checking one level
deeper, since this is the finding the task asks me to weigh most heavily
— I confirm QUANTUM's related point that `echo_field_curve()`'s own
`E_echo` is *itself* echo-only (no `E_direct` on either side of the
comparison already run), by reading that function's own docstring
directly: it computes "the per-point complex contribution to the
REFLECTED (echo) field," nothing else. So part (d)'s current R² test is
internally consistent on its own narrow terms (echo-only vs. echo-only) —
QUANTUM is right that the record's stated justification for the omission
("valid only insofar as it cancels... across pair deltas") is the wrong
justification for *that* narrow point, and the *real* stakes of the
omission are about the free-period test that has never been run, where
`E_direct` is expected (per PHOTONICS' own exp-079 feasibility probe) to
be the dominant carrier of whatever real period content exists.

**Net: QUANTUM's finding is correct at both levels it makes it — the
methodology substitution is real, confirmed against the primary source,
and the internal-consistency nuance about `echo_field_curve` being
echo-only is also independently confirmed.**

### 0.4 Everything else, independently spot-checked

| # | Claim | Source | My result |
|---|---|---|---|
| 1 | `d_F=113,100.8` cells; `dist_ratio` `0.76–2.15%`; `theta_local` spread `2.60–2.75×`, all 5 configs | Phase 1 / Phase 2 audit | Re-derived from raw `dg065.CONFIGS`; bit-identical, all 5 configs |
| 2 | `part_b`/`part_b_realizable` mean `R²=0.7345`/`0.4305`, C70 min `0.5214`, C40 realizable `−0.6230` | Phase 1, MATERIALS | Bit-identical to the printed digit (5th independent reproduction of this figure across this cycle's own record) |
| 3 | `part_d_photonics_construction` raw/scale-corrected R² per config | QUANTUM, Red Team Phase-2 | Reproduced via a fresh integral (not calling the committed function): C70 scale-corrected `R²(Re)=0.0852`, mean `0.6020` — matches to 4 decimals |
| 4 | `\|r(90°−θ_beam)\|` worst case `0.0853` at ABSORB=40, incidence angle 60° (extended sweep) | EM Phase-5 | Reproduced exactly: `0.08530802...` at ABSORB=40, θ=60°; at the *actual* used range `θ∈[48°,54°]` (θ_beam∈[36°,42°]), worst `=0.038656`, consistent with `part_c`'s own `reflected_power_fraction_max=1.494×10⁻³` (`0.038656²=1.494×10⁻³` ✓) |
| 5 | `μ_r=1` docstring says "implicitly `mu_r=ni²`" for the matched family — inconsistent with the code's own `Zi=ni/√(rad)` | MATERIALS Phase-5 | Confirmed by direct read of `validity_precheck.py` lines 278–287: docstring says `mu_r=ni^2`; the physically correct implication of `Zi=ni/√(n²−sin²θ)` (`Z_TE∝μ_r/√(n²−sin²θ)`) is `μ_r=ni`, not `ni²`. Non-load-bearing (code never references `mu_r` numerically) |
| 6 | `part_d_photonics_construction()` has no `verdict` field, unlike `part_a()`/`part_b()`/`part_b_realizable()` | VISION Phase-5 | Confirmed by direct read of `validity_precheck.py`: the function returns `per_config`, `mean_scale_corrected_r2_re`, `min_scale_corrected_r2_re`, `note` — no `verdict` key anywhere |
| 7 | `exp-080` has no `NOTES.md` | VISION Phase-5 | Confirmed: `ls` on the experiment directory lists 17 files, none named `NOTES.md` — every T28 cycle 076–079 has one |
| 8 | Zero constraint-3/witness-relevance language anywhere in the complete record | VISION (Phase-2 and Phase-5) | Independently re-grepped the complete directory myself (§0.7): every hit is a self-disclaiming or scope-note usage, none asserts relevance |
| 9 | Zero `lab/` diff this cycle; house trust suite green at shift start | Phase 3/4 | Confirmed: `git diff --stat 41070f2 -- lab/` empty at current HEAD |

**Summary: every one of the nine independently-checked claims reproduces
exactly, including the three the task asked me to prioritize.** This is,
again, an unusually clean cycle by this program's own R4 standard — the
disagreements below are about framing, pre-registration discipline, and
what the record should conclude, not about any miscalculated figure.

### 0.5 One thing I checked that none of the six reviews checked directly

Since QUANTUM's finding (§0.3) turns on what PHOTONICS' original sketch
specified, I checked whether PHOTONICS' *own* exp-080 Phase-5 review
(which independently re-derives the `E_direct` cancellation) also revisited
its own exp-079 sketch's scoring methodology, since both reviews descend
from the same original document. It does not — PHOTONICS' exp-080 review
is entirely about whether `E_direct` cancels, and treats the *existing*
R²-against-candidate-curve test as the thing to make more correct
(§4(b)), not as the wrong test to be running at all. **This means
PHOTONICS' and QUANTUM's Phase-5 findings are complementary, not
overlapping**: PHOTONICS supplies the missing ingredient (`E_direct`,
proven to cancel in pair-deltas) that the *correct* test (QUANTUM's own
identified target — the free-period fit) will need; QUANTUM supplies the
observation that the test run so far was never the right one to begin
with. Neither review, alone, would have told Iteration 58 that it now has
every ingredient in hand to run the actually-correct test for the first
time. This is exactly the kind of cross-seat synthesis this program's own
prior Red Team audits (exp-079's own §1, its own words) have found "no
single blind Phase-5 review, working alone, could have delivered" — the
same shape recurring here, one cycle later.

### 0.6 Reproduction methodology note

Every reproduction above imports only `dg065`/`br`/`ywas` primitives
directly (never `validity_precheck.py`'s own functions, except the two
places explicitly noted as sanity cross-checks). Scratch scripts are
session-local (`/tmp/claude-0/-home-user-photon-lab/.../scratchpad/`); every
number they produce is reproduced in the tables above and is
re-derivable from already-committed repo files alone.

### 0.7 RULED-OUT registry (R1–R9) and constraint-3 check

Independently re-grepped the complete experiment directory (17 files) for
constraint-3/witness/perceptual language and for any of R1–R9's own named
dead ends (refractive cloaking, integer-shell rules, grid artifacts, a
named-constant search without a null-permutation control, an unverified
robustness argument standing in for a check, an un-independently-verified
unit comparison). **Zero hits of concern** — the only constraint-3
language found is THERMODYNAMICS' own explicit disclaimers ("nowhere near
mattering to constraint 3") and VISION's own meta-commentary confirming
the same. Nothing in this cycle touches R1–R9. Confirmed independently, a
third time this iteration (after VISION's Phase-2 and Phase-5 audits), on
the complete record including this document's own predecessors.

---

## 1. Adjudication of the six Phase-5 reviews

| Seat | Verdict as filed | My independent check | Disposition |
|---|---|---|---|
| PHOTONICS | PARTIAL | `E_direct` cancellation reproduced bit-exact from scratch (§0.1); wavelength-generality check (`d_F` at 450/750nm) reproduced exactly from `br.CPL={450:15,600:20,750:25}` | **ADOPT IN FULL.** This is the single most consequential finding in this Phase-5 layer alongside QUANTUM's (§0.5) — not a restatement of an open flag, a closed, reusable, provably-correct formula Iteration 58 can cite rather than re-derive. |
| MATERIALS | PARTIAL | Realizable-admittance rerun independently reproduced a third time (now the 4th total independent reproduction across this cycle); the `α*`-scale-corrected robustness check (`R²≈0.16–0.21` even with a sign-flipping free scalar) is new, correct, and strengthens (not merely reconfirms) the REFUTE verdict at C40/G40; docstring error confirmed by direct read | **ADOPT IN FULL.** The "realizable number is the only one that could ever describe a real material" framing is a correct, useful sharpening this seat's own charter is positioned to make — it should be stated plainly the next time this cycle's part (b) is cited, per MATERIALS' own recommendation. |
| ELECTROMAGNETISM | PARTIAL | Fourth independent reproduction of the geometry; far-field-limit derivation reproduced exactly at every `D_SP` scale (§0.2); ungated `[47.5°,54.5°]` range independently confirmed by direct code read and a fresh 200-point sweep | **ADOPT IN FULL.** The refinement to Attack 1's own causal language ("the aperture never actually presents 90°−θ_beam to the wall" reads as if moving the wall would fix it — it would not) is correct and should replace, not merely supplement, the record's existing phrasing wherever it is next cited. |
| THERMODYNAMICS | PARTIAL | `part_c` table independently reproduced a third time, a new way (via the scalar `br.reflection_coefficient`, not the vectorized function); the shared-cause diagnosis (ABSORB=70/80 concentration in both angular regimes) is a genuinely new cross-Phase-2 connection, independently confirmed by a fresh 200-point continuous sweep in both regimes | **ADOPT IN FULL.** The missing "geometric interception × material reflectivity" energy-budget factor is a real, previously-unstated gap in what this eight-cycle sub-thread has ever priced for constraint 3 — folded into §6 as a Tier-0 item. |
| QUANTUM | PARTIAL | The scoring-methodology finding independently verified against the primary source (§0.3), not merely against QUANTUM's own paraphrase; the self-inconsistency finding about QUANTUM's own Phase-2 "required change" (already moot when written) is correct on my own re-read of the Phase-2 critique's own timeline | **ADOPT IN FULL, and treat as the central finding this audit's ruling turns on** (§2, §3). QUANTUM's own review is the most load-bearing of the six — it identifies that the record's current "does not clear a bar" language describes a test that was never the right one, a finding with direct Checkpoint-4 consequences (§3). |
| VISION | PARTIAL | Text-search and git-log claims re-confirmed independently (§0.4 items 8, 9, and a fresh `git log` I ran myself, below); the missing-`verdict`-field and missing-`NOTES.md` findings both confirmed by direct file inspection | **ADOPT IN FULL, and act on both same-shift** (§4): I write `NOTES.md` below, and I address the missing-verdict-field finding directly in the Checkpoint-4 reasoning (§3) rather than leaving it as an open recommendation for Iteration 58 to discover independently a second time. |

**No blind Phase-5 review is overridden.** Every seat's own load-bearing
numeric claim independently reproduces, and every seat's own PARTIAL
verdict is correct and well-calibrated. This is the second consecutive
T28 cycle (after exp-079's own Iteration 56) in which all six blind
reviews check out cleanly and the real work of this audit is
synthesis and Checkpoint reasoning, not error-correction.

Fresh `git log` I ran myself for the whole cycle (VISION's own table,
independently re-derived, not copied):

```
6fb6b99 15:06:19  Phase 1 FROZEN PREDICTIONS
23203cc 15:08:40  Phase 1 run
b8fd6e5 15:13:43  Phase 2 MATERIALS
b261731 15:14:21  Phase 2 PHOTONICS
f041bbc 15:14:29  Phase 2 VISION
fcf7915 15:16:28  Phase 2 THERMODYNAMICS
e4e7005 15:19:23  Phase 2 QUANTUM (built PHOTONICS' §4 image term)
925f9fc 15:30:03  Phase 2 Red Team audit
01ddeca 15:33:38  Phase 3+4 fold-in + re-run
0544483 15:39:39  Phase 5 VISION
52f86d9 15:40:48  Phase 5 QUANTUM
f3990c1 15:41:53  Phase 5 THERMODYNAMICS
467d9a7 15:42:09  Phase 5 MATERIALS
16e1530 15:42:43  Phase 5 PHOTONICS
79adf0b 15:43:12  Phase 5 EM
```

Confirms the blind layer is genuinely blind (all six Phase-2 critiques
committed before Red Team's Phase-2 audit; all six Phase-5 reviews
committed within a 3.5-minute window of each other, none importing or
citing another's document) and that the fold-in (`01ddeca`) is the last
commit before Phase 5 begins, matching VISION's own diff-based finding
that the frozen part (a)/(b) code is untouched by it.

---

## 2. Central adjudication: does the E_direct proof + the methodology finding change what this cycle's part (d) result means?

**Yes — materially, though not by reversing any number.** Before this
Phase-5 layer, the record (`phase3_synthesis.md` §3(c), `phase4_results.md`)
stated: PHOTONICS' §4 image-term construction "does not clear a bar
comparable to, and by the shape-only floor measure is worse than, this
cycle's own already-INCONCLUSIVE part (b) result." Read plainly, that is
comparison language borrowed from a scored test — but I confirm, directly
from the code (§0.4 item 6) and from the primary source (§0.3), that:

1. **No verdict field or pre-registered band was ever attached to part
   (d).** `part_a()`/`part_b()`/`part_b_realizable()` all compute an
   explicit `verdict` against frozen `SUPPORT_R2`/`REFUTE_R2` thresholds;
   `part_d_photonics_construction()` does not. The "does not clear a bar"
   language is a **prose comparison to part (b)'s own thresholds**, not a
   result of applying them to part (d) as a formally scored test.
2. **The comparison target itself (`y_wall_aperture_sum_results.json`'s
   per-point curve) is not real T28 data** — it is a candidate model
   already shown, by exp-079's own reflectance-ablation control, to be
   structurally incapable of discriminating a real echo from none. Red
   Team's own Phase-2 audit already used this fact to keep Checkpoint
   criterion 2 NOT YET RIPE; QUANTUM's finding extends it one step
   further — the comparison *methodology* (R² shape-fit) was never the
   one PHOTONICS specified either.
3. **`E_direct`, the one missing ingredient this methodology gap turns
   on, is now derived and proven to cancel identically in every pair-delta
   Iteration 58 needs (§0.1).** The correct test — total field
   (`E_direct+r(90°−θ_beam)·W(θ_beam)`) scored via `_free_period_search`
   against real T28 periods, exactly as PHOTONICS' own exp-079 sketch
   specified — is now fully specified and ready to build, for the first
   time in this eight-cycle sub-thread's own T28 y-wall history.

**What does NOT change**: the raw, catastrophic amplitude-regime mismatch
(`|r(90°−θ_beam)|≈0.016–0.039` vs. `|r(theta_local(y_s))|≈10⁻⁴`,
100–400×) is real, independently reproduced five times over across this
cycle's own record (including by me, §0.4 item 4), and is a direct,
numerically solid consequence of part (a)'s FORECLOSE finding regardless
of which methodology eventually scores the total field. Nothing here
rescues the plane-wave/global-steering construction, and nothing here
suggests it is more likely to succeed than the record already implies. My
ruling is about what the record should **say it has shown**, not about
reversing what it has shown.

**Recommendation, applied in §4/§6**: `part_d_photonics_construction()`'s
"does not clear a bar" framing should be explicitly downgraded in the
Combined Verdict (§5) to "a real, independently-reproduced amplitude-regime
finding about the image-term-alone component, not yet a scored test of
PHOTONICS' actual construction" — and Iteration 58's own top queue item
changes from "gate and extend what QUANTUM already built" (Phase 3's own
phrasing) to "build the construction PHOTONICS actually specified,
scored the way PHOTONICS actually specified, now that every ingredient
exists" (§6).

---

## 3. Checkpoint ruling — reasoning through all five criteria explicitly

**Criterion 1** (a configuration passes all constraint metrics): **N/A.**
Zero constraint-3 engagement anywhere in this cycle, independently
confirmed a third time (§0.7).

**Criterion 2** (a proven mechanism-class boundary): **NOT YET RIPE — and
more precisely specified now than at Phase 3/4, not merely reaffirmed by
inertia.** The raw amplitude-regime evidence against the plane-wave/
global-steering construction remains strong and unchanged (§2). But §2's
finding sharpens exactly *why* this criterion cannot fire yet: the one
test that would actually settle it (`_free_period_search` on the total
field, against real T28 periods) has never been run, and — per QUANTUM's
finding, independently confirmed at the primary source (§0.3) — the test
that *has* been run was never the right one to begin with, not merely an
early, informative approximation of it. Every ingredient for the correct
test now exists (E_direct proven and derived, §0.1); what remains is
assembly and a fresh freeze, not new derivation. **Ruling: does not
fire, unchanged from Phase 3/4, but for a more precisely stated reason.**

**Criterion 3** (engine physics beyond validated bench classes): **N/A.**
Zero new FDTD anywhere in this cycle including all six Phase-5 reviews,
confirmed directly (§0.4 item 9; every review's own scratch script imports
only already-gated primitives, confirmed by reading each review's own
methodology section).

**Criterion 4** (program-integrity drift) — **the task specifically asks
whether QUANTUM's methodology finding, the missing NOTES.md, and the
un-scored part_d verdict, TOGETHER, change this ruling. Reasoned through
below, not asserted by pattern-matching to exp-079's own non-firing
precedent.**

**The case for taking this seriously, stated as strongly as it can be
stated.** Three things are true simultaneously in this cycle's own
already-committed record (`phase3_synthesis.md`, `phase4_results.md`,
both git-committed before this Phase-5 layer began):

1. `part_d_photonics_construction()` carries no `verdict` field and no
   pre-registered SUPPORT/INCONCLUSIVE/REFUTE band (VISION's finding,
   confirmed §0.4 item 6) — unlike every other scored quantity in this
   cycle's own file.
2. Despite that, the committed record describes its result in language
   borrowed directly from a scored test ("does not clear a bar," "worse
   floor than... 0.5214") — language a reader could easily mistake for a
   properly pre-registered REFUTE, the same rhetorical weight `part_b`'s
   genuine, pre-registered REFUTE carries.
3. QUANTUM's finding (§0.3, independently confirmed against the primary
   source) shows the comparison underlying that language was never even
   the *right* comparison to be running — a second-order problem beneath
   the first: not just "unscored," but "scored against the wrong thing,
   by the wrong method."

Stacked together, this is close to the shape R8/R9 exist to catch: a
load-bearing comparison, described with more confidence than its own
pre-registration status earns, written into a document that is one phase
away from becoming part of the program's permanent record (LOGBOOK.md).
It is also, separately, the THIRD instance within this same document of
something being informally treated as settled without the actual
committed machinery behind it: EM's gate range was hand-checked in a
Phase-5 review, not re-run as a committed gate; part (d)'s comparison was
described with scored-test language without a scored-test structure;
and — smallest of the three — this cycle's hypothesis/predictions
record exists in substance (`phase1_proposal.md`) but not under the
`NOTES.md` name the program's own convention requires. That is a real,
non-trivial concentration of "looks closed but is not quite" gaps, at
least as dense as exp-079's own Iteration 56 "closer call" ruling — the
established precedent this cycle should be measured against, not a lower
bar.

**Why it still does not fire, reasoned through rather than assumed.**
Every established non-firing precedent in this program (Iterations 51,
53, and exp-079's own Iteration 56, which explicitly named this exact
test) turns on ONE distinction: was the gap **caught and independently
verified within the same review layer, before it reached LOGBOOK**, or
did it survive unexamined past a freeze point into the permanent record?
Here: (a) no number is wrong anywhere — every claim across all eleven
independent reproductions this cycle has now accumulated (five in Phase
2/Red-Team-Phase-2, six more in Phase 5 including mine) matches exactly;
(b) the gap Attack — the overconfident "does not clear a bar" framing —
exists only in `phase3_synthesis.md`/`phase4_results.md`, both
Phase-3/4 documents this very Phase-5 layer exists to check, not in
LOGBOOK.md, which has not yet been written for this cycle; (c) this
document (§2, §5) explicitly corrects the framing, in writing, before
that LOGBOOK entry is drafted — matching, not merely resembling, the
"had this audit not independently re-checked... THAT would have been the
firing shape" reasoning exp-079's own Iteration 56 audit used for its own
comparably dense correction layer.

**The distinguishing condition, stated as plainly as the task asks for:**
criterion 4 does not fire **because** this document downgrades part (d)'s
framing explicitly (§2, §5) and states the corrected Iteration-58
instruction in terms that cannot be mistaken for "PHOTONICS' construction
has been tested and found wanting" (§6). If the eventual LOGBOOK entry
for this iteration — or any future document — repeats "part (d) does not
clear a bar" or "worse floor than 0.52" as though it were a scored,
pre-registered verdict comparable to part (b)'s own REFUTE, **without**
carrying forward the qualification that (i) no verdict field or
pre-registered band was ever attached to it, (ii) the comparison target
is itself only a candidate model already known to be structurally
uninformative, and (iii) the comparison methodology was never the one
PHOTONICS actually specified — **that repetition, not anything already
computed, would be the firing shape.** This is a closer call than
exp-079's own Iteration 56 ruling (three concentrated near-misses in one
document, not one), but it resolves the same way, for the same reason:
caught here, before LOGBOOK, not after.

**Ruling: criterion 4 does not fire, conditioned explicitly on this
document's own corrections (§2, §4, §5, §6) being what Iteration 58 and
the LOGBOOK entry actually inherit — not the pre-Phase-5 framing.**

**Criterion 5** (two consecutive non-advancing iterations): **Not at
risk.** This cycle substantively narrows the board a third consecutive
time: exp-078 foreclosed the single-edge model, exp-079 foreclosed the
full-aperture-sum model, and this cycle now supplies the actually-decisive
test's missing ingredient (`E_direct`, proven) and identifies the correct
methodology for running it — real, cumulative progress toward closing the
one remaining member of the coherent-echo mechanism class, even though
the underlying T28 mechanism question stays open.

---

## 4. Same-shift mandatory-fix docket

1. **[VISION, applied this shift]** `exp-080` was missing `NOTES.md`,
   unlike every T28 cycle 076–079. **Applied**: `NOTES.md` written this
   shift (see the file itself), reconstructed honestly from
   `phase1_proposal.md`'s own hypothesis/setup/idealizations/
   pre-registered predictions and this cycle's actual, complete Phase
   1–5 record, matching the format `experiments/079-.../NOTES.md`
   establishes.
2. **[QUANTUM + VISION, §2/§3 above, applied via this document's own
   corrected framing]** `part_d_photonics_construction()`'s "does not
   clear a bar" language is downgraded, in this document's own Combined
   Verdict (§5) and Iteration-58 instruction (§6), from scored-comparison
   language to an accurately-qualified description. **Applied in this
   document; NOT applied as a code or `phase3_synthesis.md`/
   `phase4_results.md` edit** — this audit's own mandate is one file
   (`phase5_redteam_audit.md`) plus `NOTES.md`; the actual code change
   (add `E_direct`, give the construction its real free-period-fit
   verdict, retire or clearly re-label the current R² field) is
   Iteration 58's own build task (§6 item 1), not a same-shift patch to
   an already-closed Phase 3/4 record.
3. **[EM, queued, not applied this shift]** Re-run
   `gate_lossless_unimodular_range`/`gate_single_layer_identity_range`/
   `gate_passivity_range` over `[47.5°,54.5°]` before
   `photonics_image_term_curve()`/`part_c_power_budget_at_true_angle()`
   are treated as fully gated. Cheap, zero new FDTD, but it touches
   `validity_precheck.py` (or a new committed file) — outside this
   document's own scope; folded into §6 as a Tier-0 precondition for
   Iteration 58's build.
4. **[MATERIALS, queued, not applied this shift]** Fix the
   `reflection_coefficient_vec_realizable()` docstring
   (`mu_r=ni^2`→`mu_r=ni`) the next time `validity_precheck.py` is
   touched — non-load-bearing, no computed number is wrong, but should
   not propagate further. Folded into §6 as a low-priority hygiene item
   for whoever next edits that file (Iteration 58's own build, most
   likely).
5. **[MATERIALS, applied in this document, §2/§5]** The realizable
   number, not the matched one, is stated explicitly here as the only one
   that could ever describe a real material — carried forward per
   MATERIALS' own recommendation, rather than left implicit.

None of the above touches `lab/`, any frozen Test-A/part(a)/(b) number, or
any RULED-OUT item. Items 3–4 are recorded as queued, not applied, because
applying them requires editing `validity_precheck.py` — a change this
audit's own mandate (one document, plus the ruled-for `NOTES.md`) does not
extend to; Iteration 58's own build (§6) is the right place for them,
bundled with the E_direct/free-period-fit construction that will touch
the same file anyway.

---

## 5. Combined Verdict for Iteration 57: **PARTIAL**

Consistent with every T28 cycle since exp-076, and with this cycle's own
Phase 3/4 self-scoring — but stated here with the Phase-5 layer's
corrections folded in explicitly, not left as six independent addenda.

**(a) FORECLOSE.** Confirmed a fifth independent way this cycle alone (EM's
original script, Red Team's Phase-2 audit, PHOTONICS' Phase-5 wavelength
check at 450/750nm confirming it is not a 600nm artifact, EM's Phase-5
far-field-limit derivation, and my own from-scratch re-derivation, §0.2).
Stands unqualified, robust across the program's own full 3-λ sweep.

**(b) Admittance-family-dependent.** INCONCLUSIVE under the matched
(unobtainium) family (mean `R²=0.7345`); **REFUTE** under the realizable
(`μ_r=1`) family (mean `R²=0.4305`, C40/G40 negative) — and MATERIALS'
Phase-5 robustness check (§4 of its review, independently confirmed
consistent with this document's own methodology standard) shows the
C40/G40 REFUTE **survives** a best-fit-scale correction (`R²≈0.16–0.21`
even with a free, sign-flipping scalar) — a genuine phase/shape failure,
not a calibration artifact, strengthening rather than merely reconfirming
the realizable-family verdict. **The realizable number is the one that
could ever describe a real buildable wall; the matched number describes
an admittance family already established (exp-075) as unobtainium** —
stated explicitly here per MATERIALS' own recommendation.

**(c) PHOTONICS' §4 image-term construction: a real, independently-
verified amplitude-regime finding about its image-only component — NOT
yet a scored test of PHOTONICS' actual construction.** The raw
100–400× amplitude mismatch between `|r(90°−θ_beam)|` and the true
`|r(theta_local(y_s))|` range is real, a direct numerical consequence of
part (a)'s FORECLOSE, and independently reproduced five times over across
this cycle's own record (QUANTUM's Phase-2 critique, Red Team's Phase-2
audit, QUANTUM's and THERMODYNAMICS' own Phase-5 reviews, and now me).
But — per QUANTUM's Phase-5 finding, independently confirmed against the
primary source (§0.3) — the comparison run so far (`R²` shape-fit against
exp-079's own candidate curve) is neither the comparison target nor the
scoring methodology PHOTONICS' original construction specified, and
carries no pre-registered verdict band. The correct test — total field
(`E_direct+r(90°−θ_beam)·W(θ_beam)`, with `E_direct` now derived and
proven to cancel identically in every needed pair-delta, §0.1) scored via
`_free_period_search` against real T28 periods — has never been run, and
is now, for the first time in this eight-cycle sub-thread, fully specified
and buildable with existing gated primitives alone.

**None of this closes the plane-wave/global-steering construction as a
T28 mechanism candidate.** Checkpoint criterion 2 remains NOT YET RIPE
(§3), more precisely specified than before, not merely re-affirmed.
Checkpoint criterion 4 does not fire, conditioned explicitly on this
document's own corrected framing being what Iteration 58 inherits (§3).

---

## 6. Reconciled ranking for Iteration 58's queue (all six seats + this audit)

### Tier 0 — zero FDTD, desk-only, run as one batch, in this order

1. **[HIGHEST — supersedes Phase 3's "gate and extend what QUANTUM
   already built"]** Build the construction PHOTONICS actually
   specified, scored the way PHOTONICS actually specified:
   `E(θ_beam) = E_direct(θ_beam) + r(90°−θ_beam;ABSORB)·W(θ_beam)`, with
   `E_direct` PHOTONICS' own derived, closed-form, already-proven-to-cancel
   formula (§0.1 — cite it, do not re-derive it), scored via
   `_free_period_search`/staged-widening against the REAL T28 reference
   periods (`experiments/076-.../results.json::headline`), under a
   FRESH SUPPORT/INCONCLUSIVE/REFUTE band (matching the `rel_dev≤0.30`
   SUPPORT / `>1.00` REFUTE convention every T28 cycle since Iteration 46
   has used) **committed to git BEFORE running it** — closing QUANTUM's
   own pre-registration gap (§0.3, §1) for real this time, not merely in
   spirit. Retitle or retire `part_d_photonics_construction()`'s own
   docstring/note to state plainly it was a partial, image-only,
   non-authoritative draft superseded by this build.
2. **[CHEAP PRECONDITION, EM]** Re-run `gate_lossless_unimodular_range`/
   `gate_single_layer_identity_range`/`gate_passivity_range` over
   `[47.5°,54.5°]` before trusting `reflection_coefficient_vec` at this
   range in item 1's own build — currently only hand-checked in a Phase-5
   review (this cycle's EM review and, independently, this document,
   §0.2), not committed as a gate.
3. **[CHEAP, PARALLEL, THERMODYNAMICS]** Price the geometric-interception
   × material-reflectivity energy budget — the missing third quantity
   for constraint 3's own energy bookkeeping (neither part (b)'s nor
   part (c)/(d)'s `|r|²` alone answers "what fraction of total scene
   power the echo path could carry," which needs an interception factor
   too). Even a crude upper bound (already implicit: ≤0.15% before any
   interception factor, at ABSORB=40) resolves whether this entire
   construction family could ever matter to constraint 3 in absolute
   terms, independent of whether item 1's period ever matches.
4. **[HYGIENE, near-zero cost, folded into item 1's own edit]** Fix
   `reflection_coefficient_vec_realizable()`'s docstring (`mu_r=ni^2` →
   `mu_r=ni`, MATERIALS); state explicitly, per MATERIALS' own
   recommendation, that the realizable number — not the matched one — is
   the only one that will ever describe a real material, whenever this
   cycle's part (b) is next cited; state explicitly, per EM's own
   refinement, that a valid global-angle y-wall construction (should one
   ever be attempted beyond item 1) needs an angle convention built from
   `theta_local(y_s)`'s own fixed-observer geometry, not a borrowed
   `θ_beam`-steering convention — resolving the near-field problem alone
   will not fix this.

### Tier 1 — cheap FDTD, next

5. The real 750/450nm wavelength-generality x-wall leg — now deferred
   **FIVE** consecutive T28 cycles (076–080); fold in PHOTONICS' own
   Phase-5 near-field-margin table (§2(ii) of its review) since it is
   already computed and directly bears on whether the aperture stays deep
   in the Fresnel zone at every wavelength this program's own metrics
   table commits to checking.
6. Broadband pulsed reflectance spectroscopy of the `ABSORB` boundary —
   deferred five consecutive cycles.
7. The 750nm x-wall two-wall spot-check — the single oldest-unexecuted
   item on the whole T28 board, still untouched.

### Tier 2 — the standing charter-relevant test, now the single most overdue item on the board

8. Whether the `PAD`-sensitivity axis survives with a real absorbing
   article loaded — deferred **FIVE** consecutive cycles (076–080), each
   cycle's own ranking naming it explicitly and declining to run it.
   Every congruent-series config to date, across nine T28 cycles, is an
   EMPTY scene; this remains the only queued item that would tell the
   program whether this entire nine-cycle sub-thread has any downstream
   relevance to constraint 3 at all — a fundamentally different kind of
   information than another period-matching exercise (item 1 included)
   can supply. **If Iteration 58 defers this a sixth time, the reason
   must be stated explicitly against this cycle's own finding (item 1 is
   now fully specified and cheap; this item remains the only one that
   tests real-world relevance at all), not by inertia** — this program's
   own now twice-repeated standard for this exact item.

### Tier 3 — governance

9. Checkpoint criterion 2 (mechanism-class boundary) ruled NOT YET RIPE
   this cycle, more precisely specified than before — item 1 above is the
   test that would actually settle it.
10. Checkpoint criterion 4 ruled non-firing this cycle **conditioned on
    this document's own corrected framing (§2, §3, §5)** being what the
    LOGBOOK entry and Iteration 58 actually inherit, not the pre-Phase-5
    "does not clear a bar" language — the LOGBOOK entry for this
    iteration should carry that qualification explicitly, not merely cite
    the raw numbers.

---

## 7. Bottom line

**Combined Verdict: PARTIAL.** (a) FORECLOSE, robust across the program's
own full 3-λ sweep and confirmed a fifth independent way. (b)
admittance-family-dependent — INCONCLUSIVE (matched) / REFUTE (realizable,
and the REFUTE survives a best-fit-scale robustness check). (c) PHOTONICS'
own construction carries a real, five-times-independently-reproduced
amplitude-regime pathology in its image-term-alone component, but the
record's language describing it as having "not cleared a bar" is
corrected here to what it actually is: an unscored, partial draft — not a
tested-and-failed construction. Checkpoint criteria 1/3 N/A, criterion 2
NOT YET RIPE (more precisely specified, not merely reaffirmed), criterion
4 does not fire (a closer call than exp-079's own Iteration 56 precedent,
resolved the same way: caught and corrected within this Phase-5 layer,
before LOGBOOK, not after), criterion 5 not at risk.

**My single most important instruction for Iteration 58**: every
ingredient for the actually-decisive test on the plane-wave/global-
steering construction — the free-period fit of its *total* field,
including `E_direct`, against *real* T28 reference periods — now exists,
independently derived and verified, and has never been assembled. Build
that, pre-registering its own SUPPORT/INCONCLUSIVE/REFUTE band in git
before running it, before doing anything else on this construction. Do
not carry forward "does not clear a bar" or "worse floor than 0.52" as if
they were that test's own result — they are not, and this document is the
record of why.

No RULED-OUT item (R1–R9) is re-proposed or re-litigated by this document
or by anything it recommends.
