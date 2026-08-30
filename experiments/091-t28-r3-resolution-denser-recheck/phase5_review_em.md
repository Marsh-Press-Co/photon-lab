# PHASE 5 — REVIEW · ELECTROMAGNETISM (blind) · exp-091 · Panel Iteration 68

*Fresh context, no memory of Phase 1/2/3/4. Read in full: PANEL.md;
LOGBOOK.md's RULED OUT (R1–R14), ESTABLISHED, and LIVE THREADS sections,
including T10, T13, T16, and T28 in full through Iteration 67/exp-090
(both T28 CHECKPOINT entries); `experiments/091-.../phase1_proposal.md`,
`phase2_critique_{em,photonics,quantum,thermodynamics,vision}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`; exp-087/088/089/090's NOTES.md +
`results.json` for context; `lab/sections.py`, `lab/ambient.py`,
`lab/fdtd2d.py`, and `lab/validation/VALIDATION.md` for the underlying
instrument signatures. I am blind to every other seat's current Phase-5
output for this cycle. Not identified as this cycle's own Phase-2 EM
sub-agent — a different, now-finished, fresh-context instance — but I
independently re-derive that critique's substance from primitives below
rather than taking it on faith.*

## Verdict

**CONCUR-WITH-GAP.** Every load-bearing number I re-derived from
`results.json`'s raw primitives matches the printed/committed values
exactly. All three house gates (`vac_pass`, `xi_pass`, `nonneg_pass`) are
genuinely backed by hard `assert` statements in `run.py`, not merely
printed strings — I traced the control flow and confirm the script could
not have produced a `results.json` at all had any of them failed. The
PRIMARY refutation (`delta_scene(40.2°)` sign flip) and the (a2) bracket
REFUTEs are real, correctly computed, and — per §2 below — the direct,
sharpened realization of my own seat's Phase-2 circularity concern, more
severe than that critique's own proposed fix anticipated. The **gap**: (i)
the (a2) instrument, as built, can say "the crossing is not in this
bracket" but cannot say *how far* it moved or whether it still exists in
recognizable form — a real, disclosed, non-fatal limitation of this
cycle's own design that the next cycle must not mistake for "case closed";
(ii) a genuinely new finding this review surfaces (§4) — a **broad,
angle-independent 2.8×–5.2× amplitude inflation of `frac_contrast` at
`cpl=30`, not confined to the crossing-adjacent angles** — argues the
mechanism is closer to T10's established near-field point-probe
enlargement class than to a pure local-phase-dispersion account of the
sign flip alone, a distinction the record as filed does not draw.

## 1. Independent recomputation

I recomputed every headline figure directly from `results.json`'s `raw`
block rather than trusting `run_output.txt`'s prose.

**Sign flip, `delta_scene(40.2°)`.** `raw.native_leg1_cpl20_steps4200.
"40.2".delta_scene = -1.5426768×10⁻⁴`; `raw.r3_leg2_cpl30_steps4200.
"40.2".delta_scene = +4.3698986×10⁻⁴`. Sign flip confirmed, bit-exact to
the task brief's cited `-1.543e-4`/`+4.370e-4`. `delta_scene(41.4°)` does
**not** flip sign (`+1.334×10⁻⁴ → +5.626×10⁻⁴`) but grows **4.2×** — I
flag this now because it becomes load-bearing in §4.

