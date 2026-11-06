#!/usr/bin/env python3
import html, json, os, re, sys, hashlib, base64
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-en-de")
CO = os.path.join(BASE, "files/weekly-report-w45-en-core")
W43 = os.path.join(BASE, "files/weekly-report-en-de")
OUT = os.path.join(BASE, "hidden_files/w45/en-de-proof")
TEXT_RE = re.compile(r"<text([^>]*)>(.*?)</text>", re.S)
ATTR_RE = re.compile(r'([\w-]+)="([^"]*)"')
def load(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for a, c in TEXT_RE.findall(s):
        at = dict(ATTR_RE.findall(a))
        out.append({"x": float(at.get("x", 0)), "y": float(at.get("y", 0)),
                    "size": float(at.get("font-size", 0)), "fam": at.get("font-family", ""),
                    "bold": at.get("font-weight") == "700", "anchor": at.get("text-anchor", "start"),
                    "text": html.unescape(re.sub(r"<[^>]+>", "", c))})
    return out, s
PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-jeunesse", "p6-politique", "p7-langue", "p8-exercices"]
ed, co = {}, {}
for p in PAGES:
    ed[p], _ = load(os.path.join(ED, "svg", p + ".svg"))
    co[p], _ = load(os.path.join(CO, "svg", p + ".svg"))

print("== Core gloss recount (prefix 译注｜讲解｜) ==")
def gloss_reassemble(texts, prefix):
    res = []
    for i, t in enumerate(texts):
        if t["text"].startswith(prefix):
            parts = [t["text"][len(prefix):]]
            j = i + 1
            while j < len(texts) and texts[j]["x"] == t["x"] and texts[j]["size"] == t["size"]:
                parts.append(texts[j]["text"]); j += 1
            res.append(" ".join(parts))
    return res
for p in ["p2-life", "p3-culture", "p4-sport", "p5-jeunesse", "p6-politique"]:
    c = gloss_reassemble(co[p], "译注｜讲解｜")
    e = gloss_reassemble(ed[p], "Anmerkung | ")
    print(f"{p}: core={[len(x.split('·')) for x in c]} edition={[len(x.split('·')) for x in e]}")
    print(f"   core: {c}")
    print(f"   ed:   {e}")
    # headword correspondence: English headword before '=' in each item
    def heads(s):
        return [it.split("=")[0].strip() for it in s.split("·")]
    if c and e: print(f"   headwords core={heads(c[0])} ed={heads(e[0])} match={heads(c[0])==heads(e[0])}")

print("\n== P7 golden 2x (joined page text, paper ' ?' spacing) ==")
GOLD = [
    ("Tuesday, November 3, is Election Day in the United States.", "p1-front"),
    ("The hour from 1 to 2 happened twice.", "p2-life"),
    ("Which film would you choose ?", "p3-culture"),
    ("Two games, two continents, one league — that is the modern NFL.", "p4-sport"),
    ("The results will still be there in the morning.", "p5-jeunesse"),
    ("Patience is part of the system, not a failure of it.", "p6-politique"),
    ("Not every place changes.", "p2-life"),
    ("One Sunday is not enough — good thing the week has seven days.", "p4-sport"),
]
for sent, art in GOLD:
    joined_ed = {p: " ".join(t["text"] for t in ed[p]) for p in PAGES}
    joined_co = {p: " ".join(t["text"] for t in co[p]) for p in PAGES}
    ed_pages = [p for p in PAGES if sent in joined_ed[p]]
    co_pages = [p for p in PAGES if sent in joined_co[p]]
    print(f"{sent[:45]!r}: edition pages={ed_pages} core pages={co_pages}")
print("P7 phrase numbers/levels (from registry):")
reg = json.load(open(os.path.join(OUT, "registry-edition.json")))
for e in reg:
    if 100 <= e["n"] <= 111:
        print(f"  {e['n']} page={e['page']} level={e['level']} type={e['type']}")
print("P7 structure heads edition:")
for t in ed["p7-langue"]:
    if t["size"] >= 25 and t["bold"]:
        print(f"  y={t['y']} {t['text']!r}")
print("P7 structure heads core:")
for t in co["p7-langue"]:
    if t["size"] >= 25 and t["bold"]:
        print(f"  y={t['y']} {t['text']!r}")

print("\n== P7 definitions: core top-column English sentences present in edition P7 ==")
# Definitions live in content7 top columns; extract from core build source strings is not rendered-only.
# Rendered check: every core P7 text line that is pure-English prose (len>25, no CJK) must occur in edition P7 joined text,
# except lines that are section furniture (German halves) — report any missing pure-English line.
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
ed_p7 = " ".join(t["text"] for t in ed["p7-langue"])
missing = []
for t in co["p7-langue"]:
    s = t["text"]
    if len(s) > 25 and not CJK.search(s) and re.search(r"[a-z]", s):
        if s not in ed_p7:
            missing.append(s)
print(f"core P7 pure-English long lines missing from edition P7 joined text: {len(missing)}")
for s in missing: print(f"   MISSING: {s!r}")

print("\n== Readers corner: letter verbatim core vs edition ==")
def corner_texts(texts):
    # lines between READERS' CORNER head and NEXT WEEK head
    idx = [i for i, t in enumerate(texts) if "READERS' CORNER" in t["text"]]
    nxt = [i for i, t in enumerate(texts) if "NEXT WEEK" in t["text"]]
    if idx and nxt: return [t["text"] for t in texts[idx[0]+1:nxt[0]]]
    return []
ce, ee = corner_texts(co["p7-langue"]), corner_texts(ed["p7-langue"])
print("core corner lines:")
for l in ce: print(f"  CO: {l!r}")
print("edition corner lines:")
for l in ee: print(f"  ED: {l!r}")
print("core corner joined contains 'best'?", "best" in " ".join(ce), "| 'VOL.1'?", "VOL.1" in " ".join(ce))
print("edition letter English lines == core letter English lines?",
      [l for l in ee if re.search(r"[A-Za-z]", l) and not l.startswith("Anmerkung")] == [l for l in ce if re.search(r"[A-Za-z]", l)])
# disclosure box bounds: rects on P7 containing disclosure lines
_, p7raw = load(os.path.join(ED, "svg/p7-langue.svg"))
s = open(os.path.join(ED, "svg/p7-langue.svg"), encoding="utf-8").read()
rects = []
for m in re.finditer(r"<rect([^>]*)/>", s):
    a = dict(ATTR_RE.findall(m.group(1)))
    try: rects.append((float(a.get("x", 0)), float(a.get("y", 0)), float(a.get("width", 0)), float(a.get("height", 0)), a.get("fill", ""), a.get("stroke", "")))
    except ValueError: pass
disc = [t for t in ed["p7-langue"] if t["x"] == 1013.0 and t["size"] == 20]
print(f"disclosure lines y: {[t['y'] for t in disc]}")
for r in rects:
    x, y, w, h, fl, st = r
    if st and x <= 1013 and 1013 + 848 <= x + w and y <= disc[0]["y"] and disc[-1]["y"] + 20 <= y + h:
        print(f"  containing bordered rect: x={x} y={y} w={w} h={h} bottom={y+h} last-baseline={disc[-1]['y']} slack={(y+h)-(disc[-1]['y']):.1f}")

print("\n== P8 battery E bodies 137-140 (edition) ==")
p8 = ed["p8-exercices"]
for i, t in enumerate(p8):
    if "Übersetze:" in t["text"] or "Translate:" in t["text"]:
        print(f"  line {i}: {t['text']!r} (next: {p8[i+1]['text']!r} )" if i+1 < len(p8) else f"  line {i}: {t['text']!r}")

print("\n== Extra-72 note verification (segments) ==")
sys.path.insert(0, os.path.join(BASE, "tools"))
import importlib.util
spec = importlib.util.spec_from_file_location("p8mod", os.path.join(BASE, "tools/p8.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
def segs(path):
    texts = m.load_texts(path)
    els = m.answers_elements(texts)
    return m.split_joined(els, 150) or m.split_lines(els, 150)
cs, es = segs(os.path.join(CO, "svg/p8-exercices.svg")), segs(os.path.join(ED, "svg/p8-exercices.svg"))
ce = json.load(open(os.path.join(OUT, "p8-extract-core.json"))); ee = json.load(open(os.path.join(OUT, "p8-extract-edition.json")))
extra = sorted(set(ee["noted_set"]) - set(ce["noted_set"]))
bad = []
for n in extra:
    has_note_ed, _, _ = m.detect_note(es[n])
    has_note_co, _, _ = m.detect_note(cs[n])
    if not has_note_ed or has_note_co: bad.append((n, has_note_co, has_note_ed, cs[n][:60], es[n][:60]))
print(f"extra={len(extra)} bad={len(bad)} (edition-noted but core-bare expected)")
for b in bad: print("  ", b)
# also: every core-noted key matches edition key except keydiffs (already from compare), and P8 notes German: edition segments CJK?
print("edition P8 segments with CJK:", [n for n, s in es.items() if CJK.search(s)])

print("\n== Removed P1-P7 (c) items list ==")
diff = json.load(open(os.path.join(OUT, "freeze-diff-proof.json")))
with open(os.path.join(OUT, "removed-strings.txt"), encoding="utf-8") as f: txt = f.read()
for line in txt.splitlines():
    if "c-rewrap" in line and ("[P1]" in line or "[P2]" in line or "[P3]" in line or "[P4]" in line or "[P5]" in line or "[P6]" in line or "[P7]" in line):
        print("  ", line)
print("\n== P8 fragments: each fragment's words belong to consecutive registry keys ==")
reg_ed = {e["n"]: e for e in json.load(open(os.path.join(OUT, "registry-edition.json")))}
for frag in ['1. ballot · 2. midterm · 3. November 3 · 4. early · 5.', '75. d · 76. b · 77. a · 78. The map is changing colour now.']:
    nums = re.findall(r"(\d+)\.\s*([^·]+)", frag)
    print(f"  frag {frag[:40]!r}: nums={[n for n, _ in nums]} registry keys={[reg_ed[int(n)]['key'] for n, _ in nums if int(n) in reg_ed]}")

print("\n== Images + credits ==")
for p in PAGES:
    def imgs(path):
        s = open(path, encoding="utf-8").read()
        return [hashlib.sha256(base64.b64decode(m.group(1))).hexdigest()[:16] for m in re.finditer(r"data:image/(?:jpeg|png);base64,([A-Za-z0-9+/=]+)", s)]
    ei, ci = imgs(os.path.join(ED, "svg", p + ".svg")), imgs(os.path.join(CO, "svg", p + ".svg"))
    print(f"{p}: edition images={len(ei)} core images={len(ci)} payloads equal={ei==ci} {ei}")
def credits(texts):
    return [t["text"] for t in texts if "Wikimedia" in t["text"] or "Commons" in t["text"] or "©" in t["text"] or "Photo" in t["text"] or "Credit" in t["text"]]
for p in PAGES:
    if credits(ed[p]) or credits(co[p]):
        print(f"{p} credits ed={credits(ed[p])} co={credits(co[p])} equal={credits(ed[p])==credits(co[p])}")
print("\n== PDFs ==")
try:
    from pypdf import PdfReader
    for label, path in [("ed-print", os.path.join(ED, "The-Lucerna-VOL2-DE.pdf")), ("ed-web", os.path.join(ED, "The-Lucerna-VOL2-DE-web.pdf"))]:
        r = PdfReader(path); print(f"{label}: pages={len(r.pages)} size={os.path.getsize(path)} sha={hashlib.sha256(open(path,'rb').read()).hexdigest()}")
except Exception as e:
    print("pypdf fail", e)
print("ABSTRACT lines:", open(os.path.join(ED, "ABSTRACT.txt"), encoding="utf-8").read().count("\n"), "content:", repr(open(os.path.join(ED, "ABSTRACT.txt"), encoding="utf-8").read()))
print("Masthead P1:", [t["text"] for t in ed["p1-front"] if t["text"] == "The Lucerna"], "badge:", [t["text"] for t in ed["p1-front"] if "ENGLISCHER TEXT" in t["text"]])
print("DONE")
