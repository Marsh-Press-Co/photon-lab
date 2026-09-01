# Phase 5 Review — PHOTONICS (blind, fresh context)

*Panel Iteration 76, exp-099. Charter: surface interaction, absorption
spectra, angular dependence, scattering cross-sections — is the proposal's
optical response coherent as stated, across wavelength and angle? I have
not seen any other seat's Phase-5 output. All figures below were
independently recomputed from `results.json`/source this session; none are
taken on NOTES.md's word.*

## 0. Independent spot-verification

I recomputed the following load-bearing numbers directly from
`results.json` and cited source files (via Python, reading JSON, never
retyping a cited figure by hand):

1. **Item 1 filed-data deceleration ratio.** From the 4 filed cpl=40
   `delta_scene` values (`item_i.C.report`, exp-098), I rebuilt
   Δ₁=−9.591843×10⁻⁴, Δ₂=−9.272697×10⁻⁴, Δ₃=−1.150032×10⁻⁴ →
   r₃=|Δ₃|/|Δ₂|=**0.12402** (an 8.063× drop). Matches NOTES.md's "r₃=0.1240,
   ~8.06×" exactly.
2. **Item 1 new-point r-ratios (the "bounce").** From the 7-point combined
   sequence (last filed point + 3 new points: +4.704114×10⁻⁴,
   +1.322251×10⁻³, +2.456623×10⁻³, +2.778079×10⁻³), I rebuilt
   r₄=|Δ₄|/|Δ₃|=**1.3317**, r₅=|Δ₅|/|Δ₄|=**0.2834**. Matches `results.json`
   (`r_ratios=[1.3316739748300177, 0.28337723580831364]`) exactly, and
   confirms `amplitude_criteria_met=False` (r₄>0.5) is correctly derived —
   VANISHING-AMPLITUDE was correctly excluded on the amplitude test alone,
   independent of the period test Fix 5 added.
3. **Item 1 bracket-width margins.** `1.500°/0.3767516353°=3.9814×`,
   `1.500°/0.3201659178°=4.6851×` — matches "3.98×"/"4.69×" exactly.
4. **Item 2 Step 2 settling `rel_dev`.** `|5.243753×10⁻⁴−5.253136×10⁻⁴| /
   5.253136×10⁻⁴ = 0.17862%` — matches the filed 0.1786% exactly.
5. **Item 2 Step 3 Richardson `observed_ratio`.** Recomputed
   `shift_40_50 = crossing_cpl50 − theta_c40 =
   39.77686992722644 − 39.921519316666235 = −0.14464938943979178`, and
   `observed_ratio = shift_40_50 / shift_30_40(exp-098 filed) =
   −0.14464938943979178 / −0.15031902190763446 = 0.96228…` — matches
   `results.json`'s `0.962282667915931` exactly. (I initially mis-transcribed
   a comparator constant by hand while probing this figure and got a false
   "exact bit-identical duplication" alarm; re-deriving every operand
   directly from JSON, with zero hand-typed constants, resolved it — logged
   here as a reminder of exactly the discipline this sub-thread's own R4
   rule exists to enforce, including on a reviewer's own scratch work.)
6. **Item 3 `ptp` ratios and GP2′ tail bounds.** All 5 new-window
   `ptp`/`ratio_to_theta_c_5` pairs (θc=79°…87°) recomputed from
   `FastEval`-equivalent inputs reproduce `results.json` to the last printed
   digit; GP2′'s own tail `min_ratio=12.2221×`/`max_ratio=78.5343×`
   (θ=89.5°/74.5°) recomputed from `exp-098/results.json::item_v.gp2_curve`
   reproduce exactly, including the small non-monotonic uptick at θ=74.5°
   vs. 74.0° (78.534× vs. 78.283×) NOTES.md discloses.
7. **The Richardson figure NOTES.md attributes to exp-098 does NOT match
   exp-098's own current, corrected `results.json`.** See §2, below — this
   is my sharpest finding.
8. **Step 2/Step 3 angle "coincidence."** `theta_c40 − 0.067 =
   39.854519316666234`, but the hardcoded Step-2 settling angle is
   `39.854853` — a real, if small, `3.337×10⁻⁴°` gap. See §4.

## 1. Steel-man

