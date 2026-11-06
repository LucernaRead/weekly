# -*- coding: utf-8 -*-
"""Independent proof checks for W45 zh-tw x FR. READ-ONLY: parses shipped
SVG text nodes and build source as text. Never imports a content module."""
import os, re, sys, hashlib, base64, json
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-zh-tw-fr/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-zh-tw-fr/svg")
COREB = os.path.join(BASE, "hidden_files/weekly-report-w45-zhtw-build")
FRB = os.path.join(BASE, "hidden_files/weekly-report-w45-zh-tw-fr-build")
PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-youth", "p6-deep", "p7-lang", "p8-test"]
TEXTRX = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"[^>]*>([^<]*)</text>')

def texts(d, pg):
    src = open(os.path.join(d, pg + ".svg"), encoding="utf-8").read()
    out = []
    for m in TEXTRX.finditer(src):
        out.append({"x": float(m.group(1)), "y": float(m.group(2)), "fam": m.group(3),
                    "size": float(m.group(4)), "t": m.group(5), "raw": m.group(0)})
    return src, out

def iscjk(c):
    o = ord(c)
    return (0x3400 <= o <= 0x4DBF or 0x4E00 <= o <= 0x9FFF or 0xF900 <= o <= 0xFAFF
            or 0x20000 <= o <= 0x2A6DF)

def charset(d):
    s = set()
    for pg in PAGES:
        _, ts = texts(d, pg)
        for t in ts:
            for ch in t["t"]:
                if iscjk(ch):
                    s.add(ch)
    return s

print("== A. CJK union independence ==")
ed_cs, core_cs, w43_cs = charset(ED), charset(CORE), charset(W43)
outside = ed_cs - (core_cs | w43_cs)
print(f"edition={len(ed_cs)} core={len(core_cs)} w43={len(w43_cs)} outside-union={len(outside)}")
for ch in sorted(outside):
    print(f"  OUTSIDE {ch} U+{ord(ch):04X}")
print(f"edition-core={len(ed_cs-core_cs)} (expect furniture-only loss/gain)")

print("== B. Simplified-only spot scan (edition SVG text) ==")
simp = list("邮说国龙马发让对为会东车门问间见长湾网风飞头汉义习贝产严刘广厂疗发")  # curated simplified-only forms
simp = sorted(set(simp))
hits = {}
for pg in PAGES:
    _, ts = texts(ED, pg)
    joined = "".join(t["t"] for t in ts)
    for ch in simp:
        n = joined.count(ch)
        if n:
            hits.setdefault(ch, []).append((pg, n))
print("hits:", hits if hits else "ZERO")

print("== C. full-width comma counts per page (core vs edition) ==")
for pg in PAGES:
    _, cts = texts(CORE, pg); _, ets = texts(ED, pg)
    cj = "".join(t["t"] for t in cts); ej = "".join(t["t"] for t in ets)
    print(f"  {pg}: core ，={cj.count('，')} edition ，={ej.count('，')} core 、={cj.count('、')} edition 、={ej.count('、')}")

print("== D. gloss counts (source text grep, core build vs FR build) ==")
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    c = open(os.path.join(COREB, f), encoding="utf-8").read()
    e = open(os.path.join(FRB, f), encoding="utf-8").read()
    print(f"  {f}: gloss core={c.count('.gloss(')} ed={e.count('.gloss(')} | glossline core={c.count('.glossline(')} ed={e.count('.glossline(')}")
    for src, lab in [(c, "core"), (e, "ed")]:
        for m in re.finditer(r'\.gloss\("([^"]*)"\)', src):
            if "·" in m.group(1):
                print(f"    {lab} gloss WITH ·: {m.group(1)[:90]!r}")

print("== E. P7 golden phrases ==")
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "p. 1", "p1-front"),
    ("「123個國家及城市、1,600個攤位」", "p. 1", "p1-front"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "p. 2", "p2-life"),
    ("「在高雄，鋼鐵也能變成舞台」", "p. 3", "p3-culture"),
    ("「福隆的夏天，在10月26日畫下句點」", "p. 3", "p3-culture"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "p. 4", "p4-sport"),
    ("「250家店家一起討糖」", "p. 5", "p5-youth"),
    ("「旅展首日中午12點才開門」", "p. 6", "p6-deep"),
]
alltext = {}; core_text = {}
for pg in PAGES:
    _, ts = texts(ED, pg); alltext[pg] = "".join(t["t"] for t in ts)
    _, ts = texts(CORE, pg); core_text[pg] = "".join(t["t"] for t in ts)
