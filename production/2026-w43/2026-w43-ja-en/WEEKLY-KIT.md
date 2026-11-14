# WEEKLY-KIT — Japanese Weekly VOL.1 · JA × EN edition (Japanese text · English explanations)

The English-explanations edition of the Japanese Weekly VOL.1: the same issue as the
finalized core edition (Japanese text + Chinese explanations), with the whole
explanation apparatus rewritten in English for English-speaking readers. Japanese
content — articles, exercise stems and options, quoted sentences, the text being
taught — is unchanged, element for element.

- Week: Mon 19 – Sun 25 Oct 2026 (W43) · 8 pages · page size 1950×2700
- Files: `svg/` (8 SVG), `cards/` (8 PNG 1950×2700),
  `Lucerna-VOL1-EN.pdf` (print, 41,112,807 B),
  `Lucerna-VOL1-EN-web.pdf` (web, 3,117,923 B — under the ~10 MB server limit)
- Core edition (frozen, untouched): `files/weekly-report-ja-vol1/`; core build:
  `hidden_files/weekly-report-ja-build/`. This edition's build:
  `hidden_files/weekly-report-ja-en-build/` (a copy; the core was never modified —
  final check: all 8 core SVGs still byte-identical to the baseline reproduction).

## Pairing badge and footers

- P1 masthead carries the pairing line, bold olive, centered under the edition line:
  **TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS**
  (masthead name stays "Lucerna", no article — article-less language convention).
  To fit it, the masthead block shifted: wordmark baseline 262→248, edition line
  330→316, tagline 372→390, rules 392/401→406/413; the dark band stays at y=424.
- Every page footer: left `Lucerna · JAPANESE WEEKLY VOL.1 · Japanese text · English explanations`,
  right `Page n of 8`.
- In-text gloss lines use the prefix `Note — ` (was the Chinese 译注｜ in the core).

## Counts (identical to the core)

- Exercises: **150** — A2 48 · B1 75 · B2 27; per page 10/18/18/18/18/18/12/38.
  Types: fill-in 51 · multiple choice 50 · matching 12 · sentence building 8 ·
  true/false 11 · cloze multiple choice 13 · translation 4 · writing 1.
- Page 8 writing model 『私の秋の週末』 = 150 characters, unchanged.
- Visible characters (same text-element count as the core KIT): **21,149** without
  spaces / **24,040** with spaces (core: 16,815 / 18,508). The growth is the English
  apparatus; the Japanese text mass is unchanged.

## What changed vs the core — and what did not

Changed (apparatus only): every gloss/note, exercise instruction, section-header and
band-subtitle English half, the three "your turn" reader lines, the P2 season-word
card glosses, the P7 error-clinic notes, frame/letter notes, the P7 phrase
translations, the answers header, the keys' group headers, the registry type names,
and **all 150 answer notes** — rewritten as full, natural English (not glosses of
the Chinese).

Re-aimed translation items (the only key changes; the translation exercises now
point at English, the reader's language):

- #137 key (JA→EN): `The procession leaves Kyoto Gyoen at 12:00.`
- #138 key (JA→EN): `If you drop litter, the fine is 2,000 yen.`
- #139/#140 bodies are now English prompts (`Reading Week starts next Tuesday.` /
  `I want to go to the Halloween event in Ikebukuro.`); their Japanese keys are
  byte-identical to the core.
- #150's registry line reads `(open task — model text below)` (its note is #149's
  neighbour line `Model text in section H on this page (150 characters)`); the item
  itself, an open writing task, is unchanged.

Not changed: every Japanese article, stem, option, letter and figure; all other
answer keys byte-identical; the exercise registry (numbers, levels, pages, types)
identical; all 7 photos byte-identical with the same (Japanese) credit lines —
P1 Yokohama Stadium (Syced, CC0), P2 maple (Poliphilo, CC0) + mochi (Fumikas
Sagisavas, CC0), P3 Hiroshige print (PD), P4 Waseda 1911 (Bain News Service, PD),
P5 pumpkins (Petr Kratochvil, PD), P6 para swimming (EJ Hersom / US DoD, PD).

## Verification (all measured on the final render)

- **Baseline:** the unmodified build copy reproduced all 8 shipped core SVGs
  byte-identically before any edit.
- **Registry diff:** re-derived independently from both builds — identical except
  the four items above; all 150 notes new English; zero simplified-Chinese
  characters in any note.
