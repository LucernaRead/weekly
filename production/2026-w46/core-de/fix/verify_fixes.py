# -*- coding: utf-8 -*-
"""Verify every Round 1 fix on the FINAL shipped SVGs + ABSTRACT.txt files.
Exit 0 = all checks pass. Prints one line per check."""
import os, re, html, sys

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(ROOT, "files")
PAGES = ["p1-front.svg", "p2-leben.svg", "p3-kultur.svg", "p4-sport.svg",
         "p5-jugend.svg", "p6-vertiefung.svg", "p7-sprache.svg", "p8-uebungen.svg"]
ED = {"core": "weekly-report-w46-de-core", "en": "weekly-report-w46-de-en",
      "es": "weekly-report-w46-de-es", "fr": "weekly-report-w46-de-fr",
      "it": "weekly-report-w46-de-it", "ja": "weekly-report-w46-de-ja",
      "ko": "weekly-report-w46-de-ko", "nl": "weekly-report-w46-de-nl",
      "pt": "weekly-report-w46-de-pt", "ru": "weekly-report-w46-de-ru",
      "zh-cn": "weekly-report-w46-de-zh-cn", "zh-tw": "weekly-report-w46-de-zh-tw"}

def texts_of(path):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r'data:image[^"\']*', 'IMG', s)
    return [html.unescape(re.sub(r'<[^>]+>', '', c)) for c in re.findall(r'<text[^>]*>(.*?)</text>', s, re.S)]

def joined(ed, pages=None):
    out = []
    for pg in (pages or PAGES):
        out.extend(texts_of(os.path.join(FILES, ED[ed], "svg", pg)))
    return " ".join(out)

def raw(ed, pg):
    return open(os.path.join(FILES, ED[ed], "svg", pg), encoding="utf-8").read()

