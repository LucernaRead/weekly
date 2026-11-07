# WEEKLY-KIT — Lucerna Weekly VOL.1 · zh-TW × PT (fan-out edition)

**Pairing:** Traditional Chinese target text (frozen VOL.1 core) · explanations in Portuguese (Brazilian) for Portuguese-speaking readers.
**Masthead badge (P1, verbatim):** TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA
**Slug used by the parent line:** `2026-w43-zh-tw-pt` · Issue week W43: Mon 2026-10-19 → Sun 2026-10-25.
**Build dir:** `hidden_files/weekly-report-zh-tw-pt-build/` (frozen core build copied; core never edited).
**Proofread status: builder's full pass COMPLETE (see §11); INDEPENDENT proofread COMPLETE — PASS, zero problems (see §13).**

## 1. Method
- Core build copied verbatim; output paths in the copy repointed to this build's own `scratch/baseline-svg/`; unmodified copy run and proven to reproduce the shipped core SVGs byte-identically BEFORE any edit (§2).
- Only the explanation layer was rewritten, via per-string pairs with count assertions (`scratch/pairs_*.json` + `scratch/apply_pairs.py`, 295 pairs): glosses, grammar notes, instructions, exercise apparatus, furniture, and all 150 P8 answer notes — fully in Portuguese. Traditional Chinese target text, images and layout geometry frozen. No script conversion anywhere; no Simplified-edition sentences imported (guaranteed by the CJK freeze check, §8).
- The intermediary-layer term (Chinese or English form) occurs 0 times in the paper, this KIT, and the operative build code (grep-verified over bslib4/content12/34/56/7/8/render/run). One-off scratch transform scripts (`scratch/apply_pairs.py`, `scratch/dump_reg_pt.py`) quote core call strings as search patterns only, confined to `scratch/`.

## 2. Baseline proof (frozen core reproduction, BEFORE edits)
Unmodified copy of the core build, output repointed to the copy's scratch dir: **8/8 SVGs byte-identical (sha256)** to the shipped core:
- p1-front c37cb10e6c55212a1f611005e73493fe00cedb97a32d68119059185225ebbf0d
- p2-life 494af3dafa61625002a1658ff6934fb8539d4821a96719321d429ae525b1e35b
- p3-culture 15315e2e8e6cf4731006cdad2052ba22df7061587108f40ba15fcbdaa61040e6
- p4-sport 02d393f9e0a3aa0613e2eaaed211ea384f2f99a0e3095a1e982a80dbfe298cfc
- p5-youth fc677f717cbed9675a6d3da7f0b904176cad4714e3247f817353883ce5f9fb58
- p6-deep 1367d4f03a66375ee8000f010d59881cd898fa02baad3f71d5b18275815b2d0d
- p7-lang 873a21acba1bf16df0fd23936f1e45800320766763a5caccc6cfd63dedded0e0
- p8-test c532615cbc6df045db8a52662f6e186946aaf37accc6c0fa50ea87a3a79e0743
Re-verified AFTER all work: **core shipped SVG hashes 8/8 unchanged.**

## 3. Totals (identical to core)
**150 exercises — A2 56 · B1 65 · B2 29.** Per page 10/18/18/18/18/18/12/38. Types 單選 65 · 完成句子 52 · 配對 20 · 完形單選 12 · 寫作 1. Writing model 134 characters. Registry dumped from both builds (`scratch/reg-core.json`, `scratch/reg-pt.json`) and diffed field-by-field (n/page/level/type identical for all 150).

## 4. Key-diff registry (complete)
Exactly ONE key differs — the documented apparatus item:
- **#150 (寫作）:** core `(開放題,範文如下)` → PT `(pergunta aberta — modelo abaixo)`; note → "Tarefa aberta — a resposta-modelo está acima, na seção F (134 caracteres)".
All other 149 keys byte-identical to the core (this core has no translation-type items). Any other difference would have been a red flag; none occurred.

