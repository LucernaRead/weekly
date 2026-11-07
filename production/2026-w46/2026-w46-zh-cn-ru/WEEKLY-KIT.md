# WEEKLY-KIT — Lucerna 简体中文周报 VOL.3 (W46), zh-cn × ru

## Identity and spec

- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. VOL.3.
- **Pairing:** zh-cn × ru — Simplified Chinese body text with a Russian
  explanation layer, the edition for Russian-speaking readers. P1 badge
  (Cyrillic-only, W45 precedent): “ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ) ·
  ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ”.
- **Masthead:** bare `Lucerna` (no article). Every page footer reads
  “Lucerna · КИТАЙСКИЙ (УПРОЩЁННЫЙ) ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА
  КИТАЙСКОМ (УПРОЩЁННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ”; page line “Страница
  {n} из 8”. Gloss prefix “Пояснение — ”. P8 separator “— СТРАНИЦА {n} —”.
  P7 phrase tags “Страница N” (W45 RU precedent). Model answer “Образец: ”.
- **Format:** 8 pages, 1950×2700 px, 4 columns, same geometry as the core.
  150 exercises, unified numbering 1–150, P8 keys generated from the
  registry. Core text frozen (see below); only the explanation layer was
  rewritten, natively in Russian.
- **Status:** builder self-check complete (see gates below). Builder
  handoff, NOT a finalisation claim — independent proofreading is still
  owed by the parent line. No Discord, no chat dumps, no repo push.

## Contents

Identical to the core edition (`files/weekly-report-w46-zh-cn-core/
WEEKLY-KIT.md` — contents table, trend sources, W45-promise handling,
image authorisations). This KIT records only what differs: the Russian
explanation layer, the transform, and the gates.

## Frozen-core proof

- Built by copying the finished W46 core build dir and applying exact-
  string replacements (282 keys, `hidden_files/w46/maps/ru.json`,
  `hidden_files/w46/transform.py` — every key asserted found; coverage
  checked with `hidden_files/w46/coverage.py`: all English display strings
  covered or explicitly frozen).
- `tools/freeze.py diff --strict-cjk` core vs this edition: **TOTAL added
  CJK characters: 0** (exit 0). All Simplified Chinese core text is
  byte-identical in substance; CJK counts fall only where English strings
  were replaced.
- Phrases of the week: all 8 exactly 2× (article + P7) in the final SVGs
  (joined-text counting).
- Photo credits kept in English (W45 precedent). Pinyin kept; English
  glosses translated.

## Adjudications (for the independent proofreader)

- **Badge is Cyrillic-only:** the core badge's Chinese half (“简体中文正文 ·
  英语讲解”) is replaced wholesale by the Cyrillic badge, per the W45 RU
  precedent — otherwise naming the reader language in Chinese would add
  CJK characters the core does not have and fail strict-CJK. No Chinese
  reader-facing label for the explanation language is printed.
- **Exercise heads shortened (Cyrillic is wide):** “A · 读一读选一选 ·
  Читай” (from “Прочитай и выбери” via “Читай и выбери” — both too
  wide), “B · 词语填空 · Пропуски”, “C · 图表读数 · Диаграмма” (HEAD TOO
  WIDE on P2–P6 in builds 1–2; the wide heads also overlapped the
  exercise lines below them — TEXTX flags — all cleared).
- **Box title shortened:** “本周句式 · Конструкция” (BOXTITLE flag in
  build 1).
- **P2 word-card label + gloss shortened:** “gāocháochǎng · пик
  распродажи” and “пик распродажи, с 10 нояб. 20:00” — the long label
  wrapped to an extra line, pushing the gloss below the card into the
  sentence under it (TEXTX + LINEX flags in build 1; clean after).
