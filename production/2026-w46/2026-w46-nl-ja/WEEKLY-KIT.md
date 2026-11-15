# WEEKLY-KIT — De Lucerna · オランダ語週刊 VOL.3 · NL × JA

Edition slug: `2026-w46-nl-ja`. Issue week: Mon 9 Nov – Sun 15 Nov 2026
(frontmatter week `2026-W46`, weekStart `2026-11-09`, weekEnd `2026-11-15`).
VOL.3. Dutch target text frozen from the W46 NL core; explanation layer in
Japanese. Built by the W46 NL builder; insert is the coordinator's job.

## 1. Topics and sources

Same verified fact base as the W46 NL core and the NL × EN edition (see
`files/weekly-report-w46-nl-en/WEEKLY-KIT.md` §1): Sinterklaasjournaal
from 9 Nov, national arrival Grave 14 Nov, 88th Amsterdam arrival 15 Nov,
Sint-Maarten 11 Nov, Oranje Nations League vs Greece (13 Nov) and Germany
(16 Nov preview), Heel Nederland Leest (`Het diner`, Herman Koch),
Expeditie Robinson (Sundays 20:00 RTL 4). No invented polls, quotes,
accounts or results; no squad names used. Weekdays verified
`TZ='Europe/Amsterdam'`. Sinterklaas in Japanese: シンタクラース.

## 2. Promises honoured (from W45 NL VOL.2)

Sinterklaas arrival Amsterdam 15 Nov and Sint-Maarten 11 Nov are the lead
topics. Readers' corner: no real letters or best page-8 texts had arrived
at press time — labelled editor's example + on-page disclosure in Dutch
and Japanese (`締切時に本物の手紙と8ページの優秀作文はなく、編集部の例文を掲載。約束はVOL.4へ。`);
promise carried forward to VOL.4. No fabricated readers, letters, names
or quotes anywhere.

## 3. Structure and counts

8 pages, 1950×2700, 4 columns. Exercises by page: 10 / 18 / 18 / 18 / 18 /
18 / 12 / 38 = 150 total. By level: A2 47 / B1 72 / B2 31. Model essay
89 words. P6 chart explicitly labelled practice data (練習データ):
invented numbers for 100 young people, not a real survey.

## 4. Furniture (W43/W45 NL × JA measured, shipped)

- Top strip: `ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む`.
- Subtitle uses SPACED kana at 40pt: `オ ラ ン ダ 語 週 刊 · VOL.3 ·
  SINTERKLAAS · SINT-MAARTEN · ORANJE` (measured 1387.5px < 1820, fits).
- Pairing badge REPLACES the strapline at y=372, 19.5pt bold BRICK, JP
  font: `オランダ語テキスト · 日本語の解説 — 日本語読者のための版`
  (measured 541.8px, fits).
- Footer: `De Lucerna · オランダ語週刊 VOL.3 · 本文はオランダ語 · 解説は日本語`
  + `N ページ（全 8 ページ）`. Gloss prefix `解説 — `. Glosses: Dutch +
  space + Japanese, items joined by ` · `. P7 bridges use `；` separators
  and `：` for examples. P8 notes use ` = ` with FULL-WIDTH parentheses
  （） — 0 half-width `(` in Japanese strings (the 13 half-width `(` in
  the P8 SVG are all frozen Dutch multiple-choice option groups, also
  present in the core). P8 separator `— {pg} ページ —` (separator TEXT
  only). P7 quote page tags stay Dutch `(Pagina N)`.
- P8 sizes stay at CORE values (Flow bottom 2552, separators 14pt/1.16/2,
  keys 13.5pt/1.16/0.5). `bridge()` renamed to `expl()` (signature
  unchanged; expl strings carry their own `解説 — ` prefix where needed,
  P7 a/b/c expl strings have none). svglib: JP face (`endswith("JP")`,
  Noto Serif/Sans CJK JP) + kinsoku wrap patch (NO_START closers, oidashi
  + seam repair, SEAM_SLACK = 28) — copied from the W45 JA build after
  the transform; diff vs core svglib is ONLY those two hunks (45 lines).
