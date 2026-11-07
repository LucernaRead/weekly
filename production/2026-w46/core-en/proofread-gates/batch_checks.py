#!/usr/bin/env python3
"""Proofreader batch checks (read-only). Prints a checks log."""
import json, re, subprocess, unicodedata
from pathlib import Path
from collections import Counter

BASE = Path.home() / 'workspace/goals/lucernaread-social-media-operations/files'
GATE = Path.home() / 'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates'
TEXTS = GATE / 'texts'

def load_texts(ed):
    out = []
    for line in (TEXTS / f'texts-{ed}.txt').read_text(encoding='utf-8').splitlines():
        m = re.match(r'\[(p\d+-\w+)#\d+ x=(\S+) y=(\S+) (\S+)pt', line)
        page = m.group(1) if m else '?'
        txt = line.split('] ', 1)[1] if '] ' in line else line
        out.append((page, txt))
    return out

print('== REGISTRY ==')
reg = json.load(open(Path.home() / 'workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-core/registry.json'))
print(type(reg), len(reg) if isinstance(reg, (list, dict)) else '')
if isinstance(reg, dict):
    items = reg.get('exercises') or reg.get('registry') or reg
    print('keys:', list(reg.keys())[:10])
    seq = items if isinstance(items, list) else None
else:
    seq = reg
if seq:
    nums = [e.get('n', e.get('num', e.get('id'))) for e in seq]
    print('count', len(seq), 'nums min/max', min(nums), max(nums), 'unique', len(set(nums)),
          'missing', sorted(set(range(1, 151)) - set(nums)), 'dup', [n for n, c in Counter(nums).items() if c > 1])
    lv = Counter(e.get('level', e.get('lvl')) for e in seq)
    print('levels', dict(lv))
    perpage = Counter(e.get('page', e.get('p')) for e in seq)
    print('per-page', dict(sorted(perpage.items(), key=lambda kv: str(kv[0]))))
    # keys present?
    nokey = [e for e in seq if not e.get('key', e.get('answer'))]
    print('entries without key/answer field:', len(nokey), [e.get('n') for e in nokey[:10]])
    print('sample entry:', json.dumps(seq[0], ensure_ascii=False)[:400])

print('\n== P7 GOLDEN SENTENCES (core KIT list) ==')
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
core_all = ' '.join(t for _, t in load_texts('core'))
core_norm = re.sub(r'\s+', ' ', core_all)
for i, g in enumerate(gold, 1):
    # wrapped lines: join with space and collapse; also try joining without space for hyphen breaks
    found = g in core_norm
    print(i, 'VERBATIM' if found else 'NOT-FOUND', g[:60])
    if not found:
        frag = g[:40]
        print('   frag present:', frag in core_norm)

print('\n== PDF / ABSTRACT ==')
for eddir in sorted(BASE.glob('weekly-report-w46-en-*')):
    ed = eddir.name.replace('weekly-report-w46-en-', '')
    web = eddir / 'The-Lucerna-VOL3-web.pdf'
    prn = eddir / 'The-Lucerna-VOL3.pdf'
    ab = (eddir / 'ABSTRACT.txt').read_text(encoding='utf-8')
    for pdf, name in [(web, 'web'), (prn, 'print')]:
        r = subprocess.run(['pdftotext', str(pdf), '-'], capture_output=True)
        print(ed, name, 'bytes', pdf.stat().st_size, 'pdftotext-bytes', len(r.stdout),
              'pages?', subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout.splitlines()[4] if True else '')
    print(ed, 'ABSTRACT lines', ab.count('\n'), 'chars', len(ab.strip()), 'has-ASCII-dquote', ('"' in ab),
          'single-line', ab.strip().count('\n') == 0)

print('\n== BADGE / FOOTER (KIT furniture strings) ==')
KIT_FURN = {
 'de': ("ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER",
        "The Lucerna · ENGLISH WEEKLY VOL.3 · Englischer Text · Deutsche Erklärungen"),
 'es': ("TEXTOS EN INGLÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES",
        "The Lucerna · SEMANARIO INGLÉS VOL.3 · TEXTO EN INGLÉS · EXPLICACIONES EN ESPAÑOL"),
 'fr': ("TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES",
        "The Lucerna · HEBDOMADAIRE ANGLAIS VOL.3 · TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS"),
 'it': ("TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI",
        "The Lucerna · SETTIMANALE INGLESE VOL.3 · TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO"),
 'ja': ("英語テキスト · 日本語の解説 — 日本語読者のための版",
        "The Lucerna · 英語週刊 VOL.3 · 本文は英語 · 解説は日本語"),
 'ko': ("영어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판",
        "The Lucerna · 영어 주간지 VOL.3 · 텍스트는 영어 · 해설은 한국어"),
 'nl': ("TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS",
        "The Lucerna · ENGELS WEEKBLAD VOL.3 · TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS"),
 'pt': ("TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA",
        "The Lucerna · SEMANÁRIO INGLÊS VOL.3 · TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS"),
 'ru': ("ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ",
        "The Lucerna · АНГЛИЙСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА АНГЛИЙСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ"),
 'zh-tw': ("英語正文 · 繁體中文講解 — 給繁體中文讀者的版本",
        "The Lucerna · 英語週報 VOL.3 · 正文英語 · 講解繁體中文"),
 'core': (None, "The Lucerna · 英语周报 VOL.3 · LUCERNA ENGLISH WEEKLY"),
}
for ed, (badge, footer) in KIT_FURN.items():
    ts = load_texts(ed)
    p1 = [t for p, t in ts if p.startswith('p1-')]
    all_t = [t for _, t in ts]
    if badge:
        print(ed, 'badge-in-P1:', any(badge in t for t in p1), '| badge-anywhere:', any(badge in t for t in all_t))
    print(ed, 'footer-present:', sum(1 for t in all_t if footer in t), '(expect 8 pages)')
    # footer variants actually present
    foots = sorted(set(t for t in all_t if 'Lucerna ·' in t and ('VOL.3' in t)))
    for f in foots:
        print('   FOOT:', f)

print('\n== MASTHEAD LINES (P1) ==')
for ed in ['core', 'de', 'es', 'fr', 'it', 'ja', 'ko', 'nl', 'pt', 'ru', 'zh-tw']:
    ts = load_texts(ed)
    for p, t in ts:
        if p.startswith('p1-') and 'VOL.3 ·' in t and ('·' in t) and len(t) > 20 and 'Lucerna' not in t and 'WEEK' not in t:
            print(ed, repr(t))
