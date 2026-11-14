# Lucerna — Русская газета VOL.1 · RU × DE （俄语正文 + 德语讲解版）

**Edition:** Russian text + **German** explanations (target RU × reader-native DE), for German-speaking learners of Russian.
**Week:** Mon 19 – Sun 25 Oct 2026 (VOL.1, same issue week as the finalized core).
**Masthead:** **Lucerna** (no article, per SOP masthead rule). Page size 1950×2700, 8 pages, warm ivory.
**Pairing badge (P1, brick red, 20pt bold, centred under the masthead strap):**
„RUSSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
**Footers (German, every page):** left „Lucerna · RUSSISCHE WOCHENZEITUNG VOL.1 · TEXT AUF RUSSISCH · ERKLÄRUNGEN AUF DEUTSCH" · right „Seite N von 8".
**Status: BUILDER-COMPLETE.** All builder gates below passed. NOT posted to Discord (per assignment). Independent proofread + posting are the parent's next steps, per programme pattern.

Source: the finalized, P8-patched Russian core (Russian text + Chinese explanations,
`files/weekly-report-ru-vol1/`). Build copied to `hidden_files/weekly-report-ru-de-build/`;
the core's own directories were never edited. Method = the FR×DE / RU×EN sibling pattern:
rewrite the explanation layer only, freeze everything Russian.

---

## 1. Totals (registry-derived, identical to the core)

- **150 exercises** — A2 54 · B1 72 · B2 24; per page 10/18/18/18/18/18/12/38 (same as core).
- Writing model (P8 §H): **exactly 82 words**, unchanged Russian text; the „80–100 слов" task range unchanged.
- Visible characters (no-space, rendered text): core 27,474 → **this edition 32,782** (German apparatus).
- Registry `type` strings were localized to German inside this build's registry only
  (Ausfüllen 54 · Ankreuzen 42 · Zuordnen 20 · Sätze bilden 12 · Umformen 4 · Lückentext 13 ·
  Übersetzen 4 · Schreiben 1 — counts identical to the core); type strings never print.

## 2. Baseline reproduction (before any edit)

The unmodified copy of the core build regenerated all 8 SVGs **byte-identical** to the shipped
patched core SVGs (`cmp` clean on all 8), and its registry matched the core exactly
(150; A2 54·B1 72·B2 24; pages 10/18/18/18/18/18/12/38; model 82 words). All German edits were
made on top of that proven baseline.

## 3. Freeze verification (rendered SVGs, this edition vs core)

- Text-element multiset diff per page: the only removed Russian line anywhere is the P1 strap
  subtitle (the documented badge accommodation, §4). One P8 element difference („Пушкина") is a
  keys-flow line-wrap fragment, not a text change — every registry key was verified present
  verbatim in each edition's own P8 render (150/150 in both).
- Registry field diff (all 150): page and level identical for every item; **keys differ only at
  #137, #138 and #150** (the documented re-aims, §5); #139/#140 keys byte-identical Russian.
- P7's 8 phrases of the week: each occurs **exactly 2×** in the rendered issue (article + P7),
  byte-verbatim, page tags correct — identical counts in core and this edition.
- Image payloads: byte-identical to the core on every page (base64 comparison).
- **CJK characters in the final SVGs: 0.** The banned intermediary term appears nowhere in the
  paper, this KIT, or the build code (the copied library's internal method was renamed
  `Flow.note`, output-neutral).

## 4. Pairing furniture

- **Badge** replaces the P1 strap subtitle — the same accommodation the RU×EN edition used
  (the subtitle's „for learners of Russian" line is the one line two apparatuses cannot share).
  Brick red per this edition's assignment (the build palette's BRICK, #a4553a in the SVG).
- Top strip centre: „КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · JEDE WOCHE · RUSSISCH, WIE RUSSLAND ES LIEST" —
  measured span 549.3–1400.7; left item ends 376.3, the date starts 1444.0 (≥43px clear both sides).
- P1 numbers-box title shortened to „НЕДЕЛЯ В ЦИФРАХ · Zahlen" (full German half overflowed the
  box) — the same fix the RU×EN edition recorded.
- Word-of-the-week gloss kept to one line: „похолодает = es wird kälter."
- P2 matching instruction shortened to „Paare zuordnen" (the longer form clipped its column in
  the sibling edition; pre-empted here).
