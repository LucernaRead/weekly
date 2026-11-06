# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案 · Test et corrigés", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · Le test de la semaine et toutes les réponses")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判斷對錯 · Vrai ou faux", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "Le Double Neuf est le 9/9 lunaire.",
     "重陽節在農曆九月初九。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Le jour férié de Hong Kong était le lundi 19 octobre, pas le 20.",
     "香港重陽節翌日假期在10月20日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "A", "Vendredi et samedi sont les jours d'approche au plus près.",
     "颱風薔琵週五、週六最接近台灣。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Les Dragons ont gagné le match 1, 3 à 0 — pas les Brothers.",
     "台灣大賽第一戰,中信兄弟3比0贏味全龍。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Séries le samedi, programmes le vendredi.",
     "金鐘獎戲劇類在週五頒獎。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "400 - 258 = 142 économisés avec le pass dégustation.",
     "品味證比逐樣買便宜142港幣。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B · 本週大測驗 · Le grand quiz", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "L'alerte maritime pourrait être émise mercredi soir.",
     "海上颱風警報最快哪晚發佈? A. 週一 · B. 週三 · C. 週五", size=13.8, gap=0)
f.ex("A2", "單選", "B", "Prenez 4 jours de congé, obtenez 9 jours de repos.",
     "「請4放9」一共放幾天? A. 4天 · B. 9天 · C. 13天", size=13.8, gap=0)
f.ex("A2", "單選", "A", "Les femelles (蟹乸) sont au mieux au 9e mois lunaire.",
     "農曆九月先吃什麼蟹? A. 蟹乸 · B. 蟹公 · C. 蟹仔", size=13.8, gap=0)
f.ex("A2", "單選", "B", "La vente de Tianmu commence jeudi 22 octobre.",
     "天母店週年慶哪天開跑? A. 週二 · B. 週四 · C. 週六", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Au meilleur des sept : la première équipe à 4 victoires.",
     "台灣大賽要先贏幾場才封王? A. 3場 · B. 4場 · C. 7場", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Le résultat est annoncé lors de la cérémonie du samedi.",
     "人氣獎結果何時公佈? A. 投票截止時 · B. 週六典禮當晚 · C. 週日早上", size=13.8, gap=0)
f.ex("B1", "單選", "C", "Plus de 340 stands participent.",
     "美酒佳餚巡禮有幾個攤位? A. 約140個 · B. 約240個 · C. 逾340個", size=13.8, gap=0)
f.ex("B1", "單選", "B", "La Ville d'Halloween de Taoyuan ouvre le samedi 24 octobre.",
     "桃園萬聖城哪天開城? A. 10月23日 · B. 10月24日 · C. 10月25日", size=13.8, gap=0)
f.ex("B2", "單選", "B", "Le pass premium regroupe 900 HK$ d'articles.",
     "尊尚品酒證的內容總值是? A. 558港幣 · B. 900港幣 · C. 400港幣", size=13.8, gap=0)
f.ex("B2", "單選", "A", "脆 est le surnom taïwanais de Threads.",
     "哪個說法對? A. 「脆」是台灣對 Threads 的暱稱 · B. 「脆」是一種餅乾 · C. 「脆」是香港用法", size=13.8, gap=0)
f.head("C · 完成句子 · Complétez les phrases", 21, OLIVE, 5)
f.ex("A2", "完成句子", "共伴", "Typhon plus mousson : l'effet conjoint.",
     "颱風加東北季風,叫___效應。", instr="Complétez", size=13.8, gap=0)
f.ex("A2", "完成句子", "登高", "Monter en hauteur est la coutume du Double Neuf.",
     "重陽節爬山,叫作___。", instr="Complétez", size=13.8, gap=0)
f.ex("A2", "完成句子", "疏運", "疏運 — l'opération de transport des vacances.",
     "連假人多,台鐵、高鐵加開班次,這叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("A2", "完成句子", "送百", "1 000 dépensés, 100 offerts : 滿千送百.",
     "每滿一千送一百,叫滿千___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "完封", "Un blanchissage : l'autre équipe marque zéro.",
     "棒球比賽對手得0分,叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "星光", "Le tapis rouge est la 星光大道.",
     "頒獎典禮走紅毯的部分,叫___大道。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "哈囉", "哈囉喂 — l'Halloween de Hong Kong.",
     "海洋公園的萬聖節,香港人叫___喂。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "12", "Un crabe de 3 taels cuit environ 12 minutes.",
     "蒸一隻3両的大閘蟹,約___分鐘。", instr="Complétez", size=13.8, gap=0)
