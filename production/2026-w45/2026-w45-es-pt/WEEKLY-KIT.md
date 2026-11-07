# La Lucerna · SEMANÁRIO ESPANHOL VOL.2 — ES × PT (W45)

**Pairing:** Spanish target text (frozen W45 ES core) · ALL explanations in Portuguese (Brazilian) for Portuguese-speaking readers.
**Issue week:** Mon 2 – Sun 8 Nov 2026 · **Core:** `files/weekly-report-w45-es-core/` (8 SVG + KIT, shipped) · **Pages:** 8 (1950×2700)
**Build dir:** `hidden_files/weekly-report-w45-es-pt-build/` (core build copied, never edited in place)
**Transform record (asserted literal replacements, every pair count-checked):** `hidden_files/w45-es-pt-transform.py` (Parts 1–7)
**Status: BUILDER-COMPLETE — NOT finalized, NOT delivered anywhere. Awaits independent proofread (SOP §8.4).**
No Discord post, no card/PDF into main chat, no cron, no weekly-git touch — delivery is the parent line's job.

## 1. Baseline proof (frozen core reproduced before any edit)

`tools/freeze.py baseline` on the build copy before editing: **8/8 SVGs byte-identical** to the shipped core SVGs, zero warnings in the baseline run. Core shipped SVG hashes (identical before and after this build — re-verified at the end):

| page | sha256 |
|---|---|
| p1-portada | a1b3010296ad129e45d2816637762cec4f25635ff43ea2197e08e0efd0daf34d |
| p2-vida | 10e78c2e6cb295198cce99ed6182cf2472511da267ddeb9bf4379d464f0bb724 |
| p3-cultura | 5986ba9e318c985e14d33abb6e9277f22bf7c0c6a961f94501cdfa46b655aa8b |
| p4-deporte | 1894836e06be824b1dc3a3ac46474ccced7495679f23aabc0f27808c63617a67 |
| p5-juventud | cd15c68b5f8db752b6bc62346dd22826d19513d41fab16f2a2f7c119a3893fd2 |
| p6-afondo | fcfccf8267e10cc7ddbf14d5aa9dd735cf1c73a110f4fe8ec38d8e9aef07b280 |
| p7-lengua | b1774024b6a17353d18a7b9b13f4be14ce8a6a4ca1b8f2565e06fafb0a90a8fe |
| p8-ejercicios | d1c46fa439ac505db6e2708df8206f10d7046947064172dfcde22e74d7545147 |

