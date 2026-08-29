# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (blind) · exp-089 · Panel Iteration 66

*Fresh context. Read: PANEL.md in full; LOGBOOK.md's RULED OUT (R1–R14) in
full, the ESTABLISHED section, and LIVE THREADS/T28 (Iterations 58–65, both
CHECKPOINT entries) in full through Iteration 65/exp-088; the complete
exp-089 cycle record (`phase1_proposal.md`, all five Phase-2 critiques,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `results.json`,
`run.py`); `experiments/088-.../phase5_review_materials.md` for house-style
calibration. Independently recomputed every load-bearing number below from
primitives — not trusted from any prose restatement, including my own
seat's from exp-088.*

## 0. Verdict

**CONCUR-WITH-GAP.** The frozen cycle executed exactly as specified; all
nine of Red Team's Phase-2 fix-docket items landed correctly; every
arithmetic claim I independently re-derived reproduces bit-for-bit,
including the one this seat was specifically tasked to check —
`FLOOR=1.91744×10⁻⁴` is genuinely, bit-identically reused, not drifted. But
`NOTES.md`'s own Learned/Next sections — written after Q5's own finding
that `FLOOR_FRAC=0.10` is inadequately protective — propose "revisit
`FLOOR_FRAC`" as this cycle's own second-priority forward action without
restating the material-and-wavelength scoping caveat that governs exactly
that action, in a section pair the mandatory dual-section banner rule does
not literally cover. This is a live instance of the shape my own seat named
at exp-088 and the shape this sub-thread has now fired Checkpoint criterion
4 on four times — not yet a violation (nothing is claimed wrongly), but an
open door for exactly the drift those firings exist to prevent.

## 1. Independent recomputation — FLOOR reuse, R13 margins, and the resolved-margin table

Computed fresh from `experiments/083-.../results.json::per_theta` raw
fields and `experiments/089-.../results.json`, by an independent script,
not by trusting any cited table:

| Quantity | My independent computation | Cited (exp-089) | Match |
|---|---|---|---|
| RMS[frac_contrast], n=31 | `1.9174375118374476×10⁻³` | `1.917438×10⁻³` | exact |
| FLOOR (`0.10×RMS`) | `1.9174375118374476×10⁻⁴` | `1.91744×10⁻⁴` | exact, **and bit-identical to exp-088's own filed `r13_floor_gate.floor`** |
| `frac_contrast(37.2°)` | `4.162655×10⁻⁴` (margin 2.1709×) | matches | exact |
| `frac_contrast(40.2°)` | `2.830881×10⁻⁴` (margin 1.4764×) | matches | exact |
| `frac_contrast(41.4°)` | `2.510967×10⁻⁴` (margin 1.3095×) | matches | exact |
| `ratio_k(37.2°/40.2°/41.4°)` | `3.4433 / 25.082 / 28.807` | matches | exact |
| noise-floor resolved margin, 37.2° | `1.0457×` | `1.046×` | exact |
| noise-floor resolved margin, 40.2°/41.4° | `2.0870× / 4.6849×` | `2.087× / 4.685×` | exact |
| prior smallest resolved margin on record (exp-087 36.0°/38.6°/41.8°, exp-088 38.4°/38.8°) | `3.196× / 4.487× / 10.666× / 2.696× / 4.224×` | — | 37.2°'s `1.046×` genuinely IS the thinnest ever accepted (Result section's "thinnest ever" claim independently verified TRUE, not a repeat of the false superlative Red Team caught in the Phase-1 draft) |

No arithmetic, citation, or indexing defect found anywhere in the final
record. Every number in `NOTES.md`'s Result section that I re-derived from
`results.json`'s raw `thermo`/`box_dev` fields reproduces exactly.

