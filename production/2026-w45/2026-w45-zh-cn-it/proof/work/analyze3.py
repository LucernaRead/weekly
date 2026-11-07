import re, hashlib, pathlib, xml.etree.ElementTree as ET
from PIL import ImageFont
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
DEL = BASE/"files/weekly-report-w45-zh-cn-it"
CORE = BASE/"files/weekly-report-w45-zhcn-core"
W43 = BASE/"files/weekly-report-zh-cn-it"

# --- Gloss item-by-item (split on ·) core build vs it-build code ---
def gloss_items(d):
    out=[]
    for fn in ["content12.py","content34.py","content56.py"]:
        txt=(d/fn).read_text()
        for m in re.finditer(r'\.gloss\("(.*?)"\)', txt, re.S):
            s=m.group(1)
            out.append((fn, [it.strip() for it in s.split("·")]))
    return out
core_g = gloss_items(BASE/"hidden_files/weekly-report-w45-zhcn-build")
it_g = gloss_items(BASE/"hidden_files/weekly-report-w45-zh-cn-it-build")
print("gloss calls core/it:", len(core_g), len(it_g))
print("gloss item totals:", sum(len(x[1]) for x in core_g), sum(len(x[1]) for x in it_g))
for (f1,items1),(f2,items2) in zip(core_g, it_g):
    heads1=[it.split(" — ")[0] for it in items1]
    heads2=[it.split(" — ")[0] for it in items2]
    print(f1, "items", len(items1), "headwords equal:", heads1==heads2, heads1 if heads1!=heads2 else "")
# rendered Nota counts per page
for i,fn in enumerate(sorted((DEL/"svg").glob("*.svg")),1):
    tree=ET.parse(fn); n=sum(1 for el in tree.iter() if el.tag.endswith("text") and "".join(el.itertext()).startswith("Nota — "))
    print(f"rendered Nota P{i}: {n}")

# --- Images: embedded payload MD5 per page, in order ---
def payloads(d):
    out={}
    for fn in sorted((d/"svg").glob("*.svg")):
        raw=fn.read_text()
        imgs=re.findall(r'<image[^>]*href="data:image/jpeg;base64,([A-Za-z0-9+/=]+)"', raw)
        import base64
        out[fn.name]=[hashlib.md5(base64.b64decode(x)).hexdigest() for x in imgs]
    return out
cp, dp = payloads(CORE), payloads(DEL)
for k in cp:
    print("images", k, "core", len(cp[k]), "del", len(dp[k]), "identical:", cp[k]==dp[k])
# asset files MD5 core build vs it build
for a in ["locker.jpg","valley.jpg","frost.jpg","dumplings.jpg","lanparty.jpg","popcorn.jpg"]:
    h1=hashlib.md5((BASE/f"hidden_files/weekly-report-w45-zhcn-build/assets/{a}").read_bytes()).hexdigest()
    h2=hashlib.md5((BASE/f"hidden_files/weekly-report-w45-zh-cn-it-build/assets/{a}").read_bytes()).hexdigest()
    print("asset", a, "identical:", h1==h2)
print("core CREDITS.md:")
print((BASE/"hidden_files/weekly-report-w45-zhcn-build/assets/CREDITS.md").read_text())
# rendered credit lines
def credits(d, label):
    out={}
    for fn in sorted((d/"svg").glob("*.svg")):
        for el in ET.parse(fn).iter():
            if el.tag.endswith("text"):
                t="".join(el.itertext())
                if t.startswith("Foto:") or t.startswith("Photo:"):
                    out.setdefault(fn.name, []).append(t)
    print(label, out)
credits(CORE, "CORE credits")
credits(DEL, "DEL credits")

# --- W43 paren style + this edition paren counts ---
def paren_count(d):
    tree=ET.parse(d/"svg/p8-ceyan.svg"); n=0; tot=0
    for el in tree.iter():
        if el.tag.endswith("text"):
            t="".join(el.itertext())
            if re.match(r"^\d+\.", t):
                tot+=1
                if re.search(r"\(\S", t): n+=1
    return tot, n
print("W43 P8 keyed nodes / paren-form:", paren_count(W43))
print("DEL P8 keyed nodes / paren-form:", paren_count(DEL))
print("DEL full-width paren notes in P8 (should be core's 11 inside frozen stems):")
tree=ET.parse(DEL/"svg/p8-ceyan.svg")
fw=[t for el in tree.iter() if el.tag.endswith("text") for t in ["".join(el.itertext())] if "（" in t]
print(" count:", len(fw))
for t in fw: print("  ", repr(t[:120]))
# W43 shipped P8 full-width count for comparison
tree=ET.parse(W43/"svg/p8-ceyan.svg")
fw43=[ "".join(el.itertext()) for el in tree.iter() if el.tag.endswith("text") and "（" in "".join(el.itertext())]
print("W43 P8 full-width-paren nodes:", len(fw43))

# --- Band titles + P6 head + P7 head ---
def alltext(d):
    return "\n".join("".join(el.itertext()) for fn in sorted((d/"svg").glob("*.svg")) for el in ET.parse(fn).iter() if el.tag.endswith("text"))
dt=alltext(DEL)
for band in ["生活 · Vita","文化 · Cultura","体育 · Sport","青年 · Giovani","深读 · Lettura approfondita","词语 · Focus sulla lingua","测验与答案 · Test e soluzioni"]:
    print("band", band, band in dt)
for eng in ["Life","Culture","Youth","Deep read","Language focus"]:
    # careful: 'Life' substring checks on full text with word boundaries
    print("ENG band absent?", eng, bool(re.search(rf"\b{eng}\b", dt)))
print("P6 head Calcoli present:", "Calcoli" in dt, "| 'Calcoli con i cesti' absent:", "Calcoli con i cesti" not in dt)
# P6 chart labels ink check
FD="/usr/share/fonts/opentype/noto"
def font(fam,size,bold):
    base="NotoSansCJK" if "Sans" in fam else "NotoSerifCJK"
    return ImageFont.truetype(f"{FD}/{base}-{'Bold' if bold else 'Regular'}.ttc", int(round(size*4)), index=2)
tree=ET.parse(DEL/"svg/p6-shendu.svg")
texts=[]
for el in tree.iter():
    if el.tag.endswith("text"):
        texts.append((float(el.get("x",0)), float(el.get("y",0)), "".join(el.itertext()), el.get("font-family",""), float(el.get("font-size",0)), el.get("font-weight")=="700", el.get("text-anchor")))
bars=[(325,1282,810),(325,1340,537),(325,1398,480)]
for x,y,t,fam,size,bold,anchor in texts:
    if "元" in t and 1200<y<1450:
        f=font(fam,size,bold); bb=f.getbbox(t); adv=f.getlength(t)/4
        x0 = x-adv/2 if anchor=="middle" else (x-adv if anchor=="end" else x)
        print(f"P6 label {t!r} ink x[{x0+bb[0]/4:.1f},{x0+bb[2]/4:.1f}] baseline {y}")
print("bar ends x:", [x+w for x,_,w in bars])
for x,y,t,fam,size,bold,anchor in texts:
    if 1240<y<1290:
        print("P6 title-ish:", y, repr(t))
# P7 teaser band + P7 disclosure head
tree=ET.parse(DEL/"svg/p7-ciyu.svg")
for el in tree.iter():
    if el.tag.endswith("text") and "L'angolo dei lettori" in "".join(el.itertext()):
        print("P7 corner head:", "".join(el.itertext()))