- **P8 keys notes shortened:** five long notes shortened in the mapping
  (terse forms, same meaning) after one FLOW OVERFLOW warning in build 1;
  the final simulated keys flow ends at y = 2427 (bottom 2540),
  161 wrapped lines. The open-task note template was also shortened:
  “Открытое задание — образец в разделе F ({NCHARS})”.
- **Comma-after-CJK:** two Russian notes were reworded to use “—” instead
  of a comma directly after a CJK character (e.g. “Посылки берут 个 —
  не 只 и не 条.”), because the typesetter converts such commas to
  full-width “，” and that would add a CJK character under strict-CJK.
- **P7 B1 example:** the Russian explanation keeps the English example
  sentence (“So English «Monday, Nov 9» becomes …”), as in W45.
- **`.text.md` tool fix:** `hidden_files/w46/textmd.py` initially dropped
  pure-Cyrillic display strings (its filter only kept strings with a CJK
  or Latin run), so the first RU export was 1472 lines. The filter was
  fixed to also accept Cyrillic/kana/Hangul runs; the shipped RU export
  is 1884 lines, and a DE re-export with the fixed tool is byte-identical
  to the original DE file.

## Gates (final render)

- Driver: TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 164 characters, **zero** FLOW
  OVERFLOW / HEAD TOO WIDE warnings.
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): **0 flags**.
- Same-baseline ink-collision scan (`hidden_files/w46/rowcheck.py` §1):
  all 8 pages CLEAN (§2 hardcodes the NL P6 filename and does not run for
  this family; P6 chart rects verified directly: 220/330/550/770 px from
  x=325).
- `tools/p8.py extract --total 150`: noted set = 150 of 150.
- `tools/p8.py compare` core vs edition P8: status CLEAN (missing = [],
  extra = 0, keydiff = []).
- `tools/freeze.py diff --strict-cjk`: added CJK = 0 (see above).
- Web PDF (`tools/webpdf.py`): `Lucerna-VOL3-RU-web.pdf`, 2,275,745
  bytes (< 7 MB), 55,440 text bytes; `pdftotext` output byte-identical to
  the print PDF (`Lucerna-VOL3-RU.pdf`, 30,430,920 bytes). Print PDF kept
  in the edition dir.
- Visual check: P8 card read in full after the final render (keys end
  cleanly above the footer rule); P1/P2 cards spot-checked for the fixed
  head and word-card areas.
- Files: 8 SVGs in `svg/`, 8 cards PNG, print + web PDFs, `ABSTRACT.txt`
  (Russian), `2026-w46-zh-cn-ru.text.md` (exported from the source
  manuscript with the fixed `hidden_files/w46/textmd.py`, never from
  PDF), this KIT.

## Reproduction

```bash
cd hidden_files/weekly-report-w46-zh-cn-ru-build
../../tools/venv/bin/python run.py
../../tools/venv/bin/python render.py
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-zh-cn-ru
./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-zh-cn-ru/svg/p8-ceyan.svg --total 150
./venv/bin/python p8.py compare --core-p8 ../files/weekly-report-w46-zh-cn-core/svg/p8-ceyan.svg --edition-p8 ../files/weekly-report-w46-zh-cn-ru/svg/p8-ceyan.svg --total 150
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-zh-cn-core/svg --edition-svg ../files/weekly-report-w46-zh-cn-ru/svg --strict-cjk
./venv/bin/python webpdf.py ../files/weekly-report-w46-zh-cn-ru/svg ../files/weekly-report-w46-zh-cn-ru/Lucerna-VOL3-RU-web.pdf
python3 ../w46/textmd.py 2026-w46-zh-cn-ru ../files/weekly-report-w46-zh-cn-ru/2026-w46-zh-cn-ru.text.md
```

To rebuild from the core: copy the core build dir, repoint OUT paths to
`files/weekly-report-w46-zh-cn-ru/svg`, apply `hidden_files/w46/maps/
ru.json` with `hidden_files/w46/transform.py`, then run as above.

## Post-proof fix record

