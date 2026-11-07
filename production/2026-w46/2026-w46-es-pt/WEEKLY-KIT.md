# WEEKLY-KIT · 2026-w46-es-pt — La Lucerna, Spanish Weekly VOL.3, explanations in Brazilian Portuguese

Slug: `2026-w46-es-pt`. Issue week: Mon 9 – Sun 15 Nov 2026. Frontmatter week: `2026-W46`.
Target language: Spanish (all article text frozen from the W46 core). Explanation layer: Brazilian Portuguese, written natively.
Build dir: `hidden_files/weekly-report-w46-es-pt-build/` (copy of the W46 core build; transform tables `hidden_files/w46/t_pt.py` + `t_pt2.py`, applied by `hidden_files/w46/build_one.py`).

## 1. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
8 pages, 1950×2700. Final build log: zero FLOW OVERFLOW / zero HEAD TOO WIDE.
Print PDF `La-Lucerna-VOL3-PT.pdf` 4,638,608 B; web PDF `La-Lucerna-VOL3-PT-web.pdf` 520,642 B (<7 MB), text layer 46,836 B via `pdftotext`, byte-identical to the print PDF's text.
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
