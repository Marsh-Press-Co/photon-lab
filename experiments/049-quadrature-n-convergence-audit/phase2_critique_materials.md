# PHASE 2 — CRITIQUE · Panel Iteration 26 · Seat: MATERIALS & METAMATERIALS

*Blind critique of `phase1_proposal.md` (candidate exp-049). Charter:
sub-wavelength structure, realizability bound (published / plausible /
unobtainium-with-parameters), per PANEL.md.*

## Charter-fit note, stated honestly up front

This proposal makes no material-law claim, proposes no structure, and
states T1 escape route: NONE. There is no optical behavior here for
MATERIALS to bound — `gaussian_angle_weights` samples a mathematical
Gaussian kernel over injection angle; `aperture_profile`'s raised-cosine
taper is a numerical source window, not a metamaterial or coating. My
charter's usual realizability-bound job has essentially no purchase on
§1–§2 of this proposal. What IS in-lane, and what this critique actually
does: (1) verify the proposal's own claim that no `REALIZABILITY_MEMO.md`
tier is at stake, rather than taking it on faith; (2) spot-check several
of the proposal's computed numbers; (3) apply a materials-adjacent
scope/geometry check the proposal's own idealizations invite.

## Verification performed (not taken on faith)

**REALIZABILITY_MEMO.md exposure — checked directly, confirmed NIL.** I
read `experiments/034-.../REALIZABILITY_MEMO.md` in full, including Entry
2 (`graded_black_shell` at witness scale, the only entry that isn't a pure
σ(I) dynamic-range/irradiance table). Every tier in that memo rests on
either D_req = σ_on/σ_off ratios and irradiance comparators (RSA/TPA/FCA/
ENZ/graphene/combined-media rows — none of these call `design_geometry.py`
at all) or, for Entry 2, on `C = −0.7209`, computed via
`edge_diffraction_c_empty[_corrected]` at a single fixed θ (exp-030's own
FDTD run) — a code path that never calls `gaussian_angle_weights` or
`beam_divergence_*`. The function under audit here feeds only the
contamination-risk / T21 fringe channel (VISION's `C_THR` ladder,
`beam_divergence_*`'s `C_empty`), a completely separate ledger from
`REALIZABILITY_MEMO.md`'s tier table. §3's claim is correct as stated.

**Numeric spot-checks, recomputed independently, not trusted from the
table:**
- T21 fringe period, P(θ)=λ_cells/(A·cosθ)·(180/π), A=752: recomputed all
  nine (λ,θ0) entries in §2.1's table by hand from `CPL={450:15,600:20,
  750:25}` — every printed value (1.4127°…2.4866°) reproduces to the
  printed 4th decimal.
- Samples-per-period ranges (P/Δθ_sample(41,fwhm)) at all four FWHM rows:
  reproduce exactly (e.g. FWHM=20°: 0.5651–0.9946, printed as 0.57–0.99).
- Ceiling derivation: Δθ_req=1.4127/10=0.14127°, n_req=100/0.14127+1=
  708.87→**709** — matches; 1281/709=1.807×, 2561/709=3.613× — both match
  the proposal's "≈1.8×"/"≈3.6×."
- Cost note: Σ(N_SERIES)+401 = 41+81+161+321+641+1281+2561+5121+401 =
  **10,609** exactly; ×36×3 = **1,145,772** exactly. Both reproduce.
- Code cross-check against `experiments/042-.../design_geometry.py:310-355`:
  `gaussian_angle_weights`, `beam_divergence_incoherent`,
  `beam_divergence_incoherent_corrected`, and `beam_divergence_coherent`
  are read verbatim as described — no material/physics claim is embedded
  in any of the four functions; they are pure numerical quadrature over an
  already-committed analytic propagator.

No arithmetic or code-description defect found in anything checked.

## Steel-man (≤150 words)

This is exactly the disciplined instrument-fidelity work my charter
should defer to when there is no material claim to bound. §3's "T1 escape
route: NONE" and "no result here can move any `REALIZABILITY_MEMO.md`
tier" are both independently verifiable, not merely asserted — I traced
the memo's own tier table and confirmed neither the σ(I) rows nor Entry
2's C=−0.7209 anchor touch `gaussian_angle_weights` anywhere. Every number
I spot-checked (the fringe-period table, samples-per-period ranges, the
n_req≈709 ceiling, the 10,609/1,145,772 evaluation counts) reproduces
exactly from the cited formulas. The two-consecutive-doubling convergence
criterion is a genuine methodological improvement over exp-046's single
41→401 jump, closing a real non-monotonic-convergence blind spot
(§2.2) at zero new FDTD cost, on the correct 36-cell committed grid.

## Sharpest attack (≤150 words)

Idealization 7 quietly repeats this program's own T21 anti-pattern.
exp-042 validated the fringe at the wrong geometry (±40°, A=752) for six
iterations before exp-048 finally re-derived it at the geometry any real
near-boundary citation actually uses (±35° fallback, A=724, NY=1528,
LOGBOOK Iteration 25). This audit — scoped explicitly to "exp-042/046's
own geometry exactly," not exp-048's — repeats that same mistake for the
fringe's own convergence behavior. By the audit's own formula
P(θ)=λ_cells/(A·cosθ), A=724 shortens every fringe period by a factor
752/724≈1.039×, shifting every samples-per-period ratio in §2.1's table
and possibly which cells cross the two-consecutive-doubling bar —
especially the marginal FWHM=10° regime this proposal itself flags as
"genuinely open." Any future materials-mechanism proposal that later
leans on a near-boundary `beam_divergence_*` reading to support a
constraint-3 claim would be leaning on convergence evidence measured at a
geometry that isn't the one actually cited.

## Verdict

**support-with-changes.** The desk audit is honest, well-scoped, and its
own headline disclaimers (T1: NONE; no REALIZABILITY_MEMO.md tier at
stake) check out under independent verification — nothing here threatens
my charter's own memo. The one change I'd require before treating any
P-NCONV26 finding as settling FWHM=10°/20° convergence more broadly: an
explicit, committed follow-up trigger (not necessarily this cycle) to
re-run the identical n-sweep at exp-048's A=724 geometry, since that is
the geometry any future near-boundary constraint-3 or realizability-
adjacent citation would actually use, and A=752's convergence order n\*
is not guaranteed to transfer under a ~4% period shift.

## Parameter change that would flip this verdict

If §5's idealization 7 were silently dropped or reworded to imply the
n\* results generalize across geometry (rather than being disclosed as
scoped to A=752 only), I would move to **oppose** — that would let a
convergence-order claim quietly launder itself into governing the A=724
fallback geometry it was never measured at, the exact citation-scope
failure T21 already cost this program six iterations to catch once.
