# Phase 2 — blind critique: VISION SCIENCE

**Cycle:** Panel Iteration 92, candidate exp-115
(`115-t28-r234-grid-native-control-and-fab-tolerance`).
**Seat:** VISION SCIENCE. **Blind** to all other seats' current-cycle output.
**Repo state read:** `main @ ead61b6`.

---

## 1. Steel-man (≤150 words)

The identity `measured_ratio ≡ kappa_ratio × G` is real and load-bearing. I
reproduced it bit-exact from exp-114's own primitives
(`1.5 × 2.74550565394726 = 4.11825848092089`, the filed value to all 15
digits), and it genuinely reframes exp-114's verdict: what was scored as a
cross-session cost ratio *is* a single-session per-step ratio between two
grids. Measuring it directly is right, and is the queue's own Tier-1 #1.
The grep showing no control burst was ever timed on any grid but r=156 is a
real not-previously-run check.
Running three-scene blends on **both** legs repairs the empty-scene-vs-blend
incommensurability Red Team found inside the v2 straddle. M5 states its
REFUTE boundary in the measured quantity itself (`G ≤ 1.7117383` or
`≥ 3.1789426`) — the human-checkability standard my seat asks for and
rarely gets. Item 5 pays a seven-cycle debt at zero FDTD cost and states
the realizability tier it does **not** move.

*(147 words.)*

---

## 2. Sharpest attack (≤150 words)

M9(d) — the one sentence R21 pushes into Result prose and every future
citation — carries two independent defects.

**(i)** "better than `1.6×10⁻⁴` … 48 angular bins, **six box radii**" is
certified at margin=32 only. exp-108 persists `rel32` alone; the other five
margins are certified solely by the boolean `confirm_all_margins`, whose bar
is `ITEM_I_CONFIRM_REL = 0.05` — **330× looser**. §2.0 line 104 says exactly
this, in this document; line 497 then contradicts it. R4's second addendum
forbids an aggregate flag certifying an "every single X" claim.

**(ii)** M9(c) compares `exp(−2·τ_true) = 6.71e−8`, a **round-trip intensity**
ratio, against relative changes in cross-sections whose leading
core-dependent term is the interference cross-term — **linear** in the
returned amplitude, `e^−τ_true = 2.59e−4`, the same order as the measured
`1.09e−4`. On the commensurable power, (c) predicts a *resolved* effect, not
a floor.

*(137 words.)*

---

## 3. Verdict

**support-with-changes.**

The cycle should run. Item 1 is the right measurement, correctly sequenced,
honestly costed, and its primary band is checkable by hand. My objections are
to what gets *written down* and quoted forward, and to one missing guard on
the primary metric.

**The single change that would flip me to plain `support`:**

> Restate M9(d) at the resolution its evidence actually certifies —
> *"≤ 1.53×10⁻⁴ at margin = 32 across 48 bins at r = 156 and r = 312; ≤ 5%
> (the `confirm_all_margins` decision bar) at the other five box radii;
> aggregate-ledger channels only at r = 234"* — **and** either re-derive
> M9(c) in the commensurable (amplitude) power or withdraw it, since as
> written it is the sole ground for calling the measurement "floor-limited."

**Second change, near-equal weight (a guard, not a wording fix):** wire an
`M3 → M5` composition rule symmetric with the one M6 already has. M5 is the
PRIMARY metric and the only one that can move a filed LOGBOOK verdict, yet it
is the only ratio metric in §5 with **no** protocol caveat attached (§5 lines
322–349 vs. §5 lines 366–372). See Appendix item 4.

---

## 4. Appendix — derivations, re-derivations, and rule findings

Every figure below was produced by executing code or reading committed JSON
this session. Where I could not reproduce a figure, I say so.

### 4.1 — Figures I re-derived and CONFIRM

1. **`measured_ratio ≡ kappa_ratio × G`** (proposal §1, §2.0 row 3).
   From `experiments/114-.../results.json`:
   `t234_cpl25 = 7038.29048371315`, `/36000 = 0.19550806899203194`;
   `r31_control.sustained.this_session_per_step_s = 0.07121022268191168`;
   `G_E = 2.74550565394726`; `1.5 × G_E = 4.11825848092089` =
   `kappa_exponent_result.measured_ratio` to all 15 digits. **Bit-exact.**
   The proposal's claim that every cross-session term cancels is correct:
   `36000/24000 = 1.5` only because `STEPS` scales linearly with `kappa` —
   a coincidence of construction that the proposal states and I confirm.

