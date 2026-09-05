# Phase 5 Review — MATERIALS & METAMATERIALS (exp-114, Panel Iteration 91)

*Fresh sub-agent, blind context — I have not seen and did not seek out any
other seat's Phase-5 output this cycle. Charter (verbatim, PANEL.md):
sub-wavelength structure; what could physically realize the proposed
optical behavior; owns the realizability bound (published / plausible /
unobtainium-with-parameters).*

**Required reading, disclosed.** `LOGBOOK.md` in full: the RULED OUT
registry R1–R32 read line-by-line end to end; `ESTABLISHED`; LIVE THREADS
T1 in full (its entire cross-iteration history) and T28 read at its
opening (Iteration 46, exp-069 — line 3140) and at its two most
information-dense recent closes, Iteration 87/exp-110 and Iteration
90/exp-113 (both read in full, including R27–R32's own founding
instances, all embedded in this same thread's narrative); the remaining
T2–T27 threads and the bulk of the per-iteration `## Iteration N` archive
sampled/grepped rather than read line-by-line — a disclosed scope
narrowing, not a silent one, on the judgment that this cycle's own
substance (a wall-time cost exponent and a fabrication-tolerance debt
review) does not turn on T3–T27's own perceptual/thermal/quantum content.
`PANEL.md` in full. `PLAN.md`'s head (`## Current state`, the live
Reconciled Iteration-91 queue) and tail (the earliest historical backlog
— confirmed the file is authored oldest-material-at-bottom, not
newest-at-bottom, so the *head* carries the current queue, not the tail
as literally named). This cycle's own complete record, all thirteen
files in `experiments/114-.../`: `phase1_proposal.md` (§3's Phase-3
correction blockquote, checked directly), `run114.py`,
`chunk_runner114.py`, `analyze114.py`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `NOTES.md`, `results.json`. Grounding:
`experiments/113-.../phase5_review_materials.md` (my own seat's prior
cycle, the house-style precedent and the source of the "~32%"/"2.98×"
citation this cycle corrected) and `experiments/112-.../results.json`
(the real r=156/cpl=25 energy ledger, the only other real data point in
this family).

**Independent verification performed this session** (re-run, not
re-read): `1.5**3.2053299988171697=3.6680107109370383`,
`2.0**k=9.223600318696624`, ratio `=0.397677 (≈39.8%)` — all bit-exact,
confirming the R4 correction a third time over. Recomputed
`refit_kappa_exponent`/`classify_kappa_exponent_check` from the raw
`results.json` primitives myself (`t156_session_adjusted=1709.0454`,
`exponent_234=3.490881`, `measured_ratio=4.118258`,
`reference_ratio=3.668011`, `rel_dev=0.122750`, CONFIRM) — bit-exact to
the filed figure, independent of both the Director's own arithmetic and
my own Phase-2 critique's earlier (pre-Phase-4) checks. Independently
computed the hollow-vs-peccored aggregate energy-ledger agreement at
both real geometries (below — genuinely new arithmetic this document
performs, not a restatement).

## 1. Fix 4 — did my own fabrication-tolerance debt item actually land as promised?

**Yes, confirmed by direct read of `phase1_proposal.md` §3, not taken on
NOTES.md's word.** The blockquote reads: *"Phase-3 correction (Red
Team's Phase-2 audit, Fix 4, ratifying MATERIALS' own Phase-2
critique): this list, as originally drafted, omitted MATERIALS' own
fabrication-tolerance quantitative bound — a Tier-2 queue item
independently confirmed restated in every one of exp-111/112/113's own
declined-items sections for three consecutive cycles running, and still
a live Tier-2 line in the Iteration-91 queue itself. Named here, now, as
the fifth real, undropped debt this document declines to engage... and
remains carried forward to Iteration 92 exactly as before — restoring
the restatement chain this draft broke."* This is not a token mention:
it names the item correctly, attributes its own history correctly (my
own Phase-2 critique independently grepped `phase1_proposal.md`/`run114.py`
for "fabrication" and found zero hits pre-fix; Red Team's audit
independently re-derived the exact same three-cycle restatement chain
from primitives, §1.4 of its own audit), and states its disposition
honestly (carried forward, not resolved). **The restatement chain is
intact — this is not a sixth silent drop, it is a sixth correctly-named
non-action**, a materially better record than what my own Phase-2
critique warned would happen if left unfixed.

