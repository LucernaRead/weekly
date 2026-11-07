# -*- coding: utf-8 -*-
"""Builder self-gates for NL x ES W45 (run after render.py)."""
import re, sys, os
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
CORE = os.path.join(BASE, "weekly-report-w45-nl-core", "svg")
ED = os.path.join(BASE, "weekly-report-w45-nl-es", "svg")

def texts(path):
    txt = open(path, encoding="utf-8").read()
    return re.findall(r'>([^<]+)<', txt), txt

def norm_join(ts):
    return " ".join(t.strip() for t in ts)

print("== pages ==")
import glob
print("core svgs:", len(glob.glob(os.path.join(CORE, "*.svg"))), "ed svgs:", len(glob.glob(os.path.join(ED, "*.svg"))))

print("== banned / CJK / full-width scans on edition SVGs ==")
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    txt = open(f, encoding="utf-8").read()
    cjk = len(re.findall(r'[\u4e00-\u9fff]', txt))
    full = txt.count("（") + txt.count("）")
    print(os.path.basename(f), "CJK:", cjk, "fullwidth-parens:", full,
          "banned-term:", txt.count("桥接"), "VOL.2 footer:", txt.count("VOL.2"))

print("== footers ==")
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    ts, _ = texts(f)
    foots = [t for t in ts if "SEMANARIO NEERLANDÉS VOL.2" in t or "Página " in t]
    print(os.path.basename(f), foots)

print("== P7 golden sentences: each core Dutch sentence must appear exactly 2x in edition (article + P7) ==")
import json
core_all = ""
for f in sorted(glob.glob(os.path.join(CORE, "*.svg"))):
    core_all += " " + norm_join(texts(f)[0])
ed_all = ""
for f in sorted(glob.glob(os.path.join(ED, "*.svg"))):
    ed_all += " " + norm_join(texts(f)[0])
# golden quotes from content7 (Dutch, verbatim)
quotes = [
    "Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland",
    "De herfst is de beste tijd om te planten",
    "Geel betekent: let op, het weer kan gevaarlijk zijn",
    "Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts",
    "Ajax won donderdag 22 oktober met 2–0 van Atalanta",
    "Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur",
    "Een code is geen verbod, maar een advies",
    "Het weer is van ons allemaal, maar het raakt ons allemaal anders",
]
def squash(s):
    return re.sub(r'\s+', ' ', s)
core_sq, ed_sq = squash(core_all), squash(ed_all)
for q in quotes:
    print("core:", core_sq.count(q), "ed:", ed_sq.count(q), "|", q[:60])

print("== P7 word-box definition verbatim ==")
wt = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
print("core:", core_sq.count(wt), "ed:", ed_sq.count(wt))
print("== P7 phrases: check P7 table phrases occur in articles (spot: meedoen etc.) ==")

print("== readers corner (P7) ==")
p7ts, _ = texts(os.path.join(ED, "p7-taal.svg"))
p7 = " ".join(p7ts)
for needle in ["Lucía (voorbeeldbrief van de redactie)",
               "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen",
               "Sin cartas reales ni mejores textos de la página 8 al cierre: publicamos este ejemplo; los prometemos para el VOL.3.",
               "Ejemplo de la redacción, no una carta real.",
               "¡Envíanos tu carta real y tu mejor texto! Los publicaremos en el VOL.3."]:
    print(("FOUND " if needle in p7 else "MISSING "), needle[:70])

print("== image credits present in edition ==")
for credit in ["Vovogov90", "Nationaal Archief", "W. Punt", "Spaarnestad Photo"]:
    print(credit, "core:", credit in core_all, "ed:", credit in ed_all)
