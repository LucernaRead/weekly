# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PRIMA PAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1 · PRIMA EDIZIONE", 23, "sans", True, OLIVE)
p.text(975, 92, 'OGNI SETTIMANA IN ITALIANO · 毎週一号 · イタリア人が読んでいるイタリア語を読む', 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "SETTIMANA DAL 19 AL 25 OTTOBRE 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "La Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "イ タ リ ア 語 週 刊 · VOL.1 · L'ORA SOLARE · IL MALTEMPO · IL CINEMA", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "イタリア語テキスト · 日本語の解説 — 日本語読者のための版", 20, "sans", True, BRICK, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "DOMENICA DORMIAMO UN'ORA IN PIÙ!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Nella notte tra sabato e domenica gli orologi tornano indietro: dalle 03:00 alle 02:00.", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, '今週の日曜は1時間長く眠れる', 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, '標準時に戻る夜 · 詳しくは2ページ', 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, 'LA NOTIZIA · トップニュース', 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Un'ora in più di sonno: domenica torna l'ora solare", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Dalla redazione de La Lucerna · Livello di lettura: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Succede tutto domenica. Nella notte tra sabato 24 e domenica 25 ottobre, l'Italia cambia l'ora: alle 03:00 l'orologio torna indietro di un'ora e segna di nuovo le 02:00. La notte dura un'ora in più e dormiamo un'ora in più: torna l'ora solare, dopo sette mesi di ora legale.")
f.para("Ma la parola della settimana è un'altra: «meteo oggi». È la ricerca numero uno in Italia (istantanea Google Trends di martedì 20 ottobre): tutti guardano il cielo. La tempesta Adam porta l'allerta arancione in Liguria, con scuole chiuse in alcuni comuni e allagamenti intorno a Genova e Savona.")
f.para("Domenica è anche l'ultimo giorno della Festa del Cinema di Roma: la 21ª edizione chiude domenica 25 ottobre. E nel fine settimana lo sport regala due grandi partite: Napoli–Roma sabato alle 18:00 e Inter–Fiorentina domenica alle 12:30, la prima partita con l'ora solare.")
f.para("Nei paesi e nelle città è il weekend delle sagre d'autunno: il tartufo bianco è il re della stagione (pagina 3). E in tutta Italia si parla della manovra, la legge di bilancio: il voto del governo slitta a mercoledì 28 ottobre circa (pagina 6).")
f.para("Questa è la prima edizione de La Lucerna in italiano. Ogni settimana leggiamo l'Italia vera con te: piano, chiaro e con onestà. Benvenuti!")
f.expl("解説 — tornare indietro 戻す（時計を） · l'allerta arancione オレンジ警報 · la sagra 郷土の食の祭り · la manovra （国の）予算案。")
f.box('LA SETTIMANA IN CIFRE · 数字で今週', [
    ('25 — le ore della notte tra sabato e domenica（土曜→日曜の夜は25時間）', "serif", False, INK, 20.5, 1.35),
    ("03:00 → 02:00 — il cambio dell'ora, nella notte di domenica（日曜未明に変更）", "serif", False, INK, 20.5, 1.35),
    ("21ª — l'edizione della Festa del Cinema di Roma（ローマ映画祭は第21回）", "serif", False, INK, 20.5, 1.35),
    ('8ª — la giornata di Serie A del fine settimana（今週末のセリエAは第8節）', "serif", False, INK, 20.5, 1.35),
])
f.head('ADESSO TU · さっそく練習', 25)
f.ex("A2", '空所補充', "indietro", 'tornare indietro = （時計を）戻す',
     "Nella notte tra sabato e domenica, l'orologio torna ___ di un'ora.", size=20, gap=7)
f.ex("A2", '空所補充', "più", "un'ora in più = 1時間多い",
     "Domenica dormiamo un'ora in ___.", size=20, gap=7)
f.ex("A2", '空所補充', "meteo", '«meteo oggi» = 今日の天気、今週の検索第1位',
     "La parola più cercata in Italia è «___ oggi».", size=20, gap=7)
f.ex("A2", '空所補充', "Adam", '今季最初の名前つきの嵐は Adam',
     "La tempesta della settimana si chiama ___.", size=20, gap=7)
