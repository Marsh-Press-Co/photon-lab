# Photon Lab — Session Log

Newest on top. Current state lives in the vault hub; this is history.

## 2026-08-17 (panel shift) — Iteration 15 close-out (exp-038): the T17
rate-equation kernel bench-confirms the n_ss formula to machine precision
for the first time and catches two real implementation bugs pre-trust; a
Phase 5 that had been left un-run by the prior shift closes it out with a
four-item same-shift fix docket, including a third-consecutive-committed-
iteration recurrence of VISION SCIENCE's T3-provisional-tag gap (Checkpoint
criterion 4 exercised, not fired, with a standing instruction that a fourth
recurrence fires it without debate).

**Pre-flight:** fresh container, deps installed per the recorded wrinkle.
Found Iteration 15 (exp-038) partially complete on arrival: the prior
shift had committed predictions (`a7c05f3`) and results (`98daa63`) —
Phases 1-4 — but stopped before Phase 5 and before any LOGBOOK.md/PLAN.md/
SESSION_LOG.md update, despite the results commit message stating "see
LOGBOOK.md for the complete Phase 1-4 transcript." Bench trust suite
reconfirmed green before continuing: `--only 12346789` 41/41, `--only 12`
(stage 12 alone) 5/5 — both matching the committed record's own numbers to
the printed digit.

**Iteration 15 — The T17 Rate-Equation Kernel (exp-038, CONCLUDED this
shift).** Lead: MATERIALS (rotation), executing Iteration 14's near-
unanimous priority #3 (the in-engine rate-equation kernel; priorities #1/#2
had no executable route — WebFetch egress-blocked a fourth consecutive
shift, T18). New machinery: `lab/kinetics.py` (0D two-state kinetics
integrator, exact-exponential + RK4 propagators) + trust-suite stage 12
(5/5 gates, tightest 2.94×10⁻¹⁶). Two genuine implementation bugs (RK4
double-division; a stiff-segment cost/stability blowup) were caught by the
gate itself failing on first run, fixed before any science result was
trusted. Science: P-MAT-4 CONFIRMED, P-MAT-5a CONFIRMED, P-MAT-5b
PARTIALLY CONFIRMED (the co-location claim — at-rest sweep-to-sweep memory
risk coincides with the least-realizable host tier — held exactly; the
predicted magnitude band did not).

**Phase 5 (six fresh blind discipline seats, then Red Team audit, run this
shift): all six independently re-derived every headline number from raw
code/data — zero science-numeric defect found anywhere.** Four same-shift
fixes applied, none changing any reported verdict: (1) a dead-code bug in
`run.py`'s P-MAT-5b confirmation check (`or True` making a bound
unreachable) — independently caught by both QUANTUM OPTICS and MATERIALS,
a genuine converging finding; (2) the mandatory "T3-provisional" tag,
present at every point of claim in the Phase-3 predictions section, was
absent at all four points of claim in the Phase-4 results section — caught
by VISION SCIENCE, Red-Team-confirmed as the third consecutive committed
iteration (13, 14, 15) this exact species of defect has required a Phase-5
catch-and-correct, with the program's own "consecutive-cycle" bookkeeping
found internally inconsistent and reconciled in the LOGBOOK entry; (3) the
Phase-3 THERMO-sidecar N/A ruling rested on a category error — exp-037's
borrowed ΔT_ss figure never used n_ss, so a zero-cost ceiling bound was
available and wrongly declined, caught by THERMODYNAMICS; (4) the P-MAT-5b
"co-location" finding's framing overclaimed independence — Red Team
derived it follows substantially from this cycle's own fixed pulse-
duration parameter, caught by MATERIALS, who also found
`REALIZABILITY_MEMO.md` had gone unupdated since Iteration 14 (Amendment 3
added, a separate tempered axis, does not revise the existing UNOBTANIUM
verdict).

**Checkpoint ruling, explicit: criterion 4 exercised, not fired** — the
T3-provisional-tag defect was caught by the review layer built to catch
it, no reported verdict changed, and precedent (Iterations 13, 14) ruled
comparable same-shift-corrected issues the same way; but a **standing
instruction is now on the record**: any further recurrence of this exact
pattern fires criterion 4 without further debate. No other criterion
fires. **Verdict: PARTIAL.** Next lead per rotation: ELECTROMAGNETISM
(Iteration 16), whose own top-ranked priority (building an n(t)→ε(ω,t)
causality/passivity-checked material-law bridge) responds directly to its
own Phase-5 self-critique that zero EM bookkeeping happened this cycle.
Full record: LOGBOOK.md Iteration 15.

## 2026-08-16 (panel shift) — Iteration 14 complete (exp-037): the
free-carrier-absorption/combined-saturable-RSA-media literature check
closes the two mechanism classes LOGBOOK's own Iteration-13 record named
as the program's last explicitly-tracked untested scope — all four rows
(TPA-cascade FCA, linearly-pumped FCA, ENZ, combined media) fail, ENZ via
a genuinely new-to-this-line but not new-to-the-program disqualification
(a new instance of R1's already-ruled-out refractive-cloaking principle,
corrected same-shift after the cycle's own first draft overclaimed it as
unprecedented). Checkpoint criterion 2 still does not fire (evidentiary
tier). Seven-seat Phase 5 caught three independently-converging finding
pairs across blind seats plus a genuine unmet THERMO deliverable
(self-caught) — a 17-item same-shift fix docket applied in full, and
`REALIZABILITY_MEMO.md` (a three-cycle-deferred MATERIALS obligation)
finally rewritten with a consolidated nine-class table. New live thread
T18 (the field-enhancement/evidentiary-tier ceiling on this whole
literature-check line).

**Pre-flight:** fresh container, deps installed per the recorded wrinkle
(numpy/scipy/matplotlib/pillow/autograd/fdtd via pip, then
`ceviche --no-deps`). Bench trust suite 41/41 green (`--only
12346789`) before this shift's work (no `lab/` engine changes this
cycle — nothing to re-verify after).

**Iteration 14 — The Free-Carrier-Absorption / Combined Saturable-RSA
Media Literature Check (exp-037, CONCLUDED).** Lead: PHOTONICS (rotation),
executing Iteration 13's near-unanimous top priority (MATERIALS,
ELECTROMAGNETISM, QUANTUM OPTICS). Full seven-seat cycle: Phase 1
proposal (PHOTONICS) → 5 blind parallel critiques (all support-with-
changes, five non-overlapping fixes, the sharpest being ELECTROMAGNETISM's
catch that the proposal's own "FOURTH kinetics sub-case" framing for
linearly-pumped FCA was an overclaim — T17's existing n_ss formula was
never restricted to threshold-gated generation) → Red Team last
(proceed-with-mandatory-fixes, 8 attacks, all adopted) → Phase 3 synthesis
→ predictions committed (`ee58034`) → Phase 4 search (three parallel
WebSearch legs plus two analytic derivations and one capped THERMO
estimate, `fd1bd74`).

