# Lucerna Weekly — Russian VOL.1 × Italian explanations — WEEKLY-KIT

> Edition: Russian target text (frozen VOL.1 core) + explanations fully in Italian,
> for Italian-speaking readers. Week: Mon 19 – Sun 25 Oct 2026 (2026-W43).
> Masthead: **Lucerna** (no article, exactly as the core ships).
> Build dir: `hidden_files/weekly-report-ru-it-build/` (copy of the core build).
> Status: builder's own full proofread DONE; **independent proofread DONE — PASS (§13)**.

## 1. Method

1. Copied the frozen core build to `weekly-report-ru-it-build/`; repointed its
   output paths to a build-local `baseline-out/`; ran it **unmodified**.
2. Baseline proof: all 8 regenerated SVGs are **byte-identical (sha256, 8/8)**
   to the shipped core SVGs (table in §2), and the registry rebuild matched the
   core exactly (150 exercises; A2 54 · B1 72 · B2 24; per-page
   10/18/18/18/18/18/12/38; model writing 82 words).
3. Rewrote ONLY the explanation layer into Italian by exact-substring
   replacement in the copied sources (~474 replacements): glosses, grammar
   notes, instructions, exercise apparatus, all P8 answer notes. The Russian
   target text, the images and all layout geometry are frozen. The explanation
   helper method is named `expl()` in this build.
4. Rebuilt with zero flow-overflow / head-too-wide warnings; rendered cards
   (1950×2700), print PDF and web PDF.
5. Full verification battery (§§4–11) on the final rendered artifacts.

## 2. Baseline proof — shipped core SVG sha256 (re-verified unchanged at the end)

| Page | sha256 |
|---|---|
| p1-pervaya.svg | c808a77d5696156dfc5b75bbb12abc3a9e5f47a83a553e3910869888be8fc865 |
| p2-zhizn.svg | e6040d06337bec9549cdebb989c4142451cd1cba1de17092d161467271addc0a |
| p3-kultura.svg | 21f0a9d716fac63c36065bfd1f10c932dddd2b36b5f2ccb7131c5c5dbcb60d0a |
| p4-sport.svg | 4d6fab86c99d34fe15337c0ae5b547e65aa5ea1b6b94f0dcab3afad5eccec604 |
| p5-molodezh.svg | 534284d6ccf7e401b6d470e67f5ba1ef2fcbbfaea0dd45e36b5224d1a468e498 |
| p6-razbor.svg | 48e6b85a7fb234d790a38f4d1f6644bc780ef8c1f536401f06dec369329a8199 |
| p7-yazyk.svg | 8f9e861823f946bafdd2f6e4e3b74bfa52f6e3d25f09779813d1dfff017f4311 |
| p8-test.svg | fa3f80efe79f72efc7544ac990ec229df1f10f5cd40a4c4dc57b4fa62dfaf39f |

The unmodified copy reproduced all 8 byte-identically (8/8) before any edit.
After all work, `sha256sum -c` against this table still returns OK ×8 — the
frozen core was never touched (the core build was never executed in place; its
registry reference dump ran from a scratch copy with repointed outputs).

## 3. Final deliverables (files/weekly-report-ru-it/)

| File | Bytes | sha256 |
|---|---|---|
| Lucerna-VOL1-IT.pdf (print) | 22,608,651 | 24c611ab11a53e1a99be03fa35dca615223255b77aaea794fcb0de8d3cca22f3 |
| Lucerna-VOL1-IT-web.pdf (web, < 10 MB ✓) | 3,650,021 | 3b38ff55b5f55ca2f8dc710a925882a88474a91000d9e0ca263a53911e778ea6 |
| svg/ ×8, cards/ ×8 (1950×2700) | — | — |

Both PDFs have 8 pages.

## 4. Exercise ledger — identical to the core

Total **150**. Levels: **A2 54 · B1 72 · B2 24**. Per page:
P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38.
Type names renamed to Italian, counts unchanged:

| Core type | Italian | n |
|---|---|---|
| 完成句子 | Completare | 54 |
| 单选 | Scelta multipla | 42 |
| 词汇配对 | Abbinamento | 20 |
| 完形单选 | Cloze | 13 |
| 造句 | Frasi | 12 |
| 句型转换 | Trasformazione | 4 |
| 翻译 | Traduzione | 4 |
| 写作 | Composizione | 1 |

