# -*- coding: utf-8 -*-
"""Reproof pass 1 (read-only): CJK union, simplified spot, furniture, gloss
counts, P7 phrases, images, residual-Latin sweep, P8 style, readers corner,
badge geometry, P7 letter-box direct measurement, P7/P4/P6 geometry."""
import re, os, hashlib, html, json
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-zh-tw-nl/svg")
EDB = os.path.join(BASE, "hidden_files/weekly-report-w45-zh-tw-nl-build")
W43B = os.path.join(BASE, "hidden_files/weekly-report-zh-tw-nl-build")
OUT = os.path.join(BASE, "hidden_files/w45/zh-tw-nl-reproof/work/reproof1.txt")
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"([^>]*)>')
IMG_RE = re.compile(r'<image x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*href="data:image/[^;]+;base64,([^"]+)"')

def nodes(d, fn):
    s = open(os.path.join(d, fn), encoding="utf-8").read()
    out = []
    for m in TEXT_RE.finditer(s):
        attrs = m.group(3)
        fm = re.search(r'font-family="([^"]+)"', attrs)
        sm = re.search(r'font-size="([\d.]+)"', attrs)
        cm = re.search(r'fill="([^"]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anchor = "middle" if 'text-anchor="middle"' in attrs else ("end" if 'text-anchor="end"' in attrs else "start")
        out.append({"x": float(m.group(1)), "y": float(m.group(2)), "t": html.unescape(m.group(4)),
                    "fam": fm.group(1) if fm else "", "size": float(sm.group(1)) if sm else 0,
                    "fill": cm.group(1) if cm else "", "bold": bold, "anchor": anchor})
    return s, out

def allnodes(d):
    res = {}
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".svg"):
            res[fn] = nodes(d, fn)[1]
    return res

rep = []
def w(s=""):
    rep.append(s); print(s)

ed, core, w43 = allnodes(ED), allnodes(CORE), allnodes(W43)
ed_all = "".join(n["t"] for f in ed for n in ed[f])
core_all = "".join(n["t"] for f in core for n in core[f])
w(f"node counts: edition={sum(len(v) for v in ed.values())} core={sum(len(v) for v in core.values())}")

CJK = re.compile(r"[\u2e80-\u2fff\u3000-\u303f\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\U00020000-\U0002a6df]")
def cjkset(nd):
    cs = set()
    for f in nd:
        for n in nd[f]:
            cs |= set(CJK.findall(n["t"]))
    return cs
ed_cs, core_cs, w43_cs = cjkset(ed), cjkset(core), cjkset(w43)
union = core_cs | w43_cs
w("== CJK union ==")
w(f"edition={len(ed_cs)} core={len(core_cs)} w43={len(w43_cs)} union={len(union)}")
w(f"outside union: {sorted(ed_cs - union)}")
w(f"edition-core: {sorted(ed_cs - core_cs)}")
w(f"core-edition: {sorted(core_cs - ed_cs)}")
for ch in sorted(core_cs - ed_cs):
    hits = []
    for f in core:
        for n in core[f]:
            if ch in n["t"]:
                hits.append(f"{f}:{n['t'][:80]}")
    w(f"  core-only {ch!r}: {hits[:6]}")

SIMP = "邮说国龙马发让对为体汉语学读书车东头乐买卖练线纸宝电话见观现丽亿仅优礼认讲许论设证丰义习乡乱争产亲刘刘".replace("刘刘","刘")
SIMP = sorted(set(SIMP))
w("== Simplified-only spot list (target text nodes, all pages) ==")
hits = []
for f in ed:
    for n in ed[f]:
        for ch in SIMP:
            if ch in n["t"]:
                hits.append((f, ch, n["t"][:90]))
w(f"hits: {len(hits)}")
for h in hits[:20]:
    w(f"  {h}")
# also: any simplified-only char check restricted to nodes that contain CJK target text is same set; report total

w("== Gloss/match counts ==")
for name, nd in [("edition", ed), ("core", core)]:
    all_t = "".join(n["t"] for f in nd for n in nd[f])
    per = {}
    for f in nd:
        per[f] = sum(1 for n in nd[f] if n["t"].startswith("Uitleg — ") or n["t"].startswith("Notes — "))
    w(f"{name}: Uitleg/Notes-prefix nodes total={sum(per.values())} per-page={per}")
    w(f"  'Notes' residual occurrences: {all_t.count('Notes')}")
    w(f"  glossline-prefix 'Uitleg — ' count: {all_t.count('Uitleg — ')}")
w(f"edition glossline count via sources check done separately; render 'Uitleg — ' total above")

w("== Residual Latin sweep ==")
checks = [
    ("算一算 · Work it out", ed_all.count("算一算 · Work it out")),
    ("算一算 · Reken uit", ed_all.count("算一算 · Reken uit")),
    ("Baseball words", ed_all.count("Baseball words")),
    ("Honkbaltaal", ed_all.count("Honkbaltaal")),
    ("Deep-read quiz", ed_all.count("Deep-read quiz")),
    ("Diep-leesquiz", ed_all.count("Diep-leesquiz")),
]
for k, v in checks:
    w(f"  {k!r} = {v}")
for f in ed:
    for n in ed[f]:
        if "Reken uit" in n["t"]:
            w(f"  Reken uit node: {f} {n['t'][:80]}")
        if "Honkbaltaal" in n["t"] or "Diep-leesquiz" in n["t"]:
            w(f"  title node: {f} {n['t'][:80]}")
