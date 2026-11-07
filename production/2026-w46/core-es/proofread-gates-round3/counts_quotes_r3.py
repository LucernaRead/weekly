import re, xml.etree.ElementTree as ET, pathlib, json, collections
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
ED=BASE/"weekly-report-w46-es-de"; CORE=BASE/"weekly-report-w46-es-core"
NS="{http://www.w3.org/2000/svg}"
def texts(d,name):
    t=ET.parse(d/"svg"/name); return [(el.get("x"),el.get("y"),el.get("font-size"),(el.text or "")) for el in t.iter(NS+"text")]
names=["p1-portada.svg","p2-vida.svg","p3-cultura.svg","p4-deporte.svg","p5-juventud.svg","p6-afondo.svg","p7-lengua.svg","p8-ejercicios.svg"]
# Count stems: elements exactly "N." plus grouped headers? Replicate Round1: standalone stems = elements matching ^\d+\.$ ; grouped sets counted via section headers.
# Instead: count all exercise-number mentions in P1-P7 stems + P8: use text.md? Better: SVG stem elements.
for d,label in [(ED,"DE"),(CORE,"CORE")]:
    print(f"=== {label} stem elements ===")
    total_standalone=0; perpage=[]
    for nm in names:
        ts=texts(d,nm)
        stems=[s for s in ts if re.fullmatch(r"\d+\.", s[3].strip())]
        nums=sorted(int(s[3].strip()[:-1]) for s in stems)
        perpage.append((nm,len(stems),nums))
        total_standalone+=len(stems)
        print(nm, len(stems), nums[:5],"...",nums[-5:] if nums else [])
    print("standalone total:", total_standalone)
# Level chips: elements exactly A2/B1/B2 paired on same baseline as stems (Round1 method: same-baseline chip pairing)
print("\n=== DE level pairing (stem baseline -> chip) ===")
lvl=collections.Counter(); unpaired=[]
for nm in names:
    ts=texts(d,nm) if False else texts(ED,nm)
    # group by y (rounded)
    byg={}
    for x,y,fs,txt in ts:
        byg.setdefault(round(float(y),1),[]).append((x,txt))
    for y,items in byg.items():
        stems=[t for _,t in items if re.fullmatch(r"\d+\.", t.strip())]
        chips=[t for _,t in items if t.strip() in ("A2","B1","B2")]
        for s in stems:
            if chips: lvl[chips[0].strip()]+=1
            else: unpaired.append((nm,y,s,items))
print(dict(lvl), "unpaired stems:", unpaired[:20], "count unpaired:", len(unpaired))
# Quotes: 8 Spanish quotes verbatim check
quotes=[
 ("Q1","El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral."),
 ("Q2","El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos."),
 ("Q3","Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío."),
 ("Q4","España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa."),
 ("Q5","No hace falta ir al colegio electoral para votar: el voto por correo llega a casa."),
 ("Q6","La vivienda preocupa al 86,9 % de los españoles."),
 ("Q7","Una encuesta es una foto con margen de error, tomada en un día concreto."),
 ("Q8","El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45."),
]
def joined(d,nm):
    return " ".join(t[3] for t in texts(d,nm))
print("\n=== P7 quotes ===")
p7=joined(ED,"p7-lengua.svg")
for qid,q in quotes:
    # normalize whitespace
    nq=re.sub(r"\s+"," ",q)
    hits=sum(1 for nm in names if nq in re.sub(r"\s+"," ",joined(ED,nm)))
    print(qid, "in P7:", nq in re.sub(r"\s+"," ",p7), "pages containing:", hits, "|", q[:60])
print("\n=== P7 translation lines (Página tags) ===")
for x,y,fs,txt in texts(ED,"p7-lengua.svg"):
    if "(Página" in txt: print(f"y={y} fs={fs} :: {txt}")
print("\n=== P7 Q6 pair ===")
for x,y,fs,txt in texts(ED,"p7-lengua.svg"):
    if "86,9" in txt: print(f"x={x} y={y} fs={fs} :: {txt}")
