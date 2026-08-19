# PHASE 5 — REVIEW · VISION SCIENCE (blind, fresh context) · exp-045, Panel Iteration 22

**Charge executed:** independently verify — not merely re-read the prose
claim — that Iteration-21's mandatory fix 6 (NETD disclaimer propagated to
every point of claim, not block-scope-only) actually landed in exp-045's
committed `results.json`, `run.py`, and `NOTES.md`; check for any T1/Tier-W
scope creep; render a cycle verdict and ranked Iteration-23 priorities.

---

## 1. `results.json` — direct inspection, not the NOTES.md summary

Loaded `results.json` (2.16MB) and checked programmatically, not by sampling
the first point:

- **Block A, all 2080 sweep points**: every point's `"netd"` field is the
  FULL `netd_disposition()` return dict (`classification`,
  `effective_delta_t_k`, `raw_delta_t_k`, `netd_band_k`, `fill_factor`,
  `emissivity_correction`, `disclaimer`) — **2080/2080 carry a non-empty
  `"disclaimer"` string**, verified by iterating the entire array, not a
  random sample (a 20-point random sample, seed 42, checked first and
  matched before the full pass). Exactly **one** distinct disclaimer text
  across all 2080 — no drift, no truncation, no silently-different wording
  at any point.
- **Block C, all 8 points**: both `netd_first` and `netd_periodic` at every
  one of the 8 `r×gap` combinations carry the full dict including
  `disclaimer` — **16/16 sub-dicts** (8 points × 2 readings each) confirmed.
- Both blocks also carry a block-scope `"netd_disclaimer"` key, plus a
  top-level `"netd_disclaimer_ALL_CLAIMS"` key.

**Verdict on charge (1): genuinely fixed, not merely claimed fixed.** This
is the load-bearing question and it clears cleanly — a real, complete,
byte-verified propagation across all 2096 NETD dispositions this cycle
computed. This is the actual regression I flagged in my own Phase-2 blind
critique this cycle (`phase2_critique_vision.md`, "Sharpest attack") and
Red Team adopted unmodified as mandatory fix 6 — it was delivered in the
artifact that matters most, not just described as delivered.

## 2. `run.py` console prints — every print, not just "one"

Ran `run.py` directly and inspected the full console output (not the
source alone, in case an f-string evaluates differently than it reads).
Six prints touch NETD material:

| Line(s) | Content | Carries disclaimer inline? |
|---|---|---|
| 530 | `NOTE: {NETD_DISCLAIMER}` (Block B section) | Yes |
| 537 | global-max-dT line | Yes |
| 538 | `ALL 2080 points UNDETECTABLE-or-better: True` | **No** |
| 539 | ceiling-bound-holds line | n/a (no classification word) |
| 547–548 | Block-C max-periodic-dT line | Yes |
| 549 | `ALL Block-C points UNDETECTABLE-or-better: True` | **No** |

Two of the six prints that state a classification word ("UNDETECTABLE")
do **not** carry the disclaimer on their own line — but both sit on the
line *immediately following* a print that does carry it (538 follows 537;
549 follows 547–548). Red Team's mandatory fix 6 text, read literally, asks
for "at least one console print adjacent to `all_points_undetectable_or_
better`" — not that every print carry it. Read that way, **fix 6 is
satisfied as worded**. But it is worth naming precisely rather than
rounding up: a reader who captures only line 538 or 549 in isolation (e.g.
grepping `"UNDETECTABLE-or-better"` from a log, a realistic failure mode
given this exact class of gap is how the pattern has recurred before — see
§3) sees a bare classification with no adjacent qualifier in that single
line. Minor, not a mandate violation, but a residual risk worth a one-line
fix (`f"... UNDETECTABLE-or-better: {all_undetectable_or_better} ({NETD_
DISCLAIMER})"`) at essentially zero cost, since the text is already a
module-level constant.

## 3. NOTES.md's own prose — this is where the real gap is

Charge (3) asks specifically whether Results/Learned states an UNDETECTABLE
classification without the disclaimer nearby. Grepped `NOTES.md` for
`disclaimer|human-eye|human perceptual|constraint-3|constraint-4`:

```
54:  NETD disclaimer dropped per-point across all 1664 sweep points (Iteration    <- Phase-2 summary, describing MY OWN Phase-2 finding, not a disclaimer itself
164: human perceptual one — this does not bear on constraint-3/4's human-eye
165: verdict** (standing disclaimer, propagated per-point in `results.json`
```

