#!/usr/bin/env python3
"""Re-letter the 5 changed P8 note strings in the 9 transform maps (keys + values).
No build file is touched here. Asserts old keys present, new keys absent."""
import json, os, re

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")
CHANGES = [
    ("高潮场", "the peak sale period", "c", "d"),
    ("包裹", "a parcel", "b", "c"),
    ("取件码", "a pick-up code", "d", "b"),
    ("预报", "a forecast", "b", "a"),
    ("前置", "placed in advance", "a", "b"),
]
for lang in ["de", "es", "fr", "it", "ja", "ko", "nl", "pt", "ru"]:
    path = os.path.join(BASE, "w46", "maps", lang + ".json")
    raw_before = open(path, encoding="utf-8").read()
    data = json.loads(raw_before)
    for word, gloss, old, new in CHANGES:
        assert f"{word} = {gloss}, {old}" in data, (lang, word)
        assert f"{word} = {gloss}, {new}" not in data, (lang, word)
    new_data = {}
    for k, v in data.items():
        new_k, new_v = k, v
        for word, gloss, old, new in CHANGES:
            old_key = f"{word} = {gloss}, {old}"
            if k == old_key:
                new_k = f"{word} = {gloss}, {new}"
                m = re.match(r"^(.*[,、]\s?)([a-d])$", v)
                assert m and m.group(2) == old, (lang, k, v)
                new_v = m.group(1) + new
        new_data[new_k] = new_v
    changed = [k for k in data if k not in new_data]
    assert len(changed) == 5, (lang, changed)
    assert len(new_data) == len(data)
    out = json.dumps(new_data, ensure_ascii=False, indent=1)
    open(path, "w", encoding="utf-8").write(out + ("\n" if raw_before.endswith("\n") else ""))
    print(f"maps/{lang}.json: 5 note keys/values re-lettered; {len(data)} keys preserved")
print("MAPS DONE")
