# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhtw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Focus langue", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Trois niveaux, trois sujets")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Mots de la météo", 24)
a.para("La semaine du typhon remplit les journaux de mots de météo. Les six à connaître : 海上颱風警報 (alerte maritime), 陸上颱風警報 (alerte terrestre), 共伴效應 (effet conjoint), 外圍環流 (circulation périphérique), 豪雨 (pluie torrentielle), 停班停課 (travail et école suspendus).", 21.5)
a.glossline("Six mots de météo, à apprendre une fois pour toute la semaine.")
a.para("Deux sortes d'alertes : d'abord la 海上警報 (alerte maritime), tant que le typhon est en mer ; puis la 陸上警報 (alerte terrestre) quand il approche des côtes. Plus fort que 大雨 : la 豪雨 (pluie torrentielle).", 21.5)
a.ex("A2", "完成句子", "海上", "Une alerte maritime vient d'abord, tant que le typhon est encore en mer.",
     "颱風還在海上,先發佈___颱風警報。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "單選", "A", "停班停課 signifie : ni travail ni école.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "豪雨 (háo) est plus forte que 大雨.",
     "比大雨還大的雨,叫___雨。", instr="Complétez", size=20.5, gap=10)
a.ex("A2", "單選", "A", "La circulation périphérique (外圍環流) du typhon apporte la pluie.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("Entraînez-vous : « 明天會停班停課嗎？ » (« Travail et école suspendus demain ? ») — vérifiez l'annonce de votre ville.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Jours et fêtes", 24)
b.para("Semaine spéciale : groupez les mots pour les retenir — les jours libres （連假、補假）, les voyages （疏運）, les plaisirs de fête （登高、討糖、星光大道）.", 21.5)
b.glossline("Groupez les mots : jours libres (連假/補假), voyages (疏運), plaisirs de fête (登高/討糖/星光大道).")
b.para("連假 : une suite de jours libres d'affilée. Quand un jour férié tombe un week-end, le jour de semaine donné à la place est un 補假. Les trains et bus ajoutés pour les départs et retours : les 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "Un jour libre de compensation : 補假.",
     "假日逢週日,週一多放一天,叫___。", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "單選", "A", "疏運 = des transports supplémentaires pour les départs en vacances.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "討糖 est la façon taïwanaise de dire « des bonbons ou un sort ».",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Complétez", size=20.5, gap=10)
b.ex("B1", "單選", "A", "La partie tapis rouge d'une soirée de prix est la 星光大道.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Astuce : apprenez 連假 d'abord, puis la foule déplacée （疏運） et le jour ajouté （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Parler local", 24)
c.para("Taïwan et Hong Kong ont leurs mots bien à eux. À Taïwan, Threads est surnommé « 脆 » ; un bon billet se garde avec « 留友看 » (« pour que les amis le voient ») ; un compliment en symboles zhuyin est un « ㄅ級分 ».", 21.5)
c.glossline("Trois inventions d'internet taïwanaises — toutes tirées d'un bilan PopDaily de mai 2026 des mèmes de l'année, pas de l'actualité de cette semaine.")
c.para("À Hong Kong : Halloween = « 哈囉喂 » ; la fondue chinoise, « 打邊爐 » ; bon et pas cher, « 抵食 » ; les crabes se pèsent en « 両 » ; les jetons du festival sont des « 品味券 ».", 21.5)
c.ex("B2", "單選", "A", "À Taïwan, Threads est surnommé 脆 (croustillant).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "留友看 — le garder pour que les amis le lisent aussi.",
     "看到好文,先存起來「___看」。", instr="Complétez", size=20.5, gap=10)
c.ex("B2", "單選", "A", "哈囉喂 est l'Halloween de Hong Kong.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "Les coupons du festival sont des 品味券 (jetons de dégustation).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Complétez", size=20.5, gap=10)
c.para("Pas besoin de beaucoup d'expressions locales — apprenez-en cinq et chaque conversation semble plus proche.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taïwan écrit 颱風 ; 台風 est l'orthographe en kanji japonais."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "Les crabes se pèsent en 両 (taels) ; 兩 est le « deux » ordinaire, comme dans 兩隻蟹 (deux crabes)."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) marque la manière, avant le verbe."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = demander un congé soi-même ; 放假 = être en congé officiel."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Clinique des erreurs", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看警報，再決定出不出門。」 — 先…再… ordonne deux actions : d'abord X, ensuite Y. Pour la semaine du typhon : 先查公告，再改行程 (d'abord les annonces, puis vos projets)."
wcn = "À vous : écrivez votre propre phrase en 先…再…."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · La phrase-modèle", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "Lettre d'exemple de la rédaction. Le VOL.2 publiera vos vraies lettres et la meilleure rédaction de la page 8 !"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Le coin des lecteurs", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Phrases de la semaine — mot pour mot tirées des articles de ce numéro", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "La trajectoire peut encore changer ; personne ne sait encore s'il touchera terre.", "p. 1"),
    ("「請四天假,換九天連假」", "Quatre jours de congé, neuf jours de repos.", "p. 2"),
    ("「登高望遠,人也精神了」", "Monter haut, regarder loin — et se sentir revigoré.", "p. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Femelles au 9e mois lunaire, mâles au 10e.", "p. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "La première équipe à quatre victoires est la championne de l'année.", "p. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "Le typhon a changé la date, pas l'envie de faire la fête.", "p. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "Plus de 340 stands déplacent le monde au bord du port.", "p. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "Les vendredis et samedis soir durent jusqu'à 1 h du matin pour la première fois.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 146
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 146 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · La semaine prochaine (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