### Fix — Round 2 verdict D3 + D4 (blocking, frozen-core answer-key registry errors; 2026-11-03 fix worker; full Round 3 independent proofread still owed)

- **Trigger:** Round 2 proofreader verdict D3 + D4 (`hidden_files/w46/zh-cn-proofread-gates-round2/proofreader-verdict-round2.md`). Both defects lived in the shared frozen-core registry and were carried faithfully into every fan-out edition. No other change was made.
- **D3 (P2 matching, ex. 25-28):** printed P8 keys were `25. c / 26. b / 27. d` (28. a correct). Rendered right column: a. "北方冬天家里暖和，靠它" (= 供暖), b. "打开快递柜要用的号码" (= 取件码), c. "买的东西，装在里面送来" (= 包裹), d. "双11最忙的卖货时间" (= 高潮场). Correct keys: **25. d / 26. c / 27. b / 28. a**. Source: core build `content12.py:282`, keys `["c","b","d","a"]` -> `["d","c","b","a"]`, and the four P8 note trailing letters re-lettered to match (c/b/d/a -> d/c/b/a). List order 25-28 verified from source before editing.
- **D4 (P6 matching, ex. 99-100):** printed P8 keys were `99. b / 100. a` (97. c, 98. d correct). Rendered right column: a. "还没发生的事，先猜一猜" (= 预报), b. "提前放到离买家近的地方" (= 前置), c. "别人说的话，不一定是真的" (= 说法), d. "量出来的数字" (= 数据). Correct keys: **97. c / 98. d / 99. a / 100. b**. Source: core build `content56.py:226`, keys `["c","d","b","a"]` -> `["c","d","a","b"]`, and the two P8 note trailing letters re-lettered (b/a -> a/b). List order 97-100 verified from source before editing. (P8 prints `"{n}. {key} — {note}"`, so keys and note letters had to change together or the line would contradict itself.)
- **Applied in:** all 10 build dirs (`content12.py` + `content56.py` in each) and all 9 transform maps (`hidden_files/w46/maps/{de,es,fr,it,ja,ko,nl,pt,ru}.json`, 5 note entries re-lettered per map; rebuild-from-core reproducibility re-tested for ES: transform OK, 282 keys, match_set blocks byte-identical). Post-fix grep: no old key list remains in any build dir.
- **Full 150-key re-verification (core registry, static dump of all 130 `ex` + 5 `match_set`):** 145 keys confirmed correct, only 25/26/27/99/100 wrong — now corrected. All 5 matching sets checked option-by-option (P3 43-46 b/c/a/d, P4 61-64 d/c/b/a, P5 79-82 d/c/b/a confirmed correct). Arithmetic recomputed (260+90=350; 350-60=290); writing model 164 characters. Log: `hidden_files/w46/zh-cn-fix-keys/key-verification-log.md`. Flagged, NOT changed (pre-existing stem awkwardness, passed by the Round 2 proofreader; for Round 3/coordinator): ex. 101 stem reads "我拿了一个___包裹。" with key 个 — the stem already contains 一个 before the blank.
- **Re-render:** full re-render of all 10 editions from source; 0 FLOW OVERFLOW / HEAD TOO WIDE in every driver log; `.text.md` regenerated from the source manuscript (diff vs pre-fix copy = exactly the 5 corrected note lines per edition; headers preserved verbatim). Change footprint vs the pre-fix snapshot: exactly 5 files per edition changed (`.text.md`, print PDF, web PDF, `svg/p8-ceyan.svg`, `cards/p8-ceyan.png`) — P2/P6 SVGs are byte-identical because matching keys print only on P8.
- **Re-gates on final artifacts (all 10):** occlusion audit 0 flags (selftest OK); freeze `--strict-cjk` added CJK 0 every page for the 8 Latin/RU editions, JA total added 4908 and KO total added 4304 with KO Hanzi-added 0 (identical to Round 1 adjudicated figures); p8.py extract 150/150 + compare CLEAN, keydiff [] per edition; rowcheck section 1 CLEAN all 8 pages (section 2 crash on hardcoded `p6-verdieping.svg` is the known N/A); counts 150 (A2 56/B1 69/B2 25), per-page 10/18/18/18/18/18/12/38; P7 phrases 2x each; P6 chart rects exact; kinsoku 0; web PDFs 8 pages, <= 7 MB, pdftotext bytes > 0 and byte-identical web vs print; freeze baseline for the core 8/8 SHA-identical. The 5 corrected keys were verified printing correctly in this edition's native P8 rendering (25.d / 26.c / 27.b / 99.a / 100.b, key and note letter consistent). Visual: P1/P2/P6/P8 at full frame, zero defects. Gate evidence: `hidden_files/w46/zh-cn-fix-keys/gates/`.
- **Status after this fix:** re-gated clean by the fix worker; full Round 3 independent proofread of all 10 editions is still owed before shipping. No push, no insert, no Discord post, no chat dump.

