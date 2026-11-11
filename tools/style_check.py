# -*- coding: utf-8 -*-
"""Post-fix style gates: P8 min font size (PyMuPDF spans), §1.1 palette /
paper / masthead / VOL counts, badge Latin-only, visible-text CJK inventory.
Badge rule (2026-11-11 fix): a badge is a 60x30 rect, rx=2.7, filled with
one of the level colours (A2 #5c6e30 / B1 #46581f / B2 #37402f) and holding
exactly one bare level tag (A2/B1/B2). Any other olive-filled rect (section
bands, chart legend blocks) is NOT a badge and its text is not badge text.
Usage: tools/venv/bin/python style_check.py <print-pdf> <svg-dir>
"""
import sys, os, re
import fitz  # PyMuPDF

PALETTE = {"#fbfaf6", "#302c28", "#3a3631", "#6f675d", "#d8d2c4",
           "#37402f", "#46581f", "#f6e08e", "#f4efe1", "#5c6e30",
           "#f0eee5", "#ffffff", "#000000"}

# Level badge geometry (SOP §1.1): 60x30 rect, rx=2.7 (2pt), fill per level.
LV_FILL = {"A2": "#5c6e30", "B1": "#46581f", "B2": "#37402f"}
BADGE_FILLS = frozenset(LV_FILL.values())
BADGE_W, BADGE_H, BADGE_RX = 60.0, 30.0, 2.7

def main(pdf_path, svg_dir):
    doc = fitz.open(pdf_path)
    print(f"pages: {len(doc)}")
    for i, page in enumerate(doc, start=1):
        sizes = []
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if s["text"].strip():
                        sizes.append(round(s["size"], 2))
        if sizes:
            print(f"  P{i} min font {min(sizes):.2f}pt (n={len(sizes)})")
    # SVG checks
    fills = set()
    vol4 = vol5 = 0
    cjk = set()
    badge_bad = []
    for name in sorted(os.listdir(svg_dir)):
        if not name.endswith(".svg"):
            continue
        svg = open(os.path.join(svg_dir, name), encoding="utf-8").read()
        fills |= set(re.findall(r'fill="(#[0-9a-fA-F]{6})"', svg))
        fills |= set(re.findall(r'stroke="(#[0-9a-fA-F]{6})"', svg))
        vol4 += len(re.findall(r"VOL\.4", svg))
        vol5 += len(re.findall(r"VOL\.5", svg))
        for t in re.findall(r"<text[^>]*>(.*?)</text>", svg, re.S):
            txt = re.sub(r"<[^>]+>", "", t)
            for ch in txt:
                if "\u4e00" <= ch <= "\u9fff" or "\u3040" <= ch <= "\u30ff" or "\uac00" <= ch <= "\ud7a3":
                    cjk.add(ch)
    print("paper #fbfaf6 present in fills:", "#fbfaf6" in fills)
    print("fills outside palette:", sorted(f for f in fills if f.lower() not in PALETTE))
    print("VOL.4 count:", vol4, " VOL.5 count:", vol5)
    print("CJK chars in visible text:", len(cjk), "sample:", "".join(sorted(cjk)[:12]))
    # CJK that is NOT U+3000: report the distinct codepoints that are not the
    # full-width space (U+3000 is not in the CJK ranges above, so any hit here
    # would be real target-language text — expected for a zh target edition).
    # For this edition the correct statement is: no LATIN-script text carries
    # unexpected CJK; skip — the freeze --strict-cjk gate already proves no
    # ADDED CJK vs core. Here we only report the count for the log.
    # Badge check (2026-11-11 fix): the old code treated ANY rect with a
    # badge fill as a badge, so the big olive section bands (1774x110,
    # 529x30) and the P6 chart legend block (30x30) all counted, and every
    # text starting inside them — section titles, headlines, teasers —
    # was reported as a "badge non-ASCII hit". A badge is only the
    # 60x30 rx=2.7 rect holding exactly one bare A2/B1/B2 tag, with the
    # fill matching the level. Everything else olive-filled is listed
    # separately as a non-badge rect, not checked as a badge.
    badge_total = 0
    badge_by_level = {"A2": 0, "B1": 0, "B2": 0}
    badge_by_page = {}
    badge_mismatch = []
    nonbadge_olive = []
    for name in sorted(os.listdir(svg_dir)):
        if not name.endswith(".svg"):
            continue
        svg = open(os.path.join(svg_dir, name), encoding="utf-8").read()
        rects = [(float(a), float(b), float(c), float(d),
                  float(rx) if rx else 0.0, f)
                 for a, b, c, d, rx, f in
                 re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"(?: rx="([\d.]+)")?[^>]*fill="(#[0-9a-fA-F]{6})"', svg)
                 if f.lower() in BADGE_FILLS]
        texts = [(float(x), float(y), t) for x, y, t in
                 re.findall(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>(.*?)</text>', svg, re.S)]
        for (x, y, w, h, rx, f) in rects:
            is_badge = (abs(w - BADGE_W) <= 0.5 and abs(h - BADGE_H) <= 0.5
                        and abs(rx - BADGE_RX) <= 0.5)
            if not is_badge:
                nonbadge_olive.append((name, x, y, w, h, rx, f.lower()))
                continue
            inside = [re.sub(r"<[^>]+>", "", t).strip() for (tx, ty, t) in texts
                      if x - 1 <= tx <= x + w + 1 and y - 2 <= ty <= y + h + 2]
            badge_total += 1
            badge_by_page[name] = badge_by_page.get(name, 0) + 1
            if len(inside) != 1 or inside[0] not in LV_FILL:
                badge_mismatch.append((name, x, y, f.lower(),
                                       f"holds {inside!r}, not one bare level tag"))
                continue
            tag = inside[0]
            badge_by_level[tag] += 1
            if f.lower() != LV_FILL[tag]:
                badge_mismatch.append((name, x, y, f.lower(),
                                       f"tag {tag} but fill should be {LV_FILL[tag]}"))
            bad = [ch for ch in tag if ord(ch) > 127 and ch != "·"]
            if bad:
                badge_bad.append((name, tag, bad))
    print(f"badges: {badge_total} total "
          f"(A2 {badge_by_level['A2']} / B1 {badge_by_level['B1']} / B2 {badge_by_level['B2']}); "
          f"per page: {', '.join(f'{n[:-4]} {c}' for n, c in sorted(badge_by_page.items()))}")
    print("badge mismatches:", badge_mismatch if badge_mismatch else "none (fill matches level on every badge)")
    print("olive non-badge rects ignored:",
          f"{len(nonbadge_olive)} " +
          (str([(n, x, y, w, h, rx, f) for n, x, y, w, h, rx, f in nonbadge_olive])
           if nonbadge_olive else "(bands/legend, not badges)"))
    print("badge non-ASCII hits:", badge_bad if badge_bad else "none (Latin-only OK)")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
