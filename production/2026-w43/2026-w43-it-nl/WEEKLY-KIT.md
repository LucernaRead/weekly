# La Lucerna — ITALIAANS WEEKBLAD VOL.1 · IT × NL (W43)

**Edition:** Italian target text (frozen VOL.1 core, week Mon 19 – Sun 25 Oct 2026) × Dutch explanations for Dutch-speaking readers. Built by the standard fan-out method from `hidden_files/weekly-report-it-build/` into `hidden_files/weekly-report-it-nl-build/`; deliverables in this directory (`svg/` ×8, `cards/` ×8 at 1950×2700, print + web PDF). No repo insert, no Discord (per task scope).

## 1. Baseline (freeze.py)

Core build copied to `hidden_files/weekly-report-it-nl-build/` and run unmodified via `tools/freeze.py baseline`: **8/8 SVGs byte-identical** to the shipped core (record: `hidden_files/weekly-report-it-nl-build/scratch/baseline-result.json`). Core SVG sha256 prefixes: p1 bd04af2f…, p2 ff75206e…, p3 9ce43c3d…, p4 aac8356c…, p5 079552c8…, p6 5d553abe…, p7 9b4daf76…, p8 58f37fd4…. **Re-verified after the build: all 8 core hashes unchanged — the frozen core was never edited.**

Transform (count-asserted, scratch/transform.py + mapping.py): 253 Chinese literals replaced 1:1 with Dutch; exercise types swapped positionally at 141 call sites (`ex(...)`/`match_set(...)` second argument); `instr="…"` keyword swapped at 70 sites; the core's explanation-paragraph method renamed to `expl()` at 21 sites (def + calls); OUT paths, P8 separator and render names repointed. Result: **zero CJK literals in all operative files** (AST scan; the only CJK left anywhere is a non-rendering docstring inside svglib.py, inherited verbatim from the core and present in every shipped edition).

## 2. Totals (registry, identical to core)

