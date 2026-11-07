# -*- coding: utf-8 -*-
"""Append the Round 3 fix record (D-KEY-42) to all 11 W46 JA WEEKLY-KIT.md files.

Appends only; earlier sections are never read for rewriting, only appended to.
Core gets a new ## §12 section; fan-outs get a Round 3 subsection at the end
of the existing §6 Fix history (the last section in every fan-out KIT).
Verifies after appending that each file grew by exactly the appended block
and that no earlier byte changed (checked by re-reading the prefix).
"""
import os

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")

NOTES = {
    "zh-cn": "在酉の市买熊手",
    "de": "Einen Kumade auf dem Tori-no-ichi kaufen",
    "en": "Buying a kumade at Tori-no-ichi",
    "es": "Comprar un kumade en Tori-no-ichi",
    "fr": "Acheter un kumade à Tori-no-ichi",
    "it": "Comprare un kumade a Tori-no-ichi",
    "ko": "도리노이치에서 구마데 사기",
    "nl": "Een kumade kopen op Tori-no-ichi",
    "pt": "Comprar um kumade em Tori-no-ichi",
    "ru": "Покупка кумадэ на Тори-но-ити",
    "zh-tw": "在酉の市買熊手",
}
DIRS = {"zh-cn": "weekly-report-w46-ja-core"}
for c in ["de", "en", "es", "fr", "it", "ko", "nl", "pt", "ru", "zh-tw"]:
    DIRS[c] = f"weekly-report-w46-ja-{c}"

FIT = {
    "zh-cn": "single line, width 292.8 of 434 (slack 141.2), y unchanged 1428.984",
    "de": "WRAPS to two lines: full width 466.1 exceeds the 434 column, so wrap() splits after `Tori-no-ichi` (line 1 width 419.0, line 2 `kaufen` at y=1383.5); line-1 y unchanged 1368.877, keys-flow end-y unchanged 2535.0, kinsoku/orphan scan 0. The wrap breaks at a space before `kaufen`, no bracket/punctuation split; the same edition's P8 already wraps keys 68 (`Schrein`) and 97 (`(Donnerstag)`) onto single-word second lines. Flagged for the Round 3 proofreader; no note or font was changed to avoid it, per the specified fix.",
    "en": "single line, width 407.9 of 434 (slack 26.1), y unchanged 1428.984",
    "es": "single line, width 421.2 of 434 (slack 12.8), y unchanged 1396.854",
    "fr": "single line, width 405.8 of 434 (slack 28.2), y unchanged 1368.877",
    "it": "single line, width 419.7 of 434 (slack 14.3), y unchanged 1368.877",
    "ko": "single line, width 351.0 of 434 (slack 83.0), y unchanged 1368.877",
    "nl": "single line, width 411.3 of 434 (slack 22.7), y unchanged 1424.831",
    "pt": "single line, width 429.3 of 434 (slack 4.7), y unchanged 1424.831",
    "ru": "single line, width 406.7 of 434 (slack 27.3), y unchanged 1424.831",
    "zh-tw": "single line, width 292.8 of 434 (slack 141.2), y unchanged 1428.984",
}
GATES = {
    "zh-cn": "freeze baseline 8/8, freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff []",
    "de": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "en": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "es": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "fr": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "it": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "ko": "freeze diff exit 1 adjudicated legitimate: added-char set and total (308 distinct, 3464 instances, all Hangul) byte-identical to Round 2; p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "nl": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "pt": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "ru": "freeze diff exit 0 (0 added CJK); p8 compare CLEAN 150/150, keydiff [137, 138] (adjudicated redirects, as Round 2)",
    "zh-tw": "freeze diff exit 1 adjudicated legitimate: added-char set and total (158 distinct, 849 instances) byte-identical to Round 2; p8 compare CLEAN 150/150, keydiff [138] (adjudicated redirect, as Round 2)",
}
SIZES = {
    "zh-cn": "web PDF 2,496,765 bytes (< 7 MB), 44,850 pdftotext bytes, byte-identical to the print PDF (24,795,357 bytes); text.md 44,225 bytes",
    "de": "web PDF 2,366,010 bytes (< 7 MB), 47,006 pdftotext bytes, byte-identical to the print PDF (29,500,005 bytes); text.md 46,360 bytes",
    "en": "web PDF 2,318,038 bytes (< 7 MB), 46,160 pdftotext bytes, byte-identical to the print PDF (27,837,881 bytes); text.md 45,553 bytes",
    "es": "web PDF 2,346,165 bytes (< 7 MB), 47,786 pdftotext bytes, byte-identical to the print PDF (28,725,845 bytes); text.md 47,128 bytes",
    "fr": "web PDF 2,344,133 bytes (< 7 MB), 47,681 pdftotext bytes, byte-identical to the print PDF (28,745,818 bytes); text.md 47,041 bytes",
    "it": "web PDF 2,337,476 bytes (< 7 MB), 47,561 pdftotext bytes, byte-identical to the print PDF (28,720,420 bytes); text.md 46,902 bytes",
    "ko": "web PDF 2,395,657 bytes (< 7 MB), 48,533 pdftotext bytes, byte-identical to the print PDF (26,585,657 bytes); text.md 47,942 bytes",
    "nl": "web PDF 2,340,934 bytes (< 7 MB), 46,815 pdftotext bytes, byte-identical to the print PDF (28,723,682 bytes); text.md 46,163 bytes",
    "pt": "web PDF 2,348,982 bytes (< 7 MB), 47,582 pdftotext bytes, byte-identical to the print PDF (28,727,059 bytes); text.md 46,951 bytes",
    "ru": "web PDF 2,254,305 bytes (< 7 MB), 54,276 pdftotext bytes, byte-identical to the print PDF (24,646,231 bytes); text.md 53,638 bytes",
    "zh-tw": "web PDF 2,872,569 bytes (< 7 MB), 44,829 pdftotext bytes, byte-identical to the print PDF (27,062,375 bytes); text.md 44,204 bytes",
}
ENDY = {"zh-cn": "2514.9", "de": "2535.0", "en": "2532.0", "es": "2536.2",
        "fr": "2535.0", "it": "2535.0", "ko": "2520.4", "nl": "2537.4",
        "pt": "2533.5", "ru": "2524.0", "zh-tw": "2514.9"}

