# -*- coding: utf-8 -*-
"""W45 weekly cover, reader language GERMAN. 8 pages, 1950x2700.
Headlines/excerpts copied verbatim from cover-backfill/headlines-w45.json.
Explanations in German, traceable to headline+excerpt only.
Cover itself carries NO vol number (COVER mark instead); P8 lists each
core paper's own VOL (FR VOL.3, all others VOL.2, per task).
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

# German-language names for the source languages (from tables.json de column
# T_FNOUN forms, lowercased to sentence case; zh split vereinfacht/traditionell).
DE_NAME = {"en": "Englisch", "de": "Deutsch", "fr": "Französisch",
           "es": "Spanisch", "it": "Italienisch", "pt": "Portugiesisch",
           "nl": "Niederländisch", "ru": "Russisch", "ja": "Japanisch",
           "ko": "Koreanisch", "zh-cn": "Chinesisch (vereinfacht)",
           "zh-tw": "Chinesisch (traditionell)"}
FAMILY = {"en": "Noto Serif CJK SC", "de": "Noto Serif CJK SC", "fr": "Noto Serif CJK SC",
          "es": "Noto Serif CJK SC", "it": "Noto Serif CJK SC", "pt": "Noto Serif CJK SC",
          "nl": "Noto Serif CJK SC", "ru": "Noto Serif CJK SC",
          "ja": "Noto Serif CJK JP", "ko": "Noto Serif CJK KR",
          "zh-cn": "Noto Serif CJK SC", "zh-tw": "Noto Serif CJK TC"}

EXPLAIN = {
 "en": "Die Vereinigten Staaten wählen bei einer Zwischenwahl: Alle Sitze im Repräsentantenhaus, etwa ein Drittel der Senatssitze und Gouverneursposten in vielen Bundesstaaten stehen zur Wahl.",
 "de": "Eine Woche voller Fußball: Champions League am Dienstag und Mittwoch, Europa League am Donnerstag, und am Freitag beginnt der 9. Spieltag der Bundesliga — mit Bayern bei Atlético Madrid und Stuttgart bei Galatasaray am Dienstag.",
 "fr": "Nach den Allerheiligenferien kehren die Schüler in Frankreich in die Schule zurück, und die Woche endet mit drei Endspielen am Wochenende des 7. und 8. November — darunter die Endspiele des Rolex Paris Masters in Nanterre am Sonntag.",
 "es": "Die Listen sind bereits eingereicht, jetzt schreiben die Parteien ihre Programme: Am Sonntag, dem 29. November, wählt Spanien bei Parlamentswahlen, bei denen das Thema Wohnen die Kampagne entscheiden soll.",
 "it": "Am Montag, dem 2. November, kommt die erste echte Kälte der Saison nach Italien, mit Regen an der Adriaküste und leichtem Schnee in den Bergen; der November soll kälter als im Durchschnitt werden — eine Wahrscheinlichkeit, keine Gewissheit.",
 "pt": "Die Woche läuft vom Feiertag Finados am Montag, dem 2. November, bis zum ersten Tag des Enem am Sonntag, dem 8. November: eine Woche aus Ausruhen, Wiederholen und Prüfung.",
 "nl": "Vom 2. bis 8. November ist in den Niederlanden Klimaatweek: Gemeinden im ganzen Land organisieren Aktionen — Bäume pflanzen, Energie sparen, das Fahrrad statt des Autos nehmen — und jeder kann mitmachen.",
 "ru": "Eine ungewöhnliche Woche in Russland: Am Montag und Dienstag wird gearbeitet, am Mittwoch, dem 4. November, ist frei — ein freier Tag mitten in der Arbeitswoche.",
 "ja": "Der Kulturtag fällt auf Dienstag, den 3. November, einen Feiertag, an dem Schulen und Firmen geschlossen sind und im ganzen Land Kulturveranstaltungen stattfinden.",
 "ko": "Die Woche vom 2. bis 8. November markiert den Winteranfang: Samstag, der 7. November, ist Ip-dong, der erste der 24 Sonnenabschnitte, der zum Winter gehört.",
 "zh-cn": "Die Double-11-Verkaufsphase läuft bereits: Ware ist seit Mitte Oktober im Verkauf und bleibt bis zum 13. November erhältlich — und der Winter naht.",
 "zh-tw": "Die Hong Kong FinTech Week x StartmeupHK 2026 eröffnet am Montag, dem 2. November, in Hongkong und läuft fünf Tage bis Freitag, den 6. November, mit Hauptkonferenz, Ausstellung und über 100 Gemeinschaftsveranstaltungen sowie voraussichtlich über 45.000 Teilnehmenden.",
}
assert set(EXPLAIN) == {i["source_lang"] for i in ITEMS}

W, H = 1950, 2700
MX, CW = 130, 1690
FOOT_Y = 2624

def new_page():
    return Page(W, H)

def header(p, label):
    p.text(975, 128, label, 30, "sans", False, GREY, anchor="middle")

def footer(p, num):
    p.hline(MX, MX + CW, 2570, LINE, 1.2)
    p.text(MX, FOOT_Y, "Die Lucerna  ·  COVER  ·  2.-8. November 2026", 28, "sans", False, GREY)
    p.text(MX + CW, FOOT_Y, num, 28, "sans", False, GREY, anchor="end")

def para(p, x, y, s, size, kind, bold, fill, max_w, lh, family=None):
    for ln in wrap(s, kind, bold, size, max_w):
        p.text(x, y, ln, size, kind, bold, fill, family=family)
        y += size * lh
    return y

def tag_of(it):
    lang = it["source_lang"]
    return (DE_NAME[lang] + "  ·  " + LANGS[lang]["label"]).upper()

# ---------------- P1 ----------------
p = new_page()
header(p, "WOCHENCOVER  ·  2.-8. NOVEMBER 2026")
p.text(975, 330, "Die Lucerna", 168, "serif", True, INK, anchor="middle")
bw = text_w("C O V E R", "sans", True, 44) + 90
p.rect(975 - bw / 2, 385, bw, 78, fill=OLIVE, rx=10)
p.text(975, 440, "C O V E R", 44, "sans", True, PAPER, anchor="middle")
p.text(975, 560, "2.-8. November 2026", 52, "serif", False, OLIVE, anchor="middle")
p.hline(375, 1575, 620, GOLD, 3)
p.text(975, 740, "Zwölf Titelseiten, eine Woche", 84, "serif", True, INK, anchor="middle")
y = para(p, 220, 850, "Zwölf Zeitungen, zwölf Sprachen, eine Woche im November: Jede Schlagzeile unten öffnet ihre eigene Titelseite — in ihrer eigenen Sprache, mit einer kurzen Erläuterung auf Deutsch dazu, was sie sagt und warum sie ins Auge fällt.", 46, "serif", False, GREY, 1510, 1.45)
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
    header(p, "DIE LUCERNA  ·  COVER  ·  2.-8. NOVEMBER 2026")
    y = 210
    for idx in (a, b):
        it = ITEMS[idx]
        lang = it["source_lang"]
        p.text(MX, y, tag_of(it), 34, "sans", True, OLIVE)
        y += 64  # was 52: audit flagged tag ink touching headline ink (TEXTX)
        y = para(p, MX, y, it["headline"], 60, "serif", True, INK, CW, 1.28, family=FAMILY[lang])
        y += 30
        y = para(p, MX, y, it["excerpt"], 44, "serif", False, INK, CW, 1.5, family=FAMILY[lang])
        y += 34
        p.hline(MX, MX + 180, y, GOLD, 2.5)
        y += 48
        p.text(MX, y, "WAS DAS BEDEUTET", 30, "sans", True, OLIVE)
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
header(p, "DIE LUCERNA  ·  COVER  ·  2.-8. NOVEMBER 2026")
p.text(975, 300, "Die zwölf Zeitungen dieser Woche", 88, "serif", True, INK, anchor="middle")
p.text(975, 390, "Die zwölf Kernzeitungen hinter diesem Cover, in Reihenfolge.", 44, "serif", False, GREY, anchor="middle")
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