### Fix — Round 2 verdict D5 (blocking, frozen-core ex. 101 stem; 2026-11-03 fix worker; Round 3 independent proofread still owed)

- **Trigger:** Round 2 proofreader verdict D5 (`hidden_files/w46/zh-cn-proofread-gates-round2/proofreader-verdict-round2.md`, §5) — the ONLY residual defect in Round 2. The earlier fix record's "Flagged, NOT changed" line for ex. 101 is superseded by this fix; that earlier text is left untouched above as history.
- **Defect:** ex. 101 stem `我拿了一个___包裹。` with key `个` completes to `我拿了一个个包裹` — a doubled classifier, ungrammatical. The issue's own P7 error clinic on the same page corrects exactly this error (`我拿了两个包裹个` → `我拿了两个包裹。`, "number + measure word + noun"), and the P7 A2 column above teaches `一个包裹`. The key is the correct measure word and was NOT changed.
- **Fix (before → after, stem only):** `我拿了一个___包裹。` → `我拿了___包裹。` Completed with the key: `我拿了个包裹。` — grammatical, no doubling. Applied at the source: `content7.py:20` in all 10 build dirs (core `weekly-report-w46-zhcn-build` + 9 fan-out builds). No transform-map change was needed or made — the stem occurs nowhere in `hidden_files/w46/maps/*.json` (grep 0). Key `个` unchanged; P8 note 101 unchanged in this edition: `101. 个 — 包裹 берёт счётное слово 个 gè.`. No other stem, key, note, clinic line, or glossline was touched.
- **Re-render:** full re-render of all 10 editions from source (run.py → render.py → `tools/webpdf.py` → textmd.py, same drivers as the D3/D4 fix); 0 FLOW OVERFLOW / HEAD TOO WIDE in every driver log; counts 150 (A2 56 / B1 69 / B2 25), per-page 10/18/18/18/18/18/12/38, writing model 164. `.text.md` regenerated from the source manuscript: diff vs the pre-fix copy is exactly 1 changed line (line 1379, the stem) in this edition; headers verbatim. Change footprint vs the pre-fix snapshot: exactly 5 content files changed per edition (`.text.md`, print PDF, web PDF, `svg/p7-ciyu.svg`, `cards/p7-ciyu.png`) plus this KIT append — all other 15 edition files byte-identical, including P8 SVG + card (hash proof in the fix report).
- **Re-gates on final artifacts (all 10):** occlusion audit 0 flags (selftest OK); freeze `--strict-cjk` added CJK 0 every page for the 8 Latin/RU editions, JA total added 4908 and KO total added 4304 (identical to the Round 1/2 adjudicated figures; core P7 CJK total 741 → 739, exactly the 2 removed characters, all other pages unchanged); p8.py extract 150/150 + compare CLEAN, keydiff [] per edition (D3/D4 keys 25.d/26.c/27.b/99.a/100.b verified in this edition's native P8 rendering); rowcheck section 1 CLEAN all 8 pages (section 2 crash on hardcoded `p6-verdieping.svg` is the known N/A; note: the copied gate script's relative `../files` path crashed from `hidden_files/w46`, re-run with absolute paths — script in the fix dir patched); counts/phrases/chart/kinsoku as in the D3/D4 record; web PDFs 8 pages, ≤ 7 MB, pdftotext bytes > 0 and byte-identical web vs print; freeze baseline for the core 8/8 SHA-identical. Visual: P7 at full frame in all 10 editions — fixed stem clean on one line, no overflow/re-wrap orphan, error clinic + A2 column unchanged and consistent. SVG-text multiset diff vs pre-fix rebuilds: the ONLY string change in every edition is the item-101 stem. Gate evidence: `hidden_files/w46/zh-cn-fix-round3/gates/`. The ES `p.` fix and the D3/D4 key fixes survive unchanged (verified by grep + registry dump diff = exactly the stem line).
- **This edition after this fix:** `.text.md` 51674 bytes; web PDF 2275750 bytes; pdftotext 55434 bytes (web == print, −6 bytes vs the pre-fix figure — exactly the 2 removed CJK characters); print PDF 30430935 bytes. The figures in the "Gates (final render)" section above describe the PRE-fix render; the figures in this record supersede them.
- **Observation, NOT fixed (out of scope, pre-existing):** on this edition's P7 card the dark VOL.4 teaser band (rect y=2518.52, height 118) and the footer line (y=2624) overlap visually — the footer string sits on the band's lower edge in dark type. The fix worker rebuilt the PRE-fix RU P7 from the reverted source in /tmp and compared SVG element geometry: all 188 P7 elements are geometrically identical pre/post fix, so this appearance predates the D5 fix and was left untouched per the D5-only scope. Referred to the Round 3 proofreader to judge. No other edition's P7 card showed this; the other 9 were read clean at full frame.
- **Status after this fix:** re-gated clean by the fix worker; Round 3 independent proofread (P7 scope per the Round 2 verdict §5) is still owed before shipping. No push, no insert, no Discord post, no chat dump.

