# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P8 test & keys (keys generated from the registry).
# Test flow A-E, then a writing strip (task + model + photo), then keys.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案　Teste e respostas", "Lucerna", "第8版　本週大測驗　全部答案　O grande teste da semana e todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 200, 1050, tag="P8-ex")
f.head("A　判斷對錯　Verdadeiro ou falso", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "O desfile é no domingo, 22 nov., às 14:00.",
     "封王遊行11月22日下午2點出發。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "O último show da parada noturna é em 22 nov., não em 15 nov.",
     "六福村夜間遊行最終場在11月15日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "O Natal da Disney começa em 17 nov.",
     "香港迪士尼聖誕11月17日開始。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "O festival do aço termina em 22 nov., não em 15 nov.",
     "鋼雕藝術節11月15日閉幕。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Xiaoxue é 22 de nov.",
     "小雪在11月22日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Kenny G fecha o festival de jazz em 24 nov.",
     "爵士音樂節11月24日由肯尼·基收尾。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B　本週大測驗　O grande quiz", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "O desfile termina no Taipei Dome.",
     "封王遊行終點是哪裡？ A. 天母棒球場 · B. 台北大巨蛋 · C. 駁二", size=13.8, gap=0)
f.ex("A2", "單選", "C", "O demônio gigante tem 5 metros de altura.",
     "夜間遊行的巨型鹿魔有多高？ A. 1米 · B. 3米 · C. 5米", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Xiaoxue é o 20.º termo solar.",
     "小雪是二十四節氣的第幾個？ A. 第20個 · B. 第2個 · C. 第24個", size=13.8, gap=0)
f.ex("B1", "單選", "B", "O show de luzes principal dura 5 minutos cada vez.",
     "耶誕城主燈秀每次幾分鐘？ A. 30分鐘 · B. 5分鐘 · C. 1小時", size=13.8, gap=0)
f.ex("B1", "單選", "C", "587 filmes inscritos.",
     "金馬獎有幾部影片報名？ A. 87部 · B. 57部 · C. 587部", size=13.8, gap=0)
f.ex("B1", "單選", "B", "O festival do aço termina em 22 nov.",
     "鋼雕藝術節展到哪天？ A. 11月15日 · B. 11月22日 · C. 12月22日", size=13.8, gap=0)
f.ex("B2", "單選", "A", "De 17 nov. a 3 jan. são 48 dias.",
     "迪士尼聖誕一共幾天？ A. 48天 · B. 38天 · C. 58天", size=13.8, gap=0)
f.ex("B2", "單選", "B", "De 17 a 22 nov. inclusive são 6 dias.",
     "爵士音樂節第二週一共幾天？ A. 5天 · B. 6天 · C. 7天", size=13.8, gap=0)
f.ex("B2", "單選", "A", "100 pontos se convertem em crédito EasyCard.",
     "滿幾個U幣可以換成悠遊卡儲值金？ A. 100個 · B. 50個 · C. 10個", size=13.8, gap=0)
f.ex("B2", "單選", "B", "Das 14:00 às 19:00 são 5 horas.",
     "遊行下午2點，夜間遊行晚上7點，中間隔幾小時？ A. 3小時 · B. 5小時 · C. 7小時", size=13.8, gap=0)
f.head("C　完成句子　Completar as frases", 21, OLIVE, 5)
f.ex("A2", "完成句子", "封王", "Conquistar o título é 封王.",
     "拿下總冠軍，叫___。", instr="Completar", size=13.8, gap=0)
f.ex("A2", "完成句子", "夜間", "A parada noturna acontece à noite.",
     "《鹿魔覺醒》是___遊行。", instr="Completar", size=13.8, gap=0)
f.ex("B1", "完成句子", "點收", "Confira a entrega antes de abrir a caixa.",
     "包裹到了，先___再拆箱。", instr="Completar", size=13.8, gap=0)
f.ex("B1", "完成句子", "入圍", "Ser indicado é 入圍.",
     "被選進得獎名單，叫___。", instr="Completar", size=13.8, gap=0)
f.ex("B1", "完成句子", "遊行", "Uma marcha de celebração é 遊行.",
     "大家走上街頭慶祝，叫___。", instr="Completar", size=13.8, gap=0)
f.ex("B1", "完成句子", "集點", "Acumular pontos é 集點.",
     "每次運動累積點數，叫___。", instr="Completar", size=13.8, gap=0)
f.ex("B1", "完成句子", "主燈秀", "O show de luzes principal se repete a cada meia hora.",
     "耶誕城的___每半小時一次。", instr="Completar", size=13.8, gap=0)
f.ex("B1", "完成句子", "市集", "Um mercado é 市集.",
     "賣東西、逛街的地方，叫___。", instr="Completar", size=13.8, gap=0)
f.ex("B2", "完成句子", "時間軸", "Leia a linha do tempo para planejar o dia.",
     "先看___，再決定去哪一件。", instr="Completar", size=13.8, gap=0)
f.ex("B2", "完成句子", "小雪", "Xiaoxue é 22 de nov.",
     "11月22日也是___。", instr="Completar", size=13.8, gap=0)