**The disclaimer sentence appears exactly ONCE in the entire 322-line
NOTES.md file** — inside prediction **P-IT22-A1** in the *Predictions*
section (lines 158–166), committed before the run. It does **not** appear
anywhere in the **Results (Phase 4)** section (lines 208–256) or the
**Learned** section (lines 257–284), even though both sections restate
"UNDETECTABLE" repeatedly and without qualification:

- P-IT22-A1 CONFIRMED: "...all 2080 points UNDETECTABLE-or-better." — no
  disclaimer restated.
- P-IT22-A4 CONFIRMED: "...many orders below NETD." — no disclaimer.
- P-IT22-C CONFIRMED: "...population memory is real but does not threaten
  the UNDETECTABLE verdict." — no disclaimer, and this phrasing in
  particular ("does not threaten the... verdict") reads, out of context, as
  if UNDETECTABLE were a settled perceptual verdict rather than an
  instrument-band classification.
- Learned #1: "...the coupled-ODE ceiling argument... holds across 2080
  points..." — summarizes the whole cycle's headline without the qualifier
  anywhere in the paragraph.

**This is a real, if narrower, recurrence of exactly the failure class I
self-caught at Iteration 20** ("thorough in code/`results.json`, absent
from `NOTES.md`'s own prose and `run.py`'s console prints") and that Red
Team elevated to a mandatory fix at Iteration 21 (fix 6, "stated once in
Idealizations, absent at points of claim"). This cycle's version is milder
than either prior instance — the disclaimer genuinely exists once in
NOTES.md (not zero times, as at Iteration 20), and the underlying data
artifact is 100% compliant (§1) — but the specific section a future reader
or Director is most likely to skim for a quick verdict (Results/Learned)
carries it **zero** times. Someone reading only Phase 4/Learned, which is
the natural thing to do when scanning LOGBOOK.md's eventual summary of this
cycle, would see "UNDETECTABLE" asserted four separate times with no
qualifier in sight.

**A second, sharper finding in the same family, not asked for verbatim by
my charge but directly adjacent to it:** NOTES.md's Phase-3 synthesis
states, unconditionally, **"All eight of Red Team's mandatory fixes are
adopted, none overridden."** Fix 6's own text (`phase2_redteam_audit.md`
§4, item 6) explicitly requires: "...inline the disclaimer sentence at
P-EM45-A1/A2 in `phase1_proposal.md` Section 4, not only in
Idealizations." I grepped `phase1_proposal.md` directly:

```
233: NETD is an instrument/detector threshold, not a human perceptual one
234:   (VISION's standing mandatory disclaimer) — nothing in either block
235:   bears on constraint-3/4's human-eye verdict.
```

Still exactly once, still only in Idealizations (lines 233–235), **not**
inlined at P-EM45-A1/A2 in Section 4 as fix 6 required. NOTES.md's own
Phase-3 text explains this: "`phase1_proposal.md` itself is left unedited
as the historical record of what Phase 1 proposed and Phase 2 critiqued" —
a reasonable house-discipline call (T10's own "flag, don't rewrite"
precedent), but it is **in direct, unstated tension with the same
paragraph's claim that fix 6 was "adopted... none overridden."** PANEL.md
requires the Director to state which criticisms it accepts and which it
overrides, and why, in writing. This specific half of fix 6 (the
phase1_proposal.md edit) was not delivered and not flagged as a
knowingly-scoped-down partial adoption — it was rounded up to "adopted in
full" while the artifact it names was left untouched. This is a smaller
instance of the exact "claimed complete, not fully delivered" pattern Red
Team named as occurring in 5 of 7 recent iterations (LOGBOOK.md, Iteration
21 close) — this makes a sixth/seventh recurrence, at small scale, inside
a cycle whose own Red Team audit explicitly warned the Director to watch
for exactly this ("flagged explicitly so the Director closes this loop the
same shift, not merely in NOTES.md prose," `phase2_redteam_audit.md`
closing note).

**Net assessment of charge (3):** the disclaimer is not *absent* from
NOTES.md's prose (one clean, correctly-worded instance exists, in the right
technical location — a committed prediction), but it is absent from every
place a skimming reader is likeliest to encounter a bare "UNDETECTABLE"
claim (Results, Learned), and the "phase1_proposal.md left unedited"
decision quietly leaves fix 6 only partially delivered while being reported
as fully adopted. Both are cheap, same-shift fixes — one sentence in
Results, one sentence in Learned, and either editing phase1_proposal.md's
Section 4 or explicitly stating the "historical record, not overridden"
scope-narrowing in the fix-adoption line instead of claiming unconditional
adoption.

## 4. Tier-W / glare-adaptation scope check

