# -*- coding: utf-8 -*-
"""Independent SVG analysis for W45 KO x NL proofread (own code, read-only inputs).
Uses tools/occlusion_audit.py only as a font/ink parser library.
Outputs: work/analysis.json + printed summary."""
import os, re, sys, json, hashlib, base64
from collections import Counter
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
DIRS = {
    "ed": os.path.join(GOAL, "files/weekly-report-w45-ko-nl"),
    "core": os.path.join(GOAL, "files/weekly-report-w45-ko-core"),
    "w43": os.path.join(GOAL, "files/weekly-report-ko-nl"),
}
PAGES = ["p1-pyoji.svg", "p2-saenghwal.svg", "p3-munhwa.svg", "p4-seupocheu.svg",
         "p5-cheongnyeon.svg", "p6-gipi.svg", "p7-mal.svg", "p8-siheom.svg"]

def els(d, pg):
    return OA.parse_svg(open(os.path.join(d, "svg", pg), encoding="utf-8").read())[0]

def texts(d, pg):
    return [e for e in els(d, pg) if e.kind == "text" and e.text.strip()]

def is_han(ch): return "\u4e00" <= ch <= "\u9fff"
def is_hangul(ch): return "\uac00" <= ch <= "\ud7af"
def is_cjk(ch): return is_han(ch) or is_hangul(ch) or "\u3040" <= ch <= "\u30ff" or "\u3400" <= ch <= "\u4dbf"

out = {}
# ---- A. per-page CJK / Han / Hangul + multiset diff (edition vs core) ----
A = {}
for pg in PAGES:
    ce = Counter(ch for e in texts(DIRS["ed"], pg) for ch in e.text if is_cjk(ch))
    cc = Counter(ch for e in texts(DIRS["core"], pg) for ch in e.text if is_cjk(ch))
    added = dict((ce - cc))
    removed = dict((cc - ce))
    han_e = sum(1 for e in texts(DIRS["ed"], pg) for ch in e.text if is_han(ch))
    han_c = sum(1 for e in texts(DIRS["core"], pg) for ch in e.text if is_han(ch))
    A[pg] = {"cjk_ed": sum(ce.values()), "cjk_core": sum(cc.values()),
             "han_ed": han_e, "han_core": han_c, "added": added, "removed": removed}
out["A_cjk"] = A
print("== A. CJK/Han per page (ed vs core) ==")
for pg in PAGES:
    a = A[pg]
    print(f"  {pg}: CJK {a['cjk_core']}->{a['cjk_ed']} Han {a['han_core']}->{a['han_ed']} added={a['added']} removed_n={sum(a['removed'].values())} removed={dict(list(a['removed'].items())[:12])}")

# ---- B. P8 printed lines reconstructed from rendered lines ----
def p8_lines(d):
    es = [e for e in texts(d, "p8-siheom.svg") if e.baseline and e.baseline > 1328]
    # group by column x, sort by baseline; items start with "N. " or "— Pagina"
    byx = {}
    for e in es:
        byx.setdefault(round(OA.fnum(e.attrs, "x"), 1), []).append(e)
    items, seps = {}, []
    for x, g in byx.items():
        g.sort(key=lambda e: e.baseline)
        cur = None
        for e in g:
            t = e.text
            if re.match(r"^\d+\.\s", t):
                cur = t; items[int(t.split(".")[0])] = [t]
            elif t.strip().startswith("— Pagina") or t.strip().startswith("— 제"):
                seps.append(t.strip())
            elif cur is not None:
                items[int(cur.split(".")[0])].append(t)
    joined = {n: "".join(v) for n, v in items.items()}
    return joined, seps
ed8, edseps = p8_lines(DIRS["ed"]); co8, coseps = p8_lines(DIRS["core"])
out["B_p8_n"] = {"ed": len(ed8), "core": len(co8), "ed_nums_ok": sorted(ed8) == list(range(1, 151)),
                 "core_nums_ok": sorted(co8) == list(range(1, 151))}
