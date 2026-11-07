#!/usr/bin/env python3
"""KO orphan scan (README #16): window 10-45px pitch, >=3-syllable-tail
mid-word splits, line-start orphan punctuation, final-line short-token
orphans (incl. parenthesised fragments). Groups text nodes into columns
by x-cluster, then consecutive baselines with pitch in [10,45] into
paragraph groups. Reports qualifying sites; identical frozen Korean
prose must give identical results on core vs edition."""
import xml.etree.ElementTree as ET, re, sys
NS = '{http://www.w3.org/2000/svg}'
HANGUL = re.compile(r'[\uac00-\ud7a3]')
ORPHAN_START = set('?. ,)]}」』;:')
PAGES = ["p1-pyoji", "p2-saenghwal", "p3-munhwa", "p4-seupocheu",
         "p5-cheongnyeon", "p6-gipi", "p7-mal", "p8-siheom"]

def syl_count(s):
    return len(HANGUL.findall(s))

def load(edition):
    out = {}
    for pg in PAGES:
        p = f"/home/hatch/workspace/goals/lucernaread-social-media-operations/files/{edition}/svg/{pg}.svg"
        root = ET.parse(p).getroot()
        nodes = []
        for el in root.iter(NS + 'text'):
            t = ''.join(el.itertext())
            if HANGUL.search(t):
                nodes.append((float(el.get('x')), float(el.get('y')), t))
        out[pg] = nodes
    return out

def scan(edition):
    flags = []
    for pg, nodes in load(edition).items():
        # column clusters by x (tolerance 30px)
        nodes.sort(key=lambda n: (round(n[0] / 30), n[1]))
        cols = {}
        for x, y, t in nodes:
            cols.setdefault(round(x / 30), []).append((x, y, t))
        for col, items in cols.items():
            items.sort(key=lambda n: n[1])
            # paragraph groups: consecutive pitch in [10,45]
            groups, cur = [], [items[0]] if items else []
            for prev, nxt in zip(items, items[1:]):
                pitch = nxt[1] - prev[1]
                if 10 <= pitch <= 45:
                    cur.append(nxt)
                else:
                    groups.append(cur); cur = [nxt]
            if cur: groups.append(cur)
            for g in groups:
                if len(g) < 2:
                    continue
                for a, b in zip(g, g[1:]):
                    # line-start orphan punctuation
                    bt = b[2].lstrip()
                    if bt and bt[0] in ORPHAN_START:
                        flags.append((pg, round(b[1], 1), 'START-PUNCT', b[2][:40]))
                    # mid-word split: a ends with Hangul (no trailing space/punct),
                    # b starts with Hangul; tail = b's first space-delimited token
                    at = a[2].rstrip()
                    if at and HANGUL.search(at[-1]) and bt and HANGUL.search(bt[0]):
                        first = bt.split(' ')[0].split('·')[0]
                        if syl_count(first) >= 3:
                            flags.append((pg, round(b[1], 1), 'SPLIT>=3', f"{at[-12:]} | {first}"))
                # final-line orphan: last token (strip trailing punct + ')')
                last = g[-1][2].strip()
                tok = last.split(' ')[-1] if last else ''
                tok = tok.strip('.,;:!?') .rstrip(')').strip('«»「」')
                if tok and HANGUL.search(tok) and syl_count(tok) <= 2:
                    # only when the final line is a short tail line (width < 60% of group median)
                    import statistics
                    widths = [len(x[2]) for x in g]
                    if len(last) < 0.6 * statistics.median(widths):
                        flags.append((pg, round(g[-1][1], 1), 'FINAL-SHORT', last[-40:]))
    return flags

if __name__ == '__main__':
    for ed in sys.argv[1:]:
        fl = scan(ed)
        print(f"== {ed}: {len(fl)} qualifying sites ==")
        for f in fl:
            print("  ", f)
