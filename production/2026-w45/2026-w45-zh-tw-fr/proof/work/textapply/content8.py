# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P8 test & keys (keys generated from the registry).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案 · Test et corrigés", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · Le test de la semaine et toutes les réponses")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判斷對錯 · Vrai ou faux", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "La Semaine FinTech ouvre le lundi 2 nov.",
     "香港金融科技週週一(11月2日)開幕。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Lidong tombe le 7 nov., pas le 6 nov.",
     "立冬在11月6日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Les Dragons ont remporté la série 4-2.",
     "味全龍4勝2敗拿下台灣大賽。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Le match 6 s'est terminé 6-0, pas 6-3.",
     "台灣大賽第六戰比數是6比3。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Le festival de sable s'est terminé le 26 oct.",
     "福隆沙雕藝術季10月26日結束。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B2", "完形單選", "B", "Le salon du voyage ouvre à midi le 6 nov., pas à 10 h 00.",
     "旅展首日上午10點開門。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B · 本週大測驗 · Le grand quiz", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "La conférence principale se tient les 2-3 nov.",
     "金融科技週主會議是哪兩天? A. 11月1、2日 · B. 11月2、3日 · C. 11月5、6日", size=13.8, gap=0)
f.ex("A2", "單選", "C", "Le salon du voyage se poursuit jusqu'au lundi 9 nov.",
     "台北旅展展到哪天? A. 11月7日 · B. 11月8日 · C. 11月9日", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Le festival de l'acier se tient jusqu'au 22 nov.",
     "高雄鋼雕藝術節展到哪天? A. 11月22日 · B. 11月8日 · C. 11月2日", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Le défilé nocturne a eu lieu le 25 oct. à 19 h 00.",
     "天母百鬼夜行踩街在哪天晚上? A. 10月24日 · B. 10月25日 · C. 10月26日", size=13.8, gap=0)
f.ex("B1", "單選", "C", "Le Double 11 tombe le mercredi 11 nov.",
     "雙11是星期幾? A. 週一 · B. 週二 · C. 週三", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Mercedes n'a concédé qu'1 point en 14 manches.",
     "梅賽鍶台灣大賽2場先發,共失幾分? A. 1分 · B. 3分 · C. 6分", size=13.8, gap=0)
f.ex("B2", "單選", "B", "Le défilé des mascottes a lieu chaque jour à 14 h 00.",
     "旅展吉祥物大遊行每天幾點? A. 12:00 · B. 14:00 · C. 19:00", size=13.8, gap=0)
f.ex("B2", "單選", "A", "L'encyclopédie des sentiers réunit 56 itinéraires.",
     "步道大百科收錄幾條路線? A. 56條 · B. 36條 · C. 16條", size=13.8, gap=0)
f.ex("B2", "單選", "C", "Durée totale d'ouverture : 6 + 8 + 8 + 8 = 30 heures.",
     "旅展4天總開放時數是幾小時? A. 24 · B. 28 · C. 30", size=13.8, gap=0)
f.ex("B2", "單選", "B", "Le défi des tampons couvre 6 voies vertes.",
     "6大綠道集章挑戰有幾個集章點? A. 4個 · B. 6個 · C. 9個", size=13.8, gap=0)
f.head("C · 完成句子 · Complétez les phrases", 21, OLIVE, 5)
f.ex("A2", "完成句子", "金融科技", "La fintech : la technologie au service des services financiers.",
     "用手機轉帳、掃碼付款,都是___。", instr="Complétez", size=13.8, gap=0)
f.ex("A2", "完成句子", "立冬", "Lidong marque le début de l'hiver.",
     "冬天第一個節氣是___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "完封", "Un blanchissage : l'adversaire ne marque aucun point.",
     "對手得0分,叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "封王", "Remporter le titre, c'est 封王.",
     "拿下總冠軍,叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "討糖", "La chasse aux bonbons, c'est 討糖.",
     "萬聖節小朋友去店家___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "集章", "Collectionner les tampons, c'est 集章.",
     "在6大綠道蓋章收集,叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "南港", "Le salon du voyage se tient au Centre des expositions de Nangang.",
     "台北旅展在___展覽館一館。", instr="Complétez", size=13.8, gap=0)
