# Phase 2 Critique — THERMODYNAMICS (exp-097, Panel Iteration 74)

*Charter: where absorbed energy goes; what re-radiates and whether it's
detectable. This cycle is zero-FDTD and computes no energy quantity of any
kind, so that half of the charter is N/A by construction (correctly — no
`p_abs_w`/NETD claim appears anywhere in this proposal to misapply it to).
Applying this seat's other standing duty instead: the bookkeeping discipline
this seat's own prior catches (exp-096's 12-vs-10 construction-count error,
the 18-vs-20 naming mismatch, the reversed containment-ratio triple)
established as its signature contribution to this sub-thread — verifying
every accounting claim in the document survives contact with the cited
source, by hand, this session.*

## Steel-man (146 words)

This cycle correctly absorbs its own prior lesson. Its predicted
construction count — 16 (representative, rebuilt fresh) + 4 (positive
control/FI-A/B/C, likewise rebuilt fresh) + 1 (FI-D) = **21** — is stated
explicitly on the *actual-`Sim.__init__`-call* basis exp-096's own Red Team
audit established as correct (not the "distinct configuration" basis that
produced exp-096's own 18-vs-20 gap). I re-traced the arithmetic by hand
against exp-096's own code shape (representative loop + four separate
`run_checks_1234` calls in fault injection, each hitting `construct_sim` →
`Sim(...)` fresh) and it holds: 16+4=20, +1(FI-D)=21, bit-exact. FI-E/F/G
correctly cost zero new constructions (Check 6/5 are pure-Python, no
`Sim()` call in either's own design). The desk pre-check is explicitly
labeled "disclosed, not treated as proven" per R4 discipline — the right
epistemic posture for a Phase-1 document.

## Sharpest attack (150 words)

§2b's own "R4-discipline" desk pre-check asserts a false bit-exact match.
For R3: computed `y_hi=2316` is claimed to match `R3_BASE_NY`'s own comment
value, cited as `(450/60/2376)`. I hand-derived `y_hi` from
`design_geometry.py` directly: `y_hi = ny - y_lo = R3_BASE_NY - R3_BASE_ABSORB
= 2376 - 60 = 2316`. `2316 ≠ 2376` — the two numbers differ by exactly
`y_lo` (60), because `y_hi` and `NY` are not the same quantity at all: one
is the domain height, the other is where the source's upper edge sits,
offset from it by `y_lo`. The identical error recurs for R5 (`y_hi=3860`
vs. cited `R5_BASE_NY=3960`, again off by exactly `y_lo=100`) — not a
typo, a systematic mis-citation of which constant a derived quantity
should be checked against. **Non-load-bearing** — Check 5's actual code
(§2b's `assert`) correctly targets `target["y_hi"]`, not `R3_BASE_NY`, so
the real script will pass — but this is precisely the R4/R9 failure shape
this seat exists to catch: a "bit-exact" claim, in a document that
explicitly invokes R4 discipline, that does not survive independent
recomputation.

## Verdict: **support-with-changes**

The architecture (positional Check 6, formula-independent-in-name-only
Check 5 extension with its first negative control, orthogonal-axis Check 7
with FI-D) is sound, correctly scoped to Tier 0 per the reconciled queue,
and its headline accounting claim (21 constructions) is the one number this
document invited scrutiny on and it holds. The desk-check mislabeling is
real but does not touch the code path that will actually run.

**Mandatory fix before Phase 3 freeze:** correct §2b's desk pre-check
prose for both R3 and R5 to cite the correct comparison target
(`R{n}_CONFIGS["C40_R{n}"]["y_hi"]`, i.e. 2316/3860) rather than
`R{n}_BASE_NY` (2376/3960) — three numbers per family (`src_x`, `y_lo`,
`y_hi`), all three checked against fields that actually hold `y_hi`'s own
value, not against the unrelated domain-height constant. Cheap, zero-FDTD,
same shift.

## Parameter change that would flip this verdict

If Check 5's own *executable* `assert` (not merely the prose) turned out
to share this same y_hi-vs-NY confusion — i.e. if `target` in §2b's loop
were accidentally built from `R{n}_BASE_NY` instead of the real
`R{n}_CONFIGS[...]` dict — the extension would silently pass by comparing
against the wrong constant and produce a false CLEAN. It does not, as
written (`target = dg.R3_CONFIGS["C40_R3"]`, correctly sourced), but that
one substitution is the single change that would move this to *oppose*.
