# -*- coding: utf-8 -*-
"""W46 IT-family Round-1 fix worker: apply all proofreader defects at source.
Every replacement is asserted (exact count). NEVER touches transform.py,
bslib4.py, svglib.py, render.py, run.py. Run once from this dir."""
import os, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HID = os.path.join(GOAL, "hidden_files")
BUILDS = {
    "core": "weekly-report-w46-it-build",
    "de": "weekly-report-w46-it-de-build",
    "en": "weekly-report-w46-it-en-build",
    "es": "weekly-report-w46-it-es-build",
    "fr": "weekly-report-w46-it-fr-build",
    "ja": "weekly-report-w46-it-ja-build",
    "ko": "weekly-report-w46-it-ko-build",
    "nl": "weekly-report-w46-it-nl-build",
    "pt": "weekly-report-w46-it-pt-build",
    "ru": "weekly-report-w46-it-ru-build",
    "zh-tw": "weekly-report-w46-it-zh-tw-build",
}
FW = "\uff1a"  # U+FF1A full-width colon

# (build, file, old, new, expected_count, defect_tag)
REPS = []
def R(build, f, old, new, n, tag):
    REPS.append((build, f, old, new, n, tag))

ALL = list(BUILDS)
# ---- D1: FESTIVAL cross-ref Pagina 5 -> Pagina 2 (all 11) ----
for b in ALL:
    R(b, "content12.py",
      "Il Festival dei Popoli si è chiuso domenica 8 novembre: 86 film a Firenze. (Pagina 5)",
      "Il Festival dei Popoli si è chiuso domenica 8 novembre: 86 film a Firenze. (Pagina 2)", 1, "D1")
# ---- D3: agreement (all 11) ----
for b in ALL:
    R(b, "content12.py",
      "Nello stesso weekend si sono chiusi il Forum Cultura di Milano, con più di 50 eventi, e si sono aperti la finale del Panettone e la Festa del Torrone.",
      "Nello stesso weekend si è chiuso il Forum Cultura di Milano, con più di 50 eventi, e si sono aperte la finale del Panettone e la Festa del Torrone.", 1, "D3")
# ---- D2 stems: add NON (all 11) ----
for b in ALL:
    R(b, "content34.py",
      "Le partite di domenica sera cominciano ___ di quelle di giovedì. (tardi)",
      "Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi)", 1, "D2-stem56")
    R(b, "content34.py",
      "Le partite di giovedì cominciano ___ di quelle di domenica. (presto)",
      "Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)", 1, "D2-stem57")
