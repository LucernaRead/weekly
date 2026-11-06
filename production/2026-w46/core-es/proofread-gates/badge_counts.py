import re, glob, os, html, collections
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def parse_svg(path):
    s=open(path,encoding="utf-8").read()
    els=[]
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        attrs=m.group(1); inner=html.unescape(re.sub(r"<[^>]+>","",m.group(2)))
        def a(n):
            mm=re.search(n+r'="([^"]*)"', attrs); return mm.group(1) if mm else ""
        els.append({"x":float(a("x") or 0),"y":float(a("y") or 0),"size":a("font-size"),"weight":a("font-weight"),"fill":a("fill"),"anchor":a("text-anchor"),"fam":a("font-family"),"text":inner})
    return els
print("===== P1 BADGE / MASTHEAD (measured from SVG) =====")
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    els=parse_svg(f"{BASE}/files/weekly-report-w46-es-{code}/svg/p1-portada.svg")
    print(f"\n-- es-{code} --")
    for e in els:
        if 240<=e["y"]<=600:
            print(f"  y={e['y']} x={e['x']} size={e['size']} w={e['weight']} fill={e['fill']} anchor={e['anchor']} fam={e['fam'][:22]} :: {e['text'][:150]}")
    # footers on P1 (y>2580)
    for e in els:
        if e["y"]>2580:
            print(f"  FOOT y={e['y']} x={e['x']} fill={e['fill']} :: {e['text'][:150]}")
print("\n===== FOOTERS all pages (page 2 sample + check all 8 identical pattern) =====")
for code in ["de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    foots=set()
    for pg in range(1,9):
        els=parse_svg(f"{BASE}/files/weekly-report-w46-es-{code}/svg/p{pg}-{'portada' if pg==1 else ''}.svg") if False else None
    import glob as g
    for fn in sorted(g.glob(f"{BASE}/files/weekly-report-w46-es-{code}/svg/*.svg")):
        for e in parse_svg(fn):
            if e["y"]>2580 and "La Lucerna" in e["text"]: foots.add(e["text"])
    print(code, "distinct footers:", foots)
