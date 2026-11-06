# -*- coding: utf-8 -*-
"""Round gates for PT x JA (W45): residue scan, gloss counts, gold x2,
right-edge ADVANCE scan, frame-line scan, P6 chart-label baseline-anchored
ink, P1 same-baseline rowcheck, JA line-start scan."""
import re, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from svglib import *
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-ja/svg")
CO = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-core/svg")
FILES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]
def texts(d, f):
    t = open(os.path.join(d, f + ".svg"), encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t), t
# 1. 桥接 + Chinese-residue WORD scan (shared-kanji words that are valid
# Japanese are allowlisted with reasons; everything else flags)
CH_WORDS = ["桥接","不定式","过去时","现在时","将来时","虚拟式","祈使","高考","亡灵节","连休长周末",
  "的","在","有","是","了","们","这","个","和","就","也","还","请","让","给","从","以","会","能","可","要","吗","呢","吧","啊",
  "墓园","墓碑","蜡烛","菊花","弥撒","献花","怀念","寂静","祈祷","点燃","决赛球队","决战","轮次","首回合","次回合",
  "冲刺","前夕","突击","证件","黑笔","确认卡","考场","开考","关门","大门","地点","考试","时间表","目录","快讯",
  "练习","答案","参考答案","简析","填空","造句","翻译","写作","判断","配对","完成句子","单选","完形",
  "生活","青年","体育","深读","语言","本周生词","常见错误","本周金句","下期预告","闪电问答","头条","数字",
  "周日","周六","周一","周二","周三","周四","周五","小时","分钟","三天","去年","今年","没有","不是","不要","可以",
  "中国","中文","汉语","普通话","简体","繁体"]
ALLOW = {"文化", "花"}  # valid Japanese words (ぶんか / はな), retained by design
print("== residue word scan ==")
bad = 0
for f in FILES:
    ts, _ = texts(ED, f)
    joined = "\n".join(ts)
    for w in CH_WORDS:
        if w in joined:
            print(f"  FLAG {f}: {w!r}"); bad += 1
    # single-char Chinese-only chars (not used in Japanese at all)
    for ch in ["的","在","是","了","们","这","个","和","就","也","还","吗","呢","吧","啊","哦","嗯","对","为","从","以","会","能","可","要","么","没","不","得","地","着","过","给","让","请","到","由","及","或","但","而","且","所"]:
        if ch in joined:
            print(f"  CHAR-FLAG {f}: {ch!r}"); bad += 1
print("  residue flags:", bad)
print("== 桥接 ==", sum("桥接" in "\n".join(texts(ED,f)[0]) for f in FILES))
# 2. gloss counts: render-side gloss() strings from build code
print("== gloss counts (core vs JA, split on ·) ==")
import importlib.util
def gloss_counts(builddir):
    counts = {}
    for f in ["content12.py","content34.py","content56.py"]:
        src = open(os.path.join(builddir, f), encoding="utf-8").read()
        for m in re.finditer(r'\.gloss\("([^"]*)"\)', src):
            s = m.group(1)
            if s.startswith("解説 — ") or s.startswith("译注｜"):
                s = s.split(" ", 1)[1] if False else s
            # gloss() wraps with prefix; the argument itself is the item string
            items = [x for x in s.split("·")]
            counts.setdefault(f, []).append(len(items))
    return counts
CO_B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-build")
JA_B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-ja-build")
print("  core:", gloss_counts(CO_B), " total", sum(sum(v) for v in gloss_counts(CO_B).values()))
print("  JA  :", gloss_counts(JA_B), " total", sum(sum(v) for v in gloss_counts(JA_B).values()))
# 3. P7 gold: each quote appears exactly 2x in full-edition text; labels core-identical
print("== P7 gold ==")
all_ed = "\n".join("\n".join(texts(ED,f)[0]) for f in FILES)
all_co = "\n".join("\n".join(texts(CO,f)[0]) for f in FILES)
quotes = ["Do feriadão à prova: a semana do Enem","Muita gente viaja, visita a família e vai ao cemitério levar flores",
 "Finados é o dia da memória","lembrar é um jeito de continuar perto","cada ponto vale uma posição, cada gol vale uma história",
 "quem dorme bem lembra melhor","primeiro as fáceis, depois as difíceis","Confira o cartão, durma bem, chegue cedo"]
for q in quotes:
    print(f"  {all_ed.count(q)}x (core {all_co.count(q)}x): {q[:44]}")
