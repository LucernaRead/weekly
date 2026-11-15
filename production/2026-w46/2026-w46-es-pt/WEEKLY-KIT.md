# WEEKLY-KIT · 2026-w46-es-pt — La Lucerna, Spanish Weekly VOL.3, explanations in Brazilian Portuguese

Slug: `2026-w46-es-pt`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Brazilian Portuguese, written natively.
Build dir: `hidden_files/weekly-report-w46-es-pt-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_pt.py` + `t_pt2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-es-pt.pdf` 3,482,901 B; web PDF `2026-w46-es-pt.web.pdf` 412,608 B (<7 MB), text layer 46,471 B via `pdftotext`, byte-identical to the print PDF's text.
`.text.md` exported from this edition's own SVG text layer (never from PDF).

## 2. Furniture (W43 ES×PT precedent, VOL.1→VOL.3 only)

- Badge replaces the y=372 subtitle slot, 19.5pt: `TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`.
- Edition line: `SEMANÁRIO ESPANHOL · VOL.3 · LA HUELGA · LA CAMPAÑA · LA ROJA`.
- Top strip: `SEMANAL EN ESPAÑOL · O ESPANHOL QUE A ESPANHA LÊ` — see deviation F1b in §5 (the W43/W45 three-segment form collides with the longer W46 date line; the middle segment was dropped, 148px clear by venv measurement).
- Band right: `A CAMPANHA COMEÇA SEXTA, 13 · GREVE NA QUARTA, 11` / `A manchete desta edição · ver páginas 2 e 6`.
- Footer: `La Lucerna · SEMANÁRIO ESPANHOL VOL.3 · TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS` / `Página N de 8`.
- Gloss prefix `Nota — `; `bridge()` kept.
- Bands (target · PT): VIDA · VIDA COTIDIANA / CULTURA · CULTURA / DEPORTE · ESPORTE / JUVENTUD · JUVENTUDE / A FONDO · EM PROFUNDIDADE / LENGUA · LÍNGUA / EJERCICIOS Y RESPUESTAS · EXERCÍCIOS E RESPOSTAS. Band subtitles PT part in caps (W43 pattern).
- Exercise headers `EJERCICIOS · EXERCÍCIOS DA PÁGINA N`; right note `Respostas na página 8 · Os exercícios podem misturar os níveis: procure pelo número`.
- Instruction chips: Complete / Verdadeiro ou falso / Forme a frase / Reescreva / Traduza / Escreva / Associe.
- P1 furniture: `LA NOTICIA · A notícia` · `AHORA TÚ · Agora você` · `Os cinco temas · Para entender la semana` · `Nada inventado: tudo explicado aqui.` · `EN ESTA EDICIÓN · Nesta edição` · `BREVES · Em resumo` · `QUIZ RELÁMPAGO · Quiz-relâmpago` · quiz right text `Leia a capa, escolha a resposta certa · Respostas na página 8`.
- P8 header: `RESPUESTAS · Respostas — por página, procure pelo número`; right text `Cada resposta traz uma breve nota · ✓ marca a questão de redação`; separator `— PÁGINA {n} —` (core's all-caps form, as shipped in W43 — W45 R1).
- Type names translated (Completar frases / Escolha múltipla / Escolha no texto / Verdadeiro ou falso / Formar frases / Reescrever frases / Associar palavras / Tradução / Escrita); P8 check `== "Escrita"`.
- Box-title sizes (W45 F2): `LA SEMANA EN CIFRAS · Em números` tsize=20, `EL CALENDARIO · O calendário da semana` tsize=19, `EL PLAN DE LA SEMANA · O plano` tsize=20 (shortened — see §5), `ERRORES TÍPICOS · Erros comuns` 20pt, `LA PALABRA · A palavra da semana` 22pt.
- Paren-spacing rule F3 (W43 D7): a space precedes each parenthesis gloss in the CIFRAS, calendar and plan boxes. P1 word note kept to one line.

## 3. Registry verification & key-diff adjudication

`p8.py compare` vs core P8: CLEAN, 150/150, keydiff=[137, 138] — the two translation keys re-aimed to Portuguese source sentences; bodies 139/140 re-aimed to Portuguese; all other keys byte-identical. `freeze.py diff` vs core SVGs: added CJK 0 on every page; edition CJK 0.

## 4. Gates (final render)

- Builder self-check: 0 FLOW OVERFLOW / 0 HEAD TOO WIDE; 150 exercises; `p8.py extract` 150/150.
- `tools/occlusion_audit.py`: 0 flags (`hidden_files/w46/es-pt-occlusion.json`, selftest passed).
- Same-baseline furniture scan + chart GRAZE element-check (`hidden_files/w46/checks.py`): 7 rowcheck reports, all P1 contents-list 4.0px gaps — the core pattern, no overlap; chart 0 overlaps.
- Web PDF text layer: 46,859 B, identical to print text; <7 MB.
- Visual: P1, P5, P7 cards inspected — badge, top strip clear of the date line (after F1b), plan box title inside its box, letters box with disclosure inside, preview band clear of the footer rule.

## 5. Fixups (Portuguese apparatus only; core geometry and Spanish text untouched)

1. First build: P8 answer flow overflow (items 146–150 overprinting, 10 TEXTX flags) + P5 plan box title crossing its box border (ink > 961). Fixed: P8 answers 13.2pt/1.12 (EN/FR/IT/NL precedent — a deviation from W45 PT's shorten-notes approach, same geometry, noted here); plan title shortened to `EL PLAN DE LA SEMANA · O plano` at tsize=20 (measured 333.3px ≤ 394px slot; the fuller `O plano da semana` measures 444.4px at 20pt and 422.1px at 19pt — both over).
2. F1b — top strip: the W43/W45 three-segment strip (`SEMANAL EN ESPAÑOL · UM NÚMERO POR SEMANA · O ESPANHOL QUE A ESPANHA LÊ`) ends at x=1406.3 by venv measurement while the W46 date line (`SEMANA DEL 9 AL 15 DE NOVIEMBRE DE 2026`) starts at x=1408.9 — a 2.6px nominal gap that renders as a visible `LÊSEMANA` collision (the canonical audit does not flag header-zone text/text grazes; caught visually). Fixed by dropping the middle segment; the two-segment strip ends at x=1261.2, 148px clear. Rebuilt and re-gated: 0 flags, P1 visually clean.
3. Core letters-box fix inherited via rebuild from the fixed core build (disclosure inside its box).

## 6. Promises, sources, credits

As in the core: 13 Nov campaign start and 29 Nov vote lead the issue; the unverified 12 Nov decree date was NOT reintroduced; reader letters: labelled editor's example (Ana) + bilingual disclosure, promise carried to VOL.4, no reader fabricated. Sources, image credits and the full article record: see the core KIT `files/weekly-report-w46-es-core/WEEKLY-KIT.md`.

## 7. Reproduction

`python3 hidden_files/w46/build_one.py pt t_pt` (copies the fixed core build, applies `t_pt.py` + `t_pt2.py`, runs `run.py`, renders via `tools/venv`, gates freeze/p8/occlusion). Gate outputs: `hidden_files/w46/es-pt-diff.json`, `es-pt-p8-compare.json`, `es-pt-occlusion.json`, `es-pt-build.log`; gate record in `hidden_files/w46/es-gates.log`. Independent proofread (§8.4 SOP) still outstanding — do not claim finalisation.

## D5 rebuild (2026-11-15)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib <patched> --target es --reader pt --week 2026-w46` (`--check` dry-run clean first). Mode latin; `_D5_READER = "pt"`. Routing test `test_d5_routing.py` FAILURES: 0. fix2 retained (`_QUOTE_CLS` x4).
- Pre-fix census (baseline build): D5 Latin-in-CJK 495, D5 Cyrillic-in-CJK 0, curly-in-CJK 0, curly total 0 (all Newsreader). Run2 census: Latin 0 / Cyrillic 0 / curly-in-CJK 0; curly total 0 all Newsreader; Noto Sans 0.
- run1 gates 16/19; run1 -> run2 fixes (font-size reduction only, no copy changes):
- run1 G6 TEXTX: P1 band headline overlapped the translation line by 127.3x26.8px; fixed by the band size above.
- `content12.py:26` — band headline 46 -> 39.5 (gap +12.7px)
- `content12.py:177` — P2 calendar tsize 19 -> 18.5 (margin 6.2px)
- run2 gates 19/19 ALL-GREEN. G8 CLEAN (core-es P8 compare; keydiff [137, 138]). G10 CJK added 1 (P6 U+3000 run-split, as W45 es); Latin added 266 (run-split). G12 22 titles, 272 body lines, 0 DEFECT, 0 OBSERVE, 0 marginal. G14 0 defects; P8 241 rows, slack 43.7px. G15a text-layer diff 0; text.md DIFF 140 lines, native verifier ADOPT (REWRAP 36, 0 UNEXPECTED). G15b checker has no pt table (record-only, D27); native verifier ADOPT covers text.md.
- D18 gap 129.4px; D37 N/A (no badge line in the box zone; strapline y=372 above box top 588); D39(4) P7 band bottom vs footer 2596: -83.9px.
- Old (baseline build) print `La-Lucerna-VOL3-es-pt.pdf` 4,067,542 B SHA256 `368677cc065080d7bd554ae511735f96dea1b9e24bfd55dfb5005bc9a62ac7a1`; web 490,608 B SHA256 `0d4b871e951b00855bf32168de55138bf0a423600a0075880cd314d7916294e3`.
- New (run2) print `La-Lucerna-VOL3-es-pt.pdf` 3,482,901 B SHA256 `9a34021a83f146c225d11222780e143a11ed46eaf24297aa425c18c3cf09807b`; web `2026-w46-es-pt.web.pdf` 412,608 B SHA256 `4542a936df21b2c6d5482d2573be35b6c24b5c27639e430a2071661a6a3d695c`; text.md 46,614 B SHA256 `7f7ebaee53638be9b2e8a37d12ad48570f1bdf4353e4eb2bdf2e40c68d3f2f45` (textexp output, `logs/2026-w46-es-pt/2026-w46-es-pt.text.md.run2`; the `<slug>.text.md` in the edition dir is the stale 2026-11-06 fanout artifact — do NOT sync it).
- Logs: `logs/2026-w46-es-pt/GATES-SUMMARY.txt` (run2), `logs/2026-w46-es-pt/g*-run2.log`, `logs/2026-w46-es-pt/census-run2.json`, `logs/2026-w46-es-pt/freeze-diff-run2.json`. D5 report: `notes/g-es/scratch-d5-rebuild-es/2026-w46-es-pt-D5-REPORT.md`.
