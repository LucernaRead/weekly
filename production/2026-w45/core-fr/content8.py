# -*- coding: utf-8 -*-
"""W45 FR core VOL.3 — P8 (battery 42 + writing + all keys from REG)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-core/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCICES & RÉPONSES · 练习与答案", "Le Lucerna", "综合评估 ÉVALUATION · 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze ----
cloze_defs = [
    ("A2", "C", "11 月 8 日 2026 是星期日"),
    ("A2", "A", "去南泰尔看决赛"),
    ("A2", "B", "决赛选手周六晚才揭晓"),
    ("A2", "B", "品尝语境（un régal）→ goûté"),
    ("B1", "C", "se promener 漫步"),
    ("B1", "A", "avoir + 过去分词 goûté（不配合）"),
    ("B1", "C", "les finales 主语复数 → ont lieu"),
    ("A2", "A", "elle écrit 她写"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · TEXTE À TROUS · 完形填空", 24)
bf.para(f"Léa a seize ans. Le ({cnums[0]})___ 8 novembre, elle se lève tôt : c'est le jour des finales. Avec son frère, elle va à ({cnums[1]})___ pour voir le tennis. « On ne connaît pas encore les ({cnums[2]})___ », dit son frère. Le soir, Léa raconte : « À Port-en-Bessin, on a ({cnums[3]})___ des coquilles, un régal ! » Le festival ({cnums[4]})___ dans Paris. Léa a ({cnums[5]})___ la musique. Les finales ({cnums[6]})___ dimanche, et elle l'({cnums[7]})___ dans son cahier.", 21)
bf.bridge("选项：")
for n, opts in zip(cnums, [
    "A. lundi · B. samedi · C. dimanche",
    "A. Nanterre · B. Plailly · C. Dieppe",
    "A. vainqueurs · B. finalistes · C. spectateurs",
    "A. acheté · B. goûté · C. vendu",
    "A. promène · B. promènent · C. se promène",
    "A. goûté · B. goûtée · C. goûter",
    "A. a lieu · B. ont lieus · C. ont lieu",
    "A. écrit · B. écrivent · C. écris",
]):
    bf.para(f"{n}. {opts}", 19.5, "sans", False, INK, 1.32, 2)

# ---- B. single choice ----
bf.head("B · CHOIX MULTIPLE · 单选", 24)
mcq = [
    ("A2", "B", "7 nov. = samedi（最后夜场）", "La dernière nocturne a lieu... A. vendredi 6 · B. samedi 7 · C. dimanche 8"),
    ("A2", "A", "nous → allons", "Lundi, nous ___ reprendre les cours. A. allons · B. allez · C. vont"),
    ("B1", "B", "s'intéresser aux（à+les）", "Elle s'intéresse ___ festivals. A. à les · B. aux · C. des"),
    ("B2", "B", "si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音", "Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais"),
    ("B2", "A", "主语 ce programme 三单 → semble", "À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant"),
    ("B1", "B", "将来时 aura lieu（决赛在周日）", "Dimanche, la finale ___ à Nanterre. A. a lieu · B. aura lieu · C. avait lieu"),
    ("A2", "A", "三区同日复课", "Les trois zones reprennent... A. le même jour · B. à des jours différents · C. en décembre"),
    ("B1", "C", "扇贝节在 11 月 7–8 日", "Le Goût du Large, c'est... A. 14–15 nov. · B. 31 oct. · C. 7–8 nov."),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20)

# ---- C. reading ----
bf.head("C · LECTURE · 阅读理解", 24)
bf.para("Samedi soir, la famille Martin prépare son week-end. Samedi 7 novembre, ils iront à Plailly pour la dernière nocturne : de 19 heures à 1 heure du matin, avec un badge repousse-monstres pour le petit Léo. Dimanche 8, ils regarderont les finales à la télévision, puis ils goûteront des coquilles de Port-en-Bessin. « Trois finales en un week-end ! » dit Monsieur Martin. Le soir, Léo dormira tôt : demain, c'est l'école.", 21)
read_qs = [
    ("A2", "C", "夜场 19 点至凌晨 1 点", "La nocturne dure de... A. 10 h à 19 h · B. 18 h à 20 h · C. 19 h à 1 h"),
    ("A2", "A", "小徽章给小 Léo 驱怪", "Le badge repousse-monstres, c'est pour... A. le petit Léo · B. le père · C. la mère"),
    ("B1", "B", "周日先看决赛再吃扇贝", "Dimanche, la famille... A. va à Plailly · B. regarde les finales puis goûte des coquilles · C. reste au lit"),
    ("B1", "A", "周日晚上早睡因为周一上学", "Dimanche soir, Léo dort tôt parce que... A. demain, c'est l'école · B. il est malade · C. il pleut"),
    ("B2", "A", "周一是上学日（复课后正常周一）", "Lundi, Léo... A. retourne à l'école · B. reste en vacances · C. va à Plailly"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20)

# ---- D. sentence building ----
bf.head("D · PHRASES · 完成句子与转换", 24)
d_items = [
    ("A2", "Les élèves vont reprendre les cours lundi.", "aller + 原形（futur proche）",
     "Futur proche : « Les élèves reprennent les cours lundi. » → ___"),
    ("B2", "Si tu venais samedi, tu verrais la nocturne.", "si + 半过去时 venais",
     "Hypothèse : « Si tu (venir) samedi, tu verrais la nocturne. »"),
    ("B1", "Elle a goûté les coquilles à Port-en-Bessin.", "passé composé : a + 过去分词",
     "Passé composé : « Elle (goûter) les coquilles à Port-en-Bessin. »"),
    ("B2", "Selon moi, les finales sont excitantes.", "selon moi = 在我看来",
     "Opinion : « ___ moi, les finales sont excitantes. »"),
    ("B1", "Il est prévu que le Sénat examine le texte lundi.", "il est prévu que + 虚拟式",
     "Subjonctif : « Il est prévu que le Sénat (examiner) le texte lundi. » → ___"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20)

# ---- E. translation ----
bf.head("E · TRADUCTION · 翻译", 24)
e_items = [
    ("B2", "读一份日程，本身就是在了解法国。", "lire un programme = 读日程",
     "Traduisez : « Lire un programme, c'est déjà comprendre la France. »"),
    ("A2", "Il court plus vite que son frère.", "比较级 plus vite + court",
     "Traduisez : 他跑得比他哥哥更快。"),
    ("B1", "Les élèves sont en vacances depuis le 17 octobre.", "être en vacances + depuis",
     "Traduisez : 学生们自 10 月 17 日起就在放假。"),
    ("B1", "Ce soir, nous allons préparer nos cartables.", "futur proche + préparer",
     "Traduisez : 今晚，我们要准备书包。"),
    ("B2", "On ne connaît pas encore les finalistes.", "ne...pas encore = 尚未",
     "Traduisez : 人们尚不知道决赛选手是谁。"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20)

# ---- F. matching ----
bf.head("F · LES MOTS · 词汇配对", 24)
bf.match_set("B1", "词汇配对",
             ["un tournoi", "une nocturne", "un budget", "une coquille", "un festival"],
             ["une compétition avec plusieurs matchs", "une soirée qui dure jusqu'à la nuit",
              "le plan des dépenses de l'État", "le coquillage fêté à Port-en-Bessin",
              "plusieurs concerts en une semaine"],
             ["a", "b", "c", "d", "e"],
             ["tournoi=赛事 a", "nocturne=夜场 b", "budget=预算 c", "coquille=扇贝 d", "festival=音乐节 e"],
             instr="配对")

# ---- G. dialogue ----
dlg_defs = [
    ("A2", "samedi", "11 月 7 日是星期六"),
    ("A2", "coquilles (des coquilles Saint-Jacques)", "在市场买扇贝"),
    ("B1", "goûter", "goûter 品尝（原形）"),
    ("A2", "recette", "à la portaise 是一种做法"),
    ("A2", "week-end", "Bon week-end ! 周末愉快"),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G · DIALOGUE · 对话补全", 24)
bf.para(f"— Bonjour madame, c'est le marché du Goût du Large ? — Oui ! — Pour ({gnums[0]})___, le 7 novembre : je veux des ({gnums[1]})___ pour ma famille. — Goûtez celle-ci ! Vous voulez les ({gnums[2]})___ à la portaise ? — Oui, donnez-moi votre ({gnums[3]})___. — Voilà. Bon ({gnums[4]})___ ! — Merci !", 21)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · ÉCRITURE · 写作", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mon week-end du 7–8 novembre ». Racontez : un match, une fête, un plat. Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 288, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MODÈLE · 范文", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Samedi 7 novembre, j'ai regardé les demi-finales du Masters à la télévision : quelle ambiance ! Le soir, nous avons fêté la dernière nocturne avec des amis, déguisés en fantômes. Dimanche 8, nous avons goûté des coquilles Saint-Jacques à la portaise, achetées au marché de Port-en-Bessin. Le matin, nous avons marché au bord de la mer et nous avons acheté des fleurs pour ma grand-mère. Le soir, nous avons écouté de la musique et j'ai lu vingt pages de mon roman français. C'était un week-end parfait.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "RÉPONSES · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):
            s += f"（{e['note']}）"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