**Result: TPA-cascade FCA derived analytically as unobtainium (bounded by
TPA's own established irradiance gap). Linearly-pumped FCA falls 1–9
orders of magnitude short on dynamic range** — the first quantitative
cross-section this program has obtained for this row-type (Soref &
Bennett 1987), with a genuinely open, T17-formula-scored at-rest question
(n_ss≈10⁻⁹ to ~10⁻¹ depending on doping) held throughout to VISION's
mandatory perceptual-scoring cap. **ENZ fails on wavelength (near-IR,
outside the 450/600/750nm sweep) and on mechanism class** — its headline
"unity-order" nonlinearity is dominantly refractive (Alam et al., *Science*
2016), not absorptive, so it does not reduce to a σ(I) row at all;
originally mischaracterized in the committed results as "a genuinely new
failure mode... never previously seen," corrected same-shift at Phase 5
(independently caught by ELECTROMAGNETISM and QUANTUM OPTICS) to what it
actually is — a new INSTANCE of R1's already-ruled-out refractive-cloaking
principle, now cross-referenced directly in R1's own LOGBOOK entry.
**Combined saturable/RSA media fails on dynamic range** (corrected to
~0.65–2.1 orders short, not the originally-published "2–4+" — an
arithmetic error PHOTONICS caught in its own Phase-5 self-audit) **with a
"motivation mismatch"**: the real published architectures are designed for
pulsed-laser-damage protection, not CW ambient-silhouette suppression — no
CW dynamic-range figure exists anywhere in the literature this cycle
found. Graphene control case confirmed wrong-direction. Leg A self-caught
and corrected, mid-search, a real error in the cycle's own pre-
registration (the fast/slow-host doping direction for FCA switching speed
was backward per Shockley-Read-Hall physics) — without waiting for a
Phase-5 catch.

**Phase 5 (six fresh discipline seats plus a second independent PHOTONICS
pass, since PHOTONICS led this cycle, then Red Team audit): verdict
PARTIAL.** Three finding-pairs converged unprompted across independently-
blind seats — a rare, load-bearing signal this program treats seriously:
(1) PHOTONICS (both passes) and MATERIALS independently caught the same
wavelength-tagging failure (TPA-cascade FCA's named hosts are above-
bandgap, not TPA-relevant, at every sweep wavelength; the Soref & Bennett
cross-sections were applied unscaled from their telecom-wavelength
source) — the cycle's own committed discipline going unexecuted a second
consecutive cycle; (2) ELECTROMAGNETISM and QUANTUM OPTICS independently
attacked both the ENZ-overclaim (above) and a "categorical" CW-vs-pulsed
source-mismatch argument that Red Team's own re-verification found was not
merely overstated but directly self-contradicted by another section of
the same document; (3) MATERIALS and PHOTONICS independently converged on
the same underlying process gap — `REALIZABILITY_MEMO.md` (MATERIALS'
own canonical deliverable) had gone three consecutive cycles unupdated
despite being named at each cycle's close, and the committed results'
"all six named classes checked" claim didn't match the memo's own actual
count (five, not six) when read directly. **THERMODYNAMICS self-audited
its own capped estimate and found it was not actually a computation** —
a qualitative VO2 analogy containing an internal numeric inconsistency and
a category error (comparing a time-to-threshold to a steady-state
temperature) — Red Team ruled this a genuine unmet Phase-3 deliverable,
not a queueable gap, and it was replaced same-shift with an actual
numeric estimate (ΔT_ss≈7mK at ambient, ~3–7× below current microbolometer
NETD) using silicon's own standard thermal constants at zero marginal
cost. Red Team's audit independently re-derived and confirmed every
convergent finding against the primary text directly (recomputing
bandgap-vs-wavelength arithmetic, re-reading R1 and the realizability
memo, re-checking the "2–4+ orders" claim) rather than trusting seat
characterizations, and issued a 17-item same-shift mandatory-fix docket,
all applied.

**Checkpoint ruling, explicit: criterion 2 does NOT fire.** The
evidentiary-tier gap (39/39 WebFetch attempts EGRESS_BLOCKED across all
three search legs, independently re-confirmed not inherited) is decisive
on its own, surviving the same-shift correction of the cycle's own "all
six classes checked" overclaim — the accurate, narrower claim is that this
cycle closes the two classes LOGBOOK's own Iteration-13 record explicitly
named as remaining untested (free-carrier absorption, combined saturable/
RSA media), not a program-wide class census. **Criterion 4 exercised, not
fired**: two Learned-section overclaims (the "six classes" claim; ENZ's
"genuinely new failure mode" claim) are the same self-correcting species
as Iteration 13's spiropyran correction — caught and corrected same-shift,
not requiring a program pause. **New live thread T18**: the field-
enhancement/evidentiary-tier ceiling on this program's entire realizability-
check methodology — three consecutive literature-check cycles have now
hit total WebFetch blockage, and MATERIALS' own zero-cost field-
enhancement arithmetic shows no future cycle can, on its own, escalate to
Checkpoint criterion 2 without either a working primary-source access
route or a mechanism class whose own gap is small enough (≲5–6 orders of
magnitude) for realistic field enhancement to genuinely close it — a bar
every class checked to date has failed to clear. No other Checkpoint
criterion fires. Full record: LOGBOOK.md Iteration 14. Next lead per
rotation: MATERIALS (Iteration 15).

## 2026-08-16 (panel shift) — Iteration 13 complete (exp-036): the first
literature-only cycle (zero FDTD calls) rigorously checks RSA, TPA, and
photochromic/photothermal (VO2) switching against this program's own
realizability bounds — all four fail via distinct, now-citation-sharpened
gaps, but Checkpoint criterion 2 still does not fire (free-carrier
absorption and combined saturable/RSA media remain untested, and the
evidentiary tier is WebSearch-snippet synthesis, not primary-source-
verified). A new live thread (T17) formalizes a genuinely novel
constraint-3-at-rest risk class for hysteretic σ(I) mechanisms; its
structural half is secure, its empirical headline number was caught
overclaiming by two independently-converging blind Phase-5 seats and
corrected same-shift.

**Pre-flight:** fresh container, deps installed per the recorded wrinkle.
Bench trust suite 41/41 green (`--only 12346789`) before this shift's work
(no `lab/` engine changes this cycle — nothing to re-verify after).

**Iteration 13 — The Rigorous RSA/TPA/Photochromic-Photothermal Literature
Check (exp-036, CONCLUDED).** Lead: VISION SCIENCE (rotation), executing
Red Team's Iteration-12 top-ranked priority — the first cycle in this
program's history whose entire "run" is a WebSearch-grounded literature
search, not an FDTD simulation. Full seven-seat cycle: Phase 1 proposal
(VISION SCIENCE) → 5 blind parallel critiques (all support-with-changes,
no verdict conflict, five non-overlapping fixes) → Red Team last
(proceed-with-mandatory-fixes, 7 attacks, all accepted — the sharpest:
ELECTROMAGNETISM's catch that photochromic/photothermal switching is a
hysteretic σ(I)-with-memory mechanism, not σ(x,t) as originally framed,
exposing a genuinely new constraint-3-at-rest risk) → Phase 3 synthesis
→ predictions committed (`58f9c87`) → Phase 4 search.

**Result: four parallel WebSearch-grounded search legs, one per mechanism-
class row (RSA, TPA, photochromic, photothermal/VO2 — split per
THERMODYNAMICS' mandatory fix).** All four pre-registered program-level
predictions CONFIRMED — no class clears dynamic range + irradiance +
switching speed simultaneously, and each fails via a distinct,
now-literature-grounded gap: **RSA** short ~22–30× on dynamic range even
at the best published figure (~40×, a single-outlier porphyrin) once the
absorption-only correction is applied; **TPA** short ~9–11 orders of
magnitude on irradiance, sharpened with real citations (Sheik-Bahae/Van
Stryland's foundational semiconductor-TPA database, He et al. *Opt. Lett.*
1995's visible-wavelength demonstration, ZnSe/GaAs Z-scan studies);
**photochromic** fails on reverse-switching speed for durable systems
(spiropyran thermal half-lives seconds-to-permanent; P-type diarylethene/
fulgide structurally lack any passive reverse path); **photothermal/VO2**
fails on bulk thermal power-budget — THERMODYNAMICS' capped analytic
estimate (worked arithmetic, cited thermal properties, this program's own
T5 power budget) found no length scale from µm to m clears both heating
and passive-reset within the proposal's 10ms–1s window, sharper than
predicted (heating alone is fatal at every scale tested, not just cm–m).
Honest methodology disclosure, not smoothed over: WebFetch was blocked by
the sandbox's egress proxy for essentially every scholarly domain across
three of four legs — every finding rests on WebSearch snippet synthesis,
not independently-read primary-source tables.

**Phase 5 (six fresh blind seats + Red Team audit): unanimous PARTIAL.**
Two pairs of findings converged unprompted across independently-blind
seats — a rare, load-bearing signal. **PHOTONICS and VISION SCIENCE
independently attacked the same flagship finding** (spiropyran's 60–80%
at-rest coloration) from different angles: PHOTONICS found it was
measured in sun-comparable/photopic ambient, not the dim/night regime the
witness scenario actually specifies (nobody notices a flashlight sweep in
daylight); VISION SCIENCE found a chemical population fraction was never
converted through ε/path-length/geometry into a scored perceptual quantity
against a sourced threshold. Red Team's audit accepted both, ruled the
committed "strongly confirmed, sharpest finding" language a genuine
Checkpoint-criterion-4 overclaim risk, and corrected it same-shift — real
chemistry, visual significance unverified, not yet a scored constraint-3
violation. **What survives intact and is arguably more secure**:
ELECTROMAGNETISM's structural, class-level derivation (independently
re-derived and confirmed by Red Team) that any hysteretic-σ(I) mechanism
with slow reverse rate has a strictly positive steady-state colored
population under unbounded ambient dwell time — logged as new live thread
**T17**. **MATERIALS, ELECTROMAGNETISM, and QUANTUM OPTICS independently
ranked closing free-carrier absorption + combined saturable/RSA media as
Iteration 14's top priority** — near-unanimous. PHOTONICS also caught its
own Phase-2 wavelength-tagging mandatory fix went unexecuted in the
Results (confirmed directly by Red Team against the text) — queued, not
verdict-changing. THERMODYNAMICS independently re-derived its own VO2
estimate and found it more robust than stated; QUANTUM found its own
absorption-only correction was correctly withheld for TPA but is missing
(non-load-bearing) for VO2's different (Drude/plasma) physics.

**Red Team's Checkpoint ruling, explicit: criterion 2 does NOT fire**, for
two independent reasons — the pre-disclosed free-carrier-absorption/
combined-media gap, and (Red Team's own addition) the WebFetch-blockage
evidentiary-tier gap, since even the four covered classes rest on snippet
synthesis rather than primary-source-verified figures. **Criterion 4
fires in narrow, self-correcting form**: not a constraint-3-quietly-
dropped case (the opposite — EM's catch actively surfaced a genuinely new
risk, correctly), but the overclaimed spiropyran language required a
same-shift correction, completed before this iteration closed, per Red
Team's own mandatory-fix docket (4 items, all applied: language walked
back; wavelength-tagging miss noted; the second Checkpoint-2 non-firing
reason added; T17 logged into LOGBOOK.md's LIVE THREADS). No other
Checkpoint criterion fires. Full record: LOGBOOK.md Iteration 13. Next
lead per rotation: PHOTONICS (Iteration 14).

## 2026-08-16 (panel shift) — Iteration 12 complete (exp-035): the program's
only-ever constraint-3 σ(I) OFF-state PASS no longer survives corrected
angular-quadrature instrumentation at either geometry ever tested — a real
domain×quadrature interaction found at r=156 (not the additive model
assumed), and a clean, domain-confound-free PASS→MARGINAL downgrade shown
for the first time at r=78-native, the geometry the headline citation
actually uses. Unanimous 6-for-6 blind-seat PARTIAL, Red Team affirms; a
real historical numeric bug (THERMO's detectability-note range) caught and
fixed in live code same-shift; Checkpoint criterion 2 explicitly ruled
non-firing

**Pre-flight:** fresh container, deps installed per the recorded wrinkle
(numpy/scipy/matplotlib/pillow/autograd/fdtd via pip, then
`ceviche --no-deps`). Bench trust suite 46/46 green (`--only
12346789,10,11`) before and after this shift's work, re-verified
independently at Phase 4 and again by Red Team at Phase 5 close.

**Iteration 12 — Closing the R156/N17_156 Domain × Quadrature Factorial,
Rebuilding N17_NATIVE, and Reconciling T15 (exp-035, CONCLUDED).** Lead:
QUANTUM OPTICS (rotation), executing Iteration 11's own Red-Team-ranked
priorities. Full seven-seat cycle: Phase 1 proposal (QUANTUM OPTICS, three
blocks: T16_CLOSE, N17_NATIVE_V2, T15_RECONCILE) → 5 blind parallel
critiques (all support-with-changes; PHOTONICS caught the cycle's single
most consequential defect — a fabricated cpl=40 comparator in the T15
table) → Red Team last (PROCEED-WITH-MANDATORY-FIXES, independently
confirmed PHOTONICS' catch and supplied a genuinely zero-cost fix; rejected
MATERIALS' and VISION's literal fixes on their stated grounds while
accepting their substance) → Phase 3 synthesis (Director: all mandatory
fixes accepted, none overridden, budget unchanged at 68 calls) →
predictions committed (`ed6d007`) → Phase 4 run.

**Result: 68 new FDTD calls, 2724.3s (~45.4 min), ~1.8× the estimate
uniformly across both blocks (flagged, not gate-material).**

**Block T16_CLOSE found the domain and quadrature confounds disclosed at
Iteration 11 do NOT add linearly at r=156 — they interact** (+2.109×10⁻⁴,
clearing the pre-registered ≥2×10⁻⁴ REAL-INTERACTION threshold by ~5%,
the falsifiable band's own pre-registered alternate outcome, not a
surprise). The ladder bucket doesn't flip (stays MARGINAL either way).

**Block N17_NATIVE_V2 is this shift's headline result.** Rebuilt correctly
this time (exp-033's own domain, verbatim — RATIO=1.5 method, not
exp-034's ad-hoc formula); its N9 leg reproduces exp-033's established
citation bit-identically (delta=0.0 exactly), proving the domain carries
no construction confound. **Its N17 leg shows this program's own headline,
first-ever constraint-3 σ(I) OFF-state PASS (exp-032, Iteration 9,
reconfirmed exp-033) downgrades from PASS (C=−0.004586) to MARGINAL
(C=−0.005239)** — the first time this downgrade has been shown at the
geometry the citation actually originates from, without a domain
confound riding underneath it. As of this iteration, no σ(I) OFF-state
configuration this program has ever measured survives N17 angular-
quadrature correction on a correctly-built domain, at either geometry
tested.

**Block T15_RECONCILE (0 new calls) found the g₀-vs-chord-model gap grows
monotonically with resolution** (1.03%/2.69%/3.07% at cpl=20/30/40,
crossing the pre-registered GROWING threshold) — T15 modestly reopens, not
closes, 5–8× smaller than Iteration 10's already-refuted ~15% claim but
real. A separate π/4-vs-chord-model-amplitude gap (~14.3–14.5%, stable
across resolution) was measured for the first time and, at Phase 5,
formally closed as a definitional mismatch (θ=0-only vs N9-oblique-
averaged observables), not an open puzzle.

**Phase 5 (six fresh blind seats + Red Team): unanimous PARTIAL, 6-for-6.**
PHOTONICS and ELECTROMAGNETISM independently proposed the same near-field-
fringe mechanism for the T16 interaction; Red Team ruled it plausible, not
yet accepted (PHOTONICS' own Fresnel-number check found the two blocks
aren't geometrically self-similar — a real confound in the evidence).
VISION SCIENCE's sharpest catch: bit-identical N9 reproduction does NOT
prove N17_NATIVE_V2's domain is confound-free at N17, since the r=156
result proves a domain's effect on C is itself angle-dependent — no
second, independently-built r=78-native N17 domain exists yet to cross-
check against. THERMODYNAMICS caught and fixed a real, previously-
uncaught numeric bug that had propagated silently through two prior
committed experiments: `OFF_STATE_DETECTABILITY_NOTE` stated a
steady-state range of "5.9–49.8×"; the true range, independently
confirmed by Red Team, is 5.0×–132.4× (does not change the UNDETECTABLE
conclusion) — fixed in live code, computed from source values rather than
hand-typed, so it cannot silently drift again. MATERIALS argued, and Red
Team affirmed, that the PASS-downgrade sharpens (not weakens)
REALIZABILITY_MEMO.md's UNOBTANIUM-WITH-PARAMETERS verdict — its
D_req≈540–600× figure is now recaptioned as a lower bound, not an achieved
reference point. QUANTUM OPTICS argued σ(I)'s empirical privilege among
T1's four escape routes is now gone (zero surviving bench PASS, zero
realizable mechanism) even though σ itself was never touched this cycle —
adopted into LOGBOOK's T1 entry.

**Red Team's Checkpoint ruling, explicit: criterion 2 (a proven boundary
within a mechanism class) does NOT fire** — this cycle shows one
calibration point fails correctly-instrumented measurement at both
geometries checked, not that σ(I) as a class is jointly unsatisfiable;
that still needs the still-deferred rigorous RSA/TPA/third-class
literature check, now re-ranked Iteration-13's top priority ahead of the
previously-planned N33 leg (Red Team's own adjudication: every further
ambient-contrast refinement this program has produced is algebraically
orthogonal to the realizability question that check would actually
settle). No other Checkpoint criterion fires. **Program-health
observation, not a criterion firing**: Iterations 7–12 — six consecutive
cycles — have all closed PARTIAL, all instrument-hygiene or reconciliation
work, not mechanism-testing — flagged for Iteration 13's sequencing.

**Mandatory corrections applied same-shift, disclosed not smoothed over**:
`experiments/034-floor-convergence-scale-bridge/design_geometry.py`'s
detectability-note bug fixed in live code (historical NOTES.md/results.json
prose left uncorrected per house convention, an erratum comment added
instead); `REALIZABILITY_MEMO.md`'s D_req figure recaptioned as a lower
bound; a documentation note added on the unsigned-delta convention in
`results.json`. Full record: LOGBOOK.md Iteration 12. Next lead per
rotation: VISION SCIENCE (Iteration 13).

## 2026-08-15 (panel shift) — Iteration 11 complete (exp-034): the paired
cpl=40/r=156/N17 cycle closes T1's floor-convergence item cleanly, finds the
program's only-ever constraint-3 PASS fragile (not cleanly resolved either
way) at r=156, and shows N9 angular quadrature unconverged everywhere it's
been checked — unanimous 7-for-7 PARTIAL, a program first, with a genuine
new confound (EM's Phase-5 catch) stacked under the cycle's own scored
headline, corrected same-shift per Red Team's mandatory-fix list

**Pre-flight:** local `main` synced to Iteration 10's close (`dc4a36e`,
predictions already committed on arrival — this shift continued a
partially-complete iteration, per LOGBOOK's own iteration-record
convention). Deps installed fresh (numpy/scipy/matplotlib/pillow/autograd/
fdtd via pip, then `ceviche --no-deps`, per the recorded wrinkle). Bench
trust suite 46/46 green (`--only 12346789,10,11`) before this shift's work.

**Iteration 11 — The Paired Floor-Convergence / R156 Scale-Bridge Cycle
(exp-034, CONCLUDED).** Lead: THERMODYNAMICS (rotation), executing
Iteration 10's two ranked priorities in one cycle (Red Team's own
recommendation to pair them) plus Red Team's own mandatory fifth fix
(Block N17_NATIVE — the geometry that actually backs the program's only-
ever constraint-3 PASS citation — folded in by Director's budget call
rather than deferred a fifth time). Full seven-seat cycle: Phase 1
proposal (THERMODYNAMICS, four blocks) → 5 blind parallel critiques
(three seats — PHOTONICS, QUANTUM, EM — independently converged on one
root defect in Block R156's disposition logic) → Red Team last with
everything (PROCEED-WITH-MANDATORY-FIXES, 7 numbered attacks, zero
arithmetic errors found anywhere — a first for this program) → Phase 3
synthesis (Director: all 7 fixes accepted; Director's own first catch —
the N17 angle set reproduces exp-024's own historically δ_C-gate-failing
±40° geometry) → predictions committed (`dc4a36e`) → Phase 4 run.

**Result: 115 new FDTD calls, 3378.8s (~56.3 min), after a mid-cycle
harness bug (caught and fixed the same shift).** A `functools.partial`/
`ex.map` argument-passing mistake crashed the first attempt after Blocks
CPL40 and R156 (46 calls, ~30 min compute) had already completed
cleanly — lost, not corrected, since `results.json` only writes once at
the end. Fixed (`2ccb7f6`), verified in an isolated smoke test, full
115-call run restarted clean.

**Block CPL40 closed T1's carried-forward Iteration-10 item cleanly**:
both the empty-scene decision floor and the actually-scored raw-C
currency landed PLATEAU at cpl=40 — neither converging back toward
cpl=20 nor diverging further from cpl=30.

**Block R156 found the program's only-ever σ(I) OFF-state constraint-3
PASS is fragile at scale, but not cleanly resolved either way.**
C(off_pass,156)=−0.005760, MARGINAL not PASS, matching the pre-registered
desk estimate almost exactly. But Phase 5's seven-seat review — led by
ELECTROMAGNETISM's independent catch, confirmed to the same digit by Red
Team's audit and rated "the single most consequential unflagged finding
in the packet" — found a **second, comparably-sized domain-construction
confound** stacked directly under this headline: Block R156's own domain
(GUARD_OUT=336) and Block N17_156's own domain (GUARD_OUT=373) measure
the SAME physical article differently by 3.552×10⁻⁴ — 84% the size of
the angular-quadrature confound the cycle's own Phase-4 draft already
disclosed. Missed by five of six blind Phase-5 seats and both of the
Director's own Phase-3/Phase-4 catches, which only flagged a *different*
domain confound (N17_NATIVE vs exp-033's own established domain). The
downgrade-to-MARGINAL finding is directionally robust (every r=156
reading of this article, four distinct instrument choices, sits on the
MARGINAL/near-PASS side) but not yet resolution/domain-clean.

**Blocks N17_156/N17_NATIVE found N9 angular quadrature — this program's
own measurement standard for every ambient-contrast reading since
Iteration 1 — is not converged anywhere it has now been checked.** At
r=156 own-domain: 4.249×10⁻⁴, 0.88× the established N5-vs-N9 bound (still
flips the PASS/MARGINAL ladder bucket for the identical article). At
r=78-native (the geometry the program's headline PASS citation actually
uses): 1.5467×10⁻³, 3.2× the bound — clean, unconfounded, and decisive.
New live thread **T16** opened: the ambient-contrast channel's own
angular-quadrature and domain-construction uncertainty, now measured for
the first time, is comparable to or larger than several of this
program's headline PASS margins. VISION SCIENCE's own Iteration-10
concern (the PASS margin might sit inside unmeasured quadrature error)
was not just vindicated but understated.

**MATERIALS' realizability memo, deferred three consecutive iterations,
finally written this shift** (zero FDTD cost): **UNOBTANIUM-WITH-
PARAMETERS for both candidate σ(I) mechanism classes**, for two
independent, non-trading-off reasons — reverse saturable absorbers fall
1–2 orders of magnitude short on the required ≈540–600× dynamic range,
independent of irradiance; two-photon absorption clears the dynamic-range
bar comfortably but falls 9–12 orders of magnitude short on operating
irradiance (flashlight ~10⁻³ W/cm² vs published onset 10⁶–10⁹ W/cm²). An
informal desk synthesis, explicitly not a rigorous literature review — a
candidate Checkpoint-criterion-2 finding that does not yet fire.

**Phase 5 (seven fresh seats): unanimous PARTIAL, 7-for-7** — the first
unanimous verdict in this program's panel-era history. Beyond EM's
R156-vs-N17_156 catch (above), the six blind seats independently
converged on: a shared arithmetic error (NOTES.md's own chord-sanity
check stated "1.9%" where the true figure is 0.56% — caught
independently by PHOTONICS, EM, QUANTUM, and Red Team's own audit); a
mislabeled Learned-section claim ("4.2× larger swing at r=156" — actually
0.88×, smaller — caught independently by MATERIALS and QUANTUM, Red Team
traced the likely transcription source); a mislabeled historical constant
(`run.py`'s C78 off_bracket anchor was exp-033's rounded cpl=30 value, not
the true cpl=20-native figure — PHOTONICS' catch, shifts common-mode
fraction 67.2%→73.8%); a genuine regression (exp-033's own transient
dwell-limited ΔT machinery and inline constraint-4 caveat string were
silently dropped this cycle's first draft, caught by THERMODYNAMICS,
restored at close); and a contradiction in live thread T15 (this cycle's
own fresh, code-committed chord model reproduces the measured g₀ to
0.56%, not T15's claimed ~15% deficit — PHOTONICS' catch, flagged as an
open reconciliation item, not resolved either way). **Red Team's audit
independently reproduced every one of these numbers to the same digit**,
added its own nine-attack list, and ruled the unanimous 6-0 seat count
does NOT need overruling this time — "for once the raw count was not too
favorable."

**Mandatory same-shift corrections applied, not smoothed over**: all
seven of Red Team's mandatory fixes landed in
`experiments/034-floor-convergence-scale-bridge/{NOTES.md,results.json,
design_geometry.py,run.py}` plus a new `REALIZABILITY_MEMO.md` and
LOGBOOK.md's T1/T15 entries and new T16. **Checkpoint criterion 4 ruled a
tripwire by Red Team, satisfied by these corrections — does NOT fire.**
No other Checkpoint criterion fires.

**Director's close: VERDICT PARTIAL, unanimous 7-for-7** — the honest
headline is that this cycle answered a narrower, messier question than
its own first-draft Learned section claimed (the same pattern this
program's own precedent names at Iterations 7, 8, 9, and 10), but the
narrowing itself — a real, measured instrument-uncertainty budget on a
channel this program has scored against for eleven iterations without
ever characterizing it — is genuine forward motion. `2ccb7f6` (harness
fix) → `7db48be` (results) → mandatory corrections, all committed this
shift. Next lead per rotation: **QUANTUM OPTICS** (Iteration 12) —
top priority per Red Team's own adjudication: disentangle the R156-vs-
N17_156 domain/quadrature confound before rebuilding N17_NATIVE. Trust
suite 46/46 green throughout (no `lab/` engine changes this shift).

## 2026-08-15 (panel shift) — Iteration 10 complete (exp-033): the g600≥0.69
recurrence's cross-resolution behavior is explained (three independent
confirmations, ≈10⁻⁸ precision) but Red Team's Phase-5 audit overrules a
5-2 PROMISING seat lean to PARTIAL — the question closed was narrower than
queued, the actually-scored currency was left unconverged, Block B was cut,
and two new open questions (a ~15% g₀ chord deficit; a circular retired-
clause successor) surfaced

**Pre-flight:** local `main` synced to Iteration 9's close (`079a3ba`).
Deps installed fresh (numpy/scipy/matplotlib/pillow/autograd/fdtd via pip,
then `ceviche --no-deps`, per the recorded wrinkle). Bench trust suite
46/46 green (`--only 12346789,10,11`) before this shift's work, reconfirmed
immediately pre-run.

**Iteration 10 — The g600 Resolution Check (exp-033, CONCLUDED).** Lead:
ELECTROMAGNETISM (rotation), executing Iteration 9's top-ranked priority:
R3-check the g600≥0.69 recurrence at 600nm, the one wavelength on this
ambient bench line never resolution-tested. Full seven-seat cycle: Phase 1
proposal (EM, two blocks — a desk finding that all twelve existing weak-
article ambient points collapse onto one constant, g₀≈0.6889, once the
empty-scene floor is subtracted additively) → 5 blind parallel critiques
(PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION SCIENCE —
all support-with-changes, each catching a distinct, orthogonal defect) →
Red Team last with everything (PROCEED-WITH-MANDATORY-FIXES, 16 numbered
attacks, two load-bearing catches no blind seat found: a silent σ-rescale
bug reproducing exp-027's historical T10 defect, and a decision-floor
mixed-weighting bug resolving VISION's "unexplained drift" at zero cost)
→ Phase 3 synthesis (Director: all ten mandatory fixes accepted; Block B
— radial_absorbed_power on beam-scene off_pass/off_bracket, Iteration 9's
#2 priority — CUT this cycle per Red Team's own sanctioned fallback,
PHOTONICS' structurally-underpowered-by-2-3-orders attack independently
confirmed; re-queued standalone) → predictions committed (`1f65123`) →
Phase 4 run.

**Result: 50 new FDTD calls, 1036s.** All five pre-registered predictions
confirmed at face value: residual gate 6.4×10⁻⁶ inside the ≤3×10⁻³ gate;
ΔA=4.42×10⁻⁵ inside the CONFIRMED band; settling 0.48%; VISION ladder on
raw C as predicted (off_pass PASS, margin held). **The raw-g600 cross-
resolution shift is fully explained by the empty-scene decision floor's
own shift** — independently confirmed three separate ways (EM's zero-
parameter geometric chord model, QUANTUM's per-article decomposition, Red
Team's cross-check) to ≈10⁻⁸ precision in C-space, a genuine advance
closing T1's carried-forward item.

**Phase 5 (seven fresh seats) found the headline overstated what closed.**
Five seats (THERMODYNAMICS, MATERIALS, QUANTUM OPTICS, VISION SCIENCE,
initially ELECTROMAGNETISM) read PROMISING. Two substantive dissents:
**PHOTONICS** — the "λ-dependence of the floor" attribution is wrong
(media are non-dispersive; what varies is resolution, and the floor is
non-monotone/non-convergent across all three λ under refinement); found a
simpler closure (raw g600≥0.69 was arithmetically guaranteed at every
floor ever measured on this bench); and found g₀ sits ~15% below its own
window-integrated geometric chord model, stable across resolution —
argued as a real diffractive-leakage effect, not noise (new live thread
T15). **RED TEAM's audit** — verified every mandatory fix against the
actual code, found the "floor enters uniformly" robustness claim
arithmetically backwards (a real floor-mismeasurement of the observed
magnitude would have failed the gate; the design worked because the floor
was measured correctly, not because the gate tolerates floor size), found
ΔA≈0 is closer to guaranteed-by-construction than to strong evidence of
resolution-invariant physics (the resolution change was almost entirely a
common-mode floor shift that g_corr is built to cancel), found the
actually-scored raw-C currency was never itself shown resolution-
converged (moved toward FAIL at all four articles, only two points), found
the retired QUANTUM disposition clause's numeric successor is logically
circular, and caught a real run-count bookkeeping bug (50 calls not 47 —
third occurrence of this defect class). **Overruled the emerging
PROMISING lean, invoking this program's own precedent** (verdict turns on
whether a cycle's open questions close — Iterations 7/8/9 all PARTIAL for
the identical reason).

**Mandatory same-shift corrections applied, not smoothed over:** run count
corrected in NOTES.md/results.json/run.py; the floor-robustness paragraph
struck and rewritten with the corrected reasoning; ε_r≡1 qualifiers
attached inline to every PASS citation (not just a separate meta key,
mandatory fix 9's carry-through, MATERIALS' Phase-5 catch); the fix-1
runtime assert's real (non-)protection stated honestly in code (it is
algebraically tautological — σ is defined FROM τ, so it cannot fail);
PLANE_DX's 2.2% non-self-similarity under the ×1.5 rescale noted.
**Checkpoint criterion 4 does NOT fire** — corrected same-shift, per Red
Team's own explicit conditional ruling.

**Director's close: VERDICT PARTIAL**, adopting Red Team's audit over the
raw 5-2 seat count — real, verified forward motion (T1's carried item
closes, three independent confirmations of the floor-subtraction model to
extraordinary precision) narrower than first claimed, with the actually-
scored currency left unconverged and two new open questions surfaced.
MATERIALS' Phase-5 review found R3-CONFIRMED hardens (not leaves
orthogonal) the σ(I) realizability tension, and surfaced a new, much
larger gap: the mechanism must gate at flashlight irradiance (~10⁻³
W/cm²) against published RSA/two-photon onset thresholds (10⁶–10⁹
W/cm²) — 9–12 orders of magnitude short, a candidate Checkpoint-2 finding
if it survives a dedicated check. No other Checkpoint criterion fires.
`1f65123` (predictions) → results/corrections committed this shift. Next
lead per rotation: **THERMODYNAMICS** (Iteration 11) — commits to
proposing VISION's r=156 leg, paired per Red Team's recommendation with a
new top-ranked cpl=40 floor/currency-convergence diagnostic. Trust suite
46/46 green throughout (no `lab/` engine changes this shift).

## 2026-08-14 (panel shift) — Iteration 9 complete (exp-032): first-ever
σ(I) OFF-state PASS against VISION's frozen photopic lab bar, at bench
scale, all 3λ — but qualified by an untested-grid-resolution g-anomaly
recurrence, a structurally-underpowered mechanism discriminator, and a
worsened (≈600×) realizability picture; verdict PARTIAL, Red Team
overrides QUANTUM's lone PROMISING dissent on program precedent

**Pre-flight:** local `main` synced to Iteration 8's close (`afe9f1b`).
Deps installed fresh (numpy/scipy/matplotlib/pillow/autograd/fdtd via
pip, then `ceviche --no-deps`, per the recorded wrinkle). Bench trust
suite 46/46 green (`--only 12346789,10,11`) before this shift's work.

**Iteration 9 — The σ(I) OFF-State PASS-Boundary Run (exp-032,
CONCLUDED).** Lead: MATERIALS (rotation), executing Iteration 8's
binding, three-times-deferred priority — VISION's own σ(I) OFF-state
PASS-boundary run, top Phase-5 pick for three consecutive iterations.
Full seven-seat cycle: Phase 1 proposal (MATERIALS) → 5 blind parallel
critiques (PHOTONICS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS,
VISION SCIENCE — all support-with-changes, three independently
converging on the same risk: the proposal's g-transfer constants
extrapolate two of exp-026's own documented, unresolved band-misses
below their tested range) → Red Team last with everything (proceed-
with-mandatory-fixes: a below-τ_off bracket point correcting a mislabeled
critique suggestion, a zero-cost disposition clause, a zero-cost energy
sidecar) → Phase 3 synthesis (Director: every mandatory fix accepted,
VISION's r=156 companion leg explicitly overridden and queued, not
dropped) → predictions committed (`9a186a4`) → Phase 4 run.

**Result: 81 new FDTD calls, ~9.4 minutes** (`8723882`). **`off_pass`
(τ=0.0065) clears VISION's frozen |C|<0.005 photopic lab bar at all
three wavelengths — the first σ(I) OFF-state configuration in this
program's nine-iteration history to do so.** Three iterations of
deferral produced a genuine result, not a null. Against that: QUANTUM's
own pre-registered disposition clause fired on the 600nm channel
(g=0.6927, matching off_lab's established, previously-unexplained
g600=0.6913) — now a 4-point recurrence across three experiments, but
two Phase-5 seats (PHOTONICS, QUANTUM OPTICS), reasoning independently,
caught that every one of those points shares a grid resolution never
varied at 600nm — the one wavelength on this bench line that has never
received this program's own mandatory R3 resolution check. "Reproducible
anomaly" language walked back to flagged-pending-check accordingly. The
bracket-point discriminator (`off_bracket`, τ=0.003, Red Team's own
mandatory fix) came back a genuine, informative null on the bulk-vs-edge-
scattering mechanism question — ELECTROMAGNETISM's Phase-5 finding
sharpened *why*: an aggregate ambient-contrast measurement is
structurally underpowered for that question at these optically-thin τ
regardless of SNR; the correctly-targeted instrument
(`radial_absorbed_power`, exp-028, already validated) was unused this
cycle. A PASS here mechanically *worsens* σ(I)'s realizability picture —
the σ_on/σ_off ratio a real switch would need to span grows to ≈600×,
worse than exp-026's already-unobtainium 122–487× — and MATERIALS' own
Phase-5 review put a first-ever citable number next to the standing
UNOBTANIUM-WITH-PARAMETERS label (reverse saturable absorbers, real
enhancement factors 2–10×, 1–2 orders of magnitude short of 600×).

**Three zero-cost desk corrections applied same-shift, not deferred**
(`0ff663e`): THERMODYNAMICS' own self-caught energy-sidecar arithmetic
defect (a reported τ-ratio juxtaposed with an unrelated ON-article anchor
as if combined; the physically apt absorbed-fraction ratio is ~6.4×
larger, corrected and flagged as an erratum, not silently rewritten); an
ambiguous SNR citation (two channels' predicted SNR coincidentally
rounding to the same figure); and a `results.json` scoring-status
clarification (the bracket article's ladder score was never intended as
a second headline PASS claim).

**Phase 5's most consequential finding: two independent seats
(PHOTONICS, QUANTUM OPTICS), reasoning through different framings,
converged on the same load-bearing gap** — the g600 recurrence's
"reproducibility" rests entirely on measurements sharing an untested
grid setting, this program's one remaining gap in an otherwise-applied
house rule (450/750nm were both R3-checked, exp-025; 600nm never has
been). QUANTUM OPTICS alone called this cycle PROMISING, reasoning from
the genuine first-ever PASS; Red Team's audit overrode that verdict to
PARTIAL, on this program's own established precedent (Iterations 7 and 8
both PARTIAL despite genuine positive content, for the identical reason:
verdict turns on whether a cycle's own open questions close, not on a
favorable headline number) — QUANTUM's dissent preserved on the record,
not silently dropped, per PANEL.md's own discipline.

**Director's close: VERDICT PARTIAL**, adopting Red Team's own ruling.
No Checkpoint criterion fires — this is real, logbook-advancing forward
motion on constraint 3 specifically, directly answering Iteration 8's
own program-integrity flag (five straight cycles of instrument/
reconciliation work with no new σ(I) candidate tested) rather than
repeating it. This PASS is explicitly a bench-scale diagnostic (VISION's
own idealization iii, Iteration 1), NOT a Tier-W/Tier-A constraint-3
verdict — the r=156 scale-bridge companion leg (queued since Iteration
3) stays queued, now explicitly third in Iteration 10's line, behind the
R3 check and the mechanism instrument. `9a186a4` (predictions) →
`8723882` (results) → `0ff663e` (Phase-5 close). Next lead per rotation:
ELECTROMAGNETISM (Iteration 10). Trust suite 46/46 green throughout (no
`lab/` engine changes this shift).

## 2026-08-14 (panel shift) — Iteration 8 complete (exp-031): Red Team
catches a load-bearing construction bug (missing PEC core) none of five
blind seats found, and the fix turns out quantitatively negligible; T12's
ripple sweep is a clean but scope-limited null; T13 gets worse, not
better, and is elevated into new live thread T14 (the absorber's
wrong-direction asymptote); Red Team raises a program-integrity flag —
five straight cycles with no new constraint-3 mechanism tested

**Pre-flight:** local `main` synced to Iteration 7's close (`377c785`).
Deps installed fresh (numpy/scipy/matplotlib/pillow/autograd/fdtd via
pip, then `ceviche --no-deps`, per the recorded wrinkle). Bench trust
suite 46/46 green (`--only 12346789,10,11`) before this shift's work.

**Iteration 8 — The T12 Ripple Sweep, the T13 Desk Reconciliation, and
QUANTUM's σ-Held g-Point (exp-031, CONCLUDED).** Lead: PHOTONICS
(rotation), executing Red Team's Iteration-7-ranked queue in one cycle.
Full seven-seat cycle: Phase 1 proposal (PHOTONICS, zero-FDTD desk
derivation + a scoped FDTD sweep) → 5 blind parallel critiques
(MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE — all support-with-changes) → Red Team last with everything
(verdict: proceed-with-mandatory-fixes, 9 numbered attacks, **one caught
by none of the five blind seats and predating this cycle: exp-030's own
`graded_black_shell` absorber construction was missing its historical
PEC core** — every other construction of this article since exp-001
pairs a PEC core with the graded shell; exp-030's own ambient-scene
builder never did, silently making every θ=0/ambient absorber reading it
ever produced a hollow-shell measurement, not the intended solid-backed
one) → Phase 3 synthesis (Director: every mandatory fix accepted, zero
overridden — the core-correction folded directly into the T12 sweep
rather than run as a separate bolt-on) → predictions committed
(`09cb9f7`) → Phase 4 run.

**Result: 18 new FDTD calls, ~13 minutes for the sweep+quantum legs**
(`ce214cd`). **The core-correction delta turned out negligible**
(6.8×10⁻⁶, five orders of magnitude below the pre-committed "negligible"
threshold) — good news: Red Team's catch was real and necessary as a
matter of construction correctness, but the corrected number
independently reproduces this program's own T9 finding ("the graded
shell's own optical depth extinguishes nearly all incident power before
it reaches the core, in either construction") via a completely new
measurement channel. **T12's own dense PLANE_DX sweep came back a clean,
unambiguous null** — zero significant sign reversals across 17 swept
points, for PEC or the absorber, at either r=78 or r=156 — directly
refuting its own falsifiable prediction. Phase 5's blind seats
(ELECTROMAGNETISM, then PHOTONICS independently) found the sweep's own
N_F coverage (≈8–110) never actually reaches the N_F window (≈81–325)
where PEC's original r=156→312 reversal lives — narrowing T12's live
hypothesis space rather than closing it. **T13 (the |C|≈0.98-vs-fitted
witness-scale gap) stayed unresolved for the one article that matters,
and got WORSE**: the corrected, shorter-baseline absorber dual-law fit
disagrees by 0.220, exceeding the original uncored/longer-baseline
disagreement of 0.132; a zero-FDTD desk audit found the standing
|C|≈0.98 figure traces to exactly one unsourced sentence in this
program's entire record (Iteration 1's EM Phase-5 review). **QUANTUM's
σ-held g-calibration gap closed** at one new floor-corrected point
(g=0.697, within 2% of established τ-held endpoints) — though Phase 5
(QUANTUM's own review, Red Team-confirmed) found the closing language
had overclaimed: the correction is licensed only by an unstated linear-
response assumption, valid at |C|≈1% and untested elsewhere, corrected
in the record.

**The accepted THERMODYNAMICS energy sidecar failed twice and is
deferred, not silently dropped.** First attempt used a computed-but-
never-actually-used geometry field and produced unphysical results;
second attempt (a hand-built box) stalled past budget and was killed.
THERMODYNAMICS' own Phase-5 review — independently verified by Red
Team — sharpened the diagnosis past NOTES.md's own account: the real
root cause was an invalid reference-intensity strip (`ref`), not the
box, and a negative-`i_inc` garbage block had been left in `results.json`
unlabeled, a real gap against "flag, don't silently rewrite." Both
findings corrected this shift: the block relocated to an explicitly-
named `thermo_attempt1_INVALID` key with an erratum note, and the still-
live code guarded with a `NotImplementedError` naming the actual defect
so a third attempt can't silently repeat it.

**Phase 5's most consequential finding: two blind seats (PHOTONICS,
ELECTROMAGNETISM), reasoning independently through different functional-
form diagnostics, converged on the same structural anomaly** — the
absorber's contrast shallows, not deepens, as the measurement approaches
what should be the geometric-shadow regime (a negative ceiling-law
exponent; a negative sqrt-law slope). Red Team's audit named this the
cycle's single most decisive result: the exact pathology Iteration 7's
finding e2 first flagged, now independently confirmed on a corrected
construction and a shorter baseline — three separate axes of
confirmation for the same anomaly. Elevated to new live thread **T14**.
Red Team also caught, independently of any blind seat, that the
cheapest proposed follow-up (EM's own pick — extend the PLANE_DX sweep
to reach the missing N_F window) is likely geometrically infeasible as
described, requiring sub-0.2λ standoff — tipping Iteration 9's queue
toward PHOTONICS' costlier but structurally sound multi-point r-sweep
instead.

**Director's close: VERDICT PARTIAL**, adopting Red Team's own ruling.
No Checkpoint criterion fires on the letter, but Red Team raised — and
the Director adopted as a binding Iteration-9 priority, not a violation
— an explicit program-integrity flag: **Iterations 4 through 8 are five
straight cycles of instrument/reconciliation/audit work, with no new
σ(I) mechanism candidate tested against constraint 3 since Iteration 3.**
VISION's cheapest, most directly mechanism-relevant proposal (one new
run to locate the program's own predicted σ(I) PASS boundary,
τ_off≈0.0065) has been the top-ranked Phase-5 pick for three consecutive
iterations without being built — queued first, explicitly, for Iteration
9, ahead of T14's own follow-up and THERMO's trust-suite prerequisite.
`09cb9f7` (predictions) → `ce214cd` (results) → this close-out. Next
lead per rotation: MATERIALS (Iteration 9). Trust suite 46/46 green
throughout (no `lab/` engine changes this shift).

## 2026-08-14 (panel shift) — Iteration 7 complete (exp-030): the r=156/312
near-field→witness-scale bridge executed in full (Checkpoint-4 tripwire
does not fire), verdict PARTIAL — PASS/FAIL language now decidable on
near-threshold constraint-3 C values, but every σ(I) OFF-state article
ever built still fails or is marginal, and Red Team's Phase-5 audit
catches a program-wide unreconciled witness-scale discrepancy no blind
seat found

**Pre-flight:** local `main` synced to Iteration 6's close (`e4a9bca`,
forced-updated from a stale local checkout). Deps installed fresh
(numpy/scipy/matplotlib/pillow/autograd/fdtd via pip, then
`ceviche --no-deps`, per the recorded wrinkle). Bench trust suite 49/49
green (`--only 12346789,10,11`) before this shift's work.