full = "".join(alltext[p] for p in PAGES)
_, p7ts = texts(ED, "p7-lang")
p7joined = "".join(t["t"] for t in p7ts)
for q, tag, pg in quotes:
    n = full.count(q)
    # tag check: P7 renders tags like "p. 1" near the phrase; find tag occurrences in p7
    print(f"  count={n} on-article-page={q in alltext[pg]} in-core-article={q in core_text[pg]} in-P7={q in p7joined} claimed-tag={tag} page={pg}")
# what tags does P7 actually print next to phrases? list p. N strings in P7
print("  P7 'p. N' strings:", sorted(set(re.findall(r"p\. \d", p7joined))))

print("== F. images payload identity + credits ==")
for pg in PAGES:
    cs, _ = texts(CORE, pg); es, _ = texts(ED, pg)
    # need raw src for base64 payloads
    craw = open(os.path.join(CORE, pg + ".svg"), encoding="utf-8").read()
    eraw = open(os.path.join(ED, pg + ".svg"), encoding="utf-8").read()
    cp = sorted(re.findall(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', craw))
    ep = sorted(re.findall(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', eraw))
    ch = [hashlib.sha256(base64.b64decode(p)).hexdigest()[:16] for p in cp]
    eh = [hashlib.sha256(base64.b64decode(p)).hexdigest()[:16] for p in ep]
    print(f"  {pg}: core={len(cp)} ed={len(ep)} identical={ch==eh} {ch}")
    for t in texts(ED, pg)[1]:
        if t["t"].startswith("Photo:"):
            print(f"    credit {pg}: {t['t']}")

print("== G. furniture three-way ==")
for d, lab in [(CORE, "core"), (W43, "w43"), (ED, "edition")]:
    _, ts = texts(d, "p1-front")
    badge = [t for t in ts if abs(t["y"] - 378) < 3]
    print(f"  P1 badge {lab}: {[(t['t'][:80], t['size'], ('BRICK' if '#a4553a' in t['raw'] else 'OLIVE' if '#3e4c2a' in t['raw'] else t['raw'][-60:])) for t in badge]}")
for d, lab in [(CORE, "core"), (W43, "w43"), (ED, "edition")]:
    _, ts = texts(d, "p1-front")
    foot = [t["t"] for t in ts if t["t"].startswith("Lucerna ·")]
    print(f"  P1 footer {lab}: {foot}")
    _, ts8 = texts(d, "p8-test")
    seps = sorted(set(t["t"] for t in ts8 if re.match(r"^— .* —$", t["t"])))
    print(f"  P8 separators {lab}: {seps}")
    gp_ed = sum(1 for pg in PAGES for t in texts(d, pg)[1] if t["t"].startswith("Note —"))
    gp_old = sum(1 for pg in PAGES for t in texts(d, pg)[1] if t["t"].startswith("Notes｜"))
    print(f"  gloss-prefix Note — count {lab}: {gp_ed} | Notes｜ count: {gp_old}")
# W43 P8 dash vs paren style: sample key lines
_, w43p8 = texts(W43, "p8-test")
dash = [t["t"] for t in w43p8 if re.match(r"^\d+\. ", t["t"])][:6]
print("  W43 P8 sample key lines:", dash)
_, edp8 = texts(ED, "p8-test")
edash = [t["t"] for t in edp8 if re.match(r"^\d+\. ", t["t"])][:6]
print("  ED  P8 sample key lines:", edash)
_, corep8 = texts(CORE, "p8-test")
cdash = [t["t"] for t in corep8 if re.match(r"^\d+\. ", t["t"])][:6]
print("  CORE P8 sample key lines:", cdash)

print("== H. readers corner ==")
frozen = "延期披露：VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
print("  frozen disclosure byte-identical in edition P7:", frozen in p7joined)
print("  frozen disclosure byte-identical in core P7:", frozen in "".join(t["t"] for t in texts(CORE, 'p7-lang')[1]))
for needle in ["Lettre d'exemple", "écrivez-nous !", "pas une vraie lettre"]:
    i = p7joined.find(needle)
    print(f"  {needle!r}: present={i>=0} ctx={p7joined[max(0,i-60):i+40]!r}" if i >= 0 else f"  {needle!r}: ABSENT")

print("== I. P4 title wrap ==")
_, p4 = texts(ED, "p4-sport")
for t in p4:
    if "棒球詞卡" in t["t"] or "Les mots du baseball" in t["t"]:
        print(f"  x={t['x']} y={t['y']} size={t['size']} {t['t']!r}")

print("== J. P7 geometry approx (ink bottom = baseline + 0.30*size) ==")
_, p7 = texts(ED, "p7-lang")
col1 = [t for t in p7 if 60 <= t["x"] <= 500 and t["y"] < 1700]
if col1:
    m = max(t["y"] + 0.30 * t["size"] for t in col1)
    mb = max(t["y"] for t in col1)
    print(f"  P7 col1 (x 60-500, y<1700): n={len(col1)} max baseline={mb} max ink-bottom~{m:.2f} (design bottom 1560)")
body = [t for t in p7 if t["y"] < 2580]
print(f"  P7 all non-footer: max ink-bottom~{max(t['y']+0.30*t['size'] for t in body):.2f} max baseline={max(t['y'] for t in body)}")
_, p7c = texts(CORE, "p7-lang")
bodyc = [t for t in p7c if t["y"] < 2580]
print(f"  CORE P7 all non-footer: max ink-bottom~{max(t['y']+0.30*t['size'] for t in bodyc):.2f}")

print("== K. residual Latin inventory ==")
lat = set()
for pg in PAGES:
    for t in texts(ED, pg)[1]:
        if re.search(r"[A-Za-z]", t["t"]):
            lat.add(t["t"])
for s in sorted(lat):
    print(f"  {s[:130]!r}")
print("  unique Latin strings:", len(lat))
markers = ["Fill in", "Answer keys", "Word of the week", "Over to you", "Did you get it", "in English", "Traditional Chinese text", "English explanations", "Notes｜", "Staff report", "Test & keys", "True or false", "The big quiz", "Read and answer", "Say it in context", "Writing", "This week", "Life", "Deep read", "Language focus", "Youth"]
full_ed = "".join("".join(t["t"] for t in texts(ED, pg)[1]) for pg in PAGES)
for mk in markers:
    if mk in full_ed:
        print(f"  ENGLISH MARKER PRESENT: {mk!r}")
print("  marker scan done (absent unless listed above)")

print("== L. transform conversion-logic grep ==")
tfr = open(os.path.join(FRB, "transform_fr.py"), encoding="utf-8").read()
for pat in ["opencc", "OpenCC", "s2t", "t2s", "zhconv", "convert", "mapping", "Simplified", "简体"]:
    print(f"  {pat}: {tfr.count(pat)}")
print("  transform lines:", len(tfr.splitlines()))

print("== M. P8 writing model identity core vs edition ==")
def model(d):
    j = "".join(t["t"] for t in texts(d, "p8-test")[1])
    return j
cj, ej = model(CORE), model(ED)
# model text starts after 'Model answer:' / 'Texte modèle :'
import re as _re
cm = _re.search(r"Model answer: (.*?)答案", cj, _re.S)
em = _re.search(r"Texte modèle : (.*?)Réponses", ej, _re.S)
print("  core model found:", bool(cm), "ed model found:", bool(em))
if cm and em:
    print("  model identical:", cm.group(1) == em.group(1), "| model chars:", len(cm.group(1)), "| CJK chars:", sum(1 for c in cm.group(1) if iscjk(c)))
    if cm.group(1) != em.group(1):
        print("  CORE:", cm.group(1)[:200]); print("  ED:", em.group(1)[:200])

print("== N. P4/P6 bar widths (rect widths in chart fill colors) ==")
for pg in ["p4-sport", "p6-deep"]:
    for d, lab in [(CORE, "core"), (ED, "ed")]:
        raw = open(os.path.join(d, pg + ".svg"), encoding="utf-8").read()
        rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" fill="#(?:a4553a|3e4c2a)"', raw)
        print(f"  {pg} {lab}: bar rects (x,y,w,h) = {rects}")
