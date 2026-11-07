# -*- coding: utf-8 -*-
"""Gate batch 2: gloss counts, P7 phrases, images, residual Latin,
Traditional-independence cross-check, badge measurement."""
import hashlib
import os
import re
from collections import Counter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(GOAL, "weekly-report-w45-zh-tw-ru")
CORE = os.path.join(GOAL, "weekly-report-w45-zhtw-core")
W43 = os.path.join(GOAL, "weekly-report-zh-tw-ru")
BUILD = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r"[\u2e80-\u9fff\uf900-\ufaff\uff00-\uffef]")


def svg_texts(d):
    out = {}
    for f in sorted(os.listdir(os.path.join(d, "svg"))):
        txt = open(os.path.join(d, "svg", f), encoding="utf-8").read()
        out[f] = re.findall(r"<text[^>]*>([^<]*)</text>", txt)
    return out


def images(d):
    out = {}
    for f in sorted(os.listdir(os.path.join(d, "svg"))):
        txt = open(os.path.join(d, "svg", f), encoding="utf-8").read()
        hs = [hashlib.sha256(m.group(1).encode()).hexdigest()[:16]
              for m in re.finditer(r'<image[^>]*href="([^"]+)"', txt)]
        # also capture placement
        pl = re.findall(r'<image x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', txt)
        out[f] = (hs, pl)
    return out


print("== gloss counts ==")
ed_txt = svg_texts(ED)
gloss_boxes = sum(s.startswith("Пояснение — ") for pg in ed_txt.values() for s in pg)
print("rendered 'Пояснение — ' boxes:", gloss_boxes)
print("core rendered 'Notes｜' boxes:",
      sum(s.startswith("Notes｜") for pg in svg_texts(CORE).values() for s in pg))
# source counts
src_gloss = src_glossline = src_match = 0
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    t = open(os.path.join(BUILD, f), encoding="utf-8").read()
    src_gloss += t.count(".gloss(")
    src_glossline += t.count(".glossline(")
    # match_set note lists: count 'notes' items via match_set calls is hard; count via rendered match items instead
print("source .gloss( calls:", src_gloss, "| source .glossline( calls:", src_glossline)

print("== P7 phrases ==")
quotes = [
    "「用手機轉帳、掃碼付款、網上買保險，都是金融科技」",
    "「123個國家及城市、1,600個攤位」",
    "「需要才買，不要為了折扣買一堆用不到的東西」",
    "「在高雄，鋼鐵也能變成舞台」",
    "「福隆的夏天，在10月26日畫下句點」",
    "「6比0完封兄弟，龍隊拋下紅色彩帶」",
    "「250家店家一起討糖」",
    "「旅展首日中午12點才開門」",
]
all_ed = " ".join(s for pg in ed_txt.values() for s in pg)
all_core = " ".join(s for pg in svg_texts(CORE).values() for s in pg)
for q in quotes:
    print(f"  {q[:20]}... edition={all_ed.count(q)} core={all_core.count(q)}")
p7 = " ".join(ed_txt["p7-lang.svg"])
tags = re.findall(r"\(Страница (\d)\)", p7)
print("P7 tags distribution:", dict(sorted(Counter(tags).items())))
core_p7 = " ".join(svg_texts(CORE)["p7-lang.svg"])
print("core P7 tags:", dict(sorted(Counter(re.findall(r"\(p\. (\d)\)", core_p7)).items())))

print("== images ==")
ed_im, core_im = images(ED), images(CORE)
for f in sorted(ed_im):
    same = ed_im[f] == core_im[f]
    print(f"  {f}: payloads={ed_im[f][0]} placements={ed_im[f][1]} identical_to_core={same}")
print("credits verbatim:")
for c in ["Photo: Wilfredor — CC0 (Wikimedia Commons)",
          "Photo: CorraleH — CC0 (Wikimedia Commons)",
          "Photo: Bain News Service — Public domain (Wikimedia Commons)",
          "Photo: Benjamin Balazs — CC0 (Wikimedia Commons)"]:
    print(f"  {c[:40]}... present={c in all_ed}")

print("== residual Latin ==")
toks = Counter()
for s in re.findall(r"[A-Za-z][A-Za-z'’\-]*", all_ed):
    toks[s] += 1
print("distinct Latin tokens:", len(toks))
for t, n in sorted(toks.items()):
    print(f"  {t}: {n}")

print("== Traditional independence ==")
def cjk_set(d):
    s = set()
    for pg in svg_texts(d).values():
        for t in pg:
            s |= {ch for ch in t if CJK.match(ch)}
    return s
ed_set = cjk_set(ED)
union = cjk_set(W43) | cjk_set(CORE)
print(f"edition CJK chars: {len(ed_set)}; union(W43 zh-tw-ru, W45 zh-tw core): {len(union)}")
print("outside union:", sorted(ed_set - union))
simpl = list("邮说国龙马发观欢对让认识语学读书报纸电话车门问间见风云气头")
print("Simplified-only spot hits:", [ch for ch in simpl if ch in ed_set])
print("W43-only chars reused (in union via W43):", sorted((ed_set & cjk_set(W43)) - cjk_set(CORE))[:40])

print("== badge measurement ==")
from PIL import ImageFont
f = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 21, index=3)
badge = "ТЕКСТЫ НА КИТАЙСКОМ (ТРАДИЦИОННОМ) · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ"
print("RU badge width at 21pt bold sans TC:", round(f.getlength(badge), 1), "px (limit 1820)")
for label, d in [("CORE", CORE), ("W43-RU", W43), ("EDITION", ED)]:
    txt = open(os.path.join(d, "svg", "p1-front.svg"), encoding="utf-8").read()
    m = re.search(r'<text ([^>]*)>([^<]*(?:ТРАДИЦИОННОМ|TRADITION|Explanations in English)[^<]*)</text>', txt)
    print(f"  {label}: {m.group(1) if m else 'NOT FOUND'}")
    # footer
    m2 = re.search(r'<text x="65" y="2624"[^>]*>([^<]*)</text>', txt)
    print(f"  {label} footer: {m2.group(1)[:110] if m2 else 'NOT FOUND'}")
