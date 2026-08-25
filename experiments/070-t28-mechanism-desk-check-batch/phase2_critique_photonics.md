# PHASE 2 — CRITIQUE · PHOTONICS · Panel Iteration 47

**Proposal under review:** `experiments/070-t28-mechanism-desk-check-batch/phase1_proposal.md`
**Charter:** surface interaction, absorption spectra, angular dependence,
scattering cross-sections. Owns: is the proposal's optical response
coherent as stated, across wavelength and angle?

Blind to all other seats' critiques this cycle. RULED OUT check performed
(R1–R5): none re-proposed. R2 ("shell = integer×λ" resonance) is correctly
distinguished in Idealization 8 — this batch's small-integer candidates are
geometric-aperture arithmetic, not a wavelength-resonance order; agreed,
different claim class, not a resurrection.

## Steel-man (≤150 words)

Items (a) and (c) are exemplary zero-cost optics. (a) asks the right first
question — does the ~2.84° signature already live in `C40(θ)` or `C80(θ)`
individually (config-invariant, consistent with a shared diffracting edge
like `R_OUT`/`W_OBJ`/`TAPER`) or only in the difference (favoring an
`ABSORB`-tied boundary mechanism)? — a clean, single-shot, falsifiable
discriminator reusing the already-validated `_free_period_search` on new
data, no combinatorial search involved. (c) is genuinely disciplined:
`TAPER=40` cells as a sub-aperture predicts `P_taper(39°,600nm)=36.86°`,
over 10× off the observed `2.8421°` — a clean, already-computed REFUTE,
exactly the falsifiable, zero-parameter check this program's R3 meta-rule
demands. Both are legitimate diffraction-geometry reasoning, correctly
scoped as instrument/model-fidelity work (Checkpoint-2 declined), reusing
validated machinery rather than re-deriving it.

## Sharpest attack (≤150 words)

Items (b)/(d)/(e)'s named-constant search is optically incoherent as
evidence: the space nearly guarantees a match regardless of any real
mechanism. Computed directly — the declared space (14 named terms,
coefficients ±1..±10, singles+pairs) yields 36,680 candidate expressions
(7,179 distinct values). Against the disclosed `A_eff=518.81`, 140 already
land within the CONFIRM band (≤1%); against `A_alt=233.19`, 85 do — the
Ptolemaic-epicycle failure mode this critique is meant to catch. Worse:
the headline candidate (`3·R_OUT=234`) is not even the closest match in
its own space — six ties (`6·TAPER+3·LEVER`, `D_SP+8·clear_plane`, etc.)
beat it 4× tighter (0.037% vs 0.156%), with no physical story, so the
committed "record best match" algorithm (§7) will not reproduce the
narrative unless plausibility silently overrides distance-ranking. T28's
own founding fit passed a 20,000-trial null-permutation test (p<5×10⁻⁵,
exp-069); this search, over a far larger space, has no analogous
multiple-comparisons correction — its CONFIRM bands cannot license the
mechanism claim they exist to support.

## Supporting detail (not part of the word-capped sections)

- Search space computed exactly (script in scratch, reproducible): singles
  = 14 names × 20 coefficients = 280; pairs = C(14,2)=91 unordered name-pairs
  × 20×20 coefficient combos = 36,400; total 36,680 expressions, 7,179
  distinct numeric values.
- A second, related degeneracy the proposal's Idealization 4 only half
  discloses: `R_OUT=W_OBJ=78` is flagged, but `W_FLANK=78` is the *same*
  value and is silently in the same boat (confirmed above: `3·R_OUT`,
  `3·W_OBJ`, `3·W_FLANK` are one number wearing three names). Likewise
  `TAPER=ABSORB40=PAD80=40` — three names, one magnitude. Item (e)'s
  "convergence check" (do the (b) and (d) winners name the *same*
  combination?) is weaker evidence than it reads, because many nominally
  different combinations are numerically forced to agree by this labeling
  redundancy, independent of any shared physical origin.
- The 750nm cross-validation (item d, P-070-4) is a genuinely held-out
  dataset and is not directly infected by the search-space problem — but
  it only screens whichever single candidate the (contaminated) search
  hands it, and the script design never specifies a tie-break rule for the
  six-way tie shown above. Different tie-break choices would hand the
  750nm leg a different candidate period with no principled way to prefer
  one.
- Item (a) and (c) are unaffected by this attack and should proceed as
  designed.

## Verdict: support-with-changes

Run (a) and (c) as specified — sound, falsifiable, zero risk. Do not treat
a P-070-2 or P-070-4 CONFIRM as evidence for a real geometric mechanism
until the search itself is corrected; as designed it will likely CONFIRM
whether or not `ABSORB`/`R_OUT`/anything else plays a real diffractive
role, given the density shown above.

## Parameter change that would flip verdict to support

Add a pre-registered null-control on the named-constant search, mirroring
the 20,000-trial permutation test that already validated T28's own
founding free-period fit (QUANTUM, exp-069 Phase-5): run the identical
search (same 14 named terms, same coefficient range) against a large set
(e.g. N=10,000) of control targets drawn uniformly from the plausible
period-implied-length range (~[100, 1600] cells, i.e. the aperture-scale
window the physics plausibly bounds it to), and require the true targets'
best relative deviation to beat some pre-stated percentile (e.g. ≥95th) of
that null distribution before P-070-2/P-070-4 are scored CONFIRM. Report
ALL ties within the CONFIRM band, not a single cherry-picked
physically-flattering one. With that correction in place, whatever survives
is real evidence rather than a near-certainty of the search's own
construction, and I would move to support.
