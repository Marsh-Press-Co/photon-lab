# PHASE 5 — REVIEW · PHOTONICS (fresh context, blind) · Panel Iteration 26 · exp-049

*Charter: surface interaction, absorption spectra, angular dependence,
scattering cross-sections. Owns: is the proposal's optical response coherent
as stated, across wavelength and angle?*

*Method: every number below was re-derived in this session by importing
`experiments/042-t21-magnitude-bridge/design_geometry.py` unmodified and
calling `gaussian_angle_weights`/`beam_divergence_incoherent[_corrected]`/
`beam_divergence_coherent` directly — including one full re-run of the
`find_nstar` two-consecutive-doubling logic against the actual N_SERIES for
the audit's own named "hardest cell," one from-scratch recomputation of all
three per-function Spearman correlations, and a full-grid scan of
`results.json`'s own `per_cell_summary`. Nothing below is taken from
NOTES.md's prose on faith.*

---

## 1. Reading — what I verified, and how

### 1.1 What reproduces exactly

| Claim | My independent check | Result |
|---|---|---|
| P-NCONV26-0 regression gate | called `beam_divergence_coherent` at n=41/401 for all 36 cells, unmodified code | worst move **4.472688822027389%** at (36°,20°,450nm), n_above_1%=2, n_above_0.16%=3 — exact match, all digits |
| P-NCONV26-2 (all three per-function Spearman ρ) | rebuilt `predicted_difficulty_rank()` and the corrected-exemption `Δrel(41→81)` from scratch, `scipy.stats.spearmanr` | **incoherent 0.4833, incoherent_corrected 0.4667, coherent 0.4500** — exact match to `results.json`, all in [0.30,0.70) → PARTIAL, none confirm, none falsify |
| Sign-convention erratum fix, as actually shipped in `run.py` | read `predicted_difficulty_rank()` verbatim: `{cell: n-i ...}`, i=0↔hardest↔largest rank; independently confirmed this convention is the ONLY one consistent with a positive ρ against a magnitude-increasing series | the erratum is genuinely fixed in the code that ships, not just described as fixed in NOTES.md — see §1.2 for the part that is **not** fixed |
| P-NCONV26-8 worst-cell move | ran the full N_SERIES doubling test for `beam_divergence_coherent(36,20,CPL[450]=15,n=…)` myself | **n\*=81**, Δrel(41→81)=**4.474701609942433%**, all later steps (81→161→…→2561→5121) converge cleanly (Δrel ≤0.002% from the second step on) — matches `results.json` exactly, confirms P-NCONV26-8's 4.4747% is genuine, not a fluke of one lucky doubling |
| P-NCONV26-5 sharpest-stakes cell | ran the same cell (750nm,38°,FWHM=2°,`incoherent_corrected`) | n\*=41, relative move over the WHOLE doubling range (41→5121) = **7.7×10⁻⁹%** — the cell is converged to noise-floor precision, confirms Red Team's own Attack-6 finding |
| Global maximum n\* across the ENTIRE 108-cell-function grid | scanned `per_cell_summary` directly | **81** — no cell-function combination anywhere in the audit ever needs n\*=161, 321, 641, 1281, 2561, or 5121; the `Counter` of n\* values is exactly `{41: 92, 81: 16}` | see §1.2, this is where NOTES.md's own prose disagrees with its own data |
| P-NCONV26-1c / P-NCONV26-3 (FWHM≤10° universal convergence) | filtered `per_cell_summary` for fwhm≤10 (81 combos) and fwhm==10 (27 combos) | **all 81** FWHM≤10° combos have n\*=41 (100%, not the predicted ≥70%); **0** FWHM=10° combos ever show a genuine non-exempted Δrel>1% blowup — matches CONFIRMED/REFUTED exactly |

The regression gate, the erratum fix itself, and eight of the eleven scored
predictions are exactly what NOTES.md says they are. This is a well-built
instrument cycle at the level of its own frozen falsifiers. The rest of this
review is the place where the write-up's own **prose** — not its scored
predictions — disagrees with its own committed data.

### 1.2 The "Net practical conclusion" sentence is contradicted by the very table it cites

NOTES.md's Results section states, as this cycle's headline actionable
takeaway:

> "n=41 is safe everywhere except the FWHM=20° regime, where the coherent
> function specifically needs n\*≥81 … **and the incoherent_corrected
> function needs n\* up to 321 at 5 of 9 cells** (see `results.json`
> `per_cell_summary` for the exact per-cell n\* table)."

I read exactly that table, for exactly those cells. The five
`incoherent_corrected`/FWHM=20° cells with n\*>41 are (450°,36/38/40),
(600°,38°), (750°,38°) — matching the "5 of 9" count — and every one of
them has **n\*=81**, not 321:

