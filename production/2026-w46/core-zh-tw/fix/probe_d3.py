import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zh-tw-fr-build"))
from svglib import wrap, text_w
GLOSS = "Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de remerciement de deux jours pour les supporters a lieu les 21-22 nov. à Tianmu : concert sur l'herbe et camping la nuit du 21, activités avec les joueurs le 22. La ville de Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
def check(label, text, max_w=398):
    lines = wrap(text, "sans", False, 20.5, max_w)
    words = set(text.split(" "))
    splits = []
    for i in range(len(lines)-1):
        a = lines[i].split(" ")[-1]; b = lines[i+1].split(" ")[0]
        if a and b and (a+b) in words and a not in words:
            splits.append((i, a, b, a+b))
    print(f"--- {label}: {len(lines)} lines, splits={splits}")
    for ln in lines:
        print(f"  [{text_w(ln,'sans',False,20.5):6.1f}] {ln!r}")
    return lines, splits
check("CURRENT", "Note — " + GLOSS)
