# -*- coding: utf-8 -*-
"""Lucerna Weekly COVER, W43 (19-25 ottobre 2026), reader language ITALIAN.
Headlines + excerpts loaded VERBATIM from cover-backfill/headlines-w43.json.
All cover-original writing (title, intro, explanations, labels) in Italian.
8 pages, 1950x2700, weekly visual system. No VOL number on this cover."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import Page, wrap, text_w, INK, OLIVE, GOLD, PAPER, BOX, LINE, GREY, BRICK

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
SRC = os.path.join(BASE, "hidden_files/cover-backfill/headlines-w43.json")
OUT = os.path.join(BASE, "hidden_files/cover-w43-it-build/svg")
os.makedirs(OUT, exist_ok=True)

ITEMS = json.load(open(SRC, encoding="utf-8"))
assert len(ITEMS) == 12, len(ITEMS)
ORDER = ["en", "de", "fr", "es", "it", "pt", "nl", "ru", "ja", "ko", "zh-cn", "zh-tw"]
assert [i["source_lang"] for i in ITEMS] == ORDER, [i["source_lang"] for i in ITEMS]

# Italian source-language labels (tables.json, IT column T_BADGE)
LABEL = {"en": "INGLESE", "de": "TEDESCO", "fr": "FRANCESE", "es": "SPAGNOLO",
         "it": "ITALIANO", "pt": "PORTOGHESE", "nl": "OLANDESE", "ru": "RUSSO",
         "ja": "GIAPPONESE", "ko": "COREANO", "zh-cn": "CINESE SEMPLIFICATO",
         "zh-tw": "CINESE TRADIZIONALE"}

# Explanations in Italian, 1-2 sentences each, every claim traceable to that
# item's headline + excerpt ONLY (no facts beyond the source article).
EXPL = {
 "en": "Negli Stati Uniti il voto è già iniziato in alcuni Stati, con l'apertura del voto anticipato. L'appuntamento ufficiale resta il giorno delle elezioni.",
 "de": "In Germania finisce l'ora legale e si recupera un'ora di sonno. La stessa settimana è anche settimana di vacanze in undici Paesi.",
 "fr": "Le elezioni presidenziali sono lontane, ma i francesi guardano già ai sondaggi. La ricerca più diffusa della settimana lo dimostra.",
 "es": "Domenica la Spagna cambia l'ora e dorme un'ora in più. La stessa domenica si gioca anche il Clásico.",
 "it": "Nella notte tra sabato e domenica l'Italia torna all'ora solare, dopo sette mesi di ora legale. La notte dura un'ora in più e si dorme un'ora in più.",
 "pt": "Domenica i brasiliani tornano alle urne per il secondo turno delle elezioni presidenziali. In corsa restano due nomi: Lula e Flávio Bolsonaro.",
 "nl": "Nei Paesi Bassi è una settimana piena, con le vacanze autunnali nelle regioni centrali e meridionali. Nel nord, invece, la scuola ricomincia lunedì.",
 "ru": "La prima neve potrebbe arrivare già in questa settimana, tra mercoledì e venerdì. Le temperature restano intorno allo zero.",
 "ja": "Sabato alle 18:30, allo stadio di Yokohama, si gioca la prima partita della Japan Series tra Yokohama DeNA e Fukuoka SoftBank. Le due squadre si ritrovano dopo due anni.",
 "ko": "Il tifone Champi, il trentesimo della stagione, si sta spostando verso nord. Il suo nome, proposto dal Laos, significa fiore, e secondo le previsioni è un tifone molto forte.",
 "zh-cn": "Il «doppio undici» è arrivato in anticipo: le vendite sono già cominciate e questa è la settimana del pagamento finale.",
 "zh-tw": "Un forte tifone si avvicina al mare a est di Taiwan, con venti intensi e un raggio molto ampio. L'incontro con il monsone di nord-est rischia di rendere le piogge ancora più abbondanti e prolungate.",
}

W, H = 1950, 2700
ML, MR = 110, 1840          # content margins
CW = MR - ML                # 1730

def footer(p, n):
    p.hline(ML, MR, 2580, LINE, 1.2)
    p.text(975, 2624, f"La Lucerna · COVER · Pagina {n} di 8", 30, "sans", False, GREY, "middle")

def masthead_block(p, y, subtitle=None):
    # COVER badge (pill) centred above the masthead
    bw = 210
    p.rect(975 - bw // 2, y, bw, 56, fill=OLIVE, rx=28)
    p.text(975, y + 40, "COVER", 32, "sans", True, PAPER, "middle")
    y += 215  # masthead 150px: ink top ≈ baseline-112, badge bottom y+56 → 47px clear
    p.text(975, y, "La Lucerna", 150, "serif", True, INK, "middle")
    y += 62
    p.text(975, y, "19–25 ottobre 2026", 42, "sans", False, GREY, "middle")
    return y + 40

# ---------------- P1 ----------------
p = Page(W, H)
y = masthead_block(p, 110)
p.hline(ML, MR, y + 10, GOLD, 2.5)
y += 90
y = p.para(ML, y, "Dodici lingue, una settimana", 96, "serif", True, OLIVE, CW, 1.25)
y += 18
y = p.para(ML, y,
    "In questa copertina trovi la notizia principale di ognuna delle dodici edizioni della settimana: "
    "dodici lingue, dodici sguardi sulla stessa settimana, da leggere e confrontare.",
    42, "serif", False, INK, CW, 1.45)
y += 34
y = p.section_head(ML, y, "LE DODICI PRIME PAGINE", 36)
y += 46
COLW = 845
for r in range(6):
    a, b = ITEMS[2 * r], ITEMS[2 * r + 1]
    row_top = y
    for item, cx in ((a, ML), (b, ML + COLW + 40)):
        yy = row_top
        p.text(cx, yy, LABEL[item["source_lang"]], 30, "sans", True, OLIVE)
        yy += 46
        for ln in wrap(item["headline"], "serif", True, 44, COLW):
            p.text(cx, yy, ln, 44, "serif", True, INK)
            yy += 44 * 1.32
        if item is a:
            ha = yy - row_top
        else:
            hb = yy - row_top
    y = row_top + max(ha, hb) + 30
    if r < 5:
        p.hline(ML, MR, y - 14, LINE, 1.0)
# reading guide box (generic framing only, no new facts)
y += 10
guide = ["Ogni notizia è riportata nella sua lingua originale, con una breve spiegazione in italiano.",
         "Nelle pagine seguenti trovi tutti i titoli per intero; a pagina 8, l'elenco dei dodici settimanali."]
glines = []
for g in guide:
    glines += wrap(g, "serif", False, 40, CW - 72)
box_h = len(glines) * int(40 * 1.45) + 92
p.rect(ML, y - 44, CW, box_h, fill=BOX)
p.rect(ML, y - 44, 10, box_h, fill=GOLD)
gy = y + 6
p.text(ML + 36, gy, "Come leggere questa copertina", 30, "sans", True, OLIVE)
gy += 48
for ln in glines:
    p.text(ML + 36, gy, ln, 40, "serif", False, INK)
    gy += int(40 * 1.45)
y = y - 44 + box_h + 20
assert y < 2540, y
footer(p, 1)
p.save(os.path.join(OUT, "p1-copertina.svg"))

# ---------------- P2-P7: two items per page ----------------
PAIRS = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, 11)]
for pi, (ia, ib) in enumerate(PAIRS):
    p = Page(W, H)
    p.text(ML, 150, "La Lucerna", 64, "serif", True, INK)
    p.text(MR, 150, "COVER · 19–25 ottobre 2026", 30, "sans", False, GREY, "end")
    p.hline(ML, MR, 185, GOLD, 2.5)
    y = 300
    for item in (ITEMS[ia], ITEMS[ib]):
        p.text(ML, y, f"{LABEL[item['source_lang']]}", 34, "sans", True, OLIVE)
        y += 84  # headline 64px: ink top ≈ baseline-48 → 24px+ clear of the tag
        y = p.para(ML, y, item["headline"], 64, "serif", True, INK, CW, 1.28)
        y += 14
        y = p.para(ML, y, item["excerpt"], 44, "serif", False, INK, CW, 1.45)
        y += 20
        # explanation box (fill only, drawn before its text)
        expl_lines = wrap(EXPL[item["source_lang"]], "serif", False, 40, CW - 72)
        box_h = len(expl_lines) * int(40 * 1.45) + 56
        p.rect(ML, y - 44, CW, box_h, fill=BOX)
        p.rect(ML, y - 44, 10, box_h, fill=GOLD)
        ey = y + 6
        p.text(ML + 36, ey, "Spiegazione", 30, "sans", True, OLIVE)
        ey += 48
        for ln in expl_lines:
            p.text(ML + 36, ey, ln, 40, "serif", False, INK)
            ey += int(40 * 1.45)
        y = y - 44 + box_h + 110
        if item is ITEMS[ia]:
            p.hline(ML, MR, y - 48, LINE, 1.0)
    assert y < 2540, (pi, y)
    footer(p, pi + 2)
    p.save(os.path.join(OUT, f"p{pi + 2}-prime.svg"))

# ---------------- P8: the 12 core papers at a glance ----------------
p = Page(W, H)
y = masthead_block(p, 110)
p.hline(ML, MR, y + 10, GOLD, 2.5)
y += 90
y = p.para(ML, y, "I dodici settimanali della settimana", 72, "serif", True, OLIVE, CW, 1.25)
y += 16
y = p.para(ML, y, "Le edizioni principali di questa settimana, una per ogni lingua, con la loro prima pagina.",
           40, "serif", False, INK, CW, 1.45)
y += 36
for item in ITEMS:
    p.text(ML, y, f"{item['masthead']} · VOL.{item['vol']}", 32, "sans", True, OLIVE)
    y += 48
    y = p.para(ML, y, item["headline"], 44, "serif", True, INK, CW, 1.32)
    y += 26
assert y < 2540, y
footer(p, 8)
p.save(os.path.join(OUT, "p8-settimanali.svg"))
print("built 8 SVGs in", OUT)