**On the specific question this seat was tasked to answer — is FLOOR
genuinely reused bit-identical, not silently recomputed or drifted —
the answer is yes, with one mechanistic precision worth stating.**
`run.py` does not carry FLOOR forward as a hardcoded copied literal; it
calls `compute_floor()` — the *identical function object*, imported
directly from `exp088.compute_floor` (`exp088 = _load(EXP088_DIR/run.py,
...)`, line 60 of `run.py`) — which re-reads `experiments/083-.../
results.json::per_theta` (unchanged) and recomputes RMS/FLOOR fresh at
runtime. This is a *deterministic re-invocation*, not a literal reuse of a
stored constant, and `phase1_proposal.md`'s own §2 table phrase ("zero new
computation") is technically imprecise — there is a new computation, it is
just guaranteed identical because both the function and its inputs are
identical. I confirm this is **not a defect**: the value reproduces
bit-exact (`0.00019174375118374476` in both `results.json` files, matching
my own from-scratch recomputation above), so no drift occurred and the
mechanism (re-invoking the same function against unchanged upstream JSON,
via direct Python import rather than retyped numbers) is in fact a
*stronger* non-drift guarantee than a hand-copied literal would be — a
transcription error is structurally impossible here. Flagged only for
future prose precision, not escalated.

## 2. Charter question: does the Learned/Next FLOOR_FRAC-revisit proposal risk becoming an under-scoped house-wide default?

**This is the live gap.** `NOTES.md`'s Result section, at the one place
Q5's finding is directly stated, gets the scoping right: *"Whether the
correct fix is tightening `FLOOR_FRAC`, a graduated caution zone instead of
a binary gate, or something else is explicitly left to Phase 5 — this
document does not pre-judge it (Idealization 16)"* (line 321) — the
material-and-wavelength-specificity disclaimer is present, inline, exactly
where the mandatory dual-section rule requires it.

