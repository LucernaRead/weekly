# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P8 test & keys (keys generated from the registry).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-tw-es-proof/work/reg-core2/svg"
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案 · Test & keys", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · This week's test and every answer key")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判斷對錯 · True or false", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "FinTech Week opens Monday, Nov 2.",
     "香港金融科技週週一(11月2日)開幕。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Lidong is Nov 7, not Nov 6.",
     "立冬在11月6日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "The Dragons won the series 4-2.",
     "味全龍4勝2敗拿下台灣大賽。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Game 6 ended 6-0, not 6-3.",
     "台灣大賽第六戰比數是6比3。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "The sand festival closed Oct 26.",
     "福隆沙雕藝術季10月26日結束。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B2", "完形單選", "B", "The travel fair opens at noon on Nov 6, not 10:00.",
     "旅展首日上午10點開門。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B · 本週大測驗 · The big quiz", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "The main conference is Nov 2-3.",
     "金融科技週主會議是哪兩天? A. 11月1、2日 · B. 11月2、3日 · C. 11月5、6日", size=13.8, gap=0)
f.ex("A2", "單選", "C", "The travel fair runs to Monday, Nov 9.",
     "台北旅展展到哪天? A. 11月7日 · B. 11月8日 · C. 11月9日", size=13.8, gap=0)
f.ex("B1", "單選", "A", "The steel festival runs to Nov 22.",
     "高雄鋼雕藝術節展到哪天? A. 11月22日 · B. 11月8日 · C. 11月2日", size=13.8, gap=0)
f.ex("B1", "單選", "B", "The night parade marched Oct 25 at 19:00.",
     "天母百鬼夜行踩街在哪天晚上? A. 10月24日 · B. 10月25日 · C. 10月26日", size=13.8, gap=0)
f.ex("B1", "單選", "C", "Double 11 is Wednesday, Nov 11.",
     "雙11是星期幾? A. 週一 · B. 週二 · C. 週三", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Mercedes allowed 1 run in 14 innings.",
     "梅賽鍶台灣大賽2場先發,共失幾分? A. 1分 · B. 3分 · C. 6分", size=13.8, gap=0)
f.ex("B2", "單選", "B", "The mascot parade runs daily at 14:00.",
     "旅展吉祥物大遊行每天幾點? A. 12:00 · B. 14:00 · C. 19:00", size=13.8, gap=0)
f.ex("B2", "單選", "A", "The trail encyclopaedia collects 56 routes.",
     "步道大百科收錄幾條路線? A. 56條 · B. 36條 · C. 16條", size=13.8, gap=0)
f.ex("B2", "單選", "C", "Total opening hours: 6 + 8 + 8 + 8 = 30.",
     "旅展4天總開放時數是幾小時? A. 24 · B. 28 · C. 30", size=13.8, gap=0)
f.ex("B2", "單選", "B", "The stamp challenge covers 6 Greenways.",
     "6大綠道集章挑戰有幾個集章點? A. 4個 · B. 6個 · C. 9個", size=13.8, gap=0)
f.head("C · 完成句子 · Fill in", 21, OLIVE, 5)
f.ex("A2", "完成句子", "金融科技", "Fintech: technology running financial services.",
     "用手機轉帳、掃碼付款,都是___。", instr="Fill in", size=13.8, gap=0)
f.ex("A2", "完成句子", "立冬", "Lidong starts winter.",
     "冬天第一個節氣是___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "完封", "A shutout: the other side scores zero.",
     "對手得0分,叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "封王", "Winning the title is 封王.",
     "拿下總冠軍,叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "討糖", "Trick-or-treating is 討糖.",
     "萬聖節小朋友去店家___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "集章", "Collecting stamps is 集章.",
     "在6大綠道蓋章收集,叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "南港", "The travel fair is at the Nangang Exhibition Center.",
     "台北旅展在___展覽館一館。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "駁二", "Pier-2 hosts the steel festival.",
     "鋼雕藝術節在高雄___蓬萊區B3倉庫等地舉行。", instr="Fill in", size=13.8, gap=0)
