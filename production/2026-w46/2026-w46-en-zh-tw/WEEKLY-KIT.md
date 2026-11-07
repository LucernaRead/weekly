# WEEKLY-KIT — The Lucerna English Weekly VOL.3 (2026-W46) · EN × ZH-TW

- Slug week: `2026-w46` · frontmatter week `2026-W46` · issue week Mon 9 Nov – Sun 15 Nov 2026.
- Target: English (en). Reader language: Traditional Chinese (zh-tw). Edition slug: `2026-w46-en-zh-tw`. VOL.3.
- Core text frozen from `files/weekly-report-w46-en-core/` (see its WEEKLY-KIT.md for contents, trend/fact sources, images, promises). Only the explanation layer was rewritten in Traditional Chinese; English body text is byte-identical (freeze diff: 679 added CJK characters).
- Build dir: `hidden_files/weekly-report-w46-en-zh-tw-build/` (built natively in Traditional Chinese — NOT converted from Simplified: `gen_fanout.py zh-tw` first failed with 175 leftovers (MAP 95 from `kept-zh-tw.json`, 12 fragment pairs). `hidden_files/w46/authored-zh-tw.json` (163 keys) writes TC natively (e.g. 講解/譯注, 週報, 讀者, 這個, 讓, 會, 學習, 週三/週日, 慕尼黑賽, 決勝輪). Authored values verified to contain no Simplified-only characters (scan set incl. 让说这为读发国会个对话语认时电 etc. → 0 hits). Uses the W45 zh-tw svglib variant and bridge rename `expl`; pageline is None in the CFG (keeps the core page line).
- ADJUDICATION (not missed strings): 48 leftovers remain after the final run — 41 script-identical strings (value == key, e.g. `完成句子`, `填空`, `LIFE · 生活`, `fall silent = 沉寂`) plus 7 shared-glyph page-line/separator fragments (`第 `, ` 版`, ` 版 / 共 `, `第 {...} 版 / 共 {...} 版`, ` 版 —`, `— 第 `, `— 第 {...} 版 —`). These glyphs are identical in SC and TC, and the W45 EN×ZH-TW precedent keeps the page line (`第 {n} 版 / 共 {total} 版`, W45 bslib4.py line 71) and separator byte-identical. `gen_fanout.py` exit 1 here is a check artifact; the transformed dir is correct. An SC-only-character scan of the transformed sources is clean after 4 mixed-string fixes (same whole-string pattern as KO).)
- Furniture (W45 EN×ZH-TW shipped precedents, VOL.3): footer "The Lucerna · 英語週報 VOL.3 · 正文英語 · 講解繁體中文"; page line "(core page line kept: 第 {n} 版 / 共 {total} 版)"; gloss prefix "譯注｜"; P1 badge in the y=372 slot, 19.5pt bold BRICK: "英語正文 · 繁體中文講解 — 給繁體中文讀者的版本"; masthead line "英 語 週 報 · VOL.3 · 紀 念 · 足 球 · 電 影" at 46pt.
- P8 keys convention (W45 EN×ZH-TW): explicit (PRINT_SET, 70 notes). p8.py verdict: CLEAN, 70→70.

## Exercises

- Total 150 (P1 10, P2 17, P3 18, P4 18, P5 18, P6 18, P7 12, P8 39); A2 60, B1 69, B2 21 — identical numbering/levels to the core (re-measured from `hidden_files/w46/en-core/registry.json`, 150 entries, 1–150 unique); only type labels, notes and keys were translated. P8 starts at 112; dialogue 145–149; writing 150 (open). Model text "My Wednesday, November 11" = 84 words.

## Layout adjustments vs core (English text unchanged)

No layout adjustments vs core: occlusion audit clean; no string was shortened.

## Gates

- Builder self-check: PASS — final build log zero FLOW OVERFLOW / HEAD TOO WIDE warnings, 150 exercises.
- `occlusion_audit.py`: 0 flags — PASS (JSON: `hidden_files/w46/final-zh-tw-occlusion.json`).
- Supplementary scans (`hidden_files/w46/rowcheck46.py`, adapted family rowcheck: same-baseline text-ink collisions on all 8 pages, P6 chart-label GRAZE coverage, gloss-count comparison): CLEAN on all 8 pages, P6 chart-label coverage 0.0%, 0 gloss-count mismatches.
- `p8.py compare` (explicit P8 SVG paths, total 150): CLEAN, 70→70 — PASS (JSON: `hidden_files/w46/final-zh-tw-p8.json`).
- `freeze.py diff` vs core: exit 0 (plain diff, no --strict-cjk), TOTAL added CJK characters 679 — the Traditional Chinese explanation layer, expected (most strings share glyphs with the Simplified core, so the count is lower than JA/KO) — PASS (JSON: `hidden_files/w46/final-zh-tw-freeze.json`).
- Visual card pass: P1 + P8 inspected at full frame (all other pages covered by the geometric gates + same-baseline scan); no overflow/overlap, no missing glyphs/tofu, footer intact, images present with credits.
- Web PDF: `The-Lucerna-VOL3-web.pdf`, 2,204,235 bytes (< 7 MB), text layer 44,913 bytes via pdftotext. Print PDF kept: `The-Lucerna-VOL3.pdf` (24,611,428 bytes).
- `2026-w46-en-zh-tw.text.md` (43,599 bytes): exported from the fan-out source manuscript via AST (`hidden_files/w46/en_textmd.py`, never from PDF/SVG) + registry answers appended; verified byte-identical to a fresh deterministic re-export; 8 pages, 150 numbered answers.
- `ABSTRACT.txt` (392 bytes): single line + trailing newline, no ASCII double quotes, reader-native.