Instructions: Completa · Forma la frase · Trasforma · Abbina · Scrivi ·
Traduci in italiano / Traduci in russo (by direction). Model writing (#150)
stays the frozen Russian text, 82 words, verified by the registry.

## 5. Key-diff registry — the ONLY answer-key differences vs the core

Derived by dumping both builds' registries and diffing all 150 items
(levels and page assignments identical for all 150). Exactly **3 keys differ**,
all in section E (translation), plus **2 stems re-aimed** whose keys stay
Russian by design:

| # | Core key | Italian-edition key | Why |
|---|---|---|---|
| 137 | 星期日中央陆军将对阵斯巴达克。 | Domenica il CSKA gioca contro lo Spartak. | Item is "translate into the reader's language"; stem (Russian) unchanged: «В воскресенье ЦСКА играет со „Спартаком".» |
| 138 | 预报员预报十月末有雨夹雪。 | I meteorologi promettono nevischio per fine ottobre. | Same; stem: «Синоптики обещают мокрый снег в конце октября.» |
| 150 | （开放题，范文如下） | (Domanda aperta — testo modello qui sotto) | Apparatus label of the open writing item; the model text itself is unchanged Russian. |

Stems re-aimed (keys unchanged, still Russian — the reader now translates
INTO Russian):

| # | Core stem (Russian) | Italian-edition stem (Italian) | Key (unchanged) |
|---|---|---|---|
| 139 | Каникулы начинаются в субботу: всего двенадцать дней. | Le vacanze iniziano sabato: dodici giorni in tutto. | В субботу начинаются каникулы — всего двенадцать дней. |
| 140 | Я поздравляю папу с Днём отца! | Faccio gli auguri a papà per la Festa del Papà! | Поздравляю папу с Днём отца! |

Both Italian keys were checked word-by-word against their Russian stems
(weekday, teams, «мокрый снег» = nevischio); both Italian stems were checked
against their Russian keys. All other 147 keys are identical to the core.

## 6. Answer notes

- 142 of 150 registry notes rewritten in Italian; the 8 unchanged notes are
  pure-Russian form notes carrying no explanation-language content
  (#17/#104 выпасть → выпадет, #35 учиться → учился, #36 написать → написал,
  #63 закончиться → закончился, #73 День бабушек и дедушек, #90 слушать →
  слушают, #110 обещать → обещают) — same treatment as the other fan-outs.
- **Printed-note set equality (gate):** the set of exercise numbers whose
  notes are printed on P8 was extracted from the RENDERED P8 SVGs of both
  editions: core = 150, this edition = 150, **sets equal by number** (the core
  prints all 150; so does this edition). Key presence on the page: 149/150 in
  both editions — #150 prints as "150. ✓ <note>" by design in both.
- Answer-key typography: a space before each note parenthesis; half-width
  parentheses only (zero full-width parentheses in the SVGs, verified).

## 7. Images — inherited from the core, all verified placed in the render

| Page | Image | Credit (as printed) | License |
|---|---|---|---|
| P1 | Yuon, «Зима. Ростов» | Картина: Константин Юон, «Зима. Ростов» — общественное достояние (Wikimedia Commons) | Public domain |
| P2 | Bentley snowflake microphoto | Фото: Уилсон Бентли — общественное достояние (Wikimedia Commons) | Public domain |
| P3 | Kiprensky, Pushkin portrait 1827 | Картина: Орест Кипренский, 1827 — общественное достояние (Wikimedia Commons) | Public domain |
| P3 | Bilibin, «Морозко» 1932 | Иллюстрация: Иван Билибин, 1932 — общественное достояние (Wikimedia Commons) | Public domain |
| P4 | Russia 1912 Olympic football squad | Фото: автор неизвестен, 1912 — общественное достояние (Wikimedia Commons) | Public domain |
| P5 | USDA pumpkin stall photo | Фото: Министерство сельского хозяйства США — общественное достояние | Public domain |
| P6 | Toxer427, autumn park path | Фото: Toxer427 — лицензия CC0 (Wikimedia Commons) | CC0 |

All 7 images confirmed present in the rendered cards during the visual pass
(§11). P6 also carries the issue's own calendar strip and the training-data
chart (УЧЕБНЫЕ ДАННЫЕ · Dati di esercitazione; values 34/28/22/16 = 100,
labelled as exercise data, not real statistics — in both languages).

## 8. Italian furniture (verbatim) + measured shortenings

Applied verbatim:

- P1 pairing badge (brick slot): «TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO —
  L'EDIZIONE PER I LETTORI ITALIANI»
- P1 strap line: «SETTIMANALE RUSSO · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ»
- Footers, all pages: «Lucerna · SETTIMANALE RUSSO VOL.1 · TESTI IN RUSSO ·
  SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»
- Gloss prefix: «Nota — »
- Masthead: «Lucerna» (no article), unchanged from the core.

Wording shortenings forced by real-font (PIL) ink measurements — wording
changed, geometry never changed; each recorded with its measurement:

| Element | First wording | Problem (measured) | Final wording | Final ink |
|---|---|---|---|---|
| P1 box title | НЕДЕЛЯ В ЦИФРАХ · La settimana in cifre | 482.0 px from x=545 → ends 1027.0, crosses its box's right border x=961 | НЕДЕЛЯ В ЦИФРАХ · In cifre | ends 875.9 ✓ |
| P1 contents title | В ЭТОМ НОМЕРЕ · In questo numero | ink right 1913.9 — past the box border 1885 and the inner frame 1910 | В ЭТОМ НОМЕРЕ · Sommario | ends 1829.3 ✓ |
| P1 word-of-week heading | СЛОВО НЕДЕЛИ · Parola della settimana | ink right 1903.6 — past the content edge 1885 | СЛОВО НЕДЕЛИ · La parola | ends 1761.1 ✓ |
| P1 word-of-week gloss | похолодает = farà più freddo, la temperatura scenderà. | wraps to 2 lines; line 2 (baseline 1856) is crossed by the section rule at y=1844 | похолодает = farà più freddo. | 1 line, 262.6 px ✓ (the temperature detail remains in the Russian definition line above) |
| P7 error-clinic note 4 | Genitivo dopo «с» (inizio): с первого октября. | wraps to 2 lines, pushing the whole right-column stack down 26.5 units so the readers'-letters note's line 2 (baseline 1699.03) collides with the phrases rule at y=1698 | Genitivo dopo «с»: с первого октября. | 1 line; stack back at the core's positions ✓ (the "beginning" nuance remains in the Russian clinic line above) |

## 9. Freeze verification (text diff vs the core)

Visible-text multiset diff per page between the shipped core SVGs and this
edition's SVGs: every removed/added element was reviewed line by line. All
differences are (a) explanation layer rewritten in Italian, (b) pairing
furniture (badge, footers, headings), or (c) the documented registry items of
§5. **Zero Russian target text changed.** After the §8 fixes, the diff was
re-run: the only deltas vs the pre-fix diff are the 5 fixed Italian strings.
Zero CJK characters and zero full-width punctuation in the final SVGs.

## 10. Calendar verification

Italian-language weekday claims checked against the real 2026 calendar
(TZ Europe/Rome): 2026-10-22 = Thursday （giovedì ✓), 2026-10-24 = Saturday
（sabato ✓), 2026-10-25 = Sunday （domenica ✓), 2026-10-31 = Saturday
（sabato ✓). The frozen Russian text's own date claims are the core's,
already verified in the core's own proofread loop.

