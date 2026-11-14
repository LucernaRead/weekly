# WEEKLY-KIT — The Lucerna Weekly VOL.1 · RU × NL (Russian text, Dutch explanations)

Edition: Russian target text (frozen VOL.1 core, files/weekly-report-ru-vol1/) with the
complete explanation layer rewritten in Dutch for Dutch-speaking readers.
Build code: hidden_files/weekly-report-ru-nl-build/ (copied from the core build).
Russian text, images, page geometry: frozen. Pages: 8 (1950×2700), multiple-of-4 rule kept.
**Proofread status: PASS (independent proofread, one complete pass, zero problems — see §8).**

## 1. Baseline fidelity proof (fan-out method step 1)

The core build was copied to hidden_files/weekly-report-ru-nl-build/ and, before any edit,
`tools/freeze.py baseline` reproduced all 8 shipped core SVGs byte-identically (8/8):

| page | sha256 (baseline reproduction = shipped core) |
|---|---|
| p1-pervaya | c808a77d5696156dfc5b75bbb12abc3a9e5f47a83a553e3910869888be8fc865 |
| p2-zhizn | e6040d06337bec9549cdebb989c4142451cd1cba1de17092d161467271addc0a |
| p3-kultura | 21f0a9d716fac63c36065bfd1f10c932dddd2b36b5f2ccb7131c5c5dbcb60d0a |
| p4-sport | 4d6fab86c99d34fe15337c0ae5b547e65aa5ea1b6b94f0dcab3afad5eccec604 |
| p5-molodezh | 534284d6ccf7e401b6d470e67f5ba1ef2fcbbfaea0dd45e36b5224d1a468e498 |
| p6-razbor | 48e6b85a7fb234d790a38f4d1f6644bc780ef8c1f536401f06dec369329a8199 |
| p7-yazyk | 8f9e861823f946bafdd2f6e4e3b74bfa52f6e3d25f09779813d1dfff017f4311 |
| p8-test | fa3f80efe79f72efc7544ac990ec229df1f10f5cd40a4c4dc57b4fa62dfaf39f |

After all work, the baseline was re-run against the pristine core build
(hidden_files/weekly-report-ru-build): 8/8 again, core integrity re-verified — the
shipped core SVGs are unchanged (hashes identical to the table above).

Transform method: a count-asserted literal replacement script
(build dir `scratch/transform.py`, ~250 asserted replacements). The core's original
explanation strings appear in that script only as search patterns; this is the
disclosed scratch exception. The explanation helper method was renamed to `expl()`
in bslib4 and at all 19 call sites; the intermediary-layer term (either form) occurs
0 times in the paper, this KIT and the operative code.

## 2. Totals (this edition, from the final build log)

- Exercises: **150** — A2 54 · B1 72 · B2 24 (identical to core).
- Per page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38 (identical to core).
- By type (Dutch type names): Voltooi de zin 54 · Meerkeuze 42 · Woorden koppelen 20 ·
  Zinnen bouwen 12 · Zinsomvorming 4 · Cloze-meerkeuze 13 · Vertaling 4 · Schrijven 1.