# ---- D2 notes per native ----
NOTES56 = {
    "core": ("周日的比赛晚于周四的：più tardi", "两场比赛都在 20.45 开始，周日的比赛并不比周四的晚：più tardi"),
    "de": ("Das Sonntagsspiel ist später als das Donnerstagsspiel: più tardi", "Beide Spiele beginnen um 20.45 Uhr: Das Sonntagsspiel ist nicht später als das Donnerstagsspiel: più tardi"),
    "en": ("Sunday's match is later than Thursday's: più tardi", "Both matches kick off at 20:45: Sunday's match is not later than Thursday's: più tardi"),
    "es": ("El partido del domingo es después que el del jueves: più tardi", "Los dos partidos empiezan a las 20.45: el partido del domingo no es más tarde que el del jueves: più tardi"),
    "fr": ("Le match de dimanche est plus tard que celui de jeudi : più tardi", "Les deux matches commencent à 20 h 45 : le match de dimanche n'est pas plus tard que celui de jeudi : più tardi"),
    "ja": ("日曜の試合は木曜より遅い：più tardi", "両試合とも20時45分開始：日曜の試合は木曜より遅くない：più tardi"),
    "ko": ("일요일 경기는 목요일보다 늦다: più tardi", "두 경기 모두 20시 45분에 시작한다: 일요일 경기는 목요일보다 늦지 않다: più tardi"),
    "nl": ("De zondagwedstrijd is later dan de donderdagwedstrijd: più tardi", "Beide wedstrijden beginnen om 20.45 uur: de zondagwedstrijd is niet later dan de donderdagwedstrijd: più tardi"),
    "pt": ("O jogo de domingo é mais tarde do que o de quinta: più tardi", "Os dois jogos começam às 20.45: o jogo de domingo não é mais tarde do que o de quinta: più tardi"),
    "ru": ("Воскресный матч позже матча четверга: più tardi", "Оба матча начинаются в 20.45: воскресный матч не позже матча четверга: più tardi"),
    "zh-tw": ("週日的比賽晚於週四的：più tardi", "兩場比賽都在 20.45 開始，週日的比賽並不比週四的晚：più tardi"),
}
NOTES57 = {
    "core": ("周四的比赛早于周日的：più presto", "两场比赛都在 20.45 开始，周四的比赛并不比周日的早：più presto"),
    "de": ("Das Donnerstagsspiel ist früher als das Sonntagsspiel: più presto", "Beide Spiele beginnen um 20.45 Uhr: Das Donnerstagsspiel ist nicht früher als das Sonntagsspiel: più presto"),
    "en": ("Thursday's match is earlier than Sunday's: più presto", "Both matches kick off at 20:45: Thursday's match is not earlier than Sunday's: più presto"),
    "es": ("El partido del jueves es antes que el del domingo: più presto", "Los dos partidos empiezan a las 20.45: el partido del jueves no es antes que el del domingo: più presto"),
    "fr": ("Le match de jeudi est plus tôt que celui de dimanche : più presto", "Les deux matches commencent à 20 h 45 : le match de jeudi n'est pas plus tôt que celui de dimanche : più presto"),
    "ja": ("木曜の試合は日曜より早い：più presto", "両試合とも20時45分開始：木曜の試合は日曜より早くない：più presto"),
    "ko": ("목요일 경기는 일요일보다 이르다: più presto", "두 경기 모두 20시 45분에 시작한다: 목요일 경기는 일요일보다 이르지 않다: più presto"),
    "nl": ("De donderdagwedstrijd is eerder dan de zondagwedstrijd: più presto", "Beide wedstrijden beginnen om 20.45 uur: de donderdagwedstrijd is niet eerder dan de zondagwedstrijd: più presto"),
    "pt": ("O jogo de quinta é mais cedo do que o de domingo: più presto", "Os dois jogos começam às 20.45: o jogo de quinta não é mais cedo do que o de domingo: più presto"),
    "ru": ("Матч четверга раньше воскресного: più presto", "Оба матча начинаются в 20.45: матч четверга не раньше воскресного: più presto"),
    "zh-tw": ("週四的比賽早於週日的：più presto", "兩場比賽都在 20.45 開始，週四的比賽並不比週日的早：più presto"),
}
for b, (old, new) in NOTES56.items():
    R(b, "content34.py", old, new, 1, "D2-note56")
for b, (old, new) in NOTES57.items():
    R(b, "content34.py", old, new, 1, "D2-note57")
# ---- Q1: invented 'finale a Perugia' -> verified Torrone/Cremona fact (all 11) ----
for b in ALL:
    R(b, "content7.py",
      "il sole torna, la finale è a Perugia.",
      "il sole torna, la Festa del Torrone è a Cremona.", 1, "Q1")
# ---- D5 core ----
R("core", "content8.py", "mandorle 杏仁", "mandorle = 杏仁", 1, "D5")
R("core", "content8.py", "quanto costa? 多少钱", "quanto costa? = 多少钱", 1, "D5")
R("core", "content8.py", "pagare con carta 刷卡", "pagare con carta = 刷卡", 1, "D5")
# ---- F1: full-width colon -> half-width in items 16-19 notes (8 editions) ----
F1_NOTES = [
    ("dividere" + FW + "Martino → divide", "dividere: Martino → divide"),
    ("assaggiare" + FW + "noi → assaggiamo", "assaggiare: noi → assaggiamo"),
    ("aprire" + FW + "le cantine → aprono", "aprire: le cantine → aprono"),
    ("mangiare" + FW + "noi → mangiamo", "mangiare: noi → mangiamo"),
]
for b in ["de", "en", "es", "fr", "ko", "nl", "pt", "ru"]:
    for old, new in F1_NOTES:
        R(b, "content12.py", old, new, 1, "F1")
