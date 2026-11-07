#!/usr/bin/env python3
"""Apply D3/D4 registry fixes to all 10 W46 zh-cn build dirs + 9 transform maps.
Assertions: every old string must occur exactly once; nothing else changes.
Keys lists and the trailing letters inside P8 notes are fixed together —
P8 prints "{n}. {key} — {note}", and each note ends with ", <letter>",
so leaving a note letter stale would print a self-contradictory key line."""
import json, os, re, sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")
BUILD_DIRS = [
    "weekly-report-w46-zhcn-build",
    "weekly-report-w46-zh-cn-de-build", "weekly-report-w46-zh-cn-es-build",
    "weekly-report-w46-zh-cn-fr-build", "weekly-report-w46-zh-cn-it-build",
    "weekly-report-w46-zh-cn-ja-build", "weekly-report-w46-zh-cn-ko-build",
    "weekly-report-w46-zh-cn-nl-build", "weekly-report-w46-zh-cn-pt-build",
    "weekly-report-w46-zh-cn-ru-build",
]

def fix_build(d):
    for fname, old_keys, new_keys, new_notes in [
        ("content12.py", '["c", "b", "d", "a"]', '["d", "c", "b", "a"]', ["d", "c", "b", "a"]),
        ("content56.py", '["c", "d", "b", "a"]', '["c", "d", "a", "b"]', ["c", "d", "a", "b"]),
    ]:
        path = os.path.join(BASE, d, fname)
        lines = open(path, encoding="utf-8").read().split("\n")
        # keys line
        hits = [i for i, ln in enumerate(lines) if old_keys in ln]
        assert len(hits) == 1, (d, fname, "keys hits", hits)
        ki = hits[0]
        assert lines[ki].strip() == old_keys + ",", (d, fname, lines[ki])
        lines[ki] = lines[ki].replace(old_keys, new_keys)
        # notes line = next non-empty line; must hold 4 quoted note strings
        ni = ki + 1
        assert lines[ni].strip().startswith('["') or lines[ni].strip().startswith("[\""), (d, fname, lines[ni])
        notes_line = lines[ni]
        quoted = re.findall(r'"[^"]*"', notes_line)
        assert len(quoted) == 4, (d, fname, quoted)
        # each quoted note must end with separator + single letter before closing quote
        new_quoted = []
        for q, nl_ in zip(quoted, new_notes):
            m = re.match(r'^(.*[,、]\s?)([a-d])"$', q)
            assert m, (d, fname, q)
            new_quoted.append(m.group(1) + nl_ + '"')
        new_line = notes_line
        for old_q, new_q in zip(quoted, new_quoted):
            assert new_line.count(old_q) == 1, (d, fname, old_q)
            new_line = new_line.replace(old_q, new_q)
        lines[ni] = new_line
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(f"{d}/{fname}: keys {old_keys} -> {new_keys}; notes -> {new_notes}")

for d in BUILD_DIRS:
    fix_build(d)

# --- transform maps: the same 5 note strings, keys (English) + values (native) ---
CHANGES = [  # (word, english gloss, old letter, new letter)
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
    new_data = {}
    for k, v in data.items():
        new_k, new_v = k, v
        for word, gloss, old, new in CHANGES:
            old_key = f"{word} = {gloss}, {old}"
            if k == old_key:
                new_k = f"{word} = {gloss}, {new}"
                m = re.match(r"^(.*[,、])([a-d])$", v)
                assert m and m.group(2) == old, (lang, k, v)
                new_v = m.group(1) + new
        assert new_k not in new_data or new_k == k, (lang, new_k)
        new_data[new_k] = new_v
    # verify exactly 5 keys changed
    changed = [k for k in data if k not in new_data]
    assert len(changed) == 5, (lang, changed)
    assert len(new_data) == len(data)
    out = json.dumps(new_data, ensure_ascii=False, indent=1)
    # match original file ending: check trailing newline
    open(path, "w", encoding="utf-8").write(out + ("\n" if raw_before.endswith("\n") else ""))
    print(f"maps/{lang}.json: 5 note keys/values re-lettered; {len(data)} keys total preserved")
print("ALL FIXES APPLIED")
