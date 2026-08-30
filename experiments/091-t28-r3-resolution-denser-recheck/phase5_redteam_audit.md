# PHASE 5 — RED TEAM FINAL AUDIT · Panel Iteration 68 · exp-091
## "R3 Resolution & Denser Recheck"

*Fresh sub-agent, no memory of any prior cycle. Read in full: `PANEL.md`
(charter + Phase-5 spec); `LOGBOOK.md`, all ~20,000 lines — the complete
RULED OUT registry (R1–R14 full text), the ESTABLISHED section, and the
complete LIVE THREADS record (T1–T28), with particular depth on T10 (the
SIGMA_ON/τ_center erratum, lines 870–971 and 6349–6852), the four prior
disclaimer-erosion Checkpoint-4 instances (Iterations 53/63/64/65, lines
1236–1249 and 4490–4806), the R13/R14 founding texts (lines 410–538), and
the complete exp-069→exp-090 T28 sub-thread arc (lines 2234–5160); the
complete exp-091 record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`); all six Phase-5 reviews; exp-087–090's
`NOTES.md`/`phase5_redteam_audit.md`; `lab/materials.py` and `lab/fdtd2d.py`
in full. Every load-bearing number below was independently re-derived from
`results.json`/`run_output.txt`/source code, not taken from any citation,
including the task brief's own summary.*

---

## 0. Independent re-verification of the load-bearing numbers (before adjudicating anything)

All confirmed bit-exact against `results.json`'s `raw` block and
`run_output.txt`, and against `lab/materials.py`/`lab/fdtd2d.py` source:

- **Sign flip.** `delta_scene(40.2°)`: cpl=20 (Leg1, fresh STEPS=4200)
  `−1.5426768×10⁻⁴`; cpl=30 (Leg2) `+4.3698986×10⁻⁴`. Opposite signs.
  Filed STEPS=2800 comparator (`−1.540815×10⁻⁴`) agrees with fresh
  STEPS=4200 to 0.12% — the flip is a `cpl` effect, not a settling one.
- **(a2) both brackets REFUTE.** `delta_scene(40.2°)=+4.3699×10⁻⁴`,
  `delta_scene(40.4°)=+9.8564×10⁻⁴` — same sign, growing; no crossing in
  `[40.2°,40.4°]`. `delta_scene(41.4°)=+5.6255×10⁻⁴`,
  `delta_scene(41.6°)=+1.7838×10⁻⁴` — same sign, shrinking; no crossing in
  `[41.4°,41.6°]`. The known cpl=20 crossings (40.26542°, 41.46090°, both
  re-derived independently from `exp-083/results.json`'s own 31-point
  census by `find_zero_crossings`, not hand-typed) sit inside both cpl=20
  brackets and outside both cpl=30 brackets. Confirmed.
- **`_label()`'s inequality.** Read directly from
  `experiments/087-.../run.py:193-194`: `if ratio > RATIO_HIGH: return "X"`
  — a **strict** `>`. `ratio_k(40.2°,cpl=30)=10.074428486174352`;
  `(10.074428486174352−10.0)/10.0 = 0.744285%`. Confirmed razor-thin, not a
  rounding-adjacent call — at exactly `10.0` the code returns `"C"`
  (`exp-087's` own synthetic gate test asserts `(RATIO_HIGH, "C")`).
- **41.4° reclassification.** `ratio_k`: cpl=20 (Leg1) `28.845594738…`
  (ENERGY-DOMINANT) → cpl=30 `9.211607655…` (CONSISTENT). Confirmed, and
  well clear of the boundary in the new direction (not razor-thin like
  40.2°).
- **37.2° holds.** `ratio_k`: cpl=20 `3.4640971…` → cpl=30 `1.846267…`.
  Both CONSISTENT. Confirmed.
- **(b2) CONFIRM.** `frac_p_abs_R3/frac_p_abs_cpl20` = `2.7756/1.1178/
  1.3270` at 37.2°/40.2°/41.4°, all inside `[0.3,3.0]`, all sign-matched.
  Confirmed.
- **House gates.** `vac_pass`/`xi_pass`/`nonneg_pass` all `True`, backed by
  hard `assert` statements at `run.py:317,430,432` sitting between gate
  computation and the `results.json` write — the script could not have
  produced output had any failed. 40/40 calls, no duplicates
  (`assert len(jobs)==40`, `assert len(set(jobs))==40`).
- **Settling (c1/c2).** All six `c1` cells and all four `c2` cells (both
  legs, both spot-checked angles) show `rel_dev` of `10⁻⁷`–`10⁻⁴` relative,
  six-plus orders of magnitude inside the `≤1%` CONFIRM band. Under-settling
  is cleanly, independently ruled out as an explanation for anything in
  this cycle.
- **`graded_black_shell`'s actual signature** (`lab/materials.py:74`):
  `def graded_black_shell(sim, cx, cy, r_in, r_out, sigma_max=0.5,
  eps_max=1.0)`. Both native `build_article` (`experiments/083-.../
  run.py:160-161`, bit-identical since exp-024) and this cycle's new
  `build_article_r3` (`run.py:188-193`) call it with `sigma_max`/`eps_max`
  **unspecified** — i.e. `0.5` at both resolutions.
- **`lab/fdtd2d.py`'s conductivity convention**, read directly: line 21,
  `"Units: grid units (dx=1, c=1)"`; `Sim.run()`'s per-step loss
  `alpha = self.sigma_e * S / (2.0 * self.eps_r)` (`fdtd2d.py:215`), where
  `S` is a fixed Courant number independent of `cpl`. A wave crosses `N`
  cells in `N/S` steps, so accumulated loss `≈ alpha·(N/S) = sigma_e·N/
  (2·eps_r)` — **`S` cancels exactly**, leaving accumulated optical depth
  `∝ sigma_e × thickness(cells)`, independent of `cpl`. Shell thickness:
  native `78−30=48` cells; R3 `117−45=72` cells — the *same* `1.44µm`
  physical thickness (`48×30nm=72×20nm`), but **1.5× more cells** at the
  *same* `sigma_max=0.5`. This is exactly LOGBOOK's own T10/SIGMA_ON
  erratum mechanism (`τ_center=2·σ·r_out(cells)`, LOGBOOK lines 913–919),
  now recurring for the first time on `graded_black_shell` itself. **I
  independently confirm MATERIALS' self-review's finding from source, in
  full**, matching the task's own required check (item 1).
- **`p_abs_w(C40)` common-mode shift, all three angles** (my own
  recomputation from `raw`): 37.2° `2.812726→2.909923e-12` (**+3.457%**);
  40.2° `3.077219→3.187660e-12` (**+3.590%**); 41.4° `3.164978→3.282666e-12`
  (**+3.719%**). Matches MATERIALS' cited 3.46%, EM's cited +3.2–4.0% table
  (`1.0346/1.0359/1.0372` for C40; `1.0319/1.0350/1.0396` for G40 —
  independently re-derived and confirmed), and THERMODYNAMICS' cited
  +3.46–3.72% base-drift figure, via three different computation routes
  converging on the same number. A small, nearly angle-independent,
  common-mode increase — the shared signature all three seats correctly
  read as ordinary staircasing reduction, not the sigma-inflation
  confound's full effect (see §1.2/§4 below for why this does not settle
  the question for `delta_scene`).
