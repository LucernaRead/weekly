# WEEKLY-KIT · 2026-w46-es-de — La Lucerna, Spanish Weekly VOL.3, explanations in German

Slug: `2026-w46-es-de`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: German, written natively.
Build dir: `hidden_files/weekly-report-w46-es-de-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_de.py` + `t_de2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-DE.pdf` 4,641,027 B; web PDF `La-Lucerna-VOL3-DE-web.pdf` 527,654 B (<7 MB), text layer 47,074 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W43 ES×DE precedent, VOL.1→VOL.3 only)

- Badge: INSERTED line at y=574, 22pt BRICK (tagline y=372 stays Spanish): `SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`.
- Edition line: `SPANISCHE WOCHENZEITUNG · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `CADA SEMANA EN ESPAÑOL · JEDE WOCHE · SPANISCH, WIE SPANIEN ES LIEST`.
- Band right: `WAHLKAMPF AB FREITAG, 13. · GENERALSTREIK AM MITTWOCH, 11.` / `TITELTHEMA · SEITEN 2 UND 6`.
- Footer: `La Lucerna · SPANISCHE WOCHENZEITUNG VOL.3 · TEXT AUF SPANISCH · ERKLÄRUNGEN AUF DEUTSCH` / `Seite N von 8`.
- Gloss prefix `HINWEIS · `; P1 explanation line prefix `Hinweis · `, `term + German article + gloss` style; gloss boxes `term gloss` (space-separated, no `=`).
- Section heads: VIDA · LEBEN, CULTURA · KULTUR, DEPORTE · SPORT, JUVENTUD · JUGEND, A FONDO · HINTERGRUND, LENGUA · SPRACHE.
- Exercise headers `EJERCICIOS · Übungen zu Seite N`; right note `Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen`.
- P8 band `EJERCICIOS Y RESPUESTAS · ÜBUNGEN UND ANTWORTEN` / `Seite 8 · La gran prueba de la semana + todas las respuestas`; P8 header `RESPUESTAS · ANTWORTEN — nach Seiten geordnet` / `Zu jeder Aufgabe ein deutscher Kurzhinweis · ✓ = Schreibaufgabe`.
- Separator stays Spanish `— PÁGINA N —`; quotes tags `Página N` frozen; P7 errors title at 20pt (`ERRORES TÍPICOS · TYPISCHE FEHLER`).
- `bridge()` kept. Type names stay frozen Chinese (registry-internal keys, W45 DE precedent, adjudicated); only `instr=` labels translate (Ausfüllen / Richtig oder falsch / Sätze bilden / Umformen / Übersetzen / Schreiben / Zuordnen); P8 check stays `== "写作"`. Writing bridge/key/note translated; key 150's change is not visible to `p8.py compare` (writing items print `N. ✓ note`).

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to German source sentences (W45 ES×DE ruling); bodies 139/140 re-aimed to German; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK 0 on every page; edition CJK 0.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-de-occlusion2.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 47,074 B, identical to print text; <7 MB.
- Visual: P1 and P7 cards inspected — badge, five-keys note, word note, letters box (disclosure inside its box after the core letters-box fix, §5), preview band clear of the footer rule.

## 5. Fixups (German apparatus only; core geometry and Spanish text untouched except §5)

1. First build: P6 + P8 FLOW OVERFLOW, P7 col-3 at 1932.1, 3 occlusion flags (five-keys note past page edge; word-note 2nd line crossing the y=1844 rule; P5 plan title crossing its box). Fixed: P6 18.5pt/gap2 + P8 13.2pt/1.12; P7 trims (disclosure, word note, `gente` clinic note); five-keys note → `Fünf Themen, keine erfundenen Zahlen.`; word note → one line; plan title → `EL PLAN DE LA SEMANA · Wochenplan` at tsize=20.
2. Second build: disclosure still spilled one line below the letters box (para-vs-wrap underestimate, the same defect class as the core's — see §5). Fixed with the W45 DE disclosure form: `Anmerkung der Redaktion: Keine echten Briefe eingegangen — daher dieser Beispielbrief. Versprechen gilt für VOL.4!` (the no-best-P8-texts fact stands in the Spanish disclosure directly above it). Rebuilt: P7 col-3 = core value, 0 flags.
3. Core letters-box fix (§5 below) inherited via rebuild from the fixed core build: disclosure's last line now sits inside the box (baseline 1824 < box bottom 1834).

## 6. Promises, sources, credits

Promises honoured as in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced anywhere; reader letters: labelled editor's example (Ana) + bilingual disclosure stating no real letters/best P8 texts had arrived, promise carried to VOL.4 — no reader fabricated. Sources, image credits (CC0 `castanas.jpg` P3; editorial line art P1; typographic INFAMIA plate P5) and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py de t_de` (copies the fixed core build, applies `t_de.py` + `t_de2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-de-diff2.json`, `es-de-p8-compare2.json`, `es-de-occlusion2.json`, `es-de-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## 8. Fix record — Round 1 proofread defect D-1 (fix worker, 2026-11-02/03)

Defect D-1 (BLOCKING, P7 golden sentences Q6): the German translation of the frozen Spanish quote was ungrammatical — German *sorgen* cannot take an accusative object.

- Frozen Spanish quote (unchanged): `«La vivienda preocupa al 86,9 % de los españoles.»`
- Before: `Die Wohnung sorgt 86,9 % der Spanier. (Página 6)`
- After: `86,9 % der Spanier sorgen sich um die Wohnung. (Página 6)`
- Source fix (no SVG/PDF hand-edit): `hidden_files/w46/t_de2.py` line 107, transform pair for content7.py. Wording chosen to match this edition's own correct usage in DE P8 answer 127 (`CIS-Wohnungsbarometer: 86,9 % sorgen sich um die Wohnung`). The `(Página 6)` page label is unchanged.
- Re-render: full rebuild via `python3 hidden_files/w46/build_one.py de t_de` from the fixed core build; 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises (A2 50 / B1 72 / B2 28; per page 10/18/18/18/18/18/12/38). SVG change isolation: only `svg/p7-lengua.svg` changed (sha256 changed); P1–P6 and P8 byte-identical to the pre-fix render.
- Re-gates (final artifacts): `tools/freeze.py diff` — added CJK 0 on every page, edition CJK 0; `tools/p8.py compare` — CLEAN, 150/150, keydiff=[137, 138] (adjudicated re-aiming, unchanged); `tools/occlusion_audit.py` — 0 flags, selftest OK; P6 re-wrap = reflow only (non-CJK word-multiset lost = only the replaced footer words LUCERNA/SPANISH/WEEKLY); P7 quotes verified 8/8 (all Spanish quotes verbatim in exactly one article page + P7; all 8 German translations present, Q6 fixed); counts re-measured from SVGs 150 with the Round 1 stem sequences; same-baseline scan 0 reports.
- PDFs: print `La-Lucerna-VOL3-DE.pdf` 4,641,037 B; web `La-Lucerna-VOL3-DE-web.pdf` 527,663 B (<7 MB) via `tools/webpdf.py`; `pdftotext` 47,065 B, byte-identical web vs print (`cmp` passed). `.text.md` regenerated with `hidden_files/w46/es_textmd.py` from the edition's own SVG text layer (47,072 B; diff vs pre-fix = exactly the Q6 line; headers preserved verbatim).
- Visual: DE P7 card viewed full-frame — Q6 translation on one clean line under the frozen quote, no overflow/overlap. Gate outputs + build log: `hidden_files/w46/es-fix/` (`es-de-build.log`, `es-de-diff.json`, `es-de-p8-compare.json`, `es-de-occlusion.json`); fix report: `hidden_files/w46/es-fix/FIX-REPORT.md`. Round 2 independent proofread still outstanding — this record does not replace it. No other edition touched.

## 9. Fix record — Round 2 proofread defect D-6 (fix worker, Round 3, 2026-11-03)

Defect D-6 (BLOCKING, DE only, P2 ¿Y TÚ? box): the German question used transitive *sorgen* with an accusative object — the same ungrammatical construction as Round 1 D-1. A Round 1 miss, not a fix regression: P2 was untouched by the Round 1 fix, and the Round 2 freeze-diff comparison shows P2 identical pre/post Round 1 fix.

- Before: `Was sorgt dich am meisten: Löhne, Wohnungen oder Preise?`
- After: `Was beunruhigt dich am meisten: Löhne, Wohnungen oder Preise?`
- Full corrected sentence (source): `Was machst du am Mittwoch, 11. November: streiken, arbeiten oder zu Hause bleiben? Was beunruhigt dich am meisten: Löhne, Wohnungen oder Preise? Schreib zwei Sätze auf Spanisch an die Redaktion.`
- Source fix (no SVG/PDF hand-edit): `hidden_files/w46/t_de.py` line 68, transform pair for content12.py (the ¿Y TÚ? explanation string). Wording chosen by wrap simulation with the build's own `svglib.wrap` at the true draw settings (sans 20pt, width 390): `beunruhigt` keeps the identical 6-line breaks of the defective render (only line 3 changes word; line width 372.4px < 390px), while the `Sorgen`-noun alternatives rewrap three lines; `beunruhigen` is the correct transitive worry verb matching the siblings' correct worry-verbs (EN *worries*, FR *inquiète*, RU *беспокоит*). The three options (Löhne, Wohnungen, Preise) and the box's meaning are unchanged; the frozen Spanish prompt above the box is unchanged.
- Re-render: full rebuild via `python3 hidden_files/w46/build_one.py de t_de` from the fixed core build; 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises (A2 50 / B1 72 / B2 28; per page 10/18/18/18/18/18/12/38); P2 col3 ends at y=1081.5, identical to the pre-fix render. SVG/card change isolation (sha256, all 12 ES dirs incl. core): only `svg/p2-vida.svg` and `cards/p2-vida.png` changed; P1, P3–P8 SVGs/cards byte-identical; the KO edition and the other 9 editions byte-identical (only the two PDFs and `.text.md` also change, as re-rendered outputs of the one changed SVG).
- Re-gates (final artifacts, independently re-run): `tools/freeze.py diff` — added CJK 0 on every page, edition CJK 0; `tools/p8.py compare` — CLEAN, 150/150, keydiff=[137, 138] (adjudicated re-aiming, unchanged); `tools/occlusion_audit.py` — 0 flags, selftest OK (all 6 planted classes fired exactly once, clean controls silent); same-baseline scan — 0 reports (1,589 `<text>` parsed); counts re-measured from SVGs — 150, stem sequences per page 10/18/18/18/18/18/12/38, all seq-ok; P7 quotes — 8/8 Spanish quotes verbatim in exactly one article page + P7, 8 translation lines with `(Página N)` tags, Q6 fixed translation re-verified verbatim; defective string `Was sorgt dich` — 0 occurrences in the joined edition text and in every SVG; corrected question renders complete in the joined text (1 occurrence).
- PDFs: print `La-Lucerna-VOL3-DE.pdf` 4,641,045 B; web `La-Lucerna-VOL3-DE-web.pdf` 527,672 B (<7 MB) via `tools/webpdf.py`; `pdftotext` 47,070 B (>0), byte-identical web vs print (`cmp` passed; +5 B vs Round 2's 47,065 B = exactly the `beunruhigt`/`sorgt` length delta). `.text.md` regenerated with `hidden_files/w46/es_textmd.py` from the edition's own SVG text layer (47,077 B; diff vs pre-fix = exactly the one fixed line; header preserved verbatim).
- Visual: DE P2 card viewed full-frame — the corrected question renders completely and grammatically inside the ¿Y TÚ? box, no overflow/overlap; P1/P8 spot-checked, clean and unchanged. Gate outputs + build log: `hidden_files/w46/es-fix-round3/`; fix report: `hidden_files/w46/es-fix-round3/FIX-REPORT.md`. Round 3 independent proofread still outstanding — this record does not replace it. No other edition touched. The Round 2 correction on the "`12 de noviembre`" record claim (frozen-core inheritance in P8 item 122, not a defect) was left untouched, as instructed.