2. **`k`, `G_ref`, `reference_ratio`.** `KAPPA_COST_EXPONENT =
   3.2053299988171697`; `1.5**k = 3.6680107109370383` (= filed
   `reference_ratio`); `1.5**(k−1) = 2.4453404739580256 = reference_ratio/1.5`.
   **Identical.**

3. **M5's stated boundaries** (proposal lines 339–340). From
   `run114.classify_kappa_exponent_check` (`run114.py:258–281`),
   `rel_dev = |measured − reference|/reference`, `CONFIRM ≤ 0.15`,
   `REFUTE ≥ 0.30`. Dividing by 1.5: CONFIRM `G ∈ [2.0785394028643216,
   2.812141545051729]`; REFUTE `G ≤ 1.7117383317706178` or
   `≥ 3.178942616145433`. **Reproduces to 7 dp as printed.** This is the
   single best piece of human-facing writing in the proposal.

4. **`R_DEG`** (line ~99). `0.07121022268191168/0.06618270341555277 − 1 =
   0.07596424755863729`. **Exact.**

5. **M7's arithmetic.** `ε(2.0) = 2**(k−3) = 1.152950039837078`;
   constant-ε prediction `2.25 × ε = 2.5941375896334256`; model separation
   `2.5941376/2.4453405 − 1 = 0.060849242573798756` (proposal: 6.085% ✓);
   `ε_E(1.5) = G_E/2.25 = 1.2202247350876712`; distance to constant-ε
   `0.05835005240998958` (✓ 5.835%); to constant-k `0.12274985147707773`
   (✓ 12.275%). **All exact.**