## 11. Geometric occlusion audit (mandatory gate)

Script: `audit_ru_it.py` (build dir) — parses the SVGs in paint order with
real-font PIL glyph metrics; ink band = baseline −0.88em … +0.30em; flags
≥30% glyph coverage by later opaque shapes, footer-band intrusion (y>2580),
page-edge spill, line-through-ink crossings with line boxes expanded by half
the stroke width, and text ink straddling any stroked box border (either
direction, any paint order — the box-title class), plus a soft warning at the
content edge x=1885.

- **Positive control:** a synthetic SVG with 6 planted defects (cover, footer,
  edge, line-crossing, vertical straddle, horizontal straddle) — all 6 fire;
  2 clean texts unflagged. Control validated before use.
- **Core reference run:** the shipped core itself yields 4 flags (listed
  below) — the baseline for "no new flags".
- **This edition, first run:** 11 flags. 5 were real, Italian-introduced
  defects — all fixed by wording only (§8 table). P3/P4/P5/P6/P8: 0 flags.
- **Final run: 4 flags, all pixel-adjudicated NON-DEFECTS, 0 unresolved:**
  1. P1 'странице.' vs its box's bottom border (y=2304) — band-model flag;
     the card crop shows a visible gap between the descender and the border.
     The element is byte-identical in the frozen core.
  2. P2 'redazione.' vs its box's bottom border (1496.75) — measured glyph
     ink bottom = baseline+1 = 1493, i.e. 3.75 units clear; the crop confirms
     a visible gap. (The core's corresponding last line sits in the same
     design position.)
  3. P2 'Запомните пару…' strip line vs the rule at y=1804 — frozen Russian
     text at frozen core geometry; side-by-side crops of this edition and
     the core are indistinguishable: the hairline sits in the descender
     space exactly as the core ships, touching no glyph body.
  4. P2 match-set right column ends at ink x=1900.6 — soft warning only;
     the crop shows clear space before the frame line (1910). Frozen
     Russian text, identical in the core.