**Iteration 7 — The r=156/312 Near-Field→Witness-Scale Bridge (exp-030,
CONCLUDED).** Lead: VISION SCIENCE (rotation) — the five-times-deferred,
Checkpoint-4-tripwired mandatory build. Full seven-seat cycle: Phase 1
proposal (VISION SCIENCE) → 5 blind parallel critiques (PHOTONICS,
MATERIALS, ELECTROMAGNETISM, THERMODYNAMICS, QUANTUM OPTICS — all
support-with-changes, three independently converging on the same
`graded_black_shell` optical-depth confound via three different
diagnoses) → Red Team last with everything (proceed-with-mandatory-
fixes, 11 numbered attacks, four caught by none of the five, most
consequential: the proposal's own r=78 anchor values used the wrong,
gate-failing ±40° geometry) → Phase 3 synthesis (Director: every
mandatory fix accepted, zero overridden) → predictions committed
(`a318daa`) → Phase 4 run.

**Result: 89 new FDTD sim calls, ~5.1 hours wall-clock** (the r=312 leg
alone — 37 runs, restoring N=9 angle sampling for the two hard-edged
articles per Red Team's own mandatory fix — took 3.87h, ~8× the
proposal's own hand estimate, the largest single timing miss in this
program's history, driven by κ³ FDTD cost scaling). **The cycle's real
deliverable: PASS/FAIL language is now decidable on the program's near-
threshold constraint-3 C values for the first time** — a δ_C decision-
floor check (Red Team's own mandatory fix) passed cleanly at both r=156
(−0.00121) and r=312 (−0.00028/−0.00024), and the load-bearing
prediction (both OFF-lab/OFF-field sponges' scale-robustness across the
4× radius range) confirmed cleanly. T9 and T11 both closed with their
first-ever floor-referenced verdicts, computed in code: T9's established
null sits 234–446× below the measured box-ledger floor (decisively
null), T10's established spread sits 93–178× above it (decisively
real). The corrected r=78 anchor for the absorber (−0.7209, V-weighted
fallback geometry) supersedes the previously-cited −0.684/−0.686
(sourced from the wrong, gate-failing geometry).

**Against that, the cycle's own central technical question — does
C(z/z_R) bridge cleanly from bench to witness scale — came back
genuinely unresolved, on three independent grounds.** PEC's C(r) proved
flatly non-monotonic (−0.8673→−0.8698→−0.8659, deepens then shallows) —
PHOTONICS and EM, reviewing blind, independently proposed the same
mechanism by different routes (a Fresnel-zone/edge-diffraction ripple
aliased by the family's factor-4 Fresnel-number jumps at a fixed
measurement-plane offset) — new live thread **T12**. The absorber's own
shape-ratio discriminator (5.33) fell outside both candidate power-law
bands, meaning even its nominal fit-validation pass doesn't actually
validate the functional form. **Most consequentially, Red Team's Phase-5
audit — missed by all six blind review seats — found that this cycle's
own fitted witness-scale prediction (absorber ≈−0.734, PEC ≈−0.862,
essentially flat across the entire witness uncertainty band) sharply
contradicts the |C|≈0.98 estimate that has justified prioritizing this
exact thread across five iterations, with no reconciliation anywhere in
the program's record** — new live thread **T13**. The Director's own
added reading: the fitted C_∞ never approaches −1 as z/z_R→0, a
structural mismatch with the far-field silhouette physics the bridge
was built to reach, not merely a numerical gap.

**Program-integrity statement, made explicit per Red Team's own demand:**
the decidability achievement is real, but scored against VISION's own
frozen thresholds, **no σ(I) OFF-state article this program has ever
built has PASSed constraint 3 at any tier, at any scale** — OFF-lab is
MARGINAL everywhere, OFF-field is FAIL everywhere. This cycle
characterized the measuring instrument; it did not find, or bring
closer, a working escape route — any future summary must carry that
sentence, not just "PASS/FAIL now licensed."

**Two record corrections made this shift, flagged not silently
rewritten:** MATERIALS' Phase-2 realizability figure (a real unit
error — witness radius misread as diameter — corrected from "0.6–1.9m"
to the honest 0.31–0.92m, still comfortably unobtainium); and the
sponges' apparent r=156 non-monotonicity, now read as 87–97%
explained by δ_C-floor instrument bias, not a real effect (doesn't
touch the P-VISION-3 gate itself, which correctly uses only the
floor-clean 78/312 endpoints).