f.ex("B2", "完成句子", "品味", "Les coupons sont des 品味券 (jetons de dégustation).",
     "美酒佳餚巡禮的券,叫___券。", instr="Complétez", size=13.8, gap=0)
f.ex("B2", "完成句子", "留友", "留友看 — le garder pour que les amis le lisent.",
     "看到好文存起來給朋友,叫「___看」。", instr="Complétez", size=13.8, gap=0)
f.head("D · 讀一讀,答一答 · Lisez et répondez", 21, OLIVE, 5)
f.para("阿哲住在台北。光復節連假,他週六晚上在家看台灣大賽第六戰(如果有需要)。週日晚上七點,他去天母看百鬼夜行踩街,還拿到一個南瓜桶。週一是補假,他睡到自然醒,下午去信義新天地逛週年慶,買了一雙鞋:2,600元,滿千送百,他拿到200元回饋券。三天連假,他過得很開心。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Il regarde la Série de Taïwan le samedi soir.",
     "阿哲週六晚上看什麼? A. 金鐘獎 · B. 台灣大賽 · C. 電影", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Le défilé est à 19 h 00 le dimanche.",
     "踩街在週日幾點? A. 17:00 · B. 19:00 · C. 21:00", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Il fait ses achats à Xinyi le lundi férié.",
     "他週一去哪裡逛週年慶? A. 天母店 · B. 信義新天地 · C. 台中中港店", size=13.8, gap=0)
f.ex("B1", "單選", "B", "2 600 = deux milliers pleins, donc 2 x 100 = 200 offerts.",
     "鞋子2,600元,他拿到多少回饋券? A. 100元 · B. 200元 · C. 260元", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Ordre : le baseball, puis le défilé, puis les achats.",
     "這三天他的順序是? A. 先看球,再踩街,再逛街 · B. 先逛街,再看球 · C. 先踩街,再逛街,再看球", size=13.8, gap=0)
f.head("E · 情景說話 · En situation", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "Vérifiez l'alerte avant de sortir pendant un typhon.",
     "— 明天會下雨嗎? — 颱風來了,先看___再出門。(A. 警報 · B. 菜單)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "2 000 = deux milliers, donc 200 en bons.",
     "— 這件外套多少錢? — 2,000元,滿千送百,可以拿___元券。 A. 100 · B. 200", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Monter (登高) est l'activité du Double Neuf.",
     "— 你重陽節做什麼? — 我去___,還吃了紅龜粿。(A. 登高 · B. 討糖)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Le match 4 a lieu le mercredi 21 octobre.",
     "— G4 是哪天? — 週___,10月21日。(A. 二 · B. 三)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Les résultats arrivent à la cérémonie du samedi.",
     "— 人氣獎結果何時知道? — 週六___公佈。(A. 典禮當晚 · B. 下週一)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "留友看 — garder le billet pour les amis.",
     "— 這篇文不錯。 — 我先存起來,___看。(A. 留友 · B. 哈囉)", size=13.8, gap=0)
f.head("F · 寫一寫 · À vos plumes", 21, OLIVE, 5)
MODELO = ("光復節連假有三天。第一天,我在家看台灣大賽,如果打到第六戰,我一定準時打開電視。"
          "第二天晚上七點,我去天母看百鬼夜行,順便討糖。"
          "第三天是補假,我想睡晚一點,下午去信義新天地逛週年慶。"
          "下週四美酒佳餚巡禮開幕,我先買了兩張品味證,一共516元,準備帶媽媽去中環看海、吃好料。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Écriture — il n'y a pas de réponse unique. Un modèle de {NCHARS} caractères suit.")
f.ex("B2", "寫作", "(question ouverte — texte modèle ci-dessous)", f"Question ouverte — le texte modèle est imprimé dans la section F ci-dessus ({NCHARS} caractères)",
     "寫一寫《我的連假計畫》:三天連假你想做什麼?哪天看什麼活動?要買什麼票?寫 120~180 字。", instr="Écrivez", size=13.8, gap=0)
f.para("Texte modèle : " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Réponses — dans l'ordre des pages, avec une courte note en français pour chaque exercice", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Toutes les notes en français · ✓ = le texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Page {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