- **`frac_contrast` inflation, all three angles** (my own recomputation):
  37.2° `5.2079×`; 40.2° `2.7793×` (sign flip); 41.4° `4.1554×`. Matches
  EM's cited 2.8×–5.2× table exactly.
- **QUANTUM's caution-zone-inversion arithmetic** (my own from-scratch
  rebuild of the n=7 table from `exp-090/NOTES.md`/`results.json` directly,
  not from QUANTUM's citation of it):

  | θ | margin (FLOOR) | ratio_k (cpl=20) | Y (as filed) |
  |---|---|---|---|
  | 41.4° | 1.3095 | 28.807 | 1 |
  | 40.2° | 1.4764 | 25.082 | **1 ← sets lower edge** |
  | 37.2° | 2.1709 | 3.443 | **0 ← sets upper edge** |
  | 36.0° | 3.8793 | 2.642 | 0 |
  | 41.8° | 6.5889 | 5.710 | 0 |
  | 38.4° | 7.4946 | 0.908 | 0 |
  | 38.8° | 8.0187 | 3.873 | 0 |

  Zone `=[max{margin:Y=1}, min{margin:Y=0}] = [1.4764, 2.1709]`, matching
  the filed value exactly. **Relabeling 41.4° to `Y=0`** (its cpl=30
  finding, this cycle): new `Y=1={40.2°:1.4764}` alone; new
  `min{margin:Y=0}=min(2.1709, 1.3095)=1.3095`. **`1.3095 < 1.4764`: the
  order-statistic zone inverts** (lower edge exceeds upper edge) —
  confirmed exactly, and this is *precisely* `exp-090/NOTES.md`'s own
  pre-registered Q3 falsification clause: *"Falsified if the computed zone
  is empty, inverted, or the underlying separation has any tie/inversion
  (would mean Q1 itself was wrong)."* I confirm this arithmetic
  independently and rule it correct without qualification.

No arithmetic, labeling, or geometry defect found anywhere independently
checkable. All six Phase-5 reviews' cited numbers reproduce bit-exact.

---

## 1. Adjudication of the six Phase-5 reviews

### 1.1 PHOTONICS (CONCUR-WITH-GAP) — **UPHOLD, with one scope gap noted**

The reproduction (§1) is exact and the physical-plausibility argument
(§3a–d: a coherent PAD-driven phase/timing signal integrated over a
tens-of-wavelengths aperture is structurally the observable most exposed to
a resolution-driven null relocation; T10 precedent for comparable-magnitude
near-field point-probe sensitivity; no geometry-construction defect found)
is sound and correctly caveated as informal where it is informal (§3c's
back-of-envelope crossing extrapolation, ≈−0.22°/+0.23°, explicitly flagged
as illustrative, not filed). **UPHOLD in full.** The missing Result/Learned
section finding, item 10's uninformative null, and item 8's genuinely
marginal (1.6% relative) "relief" number are all independently confirmed
(§2 below). **UPHOLD.** The caution-zone analysis (§5: both `Y=1` points
now fail resolution-verification, one outright, one by 0.74%) is correct
and matches my own §0 rebuild exactly. **UPHOLD.**

**One gap PHOTONICS' own review does not cover** (not a fault — outside a
plausibility argument's natural scope, but material to the overall
picture): the physical-plausibility case for "genuine near-field
resolution sensitivity" is argued entirely independent of whether the R3
article itself is a resolution-matched replica of the native one. It is
not — see §1.2/§4.

### 1.2 MATERIALS self-review (CONCUR-WITH-GAP) — **UPHOLD the sigma_max finding in full; PARTIALLY UPHOLD its scoping**

The sigma_max/τ_center finding is real, previously undiscovered, and I
independently re-derived it from source myself (§0) rather than trusting
MATERIALS' own citation of it — same conclusion, same mechanism, same
numbers. **UPHOLD in full**, and I credit this as the single most
consequential new finding of this Phase-5 layer alongside QUANTUM's
zero-inversion arithmetic (§1.4).

MATERIALS' further judgment — "checked against the data and judged NOT the
primary driver," specifically scoped to `p_abs_w`/(b2) — is **correct as
far as it goes** (the ~3.46–3.72% uniform shift on an already
near-saturated absorber, T9's `σ_abs/σ_ext≈0.51`/`R≤0.2%` anchor, is a
physically coherent account of why bulk absorbed power barely moves under
a 1.5× nominal optical-depth inflation). **But the scoping to (b2) alone is
where I partially withhold agreement.** `graded_black_shell`'s conductivity
also sets the shell's own small residual reflectivity — the quantity
`delta_scene`/`frac_contrast`/`ratio_k` (the PRIMARY headline channel: the
sign flip, the razor-thin 40.2° survival, the 41.4° reclassification) are
built from. `PAD` is independently proven lossless vacuum (exp-076,
re-confirmed at §0 above: `_damping` depends only on `absorb`), so the
sigma inflation is **common-mode** between `C40_R3`/`G40_R3` (they share
the identical article) — but common-mode does not mean *harmless* to a
*difference* signal that is itself a coherent interference construction: a
1.5×-deeper absorbing shell's own small residual reflection amplitude
*and phase* could plausibly shift, changing how that residual couples into
the interference pattern the PAD geometry sets up, independent of whether
the bulk absorbed-power reading moves. **MATERIALS' own review never checks
this** — its data check (§4 of `phase5_review_materials.md`) is entirely
`p_abs_w`-side. Neither does any other Phase-5 review. This audit does not
resolve the question either (a clean answer needs the same cheap
sigma-rescaled rerun MATERIALS already proposed, scored against
`delta_scene`/`frac_contrast` in addition to `p_abs_w`/`frac_p_abs`) — but
I rule the scoping to (b2) alone **incomplete, not wrong**, and elevate
this to a named, undischarged, load-bearing open question for the
PRIMARY channel, not only the numerator side (see §4, §6 item 2).

The Result/Learned-section finding and its exp-080 analogy: **UPHOLD**
(§2 below; independently confirmed and I rule identically, §5). The
candidate R15 rule: **adjudicated separately, §3.**

### 1.3 ELECTROMAGNETISM (CONCUR-WITH-GAP) — **UPHOLD in full**

