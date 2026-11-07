# One-time scaffolding: inject the reviewed map.json entries into
# transform.py as the inline MAP dict. After round 1, transform.py is the
# single source of truth; do NOT regenerate from map.json again.
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "map.json"), encoding="utf-8") as f:
    m = json.load(f)
assert len(m) == 186, len(m)
entries = []
for k, v in m.items():
    entries.append("    %s: %s," % (json.dumps(k, ensure_ascii=False),
                                    json.dumps(v, ensure_ascii=False)))
map_src = "MAP = {\n" + "\n".join(entries) + "\n}"
with open(os.path.join(HERE, "transform.py"), encoding="utf-8") as f:
    t = f.read()
assert "# __MAP_PLACEHOLDER__" in t
t = t.replace("# __MAP_PLACEHOLDER__", map_src, 1)
with open(os.path.join(HERE, "transform.py"), "w", encoding="utf-8") as f:
    f.write(t)
print("injected", len(m), "entries")
