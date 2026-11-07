# -*- coding: utf-8 -*-
"""Independent proofread pass 1 (read-only): CJK union, simplified spot list,
furniture, gloss counts, P7 phrases, images, residual-Latin sweep, P8 style,
readers' corner, badge geometry. Writes a text report; prints summary."""
import re, os, hashlib, html, json
from collections import Counter

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-zh-tw-nl/svg")
EDB = os.path.join(BASE, "hidden_files/weekly-report-w45-zh-tw-nl-build")
W43B = os.path.join(BASE, "hidden_files/weekly-report-zh-tw-nl-build")
OUT = os.path.join(BASE, "hidden_files/w45/zh-tw-nl-proof/work/proof1.txt")

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')
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

# --- CJK sets (own regex, broader than builder's) ---
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
# where does core-edition char occur in core?
for ch in sorted(core_cs - ed_cs):
    hits = []
    for f in core:
        for n in core[f]:
            if ch in n["t"]:
                hits.append(f"{f}:{n['t'][:80]}")
    w(f"  core-only char {ch!r} occurs in: {hits[:6]}")

# --- Simplified-only spot list over edition text nodes ---
SIMP = list("邮说国龙马发让对为会体汉语文读书记车东头乐买卖练线路纸宝电话见观现丽亿仅优发发让礼认识讲许论设证书赵钱孙刘张黄周郑吴冯蒋沈韩杨朱秦何吕施孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公万俟司马")
SIMP = sorted(set(SIMP))
hits = []
for f in ed:
    for n in ed[f]:
        for ch in SIMP:
            if ch in n["t"]:
                hits.append((f, ch, n["t"][:100]))
w("== Simplified-only spot list (edition text nodes) ==")
w(f"hits: {len(hits)}")
for h in hits[:40]:
    w(f"  {h}")
# same list over core, for comparison
chits = []
for f in core:
    for n in core[f]:
        for ch in SIMP:
            if ch in n["t"]:
                chits.append((f, ch, n["t"][:100]))
w(f"core hits (comparison): {len(chits)}")
for h in chits[:20]:
    w(f"  CORE {h}")

# --- Furniture ---
w("== P1 badge (all three) ==")
for name, nd in [("core", core), ("w43", w43), ("edition", ed)]:
    for n in nd["p1-front.svg"]:
        if n["y"] == 378 and n["anchor"] == "middle":
            w(f"  {name}: y={n['y']} size={n['size']} bold={n['bold']} fill={n['fill']} x={n['x']} text={n['t'][:130]}")
w("== Footers (edition) ==")
for f in sorted(ed):
    for n in ed[f]:
        if "WEEKBLAD" in n["t"] or "Pagina" in n["t"]:
            w(f"  {f}: {n['t'][:130]}")
w("== Footers (w43, P1+P2) ==")
for f in ["p1-front.svg", "p2-life.svg"]:
    for n in w43[f]:
        if "WEEKBLAD" in n["t"] or "Pagina" in n["t"]:
            w(f"  {f}: {n['t'][:130]}")
w("== Badge width measurement (PIL, sans bold 21) ==")
import sys
sys.path.insert(0, os.path.join(BASE, "tools"))
from PIL import ImageFont
fb = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
for name, nd in [("core", core), ("w43", w43), ("edition", ed)]:
    for n in nd["p1-front.svg"]:
        if n["y"] == 378 and n["anchor"] == "middle":
            ft = ImageFont.truetype(fb, 21, index=3)
            w(f"  {name}: measured width={ft.getlength(n['t']):.1f} px")

# --- Gloss counts ---
w("== Gloss counts (render) ==")
for f in sorted(ed):
    s = open(os.path.join(ED, f), encoding="utf-8").read()
    w(f"  {f}: Uitleg — x{s.count('Uitleg — ')} Notes x{s.count('Notes')}")
for f in sorted(core):
    s = open(os.path.join(CORE, f), encoding="utf-8").read()
    w(f"  CORE {f}: Notes — x{s.count('Notes — ')} Notes x{s.count('Notes')}")
w("== glossline / match in edition build sources ==")
import glob as _g
for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    s = open(os.path.join(EDB, fn), encoding="utf-8").read()
    w(f"  {fn}: glossline( x{s.count('glossline(')} gloss( x{s.count('gloss(')}")

# --- P7 phrases ---
w("== P7 golden sentences ==")
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "p. 4"),
    ("「250家店家一起討糖」", "p. 5"),
    ("「旅展首日中午12點才開門」", "p. 6"),
]
trans = ["Betaal met je telefoon", "123 landen en steden", "Koop wat je nodig hebt",
         "kan zelfs staal een podium worden", "De zomer van Fulong kwam op 26 oktober",
         "Een 6-0 shutout van de Brothers", "250 winkels die samen snoep uitdelen",
         "gaan de deuren pas om 12.00 uur open"]
for (q, pg), tr in zip(quotes, trans):
    w(f"  {q[:18]}... count={ed_all.count(q)} tag=({pg}) present={('(' + pg + ')') in ed_all} NL-trans present={tr in ed_all}")

# --- Images + credits ---
w("== Images core vs edition ==")
for f in sorted(core):
    cs = open(os.path.join(CORE, f), encoding="utf-8").read()
    es = open(os.path.join(ED, f), encoding="utf-8").read()
    ci = [(m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16]) for m in IMG_RE.finditer(cs)]
    ei = [(m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16]) for m in IMG_RE.finditer(es)]
    w(f"  {f}: core {len(ci)} edition {len(ei)} identical={ci == ei}")
    if ci != ei:
        w(f"    CORE {ci} ED {ei}")
