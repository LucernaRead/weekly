# Lucerna Weekly — 日本語 × Português (JA × PT) · VOL.1 · Kit

- **Edition**: Japanese target text (frozen VOL.1 core) with ALL explanations in Portuguese (Brazilian) for Portuguese-speaking readers.
- **Issue week**: Mon 19 – Sun 25 Oct 2026 (W43). Masthead: **Lucerna** (no article, as the core).
- **Source core**: `files/weekly-report-ja-vol1/` (build `hidden_files/weekly-report-ja-build/`). Core NOT edited.
- **Build**: `hidden_files/weekly-report-ja-pt-build/` (copy of the core build; transform script in its `scratch/`).
- **Deliverables here**: `svg/` ×8, `cards/` ×8 (1950×2700), `Lucerna-VOL1-PT.pdf` (print), `Lucerna-VOL1-PT-web.pdf` (web).

## 1. Baseline proof (method step 1)

The core build was copied to `hidden_files/weekly-report-ja-pt-build/`, its OUT paths repointed to the copy's `scratch/baseline-svg/`, and run UNMODIFIED. Result: **all 8 regenerated SVGs byte-identical (sha256 8/8)** to the shipped core SVGs in `files/weekly-report-ja-vol1/svg/` (hash list preserved in `scratch/baseline.sha`). Only after this proof was the copy edited (OUT then set to `files/weekly-report-ja-pt/svg`).

Note: the core build's content files on disk (State B) differ from an earlier superseded draft of the core (different P7 clinic wording, different P8 note set); all transform pairs were derived from the live on-disk core files and verified by count assertions (transform v2: 4 initial mismatches, all in the P8 E-section instr contexts, fixed and re-asserted; final run: 0 fails).

## 2. Totals (identical to core)

- **150 exercises**: A2 48 · B1 75 · B2 27. Per page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- Types: completar frases 51 · escolha múltipla 50 · cloze 13 · associação 12 · verdadeiro ou falso 11 · construção de frases 8 · tradução 4 · escrita 1.
- P8 writing model: exactly **150 characters** (unchanged Japanese).
- Build log: zero HEAD TOO WIDE / FLOW OVERFLOW warnings.

## 3. Key-diff registry (the ONLY registry differences vs the core)

Translation-type items legitimately re-aim at Portuguese (core aimed at Chinese):

| # | Change | Core | This edition |
|---|--------|------|--------------|
| 137 | key → Portuguese; note → PT; instr | key 游行队伍12点从京都御苑出发。/ note 对照第3版 / instr 翻译 (translate to Chinese) | key **"O cortejo parte do Kyoto Gyoen às 12."** / note "Veja a página 3" / instr **"Traduza para o português"** (stem unchanged Japanese) |
| 138 | key → Portuguese; note → PT; instr | key 乱扔垃圾，要罚2,000日元。/ note 对照第5版 | key **"Se jogar lixo, a multa é de 2.000 ienes."** / note "Veja a página 5" / instr **"Traduza para o português"** (stem unchanged Japanese) |
| 139 | stem re-aimed (was Chinese, now Portuguese); note → PT; instr; **key unchanged** (Japanese 読書週間は来週の火よう日から始まります。) | stem 读书周从下周二开始。→ ___ / note 对照第7版 | stem **"A Semana da Leitura começa na próxima terça-feira. → ___"** / note "Veja a página 7" / instr **"Traduza para o japonês"** |
| 140 | stem re-aimed; note → PT; instr; **key unchanged** (Japanese 私は池袋のハロウィンのイベントに行きたいです。) | stem 我想去池袋的万圣节活动。→ ___ / note 对照第5版（池袋的活动） | stem **"Quero ir ao evento de Halloween de Ikebukuro. → ___"** / note "Veja a página 5 (o evento de Ikebukuro)" / instr **"Traduza para o japonês"** |
| 150 | key (apparatus) → PT; note → PT; writing expl → PT | key （开放题，范文如下）/ note 范文见本版 H 区（150 字） | key **"(tarefa aberta — texto-modelo abaixo)"** / note **"Texto-modelo na seção H desta página (150 caracteres)"** |

