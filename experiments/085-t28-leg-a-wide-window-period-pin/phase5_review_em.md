# PHASE 5 — BLIND FINAL REVIEW · ELECTROMAGNETISM · Panel Iteration 62 · exp-085

*Fresh context, zero memory of any other seat's current-cycle critique or
review (including a different fresh EM instance's own Phase-2 critique of
this same cycle). Independent verification performed below, not accepted
on citation — see §2 for exact recomputation, most of it from raw stored
data, one leg from the closed-form model itself.*

## 1. Verdict: **PARTIAL**

A genuinely clean negative result at the global scale (Methods A and B:
no single stationary period survives wide/dense re-evaluation — this
closes off scenario (i) of the proposal's own §1 dichotomy) sits alongside
a striking but only partially-certified local result (Method C: a highly
significant, large, monotonic local-period trend) whose own pre-registered
reliability gate has a genuine, self-disclosed gap. The headline
**STRONG COHERENT CHIRP** classification, as computed, ships un-downgraded
despite its own mandatory reliability check firing — not because anyone
hid this (`NOTES.md` states it plainly and names it "Phase 5's own first
job"), but because Fix 2's downgrade language, written before Fix 5 added
a third classification cell in the same synthesis document, only ever
specified what to do to a nominal STABLE reading. I resolve that question
below (§2.5) with new analysis, not by re-stating the ambiguity.

## 2. What I verified/computed myself

### 2.1 Fix 3 (`center_deg=39.0` → `θc`) — traced through the algebra, correctly applied

`free_period_with_widening` (`experiments/078-.../y_wall_prescreen.py`
line 346) hardcodes `center_deg=39.0` in every call to
`_free_period_search`, with no parameter to override it — confirmed
directly in source, and it is **not** touched by `phase4_derivation.py`,
which reuses it unchanged. This forecloses the naive fix (pass
`center_deg=θc`); the only route available is the post-hoc correction Fix
3 actually specifies. I re-derived why that correction is valid, not just
textually compliant:

`_free_period_search` grid-searches candidate `P*` and, for each, fits the
data in `sin(θ)`-space at period `Tc = radians(P*)·cos(center_deg)`. The
quantity actually determined by the least-squares fit is `Tc` — a pure
`sin(θ)`-space period, with **no** dependence on `center_deg` in the fit
itself; `center_deg` only sets the conversion between `Tc` and the
reported "`P*` degrees" label. Since every one of Method C's 37 sub-window
searches used the identical `center_deg=39.0` (same `Tc` grid, same
`[lo,hi]` bounds, same 3-stage widening), the best-fit `Tc*` each
sub-window recovers is genuinely comparable across sub-windows — only the
degree-label is wrong. Re-labeling via
`P_local_corrected(θc) = P_local_reported(θc)·cos(39°)/cos(θc)` is
therefore not a patch but the **exact** algebraic un-do/re-do of the
mislabeling. Read directly in `phase4_derivation.py` lines 336–338:

```python
Tc_wrong = math.radians(fit_sub["p_star_deg"]) * cos_c
p_local_corrected = math.degrees(Tc_wrong / math.cos(math.radians(thc)))
```

`degrees(radians(p)·k)=p·k` identically, so this reduces exactly to
`p_star_deg·cos_c/cos(θc)` — the prescribed formula, applied at every one
of the 37 sub-window call sites (confirmed by direct read of the loop,
lines 330–347; no sub-window is skipped). **Fix 3 is correctly and
completely implemented.** Methods A and B correctly keep `center_deg=39°`
unmodified, consistent with every existing `P_model_a`/`P_edge_A`
citation — also confirmed, they are untouched by this bug (only a
*cross*-sub-window comparison is exposed to it, exactly as Red Team's
audit argued).

### 2.2 Independent reproduction of two headline numbers, from raw stored data, by an independent method

Rather than re-run the 2353-second script, I reconstructed the inputs
myself from what is already committed and recomputed the outputs by a
**different numerical path**:

- **Method B's spectral peaks.** `derivation_results.json::method_a.curve`
  stores the full `θ`-uniform `c_wide(θ)` array (`N=3901`,
  `θ∈[2°,80°]`). I linearly interpolated this onto the exact
  `sin(θ)`-uniform grid Method B specifies (`N=32768`,
  `u∈[sin2°,sin80°]`), applied the same Hann taper and zero-padding
  (`N_PAD=131072`), and ran my own FFT/peak-search — **not** a re-run of
  the committed code, a reconstruction from stored data via
  interpolation rather than direct model evaluation. Result:
  `P_fft=8.754371395917975°`, `P_fft_full=140.0699423346876°` — **bit-for-bit
  identical** to the committed values, to all 16 printed digits.
- **Method C's `spread`/`ρ`.** Recomputed directly from the stored
  per-sub-window `p_local_corrected`/`r2_local` arrays (37 entries):
  `spread=9.258667605452366`, Spearman `ρ=0.8816974869606448`,
  `p=5.757032996494069×10⁻¹³` — exact match to the committed JSON.
- Also independently recomputed the exhaustive circular-shift null's
  headline (`1772/3900=45.44%` of shifts meet/exceed `R²_wide=0.0128`,
  itself *below* the null distribution's own mean of `0.0659`) directly
  from the stored `circular_shift_null` block — confirms `R²_wide` reads
  as noise-scale or worse, not merely "not significant."

### 2.3 What `P_fft_full=140.07°` actually is — a Fourier-resolution argument, not a re-assertion of the write-up's own prose

This is my own field-theory contribution, not previously stated anywhere
in the record with this precision. I computed the FFT's actual bin
spacing: with `N=32768` real samples and `du=(u_hi−u_lo)/(N−1)`, the
**true**, non-padded fundamental frequency resolution is
`1/(N·du)=1.0527` cycles/unit-`sinθ` — corresponding to `P=70.03°`. The
`N_PAD=131072` zero-padding is a 4× interpolation of that same underlying
spectrum; it manufactures three new bins *below* the genuine resolution
limit (bins 1–3), purely by sinc-interpolating the DC-adjacent skirt, not
by resolving new independent frequency content. **`P_fft_full=140.07°`
is bin index 2 of that padded grid** — I confirmed this exactly
(`freqs[2]=0.52635`, `f→P` gives `140.0699...°`, matching to the last
printed digit) — i.e. it sits *inside* the interpolation zone, below the
data's own true resolution floor. Concretely: the full `sin(θ)` domain
spans only **0.500 cycles** of a period this long (`(u_hi−u_lo)/Tc=
0.49998`) — half a cycle across the *entire* 78°-wide window. By the
ordinary Fourier uncertainty argument, that cannot be a resolved
oscillatory tone; it is the spectral signature of whatever single
broad hump or monotonic envelope survives Hann-tapering and mean
subtraction in the data itself.

**Physical reading, direct answer to the question this review was framed
around**: this is neither "genuine near-field chirp" evidence nor really
a *contradiction* of it — it is best read as a **windowing/resolution
artifact specifically because Method B is structurally the wrong
instrument for a signal this strongly chirped.** Method C's own finding
(below) is that the local period grows by a factor of ~28× across the
domain — a signal that chirped that fast has, by construction, no
well-defined single global spectral line; a stationarity-assuming global
FFT will always either smear the true fringe content into an
unresolved broadband spectrum or get dominated by whatever slow
envelope is left over, exactly as observed (`P2/P1=0.799`, a
near-tied secondary peak — not a sharp line either). `NOTES.md`'s own
prose ("essentially a broad low-frequency/near-DC trend, not a resolved
tone") is directionally correct; this sharpens it to a specific,
checkable reason (below-resolution bin position) rather than a
qualitative impression, and reframes Method B's negative result as
**consistent with**, not evidence against, genuine near-field chirp —
Methods A/B simply cannot see a signal at Method C's own recovered scale.

### 2.4 Is Method C's trend real, or an edge-of-domain artifact? — a new robustness check

Two things worth checking independently rather than taking the headline
`ρ=0.88`/`spread=9.26` at face value:

**(a) Robustness to dropping the domain's two least-trustworthy ends.**
Idealization 4 (and PHOTONICS' Phase-2 critique, on the near-normal end
specifically) flags `θ<~20°` and `θ>~70°` as the model's weakest scalar
regions. I recomputed `ρ`/`spread` with progressively more of the domain
excluded:

| Excluded | n | ρ | p | spread |
|---|---|---|---|---|
| none | 37 | 0.882 | 5.8×10⁻¹³ | 9.26 |
| both endpoints (θc=5°,77°) | 29 | 0.788 | 4.0×10⁻⁷ | 3.51 |
| near-normal quarter (θc<21°) | 29 | 0.843 | 9.3×10⁻⁹ | 5.48 |
| grazing end (θc>61°) | 29 | 0.789 | 3.6×10⁻⁷ | 3.92 |
| both quarters | 21 | 0.679 | 7.1×10⁻⁴ | 3.42 |

The trend **survives every cut**, remaining highly significant even with
21 of 37 points and both suspect quarters removed. This is a genuine
positive finding: the local-period growth is not an artifact of the two
edges alone. **But a second, more targeted check complicates this**:
`spread` barely moves when only `θc=5°` (the single sub-window with the
*worst* circular-shift reliability, 86.7% null pass rate, and the one
PHOTONICS' Phase-2 critique specifically flagged as possibly measuring
main-lobe curvature rather than edge fringes) is dropped alone
(`9.26→9.09`) — because the classification's `spread>0.50` threshold is
overwhelmingly driven by the **grazing** endpoint (`θc=77°`,
`P_local=34.96°`), which is simultaneously the *most* statistically solid
point in the whole sweep (`r²=1.000`, 0% null pass) and the point the
proposal's own Idealization 4 flags as *least* trustworthy on physical
(scalar/non-vector) grounds. This is a real tension the record does not
currently state: the single strongest driver of "STRONG" is
statistically bulletproof but sits exactly where this model's own
disclosed physics validity is weakest.

**(b) Is the trend just the already-refuted grating law wearing a new
face?** `P_edge_B=λ/(A·cosθ)` (REFUTEd, T21/exp-069) predicts local
period should grow with θ purely via the `1/cosθ` obliquity/projection
factor. Over `θc=5°→77°` that predicts a `cos(5°)/cos(77°)=4.43×` growth.
The observed growth is `34.956/1.232=28.38×` — over **6× steeper** than
the obliquity-only prediction. This is a genuinely useful discriminant I
computed independently, not present anywhere in the existing record: the
trend is **not** simply T21's own refuted grating law re-expressed at a
different sampling density — it demands something beyond a fixed-aperture
projection factor, consistent with the proposal's own physical account
(a position-*and*-angle-coupled Fresnel-zone construction, not a global
obliquity scalar). This is real, independent support for treating the
trend as physically distinct near-field structure, not a recycled
artifact — though it does not by itself resolve the reliability question
in (a).

### 2.5 Resolving the Fix-2 gap: my own ruling as the reviewing EM seat

`phase4_derivation.py`'s classification code only downgrades a nominal
`STABLE` reading; a nominal `STRONG COHERENT CHIRP` with a firing
reliability flag (`null_pass_rate=0.40`, exactly at Fix 2's own trigger)
prints the contradiction (`"UNRELIABLE per Fix 2 -- CLASSIFICATION (a) =
STRONG COHERENT CHIRP"`) but does not act on it — confirmed by direct
read of lines 380–396. Given §2.4's own findings, my ruling: **downgrade
to DRIFTING, not NOT-STABLY-PERIODIC, and not full STRONG COHERENT
CHIRP as filed.** The trend is real and survives the robustness checks in
§2.4(a) — it should not be discarded — but it is not "STRONG" cleanly:
the specific interior structure that makes it exceed the 0.50 spread bar
is anchored by one point (`θc=77°`) whose own statistical solidity and
physical-model trustworthiness point in opposite directions, and 4 of 10
sampled sub-windows cannot be distinguished from self-similarity alone —
a genuinely bimodal, not uniformly-clean, evidentiary picture. This
matches, rather than contradicts, Fix 2's own stated intent (a
comparable-to-exp-084 pass rate should downgrade a reading one tier); the
gap was that nobody wrote down which tier "STRONG COHERENT CHIRP"
downgrades *to*. I don't think this fires Checkpoint criterion 4 on its
own: the reliability conflict is stated plainly in `NOTES.md`, not
smoothed over or defended, and is explicitly named as the record's own
first open question — the same self-disclosure pattern this program's own
Iteration-58 precedent treated as non-firing.

### 2.6 EM bookkeeping (reciprocity/passivity/causality)

Unchanged from exp-084: this cycle evaluates the identical, unmodified
`edge_diffraction_c_empty_corrected` formula at new angles only — no new
physics, no new medium. Reciprocity (kernel symmetric in
source↔observation via `hypot`), passivity (no gain, no lossy medium
anywhere in leg (a)), and causality (the correct outgoing/retarded phase
branch) all hold by the same construction exp-084's own Phase-5 EM review
already verified from primitives. I found no new violation and no reason
to re-litigate that finding — nothing here introduces a mechanism, a
medium, or an energy flow this seat's charter would need to re-check.

## 3. Steel-man and sharpest critique

**Steel-man.** This cycle did exactly what a disciplined, cheap,
zero-FDTD follow-up should: it asked whether a null-limited narrow window
was hiding a real asymptote, ran two genuinely independent global
instruments (confirmed independent in §2.3 — Method B fails for a
structurally different reason than Method A) plus a local instrument
built for the specific hypothesis at hand, applied every one of Red
Team's seven mandatory fixes correctly (§2.1 verifies the hardest one from
primitives), and delivered an honest, disclosed negative result at global
scale rather than forcing a period-match narrative. The `1/cosθ`
discriminant in §2.4(b) — new in this review, but the underlying data was
already there for anyone to check — is a real, decisive piece of evidence
that this cycle's own Method C signal is not merely T21's ghost.

**Sharpest critique.** The cycle's own decision architecture has a live
seam exactly where its central claim is most consequential: a
brand-new classification cell (Fix 5, `STRONG COHERENT CHIRP`) was
introduced in the *same* synthesis document as the reliability-downgrade
rule (Fix 2) that was supposed to gate it, and the two were never checked
against each other before Phase 4 ran — an entirely avoidable
same-document internal-consistency gap of a kind this program has
repeatedly flagged in other cycles' decision tables (exp-076, exp-085's
own §4(b) MECE gap that Red Team already closed). It was caught honestly,
same-shift, by the record's own prose — but not by the code that actually
computes the filed verdict, which is what future citations of "exp-085:
STRONG COHERENT CHIRP" will actually inherit unless this review's
downgrade (§2.5) is adopted explicitly.

## 4. Ranked top-3 candidate next directions (ELECTROMAGNETISM's charter)

1. **Extend the circular-shift null to all 37 Method C sub-windows** (not
   just the 10 sampled) — `NOTES.md`'s own timing shows this is now cheap
   (~1 additional minute, vs. the 2259s the full-curve Method A null
   consumed). This directly resolves whether the bimodal 6-low/4-high
   pattern generalizes or whether the 10-sample happened to catch an
   unrepresentative split, and should be run *before* any downstream
   cycle cites a settled DRIFTING/STRONG-CHIRP verdict. Pre-register the
   corrected classification rule from §2.5 (or the Director's own version
   of it) before running, so this isn't adjudicated post hoc a second
   time.
2. **Formalize the `1/cosθ`-obliquity-vs-observed-growth discriminant
   (§2.4b) as its own committed, falsifiable check.** It is currently a
   one-off number in this review; written into `dg048`/`ywp` as a
   reusable comparison (observed local-period growth vs. the REFUTEd
   grating law's own predicted growth over the same sub-window centers),
   it becomes a standing test any future T28 desk cycle can re-run
   against a corrected or extended Method C, and formalizes the strongest
   available argument that this mechanism family is doing something a
   simple obliquity projection cannot.
3. **Build the matrix-valued (source-*and*-observation-point-dependent)
   Rayleigh–Sommerfeld/Kirchhoff kernel for leg (b)'s Anchor 2** (queued
   since exp-084's own Phase-5 EM review, still untouched). This cycle's
   own finding sharpens the case for prioritizing it now: Method C's
   local, per-sub-window structure is real and substantial (§2.4), while
   Method A/B's global, single-tone instruments cannot see it (§2.3) — the
   same source/observation-point-local vs. global-scalar distinction that
   already diagnosed why a bare phase-factor fix for leg (b) is
   powerless. A working local kernel would let leg (b) be tested with an
   instrument built for exactly the kind of chirped, position-coupled
   signal this cycle's own leg (a) results say the physics actually is.
