# PHASE 5 — REVIEW · ELECTROMAGNETISM (self-review of the seat's own lead cycle) · exp-092 · Panel Iteration 69

*Fresh context, no memory of Phase 1–4. Read in full: PANEL.md; LOGBOOK.md
in full (RULED OUT R1–R15, ESTABLISHED, LIVE THREADS T1–T28 through
Iteration 68/exp-091); `experiments/092-.../phase1_proposal.md`,
`phase2_critique_{materials,photonics,quantum,thermodynamics,vision}.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`results.json`, `run_output.txt`; the full `experiments/091-.../` record
(`phase1_proposal.md`, all five Phase-2 critiques, `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `results.json`,
`run_output.txt`); `lab/fdtd2d.py` (`Sim._damping`, `Sim.run`'s update law)
and `lab/materials.py::graded_black_shell` directly, not via citation. Same
SEAT led exp-092's own Phase 1 (a different, now-gone context wrote that
proposal) — this is self-review in PANEL.md's own established sense
(exp-091/MATERIALS' precedent), not memory of writing it. BLIND to every
other seat's current Phase-5 output for this cycle; did not read any
`phase5_review_*.md`/`phase5_redteam_audit.md` file under `experiments/092-`.*

## Verdict

**CONCUR-WITH-GAP.** Every load-bearing number I independently re-derived
from source — the `sigma_max_R3=1/3` algebra, the six Rank-3
sigma-correction ratios, both Rank-1 zero-crossing locations (including
the second, closely-spaced upper root), and the empty-leg
bit-exact-reproduction mechanism — reproduces exactly, and the house
passivity/energy gates (`xi_pass`, `nonneg_pass`, the per-cell
`sigma_abs≥0` check) are genuinely enforced by hard `assert`s, not merely
printed. The cycle's own PRIMARY findings (Rank 3 CONFIRM; Rank 1's clean
single lower crossing at `40.0718°`; the newly-discovered double crossing
at `41.7811°`/`41.8377°`) are real and correctly computed. **The gap is my
own seat's, not this cycle's arithmetic**: my own prior-cycle review
(`experiments/091-.../phase5_review_em.md` §4, ranked item 2 — a fresh,
different EM instance, but the same seat under this program's own
self-review convention) explicitly named "compute, not merely argue, the
predicted Yee-grid dispersion phase accumulation for this exact
aperture/propagation geometry" as the check needed to move the
"accumulated propagation phase" story from an argued claim to a verified
one, precisely because that same review had already found the sign flip
comes bundled with a **broad, angle-independent 2.8×–5.2× amplitude
inflation** inconsistent with a pure phase-shifted-fixed-amplitude
picture. `phase1_proposal.md` §1 restates the qualitative argument
essentially verbatim, one cycle later, without running that computation —
and this cycle's own new finding (a near-degenerate double root straddling
a near-total null in the upper window) is a second, independent signature
pointing the same direction my own prior review already flagged. This is
not a defect in what was computed; it is the same load-bearing physical
claim now deferred a second cycle running, self-diagnosed below rather
than caught by another seat.

## 1. Independent re-verification of load-bearing numbers

**`sigma_max_R3=1/3`, re-derived from source, not from any citation.**
`lab/materials.py::graded_black_shell` (line 97): `sim.sigma_e[shell] +=
sigma_max * sig / 0.5` — `sigma_max` is a genuine linear multiplier on the
shell's conductivity profile at every cell, confirmed directly in code
(not merely asserted by MATERIALS' steel-man, which I independently
verify is correct: the profile shape `sig` is unchanged by `sigma_max`,
so the optical depth scales linearly in it for the *graded* profile
exactly as it would for a flat one). Combined with `design_geometry.py`'s
own `R3_R_OUT=round(78×1.5)=117` (confirmed by direct read) and this
program's own established `τ_center=2·σ·r_out(cells)` convention (the
T10/SIGMA_ON mechanism): native `τ=2×0.5×78=78`; as-filed R3
`τ=2×0.5×117=117` (1.5× inflation, matching `R3_RATIO` exactly);
corrected `σ_R3=78/(2×117)=1/3` exactly. Algebraically forced, matches
`run.py:119` (`SIGMA_R3_CORRECTED = 78.0/(2*117)`) and the `assert
abs(...-1/3)<1e-12` immediately after it — this is now at least a sixth
independent derivation of this exact number across the two cycles'
combined record (EM Phase-1, MATERIALS/QUANTUM/Red-Team/Director at
Phase-2/3 of exp-092, myself here), and I find nothing to add or correct.

