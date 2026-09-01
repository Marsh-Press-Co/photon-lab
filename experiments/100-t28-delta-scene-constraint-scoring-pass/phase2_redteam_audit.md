# Phase 2 — RED TEAM final audit (Panel Iteration 77)

Input packet: PANEL.md, LOGBOOK.md (full), `phase1_proposal.md`, all five
Phase-2 blind critiques, plus independent re-derivation from primitives
(`lab/emit.py`, `lab/ambient.py`, `lab/sections.py`, `lab/phase_lines.py`,
`experiments/090/093/094/098/099-.../run.py` and `results.json`). Every
claim below is marked **[verified from primitives]** (I re-derived it
myself against source/data, independent of any seat's word) or **[relying
on critique, spot-checked]** / **[relying on critique, not independently
re-derived]**.

## 0. Housekeeping check

Word caps: none of the five critiques exceed PANEL.md's 150-word steel-man/
attack caps by inspection — no repeat of Iteration-76's own VISION finding
("3 of 5 Phase-2 critiques exceeded the 150-word cap"). **[verified]**

Arithmetic: Tier 2 Leg B's "4 angles × 2 keys × 2 conditions = 16" reproduces
(4×2×2=16); no R19-class call-count/row-count conflation found anywhere in
the proposal's own §6 budget section. **[verified]**

---

## 1. Numbered attacks

### RT-1 — [inconsistency] Leg B's four angles are `delta_scene(θ)`'s own zero-crossings — the worst possible sampling for the question Leg B claims to answer

**Claim.** The "four already-established cpl=20 crossings"
(37.127246°, 38.590230°, 40.265420°, 41.460901°, cited from
`experiments/090-.../results.json::q8.crossings_deg`) are not generic
"crossings" — they are the literal **zero-crossings of `delta_scene(θ)`
itself**, computed in `experiments/090-t28-floor-frac-threshold-fit/run.py`:

```
delta083 = np.array(j083["delta_scene"])
crossings = find_zero_crossings(thetas083, delta083)
```

