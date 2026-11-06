# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案 · Examen y respuestas", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · El examen de la semana y todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判斷對錯 · Verdadero o falso", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "El Doble Nueve es el 9/9 lunar.",
     "重陽節在農曆九月初九。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "La fiesta de Hong Kong fue el lunes 19 de octubre, no el 20.",
     "香港重陽節翌日假期在10月20日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "A", "El viernes y el sábado son los días de mayor cercanía.",
     "颱風薔琵週五、週六最接近台灣。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Los Dragones ganaron el partido 1, 3-0, no los Hermanos.",
     "台灣大賽第一戰,中信兄弟3比0贏味全龍。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Los premios de series son el sábado; el viernes, los de programas.",
     "金鐘獎戲劇類在週五頒獎。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "400 - 258 = 142 de ahorro con el pase de degustación.",
     "品味證比逐樣買便宜142港幣。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B · 本週大測驗 · El gran cuestionario", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "El aviso marítimo podría llegar el miércoles por la noche.",
     "海上颱風警報最快哪晚發佈? A. 週一 · B. 週三 · C. 週五", size=13.8, gap=0)
f.ex("A2", "單選", "B", "Pide 4 días y tendrás 9 libres.",
     "「請4放9」一共放幾天? A. 4天 · B. 9天 · C. 13天", size=13.8, gap=0)
f.ex("A2", "單選", "A", "Las hembras (蟹乸) están en su mejor momento en el mes lunar 9.",
     "農曆九月先吃什麼蟹? A. 蟹乸 · B. 蟹公 · C. 蟹仔", size=13.8, gap=0)
f.ex("A2", "單選", "B", "La venta de la tienda de Tianmu empieza el jueves 22 de octubre.",
     "天母店週年慶哪天開跑? A. 週二 · B. 週四 · C. 週六", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Al mejor de siete: gana el primero que llegue a 4.",
     "台灣大賽要先贏幾場才封王? A. 3場 · B. 4場 · C. 7場", size=13.8, gap=0)
f.ex("B1", "單選", "B", "El resultado se anuncia en la ceremonia del sábado.",
     "人氣獎結果何時公佈? A. 投票截止時 · B. 週六典禮當晚 · C. 週日早上", size=13.8, gap=0)
f.ex("B1", "單選", "C", "Participan más de 340 puestos.",
     "美酒佳餚巡禮有幾個攤位? A. 約140個 · B. 約240個 · C. 逾340個", size=13.8, gap=0)
f.ex("B1", "單選", "B", "La Ciudad de Halloween de Taoyuan abre el sábado 24 de octubre.",
     "桃園萬聖城哪天開城? A. 10月23日 · B. 10月24日 · C. 10月25日", size=13.8, gap=0)
f.ex("B2", "單選", "B", "El pase premium reúne artículos por 900 HK$.",
     "尊尚品酒證的內容總值是? A. 558港幣 · B. 900港幣 · C. 400港幣", size=13.8, gap=0)
f.ex("B2", "單選", "A", "脆 es el apodo taiwanés de Threads.",
     "哪個說法對? A. 「脆」是台灣對 Threads 的暱稱 · B. 「脆」是一種餅乾 · C. 「脆」是香港用法", size=13.8, gap=0)
f.head("C · 完成句子 · Completa las frases", 21, OLIVE, 5)
f.ex("A2", "完成句子", "共伴", "Tifón más monzón: el efecto conjunto.",
     "颱風加東北季風,叫___效應。", instr="Completa", size=13.8, gap=0)
f.ex("A2", "完成句子", "登高", "Subir a lo alto es la costumbre del Doble Nueve.",
     "重陽節爬山,叫作___。", instr="Completa", size=13.8, gap=0)
f.ex("A2", "完成句子", "疏運", "疏運 — el operativo de transporte de las fiestas.",
     "連假人多,台鐵、高鐵加開班次,這叫___。", instr="Completa", size=13.8, gap=0)
f.ex("A2", "完成句子", "送百", "Por cada 1.000, 100: 滿千送百.",
     "每滿一千送一百,叫滿千___。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "完成句子", "完封", "Dejar en blanco: el rival anota cero.",
     "棒球比賽對手得0分,叫___。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "完成句子", "星光", "La alfombra roja es la 星光大道.",
     "頒獎典禮走紅毯的部分,叫___大道。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "完成句子", "哈囉", "哈囉喂 — el Halloween de Hong Kong.",
     "海洋公園的萬聖節,香港人叫___喂。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "完成句子", "12", "Un cangrejo de 3 taels se cuece unos 12 minutos.",
     "蒸一隻3両的大閘蟹,約___分鐘。", instr="Completa", size=13.8, gap=0)
