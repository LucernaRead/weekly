# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language PORTUGUESE. 8 pages, 1950x2700.
Headlines/excerpts loaded verbatim from cover-backfill/headlines-w45.json
at build time, never retyped. Explanations in Portuguese, traceable to
headline+excerpt only. Cover itself carries NO vol number (COVER mark
instead); P8 lists each core paper's own VOL (FR VOL.3, all others VOL.2,
per task). Adapted from the W45 DE cover builder; svglib.py COPIED into
this build dir, never imported from a core build dir.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, esc, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"))
assert [i["source_lang"] for i in ITEMS] == ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"], "fixed order changed!"
assert all(i["vol"] == (3 if i["source_lang"] == "fr" else 2) for i in ITEMS), "VOL mismatch vs task"

TABLES = json.load(open("/home/hatch/workspace/goals/lucernaread-social-media-operations/tools/tables.json"))
LANGS = TABLES["languages"]

# Portuguese-language names for the source languages; zh split simplificado/tradicional.
PT_NAME = {"en": "Inglês", "de": "Alemão", "fr": "Francês",
           "es": "Espanhol", "it": "Italiano", "pt": "Português",
           "nl": "Neerlandês", "ru": "Russo", "ja": "Japonês",
           "ko": "Coreano", "zh-cn": "Chinês (simplificado)",
           "zh-tw": "Chinês (tradicional)"}
FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}

