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
- **THERMO: inherited-N/A (Fix #7).** No new absorbed power, no new FDTD
  run — this experiment inherits exp-037/038's own borrowed ΔT_ss≈7mK–0.7K
  ceiling unchanged, explicitly NOT re-derived or re-scaled here. The
  originally-proposed "f_c doubles as the re-radiation modulation
  frequency" claim is explicitly REJECTED (Red Team attack #6): f_c is a
  population-kinetics rate, not a thermal-system time constant, and this
  program has no established relationship between the two.
- **Realizability untouched by the instrument's mechanics, but restated at
  every point of claim it applies to (Fix #6).** This instrument scores
  timing only; it does not revise `REALIZABILITY_MEMO.md`'s verdicts —
  but P-EM-4/5's own headline classifications must be read against which
  grid points are actually realizable (see P-EM-5, above).

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

**Science results: 5/5 predictions CONFIRMED, zero refuted, zero
boundary_dependent results anywhere in the 50-point (25 grid points × 2
regimes) sweep.**

- **P-EM-2 CONFIRMED**: Host D f_c ∈ [1.5916, 3.1831] Hz, inside the
  predicted [1.55, 3.25] band, strictly monotonic in r.
- **P-EM-3 CONFIRMED**: Host E f_c ∈ [0.1592, 0.3183] Hz, inside the
  predicted [0.155, 0.325] band, strictly monotonic in r.
- **P-EM-4 CONFIRMED** [T3-provisional; not a scored perceptual verdict]:
  photopic — Host D r≤10⁻¹ (4 points) `sub_passband`, r=1 `in_passband`;
  all 5 Host E points `sub_passband`. Matches Phase 1's original,
  unrevised prediction exactly (this was the one prediction Red Team's
  audit did NOT find defective).
- **P-EM-5 CONFIRMED** [T3-provisional; not a scored perceptual verdict —
  **the corrected version of the cycle's headline claim**]: scotopic —
  all 5 Host D points `in_passband`; all 5 Host E points `sub_passband`.
  A clean 5/5 split, robust across the full corner/CFF uncertainty band
  at every one of the 10 points (zero `boundary_dependent` results) — this
  is the OPPOSITE distribution from Phase 1's original, Red-Team-refuted
  draft ("all 10 in_passband"), and the directionally correct reading:
  Host D (the faster of the two slow hosts) is the one classified
  timing-unfavorable at every scotopic point; Host E (the slower host)
  stays timing-favorable in BOTH regimes. **Realizability caveat, restated
  at this point of claim per Red Team fix #6**: Host D r=1 and all 5 Host
  E points (6 of these 10) are independently UNOBTANIUM-WITH-PARAMETERS on
  `realizability_tier` alone, compounding with `REALIZABILITY_MEMO.md`
  Amendment 2's separate D_req/irradiance verdict — this finding describes
  a mechanism class with zero demonstrated realizable instances in this
  program's own grid.
- **P-EM-6 CONFIRMED** [T3-provisional; not a scored perceptual verdict]:
  all 30 Hosts A/B/C points (3 hosts × 5 ratios × 2 regimes) classify
  `supra_cff`, as predicted — the classifier does not misfire at the
  grid's fast extreme.

**Honest reading of the whole cycle's science content.** This experiment's
real contribution is NOT that it discovered a dramatic new finding — it is
that Phase 2/3's own process caught and corrected a headline claim that was
wrong on inspection, before it could be committed as a result, and the
CORRECTED version confirms cleanly. The corrected P-EM-5 is real
information (a genuine photopic/scotopic divergence for Host D, none for
Host E) but is narrower than Phase 1's original framing, and — per the
realizability caveat — describes a mechanism class this program has never
shown a realizable instance of. Per the instrument's own stated
idealizations, none of this is a scored constraint-3/4 verdict: it answers
"is the switching transient in a temporally-sensitive band," not "would a
human actually see it" (that needs the still-unbuilt amplitude/contrast
bridge, Iteration 16's queued priority #3).
