# WEEKLY KIT — De Lucerna, VOL.2 (Nederlands × 日本語, W45)

## 1. Spec

- **Issue week:** Monday 2 November – Sunday 8 November 2026; issue dated Monday 2 November 2026.
- **Volume:** VOL.2 for Nederlands (sequel to W43 VOL.1).
- **Pairing:** target language **Dutch** × reader native language **Japanese** (matrix cell NL × JA).
- **Masthead:** De Lucerna (article De, per the Dutch convention).
- **Format:** 8 pages (multiple of 4), page size 1950 × 2700, 4 columns, warm ivory paper, dark olive-green accents.
- **Relation to the core:** built from `files/weekly-report-w45-nl-core/` (VOL.2, masthead De Lucerna). The Dutch core — articles, exercises, images, facts, answer keys — is frozen and identical; only the explanation layer was rewritten, into Japanese. No Discord post, no chat card/PDF dump, no cron, no weekly-git touch, no core/W43 modification (core SVGs re-hashed 8/8 unchanged at the end; weekly-git status clean).
- **Lead topic (inherited unchanged from the core KIT §4):** «Nederland in de Klimaatweek» — the national Klimaatweek (2–8 Nov), Museumnacht Amsterdam (7 Nov), Crossing Border Festival (3–8 Nov), Eredivisie matchday 12 (6–8 Nov). Facts, trend sources and verification debts are inherited unchanged from the core KIT §4.

## 2. Content per page (identical structure to the core; only the explanation layer differs)

- **P1 — Voorpagina (A2, 10 ex.):** headline «Nederland in de Klimaatweek: bomen, musea en voetbal»; week agenda; numbers box; word of the week «het klimaat»; photo herfstbos; IN HET KORT box; lightning quiz (7–10).
- **P2 — Leven (A2, 18 ex.):** «De Klimaatweek: wat kun jij doen?» — Coevorden giveaway, energy saving, KNMI colour codes; photo kinderdijk; WIST JE DAT facts; EN JIJ box (best entries to VOL.3).
- **P3 — Cultuur (A2→B1, 18 ex.):** «Amsterdam blijft wakker: de Museumnacht» — Museumnacht, Crossing Border, PAN Amsterdam, Mega Snuffelmarkt; photo gracht.
- **P4 — Sport (B1, 18 ex.):** «Europa: drie keer feest, twee keer verlies» — verified European results, matchday-10 results, standings after 10 rounds, full matchday-12 programme; photo elftal1912.
- **P5 — Jongeren (B1, 18 ex.):** «Expeditie Robinson is begonnen!» — Robinson premiere follow-up, ADE (30 years) and DDW closings, youth climate actions; no photo on this page.
- **P6 — Verdieping (B2, 18 ex.):** «Geel, oranje, rood: hoe werken de codes?» — KNMI local-warning deep read, pro/contra local warnings, program-drawn chart explicitly labeled OEFENDATA (practice data, not a real survey: 100 jongeren — thuis 45, eerst tekst 25, toch naar buiten 20, weet niet 10).
- **P7 — Taal (A2/B1/B2, 12 ex.):** A2 klimaatwoorden; B1 scheidbare werkwoorden; B2 mening geven; PAS OP clinic (4 items); word «meedoen»; readers' corner (editor's example + invitation, see §6); 8 golden sentences; VOL.3 preview (Sinterklaas 15 Nov, Sint-Maarten 11 Nov, letters + best P8 texts).
- **P8 — Toets en antwoorden (38 ex.):** A kroniek (8), B algemene vragen (8), C lees en antwoord (4, Daan/Coevorden text), D maak de zinnen (4), E vertaal (4, re-aimed — see §5), F woorden match (4), G dialoog bij de bomen (5), H schrijf zelf (1); all 150 answers with Japanese notes in dash style.

## 3. Measured exercise counts (registry output, identical to the core KIT §3)

- **Total: 150 exercises.** By page: 10 / 18 / 18 / 18 / 18 / 18 / 12 / 38.
- By level: A2 47, B1 72, B2 31.
- By type (Japanese registry labels): 文の完成 65, 選択問題 44, 単語のペア 8, 正誤判断 7, 文を作る 8, 穴埋め選択 13, 翻訳 4, 作文 1.
- Model essay (P8 H, ex. 150): **87 words** (requirement 80–100).
- Numbering continuous 1–150; P8 printed answers verified against the registry (p8.py extract: noted set = 150 of 150).