## 12. Builder's own proofread record

- Read all 8 rendered cards end-to-end; all Italian apparatus, glosses and
  notes read as natural Italian; exercise numbering continuous 1–150 with
  correct level chips; P8 key complete and flowing within the page (answer
  columns end above the footer rule).
- Re-derived keys from the registry diff (§5): 147/150 keys identical to the
  core; the 3 differences are exactly the documented translation/apparatus
  items; #139/#140 keys verified Russian with Italian stems printed.
- P7 phrases: all 8 phrases are verbatim contiguous excerpts of this issue's
  articles with correct page tags — each occurs exactly **2×** in the full
  issue text (article + phrases page), verified programmatically on the
  final SVGs.
- Totals/levels re-counted from the final build's registry: 150;
  A2 54 · B1 72 · B2 24; per-page 10/18/18/18/18/18/12/38 — equal to the core.
- VOL.2 promises printed in the core (derby result, real first snow,
  Grandparents Day 28 Oct, Halloween 31 Oct, holidays start, real readers'
  letters) are inherited unchanged with the frozen Russian text.

**Independent proofread: DONE — PASS, zero problems (§13).**

## 13. Independent proofread record — PASS (zero problems)

Independent proofreader, fresh pass on the final rendered artifacts; no builder
claim taken on trust. Scratch: `hidden_files/proof-ruit-independent/`.
No fixes were needed; nothing was re-rendered; the shipped artifacts are
exactly what was proofread.

1. **Baseline (independently reproduced).** A scratch copy of the unmodified
   core build, output paths repointed to scratch, reproduced all 8 shipped
   core SVGs **byte-identically (8/8)** against the §2 hash table; the copied
   IT build likewise reproduces all 8 shipped edition SVGs byte-identically
   (8/8). Core hashes re-verified unchanged after all proofread work (8/8).
2. **Freeze diff.** Visible-text multiset diff per page, reviewed line by
   line: every difference is (a) explanation layer rewritten in Italian,
   (b) pairing furniture (badge, footers, bilingual headings), or (c) the
   documented registry items of §5. **Zero Russian target text changed.**
   Zero CJK characters and zero full-width punctuation in the final SVGs.
