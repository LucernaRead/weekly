# -*- coding: utf-8 -*-
"""Residual check: list every string literal in the edition build's content
files that still contains Latin letters, so each can be adjudicated as
frozen (brand/team/file/code) or leftover English to translate."""
import ast
import os
import re

BUILD = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-cn-ru-build/'
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'render.py', 'run.py']:
    src = open(BUILD + fn, encoding='utf-8').read()
    print('=====', fn)
    if 'weekly-report-w45-zhcn-core' in src:
        print('  !! STILL REFERENCES CORE DIR')
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            v = node.value
            if re.search(r'[A-Za-z]', v):
                print(f'  L{node.lineno}: {v[:160]!r}')
