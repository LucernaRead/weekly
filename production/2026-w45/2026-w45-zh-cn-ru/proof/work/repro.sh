#!/bin/bash
# Independent reproof Gate 10: fresh core copy + fixed transform alone.
# NEVER touches delivery or real build dirs; OUT repointed to repro-out.
set -u
BASE=~/workspace/goals/lucernaread-social-media-operations
W=$BASE/hidden_files/w45/zh-cn-ru-reproof/work
PY=$BASE/tools/venv/bin/python
rm -rf "$W/repro-build" "$W/repro-out"
cp -r "$BASE/hidden_files/weekly-report-w45-zhcn-build" "$W/repro-build"
rm -rf "$W/repro-build/__pycache__"
mkdir -p "$W/repro-build/scratch" "$W/repro-out"
cp "$BASE/hidden_files/weekly-report-w45-zh-cn-ru-build/scratch/transform_ru_w45.py" "$W/repro-build/scratch/"
cd "$W/repro-build" || exit 1
echo "--- transform run ---"
$PY scratch/transform_ru_w45.py > "$W/repro-transform.log" 2>&1
echo "transform exit: $?"
grep -c "ZERO matches" "$W/repro-transform.log" || true
grep "TRANSFORM OK" "$W/repro-transform.log" || true
# Repoint OUT/BASE away from the real delivered dir to repro-out (all spellings)
$PY - "$W" << 'PYEOF'
import re, sys
W = sys.argv[1]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    p = f
    s = open(p, encoding="utf-8").read()
    s2, n = re.subn(r'^OUT = .*$', 'OUT = "' + W + '/repro-out/svg"', s, count=1, flags=re.M)
    assert n == 1, f
    open(p, "w", encoding="utf-8").write(s2)
s = open("render.py", encoding="utf-8").read()
s2, n = re.subn(r'^BASE = .*$', 'BASE = "' + W + '/repro-out"', s, count=1, flags=re.M)
assert n == 1, "render.py"
open("render.py", "w", encoding="utf-8").write(s2)
print("REPOINT OK")
PYEOF
echo "--- grep for real-dir references (must be empty) ---"
grep -rn "weekly-report-w45-zh-cn-ru\|weekly-report-w45-zhcn-core" content12.py content34.py content56.py content7.py content8.py render.py bslib4.py svglib.py run.py || echo "NO REAL-DIR REFERENCES"
mkdir -p "$W/repro-out"
echo "--- driver run ---"
$PY run.py > "$W/repro-run.log" 2>&1
echo "driver exit: $?"
grep -E "TOTAL|by level|by page|by type|ALL DONE|FLOW OVERFLOW|HEAD TOO WIDE" "$W/repro-run.log"
echo "--- compare repro SVGs to delivered ---"
for f in p1-touiban p2-shenghuo p3-wenhua p4-tiyu p5-qingnian p6-shendu p7-ciyu p8-ceyan; do
  a=$(sha256sum "$W/repro-out/svg/$f.svg" | cut -d' ' -f1)
  b=$(sha256sum "$BASE/files/weekly-report-w45-zh-cn-ru/svg/$f.svg" | cut -d' ' -f1)
  if [ "$a" = "$b" ]; then echo "IDENTICAL $f"; else echo "DIFFER $f repro=$a delivered=$b"; fi
done
echo "--- repro build sources vs real RU build sources (OUT/BASE lines excluded) ---"
for f in content12.py content34.py content56.py content7.py content8.py bslib4.py svglib.py run.py; do
  # strip the OUT/BASE repoint lines for comparison
  grep -v "repro-out" "$W/repro-build/$f" > "$W/cmp-repro-$f" 2>/dev/null || true
  grep -v "weekly-report-w45-zh-cn-ru" "$BASE/hidden_files/weekly-report-w45-zh-cn-ru-build/$f" > "$W/cmp-real-$f" 2>/dev/null || true
  # also strip the core path in real build? real build has ru path; repro has repro-out path; both stripped above
  if cmp -s "$W/cmp-repro-$f" "$W/cmp-real-$f"; then echo "SRC-IDENTICAL $f"; else echo "SRC-DIFF $f"; diff "$W/cmp-real-$f" "$W/cmp-repro-$f" | head -40; fi
done
