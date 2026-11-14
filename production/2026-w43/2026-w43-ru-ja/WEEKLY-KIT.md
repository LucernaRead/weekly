# WEEKLY-KIT — Lucerna Weekly RU×JA（俄语正文 + 日语讲解）

- **Edition**: 2026-W43 · VOL.1 · ロシア語テキスト · 日本語の解説 — 日本語読者のための版
- **Pairing**: target = Русский (ru) · reader native = 日本語 (ja)
- **Dates**: 2026-10-19 – 2026-10-25 (W43), Europe/Moscow editorial frame inherited from the RU core
- **Status**: PASS (independent proofread complete 2026-10-22, zero problems — see §9; ready for repo insert by the main line)
- **Source core**: files/weekly-report-ru-vol1/ (Russian body text frozen byte-for-byte; only the explanation layer rewritten)
- **Build dir**: hidden_files/weekly-report-ru-ja-build/ (copy of the RU core build, OUT repointed to files/weekly-report-ru-ja/)
- **Totals**: 150 exercises = A2 54 · B1 72 · B2 24; per page 10/18/18/18/18/18/12/38 — identical to the core registry.

## §1 Method

1. Pre-flight duplicate check: build/edition dirs did not exist, no files <30 min, no build processes — proceeded.
2. `tools/freeze.py baseline` on the RU core build: 8/8 SVGs byte-identical before any work (core p1 c808a77d, p2 e6040d06, p3 21f0a9d7, p4 4d6fab86, p5 534284d6, p6 48e6b85a, p7 8f9e8618, p8 fa3f80ef).
3. Copy of the core build repointed (both OUT spellings are `os.path.expanduser("~/…/files/weekly-report-ru-ja…")`; zero residual `weekly-report-ru-vol1` references in any .py). Copy reproduced the core 8/8 byte-identical before the transform.
4. svglib.py replaced wholesale with the JA core version (see §2).
5. Explanation layer rewritten by an AST value-mapping transform (scratch/map_data.py + scratch/transform.py): every CJK-containing string constant in content12/34/56/7/8.py had to be present in the mapping — 464 constants mapped, 249 distinct keys, 0 unmapped; every mapping key used at least once. `bridge()` renamed to `expl()` (bslib4 def + 20 call sites: 4/6/6/3/1 per file). No module was ever imported or run inside the core build directory; core-dir comparisons ran only in repointed copies (README #11).
6. One-process builds only via run.py; render.py produced cards + print/web PDFs.

## §2 JA column svglib standard

- svglib.py = JA core version, md5 **d73e23b365676c3618d7e060b835eb4d** (JP faces + kinsoku oidashi + SEAM_SLACK seam repair), verified by md5 after copying.
- Diff vs the RU core's own svglib: JP face selection + the kinsoku/seam-repair block only; illustration functions identical.
- After the swap (before translation) the copy still produced the core's text multiset with CJK totals unchanged (142/212/134/126/120/146/319/888); the only diffs were kinsoku line-break reflows of identical character sequences on p2/p3/p5.
- Line-start kinsoku scan on the finished edition: **0 violations**. Latin/Cyrillic mid-word split scan: **0** true splits (18 boundary candidates, all adjudicated as discrete match-option/word-strip item boundaries, not wrapped continuations).

## §3 Furniture (JA column, target = ロシア語, per EN×JA KIT §3)

- P1 badge (replaces the core strapline at the (975, 372) slot, 19.5pt bold BRICK, centred): «ロシア語テキスト · 日本語の解説 — 日本語読者のための版»
- P1 top band centre: «КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 毎週一号 · ロシア人が読んでいるロシア語を読む» (first/third segments are the core's frozen Russian)
- Masthead: **Lucerna** (no article for Russian), serif line «РУССКАЯ ГАЗЕТА · VOL.1 · ПЕРВЫЙ СНЕГ · КАНИКУЛЫ · ДЕРБИ» frozen
- Footer left: «Lucerna · ロシア語週刊 VOL.1 · 本文はロシア語 · 解説は日本語»
- Footer right (page line): «N ページ（全 8 ページ）»
- gloss() prefix: «解説 — »; the first expl() after the P1 headline carries the «解説 — » prefix inside its value (shipped ×JA convention); plain instruction expl() strings carry no prefix
- Section heads: Russian original · Japanese short title (e.g. «ЖИЗНЬ · 生活», «КУЛЬТУРА · 文化», «СПОРТ · スポーツ», «МОЛОДЁЖЬ · 若者», «ЯЗЫК · 言語»)
- P8 header: «ОТВЕТЫ · 全解答と解説（1–8ページ）»; right note «各問に日本語の解説つき · ✓ は模範文のある問題»
- P8 page separators: «— N ページ —» (×8), dash-style answer lines «N. key — note», writing item «N. ✓ note» (RU family dash style, verified from the core's content8 code and the shipped RU-family fan-outs)
- Exercise-type names (registry, 1:1): 空所補充 54 · 選択 42 · 語と意味を結ぶ 20 · 組み合わせ 12 · 書きかえ 4 · 空所補充・選択 13 · 翻訳 4 · 作文 1. Printed instr forms: 空所補充 / 組み合わせ / 書きかえ / 翻訳 / 作文 / 語と意味を結ぶ / 映画と説明を結ぶ / チームと事実を結ぶ / 祝福と意味を結ぶ
- Japanese Russian-grammar terminology used throughout: 生格 (genitive), 対格 (accusative), 造格 (instrumental), 与格 (dative), 主格, 現在形 / 過去形 / 未来形, 不定形, 男性 / 中性, 三人称, 複数形

## §4 Freeze adjudication (tools/freeze.py diff, final run)

Added CJK characters: 2306 (all Japanese explanation layer). Removed/added string deltas close as follows:

- **Cyrillic tokens**: p2–p6 zero delta. p1 removed = exactly the badge-slot strapline words (ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ), replaced by the JA badge per §3. p8 removed = СТРАНИЦА ×8 (separators → «— N ページ —»). p7/p8 added Cyrillic occurs only inside Japanese notes citing Russian names («Динамо», «Спартак», «Зенит», film titles «Морозко» etc. in match notes, ЦСКА in the #137 translation key) — reader-language citations, not new body text.
- **Latin tokens**: removed {LUCERNA, RUSSIAN, WEEKLY} ×1 per page = the footer-left template change to the JA form (§3). No Latin added anywhere.
- Russian body text multiset equals the core's apart from the two furniture items above; every removed Chinese-side string is explanation layer by construction (the transform could only touch mapped constants, and the mapping was asserted total).

## §5 Answer-key gate (tools/p8.py compare)

- Core printed set (measured): 150 notes, dash style. Edition forces the identical set.
- `p8.py compare`: **CLEAN** — core 150 noted, edition 150 noted, missing=[], extra=0.
- p8.py reported keydiff [54, 137, 138]. Registry-level truth (both registries dumped from one-process runs in repointed copies, scratch/regcheck/): **real keydiff = [137, 138, 150]**.
  - #137 翻訳 key: «星期日中央陆军将对阵斯巴达克。» → «日曜日、ЦСКА は «Спартак» と対戦する。» (the key IS the reader-language translation — legal class)
  - #138 翻訳 key: «预报员预报十月末有雨夹雪。» → «予報士は10月末にみぞれを予報する。» (same class)
  - #150 作文 device key: «（开放题，范文如下）» → «（自由記述、模範文は下）» (not printed; P8 prints ✓ + note — same class as other families' #150)
  - #54 is a p8.py extraction artifact (README #13 class): registry keys identical («третий») and both printed lines read «54. третий — <note>»; falsified against the registry dump, not assumed.
- Reverse-direction translation items #139/#140: Japanese source sentences printed («土曜日から休みが始まる。全部で12日間だ。→ ___», «父の日にお父さんにお祝いを言います！→ ___»), Russian keys frozen.
- Notes: 141 of 150 changed (all reader-language); the 9 identical notes are language-neutral (8 pure-Russian conjugation notes, e.g. «выпасть → выпадет»; #76 «吸血鬼 d» — 吸血鬼 is the standard Japanese word, adjudicated keep alongside 生活 / 文化 in band titles).

## §6 Geometric + content gates

- `tools/occlusion_audit.py` (selftest passed in-run): edition = 2 flags, **both byte-identical to the core's own flags on frozen Russian elements** — BOXTITLE p1 «странице.» (ink 2305.6 > border 2304.0) and LINEX p2 rule y 1803–1805 vs the frozen «Запомните пару» line. New flags vs core: **0** after the §7 fix.
- Same-line ink-collision scan (README #10): 0 collisions.
- P6 chart, element level (README #12): bars at x=685 widths 600/494/388/282 == round(v·600/34) for 34/28/22/16%; Russian labels ≤303 units wide (bars start at +620); value labels end ≤1345 < RIGHT 1885. The core chart carries Russian-only labels (no reader-language chart labels exist in the core; the bilingual honesty caption below the chart is preserved, Russian frozen + Japanese «これは編集部の練習用データで、実際の統計ではありません。»).
- Calendar strip Oct 24 – Nov 4 frozen from the core; weekday letters match the real 2026 calendar (24 Oct 2026 = Saturday, сб).
- Gloss counts: gloss() boxes per page core = edition (p2 3, p3 2, p4 1, p5 2, p6 1; P1 first-expl prefix 1 = 1; the P1 count delta in raw «解説 — » strings is the badge itself, which contains the phrase). Every core gloss entry is present, item for item — none dropped, none merged.
- P7 phrases of the week: all 8 Russian quotes verbatim, occurrence counts 1 = 1 each, page tags «(Страница N)» counts identical to the core {1:1, 2:2, 3:2, 4:1, 5:1, 6:1}; the reader-language renderings under each quote are Japanese.
- Residue scans: Chinese explanation residue = 0 (kanji-only strings in the edition were listed and adjudicated one by one as Japanese-inherent: 言語， 生活， 文化， 吸血鬼， 若者， 短信， 三学期制， 次号予告， 第12節， 第3日曜日， 模範文-headers etc.); other-column furniture = 0; the banned intermediary term appears nowhere as an operative concept in pages, this KIT, or operative code — its old method name is quoted only in the §1 rename record and in the scratch transform scripts as rename search patterns (disclosed here per the standing builder-hygiene note).
- Content red line: Russian body untouched (domestic-life topics only); the Japanese layer adds no international-politics content.
- Fonts: JP faces throughout («Noto Serif/Sans CJK JP» via the JA svglib), per tables.json indices; visual pass over all 8 cards found no missing glyphs / tofu.

## §7 Self-proof defects found & fixed (2)

1. **P7 letters-box overflow (LINEX, mine)** — first audit run flagged the phrases rule (y 1697–1699) crossing the last line of the letters-box note: my Japanese note wrapped to 3 lines where the core's Chinese wrapped to 2, growing the box stack by exactly +29.0 (col3 end 1711.96 vs core 1682.96). Fixed by shortening the note (explanation layer only): «編集部の例文です。投書ではありません。VOL.2 で本物の投書と優秀作文を掲載！» (2 lines; the VOL.2 promise content preserved). Col3 end after fix = 1682.96, identical to the core; audit re-run clean of new flags.
2. **Stray apostrophes in f-string fragments (P8 H area)** — the AST transform replaced string constants with quoted repr() literals; for constants that are fragments of an f-string (JoinedStr parts) the inserted quote characters became literal text: the writing expl line and the #150 note rendered «'82' 語» with apostrophes. Fixed by rewriting the two f-strings in content8.py as clean literals. Verified: apostrophes in rendered text elements now match the core page-for-page (only the core's frozen «Хэллоуин'26» on p5), and the H expl line renders «作文（決まった答えはありません）；模範文（82 語）は下にあります。». **Lesson for the toolkit: value-mapping transforms must substitute JoinedStr fragments as raw text, never as quoted literals.**
   - After each fix the full gate suite was re-run from a single-process build (freeze diff, p8 compare CLEAN, occlusion audit, kinsoku/split/collision scans).

Other adjudications (not defects): the P2 father's-day gloss ends with a 2-glyph tail line «葉。» and splits «言葉» across lines — ordinary CJK wrapping, same shape as the core's own «祝愿。» tail; JA-family normal. Katakana splits （チーム, グリーティングカード) are inherent to CJK wrap; the column standard bans Latin/Cyrillic splits only (0 found).

## §8 Deliverables & measured pins

- files/weekly-report-ru-ja/svg/ — 8 SVGs (p1-pervaya … p8-test)
- files/weekly-report-ru-ja/cards/ — 8 card PNGs (1950×2700)
- Print PDF: Lucerna-VOL1.pdf — 30,488,773 B, sha256 30b9d934312fb2725a93e0ab0bb01e2a0947b58112d6bbbd44272309001a6cc7
- Web PDF: Lucerna-VOL1-web.pdf — 3,552,214 B (< 10 MB), sha256 c0a5ad2f43f16651b21ada7fc9c27459d964eb4bd2007e12755c66b3adc196b4
- Core integrity at close: `freeze.py baseline` re-run 8/8 OK; shipped core SVG hashes unchanged (c808a77d / e6040d06 / 21f0a9d7 / 4d6fab86 / 534284d6 / 48e6b85a / 8f9e8618 / fa3f80ef).
- Scratch evidence: hidden_files/weekly-report-ru-ja-build/scratch/ (map_data.py, transform.py, cjk_full.json, freeze_diff2.json, p8compare.json, occl-edit2.json, regcheck/ registry dumps, scan_all.py, adjudicate.py).

**Status: PENDING** — ready for the independent proofread; no repo insert, no Discord post (per standing instructions).

## §9 Independent proofread record (2026-10-22) — PASS

Full independent re-run, nothing taken from the builder's self-report. Scratch: hidden_files/proof-ru-ja/.

- **freeze.py baseline**: core 8/8 byte-identical (start and close); my own repointed copies of BOTH builds reproduce their shipped SVGs 8/8.
- **freeze.py diff**: added CJK = 2,306 (all Japanese explanation layer). Cyrillic token delta p2–p6 = 0 (independently computed); p1 removed = badge-slot strapline only; p8 removed = СТРАНИЦА ×8; added Cyrillic all inside Japanese notes as Russian name citations (ЦСКА/Спартак/Зенит/Динамо/Родина/Оренбург, film titles). Latin removed = footer template {LUCERNA, RUSSIAN, WEEKLY} ×8 only.
- **p8.py compare**: CLEAN 150=150 (core set independently extracted = full 150). Registry-level real keydiff = {137, 138, 150} exactly (my own one-process registry dumps of both builds); #54 falsified per README #13 (registry keys identical «третий», both printed lines «54. третий — …»). Notes: 141 changed, 9 identical = language-neutral set {17, 35, 36, 63, 73, 76, 90, 104, 110}. #139/#140 Japanese stems printed as registered, Russian keys byte-identical. All 150 keys re-derived by hand from the Russian body: zero disagreements (incl. Антон passage #129–132; P6 chart 34+28+22+16=100 ↔ #85/#86/#87; 2026−1811=215; model essay 82 words).
- **P8 style from code**: both builds generate `f"{n}. {key} — {note}"` / `f"{n}. ✓ {note}"` — byte-identical answer code, only the separator string localised (README #8/#14).
- **JA column furniture**: badge (975, 372) 19.5pt bold #a4553a exact string; top band, footers ×8, page lines «N ページ（全 8 ページ）», P8 header «ОТВЕТЫ · 全解答と解説（1–8ページ）», separators «— N ページ —» ×8, bilingual heads — all verbatim vs EN×JA KIT §3. svglib md5 = d73e23b365676c3618d7e060b835eb4d re-measured.
- **×JA dual scan**: line-start kinsoku = 0 (no tspans exist; every rendered line is its own text element, so the scan is exhaustive). Latin/Cyrillic mid-word splits = 0 (6 boundary candidates in kana-carrying paragraphs, all word boundaries: чемпионата|России, с|Днём, стихи|Пушкина etc.).
- **Geometry**: occlusion_audit (selftest OK) — edition 2 flags, both byte-identical to the core's own on frozen Russian elements (BOXTITLE p1 ink 2305.6 > 2304.0; LINEX p2 same string/geometry), NEW vs core = 0. Same-line ink-collision scan (README #10, canonical ink boxes): 0 collisions. P6 element level (README #12): rect multisets identical core vs edition; any-overlap of text ink by later opaque shapes = 0; bars 600/494/388/282 = round(v·600/34) for 34/28/22/16; bilingual honesty caption in place. No HEAD TOO WIDE in either build.
- **Builder fixes verified in place**: P7 letters box rect (1451, 1372.46, 434×310.5) bottom = 1682.96 in BOTH SVGs; phrases rule y=1698; col4 card pixels rows 1684–1711 ink-free in both cards; both builds' flow logs print «P7 col3 ends 1682.96». Stray-quote scan (README #18): apostrophes per page identical to core (only p5 «Хиллоуин'26» — note: the frozen string reads Хиллоуин, not Хэллоуин as §7 says; the element is byte-identical in both editions), H expl line renders clean.
- **gloss counts**: code-level gloss() 9 = 9 and expl() 20 = 20 per file group; rendered per page core 译注｜ = edition 解説 — gloss starts (p2 3, p3 2, p4 1, p5 2, p6 1); P1 first-expl prefix 1 = 1; badge accounts for the raw-string delta. Double prefix = 0.
- **P7**: all 8 Russian quotes byte-identical to the core AND verified verbatim in their tagged article pages; page-tag distribution {1:1, 2:2, 3:2, 4:1, 5:1, 6:1} identical; Japanese renderings faithful; VOL.2 promise preserved.
- **Calendar** (Europe/Moscow, `date`-verified): Oct 18 Sun (Father's Day, 3rd Sunday), 19 Mon, 21 Wed, 22 Thu, 23 Fri, 24 Sat, 25 Sun, 26 Mon, 28 Wed, 31 Sat, Nov 3 Tue, Nov 4 Wed (День народного единства); P6 strip letters сб вс пн вт ср чт пт сб вс пн вт ср for Oct 24–Nov 4 all match.
- **Red line / residue**: politics-term scan of the whole edition = 0 hits; Chinese explanation residue = 0 in substance — exactly 4 core CJK strings survive verbatim, all Japanese-inherent (吸血鬼 note #76, 生活/文化 band titles, 三学期制 strip); simplified-only glyphs = 0; operative build code carries no banned intermediary term (scratch copies + this KIT's rename record only, per disclosure).
- **Short tails**: 10 under a uniform metric vs JA core 55, EN×JA 15, ES×JA 10, FR×JA 14 — family-normal.
- **Pins (disk-measured, D5 rebuild 2026-11-14)**: web PDF 2,630,672 B sha256 acbbd472185284daa2e36fa3d8d5c0edd6d51deb4e61580455be4ab65456d681; print PDF 27,661,599 B sha256 34ce972b51b9adf426e5db93e5b2a876a1100af4fdce5c13ca1d36c74a370da9 — D5 前 KIT 值（web 3,552,214 B / print 30,488,773 B）已滞后，以本次实测为准。

**Verdict: PASS — zero problems. Cleared for repo insert as slug 2026-w43-ru-ja via tools/insert.py.**

## §10 D5 重建記錄（2026-11-14）

D5 + §1.1 合并重建（2026-11-14；builder v3 接替 v2，v2 死于 2026-11-14 ~02:55 UTC 第 5 波 restart drain）。本节 supersedes 上述旧印/网 pin 行（以实测发运值为准；KIT 旧 SHA 不可作基线）。

- 装机：`apply_variant.py --patch-core ru --week 2026-w43`（core-ru `_D5_READER = "latin"`，+263/−28）+ 本版 `apply_variant.py --svglib patched/2026-w43-ru-ja/svglib.py --target ru --reader ja --week 2026-w43`（`_D5_READER = "latin"`，diff +120/−7）；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2 保留。
- 基线：run TOTAL 150，0 警告；印 PDF 27,697,168 B（MANIFEST +0.001%），网 PDF 2,652,626 B，`pdf_text_diff_ru.py` + TRIM_ARGS → IDENTICAL；修前普查 D5 拉丁 206、西里尔 0。
- 缺陷与修法（只动字号/断行与规则线位置，不动文字）：
- D2 (occlusion TEXTX, P1): `'A2' overlaps 'кино' 7.4×11.2px` — `content12.py:103` 目录标题 20→19pt。
- D3 (occlusion LINEX P2 ×6, 基线同款): `content12.py:232` 规则线 `ey−12`→`ey−8`。
- 门禁（run2）：全套 17 门 ALL-GREEN。run TOTAL 150；head_check 0；d5 census 拉丁/西里尔/弯引号在 CJK 均 0（弯引号总数 0；`noto_sans_elements=406`）；freeze baseline 8/8；freeze diff 新增 CJK 0、新增拉丁 strings 67（run 拆分）；spill 0（169 OBSERVE）；boxtitle 0 DEFECT（58 titles, 744 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=401, median 1.009；P8 231→231 行，slack 61.4→61.4px）；文字层 print=web 差 0（34,976 字）；text.md BYTE-IDENTICAL；census_quotes 0 defective；p8 compare CLEAN，keydiff=[137, 138]；刊头标语→日期间距 402.5px PASS。日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-ja/GATES-SUMMARY-run2.txt`。
- 新交付物（实测）：印 PDF `Lucerna-VOL1-ru-ja.pdf` **27,661,599 B**，sha256 `34ce972b51b9adf426e5db93e5b2a876a1100af4fdce5c13ca1d36c74a370da9`；网 PDF `2026-w43-ru-ja.web.pdf` **2,630,672 B**，sha256 `acbbd472185284daa2e36fa3d8d5c0edd6d51deb4e61580455be4ab65456d681`；text.md **60,813 B**，sha256 `e7d0658af396359739ee5529c2207e8f8f0835dea945742bc79fbd9af0c492f0`，与 fanout `.text.md.new` BYTE-IDENTICAL。D5 报告：`production/notes/2026-w43/g-ru/scratch-d5-rebuild-ru/D5-REPORT-2026-w43-ru-ja.md`。§8 pin 行已同步为本次实测值；§9 独立校对记录中“identical to §8”一句指 D5 前的核对，不改。
