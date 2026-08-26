# Phase 5 Review — MATERIALS & METAMATERIALS

**Cycle: exp-076 (Panel Iteration 53), G40/`PAD` decorrelation.** Fresh
context, blind to `phase5_review_*.md`/`phase5_redteam_audit.md` per the
Director's brief. `LOGBOOK.md` read in full this seat (RULED OUT R1–R8,
ESTABLISHED, LIVE THREADS T1–T28 in full, T21/T24/T27/T28 read closely,
Iterations 42/46–52's own narrative bodies), `PANEL.md` read in full, and
the complete exp-076 record read directly — `phase1_proposal.md`, all five
Phase-2 critiques, `phase2_redteam_audit.md`, `phase3_synthesis.md`,
`NOTES.md`, `run.py`, `phase4_results.md`, and `results.json` (independently
re-derived, not taken on prose: `headline`, `classification`,
`leg750_scored`, and `settling_gate` fields all cross-checked against
`phase4_results.md`'s printed numbers — bit-identical).

---

## 1. R4 check: is the caveat MATERIALS itself required actually applied correctly in `phase4_results.md`?

Yes, twice, both times word-correct against what was frozen. This cycle's
own Phase-2 finding (`phase2_critique_materials.md`) — that `ABSORB` and
`PAD` are "the same representational class... both pure `Sim(absorb=...)`/
domain-padding numerical constructs," and that §4's original language broke
that symmetry — was adopted verbatim by Red Team (Attack disposition table,
item 7) and carried into `phase3_synthesis.md` §3 as a blockquote attached
to every ABSORB-tied/PAD-tied outcome name. Checking the actual frozen text
against the actual result file, not a summary:

- **Headline result** section: *"Per the frozen PAD-TIED interpretation and
  MATERIALS' caveat (docket item 7, carried verbatim): five iterations of
  T28 causal claims... must be re-read as possibly padding/domain-geometry-
  tied, not physically tied to the graded boundary's absorption depth —
  `ABSORB` and `PAD` are both pure numerical domain-construction parameters;
  neither carries more physical standing than the other."*
- **Bottom line** section: *"...subject to MATERIALS' caveat that neither
  `ABSORB` nor `PAD` carries more physical standing than the other (both are
  pure numerical FDTD domain-construction parameters)..."*

Both instances match the frozen `phase3_synthesis.md` §3 text in substance
and match my own original Phase-2 wording closely enough that no
drift/softening occurred between critique → docket → synthesis → results
prose. I also checked the negative space: `phase4_results.md` never uses
"ABSORB-tied" or "PAD-tied" language *without* the caveat attached somewhere
in the same section (Headline result and Bottom line are the two places the
outcome is stated; both carry it). **R4 discipline satisfied on this specific
point.** This matters beyond process hygiene — it is the one piece of
prose-discipline that keeps this cycle's own headline from silently
re-committing the exact "unlabeled-physicality creep" my charter exists to
catch (the same failure class, one level more subtle, as R8's own
Iteration-52 finding about an unverified robustness argument surviving
unlabeled into a headline).

---

## 2. The substantive question: does PAD-tied make a future physical-mechanism claim on T28 more or less plausible?

**Less plausible — and not marginally. This is close to the cleanest
negative realizability signal this sub-thread could have produced.**

### 2.1 Neither `ABSORB` nor `PAD` is a material parameter — but they are not equally *distant* from one

My own caveat, correctly enforced this cycle, states the flat truth: both
axes are numerical FDTD boundary-condition/domain-construction knobs, and
neither is "more physical" than the other in the sense of being a
material's own dispersive/dissipative response. That symmetry holds exactly
at the level the caveat states it — neither has a defined loss tangent,
neither is measurable in a lab, neither appears in any published coating's
datasheet. But the caveat is deliberately silent on a second, narrower
question this Phase-5 charge specifically asks me to engage: *given that
neither is physical, which one, if either, is even loosely structured like
something a physical boundary could produce, and which one has literally no
witness-scene counterpart at all?*

`ABSORB` parameterizes the **depth of a graded, lossy layer** — a profile
that, however numerically constructed, has the right *shape* to be a stand-in
for something physically motivated (a coating thickness, an AR-taper depth,
the depth over which a real absorber's loss tangent ramps up). That is
precisely why exp-075's own WKB/boundary-reflectance and two-wall-cavity
models were built *against* `ABSORB` specifically — they treat it as a
depth over which a physically-interpretable reflectance `r(θ; ABSORB)`
could, in principle, be derived (both were REFUTEd on period grounds, but
the *attempt* was coherent: a depth-dependent reflectance is a real physical
question to ask of a real coating).

`PAD`, by contrast, parameterizes **how much extra clear vacuum sits between
the boundary band and the scored measurement window**, added purely so
`ABSORB`'s own growth would not eat into fixed clearances (`phase1_proposal.md`
§1: *"padding was added to keep other geometry parameters... congruent as
`ABSORB` grew"*). Concretely, from the geometry table I independently
re-checked against `phase1_proposal.md` §2a: `G40`/`C80` share `NY=1664` vs
`C40`'s `NY=1584` — `ΔNY=80=2×PAD`, symmetric padding added to both domain
edges — and `G40`'s own clearances (`clear_plane` 37→77, `clear_src` 20→60,
both roughly doubling relative to `C40`) show it sits in **more open
vacuum between the leaky `ABSORB=40` boundary and the scored window than
either prior settling anchor ever had** (EM's and VISION's own independently
convergent Phase-2 finding, confirmed by the settling-precondition run in
Phase 4). There is no witness-scene, no coating, no metamaterial unit cell,
no physically-realizable structure whose relevant parameter is "the amount
of empty space placed between the object and the edge of the universe." A
real flashlight beam does not know how far away this program's own
simulation domain wall sits, and no sub-wavelength structure a real
material scientist could fabricate has a free parameter that maps onto it.

### 2.2 What the measured result actually says

`x = amp_ratio(PAIR_PAD) = 0.1194` (**HIGH**, clears the strong 0.7×
reassurance bar on its own) vs `y = amp_ratio(PAIR_ABSORB40) = 0.0716`
(**MED**) — independently re-verified against `results.json::headline` and
`classification`, bit-identical to `phase4_results.md`'s printed table.
`OUTCOME = PAD_TIED`: the dominant confirmed sensitivity axis for T28's
amplitude-mismatch signal, on this cycle's own clean 3-point decorrelation,
is the one axis that has **zero physical-realizability content of any
kind** — not "weak" content, none. This is a stronger finding against
physical-mechanism plausibility than an ABSORB-tied result would have been
*for* it: had `(x,y)` landed in `ABSORB-TIED` instead, my own caveat would
still forbid calling it evidence of realizability (ABSORB is not a material
either), so the *best* available outcome this design could produce was
"narrows toward a numerical axis that is at least depth-shaped, not
evidence of anything physical." The *actual* outcome instead lands on the
one axis that isn't even depth-shaped — it's proximity-to-the-domain-wall.

### 2.3 The 750nm leg does not rescue this, and independently reinforces it

The advisory, narrow-window 750nm leg (`results.json::leg750_scored`,
independently re-verified: `x=0.4199`, `y=0.6161`) **reverses the ordering**
— `x<y` at 750nm vs `x>y` at 600nm (`same_direction_as_600nm_headline:
False`). Per the frozen design this does not overturn the 600nm headline
(narrower window, not decisive) and per PHOTONICS' own Phase-2 aliasing
attack (adopted MANDATORY), it is consistent with every config this cycle
runs at 600nm sitting on an exact-integer-λ resonant condition (`40/20=
2.000λ`, `80/20=4.000λ`) that 750nm's leg avoids (`40/30=1.6λ`,
`80/30≈2.67λ`— non-integer). Read charitably for a physical mechanism, a
real coating's reflectance dispersion is smooth in λ; an ordering that
flips outright between two wavelengths a factor of 1.25× apart is not the
signature of a smoothly-dispersive physical layer — it is more consistent
with two different, wavelength-specific numerical resonance/aliasing
conditions each dominating at their own λ. **Both readings this cycle
produced are, on their own terms, artifact-shaped**, not complementary
partial views of one underlying physical dispersion curve. This does not
prove either reading is entirely artifactual (idealizations 1 and 6 both
concede the design cannot settle this — no R3 check, no full-width 750nm
leg yet), but it removes the one escape route ("PAD dominates at 600nm by
coincidence, but a real depth-dependent physical signal is still there,
just smaller") that a same-direction result at both wavelengths would have
left open.

### 2.4 Bottom line on the charter question

A PAD-tied finding does not merely fail to support a future physical-
mechanism claim on T28 — it actively raises the realizability bar such a
claim would have to clear, because it demonstrates the signal's own
dominant confirmed sensitivity axis is bound to a domain-truncation
placement choice with no physical degree of freedom in any real scene, real
coating, or real sub-wavelength structure. **My verdict on the
realizability question this cycle bears on: UNOBTANIUM-WITH-PARAMETERS is
not even the right frame yet — this result argues T28's ~2.84° periodicity
has not been shown to correspond to anything a physical structure's
parameter space could occupy at all; the evidence so far points toward "an
artifact of how this program's own FDTD domain is truncated and padded,"
not toward a phenomenon whose realizability could be scored published /
plausible / unobtainium.**

---

## 3. Verdict on this cycle (exp-076)

**PARTIAL.**

Not RULED OUT: this cycle did not close T28 as a question, and it did not
show the ~2.84° periodicity itself is an artifact — only that one specific,
previously-confounded causal claim about *which construction axis drives
the amplitude-mismatch signal* now has a clean, independently-verified,
load-bearing answer, and that answer (PAD-tied) narrows the space of
future physical-mechanism explanations rather than eliminating T28 as a
phenomenon worth continued instrument work.

Not PROMISING: nothing in this cycle's result supports a physical
mechanism existing at all — quite the opposite, per §2 above — and the
750nm advisory tension means even the PAD-tied reading itself is not yet
wavelength-general.

This matches the pattern of every other T28 instrument-class cycle since
Iteration 46: a genuine, verified narrowing of the measurement question,
with the substantive mechanism question still open. The instrument
construction itself (geometry congruence, `G0-e` synthetic recovery,
the settling precondition, the exhaustive/mutually-exclusive 9-cell
outcome table) is sound — I found no defect in the Phase-4 execution beyond
the two disclosed, non-physics-touching serialization bugs, both correctly
flagged and both verified bit-identical across crashed and clean runs.

---

## 4. Top-3 ranked candidate directions for Iteration 54 (MATERIALS' seat)

### #1 — A genuine `PAD`-depth causal sweep, holding `ABSORB` fixed (the direct PAD-axis analog of exp-071's ABSORB causal test)

This cycle establishes *that* the signal tracks `PAD`; it does not establish
*how* — a single two-point pair (`C40` vs `G40`, `PAD` 0→40) cannot
distinguish a genuine domain-size-dependent numerical mode (which should
move smoothly/monotonically, and whose apparent period should scale in a
predictable way with the added round-trip path length to the domain wall)
from a coincidence at this one padding value. Build 2–3 new `PAD` values at
fixed `ABSORB=40` (e.g. `PAD∈{20,60,80}`, reusing `design_geometry.py`'s
own construction — `clear_plane`/`clear_src` scale mechanically as they
already do for `G40`) and score `amp_ratio` pairwise, exactly as exp-071
did for the `ABSORB` axis. **This is the single most information-dense next
move for my own charter specifically**: a monotonic, smooth
`amp_ratio(PAD)` trend (mirroring exp-071's own clean `R²=0.998`
saturating-exponential in `ABSORB`) would be strong, independently-checkable
evidence of a genuine domain-size/round-trip numerical mode — closing the
mechanism question in the "artifact, definitively" direction, which is
still real, useful, citable progress (T28 would convert from "unexplained"
to "explained, and explained as a construction artifact," a legitimate
Checkpoint-2-adjacent finding about this measurement channel's own
boundary). A non-monotonic or erratic trend would reopen room for something
else. Either way this needs the R5-addendum-mandated null-permutation
control the moment anyone tries to match the recovered period against a
named length scale (`PAD`, `2×PAD`, `ΔNY`, or any other geometric constant)
— exp-070's own dense-search null already sits on the books precisely to
stop a repeat of that failure mode.

### #2 — Close the 600nm/750nm ordering-flip before any PAD-tied citation is treated as wavelength-general

Already flagged as required by this cycle's own Idealization 1 and Red
Team's Attack 4 disposition (a full-width, 6°/31-point, non-aliased leg —
750nm is the natural first candidate since it is already partially built
via `block_leg750`, but a genuinely non-integer-λ config at 600nm itself,
if one can be constructed without breaking geometric congruence, would be
even cleaner). I am elevating this from "statistics hygiene" to a
MATERIALS-charter priority: §2.3 above shows the ordering flip is not a
cosmetic loose end — a signal whose dominant term switches identity between
two wavelengths a factor of 1.25× apart is inconsistent with any smooth
physical dispersion, and resolving whether that flip survives a genuinely
un-aliased, full-power window is a precondition for saying anything at all
about whether *either* reading (PAD- or ABSORB-tied) reflects real
wave physics versus per-λ resonant/aliasing bookkeeping.