- Writing model (#150): 82 words (registry-counted), frozen Russian, unchanged.
- Registry meta diff vs core (page, level per item): zero mismatches.

## 3. Key-diff registry (complete — derived by dumping both registries and diffing)

Keys differ from the core in exactly **3** items; stems re-aimed in exactly **2**;
all other 145 keys and 148 stems are byte-identical to the core (machine-verified).

| # | kind | core | this edition (NL) |
|---|---|---|---|
| 137 | key | 星期日中央陆军将对阵斯巴达克。 | Op zondag speelt CSKA tegen «Спартак». (note: Zie pagina 4; instr: Vertaal naar het Nederlands) |
| 138 | key | 预报员预报十月末有雨夹雪。 | De meteorologen beloven natte sneeuw voor eind oktober. (note keeps «мокрый снег = natte sneeuw»; instr: Vertaal naar het Nederlands) |
| 139 | stem | 星期六开始放假，一共十二天。→ ___ | De vakantie begint op zaterdag — twaalf dagen in totaal. → ___ (key unchanged Russian «В субботу начинаются каникулы — всего двенадцать дней.»; note: let op de naamval: двенадцать дней; instr: Vertaal naar het Russisch) |
| 140 | stem | 我祝爸爸父亲节快乐！→ ___ | Ik feliciteer papa met Vaderdag! → ___ (key unchanged «Поздравляю папу с Днём отца!»; note: поздравляю + с + instrumentalis; instr: Vertaal naar het Russisch) |
| 150 | key (writing apparatus) | （开放题，范文如下） | (open vraag — de voorbeeldtekst staat hieronder) (note: De voorbeeldtekst staat in deel H van deze pagina (82 woorden); instr: Schrijf; type: Schrijven) |

Notes rewritten in Dutch: **142 of 150**. The 8 notes byte-identical to the core are
pure-Russian form notes, language-independent, kept as printed by the core (same set as
the RU×PT sibling edition): #17/#104 «выпасть → выпадет», #35 «учиться → учился»,
#36 «написать → написал», #63 «закончиться → закончился», #73 «День бабушек и дедушек»,
#90 «слушать → слушают», #110 «обещать → обещают».

Renderer note (inherited core behaviour, identical in the sibling editions): inside P8
answer-key lines the typesetter drops «» pairs that directly wrap a single cited word
inside a note (e.g. a note drafted as «с» + instrumental prints as «с + instrumentalis» —
compare the core's own print). Not an edition defect.

## 4. Furniture (as shipped, verified on the final SVGs)

- P1 badge (tagline slot, y=372, 20pt bold brick):
  «TEKSTEN IN HET RUSSISCH · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS»
- P1 strap centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · ELKE WEEK · HET RUSSISCH DAT DE RUSSEN LEZEN»
- P1 subtitle: «RUSSISCH WEEKBLAD · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ»
- Footers (all 8 pages): «Lucerna · RUSSISCH WEEKBLAD VOL.1 · TEKSTEN IN HET RUSSISCH ·
  UITLEG IN HET NEDERLANDS» / «Pagina N van 8» (adjective uninflected, NL column rule).
- Gloss prefix: «Uitleg — » (gloss boxes and the P1 explanation line).
- P8 answer style: the core's own dash style `N. key — note`, answer-generation code
  byte-identical; P8 separators «— Pagina N —» for N = 1..8.

## 5. Mechanical gates (tools/, final artifacts)

- `freeze.py diff` core vs edition: added CJK = 0 on all 8 pages; edition CJK total = 0
  (Chinese explanation layer fully removed). Every removed string classified:
  explanation layer / pairing furniture only; no Russian text lost.
- `p8.py compare`: **CLEAN** — core 150 noted = edition 150 noted, sets EQUAL {1..150}.
  Its keydiff list [54, 137, 138]: #137/#138 are the registered key changes; #54 is an
  extractor artefact — the printed line reads «54. третий — derde plaats: третий
  (mannelijk, nominatief)» in this edition vs the core's Chinese note; the key «третий»
  is byte-identical (registry diff, §3, is authoritative: exactly {137, 138, 150}).
- `occlusion_audit.py` (selftest passed): edition 3 flags, core 2 flags, NEW vs core = 1:
  - NEW LINEX p1 «daalt.» — pixel-adjudicated **NON-DEFECT**: the word-of-week Dutch
    line's last ink row is 1842; the rule rows 1843–1844 contain zero dark pixels in the
    text's x-range (the same adjacency pattern adjudicated non-defect on the EN core).
  - Inherited from the core (identical frozen Russian text and geometry, flagged on the
    core itself): LINEX p2 (frozen Russian mnemonic paragraph vs the weather-strip
    rule) and BOXTITLE p1 «странице.» (КОРОТКО box, bottom ink 2305.6 vs border 2304.0,
    a 1.6-unit graze present byte-identically in the core). Registered as inherited,
    not edition defects; the Russian text was not touched.
  - 0 unresolved NEW defects.
- P7 phrases: all 8 quotes verbatim the core's, page tags identical and in the core's
  order (1, 2, 2, 3, 3, 4, 5, 6); whole-issue occurrence counts equal to the core's
  per phrase (1, 1, 1, 2, 1, 1, 1, 1).
- Images: embedded image data byte-identical to the core on every page
  (p1 ×1, p2 ×1, p3 ×2, p4 ×1, p5 ×1, p6 ×1). Credits (frozen Russian caption lines,
  per assets/CREDITS.md): Юон «Зима. Ростов» PD; Бентли snowflake PD; Кипренский
  Pushkin portrait 1827 PD; Билибин «Морозко» 1932 PD; 1912 football photo PD;
  USDA pumpkins PD; Toxer427 autumn path CC0.
- Calendar: every weekday/date claim verified against the real 2026 calendar
  (Europe/Moscow): Sun 18 Oct (Father's Day, 3rd Sunday), Mon 19 Oct, Wed 21 / Thu 22 /
  Fri 23 Oct, Sat 24 Oct (holidays start), Sun 25 Oct (derby 16:00), Mon 26 Oct –
  Tue 3 Nov (ministry recommendation, 9 days), Wed 28 Oct, Sat 31 Oct, Wed 4 Nov
  (Unity Day) — holidays 24 Oct – 4 Nov = 12 days. All correct.
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings; all flow end positions
  within their bottoms (P6-ex ends y=2366 = the core's own value).

## 6. Defects found by the builder's own pass and fixed (explanation layer only)

1. **P6 exercise flow overflow** (first render): flow ended y=2594 > bottom 2580 —
   the Dutch section instruction lines were longer than the Chinese ones. They were shortened
   («Kijk naar de kalender en de grafiek.» / «Voeg de twee zinnen samen.»);
   final P6-ex end y=2366, exactly the core's value.
2. **P1 box title too wide** (occlusion audit BOXTITLE): «НЕДЕЛЯ В ЦИФРАХ · De week in
   cijfers» ink to x=994 crossed the box border 961. Shortened to
   «НЕДЕЛЯ В ЦИФРАХ · In cijfers» (same solution as the ES×NL CIFRAS title).
3. **P7 col-3 stack overran the phrases rule** (occlusion audit LINEX): the Dutch
   word-box line (3 wraps vs the core's 2) and the Dutch reader-letter note (3 wraps
   vs 2) pushed the letter box bottom to 1740.96, across the full-width rule at
   y=1698. Both lines shortened («единоличный лидер = het team dat alleen aan kop
   staat.»; letter note «Redactievoorbeeld. In VOL.2 echte brieven en de beste teksten
   van pagina 8!»); final col-3 bottom = 1682.96, exactly the core's value, and the
   VOL.2 promise (real letters + best page-8 texts) is kept verbatim in substance.

## 7. Deliverables & PDF pins (measured on disk)

- files/weekly-report-ru-nl/ — svg ×8, cards ×8, WEEKLY-KIT.md (this file).
- Print PDF `Lucerna-VOL1-NL.pdf`: **21,910,121 B** (D5 rebuild 2026-11-14; D5 前 22,609,562 B), sha256
  8b22336723990a6ca947a05e10cd9b730038f74da1b65bece7102ef2fa525712
- Web PDF `Lucerna-VOL1-NL-web.pdf`: **2,284,380 B** (< 10 MB) (D5 前 3,655,800 B), sha256
  79207a11d7ed351ef802ac38220f566924cc2a555951e230a7a0630805cc8d93

No repo insert, no Discord — per scope. Next step: independent proofread, then
insert via tools/insert.py (slug 2026-w43-ru-nl, discordThread = Russian thread).

## 8. Independent proofread record (2026-10-21)

**Verdict: PASS — one complete independent pass, zero problems. No fixes, no re-render.**
Scratch: hidden_files/proof-ru-nl/scratch/ (registry dumps reg-core.json / reg-nl.json /
reg-pt.json, freeze-diff.json, p8-compare.json, occlusion.json, per-page text dumps).

- **freeze.py baseline**: pristine core build reproduces the shipped core **8/8
  byte-identical**, run at the start AND re-run as the closing step; core SVG sha256
  set identical to the §1 table before/after — frozen core untouched.
- **freeze.py diff**: added CJK = 0 on all 8 pages; edition CJK total = 0. Every
  Cyrillic-bearing added/removed string personally classified: bilingual furniture
  titles (ZH→NL), gloss lines (Russian citations kept, explanation ZH→NL), P7 Dutch
  translations replacing the Chinese ones, P8 answer lines (Russian key identical,
  note ZH→NL). No Russian body text added, removed or count-changed.
- **Registry re-dump (both builds, one process each)**: 150 = 150; page/level meta
  zero diffs (A2 54 · B1 72 · B2 24; per page 10/18/18/18/18/18/12/38); type diffs are
  exactly the ZH→NL type-name translations with identical per-type counts. **Key
  diffs exactly {137, 138, 150}** with the §3 values; stems {139, 140} verified in
  the printed P8 (Dutch stems present, Chinese stems absent, Russian keys unchanged).
  Notes: 142 rewritten in Dutch; the 8 byte-identical notes are exactly
  {17, 35, 36, 63, 73, 90, 104, 110} — independently confirmed to be the SAME set as
  RU×PT (whose registry was also dumped: identical-notes set and key-diff set both
  match). #142 and #150 notes are Dutch as registered.
- **All 150 keys re-derived by hand from the Russian text** (full per-page reads of
  the shipped SVGs): 150/150 correct, including P4 table arithmetic (25/24/23),
  P6 chart (34+28+22+16 = 100; bar label positions equally spaced per 6% step =
  proportional), the P6 day-by-day strip's weekday letters vs the real calendar,
  and the P8 reading passage (Антон) answers.
- **p8.py compare** (independent re-run): **CLEAN** — core 150 noted = edition 150
  noted, sets EQUAL {1..150}, keydiff [54, 137, 138]. #54 artefact confirmed in the
  SVG: «54. третий — derde plaats: третий (mannelijk, nominatief)», key «третий»
  byte-identical.
- **occlusion_audit.py** (selftest passed): edition 3 flags, core 2, NEW = 1 —
  identical to the builder's report. Pixel adjudications:
  - NEW P1 LINEX «daalt.»: **NON-DEFECT** — on the final card, rows 1843–1844 (the
    rule band) carry dark pixels only at the page frame (x 26–29, 1920–1923), zero
    in the text's x-range; the gloss line's last ink is row 1842, the next line's
    ink starts row 1845. Same adjacency pattern as the adjudicated EN core.
  - Inherited P2 LINEX and P1 КОРОТКО BOXTITLE (1.6-unit graze): the flagged text
    elements are byte-identical between core and edition (full element lists
    compared); both flags fire on the core itself. Frozen inheritance, not defects.
  - Builder's 3 fixes pixel/geometry-verified: P6 flow end y=2366 in BOTH builds'
    fresh run logs (= core value); P1 numbers-box title «НЕДЕЛЯ В ЦИФРАХ · In
    cijfers» true ink x 547–893, inside the box border 961; P7 col-3 letter box
    bottom 1682.96 in both editions, 15 units clear of the phrases rule at 1698,
    VOL.2 promise («Redactievoorbeeld. In VOL.2 echte brieven en de beste teksten
    van pagina 8!») present in full.
- **Furniture**: badge on P1; footers + «Pagina N van 8» correct on all 8 pages;
  «Uitleg — » gloss prefix in place; P8 separators «— Pagina 1..8 —» all present;
  P8 dash style confirmed in print.
- **P7**: 8 quotes verbatim (full-string matches), page-tag sequence (1,2,2,3,3,4,5,6)
  identical, whole-issue occurrence counts (1,1,1,2,1,1,1,1) identical in both editions.
- **Calendar** (Europe/Moscow, `date`-verified): 18 Oct 2026 = Sunday = 3rd Sunday
  of October (Father's Day); holidays Sat 24 Oct – Wed 4 Nov = 12 days (Unity Day);
  ministry Mon 26 Oct – Tue 3 Nov = 9 days; derby Sun 25 Oct; 19 Mon / 21 Wed /
  22 Thu / 23 Fri / 28 Wed / 31 Sat all correct. P1 «215 лет» (2026−1811) correct.
- **Images & credits**: embedded image data byte-identical per page (p1×1, p2×1,
  p3×2, p4×1, p5×1, p6×1); all 9 credit lines byte-identical to the core and
  matching assets/CREDITS.md (all PD/CC0). Cards 8× 1950×2700.
- **Banned intermediary term**: 0 in final SVGs, this KIT and operative code;
  occurrences confined to scratch/transform.py as rename search patterns
  («def bridge(» → «def expl(», «.bridge(» → «.expl(» ×20 call sites) — the
  disclosed exception, confirmed in scope. `expl()` rename verified in code.
- **Content scope**: Dutch layer introduces no international politics; all content
  is the frozen core's Russian domestic-life material with translated explanations.
- **Final PDF pins (measured on disk, identical to §7)**: web
  `Lucerna-VOL1-NL-web.pdf` **3,655,800 B** / sha256
  d82f711e7b51e36172a68a59e60e38f98d23e8fc926d75feb93eb7d22174b43a (< 10 MB);
  print `Lucerna-VOL1-NL.pdf` **22,609,562 B** / sha256
  a0c01319a7916f89813e4edce69ae20830af10722fe2c60898477cd7d4fb42bf
  (print size inherited from the core's image sources; recorded, not treated).

Ready for repo insert via tools/insert.py (slug 2026-w43-ru-nl).

## 9. D5 rebuild (2026-11-14)

D5 + §1.1 合并重建（2026-11-14；builder v3 接替 v2，v2 死于 2026-11-14 ~02:55 UTC 第 5 波 restart drain）。本节 supersedes 上述旧印/网 pin 行（以实测发运值为准；KIT 旧 SHA 不可作基线）。

- 装机：`apply_variant.py --patch-core ru --week 2026-w43`（core-ru `_D5_READER = "latin"`，+263/−28）+ 本版 `apply_variant.py --svglib patched/2026-w43-ru-nl/svglib.py --target ru --reader nl --week 2026-w43`（`_D5_READER = "latin"`，diff +63/−2）；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2 保留。
- 基线：run TOTAL 150，0 警告；印 PDF 22,257,842 B（MANIFEST +0.001%），网 PDF 2,331,803 B，`pdf_text_diff_ru.py` + TRIM_ARGS → IDENTICAL；修前普查 D5 拉丁 461、西里尔 0。
- 缺陷与修法（只动字号/断行与规则线位置，不动文字）：
- D2 (occlusion TEXTX, P1): `'A2' overlaps 'кино' 7.4×11.2px` — `content12.py:103` 目录标题 20→19pt。
- D3 (occlusion LINEX P2 ×6, 基线同款): `content12.py:232` 规则线 `ey−12`→`ey−8`。
- D5 (occlusion LINEX P7, D5 新增, run2 新发现): 纠错栏第 4 条荷兰语注 19.5pt 绕 2 行，`eh` +26.52px — `content7.py:70` `eh` wrap 与 `:78` p.para 两处同改，19.5→19pt。
- D6 (occlusion LINEX P1, 基线同款, run2 新发现): 每周一词释义第 2 行 `temperatuur daalt.` 下行字母触 row-B 分隔线 y=1844 — `content12.py:116` 分隔线 1844→1848。
- 门禁（run3）：全套 17 门 ALL-GREEN。run TOTAL 150；head_check 0；d5 census 拉丁/西里尔/弯引号在 CJK 均 0（弯引号总数 0；`noto_sans_elements=404`）；freeze baseline 8/8；freeze diff 新增 CJK 0、新增拉丁 strings 148（run 拆分）；spill 0（174 OBSERVE）；boxtitle 0 DEFECT（58 titles, 715 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=404, median 1.019；P8 241→241 行，slack 44.5→44.5px）；文字层 print=web 差 0（40,169 字）；text.md BYTE-IDENTICAL；census_quotes 0 defective；p8 compare CLEAN，keydiff=[137, 138]；刊头标语→日期间距 282.9px PASS。日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-nl/GATES-SUMMARY-run3.txt`。
- 新交付物（实测）：印 PDF `Lucerna-VOL1-ru-nl.pdf` **21,910,121 B**，sha256 `8b22336723990a6ca947a05e10cd9b730038f74da1b65bece7102ef2fa525712`；网 PDF `2026-w43-ru-nl.web.pdf` **2,284,380 B**，sha256 `79207a11d7ed351ef802ac38220f566924cc2a555951e230a7a0630805cc8d93`；text.md **61,077 B**，sha256 `96a8fbbe4457ad147bf38770c668e7669c01ed34a70425cf6f7262a429d2cf13`，与 fanout `.text.md.new` BYTE-IDENTICAL。D5 报告：`production/notes/2026-w43/g-ru/scratch-d5-rebuild-ru/D5-REPORT-2026-w43-ru-nl.md`。§8 独立校对记录重复引用的旧 pin（印 22,609,562 B / 网 3,655,800 B）为 D5 前实测值，系历史记录，不改。
