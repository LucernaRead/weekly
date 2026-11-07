# -*- coding: utf-8 -*-
import os, sys
BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-zh-tw-fr-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
texts = {f: open(os.path.join(BUILD, f), encoding="utf-8").read() for f in FILES}
R = [
 # head: fit 434px at 28pt
 ("讀懂了嗎? · Vous avez compris ?", "讀懂了嗎? · Tout compris ?", 5),
 # P7 col3 trims (one line each)
 ("Les crabes se pèsent en 両 (taels) ; 兩 est le « deux » de tous les jours, comme dans 兩隻蟹 (deux crabes).",
  "Les crabes se pèsent en 両 (taels) ; 兩 est le « deux » courant : 兩隻蟹, deux crabes.", 1),
 ("「先看警報，再決定出不出門。」 — la structure 先…再… donne l'ordre de deux actions : d'abord X, ensuite Y. Elle est faite pour la semaine du typhon : 先查公告，再改行程 (vérifiez d'abord les annonces, puis changez vos projets).",
  "「先看警報，再決定出不出門。」 — la structure 先…再… donne l'ordre de deux actions : d'abord X, ensuite Y. Faite pour la semaine du typhon : 先查公告，再改行程 (vérifiez les annonces, puis changez vos projets).", 1),
 ("Une lettre d'exemple de la rédaction — pas une vraie. Le VOL.2 publiera de vraies lettres de lecteurs et la meilleure rédaction de la page 8 !",
  "Lettre d'exemple de la rédaction — pas une vraie. Le VOL.2 publiera vos lettres et la meilleure rédaction de la page 8 !", 1),
 # P8-bound notes tightened to one printed line
 ("Vendredi et samedi : approche au plus près, temps le plus mauvais.", "Vendredi, samedi : approche maximale, pire temps.", 1),
 ("Ce sont les villes et les comtés qui annoncent les suspensions de travail et d'école.", "Les villes et comtés annoncent les suspensions.", 1),
 ("Le dernier jour de la vente du magasin de Zhonggang, à Taichung, est le dimanche 25 octobre.", "Dernier jour de vente à Zhonggang : dimanche 25 octobre.", 1),
 ("補假 — un jour de congé de compensation quand un jour férié tombe un week-end.", "補假 — jour de compensation (férié le week-end).", 1),
 ("疏運 — les transports supplémentaires organisés pour les départs en vacances.", "疏運 — transports supplémentaires des vacances.", 1),
 ("Les familles offrent un poulet entier et des gâteaux tortues rouges.", "Poulet entier et gâteaux tortues rouges offerts.", 1),
 ("Les gâteaux tortues rouges souhaitent une longue vie aux aînés.", "Gâteaux tortues rouges : longue vie aux aînés.", 1),
 ("薑茶 — un thé au gingembre après le crabe, pour réchauffer l'estomac.", "薑茶 — thé au gingembre après le crabe.", 1),
 ("Les Dragons sont champions de la première moitié de saison, meilleur bilan global.", "Dragons : champions de mi-saison, meilleur bilan.", 1),
 ("Les matchs suivants sont sautés dès qu'une équipe atteint quatre victoires.", "Matchs sautés dès qu'une équipe a quatre victoires.", 1),
 ("味全龍 — champions de la première moitié, meilleur bilan global.", "味全龍 — champions de mi-saison, meilleur bilan.", 1),
 ("La cérémonie commence à 19 h 00 ; le tapis rouge est à 17 h 00.", "Cérémonie à 19 h ; tapis rouge à 17 h.", 1),
 ("Le festival se tient sur le front de mer de Central et au parc Tamar.", "Au front de mer de Central et au parc Tamar.", 1),
 ("Les parcours de dégustation guidés sont nouveaux cette année.", "Nouveau cette année : les parcours guidés.", 1),
 ("Les vendredis et samedis soir durent maintenant jusqu'à 1 h du matin.", "Vendredi, samedi : ouvert jusqu'à 1 h du matin.", 1),
 ("尊尚品酒證 — 558 HK$, avec le pass du salon de dégustation premium.", "尊尚品酒證 — 558 HK$, salon premium inclus.", 1),
 ("Une alerte maritime vient d'abord, tant que le typhon est encore en mer.", "D'abord l'alerte maritime, typhon encore en mer.", 1),
 ("La circulation périphérique (外圍環流) du typhon apporte la pluie.", "外圍環流 : la circulation qui apporte la pluie.", 1),
 ("疏運 = des transports supplémentaires pour les départs en vacances.", "疏運 = transports en plus pour les vacances.", 1),
 ("討糖 est la façon taïwanaise de dire « des bonbons ou un sort ».", "討糖 — « des bonbons ou un sort » en taïwanais.", 1),
 ("Les coupons du festival sont des 品味券 (jetons de dégustation).", "品味券 : les jetons de dégustation du festival.", 1),
 ("Les prix des séries sont le samedi ; le vendredi, ce sont les programmes.", "Séries le samedi, programmes le vendredi.", 1),
 ("La vente du magasin de Tianmu commence le jeudi 22 octobre.", "La vente de Tianmu commence jeudi 22 octobre.", 1),
]
fails = []
for old, new, cnt in R:
    total = sum(texts[f].count(old) for f in FILES)
    if total != cnt:
        fails.append(f"{old[:50]!r}: got {total}, want {cnt}")
        continue
    for f in FILES:
        texts[f] = texts[f].replace(old, new)
if fails:
    print("FAIL"); [print(" -", x) for x in fails]; sys.exit(1)
for f in FILES:
    open(os.path.join(BUILD, f), "w", encoding="utf-8").write(texts[f])
print("TIGHTEN OK")