## 4. Gates — measured values (all builder-run; logs in hidden_files/weekly-report-w45-nl-ja-build/)

- **Pages:** 8 (multiple of 4). SVGs 8, cards 8 at 1950×2700, print PDF 8 pages, web PDF 8 pages.
- **Core freeze:** `tools/freeze.py baseline` on the W45 NL core build reproduced the core **8/8 byte-identical** (sha prefixes p1 5424557b · p2 78e6fcd2 · p3 5b9854e3 · p4 cc227fd9 · p5 e58064c9 · p6 6583fe28 · p7 65cfe2b3 · p8 fe22a151) and re-hashed the shipped core unchanged at the end; `freeze.py diff` core-vs-edition: added CJK **3,087** characters total (p1 246 · p2 267 · p3 211 · p4 178 · p5 258 · p6 253 · p7 403 · p8 1,271), every added character kana or standard Japanese kanji (distinct-char inventory inspected; no Simplified-only character). Added-CJK attribution: 100% Japanese explanation layer. Pure-Dutch removals close as: P1 only the y=372 strapline replaced by the JA badge (W43 precedent, §7); P4/P5/P6 byline wrap fragments (full bylines verified present in the edition); P6 one lone «）» wrap fragment from the core chart-caption parenthetical (JA caption wraps differently, text verified present); P7 Dutch tail fragments of clinic notes (same Dutch words present in the JA-side fragments); P8 «104. blijf — rood = blijf binnen» (key «blijf» identical; only the Dutch-only gloss note was translated to Japanese, per the §5 note rule) and the 8 «— PAGINA N —» separators (replaced by the W43 JA separator form, §7). No Dutch article, exercise body, option, fact or figure differs.
- **P7 word-box freeze (blocking gate):** core Dutch definition sentence «meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee. is **byte-identical** in the edition (SVG elements 119–121 = core 118–120, same line breaks); only the gloss was localized: «meedoen = 参加する：気候週間にはオランダ中が参加する。».
- **P8 printed-note set:** `tools/p8.py compare`: core 150 noted, edition 150 noted, status **CLEAN**, missing [] extra 0 uncertain []. Keydiff [3, 7, 17, 29, 70, 71, 76, 96, 137, 138, 148] — adjudicated in §5; no key is missing, no extra key, no SHORT. Full 150-item printed-key-token comparison: diffs exactly [137, 138, 150] (see §5).
- **Geometric occlusion audit:** `tools/occlusion_audit.py` (selftest OK): edition **0 flags**, core **0 flags**, NEW vs core **0**.
- **Same-baseline ink scan** (build/rowcheck.py, README #10): same-baseline text-ink overlaps **0 on all 8 pages**.
- **P6 chart-label coverage** (build/rowcheck.py, baseline-anchored PIL getmetrics ascent/descent, anchor ls — NOT getbbox, which inflates): all 4 labels **0.0%** (label boxes end 4 px above their bars); bar geometry x=1473, widths 180/100/80/40, heights 18, y=304/362/420/478, values 45/25/20/10 — identical to the core.
- **Gloss counts (rendered gloss() strings split on ·):** P2 6 = 6, P3 5 = 5, P4 5 = 5, P5 5 = 5, P6 5 = 5 — core 1:1 in every box. P1 expl box 4 items, unchanged in count.
- **P7 golden sentences:** all 8 Dutch sentences occur exactly **2×** (source article page + P7), verbatim, with page tags identical to the core: Pagina 1, 1, 2, 3, 4, 5, 6, 6. Each sentence was confirmed on its tagged article page (P1 ×2, P2, P3, P4, P5, P6 ×2). Golden-sentence Japanese translations are the edition's own (see transform.py).
- **Japanese line-start scan (rendered SVGs):** line-start kinsoku closers (、。！？：；）」』】ー…‥・) and small kana (ぁぃぅぇぉゃゅょっァィゥェォャュョッ) = **0 hits** on all 8 pages. Japanese mid-word character wraps (e.g. the P7 word gloss breaking オラン｜ダ, the P7 B2 bridge breaking 思｜える) are normal Japanese line-breaking, not defects; the scan criterion is line-start punctuation/small kana only, and every change was judged on rendered SVG, never on source estimates.
- **Readers' corner (§6):** no reader, letter, name or quote invented; the only letter on the page is the labeled editor's example.
- **Images:** only clearly public-domain/CC0 images, reused byte-identical from the core build assets (assets diff clean): P1 herfstbos, P2 kinderdijk, P3 gracht, P4 elftal1912. Every credited image is typeset on its page (1 `<image>` element per photo page; P5/P6/P7/P8 carry no photo, as in the core). Note: the P4 credit line wraps to 2 lines in the JP face («Foto: Spaarnestad Photo / Wikimedia Commons — publiek» + «domein») vs 1 line in the core SC face — same text, verified present; the facts box below it is unaffected (occlusion 0).
- **Image credits (from the Commons API Artist field, per the core KIT §5 / W43 CREDITS.md):** P1 Foto: Vovogov90 — CC0; P2 Foto: Nationaal Archief — CC0; P3 Foto: W. Punt / Anefo, Nationaal Archief — CC0; P4 Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein. All four credit lines verified present in the rendered SVGs.
- **Banned-string / residue scans (all 8 SVGs):** 桥接 0, 译注 0, 讲解 0, Simplified furniture strings (练习与答案/参考答案/中文简析/本/第 N 版) 0, Cyrillic 0, Hangul 0, other families' furniture (DE/EN/PT/FR forms) 0, double gloss prefix 0. The one Chinese remnant caught by the final word-list rescan (P8 #77 note «不定式», missed in the first pass because its characters are shared kanji) was fixed in fix round 3; the rescan after the fix reads 不定式 0 everywhere.
- **Footers:** 8/8 carry «De Lucerna · オランダ語週刊 VOL.2 · 本文はオランダ語 · 解説は日本語» with «N ページ（全 8 ページ）» (n = 1–8).
- **Build warnings:** final render log shows **zero FLOW OVERFLOW / HEAD TOO WIDE** warnings.
- **Visual inspection:** all 8 rendered PNG cards viewed page by page: clean, no overlaps, no cut-off text, no defects (including the fixed P1 word-note area, the P2 match set, the P6 chart, the P7 col-3 stack and the P8 key block foot).

## 5. What changed vs the core — and what did not

Rewritten into Japanese (the whole explanation layer): every word gloss («解説 — » boxes), every section instruction, the error-clinic notes, the readers'-corner notes, the teaser apparatus, the phrases-of-the-week translations, all 150 answer notes, all bilingual page headers and subtitles, the P1 numbers-box parentheticals, the P2 code-box labels, the P6 chart caption's second line, the readers' prompts (EN JIJ boxes), and the P8 answer-key header lines.

Unchanged: all Dutch articles, headlines, exercise bodies and options, all facts and figures, all images and credits, the chart geometry and values, and the answer keys except §5 items.

### Type / instruction mapping (W43 NL × JA registry forms)

完成句子 → 文の完成 · 单选 → 選択問題 · 完形单选 → 穴埋め選択 · 词汇配对 → 単語のペア · 判断对错 → 正誤判断 · 造句 → 文を作る · 翻译 → 翻訳 · 写作 → 作文. Instructions: 填空 → 空所補充 · 判断 → 正誤 · 造句 → 文を作る · 写作 → 作文 · 把词和释义配对 → 語と意味を結ぶ. `bridge()` renamed `expl()` throughout (bslib4 definition + 22 call sites), per the W43 NL × JA precedent; the rendered prefix is «解説 — » in both expl lines and gloss boxes.

### KEEP set — notes byte-identical to the core (language-neutral, W43 JA precedent)

#6 «veel mensen → planten», #78 «hij → gaat praten», #85 «45 + 25 = 70», #101 «wij → planten», #102 «je → bespaar», #105 «ik → doe mee». (P8 #77's note «wij → gaan + 不定式 kijken» was initially missed and kept verbatim by accident; fix 3 translated it to «wij → gaan + 不定詞 kijken», so it is NOT in the final KEEP set.) All other 143 notes are Japanese (Dutch words cited inside Japanese notes are the explained vocabulary itself, not untranslated explanation).

### P8 keydiff adjudication (compare output keydiff [3, 7, 17, 29, 70, 71, 76, 96, 137, 138, 148])

- **Genuine re-aims (translation items, as in the W43 NL × JA precedent): 137, 138.** Exercises 137–138 keep their Dutch source sentences and are now translated **into Japanese** (137 «気候週間は7日間続く。», 138 «オレンジ警報は「備えよ」という意味だ。」). Exercises 139–140 swap direction — the printed source is now Japanese and the key is the Dutch sentence, byte-identical to the core's keys (139 «Museumnacht duurt van 19:00 uur tot 02:00 uur.», 140 «Ik doe mee aan de Klimaatweek.»); 139/140 are therefore NOT in the keydiff, and 150's printed line is the translated writing-task pointer (apparatus) with the 87-word Dutch model text byte-identical.
- **Extraction artifacts, not key changes: 3, 7, 17, 29, 70, 71, 76, 96, 148.** For these nine, the printed answer token before the first « — » is byte-identical to the core (3: 7, 7: B, 17: wortelen, 29: B, 70: eiland, 71: proef, 76: gaat winnen, 96: advies, 148: B); only the translated note differs. p8.py's paren branch swallows the note into its key field exactly when a note contains full-width parentheses (e.g. «ミュージアムナハトは11月7日（土）», «eiland = 島（het）», «zachte = 柔らかい（土）») — the same artifact family as README #13. Verified against the printed P8 lines in both SVGs, not just the tool output.

### P8 note bracket form (cross-family rule)

Notes use the JA family's shipped form: full-width parentheses （） for parentheticals (W43 NL × JA P8: «103. B — half vijf = 4:30（ひっかけ）», «150. ✓ 模範文はこのページの H 欄（87語）»). Measured on the final render: P8 answer lines carry 16 full-width «（» and **0** half-width «(». P8 style is the NL family's dash style `N. key — note`, writing item `N. ✓ note`, with the core's dash-generation code byte-identical.

### Layout adjudications (apparatus only — the Dutch core was never touched)

1. **P2 exercise spacing (EN precedent):** P2 exercise gaps 8 → 4 and section-head gaps 13 → 8 (P2 only), plus the first P2 bridge shortened to one line («2ページを読んで正解を選んでください。», 正しい答え → 正解, same meaning). Without this, the P2 match set overflowed its region (first-render overflow: match set needed 428 at y=2191, bottom 2580). Final P2 exercise flow ends y = 2402 (bottom 2580).
2. **P7 column-3 stack:** the BRIEVEN box initially ended y = 2043, crossing the zinnen gold rule (y = 1937). Fixed by shortening the invitation 4 → 2 lines (imperative + VOL.3 promise kept), trimming two clinic notes to one line each (the Dutch right lines carry the full rule), and tightening the col-3 box gaps 18 → 8. Final P7 col-3 ends y = 1906, 31 px clear of the rule. No Dutch text, quote or preview text changed.
3. **P1 word-of-the-week note:** the Japanese note initially ran 3 lines; its last line (y = 1897.6) fell inside the IN HET KORT box (top 1874) and overprinted the box title (occlusion NEW flags). Shortened to 2 lines («「気候」とは長期的な天気と自然のこと。気候週間は私たちの気候の週だ。」), last baseline back to 1871.9, exactly the core's. Final occlusion: 0.
4. **P8 #77 note (fix 3):** the first-pass transform missed «wij → gaan + 不定式 kijken» (its characters are shared kanji, so the Simplified-only character scan missed it; the final word-list rescan caught it). Fixed to «wij → gaan + 不定詞 kijken». No layout change (same character count; P5 SVG byte-identical before/after).

## 6. Readers' corner — honest note

No real reader letter exists for this issue. P7 prints a **clearly labeled editor's example** («Li (voorbeeldbrief van de redactie)», Dutch example letter text kept verbatim from the core) plus an on-page disclosure and invitation. All three facts are on the page, in Dutch and in Japanese: (1) no real letters had arrived at press time, (2) no best page-8 texts had arrived, (3) the example stands with the promise carried to VOL.3. The Dutch disclosure is kept verbatim: «Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.» The Japanese disclosure carries the same meaning and explicitly labels the example as the editors': «締切時に本物の手紙と8ページの優秀作文はなく、編集部の例文を掲載。約束はVOL.3へ。» The explicit Japanese public invitation, verbatim:

> あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！

(Imperative + publication promise; the contents-preview line and other pages' exercise prompts are not counted as the invitation.) No reader, letter, name or quote was invented for this edition.

## 7. Furniture — measured attributes and W43 comparison

tables.json has **no established JA-native furniture column** (`furniture ja --target nl` errors), so the shipped W43 NL × JA SVG is the authority throughout (task rule: W43 measured beats README generic text). Every string below was verified in the shipped W43 SVGs and reproduced in this edition:

- **Pairing badge (P1 masthead, replaces the core's Dutch strapline at y = 372):** «オランダ語テキスト · 日本語の解説 — 日本語読者のための版», centered x = 975, y = 372, 19.5 pt, bold, BRICK #a4553a, Noto Sans CJK JP (W43 SVG measured: same x/y/size/weight/colour). The removed Dutch strapline is the only pure-Dutch removal on P1 (see §4 attribution).
- **Footer (all pages):** «De Lucerna · オランダ語週刊 VOL.2 · 本文はオランダ語 · 解説は日本語» (W43 form with VOL.1 → VOL.2), 20 pt sans, grey, baseline 2624, footer rule y = 2580, with «N ページ（全 8 ページ）» right-aligned.
- **Gloss prefix:** «解説 — » (single layer; double prefix = 0 in the final render).
- **Top strip:** centre «ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む» (W43 JA string, identical core Chinese); left «VOL. 2»; right week dates in Dutch, unchanged.
- **Flower line:** «オ ラ ン ダ 語 週 刊 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12» (W43 JA pattern: language name Japanized, theme words kept Dutch). Measured 1598.9 px < 1820 px inner width, so the full line is kept — unlike the W45 NL × EN edition, whose Dutch line measured 1958.8 px and had to drop MUSEUMNACHT. No deviation from W43 here.
- **Page headers:** Dutch + Japanese throughout (e.g. «LEVEN · 生活», «CULTUUR · 文化», «SPORT · スポーツ», «JONGEREN · 若者», «VERDIEPING · 深掘り», «TAAL · 言語», «TOETS EN ANTWOORDEN · テストと解答»). Band sub-lines give the Dutch description followed by the Japanese one. Section heads follow the W43 JA short forms («DE WEEK IN CIJFERS · 数字で見る今週», «ZO ONTHOUD JE HET · 覚え方», «EN JIJ? · あなたは?», «BLIKSEMQUIZ · 早押しクイズ», «PAS OP! · 間違いクリニック», «HET WOORD · 今週の単語», «ZINNEN VAN DE WEEK · 今週の名文（本号の記事から逐語引用）», «VOLGENDE WEEK · 来週の予告 (VOL.3)», «ANTWOORDEN · 全解答と解説（1–8ページ）»).
- **Exercise导语行:** «答えは8ページ · 問題はレベル混合、番号で探してください» (W43 JA form).
- **P8 separator:** «— N ページ —» (1–8; W43 JA form, replacing the core's «— PAGINA N —»).
- **P8 style:** dash style `N. key — note`, writing item `N. ✓ note` (NL family form, core code byte-identical).
- **P7 golden sentences:** Dutch quotations verbatim frozen + Japanese translations + (Pagina N) tags identical to the core (8 items).
- **Family case (README #20):** the NL core has a native subtitle slot at y = 330 and a Dutch strapline at y = 372; the W43 NL × JA precedent replaces the strapline in place with the badge at y = 372 (19.5 pt bold BRICK) — this edition follows that case exactly (no masthead shift, no inserted badge row; frozen elements below y = 606 unmoved).
- **Chart title (deviation note vs NL × EN):** «DE GRAFIEK · グラフ（練習データ）» measured 404.5 px < 412 px box inner edge, so the full form is kept — unlike NL × EN, which shortened to «DE GRAFIEK · PRACTICE DATA» (459.4 px). The OEFENDATA label stays in the Dutch caption («OEFENDATA — verzonnen cijfers…») and the Japanese caption («練習データ：架空の数字で、練習用です。本当の調査ではありません。…»).

## 8. Toolchain

- **run.py interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0 (same venv that reproduced the core baseline 8/8 byte-identical; system python3 is also 3.12.3 but ships Pillow 10.2.0 and no cairosvg, so it was NOT used).
- **render.py (CairoSVG) interpreter:** tools/venv/bin/python — Python 3.12.3, Pillow 13.0.0, cairosvg 2.9.1 (system python3 lacks cairosvg, as the task states).
- **Pipeline:** one-process run.py (content12 → 34 → 56 → 7 → 8, so the exercise registry accumulates — never run modules standalone, never import them inside the core build dir, per README #11) → render.py (SVG → 1950×2700 PNG cards → print PDF via cairosvg+pypdf → web PDF JPEG q85 @1400 px).
- **svglib:** the Japanese-core svglib, md5 `d73e23b365676c3618d7e060b835eb4d` (copied from the W43 NL × JA build and verified; the canonical file itself was never edited). Its only code-comment CJK («for 重阳» in the JA core's own file) is not rendered and was left untouched.
- **Transform record:** build/transform.py (line-literal replacements with counts, plus fix rounds 1–3) maps the core build to this build; build/gates.py holds the rendered-SVG gate scans; build/rowcheck.py holds the same-baseline + P6 chart-label scans. The core build directory was copied, never modified; repointing covered every OUT spelling (expanduser form) in content12/34/56/7/8 and render.py, verified by grep (no production output path in the build code points at the core dir; the only core-dir references left are read-only: rowcheck.py reads the core SVGs for comparison, and transform.py holds the old strings as replacement sources).
- **Fix-round baselines:** pre-round sha256 of the edition's SVG/cards/PDFs written to build/fix1-baseline-sha256.txt (SVGs, pre-render), build/fix2-baseline-sha256.txt (18 files) and build/fix3-baseline-sha256.txt (18 files) before each re-render round, per the fix-round baseline rule.

## 9. Build rounds

1. **First render:** counts exact (150; levels/pages/types as §3), but P2 exercise overflow (match set needed 428 at y=2191) and P7 col-3 stack ending 2043 (crossing the zinnen rule) — fixed per §5 items 1–2.
2. **Fix 1:** zero build warnings; P2 ends 2402, P7 col-3 ends 1906 — but occlusion audit flagged 2 NEW P1 defects (word-note last line inside the IN HET KORT box) — fixed per §5 item 3.
3. **Fix 2:** zero build warnings; occlusion edition 0 / core 0 / NEW 0 — but the final word-list rescan caught one missed Chinese note (P8 #77 不定式) — fixed per §5 item 4.
4. **Fix 3:** zero build warnings; occlusion 0 / 0 / 0; p8 CLEAN 150=150; all gates in §4 re-run on the final render; P5 SVG byte-identical before/after (note-only change).

## 10. Delivery note

- This edition is delivered as **builder-complete only**. It is NOT finalized: finalization requires an independent proofread round (which must re-run every gate independently and must not take this KIT's values on trust).
- Files: `files/weekly-report-w45-nl-ja/` — `svg/` (8 SVGs), `cards/` (8 PNGs), `De-Lucerna-VOL2-JA.pdf` (20,540,632 bytes, 8 pages), `De-Lucerna-VOL2-JA-web.pdf` (3,584,046 bytes, 8 pages, under the 10 MB limit), `WEEKLY-KIT.md`, `ABSTRACT.txt`.
- NOT pushed to git, NOT posted to Discord, NOT messaged anywhere (per task instruction). Handoff to the parent agent for independent proofread and repo insert. Repo insert data: slug `2026-w45-nl-ja`, abstract heading `概要` (tables.json languages.ja.abstract_heading), web-PDF pins in §1 table below (verify at insert time from the actual file).

## 11. Final pins (disk-measured, final render)

| File | Bytes | SHA-256 |
|---|---|---|
| De-Lucerna-VOL2-JA.pdf (print, 8 pp.) | 20,540,632 | `64fb9b6d95ca844d0bc98fbfe85db96ec53c791dd54cfd574fec1da214f17b40` |
| De-Lucerna-VOL2-JA-web.pdf (web, 8 pp.) | 3,584,046 | `3b18ca1a9ca6b76114b8cccd3f40999c41cf5eff829829287b0af170870cbbf4` |
| svg/ ×8 · cards/ ×8 PNG (1950×2700) | — | rendered from the same single-process run.py + render.py round; full hashes in build/final-sha256.txt |
