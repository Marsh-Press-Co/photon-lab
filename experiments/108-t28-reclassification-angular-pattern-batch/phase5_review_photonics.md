# PHASE 5 — PHOTONICS REVIEW (SELF-REVIEW) · Panel Iteration 85 (exp-108)

*Fresh context. This cycle's rotation lead — I wrote `phase1_proposal.md`.
Charter: surface interaction, absorption spectra, angular dependence,
scattering cross-sections. Owns: is the proposal's optical response
coherent as stated, across wavelength and angle? Every number below was
re-derived from primitives this shift (re-ran `reclassify_106.py`,
`analyze.py`, `lab/validation/run_all.py --only 26`, and hand-recomputed
from the raw pickled captures still sitting in scratch) — not trusted from
NOTES.md's own prose.*

---

## 1. Independent re-verification from primitives — all exact

Re-ran the three cheap, zero-new-FDTD scripts named in the task brief,
against the committed pickles/`results.json` still on disk:

- `python3 reclassify_106.py` → `THREE-WAY-AMBIGUOUS (REFUTES-...)
  (NOT-TRUSTED -- r=312 MARGINAL/unsettled)`, all other fields
  bit-identical to exp-106's own `results.json` — matches `run_output.txt`
  and NOTES.md's Result verbatim.
- `python3 lab/validation/run_all.py --only 26` → 2/2, positive control
  `0.000e+00`, negative control `2.000` (200%) — matches exactly.