Every independent recomputation matches (§0). The "vindicated but
exceeded" framing of its own Phase-2 circularity concern is accurate and
well-argued: the ±0.2° bracket Phase 3 adopted (itself a faithful,
grid-aligned execution of EM's own Phase-2 proposed fix) was not wide
enough to *locate* the crossing, only to show it isn't where the old
FLOOR/bracket construction expected — a real, disclosed limitation, and EM
is correct that a future citation reading this as "the crossing moved a
little" rather than "the crossing's location is presently unknown beyond
being outside two named windows" would overclaim. **UPHOLD.**

The broad, angle-independent 2.8×–5.2× `frac_contrast` inflation at **all
three** census angles, not merely the two crossing-adjacent ones —
independently reconfirmed at §0 exactly (5.2079/2.7793/4.1554×) — is a
genuinely new, correctly-argued finding (a pure phase shift of a
fixed-amplitude sinusoid should not inflate the sinusoid's own amplitude
far from a zero; something amplitude-side is also moving). **UPHOLD.**
EM's own energy-side corroboration (the p_abs_w common-mode
+3.2%–4.0% table) independently matches MATERIALS'/THERMODYNAMICS' figures
via yet a third computation route — genuinely convergent, not merely
repeated. **UPHOLD.**

EM explicitly states it did **not** compute the Yee-grid dispersion
integral it argues qualitatively for, and correctly names this as its own
Rank-2 item precisely to keep the claim "argued-then-verified" rather than
"argued-and-accepted" — the R8 discipline applied to its own claim. This
self-discipline is exactly right and I do not treat the un-computed
integral as a defect; it is correctly flagged forward, not silently
assumed.

### 1.4 THERMODYNAMICS (CONCUR with PARTIAL) — **UPHOLD**

The mechanistic decomposition — a mundane, staircasing-driven ~3.46–3.72%
common-mode `p_abs_w` growth, amplified by R14's own subtractive-
cancellation shape into the filed 1.12×–2.78× `frac_p_abs` swing —
independently reproduces exactly against my own §0 numbers and against
EM's/MATERIALS' independent figures. **UPHOLD**, and I credit this as the
clearest mechanistic account in this Phase-5 layer of *why* (b2) behaves
as it does (as distinct from *whether* it is fully clean — see §1.2).
Reclassifying `frac_p_abs` as "classification-stable, not
resolution-converged" (with a falsifiable, directional prediction —
further growth, not oscillation, at `cpl=40`) is the correct, careful
characterization; I adopt it. The energy sidecar (364×–433× below NETD,
consistent with exp-087's established margin) is correctly scoped and
correctly disclaimed (Idealizations 3/6/7). **UPHOLD.**

THERMODYNAMICS' forward-flagged structural question — that R13's own
presupposition (a denominator zero-crossing is a fixed, resolution-stable
feature, only needing to be avoided at one resolution) is now shown false
on this cycle's own evidence — is correctly flagged as outside its own
charter and handed forward rather than adjudicated. I agree with the
substance (§4 below formalizes it) and rule THERMODYNAMICS correct to
raise it without resolving it itself.

### 1.5 QUANTUM OPTICS (CONCUR-WITH-GAP) — **UPHOLD in full**

The caution-zone-inversion arithmetic (§2 of its review) is independently
reconfirmed exactly at §0 above, including the AUC computation
(6 negative/1 positive under the relabeling, 5 of 6 concordant pairs,
`AUC=5/6≈0.833`) and the observation that the *aggregate* AUC looks only
mildly damaged while the *specific, order-statistic zone construction*
(built from an n=2 positive class) breaks completely — a genuinely
important distinction, correctly drawn. **UPHOLD, decisive.** This is the
single most consequential quantitative finding in this Phase-5 layer,
alongside MATERIALS' sigma_max discovery.

The self-assessment of its own Phase-2 margin/crossing-distance
metric — mechanistically real in *direction* (a `1/x`-type nonlinearity
near a pole amplifying a small input difference is not numerology), but
explicitly declined as a standing rule off a single confirming instance,
citing the R5/R7/R12 "don't generalize from n=1" lineage by name — is
exactly the correct application of this program's own house discipline,
and I adopt QUANTUM's own recommendation (log as a candidate
"crossing-proximity fragility index," not a rule) without modification.
**UPHOLD.**

The (a2) "moved vs. hidden short double-crossing" extrapolation is
reasoned correctly and matches my own independent read: (i) both bracket
windows preserve their cpl=20 local slope *sign* (no reversal, which a
true in-window double-crossing would require somewhere), (ii) the two
naive linear extrapolations (≈40.04°/≈41.69°, independently reproduced by
PHOTONICS via the identical arithmetic) move in *opposite* directions,
disfavoring a single systematic angular-calibration explanation, and
(iii) no periodicity on record operates at a sub-0.2° length scale. All
three legs are correctly, explicitly caveated as non-conclusive.
**UPHOLD** as the more parsimonious reading, not a settled fact.

The Checkpoint criterion 4 three-part reasoning (named-gap-being-
discharged is not "known, named, ignored"; the finding itself is caught
blind, before LOGBOOK, hence non-firing on the standard discharge test;
the missing Result section is a completeness gap, not an omission-lineage
violation, because nothing yet exists to have failed to propagate into)
is correct and I adopt it as part of my own Checkpoint ruling (§4).
**UPHOLD.**

### 1.6 VISION SCIENCE (CONCUR-WITH-GAP) — **UPHOLD the facts in full; rule explicitly on the Checkpoint question it declined to adjudicate (§2)**

Every fact VISION cites is independently confirmed: `NOTES.md` has no
`## Result` heading (grep confirms only `Hypothesis`/`Setup`/`Predictions`/
`Idealizations`, 221 lines); `netd_disclaimer`/`scope_note` are written to
`results.json` (`run.py:746,749`) but have **no corresponding `print()`
call anywhere in the 771-line script** — I confirmed this directly by
grepping every `print(` call in `run.py` (there are print statements for
every one of (a)/(a2)/(b)/(b2)/(c1)/(c2)/(d), none for the two disclaimer
fields); `run_output.txt` contains zero occurrences of "NETD",
"Idealization", "human-eye", "constraint-3", "instrument recalibration",
or "REALIZABILITY_MEMO" in its 125 lines (independently grepped). **UPHOLD,
fully.**

The perceptual-threshold recheck using the cycle's *actual measured*
cpl=30 `delta_scene` values (not merely the pre-registered band edges) is
independently reconfirmed: every measured value stays 4.0×–28.0× below
`C_THR_BASE=0.005`, with 37.2° the tightest at ≈4.0×, correctly landing
between the two pre-registered hypothetical band-edge margins — a genuine,
correctly-executed R9-discipline check (comparing `delta_scene`, not
`frac_contrast`, against the threshold, avoiding the unit mismatch R9 was
adopted to catch). **UPHOLD.** The forward-flagged R9-shape conflation
risk (40.2°'s razor-thin margin against `RATIO_HIGH=10.0`, an instrument-
classification gate, is a completely different quantity from the
perceptual margin against `C_THR_BASE=0.005`, and a future write-up
merging the two "close to a threshold" narratives would misstate both) is
a genuinely useful, prospective catch. **UPHOLD**, and I fold it into my
own drafted Result section (§5) as an explicit guard.

**On the Checkpoint-4 question VISION explicitly declined to rule on
itself:** adjudicated in full at §2, below.

---

## 2. Ruling on VISION's disclaimer-propagation finding: a new gap shape, not a fifth instance of the Iteration-65 lineage — reasoned explicitly

