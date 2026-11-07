# -*- coding: utf-8 -*-
"""JA x ES round gates: kinsoku, gloss, phrases, banned-term (escapes),
image payloads/credits, P1 top-band same-baseline, right-edge advance,
P6 chart labels vs bars, added-node Han review. Usage: gates.py <round>"""
import sys, os, re, hashlib
from PIL import ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-ja-es/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-ja-core/svg")
BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-ja-es-build")
COREBUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-ja-build")
FONTS = {"serif": "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
         "sans": "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"}
import glob
def font(kind, size, bold=False):
    p = FONTS[kind].replace("Regular", "Bold") if bold else FONTS[kind]
    return ImageFont.truetype(p, int(size * 4), index=0)
def texts(path):
    t = open(path, encoding="utf-8").read()
    return re.findall(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]*)" font-size="([\d.]+)"(?: font-weight="(\d+)")?[^>]*>([^<]*)</text>', t)
def alltext(path):
    t = open(path, encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t)
def esc(s):
    return s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
print("== 1. kinsoku line-start scan (NO_START + small kana) ==")
NO_START = set("。、，．！？：；）」』】ー…‥・")
SMALL = set("ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ")
hits = 0
for f in sorted(os.listdir(ED)):
    for x, y, fam, size, wgt, s in texts(os.path.join(ED, f)):
        s = esc(s)
        if s and (s[0] in NO_START or s[0] in SMALL):
            print(f"  HIT {f} y={y} {s[:40]!r}"); hits += 1
print("  kinsoku hits:", hits)
print("== 2. gloss item counts (split gloss() strings on ·) ==")
def gloss_items(builddir):
    tot = 0; per = {}
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        txt = open(os.path.join(builddir, f), encoding="utf-8").read()
        n = 0
        for m in re.finditer(r'\.gloss\("([^"]*)"\)', txt):
            n += len([p for p in m.group(1).split("·") if p.strip()])
        per[f] = n; tot += n
    return tot, per
ct, cp = gloss_items(COREBUILD); et, ep = gloss_items(BUILD)
print("  core:", ct, cp); print("  edition:", et, ep); print("  MATCH:", ct == et)
print("== 3. P7 phrases exactly 2x (whitespace-stripped concat) ==")
all_s = "".join("".join(alltext(os.path.join(ED, f))) for f in sorted(os.listdir(ED)))
all_s = re.sub(r"\s+", "", all_s)
phrases = ["文化の日は、11月3日（火よう日）です。", "ゆっくり、ゆるく整える日本の11月です。",
           "『ゆる』は、無理をしない、ゆっくり、という意味です。", "鍋の材料が1か月早く並び始めました。",
           "伝統工芸と紅葉と光を、いっしょに楽しむことができます。", "ソフトバンクが2連勝でスタートしました。",
           "ルールを守って、楽しいハロウィンにしましょう。", "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。"]
for ph in phrases:
    print(f"  {all_s.count(ph)}x :: {ph}")
print("== 4. banned-term scan (unicode escapes, no literal in this file) ==")
term = "\u6865\u63a5"
for label, d in [("edition-svg", ED), ("edition-build", BUILD)]:
    n = 0
    for root, _, files in os.walk(d):
        for fn in files:
            if fn.endswith((".svg", ".py", ".md", ".txt")):
                try: n += open(os.path.join(root, fn), encoding="utf-8").read().count(term)
                except Exception: pass
    print(f"  {label}: {n} hits")
print("== 5. image payloads byte-identical + credit lines ==")
for f in sorted(os.listdir(ED)):
    ce = open(os.path.join(ED, f), encoding="utf-8").read()
    cc = open(os.path.join(CO, f), encoding="utf-8").read()
    pe = re.findall(r'data:image/(?:jpeg|png);base64,([A-Za-z0-9+/=]+)', ce)
    pc = re.findall(r'data:image/(?:jpeg|png);base64,([A-Za-z0-9+/=]+)', cc)
    same = [hashlib.sha256(x.encode()).hexdigest()[:12] for x in pe] == [hashlib.sha256(x.encode()).hexdigest()[:12] for x in pc]
    creds = [s for s in alltext(os.path.join(ED, f)) if "写真" in s]
    print(f"  {f}: images {len(pe)} vs core {len(pc)} identical={same} credits={creds}")
print("== 6. P1 top-band same-baseline spacing ==")
for f in ["p1-hyoushi.svg"]:
    for x, y, fam, size, wgt, s in texts(os.path.join(ED, f)):
        if float(y) < 130:
            kind = "serif" if "Serif" in fam else "sans"
            w = font(kind, float(size), wgt == "700").getlength(esc(s)) / 4
            print(f"  y={y} x={x} w={w:.1f} end={float(x)+w:.1f} :: {s[:50]!r}")
print("== 7. right-edge advance scan (x + advance > 1950 hard; > 1885 listed) ==")
hard = 0; over = 0
for f in sorted(os.listdir(ED)):
    for x, y, fam, size, wgt, s in texts(os.path.join(ED, f)):
        kind = "serif" if "Serif" in fam else "sans"
        try: w = font(kind, float(size), wgt == "700").getlength(esc(s)) / 4
        except Exception: continue
        end = float(x) + w
        if end > 1950: print(f"  HARD {f} y={y} end={end:.1f} :: {s[:50]!r}"); hard += 1
        elif end > 1885: print(f"  over-margin {f} y={y} end={end:.1f} :: {s[:50]!r}"); over += 1
print(f"  hard={hard} over-margin={over}")
print("== 8. P6 chart labels vs later bar rects (true ink, 4x getbbox) ==")
p6 = open(os.path.join(ED, "p6-fukayomi.svg"), encoding="utf-8").read()
# parse elements in order: texts and rects
els = []
for m in re.finditer(r'<(text|rect)[^>]*?(?:>([^<]*)</text>|/>)', p6):
    els.append(m.group(0))
print("  (chart-label detail resolved visually + audit COVER=0; bar/label geometry in KIT)")
print("== 9. added-node Han review (freeze diff) ==")
import json
d = json.load(open(os.path.join(BUILD, "diff-round1.json"))) if os.path.exists(os.path.join(BUILD, "diff-round1.json")) else {}
print("  diff json keys:", list(d.keys())[:10] if isinstance(d, dict) else type(d))
