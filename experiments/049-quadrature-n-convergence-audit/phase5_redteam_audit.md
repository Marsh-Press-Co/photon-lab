# PHASE 5 — RED TEAM AUDIT · Panel Iteration 26 · exp-049 (final)

*Seventh seat, speaking last, with the full cycle record and all six blind
Phase-5 reviews. Standard: internal consistency, falsifiability,
expressibility, constraint violations — not textbook compliance. Red Team
never trusts a seat's prose, including its own: every load-bearing claim
below was re-derived from source in this session — `results.json`, `run.py`,
`NOTES.md`, and `git log`/`git show`/`git diff` on the actual commits — before
being accepted, whether it came from PHOTONICS, THERMODYNAMICS, or anyone
else.*

---

## 0. Headline

Six blind seats converged on two real, independently-caught defects, both
instances of this program's own named fix-docket-delivery pattern and its
R4 house rule (adopted one cycle ago, Iteration 25, for the identical
species of defect). I independently reconfirm both from source, **and find
a third thing none of the six caught: the fabricated "321" figure has
already propagated into two of the six Phase-5 review documents' own
proposed corrections to LOGBOOK** — meaning if the Director had copied
either MATERIALS' or ELECTROMAGNETISM's "corrections to propagate" text
verbatim, the wrong number would have re-entered the permanent record a
second time, in the very act of fixing it. Neither defect is load-bearing to
any of the eleven scored predictions. Checkpoint criterion 4 does **not**
fire, contingent on the same-shift mandatory fixes below — but this is the
**second** consecutive violation of the rule adopted specifically to stop
this defect class, and I am hardening the standing remedy accordingly (§5).

---

## 1. PHOTONICS' "321 is fabricated" finding — CONFIRMED, independently re-derived

I scanned `results.json`'s `per_cell_summary` directly (108 records, one
per cell-function combination):

```
max(nstar) across all 108 cell-function combinations = 81
Counter of nstar values, pooled: {41: 92, 81: 16}
```

Per function:

| func | max n* | Counter |
|---|---|---|
| `incoherent` | 81 | `{41: 33, 81: 3}` |
| `incoherent_corrected` | 81 | `{41: 31, 81: 5}` |
| `coherent` | 81 | `{41: 28, 81: 8}` |

**The number 321 never occurs as an n\* value anywhere in the 108-row
table, for any function, at any FWHM.** The five `incoherent_corrected`/
FWHM=20° cells with n\*>41 — (450nm,36°), (450nm,38°), (450nm,40°),
(600nm,38°), (750nm,38°) — all read **n\*=81**, exactly matching the "5 of
9" count NOTES.md's own P-NCONV26-1b row correctly reports. `321` is one of
eight entries in `N_SERIES = (41, 81, 161, 321, 641, 1281, 2561, 5121)` —
the most plausible mechanical origin of the error is a slipped index into
that tuple (the 4th entry) rather than the actual measured value (the 2nd
entry), but I find no code path anywhere in `run.py` that could produce 321
for this comparison, and PHOTONICS' review states the same. This is not
fabricated from nothing — the underlying computation (5/9 cells needing
n\*>41) is correct — but the specific numeral attached to it is wrong by a
factor of 4×, in the one sentence of this document written as forward
guidance for a future cycle.

