# -*- coding: utf-8 -*-
"""W47 PT fan-out transform — generic driver.

Usage (run once, on a fresh copy of core-pt):
  tools/venv/bin/python transform.py <edition_dir> <lang>
Reads tables_<lang>.py from the same directory as this script
(scratch-fanout-pt), which defines SEG and OVR dicts, plus FURN in
furniture.py (footer / page line / gloss prefix / badge / subtitle /
disc variable / model-text lines).

Steps (W46 transform precedent):
  0. bslib4 furniture (footer line, page-line f-string, gloss prefix).
  1. P1 masthead lines 330 (subtitle) + 372 (badge) whole-line replace.
  2. content8 f-string subs: model bridge + model note.
  3. content7 disc_cn -> disc_<lang>.
  4. OVR (longest first) then SEG (longest first) on bslib4 + content*.py.
  5. Latin-script editions (en/de/fr/es/it/nl/ru): fullwidth punctuation
     -> ASCII (。、，；：（）！), matching W46 S5c (fullwidth colon fix).
     CJK editions (ja/ko/zh-tw): keep native punctuation; ko converts
     。->. and ：->: only (W46 ko precedent — verify in review).
  6. Verify: Latin/ru editions must have ZERO CJK chars in build sources;
     CJK editions must have zero SIMPLIFIED-only chars (checked separately).
Frozen Portuguese text, P7 example letter, PT disclosure and P7 quote
strings + page tags are never touched (they contain no CJK).
"""
import os, re, sys, importlib

ED = sys.argv[1]
LANG = sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
tables = importlib.import_module("tables_" + LANG)
FURN = importlib.import_module("furniture").FURN[LANG]
SEG, OVR = tables.SEG, tables.OVR

CJK = re.compile(r'[\u4e00-\u9fff]')

def load(fn):
    with open(os.path.join(ED, fn), encoding='utf-8') as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(ED, fn), 'w', encoding='utf-8') as f:
        f.write(txt)

def sub(txt, old, new, fn=''):
    n = txt.count(old)
    assert n >= 1, f'{fn}: {old!r} not found'
    return txt.replace(old, new)

def line_replace(txt, anchor, newline, fn=''):
    lines = txt.split('\n')
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == 1, f'{fn}: anchor {anchor!r} hits {hits}'
    lines[hits[0]] = newline
    return '\n'.join(lines)

FILES = ['bslib4.py', 'content12.py', 'content34.py', 'content56.py',
         'content7.py', 'content8.py']

# ---------- 0. bslib4 furniture ----------
t = load('bslib4.py')
t = line_replace(t, 'A Lucerna\u3000葡萄牙语周报',
    '        self.text(MX, 2624, "A Lucerna\u3000' + FURN["footer"] + '", 17, "sans", False, GREY)',
    'bslib4.py')
t = sub(t, 'f"第{n}版／共{total}版"', FURN['page_line'], 'bslib4.py')
t = sub(t, '("译注｜" + s', '("' + FURN["gloss"] + '" + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 1. P1 masthead lines ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "' + FURN["sub330"] + '", ' + str(FURN["sub330_size"]) + ', "serif", True, OLIVE, anchor="middle", spacing=0)',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "' + FURN["badge372"] + '", 16, "sans", False, GREY, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 2b. P8 answer-key size (W46 precedent: EN notes are longer
# than the Chinese notes, so the keys flow overflows at 13.5/1.16) ----------
if FURN.get("p8_keys_small"):
    t = load('content8.py')
    t = line_replace(t, 'af.para(txt, 13.5',
        '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
        'content8.py')
    save('content8.py', t)

# ---------- 2. content8 f-string subs ----------
t = load('content8.py')
t = sub(t, 'f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。"',
        'f"' + FURN["model_bridge"] + '"', 'content8.py')
t = sub(t, 'f"范文见本版 H 区（{NWORDS} 词）"',
        'f"' + FURN["model_note"] + '"', 'content8.py')
save('content8.py', t)

# ---------- 3. content7 disc rename ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', FURN['disc_var'])
save('content7.py', t)

# ---------- 3b. P7 geometry (reader languages with longer notes) ----------
if FURN.get("p7_geo"):
    g = FURN["p7_geo"]
    t = load('content7.py')
    for old, new in [
        (")) * 29 + 35", f")) * 29 + {g['letters_pad']}"),
        ("ly + lh + 36", f"ly + lh + {g['fy_gap']}"),
        ("(i % 4) * 96", f"(i % 4) * {g['quote_step']}"),
    ]:
        assert t.count(old) == 1, f'content7.py p7_geo {old!r} count {t.count(old)}'
        t = t.replace(old, new)
    save('content7.py', t)

# ---------- 4. OVR then SEG ----------
found_ovr = set()
for fn in FILES:
    t = load(fn)
    for old, new in sorted(OVR.items(), key=lambda kv: -len(kv[0])):
        if old in t:
            t = t.replace(old, new)
            found_ovr.add(old)
    for old, new in sorted(SEG.items(), key=lambda kv: -len(kv[0])):
        if old in t:
            t = t.replace(old, new)
    save(fn, t)
missing_ovr = sorted(set(OVR) - found_ovr)
if missing_ovr:
    print(f'WARN OVR not found in any file ({len(missing_ovr)}):')
    for old in missing_ovr:
        print(f'  MISSING OVR: {old[:80]!r}')

# ---------- 5. punctuation ----------
if LANG in ('en', 'de', 'fr', 'es', 'it', 'nl', 'ru'):
    PUNCT = {'。': '.', '，': ', ', '、': ', ', '；': '; ', '：': ':',
             '（': '(', '）': ')', '！': '!', '？': '?'}
elif LANG == 'ko':
    # D6 (proof-pt-ko1): Korean needs a space after ':'; the Chinese source
    # has none, so '：' -> ': ' when followed by a non-space char (the 11
    # SEG values ending in '：' and the source-inline '：' alike).
    # D8 (proof-pt-ko1): '，' -> ',' (was unconverted, left fullwidth).
    PUNCT = {'。': '.', '，': ','}
else:
    PUNCT = {}
for fn in FILES:
    t = load(fn)
    for old, new in PUNCT.items():
        if old in t:
            t = t.replace(old, new)
    if LANG == 'ko':
        t = re.sub(r'：(?=\S)', ': ', t)
    save(fn, t)

# ---------- 6. verify ----------
if LANG in ('en', 'de', 'fr', 'es', 'it', 'nl', 'ru'):
    bad = {}
    for fn in FILES:
        t = load(fn)
        hits = CJK.findall(t)
        if hits:
            bad[fn] = (len(hits), hits[:10])
    assert not bad, f'CJK remains: {bad}'
    print('CJK 0 OK in all build sources')
print('TRANSFORM COMPLETE', LANG, ED)
