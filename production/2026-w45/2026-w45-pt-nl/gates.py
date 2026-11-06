# -*- coding: utf-8 -*-
"""Full gate battery for PT x NL W45 (builder self-check, round 3 output).
Reads only rendered SVGs + build sources; never imports content modules.
Methods stated per check; PIL used for ink/advance measurements.
"""
import re, os, sys, hashlib
from PIL import ImageFont

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-nl/svg")
CO = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-core/svg")
EB = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-nl-build")
CB = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-build")

FONTS = {
    ("Noto Sans CJK SC", False): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 0),
    ("Noto Sans CJK SC", True): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", 0),
    ("Noto Serif CJK SC", False): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 0),
    ("Noto Serif CJK SC", True): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc", 0),
    ("UnifrakturMaguntia", False): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", 0),
    ("UnifrakturMaguntia", True): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf", 0),
}
_cache = {}
def font(fam, bold, size):
    key = (fam, bold, size)
    if key not in _cache:
        path, idx = FONTS.get((fam, bold), FONTS[("Noto Sans CJK SC", False)])
        try:
            _cache[key] = ImageFont.truetype(path, int(round(size)), index=idx)
        except Exception:
            _cache[key] = ImageFont.truetype(path, int(round(size)))
    return _cache[key]

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"(?: font-weight="700")?[^>]*?(?: text-anchor="(\w+)")?>([^<]*)</text>')

def texts_of(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in TEXT_RE.finditer(s):
        x, y, fam, size = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4))
        anchor = m.group(5) or "start"
        bold = 'font-weight="700"' in m.group(0)
        out.append({"x": x, "y": y, "fam": fam, "size": size, "bold": bold,
                    "anchor": anchor, "t": m.group(6)})
    return out, s

def inkbox(t):
    """Ink box via PIL getbbox anchor='ls' (baseline origin) + advance shift."""
    f = font(t["fam"], t["bold"], t["size"])
    try:
        l, tp, r, b = f.getbbox(t["t"], anchor="ls")
        adv = f.getlength(t["t"])
    except Exception:
        return (t["x"], t["y"] - t["size"], t["x"] + len(t["t"]) * t["size"] * 0.6, t["y"])
    if t["anchor"] == "middle":
        ox = t["x"] - adv / 2
    elif t["anchor"] == "end":
        ox = t["x"] - adv
    else:
        ox = t["x"]
    return (ox + l, t["y"] + tp, ox + r, t["y"] + b)

def advbox(t):
    f = font(t["fam"], t["bold"], t["size"])
    adv = f.getlength(t["t"])
    if t["anchor"] == "middle":
        return (t["x"] - adv / 2, t["x"] + adv / 2)
    if t["anchor"] == "end":
        return (t["x"] - adv, t["x"])
    return (t["x"], t["x"] + adv)

pages = ["p1-capa", "p2-vida", "p3-cultura", "p4-esporte", "p5-jovens",
         "p6-aprofundamento", "p7-lingua", "p8-avaliacao"]
EDT, COT = {}, {}
for pg in pages:
    EDT[pg], _ = texts_of(os.path.join(ED, pg + ".svg"))
    COT[pg], _ = texts_of(os.path.join(CO, pg + ".svg"))

CJK = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff\u3000-\u303f\uff00-\uffef]')
print("== 1. CJK per page (rendered text nodes) ==")
for pg in pages:
    txt = "".join(t["t"] for t in EDT[pg])
    print(f"  {pg}: edition CJK {len(CJK.findall(txt))} (core {len(CJK.findall(''.join(t['t'] for t in COT[pg])))} )")

EN_PHRASES = ["Note | ", "Page ", " of 8", "Answers on page", "Levels are mixed",
              "Complete the sentence", "Multiple choice", "Build the sentence",
              "True or false", "Cloze", "Vocabulary matching", "Sentence building",
              "Fill in", "Match the pairs", "IN THIS ISSUE", "IN NUMBERS",
              "Text in Portuguese", "Explanations in English",
              "THE EDITION FOR ENGLISH-SPEAKING", "PORTUGUESE WEEKLY",
              "HINWEIS", "Seite ", "EXPLICATIONS EN", "EXPLICACIONES EN",
              "SPIEGAZIONI IN", "Nota — ", "TEST IN PORTUGUESE"]
print("== 2. English/other-family apparatus residual scan (all 8 pages) ==")
found = []
for pg in pages:
    txt = " ".join(t["t"] for t in EDT[pg])
    for ph in EN_PHRASES:
        if ph in txt:
            found.append((pg, ph))
print("  hits:", found if found else "NONE (0)")

print("== 3. Footer / badge / page lines ==")
for i, pg in enumerate(pages, 1):
    fl = [t["t"] for t in EDT[pg] if t["y"] == 2624 and t["anchor"] == "start"]
    fr = [t["t"] for t in EDT[pg] if t["y"] == 2624 and t["anchor"] == "end"]
    ok = (fl and "PORTUGEES WEEKBLAD VOL.2" in fl[0]
          and "TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS" in fl[0]
          and fr == [f"Pagina {i} van 8"])
    print(f"  {pg}: footer_ok={ok} left={fl} right={fr}")
