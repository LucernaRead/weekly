#!/bin/bash
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
GATE=$ROOT/hidden_files/w46/zh-cn-proofread-gates-round3
RB=$GATE/rebuild-pre
PY=$ROOT/tools/venv/bin/python
mkdir -p "$RB"
# hash guard: shipped edition hashes before
find $ROOT/files/weekly-report-w46-zh-cn-core $ROOT/files/weekly-report-w46-zh-cn-de $ROOT/files/weekly-report-w46-zh-cn-es $ROOT/files/weekly-report-w46-zh-cn-fr $ROOT/files/weekly-report-w46-zh-cn-it $ROOT/files/weekly-report-w46-zh-cn-ja $ROOT/files/weekly-report-w46-zh-cn-ko $ROOT/files/weekly-report-w46-zh-cn-nl $ROOT/files/weekly-report-w46-zh-cn-pt $ROOT/files/weekly-report-w46-zh-cn-ru -type f | sort | xargs sha256sum > "$GATE/rebuild-guard-before.txt"
declare -A BUILD=( [en]=weekly-report-w46-zhcn-build [de]=weekly-report-w46-zh-cn-de-build [es]=weekly-report-w46-zh-cn-es-build [fr]=weekly-report-w46-zh-cn-fr-build [it]=weekly-report-w46-zh-cn-it-build [ja]=weekly-report-w46-zh-cn-ja-build [ko]=weekly-report-w46-zh-cn-ko-build [nl]=weekly-report-w46-zh-cn-nl-build [pt]=weekly-report-w46-zh-cn-pt-build [ru]=weekly-report-w46-zh-cn-ru-build )
for lang in en de es fr it ja ko nl pt ru; do
  echo "===== rebuild $lang ====="
  SRC=$ROOT/hidden_files/${BUILD[$lang]}
  DST=$RB/$lang-build
  rm -rf "$DST"; cp -r "$SRC" "$DST"
  mkdir -p "$RB/$lang/svg"
  # redirect OUT in content*.py to rebuild svg dir; revert stem in content7.py only
  python3 - "$DST" "$RB/$lang/svg" <<'PYEOF'
import glob, sys, os
dst, outdir = sys.argv[1], sys.argv[2]
for f in glob.glob(os.path.join(dst, "content*.py")):
    s = open(f, encoding="utf-8").read()
    import re
    s2 = re.sub(r'OUT = os\.path\.expanduser\("[^"]+"\)', 'OUT = '+repr(outdir), s)
    if s2 == s:
        print("WARN no OUT rewrite in", f)
    open(f, "w", encoding="utf-8").write(s2)
c7 = os.path.join(dst, "content7.py")
s = open(c7, encoding="utf-8").read()
assert s.count("我拿了___包裹。") == 1, s.count("我拿了___包裹。")
s = s.replace("我拿了___包裹。", "我拿了一个___包裹。")
open(c7, "w", encoding="utf-8").write(s)
print("reverted stem in", c7)
PYEOF
  (cd "$DST" && $PY run.py > "$GATE/rebuild-pre-$lang-run.log" 2>&1; echo "run exit=$?" >> "$GATE/rebuild-pre-$lang-run.log")
  tail -n 8 "$GATE/rebuild-pre-$lang-run.log"
  ls "$RB/$lang/svg" | wc -l
done
find $ROOT/files/weekly-report-w46-zh-cn-core $ROOT/files/weekly-report-w46-zh-cn-de $ROOT/files/weekly-report-w46-zh-cn-es $ROOT/files/weekly-report-w46-zh-cn-fr $ROOT/files/weekly-report-w46-zh-cn-it $ROOT/files/weekly-report-w46-zh-cn-ja $ROOT/files/weekly-report-w46-zh-cn-ko $ROOT/files/weekly-report-w46-zh-cn-nl $ROOT/files/weekly-report-w46-zh-cn-pt $ROOT/files/weekly-report-w46-zh-cn-ru -type f | sort | xargs sha256sum > "$GATE/rebuild-guard-after.txt"
diff "$GATE/rebuild-guard-before.txt" "$GATE/rebuild-guard-after.txt" && echo "GUARD: shipped files UNCHANGED during rebuild"
echo "REBUILD ALL DONE"
