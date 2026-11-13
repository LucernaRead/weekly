#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export <slug>.text.md for W46 zh-tw editions from the edition's own SVG
text layer in page order (source-side; never from a PDF). Format matches
the shipped core/DE text.md files: H1 + '## Page N — <name>' headings,
every non-empty <text> node in document order, blank line between nodes.
Usage: export_zhtw_textmd.py <svg_dir> <out.md> "<H1 without leading #>"
"""
import html, os, re, sys

PAGES = [("p1-front.svg", "Front"), ("p2-life.svg", "Life"),
         ("p3-culture.svg", "Culture"), ("p4-sport.svg", "Sport"),
         ("p5-youth.svg", "Youth"), ("p6-deep.svg", "Deep read"),
         ("p7-lang.svg", "Language focus"), ("p8-test.svg", "Test and keys")]

def page_text(path):
    s = open(path, encoding="utf-8").read()
    lines = []
    for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
        if t and t != "Lucerna":  # masthead wordmark only; footers stay (DE precedent)
            lines.append(t)
    return lines

def main():
    svg_dir, out, title = sys.argv[1], sys.argv[2], sys.argv[3]
    out_lines = [f"# {title}", ""]
    for i, (fname, name) in enumerate(PAGES, 1):
        out_lines.append(f"## Page {i} — {name}")
        out_lines.append("")
        for t in page_text(os.path.join(svg_dir, fname)):
            out_lines.append(t)
            out_lines.append("")
        out_lines.append("")
    text = "\n".join(out_lines)
    open(out, "w", encoding="utf-8").write(text)
    print(f"wrote {out}: {len(text)} bytes")

if __name__ == "__main__":
    main()