p1badge = [t for t in EDT["p1-capa"] if t["y"] == 372]
print("  P1 badge:", [(t["t"], t["size"], t["bold"], t["fam"]) for t in p1badge])
p1sub = [t for t in EDT["p1-capa"] if t["y"] == 330]
print("  P1 subtitle:", [(t["t"], t["size"]) for t in p1sub])

print("== 4. Gloss counts (build-source gloss() strings, split on U+00B7 itself) ==")
import glob as _glob
def gloss_counts(bdir):
    res = {}
    fmap = {"content12.py": ["p2-vida"], "content34.py": ["p3-cultura", "p4-esporte"],
            "content56.py": ["p5-jovens", "p6-aprofundamento"]}
    for fn, pgs in fmap.items():
        src = open(os.path.join(bdir, fn), encoding='utf-8').read()
        calls = re.findall(r'\.gloss\("([^"]*)"\)', src)
        # assign in file order to pages that carry a gloss (one per page in this build)
        for call, pg in zip(calls, pgs):
            items = [it.strip().strip("。").strip(".") for it in call.split("·")]
            items = [it for it in items if it]
            res[pg] = items
    return res
gc_ed, gc_co = gloss_counts(EB), gloss_counts(CB)
tot_e = tot_c = 0
for pg in ["p2-vida", "p3-cultura", "p4-esporte", "p5-jovens", "p6-aprofundamento"]:
    ce, cc = gc_ed.get(pg, []), gc_co.get(pg, [])
    tot_e += len(ce); tot_c += len(cc)
    # each edition item's PT head term must survive in the render
    svg_txt = " ".join(t["t"] for t in EDT[pg])
    missing = [it for it in ce if it.split("=")[0].strip() not in svg_txt]
    print(f"  {pg}: core {len(cc)} edition {len(ce)} missing_in_render={missing}")
print(f"  TOTAL gloss items core {tot_c} edition {tot_e}")

print("== 5. P7 quotes: 2x each, tagged page, PT verbatim ==")
src7 = open(os.path.join(CB, "content7.py"), encoding='utf-8').read()
quotes = re.findall(r'\("«([^»]*)»", "[^"]*", "(Página \d+)"\)', src7)
# fallback: parse the quotes list block directly
if len(quotes) != 8:
    block = src7[src7.index("quotes = ["):src7.index("]\n", src7.index("quotes = ["))]
    quotes = re.findall(r'"«([^»]*)»".*?"(Página \d+)"', block)
alltxt = {}
for pg in pages:
    alltxt[pg] = re.sub(r"\s+", " ", " ".join(t["t"] for t in EDT[pg])).replace("«", "").replace("»", "")
for q, pg_tag in quotes:
    qn = re.sub(r"\s+", " ", q).strip()
    total = sum(alltxt[pg].count(qn) for pg in pages)
    pgfile = {"Página 1": "p1-capa", "Página 2": "p2-vida", "Página 3": "p3-cultura",
              "Página 4": "p4-esporte", "Página 5": "p5-jovens", "Página 6": "p6-aprofundamento"}[pg_tag]
    onpage = qn in alltxt[pgfile]
    print(f"  {qn[:52]!r} total={total} tag={pg_tag} on_tagged_page={onpage}")

print("== 6. P7 word box + readers corner ==")
wt = "« feriadão »: sábado, domingo e segunda — três dias de descanso."
ed7 = " ".join(t["t"] for t in EDT["p7-lingua"])
co7 = " ".join(t["t"] for t in COT["p7-lingua"])
print("  wt PT verbatim in edition:", wt in ed7, "| in core:", wt in co7)
disc_pt = "Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3."
print("  disc_pt verbatim in edition:", disc_pt in ed7)
lt = "«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO"
print("  example letter lt identical:", lt in ed7 and lt in co7)
for frag in ["Voorbeeld van de redactie — geen echte brief",
             "Stuur je brief op",
             "de beste verschijnen op pagina 7 in VOL.3",
             "Opmerking van de redactie",
             "waren nog niet binnen",
             "het voorbeeld blijft, de belofte gaat naar VOL.3"]:
    print(f"  NL corner fragment {frag[:45]!r}: {frag in ed7}")

print("== 7. P8 key-token comparison (dash style: token before first ' — ') ==")
def answer_map(pgtexts):
    items, cur = {}, None
    for t in pgtexts:
        s = t["t"]
        if t["y"] == 2624:
            continue  # footer, never an answer continuation
        m = re.match(r"^(\d+)\. (.*)$", s)
        if m:
            # P8 exercise bodies (113-150) come first in document order and
            # are overwritten by the later answer-key lines with the same
            # numbers; 1-112 exist only in the key section.
            cur = int(m.group(1)); items[cur] = m.group(2)
        elif cur is not None and not re.match(r"^— Pagina", s) and not re.match(r"^RESPOSTAS", s):
            # continuation of a wrapped answer line (same column flow order)
            if items[cur] and not s.startswith("A Lucerna"):
                items[cur] += " " + s
    toks = {}
    for n, line in items.items():
        if line.startswith("✓"):
            toks[n] = "✓-APPARATUS"
        elif " — " in line:
            toks[n] = line.split(" — ")[0]
        else:
            toks[n] = line
    return toks
