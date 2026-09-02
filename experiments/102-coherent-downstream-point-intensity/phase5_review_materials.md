# Phase 5 Review — MATERIALS & METAMATERIALS

**Panel Iteration 79, exp-102. Fresh sub-agent, blind and parallel — no
other seat's Phase-5 output read this cycle.** Charter: sub-wavelength
structure; what could physically realize the proposed optical behavior;
owns the realizability bound (published / plausible /
unobtainium-with-parameters).

## 1. Verification of my own Phase-2 mandatory fix 7

Fix 7 (my own Phase-2 critique, elevated verbatim by Red Team's Phase-2
audit attack 6, adopted 0-overridden at Phase 3) required: *"the
UNOBTANIUM-WITH-PARAMETERS/'a buildable coating at this thickness would
show a shallower, not deeper, on-axis darkening' caveat MUST be stated
inline beside Prediction 1's κ(θ) confirmation text in the Result section
below (not only cross-referenced via Idealizations)."*

`NOTES.md`'s Result section, quoted verbatim:

> "on-axis coherent intensity ratio `κ(θ)` (region-averaged) ranges
> `3.68×10⁻³`–`7.29×10⁻³` across all 12 (angle,config) cells — genuinely
> dark, well inside `[0,0.10]`. **Realizability caveat (per fix 7, stated
> inline as required): this article is the byte-identical R4-family
> `graded_black_shell`, already locked UNOBTANIUM-WITH-PARAMETERS
> (`REALIZABILITY_MEMO.md` Amendments 6–7) — a real, buildable coating at
> this shell thickness would show a shallower, not deeper, on-axis
> darkening than this idealized figure.**"

**Judgment: HONORED, exactly as required, at the one location the fix's
own text names.** The caveat sits in the same paragraph, immediately
after the κ(θ) confirmation sentence, not merely cross-referenced via
Idealizations. This is a genuine instance of the discipline working —
the identical shape of gap R1's own Iteration-14 ENZ addendum exists to
prevent was caught before Phase 3 froze, not after.

**But the fix's OWN SCOPE was narrower than the risk it exists to close,
and that gap is now visible.** Fix 7's text bound the caveat to travel
"beside Prediction 1's κ(θ) confirmation text" — singular, one sentence.
`NOTES.md`'s **Learned** section, item 1, restates the identical headline
figure a second time, in different rounding, with no caveat attached:

> "a genuine, spatially-localized on-axis darkening of `κ~0.4–0.7%`,
> immune by construction to the `i_inc`/cosθ artifact... and to
> fixed-lab-frame registration..."

A reader who cites Learned #1 in isolation — the section this program's
own convention (R21, R20) treats as the durable, future-citable summary
of "what this cycle established" — gets the bare number with no
realizability qualifier at all. This is not a violation of fix 7's
literal text (which named Result, specifically, and Result complies); it
is the exact residual the fix's narrow scoping leaves uncovered, and it
is precisely the R1/Iteration-14 failure shape: an idealized,
already-locked-unrealizable article's optics, restated in the section a
future cycle is most likely to skim and cite, without the qualifier that
makes it safe to read. **Next** does not restate the number at all (item
4 refers to "this cycle's raw `κ(θ)`/`I_abs(θ)`" generically, no digits),
so the gap is confined to Learned #1 — one location, not a pattern, but
a real one. Recommend, forward: any future fix in this lineage should
bind the caveat to travel with the FIGURE, not the section — i.e., any
sentence in Result OR Learned OR Next that restates this cycle's κ(θ)
magnitude carries the qualifier, not only the first sentence that states
it.

## 2. Independent numeric verification (recomputed from `results.json`,
## not restated)

I recomputed several of `NOTES.md`'s cited figures directly from
`primary_rows`/`gates` in `results.json` rather than trusting the prose:

- **Gate C corrected max deviation**: recomputed
  `|I0_corrected·u_x − i_inc|/I0_corrected` from the raw
  `i0_corrected`/`u_x`/`i_inc` triples for all 12 cells — max
  `0.009197942611745866` (G40_R4@42.960901), min `0.0004354976390685828`
  (G40_R4@40.26542). **Matches `NOTES.md`'s "max deviation 0.92% across
  all 12 cells (range 0.04%–0.92%)" exactly.**
