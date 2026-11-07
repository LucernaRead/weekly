import sys, os, re
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zh-tw-fr-build"))
from svglib import wrap, text_w, _fw
def check(label, text, max_w=398):
    lines = wrap(text, "sans", False, 20.5, max_w)
    t = _fw(text); words = set(t.split(" "))
    splits = []
    for i in range(len(lines)-1):
        a = lines[i].split(" ")[-1]; b = lines[i+1].split(" ")[0]
        balpha = re.match(r"[A-Za-zÀ-ÿ]+", b)
        if a and balpha and a[-1].isalpha() and (a + balpha.group(0)) in words:
            splits.append((i, a, b))
    print(f"--- {label}: {len(lines)} lines, splits={splits}, maxw={max(text_w(l,'sans',False,20.5) for l in lines):.1f}")
    for ln in lines: print(f"  [{text_w(ln,'sans',False,20.5):6.1f}] {ln!r}")
P = "Note — "
base = "Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de remerciement de deux jours pour les supporters se tient les 21-22 nov. à Tianmu : concert sur l'herbe et camping la nuit du 21, activités avec les joueurs le 22. "
V5 = base + "Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
V6 = base + "La ville de Taipei double les points U-Sport en novembre : 10 points par visite au lieu de 5, dans 267 lieux."
V7 = base + "La ville de Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
for lbl, v in [("V5 se tient + Taipei", V5), ("V6 se tient + en novembre", V6), ("V7 se tient only (=V1)", V7)]:
    check(lbl, P + v)