3. **Keys (own registry dumps of both builds).** Page/level identical for
   all 150. Key diff = **exactly {137, 138, 150}**: #137 «Domenica il CSKA
   gioca contro lo Spartak.», #138 «I meteorologi promettono nevischio per
   fine ottobre.» — both read on the printed page against their Russian
   stems («В воскресенье ЦСКА играет со „Спартаком".» / «Синоптики обещают
   мокрый снег в конце октября.») and faithful; #150 apparatus in Italian.
   Stems #139/#140 printed in Italian («Traduci in russo») with keys
   byte-identical to the core. Notes: 142 rewritten in Italian; the 8
   unchanged are exactly {#17, #35, #36, #63, #73, #90, #104, #110}, all
   pure-Russian form notes — as claimed.
4. **Printed-note set equality (decisive).** Parsed from the shipped P8
   SVGs of both editions: core printed set = {1..150}, this edition =
   {1..150} — **EQUAL by number**. Printed answers match the registry for
   all 150 entries in this edition (the core matches its own registry too;
   its single parser delta is a line-wrap space inside one Chinese note).
5. **Totals.** 150 exercises; A2 54 · B1 72 · B2 24; per page
   10/18/18/18/18/18/12/38; numbering continuous 1–150; writing model
   82 words — all equal to the core.
6. **P7 phrases.** All 8 Russian phrases and their (Страница N) tags are
   byte-identical to the core's (none appears in the freeze diff); only the
   translations changed (Chinese → Italian). The phrases are the core's own
   lightly condensed form of its article sentences (e.g. P4's), inherited
   unchanged, exactly as shipped in the core; translations verified
   faithful and natural.
7. **Calendar (own `date` run, Europe/Rome).** Every Italian weekday claim
   verified: 22 Oct Thu («Il 22 è giovedì», films «da giovedì»), 24 Oct Sat
   (vacations begin), 25 Oct Sun (derby), 31 Oct Sat (Halloween), 23 Oct Fri
   (round 12 opens, last school day), 21 Oct Wed (forecast snow), 19 Oct Mon
   (Lyceum Day), 18 Oct Sun = third Sunday (Father's Day); P6 calendar
   strip weekday letters all correct through 4 Nov (Wed); 1811 → 215 years
   arithmetic correct; chart 34+28+22+16 = 100, labelled exercise data in
   both languages.
8. **Furniture.** Badge, strap, footers («Lucerna · SETTIMANALE RUSSO
   VOL.1 · TESTI IN RUSSO · SPIEGAZIONI IN ITALIANO» / «Pagina N di 8»),
   gloss prefix «Nota — » and masthead «Lucerna» all verbatim as claimed.
   The 5 §8 shortenings verified in the render and by measurement: the three
   P1 titles end at x = 875.9 / 1829.3 / 1761.1, inside their bounds; the
   word-of-week gloss «похолодает = farà più freddo.» is one line; the P7
   clinic note 4 «Genitivo dopo «с»: с первого октября.» is one line and
   the right-column stack is back at the core's positions.
9. **Geometric occlusion audit (own implementation).** Paint-order parse,
   PIL real-font ink boxes (SC index, band −0.88em/+0.30em), line boxes
   expanded by half stroke width; synthetic positive control fired all 6
   planted classes (COVER/LINEX/FOOTER/EDGE/STRADDLE-H/STRADDLE-V) and
   left clean text unflagged — validated before the real run. Edition and
   core produce the same flag structure: footer self-flags on all pages
   (the footers themselves, identical in both — design, not defects) plus:
   - P1 «странице.» vs box bottom border (y=2304): element byte-identical
     in the frozen core; pixel rows identical in both cards; descender tip
     ends one row above the border — NON-DEFECT (inherited).
   - P2 «Запомните пару…» strip vs rule y=1804: glyph descenders end at
     row 1802, the rule occupies 1803–1805; pixel distributions identical
     in both editions — NON-DEFECT (inherited).
   - P2 «redazione.» (the one edition-specific flag): rendered ink ends at
     row 1490, box border at 1496.75 — ≥6 rows clear — NON-DEFECT.
   - Soft model note: two frozen Russian lines have advance-width ink
     models past x=1885 (P1 sidebar line to 1894.9; P2 match line
     «c. так поздравляют первого января» to 1900.6, the builder's flag 4);
     rendered ink ends at x=1892 (P1, identical in the core) and x=1901
     (P2), both inside the inner frame (1910) — NON-DEFECTS.
   No COVER, no EDGE, no FOOTER intrusions by body text; **0 unresolved
   flags; no new flags vs the core.**
10. **Images & credits.** All 7 image payloads byte-identical to the core
    per page (P1×1, P2×1, P3×2, P4×1, P5×1, P6×1); every printed credit
    matches a placed image and the §7 table (Yuon PD, Bentley PD,
    Kiprensky PD, Bilibin PD, 1912 squad PD, USDA PD, Toxer427 CC0).
11. **Banned-term scan.** The banned intermediary-layer term: **0
    occurrences** (both language forms) in the paper, this KIT, and the
    operative build code.
12. **PDFs (measured by the proofreader).** Web PDF **3,650,021 B**,
    sha256 `3b38ff55b5f55ca2f8dc710a925882a88474a91000d9e0ca263a53911e778ea6`
    (< 10 MB ✓), 8 pages; print PDF **22,608,651 B**, sha256
    `24c611ab11a53e1a99be03fa35dca615223255b77aaea794fcb0de8d3cca22f3`,
    8 pages — both exactly as the builder claimed. All 8 cards are
    1950×2700 and were viewed end-to-end: Italian apparatus natural
    throughout, no residual Chinese, no overflow.

**Verdict: PASS — one complete independent pass, zero problems. The
edition is final and cleared for repo insertion with the pins in item 12.**

## 14. D5 rebuild (2026-11-14)

D5 + §1.1 合并重建（2026-11-14；builder v3 接替 v2，v2 死于 2026-11-14 ~02:55 UTC 第 5 波 restart drain）。本节 supersedes 上述旧印/网 pin 行（以实测发运值为准；KIT 旧 SHA 不可作基线）。

- 装机：`apply_variant.py --patch-core ru --week 2026-w43`（core-ru `_D5_READER = "latin"`，+263/−28）+ 本版 `apply_variant.py --svglib patched/2026-w43-ru-it/svglib.py --target ru --reader it --week 2026-w43`（`_D5_READER = "latin"`，diff +63/−2）；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2 保留。
- 基线：run TOTAL 150，0 警告；印 PDF 22,257,214 B（MANIFEST +0.001%），网 PDF 2,331,826 B，`pdf_text_diff_ru.py` + TRIM_ARGS → IDENTICAL；修前普查 D5 拉丁 454、西里尔 0。
- 缺陷与修法（只动字号/断行与规则线位置，不动文字）：
- D2 (occlusion TEXTX, P1): `'A2' overlaps 'кино' 7.4×11.2px` — `content12.py:103` 目录标题 20→19pt。
- D3 (occlusion LINEX P2 ×6, 基线同款): `content12.py:232` 规则线 `ey−12`→`ey−8`。
- 门禁（run2）：全套 17 门 ALL-GREEN。run TOTAL 150；head_check 0；d5 census 拉丁/西里尔/弯引号在 CJK 均 0（弯引号总数 0；`noto_sans_elements=411`）；freeze baseline 8/8；freeze diff 新增 CJK 0、新增拉丁 strings 153（run 拆分）；spill 0（173 OBSERVE）；boxtitle 0 DEFECT（58 titles, 716 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=408, median 1.021；P8 208→208 行，slack 44.5→44.5px）；文字层 print=web 差 0（40,410 字）；text.md BYTE-IDENTICAL；census_quotes 0 defective；p8 compare CLEAN，keydiff=[137, 138]；刊头标语→日期间距 279.2px PASS。日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-it/GATES-SUMMARY-run2.txt`。
- 新交付物（实测）：印 PDF `Lucerna-VOL1-ru-it.pdf` **21,910,845 B**，sha256 `4697e0e4a1014d46572c5a3c63d7ffd4db9f48544df3cc94695cbe387dabf6df`；网 PDF `2026-w43-ru-it.web.pdf` **2,285,122 B**，sha256 `30176f1b9fc9ea03e3e183ac841e22cb1bf1a3bf81b80d9f63616f539ca85fb6`；text.md **60,839 B**，sha256 `919bee16aa994b6442972a3bf1fba19e4bb9f3798f68a2db622ce56d9bad38fd`，与 fanout `.text.md.new` BYTE-IDENTICAL。D5 报告：`production/notes/2026-w43/g-ru/scratch-d5-rebuild-ru/D5-REPORT-2026-w43-ru-it.md`。本版 pin 此前只在独立校对记录（§13）中以实测值出现（印 22,608,651 B / 网 3,650,021 B）；该记录为历史实测，不改；新 pin 只记于本节。