f.head("D　讀一讀，答一答　Leia e responda", 21, OLIVE, 5)
f.para("阿玲住在台北。11月22日（週日）早上，她先查好遊行路線，下午2點去天母看封王遊行，大家都穿紅色衣服。晚上回家，她和爸爸一起看金馬獎轉播，典禮晚上6點30分開始。同一天，高雄鋼雕藝術節閉幕，小雪也在這一天。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Ela assiste ao desfile em Tianmu à tarde.",
     "阿玲週日下午去哪裡？ A. 大巨蛋 · B. 天母棒球場 · C. 駁二", size=13.8, gap=0)
f.ex("B1", "單選", "B", "O desfile é às 14:00.",
     "封王遊行在週日下午幾點出發？ A. 12:00 · B. 14:00 · C. 19:00", size=13.8, gap=0)
f.ex("B1", "單選", "A", "A cerimônia começa às 18:30.",
     "金馬獎頒獎典禮晚上幾點開始？ A. 6點30分 · B. 5點 · C. 8點", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Ordem: primeiro o desfile, depois a cerimônia na tela.",
     "這一天她的順序是？ A. 先看遊行，再看金馬獎轉播 · B. 先看金馬獎，再看遊行 · C. 只看夜間遊行", size=13.8, gap=0)
f.ex("B2", "單選", "A", "O encerramento do aço e Xiaoxue caem ambos em 22 nov.",
     "11月22日還是哪兩個日子？ A. 鋼雕閉幕和小雪 · B. 雙11和旅展 · C. 爵士音樂節開幕", size=13.8, gap=0)
f.head("E　情景說話　Dizer no contexto", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "O desfile é no domingo, 22 nov.",
     "— 封王遊行哪天出發？ — 本週日___出發。(A. 11月22日 · B. 11月15日)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "A parada noturna começa às 19:00.",
     "— 夜間遊行晚上幾點？ — ___(A. 晚上7點 · B. 下午2點)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "O show de luzes principal dura 5 minutos cada vez.",
     "— 主燈秀每次幾分鐘？ — ___(A. 5分鐘 · B. 30分鐘)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "A cerimônia é em 22 nov.",
     "— 金馬獎哪天頒獎？ — ___(A. 11月22日 · B. 11月15日)", size=13.8, gap=0)
f.ex("A2", "完形單選", "A", "Xiaoxue é o 20.º termo solar.",
     "— 小雪是第幾個節氣？ — ___(A. 第20個 · B. 第2個)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Quanto mais frio faz, mais é preciso se manter aquecido: 越…越….",
     "— 天氣越冷，越要___？ — ___(A. 保暖 · B. 開窗)", size=13.8, gap=0)
f.end_report()

# ================= F · writing strip (task + model) =================
# The notes photo fills the flow's last column below the last test item.
img_y = int(f.y) + 30
image(p, "notes.jpg", COLX[3], img_y, CW, 200)
caption(p, COLX[3], img_y + 206, CW, "寫下來，才記得住（資料照片）。",
        "Foto: fazendo anotações com um lápis — CC0 (Unsplash)")
MODELO = ("早上我先列好清單，查好遊行路線和公車時間，才出門。"
          "11月22日是星期日，也是小雪。下午2點，我和家人去天母看封王遊行，大家都穿紅色衣服。"
          "晚上回家，我和爸爸一起看金馬獎轉播，等得獎名單揭曉。"
          "鋼雕藝術節也在這一天閉幕，我想下次去高雄看。"
          "一天看了兩件大事，天氣一天比一天冷，出門要記得保暖。")
NCHARS = len(MODELO.replace(" ", ""))
print("MODEL chars:", NCHARS)
wy = 1050 + 30  # full-width strip below the test flow (bottom 1050)
p.hline(MX, RIGHT, wy - 16, OLIVE, 2)
wx, ww = span_x(0, 3)
p.text(wx, wy + 26, "F　寫一寫　Escrever", 25, "sans", True, OLIVE)
n = reg_ex("B2", "寫作", "(開放題，範文如下)", f"Tarefa aberta — a resposta modelo está impressa acima, na seção F ({NCHARS} caracteres)")
chip(p, wx, wy + 48, "B2")
p.text(wx + 72, wy + 48 + 23, f"{n}.", 24, "sans", True, OLIVE)
p.text(wx + 142, wy + 48 + 23, "Escrever", 19.5, "sans", False, GREY)
ly = p.para(wx, wy + 48 + 36 + 20, "寫一寫《我的一天：11月22日》：11月22日你做了什麼？看了哪一件大事？天氣怎麼樣？寫 120～180 字。", 20, "serif", False, INK, ww, 1.45) + 6
ly = p.para(wx, ly + 18, "Resposta modelo: " + MODELO, 16, "serif", False, INK, ww, 1.35)
strip_end = ly
print("P8 writing strip ends", strip_end, "(flow ended", f.y, ")")

# ================= keys =================
ky = strip_end + 30
p.hline(MX, RIGHT, ky - 14, OLIVE, 2)
p.text(MX, ky + 26, "答案　Respostas — em ordem de página, com uma nota breve em português para cada item", 25, "sans", True, OLIVE)
p.text(RIGHT, ky + 26, "Todas as notas em português　✓ = o modelo de redação", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Página {pg} —", 13.0, "sans", True, OLIVE, lh=1.12, gap=1, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, "sans", False, INK, lh=1.12, gap=1, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