out["B_p8_seps_ed"] = sorted(set(edseps)); out["B_p8_seps_core"] = sorted(set(coseps))
print(f"== B. P8 reconstructed items: ed={len(ed8)} core={len(co8)} ed_nums_1..150={sorted(ed8)==list(range(1,151))}")
print(f"   seps ed={sorted(set(edseps))} core={sorted(set(coseps))}")
for n in [104, 109, 115, 136, 137, 138, 139, 140, 150]:
    print(f"   #{n} ED : {ed8.get(n)}")
    print(f"   #{n} CORE: {co8.get(n)}")
out["B_p8_spot"] = {str(n): {"ed": ed8.get(n), "core": co8.get(n)} for n in [104, 109, 115, 136, 137, 138, 139, 140, 150]}
# P8 note purity: note = after ' — ' (dash); for 150 the whole line is apparatus
note_han, note_issues = 0, []
for n, line in ed8.items():
    if n == 150:
        continue
    m = line.split(" — ", 1)
    note = m[1] if len(m) == 2 else ""
    h = sum(1 for ch in note if is_han(ch))
    note_han += h
    if h: note_issues.append((n, note))
out["B_note_han_total"] = note_han; out["B_note_han_items"] = note_issues
print(f"   P8 note-segment Han total (excl #150 apparatus): {note_han} issues={note_issues}")
# notes containing Hangul (frozen citations inside Dutch notes) - list them
hangul_notes = {n: line.split(" — ", 1)[1] for n, line in ed8.items() if n != 150 and len(line.split(" — ", 1)) == 2 and any(is_hangul(ch) for ch in line.split(" — ", 1)[1])}
print(f"   P8 notes containing Hangul citations: {hangul_notes}")
out["B_notes_with_hangul"] = hangul_notes

# ---- C. furniture P1 three-way ----
def furn(d, pg="p1-pyoji.svg"):
    es = els(d, pg)
    res = {}
    for e in es:
        if e.kind == "text":
            t = e.text
            if t == "Lucerna": res["masthead"] = (t, OA.fnum(e.attrs, "x"), e.baseline, OA.fnum(e.attrs, "font-size"))
            if "TEKSTEN IN HET KOREAANS" in t: res["badge"] = (t, e.baseline, OA.fnum(e.attrs, "font-size"), e.attrs.get("fill"), e.attrs.get("font-weight"))
            if t.startswith("Lucerna ·") and "WEEKBLAD" in t or (t.startswith("Lucerna ·") and "VOL" in t): res["footer_p1"] = t
            if re.match(r"^Pagina \d+ van 8$", t): res["pageline"] = t
            if "주간 신문" in t: res["subtitle"] = (t, e.baseline, OA.fnum(e.attrs, "font-size"))
    # rules: hlines near top; dark band rect
    lines = sorted(set(round(OA.fnum(e.attrs, "y1"), 1) for e in es if e.kind == "line" and OA.fnum(e.attrs, "y1") < 500))
    res["top_lines"] = lines
    bands = [(OA.fnum(e.attrs, "y"), OA.fnum(e.attrs, "height"), e.attrs.get("fill")) for e in es if e.kind == "rect" and OA.fnum(e.attrs, "height") == 118 and OA.fnum(e.attrs, "y") < 600]
    res["band_rects_y<600"] = bands
    bandtexts = [(t, round(b, 1)) for t, b in [(e.text, e.baseline) for e in es if e.kind == "text"] if 470 < b < 550]
    res["band_texts"] = bandtexts
    # footer: last page footer? use p1 footer text search
    foots = [e.text for e in es if e.kind == "text" and e.baseline and e.baseline > 2600]
    res["p1_footer_texts"] = foots
    return res
for k in ["core", "w43", "ed"]:
    f = furn(DIRS[k]); out[f"C_furn_{k}"] = {kk: (list(vv) if isinstance(vv, tuple) else vv) for kk, vv in f.items()}
    print(f"== C. furniture {k}: masthead={f.get('masthead')} subtitle_y={f.get('subtitle', (None, None))[1] if f.get('subtitle') else None} badge={f.get('badge')} lines={f.get('top_lines')} bands={f.get('band_rects_y<600')} bandtexts={f.get('band_texts')} footer={f.get('p1_footer_texts')}")
