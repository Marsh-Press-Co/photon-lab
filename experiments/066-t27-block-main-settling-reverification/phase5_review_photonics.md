# PHASE 5 — REVIEW · PHOTONICS · Panel Iteration 43 · exp-066

*Fresh sub-agent, PHOTONICS charter, blind to the other five seats' Phase-5
reviews this cycle. Preserved verbatim as delivered.*

## 1. Independent verification (recomputed directly from `results.json`, not relayed from prose)

I re-derived every headline number from raw fields rather than trusting
`phase4_results.md`'s tables:

- **Gate P-066-G1**: pulled all 18 `block_g1ext` rows and diffed against
  exp-041's own committed `results.json::block_main` values — **18/18
  bit-exact, Δ=0.0**, matching the claim.
- **P-066-1**: computed `|ΔC(2800−1400)|` myself from `block_g1ext` (1400)
  vs `block_main2800` (2800) for the 18 new cells → **median =
  0.005766909912278462, max = 0.009574688227676709** — matches
  `phase4_results.md` to the printed digit, and the median sits cleanly
  inside the pre-registered [0.001, 0.010] CONFIRM band.
- **P-066-2**: recomputed sign flips myself on the same 18-cell pair →
  **exactly 3 flips**: (−39°,450nm), (39°,750nm), (−39°,750nm). Matches
  the claim, and — worth noting for my own charter — all three flip cells
  are 450nm or 750nm band-edge wavelengths, none at 600nm, consistent with
  600nm being this channel's best-characterized/most-Nyquist-favorable
  wavelength throughout the T20/T21 history.
- **Closure-summary bucket-flip table**: recomputed GATE_HARD (0.001)
  pass/fail across all 36 mandate cells from `closure_summary.rows` →
  **31/36 fail at STEPS=1400, 34/36 fail at STEPS=2800**, **5 total bucket
  flips (4 PASS→FAIL, 1 FAIL→PASS)**, and the five specific cells/values
  reproduce the table in `phase4_results.md` exactly, including the
  FAIL→PASS cell (+38°/600nm) being the same one exp-065's own headline
  first reported. Confirmed the "net worse, not better" framing is not
  spin — it is the correct read of the data.
- **Citation integrity check** (not requested, but load-bearing to trust):
  I cross-referenced all 18 "cited" (not re-run) ±35°/±38°/±40° values
  against exp-065's own committed `settled_sweep_steps2800_diagnostic.json`
  directly — **0 mismatches, all bit-exact**. The "citation, not re-run"
  claim for mandatory fix A is honest, not a shortcut with silent drift.
- **P-066-3a/3b**: verified the ratio arithmetic
  (`|ΔC(4200−2800)|/|ΔC(2800−1400)|`) by hand from the raw
  `C_1400/C_2800/C_4200` fields — 0.0098% and 0.00072% respectively, both
  ~100–1000× inside their 1% bar. I also checked *why* 750nm needed the
  largest 1400→2800 correction of any cell in the dataset (ΔC≈0.0143, the
  single largest in the whole 36-cell set) yet converges essentially
  instantly from 2800→4200: this is exactly the signature predicted by the
  already-on-record "periods of settling margin" mechanism (13.0/9.8/7.8
  periods at 450/600/750nm, thinnest at 750nm — exp-042 Phase-5) rather
  than an ad hoc coincidence. That internal consistency is a genuine,
  uncredited confirming detail for the settling explanation.
- **P-066-4 fringe refit**: confirmed `run.py` calls
  `dg042.edge_diffraction_c_empty_corrected` — exp-042's own committed
  function, imported and invoked, not reimplemented or hand-typed
  (satisfies R4). Confirmed the refit's 30-row input set is exactly Block
  MAIN's own 30 cells (12 cited `main_block` + 18 new), correctly
  excluding the ±35° fallback cells, matching exp-042's own original
  scoring population. r²(c*) 0.7852→0.8271, sign-agree 27/30→30/30, both
  reproduce.

**Everything I could independently re-derive checks out to the printed
digit.** No numeric error found anywhere in the headline chain.

## 2. Argue the next change — ranked top-3 for Iteration 44 (PHOTONICS' charter)