SOURCE_LINE = {
    "zh-cn": "core build `hidden_files/weekly-report-w46-ja-build/content34.py:95`, the single registry source (`e.ex` key argument)",
    "zh-tw": "regenerated by `hidden_files/w46/gen_ja_zhtw.py` from the fixed core (MAP untouched, 187 entries); this build's `content34.py:95` carries the new key with the Traditional note",
}
for c in ["de", "en", "es", "fr", "it", "ko", "nl", "pt", "ru"]:
    SOURCE_LINE[c] = (f"regenerated by this edition's `transform.py` from the fixed core "
                      f"(no transform-table edit); this build's `content34.py:95` carries "
                      f"the new key with the unchanged {c.upper()} note")


def core_block(code):
    note = NOTES[code]
    return f"""
## §12 Fix record — Round 3 proofread defect D-KEY-42 (fix worker, 2026-11-03)

Round 2 verdict: FAIL on D-KEY-42 only (all Round 1 defects confirmed
fixed). Fix applied at the source; edition fully re-rendered; re-gated
on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix-round3/`). Round 3 independent proofread
still required; this re-gating does not replace it.

- D-KEY-42 (P8 key 42 omits a stem piece, BLOCKING, all 11 editions):
  P3 stem item 42 is `酉の市で / 熊手を / 買います → ___` (造句).
  The printed P8 key omitted the location piece `酉の市で`, while
  all 7 sibling 造句 keys (39, 40, 41, 133, 134, 135, 136) include
  every stem piece. Source: {SOURCE_LINE[code]}.
  Before (P8 key 42): `42. 熊手を買います。 — {note}`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — {note}`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  The article sentence `酉の市では、熊手を買います。` (content34.py:24)
  is unchanged. No SVG/PDF was hand-edited; no other string was
  reworded. Fit: {FIT[code]}.
- Change isolation: SVG text-multiset diff vs the pre-fix snapshot
  shows exactly one changed text in this edition (the key-42 line);
  hash check over the 132 edition files shows only the P8 SVG, both
  PDFs, and the .text.md changed in this edition (P1–P7 SVGs and
  ABSTRACT.txt byte-identical). Round 1 fixes survive: `svglib.py`
  md5 unchanged (74177544422fe677639d769cd80499fb, NO_END block
  intact), `CANON_SVGLIB_MD5` guards unchanged, zh-tw MAP 187 entries
  with all 8 Traditional conversions intact, SC scan still clean.
- Re-gate (final artifacts): {GATES[code]}; occlusion audit 0 flags
  (synthetic selftest passed); kinsoku scan start 0 / end 0 / orphan 0;
  counts 150 (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38),
  stems and keys 1–150 complete, sibling 造句 keys 39/40/41/133/134/
  135/136 unchanged and complete, P6 bars 480/720/780/1020 with all
  labels + practice-data label, P7 phrases 2× verbatim, keys-flow
  end-y {ENDY[code]}; {SIZES[code]}. P8 card visually checked at full
  frame: key 42 correct, no overflow, overlap, or tofu.
"""