| λ | θ₀ | n\* |
|---|---|---|
| 450 | 36 | 81 |
| 450 | 38 | 81 |
| 450 | 40 | 81 |
| 600 | 38 | 81 |
| 750 | 38 | 81 |

The number 321 never occurs as an n\* anywhere in the committed
`per_cell_summary` — for `incoherent_corrected`, for either of the other two
functions, or for any of the 36 cells at any FWHM. The global maximum n\*
across all 108 cell-function combinations, confirmed above by direct scan,
is 81. This is not a rounding or labeling nuance: 321 is 4× the actual
figure, and it is the one sentence in the entire document written as
practical guidance for future cycles ("any future citation of a FWHM=20°
coherent reading … should use n≥81" is correct and immediately followed by
an incorrect companion claim for the incoherent-corrected function). I can
find no code path or intermediate computation anywhere in `run.py` that
would produce 321 for this comparison — the two-consecutive-doubling test
as shipped simply never returns that value for this function.

**Charter relevance.** This is exactly PHOTONICS' own lane — whether the
optical-response convergence claim is coherent as stated, across the swept
grid — and it fails at the one place a future cycle would actually go to
look up "how many angular samples do I need." LOGBOOK's own **R4** house
rule (adopted one cycle ago, Iteration 25, for the identical species of
defect — a headline figure that does not reproduce from the committed
record) exists precisely to catch this. This is now the **fourth
consecutive cycle** (23, 24, 25, 26) carrying an instance of the pattern
LOGBOOK already names, this time in the Results narrative rather than an
idealization citation, and one cycle after the rule meant to stop it was
adopted. Non-load-bearing to any of the eleven scored predictions (P-NCONV26-1b
itself is correctly scored PARTIAL off the *count* of failing cells, 5/9,
not off any n\*=321 claim) — but it is the exact sentence a future cycle
would paste into a design-geometry docstring, and as written it overstates
the actual quadrature cost by 4×.

### 1.3 A second, related defect: the erratum-disclosure fields in `results.json` are not reproducible from the currently-committed `run.py`

The task brief asked me to check the sign-convention erratum is "actually
fixed correctly in the committed run.py and results.json — don't just trust
the NOTES.md narrative." The fix itself is genuine (§1.1) — but the
*disclosure machinery* has a gap. `results.json` carries two fields that
document the erratum:

- `meta.phase4_erratum` (a full prose description of the bug, the buggy
  ρ-values, and the fix)
- `predictions.P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` (the three buggy
  ρ-values themselves: −0.4833/−0.4667/−0.4500 — exact negatives of the
  corrected values, internally consistent with the described bug, which
  simply reverses a rank order)

I read the currently-committed `run.py` end to end (388 lines). **Neither
field is constructed anywhere in it.** The `meta=dict(...)` literal at the
bottom of `main()` lists exactly ten keys, none of them
`phase4_erratum`; the `predictions=dict(...)` literal lists exactly twelve
keys, none of them `P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY`. Running the
committed `run.py` today, unmodified, would produce a `results.json` that
is a **strict subset** of the one actually committed — correct on every
number I could check (§1.1), but missing the two fields that document this
cycle's own honesty about its own bug.

I do not believe the disclosed numbers are fabricated — they are exactly
the sign-flip the described bug would produce, and I independently verified
that flipping `predicted_difficulty_rank()`'s rank assignment (ascending
instead of descending) negates the Spearman statistic, which is exactly
what −0.4833/−0.4667/−0.4500 vs. +0.4833/+0.4667/+0.4500 shows. The most
likely history is that an intermediate version of `run.py` computed and
kept both readings, and the version actually committed was cleaned up to
only compute the corrected one, without correspondingly regenerating
`results.json`. But as things stand, this program's own committed artifact
pair fails its own regression contract at exactly the file that is supposed
to demonstrate this cycle didn't hide a mistake — a smaller-scale instance
of the same "artifact doesn't reproduce from the committed function" defect
class R4 was written for, this time in the erratum-disclosure machinery
itself rather than in a headline number.

### 1.4 The T21-period analogy: directionally right, but weaker than "directionally right" sounds

NOTES.md's own reading — "the T21-period analogy correctly predicts
direction but is not a reliable per-cell predictor" — is accurate, and I
want to sharpen it rather than dispute it. All three per-function ρ values
are positive (0.45–0.48, confirmed independently, §1.1) and none reach the
0.70 confirm bar, which is the stated finding. What the write-up does not
surface: at n=9 points per function, **none of the three correlations is
statistically significant at conventional levels** (p=0.187, 0.205, 0.224
— all comfortably above 0.05, computed directly by `scipy.stats.spearmanr`
on the same series). A positive-but-non-significant ρ at n=9 is materially
weaker evidence than "directionally right" implies to a reader who doesn't
check the p-values — with this few points, a correlation in this range is
also consistent with pure chance. This doesn't change any scored outcome
(P-NCONV26-2's own falsification band was pre-registered at ρ<0.30 or
negative, and 0.45–0.48 sits inside the PARTIAL band regardless of
significance), but a future cycle reading "T21-period analogy: partial
directional support" should not read that as "probably real, just noisy" —
the p-values say it is equally consistent with "no real predictive content
at this sample size."

