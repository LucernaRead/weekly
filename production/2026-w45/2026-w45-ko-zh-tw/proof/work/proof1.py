# -*- coding: utf-8 -*-
"""Independent proof script 1 for W45 KO x ZH-TW. Read-only on delivery/core/W43.
Writes JSON + summary txt to this script's directory (work/)."""
import re, os, json, html, hashlib, base64, io
from collections import Counter

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-zh-tw/svg")
W43 = os.path.join(GOAL, "files/weekly-report-ko-zh-tw/svg")
PAGES = ["p1-pyoji", "p2-saenghwal", "p3-munhwa", "p4-seupocheu",
         "p5-cheongnyeon", "p6-gipi", "p7-mal", "p8-siheom"]
HANGUL = re.compile(r"[\uac00-\ud7a3]+")
HAN = re.compile(r"[\u4e00-\u9fff]")
CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")

def parse(path):
    s = open(path, encoding="utf-8").read()
    texts, rects, lines, images = [], [], [], []
    for m in re.finditer(r"<text\s([^>]*)>(.*?)</text>", s, re.S):
        attrs, body = m.group(1), re.sub(r"<[^>]+>", "", m.group(2))
        body = html.unescape(body)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else ""
        texts.append(dict(x=float(g("x") or 0), y=float(g("y") or 0),
                          size=float(g("font-size") or 0), fam=g("font-family"),
                          bold="700" in attrs, anchor=g("text-anchor") or "start",
                          fill=g("fill"), t=body))
    for m in re.finditer(r"<rect\s([^>]*)/>", s):
        attrs = m.group(1)
        def g(k):
            mm = re.search(k + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else ""
        try:
            rects.append(dict(x=float(g("x") or 0), y=float(g("y") or 0),
                              w=float(g("width") or 0), h=float(g("height") or 0),
                              fill=g("fill"), stroke=g("stroke")))
        except ValueError:
            pass
    for m in re.finditer(r"<image\s([^>]*)/>", s):
        attrs = m.group(1)
        mm = re.search(r'href="data:image/[^;]+;base64,([^"]+)"', attrs)
        images.append(mm.group(1) if mm else "")
    return texts, rects, lines, images

def norm(s):
    return re.sub(r"\s+", "", s)

R = {}
# ---------- freeze / CJK / hangul / skeleton ----------
PAGE_LINES = ({"제 %d 면 / 총 8 면" % n for n in range(1, 9)}
              | {"第 %d 版 / 共 8 版" % n for n in range(1, 9)})
SEPS = ({"— 제%d면 —" % n for n in range(1, 9)}
        | {"— 第 %d 版 —" % n for n in range(1, 9)})
FURN = PAGE_LINES | SEPS | {
    "Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY",
    "Lucerna · 韓語週報 VOL.2 · 正文韓語 · 講解繁體中文",
    "韓語正文 · 繁體中文講解 — 給繁體中文讀者的版本",
    "답 · 参考答案 — 按版面分页排列，找到题号即可",
    "답 · 全部答案與簡析（第 1–8 版）",
    "每题附一句中文简析 · 带 ✓ 的为范文题",
    "每題附一句中文簡析 · 帶 ✓ 的為範本題",
}
DISC_CORE = norm("郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。")
DISC_ED = norm("鄭重說明：截至截稿時，未收到真實讀者來信與第 8 版優秀作文，因此仍刊範例，上期承諾順延至 VOL.3。請把你的來信和第 8 版作文寄給我們！")
freeze = {}
for pg in PAGES:
    ct, _, _, _ = parse(os.path.join(CORE, pg + ".svg"))
    et, _, _, _ = parse(os.path.join(ED, pg + ".svg"))
    cc, ec = Counter(t["t"] for t in ct), Counter(t["t"] for t in et)
    removed = list((cc - ec).elements()); added = list((ec - cc).elements())
    # CJK multiset (own recompute)
    core_cjk = Counter(ch for t in ct for ch in t["t"] if CJK.search(ch))
    ed_cjk = Counter(ch for t in et for ch in t["t"] if CJK.search(ch))
    added_cjk = sum((ed_cjk - core_cjk).values())
    removed_cjk = sum((core_cjk - ed_cjk).values())
    # Hangul runs multiset
    core_hr = Counter(r for t in ct for r in HANGUL.findall(t["t"]))
    ed_hr = Counter(r for t in et for r in HANGUL.findall(t["t"]))
    only_core_hr = dict((core_hr - ed_hr)); only_ed_hr = dict((ed_hr - core_hr))
    # skeleton: exclude furniture + disclosure-substring lines, Han-strip, join in draw order
    def is_furn(s):
        ns = norm(s)
        return s in FURN or ns in DISC_CORE or ns in DISC_ED
    rem_nf = [s for s in removed if not is_furn(s)]
    add_nf = [s for s in added if not is_furn(s)]
    sk_eq = HAN.sub("", norm("".join(rem_nf))) == HAN.sub("", norm("".join(add_nf)))
    freeze[pg] = dict(core_cjk_total=sum(core_cjk.values()), ed_cjk_total=sum(ed_cjk.values()),
                      net=sum(ed_cjk.values()) - sum(core_cjk.values()),
                      added_cjk=added_cjk, removed_cjk=removed_cjk,
                      strings_removed=len(removed), strings_added=len(added),
                      hangul_only_core=only_core_hr, hangul_only_ed=only_ed_hr,
                      skeleton_equal=sk_eq,
                      skeleton_core_len=len(HAN.sub("", norm("".join(rem_nf)))),
                      skeleton_ed_len=len(HAN.sub("", norm("".join(add_nf)))))
R["freeze"] = freeze
R["freeze_added_total"] = sum(v["added_cjk"] for v in freeze.values())

# ---------- P8 printed lines (own extraction) ----------
def p8_lines(d):
    texts, _, _, _ = parse(os.path.join(d, "p8-siheom.svg"))
    out = {}
    for t in texts:
        if 1328 <= t["y"] < 2580:
            m = re.match(r"^(\d+)\.\s(.*)$", t["t"])
            if m:
                out[int(m.group(1))] = m.group(2)
    return out
ck, ek = p8_lines(CORE), p8_lines(ED)
def keypart(line):
    if line is None: return None
    if line.startswith("✓ "): return "APPARATUS"
    return line.split(" — ", 1)[0]
def notepart(line):
    if line is None: return None
    return line.split(" — ", 1)[1] if " — " in line else ""
p8 = dict(core_noted=len(ck), ed_noted=len(ek), numbers_ok=sorted(ek) == list(range(1, 151)),
          keydiff=[n for n in range(1, 151) if keypart(ck.get(n)) != keypart(ek.get(n))],
          full_line_diff=[n for n in range(1, 151) if ck.get(n) != ek.get(n)],
          adjudicate={n: dict(core=ck.get(n), ed=ek.get(n), core_key=keypart(ck.get(n)), ed_key=keypart(ek.get(n)))
                      for n in (109, 137, 138, 139, 140, 150)})
# P8 notes purity: notes containing Hangul (frozen headword citations?) + non-Han scripts
note_hangul = {}
for n in range(1, 151):
    nt = notepart(ek.get(n))
    if nt and HANGUL.search(nt):
        note_hangul[n] = nt
p8["notes_with_hangul"] = note_hangul
# cross-script: any Cyrillic / kana / hiragana in edition P8 notes?
p8["notes_cross_script"] = {n: notepart(ek.get(n)) for n in range(1, 151)
                            if re.search(r"[\u0400-\u04ff\u3040-\u30ff]", notepart(ek.get(n)) or "")}
R["p8"] = p8

# ---------- gloss boxes (rect method) + word heads ----------
def gloss_boxes(d):
    per = {}
    for pg in PAGES:
        texts, rects, _, _ = parse(os.path.join(d, pg + ".svg"))
        boxes = []
        for r in rects:
            if r["fill"] != "#f1ead6": continue
            inside = [t for t in texts if r["x"] <= t["x"] < r["x"] + r["w"] and r["y"] <= t["y"] < r["y"] + r["h"]]
            pref = [t for t in inside if t["t"].startswith("譯注｜") or t["t"].startswith("译注｜")]
            if pref:
                segs = sum(t["t"].count("·") for t in inside) + 1
                heads = "".join(HANGUL.findall("".join(t["t"] for t in inside)))
                boxes.append(dict(segs=segs, lines=[t["t"] for t in inside], heads=heads))
        per[pg] = boxes
    return per
gb_c, gb_e = gloss_boxes(CORE), gloss_boxes(ED)
gloss = {}
for pg in PAGES:
    bc, be = gb_c[pg], gb_e[pg]
    gloss[pg] = dict(core_boxes=len(bc), ed_boxes=len(be),
                     core_segs=sum(b["segs"] for b in bc), ed_segs=sum(b["segs"] for b in be),
                     heads_equal=[b["heads"] for b in bc] == [b["heads"] for b in be],
                     core_firstline_segs=sum(b["lines"][0].count("·") + 1 if b["lines"] else 0 for b in bc),
                     ed_firstline_segs=sum(b["lines"][0].count("·") + 1 if b["lines"] else 0 for b in be),
                     ed_boxes_detail=be)
gloss["total_core_segs"] = sum(v["core_segs"] for v in gloss.values() if isinstance(v, dict))
gloss["total_ed_segs"] = sum(v["ed_segs"] for v in gloss.values() if isinstance(v, dict))
R["gloss_boxes"] = gloss

# call-string gloss (source text parse, read-only)
def gloss_calls(builddir):
    per = {}
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(builddir, f), encoding="utf-8").read()
        tot = 0; calls = []
        for m in re.finditer(r"\.(gloss|glossline)\(\s*\"((?:[^\"\\]|\\.)*)\"", src):
            segs = [s.strip().rstrip("。") for s in m.group(2).split("·")]
            segs = [s for s in segs if s]
            calls.append((m.group(1), len(segs), m.group(2)[:40]))
            tot += len(segs)
        per[f] = dict(total=tot, calls=calls)
    return per
