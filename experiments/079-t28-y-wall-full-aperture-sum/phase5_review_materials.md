# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS · Panel Iteration 56 · exp-079

*Fresh sub-agent, blind to the other six seats' Phase-5 reviews this cycle
(MATERIALS led this cycle's Phase-1 proposal, but I carry no memory of that
— reviewing the final record as an independent seat, exactly as every other
Phase-5 reviewer does). Read PANEL.md in full; AGENTS.md; LOGBOOK.md in
full (RULED OUT R1–R9; ESTABLISHED; LIVE THREADS in full, close attention
to T28's complete Iteration 46–55 history); `experiments/078-.../
phase5_redteam_audit.md` in full; this cycle's complete, final record in
order — `phase1_proposal.md` (as corrected in place, carrying the PHASE-3
UPDATE and revised §4/§7), all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`y_wall_aperture_sum.py`, `y_wall_aperture_sum_results.json`, `_output.txt`;
`experiments/075-.../boundary_reflectance.py`,
`experiments/065-.../design_geometry.py`. I ran fresh, independent
computations against the raw code/primitives rather than trusting any
write-up's numbers — see §2.*

---

## 1. Verdict: **PARTIAL**

Same shape as my own seat's exp-078 verdict, for the same underlying
reason, sharpened rather than reversed by this cycle's own central finding.
This cycle's headline result — the recovered `theta_beam`-dependence is
structurally locked to the shared aperture's T21-family content and
**cannot discriminate a real y-wall echo, at any period, from no echo at
all** (Red Team's Attack 1, adopted in full at Phase 3) — is a finding
about *geometry*, not about *admittance*. It does not touch the
realizability bound this seat owns, in either direction: `r(theta_local
(y_s))` is still built from `boundary_reflectance.py`'s matched-`eps=mu`
(TE) transfer function, still requires a broadband, angle-tracking magnetic
loss response (`mu_r != 1`) with no realizable analog for an ordinary
dielectric/conductive coating at optical frequencies, and this cycle
neither confirms nor refutes anything about whether a *buildable*
(`mu_r=1`) instantiation would behave differently — that remains genuinely
untested for the y-wall mechanism class as a whole.

What this cycle *does* newly establish, and the reason the verdict stays
PARTIAL rather than moving to RULED OUT: **the specific citation this
cycle's own Idealization 1 leans on to argue realizability doesn't matter
here — MATERIALS' own exp-078 Pearson-r>0.9997 "near period-invariant"
finding — does not survive independent testing at the angular range this
cycle's own construction actually uses.** It was computed at exp-078's
narrow, single-point, 48°–54° envelope; at exp-079's real full-aperture
4.77°–15.50° envelope, the same admittance-choice correlation collapses
badly, including one config where it goes *negative* (§2a below). This is
a genuine, previously-untested gap now closed — but closed in a way that,
on independent re-verification (§2b), still lands on the same practical
conclusion the citation was used to support, for a different and more
robust reason than the citation itself gave. Not PROMISING: nothing here
newly implicates a buildable structure, and the corrected Combined Verdict
(1/3 non-informative nominal SUPPORT, 0/3 REFUTE) is unchanged by anything
in this seat's review.

---

## 2. Independent checks

### 2a — The inherited Pearson-r>0.9997 "near-invariant" citation does NOT hold at this cycle's own operative angular range

`phase1_proposal.md` §6 Idealization 1 states, honestly disclosed as
untested this cycle: *"MATERIALS' own re-ranking (exp-078 Phase-5, F2)
found the realizable (`mu_r=1`) substitution is near period-invariant for
the y-wall specifically (Pearson `r>0.9997`)... but was not independently
re-tested here."* I read `phase5_review_materials.md` (exp-078, my own
seat's prior-cycle review) directly: that `r>0.9997` figure was computed
"at the y-wall's own corrected angle envelope (`theta_y = 90-theta = 48
deg-54 deg`)" — the single near-edge point's own `90-theta_beam` convention,
a completely different angular regime from this cycle's own per-point
`theta_local(y_s)` envelope, which the geometry table (`phase1_proposal.md`
§2) states spans `[4.77 deg, 15.50 deg]` globally.

I independently rebuilt both admittance formulas from `boundary_
reflectance.py`'s own `reflection_coefficient` (matched, `Z=n/sqrt(n^2-
sin^2(theta))`) and the realizable `mu_r=1` TE form (`Z'=1/sqrt(n^2-
sin^2(theta))`, the same substitution MATERIALS used at exp-077/078) and
swept both across the ACTUAL `[4.77 deg, 15.50 deg]` envelope this cycle
gates at (200-point sweep, all four `ABSORB` depths, `n_profile_exact` from
`br.damp_e_profile`/`br.nu_profile` unchanged):

| ABSORB | Pearson r, `arg(r)` (matched vs realizable), 48°–54° (exp-078, cited) | Pearson r, `arg(r)`, 4.77°–15.50° (this review, independently computed) | `arg(r)` max deviation |
|---|---|---|---|
| 40 | 0.999982 | 0.873191 | 89.08° |
| 60 | 0.999890 | 0.878742 | 18.35° |
| 70 | 0.999865 | **−0.630059** | 5.76° |
| 80 | 0.999754 | 0.743649 | 1.19° |

**The near-invariance claim does not generalize.** At the actual envelope
this cycle's own coherent aperture sum uses, three of four `ABSORB` depths
drop to `r approx 0.74-0.88` and one (`ABSORB=70`) goes *negative* — the
matched and realizable admittance formulas' angular dependence are not even
correlated in the same direction there. `|r|` magnitude also diverges by
an order of magnitude at some depths (e.g. `ABSORB=60`: matched `|r| approx
2-5e-6` vs realizable `|r| approx 7.8-8.2e-5`). This is exactly the failure
shape this program's own R8/R9 family exists to catch: an inherited,
correctly-scoped finding (true at the geometry it was measured at) cited
as a general property ("near period-invariant for the y-wall specifically")
at a materially different geometry where it was never re-checked. The
citation in `phase1_proposal.md` §6 is honest about not re-testing this —
it is not a false claim in the R4 sense — but the specific number it leans
on for reassurance is, at this cycle's own operative range, simply wrong.

### 2b — But: independently recomputing exp-079's own Test A under the realizable admittance shows the practical conclusion holds anyway, for a different, stronger reason

Given 2a's result, the honest next question is whether this matters — does
substituting the realizable admittance into THIS cycle's own full
coherent-sum construction change any scored Test-A number? I did not
assume either way; I recomputed it, reusing every primitive `y_wall_
aperture_sum.py` itself imports (`build_aperture_grid`, `theta_local_deg`,
`aperture_amplitude`, `source_driven_phase`, `dist_image_cells`,
`br.n_profile_exact`, `free_period_with_widening`), with only `reflection_
coefficient_vec`'s admittance line swapped (`Zi = 1/sqrt(n^2-sin^2(theta))`
in place of `Zi = n/sqrt(n^2-sin^2(theta))`):

| comparison | P*_model, matched (committed) | P*_model, realizable (this review) | rel_dev vs T28 real target | verdict |
|---|---|---|---|---|
| `PAIR_PAD` | `1.9925°` | `2.0075°` | `0.5647` | INCONCLUSIVE (unchanged) |
| `PAIR_ABSORB40` | `2.0226°` | `2.0075°` | `0.5193` | INCONCLUSIVE (unchanged) |
| `C80-C40` | `2.0301°` | `2.0150°` | `0.2910` | SUPPORT (unchanged, still non-informative per §5.3's ablation control) |

**Every period shifts by at most `0.015°`** (vs the matched-admittance
model), an order of magnitude smaller than the `1.6%-3.5%` gap that already
separates the recovered period from T21's own exact value, and every
Test-A verdict is bit-for-bit unchanged. This independently confirms, from
a genuinely new computation at the correct envelope (not by re-reasoning
about the old one), that the realizability idealization is not load-bearing
for this cycle's own scored numbers — but for the reason Red Team's own
Attack 1 gives (the model's entire `theta_beam`-dependence is carried by
the shared, admittance-independent driven-phase ramp; `r(theta_local(y_s))`
only reshapes a slowly-varying envelope), not for the reason Idealization 1
cites (a narrow-angle correlation that, per §2a, does not actually hold at
this envelope). This is the same qualitative conclusion the reflectance-
ablation control (`r(theta_local(y_s)) -> 1.0`, §5.3 of `phase1_proposal.md`)
already reached by a more extreme substitution — my own check here shows
the result is not an artifact of that one extreme ablation; a physically
motivated, merely-different admittance model lands in the same place.

### 2c — The admittance formula itself is unaffected by anything this cycle changed

Confirmed by direct source read (`y_wall_aperture_sum.py` line 234,
`reflection_coefficient_vec`; `boundary_reflectance.py` line 195,
`reflection_coefficient`): both the scalar, already-gated function and this
cycle's own new vectorized re-implementation use the identical matched
(`eps=mu`) TE admittance `Z=n/sqrt(n^2-sin^2(theta))` — validated bit-exact
against each other (`max|r_vec-r_scalar|=7.988e-16`, independently
re-confirmed) but never validated against anything physically realizable.
Nothing in this cycle's own nine-item mandatory-fix docket touches this
formula. My exp-078 review's finding stands unchanged: this admittance
requires an equal, angle-tracking magnetic-loss response with no known
realizable analog at optical frequencies — `unobtainium-with-parameters`,
exactly as for the x-wall (exp-075/077).

### 2d — Verification from primitives (independent of any prior cycle's numbers)

Recomputed directly, not copied: `theta_local(y_lo)` for `C40` =
`atan(223/(792+40))` = **`15.00425801922111°`**, matching `phase1_
proposal.md` §2's table to the printed digit. T21's own established fringe
period, `P(theta)=lambda/(A*cos(theta))` at `A=752`, `CPL[600]=20`,
`theta=39°`: `degrees(20/(752*cos(radians(39))))` = **`1.9607950099405438°`**,
matching the committed `t21_fringe_period_A752_600nm_39deg` exactly. Both
reproduce independently from the raw geometric/material primitives, not
from either write-up's prose.

---

## 3. Direct answers to the task's own questions

**Does the realizability caveat (Idealization 1) hold up under independent
scrutiny at this much wider angular range than any prior cycle tested it
at?** No — the specific `Pearson r>0.9997` figure it cites does not
generalize from exp-078's `48°-54°` envelope to this cycle's own
`4.77°-15.50°` envelope; the correlation collapses to `0.74-0.88` at three
`ABSORB` depths and goes negative at a fourth (§2a). But the practical
conclusion the citation was used to support — that this idealization is
unlikely to move §5.3's headline finding — is independently confirmed true
anyway, by a direct recomputation at the correct envelope (§2b), for a
structural reason (Attack 1) that has nothing to do with admittance-choice
correlation at all. Both halves of this are load-bearing: the citation
needs correcting (a same-shift record-hygiene item, not a verdict change),
and the bottom line it gestured at survives independent, from-scratch
verification.

**Is the standing forward item — retarget the realizable-admittance
(`mu_r=1`) refit at the X-WALL, not the y-wall — still the right call given
this cycle's own finding that the y-wall construction can't discriminate a
real echo at all?** Yes, and more robustly so than before. exp-078's own
re-ranking reasoning for that retarget (the narrow-angle Pearson-r
invariance claim) has just been shown, by this review, not to generalize —
so if that had been the *only* reason to deprioritize a y-wall admittance
refit, this cycle would have weakened the case for the X-WALL retarget, not
strengthened it. It does not, because Attack 1 supplies an independent,
stronger reason that survives §2a's correction intact: this construction's
entire `theta_beam`-dependence is carried by geometry that has nothing to
do with `r()`'s specific form, confirmed directly (§2b) rather than merely
argued. A realizable-admittance refit of the CURRENT y-wall reduction
(single-edge or full-aperture-sum alike) would not plausibly move any
verdict, for a reason that has nothing to do with how close matched and
realizable admittances happen to sit at any particular angle — whereas
the X-WALL's own Test-B numbers (`r^2=0.0001-0.0418`, exp-077, an order of
magnitude below the SUPPORT bar) remain the one place on the whole T28
board where this specific substitution could plausibly still matter,
because that model's `theta_beam`-dependence is NOT geometry-locked the
same way. The retarget stands, now on firmer ground.

**Does the structural finding (Red Team's Attack 1) change anything about
the realizability question specifically, or is it fully orthogonal?** Not
fully orthogonal, but not a resolution either — it changes the *relevance*
of realizability to THIS reduction without touching the *underlying bound*.
Attack 1 makes the admittance formula's realism practically moot for
scoring the current y-wall construction (§2b: swapping it changes nothing
scored, matching the ablation control's own more extreme result), which is
new information this seat did not have at exp-078 (where the invariance
argument, now shown fragile, was the only basis for a similar conclusion).
But Attack 1 says nothing about whether a *future, different* y-wall
instrument — the plane-wave/global-steering construction Red Team's own §8
names as the genuinely different next move, were it built — would face the
same realizability question with the same or different urgency; that
instrument does not yet exist, and per this cycle's own §2a finding,
nothing about admittance-sensitivity at one geometry may be assumed to
transfer to another without a fresh check. The underlying bound (is any
realizable coating for this engine's graded-loss boundary a buildable
`mu_r=1` structure, for either wall orientation) remains exactly where
exp-075/077/078 left it: untested, unobtainium only for the matched
construct actually used.

---

## 4. Ranked top-3 candidate next directions (MATERIALS' own lens)

1. **Execute the still-unexecuted realizable-admittance (`mu_r=1`) refit on
   the x-wall's own two-wall model** (`experiments/077-.../`, `PAIR_PAD`/
   `PAIR_ABSORB40` Test A+B). Now the single oldest-deferred MATERIALS item
   on the whole T28 board — carried unexecuted across exp-078 AND exp-079
   (this cycle makes it three cycles), independently reconfirmed here as
   the only place on the board a realizability substitution could
   plausibly move a verdict, since the y-wall's own Test A is now shown
   robust to admittance choice by two independent methods across two
   different angular regimes (the ablation control, §5.3 of `phase1_
   proposal.md`, and this review's own §2b). Zero new FDTD — reuses
   `boundary_reflectance.py`'s already-committed transfer-matrix machinery
   and already-collected real data, exactly as this review's own §2b did
   for the y-wall.
2. **Same-shift correction to `phase1_proposal.md` §6 Idealization 1**
   (record hygiene, zero cost): replace the bare "near period-invariant...
   Pearson `r>0.9997`" citation with the corrected picture this review
   establishes — the invariance claim is envelope-specific (true at
   exp-078's `48°-54°`, false at this cycle's own `4.77°-15.50°`), but the
   practical conclusion (this idealization does not move exp-079's own
   scored numbers) is independently reconfirmed by direct recomputation at
   the correct envelope, not merely inherited. Matches this program's own
   R8/R9 discipline: a specific, affordable, previously-unrun check now
   exists and should not be left un-folded into the permanent record for a
   future cycle to rediscover the gap or, worse, to cite the uncorrected
   `r>0.9997` figure as a general fact about "the y-wall."
3. **Before any future y-wall instrument is built** — specifically the
   plane-wave/global-steering construction Red Team's own §8/§9 names as
   the genuinely different next move, the one construction on this board
   that would NOT inherit Attack 1's geometry-locked limitation — **price
   its admittance-sensitivity from the start**, as a five-minute desk
   check against both formulas at whatever angular range that construction
   actually uses, rather than importing either this cycle's or exp-078's
   own conclusion by analogy. §2a's own finding is the concrete cautionary
   precedent: admittance-choice sensitivity is not a portable property of
   "the y-wall," it is a property of the specific construction and angular
   range being tested, and must be re-measured, not assumed, each time
   either changes.

---

## Compliance note

No RULED OUT item (R1-R9) is re-proposed or re-litigated. R4/R9: every
number cited from the existing record was independently re-derived from
committed JSON, source, or raw geometric/material primitives (§2a-§2d), not
hand-typed from either write-up; §2a/§2b's tables are disclosed as this
review's own fresh computation, not attributed to any prior cycle. Per R8's
standard, §2a/§2b are reported as actually-computed checks, not
re-reasoning about an inherited claim: I did not assume the exp-078
Pearson-r figure carried over to this cycle's own wider envelope, and I did
not assume the resulting divergence would matter to Test A either — both
were computed, and the two answers point in different directions (the
citation fails; the bottom line survives anyway), which is exactly why
both needed to be checked rather than one inferred from the other.
