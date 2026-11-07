# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-pt/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · Exercícios e respostas", "Die Lucerna", "SCHLUSSTEST · Teste final · Todas as respostas no fim desta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "schnitzen = esculpir (a abóbora)"),
    ("A2", "A", "geht in die Bibliothek = vai à biblioteca"),
    ("A2", "A", "Uhr zurückgestellt = o relógio atrasado"),
    ("A2", "C", "Winterzeit = começa o horário de inverno"),
    ("A2", "B", "eine Stunde länger = uma hora a mais"),
    ("A2", "A", "der erste Frost = a primeira geada"),
    ("B1", "B", "gefällt mir gut = gosto muito"),
    ("A2", "C", "ich gehe (primeira pessoa)"),
]
cnums = [reg_ex(lv, "Completar o texto", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · Texto lacunar", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("Opções:")
for n, opts in zip(cnums, [
    "A. kocht · B. schnitzt · C. malt",
    "A. geht · B. schläft · C. kocht",
    "A. zurückgestellt · B. vorgestellt · C. vergessen",
    "A. Sommerzeit · B. Ferienzeit · C. Winterzeit",
    "A. früh · B. länger · C. laut",
    "A. Frost · B. Sommer · C. Frühling",
    "A. geht · B. gefällt · C. macht",
    "A. gehen · B. gehst · C. gehe",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B · WISSENSFRAGEN · Quiz", 24)
bf.ex("B1", "Escolha múltipla", "A", "o Dia das Bibliotecas lembra Preusker",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "domingo às 3 se atrasa",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "A", "O bis O = de outubro à Páscoa",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "o Klassiker é em Dortmund",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "a proteção se forma em 10–14 dias",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "nas farmácias, vacina a partir dos 18 anos",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "o jogão de sábado: Dortmund–Frankfurt",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "a hora das 2 às 3 aparece duas vezes",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · Leitura", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "Escolha múltipla", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "às onze joga Bingo com as crianças",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "à noite, em casa, ajusta os relógios",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "como o relógio atrasa, pode dormir mais",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · Monte frases", 24)
bf.ex("A2", "Construir frases", "Die Uhr wird am Sonntag zurückgestellt.", "wird na segunda posição, o particípio no fim",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("A2", "Construir frases", "Wir schlafen eine Stunde länger.", "ordem sujeito–verbo–objeto",
      "wir / schlafen / eine Stunde / länger → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("B1", "Construir frases", "Die Kinder freuen sich, weil Ferien sind.", "com weil o verbo vai para o fim",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("B1", "Construir frases", "Am Samstag ist der Tag der Bibliotheken.", "começa pela indicação de tempo; o verbo na segunda posição",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="Monte a frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · Tradução", 24)
bf.ex("A2", "Tradução", "Esta noite tem 25 horas.", "Stunden = horas",
      "Die Nacht hat 25 Stunden.", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("A2", "Tradução", "No sábado à noite, ajusto o relógio.", "umstellen = ajustar (um relógio)",
      "Ich stelle die Uhr am Samstagabend um.", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("B1", "Tradução", "Am Sonntag schlafe ich eine Stunde länger.", "dormir uma hora a mais = eine Stunde länger schlafen",
      "No domingo, durmo uma hora a mais.", instr="Traduza para o alemão", size=19.5, gap=8)
bf.ex("B1", "Tradução", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen = pode-se pegar emprestado",
      "Na biblioteca, pode-se pegar livros emprestados.", instr="Traduza para o alemão", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · Associe", 24)
bf.match_set("B1", "Correspondência de palavras",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung = a troca entre horário de verão e de inverno, b", "Mitgliedstaaten = os Estados-membros, c", "Mehrheit = a maioria, d", "Feiertag = o feriado, a"],
             instr="Associe as palavras")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch = o livro (para o filho)"),
    ("B1", "B", "im ersten Stock = no primeiro andar (acima do térreo)"),
    ("A2", "C", "Bingo = o bingo da biblioteca"),
    ("B1", "A", "Bibliotheksausweis = a carteirinha da biblioteca"),
    ("B1", "B", "behalten = ficar com (o livro)"),
]
dnums = [reg_ex(lv, "Completar o diálogo", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · Complete o diálogo", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("Opções:")
for n, opts in zip(dnums, [
    "A. Buch · B. Bett · C. Brot",
    "A. Keller · B. Stock · C. Garten",
    "A. Fußball · B. Kino · C. Bingo",
    "A. Bibliotheksausweis · B. Bibliotheksausflug · C. Bibliotheksautor",
    "A. essen · B. behalten · C. singen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "Escrita", "Pergunta aberta — siga os pontos do quadro de escrita; o texto-modelo está no quadro desta página", "Avaliação pelos pontos indicados")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · Escrita", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Escreva em alemão 80–100 palavras: «O meu domingo, 25 de outubro». Conte quanto você dorme, o que faz de manhã, à tarde e à noite, e escreva também uma frase sobre o relógio.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · Texto-modelo (87 palavras)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · TODAS AS RESPOSTAS COM NOTAS (PÁGINAS 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