- `python3 analyze.py` (re-run against the 6 already-captured `.pkl`
  files still in this session's scratchpad) → `item_i` CONFIRM/CONFIRM,
  `item_ii` CONFIRM/CONFIRM (`residual_std=2.8972e-06`/`2.1022e-06`),
  `item_iii` `0.1827`/`0.2525` PASS/PASS, `closure` 0.0196%/0.0563%
  (hollow), 0.0160%/0.0581% (PEC-cored) — every digit matches
  `run_output.txt` and NOTES.md's Result table exactly.

Gate P0, the reproduction precondition, the `sum(pattern)==sigma_scat`
identity (`<1e-9` at all 6 margins, both articles, both r), and the R23
live-fire check all reproduce as claimed. **Nothing in this cycle's
headline numbers is wrong, fabricated, or non-reproducing.** The rest of
this review is about what those correctly-computed numbers do and do not
actually test — the question inside my own charter.

---

## 2. Owning my own Phase-1 defects

**2a. The "same order T9 found at r=78" mischaracterization (caught,
corrected).** My own `phase1_proposal.md` §1 wrote that the hollow-vs-
PEC-cored `abs_ext_ratio` delta (2.97×10⁻⁵/2.47×10⁻⁵) was "the same order
T9 found at r=78" — MATERIALS caught, and Red Team independently
re-verified against LOGBOOK's own Iteration-84 record, that this exact
comparison was corrected one cycle earlier to a real **19.0×/15.8×** gap
against the like-for-like `exp-027` anchor (1.56×10⁻⁶), not "same order."
I had that correction available — it is in PLAN.md's own Current-state
section, which every rotation lead reads — and wrote the pre-correction
framing anyway. Director's synthesis fixed it in NOTES.md; I did not
catch it myself before Phase 2. This is squarely my own charter's mistake
(a wavelength/angle-independent aggregate-signal characterization) and I
own it plainly, not as a footnote.

**2b. The two-point `box_a`/`box_b` REFUTE bar and item ii's raw-`std`
noise-floor proxy (caught, corrected, superseded by Red Team's own
unified fix, §3 below).** My own Phase-1 tables treated box radius as an
exchangeable nuisance parameter in both items i and ii — EM and QUANTUM
independently found the same root-cause error from two different angles
(item i: the angular *distribution* of scattered flux is a near/mid-field
quantity, not conserved across radii, unlike the *integrated* flux
`box_a`/`box_b`-style comparisons are legitimately built for; item ii: six
increasing margins on one deterministic field are an ordered sequence,
not iid draws, so raw `std` conflates near-field convergence bias with
placement noise). Red Team combined both into the multi-margin
convergence/detrending fix Phase 3 adopted in full. This was a genuine
design flaw in my own instrument-design section, not a peripheral one —
it went to the heart of whether item i's REFUTE gate tests what it claims
to test. I did not catch it myself before Phase 2 either.

**2c. A new defect I did NOT know about until this review, also my own:
`angular_scattered_pattern`'s own provenance is mis-cited.** My §1
narrative and parameter table both state the function was "built and
gated at exp-059/060." I re-checked this against LOGBOOK.md directly,
not from memory: **every other citation of this function in LOGBOOK's own
23,000-line record — at least four independent instances, including
exp-060's own Phase-2 PHOTONICS critique text itself** ("`lab/sections.py::
angular_scattered_pattern` already exists (**exp-016/017**, zero marginal
FDTD cost)", `experiments/060-.../NOTES.md` line 145) — gives the origin
as **exp-016/017** ("017-trough-angular-pattern"), not exp-059/060.
exp-059 (Iteration 36) is the unrelated `Q_ext(x)` closed-form
cylinder/disk check; exp-060 (Iteration 37) is where the function was
**reused** as a Phase-2 mandatory fix, not where it was built or first
gated. This is a plain R4-class defect (a citation that does not
reproduce from its own cited source) in my own document, and it did not
stay contained to my own prose: MATERIALS' Phase-2 steel-man repeated it
verbatim ("already-gated machinery (`angular_scattered_pattern`,
exp-059/060)"), and it survived unchanged into NOTES.md's own frozen
Hypothesis section. **Zero of the five Phase-2 critiques and zero of Red
Team's own primitives-based audit caught it**, despite Red Team's audit
explicitly claiming to re-verify "every load-bearing figure below... not
trusted from any seat's restatement, including this document's own
quotations" (§0, `phase2_redteam_audit.md`). It is non-load-bearing — no
gate, band, or verdict depends on which exact prior experiment built the
function — but it is exactly the density-pattern R20 was written to
notice, and I am the seat whose charter this citation sits inside. Filed
here for the record; I do not think it individually rises to a LOGBOOK
addition (a single non-load-bearing instance, R4's own "does not fire on
its own founding instance" standard), but it is worth naming precisely
because nobody else's charter would have caught it and mine should have.

---

## 3. Item i's own classification logic — the task's central question

I re-derived `classify_item_i()` (`run.py:196-250`) against its own stated
predictions (NOTES.md §Predictions, Tier 1 item i) and against the actual
per-bin data pulled fresh from the six committed `.pkl` captures. Three
findings, in order of how load-bearing they are.

### 3a. The pre-registered per-bin floor-gate was never implemented

NOTES.md's own committed Predictions table conditions the CONFIRM
criterion on "every one of the 48 bins **that clears the item-ii absolute
floor**" — and `classify_item_i`'s own docstring says its
`sigma_scat_by_margin_peccored` argument arrives with a "floor-cleared
mask applied upstream." **No such mask exists anywhere in the code.**
`analyze.py` (lines 66-73) passes `pattern_peccored[m]` and
`pattern_delta[m]` straight from `angular_scattered_pattern()`'s raw
output into `classify_item_i()`, unmasked, for all 48 bins at all 6
margins. I grepped `run.py` and `analyze.py` for "floor" — the only floor
logic anywhere in this cycle's code is item iii's *numerator* floor gate
(`sc_floor_gate_window`, a completely different quantity: RMS-normalized
grid-cell intensity in the downstream window, not a per-bin angular
scattered-power comparison). This is also a category error in the
specification itself, not just a missing wire-up: item ii's own "absolute
floor" is a single scalar per r (`residual_std` of the six-margin
`abs_ext_ratio` fit, dimensionless-ratio units) — there is no coherent way
to apply it as a per-bin filter on `angular_scattered_pattern`'s own
per-bin, cross-section-like output; the two quantities do not share
units. **What was actually tested is stronger, not weaker, than what was
promised** — all 48 bins, not a floor-cleared subset — so this does not
undermine the CONFIRM verdict itself. But it is a genuine gap between the
pre-registered Predictions and the executed Result that survived Phase 3
into a "PROMISING... cleanest cycle" write-up without being flagged
anywhere in NOTES.md, and it means no per-bin angular-pattern noise floor
has actually been characterized by this cycle, despite the table's own
language implying one was.

### 3b. Global-max normalization is structurally insensitive to low-cross-section angular structure — the real answer to "could a real signature hide beneath the classification's own thresholds"

`rel32 = |Δpattern| / max_bin(σ_scat_per_bin[PEC-cored])` divides every
bin's deviation by the single largest bin (the forward-scattering peak),
not by that bin's own local magnitude. I pulled the raw per-bin patterns
directly from the captured phasor fields to check how skewed this
normalization actually is:

| r | bins with `\|pattern\|` < 1% of peak | < 0.1% of peak | reported `max(rel32)` (global-norm, as coded) | max **local**-normalized deviation (recomputed) |
|---|---|---|---|---|
| 156 | 30/48 (62.5%) | 22/48 (45.8%) | 1.48×10⁻⁴ | **9.88%** (bin at −146.25°) |
| 312 | 30/48 (62.5%) | 20/48 (41.7%) | 1.53×10⁻⁴ | **10.88%** (bin at +168.75°) |

The pattern is strongly forward-peaked (peak values 36.1/77.0 vs. a
minimum resolved bin of 3.4×10⁻⁵/7.6×10⁻⁵ — five orders of magnitude of
dynamic range across 48 bins), and nearly two-thirds of the angular
domain sits below 1% of the peak. Under the as-coded global-max
normalization, deviations in those low-signal bins are numerically
invisible almost by construction: a bin whose own hollow-vs-PEC-cored
scattered power differs by ~10% *locally* — comparable in magnitude to
half the 15% REFUTE bar — registers as `~10⁻⁷` relative to the global max,
over 1000× below the 5% CONFIRM line, regardless of whether that 10% is
real shape structure or noise. Because §3a's per-bin floor was never
computed either, there is no way from this cycle's own record to tell
whether that ~10% local deviation in the near-null bins is a genuine (if
modest) angular-shape effect concentrated in the side/back-scatter
directions — physically the most interesting region for constraint 2's
"no specular return to observer" concern, and generically where
interference-fringe/near-null structure in a scattering pattern tends to
concentrate — or purely a near-null relative-error blowup (small absolute
numerator, small absolute denominator, both near the solver's own
discretization/PML noise floor). **The classification's own normalization
choice makes this question un-askable by construction**, not merely
unanswered: even a doubling of the pattern in the lowest-signal bins
could not move `rel32` enough to register. This is exactly the "real
signature masked beneath the classification's own thresholds" scenario
the task brief named, and it was not caught by any of the five Phase-2
critiques or by Red Team's audit — all of which focused on the
box-radius-as-nuisance-parameter defect (§2b above), a real and different
issue, not this one.

**What this does and does not mean for the CONFIRM verdict.** For the
angular sectors that carry the bulk of the scattered power — where the
comparison this instrument is actually sensitive to lives — the result is
genuinely strong: deviations there sit ~300× below the 5% bar (max
`rel32` = 1.5×10⁻⁴), not a close call at all, for a mechanism (T9's
core-irrelevance null) that is itself independently well-supported. I do
not dispute that the dominant-lobe null generalizes. What I dispute is
NOTES.md's own framing that this was "the first genuinely two-sided test
that **could have found a real angular signature** and did not" — as
built, the test could not have found a signature confined to the
low-cross-section side/back-scatter sectors, which is most of the
angular domain by bin count. The CONFIRM should be read as scoped to the
forward-lobe-dominated shape, not the full 360°.

### 3c. Item ii's own "unified fix" detrending is ungated for fit quality — and fails its own implicit premise at r=312

Red Team's own combined fix (§3 of `phase2_redteam_audit.md`, adopted as
the cycle's "deepest finding") rests on the premise that the six-margin
`Δ(abs_ext_ratio)` sequence carries a real, physically-expected
near-to-far-field convergence trend that must be detrended (fit to
`A + B/margin`) before the residual is trusted as a noise floor. I
recomputed the fit diagnostics directly:

| r | sequence monotonic? | R² of `A+B/margin` fit | raw `std` | detrended `residual_std` | reduction |
|---|---|---|---|---|---|
| 156 | No | 0.665 | 5.01×10⁻⁶ | 2.90×10⁻⁶ | ~42% |
| 312 | No | **0.021** | 2.12×10⁻⁶ | 2.10×10⁻⁶ | **~1%** |

At r=312 the fit explains essentially none of the six-point sequence's
variance — detrending removes almost nothing, and the "genuine, detrended
floor" NOTES.md reports there is numerically indistinguishable from the
raw, un-detrended `std` that QUANTUM's own Phase-2 critique specifically
warned against trusting. Item i's own classification, built from the
identical fit function, correctly requires a quality gate before trusting
a fit's shape (`smooth = is_monotonic or r_squared ≥ 0.90`) before ever
letting a migration-based REFUTE stand; item ii applies no analogous
gate — the residual is reported as "the genuine floor" regardless of
whether the fit that produced it is any good. This is an internal
inconsistency in how rigorously the same machinery is trusted across the
two items sharing it, introduced this cycle, not caught by Phase 2 or Red
Team (the actual fit-quality numbers did not exist until Phase 4). It is
non-load-bearing here — both r pass CONFIRM whether the raw or detrended
statistic is used (2.12–5.01×10⁻⁶ either way, against a 1.23–1.48×10⁻⁵
CONFIRM bar) — but it means Red Team's own "deepest finding" premise
(box radius carries a real, removable convergence bias) is only
partially borne out by this cycle's actual data, and not at all at
r=312, where the six points are closer to noise-scattered than to any
smooth trend.

### 3d. The smooth-migration discriminator — the audit's own novel machinery — shipped with no positive control

`linear_fit_1_over_margin`'s monotonic-or-`R²≥0.90` smooth/noise
discriminator is the one genuinely new piece of classification logic this
cycle introduces (beyond reused conventions), and Red Team named it
explicitly as this audit's deepest finding. It is invoked only inside
`classify_item_i`'s `run_details` loop — and because zero candidate bin
runs ever cleared the 15% REFUTE bar at margin=32, at either r
(`runs=[]` both times, confirmed by direct re-run), **that loop body never
executed on real data this cycle.** Unlike item iv's own new machinery
(the chunked/continuous suite stage), which R18 discipline correctly
required a paired positive **and** negative control for before trusting it
(both present, both PASS, independently reproduced above), the
smooth-migration discriminator has no synthetic positive control anywhere
in this codebase or in the trust suite — nobody has verified, on a known
injected smooth-migration or known-noise sequence, that `smooth=True`/
`False` actually falls out correctly. This is not a defect that changes
anything this cycle (there was nothing for it to classify), but it means
the mechanism Red Team called out as the deepest structural fix of the
audit is, as of this cycle's close, entirely unexercised — an R18-shaped
gap that nobody named for this specific piece of machinery the same way
it was named for item iv's.

---

## 4. Does this cycle re-tread RULED OUT ground?

No. Re-checked directly: T1 is correctly N/A throughout (no σ(I)/σ(x,t)/
angular-selectivity/sub-threshold mechanism is proposed, varied, or
scored by any branch of this cycle — confirmed by my own read of
`run.py`/`analyze.py`/`chunk_runner.py` in full, matching Red Team's own
grep). R23/R24/R25's registry text (LOGBOOK.md lines 908-1038) matches
what the proposal, critiques, and NOTES.md quote from it verbatim — I
re-grepped all three entries directly rather than trust the cycle's own
restatement, and confirm: R25 was already ratified at Iteration 84 (this
cycle's "ratify" line is bookkeeping, correctly labeled as such); R24 is
a distinct rule (same-cycle wiring gap) from R25 (cross-cycle queue-
survival gap), and this cycle's own patch discharges R25's founding
instance correctly, on the record, with the reclassified string quoted
inline as R25's own conditional required; R23's three-cycle-old scope
question is closed with a stated reason (not a re-deferral), and the
mandatory VISION live-fire check (`run.py --predictions-only`, grep for
`DISCLAIMER`) genuinely ran and genuinely passed (4 hits in `run.py`,
0 in the three non-text-generating scripts — correctly scoped). Nothing
here revives R1 (refractive cloaking), R5 (unconstrained-search
look-elsewhere), or any other foreclosed mechanism class — there is no
mechanism here to check against those rules in the first place.

---

## 5. Verdict: **CONFIRM-WITH-GAPS**

The governance work (Tier 0) is sound, correctly executed, and — unlike
the exp-106→107 precedent this cycle was built specifically to avoid
repeating — genuinely verified executed, not merely described. Every
headline number in Tier 1 reproduces bit-exact from primitives; the
CONFIRM/PASS verdicts item i/ii/iii/iv report are the numerically correct
output of the code as written, and I found no arithmetic error anywhere.
The angular-pattern null generalizing for the dominant, power-carrying
part of the scattering pattern is a real, well-supported finding, and the
box-radius-as-nuisance-parameter defect my own Phase-1 design shipped
(§2b) was genuinely fixed by Phase 3, not merely patched over.

The gaps are real and, individually, non-load-bearing to any scored
verdict, but they cluster in exactly the place my own charter is supposed
to watch hardest: **item i's own classification, even after the Phase-2
unified fix, cannot see a real angular signature confined to the
low-cross-section side/back-scatter sectors that make up roughly
two-thirds of the sampled angular domain** (§3b) — a genuine, previously
unflagged instrument-design blind spot, compounded by a pre-registered
floor-gate that was never implemented (§3a) and a "unified fix" premise
that only partially holds at r=156 and essentially does not hold at
r=312 (§3c). None of this overturns the CONFIRM — the forward-lobe result
is genuinely strong — but NOTES.md's own "the first genuinely two-sided
test that could have found a real angular signature and did not" is
overclaimed relative to what was actually tested, and should be corrected
to state the CONFIRM's true scope (dominant-lobe shape only) explicitly
before any future cycle cites it as closing the angular question in
full. I also carry two of my own Phase-1 defects into this record (§2a,
§2b, both already caught and fixed) plus one new one I found this shift
(§2c, non-load-bearing).

---

## 6. The single most important thing for Iteration 86

**Re-normalize (or floor-gate) item i's per-bin comparison before this
instrument is trusted on the low-cross-section angular sectors at all.**
Concretely: report `|Δpattern(θ)|` relative to each bin's OWN local
`σ_scat_per_bin[PEC-cored]` magnitude (not the global max), gated by a
genuine, freshly-computed per-bin absolute noise floor (comparable in
spirit to item ii's own six-margin detrending, but built for a per-bin
quantity, in the right units this time) — zero new `Sim.run()` calls,
since all six margins' full 48-bin arrays already sit in this cycle's own
committed captures. Until that exists, this cycle's own CONFIRM should be
cited as "the forward-dominated scattering shape is interchangeable
between hollow and PEC-cored fill" — not as "the angular pattern is
interchangeable," full stop.