- Registry labels: type tokens TRANSLATED to Japanese (穴埋め選択,
  文の完成, 対応付け, 正誤判断, 選択問題, 文を作る, 翻訳, 作文);
  instruction words localised (空所補充, 正誤, 文を作る, 作文, 翻訳;
  per-direction `日本語に訳す` / `オランダ語に訳す`, 2× each; match
  instr `語と意味を結ぶ`). The disclosure variable is `dt_ja`.
- P7 word-box: Dutch definition sentence verbatim; only the gloss line
  below is Japanese. Clinic Dutch wrong/right sentences verbatim; notes
  in Japanese. Translation items 137/138 re-aimed NL→JA (keys are the
  Japanese translations); 139/140 prompts re-aimed JA→NL (keys stay
  Dutch).

## 5. P7 golden sentences

8 sentences, each verbatim from this issue's own articles. Glosses in
Japanese with Dutch `(Pagina N)` page tags kept.

## 6. Images (PD/CC0, Wikimedia Commons Artist credits, verified 2026-10-21)

Reused from the W45 build assets, no new downloads: P1 `westertoren.jpg`
(Wim van Rossem / Anefo, Nationaal Archief, CC0); P2 `kinderdijk.jpg`
(Nationaal Archief, CC0); P3 `gracht.jpg` (W. Punt / Anefo, Nationaal
Archief, CC0); P4 `elftal1912.jpg` (Spaarnestad Photo, public domain).
P5 no photo. Credits printed under each photo.

## 7. Build / repro

Build dir: `hidden_files/weekly-report-w46-nl-ja-build/` (copied from the
W46 core build dir, never from W45 content). One-off `transform.py`
generated from the EN rep pairs by mapping every EN string to Japanese
(`gen_ja.py`, kept at `hidden_files/w46/gen_ja.py`; 334 replacements,
FAILED: 0; the pairs file `hidden_files/w46/en-reps.txt` was re-extracted
from the shipped EN transform after a /tmp wipe — 265 pairs, exact EN
wording incl. `Translate into English/Dutch` refinements and `True:`/
`False:` forms). Freeze baseline before transform: 8/8 byte-identical,
core untouched. Transform run ONCE per fresh copy (the badge-insert rep
doubles the badge on a second run — FR lesson). After the transform, the
W45 JA `svglib.py` was copied over the build dir's `svglib.py`. Build:
`run.py` (one process) + `render.py` (cards + print PDF). Web PDF via
`tools/webpdf.py`.

Files in this edition dir: `svg/`, `cards/`, print PDF
`De-Lucerna-VOL3-JA.pdf` (10,702,606 bytes; SHA-256 `8ae383d5adb1660e1e86727e2c7287a321ff6ca941b930d23826ead062fb1f08`), web PDF
`2026-w46-nl-ja.web.pdf` (1,073,941 bytes, 37,811 text bytes; SHA-256 `bf75a711695d8dfa05f1cd3e833c4ec089644d039330a4eebbf37a1424a4302b`),
`WEEKLY-KIT.md`, `ABSTRACT.txt`, `2026-w46-nl-ja.text.md` (D5 rebuild export, `logs/2026-w46-nl-ja/2026-w46-nl-ja.text.md.run2`; the `production/` same-named file is the 2026-11-06 fanout product, do not use).

## 8. Fix record (W46 JA)

- Fix 1 — P7 stack graze (visual check): the letters-box bottom edge sat
  on the gold rule (1957.0 vs 1937). Invitation shortened to one line
  (`編集部の例文です。送ってください！`); stack ends 1928.0, same as core.
- Fix 2 — P1 COVER (visual check; the scans missed it): the Japanese
  word-of-the-week gloss ran 2 lines, its second line falling under the
  IN HET KORT box (drawn later). Shortened to one line:
  `「de intocht」：祝祭の到着行列。` Crop re-checked clean.

## 9. Gates (2026-11-02, recorded in `hidden_files/w46/nl-gates.log`)

- Builder self-check: TOTAL 150, by page 10/18/18/18/18/18/12/38, zero
  FLOW OVERFLOW / HEAD TOO WIDE.
