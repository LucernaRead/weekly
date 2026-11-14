# Lucerna 日本語版 · Japanese Weekly — VOL.1 · Édition française (JA × FR) Production Kit

Week: **Monday 19 – Sunday 25 October 2026** · Pairing: **Japanese target text (frozen core) + explanations written natively in French** — Japanese articles byte-identical to the core; definitions, grammar notes, instructions and ALL P8 answer notes fully in French.

Core: `files/weekly-report-ja-vol1/` (build `hidden_files/weekly-report-ja-build/`).
This edition's build: `hidden_files/weekly-report-ja-fr-build/` (content12.py, content34.py, content56.py, content7.py, content8.py, bslib4.py, svglib.py, render.py, run.py, audit_ja_fr.py, audit_titles.py, assets/ + CREDITS.md).
Deliverables here: `svg/` (8), `cards/` (8 PNG @1950×2700), `Lucerna-VOL1-FR.pdf` (print, 8 pp, 42,023,248 B, sha256 5de33963cc10677f14199e2ff8c3125ed6ad83a7c3000c418d7ba6f5743653c5), `Lucerna-VOL1-FR-web.pdf` (web, 8 pp, **3,197,062 B**, sha256 e33de9f34c6d247f0f62dbd05b23faf2dbbe0a230174ead9ca406ab4c1679f44 — under the measured ~10 MB server limit).

## 1. Baseline proof (fan-out method step 1)

The unmodified copy of the core build dir reproduced **all 8 shipped core SVGs byte-identically** (sha256 compared one by one: p1-hyoushi … p8-tesuto — 8/8 IDENTICAL) before any edit was made. All subsequent baselines, freeze diffs and the key-diff registry are against the CORE's shipped SVGs, never against a sibling edition.

## 2. Spec (per SOP)

- 8 pages (multiple of 4 ✓), 1950×2700 units, 4 columns, warm ivory `#f7f1e2`, deep olive accents (`#3e4c2a`), brick chips — all inherited unchanged from the core.
- Masthead: blackletter **Lucerna** with **NO article** (Japanese is article-less, SOP masthead rule).
- Ramp and per-item level badges inherited from the core; every exercise individually badged [A2]/[B1]/[B2].
- The SOP-banned intermediary-layer term appears NOWHERE in the pages, this KIT, or the build code (checked programmatically in code and in the final SVGs: 0 occurrences, both language forms; the inherited explanation method is renamed `expl()`).
- Weekday/date claims re-verified against the real 2026 calendar: Oct 17 Sat, 18 Sun, 19 Mon, 20 Tue, 22 Thu, 23 Fri, 24 Sat, 25 Sun, 27 Tue, 31 Sat, Nov 9 Mon — all French notes agree (Japan Series G1 = Saturday Oct 24, 18:30, DeNA vs SoftBank ✓).

## 3. Measured totals (visible-text extraction from the final SVGs, same method as the core KIT)

- **Characters: 22,566 (no spaces) / 25,631 (with spaces)** — higher than the core's 18,508 with spaces because the French apparatus is fuller than the core's Chinese apparatus; the Japanese layer is unchanged. Per page (no-space/with-space): P1 2136/2335 · P2 2200/2398 · P3 1949/2166 · P4 2298/2492 · P5 1962/2121 · P6 1836/1985 · P7 2555/2844 · P8 7630/9290.
- **Exercises: 150 exactly** — identical to the core.
  - By level: **A2 48 · B1 75 · B2 27** (identical to core).
  - By page: P1 10 · P2 18 · P3 18 · P4 18 · P5 18 · P6 18 · P7 12 · P8 38 (identical to core).
  - By type (French names ← core types): Compléter 51 · Choix multiple 50 · Texte à trous 13 · Appariement 12 · Vrai ou faux 11 · Former une phrase 8 · Traduction 4 · Rédaction 1 — a 1:1 mapping of the core's type counts.
- P8 writing model 『私の秋の週末』: **150 characters** (unchanged Japanese, counted programmatically).
- P6 practice chart unchanged: 車いすテニス 34% · 水泳 28% · 陸上 22% · その他 16% = 100%.