All other **145 keys are byte-identical to the core** — verified on the RENDERED P8: the set of printed key lines differs from the core's only at {137, 138, 150}. Keys keep the core's byte formats (e.g. "2,000", "1.5", "1,342" inside Japanese keys); Portuguese notes use PT number style (2.000 pessoas, 1.342 pontos, decimal comma "1,5 vez"). All 150 answer notes rewritten in Portuguese, including the notes the core printed as bare Japanese glosses. Key format kept: `{n}. {key} — {note}` with `— Página N —` separators.

## 4. Printed-note set verification

Extracted from the rendered P8 SVG by number: **this edition prints notes for exactly {1..150} = the core's printed set {1..150} — EQUAL.** (Items 141–144 also appear as match-exercise stems in the P8 test section, as in the core; counted once as notes.)

## 5. PT furniture — strings as finally shipped (verbatim)

- **Pairing badge (P1, 19px sans bold, brick)**: `TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`
- **Footer line (every page)**: `Lucerna · SEMANÁRIO JAPONÊS VOL.1 · TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS`
- **Footer page line**: `Página N de 8`
- **Gloss prefix**: `Nota — ` (the library gloss adds it; gloss strings do not carry it in-string)
- **Masthead**: `Lucerna` (no article). Masthead reflow identical to the other JA fan-outs: wordmark y 262→248, subtitle 330→316, badge inserted at y=356, tagline 372→390, rules 392/401→406/413. Portuguese deviations from the prescription: NONE required — badge and footers fit at full wording (verified by the geometric audit: zero edge-spill flags).
- Section heads follow the pattern `<Japanese> · <PT suffix>`: Em destaque / Em números / Pratique agora / Neste número (contents level for P8: TODOS) / A palavra da semana / Notícias breves / Quiz-relâmpago / Folhagem e sabores do outono / Palavras da estação / O uso de «見頃» / Exercícios da página N (right: `Respostas na página 8 · Níveis mistos: procure o seu número`) / O Jidai Matsuri e o fim de semana / Calendário / As dez escolas das classificatórias / Jovens / Comédia e Halloween / Os Jogos Para-Asiáticos em profundidade / Vamos ler o gráfico / Dados de prática / Língua / Clínica dos erros / A frase modelo / Cantinho dos leitores / Frases da semana (textuais, deste número) / Na próxima semana (VOL.2) / Teste e respostas / Respostas — agrupadas por página: basta procurar o seu número (right: `Uma nota breve em português para cada resposta · ✓ = a pergunta com o texto-modelo`).
- Instructions: Complete · V ou F · Construa a frase · Escreva · Associe lugares e picos (P2) · Associe eventos e lugares (P3) · Associe as palavras (P8 F) · Traduza para o português / Traduza para o japonês (P8 E). `あなたは？` boxes: suffix `· E você?`.
- P7 phrase translations carry `(p. N)` tags. Photo captions and credit lines stay byte-identical Japanese （写真：…), as in all JA fan-outs.

## 6. P7 phrases of the week — verification

Each of the 8 phrases is a verbatim contiguous excerpt of this issue's own articles; verified programmatically (reading-order concatenation per page): each occurs **exactly 2×** in the issue (once in its article, once in the phrases section) with the correct page tag (p. 1 ×2, p. 2 ×2, p. 3, p. 4, p. 5, p. 6).

## 7. Geometric occlusion audit (mandatory gate)

Method: paint-order SVG parse; real-font (PIL, Noto CJK JP faces, bold files for weight 700) INK boxes at 4× supersampling; checks = ≥30% glyph coverage by later opaque shapes, footer-band intrusion (y>2580, footer lines excluded), page-edge spill, line-through-ink (line boxes expanded by half stroke width), text-vs-text ink overlap, box-title/text ink vs box borders, stacked-box bottoms. Script validated first on a synthetic positive control (4 planted defects, 4 flagged).

- **This edition: 3 flags, ALL inherited from the frozen core with identical measurements** —
  1. P4 [BORDER] Japanese line-final `ません。` ink grazes the schedule-box bottom border (79.2×0.5px) — present identically in the core (its own audit: same text, same overlap). Frozen target text; not a fan-out defect.
  2–3. P7 [TXTTXT] ×2 — PIL ink-box overestimates between Japanese paragraph lines of adjacent level columns (9.2×20.2 and 30.0×20.0), byte-identical in the core; visually the columns are cleanly separated (verified on the rendered card).