# gloss prefix + section headers + exercise headers (ed vs w43): search all pages
def find_text(d, pred):
    hits = []
    for pg in PAGES:
        for e in texts(d, pg):
            if pred(e.text): hits.append((pg, e.text))
    return hits
for label, pred in [("gloss_prefix", lambda t: t.startswith("Uitleg — ")),
                    ("ex_header", lambda t: "Oefeningen blz." in t),
                    ("ex_right", lambda t: "Antwoorden op blz. 8" in t and "Niveaus" in t),
                    ("p1_quiz_right", lambda t: "Lees de voorpagina" in t),
                    ("p8_header", lambda t: t.startswith("답 · Antwoorden")),
                    ("p8_header_right", lambda t: "Bij elk antwoord" in t)]:
    he = find_text(DIRS["ed"], pred); hw = find_text(DIRS["w43"], pred)
    print(f"   {label}: ed_n={len(he)} w43_n={len(hw)} ed_sample={he[:2]} w43_sample={hw[:2]} equal_texts={sorted(set(t for _, t in he))==sorted(set(t for _, t in hw))}")
    out[f"C_{label}"] = {"ed": he, "w43": hw}

# ---- D. rendered gloss decomposition ----
def rendered_gloss(d):
    per = {}
    for pg in PAGES:
        es = [e for e in texts(d, pg) if ("Sans" in e.attrs.get("font-family", "")) and abs(OA.fnum(e.attrs, "font-size") - 20.5) < 0.1 and e.attrs.get("fill") == "#57523f"]
        es.sort(key=lambda e: (OA.fnum(e.attrs, "x"), e.baseline))
        units, cur = [], []
        for e in es:
            if cur and (OA.fnum(e.attrs, "x") != OA.fnum(cur[-1].attrs, "x") or e.baseline - cur[-1].baseline > 45):
                units.append(cur); cur = []
            cur.append(e)
        if cur: units.append(cur)
        udetail = []
        for u in units:
            joined = "".join(t.text for t in u)
            udetail.append({"x": OA.fnum(u[0].attrs, "x"), "lines": len(u), "items": len(joined.split("·")), "joined": joined})
        per[pg] = {"units": len(units), "items": sum(u["items"] for u in udetail), "detail": udetail}
    return per
rg_ed = rendered_gloss(DIRS["ed"]); rg_co = rendered_gloss(DIRS["core"])
out["D_gloss_ed"] = rg_ed; out["D_gloss_core"] = rg_co
print("== D. rendered gloss (units/items) ==")
for pg in PAGES:
    print(f"   {pg}: ed {rg_ed[pg]['units']}u/{rg_ed[pg]['items']}i core {rg_co[pg]['units']}u/{rg_co[pg]['items']}i")
print(f"   TOTAL ed={sum(v['items'] for v in rg_ed.values())} core={sum(v['items'] for v in rg_co.values())}")
print(f"   P8 ed detail: {rg_ed['p8-siheom.svg']['detail']}")
print(f"   P7 ed detail: {rg_ed['p7-mal.svg']['detail']}")

# ---- E. golden sentences + P7 phrases ----
GOLD = [("11월 7일은 입동이에요", "p1-pyoji.svg"), ("절정에 가까운 주말이라고만 말할 수 있어요", "p1-pyoji.svg"),
        ("김장은 겨울 내내 먹는 김치를 담그는 일이에요", "p1-pyoji.svg"), ("수능까지 17일 남았어요. 오늘이 D-17예요", "p2-saenghwal.svg"),
        ("낮은 길은 더 늦게 물들어요", "p3-munhwa.svg"), ("KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요", "p4-seupocheu.svg"),
        ("온 나라가 수험생을 응원해요", "p5-cheongnyeon.svg"), ("날짜를 먼저 보세요", "p6-gipi.svg")]
def page_stripped(d):
    return {pg: re.sub(r"\s+", "", "".join(e.text for e in texts(d, pg))) for pg in PAGES}
