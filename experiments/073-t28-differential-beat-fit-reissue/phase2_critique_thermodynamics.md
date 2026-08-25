# PHASE 2 — CRITIQUE · Panel Iteration 50 · exp-073 · THERMODYNAMICS (blind)

## Steel-man (≤150 words)

This is the most disciplined re-issue this program has produced. The R4
lesson is applied correctly and verifiably: `m₀ = 0.0025563909774436134`
matches exp-071's own `trend.linear_fit.slope` to the printed digit — I
recomputed it from the raw `(ABSORB, period)` pairs independently and it
reproduces exactly, while the old `0.00244361` figure reproduces exactly
as the C40→C80 endpoint chord, confirming the R4 diagnosis rather than
merely repeating it. The entire §2c power table (predicted ΔP, ΔP/P̄,
ramp/carrier %) recomputes bit-for-bit from `m₀` and public window
geometry alone — I rebuilt it from scratch and every cell matches. The
PAD/ABSORB confound (Idealization 2) is carried forward exactly as
Iteration 48 closed it, binding under every verdict branch, not just
CONFIRM. The saturating-vs-linear demotion correctly restates exp-072's
own Red-Team-corrected language ("engine-motivated, not engine-derived")
rather than reverting to the overclaim it replaced.

## Sharpest attack (≤150 words)

`m₀` is loaded correctly per R4 but is the **wrong-resolution** reference.
§2b.1 adopts `n_grid=3000` specifically to remove "the 0.0075°
node-collision quantization that reversed C70/C80's order at n_grid=400."
But `m₀` (0.0025564°/cell, R²=0.8664) is exp-071's `n_grid=400` fit — the
same collision. exp-072's own Phase-5 audit already computed and
published the correctly-resolved comparator: refitting the four periods
at `n_grid=3000` (`results.json → periods_n_grid3000`, already committed)
gives slope **0.0024637°/cell, R²=0.8328** — a 3.76% shift and a real
R² drop, flagged there as "the exact Attack-5 defect, reproduced inside
the disclosure written to prevent it." exp-073 reproduces the identical
substitution again, this time in its own §2c table and P-073-4's
disclosed rate band, while Idealization 6 downplays it as merely
"disclosed, not resolved" without surfacing the number that already
resolves it. Low-stakes numerically (non-gating, [m₀/3,3m₀] band is wide)
but it is the same named defect recurring for a third time on the same
quantity, and this cycle exists specifically to close the class of defect
that recurs.

## Verdict

**support-with-changes**

## Optional: the parameter change that would flip my verdict

Re-anchor the §2c table and P-073-4's disclosed rate comparison to the
`n_grid=3000`-consistent slope (0.0024637°/cell, sourced from exp-072's
already-committed `results.json → periods_n_grid3000`, refit at Phase 3
— zero new computation, one `lstsq` on four already-public numbers),
carrying `m₀` alongside only as the historical/Iteration-48-native value.
This does not change my verdict from support-with-changes to oppose even
unaddressed — the effect is non-gating and an order of magnitude below
anything that could move P-073-2/P-073-4's outcome — but it is the one
concrete fix that removes the recurrence and should land before
prediction-freeze, not after.

---

### Secondary note (not part of the required sections, offered as support)

Idealization 13 cites "house precedent, Iteration 5" for the claim that
the THERMODYNAMICS energy sidecar is correctly argued N/A rather than
silently omitted. I checked this against the LOGBOOK text directly: the
actual house norm being invoked — "a deferral must be a stated decision,
not an omission" — is LOGBOOK's own **Iteration-2** precedent, cited
verbatim under that label at Iteration 3 (exp-026 critique) and again at
Iteration 5 itself, where VISION's own Phase-2 critique invokes "the
Iteration-2 precedent" against that cycle's own THERMODYNAMICS-led
proposal for an *inadequately* argued deferral. Iteration 5 is, if
anything, an instance of the norm being applied against a THERMO
deferral, not the norm's origin. This is a citation-provenance slip, not
a substantive gap — the sidecar-N/A claim itself is correctly argued on
its merits (constraint-3/mechanism work is genuinely absent this cycle,
per Idealization 13's own reasoning and §6's T1 N/A statement) — but it
is exactly the kind of unverified "precisely cited" figure this program's
own R4 rule was built to catch in prose, just applied to a citation
rather than a number. Recommend the citation be corrected to Iteration 2,
or dropped in favor of restating the argument in this document's own
words.
