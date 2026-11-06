# -*- coding: utf-8 -*-
"""Independent proof checks: gloss counts, P6 chart rects, image payloads, P7 measures."""
import re, glob, hashlib, base64, os, sys

CORE_BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zhcn-build")
PT_BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-cn-pt-build")
CORE_SVG = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg")
ED_SVG = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-pt/svg")
ASSETS = os.path.join(CORE_BUILD, "assets")

def gloss_calls(build):
    out = []
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(build, f), encoding="utf-8").read()
        for m in re.finditer(r'\.gloss\("((?:[^"\\]|\\.)*)"\)', src):
            out.append(m.group(1))
    return out

core = gloss_calls(CORE_BUILD)
ed = gloss_calls(PT_BUILD)
print("gloss calls core:", len(core), "ed:", len(ed))
cc = [len(s.split("·")) for s in core]
ec = [len(s.split("·")) for s in ed]
print("core per-call:", cc, "total:", sum(cc))
print("ed   per-call:", ec, "total:", sum(ec))
assert cc == ec, "GLOSS COUNT MISMATCH"
# headwords (Chinese token before ' — ') must be identical item by item
for i, (a, b) in enumerate(zip(core, ed)):
    ha = [x.split(" — ")[0].strip() for x in a.split("·")]
    hb = [x.split(" — ")[0].strip() for x in b.split("·")]
    assert ha == hb, (i, ha, hb)
print("gloss headwords identical item-by-item: OK")
# rendered: each PT gloss item's headword + prefix present in edition SVGs
edtext = ""
for f in sorted(glob.glob(os.path.join(ED_SVG, "*.svg"))):
    edtext += open(f, encoding="utf-8").read()
print("gloss prefix 'Nota — ' occurrences in edition SVGs:", edtext.count("Nota — "))
print("gloss prefix 'Notes' occurrences in edition SVGs:", edtext.count("Notes"))

# P6 chart rects: bars drawn from x=325; compare core vs edition rect sets
def rects(path):
    src = open(path, encoding="utf-8").read()
    return re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^/]*/>', src)
rc, re_ = rects(os.path.join(CORE_SVG, "p6-shendu.svg")), rects(os.path.join(ED_SVG, "p6-shendu.svg"))
print("P6 rect count core:", len(rc), "ed:", len(re_), "identical sets:", rc == re_)
for r in rc:
    if r not in re_:
        print("  core-only rect:", r)
for r in re_:
    if r not in rc:
        print("  ed-only rect:", r)
# chart rows: look for bar widths 810/537/480
for w in ("810", "537", "480"):
    print(f"  width {w} in core P6:", sum(1 for r in rc if r[2] == w), " in ed P6:", sum(1 for r in re_ if r[2] == w))

# Images: payload md5 in edition SVGs vs core assets and vs core SVGs
am = {}
for f in glob.glob(ASSETS + "/*.jpg"):
    am[hashlib.md5(open(f, "rb").read()).hexdigest()] = os.path.basename(f)
print("asset md5 map:", am)
def payloads(svgdir):
    out = {}
    for f in sorted(glob.glob(os.path.join(svgdir, "*.svg"))):
        s = open(f, encoding="utf-8").read()
        hs = []
        for m in re.finditer(r'data:image/jpeg;base64,([A-Za-z0-9+/=]+)', s):
            hs.append(hashlib.md5(base64.b64decode(m.group(1))).hexdigest())
        out[os.path.basename(f)] = hs
    return out
pc, pe = payloads(CORE_SVG), payloads(ED_SVG)
for k in sorted(pc):
    print(k, "core:", [(h[:8], am.get(h, "UNKNOWN")) for h in pc[k]], "| ed:", [(h[:8], am.get(h, "UNKNOWN")) for h in pe[k]], "| identical:", pc[k] == pe[k])
print("ALL IMAGE PAYLOADS IDENTICAL TO CORE:", pc == pe)
# credit lines in edition SVGs
for f in sorted(glob.glob(os.path.join(ED_SVG, "*.svg"))):
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r'<text[^>]*>([^<]*(?:Foto|Domínio|CC0|Wikimedia)[^<]*)</text>', s):
        print(os.path.basename(f), "credit:", m.group(1))
print("leftover 'Public domain' in ed SVGs:", edtext.count("Public domain"))
