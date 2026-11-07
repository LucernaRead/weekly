#!/usr/bin/env python3
"""Proofreader-only: render freeze-diff JSONs as readable per-edition
removed/added string lists. Read-only."""
import json, sys
from pathlib import Path

g = Path.home() / 'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates'
for ed in ['de', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh-tw']:
    d = json.load(open(g / f'freeze-{ed}.json'))
    lines = []
    for pg in sorted(d['pages'], key=lambda k: int(k)):
        p = d['pages'][pg]
        lines.append(f'===== PAGE {pg} =====')
        lines.append(f'--- REMOVED (core zh-cn layer) [{len(p.get("removed_strings", []))}] ---')
        for s in p.get('removed_strings', []):
            lines.append(f"R x{s['count']}: {s['text']}")
        lines.append(f'--- ADDED (edition layer) [{len(p.get("added_strings", []))}] ---')
        for s in p.get('added_strings', []):
            lines.append(f"A x{s['count']}: {s['text']}")
    (g / f'diff-{ed}.txt').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(ed, 'removed', sum(len(d['pages'][k].get('removed_strings', [])) for k in d['pages']),
          'added', sum(len(d['pages'][k].get('added_strings', [])) for k in d['pages']))
