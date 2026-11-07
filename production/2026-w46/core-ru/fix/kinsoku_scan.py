# -*- coding: utf-8 -*-
"""Kinsoku scan: SVG text nodes ending with an opening bracket or starting
with a closing punctuation mark. Usage: kinsoku_scan.py <edition-dir>..."""
import re, sys, os, glob
TEXT_RE = re.compile(r'<text[^>]*x="([0-9.]+)"[^>]*y="([0-9.]+)"[^>]*font-size="([0-9.]+)"[^>]*>(.*?)</text>', re.S)
OPEN_END = set([chr(c) for c in [0xFF08, 0x28, 0xFF3B, 0xFF5B, 0x3008, 0x300A, 0x300C, 0x300E, 0x3010]])
CLOSE_START = set([chr(c) for c in [0x3002, 0x3001, 0xFF0C, 0xFF0E, 0xFF01, 0xFF1F, 0xFF1A, 0xFF1B, 0xFF09, 0x300D, 0x300F, 0x3011, 0x30FC, 0x2026, 0x2025, 0x30FB]])
def main():
    found = 0
    for ed in sys.argv[1:]:
        for svg in sorted(glob.glob(os.path.join(ed, "svg", "*.svg"))):
            t = open(svg, encoding="utf-8").read()
            for m in TEXT_RE.finditer(t):
                txt = re.sub(r"<[^>]+>", "", m.group(4)).strip()
                if not txt:
                    continue
                if txt[-1] in OPEN_END:
                    print("OPEN-END %s %s x=%s y=%s: %r" % (ed, os.path.basename(svg), m.group(1), m.group(2), txt))
                    found += 1
                if txt[0] in CLOSE_START:
                    print("CLOSE-START %s %s x=%s y=%s: %r" % (ed, os.path.basename(svg), m.group(1), m.group(2), txt))
                    found += 1
    print("TOTAL KINSOKU HITS: %d" % found)
    return 1 if found else 0
if __name__ == "__main__":
    sys.exit(main())
