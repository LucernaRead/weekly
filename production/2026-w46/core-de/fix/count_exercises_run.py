#!/usr/bin/env python3
"""Independent re-measurement of exercise totals + level split from SHIPPED SVGs.
Reads <text> elements in document order. A level chip is a standalone 'A2'/'B1'/'B2'
element; an exercise item is the next expected sequential number, either standalone
'N.' or inline 'N. ...'. Skips the P1 Fragen box and the P8 answer-key region.
Untagged P8 groups (cloze options, dialogue options) are counted as UNTAGGED here;
their registry levels are cross-checked separately from the frozen build sources
(content8.py cloze_defs/ddefs, read-only)."""
import re, html, json, pathlib, sys

BASE = pathlib.Path.home()/'workspace/goals/lucernaread-social-media-operations/files'
PAGES = ['p1-front.svg','p2-leben.svg','p3-kultur.svg','p4-sport.svg','p5-jugend.svg','p6-vertiefung.svg','p7-sprache.svg','p8-uebungen.svg']

def texts_of(path):
    s = path.read_text(encoding='utf-8')
    s = re.sub(r'data:image[^"\']*', 'IMG', s)
    return [html.unescape(re.sub(r'<[^>]+>', '', c)).strip()
            for c in re.findall(r'<text[^>]*>(.*?)</text>', s, re.S)]

def count_edition(edir):
    items = []  # (n, level, page)
    per_page = {}
    for pgfile in PAGES:
        ts = texts_of(edir/'svg'/pgfile)
        cur = None
        expected = None
        skip_fragen = False
        in_ex = False
        page_items = []
        for t in ts:
            if not in_ex and ('ÜBUNGEN' in t or 'JETZT ÜBEN' in t or 'UHRZEITEN & DATEN' in t or 'UHRZEITEN' in t):
                in_ex = True
            if not in_ex:
                continue
            if pgfile.startswith('p1') and ('Fragen der Woche' in t or 'FRAGEN' in t):
                skip_fragen = True
            if skip_fragen and t.startswith('IN DIESER AUSGABE'):
                skip_fragen = False
            if skip_fragen:
                continue
            if pgfile.startswith('p8') and t.startswith('ANTWORTEN'):
                break
            if t in ('A2', 'B1', 'B2'):
                cur = t
                continue
            m = re.match(r'^(\d+)\.$', t) or re.match(r'^(\d+)\.\s', t)
            if m and '–' not in t:
                n = int(m.group(1))
                if expected is None:
                    expected = n
                if n == expected and n not in [x[0] for x in page_items]:
                    page_items.append((n, cur, pgfile))
                    expected = n + 1
        per_page[pgfile] = page_items
        items.extend(page_items)
    return items, per_page

out = {}
for slug in ['de-core','de-en','de-es','de-fr','de-it','de-ja','de-ko','de-nl','de-pt','de-ru','de-zh-cn','de-zh-tw']:
    items, per_page = count_edition(BASE/f'weekly-report-w46-{slug}')
    from collections import Counter
    lv = Counter(l for _, l, _ in items)
    out[slug] = {
        'total_scanned': len(items),
        'numbers': [n for n, _, _ in items],
        'continuous_1_to_N': [n for n, _, _ in items] == list(range(1, len(items)+1)),
        'per_page': {k: len(v) for k, v in per_page.items()},
        'levels_from_chips': dict(lv),
        'untagged': [n for n, l, _ in items if l is None],
        'missing_in_scan': [n for n in range(1, 151) if n not in [x[0] for x in items]],
    }
    print(slug, 'total=', len(items), 'per_page=', out[slug]['per_page'], 'levels=', dict(lv),
          'untagged=', out[slug]['untagged'], 'missing=', out[slug]['missing_in_scan'])
pathlib.Path(sys.argv[1]).write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding='utf-8')
