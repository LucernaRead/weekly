# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P8: 38 exercises + registry-generated answers. Dash style, as W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · EJERCICIOS Y RESPUESTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("EJERCICIOS Y RESPUESTAS　練習與答案", "La Lucerna", "第8版　La gran prueba de la semana + todas las respuestas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRÓNICA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "visita a Chequia = 客場對捷克",
     "El jueves, la Roja ___ a Chequia en Praga. (A. recibe · B. visita)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "recibir a Inglaterra = 主場迎戰英格蘭",
     "El domingo, España ___ a Inglaterra en Madrid. (A. visita · B. recibe)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "la lista = 徵召名單",
     "De la Fuente dio ___ el viernes 6. (A. la lista · B. la huelga)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "la huelga dura 24 horas = 罷工持續 24 小時",
     "La huelga del miércoles ___ 24 horas. (A. empieza · B. dura)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "empieza la campaña = 競選開始",
     "El viernes 13 ___ la campaña electoral. (A. empieza · B. termina)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "el sobre = 信封",
     "El voto por correo llega en un ___. (A. puente · B. sobre)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "週日上演西班牙–英格蘭",
     "El domingo se juega el ___ en el Metropolitano. (A. España–Inglaterra · B. derbi madrileño)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "veranillo = 小陽春",
     "En noviembre llega el ___ de San Martín. (A. veranillo · B. puente)", size=15.5, gap=1)
f.head("B　PREGUNTAS GENERALES", 22, OLIVE, 5)
f.ex("A2", "單選", "B", "大罷工在 11 月 11 日週三",
     "La huelga general es el... A. lunes 9 · B. miércoles 11 · C. viernes 13", size=15.5, gap=1)
f.ex("A2", "單選", "A", "聖馬丁節 11 月 11 日",
     "San Martín es el... A. 11 de noviembre · B. 12 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.ex("A2", "單選", "C", "西班牙–英格蘭與罷工都在本週",
     "Esta semana hay... A. solo fútbol · B. solo huelga · C. la huelga y el España–Inglaterra", size=15.5, gap=1)
f.ex("B1", "單選", "B", "magosto 吃烤栗子",
     "¿Qué se come en el magosto? A. flan · B. castañas asadas · C. chocolate", size=15.5, gap=1)
f.ex("B1", "單選", "A", "罷工口號：工資、住房、物價",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=15.5, gap=1)
f.ex("B1", "單選", "C", "大選在 11 月 29 日",
     "Las elecciones generales son el... A. 29.10 · B. 13.11 · C. 29.11", size=15.5, gap=1)
f.ex("B2", "單選", "B", "CIS 住房晴雨表：擔心住房者 86,9%",
     "Según el CIS de vivienda, está preocupado el... A. 13,5 % · B. 86,9 % · C. 79 %", size=15.5, gap=1)
f.ex("B1", "單選", "A", "競選 11 月 13 日開始",
     "La campaña electoral empieza el... A. 13 de noviembre · B. 3 de noviembre · C. 29 de noviembre", size=15.5, gap=1)
f.head("C　LEE Y RESPONDE", 22, OLIVE, 5)
f.para("Pablo vive en Madrid: el miércoles 11 sigue la huelga en las noticias y el domingo ve el España–Inglaterra en el Metropolitano. Ana vive en Barcelona: el miércoles 11 trabaja, y el domingo ve el partido por televisión. Los dos leen los programas antes de votar el 29.", 16.5, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Pablo 週日去大都會球場",
     "¿Quién ve el partido en el Metropolitano? A. Ana · B. Pablo · C. los dos", size=15.5, gap=1)
f.ex("A2", "單選", "A", "Ana 週三上班",
     "El miércoles 11, Ana... A. trabaja · B. va a la huelga · C. duerme", size=15.5, gap=1)
f.ex("A2", "單選", "A", "兩人都讀綱領再投票",
     "Antes de votar, los dos... A. leen los programas · B. ven «Infamia» · C. viajan a Praga", size=15.5, gap=1)