## Proofread record (builder self-check, 3 Nov 2026)

- Round 1: full read of the line-by-line proof diff against a same-exporter en-de reference (258 lines; lines identical to en-de, i.e. the shared English body, hidden). Round 2: regeneration of the proof diff from the final text.md export and exact diff against round 1 — the ONLY differences were the intended fix lines below (re-read and verified); all other lines byte-identical to the round-1 proofread text. Zero new issues in round 2.
- FLAG FOR THE COORDINATOR (core-source defect, inherited unchanged): the P7/P8 gloss of "HOW LONG?" as a term of office ("El mandato" / "O mandato" / "Срок полномочий" / "임기는 얼마나?" / "任期多長？" / "任期はどれくらい？") comes from the frozen core source and is shared by all 11 natives including shipped en-de and en-zh-cn. It was NOT diverged in these 9 editions — fixing it means fixing the core. An independent proofreader follows; this self-proofread does not replace it.

### Fixes applied in this edition

- Matching notes "word=gloss" → "word = gloss" (regex `"([a-z-]+)=([\u4e00-\u9fff])`, all matching notes).
- #29: "約翰尼·德普" → "強尼·戴普" (Taiwan standard name).
- P7 notes without "=" match the core's terse style consistently; left as-is.

## Repro

```bash
cd ~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-zh-tw-build
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python run.py
~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python render.py
cd ~/workspace/goals/lucernaread-social-media-operations/tools
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-en-zh-tw
./venv/bin/python webpdf.py ../files/weekly-report-w46-en-zh-tw/svg ../files/weekly-report-w46-en-zh-tw/The-Lucerna-VOL3-web.pdf
```

## Fix record — independent proofread Round 1 fixes (fix worker, 2026-11-03)

Source-only fixes per `hidden_files/w46/en-proofread-gates/proofreader-verdict-round1.md`; full re-render from the build sources (run.py + render.py + tools/webpdf.py + en_textmd.py). No rendered SVG/PDF was hand-edited. A Round 2 independent proofread follows; this record is not a proofread verdict.
- B4 (all 11 editions, frozen core): P7 toolbox B1 sentence wrapped with a lone closing guillemet `»` alone on a line. Source `hidden_files/weekly-report-w46-en-build/content7.py:51` (and the same line in every fan-out `content7.py`): before `B1 — « Dickens wrote the story in 1843. »` → after `B1 — « Dickens wrote the story in 1843.»` (space before `»` removed in the toolbox para only; the P7 B1 box example on line 32 keeps the spaced form). Rendered in all 11 as two lines `B1 — « Dickens wrote the story in` / `1843.»`; no lone `»` line remains in any edition (verified by SVG text extraction and visually on the P7 cards of all 11 editions).
- B5 (core + zh-tw): P7 editor's-note paragraph wrapped with a lone `。` alone on a line. Source `content7.py:115`: before `…請把你的來信與寫作寄來，VOL.4 起刊登收到的真實來信。` → after `…請把來信與寫作寄來，VOL.4 起刊登收到的真實來信。` (redundant `你的` deleted; paragraph now 2 lines, `。` attached). Verified visually on the P7 card.
- B6 (zh-tw): P2 `B · WILL` bridge wrapped with a lone `。` alone on a line. Source `content12.py:256`: before `用 will + 動詞原形改寫（承諾與將要發生的事）。` → after `用 will + 動詞原形來改寫（承諾與將要發生的事）。` (the praised `動詞原形` clarification kept; `來` added to re-break). CORRECTION (Round 3): the Round 1 record's phrase "bridge now ends `）。`" misdescribed the render — as printed, `）。` stood ALONE on a second line (`[p2-life#161 x=527 y=2067.225] ）。`), not as a line ending; the punctuation-only-line defect class remained (Round 2 residual R-B6, fixed in the Round 3 record below). Verified visually on the P2 card at full frame.
- M2 (fr/ko/zh-tw): doubled gloss prefix `譯注｜譯注｜` on the 5 P2–P6 gloss boxes. The 5 `f.gloss(...)` call strings (`content12.py:180`, `content34.py:28,111`, `content56.py:26,107`) repeated the furniture prefix that `Flow.gloss()` prepends; the leading `譯注｜` in each call string was replaced with `講解｜`, rendering the distinct pair `譯注｜講解｜` (W45 shipped precedent). CORRECTION TO THIS KIT: the furniture claim above (§Furniture) says the gloss prefix is single `譯注｜`; the rendered furniture is the distinct pair `譯注｜講解｜` — the single-prefix claim was the doubled-prefix defect's cause and is superseded by this record. P1 single-prefix line untouched. Verified on the P2 card at full frame.
- `<slug>.text.md` regenerated with the canonical `hidden_files/w46/en_textmd.py` (uniform family format; headers verbatim). Old text.md preserved under `hidden_files/w46/en-fix/old-textmd/`. For this edition the diff vs the old file is exactly the fix lines listed above.
- Re-gates on the final artifacts: build log zero `FLOW OVERFLOW` / `HEAD TOO WIDE`, TOTAL 150; canonical `occlusion_audit.py` 0 flags, selftest OK; `rowcheck46.py` 0 same-baseline collisions, 0 gloss-count mismatches, P6 chart-label GRAZE 0.0%; registry re-measured (core): 150 unique exercises 1–150, per-page 10/17/18/18/18/18/12/39, A2 60 / B1 69 / B2 21.
- `freeze.py diff` vs core: exit 0, TOTAL added CJK characters 680 (was 679; +1 is the M2 `講解` pair, all Traditional Han explanation layer; script scan: Han only, 0 Simplified-only residue by the KIT scan set). `p8.py compare --total 150`: CLEAN, 70→70, missing [], uncertain [], keydiff [137, 138, 139, 140, 150] legitimate. Web PDF 2,204,469 bytes (< 7 MB), pdftotext 44,908 bytes (equal to print extraction, 8 pages); print PDF 24,611,678 bytes; text.md 43,595 bytes.

