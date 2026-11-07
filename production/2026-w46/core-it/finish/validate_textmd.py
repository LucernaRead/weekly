# -*- coding: utf-8 -*-
"""Validate an IT <slug>.text.md against the edition's own SVGs (consistency
check only — the .text.md itself is derived from build sources, never from
SVG/PDF). Both directions, whitespace-insensitive (SVG wraps lines).
"""
import glob, html, os, re, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")


def svg_text(eddir):
    parts = []
    for f in sorted(glob.glob(os.path.join(eddir, "svg", "*.svg"))):
        s = open(f, encoding="utf-8").read()
        for m in re.finditer(r"<text[^>]*>(.*?)</text>", s, re.S):
            t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
            if t:
                parts.append(t)
    return parts


def flat(s):
    return re.sub(r"\s+", "", s)


def main(code, slug):
    eddir = os.path.join(GOAL, "files", f"weekly-report-w46-it-{code}")
    md = open(os.path.join(eddir, f"{slug}.text.md"), encoding="utf-8").read()
    nodes = svg_text(eddir)
    svgflat = flat(" ".join(nodes))
    # ---- forward: text.md content must be in SVG text ----
    fwd_miss = []
    for line in md.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^\d+[–-]\d+\. \[.*?\]\s*(.*)$", line) or re.match(r"^\d+\. \[.*?\]\s*(.*)$", line)
        if m:
            rest = m.group(1)
            # match_set item: "left — right (key K · note)" -> check parts separately
            mm = re.match(r"^(.*?) — (.*?) \(key \S+ · (.*)\)$", rest)
            if mm:
                for comp in mm.groups():
                    if len(flat(comp)) >= 8 and flat(comp) not in svgflat:
                        fwd_miss.append(("ms-part", comp[:60]))
                continue
            body = re.split(r"\s+— key:|\s+\[", rest)[0]
            for comp in [body]:
                if len(flat(comp)) >= 8 and flat(comp) not in svgflat:
                    fwd_miss.append(("ex-body", comp[:70]))
            km = re.search(r"— key: (.+?)(?: \(|\s*\[|$)", rest)
            # writing items print only ✓ + note on P8; their parenthesised
            # open-task key is registry-only and never rendered
            if km and not km.group(1).startswith("(") \
                    and len(flat(km.group(1))) >= 3 and flat(km.group(1)) not in svgflat:
                fwd_miss.append(("ex-key", km.group(1)[:60]))
            nm = re.search(r"\(([^()]*)\)\s*(?:\[|$)", rest)
            if nm and len(flat(nm.group(1))) >= 8 and flat(nm.group(1)) not in svgflat:
                fwd_miss.append(("ex-note", nm.group(1)[:60]))
            continue
        m2 = re.match(r"^\d+\. (.*)$", line)
        if m2 and " — " in m2.group(1) and "(key " in m2.group(1):
            # match_set item: "N. left — right (key K · note)"
            mm = re.match(r"^(.*?) — (.*?) \(key \S+ · (.*)\)$", m2.group(1))
            if mm:
                for comp in mm.groups():
                    if len(flat(comp)) >= 8 and flat(comp) not in svgflat:
                        fwd_miss.append(("ms-part", comp[:60]))
                continue
        if m2 and "—" in m2.group(1):
            # Risposte answer line
            for comp in m2.group(1).split("—"):
                if len(flat(comp)) >= 8 and flat(comp) not in svgflat:
                    fwd_miss.append(("ans", comp.strip()[:60]))
            continue
        if len(flat(line)) >= 8 and flat(line) not in svgflat:
            fwd_miss.append(("line", line[:80]))
    # ---- reverse: long SVG nodes must be in text.md ----
    mdflat = flat(md)
    rev_miss = []
    for t in nodes:
        tt = t.strip()
        # strip render-added exercise numbers / right-column letters; the
        # body after them is what the manuscript must contain
        tt = re.sub(r"^\d+\s*[–-]\s*\d+\.\s+", "", tt)
        tt = re.sub(r"^\d+\.\s+(?=[A-ZÀ-Þa-z«\"'\(])", "", tt)
        tt = re.sub(r"^[a-d]\.\s+", "", tt)
        if len(flat(tt)) < 8:
            continue
        if re.search(r"^(Page|Pagina|Página|Seite|Страница|第)\b.*\b(of|di|de|von|из|/)\b", tt) \
                or re.fullmatch(r"—[^—]*\d+[^—]*—", tt) \
                or tt in ("La Lucerna",) or "VOL.3" in tt:
            continue
        if flat(tt) not in mdflat:
            rev_miss.append(t[:90])
    print(slug, "forward-miss:", len(fwd_miss), "reverse-miss:", len(rev_miss))
    for k, v in fwd_miss[:20]:
        print("  FWD", k, repr(v))
    for v in rev_miss[:20]:
        print("  REV", repr(v))
    return 0 if not fwd_miss and not rev_miss else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