te, tc = answer_map(EDT["p8-avaliacao"]), answer_map(COT["p8-avaliacao"])
diff = {n: (tc.get(n), te.get(n)) for n in sorted(set(tc) | set(te)) if tc.get(n) != te.get(n)}
print(f"  numbers compared: core {len(tc)} edition {len(te)}; token diffs: {sorted(diff)}")
for n, (a, b) in sorted(diff.items()):
    print(f"    {n}: core={a!r} edition={b!r}")

print("== 8. Same-baseline ink overlap scan (PIL, all pages) ==")
flags = []
for pg in pages:
    ts = EDT[pg]
    boxes = [(t, inkbox(t)) for t in ts]
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            (t1, b1), (t2, b2) = boxes[i], boxes[j]
            if abs(t1["y"] - t2["y"]) > 0.5:
                continue
            ox = min(b1[2], b2[2]) - max(b1[0], b2[0])
            oy = min(b1[3], b2[3]) - max(b1[1], b2[1])
            if ox > 1.0 and oy > 0.5:
                flags.append((pg, t1["t"][:40], t2["t"][:40], round(ox, 1), round(oy, 1)))
print("  same-baseline overlap flags:", flags if flags else "0")

print("== 9. Frame / right-edge scan (ADVANCE method; frames outer 28..1922, inner 40..1910) ==")
for pg in pages:
    maxr, minl, worst = 0, 9999, []
    for t in EDT[pg]:
        al, ar = advbox(t)
        ib = inkbox(t)
        maxr = max(maxr, ar); minl = min(minl, al)
        if ar > 1910.01 or al < 39.99:
            worst.append((t["t"][:40], round(al, 1), round(ar, 1)))
        if t["y"] not in (2624,) and ib[3] > 2580:
            worst.append(("BELOW-FOOTER-RULE " + t["t"][:30], round(ib[3], 1)))
    print(f"  {pg}: max_adv_right={maxr:.1f} min_adv_left={minl:.1f} defects={worst if worst else 'NONE'}")

print("== 10. P6 chart-label coverage, baseline-anchored ink vs later rects ==")
s6 = open(os.path.join(ED, "p6-aprofundamento.svg"), encoding='utf-8').read()
# document-order walk of <text> and <rect>
tokens = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^/]*/>|<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"(?: font-weight="700")?[^>]*?(?: text-anchor="(\w+)")?>([^<]*)</text>', s6)
items = []
for m in tokens:
    if m[0]:
        items.append(("rect", float(m[0]), float(m[1]), float(m[2]), float(m[3])))
    else:
        items.append(("text", m[4], m[5], m[6], m[7], m[8] or "start", m[9]))
for idx, it in enumerate(items):
    # it = ("text", x, y, fam, size, anchor, text)
    if it[0] == "text" and it[6] in ("portões abertos", "espera", "prova", "60 min", "30 min", "330 min"):
        t = {"x": float(it[1]), "y": float(it[2]), "fam": it[3], "size": float(it[4]),
             "bold": it[6] in ("portões abertos", "espera", "prova"), "anchor": it[5], "t": it[6]}
        ib = inkbox(t)
        area = max(0, ib[2] - ib[0]) * max(0, ib[3] - ib[1])
        cov = 0.0
        for later in items[idx + 1:]:
            if later[0] == "rect":
                _, rx, ry, rw, rh = later
                ox = min(ib[2], rx + rw) - max(ib[0], rx)
                oy = min(ib[3], ry + rh) - max(ib[1], ry)
                if ox > 0 and oy > 0:
                    cov += ox * oy
        print(f"  label {it[6]!r}: ink={tuple(round(v, 1) for v in ib)} coverage={100 * cov / area if area else 0:.1f}%")

print("== 11. Image blob + credit ==")
def blobs(path):
    s = open(path, encoding='utf-8').read()
    return [hashlib.sha256(b.encode()).hexdigest() for b in re.findall(r'data:image/\w+;base64,([A-Za-z0-9+/=]+)', s)]
be, bc = blobs(os.path.join(ED, "p1-capa.svg")), blobs(os.path.join(CO, "p1-capa.svg"))
print("  image blobs edition==core:", be == bc, be)
p1txt = " ".join(t["t"] for t in EDT["p1-capa"])
print("  credit line present:", "Foto: Gary Todd / Wikimedia Commons — CC0" in p1txt)
print("  CREDITS.md:", open(os.path.join(EB, "assets", "CREDITS.md"), encoding='utf-8').read().strip())
