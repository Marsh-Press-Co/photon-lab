# PHASE 5 — REVIEW · THERMODYNAMICS · Panel Iteration 58 · exp-081

*Fresh sub-agent, zero memory of any prior session — including this cycle's
own Phase-1 THERMODYNAMICS lead, a different fresh agent. Blind to the other
six seats' current-cycle Phase-5 reviews. Read, in order: `PANEL.md` in full,
`AGENTS.md` in full, `LOGBOOK.md` (RULED OUT R1–R9 in full; ESTABLISHED;
LIVE THREADS in full, T28's complete Iteration 46–57 history), `PLAN.md`'s
Iteration-58 queue, and the complete `experiments/081-.../` directory in
order: `phase1_proposal.md`, `photonics_construction.py`,
`phase1_results.json`, `_output.txt`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `phase4_results.md`,
`phase4_results.json`, `NOTES.md`. No `phase5_review_*.md`/
`phase5_redteam_audit.md` file from this cycle consulted.*

**No RULED-OUT item (R1–R9) is re-proposed or re-litigated here.**

---

## Verdict on the whole cycle: **PARTIAL**

This is a sound, well-audited cycle. Item 1's headline (Combined Verdict
NEITHER mechanically, REFUTE-leaning substantively) is now the
actually-decisive test this nine-cycle T28 y-wall sub-thread has needed
since exp-069, run for the first time, correctly against real reference
data, and stress-tested from four independent directions (admittance
family, reflectance ablation, `conj(r)` phase-convention sensitivity, and
git-provenance) — every stress test was actually *run*, by Red Team's own
Phase-2 audit, not merely argued about, and none flipped the Combined
Verdict. That is real, cumulative narrowing of the plane-wave/global-
steering coherent-echo construction family. It is PARTIAL, not
PROMISING, because T28's own substantive mechanism question — the origin
of the ~2.84°-family periodicity — remains exactly as open as it was
before this cycle; and not RULED OUT because Checkpoint criterion 2 is
correctly and consistently ruled NOT YET RIPE throughout the record (a
single result, one construction, one wavelength, on an empty scene).

---

## 1. The energy-budget precision check (item 3) — my own charter's
## Phase-1 work, audited fresh

### 1a. Is the `theta_local` vs. `90°−θ_beam` convention distinction stated precisely in the final record?

