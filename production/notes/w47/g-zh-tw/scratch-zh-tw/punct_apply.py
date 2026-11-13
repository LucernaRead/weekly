# Apply ASCII->full-width punctuation inside CJK strings (tokenize-based).
# v2 rules: (a) ',' skipped when both neighbours are digits (thousands sep);
# (b) '?' '!' convert when prev is CJK/CJK-punct (or '_' run after CJK), any next;
# (c) parens: string boundary counts as an acceptable neighbour.
import tokenize, io, sys

CJK = lambda ch: "\u4e00" <= ch <= "\u9fff"
CJKP = set("，。？！：；、（）《》「」『』—…")
def inset(ch): return CJK(ch) or ch in CJKP or ch.isdigit()
MAP = {",": "，", "?": "？", "!": "！", ";": "；"}

def prev_cjk(out, i):
    j = i - 1
    while j >= 0 and out[j] == "_":
        j -= 1
    return j >= 0 and (CJK(out[j]) or out[j] in CJKP)

def conv(s):
    out, i, changes = list(s), 0, []
    while i < len(out):
        ch = out[i]
        if ch in MAP:
            prev = out[i-1] if i > 0 else ""
            nxt = out[i+1] if i+1 < len(out) else ""
            ok = False
            if ch == ",":
                ok = inset(prev) and inset(nxt) and not (prev.isdigit() and nxt.isdigit())
            elif ch == ";":
                ok = inset(prev) and inset(nxt)
            elif ch in "?!":
                ok = prev_cjk(out, i)
            if ok:
                changes.append((ch, MAP[ch]))
                out[i] = MAP[ch]
        elif ch == ":":
            prev = out[i-1] if i > 0 else ""
            nxt = out[i+1] if i+1 < len(out) else ""
            if (CJK(prev) or prev in CJKP) and (CJK(nxt) or nxt.isdigit()):
                changes.append((ch, "："))
                out[i] = "："
        elif ch == "(":
            j = s.find(")", i)
            if j > i:
                inner = s[i+1:j]
                prev = out[i-1] if i > 0 else ""
                after = out[j+1] if j+1 < len(out) else ""
                if inner and all(inset(c) or c in " " for c in inner) and any(CJK(c) for c in inner) \
                   and (prev == "" or CJK(prev) or prev in CJKP or prev.isdigit()) \
                   and (after == "" or CJK(after) or after in CJKP or after.isdigit()):
                    changes.append(("(", "（")); changes.append((")", "）"))
                    out[i] = "（"; out[j] = "）"
        i += 1
    return "".join(out), changes

mode = sys.argv[1] if len(sys.argv) > 1 else "dry"
for path in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "checks.py"]:
    src = open(path, encoding="utf-8").read()
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    # rebuild source by applying replacements to string token spans
    edits = []
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
            if mode == "dry":
                print(f"{path}:{t.start[0]}: {val[:60]!r} -> {len(ch)} changes: {ch}")
            else:
                # re-quote with the same quote style as the original token
                q = t.string[0]
                if t.string.startswith(('"""', "'''")):
                    q = t.string[:3]
                esc_new = new.replace("\\", "\\\\").replace(q, "\\" + q)
                edits.append((t.start, t.end, q + esc_new + q))
    if mode == "apply" and edits:
        lines = src.splitlines(keepends=True)
        # apply edits from last to first (same line, later columns first)
        for (sline, scol), (eline, ecol), rep in sorted(edits, reverse=True):
            assert sline == eline
            lines[sline-1] = lines[sline-1][:scol] + rep + lines[sline-1][ecol:]
        open(path, "w", encoding="utf-8").write("".join(lines))
    print(f"{path}: {total} conversions")
