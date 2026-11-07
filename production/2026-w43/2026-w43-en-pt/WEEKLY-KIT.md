# WEEKLY-KIT — EN × PT (VOL.1, W43)

- **Edition**: The Lucerna Weekly VOL.1 — English target text, explanations in Portuguese (Brazilian). Slug: `weekly-report-en-pt`. FIRST edition of the Portuguese-explanations column: the furniture strings in §5 are the column pattern for all later ×PT editions.
- **Frozen core**: `files/weekly-report-en-vol1/` (never edited; build copy in `hidden_files/weekly-report-en-pt-build/`).
- **Status**: built + builder-proofread + geometric audit passed. **Independent proofread: PASS (2026-10-21, zero problems after one fix — see §7.8 and §12).**

## 1. Baseline proof

The unmodified core build, copied to `hidden_files/weekly-report-en-pt-build/` with output paths repointed to a scratch dir, reproduced all 8 shipped core SVGs **byte-identically (sha256 8/8 MATCH)** before any edit. At the end of the build the core's shipped SVG hashes were re-verified: **unchanged 8/8**.

## 2. Totals (identical to core)

- **149 exercises** — levels **A2 58 · B1 72 · B2 19**; per page 10 / 17 / 18 / 18 / 18 / 18 / 12 / 38.
- Type counts (PT names): Completar frases 39 · Escolha múltipla 34 · Transformação de frases 16 · Associação de palavras 12 · Leitura: V ou F 8 · Cloze 8 · Prática guiada 8 · Leitura de gráfico 6 · Completar o diálogo 5 · Correção 4 · Compreensão de leitura 4 · Tradução 4 · Escrita 1.

## 3. Key-diff registry (COMPLETE — the only registry differences vs the core)

Keys (answer field): only 3 of 149 differ, all legitimate re-aims of translation/apparatus items:

| # | Core key | EN × PT key |
|---|---|---|
| 136 | 投票不再是一天的事情，而是一个季节。 | `Votar não é mais coisa de um dia; é uma estação.` |
| 139 | 两家俱乐部都从未赢过世界大赛。 | `Nenhum dos dois clubes jamais venceu a World Series.` |
| 149 | 开放题 — 要点见写作框，范文在第 8 版写作框内 (apparatus) | `(pergunta aberta — o modelo está no quadro de escrita)` (note: `avaliação pelos pontos do enunciado`) |

Stems (printed exercise text, not the key field): only 2 differ — the translation instructions re-aimed at Portuguese:

| # | Core stem | EN × PT stem | Key |
|---|---|---|---|
| 137 | 翻译：76 人队以 106 比 100 赢得了比赛。 | `Traduza: 76ers venceram por 106 a 100.` | English, byte-identical |
| 138 | 翻译：今年，提前投票在星期一开始了。 | `Traduza: Este ano, a votação antecipada começou na segunda-feira.` | English, byte-identical |

