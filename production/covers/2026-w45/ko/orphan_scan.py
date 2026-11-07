# -*- coding: utf-8 -*-
"""Orphan scan for the W45 KO cover (task definition): cover EVERY final-line
text element, with trailing punctuation [.!?…)]»」 etc. stripped before measuring.
Flags: stripped final line of <=3 chars, or a final line starting with closing
punctuation. Headline single-word finals are headline wraps, reported separately.
Also prints every final line so mid-word-split tails (>=3-syllable tail on a
final line, or a line starting with orphan punctuation) can be eyeballed.
Run: python3 orphan_scan.py  (exit 0 = no prose orphan flags)
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
ITEMS = json.load(open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/cover-backfill/headlines-w45.json"), encoding="utf-8"))
TRAIL = ".!?\u2026)\]\u00bb\u300d\u300f\u3011\u300b"
flags = []
def check(label, s, kind, bold, size, max_w, prose=True):
    lines = wrap(s, kind, bold, size, max_w)
    last = lines[-1] if lines else ""
    stripped = last.rstrip(TRAIL).strip()
    bad = len(stripped) <= 3 or (last[:1] in ".,!?%:;\"')]}")
    tag = "FLAG" if bad else "ok"
    if bad and prose:
        flags.append((label, last))
    print(f"{label}: nlines={len(lines)} final={last!r} -> {tag}")
for it in ITEMS:
    L = it["source_lang"]
    check(f"P1-teaser-{L}", it["headline"], "serif", True, 35, 1650, prose=False)
    check(f"Px-head-{L}", it["headline"], "serif", True, 58, 1650, prose=False)
    check(f"Px-excerpt-{L}", it["excerpt"], "serif", False, 45 if L == "zh-cn" else 46, 1650, prose=True)
    check(f"Px-expl-{L}", EXPL[L], "serif", False, 46, 1650, prose=True)
    check(f"P8-head-{L}", it["headline"], "serif", True, 40, 1650, prose=False)
# Cover-original P1/P8 furniture lines (prose where multi-line)
check("P1-title", "열두 개의 언어로 읽는 한 주", "serif", True, 66, 1650, prose=True)
check("P1-intro", "이번 주 세계 각지의 신문 1면이 전하는 소식들을 한곳에 모았어요. 열두 언어로 쓰인 헤드라인을 원문 그대로, 한국어 설명과 함께 읽어 보세요.", "serif", False, 38, 1500, prose=True)
check("P8-title", "이번 주 열두 편의 핵심 신문", "serif", True, 60, 1650, prose=True)
check("P8-intro", "아래 목록은 이번 주 12개 언어 핵심 신문의 1면 헤드라인이에요.", "serif", False, 36, 1500, prose=True)
print("PROSE ORPHAN FLAGS:", len(flags), flags)
sys.exit(1 if flags else 0)
