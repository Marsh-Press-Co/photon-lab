# PHASE 5 — REVIEW · ELECTROMAGNETISM seat · exp-097 (Panel Iteration 74)

*Blind review — no access to any other seat's Phase-5 write-up this cycle.
Charter applied per the Director's framing: T1 is N/A this cycle (zero-FDTD
registration-code verification, no mechanism/energy claim), so the
reciprocity/passivity/causality discipline is applied instead to whether
`run.py`'s own construction/comparison logic — the shared-`Sim` design in
`run_checks_1234_and_7`, the phase-ramp and amplitude-taper formulas — is
self-consistent field theory, correctly implemented as coded, independently
re-derived from `lab/fdtd2d.py` source, not taken on NOTES.md's word.*

## 0. Method

Read `PANEL.md` in full; `LOGBOOK.md`'s RULED OUT registry R1–R18 verbatim
and the T28 sub-thread Iterations 70–73 (exp-093 through exp-096) in full;
`experiments/096-.../NOTES.md` and `run.py`; every file in
`experiments/097-t28-r18-tier0-gate-closure/` (`phase1_proposal.md`, all
five Phase-2 critiques, `phase2_redteam_audit.md`, `NOTES.md`, `run.py`,
`results.json`); `experiments/069-.../design_geometry.py` in full; and
`lab/fdtd2d.py` lines 120–186 (`add_line_source`, `Sim.__init__`) directly
from source.

**Independently re-executed `run.py` this session** (`python3
experiments/097-.../run.py`) and diffed the freshly-produced `results.json`
against the committed one field-by-field (all keys, `wall_time_s`
excepted): **bit-identical.** Every predicted-vs-actual row in NOTES.md's
Result table (positive control, FI-A/B/C/D/E/F/G/H, the 21-construction
count, both Check-5 and Check-6-old/new outcomes) reproduces exactly from
the committed script — this is not merely a plausible narrative, it is a
verified reproduction.

## 1. Field-theory formulas: correct, bit-exact against source

Independently re-derived, not accepted from any Phase-1/2 claim:

- **Phase-ramp (`phase_expected`, Check 4).** `k = 2π/lam; phase = k·sinθ·
  (y−ȳ) + rel_phase`, where `lam` is cells-per-wavelength — read directly
  against `lab/fdtd2d.py:171–175`. This is the standard linear-phase-
  gradient beam-steering relation for a tilted plane-wave line source;
  units are self-consistent (`k` in rad/cell, `(y−ȳ)` in cells, product in
  radians). Bit-exact match, both formula and the ONE-recomputation
  discipline (fix #8, exp-096 — using the already-verified `sim.lam` from
  Check 1, not a second independent `lam` reconstruction).
- **Amplitude taper (`taper_expected`, Check 7, new this cycle).**
  `p=ones(n); win=0.5·(1−cos(π·i/edge)); p[:edge]=win; p[-edge:]=win[::-1]`,
  stored as `amplitude·p` — read directly against `lab/fdtd2d.py:160–164`.
  Bit-for-bit copy, not a paraphrase. Physically this is a raised-cosine
  (Hann-family) aperture apodization, entirely independent of `angle_deg`
  and `lam`/`cpl` — a structural fact I independently confirmed by
  inspection of `add_line_source`'s own code (the `p` array is built
  before the `if angle_deg or rel_phase:` branch and never touches `k` or
  `self.lam`). This licenses the specificity claim (FI-A/B/C predicted
  CLEAN on Check 7, FI-D predicted DEFECT-FOUND-only-on-Check-7) as a
  genuine structural fact, not a coincidence of this cycle's chosen test
  points — I re-derive it independently here rather than accept the
  proposal's own assertion of it.

Both recomputations correctly avoid a self-referential-comparator trap: they
consume the **intended** (not actual/possibly-corrupted) upstream value —
`sim.lam` for Check 4 only after Check 1 has independently verified it is
correct, `TAPER[family]` for Check 7 (the intended `edge`, never read back
from the constructed object) — this is the right design and is stated
explicitly as such in Idealizations 41/43.

## 2. The `y_hi`/`BASE_NY` mis-citation — confirmed corrected, confirmed did
## not leak into Result