## 5. Portuguese furniture as shipped (verbatim)
- P1 badge (21pt bold, BRICK, centred; ink 1275 of 1820 slot): «TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA»
- Footer L: «Lucerna · SEMANÁRIO CHINÊS TRADICIONAL VOL.1 · TEXTOS EM CHINÊS TRADICIONAL · EXPLICAÇÕES EM PORTUGUÊS» (ink 1136)
- Footer R: «Página N de 8» (ink 122, right-anchored 1885; clear of footer L)
- Gloss-box prefix: «Nota — » (the library's gloss()).
- Masthead: «Lucerna» (no article), exactly as the core ships.
- Band subtitles: P2 «… · Tempo, feriados e a liquidação de aniversário»; P3 «… · O Duplo Nove e a temporada do caranguejo-peludo»; P4 «… · A Série de Taiwan: Dragons contra Brothers»; P5 «… · As noites do Golden Bell e o mapa do Halloween»; P6 «… · Contagem regressiva para o Wine & Dine Festival»; P7 «… · Três níveis, três temas»; P8 «… · O teste da semana e todas as respostas».
- Section heads: 讀懂了嗎？ · Entendeu? / 填一填 · Complete / 算一算 · Faça as contas / 看賽程表 · A tabela / 看圖答題 · Leia o gráfico; P7 heads «A2 · 天氣的話 · Palavras do tempo», «B1 · 日子與節日 · Dias e festas», «B2 · 在地說法 · Jeito local de falar»; P8 heads «A · 判斷對錯 · Verdadeiro ou falso», «B · 本週大測驗 · O grande quiz», «C · 完成句子 · Complete as frases», «D · 讀一讀，答一答 · Leia e responda», «E · 情景說話 · Diga no contexto», «F · 寫一寫 · Redação».
- Instruction words: Complete (fill) · Associe palavra e definição / Associe nome e informação / Associe evento e informação / Associe ingresso e informação (matches) · Redação (writing).
- Keys header: «答案 · Respostas — em ordem de página, com uma breve nota em português para cada exercício» (ink 1177) + right «Todas as notas em português · ✓ = o modelo de redação» (ink 517; gap to left string 126, no overlap). Page headers «— Página N —».
- Key-line format: `N. key (note)` — space before the parenthesis, half-width parens only; writing item `150. ✓ (note)`.
- Number localisation: thousands separator "." (1.390, 40.000, 2.380), decimal comma, ordinals 1.º / 9.º / 10.º / 61.ª; currency written «HK$ 258» order; times kept HH:MM as in the frozen stems.

**Deviations from the core furniture (all recorded; wording shortened, never geometry):**
1. P1 badge: the core's bilingual badge line is replaced by the single all-caps PT badge in the BRICK slot (the shipped zh fan-out pattern; follows the PT column pattern of EN×PT/FR×PT).
2. P1 head «標題填空 · Palavras do título» — the fuller «Palavras das manchetes» measured 448.2 advance > CW 434 (build flagged HEAD TOO WIDE); shortened wording chosen by measurement.
3. P7 head «B2 · 在地說法 · Jeito local de falar» — «Jeitos locais de falar» measured 436.5 > 434 (HEAD TOO WIDE); shortened.
4. P4 box title «本週賽程 · Jogos» (short form, mirrors the zh×IT sibling's shortening of the same box).
5. P5 box title «週末行程 · Fim de semana» — shortened AFTER the occlusion audit: the fuller «Plano do fim de semana» ink (430) crossed the box's right border (pixel-confirmed, §10).
6. P2 «你呢？» box PT para and P6 pass-breakdown footnote para shortened AFTER the audit (each wrapped one line longer than the core's English and struck the box's bottom border; pixel-confirmed, §10).
7. Answer keys typeset tightened from the core's 13.3/1.16 (headers gap 2, lines gap 0.5) to 13.0/1.13 (headers gap 1, lines gap 0.25) — the same tightening the zh×IT sibling shipped; keys flow ends y=2520 (bottom 2540).
8. Two P8 notes shortened by wording for the keys flow: #121 «As fêmeas (xiè nǎ) estão no auge no 9.º mês lunar.» and #136 «Um caranguejo de 3 taéis cozinha ao vapor uns 12 minutos.» — content-equivalent; keys untouched.

## 6. Printed-note set verification (from the rendered P8 SVG, by number)
Core prints a note for every item. This edition: item-start lines extracted from the rendered `p8-test.svg` = **{1..150}, EQUAL to the core's set**; every item reassembled from its wrapped lines carries its parenthesised note (150/150); #150 prints as «150. ✓ (Tarefa aberta — …)».

## 7. Pinyin discipline verification (rendered P8 answer block)
Chinese words cited inside Portuguese notes are tone-marked PINYIN (e.g. mǎn qiān sòng bǎi, xiè nǎ, shūyùn, dēnggāo, pǐnwèi quàn, liú yǒu kàn). Final state measured on the rendered SVG: **full-width parens in the answer block = 0; parenthesis groups containing Han characters = 0.** (Chinese keys themselves are frozen target text and stand outside the parentheses, as in the core.)

## 8. CJK freeze check (per page, rendered SVGs)
Per-page CJK character multisets compared core vs this edition: **characters ADDED = 0 on all 8 pages** (strict sub-multiset — script conversion and sentence drift mathematically excluded). Removed CJK is confined to the explanation layer / pairing furniture (core's English-badge and bilingual heads, Chinese citations inside P8 notes converted to pinyin): p1 −30, p2–p7 −20 each, p8 −148.

## 9. Images (payloads byte-identical to the core; printed credits byte-identical)
- P1 typhoon.jpg — NASA Johnson Space Center — Public domain
- P2 rain.jpg — CorraleH — CC0
- P3 chrysanthemum.jpg — Masaki Ikeda （池田正樹） — Public domain
- P3 crab.jpg — Fumikas Sagisavas — CC0
- P4 baseball.jpg — unknown author — Public domain
- P5 stage.jpg — Kurt Kaiser — CC0
- P5 pumpkin.jpg — Benjamin Balazs — CC0
- P6 harbour.jpg — Wilfredor — CC0
- P6 wine.jpg — Jon Sullivan — Public domain
(Credits from the core KIT, generated from the Wikimedia Commons API Artist field. Payload counts per page 1/1/2/1/2/2/0/0.)

## 10. Geometric occlusion audit (mandatory gate)
Implementation: `scratch/audit_zh_tw_pt.py` — paint-order SVG parse; text boxes from TRUE INK extents (PIL `textbbox`, anchor "ls", production Noto CJK fonts with the TC index, bold included), line boxes expanded by half stroke width; checks COVER (≥30%), FOOTER (ink bottom > 2580), EDGE (page spill), LINEX (later line through ink), STRADDLE (ink crossing an earlier filled rect's border — includes every box title vs its own box borders and stacked-box bottoms vs subtitles below), TT-OVERLAP (text-vs-text).
- **Positive control:** synthetic SVG with six planted defects (cover, line-crossing, footer intrusion, edge spill, title-vs-border, text overlap) — **6/6 flagged**, clean control text unflagged.
- **Core baseline under this audit: 1 flag** — P1 masthead LINEX (the y=268 rule vs the «Lucerna» ink band), adjudicated non-defect (glyph ink does not touch the rule; identical in the shipped core).
- **This edition, first run: 4 flags** = the same masthead flag + 3 NEW STRADDLEs, all pixel-adjudicated on the rendered cards as REAL ink crossings and fixed by wording only (§5 items 5–6): P2 «你呢？» box para's 3rd line on the box bottom border; P5 «週末行程» box title ink crossing the right border; P6 pass-breakdown footnote's 3rd line on the box bottom border.
- **Final run after fixes: 1 flag — the same adjudicated masthead flag as the core. 0 unresolved NEW flags vs the core.**
- Also verified: P7 flows end above the phrases rule (hline y=1764 in this edition); P7 teaser ends 2564.16, above the footer band; P8 keys end y=2520 (bottom 2540).

## 11. Builder's proofread record (COMPLETE; independent proofread PENDING)
Read all 8 pages end-to-end in the rendered text. Re-derived all 150 keys against the Traditional Chinese stems (identical to the core registry except #150, §4). Wine & Dine arithmetic re-checked in the PT layer: 40+200+160=400, saves 142; 40+400+260+200=900, saves 342; 558−258=300; 2.380−1.580=800; model buys 2×258=516. All other arithmetic notes re-added (5.000/1.000→500; 2.600→200; 2.000→200; 498×2=996; 798−498=300; 15−12=3; 13+13=26; 2+1+4+2=9). P7 phrases: all 8 verbatim contiguous excerpts, each exactly 2× issue-wide (1× source article + 1× P7), tags p. 1, 2, 3, 3, 4, 5, 6, 6 — verified against both the PT and core renders. Every weekday/date claim checked against the real 2026 calendar (Oct 17 Sat G1 · Oct 18 Sun 重陽 · Oct 19 Mon HK holiday · Oct 20 Tue G3 · Oct 21 Wed G4 + sea warning · Oct 22 Thu Tianmu sale · Oct 23 Fri Golden Bell programmes + 疏運 starts · Oct 24 Sat drama + 連假 starts + Taoyuan opens · Oct 25 Sun parade 19:00 · Oct 26 Mon main event · Oct 29 Thu–Nov 1 Sun Wine & Dine · Oct 30 Fri Edward Lee dinner). Landfall explicitly undecided in both layers («會不會登陸，還沒有人知道» / "ninguém sabe ainda se ele vai tocar a terra"). Zero politics anywhere. Totals/levels = core (§3).

## 12. Deliverables (files/weekly-report-zh-tw-pt/)
- `svg/` ×8, `cards/` ×8 (1950×2700 PNG).
- Print PDF `Lucerna-VOL1-PT.pdf` — **37,638,298 bytes**, sha256 `2e9e5262ce04eafd507e902946cf0709ead4b0c9a5d63a09356bf2b321e2571e`.
- Web PDF `Lucerna-VOL1-PT-web.pdf` — **3,620,452 bytes (< 10 MB)**, sha256 `4b5b3ac5ff630ac12cdb6bfeb621ac53071d51b012da022bba1c5ffdcac434ab`.

## 13. Independent proofread record (COMPLETE — PASS, zero problems)

Independent, skeptical pass on the final rendered artifacts; nothing taken on trust, no fixes needed, no files of the edition altered (edition SVG hashes identical before/after this pass).

- **Baseline, re-run by the proofreader:** scratch copies of BOTH builds executed with output repointed to proofreader scratch — core build reproduces the shipped core SVGs 8/8 byte-identically; PT build reproduces the shipped edition SVGs 8/8 byte-identically.
- **Freeze / CJK accounting (per page, rendered SVGs):** CJK characters ADDED = 0 on all 8 pages; removed exactly p1 −30, p2–p7 −20 each, p8 −148 (matches §8). Strict sub-multiset — script conversion and target-text drift excluded. Full per-string diff read end-to-end: every removed string is a core English explanation/furniture string; every added string is its Portuguese counterpart; bilingual heads keep their Chinese halves verbatim.
- **Registry diff (proofreader's own dumps of both builds):** page/level/type metadata 0 diffs; stems (body) 0 diffs; instructions 0 diffs; **key diff exactly {#150}** — `(pergunta aberta — modelo abaixo)`, note `Tarefa aberta — a resposta-modelo está acima, na seção F (134 caracteres)`; all 150 notes rewritten, none contains a CJK character.
- **Printed keys/notes vs registry (rendered P8):** all 149 ordinary printed keys match the registry in both editions; all 150 PT printed notes match the registry notes (whitespace-normalised). #150 prints `✓ (note)` in the same convention as the core's `✓ Open task - …`. Core anomalies #104/#121 are the core's own typesetter full-width-paren conversion inside CJK citations — pre-existing core rendering, not an edition defect.
- **Printed-note sets BY NUMBER: core {1..150} = edition {1..150} — EQUAL** (core dash style `N. key — note`; edition paren style `N. key (note)`; every printed PT item carries exactly one parenthesised note, 150/150).
- **Pinyin discipline:** full-width parens in the PT answer block = 0; parenthesis groups containing Han = 0; Chinese citations inside PT notes are tone-marked pinyin throughout (mǎn qiān sòng bǎi, xiè nǎ, xiè gōng, shūyùn, dēnggāo, pǐnwèi quàn/zhèng, liú yǒu kàn, hāluō wèi, wàiwéi huánliú, zhūyú, fēng wáng, …).
- **Totals:** 150 — A2 56 · B1 65 · B2 29; per page 10/18/18/18/18/18/12/38; types 單選 65 · 完成句子 52 · 配對 20 · 完形單選 12 · 寫作 1; writing model 134 chars — identical to core in both registry dumps.
- **P7 phrases:** 8 phrases byte-identical to the core, tags p. 1, 2, 3, 3, 4, 5, 6, 6, each occurring exactly 2× issue-wide in BOTH editions and present on its tagged page.
- **Calendar (verified with `date`, Asia/Taipei):** Oct 17 Sat G1 · Oct 18 Sun 重陽 · Oct 19 Mon HK holiday · Oct 20 Tue G3 · Oct 21 Wed G4 + sea warning · Oct 22 Thu Tianmu sale · Oct 23 Fri Golden Bell programme awards · Oct 24 Sat drama awards + Taoyuan opens · Oct 25 Sun parade 19:00 · Oct 26 Mon main event · Oct 29 Thu–Nov 1 Sun Wine & Dine · Oct 30 Fri Edward Lee dinner — all correct. Landfall explicitly undecided in both layers. Zero politics.
- **Arithmetic re-added:** Wine & Dine 40+200+160=400 (saves 142), 40+400+260+200=900 (saves 342), 558−258=300, 2.380−1.580=800, model 2×258=516; plus 5.000/1.000→500, 2.600→200, 2.000→200, 498×2=996, 798−498=300, 15−12=3, 13+13=26, 2+1+4+2=9, Oct 23–27=5 days, 17:00→19:00=2h, 17:00→23:00=6h, 8×25=200 — all correct.
- **Geometric occlusion audit (two independent implementations):** (a) the canonical shared tool `tools/occlusion_audit.py` — selftest passed, then edition 0 flags, core 0 flags, 0 NEW; (b) the proofreader's own audit (paint-order parse, PIL true-ink boxes at TC face index 3, bold included, line boxes stroke-expanded; synthetic positive control 6/6 classes fired after the control caught and the proofreader fixed a tag-parser bug) — 0 flags on all 8 pages of both editions.
- **Pixel adjudication of the builder's claims (§10):** P1 masthead — «Lucerna» ink y 99.8–223.0 vs the y=268 rule band 266.5–269.5, card crop confirms a wide clear gap, identical in the core: NON-DEFECT confirmed. The 3 wording fixes verified by ink measurement AND card crops: P2 «你呢？» box PT para last line clears the box bottom by 17.3 units; P5 title «週末行程 · Fim de semana» ink clears the right border by 90.8 units; P6 pass-breakdown footnote last line clears the box bottom by 20.8 units. P8 typesetting tightening (§5 item 7) verified content-neutral (printed content = registry, above) with max non-footer ink bottom 2537.7, clear of the 2580 footer rule (core 2534.0).
- **Furniture:** badge, all 8 left footers and all «Página N de 8» strings byte-exact against the claimed PT column pattern; gloss prefix «Nota — » throughout (11 gloss boxes); masthead «Lucerna»; no English explanation residue anywhere.
- **Images:** embedded payloads + geometry byte-identical to the core per page (1/1/2/1/2/2/0/0); every printed credit byte-identical to the core and matching the core KIT (§9).
- **Banned-term scan:** the intermediary-layer term = 0 occurrences (both written forms) in the paper, this KIT, and the operative build code.
- **PDF pins (measured by the proofreader):** web `Lucerna-VOL1-PT-web.pdf` — **3,620,452 bytes (< 10 MB)**, sha256 `4b5b3ac5ff630ac12cdb6bfeb621ac53071d51b012da022bba1c5ffdcac434ab`; print `Lucerna-VOL1-PT.pdf` — **37,638,298 bytes**, sha256 `2e9e5262ce04eafd507e902946cf0709ead4b0c9a5d63a09356bf2b321e2571e` — both identical to §12.
- **Core integrity:** the frozen core's 8 shipped SVG sha256 re-verified after all work — unchanged (c37cb10e… / 494af3da… / 15315e2e… / 02d393f9… / fc677f71… / 1367d4f0… / 873a21ac… / c532615c…).

**Verdict: PASS — one complete independent pass, zero problems. Ready for repo insert as slug `2026-w43-zh-tw-pt`.**
