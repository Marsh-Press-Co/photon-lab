# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 53 · exp-076

*Fresh sub-agent, THERMODYNAMICS charter (PANEL.md, verbatim): "where
absorbed energy goes. Always asks what re-radiates and whether it would be
detectable. Owns the per-proposal energy sidecar: absorbed power ->
temperature rise -> emission band -> detectability. Expressibility contract:
the sidecar is a post-run analytic calculation, not an FDTD output, and is
labeled as such." Blind to every other seat's Phase-5 review this cycle and
to Red Team's Phase-5 final audit. Per the task's own instruction: no memory
of this cycle's earlier phases, and the fact that this seat's own Phase-2
critique (docket item 8) is the one that put the N/A sentence into the
record does not exempt it from being re-checked here exactly as skeptically
as any other seat's finding — see §1.**

---

## 0. Verdict

**PARTIAL.**

The cycle did exactly what it set out to do — build `G40`, decorrelate
`PAD` from `ABSORB`, and answer a real, previously-unanswerable, load-
bearing question (which construction axis T28's amplitude-mismatch signal
tracks) — and it answered in the less convenient of the two directions
(`PAD_TIED`, `x=0.119` HIGH vs `y=0.072` MED). That is a genuine narrowing:
five iterations of prior `ABSORB`-series causal framing (48–52) must now be
read with the padding/domain-geometry confound live, not settled. But T28's
own substantive question — the ~2.84° periodicity's origin — is not
answered, the cycle's own 750nm advisory leg shows the *opposite* ordering
from the 600nm headline (a genuinely disclosed, unresolved tension, not
swept aside), and every config this cycle runs at its one decisive
wavelength sits on an exact-integer-λ (aliased) boundary-thickness point
(PHOTONICS' Phase-2 attack, adopted). From my own seat's charter the
cycle is unusually clean process-wise (see §2) — but a clean process
around an instrument-diagnostic result that itself remains wavelength-
unconfirmed is a PARTIAL, not a PROMISING, outcome. Nothing here is RULED
OUT — the instrument itself (G40, the decorrelation machinery, `G0-e`) is
sound and reusable regardless of how the mechanism question eventually
resolves.

---

## 1. Independent re-verification (R4 — recompute, don't restate)

I did not take `phase4_results.md`'s headline table on faith.

- Loaded `results.json` directly: `classification = {x: 0.11936588174716538,
  y: 0.07161594894162475, x_bin: HIGH, y_bin: MED, outcome: PAD_TIED}`,
  `thresh_low = 0.049761897`, `thresh_high = 0.116111093` — matches
  `phase4_results.md`'s printed 0.119366/0.071616/HIGH/MED/PAD_TIED to the
  stated precision, and matches `NOTES.md`'s pre-registered
  `THRESH_LOW≈0.049762`/`THRESH_HIGH≈0.116111` bin edges exactly.
- `settling_gate.forward = {frac_39: 1.03e-4, frac_40: 7.47e-5, passed:
  true}` against `bar_cited = THRESH_LOW` — reproduces the "≈500× inside
  the gate" figure `phase4_results.md` reports (0.0498/0.0001 ≈ 498–664×,
  consistent with "~500×").
- `settling_gate.backward_39.rel_shift = 0.6170` and `backward_40_bonus.
  rel_shift = 0.6404` — reproduces the disclosed 61.7%/64.0% figures
  exactly; both correctly marked `gates: false, disclosed_only: true`, i.e.
  neither backward reading touches the frozen classification.
- `rho_pad_absorb = 0.21078504423289166` — matches the reported 0.2108,
  correctly reported with zero verdict attached (`R_q_disclosure` field
  states plainly: used only in this non-gating diagnostic, no
  null-calibration).
- Cross-checked `total_new_runs=50`, `total_elapsed_s≈1012s` (≈16.9 min)
  against the FROZEN-PREDICTIONS budget table (50 calls, ~15–17 min) —
  consistent.
- `t1_escape_route` field in `results.json` reads verbatim `"N/A
  (instrument/model-fidelity class, phase1_proposal.md Sec3)"` — correctly
  disengaged, matching every T28 instrument cycle since exp-065/exp-069.

No discrepancy found between the committed `results.json`, `phase4_
results.md`'s prose, and `NOTES.md`'s FROZEN PREDICTIONS anywhere I checked.

---

## 2. Sidecar disposition — independently re-confirmed, and re-derived from
first principles, not merely re-read

This cycle's own docket item 8 traces to THERMODYNAMICS' own Phase-2
critique this cycle — a fresh Phase-5 sub-agent, per the task brief, owes
that exact sentence the same skepticism as anything else in the record, not
a pass. I re-checked it three independent ways.