Independently re-verified the arithmetic myself against `design_geometry.py`
directly: `R3_BASE_NY=2376` (domain height) is a different quantity from
`r3_config()`'s own `y_hi=ny−y_lo=2316` (the source's upper placement edge,
offset from `NY` by `y_lo=60`); identical structure for R5 (`3960` vs.
`3860`, offset by `y_lo=100`). Phase 1's §0 and §2b both cited the wrong
constant as the desk-check's own comparison target (caught convergently by
EM and THERMODYNAMICS at Phase 2, extended by Red Team to the second,
higher-confidence instance in §0's compliance header).

**Verification that it landed correctly in the frozen document, not just
noted as fixed:** `NOTES.md` §"Changes from Phase 1" item 1 and §Setup item
3 both now state the desk pre-check reproduces `src_x=450, y_lo=60,
y_hi=2316` (R3) / `src_x=750, y_lo=100, y_hi=3860` (R5) against
`R{3,5}_CONFIGS["C40_R{3,5}"]`'s own stored fields — `R{n}_BASE_NY` is
never cited as a comparison target anywhere in the frozen NOTES.md. The
**Result** section (where the actual executed numbers are reported) does
not restate the desk-check narrative at all — it reports only "CLEAN, 3/3
families" against the true stored fields, which I independently re-derived
above to be correct. **Confirmed: the false "bit-exact… matches
`R{n}_BASE_NY`" claim did not survive into the frozen Predictions text and
does not appear in Result.** The fix landed exactly where Red Team's own
audit (§1) said it had to — in the committed NOTES.md text itself, not
merely a Phase-2 margin note — a correctly-discharged R4 instance.

## 3. A genuinely new finding, not caught by any of the five blind
## critiques, Red Team's own Phase-2 audit, or the Director's synthesis:
## Idealization 40 mischaracterizes `cpl_ok`'s own independence

NOTES.md's Idealization 40, describing the fixed `check6_positional_and_cpl`
(the check Red Team's own Phase-2 audit ranked the highest-priority fix in
the whole docket):

> "`cpl_ok`, however, is STILL keyed by `pt["family"]` on both sides after
> `family_ok` has passed — this is now safe... but it means `cpl_ok` alone,
> read in isolation from `family_ok`, is still not an independent per-point
> check."

I traced the actual committed code (`run.py:156–171`) line by line, then
independently executed it:

```python
family_frozen = NOTES_MD_FROZEN_FAMILY_BY_LINE[line]     # keyed by notes_line — independent of pt["family"]
cpl_frozen, _ = NOTES_MD_FROZEN_CPL_BY_FAMILY[family_frozen]   # ← keyed by family_frozen, NOT pt["family"]
cpl_ok = bool(CPL[pt["family"]] == cpl_frozen)
```

`cpl_frozen`'s own lookup key is `family_frozen` (the independent,
`notes_line`-keyed ground truth), **not** `pt["family"]`. Only `cpl_ok`'s
LEFT operand (`CPL[pt["family"]]`) depends on the untrusted field; the
RIGHT operand is already independent of it. This is the opposite of what
Idealization 40 claims ("still keyed by `pt["family"]` on both sides"). I
confirmed this is not merely a reading of the source but an operative fact
by direct execution — reconstructing FI-H's own mislabeled point
(`family="R3"→"R4"` override at the true line-511/38.4° point) and calling
`check6_positional_and_cpl` on it directly:

```
{'theta_ok': True, 'family_ok': False, 'cpl_ok': False, 'clean': False}
```

`cpl_ok` is independently `False` here — not merely riding on `family_ok`'s
own correct `False`. Because `R3`/`R4`/`R5`'s `cpl` values (30/40/50) are
pairwise distinct, **`cpl_ok` alone, with no dependence on `family_ok`
whatsoever, already discriminates every currently-possible family mislabel
among the three families this gate covers** — a strictly stronger property
than Idealization 40 discloses, and stronger than Red Team's own Phase-2
fix (§3 of `phase2_redteam_audit.md`) claims it achieves.

