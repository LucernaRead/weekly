# WEEKLY-KIT — Lucerna 简体中文周报 VOL.3 (W46), zh-cn × de

## Identity and spec

- **Issue week:** Monday 2026-11-09 to Sunday 2026-11-15. VOL.3.
- **Pairing:** zh-cn × de — Simplified Chinese body text with a German
  explanation layer, the edition for German-speaking readers. P1 badge
  (Latin-only, W45 precedent): “CHINESISCHER TEXT (VEREINFACHT) ·
  DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER”.
- **Masthead:** bare `Lucerna` (no article). Every page footer reads
  “Lucerna · CHINESISCHE WOCHENZEITUNG VOL.3 · TEXT AUF CHINESISCH
  (VEREINFACHT) · ERKLÄRUNGEN AUF DEUTSCH”; page line “Seite {n} von 8”.
  Gloss prefix “HINWEIS · ”. P8 separator “— Seite {n} —”. P7 phrase tags
  “S. N”.
- **Format:** 8 pages, 1950×2700 px, 4 columns, same geometry as the core.
  150 exercises, unified numbering 1–150, P8 keys generated from the
  registry. Core text frozen (see below); only the explanation layer was
  rewritten, natively in German.
- **Status:** builder self-check complete (see gates below). Builder
  handoff, NOT a finalisation claim — independent proofreading is still
  owed by the parent line. No Discord, no chat dumps, no repo push.

## Contents

Identical to the core edition (`files/weekly-report-w46-zh-cn-core/
WEEKLY-KIT.md` — contents table, trend sources, W45-promise handling,
image authorisations). This KIT records only what differs: the German
explanation layer, the transform, and the gates.

## Frozen-core proof

- Built by copying the finished W46 core build dir and applying exact-
  string replacements (282 keys, `hidden_files/w46/maps/de.json`,
  `hidden_files/w46/transform.py` — every key asserted found; coverage
  checked with `hidden_files/w46/coverage.py`: all English display strings
  covered or explicitly frozen).
- `tools/freeze.py diff --strict-cjk` core vs this edition: **TOTAL added
  CJK characters: 0** (exit 0). All Simplified Chinese core text is
  byte-identical in substance; CJK counts fall only where English strings
  were replaced.
- Phrases of the week: all 8 exactly 2× (article + P7) in the final SVGs.
- Photo credits kept in English (W45 precedent). Pinyin kept; English
  glosses translated.

## Adjudications (for the independent proofreader)

- **Badge is Latin-only:** the core badge's Chinese half (“简体中文正文 ·
  英语讲解”) is replaced wholesale by the Latin badge, per the W45 DE
  precedent — otherwise the word “德语” would add a CJK character the core
  does not have and fail strict-CJK. No Chinese reader-facing label for
  the explanation language is printed.
- **Press-time line shortened:** “Redaktionsschluss: 2. Nov. — noch offen”
  (the full English line does not fit the calendar box in German; the
  longer disclosure paragraph above it still states that the finalists
  were not known at press time).
- **German notes shortened for the P8 keys budget:** the first DE build
  overflowed the P8 keys flow (9 FLOW OVERFLOW warnings, keys drawn past
  the footer). Notes were shortened in the mapping (terse forms, same
  meaning) and the issue re-rendered; the final build has zero overflow
  warnings and the simulated keys flow ends at y = 2397 (bottom 2540).
  Three exercise heads were also shortened (“Lesen & wählen”,
  “Zeiten & Zahlen”, “Lesen & antworten”) after HEAD TOO WIDE warnings.
- **Comma-after-CJK:** two German notes were reworded to use “—” instead
  of a comma directly after a CJK character (e.g. “Pakete nehmen 个 —
  nicht 只 oder 条.”), because the typesetter converts such commas to
  full-width “，” and that would add a CJK character under strict-CJK.
- **P7 B1 example:** “So wird aus dem englischen «Monday, Nov 9» …” —
  the German explanation keeps the English example sentence, as in W45.

## Gates (final render)

- Driver: TOTAL 150, levels A2 56 / B1 69 / B2 25, pages
  10/18/18/18/18/18/12/38, writing model 164 characters, **zero** FLOW
  OVERFLOW / HEAD TOO WIDE warnings.
- Occlusion audit (`tools/occlusion_audit.py`, selftest first): **0 flags**.
- Same-baseline ink-collision scan (`hidden_files/w46/rowcheck.py`):
  **0 flags**.
- `tools/p8.py extract --total 150`: noted set = 150 of 150.
- `tools/freeze.py diff --strict-cjk`: added CJK = 0 (see above).
- Web PDF (`tools/webpdf.py`): `Lucerna-VOL3-DE-web.pdf`, 2,512,308
  bytes (< 7 MB); `pdftotext` output byte-identical to the print PDF
  (`Lucerna-VOL3-DE.pdf`, 41,752,800 bytes). Print PDF kept in the edition
  dir.
- Visual check: P8 card read in full after the final render (keys end
  cleanly above the footer rule); P1/P2 cards spot-checked for the two
  fixed box-title areas.