- **Rendered-text diff:** per-page element multisets vs the core — every removed
  element is Chinese apparatus, every added element its English counterpart, the
  badge, or the pairing footer (identical/apparatus-only on all 8 pages).
- **CJK scan:** simplified-only character hits = the character 写 inside 写真
  (Japanese for "photo", in the unchanged credit lines) and 声 inside 大きな声
  (Japanese article text) — both Japanese shinjitai in Japanese content, zero
  Chinese-apparatus remnants. The banned term: 0 occurrences
  (paper, code, KIT).
- **P7 phrases:** each of the 8 phrases occurs exactly 2× (verbatim from the
  issue's articles), with English translations and (p.N) tags.
- **Re-solve sample:** 30+ exercises re-solved from the articles (incl. all three
  matching maps 25–28 / 43–46 / 141–144 and chart items 91–93); all keys correct
  against their English notes.
- **P8 keys flow:** ends at y=2382 (column 3); the lowest small-type baseline on
  the page is 2514.9 — 65px above the footer rule at 2580 (requirement ≥40px);
  no text in the 2540–2580 band.
- **GEOMETRIC OCCLUSION AUDIT (SOP addendum):** paint-order coverage ≥30% = 0
  flags; footer-band intrusion = 0; page-edge spill = 0; frame-crossing scan
  (start-anchored text ending past the inner frame x=1910) = 0 after the fixes
  below. One line-crossing flag: P2's model-sentence line vs the exercises rule
  at y=1804 — the rule rides the sentence's baseline as an underline, glyph ink
  entirely above it (crop-adjudicated). The identical flag fires on the frozen
  core SVG: inherited geometry, the +0.30em band overestimates CJK descent;
  **not a defect**. Zero unresolved flags.

## Adjudications

- P1 masthead shifted up to make room for the badge line (see above); nothing else
  on P1 moved.
- Four strings shortened after glyph-width measurement (PIL, production fonts):
  P1 numbers-box title → `数字で見る今週 · Week in numbers` (was ending 10px past
  the box border); P2 match instruction → `Match place to peak date` (was ending
  at x=1946, across the page frame); P3 match instruction → `Match events to
  places`; P8 match instruction → `Match words to meanings` (both were spilling
  into the next column).
- P7 readers'-corner English note shortened to `Editors' example — not a real
  letter. VOL.2: real letters and the best Page 8 writing!` — the longer draft
  pushed the VOL.2 teaser to y=2551, past the 2540 content limit; it now ends
  at 2522.
- #137's key uses "leaves" (not "sets off from") so the registry line does not
  strand a lone numeral on its second line.
- P4 Ohtani box: the ※ line's last word sits one line below the box's bottom
  border — byte-identical inherited core geometry (region crop SHA-identical to
  the core card), fully legible, kept as in the core.
- One core gloss itself used the simplified form 见 for a Japanese word; the
  English note prints the correct Japanese form （見たい = want to see).
- A handful of Japanese body lines measure up to ~18px over the nominal column
  width (kinsoku push-out in the frozen core wrap); the overshoot lands in the
  28px gutter and touches nothing — identical in the core, kept.

## Carried VOL.2 promises (printed in the P7 teaser, Japanese, unchanged)

1. Reading Week coverage (Tue Oct 27 – Mon Nov 9; slogan 「静かだけど、冒険中。」).
2. Halloween report (Sat Oct 31 — Shibuya rules, Ikebukuro festival).
3. Japan Series results.
4. Real readers' letters + the best Page 8 『私の秋の週末』 writing.

## Reproduce

```bash
cd hidden_files/weekly-report-ja-en-build
/tmp/wp-venv/bin/python run.py      # writes svg/ into files/weekly-report-ja-en/
 /tmp/wp-venv/bin/python render.py # cards + Lucerna-VOL1-EN.pdf + -web.pdf
```

---

## Independent proofread record (separate proofreader, fresh pass)

**Scope & method.** Full independent re-verification against the shipped artifacts, not the builder's notes: (1) scratch rebuilds of BOTH build trees (OUT redirected) reproduce all 16 shipped SVGs **byte-identically** — EN and core; (2) registry re-dumped from both builds and diffed; (3) full-text character counts recomputed from the shipped SVGs; (4) element-level (multiset) text diff of all 8 pages, EN vs frozen core, every element accounted for; (5) all 150 exercises re-solved from the printed stems (P8's 38 from the test page itself; P1–P7 from the rendered pages, including both matching maps and the chart arithmetic); (6) independent geometric audit with production font metrics (paint-order coverage, footer band, page edges, thin-line ink-band crossings); (7) all 8 rendered pages viewed in full, plus adjudication crops.

**Findings: ZERO problems.** Nothing required fixing; no re-render was needed.

Verified in detail:
- Registry: 150 items in both editions; pages 10/18/18/18/18/18/12/38; A2 48 · B1 75 · B2 27; type distributions map exactly. Key diff vs core = ONLY #137, #138, #150 — precisely the documented reader-language items. #139/#140 Japanese keys identical; the English model 『私の秋の週末』 counts exactly **150 characters** in the shipped SVG.
- Text diff: every removed element is Chinese apparatus; every added element is English apparatus, the masthead badge, a pairing footer, or a documented item (masthead block shift; the four shortened strings on P2/P3/P8 + the P7 readers'-corner note; the P7 teaser geometry change). **No undocumented core change.** All 150 English answer notes read and checked — accurate, grammatical, each with the space before its " — " note separator.
- Language audit: zero Chinese apparatus remnants. Character scans find only Japanese shinjitai inside Japanese content （国・当・写・声 etc.); U+FFFD count 0 in both editions; the banned "bridge" term occurs 0 times in paper, code and this KIT.
- Character counts recomputed: EN **21,149 / 24,040**; core 16,815 / 18,508 — both exactly as the build record states.
- P7 phrases: each of the 8 occurs exactly 2×; page tags (p.1)×2, (p.2)×2, (p.3), (p.4), (p.5), (p.6) all correct. Chart bars on P6 measured: 1020/840/660/480 = exactly 30 units per percent, identical to core.
- Images: 7 payloads byte-identical to core per page; credits ride inside identical Japanese text elements.
- Geometry: coverage audit (5% reporting threshold, stricter than the SOP's 30%) — zero flags on all 8 pages; footer band — zero intrusions; page edges — zero spill. P8 lowest baselines 2514.92 (cols 1/3), 2513.42 (col 2) — builder's 2514.9 confirmed, 65px clear of the 2580 rule. P7 teaser band bottom measured **2522.12** — builder's 2522 confirmed.
- Badge: visible in the P1 render ("TEXT IN JAPANESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS"); pairing footers on all 8 pages. PDFs: print 41,112,807 B / web 3,117,923 B, both 8 pages.

**Adjudications (proofreader's own judgement, crops examined):**
1. **P2 model-sentence rule (y=1804) — AGREE: keep.** The identical flag fires on the frozen core. The crop shows the rule running directly beneath the model sentence as a section underline, ~4px below the baseline; it strikes no glyph and the sentence is fully legible in both editions.
2. **P4 Ohtani box ※ line — AGREE: keep.** The EN and core region crops are literally identical (same SHA-256). The final line 「ません。」 is complete and legible; its baseline sits inside the box with ink grazing ~4px past the bottom border — an inherited core cosmetic quirk, not a defect of this edition; altering it here would only diverge the EN layout from the frozen core.

**Verdict: the edition is FINAL.** One complete independent pass found zero problems; the builder's claims held at every point checked, including both adjudicated items and all measured figures.

---

## Patch note — 2026-10-21 · Core-level correction: P7 vocabulary-deck column-seam overprints (geometry only)

**Defect (found by the JA×PT independent proofread, §13; record: hidden_files/ja-p7-overprint-correction.md).** Two frozen Japanese lines on P7 wrapped past their column and overprinted the neighbouring column's first glyph, producing merged illegible glyphs: (a) B1 column (x=527, baseline y=336.86) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; (b) A2 column (x=65, baseline y=369.54) line ending …季節で vs B1 column (x=527) な声… Inherited from the JA core by every shipped JA fan-out; earlier "visually clean" adjudications of these flags were wrong and are superseded.

**Diagnosis.** The wrap width metric is correct (PIL, Noto Serif CJK JP; every greedy pre-kinsoku line fits the 434-unit column). The defect is in the kinsoku oidashi loop in `svglib.py` `wrap()`: pulled glyphs are never re-measured, and a line starting with a NO_START chain pulls one glyph per pass — B1's line cascaded 3 pulls (』→！→な) to 23 glyphs = 491.92 units (+57.92 over the limit; ≈30 units of ink past the 462-unit column pitch), A2's line cascaded 2 pulls to 471.28 (+37.28; ≈9 units past the pitch). A programme-wide census of the core found 16 overfull lines; only these 2 exceed the 28-unit gutter (all others ≤17.50 over, ink inside the gutter, shipped and audit-clean).

**Fix (identical in all 7 JA build dirs; patched `svglib.py` md5 d73e23b365676c3618d7e060b835eb4d in each).** New module constant `SEAM_SLACK = 28` (grid pitch 462 − column width 434). `wrap()` now records pre-kinsoku line widths and, after the oidashi loop, repairs ONLY lines oidashi itself grew past `max_w + SEAM_SLACK`: trailing glyphs are shed to the head of the next line until the line fits `max_w` again (cascading forward; a NO_START glyph is shed together with the preceding glyph so no line starts with one). No content string changed; no other wrap result in the issue changes (verified below).

**Verification (this edition).** Pages 1–6 and 8 SVGs byte-identical to the previously shipped files. P7 SVG differs in exactly 4 text elements — the two seam line pairs, at unchanged coordinates (A2 lines at y=369.54/402.22: …本を読む季節で→…本を読む季 / す。→節です。; B1 lines at y=336.86/369.54: …スタジアムで大き→…スタジアム / な声が聞こえます。→で大きな声が聞こえます。); concatenated text identical on all 8 pages; exercise registry unchanged (150). Geometric occlusion audit (ink-extent, synthetic positive control passed): flags 20 → 18, the delta being exactly the two P7 TEXTX seam flags removed, zero new flags. Pixel check on the rendered P7 card: seam (a) B1 ink now ends at column 962, B2 ink starts 994 (31 clear columns); seam (b) A2 ink ends 502, B1 ink starts 528 (25 clear columns) — glyphs no longer touch at either seam.

**Pins.** Web PDF: 3,117,923 B / sha256 576ab24ff2a8c097087634fe6f73192a94be6a5f3e5d8babe2540aaff2c1af83 → **3,118,400 B / sha256 54a60a46fb02e03d3c05edd3d5424a67af51c69c5d06aafc45ff568c3b946b64**. Print PDF: 41,112,807 B → 41,112,804 B. Repo re-pin by the main line.

---

## D5 rebuild (2026-11-13)

SOP §1.1 字体修复（D5）：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP。施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-en/`；逐版报告：`production/notes/2026-w43/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w43-ja-en.md`。

**装机**：移植模板路线（D5-METHOD §1.7；安装器拒单已实测，见家族报告 §3–§4）。本版 svglib 取 `svglib-ja-d5.py`，`_D5_READER = "latin"`，与 W47 对应模式参照逐字节相同；`test_d5_routing.py` FAILURES: 0；fix2 + kinsoku 齐全。

**基线**：run TOTAL 150；SVG 8/8 与 fanout 相同；印 PDF 40,781,467 B；pdfdiff vs 已发件 IDENTICAL 8/8；修前普查 D5 拉丁 415。

**门禁**：17 门 + D18 中 16 门 + D18 全绿——run 150 / head_check 0 / d5 census 0 / render RC=0 / webpdf RC=0（2,522,480 B）/ occlusion 0 / p8 extract 150/150 / p8 compare CLEAN（keydiff [137, 138]）/ freeze baseline 8/8 / freeze diff 新增 CJK 0 / spill 0 / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects（P8 192→192 行，slack 47.9px）/ print=web 文字层差 0 / census_quotes 0 defective / 刊头间距 306.5px PASS。门 15b `verify_textmd.py` carryover FAIL 为工具-格式口径差（基线同跑亦 FAIL；权威证据为 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）。

**新交付物（实测值）**：印 PDF `Lucerna-VOL1-EN.pdf` 37,480,479 B / SHA-256 `4e681cf14853586df7f35b728c8e04219e1113809a909d58627933a89c60f929`；网 PDF `2026-w43-ja-en.web.pdf` 2,522,480 B / SHA-256 `d8f7700aef8fbcdd19c326aabbde14ea76c2c3333a25df72503888bab55736d9`（D5 前已发版 2,694,526 B，`3531bf6d885c…`）；text.md **新建** 45,691 B / SHA-256 `ff3ae1df8850b879adf90421c69d123209f127a3d1dffc3777b2055a4a477885`。