My charter is "is the optical response coherent as stated, across
wavelength and angle" — that reframes the generic queue somewhat:

**#1 — Resolve Block MINI's period-match test (T21 mechanism-vs-artifact),
don't defer it a further cycle.** This is the single most consequential
open PHOTONICS-charter question in the entire T20/T21/T27 lineage: is
there a *genuine* coherent Huygens edge-diffraction fringe with a real
λ/θ-dependent period `P(θ)=λ/(A·cosθ)`, or is the apparent fringe
substantially settling-transient content that happens to share the same
geometric clock `A·cosθ`? It has been UNDECIDED since exp-051 (Iteration
28), restated UNDECIDED at exp-065, and this cycle's own P-066-4 —
despite being correctly, carefully hedged as "strictly statistical" —
produced exactly the kind of number (R² *improving* under the corrected
data, sign-agree going to a clean 30/30) that a less careful future
citation will be tempted to read as vindication. The program has now
caught this exact failure mode three times (R4, T19, Block MINI itself).
A proper period-match test, or a genuinely discriminating alternative
(e.g., a resolution/cpl sweep — a true diffraction fringe's period is set
by geometry and is cpl-independent in cells-per-λ terms once expressed in
physical units, while a settling-transient residual's apparent "period"
in θ should NOT survive an independent R3 check the way a real fringe
would), should be Iteration 44's top item. Cost: likely zero-to-low FDTD,
mostly design work.

**#2 — Settle Block ARTICLE's article-PRESENT legs, not only the empty
floor.** Every settling number this program has now characterized
(exp-065, exp-066) is on the *empty* scene. VALIDATION.md's own
Iteration-35 lesson, cited approvingly in this cycle's own EM critique,
says a lossy object *changes* the transient decay time (an absorbing
interior gives the field somewhere to dissipate beyond the graded
boundary bands alone). That means the empty-scene settling correction
measured here is not guaranteed to transfer, in either direction or
magnitude, to `off_pass`/`off_bracket`-class scenes with an actual
absorbing article present — exactly the scenes T16/T21's real constraint-3
PASS/MARGINAL citations are built from. This is PLAN.md's own queued item
#2, and from my charter it is higher-stakes than its "narrower in
downstream stakes" ranking suggests, because it is the one remaining gap
between "the instrument's own empty floor is characterized" and "a real
constraint-3 verdict involving absorption is trustworthy at settled
STEPS."

