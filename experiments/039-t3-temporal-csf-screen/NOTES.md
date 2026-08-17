# exp-039 — The T3 Temporal-CSF Screen

Panel Iteration 16 · Runner: cloud panel shift · Lead: ELECTROMAGNETISM (rotation)

Full seven-seat cycle: Phase 1 proposal (ELECTROMAGNETISM) → 5 blind parallel
critiques (PHOTONICS, MATERIALS, THERMODYNAMICS, QUANTUM OPTICS, VISION
SCIENCE — unanimous **support-with-changes**, five non-overlapping fixes) →
Red Team last with everything (verdict: **proceed-with-mandatory-fixes**, 8
numbered attacks including one load-bearing independent catch none of the
five blind seats found) → Phase 3 synthesis (this file) → predictions
committed here, before any run → Phase 4 build + run. Verbatim panel
transcript: this shift's session record (LOGBOOK.md Iteration 16 carries the
full text).

## Pre-flight (this shift)

Fresh container, deps installed per the recorded wrinkle (numpy/scipy/
matplotlib/pillow/autograd/fdtd via pip, then `ceviche --no-deps`). Bench
trust suite 41/41 green (`--only 12346789`), stage 12 (kinetics) 5/5 green,
both matching Iteration 15's committed record to the printed digit — Iteration
15 fully closed out on arrival (predictions/results/LOGBOOK/PLAN/SESSION_LOG
all present and consistent; no partial state found).

## Hypothesis