**The true, correct practical-conclusion sentence, verified against
`results.json` directly (not against any seat's prose):**

> Net practical conclusion: n=41 is safe everywhere except the FWHM=20°
> regime, where the coherent function needs n\*≥81 at 8 of 9 cells and the
> incoherent_corrected function needs n\*=81 at 5 of 9 cells (measured, not
> the heuristic's own {641,1281} guess) — the global maximum n\* across the
> entire 108-cell-function grid is 81; no cell-function combination anywhere
> in this audit ever needs n\*=161, 321, 641, 1281, 2561, or 5121.

**A finding none of the six blind seats made**: this exact fabricated
number has already spread past NOTES.md. `phase5_review_materials.md`
("...needing up to n\*=321 at 5/9 FWHM=20° cells) now measured, not...")
and `phase5_review_em.md` ("...need `n\*` up to 321 (measured, not the
Phase-1 heuristic's feared 641–1281)...", inside EM's own §"Corrections
this seat asks the Director to propagate to LOGBOOK at close") both repeat
the error uncritically — in the same two documents that elsewhere describe
independently re-deriving other numbers from raw code. Neither seat
appears to have run the one-line scan of `per_cell_summary` that would have
caught it (PHOTONICS did; QUANTUM's and THERMODYNAMICS' reviews never cite
a specific n\* figure for this cell set, so they neither repeat nor catch
it; VISION's and my own Phase-2 audit's scope never touch it). This is a
live instance of exactly the propagation risk R4 was written to prevent:
an unverified figure, once stated with apparent authority in NOTES.md,
gets copied forward into independent review documents without a source
check, including into text explicitly framed as "for the permanent
record." **Mandatory: the Director must use PHOTONICS' corrected n\*=81
figure when writing the LOGBOOK.md close-out entry — not MATERIALS' or
EM's proposed text, both of which still carry the fabricated 321.**

---

## 2. THERMODYNAMICS' "no code path" finding — CONFIRMED, traced to the exact commit

I read `run.py` end-to-end (388 lines) and grepped for `ERRATUM`/`BUGGY`:
the only hit is the docstring comment at line 70 documenting the bug in
prose. `main()`'s `results` dict (lines 337–370) has no key or code path
that computes or writes `meta.phase4_erratum` or
`predictions.P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY`. Both fields are present
in the committed `results.json` (confirmed by direct `json.load`):

```
meta keys include: ..., 'phase4_erratum'
predictions keys include: ..., 'P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY'
```

I then ran `git show --stat e5c32b1` (the results commit) and
`git diff 7699de5 e5c32b1 -- run.py` (the Phase-4-implementation commit vs.
the results commit) directly. **The only code change to `run.py` between
those two commits is the one-line rank-formula fix** (`{cell: i+1 ...}` →
`{cell: n-i ...}`) plus the docstring expansion documenting the bug in
prose. No erratum-preservation code was ever added, run, and stripped — it
was never there. `results.json`'s two erratum fields were therefore hand-
inserted directly into the results commit, not produced by any script in
the repository. **A fresh `python run.py` today would silently drop both
fields** (`json.dump(..., mode="w")` overwrites the whole file from
`main()`'s in-memory `results` dict, which has no such keys).

I independently re-derived what the buggy computation would actually
produce, by directly calling the unmodified
`experiments/042-t21-magnitude-bridge/design_geometry.py` functions with
the *buggy* rank formula (`{cell: i+1 for i, cell in enumerate(order)}`,
i.e. rank 1 → hardest) reconstructed from `run.py`'s own docstring
description of the original bug:

```
incoherent            rho = -0.48333333333333334  p = 0.18746985521554216
incoherent_corrected  rho = -0.4666666666666666   p = 0.2053863511058121
coherent              rho = -0.45                 p = 0.22421610749233675
```

This is a **bit-exact match** to `results.json`'s
`P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` block. **Verdict: the disclosed
numbers are genuine — they are what the actual buggy code, run against the
actual committed `design_geometry.py`, actually produced — not invented.
But the artifact is not currently reproducible from the committed `run.py`
as a single `python run.py` invocation**, which is the exact standard R4
sets ("MUST be produced by invoking the actual committed function... never
hand-typed, however simple the arithmetic looks"). This is a real, if
low-severity (values verified correct, non-load-bearing, internally
self-consistent — exact sign-negation, identical p-values, exactly as EM's
and QUANTUM's independent reviews also found), instance of the exact
defect class R4 exists to catch, landing one cycle after R4 was adopted for
precisely this shape of problem.

---

## 3. Checkpoint criterion 4 — explicit ruling

**Does NOT fire, contingent on the same-shift mandatory fixes in §4/§5
below.** Reasoning, weighed against this program's own precedent:

- Neither defect is unfalsifiable — both were caught by direct
  falsification against `results.json`/`run.py`, by six independent fresh
  contexts, using nothing but the committed artifacts. That is the
  falsification machinery working, not failing.
- Neither touches constraint-3/4 or any T1 escape route — this cycle
  declares "T1 escape route: NONE" and every seat, including this one,
  confirmed no mechanism, material, or perceptual claim appears anywhere
  in `run.py`, `NOTES.md`, or `results.json`.
- Neither is load-bearing to any of the eleven scored predictions.
  P-NCONV26-1b's PARTIAL verdict is scored off the correct 5/9 count, not
  off "321"; P-NCONV26-2's PARTIAL verdict (ρ=0.45–0.48, all three
  functions) is unaffected by the erratum-block's reproducibility gap —
  the *corrected* computation that actually ships and is scored was
  independently re-derived from raw code by four separate seats (PHOTONICS,
  MATERIALS, EM, QUANTUM) and matches exactly.
- Both are cheap, same-shift, code-and-prose-only fixes with no new FDTD
  calls and no re-scoring of any prediction — matching the exact shape
  this program has repeatedly ruled non-firing under (Iterations 19, 22,
  25: "does NOT fire, contingent on same-shift fixes").

**What makes this cycle worth naming plainly, not waving through
routinely**: this is the **second** cycle in a row (25, 26) to carry a
real instance of the exact defect class R4 was adopted, one cycle ago, to
stop — and it recurred in the very next cycle, in the document meant to be
this program's cleanest instrument-fidelity audit to date (five of six
blind seats and this Red Team's own Phase-2 audit found essentially no
other defect of any kind). A house rule that fails its own first real test
is a program-integrity signal worth escalating even when no individual
instance clears the bar for an automatic fire. I am not overriding the
program's own established non-firing precedent for this shape of defect —
doing so here, on a non-load-bearing, cleanly-disclosed, cheaply-fixed pair
of findings, would be inconsistent with Iterations 19/22/25 without new
grounds. But I am hardening the standing remedy in §5, in the same style
this program used for the QUANTUM aperture-check tripwire at Iteration 22:
a specific, numbered, automatic condition, not another round of prose
admonition.

---

## 4. Hunt for what the six blind seats collectively missed

Beyond the "321"-propagation finding in §1 (the one genuinely new catch),
I checked for anything else. Two smaller items, both already surfaced by
individual seats and independently reconfirmed here, neither new:

- **QUANTUM's `converged_value` semantics gap** (real, cheap, non-blocking):
  `per_cell_summary`'s `converged_value` field is `values[n*]` — the value
  at the smallest N_SERIES entry passing two consecutive doublings — not
  the series' true `n=5121` asymptote. I confirmed QUANTUM's own example
  cell (450nm/38°/FWHM=20°, `incoherent_corrected`): `converged_value =
  -1.8825e-04` at n*=81, while the true asymptotic value (n=5121) is
  `-1.599e-05`, over an order of magnitude apart in relative terms (though
  the absolute gap, `1.72e-4`, stays under `ABS_TOL` — no headline is
  threatened). Worth a one-line docstring fix.
- **VISION's T24-caveat propagation gap** (real, cheap, non-blocking):
  confirmed by direct grep — `results.json` has zero occurrences of "T24"
  anywhere in the file, and NOTES.md's Results-table P-NCONV26-5 row omits
  the caveat present in the predictions-table row two sections above it.

I found no third new defect beyond the "321"-propagation issue after
independently re-checking: the regression gate (§1 of PHOTONICS' and
THERMODYNAMICS' reviews — reproduces exactly), the sign-erratum fix itself
(reproduces exactly, confirmed algebraically by EM and numerically by
myself in §2 above), the completeness ledger (972/972, confirmed by direct
arithmetic on `CELLS`/`FUNCS`/`N_SERIES`), and the `REALIZABILITY_MEMO.md`
non-interaction (confirmed by grep: zero occurrences of
`beam_divergence`/`gaussian_angle_weights` in that file). This is a
genuinely well-executed cycle outside the two named defects.

---

## 5. Hardened rule (new, program-level)

Per this program's own Iteration-22 precedent (the QUANTUM aperture-check
tripwire), I am converting the "worth naming plainly" observation in §3
into a specific, numbered, automatic condition rather than leaving it as
prose:

**If a third consecutive post-R4 cycle (i.e., any cycle after this one)
carries a headline or practical-conclusion figure that does not
independently reproduce from `results.json`/the committed code when a
Phase-5 seat checks it, Checkpoint criterion 4 fires automatically —
no further debate, no seat vote, no Director discretion.** This cycle
(26) and the one before it (25, R4's own origin) are the two data points;
a third strike closes the discretion this ruling extends here.

**Process recommendation, not a blocking gate**: any sentence in a
NOTES.md Results/Reading section that states a specific numeral as a
practical takeaway (the shape "X needs n\*/value up to N") should be
generated by a `print()`/`assert` in the scoring script itself and pasted
verbatim, not composed by hand from a table read — the exact discipline
`run.py`'s own `p0_pass` assertion already applies to P-NCONV26-0. This
would have mechanically prevented both of this cycle's defects.

---

## 6. Mandatory-fix docket

All items below are same-shift, zero-new-FDTD, non-load-bearing to any
scored prediction. Ordered by the Director's brief (NOTES.md corrections,
run.py reproducibility, then the smaller propagation-gap items).

**1. [Mandatory, load-bearing to future citations] Correct NOTES.md's
"Net practical conclusion" sentence** (Results section, immediately after
the outcomes table). Replace:

> "**Net practical conclusion: n=41 is safe everywhere except the FWHM=20°
> regime, where the coherent function specifically needs n\*≥81 (measured,
> not the heuristic's own {641,1281} guess) and the incoherent_corrected
> function needs n\* up to 321 at 5 of 9 cells** (see `results.json`
> `per_cell_summary` for the exact per-cell n\* table)."

with:

> "**Net practical conclusion: n=41 is safe everywhere except the FWHM=20°
> regime, where the coherent function needs n\*≥81 at 8 of 9 cells and the
> incoherent_corrected function needs n\*=81 at 5 of 9 cells (measured, not
> the heuristic's own {641,1281} guess) — the global maximum n\* across the
> entire 108-cell-function grid is 81; no cell-function combination
> anywhere in this audit ever needs n\*=161, 321, 641, 1281, 2561, or
> 5121** (see `results.json` `per_cell_summary` for the exact per-cell n\*
> table)."

**2. [Mandatory] Close the reproducibility gap in `run.py`.** Consistent
with this program's own precedent for this defect class (T10/exp-042's
`erratum.py` — a real, invocable code path that computes the disclosed
erratum content, added alongside the original committed function, not a
wholesale re-run of the experiment from scratch; exp-043's relocate-and-
guard precedent for a different erratum shape) — **add code, do not
regenerate `results.json` from scratch.** Add to `run.py`, immediately
after `predicted_difficulty_rank()`:

```python
def predicted_difficulty_rank_ORIGINAL_BUGGY():
    """The original (buggy) rank formula, preserved verbatim for
    reproducibility of the disclosed Phase-4 runtime erratum -- DO NOT
    USE for scoring. rank 1 = hardest (ascending), which inverts the
    Spearman sign against a magnitude-increasing measured series. See
    predicted_difficulty_rank()'s docstring for the full erratum account."""
    order = []
    for lam in LAMBDAS:
        for th in THETA0S:
            order.append((th, lam))
    return {cell: i + 1 for i, cell in enumerate(order)}
```

and, inside `main()`, immediately after the `p_ncov2` block is computed:

```python
    # ---- Erratum replay: reproduces the disclosed Phase-4 runtime bug
    # bit-for-bit from the actual committed function, for reproducibility
    # (LOGBOOK R4) -- NOT used for scoring, preserved for disclosure only.
    rank_map_buggy = predicted_difficulty_rank_ORIGINAL_BUGGY()
    p_ncov2_erratum_buggy = {}
    for fn in FUNCS:
        predicted = []
        measured = []
        for (th, fw, lam) in fwhm20_cells:
            d = per_cell_func[(th, fw, lam, fn)]
            step0 = d["steps"][0]
            dabs = step0["dabs"]
            drel = step0["drel"]
            magnitude = drel if drel is not None else (dabs / ABS_TOL) * REL_TOL
            predicted.append(rank_map_buggy[(th, lam)])
            measured.append(magnitude)
        rho, pval = spearmanr(predicted, measured)
        p_ncov2_erratum_buggy[fn] = dict(
            spearman_rho=float(rho), pvalue=float(pval), outcome="REFUTED",
        )
```

and add `P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY=p_ncov2_erratum_buggy` to the
`predictions=dict(...)` block, and a `phase4_erratum=(...)` string
(verbatim text already in the committed `results.json`, unchanged) to the
`meta=dict(...)` block. I independently verified this exact construction
reproduces `results.json`'s current `P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY`
bit-for-bit (§2, above — ρ = −0.48333.../−0.46666.../−0.45,
p = 0.18746.../0.20538.../0.22421..., all matching to every printed digit).
After this fix, `python run.py` regenerates the full committed
`results.json`, including both erratum fields, from a single invocation —
closing the gap without discarding or re-deriving anything.

**3. [Mandatory, cheap — VISION's Attack-6 propagation gap.] Add the T24
caveat to the two loci that don't currently carry it.** In `run.py`, add a
`t24_caveat` string field to the `p_ncov5` dict (verbatim text already
frozen in NOTES.md's predictions-table row). In NOTES.md's Results-table
P-NCONV26-5 row, append: "— T24's separate ABSORB-boundary systematic at
this cell remains untested by this audit (see the frozen prediction's own
disclosure)."

**4. [Recommended, not blocking — QUANTUM's `converged_value` semantics.]
Add one sentence to `run.py`'s docstring or a comment at the
`per_cell_summary` construction site: `converged_value` is the value at
the smallest N_SERIES entry passing the two-consecutive-doublings test,
not the series' n=5121 asymptote — cite QUANTUM's own example cell if a
concrete illustration is wanted.**

**5. [Mandatory, Director-authorship instruction, not a code/doc change.]
When writing the LOGBOOK.md close-out entry for this iteration, use
PHOTONICS' corrected n\*=81 figure (§1, above) for any sentence
characterizing the `incoherent_corrected` function's worst-case n\*. Do
**not** copy MATERIALS' or ELECTROMAGNETISM's own proposed "corrections to
propagate to LOGBOOK" text verbatim on this point — both currently carry
the fabricated 321 figure, uncorrected, in the same paragraphs offered as
close-out-ready prose.**

**6. [Carry forward, not new — already correctly scheduled.] The A=724/
NY=1528 `PLAN.md` follow-up trigger (idealization 7 / Attack 1) has not
yet landed in `PLAN.md`'s queue.** Confirmed directly (`PLAN.md`'s
"Current state" section is still headed "panel Iteration 25"). This is
expected — Phase-5 close-out, which lands the trigger, happens after all
seven seats report, and this is the seventh. Not a defect; must land in
the same close-out commit that applies items 1–3 above, per the Director's
own repeated commitment (three independent loci in the record already
promise it).

---

## Verdict

**PROMISING**, adjudicating six blind reviews (5 PROMISING: MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE; 1
PARTIAL: PHOTONICS, scoped specifically to the two defects this audit
confirms). Per this program's own established precedent (verdict turns on
whether open questions close, not seat count — Iterations 9, 10, 12, 17,
21, 22, 25), both of PHOTONICS' load-bearing catches close with the
same-shift fixes in §6: the "321" figure is a one-sentence, mechanically
verifiable correction, and the reproducibility gap is a genuine but
narrow, non-load-bearing code addition with a fully worked, independently
verified fix in hand. The cycle's own central hypothesis
(P-NCONV26-1a — n=41 is genuinely under-converged for the coherent
function at FWHM=20°) holds cleanly, confirmed four independent ways
(PHOTONICS, MATERIALS, EM, QUANTUM, each re-running the actual function);
the mandatory coherent cross-check this program has leaned on since
Iteration 19 survives at a properly converged n; and every one of the
eleven scored predictions' outcomes is unaffected by either defect found
here. What did not close cleanly on the first pass: two independent
instances of this program's own R4 house rule, recurring in the cycle
immediately following its adoption, and one of them already visible inside
two of the six review documents meant to catch it — worth the hardened
tripwire in §5, not worth withholding PROMISING for a non-load-bearing,
cheaply-and-fully-fixed pair of disclosure gaps.

**Checkpoint criterion 4: does NOT fire**, contingent on §6 items 1–3
being applied this same shift (the Director's own established remedy for
this exact defect shape, Iterations 19/22/25). No other Checkpoint
criterion fires — no constraint-3/4 claim, no mechanism, no
`REALIZABILITY_MEMO.md` tier movement anywhere in this cycle's record.

**Next lead per rotation: MATERIALS** (PHOTONICS' own rotation slot closes
with this cycle; VISION SCIENCE→PHOTONICS→MATERIALS→ELECTROMAGNETISM→
THERMODYNAMICS→QUANTUM OPTICS→VISION SCIENCE→repeat).

**Ranked priorities for Iteration 27** (synthesized across all six
Phase-5 reviews plus this audit; adjudicating near-unanimous convergence
on item 1):

1. **Re-run this identical n-doubling sweep at exp-048's A=724/NY=1528
   fallback geometry** (idealization 7 / Attack 1's own follow-up trigger,
   now due — five of six seats independently rank this at or near #1;
   this is the geometry any actual near-boundary constraint-3 or
   realizability citation would use, and it has never been convergence-
   tested).
2. **Genuine FDTD `ABSORB` sweep at the T21-vs-T24 geometry** (queued
   since Iteration 23, sharpened by this cycle's own finding that the
   sharpest-stakes cell's n-convergence uncertainty is now known to be
   ~7.7×10⁻⁹% — effectively zero — leaving T24's ~0.0070 boundary
   systematic as the only remaining unresolved uncertainty source on this
   program's own sharpest contamination-risk cell).
3. **EM's phase-corrected difficulty-predictor test** (§3 of
   `phase5_review_em.md`): score `Δrel(41→81)` against a predictor that
   includes each cell's phase offset within its own local T21 fringe
   period, not period-vs-Nyquist-margin alone — the concrete, cheap,
   desk-only test that would distinguish "wrong length scale for
   `coherent`" from "missing phase term for everyone," the ambiguity this
   cycle's own P-NCONV26-2 result leaves open (ρ=0.45–0.48 for all three
   functions, an unexpectedly uniform outcome across mechanistically
   distinct functions).
4. **Build and measure the fixed-absolute-thickness `graded_black_shell`
   variant** (now a 9-plus-iteration-deferred MATERIALS pick, independently
   re-ranked again this cycle).
5. **THERMODYNAMICS' own standing `h_eff` re-derivation** for this
   program's two thinnest surviving detectability margins (exp-043
   ON-endpoint, exp-045 dose-accumulation) — overdue since Iteration 25
   close, unrelated to this cycle, next on THERMODYNAMICS' own rotation
   slot's backlog.

---

## Verification appendix — what I actually did

**Files read in full:** `PANEL.md`; `LOGBOOK.md` in full (9413 lines,
including RULED OUT R1–R4, ESTABLISHED, the fix-docket-delivery pattern's
own history at Iterations 13–25, and R4's adoption text at Iteration 25);
`experiments/049-.../phase1_proposal.md`, all five
`phase2_critique_*.md`, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py` (388 lines, full read), `results.json` (1331 lines,
`meta`/`predictions`/`per_cell_summary` all read/queried programmatically);
all six `phase5_review_*.md` files in full; `experiments/046-.../
phase5_redteam_audit.md` for style calibration.

**Commands run:** `python3` direct `json.load` of `results.json`,
programmatic scan of `per_cell_summary` for `max(nstar)` and per-function
`Counter`s (§1); `git log --oneline -- experiments/049-.../`; `git show
--stat e5c32b1` and `7699de5`; `git diff 7699de5 e5c32b1 --
experiments/049-.../run.py` (confirms the only code change between the
Phase-4-implementation and results commits is the one-line rank-sign fix —
no erratum-preservation code was ever present, matching THERMODYNAMICS'
own independent finding); `grep -rn "321"` across every file in
`experiments/049-.../` (locates the fabricated figure's occurrences,
including its spread into `phase5_review_materials.md` and
`phase5_review_em.md`); `grep -n "exp-049|A=724" PLAN.md` (confirms the
follow-up trigger has not yet landed, as expected pre-close-out).

**Python executed directly against the real code** (not `run.py`):
imported `experiments/042-t21-magnitude-bridge/design_geometry.py`
unmodified and reconstructed the ORIGINAL BUGGY `predicted_difficulty_
rank()` (`{cell: i+1 ...}`) from `run.py`'s own docstring account of the
bug, ran the full P-NCONV26-2 computation against it at all 9 FWHM=20°
cells for all three functions, and reproduced `results.json`'s
`P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` block bit-for-bit (ρ =
−0.48333.../−0.46666.../−0.45, p = 0.18746.../0.20538.../0.22421...,
matching to every printed digit) — this is the exact construction
proposed as mandatory fix 2, verified working before being handed to the
Director.

**Ruled-out check:** nothing in this cycle or this audit resurrects R1,
R2, or R3 — no mechanism, no cloaking, no shell-thickness claim anywhere
in `phase1_proposal.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`, or
any of the six Phase-5 reviews.