6. **M8's two sensitivities.** `short` reading: `speed_ratio =
   0.422112913224623` (filed). v2: `measured_ratio = 3.2171956285212335`,
   signed dev `−0.12290452`, spread vs. original `(4.11826−3.21720)/3.21720
   = 0.28008` (✓ 28.0%). **Matches `phase5_redteam_audit.md` §2 exactly.**

7. **exp-108 per-bin figures** (`experiments/108-.../results.json`):
   `max(rel32) = 1.4760284822434646e-04` (r=156),
   `1.5265673604659632e-04` (r=312), `confirm_all_margins = True`, 48 bins
   each, verdict CONFIRM. **Exact.**

8. **Sidecar ledger deltas.** Recomputed from
   `experiments/112-.../results.json` and `experiments/114-.../results.json`
   `energy_ledger`. All six quoted figures reproduce **only** under a
   symmetric mean normalization `|h−p| / ((h+p)/2)`:
   r=156 σ_scat `8.359387007873527e-05`, σ_abs `4.084328355450674e-05`,
   σ_ext `2.146912588710513e-05`; r=234 σ_scat `1.0873544930288214e-04`,
   σ_abs `5.666217924972678e-06`, σ_ext `5.20438064401917e-05`. **Exact to
   every quoted digit.** (See 4.10 for the disclosure gap this exposes.)

9. **Floor-gate range.** `8.359387e-05/6.6495e-06 = 12.57`;
   `5.666218e-06/2.7794e-05 = 0.2039`. **"0.2×–12.6×" confirmed.**

10. **`exp(−2·τ_true)`.** `exp(−16.517639659373354) = 6.708e−08`.
    **Confirmed** (proposal: `6.71e-08`).

11. **`τ_shell` and physical thickness.** `experiments/108-.../run.py:52–53`:
    `ABS_THICKNESS = 48`, `SIGMA_MAX_FIXED = 0.5`, `CPL_600 = 20` →
    `τ_shell = 24.0`, `48 × 30 nm = 1.440 µm`. cpl=25 family: `60 × 24 nm =
    1.440 µm`, `0.4 × 60 = 24.0`. **The thickness-invariance claim in M9(d)
    holds.** (Note the σ_max difference, 0.5 vs 0.4 — correctly disclosed as
    Idealization 9.)

12. **Tier arithmetic.** `100/1.44 = 69.4`, `500/1.44 = 347` (✓ "70–350×");
    `OD = 8.2588/ln(10) = 3.5867` (✓ 3.587); `1/5.7353e4 cm = 174.4 nm`
    (✓ e-fold). **All confirmed.**

### 4.2 — FINDING 1 (primary): M9(d) certifies five of six box radii from an aggregate boolean — R4, second addendum

`experiments/108-.../run.py:244–254` computes `confirm_all_margins` as a
single boolean over `MARGINS = (24, 32, 40, 48, 57, 65)`, set `False` on the
first bin anywhere exceeding `ITEM_I_CONFIRM_REL = 0.05`. Only
`rel32` — the margin=32 array — is persisted (`results.json`
`tier1.r{156,312}.item_i.rel32`, 48 entries; I enumerated the keys and
confirmed no other margin's array exists).

The proposal itself states this correctly at **line 104**. Line **497** then
writes the tight figure across "48 angular bins, six box radii." The
certified statement is:

- margin = 32: `≤ 1.5265673604659632e-04` (measured, per-bin array on file);
- margins 24/40/48/57/65: `≤ 0.05` (a decision bar, boolean-certified).

That is a **330× gap** — the proposal's own number. R4's second addendum
(LOGBOOK.md lines ~82–96) is explicit: *"an aggregate flag or a mean/range
table is not sufficient to certify an 'every single X' claim — the resolution
the claim is made at … must be independently checked."* Red Team's own
Iteration-92 queue item 5 (`phase5_redteam_audit.md` §7 Tier 1 item 5)
characterises the available evidence as *"48-bin angular check ≤5% at
r=156/312"* — the looser figure. M9(d) silently upgrades it.

This matters more than a normal citation slip because R21 requires M9(d) to
be quoted verbatim into Result prose, and MATERIALS explicitly wrote it *"to
be quoted there"* (§8, line ~714). A defect frozen into that sentence
propagates by design.

**Also inside the same sentence:** "two grid resolutions (cpl 20 and 25)" and
"48 angular bins" do not co-occur. The per-bin channel is cpl=20 / σ_max=0.5
only (exp-108); the aggregate channels are cpl=25 / σ_max=0.4 only
(exp-112/114). Idealization 7 discloses the radius factorisation but not the
resolution factorisation.

### 4.3 — FINDING 2: M9(c) is not dimensionally commensurable with M9(b) — R9

`τ_true` is an **intensity** optical depth: `α_true × t = 5.7353×10⁴ cm⁻¹ ×
1.44×10⁻⁴ cm = 8.259`, and `OD = τ/ln10 = 3.587` is a decadic *intensity*
density. Therefore:

- one-way intensity transmission `e^−τ = 2.59×10⁻⁴`;
- **round-trip field amplitude** `e^−τ_true = 2.59×10⁻⁴`;
- round-trip intensity `e^−2τ_true = 6.71×10⁻⁸` (the proposal's figure).

The measured quantities in M9(b) are **relative changes in cross-sections**
between a vacuum core and a PEC core. Writing the far-field scattered
amplitude as `A_main + A_core`, `σ_scat ∝ |A_main|² + 2·Re(A_main A_core*) +
|A_core|²`. The core-dependent change is dominated by the **cross term**,
which is linear in `|A_core|/|A_main| ~ e^−τ_true ≈ 2.6×10⁻⁴` — not by
`|A_core|²/|A_main|² = e^−2τ_true = 6.7×10⁻⁸`. Nothing here is stochastic:
this is a deterministic steady-state FDTD field, so the two contributions
interfere coherently and the cross term does not average away.

`2.6×10⁻⁴` is within a factor of ~2.4 of the largest measured delta
(`1.087×10⁻⁴`, r=234 σ_scat). So the correctly-powered version of (c) is
**consistent with the deltas being a genuine, resolved core signature**, and
is not evidence that (b) is floor-limited. The proposal draws the opposite
conclusion at line 476 (*"fully consistent with (b)'s reading that the
measurement is floor-limited"*), and (b)'s "upper bound, not a resolved
measurement" reading at lines 462–470 rests on it.

This is R9's exact shape: the arithmetic of (c) reproduces (I confirmed it,
item 10 above); the **operands' commensurability** does not. R9's own text —
*"reproducing the division is necessary, not sufficient"* — was founded on a
VISION-adjacent dimensional error of the same family (`amp_ratio` vs.
`C_thr`, LOGBOOK T16 correction, Iteration 54).

I do not claim the geometric prefactor: PHOTONICS/EM own the angular and
near-tangent-chord factors, and Idealization 8 already notes tangent chords
are *longer* (which pushes the estimate down, not up). What I claim is the
**power**: `e^−2τ` is the wrong exponent for a quantity whose leading term is
an interference cross-term, and the conclusion the sidecar draws from it
inverts under correction.

**Consequence for M9's own HALT design:** M9's stated falsifiable element is
an arithmetic-reproduction gate to `<1e-12`. That gate would pass on a
figure that is off by 3.6 orders of magnitude in its *interpretation*. A
reproduction gate cannot catch a power error; only a stated derivation can.

### 4.4 — FINDING 3: M5, the PRIMARY metric, has no composition rule; M6 does

§5 gives composition rules to M3 (gated on M4, lines 313–320), M6 (gated on
M3, lines 366–372) and M7 (its own power condition, line 402). **M5 has
none** (lines 322–349).

Yet M5 substitutes a `3334`-steps/scene control-burst `G` for exp-114's
`12000`-steps/scene production numerator, and asserts this means *"the
protocol mismatch removed by design"* (line 333). The mismatch is not
removed — it is moved to the other side of the comparison. The reference it
is scored against, `1.5**k`, is a model of **production** cost.

If M3 reads `DOES-NOT-CANCEL`, the cycle will have *measured* that duration
does not divide out of `G`, and M5's numerator is then known not to represent
the production quantity — but M5 is still scored, and per line 344 it can
*"move the filed verdict to AMBIGUOUS"* and force a LOGBOOK re-framing.

There is a second, R17-flavoured problem with the M5 REFUTE branch's label:
*"`KAPPA_COST_EXPONENT` is not portable to `kappa_ratio = 1.5`."* An equally
live hypothesis — that `k` is not portable from `3334`-step bursts to
`12000`-step production — is available, is exactly what M3 exists to test,
and is not named on that branch. R17's founding lesson (LOGBOOK ~lines
662–740) is precisely that a FAIL branch's pre-registered interpretive label
must give equal weight to the instrument-side explanation *unless a named
test has actually discriminated them*.

Note also the **span** issue: M3 tests `1000 → 3334` (3.33×). The
extrapolation M5 needs is `3334 → 12000` (3.60× further, and unanchored). A
clean `CANCELS` at M3 does not license the M5 framing over the larger,
untested span; it is suggestive, not sufficient. Under R17 that span
mismatch should be stated before the run, not after.

**Minimum fix:** if M3 ∈ {`DOES-NOT-CANCEL`, `PARTIAL`} or M3 is
`UNINTERPRETABLE`, persist `m5_protocol_caveat = True` and report M5 as a
**bounded replication**, not a verdict that can move exp-114's LOGBOOK
entry. Code it, per R24.

### 4.5 — FINDING 4: M4's three labels hide two consequential thresholds — legibility

`d_rep` carries **four** distinct cut points but only **three** labels:

| `d_rep` | label | silent consequence |
|---|---|---|
| ≤ 0.02 | REPEATABLE | — |
| 0.02–0.03 | MARGINAL | — |
| **0.03**–0.0379821 | MARGINAL | **M7 model comparison → `UNDERPOWERED`** (line 402) |
| **0.0379821**–0.0759642 | MARGINAL | **M3 → `UNINTERPRETABLE`, no M3 verdict** (line 316) |
| ≥ 0.0759642 | NOISY | both of the above |

A human reading "M4: MARGINAL" in a Result section cannot tell whether M3 was
scored or voided. This is the same class of defect R21 exists to close
(persisted ≠ narrated) one level up: here the *label itself* is
under-resolved. **Cheap fix:** split MARGINAL into three named buckets at
`0.03` and `R_DEG/2`, so the label carries the consequence.

### 4.6 — FINDING 5: M7's `AMBIGUOUS` bucket is where the in-force model actually lives

Computed from the committed constants:

- `excess` predicted by the **in-force** constant-`k` model:
  `2.4453404739580256/2.25 − 1 = 0.08681798842578914` → falls in
  **`AMBIGUOUS`** (0.05 < 0.0868 < 0.15295).
- `excess` predicted by the **constant-ε** model:
  `2.25 × 2**(k−3)/2.25 − 1 = 0.152950039837078` → this is **exactly the
  `N2_FAILS` bar** (`0.1529500`), exceeding it by `4.0×10⁻⁸`.

So: (a) if `KAPPA_COST_EXPONENT` is exactly right, M7 reports `AMBIGUOUS` —
a label a human reader will take as "no information," when it is in fact the
in-force model's own point prediction; (b) the alternative model sits on a
knife-edge of the `N2_FAILS` boundary, and which side it lands on depends on
how many digits the code carries. Neither candidate model can produce
`N2_HOLDS`; that outcome requires **both** to be wrong.

None of this is hidden dishonestly — it falls straight out of the proposal's
own numbers — but a reader cannot see it from the table as written. **Fix:**
annotate the M7 table with each model's predicted `excess`, and rename
`AMBIGUOUS` (e.g. `CONSISTENT-WITH-CONSTANT-k`).

Related, and worth stating: M7's secondary comparison is **not independent of
M5**. `ε_E/ε_k ≡ G_E/G_ref ≡ measured_ratio/reference_ratio`, so the "12.275%"
in line ~408 is *numerically identical* to exp-114's filed `rel_dev =
0.12274985147707763`. A CONFIRM at M5 and a "constant-k looks weaker" reading
at M7 are one datum wearing two hats. The proposal should say so.

### 4.7 — FINDING 6: M5's stated invocation does not type-check against the committed function — R18

Line 324–326: *"scored by importing and invoking
`run114.classify_kappa_exponent_check()` **unmodified**"*, with the input
given as `measured_ratio_B = 1.5 × G_sustained`.

`run114.py:258` — `def classify_kappa_exponent_check(exponent_234,
kappa_ratio=KAPPA_RATIO_234_156)` — takes an **exponent**, and derives
`measured_ratio = kappa_ratio ** exponent_234` internally (line 268). Passing
the ratio where the exponent belongs is executable and silently wrong:

```
1.5 ** 4.11825848092089 = 5.311159219494333
rel_dev = |5.311159 − 3.668011| / 3.668011 = 0.44796720567305326  →  REFUTE
```

A plausible-looking REFUTE from a transcription that the proposal's own text
invites. exp-114 did it correctly (`phase5_review_vision.md` lines 84–92:
`exponent_234 = ln(t234/t156_adj)/ln(1.5)`, then classify), so the intent is
clear — but the log-inversion step is nowhere in this document. R18 requires a
check's documented scope to be confirmed against its actual source before it
is relied on. **Fix (one line):** state
`exponent_B = ln(1.5 × G_sustained)/ln(1.5)`, then
`classify_kappa_exponent_check(exponent_B)`, and code-assert
`abs(result["measured_ratio"] − 1.5*G_sustained) < 1e-12`.

### 4.8 — FINDING 7: R23's human-readable half — the caveat registry is warning and nothing is failing

I executed `python lab/caveat_lint.py` this session. It emits **seven WARNs
against this proposal** and **exits 0**:

```
WARN  trigger 'P-10'      → phase1_proposal.md   [exp060-p10-fresnel-not-diffraction]
WARN  trigger 'tau_shell' → phase1_proposal.md   [exp052-alpha-60nm-absorptivity-open]
WARN  trigger 'T23'       → phase1_proposal.md   [exp064-length-provenance-disclosure]
WARN  trigger 'T28'       → phase1_proposal.md   [exp065-steps1400-unsettled-plane-channel]
WARN  trigger 'e-fold'    → phase1_proposal.md   [exp063-alpha-true-efold-staleness]
WARN  trigger 'T28'       → phase1_proposal.md   [exp070-t28-named-constant-null-control]
WARN  trigger 'T28'       → phase1_proposal.md   [exp071-t28-absorb-pad-confound-...]
15 caveat(s) checked, 0 required-site failure(s).
```

Triage, honestly:

- `P-10` is a **false positive** — the regex `P-10` matches inside `exp-105`.
- The three `T28` WARNs are, in substance, satisfied or not applicable: the
  proposal cites `≈233/234` **with** its R5-addendum rejection (line ~700),
  and does not cite the exp-069/071 headline figures at all.
- **`exp052-alpha-60nm-absorptivity-open` is substantively live.** Its text:
  *"Every site that cites this number MUST disclose that the absorptivity
  question, not just the thickness question, remains open."* M9(e) does the
  opposite — line 520 says the bound leaves *"thickness as the binding
  constraint it already was."* None of the three required phrases appears.
- **`exp063-alpha-true-efold-staleness` is live**: the proposal cites `e-fold
  174.36 nm` and `τ_true = 8.2588` (line 107) with no corrected-framing
  phrase.

**Two silent-blindness findings, both executed and reproducible:**

1. `exp061-t18-evidentiary-tier-propagation` — the entry that has fired
   Checkpoint criterion 4 **twice in one iteration** — does **not** fire on
   this document, because *none* of its three triggers matches:
   - `PUBLISHED.{0,10}PLAUSIBLE.{0,10}UNOBTANIUM` misses line 509's
     *"published / plausible / **unobtainium**-with-parameters"*: the trigger
     is spelled **UNOBTANIUM**, PANEL.md line 57 (and this proposal) spell it
     **unobtainium**. A one-letter divergence between the registry and the
     charter.
   - `alpha.{0,15}(…5\.73|5\.74)` misses `α_true = 5.7353×10⁴ cm⁻¹` — the
     trigger is ASCII `alpha`, the document uses Unicode `α`.
   I verified both directly (`re.search(..., re.I)` → `False`; the
   lower-cased-spelling variant → `True`).
2. Even had it fired, the tool would have **PASSED** the document, because
   `T18` appears at line 535 — 428 lines after the verdict restatement at
   line 107. The entry's own requirement is *"AT THE VERDICT ITSELF, not only
   in a general methodology section elsewhere in the same document,"* which
   is document-scoped-untestable by this tool. **Line 107 restates exp-061's
   `UNOBTANIUM-WITH-PARAMETERS` verdict plus its literature figures
   (100–500 µm CNT forests, MP-2/MP-4 CONFIRMED) with zero T18 disclosure at
   that row** — the exact founding shape of that registry entry
   (*"stated the tier in its search-plan and Idealizations sections but NOT
   at the specific table rows a Phase-4 verdict is actually cited from"*).

**And the standing gap:** `lab/caveat_lint_config.json` holds **15** entries,
the newest founded at exp-071 (Iteration 48). **Forty-three subsequent
experiments (exp-072 → exp-114) have added zero entries**, across which
R23-First-Addendum and R30–R33 were all adopted. The proposal names
`DISCLAIMER_115` exactly once (line 719) and **never states its text**, and
proposes **no** registry entry for the new fabrication-tolerance claim.

`lab/ARTIFACTS.md` states the invariant this program already wrote for
itself: *"a silent gate and an absent gate produce identical observations."*
A lint that WARNs seven times and exits 0 is that gate.

**Recommended, cheap, this cycle:** (a) add a `caveat_lint_config.json` entry
for the exp-115 tolerance bound, with the certified-resolution wording from
§3 as its required phrase — R23's own single-source-of-truth principle
applied to the claim this cycle creates; (b) fix the two blindnesses above
(spelling alternation, Unicode `α`); (c) state `DISCLAIMER_115`'s text in the
proposal so Phase 2 can review the caveat, not just its variable name.

### 4.9 — FINDING 8: constraint-3 drift, and the metrics table — the Director's question, answered

**Answered plainly: this proposal does not keep constraint 3 from slipping.
It is scrupulously honest about that, and it slips anyway.**

Verified this session, not restated:

- `lab/ambient.py`'s Weber-contrast entry points (`weber`,
  `contrast_from_runs`, `observer_profile`) were **last invoked by any
  experiment at exp-100** (Iteration 77). `grep -rln "weber(\|
  contrast_from_runs\|observer_profile" experiments/*/*.py` returns
  exp-087, 088, 089, 091, 098, 100 — nothing after. **exp-101 → exp-114 is
  fourteen consecutive cycles with no constraint-3 number; exp-115 would be
  the fifteenth.**
