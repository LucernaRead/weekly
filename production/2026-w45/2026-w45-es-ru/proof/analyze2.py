#!/usr/bin/env python3
import re, os, json
from collections import Counter
H = os.environ['HOME'] + "/workspace/goals/lucernaread-social-media-operations/files/"
ED = H + "weekly-report-w45-es-ru/svg/"
CO = H + "weekly-report-w45-es-core/svg/"
PAGES = ["p1-portada","p2-vida","p3-cultura","p4-deporte","p5-juventud","p6-afondo","p7-lengua","p8-ejercicios"]
def texts(path):
    s = open(path, encoding='utf-8').read()
    els = []
    for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)"([^>]*)>(.*?)</text>', s, re.S):
        x, y, a, inner = m.groups()
        els.append({"x": float(x), "y": float(y), "attrs": a, "text": re.sub(r'<[^>]+>', '', inner)})
    return els
def raw(path):
    return open(path, encoding='utf-8').read()
# --- clean Latin token diff ---
WORD = re.compile(r"[A-Za-z\u00c1\u00c9\u00cd\u00d3\u00da\u00dc\u00d1\u00e1\u00e9\u00ed\u00f3\u00fa\u00fc\u00f1]+|\d+(?:[.,]\d+)?")
def toks(els):
    c = Counter()
    for e in els:
        for t in WORD.findall(e["text"]):
            c[t] += 1
    return c
tot_add, tot_rem = Counter(), Counter()
per_page = {}
for p in PAGES:
    ce, co = toks(texts(ED+p+".svg")), toks(texts(CO+p+".svg"))
    add = {k: ce[k]-co[k] for k in set(ce) if ce[k] > co.get(k, 0)}
    rem = {k: co[k]-ce[k] for k in set(co) if co[k] > ce.get(k, 0)}
    per_page[p] = {"added": add, "removed": rem}
    tot_add.update(add); tot_rem.update(rem)
print("TOKEN per page:")
for p, d in per_page.items():
    print(" ", p, "added:", d["added"], "removed:", d["removed"])
print("TOKEN totals added:", dict(tot_add))
print("TOKEN totals removed:", dict(tot_rem))
# --- quotes normalized ---
def norm_all(path_list):
    txt = " ".join(e["text"] for path in path_list for e in texts(path))
    return re.sub(r"\s+", " ", txt)
norm_ed = norm_all([ED+p+".svg" for p in PAGES])
norm_co = norm_all([CO+p+".svg" for p in PAGES])
quotes = [
 "Las listas ya están presentadas: ahora los partidos escriben sus programas.",
 "El lunes 2 de noviembre es festivo en nueve comunidades — y día de trabajo en las demás.",
 "Tres fiestas, una misma noche de otoño.",
 "El Madrid ganó 2–1 en el Camp Nou: fue la primera derrota liguera del Barça.",
 "El Bernabéu cambia el césped por el emparrillado: el fútbol americano llega a Madrid.",
 "La vivienda es el principal problema para el 55,7 % de los españoles.",
 "Una encuesta es una foto con margen de error, tomada en un día concreto.",
 "El domingo 8, Madrid tiene dos citas: la NFL a las 15:30 y el Atlético–Barça a las 21:00.",
]
print("QUOTES normalized counts ed:", {q[:30]: norm_ed.count(re.sub(r"\s+", " ", q)) for q in quotes})
print("QUOTES normalized counts co:", {q[:30]: norm_co.count(re.sub(r"\s+", " ", q)) for q in quotes})
# --- gloss: join para lines ---
def gloss_items(els, start_marker):
    els_sorted = sorted(els, key=lambda e: (e["x"], e["y"]))
    for i, e in enumerate(els_sorted):
        if start_marker in e["text"]:
            x0 = e["x"]; lines = [e["text"]]; prev_y = e["y"]
            for f in els_sorted[i+1:]:
                if f["x"] == x0 and 0 < f["y"] - prev_y < 45:
                    lines.append(f["text"]); prev_y = f["y"]
                elif f["x"] == x0 and f["y"] > prev_y:
                    break
            joined = " ".join(lines)
            body = joined.split("—", 1)[1] if "—" in joined else joined
            if "｜" in joined:
                body = joined.split("｜", 1)[1]
            items = [s.strip() for s in body.split("·") if s.strip()]
            return lines, items
    return None, []
for p in ["p2-vida","p3-cultura","p4-deporte","p5-juventud"]:
    el, il = gloss_items(texts(ED+p+".svg"), "Пояснение")
    cl, ci = gloss_items(texts(CO+p+".svg"), "译注")
    print("GLOSS", p, "ed n=", len(il), il, "| co n=", len(ci))
    print("   ed lines:", el)