EXPLAIN = {
 "en": "Os Estados Unidos votam numa eleição intercalar: todos os 435 lugares da Câmara dos Representantes, cerca de um terço do Senado e governos de muitos estados estão em disputa.",
 "de": "Uma semana cheia de futebol: Liga dos Campeões na terça e na quarta, Liga Europa na quinta, e na sexta começa a 9.ª jornada da Bundesliga, com o Bayern no Atlético Madrid e o Estugarda no Galatasaray na terça.",
 "fr": "Depois das férias de Todos os Santos, os alunos regressam à escola em França e a semana termina com três finais no fim de semana de 7 e 8 de novembro, incluindo as finais do Rolex Paris Masters em Nanterre no domingo.",
 "es": "As listas já foram apresentadas e os partidos escrevem agora os seus programas: no domingo, 29 de novembro, a Espanha vota em eleições gerais em que a habitação deve decidir a campanha.",
 "it": "Na segunda-feira, 2 de novembro, chega à Itália o primeiro frio a sério da estação, com chuva na costa adriática e a primeira neve ligeira nas montanhas; novembro deverá ser mais frio do que a média, uma probabilidade, não uma certeza.",
 "pt": "A semana vai do feriado de Finados, na segunda-feira, 2 de novembro, até ao primeiro dia do Enem, no domingo, 8 de novembro: descansar, rever e fazer a prova.",
 "nl": "De 2 a 8 de novembro é a Semana do Clima nos Países Baixos: municípios de todo o país organizam ações, plantar árvores, poupar energia, ir de bicicleta em vez de carro, e todos podem participar.",
 "ru": "Uma semana invulgar na Rússia: trabalha-se na segunda e na terça, e a quarta-feira, 4 de novembro, é feriado, um dia livre a meio da semana de trabalho.",
 "ja": "O Dia da Cultura cai na terça-feira, 3 de novembro, um feriado em que escolas e empresas fecham e há eventos culturais em todo o país.",
 "ko": "A semana de 2 a 8 de novembro marca a chegada do inverno: o sábado, 7 de novembro, é o Ip-dong, o primeiro dos 24 períodos solares do inverno.",
 "zh-cn": "A fase de vendas do Double 11 já está a decorrer: os produtos estão à venda desde meados de outubro e continuam até 13 de novembro, e o inverno também está a chegar.",
 "zh-tw": "A Semana FinTech de Hong Kong x StartmeupHK 2026 abre na segunda-feira, 2 de novembro, em Hong Kong e dura cinco dias, até sexta-feira, 6 de novembro, com conferência principal, exposição e mais de 100 eventos comunitários, e mais de 45 000 participantes esperados.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}
# Cover-original text must use ASCII apostrophes only (no U+2019: it renders
# fullwidth in Noto CJK). Portuguese cover text here needs no apostrophes.
for _k, _v in EXPLAIN.items():
    assert "\u2019" not in _v and "\u2018" not in _v, f"curly quote in {_k}"

W, H = 1950, 2700
MX, CW = 130, 1690
FOOT_Y = 2624

def new_page():
    return Page(W, H)

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "A Lucerna  ·  COVER  ·  2 a 8 de novembro de 2026", 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

def tag_of(it):
    lang = it["source_lang"]
    pt_name = PT_NAME[lang].upper()
    native = LANGS[lang]["label"].upper()
    # Dedupe: Portuguese name == native label for IT and PT (ITALIANO,
    # PORTUGUÊS) — printing both would read as a stutter.
    if pt_name == native:
        return pt_name
    return pt_name + "  ·  " + native

# ---------------- P1 ----------------
p = new_page()
header(p, "CAPA SEMANAL  ·  2 A 8 DE NOVEMBRO DE 2026")
p.text(975, 330, "A Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, "2 a 8 de novembro de 2026", 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "Doze capas, uma semana", 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Doze jornais, doze línguas, uma semana de novembro: cada manchete abaixo abre a sua própria capa, na sua própria língua, com uma breve explicação em português sobre o que ela diz e por que chama a atenção.", 46, "serif", False, GREY, 1510, 1.45)
y += 40
p.hline(MX, MX + CW, y, GOLD, 2)
y += 55
for it in ITEMS:
    p.text(MX, y, tag_of(it), 28, "sans", True, OLIVE)
    y += 38
    y = para(p, MX, y, it["headline"], 38, "serif", True, INK, CW, 1.28, family=FAMILY[it["source_lang"]])
    y += 14
    assert y < 2520, f"P1 overflow at {it['source_lang']}: y={y}"
footer(p, "1")
p.save(os.path.join(OUT, "p1-cover.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (a, b) in enumerate(PAIRS):
    p = new_page()
    header(p, "A LUCERNA  ·  COVER  ·  2 A 8 DE NOVEMBRO DE 2026")
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, tag_of(it), 34, "sans", True, OLIVE)
        y += 64  # widened per W45 DE cover: audit flagged tag ink touching headline ink at 52
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "O QUE ISTO SIGNIFICA", 30, "sans", True, OLIVE)
        y += 46
        y = para(p, MX, y, EXPLAIN[lang], 44, "sans", False, GREY, CW, 1.5)
        y += 58
        if idx == a:
            p.hline(MX, MX + CW, y, LINE, 1.5)
            y += 62
        assert y < 2540, f"P{pi+2} overflow at {lang}: y={y}"
    footer(p, str(pi + 2))
    p.save(os.path.join(OUT, f"p{pi+2}-cover.svg"))

# ---------------- P8: twelve cores at a glance ----------------
p = new_page()
header(p, "A LUCERNA  ·  COVER  ·  2 A 8 DE NOVEMBRO DE 2026")
p.text(975, 300, "Os doze jornais desta semana", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "Os doze jornais principais por trás desta capa, por ordem.", 44, "serif", False, GREY, anchor="middle")
p.hline(MX, MX + CW, 440, GOLD, 3)
y = 520
for it in ITEMS:
    lang = it["source_lang"]
    vol = it["vol"]
    p.text(MX, y, f"{it['masthead']}  ·  VOL.{vol}", 36, "sans", True, OLIVE)
    y += 50
    y = para(p, MX, y, it["headline"], 44, "serif", True, INK, CW, 1.32, family=FAMILY[lang])
    y += 40
    assert y < 2520, f"P8 overflow at {lang}: y={y}"
footer(p, "8")
p.save(os.path.join(OUT, "p8-cover.svg"))
print("OK: 8 SVGs in", OUT)