**(a2) bracket REFUTEs.** `per_pair."40.2-40.4"`: `v0=+4.3699×10⁻⁴,
v1=+9.8564×10⁻⁴` — both positive, no sign change, `crossing_cpl30=null`.
`per_pair."41.4-41.6"`: `v0=+5.6255×10⁻⁴, v1=+1.7838×10⁻⁴` — both
positive, no sign change. I confirm `find_zero_crossings` (exp-090's own,
reused verbatim per `run.py`'s docstring) is the correct, already-gated
tool for this — it is a simple consecutive-sign-change interpolator, and
correctly returns nothing when consecutive samples share a sign. Both
REFUTEs are genuine: the known `cpl=20` crossings (40.2654°, 41.4609°,
independently re-derived by `find_zero_crossings` on `exp-083`'s own raw
31-point census, not hand-typed) sit **inside** each `cpl=20` bracket but
**outside** both `cpl=30` brackets.

**`ratio_k` reclassification.** `b.per_theta`: 37.2° `1.8463→CONSISTENT`
(cpl20 leg1 `3.4641→CONSISTENT`, match); 40.2° `10.0744→ENERGY-DOMINANT`
(cpl20 leg1 `25.0503→ENERGY-DOMINANT`, match — but `10.0744` clears
`RATIO_HIGH=10.0` by only **0.744%**, i.e. `0.0744` absolute); 41.4°
`9.2116→CONSISTENT` (cpl20 leg1 `28.8456→ENERGY-DOMINANT`, **mismatch**).
All bit-exact to the task brief.

**`frac_p_abs` (b2) CONFIRM.** Ratios `2.7756/1.1178/1.3270` at
`37.2°/40.2°/41.4°`, all inside `[0.3,3.0]`, all sign-matched. Confirmed.

## 2. My own seat's Phase-2 concern: vindicated, and exceeded

The Phase-2 ELECTROMAGNETISM critique (`phase2_critique_em.md`, a
different fresh-context instance) argued that testing `ratio_k`'s
classification survival against the OLD, `cpl=20`-derived `FLOOR` "tests
whether the crossing has moved using a threshold whose own validity
presumes it hasn't" — circular, and unable to distinguish "stable
classification" from "the crossing moved." **This is vindicated in full**:
the (a2) test that critique's own proposed fix produced shows the crossing
did move, and moved in a way the classification-comparison alone (§4b)
could not have told apart from ordinary noise — exactly the diagnosed
failure mode.

**But the magnitude exceeds what that critique itself anticipated, and I
find this the sharper of the two facts.** That critique's own remedy
proposed "2–4 cheap `cpl=30` points bracketing 40.2°/41.4° at ±0.1–0.2°...
sufficient to directly locate the cpl=30 delta_scene zero-crossings."
Phase 3 adopted a **±0.2° grid-aligned version of exactly this fix**
(40.4°/41.6°, the existing `DENSE_ANGLES` neighbors) — and it was **not
wide enough**. The crossing is not merely shifted within that window; it
has left it entirely, in *both* directions independently (40.2°→40.4° and
41.4°→41.6°). A critique that correctly diagnosed the disease still
under-scoped the cure's own width. **Implication**: the true `cpl=30`
location of these two crossings remains genuinely unknown — not "shifted
by some sub-0.2° amount we can bound," but unlocated. Any future citation
that reads this cycle's REFUTE as "the crossing moved a little" rather
than "the crossing's new location is presently unknown, other than being
outside `[40.2°,40.4°]`/`[41.4°,41.6°]`" would overclaim. This is
correctly, I confirm, how `results.json::a2.per_pair` states it
(`"crossing not reproduced in this bracket"`, `shift_deg=null`, not a
numeric shift) — the record does not overclaim; a future prose citation
could.

## 3. Energy/passivity check

**Absorbed power (`p_c`/`p_g`), all four legs, all cells: positive
throughout, no exceptions.** I read every value in `raw.*`: native `p_c`
range `2.813×10⁻¹²`–`3.165×10⁻¹²` W, native `p_g` range
`2.809×10⁻¹²`–`3.188×10⁻¹²` W; R3-leg2 `p_c` `2.910×10⁻¹²`–`3.283×10⁻¹²`,
`p_g` `2.898×10⁻¹²`–`3.314×10⁻¹²`; R3-leg3 (settling spot-check) and
R3-leg4 (bracket) both in the same `2.9×10⁻¹²`–`3.35×10⁻¹²` band. All
positive, all physically sane in magnitude (consistent with T9's
established `ratio_abs_ext≈0.51` anchor and every prior T28 `p_abs_w`
citation since exp-087) — no passivity violation anywhere in this cycle's
40 calls.

**Gates are not merely printed — I traced them to hard control flow.**
`run.py:317` (`assert vac_pass, "P1 FAILED..."`), `:430`
(`assert xi_pass, "P4 FAILED..."`), `:432` (`assert nonneg_pass...`): each
sits between the gate's computation and any further code, including the
`results.json` write at the end of `main()`. Had any gate failed, the
script would have raised and **no `results.json` would exist to read** —
so the file's own existence is itself evidence the printed `True` values
are not decorative. I also find the non-negativity check is **doubly
enforced**, at two granularities: the aggregate `nonneg_pass` flag (set
`False` if any `w["sigma_abs"] < 0`, `run.py:394-395`) AND a second, harder,
per-cell `assert p["p_abs_w"] >= 0` (`run.py:410`) fired immediately after
each individual thermo-sidecar call, before the aggregate flag is even
consulted — a redundant, independent enforcement I had not seen requested
anywhere in this cycle's own record, and a genuinely good practice.
`xi_ext` (extinction-routes agreement) is computed per-box as
`abs(sigma_ext_cross - sigma_ext)/abs(sigma_ext)` and compared against
`XI_TOL=0.12` at **every one of the 20 (config,θ,steps) cells × 2 boxes =
40 box-level checks** this cycle runs, not sampled — the `xi_pass=True`
claim is exhaustive, not a spot-check. I conclude: the house energy/
passivity gates are genuinely, not nominally, clean this cycle.

## 4. Is the sign flip ordinary FDTD numerical dispersion, or something structural?

**Two separable questions, and the record (correctly) only answers the
first.** (i) Is a `delta_scene` sign flip, this close to a genuine zero, a
plausible consequence of ordinary Yee-grid numerical dispersion under a
1.5× grid refinement? (ii) Does the *size* of the shift argue for
something else?

**(i) Plausible, on this program's own established precedent, without a
new calculation.** `lab/validation/VALIDATION.md`'s own "Measurement
lessons" record, verbatim: *"Point-wise B(y) flatness is fringe-limited on
a soft-source bench... the finite tapered aperture throws Fresnel edge
fringes... Gate window MEANS, not points."* `delta_scene` is built
(`lab/ambient.py::contrast_from_runs`→`weber`) from exactly this
point/window-probed flux profile, not a closed-surface flux integral —
the same distinction LOGBOOK's **T10** thread already drew empirically:
box-ledger channels (`sections.widths`, this cycle's own `p_abs_w`) stayed
resolution-clean while a near-field envelope-ratio channel's relative
spread grew 46%→128% under a 1.5× `cpl` refinement (T10, exp-027, later
found ~96% attributable to an unrescaled `SIGMA_ON` confound — see below).
T28's own established `~2.84°–2.95°` period for this exact channel is,
relative to a typical fringe spacing, extremely fine — implying the
interference is generated by path-length differences accumulated across a
large fraction of the aperture's own half-width (`A=752` cells native,
`1128` cells at R3, i.e. tens of wavelengths). A per-cell numerical-
dispersion phase-velocity error that is individually tiny (leading-order
Yee dispersion error scales `~(Δx/λ)²`; `cpl` 20→30 changes this by a
factor `(20/30)²≈0.44`, i.e. roughly halves it) still integrates over that
many wavelengths of propagation into an accumulated phase difference that
can easily exceed `2π` between the two resolutions — more than enough to
relocate a fine interference null by several multiples of `0.2°`. **I have
not computed this integral for this exact geometry — I state it as the
qualitative, precedented mechanism, not a verified number — and I name the
computed version of this argument as my own Rank-1 recommendation below,
precisely so this stays an argued-then-verified claim rather than an
argued-and-accepted one (the R8 discipline this program's own T28 record
enforces on exactly this shape of claim).**

**(ii) The size of the shift is not, by itself, damning — but a genuinely
new finding this review adds sharpens what "size" means here.** I checked
whether `frac_contrast`'s **magnitude** inflation is localized to the two
crossing-adjacent angles (which local-dispersion-near-a-null would
predict) or general across the sampled window (which a broader amplitude
artifact would predict). Computing `frac_contrast_cpl30/frac_contrast_
cpl20` at all three census angles, independent of the (a) verdict's own
sign-flip trigger:

| θ | `frac_contrast` cpl20 (Leg1) | cpl30 (Leg2) | ratio |
|---|---|---|---|
| 37.2° | 4.153×10⁻⁴ | 21.63×10⁻⁴ | **5.21×** |
| 40.2° | 2.834×10⁻⁴ | 7.877×10⁻⁴ | 2.78× (sign flip) |
| 41.4° | 2.505×10⁻⁴ | 10.41×10⁻⁴ | **4.16×** |

**All three angles inflate by a large, roughly similar factor (2.8×–5.2×)
— not just the two crossing-proximate ones.** 37.2° and 41.4° sit
0.073°/0.061° and 4.2°/1.9° away from their nearest known crossings
respectively (37.1272°, 41.4609°) and are far from any *other* crossing —
if this were purely a local phase-shift-near-a-null effect, an angle this
far from its own crossing should show a much smaller *magnitude* change
(a phase-shifted sinusoid has unchanged amplitude away from its zeros). It
does not. I traced this to the numerator, not a re-normalization: `|C_c|`
(the denominator) is stable across resolutions at every angle (e.g. 37.2°:
`0.5641→0.5766`, 2.2% change) while `delta_scene` itself (the numerator)
grows by the full 2.8×–5.2× factor. **This is closer to T10's established
mechanism — a near-field point-probe differential channel's amplitude
genuinely enlarging under grid refinement — than to "the same fringe,
phase-shifted."** I checked for T10's own historical confound (an
un-rescaled module constant held at its native cell count inside the
rescaled grid) and did not find one here (§5) — Idealization 4's "same
~2.34µm physical radius" claim and every clearance/reference-window
constant verify correctly R3-scaled. So the T10 erratum's specific
mechanism (a forgotten rescale) is ruled out as the explanation this time;
the residual, genuine near-field point-probe sensitivity T10 also found
(a small but real effect, after its own confound was removed) is left
standing as the most likely account, now observed at a much larger
magnitude on a channel with a much finer intrinsic fringe period than
T10's own beam-behind measurement. **I do not read this as evidence
against the geometry (see §5) — I read it as evidence that this specific
instrument (point-probed Weber contrast on a tapered-aperture near-field
scene) is simply more resolution-sensitive, in amplitude as well as in
null-location, than this program's box-ledger channels, exactly as T10 and
VALIDATION.md's own "fringe-limited" lesson already state — but this
review is the first record to show the effect is broad, not
crossing-localized, which the filed record does not currently say.**