EM's own Phase-2 sharpest attack (that the coherent function's grating-lobe
mechanism has a different natural length scale — `GUARD_OUT+W_FLANK=263`
cells, the observation-window geometry, not `A=752`, the source-aperture
edge offset) was never actually tested this cycle. The mandatory-fix docket
split P-NCONV26-2's correlation three ways (per function) but did not add
the alternative-length-scale correlation EM's own flip proposed. The
coherent function's own ρ=0.450 (the weakest of the three, and the one
function whose sensitivity mechanism is agreed by every seat to be
physically distinct from the edge fringe) is exactly where that alternative
model would matter most, and it remains untested. See §3, item 3.

### 1.5 The FWHM=10° finding is genuine and well-supported

This is the one place the audit *overturns* its own prior cleanly, and I
verified it holds under my own from-scratch recomputation: every one of
the 27 FWHM=10° cell-function combinations has n\*=41 (100%, not merely the
predicted ≥70%), and the four Δrel-blowup cells Red Team flagged in Phase 2
(450nm/{36°,38°}×{incoherent,incoherent_corrected}) all pass the corrected
exemption criterion cleanly — their large swings (spot-checked above,
e.g. C(41)=3.85×10⁻⁵ → C(401)=−1.03×10⁻⁴ at 450°/36°) are confined to
values two-to-three orders below C_THR, exactly the near-null regime the
Attack-5 exemption was built to neutralize, and the exemption does its job:
n\*=41 there reflects a passing `Δabs≤5×10⁻⁴` test, not a claim that the raw
value itself is stable (it is not — it swings sign). That's a correct,
disclosed design choice (idealization 2), not a defect, but a future reader
citing "FWHM=10° is universally converged at n=41" should understand it
means "converged relative to C_THR," not "the raw C value itself is
stable" at these four particular cells.

### 1.6 Minor, non-load-bearing

- P-NCONV26-3's committed band text ("≥1 of the **12** FWHM=10° cell-function
  combinations") is arithmetically wrong — the actual grid is 3λ×3θ₀×3
  functions = **27**, not 12, and this number survives unchanged from Phase 1
  through Phase 3/NOTES.md without any of the five blind Phase-2 seats or
  Red Team's own audit (which recomputed nearly everything else in this
  prediction) catching it. Doesn't change the REFUTED outcome (0 qualifying
  cells regardless of denominator), but it is one more small arithmetic slip
  in a document whose own THERMO/Red-Team Phase-2 exchange (Attack 3) already
  caught and fixed a comparable one.
- P-NCONV26-7's "max shift 0.0 percentage points" is true but close to
  tautological: every FWHM≤10° cell has n\*=41 (§1.1/1.5), so
  `converged_value` equals `values[41]` by construction for all of them — the
  0.0pp figure confirms nstar=41 universally, not an independent
  stability check of the coherent function's central-lobe shape at a
  genuinely different n.

---

## 2. Physical meaning for the program

1. **The coherent function's FWHM=20° aliasing is real, bounded, and cheap
   to fix — n\*=81 suffices everywhere, not the {641,1281} the Phase-1
   heuristic feared.** This is the audit's central, well-supported finding.
   Any future citation of a `beam_divergence_coherent` reading at FWHM=20°
   from this geometry should re-run at n≥81; the committed n=41 readings
   in exp-042/046's own record (the ones this cycle exists to characterize)
   are the ones actually affected.
2. **n=41 is broadly safe** — 100/108 combinations already sit at their own
   converged value at the committed default, and the FWHM≤10° regime is
   universally converged (§1.5), a materially better result for the
   instrument's own existing default than the T21-period Nyquist-margin
   heuristic predicted.
3. **The T21 fringe-period analogy does not transfer as a strong per-cell
   predictor to this different quadrature construction** — directionally
   consistent (all three functions positive), but none of the three
   per-function correlations reaches significance at this sample size
   (§1.4). This narrows, usefully, what future cycles can lean on the T21
   period formula for: it is a source of falsifiable priors, not a
   calibrated predictor, for `gaussian_angle_weights`-driven quantities.
4. **None of this transfers to exp-048's A=724/NY=1528 fallback geometry**
   (idealization 7, correctly scoped and correctly affirmed by every seat
   at Phase 2) — the geometry any actual near-boundary constraint-3 citation
   would use has not had this sweep run against it yet.
