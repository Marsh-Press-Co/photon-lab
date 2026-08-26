# Phase 5 Review — VISION SCIENCE

**Panel Iteration 53, exp-076 (T28 G40/`PAD` decorrelation). Fresh
sub-agent, blind to all other Phase-5 reviews and the Red Team final
audit.** Charter: human perceptual limits — contrast thresholds, luminance
edge detection, spectral sensitivity, adaptation, temporal sensitivity;
central question: what would make a human eye FAIL to register something
physically present; duty: pin numeric thresholds, with sources, BEFORE any
run that scores against them.

Read in full before writing this review: `PANEL.md`; `LOGBOOK.md`
(RULED OUT R1–R8; ESTABLISHED; every LIVE THREAD, T1–T28, in full, with
T2, T16, T20, T21, T24, T27, T28 read closely; Iteration 1's original
threshold pinning and Iteration 42/exp-065's own settling-gap record);
`phase1_proposal.md`, all five `phase2_critique_*.md`,
`phase2_redteam_audit.md`, `phase3_synthesis.md`, `NOTES.md`, `run.py`,
`phase4_results.md`, `results.json` (independently re-derived from the
committed arrays, not taken from prose — see §1).

---

## 1. R4 duty: the settling precondition, independently re-verified

Constraint 3 is not engaged this cycle (§3 of the proposal, correctly —
this is instrument/model-fidelity work on the `C_empty(θ)` boundary
channel, not a mechanism scored against a perceptual threshold), so my
charter's "pin thresholds before any run that scores against them" duty
applies here as a verification duty on the one perceptual-adjacent
instrument gate this cycle actually ran: the settling precondition.

Pulled `results.json::settling_gate` directly, not from `phase4_results.md`'s
prose:

```
amp_ref    = 0.0052452   (= amp_ratio(C40,C80)'s own fitted carrier amplitude)
thresh_low = 0.0497619   (= 0.3 x amp_ratio(C40,C80), the smallest live band edge)
forward.shift_39 = 5.427e-07   frac_39 = 1.035e-04   passed = true
forward.shift_40 = 3.919e-07   frac_40 = 7.472e-05   passed = true
```

`frac_39` clears the bar by **481×**; `frac_40` by **666×**. Both numbers
match `phase4_results.md`'s "~500× inside" claim and its own rounded
`0.0001`/`0.0001` — verified, not merely re-stated. This is a genuinely
wide margin, not a borderline pass dressed up as clean.

This closes the specific gap raised at this cycle's own Phase 2 by both
ELECTROMAGNETISM (forward-settling argument: `G40` decouples boundary
thickness from domain size, a combination this program had never
settling-tested) and VISION SCIENCE (citation-provenance argument: `G40`
had been run in FDTD exactly once before, at `STEPS=1400`, never at 2800).
Both concerns were real — this program's own T27 thread exists precisely
because an analogous "established floor" citation-by-inheritance turned
out to be wrong by ~60–74% at other geometries (Iteration 42/exp-065, my
own prior lead cycle) — and here the check was actually run rather than
argued past (R8's own standard, cleanly honored). The backward differential
(`STEPS=1400` vs `2800`, disclosed-only) moved `C_empty` by 61.7%/64.0% at
θ=39°/40° — large, consistent with T27's general finding, and correctly
never used as scored input. **Verdict on this specific duty: cleanly
discharged.** I have no outstanding settling concern on `G40`'s own
geometry for the two tested angles.

One residual, non-blocking note: the forward leg was checked at exactly
θ∈{39°,40°}, two of the 31 dense-sweep angles (plus 16 more at 750nm).
Settling (ring-down time of the domain's own absorbing-boundary echo) is a
geometry property, not an angle-dependent one in this instrument's physics
(EM's own Phase-2 framing), so I do not read this as a live gap — but it
is worth noting explicitly, since it is the same "checked at N points,
generalized to all" shape T21/T27 have both previously found real
exceptions to (the fringe *itself* is angle-dependent even when its
*settling* is not).

## 2. Does `phase4_results.md`'s prose conflate `amp_ratio`/`delta_P_obs`/`rho_pad_absorb` with a perceptual quantity?

Checked directly, not by impression: `grep -in "contrast\|C_thr\|weber\|
perceptual\|photopic\|scotopic\|GATE_HARD" phase4_results.md NOTES.md
run.py` returns **zero matches** across all three files. The prose is
careful throughout: "PAD_TIED... confound NOT relieved," "envelope-
amplitude mismatch," "pure numerical domain-construction parameters"
(MATERIALS' caveat, carried verbatim into every outcome) — never once
dressed up as a silhouette contrast, a detection statement, or anything a
human eye could register. This cycle's own §3 statement ("T1 route N/A")
and the outcome table's own closing line ("None of the five outcomes
constitutes a RESOLVED/CONFIRMED-class significance claim... unaffected by
this rewrite") hold. **No conflation found in the actual committed text.**

But there is a real, load-bearing **latent** risk the current text does
not close, and it is not new — it is my own charter's own Phase-2 finding
from this exact cycle, and it did not survive into the mandatory-fix
docket:

- `amp` — the carrier amplitude every `amp_ratio` value is *normalized
  by* — is itself a fitted `C_empty` amplitude. Independently recomputed
  from `results.json::headline.pair_pad.amplitude` and
  `pair_absorb40.amplitude`: **0.005155 / 0.005514**, both within 10% of
  VISION's own pinned lab bar `C_thr = 0.005` (Blackwell 1946, JOSA
  36:624; T2, LOGBOOK.md, frozen Iteration 1). This is a coincidence of
  what this construction happens to measure at this geometry — `C_empty`
  is a vacuum field-ratio reading, not a Weber contrast on any object —
  but it means a reader who encounters `x = amp_ratio(PAIR_PAD) = 0.119,
  bin = HIGH` without tracing the normalization back to `run.py` could
  plausibly misread "0.119" as "24× the lab detection bar," i.e. as a
  *perceptual* magnitude, when it is a *relative-to-a-vacuum-field-ratio*
  magnitude with no perceptual referent at all — exactly the failure shape
  exp-072's own Idealization 8 ("`C_empty` is a dimensionless field ratio,
  not a Michelson/Weber perceptual contrast... never photometric") was
  written to block, in that cycle's own record, at VISION's own prior
  insistence.
- I raised this at this cycle's own Phase 2 (`phase2_critique_vision.md`,
  "Secondary finding") and proposed a one-line fix: carry an
  Idealization-8-equivalent disclaimer forward into this cycle's own
  idealizations list. **Checked against the actual disposition record**:
  Red Team's audit (`phase2_redteam_audit.md`) adopted my *sharpest
  attack* (the settling differential, folded into EM's fix, docket item
  4) but its disposition table and numbered attacks (1–6) never engage
  the secondary finding at all — it is not adopted, not modified, and not
  explicitly rejected with a stated reason. `phase3_synthesis.md`'s
  acceptance table (§1) lists eight docket items tracing to five critiques
  plus Red Team's own six attacks; none of them is this one. NOTES.md's
  ten idealizations (§Idealizations) do not contain it either — confirmed
  by direct read, not by absence-of-memory (I have none of this cycle's
  own memory to trust or distrust; this is a fresh read of the committed
  files).

This is not a bug and does not change PAD_TIED, and today's actual prose
is clean by direct check (above) — so this is not gating and does not
move my verdict. But it is a genuine, disclosed-then-dropped gap, in
exactly my charter's own territory, and it is cheap to close: one sentence,
already drafted at this cycle's own Phase 2, never adopted. I flag it for
the Director's record below rather than let it silently re-surface as a
"why wasn't this caught" finding at a future Phase 5, the way this exact
sub-thread's own R4/R8 history repeatedly shows happens to disclosed-but-
unclosed gaps (Iterations 49/50/52).

## 3. Any remaining perceptual/measurement-fidelity concern, given the settling gate passed cleanly?

Two, both secondary to §1/§2 above, neither gating:

1. **The `amp`/`C_thr` coincidence (§2) is itself a measurement-fidelity
   fact worth stating plainly**: this instrument's *typical vacuum-floor
   carrier amplitude*, at this exact bench geometry (r_out=78-cell family,
   A=752, 600nm), sits within a factor of ~1.0–1.1 of the smallest
   perceptual threshold this whole program has ever pinned. That is a
   coincidence of scale, not causation — nothing here suggests the eye's
   threshold and this FDTD boundary's own diffraction/ring-down floor
   share a mechanism — but it means any future cycle that reuses this
   exact normalization convention (`amp_ratio`, or any sibling built the
   same way) for a quantity that DOES touch a real object should re-state
   the disclaimer explicitly rather than assume the prior cycle's silence
   on it means the risk was checked and cleared. It was checked (by me,
   this cycle) and NOT cleared — only left undecided.
2. **`rho_pad_absorb`'s downgrade (docket item 2) is correctly applied in
   this cycle's own text**, and I independently confirm it should stay
   downgraded: `results.json::rho_pad_absorb = 0.2108`, well below the
   `≥1.00` bar that (under the original, now-superseded language) would
   have been read as "real evidence... interaction exists." Nothing in my
   own charter's territory adds to Red Team's Attack 2 finding here — the
   uncalibrated, `R_q`-derived nature of this diagnostic is an
   ELECTROMAGNETISM/statistics-machinery question, correctly resolved
   already. I mention it only to confirm I checked it and found no
   additional perceptual-adjacent risk in its current (disclosed-only,
   non-gating) framing.

## 4. Does PAD_TIED bear on Vision Science's own domain?

This is the substantive question, and the honest answer is two-layered.

**Layer 1 — T28 was never a candidate witness-observable phenomenon, and
PAD_TIED does not change that; if anything it is the cleanest confirmation
yet that it structurally cannot be one.** Every config in this cycle's
own scored channel (`C40`, `C80`, `G40`) is an **empty scene** — no
absorber, no PEC, no article of any kind is loaded (confirmed directly:
`run.py`'s `_one_run`/`_c_empty` calls, reused verbatim from exp-069,
compute the vacuum reading only). `PAD` is a pure FDTD domain-truncation
parameter — how much extra vacuum buffer separates the graded absorbing
boundary from the scored measurement window. A real flashlight beam
crossing real open air has no "PAD": there is no finite-domain edge for a
photon in physical space to reflect off or settle around. A signal that
tracks `PAD` at least as strongly as it tracks `ABSORB` (this cycle's own
headline, `x=0.119 HIGH` vs `y=0.072 MED`) is, from a perceptual
standpoint, about as unambiguous a "this is a property of the simulation's
own bookkeeping, not of any coating, material, or scene a human eye could
ever encounter" signature as this program could produce. So: no, a real,
perceptible witness-relevant phenomenon could not plausibly track a
"padding/domain-geometry" axis — there is no physical analogue of `PAD`
for it to track. This is not a new caution about T28 specifically; it is
the same disposition MATERIALS' own docket-item-7 caveat states for
`ABSORB` too ("both pure numerical domain-construction parameters; neither
carries more physical standing than the other") — PAD_TIED sharpens that
caveat's practical stakes rather than introducing a new one.

**Layer 2 — the actionable stake for my charter is not "is T28 itself a
phenomenon" (structurally, it cannot be — T1 route N/A was correct from
this thread's opening cycle) but "how much residual, uncharacterized noise
does this same channel inject into REAL constraint-3 verdicts elsewhere in
this program."** `C_empty(θ)`, the quantity this whole T20→T21→T24→T27→T28
lineage characterizes, is not a side-channel curiosity — it is a
component of `lab/ambient.py`'s own per-angle empty-scene floor, the exact
instrument whose `FALLBACK_ANGLES` aggregate has, since Iteration 1,
produced every real constraint-3 `C` value this program has ever scored
against my own charter's `C_thr` bars (T20/T21's own text: "inside
`FALLBACK_ANGLES`, feeding Block ARTICLE's own N9 aggregate directly").
T16 already established, independently of T28, that this channel's own
angular-sampling and domain-construction uncertainty is "comparable to or
larger than the margins several of this program's headline citations rest
on" — and named this program's **only-ever constraint-3 PASS**
(exp-032/033's σ(I) OFF-state reading) as one of the citations at risk.
PAD_TIED is now a **third, independently-confirmed driver** of that same
channel's own irreducible floor uncertainty, alongside T21's edge-
diffraction fringe (mechanism identified, magnitude not fully validated)
and T27's settling-transient (mechanism identified and closed for the
tested geometries). Concretely: a domain-padding choice alone — nothing
to do with resolution, settling, or angle sampling, all already-known
uncertainty sources — can move this channel's own signal by an amount
**~24× VISION's own lab bar** (`x=0.119` vs `C_thr=0.005`) at a fixed
`ABSORB` depth. That is a genuinely new number for "how much can a pure
domain-construction choice move this instrument's floor," and it belongs
in the same accounting T16 already keeps.

**So: is this "exactly the kind of finding that should make the panel
more skeptical T28 is telling us anything about human-observable
phenomena at all"? Yes and no, and the distinction matters.** No — because
T28 was never scored as a phenomenon candidate, so there is no witness-
observable claim here to become more or less skeptical of; the skepticism
this finding earns was already fully priced in at this thread's opening
(instrument-fidelity class, constraint 3 disengaged, correctly, every
cycle since Iteration 46). Yes — in the narrower, more useful sense that
PAD_TIED should sharpen, not soften, the panel's institutional caution
(T16's own standing finding) about how much of this program's REAL,
witness-relevant constraint-3 margin claims rest on a floor now shown to
be sensitive to a construction choice with zero physical counterpart. That
caution was already live; this cycle adds a concrete magnitude to it and
a concrete new mechanism (padding, not just angle-sampling or settling)
to the list of things that can move it.

## Verdict: **PARTIAL**

Clean, well-verified instrument work: the settling precondition I and
ELECTROMAGNETISM both flagged at Phase 2 was actually run, not argued
past, and passed with a wide, independently-confirmed margin (§1); the
prose stays disciplined and free of perceptual conflation as committed
(§2, first half); PAD_TIED is a real, load-bearing, honestly-reported
finding in the less convenient direction, correctly hedged by its own
750nm ordering-flip disclosure and its aliasing caveat. Not PROMISING —
constraint 3 is untouched by design, and T28's own substantive mechanism
question is, by this cycle's own honest accounting, unresolved. Not RULED
OUT — nothing here forecloses a future mechanism-class question; if
anything it narrows what a future mechanism must explain. My own
charter's specific duty (§1) is discharged cleanly; my charter's specific
disclosed gap (§2, second half) was raised and then dropped without
adjudication, which is itself the finding I am flagging forward, not a
reason to downgrade the cycle's verdict — Red Team's audit was thorough
on the six attacks it did pursue, and non-adoption of a labeled
"secondary, not sharpest" finding is a defensible editorial choice, not a
violation, though it leaves a cheap fix unclosed.

## Ranked top-3 candidate directions for Iteration 54 (my own charter's standpoint)

1. **Close the disclosed-but-dropped conflation-disclaimer gap (§2), and
   use it as the occasion to fold PAD_TIED into T16's own instrument-floor
   accounting.** Two cheap, zero-FDTD, desk-only items: (a) add the
   Idealization-8-equivalent sentence for `amp_ratio`/`delta_P_obs`/
   `rho_pad_absorb`/`C_empty(θ)` in this exact instrument family, closing
   the gap raised at this cycle's own Phase 2 and never adjudicated; (b) an
   explicit LOGBOOK.md cross-reference from T28 to T16, recording PAD_TIED
   as T16's third independently-confirmed floor-sensitivity driver (after
   T21's fringe and T27's settling-transient) and re-stating, with this
   cycle's own `x=0.119`/`C_thr=0.005` numbers attached, that no near-
   threshold constraint-3 citation on this channel should be read as
   floor-clean without disclosing all three.
2. **Test whether the just-discovered PAD-sensitivity survives once a
   real article is loaded** — the actual charter-relevant question this
   cycle's empty-scene-only scope could not reach. Build the G40 analogue
   with `graded_black_shell` (or an `off_pass`/`off_bracket`-style
   near-null σ(I) article) present, at the same 36°–42° dense window and
   settled `STEPS=2800`, and score the SAME `amp_ratio` decomposition on
   the loaded series. Two possible outcomes, both informative: the
   PAD-sensitivity is a pure background systematic that cancels in the
   object-minus-flank subtraction real constraint-3 scoring performs (good
   news, closes the practical risk), or it rides through into the loaded
   reading (bad news — every existing PASS/MARGINAL/FAIL call at
   `FALLBACK_ANGLES`-adjacent geometries needs a fresh look, this time with
   a named, quantified PAD-construction confound, not just T16's general
   caution).
3. **Complete the still-outstanding full-width (6°/31-point) non-aliased
   leg** this cycle's own text (and PHOTONICS' Phase-2 attack) already
   flags as required before any wavelength-general citation of PAD_TIED —
   the 750nm advisory leg's ordering flip (`x<y` at 750nm vs `x>y` at
   600nm, `phase4_results.md`) is a genuinely unresolved tension, and if a
   future cycle ever cites this channel's floor behavior against a real
   3-λ constraint-3 sweep (the program's own standing broadband
   requirement), a single-wavelength, possibly-aliased headline is not
   sufficient grounding.

## Flags for the Director's LOGBOOK.md / PLAN.md update

- **Settling precondition (docket item 4): PASSED cleanly, independently
  re-verified against `results.json::settling_gate` directly (§1 above) —
  `frac_39=1.035e-04`, `frac_40=7.472e-05`, both ~500–666× inside
  `THRESH_LOW=0.0498`. This closes the specific gap both EM and I raised
  at this cycle's own Phase 2; log it as a genuine, checked-not-assumed
  settling result for `G40`'s own (previously-untested) thin-boundary/
  large-domain geometry, in the same spirit T27's own Iteration-43 closure
  was logged.
- **A disclosed Phase-2 finding (mine, this cycle) — the `amp`/`C_thr`
  numerical coincidence and its proposed one-line idealization fix — was
  not adopted, modified, or explicitly rejected by Red Team's Phase-2
  audit or Phase 3's synthesis; it simply does not appear in either
  document's disposition tables.** Not a violation (it was labeled
  "secondary, not the sharpest attack" in my own critique, and Red Team is
  not obligated to adopt every secondary finding) and does not change
  PAD_TIED or any frozen prediction — but it is a real, still-open,
  cheap-to-close gap in exactly my charter's own territory, and I recommend
  it be logged explicitly (not silently absorbed) so a future Phase 5 does
  not have to re-discover it from scratch, matching this program's own
  R4/R8 discipline against disclosed-then-dropped gaps.
- **PAD_TIED should be read into T16's own live-thread record, explicitly,
  as a third confirmed driver of the ambient-contrast instrument's floor
  uncertainty** (alongside T21's fringe and T27's settling-transient) —
  the magnitude (`x=0.119`, ~24× VISION's own lab bar `C_thr=0.005`)
  belongs in the same accounting T16 already keeps for how much of this
  program's headline constraint-3 margins are floor noise, not signal.
