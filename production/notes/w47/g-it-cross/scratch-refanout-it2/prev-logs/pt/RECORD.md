# it-pt RECORD — COMPLETE (build1, 2026-11-11)

## Deliverables
- Print PDF `La-Lucerna-VOL4-PT.pdf` — 14,036,807 bytes, sha256 `4492665b04a7a631c9e8ace2cd15cfe077dbd3607f78b6aab228e05470629882`
- Web PDF `La-Lucerna-VOL4-PT-web.pdf` — 1,262,226 bytes, sha256 `164492f8ab7b69f166b47778f856ae9d16cb29ed43dc2458208cc804f41e93c1`
- `2026-w47-it-pt.text.md` — 55,820 bytes, 1317 lines, 150 exercises (exported from production sources)
- `ABSTRACT.txt` (Portuguese, one line, no ASCII double quotes — full text in `build_edition.py` ABSTRACTS and in the edition WEEKLY-KIT.md §7)
- `WEEKLY-KIT.md` written (mirror of the en/de/fr/es KIT structure; pt numbers §7/§8)
- 8 SVG in `svg/` + 8 cards in `cards/`

## Gates — ALL PASS (`pt/gates1.log`, first run)
- run.py rc 0, 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE; flow ends P7 col3 1673.0, P8-ex col 3 y=941.1, P8-keys col 3 y=2529 (bottom 2552, 23 px spare)
- occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff [137,138,139]); freeze fragments 0 unexplained; freeze baseline direct sha256 8/8
- strict-CJK added = 8 × U+3000 only; print/web multiset identical (7,981 words); web < 7 MB; P8 min font 13.0 px = 9.75 pt
- §1.1 scans pass; VOL.5 = 3 legitimate nodes (same as core); textmd validate 0/0; keys match (except 137–139 + writing); notes match translations.py (table_gaps empty)
- P8 chip check: Q113–120, Q145–149, Q150 all B1, = core 1:1

## Build history — 1 build (no rebuilds)
- Pre-build shortenings (13 pt values in `translations.py`, each count-asserted 1×, applied BEFORE building — the de/fr/es lesson): match_set instr "Relaciona cada palavra com a sua definição" (393.6px) → "Relaciona as palavras" (194.9px, budget 254.5px); P4 E TU 3 lines → 2 ("Que jogo vais ver no domingo à noite? Escreve duas frases em italiano.", send-clause dropped); P7 disclosure 5 lines → 3 ("Exemplo da redação, não uma carta real. Sem cartas reais nem melhores redações; a promessa passa ao VOL.5." — "passa ao" not "passa para o"; both "passa para o" candidates measured 4 lines); P7 error notes 1+2+4 → 1 line each ("A Lazio é singular, e o verbo também." / "Depois de è probabile che: subjuntivo." / "Torrone é singular, e o verbo também."); P1 cifre → 2 lines each (29 → "(a Lazio lidera)"; 24 → "(24 golos em 10 jogos)"; 20.45 → "(20:45)"; mais de 150 → "(mais de 150 figurantes)"); P8 notes 44/134 → "Sujeito + verbo", 58 → "o domingo à noite é o melhor (uma opinião)", 87 → "São dados de prática, não previsões".
- P8 estimate (es method): 7 two-liners (44, 58, 87, 134, 137, 138, 139), total 4607.4 px vs 4576 px capacity (−31.4 px). The shortenings were expected to convert 3 (44, 58, 87) since 134 measured 2 lines by wrap() — "Sujeito" is one letter longer than es "Sujeto". Build1 outcome: P8-keys ends 2529/2552 — the same as es — and the shipped P8 card shows 134 on ONE line. Lesson: the estimator is conservative by ~10 px (Flow.para wraps slightly tighter than a direct wrap() call at the same width); trust the build log's flow end when estimate and build disagree by < 15 px.
- One edit-script slip, caught by the count assertion before any write: the Torrone error-note pt value is "Torrone é singular, …" (no leading "O ") — the first script asserted count 0 and wrote nothing; corrected ("Torrone é singular, por isso o verbo vai no singular." → "Torrone é singular, e o verbo também.") and re-ran cleanly. The file was never partially edited.
- Build1 (~270 s): run.py rc 0, 150 exercises, writing_type "Escrita". Gates1 ALL PASS on the first run — no fix round.
- Re-aimed pt keys (from build_edition.py tr() of the Chinese sources): 137 "Para a Madonna della Salute, as pessoas atravessam a ponte votiva." / note "Compara com o original"; 138 "No domingo à noite, a Atalanta joga contra o Inter." / "si gioca = joga-se"; 139 "No sábado, a Lazio joga em casa contra o Lecce." / "in casa = em casa"; 140 "Cada número deve ser claro. → ___" / "dovere = dever".

