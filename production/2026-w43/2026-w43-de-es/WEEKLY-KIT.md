# Die Lucerna VOL.1 — DE × ES Edition KIT

**Edition:** German target text + explanations in Spanish (edición para lectores hispanohablantes)
**Masthead:** Die Lucerna · SEMANARIO ALEMÁN VOL.1
**Week:** Monday 2026-10-19 → Sunday 2026-10-25 (W43) · Lead: „Eine Stunde geschenkt" — Zeitumstellung Sun Oct 25, 03:00→02:00; Herbstferien peak, 11 Länder.
**Pairing badge (P1):** «TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES» (brick #a4553a, bold)
**Footers:** «Die Lucerna · SEMANARIO ALEMÁN VOL.1 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL» / «Página N de 8»
**Gloss prefix:** «Nota — »

## Method (fan-out from the finalized DE core)
- Build dir: `hidden_files/weekly-report-de-es-build/` (copy of the core build dir `hidden_files/weekly-report-de-build/`).
- **Baseline proof:** the unmodified copy, with output redirected to /tmp, reproduced all 8 shipped core SVGs **byte-identically** (sha256 diff clean) before any edit. Registry total of the baseline: 150.
- Only the explanation layer was rewritten, into native Spanish: every definition, grammar note, instruction, exercise rubric and **all P8 answer notes**. The core's explanation helper was renamed `expl()` in this build; no intermediary-layer terminology appears anywhere in paper, KIT or code.
- All diffs/registries below are against the **core** (`files/weekly-report-de-vol1/`), never a sibling.

## Totals (identical to core)
- **150 exercises — A2 67 · B1 69 · B2 14**; per page 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Final build log: zero `FLOW OVERFLOW` / `HEAD TOO WIDE` warnings; P8 keys end y=2361 (limit 2560).

## Freeze verification (German target text)
- SVG text-multiset diff vs core: every non-Chinese core text element survives except (a) the P1 tagline, replaced by the ES pairing badge by design; (b) P8 key lines whose Chinese notes were re-parenthesized (full-width → half-width, space before the note parenthesis) and re-wrapped at the smaller key size — the keys themselves are registry-proven identical (below); (c) fragments of Chinese gloss elements replaced by their Spanish versions. **Zero CJK characters remain in the ES SVGs.**
- P7 verbatim check: all 8 German phrases of the week occur exactly 2× in the issue text (article + P7), same as core.
- Registry diff vs core: levels and keys identical for 147/150 items. **Key-diff registry (documented reader-language items only):**
  - **#137** (Traduce al español): key „La noche tiene 25 horas." (core key was the Chinese translation of the same German stem).
  - **#138** (Traduce al español): key „El sábado por la noche ajusto el reloj."
  - **#150** (writing, apparatus key): „Pregunta abierta — sigue los puntos del cuadro de escritura; el texto modelo está en el cuadro de esta página" (note: „Se califica según los puntos indicados").
  - **#139/#140** stems re-aimed into Spanish („El domingo duermo una hora más." / „En la biblioteca se pueden prestar libros."); their German keys are byte-identical to core.
  - 135/150 answer notes translated into Spanish; the 15 identical notes are language-neutral (e.g. „trennbar: um-ge-stellt", „46 + 18 = 64", „halb vier = 3:30"). One consistency fix during proofread: #123's note gloss aligned to „O bis O = de octubre a Pascua" (Pascua, matching the P7 toolbox).

## Layout adjudications (wording-only fixes; geometry never changed)
Spanish runs longer than the core's Chinese; the following explanation strings were shortened so every box, title and column ends inside its core geometry (all measured with production glyph metrics before rebuilding):
- P1 FRAGEN box line → „Las guías de todo el país las responden." (the slot is a single unwrapped line; the first version in
...[truncated 5016 chars]
---

## KIT completion + INDEPENDENT PROOFREAD RECORD (2026-10-21)

**⚠ KIT truncation found by the proofreader:** this file as delivered by the build ends mid-sentence in "Layout adjudications" — its final bytes are the literal marker `...[truncated 5016 chars]` (file was 3,833 B). The tail of the adjudication list, the builder's audit record, the deliverables/PDF pins and the PENDING proofread marker were therefore not present in the file. The paper itself is unaffected. Rather than reconstruct the builder's missing prose, this record (a) flags the truncation, and (b) supplies the verified final-state data those sections would have carried, all measured independently by the proofreader. The builder's surviving claims were each re-verified against the shipped artifacts; every claim checked out (see below), except that the full list of 10 in-build wording fixes is only partially recoverable from the truncated KIT (first bullet survives) — the final state itself passes every gate check on the proofreader's own measurements.

**Baselines (proofreader, independent rebuilds in an isolated copy):** the core build reproduces all 8 shipped core SVGs byte-identically; the DE×ES build reproduces all 8 shipped ES SVGs byte-identically. Registry totals identical: **150 exercises — A2 67 · B1 69 · B2 14**; per page 10/18/18/18/18/18/12/38; numbering 1–150 continuous in both registries and in the printed P8 keys.

**Freeze / key-diff verification:** registry keys differ from the core at exactly the three documented items — #137 key „La noche tiene 25 horas." (faithful to the printed stem „Die Nacht hat 25 Stunden."), #138 key „El sábado por la noche ajusto el reloj." (faithful to „Ich stelle die Uhr am Samstagabend um."), #150 apparatus in Spanish; #139/#140 stems re-aimed into Spanish with German keys byte-identical (and faithful to the Spanish stems). All other 147 keys byte-identical. Notes: 135 translated into Spanish; the 15 identical notes verified one by one as genuinely language-neutral (German verb forms, „trennbar: um-ge-stellt", arithmetic „46 + 18 = 64", „halb vier = 3:30" etc.). All 150 keys appear verbatim in the printed P8 answers. **All 150 exercises re-solved independently** by the proofreader against the printed stems, articles, fixture table and chart (46+22+18+14=100; the chart is labelled practice data in both languages): 150/150 keys correct. Writing model = 87 words, as printed.

**Spanish completeness:** zero CJK characters in the final SVGs (text layer and raw bytes). Full read of all 8 pages: every definition, rubric, instruction and all 150 P8 answer notes in Spanish. Pairing badge on P1; pairing footers + «Página N de 8» on all 8 pages; masthead «Die Lucerna». P7: all 8 phrases verbatim from this issue's articles, each exactly 2× in the issue text, page tags correct; visual check of the P7 card — no phrase tag struck through by a neighbouring quote (the in-build fix holds). Weekday/date claims all verified against the real 2026 calendar (Zeitumstellung Sun Oct 25, 03:00→02:00; Oct 24 Sat; Oct 31 Sat; Nov 1 Sun; Oct 26 Mon; Winterzeit ends Sun Mar 28, 2027). Banned intermediary-layer term: 0 hits in paper, KIT and build code. Images: payloads byte-identical to the core on every page; credits match the placed images (P1 Courtney Celley / U.S. Fish & Wildlife Service, P2 NIST, P3 Lucas Cranach d. Ä. 1528, P5 U.S. Department of Agriculture — all public domain).

**Geometric occlusion audit — flag-set diff (the decisive test):** the build's audit script (`audit_de_es.py`, family method: paint order, production font metrics, ink band baseline −0.88em…+0.30em, line boxes stroke-expanded, synthetic-control lineage) was run by the proofreader on BOTH editions' shipped SVGs:
- **DE×ES: 21 flags** — P2 ×1, P3 ×1, P4 ×18, P5 ×1, all BOXTITLE class.
- **Core: 26 flags** — the same 21 elements with identical measured values, plus 5 further flags on Chinese gloss lines (P1 Fragen head, P2/P3/P5 «Und Sie?» lines, P4 reader line) that the Spanish text renders without flagging.
- **Every one of the 21 ES flags has an identical core counterpart at the same element — ES-only flags: ZERO.**
- The supplementary text–text scan reports exactly 1 overlap in each edition: the P1 masthead pair («Die Lucerna» @262 vs the edition line @330).
- The proofreader's own independent audit (separate implementation, positive control validated — COVER/LINEX/FOOTER/EDGE/TEXTX all fire on synthetic defects): **COVER 0, LINEX 0, EDGE 0, FOOTER-crossing 0 on both editions**; TEXTX only the shared P1 masthead pair.
- Pixel adjudications on the shipped cards: P1 masthead — wordmark ink rows 141–264, edition-line ink from row 295, ≈30 rows of clear air (band-model artefact, non-defect). P4 fixture table — all 7 rows render cleanly inside their zebra bands (the 18 flags are the audit matching each row's text to the previous row's rect; identical in the core). P2/P3/P5 facts boxes — the flagged last lines („besser, sagen die Reifenexperten." / „(Kappel-Grafenhausen)." / „die Ferien.") render fully visible below the box border with the following box clear beneath: the cosmetic border-crossing class documented in the core KIT (sweep observations, deliberately not fixed), no information hidden, nothing struck through.

**Deliverables (verified by the proofreader):** svg/ ×8, cards/ ×8 (1950×2700), print PDF `Lucerna-VOL1-ES.pdf` 10,503,920 B sha256 `7b6f20a8d934666723f7175589ef659391277af6fcda2633af2b11d990210c77`, web PDF `Lucerna-VOL1-ES-web.pdf` **4,283,213 B (< 10 MB)** sha256 `f2d1f3ef2694151e9af304a60bd83f5eb637226861d3d57ba4b9f4d4335c9bcc`.

**VERDICT: PASS** — one complete independent pass, zero problems in the paper. No fixes were needed and nothing was re-rendered; the only repair made by the proofreader is this KIT completion record. This edition is clear for repo insert by the parent line. (Discord delivery is paused; nothing posted.)