pe, pc = page_stripped(DIRS["ed"]), page_stripped(DIRS["core"])
print("== E. golden sentences ==")
for sent, tagpg in GOLD:
    k = re.sub(r"\s+", "", sent)
    ce, cc = sum(v.count(k) for v in pe.values()), sum(v.count(k) for v in pc.values())
    on_tag_ed = k in pe[tagpg]; on_tag_co = k in pc[tagpg]
    print(f"   {sent[:24]}... tag={tagpg} core={cc} ed={ce} on_tag_ed={on_tag_ed} on_tag_co={on_tag_co}")
    out.setdefault("E_gold", []).append({"sent": sent, "tag": tagpg, "core": cc, "ed": ce, "on_tag_ed": on_tag_ed})
QUOTES = [("11월 7일은 입동이에요", "1면", "p1-pyoji.svg"), ("절정에 가까운 주말이라고만 말할 수 있어요", "1면", "p1-pyoji.svg"),
          ("김장은 겨울 내내 먹는 김치를 담그는 일이에요", "1면", "p1-pyoji.svg"), ("수능까지 17일 남았어요. 오늘이 D-17예요", "2면", "p2-saenghwal.svg"),
          ("낮은 길은 더 늦게 물들어요", "3면", "p3-munhwa.svg"), ("KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요", "4면", "p4-seupocheu.svg"),
          ("온 나라가 수험생을 응원해요", "5면", "p5-cheongnyeon.svg"), ("날짜를 먼저 보세요", "6면", "p6-gipi.svg")]
print("== E2. P7 phrases: verbatim in tagged article + Dutch line tag ==")
p7texts_ed = [e.text for e in texts(DIRS["ed"], "p7-mal.svg")]
for q, tag, tagpg in QUOTES:
    k = re.sub(r"\s+", "", q)
    in_art = k in pe[tagpg]
    # Dutch rendering line on P7: find text containing the Dutch translation? just check tag appears adjacent: search P7 texts for "(N면)"
    taglines = [t for t in p7texts_ed if f"({tag})" in t]
    print(f"   {q[:24]}... in_tagged_article_ed={in_art} P7_lines_with_({tag})={taglines}")

# ---- F. essay ----
def essay_of(d):
    es = [e for e in texts(d, "p8-siheom.svg") if e.baseline and e.baseline < 1328]
    full = "".join(e.text for e in es)
    i = full.find("나의 겨울 준비는 김장부터 시작해요.")
    return full, i
fe, ie = essay_of(DIRS["ed"]); fc, ic = essay_of(DIRS["core"])
print(f"== F. essay: ed_found_at={ie} core_found_at={ic}")
# reconstruct essay: MODELO from content8 source (edition + core) for exact compare
import ast as _ast
def modelo(path):
    src = open(path, encoding="utf-8").read()
    tree = _ast.parse(src)
    for node in _ast.walk(tree):
        if isinstance(node, _ast.Assign) and getattr(node.targets[0], "id", "") == "MODELO":
            return _ast.literal_eval(node.value)
    return None
