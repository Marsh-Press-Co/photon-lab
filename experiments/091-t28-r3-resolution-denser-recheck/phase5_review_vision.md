# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 68 · exp-091

Fresh context, no memory of any prior cycle beyond what is written down.
Read in full: `PANEL.md`; `LOGBOOK.md` in full (RULED OUT R1–R14; LIVE
THREADS T1–T28 through Iteration 67/exp-090, including every prior
disclaimer-erosion Checkpoint-4 instance: Iteration 53/T16, Iteration
63/exp-086, Iteration 64/exp-087, Iteration 65/exp-088 [FIRED], and the
Iteration 66/exp-089 and Iteration 67/exp-090 near-misses ruled
non-firing on reasoned, not reflexive, grounds); the complete exp-091
record — `phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`run_output.txt`, `results.json`; exp-090's own `NOTES.md` and
`phase5_redteam_audit.md` for the precedent wording of the mandatory
NETD/constraint-3-4 disclaimer and the dual-section carried-idealizations
banner. Blind to every other seat's current-cycle output.

## Verdict, up front

**CONCUR-WITH-GAP.** Every scientific number I independently re-checked
reproduces exactly, and the design itself (the R3 leg, the settling
spot-checks, the crossing-bracket leg) is sound, well-targeted, and
correctly scoped as pure instrument recalibration (T1 N/A, Checkpoint
criterion 2 N/A). But this cycle's own disclaimer/scope-note propagation
has a real, newly-discovered gap — on a surface this sub-thread has never
checked before — that I judge at least as serious as the four prior
disclaimer-erosion instances, and I flag it for the Director/Red Team to
weigh explicitly against Checkpoint criterion 4, rather than ruling it
myself either way.

## What I independently verified

I did not trust the brief handed to me. I read `run_output.txt` and
`results.json` directly and re-derived the headline numbers from them.

- **(a) PRIMARY**: `run_output.txt` line 72 reads `VERDICT=REFUTE`. Cause:
  `theta=40.2` sign_match=`False` — cpl=20 (Leg1, fresh `STEPS=4200`)
  gives `delta_scene=-1.542677e-04`, cpl=30 (Leg2) gives
  `delta_scene=+4.369899e-04` — a genuine sign flip, not a magnitude
  miss. 37.2°/41.4° both hold sign (ratios 5.2079/4.1554 — both in the
  disclosed `(3.0,10]` NEITHER band, not CONFIRM, but that is
  independent of the REFUTE verdict, which fires on the sign flip alone
  per the pre-registered priority rule). Matches the brief.
- **(a2)**: both bracket pairs report `crossing_cpl30=None`,
  `VERDICT=REFUTE` — at cpl=30, `delta_scene(40.2°)=+4.37e-4` and
  `delta_scene(40.4°)=+9.86e-4` are **both positive** (no crossing in
  that bracket at all — the true cpl=30 crossing has moved outside the
  window the cpl=20 crossing location predicted), and likewise
  `delta_scene(41.4°)=+5.63e-4`/`delta_scene(41.6°)=+1.78e-4` are both
  positive. This is a stronger, more specific finding than "the
  crossing shifted by more than 0.1°" — it is "the crossing is not
  where either bracket was built to find it." Matches the brief's
  "REFUTE at both brackets."
- **(b) PRIMARY**: 37.2° `cpl30=CONSISTENT` (`ratio_k=1.8463`) vs.
  `cpl20_filed=CONSISTENT` (`3.4433`) — unchanged, confirmed. 40.2°
  `cpl30=ENERGY-DOMINANT` at `ratio_k=10.0744` against
  `RATIO_HIGH=10.0` — I confirm this is razor-thin (0.74% above the
  gate, on a channel whose own R13 floor-gate history (Iteration 66)
  already found a 1.3–1.5× margin "empirically inadequate"). 41.4°
  `cpl30=CONSISTENT` (`ratio_k=9.2116`) against `cpl20_filed=
  ENERGY-DOMINANT` (`28.8072`) — the reclassification is real and
  matches the brief exactly.
- **(c1)/(c2)**: all six + four cells report `VERDICT=CONFIRM`, `rel_dev`
  ≤0.0138% throughout — settling is clean at both resolutions and both
  spot-checked angles. Confirmed.
- **`netd_disclaimer`/`scope_note`**: present in `results.json` (only, see
  below) at the top level:
  `"NETD is an instrument/detector threshold, not a human perceptual
  one -- does NOT bear on constraint-3/4's human-eye verdict.
  (Idealization 3)"` and `"This cycle is pure instrument recalibration
  (T1 route N/A, Checkpoint criterion 2 N/A) -- no phenomenon-mechanism
  claim, REALIZABILITY_MEMO.md untouched. (Idealization 7)"`.

