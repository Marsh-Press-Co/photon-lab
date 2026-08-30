# PHASE 5 REVIEW — THERMODYNAMICS (blind) · exp-094 · Panel Iteration 71

*Fresh sub-agent, THERMODYNAMICS charter: where absorbed energy goes; owns
the per-proposal energy sidecar (absorbed power → temperature rise →
emission band → detectability), expressed as a post-run analytic
calculation, labeled as such. Read in full: PANEL.md, LOGBOOK.md (RULED OUT
R1–R15, ESTABLISHED, LIVE THREADS T1–T28 in full), PLAN.md's Current-state
section, and the complete exp-094 record (`phase1_proposal.md`, all five
Phase-2 critiques including my own prior-cycle critique that RT-5
elevated, `phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md` in
full, `run.py`, `results.json`, `run_output.txt`). Did not read any other
seat's Phase-5 review or the Phase-5 Red Team audit. All numbers below were
independently recomputed from `results.json`'s raw fields and cross-checked
against `run.py`'s source — none taken from `NOTES.md`'s own prose
restatement on faith.*

## Verdict: **CONCUR-WITH-GAP(S)**

## 0. Independent re-verification of RT-5's own headline number

Pulled `rank1b.per_theta` directly from `results.json` and recomputed
`p_g/p_c` (the G4/C4 `p_abs_w` ratio) from the raw `p_c`/`p_g` primitives at
all six angles, not from the stored `pg_pc_ratio` field:

| θ | p_c (W) | p_g (W) | p_g/p_c | dev. from 1.0 |
|---|---|---|---|---|
| 41.750° | 3.221140042e-12 | 3.239620140e-12 | 1.0057371297 | **0.5737%** |
| 41.775° | 3.226608851e-12 | 3.243693396e-12 | 1.0052948920 | 0.5295% |
| 41.825° | 3.237396951e-12 | 3.251543041e-12 | 1.0043695879 | 0.4370% |
| 41.850° | 3.242689157e-12 | 3.255302127e-12 | 1.0038896636 | 0.3890% |
| 41.875° | 3.247895629e-12 | 3.258939639e-12 | 1.0034003586 | 0.3400% |
| 41.900° | 3.253003257e-12 | 3.262447681e-12 | 1.0029032937 | 0.2903% |

Bit-exact match to my own hand recomputation, to `results.json`'s own
`pg_pc_ratio` field at every angle, and to its own
`pg_pc_ratio_max_dev_pct_informational=0.5737129680636555`. **NOTES.md's
"stays within 0.57% of 1.0 across all six angles" reproduces from
primitives — CONFIRMED, not merely restated.** One precision nit, non-load-
bearing: the true max is 0.5737%, so "within 0.57%" read as a strict upper
bound is off by 0.0037 points (0.57% is the correctly-*rounded* figure, not
a valid ceiling) — worth "≲0.6%" in a future citation, not worth a fix here.

**A genuinely new observation this independent recompute surfaces, not
stated anywhere in `NOTES.md`:** the six deviations are not scattered around
a noise floor — they fall **monotonically** from 0.574%→0.530%→0.437%→
0.389%→0.340%→0.290% as θ increases from 41.750° to 41.900°, a clean,
smooth, ~2× fall across the window. "Flat" is the right verdict for the
*decision* (nothing here threatens UNDETECTABLE or contaminates
`delta_scene`), but the underlying quantity is not literally noise-floor-
flat — it carries a small, real, monotonic angular trend, the same
qualitative shape (small, smooth, continuous) MATERIALS' own T10 argument
invokes to explain why the *coherent* channel moves continuously rather
than discontinuously under refinement. That the energy channel shows an
analogous smooth structure, at ~50× smaller amplitude, is worth carrying
forward as a data point, not a threat.

## 1. The core question: is one `cpl=40` point at one window sufficient to call the energy channel "resolution-robust"?

**No, and NOTES.md itself does not actually claim that — but it comes close
enough that the distinction needs stating explicitly for the record.**
Learned #2 is correctly scoped in its own text ("applied specifically to
this near-null band," "in the identical window") — it does not claim
flatness holds anywhere `p_abs_w` hasn't been measured. That scoping is
sound and should not be walked back.

