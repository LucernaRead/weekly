import re, glob, os
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def gloss_strings(builddir):
    out=[]
    for fn in sorted(glob.glob(builddir+"/content*.py")):
        s=open(fn,encoding="utf-8").read()
        for m in re.finditer(r'gloss\(\s*"((?:[^"\\]|\\.)*)"', s):
            out.append((os.path.basename(fn), m.group(1)))
        for m in re.finditer(r"gloss\(\s*'((?:[^'\\]|\\.)*)'", s):
            out.append((os.path.basename(fn), m.group(1)))
    return out
core=gloss_strings(BASE+"/hidden_files/weekly-report-w46-es-build")
print("CORE gloss calls:", len(core))
for fn,s in core:
    items=[p.strip() for p in s.split("·")]
    print(f"  {fn}: {len(items)} items :: {s[:110]}")
    print(f"     items: {items}")
for code in ["de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    gs=gloss_strings(BASE+f"/hidden_files/weekly-report-w46-es-{code}-build")
    print(f"\n{code}: gloss calls {len(gs)}")
    for fn,s in gs:
        items=[p.strip() for p in s.split("·")]
        print(f"  {fn}: {len(items)} :: {s[:130]}")
