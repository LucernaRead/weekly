import re, html, pathlib
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
CLOSERS=set("。，、；：？！）〕］｝》」』】％‰)]}.,!?%:;\"'„“”") | {"…"}
# Note: „ “ are German opening quotes - exclude opening „ ; closing “ is in set? German closing quote is “ (U+201C) - a line starting with it would be a wrap fragment of a quote. Keep “ in set, drop „.
CLOSERS.discard("„")
def scan(d):
    out=[]
    for f in sorted(d.glob("*.svg")):
        s=f.read_text(encoding="utf-8")
        for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
            a=m.group(1); txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
            t=txt.strip()
            if not t: continue
            if t[0] in CLOSERS:
                xm=re.search(r'x="([\d.]+)"',a); ym=re.search(r'y="([\d.]+)"',a)
                out.append((f.name,float(xm.group(1)),float(ym.group(1)),t[:90]))
    return out
for name,d in [("CORE",G/"files/weekly-report-w45-de-core/svg"),("ED",G/"files/weekly-report-w45-de-zh-tw/svg")]:
    hits=scan(d)
    print(f"===== {name} total {len(hits)} =====")
    for h in hits: print(" ",h)
