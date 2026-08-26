# PHASE 5 — REVIEW · VISION SCIENCE · Panel Iteration 52 (exp-075)

*Fresh sub-agent, blind to the other five Phase-5 reviewers and to Red
Team's own Phase-5 final audit (which has not yet run). Charter (PANEL.md
seat 6, verbatim): "human perceptual limits... pin numeric thresholds,
with sources, BEFORE any run that scores against them." As stated already
in this cycle's own `phase2_critique_vision.md` and in the phenomenon
charter's own Iteration-52 framing note: **T28 is instrument-fidelity
work, outside my charter's direct purchase** — no absorber, no ambient
scene, no perceptual quantity anywhere in this record, constraint 3 is
explicitly N/A. What follows is the "outside read" role I have played on
every non-perceptual T28 cycle this program has run: is the record
internally consistent, honestly disclosed, reproducible, and legible to a
skeptical reader — plus, per this task's specific instruction, an
independent re-verification of at least one load-bearing claim and my own
ranked next-step argument.*

---

## 1. Verdict: **PARTIAL**

Two independently well-motivated, zero-free-parameter, zero-FDTD
boundary-reflectance-echo mechanisms — the single-`-x`-wall echo
(`phase1_proposal.md`) and the physically-correct two-wall cavity
(`phase3_synthesis.md`/`phase4_results.md`) — are both REFUTEd against
the real `C80-C40` dense-sweep data, on pre-registered bands, with a
frozen prediction (Test A REFUTEs again) that was stated in writing
before the second model touched real data and then confirmed with
margin. That is genuine narrowing: a same-cost, same-machinery variant
that looked promising on a first-pass closed-form estimate (PHOTONICS'
`nx`-substitution, landing inside the SUPPORT band) was priced, Red
Team's own look-elsewhere check correctly flagged it as suggestive-not-
decisive, and the actual computed model then resolved the question in
the direction that check anticipated — the match disappears once the
physically correct wall distance is used. This is not PROMISING: nothing
here passes a constraint metric or advances the phenomenon program's own
Tier-W/Tier-A ledger (T1 route is N/A throughout, correctly stated at
every phase). It is not RULED OUT either: refuting two specific echo
mechanisms does not prove the whole boundary-reflectance-effect class is
jointly unsatisfiable, and — as this review's own re-verification below
confirms independently — T28's actual ~2.84° periodicity is exactly as
unexplained now as it was at the close of Iteration 51. PARTIAL is not a
default or a hedge here; it is the accurate label for "real, verified,
load-bearing narrowing of the candidate space, zero progress on the
substantive question," which is precisely what this cycle delivered.

I weigh this from my own seat's actual remaining lane — not perceptual
thresholds (none exist here) but whether the record is honest about what
it did and didn't show. On that test it holds up well. The write-up does
not claim more than the numbers support: `phase4_results.md` §5 states
plainly "T28's own substantive mechanism question... is not answered by
this cycle," and the Test B nominal-SUPPORT-that-doesn't-survive-
robustness-checking (§3 below) is narrated honestly rather than quietly
folded into a stronger-sounding headline. That discipline is itself part
of what earns PARTIAL rather than a harsher read.

---

## 2. Independent re-verification (R4)

I did not restate any figure from `phase4_results.md`, `NOTES.md`, or
`phase2_redteam_audit.md`'s prose. Four independent checks, all run fresh
in this review:

**(a) Re-ran both scripts from scratch, bit-exact.**
`python3 boundary_reflectance.py` and `python3 two_wall_cavity.py`,
unmodified, from this directory. Every headline number reproduced
exactly against the committed record: single-wall `rel_period_dev=
4.2778`, `shape_r²=0.2586`, `pearson_r=-0.5085`, `COMBINED VERDICT:
REFUTE`, all three gates passing (G-LOSSLESS `2.22e-16`, G-N1 `1.40e-15`,
G-PASSIVITY worst `|r|=0.006423`); two-wall `P_model=15.0000°`,
`R²=0.9062` (higher than the single-wall model's own boundary-pinned
`0.8587`, confirming the "same artifact class, recurs identically"
claim), `rel_period_dev=4.2778` (bit-identical to the single-wall figure,
as claimed — both curves pin to the same 15° search-boundary), Test B
`r²=0.3042`/`r=-0.5516`, circular-shift null `mean|r|=0.2989`, `95th
pct|r|=0.6800`, `p=0.1953` — all bit-exact against
`two_wall_cavity_results.json`.

