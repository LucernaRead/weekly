# -*- coding: utf-8 -*-
"""W45 zh-tw-pt builder self-checks (supplements tools/freeze.py, p8.py,
occlusion_audit.py): same-baseline ink collisions, chart-label element
check, gloss-box counts, Traditional-independence cross-check, image
payloads + credits, P7 phrases, residual-Latin adjudication, registry
key/note diff (registry dumps are produced separately by dump_reg.py
run inside each build copy)."""
import base64, hashlib, html, json, os, re, sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "tools"))
import occlusion_audit as OA

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
ED = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-pt/svg")
W43 = os.path.join(GOAL, "files/weekly-report-zh-tw-pt/svg")
NAMES = ["p1-front.svg", "p2-life.svg", "p3-culture.svg", "p4-sport.svg",
         "p5-youth.svg", "p6-deep.svg", "p7-lang.svg", "p8-test.svg"]


def texts(path):
    t = open(path, encoding="utf-8").read()
    return [html.unescape(s) for s in
            re.findall(r"<text[^>]*>([^<]*)</text>", t)]


def main():
    out = {}
    # --- 1. same-baseline ink collisions (all pages, esp. P1 top band) ---
    print("== same-baseline ink collisions ==")
    total = 0
    for n in NAMES:
        els, _, _ = OA.parse_svg(open(os.path.join(ED, n), encoding="utf-8").read())
        by_base = {}
        for el in els:
            if el.kind == "text" and el.baseline:
                by_base.setdefault(round(el.baseline, 1), []).append(el)
        for b, group in by_base.items():
            group.sort(key=lambda e: e.box[0])
            for a, c in zip(group, group[1:]):
                # same baseline, horizontal ink overlap (allow 0.5 slack)
                if a.box[2] > c.box[0] + 0.5 and a.text.strip() and c.text.strip():
                    print(f"  COLLISION {n} y={b}: {a.text[:40]!r} vs {c.text[:40]!r}")
                    total += 1
    print(f"  total: {total}")
    out["same_baseline_collisions"] = total

    # --- 2. chart-label element check: text ink vs later-drawn rects ---
    print("== chart-label element check (P4 + P6) ==")
    for n in ["p4-sport.svg", "p6-deep.svg"]:
        els, _, _ = OA.parse_svg(open(os.path.join(ED, n), encoding="utf-8").read())
        hits = 0
        for i, el in enumerate(els):
            if el.kind != "text" or not el.text.strip():
                continue
            if el.box is None:
                continue
            for rc in els[i + 1:]:
                if rc.kind == "rect" and OA.is_opaque(rc) and rc.box is not None:
                    rb = rc.box
                    if OA.overlap(el.box, rb)[0] > 0:
                        # ignore full-page paper rect + page frame rects
                        if rb[2] - rb[0] > 1800:
                            continue
                        print(f"  OVERLAP {n}: {el.text[:50]!r} vs rect {tuple(round(v,1) for v in rb)}")
                        hits += 1
        print(f"  {n}: {hits} text-vs-later-rect overlaps (excl. page frame)")
        out[f"chart_check_{n}"] = hits

    # --- 3. gloss-box counts (gloss() calls in build code) ---
    print("== gloss boxes ==")
    for label, d in [("core", os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")),
                     ("pt", os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-pt-build"))]:
        c = 0
        for f in ["content12.py", "content34.py", "content56.py", "content7.py"]:
            c += open(os.path.join(d, f), encoding="utf-8").read().count("f.gloss(") \
                + open(os.path.join(d, f), encoding="utf-8").read().count("e.gloss(")
        # content7 uses a./b./c. flows; count .gloss( generally, minus glossline
        tot = 0
        for f in ["content12.py", "content34.py", "content56.py", "content7.py"]:
            txt = open(os.path.join(d, f), encoding="utf-8").read()
            tot += len(re.findall(r"\.gloss\(", txt))
        print(f"  {label}: gloss() calls = {tot}")
        out[f"gloss_{label}"] = tot

    # --- 4. Traditional-independence cross-check ---
    print("== Traditional-independence cross-check ==")
    def cjk_set(d):
        s = set()
        for n in NAMES:
            for t in texts(os.path.join(d, n)):
                for ch in t:
                    if "\u2e80" <= ch <= "\u9fff" or "\uff00" <= ch <= "\uffef":
                        s.add(ch)
        return s
    union = cjk_set(CORE) | cjk_set(W43)
    ed_set = cjk_set(ED)
    outside = sorted(ed_set - union)
    print(f"  core CJK chars: {len(cjk_set(CORE))}, W43-pt CJK chars: {len(cjk_set(W43))}")
    print(f"  union: {len(union)}, edition: {len(ed_set)}, outside union: {len(outside)}")
    for ch in outside:
        print(f"    OUTSIDE: {ch} U+{ord(ch):04X}")
    out["trad_outside_union"] = [f"{ch} U+{ord(ch):04X}" for ch in outside]
    # Simplified-only spot scan: chars that OpenCC s2t would change are
    # exactly the union-exclusion test above; additionally list any char
    # in the edition that is NOT in the core set but IS in W43 set (fine).
    print(f"  edition chars not in core but in W43-pt: {len((ed_set - cjk_set(CORE)) & cjk_set(W43))}")

    # --- 5. image payloads + credits ---
    print("== images ==")
    img_re = re.compile(r'<image[^>]*href="data:image/[^;]+;base64,([^"]+)"')
    cred_re = re.compile(r"Photo: [^<]*")
    for n in NAMES:
        ct = open(os.path.join(CORE, n), encoding="utf-8").read()
        et = open(os.path.join(ED, n), encoding="utf-8").read()
        cp = [hashlib.sha256(base64.b64decode(m)).hexdigest()[:12]
              for m in img_re.findall(ct)]
        ep = [hashlib.sha256(base64.b64decode(m)).hexdigest()[:12]
              for m in img_re.findall(et)]
        cc, ec = cred_re.findall(ct), cred_re.findall(et)
        print(f"  {n}: payloads core={cp} edition={ep} identical={cp == ep}; "
              f"credits identical={cc == ec} {ec}")
        out[f"images_{n}"] = {"payload_identical": cp == ep,
                              "credits_identical": cc == ec, "credits": ec}

    # --- 6. P7 golden sentences ---
    print("== P7 golden sentences ==")
    all_ed = "\n".join("".join(texts(os.path.join(ED, n))) for n in NAMES)
    # Inner text (P7 prints the quote bracketed; the article prints it
    # bare, so the verbatim count is measured on the inner text).
    quotes = [
        ("用手機轉帳、掃碼付款、網上買保險，都是金融科技", "p. 1"),
        ("123個國家及城市、1,600個攤位", "p. 1"),
        ("需要才買，不要為了折扣買一堆用不到的東西", "p. 2"),
        ("在高雄，鋼鐵也能變成舞台", "p. 3"),
        ("福隆的夏天，在10月26日畫下句點", "p. 3"),
        ("6比0完封兄弟，龍隊拋下紅色彩帶", "p. 4"),
        ("250家店家一起討糖", "p. 5"),
        ("旅展首日中午12點才開門", "p. 6"),
    ]
    p7 = texts(os.path.join(ED, "p7-lang.svg"))
    ok = True
    for q, pg in quotes:
        # occurrences across concatenated page texts (article + P7 = 2)
        cnt = all_ed.count(q)
        tag = f"(p. {pg.split('. ')[1]})" if ". " in pg else pg
        tag_ok = any(tag in t for t in p7)
        print(f"  {q[:20]}... count={cnt} tag {tag} on P7: {tag_ok}")
        ok = ok and cnt == 2 and tag_ok
    print(f"  all 8 verbatim x2 with correct tags: {ok}")
    out["p7_phrases_ok"] = ok

    # --- 7. readers' corner disclosures ---
    print("== readers' corner ==")
    core_p7 = texts(os.path.join(CORE, "p7-lang.svg"))
    ed_p7 = texts(os.path.join(ED, "p7-lang.svg"))
    trad = "延期披露：VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文；截至截稿，本報未收到可刊登的真實來信與投稿，因此本期仍刊登編輯範例，並繼續公開徵集。你的來信，下一期見。"
    # SVG text nodes wrap; join to compare
    core_join = "".join(core_p7)
    ed_join = "".join(ed_p7)
    print(f"  Traditional disclosure intact in edition: "
          f"{trad[:40] in ed_join and all(c in ed_join for c in trad)}")
    pt_disc = [t for t in ed_p7 if "Carta de exemplo" in t]
    print(f"  PT disclosure lines present: {len(pt_disc)}")
    out["readers_trad_intact"] = trad[:40] in ed_join

    # --- 8. residual-Latin adjudication: added strings vs core ---
    print("== residual Latin in added strings ==")
    core_sets = {n: Counter(texts(os.path.join(CORE, n))) for n in NAMES}
    ed_sets = {n: Counter(texts(os.path.join(ED, n))) for n in NAMES}
    EN_WORDS = re.compile(r"\b(the|and|with|from|this|that|week|English|notes|"
                          r"explanations|answer keys|first|more than|your|you are|"
                          r"is a|are the|for the|of the|to the|in the|on the)\b",
                          re.I)
    bad = 0
    for n in NAMES:
        for s, c in (ed_sets[n] - core_sets[n]).items():
            if re.search(r"[A-Za-z]", s) and EN_WORDS.search(s):
                print(f"  SUSPECT {n}: {s[:120]!r}")
                bad += 1
    print(f"  suspect added strings: {bad}")
    out["residual_latin_suspects"] = bad

    json.dump(out, open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "checks.json"), "w"),
        ensure_ascii=False, indent=1)
    print("checks.json written")


if __name__ == "__main__":
    main()
