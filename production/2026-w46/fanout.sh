#!/bin/bash
# fanout.sh <lang> <CODE> — copy core build, repoint, translate, run, render.
# Usage: fanout.sh de DE   (edition dir files/weekly-report-w46-zh-cn-de/)
set -e
LANG=$1; CODE=$2
G=~/workspace/goals/lucernaread-social-media-operations
SRC=$G/hidden_files/weekly-report-w46-zhcn-build
DST=$G/hidden_files/weekly-report-w46-zh-cn-$LANG-build
ED=$G/files/weekly-report-w46-zh-cn-$LANG
if [ -d "$DST" ]; then echo "DST EXISTS: $DST — refusing to overwrite"; exit 1; fi
cp -r "$SRC" "$DST"
mkdir -p "$ED/svg"
cd "$DST"
sed -i "s/weekly-report-w46-zh-cn-core/weekly-report-w46-zh-cn-$LANG/g" content12.py content34.py content56.py content7.py content8.py render.py
sed -i "s/Lucerna-VOL3\.pdf/Lucerna-VOL3-$CODE.pdf/" render.py
if [ "$LANG" = "ja" ]; then
  python3 - << 'PY'
# W45 precedent: small kana must not start a line (build-copy svglib only)
p = "svglib.py"
src = open(p, encoding="utf-8").read()
anchor = 'NO_START = "'
i = src.index(anchor)
j = src.index("\n", i)
linestart = src.rindex("\n", 0, i) + 1
indent = src[linestart:i]
src = src[:j] + "\n" + indent + 'NO_START += "ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ"  # W46 zh-cn x ja: small kana (W45 precedent)' + src[j:]
open(p, "w", encoding="utf-8").write(src)
print("ja NO_START extended")
PY
fi
python3 ../w46/coverage.py ../w46/maps/$LANG.json
python3 ../w46/transform.py "$DST" ../w46/maps/$LANG.json > ../w46/transform-$LANG.log 2>&1 || { tail -n 20 ../w46/transform-$LANG.log; exit 1; }
tail -n 2 ../w46/transform-$LANG.log
../../tools/venv/bin/python run.py 2>&1 | grep -E "saved|TOTAL|levels|writing|OVERFLOW|TOO WIDE"
../../tools/venv/bin/python render.py 2>&1 | tail -n 3
echo "FANOUT BUILD DONE: $LANG ($CODE) -> $ED"
