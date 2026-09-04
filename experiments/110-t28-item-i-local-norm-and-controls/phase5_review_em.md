# PHASE 5 — REVIEW · ELECTROMAGNETISM (SELF-REVIEW) · Panel Iteration 87 (exp-110)

*Fresh context, no memory of authoring the Phase-1 proposal — read as a
document to audit adversarially, per this program's own R4/R9/R18
precedent for self-review cycles (Iteration 85/PHOTONICS, Iteration
86/MATERIALS). Read in full before writing: PANEL.md; LOGBOOK.md (RULED
OUT R1–R26; T28 Iterations 83–86, exp-106/107/108/109); every file in
`experiments/110-t28-item-i-local-norm-and-controls/`; `lab/validation/
run_all.py` lines 2698–2825 (stage26 including Gate 3). No other seat's
Phase-5 output seen.*

## 0. Charter framing

ELECTROMAGNETISM owns reciprocity/passivity/causality bookkeeping and
formalizes what T1 permits/forbids. T1 is N/A this cycle (confirmed
independently below, §1) — the charter's live-thread duty is not engaged.
Per the Director's brief for this self-review, I instead audit (a) my own
Phase-1 proposal's central physical claim (the mirror-symmetry premise),
(b) the cost-gate bookkeeping math built into this cycle's own code
(`cost_gate_check()`), (c) whether Phase 2's 8 mandatory fixes actually
landed, and (d) whether the grounding-fact/persistence finding genuinely
closes the gap it claims to.

---

## 1. Re-derivation: `CY = N/2` mirror-symmetry proof, independently,
## from `geom_fixedabs`'s own source, at both r

The Phase-1 proposal (§1, Item 1) asserted "this bench is mirror-symmetric
about the propagation axis" **without showing the algebra** — a real gap
in my own original document, only closed by PHOTONICS' Phase-2 critique,
which read `geom_fixedabs()`/`add_line_source` directly rather than take
my prose on faith. Re-derived here independently again, not by citing
PHOTONICS' or Red Team's write-up:

**Geometry.** `run.py::geom_fixedabs(r)`: `N0=560`, `CY0=280` (module
constants), `k = kappa_of(r) = r/78`, `N = round(N0*k)`, `CX = round(CX0*k)`,
`CY = round(CY0*k)`. Since `CY0/N0 = 280/560 = 1/2` exactly, and both `N`
and `CY` are scaled by the identical `k`, `CY = N/2` holds whenever the
rounding is exact. I ran this directly rather than trust the arithmetic on
paper:

```
r=156: k=2.0 -> N=1120, CY=560,  CY==N/2 -> True
r=312: k=4.0 -> N=2240, CY=1120, CY==N/2 -> True
```

`k` is exactly `2.0`/`4.0` at both r (integer `R_BASE=78` divides `156`/`312`
evenly), so `round(N0*k)`/`round(CY0*k)` involve no rounding error at all —
this is exact arithmetic, not an approximation that happens to round
favorably.

**Source symmetry.** `add_line_source`'s default span is `y_lo=self.absorb`,
`y_hi=self.ny-self.absorb` — read directly from `lab/fdtd2d.py`. Midpoint
`= (absorb + (ny-absorb))/2 = ny/2 = N/2 = CY` exactly, with an identical
tapered-edge window (`edge` cells) applied at both ends — a genuine
full-width, `y`-symmetric plane wave centered exactly on `CY`, not a beam
offset from it.

**Box/circle symmetry.** Every circle (`hypot(x-CX, y-CY)`) and every
`margin_box`/`box_a`/`box_b`/`ref` is built from `CY±(half-width)` —
manifestly even under `y -> 2*CY - y`.

**Conclusion, re-derived independently: `pattern[i] = pattern[47-i]` is
forced by geometry + source + box construction in the noiseless/
exact-grid-symmetry limit, at both r.** This is the premise
`classify_item_i_local`'s floor gate needs, and it holds. I confirm
PHOTONICS' and Red Team's Phase-2 re-derivations (`phase2_critique_
photonics.md` §Verification, `phase2_redteam_audit.md` §1.1) exactly, by
independent computation from source rather than by citation.