- Contents head shortened to „В ЭТОМ НОМЕРЕ · Inhalt" — the full „· In dieser Ausgabe" measures
  440.1px against the box's 390px inner width and spilled past the border in the first render;
  „Inhalt" = 303.6px. („СЛОВО НЕДЕЛИ · Wort der Woche" fits as-is at its 22pt size: 381.2px.)

## 5. Re-aimed items (the only key/prompt changes — translation pedagogy)

| # | Change | Key in this edition |
|---|---|---|
| 137 | RU→DE: Russian stem kept; instruction „Ins Deutsche übersetzen" | „Am Sonntag spielt ZSKA gegen Spartak." (note: Vergleichen Sie Seite 4) |
| 138 | RU→DE: Russian stem kept; instruction „Ins Deutsche übersetzen" | „Die Wetterdienste versprechen Schneeregen für Ende Oktober." (note: мокрый снег = Schneeregen) |
| 139 | Prompt now German: „Die Ferien beginnen am Samstag — insgesamt zwölf Tage. → ___"; instruction „Ins Russische übersetzen" | Russian sentence, **byte-identical** (note: Achten Sie auf den Kasus: двенадцать дней) |
| 140 | Prompt now German: „Ich wünsche meinem Papa alles Gute zum Vatertag! → ___"; instruction „Ins Russische übersetzen" | Russian sentence, **byte-identical** (note: поздравляю + с + Instrumental) |
| 150 | Registry line is German apparatus | „(offene Aufgabe — Mustertext unten)"; note „Der Mustertext steht in Abschnitt H dieser Seite (82 Wörter)" |

The P8 §H instruction prints the count from the registry: „der Mustertext (82 Wörter)". The model
letter itself is unchanged Russian. All other 145 keys byte-identical to the core.

## 6. Answer notes

All 150 P8 notes are in German (grammar, facts, glosses), in the core's terse register, with a
space before every note parenthesis (half-width parentheses only; the full read-through of all
150 notes is the builder's re-solve pass — every key was re-derived from the issue's own facts:
forecast window 21–23 Oct; Father's Day Sun 18 Oct; holidays Sat 24 Oct – 4 Nov = 12 days;
Dynamo 25 / Zenit 24 / Spartak 23; derby Sun 25 Oct 16:00; 900 ₽ ticket; chart 34/28/22/16;
weekday claims re-checked against the 2026 calendar: 18 Sun, 22 Thu, 24 Sat, 25 Sun, 28 Wed,
31 Sat, 4 Nov Wed — all match).

## 7. Geometric audit (mandatory SOP gate — builder run)

Paint-order audit of all 8 final SVGs with real-font (production-metrics) glyph boxes
(coverage ≥30%, footer band y>2580, page edges, thin-line crossings; script
`audit_ru_de.py` in the build dir, same tool as the IT×DE sibling):

- **0 flags on all 8 pages.** Control run on the core SVGs: also 0 flags.
- **P8 key baselines per column (rule at 2580):** col 1 lowest 2517.90 (62.1px clear) ·
  col 2 2502.26 (77.7px) · col 3 2521.47 (58.5px) · col 4 2430.48 (149.5px). Overall lowest
  2521.47 → **58.5px clear**, better than the core's patched 47.4px; the ≥40px requirement holds
  in every column despite longer German notes.