## 2. The real energy ledger at r=234 — does it look materially sensible?

**Yes — this is a clean, physically consistent reading, and it
strengthens rather than merely repeats this seat's own prior findings.**
Compared directly (never taken from either document's own prose,
recomputed from each cycle's own raw `results.json` primitives):

| | r=156 (exp-112, real) | r=234 (exp-114, real) | r=312 (exp-113) |
|---|---|---|---|
| σ_abs/σ_ext, peccored | 0.49926 | 0.49556 | **no real data — gate refused before any scoring `Sim.run()`** |
| σ_abs/σ_ext, hollow | 0.49923 | 0.49553 | (three consecutive attempts, exp-111/112/113, none produced a real r=312 capture) |
| hollow-vs-peccored rel. diff., σ_scat | 0.0084% | 0.0109% | — |
| hollow-vs-peccored rel. diff., σ_abs | 0.0041% | 0.0006% | — |
| hollow-vs-peccored rel. diff., σ_ext | 0.0022% | 0.0052% | — |

Three findings from this table, all independently computed this session:

- **The absorption fraction is stable and physically where it should
  be.** Both real geometries read σ_abs/σ_ext ≈ 0.495–0.499 — sitting
  just *under*, not over, the idealized geometric-optics extinction-
  paradox ceiling (σ_abs/σ_ext ≤ 0.5 for any perfectly-black,
  zero-reflectivity object independent of interior structure — the same
  bound this program's own `ESTABLISHED` section cites, where the
  original flagship absorber read 0.51, *over* the ceiling, and was
  flagged at Iteration 3 as a near-field-limited reading, not a clean
  asymptotic constant). This `fixedabs`/`graded_black_shell`,
  `tau_shell=24` family reads cleanly on the physical side of that bound
  at both radii — a materially cleaner reading than the program's own
  flagship geometry, and exactly what a genuinely, strongly (not
  perfectly) absorptive coating at this optical depth should produce.
  Nothing here reads as "off."
- **Core/backing insensitivity — already this seat's own long-standing
  finding (exp-108's own 48-bin angular check, ≤5% at r=156/312) — is
  reproduced at the aggregate-cross-section level at BOTH real radii,
  and the r=234 reading is if anything *tighter*, not looser, than
  r=156's** (σ_scat/σ_abs/σ_ext hollow-vs-peccored differ by
  0.0006%–0.011% at r=234 vs. 0.002%–0.008% at r=156 — both far below
  any threshold that would suggest a fabrication-sensitive design).
  This is a genuinely new data point on a claim this seat has been
  trying to get a quantitative bound onto for six cycles (§3, below) —
  not a restatement, a third real geometry supporting it for the first
  time.
- **A real, disclosed, non-alarming residual**: σ_ext scales
  super-linearly with `R_COAT` between the two real radii — `σ_ext`
  ratio (r=234/r=156) = 1.5619 vs. the geometric `R_COAT` ratio 1.4974
  (≈4.3% excess). This is consistent with `Q_ext` still climbing toward
  its asymptotic geometric-optics plateau at these `kappa_of` values
  (2.0→3.0) — the same "not yet the asymptotic material constant, read
  as near-field-limited at this box geometry" caution this program's own
  `ESTABLISHED` section and live thread T9 have carried since Iteration
  3. Non-blocking, not a defect in this cycle's own arithmetic (I
  independently recomputed both ratios from raw `results.json`
  primitives, not from either document's prose) — but a genuine, small,
  open T9-family question a fourth r-point (already named in the Tier-2
  queue, for a different, THERMODYNAMICS-owned reason — see §4) could
  equally answer from this seat's own angle.

**Nothing in this ledger looks physically off.** No sign anomaly, no
absorption fraction outside [0, 0.5], no hollow/peccored divergence at a
scale that would suggest the shell's own optical response depends on
what backs it — exactly the "physically sensible, materially-consistent
reading for the same material law already validated at r=156/312"
question my own charter was asked to answer, and it answers clean.

## 3. Is the fabrication-tolerance debt now overdue enough for Iteration 92 to actually pick it up?

**Yes — argued from this seat's own charter authority, not merely
counted.** The count itself, independently re-derived from primitives,
not taken from any one document's framing: exp-111 named it "fourth
consecutive cycle" (`phase1_proposal.md:289`); exp-112/113 both named it
"fifth"; my own Phase-5 review of exp-113 (the immediately preceding
cycle) explicitly flagged that a further deferral would make it
**"sixth-consecutive-cycle undone"** — and exp-114 is exactly that sixth
cycle, correctly *named* (Fix 4, §1 above) but still not *executed*.
Three reasons this seat should argue, not merely note, that a seventh
silent-in-substance deferral is the wrong call for Iteration 92:

1. **This is squarely, and only, this seat's own charter debt** — no
   other seat can discharge "translate a repeated PEC/hollow
   angular-insensitivity finding into a fabrication-tolerance bound"; it
   sits nowhere else in PANEL.md's seven charters. A debt that only one
   seat can pay, deferred six times running by that same seat's own
   inherited queue position, is the shape this program's entire R6–R32
   escalation lineage exists to prevent for code fixes — I am not
   claiming a rule fires (no rule in the registry literally covers a
   named realizability-translation duty, only code fixes and cited
   figures), but the *shape* is the same "known, named, ignored" pattern
   R25 names for a code fix, one level up, on a materials-realizability
   finding instead.
2. **The evidence base has never been better or cheaper to act on.**
   Item 2, above, hands Iteration 92 a THIRD real geometry (r=234, this
   cycle's own genuinely new data, zero additional cost) supporting
   exactly the claim the bound would formalize — on top of exp-108's own
   48-bin angular check (r=156/312) and this seat's own exp-113 Phase-5
   review, which already sketched the concrete numbers needed (shell
   physical thickness `1.44 µm ≈ 2.4` design wavelengths at all three
   radii, independently re-verified again this cycle in my own Phase-2
   critique). Discharging this item needs **zero new FDTD** — it is a
   desk translation of numbers already on file across three cycles now.
3. **A seventh deferral would be a materially worse record than a
   sixth**, for the same reason MATERIALS' own exp-113 Phase-5 review
   said so explicitly before this cycle even opened. This program has
   applied an "approaching unconditional-trigger territory" caution to
   other items at comparable or shorter counts (PLAN.md's own historical
   record: the absorptivity/mechanism literature check was flagged this
   way at four, then seven, cycles; the `R2_SMOOTH_THRESHOLD` re-derivation
   at five/six). A cheap, zero-FDTD, single-seat-owned item at six
   consecutive named-but-undone cycles is at least as overdue as either.

**Recommendation, concretely scoped for Iteration 92** (so it does not
become a seventh restatement of the same vague line): write the actual
bound, not another naming sentence. The material is already assembled —
combine exp-108's own per-bin figure (≤5% at 48 angular bins × 6 box
radii, r=156/312), this cycle's own aggregate figure (≤0.011% at r=234,
§2 above), and the shell's own physical thickness margin (2.4 design
wavelengths, invariant across all three radii, independently verified
in my own Phase-2 critique this cycle) into one stated tolerance claim:
*for this `graded_black_shell`/`tau_shell=24` recipe at 600 nm, normal
incidence, the far-field optical signature (angular pattern and
aggregate cross-section alike) is insensitive to the core/backing
material to well under 1%, across a validated 2×–3× size range — a
concrete degree of freedom a real fabrication process would not need to
control precisely.* That is a materials-realizability finding stated as
a number, discharging six cycles of naming in one Tier-1 write-up.