**Why this is a genuine R18-class finding, not a nitpick.** R18's own text
requires a check's documented scope to be "independently confirmed against
the check's own actual source code... before it is relied upon, cited as
closing a defect class, or described as load-bearing." Idealization 40 is
exactly such a documented-scope claim, and it does not match the code —
this is R18's own founding concern, recurring one cycle after R18's
adoption, inside the very cycle whose stated mission is applying R18 to
close prior instances of it (Learned item 1 already names one such
recurrence, Red Team's own `cpl_ok`-tautology catch in the Phase-1 draft;
this is a second, distinct instance, surviving that same fix, in the
*corrected* code's own self-description). **Every reviewer who has touched
this document — five blind Phase-2 critiques, Red Team's own audit, and
the Director's synthesis — described `cpl_ok` post-fix using language
matching Idealization 40's claim; none independently executed the
corrected function against a mislabeled point and inspected `cpl_ok` in
isolation.** `FI_H`'s own logged result (`results.json`) never surfaces
`cpl_ok` at all — only `clean` and `family_ok` are extracted into
`run_fi_h`'s return dict — so this fact was genuinely invisible to anyone
who read only the committed JSON, exactly the shape of gap this program's
own R4/R9 lineage exists to catch (a claim about the code that does not
survive independent execution).

**Disposition — non-load-bearing, direction matters.** This is the mirror
image of every prior R18 instance: those found a check's real coverage
NARROWER than claimed (a false sense of security); this finds `cpl_ok`'s
real coverage WIDER than claimed (an undisclosed redundancy). It does not
threaten the CLEAN verdict, does not create a false-negative risk, and
`family_ok` remains correct and necessary in its own right (it is the only
sub-check keyed to independent ground truth for `family` when `cpl` values
are not pairwise distinct — a condition this program does not currently
violate but has no standing guarantee against). I flag it because R18's
own discipline makes no exception for "the actual code is stronger than
documented" — an inaccurate self-description of a check's own logic is the
exact failure class named, regardless of which direction the error points,
and a future cycle citing Idealization 40's text (e.g. to justify removing
`family_ok` as "redundant with a strengthened `cpl_ok`," or the reverse) is
now working from a specification that does not match the code it describes.

## 4. Other construction/comparison logic checked and found sound

