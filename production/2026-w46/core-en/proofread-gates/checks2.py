#!/usr/bin/env python3
"""Proofreader checks part 2 (read-only)."""
import re, json
from pathlib import Path
from collections import Counter

BASE = Path.home() / 'workspace/goals/lucernaread-social-media-operations/files'
GATE = Path.home() / 'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates'
TEXTS = GATE / 'texts'

def load(ed):
    out = []
    for line in (TEXTS / f'texts-{ed}.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'\[(p\d+-\w+)#(\d+) x=(\S+) y=(\S+) (\S+)pt', line)
        page, idx, x, y, size = m.group(1), int(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5)
        txt = line.split('] ', 1)[1] if '] ' in line else line
        out.append({'page': page, 'idx': idx, 'x': x, 'y': y, 'size': size, 'text': txt})
    return out

print('== P7 golden sentences ON P7 ONLY (core) ==')
gold = [
 "On Wednesday, November 11, at eleven o'clock in the morning, something quiet happens across the English-speaking world.",
 "At 11 a.m. on November 11, 1918, the guns of the First World War fell silent.",
 "For two minutes, nobody speaks.",
 "Christmas is still six weeks away.",
 "One Sunday is not enough — good thing the week has seven days.",
 "The total will still be there in the morning — and so will the kindness.",
 "Patience is part of the system, not a failure of it.",
 "There were no results to print — and this paper invents none.",
]
core = load('core')
p7 = ' '.join(e['text'] for e in core if e['page'].startswith('p7-'))
p7n = re.sub(r'\s+', ' ', p7)
for i, g in enumerate(gold, 1):
    print(i, 'ON-P7' if g in p7n else 'NOT-ON-P7', g[:50])

print('\n== P1 SEARCHES bars (rect widths in searches box x>=1470) ==')
RECT_RE = re.compile(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)"[^>]*fill="([^"]*)"')
for ed in ['core', 'de', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh-tw']:
    svg = (BASE / f'weekly-report-w46-en-{ed}/svg/p1-front.svg').read_text(encoding='utf-8', errors='replace')
    bars = []
    for m in RECT_RE.finditer(svg):
        x, y, w, h, fill = float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)), m.group(5)
        # searches bars: right column, olive/tan fills, height ~18-24, width 40-400
        if x >= 1470 and 600 <= y <= 1250 and 30 <= w <= 420 and 10 <= h <= 30:
            bars.append((round(y), round(w), fill))
    bars.sort()
    print(ed, bars)

print('\n== IMAGE CREDITS present in SVG texts ==')
credits = ['Claude Monet', 'Horace Nicholls', 'John Leech', 'Frank R. Snyder', 'Kenneth C. Zirkel']
for ed in ['core', 'de', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh-tw']:
    ts = load(ed)
    allt = ' '.join(e['text'] for e in ts)
    print(ed, {c: (c in allt) for c in credits})

print('\n== SCRIPT SCANS (char counts in all SVG texts) ==')
def script_counts(s):
    c = Counter()
    for ch in s:
        o = ord(ch)
        if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf': c['Han'] += 1
        elif '\u3040' <= ch <= '\u309f': c['Hiragana'] += 1
        elif '\u30a0' <= ch <= '\u30ff': c['Katakana'] += 1
        elif '\uac00' <= ch <= '\ud7a3': c['Hangul'] += 1
        elif '\u0400' <= ch <= '\u04ff': c['Cyrillic'] += 1
    return dict(c)
for ed in ['core', 'de', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh-tw']:
    allt = ' '.join(e['text'] for e in load(ed))
    print(ed, script_counts(allt))

print('\n== SC-ONLY chars in zh-tw texts (curated set) ==')
SC_ONLY = set('让认说的话读发国会个对时电这为讲译练习读过达运连远还进远边长门问间实应头发关并没这与将让认说这为读发国会个对话语认时电让说这为读发国会个对话语认时电')
# use a standard simplified-only list (chars with no TC equivalent form)
SC_ONLY = set(list('让认说话读发国会个对时电这为讲译练过达运连远还进边长门问间实应头关并没与将让认说读发国会个对话语认时电让说这为读发国会个对话语认时电') + ['让','认','说','话','读','发','国','会','个','对','时','电','这','为','讲','译','练','过','达','运','连','远','还','进','边','长','门','问','间','实','应','头','关','并','没','与','将','从','众','义','习','卫','双','发','变','头','买','卖','乐','东','业','丝','专','传','伤','体','余','作','侧','侨','俭','仓','仪','们','优','会','传','伤','伦','伟','传','伤','伦','伟','伪','伞','众','优','会'])
zhtw = ' '.join(e['text'] for e in load('zh-tw'))
hits = Counter(ch for ch in zhtw if ch in SC_ONLY)
print('zh-tw SC-only hits:', dict(hits))
# show contexts
for e in load('zh-tw'):
    bad = [ch for ch in e['text'] if ch in SC_ONLY]
    if bad:
        print(' ', e['page'], repr(e['text'][:120]), 'chars:', bad)
print('== Han chars in ko texts (expect 0) ==')
ko = load('ko')
for e in ko:
    han = [ch for ch in e['text'] if '\u4e00' <= ch <= '\u9fff']
    if han:
        print(' ', e['page'], repr(e['text'][:120]), han)

print('\n== KINSOKU scan: line-start closers / line-end openers (ja, zh-tw, core) ==')
CLOSERS = set('。、，．,）〕］｝》」』’”!！?？:：;；')
OPENERS = set('（〔［｛《「『‘“(')
for ed in ['ja', 'zh-tw', 'core']:
    print('--', ed)
    for e in load(ed):
        t = e['text']
        if not t: continue
        if t[0] in CLOSERS and t[0] not in '.,':
            print('  START-CLOSER', e['page'], repr(t[:60]))
        if t[-1] in OPENERS:
            print('  END-OPENER', e['page'], repr(t[-60:]))
