# Phase 2 — PHOTONICS blind critique (exp-062 / Panel Iteration 39)

*Fresh sub-agent, blind to the other six seats' current-cycle critiques.
Speaking only from surface interaction / absorption spectra / angular
dependence / scattering cross-sections — PANEL.md's PHOTONICS charter.*

## Steel-man (≤150 words)

The Airy-stack decomposition is correct, executed textbook thin-film
optics, and it cleanly separates two effects the prior cycle (exp-061)
conflated into one unchecked "1.20×" point estimate. The R-vs-T
geometric factor (~2×, an ordinary double-pass ray effect through a
backed film) and genuine coherent multi-beam interference are correctly
disaggregated and independently derived: the passivity bound
(`|r₁₂|,|r₂₃|≤1 ⟹ |ΔR/R₁₂|≲2e^{-τ}`) is dimensionally sound, self-
consistently checked against its own dropped `O(e^{-2τ})` term, and
gives ≤0.2%/≤6.3% at the two candidate τ — small in both cases, as
claimed. It also correctly identifies that the *same* Airy stack, at low
τ, crosses into a qualitatively different regime (critical coupling /
Salisbury screen) where near-zero R implies a tuned resonance, not a
large bulk α — a mechanistically grounded alternative, not an afterthought.
Bracketing the target to [0.60×,1.20×] under either OD convention is a
real, falsifiable, zero-FDTD result.

## Sharpest attack (≤150 words)

EM-3's broadband/narrowband "resonance discriminator" is not an
optical-response test — it is a search for whether a patent's claims
language happens to say "broadband," the identical vocabulary-presence
failure mode this program downgraded one cycle earlier (QUANTUM's
coherence/localization fallback, exp-061 MP-4). It can also point the
wrong physical direction: a critically-coupled thin film's interference
condition is set by round-trip phase `2β=2(2π/λ)n₂d·cosθ_t`, so ANY
angle-averaged reflectance measurement (integrating-sphere/hemispherical
OD, ordinary display-industry metrology) *smears* a genuinely narrowband
resonant dip across wavelength — making a resonant absorber read as
spectrally broadband, the opposite of what EM-3 treats "broadband" as
evidence for. Idealization 1 explicitly declines to model angle at all,
so this inversion is never checked, yet EM-4 leans on EM-3's outcome to
call the mechanism-class exclusion "confirmed, not threatened." No
falsification condition in §8 asks whether the source OD is
specular/near-normal or angle-integrated — the one fact that decides
whether EM-3 measures the right thing at all.

## Verdict

**Support-with-changes.** The core Airy/passivity mathematics is
correct and the R-vs-T decomposition is a genuine improvement over
exp-061's unchecked point estimate. But EM-3, as specified, cannot
carry the evidentiary weight EM-4 places on it: it is a text-matching
heuristic standing in for a physical discriminator, vulnerable to
exactly the angle-averaging inversion described above, and the
proposal's own Idealization 1 (normal incidence only) forecloses ever
noticing if that inversion applies to this specific candidate. This
does not touch exp-061's headline UNOBTANIUM-WITH-PARAMETERS tier — that
verdict is independently overdetermined by MP-2's thickness axis
(70–350×), which this cycle does not revisit — but it does mean EM-3/
EM-4's own narrower claim ("confirms the mechanism-class exclusion, not
merely a numeric near-miss") is not yet earned as stated.

## Checked against the ruled-out registry

No re-proposal of R1–R5 or of any refuted T1–T26 mechanism/model claim.
This cycle scores no constraint metric (T1 escape route: NONE) and
touches no σ(I)/σ(x,t)/angular-selectivity machinery; it is a
realizability-bound continuation in the same register as exp-036/037/061,
and its Section 4 physics is new (an Airy-stack/passivity treatment of
one literature figure) rather than a restatement of any standing thread.

## Parameter change that would flip the verdict

Add one query (or one explicit, disclosed abstention) to Section 6's
search plan targeting the black-matrix OD figure's own **measurement
geometry** — specular/near-normal vs. diffuse/integrating-sphere/
angle-averaged — and add a corresponding branch to EM-3's falsification
condition (§8) stating explicitly that an angle-*integrated* broadband
reading is NOT evidence against Section 4.4's resonant-absorber
hypothesis (it is at best uninformative, and plausibly the expected
signature of it). With that branch in place, EM-3/EM-4 becomes a
correctly-scoped result instead of an over-read one, and I would move to
unconditional support.