f.ex("B1", "完成句子", "駁二", "Pier-2 accueille le festival de l'acier.",
     "鋼雕藝術節在高雄___蓬萊區B3倉庫等地舉行。", instr="Complétez", size=13.8, gap=0)
f.ex("B2", "完成句子", "全球擴張", "L'expansion mondiale : vendre ses produits dans le monde entier.",
     "幫新創公司把產品賣到世界各地,叫___。", instr="Complétez", size=13.8, gap=0)
f.ex("B2", "完成句子", "人工智慧", "L'IA dans la finance, c'est 人工智慧＋.",
     "銀行、投資、保險用___看數據、抓風險。", instr="Complétez", size=13.8, gap=0)
f.head("D · 讀一讀,答一答 · Lisez et répondez", 21, OLIVE, 5)
f.para("阿哲住在台北。週五(11月6日)中午12點,他去南港展覽館看旅展,下午2點看了吉祥物大遊行。週六是立冬,他和家人吃薑母鴨。週日他又去旅展,買了一組11月8日限定的探索廚房自助餐券,4張一共4,100元,準備帶家人去吃自助餐。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Il se rend au salon du voyage le vendredi à midi.",
     "阿哲週五中午去哪裡? A. 大巨蛋 · B. 南港展覽館 · C. 駁二", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Le défilé a lieu à 14 h 00.",
     "吉祥物大遊行在週五幾點? A. 12:00 · B. 14:00 · C. 19:00", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Un lot de 4 bons coûte 4 100 (prix affiché 8 200).",
     "一組探索廚房自助餐券4張一共多少錢? A. 4,100元 · B. 8,200元 · C. 1,600元", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Il mange du canard au gingembre pour Lidong le samedi.",
     "阿哲週六和家人吃什麼? A. 薑母鴨 · B. 冰品 · C. 生魚片", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Ordre : le salon, puis la fondue de Lidong, puis le lot de bons pour un buffet.",
     "這三天他的順序是? A. 先看旅展,再吃薑母鴨,再買餐券去吃自助餐 · B. 先吃自助餐,再看旅展 · C. 先吃薑母鴨,再看旅展,再買券", size=13.8, gap=0)
f.head("E · 情景說話 · En situation", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "Le salon du voyage ouvre le vendredi à midi.",
     "— 旅展哪天開? — 週五___開幕。(A. 中午12點 · B. 晚上7點)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Lidong est le premier terme solaire de l'hiver.",
     "— 立冬是什麼意思? — 冬天___的日子。(A. 結束 · B. 開始)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Un blanchissage signifie que l'adversaire ne marque aucun point.",
     "— 什麼叫完封? — 對手得___分。(A. 0 · B. 6)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Les Dragons ont remporté la série 4-2.",
     "— 台灣大賽誰封王? — 味全龍,___勝2敗。(A. 3 · B. 4)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Le défilé des mascottes a lieu chaque jour à 14 h 00.",
     "— 吉祥物大遊行每天幾點? — 下午___點。(A. 2 · B. 7)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Comparez d'abord les prix, puis payez : 先比價，再結帳.",
     "— 雙11怎麼買才聰明? — 先___，再結帳。(A. 比價 · B. 亂買)", size=13.8, gap=0)
f.head("F · 寫一寫 · À vos plumes", 21, OLIVE, 5)
MODELO = ("旅展從11月6日到11月9日。我想週六去南港展覽館,先看吉祥物大遊行,再去集章。"
          "立冬那天,我想和家人吃薑母鴨,幫身體進補。"
          "旅展有1,600個攤位,我想慢慢逛,不要趕時間。"
          "我想買一組探索廚房自助餐券,4張一共4,100元,帶家人去吃自助餐。"
          "雙11之前,我先列好購物清單,不亂買。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Rédaction — il n'y a pas de réponse unique. Un modèle de {NCHARS} caractères suit.")
f.ex("B2", "寫作", "(開放題,範文如下)", f"Tâche ouverte — le texte modèle est imprimé dans la section F ci-dessus ({NCHARS} caractères)",
     "寫一寫《我的旅展計畫》:旅展你想哪天去?先看什麼?想買什麼票?雙11之前怎麼準備?寫 120~180 字。", instr="Écrivez", size=13.8, gap=0)
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
    af.para(f"— Page {pg} —", 12.8, "sans", True, OLIVE, lh=1.12, gap=1, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.8, "sans", False, INK, lh=1.12, gap=1, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