- **`Sim.lam` assignment.** Independently confirmed at `lab/fdtd2d.py:75`,
  `self.lam = float(cells_per_lambda)` — Check 1's `sim.lam ==
  float(cpl_intended)` compares against the actual assignment target, not
  an inferred proxy.
- **FI-A's "spurious agreement" on Check 4 is correctly disclosed, not a
  fresh gap.** Independently confirmed in `results.json`:
  `check4_phase_ramp=true` under FI-A (the family/`cpl` swap) — Check 4
  recomputes its own comparator from `sim.lam`, which is *already* the
  corrupted value under this fault, so both sides of the `np.allclose`
  agree by construction. This is carried forward accurately from exp-096's
  own R18 finding (not re-claimed as newly discovered here) and correctly
  distinguished in NOTES.md's own predicted-outcomes table from Check 7's
  CLEAN-under-FI-A, which is a genuine specificity result (the taper
  profile structurally cannot depend on resolution — verified in §1 above)
  rather than a spurious one. The document does not conflate these two
  different reasons for an identical CLEAN reading, which it would be easy
  to do carelessly; it does not.
- **Check-5 extension arithmetic (`R3`/`R5`).** Independently re-derived
  from `design_geometry.py` directly (not from NOTES.md's own restated
  figures): `R3` (ratio=1.5) → `src_x=450, y_lo=60, y_hi=2316`; `R5`
  (ratio=2.5) → `src_x=750, y_lo=100, y_hi=3860`. Both bit-exact against
  `r3_config()`/`r5_config()`'s own actual output (`R3_CONFIGS["C40_R3"]`,
  `R5_CONFIGS["C40_R5"]`), independent of the (corrected) desk-check prose.
- **Construction count (21).** Independently re-traced: 16 representative +
  4 (positive control/FI-A/B/C, shared-object with Check 7) + 1 (FI-D) =
  21, `sim.__init__` calls only; FI-E/F/G/H are pure-Python/no-`Sim()`,
  correctly zero-cost. Reproduces exactly on independent execution.
- **Shared-`Sim` design (`run_checks_1234_and_7`).** Physically sound: one
  `Sim`/`add_line_source` call populates `sim.lam`, `sim.source_specs`,
  and `sim.sources[-1]` (`x`, `sl`, `phase`, `profile`) simultaneously —
  reading multiple fields off one already-fully-determined object for
  Checks 1/2/3/4/7 together is not a shortcut that risks masking a
  fault; each check still reads a different, structurally distinct field
  (`lam`, `angle_deg` metadata, `x`/`sl`, `phase` array, `profile` array)
  and each retains its own independent recompute where one exists (Checks
  4 and 7). No cross-check contamination found.

## Verdict: **CONCUR-WITH-GAP(S)**

**Concur** with the composite CLEAN outcome and with every headline claim I
independently re-verified: the phase-ramp and taper formulas are bit-exact
field-theory reproductions of `lab/fdtd2d.py`; the `y_hi`/`BASE_NY`
mis-citation is genuinely corrected in the frozen document and does not
appear in Result; the 21-construction accounting, the Check-5 `R3`/`R5`
extension, and all nine fault-injection scenarios (positive control,
FI-A through FI-H) reproduce bit-exact on independent execution of the
committed `run.py`; the shared-`Sim` design introduces no field-theoretic
inconsistency.

**Gap:** Idealization 40 misdescribes `cpl_ok`'s own independence property
(§3) — a genuine, previously-uncaught instance of R18's own "documented
scope must match actual code" concern, missed by all five blind Phase-2
critiques, Red Team's own Phase-2 audit, and the Director's synthesis, all
of whom described the fixed check using language the code itself
contradicts. Non-load-bearing to the CLEAN verdict and to any downstream
citation of this cycle's own result; correction is a one-line prose fix to
Idealization 40 (state that `cpl_ok`'s own right-hand operand is already
independently keyed via `family_frozen`, making it non-tautological even in
isolation given the current pairwise-distinct `cpl` values across
`R3`/`R4`/`R5` — and that this independence is contingent on that
distinctness, not structurally guaranteed).

## Ranked candidates for Iteration 75

1. **Item 6 — bracket the other three established `cpl=20` nulls at
   `cpl=40` (~24 calls).** With registration-defect explanations now
   exhausted about as far as zero-FDTD code review can take them (caller
   plumbing, transcription, one-point-per-family recipe arithmetic, and
   now amplitude-taper registration, all fault-injection-verified this
   cycle and last), the highest-information next real-data step is the one
   that discriminates a family-wide `cpl=40` recipe defect from
   feature-specific node migration — exactly this item's own stated
   purpose. Field-theoretically this is also the cleanest test: it reuses
   the already twice-validated `R4` construction recipe rather than
   introducing a new ratio, so no fresh ground-truth-recovery control is
   needed before it runs (the `R4` family's far-from-null behavior was
   already validated at exp-095's own Rank 1a/4).
2. **Item 7 — the re-centered node-bracketing re-run at θ₀≈38.590° at the
   confirmed ≥0.5° half-width (~8–16 calls).** The direct answer to the
   question this entire two-cycle registration detour exists to enable.
   Ranked second, not first, because on its own (per the R15 addendum this
   sub-thread adopted at Iteration 71) a single additional resolution
   point still cannot distinguish genuine convergence from a persistent
   recipe-level artifact — item 6's family-wide census is the more
   information-dense use of the next FDTD budget, and item 7's own result
   is more interpretable once item 6 establishes whether the `cpl=40`
   recipe carries a systematic, family-wide effect or not.
3. **Item 8 — pre-wire `netd_row()`/`cell_metrics_r{3,4,5}` sidecar
   extraction into whichever of items 6/7 runs first, per R16.** Zero
   marginal FDTD cost, purely preventive, and this sub-thread has now
   twice (R16, exp-094; a near-miss disclosed and fixed this cycle, §3
   above) shown that a claimed-but-unwired data channel is a recurring,
   catchable-in-advance failure mode. Bundle into item 6's own script from
   first commit rather than treat as separate.

Standing, unranked (carried correctly in this cycle's own NOTES.md, not
re-ranked here): PHOTONICS' grazing-incidence validity check (10 cycles);
the x-wall wavelength-generality leg (22 cycles); the unbiased
margin-vs-distance rebuild; the ritualization governance question.
