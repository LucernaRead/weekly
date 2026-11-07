#!/usr/bin/env python3
"""Export <slug>.text.md from an edition's builder SVG manuscript.

Reads the 8 page SVGs in order, concatenates <text> elements in document
order, and writes a plain-text manuscript export. Never reads a PDF.
Usage: make_textmd.py <svg_dir> <slug> <week_label> <out_path>
"""
import re, html, glob, os, sys

def page_text(path):
    s = open(path, encoding="utf-8").read()
    lines = []
    for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", c)).strip()
        if t:
            lines.append(t)
    return lines

def main():
    svg_dir, slug, week, out = sys.argv[1:5]
    files = sorted(glob.glob(os.path.join(svg_dir, "*.svg")))
    assert len(files) == 8, f"expected 8 SVGs, got {len(files)}"
    out_lines = [f"# {slug}", "", f"Week: {week}", ""]
    for i, f in enumerate(files, 1):
        out_lines.append(f"## Page {i}")
        out_lines.append("")
        out_lines.extend(page_text(f))
        out_lines.append("")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out_lines))
    print(f"wrote {out} ({os.path.getsize(out)} bytes)")

if __name__ == "__main__":
    main()