**Freeze check (code level):** all edits are asserted literal replacements in the transform script (README #17: whole lines / exact unique literals, never AST byte offsets; README #18: value maps use bare text, never repr literals — the one f-string-adjacent case, the P8 type check, is a plain `== "Escrita"` token swap). No Spanish target text, geometry, or exercise structure changed outside the registries below. The core build directory was never imported into (README #11); all content modules ran only inside the copy through the single ONE-driver process `run.py` (README #7). The W43 ES×PT directory and its build directory were read-only references, never written.

## 2. Totals (identical to core)

150 exercises — A2 50 · B1 72 · B2 28. By page: 10/18/18/18/18/18/12/38.
Final build log: **zero FLOW OVERFLOW / zero HEAD TOO WIDE** (see §8 for the first-build overflows and their fix-ups).
8 pages, 1950×2700; 8 full-page PNGs at 1950×2700.
Margin note (not a warning): P5 exercise flow ends at y=2577 against bottom 2580 (3px margin, deterministic — same on every re-render).

## 3. PT furniture as finally shipped (verbatim from W43 ES×PT, VOL.1→VOL.2 only)

- **Masthead:** `La Lucerna` (exactly as the core ships)
- **Title line:** `SEMANÁRIO ESPANHOL · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL` (measured 1715.5px < 1820px page width)
- **P1 badge** (19.5pt sans bold, brick slot, y=372 — README #20 ES-family case, identical to W43 shipped): `TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`
- **Top strip:** `SEMANAL EN ESPAÑOL · UM NÚMERO POR SEMANA · O ESPANHOL QUE A ESPANHA LÊ` — see deviation F1.
- **Footer (every page):** `La Lucerna · SEMANÁRIO ESPANHOL VOL.2 · TEXTOS EM ESPANHOL · EXPLICAÇÕES EM PORTUGUÊS` / `Página N de 8`
- **Gloss prefix:** `Nota — `
- **Bands (target · PT):** VIDA · VIDA COTIDIANA / CULTURA · CULTURA / DEPORTE · ESPORTE / JUVENTUD · JUVENTUDE / A FONDO · EM PROFUNDIDADE / LENGUA · LÍNGUA / EJERCICIOS Y RESPUESTAS · EXERCÍCIOS E RESPOSTAS
- **Band subtitles (PT part in caps, W43 pattern):** A PONTE DE SEGUNDA, 2 DE NOVEMBRO / A SEMANA PASSADA: TRÊS NOITES DE OUTONO / A EUROPA PRIMEIRO, DOMINGO ÀS 21:00 / A NFL EM MADRID / A HABITAÇÃO DECIDE A CAMPANHA / FOCO NA LÍNGUA · Tres niveles, tres herramientas · TRÊS NÍVEIS, TRÊS FERRAMENTAS / PÁGINA 8 · La gran prueba de la semana + todas las respuestas
- **Exercise headers:** `EJERCICIOS · EXERCÍCIOS DA PÁGINA N`; right text: `Respostas na página 8 · Os exercícios podem misturar os níveis: procure pelo número`
- **Instruction chips:** Complete / Verdadeiro ou falso / Forme a frase / Reescreva / Traduza / Escreva / Associe
- **P1 furniture:** `LA NOTICIA · A notícia` · `AHORA TÚ · Agora você` · `Os cinco temas · Para entender la semana` · `Nada inventado: tudo explicado aqui.` · `EN ESTA EDICIÓN · Nesta edição` · `BREVES · Em resumo` · `QUIZ RELÁMPAGO · Quiz-relâmpago` · quiz right text `Leia a capa, escolha a resposta certa · Respostas na página 8` (W43 verbatim except the LA NOTICIA slot — see R5; coordinator KIT-only correction 2026-10-27)
- **P8 header:** `RESPUESTAS · Respostas — por página, procure pelo número`; right text `Cada resposta traz uma breve nota · ✓ marca a questão de redação`; separator `— PÁGINA {n} —` (core's all-caps form, as shipped in W43 — see discrepancy R1)
- **Answer-key format:** dash style `{n}. {key} — {note}`, half-width parens only — identical style to the core and all shipped ES fan-outs.
- **Type names** (registry metadata, never rendered; W45-sibling convention — see discrepancy R2): Completar frases / Escolha múltipla / Escolha no texto / Verdadeiro ou falso / Formar frases / Reescrever frases / Associar palavras / Tradução / Escrita; P8 type check updated to `== "Escrita"`.

### Furniture deviations / measured fixes (wording/size only — frozen geometry untouched)

- **F1 — top strip first segment (W43 KIT D1 carry-over, re-measured for W45):** the `CADA SEMANA EN ESPAÑOL` form with the PT segments measures ink end x=1429.5 against the W45 date line ink start x=1420.7 — a real 8.8px collision. Shipped with W43's proven `SEMANAL EN ESPAÑOL` form (ink ends x=1406.3, 14.4px clear of the date). Verified on the rendered P1 card.
- **F2 — box titles at reduced size** (ink measured with the build's real font metrics against the 416px title slot):
  - `LA SEMANA EN CIFRAS · Em números` tsize=20 (23pt measures 425.9px — over; W43 D3 precedent).
  - `EL CALENDARIO · O calendário da semana` tsize=19 (20pt still measures 420.6px — over by 4.6px; 19pt fits, wording kept whole).
  - `EL PLAN DEL PUENTE · O plano da ponte` tsize=20 (23pt measures 466.5px — over).
  - `ERRORES TÍPICOS · Erros comuns` 20pt and `LA PALABRA · A palavra da semana` 22pt (W43 D3 verbatim; both also fit at core sizes, W43 sizes kept).
- **F3 — paren spacing (W43 D7):** a space precedes each parenthesis gloss in the P1 CIFRAS box (3×), the P2 calendar box (7×) and the P5 PLAN box (5×).
- **F4 — P1 word note kept to one line:** `«Pré-campanha»: semanas antes da campanha.` (419.9px < 434px), clear of the y=1844 rule — same discipline as W43 D5.

### Recorded discrepancies for the coordinator (W43 shipped vs generic references)

- **R1 — P8 separator:** tables.json's generic PT `p8_separator` reads `— Página {n} —`, but W43 ES×PT shipped the core's all-caps `— PÁGINA {pg} —`. This edition keeps the shipped form per the tasking rule (W43 shipped wins).
- **R2 — type names:** W43 ES×PT kept registry type names identical to the core (metadata, never rendered); the W45 ES×EN/FR/IT siblings translate them. This edition follows the W45 siblings (PT names above). No rendered difference either way.
- **R3 — `bridge` method name:** kept as `bridge()` (all W45 ES siblings do the same). W43's `expl()` rename was W43-specific hygiene; the method name never renders.
- **R4 — tables.json furniture vol:** the PT column records VOL.1 (W43); this edition renders VOL.2 by the VOL.1→VOL.2-only rule.
- **R5 — LA NOTICIA slot + P8 right text (coordinator KIT-only correction 2026-10-27):** W43 ES×PT shipped `LA NOTICIA · A manchete`; this edition ships `LA NOTICIA · A notícia` (same P1 kicker line renders `A manchete desta edição`). `A notícia` is a legitimate translation variant, not a mistranslation — the slot varies by pair (W45 ES×IT ships `LA NOTIZIA`) and is not on the verbatim-furniture list, so the paper stands as-is; only this KIT's "all W43 verbatim" claim was false and is corrected here. Likewise the P8 exercise-header right text is a translation of the W45 core's Chinese wording (core-driven), not of W43's Portuguese right text — a core-driven difference, not a furniture deviation.

## 4. Key-diff registry (complete — derived from a full registry diff vs the core)

Only translation-type items legitimately re-aim at Portuguese. **Keys changed (3):**

| # | core key | ES×PT key | note (PT) |
|---|---|---|---|
| 137 | 周一在九个自治区是假日。 (P1 Spanish sentence, ES→native direction) | `Na segunda-feira é feriado em nove comunidades.` | Confira no original |
| 138 | 周日我们看 NFL 和马竞–巴萨。 | `No domingo vemos a NFL e o Atlético–Barça.` | Confira no original |
| 150 | （开放题，范文如下） (apparatus) | `Questão aberta — texto-modelo abaixo, nesta página` | Texto-modelo na seção H desta página (84 palavras) |

**Stems re-aimed at Portuguese (2; Spanish keys byte-identical):**

| # | stem in this edition |
|---|---|
| 139 | `O Bernabéu recebe um jogo da NFL. → ___` (key stays: El Bernabéu acoge un partido de la NFL.) |
| 140 | `Cada gráfico tem de indicar a sua fonte. → ___` (key stays: Cada gráfico tiene que llevar su fuente; W43 wording verbatim) |

All other 147 keys byte-identical to the core — proven by an independent dash-parse below, NOT by trusting the tool's keydiff list.

### Tool keydiff adjudication (README #13: suspect the tool first)

`tools/p8.py compare` reports CLEAN 150=150 with keydiff [34, 57, 83, 85, 93, 94, 95, 96, 98, 101, 107, 109, 110, 111, 117, 137, 138, 148]. Of these 18:
- **16 are extraction artifacts of `detect_note`'s paren branch** (34, 57, 83, 85, 93, 94, 95, 96, 98, 101, 107, 109, 110, 111, 117, 148): every one of these segments ends with a parenthesised note-gloss in PT (e.g. `flores — levar flores aos falecidos (flores)`), so the tool returns paren-style key = everything before the paren group — swallowing note text into the "key" — while the core's corresponding segment took the dash branch (no trailing paren group, or a full-width paren group positioned differently). Independent dash-parse (split each printed segment on the FIRST ` — `; `✓` form for #150) shows the true keys byte-identical for all 16 (flores / muchísimos / A / C / tenga / sea / para que / Aunque / muestra / 2 / mejor / baje / sea / es / A / A).
- **2 are true redirections** (137, 138 — §4 table above, W43 ES×PT KIT §3 precedents).
- **#150 is not in keydiff** (both editions render `150. ✓ {note}`; the marker is identical; only the pointer note differs per the §4 precedent).

**Independent dash-parse result: exactly 2 key diffs (137, 138). 139/140 reverse keys byte-identical. 150 marker identical. Model text (MODELO) word count measured: 84 words** (matches the printed `84 palavras` note and the core's 84-word count; the Spanish model text itself is byte-identical to the core).

## 5. Frozen-text diff (tools/freeze.py diff, --strict-cjk)

| page | added strings | removed strings | added CJK chars |
|---|---|---|---|
| P1 | 26 | 25 | 0 |
| P2 | 49 | 43 | 0 |
| P3 | 33 | 30 | 0 |
| P4 | 30 | 27 | 0 |
| P5 | 47 | 40 | 0 |
| P6 | 17 | 17 | 0 |
| P7 | 43 | 42 | 0 |
| P8 | 163 | 160 | 0 |

**Added CJK = 0 on all 8 pages; edition CJK = 0 on all pages except P7 = 2** — those 2 are the full-width parentheses `（` `）` inside the FROZEN Spanish readers'-letter attribution (`Ana （ejemplo, escrito por la redacción）`), byte-identical to the core (same adjudication as the W43 ES×PT proofread: frozen target text, not the key format). Added CJK = 0, so the strict gate holds.

**Spanish-removal audit (every removed string without CJK — 6 items, each classified):**
- P1 `EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA` → furniture: the y=372 subtitle slot replaced in place by the PT badge (W43 precedent).
- P5 `la NFL.` → re-wrap fragment: the P5 exercise stem's translated parenthetical (`(原形 acoger)` → `(infinitivo: acoger)`, EN/FR/IT precedent) re-wrapped the stem; counterpart added fragment `partido de la NFL.` confirmed.
- P6 `indecisos · margen de error` → re-wrap fragment: the P6 D-bridge word list re-wrapped; counterpart added fragment `muestra · indecisos · margen de error` confirmed.
- P7 `mejor。` → re-wrap fragment: the P7 B1-bridge tail re-wrapped; counterpart added fragment `más mejor.` confirmed.
- P8 `1. programas — las listas ya están presentadas; ahora se escriben` + `los programas` → the two wrapped lines of answer #1, whose Spanish explanation note was translated to PT (explanation layer, EN/FR precedent).
All other removed strings contain Chinese (explanation layer) or are mixed explanation strings whose Spanish headwords/keys survive verbatim in the PT strings (gloss headwords, box-title Spanish parts, band Spanish parts, calendar/CIFRAS/PLAN Spanish sentences, match-set heads, the P6 D-bridge word list). Frozen-sentence presence spot-checks pass on all 8 pages (headlines, article leads, P7 quotes, letter body, model text).

## 6. Geometric occlusion audit (mandatory gate)

Tool: `tools/occlusion_audit.py` (true-ink, PIL/FreeType). Selftest passed first (all 6 planted classes fired exactly once; clean controls silent).
- **This edition: 0 flags. Core: 0 flags. NEW flags vs core: 0.**
- **Same-baseline ink scan** (FR×RU `rowcheck.py` method, adapted as `hidden_files/w45-es-pt-rowcheck.py`): core 7 reports, edition 7 reports — the identical 7 P1 contents-list rows (`Pág. n` + title, 4.0px gaps, no overlap). No new same-row collision; P1 top band, masthead and footer rows silent in both.
- **Chart-page element check** (README #12 graze class, P6): all 34 chart elements (labels, bars, values, captions) **byte-identical to the core** — text ink vs later-drawn rects shows nothing new.
- **Known frozen defect (NOT this edition's problem, per task gate 5 + coordinator adjudication 2026-10-27):** P6 second-chart label `Inmigración` (x=1011, y=1717, 21pt bold; ink right 1144.2) vs the following bar rect (left edge 1139) — a ~5px tail graze, geometry verified identical to the shipped ES core (same text/rect indices, coordinates, fill). Kept as-is; not repaired (repair would require re-shipping the core and rebuilding all ES fan-outs); not listed as a defect of this edition. Any future proof must report presence only, to confirm identity.

## 7. Content verification (builder-run; independent proofread pending)

- **Gloss counts** (split on `·` itself, README #21): P2 5 = 5, P3 5 = 5, P4 5 = 5, P5 4 = 4 vs the core, item by item; every headword present in the rendered SVG text.
- **Images (payload MD5-identical to the core per page):** P3 `castanas.jpg` (Wikimedia Commons, CC0 — W43 asset reuse per the core KIT) and P5 `kuerbis.jpg` (USDA public domain — W43 asset reuse); printed credits byte-identical to the core. P1 carries the core's program-drawn house illustration (`illus_houses()`), not a photo — same as the core.
- **P7 phrases:** all 8 `FRASES DE LA SEMANA` quotes are verbatim contiguous excerpts of this issue's articles, each occurring **exactly 2×** in the full issue (article + P7), with PT translations underneath and page tags (Página 1, 2, 3, 4, 5, 6, 6, 1).
- **Readers' corner (gate 7):** the core FIX1 disclosure is carried over (Spanish `ld` frozen; PT `ldcn` translated) with all three facts intact — no real readers' letters had arrived by press time, no best page-8 texts had arrived, the labelled editors' example is printed and the promise carries to VOL.3 (the invitation `Escreva-nos!` was dropped for line parity, per the W45 ES×EN §3.7 precedent — all three facts kept). The Ana example letter (body, name, Shanghái, full-width-paren attribution) is byte-identical to the core. No readers, letters or quotations invented.
- **Visual check:** P1 and P7 cards read end-to-end (masthead/badge/strip/band, CIFRAS box, claves box, contents, word note clear of the y=1844 rule, illustration, breves, quiz, footer; P7 grammar columns, errs/palabra/cartas boxes, frases, preview box clear of the footer). No anomalies.

## 8. Build iterations (what the first build caught, and the fix-ups)

- **First build:** 150 exercises, correct levels/pages, but 3 P6-exercise-flow overflows, 10 P8-answer-flow overflows, and P7 col3 ending at 1962.6 — which would have pushed the preview box onto the footer rule.
- **Fix-ups (transform PART 7, all measured with the build's real wrap metrics, W43 D6 line-parity method):**
  - P6 bridges shortened to core line parity: A 2→1 lines (`Veja os gráficos e escolha a certa.`), D 3→2 lines (`Complete com as palavras: sondeo · muestra · indecisos · margen de error`).
  - P7 col3 shortened to restore the core geometry EXACTLY: errs note 2→1 lines, palabra note 4→3 lines, disclosure 6→3 lines. Result: **P7 col3 ends 1820.08 = core exactly; preview rect y=2440.08 = core exactly** (title baseline 2484.08, preview bottom 2558.08, 22px clear of the 2580 footer rule).
  - 25 P8 answer notes shortened to core line parity (each verified 1 line for the full `N. key — note` string at 13.5pt serif in 434px); #137/#138 deliberately NOT shortened (their PT keys are full sentences wrapping to 2 lines — the accepted W43 ES×PT exception, absorbed with zero warnings).
- **Final build:** zero FLOW OVERFLOW / zero HEAD TOO WIDE; all flows end inside their regions (P5-ex at 2577/2580 is the tightest, 3px margin, deterministic).

## 9. Reproduction

- Build copy: `hidden_files/weekly-report-w45-es-pt-build/`
- Transform record: `hidden_files/w45-es-pt-transform.py` (restore the copy from `hidden_files/weekly-report-w45-es-build/` and re-run it from scratch if any assertion ever fails mid-run — the script is not idempotent by design, it asserts)
- Single-process full build (never run content modules standalone):
  `cd hidden_files/weekly-report-w45-es-pt-build && ../../tools/venv/bin/python run.py`
- Render PNG + PDFs:
  `../../tools/venv/bin/python render.py` (render.py points at the new edition dir and the `VOL2-PT` PDF names)
- Geometry audit records: `hidden_files/w45-es-pt-occlusion.json` (0 flags) · `hidden_files/w45-es-pt-occlusion-core.json` (core 0, NEW 0) · `hidden_files/w45-es-pt-diff.json` (freeze diff) · `hidden_files/w45-es-pt-rowcheck.py` (same-baseline scan) · build logs `hidden_files/w45-es-pt-build1.log` (first build, overflows) → `hidden_files/w45-es-pt-build2.log` (final, clean) · `hidden_files/w45-es-pt-render.log`

## 10. Deliverables (files/weekly-report-w45-es-pt/)

- `svg/` 8 pages · `cards/` 8 PNGs (1950×2700)
- `La-Lucerna-VOL2-PT.pdf` (print) · `La-Lucerna-VOL2-PT-web.pdf` (web)
- This KIT · `ABSTRACT.txt` (Portuguese, single line, no ASCII double quotes; abstract_heading for insert: `Resumo`)

| file | bytes | sha256 |
|---|---|---|
| La-Lucerna-VOL2-PT.pdf (print) | 7,162,060 | a6459268952a33f3675793d6c860b222962f24ee816299fc2bacfd6a80f0e0cb |
| La-Lucerna-VOL2-PT-web.pdf (web) | 3,735,347 | 754cd83c50d69c9633df6be41ea9b7ded07759d7a635a78b52df6cf10142e672 |

Web PDF 3.74 MB < 10 MB limit ✓ (JPEG q85 @1400px, same recipe as the shipped ES siblings).

| page | edition SVG sha256 |
|---|---|
| p1-portada | 63f845cea51e412723b11e59e302e9f68d4cfab389fb9e3dd036204f02156063 |
| p2-vida | fc3c1f8f17b55fb93300a758be17a43d1574a216bd5cd66fad1c53dd09c8d8f4 |
| p3-cultura | 9122d2630a542ff0ea3378271b97c43ee51ac1b69ee6c417a78a4ef1a19387bb |
| p4-deporte | 223191328f3e409cf0538b27adbb0f272f411db937bcea5c826a1fc1ae712118 |
| p5-juventud | 0d3736f228897a2fed661e103e554bedbd81dad5e5579e2a00a5b1bca7c68e34 |
| p6-afondo | 97efd914d9067becf3c3c767a3c139d0068608ce6120c29970e061f1b3455fca |
| p7-lengua | 307daaeb1c6c5d0ac02d9f2203898093fdd2549ff08b9e92687153bbac95fd04 |
| p8-ejercicios | 325e692e08dbe850b6dd5f9bef5c508c204955d78ef122ed5aa672d03b169f2c |

## 11. Known items (for the independent proofreader — none of these block builder-complete)

1. P6 `Inmigración` ~5px bar graze — frozen core geometry, coordinator-adjudicated non-blocking (§6). Report presence only.
2. P8 #137/#138 print on 2 lines each (full-sentence PT keys) — accepted W43 ES×PT exception, absorbed with zero overflow warnings (§4, §8).
3. P5 exercise flow ends 3px above its bottom (2577/2580) — passes, deterministic, no warning.
4. P7 edition SVG contains 2 CJK-range characters — the frozen letter attribution's full-width parentheses (§5). Added CJK = 0.
5. The core's 11月12日 verification debt is VOID (core FIX1 removed that date from P6/P7); nothing in this edition reintroduces it.

## 12. Coordinator adjudications (2026-10-27, documentation only, no render change, FINALIZED)

- Independent proof (hidden_files/w45/es-pt-proof/PROOF-REPORT.md): paper ZERO defects (baseline 8/8, p8 CLEAN true diffs only [137,138], occlusion 0 + NEW 0, gloss 19=19, P7 golden 2×, 150, 8 cards visual, PDFs match §10 pins); sole blocking item was KIT §3 wording, corrected above (§3 + R5). No new proof round needed (KIT-only precedent).
- **O1 — P7 cartas box-bottom ink contact: ACCEPTED as frozen-core artifact, non-blocking.** Coordinator re-measured: cartas box rect (x=1451, y=1299.58, h=520.5 → bottom 1820.08) and disclosure last-line baseline 1832.69 are byte-identical in core and edition; the ink-riding-the-box-line phenomenon exists on the core card too and was not introduced by this edition. Audit 0 flags; text readable. Future ES fan-out proofs: report presence only, same as the P6 Inmigración graze rule; fail only if geometry differs from core or text is unreadable.
- **P1 `LA NOTICIA · A notícia`: ACCEPTED as-is** (see R5). No rebuild, no reproof for a legitimate pair-varying translation.
