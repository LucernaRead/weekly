import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
G=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED=f"{G}/files/weekly-report-w45-de-es/svg"
def load(name):
    s=open(f"{ED}/{name}",encoding="utf-8").read()
    return OA.parse_svg(s)
for name in ["p1-front.svg","p2-leben.svg","p6-vertiefung.svg","p8-uebungen.svg"]:
    els,_,_=load(name)
    print(f"\n== {name}: {len(els)} elements ==")
    if name=="p1-front.svg":
        for e in els:
            if e.kind=="text" and e.box and e.box[1]<250:
                print(f" y={e.attrs.get('y')} box={tuple(round(v,1) for v in e.box)} text={e.text!r:.120}")
        # dark band: search texts containing Semana / Champions / Tankrabatt subtitle?
        for e in els:
            if e.kind=="text" and e.text and ("Semana de fútbol" in e.text or "Champions" in e.text or "Der Tankrabatt" in e.text or "FUSSBALL" in e.text):
                print(" band:", e.attrs.get('y'), tuple(round(v,1) for v in e.box), e.text[:100])
    if name=="p2-leben.svg":
        # elements whose ink bottom near 1550-1560, and line at 1554
        for e in els:
            if e.box and 1540 < e.box[3] < 1570:
                print(f" near1554: kind={e.kind} box={tuple(round(v,2) for v in e.box)} text={(e.text or '')[:80]!r} attrs={e.attrs}")
        for e in els:
            if e.kind=="line" and e.attrs.get("y1")=="1554": print(" line1554:", e.attrs, e.box)
    if name=="p6-vertiefung.svg":
        for e in els:
            if e.kind=="text" and e.text and e.text.strip() in ("familiares","servicio","residencia") or (e.kind=="text" and e.text and ("zu Hause" in e.text or "professionell" in e.text or "Heim" in e.text)):
                print(f" chart text: y={e.attrs.get('y')} x={e.attrs.get('x')} box={tuple(round(v,1) for v in e.box)} {e.text!r}")
        for e in els:
            if e.kind=="rect" and e.box and e.box[1] in (1482.0,1534.0,1586.0) or (e.kind=="rect" and e.box and 1470<e.box[1]<1620 and e.box[0]==535.0):
                print(f" bar rect: box={e.box} attrs={e.attrs}")
        # German chart labels: texts at x=65 y ~1480-1610
        for e in els:
            if e.kind=="text" and e.attrs.get("x")=="65" and e.box and 1450<e.box[1]<1650:
                print(f" DE label: box={tuple(round(v,1) for v in e.box)} {e.text!r}")
    if name=="p8-uebungen.svg":
        # keys section: texts with font-size 12, max ink bottom
        ks=[e for e in els if e.kind=="text" and e.attrs.get("font-size")=="12"]
        print(" 12pt texts:", len(ks), "max ink bottom:", max(e.box[3] for e in ks if e.box), "min top:", min(e.box[1] for e in ks if e.box))
        ks_sorted=sorted(ks, key=lambda e: e.box[3] if e.box else 0)
        for e in ks_sorted[-6:]: print("  last12:", tuple(round(v,1) for v in e.box), (e.text or "")[:90])
        # check gap/lh in content8
