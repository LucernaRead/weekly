import re
from pathlib import Path
BASE = Path.home() / "workspace/goals/lucernaread-social-media-operations/files"
TEXT_RE = re.compile(r'<text\b([^>]*)>(.*?)</text>', re.S)
ATTR_RE = re.compile(r'(\w[\w-]*)="([^"]*)"')
def texts(ed, pg):
    raw = (BASE / f"weekly-report-w46-en-{ed}/svg/{pg}").read_text(encoding="utf-8")
    out = []
    for m in TEXT_RE.finditer(raw):
        a = dict(ATTR_RE.findall(m.group(1)))
        out.append((float(a.get("x",0)), float(a.get("y",0)), a.get("font-size"), re.sub(r"<[^>]+>","",m.group(2))))
    return out
for ed in ["core","de","es","fr","it","ja","ko","nl","pt","ru","zh-tw"]:
    print(f"== P7 {ed} toolbox (x=1451) ==")
    for x,y,s,t in texts(ed,"p7-langue.svg"):
        if x == 1451 and 380 <= y <= 560: print(f"  y={y} {s}pt {t!r}")
print("== P7 editor note (core/zh-tw) ==")
for ed in ["core","zh-tw"]:
    for x,y,s,t in texts(ed,"p7-langue.svg"):
        if 2000 <= y <= 2200 and "VOL.2" in t or (2000 <= y <= 2200 and ("编辑" in t or "編輯" in t)): print(f"  {ed} y={y} {t[:60]!r}")
print("== P2 zh-tw bridge ==")
for x,y,s,t in texts("zh-tw","p2-life.svg"):
    if "動詞原形" in t: print(f"  y={y} {t!r}")
print("== P6 box titles es/pt/ru ==")
for ed in ["es","pt","ru"]:
    for x,y,s,t in texts(ed,"p6-politique.svg"):
        if "HOW LONG" in t: print(f"  {ed} x={x} y={y} {t!r}")
print("== P3/P4 ko gloss lines ==")
for x,y,s,t in texts("ko","p3-culture.svg"):
    if "아직 오지" in t or "은 것" in t: print(f"  P3 y={y} {t!r}")
for x,y,s,t in texts("ko","p4-sport.svg"):
    if "스타선수" in t: print(f"  P4 y={y} {t!r}")
print("== P8 de/fr band ==")
for ed in ["de","fr"]:
    for x,y,s,t in texts(ed,"p8-exercices.svg"):
        if "FINAL TEST" in t: print(f"  {ed} y={y} {t!r}")
print("== P3 nl/pt titles ==")
for ed in ["nl","pt"]:
    for x,y,s,t in texts(ed,"p3-culture.svg"):
        if "SCROOGE" in t: print(f"  {ed} x={x} y={y} {t!r}")
print("== P2 gloss boxes fr/ko/zh-tw (first gloss line) ==")
for ed in ["fr","ko","zh-tw"]:
    for x,y,s,t in texts(ed,"p2-life.svg"):
        if "a silence" in t: print(f"  {ed} x={x} y={y} {t[:80]!r}")
print("== P6 de gloss ==")
for x,y,s,t in texts("de","p6-politique.svg"):
    if "call a race" in t: print(f"  y={y} {t[:90]!r}")
print("== P8 ko B3 lines ==")
for x,y,s,t in texts("ko","p8-exercices.svg"):
    if "솔퍼드" in t or "묵념해요" in t: print(f"  y={y} {t[:90]!r}")
