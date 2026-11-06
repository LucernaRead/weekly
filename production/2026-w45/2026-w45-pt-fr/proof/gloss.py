import re, glob
def gloss_calls(builddir):
    out = []  # (file, gloss string)
    for f in sorted(glob.glob(builddir + '/content*.py')):
        t = open(f, encoding='utf-8').read()
        for m in re.finditer(r'gloss\((.*?)\)', t, re.S):
            arg = m.group(1)
            # extract string literals
            lits = re.findall(r'"([^"]*)"', arg)
            s = ''.join(lits)
            out.append((f.split('/')[-1], s))
    return out
for label, bd in [('CORE','hidden_files/weekly-report-w45-pt-build'),('ED','hidden_files/weekly-report-w45-pt-fr-build')]:
    calls = gloss_calls(bd)
    print(f"===== {label}: {len(calls)} gloss() calls")
    tot = 0
    for f, s in calls:
        items = [i for i in s.split('·')]
        print(f"  {f}: {len(items)} items :: {s[:120]!r}")
        tot += len(items)
    print(f"  TOTAL items (split on ·): {tot}")