## 4. Registry & key-diff vs the CORE

Both registries regenerated from the build code and compared programmatically: **n / page / level identical for all 150 exercises; all 150 answer notes changed (Chinese → French)**. Key changes — complete list (3):

| # | Core key | FR key | Why |
|---|----------|--------|-----|
| 137 | 游行队伍12点从京都御苑出发。 | Le cortège part du jardin impérial de Kyoto à 12 h. | JA→reader-language translation exercise, re-aimed at French. Note: «Voir page 3» |
| 138 | 乱扔垃圾，要罚2,000日元。 | Jeter des déchets coûte 2 000 yens d'amende. | Same re-aim. Note: «Voir page 5» |
| 150 | （开放题，范文如下） | (question ouverte — modèle ci-dessous) | Apparatus line of the writing exercise. Note: «Modèle dans la section H de cette page (150 caractères)» |

#139/#140: their **stems** are re-aimed into French («La Semaine de la lecture commence mardi prochain. → ___»; «Je veux aller à l'événement d'Halloween d'Ikebukuro. → ___»); their Japanese keys are byte-identical to the core. Every other key is byte-identical to the core; all remaining registry diffs are note-text only. French key typography: half-width parentheses only, a space before each note parenthesis.

Freeze diff of visible SVG text (core vs this edition, all 8 pages): every removed string is a Chinese explanation-layer string, a Chinese furniture label, an exercise-type/instruction label, or one of the documented items above; every added string is its French equivalent or pairing furniture. Japanese target text is otherwise byte-identical — the only layout-level differences are line-wrap artefacts of the longer French notes inside P8 key lines #133/#136 (same key strings, wrapped at a different point). Image payloads: byte-identical to the core on all 8 pages (data-URI comparison; 7 images, same files, same credits — see the core KIT §Images and build `assets/CREDITS.md`).

P7 phrases of the week: each of the 8 Japanese phrases occurs **exactly 2×** in the whitespace-stripped concatenation of all SVG text (once in its article, once on P7) — verified programmatically after the final render; their French translations and «(p. N)» tags are the explanation layer.

## 5. Furniture (French column, as shipped in EN×FR / DE×FR / ES×FR / IT×FR / PT×FR / NL×FR / RU×FR)