- **P7 columns:** col 1 ends 1653.96 · col 2 ends 1653.96 · col 3 ends **1682.96** (exactly the
  core's value) — all above the phrases band (rule y=1698). Getting col 3 there took one fix:
  the readers'-corner note first wrapped to 3 lines (col ended 1711.96, inside the band);
  final note „Beispiel der Redaktion, kein echter Brief. In VOL.2: echte Briefe und beste
  Texte!" wraps to 2 lines and keeps both VOL.2 promises. Clinic note #4 was likewise kept to
  one line („Genitiv nach «с»: с первого октября.").
- **Known P2 item (kept, measured):** the weather-strip reminder line (baseline 1800) vs the
  exercises rule (rows 1803–1804). My own pixel measurement of THIS edition's rendered P2 card:
  glyph ink ends at row **1802**; the rule rows 1803–1804 carry **zero** dark ink pixels
  (1820 gold px each). No contact — the same non-defect adjudication as the core and RU×EN;
  geometry unchanged.
- Build log: zero FLOW OVERFLOW / HEAD TOO WIDE warnings in the final run.
- All 8 cards viewed by the builder after the final render.

## 8. Builder fixes during production (all geometry/apparatus only)

1. P1 contents head „In dieser Ausgabe" → „Inhalt" (§4, width).
2. P1 numbers box: space added before the two German note parentheses („октября (vier neue …",
   „футболу (12. Spieltag …)") — German typography; lines re-wrap inside the measured box.
3. P7 readers'-corner note shortened to 2 lines (§7) + clinic note #4 to one line.
4. Badge fill set to brick red (final pass).

Inherited core keeps (identical in the core and the EN sibling; frozen geometry, not defects of
this edition): the P1 „КОРОТКО" box's last Russian line sits on its fixed-height border; all
captions and credits are Russian by design.

## 9. Images & credits (byte-identical payloads; credits identical to the core)

| Page | Image | Credit (as printed) |
|---|---|---|
| P1 | Konstantin Yuon, «Зима. Ростов» (winter in Rostov) | Константин Юон — public domain (Wikimedia Commons) |
| P2 | Wilson Bentley snowflake microphotograph | Уилсон Бентли — public domain (Wikimedia Commons) |
| P3 | Kiprensky, Portrait of Pushkin, 1827 | Орест Кипренский, 1827 — public domain (Wikimedia Commons) |
| P3 | Bilibin, «Морозко» illustration, 1932 | Иван Билибин, 1932 — public domain (Wikimedia Commons) |
| P4 | Russian football team, 1912 Olympics | автор неизвестен, 1912 — public domain (Wikimedia Commons) |
| P5 | USDA Halloween farmers-market photo | Министерство сельского хозяйства США — public domain |
| P6 | Autumn park (Toxer427) | Toxer427 — CC0 (Wikimedia Commons) |

Image licensing verification is the core's (§9 of the core KIT); this edition changes no image.

## 10. Facts (identical to the core)

«Первый снег» lead (window 21–23 Oct, forecasters disagree); last school week, holidays
Sat 24 Oct – Wed 4 Nov = 12 days (ministry recommendation Mon 26 Oct – Tue 3 Nov + weekends +
Unity Day); Lyceum Day Mon 19 Oct (1811, 215 years); four fairy-tale films Thu 22 Oct; RPL
matchday 12 from Fri 23 Oct, derby ZSKA–Spartak Sun 25 Oct 16:00 (pre-match, no result printed);
Halloween Sat 31 Oct; Grandparents' Day Wed 28 Oct; Father's Day Sun 18 Oct (6th since 2021).
Russian domestic life only; no politics. The P6 chart is labelled an editorial exercise survey
in both languages („Übungsdaten — keine echte Statistik"), bars 34/28/22/16 as the core.

## 11. Files

- `files/weekly-report-ru-de/svg/` — 8 final SVGs
- `files/weekly-report-ru-de/cards/` — 8 cards (1950×2700 PNG)
- `files/weekly-report-ru-de/Lucerna-VOL1-DE.pdf` — print PDF, **21,917,907 bytes** (D5 rebuild 2026-11-14; D5 前 22,613,373 bytes) — sha256 `2f688f3f8bd3e5a8b896e18517d500735816273550f92c69f7fe1caa9e396c04`
- `files/weekly-report-ru-de/Lucerna-VOL1-DE-web.pdf` — web PDF, **2,292,159 bytes** (D5 rebuild 2026-11-14; D5 前 3,678,837 bytes) — sha256 `2861dafdc5460f80f7cfaa29d87dd605128b8821efd54ea643f332ad60a27e4d` (< 10 MB Discord limit)
- Build: `hidden_files/weekly-report-ru-de-build/` (run.py → render.py; audit_ru_de.py alongside)

## 12. Independent proofread record (second pair of eyes, 2026-10-21)

**Method.** Fresh full pass over the shipped artifacts, trusting nothing in §§1–11: both
builds re-run in scratch copies — each reproduces its shipped SVGs byte-identically and
its registry exactly (150; A2 54 · B1 72 · B2 24; pages 10/18/18/18/18/18/12/38; model
82 words); full text-element multiset diff of all 8 pages against the frozen core plus a
Cyrillic/digit token-multiset diff per page; all 150 exercises re-solved from the printed
stems, options, articles and chart (not a sample); all 150 German notes read against
their keys; every weekday re-checked against the real 2026 calendar; geometric audit
re-run with a synthetic positive control, plus independent P8-baseline, text–text and
pixel measurements; image payloads hashed per page; all 8 cards viewed.

**Problems found: none. Fixes made: none.** No re-render was needed; the shipped files
stand as built.

**Verified, point by point:**
- **Freeze.** Registry page/level identical for all 150; keys differ only at #137/#138
  (German) and #150 (apparatus line); #139/#140 keys byte-identical Russian. Every
  Cyrillic-bearing text difference is a bilingual header/gloss line whose Russian half is
  byte-identical, the documented P1 strap-subtitle → badge replacement, or P8 apparatus
  (German notes; #39–42 notes cite the Russian film titles where the core cited Chinese
  translations — apparatus either way, keys unchanged). Writing model byte-identical to
  the core, exactly 82 words (AST-extracted from both builds).
- **The two builder shortenings.** Contents head „· Inhalt": the box's Russian half and
  all seven contents entries (titles, pages, level tags) are identical to the core —
  nothing is lost; „Inhalt" carries the head's whole meaning. Readers'-corner note
  (2 lines): both VOL.2 promises survive („echte Briefe und beste Texte"); the dropped
  "page 8" qualifier of the core's note is carried by the teaser's Russian line on the
  same page („лучшие сочинения со страницы 8"). Clinic note #4 is the claimed one-liner.
- **Numbers box (P1).** Russian facts untouched (12 days · 4 films Thu 22 Oct · 8 matches ·
  215 years); the space before both German note parentheses is present — in fact a full
  scan finds no letter/digit glued to "(" anywhere in the edition.
- **Language.** CJK/full-width characters: 0 on all 8 pages. German apparatus is natural
  and complete (glosses, instructions, clinic, chart disclaimer „keine echte Statistik",
  all 150 notes); case terminology used correctly throughout. The banned intermediary
  term occurs 0 times in the paper, this KIT and the build code.
- **Re-solve.** All 150 keys correct against the printed matter, incl. all five matching
  sets (25–28, 39–42, 57–60, 75–78, 141–144), the chart items (#85 = grandparents 34 %,
  #86 = 22 %, #87 = 28 %; bars re-measured in the SVG at 600/494/388/282 px, identical to
  the core), the calendar strip's 12 weekday letters, and the Anton reading set.
  Weekdays: 18 Sun · 19 Mon · 22 Thu · 24 Sat · 25 Sun · 28 Wed · 31 Sat · 4 Nov Wed —
  all match the 2026 calendar.
- **Geometry.** Builder's audit re-run on the shipped SVGs: 0 flags on all 8 pages (core
  control also 0); the audit script itself was validated on a doctored page (injected
  cover rect + line → flagged). P8 lowest baselines per column re-measured independently:
  **2517.90 / 2502.26 / 2521.47 / 2430.48** — the builder's figures to the decimal; worst
  clearance 58.5 px. Text–text scan: the only band overlap is the P1 masthead/strap pair,
  byte-identical geometry to the frozen core and visually clean (band-model descender
  allowance; „Lucerna" has no descenders). P1 КОРОТКО box's last line sits on its border
  exactly as in the frozen core — the documented inherited keep.
- **P2 known item — re-measured on this edition's card.** Reminder-line ink ends at row
  1802 (descender tips at isolated x positions); rule rows 1803–1804 carry zero text ink
  (the only dark pixels there are the page-frame borders, present on every row). No
  contact → non-defect, as adjudicated in the core and RU×EN. Builder's claim exact.
- **Furniture/facts.** Badge present on P1 (centred x=975, y=372, 20 pt bold, fill
  #a4553a); top-strip centre span re-measured 549.3–1400.7 with ≥43 px air both sides;
  pairing footers with correct page numbers on all 8 pages; masthead „Lucerna" (no
  article). P7's 8 Russian phrases byte-identical, each occurring exactly 2× issue-wide,
  page tags byte-identical Russian «(Страница N)» and correct; German translations
  complete (phrase 2 wraps two elements — verified whole). Image payloads MD5-identical
  to the core on every page; Russian credits identical. Char counts reproduce exactly
  (core 27,474 → this edition 32,782, no-space). Both PDFs 8 pages; sizes as in §11.

**Final verdict.** One complete independent pass found **zero problems**. The RU × DE
edition is final and ready to post.

## 13. D5 rebuild (2026-11-14)

D5 + §1.1 合并重建（2026-11-14；builder v3 接替 v2，v2 死于 2026-11-14 ~02:55 UTC 第 5 波 restart drain）。本节 supersedes 上述旧印/网 pin 行（以实测发运值为准；KIT 旧 SHA 不可作基线）。

- 装机：`apply_variant.py --patch-core ru --week 2026-w43`（core-ru `_D5_READER = "latin"`，+263/−28）+ 本版 `apply_variant.py --svglib patched/2026-w43-ru-de/svglib.py --target ru --reader de --week 2026-w43`（`_D5_READER = "latin"`，diff +63/−2）；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2 保留。
- 基线：run TOTAL 150，0 警告；印 PDF 22,261,264 B（MANIFEST +0.001%），网 PDF 2,336,205 B，`pdf_text_diff_ru.py` + TRIM_ARGS → IDENTICAL；修前普查 D5 拉丁 453、西里尔 0。
- 缺陷与修法（只动字号/断行与规则线位置，不动文字）：
- D1 (boxtitle/creambox, P1): 出处行越框 +3.5px（基线 −5.5px）— `content12.py:85` 19→18pt。
- D2 (occlusion TEXTX, P1): `'A2' overlaps 'кино' 7.4×11.2px` — `content12.py:103` 目录标题 20→19pt。
- D3 (occlusion LINEX P2 ×6, 基线同款): `content12.py:232` 规则线 `ey−12`→`ey−8`。
- 门禁（run2）：全套 17 门 ALL-GREEN。run TOTAL 150；head_check 0；d5 census 拉丁/西里尔/弯引号在 CJK 均 0（弯引号总数 0；`noto_sans_elements=411`）；freeze baseline 8/8；freeze diff 新增 CJK 0、新增拉丁 strings 151（run 拆分）；spill 0（171 OBSERVE）；boxtitle 0 DEFECT（58 titles, 715 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=405, median 1.022；P8 212→212 行，slack 61.0→61.0px）；文字层 print=web 差 0（40,487 字）；text.md BYTE-IDENTICAL；census_quotes 0 defective；p8 compare CLEAN，keydiff=[137, 138]；刊头标语→日期间距 294.0px PASS。日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-de/GATES-SUMMARY-run2.txt`。
- 新交付物（实测）：印 PDF `Lucerna-VOL1-ru-de.pdf` **21,917,907 B**，sha256 `2f688f3f8bd3e5a8b896e18517d500735816273550f92c69f7fe1caa9e396c04`；网 PDF `2026-w43-ru-de.web.pdf` **2,292,159 B**，sha256 `2861dafdc5460f80f7cfaa29d87dd605128b8821efd54ea643f332ad60a27e4d`；text.md **60,804 B**，sha256 `0f6cd66c590b820e98afbfdd999a91932ad6ee3e3e569e5a13610b1fc05d7a11`，与 fanout `.text.md.new` BYTE-IDENTICAL。D5 报告：`production/notes/2026-w43/g-ru/scratch-d5-rebuild-ru/D5-REPORT-2026-w43-ru-de.md`。
