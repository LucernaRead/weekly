# -*- coding: utf-8 -*-
import os, sys
BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-zh-tw-fr-build")
t = open(os.path.join(BUILD, "content7.py"), encoding="utf-8").read()
R = [
("La semaine du typhon remplit les journaux de mots de météo — apprenez les six que vous verrez le plus : 海上颱風警報 (alerte maritime), 陸上颱風警報 (alerte terrestre), 共伴效應 (effet conjoint), 外圍環流 (circulation périphérique), 豪雨 (pluie torrentielle), 停班停課 (travail et école suspendus).",
 "Semaine de typhon : les journaux parlent météo. Voici les six mots à connaître : 海上颱風警報 (alerte maritime), 陸上颱風警報 (alerte terrestre), 共伴效應 (effet conjoint), 外圍環流 (circulation périphérique), 豪雨 (pluie torrentielle), 停班停課 (travail et école suspendus)."),
("Six mots de météo font l'actualité de la semaine — apprenez-les une fois, lisez toute la semaine.",
 "Six mots de météo font l'actualité — apprenez-les, lisez toute la semaine."),
("Les alertes sont de deux sortes : d'abord une 海上警報 (alerte maritime), tant que le typhon est encore en mer ; puis une 陸上警報 (alerte terrestre) quand il approche des côtes. Une pluie plus forte que 大雨 est une 豪雨 (pluie torrentielle).",
 "Deux sortes d'alertes : la 海上警報 (maritime) d'abord, tant que le typhon est en mer ; puis la 陸上警報 (terrestre) près des côtes. Plus forte que 大雨 : la 豪雨 (pluie torrentielle)."),
("Entraînez-vous : « 明天會停班停課嗎？ » (« Le travail et l'école seront-ils suspendus demain ? ») — vérifiez l'annonce de votre ville.",
 "À vous : « 明天會停班停課嗎？ » (« Travail et école suspendus demain ? ») — vérifiez l'annonce de votre ville."),
("Les jours de cette semaine sont spéciaux. Groupez les mots et ils restent : les jours libres （連假、補假）, les voyages （疏運） et les plaisirs de fête （登高、討糖、星光大道）.",
 "Semaine spéciale : groupez les mots pour les retenir — jours libres （連假、補假）, voyages （疏運）, plaisirs de fête （登高、討糖、星光大道）."),
("連假 est une suite de jours libres d'affilée ; quand un jour férié tombe un week-end et qu'un jour de semaine est donné à la place, ce jour supplémentaire est un 補假 ; et les trains et bus supplémentaires mis en place pour emmener tout le monde et le ramener sont les 疏運.",
 "連假 : une suite de jours libres. Si un férié tombe un week-end, le jour donné en semaine est un 補假 ; les trains et bus en plus pour emmener tout le monde sont les 疏運."),
("Astuce mémoire : apprenez d'abord 連假, puis la foule qu'il déplace （疏運） et le jour supplémentaire qu'il ajoute （補假）.",
 "Astuce : apprenez 連假, puis la foule qu'il déplace （疏運） et son jour en plus （補假）."),
("Taïwan et Hong Kong ont chacun leur façon de dire les choses. À Taïwan, Threads est surnommé « 脆 » ; un bon billet se garde avec « 留友看 » — « le garder pour que les amis le voient » ; et un compliment noté en symboles zhuyin est un « ㄅ級分 ».",
 "Taïwan et Hong Kong ont leurs mots à eux. À Taïwan, Threads se surnomme « 脆 » ; un bon billet se garde par « 留友看 » (« pour que les amis le voient ») ; un compliment en zhuyin est un « ㄅ級分 »."),
("Trois inventions d'internet taïwanaises — toutes tirées d'un bilan PopDaily de mai 2026 des mèmes de l'année, pas de l'actualité de cette semaine.",
 "Trois inventions taïwanaises — tirées d'un bilan PopDaily (mai 2026) des mèmes de l'année, pas de l'actualité."),
("Pas besoin de beaucoup d'expressions locales — apprenez-en cinq et chaque conversation semble plus proche.",
 "Cinq expressions suffisent — les conversations deviennent plus proches."),
]
for old, new in R:
    assert t.count(old) == 1, old[:60]
    t = t.replace(old, new)
open(os.path.join(BUILD, "content7.py"), "w", encoding="utf-8").write(t)
print("P7 TRIMS OK")
