# -*- coding: utf-8 -*-
"""Adapt gates_core.py into a per-edition gates.py.

Usage: adapt_gates.py <build-dir> <edition-dir-name> <footer> <pageline-fmt>
  <badge-substring> <disc-string> <label-substring> <disc-check-name> <cjk-mode>
pageline-fmt: python f-string body with {i} for the page number, e.g.
  "Page {i} of 8". cjk-mode: 'zero' (no CJK allowed in render) or 'skip'.
The disc-string/label are checked verbatim in the P7 joined text; for CJK
reader languages the check uses the space-stripped comparison like the core.
"""
import sys

build_dir, ed_name, footer, pageline, badge, disc, label, disc_name, cjk_mode = sys.argv[1:10]
core = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-pt-build/gates_core.py'
t = open(core, encoding='utf-8').read()
t = t.replace('"""Builder self-check for W46 PT core (zh-cn explanations). Adapted from the\nW45 PT x EN gates.py: ink boxes via PIL getbbox anchor=\'ls\'."""',
              f'"""Builder self-check for W46 PT x {ed_name.split("-")[-1].upper()} (VOL.3)."""')
t = t.replace('ED = os.path.join(GOAL, "weekly-report-w46-pt-core")', f'ED = os.path.join(GOAL, "{ed_name}")')
t = t.replace("check('P1 subtitle topics', 'ENEM, DIA 2' in p1 and 'PROCLAMAÇÃO DA REPÚBLICA' in p1, 'subtitle line')",
              "check('P1 subtitle topics', 'ENEM, DIA 2' in p1 and 'PROCLAMAÇÃO DA REPÚBLICA' in p1, 'subtitle line')\n"
              f"check('P1 pairing badge', {badge!r} in p1, 'badge line 372')")
import re as _re
_pat = _re.compile(r"if 'A Lucerna[^']*' not in j or f'[^']*' not in j:")
_new = f"if {footer!r} not in j or f'{pageline.replace('{total}', '8')}' not in j:"
t, _n = _pat.subn(_new, t)
assert _n == 1, 'footer line not replaced'
t = t.replace("'VOL.3 ZH footer + page line on all pages'", "'VOL.3 footer + page line on all pages'")
t = t.replace("missing = [it.split()[0] for pg, its in gc.items() for it in its if it.split()[0].rstrip('.') not in allj]",
              "missing = [it for pg, its in gc.items() for it in its if it.split('=')[0].strip() not in allj]")
t = t.replace("check('P7 quotes 2x + page tag + ZH on P7', qok,", "check('P7 quotes 2x + page tag + reader lang on P7', qok,")

old_disc = """disc_cn = '编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。'
p7nospace = re.sub(r'\\s+', '', p7j)
checks = {
    'PT example verbatim': lt in p7j,
    'PT disclosure verbatim': disc_pt in p7j,
    'ZH disclosure verbatim': re.sub(r'\\s+', '', disc_cn) in p7nospace,
    'ZH example label': '编辑部示例，非真实来信' in p7nospace,
    'VOL.4 carry': 'VOL.4' in p7j,
}"""
if cjk_mode == 'zero':
    new_disc = f"""disc_rl = {disc!r}
checks = {{
    'PT example verbatim': lt in p7j,
    'PT disclosure verbatim': disc_pt in p7j,
    {disc_name!r}: disc_rl in p7j,
    'reader example label': {label!r} in p7j,
    'VOL.4 carry': 'VOL.4' in p7j,
}}"""
else:
    new_disc = f"""disc_rl = {disc!r}
p7nospace = re.sub(r'\\s+', '', p7j)
checks = {{
    'PT example verbatim': lt in p7j,
    'PT disclosure verbatim': disc_pt in p7j,
    {disc_name!r}: re.sub(r'\\s+', '', disc_rl) in p7nospace,
    'reader example label': re.sub(r'\\s+', '', {label!r}) in p7nospace,
    'VOL.4 carry': 'VOL.4' in p7j,
}}"""
assert old_disc in t, 'disc block not found in gates_core.py'
t = t.replace(old_disc, new_disc)
if cjk_mode == 'zero':
    marker = "print('FAILURES:', fails if fails else 'none')"
    t = t.replace(marker, "check('no CJK residue in edition', not re.findall(r'[\\u4e00-\\u9fff]', allj), 'explanation layer fully translated')\n" + marker)
open(f'{build_dir}/gates.py', 'w', encoding='utf-8').write(t)
print('gates.py written for', ed_name)
