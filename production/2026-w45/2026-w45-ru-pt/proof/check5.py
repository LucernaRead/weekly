import re, glob
for label,base in [("ED","/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-pt-build"),
                   ("CORE","/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-build")]:
    print(f"===== {label} gloss() calls =====")
    total=0
    for f in sorted(glob.glob(base+"/content*.py")):
        src=open(f,encoding='utf-8').read()
        # find gloss( ... ) balanced-ish: gloss calls span until '")' ? print raw call snippets
        for m in re.finditer(r'gloss\((.*?)\)\s*(?:,|\n)', src, re.S):
            arg=m.group(1)
            # items split on · itself per README21
            items=[s.strip() for s in arg.split('·')]
            print(f"  {f.split('/')[-1]}: n_items={len(items)} :: {arg[:160]!r}")
            total+=len(items)
    print(f"  TOTAL items={total}")
