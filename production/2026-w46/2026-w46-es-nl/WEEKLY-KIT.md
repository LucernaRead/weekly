# WEEKLY-KIT · 2026-w46-es-nl — La Lucerna, Spanish Weekly VOL.3, explanations in Dutch

Slug: `2026-w46-es-nl`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Dutch, written natively.
Build dir: `hidden_files/weekly-report-w46-es-nl-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_nl.py` + `t_nl2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-nl.pdf` 3,482,208 B; web PDF `2026-w46-es-nl.web.pdf` 411,903 B (<7 MB), text layer 46,432 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W45 ES×NL KIT §5, VOL.1→VOL.3 only)

- Badge replaces the y=372 subtitle slot, 19.5pt: `TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS`.
- Edition line: `SPAANS WEEKBLAD · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `CADA SEMANA EN ESPAÑOL · ELKE WEEK · HET SPAANS VAN SPANJE` — see deviation in §5 (the W43 verbatim third segment collides with the longer W46 date line).
- Band right: `DE CAMPAGNE BEGINT VRIJDAG 13 · STAKING WOENSDAG 11` / `Hoofdverhaal · zie pagina 2 en 6`.
- Footer: `La Lucerna · SPAANS WEEKBLAD VOL.3 · TEKSTEN IN HET SPAANS · UITLEG IN HET NEDERLANDS` / `Pagina N van 8`.
- Gloss prefix `Uitleg — `; `bridge()` → `expl()` (definition and all call sites).
- Bands: VIDA · Leven / CULTURA · Cultuur / DEPORTE · Sport / JUVENTUD · Jeugd / A FONDO · Achtergrond / LENGUA · Taal / EJERCICIOS Y RESPUESTAS · Oefeningen en antwoorden.
- Exercise headers `EJERCICIOS · Oefeningen van pagina N`; right note `Antwoorden op pagina 8 · Niveaus door elkaar — zoek op nummer`.
- P8 separator `— Pagina N —` (unaccented); P7 phrase tags `(Pagina N)` (unaccented).
- P8 header: `RESPUESTAS · Antwoorden — per pagina gerangschikt; zoek op nummer` / `Bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst`.
- Type names translated: Zinnen aanvullen 48 · Meerkeuze 47 · Cloze-meerkeuze 13 · Woorden combineren 12 · Zinnen omvormen 10 · Lezen: waar/onwaar 8 · Zinnen maken 7 · Vertalen 4 · Schrijven 1. P8 check `== "Schrijven"`.
- Instruction chips: Vul in / W/NW / Zinnen maken / Herschrijf / Vertalen / Schrijven / Combineer. Apparatus `(原形 …)` → `(infinitief …)`.
- Word note (one line): `«La huelga general»: iedereen staakt één dag.`
- Disclosure: `Opmerking: geen echte brieven; daarom een voorbeeldbrief. Belofte: VOL.4.` (the no-best-P8-texts fact stands in the Spanish disclosure above — DE precedent; shortened by one line for fit, see §5).

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Dutch source sentences; bodies 139/140 re-aimed to Dutch; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK 0 on every page; edition CJK 0.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-nl-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 46,760 B, identical to print text; <7 MB.
- Visual: P1, P7 inspected — top strip clear of the date line (after the §5 fix), CIFRAS title inside its box, letters box with disclosure inside, preview band clear of the footer rule.

## 5. Fixups (Dutch apparatus only; core geometry and Spanish text untouched)

1. P6 exercises 18.5pt/gap2 + P8 answers 13.2pt/1.12 pre-applied (W45 NL fixups, W45 ES×NL KIT §5).
2. Box titles: `LA SEMANA EN CIFRAS · De week in cijfers` crossed its box border (ink 1025.5 > 961) and overlapped the B1 chip — replaced by `LA SEMANA EN CIFRAS · De cijfers` at tsize=20 (337.5px ≤ 394px slot). `LA PALABRA · Het woord van de week` crossed its box border (ink 1905.8 > 1885) — shortened to `LA PALABRA · Woord van de week` at the core 23pt (388.8px ≤ 412px slot).
3. P7 col-3 ran 26px long (1860.1 vs core 1834), which would have pushed the preview band onto the footer rule: disclosure shortened by one line (see §2).
4. Top strip: the W43 verbatim strip (`… HET SPAANS DAT DE SPANJAARDEN LEZEN`) ends at x=1403.3 by venv measurement while the W46 date line starts at x=1408.9 — a 5.6px nominal gap that renders as a visible `LEZENSEMANA` collision (the canonical audit does not flag header-zone text/text grazes; caught visually, same defect class as PT F1b). Fixed with `HET SPAANS VAN SPANJE` (ends x=1319.7, 89px clear). Rebuilt and re-gated: 0 flags, P1 visually clean.
5. Core letters-box fix inherited via rebuild from the fixed core build.

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py nl t_nl` (copies the fixed core build, applies `t_nl.py` + `t_nl2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-nl-diff.json`, `es-nl-p8-compare.json`, `es-nl-occlusion.json`, `es-nl-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader nl --week 2026-w46` (`--check` dry-run clean first). Mode latin; `_D5_READER = "nl"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 503, D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 0 all Newsreader; Noto Sans 0.
- run1 gates 16/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- run1 G6 TEXTX: P1 band headline overlapped the translation line by 175.0x20.8px; fixed by the band size above.
- `content12.py:26` — band headline 46 -> 37 (gap +18.7px)
- `content12.py:92` — P1 sommaire 24 -> 22.5 (margin 4.7px)
- `content56.py:22` — P5 plan tsize 20 -> 19 (margin 7.8px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 258 (run-split). G12 24 titles, 276 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 239 rows, slack 46.8px. G15a text-layer diff 0; text.md DIFF 108 lines, native verifier ADOPT (REWRAP 28, 0 UNEXPECTED). G15b CARRYOVER FAIL svg=5596 md=7196 (record-only, D27).
- D18 gap 72.4px; D37 N/A (no badge line in the box zone; strapline y=372 above box top 588); D39(4) P7 band bottom vs footer 2596: -30.9px.
- Old (baseline build) print `La-Lucerna-VOL3-es-nl.pdf` 4,068,620 B SHA256 `803b5879b5e4aacee6b03f620f788d0ebef77bc63d77dd7371b46c0095913f40`; web 492,312 B SHA256 `66abe1a822dc952c08d76d83c7492b5a305a43189363bde66c0abad45a91ec88`.
- New (run2) print `La-Lucerna-VOL3-es-nl.pdf` 3,482,208 B SHA256 `69855a88e5a360a87cfdb86061c66f712825eaa8758d5512f061eb90e0d4ab72`; web `2026-w46-es-nl.web.pdf` 411,903 B SHA256 `b2bae05871d1216f12c5d1ef4c53d0fbe5844e8dcc37346beda4cfdf4ea890a5`; text.md 46,632 B SHA256 `d1068dc7b89c7066217201410a93ccc9cb5440eb0c8df503a239a6bbf7d575c5` (textexp output, `logs/2026-w46-es-nl/2026-w46-es-nl.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-nl/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-nl/g*-run2.log`, `logs/2026-w46-es-nl/census-run2.json`, `logs/2026-w46-es-nl/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-nl-D5-REPORT.md`.