- `occlusion_audit.py`: selftest OK, edition 0 flags, core 0 flags,
  NEW vs core: 0.
- Same-baseline furniture scan (rowcheck.py): all 8 pages CLEAN; P6
  chart-label GRAZE coverage 0.0%; gloss counts core-vs-edition OK
  (6/5/5/5/5).
- `freeze.py diff` (non-strict; strict-CJK is inapplicable — Japanese
  legitimately adds CJK): exit 0; added CJK 3,340 chars adjudicated
  per-char (measured on the final Round 3 artifacts; Round 2 measured 3,341 before the N-1 core fix added 到 to the core CJK multiset, netting one fewer added char); every added CJK character is from the authored Japanese
  strings (kana, kanji, 、, and the Japanese punctuation ～ ？ ／ 々 ＋);
  0 Chinese characters added.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138]
  (legal re-aims: keys are the Japanese translations).
- Kinsoku scan (gates.sh --ja): 0 line-start hits; P8 half-width `(` = 13
  (all frozen Dutch option groups, adjudicated), full-width （ = 21.
- Web PDF: 1,375,362 bytes (<7 MB), 47,973 text bytes (>0).
- Visual check: P1 viewed clean (badge replaces strapline, spaced-kana
  subtitle, word gloss 1 line after Fix 2); P7 letters-box crop viewed
  (Fix 1 verified: clean gap above the rule).

## 10. Reader-facing sweep

No internal labels, version codes, language codes, repo links, or producer
language on any page. Cover carries masthead + plain date + story grid
only, no interactive elements. Explanations fully in Japanese; Dutch
target text untouched except the re-aimed translation items.

## 11. Open items

None for this edition. Whether the coordinator wants a separate
`files/weekly-report-w46-nl-zh-cn/` dir in addition to the core dir is
flagged in the builder's final report (W45 precedent: core dir IS the
zh-cn edition; no separate dir built).

## Fix record — Round 1 proofread defects (fix worker, 2026-11-03 UTC)

Independent proofreader Round 1 verdict: FAIL (F-1, F-2a, F-2b, E-1, E-2, E-3). All fixes below were made at the source and fully re-rendered; no SVG/PDF was hand-edited. Full evidence: `hidden_files/w46/nl-fix/` (FIX-REPORT.md, build logs, gate JSONs). A full Round 2 independent proofread follows; this record is not a substitute for it.

- F-1 (all 11 editions): `ABSTRACT.txt` closing rewritten from news framing to practice framing, rest of the abstract verbatim, single line, 0 ASCII quotes. Before tail: `ションズリーグ・ギリシャ戦とドイツ戦。オランダ語本文・日本語解説、A2～B2レベル、150問の練習でオランダのニュースからオランダ語を学ぶ。` After tail: `オランダ代表のネーションズリーグ・ギリシャ戦とドイツ戦。オランダ語本文・日本語解説、A2～B2レベル、今週の話題を素材にした150問の練習。`
- F-2a/F-2b: inherited from the fixed frozen core by re-derivation: this edition's one-off `transform.py` old-strings were updated to the new core strings and the build was re-derived from the fixed core (FAILED: 0). Source diff vs the pre-fix build: 0 lines (byte-identical to the pre-fix build sources).
- Record correction: this KIT's freeze total 3,377 is stale; the measured added-CJK total on the final Round 3 artifacts is 3,340 (Round 2 measured 3,341; the N-1 core fix added 到 to the core CJK multiset, netting one fewer added char).

