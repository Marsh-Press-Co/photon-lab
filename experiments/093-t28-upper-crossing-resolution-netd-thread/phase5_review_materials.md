# PHASE 5 — REVIEW · MATERIALS & METAMATERIALS (fresh context, blind) · exp-093 · Panel Iteration 70

*Fresh sub-agent. Charter: sub-wavelength structure / realizability bound
(published / plausible / unobtainium-with-parameters); founding seat of
standing rule R15 (resolution-sensitivity of calibration-boundary
classifications). This cycle makes no phenomenon-mechanism claim (T1 N/A),
so the realizability-bound half of the charter has nothing new to bound;
this review is written almost entirely under the R15-founder half.*

## 1. The `r15_disclaimer` — wording and print-parity check (JSON *and* stdout)

**Wording, verbatim against the Phase-3-adopted text (`phase3_synthesis.md`
§1.3):** matches exactly, word for word, in all three surfaces —
`phase3_synthesis.md`'s own adopted text, `results.json`'s
`r15_disclaimer` (top-level *and* nested under `item2`), and
`run_output.txt` line 221. No drift, no silent softening, no reversion to
the pre-fix "direct completion" language my own exp-093 Phase-2 critique
flagged. **Confirmed correct, confirmed printed to both surfaces — this
specific disclaimer clears the print-parity bar cleanly.**

**But the check this program's own R4/disclaimer-erosion lineage actually
demands is broader than "does the string appear in JSON and stdout" — it
also requires the *third* surface, `NOTES.md`, to carry it, since that is
the document a future cycle actually cites (Iteration 65's own CHECKPOINT
text: "precisely the section a future citation is most likely to quote").
`NOTES.md` as currently committed (`git log -- NOTES.md`: last touched at
Phase 3, commit `39f0e6b`, frozen *before* Phase 4 ran) has no `## Result`,
`## Learned`, or `## Next` section at all** — I checked with `grep -n "^##
"`: the document ends at `## T1 escape route`, exactly where the
Phase-3-frozen predictions section left it. Every other T28-family
sibling I checked (exp-091, exp-092) has all three post-run sections. This
is not a wording defect in the disclaimer itself — it is a **completeness
defect at the exact structural checkpoint R15's own founding entry
(Iteration 68) named as its forward safeguard**: "a `## Result`-
section-exists check... before any cycle's Phase-4 output is treated as
complete." That check was never applied here. Git confirms Phase 4
completed (`563934a`, "all 56 FDTD calls complete, all house gates PASS")
with no subsequent NOTES.md commit. **This is real and load-bearing for
Phase 5 itself**: this review, and presumably the other six blind
reviews, were handed a NOTES.md that stops at the frozen predictions and
never states results in prose at all — everything past that point had to
be reconstructed from `run_output.txt`/`results.json` directly. The
disclaimer text is correct wherever it appears; it simply does not yet
appear in the one place this program's own prior CHECKPOINT ruled matters
most.

## 2. Does SINGLE-NULL itself need R15-style cross-resolution verification?

**Yes — and I have a specific, cycle-native reason beyond the generic R15
caution Idealization 16 already states.** The SINGLE-NULL verdict rests
on six interior points, all at a single fixed spatial resolution
(`cpl=30`), all corrected to `sigma_max=1/3`. Taken alone, the curve is
genuinely clean: `-4.33e-5 → -6.80e-5 → -1.03e-4 → -1.13e-4 → -1.17e-4 →
-1.17e-4`, a smooth, monotone-then-flattening trough with no sign changes
and no noisy scatter — good evidence *at this resolution* of one real
minimum, not an artifact of under-sampling in angle. Idealization 16
correctly notes this is angular-only, not itself an R15-grade
cross-resolution finding, and I concur with that as the general rule.

