# Dry run: convert ASCII punctuation to full-width inside CJK strings.
# Rules: only inside string literals containing CJK; only when both neighbours
# are in the CJK set {CJK, CJK punct, digits} (for , ? ! : ;) — end-of-string
# counts as a neighbour for ? and ! only when the other side is CJK.
# Parens: convert a (...) pair only when its content is CJK/digits/punct and the
# char before '(' and after ')' are CJK/CJK-punct/digit/end.
# Colon ':' is skipped when both neighbours are digits (times like 14:00).
import tokenize, io, unicodedata

CJK = lambda ch: "\u4e00" <= ch <= "\u9fff"
CJKP = set("，。？！：；、（）《》「」『』—…")
def inset(ch): return CJK(ch) or ch in CJKP or ch.isdigit()

MAP = {",": "，", "?": "？", "!": "！", ";": "；"}
def conv(s):
    out, i, changes = list(s), 0, []
    while i < len(out):
        ch = out[i]
        if ch in MAP:
            prev = out[i-1] if i > 0 else ""
            nxt = out[i+1] if i+1 < len(out) else ""
            ok = False
            if ch in ",;":
                ok = inset(prev) and inset(nxt)
            elif ch in "?!":
                ok = (CJK(prev) or prev in CJKP) and (nxt == "" or inset(nxt))
            if ok:
                changes.append((i, ch, MAP[ch], "".join(out[max(0,i-6):i+7])))
                out[i] = MAP[ch]
        elif ch == ":":
            prev = out[i-1] if i > 0 else ""
            nxt = out[i+1] if i+1 < len(out) else ""
            if (CJK(prev) or prev in CJKP) and (CJK(nxt) or nxt.isdigit()):
                changes.append((i, ch, "：", "".join(out[max(0,i-6):i+7])))
                out[i] = "："
        elif ch == "(":
            j = s.find(")", i)
            if j > i:
                inner = s[i+1:j]
                prev = out[i-1] if i > 0 else ""
                after = out[j+1] if j+1 < len(out) else ""
                if inner and all(inset(c) or c in " " for c in inner) and any(CJK(c) for c in inner) \
                   and (CJK(prev) or prev in CJKP or prev.isdigit()) \
                   and (after == "" or CJK(after) or after in CJKP or after.isdigit()):
                    changes.append((i, "(", "（", "".join(out[max(0,i-6):j+7])))
                    changes.append((j, ")", "）", ""))
                    out[i] = "（"; out[j] = "）"
        i += 1
    return "".join(out), changes

for path in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "checks.py"]:
    src = open(path, encoding="utf-8").read()
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    total = 0
    for t in toks:
        if t.type != tokenize.STRING:
            continue
        try:
            val = eval(t.string)
        except Exception:
            continue
        if not isinstance(val, str) or not any(CJK(c) for c in val):
            continue
        new, ch = conv(val)
        if ch:
            total += len(ch)
            print(f"{path}:{t.start[0]}: {val[:60]!r}")
            for c in ch:
                print(f"    {c[1]}->{c[2]}  ...{c[3]}...")
    print(f"{path}: {total} conversions\n")