ENG = ["Explanations in English", "Quick quiz", "Did you get it", "Fill in", "True or false",
       "Answer keys", "Model answer", "Open task", "Notes", "Match", "Writing", "Over to you",
       "Practice example", "Read the chart", "Work it out", "Sentence frame", "Readers' corner",
       "Phrases of the week", "Next week"]
bad = [(p, ed_all.count(p)) for p in ENG if ed_all.count(p) > 0]
w(f"  English-phrase hits (should be []): {bad}")

w("== P7 golden sentences (bare count, edition + core) ==")
gold = ["用手機轉帳", "123個國家及城市、1,600個攤位", "需要才買", "在高雄，鋼鐵也能變成舞台",
        "福隆的夏天，在10月26日畫下句點", "6比0完封兄弟，龍隊拋下紅色彩帶", "250家店家一起討糖", "旅展首日中午12點才開門"]
for g in gold:
    w(f"  {g[:30]!r}: edition={ed_all.count(g)} core={core_all.count(g)}")
w("  (p. N) tags on P7:")
for n in ed["p7-lang.svg"]:
    if "(p." in n["t"]:
        w(f"    {n['t'][:100]}")

w("== Readers corner ==")
for f in ["p7-lang.svg"]:
    for n in ed[f]:
        if "Voorbeeldbrief" in n["t"] or "Stuur je brief" in n["t"]:
            w(f"  ED {n['t'][:200]}")
    for n in core[f]:
        if "Deferral" in n["t"] or "example letter" in n["t"]:
            w(f"  CORE {n['t'][:200]}")
w("  frozen Traditional disclosure identical core vs edition:")
core_disc = [n["t"] for n in core["p7-lang.svg"] if "延期披露" in n["t"]]
ed_disc = [n["t"] for n in ed["p7-lang.svg"] if "延期披露" in n["t"]]
w(f"    core={core_disc}")
w(f"    edition={ed_disc}")
w(f"    identical={core_disc == ed_disc}")

w("== Furniture: badge/footer/P8 header/separators ==")
for name, nd, fn in [("edition", ed, "p1-front.svg"), ("core", core, "p1-front.svg"), ("w43", w43, "p1-front.svg")]:
    for n in nd[fn]:
        if n["y"] == 378 or (n["size"] == 21 and n["bold"] and n["y"] < 400):
            w(f"  {name} badge-candidate y={n['y']} size={n['size']} bold={n['bold']} fill={n['fill']} text={n['t'][:120]}")
for name, nd in [("edition", ed), ("w43", w43)]:
    foots = set()
    for f in nd:
        for n in nd[f]:
            if "WEEKBLAD" in n["t"] or "Pagina" in n["t"] and "van 8" in n["t"]:
                foots.add(n["t"])
    w(f"  {name} footer strings: {sorted(foots)[:4]}")
ed_p8 = "".join(n["t"] for n in ed["p8-test.svg"])
w43_p8 = "".join(n["t"] for n in w43["p8-test.svg"])
for needle in ["Antwoordsleutel — in paginavolgorde", "Alle noten in het Nederlands"]:
    w(f"  P8 header needle {needle!r}: edition={needle in ed_p8} w43={needle in w43_p8}")
w(f"  edition P8 separators count 'Pagina': {ed_p8.count('Pagina')}")
import re as _re
seps = _re.findall(r"— Pagina \d+ —", ed_p8)
w(f"  edition separators: {seps}")
w(f"  edition P8 dash keys sample: {[n['t'][:70] for n in ed['p8-test.svg'] if n['t'][:4] in ('138.', '100.', '1. ')][:6]}")
for n in ed["p8-test.svg"]:
    if n["t"].startswith("138."):
        w(f"  P8 key 138: {n['t']}")
for n in ed["p6-deep.svg"]:
    if "AI+" in n["t"] and "kunstmatige" in n["t"]:
        w(f"  P6 AI gloss: {n['t'][:200]}")
w(f"  W43 P8 has AI item: {'人工智慧' in w43_p8}")

w("== Images: payload hashes per page ==")
for f in sorted(ed):
    s_ed, _ = nodes(ED, f)
    s_co, _ = nodes(CORE, f)
    im_ed = [(m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16]) for m in IMG_RE.finditer(s_ed)]
    im_co = [(m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16]) for m in IMG_RE.finditer(s_co)]
    w(f"  {f}: edition={im_ed} core={im_co} match={im_ed == im_co}")
    for n in ed[f]:
        if n["t"].startswith("Photo:"):
            w(f"    credit ED: {n['t']}")
    for n in core[f]:
        if n["t"].startswith("Photo:"):
            w(f"    credit CORE: {n['t']}")

w("== P4/P6 chart bars (rect widths) ==")
for f in ["p4-sport.svg", "p6-deep.svg"]:
    s, _ = nodes(ED, f)
    rects = [(float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))) for m in RECT_RE.finditer(s)]
    sc, _ = nodes(CORE, f)
    rects_c = [(float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))) for m in RECT_RE.finditer(sc)]
    w(f"  {f} edition rect widths multiset sample: {sorted(Counter([r[2] for r in rects]).items())}")
    w(f"  {f} core rect widths: {sorted(Counter([r[2] for r in rects_c]).items())}")

w("== W43 build dash precedent ==")
for src, d in [("W43 content8", W43B), ("edition content8", EDB)]:
    p = os.path.join(d, "content8.py")
    s = open(p, encoding="utf-8").read()
    for line in s.splitlines():
        if "Pagina" in line or ("af.para" in line and "pg" in line):
            w(f"  {src}: {line.strip()[:140]}")
    for line in s.splitlines():
        if "12.8" in line or "13.3" in line:
            w(f"  {src} size line: {line.strip()[:140]}")

with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(rep) + "\n")
w("WROTE " + OUT)