What sharpens this from "the standing caution applies" to "this specific
feature is empirically shown fragile" is **item 3's own result in the
identical angular band**: at θ=42.0°, `sigma_max` rescaling alone (a pure
grid-refinement bookkeeping correction, not a new material or a new
angle) flips `delta_scene`'s *sign* — native `+8.04×10⁻⁵` versus
sigma-corrected `-5.81×10⁻⁵` (`delta_scene_sign_match=False`, confirmed
directly from `results.json::item3.per_theta["42.0"]`). That is not a
generic R15 worry — it is a **directly observed instance, this cycle, in
this exact near-null pocket, of the sign of the scored quantity flipping
under a resolution-adjacent numerical correction.** A feature whose sign
already flips under one axis of refinement (the `sigma_max` renormalization
that holds `τ_center` invariant across `cpl`) in the *same* θ-window a
different axis of refinement (`cpl` itself) is being asked to adjudicate
is a textbook R15 hazard, not a hypothetical one. My position: **SINGLE-
NULL should be treated as provisional, not merely "further work would be
nice" but specifically because this cycle already produced direct
evidence of instability in the identical location** — a `cpl=40` check at
41.75°–41.90° is not just R15 hygiene in the abstract, it is the most
directly motivated single follow-up this cycle's own data argues for.

## 3. Independent recomputation (this program's own R4 discipline)

I reproduced two non-trivial figures from scratch, independently of
`run.py`, using only the formulas stated in `NOTES.md`/`phase3_synthesis.md`
and Brent's method / NumPy directly:

**(a) Item 4 — Yee-grid dispersion ratios at `ℓ=A_HALF_APERTURE`.**
Reimplemented `yee_dispersion_k`/`delta_phi_deg` from the stated dispersion
relation `(1/S²)sin²(πS/cpl) = sin²(k·cosθ/2) + sin²(k·sinθ/2)`,
`S=0.99/√2`, solved via `brentq`. Result: **32.106×, 80.218×, 95.792×** at
θ=40.0718°/41.7811°/41.8377° respectively — bit-exact to the reported
32.1×/80.2×/95.8× (and to the Director's own independent third derivation
in `phase3_synthesis.md`). Item 4's CONFIRM verdict (dispersion-alone
REFUTEd by one clean order of magnitude, not the pre-freeze draft's
mistaken two orders) is independently reproduced.

**(b) Item 2 — AUC / Firth logistic fit on the `n=8` `cpl=30` table.**
Reimplemented `firth_logistic` verbatim (Newton-Raphson on the Firth
modified score equation) and the Mann-Whitney `auc` function from the
margin/`Y` pairs listed in `run_output.txt`. Result: `auc(-pos,-neg)=1.0`,
zone `[4.1083, 5.4287]`, `β=[3.76504788, -5.60700572]`, `m₅₀=4.6934`,
converged in 15 iterations — **bit-exact match** to both the frozen
`NOTES.md` prediction and the live `run.py` recomputation. Item 2's base-
table CONFIRM verdict is independently reproduced.

Both checks pass; I found no arithmetic defect in either headline number.

## 4. A new finding: the item-1 "combined curve" comparability note is wrong in the branch that actually fired

`run.py` (lines 577–592) builds a context-only "combined curve,
41.6°–42.0°" for interpreting the SINGLE-NULL question visually. The
*code* correctly branches on which `sigma_max` item 1 actually ran at:
when `sigma_item1 != SIGMA_NATIVE` (the REFUTE branch, which is what
fired), `combined_curve[41.8]`/`combined_curve[42.0]` are populated from
`item3_report[...]["sigma_corrected_delta_scene"]`, **not** from item 5's
native-sigma values — I confirmed this by hand-checking the printed
numbers against `results.json::item3`: `-8.790557e-05` at 41.8° matches
`sigma_corrected_delta_scene`, not `native_delta_scene` (`-1.865127e-05`);
`-5.810166e-05` at 42.0° matches the sigma-corrected value (which is also
the value that carries the sign flip from item 2, above), not the native
`+8.041787e-05`. **The code's data selection is correct and adaptive.**

