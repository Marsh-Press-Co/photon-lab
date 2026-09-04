# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 87 (exp-110)

*Fresh context, blind to every other seat's Phase-5 output this cycle.
Charter (PANEL.md, verbatim): surface interaction, absorption spectra,
angular dependence, scattering cross-sections — is the proposal's optical
response coherent as stated, across wavelength and angle? Note for the
record: my own Iteration-85 self-review (exp-108) is the origin of the two
named low-power bins (−146.25° at r=156, +168.75° at r=312) this cycle's
new instrument was built to test — read that finding as the thing being
tested here, not as ground truth to defend.*

## 0. Verification performed (from primitives, not from NOTES.md's prose)

All figures below were independently recomputed — either by importing
`run.py`'s actual committed functions and running them against
`results.json`'s own persisted `raw_patterns`, or by live-executing the
cycle's own scripts — not read off NOTES.md and trusted.

**0.1 — `mirror_pooled_floor`/`classify_item_i_local` re-derived from
primitives (task a).** Loaded `run.py` via `importlib`, pulled
`raw_patterns[m]["peccored"/"hollow"/"delta"]` for all 6 margins at both
r directly from the committed `results.json`, and re-ran
`classify_item_i_local` myself. Every one of the 6×2=12 `(r, margin)`
outputs — `floor`, `floor_peccored_pooled`, `floor_hollow_pooled`, the
full 48-element `resolved` boolean array, `n_resolved`, `n_total` —
reproduces **bit-for-bit** against what is stored in
`results.json[r]["local_diag"][m]`. Aggregating: **r=156: 203/288
RESOLVED (70.5%), 85 UNRESOLVED-BY-CONSTRUCTION (29.5%); r=312: 222/288
RESOLVED (77.1%), 66 UNRESOLVED (22.9%)** — matches NOTES.md's Result
table exactly, independently re-summed from the per-margin arrays, not
copied. Both named bins: **UNRESOLVED-BY-CONSTRUCTION** at margin=32,
confirmed by index (`bin_centers_deg.index(-146.25)`/`.index(168.75)`),
matching `named_bin_status` exactly. **Confirmed correct — n_resolved/
n_total counts and both named bins' disposition are exactly as reported.**

**0.2 — Mirror-index algebra re-derived independently.** `bin_centers_deg[i]
== -bin_centers_deg[47-i]` for all 48 bins, both r, checked directly
against the committed array (`all(abs(bc[i]+bc[47-i])<1e-9 ...)` → True
both r) — not merely re-asserted from the proposal's formula.