VISION asks Red Team to weigh this "at least as serious as the four prior
instances" against the Iteration-65 CHECKPOINT's unconditional "a fourth
instance fires automatically" language, rather than assuming non-firing by
analogy to this cycle's own milder Phase-2 footnote-miscitation catch. I
take the question seriously and reason through it on its own facts, as
instructed, rather than pattern-matching either way.

**What the Iteration-65 rule's own text actually targets.** Re-reading the
CHECKPOINT block itself (LOGBOOK lines 4698–4759) verbatim: the defined
shape is *"NETD-not-human-eye/constraint-3-not-tested language present in
the record's own supporting data (`results.json::netd_disclaimer`/
`scope_note`) but silently absent from **one prose restatement** of the
classification it governs."* Every one of the four prior instances
(Iterations 53/63/64/65) shares this exact structure: **two (or more)
existing prose locations**, a caveat correct and present in one, silently
missing from another written alongside it in the same document, in the
same cycle. Iteration 65's own founding instance is paradigmatic: Q1/Q5/Q6
of `NOTES.md` carried the idealization inline; the adjacent Q4 paragraph,
written in the same document at the same time, did not.

**What exp-091's defect actually is, on inspection.** There are, in fact,
**two** distinct gaps bundled in VISION's finding, and they should be
separated:

1. **`NOTES.md` has no Result section at all.** There is no second prose
   location for anything to have failed to propagate *into* — the
   propagation-failure mechanism the rule was built to catch (a caveat
   present in location A, dropped from location B) cannot even be
   evaluated, because location B does not exist. This is a **completeness
   gap** (adjudicated on its own terms at §5, matching the exp-080
   precedent), not a propagation failure.
2. **`run_output.txt` never prints the disclaimer, even though `run.py`
   prints every other result.** This is a genuinely different *kind* of
   authoring gap from any of the four priors: not a caveat that migrated
   incompletely between two hand-written prose sections, but a single
   `print()` call that was never written for two specific dict keys, in a
   script whose every *other* output field has one. The failure surface is
   **JSON-vs-stdout**, not **prose-section-A-vs-prose-section-B** — a
   surface this sub-thread's entire four-instance disclaimer-erosion
   history has never previously exercised, checked, or named.

**Ruling: this is a new, distinct gap shape — mechanistically different
from the Iteration-65 lineage's own defined shape, not merely a
"milder"/"worse" variant of it — and does NOT fire Checkpoint criterion 4
as a fifth instance of that specific rule.** I reach this independent of,
and for a more precise reason than, the "shape not severity" analogy
Red Team's own Phase-2 audit used for this cycle's unrelated
footnote-miscitation catch (§1.5 of `phase2_redteam_audit.md`): the
Iteration-65 rule's unconditional consequence was scoped, by its own text,
to a specific recurring failure *mechanism* (prose-to-prose non-
propagation of an existing caveat) discovered and named across four
concrete instances. A textually different mechanism — a print statement
that was never authored at all, on a surface never previously
implicated — is not "the same defect a fifth time"; it is a new failure
mode surfacing for the first time, which this program's own R5/R6/R9/R10/
R11/R12/R13/R14 precedent uniformly treats as a **founding** instance
(non-firing, on the standard discharge test) rather than a retroactive
violation of an existing rule calibrated on different evidence. I do not
find this a case of avoiding the rule's spirit: had `NOTES.md`'s Result
section existed and dropped the banner from one paragraph while carrying
it in another — the literal fourth-instance-plus-one shape — I would rule
differently, and say so plainly. That is not what happened here.

**This does not mean the finding is minor.** I agree with VISION's own
characterization that, judged by *end-state severity* (a reader of the
one human-legible artifact this program's convention calls "the
human-readable record" finds the disclaimer nowhere), this is at least as
bad as, arguably worse than, any of the four prior instances — three of
which left the caveat findable in at least one prose location a reader
might actually open. Severity and Checkpoint-firing are not the same
question, and this program's own explicit design (Checkpoint criteria, not
scientific importance, are the only gates) applies exactly as much to a
severe-but-differently-shaped process gap as it does to a scientifically
major finding (§4 works through the analogous reasoning for the cycle's
substance). **Discharge test, applied for completeness**: caught blind, by
VISION's own Phase-5 review, before any LOGBOOK entry for this cycle
exists — the standard non-firing condition this program has applied
uniformly to every rule's first discovery. Both grounds (new shape;
standard discharge) independently support non-firing; I rule non-firing
on both.

**What this does warrant**, matching VISION's own Rank-3 recommendation and
extending it slightly: a **new**, narrowly-scoped structural safeguard —
not a retroactive extension of the Iteration-65 rule, but its own named
item — requiring (a) a mechanical check, before Phase 5 begins, that every
`results.json` key ending in `_disclaimer`/`_note` has at least one
corresponding `print()` call in the committed `run.py`, and (b) that a
`## Result` section exists in `NOTES.md` before a cycle's Phase-4 output is
treated as complete. I recommend the Director log this as a named,
citable safeguard for Iteration 69's board (Tier-0, structural, below) —
distinct from MATERIALS' proposed R15 (§3), which concerns a substantive
calibration-boundary question, not a print-parity/document-completeness
one.

---

## 3. Ruling on MATERIALS' candidate R15: **ADOPT, with the standard founding-instance exemption**

**Text as proposed:** *"A calibration boundary (threshold, caution zone,
fitted classifier edge) built from points whose classification depends on
proximity to a demonstrated or plausible resolution-sensitive interference
node must have that resolution-sensitivity independently R3-verified
before the boundary is trusted for any future classification; R13's own
floor gate (guarding a literal near-zero denominator) is necessary but not
sufficient, since a point can clear R13's floor cleanly at every tested
resolution and still have its classification flip under grid
refinement."*

**Adjudication.** I adopt this rule, unmodified in substance, for three
independent reasons:

1. **It names a genuinely distinct failure axis, not a restatement of
   R13/R14.** R13 guards against a ratio classifier's denominator being
   too close to a *known* zero at the resolution it was measured at — a
   single-resolution, algebraic-instability concern. R14 guards a
   numerator built as a small difference between comparable quantities —
   also single-resolution. Neither rule's text says anything about whether
   the underlying feature's *location* is itself stable across grid
   refinement. This cycle is the first direct demonstration that "clears
   R13's floor at every tested resolution" and "classification is
   resolution-stable" are genuinely separate properties — MATERIALS'
   own §5 argument, independently confirmed at §0/§1.5 above (both
   `Y=1`-defining points cleared `floor_pass=True` at both resolutions
   throughout, and both still failed the classification-stability
   question one clears by 0.74% and the other fails outright).
2. **It is founded on a real, not hypothetical, instance.** Unlike a
   rule proposed defensively against a possible future risk, R15 responds
   to a demonstrated fact on this program's own record: exp-090's own
   caution zone, cited in LOGBOOK's own Iteration-67 entry as "sound,
   correctly scoped, and now independently reproduced by at least nine
   parties," has its *entire* positive-class foundation (both `Y=1`
   points) shown unstable at the one resolution this program has actually
   checked them at, and relabeling per the new data inverts the zone's
   own pre-registered falsification clause (§0). That is exactly the
   evidentiary weight R3/R5/R13/R14 were each adopted on.
