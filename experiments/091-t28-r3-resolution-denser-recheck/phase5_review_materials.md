# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (self-review, fresh context) · exp-091 · Panel Iteration 68

*Fresh sub-agent, no memory of proposing this cycle at Phase 1. Read in full:
PANEL.md; LOGBOOK.md's RULED OUT (R1–R14) and LIVE THREADS (T1–T28, complete
T28 sub-thread through Iteration 67/exp-090, both CHECKPOINT entries at
Iterations 61 and 65); the complete exp-091 record (`phase1_proposal.md`, all
five Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `run_output.txt`, `results.json`); exp-087/088/089/090's
`NOTES.md`/`phase5_redteam_audit.md`. This program's convention (stated in the
task brief and confirmed by exp-090's own Phase-1-lead self-review) is that
the lead seat DOES review its own cycle at Phase 5 — I treat `phase1_
proposal.md` as a different agent's work product to be checked, not
inherited, and I re-derived every load-bearing number below from `results.
json`/`run.py` myself before writing anything.*

## 0. Verdict

**CONCUR-WITH-GAP.**

The cycle's own scientific conclusions are sound and I independently
reproduce every headline number bit-exact (§1). The Phase-1/2/3 record
correctly discharges R3's own three-cycle-overdue debt on this channel,
correctly self-corrected the "40.2° is the hardest case" error, and
correctly ran all four falsifiable predictions as pre-registered. **But my
own charter's specific duty this cycle — verify the R3-rescaled article
geometry against `lab/materials.py::graded_black_shell`'s actual signature
— surfaces a real, previously undisclosed and unchecked construction
question that no Phase-1 draft, no Phase-2 critique (including my own
seat's), and no Red Team audit raised**: the PEC-core/shell **radii** are
correctly and uniquely determined by `R3_RATIO=1.5` (verified in code, §3),
but `graded_black_shell`'s `sigma_max` — the parameter that actually sets
the shell's physical optical depth — was left at its unscaled default at
both resolutions, and this program's own established `τ_center = 2·σ·
r_out(cells)` convention (T1, the SIGMA_ON/T10 erratum precedent) implies
that construction should inflate the R3 article's optical depth by exactly
`R3_RATIO=1.5×` relative to native, not hold it invariant. I traced this
through to the actual data (§4) and found the empirical impact is real but
modest (~3.5% on bulk `p_abs_w` at a crossing-clear angle) — this is NOT,
on the evidence, the primary driver of the cycle's dramatic `frac_contrast`
swings, which are independently and convincingly explained by proximity to
a genuine, resolution-sensitive `delta_scene` zero-crossing (R13's own
mechanism, §5) — but it is a real, disclosed-incompletely confound sitting
under the numerator-side `frac_p_abs`/(b2) comparison specifically, and it
is the first time in this program's history `graded_black_shell` has ever
been run under an R3 rescale, so no prior precedent covers it either way.
Separately, `NOTES.md` ships with **no Result/Learned section at all**
(§6) — a completeness gap this house's own convention (CLAUDE.md: every
experiment's NOTES.md carries hypothesis/setup/result/learned/next)
requires and which this exact sub-thread has fired on before (exp-080's
missing `NOTES.md`, closed same-shift by Red Team's final audit). Neither
gap changes my agreement with the cycle's actual measured outcomes.

## 1. Independent reproduction — spot-checks against raw JSON (R4/R9 discipline)

I did not trust any cited figure without recomputing it from `results.json`
myself.

| Quantity | My independent computation | Cited | Match |
|---|---|---|---|
| `frac_contrast_R3/frac_contrast_cpl20`, 40.2° | `7.877482×10⁻⁴/2.830881×10⁻⁴ = 2.7826963` (vs filed STEPS=2800); `/2.834300×10⁻⁴=2.779339` (vs Leg1 fresh) | `2.7793393959337838` | exact |
| `delta_scene(40.2°)` sign flip | Leg1 (cpl=20): `−1.5426768×10⁻⁴`; Leg2 (cpl=30): `+4.3698986×10⁻⁴` — opposite signs | `sign_match: false` | confirmed, independently re-derived |
| `ratio_k(40.2°, cpl=30) = frac_p_abs/frac_contrast` | `0.007936112988871345/0.0007877482082246626 = 10.074428…` | `10.074428486174352` | exact |
| `ratio_k(41.4°, cpl=30)` | `0.009588537373384361/0.0010409189939562388 = 9.211608…` | `9.211607655405578` | exact |
| `_label(10.074428)` vs `_label(10.0)` boundary | `ratio > RATIO_HIGH` is a **strict** inequality (`lab/…/run.py::_label`, confirmed against exp-087's own synthetic gate `(RATIO_HIGH, "C")`) | 10.074 clears X by **0.74%** | classification confirmed razor-thin, not a clean margin |
| `a2` bracket 40.2°→40.4° at cpl=30 | `v0=+4.3698986×10⁻⁴, v1=+9.8563820×10⁻⁴` — **same sign**, no crossing in `[40.2°,40.4°]` | `crossing_cpl30: null`, `verdict: REFUTE` | confirmed |
| `a2` bracket 41.4°→41.6° at cpl=30 | `v0=+5.6255250×10⁻⁴, v1=+1.7837587×10⁻⁴` — **same sign**, no crossing in `[41.4°,41.6°]` | `crossing_cpl30: null`, `verdict: REFUTE` | confirmed |
| `frac_contrast` ordering, cpl=30 | `37.2°(2.1627×10⁻³) > 40.2°(7.877×10⁻⁴)`, but `40.2°(7.877×10⁻⁴) < 41.4°(1.0409×10⁻³)` — **order reversed at 40.2°/41.4° vs cpl=20** | `ordering_check.cpl30_leg2: false` | confirmed |
| `p_c` (=`p_abs_w(C40)`) shift, 37.2° (crossing-clear angle) | native `2.812725669351364×10⁻¹²` → R3 `2.90992336586183×10⁻¹²`, ratio `1.03457×` | — (not filed as its own metric) | independently derived, §4 |
| `b2` verdict | all three ratios (2.776, 1.118, 1.327) inside `[0.3,3.0]`, all signs match | `"CONFIRM"` | exact |
| House gates | `vac_pass/xi_pass/nonneg_pass` all `true`, 40/40 calls, no duplicate jobs | matches | confirmed |

Every PRIMARY finding in the task brief's own summary reproduces bit-exact
from `results.json`. I add nothing that contradicts the record; §3–§6 below
add findings the record itself does not yet state.

## 2. Was MATERIALS right to push this across three cycles? Plainly: yes, and the result is sharper than "vindicated."

I pushed this exact check at exp-088, exp-089, and exp-090's own Phase-2/5
reviews specifically because 40.2°/41.4° sit closer (relative to their own
signal size) to a `delta_scene` zero-crossing than anything this program's
R3 machinery had certified before. The result is not a mild confirmation of
that suspicion — it is close to the worst outcome the design's own two-sided
framing allowed for:

- **(a) outright REFUTEs** — `delta_scene(40.2°)` does not merely shrink or
  grow under `cpl` 20→30, it **changes sign**, from `−1.54×10⁻⁴` to
  `+4.37×10⁻⁴`.
- **(a2) is worse than a simple "REFUTE," and worth stating precisely**:
  neither bracket even shows the *expected* sign change inside the window
  that contains the known `cpl=20` crossing. At 40.2°→40.4° (cpl=20 crosses
  at 40.265°, squarely inside this bracket), the cpl=30 series reads
  **positive at both ends** — the crossing that should sit between them at
  cpl=20 is simply not there at cpl=30, in either direction, anywhere in a
  0.2° window centered almost exactly on it. Same at 41.4°→41.6° (cpl=20
  crosses at 41.461°, inside the bracket; cpl=30 reads positive at both
  ends again). This is not "the node moved a little" — on the evidence
  actually collected, the local `delta_scene(θ)` structure near 40–42° has
  been qualitatively reshaped between cpl=20 and cpl=30, not merely shifted
  in phase. `d`'s own ordering-check corroborates this independently:
  `frac_contrast(40.2°) < frac_contrast(41.4°)` at cpl=30, the reverse of
  the cpl=20 ordering — a third, independent signature of real local
  reshaping, not sampling noise on one channel.
- **(b) 41.4° reclassifies outright** (ENERGY-DOMINANT → CONSISTENT,
  `ratio_k` 28.85→9.21), and **40.2° survives only by the barest technical
  margin**: `ratio_k=10.074428` clears `RATIO_HIGH=10.0` by 0.74%, under a
  **strict** `>` inequality I independently confirmed in `_label()`'s own
  code and its own synthetic boundary test (`(RATIO_HIGH, "C")` — exactly
  at 10.0 is CONSISTENT, not ENERGY-DOMINANT). A settling residual,
  rounding choice, or R3-scale-factor rounding a few tenths of a percent
  different would have flipped 40.2° too. Both of exp-090's caution-zone-
  defining angles are now shown to be, in different ways, unstable under
  exactly the resolution axis this program's own R3 meta-rule exists to
  check.

**I was right to keep raising this, and the panel was right to keep
deferring it behind cheaper items rather than rushing it** — the design
that finally ran it (this cycle) is materially better for having waited
for the mandatory-fix docket to add the bracket leg, the settling
spot-check at both angles, and the numerator-side co-equal test, none of
which existed in my own three prior asks.

## 3. Checking my own charter's specific duty: is the R3-rescaled article geometry actually correct and uniquely determined by `R3_RATIO=1.5`?

**The radii: yes, verified in code, no bug.** `build_article_r3` calls
`materials.pec_disk(sim, cx, cy, PEC_R_R3)` then `materials.
graded_black_shell(sim, cx, cy, PEC_R_R3, R3_R_OUT_CELLS)` with
`PEC_R_R3 = round(30×1.5) = 45` and `R3_R_OUT_CELLS = dg.R3_R_OUT =
round(78×1.5) = 117` (confirmed directly in `design_geometry.py`). Native
`build_article` (bit-identical across exp-082/083/etc., confirmed by
`grep`) calls `pec_disk(sim,cx,cy,30)` then `graded_black_shell(sim,cx,cy,
30,dg.R_OUT=78)` — **r_in equals the PEC radius in both constructions**
(30 native, 45 at R3): the shell begins exactly at the PEC surface with no
gap and no overlap, and this contiguity is preserved exactly by the
`×1.5` scaling (`45=30×1.5`, no rounding ambiguity since `30×1.5=45.0`
exactly). Shell thickness: native `78−30=48` cells `=1.44µm`; R3
`117−45=72` cells `=1.44µm` — **identical physical thickness**, and shell
thickness in wavelengths is trivially preserved too (`48/20=72/30=2.4λ`),
since physical size and λ are both held fixed by the design's own `L_
GEOMETRIC_M` identity (independently re-verified: `117×20nm = 2.34µm =
78×30nm`). The `r3_article_geometry_note`'s claim — "uniquely determined
by the single R3_RATIO=1.5 scaling rule this whole design already applies
to every other geometric constant" — is **true and independently
verified** for every radius in the construction. No bug here.

**But the disclosure is incomplete, and the gap it leaves out is not
cosmetic.** `graded_black_shell(sim, cx, cy, r_in, r_out, sigma_max=0.5,
eps_max=1.0)` (confirmed signature, `lab/materials.py:74`) is called at
**both** resolutions with `sigma_max` and `eps_max` unspecified — i.e. left
at their hardcoded defaults, identical numeric value (0.5) at native and
R3. `eps_max=1.0` is a dimensionless index ratio and needs no rescaling.
`sigma_max` is different in kind: it is the amplitude of a **per-cell**
conductivity array (`lab/fdtd2d.py`'s own docstring: "Units: grid units
(dx=1, c=1)"), and this program's own established optical-depth idiom —
`τ_center = 2·σ·r_out(cells)` (LOGBOOK, T1; the SIGMA_ON constant
`3.9/(2·78)` computed explicitly to hold τ fixed when `r_out(cells)`
changes) — states plainly that accumulated optical depth in this engine's
convention scales with **σ × geometric extent measured in cells**, not
with σ alone. I re-derived why from the update equation itself: `alpha =
sigma_e·S/(2·eps_r)` is the per-timestep loss, and a wave crosses `N`
cells in `N/S` timesteps (Courant condition), so accumulated loss
`≈ alpha·(N/S) = sigma_e·N/(2·eps_r)` — **the Courant factor `S` cancels
exactly**, leaving accumulated optical depth proportional to `sigma_e ×
thickness(cells)` alone, independent of `cpl`/`S`. `build_article_r3`
holds `sigma_max` at the SAME numeric value while the shell's own
thickness in cells grows by exactly `R3_RATIO=1.5` (48→72 cells, same
normalized smoothstep profile shape at both resolutions) — by this
program's own established convention, that is not "the same absorber at a
finer grid," it is **an absorber with ~1.5× the accumulated optical depth**
of the native construction. This is the identical failure *shape* as the
T10/SIGMA_ON erratum (LOGBOOK Iteration 4/5: "a systematically different,
more strongly absorbing article at every λ, not a resolution-matched
rerun... by construction, not by measurement") — here recurring, for the
first time, on `graded_black_shell` itself rather than on a uniform-shell
`SIGMA_ON` constant, because this is (per the module's own docstring) the
first-ever R3-resolution FDTD call that also builds this article. **The
`r3_article_geometry_note`'s framing — "uniquely determined by the single
R3_RATIO=1.5 rule... governs every other geometric constant" — is accurate
for the radii and silently does not address `sigma_max` at all**, which is
not a geometric constant in the sense the note means (a cell count) but a
material rate parameter whose own resolution-correct treatment, by this
program's established convention, is the **inverse** scaling
(`sigma_max_R3 = sigma_max/R3_RATIO ≈ 0.333`, mirroring `SIGMA_ON`'s own
`τ/(2·r_out)` derivation), not an unscaled default.

## 4. Does this actually matter here? Checked against the data, not argued.

I do not think this is the primary driver of §2's dramatic findings, and I
can show why rather than assert it. `p_abs_w(C40)` at 37.2° — the one
census angle with no crossing-proximity complication — moves from
`2.812725669×10⁻¹²` (native) to `2.90992336586183×10⁻¹²` (R3), a
**3.46% increase**. If the ~1.5× optical-depth inflation from §3 were
translating directly into a comparably large change in absorbed power, I
would expect something far larger than 3.46% on an object whose native
absorption is *not* already saturated. It very likely *is* already
saturated: T9's own established finding is that `graded_black_shell`
already returns `R≤0.2%` reflectance and `σ_abs/σ_ext≈0.51` at native
geometry — essentially all incident power reaching the shell is already
absorbed well before reaching `r_in`, so a further ~50% increase in
nominal optical depth on an already-near-total absorber has genuinely
diminishing returns on the *bulk* absorbed-power reading. That is a
plausible, physically coherent account of why `p_abs_w` itself barely
moves even though the underlying construction is not, by this program's
own convention, a strict finer-grid replica of the native object.

**Where it is NOT obviously safe to wave off is `frac_p_abs`
specifically** — the (b2) numerator, `|p_abs_w(G,θ)−p_abs_w(C,θ)|/
p_abs_w(C,θ)`, a small residual (0.14%–0.9% of the base value) built from
the difference of two near-equal numbers. A ~3–4% common-mode shift in the
bulk absorbed power need not cancel cleanly in that difference if `C40`'s
and `G40`'s own responses to the inflated optical depth differ even
slightly (plausible, since they differ in `PAD` and therefore in the
coherent field structure the absorber sits in) — and (b2) is exactly the
channel R14 already flags as fragile-by-construction for this reason. The
observed (b2) ratios (2.78×, 1.12×, 1.33×) all clear `[0.3,3.0]` and the
cycle self-scores CONFIRM — I am not disputing that score, since it is
computed and reported correctly against the pre-registered band — but I
do not think this design has actually shown `frac_p_abs`'s CONFIRM is
clean of the sigma_max confound, only that it is *consistent with* the
band regardless. **The cheap, decisive check** (matching this program's
own R8 discipline — compute it, don't argue it): re-run `build_article_r3`
with `sigma_max=0.5/R3_RATIO≈0.333` explicitly and compare `p_abs_w`/
`frac_p_abs` against this cycle's as-filed (`sigma_max=0.5`, unscaled)
run — 2–4 extra calls, zero change to any other machinery, and it would
settle, rather than leave open, whether the ~3.5% common-mode shift and
the (b2) ratios above are pure grid-refinement physics or partly an
artifact of this specific confound. I rank this Iteration-69's #2 item,
below.

## 5. Epistemic status of R13's floor gate and exp-090's caution zone, now that 41.4° has reclassified

**R13's floor gate itself is not shown broken — it is shown to be
answering a narrower question than the caution zone built on top of it
needs.** Both 40.2° and 41.4° cleared `floor_pass=True` at *both*
resolutions (never `NODE-UNRESOLVABLE`) — R13's actual guarantee (the
denominator is not so close to its own known zero that the ratio is
undefined by construction) held throughout. What this cycle demonstrates
is a **distinct** failure mode R13's text was never written to catch:
a point can clear the floor gate comfortably at one resolution and still
have its *classification* flip at another, because the underlying
oscillatory feature's own zero-crossing *location* — not just its
distance from a fixed cpl=20 measurement — moves under grid refinement.
R13 protects against a literal near-zero denominator; it says nothing
about whether the crossing itself is resolution-stable. This cycle is the
first direct demonstration that the two questions are genuinely separate,
and that clearing the first does not license trusting the second.

**exp-090's caution zone (`[1.4764, 2.1709]` in FLOOR-margin units) is
harder hit, and I think its status should be downgraded explicitly, not
just noted.** The zone's own lower edge is set by 40.2°'s margin
(1.4764×) — the *largest* margin among the points exp-090 classified
"misclassified" (ENERGY-DOMINANT); 41.4°'s margin (1.3095×) sits further
inside that same "confidently misclassified" territory, comfortably
*below* the zone, not at its ambiguous boundary. The point that looked,
under the zone's own cpl=20 metric, like the *more* confidently
ENERGY-DOMINANT of the two (41.4°, smaller margin, further from the
zone) is precisely the one that reclassifies at cpl=30, while the point
sitting *at* the zone's own ambiguous edge (40.2°, margin closest to the
lower bound) does not reclassify — though only by a margin
(§1, 0.74% over `RATIO_HIGH`) thinner than any margin the caution zone
itself was built to resolve. **This is the wrong direction for the zone's
own logic**: if FLOOR-margin distance genuinely tracked resolution
robustness, the point deeper into "confidently misclassified" territory
should have been the more stable one, not the one that flips. That it
did not means FLOOR-margin (a cpl=20-only quantity measuring distance from
the cpl=20 RMS floor) is not a reliable proxy for the thing the caution
zone is actually meant to warn about — whether a classification survives
resolution refinement. I recommend the caution zone be treated, from this
point forward, as **cpl=20-specific and provisional**, not yet licensed as
a general-purpose resolution-risk predictor, until either (a) all seven of
exp-090's own points receive the same R3 treatment this cycle gave three
of them, or (b) a genuinely resolution-aware regressor (e.g. crossing
distance measured consistently at both resolutions, or the a2-style
bracket-shift diagnostic this cycle introduces) replaces FLOOR-margin as
the zone's own basis. This does not retract exp-090's deliverable — it was
correctly, honestly scoped as an n=7, cpl=20-only desk fit with the R3 gap
explicitly named as its own open item — but that named gap has now been
shown to matter enormously, not modestly, and the zone's practical
reliability should be described that way going forward.

## 6. A genuine completeness gap: `NOTES.md` has no Result or Learned section

`NOTES.md` (last modified before the Phase-4 run — `results.json`/
`run_output.txt` postdate it) contains a Hypothesis, Setup, and the frozen
Predictions/Idealizations sections — and nothing else. There is no Result
section reporting what the 40 FDTD calls actually found (the sign flip,
the 41.4° reclassification, the a2 bracket non-crossings, the r3_article_
geometry_note), and no Learned section. This is not a disclaimer-erosion
instance in the Iteration-65-lineage sense (nothing here *omits* a caveat
that exists correctly elsewhere) — it is closer to exp-080's own
precedent (a substantively-complete cycle whose `NOTES.md` was simply
never written, closed same-shift by Red Team's final audit writing it).
Per that precedent I recommend the same disposition here: not a
Checkpoint-4 matter on its own, but a mandatory same-shift fix — the
Result section should state the four PRIMARY outcomes precisely
(REFUTE/REFUTE/mixed/CONFIRM for a/a2/b/b2, per §1's own verified numbers)
before this cycle is cited by any future T28 document, since `results.
json` alone is not the citable narrative this program's own convention
relies on.

## 7. Other checks, no issues found

- `G40_R3`'s cell footprint (`nx=660, ny=2496`) and aperture `A=1128`
  independently re-confirmed bit-identical to `C80_R3`'s, matching the
  file's own congruence assertion (`run.py` lines 124–127) — no drift.
- The bracket angles (40.4°, 41.6°) are genuine `DENSE_ANGLES` grid
  members, selected by value not by a hand-typed index (`dg.DENSE_ANGLES.
  index(40.4)` — R4-safe), confirmed against the generator's own
  `39.0+i×0.2` formula.
- `c1`/`c2` settling checks: all six `c1` cells and all four `c2` cells
  (both `C`/`C_empty`, both angles, both configs) read `rel_dev` in the
  `10⁻⁷`–`10⁻⁴` range, orders of magnitude inside the `≤1%` CONFIRM band —
  genuinely clean, not a marginal pass. `STEPS=2800`/`4200` and
  `R3_STEPS=4200`/`6300` are both independently shown settled on this
  channel; the observed instability is not a settling artifact at either
  resolution.
- The R14(a) smoothness gate passes at all eight steps across the five
  cpl=30 angles (37.2°/40.2°/40.4°/41.4°/41.6°) — `p_abs_w` is monotonically
  non-decreasing with angle at cpl=30 for both configs, unlike the R14
  founding dip's own 38.4° behavior. No new numerator-side anomaly of that
  specific shape appears in this cycle's own window.
- No `constraint-1–4`/T1 claim anywhere in the record; `REALIZABILITY_
  MEMO.md` correctly untouched. Checkpoint criterion 2 correctly N/A.

## 8. Ranked top-3 candidate directions for Iteration 69

1. **Locate where the cpl=30 `delta_scene` structure near 40–42° actually
   is.** §2's a2 finding (neither bracket shows the expected crossing at
   cpl=30) is more informative left un-followed-up than followed: it tells
   us the crossing isn't in the tested ±0.2° window, not where it went. A
   cheap, dense cpl=30 sweep (e.g. `DENSE_ANGLES[18..30]`, θ≈39.6–42.0°,
   0.2° step, mirroring exp-083's own 31-point census methodology but at
   `cpl=30`, ~26 calls) would directly re-locate the cpl=30 crossings (or
   show they have genuinely vanished/merged) rather than inferring their
   fate from two narrow, uninformative brackets — the precondition for
   rebuilding exp-090's caution zone on resolution-consistent footing
   (§5) at all.
2. **The `sigma_max` R3-scaling check I named in §3–§4** (2–4 calls: re-run
   `build_article_r3` with `sigma_max` explicitly rescaled by
   `1/R3_RATIO≈0.333`, compare `p_abs_w`/`frac_p_abs` against this cycle's
   as-filed run). Cheap, decisive, and closes the one construction question
   this cycle's own record — and every Phase-2/Red-Team pass on it — did
   not check, on the exact channel (b2) scores as CONFIRM.
3. **Extend R3 to the remaining four of exp-090's seven caution-zone
   points** (36.0°, 38.4°, 38.8°, 41.8° — exp-087/088's own angles), not
   only the three census points this cycle covered. §5's finding (FLOOR-
   margin does not predict resolution-stability in the direction the zone
   assumes) is drawn from only 2 of 7 zone-defining points; a full
   accounting needs all seven before the zone is rebuilt or formally
   retired.

**A new standing rule is warranted, and I recommend Red Team formally
adopt it** (I name it here as a recommendation, not an adoption — that is
Red Team's Phase-5 call): a candidate **R15** — *a calibration boundary
(threshold, caution zone, fitted classifier edge) built from points whose
classification depends on proximity to a demonstrated or plausible
resolution-sensitive interference node must have that resolution-
sensitivity independently R3-verified before the boundary is trusted for
any future classification; R13's own floor gate (guarding a literal
near-zero denominator) is necessary but not sufficient, since this cycle
shows a point can clear R13's floor cleanly at every tested resolution and
still have its classification flip under grid refinement.* Per this
program's own precedent (R5/R6/R9/R10/R11/R12/R13 all exempt their own
founding/discovery instance), this should not retroactively fault
exp-090 — the R3 gap was disclosed as exp-090's own named, open
Idealization at the time, exactly the discipline R15 would make
mandatory going forward.
