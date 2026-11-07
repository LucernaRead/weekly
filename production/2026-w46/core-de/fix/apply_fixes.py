# -*- coding: utf-8 -*-
"""W46 DE-family Round 1 fix worker: source-only edits, assertion-checked.
Each edit: (build-dir key, relative file, old, new, expected count, tag).
No rendered SVG/PDF is touched here; kinsoku_patch.py (svglib wrap) +
re-render follow. ABSTRACT.txt rewrites are handled separately below
with their own assertions.
Build keys: core = frozen core build; others = fan-out build copies.
"""
import os, sys

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HF = os.path.join(ROOT, "hidden_files")
BUILDS = {
    "core": "weekly-report-w46-de-build",
    "en": "weekly-report-w46-de-en-build",
    "es": "weekly-report-w46-de-es-build",
    "fr": "weekly-report-w46-de-fr-build",
    "it": "weekly-report-w46-de-it-build",
    "ja": "weekly-report-w46-de-ja-build",
    "ko": "weekly-report-w46-de-ko-build",
    "nl": "weekly-report-w46-de-nl-build",
    "pt": "weekly-report-w46-de-pt-build",
    "ru": "weekly-report-w46-de-ru-build",
    "zh-cn": "weekly-report-w46-de-zh-cn-build",
    "zh-tw": "weekly-report-w46-de-zh-tw-build",
}
ALL = list(BUILDS)
EDITS = []
def E(key, rel, old, new, exp, tag):
    EDITS.append((key, rel, old, new, exp, tag))

# ---- D-CORE-1: P4 caption, all 12 build dirs (frozen core German) ----
OLD_CAP = "Die Nationalelf spielt in dieser Woche in Belgrad und Berlin."
NEW_CAP = "Die Nationalelf spielt in dieser Woche in Belgrad — am Montag danach in Berlin."
for k in ALL:
    E(k, "content34.py", OLD_CAP, NEW_CAP, 1, "D-CORE-1")

# ---- D-TOOLBOX: present-passive glosses, 6 editions, content7.py ----
E("en", "content7.py", "Es wird gespielt. = It will be played", "Es wird gespielt. = It is played", 1, "D-TOOLBOX-en")
E("es", "content7.py", "Es wird gespielt. = Se jugará", "Es wird gespielt. = Se juega", 1, "D-TOOLBOX-es")
E("fr", "content7.py", "Es wird gespielt. = Il sera joué", "Es wird gespielt. = Il est joué", 1, "D-TOOLBOX-fr")
E("it", "content7.py", "Es wird gespielt. = Si giocherà", "Es wird gespielt. = Si gioca", 1, "D-TOOLBOX-it")
E("pt", "content7.py", "Es wird gespielt. = Vai ser jogado", "Es wird gespielt. = Joga-se", 1, "D-TOOLBOX-pt")
E("ru", "content7.py", "Es wird gespielt. = Будет сыграно", "Es wird gespielt. = Играется", 1, "D-TOOLBOX-ru")

# ---- D-IT-1: noun gloss, IT only ----
E("it", "content34.py", "das Geschnatter = starnazzare", "das Geschnatter = lo starnazzare", 1, "D-IT-1")

# ---- D-NL-1 + M-2 (NL): full P6 gloss with headwords ----
E("nl", "content56.py",
  "gedenken = herdenken · Kranzniederlegung = krans · stille Tag = stille dag · verbondenheid · verzoening.",
  "gedenken = herdenken · die Kranzniederlegung = kranslegging · der stille Tag = stille dag · die Verbundenheit = verbondenheid · die Versöhnung = verzoening.",
  1, "D-NL-1")

# ---- D-RU-1: full German definition, RU only ----
E("ru", "content7.py",
  "«das Geisterspiel» (Seite 4): Spiel ohne Zuschauer. Матч-призрак.",
  "«das Geisterspiel» (Seite 4): ein Spiel ohne Zuschauer im Stadion. Матч-призрак.",
  1, "D-RU-1")