Items 1 and 2 are a genuine improvement in this sub-thread's own
discipline, and I say this having independently re-derived the mechanics,
not merely read the prose. Item 1's bracket direction and width are
derived from Null C's *own* measured cpl20→cpl30 shift, not borrowed by
analogy — a real, verified R17 discharge (margins 3.98×/4.69× over the two
established shifts, independently confirmed above). Item 2 is the first
real FDTD ever spent on the R5 family, and it is gated by machinery this
cycle actually validates at R5's own resolution: a fault-injection
re-scoring at `family="R5"` (previously nonexistent at any resolution
above cpl=40, per Red Team's own Phase-2 audit, independently confirmed at
source in that document) and a far-from-null ground-truth sign check
(36.0°, matching the established R4 sign, confirmed above) — both run and
gating *before* the 16-call interior sweep, exactly the sequencing Red
Team's three-way-convergent Phase-2 attack (MATERIALS/QUANTUM/EM) demanded.
The pre-registered outcome scheme for item 1 correctly and honestly reports
INCONCLUSIVE-AT-THIS-WIDTH rather than forcing a clean verdict onto messy
data, and item 3's falsification criterion is genuinely applied both ways
(the honest "does not resolve cleanly" reading, not a coin-flip default).
This is careful, well-instrumented work.

## 2. Sharpest finding

**NOTES.md's own headline "Learned #4" finding rests on a Richardson-ratio
figure for exp-098 that was retracted by exp-098's own Phase-5 review one
cycle earlier — and citing the correct, currently-filed figure instead
reverses the qualitative story this cycle claims to be reproducing.**

NOTES.md's Result section states: *"Richardson (30/40/50, corrected
marginal-to-marginal, descriptive only): observed_ratio=0.9623 vs naive
2nd-order 0.64 — same-sign, larger-than-naive, the same qualitative pattern
as exp-098's own Null-B Richardson figure (20/30/40: observed 1.777 vs.
naive 0.5625)."* Learned #4 restates this as *"the Richardson-style
super-linear-growth pattern (observed ratio well above the naive 2nd-order
expectation, same sign) reproduced at a second, independent point-pair on
Null B."*

I pulled `experiments/098-.../results.json::richardson_diagnostic.B`
directly this session: `observed_ratio = 0.7765163757372424`, **not
1.777**. This is not a rounding artifact — `1.777` is exp-098's own
*original, miscomputed* figure (`shift_20_40/shift_20_30`, a
cumulative-over-marginal category mismatch), independently caught by
MATERIALS' Phase-2 critique and Red Team's Phase-2 audit of exp-098 itself,
and explicitly, permanently corrected in that document's own Result/Learned
sections, its own Red Team audit, and LOGBOOK.md Iteration 75: *"the
Richardson diagnostic compared a cumulative shift against a marginal one, a
category mismatch reversing the reported direction (corrected: 0.777
shrinking, not 1.777 growing)."* `exp-098/NOTES.md` itself states, in its
own Learned section: *"the corrected number is mildly reassuring, not
alarming"* and its own Phase-5 Red Team audit's table reads: *"0.777, not
1.777 — still shrinking, only ~38% off the naive."* `1.777` exists in
exp-098's record ONLY as the named, retracted, pre-correction value.

