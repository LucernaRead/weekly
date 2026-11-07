# -*- coding: utf-8 -*-
"""Gate 0 independent verification of tools/occlusion_audit.py _path_points.
No builder outputs are trusted: every case is recomputed here."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA

def bbox(pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))

cases = [
    # (name, d, expected points or bbox)
    ("JA frost rel M/l", "M451.0 2022.0 l20.0 -14.0 M451.0 2022.0 l20.0 14.0 M571.0 2022.0 l-20.0 -14.0 M571.0 2022.0 l-20.0 14.0",
     [(451,2022),(471,2008),(451,2022),(471,2036),(571,2022),(551,2008),(571,2022),(551,2036)]),
    ("core frost abs M/L", "M451.0 2022.0 L471.0 2008.0 M451.0 2022.0 L471.0 2036.0 M571.0 2022.0 L551.0 2008.0 M571.0 2022.0 L551.0 2036.0",
     [(451,2022),(471,2008),(451,2022),(471,2036),(571,2022),(551,2008),(571,2022),(551,2036)]),
    ("implicit lineto after M", "M10 10 20 20 30 10", [(10,10),(20,20),(30,10)]),
    ("implicit lineto after rel m", "m100 100 10 0 0 10", [(100,100),(110,100),(110,110)]),
    ("H/V abs", "M10 20 H50 V60 h-10 v-10", [(10,20),(50,20),(50,60),(40,60),(40,50)]),
    ("H/V rel", "M10 20 h30 v40", [(10,20),(40,20),(40,60)]),
    ("C abs incl ctrl pts", "M0 0 C10 0 20 10 30 10", [(0,0),(10,0),(20,10),(30,10)]),
    ("C rel incl ctrl pts", "M100 100 c10 0 20 10 30 10", [(100,100),(110,100),(120,110),(130,110)]),
    ("S/Q rel", "M0 0 s10 10 20 0 q5 5 10 0", [(0,0),(10,10),(20,0),(25,5),(30,0)]),
    ("T rel", "M0 0 t10 10 t10 -10", [(0,0),(10,10),(20,0)]),
    ("A endpoint", "M0 0 A10 10 0 0 1 40 30", [(0,0),(40,30)]),
    ("A rel endpoint", "M100 100 a10 10 0 0 1 40 30", [(100,100),(140,130)]),
    ("Z reset", "M10 10 L20 20 Z L30 30", [(10,10),(20,20),(30,30)]),
    ("comma/sign separators", "M10,20l20-14,30,40", [(10,20),(30,6),(60,46)]),
    ("sign-sep decimals", "M10.5 20.5l.5-.5", [(10.5,20.5),(11.0,20.0)]),
    ("multiple subpaths M reset", "M0 0 L10 0 M100 100 L110 100", [(0,0),(10,0),(100,100),(110,100)]),
]
fails = 0
for name, d, exp in cases:
    got = OA._path_points(d)
    ok = len(got) == len(exp) and all(abs(a-c) < 1e-9 and abs(b-dd) < 1e-9 for (a,b),(c,dd) in zip(got, exp))
    print(("PASS " if ok else "FAIL ") + name + " got=" + str(got))
    if not ok: fails += 1

ja = OA._path_points(cases[0][1]); core = OA._path_points(cases[1][1])
print("JA frost bbox:", bbox(ja), "core frost bbox:", bbox(core), "EQUAL:", bbox(ja) == bbox(core) == (451,2008,571,2036))
print("OLD buggy alternating-pair bbox of JA frost numbers would be (-20,-14,571,2022): check old logic:")
nums = OA._PATH_NUM.findall(cases[0][1])
pairs = [(float(nums[i]), float(nums[i+1])) for i in range(0, len(nums)-1, 2)]
print("  old pairs bbox:", bbox(pairs))
print("FAILS:", fails)
sys.exit(1 if fails else 0)