R("ko", "content56.py", "빈칸 채우기" + FW + "manovra", "빈칸 채우기: manovra", 1, "F1-ko-header")
# ---- EN ----
R("en", "content12.py", "THE ITALIAN ITALIANS ARE READING", "THE ITALIAN THAT ITALIANS ARE READING", 1, "EN-strapline")
R("en", "content8.py", "The title sums up two cities, two sweets", "The title sums up two cities, two festivals", 1, "EN-132")
R("en", "content34.py", "Subject + essere + place", "Subject + essere + place + date", 1, "EN-44")
R("en", "content8.py", "Subject + essere + place", "Subject + essere + place + date", 1, "EN-134")
# ---- ES ----
R("es", "content8.py", "El mejor título: dos ciudades, dos dulces", "El mejor título: dos ciudades, dos fiestas", 1, "ES-132")
R("es", "content8.py", "La Festa del Torrone abre en Cremona", "La Festa del Torrone continúa en Cremona", 1, "ES-117")
# ---- FR ----
R("fr", "content8.py", "Le titre résume deux villes, deux douceurs", "Le titre résume deux villes, deux fêtes", 1, "FR-132")
# ---- KO ----
R("ko", "content56.py", "스크리토리ンチ타", "스크리토린치타", 4, "KO-katakana")
R("ko", "content8.py", "스크리토리ンチ타", "스크리토린치타", 2, "KO-katakana")
R("ko", "content34.py", "상자 안의 단어로 빈칸을 채우세요。", "상자 안의 단어로 빈칸을 채우세요.", 1, "KO-stop")
R("ko", "content56.py", "단순 미래 (futuro semplice)로 완성하세요。", "단순 미래 (futuro semplice)로 완성하세요.", 1, "KO-stop")
R("ko", "content8.py", "mandorle 아몬드", "mandorle = 아몬드", 1, "D5-ko")
# ---- NL ----
R("nl", "content12.py", "durare: l'estate → dura (hij)", "durare: l'estate → dura (zij)", 1, "NL-20")
R("nl", "content8.py", "mandorle: amandelen", "mandorle = amandelen", 1, "NL-146")
# ---- PT ----
R("pt", "content8.py", "O título resume duas cidades e dois doces", "O título resume duas cidades e duas festas", 1, "PT-132")
R("pt", "content7.py", "escrevam à redação", "escreve à redação", 2, "PT-register")
# ---- RU ----
R("ru", "content7.py", "Писем и лучших сочинений нет; обещание — VOL.4.",
   "К моменту сдачи номера писем и лучших сочинений нет; обещание — VOL.4.", 2, "RU-disclosure")
R("ru", "content34.py", "mandorle = миндаль (мн. ч.)", "mandorle = миндаль", 1, "RU-38")
# ---- ZH-TW ----
R("zh-tw", "content7.py", "未來時", "將來時", 3, "ZHTW-term")
R("zh-tw", "content12.py",
  "11 — 11月、聖馬丁節那天、週三（聖馬丁節，11 月 11 日週三）",
  "11 — 11月11日週三，聖馬丁節", 1, "ZHTW-orphan-P1")
R("zh-tw", "content56.py",
  "3. Venerdì: apre Eurochocolate（週五：巧克力節開幕）",
  "3. Venerdì: apre Eurochocolate（週五巧克力節開幕）", 1, "ZHTW-orphan-P5")
R("zh-tw", "content8.py", "mandorle 杏仁", "mandorle = 杏仁", 1, "D5-zhtw")
R("zh-tw", "content8.py", "quanto costa? 多少錢", "quanto costa? = 多少錢", 1, "D5-zhtw")
R("zh-tw", "content8.py", "pagare con carta 刷卡", "pagare con carta = 刷卡", 1, "D5-zhtw")

def main():
    failed = 0
    for build, f, old, new, n, tag in REPS:
        path = os.path.join(HID, BUILDS[build], f)
        txt = open(path, encoding="utf-8").read()
        c = txt.count(old)
        if c != n:
            print(f"FAIL {tag} {build}/{f}: found {c}, expected {n}: {old[:60]!r}")
            failed += 1
            continue
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
        print(f"OK {tag} {build}/{f} x{n}")
    print("TOTAL", len(REPS), "FAILED", failed)
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
