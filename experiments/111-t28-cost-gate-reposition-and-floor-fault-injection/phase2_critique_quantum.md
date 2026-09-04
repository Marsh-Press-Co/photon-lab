# Phase 2 Critique — QUANTUM OPTICS

## Steel-man

This proposal closes exactly the gap my own seat flagged at Iteration 87
(exp-110 Phase 5), and I independently re-derived its central claim in real
numpy rather than trusting the prose. FI-C's construction —
`peccored[i]=3.0e-3+1.0e-6·(i-23.5)²`, `hollow[i]=1.5e-3+4.0e-7·(i-23.5)²` —
does drive `floor_peccored_pooled`/`floor_hollow_pooled` to *bit-exact* 0.0,
not a tiny float residual: squaring symmetric offsets (`x` vs `-x`) is
IEEE-754-exact, so every one of the 24 mirror pairs is bit-identical and the
median is exactly 0.0. The `floor>0.0` guard therefore genuinely flips
`resolved` from the current code's trivial `[True]*48` to `[False]*48`. I
also pulled `raw_patterns` directly from exp-110's own committed
`results.json` and ran the patched function on all 12 real (r,margin)
cells myself: `floor_degenerate=False` and `n_resolved` bit-identical
everywhere — the non-regression claim is genuinely true, independently
verified, not merely asserted. Item 4's exponent (3.2053299988171697) also
reproduces exactly from committed wall-time data.

## Sharpest attack

The fix is incomplete on its own terms. `classify_item_i_local` returns
`local_snr_peccored`/`local_snr_hollow` from a **pre-existing, untouched**
ternary: `np.full(shape, np.inf) if floor<=0 else ...`. I ran the patched
function on FI-C's exact construction: `floor_degenerate=True`,
`resolved=[False]*48` (correct) — but `local_snr_peccored` and
`local_snr_hollow` are `[inf, inf, ..., inf]`, all 48 entries, in the
*same* returned dict. That is a live self-contradiction the proposed fix
introduces no guard against: "unresolved-by-construction" sitting beside
"infinite SNR" for the identical bins. FI-C's own test table (§2.1) checks
only `floor_peccored_pooled`/`floor_hollow_pooled`/`resolved`/
`floor_degenerate` — it never asserts on `local_snr_*`, so this
contradiction ships silently and would surface the first time any future
NOTES.md table or Phase-5 reviewer reads `local_snr` instead of `resolved`
for the degenerate branch, exactly the kind of silent-defeat-of-the-guard
failure mode this cycle exists to close.

## Verdict

**support-with-changes**

## Parameter change that would flip to full support

Extend the `floor>0.0` guard (or an explicit `np.nan` fill) to
`local_snr_peccored`/`local_snr_hollow` in the same patch, and add one more
assertion to `floor_fault_injection_control.py`'s FI-C case:
`local_snr_peccored/hollow` must NOT be `inf` (e.g. assert `nan` or `0.0`)
when `floor_degenerate=True`. Zero new FDTD, same scope, closes the gap
before it ships rather than after a seventh Phase-5 review finds it.