The printed *label* is not: line 589 hardcodes `"41.6/41.8/42.0 are always
native sigma_max=0.5"` regardless of which branch fired — copied forward
unchanged from `phase1_proposal.md`'s own pre-registered CONFIRM-branch
language (lines 159/522, "all native-`sigma_max`"), never updated for the
REFUTE branch that actually ran. In the branch that fired, only 41.6° is
native; 41.8°/42.0° are sigma-corrected — the opposite of what the printed
note tells a reader. `results.json`'s own `item1.combined_curve_41_6_to_42_0`
carries no comparability annotation at all, so this incorrect claim exists
**only** in `run_output.txt`, uncorrected anywhere in the persisted record.
**Not load-bearing to the SINGLE-NULL verdict itself** (that verdict is
computed only from the six interior points, which are uniformly
sigma-corrected and unaffected by this mislabeling) — but it directly
misstates comparability exactly where Idealization 11 exists to protect
it, in the same family as this program's own R12/R13/R14 "prose doesn't
match what the data actually is" lineage. A same-shift, zero-FDTD fix
(correct the note string to be branch-conditional, and add the missing
comparability flag to `results.json`).

## Verdict: **CONCUR-WITH-GAP(S)**

Every scored, load-bearing verdict I independently checked (Item 4's
dispersion CONFIRM, Item 2's base-table CONFIRM) reproduces bit-exact. The
`r15_disclaimer` text itself is correctly worded and correctly present in
both `results.json` and `run_output.txt`. I found no defect that
overturns Item 1's SINGLE-NULL classification, Item 2's CONFIRM, Item 3's
REFUTE, or Item 4's CONFIRM. The gaps are: (i) `NOTES.md` itself — the
document R15's own founding entry named as needing a structural
"Result-section-exists" check — has no Result/Learned/Next section as
committed, unlike every sibling T28 cycle; (ii) a mislabeled, uncorrected
comparability claim in the item-1 context curve, non-load-bearing but
real, in a place this program's own house rules exist specifically to
police; (iii) SINGLE-NULL itself, while cleanly measured at `cpl=30`, is
not yet cross-resolution-verified, and this cycle's own item-3 sign-flip
in the identical band is concrete evidence — not merely generic caution —
that it should be before being cited as settled.

## Ranked candidate directions — Iteration 71 (MATERIALS perspective)

**Rank 1 — a targeted `cpl=40` resolution check at 41.75°–41.90°
specifically** (not a broad re-sweep). This is the single most directly
motivated test this cycle's own data argues for (§2 above): it discharges
R15's second remaining condition (a `cpl=40` comparator confirming
`cpl=30` is converged, not merely a second fixed resolution) exactly where
the feature under question lives, and is cheap — six points, the same
budget class as this cycle's own item 1.

**Rank 2 — R3-verify (`cpl=30`) the three still-unmeasured original
caution-zone points (36.0°, 38.4°, 38.8°).** Discharges R15's first
remaining condition; this is also the single most-repeated deferred item
on the whole T28 board by a wide margin. I rank it second, not first,
because Rank 1 targets a feature this cycle *newly* showed to be fragile
(the sign flip), while this item extends an already-established zone
construction to points whose classification is not currently in dispute.

**On the framing question — should closing R15's own two discharge
conditions be the program's next priority, now that this sub-thread has
run five consecutive desk/instrument cycles:** yes, conditionally. Both
Rank 1 and Rank 2 are cheap, well-specified, and would let R15 be cited as
genuinely closed for the first time since its own founding — a real,
overdue deliverable. But I would not endorse a *sixth* narrow near-null
zoom-in cycle after these two land, regardless of outcome. **Rank 3 — if
Ranks 1+2 close cleanly (either direction), the next cycle should return
to a standing board debt outside this narrow sub-question** — PHOTONICS'
own grazing-incidence validity check (still the single most-repeated item
on the whole T28 board) or the x-wall wavelength-generality leg (now
seventeen consecutive cycles deferred) — rather than opening a new T28
near-null sub-question. Five consecutive desk/instrument cycles on this
exact upper-crossing thread, however each individually disciplined, is
close to the shape Checkpoint criterion 5 (two consecutive non-advancing
iterations) exists to guard against at the *sub-thread* level even when
each cycle technically advances something; closing R15 cleanly and then
deliberately changing which board item gets attention is the healthier
next step from this seat.