**Self-critique, standing:** the original Phase-1 proposal should have
shown this arithmetic itself — asserting a physical symmetry premise
without deriving it from the actual construction is exactly the discipline
R18/R9 exist to enforce, and it was only luck (a genuinely correct
assertion) that saved this cycle from an RT-3-grade "inconsistency" attack
on the premise itself, rather than only on its downstream mislabeling
(RT-3 fired on the R13/R14 discharge claim instead, a related but
different defect — see §3 below).

---

## 2. Audit: the R27 cost-gate math (`run.py::cost_gate_check()`)

### 2.1 The formula as built

```python
kappa_ratio = kappa_of(312) / kappa_of(156)          # = 2.0
projected_312_total_s = pilot_total_wall_s * (kappa_ratio ** 3)
```

The physical justification (per-step cost ~ grid area `N^2` (2D domain,
`N` scales linearly with `k`) times step count (`STEPS0*k`, also linear in
`k`) => total cost ~ `k^3`) is dimensionally sound and I re-derive it the
same way independently: `N` and `STEPS` both scale by the identical `k`
in `geom_fixedabs`, so a pure grid-and-step-count accounting gives exactly
`kappa_ratio**3` between any two `r` in this family. **This is a
physically motivated estimate, not an arbitrary guess** — but "physically
motivated" and "empirically validated" are different claims, and the
run.py docstring's own "checked... as a sanity bound, not a hard
derivation" language does not distinguish them. What was actually checked
before this cycle's own Phase 4 (per the docstring) is that this cycle's
**total** 6-call wall time (128.17 min) is close to exp-108's own
historical **total** (128.5 min) — a check that the re-capture reproduces
a prior aggregate spend, not a check that the `kappa^3` **scaling law
between r=156 and r=312 specifically** is accurate. Those are different
claims, and only the first was ever validated before this cycle.

### 2.2 The check the task asks for: does real data now support or
### contradict the formula?

This cycle is the first time real timing data exists at both r for this
exact family (`results.json`, both committed and independently re-read
by me):

| Scene | r=156 (s) | r=312 (s) | actual ratio | `kappa_ratio**3`=8.0 predicts |
|---|---|---|---|---|
| empty | 250.627 | 2334.842 | **9.316×** | 8.0× |
| hollow | 250.083 | 2232.955 | **8.929×** | 8.0× |
| peccored | 251.513 | 2370.409 | **9.425×** | 8.0× |
| **combined total** | 752.223 | 6938.207 | **9.224×** | **8.0×** |

Recomputed directly from `results.json`'s own persisted `total_wall_s`
dicts, both r — not read from any narrated figure.

**Verdict: the real ratio CONTRADICTS the formula's accuracy, though not
its functional form.** The actual r=312/r=156 ratio (9.22×, per-scene
range 8.93×–9.42×) sits **consistently above** the projected 8.0× at
every one of the three scenes — not scattered around it, which would look
like noise, but uniformly high, which looks like a systematic effect the
formula omits. Solving for the effective exponent (`ratio =
kappa_ratio**x`) gives `x ≈ 3.16–3.24` per scene (`3.21` combined), not
`3.00` — real FDTD cost at this domain-size jump grows measurably faster
than pure area-times-steps accounting predicts (plausibly: reduced
cache/memory-bandwidth efficiency on the larger `N=2240` arrays, `numpy`
overhead structure, or non-`N^2`-scaling components in `full_capture`/
phasor extraction — not investigated further here, out of this cycle's
own scope).

**Is this outcome-reversing this cycle? No** — checked directly: using
the ACTUAL 6938.207s in place of the formula's projected 6017.786s, both
sit comfortably under `COST_GATE_TOTAL_S=10800s` (180 min) — the real
number uses 64.2% of budget vs. the projected number's 55.7%, a real
~8.5-point shrink in headroom (44.3% → 35.8%), but `total_pass` would
still have evaluated `True` under the real figure. **Is it disclosed
anywhere in the frozen document? No** — grepped `NOTES.md` and every `.py`
file in this directory for the actual/projected comparison, the effective
exponent, or any acknowledgment that real r=312 data now exists to check
the formula against: zero hits. Nothing in the Result section states this
comparison, despite item 1a's own re-capture being exactly the data
needed to run it.

