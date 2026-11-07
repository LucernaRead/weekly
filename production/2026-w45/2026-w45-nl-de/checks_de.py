# -*- coding: utf-8 -*-
"""DE edition supplementary gates (in addition to tools/occlusion_audit.py):
golden sentences 2x verbatim with correct page labels; P7 phrases verbatim
from this issue's articles; P7 word-box Dutch definition sentence verbatim;
readers' corner three facts + explicit German imperative invitation;
footers 8/8 VOL.2 + badge; image credits present and placed; banned strings;
Chinese chars 0; 'bridge' term 0; P8 footer/page lines.
"""
import re, os, html, sys

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-de/svg")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-core/svg")
TEXT_RE = re.compile(r'<text[^>]*>([^<]*)</text>')

def texts(d, name):
    t = open(os.path.join(d, name), encoding="utf-8").read()
    return [html.unescape(m) for m in TEXT_RE.findall(t)], t

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

pages = ["p1-voorpagina.svg", "p2-leven.svg", "p3-cultuur.svg", "p4-sport.svg",
         "p5-jongeren.svg", "p6-verdieping.svg", "p7-taal.svg", "p8-toets.svg"]
all_ed = {}
for pg in pages:
    ts, raw = texts(ED, pg)
    all_ed[pg] = (ts, raw)
full = " ".join(norm(" ".join(ts)) for ts, _ in all_ed.values())

print("== footers / badge ==")
badge = "NIEDERLÄNDISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
print("badge on P1:", badge in norm(" ".join(all_ed["p1-voorpagina.svg"][0])))
for pg in pages:
    ts, _ = all_ed[pg]
    joined = norm(" ".join(ts))
    n = pg[1]
    foot = "De Lucerna · NIEDERLÄNDISCHE WOCHENZEITUNG VOL.2 · TEXT AUF NIEDERLÄNDISCH · ERKLÄRUNGEN AUF DEUTSCH"
    line = f"Seite {n} von 8"
    print(f"  {pg}: footer={foot in joined} pageline={line in joined}")

print("== golden sentences (Dutch, verbatim, 2x, page labels) ==")
quotes = [
    ("Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland", "Pagina 1"),
    ("De herfst is de beste tijd om te planten", "Pagina 1"),
    ("Geel betekent: let op, het weer kan gevaarlijk zijn", "Pagina 2"),
    ("Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts", "Pagina 3"),
    ("Ajax won donderdag 22 oktober met 2–0 van Atalanta", "Pagina 4"),
    ("Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur", "Pagina 5"),
    ("Een code is geen verbod, maar een advies", "Pagina 6"),
    ("Het weer is van ons allemaal, maar het raakt ons allemaal anders", "Pagina 6"),
]
for q, pg in quotes:
    c = full.count(norm(q))
    print(f"  count={c} label={pg} present_on_P7={pg in norm(' '.join(all_ed['p7-taal.svg'][0]))} :: {q[:60]}")

print("== P7 phrases verbatim from articles ==")
# P7 golden-sentence table rows carry the German translation + (Pagina N);
# the Dutch quotes above ARE the phrases; check each appears in its source page too
src = {"Pagina 1": "p1-voorpagina.svg", "Pagina 2": "p2-leven.svg", "Pagina 3": "p3-cultuur.svg",
       "Pagina 4": "p4-sport.svg", "Pagina 5": "p5-jongeren.svg", "Pagina 6": "p6-verdieping.svg"}
for q, pg in quotes:
    s = norm(" ".join(texts(ED, src[pg])[0]))
    print(f"  in {pg}: {norm(q) in s} :: {q[:50]}")

print("== P7 word-box Dutch definition verbatim ==")
wt = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
print("  HET WOORD Dutch sentence verbatim:", wt in norm(" ".join(all_ed["p7-taal.svg"][0])))
# PAS OP Dutch wrong/correction lines verbatim vs core P7
cts, _ = texts(CORE, "p7-taal.svg")
ets, _ = all_ed["p7-taal.svg"]
for s in ["«Het klimaat is slecht weer.»", "«Ik doe mee aan de klimaatweek.»", "«Ik plant een bomen.»",
          "«Omdat het regent, ik blijf thuis.»", "→ Fout: het klimaat is het weer over een lange tijd.",
          "→ «Klimaatweek» krijgt een hoofdletter: het is een naam.",
          "→ «Een» is enkelvoud: «een boom» of «bomen».",
          "→ Na «omdat» staat het werkwoord op plaats 2: «... blijf ik thuis.»"]:
    print(f"  PAS OP frozen: {s in norm(' '.join(ets))} :: {s[:50]}")

print("== readers' corner (P7) ==")
p7 = norm(" ".join(all_ed["p7-taal.svg"][0]))
print("  Dutch disclosure (frozen):", "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3." in p7)
print("  German disclosure:", "Redaktionsschluss: keine echten Briefe, keine besten Seite-8-Texte — darum ein Beispiel; Versprechen für VOL.3." in p7)
print("  example labelled:", "Beispiel der Redaktion, kein echter Brief." in p7)
print("  imperative invitation:", "Schicke uns echte Briefe und beste Seite-8-Texte — wir drucken sie in VOL.3!" in p7)
print("  example letter frozen:", "«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)" in p7)

print("== credits ==")
for pg, credit in [("p1-voorpagina.svg", "Foto: Vovogov90 — CC0"),
                   ("p2-leven.svg", "Foto: Nationaal Archief — CC0"),
                   ("p3-cultuur.svg", "Foto: W. Punt / Anefo, Nationaal Archief — CC0"),
                   ("p4-sport.svg", "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")]:
    print(f"  {pg}: {credit in norm(' '.join(all_ed[pg][0]))}")

print("== banned / residual ==")
cjk = re.compile(r'[\u4e00-\u9fff]')
total_cjk = 0
for pg in pages:
    ts, raw = all_ed[pg]
    n = sum(len(cjk.findall(x)) for x in ts)
    total_cjk += n
    print(f"  {pg}: CJK chars in text nodes = {n}")
print("  TOTAL CJK:", total_cjk)
for term in ["桥接", "讲解", "译注"]:
    print(f"  banned {term!r}: {sum(term in ' '.join(ts) for ts, _ in all_ed.values())} pages contain it")
print("  ASCII double-quote count in SVG texts:",
      sum(s.count('"') for ts, _ in all_ed.values() for s in ts))
print("  OEFENDATA label present (P6):", "OEFENDATA" in norm(" ".join(all_ed["p6-verdieping.svg"][0])))