f.ex("B2", "完成句子", "全球擴張", "Global expansion: selling products worldwide.",
     "幫新創公司把產品賣到世界各地,叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B2", "完成句子", "人工智慧", "AI inside finance is 人工智慧＋.",
     "銀行、投資、保險用___看數據、抓風險。", instr="Fill in", size=13.8, gap=0)
f.head("D · 讀一讀,答一答 · Read and answer", 21, OLIVE, 5)
f.para("阿哲住在台北。週五(11月6日)中午12點,他去南港展覽館看旅展,下午2點看了吉祥物大遊行。週六是立冬,他和家人吃薑母鴨。週日他又去旅展,買了一組11月8日限定的探索廚房自助餐券,4張一共4,100元,準備帶家人去吃自助餐。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "He goes to the travel fair on Friday at noon.",
     "阿哲週五中午去哪裡? A. 大巨蛋 · B. 南港展覽館 · C. 駁二", size=13.8, gap=0)
f.ex("B1", "單選", "B", "The parade is at 14:00.",
     "吉祥物大遊行在週五幾點? A. 12:00 · B. 14:00 · C. 19:00", size=13.8, gap=0)
f.ex("B1", "單選", "A", "A set of 4 coupons costs 4,100 (list price 8,200).",
     "一組探索廚房自助餐券4張一共多少錢? A. 4,100元 · B. 8,200元 · C. 1,600元", size=13.8, gap=0)
f.ex("B1", "單選", "A", "He eats ginger duck for Lidong on Saturday.",
     "阿哲週六和家人吃什麼? A. 薑母鴨 · B. 冰品 · C. 生魚片", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Order: fair, then Lidong pot, then the coupon set for a buffet.",
     "這三天他的順序是? A. 先看旅展,再吃薑母鴨,再買餐券去吃自助餐 · B. 先吃自助餐,再看旅展 · C. 先吃薑母鴨,再看旅展,再買券", size=13.8, gap=0)
f.head("E · 情景說話 · Say it in context", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "The travel fair opens Friday at noon.",
     "— 旅展哪天開? — 週五___開幕。(A. 中午12點 · B. 晚上7點)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Lidong is the first solar term of winter.",
     "— 立冬是什麼意思? — 冬天___的日子。(A. 結束 · B. 開始)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "A shutout means the other side scores zero.",
     "— 什麼叫完封? — 對手得___分。(A. 0 · B. 6)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "The Dragons won the series 4-2.",
     "— 台灣大賽誰封王? — 味全龍,___勝2敗。(A. 3 · B. 4)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "The mascot parade is at 14:00 daily.",
     "— 吉祥物大遊行每天幾點? — 下午___點。(A. 2 · B. 7)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Compare prices first, then pay: 先比價，再結帳.",
     "— 雙11怎麼買才聰明? — 先___，再結帳。(A. 比價 · B. 亂買)", size=13.8, gap=0)
f.head("F · 寫一寫 · Writing", 21, OLIVE, 5)
MODELO = ("旅展從11月6日到11月9日。我想週六去南港展覽館,先看吉祥物大遊行,再去集章。"
          "立冬那天,我想和家人吃薑母鴨,幫身體進補。"
          "旅展有1,600個攤位,我想慢慢逛,不要趕時間。"
          "我想買一組探索廚房自助餐券,4張一共4,100元,帶家人去吃自助餐。"
          "雙11之前,我先列好購物清單,不亂買。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Writing — there is no single right answer. A {NCHARS}-character model follows.")
f.ex("B2", "寫作", "(開放題,範文如下)", f"Open task - the model answer is printed in section F above ({NCHARS} characters)",
     "寫一寫《我的旅展計畫》:旅展你想哪天去?先看什麼?想買什麼票?雙11之前怎麼準備?寫 120~180 字。", instr="Writing", size=13.8, gap=0)
f.para("Model answer: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Answer keys — in page order, with a short English note for every item", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "All notes in English · ✓ = the writing model", 19.5, "sans", False, GREY, anchor="end")
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