**This is a real, previously-uncaught, non-outcome-reversing gap.** It
could not have been caught at Phase 2 (no real r=312 timing existed yet)
or by the Director's own Phase-3/Phase-4 layers (the formula's own
docstring frames it as a disclosed estimate, and no step in `analyze.py`/
`finalize.py` ever re-derives the comparison once the data exists) — it
is a genuine Phase-5-only finding, exactly the kind this cycle's own task
brief flagged as newly possible. **The formula is anti-conservative in
the wrong direction for a safety gate**: a projection that under-predicts
true cost by a consistent ~15% (12–18% per scene) gives false confidence
precisely when the gate is meant to be protective. Non-blocking here only
because of a wide (44%/36%) margin that has nothing to do with the
formula's own accuracy — a future cycle at a different `kappa_ratio`
(untested: this formula has only ever been exercised at the one fixed
`kappa_ratio=2.0` this r-family produces) or a tighter `COST_GATE_TOTAL_S`
could receive a false "proceed" from this exact code path.

**Recommendation, Iteration-88 queue:** disclose the ~15%/`x≈3.2`
empirical finding in this document's own Idealizations (same-shift
annotation, R4-convention); apply an explicit empirical safety margin
(e.g. multiply the projection by ~1.2× or use the measured exponent
rather than the assumed one) before this gate is relied upon at a smaller
headroom; note that `kappa_ratio**3` remains untested at any `kappa_ratio`
other than `2.0`.

---

## 3. Verification: did all 8 mandatory fixes actually land?

Checked against the committed source, not against NOTES.md's own claim
table alone (R18 discipline — a claimed disposition must be confirmed
against actual code/text, line-by-line).

| # | Fix | Claimed disposition | Independently verified |
|---|---|---|---|
| 1 | Pool the mirror-floor statistic (median, within-margin, 24 bin-pairs) | Implemented, `mirror_pooled_floor()` | **Confirmed** — `run.py:288-307`: `pairs = |pattern[i]-pattern[n-1-i]|/2` over `n//2=24` pairs, `np.percentile(pairs, 50)`. `classify_item_i_local` calls it once per pattern per margin (`floor_p`, `floor_h`), not per-bin — matches Fix 1's spec exactly. |
| 2 | Disclose common-mode blindness; split Iteration-88 fault-injection into (a)/(b) | Disclosed in `DISCLAIMER`; queued as (a)/(b) | **Confirmed** — `DISCLAIMER` (`run.py:376-382`) states the bias explicitly; NOTES.md Idealizations lists "(a) an injected ASYMMETRIC... (b) an injected SYMMETRIC/common-mode..." as separate numbered sub-items. |
| 3 | "Discharges R13 and R14" → "discharges R13 only" | Implemented, docstring + NOTES.md | **Confirmed in code** — `classify_item_i_local`'s docstring (`run.py:314-318`): "Discharges R13... ONLY -- NOT R14." **Minor gap**: NOTES.md's own prose never restates this correction as a standalone sentence outside the Fix-table row (line 76) — the claim "this NOTES.md" in that row overstates NOTES.md's own narrative discharge slightly; the code fix itself is real and correct. |
| 4 | Discretization-vs-fabrication-tolerance disclaimer | Implemented in `DISCLAIMER` | **Confirmed** — `DISCLAIMER` states the floor "characterizes grid-discretization/floating-point noise for the IDEALIZED simulated geometry ONLY" and licenses no fabrication-tolerance inference, verbatim. |
| 5 | Wire `COST_GATE_*` as executable code | Implemented, `cost_gate_check()` | **Confirmed wired and called** (`analyze.py:106`, gates the r=312 attempt) — see §2 above for a substantive audit of the formula itself, a distinct question from whether it is code-enforced (it is). |
| 6 | Distinguish this cycle's new wall time from exp-108's historical 7712.0s via `wall_time_source` | Implemented | **Confirmed** — `finalize.py:65-76` builds an explicit `wall_time_source` string with this cycle's own 7690.4s and per-scene breakdown, passed into `build_result_text`; appears verbatim in the committed `result_text` (independently diffed, below). |
| 7 | Bind Phase 3/4 to `build_predictions_text`/`build_result_text`, assert `DISCLAIMER in` both, persist both, NOTES.md quotes `result_text` verbatim | Implemented | **Confirmed, byte-exact.** Re-ran the diff myself: `results.json["predictions_text"]` and `["result_text"]` match NOTES.md's own quoted blocks **character-for-character** (Python string equality, both blocks, both directions) — not merely "consistent," identical. Both `assert DISCLAIMER in ...` calls exist in `finalize.py:86-87` and print "BOTH PASSED." |
| 8 | State bin counts clearing/failing K=3, and the two named bins' disposition, in Result prose | Committed to, reported after Phase 4 | **Confirmed** — Result text states `203/288`/`222/288` and both named bins' `UNRESOLVED-BY-CONSTRUCTION` status explicitly; independently recomputed from `results.json`'s own `n_resolved`/`n_total`/`named_bin_status` fields and reproduces exactly (203/288, 222/288, both bins `resolved=False`). |