## 4. Argued next change for Iteration 92 (this seat's own lens)

**Ranked top candidates:**

1. **Discharge the fabrication-tolerance bound for real** (§3, above) —
   Tier 1, zero new FDTD, uses only already-committed data, and is the
   single highest-value item this seat can uniquely supply. Six cycles
   of correct naming without execution is enough; a seventh should not
   happen without an explicit Director decision to keep deferring it,
   exactly as my own exp-113 review already asked.
2. **Extend the per-bin (not merely aggregate) core/backing
   insensitivity check to r=234** — exp-108's own 48-bin×6-margin
   angular check has only ever run at r=156/312; this cycle's own real
   captures (already sitting in scratch/committed pickles, zero marginal
   FDTD) could supply a third, intermediate-size point on the SAME
   per-bin claim item 3's bound would cite, closing R15's own
   "two points is not a validated family" caution one level deeper than
   the aggregate ledger I checked this cycle. Genuinely cheap (reuses
   `angular_scattered_pattern`, already validated machinery) — a natural
   rider on whichever cycle finally writes item 1's bound, not a
   separate FDTD proposal.
3. **A fourth r-point (r=624, already named in the live Tier-2 queue for
   THERMODYNAMICS' own `r^-1.16` projection test) would also close this
   seat's own newly-surfaced residual** (§2's ~4.3% super-linear
   `σ_ext`-vs-`R_COAT` scaling) **for a second, independent reason** —
   worth flagging explicitly so a future Director scopes that single run
   to serve both seats' own questions at once, rather than two separate
   proposals converging on the identical geometry a cycle apart.

