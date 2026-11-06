# -*- coding: utf-8 -*-
"""W46 EN-family Round 1 fix worker: source-only edits, assertion-checked.
Each edit: (build-dir key, relative file, old, new, expected count).
No rendered SVG/PDF is touched here; re-render follows."""
import os, sys
ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HF = os.path.join(ROOT, "hidden_files")
BUILDS = {
 "core": "weekly-report-w46-en-build",
 "de": "weekly-report-w46-en-de-build", "es": "weekly-report-w46-en-es-build",
 "fr": "weekly-report-w46-en-fr-build", "it": "weekly-report-w46-en-it-build",
 "ja": "weekly-report-w46-en-ja-build", "ko": "weekly-report-w46-en-ko-build",
 "nl": "weekly-report-w46-en-nl-build", "pt": "weekly-report-w46-en-pt-build",
 "ru": "weekly-report-w46-en-ru-build", "zh-tw": "weekly-report-w46-en-zh-tw-build",
}
EDITS = []
# B4: all 11 builds, content7.py toolbox para only (quoted-string form excludes the P7 box example on line 32)
B4_OLD = '"B1 — « Dickens wrote the story in 1843. »"'
B4_NEW = '"B1 — « Dickens wrote the story in 1843.»"'
for k in BUILDS:
    EDITS.append((k, "content7.py", B4_OLD, B4_NEW, 1, "B4"))
# B5 core + zh-tw editor's note
EDITS.append(("core", "content7.py", "请把你的来信与写作寄来", "请把来信与写作寄来", 1, "B5-core"))
EDITS.append(("zh-tw", "content7.py", "請把你的來信與寫作寄來", "請把來信與寫作寄來", 1, "B5-zh-tw"))
# B6 zh-tw P2 bridge (keep 原形 clarification; add 來 to re-break)
EDITS.append(("zh-tw", "content12.py", "用 will + 動詞原形改寫", "用 will + 動詞原形來改寫", 1, "B6"))
# B1 es/pt/ru — FITTING question forms (verdict proposals overflow the 434px box:
# 469/456/473px measured; IT precedent 'Quanto dura?' 329px). See FIX-REPORT §B1.
EDITS.append(("es", "content56.py", "HOW LONG ? · El mandato", "HOW LONG ? · ¿Cuánto dura?", 1, "B1-es"))
EDITS.append(("pt", "content56.py", "HOW LONG ? · O mandato", "HOW LONG ? · Quanto dura?", 1, "B1-pt"))
EDITS.append(("ru", "content56.py", "HOW LONG ? · Срок полномочий", "HOW LONG ? · Каков срок?", 1, "B1-ru"))
# B3 ko P8 notes (simulated: C2/D1 eliminate S3, no new S3)
EDITS.append(("ko", "content56.py", "갈라쇼는 솔퍼드에서 생방송돼요", "모금 갈라쇼는 솔퍼드에서 생방송돼요", 1, "B3-68"))
EDITS.append(("ko", "content8.py", "전교생이 2분간 묵념해요", "전교생이 2분 동안 묵념해요", 1, "B3-130"))
# M1 de/fr FINAL TEST native tails (family pattern: English kept + native line)
EDITS.append(("de", "content8.py",
  "FINAL TEST · Abschlusstest · Answers at the bottom of this page",
  "FINAL TEST · Abschlusstest · Answers at the bottom of this page · Die Antworten stehen am Ende dieser Seite", 1, "M1-de"))
EDITS.append(("fr", "content8.py",
  "FINAL TEST · Test final · Answers at the bottom of this page",
  "FINAL TEST · Test final · Answers at the bottom of this page · Les réponses sont en bas de cette page", 1, "M1-fr"))
# M2 fr: strip duplicated prefix from the 5 f.gloss() calls only (P1 instrline untouched)
EDITS.append(("fr", "content12.py", 'f.gloss("Note | ', 'f.gloss("', 1, "M2-fr"))
EDITS.append(("fr", "content34.py", 'f.gloss("Note | ', 'f.gloss("', 2, "M2-fr"))
EDITS.append(("fr", "content56.py", 'f.gloss("Note | ', 'f.gloss("', 2, "M2-fr"))
# M2 ko: strip duplicated prefix from the 5 f.gloss() calls only (P1 bridge untouched)
EDITS.append(("ko", "content12.py", 'f.gloss("해설 — ', 'f.gloss("', 1, "M2-ko"))
EDITS.append(("ko", "content34.py", 'f.gloss("해설 — ', 'f.gloss("', 2, "M2-ko"))
EDITS.append(("ko", "content56.py", 'f.gloss("해설 — ', 'f.gloss("', 2, "M2-ko"))
# M2 zh-tw: restore distinct pair 譯注｜講解｜ in the 5 f.gloss() calls (P1 expl untouched)
EDITS.append(("zh-tw", "content12.py", 'f.gloss("譯注｜', 'f.gloss("講解｜', 1, "M2-zh-tw"))
EDITS.append(("zh-tw", "content34.py", 'f.gloss("譯注｜', 'f.gloss("講解｜', 2, "M2-zh-tw"))
EDITS.append(("zh-tw", "content56.py", 'f.gloss("譯注｜', 'f.gloss("講解｜', 2, "M2-zh-tw"))
# M3 de: both occurrences (P6 gloss + P8 note source) -> das Ergebnis verkünden
EDITS.append(("de", "content56.py", "ein Rennen entscheiden", "das Ergebnis verkünden", 2, "M3-de"))
# M4 nl/pt: restore SCROOGE'S NIGHT · + short gloss (full caps titles 526/488px overflow
# the 434px box; DE 'Scrooge-Nacht' / IT 'La notte' short-gloss precedent)
EDITS.append(("nl", "content34.py", 'v3.box("DE NACHT VAN SCROOGE"', 'v3.box("SCROOGE\'S NIGHT · Scrooge-nacht"', 1, "M4-nl"))
EDITS.append(("pt", "content34.py", 'v3.box("A NOITE DE SCROOGE"', 'v3.box("SCROOGE\'S NIGHT · A noite"', 1, "M4-pt"))

fails = 0
for key, rel, old, new, exp, tag in EDITS:
    path = os.path.join(HF, BUILDS[key], rel)
    txt = open(path, encoding="utf-8").read()
    n = txt.count(old)
    if n != exp:
        print(f"FAIL {tag} {key}/{rel}: found {n}, expected {exp}: {old!r}")
        fails += 1
        continue
    open(path, "w", encoding="utf-8").write(txt.replace(old, new))
    print(f"OK   {tag} {key}/{rel}: {old!r} -> {new!r}")

# B2: ko ABSTRACT.txt single character U+B326 -> U+BB8C
apath = os.path.join(ROOT, "files/weekly-report-w46-en-ko/ABSTRACT.txt")
atxt = open(apath, encoding="utf-8").read()
assert atxt.count("댦") == 1, atxt.count("댦")
assert "뮌" not in atxt
open(apath, "w", encoding="utf-8").write(atxt.replace("댦", "뮌"))
print("OK   B2 ko ABSTRACT.txt: 댦 U+B326 -> 뮌 U+BB8C")
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
