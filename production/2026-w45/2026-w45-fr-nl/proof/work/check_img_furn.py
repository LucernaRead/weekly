import re, base64, hashlib, sys
sys.path.insert(0, "/home/hatch/workspace/goals/lucernaread-social-media-operations/tools")
from occlusion_audit import ink_box
from pathlib import Path
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
IMG = re.compile(r'<image x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*href="data:image/jpeg;base64,([^"]+)"')
ATTR = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"([^>]*)>([^<]*)</text>')
for label,d in [("ED",BASE/"weekly-report-w45-fr-nl/svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg")]:
    print(f"===== {label} images =====")
    for p in sorted(d.glob("*.svg")):
        raw=p.read_text(encoding="utf-8")
        for m in IMG.finditer(raw):
            b64=m.group(5); dec=base64.b64decode(b64)
            print(f" {p.name} x={m.group(1)} y={m.group(2)} w={m.group(3)} h={m.group(4)} b64sha={hashlib.sha256(b64.encode()).hexdigest()[:16]} decsha={hashlib.sha256(dec).hexdigest()[:16]} decbytes={len(dec)} b64len={len(b64)}")
    print(f"===== {label} credit-ish lines =====")
    for p in sorted(d.glob("*.svg")):
        raw=p.read_text(encoding="utf-8")
        for m in ATTR.finditer(raw):
            s=m.group(6)
            if any(k in s for k in ["Atget","Hiroshige","Flora de Filipinas","LACMA","Blanco","1857","1797","XIXe","Crédit","Credit","©","Source"]):
                print(f" {p.name} y={m.group(2)} x={m.group(1)} fs={m.group(4)} {s!r}")
print("===== ED P7 reader box + preview ink =====")
raw=(BASE/"weekly-report-w45-fr-nl/svg/p7-langue.svg").read_text(encoding="utf-8")
# reader box rect (989,1878)-(1885,2258); preview strip (989,2270)-(1885,2540)
for name,(bx0,by0,bx1,by1) in [("reader-box",(989,1878,1885,2258)),("preview-strip",(989,2270,1885,2540))]:
    inside=[]
    for m in ATTR.finditer(raw):
        x,y,fam,fs,rest,s=float(m.group(1)),float(m.group(2)),m.group(3),float(m.group(4)),m.group(5),m.group(6)
        bold='font-weight="700"' in rest; am=re.search(r'text-anchor="([^"]*)"',rest); anchor=am.group(1) if am else "start"
        ib=ink_box(s,fam,fs,bold,x,y,anchor)
        if ib and bx0<=ib[0] and ib[2]<=bx1 and by0<=ib[1] and ib[3]<=by1:
            inside.append((y,ib[3],s[:70]))
    inside.sort()
    print(f" {name}: n={len(inside)} max_ink_bottom={max(v[1] for v in inside):.2f} box_bottom={by1} margin={by1-max(v[1] for v in inside):.2f}")
    for y,b,s in inside[-4:]: print(f"   last y={y} inkbot={b:.2f} {s!r}")
    for y,b,s in inside[:3]: print(f"   first y={y} {s!r}")
print("===== ED column heads / P8 heads =====")
for p in sorted((BASE/"weekly-report-w45-fr-nl/svg").glob("*.svg")):
    raw=p.read_text(encoding="utf-8")
    heads=[]
    for m in ATTR.finditer(raw):
        if float(m.group(4))>=23 and "·" in m.group(6):
            heads.append((float(m.group(2)),m.group(6)))
    print(f" {p.name}:")
    for y,s in sorted(heads): print(f"   y={y} {s!r}")
print("===== ED P8 separators + keys head =====")
raw=(BASE/"weekly-report-w45-fr-nl/svg/p8-exercices.svg").read_text(encoding="utf-8")
print(" seps:",[m.group(6) for m in ATTR.finditer(raw) if "PAGINA" in m.group(6)])
print(" keys head:",[m.group(6) for m in ATTR.finditer(raw) if "RÉPONSES" in m.group(6)])
print("===== W43 P8 separators + keys head =====")
raw=(BASE/"weekly-report-fr-nl/svg/p8-exercices.svg").read_text(encoding="utf-8")
print(" seps:",[m.group(6) for m in ATTR.finditer(raw) if "PAGINA" in m.group(6)])
print(" keys head:",[m.group(6) for m in ATTR.finditer(raw) if "RÉPONSES" in m.group(6)])
print("===== exercise numbers per page (ED vs CORE) =====")
NUM=re.compile(r"^(\d+)\.$")
for label,d in [("ED",BASE/"weekly-report-w45-fr-nl/svg"),("CORE",BASE/"weekly-report-w45-fr-core/svg")]:
    print(f" {label}:")
    for p in sorted(d.glob("*.svg")):
        raw=p.read_text(encoding="utf-8"); nums=[]
        for m in ATTR.finditer(raw):
            mm=NUM.match(m.group(6).strip())
            if mm:
                y=float(m.group(2))
                # P8: battery only (y<1526, and not answer section); other pages: all
                if p.name=="p8-exercices.svg" and y>=1526: continue
                nums.append(int(mm.group(1)))
        print(f"   {p.name}: count={len(nums)} range={min(nums) if nums else None}..{max(nums) if nums else None} nums={nums}")
