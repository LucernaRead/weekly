# it-es RECORD — COMPLETE (build1, 2026-11-11)

## Deliverables
- Print PDF `La-Lucerna-VOL4-ES.pdf` — 14,033,685 bytes, sha256 `9c7ee019b041a7484aed75d92c5d9f21f7e899fde8e8fa05813cc3c60b0b8d31`
- Web PDF `La-Lucerna-VOL4-ES-web.pdf` — 1,259,244 bytes, sha256 `d05e956d056c76f8bf3f6ce560073d1c341a7e1ea71ce0fa17f1e19ee3d93408`
- `2026-w47-it-es.text.md` — 56,259 bytes, 1317 lines, 150 exercises (exported from production sources)
- `ABSTRACT.txt` (Spanish, one line, no ASCII double quotes — full text in `build_edition.py` ABSTRACTS and in the edition WEEKLY-KIT.md §7)
- `WEEKLY-KIT.md` written (mirror of the en/de/fr KIT structure; es numbers §7/§8)
- 8 SVG in `svg/` + 8 cards in `cards/`

## Gates — ALL PASS (`es/gates1.log`, first run)
- run.py rc 0, 150 exercises, zero FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE; flow ends P5 col3 1249.75, P6 col3 1096.5, P7 col3 1673.0, P8-ex col 3 y=941.1, P8-keys col 3 y=2529 (bottom 2552, 23 px spare)
- occlusion 0 flags; p8 extract 150/150, compare CLEAN (keydiff [137,138,139]); freeze fragments 0 unexplained; freeze baseline direct sha256 8/8
- strict-CJK added = 8 × U+3000 only; print/web multiset identical (8,012 words); web < 7 MB; P8 min font 13.0 px = 9.75 pt
- §1.1 scans pass; VOL.5 = 3 legitimate nodes (same as core); textmd validate 0/0; keys match (except 137–139 + writing); notes match translations.py (table_gaps empty)
- P8 chip check: Q113–120, Q145–149, Q150 all B1, = core 1:1

## Build history — 1 build (no rebuilds)
- Pre-build shortenings (12 es values in `translations.py`, each count-asserted 1×, applied BEFORE building — the de/fr lesson): match_set instr "Relaciona cada palabra con su definición" (369.4px) → "Relaciona las palabras" (202.3px, budget 254.5px); P4 E TU 3 lines → 2 ("¿Qué partido verás el domingo por la noche? Escribe dos frases en italiano.", send-clause dropped); P7 disclosure 5 lines → 3 ("Ejemplo de la redacción, no una carta real. Sin cartas reales ni mejores redacciones; la promesa pasa al VOL.5."); P7 error notes 1+4 → 1 line each ("La Lazio es singular, y el verbo también." / "Torrone es singular, y el verbo también."); P1 cifre → 2 lines each (29 → "(la Lazio lidera)"; 24 → "(24 goles en 10 partidos)"; 20.45 → "(20:45)"; más de 150 → "(más de 150 figurantes)"); P8 notes 44/134 → "Sujeto + verbo", 58 → "el domingo por la noche es el mejor (una valoración)", 87 → "Son datos de práctica, no previsiones".
- P8 estimate (NEW method, done before building): mapped the fr `.text.md` RISPOSTE lines through translations.py (fr→es, longest-first) and wrapped each at sans 13 in 422.5 px: 7 two-liners (44, 58, 87, 134, 137, 138, 139), total 4607.4 px vs 4576 px capacity (−31.4 px). The 4 P8 note shortenings convert 4 two-liners → one-liners (59.3 px saved, est. ~4548 px). Build1 confirmed: P8-keys ends 2529/2552. Note the 136 note ("Sujeto + verbo + lugar") was NOT shortened — it was a 1-liner already; 44/134 share the "主语 + 动词 + 地点 + 日期" entry, 136 uses "主语 + 动词 + 地点" (different entry — verified against the fr edition's content8.py, where 134 = "Sujet + verbe" and 136 = "Sujet + verbe + lieu").
- Build1 (~272 s): run.py rc 0, 150 exercises, writing_type "Escritura". Gates1 ALL PASS on the first run — no fix round.
- Re-aimed es keys (from build_edition.py tr() of the Chinese sources): 137 "Para la Madonna della Salute, la gente cruza el puente votivo." / note "Compara con el original"; 138 "El domingo por la noche, el Atalanta juega contra el Inter." / "si gioca = se juega"; 139 "El sábado, la Lazio juega en casa contra el Lecce." / "in casa = en casa"; 140 "Cada cifra debe ser clara. → ___" / "dovere = deber".

## Visual — 8/8 cards viewed, zero defects
- P1: cifre box 2-line items clean; bridge 3 lines OK; masthead "SEMANARIO ITALIANO VOL.4" correct; footer "Página 1 de 8". OBSERVATION (not a defect): the masthead band starts at x=0.0, flush with the left page edge (en 7.4, fr 63.2, core 185.8); zoom-verified the initial "S" and final "A" are fully rendered, no glyph clipped, right edge ≈1881 < 1950. Same pattern as the accepted en edition, at the boundary. pt ("SEMANÁRIO ITALIANO") and nl ("ITALIAANS WEEKBLAD") will likely show the same; watch, do not pre-fix.
- P2: "Relaciona las palabras" instr fits; E TU box 2-line reader question fits ("¿Has cruzado alguna vez un puente votivo o plantado un árbol? Escribe dos frases en italiano a la redacción.").
- P3: E TU box clean ("¿Prefieres el turrón o el chocolate? Escribe dos frases y envíalas.").
- P4: E TU box ends flush with the table header at 1140.45 = core; match_set instr fits; results table clean.
- P5: clean (structural mid-page whitespace is the core pattern).
- P6: clean — practice bar chart + "MÍNIMAS DE EJEMPLO" box + Q83–100.
- P7: error notes 1 line each; disclosure 3 lines ends 1673.0, clear of the FRASI hline; LA PAROLA gloss 2 lines.
- P8: Q113–120 B1 badges; 141–144 "Relaciona las palabras" fits, no graze; RISPOSTE 1–150 all present; Q137/138/139 wrap to 2 lines each (fit, flow ends 2529/2552); Q149/Q150 separate lines; "150. ✓ Texto modelo en la sección H abajo (99 palabras)".

## Self-read — full .text.md (1317 lines), all 150 keys re-verified
- Spanish explanation layer throughout; only CJK is the deliberate 「翻译」 type label on Q137–140 (W46 precedent) + the frozen verb-paradigm fullwidth colon ： in notes 16–20/60–61 (core pattern, no added CJK).
- Spot checks: Q22 A voto de 1630; Q29 B; Q32 A «Fate dolci»; Q44/134 note "Sujeto + verbo"; Q51 B; Q58 "el domingo por la noche es el mejor (una valoración)"; Q59 meglio; Q66 B 23 Nov; Q81 Vero; Q82 Falso; Q85 B (13−11=2); Q86 A (6+7=13); Q87 note "Son datos de práctica, no previsiones"; Q92 +0.8%; Q104 B; Q108 A; Q112 B; Q120 B 24 Nov; Q136 note "Sujeto + verbo + lugar" (kept, 1-liner); Q137–140 re-aimed.
- Model text 99 words frozen. Disclosure 3-line version in P7 LETTERE (es): "Ejemplo de la redacción, no una carta real. Sin cartas reales ni mejores redacciones; la promesa pasa al VOL.5."

## Quota stops on this shift: NONE. Core-it untouched.
