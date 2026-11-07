import json, re, collections, unicodedata, sys
d = json.load(open('freeze-diff-proof.json'))
print("TOP KEYS:", list(d.keys()))
# dump structure sample
import pprint
def is_cjk(ch):
    o = ord(ch)
    return (0x4E00<=o<=0x9FFF) or (0x3400<=o<=0x4DBF) or (0xAC00<=o<=0xD7A3) or (0x1100<=o<=0x11FF) or (0x3130<=o<=0x318F) or (0x3040<=o<=0x30FF) or (0x0400<=o<=0x04FF)
def is_hangul_syl(ch):
    return 0xAC00 <= ord(ch) <= 0xD7A3
def is_hanja(ch):
    return 0x4E00 <= ord(ch) <= 0x9FFF or 0x3400 <= ord(ch) <= 0x4DBF

# Try to find per-page entries
pages = d.get('pages') or d.get('per_page') or d
if isinstance(pages, dict):
    items = pages.items()
else:
    items = enumerate(pages)
tot_delta = 0; tot_hangul_delta = 0; tot_hanja_delta = 0
for k, v in items:
    print(f"--- page key {k}: type {type(v)} keys {list(v.keys()) if isinstance(v, dict) else ''}")
    if isinstance(v, dict):
        for kk in v:
            val = v[kk]
            if isinstance(val, (list, dict)):
                print(f"    {kk}: {str(val)[:300]}")
            else:
                print(f"    {kk}: {val}")