- **150 exercises — A2 46 · B1 71 · B2 33**; by page **10 / 18 / 18 / 18 / 18 / 18 / 12 / 38**.
- By type (Dutch names): Voltooi de zin 60 · Meerkeuze 49 · Cloze 13 · Woorden koppelen 12 · Zinnen bouwen 7 · Vertaling 4 · Waar of onwaar 3 · Zinsomvorming 1 · Schrijven 1.
- Writing model (#150): **90 words**, as the core.
- Build log: **0 warnings** (no FLOW OVERFLOW, no HEAD TOO WIDE). P6 exercise flow ends y=2569 — the core's exact position; P8 keys pack to exactly the core's 150 wrapped lines.

## 3. Key-diff registry (complete)

Registry-level diff vs the core: **keys differ at exactly {137, 138, 150}** — the family's translation/writing apparatus, as in every shipped IT fan-out:

| # | Core key (Chinese) | NL key |
|---|---|---|
| 137 | 周日我们多睡一个小时。 | `Op zondag slapen we een uur langer.` |
| 138 | 展览一直开放到四月。 | `De tentoonstelling blijft open tot april.` |
| 150 | （开放题，范文如下） | `(open vraag — het model staat hieronder)` — note: `Het model staat in sectie H van deze pagina (90 woorden)` |

Reverse items (stem re-aimed at Dutch, Italian key byte-identical): **#139** stem → `Zaterdag om 18:00: Napoli tegen Roma. → ___`; **#140** stem → `Elk cijfer moet een bron hebben. → ___`. All other 145 keys are byte-identical to the core; #86's note `5 − 3,4 = 1,6` is language-neutral and unchanged.

**Answer style:** the IT core prints its P8 keys in **dash style** `N. key — note` (verified in the core SVG), and this edition keeps the core's format code unchanged — notes' internal full-width parentheses became half-width. (The task brief's mention of a paren style does not match the core's own code/SVG; the core's evidence governs.)

**Note compressions (wording only, no key/geometry change):** 27 P8 notes were tightened so every printed key fits the core's one-line format in serif at 13.5 pt (items 3, 4, 6, 23, 32, 37, 40, 44, 45, 46, 51, 59, 62, 63, 73, 76, 78, 83, 90, 95, 133–139). Each was verified with the toolkit's own wrap metrics; meaning preserved in every case.

## 4. NL furniture (as shipped, verbatim)

- Masthead: `La Lucerna` (as the core ships); subtitle: `ITALIAANS WEEKBLAD · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA`; top strip: `OGNI SETTIMANA IN ITALIANO · ELKE WEEK · HET ITALIAANS DAT DE ITALIANEN LEZEN`.
- **Pairing badge (P1, replaces the core's Italian tagline call at (975, 372), 20 pt bold brick — the IT×PT/ES family precedent):** `TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`.
- Footers: `La Lucerna · ITALIAANS WEEKBLAD VOL.1 · TEKSTEN IN HET ITALIAANS · UITLEG IN HET NEDERLANDS` / `Pagina N van 8` (uninflected adjective, per tables.json + EN×NL/FR×NL).
- Gloss prefix: `Uitleg — `; P8 separators: `— Pagina N —`; section furniture follows the tables.json NL column (`IN QUESTO NUMERO · INHOUD`, `QUIZ LAMPO · BLITSQUIZ`, `RISPOSTE · ANTWOORDEN — per pagina gerangschikt: zoek op nummer`, etc.).

**Measured deviations (wording shortened, never geometry):**
1. P7 errors-box title ships as `ERRORI TIPICI · VEEL FOUTEN` — `VEELGEMAAKTE FOUTEN` measured 58 px of ink past the 434-wide box border.
2. P1 numbers box and P2 frase box titles take `tsize=20` (the IT×PT precedent for these two boxes): at the default 23 pt their ink crossed the box border by 6 px / 44.5 px.
3. Match-set instruction shortened to `Koppel woord en betekenis` on P2/P4/P8 (the full sentence ran past the page edge in the col-3 header row).
4. P6 group-A instruction ships as `Grafieken hierboven: kies het antwoord.` (one line; the two-line version cascaded the exercise flow 104 units past its bottom).
5. P7 col-3 stack glosses compressed to the core's exact line counts (errors glosses ×4, word-of-week gloss, letter disclaimer) so the stack ends at y=1674, above the FRASI rule at 1686 — the core's own clearance restored.
6. Word-of-week gloss ships as `anteprima = première. Op pagina 5 draaien films voor het eerst.` — the earlier wording's last line grazed its box border by 0.5 px of descender ink.

## 5. Gates (shared tools, final artifacts)

- **p8.py compare** (core P8 vs edition P8, total 150): `150 noted = 150 noted — status: CLEAN, missing=[], extra_count=0`. Printed-note set **EQUALS** the core's {1..150}. (The tool also lists keydiff=[12, 37, 58, 59, 62, 72, 78, 101, 137, 138]; the registry-level diff in §3 is authoritative — 137/138 are the real key changes, #150 prints as the ✓ line, and the rest are wrap-parse artifacts of the tool, spot-verified in the SVGs: printed keys at #12 `mezza` and #101 `Sono` are byte-identical to the core at identical y-coordinates.)
- **occlusion_audit.py** (selftest OK; run with `--core`): first run found **8 NEW flags**, all Dutch-length effects — 2 box titles (§4.2), 1 box title (§4.1), 1 page-edge instruction + 2 text overlaps (§4.3), P7 letter box struck by the FRASI rule + gloss/disclaimer overlap (§4.5). All fixed by wording; one residual 0.5 px descender graze fixed per §4.6. **Final run: 0 flags; NEW vs core: 0.**
- **freeze.py diff**: per-page text-multiset diff fully classified — every removal is either a Chinese explanation string replaced by Dutch, one of 11 pure-Latin items (the badge replacement §4, 8 × `— PAGINA N —` → `— Pagina N —`, and 2 re-wrap fragments whose Italian content was verified intact), or the §4.3 instruction. **Edition CJK total: 0 on all 8 pages; added CJK characters: 0.**
- P7 phrases: the 8 verbatim Italian quotes (page tags 1, 1, 2, 2, 3, 4, 5, 6) each occur exactly **2×** in the edition (article + P7 box), matching the core's counts.

## 6. Manovra honesty disclosure

Intact. The chart components (5,0 + 5,0 + 3,4 = 13,4) still do not sum to the printed total (≈23,5), and the frozen Italian caption ships byte-identical: `Tre voci pubblicate nel DPB del 15 ottobre — non è il totale della manovra (circa 23,5 miliardi).` / `Fonte: DPB, documento mandato a Bruxelles il 15 ottobre 2026.` The disclosure also survives in the Dutch layer: P6 item note `5 + 5 + 3,4 = 13,4 (niet het totaal)` and P8 key #85 `B — 5 + 5 + 3,4 = 13,4 (niet het totaal)`.

## 7. Images (inherited from the core KIT §8, verified there 2026-10-21 via the Wikimedia Commons API)

| Asset | Placement | Source | Licence |
|---|---|---|---|
| assets/atomuhr.jpg | P1 (NIST-F1 atomic clock, captioned as such) | NIST — File:Nist-f1.jpg | Public domain |
| assets/tartufo.jpg | P3 (white truffle *Tuber magnatum*) | Wikimedia Commons — File:Tuber Magnatum Pico.jpg | Public domain |
| assets/artemisia.jpg | P3 (Artemisia Gentileschi, *Judith Beheading Holofernes*, Naples version) | Wikimedia Commons — File:Gentileschi Artemisia Judith Beheading Holofernes Naples.jpg | Public domain |
| assets/chaplin.jpg | P5 (*The Gold Rush*, 1925, still) | Wikimedia Commons — File:Chaplin the gold rush boot.jpg | Public domain |
| assets/castagne.jpg | unused in this issue (as in the core) | Wikimedia Commons — File:Sugar-roasted chestnuts (1).jpg | CC0 |

## 8. Deliverable pins

- Print PDF `La-Lucerna-VOL1-NL.pdf`: **9,078,939 bytes**, sha256 `dc27f1a5b3a95ea1d96c4942366912baf240e54e9cafb462d891e7aea300c17f`
- Web PDF `La-Lucerna-VOL1-NL-web.pdf`: **3,627,469 bytes** (< 10 MB), sha256 `e15d2a51205bd6a1b20d210d1198ef946019a7bec093f18be811814ded1fc0e8`
- `svg/` ×8 and `cards/` ×8 (1950×2700) in this directory.

## 9. Proofread record

- **Builder's full pass: DONE.** All 8 pages read end-to-end in the final render; all 150 keys re-derived (registry diff = §3, nothing else); every weekday/date claim checked against the real 2026 calendar (clock change Sun 25 Oct; Artemisia opens Wed 21 Oct; Napoli–Roma Sat 24 Oct 18:00; vote slips to Wed 28 Oct; Lucca opens Wed 28 Oct; Allerheiligen Sun 1 Nov — all correct); totals = core; Manovra disclosure verified on P6 and P8 (§6).
- **Independent proofread: PASS** (2026-10-21, fresh independent pass over the final artifacts, zero problems; no fixes required, no re-render). Verified: freeze.py baseline 8/8 byte-identical + core hashes unchanged start→end (bd04af2f…/ff75206e…/9ce43c3d…/aac8356c…/079552c8…/5d553abe…/9b4daf76…/58f37fd4…); freeze.py diff fully classified, edition CJK = 0 / added CJK = 0 on all pages; fresh registry dumps from both builds — 150 = 150, page/level meta identical, registry key diffs exactly {137, 138, 150} as §3; p8.py compare independently CLEAN 150 = 150 EQUAL (the tool's extra keydiff numbers are note-language/segmentation artifacts — #12 «mezza» and #101 «Sono» print byte-identical keys at identical y-coordinates 1732.24 / 2088.16 in both editions); occlusion_audit.py (selftest first) 0 flags, 0 NEW vs core, with pixel adjudication of every builder-fixed site (errors-box title, letter box vs FRASI rule, word-of-week gloss, P1/P2 tsize=20 titles, P6 instruction) — all clear; Manovra disclosure intact (frozen P6 caption byte-identical; #85 note «5 + 5 + 3,4 = 13,4 (niet het totaal)» on P8; #86 byte-identical); dash-style adjudication confirmed from core code + SVG; P7's 8 quotes verbatim, each exactly 2× in both editions, tags (1,1,2,2,3,4,5,6); all weekday/date claims re-verified against the real 2026 calendar; writing model hand-counted at exactly 90 words, byte-identical to the core; ~75 keys re-derived by hand from the articles — all correct; all 27 compressed notes (§3) spot-checked semantically equivalent; images byte-identical per page, credits byte-identical to the core (KIT §8 table matches); banned intermediary term 0 in SVGs/KIT/operative code (`expl()` rename complete; only CJK in code is the inherited non-rendering svglib.py docstring). Final pins re-measured from disk: web 3,627,469 B / e15d2a51205bd6a1b20d210d1198ef946019a7bec093f18be811814ded1fc0e8; print 9,078,939 B / dc27f1a5b3a95ea1d96c4942366912baf240e54e9cafb462d891e7aea300c17f. Proofreader scratch: `hidden_files/proof-it-nl/scratch/`.