**Rank 3's six comparison cells, recomputed from `results.json`
directly.** `delta_scene` ratios `0.9226/1.0141/1.1720` at
`37.2°/40.2°/41.4°`, all sign-held, all inside `[0.3,3.0]`;
`frac_contrast` ratios `0.9382/1.0267/1.1827`, same. `ratio_sign_verdict`
(imported verbatim from `experiments/091-.../run.py:253-263`, I read the
function body directly): REFUTE fires on any sign mismatch or any ratio
outside `[0.1,10]`, CONFIRM only if every cell sits in `[0.3,3.0]` — all
twelve values here clear that bar with room (closest margin: `41.4°`
`frac_contrast` ratio `1.1827`, still `1.6×` inside the `3.0` ceiling).
**R3 CONFIRM is correctly computed, not a close or borderline call.**

**Both Rank-1 crossing locations, recomputed by hand from the printed
window values, not merely trusted.** Lower window
`[-2.4921,-2.2113,-1.6707,-0.9793,-0.2449,+0.4370,+0.9856]×10⁻³` at
`{39.2°...40.4°}`: exactly one sign change, between `40.0°` and `40.2°`;
linear interpolation `40.0 + 0.2×0.2449/(0.2449+0.4370) = 40.0718°` —
matches `results.json` to the printed digit. Upper window
`[+5.6255,+1.7838,-0.1865,+0.8042]×10⁻⁴` at `{41.4°,41.6°,41.8°,42.0°}`:
**two** sign changes — `41.6°→41.8°` (`41.6+0.2×1.7838/(1.7838+0.1865)
=41.7811°`) and `41.8°→42.0°` (`41.8+0.2×0.1865/(0.1865+0.8042)
=41.8376°`) — both reproduce exactly. `find_zero_crossings`
(`experiments/090-.../run.py:113-122`, read directly) is a bare
consecutive-sign-change linear interpolator with no smoothing or
peak-suppression step — it cannot merge or discard a genuine double root,
so the two-crossing report is a correct, mechanical consequence of the
data, not a search-machinery artifact.

**Empty-leg bit-exact-match claim — the EM justification, verified
directly from `run.py` source, not from `NOTES.md`'s restatement of it.**
`_run_sim_r3_sigma` (`run.py:135-148`):
```
if with_article:
    build_article_r3_sigma(sim, cfg["obj_x"], cfg["obj_y"], sigma_max)
```
`sigma_max` is a function parameter that is **read exactly once**, inside
this `if` block — when `with_article=False` (every empty-leg call, both
Rank 3 and Rank 1), the parameter is passed in but never dereferenced;
`build_article_r3_sigma` — the only function in this file that ever calls
`materials.pec_disk`/`materials.graded_black_shell` — is never invoked.
The `Sim` object that produces the empty-leg capture is therefore
constructed identically regardless of `sigma_max`'s value: same `nx`/`ny`
(from `dg.R3_CONFIGS[key]`, unaffected by any `sigma_max` argument), same
`courant_frac`, same `absorb`, same `add_line_source` call — every
input to the leapfrog Yee update is bit-identical between a
`sigma_max=0.5` and a `sigma_max=1/3` empty-leg call at the same
`(key,θ,steps)`. **This is exactly the "zero coupling into the empty
leg's own fields" claim, verified as a structural property of the call
graph, not an empirical coincidence** — and `results.json`'s own
`empty_leg_consistency_check` (all six cells, `bit_exact_match: true`,
float equality, not a tolerance) is the correct, and only necessary,
empirical confirmation of what the source already guarantees. I find no
gap between the code and the claim.

