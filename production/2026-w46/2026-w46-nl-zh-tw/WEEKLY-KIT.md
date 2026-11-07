# WEEKLY-KIT — De Lucerna · 荷語週報 VOL.3 · NL × ZH-TW

Edition slug: `2026-w46-nl-zh-tw`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Traditional Chinese (Taiwan/Hong Kong usage), written natively — Simplified
and Traditional Chinese are independent editions, never converted from one
another. Built by the W46 NL builder; insert is the coordinator's job.

## 1. Topics and sources

Same verified fact base as the W46 NL core and the NL × EN edition (see
`files/weekly-report-w46-nl-en/WEEKLY-KIT.md` §1): Sinterklaasjournaal
from 9 Nov, national arrival Grave 14 Nov, 88th Amsterdam arrival 15 Nov,
Sint-Maarten 11 Nov, Oranje Nations League vs Greece (13 Nov) and Germany
(16 Nov preview), Heel Nederland Leest (`Het diner`, Herman Koch),
Expeditie Robinson (Sundays 20:00 RTL 4). No invented polls, quotes,
accounts or results; no squad names used. Weekdays verified
`TZ='Europe/Amsterdam'`. Sinterklaas in Traditional Chinese: 辛特克拉斯;
Grave: 赫拉弗; Sint-Maarten: 聖馬丁節; `Het diner`: 《晚餐》; Oranje:
荷蘭隊; lampion: 燈籠.

## 2. Promises honoured (from W45 NL VOL.2)

