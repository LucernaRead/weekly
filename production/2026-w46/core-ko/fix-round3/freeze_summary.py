import json

def summ(p):
    d = json.load(open(p, encoding="utf-8"))
    t = d.get("cjk_added_total", {})
    hang = sum(v for k, v in t.items() if "\uac00" <= k <= "\ud7a3")
    fffd = {k: v for k, v in t.items() if ord(k) == 0xFFFD}
    return sum(t.values()), hang, fffd

BASE3 = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-fix-round3/gates"
BASE2 = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ko-proofread-gates-round2"
for code in ["de", "en", "es", "fr", "it", "ja", "nl", "pt", "ru", "zh-tw"]:
    print("R3", code, summ(f"{BASE3}/freeze-{code}.json"))
for code in ["ja", "pt", "zh-tw"]:
    print("R2", code, summ(f"{BASE2}/freeze-{code}.json"))
