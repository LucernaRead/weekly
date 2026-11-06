import re, os, glob, html
from collections import Counter
G=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED=f"{G}/files/weekly-report-w45-de-es/svg"; CORE=f"{G}/files/weekly-report-w45-de-core/svg"; W43=f"{G}/files/weekly-report-de-es/svg"
def raw(p): return open(p,encoding="utf-8").read()
def texts(p):
    return [re.sub(r"\s+"," ",html.unescape(re.sub(r"<[^>]+>","",c))).strip() for c in re.findall(r"<text[^>]*>(.*?)</text>",raw(p),re.S)]
def joined(p): return " ".join(texts(p))
# gloss: find Nota — ... segments containing · ; split by · per box: use joined text, find gloss boxes by keywords
print("== GLOSS split by · (raw text search) ==")
for pg,kw in [("p2-leben.svg","Tankrabatt"),("p3-kultur.svg","Ferienwechsel"),("p4-sport.svg","Englische Woche"),("p5-jugend.svg","Pausenhof"),("p6-vertiefung.svg","Angehörige")]:
    t=joined(f"{ED}/{pg}")
    # find Nota segment: from Nota — to next title-ish? print surrounding
    i=t.find("Nota —")
    print(pg, "Nota idx", i)
    # count · in gloss region: take from first Nota to '. ' end? Just print gloss chunk (first 600 chars from Nota)
    print("  chunk:", t[i:i+700] if i>=0 else "NOT FOUND")
    # count items: split chunk by · ; first chunk contains Nota prefix
    if i>=0:
        chunk=t[i:]
        # gloss ends at next section? approximate: count · before '· der' etc - just report total · in first 700
        print("  · count in chunk700:", chunk[:700].count("·"))
print("\n== P7 sentences ==")
sents=["Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.","Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.","Wer 50 Liter tankt, spart rund 8,35 Euro.","Die Schule hat nach den Herbstferien wieder begonnen.","Die Tage sind kurz, die Abende lang.","Zwei schwere Auswärtsspiele für die deutschen Teams.","Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.","Es geht langsam aufwärts — aber von allein geht es nicht."]
full=" ".join(joined(f"{ED}/{p}") for p in ["p1-front.svg","p2-leben.svg","p3-kultur.svg","p4-sport.svg","p5-jugend.svg","p6-vertiefung.svg","p7-sprache.svg"])
full_n=re.sub(r"\s+"," ",full)
for s in sents: print(full_n.count(s), "|", s)
print("P7 Seite labels in p7:", Counter(re.findall(r"Seite \d", joined(f"{ED}/p7-sprache.svg"))))
print("Core P7 Seite labels:", Counter(re.findall(r"Seite \d", joined(f"{CORE}/p7-sprache.svg"))))
print("P7 table labels (Seite N · level):", re.findall(r"Seite \d · [A-Z]\d", joined(f"{ED}/p7-sprache.svg")))
print("Core P7 table labels:", re.findall(r"Seite \d · [A-Z]\d", joined(f"{CORE}/p7-sprache.svg")))
print("\n== translations 7/8 ==")
for n in [7,8]:
    pass
p7=joined(f"{ED}/p7-sprache.svg")
for tr in ["La economía alemana sale del estancamiento, pero aún no se sostiene sola.","Mejora lentamente, pero no mejora sola."]:
    print(tr, "count:", p7.count(tr), "has lentamente:", "lentamente" in tr)
print("\n== badge vs W43 ==")
def badge(p):
    s=raw(p)
    m=re.search(r"<text[^>]*>[^<]*TEXTOS EN ALEMÁN[^<]*</text>",s)
    return m.group(0) if m else None