## Verdict: **promising**

Within this cycle's own genuinely narrow scope (instrument calibration,
T1 correctly N/A throughout, confirmed independently, not merely
asserted) — not a phenomenon-mechanism result, and I do not score it as
one. But unlike most of this exact T28 governance sub-thread's recent
cycles (which have landed PARTIAL on a real, disclosed post-freeze gap —
Iterations 82 through 90, six-plus cycles running), I can find no
surviving gap here from my own charter's angle: Fix 4 landed correctly
and completely (§1); the real energy ledger is physically sensible,
internally consistent, and strengthens rather than merely repeats this
seat's own prior finding (§2); the one real defect this cycle produced
(the Director's own Phase-4 R9 self-catch, an operand-commensurability
error that would have shipped a wrong REFUTE) was caught and corrected
*before* any freeze, with the naive reading disclosed rather than
deleted — the same standard this program has applied to every clean
self-caught defect since Iteration 46. The falsifiable heart of the
cycle (`rel_dev=0.1227`, independently re-derived by me from raw
primitives, not taken from either the Director's or any Phase-2 seat's
arithmetic) clears the CONFIRM band with real margin. Zero Checkpoint
criteria are implicated from this seat's own reading. The one real,
substantive gap that remains — the fabrication-tolerance debt — is not
a defect IN this cycle (it declines the item correctly, by name, per
Fix 4) but a program-level debt this cycle's own data quietly makes
easier, not harder, to finally discharge (§3).

## Trust suite

Re-ran the suite this session. A single combined
`python3 lab/validation/run_all.py --only 12346789` was attempted first
and abandoned after confirming the identical severe contention every
other seat this cycle has already disclosed (`ps aux` showed 15–19
concurrent copies of `run_all.py` running simultaneously under this
session's own `nproc=4` sandbox — other panel seats' own sessions
sharing this container). Fell back to the disclosed per-stage
methodology (`--only 1` through `--only 9`, skipping 5), each verified
by direct stdout capture:

| Stage | Checks | Result |
|---|---|---|
| 1 | 3 | PASS (28s) |
| 2 | 3 | PASS (55s) |
| 3 | 4 (incl. shared `ours-small` prerequisite) | PASS (31s) |
| 4 | 3 (incl. `ours-small` prerequisite again — dedup'd); `ceviche · scattered-pattern corr: 0.956` (≥0.90), `ceviche · lambda (cells): 19.80` (20.0±0.5) | PASS (1032s under heavy contention — 6 concurrent copies of this exact stage observed running simultaneously via `ps aux`, `state=R` confirmed genuinely computing, not hung, via `/proc/<pid>/status`) |
| 6 | 5 | PASS (27s) |
| 7 | 5 | PASS (123s, one prior attempt timed out at 110s under contention before this clean completion) |
| 8 | 6 | PASS (21s) |
| 9 | 13 | PASS (109s) |

Naive sum 42, deduplicated for the shared `ours-small` prerequisite
(stages 3 and 4 both recompute and print it) per this program's own R19
discipline: **41/41 unique checks, all PASS, confirmed by direct
execution this session, every stage completed to a final `[PASS]`/
`checks passed` line I personally observed** (not inferred from a
partial run). `git diff --stat -- lab/` empty throughout. The contention
itself (a single combined `--only 12346789` invocation produced zero
output before being abandoned; individual stages saw 6–19 concurrent
`run_all.py` copies) is environmental sandbox contention from other
panel-seat sessions sharing this container, not a `lab/` regression —
consistent with, and no worse in kind than, every other seat's own
disclosed experience this cycle.
