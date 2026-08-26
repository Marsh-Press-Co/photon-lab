# Phase 2 — RED TEAM Audit (exp-076, Panel Iteration 53)

**Seat: RED TEAM.** Read: `LOGBOOK.md` in full (RULED OUT R1–R8 in full;
LIVE THREADS T1–T28 in full, T21/T24/T27/T28 read closely); `PANEL.md`;
`phase1_proposal.md`; both supporting files; all five blind Phase-2
critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, VISION
SCIENCE). Independent verification performed computationally this cycle
(all zero-new-FDTD, per the Director's scope): re-ran
`g0e_amplitude_channel_check.py` to completion (matches committed output
bit-for-bit: Case 1 worst 1.03×10⁻⁴, Case 2 worst 8.35×10⁻³, PASS); re-ran
`experiments/065-.../design_geometry.py` (reproduces the G40 congruence
table and the `[1b] ALIASING CHECK` block bit-for-bit); independently
recomputed `amp_ratio`/`delta_P_obs` for all four baseline pairs directly
from `experiments/072-.../results.json` (0.16106/0.04067/0.01976/0.16587,
`delta_P_obs(C40,C80)=0.06684`° — matches the proposal and all five
critiques to stated precision); read `experiments/072-.../run.py` in full,
including the `rho_c`/`rho_c_common_carrier_residual` machinery this
cycle's §4(c2) explicitly builds on; confirmed via `grep`/direct read that
`experiments/066-.../run.py`'s Block STRESS settling test uses only `C40`
and `experiments/069-.../design_geometry.py`'s Block SETTLE uses only
`C80`; confirmed `experiments/069-.../results.json::block_leg750` is a
already-committed, 16-point, `STEPS=2800`, non-aliased 750nm leg for
`C40`/`C80` (θ∈[38°,41°], 0.2° step) — a fact none of the five critiques
used.

---

## Numbered attacks

### Attack 1 — §4's falsifiable bands are neither mutually exclusive nor exhaustive [inconsistency]

None of the five blind critiques checked this. Treat `x = amp_ratio
(PAIR_PAD)`, `y = amp_ratio(PAIR_ABSORB40)`, both ≥ 0 by construction
(they are magnitudes). The three named outcomes are:

- (a): `y ≥ 0.116` **AND** `x ≤ 0.050`
- (b): `x ≥ y` **OR** `x ≥ 0.116`
- (c1): `x < 0.050` **AND** `y < 0.050`

**Not mutually exclusive.** (b)'s first disjunct (`x ≥ y`) carries **no
magnitude floor at all** — it resolves for literally any pair of distinct
non-negative reals, however small. Concretely: `x=0.04, y=0.01` satisfies
(c1) ("both small... near-noise-floor") **and** satisfies (b) via
`x ≥ y` — the SAME data point simultaneously trips "(b): five iterations
of T28 causal claims... must be re-read as possibly padding/domain-
geometry-tied... a real, load-bearing correction" and "(c1): neither
pure-axis effect individually clears the smallest established baseline
reading." Given PHOTONICS' own, independently-confirmed finding that no
error bar exists on either `amp_ratio` reading, a hairline `x` vs `y`
ordering at these magnitudes (comparable to the established
`C70–C80=0.0198` floor) is exactly the kind of noise-level tie-break that
should never be allowed to trigger "(b)"'s strong load-bearing language
on its own.

**Not exhaustive.** Solve for the region NOT covered by any of (a)/(b)/
(c1): whenever `x < y < 0.116` **and** `y ≥ 0.050` (e.g. `x=0.03,
y=0.07`, or `x=0.08, y=0.15`), none of (a), (b), or (c1) fires — Phase 3
has no pre-registered verdict to apply. This is not an edge case: it is
precisely the outcome shape a genuine-but-modest, correctly `ABSORB`-tied
effect (real, but not large enough to clear the strict 0.7× reassurance
bar) with a near-zero `PAD` effect would produce — arguably the single
most physically plausible non-null result this design could return, and
it has no named verdict.

**Independent check performed, not asserted**: I solved the region
algebraically (see derivation above) rather than spot-checking a few
points; both the overlap and the gap are provable for open sets of
`(x, y)`, not isolated coincidences.

**Verdict: MANDATORY.** §4 must be rewritten before Phase 3 freeze so
that every possible `(x, y) ≥ (0, 0)` maps to exactly one named outcome,
and (b)'s "confound not relieved" language must carry its own magnitude
floor (e.g. require `max(x, y) ≥ 0.050` before an ordering comparison is
read as decisive), not a bare inequality between two point estimates with
no attached uncertainty.

### Attack 2 — the `rho_pad_absorb` interaction claim contradicts its own cited machinery [inconsistency / unfalsifiable]

This is the diagnostic the task brief specifically asked to be checked
against this sub-thread's own history of subtle errors in this exact
statistical machinery (R4/R6/R7/R8's trigger cycles), and it does have
one.

§4(c2) states: `rho_pad_absorb ≥ 1.00` is "a genuine, detectable
aggregate non-additivity signature — **real evidence an `ABSORB×PAD`
interaction exists** in the amplitude/period structure." §5 Idealization
3 justifies routing the additivity check through `delta_P_obs` rather
than `amp_ratio` by citing `delta_P_obs`'s "own established `rho_c`
convention, exp-072."

I read `experiments/072-.../run.py` directly (not the prose citing it)
and independently re-ran the relevant computation against the committed
`results.json`. Two findings, both load-bearing:

1. **`rho_c` was never evaluated on real data, in this program's entire
   history.** `p072_3 = "NOT_EVALUABLE"`, `rho_c = None` in the committed
   `experiments/072-.../results.json` — the gate (`if not
   all(adj_resolved): rho_c = None`) never fired because none of the
   three adjacent `ABSORB` pairs was ever `resolved`. Calling this a
   "established... convention" (§5, Idealization 3) is a citation of
   machinery that exists in code but has never once produced a scored
   number — exactly the class of unverified characterization R4/R8 exist
   to catch, now applied to this proposal's own supporting citation, not
   a prior cycle's.
2. **The source code itself explicitly disclaims the interpretation §4(c2)
   assigns to it.** `run.py` line 687–690: *"`rho_c` is therefore NOT a
   basis-stability check — it is entirely an artifact of each pair
   choosing its OWN `T_mean`, and is this cycle's cleanest single
   measurement of carrier sensitivity, not item 8's calibration
   target."* This is because `R_q` (and therefore `delta_P_obs`, which is
   built directly from `R_q`) is a genuinely LINEAR functional of the raw
   series **only when the design matrix — i.e. the carrier `(T_x, psi)` —
   is shared** across the pairs being summed. `rho_c_common_carrier_
   residual` (the shared-carrier version) is 1.325×10⁻¹⁶ — machine-zero,
   confirming the raw series telescope exactly (`G0-b`) and that a
   *shared*-carrier `R_q` telescopes trivially. The *gated* `rho_c` uses
   each pair's own independently-fit carrier — exactly what §5
   Idealization 3 discloses `PAIR_PAD`/`PAIR_ABSORB40` also do
   ("Different pairs use independently-fit carriers") — and for that
   construction, a nonzero telescoping gap is expected even under
   perfect physical additivity; it is a property of evaluating a
   nonlinear (carrier-fit-dependent) functional at three different
   linearization points, not evidence about the physics.

`rho_pad_absorb` is built the same way (`PAIR_PAD`, `PAIR_ABSORB40`, and
`(C40,C80)` each use their own independently-fit carrier — confirmed
directly against §2c/§5). It inherits the identical property: a large
value is **at least as consistent with carrier-choice sensitivity as with
a real interaction**, and this cycle's own `G0-e` check (which I
independently re-ran) validates `amp_ratio` recovery only — it never
tests whether `delta_P_obs`'s cross-pair telescoping gap is a physics
signal or a basis artifact. §4(c2)'s "real evidence... interaction
exists" language is not licensed by anything this cycle has actually
built or verified, and directly contradicts the disposition its own
cited precedent's source code carries.