gc = gloss_calls(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-build"))
ge = gloss_calls(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-zh-tw-build"))
R["gloss_callstring"] = dict(core={k: v["total"] for k, v in gc.items()},
                             edition={k: v["total"] for k, v in ge.items()},
                             core_total=sum(v["total"] for v in gc.values()),
                             edition_total=sum(v["total"] for v in ge.values()),
                             core_calls_detail=gc, edition_calls_detail=ge)

# ---------- golden sentences ----------
def page_norm_text(d, pg):
    texts, _, _, _ = parse(os.path.join(d, pg + ".svg"))
    return norm("".join(t["t"] for t in texts))
def page_raw_text(d, pg):
    texts, _, _, _ = parse(os.path.join(d, pg + ".svg"))
    return "".join(t["t"] for t in texts)
et7, _, _, _ = parse(os.path.join(ED, "p7-mal.svg"))
p7texts = [t["t"] for t in et7]
hdr = next(i for i, t in enumerate(p7texts) if t.startswith("이번 주의 문장"))
quotes = []
for i in range(hdr + 1, len(p7texts)):
    m = re.match(r"^「(.+)」$", p7texts[i])
    if m and HANGUL.search(m.group(1)):
        tag = None
        for u in p7texts[i + 1:i + 3]:
            mm = re.search(r"\((\d)면\)", u)
            if mm: tag = int(mm.group(1)); break
        quotes.append((m.group(1), tag))
gold = []
for q, tag in quotes:
    nq = norm(q)
    fc = sum(page_norm_text(CORE, pg).count(nq) for pg in PAGES)
    fe = sum(page_norm_text(ED, pg).count(nq) for pg in PAGES)
    # space-sensitive: raw joined text count
    fc_s = sum(page_raw_text(CORE, pg).count(q) for pg in PAGES)
    fe_s = sum(page_raw_text(ED, pg).count(q) for pg in PAGES)
    tagged = page_norm_text(ED, PAGES[tag - 1]).count(nq) if tag else 0
    gold.append(dict(quote=q, tag=tag, core_insensitive=fc, ed_insensitive=fe,
                     core_sensitive=fc_s, ed_sensitive=fe_s, tagged_page_count=tagged))
R["golden"] = gold

# ---------- P7 readers corner + phrases + teaser ----------
p7all = norm("".join(p7texts))
R["readers"] = dict(
    editor_example="編輯部範例信，非真實來信。" in p7all,
    no_real_letters="未收到真實讀者來信" in p7all,
    no_best_p8="未收到真實讀者來信與第8版優秀作文" in p7all,
    deferred_vol3="順延至VOL.3" in p7all,
    solicitation="請把你的來信和第8版作文寄給我們！" in p7all,
    solicitation_without_bang="請把你的來信和第8版作文寄給我們" in p7all)
# full P7 text dump (ordered) for manual phrase/teaser identification
R["p7_texts_ordered"] = p7texts

# ---------- furniture three-way ----------
def p1_dump(d):
    texts, rects, lines, _ = parse(os.path.join(d, "p1-pyoji.svg"))
    return texts, rects, lines
def find(texts, pred):
    return [t for t in texts if pred(t["t"])]
furn = {}
for name, d in (("core", CORE), ("w43", W43), ("edition", ED)):
    texts, rects, lines = p1_dump(d)
    badge = find(texts, lambda s: "講解" in s and "版本" in s)
    sub = find(texts, lambda s: s.startswith("한국어를 배우는"))
    foot = find(texts, lambda s: s.startswith("Lucerna ·"))
    furn[name] = dict(badge=[(t["t"], t["size"], t["fill"], t["bold"], t["x"], t["y"]) for t in badge],
                      subtitle_y=[t["y"] for t in sub],
                      footer=[t["t"] for t in foot])
    # rules/band: use svg raw for line y and rect y
    s = open(os.path.join(d, "p1-pyoji.svg"), encoding="utf-8").read()
    furn[name]["rule_lines"] = sorted(set(float(y) for y in re.findall(r"<line[^>]*y1=\"([0-9.]+)\"", s)))[:4]
    furn[name]["band_rects"] = sorted(set((float(x), float(y)) for x, y in re.findall(r"<rect[^>]*x=\"([0-9.]+)\"[^>]*y=\"([0-9.]+)\"", s) if float(y) in (424.0, 433.0)))
R["furniture_p1"] = furn
# per-page footers/pagelines/fonts/band titles edition vs w43 vs core
fp = {}
for pg in PAGES:
    row = {}
    for name, d in (("core", CORE), ("w43", W43), ("edition", ED)):
        texts, _, _, _ = parse(os.path.join(d, pg + ".svg"))
        ts = [t["t"] for t in texts]
        row[name] = dict(footer=[t for t in ts if t.startswith("Lucerna ·")],
                         pageline=[t for t in ts if re.match(r"^(第 \d 版|제 \d 면)", t)],
                         fonts=sorted(set(t["fam"] for t in texts)),
                         gloss_prefix=any(t.startswith("譯注｜") or t.startswith("译注｜") for t in ts))
    fp[pg] = row
R["furniture_pages"] = fp
# P8 head/seps + band titles
for name, d in (("core", CORE), ("w43", W43), ("edition", ED)):
    texts, _, _, _ = parse(os.path.join(d, "p8-siheom.svg"))
    ts = [t["t"] for t in texts]
    R.setdefault("p8_furniture", {})[name] = dict(
        head_left=[t for t in ts if t.startswith("답 ·")],
        head_right=[t for t in ts if "中文" in t and ("簡析" in t or "简析" in t)],
        seps=[t for t in ts if re.match(r"^— (第 \d 版|제\d면) —$", t)])
# band titles: texts at y~? use P1 band? Instead: dark-band title texts per page from content: find texts with size 36? record per page edition
bt = {}
for pg in PAGES:
    texts, _, _, _ = parse(os.path.join(ED, pg + ".svg"))
    bt[pg] = [t["t"] for t in texts if t["size"] == 36]
R["edition_size36_texts"] = bt

# ---------- images ----------
imgs = {}
for pg in PAGES:
    _, _, _, im_c = parse(os.path.join(CORE, pg + ".svg"))
    _, _, _, im_e = parse(os.path.join(ED, pg + ".svg"))
    def hashes(lst):
        out = []
        for b in lst:
            raw = base64.b64decode(b)
            out.append(dict(b64_sha=hashlib.sha256(b.encode()).hexdigest(),
                            jpeg_sha=hashlib.sha256(raw).hexdigest()))
        return out
    tc, _, _, _ = parse(os.path.join(CORE, pg + ".svg"))
    te, _, _, _ = parse(os.path.join(ED, pg + ".svg"))
    imgs[pg] = dict(core_n=len(im_c), ed_n=len(im_e), equal=hashes(im_c) == hashes(im_e),
                    hashes_ed=hashes(im_e),
                    credits_core=[t["t"] for t in tc if t["t"].startswith("사진:") or t["t"].startswith("그림:")],
                    credits_ed=[t["t"] for t in te if t["t"].startswith("사진:") or t["t"].startswith("그림:")],
                    # caption continuation lines: texts on same page containing '사진' fragments near credits
                    ed_caption_texts=[t["t"] for t in te if "사진" in t["t"] or "자료" in t["t"]])
R["images"] = imgs

# ---------- quotes balance / fonts / Han sets ----------
qb = {}
for pg in PAGES:
    te, _, _, _ = parse(os.path.join(ED, pg + ".svg"))
    all_t = "".join(t["t"] for t in te)
    qb[pg] = dict(open=all_t.count("「"), close=all_t.count("」"), ascii_dquote=all_t.count('"'))
R["quotes_balance"] = qb
def han_set(d):
    s = set()
    for pg in PAGES:
        texts, _, _, _ = parse(os.path.join(d, pg + ".svg"))
        for t in texts:
            s |= set(ch for ch in t["t"] if "\u4e00" <= ch <= "\u9fff")
    return s
R["han_sets"] = dict(edition=sorted(han_set(ED)), w43=sorted(han_set(W43)),
                     core=sorted(han_set(CORE)))
R["han_counts"] = dict(edition=len(han_set(ED)), w43=len(han_set(W43)), core=len(han_set(CORE)))
R["edition_only_vs_w43"] = sorted(han_set(ED) - han_set(W43))

# ---------- model paragraph (P8 H) ----------
def model_text(d):
    texts, _, _, _ = parse(os.path.join(d, "p8-siheom.svg"))
    # model paragraph: texts after the 150 apparatus line, in draw order; find start marker
    ts = [t["t"] for t in texts]
    idx = next((i for i, t in enumerate(ts) if t.startswith("✓")), None)
    return ts, idx
for name, d in (("core", CORE), ("edition", ED)):
    ts, idx = model_text(d)
    R.setdefault("model", {})[name] = dict(apparatus_idx=idx, tail=ts[idx:idx + 12] if idx is not None else [])
# model chars excluding spaces: join tail texts after apparatus, strip? use full joined minus spaces for the model sentence block
# locate the model sentence start '나의 겨울'
def model_block(d):
    texts, _, _, _ = parse(os.path.join(d, "p8-siheom.svg"))
    ts = [t["t"] for t in texts]
    start = next((i for i, t in enumerate(ts) if "나의 겨울 준비는" in t), None)
    if start is None: return None
    # collect until footer? model paragraph is contiguous texts; take texts from start while they look like model continuation
    block = []
    for t in ts[start:]:
        if t.startswith("Lucerna ·") or re.match(r"^第 \d 版", t): break
        block.append(t)
    return block
for name, d in (("core", CORE), ("edition", ED)):
    b = model_block(d)
    R.setdefault("model_block", {})[name] = dict(block=b,
        chars_no_space=len(re.sub(r"\s+", "", "".join(b))) if b else None,
        joined="".join(b) if b else None)

# ---------- digit sequences multiset (new-claim screen) ----------
def digits(d):
    c = Counter()
    for pg in PAGES:
        texts, _, _, _ = parse(os.path.join(d, pg + ".svg"))
        for t in texts:
            for m in re.finditer(r"\d+", t["t"]):
                c[m.group(0)] += 1
    return c
dc, de = digits(CORE), digits(ED)
R["digit_multiset_diff"] = dict(only_core=dict(dc - de), only_ed=dict(de - dc))

outdir = os.path.dirname(os.path.abspath(__file__))
json.dump(R, open(os.path.join(outdir, "proof1.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# concise summary
lines = []
lines.append("FREEZE added CJK total=%d per-page=%s" % (R["freeze_added_total"],
    {k: v["added_cjk"] for k, v in freeze.items()}))
lines.append("FREEZE CJK totals core->ed: " + str({k: (v["core_cjk_total"], v["ed_cjk_total"]) for k, v in freeze.items()}))
lines.append("SKELETON equal: " + str({k: v["skeleton_equal"] for k, v in freeze.items()}))
lines.append("HANGUL only_core: " + str({k: v["hangul_only_core"] for k, v in freeze.items()}))
lines.append("HANGUL only_ed: " + str({k: v["hangul_only_ed"] for k, v in freeze.items()}))
lines.append("P8: " + json.dumps({k: p8[k] for k in ("core_noted", "ed_noted", "numbers_ok", "keydiff", "full_line_diff")}, ensure_ascii=False))
for n, v in p8["adjudicate"].items():
    lines.append("P8 #%d core=%r ed=%r" % (n, v["core"], v["ed"]))
lines.append("P8 notes_with_hangul: " + json.dumps(note_hangul, ensure_ascii=False))
lines.append("GLOSS boxes core/ed segs: " + str({k: (v["core_segs"], v["ed_segs"]) for k, v in gloss.items() if isinstance(v, dict)}))
lines.append("GLOSS heads_equal: " + str({k: v["heads_equal"] for k, v in gloss.items() if isinstance(v, dict)}))
lines.append("GLOSS firstline segs core/ed: " + str({k: (v["core_firstline_segs"], v["ed_firstline_segs"]) for k, v in gloss.items() if isinstance(v, dict)}))
lines.append("GLOSS callstring core=%s ed=%s totals %d/%d" % (R["gloss_callstring"]["core"], R["gloss_callstring"]["edition"], R["gloss_callstring"]["core_total"], R["gloss_callstring"]["edition_total"]))
for g in gold:
    lines.append("GOLDEN tag=%s core_ins=%d ed_ins=%d core_sens=%d ed_sens=%d tagged=%d :: %s" % (g["tag"], g["core_insensitive"], g["ed_insensitive"], g["core_sensitive"], g["ed_sensitive"], g["tagged_page_count"], g["quote"]))
lines.append("READERS: " + json.dumps(R["readers"], ensure_ascii=False))
lines.append("IMAGES: " + str({k: (v["core_n"], v["ed_n"], v["equal"]) for k, v in imgs.items()}))
lines.append("QUOTES: " + json.dumps(qb, ensure_ascii=False))
lines.append("HAN counts ed/w43/core: %s edition_only_vs_w43 n=%d" % (R["han_counts"], len(R["edition_only_vs_w43"])))
lines.append("MODEL core chars=%s ed chars=%s equal_block=%s" % (R["model_block"]["core"]["chars_no_space"], R["model_block"]["edition"]["chars_no_space"], R["model_block"]["core"]["joined"] == R["model_block"]["edition"]["joined"]))
lines.append("DIGIT only_core=%s only_ed=%s" % (R["digit_multiset_diff"]["only_core"], R["digit_multiset_diff"]["only_ed"]))
open(os.path.join(outdir, "proof1-summary.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines))
