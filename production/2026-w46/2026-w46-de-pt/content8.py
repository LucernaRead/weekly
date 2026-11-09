# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　Exercícios e respostas", "Die Lucerna", "SCHLUSSTEST　Teste final　Alle Antworten unten auf dieser Seite — todas as respostas no fim desta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "beginnt (3.ª pessoa do singular)"),
    ("A2", "B", "bastelt (3.ª pessoa do singular)"),
    ("A2", "A", "geht (3.ª pessoa do singular)"),
    ("A2", "B", "singt (3.ª pessoa do singular)"),
    ("A2", "A", "schaut (3.ª pessoa do singular)"),
    ("B1", "B", "sieht (3.ª pessoa do singular)"),
    ("A2", "B", "erzählt (3.ª pessoa do singular)"),
    ("B1", "A", "beginnt (3.ª pessoa do singular)"),
]
cnums = [reg_ex(lv, "Completar o texto", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　Lacunas", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ die Schule wieder, und Lena ({cnums[1]})___ eine Laterne aus Papier. Am Mittwoch ({cnums[2]})___ sie mit ihrer Klasse beim Laternenumzug mit und ({cnums[3]})___ Martinslieder. Am Freitagabend ({cnums[4]})___ sie Deutschland in Belgrad. Am Sonntag ({cnums[5]})___ sie die NFL in München im Fernsehen. In der Schule ({cnums[6]})___ Lena: „Die Woche war toll! Der Karneval ({cnums[7]})___ um 11.11 Uhr.“", 20.5)
bf.bridge("Opções:")
for n, opts in zip(cnums, [
    "A. beginnt · B. beginnen · C. begann",
    "A. basteln · B. bastelt · C. bastelte",
    "A. geht · B. gehen · C. ging",
    "A. singen · B. singt · C. sang",
    "A. schaut · B. schauen · C. schaute",
    "A. sehen · B. sieht · C. sah",
    "A. erzählen · B. erzählt · C. erzählte",
    "A. beginnt · B. beginnen · C. begann",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　Quiz", 24)
bf.ex("B1", "Escolha múltipla", "A", "o carnaval começa às 11.11",
      "Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "fora, na Sérvia, na sexta-feira",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "C", "NFL domingo às 15.30",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "A", "o dia de recordação é 15 de novembro",
      "Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "o imposto das famílias é de 2,05 cêntimos",
      "Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "o selecionador anuncia a lista a 5 de novembro",
      "Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "A", "a ZDF em direto desde as 13.30",
      "Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "C", "Totensonntag é 22 de novembro",
      "Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　Leitura", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Mittwoch bastelt die Familie eine Laterne aus Papier. Am Freitag schaut sie Deutschland in Belgrad im Fernsehen. Am Sonntag schaut sie das NFL-Spiel um 15.30 Uhr. „Eine Woche mit Laternen und Football“, sagt Frau Berger.", 20.5)
bf.ex("B1", "Escolha múltipla", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "fazer uma lanterna na quarta-feira",
      "Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "A", "ver a Alemanha na sexta-feira",
      "Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "NFL domingo às 15.30",
      "Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　Frases", 24)
bf.ex("A2", "Construir frases", "Die Karnevalssession beginnt am Mittwoch.", "o tempo, o verbo em segundo",
      "die Karnevalssession / beginnt / am Mittwoch → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("A2", "Construir frases", "Wir basteln eine Laterne aus Papier.", "ordem sujeito–verbo–objeto",
      "wir / basteln / eine Laterne / aus Papier → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("B1", "Construir frases", "Die Kinder gehen am Montag wieder in die Schule.", "o tempo primeiro, o verbo em segundo",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("B1", "Construir frases", "Am Sonntag ist Volkstrauertag in ganz Deutschland.", "lugar e tempo primeiro, verbo em segundo",
      "am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___", instr="Monte a frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　Tradução", 24)
bf.ex("A2", "Tradução", "O carnaval começa às 11.11 em Colónia.", "beginnen = começar",
      "Der Karneval beginnt um 11.11 Uhr in Köln. (traduza para português)", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("A2", "Tradução", "Faço uma lanterna na quarta-feira.", "basteln = fazer, construir",
      "Ich bastle am Mittwoch eine Laterne. (traduza para português)", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("B1", "Tradução", "A escola recomeçou a 9 de novembro.", "wieder begonnen = recomeçado",
      "Die Schule hat am 9. November wieder begonnen. (traduza para português)", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("B1", "Tradução", "Am Sonntag schaue ich das NFL-Spiel.", "ver um jogo = das Spiel schauen",
      "Vejo o jogo da NFL no domingo. (traduza para alemão)", instr="Traduza para o alemão", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　Pares", 24)
bf.match_set("B1", "Correspondência de palavras",
             ["der Mantel", "die Laterne", "das Geisterspiel", "die Versöhnung"],
             ["das Licht aus Papier, das die Kinder am Abend tragen",
              "der warme Umhang, den Martin mit dem Bettler teilte",
              "die Aussöhnung nach einem Streit — Frieden zwischen Menschen",
              "ein Spiel ohne Zuschauer im Stadion"],
             ["b", "a", "d", "c"],
             ["Mantel=manto b", "Laterne=lanterna a", "Geisterspiel=jogo fantasma d", "Versöhnung=reconciliação c"],
             instr="Associe as palavras")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "singst (2.ª pessoa do singular)"),
    ("A2", "A", "macht (2.ª pessoa do plural)"),
    ("A2", "A", "essen (1.ª pessoa do plural)"),
    ("B1", "B", "machst (2.ª pessoa do singular)"),
    ("B1", "A", "schaue (1.ª pessoa do singular)"),
]
dnums = [reg_ex(lv, "Completar o diálogo", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　Completar o diálogo", 24)
bf.para(f"— Hallo, Lena! Bastelst du eine Laterne? — Ja, für St. Martin! Am Mittwoch gehen wir mit. — ({dnums[0]})___ du auch Martinslieder? — Ja, mit meiner Klasse. — Und was ({dnums[1]})___ ihr am Abend? — Wir singen und laufen mit den Laternen. Am Sonntag ({dnums[2]})___ wir Brezeln und schauen die NFL. — Lecker! Und was ({dnums[3]})___ du am Freitag? — Ich ({dnums[4]})___ Deutschland in Belgrad im Fernsehen!", 20.5)
bf.bridge("Opções:")
for n, opts in zip(dnums, [
    "A. singe · B. singst · C. singen",
    "A. macht · B. machen · C. machst",
    "A. essen · B. esse · C. esst",
    "A. machen · B. machst · C. macht",
    "A. schaue · B. schaust · C. schaut",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "Escrita", "Tarefa aberta — segue os pontos do quadro de escrita; o texto-modelo está no quadro desta página", "Avaliado segundo os pontos indicados")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　Escrita", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über St. Martin oder den Volkstrauertag! Die besten Texte drucken wir in VOL.4 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Escreva em alemão, 80–100 palavras: «A minha semana de novembro». Diga o que faz, que jogos vê e com quem — e acrescente uma frase sobre o dia de São Martinho ou o dia de recordação.", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　Texto-modelo (84 palavras)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　Todas as respostas com notas (páginas 1–8)", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f"({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
