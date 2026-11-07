import sys, os, re
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zh-tw-fr-build"))
from svglib import wrap, text_w, _fw
def check(label, text, max_w=398):
    lines = wrap(text, "sans", False, 20.5, max_w)
    # split detection: line ends with letter, next starts with letter, and
    # last-frag + first-token-alpha forms a word present in the _fw text
    t = _fw(text); words = set(t.split(" "))
    splits = []
    for i in range(len(lines)-1):
        a = lines[i].split(" ")[-1]; b = lines[i+1].split(" ")[0]
        balpha = re.match(r"[A-Za-zÀ-ÿ]+", b)
        if a and balpha and a[-1].isalpha() and (a + balpha.group(0)) in words:
            splits.append((i, a, b))
    print(f"--- {label}: {len(lines)} lines, splits={splits}, maxw={max(text_w(l,'sans',False,20.5) for l in lines):.1f}")
    for ln in lines: print(f"  [{text_w(ln,'sans',False,20.5):6.1f}] {ln!r}")
    return splits
P = "Note — "
V1 = "Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de remerciement de deux jours pour les supporters se tient les 21-22 nov. à Tianmu : concert sur l'herbe et camping la nuit du 21, activités avec les joueurs le 22. La ville de Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
V2 = "Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de remerciement de deux jours pour les supporters a lieu les 21-22 nov. à Tianmu : concert sur l'herbe et camping la nuit du 21, activités avec les joueurs le 22. Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
V3 = "Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de remerciement de deux jours pour les supporters a lieu les 21-22 nov. à Tianmu : concert sur l'herbe et camping la nuit du 21, animations avec les joueurs le 22. La ville de Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
V4 = "Le défilé du titre des Wei Chuan Dragons est prévu dimanche prochain (22 nov.) à 14h00, du stade de baseball de Tianmu au Taipei Dome. Un festival de remerciement pour les supporters a lieu les 21-22 nov. à Tianmu : concert sur l'herbe et camping la nuit du 21, activités avec les joueurs le 22. La ville de Taipei double les points U-Sport tout le mois de novembre : 10 points par visite au lieu de 5, dans 267 lieux."
for lbl, v in [("V1 se tient", V1), ("V2 Taipei", V2), ("V3 animations", V3), ("V4 sans deux jours", V4)]:
    check(lbl, P + v)