f.ex("A2", '空所補充', "Roma", '映画祭はローマ、日曜に閉幕',
     "La Festa del Cinema chiude domenica a ___.", size=20, gap=7)
f.ex("B1", '空所補充', "allagamenti", 'allagamenti = 浸水、あふれた水',
     "A Genova e Savona, la tempesta ha portato ___ in alcune strade.", size=20, gap=7)
f.end_report()

# ---- le ricerche di martedì (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "LE RICERCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DI MARTEDÌ", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "火曜の検索 · Cosa cerca l'Italia (Google Trends)", 19, "sans", False, GREY)
gt = [
    ("meteo oggi", "10.000+", 250),
    ("weather", "2.000+", 196),
    ("spurs – thunder", "200+", 122),
    ("meteo palermo", "200+", 122),
    ("clima", "200+", 122),
]
byy = gy + 150
for i, (lab, vol, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.text(gx + gw - 22, byy + 22, vol, 20, "sans", True, BRICK, anchor="end")
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Istantanea di martedì 20 ottobre:", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "le ricerche cambiano ogni ora.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, 'Google トレンド 10月20日（火）。数字は概数です。', 16.5, "sans", False, GREY)

# ---- sommario (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, 'IN QUESTO NUMERO · 今号の内容', 24, "sans", True, OLIVE)
som = [
    ("Pag. 2", "L'ora solare e il meteo", "A2"),
    ("Pag. 3", "Le sagre d'autunno", "A2→B1"),
    ("Pag. 4", "La Serie A", "B1"),
    ("Pag. 5", "Lucca e i giovani", "B1"),
    ("Pag. 6", "La manovra 2027", "B2"),
    ("Pag. 7", "Frasi della settimana", "A2→B2"),
    ("Pag. 8", "Esercizi e risposte", "tutti"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- parola della settimana (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PAROLA DELLA SETTIMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
y2 = p.para(gx, my + 76, "« il maltempo » : la pioggia forte, il vento, le tempeste. Questa settimana il maltempo ha un nome: Adam.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, y2 + 28, '「悪天候」：大雨、強風、嵐、名前は Adam。', 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
# PATCH 2026-10-21 (KIT §13): rule was 1844, striking through the Chinese weather
# gloss above (baseline 1846.3, ink bottom ≈1852); moved to 1864 (row B still at 1874).
p.hline(MX, RIGHT, 1864, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "atomuhr.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Un orologio atomico tra i più precisi del mondo (il NIST-F1, negli Stati Uniti). Anche l'ora ufficiale italiana nasce da orologi atomici — e nella notte di domenica, tutti tornano indietro di un'ora. (Pagina 2)",
        "Foto: NIST (USA) — dominio pubblico")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-autunno")
f2.head("L'AUTUNNO ENTRA NEL VIVO", 25)
f2.para("Giornate più corte, la prima tempesta con un nome, il cinema che chiude e le sagre che aprono: l'autunno italiano mostra questa settimana tutto il suo programma.", 22.5)
f2.para("Il suo regalo per i lettori è un'ora in più di sonno. Prendila — e continua a leggere a pagina 2!", 22.5)
f2.end_report()
# col 3 IN BREVE
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, 'IN BREVE · 短信', 24, "sans", True, OLIVE)
brefs = [
    ("L'ORA", "Domenica alle 03:00 gli orologi tornano alle 02:00: un'ora di sonno in più. (Pagina 2)"),
    ("CINEMA", "La Festa del Cinema di Roma chiude domenica (13–25 ottobre). (Pagina 5)"),
    ("SAGRE", "Weekend: tartufo a Montaione, formaggio Bagòss a Bagolino. (Pagina 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz lampo ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, 'QUIZ LAMPO · 早押しクイズ', 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, '1面を読んで、正しい答えを選ぼう · 答えは8ページ', 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", '選択肢', "B", '時刻変更は土曜から日曜の夜',
      "Il cambio dell'ora è... A. sabato mattina · B. nella notte tra sabato e domenica · C. lunedì", size=21)
qf.ex("A2", '選択肢', "A", '03:00 が 02:00 に戻る',
      "Alle 03:00, l'orologio torna alle... A. 02:00 · B. 04:00 · C. 03:00", size=21)
qf.ex("A2", '選択肢', "C", 'リグーリア州にオレンジ警報',
      "La tempesta Adam porta l'allerta... A. bianca · B. verde · C. arancione", size=21)
qf.ex("A2", '選択肢', "B", '映画祭は日曜に閉幕',
      "La Festa del Cinema di Roma finisce... A. venerdì · B. domenica · C. lunedì", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-prima.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VITA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band('VITA · 生活', "La Lucerna", "LIVELLO A2 · L'ora solare e il meteo · 標準時と天気")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Un'ora in più di sonno: come funziona il cambio", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2")
f.para("Una volta all'anno, una notte dura 25 ore. Nella notte tra sabato 24 e domenica 25 ottobre finisce l'ora legale: alle 03:00 gli orologi tornano indietro, alle 02:00. L'ora tra le 02:00 e le 03:00 arriva due volte nella stessa notte.")
f.para("Sette mesi di ora legale finiscono così. La sera, però, il buio arriva prima: domenica il tramonto arriva un'ora prima, e le giornate sembrano più corte. Gli esperti del sonno parlano di un piccolo «jet lag»: il corpo ha bisogno di qualche giorno per abituarsi.")
f.para("Quali orologi cambiano da soli? Il telefono e il computer cambiano da soli. Ma l'orologio del forno, quello vecchio in cucina e quello dell'auto hanno bisogno della tua mano. Il nostro consiglio: cambia gli orologi sabato sera — e domenica mattina è tutto tranquillo.")
f.head("E IL METEO?", 25)
f.para("La settimana è cominciata con il maltempo. La tempesta Adam — la prima tempesta con un nome della stagione — ha portato l'allerta arancione in Liguria: scuole chiuse in alcuni comuni liguri e allagamenti intorno a Genova e Savona. Per questo «meteo oggi» è la parola più cercata d'Italia: prima di uscire, tutti guardano il cielo.", 23.5)
f.para("E la scuola? In Italia questa è una settimana normale: non c'è una vacanza d'autunno nazionale. Si va a scuola e al lavoro come sempre — solo la notte di domenica è speciale.", 23.5)
f.box('LA FRASE PER RICORDARE · 覚え方', [
    ("«In primavera avanti, in autunno indietro.» Così gli italiani ricordano la direzione del cambio: avanti a marzo, indietro a ottobre — e in autunno, un'ora di sonno in più.", "serif", False, INK, 21.5, 1.4),
])
f.gloss("l'ora legale 夏時間 · l'ora solare 標準時 · il tramonto 日没 · gli allagamenti 浸水 · abituarsi 慣れる。")
f.end_report()

# col 3: facts + e tu? (sequential, measured)
ix = COLX[3]
facts = ["La notte tra sabato e domenica dura 25 ore: è la notte più lunga dell'anno.",
         "L'ora solare resta fino all'ultima domenica di marzo 2027: il 28 marzo gli orologi tornano avanti.",
         "Il telefono cambia l'ora da solo; l'orologio del forno no: serve la tua mano."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LO SAPEVI?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Cosa fai con un'ora in più: dormi, leggi o esci? Scrivi due frasi in italiano e mandale alla redazione: le migliori escono nel VOL.2 (pagina 7, «Lettere dei lettori»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap('増えた1時間を何に使いますか。寝る、読む、それとも出かける？イタリア語で2文書いて、編集部に送ってください。', "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, 'E TU? · あなたは？', 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, '増えた1時間を何に使いますか。寝る、読む、それとも出かける？イタリア語で2文書いて、編集部に送ってください。', 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Dire l'ora wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "DIRE L'ORA · 時刻の言い方", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, 'Gli orari della settimana · 今週の時刻は全部使えます', 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fdfaf0" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{BRICK}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 130, 70, 1, 0, "È l'una.")
clock(560, dy + 130, 70, 2, 30, "Sono le due e mezza.")
clock(880, dy + 130, 70, 2, 45, "Sono le tre meno un quarto.")
lx = 1090
ly = dy + 58
for line in [
    ("È l'una", '= 1:00（1時のときだけ è）'),
    ("e un quarto / e mezza", '= +15分 / +30分'),
    ("meno un quarto", '= 15分前（2:45 = le tre meno un quarto）'),
    ("mezzogiorno / mezzanotte", '= 正午 12:00 / 真夜中 0:00'),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 330, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(lx, ly + 22, "Attenzione: domenica Inter–Fiorentina comincia alle 12:30 — «è mezzogiorno e mezza». Sabato, Napoli–Roma è alle 18:00: «sono le sei di sera».", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, 'ESERCIZI · 2ページの練習', 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, '答えは8ページ · レベルは混在しています。番号で探してください', 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · CHE ORA È?", 25)
e.expl('時刻を見て、イタリア語で文を完成させなさい。')
e.ex("A2", '空所補充', "È", "1:00 は È l'una としか言いません",
     "1:00 — ___ l'una.", instr='空所補充', size=20, gap=8)
e.ex("A2", '空所補充', "mezza", 'e mezza = 〜時半（+30分）',
     "2:30 — Sono le due e ___.", instr='空所補充', size=20, gap=8)
e.ex("A2", '空所補充', "meno", 'meno un quarto = 15分前',
     "2:45 — Sono le tre ___ un quarto.", instr='空所補充', size=20, gap=8)
e.ex("A2", '空所補充', "mezzogiorno", '12:00 = 正午 mezzogiorno',
     "12:00 — È ___.", instr='空所補充', size=20, gap=8)
e.head("B · IL PRESENTE", 25)
e.expl('動詞の現在形を補いなさい。')
e.ex("A2", '空所補充', "dormo", "dormire：io → dormo",
     "Io ___ (dormire) un'ora in più domenica.", instr='空所補充', size=20, gap=8)
e.ex("A2", '空所補充', "dormono", "tutti → dormono（loro）",
     "Domenica ___ (dormire) tutti un'ora in più.", instr='空所補充', size=20, gap=8)
e.ex("A2", '空所補充', "cambiano", "gli orologi → cambiano（loro）",
     "Gli orologi del telefono ___ (cambiare) da soli.", instr='空所補充', size=20, gap=8)
e.ex("B1", '空所補充', "si sveglia", '再帰動詞 svegliarsi → si sveglia',
     "Maria ___ (svegliarsi) alle otto.", instr='空所補充', size=20, gap=8)
e.ex("A2", '空所補充', "torna", "l'orologio → torna（lui）",
     "L'orologio ___ (tornare) indietro alle 03:00.", instr='空所補充', size=20, gap=8)
e.head("C · COMPRENSIONE", 25)
e.expl('2ページの記事を読んで、正しい答えを選びなさい。')
e.ex("A2", '選択肢', "C", '02:00–03:00 の1時間が2回現れる',
     "L'ora tra le 02:00 e le 03:00 arriva... A. mai · B. una volta · C. due volte", size=20, gap=8)
e.ex("A2", '選択肢', "B", 'オーブンの時計は手で直す',
     "Quale orologio NON cambia da solo? A. quello del telefono · B. quello del forno · C. quello del computer", size=20, gap=8)
e.ex("A2", '選択肢', "B", 'リグーリア州にオレンジ警報',
     "La tempesta Adam ha portato l'allerta... A. gialla · B. arancione · C. rossa", size=20, gap=8)
e.ex("A2", '選択肢', "B", 'イタリアの今週は通常の週で、全国的な秋休みはない',
     "In Italia, questa settimana di ottobre... A. è vacanza nazionale · B. è una settimana normale · C. le scuole sono chiuse ovunque", size=20, gap=8)
e.ex("B1", '選択肢', "A", '標準時では日没が1時間早くなる',
     "Con l'ora solare, il tramonto arriva... A. un'ora prima · B. un'ora dopo · C. alla stessa ora", size=20, gap=8)
e.head("D · LE PAROLE DEL METEO", 25)
e.match_set("A2", '語と意味を結ぶ',
            ["il maltempo", "l'allagamento", "il tramonto", "abituarsi"],
            ["quando il sole scende e arriva il buio",
             "prendere l'abitudine, piano piano",
             "pioggia forte e tempesta",
             "l'acqua che copre le strade"],
            ["c", "d", "a", "b"],
            ['maltempo=大雨と嵐 c', 'allagamento=水が道を覆う d', 'tramonto=日没 a', 'abituarsi=少しずつ慣れる b'],
            instr='語と意味を結ぶ')
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vita.svg")
print("P2 saved, exercises so far:", len(REG))