## Wording check against exp-090's precedent

exp-090's own `NOTES.md` carries this program's exact precedent text for
the mandatory dual-section banner, verbatim, at **both** its Predictions
section (line 66) and its Result section (line 264): *"Carried
idealizations banner (mandatory at both this section and the
[Predictions/Result] section, per the Iteration-65 CHECKPOINT's own
escalated[, non-discretionary] rule)... every finding below is governed
by Idealizations 6/7/13 (NETD is not a human-eye threshold; this cycle
does not test constraint 1/2/3/4; `FLOOR`/`RMS` are `graded_black_shell`/
600nm-specific)."* One nuance worth stating precisely, since this
program's own R9 rule exists to police exactly this kind of
comparison-precision: **exp-090 is a zero-FDTD desk cycle and its
`results.json` carries no `netd_disclaimer`/`scope_note` field at
all** — the mandatory-banner precedent lives entirely in its `NOTES.md`
prose, not in JSON. The actual JSON-field precedent (`netd_disclaimer`
as a literal `results.json` key, worded "NETD is an instrument/detector
threshold, not a human perceptual one -- does NOT bear on
constraint-3/4's human-eye verdict") comes from exp-087/088/089, most
recently exp-089's top-level field, worded **identically** to exp-091's
except for the idealization-number citation (9 vs. 3, correctly
updated). So: exp-091's JSON wording is a clean, correct, verbatim
carry-forward of the *right* precedent (exp-089's JSON field), not of
exp-090 (which has no such field to copy). This is a genuinely correct
propagation, and should be credited as such — but it is also the
**only** place either disclaimer appears anywhere in this cycle's
record, which is where the real gap opens (below).

## Sharpest finding — a new propagation surface, worse than any of the four prior instances

**`NOTES.md` has no `## Result` section at all.** I grepped every `## `
heading in the file: `Hypothesis`, `Setup`, `Predictions`,
`Idealizations` — full stop, 221 lines, ending mid-idealization-list.
Every other T28 cycle I checked for comparison (exp-088, exp-089) has a
`## Result` section (and a `## Learned` section) filled in after Phase 4.
This cycle's `run.py`/`run_output.txt`/`results.json` are timestamped
04:30 — after `NOTES.md`'s 03:39 — so Phase 4 genuinely ran, but nobody
wrote its outcome into the document the mandatory dual-section banner
rule is about. **The rule that "a banner scoped to one section does not
propagate to the other" (Iteration 65's own structural remedy) cannot
even be tested here, because the second mandatory section does not
exist to carry it.**

Separately, and independently: **`netd_disclaimer`/`scope_note` are
written into `results.json` (lines 746–751 of `run.py`) but never
`print()`-ed.** I read `run.py` end to end: every single numbered
result — (a), (a2), (b), (b2), (c1), (c2), (d) — has a matching `print()`
call feeding `run_output.txt`. The two disclaimer fields are the *only*
two entries in the entire `out` dict with no corresponding print
statement anywhere in the script. I confirmed this the direct way, not
by inference: `run_output.txt` contains zero occurrences of "NETD",
"Idealization", "human-eye", "constraint-3", "instrument recalibration",
or "REALIZABILITY_MEMO" anywhere in its 125 lines. A reader of the
human-facing, printed record — the file this house convention calls
"the human-readable record" — sees only raw verdicts: `REFUTE`,
`ENERGY-DOMINANT`, `CONSISTENT`, `10.0744`. Nothing in it says this is
an instrument-calibration cycle, nothing says NETD isn't a perceptual
threshold, nothing says constraint 3 isn't being tested.

**This is a genuinely new instance of the exact fact pattern this
program's Checkpoint-4 lineage exists to police — a disclaimer that is
correct and present somewhere in the record, but does not reach where a
human actually reads the finding — surfacing on a surface (`results.json`
vs. printed `stdout`) this sub-thread has never checked propagation
across before.** I considered, and reject, reading this as "milder" by
analogy to this cycle's own Phase-2 catch (the wrong-idealization-number
footnote, correctly ruled a different, milder defect by Red Team's own
Phase-2 audit): that ruling concerned a *citation number* pointing at
the wrong item in an otherwise-present, otherwise-correct banner. Here
there is no banner at all in either of the two places a human reads this
cycle's output (`NOTES.md`'s Result section: absent; `run_output.txt`:
never printed). Judged by the same "shape, not just presence" standard
Red Team applied to this cycle's own Phase-2 finding and to exp-089's
freshly-composed-false-claim near-miss, I read this defect's shape as
matching the *omission* lineage (Iterations 53/63/64/65) more closely
than either of those two milder precedents — arguably a more complete
omission than any of the four, since none of the four had a **totally
absent** Result section; each had a present-but-incomplete one. **I do
not rule Checkpoint criterion 4 myself — that adjudication belongs to
Red Team's final audit — but I recommend it be weighed seriously, on
its own facts, against the unconditional "a fourth instance fires
automatically" standard Iteration 65 set, rather than assumed
non-firing by analogy to this cycle's milder Phase-2 catch.**

