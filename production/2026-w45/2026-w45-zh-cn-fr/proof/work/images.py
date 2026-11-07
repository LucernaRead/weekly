import re, glob, hashlib, os
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg"
for label,d in [("ED",ED),("CORE",CO)]:
    print("=====",label)
    for f in sorted(glob.glob(d+"/*.svg")):
        s=open(f,encoding="utf-8").read()
        imgs=re.findall(r"<image[^>]*>", s)
        print(" ",os.path.basename(f),"images:",len(imgs))
        for im in imgs:
            href=re.search(r'(?:href|xlink:href)="([^"]*)"', im)
            print("    ",href.group(1) if href else im[:150])
        # credit lines
        ts=[re.sub(r"<[^>]+>","",m) for m in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
        for t in ts:
            if "Photo" in t and ("CC0" in t or "public domain" in t or "domaine" in t or "Commons" in t):
                print("    CREDIT:",repr(t[:160]))
