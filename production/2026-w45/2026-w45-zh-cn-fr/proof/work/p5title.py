import re
from PIL import ImageFont
s=open("/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg/p5-qingnian.svg",encoding="utf-8").read()
for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
    t=re.sub(r"<[^>]+>","",m.group(2))
    if "Mots de la semaine" in t:
        a=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        print("title node:",a,repr(t))
        # measure ink: font sans bold? check weight
        bold=a.get("font-weight") in ("700","bold")
        size=float(a.get("font-size",20))
        path="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
        f=ImageFont.truetype(path,int(round(size)),index=2)
        l,tt,r,b=f.getbbox(t); adv=f.getlength(t)
        x=float(a["x"]); anchor=a.get("text-anchor","start")
        if anchor=="middle": x0=x-adv/2+l; x1=x-adv/2+r
        elif anchor=="end": x0=x-adv+l; x1=x-adv+r
        else: x0=x+l; x1=x+r
        print(f"  ink x0={x0:.1f} x1={x1:.1f} (builder claims ink end 953.9 vs border 961)")
# find bordered box rects near title y
for m in re.finditer(r"<rect([^>]*)/>", s):
    a=dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
    try: y=float(a.get("y",0)); x=float(a.get("x",0)); w=float(a.get("width",0))
    except: continue
    if 500<y<800 and x<100:
        print("  rect near:",a)
