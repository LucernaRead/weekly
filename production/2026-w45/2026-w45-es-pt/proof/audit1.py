import json, re, unicodedata
def is_cjk(ch): return '\u4e00'<=ch<='\u9fff' or '\u3400'<=ch<='\u4dbf' or '\u3040'<=ch<='\u30ff' or '\uac00'<=ch<='\ud7af'
d=json.load(open(f'{__import__("os").environ["HOME"]}/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-pt-proof/freeze-diff.json'))
for pg, v in sorted(d['pages'].items(), key=lambda x: int(x[0])):
    rem=v['removed_strings']; add=v['added_strings']
    nocjk=[r for r in rem if not any(is_cjk(c) for c in r['text'])]
    print(f"\n===== PAGE {pg}: removed={len(rem)} added={len(add)} removed-noCJK={len(nocjk)} =====")
    for r in nocjk: print(f"  REM[{r['count']}] {r['text']!r}")
    print(f"  --- added-noCJK sample (all {len([a for a in add if not any(is_cjk(c) for c in a['text'])])}):")
    for a in add:
        if not any(is_cjk(c) for c in a['text']): print(f"  ADD[{a['count']}] {a['text']!r}")
