# -*- coding: utf-8 -*-
"""JA edition scans: (1) line-start orphans (kinsoku closers + small kana
+ ASCII closers) per SVG <text> node; (2) residual Chinese word-level
scan: every CJK run in edition SVGs, for adjudication."""
import re, glob, sys

NO_START = set("。、，．！？：；）」』】ー…‥・")
NO_START |= set("ぁぃぅぇぉゃゅょっゎァィゥェォャュョッヮ")
NO_START |= set(").,;:!?%")
CJK = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]+")

for path in sorted(glob.glob('files/weekly-report-w45-it-ja/svg/*.svg')):
    t = open(path, encoding='utf-8').read()
    texts = re.findall(r'<text[^>]*>([^<]*)</text>', t)
    orph = [x for x in texts if x and x[0] in NO_START]
    print("== %s: nodes=%d orphans=%d" % (path.split('/')[-1], len(texts), len(orph)))
    for o in orph:
        print('   ORPHAN:', repr(o))
    if '--cjk' in sys.argv:
        runs = set()
        for x in texts:
            runs.update(CJK.findall(x))
        print('   CJK runs:', len(runs))
        for r in sorted(runs):
            print('   ', r)
