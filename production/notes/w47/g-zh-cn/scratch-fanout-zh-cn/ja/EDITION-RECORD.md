# EDITION-RECORD — 2026-w47-zh-cn-ja (Japanese explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-JA.pdf` (print) | 36,336,862 | `c395a505f050c4a592f338b1791d44779979b933c1dfc93b85a42070cc4353b6` |
| `Lucerna-VOL4-JA-web.pdf` (web) | 2,900,721 | `c620b9eefc22727fd14eb0b1cd249942d26393b94cf768ed219bb19ce74ba65a` |
| `2026-w47-zh-cn-ja.text.md` | 52,444 | `68d850eac576bd5854ba2265ffa9fe69754c2779e01cc0a8ca2cf63b104dd5e4` |
| `ABSTRACT.txt` | 315 | matches `tables.py` ABSTRACT['ja'] + newline |

## Fixes applied in #3 (2026-11-11)

First `run.py`: RC=0 TOTAL 150, ALL PASS on the first run (0 overflow,
teaser 2505.24, keys 2521.8) — no layout fixes needed. Two content/build
fixes followed:

1. **Small-kana `NO_START` extension (W45/W46 precedent):** added
   `NO_START += "ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ"` to the
   build copy's `svglib.py` only (never the canonical file). The W47
   canonical file has TWO `NO_START =` assignments (lines 164 and 190 —
   the kinsoku END pass and the kinsoku shori pass); the `+=` line was
   added after BOTH, since the END pass also consults `NO_START` via
   `_kinsoku_shed_piece`. Verified the canonical file has 0 `+=` lines.
   Re-ran `run.py`: identical numbers (teaser 2505.24, keys 2521.8) —
   no line breaks moved.
2. **Film titles kept in Simplified Chinese (3 notes):** the
   Chinese-run conservation check found the only non-furniture missing
   runs on P8: the P8-key notes rendered the two film titles in
   Traditional/Japanese kanji — “《我們僅有一次的人生》” (Q76, Q97)
   and “《珠穆朗瑪：雲中彼岸》” (Q94) — while the P5 article, the test
   stems and all other editions use Simplified “《我们仅有一次的人生》”
   / “《珠穆朗玛：云中彼岸》”. Fixed in `fresh.py` + `content56.py`
   (table diff = exactly those 3 ja lines); re-ran conservation to
   0 missing (badge excepted) and `run.py` to ALL PASS.
3. `WEEKLY-KIT.md` rewritten for ja (was an untranslated copy of the
   core KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-ja.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 238, P2 257, P3 201, P4 247, P5 203, P6 212, P7 216, P8 908) |
| pdftotext_nonempty | print 46,219 B, web 46,219 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75), spans 804 |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; P7 teaser ends 2505.24; P8 keys
end 2521.8; `freeze.py baseline` core 8/8 byte-identical (venv Pillow
13.0.0 / FreeType 2.14.3, core integrity confirmed); `freeze.py diff
--strict-cjk` TOTAL added CJK **4648** (p1 366, p2 371, p3 263, p4 331,
p5 260, p6 386, p7 787, p8 1884) — EXPECTED, adjudicated by Chinese-run
conservation, NOT a failure (`freeze-diff-ja.log`); **conservation**
(`conserve-ja-2.log`, `conserve_ja.py`): only 2 missing runs, both
adjudicated badge furniture (“简体中文正文”, “英语讲解”); P2–P8 0
missing; the 「决赛」 gloss sentence is conserved verbatim; leak scan
over all 275 translate sources vs final SVG + text.md: **0 real
leaks** (`leak-ja.log`); phrases of the week all 8 exactly 2×.

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (gates log `p8_extract`).
- `p8.py compare` core vs edition: **CLEAN**, keydiffs 0 (gates log
  `p8_compare`).
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Japanese-only on the masthead rule; press-time line
  visible; word box “「决赛」 juésài — 決勝、最後の試合。决赛是谁和谁打？
  赢了就是冠军。” verbatim. PASS.
- P2: calendar title “今週のカレンダー” fully visible, clear of the
  valley photo; all 4 word cards inside their boxes, examples 1 line.
  PASS.
- P4: Notes box 6 lines, bottom clear of “GEN，” below; C head
  “日程を読む” fits. PASS.
- P5: C head “時刻と数字” fits. PASS.
- P7: teaser band ends 2505.24, clear of footer. PASS.
- P8: D head “読んで答える” fits; test sections A–F, keys 1–150 +
  footer clear; Q76/Q94/Q97 simplified titles. PASS.
- P3/P6: unchanged since transform.

## Logs (this dir)

`transform-ja.log`, `run-ja.log`, `run-ja-2.log` (after NO_START),
`run-ja-3.log` (after title fixes), `render-ja.log`, `render-ja-2.log`,
`webpdf-ja.log`, `gates-ja.log`, `freeze-diff-ja.log`,
`conserve-ja.log`, `conserve-ja-2.log`, `leak-ja.log`,
`vis-ja-p1/p2/p4/p5/p7/p8.png`.
