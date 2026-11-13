# EDITION-RECORD — 2026-w47-zh-cn-ko (Korean explanations)

## Verdict

**COMPLETE — all gates green on the final files.** Builder handoff, NOT a
finalisation claim: independent proofreading is still owed by the parent
line. No commit, no push, no insert, no lint run by this builder.

## Final artifacts

| File | Bytes | SHA-256 |
|---|---|---|
| `Lucerna-VOL4-KO.pdf` (print) | 36,966,399 | `7a664d88cd6f129463c2a9d5a8946c54b5db3c8f45a95aab27bf20300509a3ce` |
| `Lucerna-VOL4-KO-web.pdf` (web) | 2,818,175 | `64085a3e92316c72a20c63f0dd5f294ce22e2db6d919be61069660881390cdcc` |
| `2026-w47-zh-cn-ko.text.md` | 52,732 | `cce71e996d494135c6c82f1f744676186119b46d8f46737112ac920a1947c904` |
| `ABSTRACT.txt` | 314 | matches `tables.py` ABSTRACT['ko'] + newline |

## Fixes applied in #3 (2026-11-11)

None needed. First `run.py`: RC=0 TOTAL 150, ALL PASS on the first run
(0 overflow, teaser 2531.76, keys 2475.7; only 2 keys wrap to 2 lines,
Q13 and Q109, with 84.3 px spare). All heads, the calendar title, the
P4 gloss and the P2 word cards fit as built.

Pre-build checks (no changes):

1. **Kana pre-scan of the ko table values: 0 strays** (no
   hiragana/katakana in any of the 280 ko values).
2. **Hanzi-added accounting (`hanzi_ko.py`, mirroring `freeze.py`'s
   multiset counting, Hanzi only): 0 added on all 8 pages** (P1 739→725,
   P2 913→909, P3 752→748, P4 647→643, P5 802→798, P6 787→783, P7
   618→612, P8 962→944 — counts fall only). The two 双 occurrences in
   the ko table are the shared table's rendering of “Double 11” in the
   writing prompt and the “双11词语卡” header (also written 双11 in
   every other edition this week); the accounting proves neither adds
   Hanzi against the core on its page, so no “더블 11” replacement was
   needed — unlike the W46 build, where three stray 双11s in Korean
   explanations had to be replaced.
3. `WEEKLY-KIT.md` rewritten for ko (was an untranslated copy of the
   core KIT, pairing zh-cn × en).

## Gates (final files)

`gates-zhcn.py` (`gates-ko.log`): **11/11 PASS, OVERALL ALL PASS.**

| Gate | Result |
|---|---|
| occlusion | rc=0, 0 flags (selftest OK) |
| img_overlap | 0 hits |
| p8_extract | 150/150 |
| p8_compare | CLEAN, keydiffs 0 |
| freeze_sha256 | run rc=0, match 8/8 |
| print_web_text | 8/8 pages, posdiff 0, msdiff 0 (P1 253, P2 263, P3 205, P4 263, P5 208, P6 229, P7 280, P8 998) |
| pdftotext_nonempty | print 46,019 B, web 46,019 B |
| p8_fontsize | answer-zone min 9.98 pt, median 9.98 pt (≥ 9.75), spans 1000 |
| p8_chips | A2 11 / B1 24 / B2 3 = core |
| u2019 | 0 files |
| s11_svg | off-palette {}, no gold, 0 stroked rects, VOL.5 = core (1), paper #fbfaf6 × 8 |

Plus: `run.py` RC=0 TOTAL 150 (A2 56 / B1 69 / B2 25; pages
10/18/18/18/18/18/12/38), 0 overflow; P7 teaser ends 2531.76; P8 keys
end 2475.7; `freeze.py baseline` core 8/8 byte-identical (venv Pillow
13.0.0 / FreeType 2.14.3, core integrity confirmed); `freeze.py diff
--strict-cjk` TOTAL added CJK **4040** (p1 322, p2 323, p3 215, p4 264,
p5 221, p6 306, p7 660, p8 1729) — EXPECTED, adjudicated by Hanzi-added
accounting above (added Hanzi = 0 on all 8 pages), NOT a failure
(`freeze-diff-ko.log`); leak scan over all 275 translate sources vs
final SVG + text.md: **0 real leaks** (`leak-ko.log`); phrases of the
week all 8 exactly 2×.

## 150-key verification

- `p8.py extract --total 150`: noted set = 150 of 150, keys 1–150 all
  present (gates log `p8_extract`).
- `p8.py compare` core vs edition: **CLEAN**, keydiffs 0 (gates log
  `p8_compare`).
- Registry: `run.py` TOTAL 150, same level/page/type split as the core.

## Visual

- P1: badge Korean-only on the masthead rule (no Hanzi in the badge);
  press-time line visible. PASS.
- P2: calendar title “이번 주 날짜” fully visible, clear of the valley
  photo; all 4 word cards inside their boxes, examples 1 line. PASS.
- P4: Notes box 6 lines, bottom clear of “GEN，” below; C head “일정
  읽기” fits. PASS.
- P5: C head “시간과 숫자” fits. PASS.
- P7: teaser band ends 2531.76, clear of footer. PASS.
- P8: D head “읽고 답하기” fits; test sections A–F, keys 1–150 +
  footer clear. PASS.
- P3/P6: unchanged since transform.

## Logs (this dir)

`transform-ko.log`, `run-ko.log`, `p8sim-ko.log`, `render-ko.log`,
`webpdf-ko.log`, `gates-ko.log`, `freeze-diff-ko.log`, `hanzi-ko.log`,
`leak-ko.log`, `vis-ko-p1/p2/p4/p5/p7/p8.png`.
