#!/usr/bin/env python3
import re, os, json, hashlib
from collections import Counter
H = os.environ['HOME'] + "/workspace/goals/lucernaread-social-media-operations/files/"
ED = H + "weekly-report-w45-es-ru/svg/"
CO = H + "weekly-report-w45-es-core/svg/"
W43 = H + "weekly-report-es-ru/svg/"
PAGES = ["p1-portada","p2-vida","p3-cultura","p4-deporte","p5-juventud","p6-afondo","p7-lengua","p8-ejercicios"]
out = {}
def texts(path):
    s = open(path, encoding='utf-8').read()
    els = []
    for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)"([^>]*)>(.*?)</text>', s, re.S):
        x, y, attrs, inner = m.groups()
        els.append({"x": float(x), "y": float(y), "attrs": attrs, "text": re.sub(r'<[^>]+>', '', inner)})
    return els
def raw(path):
    return open(path, encoding='utf-8').read()
def toks(els):
    c = Counter()
    for e in els:
        for t in re.findall(r"[A-Za-z\xc1\xc9\xcd\xd3\xda\xdc\xd1\xe1\xe9\xed\xf3\xfa\xfc\xf1 0-9]+(?:[.,][0-9]+)?", e["text"]):
            c[t] += 1
    return c
tokdiff = {}
for p in PAGES:
    ce, co = toks(texts(ED+p+".svg")), toks(texts(CO+p+".svg"))
    added = {k: ce[k]-co[k] for k in set(ce) if ce[k] > co.get(k, 0)}
    removed = {k: co[k]-ce[k] for k in set(co) if co[k] > ce.get(k, 0)}
    tokdiff[p] = {"added": added, "removed": removed}
out["token_diff"] = tokdiff
p7ed, p7co = texts(ED+"p7-lengua.svg"), texts(CO+"p7-lengua.svg")
def col1473(els, lo, hi):
    return [(e["y"], e["text"]) for e in els if e["x"] == 1473 and lo <= e["y"] <= hi]
out["p7_ed_cartas"] = col1473(p7ed, 1330, 1840)
out["p7_co_cartas"] = col1473(p7co, 1330, 1840)
out["p7_ed_rects1451"] = re.findall(r'<rect x="1451"[^>]*>', raw(ED+"p7-lengua.svg"))
out["p7_co_rects1451"] = re.findall(r'<rect x="1451"[^>]*>', raw(CO+"p7-lengua.svg"))
out["p7_ed_total_texts"] = len(p7ed)
out["p7_preview"] = [(e["x"], e["y"], e["text"][:80]) for e in p7ed if 2437 <= e["y"] <= 2530]
out["p7_frases_head"] = [(e["x"], e["y"], e["text"]) for e in p7ed if "FRASES DE LA SEMANA" in e["text"]]
ana_ed = [t for _, t in col1473(p7ed, 1380, 1575)]
ana_co = [t for _, t in col1473(p7co, 1380, 1575)]
out["ana_letter_identical_text"] = (ana_ed == ana_co)
out["ana_letter_ed"] = ana_ed
esnote_ed = [t for _, t in col1473(p7ed, 1620, 1720)]
esnote_co = [t for _, t in col1473(p7co, 1620, 1720)]
out["es_note_identical_text"] = (esnote_ed == esnote_co)
disc = " ".join(t for _, t in col1473(p7ed, 1770, 1835))
out["disclosure_joined"] = disc
out["disclosure_lines"] = col1473(p7ed, 1770, 1835)
out["disclosure_has_invitation"] = "Ждём писем!" in disc
out["disclosure_facts"] = {"no_letters": "писем" in disc and "нет" in disc, "no_best_p8": "лучших текстов со страницы 8 нет" in disc, "example_and_vol3": "печатаем пример" in disc and "обещание — на VOL.3" in disc}
out["old_label_present"] = "Примечание редакции:" in raw(ED+"p7-lengua.svg")
out["w43_disclosure"] = [(e["y"], e["text"]) for e in texts(W43+"p7-lengua.svg") if e["x"] == 1473 and 1620 <= e["y"] <= 1670]
alltext = "\n".join(e["text"] for p in PAGES for e in texts(ED+p+".svg"))
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
out["quote_counts"] = {q: alltext.count(q) for q in quotes}
lab = Counter()
for e in p7ed:
    for m in re.finditer(r"\(Страница (\d)\)", e["text"]):
        lab[int(m.group(1))] += 1
