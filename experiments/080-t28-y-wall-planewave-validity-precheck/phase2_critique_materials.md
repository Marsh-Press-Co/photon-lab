# PHASE 2 — CRITIQUE · MATERIALS & METAMATERIALS · Panel Iteration 57 · exp-080

*Fresh sub-agent, blind to the other six seats' Phase-2 critiques this
cycle. Read PANEL.md, AGENTS.md, `phase1_proposal.md` in full (including
its post-freeze PHASE 1 RESULTS section), `validity_precheck.py`,
`validity_precheck_results.json`, and my own seat's prior review this
exact sub-thread inherits from (`experiments/079-.../
phase5_review_materials.md` §2a/§2b/§4 item 3) and its Red Team audit
adjudication (§2). Independent verification performed below, not asserted
from memory — see the two checks.*

---

## 1. Steel-man (≤150 words)

Part (a)'s FORECLOSE finding is solid and admittance-independent: `d_F`,
`dist_image`, and `theta_local` are pure geometry, computed from
already-committed constants with zero reflectance physics involved, and I
independently reproduced `theta_local(y_lo)=15.0043°` for C40 by hand
(`atan(223/832)`... matches exactly). The version-drift guard passing at
exactly `0.0` for both proxies, at every config, is real, load-bearing
verification, not decoration. And the write-up does something this
sub-thread has repeatedly failed to do before: it explicitly names my own
seat's exp-079 §2a admittance-correlation collapse as part of the
reasoning-against for its own pre-registered (b) prediction, rather than
silently assuming the matched family's behavior generalizes. That is the
right instinct, even though (see Attack) it stops one step short of
actually pricing it.

---

## 2. Sharpest attack (≤150 words)

Part (b) is scored ONLY under the matched (`mu_r≠1`, unobtainium)
admittance — the exact gap my own exp-079 §2a/§4-item-3 flagged and
explicitly told this sub-thread to close *before* any future y-wall
instrument's admittance-sensitivity is priced by analogy. I reran (b)
end-to-end with only `Zi=n/sqrt(n²-sin²θ)` swapped for the realizable
`Zi=1/sqrt(n²-sin²θ)` (same substitution as exp-079 §2b): mean
`R²(Re,primary)` drops from **0.7345 (INCONCLUSIVE)** to **0.4305**, with
C40 and G40 (both `ABSORB=40`, the depth with the largest matched-vs-
realizable `arg(r)` deviation, `89.08°`, per my own exp-079 table) going
**negative** (`−0.62`, `−0.21`). Realizable mean falls *below* the
pre-registered REFUTE bar (`<0.50`). The (b) verdict is not a stable
INCONCLUSIVE; it is admittance-family-dependent, spanning INCONCLUSIVE→
REFUTE depending on an unresolved realizability question this exact
sub-thread already named. Separately: I swept `r(theta)` from 2°–20° for
all four ABSORB depths under the matched family and found no resonance,
branch-cut jump, or near-cutoff behavior (`Re(n)≡1.0000` identically,
`|r|`/`arg(r)` vary smoothly) — the fragility is admittance-*choice*, not
a numerical artifact.

---

## 3. Verdict: **support-with-changes**

Part (a)'s FORECLOSE stands on its own, admittance-independent, geometric
merits — I do not contest it. Part (b)'s INCONCLUSIVE verdict, and the
proposal's own recommendation to "carry (b) forward as a documented
caveat" into PHOTONICS' build, understates what is actually known: my
independent rerun shows the true state, once the open realizability
question is priced (as my own prior review told this sub-thread to do
before building any future y-wall instrument), sits at or below the
REFUTE line for two of five configs, not merely "good at 3/5, weak at
2/5." This does not change part (a)'s FORECLOSE, and it does not prove
PHOTONICS' own `θ_beam`-dependent construction is doomed (Idealization 2
still holds — a static `theta_eff` test cannot settle that). But it does
mean the caveat PHOTONICS is being handed is too soft: "R²=0.73 mean,
INCONCLUSIVE" reads as a coin-flip; "R²=0.43 mean under the one
alternative admittance family this exact sub-thread has already shown
diverges sharply at ABSORB=40" reads as a warning sign concentrated
exactly where the physics is least trustworthy.

---

## 4. The single parameter change that would flip my verdict

Add the realizable (`mu_r=1`) admittance rerun of part (b) to
`validity_precheck.py` itself (a five-line swap, mirroring exp-079 §2b —
zero new FDTD, reuses everything already imported) and report BOTH
admittance families' `R²` tables side by side in the PHASE 1 RESULTS
section, rather than citing the matched-family number alone with a prose
caveat. If that had been done and the combined finding ("INCONCLUSIVE
under matched, REFUTE-range under realizable, worst at ABSORB=40") were
disclosed plainly as this cycle's own (b) verdict, I would move to
**support** — the recommendation to proceed to PHOTONICS' build carrying
a correctly-weighted caveat is reasonable; it is the currently-reported
single-admittance-family caveat that is too optimistic.