- **Gate D discrimination percentages**: recomputed
  `|κ_perturbed−κ_correct|/κ_correct` from the raw region-κ pairs —
  `48.951%` (C40_R4) and `8.242%` (G40_R4). **Matches `NOTES.md`'s
  "48.95% (C40_R4) and 8.24% (G40_R4)" exactly.**
- **Off-axis `κ_off(θ)` range**: recomputed min/max across all 12
  `kappa_off_region` values — `1.0405807`–`1.0766458`. **Matches
  `NOTES.md`'s "1.041–1.077" to stated precision.**
- **Point-vs-region ratio range**: recomputed `κ_point/κ_region` for all
  12 cells — `1.2301`–`1.5591`. **Matches `NOTES.md`'s "1.23–1.56×"
  exactly.**
- **`Δφ(θ)` range**: recomputed min/max of `delta_phi` — `0.2092`–
  `0.5871` rad, all positive. **Matches "+0.21–+0.59 rad, all positive"
  exactly.**

**One figure did NOT reproduce — see §3.**

## 3. Citation/restatement defect found (R4/R9/R20 lineage)

`NOTES.md`'s Result section states the primary-channel on-axis
`κ(θ)`(region-averaged) range as **`3.68×10⁻³`–`7.29×10⁻³`**. I
independently recomputed min/max over all 12 `p1_on_axis_kappa` cells in
`results.json`:

```
C40_R4@41.460901  0.003479968184461652   <- true minimum
C40_R4@38.59023   0.003681515158129401   <- second-smallest (≈3.68e-3)
...
C40_R4@42.960901  0.007289772019643874   <- true maximum (matches stated 7.29e-3)
```

**The true minimum across the committed data is `3.48×10⁻³`
(C40_R4@41.460901°), not the `3.68×10⁻³` `NOTES.md` cites** — a genuine,
independently-checkable mismatch between a stated "precisely reported"
range and the underlying `results.json` array, not a rounding artifact
(the two values differ in their second significant digit). The maximum
endpoint (`7.29×10⁻³`) is correct. `run_output.txt` contains no
autogenerated min/max summary line for this quantity, so the range in
`NOTES.md` was hand-composed rather than machine-printed — the
second-smallest value (`3.6815×10⁻³`, the C40_R4@38.59023 cell, which
happens to be one of the more prominently-logged rows in
`run_output.txt`) was most likely mistaken for the true minimum.

**Disposition: non-load-bearing.** Both the stated and the true value sit
comfortably inside Prediction 1's `[0,0.10]` falsification band, and
Learned item 1's own rounded restatement (`κ~0.4–0.7%`) is arguably even
looser than either — a materially-affected verdict does not follow from
this defect. But it is a genuine instance of the class R4 exists to name
("a hand-typed 'precisely recomputed' figure that does not actually
reproduce from committed data"), located in the Result section, and it
lands in the **very next cycle** after R20's own automatic clause fired
for the first time in this program's history (Iteration 78, exp-101,
three R4-class Result-section defects). I flag it explicitly for Red
Team's own tally: on my count this is the only R4-class defect I found
in this document (I checked every other numeric claim in Result/Learned
against source and all reproduced exactly — §2, above), so it does not
by itself approach R20's "three or more" bar, but Red Team should
combine this with any other seats' independent findings before ruling.

## 4. Realizability-bound classification (this cycle's own charter
## question)