CHECKS = []
def check(tag, ok, detail=""):
    CHECKS.append((tag, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + tag + ((" :: " + detail) if detail and not ok else ""))

NEW_CAP = "Die Nationalelf spielt in dieser Woche in Belgrad — am Montag danach in Berlin."
OLD_CAP = "Die Nationalelf spielt in dieser Woche in Belgrad und Berlin."
for ed in ED:
    j4 = joined(ed, ["p4-sport.svg"])
    check("D-CORE-1 new caption [%s]" % ed, NEW_CAP in j4)
    check("D-CORE-1 old caption absent [%s]" % ed, OLD_CAP not in joined(ed))
    check("D-CORE-1 P1 caption fact [%s]" % ed, "Am Montag danach kommen die Niederlande nach Berlin" in joined(ed, ["p1-front.svg"]))
    check("D-CORE-1 P4 article fact [%s]" % ed, "16. November" in j4)

OPEN_END = set("（(［｛〈《「『")
CLOSE_START = set("。、，．！？：；）」』】}]),.:;!?")
LONE = {"。", ")", "）", "(", "（", ","}
CJK_EDS = ["core", "zh-cn", "zh-tw", "ja", "ko"]
for ed in ED:
    lone, ks = [], []
    for pg in PAGES:
        for t in texts_of(os.path.join(FILES, ED[ed], "svg", pg)):
            st = t.strip()
            if st in LONE:
                lone.append("%s:%r" % (pg, st))
    check("LONE-PUNCT none [%s]" % ed, not lone, "; ".join(lone[:5]))
    # Kinsoku scan: proofreader's method covered the CJK editions only
    # (orphan-kinsoku-scan.txt lists de-core/ja/ko/zh-cn/zh-tw). Latin
    # editions were never kinsoku-scanned; their wraps are out of scope.
    if ed in CJK_EDS:
        for pg in PAGES:
            for t in texts_of(os.path.join(FILES, ED[ed], "svg", pg)):
                st = t.strip()
                if st:
                    if st[0] in CLOSE_START:
                        ks.append("%s START %r" % (pg, st[:30]))
                    if st[-1] in OPEN_END:
                        ks.append("%s END %r" % (pg, st[-30:]))
        check("KINSOKU 0 [%s]" % ed, not ks, "; ".join(ks[:5]))

TB = {"en": ("It is played", "It will be played"), "es": ("Se juega", "Se jugará"),
      "fr": ("Il est joué", "Il sera joué"), "it": ("Si gioca", "Si giocherà"),
      "pt": ("Joga-se", "Vai ser jogado"), "ru": ("Играется", "Будет сыграно")}
for ed, (new, old) in TB.items():
    j7 = joined(ed, ["p7-sprache.svg"])
    check("D-TOOLBOX [%s]" % ed, ("Es wird gespielt. = " + new) in j7 and old not in j7)
for ed, gloss in [("nl", "Er wordt gespeeld"), ("ja", "試合が行われる"), ("ko", "경기가 열린다")]:
    check("D-TOOLBOX control untouched [%s]" % ed, gloss in joined(ed, ["p7-sprache.svg"]))
check("D-TOOLBOX core gloss untouched", "比赛将进行（被动）" in joined("core", ["p7-sprache.svg"]))

check("D-IT-1", "das Geschnatter = lo starnazzare" in joined("it", ["p3-kultur.svg"])
      and "das Geschnatter = starnazzare" not in joined("it", ["p3-kultur.svg"]))
j6nl = joined("nl", ["p6-vertiefung.svg"])
check("D-NL-1", "die Verbundenheit = verbondenheid" in j6nl and "die Versöhnung = verzoening" in j6nl
      and "die Kranzniederlegung = kranslegging" in j6nl and "· verbondenheid · verzoening." not in j6nl)
check("D-RU-1", "ein Spiel ohne Zuschauer im Stadion. Матч-призрак." in joined("ru", ["p7-sprache.svg"])
      and ": Spiel ohne Zuschauer." not in joined("ru", ["p7-sprache.svg"]))

M1 = {"es": "Útiles", "fr": "Outils", "it": "Attrezzi", "nl": "Werktuig",
      "pt": "Caixa", "ru": "Ящик", "ja": "道具箱", "ko": "도구 상자"}
for ed, gloss in M1.items():
    check("M-1 toolbox gloss [%s]" % ed, ("DER WERKZEUGKASTEN · " + gloss) in joined(ed, ["p7-sprache.svg"]))
check("M-1 RU P1 gloss", "IN DIESER AUSGABE · В номере" in joined("ru", ["p1-front.svg"]))

M2 = {"es": "ofrenda floral", "fr": "dépôt de gerbe", "it": "deposizione di corone",
      "pt": "deposição de coroas", "ru": "возложение венков", "nl": "kranslegging"}
for ed, form in M2.items():
    j6 = joined(ed, ["p6-vertiefung.svg"])
    check("M-2 [%s]" % ed, ("Kranzniederlegung = " + form) in j6 or ("die Kranzniederlegung = " + form) in j6)
check("M-2 es bare absent", "Kranzniederlegung = ofrenda ·" not in joined("es", ["p6-vertiefung.svg"]))

M3Q = {"es": ["¿Qué canciones cantan los niños", "¿Quién gana en Belgrado", "¿Qué canción cantas"],
       "fr": ["Quelles chansons chantent", "Qui gagne à Belgrade", "Quelle chanson chantes-tu"],
       "it": ["Quali canzoni cantano", "Chi vince a Belgrado", "Quale canzone canti"],
       "nl": ["Welke liedjes zingen", "Wie wint er in Belgrado", "Welk lied zing jij"],
       "pt": ["Que canções cantam", "Quem ganha em Belgrado", "Que canção canta"],
       "ru": ["Какие песни поют", "Кто победит в Белграде", "Какую песню вы поёте"]}
M3OLD = {"es": "¿Tu canción?", "fr": "Ta chanson ?", "it": "La tua canzone?",
         "nl": "Jouw lied?", "pt": "A tua canção?", "ru": "Ваша песня?"}
for ed, frags in M3Q.items():
    j = joined(ed, ["p3-kultur.svg", "p4-sport.svg", "p5-jugend.svg"])
    check("M-3 Q2 restored [%s]" % ed, all(f in j for f in frags), str([f for f in frags if f not in j]))
    check("M-3 old fragment absent [%s]" % ed, M3OLD[ed] not in j)

_ja8 = joined("ja", ["p8-uebungen.svg"])
check("M-4 JA plain", "水曜日にランタンを" in _ja8 and "作る。" in _ja8
      and "作ります" not in joined("ja"))
check("M-4 KO polite", "개막합니다" in joined("ko", ["p8-uebungen.svg"])
      and "개막한다" not in joined("ko"))
check("T-1", "Alle Antworten unten auf dieser Seite — 答案在本版下方" in joined("zh-tw", ["p8-uebungen.svg"]))

jpt = joined("pt")
FORBIDDEN = ["Escreve ", "Fizeste", "Lê ", "Escolhe", "Reescreve", "Completa com",
             "Olha para", "Junta as", "Usa o gráfico", "(traduz para", "corrige-os",
             "A tua canção", "fazes", "vês", "acrescenta", "Diz o que", "tua canção",
             "Escreve duas", "Fizeste uma"]
for tok in FORBIDDEN:
    check("D-PT-1 absent %r" % tok, tok not in jpt)
for tok in ["Escreva duas frases", "Leia o artigo", "Escolha a resposta certa",
            "Reescreva", "Complete com", "Olhe para", "(traduza para português)",
            "(traduza para alemão)", "corrija-os", "Escreva em alemão", "Fez uma lanterna"]:
    check("D-PT-1 present %r" % tok, tok in jpt)
check("D-PT-1 disclosure retained", "Enviem-nos as vossas para VOL.4!" in jpt)

BANNED = {"core": "通过德国新闻学德语", "zh-cn": "通过德国新闻学德语", "zh-tw": "通過德國新聞學德語",
          "en": "learn German by reading", "es": "leyendo noticias alemanas",
          "fr": "en lisant les vraies nouvelles", "it": "leggendo vere notizie",
          "ja": "ニュースでドイツ語を学ぶ", "ko": "뉴스를 읽고 독일어를",
          "nl": "door echt Duits nieuws", "pt": "a ler notícias alemãs",
          "ru": "по настоящим немецким новостям"}
PRACTICE = {"core": "以本周话题为素材", "zh-cn": "以本周话题为素材", "zh-tw": "以本週話題為素材",
            "en": "exercises on this week's topics", "es": "ejercicios sobre los temas",
            "fr": "exercices sur les sujets", "it": "esercizi sui temi",
            "ja": "今週の話題を素材にした", "ko": "이번 주 화제를 소재로 한",
            "nl": "oefeningen over de onderwerpen", "pt": "exercícios sobre os temas",
            "ru": "упражнений по темам этой недели"}
for ed in ED:
    txt = open(os.path.join(FILES, ED[ed], "ABSTRACT.txt"), encoding="utf-8").read()
    check("D-ABSTRACT format [%s]" % ed, txt.count("\n") == 1 and txt.endswith("\n") and '"' not in txt)
    check("D-ABSTRACT practice [%s]" % ed, PRACTICE[ed] in txt and BANNED[ed] not in txt)

GOLDEN = ["Die Bundesliga pausiert — aber die Nationalmannschaft spielt.",
          "Um 11.11 Uhr beginnt in Köln die neue Karnevalssession.",
          "Sein Gedenktag ist der 11. November.",
          "Die Rucksäcke sind gepackt, die Pausenhöfe sind wieder laut.",
          "Der November ist dunkel, aber er ist nicht still: Er singt, leuchtet und feiert.",
          "Das Spiel ist ausverkauft, RTL überträgt live.",
          "Gedenken heißt hier: innehalten, erinnern — und für Frieden und Versöhnung einstehen.",
          "Am Sonntag ist es still im Land."]
for ed in ED:
    j = re.sub(r"\s+", " ", joined(ed))
    bad = [g for g in GOLDEN if j.count(g) != 2]
    check("GOLDEN 2x [%s]" % ed, not bad, str([g[:30] for g in bad]))

for ed in ED:
    r6 = raw(ed, "p6-vertiefung.svg")
    rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="#3e4c2a"', r6)
    bars = sorted(float(w) for x, y, w, h in rects if x == "535")
    check("P6 bars [%s]" % ed, bars == [340.0, 578.0, 782.0], str(bars))

fails = sum(1 for _, ok, _ in CHECKS if not ok)
print("\nTOTAL: %d checks, %d failures" % (len(CHECKS), fails))
sys.exit(1 if fails else 0)