me = modelo(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-nl-build/content8.py"))
mc = modelo(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-nl-build/orig/content8.py"))
print(f"   MODELO equal={me == mc} len_nospace ed={len(me.replace(' ', '')) if me else None} core={len(mc.replace(' ', '')) if mc else None} opens={me[:24] if me else None}")
print(f"   MODELO ed == P8 printed essay region? ed_svg_contains_opening={'나의 겨울 준비는 김장부터 시작해요.' in fe} core_svg_contains={'나의 겨울 준비는 김장부터 시작해요.' in fc}")
out["F_modelo"] = {"equal": me == mc, "len_ed": len(me.replace(" ", "")) if me else None, "len_core": len(mc.replace(" ", "")) if mc else None, "text": me}

# ---- G. letters (P7 col3, x~1473) ----
def letters(d):
    es = [e for e in texts(d, "p7-mal.svg") if abs(OA.fnum(e.attrs, "x") - 1473) < 1 and 1200 < e.baseline < 1900]
    es.sort(key=lambda e: e.baseline)
    return [(round(e.baseline, 2), round(e.box[3], 2) if e.box else None, e.text) for e in es]
le, lc = letters(DIRS["ed"]), letters(DIRS["core"])
print("== G. letters col (x=1473) ==")
print(f"   ed lines={len(le)} core lines={len(lc)}")
for row in le: print(f"   ED {row}")
out["G_letters_ed"] = le; out["G_letters_core"] = lc
# Korean letter + disclosure frozen? compare Korean-script lines sets
kor_ed = [t for _, _, t in le if any(is_hangul(ch) for ch in t)]
kor_co = [t for _, _, t in lc if any(is_hangul(ch) for ch in t)]
print(f"   Korean-script letters lines equal (as multisets, order-insensitive)={Counter(kor_ed) == Counter(kor_co)}")
print(f"   Korean lines ed: {kor_ed}")
print(f"   Korean lines core: {kor_co}")
# Dutch short note + disclosure paragraph: find in P7 texts
for label, needle in [("short_note", "Voorbeeldbrief van de redactie"), ("disclosure", "Tot de deadline kwamen er geen echte brieven")]:
    hits_ed = [t for t in p7texts_ed if needle in t]
    print(f"   {label}: ed_hits={hits_ed}")

# ---- H. images + credits + ssam caption ----
def images(d):
    res = {}
    for pg in PAGES:
        s = open(os.path.join(d, "svg", pg), encoding="utf-8").read()
        arr = []
        for mm in re.finditer(r"data:image/[^;]+;base64,([A-Za-z0-9+/=]+)", s):
            b64 = mm.group(1); raw = base64.b64decode(b64)
            arr.append((hashlib.sha256(b64.encode()).hexdigest()[:12], hashlib.sha256(raw).hexdigest()[:12]))
        res[pg] = arr
    return res
ie_, ic_ = images(DIRS["ed"]), images(DIRS["core"])
print("== H. images ==")
for pg in PAGES:
    print(f"   {pg}: ed={ie_[pg]} core={ic_[pg]} equal={ie_[pg] == ic_[pg]}")
out["H_images"] = {"ed": ie_, "core": ic_}
for pg in PAGES:
    creds = [e.text for e in texts(DIRS["ed"], pg) if "사진:" in e.text or "그림:" in e.text]
    if creds: print(f"   credits {pg}: {creds}")
p2texts = [e.text for e in texts(DIRS["ed"], "p2-saenghwal.svg")]
print(f"   P2 kimjang/ssam texts: {[t for t in p2texts if 'kimjang' in t.lower() or 'ssam' in t.lower() or 'niet' in t.lower()]}")
out["H_p2_caption_candidates"] = [t for t in p2texts if "kimjang" in t.lower() or "ssam" in t.lower()]

# ---- I. line-start quote inventory ----
def quote_starts(d):
    res = []
    for pg in PAGES:
        for e in texts(d, pg):
            t = e.text.strip()
            if t.startswith("'"):
                res.append((pg, round(OA.fnum(e.attrs, "x"), 1), round(e.baseline, 2), t[:60]))
    return res
qe, qc = quote_starts(DIRS["ed"]), quote_starts(DIRS["core"])
print(f"== I. line-start single-quote inventory: ed={len(qe)} core={len(qc)}")
for r in qe: print(f"   ED {r}")
for r in qc: print(f"   CORE {r}")
print(f"   sets equal={set(qe) == set(qc)} ed-only={set(qe) - set(qc)} core-only={set(qc) - set(qe)}")
out["I_quotes"] = {"ed": qe, "core": qc}

# ---- J. Dutch number formats + spot facts from P8 lines ----
for needle in ["551.864", "415,5", "300.000", "1.312", "27.000"]:
    hits = [f"{n}: {line}" for n, line in ed8.items() if needle in line]
    print(f"== J. format {needle}: {hits}")
out["J_formats"] = {nd: [f"{n}: {line}" for n, line in ed8.items() if nd in line] for nd in ["551.864", "415,5", "300.000", "1.312", "27.000"]}
for n in [14, 22, 55, 90, 118, 131]:
    print(f"   spot #{n} ED: {ed8.get(n)}")
    print(f"   spot #{n} CORE key/note (registry-independent, printed): {co8.get(n)}")

json.dump(out, open(os.path.join(GOAL, "hidden_files/w45/ko-nl-proof/work/analysis.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("WROTE analysis.json")
