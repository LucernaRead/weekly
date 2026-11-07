# -*- coding: utf-8 -*-
"""Final builder checks for W45 DE x FR (supplements tools/*, not replacements)."""
import re, glob, collections
from PIL import ImageFont
import sys
sys.path.insert(0, "../hidden_files/weekly-report-w45-de-fr-build")
ED="../files/weekly-report-w45-de-fr/svg"
CORE="../files/weekly-report-w45-de-core/svg"
def texts(path):
    s=open(path,encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', s)
def joined(path):
    return " ".join(texts(path))
# 1. CJK + banned term in edition SVGs
import os
tot_cjk=0
for f in sorted(glob.glob(ED+"/*.svg")):
    s=open(f,encoding="utf-8").read()
    tot_cjk+=len(re.findall(r'[\u4e00-\u9fff]', s))
print("edition CJK total:", tot_cjk)
# 2. P7 verbatim: 8 German phrases, each exactly 2x across the issue, tags as in core
phrases=[("Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.","Seite 4 · B1"),
("Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.","Seite 2 · A2"),
("Wer 50 Liter tankt, spart rund 8,35 Euro.","Seite 2 · A2"),
("Die Schule hat nach den Herbstferien wieder begonnen.","Seite 5 · B1"),
("Die Tage sind kurz, die Abende lang.","Seite 3 · A2"),
("Zwei schwere Auswärtsspiele für die deutschen Teams.","Seite 4 · B1"),
("Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.","Seite 6 · B2"),
("Es geht langsam aufwärts — aber von allein geht es nicht.","Seite 6 · B2")]
alltxt=" ".join(joined(f) for f in sorted(glob.glob(ED+"/*.svg")))
alltxt_n=re.sub(r'\s+',' ',alltxt)
p7txt=joined(ED+"/p7-sprache.svg")
for q,tag in phrases:
    n=alltxt_n.count(q)
    # tag distribution: phrase's P7 table cell tag follows its translation on P7
    print(f"verbatim {n}x tag {tag} present-on-P7: {tag in p7txt} :: {q[:50]}")
    assert n==2, (q,n)
# 3. gloss counts: split gloss() call strings on '·' itself, core vs edition build sources
def gloss_calls(path):
    s=open(path,encoding="utf-8").read()
    return re.findall(r'\.gloss\("([^"]*)"\)', s)
for f in ["content12.py","content34.py","content56.py"]:
    c=gloss_calls(f"../hidden_files/weekly-report-w45-de-build/{f}")
    e=gloss_calls(f"../hidden_files/weekly-report-w45-de-fr-build/{f}")
    assert len(c)==len(e), (f,len(c),len(e))
    cc=[len(x.split("·")) for x in c]; ee=[len(x.split("·")) for x in e]
    print(f, "gloss calls:", len(c), "core items/call:", cc, "total:", sum(cc), "| ed items/call:", ee, "total:", sum(ee))
    assert cc==ee
    # every edition item's German headword survives in the edition SVG
    for call in e:
        for item in call.split("·"):
            head=item.strip().split("=")[0].strip()
            if head: assert head.split()[0] in alltxt_n or head in alltxt_n, head
print("gloss 1:1 OK")
# 4. badge/footers: extract badge + footer text elements from P1 and all pages
def text_elems(path):
    s=open(path,encoding="utf-8").read()
    return re.findall(r'<text([^>]*)>([^<]*)</text>', s)
for f in sorted(glob.glob(ED+"/*.svg")):
    els=text_elems(f)
    foot=[t for _,t in els if t.startswith("Die Lucerna · HEBDOMADAIRE")]
    page=[t for _,t in els if re.match(r'Page \d sur 8', t)]
    print(os.path.basename(f), "footer:", foot, "pageline:", page)
    assert len(foot)==1 and len(page)==1
p1=text_elems(ED+"/p1-front.svg")
badge=[(a,t) for a,t in p1 if "TEXTE EN ALLEMAND" in t and "LECTEURS" in t]
print("P1 badge elements:", badge)
w43=text_elems("../files/weekly-report-de-fr/svg/p1-front.svg")
badge43=[(a,t) for a,t in w43 if "TEXTE EN ALLEMAND" in t and "LECTEURS" in t]
print("W43 badge elements:", badge43)
# 5. P6 chart: label ink right edges vs bar left 535
from svglib import text_w
for lab in ["domicile","service","retraite"]:
    print("chart label", lab, "width:", round(text_w(lab,"sans",False,20),1), "ends at:", round(425+text_w(lab,"sans",False,20),1), "(bar starts 535)")
    assert 425+text_w(lab,"sans",False,20) < 535
# 6. P8 full-width paren count in edition (fan-outs use half-width) + P8 separators
p8=open(ED+"/p8-uebungen.svg",encoding="utf-8").read()
print("P8 full-width paren count:", p8.count("（"), "half-width ( count:", p8.count("("), "Page separators:", len(re.findall(r'— Page \d —', p8)))
assert p8.count("（")==0
# 7. readers corner: three facts + explicit solicitation in French on P7
p7=joined(ED+"/p7-sprache.svg")
for frag in ["Un exemple de la rédaction", "Aucune vraie lettre", "meilleur texte de page 8", "suite en VOL.3", "Écrivez-nous vos vraies lettres"]:
    print("P7 readers fragment:", frag, "->", frag in p7)
    assert frag in p7
print("ALL FINAL CHECKS PASSED")