But the framing invites exactly the over-generalization the review brief
asks me to guard against, for a structural reason specific to my own
discipline's charter question ("does absorbed energy also move here?"):
this cycle's own single most dramatic finding — 38.4° FLIPPING by a
factor of ~19× (Rank 3) — sits in a **different** near-null than the
41.6°–42.0° window Learned #2 is scoped to, and **has no `p_abs_w`
companion check at any resolution, not even the `cpl=30` at which the
flip itself was measured** (§2, below). So the honest current state is:
the energy channel has been checked, and found flat, at exactly the two
locations this cycle happened to budget it for (41.6°, and the six
41.75°–41.90° points) — not at the location this cycle's own data most
directly motivates checking it. Symmetric to the review brief's own
framing of the coherent channel's history: `delta_scene` looked settled at
two resolutions before failing at a third: `p_abs_w`'s own "never moves"
run has, if anything, *fewer* independent test locations behind it than
`delta_scene` had before its reversal, even though it has now survived
three resolution points at the one location it has been checked.

## 2. Genuinely new defect #1 — the newest, largest flip this cycle discovered has zero energy-channel check

Traced `run.py`'s Rank 3 block end-to-end. `pair_metrics_full` is called at
line 536 for all three census angles (36.0°/38.4°/38.8°), and — confirmed
by reading `pair_metrics_full`'s own source in `experiments/093-.../run.py`
— its return dict already carries `p_c`/`p_g`/`frac_p_abs` (computed at
zero marginal FDTD cost, forwarded straight from each cell's own `thermo`
dict). But `rank3_report` (`run.py:545-550`) extracts only `delta_scene`,
`frac_contrast`, `ratio_k`, `floor_pass`, and the two `Y` labels — **no
`p_abs_w`/`frac_p_abs` field anywhere in Rank 3's output**, confirmed absent
from `results.json`'s `rank3` block and from every line of `run_output.txt`
(grepped both). This means 38.4° — the site of the cycle's own largest
reversal, larger in absolute swing than the 41.4° precedent that motivated
an entire prior cycle's design (exp-092) — has never had the one
zero-marginal-cost check (`p_abs_w` vs. the 0.51 T9 anchor) that was applied
to its sibling item (Rank 2) and to the interior sweep (Rank 1b). RT-5's own
mandate was scoped to Rank 1b only; nothing in Phase 2/3 named this gap on
Rank 3, and it is a live, affordable, previously-unflagged omission on
exactly the point this cycle's own review-brief question is most pointed
at.

## 3. Genuinely new defect #2 — the NETD byproduct itself is silently dropped for every item this cycle, reproducing a named, previously-tripwired pattern

Checked the `netd_disclaimer`/RT-4 question directly, as asked:

- **The top-level `netd_disclaimer` key landed correctly.** Confirmed
  present in `results.json` (verbatim match, byte-for-byte, against
  `experiments/093-.../results.json`'s own string — checked
  programmatically). Printed once in `run_output.txt` (line 156). RT-4's
  literal mandate is satisfied.
- **But every NETD byproduct field the `_full` machinery actually computes
  this cycle is silently discarded, for all three ranks.** Traced source:
  `pair_metrics_full` (Rank 2/Rank 3) and `cell_metrics_r4`'s own `thermo`
  dict (Rank 1a/1b, via `ts.netd_disposition`/`ts.mixed_length_scale_regime`)
  both compute `dt_ss_full_K`/`netd_classification` (both configs) at every
  cell this cycle ran with an article present — confirmed by reading
  `cell_metrics_r4` (`run.py:295-342`) and `pair_metrics_full`
  (`experiments/093-.../run.py:167-182`) directly. Grepped exp-094's own
  `run.py`, `results.json`, and `run_output.txt` for `netd_classification`
  and `dt_ss_full_K`: **zero hits anywhere outside the function
  definitions/docstrings that compute them.** Not one NETD classification
  or temperature-rise value from this cycle's 20 article-bearing cells
  (4 Rank 2 + 12 Rank 3 + 4 Rank 1a-settling-pair, before Rank 1b) is
  reported anywhere.