(#137's stem is compressed to one line — headline-style Portuguese — so the item keeps the core's column packing on p.8; see §7.) All other 144 keys are byte-identical to the core; every note was rewritten in Portuguese; levels/pages unchanged for all 149.

## 4. Printed-note rule — deliberate choice, verified

The EN core's build filters which P8 answer notes print (a length threshold calibrated for Chinese) and prints only **62 of 149** notes. **Deliberate choice for this edition: print exactly the core's printed set (62), NOT the all-149 superset.** Portuguese notes are longer than Chinese ones, so the core's threshold rule cannot be reused; the edition's build applies the printed set **explicitly by exercise number** (`PRINT_NOTES` in content8.py, with the reasoning in a code comment).

Verification (sets extracted from the shipped P8 SVGs by matching each item's `N. key (note)` string): **core printed set = edition printed set = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82, 83, 84, 85, 86, 87, 89, 101, 106, 108–149} (62 items)**. Answer-key format: space before each note parenthesis, half-width parens only.

## 5. PT-column furniture (ESTABLISHED HERE — later ×PT editions copy these strings)

- Masthead: `The Lucerna` (exactly as the core ships).
- Masthead subtitle (46px serif): `SEMANÁRIO EM INGLÊS · VOL.1 · ESTÁDIOS · VOTOS · ABÓBORAS` (1533px, centered).
- **P1 badge (y=372 slot, brick, bold, 19.5px)**: `TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA` (1046px).
- Top strip centre: `WEEKLY IN ENGLISH · UM NÚMERO POR SEMANA · O INGLÊS QUE A AMÉRICA LÊ`.
- Clock band, right lines: `A EUROPA ATRASA O RELÓGIO DOMINGO` / `NOS EUA, EM 1.º DE NOVEMBRO (P. 7)` (the English line 2 ends at x≈1453; the PT line starts at x≈1494 — do not lengthen).
- Footer left: `The Lucerna · SEMANÁRIO INGLÊS VOL.1 · TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS`; footer right: `Página {n} de {total}`.
- Gloss/explanation prefix: `Nota — ` (comma-style glosses: `word, explicação · …`). NOTE: the build library's `gloss()` adds the prefix itself, so gloss-call strings must NOT carry it in-string (the core carried a doubled marker; this edition strips it at the 5 gloss() calls, keeping exactly one visible prefix everywhere).
- Explanation method: the core's explanation-box method is renamed `expl()` in this build; the old name occurs 0 times in paper, KIT and operative build code (one-off transform script in `scratch/` quoted the original call strings as rename search patterns — scratch only, not operative code).
- P8 keys header: `ANSWERS · Respostas e notas (páginas 1–8)`; group header `— Página {pg} —`; note format ` ({note})`.
- Section heads: pattern `ENGLISH · short PT suffix`, sized to the 434px column (≤ ~30 chars at 25px). As shipped: `A · TRUE OR FALSE ? · V ou F`, `B · FESTIVAL WORDS · Da festa`, `D · SENTENCES · Transforme`, `B · SPORTS WORDS · Do esporte`, `C · COMPARATIVES · Comparação`, `D · VERB FORMS · No passado`, `B · SCREEN WORDS · Da tela`, `C · THIS WEEK, LIVE · Presente`, `READING THE CHART · O gráfico`, `ELECTION WORDS · Da eleição`, `THE TOOLBOX · Ferramentas`, `THE ERROR CLINIC · Clínica`, `B · MULTIPLE CHOICE · Escolha`, `C · READING · Compreensão`, `D · SENTENCES · Frases`, `F · WORDS · Associação`, `G · DIALOGUE · Diálogo`.
- Box titles (≤ 398px at 23px bold — the box inner width): paired labels shortened the same way. As shipped: `THE WEEK IN NUMBERS · Semana`, `SAY IT ON THE NIGHT · Na noite`, `FESTIVAL WORDS · Da festa`, `DATES TO REMEMBER · Datas`, `THE WEEK'S FIXTURES · Jogos`, `SPORTS WORDS · Do esporte`, `WORDS OF THE SCREEN · Da tela`, `SAY IT ONLINE · Diga on-line`, `HOW TO FOLLOW IT · Como seguir`, `ELECTION WORDS · Da eleição`, `HEADLINE LANGUAGE · Manchete`. Rule for the column: **measure every title/head/fixed string with the build's text_w before shipping; shorten wording, never geometry.**
- P1 searches-box head: `Buscas da semana · Google Trends EUA` (413px in a 432px slot).
- Instruction words: 填空 `Complete` · 改写 `Reescreva` · 判断 `V ou F` · 配对 `Associe` (match header: `Associe as palavras`).
- Number localization: decimal comma (3,6% · 0,45 kg · US$ 13,5 bilhões), thousands dot (7.889 pessoas), ordinal `1.º`, `24.ª temporada`.
- **Portuguese target-name table (column standard)**: INGLÊS · ALEMÃO · FRANCÊS · ESPANHOL · ITALIANO · **NEERLANDÊS** · RUSSO · JAPONÊS · COREANO · CHINÊS SIMPLIFICADO · CHINÊS TRADICIONAL. (NEERLANDÊS chosen over HOLANDÊS, following the PT core's own usage «neerlandês».)

## 6. Method

Core build copied, baseline-proven, then ONLY the explanation layer rewritten (glosses, notes, instructions, apparatus, P8 answer notes) — English target text, images and layout geometry frozen. Freeze check: per-page token diff vs the core — every lost non-CJK token is accounted for by furniture replacement, gloss comma-style punctuation attachment, CJK-adjacent digit tokens, or number localization (0.45→0,45; 7,889→7.889); no English target sentence lost or gained a content word. Zero CJK/fullwidth characters in the final SVGs (verified per page).

## 7. Defects found and fixed during this build (wording only — geometry never touched)

1. **P6 article gloss overflow**: the article flow's space for the gloss box is 170px (core's 3-line Chinese gloss); the full PT gloss needed 5 lines → the box overflowed into the chart zone. Rewritten to a 3-line gloss (`midterm, eleição de meio de mandato · House, a Câmara · turnout, a participação · incumbent, o titular.`); *margin* is dropped there only — it stays glossed in the page's ELECTION WORDS box and exercises. Article flow now ends y=1408, exactly the core's value.
2. **P8 battery overflow into the writing strip**: PT translation stems (#137/#138) wrap to 2 lines where the Chinese took 1, pushing #137 into column 3 and the dialogue tail ink to y=1549.7 — inside the MODEL box region (top y=1500). #137's stem compressed to one line (see §3), restoring the core's column packing; battery ends y=1448 (core: 1418; writing hline at 1486).
3. **P1 searches-box head spill**: `Buscas da semana nos EUA · Google Trends, retrato dos EUA` measured 626.7px in a 432px slot — ink reached x=2001, past the page edge. Shortened to `Buscas da semana · Google Trends EUA` (413.4px).
4. **Box titles crossing their borders**: 11 paired box titles measured 401–555px vs the 398px inner width; the worst (`THE WEEK IN NUMBERS · A semana em números`, 553.6px) struck through exercise #6's text. All shortened per §5; re-verified in the rendered cards.
5. **Clock-band graze**: PT band line 2 left only a ~8px nominal gap to the English line (rendered as contact). Shortened to `NOS EUA, EM 1.º DE NOVEMBRO (P. 7)` (nominal gap ~40px; visually clear).
6. **Match instruction crossing its column**: `Associe as palavras às definições` (P2/P4 match headers) ran past the column edge; shortened to `Associe as palavras`.
7. **16 section heads** exceeded the 434px column (build HEAD TOO WIDE warnings) → shortened PT suffixes per §5. Final build log: **zero FLOW OVERFLOW / HEAD TOO WIDE warnings**; every flow ends at or inside its region, most exactly at the core's values (P2 col3 1534.6, P2-ex 2565 — the core's own adjudicated 3px trailing-gap condition, ink clear of the footer rule; P6-article 1408; P7-clinic 2107; P3-main 2410).

8. **(Added by the independent proofreader — see §12.) P6 PRACTICE DATA caption struck through by the y=1507 section rule**: the caption's Portuguese half ran ~340 px too far under the rule (x 989–1423); the builder's audit missed it. Gloss shortened to «Dados de prática fictícios.» (caption now ends x≈948, clear of the rule); only p6 re-rendered; full proofread re-run clean.

## 8. Geometric occlusion audit (mandatory gate) — PASS, 0 flags

Own implementation (`scratch/audit_pt.py` in the build dir): SVGs parsed in paint order; text ink boxes from PIL real-font metrics using the build's own fonts (Noto Serif/Sans CJK — the same metrics the layout uses), line boxes expanded by half stroke width. Checks: ≥30% glyph coverage by later opaque paint, page-edge spill, inner-frame spill, footer-band intrusion (ink below y=2580 outside the footer), box-title ink vs its own box borders (BOX-SPILL), stacked ink-on-ink overlaps (INK-INK). **Validated on a synthetic positive control (known covered line flagged, clean line not flagged).** Process note: the first audit pass used a wrong font family (DejaVu) and a text regex that silently skipped bold elements (`font-weight="700"`); both were caught and fixed — the final pass parses all ink including bold and reports **0 flags on all 8 pages**. The audit's catches plus two visual catches (§7.3–7.5) were all fixed by wording and re-audited. Known adjudicated adjacency (from the core): P1 word-of-week gloss ink vs the rule below it — in this edition the gloss is a single line (`Voltar uma hora: spring forward, fall back.`, 369px), so the adjacency does not arise.

## 9. Builder's proofread (independent proofread PENDING)

- Read all 8 pages end-to-end from the rendered text; re-derived all 149 keys against the articles — all consistent (incl. match letters p.2 b/d/c/a, p.4 d/b/a/c, chart readings 34/27/61/18/100, calendar facts).
- P7 phrases: all 8 sentences verbatim; per-phrase occurrence counts across the paper equal the core's (1, 1, 1, 1, 5, 1, 1, 1); the P7 page-tag sequence is identical to the core's (4, 6, 6, 4, 2, 4, 4, 6, 6, 2, 2).
- Weekday/date claims verified against the real 2026 calendar: Mon Oct 19 (TX opens), Tue Oct 20 (NBA), Wed Oct 21, Thu Oct 22, Fri Oct 23 (World Series G1), Sat Oct 24 (FL), Sun Oct 25 (F1 + EU clocks), Fri Oct 30 (TX ends), Sat Oct 31 (Halloween), Sun Nov 1 (US clocks), Tue Nov 3 (Election Day) — all correct.
- Visual check of rendered cards: P1 masthead/badge/band/searches/numbers box, P5 col-3 boxes, P8 battery/writing boundary — all clean.

## 10. Images (credits as in the core KIT — all public domain)

- p1: `ws1912.jpg` — Boston fans, Polo Grounds, Oct 8 1912 (Bain News Service / Library of Congress).
- p2: `sscard.jpg` — Social Security card, 1943 (Social Security Administration).
- p3: `halloween1912.jpg` — «A Halloween Wish» postcard, 1912.
- p6: `capitol.jpg` — United States Capitol.

## 11. Deliverables (`files/weekly-report-en-pt/`)

- `svg/` ×8, `cards/` ×8 PNG (1950×2700).
- Print PDF `Lucerna-VOL1-PT.pdf` — **8,622,488 bytes**, sha256 `c23e630fded096f301d1a895875821a508c92d491f4a8b3bd52585e0423a8fc4` (final, post-proofread-fix — supersedes the builder's pins).
- Web PDF `Lucerna-VOL1-PT-web.pdf` — **6,523,708 bytes** (< 10 MB), sha256 `5319ccca1fe30c8563f42ceeaecd412a94e521384e1735656855f3b85b6cdd8e` (final, post-proofread-fix — supersedes the builder's pins).

## 12. Independent proofread — **PASS** (2026-10-21)

One complete, skeptical, independent pass over the final rendered artifacts; everything below was verified by the proofreader, not taken from the builder's claims. One real defect was found and fixed (§7.8), after which the **entire pass was re-run from the top** on the final artifacts — zero remaining problems.

**8. (found by the independent proofreader) P6 PRACTICE DATA caption struck through by a section rule.** The caption's Portuguese half («Dados de prática, inventados para o exercício; não são uma pesquisa real.») carried the caption to x≈1359, and the gold section rule at y=1507 (x 989–1423, drawn after the caption) cut through the glyph stems of the last ~340 px of the line — pixel-proven on the shipped card and on an isolated two-element render (glyph ink present in the rule's rows 1506–1507 across x 997–1336). The builder's audit missed it. The frozen core's much shorter Chinese gloss ends at x≈1016 and only grazes the same rule with its final glyph's bottom row (inherited core geometry, not touched). **Fix (explanation-layer wording only):** gloss shortened to «Dados de prática fictícios.» — the English half, which remains fully printed, carries the complete wording; the caption now ends at x≈948, fully clear of the rule. Only p6's SVG changed (other 7 SVGs byte-identical); p6 card re-rendered; both PDFs rebuilt (pins in §11 supersede the builder's). The full pass was then re-run clean.

**Verification record:**
- **Baselines reproduced independently:** scratch copies of the unmodified core build and of the shipped PT build each reproduce all 8 of their shipped SVGs byte-identically (8/8 + 8/8); PT build log zero FLOW OVERFLOW / HEAD TOO WIDE; P6 article flow ends y=1408 in both logs, exactly the core's value.
- **Freeze verdict: PASS.** Full per-page text diff vs the frozen core reviewed line by line: every difference is explanation layer (Chinese → Brazilian Portuguese), pairing furniture (§5), number localization (0,45 kg · 7.889 pessoas · 24.ª), or a documented registry item (§3) — plus the §7.8 caption shortening from this proofread. No undocumented English-text change. Zero CJK and zero full-width characters in all 8 edition SVGs.
- **Registry diff (proofreader's own dumps of both builds):** levels A2 58 · B1 72 · B2 19 and per-page 10/17/18/18/18/18/12/38 identical; page/level metadata zero mismatches; type names a clean 13→13 CN→PT mapping with identical counts. **Key diffs = exactly {136, 139, 149}** with the strings in §3 (both translation keys faithful to their English sentences); **stems re-aimed = exactly {137, 138}** («Traduza: …»), their English keys byte-identical; all other 144 keys byte-identical. The only notes identical to the core are 9 language-neutral ones (verb-arrow and arithmetic notes, e.g. «34 + 27 = 61»); chart arithmetic re-checked (34/27/61/18/100 ✓; 76ers 106–100 consistent in #59/#137).
- **Printed-note sets (extracted by number from the shipped P8 SVGs):** core = {11, 14, 15, 19, 35, 36, 40, 42, 49, 65, 74, 82, 83, 84, 85, 86, 87, 89, 101, 106, 108–149} (62); edition = the same 62. **EQUAL.** The core set was cross-checked two further ways — from the core build's own print rule applied to the registry, and by whitespace-insensitive extraction (CJK notes wrap mid-phrase) — all three agree.
- **P7 phrases:** per-phrase occurrence counts identical in both editions (1, 1, 1, 1, 5, 1, 1, 1 — «Voting is no longer a day; it is a season.» legitimately recurs 5×); P7 page-tag sequence identical (4, 6, 6, 4, 2, 4, 4, 6, 6, 2, 2); the phrases are the core's own forms, inherited unchanged.
- **Calendar:** every weekday/date claim checked against the real 2026 calendar (Mon Oct 19 · Tue Oct 20 NBA · Fri Oct 23 World Series · Sun Oct 25 F1/EU clocks · Sat Oct 31 Halloween · Sun Nov 1 US clocks · Tue Nov 3 Election Day) — all correct. Portuguese quality read across all 8 pages: genuine, idiomatic Brazilian Portuguese throughout (one terse note gloss, #140 «meio-mandato», adjudicated acceptable shorthand).
- **Geometric occlusion audit — proofreader's own implementation** (paint-order parse; PIL real-font ink boxes calibrated against a pixel render; line boxes expanded by half stroke width; all `<text>` elements parsed including bold — the builder's two blind spots avoided; **synthetic positive control fired all 7 classes — COVER/LINEX/EDGE/FOOTER/TEXTX/BOXSPILL-R/BOXSPILL-B — and stayed silent on clean text**). Core reference run: 3 flags. PT final run: **2 flags, both pixel-adjudicated NON-DEFECTS** — (i) P1 masthead TEXTX: wordmark ink bottom row 264 vs subtitle ink top row 285 on the rendered card (≥20 clear rows; em-box overestimate, same pairing as the core); (ii) P2 «AND YOU?» box BOXSPILL-B: last prompt line's glyph ink ends row 1529, box border at y≈1534.6, zero dark pixels at rows 1534+ (getbbox descender allowance overestimates). The core's P1 word-of-week LINEX graze was re-adjudicated on pixels: gloss ink rows 1830–1842, rule rows 1843–1844 — zero overlap, non-defect as previously adjudicated; in this edition the gloss is a single line and the adjacency does not arise. Builder's §7 fixes pixel-/measure-verified: P1 searches head ink ends x=1832 inside its slot; clock-band PT line starts x=1493.7 with the claimed ~40 px gap; P8 battery max ink bottom 1460.1 in both editions, clear of the writing strip (hline 1486 / model box 1500); all box titles inside their borders (0 BOXSPILL survivors).
- **Images:** embedded payloads byte-identical to the core per page (p1/p2/p3/p6, one each); printed credits identical and matching §10 / the core KIT.
- **Banned-term scan:** 0 occurrences in the paper, this KIT, and the operative build code.
- **Final PDF pins (measured by the proofreader; supersede the builder's):** web **6,523,708 B**, sha256 `5319ccca1fe30c8563f42ceeaecd412a94e521384e1735656855f3b85b6cdd8e`, 8 pages, < 10 MB ✓; print **8,622,488 B**, sha256 `c23e630fded096f301d1a895875821a508c92d491f4a8b3bd52585e0423a8fc4`, 8 pages.
- **Core integrity:** the frozen core's 8 shipped SVG sha256 are **unchanged** after all proofread work (verified at start and end). Furniture cross-check vs FR×PT §5: same badge/footer/gloss patterns and target-name table (NEERLANDÊS) — the only divergence is per-edition wording of the P8 keys-head Portuguese gloss («Respostas e notas» here vs «TODAS AS RESPOSTAS COM NOTAS» in FR×PT), recorded here for the parent line; not a defect.

**Verdict: PASS — zero problems. Ready for repo insert as slug `2026-w43-en-pt`.**