- **Core (same script): 19 flags** (the 3 above + its own 16 footer-band lines, which are the core's legitimate footer elements; the PT footer lines are whitelisted by pattern and equally legitimate).
- **Adjudicated graze — あなたは？ boxes (P2/P3/P5)**: the Portuguese prompt's last line ends 1.2 / 0.65 / 0.4 px above the box's bottom border (core's Chinese prompt: 2.5 px). Mechanism: the box height is computed by the core's own formula from the prompt strings; Latin descenders extend ~2.5px lower than CJK ink from the same baseline. Ink never intersects the border or any glyph body (pixel-verified on the P5 zoom). Shortening experiments confirmed the gap is a formula constant (box shrinks in lockstep), so the full-fidelity prompt wordings were kept. NOT a defect by the shipped standard (defect = line intersecting actual ink); recorded here for the independent proofreader.
- **Result: 0 unresolved NEW flags vs the core.**

## 8. Freeze check

Full text diff of all 8 SVGs vs the core (multiset of text elements): every difference is explanation layer, pairing furniture, or a §3 registry item. No Japanese target text outside the registry changed. Residual Chinese-explanation characters: **0** (remaining Han-only strings are Japanese target text: dates, place names, vocabulary, tables, credit lines). The banned intermediary-layer term occurs **0 times** in the paper, this KIT, and the operative build code (methods renamed `.bridge(` → `.expl(`); the one-off transform scripts under `scratch/` quote the core's original call strings as search patterns for the renaming — scratch-only, as permitted.

## 9. Images (from the core KIT; all placed in the render, captions/credits unchanged Japanese)

| File | Subject | Credit / License |
|------|---------|------------------|
| stadium.jpg | Yokohama Stadium | Syced — CC0 (Wikimedia Commons) |
| maple.jpg | Autumn maple leaves | Poliphilo — CC0 (Wikimedia Commons) |
| mochi.jpg | Handmade mochi | Fumikas Sagisavas — CC0 (Wikimedia Commons) |
| hiroshige.jpg | Meiji-era procession print, 1876 | Utagawa Hiroshige III — Public Domain (Wikimedia Commons) |
| waseda1911.jpg | Waseda baseball team, 1911 | Bain News Service — Public Domain (Wikimedia Commons) |
| pumpkin.jpg | Halloween pumpkins | Petr Kratochvil — Public Domain (Wikimedia Commons) |
| paraswim.jpg | Para swimming (US DoD photo; caption states it is NOT this event) | EJ Hersom / US DoD — Public Domain (Wikimedia Commons) |

## 10. PDFs

- Print: `Lucerna-VOL1-PT.pdf` — **42,005,328 bytes**, sha256 `4c0ba09332bf83eb9a78db4c9e5807ad835f6baa23cb1279c9463c791aeaaa72`
- Web: `Lucerna-VOL1-PT-web.pdf` — **3,185,683 bytes** (< 10 MB), sha256 `519608cef8a07d977174caba10787d0670412ef0bd664c56412a8e766798ec3f`

## 11. Core integrity after the build

The shipped core SVGs were re-hashed after all work: **8/8 identical** to the pre-work record (`scratch/baseline.sha`). The core was never edited.

## 12. Proofread status

- Builder's own full proofread: DONE — all 8 pages read end-to-end on the rendered cards; all 150 keys re-derived against the Japanese text; calendar claims verified against the real 2026 calendar (Oct 17 Sat, 18 Sun, 19 Mon, 20 Tue, 22 Thu, 23 Fri, 24 Sat, 25 Sun, 27 Tue, 31 Sat, Nov 1 Sun, Nov 9 Mon — all match); totals/levels = core; P6 chart bars re-measured against the frozen data (34/28/22/16).
- **Independent proofread: PASS — ZERO PROBLEMS** (2026-10-21, second reader; full record in §13 below). No fixes were required; the shipped artifacts are byte-identical to the builder's delivery (edition SVG hashes re-measured at start and end of the proofread, unchanged).

## 13. Independent proofread record (second reader, full pass — shipping gate)

Method: everything re-derived independently; the builder's claims were not trusted. Baseline reproduced from the LIVE core build in a scratch copy (OUT repointed): all 8 regenerated SVGs **byte-identical (sha256 8/8)** to the shipped core SVGs. The builder's PT build copy likewise reproduces the shipped edition SVGs **8/8 byte-identical**, with zero HEAD TOO WIDE / FLOW OVERFLOW warnings and all flows ending inside their bottoms (P8 keys end y=2426 vs bottom 2540). The superseded-draft history (§1) is closed out: the edition's P7 clinic head is the live core's current wording （まちがい診療所） and its P8 note set is the live core's — the freeze diff below was run against the live core, not any draft or sibling.

**Freeze diff (all 8 SVGs, text multiset + non-text skeleton + image payloads).** Every text difference is explanation layer, pairing furniture, or a §3 registry item — **no undocumented Japanese-text change**. Non-text geometry differences are confined to: P1 masthead rules (documented reflow, identical to the other JA fan-outs: wordmark y=248, badge at 356), gloss/prompt box heights and the flow-shifted chips below them (the core library's own box formula reacting to Portuguese text length), and the P3 feature head 行列の見方 moving to the top of column 2 — byte-identical placement (x=527, y=225) in **all six shipped JA fan-outs** (DE/EN/ES/FR/IT/PT), i.e. the family's established balancer behaviour, not a PT anomaly. Image payloads are **byte-identical to the core on every page** (1/2/1/1/1/1/0/0), and every printed credit line matches the core and §9 (Syced CC0 · Poliphilo CC0 · Fumikas Sagisavas CC0 · Hiroshige III PD · Bain News Service PD · Petr Kratochvil PD · EJ Hersom / US DoD PD, with the P6 caption's not-this-event disclaimer intact).

**Key-diff verification (registry dumped from both builds and diffed programmatically).** Page/level metadata diffs: **none**. Key diffs: **exactly {137, 138, 150}**, strings exactly as in §3 (137 → "O cortejo parte do Kyoto Gyoen às 12."; 138 → "Se jogar lixo, a multa é de 2.000 ienes."; 150 apparatus → "(tarefa aberta — texto-modelo abaixo)"). The other **147 keys are byte-identical**. Stems re-aimed: **exactly {139, 140}** (Portuguese stems, Japanese keys byte-identical). All **150 notes differ from the core's — every one rewritten in Portuguese**, none left in Chinese. The four instruction strings verified in the render: "Traduza para o português" ×2 (137/138), "Traduza para o japonês" ×2 (139/140). All 150 keys re-derived against the Japanese text and the articles: correct, including the arithmetic (671+671=1,342, margin 33; 91+49+3=143; 71+69+3=143; 91/140=.650; chart 34+28+22+16=100, 34+28=62, 22−16=6; 1分46秒=106秒； 168%増→×2.68≈2.7倍） and the matching maps (25–28, 43–46, 141–144 → b,c,d,a).

**Printed-note set equality (mandatory gate).** Extracted from the shipped P8 SVGs by entry number: **core prints {1..150}; this edition prints {1..150} — EQUAL**, each entry carrying its note (150 in the ✓ model form, as in the core). Separators localized to "— Página N —", dash style kept.

**Totals/numbering.** 150 exercises, continuous 1–150; A2 48 · B1 75 · B2 27; per page 10/18/18/18/18/18/12/38; type counts map 1:1 onto the core's; writing model exactly 150 characters (frozen Japanese, string-identical to the core).

**P7 phrases.** All 8 phrases occur **exactly 2×** in the whitespace-stripped full text of both the core and this edition, with correct (p. N) tags on the Portuguese translations — counts EQUAL to the core per phrase.

**Calendar.** Every weekday/date claim machine-checked against the real 2026 calendar (Asia/Tokyo): Jidai Matsuri + general ticket sale Thu Oct 22; Japan Series G1 Sat Oct 24 18:30 and Shosoin opening + Para Games closing the same Saturday; G2 Sun Oct 25 18:00; Irohazaka peak from Fri Oct 23; ekiden qualifier + King of Conte final Sat Oct 17; Reading Week Tue Oct 27 – Mon Nov 9; Halloween Sat Oct 31 — all as printed. The Series is a preview everywhere; no result or score appears anywhere.

**Portuguese completeness and quality.** All 8 pages read end-to-end (full text extraction + all 8 rendered cards viewed). Every explanation element is genuine Brazilian Portuguese: glosses ("Nota — …"), heads, instructions, the あなたは？ prompts, all 150 P8 notes. Residual Chinese-explanation characters: **0** — every Han substring appearing in an edition-only text element is a Japanese target-text citation that occurs in the core's same-page text (verified programmatically). The P1 heat box keeps its date-labeled approximate framing ("Valores aproximados, de 17 de outubro." under the frozen Japanese approximate-count header).

**Furniture cross-check.** Badge, footers, "Página N de 8", gloss prefix "Nota — " and the SEMANÁRIO JAPONÊS VOL.1 pattern match the shipped EN×PT/FR×PT patterns exactly (target name JAPONÊS per the shipped table); masthead "Lucerna" with no article on all 8 pages; badge fits at full wording on one line (no shortenings). No divergences.

**Geometric occlusion audit (proofreader's own implementation).** Paint-order parse; PIL real-font INK boxes (JP index auto-detected exactly as the build library does; bold files for weight 700); line boxes expanded by half the stroke width; checks COVER (≥30%), LINEX, FOOTER (y>2580), EDGE, TEXTX, BOXTITLE-R. **Validated on a synthetic positive control first: all 6 planted defect classes fired (COVER/LINEX/FOOTER/EDGE/TEXTX/BOXTITLE-R), clean text and the legitimate footer stayed silent.** Results — core: **2 flags**; this edition: **2 flags, the identical pair, zero NEW**:
- P7 TEXTX ×2 — see the escalation note below (inherited core defect, pixel-identical).
- The builder's P4 BORDER item (line-final 「ません。」 vs the schedule-box bottom border) was pixel-adjudicated on the rendered cards of BOTH editions: border row 962, last ink row 960, **1 clear row between, identical in core and edition** — a sub-pixel model graze, ink never touches the border. Non-defect.
- The three あなたは？ prompt boxes were pixel-scanned on the rendered cards: last-ink vs border — P2: 6 clear rows (core 2), P3: 5 clear rows (core 2), P5: ink ends on the row immediately above the border row (0 clear rows; row profile of the border row shows 0 dark pixels, only the border's own anti-aliasing) — the descenders approach the border (~0.4 px, as the builder documented) but **no ink intersects the border** in any of the three. Non-defects; P5 is the tightest and is recorded here with its measurements.
- Stacked-box bottoms and box titles were covered by the audit's box checks plus the full card-by-card visual pass: no title ink crosses its own box border, no stacked box collides with the rules/subtitles below it, no page-edge spill anywhere.

**⚠️ Escalation — inherited FROZEN-CORE defect (not an edition defect; not fixable in the explanation layer).** The two P7 TEXTX flags are **real glyph overprints**, not measurement artifacts — this corrects the builder's §7 rationale ("visually the columns are cleanly separated"), which the pixels do not bear out. At the P7 level-column seams, frozen Japanese paragraph lines wrapped wider than the 434-unit columns overprint the neighbouring column's first glyph on the same baseline row: (a) B1 line at (527, 336.86) …スタジアムで大き × B2 line at (989, 336.86) という意味です… — ink overlap ≈30 units at true size; the き and と glyphs are superimposed into an illegible merged shape; (b) A2 line at (65, 369.54) …本を読む季節で × B1 line at (527, 369.54) な声が聞こえます。 — ink overlap ≈9 units; で/な merge. Pixel proof of inheritance: the corresponding strips of the rendered P7 cards are **hash-identical between the core and this edition** (strip sha256 55ab31e7… and fc5a4895…, and the wider y 280–400 crop is likewise identical, 4b71a2ea…), and the strings/coordinates are identical in both SVGs — the defect sits in the frozen core's P7 (21.5 px text wrapped past the 434-unit column pitch) and is therefore present in the core and in every shipped JA fan-out. It is recorded here for a future **core-level** correction cycle; altering it in this edition alone would break the freeze against the core and all siblings, and Japanese-text layout is outside the fan-out fix scope. It does not block this edition: on every gate that concerns the fan-out itself (freeze fidelity, explanation layer, keys, note set, furniture, PDFs) the edition is exact.

**Banned-term scan.** The intermediary-layer term (Chinese and English forms): **0 occurrences in the paper (all 8 SVGs) and 0 in the operative build code** (the explanation method carries its renamed form throughout). The KIT text itself quotes the core method's original name once, inside §8's disclosure parenthetical documenting the rename — the same disclosure pattern as the shipped JA×EN/JA×DE KITs (1 occurrence each); the two one-off transform scripts under the build's `scratch/` quote the core's original call strings as search patterns, as disclosed in §8 (adjudicated exception zone). No occurrence functions as a concept word anywhere in the edition.

**PDF pins (measured by the proofreader, identical to the builder's — no superseding render).** Web: **3,185,683 bytes** (< 10 MB), sha256 `519608cef8a07d977174caba10787d0670412ef0bd664c56412a8e766798ec3f`, 8 pages. Print: **42,005,328 bytes**, sha256 `4c0ba09332bf83eb9a78db4c9e5807ad835f6baa23cb1279c9463c791aeaaa72`, 8 pages.

**Core integrity.** The frozen core's 8 shipped SVG sha256 were measured before and after this proofread: **unchanged 8/8** (db328eb8… / ef09afeb… / 07e44381… / 01ade8a4… / 403dd3db… / 8a92c611… / 40984ce3… / 355de22c…).

**Verdict: PASS — one complete independent pass, zero problems in the edition. No fixes were needed or made.** One inherited core defect (P7 column-seam overprint ×2) is escalated above for the parent line; it is byte-identical in the frozen core and all shipped JA fan-outs.

---

## Patch note — 2026-10-21 · Core-level correction: P7 vocabulary-deck column-seam overprints (geometry only)

**Defect (found by the JA×PT independent proofread, §13; record: hidden_files/ja-p7-overprint-correction.md).** Two frozen Japanese lines on P7 wrapped past their column and overprinted the neighbouring column's first glyph, producing merged illegible glyphs: (a) B1 column (x=527, baseline y=336.86) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; (b) A2 column (x=65, baseline y=369.54) line ending …季節で vs B1 column (x=527) な声… Inherited from the JA core by every shipped JA fan-out; earlier "visually clean" adjudications of these flags were wrong and are superseded.

**Diagnosis.** The wrap width metric is correct (PIL, Noto Serif CJK JP; every greedy pre-kinsoku line fits the 434-unit column). The defect is in the kinsoku oidashi loop in `svglib.py` `wrap()`: pulled glyphs are never re-measured, and a line starting with a NO_START chain pulls one glyph per pass — B1's line cascaded 3 pulls (』→！→な) to 23 glyphs = 491.92 units (+57.92 over the limit; ≈30 units of ink past the 462-unit column pitch), A2's line cascaded 2 pulls to 471.28 (+37.28; ≈9 units past the pitch). A programme-wide census of the core found 16 overfull lines; only these 2 exceed the 28-unit gutter (all others ≤17.50 over, ink inside the gutter, shipped and audit-clean).

**Fix (identical in all 7 JA build dirs; patched `svglib.py` md5 d73e23b365676c3618d7e060b835eb4d in each).** New module constant `SEAM_SLACK = 28` (grid pitch 462 − column width 434). `wrap()` now records pre-kinsoku line widths and, after the oidashi loop, repairs ONLY lines oidashi itself grew past `max_w + SEAM_SLACK`: trailing glyphs are shed to the head of the next line until the line fits `max_w` again (cascading forward; a NO_START glyph is shed together with the preceding glyph so no line starts with one). No content string changed; no other wrap result in the issue changes (verified below).

**Verification (this edition).** Pages 1–6 and 8 SVGs byte-identical to the previously shipped files. P7 SVG differs in exactly 4 text elements — the two seam line pairs, at unchanged coordinates (A2 lines at y=369.54/402.22: …本を読む季節で→…本を読む季 / す。→節です。; B1 lines at y=336.86/369.54: …スタジアムで大き→…スタジアム / な声が聞こえます。→で大きな声が聞こえます。); concatenated text identical on all 8 pages; exercise registry unchanged (150). Geometric occlusion audit (ink-extent, synthetic positive control passed): flags 24 → 22, the delta being exactly the two P7 TEXTX seam flags removed, zero new flags. Pixel check on the rendered P7 card: seam (a) B1 ink now ends at column 962, B2 ink starts 994 (31 clear columns); seam (b) A2 ink ends 502, B1 ink starts 528 (25 clear columns) — glyphs no longer touch at either seam.

**Pins.** Web PDF: 3,185,683 B / sha256 519608cef8a07d977174caba10787d0670412ef0bd664c56412a8e766798ec3f → **3,186,184 B / sha256 6dee5721afa3017c6c67fc71b689602949efae271b7105f60ddf8a9b8fb0f124**. Print PDF: 42,005,328 B → 42,005,324 B. Repo re-pin by the main line.