### #3 — A structurally independent absorbing-boundary implementation (the parked "true PML") as a cross-technology check

Higher cost, longer horizon, but the most decisive test available for the
question this Phase-5 charge actually asks: is the ~2.84°-family
periodicity, or its newly-demonstrated `PAD` sensitivity, a property of
*this specific* graded-damping-mask boundary construction, or would it
recur under a completely different absorbing-boundary algorithm? "True
PML" has sat in this program's own PARKED list (`LOGBOOK.md`, "Original
parking lot") since before the panel existed, never built. Standing up a
minimal PML implementation and re-running a matched-geometry `PAD`-like
sensitivity check against it would be the closest this program can get to
asking the real-world question directly: does a physical, non-numerical
truncation (i.e., no truncation at all — an infinite or sufficiently large
real domain) still show this sensitivity, or does it vanish with the
specific boundary algorithm that produced it? I flag this as #3, not #1,
because it is a genuine engine-physics build (PANEL.md Checkpoint criterion
3 territory — "a synthesis requires engine physics beyond the validated
bench classes") and should not preempt the two cheaper, faster-turnaround
items above; but it is the test that would most directly and permanently
answer the realizability question my seat owns, and it should not sit
parked indefinitely once #1 and #2 are in hand.

---

## 5. Flags for the Director's LOGBOOK.md / PLAN.md update

1. **T28's entry should record, explicitly, that PAD-tied is evidence
   AGAINST future physical-mechanism plausibility, not merely a neutral
   "confound not relieved" finding.** The existing `phase4_results.md`
   Bottom Line language ("the opposite of... 'confound relieved'... hoped
   for") is accurate but framed procedurally; LOGBOOK.md's own T28 entry
   should carry the sharper, charter-level reading from §2 above — `PAD`
   has no witness-scene or realizable-structure analog at all, which is a
   stronger and different claim than "still confounded."
2. **The 600nm/750nm ordering-flip (§2.3) deserves its own explicit
   sentence in LOGBOOK.md's T28 update**, not just a citation restriction —
   it is itself a finding (two artifact-shaped readings, not one physical
   dispersion curve), and future cycles reading only the "PAD_TIED,
   advisory leg non-decisive" summary could miss that the two legs actively
   disagree on which axis dominates, not merely that one leg is under-powered.
3. **No Checkpoint criterion fires from my seat's review.** Criterion 4
   (program-integrity drift) does not apply — this cycle's own Phase-2
   process caught and fixed the two defects (Attacks 1/2) that could have
   triggered it, exactly per this program's own established non-firing
   precedent, and I found no new instance of overclaiming in the Phase-4
   prose (§1, above). Criterion 2 (proven mechanism-class boundary) does
   not fire either — this narrows a measurement-instrument question, not a
   T1 mechanism class; constraint 3 was never engaged this cycle (correctly
   disclaimed throughout).
4. **PLAN.md's Iteration-54 queue** should carry my #1 (PAD causal sweep)
   as a near-top item given it directly extends the exact machinery and
   convention this cycle already built and validated (`G0-e` PASS,
   settling-precondition PASS, congruence-table machinery) — genuinely
   cheap, and the single test most likely to convert T28 from "unexplained
   periodicity" to a scored, citable verdict on whether it is a domain-
   construction artifact, from either direction.
