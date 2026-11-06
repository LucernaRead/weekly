# -*- coding: utf-8 -*-
"""Verify Round 1 fixes on FINAL rendered SVGs + PDFs (read-only)."""
import re, os, subprocess, sys
from pathlib import Path
BASE = Path.home() / "workspace/goals/lucernaread-social-media-operations/files"
EDS = {"core": "weekly-report-w46-en-core", "de": "weekly-report-w46-en-de",
 "es": "weekly-report-w46-en-es", "fr": "weekly-report-w46-en-fr",
 "it": "weekly-report-w46-en-it", "ja": "weekly-report-w46-en-ja",
 "ko": "weekly-report-w46-en-ko", "nl": "weekly-report-w46-en-nl",
 "pt": "weekly-report-w46-en-pt", "ru": "weekly-report-w46-en-ru",
 "zh-tw": "weekly-report-w46-en-zh-tw"}
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*)="([^"]*)"')
def texts(svg):
    raw = Path(svg).read_text(encoding="utf-8", errors="replace")
    out = []
    for m in TEXT_RE.finditer(raw):
        a = dict(ATTR_RE.findall(m.group(1)))
        inner = re.sub(r"<[^>]+>", "", m.group(2)).replace("&amp;","&").replace("&lt;","<").replace("&gt;",">")
        out.append({"x": float(a.get("x", 0)), "y": float(a.get("y", 0)), "size": a.get("font-size"), "text": inner})
    return out
fails = []
def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond: fails.append(label)

for ed, d in EDS.items():
    p7 = texts(BASE / d / "svg/p7-langue.svg")
    # B4: no lone » element on P7; B1 line must contain 1843.»
    lone = [t for t in p7 if t["text"].strip() == "»"]
    check(not lone, f"B4 {ed}: no lone » on P7 (found {len(lone)})")
    b1 = [t["text"] for t in p7 if "1843" in t["text"]]
    check(any("1843.»" in t for t in b1), f"B4 {ed}: B1 toolbox line carries 1843.» : {b1}")
    # B5: no lone 。 on P7 anywhere
    lonep = [t for t in p7 if t["text"].strip() == "。"]
    check(not lonep, f"B5 {ed}: no lone 。 on P7 (found {len(lonep)})")
    p2 = texts(BASE / d / "svg/p2-life.svg")
    lone2 = [t for t in p2 if t["text"].strip() == "。"]
    check(not lone2, f"B6 {ed}: no lone 。 on P2 (found {len(lone2)})")

# B1 glosses (P6 box titles)
def alltexts(ed):
    out = []
    for svg in sorted((BASE / EDS[ed] / "svg").glob("*.svg")):
        out += texts(svg)
    return out
for ed, expect in {"es": "HOW LONG ? · ¿Cuánto dura?", "pt": "HOW LONG ? · Quanto dura?", "ru": "HOW LONG ? · Каков срок?"}.items():
    ts = [t["text"] for t in alltexts(ed) if "HOW LONG" in t["text"]]
    check(ts == [expect], f"B1 {ed}: P6 title == {expect!r} (got {ts})")
for ed, expect in {"de": "Wie lange im Amt?", "fr": "Quelle durée ?", "it": "Quanto dura?",
                   "ja": "任期はどれくらい？", "ko": "임기는 얼마나?", "nl": "Hoe lang?", "zh-tw": "任期多長？", "core": "任期多长？"}.items():
    ts = [t["text"] for t in alltexts(ed) if "HOW LONG" in t["text"]]
    check(len(ts) == 1 and expect in ts[0], f"B1-untouched {ed}: {ts}")
# M1
for ed, tail in {"de": "Die Antworten stehen am Ende dieser Seite", "fr": "Les réponses sont en bas de cette page"}.items():
    ts = [t["text"] for t in alltexts(ed) if "FINAL TEST" in t["text"]]
    check(len(ts) == 1 and tail in ts[0] and "Answers at the bottom of this page" in ts[0], f"M1 {ed}: {ts}")
# M2: no doubled prefixes anywhere; zh-tw distinct pair present
for ed in EDS:
    ts = [t["text"] for t in alltexts(ed)]
    joined = "\n".join(ts)
    check("Note | Note |" not in joined, f"M2 {ed}: no 'Note | Note |'")
    check("해설 — 해설 —" not in joined, f"M2 {ed}: no doubled 해설")
    check("譯注｜譯注｜" not in joined, f"M2 {ed}: no doubled 譯注")
    check("译注｜译注｜" not in joined, f"M2 {ed}: no doubled 译注")
    check("Anmerkung | Anmerkung" not in joined, f"M2 {ed}: no doubled Anmerkung")