3. **It generalizes correctly, not narrowly.** R15's scope ("a calibration
   boundary... built from points whose classification depends on
   proximity to a... resolution-sensitive interference node") is written
   at the right level of generality to apply to any future T28
   caution-zone/threshold-fit deliverable built on this or a structurally
   similar channel — not narrowly hand-fitted to exp-090's own zone alone
   — matching R3's/R13's own house convention of stating the general
   principle, not just the triggering instance.

**Adopted, with the standard founding-instance exemption** (matching every
prior rule in the R5–R14 lineage): **R15 does not fire on its own founding
instance** — exp-090's own zone was correctly, honestly filed with the R3
gap explicitly named as its own open Idealization (9, 11 in `exp-090/
NOTES.md`) at the time it was built; R15 makes that discipline mandatory
going forward, it does not retroactively fault the cycle that first named
the gap it closes. **Full text, adopted verbatim as R15** (RULED-OUT
registry text, for the Director to append to `LOGBOOK.md`):

> **R15 — a calibration boundary (threshold, caution zone, fitted
> classifier edge) built from points whose classification depends on
> proximity to a demonstrated or plausible resolution-sensitive
> interference node must have that resolution-sensitivity independently
> R3-verified before the boundary is trusted for any future classification
> (adopted Iteration 68, exp-091, MATERIALS' self-review finding).** R13's
> own floor gate (guarding a literal near-zero denominator at the
> resolution it was measured) is necessary but not sufficient: a point can
> clear R13's floor cleanly at every tested resolution and still have its
> classification flip under grid refinement, because the underlying
> feature's own zero-crossing *location* — not merely its measured
> distance from a fixed-resolution floor — can itself move under `cpl`
> refinement. Founding instance: exp-090's caution zone `[1.4764,2.1709]`
> (built from exp-087/088/089's n=7 sample), whose entire `Y=1` class
> (40.2°, 41.4°) failed exp-091's own resolution check — one outright
> reclassifying, one surviving only by 0.74% of the threshold's own value —
> and whose non-parametric zone construction *inverts* under the
> relabeling this demands (min{margin:Y=0}=1.3095 < max{margin:Y=1}=
> 1.4764, exactly triggering exp-090's own pre-registered "falsified if
> inverted" clause). **Does not fire on its own founding instance**
> (exp-090), matching R5/R6/R9/R10/R11/R12/R13/R14's own precedent that a
> rule's founding cycle establishes the standard rather than retroactively
> violating it — exp-090's own record named the R3 gap explicitly as an
> open Idealization at the time. Full record: `experiments/091-t28-r3-
> resolution-denser-recheck/phase5_review_materials.md` §3–§5,
> `phase5_redteam_audit.md` §0/§3, LOGBOOK.md Iteration 68.

---

## 4. Checkpoint ruling: worked through all five criteria explicitly

**Criterion 1 (all constraint metrics pass — candidate reproduction):**
does not fire, not close. This cycle makes no constraint-1–4 claim of any
kind (T1 route N/A throughout, correctly and consistently disclosed) —
there is no metric to have passed.

**Criterion 2 (a proven mechanism-class boundary, gates clean):** N/A,
correctly and consistently, matching every T28 desk/instrument cycle since
exp-069. This cycle recalibrates an instrument; it takes no position on
σ(I)/σ(x,t)/angular-selectivity/sub-threshold-operation and does not touch
`REALIZABILITY_MEMO.md`.

**Criterion 3 (engine physics beyond validated bench classes):** does not
fire. No new engine machinery was needed — `_run_sim_r3`/`build_article_r3`
are R3-scaled mirrors of already-validated primitives (`Sim`,
`materials.pec_disk`/`graded_black_shell`, `sc.full_capture`), confirmed
by direct `git diff`-equivalent inspection (the module docstring's own
"zero `lab/` diff" claim, which I independently confirm: the only
non-additive change anywhere is the single new `G40_R3` entry in
`experiments/069-.../design_geometry.py::R3_CONFIGS`, additive by
construction).

**Criterion 5 (two consecutive non-advancing iterations):** does not fire.
exp-090 closed PARTIAL with a real, usable deliverable (LOGBOOK's own
characterization). exp-091, independent of how its own findings ultimately
resolve, directly discharges the single oldest undischarged item on the
whole T28 board (the R3 gap on the C40/G40 `PAIR_PAD` channel, flagged
across three consecutive cycles) and produces multiple new, independently
confirmed findings (the sign flip, the caution-zone inversion, the
sigma_max confound). Logbook-advancing by construction, on both criteria's
own texts.

**Criterion 4 (program-integrity drift — unfalsifiable claims, a
constraint quietly dropped, or a "known, named, ignored" rule violation):**
**does not fire.** Worked through every candidate matter individually,
not by inertia:

- **VISION's disclaimer-propagation gap** — ruled non-firing at §2, on two
  independent grounds (new shape, not a fifth instance of the Iteration-65
  lineage; standard discharge test met regardless).
- **The missing `NOTES.md` Result/Learned section** — ruled non-firing at
  §5, matching the exp-080 precedent exactly (same-shift fix, by this
  audit, non-firing).
- **QUANTUM's caution-zone-inversion finding** — this is a genuinely major
  *scientific* correction to a standing LOGBOOK characterization ("sound,
  correctly scoped, now independently reproduced by at least nine
  parties"), but per this program's own explicit design, scientific
  importance alone is not a criterion-4 trigger; the operative question is
  whether it is a "known, named, ignored" instance of an existing rule.
  It is not: the R3 gap was named (MATERIALS, three consecutive cycles)
  and this cycle exists specifically to close it; discovering the sample
  is shakier than believed *by discharging the named gap* is the program
  working as designed, not drift. Caught blind, by QUANTUM's own Phase-5
  review, before any LOGBOOK entry for this cycle — the standard
  discharge condition, met.
- **MATERIALS' sigma_max/graded_black_shell finding** — a genuinely new,
  previously-undiscovered confound, first exercised in this exact cycle
  (per `run.py`'s own docstring: "the first-ever R3-resolution FDTD call
  that also builds the PAIR_PAD article" — `graded_black_shell` has never
  before been run under an R3 rescale by anyone). No prior cycle could have
  named this gap, so there is no "ignored" history to have failed to act
  on. Caught blind, by MATERIALS' own self-review, before any LOGBOOK
  entry — the standard discharge condition, met. This audit's own
  extension of the concern to (a)/(a2)/(b) (§1.2) is likewise a fresh
  finding, disclosed forward as an open item, not a violation.
- **The EM Phase-2 circularity concern "exceeded" by the actual result**
  (§1.3 of EM's review) — this is Phase 2 working correctly (a critique
  correctly diagnosed a real gap; the fix adopted at Phase 3 under-scoped
  the cure's own width relative to what the data then showed) — not a
  known gap left unaddressed. Non-firing, plainly.
- **No LOGBOOK misstatement found anywhere** in this cycle's own record —
  every cited historical figure (the n=7 table, the FLOOR value, the three
  crossing locations, the P-069-5 precedent ratios, exp-089's Learned #4
  figure) reproduces bit-exact against its own primary source, checked
  independently at every phase of this cycle (Phase 2's own audit, the
  Director's synthesis, and this audit, three independent passes).

**No criterion fires.** This is a notification-only ruling under this
program's own unbroken precedent (a Checkpoint firing is a notification,
not a pause) — moot here since nothing fires, but stated for completeness
per PANEL.md's own procedure.

---

## 5. Ruling on the missing NOTES.md Result/Learned section: write it now, same-shift, non-firing — matching the exp-080 precedent

**Ruling: yes, write it now, as part of this audit — matching exp-080's
own precedent exactly** (LOGBOOK Iteration 57: VISION found exp-080 was
missing its `NOTES.md`; Red Team's Phase-5 final audit wrote it same-shift,
non-firing, "the same defect class Iteration 56/exp-078 caught and
closed"). Three of six Phase-5 reviews (PHOTONICS, MATERIALS, QUANTUM)
independently converged on this exact disposition unprompted, and I concur
for the same reasons all three gave: the underlying numbers are correct
and thoroughly re-verified (this audit is the ninth-plus independent
reproduction of this cycle's headline figures); the gap is a completeness
defect in the permanent written record, not a scientific one; and leaving
it open risks a future citation quoting `results.json` numbers (especially
the newsworthy 41.4° flip) without the instrument-calibration-only scope
that governs them, exactly the risk VISION's own "exciting result" section
names as prospective, not yet realized.

**Draft Result and Learned sections below — for the Director to apply to
`NOTES.md` verbatim or edit, citing this audit.** I have not modified
`NOTES.md` myself, per the task's own instruction.

<blockquote>

## Result

**Carried idealizations banner** (mandatory at both this section and the
Predictions section, per the Iteration-65 CHECKPOINT's own escalated,
non-discretionary rule): every finding below is governed by
**Idealizations 3/6/7**: NETD is an instrument/detector threshold, not a
human perceptual one — nothing here bears on constraint-3/4's human-eye
verdict; this cycle does not test constraint 1/2/3/4 and takes no T1
escape-route position (`REALIZABILITY_MEMO.md` untouched, Checkpoint
criterion 2 N/A); `FLOOR`/`RMS[frac_contrast]` are applied, not recomputed,
against the new `cpl=30` numbers — a disclosed mixed-resolution comparison.

All 40 FDTD calls completed; all house gates PASS (`vac_pass`, `xi_pass`,
`nonneg_pass`, all exhaustively checked, not sampled).

- **(a) PRIMARY — REFUTE.** `delta_scene(40.2°)` changes sign between
  cpl=20 (`−1.5427×10⁻⁴`) and cpl=30 (`+4.3699×10⁻⁴`). 37.2°/41.4° hold
  sign but land outside the `[0.3,3.0]` CONFIRM band (ratios 5.21×/4.16×,
  the disclosed NEITHER outcome) — under the pre-registered priority rule,
  the single sign flip alone determines the overall REFUTE.
- **(a2) — REFUTE at both brackets.** Neither `[40.2°,40.4°]` nor
  `[41.4°,41.6°]` shows a sign change at `cpl=30` — both pairs read
  same-signed (positive at both ends). The known `cpl=20` crossings
  (40.2654°, 41.4609°) sit inside both `cpl=20` brackets and are not
  reproduced in either `cpl=30` bracket. **This instrument, as built, can
  say the crossings are not in the tested `±0.2°` windows; it cannot say
  where they went** — two independent, disclosed, non-fatal
  back-of-envelope linear extrapolations (PHOTONICS' and QUANTUM's
  Phase-5 reviews, matching arithmetic) suggest both crossings moved
  further than the tested window, in opposite directions, but this is an
  informal estimate, not a located measurement, and is not adopted as a
  filed result.
- **(b) PRIMARY — mixed, at the single most consequential possible
  outcome the design's own two-sided framing anticipated.** 37.2° stays
  CONSISTENT (`ratio_k`: 3.4641→1.8463). 40.2° stays formally
  ENERGY-DOMINANT (`ratio_k`: 25.0503→10.0744) but clears `RATIO_HIGH=10.0`
  by only **0.74%** under `_label()`'s own strict `>` inequality — a
  razor-thin, not a comfortable, survival. 41.4° **reclassifies**
  (`ratio_k`: 28.8456→9.2116, ENERGY-DOMINANT→CONSISTENT). Neither
  reclassification result was hedged into a default lean by this cycle's
  own pre-registration; both hold/hold and hold/flip outcomes were treated
  as equally informative in advance.
- **(b2) PRIMARY — CONFIRM.** `frac_p_abs` survives `cpl` 20→30 at all
  three angles (ratios 2.78×/1.12×/1.33×, all inside `[0.3,3.0]`, all
  sign-matched) — resolution-robust in the sense this cycle's band tests.
  **Read this as "classification-stable across these two resolutions," not
  "resolution-converged"**: the underlying `p_abs_w` primitive itself grows
  a small, uniform, mechanistically well-understood ~3.5–3.7% at every
  angle (consistent with reduced staircasing of the graded shell's curved
  boundary at finer `Δx` — THERMODYNAMICS' Phase-5 finding, independently
  corroborated by EM and MATERIALS via two further computation routes), not
  scattering around a fixed value — a `cpl=40` check is expected, on this
  reading, to show further growth in the same direction, not oscillation.
  **A separate, currently undischarged open question** (flagged forward,
  not resolved by this cycle): `graded_black_shell`'s `sigma_max` parameter
  was left at its unscaled native default (`0.5`) at both resolutions,
  which by this program's own `τ_center=2·σ·r_out(cells)` convention
  (the T10/SIGMA_ON erratum precedent) means the `cpl=30` article carries
  ~1.5× the native accumulated optical depth, not a strict resolution-
  matched replica. Checked against `p_abs_w` and judged a small (~3.5%),
  not primary, driver there (consistent with an already near-saturated
  absorber, T9's own `σ_abs/σ_ext≈0.51` anchor) — **not yet checked
  against `delta_scene`/`frac_contrast`/`ratio_k`, the PRIMARY channel**,
  since the sigma inflation, while common-mode between `C40_R3`/`G40_R3`,
  could still plausibly shift the shell's own small residual-reflection
  phase and thereby the interference pattern `delta_scene` is built from.
- **(c1)/(c2) — CONFIRM, cleanly.** All six `c1` cells (native-`cpl`
  `STEPS=4200` vs. exp-083's own `STEPS=2800`) and all four `c2` cells
  (R3-resolution `STEPS=6300` vs. `4200`, at both spot-checked angles)
  read relative deviations of `0.0001%`–`0.0138%`, six-plus orders of
  magnitude inside the `≤1%` CONFIRM band. **Settling is independently,
  cleanly ruled out as an explanation for the sign flip or any other
  surprise in this cycle, at either resolution.**
- **(d) — disclosed, non-gating.** The 37.2° `resolved`-gate noise-floor
  margin at `STEPS=4200` is `1.061940×`, against the cited `STEPS=2800`
  figure of `1.045659×` — a genuinely marginal `1.6%` relative increase.
  This is technically relief in the predicted direction but is itself
  still a "felt-lucky," not a robust, margin; the §1 narrative's
  "directly relieving" framing should be read as weakly, not
  substantively, discharged. The R14(a)-style smoothness gate passes
  cleanly across all five `cpl=30` angles, both configs (no non-monotonic
  dip of the R14-founding shape at this cycle's own window). The ordering
  check (`frac_contrast(37.2°)>40.2°>41.4°`) holds at `cpl=20` but **fails**
  at `cpl=30` (40.2° < 41.4°) — a further, independent signature that the
  local `delta_scene(θ)` structure near 40–42° is genuinely reshaped
  between resolutions, not merely phase-shifted in place. **Mandatory
  cross-reference (item 10):** both (a2) brackets returned an
  uninterpretable null (`crossing_cpl30=None` at both), so the requested
  cross-reference against (c2)'s settling residuals cannot be computed as
  specified — this null is itself informative (both crossings left their
  tested windows entirely) but is not a numeric answer to the question
  asked.

**Note on exp-090's caution zone (Idealization 9/11's own named gap, now
discharged for these three points).** Both `Y=1` (ENERGY-DOMINANT) points
in exp-090's own n=7 caution-zone sample — 40.2° and 41.4° — are the two
angles this cycle resolution-tested. Neither survives cleanly: 41.4°
reclassifies outright; 40.2° survives by 0.74% of the threshold's own
value. Relabeling 41.4° per this cycle's own finding **inverts** the
zone's own non-parametric construction (`min{margin:Y=0}=1.3095 <
max{margin:Y=1}=1.4764`) — exactly `exp-090/NOTES.md`'s own pre-registered
Q3 falsification clause ("falsified if... inverted"). **The caution zone
`[1.4764,2.1709]` and Firth's fit `m₅₀=2.071013` should be treated,
from this point forward, as `cpl=20`-specific and provisional — not a
resolution-verified decision boundary — until re-fit** (see
`phase5_redteam_audit.md` §0/§3 for the full arithmetic and the newly
adopted R15).

## Learned

1. **A channel proven to carry a coherent, PAD-driven phase/timing signal
   (not a magnitude/absorption one) is exactly the class of quantity where
   grid refinement can relocate a zero-crossing rather than merely
   rescaling an amplitude** — the sign flip and both bracket REFUTEs are
   consistent with, and arguably the clearest demonstration yet of, this
   program's own T10 precedent (a near-field point-probe channel's
   relative spread growing under `cpl` refinement), now observed on a
   finer intrinsic fringe period and at a larger magnitude than T10's own
   original beam-behind measurement.
2. **A calibration boundary's own floor-gate clearing (R13) does not
   imply its classification is resolution-stable** — both points defining
   exp-090's caution-zone edges cleared `floor_pass=True` at every tested
   resolution while one flipped outright and the other survived by 0.74%.
   This is a genuinely new failure axis, formalized this cycle as R15.
3. **A common-mode construction confound in a shared article does not
   automatically cancel in a config-differential channel** — `sigma_max`'s
   unscaled default under the R3 rescale inflates both `C40_R3`'s and
   `G40_R3`'s optical depth identically, but this cycle did not (and, on
   reflection, structurally could not, without a dedicated sigma-rescaled
   rerun) rule out that this shared inflation still perturbs the
   *difference* signal (`delta_scene`) the pair is built to isolate, via
   the shell's own residual-reflection phase. Flagged forward, not
   resolved.
4. **A record's own printed, human-readable log and its underlying JSON
   are a distinct propagation surface from prose-to-prose caveat
   carry-forward** — this cycle's `netd_disclaimer`/`scope_note` fields
   were correctly written to `results.json` but never printed to
   `run_output.txt`, a gap this sub-thread's four prior disclaimer-erosion
   catches never checked for because none of them involved a
   never-printed field. See `phase5_redteam_audit.md` §2 for the full
   reasoning on why this is ruled a new gap shape, not a fifth instance of
   that lineage.

**Next:** see `phase5_redteam_audit.md` §6 for the full ranked Iteration-69
candidate list, reconciling all six Phase-5 reviews' own top-3s.

</blockquote>

---

## 6. Ranked Iteration-69 candidate list (reconciling all six reviews' top-3s)

**Tier 0 — same-shift, applied by this audit, before this document is
cited:** the Result/Learned section above (§5); R15 adopted (§3); the
Checkpoint ruling recorded (§4); the VISION disclaimer-propagation
question ruled (§2). The Director should additionally record, in the
eventual LOGBOOK entry, the explicit amendment QUANTUM's review names:
Iteration-67's own "sound, correctly scoped" characterization of
exp-090's caution zone needs an explicit qualifier ("cpl=20-specific,
provisional pending re-fit") going forward, not silent inheritance.

**Tier 1 — cheap, near-unanimous across the six reviews (5 of 6 name a
version of this):**

1. **Locate the actual `cpl=30` crossings near 40–42°, with a wider net
   than this cycle's own ±0.2° bracket.** Named by PHOTONICS (#3),
   MATERIALS (#1, a full ~26-call dense re-sweep), ELECTROMAGNETISM (#1,
   extend outward not inward), QUANTUM (Rank 2, extend outward per its
   own extrapolation direction), and VISION (#2). This is the single most
   convergent recommendation in this Phase-5 layer and should rank first:
   it directly resolves the (a2) "REFUTE, location unknown" gap into a
   located measurement, and is the precondition for rebuilding R15's own
   caution zone on resolution-consistent footing.
2. **Rebuild exp-090's caution zone/Firth fit under both the "drop 41.4°"
   and "relabel 41.4° to Y=0" treatments, reported side by side against
   the original — zero FDTD, uses only already-committed data.** Named by
   QUANTUM (Rank 1) and independently recommended in substance by
   PHOTONICS (#2) and MATERIALS (§5). Should run in parallel with item 1,
   not wait on it, since it costs nothing and directly determines whether
   the existing, LOGBOOK-cited zone can still be cited as filed.
3. **The sigma_max R3-rescale check (MATERIALS' §4 proposal), extended
   per this audit's own §1.2/§4 finding to score `delta_scene`/
   `frac_contrast`/`ratio_k`, not only `p_abs_w`/`frac_p_abs`.** Re-run
   `build_article_r3` with `sigma_max=0.5/R3_RATIO≈0.333` explicitly, and
   compare the full (a)/(a2)/(b)/(b2) result set against this cycle's
   as-filed run — 2–4 extra calls, zero change to any other machinery.
   This is the cheapest, most decisive check of whether any fraction of
   this cycle's own PRIMARY headline result (the sign flip, the razor-thin
   40.2° survival) is attributable to the unscaled-sigma confound rather
   than pure grid-resolution physics — currently open on the PRIMARY
   channel specifically, not merely the numerator side MATERIALS itself
   checked.

**Tier 2 — a genuine third resolution point, near-unanimous among the
"physics" seats (EM #3, THERMODYNAMICS #2, QUANTUM Rank 3):**

4. **A `cpl=40` (or `cpl=25`) third resolution point at 40.2°/41.4°
   (and ideally 37.2°),** to distinguish "converging toward a stable
   value" from "still drifting" — a two-point (`cpl=20→30`) comparison
   cannot establish a limit, only a direction, and this is the standard
   `cpl=20/30/40` sequence this program has already used elsewhere (e.g.
   T15). This would upgrade both `frac_p_abs`'s "CONFIRMed at two
   resolutions" status and `frac_contrast`'s own convergence question to
   an actual trend.

**Tier 3 — extend R15's own evidentiary base:**

5. **Extend R3 to the remaining four of exp-090's seven caution-zone
   points** (36.0°, 38.4°, 38.8°, 41.8°) — named by MATERIALS (#3). R15's
   own finding is currently drawn from only 2 of 7 zone-defining points; a
   full accounting needs all seven before the zone is formally re-fit or
   retired under R15's own new discipline.

**Tier 4 — structural/governance, cheap, not urgent:**

6. Persist `sigma_ext_cells`/`ratio_abs_ext_raw` into `results.json` for
   every `thermo`-chain cell going forward on this channel (THERMODYNAMICS
   #1) — zero marginal FDTD cost, closes a real verification gap this
   audit and THERMODYNAMICS' own review both had to work around.
7. The new print-parity/Result-section-existence structural safeguard
   named at §2 (extending VISION's own #3, and Red Team's already-named
   mechanical idealization-citation-parity lint from Iteration 67's board)
   — for whichever seat builds Iteration 69's tooling improvements.

**Still open, standing, unaffected by this cycle** (carried forward
unchanged, per every review's own consistent accounting): PHOTONICS' own
grazing-incidence validity check (still the single most-repeated item on
the whole T28 board); the x-wall wavelength-generality leg (now
sixteen-plus consecutive cycles deferred); the still-queued R14(b) formal
null-controlled period fit against the raw signed `p_abs(G40,θ)−
p_abs(C40,θ)` difference; the Rank-2-in-exp-090's-own-queue unbiased
margin-vs-distance rebuild on the full 31-point window (Q8's own
construction confound, separate from this cycle); the ritualization
governance question (Iteration 61), still unresolved.

---

## 7. Combined Verdict: **PARTIAL**

**Confirmed, cleanly, by this cycle:**
- 37.2° stays CONSISTENT across `cpl` 20→30 — the one census angle with no
  crossing-proximity complication, exactly as predicted.
- `frac_p_abs`/(b2) is resolution-robust (CONFIRM) at all three census
  angles — a genuine methodological win discharging a real, previously
  untested R14-numerator gap — though it should be read as
  "classification-stable across these two resolutions," not
  "resolution-converged" (THERMODYNAMICS' correctly-qualified reading),
  and is not yet shown fully clean of the sigma_max confound on the
  PRIMARY (`delta_scene`) side.
- Settling adequacy at both resolutions (c1/c2), cleanly, across all ten
  checked cells — under-settling is independently ruled out as an
  explanation for anything else this cycle found.
- All house gates pass, exhaustively, not sampled; no geometry-rescale
  defect found in the article's own radii (independently verified from
  source by three seats plus this audit).

**Materially revised by this cycle:**
- **exp-090's caution zone `[1.4764,2.1709]` and Firth's fit
  `m₅₀=2.071013`**, previously characterized in LOGBOOK as "sound,
  correctly scoped, and now independently reproduced by at least nine
  parties," must now be treated as **`cpl=20`-specific and provisional**,
  not a resolution-verified decision boundary. Both `Y=1`-class points
  defining the zone's foundation failed this program's own first
  resolution check on this channel — one outright reclassifying, one
  surviving by a margin (0.74%) an order of magnitude thinner than
  anything the zone itself was built to resolve — and relabeling per this
  cycle's own data inverts the zone's own non-parametric construction,
  triggering exp-090's own pre-registered falsification clause under the
  relabeled reading. This is a real, program-standing methodological
  correction, formalized as new standing rule R15.

**Genuinely new, undischarged, load-bearing gap surfaced (not yet
resolved either way):**
- `graded_black_shell`'s `sigma_max` was left at its unscaled native
  default under the R3 rescale — independently confirmed from source code
  by this audit — inflating the R3 article's accumulated optical depth by
  ~1.5× relative to native, by this program's own established
  τ_center-scaling convention. Checked and judged small on the absorbed-
  power side (~3.5%, consistent with near-saturated absorption) but
  **not yet checked against the PRIMARY channel** (`delta_scene`/
  `frac_contrast`/`ratio_k`) that this cycle's own headline sign flip and
  reclassification are built on. This audit extends MATERIALS' own
  scoping and flags it, unresolved, as this cycle's single most
  consequential open question, on par with (not superseded by) the
  crossing-relocation question.

**Also genuinely, but only partially, answered:**
- (a)/(a2) formally REFUTE — the sign flip and both bracket non-crossings
  are real, correctly computed, and independently reconfirmed by every
  seat and this audit. But the true `cpl=30` location of both crossings
  remains **unlocated** (not "shifted a little" — outside both tested
  ±0.2° windows, in opposite directions), so this cycle answers "is the
  cpl=20 reading resolution-stable" (no) without yet answering "where did
  it go."

**Process:** a real record-hygiene gap (`NOTES.md`'s missing Result/
Learned section, and `run_output.txt`'s never-printed disclaimers) —
closed same-shift by this audit (§5), matching the exp-080 precedent; and
a newly-identified, distinct disclaimer-propagation gap shape (§2), ruled
non-firing on two independent grounds. **No Checkpoint criterion fires**
(§4, worked through all five explicitly). Not RULED OUT (no mechanism
class is engaged or foreclosed; T1 route N/A throughout, correctly) and
not PROMISING (no constraint-metric progress is claimed, correctly, by
this cycle's own scope) — PARTIAL is the correct characterization, and a
materially information-dense one: this cycle both confirmed a real
methodological win (the numerator-side R14 discipline holding up under
resolution) and delivered the most consequential single correction to a
standing LOGBOOK-cited deliverable (exp-090's caution zone) that this T28
sub-thread has produced since R13/R14's own founding cycles — while
opening, not closing, two genuinely new questions (the crossings' true
location; the sigma_max confound's effect on the PRIMARY channel) that
Iteration 69 should treat as its own top priorities.

Full record: `experiments/091-t28-r3-resolution-denser-recheck/` —
`phase1_proposal.md`, five Phase-2 blind critiques, `phase2_redteam_
audit.md`, `phase3_synthesis.md`, `NOTES.md` (Result/Learned drafted at
§5 above, for the Director to apply), `run.py`/`results.json`/
`run_output.txt`, six Phase-5 blind reviews, this document.