**#3 — Complete angular coverage: the four interior `FALLBACK_ANGLES`
(0°/±5°/±15°/±25°) and the Block EXTEND boundary (41°–43°).** This cycle
closed the near-grazing window (35°–40°) cleanly, but the full 9-angle
quadrature every constraint-3 `C` value in this program's history sums
over includes four angles this cycle never touched at STEPS≥1400
verification, and the settling behavior at 41°–43° (just past this
cycle's own upper edge) is unknown — if the fringe amplitude/settling-
margin trend continues past 40°, that boundary matters for any future
extension of the MAIN-block window. A from-first-principles causal-
transit-time formula (θ,λ)→required-STEPS, closing the "extrapolated, not
individually verified" idealization this cycle is honest about at 33 of
36 cells, would let future cycles predict rather than re-measure — a
standing EM/PHOTONICS joint item, not purely mine, but directly serves my
charter's "coherent across wavelength and angle" mandate.

*(R_contact — named correctly and disclosed this cycle as a third
consecutive deferral — is outside my charter to rank; I note only that
the disclosure requirement was met.)*

## 3. Verdict: **PARTIAL** (PHOTONICS' perspective)

This is not a mechanism cycle — T1 escape route is correctly NONE, and I
found nothing that smuggles one in (no σ(I)/σ(x,t)/ε(ω) parameter appears
anywhere in `design_geometry.py`'s reuse of exp-065's own harness). So
there is no constraint-satisfaction claim to score PROMISING or RULED-OUT
against. From my own charter's angle:

- **Real, verified progress**: the instrument's own optical-response floor
  is now characterized at settled STEPS across the full mandate-named
  36-cell angular/wavelength set, not just the 12 cells exp-065 happened
  to leave settled. The citation audit (§4 of Phase 1, closed in phase4)
  is genuinely more complete than what existed before.
- **But the headline result is a net negative for confidence, not a
  fix**: GATE_HARD failures went *up* (31/36→34/36) at the corrected step
  count. My charter's central question — "is the optical response coherent
  across wavelength and angle" — is answered **less** favorably after this
  cycle than before it, even though the measurement itself is now more
  trustworthy. That is exactly why PARTIAL, not PROMISING, is right: an
  instrument getting more accurate and thereby exposing a worse floor is
  good science, not a favorable finding.
- **The one question that would actually resolve my charter's coherence
  question — mechanism vs. artifact for the T21 fringe — remains
  explicitly open**, and this cycle, correctly, declined to close it
  rather than oversell a correlational statistic. That restraint is itself
  the right call, but it means "is the optical response coherent" still
  cannot be answered with a mechanism, only with a magnitude table.

This matches the six-blind-seat/Red-Team PARTIAL precedent this exact
class of instrument-fidelity cycle has received twice before (exp-041,
exp-065) — I concur independently, from my own charter, not by deference.

## 4. Over-claims / under-disclosures / errors in `phase4_results.md`

I looked specifically for the recurring defect class this program's
Checkpoint history names — caveat-propagation gaps, scope-narrowing,
undisclosed idealizations — not physics errors, since I found none of the
latter.

- **No numeric or physics error found.** Every load-bearing number I
  independently recomputed reproduced exactly.
- **No mechanism overclaim found in the shipped text.** P-066-4's table
  row itself carries "(fit quality recovered — **no mechanism claim**)"
  inline, not buried 180 lines below as exp-065's own scorecard-
  propagation bug did — this cycle visibly learned from that specific
  prior defect. I checked the summary table at the top of
  `phase4_results.md` and the detailed section separately; both carry the
  same hedge consistently.
- **One genuine open item, correctly flagged but worth restating for the
  Director's close**: `phase4_results.md` itself says updating
  `lab/caveat_lint_config.json`'s `exp065-steps1400-unsettled-plane-
  channel` entry to reflect Block MAIN's 30-row closure is "a
  Phase-5/close-of-cycle task, not this Phase-4 file's own scope." I
  confirmed directly — as of the current commit, that entry's description
  still reads as if Block MAIN is uniformly unsettled, with no distinction
  for the now-closed 36-cell set vs. the still-open interior-angle/Block-
  ARTICLE gaps. This is not a defect in phase4_results.md (it correctly
  disclaims responsibility for it), but it is unfinished work the Director
  must not let slip past this Phase-5 close — if it ships without that
  entry being narrowed, that is precisely the class of gap this program's
  own Checkpoint-4 near-misses have repeatedly caught one cycle late.
- **Minor communication risk, not a factual error**: the "Closure summary"
  section header promises "the concrete answer to 'how many citations are
  affected'" but its content is actually the PASS/FAIL bucket-flip table,
  not a citation list — the actual citation-scope answer arrives in the
  next section ("Downstream citation scope"). A reader skimming only the
  first section could walk away thinking citation-scoping is done there.
  Low stakes (the real answer is present and correct one section later),
  but worth a heading fix.
- **Everything else I checked — the R_contact third-deferral disclosure,
  the ramp-vs-transit mechanism arithmetic correction (Red Team's own
  10.5×/one-order-of-magnitude fix), the ±35° citation provenance, the
  strictly-statistical framing of P-066-4 — was accurately and completely
  carried from Phase 3 into Phase 4 with no silent drift.**

## Summary for the Director

exp-066 is clean, well-verified instrument work: every number I could
independently check reproduced to the printed digit, its Phase 2/3
process caught and fixed real scope-narrowing and citation gaps before
the run (visible, working house discipline), and its Phase 4 write-up
avoided the specific overclaim failure modes this program has been burned
by before. The substantive finding — the instrument's own per-angle
optical-response floor is worse, not better, once settled, and the T21
fringe's mechanism-vs-artifact question is still open — is honestly
reported. My one actionable ask of the Director: confirm
`lab/caveat_lint_config.json`'s entry is actually narrowed at this
Phase-5 close, since `phase4_results.md` explicitly deferred that edit to
this step.