pair = [t for t in alltexts("zh-tw") if t["text"].startswith("譯注｜講解｜")]
check(len(pair) == 5, f"M2 zh-tw: 5 gloss boxes with 譯注｜講解｜ (found {len(pair)})")
for ed, pre in {"fr": "Note | ", "ko": "해설 — "}.items():
    gs = [t for t in alltexts(ed) if t["text"].startswith(pre) and ("a silence" in t["text"] or "a miser" in t["text"] or "a fixture" in t["text"] or "an appeal" in t["text"] or "to call a race" in t["text"])]
    check(len(gs) == 5, f"M2 {ed}: 5 single-prefix gloss boxes (found {len(gs)})")
check([t["text"] for t in alltexts("de") if t["text"].startswith("Anmerkung | Erklärung |")].__len__() == 5, "M2 de: 5 distinct-pair boxes untouched")
# M3
dets = [t["text"] for t in alltexts("de") if "call a race" in t["text"] or "Rennen" in t["text"] or "Ergebnis verkünden" in t["text"]]
check(not any("Rennen entscheiden" in t for t in dets), f"M3 de: no 'ein Rennen entscheiden' left: {dets}")
check(sum(1 for t in dets if "das Ergebnis verkünden" in t) == 2, f"M3 de: 2x 'das Ergebnis verkünden': {dets}")
# M4
for ed, expect in {"nl": "SCROOGE'S NIGHT · Scrooge-nacht", "pt": "SCROOGE'S NIGHT · A noite"}.items():
    ts = [t["text"] for t in alltexts(ed) if "SCROOGE" in t["text"] and "NIGHT" in t["text"]]
    check(ts == [expect], f"M4 {ed}: P3 title == {expect!r} (got {ts})")
for ed in ["es", "fr"]:
    ts = [t["text"] for t in alltexts(ed) if t["text"] in ("LA NOCHE DE SCROOGE", "LA NUIT DE SCROOGE")]
    print(f"NOTE M4-scope {ed}: title still {ts} (untouched per verdict scope)")
# B2 abstract
ab = (BASE / EDS["ko"] / "ABSTRACT.txt").read_text(encoding="utf-8")
check("뮌헨" in ab and "댦" not in ab, "B2 ko ABSTRACT: 뮌헨 present, 댦 absent")
check(ab.count("\n") == 1 and '"' not in ab, "B2 ko ABSTRACT: single line, no ASCII dquote")
# B3 rendered P8: words unsplit
p8ko = texts(BASE / EDS["ko"] / "svg/p8-exercices.svg")
lines = [t["text"] for t in p8ko]
check(any("솔퍼드" in t for t in lines), f"B3 ko: 솔퍼드 unsplit on one P8 line: {[t for t in lines if '솔퍼드' in t or t.rstrip().endswith('솔')]}")
check(any("묵념해요" in t for t in lines), f"B3 ko: 묵념해요 unsplit on one P8 line: {[t for t in lines if '묵념' in t]}")
check(not any(t.rstrip().endswith("솔") for t in lines), "B3 ko: no P8 line ends with 솔")
check(not any(t.rstrip().endswith("묵") for t in lines), "B3 ko: no P8 line ends with 묵")
# B6 bridge rendered
br = [t["text"] for t in alltexts("zh-tw") if "動詞原形" in t["text"]]
check(any("動詞原形來改寫" in t for t in br), f"B6 zh-tw bridge: {br}")
# PDFs
for ed, d in EDS.items():
    web = BASE / d / "The-Lucerna-VOL3-web.pdf"
    prn = BASE / d / "The-Lucerna-VOL3.pdf"
    txt = subprocess.run(["pdftotext", str(web), "-"], capture_output=True).stdout
    txtp = subprocess.run(["pdftotext", str(prn), "-"], capture_output=True).stdout
    info = subprocess.run(["pdfinfo", str(web)], capture_output=True, text=True).stdout
    pages = [ln for ln in info.splitlines() if ln.startswith("Pages:")]
    check(web.stat().st_size <= 7_000_000, f"PDF {ed}: web {web.stat().st_size}B <= 7MB")
    check(len(txt) > 0, f"PDF {ed}: web pdftotext {len(txt)}B > 0")
    check(len(txt) == len(txtp), f"PDF {ed}: web text {len(txt)}B == print text {len(txtp)}B")
    check(pages and pages[0].split() == ["Pages:", "8"], f"PDF {ed}: 8 pages ({pages})")
    print(f"  inventory {ed}: web={web.stat().st_size} print={prn.stat().st_size} webtext={len(txt)}")
print("FAILURES:", len(fails))
for f in fails: print(" -", f)
sys.exit(1 if fails else 0)
