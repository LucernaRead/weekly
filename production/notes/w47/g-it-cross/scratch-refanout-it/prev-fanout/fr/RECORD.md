# it-fr RECORD — COMPLETE (build1, 2026-11-11)

## Deliverables
- Print PDF `La-Lucerna-VOL4-FR.pdf` — 14,034,268 bytes, sha256 `5445d1a62f631bb75cafcb20df40c376d44b608254824444166714670f2dc0c7`
- Web PDF `La-Lucerna-VOL4-FR-web.pdf` — 1,258,939 bytes, sha256 `416b11053b82475ad84bcb1badc10d992357a3e0fbde1786c55bee693bb3c0a8`
- `2026-w47-it-fr.text.md` — 56,616 bytes, 1317 lines, 150 exercises (exported from production sources)
- `ABSTRACT.txt` (French, one line, no ASCII double quotes — full text in `build_edition.py` ABSTRACTS and in the edition WEEKLY-KIT.md §7)
- `WEEKLY-KIT.md` written (mirror of the en/de KIT structure; fr numbers §7/§8)
- 8 SVG in `svg/` + 8 cards in `cards/`

## Gates — ALL PASS (`fr/gates2.log`)
- run.py rc 0, 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE; flow ends P1 1250.24, P2 1350.6, P3 1290.6, P4 col3 1140.45 (= core), P5 1249.75, P6 1096.5, P7 col3 1673.0, P8 941.1
- occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff [137,138,139]); freeze fragments 0 unexplained; freeze baseline direct sha256 8/8
- strict-CJK added = 8 × U+3000 only; print/web multiset identical (8,028 words); web < 7 MB; P8 min font 13.0 px = 9.75 pt
- §1.1 scans pass; VOL.5 = 3 legitimate nodes (same as core); textmd validate 0/0; keys match (except 137–139 + writing); notes match translations.py (table_gaps empty)
- P8 chip check: Q113–120, Q145–149, Q150 all B1, = core 1:1

## Build history — 1 build (no rebuilds)
- Pre-build shortenings (13 fr values in `translations.py`, each count-asserted 1×, applied BEFORE building — the de lesson applied pre-emptively): match_set instr "Associe chaque mot à sa définition" (314.1px) → "Associe mots et définitions" (242.7px, budget 254.5px); P4 E TU question 3 lines → 2 ("Quel match vas-tu regarder dimanche soir? Écris deux phrases en italien.", send-clause dropped); P7 disclosure 6 lines → 3 ("Exemple de la rédaction, pas une vraie lettre. Pas de vraie lettre ni de meilleure rédaction ; promesse reportée au VOL.5."); P7 error notes → 1 line each ("La Lazio est au singulier, le verbe aussi." / "Après è probabile che : subjonctif." / "Torrone est au singulier, le verbe aussi."); P1 cifre items → 2 lines each (29 → "(la Lazio mène)"; 24 → "(24 buts en 10 matches)"; 20.45 → "(20 h 45)"; plus de 150 → "(plus de 150 figurants)"); P8 notes 58 → "le plus beau dimanche soir (un jugement)", 87 → "Ce sont des données d'exercice, pas des prévisions", 44/134 → "Sujet + verbe". P1 bridge stayed 3 lines (as de, OK). P8 fr re-aimed keys measured: 137 = 2 lines, 138 = 1 line, 139 = 2 lines; est. P8 total ~4533px < 4576px capacity.
- Build1 (~272 s): run.py rc 0, 150 exercises, writing_type "Rédaction". NOTE: the build command's `tee fr/build1.log` failed with "No such file or directory" because the fr/ dir did not exist when tee started; the build's own logs exist in fr/ (build1.log, render1.log, webpdf1.log).
- Gates1: 19/20 PASS — only textmd validate failed: reverse-miss 8, REV 'Page 1 sur 8' … 'Page 8 sur 8'.
- Root cause (validator bug, NOT an edition defect): the reverse skip regex in scratch adapter `validate_edition_textmd.py` only covered footers whose preposition is in (of|di|de|von|из|/) — en "of" and de "von" pass, but fr "sur" (and nl "van", ja/ko/zh-tw forms) were never covered. The `.text.md` body export correctly omits footers (verified: en/de .text.md files also contain no "Page 8 of 8" / "Seite 8 von 8", grep count 0).
- Fix applied (scratch tool only, not a shared tool): per-language `FOOT_RE` dict added to `validate_edition_textmd.py`, keyed by the lang suffix of the slug — en `^Page \d+ of \d+$`, de `^Seite \d+ von \d+$`, fr `^Page \d+ sur \d+$`, es/pt `^Página \d+ de \d+$`, nl `^Pagina \d+ van \d+$`, ru `^Страница \d+ из \d+$`, ja `^\d+ ページ（全 \d+ ページ）$`, ko `^제 \d+ 면 / 총 \d+ 면$`, zh-tw `^第\d+版／共\d+版$`; footer nodes matching it are skipped before the generic skip. `flat()` only strips whitespace, so patterns are matched against the original node text. Also note for later: the es/pt/nl/ru/ja/ko/zh-tw footer forms now have a skip pattern too (this was missing before this fix).
- Re-run (`fr/gates2.log`): GATES ALL PASS.