exp-099's own `run.py` correctly pulls `RICHARDSON_B_FILED =
j098["richardson_diagnostic"]["B"]` from the corrected, current file (I
independently confirmed the code path is right and `results.json`'s own
`step3.richardson_30_40_50.shift_20_30` field is bit-exact to the corrected
`-0.15031902190763446`) — the defect is confined to NOTES.md's *prose*,
which hand-cites `1.777`/`0.5625` from memory or an earlier draft rather
than reading the number back from the very file `run.py` itself loads two
lines above. This is precisely the failure shape R4 exists to name (a
figure cited as established/reproduced that does not reproduce from its own
cited source), and precisely the shape this document's own Attack 4/6
already caught twice in this same cycle (the Null C θ₀ digit and the
41.294235°/41.627568° angle-label errors) — this is now a **third** instance
of a hand-derived-not-recomputed figure inside one document that
explicitly, repeatedly, trades on "not hand-typed"/"re-read this session"
language to earn trust for its own arithmetic.

**This is not cosmetic — it inverts the qualitative claim.** `0.9623`
(this cycle, fresh) and `0.7765` (exp-098, corrected) are both `<1`: the
marginal shift is *shrinking* between successive resolution steps at both
point-pairs, a materially different and more reassuring reading than
"super-linear growth" (`>1`, shift getting *larger*, which `1.777` would
indicate and which is what a genuinely worsening/non-convergent resolution
family would look like). The correctly-characterized reproduced pattern is
"above the naive 2nd-order ratio but shrinking, twice" — real, and worth
scoping to Null A as NOTES.md's own Next §3 proposes — but "super-linear
growth... reproduced" as currently written overstates a convergence
concern that the actual, correctly-cited data does not support.

## 3. Secondary findings

**3a. The Null C "bounce" is direct empirical confirmation of the exact
concern this seat raised at Phase 2 — a connection NOTES.md's own Next
section does not draw.** My own Phase-2 critique (and Red Team's adopted
Attack 5/Fix 5) argued the bare amplitude-decay criterion could not
distinguish true asymptotic decay from ordinary curvature approaching a
trough of `delta_scene`'s own established ~2.84–2.95° oscillation, and
that 1.5° (about half that period) was not obviously wide enough to settle
it. The actual result — `delta_scene` decelerates, reaches a local minimum
somewhere in [θ₀+0.500°, θ₀+0.833°], then *reverses and climbs*
(r₄=1.332, unambiguously growing) — is not merely "consistent with"
oscillatory curvature; a reversal well inside a half-period is close to
the textbook signature the Phase-2 concern named. NOTES.md's Learned #2
correctly calls this "a genuine bounce, not a stall," but neither Learned
nor Next explicitly reconnects this new, concrete reversal to the
same-lobe-oscillation question Fix 5 was built to guard against — Next
item 1 proposes widening the bracket to ≥2.9474° (the right next
instrument) but frames the goal only as "true local minimum or... wider
oscillation," not as the direct test of the Phase-2 hypothesis it actually
is. (One hedge on my own observation: θ₀ is Null C's *cpl=20* crossing
location, not a confirmed zero of the *cpl=40* curve this cycle measures —
exp-098's own item (i) already found cpl=40 has no crossing within ±0.5°
of θ₀ at all, so I do not treat "θ₀+quarter-period" as a validated phase
anchor for the cpl=40 curve specifically; I raise the reversal's timing as
suggestive, not as a confirmed period-lock.)

**3b. A third, independently-found small numeric-provenance defect in the
same document (non-load-bearing).** Item 2's own design states Rank 2a's
settling angle "intentionally coincides with one Rank 2b interior angle
(39.854853°)" and explicitly discloses "the resulting 4 overlapping...
jobs... are not deduplicated." I recomputed the actual Step-3 interior
angle at that position directly: `theta_c40 − 0.067 =
39.854519316666234`, not `39.854853` — a real `3.337×10⁻⁴°` gap between
the two angles NOTES.md's own table labels as the same point ("39.854853°
| −0.067° (= Rank 2a angle)"). Physically negligible and, if anything,
this means the two FDTD points are NOT literal duplicates (so no call was
actually wasted the way the design's own text worried) — but it is a third
instance, inside one document, of a hand-set literal-decimal constant
(here, the hardcoded `settle_angle = 39.854853`) drifting from an
arithmetically-derived value from the same design (`theta_c40 − 0.067`),
the identical defect *shape* Red Team's own Attack 4 named for Null C's
angle labels (`θ₀±0.1667` vs `θ₀±1/6`). Worth a house-level note (Learned
#1 already proposes exactly this kind of standing convention) — not
verdict-affecting.

**3c. Item 3's unpredicted early reversal (77°→79°) deserved more than one
sentence.** The proposal's own weak lean ("continued decline from θc=77°")
missed at the very next point — a +37% jump, not a small ~0.3% wiggle like
the 74°/74.5° uptick already on file. NOTES.md discloses this honestly
("disclosed directly, not glossed over") but does not attempt any
qualitative account of *why* a windowed peak-to-peak statistic would show
a local re-ascent at θc=79°–81° before resuming its decline — worth a
one-line hypothesis (e.g., a second near-grazing feature of the underlying
closed-form curve, distinct from the θc≈69° peak) for whoever picks up
Next §4's direct-recompute item, rather than leaving the reversal as an
unexplained residual.

## 4. Verdict

**CONCUR-WITH-GAP(S).**

Items 1–3 are honestly executed, correctly gated per the mandatory Phase-2
fixes (independently confirmed at source, §0 above), and every headline
FDTD/numerical result I recomputed reproduces exactly except one. That one
exception is not trivial: NOTES.md's own "Learned #4" — a claimed,
twice-reproduced "super-linear-growth" pattern — is built on a citation of
a number exp-098's own record explicitly retracted one cycle earlier, and
the qualitatively correct comparison (0.9623 vs. the corrected 0.7765,
both `<1`, both "shrinking") supports a materially different, more
reassuring characterization than what is currently written. This does not
change either scored verdict (item 1: INCONCLUSIVE-AT-THIS-WIDTH; item 2:
SIGN-CHANGE-FOUND) — both rest on this cycle's own freshly-measured
`delta_scene` values, which are correct — but it does mean a genuinely new
"finding" this cycle presents to LOGBOOK is, as stated, false, and should
be corrected before Iteration 77 inherits "super-linear growth" as an open
concern that the actual data does not support.

## 5. Ranked top-3 candidate directions for Iteration 77 (independently reasoned)

1. **Fix the Richardson mis-citation (zero-FDTD, must happen before
   anything else builds on Learned #4), then run the widened Null C
   bracket Fix 5's own period bar names — but explicitly framed and scored
   as the same-lobe-oscillation discriminator my own Phase-2 critique
   raised, not merely "wider."** I agree with NOTES.md's own Next §1 that
   a ≥2.9474° half-width is the right next instrument, now sharpened by a
   concrete reversal point to center around — but I would pre-register the
   test explicitly against the oscillation hypothesis (does `delta_scene`
   cross zero, or complete a second trough/rise cycle, at roughly one more
   period past the located bounce?) rather than leave "true local minimum
   or wider oscillation" as an open-ended framing. This should also close
   §2's citation defect and, opportunistically, correct §3b's angle-label
   imprecision in the same pass.

2. **Generalize the (corrected) shrinking-Richardson pattern to Null A's
   own cpl=30 counterpart, zero new FDTD cost if Null A's cpl30 crossing
   is already on file** — I agree with NOTES.md's Next §3 that this is a
   real, worth-scoping question, but for a reason NOTES.md does not state:
   with the citation corrected, the actual open question is not "is
   super-linear growth a general feature" (it is not, on the corrected
   number) but "is a shrinking-but-slower-than-2nd-order convergence rate
   a genuine, resolution-family-wide property of this angular-null
   structure, or specific to Null B's own geometry" — directly bears on
   whether the whole `{R3,R4,R5}` family's crossing-location estimates can
   be trusted as converging to a real continuum answer at all, which is
   upstream of any constraint-metric use of `delta_scene(θ)`.

3. **THERMODYNAMICS' own T1/constraint-scoring trigger (NOTES.md's Next
   §2) is a legitimate, overdue governance question, but I would rank it
   third, not first or second, on PHOTONICS grounds — not silence it.**
   Scoring `delta_scene(θ)`'s sign structure as an angular-selectivity
   parameter against constraint-1/2/3/4 instruments before (a) Null C's own
   SIGN-vs-NO-SIGN status is resolved (still genuinely open after this
   cycle) and (b) the resolution-convergence-rate question in item 2 above
   is settled, risks promoting a signal whose own asymptotic behavior and
   grid-convergence rate are not yet trustworthy into a constraint-metric
   input. I do not think Iteration 77 should file T1: N/A silently an
   eighth time either — but I would sequence it after items 1–2 above, one
   cycle later than THERMODYNAMICS' own draft proposes, and say so
   explicitly rather than defer by default.

Standing items I did not re-rank but note remain genuinely open, unchanged
by this cycle: the x-wall wavelength-generality leg and PAD-with-article
survival check (both still deferred, per NOTES.md's own Next §5) — neither
is my seat's own charter priority to re-litigate this cycle, but both
should continue to require an explicit stated reason, not silence, if
deferred again.