def fanout_block(code):
    note = NOTES[code]
    return f"""
Fix record — Round 3 proofread defect D-KEY-42 (fix worker, 2026-11-03).
Round 2 verdict: FAIL on D-KEY-42 only (all Round 1 defects confirmed
fixed). Fix applied at the source in the core build and propagated by
regeneration; this edition was fully re-rendered through the pipeline
in §5 and re-gated on the final artifacts (gate JSONs/logs under
`hidden_files/w46/ja-fix-round3/`). Round 3 independent proofread
still required.

- D-KEY-42 (P8 key 42 omits a stem piece, BLOCKING, all 11 editions):
  P3 stem item 42 is `酉の市で / 熊手を / 買います → ___` (造句).
  The printed P8 key omitted the location piece `酉の市で`, while
  all 7 sibling 造句 keys (39, 40, 41, 133, 134, 135, 136) include
  every stem piece. Source: {SOURCE_LINE[code]}.
  Before (P8 key 42): `42. 熊手を買います。 — {note}`
  After (P8 key 42): `42. 酉の市で熊手を買います。 — {note}`
  The reader-language note is UNCHANGED. The P3 stem is unchanged.
  No SVG/PDF was hand-edited; no other string was reworded.
  Fit: {FIT[code]}.
- Change isolation: SVG text-multiset diff vs the pre-fix snapshot
  shows exactly one changed text in this edition (the key-42 line
  {"plus its `kaufen` wrap continuation" if code == "de" else ""});
  hash check over the 132 edition files shows only the P8 SVG, both
  PDFs, and the .text.md changed in this edition (P1–P7 SVGs and
  ABSTRACT.txt byte-identical). Round 1 fixes survive (kinsoku 0/0/0,
  abstracts unchanged, zh-tw conversions intact where applicable).
- Re-gate (final artifacts): {GATES[code]}; occlusion audit 0 flags
  (synthetic selftest passed); kinsoku scan start 0 / end 0 / orphan 0;
  counts 150 (A2 46 / B1 75 / B2 29, per-page 10/18/18/18/18/18/12/38),
  stems and keys 1–150 complete, sibling 造句 keys unchanged and
  complete, P6 bars 480/720/780/1020 with all labels + practice-data
  label, P7 phrases 2× verbatim, keys-flow end-y {ENDY[code]};
  {SIZES[code]}. P8 card visually checked at full frame: key 42
  correct, no overflow, overlap, or tofu.
"""


for code, d in DIRS.items():
    path = os.path.join(GOAL, "files", d, "WEEKLY-KIT.md")
    with open(path, encoding="utf-8") as fh:
        before = fh.read()
    block = core_block(code) if code == "zh-cn" else fanout_block(code)
    assert "D-KEY-42" not in before, f"{code}: Round 3 record already present?"
    assert before.endswith("\n"), f"{code}: KIT does not end with newline"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(before + block)
    with open(path, encoding="utf-8") as fh:
        after = fh.read()
    assert after == before + block, f"{code}: prefix changed during append!"
    print(code, "appended", len(block), "chars; total lines:", after.count("\n"))
print("KIT-APPEND-DONE")