**(i) Text audit, mechanical.** `grep -in "sidecar\|thermo\|energy\|
absorbed\|re-radiat\|watt" run.py results.json` returns exactly one hit —
`run.py`'s own docstring, line 66, restating docket item 8's disposition as
implemented ("textual, carried in NOTES.md's idealizations"). `results.json`
carries **zero** sidecar-adjacent keys — no `absorbed_power`, no `delta_T`,
no `sidecar` field of any kind, in either the success or the (untriggered)
HALT branch. This is the correct signature of a genuine N/A, not a silently
dropped one: the prior five cycles (exp-071–075, independently grepped this
review) all state the disposition as *prose*, in an idealization line, with
no corresponding data field either — N/A means "not computed," and nothing
in this cycle's `results.json` was computed that shouldn't have been.

**(ii) Wording audit against the docket's own literal requirement.**
`phase2_critique_thermodynamics.md`'s mandatory fix asked for: *"the
one-line argument (no article in either `G40`'s or `C80`'s domain; `ABSORB`
is a numerical boundary-condition parameter, not a lossy medium with a
defined loss tangent; no dissipative volume exists to integrate a Poynting
divergence over)."* `NOTES.md` idealization 9 reads: *"`ABSORB`/`PAD` are
numerical damping-mask constructs with no loss tangent or physical
dissipative volume; no absorbed-power/thermal disposition is produced or
applicable, consistent with every T28 instrument cycle since exp-071."*
This is the requested argument, correctly worded — "no loss tangent," "no
… dissipative volume," and the correct backward citation chain
(exp-071→072→073→074(*)→075→076, independently re-verified this review by
`grep -n sidecar` against all five prior `NOTES.md`/`phase1_proposal.md`
files; (*) exp-074's own N/A sentence lives in its `phase1_proposal.md` §9
rather than `NOTES.md`, a filing-location detail that does not weaken the
unbroken-convention claim). `phase3_synthesis.md`'s acceptance table (row
8) and `run.py`'s docstring both point to the same sentence — no drift
between what was promised at Phase 2, what was frozen at Phase 3, and what
shipped.

