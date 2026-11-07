# -*- coding: utf-8 -*-
import re, os
from PIL import ImageFont
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ru-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-ru-it/svg")
W43 = os.path.join(GOAL, "files/weekly-report-ru-it/svg")

def elements(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<text\s+([^>]*)>(.*?)</text>", s, re.S):
        attrs, inner = m.group(1), re.sub(r"<[^>]+>", "", m.group(2)).strip()
        def a(n):
            mm = re.search(n + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else None
        out.append({"x": a("x"), "y": a("y"), "size": a("size"), "text": inner, "attrs": attrs})
    return out

def joined(path):
    return " ".join(e["text"] for e in elements(path))

print("== GOLDEN 8 (bare sentence, whitespace-normalized) ==")
quotes = [
 "Среда, 4 ноября, — выходной посреди рабочей недели",
 "Как жить неделю с праздником посреди недели",
 "Во вторник, 3 ноября, рабочий день короче на час",
 "В среду города устраивают ярмарки и концерты",
 "В воскресенье, 8 ноября, — три матча",
 "Сначала — список: что вам правда нужно",
 "Многие берут отпуск в четверг и в пятницу",
 "Пять дней — почти маленькие каникулы",
]
def norm(s):
    return re.sub(r"\s+", " ", s)
cj, ej = norm(joined(f"{CORE}/p7-yazyk.svg")), norm(joined(f"{ED}/p7-yazyk.svg"))
for q in quotes:
    print(f"  core x{cj.count(q)} ed x{ej.count(q)}: {q[:70]!r}")

print("== GLOSS ITEM COUNTS (split on ·) ==")
for label, bdir in [("core", os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-build")),
                    ("ed", os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-it-build"))]:
    total = []
    for f in ["content12.py", "content34.py", "content56.py"]:
        src = open(os.path.join(bdir, f), encoding="utf-8").read()
        # gloss("...") single-line calls
        for m in re.finditer(r'gloss\("([^"]*)"\)', src):
            items = [x for x in m.group(1).split("·")]
            total.append(len(items))
    print(f"  {label}: per-call={total} total={sum(total)} ncalls={len(total)}")

print("== MODEL WORD COUNT (P8 section H) ==")
# model text: Russian paragraph in P8; find it in content8 source (model var) and count
src = open(os.path.join(GOAL, "hidden_files/weekly-report-w45-ru-it-build/content8.py"), encoding="utf-8").read()
i = src.find("84")
print("  content8 mentions of 84:", [src[max(0, m.start()-80):m.start()+80].replace("\n", " ") for m in re.finditer(r"84", src)][:5])
# find model paragraph: search for a long Russian string literal in content8
for m in re.finditer(r'"([^"]*[\u0400-\u04FF][^"]{100,})"', src):
    t = m.group(1)
    if len(t) > 150:
        print(f"  candidate model len={len(t)} words={len(t.split())}: {t[:120]!r}")

print("== CONTENTS 'все' tag + bilingual heads ==")
for e in elements(f"{ED}/p1-pervaya.svg"):
    if "Стр. 8" in e["text"] or "все" in e["text"]:
        print(f"  P1: {e['text'][:120]!r}")
heads = ["НЕДЕЛЯ В ЦИФРАХ · In cifre", "В ЭТОМ НОМЕРЕ · Sommario", "СЛОВО НЕДЕЛИ · La parola",
         "БЛИЦ-ВИКТОРИНА · Quiz lampo", "КОРОТКО · In breve", "ЗА И ПРОТИВ · Pro e contro",
         "БОЛЬШОЙ РАЗБОР · Analisi", "МОЛОДЁЖЬ · Giovani", "А ВЫ? · E tu?"]
alled = []
for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]:
    alled += [e["text"] for e in elements(f"{ED}/{p}.svg")]
for h in heads:
    print(f"  {h!r}: in_ed={h in alled}")

print("== FULL-WIDTH PARENS + CJK in ed ==")
for p in ["p1-pervaya", "p2-zhizn", "p3-kultura", "p4-sport", "p5-molodezh", "p6-razbor", "p7-yazyk", "p8-test"]:
    s = open(f"{ED}/{p}.svg", encoding="utf-8").read()
    print(f"  {p}: fullwidth_parens={s.count('（')+s.count('）')}")

print("== FONT MEASUREMENTS (PIL) ==")
# find a usable serif font
import glob
fonts = glob.glob("/usr/share/fonts/**/*.ttf", recursive=True) + glob.glob(os.path.expanduser("~/.fonts/**/*.ttf"), recursive=True)
print("  fonts sample:", [f for f in fonts if "Noto" in f][:10], "total", len(fonts))
# top strip: font-size 21, family Noto Serif CJK SC; try DejaVu Serif as proxy AND any NotoSerif
def measure(text, size, fontpath):
    f = ImageFont.truetype(fontpath, size)
    return f.getlength(text)
cands = [f for f in fonts if "Serif" in f]
print("  serif fonts:", cands[:20])
top = "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · OGNI SETTIMANA · IL RUSSO CHE LEGGE LA RUSSIA"
for fp in cands[:6]:
    try:
        w = measure(top, 21, fp)
        print(f"  top strip width via {fp}: {w:.1f} -> span {975-w/2:.1f}–{975+w/2:.1f} (KIT 547.5–1402.5)")
    except Exception as ex:
        print("  err", fp, ex)
# P6 labels at size? get label element attrs
for e in elements(f"{ED}/p6-razbor.svg"):
    if e["text"] in ("Дома с семьёй", "Короткая поездка", "Ярмарка или концерт", "Просто выспятся"):
        print(f"  P6 label: size={e['size']} x={e['x']} text={e['text']!r} attrs={e['attrs'][:160]}")
# chart note line: find P6 text containing 'учебн' / 'Dati'
for e in elements(f"{ED}/p6-razbor.svg"):
    if "учебн" in e["text"].lower() or "Dati di esercitazione" in e["text"]:
        print(f"  P6 note: size={e['size']} x={e['x']} y={e['y']}: {e['text'][:160]!r}")
# P1 media head
for e in elements(f"{ED}/p1-pervaya.svg"):
    if e["text"].startswith("СМИ"):
        print(f"  P1 media head: size={e['size']} x={e['x']} y={e['y']}: {e['text']!r}")
print("DONE4")
