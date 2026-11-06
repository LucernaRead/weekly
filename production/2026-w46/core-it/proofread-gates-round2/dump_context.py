# -*- coding: utf-8 -*-
"""Dump P7 with y-coords + P8 56/57 wrapped continuations + P2 D3 sentence + P4 stems, read-only."""
import html, os, re
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(BASE, "files")
DIRMAP = {"core":"weekly-report-w46-it-core","de":"weekly-report-w46-it-de","en":"weekly-report-w46-it-en",
 "es":"weekly-report-w46-it-es","fr":"weekly-report-w46-it-fr","ja":"weekly-report-w46-it-ja",
 "ko":"weekly-report-w46-it-ko","nl":"weekly-report-w46-it-nl","pt":"weekly-report-w46-it-pt",
 "ru":"weekly-report-w46-it-ru","zh-tw":"weekly-report-w46-it-zh-tw"}

def elems(ed, fname):
    s = open(os.path.join(FILES, DIRMAP[ed], "svg", fname), encoding="utf-8").read()
    out=[]
    for m in re.finditer(r'<text[^>]*\bx="([\d.]+)"[^>]*\by="([\d.]+)"[^>]*>(.*?)</text>', s, re.S):
        t = html.unescape(re.sub(r"<[^>]+>","", m.group(3))).strip()
        if t: out.append((float(m.group(2)), float(m.group(1)), t))
    out.sort()
    return out

print("===== P7 full text with y (ru, fr, de, nl, pt, en) =====")
for code in ["ru","fr","de","nl","pt","en"]:
    print(f"--- {code} P7 ---")
    for y,x,t in elems(code,"p7-lingua.svg"):
        print(f"  y={y:7.1f} x={x:6.1f} {t!r}")
print("\n===== P8 items 56/57 full wrapped blocks (all) =====")
for code in DIRMAP:
    print(f"--- {code} P8 ---")
    el = elems(code,"p8-valutazione.svg")
    # find index of elements starting with 56. / 57. (key line) and print next 3 elements in same column (same x band, increasing y)
    for idx,(y,x,t) in enumerate(el):
        if re.match(r"^(56|57)\.", t):
            print(f"  y={y:.1f} x={x:.1f} {t!r}")
            for (y2,x2,t2) in el[idx+1:idx+4]:
                print(f"    cont y={y2:.1f} x={x2:.1f} {t2!r}")
print("\n===== P2 D3 sentence block (core) =====")
el = elems("core","p2-vita.svg")
for idx,(y,x,t) in enumerate(el):
    if "si è chiuso" in t or "si sono aperte" in t or "Forum Cultura" in t:
        print(f"  y={y:.1f} x={x:.1f} {t!r}")
        for (y2,x2,t2) in el[max(0,idx-2):idx+3]:
            print(f"    ctx y={y2:.1f} x={x2:.1f} {t2!r}")
        print("  ---")
print("\n===== P4 stems 56/57 full blocks (core + en) =====")
for code in ["core","en"]:
    print(f"--- {code} P4 ---")
    el = elems(code,"p4-sport.svg")
    for idx,(y,x,t) in enumerate(el):
        if "NON cominciano" in t or "cominciano ___" in t:
            print(f"  y={y:.1f} x={x:.1f} {t!r}")
            for (y2,x2,t2) in el[idx+1:idx+3]:
                print(f"    cont y={y2:.1f} x={x2:.1f} {t2!r}")
print("\n===== RU P7 geometry: rects + lines y in 1500-1800 =====")
s = open(os.path.join(FILES, DIRMAP["ru"], "svg", "p7-lingua.svg"), encoding="utf-8").read()
for m in re.finditer(r'<(rect|line)[^>]*>', s):
    tag=m.group(0)
    ys = re.findall(r'\by\d?="([\d.]+)"', tag)
    if tag.startswith("<rect"):
        y=re.search(r'\by="([\d.]+)"', tag); h=re.search(r'\bheight="([\d.]+)"', tag)
        if y and h and 1400 <= float(y.group(1)) <= 1900:
            print(f"  RECT {tag[:220]}")
    else:
        y1=re.search(r'\by1="([\d.]+)"', tag); y2=re.search(r'\by2="([\d.]+)"', tag)
        if y1 and 1400 <= float(y1.group(1)) <= 1900:
            print(f"  LINE {tag[:220]}")
print("\n===== RU P7 text y in 1500-1800 =====")
for y,x,t in elems("ru","p7-lingua.svg"):
    if 1500 <= y <= 1900: print(f"  y={y:.1f} x={x:.1f} {t!r}")
print("\n===== NL P8 bottom geometry: max text y + footer =====")
for code in ["nl","core"]:
    el = elems(code,"p8-valutazione.svg")
    print(f"--- {code} last 8 P8 texts ---")
    for y,x,t in el[-8:]: print(f"  y={y:.1f} x={x:.1f} {t!r}")
    print(f"--- {code} max non-footer text y (y<2580): {max(y for y,x,t in el if y<2580):.1f}")
print("\n===== P3 title + P1 Cremona lines (core) =====")
for fname in ["p1-prima.svg","p3-cultura.svg"]:
    print(f"--- {fname} ---")
    for y,x,t in elems("core",fname):
        if "Cremona" in t or "Due feste" in t or "Torrone" in t and y<700: print(f"  y={y:.1f} {t!r}")
print("\n===== Edition-specific P8 dumps =====")
def p8lines(code, pat):
    el = elems(code,"p8-valutazione.svg")
    for y,x,t in el:
        if re.search(pat,t): print(f"  {code} y={y:.1f} {t!r}")
print("-- en 132/44/134 --"); p8lines("en", r"132\.|44\.|134\.")
print("-- es 132/117 --"); p8lines("es", r"132\.|117\.")
print("-- fr 132 --"); p8lines("fr", r"132\.")
print("-- nl 20 --"); p8lines("nl", r"^20\.")
print("-- pt 132 --"); p8lines("pt", r"132\.")
print("-- ru 38 --"); p8lines("ru", r"^38\.")
print("-- pt P7 escreve --")
for y,x,t in elems("pt","p7-lingua.svg"):
    if "escrev" in t or "redação" in t: print(f"  pt y={y:.1f} {t!r}")
print("\n===== Badge strings P1 (all) =====")
for code in DIRMAP:
    el = elems(code,"p1-prima.svg")
    for y,x,t in el:
        if any(k in t for k in ["Explanations","EXPLANATIONS","Erklärungen","EXPLICACIONES","Explications","解説","해설","UITLEG","EXPLICAÇÕES","ОБЪЯСНЕНИЯ","講解","Erklär"]):
            print(f"  {code} y={y:.1f} {t!r}")
