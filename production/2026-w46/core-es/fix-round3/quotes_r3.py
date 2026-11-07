# -*- coding: utf-8 -*-
"""Round 3 DE-only P7 quote/translation check (adapted from Round 1 quotes_check.py).
Verifies: 8 frozen Spanish quotes verbatim in P7 and in exactly one article page
each; 8 German translations present with (Página N) tags; Q6 fixed line exact.
Read-only; DE edition + frozen core only."""
import re, os, html
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")

def page_texts(code, pgfile):
    s = open(BASE + f"/files/weekly-report-w46-es-{code}/svg/{pgfile}", encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>", "", c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

QUOTES = [
    ("Q1", "El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral."),
    ("Q2", "El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos."),
    ("Q3", "Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío."),
    ("Q4", "España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa."),
    ("Q5", "No hace falta ir al colegio electoral para votar: el voto por correo llega a casa."),
    ("Q6", "La vivienda preocupa al 86,9 % de los españoles."),
    ("Q7", "Una encuesta es una foto con margen de error, tomada en un día concreto."),
    ("Q8", "El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45."),
]
TRANSLATIONS = [
    # Only Q6 is asserted verbatim here (the Round 1 fix, re-verified).
    # The other 7 translations are unchanged: P7 SVG is byte-identical to the
    # Round 2-verified render (see hash isolation), where 8/8 were verified.
    ("Q6", "86,9 % der Spanier sorgen sich um die Wohnung. (Página 6)"),
]
files = [("p1-portada.svg", 1), ("p2-vida.svg", 2), ("p3-cultura.svg", 3),
         ("p4-deporte.svg", 4), ("p5-juventud.svg", 5), ("p6-afondo.svg", 6)]
for code in ["de"]:
    joined = {pg: norm(" ".join(page_texts(code, fn))) for fn, pg in files}
    p7texts = page_texts(code, "p7-lengua.svg")
    p7joined = norm(" ".join(p7texts))
    print(f"===== es-{code} P7 quotes =====")
    for qid, q in QUOTES:
        hits = [pg for pg, t in joined.items() if norm(q) in t]
        print(qid, "article pages:", hits, "| P7 frozen quote present:", ("«" + q + "»") in p7joined)
    print("--- translations spot-checked (full 8/8 verified in Round 2; Q6 re-verified here) ---")
    for qid, tr in TRANSLATIONS:
        print(qid, "translation present in P7:", norm(tr) in p7joined)
    # all 8 translation lines: lines carrying a (Página N) tag in P7
    tagged = [t for t in p7texts if re.search(r"\(Página \d+\)", t)]
    print("P7 lines with (Página N) tag:", len(tagged))
    for t in tagged:
        print("  |", t)
    # defective D-6 / D-1 strings absent from whole edition (joined all pages)
    _pages = ["p1-portada", "p2-vida", "p3-cultura", "p4-deporte", "p5-juventud", "p6-afondo", "p7-lengua", "p8-ejercicios"]
    whole = norm(" ".join(" ".join(page_texts(code, pg + ".svg")) for pg in _pages))
    print("defective 'Was sorgt dich' occurrences (joined):", whole.count("Was sorgt dich"))
    print("defective 'Die Wohnung sorgt' occurrences (joined):", whole.count("Die Wohnung sorgt"))
    print("corrected 'Was beunruhigt dich am meisten' occurrences (joined):", whole.count("Was beunruhigt dich am meisten"))
    print("corrected question full (joined):", "Was beunruhigt dich am meisten: Löhne, Wohnungen oder Preise?" in whole)
    n = sum(len(page_texts(code, pg + ".svg")) for pg in
            ["p1-portada", "p2-vida", "p3-cultura", "p4-deporte", "p5-juventud", "p6-afondo", "p7-lengua", "p8-ejercicios"])
    print("<text> elements parsed (DE total):", n)
