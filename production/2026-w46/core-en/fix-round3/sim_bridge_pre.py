#!/usr/bin/env python3
"""Round 3 pre-fix simulations (read-only): zh-tw P2 bridge wrap with the
zh-tw build's own TC svglib, and es/fr P3 title-slot measurements with each
edition's own svglib. No edition file touched."""
import sys
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-zh-tw-build')
from svglib import wrap, text_w
def show(label, s, kind, bold, size, w):
    lines = wrap(s, kind, bold, size, w)
    print(f"--- {label} ({len(lines)} line(s), total {text_w(s, kind, bold, size):.1f}px)")
    for ln in lines:
        print(f"  [{text_w(ln, kind, bold, size):7.1f}px] {ln!r}")
    return lines

# Bridge: expl() -> para 20.5pt sans, column width 434 (bslib4.py CW=434)
show("CURRENT zh-tw bridge (Round 1 fix, with lai + parens)",
     "用 will + 動詞原形來改寫（承諾與將要發生的事）。", "sans", False, 20.5, 434)
show("CORE bridge control (zh-cn, SC font in core build is NOT used here; TC wrap of core text)",
     "用 will + 动词改写（承诺与将要发生的事）。", "sans", False, 20.5, 434)
show("PROPOSED 1-line (verdict R-B6 correct text)",
     "用 will + 動詞原形改寫，承諾與將要發生的事。", "sans", False, 20.5, 434)
show("ALTERNATIVE 2-line (verdict)",
     "用 will + 動詞原形來改寫，表達承諾與將要發生的事。", "sans", False, 20.5, 434)
show("cand c no-lai short-tail",
     "用 will + 動詞原形改寫（承諾與未來）。", "sans", False, 20.5, 434)
show("cand d express future no-parens",
     "用 will + 動詞原形來改寫，表達承諾與未來。", "sans", False, 20.5, 434)
show("cand f parens short-tail no-lai",
     "用 will + 動詞原形改寫（承諾、未來）。", "sans", False, 20.5, 434)
