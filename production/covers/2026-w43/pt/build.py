# -*- coding: utf-8 -*-
"""W43 cover for Portuguese readers. Headlines/excerpts loaded verbatim
from the shared backfill JSON; explanations are original Portuguese text
traceable to each item's headline + excerpt only."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "svg")
os.makedirs(OUT, exist_ok=True)

SRC = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/cover-backfill/headlines-w43.json")
ITEMS = json.load(open(SRC, encoding="utf-8"))
assert len(ITEMS) == 12, len(ITEMS)
ORDER = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
assert [i["source_lang"] for i in ITEMS] == ORDER, "fixed order violated"

TAG = {"en": "INGLÊS", "de": "ALEMÃO", "fr": "FRANCÊS", "es": "ESPANHOL",
       "it": "ITALIANO", "pt": "PORTUGUÊS", "nl": "NEERLANDÊS", "ru": "RUSSO",
       "ja": "JAPONÊS", "ko": "COREANO", "zh-cn": "CHINÊS SIMPLIFICADO",
       "zh-tw": "CHINÊS TRADICIONAL"}
FAM = {"ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
       "zh-tw": "Noto Serif CJK TC"}
EXPL = {
 "en": "As eleições americanas já começaram na prática: a votação antecipada abriu no Texas e em outros quatro estados, antes do dia oficial das eleições, 3 de novembro.",
 "de": "No domingo, a Alemanha atrasa os relógios uma hora, encerrando o horário de verão, numa semana em que onze Länder estão de férias.",
 "fr": "Apesar de a eleição ser só em 2027, os franceses já falam dela — e a pesquisa mais popular da semana no Google em França é justamente sobre as sondagens da presidencial de 2027.",
 "es": "Na madrugada de domingo, a Espanha atrasa os relógios e dorme uma hora a mais — e no mesmo domingo joga-se o Clásico.",
 "it": "Na noite de sábado para domingo, a Itália atrasa os relógios uma hora e volta à hora solar, depois de sete meses de horário de verão.",
 "pt": "No domingo, os brasileiros voltam às urnas para o segundo turno da eleição presidencial, disputada por Lula (PT) e Flávio Bolsonaro (PL).",
 "nl": "É uma semana cheia nos Países Baixos: as regiões Centro e Sul estão de férias de outono até domingo, o Norte volta às aulas na segunda — e a semana traz ainda design, dance e uma hora extra de sono.",
 "ru": "Os meteorologistas esperam os primeiros flocos de neve entre quarta e sexta-feira, de 21 a 23 de outubro, com temperaturas em torno de zero graus.",
 "ja": "O primeiro jogo da Série do Japão é no sábado, 24 de outubro, às 18h30, no Estádio de Yokohama, opondo os BayStars aos Hawks — um confronto que não acontecia há dois anos.",
 "ko": "O tufão Champi, o 30.º da temporada, avança para norte e foi classificado como muito forte na manhã do dia 21; o nome, dado pelo Laos, significa flor.",
 "zh-cn": "O Duplo 11 chegou mais cedo este ano: a JD pôs produtos à venda a 12 de outubro, a Taobao e a Tmall abriram a pré-venda a 15 — e há ainda uma abertura a 20 de outubro.",
 "zh-tw": "O forte tufão 薔琵 aproxima-se do mar a leste de Taiwan, grande e forte, e o seu efeito combinado com a monção de nordeste promete chuva maior e mais prolongada.",
}

W, H = 1950, 2700
X0, X1 = 130, 1820
CW = X1 - X0

def footer(p, n):
    p.hline(X0, X1, 2560, GOLD, 2)
    p.text(X0, 2624, "A Lucerna · COVER · Semana 43", 34, "sans", True, GREY)
    p.text(X1, 2624, f"Página {n} de 8", 34, "sans", True, GREY, anchor="end")

def header_small(p, label):
    p.text(X0, 170, "A LUCERNA — COVER · SEMANA 43", 32, "sans", True, OLIVE)
    p.text(X1, 170, label, 32, "sans", True, GREY, anchor="end")
    p.hline(X0, X1, 196, GOLD, 2)

def fam_of(lang):
    return FAM.get(lang, "Noto Serif CJK SC")

# ---------------- P1 ----------------
p = Page(W, H)
bw = text_w("COVER", "sans", True, 44) + 90
p.rect((W - bw) / 2, 128, bw, 68, fill=BOX, stroke=INK, sw=2)
p.text(W / 2, 176, "COVER", 44, "sans", True, INK, anchor="middle")
p.text(W / 2, 400, "A Lucerna", 168, "serif", True, INK, anchor="middle")
p.hline(520, 1430, 448, GOLD, 3)
p.text(W / 2, 540, "19 a 25 de outubro de 2026 · Semana 43", 42, "sans", True, OLIVE, anchor="middle")
p.text(W / 2, 700, "Uma semana, doze manchetes", 96, "serif", True, INK, anchor="middle")
intro = ("Nesta capa reunimos as doze manchetes principais da semana, cada uma "
         "na sua língua original e acompanhada de uma breve explicação em português. "
         "Folheie, compare e descubra o que marcou a semana em cada língua.")
y = p.para(W / 2, 800, intro, 42, "serif", False, GREY, max_w=1520, lh=1.5, anchor="middle")
y += 40
p.text(X0, y, "As doze manchetes", 42, "sans", True, OLIVE)
p.hline(X0, X1, y + 16, GOLD, 2)
y += 70
COLW, COLX = 820, [X0, 1000]
rows = [(ITEMS[i], ITEMS[i + 6]) for i in range(6)]
for left, right in rows:
    rh = 0
    for item, cx in ((left, COLX[0]), (right, COLX[1])):
        tag = f"{ORDER.index(item['source_lang']) + 1:02d} · {TAG[item['source_lang']]}"
        hl = wrap(item["headline"], "serif", True, 38, COLW)
        hh = 56 + (len(hl) - 1) * 51 + 46
        rh = max(rh, hh)
        yy = y
        p.text(cx, yy, tag, 30, "sans", True, OLIVE)
        yy += 56
        for ln in hl:
            p.text(cx, yy, ln, 38, "serif", True, INK, family=fam_of(item["source_lang"]))
            yy += 51
    y += rh + 26
assert y <= 2540, f"P1 overflow: {y}"
p.hline(520, 1430, 2400, GOLD, 2)
p.text(W / 2, 2470, "Boa leitura em doze línguas.", 42, "serif", False, GREY, anchor="middle")
footer(p, 1)
p.save(os.path.join(OUT, "p1.svg"))

# ---------------- P2-P7: two items per page ----------------
pairs = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(pairs):
    p = Page(W, H)
    header_small(p, f"As manchetes da semana · {pi + 2} de 8")
    y = 290
    for k, item in enumerate((ITEMS[a], ITEMS[b])):
        lang = item["source_lang"]
        fam = fam_of(lang)
        p.text(X0, y, f"{TAG[lang]} · {item['masthead']}", 36, "sans", True, OLIVE)
        y += 78
        hl = wrap(item["headline"], "serif", True, 58, CW)
        for ln in hl:
            p.text(X0, y, ln, 58, "serif", True, INK, family=fam)
            y += 78
        y += 18
        y = p.para(X0, y, item["excerpt"], 44, "serif", False, INK, max_w=CW, lh=1.55, family=fam)
        y += 26
        p.text(X0, y, "O que isto quer dizer", 36, "sans", True, OLIVE)
        y += 58
        y = p.para(X0, y, EXPL[lang], 44, "serif", False, INK, max_w=CW, lh=1.55)
        y += 30
        if k == 0:
            p.hline(X0, X1, y + 8, LINE, 1.5)
            y += 62
    assert y <= 2540, f"P{pi + 2} overflow: {y}"
    footer(p, pi + 2)
    p.save(os.path.join(OUT, f"p{pi + 2}.svg"))

# ---------------- P8 ----------------
p = Page(W, H)
header_small(p, "Os jornais da semana")
y = 290
p.text(X0, y, "Os doze jornais da semana", 56, "serif", True, INK)
y += 66
y = p.para(X0, y, "As edições principais de cada língua, com a sua manchete de capa.",
           42, "serif", False, GREY, max_w=CW, lh=1.5)
y += 40
for i, item in enumerate(ITEMS):
    lang = item["source_lang"]
    p.text(X0, y, f"{i + 1:02d} · {TAG[lang]} — {item['masthead']} · VOL. {item['vol']}",
           34, "sans", True, OLIVE)
    y += 50
    hl = wrap(item["headline"], "serif", True, 38, CW)
    for ln in hl:
        p.text(X0, y, ln, 38, "serif", True, INK, family=fam_of(lang))
        y += 50
    y += 26
assert y <= 2540, f"P8 overflow: {y}"
footer(p, 8)
p.save(os.path.join(OUT, "p8.svg"))
print("OK, pages written to", OUT)
