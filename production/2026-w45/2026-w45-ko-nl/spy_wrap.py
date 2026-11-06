# -*- coding: utf-8 -*-
"""Wrap-spy for W45 KO x NL orphan scan (ko-pt spy method, adapted).
Copies the transformed build to spy/, patches spy/svglib.py's wrap() to
log {text, kind, size, max_w, pre, post} lines per call, runs run.py in
spy/ (OUT redirected to spy/svg), verifies spy SVGs reproduce delivery
SVGs 8/8, then analyses post-kinsoku lines with the token-span method:
- a line boundary strictly inside a space-delimited token's span is a
  mid-token split; tail = the token remainder visible on the next line;
  flag iff tail has >=3 Hangul syllables (W45 KO standard, all prose
  columns; only tokens containing Hangul are in scope);
- a line starting with a NO_START closer is flagged (KO svglib ASCII set
  + full-width closers).
Run from this dir with tools/venv/bin/python spy_wrap.py
"""
import os, re, shutil, subprocess, sys, json, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.path.join(HERE, "spy")
LOG = os.path.join(HERE, "spy-wrap.log")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-nl")

def main():
    if os.path.exists(SCRATCH):
        shutil.rmtree(SCRATCH)
    os.makedirs(os.path.join(SCRATCH, "svg"))
    for f in ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "svglib.py", "run.py"]:
        shutil.copy(os.path.join(HERE, f), os.path.join(SCRATCH, f))
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(SCRATCH, "assets"))
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(SCRATCH, f)
        s = open(p, encoding="utf-8").read()
        s = s.replace("files/weekly-report-w45-ko-nl/svg",
                      "hidden_files/weekly-report-w45-ko-nl-build/spy/svg")
        open(p, "w", encoding="utf-8").write(s)
    p = os.path.join(SCRATCH, "svglib.py")
    s = open(p, encoding="utf-8").read()
    assert "import os" in s and "# kinsoku shori" in s, "svglib markers missing"
    s = s.replace("from PIL import ImageFont",
                  "from PIL import ImageFont\nimport json as _json")
    s = s.replace("    # kinsoku shori",
                  "    _spy_pre = list(lines)\n    # kinsoku shori")
    s = s.replace("    return lines\n\ndef esc",
                  "    _log = os.environ.get('SPY_LOG', '')\n"
                  "    if _log:\n"
                  "        with open(_log, 'a', encoding='utf-8') as _fh:\n"
                  "            _fh.write(_json.dumps({'text': text, 'kind': kind, 'bold': bold, 'size': size, 'max_w': max_w, 'pre': _spy_pre, 'post': list(lines)}, ensure_ascii=False) + '\\n')\n"
                  "    return lines\n\ndef esc")
    assert "_log" in s, "wrap return patch did not apply"
    open(p, "w", encoding="utf-8").write(s)
    if os.path.exists(LOG):
        os.remove(LOG)
    env = dict(os.environ, SPY_LOG=LOG)
    venv = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python")
    r = subprocess.run([venv, "run.py"], cwd=SCRATCH, env=env,
                       capture_output=True, text=True)
    print(r.stdout[-800:])
    print(r.stderr[-800:])
    assert r.returncode == 0, "spy run failed"
    n = sum(1 for _ in open(LOG, encoding="utf-8"))
    print(f"spy log: {n} wrap calls -> {LOG}")

    def sha(pth):
        return hashlib.sha256(open(pth, "rb").read()).hexdigest()
    ok = 0
    for fn in sorted(os.listdir(os.path.join(SCRATCH, "svg"))):
        same = sha(os.path.join(SCRATCH, "svg", fn)) == sha(os.path.join(ED, "svg", fn))
        ok += same
        print(f"  {fn}: spy==delivery {same}")
    print(f"spy reproduction: {ok}/8")
    assert ok == 8, "spy run did not reproduce delivery SVGs"

    HANGUL = lambda ch: "\uac00" <= ch <= "\ud7af"
    NO_START = set(")]}〉》.,!?%:;\"\'")
    splits, splits12, linestarts, unparsed = [], [], [], []
    for line in open(LOG, encoding="utf-8"):
        rec = json.loads(line)
        T, post = rec["text"], rec["post"]
        for nxt in post[1:]:
            if nxt.strip()[:1] in NO_START:
                linestarts.append({"text": T[:60], "next": nxt[:40], "first": nxt.strip()[:1], "size": rec["size"]})
        if len(post) < 2:
            continue
        p = 0
        for li, L in enumerate(post):
            seg = T[p:p + len(L)]
            if seg != L:
                # kinsoku oidashi: L's last char moved from next segment's start
                if li < len(post) - 1 and len(L) > 0 and L[:-1] == T[p:p + len(L) - 1] and L[-1] == T[p + len(L)]:
                    p += len(L) + 1
                    continue
                unparsed.append({"text": T[:80], "line": li, "L": L[:50], "seg": seg[:50], "p": p})
                break
            if li < len(post) - 1:
                b = p + len(L)
                if b < len(T) and T[b] == " ":
                    p = b + 1
                else:
                    ts = T.rfind(" ", 0, b) + 1
                    te = T.find(" ", b)
                    if te == -1:
                        te = len(T)
                    tok = T[ts:te]
                    if any(HANGUL(c) for c in tok):
                        nxtline = post[li + 1]
                        tail = T[b:min(te, b + len(nxtline))]
                        syl = sum(1 for c in tail if HANGUL(c))
                        ent = {"token": tok, "tail": tail, "tail_syl": syl,
                               "prev": L[-30:], "next": nxtline[:30], "size": rec["size"]}
                        splits.append(ent)
                        if syl >= 3:
                            splits12.append(ent)
                    p = b
    print(f"unparsed calls: {len(unparsed)}")
    for u in unparsed[:5]:
        print("  UNPARSED", u)
    print(f"mid-word splits total: {len(splits)}; tail>=3 syllables: {len(splits12)}")
    for e in splits12:
        print("  SPLIT>=3", e["token"], "tail", repr(e["tail"]), e["tail_syl"], "| prev", e["prev"], "| next", e["next"])
    print(f"line-start NO_START (post-kinsoku): {len(linestarts)}")
    for e in linestarts:
        print("  LINESTART", repr(e["first"]), e["next"][:50])
    json.dump({"splits": splits, "splits_ge3": splits12, "linestarts": linestarts},
              open(os.path.join(HERE, "spy_wrap_analysis.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("analysis -> spy_wrap_analysis.json")

if __name__ == "__main__":
    main()
