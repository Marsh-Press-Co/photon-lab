# Phase 5 Review — PHOTONICS

**Cycle: exp-076, Panel Iteration 53 (G40/PAD decorrelation).** Fresh
context, blind to any other Phase-5 review or the red-team audit this
cycle. LOGBOOK.md read in full this seat (RULED OUT R1–R8, ESTABLISHED,
LIVE THREADS T1–T28 in full, T21/T24/T27/T28 read closely, full
Iteration-1-through-53 narrative). Read in full: `phase1_proposal.md`, all
five `phase2_critique_*.md` (including my own seat's independent Phase-2
critique for this cycle, which raised the 600nm even-integer-λ aliasing
concern the Director's brief references), `phase2_redteam_audit.md`,
`phase3_synthesis.md`, `NOTES.md`, `run.py`, `phase4_results.md`,
`results.json`. Independently re-derived, not taken on the record's own
word (R4): the `amp_ratio`/carrier-fit pipeline was re-run directly against
the committed `headline` and `leg750_scored` arrays in `results.json`
(`g0e_amplitude_channel_check.py`'s own `_amp_ratio_recover`/`carrier_fit`),
reproducing `x=0.119366`/`y=0.071616` (600nm) and `x750=0.419868`/
`y750=0.616131` (750nm) bit-exact, plus recovering the fitted carrier
period/R² for all four pairs — a diagnostic the committed record never
persisted (see finding 1, below). `rho_pad_absorb=0.2108` was independently
recomputed from the disclosed `dp_pad=-0.05013°`/`dp_absorb40=+0.13105°`/
`dp_c40_c80=+0.06684°` and matches. Settling gate re-checked: forward
(`STEPS=2800` vs `4200`) passes ~500× inside `THRESH_LOW` at both angles;
geometry congruence (`G40` bit-identical to `C80` in every scene coordinate
except `absorb`) independently confirmed via `results.json::
geometry_congruence`.

## Verdict on this cycle: **PARTIAL**

`PAD_TIED` is a real, disciplined, honestly-reported finding — the
instrument build is sound, the Phase-2 mandatory-fix docket (all 8 items,
zero overridden) closed two genuine defects (Attack 1's gappy/non-exclusive
bands, Attack 2's overclaimed `rho_pad_absorb` "interaction" language)
before they could reach a frozen verdict, and the settling precondition my
own charter has no special claim over but which bears directly on whether
`C_empty(θ)` at this new geometry is a trustworthy angular reading at all
passed cleanly with wide margin. This advances the logbook: it is new,
falsifiable, pre-registered information that narrows what a future T28
mechanism must explain (it must now also explain a real `PAD`/domain-
geometry sensitivity, not just an `ABSORB`-depth dependence). It is not
PROMISING because T28's own substantive question — the ~2.84° periodicity's
physical origin — remains exactly where it was, and because (see below) I
find the cycle's own advisory 750nm leg to be *less* trustworthy, on optical
grounds, than its "advisory, narrow-window, not decisive" framing already
discloses — a further methodological gap, not resolved this cycle, that
should be named explicitly rather than left implicit in a hedge phrase.

## Does the 600nm headline hold up under my own scrutiny?

Yes, on the numbers as measured. Three checks specific to my charter (is
the optical response coherent across angle and wavelength):

1. **`G40` and `C40`'s angular fingerprints are consistent with sharing the
   same `ABSORB=40` boundary.** Both series in `results.json::headline`
   oscillate with the same sign pattern across the 31-point sweep (peak
   near θ≈37.2–37.4°, trough near θ≈40.4–40.6° in both `C40` and `G40`) —
   exactly what should happen if the boundary depth, not the domain padding,
   sets the dominant angular structure at fixed `ABSORB`, with `PAD`
   contributing a real but second-order shift on top. This is a coherent
   optical picture, not a discontinuity between the two series.
2. **The 600nm carrier fits land on-target.** I independently re-fit both
   new pairs' carriers: `PAIR_PAD` → `T_mean_deg=2.407°` (r²=0.438),
   `PAIR_ABSORB40` → `T_mean_deg=2.457°` (r²=0.432) — both sit inside T28's
   own established per-config free-period band (2.44°–2.84°, exp-070/071),
   not near T21's separately-characterized 1.9608° edge-diffraction fringe.
   The weak r² (~0.43) is not new or alarming on its own — it matches this
   sub-thread's own historical fit quality (R²≈0.26–0.44 has been typical
   since exp-070) — but it does mean neither `amp_ratio` reading carries an
   error bar, a gap PHOTONICS' own Phase-2 critique already named and that
   remains true of the frozen headline.
3. **Settling and geometry are clean.** `G40`'s previously-untested
   (thin-boundary × large-domain) combination settles at `STEPS=2800` with
   ~500× margin — a real, previously-uncharacterized gap (T27 never tested
   this cell) that turned out benign, which is itself useful information for
   this sub-thread's own settling record.

I do not find an inconsistency in the 600nm headline `PAD_TIED` reading
itself. My concern is entirely about the 750nm leg used to stress-test it.

## The 750nm leg: my own reading is that it is a *weaker*, not stronger,
## challenge to the 600nm headline than `phase4_results.md`'s "genuinely
## informative tension" framing suggests — for a reason beyond aliasing

`phase4_results.md` frames the 750nm ordering flip (`x750=0.420 < y750=
0.616`, opposite the 600nm `x>y`) as "the kind of signal PHOTONICS' original
aliasing attack predicted could exist" and correctly labels it advisory/
non-decisive. That framing is honest as far as it goes, but it stops one
step short of diagnosing *why* the leg is unreliable, and my own
independent re-fit of the leg750 carrier finds a second, distinct defect
that neither aliasing (already disclosed) nor "narrow window" (already
disclosed as a bare fact) fully captures:

**The 750nm free-period search locks onto a period that matches neither
established periodicity in this sub-thread.** Re-running `carrier_fit`
directly on `results.json::leg750_scored`'s own committed arrays: `PAIR_PAD`
→ `T_mean_deg=1.780°` (r²=0.511), `PAIR_ABSORB40` → `T_mean_deg=1.761°`
(r²=0.584). This is *not* T28's own established periodicity (2.44°–2.84°,
confirmed on-target at 600nm above) — it is also not T21's own
edge-diffraction fringe model's predicted period AT 750nm specifically
(P(θ)=λ/(A·cosθ) scales linearly with λ, so T21 predicts ≈2.4° at 750nm,
per LOGBOOK Iteration 18/19's own committed model — not 1.78°). The 750nm
leg's carrier is landing on a third, unexplained, weakly-fit (r²≈0.51–0.58,
versus the already-weak 0.43 at 600nm) periodicity that this cycle's own
record never surfaces, because `score_leg750()` discards the fitted
`T_mean_deg`/r² after computing `amp_ratio` — they are not persisted
anywhere in `results.json`. This is a genuine, previously-undisclosed
record gap: the one diagnostic that would let a reader judge whether the
750nm `amp_ratio` figures are measuring "the same thing" as the 600nm
headline was computed transiently and thrown away.

**Why this matters more than the window-width disclosure alone conveys.**
The leg750 window is 3° wide; a period of ~1.78° means the free-period
search is being asked to resolve a carrier from barely 1.7 cycles of data
at 16 points — a substantially worse-conditioned problem than the already-
marginal 600nm window PHOTONICS' own Phase-2 critique flagged (`cond9≈478–
529`, `VIF_Rq≈31–37`, itself a 6°/31-point window fitting a ~2.5° period,
i.e. ~2.4 cycles). The leg750 window is conditioned for *fewer* cycles of
its own recovered signal than the headline window already was, and the
recovered period itself is shorter and off-target relative to both
plausible physical candidates. Compounding this: the R6/`G0-e` synthetic
ground-truth check this cycle ran (Phase 1, `g0e_amplitude_channel_check.py`)
injected its matched-period case at `P_true=2.49°` on the *full 31-point,
6° window* — it never validated the pipeline's recovery behavior at a
3°-window/16-point/short-recovered-period operating point resembling
leg750's actual regime. The `G0-e OVERALL: PASS` therefore licenses trust
in the 600nm headline's noiseless-bias behavior; it does not, by
construction, license the same trust in the 750nm leg's numbers.

**My own reading of both legs' raw numbers, per the Director's brief:**
this does *not* reverse the `PAD_TIED` 600nm headline (nothing in the 750nm
leg is powered to make that claim either way), and it does not, on
reflection, straightforwardly *weaken* PAD_TIED's own evidentiary standing
either (the headline is measured on its own well-targeted, if noisy,
carrier). What it does is **remove most of the 750nm leg's own standing as
an independent check** — a leg whose carrier fit lands on an unexplained
third periodicity at low r² on a window too narrow to resolve it is not
strong evidence of anything, in either direction, about wavelength-
generality. `phase4_results.md`'s "genuinely informative tension" language
slightly overstates what this leg actually shows; "a disclosed, unresolved
discrepancy whose own instrument is not powered to adjudicate it" is the
more defensible reading. This is not a reversal of the cycle's verdict —
Idealization 1 and the docket's own advisory/`decisive=False` labeling
already correctly forbid citing this cycle as wavelength-general — but the
specific *reason* is sharper and more actionable than "narrow window" alone
conveys, and belongs in the permanent record so a future reader doesn't
mistake the ordering flip for a clean, well-measured contradiction.

## Cheapest follow-up that would resolve the aliasing-vs-real-effect question

**Re-run the 750nm (or 450nm) leg at the FULL 6°/31-point `DENSE_ANGLES`
window**, not the 3°/16-point `block_leg750` subset — this is the single
change that fixes both the window-conditioning problem and gives the
free-period search enough cycles to land on-target if the true periodicity
is genuinely wavelength-independent (as T28's own physical mechanism, still
unidentified, would presumably require it to be) or genuinely
wavelength-dependent (which would itself be new, real information about
T28). Marginal cost: 31 new FDTD calls for `G40` (`C40`/`C80` at 750nm and
full-window already exist for neither — verify before running, but even in
the worst case this is the same ~31-call order as this cycle's own core
budget). Persist `T_mean_deg`/r² for every carrier fit in `results.json`
going forward (a one-line fix) so this diagnosis is available without
re-deriving it by hand next time.

## My own top-3 ranked candidate directions for Iteration 54

1. **Full-width, non-aliased leg for `G40` at a second wavelength (450nm or
   750nm), reusing `DENSE_ANGLES`'s exact 31-point/6° window, not
   `block_leg750`'s 3° subset.** (~31 FDTD calls, zero new `lab/` machinery
   — reuses this cycle's own `_one_run`/`carrier_fit` chain verbatim.) This
   is the item this cycle's own Idealization 1 and docket item 5 already
   name as required before any wavelength-general citation of `PAD_TIED`,
   and my own finding above sharpens *why* the existing 750nm leg cannot
   substitute for it: a properly-powered window is needed to tell whether
   the ordering flip is real wavelength dependence or an artifact of an
   under-resolved carrier fit. Persist the fitted `T_mean_deg`/r² in
   `results.json` for both new legs (cheap, closes the record gap named
   above).
2. **Zero-FDTD, same-shift desk check: re-score the already-collected
   `leg750_scored` data under a FIXED carrier matched to the 600nm-
   established ~2.5° periodicity, instead of `carrier_fit`'s free-period
   re-search.** This directly tests whether the 750nm ordering flip
   survives when the carrier is not allowed to wander onto the
   short-period, low-r² alternative my own re-fit found — if `x750`/`y750`
   under a fixed, physically-motivated period agree in sign with the 600nm
   headline, that is real evidence the free-period search (not the
   underlying physics) drove the flip; if the flip survives a fixed-period
   re-score too, that is stronger, not weaker, evidence of genuine
   wavelength dependence. Costs nothing beyond a script re-using
   `design_matrix()` at a supplied `(T_x, psi)` instead of `carrier_fit`'s
   own search — a natural, cheap companion to run before committing FDTD
   budget to item 1.
3. **A 2–4 call cpl 20→30 R3 resolution check on `G40`'s own dominant
   `PAIR_PAD` reading**, at its peak/trough angles in the 600nm dense
   window (θ≈37.2°/40.6°, the extrema of the `x` signal). `PAD_TIED`'s
   headline (`x=0.119`, `HIGH`) is now the single largest, most
   consequential unrefuted reading this sub-thread has produced since T27's
   own settling closure, and Idealization 6 explicitly declines any
   resolution check this cycle. Given this program's own precedent that a
   near-field/boundary-construction effect can grow, not just confirm or
   vanish, under refinement (T10's original finding, later mostly — not
   fully — explained away; T11's box-ledger R3 anomaly), a cheap
   grid-convergence check on the specific reading that now drives five
   iterations' worth of re-reading is warranted before `PAD_TIED` is cited
   as a converged optical result rather than a native-resolution one.

## Flags for the Director's LOGBOOK.md/PLAN.md update

- **A record gap, not a numeric error**: the 750nm leg's fitted carrier
  period and R² (`T_mean_deg≈1.78°`/`1.76°`, r²≈0.51/0.58 — landing on
  neither T28's own established periodicity nor T21's own model's 750nm
  prediction) were computed by `score_leg750()`/`_amp_ratio_recover()` but
  never persisted to `results.json`. Recommend a one-line fix (return and
  store `diag_x`/`diag_y`, already computed, currently discarded) for any
  future leg at any wavelength — this diagnostic is exactly what let this
  review distinguish "a genuine wavelength effect" from "a carrier fit that
  wandered off-target on an under-resolved window," and it should not have
  to be re-derived by hand each time.
- **A sharper reading than `phase4_results.md`'s own prose offers**: the
  750nm leg's "genuinely informative tension, not decisive" framing is
  accurate as a hedge but under-explains itself. My own re-derivation shows
  the leg's own instrument (a free-period carrier fit on a 3°/16-point
  window) is landing on an unexplained, weakly-fit third periodicity, not
  merely "too narrow to be decisive" in the abstract. Recommend the LOGBOOK
  entry for this cycle state the specific diagnosis (carrier lands off
  T28's/T21's established bands, r²≈0.5, window ≈1.7 recovered periods)
  rather than only "advisory, narrow-window" — this is the information a
  future reader needs to correctly weight the 750nm leg against the 600nm
  headline, and to correctly scope Iteration 54's item 1 (above) as
  resolving a diagnosed defect, not merely widening a window.
- **No error found in the 600nm headline, the settling gate, the geometry
  congruence, or the `G0-e` recovery check** — all independently
  re-verified against `results.json`/the committed scripts and confirmed
  bit-exact or within stated tolerance. `PAD_TIED` stands on its own 600nm
  evidence as reported.
- **Concur with MATERIALS' Phase-2 caveat as carried through**: `ABSORB`
  and `PAD` are both pure numerical FDTD boundary/domain-construction
  parameters; nothing in my own re-analysis treats one as more "real" than
  the other, and `PAD_TIED`'s correction to five iterations of prior
  `ABSORB`-series claims should continue to carry that caveat forward
  unchanged.

## Summary for the closing message

Verdict: **PARTIAL** — `PAD_TIED` is a real, honestly-scored, load-bearing
finding at 600nm that I could not fault on optical-response grounds; my own
independent re-fit of the 750nm advisory leg finds it is *less* reliable
than its own "advisory, narrow-window" label conveys (a free-period carrier
fit landing on an unexplained ~1.78° periodicity, r²≈0.5, on a window
barely wider than that period), which neither reverses nor confirms the
600nm headline — it mainly shows the 750nm leg is not yet powered to
adjudicate wavelength-generality either way. Top pick for Iteration 54: a
full-width (31-point/6°), non-aliased second-wavelength leg for `G40`,
paired with a zero-cost fixed-carrier re-score of the already-collected
750nm data to separate a genuine wavelength effect from a free-period-fit
artifact before spending the FDTD budget.