- PANEL.md's Metrics table (lines 138–151) is unamended and still reads
  *"Metrics — recorded every run"* and *"Both ambient regimes are recorded
  every run."* This proposal records **zero of the seven rows**. Not one.
- The de facto amendment lives in a per-cycle `DISCLAIMER` string
  (`run114.py:301–306`: *"No … Weber-contrast or C_thr(L) perceptual
  scoring, is performed anywhere in this document"*), which I traced to
  **fourteen** files across exp-103 → exp-114. A disclaimer repeated fourteen
  times is a policy; it belongs in PANEL.md, where a human reading the
  charter would find it. As it stands, PANEL.md promises a reader a
  constraint-3 number on every run and has not delivered one for fifteen
  cycles.

**My own charter duty this cycle is vacuous**, and that is the diagnosis, not
an excuse: *"Duty: pin numeric thresholds, with sources, BEFORE any run that
scores against them."* There is nothing to pin. There has been nothing to pin
for fifteen cycles.

**On the specific decline (§3 item 6).** The proposal declines Tier-3 item 10
— my seat's re-score of the program's only-ever Tier-W/Tier-A constraint-3
citation, unrun since Iteration 12 — and gives the reason as *"this cycle
executes the queue in its own Tier order."* Red Team's own queue
(`phase5_redteam_audit.md` §7, Tier 3 item 10) is explicit that it is ranked
below Tier 1/2 *"not because this item matters less"*, and calls it *"the
single highest-value NEW-territory move available."* The proposal quotes that
framing and then applies Tier order as though it were binding. **Tier order
is the mechanism by which constraint 3 slips.** An item ranked low for cost
reasons, deferred by an ordering rule, in a queue regenerated every cycle
from the previous cycle's residuals, will never be reached: each cycle's
Tier-1 is manufactured by the cycle before it.

I am **not** asking exp-115 to run item 10 instead of item 1. Item 1 is
cheap, is the right measurement, and I support it. I am asking for one
sentence of Director-level bookkeeping that the proposal itself invites
(*"flagged again, deliberately, so it does not decay into furniture"*, line
~247): **a stated commitment that item 10 is Iteration 93's lead, or an
explicit on-the-record Director decision to keep deferring it** — the same
standard Red Team applied to item 5 (*"An eighth silent cycle should not
happen without an explicit Director decision to keep deferring, stated as
such"*). Item 5 got that treatment after seven cycles and is being paid this
cycle. Item 10 is at eighty.

**Would I fire Checkpoint criterion 4 on this?** Not on this proposal — it
discloses every one of these facts about itself, which is the opposite of
drift-by-concealment. But criterion 4's own trigger language is *"a
constraint quietly dropped — especially #3,"* and a charter clause that has
been contradicted by fourteen consecutive cycles without ever being amended
is, structurally, quiet. That is a program-level finding for the Director and
Red Team, not a reason to block this cycle.

### 4.10 — Smaller findings (checkability)

1. **Undisclosed, non-uniform normalization conventions in the M9(a)/(b)
   table.** The six deltas reproduce **only** under a symmetric-mean
   denominator; the two self-consistency floors reproduce **only** under the
   `peccored` scene (r=156: `/peccored = 6.649462e-06` → quoted `6.6495e-06`;
   `/hollow = 6.649320e-06` → would round to `6.6493e-06`. r=234:
   `/peccored = 2.7793671e-05` → quoted `2.7794e-05`; `/hollow =
   2.7792225e-05` → `2.7792e-05`). Neither convention is stated. So the
   headline R13 floor-gate ratio, `0.2×–12.6×`, mixes a mean-normalized
   numerator with a `peccored`-normalized denominator. **The numbers are
   right; a reader cannot reproduce them without guessing twice.** One
   sentence of formula fixes it.

2. **"three orders of magnitude below anything this instrument can
   resolve"** (line ~476) is off by one order against the tightest floor on
   the same table: `6.708e−08 / 6.649e−06 = 0.01009` — **exactly two
   orders**. It is ~3.4 orders below the largest *measured delta*, but a
   delta is not a resolution limit. (This is separate from, and much smaller
   than, Finding 2.)

3. **"82% of the way to its upper edge"** (line 343) is measured from the
   *reference*, not from the window's lower edge. From the CONFIRM window's
   lower edge, `G_E` sits at **90.9%**
   (`(2.7455057−2.0785394)/(2.8121415−2.0785394)`). The 82% figure is
   `rel_dev/0.15 = 0.8183`. Both are defensible; the sentence does not say
   which, and they differ by 9 points on the reader's sense of margin.

4. **M6's R17 anchor is from a different axis.** `0.15295` is R28's own
   cost-*exponent* founding miss at `kappa_ratio = 2.0`. M6 measures
   **cross-machine transfer** of a memory-hierarchy superlinearity. R17
   requires the anchor be *"the largest already-established cross-resolution
   (or cross-condition) shift magnitude on file for a comparable
   transition"*; no cross-machine magnitude exists on file at all (the
   proposal says so: *"This bench has no measured per-step FDTD rate for
   either grid"*). The nearest established cross-session magnitude is R31's
   own founding `2.19×`. The anchor should be labelled as **an analogy, not
   a comparable-transition anchor** — the labelling R17 was founded to
   require.

5. **PANEL.md Phase-4 house gate, new machinery.** `chunk_runner115.py`
   parameterises `r` in `_time_control_blend`, which PANEL.md's
   *"new machinery ⇒ new suite stage with at least one absolute identity
   gate BEFORE results are trusted"* arguably reaches. §2.0's
   `--verify-geometry` check certifies the **geometry**, not the **timing
   harness**. **Cheap discharge:** assert that
   `_time_control_blend_115(156)` constructs a scene set identical to
   `chunk_runner114._time_control_blend()` — an absolute identity gate on the
   r=156 branch, which the cycle runs anyway (readings 1/3/5).

6. **`DISCLAIMER_115` is named but never written** (line 719). Phase 2 cannot
   review a caveat string it has not been shown. R23's First Addendum
   requires both asserts in the same cycle; a Phase-2 seat can only verify
   that if the text exists.

### 4.11 — On the assigned question: is the sidecar's "removes substrate control" claim stated with the tier it does NOT change?

**Yes — and this is genuinely well done.** M9(e) states
`UNOBTANIUM-WITH-PARAMETERS — inherited unchanged, and this finding does not
move it`, names the binding axis (thickness, 70–350×), states the T18
evidentiary tier, and forward-states the two conditionals as conditionals.
§4 independently states that the article *fails constraint 3 by
construction*. That is the right structure and I do not want it weakened.

Three qualifications:

- **"at all" is stronger than the evidence.** The measured perturbation is
  vacuum → PEC at one λ, normal incidence, 2D TM. Those are two extremes of
  one axis; they do not bracket a resonant or dispersive dielectric core, nor
  any interface roughness or gap. The generic argument that *would* cover an
  arbitrary passive core is M9(c) — which is the one Finding 2 disputes. So
  the strongest form of the claim currently rests on the weakest of its three
  legs. Recommend: *"…does not need to control the core/backing material over
  the vacuum-to-PEC range tested"*, and let (c), once re-derived, do the
  generalising.
- **The tier disclosure does not travel.** R21 will pull M9(d) into Result
  prose; M9(d) does **not** contain the tier, the constraint-3 caveat, or the
  T18 sourcing tier — those live in (e) and §4. The one sentence built to be
  quoted is the one sentence stripped of its qualifiers. See Finding 7's
  recommendation (a).
- **`exp052-alpha-60nm-absorptivity-open` bites here specifically.** M9(e)'s
  framing — thickness is *"the binding constraint it already was"* — is
  precisely what that registry entry exists to prevent, because the
  absorptivity half has never been checked against a primary CNT-forest
  absorption coefficient. A tolerance bound that removes one fabrication
  constraint should not, in the same paragraph, imply the remaining
  constraint list is settled.

---

## 5. What I am NOT objecting to

For the record, so the Director can see where I decline to attack:

- The **cost gate design** (§6) is R27/R28-correct: executable, branching,
  causally upstream of each `Sim.run()`, with the degradation branch spending
  the *repeat* rather than the *primary*. That is the right ordering.
- **R33 inapplicability by construction** for M5 is correctly argued, not
  evaded: no scored operand mixes sessions. M6 is honestly labelled
  cross-machine.
- The **declined-items list** (§3) is R25-compliant — seven numbered lines,
  each with a stated reason, including item 3's genuinely new reason (the
  exp-114 r=234 captures were never committed).
- **Idealization 5** (pickle I/O excluded from both sides, verified by direct
  read of `chunk_runner114.py::step_budgeted`) is exactly the kind of check
  that usually goes unowned. Credit.
- The proposal's **self-flagged uncertainty** (§8, closing paragraph — whether
  a minutes-long burst can represent a multi-hour thermal soak) is real, is
  correctly identified as the weakest joint, and is what Finding 3 (§4.4)
  formalises into a coded rule rather than a flagged worry.

---

*VISION SCIENCE, Panel Iteration 92, Phase 2. Blind. No sub-agents. No git
state changed. No simulations run; arithmetic checks executed against
committed JSON and committed source only.*