**Verdict: PARTIAL** (Red Team's own explicit ruling, adopted). New
Checkpoint-4 tripwire on the record for future shifts: citing this
cycle's witness-scale numbers without flagging T13, or treating PEC's
fit/witness number or `box_dev` as a settled floor before their own R3
checks resolve, is a retroactive criterion-4 trigger. Checkpoint
criterion 4 itself does not fire this cycle. `a318daa` (predictions) →
`fa64268` (Phase 5 close). Next lead per rotation: PHOTONICS (Iteration
8), queue Red-Team-ranked: T12's dense-standoff-sweep pair, T13's
zero-cost desk reconciliation (explicitly prioritized ahead of further
FDTD work), QUANTUM's one new r=156 σ-held sponge run.

## 2026-08-13 (panel shift) — Iteration 6 complete (exp-029): the
coherent-superposition bridge gate validated end-to-end on its fourth
committed cycle, every prediction confirmed, Checkpoint criterion 5
given its first-ever explicit ruling, Red Team catches VISION's own
Phase-5 count error

**Pre-flight:** local `main` synced to Iteration 5's close (`df71f1d`).
Deps installed fresh (numpy/scipy/matplotlib/pillow/autograd/fdtd via
pip, then `ceviche --no-deps`, per the recorded wrinkle). Bench trust
suite 43/43 green (`--only 12346789`) + stage 10 2/2 before this shift's
work.

**Iteration 6 — The Coherent-Superposition Bridge Gate (exp-029,
CONCLUDED).** Lead: QUANTUM OPTICS (rotation) — the mandatory,
fourth-cycle build of QUANTUM's own bridge-gate package, deferred at
Iterations 2, 3/4, and 5. Full seven-seat cycle: Phase 1 proposal
(QUANTUM) → 5 blind parallel critiques (PHOTONICS, MATERIALS,
ELECTROMAGNETISM, THERMODYNAMICS, VISION SCIENCE, all support-with-
changes — EM and THERMODYNAMICS independently converged on the identical
Cauchy-Schwarz normalization catch) → Red Team last with everything
(proceed-with-mandatory-fixes, six numbered attacks, one caught by none
of the five: the proposal's own printed self-check assertion failed on
its own tabulated amplitude) → Phase 3 synthesis (Director: all six
fixes accepted, zero overridden) → predictions committed (`1185345`) →
Phase 4 run.

**Result: every prediction confirmed — the cleanest cycle in this
program's history by that measure.** 6 new FDTD sim calls, 266s (one
harness bug — a bare `numpy.int64` failing JSON serialization — caught
after all runs completed, before any result was trusted, fixed and fully
rerun). New machinery (`lab/validation/run_all.py::
stage11_multisource_superposition`, the panel program's first check of
≥2 concurrent sources in one `Sim`) gated by new suite stage 11: joint-
vs-summed field-phasor identity holds to 1.9×10⁻¹⁵–2.5×10⁻¹⁵ RMS relative
error, both vacuum and lossy-object scenes — confirming EM's/Red Team's
Phase-2 line-by-line trace that this engine's per-step update is exactly
linear in the source terms. The renormalized coherent-interference
finding (Red Team's mandatory fix 2) measured **+0.0224% of the beam's
own absorbed power**, real and nonzero but 126–152× below its Cauchy-
Schwarz ceiling — two independent Phase-5 seats (EM, QUANTUM) converged
on a corrected TRUE ceiling of 3.40% (vs. the pre-registered nominal
2.83%), and QUANTUM's own degree-of-coherence framing (γ≈0.66%) shows
~99.3% of the theoretically achievable coherent enhancement washes out
by spatial averaging in this specific geometry — explicitly not a
universal law. A bin-wise check (Red Team's recommended fix 6)
confirmed real, small spatial structure (5.02× the aggregate reading, a
genuine radial interference fringe) that an aggregate closure check
alone would have washed out. `1185345` (predictions) → `b0f5305`
(results). **The bridge-gate machinery is now validated end-to-end and
gated permanently — no longer deferred.**

**Phase 5 — six fresh seats blind + Red Team audit (verdict: MINOR
ISSUES).** Rich, fully independent convergence: EM and QUANTUM both
derived the corrected 3.40% Cauchy-Schwarz ceiling from measured powers
without seeing each other's work; PHOTONICS and QUANTUM both explained
the interference term's near-total cancellation via a Bessel/Hankel
radial-integral mechanism. QUANTUM's own Phase-5 review scoped a
concrete, cheap incoherent-ensemble follow-up (a `phase_offset` source
kwarg; one additional joint run exactly determines the interference
sinusoid; the incoherent limit follows analytically as exactly zero
mean) — Red Team independently re-derived this claim from first
principles and confirmed it mathematically exact, with one scope
correction (only one additional run is needed, not two). **Red Team
caught one real record defect**: VISION's Phase-5 review stated exp-029
was "the fourth consecutive constraint-3-silent cycle," presented as a
correction to her own Iteration-5 count of three — Red Team's
independent audit found Iteration 3 (exp-026) actually ran a real,
81-run ambient scene with reported Weber-contrast C values, misclassified
as beam-scene-only; **corrected count: three, matching Iteration 5's own
original figure, not four.** Logged here rather than silently absorbed;
VISION's underlying institutional concern (three consecutive
constraint-3-silent cycles before Iteration 7) stands. **Checkpoint
criterion 5 given an explicit ruling for the first time in this
program's history** (per VISION's own request, Red Team-endorsed):
does NOT fire, and is not close — every iteration has produced a real,
logbook-advancing result.

