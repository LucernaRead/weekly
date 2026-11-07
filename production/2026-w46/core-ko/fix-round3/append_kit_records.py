#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append the Round 3 fix record to all 11 W46 KO WEEKLY-KIT.md files.
Append-only: earlier sections are never touched. Asserts the Round 1
record is present exactly once and no Round 3 record exists yet."""
import os

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
W = os.path.join(GOAL, "hidden_files/w46/ko-fix-round3")

GLOSS_AFTER = {
 "zh-cn": "译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。",
 "de": "HINWEIS · 겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen",
 "en": "Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share",
 "es": "Nota — 겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir",
 "fr": "Note — 겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager",
 "it": "Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere",
 "ja": "解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う",
 "nl": "Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen",
 "pt": "Nota — 겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar",
 "ru": "Пояснение — 겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться",
 "zh-tw": "譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。",
}
GLOSS_BEFORE = {  # Round 1 post-fix form (entry deleted), i.e. the restored string minus the 가늘다 entry
 "zh-cn": "译注｜겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。",
 "de": "HINWEIS · 겹치다 = sich überschneiden · 감사하다 = danken · 나누다 = unterscheiden, teilen",
 "en": "Note — 겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share",
 "es": "Nota — 겹치다 = coincidir, solaparse · 감사하다 = agradecer · 나누다 = distinguir, compartir",
 "fr": "Note — 겹치다 = se chevaucher · 감사하다 = remercier · 나누다 = distinguer, partager",
 "it": "Nota — 겹치다 = sovrapporsi · 감사하다 = ringraziare · 나누다 = distinguere, condividere",
 "ja": "解説 — 겹치다 = 重なる · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う",
 "nl": "Uitleg — 겹치다 = samenvallen · 감사하다 = bedanken · 나누다 = onderscheiden, delen",
 "pt": "Nota — 겹치다 = sobrepor-se · 감사하다 = agradecer · 나누다 = distinguir, partilhar",
 "ru": "Пояснение — 겹치다 = совпадать · 감사하다 = благодарить · 나누다 = различать, делиться",
 "zh-tw": "譯注｜겹치다 重疊 · 감사하다 感謝 · 나누다 區分、分享。",
}
# (edition dir, web pdf name, print pdf name, textmd name, textmd bytes, textmd items,
#  web bytes, pdftotext bytes, print bytes, keydiff, koscan candidates, freeze-added note)
DATA = {
 "zh-cn": ("weekly-report-w46-ko-core", "Lucerna-VOL3-web.pdf", "Lucerna-VOL3.pdf",
           "2026-w46-ko-zh-cn.text.md", 27449, 338, 2528382, 50756, 32011292, "[137, 138]", 360, "n/a (core baseline)"),
 "de": ("weekly-report-w46-ko-de", "Lucerna-VOL3-web.pdf", "Lucerna-VOL3.pdf",
        "2026-w46-ko-de.text.md", 28128, 338, 2317186, 53316, 32911089, "[137, 138]", 357, "0"),
 "en": ("weekly-report-w46-ko-en", "Lucerna-VOL3-EN-web.pdf", "Lucerna-VOL3-EN.pdf",
        "2026-w46-ko-en.text.md", 27959, 338, 2292773, 52452, 32290743, "[137, 138]", 358, "0"),
 "es": ("weekly-report-w46-ko-es", "Lucerna-VOL3-ES-web.pdf", "Lucerna-VOL3-ES.pdf",
        "2026-w46-ko-es.text.md", 28264, 338, 2297594, 54064, 32467650, "[137, 138]", 357, "0"),
 "fr": ("weekly-report-w46-ko-fr", "Lucerna-VOL3-FR-web.pdf", "Lucerna-VOL3-FR.pdf",
        "2026-w46-ko-fr.text.md", 28287, 338, 2305618, 54155, 32499010, "[137, 138]", 361, "0"),
 "it": ("weekly-report-w46-ko-it", "Lucerna-VOL3-IT-web.pdf", "Lucerna-VOL3-IT.pdf",
        "2026-w46-ko-it.text.md", 28242, 338, 2288549, 53507, 32463409, "[137, 138]", 359, "0"),
 "ja": ("weekly-report-w46-ko-ja", "Lucerna-VOL3-web.pdf", "Lucerna-VOL3.pdf",
        "2026-w46-ko-ja.text.md", 28252, 339, 2661599, 53821, 36156863, "[137, 138]", 360, "2,664 (Round 2: 2,662; +2 = restored 細, Hangul added 0)"),
 "nl": ("weekly-report-w46-ko-nl", "Lucerna-VOL3-NL-web.pdf", "Lucerna-VOL3-NL.pdf",
        "2026-w46-ko-nl.text.md", 28108, 338, 2291086, 53178, 32464313, "[137, 138]", 358, "0"),
 "pt": ("weekly-report-w46-ko-pt", "Lucerna-VOL3-web.pdf", "Lucerna-VOL3.pdf",
        "2026-w46-ko-pt.text.md", 28267, 338, 2301018, 53675, 32469019, "[137, 138]", 358, "8 Hangul (unchanged adjudicated quoted sentence)"),
 "ru": ("weekly-report-w46-ko-ru", "Lucerna-VOL3-RU-web.pdf", "Lucerna-VOL3-RU.pdf",
        "2026-w46-ko-ru.text.md", 30342, 340, 2243389, 61396, 30827141, "[137, 138]", 362, "0"),
 "zh-tw": ("weekly-report-w46-ko-zh-tw", "Lucerna-VOL3-ZHTW-web.pdf", "Lucerna-VOL3-ZHTW.pdf",
           "2026-w46-ko-zh-tw.text.md", 27530, 340, 2654630, 50903, 32054373, "[]", 361, "904 (Round 2: 903; +1 = restored 細, Hangul added 0)"),
}

D3_BEFORE = "한국시리즈 시작이 하루 ___어요."
D3_AFTER = "한국시리즈 시작이 하루 ___."
D4_BEFORE = "미리 소금에 절인 배추를 ___이라고 해요."
D4_AFTER = "미리 소금에 절인 배추를 ___라고 해요."

for code, (edir, web, prn, tm, tm_bytes, tm_items, web_bytes, txt_bytes, prn_bytes,
           keydiff, koscan, freeze_note) in DATA.items():
    path = os.path.join(GOAL, "files", edir, "WEEKLY-KIT.md")
    text = open(path, encoding="utf-8").read()
    assert text.count("Fix record — Round 1") == 1, (code, "Round 1 marker")
    assert "Fix record — Round 3" not in text, (code, "Round 3 already present")
    d1 = ""
    if code == "zh-tw":
        d1 = ("- D1 survives: `规` = 0 in this edition; expanded OpenCC s2t Simplified-only scan "
              "re-run on the final SVGs returns exactly the 2 adjudicated non-defects "
              "(`峰` U+5CF0 ×8, `准` U+51C6 ×1). P6 gloss `譯注｜재다 衡量 · 규모 規模 · 섞다 混淆。` intact.\n")
    core_note = ""
    if code == "zh-cn":
        core_note = ("- Core `check_core.py` re-run on the final artifacts: exit 0; P7 phrases all verbatim; "
                     "dates all True; gloss-occurrence diagnostics 19 (was 18 after Round 1) — the +1 is the "
                     "restored `가늘` hand-list entry, a known naive-substring diagnostic of the same class as "
                     "the other 18 (dictionary form vs inflected prose form, e.g. `막히`/`막혀`, `가늘`/`가늰`); "
                     "the KIT adjudication of the `가늘다 → 가늰` pair stands.\n")
    record = f"""
