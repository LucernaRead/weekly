# -*- coding: utf-8 -*-
"""Read-only verification suite for RU x ZH-TW W45 (edition vs core)."""
import re, os, hashlib
from collections import Counter
import xml.etree.ElementTree as ET

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(BASE, "files/weekly-report-w45-ru-core/svg")
ED = os.path.join(BASE, "files/weekly-report-w45-ru-zh-tw/svg")
PAGES = ["p1-pervaya.svg", "p2-zhizn.svg", "p3-kultura.svg", "p4-sport.svg",
         "p5-molodezh.svg", "p6-razbor.svg", "p7-yazyk.svg", "p8-test.svg"]

def texts(path):
    s = open(path, encoding="utf-8").read()
    return re.findall(r"<text[^>]*>(.*?)</text>", s)

def unesc(s):
    return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

def is_cjk(ch):
    o = ord(ch)
    return 0x4E00 <= o <= 0x9FFF or 0x3400 <= o <= 0x4DBF

CYR = re.compile(r"[А-Яа-яЁё]+")

print("== 1. Cyrillic token multiset diff per page ==")
for pg in PAGES:
    c = Counter(t for t in texts(os.path.join(CORE, pg)) for t in CYR.findall(unesc(t)))
    e = Counter(t for t in texts(os.path.join(ED, pg)) for t in CYR.findall(unesc(t)))
    diff = {k: (c[k], e[k]) for k in set(c) | set(e) if c[k] != e[k]}
    print(f"  {pg}: core_total={sum(c.values())} ed_total={sum(e.values())} diff={diff}")

print("== 2. Furniture counts ==")
p1 = [unesc(t) for t in texts(os.path.join(ED, "p1-pervaya.svg"))]
print("  badge x1:", sum(1 for t in p1 if t == "俄語正文 · 繁體中文講解 — 給繁體中文讀者的版本"))
print("  top strip x1:", sum(1 for t in p1 if t == "КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · 每週一期 · 讀俄羅斯人正在讀的俄語"))
print("  subtitle kept x1:", sum(1 for t in p1 if t.startswith("ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА")))
for pg in PAGES:
    ts = [unesc(t) for t in texts(os.path.join(ED, pg))]
    print(f"  {pg} footer={sum(1 for t in ts if t.startswith('Lucerna · 俄語週報 VOL.2'))} pageline={sum(1 for t in ts if re.match(r'^第 \\d 版 / 共 8 版$', t))}")
p8 = [unesc(t) for t in texts(os.path.join(ED, "p8-test.svg"))]
print("  P8 separators:", [t for t in p8 if re.match(r"^— 第 \d 版 —$", t)])
print("  P8 head:", [t for t in p8 if t.startswith("ОТВЕТЫ") or t.startswith("每題附一句")])
print("  P8 band:", [t for t in p8 if t.startswith("ТЕСТ И ОТВЕТЫ")])

print("== 3. Simplified-residue scan (edition SVG text) ==")
sc_only = set("万与两为么义乐习乱于会伦体余兑关养写军几别办动区单历参双变号团图圣场够头夹举学实宾对将尔属带广应开录态战报换据数无时机条来汇泽点状玛现电着码确离简级练结给续编缩罗聪胜节范见让讯讲许诊词译详语说请诺读调谈账购贸赛车转轮较辈辑输达过这连选释里销错长闪问间队阳阵陆静页项顺顾预题个后周组价该发干划舍获复系只钟涂斗邮")
for pg in PAGES:
    ts = [unesc(t) for t in texts(os.path.join(ED, pg))]
    hits = Counter()
    for t in ts:
        for ch in t:
            if ch in sc_only:
                hits[ch] += 1
    print(f"  {pg}: residue={dict(hits)}")
all_ed_text = " ".join(unesc(t) for pg in PAGES for t in texts(os.path.join(ED, pg)))
for w in ["视频", "网络", "软件", "计划", "范文", "屏幕", "连休"]:
    print(f"  mainland word {w}: {all_ed_text.count(w)}")
print("  ASCII double-quote in SVG text:", sum(1 for pg in PAGES for t in texts(os.path.join(ED, pg)) if '"' in unesc(t)))
forbidden = "\u6865\u63a5"
print("  forbidden intermediary term in SVG text:", all_ed_text.count(forbidden))

print("== 4. Orphan scan ==")
closers = set("。；：、，）〕」』》！？")
openers = set("（〔「『《")
for label, d in [("core", CORE), ("edition", ED)]:
    ls, le = 0, 0
    examples = []
    for pg in PAGES:
        for t in texts(os.path.join(d, pg)):
            t = unesc(t).strip()
            if t and t[0] in closers:
                ls += 1; examples.append((pg, t[:20]))
            if t and t[-1] in openers:
                le += 1; examples.append((pg, t[-20:]))
    print(f"  {label}: line-start closers={ls} line-end openers={le} examples={examples[:10]}")

