# WEEKLY-KIT · 2026-w46-es-fr — La Lucerna, Spanish Weekly VOL.3, explanations in French

Slug: `2026-w46-es-fr`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: French, written natively.
Build dir: `hidden_files/weekly-report-w46-es-fr-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_fr.py` + `t_fr2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-fr.pdf` 3,480,500 B; web PDF `2026-w46-es-fr.web.pdf` 410,179 B (<7 MB), text layer 47,205 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W45 ES×FR KIT §2, VOL.2→VOL.3 only)

- Badge replaces the y=372 subtitle slot, 20pt bold BRICK: `TEXTES EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`.
- Edition line: `HEBDOMADAIRE ESPAGNOL · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `CADA SEMANA EN ESPAÑOL · CHAQUE SEMAINE · L'ESPAGNOL DES ESPAGNOLS`.
- Band right: `LA CAMPAGNE COMMENCE VENDREDI 13 · GRÈVE MERCREDI 11` / `À LA UNE · VOIR PAGES 2 ET 6`.
- Footer: `La Lucerna · HEBDOMADAIRE ESPAGNOL VOL.3 · TEXTE EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS` / `Page N sur 8`.
- Gloss prefix `Note — `; P1 explanation line prefix `Notes — `, `terme = gloss` entries; `bridge()` kept.
- Section heads: VIDA · VIE QUOTIDIENNE, CULTURA · CULTURE, DEPORTE · SPORT, JUVENTUD · JEUNESSE, A FONDO · EN PROFONDEUR, LENGUA · LANGUE, EJERCICIOS Y RESPUESTAS · EXERCICES ET RÉPONSES.
- Box titles: LA SEMANA EN CIFRAS · EN CHIFFRES (tsize=20), EL CALENDARIO · LE CALENDRIER, EN ESTA EDICIÓN · SOMMAIRE, BREVES · EN BREF, QUIZ RELÁMPAGO · QUIZ ÉCLAIR, LA NOTICIA · À LA UNE, AHORA TÚ · À TOI DE JOUER, ERRORES TÍPICOS · ERREURS TYPES (20pt), LA PALABRA · MOT DE LA SEMAINE, FRASES DE LA SEMANA · PHRASES DE LA SEMAINE (MOT POUR MOT, TIRÉES DE CE NUMÉRO), LA PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.4); plan box `EL PLAN DE LA SEMANA · LE PLAN` (tsize=20).
- Exercise headers `EJERCICIOS · EXERCICES` (no page number) + right note `Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro`.
- P8 header `RESPUESTAS · CORRIGÉS — classés par page, cherchez le numéro` + `Une courte explication en français pour chaque exercice · ✓ = exercice d'écriture`; P8 band sub `Page 8 · La gran prueba de la semana + todas las respuestas`.
- Separator stays Spanish `— PÁGINA N —`; quotes tags `Página N` frozen; `¿Y TÚ? · ET TOI?`; five-keys note `Cinq clés, sans chiffres inventés.`; P7 band sub `Focus langue · Tres niveles, tres herramientas · Trois niveaux, trois outils`.
- Disclosure: `Note de la rédaction : sans lettre réelle ni meilleur texte de la page 8, voici notre exemple ; promesse reportée au VOL.4.` (all facts kept; the invitation tail dropped for fit, as in DE).
- Type names frozen Chinese (registry-internal); instr labels: Compléter / Vrai ou faux / Former une phrase / Reformuler / Traduire / Écrire / Associer; `原形` → `infinitif`; translation items re-aimed as in EN.

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to French source sentences; bodies 139/140 re-aimed to French; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK 0 on every page; edition CJK 0.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-fr-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 47,517 B, identical to print text; <7 MB.
- Visual: P1, P6, P7 cards inspected — badge, CIFRAS title inside its box, word note one line, charts legible, letters box with disclosure inside, preview band clear of the footer rule.

## 5. Fixups (French apparatus only; core geometry and Spanish text untouched)

1. First build: 32 occlusion flags — P6 exercise flow overflow (+82px past the footer), P8 answer flow overflow (items 146–150 overprinting), P7 col-3 at 1918.1 pushing the preview band onto the footer rule, P1 word-note 2nd line crossing the y=1844 rule, CIFRAS box title crossing its box border (ink 976.8 > 961). Fixed: P6 18.5pt/gap2 + P8 13.2pt/1.12 (EN/NL precedent); P7 trims (disclosure shortened, palabra note shortened to one sentence); P1 word note → one line `« Grève générale » : arrêt de travail de 24 heures.`; CIFRAS title tsize=20.
2. Rebuilt: zero overflows, P7 col-3 1831.1 (≈ core 1834), 0 occlusion flags. Core letters-box fix inherited via rebuild (disclosure inside its box).

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py fr t_fr` (copies the fixed core build, applies `t_fr.py` + `t_fr2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-fr-diff.json`, `es-fr-p8-compare.json`, `es-fr-occlusion.json`, `es-fr-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader fr --week 2026-w46` (`--check` dry-run clean first). Mode latin; `_D5_READER = "fr"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 504, D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 0 all Newsreader; Noto Sans 0.
- run1 gates 16/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- run1 G6 TEXTX: P1 band headline overlapped the translation line by 225.0x20.8px; fixed by the band size above.
- `content12.py:26` — band headline 46 -> 35 (gap +11.7px)
- `content12.py:45` — P1 numbers tsize 20 -> 19 (margin 9.1px)
- `content12.py:92` — P1 sommaire 24 -> 23.5 (margin 5.7px)
- `content12.py:185` — P2 calendar f.box tsize added 21 (was default 23) (margin 9.2px)
- `content7.py:90` — P7 word 23 -> 20.5 (margin 2.1px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 259 (run-split). G12 20 titles, 278 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 236 rows, slack 45.8px. G15a text-layer diff 0; text.md DIFF 122 lines, native verifier ADOPT (REWRAP 33, 0 UNEXPECTED). G15b CARRYOVER FAIL svg=5742 md=7212 (record-only, D27).
- D18 gap 18.5px; D37 N/A (no badge line in the box zone; strapline y=372 above box top 588); D39(4) P7 band bottom vs footer 2596: -57.4px.
- Old (baseline build) print `La-Lucerna-VOL3-es-fr.pdf` 4,064,165 B SHA256 `bf7cdd111340b6b6eb815c5dbef26c8ec4b8722b7d8325047968dcc9affe6890`; web 487,709 B SHA256 `7904c676e0491acf6bb0cd541646c3f8e8b1d819459ea4ae0007519f9deee0f1`.
- New (run2) print `La-Lucerna-VOL3-es-fr.pdf` 3,480,500 B SHA256 `7145519505303d50e4bf06052496cb02915e99f259f03575b6b7c39e1c6b1441`; web `2026-w46-es-fr.web.pdf` 410,179 B SHA256 `f33bbae5cae4833bb2734620114c5f7cdb94980117dcc99d2879e8e4f94b1955`; text.md 47,366 B SHA256 `9be9217d9f31ae2df15a7739398a83ed2fe4bb1ffa5f49647aa2544c437fb402` (textexp output, `logs/2026-w46-es-fr/2026-w46-es-fr.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-fr/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-fr/g*-run2.log`, `logs/2026-w46-es-fr/census-run2.json`, `logs/2026-w46-es-fr/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-fr-D5-REPORT.md`.
