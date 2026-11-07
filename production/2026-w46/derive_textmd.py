# -*- coding: utf-8 -*-
"""Derive a fan-out <slug>.text.md from the core .text.md by applying the
fan-out transform.py REPL table (AST-extracted, never executed) plus
per-edition header replacements. Fails if CJK remains (non-CJK editions)
or if the core file changed shape unexpectedly."""
import ast, sys, re

def extract_repl(transform_path):
    tree = ast.parse(open(transform_path, encoding='utf-8').read())
    repl = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and getattr(node.targets[0], 'id', '') == 'REPL':
            repl.extend(ast.literal_eval(node.value))
        elif isinstance(node, ast.AugAssign) and getattr(node.target, 'id', '') == 'REPL':
            repl.extend(ast.literal_eval(node.value))
    # dedupe, longest-first
    seen, ordered = set(), []
    for old, new in repl:
        if old not in seen:
            seen.add(old); ordered.append((old, new))
    return sorted(ordered, key=lambda r: -len(r[0]))

def main(transform_path, core_text, out_path, header_old, header_new, sub_old, sub_new, allow_cjk, extras):
    repl = extract_repl(transform_path)
    t = open(core_text, encoding='utf-8').read()
    assert header_old in t, 'header line not found'
    t = t.replace(header_old, header_new, 1)
    assert sub_old in t, 'subtitle line not found'
    t = t.replace(sub_old, sub_new, 1)
    missing = []
    for old, new in repl:
        if old in t:
            t = t.replace(old, new)
        else:
            missing.append(old)
    print(f'applied {len(repl) - len(missing)}/{len(repl)} REPL entries; {len(missing)} absent from .text.md (expected: furniture-only strings)')
    for old, new in extras:
        assert old in t, f'extra not found: {old[:60]!r}'
        t = t.replace(old, new)
    for m in missing[:10]:
        print('  absent:', repr(m[:70]))
    if not allow_cjk:
        hits = re.findall(r'[\u4e00-\u9fff]', t)
        assert not hits, f'CJK remains: {len(hits)} chars'
        print('CJK 0 OK')
    open(out_path, 'w', encoding='utf-8').write(t)
    print('WROTE', out_path, len(t), 'bytes')

if __name__ == '__main__':
    extras = []
    rest = sys.argv[9:]
    assert len(rest) % 2 == 0, 'extras must be old/new pairs'
    for i in range(0, len(rest), 2):
        extras.append((rest[i], rest[i + 1]))
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8] == '1', extras)
