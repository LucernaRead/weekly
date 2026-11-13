# WEEKLY-KIT — Portuguese Weekly VOL.4 (Japanese explanation layer)

- Issue: 2026-W47, Monday 16 November – Sunday 22 November 2026
- Target language: Portuguese (Brazilian text) · Explanation layer: Japanese
- Repo slug: `2026-w47-pt-ja`; built by copying `core-pt/` (read-only) and rewriting only the explanation layer (SEG/OVR tables + furniture). Target-language text, numbers, facts, dates and answer keys are frozen from the core.
- Layout: 8 pages, 1950×2700, 4 columns; 150 exercises (A2 48 / B1 71 / B2 31; per page 10/18/18/18/18/18/12/38); model text 88 words (within the 80–100 range, counted by program).
- Deadline: 10 November 2026 (noted in the P4 table note and in this KIT; 14–22 November fixtures are previews, results in the next issue).
- **Kinsoku:** this edition reuses the W46 pt-ja `svglib.py` whole (md5 `f61efb1bdac0e1c0a38fc60b300f238e`, byte-identical to the W46 pt-ja file, copied over the core's svglib.py after the core copy). The W47 core svglib is byte-identical to the W46 en svglib (no kinsoku); the ja edition must NOT use it. `bslib4.py` is the core's — the only differences from W46 pt-ja bslib4.py are the already-transformed footer/gloss furniture lines, which transform.py's bslib4 step writes.

## 1. Content per page

- P1 lead (A2): Consciência Negra: sexta é feriado em todo o país (41 non-space characters, ≤56 limit). Friday 20 November Black Consciousness Day national holiday + three-day break 20–22 Nov; numbers box (20 / 1695 / 2023 / 3); word of the week consciência; week calendar (Mon 16–Sun 22, incl. national team 14/17 Nov, Enem day 2 on 15 Nov, Palmeiras × Flamengo on 21 Nov); capoeira image + row-B mini-feature "two halves of a week" (7–8 Nov cup semi-finals + São Paulo GP; 14–22 Nov national team + Enem + Brasileirão) + 3 flash items; practice 1–6; lightning quiz 7–10. Japanese: "3連休" (lead gloss), "速攻クイズ" for the lightning quiz, "短報" for the EM POUCAS PALAVRAS section.
- P2 Life (A2): Sexta, 20 de novembro: o feriado e o feriadão. Holiday details, shops on the holiday, "don't get it wrong" mantra box, gloss; VOCÊ SABIA? 3 items; long-weekend schedule 4 cells (SEX 20 / SÁB 21 / DOM 22 / SEG 23); exercises 11–28.
- P3 Culture (A2→B1): Zumbi e Palmares: a história do 20 de novembro. Zumbi's death 20 November 1695, Palmares history; Zumbi portrait (Antônio Parreiras, 1927); "words of memory" box; exercises 29–46.
- P4 Sport (B1): Grêmio e Palmeiras decidem a Copa do Brasil. Verified semi-final second-leg results (Atlético-MG 1–1 Grêmio, aggregate 3–1; Vasco 2–1 Palmeiras, aggregate 2–2, penalties 5–4) + final (6 December, single match, Mané Garrincha) + Brasileirão rounds 35/36 + F1 Norris win; "finalists" data box + 6-row football week table (with deadline note); exercises 47–64. Matching instruction: "ペアを作ろう" (no W46 ja hit for this string; new, in the W46 "〜しよう" instruction style).
- P5 Youth (B1): Depois do Enem: a espera começa. Day 2 of the exam + unofficial keys out the same evening + official key by the 10th working day (end of November) + TRI scoring; five-step "waiting plan" box + gloss; study photo (Gary Todd); exercises 65–82. True/false instruction: "正しいか間違いか" (W46 shipped).
- P6 In depth (B2): O gabarito explicado: como funciona a espera. Two Sundays, Edital nº 64/2026 §15.1 "até o 10º dia útil", 27–30 November window (the disagreement is whether the 20 November holiday counts as a working day; this issue prints both dates), TRI + golden rule; charts: working-day count (16–30 Nov = 15 days = 10 working days + 5 weekend/holiday days) and "two answer keys" comparison; 6-step timeline; exercises 83–100.
- P7 Language (A2/B1/B2): three-level grammar (holiday and dates em/no dia 20, cair; pretérito perfeito for the cup weekend; futuro do subjuntivo for waiting for the key); 4 common mistakes; word of the week; readers' letters (editorial example + bilingual disclosure, see §4); Os Lusíadas 1572 first edition image; 8 phrases of the week (verbatim from this issue, see §5); next-week preview VOL.5 (27 November Black Friday + official key + 6 December final); exercises 101–112.
- P8 Test (38 items): chronicle fill-in 113–120, general questions 121–128, reading (Rafael's long weekend in Salvador) 129–132, sentence building 133–136, translation 137–140, matching 141–144, box-office dialogue 145–149, writing 150 + model text (88 words) + all 150 answers (register-generated); Mané Garrincha stadium photo below the exercise flow in column 3.

## 2. Fact sources

Same as the core KIT (checked 2026-11-10, all public): Consciência Negra / Lei nº 12.519/2011 / Lei nº 14.759/2023; Copa do Brasil semi-final second legs 7–8 Nov 2026; Enem 2026 Edital nº 64/2026 §15.1; Brasileirão 2026 rounds 35/36; São Paulo GP 8 Nov 2026; national team FIFA window (14 Nov 7h15 Japan × Brazil, 17 Nov 7h Singapore × Brazil — D1 correction: 17 November is 7h, not 7h15); Novembro Azul; Black Friday 27 November. No new facts added in this edition; target-language text frozen from the core. Full source list and refs are in `core-pt/WEEKLY-KIT.md` §2 and in `2026-w47-pt-en/WEEKLY-KIT.md` §2.

## 3. Images (5, all checked via Wikimedia Commons API, credit printed; full table in `assets/CREDITS.md`)

Same 5 images as the core, byte-identical (capoeira 699,781 / zumbi 194,233 / estudo 256,737 / lusiadas 404,078 / garrincha 914,576 bytes; cmp verified):

- P1 capoeira.jpg: Johann Moritz Rugendas, "Jogar capoëra ou danse de la guerre", from *Voyage pittoresque dans le Brésil* (Paris, 1835), Rio. Public domain (PD). Core KIT correction: caption by publication year 1835 (not "c. 1830").
- P3 zumbi.jpg: Antônio Parreiras, "Zumbi", 1927 (signed). Public domain.
- P5 estudo.jpg: Gary Todd, Sias Library students studying, 2017, CC0.
- P7 lusiadas.jpg: *Os Lusíadas* first-edition title page, Luís de Camões, Lisbon, António Gonçalves, 1572. Public domain.
- P8 garrincha.jpg: Estádio Mané Garrincha exterior, Brasília, photo by Luis Dantas. Public domain.

## 4. Promises kept

- W46 VOL.3 promises (Copa do Brasil second-leg results + finalists; Black Consciousness Day Friday 20 November; Enem answer keys as a topic): all kept — P4 / P1 lead / P5+P6 main thread respectively.
- Readers' letters + best P8 essays: no real letter arrived (F-MAIL rule: only submissions the user sends directly count; mailbox not checked, no readers/names/quotes invented). P7 carries the editorial example («Vou aproveitar o feriadão para ler sobre Zumbi. Bom feriado!» — EXEMPLO DA REDAÇÃO) + bilingual disclosure: Portuguese Nota da redação: as cartas reais e os melhores textos do VOL.3 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.5.; Japanese (W46 shipped style, VOL.2→VOL.3, VOL.4→VOL.5, pre-measured at 3 lines before run1 — see §6): "編集部注：VOL.3 で約束した実際の手紙と最優秀作文は締切までに届かず、本号は例文を掲載し、約束は VOL.5 へ延期します。" Example label: "編集部の作例です。本物の手紙ではありません。あなたの手紙を送ってください。" (W46 ja form, ending "。" — see §6 for the OVR mechanism). Promise carries to VOL.5. Fan-out keeps the Portuguese example + Portuguese disclosure verbatim; only the disclosure/label are translated.
- Next issue preview (P7, VOL.5): 27 November Black Friday + official key before the end of the month + 6 December final approaching. Open update slots: exact official-key date, 14–22 November results (two national-team friendlies, Brasileirão rounds 35/36) in VOL.5.

## 5. Phrases of the week (P7, verbatim from this issue, each occurring exactly twice in the body text; gates_core.py counts each one)

1. Consciência Negra: sexta é feriado em todo o país (P1 lead) · 2. o feriado abre um fim de semana de três dias (P1) · 3. Zumbi nasceu em Palmares (P3) · 4. sem memória, não há futuro (P3) · 5. o agregado ficou em 2 a 2 (P4) · 6. a espera pelo gabarito (P5 body) · 7. primeiro as fáceis, depois as difíceis (P6) · 8. Confira o transporte, guarde o documento e aproveite o feriadão (P2 PARA NÃO ERRAR box). P7 gives each a Japanese translation + page tag.

## 6. Gate record (Japanese edition, own measured values)

- Build self-check gates.py (adapted from gates_core.py): **16/16 PASS** (VOL.4/date/subtitle, footer + page numbers 8/8, no VOL.3 masthead residue — VOL.3 appears only in the P7 disclosure as the cited promise issue, deadline note + final naming, P1 masthead line width ≤1820, same-baseline collisions 0, page-frame ink crossings 0, P6 chart-label GRAZE 0%, gloss 29 items enumerated + stems alive, P7 phrases 2× + page tags + Japanese, readers'-corner strings 5/5, images + credits 5/5, P7 phrase zone clear of the preview box, P1 lead ≤56 non-space characters, 41).
- tools/occlusion_audit.py on the final SVGs: **1 flag — the P1 LINEX graze, core-carried, not a ja defect.** Detail: the quiz-section rule at y=2312 grazes the top 0.2px of the ink of the frozen line "em Brasília. (Página 4)" (ink top 2312.8 vs line box [2311, 2313]); invisible in the render. The geometry and element order are byte-identical in core-pt and in all shipped fan-out editions; re-running the same tool on the shipped pt-fr SVG and on core-pt/svg gives the same 1 flag. The earlier en/de/fr "0 flags" records predate the current tool state — the flag is deterministic now, and it is not fixable inside a fan-out edition without moving frozen core layout. Note: the FIRST occlusion run for ja failed its own self-test (clean control page produced 1 COVER flag on the kana "リ", 84% covered) and reported nothing; the immediate re-run passed (selftest OK, clean controls silent, 1 LINEX flag). The first failure was a transient self-test flake, not an edition defect — recorded here because the self-test result is part of the gate record.
- tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150: **150/150**. tools/p8.py compare vs core: **CLEAN**, keydiff=[137, 138] only — the two translation answers, verified correct in Japanese (137 "11月20日金曜日は全国の祝日です。", 138 "パルメイラスはPK戦で5–4で勝ちました。").
- tools/freeze.py baseline: **8/8 SVGs byte-identical** (repointed files: none). freeze diff: CJK added 3,255 (expected — the Japanese explanation layer replaces the Chinese one; kanji/kana are CJK by Unicode range). For ja the meaningful freeze check is the U+3000 furniture separators (9 total, same as the Latin editions) and the absence of Simplified-only characters (verified: NONE in the tables and in the final SVGs).
- Print PDF: A-Lucerna-VOL4.pdf, **15,449,291 bytes**, 8 pages, sha256 `9208d231d66cf6e612f367cc1702c8003b5c1bcfd447da414dcedac5d8037768`. Web PDF: A-Lucerna-VOL4-web.pdf, **1,433,879 bytes**, 8 pages, sha256 `a9b4a30929c18cbd949062d1cf79425eb0d1943363251a7f7fbb578da280862b`, 47,917 text bytes. Print/web `pdftotext` byte-identical (47,917 B each). *(D5 rebuild, 2026-11-12; pre-D5 disk values in the D5 section at the end.)*
- Print PDF is ~the same size as the core's 25,311,626 bytes (not ~12.4 MB smaller like the Latin editions). Cause: the Japanese explanation layer embeds thousands of distinct CJK glyphs, just like the core's Chinese layer. All 5 images are byte-identical between core and ja (see §3).
- P8 answer font size measured: **10.125pt** — above the SOP §1.1 floor of 9.75pt (13.5 SVG units × 0.75 page scale; page 1462.5×2025 pt over 1950×2700 units). p8_keys_small is OFF for ja (13.5 units, line height 1.16 — the W46 pt-ja size, per the standing rule; transform.py only applies the small size when FURN p8_keys_small is set). P8 answer-region spans: min 10.125pt, 619 spans, 770 words. P8 answers flow ends at y=2504 (bottom 2560) — fits with 56px margin at the larger size; no note shortening was needed for ja.
- §1.1 spot checks (final SVGs): paper #fbfaf6 ×8, gold/brick-red/near-black 0, "double" 0, badge colours all three present (#37402f, #46581f in P1), VOL.4 ×9, VOL.5 ×3 (all inside the P7 disclosure / next-week text, allowed). P8 chips re-verified: Q113–120 all B1, Q145–149 all B1, Q150 B1 (exercise instance; the answers-flow duplicate "150. " token carries no chip, same as core). Writing title badge present ("H ESCREVA VOCÊ", bridge "作文の課題（正解は1つではありません）。模範文（88語）は下です。"). Simplified-only characters in the final SVGs: NONE (checked against a simplified-only set; the 1,588 CJK-range characters are Japanese kanji/kana plus the frozen logo `<title>Lucerna 三色蛾</title>` in P1, same as core — not Simplified Chinese text).
- All 8 cards visually inspected on the final render; full .text.md read through (534 lines); all 150 questions checked one by one (see below); full-text and 150-key review found zero issues at the final round. No SOP §8 independent second-person proofread — builder self-check only, reported as such. Independent proofreading is assigned separately by the coordinator.
- Self-check rounds: **round 1** (run1/render1/webpdf1: run RC=0, 0 overflow, gates 16/16, occlusion 1 flag — the core-carried LINEX only, after the transient self-test flake on the first occlusion run; final visual + text review) zero issues. First fan-out edition to ship clean in a single round since it, because the disclosure was pre-shortened to 3 lines, E1–E3 pre-measured at 2 lines each, the bridge pre-measured at 2 lines, and the numbers-box total line count pre-measured equal to en (10 lines) before the build, using the ru lessons.
- Fan-out defects found and fixed in this edition (same classes must be avoided in the other 2 languages):
  1. **Label trailing "！" — ja-specific.** transform.py does NO punctuation conversion for ja (PUNCT={}), so the SEG value for the label (key excludes the trailing "！") would have rendered with a full-width "！" ("…送ってください！"), while the W46 ja shipped label ends with "。" ("編集部の作例です。あなたの手紙を送ってください。"). Fix: an OVR entry for the WHOLE literal including "！" ("编辑部示例，非真实来信。真实来信请寄编辑部，下期见！") → "編集部の作例です。本物の手紙ではありません。あなたの手紙を送ってください。" — OVR is applied before SEG and consumes the "！". The SEG entry for the same text (without "！") stays in the table for key-equality but never matches after the OVR. OVR has 55 entries vs en's 54 for this reason.
  2. **P7 pre-measured, not repaired** — the Japanese disclosure is the W46 shipped form with VOL updates ("編集部注：VOL.3 で約束した実際の手紙と最優秀作文は締切までに届かず、本号は例文を掲載し、約束は VOL.5 へ延期します.", 3 lines by svglib wrap(), "sans", 19.5pt, CW−44=378.5); E3 was shortened from "パルメイラスはPK戦5–4で勝ち進みました。規定時間ではヴァスコが2–1で勝ちました" (3 lines) to "パルメイラスはPK戦5–4で勝ち進みました。ヴァスコは2–1で勝ちました" (2 lines); E1/E2/E4 each 2 lines; final p7_geo = pad 22, fy_gap 16, quote_step 80; last quote JA baseline 2351.17, ink bottom ~2356.2, clears the 2404 preview-box top by ~48px.
  3. **P8 bridge pre-measured (nl lesson applied)** — "作文の課題（正解は1つではありません）。模範文（88語）は下です。" is 2 lines at 20.5pt, CW=422.5. P8 exercise flow end y=908.62.
  4. **Numbers-box total pre-measured (ru lesson applied)** — the four ja box items in serif at 386.5: 20 (2) + 1695 (3) + 2023 (3) + 3 (2) = 10 lines, exactly en's total (3+2+2+3) — no P1 overflow. Note the item-by-item split differs (ja 1695 is 3 lines vs en 2; ja 20 is 2 vs en 3) — only the TOTAL matters for the flow.
  5. **No "?2文" merges, no paren-joins, no double "。", no simplified chars, no " :"** — the en/de/fr/es/it/nl/ru defect classes were checked up front for ja and are absent (full-sentence SEG keys for the 4 E VOCÊ prompts, with proper "…。2 文書いて送ってください。" forms; "（" is kept as full-width "（" in Japanese values — no conversion, no "( (" risk; SEG values ending in "。" were checked against doubling — none, because the "。" is inside the matched key; the OVR label is the only value ending in "。" whose key does not end in "。" and it consumes the trailing "！" via the OVR). Systematic scans re-run on the final SVGs: ?2文 0, ?Write 0, ".." (outside "...") 0, "( (" 0, " :" 0, simplified-only chars 0. The .text.md quote lines show "….(Página N)" with no space before "(" — identical to the core export and to the shipped fr .text.md (the build code adds the space in the SVG, the source export does not); not a defect.
  6. **P7 geometry rule (restated, verified again for ja)** — the gates' "P7 quotes clear of preview box" check is vacuous (it filters y<2404 then asserts max<2404, so a 4th quote row at 2409.67 passed unseen in es run1 while gates said max 2360.0). Enforce manually + occlusion + visual. P7 quote geometry: header at fy+3, PT rows at fy+66+(i·step), reader lines at +49.67; step 80 → JA→next-PT gap 30.33px; last-reader baseline must be < 2404 (ink bottom ~baseline+5 must clear 2404).
- Reproducibility: NOT re-checked for ja (de was verified 6/6 before run1; the ja tables were written fresh from the en keys — SEG key equality verified 220/220 programmatically before run1; OVR has 55 entries vs en's 54 — the extra one is the label whole-literal override, recorded above).
- 150-key review (final): P8 notes 150/150 in both core and ja; key-part diffs are only [137, 138] (above). Q131 = A in both (core D2 fix present). Q150 = '✓' in both (open writing task, model-text marker). All 150 answer keys verified against the questions and the reading texts; no key differs from core except the two translation answers (137/138), which are reader-language renderings of the same answers.
- Layout notes: P3/P5 word-list intro at the top of column 2 with the section header at the bottom of column 1, and P4 "B AS PALAVRAS" header orphan at the bottom of column 1, are core flow behavior, not defects. Japanese gloss style uses appositions ("o feriadão 3連休", "o agregado 合計スコア"). The P1 football text's 3rd line "em Brasília. (Página 4)" sits at baseline 2327.60 with the quiz rule at y=2312 — the 0.2px LINEX graze (see occlusion note above); visually clean in the card.

## 7. Reproduction

Build directory: this directory (copied from `production/2026-w47/core-pt/`, core untouched). Mechanism: `tables_ja.py` (SEG/OVR — SEG keys identical to tables_en.py: SEG 220, OVR 55 = en's 54 + the label whole-literal override, verified) + `furniture.py` FURN[ja] in the scratch dir `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-pt/`; `transform.py <edition_dir> ja` rewrites the explanation layer; `make_gates.py` adapts gates; then:

```
cd ~/workspace/weekly-git/production/2026-w47/2026-w47-pt-ja
cp ~/workspace/weekly-git/production/2026-w46/2026-w46-pt-ja/svglib.py svglib.py   # kinsoku — MUST overwrite the core copy BEFORE transform/run
~/workspace/weekly-git/tools/venv/bin/python -u run.py
~/workspace/weekly-git/tools/venv/bin/python -u gates.py
~/workspace/weekly-git/tools/venv/bin/python ../../../tools/occlusion_audit.py svg --json <scratch>/ja-occlusion1.json
~/workspace/weekly-git/tools/venv/bin/python ../../../tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150 --json <scratch>/ja-p8-extract.json
~/workspace/weekly-git/tools/venv/bin/python ../../../tools/p8.py compare --core-p8 ../core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150 --json <scratch>/ja-p8-compare.json
~/workspace/weekly-git/tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-pt-ja --core-svg production/2026-w47/2026-w47-pt-ja/svg --out <scratch>/ja-freeze1
~/workspace/weekly-git/tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg production/2026-w47/2026-w47-pt-ja/svg --json <scratch>/ja-freeze-diff1.json
~/workspace/weekly-git/tools/venv/bin/python -u render.py
~/workspace/weekly-git/tools/venv/bin/python -u tools/webpdf.py production/2026-w47/2026-w47-pt-ja/svg production/2026-w47/2026-w47-pt-ja/A-Lucerna-VOL4-web.pdf
```

render.py produces cards + print PDF only, not the web PDF. Web PDF only via tools/webpdf.py. After the core is finalised, never modify source files again; any change must re-run all gates and re-do the freeze baseline. Scratch files and run logs live in `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-pt/` (ja-*.log/json, run1/render1/webpdf1 logs). Render log redirect: write logs to scratch files, never to /tmp (a /tmp stop record was lost in a VM restart; disk records are authoritative).

## 8. .text.md note

`2026-w47-pt-ja.text.md` (534 lines) is exported from the build sources (content modules), ordered as printed (titles, paragraphs, columns, exercises 1–150 with answer hints, P8 answers as in-exercise answers + the full 150-answer summary), and checked line by line against the rendered text — never extracted back from the PDF. Mechanical checks: 50 lines changed vs core, 484 identical, simplified-only characters 0, question numbers 150/150, paren-joins 0, suspicious ".." (not part of "...") 0. (Japanese kanji/kana are CJK by Unicode range, so the check is simplified-only chars, not CJK 0.) Header lines: "# A Lucerna · ポルトガル語週刊 VOL.4", "2026年11月16日〜22日 · 本文はポルトガル語 · 解説は日本語 · レベルA2–B2 · 練習問題150問". For the site's single-issue page body and search (weekly repo AGENTS.md rules 4/9).

## Re-fanout (2026-11-11, core-pt fix2)

Full rebuild from the finalised core-pt (fix2, `d2b0e182`): the first-round
edition in this directory predated core fix1 (`4b688318`, box heights +
P8 `max_w=395`), so it was rebuilt from scratch, not patched. Driver:
`scratch-refanout-pt/build_edition.sh ja`, then `gates_pt.py ja --skip-render`.
Every step ran under `~/workspace/weekly-git/tools/venv/bin/python` —
Python 3.12.3, Pillow 13.0.0, FreeType 2.14.3 (bundled
`pillow.libs/libfreetype-57f805ba.so.6.20.6`), HarfBuzz bundled, raqm 0.11.0.
System python3 was NOT used.

New files (sha256):
- Print PDF `A-Lucerna-VOL4.pdf` 24,991,049 bytes
  `e45f4a9471d59a78e615cfd010679b7aff4dd963f092ab7457f6d8214fda8a08`
- Web PDF `A-Lucerna-VOL4-web.pdf` 1,680,796 bytes
  `ff67441e1c61e58b002b0a9c40711732512d089bde84aeadc57ff774778281e8`
- Text `2026-w47-pt-ja.text.md` 37,915 bytes, 535 lines
  `90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830`

Gates (all pass): edition `gates.py` 16/16; occlusion 0 flags (venv);
p8 extract 150/150, compare CLEAN (keydiff [137, 138] — expected, the
Q137/138 keys re-aim at Japanese); freeze baseline 8/8; creambox 0 spill;
boxtitle true-ink clear on all boxes; keycheck 149/150 (Q150 is the open
writing task, extracted as `✓`); sweep 0 bridge widows; print/web
`pdftotext` byte-identical (107,708 bytes); italic spans print 1 = web 1
(webpdf.py italic-face check); P8 min font 10.125pt (CJK floor, ≥ 9.75pt);
check_final word multiset diff 0.

D5 gloss (core fix2): core changed P4 gloss `o título 冠军` → `o título 冠军头衔`.
ja value `優勝/タイトル` (new SEG key `冠军头衔`; the old `冠军 → 優勝者`
mapping is untouched). PIL probe of the rendered P4 gloss box: 4 lines,
last line right clear +236.5px, bottom clear +42.7px, no overflow; rendered
`o título 優勝/タイトル`.

Kinsoku svglib: the edition's `svglib.py` is the W46 pt-ja kinsoku version
restored from the backup (md5 `f61efb1bdac0e1c0a38fc60b300f238e`), NOT the
core's (`4228b7e7fc52caaec9d690f614755b4a`). The build driver copies it
over the core's file before running transform. Verified by md5 after the
build.

Proof1 fixes carried in this rebuild: D4 `数字` → `数字` (P1 numbers-box
title — the value is now the single character, was `数字で見る`);
D5 SÁB 21 whole-sentence key — rendered `土曜日16:30、パルメイラス対フラメンゴ`
(previously `土曜日16日:30`); Q65 whole-sentence key (proof1 miss, same
class) — rendered `65. B — 2日目は自然科学と数学、13:30–18:30` (previously
`65. B — 2日目は自然科学と数学、13:30 18日まで:30`). The fragment keys
`周六 16` and `至 18` were deleted from the tables.

text.md changes vs the first-round file (2 lines): L215 D5 gloss
(`o título 優勝者` → `o título 優勝/タイトル`); L433 verbatim line →
`（本号の記事から一字一句）`.

Hand-patch inventory (`classify_pt.py ja`): 29 diffs vs the backed-up
first-round sources, ALL classified KEEP — core-fix1 lines + the numbers
title + the two whole-sentence keys + the D5 `優勝/タイトル` line.
(`svglib.py` shows no diff: backup and rebuild carry the same kinsoku
file.) 0 REVERT, 0 lost hand patches.

Also fixed in the mechanism (not a ja defect): a core-fix1 comment
(`墨底 +33` in content12.py:131) broke the transform's CJK-0 assertion
for every Latin edition; a SEG key `墨底` was added to all 10 tables
(ja value `インク下端`).

## D5 rebuild (2026-11-12; SOP §1.1: CJK-reader sans Latin/Digits → Newsreader, script-based routing per CJK-DECISION.md §1)

- Install: `apply_variant.py --target pt --reader ja` (mode cjk; installer also added the fix2 block — this edition's svglib had none; CJK index SC→JP, kinsoku already present). `route_assert.py` latin: FAILURES 0. svglib md5 `f61efb1b…` → `fb698ac3…`.
- Pre-D5 baseline (snapshot `scratch-d5-rebuild-pt/2026-w47-pt-ja/baseline/`): production census D5 Latin **347** (CENSUS FAIL); baseline gates occlusion/boxtitle/spill/edge all 0. Pre-D5 PDFs on disk: print `568eb36b19a0d285dfbb9058933659e3dd97afae0d5de535a5b47bb7906b6ea5` (24,991,052 B), web `b18b3df2a2daf3ddd878ebc95d2f30e2bab87d10ef4deb09a61a64da14851107` (1,680,799 B).
- NOTE on pre-D5 SHAs: the KIT §6 pre-D5 line recorded different values (`04f284ed…`, 24,992,044 B / `339d2b05…`, 1,644,666 B) — the on-disk PDFs were rebuilt after the KIT was written (same pattern as pt-fr's fix2 note and pt-nl); the snapshot file is authoritative for the pre-D5 disk state.
- Round 1 defects (all D5-caused, baseline 0):
  1. HEAD TOO WIDE ×1: P2-ex `C　COMPLETE COM OS NÚMEROS` 408.8→460.0px (+12.5%). Fix (text unchanged): P2-ex battery heads A–D uniform 25→22 (same as core-pt).
  2. Self-gates FAIL ×2 — D5 run-split measurement artifacts, not content loss (same class as core-pt): footer check (`1ページ（全8ページ）`) and P7 quotes check (two JA translations containing digits, `3日間` / `2–2`) failed only because D5 splits one source string into several `<text>` runs and `joined()` inserts a space at the split. Baseline gates.py passed pre-D5 (FAILURES: none); squashed (whitespace-folded) comparison on the D5 build passes footer 8/8 and both quotes; pdftotext still extracts `1ページ（全8ページ）`. Fix: `gates.py` gained `squashed()` (mirroring `gates_core.py`), used ONLY for the footer check and the P7 quotes check.
  3. No box-title overflow (boxtitle 0 DEFECT, creambox PASS in round 1): the JA subtitles are short enough that the widened Latin heads stayed inside.
- Gates round 2 (ALL-GREEN): run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE (head_check PASS); gates.py **16/16, FAILURES: none**; occlusion **0 flags**; p8 extract **150/150**, compare **CLEAN** keydiff=[137, 138] (expected reader-language keys); freeze baseline **8/8**; freeze-diff vs own baseline added CJK **0** (added Latin 228 = run split); spill **0**; boxtitle **0 DEFECT**; edge **0 TOUCH, 0 NEAR**; creambox (mechanism + tools) **PASS 0 defects** (n=396, median 1.04, bold 1.057; P8 222→222 lines, slack 41.0px); D5 census **PASS**; census_quotes **0 defective**; print/web text byte-identical (47,917 bytes; `-layout` 口径各 96,021 字符，字符多重集差 0).
- New SHAs: print `9208d231d66cf6e612f367cc1702c8003b5c1bcfd447da414dcedac5d8037768` (15,449,291 B); web `a9b4a30929c18cbd949062d1cf79425eb0d1943363251a7f7fbb578da280862b` (1,433,879 B). text.md unchanged (md5 `83035b2da702df00c6fc63510b38d64d`, = pre-D5).
- Text SHA-256: `2026-w47-pt-ja.text.md` 37,915 bytes, SHA-256 `90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830` (unchanged since Re-fanout — see that section).
- Files changed (not committed): `svglib.py` (D5 + fix2, CJK SC→JP), `content12.py` (battery heads 25→22), `gates.py` (`squashed()` measurement fix, no content change), `WEEKLY-KIT.md` (§6 + this section). Logs: `scratch-d5-rebuild-pt/2026-w47-pt-ja/` (baseline/, baseline-gates/, install.log, run/render/webpdf.log, gates-1/, gates-2/, freeze-baseline*.log).