## Fix record — Round 3 (2026-11-03; Round 2 verdict FAIL — three frozen-core defects)

Round 2 proofreader verdict (2026-11-03): all 11 editions FAIL on three blocking frozen-core defects; D1 confirmed; keys 150/150 confirmed; gates clean. Round 3 fixed ONLY the three defects below, at the build sources (no SVG/PDF patches), full re-render of all 11 editions. D1 was NOT disturbed. No other family touched. Nothing pushed/inserted/posted. Full report: `hidden_files/w46/ko-fix-round3/FIX-REPORT.md`.

- R-GLOSS — RESTORE the `가늘다` gloss entry in the P3 gloss line, exactly as pre-fix (reverses the Round 1 D2 deletion, whose "occurs nowhere" premise Round 2 refuted: `가늰` occurs 3× per edition — P3 body, P5 body, P5 exercise 69 option A, key 69 = A — and `가늘다 → 가늰` is a ㄹ-irregular attributive). Restored in `content34.py`, both sides of the `supp_*.py` record pair, and the core `check_core.py` hand list.
  - Before (Round 1 form): `{GLOSS_BEFORE[code]}`
  - After (restored, verified verbatim from the rendered P3 SVG gloss band): `{GLOSS_AFTER[code]}`
  - This resolves the Round 1 discrepancy flag in this KIT: the stem DOES occur (as inflected `가늰`); the entry is restored, not deleted.