One reassuring data point, computed independently this cycle (not in the
committed record, since `rho_c` was never gated): applying the *identical*
formula retroactively to the real baseline series gives `rho_c ≈ 0.041`
(`S = 0.06967+0.00850-0.00861 = 0.06957`° vs `D = 0.06684`°, gap
`0.00272`°/`0.06684` ≈ 4.1%) — small, i.e. in the one case this program
can check, the carrier-artifact contribution is modest. This is
suggestive, not dispositive (n=1, and it uses the ORIGINAL four-config
series, not this cycle's G40-based decomposition), and does not license
treating a future `rho_pad_absorb ≥ 1.00` as decisive interaction
evidence.

**Verdict: MANDATORY.** §4(c2)'s "real evidence... interaction exists"
language must be downgraded to something like: *"a disclosed, uncalibrated
magnitude signal that cannot, by this design, be distinguished from an
artifact of each pair's independently-fit carrier — the identical
construction in `experiments/072-.../run.py` is explicitly documented as
NOT a basis-stability or interaction test. No interaction claim may be
drawn from `rho_pad_absorb` alone."* §5 Idealization 3's "established
rho_c convention" phrase must be corrected to disclose that `rho_c` has
never been evaluated on real data.

### Attack 3 — §2c's "R_q is not used" claim is imprecise [inconsistency, minor]

§2c states plainly: *"`R_i`, `R_q`... are NOT part of this statistic and
are not used for any significance claim this cycle."* True for the
**gating** statistic (`amp_ratio`, built from `A_i`/`A_q` only — verified
directly against `_amp_ratio_recover()` and `analyze_pair()`). False as a
blanket claim: §4(c2)'s `rho_pad_absorb` is built from `delta_P_obs`,
which is `-(R_q/(2π·amp·f_bar))·T_mean` — a direct function of `R_q`.
No null-calibration/significance test is attached to it (so this does not
independently retrigger R7 — see Attack 6 below), but the blanket "not
used" phrasing overstates what §2c actually disclaims and should be
scoped precisely: *"not used in the gating `amp_ratio` statistic; `R_q`
is used, via `delta_P_obs`, in the disclosed-only `rho_pad_absorb`
diagnostic (§4c2), without null-calibration."*

**Verdict: MANDATORY but trivial** — a one-sentence correction, folds
into the same edit as Attack 2.

### Attack 4 — PHOTONICS' aliasing finding is correct; its proposed fix is underspecified [constraint-analogue: overstates decidability]

Independently reverified, not taken on trust: I re-ran
`experiments/065-.../design_geometry.py` myself. Its own `[1b] ALIASING
CHECK` block prints, verbatim: `ABSORB=40: ... 600nm=2.000 <-- INTEGER at
600nm`, `ABSORB=80: ... 600nm=4.000 <-- INTEGER at 600nm` (`G40` shares
`ABSORB=40` with `C40`, hence the identical 2.000λ reading — the script's
own congruence table confirms `G40`'s geometry is otherwise bit-identical
to `C80`). Every config this cycle runs at its one tested wavelength sits
on an exact integer-λ boundary-thickness point — the exact resonant
condition `C70` was added, in this identical sub-thread's own precedent
cycle (`experiments/065-...`), specifically to guard against. PHOTONICS'
attack is correct and, given that precedent, unusually well-grounded —
this is not speculative caution, it is a documented failure mode in this
exact codebase.

PHOTONICS' proposed fix (≈6 calls, `SWEEP_ANGLES` = `(-40,-38,-35,35,38,
40)`, 6 sparse points) is real and cheap, but underspecified in the
dimension that matters: `amp_ratio` requires the dense, ~31-point,
carrier-fitted window to exist at all (`carrier_fit`'s free-period search
needs a well-sampled multi-period window) — a 6-point sparse grid spanning
±35° to ±40° cannot reproduce the same statistic, only a cruder
point-difference comparison. Treating that as sufficient to "flip this to
plain support" (PHOTONICS' own words) overstates what 6 sparse points can
decide.

**Better, cheaper infrastructure exists and none of the five critiques
found it.** `experiments/069-.../results.json::block_leg750` is an
**already-committed**, `STEPS=2800`, 16-point, 0.2°-step, non-aliased
750nm leg for `C40`/`C80` (θ∈[38°,41°]; `ABSORB=40→1.6λ`, `ABSORB=80→
3.2λ` at 750nm — genuinely non-integer, confirmed directly). Extending
`G40` alone to this exact window (16 new FDTD calls, zero marginal cost
for `C40`/`C80`) gives a real, same-methodology `amp_ratio` computation
at a second, non-aliased wavelength, for a fraction of a full 31-point
leg's cost. Caveat, disclosed here rather than left implicit: this window
is narrower (3° vs. the 600nm window's 6°) than the window PHOTONICS'
own supporting detail already flagged as poorly conditioned for this
exact 5-column carrier-fit machinery (Cramér–Rao pricing, `cond9≈478–
529`) — so this cheap leg should be run and reported, but treated as
advisory, not decisive, pending a full matching-width leg.

**Verdict: MODIFY.** Adopt PHOTONICS' underlying concern as MANDATORY
(no wavelength-general citation of this cycle's (a)/(b) verdict is
licensed without it); replace the proposed 6-call sparse check with a
16-call `G40`-at-750nm leg reusing `block_leg750`'s exact window,
explicitly labeled advisory/narrow-window; require a full matching-width
(6°/31-point) non-aliased leg at a future iteration before any (a)/(b)
verdict from this sub-thread is cited as wavelength-general.

### Attack 5 — §4(a)'s prose gloss on the 0.050 threshold is numerically backwards [inconsistency, cosmetic]

§4(a) describes the `≤0.050` PAD-effect threshold as "at or below the
size of the smallest already-established adjacent-pair reading, `C70–
C80=0.020`." `0.050 > 0.020`, not `≤` — the threshold is 2.5× the cited
comparator, the opposite of what the prose says. The numeric threshold
itself is correctly computed (`0.3×0.16587≈0.0498≈0.050`, verified
independently); only the plain-language gloss is wrong. Low stakes on
its own, but this is exactly the R4-class defect this program has been
bitten by repeatedly (a hand-written characterization of a number, not
checked against the number it cites) — worth fixing in the same pass as
Attacks 1–3, not worth blocking on its own.

**Verdict: MANDATORY but trivial** — fix the sentence.

### Attack 6 — R7/seventh-cycle re-opening risk: independently checked, does not fire, but §7's margin is thinner than claimed

§7 argues `amp_ratio` reads off `A_i`/`A_q` (not `R_i`/`R_q`) and attaches
no null-calibration, so it sits outside R7's retirement ("a sign-flip/
permutation null on this ramped-quadrature OLS basis... certifying a
closure or detection claim"). I verified this directly against
`_amp_ratio_recover()`/`analyze_pair()`: correct — `amp_ratio` is
genuinely null-free and `R_q`-free. This holds.

But `rho_pad_absorb` (Attack 2/3) *is* `R_q`-derived and *is* used to
assert a physical claim ("real evidence... interaction exists") without
any null-calibration at all — arguably a step in the wrong direction from
R7's actual discipline (R7 requires fit-and-calibrate before a
closure/detection claim; `rho_pad_absorb` as written skips calibration
entirely rather than failing it). It does not literally retrigger R7's
narrow text (no null/permutation construction is built), so this is not
itself a rule violation — but it is the same underlying failure shape
(an `R_q`-derived quantity licensing a "real evidence" claim without the
calibration step this exact sub-thread's rules exist to force) in
adjacent form, one cycle after R8 was adopted for precisely this pattern
(an unverified argument substituting for an affordable check). Closing
Attack 2 (downgrading the "real evidence" language) closes this risk too;
no separate fix is needed beyond that one.

**Verdict: no independent fix required — resolved by Attack 2's fix.**

---

## Disposition of the five critiques' proposed fixes

| Critique | Fix proposed | Disposition |
|---|---|---|
| **PHOTONICS** | ~6-call second-λ `SWEEP_ANGLES` leg | **MODIFY** — see Attack 4. Replace with a 16-call `G40`-at-750nm leg reusing the already-committed `block_leg750` window; keep PHOTONICS' underlying "no wavelength-general citation without this" requirement as MANDATORY. |
| **MATERIALS** | One sentence: `ABSORB`/`PAD` are the same representational class, neither carries more physical standing | **ADOPT**, verbatim, applied uniformly to §4(a) and §4(b) as MATERIALS specifies. Independently reviewed §4's language myself; MATERIALS' reading is accurate and the fix is correctly scoped — a real, if textual, gap, no deeper issue found. |
| **ELECTROMAGNETISM** | 2-call `STEPS=2800`-vs-`4200` settling leg on `G40` (θ=39°/40°) | **ADOPT as MANDATORY**, and MODIFY to fold in VISION's complementary 1-call `2800`-vs-`1400` differential at near-zero marginal cost (both target the same real gap from different directions — see below). |
| **THERMODYNAMICS** | One idealization sentence: energy-sidecar N/A disposition | **ADOPT**, verbatim. Independently reviewed; correctly scoped as documentation-only, no deeper physics gap found. |
| **VISION SCIENCE** | 1-call `G40`-specific `2800`-vs-`1400` settling differential, scored against T27's 1%-relative REFUTE bar | **ADOPT, folded into EM's fix (MODIFY of the combined docket)** — see below. |

### EM's and VISION's settling-gap findings: independently re-verified, not both wrong for the same reason, both correct, MANDATORY

I checked the two claims against source directly, not against each
other's prose. `experiments/066-.../run.py` (Block STRESS, the
`STEPS=2800`-vs-`4200`/`5600` settling-generalization test from T27's own
closing cycle) calls `R._settle_one(("C40", ...))` exclusively —
confirmed by grep, every settling-stress cell in that file uses `"C40"`,
never `"C80"` or `"G40"`. `experiments/069-.../design_geometry.py` /
`run.py` (Block SETTLE, the companion `2800`-vs-`4200` test) targets
`CONFIGS["C80"]` exclusively (`block_settle()`'s own row key is
`C_empty_C80_4200`). So the two configs this program has ever settling-
tested at `STEPS≥2800` are: `C40` (`ABSORB=40`, thin boundary, **small**
domain, `NY=1584`) and `C80` (`ABSORB=80`, thick boundary, **large**
domain, `NY=1664`) — boundary thickness and domain size have always
co-varied in every settling check this program has ever run. `G40`
(`ABSORB=40`, thin boundary, **large** domain, `NY=1664`, sharing `C80`'s
entire domain) decouples exactly the two variables T27 never tested
independently, and its own clearances (`clear_plane` 37→77, `clear_src`
20→60) show materially more open vacuum between the leaky boundary and
the scored window than either settling anchor ever had. This is a real,
previously-uncharacterized geometric gap, independently confirmed by two
blind critiques from different angles (EM: forward-settling argument;
VISION: citation-provenance argument on where `G40` has and hasn't been
run) — not a shared blind spot, a correctly-triangulated finding.

**Verdict: MANDATORY.** Combined fix: run EM's 2-call `2800`-vs-`4200`
leg (the house-standard forward-settling test, mirroring
`experiments/069-...`'s own `block_settle` construction) **and** VISION's
1-call `2800`-vs-`1400` differential (a cheap, complementary backward
check bounding how wrong the one existing unsettled `G40` reading —
exp-065's own `Block PAD`, `STEPS=1400` — actually was) before any real
`G40` `amp_ratio` is read as decision-grade against §4's bands. Combined
marginal cost: 3 calls.

---

## Revised FDTD budget

| Item | Calls |
|---|---|
| `G40` × 31 angles × 600nm × `STEPS=2800` (original scope, unchanged) | 31 |
| `G40` settling leg: θ∈{39°,40°} × `STEPS=4200` (EM's fix) | 2 |
| `G40` settling differential: θ=39° × `STEPS=1400` (VISION's fix, folded in) | 1 |
| `G40` × 16 angles (θ∈[38°,41°]) × 750nm × `STEPS=2800` (Attack 4's fix, reusing `block_leg750`'s window) | 16 |
| **Total** | **50** |

Still cheap (~15–17 min wall-clock by the proposal's own linear-scaling
method), well inside the scope of "item 1 of 4" on the Iteration-53
queue.

---

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

The instrument itself is sound: I independently reproduced the `G40`
geometry table, the `[1b]` aliasing table, the `static_construction_
identity`-class congruence claims, and the `G0-e` recovery check
(bit-for-bit), and independently recomputed all four baseline `amp_ratio`/
`delta_P_obs` figures from the committed `results.json`. Nothing here is
HALT-grade: no mechanism is claimed (T1/constraint-3 correctly stays
disengaged), no engine change is proposed, and the core `amp_ratio`
channel (§2c's headline gating statistic) is genuinely null-free and
`R_q`-free, so R7's retirement is not literally retriggered. But two
independent, previously-uncaught defects — the falsifiable bands' own
internal gaps (Attack 1) and the `rho_pad_absorb` diagnostic's
contradiction of its own cited precedent (Attack 2) — are exactly the
class of thing that has forced a Checkpoint-4 notification in this
sub-thread's history when caught late (Iterations 49, 50, 52) rather than
now. Catching them at Phase 2, before Phase 3 freezes any language, is
this program's own established non-firing pattern — provided the docket
below actually lands before that freeze.

### Mandatory-fix docket (Director executes directly in Phase 3 synthesis)

1. Rewrite §4(a)/(b)/(c1) so every `(amp_ratio(PAIR_PAD), amp_ratio
   (PAIR_ABSORB40)) ≥ (0,0)` pair maps to exactly one named outcome —
   close the exhaustiveness gap (`x<y<0.116` and `y≥0.050`) with an
   explicit fourth band, and add a magnitude floor to (b)'s bare
   `x ≥ y` disjunct (e.g. `max(x,y) ≥ 0.050`) so a noise-level ordering
   between two point estimates with no error bars cannot alone trigger
   "re-read five iterations of prior claims" language. [Attack 1]
2. Downgrade §4(c2)'s `rho_pad_absorb ≥ 1.00` language from "real
   evidence... interaction exists" to a disclosed, explicitly uncalibrated
   magnitude signal indistinguishable from a carrier-choice artifact per
   `experiments/072-.../run.py`'s own documented disposition of the
   identical construction; correct §5 Idealization 3's "established
   `rho_c` convention" phrase to disclose `rho_c` was never evaluated on
   real data in this program's history. [Attack 2]
3. Correct §2c's "`R_i`, `R_q`... not used for any significance claim
   this cycle" to scope it precisely to the gating `amp_ratio` statistic;
   disclose `R_q`'s (uncalibrated) role in `rho_pad_absorb`. [Attack 3]
4. Add EM's 2-call `G40` `STEPS=2800`-vs-`4200` settling leg (θ=39°/40°,
   600nm) plus VISION's 1-call `2800`-vs-`1400` differential, both
   MANDATORY preconditions before any real `G40` `amp_ratio` is scored
   against §4's bands. [EM + VISION, combined]
5. Replace PHOTONICS' proposed 6-call sparse second-λ leg with a 16-call
   `G40`-at-750nm leg reusing `experiments/069-.../results.json::
   block_leg750`'s exact window (θ∈[38°,41°], 0.2° step); label it
   advisory/narrow-window in the record; state explicitly that no (a)/(b)
   verdict from this cycle may be cited forward as wavelength-general
   without a future full-width non-aliased leg. [Attack 4]
6. Fix §4(a)'s backwards "at or below `C70-C80=0.020`" gloss on the
   0.050 threshold. [Attack 5]
7. Add MATERIALS' one-sentence `ABSORB`/`PAD`-same-representational-class
   caveat, uniformly across §4(a) and §4(b). [MATERIALS]
8. Add THERMODYNAMICS' one-sentence energy-sidecar N/A disposition.
   [THERMODYNAMICS]

Revised total budget: 50 FDTD calls (up from 31), ~15–17 min wall-clock.

### Checkpoint status

None of PANEL.md's five criteria fire on this cycle as it stands after
the docket above. Criterion 1/2 do not apply (no constraint metric is
scored, no mechanism-class boundary is at issue — correctly disengaged,
§3). Criterion 3 does not apply (no engine change; reuses the validated
`Sim` bench as-is). Criterion 5 is not at risk (Iteration 52 delivered a
genuine narrowing — two REFUTEd mechanism classes, R8 adopted — and this
cycle is designed so that any of its outcomes, (a)/(b)/(c), advances the
logbook). **Criterion 4 (program-integrity drift, unfalsifiable claims) is
the live one** — Attacks 1 and 2 are exactly its shape (gapped/gameable
falsifiable bands; a physical-evidence claim contradicted by its own
cited machinery) — but per this program's own repeated ruling (most
recently exp-065/Iteration 42's own explicit language, "Phase 2 catching
defects before Phase 3 freeze is the designed mechanism working, not
failing"), it does **not** fire *provided* the docket above is applied
before Phase 3 freezes §4's language. Should Attack 1 or 2's language
survive into `phase3_synthesis.md` unaddressed and later prove
outcome-determining (matching the exact shape that fired Criterion 4 at
Iterations 49, 50, and 52), that would be a fresh, mechanically
predictable Criterion-4 firing at Phase 5 — the docket above exists
specifically to prevent that.