w("== Credit lines (edition) ==")
for f in sorted(ed):
    for n in ed[f]:
        if "Photo:" in n["t"] or "Commons" in n["t"] or "Wilfredor" in n["t"] or "CorraleH" in n["t"] or "Bain" in n["t"] or "Balazs" in n["t"]:
            w(f"  {f}: {n['t'][:160]}")
w("== Credit lines (core, same filter) ==")
for f in sorted(core):
    for n in core[f]:
        if "Photo:" in n["t"] or "Commons" in n["t"] or "Wilfredor" in n["t"] or "CorraleH" in n["t"] or "Bain" in n["t"] or "Balazs" in n["t"]:
            w(f"  CORE {f}: {n['t'][:160]}")

# --- Residual Latin sweep ---
w("== Residual-Latin checks ==")
for needle, want in [("算一算 · Work it out", 0), ("算一算 · Reken uit", 3),
                     ("Baseball words", 0), ("Honkbaltaal", 1),
                     ("Deep-read quiz", 0), ("Diep-leesquiz", 1)]:
    got = ed_all.count(needle)
    w(f"  {needle!r}: {got} (want {want}) {'OK' if got == want else 'MISMATCH'}")
w("== English phrase grep (edition) ==")
for ph in ["Explanations in English", "Quick quiz", "Did you get it", "Fill in", "True or false",
           "Answer keys", "Model answer", "Open task", "Notes", "Match", "Writing",
           "Over to you", "Practice example", "Read the chart", "Work it out",
           "English explanations", "the edition for English-speaking"]:
    w(f"  {ph!r}: {ed_all.count(ph)}")
w("== Distinct Latin-bearing text nodes (edition) ==")
latin = Counter()
for f in ed:
    for n in ed[f]:
        if re.search(r"[A-Za-z]", n["t"]):
            latin[n["t"]] += 1
w(f"  distinct: {len(latin)} total nodes: {sum(latin.values())}")
for t, c in sorted(latin.items()):
    w(f"  x{c} {t[:130]}")

# --- P8 style ---
w("== P8 dash style + separators + header ==")
p8 = ed["p8-test.svg"]
for n in p8:
    if "Antwoordsleutel" in n["t"] or "Alle noten" in n["t"] or "Pagina" in n["t"]:
        w(f"  {n['t'][:130]} size={n['size']}")
w("== P8 key lines sample (first 8 note lines) ==")
cnt = 0
for n in p8:
    if re.match(r"^\d+\. ", n["t"]) and "—" in n["t"]:
        w(f"  {n['t'][:120]}")
        cnt += 1
        if cnt >= 10:
            break
w("== P8 AI note + P6 AI gloss in render ==")
for f in ["p8-test.svg", "p6-deep.svg"]:
    for n in ed[f]:
        if "人工智慧＋" in n["t"]:
            w(f"  {f}: {n['t'][:150]}")
w("== W43 P8 AI note (shipped SVG) ==")
for n in w43["p8-test.svg"]:
    if "人工智慧" in n["t"]:
        w(f"  W43 p8: {n['t'][:150]}")
w("== W43 P8 separator geometry (shipped SVG) ==")
for n in w43["p8-test.svg"]:
    if "Pagina" in n["t"]:
        w(f"  W43 sep: size={n['size']} y={n['y']} text={n['t']}")
        break
for n in ed["p8-test.svg"]:
    if "Pagina" in n["t"]:
        w(f"  ED sep: size={n['size']} y={n['y']} text={n['t']}")
        break

# --- Readers' corner ---
w("== Readers' corner: Traditional disclosure core vs edition ==")
def corner(nd):
    out = []
    for n in nd["p7-lang.svg"]:
        if "延期披露" in n["t"] or "VOL.1曾預告" in n["t"] or "台北小讀者" in n["t"] or "編輯範例" in n["t"]:
            out.append(n["t"])
    return out
w(f"  CORE: {corner(core)}")
w(f"  ED: {corner(ed)}")
w(f"  identical: {corner(core) == corner(ed)}")
for n in ed["p7-lang.svg"]:
    if "Voorbeeldbrief" in n["t"] or "Stuur je brief in" in n["t"]:
        w(f"  ED NL disclosure: {n['t'][:200]}")
for n in w43["p7-lang.svg"]:
    if "Voorbeeldbrief" in n["t"] or "Stuur je brief in" in n["t"]:
        w(f"  W43 NL disclosure: {n['t'][:200]}")

# --- P7 letter-box geometry (SVG level) ---
w("== P7 letter box geometry (edition SVG) ==")
s7 = open(os.path.join(ED, "p7-lang.svg"), encoding="utf-8").read()
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"')
# find letter disclosure text nodes and nearby rects: print all rects in col3 region + disclosure nodes
for n in ed["p7-lang.svg"]:
    if "Voorbeeldbrief" in n["t"] or "Stuur je brief" in n["t"]:
        w(f"  disclosure node: x={n['x']} y={n['y']} size={n['size']} text={n['t'][:120]}")

open(OUT, "w", encoding="utf-8").write("\n".join(rep))
w(f"REPORT WRITTEN {OUT}")