**0.3 — `reproduction_precondition` figures vs exp-108's own committed
`results.json` (task c).** Read exp-108's own `tier1.r156/r312.
reproduction_precondition.widths` directly:
`sigma_abs=279.66065695338267, sigma_ext=560.198850825502` (r=156);
`sigma_abs=588.021832145504, sigma_ext=1191.3258584254531` (r=312).
Compared against exp-110's own `results.json[r].reproduction_precondition.
checks` — **`rel_dev=0.0` exactly, all three fields (`sigma_abs`,
`sigma_ext`, `abs_ext_ratio`), both r.** `gate_p0` and
`reproduction_precondition_108` also PASS exact, both r
(`rel_abs=rel_ext=0.0`). **Confirmed: the reproduction chain
(exp-106→exp-108→exp-110) holds to full float precision, not merely to
the claimed `<1e-9` bound — it is 0.0.**

**0.4 — Beyond what NOTES.md itself claims: bit-exact `rel32` reproduction.**
Not asked for by name, but the natural extension of (0.3): I compared this
cycle's own freshly re-captured `item_i.rel32` (48-element array, both r)
against exp-108's own committed `rel32`. **`max|Δ|=0.0` exactly, both r.**
This is a stronger fidelity check than the box_a-widths-only comparison
NOTES.md reports — the *entire* re-capture, not just one scalar ledger
triple, reproduces bit-for-bit. Worth stating for the record since it is
not currently narrated anywhere in this document.

**0.5 — Live re-execution, not just static reads.** Re-ran
`lab/validation/run_all.py --only 26` (3/3, `rel_diff_truncated=1.999`,
exact match), the full standard suite `--only 12346789` (41/41, 80s), and
`linear_fit_control.py` (all four synthetic cases reproduce to the
document's own printed precision). All green, all matching.

**No discrepancy found anywhere in (a) or (c).** The headline
counts, the two named bins' disposition, and the reproduction-precondition
figures are exactly as NOTES.md states.

## 1. Task (b) — is "narrows rather than resolves" a fair characterization?

**Short answer: defensible but under-stated in the negative direction —
this cycle's own instrument produces a more decisive finding than its own
"genuinely open, not resolved either direction" framing conveys, though
the caution itself (the common-mode blind spot) is real and correctly
disclosed.**

Checked the actual margin of failure, not just the RESOLVED/UNRESOLVED
boolean, by reading `local_snr_peccored`/`local_snr_hollow` at both named
bins directly from `results.json`:

| r | bin | local_snr_peccored | local_snr_hollow | ratio to K=1 threshold |
|---|---|---|---|---|
| 156 | −146.25° | 0.097 | 0.106 | signal is ~10× **below** even an unmultiplied (K=1) median-odd-noise floor |
| 312 | +168.75° | 0.258 | 0.287 | signal is ~3.5–4× below K=1 |

Two things I checked that NOTES.md's Result prose does not report, both
strengthening the finding:

1. **This is not a boundary call.** At r=156 the entire population splits
   cleanly: every UNRESOLVED bin (margin=32) has `snr ≤ 0.45`; every
   RESOLVED bin has `snr ≥ 1.33` — a clean bimodal gap, no bin anywhere
   near the K=3 (or even K=1) cutoff. Same shape at r=312 (`≤0.79` vs
   `≥1.32`). The named bins sit deep inside the noise-dominated cluster,
   not at its edge.
2. **The disposition is margin-independent.** I checked all 6 margins,
   not only margin=32 (the one NOTES.md's Result narrates): both named
   bins are UNRESOLVED-BY-CONSTRUCTION at **every** margin
   (24/32/40/48/57/65), with `local_snr` consistently in the 0.06–0.40
   (r=156) / 0.13–0.39 (r=312) range throughout. This data is already
   computed and persisted (`local_diag[m]` for every `m`) but never
   stated in Result prose — an R21-adjacent narration gap (the finding
   *is* persisted, so R21 does not literally fire, but a future citation
   reading only the Result paragraph would see one margin's worth of
   evidence, not six).

From my own charter's lens (angular-dependence, scattering
cross-sections): this pattern — a physically real, strongly forward-peaked
diffraction pattern whose low-cross-section side/back-scatter bins carry
field amplitudes far below the simulation's own discretization-noise
scale — is exactly the textbook signature of near-null relative-error
blowup, not of genuine shape structure hiding under a global-peak
normalization. A real physical asymmetry between the PEC-cored and hollow
patterns at these specific angles would need to be a *change in a
quantity that is itself already deep in the noise floor*, which is
possible in principle but is the less parsimonious reading given the data
in hand.

**What does NOT change my assessment:** the common-mode blind spot
(RT-1/PHOTONICS' own Phase-2 attack, independently re-derived by Red Team
as an exact algebraic identity — a bias identical at bin `i` and its
mirror bin cancels in `|pattern[i]-pattern[47-i]|` at any sample size) is
real, correctly disclosed, and genuinely unclosed by this cycle's pooling
fix. It is the honest reason the document does not — and should not —
declare the question resolved. My finding is that the document's caution
is calibrated to the *existence* of that blind spot but not to how large
a common-mode effect would need to be to overturn the odd-noise evidence
already in hand: the peccored/hollow signal at both named bins sits
3.5×–30× below even an unmultiplied noise floor, at every margin, so any
rescuing common-mode structure would need to be comparably large — a
possibility with no independent evidence for it anywhere else in this
heavily cross-verified codebase. **Net: "narrows" is true and honestly
scoped; a more forthright Result narration would say the narrowing
leans clearly toward "artifact," margin-independently, while correctly
stopping short of "resolves."** This is an interpretive/completeness gap,
not a factual error — nothing here is wrong, only somewhat more
hedged than the magnitude of the underlying numbers supports.

## 2. Other checks performed against my own charter

- **Physical premise of the mirror floor** (CY=N/2, symmetric source,
  CY-centered geometry) — re-verified from `run.py`'s own
  `geom_fixedabs()` exactly as I did at Phase 2; unchanged this cycle,
  still holds exactly at both r.
- **`angular_scattered_pattern`'s own construction** (`lab/sections.py`
  lines 200–263) — read again: it is a signed, per-cell Poynting-flux
  quantity on a square perimeter path (near/mid-field, not true far
  field, correctly disclosed in `DISCLAIMER`), consistent with every
  prior use on this channel. `pattern_delta = peccored - hollow`,
  confirmed directly in `analyze.py`.
- **Fix 1 (pooling) and Fix 2 (disclosure)** — both genuinely implemented
  as specified: `mirror_pooled_floor` takes the median over 24
  within-margin bin-pairs (not a single-point draw), and the
  common-mode-blindness sentence is verbatim in `DISCLAIMER`, live-fired
  in both `predictions_text` and `result_text` (checked: `DISCLAIMER in`
  both, exact substring). My own Phase-2 flip condition (split the
  Iteration-88 fault-injection control into an asymmetric case and an
  explicit symmetric/common-mode case) was adopted verbatim in the
  Idealizations section.
- **Item i's frozen CONFIRM verdict** — untouched, correctly informational
  scoping preserved; re-derived `classify_item_i` from this cycle's own
  fresh capture and confirmed it independently reproduces `CONFIRM` at
  both r with `confirm_all_margins=True`, `runs=[]` — bit-identical to
  exp-108's own (§0.4, above).

## 3. Verdict on the Combined Verdict claim

**CONFIRM-WITH-GAPS.**

Every numeric claim I independently re-derived from primitives —
n_resolved/n_total counts, both named bins' RESOLVED/UNRESOLVED
disposition, the reproduction-precondition figures against exp-108's own
committed data, item 2's synthetic table, item 3's stage26 controls, the
mirror-index algebra — reproduces exactly, several of them to a tighter
bound (`0.0` exact) than the document itself claims (`<1e-9`). No
arithmetic, citation, or classification-logic defect found anywhere.
This is a genuinely clean, well-verified governance cycle, matching this
sub-thread's own high bar. The one gap I found (§1) is interpretive, not
factual: the Result prose's "genuinely open, not resolved either
direction" framing for item 1c/1d is defensible given the correctly-named
common-mode blind spot, but understates how decisively (3.5×–30× below
even an unmultiplied floor, at every one of six margins, with a clean
bimodal separation from the resolved-bin population) the odd-noise
evidence actually leans against PHOTONICS' own prior "real shape
structure" reading — and the margin-independence of that finding is
computed and persisted but never stated in Result prose (a cheap,
zero-new-FDTD fix). Neither gap is outcome-reversing: item 1 stays
correctly informational and does not touch any scored verdict this cycle.

## 4. Ranked top-3 candidate directions for Iteration 88

1. **Execute the already-queued independent, non-differencing floor check
   at the two named bins** (a `cpl`-refinement spot check, named in Red
   Team's Phase-2 audit §6 item (i) and this cycle's own Idealizations) —
   the single instrument that can actually discriminate "genuine
   discretization noise" from "real common-mode-masked structure" at
   exactly the two bins this whole sub-thread has been circling since
   Iteration 85. This is the highest-value item because §1 above shows
   the odd-noise evidence is already about as decisive as this
   construction can make it — the common-mode axis is the only piece
   still missing.
2. **State item 1c/1d's per-margin consistency in Result prose**, not
   only the margin=32 headline: both named bins are UNRESOLVED-BY-
   CONSTRUCTION at all 6 margins with `local_snr` consistently
   0.06–0.40/0.13–0.39, not a single-margin coincidence. Zero new FDTD —
   the data is already in `results.json["local_diag"]`. Closes the
   narration gap named in §1 before a future citation reads only the
   one-margin summary.
3. **Run the already-planned symmetric/common-mode fault-injection case
   (Fix 2(b))** with a graded series of injected common-mode amplitudes,
   not just a single pass/fail check — since §1's own finding is that the
   real named bins sit 3.5×–30× below the odd-noise floor, the
   informative question for Iteration 88 is not merely "does the floor
   correctly ignore a symmetric perturbation" but "how large would an
   injected common-mode signal need to be, relative to that same margin,
   before it would plausibly explain the two named bins' historical ~10%
   reading" — turning the qualitative disclaimer into a quantitative
   bound on how much common-mode contamination the data can actually
   hide.
