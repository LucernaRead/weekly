import re, glob, os, html
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def page_texts(code, pgfile):
    s=open(BASE+f"/files/weekly-report-w46-es-{code}/svg/{pgfile}",encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
QUOTES=[
 ("Q1","El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral."),
 ("Q2","El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos."),
 ("Q3","Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío."),
 ("Q4","España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa."),
 ("Q5","No hace falta ir al colegio electoral para votar: el voto por correo llega a casa."),
 ("Q6","La vivienda preocupa al 86,9 % de los españoles."),
 ("Q7","Una encuesta es una foto con margen de error, tomada en un día concreto."),
 ("Q8","El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45."),
]
files=[("p1-portada.svg",1),("p2-vida.svg",2),("p3-cultura.svg",3),("p4-deporte.svg",4),("p5-juventud.svg",5),("p6-afondo.svg",6)]
def norm(s): return re.sub(r"\s+"," ",s).strip()
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    joined={pg: norm(" ".join(page_texts(code,fn))) for fn,pg in files}
    p7joined=norm(" ".join(page_texts(code,"p7-lengua.svg")))
    for qid,q in QUOTES:
        hits=[pg for pg,t in joined.items() if norm(q) in t]
        # also count occurrences in whole issue incl P7 (expect 2: article + P7; Q6/Q7 may appear in P6 text + P7)
        whole=" ".join(list(joined.values())+[p7joined])
        print(qid, "article pages:", hits, "| P7 contains:", norm(q) in p7joined)
    # Q8 tag check: P7 translation line tag
    p7=page_texts(code,"p7-lengua.svg")
    for t in p7:
        if "Metropolitano" in t or "小组赛" in t: print("  P7:", t[:160])
