# -*- coding: utf-8 -*-
"""Independent orphan analysis on MY OWN instrumented wrap log.
Method (different from builder's spy token-span code):
 (a) char-sequence preservation: post lines joined with '' (spaces removed)
     must equal the original text with spaces removed (kinsoku moves only
     shift boundaries, never lose/duplicate chars);
 (b) boundary walk: walk a pointer over the original text; each post line
     must tile the text (exact match, or one-char oidashi shift where the
     line's last char equals the next text char); a boundary inside a
     space-delimited token yields a tail = token remainder visible on the
     next line; flag iff tail has >=3 Hangul syllables;
 (c) line-start scan: post[1:] lines starting with a NO_START closer
     (builder's set, incl. ASCII quote) are listed for adjudication.
"""
import json, sys
LOG = sys.argv[1]
HANGUL = lambda ch: "\uac00" <= ch <= "\ud7af"
NO_START = set(")]}〉》.,!?%:;\"'")
calls = [json.loads(l) for l in open(LOG, encoding="utf-8")]
print(f"wrap calls logged: {len(calls)}")
seq_bad, unparsed, splits_ge3, linestarts = [], [], [], []
for ci, rec in enumerate(calls):
    T, post = rec["text"], rec["post"]
    if "".join(post).replace(" ", "") != T.replace(" ", ""):
        seq_bad.append((ci, T[:70], post[:3]))
    # boundary walk
    p = 0; ok = True
    for li, L in enumerate(post):
        if li == len(post) - 1:
            # last line: must match remainder (allowing trailing strip)
            if T[p:].strip() != L.strip() and T[p:] != L:
                # oidashi on last line is impossible (no next line); allow rstrip diff only
                if T[p:].rstrip() != L.rstrip():
                    ok = False
            break
        seg = T[p:p + len(L)]
        adv = len(L)
        if seg == L:
            pass
        elif L and L[:-1] == T[p:p + len(L) - 1] and L[-1] == T[p + len(L)]:
            adv = len(L) + 1  # oidashi: last char pulled from next segment
        else:
            ok = False; break
        b = p + adv
        if b < len(T) and T[b] != " ":
            ts = T.rfind(" ", 0, b) + 1
            te = T.find(" ", b)
            if te == -1: te = len(T)
            tok = T[ts:te]
            if any(HANGUL(c) for c in tok):
                nxt = post[li + 1]
                tail = T[b:min(te, b + len(nxt))]
                syl = sum(1 for c in tail if HANGUL(c))
                if syl >= 3:
                    splits_ge3.append({"call": ci, "token": tok, "tail": tail, "syl": syl,
                                       "prev": L[-30:], "next": nxt[:30]})
        # advance: skip the space(s) at the boundary
        p = b
        while p < len(T) and T[p] == " ":
            p += 1
    if not ok:
        unparsed.append((ci, T[:80], post))
    for nxt in post[1:]:
        if nxt.strip()[:1] in NO_START:
            linestarts.append({"call": ci, "text": T[:70], "next": nxt[:50], "first": nxt.strip()[:1]})
print(f"char-sequence violations: {len(seq_bad)}")
for x in seq_bad[:5]: print("  SEQ", x)
print(f"unparsed (tiling failures): {len(unparsed)}")
for x in unparsed[:5]: print("  UNPARSED", x)
print(f"mid-token splits with tail>=3 Hangul syllables: {len(splits_ge3)}")
for x in splits_ge3[:10]: print("  SPLIT>=3", x)
print(f"line-start NO_START (post[1:]): {len(linestarts)}")
for x in linestarts: print("  LINESTART", x)