# ---- M-1: short reader-language glosses on DER WERKZEUGKASTEN (measured to fit) ----
E("es", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · Útiles"', 1, "M-1-es")
E("fr", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · Outils"', 1, "M-1-fr")
E("it", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · Attrezzi"', 1, "M-1-it")
E("nl", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · Werktuig"', 1, "M-1-nl")
E("pt", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · Caixa"', 1, "M-1-pt")
E("ru", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · Ящик"', 1, "M-1-ru")
E("ja", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · 道具箱"', 1, "M-1-ja")
E("ko", "content7.py", '"DER WERKZEUGKASTEN"', '"DER WERKZEUGKASTEN · 도구 상자"', 1, "M-1-ko")
# RU P1: full gloss fits at 382px (bare form was load-bearing only for the longer Содержание form)
E("ru", "content12.py", '"IN DIESER AUSGABE"', '"IN DIESER AUSGABE · В номере"', 1, "M-1-ru-P1")

# ---- M-2: full Kranzniederlegung glosses (P8 key-97 forms, gloss-sized) ----
E("es", "content56.py", "Kranzniederlegung = ofrenda", "Kranzniederlegung = ofrenda floral", 1, "M-2-es")
E("fr", "content56.py", "Kranzniederlegung = gerbe", "Kranzniederlegung = dépôt de gerbe", 1, "M-2-fr")
E("it", "content56.py", "Kranzniederlegung = corona", "Kranzniederlegung = deposizione di corone", 1, "M-2-it")
E("pt", "content56.py", "Kranzniederlegung = coroa", "Kranzniederlegung = deposição de coroas", 1, "M-2-pt")
E("ru", "content56.py", "Kranzniederlegung = венок", "Kranzniederlegung = возложение венков", 1, "M-2-ru")

# ---- M-2/M-1 gloss-fit accommodation: P6-main flow ends y=1062 (bottom 1080) in
# all editions; the mandated 5-line gloss adds 29.7px and overflows by 11.7px.
# Recover 22px with invisible spacing only (no text change): final German para
# gap 10->0 and P6 gloss-box gap 12->0, in the 6 affected editions. ----
FINAL_PARA = "Zwei Themen, ein Muster: Gedenken und Energiepolitik betreffen fast jeden Haushalt. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter."
for k in ["es", "fr", "it", "pt", "ru", "nl"]:
    E(k, "content56.py", 'f.para("' + FINAL_PARA + '")', 'f.para("' + FINAL_PARA + '", gap=0)', 1, "M-2-fit-para-" + k)
# gloss gap=0: append , gap=0 to the P6 f.gloss call by targeting the new gloss tail
E("es", "content56.py", "Versöhnung = reconciliación.\")", "Versöhnung = reconciliación.\", gap=0)", 1, "M-2-fit-gloss-es")
E("fr", "content56.py", "Versöhnung = réconciliation.\")", "Versöhnung = réconciliation.\", gap=0)", 1, "M-2-fit-gloss-fr")
E("it", "content56.py", "Versöhnung = riconciliazione.\")", "Versöhnung = riconciliazione.\", gap=0)", 1, "M-2-fit-gloss-it")
E("pt", "content56.py", "Versöhnung = reconciliação.\")", "Versöhnung = reconciliação.\", gap=0)", 1, "M-2-fit-gloss-pt")
E("ru", "content56.py", "Versöhnung = примирение.\")", "Versöhnung = примирение.\", gap=0)", 1, "M-2-fit-gloss-ru")
E("nl", "content56.py", "die Versöhnung = verzoening.\")", "die Versöhnung = verzoening.\", gap=0)", 1, "M-2-fit-gloss-nl")

# ---- M-3: restore full UND SIE? invitations (P3/P4/P5) in es/fr/it/nl/pt/ru.
# Old strings occur 2x per file (eh height formula + rendered para); both updated.
# P2 invitations already match the EN/core one-question pattern; only PT address
# form changes there (see D-PT-1). ----
M3 = {
 ("es", "content34.py", "¿Hiciste un farolillo? ¡Escribe dos frases en alemán!",
  "¿Hiciste un farolillo? ¿Qué canciones cantan los niños en tu país? ¡Escribe dos frases en alemán!"),
 ("es", "content34.py", "¿Fútbol o fútbol americano? ¿Quién gana? ¡Dos frases!",
  "¿Fútbol o fútbol americano? ¿Quién gana en Belgrado? ¡Escribe dos frases en alemán!"),
 ("es", "content56.py", "¿Un farolillo de niño? ¿Tu canción? ¡Dos frases!",
  "¿Hiciste un farolillo de niño? ¿Qué canción cantas en noviembre? ¡Escribe dos frases en alemán!"),
 ("fr", "content34.py", "Tu as fait une lanterne ? Écris deux phrases en allemand !",
  "Tu as fait une lanterne ? Quelles chansons chantent les enfants dans ton pays ? Écris deux phrases en allemand !"),
 ("fr", "content34.py", "Foot ou foot US ? Qui gagne ? Deux phrases en allemand !",
  "Foot ou foot US ? Qui gagne à Belgrade ? Écris deux phrases en allemand !"),
 ("fr", "content56.py", "Une lanterne enfant ? Ta chanson ? Deux phrases en allemand !",
  "As-tu fait une lanterne enfant ? Quelle chanson chantes-tu en novembre ? Écris deux phrases en allemand !"),
 ("it", "content34.py", "Hai fatto una lanterna? Scrivi due frasi in tedesco!",
  "Hai fatto una lanterna? Quali canzoni cantano i bambini nel tuo paese? Scrivi due frasi in tedesco!"),
 ("it", "content34.py", "Calcio o football americano? Chi vince? Due frasi!",
  "Calcio o football americano? Chi vince a Belgrado? Scrivi due frasi in tedesco!"),
 ("it", "content56.py", "Una lanterna da bambino? La tua canzone? Due frasi!",
  "Hai fatto una lanterna da bambino? Quale canzone canti a novembre? Scrivi due frasi in tedesco!"),
 ("nl", "content34.py", "Heb je een lantaarn gemaakt? Twee Duitse zinnen!",
  "Heb je een lantaarn gemaakt? Welke liedjes zingen kinderen in jouw land? Schrijf twee Duitse zinnen!"),
 ("nl", "content34.py", "Voetbal of American football? Wie wint? Twee zinnen!",
  "Voetbal of American football? Wie wint er in Belgrado? Schrijf twee Duitse zinnen!"),
 ("nl", "content56.py", "Een lantaarn als kind? Jouw lied? Twee zinnen!",
  "Heb je als kind een lantaarn gemaakt? Welk lied zing jij in november? Schrijf twee Duitse zinnen!"),
 ("pt", "content34.py", "Fizeste uma lanterna? Escreve duas frases em alemão!",
  "Fez uma lanterna? Que canções cantam as crianças no seu país? Escreva duas frases em alemão!"),
 ("pt", "content34.py", "Futebol ou futebol americano? Quem ganha? Duas frases!",
  "Futebol ou futebol americano? Quem ganha em Belgrado? Escreva duas frases em alemão!"),
 ("pt", "content56.py", "Uma lanterna em criança? A tua canção? Duas frases!",
  "Fez uma lanterna em criança? Que canção canta em novembro? Escreva duas frases em alemão!"),
 ("ru", "content34.py", "Вы делали фонарик? Напишите два предложения!",
  "Вы делали фонарик? Какие песни поют дети в вашей стране? Напишите два предложения!"),
 ("ru", "content34.py", "Футбол или американский футбол? Кто победит? Два предложения!",
  "Футбол или американский футбол? Кто победит в Белграде? Напишите два предложения!"),
 ("ru", "content56.py", "Фонарик в детстве? Ваша песня? Два предложения!",
  "Вы делали фонарик в детстве? Какую песню вы поёте в ноябре? Напишите два предложения!"),
}
for k, rel, old, new in sorted(M3):
    E(k, rel, old, new, 2, "M-3")

# ---- M-4: normalize E-section translation register (one edit per edition) ----
E("ja", "content8.py", "水曜日にランタンを作ります。", "水曜日にランタンを作る。", 1, "M-4-ja")
E("ko", "content8.py", "카니발은 11시 11분에 쾰른에서 개막한다.", "카니발은 11시 11분에 쾰른에서 개막합니다.", 1, "M-4-ko")

# ---- T-1: ZH-TW P8 band separator ----
E("zh-tw", "content8.py",
  "Alle Antworten unten auf dieser Seite 答案在本版下方",
  "Alle Antworten unten auf dieser Seite — 答案在本版下方", 1, "T-1")

# ---- D-PT-1: normalize PT to você-form throughout (M-3 PT strings above
# already use você; these are the remaining tu-form headers/instructions).
# The readers'-corner disclosure "Enviem-nos as vossas" (plural address to
# all readers, internally consistent Enviem+vossas) is deliberately retained.
# ----
E("pt", "content12.py", "Carnaval ou São Martinho? Escreve duas frases em alemão!",
  "Carnaval ou São Martinho? Escreva duas frases em alemão!", 2, "D-PT-1-P2")
E("pt", "content12.py", "Lê a primeira página e escolhe a resposta certa · Respostas na página 8",
  "Leia a primeira página e escolha a resposta certa · Respostas na página 8", 1, "D-PT-1-quizsub")
E("pt", "content12.py", "Lê o artigo da página 2 e completa as horas.",
  "Leia o artigo da página 2 e complete as horas.", 1, "D-PT-1-b1")
E("pt", "content12.py", "Reescreve no Perfekt (pretérito perfeito).",
  "Reescreva no Perfekt (pretérito perfeito).", 1, "D-PT-1-b2")
E("pt", "content12.py", "Lê o artigo da página 2 e escolhe a resposta certa.",
  "Leia o artigo da página 2 e escolha a resposta certa.", 1, "D-PT-1-b3")
E("pt", "content34.py", "Lê o artigo da página 3. Verdadeiro ou falso?",
  "Leia o artigo da página 3. Verdadeiro ou falso?", 1, "D-PT-1-b4")
E("pt", "content34.py", "Completa com as palavras do quadro.",
  "Complete com as palavras do quadro.", 1, "D-PT-1-b5")
E("pt", "content34.py", "Escolhe a resposta certa.",
  "Escolha a resposta certa.", 1, "D-PT-1-b6")
E("pt", "content34.py", "Lê o artigo da página 4 e escolhe a resposta certa.",
  "Leia o artigo da página 4 e escolha a resposta certa.", 1, "D-PT-1-b7")
E("pt", "content34.py", "Completa com o comparativo (a palavra entre parênteses está no positivo).",
  "Complete com o comparativo (a palavra entre parênteses está no positivo).", 1, "D-PT-1-b8")
E("pt", "content34.py", "Olha para o calendário acima e escolhe a resposta certa.",
  "Olhe para o calendário acima e escolha a resposta certa.", 1, "D-PT-1-b9")
E("pt", "content56.py", "Lê o artigo da página 5 e escolhe a resposta certa.",
  "Leia o artigo da página 5 e escolha a resposta certa.", 1, "D-PT-1-b10")
E("pt", "content56.py", "Junta as duas frases com weil (o verbo vai para o fim).",
  "Junte as duas frases com weil (o verbo vai para o fim).", 1, "D-PT-1-b11")
E("pt", "content56.py", "Usa o gráfico de exercício acima.",
  "Use o gráfico de exercício acima.", 1, "D-PT-1-b12")
E("pt", "content56.py", "Lê o artigo da página 6.",
  "Leia o artigo da página 6.", 1, "D-PT-1-b13")
E("pt", "content56.py", "Completa com a forma entre parênteses.",
  "Complete com a forma entre parênteses.", 1, "D-PT-1-b14")
E("pt", "content7.py", "corrige-os primeiro, depois verifica",
  "corrija-os primeiro, depois verifique", 1, "D-PT-1-clinic")
E("pt", "content8.py", "(traduz para português)", "(traduza para português)", 3, "D-PT-1-p8a")
E("pt", "content8.py", "(traduz para alemão)", "(traduza para alemão)", 1, "D-PT-1-p8b")
E("pt", "content8.py",
  "Escreve em alemão, 80–100 palavras: «A minha semana de novembro». Diz o que fazes, que jogos vês e com quem — e acrescenta uma frase sobre o dia de São Martinho ou o dia de recordação.",
  "Escreva em alemão, 80–100 palavras: «A minha semana de novembro». Diga o que faz, que jogos vê e com quem — e acrescente uma frase sobre o dia de São Martinho ou o dia de recordação.",
  1, "D-PT-1-writing")

fails = 0
for key, rel, old, new, exp, tag in EDITS:
    path = os.path.join(HF, BUILDS[key], rel)
    txt = open(path, encoding="utf-8").read()
    n = txt.count(old)
    if n != exp:
        print(f"FAIL {tag} {key}/{rel}: found {n}, expected {exp}: {old!r}")
        fails += 1
        continue
    open(path, "w", encoding="utf-8").write(txt.replace(old, new))
    print(f"OK   {tag} {key}/{rel}: {old[:60]!r} -> {new[:60]!r}")

# ---- D-ABSTRACT: rewrite closings to practice framing (coordinator ruling:
# user 2026-10-28 rule governs over SOP §9 example). Only the closing is
# replaced; topics/levels/counts kept verbatim. Core dir carries the zh-cn
# abstract (duplicate dir) and is rewritten identically. ----
ABSTRACTS = {
 # (old tail incl. the exercise-count phrase, new tail) — the count phrase
 # is part of the replaced tail so the new closing never duplicates it.
 "core": ("150 道练习，适合学德语的读者通过德国新闻学德语。",
          "150 道以本周话题为素材的练习。"),
 "zh-cn": ("150 道练习，适合学德语的读者通过德国新闻学德语。",
           "150 道以本周话题为素材的练习。"),
 "zh-tw": ("150 道練習，適合學德語的讀者通過德國新聞學德語。",
           "150 道以本週話題為素材的練習。"),
 "en": ("150 exercises, for learners who want to learn German by reading real German news.",
        "150 exercises on this week's topics."),
 "es": ("150 ejercicios, para aprender alemán leyendo noticias alemanas reales.",
        "150 ejercicios sobre los temas de esta semana."),
 "fr": ("150 exercices, pour apprendre l'allemand en lisant les vraies nouvelles allemandes.",
        "150 exercices sur les sujets de cette semaine."),
 "it": ("150 esercizi, per imparare il tedesco leggendo vere notizie tedesche.",
        "150 esercizi sui temi di questa settimana."),
 "ja": ("150問の練習問題。本物のドイツのニュースでドイツ語を学ぶ読者のために。",
        "今週の話題を素材にした150問の練習問題。"),
 "ko": ("연습문제 150개. 진짜 독일 뉴스로 독일어를 배우는 독자를 위해.",
        "이번 주 화제를 소재로 한 연습문제 150개."),
 "nl": ("150 oefeningen, om Duits te leren door echt Duits nieuws te lezen.",
        "150 oefeningen over de onderwerpen van deze week."),
 "pt": ("150 exercícios, para aprender alemão a ler notícias alemãs reais.",
        "150 exercícios sobre os temas desta semana."),
 "ru": ("150 упражнений, для тех, кто учит немецкий по настоящим немецким новостям.",
        "150 упражнений по темам этой недели."),
}
EDDIR = {
 "core": "weekly-report-w46-de-core", "en": "weekly-report-w46-de-en",
 "es": "weekly-report-w46-de-es", "fr": "weekly-report-w46-de-fr",
 "it": "weekly-report-w46-de-it", "ja": "weekly-report-w46-de-ja",
 "ko": "weekly-report-w46-de-ko", "nl": "weekly-report-w46-de-nl",
 "pt": "weekly-report-w46-de-pt", "ru": "weekly-report-w46-de-ru",
 "zh-cn": "weekly-report-w46-de-zh-cn", "zh-tw": "weekly-report-w46-de-zh-tw",
}
for key, (old_close, new_close) in ABSTRACTS.items():
    p = os.path.join(ROOT, "files", EDDIR[key], "ABSTRACT.txt")
    txt = open(p, encoding="utf-8").read()
    assert txt.count(old_close) == 1, (key, txt.count(old_close), txt[-120:])
    new = txt.replace(old_close, new_close)
    assert new.count("\n") == 1 and new.endswith("\n"), (key, repr(new[-30:]))
    assert '"' not in new, key
    open(p, "w", encoding="utf-8").write(new)
    print(f"OK   D-ABSTRACT {key}: {old_close[:40]!r} -> {new_close[:40]!r}")

print("FAILURES:", fails)
sys.exit(1 if fails else 0)