**(iii) Substance audit — is N/A actually correct here, independent of
whether it was correctly transcribed?** Yes, and more strongly than the
idealization sentence itself states. I pulled the underlying evidence this
cycle's own machinery already produced: `experiments/065-.../
design_geometry_output.txt` line 85 — `static_construction_identity`'s own
printed check, `max over all = 0.000e+00 (scored window is pure vacuum:
True)`. This is not merely "`ABSORB` has no loss tangent in the abstract" —
it is a direct, gate-verified statement that the **object/flank/guard
windows this cycle's own `amp_ratio` statistic is computed over contain no
absorbing material of any kind, in either `C40`'s or `G40`'s construction**
(and, by the congruence table, `C80`'s too). There is no field anywhere in
the scored region for a Poynting divergence to be nonzero at. The N/A
disposition is therefore not merely "the standard T28-instrument-cycle
boilerplate carried forward by convention" (though it is that) — it is
independently derivable, this cycle, from a gate this cycle's own authors
already ran for an unrelated reason (ruling out a coordinate-shift bug,
per PHOTONICS' Phase-2 critique) and never connected to the sidecar
question. Worth naming explicitly in the record as a second, independent
confirmation, not just a restated convention.

**Verdict on this sub-question: the sidecar N/A disposition survived
correctly into the final record — worded as the docket required, filed in
the correct document, consistent with the unbroken exp-071–075 precedent,
and independently over-determined by this cycle's own construction-identity
gate.** No correction needed.

---

## 3. Charter-standpoint analysis — does `PAD_TIED` (vs `ABSORB_TIED`) change
whether a *future* T28 mechanism candidate would ever need an energy story?

This is the substantive question my charter was asked to weigh in on, and
my answer is: **`PAD_TIED` makes an energy/absorption-based mechanism
explanation *less* likely to ever become relevant to T28, not more — for
two separable reasons, one about this cycle's own scope and one about
where the outcome points the mechanism search.**

**(a) Scope reason — this was already true regardless of outcome, and stays
true.** §2(iii) above establishes that neither construction (`C40`, `G40`,
nor, by congruence, `C80`) has any absorbing material inside the scored
measurement windows — the field there is provably vacuum in every
configuration this sub-thread has ever built. `ABSORB` names a graded
*damping-mask* parameter of the domain's outer boundary condition (a
matched-`eps=mu` numerical absorber, the FDTD engine's substitute for a
true PML), not a physical coating in the scene under study — a distinction
MATERIALS' own docket item 7 (adopted verbatim this cycle, and previously
established at exp-075 Phase 5: *"`graded_black_shell`... is a code path
fully disjoint from this cycle's matched-`eps=mu` numerical construct — this
REFUTE says nothing about physically realizable absorber coatings"*)
already puts on the permanent record. Had this cycle come back `ABSORB_
TIED` instead, there would *still* be no dissipative volume in the scored
region to attach a sidecar to — the outcome of the decorrelation was never
going to change *whether* an energy story applies to this instrument's own
diagnostic use of `ABSORB`. Both branches of §4's frozen 9-cell table
carry the identical N/A disposition; that is by design, and it held.

**(b) Mechanism-search reason — this is the part that *does* depend on the
outcome, and cuts further away from thermo, not toward it.** The question
worth asking is not "does this cycle need a sidecar" (no, either way) but
"does the *kind* of future mechanism this outcome now favors ever route
through a dissipative process." Before this cycle, "`ABSORB`-tied" and
"`PAD`-tied" were symmetric unknowns; after it, the evidence (`x=0.119`
HIGH vs `y=0.072` MED, `x` clearing the strong bar on its own) points
toward the signal tracking the *padded-domain/vacuum-clearance*
construction — `clear_plane` (37→77 cells), `clear_src` (20→60 cells), and
`clear_span_y` (0→40 cells), the geometric quantities that differ between
`(C40,G40)` at fixed `ABSORB` — rather than the graded boundary's own
absorption *depth*. A domain-padding/vacuum-clearance effect is native
territory for propagation-distance, diffraction, and reflection-timing
mechanisms (EM's and PHOTONICS' charters — e.g., a residual echo off the
domain's *other* PEC wall, referenced to a `PAD`-dependent round-trip
distance, in the spirit of exp-075's own two-wall cavity model but
re-anchored to `PAD` rather than `ABSORB`) — none of which involve a lossy
medium, a Poynting divergence, or a re-radiation band at any point in the
causal chain. An `ABSORB`-tied outcome, by contrast, would at least have
kept the mechanism search adjacent to a component that *is* graded and
lossy (even though, per (a), not a real material) — the kind of finding
that has, historically in this program, tempted exactly the "absorption
depth" ↔ "absorbed power" analogy MATERIALS' caveat (docket item 7) exists
to head off. **`PAD_TIED` cuts that analogy off at the root**: nobody
reaching for an energy story to explain a signal that tracks vacuum
clearance and domain padding would find a hook to hang it on. In that
specific sense, the less-convenient outcome is thermodynamically the
*safer* one to have gotten — it is harder, not easier, to misread as an
energy finding going forward.

**Bottom line for this sub-question:** an energy-based mechanism
explanation was never live for T28's instrument-diagnostic work, and
`PAD_TIED` — by pointing the search toward pure vacuum-propagation/domain-
geometry territory rather than the (still non-physical, but at least
loss-adjacent) `ABSORB` axis — makes it *more* firmly, not less, the case
that whatever eventually explains the ~2.84° periodicity will be an EM/
propagation mechanism, not a thermal one.

---

## 4. Detectability angle for future work — the one tripwire worth naming
even though this cycle stays correctly N/A

My charter's actual duty ("what re-radiates and whether it would be
detectable") has nothing to attach to in an empty-scene, vacuum-window
FDTD-boundary diagnostic. But T28 is not permanently confined to that
territory — it began (Iterations 46–48) as a question about the real,
physically-motivated graded-loss `ABSORB` band, and exp-075's own two
REFUTEd mechanism candidates were attempts to give that band's own
reflectance a physical (if still numerical-construct) story. **The one
scenario in which my charter re-engages is if a future T28 cycle stops
treating `ABSORB`/`PAD` as pure instrument parameters and instead proposes
translating whatever mechanism eventually explains the periodicity into a
real, witness-relevant absorbing article** — e.g., testing whether a
physical coating built with a similar graded-loss radial profile produces
an analogous angular structure in a genuine object-present constraint-3
ambient-contrast scene (not an empty-scene boundary diagnostic). At that
moment, and not before, there is a real dissipative volume, a real absorbed
-power budget, and a real question of whether any re-radiated signature
would sit inside or outside a microbolometer's NETD band (T5's own already-
built, already trust-suite-gated infrastructure — `lab/thermo_sidecar.py`,
stage 15 — needs no new capability to answer it, only a real object to
point it at).

**Flag for the Director / LOGBOOK.md**: I recommend a one-line standing
note attached to T28 (parallel in spirit to R6/R7/R8's own "when X, then Y
is mandatory" shape, but not proposed as a numbered rule — this is a
scope reminder, not a new discipline failure class): *"T28's energy-sidecar
N/A disposition is correct for every instrument-diagnostic cycle to date
(exp-065, 069, 071–076) because no scored window in any tested
configuration contains a dissipative medium (independently gate-verified,
exp-065's `static_construction_identity`, re-confirmed exp-076 §2); the
disposition must be explicitly re-examined, not carried forward by
default, the first time a T28 cycle proposes scoring a real physical
absorbing article rather than an `ABSORB`/`PAD` boundary-condition
variant."* This costs nothing now and prevents the N/A convention from
calcifying into an unexamined default the one time it would stop being
true.

---

## 5. Top-3 ranked candidate directions for Iteration 54

Ranked from THERMODYNAMICS' own charter standpoint (where it has direct
standing) down to where it is offering a charter-informed opinion on
territory that is properly EM's/PHOTONICS'/VISION's — flagged as such.

1. **Resolve the 600nm/750nm ordering-flip tension with the still-
   outstanding full-width, non-aliased leg — the item this cycle's own
   Idealization 1 and `phase4_results.md`'s Bottom Line already name as
   required before any wavelength-general citation.** Not primarily my
   charter, but I rank it first because it is the cheapest, most
   information-dense open item this specific cycle produced (the 750nm
   *advisory* leg's `x<y` ordering is the *opposite* of the 600nm
   headline's `x>y`, and PHOTONICS' Phase-2 aliasing attack — every config
   this cycle runs sits at an exact-integer-λ boundary thickness at 600nm
   — was adopted as MANDATORY-for-any-future-citation, not resolved) —
   until it lands, `PAD_TIED` itself is a 600nm-only, aliased-condition
   reading, and no downstream mechanism proposal (thermal or otherwise)
   should be built on it as settled.
2. **A `PAD`/domain-geometry-native mechanism candidate, informed directly
   by §3(b)'s reasoning above** — e.g., a two-wall-cavity-style model
   re-anchored to `PAD`-dependent round-trip distances/vacuum clearances
   (`clear_plane`, `clear_src`, `clear_span_y`) rather than to `ABSORB`
   depth, following the same transfer-matrix/pre-registration discipline
   exp-075 already validated for the (now-REFUTEd) `ABSORB`-anchored
   version. This is squarely EM's/PHOTONICS' charter territory, but my own
   §3 analysis is a direct, load-bearing input to scoping it correctly:
   don't re-litigate an `ABSORB`-depth-dependent echo model against this
   cycle's `PAD`-dominant finding — build the `PAD`-native analogue from
   the start.
3. **Item 2 of the still-active Iteration-53 queue (PLAN.md, untouched by
   this cycle): score the already-built two-wall model against the
   already-collected 750nm `block_leg750` data (zero new FDTD).** Cheap,
   decisive, and independent of items 1–2 above — a second, genuinely
   independent stress test of exp-075's own REFUTE at a different
   wavelength, using data this program already owns. From my own charter
   this is orthogonal (no energy content either way) but it remains the
   single cheapest lever left on T28's board and should not be allowed to
   fall further behind the newer G40 thread.

---

## 6. Anything else for the Director's LOGBOOK.md/PLAN.md update

- **Confirm, verbatim-safe for LOGBOOK.md**: "exp-076's THERMODYNAMICS
  energy-sidecar N/A disposition (docket item 8) survived correctly into
  the final record — worded per the docket, filed in `NOTES.md`
  idealization 9, zero sidecar-adjacent keys in `results.json`, and
  independently over-determined by exp-065's own `static_construction_
  identity` gate (`scored window is pure vacuum: True`), not merely by
  citation of the exp-071–075 convention."
- **New, this review**: the `PAD_TIED` outcome does not merely leave the
  sidecar N/A (as it always would have, either way) — it also makes the
  *class* of future mechanism this thread is likely to need (vacuum-
  propagation/domain-geometry, not loss-tangent-adjacent) less likely to
  ever route through an absorbed-power/re-radiation story. Worth one
  sentence in T28's LIVE THREADS entry so a future cycle doesn't have to
  re-derive this scoping call from scratch.
- **Scope tripwire (§4)**: recommend logging the one-sentence standing
  reminder above (re-examine N/A the first time a T28 cycle proposes a
  real physical article, not an `ABSORB`/`PAD` boundary variant) — cheap,
  prevents a future silent default.
- No Checkpoint-criterion concern from this seat. My own docket item
  landed cleanly (§2), and I found no integrity gap in how it was carried
  from Phase 2 through the final `results.json`.