Re-gate evidence (final artifacts, 2026-11-03 UTC; logs/JSONs under `hidden_files/w46/nl-fix/`):
- Counts re-measured: TOTAL 150; per page 10/18/18/18/18/18/12/38; A2 47 / B1 72 / B2 31 (text.md bracketed 142 + 8 range-header items; SVG stems 142, per page 10/14/18/18/18/18/12/34).
- Freeze (`freeze.py diff`): added CJK 3,341 (kana/kanji + Japanese punctuation only); exit 0.
- `p8.py compare`: CLEAN, core 150 = edition 150, keydiff=[137, 138] (legal re-aims).
- `occlusion_audit.py`: selftest OK; edition-alone 0 flags; NEW-vs-core 0 new flags (core: edition-alone 0 flags). Exit 0.
- Lone-`。`/stranded-number scan (all 8 pages): 0 lone-`。` elements, 0 line-start-`。` elements, 142 exact `N.` stem elements at stem x-coords, 0 stranded numbers.
- Gloss counts P2–P6: 6/5/5/5/5, identical Dutch headwords in order. P6 chart bars measured: widths 160/100/80/60 (values 40/25/20/15), fill `#3e4c2a`, identical in all 11 editions. P7: 8/8 golden sentences verbatim; page tags in order Pagina 1,1,2,3,4,5,6,6. Model essay 89 words; chart-answer arithmetic spot-verified (40+25+20+15=100).
- Final inventory: `.text.md` 33220 bytes; web PDF 1375362 bytes, pdftotext 47973 bytes (>0), 8 pages, 1462.5×2025 pts, ≤7 MB; print PDF 19287942 bytes; web-vs-print extracted text 0 diff tokens; cards 1950×2700; 0 FLOW OVERFLOW / HEAD TOO WIDE warnings.
- No other changes were made. Observations O-2–O-5: no action, per coordinator rulings.

## D5 rebuild (2026-11-15, W46 nl family)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --week 2026-w46` (`--check` dry-run first, all clean). Mode: cjk. `_D5_READER` at `svglib.py:100` = `cjk`; fix2 retained (`_QUOTE_CLS` x4 per file); `test_d5_routing.py` FAILURES: 0.
- Pre-fix D5 census (baseline): D5 Latin 323. Baseline: run TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print/web text layers vs shipped PDF stripped-diff 0; `issues/` pin matched; text.md BYTE-IDENTICAL vs `issues/`.
- Fixes (all font-size reductions, zero copy changes; probe = SVG-measured ink width, largest size leaving >=2px slack):
  - P2 head `DRIE DINGEN VOOR 11 NOVEMBER` — content12.py:175, head 25→22pt (ink 471.1→414.5px, slack 8.0)
  - P1 numbers box title `DE WEEK IN CIJFERS　数字で見る今週` — content12.py:48, f.box tsize 23→20.5 (ink →394.5px, slack 10.0)
  - P6 `DE GRAFIEK　グラフ（練習データ）` — content56.py:142, p.text 24→22pt (ink →390.6px, slack 9.9); ### line lost, see blocker
- P8 (run2): lines 224/224, max ink bottom 2551.5, slack to footer rule 2596 = 44.5px, slack to page bottom 2700 = 148.5px; `p8.py compare` CLEAN, keydiff=[137, 138].
- Pins (run2, final): print PDF `De-Lucerna-VOL3-JA.pdf` 10,702,606 bytes, SHA-256 `8ae383d5adb1660e1e86727e2c7287a321ff6ca941b930d23826ead062fb1f08` (baseline 18,688,956 bytes, `3c0f44d6c949b95cce9234358c50fb07b951f166c35e94b0e45e2833cc1360f6`); web PDF `2026-w46-nl-ja.web.pdf` 1,073,941 bytes, SHA-256 `bf75a711695d8dfa05f1cd3e833c4ec089644d039330a4eebbf37a1424a4302b` (baseline 1,289,644 bytes, `1b49dad909a514c12e7628150947880ed0ccfb76270994b33f620d5f516d3ee3`); text.md 42,197 bytes, SHA-256 `15bfe2c3a49eacc7e4a84426742637febd58efcf32295aa8f8a16148d8d37a29` — BYTE-IDENTICAL vs shipped (D47 補行后; G15a/G15c 针对性重验通过)
- Gates run2: 17/19 (G15a FAIL + G15c HOLD, exporter 24pt ### threshold; all other 17 gates PASS). G15b record-only (D27). Full gate log: `logs/2026-w46-nl-ja/GATES-SUMMARY-run2.txt` in scratch `hidden_files/d5-redo/scratch-2026-w46-nl/`. Family report: `hidden_files/d5-redo/FAMILY-W46-NL-BUILD.md`.
