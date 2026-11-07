import xml.etree.ElementTree as ET, pathlib, re, json, sys
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
G=BASE/"hidden_files/w46/zh-tw-proofread-gates"
NS="{http://www.w3.org/2000/svg}"
def texts(svg):
    root=ET.parse(svg).getroot()
    out=[]
    for el in root.iter(NS+"text"):
        t="".join(el.itertext()).strip()
        if t: out.append((float(el.get("x",0)), float(el.get("y",0)), el.get("font-size",""), el.get("fill",""), t))
    return out
editions={"de":"weekly-report-w46-zh-tw-de","es":"weekly-report-w46-zh-tw-es","fr":"weekly-report-w46-zh-tw-fr","it":"weekly-report-w46-zh-tw-it","ja":"weekly-report-w46-zh-tw-ja","ko":"weekly-report-w46-zh-tw-ko","nl":"weekly-report-w46-zh-tw-nl","pt":"weekly-report-w46-zh-tw-pt","ru":"weekly-report-w46-zh-tw-ru","en":"weekly-report-w46-zhtw-core"}
for nat,dirname in editions.items():
    d=BASE/"files"/dirname/"svg"
    for svg in sorted(d.glob("*.svg")):
        lines=texts(svg)
        with open(G/f"txt-{nat}-{svg.stem}.txt","w",encoding="utf-8") as f:
            for x,y,fs,fill,t in lines:
                f.write(f"[{y:8.1f} x={x:6.0f} fs={fs} fill={fill}] {t}\n")
print("done")
# targeted: Practice
for nat,dirname in editions.items():
    svg=BASE/"files"/dirname/"svg"/"p5-youth.svg"
    ts=[t for *_,t in texts(svg)]
    hits=[t for t in ts if "Practice" in t or "450" in t or "1,550" in t or "2,000" in t or "budget" in t.lower()]
    print(f"== {nat} P5 Practice-related text nodes ({len(hits)}):")
    for h in hits: print("   ",repr(h))