## Visual — 8/8 cards viewed, zero defects
- P1: cifre box 2-line items clean; bridge 3 lines OK; masthead "JOURNAL ITALIEN VOL.4" correct; footer "Page 1 sur 8".
- P2: "Associe mots et définitions" instr fits; E TU box 2-line reader question fits ("As-tu déjà traversé un pont votif ou planté un arbre ? Écris deux phrases en italien à la rédaction.").
- P3: E TU box clean ("Tu préfères le torrone ou le chocolat ? Écris deux phrases et envoie-les-nous.").
- P4: E TU box ends flush with the table header at 1140.45 = core; match_set instr fits; results table clean.
- P5: clean (structural mid-page whitespace is the core pattern).
- P6: clean — practice bar chart + "MINIMA D'EXEMPLE" box + Q83–100.
- P7: error notes 1 line each; disclosure 3 lines ends 1673.0, clear of the FRASI hline; LA PAROLA gloss 2 lines.
- P8: Q113–120 B1 badges; 141–144 "Associe mots et définitions" fits, no graze; RISPOSTE 1–150 all present; Q137 wraps to 2 lines (fits); Q149/Q150 separate lines; "150. ✓ Texte modèle en section H ci-dessous (99 mots)".

## Self-read — full .text.md (1317 lines), all 150 keys re-verified
- French explanation layer throughout; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent).
- Spot checks: Q22 A vœu de 1630; Q29 B; Q32 A « Fate dolci »; Q44/134 note "Sujet + verbe"; Q51 B; Q58 "le plus beau dimanche soir (un jugement)"; Q59 meglio; Q66 B 23 Nov; Q81 Vero; Q82 Falso; Q85 B (13−11=2); Q86 A (6+7=13); Q87 note "Ce sont des données d'exercice, pas des prévisions"; Q92 +0.8%; Q104 B; Q108 A; Q112 B; Q120 B 24 Nov; Q137–140 re-aimed (137 "Pour la Madonna della Salute, on traverse le pont votif.", 138 "Dimanche soir, l'Atalanta joue contre l'Inter.", 139 "Samedi, la Lazio joue à domicile contre Lecce.", 140 "Ogni cifra deve essere chiara.").
- Model text 99 words frozen. Disclosure 3-line version in P7 LETTERE (fr): "Exemple de la rédaction, pas une vraie lettre. Pas de vraie lettre ni de meilleure rédaction ; promesse reportée au VOL.5."

## Quota stops on this shift: NONE. Core-it untouched.
