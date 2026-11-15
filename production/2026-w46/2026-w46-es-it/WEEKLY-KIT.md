# WEEKLY-KIT · 2026-w46-es-it — La Lucerna, Spanish Weekly VOL.3, explanations in Italian

Slug: `2026-w46-es-it`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Italian, written natively.
Build dir: `hidden_files/weekly-report-w46-es-it-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_it.py` + `t_it2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-it.pdf` 3,477,440 B; web PDF `2026-w46-es-it.web.pdf` 407,145 B (<7 MB), text layer 46,522 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W43/W45 ES×IT precedent, VOL.2→VOL.3 only)

- Badge: INSERTED line at y=574, 22pt bold BRICK (strapline y=372 retained): `TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`.
- Edition line: `SETTIMANALE SPAGNOLO · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip (W43 shortened form, kept verbatim): `CADA SEMANA EN ESPAÑOL · OGNI SETTIMANA · LO SPAGNOLO DEGLI SPAGNOLI`.
- Band right: `LA CAMPAGNA INIZIA VENERDÌ 13 · SCIOPERO MERCOLEDÌ 11` / `Il tema di copertina · vedi le pagine 2 e 6`.
- Footer: `La Lucerna · SETTIMANALE SPAGNOLO VOL.3 · TESTI IN SPAGNOLO · SPIEGAZIONI IN ITALIANO` / `Pagina N di 8`.
- Gloss prefix `Nota — ` (vocab boxes `termine = gloss`); `bridge()` kept with bare style (core `讲解｜` prefix dropped, not translated).
- Bands: VIDA · VITA QUOTIDIANA, CULTURA · CULTURA, DEPORTE · SPORT, JUVENTUD · GIOVENTÙ, A FONDO · APPROFONDIMENTO, LENGUA · LA LINGUA, EJERCICIOS Y RESPUESTAS · ESERCIZI E RISPOSTE. Band subtitles Italian second half; P8 band `Pagina 8 · La gran prueba de la semana + todas las respuestas` (Spanish descriptor kept, Italian page marker only, W43 ruling).
- Box titles: LA SEMANA EN CIFRAS · IN CIFRE, EL CALENDARIO · IL CALENDARIO, EN ESTA EDICIÓN · IL NUMERO, BREVES · IN BREVE, QUIZ RELÁMPAGO · QUIZ LAMPO, LA NOTICIA · LA NOTIZIA, AHORA TÚ · TOCCA A TE, ¿Y TÚ? · TOCCA A TE, ERRORES TÍPICOS · ERRORI TIPICI, LA PALABRA · LA PAROLA, FRASES DE LA SEMANA · LE FRASI DELLA SETTIMANA (testuali, da questo numero), LA PRÓXIMA SEMANA · LA PROSSIMA SETTIMANA (VOL.4), EJERCICIOS · ESERCIZI · PAGINA N, EL PLAN DE LA SEMANA · IL PIANO (tsize=20, shortened per W45 §5.4), RESPUESTAS · LE RISPOSTE — ordinate per pagina: cerca il numero (+ right note `Una nota in italiano per ogni risposta · ✓ = testo modello`).
- Exercise right note: `Risposte a pagina 8 · livelli misti: cerca per numero`. P8 separator stays Spanish `— PÁGINA N —`.
- Type names frozen Chinese (registry-internal, W45 IT precedent); instr labels: Completa · Vero o falso · Costruisci · Riscrivi · Traduci · Scrivi · Abbina le parole; `原形` → `infinito`.
- P6/P8 sizes pre-applied per W45 IT §5.1–5.2: P6 exercises 18.5pt/gap2, P6 §A bridge shortened to `Guarda i grafici e scegli.`; P8 answers 13.2pt/1.12. P1 word note one line; disclosure kept at 4 lines with all facts + invitation.

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Italian source sentences; bodies 139/140 re-aimed to Italian; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK 0 on every page; edition CJK 0.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-it-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer present and consistent with print text; <7 MB.
- Visual: P1 and P7 cards inspected — badge, word note, letters box with disclosure inside, preview band clear of the footer rule. (W45 IT §5.6 palabra box-bottom graze did not recur: no EDGE flag.)

## 5. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 6. Reproduction

`python3 hidden_files/w46/build_one.py it t_it` (copies the fixed core build, applies `t_it.py` + `t_it2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-it-diff.json`, `es-it-p8-compare.json`, `es-it-occlusion.json`, `es-it-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader it --week 2026-w46` (`--check` dry-run clean first). Mode latin; `_D5_READER = "it"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 499, D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 0 all Newsreader; Noto Sans 0.
- run1 gates 16/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- run1 G6 TEXTX: P1 band headline overlapped the translation line by 185.5x25.5px; fixed by the band size above.
- `content12.py:27` — band headline 46 -> 37 (gap +8.2px)
- `content12.py:50` — P1 numbers f.box tsize added 21.5 (was default 23) (margin 10.0px)
- `content12.py:93` — P1 sommaire 24 -> 23.5 (margin 4.7px)
- `content12.py:186` — P2 calendar f.box tsize added 21.5 (was default 23) (margin 4.5px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 266 (run-split). G12 22 titles, 274 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 231 rows, slack 58.5px. G15a text-layer diff 0; text.md DIFF 128 lines, native verifier ADOPT (REWRAP 34, 0 UNEXPECTED). G15b CARRYOVER FAIL svg=5569 md=7139 (record-only, D27).
- D18 gap 7.9px; D37 margin=106.4px; D39(4) P7 band bottom vs footer 2596: -25.9px.
- Old (baseline build) print `La-Lucerna-VOL3-es-it.pdf` 4,061,333 B SHA256 `262601e7f20cc80ae54e8c13b98b057744e3c24dd17da78c1a824d136caab8ce`; web 483,864 B SHA256 `822ddeef92f5becccfc5a2f8f18fede09c643ed2c535d712f65b1ce7da1b1921`.
- New (run2) print `La-Lucerna-VOL3-es-it.pdf` 3,477,440 B SHA256 `543439c04489e9b6d01fb64bd61dd9da4ed6f23bdc243d93a143bb0cc17142a2`; web `2026-w46-es-it.web.pdf` 407,145 B SHA256 `25f1f7b2b58f85b955abe44745422bfe090840b0ab1395b57d0d55d9283729dd`; text.md 46,715 B SHA256 `11c2fc4dcfb1ae65cf85bdcb2b454836e00f569c057695868a258567feceb0c9` (textexp output, `logs/2026-w46-es-it/2026-w46-es-it.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-it/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-it/g*-run2.log`, `logs/2026-w46-es-it/census-run2.json`, `logs/2026-w46-es-it/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-it-D5-REPORT.md`.
