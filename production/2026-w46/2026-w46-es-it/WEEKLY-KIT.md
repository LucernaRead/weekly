# WEEKLY-KIT · 2026-w46-es-it — La Lucerna, Spanish Weekly VOL.3, explanations in Italian

Slug: `2026-w46-es-it`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Italian, written natively.
Build dir: `hidden_files/weekly-report-w46-es-it-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_it.py` + `t_it2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-IT.pdf`; web PDF `La-Lucerna-VOL3-IT-web.pdf` (<7 MB) with a real text layer via `pdftotext`, consistent with the print text.
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