- Files: 8 SVGs in `svg/`, 8 cards PNG, print + web PDFs, `ABSTRACT.txt`
  (German), `2026-w46-zh-cn-de.text.md` (exported from the source
  manuscript with `hidden_files/w46/textmd.py`, never from PDF), this KIT.

## Reproduction

```bash
cd hidden_files/weekly-report-w46-zh-cn-de-build
../../tools/venv/bin/python run.py
../../tools/venv/bin/python render.py
cd ../../tools
./venv/bin/python occlusion_audit.py --selftest
./venv/bin/python occlusion_audit.py ../files/weekly-report-w46-zh-cn-de
./venv/bin/python p8.py extract --p8 ../files/weekly-report-w46-zh-cn-de/svg/p8-ceyan.svg --total 150
./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w46-zh-cn-core/svg --edition-svg ../files/weekly-report-w46-zh-cn-de/svg --strict-cjk
./venv/bin/python webpdf.py ../files/weekly-report-w46-zh-cn-de/svg ../files/weekly-report-w46-zh-cn-de/Lucerna-VOL3-DE-web.pdf
python3 ../w46/textmd.py 2026-w46-zh-cn-de ../files/weekly-report-w46-zh-cn-de/2026-w46-zh-cn-de.text.md
```

To rebuild from the core: copy the core build dir, repoint OUT paths to
`files/weekly-report-w46-zh-cn-de/svg`, apply `hidden_files/w46/maps/
de.json` with `hidden_files/w46/transform.py`, then run as above.

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
- **Fix (before → after, stem only):** `我拿了一个___包裹。` → `我拿了___包裹。` Completed with the key: `我拿了个包裹。` — grammatical, no doubling. Applied at the source: `content7.py:20` in all 10 build dirs (core `weekly-report-w46-zhcn-build` + 9 fan-out builds). No transform-map change was needed or made — the stem occurs nowhere in `hidden_files/w46/maps/*.json` (grep 0). Key `个` unchanged; P8 note 101 unchanged in this edition: `101. 个 — 包裹 nimmt das Zählwort 个 gè.`. No other stem, key, note, clinic line, or glossline was touched.
- **Re-render:** full re-render of all 10 editions from source (run.py → render.py → `tools/webpdf.py` → textmd.py, same drivers as the D3/D4 fix); 0 FLOW OVERFLOW / HEAD TOO WIDE in every driver log; counts 150 (A2 56 / B1 69 / B2 25), per-page 10/18/18/18/18/18/12/38, writing model 164. `.text.md` regenerated from the source manuscript: diff vs the pre-fix copy is exactly 1 changed line (line 1379, the stem) in this edition; headers verbatim. Change footprint vs the pre-fix snapshot: exactly 5 content files changed per edition (`.text.md`, print PDF, web PDF, `svg/p7-ciyu.svg`, `cards/p7-ciyu.png`) plus this KIT append — all other 15 edition files byte-identical, including P8 SVG + card (hash proof in the fix report).
- **Re-gates on final artifacts (all 10):** occlusion audit 0 flags (selftest OK); freeze `--strict-cjk` added CJK 0 every page for the 8 Latin/RU editions, JA total added 4908 and KO total added 4304 (identical to the Round 1/2 adjudicated figures; core P7 CJK total 741 → 739, exactly the 2 removed characters, all other pages unchanged); p8.py extract 150/150 + compare CLEAN, keydiff [] per edition (D3/D4 keys 25.d/26.c/27.b/99.a/100.b verified in this edition's native P8 rendering); rowcheck section 1 CLEAN all 8 pages (section 2 crash on hardcoded `p6-verdieping.svg` is the known N/A; note: the copied gate script's relative `../files` path crashed from `hidden_files/w46`, re-run with absolute paths — script in the fix dir patched); counts/phrases/chart/kinsoku as in the D3/D4 record; web PDFs 8 pages, ≤ 7 MB, pdftotext bytes > 0 and byte-identical web vs print; freeze baseline for the core 8/8 SHA-identical. Visual: P7 at full frame in all 10 editions — fixed stem clean on one line, no overflow/re-wrap orphan, error clinic + A2 column unchanged and consistent. SVG-text multiset diff vs pre-fix rebuilds: the ONLY string change in every edition is the item-101 stem. Gate evidence: `hidden_files/w46/zh-cn-fix-round3/gates/`. The ES `p.` fix and the D3/D4 key fixes survive unchanged (verified by grep + registry dump diff = exactly the stem line).
- **This edition after this fix:** `.text.md` 43166 bytes; web PDF 2512298 bytes; pdftotext 46142 bytes (web == print, −6 bytes vs the pre-fix figure — exactly the 2 removed CJK characters); print PDF 41752791 bytes. The figures in the "Gates (final render)" section above describe the PRE-fix render; the figures in this record supersede them.- **Status after this fix:** re-gated clean by the fix worker; Round 3 independent proofread (P7 scope per the Round 2 verdict §5) is still owed before shipping. No push, no insert, no Discord post, no chat dump.