5. **The practical "safe n" guidance, as currently written in NOTES.md, is
   wrong for one of its two clauses** (§1.2) and should not be quoted or
   propagated into any future `design_geometry.py` docstring or LOGBOOK
   thread update until corrected — the correct figure (n\*≤81 everywhere in
   this geometry, for all three functions) is a *stronger*, cheaper, more
   useful result than the one currently written down, not a weaker one, so
   the fix is good news, not a retraction.

---

## 3. Argued next change (one concrete item) + ranked top-3

**Argued next change: fix NOTES.md's Results narrative same-shift, before
any future cycle cites "n* up to 321."** Two one-line corrections, zero new
computation (the correct numbers are already sitting in the committed
`results.json`):

1. Replace "the incoherent_corrected function needs n\* up to 321 at 5 of 9
   cells" with "the incoherent_corrected function needs n\*=81 at the same
   5 of 9 cells" (per §1.2's table, drawn directly from the committed
   `per_cell_summary`).
2. Either restore the code path that produces `meta.phase4_erratum` and
   `P_NCONV26_2_ERRATUM_ORIGINAL_BUGGY` in the committed `run.py` (so a
   fresh run regenerates the full committed `results.json`), or add an
   explicit one-line disclosure in `run.py`'s own docstring that these two
   fields were preserved from an intermediate script version and a fresh
   invocation will not reproduce them — whichever is cheaper, but not
   silence, per this program's own R4 precedent (§1.3).

## Ranked top-3 candidate directions for Iteration 27

1. **Re-run this identical sweep at exp-048's A=724/NY=1528 fallback
   geometry** (idealization 7's own committed trigger, MATERIALS' Attack 1,
   adopted). This is the geometry every actual near-boundary constraint-3 or
   realizability-adjacent citation in this program's live threads (T21, T24)
   would use — none of this cycle's n\* findings license anything at that
   geometry yet, and the re-run is a near-zero-cost parameter substitution of
   an already-profiled script (measured ≈46 min at the A=752 geometry).
2. **Test EM's own alternative length-scale predictor for the coherent
   function's difficulty ordering** (`GUARD_OUT+W_FLANK=263` cells /
   grating-lobe offset, vs. `A=752`) — the one Phase-2 flip that was raised,
   affirmed by Red Team's own demonstrated ρ-split (0.717/0.600/0.450), but
   never actually built or scored this cycle. The coherent function's own
   ρ=0.450 is the weakest and least significant of the three (§1.4) and is
   exactly the case every seat agrees has a different governing mechanism —
   a real, falsifiable, zero-FDTD test of whether a mechanistically-correct
   predictor does better than the reused T21 analogy.
3. **Fix the NOTES.md narrative + `run.py`/`results.json` reproducibility
   gap named in §3's argued-next-change**, same shift, before either number
   is cited elsewhere — cheapest item on this list, and the one most likely
   to otherwise propagate silently (LOGBOOK's own R4 rationale) into a
   future `design_geometry.py` docstring or LOGBOOK thread update.

---

## 4. Verdict

**PARTIAL.**

The instrument design is sound, the Phase-2/Red-Team process caught and
correctly fixed two real defects before the run (the ill-conditioned Δrel
near |C|≈0, the non-executable regression gate), and eight of eleven scored
predictions — including the central P-NCONV26-1a/1c/8 findings this cycle
exists to establish — reproduce exactly under my own independent
recomputation from the committed code. That is genuine, well-verified
instrument progress: n\*=81 is a cheap, sufficient fix for the one regime
that actually needed one, and the FWHM≤10° regime is more robust at n=41
than the audit's own prior feared.

Against that: the one sentence written as this cycle's practical takeaway —
the reason Red Team ranked this item non-negotiable in the first place — is
contradicted by the very `per_cell_summary` table it cites as its source
(§1.2), by a factor of 4×, and the erratum-disclosure fields in the
committed `results.json` cannot be regenerated from the committed `run.py`
(§1.3). Neither defect threatens any of the eleven frozen, scored
predictions, and neither is a mechanism failure — but this is the fourth
consecutive cycle carrying an instance of the exact defect class (a
headline figure or disclosure artifact that does not reproduce from the
committed record) LOGBOOK's own R4 rule was adopted one cycle ago to stop.
Not RULED OUT — nothing here is a dead instrument or a falsified central
claim, and both defects are same-shift, zero-new-computation fixes using
numbers already sitting in the committed `results.json`. Not PROMISING — a
practical-guidance sentence that overstates a quadrature-cost requirement
by 4×, in the one document a future cycle would actually go to for that
number, is exactly the class of defect this program's Phase-5 culture
exists to catch before it propagates.