print("== 5. P7 golden sentences ==")
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
for label, d in [("core", CORE), ("edition", ED)]:
    joined = " ".join(unesc(t) for pg in PAGES for t in texts(os.path.join(d, pg)))
    print(f"  {label}: bare counts={[joined.count(q) for q in quotes]}")
p7ed = [unesc(t) for t in texts(os.path.join(ED, "p7-yazyk.svg"))]
print("  P7 page tags:", Counter(re.findall(r"\(Страница \d\)", " ".join(p7ed))))
print("  P7 golden translations present:",
      sum(1 for cn in ["11 月 4 日星期三，是工作週中間的休息日。",
                       "夾著一個假日的一週該怎麼過？",
                       "11 月 3 日星期二，工作日短一小時。",
                       "星期三，各城市舉辦集市和音樂會。",
                       "11 月 8 日星期日，有三場比賽。",
                       "先列清單：你真正需要什麼？",
                       "許多人在星期四和星期五請假。",
                       "五天——幾乎就是一個小長假！"] if any(cn in t for t in p7ed)))

print("== 6. P7 readers corner geometry ==")
for label, d in [("core", CORE), ("edition", ED)]:
    s = open(os.path.join(d, "p7-yazyk.svg"), encoding="utf-8").read()
    rects = re.findall(r'<rect x="([^"]*)" y="([^"]*)" width="([^"]*)" height="([^"]*)"', s)
    texts_y = re.findall(r'<text x="[^"]*" y="([^"]*)"[^>]*>(.*?)</text>', s)
    print(f"  {label} col3 rects (x=1405):", [(x, y, w, h) for x, y, w, h in rects if x == "1405"])
    print(f"  {label} baselines 1650-1800:", [(y, t[:30]) for y, t in texts_y if 1650 <= float(y) <= 1800])

print("== 7. Image payloads ==")
for pg in PAGES:
    def imgs(d):
        s = open(os.path.join(d, pg), encoding="utf-8").read()
        hrefs = re.findall(r'(?:xlink:href|href)="([^"]+)"', s)
        els = re.findall(r'<image[^>]*>', s)
        return [(len(h), hashlib.sha256(h.encode()).hexdigest()[:16]) for h in hrefs], els
    c, ce = imgs(CORE); e, ee = imgs(ED)
    print(f"  {pg}: core={c} ed={e} geom_equal={ce == ee}")

print("== 8. P6 chart element check (later rect vs earlier text, XML parse) ==")
NS = "{http://www.w3.org/2000/svg}"
for label, d in [("core", CORE), ("edition", ED)]:
    tree = ET.parse(os.path.join(d, "p6-razbor.svg"))
    root = tree.getroot()
    items = []
    for el in root.iter():
        tag = el.tag.replace(NS, "")
        if tag == "text":
            items.append(("text", float(el.get("x")), float(el.get("y")), el.text or ""))
        elif tag == "rect":
            items.append(("rect", float(el.get("x") or 0), float(el.get("y") or 0),
                          float(el.get("width")), float(el.get("height"))))
    overlaps = []
    for i, it in enumerate(items):
        if it[0] == "text":
            for j in range(i + 1, len(items)):
                r = items[j]
                if r[0] == "rect" and r[1] <= it[1] <= r[1] + r[3] and r[2] <= it[2] <= r[2] + r[4]:
                    overlaps.append((it[3][:20], r))
    print(f"  {label}: point-in-later-rect overlaps={len(overlaps)} {overlaps[:5]}")

print("== 9. Non-CJK text-element geometry (frozen Russian render check) ==")
for pg in PAGES:
    def noncjk(d):
        out = []
        s = open(os.path.join(d, pg), encoding="utf-8").read()
        for m in re.finditer(r'<text x="([^"]*)" y="([^"]*)"[^>]*>(.*?)</text>', s):
            t = unesc(m.group(3))
            if not any(is_cjk(c) for c in t):
                out.append((m.group(1), m.group(2), t))
        return Counter(out)
    c, e = noncjk(CORE), noncjk(ED)
    diff = {k: (c[k], e[k]) for k in set(c) | set(e) if c[k] != e[k]}
    print(f"  {pg}: non-CJK element diff keys={len(diff)}")
    for k, v in list(diff.items())[:12]:
        print(f"     {v} {k[2][:60]!r} @({k[0]},{k[1]})")