- P1 badge (19 pt bold, brick #a4553a, JA×DE masthead geometry): «TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES» (measured 961.2 px ≤ 1820 with the build's own font metrics).
- P1 edition line: the core's Japanese line is kept («日本語版 · VOL.1 · 日本シリーズ · 紅葉 · 読書の秋»); no HEBDOMADAIRE line was needed in this layout — the pairing is badged by the line above and by every footer.
- Top strip centre: «毎週、日本語で · Chaque semaine · 日本人が読んでいる日本語を読む».
- Footers, all 8 pages: «Lucerna · HEBDOMADAIRE JAPONAIS VOL.1 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS» (measured 897.3 px, fits) / «Page N sur 8».
- Gloss boxes prefixed «Note — » (FR column convention, replacing the core's Chinese gloss prefix).
- Exercise types localized: Compléter / Choix multiple / Texte à trous / Appariement / Vrai ou faux / Former une phrase / Traduction / Rédaction; instruction labels: Complétez / Vrai/faux / Formez la phrase / Traduisez; matching instructions in full French sentences.
- Band subtitles, box titles, section heads: Japanese + French pairs throughout (e.g. «トップニュース · À la une», «練習 · Exercices · page N», «答え · Réponses — classées par page, cherchez le numéro», keys grouped under «— Page N —»).

## 6. Fit shortenings (French apparatus only — no core geometry or Japanese moved)

Found by the geometric/title audits (§7) and fixed in the sources, then re-rendered and re-audited:

1. P1 numbers-box title «数字で見る今週 · La semaine en chiffres» ink ended at x=981, past its box border (961) → shortened to «数字で見る今週 · En chiffres».
2. P2 usage-box title «『見頃』の使い方 · Comment employer 見頃» ink to x=1029 vs border 961 → «『見頃』の使い方 · L'emploi de 見頃».
3. P4 schedule-box title «日本シリーズの日程 · Le calendrier des matchs» ink to x=1055 vs border 961 → «日本シリーズの日程 · Calendrier».
4. P7 clinic title «まちがい診療所 · Le cabinet des erreurs» ink to x=1907 vs border 1885 → «まちがい診療所 · Erreurs fréquentes».
5. P7 frame title «今週のフレーム · La structure de la semaine» ink to x=1954 — past its box border AND the page edge (1950) → «今週のフレーム · Modèle de phrase» (final ink ends ≈1862).
6. P1 word-of-week French gloss wrapped to two lines; the second line («admirer.», baseline 1856) was struck through by the row-B rule at y=1844 — pixel-confirmed on the rendered card (the rule crosses the ascender of the «d»). Shortened to one line: «見頃 (migoro) = le meilleur moment.» (wrap check: 1 line at 19 pt in 434 px). Same slot and geometry as the core's one-line Chinese gloss.

## 7. Geometric occlusion audit (mandatory gate — builder's run)

Script: `audit_ja_fr.py` (paint-order coverage with real-font PIL metrics via the build's svglib; line boxes expanded by half the stroke width) + `audit_titles.py` (box titles vs their own box borders). The audit script was first validated on a synthetic positive control (a covered text, a thin-line crossing, a footer-band intrusion — all 3 fired; a clean text did not).

Final run on the shipped SVGs: **0 COVER, 0 FOOTER, 0 EDGE, 0 TITLE flags.** One LINEX flag remains and is adjudicated a **non-defect** by pixel measurement:

- P2 model sentence (baseline 1800) vs the exercise-section rule at y=1804: the flag comes from the audit's generic ink band (+0.30 em). Measured on the rendered card, the sentence's actual glyph ink ends at row **1801** and rows 1802–1811 are empty — the rule at 1804 touches no ink (3 px clear). The geometry is byte-identical to the shipped core, which carries the same band relationship.

All 8 card PNGs were viewed page by page in the builder's pass (masthead/badge, boxes, images, keys, footers).

## 8. Builder's proofread (full pass)

- Freeze diff (core vs FR, visible text, all 8 pages) reviewed line by line: changes confined to the explanation layer + furniture + documented items (§4).
- Registry comparison (§4): numbering continuous 1–150, no gaps or duplicates; levels/pages/types as §3.
- All 150 French notes read against their stems and the article text; every glossed word verified present on its own page (unchanged from the core's verified set — only the gloss language changed).
- Dates/weekdays re-verified (§2); arithmetic inherited from the core and re-checked where a French note restates it (671+671 = 1 342; 34+28 = 62; 22−16 = 6; 1 min 46 s = 106 s; 91/140 = .650).
- Residual-language scan of the final SVGs: no Chinese explanation strings remain; the only simplified-form characters present are legitimate Japanese shinjitai inside Japanese text （写真 in photo credits, 点 in scores, 声 in 声援）. Banned term: 0 occurrences in pages, KIT and code.
- No FLOW OVERFLOW and no HEAD TOO WIDE warnings in the final build; P2 col-3 stack ends at y=1550.4, 3.6 px clear of the season-words rule at 1554 (tight but non-touching, confirmed on the card); P8 keys end at y=2457, well clear of the footer rule.

**Proofread status: builder's full pass complete. INDEPENDENT PROOFREAD: PASS — see §8.1.**

## 8.1 Independent proofread record (2026-10-21, fresh proofreader, not the builder)

One complete independent pass over the shipped files — **zero problems found; nothing was fixed and nothing re-rendered.** The edition is final as shipped.

- **Reproducibility / baseline**: both builds were re-run from source in an isolated copy — the core build reproduces all 8 shipped core SVGs byte-identically, and this edition's build reproduces all 8 shipped FR SVGs byte-identically. The builder's baseline claim is therefore verified, not trusted.
- **Freeze diff vs CORE** (node-level text multiset, all 8 pages, independently extracted): every removed string is a Chinese explanation-layer string, a Chinese furniture label, or an exercise-type/instruction label; every added string is its French equivalent or pairing furniture. No Japanese target-text change outside the §4 registry. The claimed #133/#136 artefacts are confirmed as note wrap-segmentation only — both Japanese keys stand complete on their first key line (the stray nodes are the French note wraps «verbe» / «した», plus «lecture», «Angeles», «2028», «3» wraps of notes #132/#87/#97/#137 and the #140 note parenthesis). Shape elements differ from the core only where the longer French apparatus resizes its own boxes (Note boxes 115.95→145.68 tall, «あなたは？» boxes taller, P1 masthead rules −14 px, P7 right-column flow +29.7 px) — shape counts per page are identical and no Japanese text block is covered or displaced into another element (see the geometric audit below).
- **French apparatus completeness**: residual-Chinese scan of the final SVGs (text layer) finds no Chinese explanation strings; the only simplified-form glyphs present are Japanese shinjitai inside Japanese text （国・来 in 国立・来週 etc.). Every gloss, instruction, box title and all 150 P8 answer notes are in French; French key typography = half-width parentheses with a space before each note parenthesis.
- **Answer keys re-derived independently**: all 150 keys were re-solved from the printed Japanese articles/stems/options (not copied from the core) — 150/150 agree with the printed keys. Registry re-derived from both builds' code and compared programmatically: n / page / level identical for all 150; key differences are exactly #137, #138, #150 (the §4 registry is complete — no undocumented key changes); type differences are only the 1:1 French localization of the 8 type names with identical counts (51/50/13/12/11/8/4/1); all 150 notes differ (Chinese → French) as designed. #139/#140 stems are re-aimed into French and their Japanese keys are byte-identical to the core and correct. Translation keys verified faithful against the printed Japanese stems: #137 «Le cortège part du jardin impérial de Kyoto à 12 h.» = 行列は京都御苑を12時に出発します。; #138 «Jeter des déchets coûte 2 000 yens d'amende.» = ゴミを捨てると、2,000円の罰金です。
- **Totals**: 150 exercises — A2 48 · B1 75 · B2 27; by page 10/18/18/18/18/18/12/38; numbering 1–150 continuous in the rendered pages and in the P8 key list. P8 model essay re-counted: exactly 150 characters. P6 chart values 34/28/22/16 = 100.
- **P7 phrases**: all 8 Japanese phrases occur exactly 2× in the whitespace-stripped whole-issue text (article + P7), each on its tagged page, with French translations and correct «(p. N)» tags (1, 1, 2, 2, 3, 4, 5, 6).
- **Weekdays/dates**: every claim checked against the real 2026 calendar — Oct 17 Sat, 18 Sun, 19 Mon, 20 Tue, 22 Thu, 23 Fri, 24 Sat, 25 Sun, 27 Tue, 31 Sat, Nov 9 Mon — all correct in the Japanese text and in the French notes (Japan Series G1 = Saturday Oct 24, 18:30, DeNA vs SoftBank ✓).
- **Furniture**: P1 badge present («TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES»); all 8 footers carry the pairing line and «Page N sur 8»; masthead is «Lucerna» with NO article (no «Le Lucerna» / «The Lucerna» anywhere).
- **Geometric occlusion audit (proofreader's own implementation, production PIL font metrics, line boxes expanded by half the stroke width, union-area coverage)**: validated first on synthetic positive controls (100%-covered text, thin-line crossing, footer-band intrusion, title spill — all 4 fired; clean text did not). Result on the shipped SVGs: **0 COVER, 0 FOOTER, 0 EDGE, 0 TITLE flags**; the 5 shortened box titles of §6 re-measured individually and all sit inside their box borders (P1 «数字で見る今週 · En chiffres», P2 «『見頃』の使い方 · L'emploi de 見頃», P4 «日本シリーズの日程 · Calendrier», P7 clinic «まちがい診療所 · Erreurs fréquentes», P7 frame «今週のフレーム · Modèle de phrase»). One LINEX flag — the known P2 adjacency (model sentence baseline 1800 vs the rule box at y 1803–1805) — pixel-adjudicated on the rendered FR card: the sentence's ink ends at row 1801 and rows 1802–1816 contain zero dark pixels in the sentence's span, a row profile identical to the shipped core's card → the rule touches no ink, **non-defect**. The §6 P1 gloss fix is likewise pixel-verified: the gloss «見頃 (migoro) = le meilleur moment.» is a single line whose ink ends at row 1834, ≥10 px clear of the y=1844 rule zone, with no second line below.
- **Images & PDFs**: image payloads byte-identical to the core on all 8 pages (7 images); printed credits match the placed images and the core KIT's verified PD/CC0 record (Syced CC0; Poliphilo CC0; Fumikas Sagisavas CC0; Hiroshige III PD; Bain News Service PD; Petr Kratochvil PD; EJ Hersom / US DoD PD); build `assets/CREDITS.md` identical to the core's. Web PDF independently measured: **3,197,062 B, sha256 e33de9f34c6d247f0f62dbd05b23faf2dbbe0a230174ead9ca406ab4c1679f44** (matches the KIT header; < 10 MB); web and print PDFs both 8 pages.
- **Banned-term scan**: the SOP-banned intermediary-layer term (Chinese and English forms) = 0 occurrences in the paper's SVGs, this KIT, and the build code.

**Verdict: PASS — the independent zero-problem gate is met. This edition is cleared for repo insertion by the parent agent.**

## 9. Reproduction

```
cd hidden_files/weekly-report-ja-fr-build
python run.py        # writes svg/ into files/weekly-report-ja-fr/svg, prints registry stats
python render.py     # cards/ PNG @1950×2700, print PDF, web PDF (JPEG q85 @1400px)
python audit_ja_fr.py  ../../files/weekly-report-ja-fr/svg   # (path as given in build dir)
python audit_titles.py ../../files/weekly-report-ja-fr/svg
```

Delivery (per the 2026-10-21 ruling): GitHub weekly repo only, by the parent agent after the independent proofread; Discord delivery is paused; nothing was posted or inserted by the builder.

---

## Patch note — 2026-10-21 · Core-level correction: P7 vocabulary-deck column-seam overprints (geometry only)

**Defect (found by the JA×PT independent proofread, §13; record: hidden_files/ja-p7-overprint-correction.md).** Two frozen Japanese lines on P7 wrapped past their column and overprinted the neighbouring column's first glyph, producing merged illegible glyphs: (a) B1 column (x=527, baseline y=336.86) line ending …スタジアムで大き vs B2 column (x=989) という意味です…; (b) A2 column (x=65, baseline y=369.54) line ending …季節で vs B1 column (x=527) な声… Inherited from the JA core by every shipped JA fan-out; earlier "visually clean" adjudications of these flags were wrong and are superseded.

**Diagnosis.** The wrap width metric is correct (PIL, Noto Serif CJK JP; every greedy pre-kinsoku line fits the 434-unit column). The defect is in the kinsoku oidashi loop in `svglib.py` `wrap()`: pulled glyphs are never re-measured, and a line starting with a NO_START chain pulls one glyph per pass — B1's line cascaded 3 pulls (』→！→な) to 23 glyphs = 491.92 units (+57.92 over the limit; ≈30 units of ink past the 462-unit column pitch), A2's line cascaded 2 pulls to 471.28 (+37.28; ≈9 units past the pitch). A programme-wide census of the core found 16 overfull lines; only these 2 exceed the 28-unit gutter (all others ≤17.50 over, ink inside the gutter, shipped and audit-clean).

**Fix (identical in all 7 JA build dirs; patched `svglib.py` md5 d73e23b365676c3618d7e060b835eb4d in each).** New module constant `SEAM_SLACK = 28` (grid pitch 462 − column width 434). `wrap()` now records pre-kinsoku line widths and, after the oidashi loop, repairs ONLY lines oidashi itself grew past `max_w + SEAM_SLACK`: trailing glyphs are shed to the head of the next line until the line fits `max_w` again (cascading forward; a NO_START glyph is shed together with the preceding glyph so no line starts with one). No content string changed; no other wrap result in the issue changes (verified below).

**Verification (this edition).** Pages 1–6 and 8 SVGs byte-identical to the previously shipped files. P7 SVG differs in exactly 4 text elements — the two seam line pairs, at unchanged coordinates (A2 lines at y=369.54/402.22: …本を読む季節で→…本を読む季 / す。→節です。; B1 lines at y=336.86/369.54: …スタジアムで大き→…スタジアム / な声が聞こえます。→で大きな声が聞こえます。); concatenated text identical on all 8 pages; exercise registry unchanged (150). Geometric occlusion audit (ink-extent, synthetic positive control passed): flags 28 → 26, the delta being exactly the two P7 TEXTX seam flags removed, zero new flags. Pixel check on the rendered P7 card: seam (a) B1 ink now ends at column 962, B2 ink starts 994 (31 clear columns); seam (b) A2 ink ends 502, B1 ink starts 528 (25 clear columns) — glyphs no longer touch at either seam.

**Pins.** Web PDF: 3,197,062 B / sha256 e33de9f34c6d247f0f62dbd05b23faf2dbbe0a230174ead9ca406ab4c1679f44 → **3,197,475 B / sha256 58a09928f2d569a4ea97d13519ebe05d000ca6dd669d24752be9b89899b6d450**. Print PDF: 42,023,248 B → 42,023,247 B. Repo re-pin by the main line.

---

## D5 rebuild (2026-11-13)

SOP §1.1 字体修复（D5）：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP。施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-fr/`；逐版报告：`production/notes/2026-w43/g-ja/scratch-d5-rebuild-ja/D5-REPORT-2026-w43-ja-fr.md`。

**装机**：移植模板路线（D5-METHOD §1.7；安装器拒单已实测，见家族报告 §3–§4）。本版 svglib 取 `svglib-ja-d5.py`，`_D5_READER = "latin"`，与 W47 对应模式参照逐字节相同；`test_d5_routing.py` FAILURES: 0；fix2 + kinsoku 齐全。

**基线**：run TOTAL 150；SVG 8/8 与 fanout 相同；印 PDF 40,853,225 B；pdfdiff vs 已发件 IDENTICAL 8/8；修前普查 D5 拉丁 420。

**门禁**：17 门 + D18 中 16 门 + D18 全绿——run 150 / head_check 0 / d5 census 0 / render RC=0 / webpdf RC=0（2,531,064 B）/ occlusion 0 / p8 extract 150/150 / p8 compare CLEAN（keydiff [137, 138]）/ freeze baseline 8/8 / freeze diff 新增 CJK 0 / spill 0 / boxtitle 0 DEFECT / edge 0 TOUCH 0 NEAR / creambox PASS 0 defects（P8 204→204 行，slack 47.9px）/ print=web 文字层差 0 / census_quotes 0 defective / 刊头间距 264.5px PASS。门 15b `verify_textmd.py` carryover FAIL 为工具-格式口径差（基线同跑亦 FAIL；权威证据为 ja 原生校验器 `verify_textexp_ja.py --edition` ADOPT，0 UNEXPECTED）。

**新交付物（实测值）**：印 PDF `Lucerna-VOL1-FR.pdf` 37,489,063 B / SHA-256 `d3b1e47f566736a19aefc6e953157afd3ea91a7693348b6876bd7b3aa71ca13d`；网 PDF `2026-w43-ja-fr.web.pdf` 2,531,064 B / SHA-256 `f5149f5b1eaae60506fc29d19529ab860ad80c1a4c40d8d9922b0a34b0849b27`（D5 前已发版 2,727,248 B，`bc1f029e71b3…`）；text.md **新建** 47,522 B / SHA-256 `85f33d40a06bc3f01e2499537d0eb4f9bd86c6e7c4deaa2c1f52ce2af31a6f57`。
