import json, hashlib

W = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-fix-round3"
CODES = ["zh-cn", "de", "en", "es", "fr", "it", "ja", "nl", "pt", "ru", "zh-tw"]

def khash(j):
    return hashlib.sha256(json.dumps(j["keys"], ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]

print("== P8 key extraction diff, pre-fix vs post-fix ==")
for code in CODES:
    a = json.load(open(f"{W}/pre-fix/p8keys/{code}.json", encoding="utf-8"))
    b = json.load(open(f"{W}/gates/p8keys-post-{code}.json", encoding="utf-8"))
    same_keys = a["keys"] == b["keys"]
    same_set = a["noted_set"] == b["noted_set"]
    diffs = [n for n in a["keys"] if a["keys"][n] != b["keys"].get(n)]
    print(code, "keys-identical:", same_keys, "noted-set-identical:", same_set,
          "diff-numbers:", diffs, "hash:", khash(a), khash(b),
          "| 54:", b["keys"]["54"], "| 103:", b["keys"]["103"])

print()
print("== exercise blocks 54 / 103 / 69 from post-fix extraction ==")
ex = json.load(open(f"{W}/gates/counts/exercises-all.json", encoding="utf-8"))
for code in CODES:
    items = {it["num"]: it for it in ex[code]["items"]}
    for n in ("54.", "103.", "69."):
        it = items.get(n)
        print(code, n, it["level"] if it else None, repr(it["text"]) if it else "MISSING", it["page"] if it else "")
    print("---")
