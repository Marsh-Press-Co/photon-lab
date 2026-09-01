# Phase 5 Review — VISION SCIENCE (Panel Iteration 77, exp-100)

## Verdict

**CONCUR-WITH-GAP(S).**

Both of my Phase-2 mandatory fixes landed correctly, verified directly
against `run.py`/`results.json`, not taken on the Director's word. The
science is sound within its own disclosed scope. But one caveat-propagation
gap remains at the exact point-of-claim my own fix 8 was written to protect
— Leg A's Result paragraph states a bare "PASS at both bars" headline
before its own governing "instrument-characterization-only" status (Tier
1's ambiguous outcome) is restated alongside it — a smaller instance of a
defect class this program has fired Checkpoint-4-adjacent findings on
before (Iteration 24's MARGINAL-band/Hypothesis-slip; Iteration 76's
"ambient-light-analog caveat propagated to dispositions (b)/(c), not only
(a)"). Not severe enough to dispute the cycle — the caveat text exists,
correctly worded, one clause later in the same entry — but real enough to
flag before this becomes the next cycle's citation.

## 1. Were both Phase-2 mandatory fixes actually implemented correctly?

**Fix 9 (corrected scotopic anchors) — YES, verified from primitives.**
`run.py:404-405`:
```
L_STAR_LAB_BAND = (5.3e-6, 7.5e-5)
L_STAR_FIELD_BAND = (1.7e-4, 1.2e-3)
```
This reproduces the corrected Phase-3-committed band digit-for-digit
(`L*_lab∈[5.3×10⁻⁶,7.5×10⁻⁵]`, `L*_field∈[1.7×10⁻⁴,1.2×10⁻³] cd/m²`), not
the superseded Iteration-1 draft numbers my Phase-2 critique caught
(`L*≈5×10⁻⁶–4×10⁻⁵`, moonless-rural `≈1.7×10⁻⁴`). `results.json`'s
`tier2_leg_a.l_star_lab_band`/`l_star_field_band` fields carry the same
values through to the persisted record. Clean.

**Fix 8 (static-contrast-bound-only caveat) — YES, verified from
primitives.** `run.py:418-425` attaches this exact string to every
`tier2_leg_a` result:
> "Fix 8 (VISION-a): static-contrast bound only, provisional pending T3
> (still this program's longest-standing unbuilt instrument) — NOT a
> completed Tier-W/Tier-A verdict on a swept angular fringe. Fix/
> Idealization 64 (PHOTONICS): 600nm-only; LOGBOOK's established T21
> 750nm/theta=40deg fringe (0.0237, 4.7x C_thr) in this identical window is
> an unaddressed same-window contamination-risk precedent, not tested this
> cycle."

This is not merely present in prose — it is a `dict` field co-computed with
`peak_abs_delta_scene`/`pass_lab`/`pass_field` inside `tier2_leg_a()`
itself, so it cannot be dropped independently of the numbers it qualifies
(the shape of defect fix 8 exists to prevent). It also correctly folds in
PHOTONICS' Phase-2 fix (the T21 750nm/4.7×`C_thr` same-window precedent),
which Red Team ruled ADOPTED alongside mine — both riders present in one
string, at the one place the number is computed. I checked the whole file
for a stray unqualified "Tier-W"/"Tier-A" claim (the exact Iteration-24
recurrence risk): none found — every other occurrence in `NOTES.md` is
either the bars' own name (`§Setup`: "photopic bars... (Tier A)... corrected
scotopic band (fix 9) for Tier W" — naming, not claiming) or paired with
the caveat inline. Both fixes are correctly implemented in code, not just
promised in Phase-3 prose.

## 2. Does NOTES.md's Result section read honestly? The gap.

Read literally, yes: the same paragraph that reports "PASS at both bars, as
predicted" also states, three sentences later, "reported as a
**static-contrast bound only, provisional pending T3** — not a completed
Tier-W/Tier-A verdict" and the 600nm/T21 rider. No overclaim ships
uncaveated to `results.json` or to `NOTES.md`'s own prose. On the letter of
fix 8, this is compliant.

**The gap I am flagging is a second, distinct caveat this cycle's own
architecture demands and does not restate at Leg A's point of claim: Tier
1 came back AMBIGUOUS, not majority-PAD or coupling-detected.** Fix 3's own
pre-registered branches (Idealization 70) state explicitly that under the
ambiguous outcome, **"Tier 2's numbers are filed as
instrument-characterization only; T1 stays N/A, unresolved"** — this
exact sentence lives in `t1_label` (`results.json`) and in the Idealization
70 text, but Leg A's own Result paragraph never repeats it. A reader citing
only "Tier 2, Leg A — PASS at both bars, plus VISION's static-contrast/
600nm caveats" — the two caveats that *are* stated there — would not learn
from that paragraph alone that the very identity of what is being scored
(a real diffraction signal vs. a domain artifact) was left unresolved this
cycle. This matters for my own charter specifically: a threshold
comparison's meaning depends on what physical quantity is being compared
to it, and Tier 1's ambiguous finding is exactly a question about whether
`delta_scene` is a physical quantity a real observer could ever encounter,
or a PAD/domain-construction artifact with no scene-realizable analog at
all. The two caveats present (static-vs-transient; 600nm-only) are about
*instrument scope*; the missing one (ambiguous mechanism identity) is about
*whether there is a real photonic phenomenon here at all* — a different,
independently necessary caveat, not redundant with the two already
present. **Recommend, cheap, same-cycle if reopened, else Iteration 78's
own first edit**: append one clause to Leg A's Result paragraph tying it
explicitly back to the ambiguous T1 label — e.g. "…left untested this
cycle; per Idealization 70's ambiguous branch, this score itself is filed
as instrument-characterization only, not a verdict on a confirmed
article-coupled phenomenon."

One further, milder observation on the same paragraph: it leads with the
bolded "PASS at both bars, as predicted" before either caveat — the same
headline-ordering shape Red Team required THERMODYNAMICS to fix at a
recent cycle's close ("lead with the... caveat, before the raw numbers").
Here the caveat follows within the same short paragraph rather than pages
later, so I am not elevating this to a mandatory fix on its own — but
combined with the missing ambiguous-T1 restatement above, the pattern is
the same shape twice in one paragraph, worth correcting together.

## 3. Perceptual-relevance angle on the ambiguous Tier-1 outcome and the `beam_behind_t28` defect

**On the ambiguous Tier-1 outcome:** it does not change Leg A's own
arithmetic. `C_thr(L)` scores `delta_scene`'s magnitude directly; a human
retina responds to the physical field pattern at the observer, not to
whether that pattern's origin traces to a genuine article-coupled
diffraction term or a domain/PAD construction artifact — the same photon
flux looks the same either way. So the ambiguous mechanism finding does
not threaten Leg A's PASS reading as a *magnitude* statement. What it does
threaten — and what my gap above is about — is treating that PASS as a
statement about a *real scene* at all: if the eventual disposition lands
on majority-PAD (a live possibility the family-stratified split has not
ruled out — R4, the family Leg B itself measured, shows no significant
correlation), the correct reading is "an instrument/domain quantity was
shown too small to matter, which was never at perceptual risk in the first
place because it may not correspond to anything a real flashlight-and-
object scene would produce." That is a materially different claim than
"a real diffraction fringe was shown too small to matter," even though
both currently read as the same PASS number.

**On `beam_behind_t28`'s UNINTERPRETABLE reading — this is the more
consequential flag, and it cuts toward urgency, not caution.** The defect
(a fixed downstream window that does not track the oblique-incidence
lateral shadow walk, 125.7–154.6 cells at these angles) produced readings
of 0.42–0.46 — dramatically above the established ~1.5–1.8%
`graded_black_shell` figure. NOTES.md's own diagnosis correctly attributes
this to un-shadowed side-flux contamination, not real transmission, and
correctly declines to report it as a constraint-1 finding. That discipline
is right, and I have nothing to correct in it. But I want to pin, for the
record, exactly what is and is not at stake perceptually once Iteration
78's corrected re-measurement runs: **a beam transmission fraction at the
0.42–0.46 scale, if it were ever real, is not a near-threshold call my
charter would need to adjudicate at all.** `C_thr(L)` tops out at 0.02
(field bar); a leaked beam at tens of percent of incident power is 20+×
above even the loosest bar in this program's own table, orders of
magnitude past the static-vs-transient or photopic-vs-scotopic
distinctions fix 8 exists to police. In other words: **the corrected
`beam_behind_t28` re-run does not need to wait on any new VISION
threshold work, and its outcome does not hinge on T3.** If the fixed
window still reads far above the ~1.5–1.8% established figure, that is an
unambiguous, construct-validity-proof perceptual failure (a visible gap or
bright leak in an otherwise-opaque silhouette) diagnosable by inspection
against bars already pinned since Iteration 1 — a genuinely different
situation from `delta_scene`'s own sub-threshold ripple, which does need
T3 to fully close. I flag this so Iteration 78 does not accidentally
bundle the corrected constraint-1 re-run behind T3's own build queue: it
should not be gated on it.

## 4. Ranked top-3 for Iteration 78

**1. Build T3 — yes, it is time, and I am ranking it first.** This cycle's
own Result section states plainly that Leg A "cannot be upgraded to a
genuine Tier-W/Tier-A verdict without it" — the first time in this
program's history that a specific, already-filed, already-scored measurement
is named as blocked on T3's absence, rather than T3 being cited only as a
general standing gap. T3 has been unbuilt since PANEL.md's Iteration-1
metrics table, was LOCKED and UNCONDITIONAL for Iteration 30 (47 iterations
ago), and was blocked twice at that attempt by a reproducible upstream
`[bio]`-tagged content-policy false-positive on ordinary kinetics/
temporal-CSF vocabulary in an entirely classical-optics context — a
routine-cannot-execute stop requiring direct human intervention, not a
scientific finding, and (per my own full LOGBOOK read) never subsequently
retried. Recommend Iteration 78 make a genuine, differently-scoped attempt
— e.g. a session/dispatch route that does not concatenate the exact
`n(t)`/"dose accumulation"/"carrier lifetime" vocabulary cluster that
pattern-matched before, or an explicit human-in-the-loop dispatch as
LOGBOOK's own Iteration-30 entry recommended — rather than leaving it to
silently compete against cheaper items on a ranked list a ninth time. This
is a process/scheduling ask, not a physics one, and it does not compete for
the same FDTD budget as the two items below.

**2. Fix `beam_behind_t28`'s window centering and re-run constraint 1 at
the same 6 angles (NOTES.md's own Tier 0).** Concur with the Director's
own draft queue. From my seat specifically: this is not a threshold
question (see §3 above) — it is a pure instrumentation fix, cheap, and it
resolves this cycle's own explicitly-disclosed UNINTERPRETABLE result
before another cycle's citation has to carry the disclaimer forward. Zero
dependency on T3.

**3. The real 750nm (and 450nm) wavelength-generality leg for Leg A's own
scored window.** This directly closes the caveat my own fix 8 (jointly
with PHOTONICS' Idealization 64) currently leaves open every cycle it is
repeated rather than tested: LOGBOOK's own T21 entry already measured a
750nm/θ=40° fringe at 4.7× `C_thr` in this *identical* 36°–43° window — an
on-file precedent, not a hypothetical. A single-wavelength PASS cannot
bound a real flashlight's white-light contamination risk, and this is now
the second consecutive T28-adjacent cycle (this one, plus the standing
5-8-cycle-deferred item NOTES.md's own §Next already names) to inherit the
gap rather than test it. Cheaper than T3, does not require the transient
instrument, and would let a future Leg A citation drop the 600nm-only
caveat instead of repeating it indefinitely.

## Sources checked directly this review

`run.py:399-427` (Tier 2 Leg A implementation), `results.json` (`tier1_item1`,
`tier1_item2`, `tier2_leg_a`, `t1_label`, `tier2_leg_b` blocks),
`disposition_memo.md`, `NOTES.md` (full), `phase1_proposal.md` (full),
`phase2_critique_{vision,em,materials,photonics,thermodynamics}.md`,
`phase2_redteam_audit.md`, and LOGBOOK.md's T2/T3/T16/T21/T24/T27 thread
entries plus the Iteration-24/-30/-31/-76 narrative entries bearing on
T3's build history and this program's caveat-propagation precedents.