## Fix record — independent proofread Round 2 residual R-B6, Round 3 (fix worker, 2026-11-03 UTC)

Source-only fix per `hidden_files/w46/en-proofread-gates-round2/proofreader-verdict-round2.md` §5/§10; full re-render from the build source (run.py + render.py + tools/webpdf.py + en_textmd.py). No rendered SVG/PDF was hand-edited. A Round 3 independent proofread follows; this record is not a proofread verdict. Answer keys untouched (Round 2 §11: 150/150 semantically correct, no registry change).
- R-B6 (zh-tw, BLOCKING): P2 `B · WILL` bridge still wrapped to a punctuation-only final line after the Round 1 fix. Rendered (Round 2): `[p2-life#160 x=527 y=2037.5] 用 will + 動詞原形來改寫（承諾與將要發生的事` + `[p2-life#161 x=527 y=2067.225] ）。` — the second line contained only `）。` at the left margin. Source `hidden_files/weekly-report-w46-en-zh-tw-build/content12.py:256` (`e.expl(...)`, bridge 20.5pt sans, 434px column): before `用 will + 動詞原形來改寫（承諾與將要發生的事）。` → after `用 will + 動詞原形改寫，承諾與將要發生的事。` (the praised `動詞原形` clarification and the full meaning kept; only `來` and the parentheses dropped — the verdict's 1-line text, not the 2-line alternative). Wrap re-simulated with the real wrap (zh-tw build's TC svglib, `sim_bridge_pre.py`/`sim_bridge_post.log`): current text reproduced exactly as 2 lines with a lone `）。` tail (41.0px); new text wraps as 1 line, 427.9px in the 434px box. Rendered as a single `<text x="527" y="2037.5">` element; no lone-`）。` element remains. Visually confirmed at full frame on the P2 card and in a 2× crop of the bridge (`hidden_files/w46/en-fix-round3/crops/r3-b6-zh-tw-p2-bridge.png`): one bridge line ending `。`, exercise 16 directly below, no second line.
- CORRECTION to the Round 1 B6 line in this KIT (above): "bridge now ends `）。`" misdescribed the Round 1 render; `）。` was a standalone second line, not a line ending.
- `<slug>.text.md` regenerated with the canonical `hidden_files/w46/en_textmd.py` (uniform family format; headers verbatim, first 6 lines identical). Answers section: 150 entries, 1–150 unique and complete.
- Re-gates on the final artifacts: build log zero `FLOW OVERFLOW` / `HEAD TOO WIDE`, TOTAL 150; canonical `occlusion_audit.py` 0 flags, selftest OK; `rowcheck46.py` 0 same-baseline collisions, 0 gloss-count mismatches, P6 chart-label GRAZE 0.0%; `freeze.py diff` vs core: exit 0, TOTAL added CJK characters 680 (unchanged from Round 2; all Traditional Han explanation layer); `p8.py compare --target en --total 150`: CLEAN, 70→70, missing [], uncertain [], keydiff [137, 138, 139, 140, 150] legitimate. Round 2 → Round 3 SVG-text multiset diff: only the bridge changed (2 lines → 1 line); no other string changed in any page. Web PDF 2,204,231 bytes (< 7 MB), 8 pages, pdftotext 44,900 bytes (equal to print extraction); print PDF 24,611,412 bytes; text.md 43,589 bytes. Gate JSONs/logs: `hidden_files/w46/en-fix-round3/` (`freeze-zh-tw.json/.log`, `p8-zh-tw.json/.log`, `occlusion-zh-tw.json/.log`, `rowcheck-zh-tw.log`, `sim_bridge_pre.log`, `sim_bridge_post.log`, `r2r3-multiset-diff.log`).
