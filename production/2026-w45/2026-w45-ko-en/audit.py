# -*- coding: utf-8 -*-
"""KO x EN audit helpers (rendered-SVG based, venv PIL metrics).
- line_start_scan: any text node starting with a NO_START closer.
- split_scan: source-aware mid-word split check. Korean eojeol (space
  delimited words) are collected from the build source literals (ast,
  no execution). A rendered consecutive pair (same x, pitch 10-45)
  is a split iff the last token of line 1 + first token of line 2
  concatenates to a source word, the pair does NOT occur as two
  consecutive words in any source string, and the continuation token
  has >= 3 Hangul syllables. The retired 'first segment <= 1 syllable'
  criterion is NOT used.
- rowcheck: same-baseline (within 2px) text pairs, anchor-aware PIL
  advance boxes, overlapping or < 4px gap.
- edge_scan: anchor-aware rendered text extending past x=1887.
Usage: venv python audit.py <build-dir> <edition-svg-dir> [core-svg-dir]
"""
import re, sys, os, glob, ast

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

HANGUL = re.compile(r'[\uac00-\ud7a3]')
NO_START = set("。、，．！？：；）」』】ー…‥・)]}〉》.,!?%:;")
TEXT_RE = re.compile(r'<text([^>]*)>([^<]*)</text>')


def _attr(attrs, name):
    m = re.search(r'%s="([^"]+)"' % name, attrs)
    return m.group(1) if m else None


PUNCT = ".,!?%:;·、，。）」』】)]}〉》「『（【〈《([{ "


def load_texts(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in TEXT_RE.finditer(s):
        attrs, t = m.groups()
        fam = _attr(attrs, "font-family") or ""
        kind = "serif" if "Serif" in fam else "sans"
        out.append((float(_attr(attrs, "y")), float(_attr(attrs, "x")),
                    float(_attr(attrs, "font-size")), kind,
                    _attr(attrs, "font-weight") == "700",
                    _attr(attrs, "text-anchor") or "start", t))
    return sorted(out)


def line_start_scan(texts):
    return [(round(y, 1), round(x, 1), "LINE-START", t[:40])
            for y, x, fs, kind, bold, anchor, t in texts
            if t and t[0] in NO_START]


def source_words(build_dir):
    words, pairs = set(), set()
    for f in glob.glob(os.path.join(build_dir, "content*.py")):
        tree = ast.parse(open(f, encoding='utf-8').read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                toks = node.value.split()
                for tok in toks:
                    clean = tok.strip(PUNCT)
                    if HANGUL.search(clean):
                        words.add(clean)
                for a, b in zip(toks, toks[1:]):
                    pairs.add((a.strip(PUNCT), b.strip(PUNCT)))
    return words, pairs


def split_scan(texts, words, pairs):
    by_x = {}
    for y, x, fs, kind, bold, anchor, t in texts:
        by_x.setdefault(round(x, 1), []).append((y, t))
    flags = []
    for x, items in by_x.items():
        items.sort()
        for (y1, t1), (y2, t2) in zip(items, items[1:]):
            pitch = y2 - y1
            if not (10 <= pitch <= 45) or not t1 or not t2:
                continue
            frag1 = t1.split(" ")[-1].strip(PUNCT)
            frag2 = t2.split(" ")[0].strip(PUNCT)
            if not frag1 or not frag2:
                continue
            if not HANGUL.search(frag1[-1:]) or not HANGUL.search(frag2[:1]):
                continue
            joined = frag1 + frag2
            if joined in words and (frag1, frag2) not in pairs:
                n = len(HANGUL.findall(frag2))
                if n >= 3:
                    flags.append((round(y1, 1), round(x, 1),
                                  f"SPLIT tail={n}",
                                  f"{t1[-16:]!r} | {t2[:16]!r}"))
    return flags


def boxes(texts):
    out = []
    for y, x, fs, kind, bold, anchor, t in texts:
        w = svglib.text_w(t, kind, bold, fs)
        if anchor == "middle":
            out.append((y, x - w / 2, x + w / 2, t))
        elif anchor == "end":
            out.append((y, x - w, x, t))
        else:
            out.append((y, x, x + w, t))
    return out


def rowcheck(texts):
    by_y = {}
    for y, l, r, t in boxes(texts):
        by_y.setdefault(round(y), []).append((l, r, t))
    flags = []
    for y, parts in by_y.items():
        if len(parts) < 2:
            continue
        parts.sort()
        for (l1, r1, t1), (l2, r2, t2) in zip(parts, parts[1:]):
            if r1 > l2 - 4:
                flags.append((y, f"ROW-OVERLAP gap={l2 - r1:.1f} {t1[:28]!r} | {t2[:28]!r}"))
    return flags


def edge_scan(texts):
    return [(round(y, 1), f"RIGHT-EDGE ends={r:.1f} {t[:40]!r}")
            for y, l, r, t in boxes(texts) if r > 1887]


def main():
    build_dir, ed_dir = sys.argv[1], sys.argv[2]
    core_dir = sys.argv[3] if len(sys.argv) > 3 else None
    words, pairs = source_words(build_dir)
    print(f"source words: {len(words)}, word pairs: {len(pairs)}")
    for label, d in [("ED", ed_dir), ("CORE", core_dir)]:
        if not d:
            continue
        print(f"##### {label} {d}")
        for f in sorted(glob.glob(os.path.join(d, "*.svg"))):
            texts = load_texts(f)
            ls = line_start_scan(texts)
            sp = split_scan(texts, words, pairs)
            rw = rowcheck(texts)
            eg = edge_scan(texts)
            print(f"{os.path.basename(f)}: line-start={len(ls)} splits>=3={len(sp)} "
                  f"row-overlap={len(rw)} right-edge={len(eg)}")
            for flag in ls + sp + rw + eg:
                print("   ", flag)
            if "p7-" in f:
                print("   P7 teaser title:",
                      [(round(y, 1), t[:40]) for y, x, fs, k, b, a, t in texts
                       if t.startswith("다음 주")])
            if "p8-" in f:
                keys = [y for y, x, fs, k, b, a, t in texts if 1328 < y < 2540]
                print(f"   P8 keys flow last baseline: {max(keys) if keys else None}")


if __name__ == "__main__":
    main()