Grepped every file in this experiment's directory for
`glare|adaptation|weber|ambient.contrast|photopic|scotopic|C_thr|tier-w`.
The only hits are in my own Phase-2 blind critique (`phase2_critique_
vision.md`), correctly noting the cycle does *not* trigger the sidecar, and
one cross-reference in another seat's Phase-5 review filename I did not
read (per the blind-Phase-5 protocol). **exp-045 itself — `phase1_
proposal.md`, `run.py`, `NOTES.md`, `results.json` — contains zero
ambient-contrast, glare, adaptation, or Weber-contrast content of any
kind.** T1 escape route is stated as "NONE" throughout and the mechanism
narrative never touches a σ(I)/σ(x,t)/angular/sub-threshold claim. This
correctly stays entirely outside my own Iteration-23 tripwire lane — there
was no ambient-silhouette scene here to trigger it early, and nothing in
either block could plausibly be misread as touching it. **Confirmed clean.**

Per LOGBOOK.md's Iteration-21 close, my own tripwire is explicitly **"not
yet due"** at Iteration 22 ("Tier 3 (standing, not yet due)") and next
comes due at **Iteration 23** — the cycle immediately following this one.
It is correctly untouched here, and correctly still on the books for next
cycle, not accelerated (matching Red Team's own Iteration-21
REJECT-AS-OVERREACH ruling on acceleration, which still stands — nothing in
this cycle gives new cause to revisit that ruling).

---

## Cycle verdict: **PARTIAL**

The instrument-fidelity substance is sound and my own primary mandate —
did the load-bearing disclaimer-propagation fix actually land in the
machine-checkable artifact — clears with a clean, fully-verified pass
(§1: 2096/2096 NETD dispositions carry the disclaimer, zero exceptions).
The headline physics finding (UNDETECTABLE survives the entire
intermediate-dwell regime, 2080 points, Red Team's Attack 12 ceiling-bound
argument) is not in question from this seat and is not touched by anything
below. What keeps this from a clean PROMISING: (i) the same disclaimer,
thorough in the data layer, is nearly absent from the two sections of
`NOTES.md` a reader actually scans for a verdict (§3); (ii) an
unconditional "all eight fixes adopted, none overridden" claim sits next to
a same-paragraph admission that one fix's own artifact-level requirement
(editing `phase1_proposal.md` Section 4) was not done — a real, if small,
instance of the "claimed complete, not fully delivered" pattern Red Team
has now flagged as recurring across most of this program's recent history.
Neither finding threatens any UNDETECTABLE verdict or reopens any
constraint question; both are same-shift, sentence-level fixes.

## Ranked top-3 candidate directions for Iteration 23

1. **My own glare/adaptation Tier-W sidecar (self-imposed Iteration-21
   tripwire) — now due, should rank highest.** This is the actual missing
   instrument behind T3's still-open finding ("T3's joint constraint-3/4
   verdict still does not exist" — LOGBOOK.md T3, unresolved since
   Iteration 17): compose exp-038's kinetics trajectory n(t), exp-039's
   temporal-CSF timing classification, and exp-040's amplitude bridge
   C(t)-vs-C_thr(L) into ONE scored transient, evaluated specifically at
   the reported witness's own adaptation state (night ambient, observer =
   flashlight holder, self-glare pinned with sources) — Tier-W by
   definition. EM's own Iteration-17 Phase-5 finding already established
   this composition needs zero new engine code; Iteration 18 already named
   it the top candidate route. My tripwire and this composition are the
   same missing piece from two angles (mine supplies the correct
   adaptation-state C_thr(L) branch; the composition supplies the scored
   transient it feeds into) — bundling them is the efficient move, not two
   separate future asks.
2. **QUANTUM's aperture-consistent single-coherent-mode beam check**
   (Checkpoint-4 tripwire, already twice deferred — Iterations 19→20→21,
   and exp-045's own Red Team audit confirms it remains untouched by this
   cycle's Block C). Not my native charge, but the standing rule is
   explicit: a third deferral "fires Checkpoint criterion 4 without further
   debate." Flagging this at rank 2 regardless of seat, because if
   Iteration 23 runs only my sidecar and this lapses a third time, the
   program pays a process cost that was fully foreseeable from this
   cycle's own record.
3. **A closing pass on this cycle's own two prose gaps (§3) plus the
   short-console-print gap (§2)** — cheap, same-shift, and worth doing
   before either of the above so the pattern does not compound into a
   third recurrence next cycle. Lowest-cost item on this list by a wide
   margin (three sentences), included because Red Team's own closing note
   this cycle explicitly asked the Director to close this exact loop
   "the same shift, not merely in NOTES.md prose" — and, per §3, that
   request was only partially honored.