**House gates, traced to control flow, not print statements.**
`run.py:270` (`assert vac_pass`), `:310`/`:429` (`assert xi_pass`, run
independently after both Rank 3 and Rank 1), `:312`/`:431` (`assert
nonneg_pass`) — all four assertions sit strictly before the
`results.json` write; the file's own existence is evidence they held.
`xi_ext≤0.12` is checked at **every** `(config,θ,steps)` cell × 2 boxes
this cycle runs (20 cells × 2 = 40 checks for Rank 3+Rank 1 combined),
exhaustive, not sampled. `sigma_abs≥0` is checked per-cell inside
`cell_metrics` (`run.py:205`, `bool(ba["sigma_abs"] >= 0)`) and folded
into the aggregate `nonneg_pass` flag at both call sites — I confirm this
is enforced, not merely computed and ignored. **No passivity violation
anywhere in this cycle's 40 FDTD calls; reciprocity and causality are
properties of the underlying leapfrog Maxwell update this cycle does not
and need not re-test (nothing here changes the update law itself, only
`sigma_max`, `θ`, and the empty/article leg) — correctly, the design
takes no position requiring a fresh reciprocity check.**

## 2. Does the Rank-3 CONFIRM validate my own seat's Phase-1 §1 passivity/reciprocity/causality argument?

**Partially, and it is important to be precise about which part.** §1's
argument has two components: (a) a structural claim — passivity forbids
amplification, reciprocity/causality are properties of the continuous
Maxwell system the leapfrog update preserves at any stable Courant
fraction, "none of that machinery cares what `cpl` is"; (b) a mechanistic
claim — what refinement *can* move is accumulated propagation phase, and
a coherent null's location (not its existence) is exactly what that kind
of error moves.