## The "exciting result" risk — checked, and inverted from how it was posed

I was asked whether Phase 5's own interest in the dramatic 41.4°
reclassification could cause a *different* scope disclaimer to be
dropped — specifically, overstating an instrument-calibration finding
(Idealization 7) as phenomenon-relevant. **The honest answer is that
this risk has not yet materialized, for the same reason the sharpest
finding above exists: no prose write-up of the result exists anywhere
in this record for the risk to appear in.** `run_output.txt`'s own
printed lines do **not**, on their own, make the constraint-3/T1 scope
boundary clear — I confirm this directly, per the grep above. A future
reader who sees only the printed verdicts (`REFUTE`, the 40.2°/10.0744
razor-margin, the 41.4° flip) with no accompanying scope text is exactly
the reader positioned to overstate this as a phenomenon finding, not
because anything currently says so, but because nothing currently says
otherwise. The risk is prospective, not yet realized: whoever writes
this cycle's still-missing Result section — plausibly under exactly the
excitement this question anticipates, given the 41.4° flip is this
cycle's one genuinely newsworthy number — is the point where the
disclaimer could now fail to propagate a fifth way. I also flag a
second, related, not-yet-occurred confusion risk worth naming before it
happens: 40.2°'s "razor-thin" margin is against `RATIO_HIGH=10.0` (an
R13/R14 instrument-classification gate), a completely different
quantity from the perceptual margin against `C_THR_BASE=0.005` computed
below — the two "close to a threshold" narratives sit adjacent in this
cycle's headline and would be an R9-shape dimensional conflation if a
future write-up ever merged them.

## The perceptual-threshold recheck (VISION's numeric-threshold-pinning duty)

Re-derived, not assumed. `C_THR_BASE=0.005` (`lab/glare_sidecar.py`,
Blackwell 1946/Rose 1948/CIE 19/2/Adrian 1989 — the same source Red
Team's own Phase-2 audit cited at `phase2_redteam_audit.md` §3, using
only the pre-registration's **cpl=20** values, since cpl=30 data did not
exist yet). Using the now-real, measured **cpl=30** `delta_scene`
magnitudes (Leg 2, `run_output.txt` lines 62–64, plus Leg 4's bracket
points):

| θ | leg | `\|delta_scene\|` (cpl=30, measured) | `/C_THR_BASE` | margin below threshold |
|---|---|---|---|---|
| 37.2° | Leg2 | 1.247091×10⁻³ | 24.9% | **≈4.01×** |
| 40.2° | Leg2 | 4.369899×10⁻⁴ | 8.7% | ≈11.4× |
| 41.4° | Leg2 | 5.625525×10⁻⁴ | 11.3% | ≈8.9× |
| 40.4° | Leg4 | 9.856382×10⁻⁴ | 19.7% | ≈5.1× |
| 41.6° | Leg4 | 1.783759×10⁻⁴ | 3.6% | ≈28.0× |