Sinterklaas arrival Amsterdam 15 Nov and Sint-Maarten 11 Nov are the lead
topics. Readers' corner: no real letters or best page-8 texts had arrived
at press time — labelled editor's example + on-page disclosure in Dutch
and Traditional Chinese (`截稿時未收到真實來信或第 8 版最佳作文，刊登示例信，承諾順延 VOL.4。`);
promise carried forward to VOL.4. No fabricated readers, letters, names
or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (練習數據):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × ZH-TW measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · 每週一期 · 讀荷蘭人正在讀的荷蘭語`.
- Subtitle uses SPACED form at 40pt: `荷 語 週 報 · VOL.3 · SINTERKLAAS ·
  SINT-MAARTEN · ORANJE` (measured 1237.5px < 1820, fits).
- Pairing badge REPLACES the strapline at y=372, 19.5pt bold BRICK:
  `荷語正文 · 繁體中文講解 — 給繁體中文讀者的版本` (measured 444.9px, fits).
- Footer: `De Lucerna · 荷語週報 VOL.3 · 正文荷語 · 講解繁體中文` +
  `第 N 版 / 共 8 版` (core form, unchanged). Gloss prefix `譯注｜`
  (added by `gloss()` itself; core simplified `译注｜` replaced).
  Glosses: Dutch word + space + Traditional Chinese, items joined by
  ` · `. P7 bridges use `；` separators and `：` for examples. P8 notes
  use ` = ` with FULL-WIDTH parentheses （）. P8 separator
  `— 第 {pg} 版 —`. P7 quote page tags stay Dutch `(Pagina N)`.
- P8 sizes stay at CORE values (Flow bottom 2552, separators 14pt/1.16/2,
  keys 13.5pt/1.16/0.5). `bridge()` renamed to `expl()` (signature
  unchanged; the P1 expl string carries its own `講解｜` prefix, P7 a/b/c
  expl strings have none). svglib: TC face (`_tc_index`,
  `endswith("TC")`, Noto Serif/Sans CJK TC) — copied from the W45 zh-tw
  build after the transform; diff vs core svglib is ONLY those 4 hunks.
- Registry labels: type tokens in Traditional forms (完形單選, 單選,
  詞彙配對, 判斷對錯, 完成句子, 造句, 翻譯, 寫作); instruction words
  localised (判斷, 寫作, 翻譯 — all four translation items carry instr
  `翻譯`, no direction refinement, W45 zh-tw precedent; match instr
  `把詞和釋義配對`). The disclosure variable KEEPS the name `dt_zh`
  (W45 zh-tw precedent).
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Traditional Chinese. Clinic Dutch wrong/right sentences
  verbatim; notes in Traditional Chinese. Translation items 137/138
  re-aimed NL→ZH-TW (keys are the Traditional Chinese translations);
  139/140 prompts re-aimed ZH-TW→NL (keys stay Dutch).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Traditional Chinese with Dutch `(Pagina N)` page tags kept.

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-zh-tw-build/` (copied from
the W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to natively
written Traditional Chinese (`gen_zhtw.py`, kept at
`hidden_files/w46/gen_zhtw.py`; 313 replacements, FAILED: 0; the pairs
file `hidden_files/w46/en-reps.txt` was re-extracted from the shipped EN
transform after a /tmp wipe — 265 pairs, exact EN wording incl.
`Translate into English/Dutch` refinements and `True:`/`False:` forms).
Freeze baseline before transform: 8/8 byte-identical, core untouched.
Transform run ONCE per fresh copy. After the transform, the W45 zh-tw
`svglib.py` was copied over the build dir's `svglib.py`. Build: `run.py`
(one process) + `render.py` (cards + print PDF). Web PDF via
`tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-ZH-TW.pdf` (18,513,144 bytes — larger than the Latin
editions because the CJK TC fonts are embedded), web PDF
`De-Lucerna-VOL3-ZH-TW-web.pdf` (1,614,950 bytes, 44,458 text bytes),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-zh-tw.text.md` (exported
from the source manuscript via `hidden_files/w46/export_text.py`, never
from PDF).

## 8. Fix record (W46 ZH-TW)

- Fix 1 — simplified-leftover scan: the transform's tail check uses a
  discriminator set of simplified-only characters. Its first run reported
  1 hit — a false positive: 具 in the authored string 三件工具 (具 is
  shared Traditional/Simplified). The set was corrected (具 removed);
  re-run reports 0 simplified-only characters left.
- No geometry fixes were needed: P7 col-3 stack ends 1927.5 (= core),
  P1 word gloss 1 line, all gates green on the first full build.

## 9. Gates (2026-11-02, recorded in `hidden_files/w46/nl-gates.log`)

- Builder self-check: TOTAL 150, by page 10/18/18/18/18/18/12/38, zero
  FLOW OVERFLOW / HEAD TOO WIDE.
- `occlusion_audit.py`: selftest OK, edition 0 flags, core 0 flags,
  NEW vs core: 0.
- Same-baseline furniture scan (rowcheck.py): all 8 pages CLEAN; P6
  chart-label GRAZE coverage 0.0%; gloss counts core-vs-edition OK
  (6/5/5/5/5).
- `freeze.py diff` (non-strict; strict-CJK is inapplicable — Traditional
  Chinese legitimately adds characters the Simplified core does not
  have): exit 0; added CJK 1,241 chars adjudicated per-char — 0
  simplified-only characters among the added set; all added characters
  are Traditional forms from the authored strings.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138]
  (legal re-aims: keys are the Traditional Chinese translations).
- Web PDF: 1,614,950 bytes (<7 MB), 44,458 text bytes (>0).
- Visual check: P1 viewed clean (badge replaces strapline, spaced
  subtitle, top-strip gap, word gloss 1 line); P7 letters-box crop viewed
  (clean gap above the rule, stack ends 1927.5).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Traditional Chinese;
Dutch target text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: ` 月 11 日聖馬丁節燈籠、荷蘭隊國家聯賽對希臘與德國之戰。荷語正文・繁體中文講解，A2～B2 程度，150 道練習題，用荷蘭新聞學荷蘭語。` After tail: `1 月 11 日聖馬丁節燈籠、荷蘭隊國家聯賽對希臘與德國之戰。荷語正文・繁體中文講解，A2～B2 程度，150 道以本週話題為素材的練習題。`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: exactly 3 lines (gloss, chart caption, P8 H-intro below).
- E-2: P6 chart caption (`capcn`) `transform.py` new-string `練習數據：僅供練習的虛構數字，不是真實調查。問題：…` → `練習數據：虛構數字，僅供練習，非真實調查。問題：…` (exact Traditional mirror of the core caption); line 1 now ends with `。`, line 2 starts `問題：`. Verified visually (full frame + crop).
- E-3: P8 H-intro `transform.py` new-string `寫作題（沒有唯一答案）；範文（{NWORDS} 詞）見下。` → `寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。` — now one line (416.8px), no lone `。`. Verified visually (full frame + crop). P6 gloss also carries the F-2b tightening (`關注· de`) with the gloss already reading `嚇人`.

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): added CJK 1,238, 0 simplified-only characters (spot-list scan); exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 32320 bytes; web PDF 1615015 bytes, pdftotext 44455 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 18512823 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.