**Component (a) is independently re-confirmed this cycle, cleanly** —
§1's own energy/passivity gates (`xi_ext`, `sigma_abs≥0`) hold exhaustively
across all 40 calls (§1, above), and nothing in varying `sigma_max` from
`0.5` to `1/3` (a genuinely different, still-passive material) produced
any gate failure or sign anomaly inconsistent with a passive, causal
medium. This is real evidence *for* (a), though it is worth stating
plainly what kind of evidence: Rank 3 tests whether a *different material
parameter* contaminates the channel, not whether *resolution itself*
does — the two are logically separate questions (RT-1 in
`phase2_redteam_audit.md` makes exactly this point about the reused
tolerance band, and I independently confirm it is correct and was
correctly folded into `NOTES.md`'s wording). Rank 3's CONFIRM rules out
one specific rival explanation for exp-091's sign flip (a wrongly-scaled
absorber, this sub-thread's own T10/SIGMA_ON-precedent failure mode) —
it does not, by itself, add new evidence for the "accumulated phase"
MECHANISM in (b); it removes a confound that could have explained the
observation *without* invoking (b) at all. `NOTES.md`'s own Learned item
1 ("exp-091's own headline sign flip... stand *more* firmly for having
survived this check") states this correctly and I concur with it exactly
as worded.

**Component (b) is NOT tested this cycle, and my own seat's Phase-1
document does not disclose that it isn't** — this is the gap the Verdict
names. §1 restates the qualitative dispersion-accumulation picture as the
reason a sign flip is "the expected signature," but the actual check that
would verify it (computing the predicted phase accumulation for this
aperture/propagation geometry at `cpl=20` vs `cpl=30`, checking whether
it is of the right order of magnitude and whether it can also explain the
amplitude-inflation finding, not just the sign flip) is the exact item my
own seat's own prior-cycle review named as the follow-up this argument
needed (`experiments/091-.../phase5_review_em.md` §4(i)–(ii), ranked
item 2 of that review's own top-3). It was not run this cycle, and §1 of
`phase1_proposal.md` does not flag it as outstanding — it simply
reasserts the qualitative version a second time. This is not a false
claim (the qualitative argument remains plausible and precedented, per
`VALIDATION.md`'s own fringe-limited-instrument lesson, cited correctly
in the prior review), but it is an under-disclosed gap: a Phase-1 seat
citing its own charter's central bookkeeping argument should either run
the computation or say explicitly that it has not, especially one cycle
after that exact gap was named in writing by the same seat.

## 3. Does the double-crossing finding complicate the "single smoothly-moving null" picture?

**Yes, and this cycle's own Learned section states the *empirical* fact
correctly (items 2–3) without connecting it back to what it implies for
§1's own physical framing — the connection is mine to draw here.** A
"coherent interference null relocates under a phase-velocity error"
picture, taken at face value, predicts a single zero-crossing translating
smoothly in `θ` as `cpl` changes — one root moving, not splitting. What
this cycle actually found in the upper window is a curve that goes
positive → positive → **slightly negative** → positive across four
consecutive `0.2°`-spaced points, i.e. a curve that dips *just* below
zero and climbs back out again within `0.057°` — a near-tangency to zero,
not a clean transit through it. Two facts corroborate this is a real
feature, not sampling noise, independent of the crossing search itself:
the dip coincides with `41.8°`'s own `NODE-UNRESOLVABLE` classification
(`floor_pass=False`, the smallest-magnitude `delta_scene` this cycle
measured by nearly an order of magnitude — `results.json::rank1.per_theta.
"41.8"`), and `42.0°` (also `floor_pass=False`) sits on the same
near-null shelf. This is a materially richer local structure than a
single moving root, and it is the *same* underlying suspicion my own
seat's own prior review already raised on independent grounds (§4(ii) of
`experiments/091-.../phase5_review_em.md`: a pure phase shift of a
fixed-amplitude sinusoid should not inflate the sinusoid's amplitude away
from its zeros, which is what the broad `2.8×`–`5.2×` `frac_contrast`
growth at non-crossing angles already showed one cycle ago). A
near-degenerate double root — two closely-spaced zeros bracketing a deep,
narrow near-null — is exactly the kind of local feature a genuine
near-field point-probe amplitude effect (T10's own established class:
finer grids can reveal *more* structure a coarser grid partially smooths,
not merely translate one feature) would produce, and is a qualitatively
different claim from "the null moved because of accumulated dispersion
phase." **Both explanations remain physically legal — nothing about a
near-degenerate double root violates passivity, reciprocity, or
causality; T10's own mechanism is itself an ordinary, physically legal
near-field effect, not a new escape from any conservation law — but they
are different physical pictures with different implications for how this
channel should be treated going forward** (a single moving null is a
one-parameter correction; a near-degenerate double root implies the
region between the original crossings is developing genuine internal
structure that a coarser future resolution check could again fail to
resolve). `NOTES.md`'s own Learned items correctly report the empirical
finding but do not flag this tension against §1's own framing — worth
stating explicitly for Iteration 70, not left as an implicit reading.

## 4. exp-092's own §2a "widening lobe" argument — checked against what actually happened

`phase1_proposal.md` §2a argued the net should be asymmetric and
outward-biased because (i) the two crossings' naive linear extrapolations
move in opposite directions, and (ii) EM's own independently-reconfirmed
`2.8×`–`5.2×` `frac_contrast` inflation at three non-crossing angles is
"the same direction as" — cited as corroborating — a widening lobe.
PHOTONICS' Phase-2 critique correctly identified (ii) as a non sequitur
(a zero-crossing of `f(θ)` is invariant under uniform amplitude
rescaling; vertical growth carries no information about horizontal
relocation), Red Team upheld it exactly (`phase2_redteam_audit.md` §1.1),
and I independently re-verify the logical point is correct: amplitude
inflation at points that are not themselves near either crossing cannot,
on its own, support a claim about which direction a *different* point (a
zero) moves. **What actually happened**: the directional prediction
itself turned out correct (lower crossing moved to smaller `θ`, upper
region's structure moved to larger `θ`, both matching the naive secant's
own sign), but the true structure — a single clean crossing on one side, a
near-degenerate double root on the other — was never a shape either the
secant extrapolation or the "widening lobe" narrative could represent to
begin with (a lobe "widening" implies one interior region growing between
two still-single crossings, not one of those crossings splitting into
two). PHOTONICS' attack is vindicated twice over: the amplitude
corroboration was invalid reasoning as stated, *and* the "widening lobe"
picture itself, even setting the invalid corroboration aside, was too
simple a model for what the region actually contains. The naive 2-point
secant's own *numeric* accuracy for the lower crossing (`+0.032°` off) is
a genuine, if `n=1`, positive result — but it is a coincidence of the
lower window's own simpler (single-root) structure, not evidence the
underlying "widening lobe" mental model was correct; §2a's own reasoning
should not be read as vindicated by this cycle's own numbers, only its
directional guess.

## 5. Standing-rule / Checkpoint check (independently worked through, not deferred to Red Team's own audit)

**R3/R15**: this cycle is a faithful, correctly-scoped continuation of
both — Rank 1 extends the search net, Rank 3 extends the resolution-check
discipline to a second confound on the PRIMARY channel, exactly what
R15's own founding text calls for. **R13/R14**: applied unchanged, correctly
(§1c is explicitly diagnostic-only, not re-scored against either
threshold). One minor, non-blocking observation for a future cycle: `39.4°`'s
`frac_p_abs=0.000302` (`ratio_k=0.076`, this cycle's smallest value) is
built from `|p_g-p_c|` where both `p_c,p_g≈3×10⁻¹²`W — a genuine R14-shape
small-subtractive-cancellation numerator, reported here only as
diagnostic context (R1c, non-gating, per the pre-registered design), so
R14's floor-gate machinery correctly does not apply to it this cycle — but
a future cycle that promotes any Rank-1 diagnostic angle to a scored
PRIMARY claim should re-apply R14's own numerator-distrust discipline to
it first. **No Checkpoint criterion fires on anything I independently
checked.** The §1/§2 gap named above is a disclosure gap in a Phase-1
document's own argument, caught here at Phase 5, in the identical seat
that wrote it, with nothing in the frozen record misstating a check as
completed when it was not (§1's language is qualitative throughout,
consistent with how it read in exp-091 before my own seat's prior review
flagged it) — this matches the program's own standard non-firing shape
(a real gap, disclosed and correctable, not a false verification claim
defended into the permanent record). I judge this closer to R8's own
"named check not run" shape than to a fresh rule; I do not propose a new
numbered rule for it, since the existing R8 language (an affordable named
check, once identified, should be run or its absence disclosed) already
covers a Phase-1 seat re-citing its own charter argument without running
a check its own prior cycle named — worth Red Team weighing explicitly
whether the two-cycle recurrence (named at exp-091 Phase-5, not run at
exp-092 Phase-1, silently) crosses into that rule's own territory, rather
than my asserting it does on my own.

## 6. Ranked top-3 for Iteration 70

1. **A denser, off-grid sweep of the upper window (`~41.6°`–`42.2°`,
   finer than the native `0.2°` `DENSE_ANGLES` step, `NOTES.md`'s own
   Next item 2) — the single most decisive, cheapest test of §3 above.**
   Resolving whether `41.78°`/`41.84°` is a genuine two-node feature or an
   under-resolved single deep null directly discriminates between "ordinary
   translating-null dispersion" and "near-field point-probe structural
   effect" (T10's class) — the exact ambiguity this review's §2–§3 leave
   open, and the one with the most consequence for how much future trust
   this channel's own crossing locations deserve.
2. **Compute, not merely re-argue, the predicted Yee-grid dispersion phase
   accumulation for this exact aperture/propagation geometry at `cpl=20`
   vs `cpl=30` — my own seat's own twice-named, still-unexecuted
   recommendation, now sharpened by two additional facts this cycle
   supplies for free**: does a pure accumulated-phase model predict a
   magnitude and *sign* of shift consistent with the newly precise
   `-0.194°`/`+0.320°`–`+0.377°` measured shifts (§ above), and — the
   harder, more discriminating test — can a phase-only model produce a
   near-degenerate double root at all, or does producing one intrinsically
   require an amplitude-side (T10-class) contribution? Zero new FDTD; a
   desk calculation using this bench's own established Yee-dispersion
   relation and the aperture's own known geometry (`A=1128` cells at R3).
3. **Re-fit R15's own caution zone using the two (or three, counting the
   upper pair separately) newly-located `cpl=30` crossings as inputs**
   (`NOTES.md`'s own Next item 1) — the natural completion of R15's own
   mandate now that Rank 3 has removed the sigma_max confound as a rival
   explanation; should explicitly report a version that treats the upper
   region as "one node, location uncertain between two close roots" and a
   version that treats it as "two genuine nodes," disclosing which, if
   either, changes the zone's own qualitative shape — not deferred to
   whichever future cycle happens to need it.