- D3 — item 54 (P4), stem fix at the core source, key UNCHANGED (`밀렸어요`).
  - Before: `{D3_BEFORE}` → reconstructed `하루 밀렸어요어요` (doubled ending).
  - After: `{D3_AFTER}` → reconstructed `한국시리즈 시작이 하루 밀렸어요.` (verified in all 11 renderings).
- D4 — item 103 (P7), stem fix at the core source, key UNCHANGED (`절임배추`).
  - Before: `{D4_BEFORE}` (ungrammatical: `배추` is vowel-final, quotative must be `라고`).
  - After: `{D4_AFTER}` → reconstructed `미리 소금에 절인 배추를 절임배추라고 해요.` (verified in all 11 renderings; contrast item 101 `김장이라고`, batchim-final, unchanged).
- Same-class sweep (AST text-read of the build sources, `sweep.py`): all 77 fill-in stems scanned for stem+key doubling — exactly 1 candidate (item 54); all quotative `이라고/라고` usages scanned for final-syllable mismatch — exactly 1 mismatch (item 103) among 3 quotative stems, plus 4 correct prose usages and 1 non-applicable (`'D-7'이라고`, non-Hangul token) reported unscanned-as-defect for Round 3 adjudication. No further candidates; nothing else fixed.
- Keys UNCHANGED: p8.py compare CLEAN 150/150, keydiff {keydiff}; per-edition key-extraction JSONs byte-identical pre-fix vs post-fix (all 150 keys, noted sets identical; keys 54 `밀렸어요` and 103 `절임배추` unchanged everywhere).

Re-gates on the final artifacts (all 11 editions; full logs/JSONs under `hidden_files/w46/ko-fix-round3/gates/`):
- Freeze: core baseline 8/8 SVGs byte-identical; this edition added CJK/Hangul characters vs core: {freeze_note}. No U+FFFD.
- p8.py: CLEAN 150/150, keydiff {keydiff}. Occlusion audit: 0 flags in all 88 pages, selftest OK. Counts re-measured: 150 exercises, A2 51 / B1 72 / B2 27, per-page 10/18/18/18/18/18/12/38. Kinsoku: 0. Koscan reconstruction: CANDIDATES={koscan} TRUE_SPLITS=0 S3=0 (script preserved at `hidden_files/w46/ko-fix-round3/koscan-round3.py`).
- P3 gloss-box geometry: gloss lines inside their box (top margin 38.5, bottom margin 47.725); occlusion 0. Visual: P3 full frame checked (restored gloss inside its box, no overflow); P4 item 54 / P7 item 103 checked at full frame in the core + spot checks (de P4, ja P7).
{d1}{core_note}- Render: 0 FLOW OVERFLOW / HEAD TOO WIDE. `{web}` {web_bytes} bytes (< 7 MB), 8 pages, pdftotext {txt_bytes} bytes. `{prn}` {prn_bytes} bytes, 8 pages, pdftotext {txt_bytes} bytes. `{tm}` regenerated via `textmd.py` (headers byte-identical to pre-fix, {tm_items} items, {tm_bytes} bytes; diff vs pre-fix export is only the restored P3 gloss line).
- Change isolation: hash diff vs the pre-fix snapshot — exactly 9 files changed in this edition (svg/p3, svg/p4, svg/p7, cards p3/p4/p7, print PDF, web PDF, `.text.md`); SVG-text multiset diff — the ONLY string changes are the three fixes (P3 gloss wrap lines, P4 item-54 stem, P7 item-103 stem). No other string changed anywhere.
"""
    if not text.endswith("\n"):
        text += "\n"
    open(path, "w", encoding="utf-8").write(text + record)
    print(code, "appended", len(record), "chars")
print("all 11 KIT records appended")