print("ED badge:", badge(f"{ED}/p1-front.svg"))
print("W43 badge:", badge(f"{W43}/p1-front.svg"))
print("identical:", badge(f"{ED}/p1-front.svg")==badge(f"{W43}/p1-front.svg"))
print("\n== footer / masthead ==")
for f in sorted(glob.glob(ED+"/*.svg")):
    t=joined(f)
    print(os.path.basename(f), "footer:", "Die Lucerna · SEMANARIO ALEMÁN VOL.2 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL" in t, "| Página:", re.findall(r"Página \d de 8",t), "| Die Lucerna count:", t.count("Die Lucerna"))
print("\n== reader garden P7 ==")
p7t=joined(f"{ED}/p7-sprache.svg")
for frag in ["¡Un ejemplo de la redacción!","Ejemplo de la redacción, no una carta real:","hasta el cierre, sin cartas reales ni mejores","textos de la página 8. ¡Envíanos tu carta","real para VOL.3!","LESERBRIEFE · Tus cartas"]:
    print(frag, "->", frag in p7t)
# raw joined with spaces may split; also check normalized full p7 svg text
pn=re.sub(r"\s+"," ",p7t)
print("full sentence normalized present:", "Ejemplo de la redacción, no una carta real: hasta el cierre, sin cartas reales ni mejores textos de la página 8. ¡Envíanos tu carta real para VOL.3!" in pn)
print("\n== P8 separators / keys ==")
p8=joined(f"{ED}/p8-uebungen.svg")
print("separators:", re.findall(r"— Página \d —",p8))
print("key140 present:", "Am Sonntag schlafe ich eine Stunde länger." in p8)
print("key137/138/139:", [x for x in ["El descuento en la gasolina dura hasta diciembre.","Veo fútbol el martes.","La escuela ha empezado de nuevo."] if x in p8])
print("key150:", "Pregunta abierta" in p8)
corep8=joined(f"{CORE}/p8-uebungen.svg")
print("core key140:", "Am Sonntag schlafe ich eine Stunde länger." in corep8)
print("core 137/138/139 zh keys present:", "油价减税持续到十二月" in corep8, "我周二看足球" in corep8, "学校又开学" in corep8)
print("\n== first-22 original strings absent in final ==")
orig=["Las grandes preguntas de la semana · Die Fragen der Woche","Las cinco preguntas de las que habla Alemania esta semana.","DIE WOCHE IN ZAHLEN · La semana en cifras","IN DIESER AUSGABE · En este número","AN DER ZAPFSÄULE · En el surtidor","FERIENWECHSEL · Cambio de vacaciones","HERBSTWÖRTER · Palabras de otoño","DER TIPP · Consejo de la redacción","SCHULWÖRTER · Palabras del colegio","familiares que cuidan","servicio profesional","en una residencia","ÜBUNGSDATEN · Datos de práctica — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.","DIE ZAHLEN · Las cifras de la semana","LESERBRIEFE · Cartas de los lectores"]
allf=" ".join(joined(f) for f in sorted(glob.glob(ED+"/*.svg")))
for o in orig: print(("ABSENT OK" if o not in allf else "STILL PRESENT!!"), o[:60])
print("final replacements present:", [x for x in ["DIE WOCHE IN ZAHLEN · En cifras","Preguntas · Die Fragen der Woche","Las cinco preguntas de la semana.","IN DIESER AUSGABE · Contenido","AN DER ZAPFSÄULE · El surtidor","FERIENWECHSEL · Vacaciones","HERBSTWÖRTER · Vocabulario","DER TIPP · Consejo","SCHULWÖRTER · Vocabulario","LESERBRIEFE · Tus cartas","DIE ZAHLEN · Cifras"] if x in allf])
print("\n== ABSTRACT ==")
a=open(f"{G}/files/weekly-report-w45-de-es/ABSTRACT.txt",encoding="utf-8").read()
print(repr(a)); print("lines:", a.strip().count("\n")+1 if a.strip() else 0, "has ASCII dq:", '"' in a, "has aprender alemán con fútbol:", "aprender alemán con fútbol" in a)