f.ex("B2", "完成句子", "品味", "Los cupones son 品味券 (fichas de degustación).",
     "美酒佳餚巡禮的券,叫___券。", instr="Completa", size=13.8, gap=0)
f.ex("B2", "完成句子", "留友", "留友看 — guardarlo para que lo lean los amigos.",
     "看到好文存起來給朋友,叫「___看」。", instr="Completa", size=13.8, gap=0)
f.head("D · 讀一讀,答一答 · Lee y responde", 21, OLIVE, 5)
f.para("阿哲住在台北。光復節連假,他週六晚上在家看台灣大賽第六戰(如果有需要)。週日晚上七點,他去天母看百鬼夜行踩街,還拿到一個南瓜桶。週一是補假,他睡到自然醒,下午去信義新天地逛週年慶,買了一雙鞋:2,600元,滿千送百,他拿到200元回饋券。三天連假,他過得很開心。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Ve la Serie de Taiwán el sábado por la noche.",
     "阿哲週六晚上看什麼? A. 金鐘獎 · B. 台灣大賽 · C. 電影", size=13.8, gap=0)
f.ex("B1", "單選", "B", "El desfile es el domingo a las 19:00.",
     "踩街在週日幾點? A. 17:00 · B. 19:00 · C. 21:00", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Compra en Xinyi el lunes de fiesta.",
     "他週一去哪裡逛週年慶? A. 天母店 · B. 信義新天地 · C. 台中中港店", size=13.8, gap=0)
f.ex("B1", "單選", "B", "2.600 = dos miles completos, así que 2 × 100 = 200 de vuelta.",
     "鞋子2,600元,他拿到多少回饋券? A. 100元 · B. 200元 · C. 260元", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Orden: primero el béisbol, después el desfile, después las compras.",
     "這三天他的順序是? A. 先看球,再踩街,再逛街 · B. 先逛街,再看球 · C. 先踩街,再逛街,再看球", size=13.8, gap=0)
f.head("E · 情景說話 · Diálogo en contexto", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "Consulta el aviso antes de salir con tifón.",
     "— 明天會下雨嗎? — 颱風來了,先看___再出門。(A. 警報 · B. 菜單)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "2.000 = dos miles, así que 200 en vales.",
     "— 這件外套多少錢? — 2,000元,滿千送百,可以拿___元券。 A. 100 · B. 200", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Subir (登高) es lo propio del Doble Nueve.",
     "— 你重陽節做什麼? — 我去___,還吃了紅龜粿。(A. 登高 · B. 討糖)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "El partido 4 es el miércoles 21 de octubre.",
     "— G4 是哪天? — 週___,10月21日。(A. 二 · B. 三)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Los resultados llegan en la ceremonia del sábado.",
     "— 人氣獎結果何時知道? — 週六___公佈。(A. 典禮當晚 · B. 下週一)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "留友看 — guarda la publicación para los amigos.",
     "— 這篇文不錯。 — 我先存起來,___看。(A. 留友 · B. 哈囉)", size=13.8, gap=0)
f.head("F · 寫一寫 · A escribir", 21, OLIVE, 5)
MODELO = ("光復節連假有三天。第一天,我在家看台灣大賽,如果打到第六戰,我一定準時打開電視。"
          "第二天晚上七點,我去天母看百鬼夜行,順便討糖。"
          "第三天是補假,我想睡晚一點,下午去信義新天地逛週年慶。"
          "下週四美酒佳餚巡禮開幕,我先買了兩張品味證,一共516元,準備帶媽媽去中環看海、吃好料。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Redacción — no hay una única respuesta correcta. A continuación va un modelo de {NCHARS} caracteres.")
f.ex("B2", "寫作", "(pregunta abierta — modelo a continuación)", f"Pregunta abierta — el modelo está impreso arriba, en la sección F",
     "寫一寫《我的連假計畫》:三天連假你想做什麼?哪天看什麼活動?要買什麼票?寫 120~180 字。", instr="Redacción", size=13.8, gap=0)
f.para("Respuesta modelo: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Respuestas — en orden de páginas, con una nota breve en español para cada ejercicio", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Todas las notas en español · ✓ = el modelo de redacción", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
# Fan-out key typography: half-width parentheses with a space before the note
# parenthesis. svglib._fw would convert the outer pair to full-width whenever
# the note contains a Chinese term, so key lines (only) bypass the pair rule.
import svglib as _sg, re as _re
_orig_fw = _sg._fw
def _fw_keys(s):
    if _re.match(r"^\d+\. ", s):
        return s
    return _orig_fw(s)
_sg._fw = _fw_keys
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Página {pg} —", 13.0, "sans", True, OLIVE, lh=1.13, gap=1, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ ({e_['note']})"
        af.para(txt, 13.0, lh=1.13, gap=0.25, split=False)
_sg._fw = _orig_fw
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