# --- P8 restricted to RESPUESTAS section ---
def p8_answers(path):
    els = texts(path)
    start = None
    for i, e in enumerate(els):
        if e["text"].strip().startswith("RESPUESTAS"):
            start = i; break
    assert start is not None
    ans = {}; cur = None
    for e in els[start+1:]:
        t = e["text"].strip()
        if t.startswith("La Lucerna") or e["y"] == 2624:
            continue
        m = re.match(r'^(\d+)\.\s+(.*)$', t)
        if m:
            cur = int(m.group(1)); ans[cur] = m.group(2)
        elif cur is not None and t and not t.startswith("— СТРАНИЦА"):
            ans[cur] += " " + t
    return ans, els, start
ed_ans, ed_els, st = p8_answers(ED+"p8-ejercicios.svg")
co_ans, _, _ = p8_answers(CO+"p8-ejercicios.svg")
print("P8 answers ed:", len(ed_ans), "co:", len(co_ans), "continuous:", sorted(ed_ans) == list(range(1, 151)))
def dashkey(v):
    return v.split(" — ")[0].strip()
dashdiff = [n for n in range(1, 151) if dashkey(ed_ans[n]) != dashkey(co_ans[n])]
print("P8 dashdiff (RESPUESTAS-only):", dashdiff)
print("P8 #150 ed:", repr(ed_ans[150]))
print("P8 #150 co:", repr(co_ans[150]))
print("P8 #137 ed full:", repr(ed_ans[137]), "| KIT:", repr("Понедельник — выходной в девяти сообществах."))
print("P8 #138 ed full:", repr(ed_ans[138]), "| KIT:", repr("В воскресенье мы смотрим NFL и «Атлетико» — «Барса»."))
print("P8 #139 keys equal:", ed_ans[139].split(" — ")[0] == co_ans[139].split(" — ")[0], "| #140 keys equal:", ed_ans[140].split(" — ")[0] == co_ans[140].split(" — ")[0])
# pagination within RESPUESTAS section
seps = []; counts = []; cur = 0; in_resp = False
for e in ed_els:
    t = e["text"].strip()
    if t.startswith("RESPUESTAS"):
        in_resp = True; continue
    if not in_resp:
        continue
    if t.startswith("— СТРАНИЦА"):
        seps.append(t); counts.append(cur); cur = 0
    elif re.match(r'^\d+\.\s+', t):
        cur += 1
counts.append(cur)
print("P8 pagination (RESPUESTAS-only, incl leading):", counts, "-> sections:", counts[1:], "sum:", sum(counts[1:]))
# --- levels across all pages ---
lvl_ed = Counter(); lvl_co = Counter()
for p in PAGES:
    lvl_ed.update(e["text"].strip() for e in texts(ED+p+".svg") if e["text"].strip() in ("A2","B1","B2"))
    lvl_co.update(e["text"].strip() for e in texts(CO+p+".svg") if e["text"].strip() in ("A2","B1","B2"))
print("LEVEL badge texts all pages ed:", dict(lvl_ed), "co:", dict(lvl_co), "equal:", lvl_ed == lvl_co)
# --- P6 rect diff: exactly which rects differ ---
def rects(path):
    return re.findall(r'<rect[^>]*>', raw(path))
ed6, co6 = rects(ED+"p6-afondo.svg"), rects(CO+"p6-afondo.svg")
ce, cc = Counter(ed6), Counter(co6)
print("P6 rects only-in-ed:", list((ce-cc).elements()))
print("P6 rects only-in-co:", list((cc-ce).elements()))
def parse_rect(r):
    return dict(re.findall(r'(\w[\w-]*)="([^"]*)"', r))
badges_ed = [parse_rect(r) for r in ed6 if parse_rect(r).get("width") == "60" and parse_rect(r).get("height") == "30"]
badges_co = [parse_rect(r) for r in co6 if parse_rect(r).get("width") == "60" and parse_rect(r).get("height") == "30"]
from collections import defaultdict
ge = defaultdict(list); gc = defaultdict(list)
for b in badges_ed: ge[b["x"]].append(b)
for b in badges_co: gc[b["x"]].append(b)
same = 0; yonly = 0; other = 0
for x in sorted(set(ge) | set(gc)):
    ae = sorted(ge[x], key=lambda b: float(b["y"])); ac = sorted(gc[x], key=lambda b: float(b["y"]))
    for be, bc in zip(ae, ac):
        if be["y"] == bc["y"]:
            same += 1
        elif all(be[k] == bc[k] for k in ("x","width","height","fill","rx")):
            yonly += 1
        else:
            other += 1
print("P6 badges by-column pairing: same_y=", same, "y_only=", yonly, "other=", other, "cols ed:", {k: len(v) for k, v in ge.items()})