## Visual — 8/8 cards viewed, zero defects
- P1: cifre box 2-line items clean; bridge 3 lines OK; masthead "SEMANÁRIO ITALIANO VOL.4" correct; footer "Página 1 de 8". OBSERVATION (not a defect): masthead band starts at x=0.0, flush with the left page edge (same as es); initial "S" and final "A" fully rendered, no glyph clipped, right edge ≈1881 < 1950.
- P2: "Relaciona as palavras" instr fits; E TU box 2-line reader question fits ("Já atravessaste uma ponte votiva ou plantaste uma árvore? Escreve duas frases em italiano para a redação.").
- P3: E TU box clean ("Preferes torrone ou chocolate? Escreve duas frases e envia-as.").
- P4: E TU box ends flush with the table header at 1140.45 = core; match_set instr fits; results table clean.
- P5: clean (structural mid-page whitespace is the core pattern).
- P6: clean — practice bar chart + "MÍNIMAS DE EXEMPLO" box + Q83–100.
- P7: error notes 1 line each; disclosure 3 lines ends 1673.0, clear of the FRASI hline; LA PAROLA gloss 2 lines.
- P8: Q113–120 B1 badges; 141–144 "Relaciona as palavras" fits, no graze; RISPOSTE 1–150 all present; Q137/138/139 wrap to 2 lines each (fit, flow ends 2529/2552); Q134 on ONE line (see estimator lesson above); Q149/Q150 separate lines; "150. ✓ Texto modelo na secção H abaixo (99 palavras)".

## Self-read — full .text.md (1317 lines), all 150 keys re-verified
- Portuguese explanation layer throughout; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK).
- Spot checks: Q22 A voto de 1630; Q29 B; Q32 A «Fate dolci»; Q44/134 note "Sujeito + verbo"; Q51 B; Q58 "o domingo à noite é o melhor (uma opinião)"; Q59 meglio; Q66 B 23 Nov; Q81 Vero; Q82 Falso; Q85 B (13−11=2); Q86 A (6+7=13); Q87 note "São dados de prática, não previsões"; Q92 +0.8%; Q104 B; Q108 A; Q112 B; Q120 B 24 Nov; Q136 note "Sujeito + verbo + lugar" (kept, 1-liner); Q137–140 re-aimed.
- Model text 99 words frozen. Disclosure 3-line version in P7 LETTERE (pt): "Exemplo da redação, não uma carta real. Sem cartas reais nem melhores redações; a promessa passa ao VOL.5."

## Quota stops on this shift: NONE. Core-it untouched.

---

## Re-fan-out (2026-11-11)
- Rebuilt from core-it fix3 (36bdec2e) by build_edition.py, RC=0 first attempt; text.md 55,739 bytes, 1317 lines, 150 exercises.
- Gates: 20/20 PASS, 0 FAIL (`scratch-refanout-it/gates-pt.log`); P8-keys flow ends y=2529 (bottom 2552); freeze baseline re-taken 8/8 (this dir's baseline is the re-fan-out one; first-fan-out baseline preserved in `scratch-refanout-it/prev-fanout/pt/`).
- fix3 9 lines + E labels + table values verified by `scratch-refanout-it/check_refanout.py` (ALL PASS); sim cross-check 0 unexpected changes.
- KIT updated with the new SHAs + §11 (see the edition dir). Full report: `scratch-refanout-it/FANOUT-REPORT-it.md`.