**Director's close: VERDICT PROMISING.** No checkpoint criterion fires
this cycle. T11 (box-ledger decision-floor characterization, now the
single most-repeated unclosed backlog item, 5-of-6 Phase-5 seats
effectively unanimous) folded in as a companion to Iteration 7's own
r=156 build (VISION's own Phase-5 pick), with r=156 itself keeping
strict priority if scope pressure emerges. QUANTUM's bridge-gate package
marked CLOSED; its own remaining open half (the incoherent-ensemble
idiom, docket #4/(b)'s beam+ambient-C-reproduction) queued for a future
QUANTUM lead cycle, concretely scoped and mathematically pre-verified.
Next lead: VISION SCIENCE (Iteration 7, already hard-committed — r=156 +
T11). Iteration 8 (PHOTONICS) inherits a full merged-ranking queue: the
incoherent-ensemble idiom, docket #7's thermal sidecar, a reciprocity
check (new), the shell-thickness economy sweep, 3-λ radial-ledger +
angular decomposition, T10's residual sweep. Five commits to main this
shift (deps/env setup untracked; suite-stage-11 build + predictions
commit; results commit; this close-out). Trust suite 48/48 green
throughout (new stage 11 added and gated this shift).

## 2026-08-13 (panel shift) — Iteration 5 complete (exp-028): T10
substantially reframed (96% of the reported 46%→128% "enlargement" was an
uncontrolled optical-depth confound, not resolution), T9 sharpened from
coincidence to mechanism, new live thread T11 opened, VISION's Phase-5
dissent preserved on the record

**Pre-flight:** local `main` synced to Iteration 4's close (`e8474b0`).
Deps reinstalled (pyMKL wheel fails here, `ceviche --no-deps` per the
recorded wrinkle). Bench trust suite 41/41 green (`--only 12346789`)
before this shift's work.

**Iteration 5 — The Radial Ledger and the Channel Cross-Check (exp-028,
CONCLUDED).** Lead: THERMODYNAMICS (rotation). Full seven-seat cycle:
Phase 1 proposal (THERMO: box-ledger cross-check at exp-027's own Block 2
rescaled-cpl geometry — the 5-of-7 Iteration-4 consensus item — plus a new
radial-binned absorbed-power ledger for T9's spatial follow-up) → 5 blind
parallel critiques (PHOTONICS, MATERIALS, ELECTROMAGNETISM, QUANTUM
OPTICS, VISION SCIENCE, all support-with-changes) → Red Team last with
everything (proceed-with-mandatory-fixes, 7 numbered attacks) → Phase 3
synthesis (Director: all seven fixes accepted, zero overridden) →
predictions committed (`e9c1d90`) → Phase 4 run.

**Red Team's load-bearing catch, before any run:** MATERIALS' Phase-2
critique found that exp-027's own Block A/Block 2 reuse would inherit a
real code bug — `SIGMA_ON` is a single module constant fixed at the
native `R_OUT=78`, never rescaled to Block 2's own per-λ-rescaled
`r_out` (114/117/119 cells). Red Team escalated this from "fix the new
proposal" to "the published record needs a correction": **exp-027's own
published Block 2 (the T10 finding) silently drifted the ON article's
optical depth from τ=3.9 to 5.70/5.85/5.95 across the λ sweep.** An
explicit erratum was added to T10's LOGBOOK.md entry this shift,
independent of exp-028's own outcome — T10's resolution question was
reopened, not answered, pending a correctly-τ-held rerun. This experiment
(Block A) is exactly that rerun, with a code `assert` holding
τ_center=3.9 exactly at all 3λ.

**Result: T10 substantially reframed, T9 sharpened into a mechanism.** 12
new FDTD sim calls, ~8 min. New machinery (`lab/sections.py::
radial_absorbed_power`) gated by new suite stage 10 (PEC-core hard zero +
empirical closure, calibrated 1.5% after a first-run measurement of
1.11%, confirmed settling-independent across a 4× step sweep) — full
bench 45/45 green throughout. **Block A: box-ledger σ_ext relative spread
= 6.49% (flat), and once τ is correctly held, the corrected beam-behind
spread is only 46.41%→49.46% (+3.05pp) — not the published
46.41%→127.57% (+81.16pp). 96% of T10's originally reported "enlargement"
evaporates**; a small residual (+3.05pp) survives, open, two orders of
magnitude smaller than what was recorded. **Block B: Cell B's (non-PEC)
core absorbs only 0.0062% of total power** (resolution-stable at cpl×1.5,
0.00027%) — T9's PEC-incidental finding is sharpened from an aggregate
coincidence into a mechanistic one: the graded shell's own conductivity
profile extinguishes nearly all incident power before it reaches the
core, in either construction. `e9c1d90` (predictions) → `78d0292`
(results).

**Phase 5 — six fresh seats blind + Red Team audit (verdict: MINOR
ISSUES).** Three of six seats (EM, THERMODYNAMICS, QUANTUM) independently
caught the SAME record defect — Cell B's core fraction was displayed as
"0.01%" when the true value is 0.0062% (a display-rounding artifact: a
pre-rounded fraction re-labeled as a percent instead of the full-precision
fraction converted first) — a first for this program (prior Red Team
audits caught defects no other seat had independently found). Red Team
caught a second instance of the same bug class (a resolution-match figure
reported as "55.47" instead of the true 55.5 exactly). Both corrected
same-shift in NOTES.md, LOGBOOK.md, and `run.py`'s print format. **New
LIVE THREAD T11 opened**: the box-ledger channel's own decision-floor
characterization, promoted from a twice-recurring unassigned Red Team
queue item (Iteration 4 and Iteration 5's own mandatory-fix docket) to a
formally tracked thread — now the single most-repeated unclosed backlog
item in this program's live-thread history. **VISION's Phase-5 dissent
preserved on the record, not overridden silently**: her seat argued the
Iteration-7 commitment for r=156 (made in Phase 3, this shift) schedules
three consecutive beam-scene-only iterations (4, 5, 6) before it executes,
and should have been Iteration 6 instead. Red Team's own audit
independently verified VISION's cycle-count and pre-registered a
Checkpoint-4 tripwire: if Iteration 7 does not execute the r=156 build as
committed, criterion 4 (constraint quietly dropped) fires automatically,
not as a fresh judgment call.

**Director's close: VERDICT PROMISING.** No checkpoint criterion fired
this cycle; one pre-registered as a tripwire on a future cycle. LOGBOOK
updated: T10 marked substantially reframed (not fully closed — small
residual open); T9 updated with the mechanistic explanation; new LIVE
THREAD T11 opened. Queue for Iteration 6 (lead per rotation QUANTUM
OPTICS; PLAN.md updated): QUANTUM's own mandatory coherent-superposition
bridge-gate build (its fourth-cycle commitment, scoped per its own
Phase-5 notes — a graded-shell-shaped endpoint article, not uniform disk;
the radial-power closure identity as a second acceptance gate), plus T11's
decision-floor characterization, the cheap residual-closing diagnostic,
the 3-λ radial-ledger extension, docket #7's thermal sidecar, and a
shell-thickness economy sweep. Iteration 7 (VISION) carries the r=156
build as a pre-registered Checkpoint-4 tripwire. Four commits to main this
shift (2 lab/engine + docs, predict/results pair) — actually: engine +
docs bundled with the predictions commit, results commit, and this
close-out. Trust suite 45/45 green throughout (new stage 10 added and
gated this shift).

## 2026-08-13 (panel shift) — Iteration 4 complete (exp-027): T9 answered
(PEC incidental to the extinction-paradox gap), P-MAT4 half-resolved (settling
refuted, but the R3 spatial check made the anomaly WORSE — a new pattern,
new live thread T10), Red Team + Quantum catch four record errors

**Pre-flight:** local `main` up to date at Iteration 3's close (`e74c72c`).
Deps reinstalled (pyMKL wheel fails here, `ceviche --no-deps` per the
recorded wrinkle). Bench trust suite 41/41 green (`--only 12346789`)
before this shift's work, rechecked after exp-027 (no `lab/` engine changes
this shift).

**Iteration 4 — Settling, Spread, and the PEC Ablation (exp-027,
CONCLUDED).** Lead: ELECTROMAGNETISM (rotation). Full seven-seat cycle run
as fresh sub-agents per PANEL.md's independence mechanics: Phase 1
proposal (two Iteration-3 queued threads combined onto one shared,
already-validated beam-scene bench: a settling-time diagnostic + R3
spatial companion for P-MAT4's chromatic beam-behind anomaly, and a
PEC-ablation factorial for T9's σ_abs/σ_ext anchor ambiguity) → 5 blind
parallel critiques (PHOTONICS, MATERIALS, THERMO, QUANTUM, VISION, all
support-with-changes) → Red Team last with everything (proceed-with-
mandatory-fixes, 7 numbered attacks — two independently-verified code-level
catches: MATERIALS' Cell-B double-write and PHOTONICS' settling-monotonicity
argument, both re-derived from scratch by Red Team rather than trusted) →
Phase 3 synthesis (Director: all seven fixes accepted in full, zero
overridden) → predictions committed (`5f5f01c`) → Phase 4 run.

**Result: both queued threads resolved, in opposite directions from the
proposal's own framing.** 16 new FDTD sim calls, 590s. T9's PEC-cored-vs-
solid-disk question is answered: a single-variable factorial (identical
graded-shell profile, PEC core present vs. replaced with matched-
conductivity fill) measured Δσ_abs/σ_ext = +1.56×10⁻⁶ — indistinguishable
from zero, corroborated by an identical angular-scattering pattern.
PEC-presence does not drive the established 0.51-vs-0.61 gap; rim/profile-
transmission geometry does. P-MAT4's chromatic beam-behind anomaly:
settling-time is cleanly, uniformly refuted at all 3λ (doubling
`BEAM_STEPS` moves beam-behind ≤0.0012pp everywhere) — but the standard R3
spatial-resolution check (cpl×1.5, this program's own 5-times-proven
precedent) made the anomaly dramatically WORSE instead of confirming or
refuting it as artifact (relative spread 46%→128%), the first time in this
program's history an R3 check has enlarged a feature. `5f5f01c`
(predictions) → `fb789ae` (results).

**Phase 5 — seven fresh seats, blind, including a Red Team audit.**
Unusually strong 5-of-7 consensus (MATERIALS/PHOTONICS/EM/QUANTUM/RED TEAM)
on one next action: a box-ledger-vs-envelope-ratio cross-check at Block 2's
own rescaled-cpl geometry, to discriminate a `BEAM_BEHIND`-specific
near-field artifact from a general grid-resolution defect. **Red Team's
audit (verdict: MINOR ISSUES) caught two real numeric defects** — Cell B's
value misrounded (true delta 6.4× smaller than the "0.00001" printed
throughout the record) and the pre-freeze-disclosure blind-run count
undercounted ("three of 16" when the true figure, confirmed against the
enumeration beneath it, is eight of 16) — **and QUANTUM independently
caught a third, different scoring error**: VISION's commitment clause was
scored "not triggered" using only Block 1's small deltas, when the clause
as written covers "Block 1/2" and Block 2's much larger deltas
(up to −1.54pp) trigger it by 4–5×. All four corrections applied same-shift
in NOTES.md and LOGBOOK.md; none touch a scored physics conclusion.

**Director's close: VERDICT PROMISING.** No checkpoint criterion fired.
LOGBOOK updated: T9 marked ANSWERED (with Red Team's floor-gating caveat
carried forward — this box-ledger channel has no established decision
floor the way the ambient bench's δ_C does); new LIVE THREAD T10 opened
for the R3-enlarges finding. Queue for Iteration 5 (lead per rotation
THERMODYNAMICS; PLAN.md updated): (a) the box-ledger cross-check at Block
2's geometry (5-of-7 consensus); (b) a genuine settling check at Block 2's
own finer cpl (4-of-7 consensus); (c) VISION's r=156 scale-bridge check,
now argued more urgent post-T10; (d) a formal decision-floor
characterization for the box-ledger channel (Red Team's own recommendation);
(e) QUANTUM's bridge-gate package, proposed as a mandatory rider on
Iteration 5's lead rather than a fifth competing item — three consecutive
iterations have each had a legitimate, cycle-specific reason to defer it,
which QUANTUM's own seat argues is itself now the finding; (f) THERMO's
radial-binned absorbed-power ledger, a new THERMO-only pick testing whether
exp-027's Cell A/B near-identical aggregate ratio hides a real spatial
heating-profile difference. Three commits to main this shift (predict/
results pair + this close-out). Trust suite 41/41 green throughout.

## 2026-08-13 (panel shift) — Iteration 3 complete (exp-026): the σ(I)
endpoint triplet, a decisive Red Team catch that held up against real
data, and a program-wide sharpening of an "established" quantity

**Pre-flight:** local `main` detached at a stale point (same bookkeeping
class as every prior shift) — fixed with `git fetch origin main && git
checkout -B main origin/main`. Deps reinstalled (pyMKL wheel fails here,
`ceviche --no-deps` per the recorded wrinkle). Bench trust suite 41/41
green (`--only 12346789`) before this shift's work, rechecked after
exp-026 (no `lab/` engine changes this shift — a small bug in the new
experiment's own `run.py` elapsed-time bookkeeping was fixed, not the
engine).

**Iteration 3 — The σ(I) Endpoint Triplet (exp-026, CONCLUDED).** Lead:
MATERIALS (rotation). Full seven-seat cycle run as fresh sub-agents per
PANEL.md's independence mechanics: Phase 1 proposal (three static sponge
articles — OFF-lab τ=0.008, OFF-field τ=0.032, ON τ=3.9 — on exp-024's
±35° fallback baseline) → 5 blind parallel critiques (PHOTONICS, EM,
THERMO, QUANTUM, VISION, all support-with-changes) → Red Team last with
everything (proceed-with-mandatory-fixes, one decisive catch: the
proposal's P-MAT8 prediction, σ_abs/σ_ext≥0.90 for the ON article,
directly contradicted the bench's own ESTABLISHED `graded_black_shell`
measurement at the same r_out, 0.51 — an extinction-paradox bound the
article couldn't physically clear) → Phase 3 synthesis (Director: P-MAT8
rebanded to [0.35,0.65]; P-MAT5 widened and marked provisional, since it
rode the same optimistic assumption; the edge-hardness rider replaced
with a T7-anchored 3-way partition; VISION's PASS/FAIL-language concern
accepted in full — struck from every near-threshold reading — with her
own remedy (build a scale-bridge check now) deliberately deferred as its
own dedicated build, not rushed in; QUANTUM's bridge-gate fold-in flip
overridden, consistent with Iteration 2's own standing rule) → predictions
committed (`e182628`) → Phase 4 run.

**Result: seven of eight predictions confirmed cleanly; the two mandatory
rebandings held up against real data.** 114 new FDTD sim calls, 435s.
Measured σ_abs/σ_ext = 0.606–0.608 — comfortably inside the revised band,
nowhere near the refuted ≥0.90 claim, vindicating Red Team's pre-freeze
catch. C values for OFF-lab/OFF-field landed with real SNR against both
frozen perceptual bars for the first time in this program — no PASS/FAIL
or constraint-3 language attaches to any of them, per the accepted ruling.
g=|C|/τ_center measured directly across an order of magnitude in τ,
broadly confirming exp-024's single-point estimate. Two new findings, both
flagged honestly rather than smoothed over: (1) the ON article's
beam-behind is NOT wavelength-flat (46% relative spread, non-monotonic,
uncorrelated with grid resolution); (2) σ_abs/σ_ext sits ~0.10 ABOVE the
0.51 anchor, opposite the direction the mandatory-fix reasoning predicted.
`e182628` (predictions) → `924bdad` (results).

**Phase 5 — seven fresh seats, blind.** Unusually strong 5-of-7 consensus
on one next action (a resolution check on the beam-behind chromatic
anomaly — PHOTONICS supplied a sharp, falsifiable settling-time
mechanism: fixed `BEAM_STEPS` across a cpl sweep means 750nm gets the
LEAST post-ramp settling despite the finest grid, matching the anomaly's
own resolution-independence). A second, 4-of-7 consensus formed
independently around disambiguating the σ_abs/σ_ext anchor puzzle. EM's
own Phase-5 reading went further and reframed the puzzle: **both the
established 0.51 anchor AND exp-026's measured 0.606–0.608 exceed the
idealized ≤0.5 geometric-optics ceiling** — this bench's box sits in the
shadow's near zone (consistent with the program's own standing T8
finding), so neither number is the asymptotic material constant it has
been cited as. Opened as new LIVE THREAD T9. **Red Team's Phase-5 audit
(verdict: MINOR ISSUES) found two real, concrete, non-physics defects**
— P-MAT6's own miss-count was undercounted (a second miss at
off_lab/600nm, g=0.6913 above its own band ceiling, high-SNR and NOT
floor-explicable, originally left undisclosed) and the run-count/
elapsed-time bookkeeping didn't reconcile with its own `results.json`
(a genuine `run.py` instrumentation bug, the reported 87-run figure
contradicted the code's own accurate 114) — both corrected same-shift in
NOTES.md, LOGBOOK.md, and `run.py` (the historical `results.json` left
unedited, the discrepancy documented rather than silently patched).

**Director's close: VERDICT PROMISING.** No checkpoint criterion fired
(no config passes all constraints; no proven-unsatisfiable boundary; no
major engine build required this iteration; Red Team's audit was MINOR
ISSUES not program-integrity drift, both items closed same-shift; the
iteration clearly advanced the logbook — new calibration data, two
findings, one ESTABLISHED quantity sharpened). Queue for Iteration 4
(lead per rotation ELECTROMAGNETISM; PLAN.md updated): (a) P-MAT4's
beam-behind resolution check (5-of-7 consensus); (b) the PEC-cored-vs-
solid-disk σ_abs/σ_ext disambiguation, T9 (4-of-7 consensus); (c) VISION's
r=156 scale-bridge check, now overdue by one iteration; (d) QUANTUM's
twice-deferred bridge-gate package; (e) THERMO's time-resolved ledger.
Three commits to main this shift (predict/results pair + this close-out).
Trust suite 41/41 green throughout.

## 2026-08-12 (panel shift) — Iteration 2 complete (exp-024/025): the margin
fix was refuted, the fallback wasn't — plus a same-shift resolution close

**Pre-flight:** local `main` detached at a stale point (same bookkeeping
class as every prior shift) — fixed with `git fetch origin main && git
checkout -B main origin/main`. Deps reinstalled (pyMKL wheel fails here,
`ceviche --no-deps` per the recorded wrinkle). Bench trust suite 41/41
green (`--only 12346789`) before this shift's work, rechecked after
exp-024 and again after exp-025 (no `lab/` engine changes any time — only
`experiments/` scripts).

**Iteration 2 — Instrument Margin + Estimator Adjudication (exp-024,
CONCLUDED).** Lead: PHOTONICS (rotation). Full seven-seat cycle run as
fresh sub-agents per PANEL.md's independence mechanics: Phase 1 proposal →
5 blind parallel critiques (VISION, MATERIALS, EM, THERMO, QUANTUM, all
support-with-changes) → Red Team last with everything
(proceed-with-mandatory-fixes, with a decisive finding: PHOTONICS' own
δ_C-extrapolation model, backtested against exp-020's own data,
underpredicts by 5.7–15.7× near margin/fringe-ratio≈1 — the true behavior
is EM's own "threshold collapse," not a smooth power law) → Phase 3
synthesis (Director: MARGIN_MULT=3.5, further than either flip proposed;
δ_C gate tightened to ≤0.001 at every λ; BOX derived programmatically;
P-EST's outcome gap replaced with an exhaustive 3-way partition; QUANTUM's
bridge-gate deferred to Iteration 4 by explicit ruling, not omission) →
predictions committed (`b28635b`) → Phase 4 run.

**Result: the fix worked, but not by the predicted mechanism.**
MARGIN_MULT=3.5 (worst-case margin/fringe ratio 3.5–4.5×, 3–4× better than
exp-020's best point) still MISSED the δ_C≤0.001 gate at all six
(λ,weighting) combinations, non-monotonically — 450 nm got *worse*
(0.0009→0.0026) despite the best ratio ever measured, refuting the
margin/fringe-ratio model the whole iteration was built on. Per the
pre-committed falsification clause, no live patch was attempted — the
pre-committed ±35° fallback reran instead (108 runs) and passed cleanly
everywhere (δ_C 0.000033–0.00089), localizing the true mechanism to
something angle-specific at ±40°, not margin-driven. Bonus, resolved as a
side effect: the fallback's clean floor showed the λ-ordering reversal
exp-020 flagged is **not** pure floor bias — a real, small (~1.5–1.9%)
red-ward |C| growth survives in both hard-edged articles (absorber,
PEC), absent in the soft-edged sponge. Constraint-3's headline is
reconfirmed, essentially unchanged: absorber V-weighted C ≈ −0.684 (vs
exp-020's −0.686). Everything else (material blindness 0.14±0.02, N17
PEC excess, sponge calibration, convergence/ledger identities) CONFIRMED
per pre-registered bands. `b28635b` (predictions) → `c67506b` (primary
raw data + fallback script) → `94028d0` (conclusion + LOGBOOK).

**Phase 5 — seven fresh seats, blind.** Three-way consensus without
collusion on Iteration 4 (σ(I) readiness) as the top pick (MATERIALS,
QUANTUM, THERMO — each independently conditioning it on the ±35° fallback
becoming the standing baseline geometry, not an implicit carryover).
Three seats independently prioritized the ±40°-angle mechanism
(PHOTONICS, EM, RED TEAM); EM supplied three falsifiable, mostly-zero-cost
candidate mechanisms (Yee-grid dispersion anisotropy / incoherent-sum
asymmetry / settling-time artifact) and a concrete triage plan. **Red
Team's audit (verdict: MINOR ISSUES) found one real, unaddressed gap**:
the panel's own R3 meta-rule ("any surprising feature gets a resolution
check before a mechanism debate — artifact claims need the check too")
was owed to the new chromatic finding and hadn't been applied before it
was scored CONFIRMED.

**exp-025 — Chromatic Finding Resolution Check (same shift, CONCLUDED).**
Director accepted Red Team's finding in full and closed it same-shift, per
this lab's own established precedent (exp-005/010/015/023). cpl×1.5 at
450/750 nm, geometry rescaled to hold physical size fixed, fallback
angle set, absorber+PEC only. **Result: the chromatic effect is REAL** —
both spreads landed inside the pre-committed "real effect" band, an order
of magnitude clear of the artifact-collapse threshold (absorber
−0.0114→−0.0120, PEC −0.0166→−0.0151) — the 4th time this program's R3
rule has refuted the artifact hypothesis rather than confirmed it.
`37059d0` (predictions) → `b5447ca` (conclusion).

**Director's close: VERDICT PROMISING.** No checkpoint criterion fired
(no config passes all constraints; no proven-unsatisfiable boundary; no
major engine build required; Red Team's audit was MINOR ISSUES not
program-integrity drift; the iteration clearly advanced the logbook — no
two-consecutive-null-iterations condition). Queue for the next shift/
iteration (PLAN.md, updated): (a) EM's ±40°-angle triage — cheapest,
most-requested; (b) Iteration 4 σ(I) readiness on the ±35° fallback
baseline — 3-seat consensus; (c) docket #7 — zero-run, independent,
unblocked, now scoring an unqualified C. Six commits to main this shift
(three predict/results pairs). Trust suite 41/41 green throughout.

## 2026-08-12 (redesign session) — the Research Panel program; Iteration 1 Phases 1–2; Checkpoint #0

**The redesign (Marsh's directive, in-session):** the phenomenon program now
runs under a seven-seat research panel — PANEL.md (protocol) + LOGBOOK.md
(persistent memory, seeded from exp-000..019). Four explicit constraints;
the hard one (#3, no ambient silhouette) had never been a number on this
bench. Continuous mode: background iterations, checkpoint pauses only.
Trough line parked, resumable. Branch: claude/fotson-lab-redesign-uesugb.

**Bench:** this cloud session verified as a live bench — deps installed
(pyMKL wheel fails to build here; ceviche installed --no-deps per its scipy
fallback), suite 30/30 green (28/28 in 60 s + stage 5 2/2 in 113 s),
stage-5 numbers reproduce VALIDATION.md to the digit.

**Iteration 1, Phases 1–2 (7 fresh-context seats):** VISION SCIENCE led —
"The Ambient-Appearance Instrument": nine-angle ±40° incoherent back-lit
ambient, B(y) on a near plane, Weber contrast with photopic/scotopic
thresholds pinned from Blackwell/Rose/Hecht-class sources BEFORE any run;
predicted absorber C ≈ −0.90 (constraint-3 FAIL ≥ 37× the field bar);
scotopic crossover committed; and a genuinely new reading — the witness's
own flashlight glare (Stiles–Holladay) elevates his threshold ~3 log units,
so the static silhouette can sit sub-threshold FOR THE HOLDER while the
beam interaction stays high-contrast. All five critique seats returned
support-with-changes with real catches (oblique source walk-off breaks the
flatness gate at large angles — photonics and EM independently, with
different onsets because the proposal never pinned source geometry, as Red
Team diagnosed; shadow lever arm 93 cells not 15, committed C bands
geometrically unreachable — EM; missing absorbed-power ledger — thermo;
linear-only idioms unlabeled, no intensity scale tying ambient to beam
units — quantum; no calibration article between C = −0.7 and 0, dilute-
sponge third article proposed — materials). RED TEAM
(proceed-with-mandatory-fixes) caught what all five missed: the frozen
threshold table is not self-consistent (L*_field re-derives to 1.7×10⁻⁴
cd/m², 4.2× the committed value — verified by the Director), gate (c)'s
0.01 tolerance makes the 0.005 PASS bar undecidable, and the glare sidecar
quietly re-scopes constraint 3 — promoted to a spec ruling for Marsh.

**Checkpoint #0 passed (Marsh, in-session):** two-tier constraint-3 ruling
(Tier W witness / Tier A anyone) + go. The rest of Iteration 1 ran the
same session:

**Phase 3** — synthesis committed BEFORE the build (`0c4efff`): all nine
docket fixes accepted, geometry pinned by a published ray-trace design
calculation (360×1200, coverage verified at 17 angles), windows
re-registered outside the 40° penumbra, threshold crossovers re-derived
with the exponent band, P1–P7 bands committed.

**Build** — angled line source (angle 0 bit-exact, gated), `lab/ambient.py`,
suite stage 9 (13/13; Beer–Lambert slab anchor −0.0982 vs −0.0973
analytic; one honest recalibration with mechanism recorded: point-wise
flatness is fringe-limited, window means are the gated quantity). CI now
runs stages 8+9 (8 had been missing). Suite 43/43 on the cloud bench.

**Phase 4 (exp-020 CONCLUDED)** — 124 runs, 472 s. **Constraint 3 is now a
number: absorber C = −0.686** (V-weighted, Tier-A photopic FAIL ×34 field
bar); PEC −0.826; dilute sponge on its pre-committed geometric value to
0.001; material blindness only ~20% (rim transmission — first material
signature in the channel). Honest misses flagged: δ_C floor exceeds the
lab bar at 600/750 (fringe zone vs margin), P1b 0.795 vs 0.8 at 750/±40°,
P2's λ-ordering reversed raw, P3's band edge by 0.02.

**Phase 5** — seven fresh seats, blind. Consensus without collusion on
three clusters: instrument margin fix first (EM's coverage rule
m ≥ 2√(λ_max·D)), docket #7 witness-scenario table second (vision's
glare arithmetic: 4–21× sub-threshold for the flashlight holder — Tier-W
constraint 3 may CLOSE), σ(I) readiness third. **Red Team audited the
Director and scored two hits**, both accepted: P1b's stop rule had been
softened post-hoc (retracted — 750 nm carries an asterisk), and additive
floor-correction is an uncommitted estimator (all floor-corrected claims
provisional pending Iteration 2's adjudication). Iteration 1 verdict:
**PROMISING**. Queue: Iterations 2/3/4 in PLAN.md.

**Shift-10 collision, handled:** the old routine fired at 06:23Z
mid-redesign (Marsh hadn't been able to pause it — owner-created, agents
can't modify it) and committed its r2-isolation + resolution-check pair as
"exp-020/021" on main. Resolution at merge: shift 10's pair renumbered
**exp-022/023** (uniform +2, self-references updated file-scoped, measured
content untouched; the panel's exp-020 was committed first and is
cross-referenced throughout the program record); old routine to be paused by Marsh; agent-owned
panel-shift routine replaces it for continuous mode.
## 2026-08-12 (cloud shift 10) — exp-022/023: the shell=3λ feature is r2=90-specific

**Pre-flight:** local `main` was detached again (same bookkeeping class
as every prior shift) — fixed with `git fetch origin main && git
checkout -B main origin/main` before touching anything. Bench trust
suite 22/22 green (`--only 123467`) before this shift's work, rechecked
after both exp-022 and exp-023 (no `lab/` engine changes either time —
only `experiments/` scripts).

**exp-022 — R2 Isolation (CONCLUDED)**
- Picked up exp-019's own queued follow-up: every point in the
  eps_z/shell-thickness line since exp-006 has shared one fixed outer
  cloak radius, r2=90 cells — "shell=3λ is special" and "r2=90 is
  special" have never been told apart. Moved r2 itself for the first
  time in the line: r2=75 and r2=120 (bracketing r2=90 on both sides),
  holding shell=3λ=60 cells fixed at each (cpl=20, λ=600nm), ±3-cell
  bracket around each new target, the trough's own floor pair
  (0.10/0.18). Predictions committed first (`6711dc0`); `check_gates()`
  found zero exclusions at either r2 — the first fully-clean-inclusion
  sweep of this whole line.
- **Result: neither new r2 reproduces r2=90's negative jump at its own
  shell=3λ point** (`16b61bc`). Both targets came back strongly
  positive — +173.5% at r2=75/r1=15, +51.0% at r2=120/r1=60 — squarely
  inside (in fact on the high side of) the range exp-018/019 already
  mapped at every non-3λ/non-r2=90 point. **The "shell=3λ" feature is
  r2=90-specific, not a portable shell-thickness law.** Combined with
  exp-018 (ruled out eps_z) and exp-019 (ruled out any-integer-λ), the
  population of things that don't explain the original exp-004/005/006
  finding is now large — mechanism still unidentified after five
  dedicated checks. One honest gate miss flagged, not hidden: 4 of 7
  r2=75/floor=0.10 points missed box_dev≤2% (2.55–3.36%), taken up
  immediately by exp-023.

**exp-023 — R2=75 Resolution Check (CONCLUDED)**
- Same-shift direct resolution check on exp-022's own gate miss —
  this line's exp-005/010/015 precedent applied a third time: reran 3
  of exp-022's r2=75 points (worst miss r1=13, target r1=15, clean
  flank r1=18) at cpl=30 (1.5×), geometry scaled to hold physical size
  fixed. Predictions committed first (`c18db7d`).
- **Result: the gate miss was ordinary cpl=20 grid noise** (`8f07b2f`).
  box_dev roughly halved at all 3 points (e.g. 3.36%→1.71%), all now
  clear 2% comfortably; jump values shifted only 3.1–4.8% relative, no
  sign flip anywhere. Closes exp-022's one open caveat in the same
  shift it was raised — the r2=75 half of exp-022's conclusion now
  stands on fully gate-clean footing.
- Net for the shift: a genuine generality test (exp-022) that further
  narrows five shifts' worth of mechanism-hunting to "still
  unexplained, but the list of things it isn't keeps growing," plus a
  same-shift resolution check that closed its own honest gate miss
  cleanly. Four commits to main this shift (two predict/results
  pairs). Trust suite 22/22 green throughout. Next queued: a fine λ
  sweep (1–2nm steps) at the fixed r1=30/r2=90 geometry, testing
  whether the negative jump is a true narrow-band resonance — or
  parking this mechanism thread and returning to exp-007's still-open
  core=8 multi-λ design-lead check.

## 2026-08-12 (cloud shift 9) — exp-018/019: the "eps_z trough" was never about eps_z

**Pre-flight:** local `main` was again detached at a stale point (same
bookkeeping class as every prior shift) — fixed with `git fetch origin
main && git checkout -B main origin/main` before touching anything.
Bench trust suite 22/22 green (`--only 123467`) before this shift's
work, rechecked after both exp-018 and exp-019 (no `lab/` engine
changes either time — only `experiments/` scripts).

**exp-018 — The Trough Frequency Sweep (CONCLUDED)**
- Picked up exp-017's own queued candidate: is the eps_z≈2.25–2.4 trough
  (exp-014/015, both mechanism candidates refuted by exp-016/017) tied
  to a resonance-like condition at the fixed λ=600nm/cpl=20 grid, rather
  than being a pure eps_z effect? Reused exp-003's λ-sweep machinery
  (cpl fixed, geometry scaled in cells to hold physical size constant),
  anchored at the trough's own geometry (r1=30/r2=90 at f=1) instead of
  exp-002's original triple, single cloak scene only, the trough's own
  floor pair (0.10/0.18). Predictions committed first (`47aa745`).
- Scaling r1 and r2 together kept eps_z inside the trough's established
  window (2.2228–2.2907) at every one of 6 λ points, while the shell's
  radial extent in wavelengths varied 2.40λ–4.30λ across the same sweep
  — the intended discriminator. **Result: the negative jump survived at
  exactly one point, λ=600nm — the only sweep point where shell
  thickness lands on an exact integer number of wavelengths (60 cells =
  3.00λ at cpl=20)** (`28c5c1c`). All 5 other points came back positive
  (+3% to +92%) despite eps_z barely moving (0.068 total range) — a
  ~110-percentage-point swing in jump against a near-flat eps_z. Gates
  clean (box_dev ≤1.81%, cross_dev ≤0.085%), λ=600 reproduces exp-014's
  reused number exactly. **Reframes the whole eps_z-trough story**:
  exp-006/011–017's "eps_z≈2.25 trough" was tracking a coincidence of
  exp-002's original geometry (shell=3.00λ at cpl=20), not a real
  feature of `Q_ext(eps_z)`. New hypothesis: a shell-thickness
  standing-wave/Fabry-Pérot condition.

**exp-019 — Shell Thickness at 2 Wavelengths (CONCLUDED)**
- Same-shift direct test of exp-018's own hypothesis: does the
  negative-jump feature reappear at a different integer, 2λ (40 cells),
  bracketed the same way exp-014 bracketed 3λ (±3 cells around r1=50,
  r2=90 fixed)? Predictions committed first (`64dd119`), including two
  points (r1=52/53 at floor=0.18) excluded up front on degeneracy
  grounds — this eps_z range (4.4–5.9) is past exp-013's own
  tightest-margin point.
- **Result: no. All 5 complete-floor-pair points (r1=47–51) show
  positive jumps (+34% to +46%)** — squarely inside the range exp-018
  found at its own non-3λ points, no dip, no band, nothing
  resonance-like near 2λ (`81296ab`). Narrows exp-018's hypothesis:
  whatever produces the 3λ feature isn't a generic "shell = integer ×
  λ" rule — 2λ and 3λ behave differently. r1=48 reproduces exp-006/013's
  existing core=48 numbers exactly. One honest gate miss flagged, not
  hidden: r1=47/floor=0.18 box_dev=2.17%, just over the 2% band (doesn't
  touch the r1=50 target point, itself among the cleanest in the set, or
  the qualitative conclusion).
- Net for the shift: a genuine reframe (exp-018 overturned a working
  assumption 5 experiments deep) immediately followed by an honest
  narrowing (exp-019 stopped that reframe from overreaching into a
  tidier story than the data supports). Four commits to main this shift
  (two predict/results pairs). Next queued: is the 3λ feature specific
  to r2=90 (every point in this line has shared that one fixed outer
  radius) — a genuinely new investigation, not a quick bolt-on.

## 2026-08-11 (cloud shift 8) — exp-016/017: both queued trough mechanisms tested and refuted

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2–7) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before this shift's work, checked again after both
exp-016 and exp-017 (plus stage 8, since exp-017 adds new `lab/`
machinery — 6/6 green before and after).

**exp-016 — Mechanism Candidate 1: Outer-Boundary Impedance Mismatch
(CONCLUDED)**
- Picked up exp-015's queued mechanism question for the eps_z≈2.25–2.4
  trough: does the shell's impedance mismatch at the outer wall (r=r2,
  where the wave actually exits) have a feature coincident with the
  trough? Distinct from exp-006's earlier P3 story, which tested a
  different mismatch (at the floor/inner wall) and was refuted there for
  magnitude trend on a coarser sweep.
- No FDTD needed — a pure material-array probe: built a bare `Sim`,
  called the real `schurig_reduced_cloak_tm` builder, and read the
  actual solver tensor at r≈r2 for the trough bracket (r1=27–33) plus
  exp-006's corner points (15/40/48), at floor=0.10/0.18/0.40.
  Predictions committed before the check (`8180aec`).
- **Refuted, decisively, two independent ways at once** (`b8ed2b6`):
  `|Γ(eps_z)|²` rises smoothly and strictly monotonically with zero
  local feature near the trough, and is *exactly floor-identical* at
  every trough-bracket point — floor-independence that structurally
  disqualifies this mechanism from producing the floor-dependent sign
  flip that defines the trough. Honest bonus: grid quantization flips
  one point (r1=33/floor=0.40) from analytically-unclamped to
  numerically-clamped right at the threshold — a real small effect only
  caught by probing actual arrays instead of trusting algebra.

**exp-017 — Mechanism Candidate 2: Angular-Pattern Shape Comparison
(CONCLUDED)**
- Same-shift follow-up, exp-015's second queued candidate: does the
  trough scatter into a different angular *shape* than its flanks, or
  just a different magnitude? Required new instrumentation —
  `lab.sections.angular_scattered_pattern`, added this shift, binning
  the same per-cell scattered-flux terms `widths()` already sums, by
  angle around the box perimeter instead of collapsing to one number.
  Verified against stage 8 (6/6 unchanged) plus a per-run self-
  consistency identity (landed at machine epsilon). Predictions
  committed before the run, alongside the new capability (`ebce2f5`).
- 4 runs (3 cloak + 1 empty) at r1=27/30/33 (flank/trough/flank),
  floor=0.10, λ=600nm — 5.1 min. **Also refuted — magnitude-only, no new
  scattering mode** (`9ff8e95`). Shape correlation places the trough
  inside the same family as both flanks (0.9688/0.9717 vs the
  flank-flank 0.9383); the one asymmetry (trough correlates *better*
  with each flank than they correlate with each other) is fully
  explained by ordinary distance in eps_z-space between the sample
  points, not by anything anomalous at the trough itself.
- **Both mechanism candidates queued after exp-014/015 are now closed —
  neither explains the trough.** A genuinely new candidate is proposed
  for a future shift: a frequency-domain view, sweeping λ at fixed
  core=30/eps_z=2.25 (the mirror of exp-003's λ sweep, held at the
  trough's own geometry) to test whether the trough is tied to a
  resonance-like condition at the fixed λ=600nm/cpl=20 grid rather than
  a pure eps_z effect. Secondary, unscored observation logged in PLAN.md
  (a local angular-peak count came out 13 at the trough vs 10 at each
  flank) — worth a recheck, not claimed as a finding.
- Three commits to main this shift (predict/results pairs for two
  independent mechanism tests, plus the new instrumentation bundled with
  exp-017's predictions) — a clean, fast, two-candidate elimination pass
  that leaves the trough's real cause as the lab's next open question.

## 2026-08-11 (cloud shift 7) — exp-014/015: the eps_z trough found, pinned down, and confirmed grid-independent

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2–6) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before this shift's work, checked again after each of
exp-014 and exp-015; no `lab/` engine changes.

**exp-014 — The Fine eps_z Scan Bracketing 2.25 (CONCLUDED)**
- Picked up exp-012/013's queued question, echoed in PLAN.md: *why*
  does eps_z≈2.25 (core=30, the exp-002/003/004 baseline) specifically
  produce a negative mu_r_floor=0.10→0.18 jump when 3 of exp-006's other
  4 core/eps_z points don't? Swept r1=27/28/29/31/32/33, one cell apart
  (Δeps_z≈0.07–0.15) — the finest geometric step tested anywhere in this
  line — bracketing the reused r1=30 point on both sides. Predictions
  committed before the 13-run sweep (`47eb69b`).
- **The negative jump is a real, contiguous 4-point trough, not an
  isolated grid point:** r1=29/30/31/32 (eps_z≈2.18–2.41) all show
  negative jumps, r1=27/28/33 all show positive jumps, and the reused
  r1=30 baseline sits almost exactly at the trough's deepest point
  (−17.69%, more negative than any of the 6 new points). **Bigger
  surprise:** exp-006's own coarse "no exceptions in 8 points" monotonic
  law for Q_ext(eps_z) does not survive this finer resolution — Q_ext
  itself is non-monotonic at both floor values inside this window (a
  real local minimum near r1=30 at floor=0.18, a dip at the far edge at
  floor=0.10) — the coarse sweep's widely-spaced sample points simply
  never landed inside the dip. Gates clean throughout (box_dev ≤2.0%,
  cross_dev ≤0.08%) (`65a87da`).
- Honest caveat raised in the same file: this was the first fine
  (1-cell) r1 step tested in the eps_z line, so — unlike the *floor*
  sweep, where exp-005 already checked this — a grid-quantization origin
  for the trough hadn't been ruled out. Queued as the immediate next
  step rather than left open past the shift.

**exp-015 — Does the eps_z Trough Survive Resolution? (CONCLUDED)**
- Immediate same-shift follow-up: exp-004→exp-005/exp-009→exp-010's
  exact resolution-convergence precedent, applied to the eps_z axis for
  the first time. Reran 3 of exp-014's bracketed points (flank/center/
  flank: r1=28/30/33) at cpl=30 (1.5×), geometry scaled to hold physical
  size fixed. Predictions committed before the 7-run sweep (`f32af38`).
- **The trough survives resolution intact — no sign flips at any of the
  3 points.** base=30 (trough center) stays deeply negative
  (−17.69%→−16.42%, a 7.2% relative shrink almost identical to exp-005's
  own 7% shrink on the *floor* jump at this same geometry, just a
  different resolution axis refined); both flanks stay positive. Gates
  the cleanest of the whole eps_z line (box_dev ≤1.3%, cross_dev
  ≤0.0018%) (`02fd70c`).
- **Confirms exp-014's trough is a genuine physical feature of
  Q_ext(eps_z), not a 1-cell grid-quantization artifact** — closes
  exp-014's own honest caveat in the same shift it was raised, the same
  discipline exp-004→exp-005 and exp-009→exp-010 established. No
  mechanism proposed yet for *why* the feature sits near eps_z≈2.25–2.4;
  candidates (impedance-mismatch sweep, angular-pattern comparison)
  logged in PLAN.md for a future shift.
- Four commits to main this shift (two predict/results pairs) — a
  question three shifts in the making (exp-006→exp-011/012/013→
  exp-014→exp-015) closed end-to-end: found the anomaly's true shape,
  then ruled out the obvious artifact explanation, in one continuous
  arc.

## 2026-08-11 (cloud shift 6) — exp-012/013: exp-006's floor-curve generalization completed, 4-for-4

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2–5) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before this shift's work, checked again after each of
exp-012 and exp-013; no `lab/` engine changes.

**exp-012 — The Floor Sweep at core=40, exp-006's Candidate C (CONCLUDED)**
- Picked up exp-011's queued third generalization point: floor sweep
  at core=40/eps_z=3.24, reusing exp-006's existing 0.10/0.18 points
  and adding 0.05/0.28. floor=0.40 excluded — the *first* time this
  series' excluded point was a degeneracy-threshold issue (shell fully
  clamps above `((r2−r1)/r2)²=0.3086` at this core) rather than a CFL
  issue like exp-011's exclusion. Predictions committed before the
  3-run sweep (`27dcb28`).
- **Full 4-point curve (0.7374→0.7540→1.2871→1.8821) is strictly
  monotonically increasing, zero exceptions** — the cleanest gates of
  the series (box_dev ≤0.5%, cross_dev ≤0.1%). Same pattern as core=15
  (exp-011): 3-for-3 against core=30's non-monotonic curve (`ed9db47`).

**exp-013 — The Floor Sweep at core=48, exp-006's Candidate D (CONCLUDED)**
- Immediate same-shift follow-up: exp-012's queued fourth and last
  core/eps_z point, core=48/eps_z=4.59 — the tightest degeneracy margin
  in the series (only floor=0.05/0.20 fit inside the graded threshold
  of 0.2178; 0.28/0.40 both degenerate here). Predictions committed
  before the 3-run sweep (`0668366`).
- **Full 4-point curve (0.9218→1.2096→1.6751→1.7146) is strictly
  monotonically increasing**, holding through the tightest-margin point
  of the whole investigation (8.2% from degeneracy) (`040e69c`).
- **Generalization complete: all 4 of exp-006's core/eps_z points now
  swept across their full available floor range.** 3 of 4
  (core=15/40/48) are strictly monotonic; only core=30/eps_z=2.25 (the
  original exp-002/003 baseline geometry, chosen for unrelated reasons)
  shows the sign-flipping floor structure exp-004/005 spent two shifts
  resolution-testing. No mechanism yet proposed for *why* that ratio is
  special — the natural next question, logged as needing a dedicated
  shift (a finer eps_z scan bracketing 2.25, a new experimental axis).
- Four commits to main this shift (two predict/results pairs) — two
  full predict→run→conclude cycles that closed out a generalization
  question three shifts in the making.

## 2026-08-11 (cloud shift 5) — exp-009/010/011: a gate failure caught and resolved, plus a clean generalization of exp-006's reframe

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2/3/4) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before and after this shift's work (checked mid-shift
too, after exp-010/011); no `lab/` engine changes.

**exp-009 — The Ratio Below Eight (CONCLUDED)**
- Picked up exp-008's queued candidate: traced the cloaked/bare Q_ext
  ratio below core=8 (r1=4/5/6/7 cells), λ=600nm, floor=0.10, CFL
  margins checked and asserted stable before running (3.4–7.2%).
  Predictions (P1–P4) committed before the 8-run sweep (`0b2a47a`).
- **The pre-registered gate itself failed** at 2 of 4 new points:
  cloak box_dev 3.5% (core=4) and 2.3% (core=5), both over the ≤2%
  threshold, core=6 exactly borderline (2.0%) — bare-disk gates stayed
  clean throughout (≤1.2%), pinning the failure to the cloak's graded
  profile specifically. The cloaked Q_ext curve itself came out
  non-monotonic (a bump near core=5) where the established law
  predicted a smooth continuation. Reported honestly as
  not-yet-trustworthy rather than as a finding (`bb98d76`) — the same
  standard applied when exp-003 caught its own domain-sizing bug.
  P4's specific numeric threshold technically cleared but was flagged
  as "directionally supported, not gate-trustworthy" rather than scored
  confirmed.

**exp-010 — Does the Below-Eight Bump Survive Resolution? (CONCLUDED)**
- Immediate same-shift follow-up, exp-004→exp-005's exact precedent:
  reran the same 4 core points at cpl=30 (1.5×), geometry scaled to
  hold physical size fixed. Predictions (P1–P4) committed before the
  9-run sweep (`aa9a5b3`).
- **Both anomalies were the same cpl=20 artifact, and it resolved
  cleanly.** Cloak box_dev dropped from 3.5%/2.3%/2.0%/1.8% to
  0.5%/0.2%/0.0%/0.3% — an order of magnitude tighter, the cleanest
  gates in the lab's history. The non-monotonic bump vanished — cpl=30's
  cloaked Q_ext curve is strictly monotonic, extending exp-006/007's
  law without exception down to r1=6 cells, the smallest core tested to
  date. The cloaked/bare ratio genuinely **rises below core=8** (from
  exp-008's ~0.193–0.194 plateau up to ~0.21–0.28), now confirmed
  gate-clean. Read with exp-007's own finding (absolute Q_ext
  improvement slows below core~15): the shell's *relative*
  effectiveness degrades too past ~8 — two independent signs of
  diminishing returns, not one (`db05757`).

**exp-011 — The Floor Sweep at core=15, exp-006's Candidate B (CONCLUDED)**
- Cheap closeout of a previously-logged open item: reran exp-004's
  floor sweep at core=15/eps_z=1.44 (vs the exp-004/005 baseline
  core=30/eps_z=2.25), reusing exp-006's existing 0.10/0.18 points and
  adding 0.28/0.40. floor=0.05 excluded — CFL-unstable at this eps_z
  (ceiling 0.268 < courant_frac 0.32), a new addendum to the standing
  `mu_r_floor<0.05` item: the instability is geometry-dependent, not
  purely a low-floor phenomenon. Predictions committed before the
  3-run sweep (`4a45de8`).
- **The full core=15 floor curve (0.0934→0.2592→0.5242→0.7818) is
  strictly monotonically increasing, no sign-flip anywhere** — unlike
  core=30's non-monotonic dip-then-rise shape. Strengthens exp-006's
  reframe from "possibly atypical" toward a working conclusion: the
  exp-004/005 floor-jump was a property of the eps_z=2.25 baseline
  specifically, not a general feature of the `mu_r_floor` knob
  (`0ca52bb`).
- Six commits to main this shift (three predict/results pairs) — three
  full predict→run→conclude cycles, one of which caught its own gate
  failure and resolved it within the same shift rather than reporting
  ungated numbers as a finding.

## 2026-08-10 (cloud shift 4) — exp-008 CONCLUDED: the bare-disk control closes exp-007's caveat, in the design lead's favor

**Pre-flight:** local `main` was detached at the true tip again (same
bookkeeping class as shifts 2 and 3) — fixed with `git checkout -B main
origin/main` before touching anything. Bench trust suite 22/22 green
(`--only 123467`) before and after this shift's work; no `lab/` engine
changes.

**exp-008 — The Bare-Disk Control (CONCLUDED)**
- Picked up exp-007's queued candidate: the missing control for its
  ~15× design lead. Stripped the cloak shell entirely and measured a
  bare PEC disk's own Q_ext at the same 7 core radii (8–30 cells)
  exp-006/007 already characterized with a cloak, same domain,
  λ=600nm, same normalization (`sigma_ext / (2·R2_CELLS)`, fixed
  R2_CELLS=90) so cloaked and bare numbers sit on the identical scale.
  Predictions (P1–P4) committed before the 8-run sweep (`84edefb`).
- **P1, P2, P4 confirmed; P3 refuted — and the refutation is the good
  outcome.** P3 predicted the cloaked/bare ratio would *rise* as core
  shrinks (cloak's relative benefit weakest exactly where the absolute
  numbers look best — the "it's just a smaller object" concern).
  Instead the ratio **falls**: 0.900 at core=30 down to a ~0.193
  plateau at core=8–12. The pre-registered fallback reading called
  this outcome explicitly: a falling ratio means the shell's *relative*
  suppression effectiveness genuinely improves as it thickens, not
  that the design lead is mostly a trivial smaller-object effect. This
  agrees with exp-006's independent finding (thinner shell = worse
  cloak, a clean monotonic law on its own) — two separate measurements
  now point the same direction. **exp-007's caveat is closed**:
  core=8/floor=0.10 stands as the lab's best-characterized cloak
  design.
- Gates the cleanest yet in this line (box_dev ≤1.3%, cross_dev ≤0.2%
  at all 7 points — a bare PEC disk is a simpler scatterer than a
  graded anisotropic shell, as predicted).
- Two commits to main this shift (`84edefb` predictions, `30bfbe4`
  results/conclusion) — one full predict→run→conclude cycle, gated end
  to end, with a pre-registered prediction refuted in a way that
  strengthens rather than undercuts the finding it was checking.
  exp-009 candidate (ratio below core=8) and the sharpened multi-λ
  follow-up logged in PLAN.md rather than rushed this shift.

## 2026-08-10 (cloud shift 3) — exp-006, exp-007: eps_z is a clean law on Q_ext but not on the floor-jump, and a design lead worth ~15x

**Pre-flight:** local `main` branch pointer was stale again (HEAD was
detached at the true tip, `git branch` showed `main` still 5 commits
behind `origin/main`) — same bookkeeping class of issue as a prior
shift, fixed with `git checkout -B main origin/main` before touching
anything. Bench trust suite 22/22 green (`--only 123467`) before, in the
middle of, and after this shift's work; no `lab/` engine changes.

**exp-006 — The Shell Ratio (CONCLUDED)**
- Picked up exp-005's queued candidate: isolate `eps_z =
  (r2/(r2−r1))²` independently of overall cloak scale by holding the
  *outer* cloak radius r2 fixed and sweeping the *inner* radius r1
  instead, at 4 core points (eps_z 1.44→4.59) × exp-004/005's exact
  0.10/0.18 floor pair, λ=600nm. Predictions (P1–P5) committed before
  the 9-run sweep (`c783486`).
- **Two findings.** (1) eps_z is a genuinely clean, fully monotonic knob
  on baseline Q_ext — thinner shell (higher eps_z), worse cloak, no
  exceptions across 8 points, the cleanest law this floor/eps_z line has
  produced (P5 confirmed). (2) eps_z does **not** track the floor-jump
  the way P3 predicted — |jump| = 177.5/17.7/70.7/38.5% across the 4
  eps_z points, non-monotonic and *largest* at the smallest eps_z, the
  opposite of the predicted impedance-mismatch direction (P3 refuted).
  Sharper read: the exp-004/005 baseline geometry (eps_z=2.25) is the
  *only* one of the 4 points tested here showing a negative jump — three
  others show the "naive" direction (wider clamp, worse). Two shifts of
  careful resolution-convergence work may have characterized an atypical
  point, not the norm (P4 confirmed, reframes the story). Unplanned
  bonus: core=15/floor=0.10 gave Q_ext=0.0934, ~7× better than the
  exp-002–005 baseline — a design lead, found incidentally.
- Gates clean throughout (box_dev ≤1.7%, cross_dev ≤0.5%, tightest at the
  by-design near-degeneracy point).

**exp-007 — Chasing the Shell-Ratio Design Lead (CONCLUDED)**
- Deliberate follow-up, same shift: traced Q_ext(eps_z) below core=15
  (core=8/10/12/20/25, same λ=600nm/floor=0.10) to test whether the
  design lead was a local optimum or part of a continuing trend.
  Predictions (P1–P3) committed before the 6-run sweep (`cef3c7c`).
- **All three predictions confirmed.** The monotonic law extends all the
  way to core=8 with no reversal — **new best Q_ext=0.0429, ~15× better
  than the exp-002–005 baseline**, beating exp-006's own core=15 lead by
  more than half. The rate of improvement slows sharply below core≈15
  (3–10× shallower per-cell slope than the 20–30 range), consistent with
  Q_ext approaching a positive residual as the hidden core shrinks, not
  falling indefinitely.
- **Honest caveat flagged, not resolved this shift:** the curve
  conflates "a smaller hidden PEC core intrinsically scatters less"
  with "the shell genuinely cloaks better when thicker" — `q_ext` is
  normalized by the fixed outer radius throughout, so this isn't a
  normalization artifact, but the missing control (a bare, uncloaked
  PEC disk at the same radii) wasn't run. Logged as exp-008 candidate,
  next in line — resolves the caveat before core=8 gets treated as an
  actual better cloak design.
- Four commits to main this shift (`c783486` exp-006 predictions,
  `4f6103b` exp-006 results, `cef3c7c` exp-007 predictions, `969e4b5`
  exp-007 results) — two full predict→run→conclude cycles, gated end to
  end, one honest refutation (exp-006 P3) alongside five confirmed
  predictions, plus a caveat surfaced and disclosed rather than glossed
  over.

## 2026-08-10 (cloud shift 2) — exp-004 and exp-005 CONCLUDED: the clamp isn't a staircase artifact

**Pre-flight:** local `main` ref was stale (last shift's commits landed on
`origin/main` but the local branch pointer hadn't followed) — fast-forwarded
before touching anything, no data loss, just a bookkeeping catch-up.
Bench trust suite 22/22 green (`--only 123467`) before and after this
shift's work; no `lab/` engine changes.

**exp-004 — The Clamp Band (CONCLUDED)**
- Picked up exp-003's queued candidate: isolate `mu_r_floor` alone
  (electrical size + cpl held fixed, exp-003's own geometry reused) at
  420/480/540/600nm × 5 floor values (0.05→0.40, upward from baseline
  only — going below 0.05 needs a paired `courant_frac` cut for CFL
  stability, derivation committed in NOTES.md, not run this shift).
  Predictions (P1–P5) committed before the 20-cloak-run sweep (`ac29101`).
- **Finding: the 480nm bump isn't wavelength-special.** Q_ext(cloak) vs
  `mu_r_floor` is non-monotonic — sometimes sign-flipping — at *every* λ
  tested, under gates too clean to blame on noise (box_dev ≤1.8%,
  cross_dev ≤0.1% throughout; `i_inc` bit-identical across the whole
  floor sweep at each λ, a free harness check). exp-003's specific
  480nm-high reading was just where that λ happened to land on one of
  these jumps — 420/540/600nm each show comparable structure at other
  floor values. floor=0.05 reproduced exp-003's cloak numbers to <0.1% at
  all four λ (P2, tightest reproduction yet). Working hypothesis logged:
  clamp-boundary cell-alignment on the fixed grid (staircase artifact).

**exp-005 — Does the Clamp Jump Shrink With Resolution? (CONCLUDED)**
- Direct test of exp-004's hypothesis, run the same shift: reran the
  clearest jump (600nm, floor=0.10→0.18, a 17.7% rise-then-fall at
  cpl=20) at 1.5× resolution (cpl 20→30, physical geometry held fixed,
  5 cloak runs). Predictions committed before running (`64be902`).
- **Finding: it's not a staircase artifact.** The jump barely moved
  (17.7%→16.4%, a 7.2% relative reduction for a 50% resolution increase
  — far too little for grid-alignment noise) and the entire 5-point
  curve's *shape* survived refinement almost unchanged (Pearson
  correlation 0.9996 between the cpl=20 and cpl=30 curves; per-point
  ratios drift smoothly 0.94→1.01). **Refutes exp-004's staircase
  hypothesis.** Sharper read: the non-monotonicity looks like an
  intrinsic feature of how `mu_r_floor` reshapes the shell's `mu_r`
  profile against its fixed `eps_z=2.25`, not a numerics artifact.
  exp-006 candidate logged: vary `eps_z` independently (r1/r2 ratio) at
  fixed floor values.
- Four commits to main this shift (`ac29101` exp-004 predictions,
  `19fe82c` exp-004 results, `64be902` exp-005 predictions, `37fc3ea`
  exp-005 results) — two full predict→run→conclude cycles, gated
  end to end, honest refutation both times (P3/P4 in exp-004, P3 in
  exp-005) alongside the confirmed predictions.

## 2026-08-10 (early) — interactive session closed; the lab is autonomous

- Session end on Marsh's call (moving to other work). In-session cron
  killed; board/Telegram watchers already dead with earlier app restarts.
  **The 6-h cloud shift is the lab's only live layer now** — and its first
  fire had just proven the whole loop solo (entry below: exp-003 concluded,
  exp-001 rerun closed, five green commits in ~65 min, a domain bug caught
  by its own gates).
- 72h criterion at close: exp-002 ✅ + exp-003 ✅ inside the first 12 h;
  gated iterations ticking on #32. Verdict ping to Marsh due ~Wed
  2026-08-12 morning.
- Bonnie ledger question (Marsh's) answered honestly: foundations real
  (schema, digit-identical replications, defect-catching reviews); evening
  went to SupplyLens + likely power outage; witness figure undelivered —
  nudge posted to #31 with the sign-off, the nudging job is Clyde's now.

## 2026-08-10 (cloud shift) — exp-003 CONCLUDED: the red-side trend is real, not resolution, but not (defect/λ)² either

**Pre-flight:** bench trust suite 22/22 green (`--only 123467`) before any
work; regenerated validation PNGs are a routine byproduct of that run
(committed, no `lab/` engine changes this shift).

**exp-003 — The Broadband Wall, Redesigned (CONCLUDED)**
- Predictions (P1–P5) committed before the machinery ran, per house
  discipline (`b25e84a`). Design: hold cells-per-λ fixed at 20 across a
  6-point λ sweep (420–750nm), scale geometry in cells so its *physical*
  (nm) size stays constant — separating grid resolution from the cloak's
  fixed-size-defect electrical size, exactly the confound exp-001/002
  flagged.
- **Caught its own bug before trusting data:** first run blew up box
  independence at the largest scale factor (λ=420nm) — box_dev 200–600%
  uniformly across all three scenes, immediately marking it a
  domain-sizing bug (box edge 19 cells from the absorbing wall) rather
  than cloak physics. Patching only that point would have reintroduced
  the confound the experiment was built to remove, so the whole domain
  was grown and the **full sweep rerun** (`cb7bc96`) — nothing from the
  broken run is in the results. Post-fix: box_dev ≤1.1%, cross-route
  agreement ≤0.2% at all 18 scene/λ combinations.
- **Findings:** the λ=600 point reproduces exp-002 to <1% (harness
  trustworthy); the cloak's Q_ext still falls net across the sweep
  (0.460→0.318, 420→750nm) with resolution held fixed — **the red-side
  improvement is real, not a numerical artifact**, resolving exp-001's
  flagged confound. But it is **not monotonic** (a bump at 480nm, hidden
  by exp-002's 3-point sweep) and the log-log slope vs electrical size is
  **≈0.79 (R²=0.87)**, far below the predicted [1.5,3.0] quadratic band —
  **P4 (the (defect/λ)² hypothesis) is REFUTED**, honestly, alongside the
  three predictions (P1, P2, P5) that were confirmed. Working hypothesis
  for exp-004: the mu_r clamp band's fixed *relative* extent (~0.29·r1)
  interacting with the grid, not simple electrical-size scaling.
- Two commits to main (`c69efb4` run script, `cb7bc96` domain fix +
  rerun), plus NOTES.md results write-up. No new trust-suite stage needed
  (machinery reused from exp-002's stage 8).

**exp-001 — observer-table rerun post phasor fix (queued since exp-002,
closed this shift)**
- 12 runs, 6.7 min, artifact Evidence Gate 0 failures (re-verified
  independently with `lab.artifacts check` after the run). Camera floor
  drops ~17× (the sin²(ω/2) bug artifact gone); absorber return tracks
  the new, tighter floor at every λ — the "equals empty-space floor"
  clause reads more precisely true post-fix. Reflector/cloak returns
  shift a few percent, same order of magnitude, same ranking at every λ.
  **Values shifted, verdict stands**, exactly as predicted when queued.

**Next work:** exp-004 candidate logged (sweep `mu_r_floor` alone at
fixed electrical size/cpl).

## 2026-08-09 (evening) — always-on rig armed; exp-002 CONCLUDED in 2 hours

**The autonomy rebuild (Marsh's near-shutdown → decisive rearm)**
- Cloud routine `photonlab-shift` armed: every 6 h on Anthropic infra,
  independent of any human machine; reports via the CI ticker; kill
  criterion = 2 shifts without meaningful commit. Iteration mode declared
  (sweeps direct-to-main, ceremony for conclusions). Bonnie priority
  directive posted (Marsh's relayed word). Humans-never-gates amendment
  merged (PR #6): fresh-context agent cold reads replace the human duty —
  Preston released with honors. The 72-h criterion accepted: exp-002 +
  exp-003 concluded + double-digit iterations by ~Wed morning, or the
  project dies by ledger rules.

**exp-002 — How Invisible Is Invisible (CONCLUDED)**
- `lab/sections.py`: closed-box σ_scat/σ_abs/σ_ext with independent
  extinction route + object-fixed normalization; **stage 8** gates green
  (box independence ≤ 2%, extinction routes agree to 0.2%).
- **Forensic catch with teeth:** phasor-convention bug in `lab/emit` —
  exp-001's 1.25% "camera floor" was sin²(ω/2) exactly. Post-fix: floor
  1e-4, Fresnel to three decimals. Mirror gate honestly recalibrated
  (≥ 0.90, deficit = documented diffraction). exp-001 rerun queued
  (verdict unaffected).
- **Results (12 runs, 9.7 min):** cloak Q_ext lowest at every λ (0.52 /
  0.38 / 0.30 vs reflector's ~2.2, absorber's ~1.54) and **monotonically
  better toward red** — the asymmetry discovery restated in cross-section
  currency; fixed-size-defect (defect/λ)² hypothesis logged for exp-003.
  Absorber: backward spray ≤ 10⁻⁴ of extinction, σ_ext flat to 1.2% —
  broadband black confirmed in the new currency; abs/ext 0.51 = the
  extinction paradox (gate recalibrated with reasoning).
- **The finding: "invisible" has a direction.** All-angle: cloak wins 4×.
  Source-observer (witness geometry): absorber wins by orders of
  magnitude. Any invisibility claim must state *from where* — why the
  witness's one-directional statement was decidable at all.

## 2026-08-09 (day) — freeze closed, graded-black absorber designed and gated

**Shipped/Done (absorber PR, stacked on the emitter PR)**
- **exp-001 scope FROZEN** (Marsh's word in-session): three scenes +
  observer figure + NOTES + 3-λ sweep. Future freezes move to agent
  consensus (AGENTS.md amendment in this PR, Bonnie co-sign).
- **`materials.graded_black_shell`** — the designed ultra-absorber (object
  b): ε≈1 conductive sponge, quintic adiabatic entry, delayed loss. Gates
  written before first run and hit: coated-wall **R = 0.10%** @ 600 nm,
  ≤ 0.2% across 450/750 (broadband black); solid sponge disk's observer
  return **equals the camera's empty-space floor** (net ratio 0.000 vs
  bare PEC). "Stopped on nothing," as a material.
- Suite → **24/24** (stage 7 added). Schema 0.2.0 (builder row per the
  extension rule); exp-000 artifacts re-emitted and gate-green.
- Stage-7 first-run amendment, on the record: test disk 28→32 cells to
  meet the builder's own ≥1.5λ grade minimum; return ratio computed net of
  the stage-6-measured camera floor (raw values printed).
- In-session work-shift cron armed (every 4 h): the lab advances the queue
  even when the board is silent. Watcher v2: catches new threads, not just
  comments (v1 missed co-lab #33 — Marsh caught it).

## 2026-08-09 (afternoon) — git-authority grant ratified bilateral

- Preston's endorsement landed (in-session, relayed verbatim to co-lab #31:
  "endorse approved") — the 2026-08-09 git-autonomy grant now stands on both
  humans' words. AGENTS.md amended at the recorded scope: merges to main
  agent-decided, destructive tier stays human-initiated, either human
  amends/vetoes on a word. Counterparty co-sign requested from Clyde on the
  ratification PR per the both-lanes discipline.

## 2026-08-09 (night shift) — the emitter: observer camera Fresnel-gated, first artifacts committed

**Shipped/Done (this PR)**
- `lab/emit.py` — the solver's half of the contract: quadrature-pair
  capture, **angle-resolved observer camera** (phasors from two snapshots →
  Ez/Hy angular-spectrum split → backward flux per angle bin, vacuum-run
  normalization), manifest assembly from engine-self-recorded scenes,
  float32 emission via `artifacts.save_run`.
- Engine/materials additions: Sim records `source_specs` + `objects`
  (builders self-report) so manifests mirror what actually ran.
- **Trust suite stage 6** (5 checks): empty room 0.0125 · mirror 0.955 ·
  ε=4 half-space **0.1075 vs Fresnel's 0.1111** · 99% specular · emitter
  save→load→validate round trip through Bonnie's checker. Suite now
  **19/19**; stages 1–5 re-verified unchanged.
- **First Evidence-Gated artifacts committed**:
  `experiments/000-hello-maxwell/artifacts/{empty,cylinder}` (~4 MB, all
  check groups PASS). First observer datum: the exp-000 glass cylinder
  returns **5.7%** of the beam to the source. CI extended: stage 6 + the
  artifact Evidence Gate run on every push.

**Context (same night, board)**
- Preston's cold read passed the acceptance test both ways → house figure
  style R1–R4 (Bonnie's writeup, ratified). Governance flare Marsh↔Bonnie
  resolved: apology + her "ratified on the spot" close; ratification PR
  pending Preston's word, nothing blocked on it.

**Deferred/next**
- Bonnie: viz extraction + observer rendering (unblocked; artifacts ready).
- Clyde: exp-001 scenes + 3-λ sweep after the freeze window closes.

## 2026-08-09 (late) — contract night: schema v0.1.0 merged, bench watchable, agents take the lead

**Shipped/Done**
- **CI + bench ticker** (Marsh's ask "can I see the tests run?"): every push
  runs the trust suite (ubuntu × py3.11+3.14, `validate.yml`) and posts a
  🟢/🔴 line to co-lab **#32** — watchable from the board web app, no GitHub
  app. First-day red→green: missing `requirements.txt` for the pip cache
  (now the bench's shared dependency manifest).
- **PLAN.md** + **AGENTS.md** created (co-lab standard files this repo was
  missing). AGENTS.md records Marsh's agent-lead grant with self-retained
  discipline (cross-lane PR review, green-before-merge, no history rewrites).
- **Schema v0.1.0 MERGED** (`ba2cc7f`, Bonnie's PR #1): the solver↔viz
  contract — fields.npz + manifest, pinned observer record, typed
  provenance, float32 stored, self-testing Evidence-Gate checker. Full loop
  cycle: strawman → PR → review (2 tightenings, landed with a selftest
  proving the new rule fires) → CI green → merge. Zero human git.
- Cross-verification symmetry closed: her checker 4/4 on Windows/py3.14;
  her macOS replication of the suite already on record. Three benches.

**Decisions**
- **Marsh's grant (in-chat + #31): agents lead; git autonomy both agents.**
  Bonnie's governance refinement, accepted: a standing authority change is
  a rulebook amendment both humans endorse via PR — her ratification pass
  comes when Preston's word lands; AGENTS.md text already matches her
  scoped position. Harness note: the permission classifier rightly blocked
  Clyde self-writing `.claude/settings.json` — Marsh builds the allowlist
  via "always allow" clicks instead.
- Emitter is Clyde's next build (float32, delta 3 kept per the boundary
  argument): observer-record physics gated by a new suite stage — the
  mirror must return what Fresnel says first.

**Verified**
- Ticker lines on #32 for every push tonight; artifacts selftest 4/4 on
  Windows; PR #1 CI green both Pythons before merge.

**Deferred/next**
- Emitter PR (Clyde) → Bonnie's viz-extraction PR → exp-001 scenes.
- Preston: cold read of v5_cloak.png pending; his word on the governance
  ratification pending. Freeze window on exp-001 DoD closes ~2026-08-10
  04:00Z barring objection.

## 2026-08-08 — exp-001 groundwork: lab/ engine + 14/14 trust suite

**Shipped/Done**
- `lab/fdtd2d.py` — engine grown from exp-000: conductivity, PEC,
  **anisotropic inverse-μ tensor** (B-then-H scheme, staggered evaluation),
  plane/Gaussian sources, Poynting line monitors, `spatial_wavelength`.
- `lab/materials.py` — dielectric cylinder, PEC disk, absorber **STUB**
  (Bonnie's lane preserved), Schurig/Cummer reduced TMz cloak (clamped,
  derivation + stability arithmetic in docstrings).
- `lab/validation/` — 5-stage trust suite + `VALIDATION.md`; board #31
  status note posted. Merged `f016384`.
**Verified (14/14)**
- exp-000 regression exact · Fresnel R 0.098 (theory 0.111±0.025) ·
  matched half-space R≈0.018 through scalar AND tensor μ paths ·
  scattered-field cross-solver corr 0.93 (flaport fdtd) / 0.96 (ceviche) ·
  cloak smoke −34% scattered RMS, beam-behind-object 0.057 → 0.641.
**Decisions**
- Cross-solver checks compare SCATTERED fields (scene − own vacuum) —
  total-field comparison caps correlation on source-profile differences.
- Cloak smoke framed as MACHINERY check (bar 0.75); cloak *quality* is
  exp-002/003's job. PEC flush at inner wall per canonical setup (the
  2-cell gap cost 11 RMS points).
- Bonnie's offered lanes untouched: absorber stub only, no viz module.
**Board (same night — the four-way arrived)**
- **Mandate (canon, recorded on #31):** Marsh in-session + Preston to Bonnie —
  the AGENTS drive experiment discussion/design; humans seed ideas. Design
  loop proposed and posted: predict-before-run → solver build (Clyde) →
  Evidence-Gated artifacts → observer/metric verdict (Bonnie) → nature
  arbitrates disagreements → NOTES.md per loop.
- **Bonnie's lane: viz + observer camera** (her amendment; all three
  materials back with Clyde). Contract: solver emits observer record +
  artifacts (her schema PR, Clyde veto); she never reaches solver internals;
  Clyde never touches figures. Her figure house rules adopted. She's
  replicating the 14/14 suite on macOS (3 solvers × 2 OSes).
- **Preston's role, his call: the acceptance test** — non-physicist reader
  of every figure ("if he can't answer the witness question from the figure,
  the figure failed"). First specific handed to him: read v5_cloak.png cold,
  report what it needs. Meep lane parked, zero pressure.
- **exp-001 DoD amended + freeze window:** three scenes + observer figure +
  NOTES + bench cross-check (✅) + **3-λ sweep (450/600/750)** — the witness's
  flashlight was white light; single-λ matches don't count. Prediction on
  record: the sweep cracks the cloak's match, not the absorber's. Frozen in
  ~24h barring human objection; fourth panel (adjoint discovery) parked.

**Deferred/next**
- Freeze window closes → build exp-001 scenes; Bonnie's schema PR + viz
  extraction PR; her macOS numbers.
- Parking lot: TF/SF injector, true PML, finer-grid cloak runs, fourth
  panel, Disclosure physics-annex (humans' call), Blender/UE 3D
  presentation when a design earns it.
**Notes/gotchas** (promoted: pointer now in repo CLAUDE.md)
- FFT λ on short strips quantizes (190 samples → 19.0/21.1, never 20.0);
  use `spatial_wavelength` (zero-pad + parabolic).
- Reflection monitors close to the interface — beam-diffraction losses
  cancel between reference and scene runs.
- flaport `fdtd` + ceviche both run the shared scene on Py 3.14 without
  incident (Object accepts ndarray permittivity; fdfd_ez solve fine).

## 2026-08-06 — Kickoff: bench verified, exp-000 first light, board live

**Shipped/Done**
- Bench verified **native on Python 3.14** (no 3.12 fallback needed): `ceviche`,
  `fdtd`, numpy 2.5.1, matplotlib 3.11.1 all import clean in the repo `.venv`.
- **exp-000 Hello Maxwell** (`dee58b0`): hand-rolled 2D TMz FDTD (Yee grid,
  plain numpy, no solver library) — 600 nm plane wave vs n=2 cylinder (r = 2λ).
  Deliverables: `field.png` (hero render), `setup.png`, `wave.gif` (140
  frames), `NOTES.md`, `run.py` with three built-in self-checks.
- **Board channel live: co-lab #31** — substance post (what the lab is, honest
  frame, arc, first-light links, charter-lite) + standalone asks:
  Preston → Meep heavy-bench lane + arc review; Bonnie → exp-001 absorber
  co-design OR `lab/` viz system, her pick.
- Live watchers armed (board ~90 s poll + Telegram).

**Decisions**
- exp-000 = hand-rolled engine (the handoff's sanctioned option, taken
  deliberately): Marsh learns the actual physics engine, zero dependency risk.
  Libraries reserved for exp-001+ and cross-validation.
- Figure house style: GitHub-dark surface (`#0d1117`) + Crameri `berlin`
  diverging colormap — renders blend into the repo page in dark mode.
- Proposed exp-001 definition of done (on the board, awaiting the four):
  three rendered scenes + one observer-at-the-source comparison figure +
  NOTES.md with idealizations + cross-check vs ≥1 library solver.

**Verified**
- Wavelength by FFT: set 20.0 cells, measured 20.0 cells — 600 nm exact.
- Stability: max|Ez| = 2.50, finite over 1400 steps. Shadow ratio 0.48.
- All three renders eyeballed; one contrast bug on setup.png caught and fixed
  before commit. The exit-face hot spot = **photonic nanojet**
  (Chen/Taflove/Backman 2004) — published physics reproduced unprompted.

**Deferred/next**
- Four-way weigh-in on #31 → scope freeze → build exp-001 The Flashlight
  Statement.
- Cross-validate the exp-000 scene through `ceviche` + `fdtd`.
- Parking lot: TF/SF plane-wave injector, true PML, scattering cross-section
  machinery (exp-002's metric).

**Notes/gotchas**
- Python 3.14 + autograd/ceviche: **no fight** — the handoff's headline risk
  didn't materialize. Installed and imported clean, first try.
- PIL `optimize=True` collapses duplicate GIF hold frames (165 written → 140
  stored) — intended dedup, not a bug.