## 5. Is the `r3_article_geometry_note` disclosure adequate?

**Yes, and I independently corroborate it two ways beyond what the note
itself claims.**

**(a) Digit-level geometric congruence, checked against the native
article, not merely against `run.py`'s own assertions.** Native
`build_article` (bit-identical across exp-082/083/etc.): PEC core radius
30 cells, `graded_black_shell(30, R_OUT=78)`. This cycle's
`build_article_r3`: PEC core radius `45=round(30×1.5)`, shell
`(45, R3_R_OUT=117=round(78×1.5))`. Both scale by the identical
`R3_RATIO=1.5` the rest of the design already uses — I did not find this
ratio applied inconsistently anywhere I checked (clearances 12/24→18/36,
`REF_HALF_H` 80→120, `A` 752→1128, PEC core 30→45, shell 78→117). In
physical units: native PEC radius `30×30nm=900nm=1.5λ`; R3 PEC radius
`45×20nm=900nm=1.5λ` — identical, confirmed independently by hand, not
merely by `run.py`'s own `L_GEOMETRIC_M`/`L_GEOMETRIC_M_R3` assertion
(which only checks `R_OUT`, not the PEC core or shell `r_in`, so my check
covers ground that assertion does not).

**(b) The absorbed-power (`p_abs_w`) magnitude scales as physically
expected between resolutions — this is the EM-charter-relevant check the
task specifically asks for, and it is genuinely informative because it is
independent of the contrast-channel instability (§4) by construction (a
box-ledger flux integral, not a point probe).** I computed
`p_abs_w`(R3, `cpl=30`) / `p_abs_w`(native, `cpl=20`) at every angle, both
configs:

| θ | C40: native→R3 ratio | G40: native→R3 ratio |
|---|---|---|
| 37.2° | 1.0346 | 1.0319 |
| 40.2° | 1.0359 | 1.0350 |
| 41.4° | 1.0372 | 1.0396 |

**A small (+3.2%–+4.0%), angle-independent, config-independent increase —
not a large jump, not a sign change, not an order-of-magnitude shift, and
not scattered/inconsistent across the three widely-separated angles.**
This is exactly the signature of ordinary PEC/shell-boundary staircase
discretization error shrinking as resolution increases (a well-behaved,
small, monotone convergence trend), not of a geometry mismatch — a real
scaling error in the new `G40_R3` article (e.g. a mis-scaled core-vs-shell
ratio, or a physically-larger/smaller absorber) would be expected to
produce either a much larger discrepancy or an angle-dependent one, since
the article's interaction with the field is angle-sensitive at oblique
incidence (T9's own `ratio_abs_ext` anchor already establishes this
absorber's cross-sections are angle-varying). Finding instead a uniform
~3–4% shift, common to both configs and all three angles, is itself
evidence *for* correct geometric congruence, not merely consistent with
the note's claim. **Combined with (a), I judge the disclosure adequate as
written, and now backed by an independent, quantitative energy-bookkeeping
check the note itself does not perform.**

## 6. Ranked top-3 for Iteration 69

1. **Locate the actual `cpl=30` crossings near 40.2°/41.4° with a wider
   net, not a repeat of this cycle's own ±0.2° bracket.** §2 shows the true
   `cpl=30` crossing locations are presently unknown beyond "not in
   `[40.2°,40.4°]`/`[41.4°,41.6°]`." A denser `cpl=30` sub-sweep spanning
   roughly `[39.6°,42.2°]` at the existing `0.2°` grid (reusing this
   cycle's own `_run_sim_r3`/`build_article_r3` verbatim, ~10–14 calls) is
   the direct, decisive answer to the question this cycle's own instrument
   could only bound, not resolve — and would additionally show whether the
   `cpl=30` structure near these angles is a simple shifted zero (T21/T28
   dispersion-consistent) or something qualitatively different (a
   broadened/split feature), which bears directly on §4's still-open
   dispersion-vs-something-else question.
2. **Compute, not merely argue, the predicted Yee-grid dispersion phase
   accumulation for this exact aperture/propagation geometry at `cpl=20`
   vs `cpl=30`**, and check whether it is of the right order of magnitude
   to explain both the sign-flip-near-a-null (§4(i)) and, separately, the
   broad 2.8×–5.2× amplitude inflation this review found not confined to
   the crossing-adjacent angles (§4(ii)) — the latter is the part my own
   qualitative dispersion argument does *not* obviously cover (a pure
   phase shift of a fixed-amplitude sinusoid should not inflate the
   sinusoid's own amplitude at points far from its zeros), so a clean
   dispersion-only account would need to explain both facts, not just the
   sign flip. Zero new FDTD; this is the specific computed-not-argued
   check R8's own standing rule calls for, applied to this review's own
   claims rather than left as an accepted informal argument.
3. **A third resolution point (e.g. `cpl=25`) at 37.2°/40.2°/41.4°**,
   testing whether `frac_contrast`'s own magnitude is converging
   (a monotonically shrinking `cpl`-to-`cpl` increment, Richardson-style)
   or non-convergent at this specific channel and angle set. This is the
   test that would most cleanly separate "an unusually large but ordinary
   convergent numerical effect" from "this specific point-probe channel
   cannot be trusted for `ratio_k` classification near these angles at any
   affordable resolution" — the second reading, if confirmed, would be a
   materially stronger and more actionable finding for R13's own future
   refinement than anything a two-point (`cpl=20`/`cpl=30`) comparison can
   establish on its own.

Also still open, not superseded by this cycle: the R3-native `FLOOR`
rebuild (Idealization 6/§4d, ~124 calls, explicitly out of scope this
cycle) is now more urgent, not less — 40.2° survives `cpl=30`
ENERGY-DOMINANT by only `0.744%` over `RATIO_HIGH=10.0`, against a `FLOOR`
this cycle's own §4 amplitude-inflation finding suggests could itself
shift substantially under a genuine R3-native rebuild.