**Confirmed: every actually-measured cpl=30 `delta_scene` value stays
comfortably below `C_THR_BASE=0.005` — the hypothesis in the brief
holds** (40.2°'s own cited 4.370×10⁻⁴ is exactly the value in the second
row above, ≈11.4× below threshold, not a close call at all). The
tightest realized margin is 37.2° at **≈4.0×**, sitting between the two
pre-registered band-edge margins Red Team's Phase-2 audit computed from
cpl=20 data alone (7.0–12.5× at the CONFIRM edge, 2.1–3.7× at the REFUTE
edge) — which is exactly where a real point value should land relative
to two hypothetical band edges, not a discrepancy. **On the specific
question of whether the up-to-5.2× larger cpl=30 `frac_contrast` values
change this comparison: they do not, and correctly so, because
`frac_contrast` is never the compared quantity** — `frac_contrast =
|delta_scene|/|C40_C|` is a dimensionless ratio normalized by the
scene's own ≈0.53–0.56 baseline contrast, and comparing it (or a
multiple of it) directly to `C_THR_BASE` would be the exact R9-shape
unit mismatch this program corrected at Iteration 54. Both the original
Phase-2 computation and my own recheck correctly use `delta_scene`
itself. This channel's own instrument-calibration-only scope
(Idealization 3/7) is not put under any new numeric pressure by this
cycle's results.

## Secondary findings

- **No per-cell `netd_disclaimer` this cycle, unlike its own established
  precedent.** exp-089's `results.json` carries the disclaimer both at
  the top level and repeated at all six per-(config,angle) result cells.
  exp-091 carries it exactly once, at the very end of a 750-line JSON
  file, after ten other top-level keys (`raw`, `a`, `a2`, `b`, `b2`,
  `c1`, `c2`, `d`) — the single least-likely place in the file for a
  future reader to encounter it first. Not blocking on its own (JSON
  readers can search), but it compounds with the print-gap above: there
  is now no location in this cycle's *entire output* where the
  disclaimer sits next to the number it governs.
- **No `floor_rms_specificity_note`-equivalent field**, unlike exp-089's
  own precedent (Idealization 16 there). Idealization 6 here (FLOOR/RMS
  applied unrecomputed against new cpl=30 numbers) is exactly the kind
  of standing, reusable caveat that precedent field exists to carry
  forward mechanically. Minor, non-blocking.
- **The footnote-numbering defect my own seat's Phase-2 critique raised**
  (banner citing "Idealizations 3/7/8" instead of "3/6/7") was correctly
  fixed in `NOTES.md` before freeze — I confirm both occurrences in the
  frozen Predictions section now read "3/6/7"/"3/7" correctly. Red
  Team's Phase-2 ruling that this is a milder, differently-shaped defect
  from the disclaimer-erosion lineage (a miscitation inside an otherwise
  correct and present banner) reads as correct and well-reasoned on my
  own re-read — I do not disturb that ruling; it is a genuinely
  different question from the Result-section/print-gap finding above.

## Ranked top-3 for the Director's Iteration-69 queue

1. **Immediate, same-shift, near-zero cost**: write `NOTES.md`'s missing
   `## Result` section (and a `## Learned` section, house convention),
   carrying the Idealization 3/6/7 banner inline at every item exactly
   as the Predictions section already does — and add one `print()` line
   to `run.py` emitting the `netd_disclaimer`/`scope_note` text into
   `run_output.txt`, so the human-readable record carries what the JSON
   already does. This closes both halves of this review's sharpest
   finding before any future LOGBOOK/PLAN.md citation quotes the 41.4°
   reclassification (this cycle's one genuinely newsworthy number)
   without its instrument-calibration-only scope attached.
2. **Cheap, zero-marginal-FDTD, directly motivated by (a2)'s own
   result**: locate the actual cpl=30 `delta_scene` zero-crossings near
   40.2°/41.4°, since this cycle proved they are not where either
   bracket was built to find them (both bracket pairs came back
   same-signed, not straddling). A short outward extension of the
   existing `DENSE_ANGLES`-aligned bracket (e.g. one step past 40.4° and
   one step below 40.2° on one side, similarly for 41.4°/41.6°) would
   convert this cycle's REFUTE from "the old bracket missed" to "here is
   where the new crossing actually is" — directly relevant to any future
   R13 floor-gate work on this channel at cpl=30.
3. **Structural, program-wide**: extend Red Team's own already-named
   mechanical lint safeguard (per-item idealization-citation parity
   between Predictions and Result sections, queued at Iteration 68's
   board) to also assert, before a cycle reaches Phase 5, that (i) a
   `## Result` section exists in `NOTES.md` at all, and (ii) every
   `results.json` key ending in `_disclaimer`/`_note` has at least one
   corresponding `print()` call in the committed `run.py`. This cycle is
   direct, first-hand proof that the JSON-vs-stdout propagation surface
   needs the same mechanical discipline this sub-thread has already
   built for cross-section prose propagation — a ninth-or-tenth manual
   catch of a shape-adjacent gap is not a substitute for closing the
   surface itself.