- This is the *exact* shape LOGBOOK.md's own record names and explicitly
  set a forward tripwire for: Iteration 69 (exp-092)'s Phase-5
  THERMODYNAMICS review found `netd_disposition` "computed for every cell
  but never persisted or printed," traced back latent to exp-091, ruled
  "first-time naming... a forward tripwire set explicitly for a third
  occurrence." exp-093 (Iteration 70) then built a dedicated `netd_row()`
  helper *specifically* to close this gap for its own items 1/3/5 — its own
  docstring says so verbatim ("matching Iteration-69 LOGBOOK's own named
  truncation defect... not repeating it here") — and RT-4's own audit this
  cycle independently confirmed exp-093's item1/item3 records DO carry
  `dt_ss_full_K_c/g`/`netd_classification_c/g` in their own `per_theta`
  rows. exp-094 imports `cell_metrics_full`/`pair_metrics_full` from that
  same module but never imports or calls `netd_row` (grepped, zero
  matches) — the exact machinery built one cycle ago to prevent this
  outcome sits unused, and the drop recurs.

**Ruling this against RT-4's own letter, not by inertia:** RT-4's mandate
was explicit that the disclaimer must travel "regardless of whether any
NETD field is ever printed" — so this is **not a violation of what RT-4
actually required**, and the disclaimer, though it now covers an empty set
this cycle, is not wrong. But it is a real, independently-confirmed
recurrence of a named pattern this program has already flagged once as
"forward-tripwired for a third occurrence," on my own charter's own output,
one cycle after the fix for it was built and demonstrably worked. Non-
load-bearing (no verdict in this cycle rests on a temperature-rise or NETD
classification value; the flatness question that actually matters is
answered by the `p_abs_w`/`ratio_abs_ext_raw` ratios, which ARE correctly
persisted for Rank 2 and Rank 1b) — but real, and I am naming it explicitly
so a third silent instance is not the first time anyone notices the
pattern again.

## Steel-man (my own discipline)

The energy-channel bookkeeping that *was* done this cycle is genuinely
careful: `p_abs_w`(G)/`p_abs_w`(C) and `ratio_abs_ext_raw` vs. the 0.51 T9
anchor are BOTH reported (module docstring disclosure (iii)), not just one
proxy for the other; the check was correctly added to Rank 1b at zero
marginal FDTD cost per my own Phase-2 critique and Red Team's RT-5
elevation; and the resulting number independently reproduces bit-exact,
extending exp-093's own `cpl≤30` energy-flatness finding to `cpl=40` for
the first time on this channel, exactly as Idealization 23 scopes it. R14's
own mechanistic account (the oscillatory imprint lives in `σ_ext(θ)`
config-differential structure, never the absorption/scattering partition)
now holds at a third independent resolution point at this one location —
a real, incremental strengthening of that account, honestly earned.

## Sharpest attack

The cycle answers "does the energy channel move where the coherent channel
already moved" but not "does the energy channel move where the coherent
channel just discovered it moves *this cycle*" — Rank 3's 38.4° flip is
newer information than anything Rank 1b's design was built to react to,
and the zero-cost check that would test it was simply never wired up,
unlike the identical check for Rank 2's flanking point. Compounding this,
the underlying `dt_ss_full_K`/`netd_classification` sidecar values my own
charter is supposed to own are computed, then thrown away, at every one of
this cycle's 20 article-bearing cells — not a scoring error, but a
completeness regression against machinery built one cycle ago for exactly
this purpose.

## Ranked top candidate next step

1. **(Cheapest, most directly responsive to this cycle's own newest
   finding.)** Add the identical `p_abs_w`-vs-0.51-T9-anchor informational
   check to Rank 3's 38.4° cell (and, for completeness, 36.0°/38.8°) — the
   values are already computed in-memory by `pair_metrics_full` during this
   very run and simply need to be extracted into `rank3_report`; a rerun of
   the same 12 calls reproduces bit-exact per this bench's established
   determinism, so this is a ~12-call, fully-reproducible addition, not new
   physics. This directly answers the review brief's own question at the
   one location it matters most this cycle, before spending anything on a
   `cpl=50` check of the already-well-charted 41.6°–42.0° window.
2. Retrofit `netd_row()` (or an equivalent explicit extraction) into
   Rank 2/Rank 3/Rank 1a/1b's own result-assembly code so the
   `dt_ss_full_K`/`netd_classification` fields the `_full` machinery already
   computes are persisted going forward, closing the tripwired pattern
   named at Iteration 69 before a third occurrence needs a second naming.
3. Only after (1): a `cpl=50`(+) check of `p_abs_w` at the *same* 41.75°–
   41.90° window, to test whether the 0.29%–0.57% monotonic trend found in
   §0 continues, plateaus, or (symmetric to the coherent channel's own
   history) turns out not to be the whole story at a fourth resolution
   point.

## Standing-rule check

No RULED-OUT item (R1–R15) is revisited or contradicted by anything above.
Both findings in §2/§3 are new instances of an already-adopted pattern
(R15's own cross-resolution-instability logic, applied here to the energy
channel by analogy; the Iteration-69 NETD-persistence tripwire) — neither
proposes a new standing rule; both are handed to Red Team's own final audit
to weigh against Checkpoint criterion 4, per this program's convention that
a reviewing seat names, not adjudicates, that question.