out["quote_page_labels"] = dict(sorted(lab.items()))
fix4 = [e for e in p7ed if "американский футбол в Мадриде" in e["text"]]
out["fixup4_elements"] = [(e["x"], e["y"], e["text"]) for e in fix4]
out["old_fixup4_phrase_present"] = "приходит в Мадрид" in alltext
gloss = {}
for p, pg in [("p2-vida","P2"),("p3-cultura","P3"),("p4-deporte","P4"),("p5-juventud","P5"),("p1-portada","P1")]:
    gloss[pg] = {"ed_poyasnenie": raw(ED+p+".svg").count("Пояснение — "), "co_poyasnenie": raw(CO+p+".svg").count("Пояснение — ")}
out["gloss_poyasnenie_counts"] = gloss
def heads(els):
    hs = []
    for e in els:
        if "·" in e["text"]:
            hs.append(e["text"].split("·")[0].strip())
    return hs
out["gloss_heads"] = {p: {"ed": heads(texts(ED+p+".svg")), "co": heads(texts(CO+p+".svg"))} for p in ["p2-vida","p3-cultura","p4-deporte","p5-juventud"]}
def datauris(path):
    return re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', raw(path))
out["image_hashes"] = {}
for p in PAGES:
    ed_u, co_u = datauris(ED+p+".svg"), datauris(CO+p+".svg")
    out["image_hashes"][p] = {"ed": [hashlib.sha256(u.encode()).hexdigest()[:16] for u in ed_u], "co": [hashlib.sha256(u.encode()).hexdigest()[:16] for u in co_u], "identical": [hashlib.sha256(u.encode()).hexdigest() for u in ed_u] == [hashlib.sha256(u.encode()).hexdigest() for u in co_u]}
cjk_total = {}
for p in PAGES:
    s = raw(ED+p+".svg")
    chars = [ch for ch in s if ('\u4e00' <= ch <= '\u9fff' or ch in '（）。，、；：？！「」『』《》〈〉【】')]
    cjk_total[p] = dict(Counter(chars))
out["cjk_per_page"] = cjk_total
orphan = []
for p in PAGES:
    for e in texts(ED+p+".svg"):
        if e["text"] and e["text"][0] in '.,;:!?%)»”':
            orphan.append((p, e["x"], e["y"], e["text"][:60]))
out["orphan_line_starts"] = orphan
out["bridge_term_count"] = {p: raw(ED+p+".svg").count("桥接") for p in PAGES}
def has(page, s):
    return s in raw(ED+page)
out["furniture"] = {
  "p1_badge": has("p1-portada.svg", "ТЕКСТЫ НА ИСПАНСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ"),
  "p1_topband": has("p1-portada.svg", "CADA SEMANA EN ESPAÑOL · КАЖДУЮ НЕДЕЛЮ · ИСПАНСКИЙ ГЛАЗАМИ ИСПАНИИ"),
  "p1_masthead": has("p1-portada.svg", "ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL"),
  "footers": {},
  "p8_respuestas": [e["text"] for e in texts(ED+"p8-ejercicios.svg") if "RESPUESTAS" in e["text"] or "К каждому" in e["text"]],
  "w43_p8_respuestas": [e["text"] for e in texts(W43+"p8-ejercicios.svg") if "RESPUESTAS" in e["text"] or "К каждому" in e["text"]],
}
for i, p in enumerate(PAGES, 1):
    out["furniture"]["footers"][p] = (("Страница %d из 8" % i) in raw(ED+p+".svg")) and ("La Lucerna · ИСПАНСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2" in raw(ED+p+".svg"))