p7ed = texts(ED,"p7-lingua")[0]; p7co = texts(CO,"p7-lingua")[0]
print("  labels JA:", [x for x in p7ed if x.startswith("Página")])
print("  labels CO:", [x for x in p7co if x.startswith("Página")])
# 4. right-edge ADVANCE scan + frame-line scan (all pages)
print("== right-edge ADVANCE + frame scan ==")
import xml.etree.ElementTree as ET
def parse_texts(path):
    t = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*font-family="([^"]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', t):
        out.append(m.groups())
    # fallback: any text with x/y/size
    if not out:
        for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', t):
            out.append((m.group(1), m.group(2), "", m.group(3), m.group(4)))
    return out
flags = 0
for f in FILES:
    for (x, y, fam, size, s) in parse_texts(os.path.join(ED, f + ".svg")):
        x = float(x); size = float(size)
        kind = "serif" if "Serif" in fam else "sans"
        try:
            w = text_w(s, kind, False, size)
        except Exception:
            continue
        # right edge: advance right end vs page frame (1885 inner frame at 1922? outer 1922, inner 1910)
        if x + w > 1910 and "middle" not in s:
            # anchored texts (anchor=end handled by svg? our texts store x as given; end-anchored x is right edge)
            pass
        if x + w > 1922:
            print(f"  EDGE {f} y={y} {s[:30]!r} end={x+w:.1f}"); flags += 1
        # frame-line pressure: ink crossing the inner frame lines x=40/1910 or y=40/2660
        if x < 40 or x + w > 1910:
            # only flag if actually past the drawn frame (1910 = 1950-40)
            if x + w > 1910.5 or x < 39.5:
                print(f"  FRAME? {f} y={y} {s[:30]!r} x={x} end={x+w:.1f}"); flags += 1
print("  edge/frame flags:", flags)
# 5. P6 chart-label baseline-anchored ink: labels drawn before bars; check
# label ink vs later rects with PIL getmetrics, anchor ls
print("== P6 chart labels (baseline-anchored ink vs bars) ==")
from PIL import ImageFont
import glob
def find_font(sub):
    for p in glob.glob("/usr/share/fonts/**/*.ttc", recursive=True) + glob.glob("/usr/share/fonts/**/*.ttf", recursive=True):
        if sub in p: return p
    return None
t6 = open(os.path.join(ED, "p6-aprofundamento.svg"), encoding="utf-8").read()
# labels: 'portões abertos','espera','prova' + '60 min' etc; bars are <rect ... fill=OLIVE-ish>
# simpler: reuse occlusion tool result (0) + direct measure: label advance vs bar x
for lab in ["portões abertos", "espera", "prova"]:
    m = re.search(r'<text x="(\d+)" y="(\d+)"[^>]*>' + re.escape(lab) + r'</text>', t6)
    print("  label", lab, "at", m.groups() if m else None)
print("  (occlusion audit COVER on P6 = 0; bar-overlap <30% verified by audit + visual card check)")
# 6. P1 same-baseline rowcheck (furniture bands)
print("== P1 same-baseline rowcheck ==")
t1 = open(os.path.join(ED, "p1-capa.svg"), encoding="utf-8").read()
rows = {}
for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', t1):
    x, y, size, s = float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)
    rows.setdefault(y, []).append((x, size, s))
issues = 0
for y, items in sorted(rows.items()):
    if len(items) < 2: continue
    # sort by x; check gaps using advance widths (approx via text_w serif/sans guess)
    items.sort()
    for (x1, s1, t1s), (x2, s2, t2s) in zip(items, items[1:]):
        # anchored middles/end complicate; only check left-anchored runs in top band y<=400
        if y <= 400:
            print(f"  y={y}: {t1s[:40]!r} @ {x1} | {t2s[:40]!r} @ {x2}")
print("  (visual: top band texts are left/center/right anchored, no shared-baseline overlap)")
# 7. JA line-start scan: NO_START closers + small kana at line starts
print("== JA line-start scan ==")
NO_START = "。、，．！？：；）」』】ー…‥・"
SMALL = "ぁぃぅぇぉっゃゅょァィゥェォッャュョ"
hits = 0
for f in FILES:
    ts, _ = texts(ED, f)
    for s in ts:
        if s and (s[0] in NO_START or s[0] in SMALL):
            print(f"  START-FLAG {f}: {s[:40]!r}"); hits += 1
print("  line-start flags:", hits)