No new mechanism, material, or parameter is proposed this cycle — T1
route N/A is correctly self-scored and I confirm it independently: the
parameter table, `run.py`, and `results.json` touch nothing but the
already-fixed R4-family `graded_black_shell` geometry and the native
flagship absorber (Gate B leg), both already resolved in
`REALIZABILITY_MEMO.md`. **Classification, restated for the record: this
cycle's article is UNOBTANIUM-WITH-PARAMETERS, unchanged** — the R4
family (`r_in=60/r_out=156`, cpl=40) is the physically-identical
construction to the native flagship (`r_in=30/r_out=78`, cpl=20) at
double grid resolution (shell thickness `96·15nm=48·30nm=1440nm`, outer
radius `156·15nm=78·30nm=2340nm` — I re-verified this arithmetic myself
in Phase 2 and it still holds; nothing in Phase 3/4 rescaled the
article), so no new realizability finding is opened or reopened by this
instrument build. The Result section's "shallower, not deeper" direction
claim is qualitatively correct and consistent with T9's own Babinet-
ceiling logic (a real, imperfect coating cannot exceed an idealized
zero-reflectivity, arbitrarily-graded absorber's own extinction) — I find
no reason to dispute the direction, only the inline/Learned-scope
completeness addressed in §1.

## 5. Verdict on the cycle's Combined Verdict candidate

**CONFIRM-WITH-GAPS.**

Reasoning, from this seat's lens: the instrument itself is a genuine,
correctly-scoped, T1:N/A diagnostic build — nothing here claims or
implies a constraint-satisfying mechanism, and the article under test
stays correctly, consistently classified UNOBTANIUM-WITH-PARAMETERS
throughout. The two "gaps" that keep this from a clean CONFIRM are: (a)
Gate B — the cross-scale reproduction check against the established
`beam_behind` figure — genuinely FAILS, diagnosed honestly as a
footprint mismatch (near-field point sample vs. far-field-relative window
average) rather than force-fixed or buried; only Gates A and D
independently support trusting this cycle's primary-channel numbers, a
real, disclosed limitation on how much weight the absolute `κ(θ)`
figures can carry until a properly-footprint-matched Gate B exists
(`NOTES.md`'s own Next item 1); (b) the §3 citation defect and the §1
caveat-scope gap, both real, both non-load-bearing, both worth fixing
before this cycle's numbers are cited elsewhere, especially given R20's
own firing on the immediately preceding cycle. Nothing found here rises
to DISPUTE — no scored prediction is wrongly marked, no constraint is
quietly dropped, and the one genuine FAIL (Gate B) is already disclosed
as a real, open limitation rather than smoothed over.

## 6. Ranked top-3 candidate directions for Iteration 80 (MATERIALS' lens)

1. **A properly-footprint-matched Gate B** (`NOTES.md`'s own Next item
   1): rebuild the cross-scale reproduction check against the LITERAL
   `beam_behind` window (or an equivalently-justified window at the R4
   scale) rather than a rescaled point/region sample. Until this exists,
   no future citation of this instrument's absolute on-axis number
   against the established `beam_behind` figure (or, eventually, against
   any REALIZABILITY_MEMO witness-scale claim) has independent cross-
   validation — this is the single highest-priority item from a
   realizability-evidentiary standpoint, since it gates how much trust
   this new channel's numbers can ever carry.
2. **Extend the new coherent point/region instrument across the T8
   bridge family (r=78/156/312), not only the single R4 near-field
   standoff.** This cycle's own `κ(θ)` machinery is, for the first time
   on this bench, a phase-resolved (not window-averaged) measure of
   on-axis darkening — exactly the missing ingredient for a
   quantitative, rather than qualitative, version of this cycle's own
   "shallower, not deeper" realizable-coating claim. A coherent
   multi-scale sweep would let a future REALIZABILITY_MEMO entry state a
   number, not merely a direction, for how much of the idealized
   article's near-field darkening is a Babinet/near-field artifact
   (T8/T9) versus surviving toward the witness-scale asymptote — directly
   sharpening the one qualifying sentence my own Phase-2 fix put into
   this cycle's Result section.
3. **Tier 1's queued `delta_scene` R3-vs-R4 split** (PHOTONICS' zero-FDTD
   physical-hypothesis check first, per the Iteration-78/79 Reconciled
   ranking) — untouched this cycle by design, and still the program's
   longest-standing unresolved diagnostic thread. From this seat's lens,
   the open question worth tracking once PHOTONICS' hypothesis check
   lands is whether any resolution-dependence found there reflects a
   genuine sub-wavelength-structure/discretization tolerance question
   (a realizability-adjacent concern — does a real coating's own
   manufacturing tolerance at this feature scale matter the way a grid
   resolution does here) or is purely a numerical artifact orthogonal to
   any physical construction question.