(`run.py` lines 295–299, confirmed by direct read — `j083["delta_scene"]`
is exp-083's own 31-point dense sweep). Tier 2 Leg B spends its entire
16-call budget measuring `beam_behind_t28`/`observer_record_t28`
**exactly at the points where `delta_scene` is smallest (≈0) by
construction**, not at its peaks. The proposal's own §7 open question 1
raises a related but strictly weaker concern (crossing-spacing vs. the
2.9474° period — an aliasing worry); it never names the more basic
problem that these are literal nulls of the very quantity whose
constraint-1/2 threat Leg B is supposed to measure. The Leg-A-cited
largest on-file value (`+2.778×10⁻³` at θ=42.960901°, exp-099) sits at an
angle **outside** Leg B's four-angle set entirely. This structurally
biases Leg B toward a clean PASS/near-camera-floor finding regardless of
whether `delta_scene` poses any real risk at its actual extrema — the
proposal's own predicted "confident lean: PASS" for `beam_behind_t28` and
"CLEAN" for the registration gate should be read as near-guaranteed by
sampling design, not as an informative test of the phenomenon.

**Tag:** [inconsistency] (the design's own stated purpose — measuring
whether `delta_scene`'s ripple threatens constraints 1/2 — is
incompatible with the angle set chosen to test it). Downstream, this
becomes a live **[constraint-1-violation]/[constraint-2-violation] risk
**: a genuine termination-margin or backscatter problem tied to
`delta_scene`'s peaks could exist and pass this cycle's Leg B silently,
because Leg B never looks there.

**Verification status: [verified from primitives]** — I independently
opened `experiments/090-.../run.py` and confirmed `find_zero_crossings`
is applied to `j083["delta_scene"]`, not to any other quantity. None of
the five blind critiques caught this.

**Mandatory fix:** before Phase 3 freeze, either (a) add angles at/near
`delta_scene`'s own local extrema inside the already-characterized
36°–43° window (comparable low marginal cost to the existing 16 calls,
per the proposal's own cost model) so Leg B actually stress-tests the
largest available signal, or (b) explicitly retitle Leg B's own scope in
§3/§4/Idealizations as "constraint-1/2 exposure at `delta_scene`'s own
nulls — a near-worst-case-for-detection design" and strike every
downstream inference from a clean Leg-B reading to "no constraint-1/2
risk from `delta_scene`" in general.

---

### RT-2 — [unfalsifiable] Tier 1 item 1(a)'s correlation test has no pre-registered decision threshold

**Claim.** `r(delta_scene, frac_p_abs)`, pooled, with a 20,000-trial
permutation null, is the proposal's own primary test of whether
`delta_scene` carries genuine article-coupled content. The predictions
table commits only a qualitative "weak lean toward small/non-significant
r... not a confident lean" — no explicit α (e.g. permutation p<0.05) or
minimum-effect-size band is committed before the desk aggregation runs.
Every substantive prior decisive test in this exact sub-thread commits a
numeric band before running (exp-071's 30% CONFIRM floor/R5's own house
rule; exp-087's `RATIO_HIGH=10`; exp-076's 9-cell/5-outcome exhaustive
table) — this program's own R7/R10 lineage exists precisely to prevent a
correlation or significance result from being read after the fact
whichever way is convenient. As filed, a small `r` can be narrated either
as "confirms majority-PAD" or "small but directionally suggestive of
coupling," and neither reading is falsified by the design as written.

**Tag:** [unfalsifiable].

**Verification status: [verified from primitives]** — checked directly
against §4 and the Tier-1-item-1 procedure text in `phase1_proposal.md`;
no threshold appears anywhere in the document.

**Mandatory fix:** commit, before Phase 4, an explicit permutation-p
threshold and/or a minimum `|r|` floor that will be read as "coupling
detected" vs. "majority-PAD" — stated once, in writing, before the
aggregation is run (it costs nothing; the aggregation script already
exists conceptually and the null test is already specified).

---

### RT-3 — [unfalsifiable] / [process] Tier 2 is not actually "gated on Tier 1's outputs" as LOGBOOK's own commissioning ranking requires — live risk of an eighth T1:N/A deferral dressed as progress

**Claim.** LOGBOOK's Reconciled Iteration-77 queue (Iteration 76, exp-099,
Red Team's own final ranking) states explicitly: *"Tier 2 — the
constraint-1/2/3/4 scoring pass itself..., **gated on Tier 1's outputs**
but not deferred an eighth cycle."* The proposal runs Tier 1 and Tier 2
in the same cycle with **no actual gate**: Leg A is stated "mandatory
both branches" (§2, Tier 2 Leg A heading) and Leg B's 16 FDTD calls are
committed unconditionally — nothing in the document describes a branch
point where a Tier-1 finding of "majority-PAD, non-significant r" would
change what Tier 2 measures, how it is scored, or (most importantly) what
T1-label the cycle's own eventual Combined Verdict is permitted to carry.

This matters because the proposal's own predicted lean (§4) is precisely
that Tier 1 will find `delta_scene` majority-PAD/non-coupled ("Weak lean
toward small/non-significant r"). If that lean is confirmed, Tier 2's
scoring — however cleanly it comes back — is measuring a domain-geometry
artifact's magnitude against perceptual/beam thresholds, not testing the
angular-selectivity escape route. QUANTUM's and MATERIALS' own blind
Phase-5 finding at Iteration 76 named exactly this risk in writing:
*"delta_scene's own realizability content... was never resolved...
NOTES.md's own T1 trigger risked scoring a domain-geometry artifact as a
material mechanism if honored literally next cycle."* The proposal's own
framing language — "the first cycle in seven to actually touch
constraint-1/2/3 scoring on `delta_scene(θ)`" — is exactly the phrasing
that could read, to a future LOGBOOK skimmer or at Checkpoint, as if the
seven-cycle T1:N/A drift was substantively broken this cycle, even if the
honest label for the whole cycle turns out to still be T1:N/A once Tier
1's own result is in. That would be an **eighth deferral in substance,
not merely in name** — precisely the "constraint quietly dropped"/
"unfalsifiable claim of progress" pattern Checkpoint criterion 4 exists
to catch.

**Tag:** [unfalsifiable] (primary — an unpinned claim of "progress on T1"
that is not yet falsifiable against Tier 1's own not-yet-run result),
secondarily [process] (a direct, citable divergence from LOGBOOK's own
commissioning instruction that Tier 2 be gated on Tier 1).

**Verification status: [verified from primitives]** — the "gated on Tier
1's outputs" text is quoted verbatim from LOGBOOK (Iteration 76 entry,
Reconciled Iteration-77 queue, read in full above); the "mandatory both
branches" / unconditional-16-calls language is quoted verbatim from
`phase1_proposal.md` §2. None of the five critiques raised this.

**Mandatory fix:** pre-register, before any run, the T1-label consequence
of EACH of Tier 1's three possible outcomes — (i) majority-PAD/no
coupling → the cycle's own Combined Verdict states **T1: N/A**
explicitly, naming `delta_scene` as excluded from the angular-selectivity
class for this specific signal, not narrated as "the first cycle to
touch scoring"; (ii) genuine coupling found → T1: angular-selectivity,
partial/gated evidence, scoped to this bench/wavelength/angle-window
only; (iii) ambiguous/underpowered — state explicitly that Tier 2's
numbers are filed as instrument-characterization only and do not move T1
in either direction. This mirrors exactly the per-outcome pre-registration
MATERIALS independently proposed for Tier-1 item 2 (§ below) — the same
fix, applied one level up, to the cycle's own headline verdict.

---

### RT-4 — [inconsistency] `observer_record_t28`'s mirror construction is provably wrong, independent of EM's critique (re-derived from `lab/emit.py` primitives)

I re-derived this from scratch, without relying on EM's own algebra, to
confirm it independently.

`lab/emit.py:80-127` documents and implements: `Ez = a+ + a-`,
`Hy = -(S·kx/ω)(a+ - a-)`, where `a+` is the +x-traveling amplitude and
`a-` the -x-traveling amplitude (confirmed by substituting a pure plane
wave `e^{i(kx·x-ωt)}` into Faraday's law as coded, `dHy/dn = S·dEz/dx`).

For a 2D TMz mode, `Ez` is a true (polar) vector component lying **in**
the mirror plane (the mirror is the y–z plane, normal along x); a polar
vector's in-plane components are unchanged in sign under reflection.
`Hy` is a pseudovector (axial) component also lying in the mirror plane;
a pseudovector's in-plane components **flip sign** under reflection
(pseudovectors and polar vectors transform oppositely under any
improper/reflection operation, `det(R)=-1`). So a correct x-mirror is
`Ez'(x') = Ez(nx-1-x')` (bare index reversal, no sign change) but
`Hy'(x') = -Hy(nx-1-x')` (index reversal **and** a sign flip) — exactly
EM's claim.

I then solved the consequence algebraically for a pure `a-` wave (the
physical case here: this bench's source sits at high-x propagating -x,
so the empty-scene field at the observer plane is essentially pure `a-`).
Applying the proposal's construction (`Ez` mirrored correctly, `Hy`
mirrored **without** the sign flip) to `Ez=C`, `Hy=+(1/scale)·C` (the
correctly-mirrored `Ez`, and the incorrectly-mirrored `Hy`, both
evaluated at the same mirrored point) and solving `Ez'=a++a-`,
`Hy'=-(1/scale)(a+-a-)` for `a+`,`a-` gives **`a+=0, a-=C`** — i.e. the
mirrored capture reads bit-for-bit as if no mirror had been applied at
all. The buggy mirror is not merely "somewhat wrong" — it is exactly as
wrong as omitting the mirror entirely, because the missing `Hy` sign
flip precisely cancels the intended effect of reversing `Ez`. This
reproduces EM's predicted consequence — `a_fwd=0`, `a_bwd=`full beam on
the empty-scene capture — by an independent derivation.

**Tag:** [inconsistency] (a stated construction that provably does not
do what it is claimed to do, verified two independent ways: EM's and
mine).

**Verification status: [verified from primitives, independently
re-derived]** — see EM's ruling below for disposition.

---

### RT-5 — [process] Idealization 65 will be stale the moment RT-4/EM's fix is adopted

Idealization 65 discloses an assumption specific to the array-mirror
construction ("assumes the domain's two x-boundary absorbing bands are
symmetric"). EM's mandated fix (§ below) replaces the mirror with an
unmirrored call plus a `p_fwd`/`p_bwd` label swap — a construction that
has no such assumption to disclose. If the mirror fix lands and
Idealization 65's text is left in place unedited, it becomes a stale
idealization describing a code path that no longer exists — a small
instance of the exact "claimed scope must match actual code" discipline
R18 exists to police, one level down (an idealization, not a check, but
the same shape).

**Tag:** [process]. Low severity, cheap to fix (delete/rewrite
Idealization 65 in the same edit that applies EM's fix).

**Verification status:** [verified from primitives] — direct read of
Idealization 65's own text against EM's proposed replacement.

---

### RT-6 — [inexpressible]: not applicable this cycle, stated for the record

No new mechanism is proposed (§1 states this explicitly and correctly);
this is an instrumentation/scoring pass over an already-existing signal,
not a claim requiring new simulation-parameter machinery. There is
nothing to strike on [inexpressible] grounds — flagged here only so the
record shows Red Team checked for it, matching this program's own
"T1 route N/A" self-disclosure precedent.

---

## 2. Ruling on each of the five critiques' own findings

### PHOTONICS — T21's 750nm/θ=40° fringe (0.0237, 4.7×`C_thr`) is an unaddressed same-window contamination-risk precedent

**Verification: [verified from primitives].** LOGBOOK line 1863 states
verbatim: *"...750nm/θ=40° amplitude — 0.0237, 4.7× VISION's own T2
photopic C_thr — pose a contamination risk for any future near-±40°
constraint-3 run"* (opened Iteration 18/19, T21), and Iteration 19's own
close states explicitly: *"The T21 fringe's contamination-risk status for
any future near-±40° constraint-3 run is NOT settled."* This is the
**identical 36°–43° angle band** Tier 2 Leg A scores, at a wavelength
this cycle never touches. PHOTONICS' attack is fully correct and, if
anything, understated: this is not merely an untested risk, it is an
**explicitly-still-open, previously-flagged, on-file contamination
question in the exact window being scored**, now inherited silently a
second time.

**Ruling: ADOPTED (mandatory fix).** Add the idealization PHOTONICS
specifies, naming the 4.7× precedent explicitly, and require any Tier-A/
Tier-W disposition drawn from Leg A to carry a λ=600nm-only caveat
inline — matching Idealization 64's own angle-window discipline exactly.

### MATERIALS — Tier-1 item 2 ("disposition memo") is a category error as scoped

**Verification: [relying on critique's factual claims, spot-checked and
confirmed]** — I independently confirmed (a) the Iteration 59/60
provenance quoted ("genuine ambiguity remains between two
opposite-realizability readings") reproduces LOGBOOK's own Iteration-60
Phase-5 text verbatim; (b) `delta_scene`'s period (2.9474°) is within
3.7% of `P_edge_A=2.8421°` per Iteration 60's own PRIMARY finding; (c)
PHOTONICS' Iteration-60 Phase-5 finding that `P_edge_A` traces to the
EMPTY-scene exp-069 run (`run.py` "contains zero article/materials
calls") is exactly as MATERIALS describes. The factual substrate is
solid. The category-error argument itself ("neither pole needs a
realizability tier") is a reasoned inference from those facts, not
independently re-derivable as an objective fact, but it is well-grounded
and the proposed remedy (a pre-registered per-outcome conditional) is
strictly better than the current text under any reading — it costs
nothing extra and directly forecloses the "fourth restatement" risk.

**Ruling: ADOPTED (mandatory fix, zero marginal cost).** Rescope item 2
into MATERIALS' proposed conditional: state, before item 1 runs, what
realizability tier follows from each of item 1's two possible outcomes.
Note for the record: this is the *same* pre-registration discipline
RT-3 above independently requires for the cycle's own T1 label — the
proposal should apply this pattern once, consistently, at both the
item-2 and the whole-cycle level.

### ELECTROMAGNETISM — `observer_record_t28`'s array-mirror is missing a required Hy sign flip

**Verification: [verified from primitives, independently re-derived —
see RT-4 above].** EM's electromagnetic derivation and its stated
consequence (`a_fwd=0`, `a_bwd=`full beam on the empty-scene capture) are
both confirmed exactly, by a route independent of EM's own text (the
pseudovector-parity argument plus direct algebraic solution of the `a+`/
`a-` system under the buggy mirror).

I additionally checked whether the proposal's own **other** new
extraction, `beam_behind_t28`, uses the correct convention for the same
class of fix: it applies a plain sign negation to `sections.flux_profile_
x`, "mirroring `ambient.observer_profile`'s own established convention."
I confirmed `lab/ambient.py:36-39` defines
`observer_profile = -sections.flux_profile_x` exactly — a scalar sign
flip, no array mirror. So `beam_behind_t28` (i) already uses the correct,
established idiom; only `observer_record_t28` (ii), in the same
proposal, deviates from it. This makes EM's fix doubly well-motivated:
it does not just correct a bug, it brings (ii) into line with how (i), in
the very same document, is already done correctly.

**Ruling: ADOPTED (mandatory fix, not merely non-blocking).** I agree
with EM's own verdict text that the empty-scene validation gate is
*likely* to catch this live — but per this program's own R8 discipline
(an unverified robustness argument is not sufficient to file a flagged
defect as non-blocking when an affordable, fully-specified, zero-marginal-
cost fix already exists), gambling on an as-yet-unwritten gate producing
a clean, interpretable HALT — rather than a silent divide-by-near-zero
blowup in `flux = flux / reference["p_forward_total"]` when
`p_forward_total≈0` — is exactly the shape of argument R8 exists to
forbid. Apply EM's specified fix (unmirrored `observer_record` call,
`p_fwd`/`p_bwd` label swap) before Phase 4 code exists. See RT-5 for the
required companion edit to Idealization 65.

### THERMODYNAMICS — `netd_row()` listed as reused but never called on the 4 new Tier-2-Leg-B pairs

**Verification: [verified from primitives].** Confirmed `netd_row()`
exists exactly as described at `experiments/093-.../run.py:185`
(`def netd_row(pm):`) and `cell_metrics_r4` at
`experiments/094-.../run.py:305`, whose body (read directly, lines
~320-345) unconditionally builds
`thermo = dict(sigma_ext_cells=..., ratio_abs_ext_raw=..., p_abs_w=...,
dt_ss_full_K=..., netd_classification=...)` for every cell processed —
matching THERMODYNAMICS' cited line ranges closely and its factual claim
exactly. I then re-read `phase1_proposal.md` end to end: `netd_row()`
appears exactly once, in the §2 tools-reused list; it is never invoked,
scheduled, or even mentioned again in Leg B's own procedure, the
Predictions table (§4), or the Idealizations (§5).

This is not a first-time gap. It is the **same shape**, on the **same
NETD-persistence channel**, for at least the third time on record: (1)
exp-092/93's boundary (closed by exp-093's own `netd_row()` fix); (2)
exp-094 (Iteration 71, R16's own founding non-firing instance — new code
that never called `netd_row()` at all); (3) exp-099/Iteration 76,
THERMODYNAMICS' own self-review finding that "its own charter instrument
(the thermal/energy sidecar) was silently omitted from Result/Learned at
R5's two landmark first-ever points" (LOGBOOK lines 6688-6691, confirmed
verbatim). R16's own standing forward-elevating clause states: *"a third
occurrence of 'a disclaimer travels but the field it is meant to cover is
never persisted,' on this or any T28-adjacent channel, in any form, fires
Checkpoint criterion 4 automatically."*

**Ruling: ADOPTED (mandatory fix, elevated severity).** This is not
optional polish. Add one explicit line committing to call `netd_row()`
on all 4 `(C40_R4,G40_R4)` pairs and persist the result, disclaimed per
the module's own EXPRESSIBILITY CONTRACT — exactly as THERMODYNAMICS'
own flip-parameter specifies. Red Team additionally flags: if this ships
to Phase 4 unfixed, and the data is again dropped, the Director should
treat R16's third-occurrence clause as live, not as another "close call."

### VISION SCIENCE — (a) construct validity of `C_thr(L)` for a swept/modulated quantity; (b) stale scotopic anchors

**(a) Verification: [verified from primitives].** LOGBOOK's Iteration-24
Phase-5 VISION review states verbatim: *"Found C_thr(L) is a static-target
threshold applied to a physically transient event (T3 still unbuilt)"*
(line 14437-14438) — VISION's citation for exp-100 reproduces this
exactly. That precedent concerned a different transient (a self-glare
sweep), but the underlying construct-validity objection generalizes
cleanly: `C_thr(L)` is T2's steady-adaptation, extended-uniform-patch
threshold (Iteration-1 idealization ii, "area contrast, not edge-profile
detectability" — consistent with everything I read about T2's own
derivation), and `delta_scene(θ)` is a ~2.9474°-period oscillation
revealed by sweeping θ — content T3 (still the program's longest-standing
unbuilt instrument, confirmed nowhere built in the full LOGBOOK read) was
built specifically to score. This is a real, previously-established,
on-point objection that the proposal's own text does not address at all
(the proposal's caveats are about *instrument floor*, not *construct
validity* — two different failure modes).

**(b) Verification: [verified from primitives].** I read the actual
Iteration-1 pre-correction draft table (Red Team's own Phase-5 attack #2,
LOGBOOK lines 6907, 6936-6941): the *originally committed* numbers were
`L*_lab=5.3×10⁻⁶` (correct, survives) and `L*_field=4×10⁻⁵` (WRONG — Red
Team's own re-derivation from the committed function gives `1.7×10⁻⁴`),
with `1.7×10⁻⁴` cited only as the section's moonless-rural-sky
*reference* point, not a threshold. The Phase-3 synthesis (lines
6996-6999) replaced this with the corrected exponent-spanning band:
`L*_lab∈[5.3×10⁻⁶,7.5×10⁻⁵]`, `L*_field∈[1.7×10⁻⁴,1.2×10⁻³] cd/m²`. The
proposal's cited "`L*≈5×10⁻⁶–4×10⁻⁵`, moonless-rural`≈1.7×10⁻⁴`" is,
digit for digit, the **superseded pre-correction draft table**, not the
committed Phase-3 band — despite being introduced as "T2's own committed
table verbatim." This is a clean, textbook R4-class defect (a claimed-
verbatim citation that does not reproduce from its own cited source),
caught here at Phase 2, before Phase 3 freeze — exactly where this
program's own R4/R20 discipline wants it caught.

**Ruling: ADOPTED, both (mandatory fixes).** (a) Add the caveat VISION
specifies: any Leg-A PASS/FAIL reading is a static-contrast bound only,
provisional pending T3, not a completed Tier-W/Tier-A verdict on a swept
angular fringe. (b) Replace the stale anchors with the corrected Phase-3
band verbatim, as VISION specifies. Per VISION's own stated condition
("If Leg A's 'complete both tiers' language ships unchanged, carrying the
superseded numbers as 'verbatim T2,' I move to oppose"), both fixes are
required for this item to remain support-with-changes rather than
oppose — Red Team concurs with that conditioning explicitly.

---

## 3. Overall verdict

**PROCEED-WITH-MANDATORY-FIXES.**

None of the nine findings below individually invalidates the cycle's
premise — Tier 1's zero-FDTD partition and Richardson characterization
remain sound as designed, and Tier 2 Leg B's basic instrument-build
(observer camera + beam-behind extraction on a new bench) is legitimate,
overdue work. But the fixes are not optional polish: three of them
(RT-1, RT-3, THERMODYNAMICS'/netd_row) sit directly on top of this
program's own most sensitive standing tripwires (a sampling design that
cannot detect the thing it claims to test; a T1-labeling ambiguity that
could read as discharging a seven-cycle drift while substantively
extending it; a NETD-persistence gap on its third occurrence). Ship all
nine before Phase 3 freeze.

**Mandatory fixes, numbered to match the attacks above:**

1. **(RT-1)** Add angles at/near `delta_scene`'s own local extrema to Leg
   B (or explicitly rescope Leg B's claims to "constraint-1/2 exposure at
   `delta_scene`'s own nulls only").
2. **(RT-2)** Pre-register an explicit numeric decision threshold
   (α and/or effect-size floor) for Tier-1 item 1(a)'s correlation test.
3. **(RT-3)** Pre-register, per Tier-1 outcome, exactly what T1 label the
   cycle's own Combined Verdict will carry — before any run.
4. **(RT-4/EM)** Replace `observer_record_t28`'s array mirror with EM's
   specified unmirrored-call-plus-label-swap fix.
5. **(RT-5)** Delete/rewrite Idealization 65 in the same edit as fix 4.
6. **(MATERIALS)** Rescope Tier-1 item 2 into a pre-registered
   per-outcome conditional, not a flat restatement.
7. **(THERMODYNAMICS)** Commit to calling `netd_row()` on all 4 new
   `(C40_R4,G40_R4)` pairs and persisting the result.
8. **(VISION-a)** Add the static-vs-transient construct-validity caveat
   to any Leg-A PASS/FAIL claim, citing T3's own still-unbuilt status.
9. **(VISION-b)** Replace the stale Iteration-1 draft scotopic anchors
   with the corrected Phase-3 band, verbatim.

**Checkpoint criterion 4 (unfalsifiable claims / a constraint quietly
dropped — especially #3): AT RISK this cycle, not yet fired.** Two live
vectors: (i) RT-3's T1-labeling ambiguity — if Phase 3/5 ship an
uncorrected "first cycle to touch scoring" headline while the underlying
Tier-1 result turns out (as predicted) to show no real coupling, that
*is* an unfalsifiable claim of progress on the central tension, caught
here pre-freeze; (ii) THERMODYNAMICS' netd_row() gap, which is now a
credible third occurrence of R16's own named pattern. Neither has yet
survived to a defended Result/Learned section — this is exactly the
"non-firing, caught blind before LOGBOOK" shape this program's own R4/
R6-R20 lineage credits, **provided** fixes 3 and 7 are actually adopted
at Phase 3, not merely acknowledged. Constraint 3 specifically ("the hard
one — do not let it slip") is touched by Leg A's own scoring; fixes 1, 8,
and 9 are the load-bearing protections against a quiet overclaim there.

**On the "seven-then-eight consecutive T1:N/A cycles" question,
directly:** As filed, this design is at real risk of becoming an eighth
deferral in substance while reading as the first break in the streak —
precisely because (a) the proposal's own predicted lean is that Tier 1
will find no genuine coupling, (b) Tier 2 runs unconditionally regardless
of that outcome, contrary to LOGBOOK's own "gated on Tier 1's outputs"
commissioning language, and (c) nothing pre-commits what T1 label the
cycle is allowed to claim under that predicted outcome. With fix 3 (and,
to strengthen the test itself, fix 1) adopted, this cycle becomes a
genuine, meaningful step: the first real constraint-1/2 FDTD measurement
on this exact signal, honestly labeled whichever way Tier 1 actually
comes out — a legitimate mapped-boundary result even if the honest
verdict is "T1: N/A, `delta_scene` excluded from the angular-selectivity
class." Without fix 3, Red Team's assessment is that the drift is not
being addressed, only re-narrated.
