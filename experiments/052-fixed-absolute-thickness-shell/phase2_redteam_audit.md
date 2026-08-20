# RED TEAM — Phase 2 Audit, Panel Iteration 29 (exp-052)

*Independently verified against the repo, not any seat's prose:
`lab/materials.py`; `experiments/030-scale-bridge/{design_geometry.py,
run.py, results.json}`; `experiments/031-ripple-core-reconciliation/
{run.py, results.json}`; `experiments/034-floor-convergence-scale-bridge/
REALIZABILITY_MEMO.md`; `PANEL.md`; `LOGBOOK.md` in full (RULED OUT, LIVE
THREADS T1–T24, Iterations 7/8/28 verbatim); `PLAN.md`'s Current-state and
LOCKED Iteration-29 entry; and the Phase-1 proposal plus all five Phase-2
critiques, verbatim.*

This is an unconditional-trigger, diagnostic/realizability cycle (T1
escape route: **None**) — the standard is whether the geometric-law claim
the cycle exists to test (does a fixed-absolute-thickness shell avoid
T14's wrong-direction shallowing?) can actually be measured cleanly by
the design as specified, not textbook-physics compliance. No constraint
(1–4) is claimed or scored this cycle, so no `constraint-#N-violation`
tag applies below — every finding is `[inconsistency]` or
`[unfalsifiable]`.

## Ruling on the five blind seats

### 1. PHOTONICS — single-λ scope undermines the program-level T14 verdict

**Verified.** `thickness_nm = 48 × 30nm = 1440nm` (bench's own dx, checked
independently at 450/600/750nm — all three convert to 30nm/cell,
confirmed in `REALIZABILITY_MEMO.md` Entry 2). `1440/450 = 3.2λ`,
`1440/600 = 2.4λ`, `1440/750 = 1.92λ` — the cited 33% swing is exact
arithmetic, not an estimate. §8's P-3 states *"the fixed-absolute-
thickness construction does NOT reproduce T14's wrong-direction
shallowing at the same strength as the self-similar family"* with no
600nm qualifier anywhere in the falsifiable-claim language, while the
whole mechanism argument (§1, §3) is explicitly about a
thickness-in-wavelengths effect — a claim whose own stated mechanism is
wavelength-dependent, tested at exactly one wavelength, and reported
without the qualifier its own physics demands.

**Ruling: REAL, LOAD-BEARING.** This is the same class of gap PANEL.md's
own metrics table exists to prevent ("Wavelength... dependence: witness
realism"), and it is a scope claim, not a measurement error — cheap to
fix either by adding one run or by re-wording P-3.

### 2. MATERIALS — §9 checks thickness only, never absorptivity

**Verified.** Grepped `REALIZABILITY_MEMO.md` in full for any
absorption-coefficient, penetration-depth, or optical-density figure tied
to a real CNT-forest/Vantablack citation: **none exists anywhere in the
memo.** Both cited ranges ("few-µm to sub-mm", "tens of nm to ~1mm") are
thickness precedents only (lines 442, 480) — §9's own "1.44µm sits inside
[both cited] ranges" comparison is therefore checking the one quantity
this program has a citation for and silently passing over the one it
doesn't. Independently computed the implied absorption length from the
proposal's own numbers: `τ_shell/thickness_nm = 24/1440nm ≈ 0.0167/nm`,
e-folding length **≈60nm** — MATERIALS' figure reproduces to the digit.

**Ruling: REAL, LOAD-BEARING.** Not a refutation (no real-material α
figure exists in this program to compare against — T18's WebFetch block
is still the root cause), but §9's "PLAUSIBLE, not PUBLISHED" language
currently rests on half the claim it needs to license, and MATERIALS
correctly scoped the fix as optional-but-verdict-moving (their own
critique states this could flip to oppose on the realizability language
specifically if unresolved).

### 3. ELECTROMAGNETISM — the reused construction is HOLLOW, the exact defect exp-031 fixed for a different experiment

**Verified directly in code, and it is worse than "unaddressed."**
`experiments/030-scale-bridge/run.py::build_ambient`'s `"absorber"`
branch:
```
elif article == "absorber":
    mat.graded_black_shell(sim, cx, cy, dg.r_in_shell(r), r, ...)
```
No `pec_disk` call, no fill of any kind for `rr < r_in` — confirmed by
direct grep and read of `lab/materials.py::graded_black_shell`, which
writes only into `shell = (rr>=r_in)&(rr<=r_out)` and never touches the
interior. `experiments/031-ripple-core-reconciliation/run.py::build_scene`
explicitly fixes this for its **own** θ=0 diagnostic (`mat.pec_disk(sim,
cx, cy, r_in)` immediately before `graded_black_shell`, with a code
comment naming exp-030's convention as historically wrong), but that fix
was never applied back to `experiments/030-scale-bridge`'s own committed
`results.json` — which is exactly the file exp-052's §8 P-1/P-2 comparator
values (`C_selfsim(156)=−0.730455`, `C_selfsim(312)=−0.732254`) are drawn
from. §2a's reuse language ("domain-construction rule... unchanged from
exp-030") never states which core-fill convention the new object itself
will use, and P-0's own gate — "reproduce exp-030's committed r=78 object
exactly (bit-identical `graded_black_shell` call)" — commits, by its own
literal wording, to reproducing the **hollow** construction, since that
is what exp-030 actually built.

Independently verified EM's r_in/r_out arithmetic: `108/156 = 0.6923`,
`264/312 = 0.8462` — matches EM's "≈0.69–0.85" exactly, versus T9's own
established null (Δσ_abs/σ_ext=1.56×10⁻⁶) measured at `30/78 = 0.3846`.
Note also, independently: because the **self-similar** family holds
`r_in/r_out` fixed at exactly 0.3846 at *every* r by construction, T9's
null actually does generalize across the self-similar family's own r=78/
156/312 — a fact worth stating precisely, because it sharpens rather than
softens EM's point: T9's null has never been tested at any ratio above
0.385, in either family, and exp-052 is the first proposal in this
program's history to build an object above that ratio at all.

**Ruling: REAL, LOAD-BEARING, and the single most consequential defect in
this cycle** — structurally identical in kind to the Iteration-8 Red Team
catch that redirected an entire cycle (same missing-`pec_disk` defect, same
`graded_black_shell` article, one cycle removed from where it was first
fixed and silently not propagated).

### 4. QUANTUM OPTICS — the coherent-vs-incoherent bridge gate was only ever validated at the self-similar r=78 geometry

**Verified.** `lab/ambient.py`'s N9 incoherent sum is the scoring
instrument for every `C` value this cycle produces (§2c). The only
empirical license for treating that sum as valid is exp-029's stage-11
bridge gate (`+0.0224%` aggregate cross-term, `5.02×` local bin-wise,
confirmed against LOGBOOK's own T1 entry), run once, on a shell whose
thickness was 61.5% of `r_out` — which is *exactly* the fixed-absolute
family's own r=78 shell fraction (`48/78=0.615`), since fixed-absolute and
self-similar coincide there by construction (P-0). But exp-052's own
mandatory scored result is at r=156, where the fixed shell is now only
`48/156=30.8%` of `r_out` — a thinner, more strongly rim-diffracting
regime the bridge gate has never touched. §5 explicitly re-verifies only
the flat-coating R-gate and is silent on the coherence assumption.

**Ruling: REAL, LOAD-BEARING** — an inherited assumption whose own
validated precondition (shell-to-radius ratio) has moved 2× at the exact
geometry the proposal's primary falsifiable result is scored at.

### 5. VISION SCIENCE — P-2's r=312 band is comparable to a known, uncharacterized instrument budget, and r=312 has no quadrature check at all

**Verified.** T16's own measured figure (LOGBOOK, Iteration 11/12):
**7.80×10⁻⁴** total angular-quadrature+domain-construction swing at r=156,
non-monotonic in r_out (worse at r=78-native than r=156). P-2's REFUTED/
CONFIRMED threshold is **0.0010** — a ratio of 1.28×, "comparable to, not
negligible against" is an accurate characterization, not an overstatement.
One caveat worth stating precisely, since it cuts both ways: T16's figure
was measured on the near-null σ(I) OFF-state sponge (|C|≈0.005), not on a
deep-shadow opaque absorber (|C|≈0.73) — whether the *same* absolute
angular-sampling uncertainty transfers to a saturated silhouette has never
been independently measured either, which is if anything a second,
compounding gap (nobody has ever characterized N9-quadrature sensitivity
for the opaque-article class at all), not a reason to discount VISION's
concern.

**Ruling: REAL, LOAD-BEARING** for the r=312 leg specifically (§7's own
cost-gating already treats r=312 as more contingent than r=156, so this
tightens an already-soft leg); the r=156 P-1 margin (0.0046, ~6× the T16
budget) is comparatively safe, as VISION's own critique states.

## New attacks — caught by none of the five blind seats

### 6. [inconsistency] The comparator baseline itself is uncorrected — and, separately, one of its cited figures does not match its own cited source

Two distinct problems, both new:

**(a) The established self-similar comparators cited in §8 — the very
numbers P-1/P-2's falsifiable bands are scored against — are themselves
the HOLLOW-core, never-corrected N9-ambient values from Attack 3, above.**
exp-031's PEC-core correction (P-DIR-1: negligible, 6.8×10⁻⁶) was measured
**only** as a single-angle (θ=0) diagnostic, at r=78 and r=156, and never
propagated into a re-run of the full 9-angle ambient sum that actually
produces the `C156`/`C312` figures exp-052 cites. This matters at exactly
the ratios (0.385→0.692) T9's own null has never been checked at, and
specifically at the grazing angles (±25°, ±35°) a boresight-only check
cannot speak to. Whichever core convention Phase 3 adopts for the *new*
object (fix per Attack 3), the *comparator* on the other side of every
P-1/P-2 delta carries this same unresolved question, unquantified at the
instrument that is actually scored.

**(b) A transcription error, independently verified against
`results.json`:** §8 states *"Established self-similar comparators
(`experiments/030-scale-bridge/results.json::fit.absorber`, 600nm-only raw
table): `C_selfsim(78)=−0.7211`..."* — the actual value at that exact path
is `C78_established = -0.7208684660449545` (rounds to **−0.7209**, not
−0.7211). The proposal's own derived figure, `|ΔC_selfsim(78→156)| =
0.00936`, is internally consistent with the *wrong* −0.7211
(`|−0.730455−(−0.7211)| = 0.009355`) rather than with the actually-cited
source (`|−0.730455−(−0.7208684660449545)| = 0.009587`). This is
non-load-bearing to the actual scored gate — P-1's CONFIRMED/PARTIAL/
REFUTED cutoffs (−0.7350/−0.7305) are hard-coded against `C_selfsim(156)`
directly, which is correctly transcribed — but it is exactly the pattern
**R4** (this program's own standing house rule, adopted Iteration 25 after
three consecutive recurrences) exists to catch: a figure cited as coming
from a specific committed path that does not actually reproduce from
invoking that path.

**Ruling: (a) REAL, LOAD-BEARING** (compounds Attack 3 — fixing the new
object's core convention alone does not close this, since the comparator
side needs its own disposition, stated explicitly, not assumed clean by
omission). **(b) REAL, COSMETIC to the scored gate, but must be corrected
before predictions freeze** — per R4, hand-verify every cited figure
against the actual file before commit, not by re-deriving from a
possibly-transcribed intermediate.

### 7. [inconsistency] §5's "mandatory" R-gate re-verification cannot detect the defect it is being asked to stand in for

Verified in code: `coated_wall_r_gate()` (`experiments/030-scale-bridge/
run.py`) builds a **flat semi-infinite wall**, PEC-backed at the taper's
far edge, illuminated at normal incidence — it never constructs the
annular disk geometry, never has an `r_in`/core-fill choice to make, and
is structurally blind to rim/tangential/near-field-cavity physics by
design (this is the same distinction PHOTONICS' own Iteration-7 Phase-5
finding already established: *"The R-gate never tests the TANGENTIAL
rim-transmission geometry... that governs the ambient C metric"*). A
clean P-4 pass (`R_coat(156) ≤ 0.002`) — which is very likely, since the
coating profile itself is bit-identical to the already-gated r=78 object
— provides **zero** evidence bearing on Attack 3/6's hollow-core or
comparator-mismatch questions, but §5 lists it as the cycle's one
"mandatory, re-verified" gate, which risks reading a clean P-4 as
reassurance about a question it cannot see.

**Ruling: REAL, COSMETIC-BUT-MUST-BE-STATED** — not a defect in the gate
itself (it does what it has always done), but the proposal's own framing
should not let P-4's pass be read as bearing on Attacks 3/6.

### 8. [unfalsifiable] P-5's THERMO sidecar prediction carries near-zero information

Every UNDETECTABLE THERMO-sidecar verdict this program has ever issued
(exp-043/044/045, multiple hosts, multiple rate constants, multiple
geometries) cleared its NETD comparator by **>100×**, several by many
orders of magnitude more. This construction changes only the object's
`r_in`/core geometry at fixed shell thickness and fixed, already-tiny
source irradiance (~6.58×10⁻⁶ W/cm², Docket #7) — nothing plausibly closes
even one order of magnitude, let alone the 10× P-5 needs to fail. Compounds
Attack 2: the sidecar's own input (the established `σ_abs/σ_ext=0.51`
ratio) is explicitly flagged in idealization 4 as unverified for this
geometry, so even the "input" side of this calculation is imported from a
different regime, further widening rather than narrowing the margin.

**Ruling: REAL, MINOR.** Already correctly labeled analytic/non-primary
per PANEL.md's THERMO expressibility contract, so this is not a
structural problem — but P-5 should be reported as an expected, low-
information confirmation (per Iteration-8's own precedent for PEC's
near-certain dual-law convergence), not presented as a genuine test of
anything this cycle is actually uncertain about.

## Overall verdict: **PROCEED-WITH-MANDATORY-FIXES**

Consistent with this program's own standing pattern (Iterations 7, 8, and
every other diagnostic/realizability cycle to date): none of the eight
findings above are irreconcilable with running this cycle. The most
serious (Attack 3/6a, the hollow-core inheritance and its uncorrected
comparator) is a **construction choice that must be made explicitly and
disclosed**, not a redesign — and this program has the exact fix on the
shelf (`experiments/031-ripple-core-reconciliation/run.py::build_scene`'s
own PEC-cored idiom). Given the unconditional-trigger status of this
build (PLAN.md: *"not contingent on... findings, not subject to a further
ranked-list competition"*), a REJECT verdict would functionally re-defer a
21-iteration-overdue commitment over defects fixable in an afternoon —
exactly the situation Red Team declined to escalate past
proceed-with-mandatory-fixes at both Iteration 7 and Iteration 8, for the
same reason.

## Must land before predictions frozen — prioritized docket

1. **[Attack 3, load-bearing]** Pin the core-fill convention explicitly
   and in code — adopt the historically-correct, exp-031-precedented
   PEC-cored construction (`pec_disk(r_in)` then `graded_black_shell`),
   since P-0's own literal wording otherwise commits by default to
   reproducing exp-030's hollow construction. State the choice as a named
   design decision in §1/§3, not an inherited silence.
2. **[Attack 6a, load-bearing]** State explicitly, in the same place, that
   the self-similar comparator values (`C_selfsim(156/312)`) are HOLLOW-
   core and uncorrected at the N9-ambient level (only θ=0-verified
   negligible, at r=78/156 only) — either accept this as a disclosed,
   bounded idealization (T9's θ=0 check gives a plausible-but-unproven
   upper bound) or add the cheap fix below (item 3) to close it on both
   sides of the comparison at once.
3. **[Attack 3 flip, moderate cost]** One radial absorbed-power ledger
   check (reusing exp-028's already-validated instrument) at r=156 or
   r=312, confirming Δσ_abs/σ_ext stays negligible at r_in/r_out≈0.69–0.85
   — not merely extrapolated from the single r_in/r_out=0.385 point T9
   actually measured. If cheap enough, extend this to a full N9-ambient
   PEC-cored rerun of the self-similar comparator at r=156, closing item 2
   completely rather than leaving it as a bounded idealization.
4. **[Attack 6b, must fix, cheap]** Correct §8's `C_selfsim(78)` citation
   to the actual `results.json` value (−0.7208684660449545, not −0.7211)
   and recompute the "1.5× the established step" narrative in code from
   the corrected figure, per house rule R4 — does not move any scored
   threshold, but must not ship uncorrected.
5. **[PHOTONICS, moderate]** Either add one confirmatory run at 450nm or
   750nm (r=156 only, cheap relative to the mandatory block) or explicitly
   scope §8's P-3 language to 600nm-only, striking the implied
   program-level T14 resolution.
6. **[MATERIALS, moderate]** Add the implied absorption coefficient
   (`α = τ_shell/thickness ≈ 60nm e-folding`) to §9 and check it against
   whatever CNT-forest optical-density figure this program can source (or
   explicitly narrow the PLAUSIBLE claim to "thickness-only, absorptivity
   unchecked, pending T18") — do not let §9 read as a two-sided
   realizability check when it is currently one-sided.
7. **[QUANTUM, moderate]** Rerun the stage-11 coherent-vs-incoherent bridge
   gate (existing machinery, no new code) at r=156 on the fixed-absolute
   object before P-1 is trusted as licensing the incoherent-sum `C` at a
   shell fraction (30.8%) the gate has never validated.
8. **[VISION, moderate, r=312-only]** Either widen P-2's REFUTED/CONFIRMED
   bands to ≥2× T16's measured r=156 budget (~0.0016) or run one cheap
   per-angle ±40° empty-scene floor spot-check at r=312 before treating
   P-2 as a clean CONFIRMED/REFUTED call rather than PLAUSIBLE-but-
   uncharacterized.
9. **[Attack 7, disclosure-only, cheap]** State explicitly that a clean R-
   gate pass (P-4) bears on flat-wall normal-incidence reflectance only
   and gives no evidence about items 1–3 above — do not let P-4 CONFIRMED
   be read as closing the core-fill question.

**Recommended, not blocking:** relabel P-5 as an expected, low-information
confirmation (item 8, Attack list) rather than a genuine falsifiable test,
consistent with every prior THERMO sidecar citation's >100× margin.

**Evidence that would change this verdict:** toward REJECT — if adopting
the PEC-cored construction (item 1) or the radial-ledger check (item 3)
shows Δσ_abs/σ_ext is no longer negligible at r_in/r_out≥0.69 (i.e., T9's
null does not survive past 0.385), the entire P-1/P-2 comparison would
need to be redesigned, not merely corrected. Toward clean PROCEED — items
1, 2, 4, and 9 landed (cheap, mechanical); items 3, 5, 6, 7, 8 either
resolved or explicitly scoped as this cycle's own stated limitation, the
same standard this program applied at Iterations 7 and 8.
