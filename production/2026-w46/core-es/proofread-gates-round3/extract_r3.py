import re, xml.etree.ElementTree as ET, pathlib, json
ED = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-de"
NS="{http://www.w3.org/2000/svg}"
def texts(name):
    t=ET.parse(ED/"svg"/name)
    out=[]
    for el in t.iter(NS+"text"):
        out.append((el.get("x"), el.get("y"), el.get("font-size"), el.get("font-weight"), el.get("fill"), el.get("text-anchor"), (el.text or "")))
    return out
# P2 col3 x=1473 block: dump all texts with x=1473 sorted by y
print("=== P2 x=1473 texts (y, size, text) ===")
for x,y,fs,w,f,a,txt in texts("p2-vida.svg"):
    if x=="1473":
        print(f"y={y} fs={fs} :: {txt}")
print("\n=== P2 all texts containing beunruhigt/sorgt/Schreib ===")
for x,y,fs,w,f,a,txt in texts("p2-vida.svg"):
    if any(k in txt for k in ("beunruhigt","sorgt","Schreib","Was machst","Was beunruhigt")):
        print(f"x={x} y={y} fs={fs} :: {txt}")
print("\n=== P2 rects near col3 (box geometry) ===")
t=ET.parse(ED/"svg"/"p2-vida.svg")
for el in t.iter():
    tag=el.tag.replace(NS,"")
    if tag in ("rect","line"):
        try:
            x=float(el.get("x",0) or 0); y=float(el.get("y",0) or 0); w=float(el.get("width",0) or 0); h=float(el.get("height",0) or 0)
        except: continue
        if x>=1400 and y>=800 and y<=1200:
            print(tag, dict(el.attrib))
print("\n=== P7 Q6 area: texts x=989 y 2050-2200 ===")
for x,y,fs,w,f,a,txt in texts("p7-lengua.svg"):
    try: yf=float(y)
    except: continue
    if x=="989" and 2000<=yf<=2200:
        print(f"y={y} fs={fs} :: {txt}")
print("\n=== P7 defective check ===")
allp7=[txt for *_,txt in texts("p7-lengua.svg")]
print("Die Wohnung sorgt count:", sum("Die Wohnung sorgt" in s for s in allp7))
print("sorgen sich um die Wohnung lines:", [s for s in allp7 if "sorgen sich um die Wohnung" in s])
print("\n=== Badge/footer ===")
for name in ["p1-portada.svg","p2-vida.svg","p3-cultura.svg","p4-deporte.svg","p5-juventud.svg","p6-afondo.svg","p7-lengua.svg","p8-ejercicios.svg"]:
    ts=texts(name)
    badge=[s for s in ts if "SPANISCHER TEXT" in s[6]]
    foot=[s for s in ts if "ERKLÄRUNGEN AUF DEUTSCH" in s[6]]
    pageline=[s for s in ts if re.match(r"Seite \d von 8", s[6])]
    print(name, "badge:", badge, "footer:", foot, "pageline:", pageline)
print("\n=== P1 masthead/tagline ===")
for x,y,fs,w,f,a,txt in texts("p1-portada.svg"):
    if y in ("262","372","574") or "La Lucerna" in txt:
        print(f"x={x} y={y} fs={fs} w={w} fill={f} anchor={a} :: {txt}")
print("\n=== P6 chart rects ===")
t=ET.parse(ED/"svg"/"p6-afondo.svg")
for el in t.iter(NS+"rect"):
    try:
        x=float(el.get("x")); y=float(el.get("y")); w=float(el.get("width")); h=float(el.get("height"))
    except: continue
    if w>10 and h and 5<h<40:
        print(f"rect x={x} y={y} w={w} h={h} fill={el.get('fill')}")
print("\n=== text counts per page ===")
for name in ["p1-portada.svg","p2-vida.svg","p3-cultura.svg","p4-deporte.svg","p5-juventud.svg","p6-afondo.svg","p7-lengua.svg","p8-ejercicios.svg"]:
    print(name, len(texts(name)))