badge = [e for e in texts(ED+"p1-portada.svg") if "ТЕКСТЫ НА ИСПАНСКОМ" in e["text"]]
out["p1_badge_elements"] = [(e["x"], e["y"], e["attrs"]) for e in badge]
badge43 = [e for e in texts(W43+"p1-portada.svg") if "ТЕКСТЫ НА ИСПАНСКОМ" in e["text"]]
out["w43_p1_badge_elements"] = [(e["x"], e["y"], e["attrs"]) for e in badge43]
out["p1_pagina4"] = [e["text"] for e in texts(ED+"p1-portada.svg") if e["text"].strip() == "(Página 4)"]
out["p1_paginas_split"] = [e["text"] for e in texts(ED+"p1-portada.svg") if "Páginas 4" in e["text"]]
out["p1_body_stranitsa4"] = [e["text"] for e in texts(ED+"p1-portada.svg") if "Страница 4" in e["text"] and "из 8" not in e["text"]]
def rects(path):
    return re.findall(r'<rect[^>]*>', raw(path))
def parse_rect(r):
    return dict(re.findall(r'(\w[\w-]*)="([^"]*)"', r))
ed6, co6 = rects(ED+"p6-afondo.svg"), rects(CO+"p6-afondo.svg")
out["p6_rect_multiset_equal"] = (Counter(ed6) == Counter(co6))
bars_ed = [r for r in ed6 if parse_rect(r).get("height") == "22"]
bars_co = [r for r in co6 if parse_rect(r).get("height") == "22"]
out["p6_bars"] = {"ed": len(bars_ed), "co": len(bars_co), "multiset_equal": Counter(bars_ed) == Counter(bars_co)}
badges_ed = [r for r in ed6 if parse_rect(r).get("width") == "60" and parse_rect(r).get("height") == "30"]
badges_co = [r for r in co6 if parse_rect(r).get("width") == "60" and parse_rect(r).get("height") == "30"]
def badge_key(r):
    d = parse_rect(r)
    return (d.get("x"), d.get("width"), d.get("height"), d.get("fill"), d.get("rx"))
same_y = 0
for a in badges_ed:
    for b in badges_co:
        if badge_key(a) == badge_key(b) and parse_rect(a).get("y") == parse_rect(b).get("y"):
            same_y += 1
            break
y_only = 0
for a in badges_ed:
    da = parse_rect(a)
    for b in badges_co:
        db = parse_rect(b)
        if badge_key(a) == badge_key(b) and da.get("y") != db.get("y") and all(da.get(k) == db.get(k) for k in ("x","width","height","fill","rx")):
            y_only += 1
            break
out["p6_badges"] = {"ed": len(badges_ed), "co": len(badges_co), "same_y_pairs": same_y, "y_only_shifted": y_only}
inm_ed = [e for e in texts(ED+"p6-afondo.svg") if "Inmigración" in e["text"]]
inm_co = [e for e in texts(CO+"p6-afondo.svg") if "Inmigración" in e["text"]]
out["inmigracion"] = {"ed": [(e["x"], e["y"], e["attrs"]) for e in inm_ed], "co": [(e["x"], e["y"], e["attrs"]) for e in inm_co], "identical": [(e["x"], e["y"], e["attrs"], e["text"]) for e in inm_ed] == [(e["x"], e["y"], e["attrs"], e["text"]) for e in inm_co]}
def p8_answers(path):
    els = texts(path)
    ans = {}
    cur = None
    for e in els:
        t = e["text"].strip()
        m = re.match(r'^(\d+)\.\s+(.*)$', t)
        if m:
            cur = int(m.group(1)); ans[cur] = m.group(2)
        elif cur is not None and t and not t.startswith("— СТРАНИЦА") and "RESPUESTAS" not in t and not t.startswith("СТРАНИЦА"):
            if 'font-size="24"' not in e["attrs"] and 'font-size="27"' not in e["attrs"] and 'font-size="23"' not in e["attrs"]:
                ans[cur] += " " + t
    return ans
