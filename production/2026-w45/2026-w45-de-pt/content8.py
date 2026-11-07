# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-pt/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · Exercícios e respostas", "Die Lucerna", "SCHLUSSTEST · Teste final · Todas as respostas estão no fim desta página")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "spielt (3ª pessoa do singular)"),
    ("A2", "A", "beginnt (3ª pessoa do singular)"),
    ("A2", "B", "kauft (3ª pessoa do singular)"),
    ("A2", "C", "schnitzt = esculpir uma abóbora"),
    ("A2", "B", "schläft (3ª pessoa do singular)"),
    ("B1", "B", "Tankrabatt = desconto no combustível"),
    ("A2", "A", "geht (3ª pessoa do singular)"),
    ("B1", "B", "erzählt (3ª pessoa do singular)"),
]
cnums = [reg_ex(lv, "Completar o texto", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · Texto lacunar", 24)
bf.para(f"Lena freut sich auf die Fußballwoche. Am Dienstag sieht sie Bayern bei Atlético Madrid, am Mittwoch Dortmund gegen Real Betis. Am Donnerstag ({cnums[0]})___ Hoffenheim bei Crystal Palace, und am Freitag ({cnums[1]})___ die Bundesliga mit Hamburg gegen Gladbach. Am Samstag ({cnums[2]})___ Lena einen Kürbis und ({cnums[3]})___ ihn zu Hause. Am Sonntag ({cnums[4]})___ sie lange, denn die Woche war anstrengend. In der Schule erzählt sie: „Die Fußballwoche war toll! Und der ({cnums[5]})___ läuft noch bis Dezember.“ Am Montag ({cnums[6]})___ Lena wieder in die Schule und ({cnums[7]})___ von den Spielen.", 20.5)
bf.bridge("Opções:")
for n, opts in zip(cnums, [
    "A. spielen · B. spielt · C. spieltet",
    "A. beginnt · B. beginnen · C. begann",
    "A. kaufen · B. kauft · C. kaufte",
    "A. malt · B. kocht · C. schnitzt",
    "A. schlafen · B. schläft · C. schlief",
    "A. Spieltag · B. Tankrabatt · C. Advent",
    "A. geht · B. gehen · C. ging",
    "A. erzählen · B. erzählt · C. erzählte",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B · WISSENSFRAGEN · Perguntas", 24)
bf.ex("B1", "Escolha múltipla", "A", "desconto vai até 31 de dezembro de 2026",
      "Der Tankrabatt läuft bis... A. 31. Dezember 2026 · B. 1. November · C. 31. Oktober", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "Bayern fora contra o Atlético na terça-feira",
      "Bayern spielt am Dienstag bei... A. Galatasaray · B. Atlético Madrid · C. Real Betis", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "A", "Hoffenheim fora contra o Crystal Palace na Liga Europa",
      "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Marseille · C. Manchester City", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "as férias de Baden-Württemberg acabaram",
      "In welchem Bundesland sind die Ferien schon vorbei? A. Bayern · B. Baden-Württemberg · C. Berlin", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "expectativas do ZEW em 28,1",
      "Der ZEW-Index: Die Erwartungen fielen im Oktober auf... A. 34,7 · B. 28,1 · C. 47,1", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "A", "Hamburgo–Gladbach abrem na sexta-feira",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "o programa de 26 de outubro debateu o cuidado em casa",
      "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober... A. die Stromsteuer · B. die Pflege zu Hause · C. den Tankrabatt", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "O Dia de Todos os Santos é 1º de novembro",
      "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · Leitura", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Dienstagabend schaut die Familie Bayern bei Atlético im Fernsehen. Am Samstag fährt sie zum Markt und kauft einen Kürbis. Am Sonntag schaut sie Hoffenheim gegen Schalke um 19.30 Uhr. „Eine Woche mit Fußball und Kürbis“, sagt Frau Berger.", 20.5)
bf.ex("B1", "Escolha múltipla", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "B", "ver o Bayern fora contra o Atlético na terça-feira",
      "Was schaut die Familie am Dienstag? A. Dortmund–Betis · B. Bayern bei Atlético · C. Hoffenheim–Schalke", size=19.5, gap=8)
bf.ex("A2", "Escolha múltipla", "A", "comprar uma abóbora no sábado",
      "Was kauft die Familie am Samstag? A. einen Kürbis · B. ein Buch · C. ein Kostüm", size=19.5, gap=8)
bf.ex("B1", "Escolha múltipla", "B", "Hoffenheim–Schalke no domingo às 19:30",
      "Wann spielt Hoffenheim gegen Schalke? A. Samstag 18.30 Uhr · B. Sonntag 19.30 Uhr · C. Freitag 20.30 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · Construir frases", 24)
bf.ex("A2", "Construir frases", "Die Bundesliga beginnt am Freitag.", "expressão de tempo primeiro, verbo em segundo",
      "die Bundesliga / beginnt / am Freitag → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("A2", "Construir frases", "Wir schauen Bayern bei Atlético.", "ordem sujeito–verbo–objeto",
      "wir / schauen / Bayern / bei Atlético → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("B1", "Construir frases", "Die Kinder gehen am Montag wieder in die Schule.", "expressão de tempo primeiro, verbo em segundo",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="Monte a frase", size=19.5, gap=8)
bf.ex("B1", "Construir frases", "In Bayern dauern die Ferien noch an.", "lugar primeiro, verbo em segundo",
      "in Bayern / dauern / die Ferien / noch an → ___", instr="Monte a frase", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · Tradução", 24)
bf.ex("A2", "Tradução", "O desconto no combustível vai até dezembro.", "laufen = durar, continuar",
      "Der Tankrabatt läuft bis Dezember.", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("A2", "Tradução", "Vejo futebol na terça-feira.", "schauen = ver",
      "Ich schaue am Dienstag Fußball.", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("B1", "Tradução", "A escola recomeçou.", "wieder begonnen = recomeçou",
      "Die Schule hat wieder begonnen.", instr="Traduza para o português", size=19.5, gap=8)
bf.ex("B1", "Tradução", "Am Sonntag schlafe ich eine Stunde länger.", "dormir uma hora a mais = eine Stunde länger schlafen",
      "Durmo uma hora a mais no domingo.", instr="Traduza para o alemão", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · Associe", 24)
bf.match_set("B1", "Correspondência de palavras",
             ["der Tankrabatt", "die Pflege", "der Advent", "der Pausenhof"],
             ["die Zeit vor Weihnachten, in der man plant und bastelt",
              "die Ermäßigung auf die Energiesteuer beim Tanken",
              "der Hof der Schule, auf dem die Kinder in der Pause spielen",
              "die Hilfe für Menschen, die nicht mehr allein leben können"],
             ["b", "d", "a", "c"],
             ["Tankrabatt = desconto no combustível b", "Pflege = cuidados d", "Advent = Advento a", "Pausenhof = pátio da escola c"],
             instr="Associe as palavras")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "schaust (2ª pessoa do singular)"),
    ("A2", "A", "siehst (2ª pessoa do singular)"),
    ("A2", "A", "kochen (1ª pessoa do plural)"),
    ("B1", "B", "machst (2ª pessoa do singular)"),
    ("B1", "A", "gehe (1ª pessoa do singular)"),
]
dnums = [reg_ex(lv, "Completar o diálogo", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · Diálogo", 24)
bf.para(f"— Hallo, Lena! Schaust du am Dienstag Fußball? — Ja, Bayern bei Atlético! Um 21.00 Uhr. — Und am Mittwoch? — Dortmund gegen Betis. Ich bin für Dortmund. — ({dnums[0]})___ du am Sonntag auch Fußball? — Ja, Hoffenheim gegen Schalke um 19.30 Uhr. — Mit wem ({dnums[1]})___ du das Spiel? — Mit meiner Familie, zu Hause. Wir ({dnums[2]})___ Kürbissuppe. — Lecker! Und was ({dnums[3]})___ du am Montag? — Ich ({dnums[4]})___ wieder in die Schule. Die Ferien sind vorbei!", 20.5)
bf.bridge("Opções:")
for n, opts in zip(dnums, [
    "A. schaut · B. schaust · C. schauen",
    "A. siehst · B. sehen · C. sieht",
    "A. kochen · B. koche · C. kocht",
    "A. machen · B. machst · C. macht",
    "A. gehe · B. geht · C. gehen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "Escrita", "Tarefa aberta — siga os pontos do quadro de escrita; o texto-modelo está no quadro desta página", "Avaliação pelos pontos indicados")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · Escrita", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Fußballwoche». Erzählen Sie: Welche Spiele schauen Sie? Mit wem? Was essen Sie beim Spiel? Schreiben Sie auch einen Satz über den Tankrabatt oder die Pflege! Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "Escreva em alemão, 80–100 palavras: «Minha semana de futebol». Diga quais jogos você assiste, com quem e o que você come durante o jogo — e acrescente uma frase sobre o desconto no combustível ou os cuidados. Os melhores textos serão publicados no VOL.3 (página 7, «Cartas dos leitores»).", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · Texto-modelo (84 palavras)", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche schaue ich viel Fußball. Am Dienstag sehe ich Bayern bei Atlético, am Mittwoch Dortmund gegen Betis. Am Donnerstag spielt Hoffenheim bei Crystal Palace. Am Freitag sehe ich Hamburg gegen Gladbach mit meinem Bruder. Wir essen Brezeln und trinken Apfelschorle. Am Sonntag schauen wir Hoffenheim gegen Schalke. Der Tankrabatt freut mich sehr: Ich tanke 50 Liter und spare rund 8,35 Euro. Am Samstag kaufe ich einen Kürbis und schnitze ihn mit Lena. Am Montag gehe ich zur Arbeit. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
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
            s += f"({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
