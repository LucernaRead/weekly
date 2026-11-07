# -*- coding: utf-8 -*-
"""Gates round 2 (corrected): word-level CN residue, simplified-only chars,
gold x2 on joined text, labels, anchor-aware ADVANCE right-edge + frame scan."""
import re, os, sys
sys.path.insert(0, 'hidden_files/weekly-report-w45-pt-ja-build')
from svglib import text_w
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-ja/svg")
CO = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-core/svg")
FILES = ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]
def texts(d, f):
    t = open(os.path.join(d, f + ".svg"), encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t)
# --- 1. word-level Chinese-only words (NOT valid Japanese) ---
CN_WORDS = ["桥接","不定式","过去时","现在时","将来时","虚拟式将来","祈使式","高考","亡灵节","墓园","墓碑",
 "蜡烛","菊花","弥撒","献花","怀念","寂静","祈祷","点燃","决赛球队","决战","轮次","首回合","次回合",
 "冲刺","前夕","突击","证件","黑笔","确认卡","考场","开考","关门","大门","地点","考试","时间表","目录","快讯",
 "练习","答案","参考答案","简析","填空","造句","翻译","写作","判断","配对","完成句子","单选","完形",
 "本周生词","常见错误","本周金句","下期预告","闪电问答","头条","周日","周六","周一","周二","周三","周四","周五",
 "小时","分钟","三天","去年","今年","没有","不是","不要","可以","中国","中文","汉语","普通话","简体","繁体",
 "连休长周末","连休","连着","说说你自己","第2版练习","第3版练习","第4版练习","第5版练习","第6版练习"]
SIMP_ONLY = set("连语说让认证备复发对观讲读欢难时际长马风电话车东头练仅汉冯龙龟齐齿国图圆当发么为从会么") - set("国图圆当发么为从会")
# note: 国/图/圆/当/发/为/从/会 are also Japanese kanji (same form) -> excluded above
SIMP_ONLY = set("连语说让认证备复发对观讲读欢难时际长马风电话车东头练仅汉冯龙龟齐齿")
bad = 0
for f in FILES:
    joined = "\n".join(texts(ED, f))
    for w in CN_WORDS:
        if w in joined: print(f"  WORD-FLAG {f}: {w}"); bad += 1
    for ch in sorted(SIMP_ONLY):
        if ch in joined: print(f"  SIMP-FLAG {f}: {ch}"); bad += 1
print("word/simplified residue flags:", bad)
# --- 2. gold x2 on joined, whitespace-normalised text ---
def joined_norm(d):
    s = " ".join(" ".join(texts(d, f)) for f in FILES)
    return re.sub(r"\s+", " ", s)
je, jc = joined_norm(ED), joined_norm(CO)
quotes = ["Do feriadão à prova: a semana do Enem","Muita gente viaja, visita a família e vai ao cemitério levar flores",
 "Finados é o dia da memória","lembrar é um jeito de continuar perto","cada ponto vale uma posição, cada gol vale uma história",
 "quem dorme bem lembra melhor","primeiro as fáceis, depois as difíceis","Confira o cartão, durma bem, chegue cedo"]
for q in quotes:
    print(f"  gold {je.count(q)}x (core {jc.count(q)}x): {q[:50]}")
p7ed = " ".join(texts(ED,"p7-lingua")); p7co = " ".join(texts(CO,"p7-lingua"))
print("  labels JA:", sorted(set(re.findall(r"\(Página \d\)", p7ed))))
print("  labels CO:", sorted(set(re.findall(r"\(Página \d\)", p7co))))
# --- 3. anchor-aware ADVANCE right-edge + frame scan ---
def parse(path):
    t = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs, s = m.group(1), m.group(2)
        def g(name):
            mm = re.search(name + r'="([^"]*)"', attrs); return mm.group(1) if mm else None
        x, y = g("x"), g("y")
        if x is None or y is None: continue
        fam = g("font-family") or ""
        if "UnifrakturMaguntia" in fam: continue
        size = float(g("font-size") or 20)
        bold = (g("font-weight") in ("700","bold"))
        kind = "serif" if "Serif" in fam else "sans"
        anchor = g("text-anchor") or "start"
        try: w = text_w(s, kind, bold, size)
        except Exception: continue
        x = float(x)
        if anchor == "middle": lo, hi = x - w/2, x + w/2
        elif anchor == "end": lo, hi = x - w, x
        else: lo, hi = x, x + w
        out.append((float(y), lo, hi, s))
    return out
flags = 0
for f in FILES:
    for (y, lo, hi, s) in parse(os.path.join(ED, f + ".svg")):
        # inner frame rect: x 40..1910, y 40..2660; outer 28..1922
        if hi > 1910.5 or lo < 39.5:
            print(f"  FRAME {f} y={y} [{lo:.1f},{hi:.1f}] {s[:44]!r}"); flags += 1
        if hi > 1922.5 or lo < 27.5:
            print(f"  OUTER {f} y={y} [{lo:.1f},{hi:.1f}] {s[:44]!r}"); flags += 1
print("anchor-aware frame/edge flags:", flags)
# show the closest-to-frame cases for the record
near = []
for f in FILES:
    for (y, lo, hi, s) in parse(os.path.join(ED, f + ".svg")):
        near.append((hi, f, y, s))
near.sort(reverse=True)
print("top-5 rightmost ends:", [(f"{h:.1f}", f, y, s[:30]) for h, f, y, s in near[:5]])