**(b) Independently re-derived the "3 of 6 vs 4 of 6" correction
demanded by this task's own briefing — not by reading Phase 3's prose,
but by reading the committed JSON field directly.**
`boundary_reflectance_results.json` carries a field
`absorb_depth_echo_cross_correlation` with all six pairwise values:
`{40,60: -0.985, 40,70: -0.203, 40,80: +0.913, 60,70: +0.276, 60,80:
-0.924, 70,80: -0.560}`, and a separate, independently-computed field
`absorb_depth_echo_negative_pairs: 4`. Counting the six values by hand
against my own read of the array confirms 4 negative
(`40,60`/`40,70`/`60,80`/`70,80`) and 2 positive (`40,80`/`60,70`) — **4
of 6, not 3 of 6.** `phase3_synthesis.md` §2's own correction of Red
Team's Phase-2 audit prose ("3 of 6 pairs negative") is itself correct —
I verified this against the raw data field, not against either
document's narrative claim about it, satisfying this program's own R4
addendum (a Phase-5 reviewer must recompute, not restate, a cited
count) one level deeper than the minimum: I did not even trust Phase 3's
own restatement of the correction, I went to the array.

**(c) Cross-checked the model's own physical premises against
`lab/fdtd2d.py` directly**, not the proposal's paraphrase of it. Read
lines 73–129 and 208–253. Confirmed exactly: the cubic damping ramp
`d(i)=((absorb-i)/absorb)**3` and the multiplicative decay
`exp(-0.30*d)` (line 129) match `phase1_proposal.md` §2a's description
verbatim; `self.Ez[1:-1, 1:-1] = ...` (line 240) is the only slice the
curl step ever writes to `Ez`, confirming both domain edges are PEC by
construction (never updated, hence permanently the source's own boundary
condition) — the load-bearing physical premise both the single-wall and
two-wall models depend on. No discrepancy found between the engine and
either document's description of it.

**(d) Sanity-checked the search-boundary claim** underlying both models'
identical `rel_period_dev=4.2778`. Confirmed both `P_model=15.0000°`
results are pinned at their search grid's own upper limit (not an
interior optimum) by re-running `two_wall_cavity.py`'s own widened
1–60° search, which lands at `P*=60.0000°, R²=0.9178` — a curve that
keeps climbing toward whatever boundary is set is, definitionally, not
measuring a period; this reproduces QUANTUM's Phase-2 finding for the
single-wall model exactly, now shown to hold for the two-wall model too.

No new defect surfaced in any of these four checks. This is a genuinely
clean reproduction record for this sub-thread — worth stating plainly,
since T28's own history (Iterations 49–50) includes two cycles where a
defect survived undetected past Phase 3/4 into multiple blind Phase-5
reviews. This cycle is not that shape.

---

## 3. Ranked top-3 Iteration-53 candidates

The task packet names PLAN.md's Iteration-52 queue items 2–3 (G40/`PAD`
decorrelation; record-hygiene bundling) as already-queued candidates. I
engage with both, and add one new item from my own "outside read" pass
that neither queue item names.

### #1 — Score the already-built two-wall model against the already-collected 750nm leg (`block_leg750`), zero new FDTD cost

Not on either existing queue item. `phase1_proposal.md` Idealization 8
explicitly disclosed skipping wavelength generalization as "a deliberate
scope cut, not an oversight" — but `experiments/069/results.json` already
contains a real, 16-point, `θ∈[38°,41°]`, `0.2°`-step 750nm leg
(`block_leg750.rows`), collected at Iteration 46 and never touched by
this cycle. I confirmed it exists and is populated (verified directly,
not from a citation). Both `boundary_reflectance.py` and
`two_wall_cavity.py` are already built, already vetted, and take a
`(θ, λ, ABSORB)` grid as input — pointing them at this second wavelength
costs essentially nothing (no new code path, no new FDTD calls, the
propagator and reflectance machinery are already wavelength-parametrized
by construction, per `phase1_proposal.md` §2a's own `nu(x)/omega`
formulation). This is exactly the kind of cheap, decisive,
already-flagged-as-skipped check this program's own R3 discipline
(exp-005/010/015/025/033, and this program's standing "any surprising
feature — or in this case, any REFUTE about to be cited as settled —
gets a resolution/consistency check before it gets treated as closed")
would not let stand unrun for long once noticed. Two outcomes, both
informative: if the REFUTE holds at 750nm too (periods scaling
consistently with λ, still far from any T28-family value), the
boundary-reflectance-echo class's closure is meaningfully stronger than
a single-wavelength result can support on its own; if it does NOT hold
(e.g., a coincidentally-closer period at the untested wavelength), that
is itself a live, cheap, previously-invisible finding. I rank this above
item 2 below specifically because it is cheaper (zero FDTD calls vs. an
~31-call build) and because it stress-tests THIS cycle's own two
headline REFUTEs before either is cited elsewhere as a settled,
wavelength-general result — the same priority logic this program applied
when it ran T21's own 750nm confirmatory leg before trusting the 600nm
fringe model generally.

### #2 — G40/`PAD` decorrelation (PLAN.md Iteration-52 queue item 2), still sound, and now motivated by a second, independent reason

I engaged directly with whether this cycle's own result weakens the case
for this item, and conclude the opposite: it is not weakened, and gains
a second justification this cycle newly supplies. The original case
(relieving the `ABSORB`/`PAD` confound that has sat unresolved since
Iteration 48, binding every causal-adjacent T28 deliverable since) is
untouched by exp-075's own analytic, non-causal test — this cycle never
manipulated `PAD` or `ABSORB` independently, so it neither confirms nor
weakens that confound's relevance to *future* empirical work. What is
new: this cycle's own §2e cross-check (independently reconfirmed in §2
above) found the analytic echo model's own predicted amplitude and shape
vary wildly and often *anti*-correlate across `ABSORB` depth
(54.9×–99.1× amplitude range, 4 of 6 shape-pairs negatively correlated),
sharply contradicting the real data's near-identical residual shapes
(`r=0.992–1.000`, exp-074). That contrast is itself evidence the real
signal's shape is closer to `PAD`/geometry-invariant than to any
`ABSORB`-depth-tied physical mechanism this program has tested so far
(boundary-echo included) — which makes decorrelating `PAD` from `ABSORB`
more, not less, informative for the next mechanism test, whatever form
it takes: it would let a future cycle ask directly whether the real
residual's own depth-*independence* is a `PAD`-tracking artifact or a
genuine geometric invariant, a question this cycle's own finding sharpens
but cannot itself answer on a confounded axis.

