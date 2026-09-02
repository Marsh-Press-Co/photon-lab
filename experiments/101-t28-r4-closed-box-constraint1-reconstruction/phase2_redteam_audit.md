# Phase-2 Red Team Audit — Panel Iteration 78 (exp-101)

Fresh seat, full packet received (proposal + all five Phase-2 critiques — no
other seat saw this). Every load-bearing numeric/code claim below was
independently re-derived from source this session (scripts run against the
actual committed files, not against any seat's restated numbers), per this
seat's own charter ("standard is NOT textbook-physics compliance"; kills
inconsistency, unfalsifiability, inexpressibility, and quiet constraint
violations — especially #3). T1 route is N/A this cycle by the proposal's
own §3 and independently confirmed true (no σ(I)/σ(x,t)/angular-selectivity/
sub-threshold parameter is touched); consequently, as flagged in the
brief, almost every attack below is a house-discipline/methodology attack,
not a constraint-#N attack. That is the correct shape for an instrument-
fidelity cycle, not evidence of a soft audit.

---

## 1. Numbered attacks (independently verified)

**1. [inconsistency] The proposal's stated warrant for the `back_frac`/
`fwd_frac` downstream/sourceward relabeling is false.**
Verification: read `experiments/087-t28-energy-interception-cross-check/
run.py:123-168` in full. `widths_direction_corrected()` computes
`s = 1.0 if w["i_inc"]>=0 else -1.0`, builds `out = dict(w)`, and multiplies
**only** `sigma_scat`, `sigma_abs`, `sigma_ext`, `sigma_ext_cross` by `s`
(explicit `for key in (...)` loop naming exactly those four keys) before
setting `out["i_inc"] = abs(w["i_inc"])`. `back_frac`/`fwd_frac` are never
in that loop — they survive from the `dict(w)` copy untouched, and their
own formula in `lab/sections.py::widths()` (`max(p_back,0)/max(p_scat,
1e-30)`) never references `i_inc` at all, so there is nothing for a sign
flip to touch. §2.5/§5's claim that this is "the same reinterpretation
already established for `sigma_scat/abs/ext` (`widths_direction_
corrected`)" is a citation of a function that provably does not do what is
claimed of it. EM caught this; I independently reproduced it by reading the
same 46 lines cold, byte for byte, before reading EM's critique text again.
Confirmed exactly.

**2. [inconsistency] The proposal's own §6 self-clearance of R13/R14/R15
is wrong on its own terms — it cites an anti-division-by-zero epsilon as
if it satisfies R13's actual, stricter, already-adopted standard.**
`back_frac`/`fwd_frac` share one denominator, `max(p_scat, 1e-30)`
(`lab/sections.py::widths()`). §6 states this "is already floor-gated by
construction (clamped away from a literal zero)." I read R13's full text
(`LOGBOOK.md` lines 410-460, verbatim): the rule requires a floor gate "on
that quantity's own absolute or amplitude-normalized magnitude — not
merely on the numerator's own measurement-noise floor," with a failing
angle reported as `UNRESOLVED-BY-CONSTRUCTION`/`NODE-UNRESOLVABLE`, never
silently scored. A `1e-30` epsilon guards against literal division by zero,
not against `p_scat` being small-but-nonzero relative to this box's own
measurement noise — a categorically different bar than R13 sets, and the
gap matters here specifically: four of the six `LEG_B_ANGLES`
(37.127246°, 38.590230°, 40.265420°, 41.460901°) are cpl20-native
zero-crossings of `delta_scene`, a genuinely oscillatory, independently-
established (exp-083) confound curve — precisely R13's founding-case shape
(a ratio built near a known zero-crossing of a *related* oscillatory
quantity). Whether `p_scat` itself dips near zero at those four angles is
not established anywhere I could find in the repo (checked
`experiments/095-*/results.json`, `098-*/results.json`, `099-*/
results.json` for a stored raw `p_scat`/`sigma_scat` field — none is
persisted, only the already-normalized ratios). EM's attack independently
converges on the same denominator (their "unlucky cell with small/negative
raw `p_scat`" scenario) without naming R13 by number; tying it to R13
explicitly shows this is not a stylistic nicety but a standing rule this
proposal currently fails to actually satisfy, despite claiming otherwise.

**3. [inconsistency] `exp-100`'s own upstream `pool_rows()` pool — the
same machinery every seat (and this proposal) used to re-derive the angle
selection and the R3-vs-R4 correlation asymmetry — contains undisclosed
duplicate rows that are not independent measurements, and this materially
changes the significance of the "family_contradiction" finding PHOTONICS'
attack leans on.** Verified by executing `pool_rows()` directly
(`experiments/100-.../run.py`) and inspecting `(family, theta)` keys: the
R3 family's stated `n=33` contains only **21 unique θ values** (12
byte-identical duplicate rows — 36% of the R3 pool — where 092/093 and
094/095/098/099's own `POOL_TABLE` citation chains re-list the same
underlying stored result under a later experiment's own report key); the
R4 family's stated `n=35` contains only **29 unique θ values** (6
duplicate rows: 38.49°/38.69° shared between 095 and 098; 40.960901°/
41.294201°/41.627601°/41.960901° shared between 098 and 099). Re-running
the module's own `permutation_test()` function on the deduplicated rows:

| family | n (as pooled) | r (pooled) | p (pooled) | n (unique θ) | r (dedup) | p (dedup) |
|---|---|---|---|---|---|---|
| R3 | 33 | 0.4862 | 0.00415 (**significant**) | 21 | 0.3596 | 0.1073 (**not significant**) |
| R4 | 35 | 0.1103 | 0.5249 | 29 | 0.1884 | 0.3269 |

The R3-vs-R4 asymmetry PHOTONICS cites verbatim ("a real, significant
coupling at R3 (r=0.486, p=0.0042)") does not survive an elementary
independence check on `pool_rows()`'s own input rows — a third of R3's
"n=33" is not 33 independent FDTD measurements, it is ~21 measurements
counted 1.57× on average via citation republishing. This is genuinely new;
none of the five critiques flagged it, and I found it only by checking the
duplication hypothesis after independently reproducing PHOTONICS' cited
figures exactly (`r=0.1102867…`, `p=0.5249`, confirmed byte for byte
against `experiments/100-.../results.json`'s `tier1_item1.by_family.R4`).
**Consequence for this cycle, scoped honestly**: neither of exp-101's own
selected extremal angles (39.200000°, 42.960901°) is among the duplicated
rows, so Tier 0's actual deliverable (the angle set, the box
reconstruction) is unaffected. But PHOTONICS' own disclosure-sentence fix
("no established correlation... r=0.110, p=0.525") is *necessary but now
insufficient* — carrying forward "a real, significant coupling at R3" as a
settled contrast, without the caveat that this contrast itself halves in
magnitude and loses significance under a one-line dedup fix, would create
a fresh, avoidable citation defect of exactly the kind R20 exists to catch,
this time originating in exp-100's own machinery rather than exp-101's.

**4. [not applicable, house-discipline/methodology attack] The proposal's
own reassurance that "Gate 1 (vacuum-footprint precondition)... already
passed in exp-094 — reused, not rerun" does not answer QUANTUM's
box-margin attack, because Gate 1 certifies a different and weaker
property.** Read `lab/fdtd2d.py::_damping()` in full:
`d = np.zeros(...)`; the ramp is written only into `d[:absorb,:]`/
`d[-absorb:,:]`/`d[:,:absorb]`/`d[:,-absorb:]`; everywhere outside those
four bands `d` stays exactly `0.0`, so `damp_e = exp(-0.30*d) == 1.0`
*exactly*, by construction, for any cell with `x >= absorb` (and the
mirror conditions on the other three edges) — there is no partial-damping
penumbra beyond the literal `absorb`-cell band. Gate 1's `all_vacuum`
check (confirmed directly in `experiments/094-.../results.json`:
`gates.gate1_vacuum_footprint_r4.report.C40_R4.BOX_B.all_vacuum == true`,
box `[136,544,1380,1788]`) therefore passes **trivially** for any box
whose footprint sits at `x0 >= 80` — it cannot distinguish a
comfortably-margined box from one sitting 1 cell outside the ramp, because
`damp_e` is binary (exactly 1.0 or genuinely ramped) at this resolution.
Exp-003's own documented failure mode (box_dev 2-6 at a 19-cell margin) is
a *near-field proximity* effect on the flux measurement itself, not a
"nonzero `damp_e` leaked into the box" effect — the two are different
claims, and Gate 1 tests only the second, which is not in dispute. Citing
"Gate 1 already passed" as reassurance against QUANTUM's margin concern is
therefore non-responsive, not merely redundant; nobody among the five
critiques (including QUANTUM, whose attack this reinforces) named this
specific conflation.

**5. [not applicable, house-discipline/methodology attack — R17] Confirmed
independently: `C40_R4`'s `BOX_B` sits 56 cells from the absorb layer's
inner edge, below exp-003's own empirically-established ≥60-cell
threshold, and the proposal's reused `XI_TOL=0.12` bound was never checked
against that larger, on-file precedent.** Recomputed from source, not
QUANTUM's restated numbers: `R4_R_OUT=156`, `BOX_CLEARANCE_B_R4=48`
(`experiments/069-.../design_geometry.py:257,295`) →
`r=204`; `R4_BASE_OBJ_X=340`, `pad=0` for `C40_R4` → `obj_x=340`;
`box_for_r4` gives `x0 = 340-204 = 136`. `R4_BASE_ABSORB=80`
(`design_geometry.py:232`), and `lab/fdtd2d.py`'s absorb ramp is applied
identically on all four edges with the interior beginning at the absolute
cell index `self.absorb` regardless of `pad` (confirmed by reading
`_damping()`, attack 4 above) → margin `= 136 - 80 = 56` cells. For
`G40_R4` (`pad=80`): `obj_x=420`, `x0=420-204=216`, margin `=216-80=136`
cells — comfortably above threshold, matching QUANTUM's claim exactly.
`BOX_A` for `C40_R4`: `r=156+24=180`, `x0=340-180=160`, margin `=80`
cells — also safe, matching QUANTUM's claim. Independently confirmed
`experiments/003-broadband-wall/NOTES.md` and `run.py`: the domain fix
there (`N` 560→680, explicit `margin_x`/`margin_y >= 60` assertion,
`ABSORB=40` in that experiment) followed a measured `box_dev` of 2-6
(200-600%) at a 19-cell margin — real, on file, and, since R4's absorb
depth (`80`) is double exp-003's (`40`), QUANTUM's inference that the true
required margin here is "likely larger" than 60 is a reasonable,
explicitly-hedged extrapolation, not an overclaim — I did not find an R4-
specific empirical margin-vs-box_dev curve on file to pin the true
threshold more precisely, so "likely larger, unverified" is the accurate
epistemic state, not "verified equal to exp-003's 60."

**6. [not applicable, house-discipline/methodology attack — R21] Confirmed
independently: this cycle's own committed pipeline will regenerate
`p_abs_w`/`dt_ss_full_K`/`netd_classification` for all 12 (θ, config)
cells via `cell_metrics_r4`, and §6's R16/R21 compliance paragraph commits
to Result-section narration for `sigma_scat_downstream` only.** Read
`experiments/094-.../run.py:305-352` in full: `cell_metrics_r4()`
unconditionally builds a `thermo` dict carrying `p_abs_w`, `dt_ss_full_K`,
`netd_classification` for every call. Grepped the full proposal text for
these three field names: `p_abs_w` appears exactly once, in the §2.5 field
table, labeled "reused, unchanged" — not in §4 (predictions) or §6
(R16/R21 compliance); `dt_ss_full_K` and `netd_classification` appear
**zero** times anywhere in the document. Read `LOGBOOK.md` lines 845-871
(R21's full text) verbatim: it names exactly two founding instances on
this identical NETD/thermal-sidecar channel — Iteration 76/exp-099 and
Iteration 77/exp-100 — and states a **third** occurrence "fires Checkpoint
criterion 4 automatically, no further deliberation." Four of the six
`LEG_B_ANGLES` (the cpl20 crossings) have never been run through the R4
thermo sidecar before, so this is not a re-derivation of already-narrated
numbers — it is fresh R21-shaped surface area with, currently, zero
written commitment to narrate it. THERMODYNAMICS' attack is exactly
right and is the single highest-severity finding in this packet, because
R21's forward-elevating clause is unconditional and automatic (unlike
R16's more forgiving "known/named/ignored" bar) — there is no seat-level
discretion once a third occurrence lands.

**7. [not applicable, house-discipline/methodology attack] MATERIALS'
finding is confirmed verbatim: T9's own disclaimer is being dropped where
Prediction 1's [0.505, 0.520] band cites "the T9 anchor (0.51)."** Read
`LOGBOOK.md` lines 1161-1169 verbatim: "**both EXCEED the idealized
geometric-optics ceiling (σ_abs/σ_ext ≤ 0.5, a Babinet/shadow-formation
bound for any perfectly-black object, independent of interior
structure)**... **neither number is an asymptotic material constant**,"
attributed to the box sitting in the near/Rayleigh zone (T8). Grepped the
full proposal: Prediction 1 cites "the T9 anchor (0.51...)" with zero
restatement of this disclaimer, and independently re-verified the cited
[0.5121, 0.5149] R4-pool band (`ratio_abs_ext_raw_c`, n=35) matches exactly
by re-running `pool_rows()` myself, and the exp-087 oblique reconfirmation
figures (0.5128-0.5138, i.e. min 0.512765…, max 0.513812… — confirmed
directly against `experiments/087-.../results.json`) are accurately
transcribed.

---

## 2. Disposition of each of the five critiques' own findings

**PHOTONICS** — sharpest attack (R4-pool-extremal angles carry no
established correlation to article optical engagement; r=0.1103,
p=0.5249). **PARTIALLY CONFIRM.** The cited R4 statistic is exact (I
reproduced `r=0.1102867…`, `p=0.5249` byte for byte from
`experiments/100-.../results.json`). But the comparator PHOTONICS leans on
for contrast — "a real, significant coupling at R3 (r=0.486, p=0.0042)" —
is itself confirmed-as-stated yet **not robust**: it is built on 33 pooled
rows of which only 21 are unique, independent measurements (attack #3
above), and the correlation loses significance (p=0.107) once deduplicated.
The core recommendation (disclose that the two chosen angles carry no
established R4-optical-engagement warrant, report violations there as
instrument-behavior data pending Tier 1) still stands and should be
adopted — but the specific "versus a real, significant coupling at R3"
framing must not be carried into NOTES.md/Result prose without the dedup
caveat, or it manufactures a new, avoidable citation defect.

**MATERIALS** — sharpest attack (Prediction 1's band silently drops T9's
disclaimer). **CONFIRM**, no correction. Independently re-derived from
`LOGBOOK.md` line 1161 verbatim (above) and from the proposal's own text
(grep confirms zero restatement of the disclaimer). The proposed fix (carry
T9's own sentence forward wherever the band is stated) is correctly scoped
and sufficient.

**ELECTROMAGNETISM** — sharpest attack (false citation of
`widths_direction_corrected` as precedent for the `back_frac`/`fwd_frac`
relabeling; missing per-cell floor on the shared `p_scat` denominator).
**CONFIRM, and extend.** Independently re-derived the false-citation
finding from the raw 46-line function body (attack #1), and independently
confirmed the missing-floor concern is not merely good practice but a
failure to meet the already-adopted, numbered standing rule R13 as
written, given the epsilon (`1e-30`) EM correctly identifies is an
anti-division-by-zero guard, not R13's required noise/amplitude floor
(attack #2). EM's own critique does not name R13 by number; I add that
connection, which raises this from "a proportionate due-diligence
suggestion" to "a currently-failing compliance obligation."

**THERMODYNAMICS** — sharpest attack (R21 third-strike risk on
`p_abs_w`/`dt_ss_full_K`/`netd_classification`, unaddressed in §6).
**CONFIRM**, no correction, and I elevate its priority. Independently
re-derived from `cell_metrics_r4`'s source (unconditional computation),
the proposal's own text (grep: zero mentions of the two NETD fields
outside one "reused, unchanged" table row), and R21's own LOGBOOK text
(automatic, no-deliberation firing on a third occurrence, with the first
two instances named explicitly and matching this exact channel). This is
the single most severe finding across the whole packet, because the
consequence (an automatic Checkpoint 4) is not a judgment call for a
future reviewer to make — it is pre-committed by standing rule.

**QUANTUM OPTICS** — sharpest attack (`BOX_B`'s clearance from the absorb
boundary for `C40_R4` is 56 cells, below exp-003's ≥60-cell precedent, an
R17 violation in reusing `XI_TOL` unchecked against it). **CONFIRM**, no
correction. Independently recomputed the full arithmetic chain from raw
constants (`R4_R_OUT`, `BOX_CLEARANCE_B_R4`, `R4_BASE_OBJ_X`,
`R4_BASE_ABSORB`, and `lab/fdtd2d.py`'s actual ramp placement) rather than
trusting the stated "56 cells," and got 56 cells exactly, plus 136 cells
for `G40_R4` and 80 cells for `C40_R4`'s `BOX_A`, both also matching
QUANTUM's own numbers exactly. Independently confirmed the exp-003
precedent (box_dev 2-6 at a 19-cell margin, `ABSORB=40`, fixed by an
explicit ≥60-cell assertion) by reading that experiment's own `NOTES.md`
and `run.py`. I additionally show (attack #4) that the proposal's own
"Gate 1 already passed" language cannot be read as rebutting this concern,
since Gate 1 tests a provably different, structurally weaker property.

---

## 3. Ruling

**PROCEED-WITH-MANDATORY-FIXES.** The Tier-0 core deliverable — the
closed four-face Poynting-box reconstruction of `beam_behind_t28` via
already-gated `sc.widths()`/`box_for_r4`/`ref_for_r4`, and the corrected
6-angle `LEG_B_ANGLES` set — is sound, correctly scoped, T1-N/A as
claimed, and does not quietly touch constraint 3 (verified: no ambient/
silhouette claim, no `C_thr` comparison, appears anywhere in the document;
the Idealizations section explicitly and correctly disclaims this). No
finding above threatens the angle selection or the box-reconstruction
mechanics themselves. The fixes below are mandatory before Phase 3 freezes
and/or before Phase 4 runs, each traceable to a specific attack/critique:

1. **Add a real noise/amplitude floor gate on `p_scat`** (not merely the
   existing `1e-30` anti-division-by-zero epsilon) before `back_frac`/
   `fwd_frac` are trusted at any angle, with a failing cell reported as
   `UNRESOLVED-BY-CONSTRUCTION` per R13's own prescribed remedy — not
   silently scored against Predictions #2/#3. Correct §6's R13/14/15
   self-clearance, which currently over-claims compliance. *(Attacks #1,
   #2; EM's critique.)*

2. **Replace the false `widths_direction_corrected` citation** in §2.5/§5
   with the actual warrant (`_face_flux`'s Sx-face correspondence +
   `plane_x_behind`'s low-x="downstream" convention, cross-checked against
   `observer_record_t28` alone) before Phase 3 freezes. *(Attack #1; EM's
   critique.)*

3. **Add an explicit, code-enforced-assert-backed Phase-3 NOTES.md
   commitment** binding all 12 fresh `netd_row()`-shaped outputs
   (`p_abs_w`, `dt_ss_full_K`, `netd_classification`, all 6 angles × 2
   configs) to inline Result-section narration, not merely persistence —
   before Phase 4 runs. This is the highest-priority fix in this packet:
   its omission is not a stylistic risk but an automatic, no-deliberation
   Checkpoint-4 trigger per R21's own text if the third occurrence lands.
   *(Attack #6; THERMODYNAMICS' critique.)*

4. **Widen `C40_R4`'s effective `BOX_B` margin to ≥90-100 cells** (grow
   that config's padding for this QA check only, or widen
   `BOX_CLEARANCE_B_R4` for `C40_R4` specifically) to clear exp-003's
   established ≥60-cell threshold with the same margin `G40_R4` already
   has (136 cells), **and** pre-register in writing that a
   `box_dev_scat_downstream` failure at an under-margined box is read as a
   domain-sizing artifact (exp-003 precedent), not a `back_frac`-fragility
   finding — before Phase 4 runs. *(Attack #5; QUANTUM's critique.)*

5. **Add PHOTONICS' proposed disclosure sentence, corrected**: state that
   the R3-vs-R4 "coupling asymmetry" itself (not just the R4 figure in
   isolation) is a fragile statistic — `pool_rows()`'s own R3 pool contains
   12 duplicate (non-independent) rows out of 33, and the significant-
   looking `r=0.486, p=0.0042` becomes `r=0.360, p=0.107` (not significant)
   once deduplicated. Do not carry "a real, significant coupling at R3"
   into Result/Learned prose as settled without this caveat. This does not
   block Tier 0 execution (neither selected angle is a duplicated row) but
   must be disclosed to avoid seeding a fresh R20-shaped citation defect
   downstream, in exp-100's own machinery. *(Attack #3 — this seat's own
   finding, extending PHOTONICS' critique.)*

6. **Carry T9's disclaimer verbatim** wherever the `[0.505, 0.520]` band
   or the bare "0.51" figure is stated in Result prose: this ratio exceeds
   the Babinet/shadow-formation ≤0.5 ceiling and is a near-field
   box-geometry artifact (T8), not an asymptotic material absorptivity
   constant. *(Attack #7; MATERIALS' critique.)*

None of these fixes require re-running Tier 0's FDTD calls or changing the
angle set, box geometry, or call budget — they are pre-registration/
labeling/gating fixes to make before Phase 3 freezes (1, 2, 5, 6) or before
Phase 4 executes (3, 4), consistent with this cycle's own zero-`lab/`-diff,
zero-new-mechanism scope.

---

## 4. Standing house-rule risk (Checkpoint criterion 4)

- **R4** — not at risk. Every cited "precisely recomputed" figure in the
  proposal (the angle ranks, the `ratio_abs_ext_raw` band, `SIGMA_R4_
  CORRECTED`) was independently re-executed by me this session against the
  actual committed source and matched to the digit.
- **R9** — not at risk. `ratio_abs_ext_raw` and the T9 anchor are
  confirmed commensurable: both derive from the identical `sc.widths()`
  fixed-central-strip incident-intensity normalization (read the single
  `i_inc` formula in `lab/sections.py::widths()` — one function, one
  convention, used everywhere both quantities are computed).
- **R11** — not applicable; no period-search/widening machinery is touched
  this cycle, confirmed.
- **R13/R14/R15** — **AT RISK as submitted** (attack #2): the proposal's
  own §6 checkbox claims compliance on a standard (an anti-zero epsilon)
  weaker than R13's actual text (a noise/amplitude floor with an
  `UNRESOLVED-BY-CONSTRUCTION` escape valve), on a denominator shared by
  four angles that are known zero-crossings of a *related* oscillatory
  quantity. **Mandatory fix 1 discharges this risk**, but only if
  implemented as an actual gate before Phase 4, not merely asserted in
  prose.
- **R16/R21** — **AT RISK as submitted**, specifically on the
  `p_abs_w`/`dt_ss_full_K`/`netd_classification` channel (attack #6): this
  is the closest live Checkpoint-4 trigger in the packet, since a third
  occurrence fires automatically with "no further deliberation" per
  R21's own adopted text, and this proposal's committed pipeline
  regenerates the exact artifact with zero current narration commitment.
  The `sigma_scat_downstream`/box-independence R16/R21 obligations are
  independently confirmed already correctly pre-committed in §6 and are
  NOT at risk. **Mandatory fix 3 discharges the NETD-channel risk**, and
  must be honored in the eventual NOTES.md Result section, not just
  pre-registered.
- **R17** — **AT RISK as submitted** (attack #5): `box_dev_scat_
  downstream`'s reuse of `XI_TOL=0.12` was not checked, before this audit,
  against the largest already-established comparable shift on file
  (exp-003's box_dev 2-6 at an under-margined box). **Mandatory fix 4
  discharges this risk.**
- **R19** — not at risk. Call-count (24) vs. row-count (6) asserts are
  already explicit and separate in §2.4, matching precedent.
- **R20** — **not yet fired, contingent risk.** This audit is itself the
  Phase-2 catch of the `pool_rows()` duplication defect (attack #3) —
  because it is caught here, before Phase 3 freezes anything into
  Result/Learned prose, R20's own trigger condition ("surviving a
  document's own Phase-3 freeze into Result/Learned, caught only at Phase
  5") is not met and does not fire. **Mandatory fix 5 is what keeps it
  that way** — if the uncorrected R3-vs-R4 contrast is instead carried
  into NOTES.md's Result section unqualified and this same defect
  resurfaces at Phase 5, that would constitute a fresh R20-shaped citation
  defect, separately countable from R21's own tally on the NETD channel.

**Bottom line:** two of nine standing rules (R13-15, R21) sit genuinely at
risk of firing Checkpoint criterion 4 if this proposal runs as submitted;
a third (R17) and a contingent fourth (R20) are also live. All four are
discharged by the six mandatory fixes above, none of which require
re-running FDTD or changing this cycle's scope, angle set, or box
geometry. No constraint (1-4) is violated or quietly dropped — this
remains, correctly, a pure T1-N/A instrument-fidelity cycle.