**All 8 mandatory fixes genuinely landed in committed code, not merely
claimed** — the one asterisk (Fix 3's NOTES.md-narration half) is cosmetic
and non-outcome-reversing, not a fresh R18/R24 instance (the code
itself is correct; only the fix-table's own attribution of "and this
NOTES.md" is mildly generous).

Also independently re-verified, not part of the numbered 8: `gate_p0`
(exact, zero mismatches, both r), `reproduction_precondition` (`rel_dev=
0.0` exactly, both r, both `sigma_abs`/`sigma_ext` — a stronger result
than the predicted `<1e-9` bound), item 2's four synthetic cases (bit-exact
against my own independent invocation of `linear_fit_1_over_margin`), and
`stage26`'s Gate 3 (re-ran `python3 lab/validation/run_all.py --only 26`
myself: `3/3`, `rel_diff_truncated=1.999`, matching NOTES.md exactly).

---

## 4. Confirmation: does the re-capture genuinely close the grounding-fact gap?

Independently re-read `results.json` directly (not trusting NOTES.md's
own persistence claim): `raw_patterns` exists for **all 6 margins**
(`24,32,40,48,57,65`), **both r** (`r156`/`r312`), with `peccored`/
`hollow`/`delta` each a full 48-element array — `6 margins × 3 arrays × 2
r = 36` arrays, `48` floats each, `1728` floats total, exactly matching
the proposal's own predicted count. Zero gaps, zero margins skipped.

`results.json` and its parent directory are committed to git (`git log`:
`e59aa03` "Phase 4 complete", clean working tree, no uncommitted
diff) — this is not a scratch artifact that could vanish the way
exp-108's own pickles did. **A future cycle can recompute `local_diag` at
any `K`/percentile, re-derive `classify_item_i`'s own `rel32`, or build an
entirely new local-normalization statistic directly from this committed
JSON, with zero new `Sim.run()` calls.** The specific failure mode this
cycle exists to close (a prior cycle's in-memory-only intermediate data
vanishing with its ephemeral scratch session) cannot recur on this
channel — the persisted arrays are the actual field-derived numbers, not
a derived summary statistic that would need to be recomputed from raw
fields to answer a differently-scoped question.