f.ex("A2", "單選", "B", "標題概括兩地對比",
     "El mejor título es... A. «Una tormenta» · B. «Dos miércoles» · C. «El Clásico»", size=15.5, gap=1)
f.head("D　CONSTRUYE FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "El miércoles hay huelga general.", "主語 + 動詞 + 地點",
     "el miércoles / hay / huelga general → ___", instr="造句", size=15.5, gap=1)
f.ex("A2", "造句", "El domingo vemos el España–Inglaterra.", "時間在前",
     "el domingo / vemos / el España–Inglaterra → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "La campaña empieza a las cero horas.", "a las cero horas = 在零點",
     "la campaña / empieza / a las cero horas → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "¿A qué hora empieza el partido?", "疑問詞在句首",
     "¿ / a qué hora / empieza / el partido / ? → ___", instr="造句", size=15.5, gap=1)
f.head("E　TRADUCE", 22, OLIVE, 5)
f.ex("A2", "翻譯", "週三全西班牙大罷工。", "對照原文",
     "El miércoles hay huelga general en toda España. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("A2", "翻譯", "週日我們看西班牙–英格蘭。", "對照原文",
     "El domingo vemos el España–Inglaterra. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("B1", "翻譯", "El voto por correo llega a casa.", "llegar a casa = 送到家裡",
     "郵寄選票送到家裡。→ ___", instr="翻譯", size=15.5, gap=1)
f.ex("B2", "翻譯", "Cada gráfico tiene que llevar su fuente.", "tener que = 必須",
     "每個圖表都必須標明來源。→ ___", instr="翻譯", size=15.5, gap=1)
f.head("F　LAS PALABRAS DEL 29N", 22, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["el sondeo", "la muestra", "el margen de error", "la junta electoral"],
            ["quien organiza las elecciones",
             "el error posible de un sondeo",
             "una encuesta de opinión",
             "las personas entrevistadas"],
            ["c", "d", "b", "a"],
            ["sondeo=民調 c", "muestra=樣本 d", "margen de error=誤差範圍 b", "junta electoral=選舉委員會 a"],
            instr="把詞和釋義配對")
f.head("G　DIÁLOGO EN LA INMOBILIARIA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "A", "alquiler = 租金",
     "— Busco un piso de ___. (A. alquiler · B. puente)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "tres habitaciones = 三居室",
     "— ¿Cuántas habitaciones? — ___. (A. Tres · B. Tres puentes)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "¿cuánto cuesta? 多少錢",
     "— ¿Cuánto ___ al mes? (A. cuesta · B. duerme)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "firmar = 簽（合同）",
     "— ¿Cuándo vamos a ___ el contrato? (A. firmar · B. votar)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "mudanza = 搬家",
     "— La ___ es el miércoles 11, día de huelga. (A. mudanza · B. campaña)", size=15.5, gap=1)
f.head("H　ESCRIBE TÚ", 22, OLIVE, 5)
f.expl("寫作題（無唯一答案）；範文（84 詞）見下。")
f.ex("B1", "寫作", "（開放題，範本如下）", "範文見本版 H 區（84 詞）",
     "«¿Qué harías tú por la vivienda?» Escribe 80–100 palabras: tu plan del miércoles 11, tu domingo 15 y tu voto del 29.", instr="寫作", size=15.5, gap=1)
MODELO = ("Vivo en Madrid, y el miércoles 11 sigo la huelga en las noticias: salarios, vivienda y precios, los tres temas de la semana. "
          "El viernes 13 empieza la campaña, y el domingo 15 veo el España–Inglaterra con mi familia. "
          "El jueves 12 veo el Chequia–España en Praga por televisión, a las 20:45. "
          "Mis amigos de Barcelona no tienen huelga en su empresa: el miércoles trabajan. Yo, en cambio, leo los programas con calma y preparo mi voto por correo. "
          "El 29 votamos. ¡Qué semana!")
f.para("Texto modelo: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RESPUESTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPUESTAS　全部答案與簡析（第1–8版）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句中文簡析　帶 ✓ 的為範本題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 第{pg}版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ejercicios.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
