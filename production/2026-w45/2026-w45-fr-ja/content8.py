# -*- coding: utf-8 -*-
"""W45 FR core VOL.2 — P8 (battery 42 + writing + all keys from REG)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("EXERCICES & RÉPONSES　練習と答え", "Le Lucerna", "総合テスト ÉVALUATION　答えはこのページの下にあります")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1485, tag="P8-battery")

# ---- A. cloze ----
cloze_defs = [
    ("A2", "C", "2026年11月8日は日曜日"),
    ("A2", "A", "ナンテールへ決勝を見に行く"),
    ("A2", "B", "決勝進出者は土曜夜に判明"),
    ("A2", "B", "試食の文脈（un régal）→ goûté"),
    ("B1", "C", "se promener 散歩する"),
    ("B1", "A", "avoir + 過去分詞 goûté（一致なし）"),
    ("B1", "C", "les finales は複数主語 → ont lieu"),
    ("A2", "A", "elle écrit 彼女は書く"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　TEXTE À TROUS　穴埋め", 24)
bf.para(f"Léa a seize ans. Le ({cnums[0]})___ 8 novembre, elle se lève tôt : c'est le jour des finales. Avec son frère, elle va à ({cnums[1]})___ pour voir le tennis. « On ne connaît pas encore les ({cnums[2]})___ », dit son frère. Le soir, Léa raconte : « À Port-en-Bessin, on a ({cnums[3]})___ des coquilles, un régal ! » Le festival ({cnums[4]})___ dans Paris. Léa a ({cnums[5]})___ la musique. Les finales ({cnums[6]})___ dimanche, et elle l'({cnums[7]})___ dans son cahier.", 21)
bf.bridge("選択肢：")
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
bf.head("B　CHOIX MULTIPLE　選択問題", 24)
mcq = [
    ("A2", "B", "7 nov. = samedi（最終ナイトイベント）", "La dernière nocturne a lieu... A. vendredi 6 · B. samedi 7 · C. dimanche 8"),
    ("A2", "A", "nous → allons", "Lundi, nous ___ reprendre les cours. A. allons · B. allez · C. vont"),
    ("B1", "B", "s'intéresser aux (à + les)", "Elle s'intéresse ___ festivals. A. à les · B. aux · C. des"),
    ("B2", "B", "si + imparfait → conditionnel présent；j' は母音の前での je のエリジオン", "Si j'étais libre dimanche, j'___ à Nanterre. A. irai · B. irais · C. vais"),
    ("B2", "A", "主語 ce programme は三人称単数 → semble", "À mon avis, ce programme ___ très riche. A. semble · B. sembler · C. semblant"),
    ("B1", "B", "将来時 aura lieu（決勝は日曜日）", "Dimanche, la finale ___ à Nanterre. A. a lieu · B. aura lieu · C. avait lieu"),
    ("A2", "A", "3つの学区が同じ月曜日に再開", "Les trois zones reprennent... A. le même jour · B. à des jours différents · C. en décembre"),
    ("B1", "C", "ホタテ祭りは11月7〜8日", "Le Goût du Large, c'est... A. 14–15 nov. · B. 31 oct. · C. 7–8 nov."),
]
for lv, k, nt, body in mcq:
    bf.ex(lv, "单选", k, nt, body, size=20)

# ---- C. reading ----
bf.head("C　LECTURE　読解", 24)
bf.para("Samedi soir, la famille Martin prépare son week-end. Samedi 7 novembre, ils iront à Plailly pour la dernière nocturne : de 19 heures à 1 heure du matin, avec un badge repousse-monstres pour le petit Léo. Dimanche 8, ils regarderont les finales à la télévision, puis ils goûteront des coquilles de Port-en-Bessin. « Trois finales en un week-end ! » dit Monsieur Martin. Le soir, Léo dormira tôt : demain, c'est l'école.", 21)
read_qs = [
    ("A2", "C", "ナイトイベントは19時から深夜1時まで", "La nocturne dure de... A. 10 h à 19 h · B. 18 h à 20 h · C. 19 h à 1 h"),
    ("A2", "A", "小さなバッジは小さな Léo の怪物よけ", "Le badge repousse-monstres, c'est pour... A. le petit Léo · B. le père · C. la mère"),
    ("B1", "B", "日曜はまず決勝を見てからホタテを味わう", "Dimanche, la famille... A. va à Plailly · B. regarde les finales puis goûte des coquilles · C. reste au lit"),
    ("B1", "A", "日曜夜に早く寝るのは月曜が学校だから", "Dimanche soir, Léo dort tôt parce que... A. demain, c'est l'école · B. il est malade · C. il pleut"),
    ("B2", "A", "月曜は登校日（再開後の通常の月曜日）", "Lundi, Léo... A. retourne à l'école · B. reste en vacances · C. va à Plailly"),
]
for lv, k, nt, body in read_qs:
    bf.ex(lv, "阅读理解", k, nt, body, size=20)

# ---- D. sentence building ----
bf.head("D　PHRASES　文の完成と変換", 24)
d_items = [
    ("A2", "Les élèves vont reprendre les cours lundi.", "aller + 不定詞（futur proche）",
     "Futur proche : « Les élèves reprennent les cours lundi. » → ___"),
    ("B2", "Si tu venais samedi, tu verrais la nocturne.", "si + 半過去 venais",
     "Hypothèse : « Si tu (venir) samedi, tu verrais la nocturne. »"),
    ("B1", "Elle a goûté les coquilles à Port-en-Bessin.", "passé composé : a + 過去分詞",
     "Passé composé : « Elle (goûter) les coquilles à Port-en-Bessin. »"),
    ("B2", "Selon moi, les finales sont excitantes.", "selon moi = 私の意見では",
     "Opinion : « ___ moi, les finales sont excitantes. »"),
    ("B1", "Il est prévu que le Sénat examine le texte lundi.", "il est prévu que + 接続法",
     "Subjonctif : « Il est prévu que le Sénat (examiner) le texte lundi. » → ___"),
]
for lv, k, nt, body in d_items:
    bf.ex(lv, "完成句子", k, nt, body, size=20)

# ---- E. translation ----
bf.head("E　TRADUCTION　翻訳", 24)
e_items = [
    ("B2", "日程表を読むことは、それ自体がフランスを理解することです。", "lire un programme = 日程表を読む",
     "和訳：« Lire un programme, c'est déjà comprendre la France. »"),
    ("A2", "Il court plus vite que son frère.", "比較級 plus vite + court",
     "仏訳：彼は兄より速く走ります。"),
    ("B1", "Les élèves sont en vacances depuis le 17 octobre.", "être en vacances + depuis",
     "仏訳：生徒たちは10月17日から休みです。"),
    ("B1", "Ce soir, nous allons préparer nos cartables.", "futur proche + préparer",
     "仏訳：今夜、私たちはかばんを準備します。"),
    ("B2", "On ne connaît pas encore les finalistes.", "ne...pas encore = まだ〜ない",
     "仏訳：決勝進出者はまだ誰も知らない。"),
]
for lv, k, nt, body in e_items:
    bf.ex(lv, "翻译", k, nt, body, size=20)

# ---- F. matching ----
bf.head("F　LES MOTS　語の対応", 24)
bf.match_set("B1", "词汇配对",
             ["un tournoi", "une nocturne", "un budget", "une coquille", "un festival"],
             ["une compétition avec plusieurs matchs", "une soirée qui dure jusqu'à la nuit",
              "le plan des dépenses de l'État", "le coquillage fêté à Port-en-Bessin",
              "plusieurs concerts en une semaine"],
             ["a", "b", "c", "d", "e"],
             ["tournoi=大会 a", "nocturne=夜のイベント b", "budget=予算 c", "coquille=ホタテ d", "festival=音楽祭 e"],
             instr="組み合わせ")

# ---- G. dialogue ----
dlg_defs = [
    ("A2", "samedi", "11月7日は土曜日"),
    ("A2", "coquilles (des coquilles Saint-Jacques)", "市場でホタテを買う"),
    ("B1", "goûter", "goûter 味わう（不定詞）"),
    ("A2", "recette", "à la portaise は調理法の一つ"),
    ("A2", "week-end", "Bon week-end ! よい週末を"),
]
gnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in dlg_defs]
bf.head("G　DIALOGUE　会話の穴埋め", 24)
bf.para(f"— Bonjour madame, c'est le marché du Goût du Large ? — Oui ! — Pour ({gnums[0]})___, le 7 novembre : je veux des ({gnums[1]})___ pour ma famille. — Goûtez celle-ci ! Vous voulez les ({gnums[2]})___ à la portaise ? — Oui, donnez-moi votre ({gnums[3]})___. — Voilà. Bon ({gnums[4]})___ ! — Merci !", 21)
bf.end_report()

# ---- writing strip ----
wy = 1500
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "写作", "自由記述 — ポイントは作文欄に、範文はこのページの作文欄の中にあります", "ポイントで採点")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　ÉCRITURE　作文", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Écrivez un petit texte (80 à 100 mots) : « Mon week-end du 7–8 novembre ». Racontez : un match, une fête, un plat. Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 190, "フランス語で80〜100語で書きましょう：11月7〜8日の私の週末。試合1つ、祭り1つ、料理1つを書きましょう。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 288, fill=BOX)
p.text(mx2 + 22, wy + 38, "MODÈLE　範文", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Samedi 7 novembre, j'ai regardé les demi-finales du Masters à la télévision : quelle ambiance ! Le soir, nous avons fêté la dernière nocturne avec des amis, déguisés en fantômes. Dimanche 8, nous avons goûté des coquilles Saint-Jacques à la portaise, achetées au marché de Port-en-Bessin. Le matin, nous avons marché au bord de la mer et nous avons acheté des fleurs pour ma grand-mère. Le soir, nous avons écouté de la musique et j'ai lu vingt pages de mon roman français. C'était un week-end parfait.", 21, "serif", False, INK, mw2 - 44, 1.42)

# Explicit printed-note set: the core's noted set (tools/p8.py
# extract, 97/150). Japanese notes are longer than the core's
# <=10-char rule, so the length rule is replaced by this set.
PRINT_NOTES = [1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32, 33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74, 77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]

# ---- keys ----
ky = wy + 312
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "RÉPONSES　全解答と解説（1–8ページ）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— {pg}ページ —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and e["n"] in PRINT_NOTES:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-exercices.svg")
print("P8 saved, TOTAL exercises:", len(REG))