One caveat, correctly disclosed by the document itself and confirmed here
independently: `raw_patterns` persists the **post-processing** (per-bin
Poynting flux), not the raw field captures (`ez`/`hx`/`hy`/`sigma_e`)
themselves — those remain ephemeral, in this session's own scratchpad
(`chunk_runner.py`'s `SCRATCH`), matching the pattern that created this
cycle's own grounding-fact finding. A future cycle wanting a genuinely
different per-bin quantity not derivable from `pattern_{peccored,
hollow,delta}` (e.g. a differently-defined angular sample, or per-bin
phase rather than flux magnitude) would still need a fresh FDTD capture —
correctly scoped as "closes local-normalization analysis on THIS
instrument's output," not "closes all future field-level analysis."
NOTES.md does not overclaim this distinction, and neither did I find it
overclaimed anywhere in the document.

---

## 5. Verdict on the Combined Verdict claim

NOTES.md's own Director synthesis states **Combined Verdict: PROMISING**.

**My verdict: CONFIRM-WITH-GAPS**, not a clean CONFIRM, and I do not
adopt "PROMISING" without qualification.

**What stands, independently re-verified, not merely re-read:**
- The `CY=N/2` mirror-symmetry premise is genuinely, exactly true at both
  r (§1) — the strongest-grounded instrument this sub-thread has built.
- All 8 mandatory fixes are genuinely implemented in code, not merely
  claimed (§3) — a clean record, matching exp-108's own "clean six-of-six"
  precedent rather than exp-109's "dangling cross-reference" one.
- R23 is genuinely, byte-exact honored (§3, Fix 7) — the strongest
  verification of this specific compliance question this document family
  has produced (character-for-character equality, not merely "verbatim by
  inspection").
- The grounding-fact/persistence gap is genuinely, permanently closed
  (§4) — a future cycle will not need to re-run FDTD for local-
  normalization analysis on this instrument's own output.
- Every predicted outcome held; nothing was falsified.

**What is a genuine gap, first found here:**
- The R27 cost-gate formula (`kappa_ratio**3`) is now shown, by data that
  did not exist when either the proposal or the Phase-2/3 layers wrote
  it, to be a consistent ~15% (per-scene 12–18%) **underestimate** of the
  true cost-scaling ratio — anti-conservative for a safety gate,
  non-outcome-reversing this cycle only by margin, and undisclosed
  anywhere in the frozen document despite this cycle's own data being
  sufficient to compute it (§2).
- Fix 3's own claimed NOTES.md-narration half is mildly overstated (§3) —
  cosmetic, non-outcome-reversing.

Neither gap changes any scored outcome this cycle (T1 remains correctly
N/A; all four falsifiable predictions held; the cost gate's own pass/fail
decision would not have flipped under the true figure). Per this
program's own precedent (a real, disclosed-but-incomplete finding that
does not reverse an outcome does not on its own warrant PARTIAL, but does
disqualify an unqualified PROMISING/CONFIRM) — **CONFIRM-WITH-GAPS** is
the accurate label. I flag the R27 finding for Red Team's own Phase-5
final audit to weigh against Checkpoint criteria; it is not, on my own
charter's authority, mine to rule on. It is not, in my own reading,
`R17`-shaped in the strict textual sense (R17 concerns a tolerance/bracket
sized to test feature presence; this concerns a cost-projection formula's
own accuracy) — more likely a candidate founding instance of a
genuinely new, narrower shape ("a numeric projection formula, now
code-enforced per R27, whose own accuracy was never checked against
real data once such data existed") — a judgment call for Red Team, not
asserted as a ruling here.

---

## 6. Ranked top-3 candidate directions for Iteration 88

1. **Disclose and correct the R27 cost-gate formula's empirical bias**
   (§2, this review). Cheap: annotate NOTES.md same-shift with the
   ~15%/`x≈3.2` finding (R4 convention — annotate, don't silently
   rewrite); apply a disclosed safety multiplier or measured exponent to
   `cost_gate_check()` before the next cycle that relies on it at a
   tighter margin. Zero new FDTD.

2. **PHOTONICS' own independent, non-differencing floor check** (already
   queued, Iteration-88 item (i) per Red Team's Phase-2 audit) — a
   `cpl`-refinement spot check at the two named bins (−146.25°/r=156,
   +168.75°/r=312), the only instrument that can distinguish "genuine
   common-mode-masked structure" from "pure grid noise" at exactly the
   two bins this cycle's own K=3 gate left open (§4's own caveat, Fix 2's
   disclosed blind spot). Genuinely new FDTD work, correctly deferred
   this cycle, now the most load-bearing open question on this specific
   channel.

3. **The split symmetric/asymmetric fault-injection control for
   `mirror_pooled_floor`/`classify_item_i_local`** (Fix 2's own deferred
   remedy, R25-discipline-named as its own Iteration-88 line item) — a
   zero-FDTD, synthetic positive/negative control confirming the floor
   correctly flags an injected asymmetric perturbation and correctly does
   NOT flag an injected symmetric/common-mode one. Cheap, closes the one
   structural gap (RT-1) this cycle's Fix 1 pooling could not reach,
   independent of item 2's own already-existing (but differently-scoped)
   `linear_fit_1_over_margin` control.

*(Standing queue items I do not re-rank above but note remain live and
untouched by this review: `R2_SMOOTH_THRESHOLD=0.90` re-derivation, a
fourth r-point r=624, the oblique-angle/750-450nm/`G40`/x-wall/`PAD`
items, `box_dev`'s own thinning margin, and Tier-0 item 0 — the
Iteration-85 Checkpoint-4/R24 ruling, still Marsh's call, still pending.)*
