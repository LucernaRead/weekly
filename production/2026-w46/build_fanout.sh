#!/bin/bash
# Fan-out builder for W46 FR family. Usage:
#   build_fanout.sh <native> <expl.py path>
# Creates build dir from the FROZEN core build dir, repoints OUT paths,
# renders, and runs p8 compare + occlusion audit + freeze diff.
# Never touches the core build dir or W45 dirs.
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
NATIVE=$1
EXPL_SRC=$2
BUILD=$ROOT/hidden_files/weekly-report-w46-fr-${NATIVE}-build
ED=$ROOT/files/weekly-report-w46-fr-${NATIVE}
CORE_BUILD=$ROOT/hidden_files/weekly-report-w46-fr-build
CORE_SVG=$ROOT/files/weekly-report-w46-fr-core/svg

if [ -d "$BUILD" ]; then rm -rf "$BUILD"; fi
cp -r "$CORE_BUILD" "$BUILD"
rm -rf "$BUILD/__pycache__"
cp "$EXPL_SRC" "$BUILD/expl.py"
mkdir -p "$ED/svg"
# Repoint OUT paths (content files only) to this edition's svg dir
sed -i "s|weekly-report-w46-fr-core/svg|weekly-report-w46-fr-${NATIVE}/svg|g" "$BUILD"/content*.py
grep -h "OUT = " "$BUILD"/content*.py | head -5
cd "$BUILD"
$ROOT/tools/venv/bin/python -c "import content12, content34, content56, content7, content8" 2>&1 | grep -E "OVERFLOW|TOO WIDE|TOTAL|saved" ; echo "RENDER EXIT:$?"
echo "=== p8 compare ==="
$ROOT/tools/venv/bin/python $ROOT/tools/p8.py compare --core-p8 "$CORE_SVG/p8-exercices.svg" --edition-p8 "$ED/svg/p8-exercices.svg" --total 150 2>&1 | tail -6
echo "=== occlusion ==="
$ROOT/tools/venv/bin/python $ROOT/tools/occlusion_audit.py "$ED/svg" 2>&1 | tail -4
echo "=== freeze diff ==="
$ROOT/tools/venv/bin/python $ROOT/tools/freeze.py diff --core-svg "$CORE_SVG" --edition-svg "$ED/svg" 2>&1 | tail -30