ed_ans, co_ans = p8_answers(ED+"p8-ejercicios.svg"), p8_answers(CO+"p8-ejercicios.svg")
out["p8_counts"] = {"ed": len(ed_ans), "co": len(co_ans), "numbers_continuous_ed": sorted(ed_ans) == list(range(1, 151))}
def dashkey(v):
    return v.split(" — ")[0].strip()
dashdiff = [n for n in range(1, 151) if n in ed_ans and n in co_ans and dashkey(ed_ans[n]) != dashkey(co_ans[n])]
out["p8_dashdiff"] = dashdiff
out["p8_keys_ed"] = {n: ed_ans.get(n) for n in (137, 138, 139, 140, 150)}
out["p8_keys_co"] = {n: co_ans.get(n) for n in (137, 138, 139, 140, 150)}
seps = []
counts = []
cur_count = 0
for e in texts(ED+"p8-ejercicios.svg"):
    t = e["text"].strip()
    if t.startswith("— СТРАНИЦА"):
        seps.append(t); counts.append(cur_count); cur_count = 0
    elif re.match(r'^\d+\.\s+', t):
        cur_count += 1
counts.append(cur_count)
out["p8_separators"] = seps
out["p8_pagination_counts_raw"] = counts
lvl_ed = Counter(e["text"].strip() for e in texts(ED+"p8-ejercicios.svg") if e["text"].strip() in ("A2","B1","B2"))
lvl_co = Counter(e["text"].strip() for e in texts(CO+"p8-ejercicios.svg") if e["text"].strip() in ("A2","B1","B2"))
out["p8_level_text_counts"] = {"ed": dict(lvl_ed), "co": dict(lvl_co)}
with open(os.environ['HOME'] + "/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-ru-reproof/analyze.json", "w", encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print("TOKEN DIFF")
for p, d in tokdiff.items():
    print(p, "added:", d["added"], "removed:", d["removed"])
print("P7 cartas ed:", out["p7_ed_cartas"])
print("P7 cartas co:", out["p7_co_cartas"])
print("disclosure:", out["disclosure_joined"], "| invitation:", out["disclosure_has_invitation"], "| facts:", out["disclosure_facts"], "| old label:", out["old_label_present"])
print("ana identical:", out["ana_letter_identical_text"], "| es note identical:", out["es_note_identical_text"])
print("quote counts:", out["quote_counts"])
print("quote labels:", out["quote_page_labels"])
print("fixup4:", out["fixup4_elements"], "| old phrase:", out["old_fixup4_phrase_present"])
print("gloss poyasnenie:", gloss)
print("images:", out["image_hashes"])
print("cjk:", out["cjk_per_page"])
print("orphan:", orphan, "| bridge:", out["bridge_term_count"])
print("furniture:", json.dumps(out["furniture"], ensure_ascii=False))
print("badge ed:", out["p1_badge_elements"], "w43:", out["w43_p1_badge_elements"])
print("pagina4:", out["p1_pagina4"], out["p1_paginas_split"], "body stranitsa4:", out["p1_body_stranitsa4"])
print("p6 rect equal:", out["p6_rect_multiset_equal"], "bars:", out["p6_bars"], "badges:", out["p6_badges"])
print("inmigracion:", out["inmigracion"])
print("p8 counts:", out["p8_counts"], "dashdiff:", dashdiff)
print("p8 keys ed:", out["p8_keys_ed"])
print("p8 keys co:", out["p8_keys_co"])
print("p8 seps:", seps, "pagination raw:", counts)
print("p8 levels:", out["p8_level_text_counts"])
print("p7 total texts:", out["p7_ed_total_texts"], "frases:", out["p7_frases_head"], "preview:", out["p7_preview"])
