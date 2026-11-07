# WEEKLY-KIT · 2026-w46-es-fr — La Lucerna, Spanish Weekly VOL.3, explanations in French

Slug: `2026-w46-es-fr`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: French, written natively.
Build dir: `hidden_files/weekly-report-w46-es-fr-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_fr.py` + `t_fr2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-FR.pdf` 4,577,684 B; web PDF `La-Lucerna-VOL3-FR-web.pdf` 516,363 B (<7 MB), text layer 47,517 B via `pdftotext`, byte-identical to the print PDF's text.
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
