# -*- coding: utf-8 -*-
"""Adapt gates_core.py into per-edition gates.py.
Usage: tools/venv/bin/python make_gates.py <edition_dir> <lang>
Reads furniture.py FURN[lang]: footer_joined, page_fmt, disc_var,
disc_text, label_nospace, lang_name (for check labels).
"""
import os, sys, importlib
ED, LANG = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
F = importlib.import_module("furniture").FURN[LANG]
src = open(os.path.join(ED, 'gates_core.py'), encoding='utf-8').read()

def rep(old, new):
    global src
    assert old in src, f'missing: {old[:70]!r}'
    src = src.replace(old, new)

rep("'A Lucerna 葡萄牙语周报 VOL.4 LUCERNA PORTUGUESE WEEKLY'",
    "'" + F['footer_joined'] + "'")
rep("f'第{i}版／共8版'", "f'" + F['page_fmt'] + "'")
rep("'VOL.4 ZH footer + page line on all pages'",
    "'VOL.4 " + F['lang_name'] + " footer + page line on all pages'")
rep("'P7 quotes 2x + page tag + ZH on P7'",
    "'P7 quotes 2x + page tag + " + F['lang_name'] + " on P7'")
# disclosure variable + checks
# NB 2026-11-11 (ko): transform.py step 5 converts 。->. and ：->: in the
# rendered build sources, so the gates' expected disclosure must carry the
# SAME conversion — otherwise the verbatim check compares "。" against the
# rendered "." and fails. (ja/zh-tw have PUNCT={} so no conversion applies.)
disc_text = F['disc_text']
if LANG == 'ko':
    disc_text = disc_text.replace('。', '.').replace('：', ':')
old_disc = "disc_cn = '编辑部说明：上期（VOL.3）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.5）。'"
rep(old_disc, F['disc_var'] + ' = "' + disc_text + '"')
assert '"' not in disc_text, 'disc_text must not contain ASCII double quotes'
src = src.replace('disc_cn', F['disc_var'])
rep("'ZH disclosure verbatim'", "'" + F['lang_name'] + " disclosure verbatim'")
rep("'ZH example label'", "'" + F['lang_name'] + " example label'")
rep("'编辑部示例，非真实来信'", '"' + F['label_nospace'] + '"')
open(os.path.join(ED, 'gates.py'), 'w', encoding='utf-8').write(src)
print('gates.py written for', LANG)
