# -*- coding: utf-8 -*-
"""W46 ES x ZH-CN transform.

ZH-CN is the core's own explanation language (Simplified Chinese). This
edition is a DISTINCT edition dir with its own pairing badge, pairing
footer and P8 separator, built from the fixed core build. No explanation
text changes: the core text is already Simplified Chinese. build_one.py
reads PAIRS (+PAIRS2) from this module and applies them to the copied
core build; the BUILD/main() below are unused by the driver.
"""
PAIRS = [
    # pairing badge: replace the y=372 subtitle slot (ZH-TW pattern, Simplified form)
    ('p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "西班牙语正文 · 简体中文讲解 — 给简体中文读者的版本", 19.5, "sans", True, BRICK, anchor="middle")', ["content12.py"]),
    # pairing footer (bslib4 foot()): core footer names the English weekly; ZH-CN names the pairing
    ('La Lucerna · 西班牙语周报 VOL.3 · LUCERNA SPANISH WEEKLY',
     'La Lucerna · 西班牙语周报 VOL.3 · 正文西班牙语 · 讲解简体中文', ["bslib4.py"]),
    # P8 separator (ZH-TW pattern, Simplified form)
    ('af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
     'af.para(f"— 第 {pg} 版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', ["content8.py"]),
    # PDF filenames in render.py (suffixed, fan-out convention)
    ('La-Lucerna-VOL3.pdf', 'La-Lucerna-VOL3-ZH-CN.pdf', ["render.py"]),
    ('La-Lucerna-VOL3-web.pdf', 'La-Lucerna-VOL3-ZH-CN-web.pdf', ["render.py"]),
    # edition dir name in render.py
    ('weekly-report-w46-es-core', 'weekly-report-w46-es-zh-cn',
     ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "render.py"]),
]
PAIRS2 = []