Iteration 15 closed with a Red-Team-adjudicated, ranked top-3 queue for
Iteration 16 (LOGBOOK.md Iteration 15 close). Priority #1 — "build stage-10's
T3 temporal-contrast instrument, sourced" — is the single most overdue item
on the program's books (deferred at Iterations 13, 14, 15's own close) and
retires the root cause of a documented pattern: Phase 5 has had to catch-and-
correct a "T3-provisional" scoring-cap violation on three consecutive
committed iterations (13, 14, 15). ELECTROMAGNETISM (this cycle's rotation
lead) proposed executing priority #1, per program precedent that the rotation
lead defaults to the ranked-#1 queue item regardless of which seat originally
named it (e.g. Iteration 14, PHOTONICS led a priority that was not
PHOTONICS' own pick), unless a structural blocker forces a deviation
(Iteration 15's own precedent). No such blocker was found this cycle:
WebSearch (unlike T18's WebFetch egress block) works, and prior literature-
check cycles (exp-036, exp-037) already established WebSearch-grounded
sourcing as this program's working evidentiary tier.

Pre-registered hypothesis: (a) exp-038's kinetics kernel is, for constant
(k_f,k_r), algebraically a single-pole linear relaxation with a well-defined
corner frequency f_c=(k_f+k_r)/(2π), independently re-derivable and
identity-checkable against the already-validated `kinetics.tau_exact`; (b)
screening f_c against sourced temporal-CSF landmarks, separately for
photopic and scotopic regimes, gives a falsifiable, necessary-not-sufficient
timing pre-screen for T3 (the constraint-3/4 interaction: does the switching
TRANSIENT itself, not just the two end states, create a detectable temporal
edge); (c) the photopic and scotopic regimes may pull in opposite directions
for exp-038's slow-relaxation hosts (D, E) — a genuinely new wrinkle in T1's
bookkeeping if confirmed.

## Phase 1 — Proposal (ELECTROMAGNETISM, abridged)

Full verbatim: this shift's session record. Proposed `lab/temporal_csf.py` +
suite stage 13 (pole-identity gate against `kinetics.tau_exact`, ≤1e-12;
classifier self-consistency gate; anchor-value regression gate), reading
exp-038's own (k_f,k_r) grid's relaxation pole f_c and classifying it against
pinned photopic (Kelly 1961; de Lange 1958; Ferry-Porter) and scotopic
(de Lange 1958; Hecht & Verrijp 1933) temporal-CSF landmark frequencies —
low corner, peak, upper cutoff/CFF. Headline predicted finding (P-EM-5, as
originally drafted): "every single Host D and Host E grid point (all 10)
classifies `in_passband` under scotopic landmarks" — the load-bearing,
program-relevant claim, contrasted against P-EM-4's photopic reading (9 of
10 points sub_passband/favorable). Explicitly scoped as timing-only, no
amplitude, not a scored constraint-3/4 verdict; T18-disclosed (WebFetch still
blocked, landmarks are WebSearch-snippet-sourced, order-of-magnitude).

## Phase 2 — Critique (five blind, then Red Team) — summary

All five blind seats independently returned **support-with-changes**, each
with a distinct, non-overlapping sharpest attack:

- **PHOTONICS**: the cited de Lange/Kelly curves are ACHROMATIC (luminance)
  TCSF. A hysteretic-σ(I) switch (spiropyran-class) changes absorption
  *spectrum shape*, not just amplitude — if the transition is spectrally
  narrowband (chromatic), a materially lower-bandwidth chromatic TCSF would
  apply instead, potentially flipping several "favorable" classifications.
  No host-specific spectral data exists to resolve this either way this
  cycle. Required an explicit disclosure of this unresolved gap.
- **MATERIALS**: P-EM-5's headline finding screens Host D (r=1) and Host E
  (all r) — points already independently tagged UNOBTANIUM-WITH-PARAMETERS
  on the realizability axis (exp-038's own `realizability_tier`,
  `REALIZABILITY_MEMO.md` Amendments 2/3) — "genuinely new wrinkle in T1's
  bookkeeping" overstates a finding about an already-unrealizable material
  corner. Required restating the realizability caveat at P-EM-5's own point
  of claim, not buried in §6.
- **THERMODYNAMICS**: the proposal is silent on THERMO, repeating the exact
  silent-sidecar pattern Iteration 15 just made house discipline to avoid
  ("no thermal feedback modeled" ≠ "no sidecar owed"). Required an explicit
  inherited-N/A carry-forward of exp-037/038's own borrowed ΔT ceiling.
  (Separately proposed treating f_c as a re-radiation modulation frequency —
  see Red Team's adjudication below.)
- **QUANTUM OPTICS**: §3's conversion reads a ONE-SHOT relaxation's pole as
  directly comparable to TCSF landmarks measured under PERIODIC flicker
  stimuli — a different physical quantity in a different stimulus class,
  the same conflation-risk species this seat flagged at Iteration 15 (Test
  B's `A` vs. T18's field-enhancement factor). §6's "envelope" defense was
  unquantified. Required either an actual spectral-overlap calculation or
  explicit relabeling of every classification as conditional/order-of-
  magnitude.
- **VISION SCIENCE**: the mandatory verbatim tag ("T3-provisional; not a
  scored perceptual verdict") — fixed as house discipline at Iteration 15's
  own Phase-5 close — is absent at P-EM-4, P-EM-5, P-EM-6's own points of
  claim. This is the exact pattern that has now required Phase-5
  intervention on three consecutive COMMITTED iterations (13, 14, 15), with
  a standing instruction that a fourth recurrence fires Checkpoint criterion
  4 without debate. Required the tag at every point of claim before commit.

**Red Team (PROCEED-WITH-MANDATORY-FIXES).** Independently re-derived rather
than trusted throughout — eight numbered attacks:

1. **[inconsistency][unfalsifiable]** — independently recomputed all 10
   Host D/E f_c values against the proposal's own stated definitions and
   found **P-EM-5's own headline claim ("all 10 points classify
   in_passband") is FALSE under the proposal's own numbers**, using either
   of its two candidate scotopic corner values (the "≈2–3 Hz cited" reading
   puts the large majority of points BELOW the corner, sub_passband, not
   in_passband; the "0.8–1.1 Hz formula-derived" reading puts all 5 Host E
   points below corner, sub_passband). Neither reading supports the
   proposal's claim as stated. None of the five blind seats recomputed this.
2. **[inconsistency]** — the scotopic low-corner cell in §1's own table
   states two DIFFERENT, unreconciled values in the same cell (a
   formula-derived 0.8–1.1 Hz vs. a separately-cited "≈2–3 Hz" range) —
   load-bearing, not a rounding nitpick, since the two give materially
   different classifications.
3. **[inconsistency, adjudicating QUANTUM's attack]** — confirmed the
   periodic-vs-one-shot category error is real (a step response's spectral
   power sits mostly below f_c, not "at" it) but ruled it **not fatal**: the
   pole-corner comparison is a legitimate order-of-magnitude proxy for the
   crude question "is this transient's timescale on one side or the other of
   the eye's temporal cutoff" (which correctly disposes of Hosts A–C,
   uncontested), just not a rigorous sub-threshold contrast calculation for
   Hosts D/E specifically.
4. **[correctable, adjudicating PHOTONICS' attack]** — confirmed the
   chromatic/achromatic gap is real and genuinely undisclosed anywhere in
   the original §6 Idealizations list.
5. **[scope/framing, adjudicating and STRENGTHENING MATERIALS' attack]** —
   confirmed via `run.py::realizability_tier` and `REALIZABILITY_MEMO.md`:
   Host D r=1 and all 5 Host E points (6 of the 10 screened) are
   independently UNOBTANIUM-WITH-PARAMETERS on the realizability axis
   ALONE — compounding with Amendment 2's separate D_req/irradiance
   UNOBTANIUM verdict, which covers every FCA sub-class checked to date
   including the "published" hosts. The entire grid this proposal
   timing-screens currently has zero demonstrated realizable instances.
6. **[rejected as stated, adjudicating THERMODYNAMICS' attack]** — f_c is
   the POPULATION-KINETICS relaxation rate; the actual re-radiation
   (thermal) bandwidth is set by the THERMAL SYSTEM's own, generally much
   slower, time constant (heat capacity/diffusion), a materially different
   physical process with no established relationship to k_f+k_r anywhere
   in this program's record. THERMO's own separate point (silent-sidecar
   carry-forward) stands and is adopted; the "f_c doubles as re-radiation
   modulation frequency" claim is rejected.
7. **[Checkpoint ruling, adjudicating VISION SCIENCE's attack]** — the
   underlying missing-tag critique is confirmed correct, BUT Checkpoint
   criterion 4 does NOT fire this cycle: the standing instruction targets a
   defect surviving into a COMMITTED record three consecutive times despite
   the process; this is a Phase-2 catch on an uncommitted Phase-1 proposal —
   the safeguard working, earlier than it ever has. Ruled: adopt as a
   mandatory fix, do not fire. A recurrence into this cycle's own committed
   Phase 4/5 record (mirroring exp-038's fixed-in-predictions/recurred-in-
   results pattern) would be the genuine fourth instance.
8. **[general sweep]** — no quiet constraint-1/2/3/4 violation found; no
   other unfalsifiable claim beyond #1 above; the scotopic decision
   procedure as originally specified was not precise enough for two
   independent implementers to agree on its output — a real
   inexpressibility gap given "predictions committed before any run" is
   non-negotiable house discipline.

**Verdict: proceed-with-mandatory-fixes.** Nine-item docket (see Phase 3).

### Director's independent checks (before adopting Red Team's attacks)

Independently recomputed all 10 Host D/E f_c values and both candidate
scotopic-corner classifications myself (`python3`, exact arithmetic) before
accepting attack #1. **Confirmed the substance of Red Team's catch, but
found an arithmetic error in Red Team's OWN count while doing so**: attack
#1's text states "6 of the 10... (all 5 Host E points, plus 4 of 5 Host D
points)" — but 5+4=9, not 6. Recomputed exactly: under the "≈2–3 Hz cited"
reading, **9 of 10 points** (all 5 Host E + 4 of 5 Host D, only Host D r=1 at
f_c=3.183 Hz clears either corner value) classify sub_passband, not
in_passband — the direction of the original claim is still wrong, more
severely than Red Team's own miscounted "6 of 10" stated. Under the
"0.8–1.1 Hz formula-derived" reading, the split is exactly 5/5 (Host D
robustly in_passband at every point, Host E robustly sub_passband at every
point) — this is the reading adopted below (Fix #1/#2), both because it
traces to a stated physical derivation (rod integration time) rather than an
unsourced "cited range," and because it produces a clean, boundary-robust
classification for this specific grid (verified: `classify_zone`'s
band-robustness check agrees across all four corner/cff endpoint
combinations at every one of the 10 points — zero `boundary_dependent`
results). Red Team's attack #5 count ("6 of 10... Host D r=1 + all Host E")
is a SEPARATE, correct calculation (realizability tier, not TCSF
classification) — independently reconfirmed against `run.py::
realizability_tier` from exp-038, no error found there.

## Phase 3 — Synthesis (Director)

**All nine Red Team mandatory-fix items adopted; zero overridden.** The
corrected `classify_zone` (built into `lab/temporal_csf.py` — see Phase 4)
resolves fixes #1–#3 directly in code, not prose: it accepts a (lo, hi)
uncertainty band for both the corner and CFF thresholds and returns a
classification ONLY if it is identical across all four band-endpoint
combinations, else explicitly reports `boundary_dependent` — no silent
point-value pick. The scotopic corner is pinned to the formula-derived
0.8–1.1 Hz band (Fix #2); the "≈2–3 Hz cited" alternative is retired from
the code (kept only in NOTES.md's record of the original, refuted draft,
above). Fixes #4 (chromatic/achromatic disclosure), #5 (relabel every
classification as an order-of-magnitude timing screen, not a rigorous
overlap calculation — QUANTUM's fix, adopted via the relabeling branch
Red Team ruled acceptable rather than building a full spectral-overlap
calculation this cycle, given scope), #6 (realizability restated at P-EM-5's
own point of claim, strengthened per Red Team's count), #7 (THERMO's
inherited-N/A carry-forward adopted; the modulation-frequency claim
rejected, not carried into any prediction below), and #8 (the mandatory
"T3-provisional; not a scored perceptual verdict" tag at every point of
claim) are all applied directly in the corrected predictions below. Fix #9
(hand-re-verify every falsification condition against the corrected
tables/logic) is executed in Phase 4 by construction — every gate and
prediction below is checked programmatically against `run.py`'s own output,
not just narrated.

## Final parameter table (corrected, as it will actually run)

| Regime | Low corner (Hz) | CFF (Hz) | Source |
|---|---|---|---|
| Photopic | 2.0 (point) | (50, 90), canonical ≈60 | Kelly 1961; de Lange 1958; Ferry-Porter (Tyler & Hamer 1990) |
| Scotopic | **(0.8, 1.1)** — formula-derived from rod integration time (~150–200 ms), the "≈2–3 Hz cited" alternative RETIRED per Red Team fix #2 | (15, 25) | de Lange 1958; Hecht & Verrijp 1933 |

Host/ratio grid: identical to exp-038's own stage-12 grid (`HOSTS = {"A":1e9,
"B":1e6, "C":1e3, "D":1e1, "E":1e0}` s⁻¹, `RATIOS = [1e-9, 1e-5, 1e-3, 1e-1,
1.0]`) — no new FDTD run, no new sweep design; this experiment re-scores
numbers exp-038 already produced.

## Falsifiable predictions (pre-registered, corrected, committed before run)

**Every prediction below is T3-provisional; not a scored perceptual
verdict** — a necessary-not-sufficient timing screen only (Fix #8). Every
prediction is additionally an order-of-magnitude directional screen, not a
rigorous spectral-overlap calculation (Fix #5/Red Team attack #3's
adjudication) — legitimate for the crude sub_passband/in_passband/supra_cff
question, not for fine sub-threshold contrast claims.

**P-EM-1 (pole-identity gate).** Central ~10⁻¹⁶, band ≤1×10⁻¹² relative, all
25 grid points, both regimes. *Falsified by any point exceeding the band.*

**P-EM-2 (Host D f_c band).** f_c(Host D) ∈ [1.55, 3.25] Hz, monotonically
increasing with r. *Falsified if any point falls outside, or is
non-monotonic.*

**P-EM-3 (Host E f_c band).** f_c(Host E) ∈ [0.155, 0.325] Hz, monotonically
increasing with r. *Falsified under the same conditions as P-EM-2.*

**P-EM-4 (photopic classification, T3-provisional).** Host D r≤10⁻¹ (4 of 5
points) classify `sub_passband`; Host D r=1 (f_c≈3.18 Hz) is the one point
predicted to classify `in_passband`. All 5 Host E points classify
`sub_passband`. **Falsified if Host D r=1 does not cross into
`in_passband`, or if any Host E point does, or if any point returns
`boundary_dependent`** (the photopic corner/CFF bands are wide enough
relative to the grid's f_c values that no boundary-dependent result is
expected; a `boundary_dependent` return here would itself indicate the
bands need tightening before this screen is trustworthy).

**P-EM-5 (scotopic classification, T3-provisional — CORRECTED from Phase 1's
refuted draft).** Under the pinned, formula-derived scotopic corner band
(0.8–1.1 Hz): **all 5 Host D points classify `in_passband`** (robust across
the full corner/CFF uncertainty band — every Host D f_c value, 1.5916–
3.1831 Hz, sits above the corner band's own upper bound of 1.1 Hz and below
the CFF band's own lower bound of 15 Hz); **all 5 Host E points classify
`sub_passband`** (robust — every Host E f_c value, 0.1592–0.3183 Hz, sits
below the corner band's own lower bound of 0.8 Hz). This is a clean 5/5
split, the OPPOSITE of Phase 1's original, refuted "all 10 in_passband"
claim. Read alongside P-EM-4: **Host D flips from favorable-except-one-point
(photopic) to unfavorable-at-every-point (scotopic); Host E stays favorable
in BOTH regimes.** This is the corrected version of the cycle's one
genuinely novel claim — a real, if narrower than originally drafted,
photopic/scotopic divergence for a slow-relaxation T17-class mechanism.
**Realizability caveat, restated at this point of claim per Red Team fix
#6**: Host D r=1 (the one point driving Host D's photopic in_passband
result, and one of the two hosts driving the whole scotopic finding) and
every Host E point are independently UNOBTANIUM-WITH-PARAMETERS on
exp-038's own realizability axis (`run.py::realizability_tier`), compounding
with `REALIZABILITY_MEMO.md` Amendment 2's separate D_req/irradiance
UNOBTANIUM verdict, which covers every FCA sub-class checked to date. **This
timing-screen finding describes a mechanism class with zero demonstrated
realizable instances in this program's own grid** — a narrower result than
"a genuinely new wrinkle in T1's bookkeeping" (Phase 1's original framing,
downgraded here). *Falsified if any Host D point classifies anything other
than `in_passband`, if any Host E point classifies anything other than
`sub_passband`, or if any point returns `boundary_dependent` (which would
mean the corrected corner band is not actually robust for this grid,
contrary to Phase 3's own pre-check above).*

**P-EM-6 (Hosts A–C, sanity/out-of-scope, T3-provisional).** f_c(A) ≈
1.6×10⁸ Hz, f_c(B) ≈ 1.6×10⁵ Hz, f_c(C) ≈ 1.6×10² Hz — all classify
`supra_cff` trivially in both regimes. Not a meaningful perceptual finding
(faster than any neural temporal-integration window, the same conclusion
P-MAT-4 reached by a different route in exp-038) — included only to confirm
the classifier doesn't misfire at the grid's fast extreme. *Falsified if any
of A/B/C classifies anything other than `supra_cff` in either regime.*

## Idealizations

- **Chromatic-vs-achromatic gap, undisclosed source data (Fix #4,
  PHOTONICS).** The cited de Lange/Kelly/Ferry-Porter landmarks are for
  ACHROMATIC (luminance) flicker. Whether a given host's colored↔bleached
  absorption change is spectrally broadband (achromatic — these landmarks
  apply as cited) or narrowband (chromatic — a materially lower-bandwidth
  chromatic TCSF, ~5 Hz-scale cutoff region per informal literature
  consensus, would apply instead) is **not resolved this cycle** — no
  host-specific absorption-spectrum-shape data exists anywhere in this
  program's record for the abstract Host A–E grid (exp-038's own hosts are
  parameterized by carrier lifetime only, not spectral character). If a
  future cycle instantiates a specific real material for one of these
  hosts, this question must be answered before P-EM-4/5's classifications
  are trusted for that material. Flagged, not silently assumed away.
- **One-shot transient vs. periodic-stimulus landmark comparison (Fix #5,
  Red Team attack #3's adjudication).** `classify_zone` compares a
  RELAXATION POLE (a one-shot, non-repeating event under constraint 4's
  actual scenario) to TCSF landmarks measured under PERIODIC flicker. This
  is a legitimate order-of-magnitude proxy for "is this transient's
  timescale entirely on one side of the eye's temporal cutoff" — which
  correctly disposes of Hosts A–C (P-EM-6) — but is NOT a rigorous
  spectral-overlap calculation for Hosts D/E, where the transient's own
  low-frequency spectral content and the TCSF's own shape near the
  corner both matter and are not captured by a single point comparison.
  Every P-EM-4/5 classification should be read as directional, not precise.
- **Timing-only, no amplitude (unchanged from Phase 1).** `classify_zone`
  says whether f_c sits in a TCSF-sensitive zone, not whether the resulting
  contrast clears any Weber-contrast threshold — necessary, not sufficient,
  for a scored constraint-3/4 verdict. The amplitude side needs Iteration
  16's still-unbuilt priority #3 (n(t)→ε(ω,t)/σ_abs(t) bridge).
  **T3-provisional; not a scored perceptual verdict** applies to every
  classification in this experiment without exception.
- **Landmarks are literature-consensus point/band values, not a digitized
  continuous curve (unchanged from Phase 1, T18).** WebFetch still blocked
  (fifth consecutive confirmed shift); every number in the parameter table
  is order-of-magnitude, pending primary-source verification.
- **Constant-(k_f,k_r) linearity, carried unchanged from `lab/kinetics.py`.**
  A future state-dependent-feedback kernel would not have a single
  well-defined pole and this framing would need re-derivation.
- **No constraint-1/2 claim; no optical-response, reciprocity, or
  causality claim beyond the pole's own construction** (real part
  negative whenever k_f+k_r>0, the same convexity argument stage-12 gate
  2a already proved for boundedness).
- **THERMO: inherited-N/A (Fix #7), full chain completed at Phase 5
  (Red Team fix docket #4, THERMODYNAMICS' own review).** No new absorbed
  power, no new FDTD run — this experiment inherits exp-037/038's own
  borrowed ΔT_ss≈7mK–0.7K ceiling unchanged, explicitly NOT re-derived or
  re-scaled here. The originally-proposed "f_c doubles as the re-radiation
  modulation frequency" claim is explicitly REJECTED (Red Team attack #6,
  independently re-confirmed at Phase 5): f_c is a population-kinetics
  rate, `f_thermal=G_th/(2π·C_th)` (heat capacity/conductance) is the
  actual re-radiation bandwidth, a materially different, never-computed
  quantity — no established relationship between the two exists anywhere
  in this program's record. **Completing THERMO's full charter chain**
  (absorbed power → temperature rise → emission band → detectability, not
  just the temperature-rise number alone): the 7mK figure sits ~3–7×
  BELOW current uncooled-microbolometer NETD (20–50mK); the 0.7K figure is
  non-negligible by the same comparison (both borrowed from
  `experiments/037-fca-combined-media-literature-check/NOTES.md`, emission
  band ~10µm per T5, unchanged/not re-derived here). **Zero-cost closing
  argument (THERMODYNAMICS' Phase-5 review):** exp-038's own Test-B
  periodic-retriggering buildup (up to 2.106× peak-n ratio at Hosts D/E)
  cannot push duty-cycle-averaged absorbed power past this inherited
  ceiling — n(t)∈[0,1] is bounded exactly by construction (stage-12 gate
  2a), and the ceiling was itself derived assuming near-total absorption
  already, so no duty cycle ≤1 can exceed an already-near-total-absorption
  assumption. An analytic argument, not FDTD-derived — stated as such.
- **Realizability untouched by the instrument's mechanics, but restated at
  every point of claim it applies to (Fix #6).** This instrument scores
  timing only; it does not revise `REALIZABILITY_MEMO.md`'s verdicts —
  but P-EM-4/5's own headline classifications must be read against which
  grid points are actually realizable (see P-EM-5, above), **under either
  bandpass/lowpass model** (see next bullet — the realizability caveat is
  model-independent).
- **Scotopic bandpass/lowpass model dependence (Phase 5, Red Team
  mandatory fix #1 — LOAD-BEARING, added post-commit before iteration
  close).** `classify_zone`'s scotopic branch applies a bandpass
  (low-frequency-exclusion) decision structure, but the regime's own cited
  source (de Lange 1958, see `temporal_csf.py`'s
  `SCOTOPIC_LOW_CORNER_BAND_HZ` docstring: "bandpass→lowpass transition
  with falling luminance") describes scotopic TCSF as LOW-PASS — sensitivity
  maximal near DC, no low-frequency exclusion. This was an undisclosed
  code-vs-docstring internal inconsistency, caught by ELECTROMAGNETISM's
  Phase-5 review (independently corroborated by VISION SCIENCE and
  PHOTONICS from different angles) and confirmed load-bearing by Red
  Team's own independent quantification: under the TRUE low-pass
  alternative (`classify_zone_lowpass`, no low-frequency exclusion), BOTH
  Host D (~87–96% of spectral power below CFF) AND Host E (~99% below CFF)
  classify `in_passband` — and Host E, read as "favorable in both
  regimes" under the bandpass model, is if anything MORE concentrated in
  the sensitive near-DC zone than Host D under the low-pass reading — the
  OPPOSITE direction. **Which model actually governs a ONE-SHOT (not
  periodic) scotopic transient is NOT resolved by this experiment** — it
  needs a primary-source check T18's WebFetch block currently prevents.
  Both readings are now reported side by side in `results.json` (see
  P-EM-5's `model_dependence` field); P-EM-5's verdict is downgraded from
  a clean CONFIRMED to `CONFIRMED-UNDER-BANDPASS-MODEL-ONLY`, and the
  original "Host E stays favorable in both regimes" headline language is
  RETRACTED as unsupported pending model resolution.
- **Spectral-overlap asymmetry within the bandpass model (Phase 5, QUANTUM
  OPTICS, Red-Team-verified arithmetic).** Independent of the model
  question above: even taken at face value, the bandpass model's Host D
  `in_passband` label only captures ~55–76% of Host D's actual one-shot
  spectral power inside the nominal passband (24–45% falls outside),
  while Host E's `sub_passband` label is well-supported (~76–91% of power
  genuinely outside the passband). The two hosts' bandpass-model
  classifications were not equally trustworthy in degree even before the
  model-family question above was raised.
- **Dropped `peak` landmark, Phase 1 vs. built instrument (Phase 5, VISION
  SCIENCE, Red Team fix docket #3).** Phase 1's proposal narrative named
  three TCSF landmarks (low corner, peak, upper cutoff/CFF); the actual
  built `lab/temporal_csf.py` implements only two (`low_corner`, `cff`) —
  no `peak` parameter anywhere in the module, `run.py`, or `results.json`.
  `classify_zone` treats the whole `[low_corner, cff]` interval as one
  undifferentiated `in_passband` zone, so a point just above the corner
  (e.g. Host D r=1, photopic, 1.18 Hz above the 2.0 Hz corner) is scored
  identically to a point at the curve's actual peak sensitivity. This drop
  between proposal and build was undisclosed until this Phase-5 catch; it
  changes no P-EM-* verdict this cycle (verdicts are pure zone-membership
  checks) but should be restored or explicitly justified before any future
  cycle relies on fine within-passband distinctions.

## Realizability bound (MATERIALS' own charter, restated per Fix #6)

Unchanged from `REALIZABILITY_MEMO.md` Amendments 2/3 and exp-038's own
`run.py::realizability_tier`: Host D is PLAUSIBLE at r≤10⁻³, UNOBTANIUM-
WITH-PARAMETERS at r=1; Host E is UNOBTANIUM-WITH-PARAMETERS at every ratio.
This experiment adds no new realizability finding — it restates the
existing one at the specific points its own P-EM-4/5 predictions depend on.

## New machinery / trust-suite stage (final, corrected)

`lab/temporal_csf.py`: `corner_frequency(k_f, k_r)`, `classify_zone(f_c,
low_corner, cff)` (band-robust — accepts scalar or (lo, hi) tuples, returns
`boundary_dependent` if the four endpoint combinations disagree, Fix #1/#2),
`score_grid(hosts, ratios, regime)`. Suite stage 13
(`stage13_temporal_csf`), wired via the digit-boundary regex established at
Iteration 15 (`_stage_selected`), three gates: pole-identity (≤1e-12),
classifier ordering self-consistency (exact), anchor-value regression
(≤1e-6). Not part of the fast default (`123456789`) or CI's own
`--only 12346789` — verified directly (`re.search` digit-boundary check on
both strings returns no match for "13") — explicit `--only 13` needed, same
convention as stages 10–12.

## Cost note

Zero new FDTD calls. Zero new WebSearch calls (all landmark citations
already gathered at Phase 1). Pure post-hoc analysis of exp-038's own
already-computed (k_f, k_r) grid plus a 4001-point synthetic sweep for the
suite's own ordering gate — sub-minute wall-clock expected for both the
suite stage and `run.py`.

## Phase 4 — Build + Test (exp-039, this shift)

`lab/temporal_csf.py` written (`corner_frequency`, band-robust
`classify_zone`, `score_grid`) exactly per Phase 3's synthesis — no
deviation from the corrected specification during implementation, no
implementation defects found (unlike exp-038's own Phase 4, which caught
two genuine bugs; this module's arithmetic is simple enough, and Phase 3's
own independent hand-verification already caught the one real defect —
Red Team attack #1 — before any code was written). Suite stage 13 added
(`stage13_temporal_csf`), wired via the same digit-boundary regex
established at Iteration 15, verified directly to stay excluded from both
the fast default (`123456789`) and CI's `--only 12346789` before being
trusted (`re.search` check on both strings, no match for "13").

**Trust suite: stage 13, 4/4 gates PASS.** Pole-identity 2.22×10⁻¹⁶
(≤1e-12); classifier ordering exact (`['sub_passband', 'in_passband',
'supra_cff']`, as pre-registered); anchor Host D r=1 3.58×10⁻⁷ rel err
(≤1e-6); anchor Host E r=1e-9 3.57×10⁻⁷ rel err (≤1e-6). Full local bench
(`--only 12346789`) re-confirmed 41/41 unaffected; stage 12 re-confirmed
5/5 unchanged (2.94e-16/0/0/0/4.73e-08, matching Iteration 15's committed
record to the printed digit); stage 12+13 run together (`--only 12,13`)
19/19 clean.

`experiments/039-.../run.py` written, applying `score_grid` to exp-038's
own grid in both regimes and scoring every P-EM-* prediction
programmatically (Red Team fix #9: hand-re-verified by construction, not
narration) against the corrected classify_zone logic.

**Science results, AS FIRST RUN this shift: 5/5 predictions CONFIRMED, zero
refuted, zero boundary_dependent results anywhere in the 50-point (25 grid
points × 2 regimes) sweep. AMENDED at Phase 5 (below) — P-EM-5 downgraded
to `CONFIRMED-UNDER-BANDPASS-MODEL-ONLY` (4 of 5 predictions stand as
originally reported; P-EM-5 required a same-shift fix and is now
model-contested, not a clean confirmation). This section is left showing
the as-first-run reasoning for the historical record (house convention),
flagged by this amendment rather than silently rewritten; `results.json`
itself now carries the corrected, regenerated numbers.**

- **P-EM-2 CONFIRMED**: Host D f_c ∈ [1.5916, 3.1831] Hz, inside the
  predicted [1.55, 3.25] band, strictly monotonic in r.
- **P-EM-3 CONFIRMED**: Host E f_c ∈ [0.1592, 0.3183] Hz, inside the
  predicted [0.155, 0.325] band, strictly monotonic in r.
- **P-EM-4 CONFIRMED** [T3-provisional; not a scored perceptual verdict]:
  photopic — Host D r≤10⁻¹ (4 points) `sub_passband`, r=1 `in_passband`;
  all 5 Host E points `sub_passband`. Matches Phase 1's original,
  unrevised prediction exactly (this was the one prediction Red Team's
  audit did NOT find defective).
- **P-EM-5, AS FIRST RUN: CONFIRMED** [T3-provisional; not a scored
  perceptual verdict]: scotopic (bandpass model) — all 5 Host D points
  `in_passband`; all 5 Host E points `sub_passband`. A clean 5/5 split,
  robust across the full corner/CFF uncertainty band at every one of the
  10 points (zero `boundary_dependent` results) — the OPPOSITE
  distribution from Phase 1's original, Red-Team-refuted draft ("all 10
  in_passband"). As-first-run reading (RETRACTED below, see Phase 5):
  Host D (the faster of the two slow hosts) is the one classified
  timing-unfavorable at every scotopic point; Host E (the slower host)
  stays timing-favorable in BOTH regimes. **Realizability caveat, restated
  at this point of claim per Red Team fix #6**: Host D r=1 and all 5 Host
  E points (6 of these 10) are independently UNOBTANIUM-WITH-PARAMETERS on
  `realizability_tier` alone, compounding with `REALIZABILITY_MEMO.md`
  Amendment 2's separate D_req/irradiance verdict — this finding describes
  a mechanism class with zero demonstrated realizable instances in this
  program's own grid, **under either bandpass or lowpass model (see
  Phase 5 amendment)**.
  **AMENDED AT PHASE 5 (Red Team mandatory fix #1, load-bearing — see
  Idealizations' "Scotopic bandpass/lowpass model dependence" bullet,
  above): the bandpass decision structure this reading depends on
  contradicts this regime's own cited source, which describes it as
  low-pass. Under the true low-pass alternative, Host E is MORE (not
  less) concentrated in the sensitive near-DC zone than Host D — the
  OPPOSITE of "Host E stays favorable in both regimes." That sentence is
  RETRACTED as unsupported. Verdict downgraded to
  `CONFIRMED-UNDER-BANDPASS-MODEL-ONLY`; both readings now reported side
  by side in `results.json`'s `model_dependence` field.**
- **P-EM-6 CONFIRMED** [T3-provisional; not a scored perceptual verdict]:
  all 30 Hosts A/B/C points (3 hosts × 5 ratios × 2 regimes) classify
  `supra_cff`, as predicted — the classifier does not misfire at the
  grid's fast extreme.

**Honest reading of the whole cycle's science content, AS FIRST WRITTEN
(amended by Phase 5, below).** This experiment's real contribution is NOT
that it discovered a dramatic new finding — it is that Phase 2/3's own
process caught and corrected a headline claim that was wrong on
inspection, before it could be committed as a result, and the CORRECTED
version confirms cleanly. The corrected P-EM-5 is real information (a
genuine photopic/scotopic divergence for Host D, none for Host E) but is
narrower than Phase 1's original framing, and — per the realizability
caveat — describes a mechanism class this program has never shown a
realizable instance of. Per the instrument's own stated idealizations,
none of this is a scored constraint-3/4 verdict: it answers "is the
switching transient in a temporally-sensitive band," not "would a human
actually see it" (that needs the still-unbuilt amplitude/contrast bridge,
Iteration 16's queued priority #3). **Phase 5 found this "clean
confirmation" reading itself rests on an unresolved, load-bearing model
choice — see below.**

## Phase 5 — Review (six fresh discipline seats, blind, then Red Team audit)

Full verbatim reviews: this shift's session record. All six seats
independently re-derived headline numbers from raw code/data (this
program's established Phase-5 standard) rather than trusting NOTES.md's
prose.

**All six independent verdicts on exp-039: PARTIAL.** PHOTONICS, MATERIALS,
ELECTROMAGNETISM, QUANTUM OPTICS, VISION SCIENCE all returned complete
reviews with independently re-verified arithmetic (zero numeric defect
found in `temporal_csf.py`/`run.py`/`results.json` by any seat).
THERMODYNAMICS' review agent hit an API error partway through its final
caveat sentence — its substantive content (all three assigned questions
fully answered) is complete and independently corroborated by Red Team's
own audit; only a verdict word and top-3 list were lost, both recoverable
from the other five seats' unanimous PARTIAL and consistent top-3 rankings.

**The cycle's one load-bearing finding: three seats independently
converged on variants of the same structural concern.** ELECTROMAGNETISM
found, by direct code inspection, that `lab/temporal_csf.py`'s own
docstring describes the scotopic regime as "low-pass" (de Lange 1958's
bandpass→lowpass transition) while `classify_zone` applies an unmodified
BANDPASS decision structure to it anyway — an internal code-vs-docstring
inconsistency none of the five Phase-2 blind seats or Red Team's own 8
Phase-2 attacks caught. VISION SCIENCE independently raised the same
concern from the literature side (a genuinely low-pass system has no
low-frequency exclusion; DC is maximally, not minimally, sensitive).
PHOTONICS independently raised the adjacent concern that a chromatic
(vs. achromatic) mechanism could invoke a different-SHAPE (not just
different-bandwidth) curve family, for the same underlying reason.

**MATERIALS** confirmed all realizability arithmetic correct (including
independently re-deriving the Director's own Phase-3 correction of Red
Team's Phase-2 "6 of 10" miscount — 9 of 10, under the retired reading)
and surfaced a new pattern: Hosts D/E are the same corner T17's own
Amendment 3 already found produces at-rest memory buildup — a real,
if near-tautological (both are monotonic functions of the same rate
constants on the same fixed grid), cross-axis anti-correlation between
temporal favorability and realizability, worth a logged LOGBOOK addendum
per Red Team's ruling, not a new material law.

**QUANTUM OPTICS** computed the exact Lorentzian one-shot spectral-overlap
fraction (an integral Red Team's own Phase-2 adjudication had only
gestured at qualitatively) and found Host D's bandpass-model `in_passband`
label captures only ~55–76% of its actual spectral power in-band, while
Host E's `sub_passband` label is well-supported (~76–91% genuinely
out-of-band) — an asymmetry in classification confidence, independent of
(and compounding) the model-choice question above.

**VISION SCIENCE** completed the assignment's highest-priority check —
line-by-line audit confirming the mandatory "T3-provisional; not a scored
perceptual verdict" tag is present at every point of claim in all three
required locations (NOTES.md predictions section, NOTES.md Phase-4
results, `results.json`'s own prediction `id` fields) — **the first cycle
in this recurring pattern's history where the tag survived intact through
Phase 3, Phase 4, AND results.json simultaneously.** Also found: Phase 1's
narrative named three TCSF landmarks (low corner, peak, CFF); the built
module implements only two — the `peak` landmark was silently dropped,
undisclosed until this catch.

### Red Team's Phase-5 audit

Independently re-derived rather than trusted throughout, per this
program's own Iteration-15 precedent. Verified all 50 `results.json` rows
by hand recomputation; independently re-checked QUANTUM OPTICS' Lorentzian
arithmetic (confirmed exact); independently quantified ELECTROMAGNETISM's
scotopic finding rather than accepting it qualitatively — computing the
true-low-pass spectral fractions directly (Host D ~87–96% below CFF, Host
E ~99% below CFF) and finding the effect is **sharper than EM's own
"collapses to undifferentiated" framing**: under the corrected model, Host
E is not merely equally-salient to Host D, it is MORE concentrated in the
sensitive zone — a directional reversal of the cycle's own headline claim,
not just a loss of differentiation. **The Director independently
re-verified this calculation once more before adopting it** (see
Idealizations, above) and found the qualitative/directional conclusion
holds, with a minor discrepancy in Red Team's own cited Host-E percentage
range (Director computed 98.6–99.6%, not Red Team's stated 93.3–99.6%) —
disclosed here per this program's own culture of catching imprecision
anywhere, including in Red Team's own numbers, rather than silently
accepting it.

**Ruling: LOAD-BEARING, mandatory same-shift fix, not merely
correctable-with-disclosure** — a disclosure sentence would leave a
classification that may point backwards still labeled CONFIRMED and cited
as the cycle's headline finding. QUANTUM OPTICS' spectral-overlap
asymmetry: confirmed correct, disclosure-worthy, compounds with (does not
independently resolve) the model question, since it was computed inside
the same possibly-wrong bandpass frame. VISION SCIENCE's dropped-peak
finding: real, undisclosed, non-blocking (changes no verdict, since
verdicts are pure zone-membership checks with no near-peak scoring).
MATERIALS' cross-axis pattern: real, worth logging, but should be framed
as a likely consequence of the fixed grid rather than an independent
discovery. THERMODYNAMICS' cut-off content: sound and usable as-is, the
incompleteness it found in itself (dropped emission-band/detectability
links) is the material item, not the cutoff.

**Checkpoint ruling, explicit: criterion 4 does NOT fire** — independently
re-confirmed (Red Team, corroborating VISION SCIENCE's own line-by-line
audit): the T3-provisional tag is present at every required point of claim
in the actual committed record. The scotopic model-dependence finding does
not itself fire criterion 4 either — it is falsifiable (a low-pass variant
gives a distinct, testable answer), was caught in-cycle before the
iteration closed (exactly what Phase 5 is for), and no constraint is
"quietly dropped" — P-EM-5 was correctly, consistently disclaimed as
non-scored everywhere it appeared, before and after the fix. **No other
quiet constraint-1/2/3/4 violation found; no unfalsifiable claim survives
in the committed record** (every prediction carries an explicit,
programmatically-checked falsification condition).

**Red Team's same-shift fix docket, applied in full, none overridden:**
(1) resolve the scotopic model question in code — DONE: `classify_zone_lowpass`
added to `lab/temporal_csf.py`, a new absolute-identity ordering gate added
to suite stage 13 (gate 4), `score_grid` computes both readings for
scotopic rows, `run.py` reports both in `results.json`'s `model_dependence`
field, P-EM-5 downgraded to `CONFIRMED-UNDER-BANDPASS-MODEL-ONLY`, the
unsupported "Host E favorable in both regimes" headline language retracted;
(2) QUANTUM OPTICS' spectral-overlap asymmetry added to Idealizations —
DONE; (3) dropped-peak-landmark Idealization bullet added — DONE; (4)
THERMO's full charter chain (emission band + detectability comparison)
completed, plus the zero-cost periodic-retriggering closing argument logged
— DONE; (5) MATERIALS' cross-axis pattern logged as a LOGBOOK addendum,
not this file — done in LOGBOOK.md Iteration 16 (T17 cross-reference); (6)
dead `TIER` dict removed from `run.py` — DONE.

**Full local bench re-verified after all fixes: `--only 12346789` 41/41,
`--only 12,13` 20/20 (new gate 4 added, 5/5 stage-13 gates now, was 4/4).**
`experiments/039-.../run.py` re-run: 4/5 predictions CONFIRMED as
originally stated, P-EM-5 now correctly reports
`CONFIRMED-UNDER-BANDPASS-MODEL-ONLY` with both model readings recorded.

### Director's close of Iteration 16

**Verdict: PARTIAL** (unanimous across all six blind seats, Red Team
concurs). The instrument itself — `lab/temporal_csf.py`, suite stage 13,
now 5/5 gates — is genuine, trust-gated machinery that retires this
program's single most overdue queued item (the T3 temporal-contrast
instrument, deferred since Iteration 1, named top priority at Iterations
13, 14, 15's own close). The pole/causality bookkeeping is independently
confirmed sound (EM's own re-derivation, tighter than the record
previously stated). The T3-provisional tag discipline held cleanly through
every stage of a committed record for the first time in a pattern that
required Phase-5 correction on three consecutive prior iterations (13, 14,
15) — genuine progress on a standing program-integrity concern. But — per
this program's own established precedent that verdict turns on whether a
cycle's own open questions close, not a favorable headline number — the
cycle's one genuinely novel claim (P-EM-5's scotopic divergence) turned out
to rest on an unresolved, load-bearing model choice, caught only at Phase 5
after surviving Phase 1 through Phase 4, and required a real same-shift
code fix (not just a disclosure) to avoid leaving a directionally uncertain
finding labeled CONFIRMED. This is a different fault line than the
T3-provisional pattern the cycle successfully avoided, but the same
underlying lesson this program keeps re-learning: a clean gate pass and a
falsified-or-not verdict are necessary, not sufficient, for a finding to be
trustworthy — the MODEL the gate checks against also has to be right.
Next lead per rotation: **THERMODYNAMICS** (Iteration 17).

**Ranked top-3 candidate directions for Iteration 17** (Red Team's
synthesis across all six seats' own top-3 lists, adjudicated not
concatenated; each checked against RULED OUT R1/R2/R3 — none resurrect a
dead idea):

1. **Build the n(t)→ε(ω,t)/σ_abs(t) causality/passivity-checked amplitude
   bridge** (ELECTROMAGNETISM's own #1, MATERIALS' #1, VISION SCIENCE's
   #1, QUANTUM OPTICS' #2 — the most convergent pick of any Iteration-16
   Phase-5 recommendation). Iteration 15/16's own carried, still-unbuilt
   priority #3. The single piece of missing machinery that would let any
   T3-provisional timing classification become an actual scored
   constraint-3/4 verdict against T2's already-pinned C_thr(L). Every
   seat's own reasoning converges: timing alone, however precisely
   classified, cannot answer "would a human actually see it."
2. **Resolve the scotopic bandpass/lowpass topology question with a
   primary source** (ELECTROMAGNETISM's #2, VISION SCIENCE's #2,
   PHOTONICS' #1 on the adjacent chromatic/achromatic shape-family
   question — three independently-converging picks). Needs a working
   full-text access route (T18) or an explicit, sourced engineering
   rationale for treating a one-shot scotopic transient as bandpass — the
   question this cycle could quantify but not resolve. QUANTUM OPTICS'
   own #1 (build the exact spectral-overlap module, replacing
   corner-comparison entirely) is a related, cheaper, zero-search-cost
   companion that should be folded in if this direction is taken.
3. **Reconsider whether continuing to screen the T17/FCA host list is the
   highest-information use of panel cycles**, given `REALIZABILITY_MEMO.md`
   Amendment 2 already found every checked FCA sub-class UNOBTANIUM on
   irradiance grounds, and this cycle's own headline result again lands
   mostly on already-unrealizable grid points (PHOTONICS' #3, EM's #3,
   MATERIALS' #2 — independently converging). Pursue T18's own still-open
   item instead: survey remaining unchecked mechanism classes for an
   irradiance gap small enough (≲5–6 OOM) that realistic field enhancement
   genuinely closes it.

*Non-blocking, queued if budget allows*: THERMODYNAMICS' own reusable
sidecar utility (still overdue a running implementation, carried from
Iterations 15/16); MATERIALS' cross-axis anti-correlation formalization
(zero-cost synthesis task, T17 + this cycle); restoring the dropped `peak`
TCSF landmark or explicitly justifying its absence.
