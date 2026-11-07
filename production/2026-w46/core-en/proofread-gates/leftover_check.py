#!/usr/bin/env python3
"""Proofreader-only source leftover check (read-only).
Extract string literals containing Han/Hangul from core build sources and
from a fan-out build's sources; report fan-out literals identical to core
literals (untranslated leftovers), with adjudication hints:
- value == key / shared glyphs (zh-tw): identical Han strings that are the
  same in SC and TC (no SC-only char) are script-identical, not residue.
- ko: any Han literal remaining in ko sources (excluding fullwidth ;/:).
"""
import ast, re, sys
from pathlib import Path

H = Path.home() / 'workspace/goals/lucernaread-social-media-operations/hidden_files'
CORE = H / 'weekly-report-w46-en-build'

def literals(builddir):
    out = {}  # literal -> [files]
    for py in sorted(Path(builddir).glob('*.py')):
        try:
            tree = ast.parse(py.read_text(encoding='utf-8'))
        except Exception:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                s = node.value
                if any('\u4e00' <= c <= '\u9fff' or '\u3040' <= c <= '\u30ff' or '\uac00' <= c <= '\ud7a3' for c in s):
                    out.setdefault(s, []).append(py.name)
    return out

core_lit = literals(CORE)
print('core Han/CJK literals:', len(core_lit))
for ed in ['ko', 'zh-tw']:
    ed_lit = literals(H / f'weekly-report-w46-en-{ed}-build')
    print(f'== {ed}: {len(ed_lit)} CJK literals in fan-out sources ==')
    identical = {s: f for s, f in ed_lit.items() if s in core_lit}
    print(f'identical-to-core literals: {len(identical)}')
    SC_ONLY = set('发让说这为读对电话语认时电个会国长门问间实应头关并没与将从众义习双变买卖乐东业丝专传伤体余侧侨俭仓仪们优伦伟伪伞运连远还进边达过讲译练')
    for s, files in sorted(identical.items()):
        sc = [c for c in s if c in SC_ONLY]
        print(f'  {"SC-RESIDUE" if sc else "shared-glyph"} {files} :: {s[:90]!r} SCchars={sc}')
    # Han literals in ko sources that are NOT in core (should be ~0; new Han = defect)
    if ed == 'ko':
        newhan = {s: f for s, f in ed_lit.items() if s not in core_lit and any('\u4e00' <= c <= '\u9fff' for c in s)}
        print(f'ko NEW Han literals (not in core): {len(newhan)}')
        for s, f in sorted(newhan.items()):
            print('  NEW-HAN', f, repr(s[:90]))