But the document does not stop at Q5. Learned item 2 (*"R13's
`FLOOR_FRAC=0.10` looks materially too permissive... the first real
evidence the gate's calibration, not merely its existence, needs
revisiting"*) and the Next section's own forward action (*"revisit
`FLOOR_FRAC` itself given Learned item 2 — a tightened threshold (e.g.
0.20–0.30×RMS) recomputed once against this cycle's now-larger sample, or a
graduated caution zone replacing the binary gate"*) carry **zero** inline
restatement of Idealization 16 anywhere in either passage — confirmed by
full-text search (`grep -n "Idealization 16\|graded_black_shell\|
material-and-wavelength" NOTES.md`): the only hits inside the Learned/Next
region are the bare, unqualified string `FLOOR_FRAC` at lines 357 and 397,
with no adjacent scoping language.

This matters for a reason specific to my charter, not a generic
disclaimer-hygiene complaint. `FLOOR` (the absolute threshold, in
`frac_contrast` units) is architecturally scene-specific by construction —
every cycle recomputes it from `experiments/083-.../results.json`, so a
different material or wavelength forces a fresh computation by construction
even if nobody remembers to. `FLOOR_FRAC` (the *fraction*, 0.10) is
different in kind: it is a bare, dimensionless Python module constant
(`FLOOR_FRAC = 0.10` in `experiments/088-.../run.py` line 93), carried
forward into exp-089 by the identical direct-import idiom
(`FLOOR_FRAC = exp088.FLOOR_FRAC # 0.10, unchanged`, `run.py` line 96) that
this sub-thread uses for every genuinely material/wavelength-invariant
convention (`NOISE_MULT`, `XI_TOL`, box clearances). Nothing about that
import mechanism forces a future cycle chaining through exp-089 the same
way to re-derive `FLOOR_FRAC` for a new context — it would simply inherit
whatever numeric value a future "recompute" leaves behind, exactly as
exp-089 inherited `0.10` from exp-088 without re-examination (correctly, in
this case, because material/wavelength are genuinely unchanged — see §1).
*Whether* `FLOOR_FRAC`'s own **adequacy** (as opposed to `FLOOR`'s raw
value) is itself material/wavelength-specific is precisely this cycle's own
new finding: Q5 showed a fraction calibrated as "protective" at ≥3× margin
elsewhere already fails by a wide margin at 1.3–1.5× on `graded_black_shell`
/600nm's own channel — nothing in the record establishes whether that
adequacy failure is a property of *this* absorber's own `frac_p_abs`
subtractive-cancellation scale (R14) relative to *this* denominator's own
RMS, or a universal defect of any 0.10 fraction. Recomputing `FLOOR_FRAC`
"once against this cycle's now-larger sample" and filing the result without
restating that scope, in a section (Learned/Next) the existing mandatory
banner rule does not literally reach, is exactly the mechanism by which a
number tuned to one material/wavelength's own hazard profile could quietly
become the next cycle's inherited, unexamined default — the same failure
shape my own exp-088 Phase-5 review flagged (§1 there: *"the risk... a
*future* cycle citing the bare number without recomputing it... remains
live as a forward risk"*), now recurring one cycle later in a slightly
different document region.

**Not currently a violation.** Nothing in exp-089's own record misapplies
`FLOOR_FRAC` outside `graded_black_shell`/600nm — confirmed by full-text
grep, matching my own exp-088 finding that no cross-material reuse occurs
inside a cycle's own scope. This is a forward-risk finding about what
Iteration 67 is set up to inherit, not a defect inside this cycle.

## 3. A second, related continuity gap: my own exp-088 ranking item 1 (the R3 spatial-resolution check) is neither executed nor disclosed as still-deferred

My own seat's Phase-5 review of exp-088 ranked, #1 priority: *"Run an
R3-mandated `cpl` resolution check on the `sigma_abs`/`frac_p_abs`
energy-interception channel... before any future cycle treats the dip as
physics or extends this channel to a new material."* LOGBOOK's own
Iteration-65 CHECKPOINT reconciled queue independently named the identical
item as Tier-1 item 3 (*"both a temporal AND, for the first time on this
channel, a spatial (`cpl`) resolution check at 38.4° — R3's own standing
meta-rule, directly triggered, undischarged"*), distinct from Tier-1 item 1
(the combined census exp-089 executes) and item 2 (a sub-grid bracket at
38.4°→38.6°, also not executed this cycle).

Grep confirms `cpl`/"resolution check"/"R3" appear nowhere in
`phase1_proposal.md` or `NOTES.md` beyond the routine `CPL[600]=20` grid
constant citation — no Idealization or Next-section line names this
specific still-open item, even though Idealization 14 explicitly itemizes
several *other* deferred items by name (Red Team's Iteration-65 "~124-call"
item, PHOTONICS' grazing-incidence check, the x-wall leg). The channel this
cycle now shows non-monotonic at THREE angles (38.4°, and by the newly
disclosed dip character, plausibly near 40.2°/41.4° too) still has never
received a spatial-resolution convergence check — the exact gap now
carries more weight than when I first named it, since exp-089's own two new
ENERGY-DOMINANT readings are additional data this channel's un-validated
resolution could in principle be shaping. This is a lower-severity finding
than §2 (it is an omission from an itemized deferred-work list, not a
scoping risk on an active forward proposal) but belongs on the record.

## 4. Other findings from my own lens

- The article/config pair (`pec_disk(r=30)` + `graded_black_shell(r_in=30,
  r_out=78, sigma_max=0.5, eps_max=1.0)`) is confirmed bit-identical to
  exp-024/082/083/087/088's own construction via the `run.py` import chain
  — no new material or geometry, so no new realizability question arises
  from the article itself this cycle (consistent with Idealization 10).
- Idealization 10's refusal to re-open `REALIZABILITY_MEMO.md`'s verdict
  (PLAUSIBLE-not-PUBLISHED, `graded_black_shell`, Iteration 29/exp-052) is
  correct and consistent with the existing record — this cycle's finding is
  a scene/energy-bookkeeping fact about `ratio_k`, not a claim about bulk
  shell realizability. MATERIALS' own Iteration-59 "zero realizability
  content" framing rule continues to apply cleanly.
- The Idealization-15 self-check bug (a naive in-file string search that
  matches its own diagnostic text, honestly disclosed in the Result
  section rather than silently patched) is a genuine but non-load-bearing
  defect, already correctly self-caught and correctly distinguished from
  the substantive claim it was meant to verify (which independent manual
  grep still confirms true). No further action needed from this seat.
- `Idealization 13`/Q4's "raw numbers only, not scored" treatment is
  applied consistently in the Result section — I confirm no place in
  `NOTES.md` treats Q4's descriptive numbers as evidence for or against
  Q3's ENERGY-DOMINANT finding, correctly implementing Red Team's own
  §7.1 decoupling requirement.

## 5. Sharpest finding

**NOTES.md's Learned/Next sections propose revisiting `FLOOR_FRAC` — a bare
module-level constant this sub-thread's own import idiom carries forward
by reference into every future cycle that chains through exp-089 the way
exp-089 chained through exp-088 — as this cycle's own named second-priority
forward action, without restating anywhere in that region the
material-and-wavelength scoping caveat (Idealization 16) that governs it,
even though the adjacent Q5 paragraph four lines earlier in the same
document gets this exactly right.** This is not yet a violation — no
cross-material misuse occurs inside exp-089's own scope, confirmed by full
grep — but it is a structurally live vector for the same class of drift my
own exp-088 review flagged as a forward risk, in a document that is, this
same cycle, the second consecutive T28 cycle to carry the mandatory
dual-section banner specifically because a scoped-in-one-place disclaimer
has now failed to propagate four times running. The Learned/Next sections
sit outside the banner rule's literal text (Predictions + Result only) —
exactly the kind of section-boundary gap that shape has already exploited
once (Iteration 65/exp-088's own Q4-Result-paragraph firing) and could
exploit again here if Iteration 67 inherits `FLOOR_FRAC`'s recomputed value
without re-deriving whether its adequacy, not just `FLOOR`'s raw number, is
material/wavelength-specific.

## 6. Ranked top-3 for the Director's Iteration-67 queue

1. **Before any `FLOOR_FRAC` recomputation is filed as a new value: state
   explicitly, adjacent to that recomputation, whether the new value is
   scoped to `graded_black_shell`/600nm specifically or is being proposed
   as a revised house-wide default — and if the latter, name what
   independent evidence (beyond this one material/wavelength's own R14
   numerator-hazard scale) justifies treating a fraction tuned here as
   portable.** Cheapest, highest-priority fix — a single sentence, zero
   FDTD cost, closes §2's forward risk before Iteration 67 inherits the
   ambiguity by import.
2. **Run the still-outstanding R3 spatial-resolution (`cpl`) convergence
   check on the `sigma_abs`/`frac_p_abs` channel** (my own exp-088 ranking
   item 1, LOGBOOK's own Iteration-65 CHECKPOINT Tier-1 item 3, undischarged
   two cycles running) — now strengthened by exp-089's own finding that the
   channel is non-monotonic at more than one location, not an isolated
   38.4° feature. Should be named explicitly as still-deferred in whatever
   document next revisits this channel, not silently absent from the
   itemized-deferrals list the way it is here.
3. **Densify around 40.2°/41.4° (NOTES.md's own named "Next" first
   priority)** — genuinely the cheapest, most decisive next FDTD step for
   the channel's own substantive question (isolated spikes vs. a broader
   elevated band), and correctly ranked ahead of the FLOOR_FRAC revisit in
   NOTES.md's own text. My only addition: run it BEFORE any `FLOOR_FRAC`
   recalibration is attempted, since a wider bracket at these two angles
   will supply more of the "larger sample" the recalibration itself is
   meant to use — sequencing item 3 before the FLOOR_FRAC half of item 1
   above gives the recalibration better-conditioned data to work from.
