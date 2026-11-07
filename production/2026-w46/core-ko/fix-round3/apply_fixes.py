#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round 3 fix application — W46 KO family (11 editions).

R-GLOSS: restore the 가늘다 gloss entry in content34.py (all 11), in both
  sides of the supp_*.py record pair (10 fan-outs; core has no supp file),
  and restore "가늘" in core check_core.py's P3 hand list.
D3: item 54 stem ___어요. -> ___. in content34.py (all 11). Key UNCHANGED.
D4: item 103 stem ___이라고 -> ___라고 in content7.py (all 11). Key UNCHANGED.

Exact-count assertions: any count != expected aborts with NO writes for
that file (edits are applied file-by-file only after all counts in the
file check out). Run once; re-running must report 0 remaining targets.
"""
import os, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HID = os.path.join(GOAL, "hidden_files")

# Restored gloss ARGUMENT strings (the f.gloss() argument; the gloss prefix
# is added by the builder). Verbatim from Round 2 verdict §2.4 / Round 1
# fix report Before column.
GLOSS_CORE = "겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。"
GLOSS_NATIVE = {
    "zh-cn": "겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。",
    "de": "겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen",
    "en": "겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share",
    "es": "겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir",
    "fr": "겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager",
    "it": "겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere",
    "ja": "겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う",
    "nl": "겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen",
    "pt": "겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar",
    "ru": "겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться",
    "zh-tw": "겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。",
}
# Current (post-Round-1) gloss argument = restored minus the 가늘다 entry.
def shortened(native):
    seg_start = native.find("가늘다")
    assert seg_start < 0, "shortened() called on restored string"
    return native

def current_gloss(native):
    # Remove "가늘다 <equiv> · " segment from the restored string.
    i = native.find("가늘다")
    j = native.find("·", i)
    return native[:i] + native[j + 2:]

BUILDS = {
    "zh-cn": "weekly-report-w46-ko-build",
    "de": "weekly-report-w46-ko-de-build",
    "en": "weekly-report-w46-ko-en-build",
    "es": "weekly-report-w46-ko-es-build",
    "fr": "weekly-report-w46-ko-fr-build",
    "it": "weekly-report-w46-ko-it-build",
    "ja": "weekly-report-w46-ko-ja-build",
    "nl": "weekly-report-w46-ko-nl-build",
    "pt": "weekly-report-w46-ko-pt-build",
    "ru": "weekly-report-w46-ko-ru-build",
    "zh-tw": "weekly-report-w46-ko-zh-tw-build",
}
SUPP = {"de": "supp_de.py", "en": "supp_en.py", "es": "supp_es.py",
        "fr": "supp_fr.py", "it": "supp_it.py", "ja": "supp_ja.py",
        "nl": "supp_nl.py", "pt": "supp_pt.py", "ru": "supp_ru.py",
        "zh-tw": "supp_zh_tw.py"}

STEM54_OLD = "한국시리즈 시작이 하루 ___어요."
STEM54_NEW = "한국시리즈 시작이 하루 ___."
STEM103_OLD = "미리 소금에 절인 배추를 ___이라고 해요."
STEM103_NEW = "미리 소금에 절인 배추를 ___라고 해요."

def replace_once(path, old, new, label):
    src = open(path, encoding="utf-8").read()
    n = src.count(old)
    assert n == 1, f"{path} {label}: expected 1 occurrence of {old!r}, found {n}"
    assert new not in src or old == new, f"{path} {label}: new string already present"
    open(path, "w", encoding="utf-8").write(src.replace(old, new, 1))
    print(f"OK {label}: {os.path.basename(path)}")

def main():
    for code, bdir in BUILDS.items():
        bpath = os.path.join(HID, bdir)
        native = GLOSS_NATIVE[code]
        cur = current_gloss(native)
        assert "가늘다" not in cur and "가늘" not in cur, (code, cur)
        # R-GLOSS in content34.py
        replace_once(os.path.join(bpath, "content34.py"), cur, native,
                     f"{code} R-GLOSS content34")
        # D3 in content34.py
        replace_once(os.path.join(bpath, "content34.py"), STEM54_OLD, STEM54_NEW,
                     f"{code} D3 item54")
        # D4 in content7.py
        replace_once(os.path.join(bpath, "content7.py"), STEM103_OLD, STEM103_NEW,
                     f"{code} D4 item103")
        # R-GLOSS in supp record pair (both sides)
        if code in SUPP:
            spath = os.path.join(bpath, SUPP[code])
            replace_once(spath, current_gloss(GLOSS_CORE), GLOSS_CORE,
                         f"{code} R-GLOSS supp core-side")
            replace_once(spath, cur, native,
                         f"{code} R-GLOSS supp native-side")
    # check_core.py P3 hand list: restore "가늘" after "겹치"
    cpath = os.path.join(HID, BUILDS["zh-cn"], "check_core.py")
    replace_once(cpath, '"겹치", "감사"', '"겹치", "가늘", "감사"',
                 "core check_core P3 hand list")
    print("ALL FIXES APPLIED")

if __name__ == "__main__":
    main()