### Fix — Round 3 verdict D6 (blocking, RU P7 footer on the dark teaser band; 2026-11-03 fix worker; Round 4 independent proofread still owed)

- **Trigger:** Round 3 proofreader verdict D6 (`hidden_files/w46/zh-cn-proofread-gates-round3/proofreader-verdict-round3.md`, §4/§4.6) — the ONLY residual defect in Round 3, RU edition only, pre-existing (predates the D5 fix; geometry comparison pre/post D5 showed 0 diffs). D5 is CONFIRMED fixed and is NOT disturbed by this fix; the other 9 editions PASS in Round 3 and are NOT touched.
- **Defect:** on RU P7 only, the dark VOL.4 teaser band sat over the footer: band rect `[183] y=2518.52 h=118` (bottom 2636.52) vs footer baseline y=2624 (12.52 px inside the band; footer ink ~2606–2629 entirely on the band); footer elements `[187]/[188]` fill `#57523f` on band `#2c2822` at 1.87:1 contrast (vs 6.94:1 on paper), effectively illegible at full frame. The footer rule line (y=2580) struck through the band interior. The canonical occlusion audit reported 0 flags — correct under its definitions (footer painted after the band; footer-baseline exemption) but blind to dark-on-dark contrast; the ruling rested on geometry + contrast + visual evidence, not on the audit.
- **Fix (before → after, geometry only, RU P7 only):** the teaser band WITH its two teaser lines was moved UP 70 px at the source, preserving their relative layout (title offset +44, sentence offset +84 from the band top, unchanged). Band: `y 2518.52 → 2448.52`, bottom `2636.52 → 2566.52` (≤ ~2570 as specified), clearing the footer rule line (y=2580) by 13.48 px and the footer ink top (~2606.40) by 39.88 px; the footer is restored to paper at 6.94:1 contrast. Applied at the source: RU build dir `content7.py` teaser `py` line only (`py = fy + 66 + 4 * 150 + 18 - 70`, with a D6 comment) — no SVG-only patch, no other build dir touched, no other source file touched. The footer was NOT recoloured (fill `#57523f` unchanged) and NOT moved (baseline y=2624, rule y=2580, unchanged). Band fill `#2c2822` unchanged. NO text changed anywhere: stem `我拿了___包裹。`, key `个`, P8 note 101 `101. 个 — 包裹 берёт счётное слово 个 gè.` all byte-identical to the Round 3 state (see the fix report for the multiset + `.text.md` proof).
- **Re-render:** RU edition only, from source with the family's own drivers (run.py → render.py → `tools/webpdf.py` → textmd.py, same drivers as the D3/D4 and D5 fixes); 0 FLOW OVERFLOW / HEAD TOO WIDE; counts 150 (A2 56 / B1 69 / B2 25), per-page 10/18/18/18/18/18/12/38, writing model 164; `P7 teaser ends 2566.52`. `.text.md` regenerated from the source manuscript and is BYTE-IDENTICAL to the pre-fix copy (51674 bytes, diff = 0 lines) — no text moved. Change footprint vs the pre-fix snapshot (210 edition files, before this KIT append): exactly 4 files changed, all RU — `svg/p7-ciyu.svg`, `cards/p7-ciyu.png`, print PDF, web PDF. All other RU files byte-identical (including all P1–P6/P8 SVGs and cards) and all 9 other editions byte-identical. Full P7 element-geometry comparison (189 elements incl. root): ONLY elements [183]/[184]/[185] differ, each y −70.00 exactly, everything else identical.
- **Re-gates on final artifacts (RU only):** occlusion audit 0 flags (selftest OK — planted classes BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX fired 1 each, clean controls silent; stated explicitly: the audit is blind to this contrast class and this verdict rests on geometry + visual, not on the audit); freeze `freeze.py diff --strict-cjk` added CJK 0, exit 0; p8.py extract 150/150 + compare CLEAN, missing=[], extra_count=0, keydiff=[]; P8 SVG + card byte-identical to the Round 3 hashes (20/20 P8 proof re-confirmed for RU: SVG `cdf804c1…958a116`, card `21daa9b9…4495`); PDF text layer web == print byte-identical, 8 pages, web PDF ≤ 7 MB. Visual: RU P7 at full frame + band/footer crop — footer fully legible on paper, band + teaser lines clean, no overlap with the footer rule or any other element, 21.48 px clear of the last phrase row's ink. Gate evidence: `hidden_files/w46/zh-cn-fix-round4/gates/`. Band-bottom comparison across all 10 editions after this fix (footer baseline 2624): core/FR/IT/JA/KO 2514.00, ES 2527.96, PT 2523.98, DE 2554.48, RU 2566.52, NL 2607.52 — RU is now inside the family range; no other edition needs this fix.
- **This edition after this fix:** `.text.md` 51674 bytes (unchanged); web PDF 2275749 bytes; pdftotext 55435 bytes (web == print; +1 byte vs the Round 3 figure 55434 — exactly one added blank-line separator in `pdftotext` output where the teaser/footer baseline gap grew from 21.48 to 91.48 px; non-blank lines and the character stream are identical, zero changed text lines); print PDF 30430934 bytes. The figures in the "Gates (final render)" section above and in the D5 record describe earlier renders; the PDF figures in this record supersede them (`.text.md` figure unchanged).
- **Status after this fix:** re-gated clean by the fix worker; RU-P7-only Round 4 independent proofread (per the Round 3 verdict §4.6) is still owed before shipping. No push, no insert, no Discord post, no chat dump.