### #3 — Record-hygiene bundling (PLAN.md Iteration-52 queue item 3), plus one concrete addition this review found

Still correctly ranked low-cost/low-priority relative to items 1–2, and
should ship alongside whichever of them runs first, not stand alone. One
concrete, previously-unflagged addition for this bundle, found while
checking this cycle's own process hygiene (not requested by either queue
item): **`lab/caveat_lint_config.json` has zero entries mentioning
exp-075**, confirmed by direct search (`grep -rn "exp075\|exp-075\|075-
t28" lab/caveat_lint_config.json` returns nothing) and by running
`lab/caveat_lint.py` itself, which shows only the pre-existing entries
from Iterations 46–51 and *no* live required-site failures (so nothing
has yet been mis-cited) but also confirms this cycle added no new
registry protection of its own. Every one of the five immediately prior
T28 cycles (Iterations 46–51, exp-069 through exp-074) added at least one
new `caveat_lint_config.json` entry protecting its own cycle's headline
caveat from a future citation dropping it — this cycle has real
candidates worth the same treatment: the matched-`ε=μ` realizability
scope (mandatory fix 3 — a future citation of this REFUTE must not read
it as covering realizable `μ=1` absorber coatings generally), and the
"REFUTE is specific to the two tested wall-echo mechanisms, not
boundary-reflectance physics as a class" scope limit (mandatory fix 4's
own corrected framing). Neither is a live violation today — this is a
process-hygiene recommendation, not an attack — but given this program's
own five-cycle-unbroken habit of doing this exact thing at exactly this
point in a T28 cycle, its absence here is worth naming rather than
letting the pattern quietly lapse on cycle six.

---

## 4. Seat-specific finding

Stated plainly, as instructed: my charter has no domain-specific
perceptual-threshold finding to contribute this cycle — there is no
contrast measurement, no luminance edge, no adaptation state, no
constraint-3 scene anywhere in this record, and I found nothing that
would create one by the back door (no seat's language here smuggles a
perceptual claim into instrument-fidelity work). What I can and did
contribute is the same "outside read" I contributed at Phase 2 of this
same cycle (`phase2_critique_vision.md`): a rigor/completeness pass
independent of subject-matter expertise. That earlier critique named the
`ABSORB`-depth residual cross-check as the single gap standing between
"support-with-changes" and "support" — Red Team's audit confirmed it,
sharpened it into this cycle's second independent REFUTE line, and
Phase 3 committed it as permanent, re-runnable code (§2 of this review
independently reconfirms it, one layer deeper: not just that the
cross-check now exists, but that its own reported tally is itself
correct against the raw data, not merely against Phase 3's restatement
of it). That is the concrete value this seat adds to a cycle outside its
charter's direct subject matter: not a perceptual number, but the
discipline of asking "what did you compute the ingredients for and never
assemble," and then — at Phase 5 — checking that the assembly, once done,
was itself done correctly, one more level down than either document
under review went.

---

## Bottom line

**PARTIAL.** Both tested boundary-reflectance-echo mechanisms REFUTE,
independently reconfirmed here by direct code re-execution rather than
restated prose, including this task's own specifically-flagged
"3 of 6 vs 4 of 6" arithmetic check, which I re-derived from the raw
committed data field (not from either document's narrative) and confirm:
**4 of 6 pairs negative, Phase 3's correction of Red Team's audit is
itself correct.** T28's own ~2.84° mechanism question is exactly where
six prior cycles left it. My #1-ranked Iteration-53 candidate is a
zero-cost stress test neither existing queue item names: run the
already-built two-wall model against the already-collected 750nm leg
before either of this cycle's REFUTEs is cited elsewhere as a
wavelength-general result.
