# -*- coding: utf-8 -*-
"""Orphan scan for the W43 KO cover (task definition, revised 2026-10-28):
KOREAN PROSE = the 12 Korean explanations (EXPL). A Korean prose paragraph
FAILS iff its final line, after stripping trailing punctuation
[.!?…)]»」 etc., holds exactly ONE whitespace token. This is the 1-token
rule. The old <=3-character rule is RETIRED for Korean prose: it wrongly
passed 4-character 1-token finals ("시작해요.", "만이에요.") and is
insufficient by construction.

Headlines and source-language excerpts are NOT Korean prose and are
reported separately, never counted as prose flags: headline single-word
wraps are headline wraps, and CJK excerpts have no whitespace tokens,
so a token count is meaningless for them. Excerpt/headline finals are
still printed for eyeball review.

Explanations are scanned at their BUILT sizes: 45pt for nl/ja (2026-10-28
orphan fix), 46pt for all others — mirroring build.py exactly.
Run: python3 orphan_scan.py  (exit 0 = no Korean-prose orphan flags)
"""
import ast, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import wrap

BASE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(BASE, "build.py"), encoding="utf-8").read()
tree = ast.parse(src)
ns = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "EXPL":
        exec(compile(ast.Module(body=[node], type_ignores=[]), "build", "exec"), ns)
EXPL = ns["EXPL"]
ITEMS = json.load(open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w43.json"), encoding="utf-8"))
TRAIL = ".!?\u2026)]\u00bb\u300d\u300f\u3011\u300b"
flags = []
def info(label, s, kind, bold, size, max_w):
    lines = wrap(s, kind, bold, size, max_w)
    last = lines[-1] if lines else ""
    print(f"{label}: nlines={len(lines)} final={last!r} (info only, not Korean prose)")
def check_expl(label, s, size, max_w=1650):
    lines = wrap(s, "serif", False, size, max_w)
    last = lines[-1] if lines else ""
    stripped = last.rstrip(TRAIL).strip()
    ntok = len(stripped.split())
    bad = ntok <= 1
    tag = "FLAG" if bad else "ok"
    if bad:
        flags.append((label, last))
    print(f"{label}: size={size} nlines={len(lines)} final={last!r} tokens={ntok} -> {tag}")
for it in ITEMS:
    L = it["source_lang"]
    info(f"P1-teaser-{L}", it["headline"], "serif", True, 35, 1650)
    info(f"Px-head-{L}", it["headline"], "serif", True, 58, 1650)
    ex_size = 45 if L == "en" else 46
    info(f"Px-excerpt-{L}", it["excerpt"], "serif", False, ex_size, 1650)
    expl_size = 45 if L in ("nl", "ja") else 46
    check_expl(f"Px-expl-{L}", EXPL[L], expl_size)
    info(f"P8-head-{L}", it["headline"], "serif", True, 40, 1650)
print("KOREAN PROSE ORPHAN FLAGS (1-token rule):", len(flags), flags)
sys.exit(1 if flags else 0)