**Yes — and it survives all four layers of the record (Phase 1 results,
Red Team's Phase-2 audit fix-docket item 6, Phase 3 synthesis §2 item 5,
and `NOTES.md`'s Director-synthesis section) with the same two numbers
carried forward unchanged and correctly labeled at every hop.**

I independently re-ran `item3_energy_budget()` from the committed
`photonics_construction.py` (not copied from any prose) and confirm:

| convention | admittance | value | tested object? |
|---|---|---|---|
| `90°−θ_beam` (`[48°,54°]`) | matched | `1.4943×10⁻³` (`0.14943%`) | **YES — the object item 1 actually built and period-tested** |
| `theta_local(y_s)` (`5.27°–15.50°`) | matched | `1.2886×10⁻⁸` | **NO — never built or period-tested this cycle** |
| `theta_local(y_s)` | realizable (`μ_r=1`) | `2.6375×10⁻⁸` | **NO — never built or period-tested this cycle** |

Ratio `1.4943×10⁻³ / 1.2886×10⁻⁸ = 1.1597×10⁵` — reproduces the record's
own `~116,000×` figure exactly, and I confirm Red Team's own Phase-2 audit
item F (R9 commensurability check: both operands are `|r(θ)|²`, same
units, same operation, differing only in which `θ` array is passed —
correctly commensurable, no unit-mismatch risk of the R9 kind).

The distinction the task asked me to fresh-eyes-check is precisely this:
Phase 1's own headline ("negligible... under either angle convention")
originally risked conflating a bound on the *tested* object with a bound
on a *different, un-built* one — exactly the shape EM's Phase-2 critique
flagged as its own secondary point ("citing the tighter number as
covering 'this construction family' conflates a bound on the object
tested with a bound on a different, not-yet-built one"). Red Team's
Phase-2 audit correctly triaged this as fix-docket **item 6 [LOW]** —
prose-only, no new computation required (the numbers were already
correct; only the framing needed disambiguation) — and Phase 3's §2 item
5 supplies the exact fix: *"the tight `theta_local`-convention bound
(`~1.3×10⁻⁸`) covers a construction item 1 never built or period-tested;
the looser `0.15%` `90°−θ_beam`-convention bound covers the object item 1
actually tested and scored."* `NOTES.md`'s Director-synthesis section
(item 5) and item 4(b)'s own disclaimer restate this identically. I
checked `phase4_results.json`: item 3 is correctly *absent* from Phase
4's re-run scope (only items 1/1b/2 were re-computed, since fix-docket
item 6 required no new arithmetic) and `phase1_results.json` is
bit-identical pre/post-Phase-3 (`git diff` empty, confirmed by
`phase4_results.md`) — so the two cited numbers are the same numbers
throughout, never silently redefined. **This is precisely what the fix
docket required, correctly triaged as prose-only, and correctly applied
without touching numbers that didn't need touching.**

### 1b. Is the expressibility contract honored (labeled as post-run analytic, not FDTD output)?

**Yes, in substance throughout; the literal charter phrase is stated once
(the boilerplate seat-header block in `phase1_proposal.md`) rather than
re-stated at item 3's own point of use.** I confirm from direct code
inspection that `item3_energy_budget()` calls only `d80.n_profile_exact`/
`nu_profile`/`damp_e_profile`, `ywas.reflection_coefficient_vec`, and
`d80.reflection_coefficient_vec_realizable` — pure `|r(θ)|²` desk
arithmetic on already-committed reflectance primitives, zero `Sim.run()`
calls, zero FDTD anywhere in this function or this cycle (confirmed
independently: `photonics_construction.py`'s only imports are `dg065`,
`br`, `ywas`, `d80` — no `fdtd2d`/`emit` module in the import list).
Idealization 7 ("Zero new FDTD anywhere in this cycle") and the repeated
Phase-3/Phase-4 disclosures ("Zero `lab/` diff this entire cycle," "zero
new FDTD... this cycle's own extension included") make the analytic,
post-run nature of the entire cycle — item 3 included — unambiguous to
any reader of the full record. The one gap, genuinely minor and
non-blocking: the specific phrase "post-run analytic calculation, not an
FDTD output, labeled as such" from the charter is not literally repeated
next to item 3's own numbers in `NOTES.md` or `photonics_construction.py`'s
docstring — a reader who only skims the "## Result" / item-3 block in
isolation, without the surrounding zero-FDTD context, would have to infer
the label rather than read it stated locally. I recommend, non-blocking,
folding one sentence into `item3_energy_budget()`'s own docstring at
Iteration 59 (e.g. "This is a desk/analytic `|r(θ)|²` calculation — no
FDTD run — per THERMODYNAMICS' own expressibility contract") so the label
travels with the function itself, not only with the seat-header
boilerplate three levels up the document.

### 1c. A genuine, independently-derived addendum this record does not yet state

Re-reading `phase1_results.json`'s own `theta_local_convention.per_absorb`
block (already computed, never highlighted in prose): **ABSORB=40 is
confirmed the worst case (largest reflected-power-fraction bound) among
all four tested depths, under both angle conventions and both admittance
families** —

| ABSORB | `90°−θ_beam` (matched) | `theta_local` (matched) | `theta_local` (realizable) |
|---|---|---|---|
| 40 | `1.494×10⁻³` | `1.289×10⁻⁸` | `2.637×10⁻⁸` |
| 60 | `5.115×10⁻⁵` | `1.597×10⁻¹¹` | `6.496×10⁻⁹` |
| 70 | `1.316×10⁻⁵` | `1.394×10⁻¹¹` | `3.136×10⁻⁹` |
| 80 | `3.569×10⁻⁶` | `4.072×10⁻¹²` | `1.335×10⁻⁹` |

All three columns decrease monotonically with `ABSORB` depth (physically
sensible: a shallower graded-loss boundary reflects more). This
independently confirms the write-up's "even under the loosest possible
[case]" language is not overstating its own scope by cherry-picking
ABSORB=40 — it genuinely is the loosest of the four depths this cycle
priced, on every metric computed. This was true in the committed JSON
already; nobody in the five blind critiques or the Red Team audit stated
it explicitly. **Non-blocking, record-hygiene addendum for Iteration 59**:
fold this table into `NOTES.md` so the "worst case across ABSORB depths"
claim is stated, not merely implied by data a reader would have to
reconstruct from the raw JSON.

One further scope note, also non-blocking: item 3's entire energy budget
is computed at 600nm only (`LAM600` hardcoded throughout
`item3_energy_budget()`), consistent with every other computation this
cycle. `NOTES.md`'s item-3 sentence ("this entire construction family
could never matter to constraint 3's energy budget... under either angle
convention") is true and correctly supported at 600nm, and the cycle's
own Checkpoint-2 ruling elsewhere in the record already discloses the
single-wavelength scope for the cycle as a whole — but that caveat is not
repeated locally at item 3's own sentence. A future reader skimming only
that sentence could read "this entire construction family" as a
wavelength-general claim. Recommend, non-blocking: append "(600nm; not
yet checked at 450/750nm)" to that sentence specifically.

---

## 2. Fresh-eyes read of the rest of the cycle, from the energy/
## detectability vantage

**The record is internally consistent on the point that matters most to
this seat: nothing in this cycle ever mixes coherent field amplitudes
(`E_direct`, `E_image`) into an incoherent power/energy quantity.** I
traced this specifically because it is the exact failure class my
charter exists to catch (an absorbed/reflected-power claim built by
squaring a sum of two *field* quantities of wildly different scale would
silently misstate a power budget by orders of magnitude). Item 1 scores
`Re{E_total}` pair-*deltas* only, never `|E_total|²`; item 3 prices
`|r(θ)|²` alone, entirely independent of `E_direct`'s magnitude or
existence. EM's own Phase-2 critique flagged this same point from the
EM vantage (§3(a): "no intensity/power quantity anywhere in this cycle
ever combines `E_direct` and `E_image` incoherently") — I independently
confirm it from the THERMODYNAMICS vantage: the `10⁵`-scale gap between
`|E_direct|≈89–111` and `|E_image|≈1.3×10⁻⁴–3.5×10⁻³` (item 1b's own
finding) never propagates into item 3's energy accounting, because item
3 is built from `r(θ)` directly, not from any curve item 1 constructs.
This is exactly the discipline a THERMODYNAMICS reviewer should demand
of any cycle that builds both a field-amplitude test and an energy
bound side by side, and it holds here.

**The energy quantity this cycle prices is a reflected-power-fraction
upper bound at the wall, not an absorbed-power/temperature-rise/emission
chain** — a legitimate and correctly-disclosed adaptation of my charter's
standard sidecar to this cycle's actual question ("what fraction of
total scene power the echo path could actually carry," PLAN.md's own
Iteration-58 item-3 framing), not the phenomenon-program's usual
absorbed→heat→re-radiation chain. That chain does not apply here because
this cycle tests a spurious coherent-echo *signal* path, not a material
*absorption* event — T1 is N/A and constraint 3 is not engaged, exactly
as every T28 instrument cycle since exp-071 has correctly disclosed (and,
per LOGBOOK's own exp-073 finding, once silently dropped — it is not
dropped here; `phase1_proposal.md` §3 states it explicitly, and `NOTES.md`
carries it through). The interception-factor-of-1 idealization (item 3's
own Idealization 5) is stated correctly as a bound that can only loosen,
never tighten — I confirm this by construction: interception multiplies
the reflected-power-fraction linearly, so any value ≤1 can only shrink
the reported bound, never grow it. No detectability claim is smuggled
past this upper bound anywhere in the record — it is used exactly as an
upper bound throughout, never cited as a point estimate.

**Nothing else in this cycle's record bears on energy/detectability
accounting that the other six seats' narrower charters would miss.** The
cycle's other three items (1, 2, 4) are a field-amplitude periodicity fit,
a reflectance-gate re-run, and a docstring fix respectively — none of
them touch power, heat, or detectability, and I find no place where a
quantity from one of those items is later, silently, treated as an energy
quantity.

---

## 3. Ranked top-3 candidate directions for Iteration 59 (THERMODYNAMICS' own ranking)

1. **The PAD-loaded real-article check (PLAN.md's Tier 2, now six
   consecutive T28 cycles deferred).** From this seat's own vantage this
   is the single highest-priority item on the board: every energy/
   reflectance number this program has ever computed for T28 — item 3's
   own `|r(θ)|²` bounds included — has been priced against an EMPTY
   scene. An empty scene cannot test whether a real absorbing article
   changes the energy budget at all; my own upper bound (interception=1)
   is a bound on a vacuum geometry's reflectance, not on any physically
   realizable absorber loading. This is the only queued item that would
   tell THERMODYNAMICS whether "negligible energy budget" survives contact
   with a real article, and it has been named explicitly, then deferred,
   in every one of the last six T28 cycles' own rankings.

2. **The real 750/450nm wavelength-generality x-wall leg (deferred six
   consecutive cycles).** Item 3's own energy bound, and item 1's own
   REFUTE-leaning finding, are both 600nm-only. This program's own
   founding discipline (the witness statement is white light; the
   established absorber's own headline finding is that it is
   wavelength-flat) makes a single-wavelength "negligible" claim
   structurally incomplete in exactly the way this lab has flagged before
   for other proposals. Directly relevant to whether my own §1c scope
   note above needs to become a load-bearing caveat rather than a
   non-blocking one.

3. **Extend `phase5_redteam_phase_convention_check.py`'s empirical FDTD
   tie-breaker to 2–3 angles inside `[47.5°,54.5°]`** (EM's own item,
   confirmed genuinely open but not outcome-determining this cycle by
   Red Team's own `conj(r)` sensitivity run). Lower priority from the
   energy-accounting vantage specifically — item 3's own bound is built
   from `|r(θ)|²`, which is identical under `r` and `conj(r)` by
   construction (`|conj(r)|=|r|`), so this convention ambiguity cannot
   move any energy number in this record, only item 1's period-recovery
   result. Still real, cheap, and queued — ranked third here because it
   is outside this seat's own charter concern, not because it is
   unimportant to the program.

---

## Summary

**Verdict: PARTIAL.** Item 3's energy-budget precision fix (fix-docket
item 6) is applied correctly and consistently across Phase 1 results,
Red Team's audit, Phase 3 synthesis, and `NOTES.md` — the `theta_local`
bound (`~1.3×10⁻⁸`/`~2.6×10⁻⁸`, never built or tested) is now clearly
distinguished from the `90°−θ_beam` bound (`0.15%`, the object item 1
actually tested), with the ~116,000× gap between them stated as a finding
about which convention describes reality, not a license to treat the two
as interchangeable. The expressibility contract is honored in substance
(zero FDTD, pure `|r(θ)|²` desk arithmetic) throughout, though the
charter's own labeling phrase could be echoed locally at item 3's own
docstring, not only in the seat-header boilerplate — a non-blocking
hygiene note for Iteration 59, alongside stating explicitly (from data
already computed but not yet narrated) that ABSORB=40 is confirmed the
worst case across all four tested depths, and appending an explicit
600nm-only scope note to item 3's headline sentence. No coherent-field
amplitude is ever silently combined into an incoherent power/energy
quantity anywhere in this cycle — the one failure mode this seat exists
to catch most directly.
