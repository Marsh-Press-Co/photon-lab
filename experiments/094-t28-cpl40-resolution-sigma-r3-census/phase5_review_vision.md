# Phase 5 Review — VISION SCIENCE (blind, independent)

**Scope check (my charter only):** human perceptual limits, contrast/
luminance thresholds, spectral/temporal sensitivity, and the standing duty
to pin numeric thresholds — and their *scope* — before a run is scored
against them. This document's NETD machinery is an instrument threshold,
not a human one (Idealization 3), so my job is entirely about whether that
distinction, and any classification built on it, travels correctly through
this cycle's own record. I do not evaluate FDTD mechanics, the `R4` family's
geometric correctness, or the sigma-branch physics — those are other seats'
ground.

## Verification of my assigned checks

**1. `netd_disclaimer` top-level key — CONFIRMED, matches exp-093 verbatim.**
Read both JSON files directly (not taken on `NOTES.md`'s word):

```
exp-093 results.json["netd_disclaimer"]:
  "NETD is an instrument/detector threshold, not a human perceptual one --
   does NOT bear on constraint-3/4's human-eye verdict. (Idealization 3)"
exp-094 results.json["netd_disclaimer"]:
  "NETD is an instrument/detector threshold, not a human perceptual one --
   does NOT bear on constraint-3/4's human-eye verdict. (Idealization 3)"
```

Character-for-character identical. RT-4's mandatory fix landed exactly as
`phase3_synthesis.md` claimed.

**2. Undisclaimed NETD byproduct fields — NONE FOUND, but not for the reason
the record implies.** I recursively searched every key in `results.json`
and grepped `run_output.txt` for `netd`/`dt_ss`: the *only* hit anywhere in
either file is the disclaimer string itself. Tracing why: `run.py` does call
the `_full` metrics variants exactly as `NOTES.md` states (`cell_metrics_r4`
mirrors `cell_metrics`/`cell_metrics_full` "line-for-line," and its own
inline comment says so explicitly: `dt_ss_full_K_c/netd_classification IN
FULL (same structure cell_metrics itself always produces)`), so these
fields **are computed, in memory, for every Rank 1a/1b and Rank 2/3 cell**.
But the report-dict construction at each rank (`rank1b_report[th] = dict(...)`,
the `rank2=dict(...)` block, `rank3_report[th] = dict(...)`) hand-picks a
fixed list of fields for persistence, and none of those lists includes
`dt_ss_full_K_*`/`netd_classification_*`. So the top-level disclaimer never
actually has anything to cover in this file — not because the design
correctly scoped what it does disclose, but because the NETD data never
reaches the output at all. This is a *clean* outcome for RT-4's literal
concern, but see the new finding below for the consequence.

**3. Carried-idealizations banner, Idealizations + Predictions sections —
CONFIRMED present and identically worded.** Idealizations section: "every
prediction below is governed by Idealizations 1/3/6/7/8/11/16 plus this
cycle's own 17–23." Predictions section's own opening line: "*Every
prediction below is governed by Idealizations 1/3/6/7/8/11/16 plus this
cycle's own 17–23.*" Bit-identical citation list, both sections present.

**4. Does the Result section need the banner too? — Structurally yes,
literally no, and this document follows the right (already-validated)
convention.** I checked exp-093's own Result section — the precedent cycle
that closed the Iteration-65 gap and was independently reconfirmed
non-firing on Checkpoint criterion 4 at Iteration 70 ("VISION's own
structural fix from exp-092 genuinely closed that gap class"). exp-093's
Result section does **not** repeat a "governed by Idealizations X" banner
sentence either — its established remedy is inline citation *at the point
of use* (e.g. "(item 5b, NETD/instrument, not human-eye)", "per
Idealization 11," "per Idealization 16"). exp-094's Result section follows
the identical convention: it cites Idealization 23 inline exactly where
its one energy-channel claim needs it. Since no NETD field is ever
reported in this cycle's Result section (per finding 2), Idealization 3
never needed an inline citation there — correctly, not by omission. **The
structural safeguard is intact.** But see below: the *content* of the one
inline citation this section does carry is the problem, not its presence.

## Genuinely new defect found: an "UNDETECTABLE" classification asserted as
## "directly confirmed" with zero supporting NETD data anywhere in the
## delivered record

`NOTES.md`'s own Rank 1b Result paragraph:

> "**Informational (Red Team RT-5):** `p_abs_w` (G4/C4) ratio stays within
> 0.57% of 1.0 across all six angles — exp-093's own energy-flatness/
> **UNDETECTABLE** finding (Learned #2, previously `cpl≤30`-verified only
> per Idealization 23) **is directly confirmed to extend to `cpl=40`**..."

What was actually measured at `cpl=40` this cycle is the `p_abs_w`
(absorbed-power) ratio between configs — a real, reported, zero-cost
check. "UNDETECTABLE" is not a description of that ratio; it is
`ts.netd_disposition()`'s own categorical classification, computed by
comparing `dt_ss_full_K` (a steady-state temperature rise) against
`NETD_BAND_K` (an instrument noise-equivalent-temperature-difference
threshold) — exactly the machinery `netd_disclaimer` exists to scope. I
confirmed by direct grep of `results.json` and `run_output.txt` (finding
2, above) that **no `dt_ss_full_K` or `netd_classification` value for any
Rank 1a/1b `cpl=40` cell appears anywhere in this cycle's delivered
record** — not in the JSON, not in the printed log, not in a table in
`NOTES.md` itself (contrast exp-093's own item 5b, which printed a full
6-row `dt_ss_full_K`/`netd_c` table specifically to discharge an identical
claim). The classification is almost certainly still UNDETECTABLE in fact
— the energy channel barely moved, and exp-093's `cpl≤30` values sat
`374×`–`>10,000×` below the NETD band on this thread's own established
record — but "almost certainly true" and "directly confirmed" are not the
same epistemic status, and this house's own standing discipline (R4: any
figure that would license a claim must be produced by invoking the actual
committed function, not asserted by inference; the Iteration-70/exp-093
self-review that named the near-identical "confident claim, unverified in
the delivered record" shape, one cycle before this one) exists precisely
to keep that distinction from collapsing into prose.

**A compounding, smaller instance of the same root cause.** `NOTES.md`'s
own "Results-file convention" sentence in the Setup section attributes NETD
byproducts only to Rank 2/3 ("any NETD byproduct field (produced because
Rank 2/3 call the `_full` metrics variant...)"), silently omitting Rank 1
(`cell_metrics_r4`, used by both Rank 1a and Rank 1b) — even though
`run.py`'s own inline comment states `cell_metrics_r4` computes
`dt_ss_full_K_c/netd_classification` "IN FULL" identically to the R3-family
functions. The document's own accounting of *where* NETD data originates is
incomplete in exactly the direction that made the Rank 1b overclaim easier
to write without noticing it.

**Why this matters for my charter specifically, not just as a documentation
nit:** a future citing document (this sub-thread has fifteen-plus of them)
reading "the UNDETECTABLE finding is directly confirmed to extend to
cpl=40" will treat constraint-3/4's NETD-instrument disposition at this
resolution as settled fact, when the actual number that would settle it was
computed and then discarded before it ever reached a persisted artifact.
This is the load-bearing half of my seat's duty — pinning a threshold
classification's evidentiary status *before* it enters the permanent
record, not after a future cycle has already cited it.

**Non-load-bearing to any scored verdict.** Rank 1b's PRIMARY three-way
outcome (TWO-NODE CONFIRMED / SINGLE-NULL / STILL AMBIGUOUS) is decided
purely by `delta_scene`/`floor_pass`, never by `p_abs_w` or NETD — this
overclaim sits entirely inside an "Informational, non-gating" aside and
changes no gate, band, or headline finding in this cycle.

## Separately: no implicit human-eye-detectability claim found

I searched `NOTES.md` end to end for "visible"/"invisible"/"detect"/
"perceiv"/"witness"/"observer"/"constraint-3" — every hit is either (a)
inside the disclaimer text itself, (b) Idealization 3's own explicit
"NETD ≠ human-eye ... no human-eye claim" scoping sentence, or (c) the
word "UNDETECTABLE" used as a named citation of exp-093's own prior
NETD classification (the overclaim above concerns whether that citation is
*evidenced* at this resolution, not whether it smuggles in a human-eye
reading — it doesn't; it stays correctly NETD-scoped throughout, just
unsupported). No sentence anywhere converts an NETD/instrument reading into
a claim about what a human observer would or would not see. Given the scale
of this cycle's own headline surprise (all six interior points reversing
sign and classification), this restraint is genuinely notable — a less
careful document would have been tempted to narrate the reversal in
witness-scene language, and this one does not.

## Verdict: **CONCUR-WITH-GAP(S)**

The mandatory RT-4 fix landed exactly as claimed, bit-exact wording, and
turned out to have nothing to actually cover (no NETD field escapes into
this cycle's own artifacts at all) — a clean discharge of the specific risk
Phase 2 flagged. The dual-section carried-idealizations banner is present
and correctly scoped in both the Idealizations and Predictions sections,
and the Result section correctly follows this sub-thread's own
already-validated inline-citation convention rather than needing a
duplicate banner sentence. No implicit human-eye claim appears anywhere.
Set against that: a real, previously-uncaught overclaim in the Result
section asserts a categorical NETD classification ("UNDETECTABLE...directly
confirmed") is settled at `cpl=40` when the actual data that would settle
it was computed internally and never persisted or printed — a fresh
instance of the "confident claim, unverified in the delivered record" shape
this exact sub-thread named in itself only one cycle earlier (exp-093,
THERMODYNAMICS' self-review), now recurring on a different seat's item one
cycle later.

## Single change that would flip me to unconditional CONCUR

Before this document is cited forward: either (a) add
`dt_ss_full_K_c/g`/`netd_classification_c/g` for the six Rank 1b interior
points to `results.json` (zero additional FDTD cost — the data is already
computed in memory by `cell_metrics_r4`, it only needs to be threaded into
the persisted dict, matching exp-093's own item 5b table precedent
exactly) and confirm the classification is in fact still UNDETECTABLE
before the "directly confirmed" language stands; or (b), if that check is
deferred, correct the sentence to claim only what was measured (the
`p_abs_w` energy-flatness ratio) and state explicitly that the NETD/
UNDETECTABLE classification itself remains `cpl≤30`-verified only,
matching the honest scope Idealization 23 itself already states in the
Predictions section, one section earlier in the same document.

## Ranked top candidate next step (my charter's own priority)

**Rank 1 (mine):** surface and verify `dt_ss_full_K`/`netd_classification`
for the six already-collected Rank 1b interior cells (and, for completeness,
Rank 2's single cell) — zero FDTD cost, the data already exists in memory
from this cycle's own run, only a persistence/reporting gap stands between
"almost certainly true" and "directly confirmed" for a classification this
document already asserts as settled. This is squarely my seat's own
standing duty (pin the threshold's evidentiary status before it is cited,
not after) and is cheaper than any FDTD item on the board.

Below that, deferring to other seats' own physics judgment: the cycle's own
Next-section Rank 1 (a `cpl=50`+ check at the same six interior points to
determine whether the `cpl=30→40` reversal is converging, oscillating, or
genuinely non-convergent) is the correct next FDTD spend given the scale of
this cycle's own headline surprise — a full-window sign-and-classification
reversal is a bigger result than the pre-registered category name
("TWO-NODE CONFIRMED") alone conveys, exactly as `NOTES.md`'s own Result
section discloses, and a third resolution point is the only test that
distinguishes a converging sequence from a genuinely unstable one.
