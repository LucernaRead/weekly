import re, html, pathlib
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
def pagetexts(d):
    out={}
    for f in sorted(d.glob("*.svg")):
        s=f.read_text(encoding="utf-8")
        txts=[html.unescape(re.sub(r'<[^>]+>','',m)) for m in re.findall(r'<text[^>]*>(.*?)</text>', s, re.S)]
        out[f.name]=" ".join(txts)
    return out
def norm(t): return re.sub(r'\s+',' ',t).strip()
def squish(t): return re.sub(r'\s+','',t)
quotes=[
 ("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.",4),
 ("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.",2),
 ("Wer 50 Liter tankt, spart rund 8,35 Euro.",2),
 ("Die Schule hat nach den Herbstferien wieder begonnen.",5),
 ("Die Tage sind kurz, die Abende lang.",3),
 ("Zwei schwere Auswärtsspiele für die deutschen Teams.",4),
 ("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.",6),
 ("Es geht langsam aufwärts — aber von allein geht es nicht.",6),
]
pagefile={1:'p1-front.svg',2:'p2-leben.svg',3:'p3-kultur.svg',4:'p4-sport.svg',5:'p5-jugend.svg',6:'p6-vertiefung.svg',7:'p7-sprache.svg',8:'p8-uebungen.svg'}
for name,d in [("CORE",G/"files/weekly-report-w45-de-core/svg"),("ED",G/"files/weekly-report-w45-de-zh-tw/svg")]:
    pages=pagetexts(d); whole=norm(" ".join(pages.values()))
    print(f"===== {name} =====")
    for q,pg in quotes:
        n=whole.count(norm(q))
        # source-page check: squished quote in squished claimed page (excluding P7 itself for article occurrence)
        src=squish(q) in squish(pages[pagefile[pg]])
        p7=squish(q) in squish(pages['p7-sprache.svg'])
        print(f"count={n} claimedSeite={pg} in-claimed-page={src} in-P7={p7} :: {q[:60]}")
    # P7 tags in order
    p7els=re.findall(r'Seite \d · [AB]\d', pages['p7-sprache.svg'])
    print("P7 tags order:", p7els)
