import sys, os
sys.path.insert(0, "tools")
import occlusion_audit as oa

def check_page(path):
    els, W, H = oa.parse_svg(open(path, encoding="utf-8").read())
    texts = [e for e in els if e.kind == "text"]
    same = []
    for i, a in enumerate(texts):
        for b in texts[i+1:]:
            if abs(a.baseline - b.baseline) < 0.6:
                if a.box[0] < b.box[2] and b.box[0] < a.box[2]:
                    same.append((a.text[:60], b.text[:60]))
    hits = []
    for i, t in enumerate(els):
        if t.kind != "text": continue
        for r in els[i+1:]:
            if r.kind == "rect" and oa.overlap(t.box, r.box)[0] > 0:
                hits.append((t.text[:70], r.box))
    return same, hits

for fn in ["p1-front.svg","p2-life.svg","p3-culture.svg","p4-sport.svg","p5-youth.svg","p6-deep.svg","p7-lang.svg","p8-test.svg"]:
    for label, d in [("ed","files/weekly-report-w45-zh-tw-pt/svg"),("co","files/weekly-report-w45-zhtw-core/svg")]:
        same, hits = check_page(os.path.join(d, fn))
        print(f"{label} {fn}: same-baseline={len(same)} text-vs-later-rect={len(hits)}")
        for s_ in same[:5]: print("   SAME:", s_)
        if fn in ("p4-sport.svg","p6-deep.svg"):
            for h in hits[:5]: print("   RECT:", h)
