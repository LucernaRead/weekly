#!/bin/bash
# Finish a W46 FR fan-out edition: cards + print PDF + web PDF + .text.md + verify.
# Usage: finish_edition.sh <native> <slug> "<text.md header title>" "<text.md header meta>"
set -u
ROOT=~/workspace/goals/lucernaread-social-media-operations
NATIVE=$1; SLUG=$2; TITLE=$3; META=$4
ED=$ROOT/files/weekly-report-w46-fr-${NATIVE}
BUILD=$ROOT/hidden_files/weekly-report-w46-fr-${NATIVE}-build
$ROOT/tools/venv/bin/python - <<EOF
import cairosvg, glob
from pypdf import PdfWriter, PdfReader
base = "$ED"
import os
os.makedirs(f'{base}/cards', exist_ok=True)
for f in sorted(glob.glob(f'{base}/svg/*.svg')):
    cairosvg.svg2png(url=f, write_to=f.replace('/svg/', '/cards/').replace('.svg', '.png'), output_width=1950)
w = PdfWriter()
for f in sorted(glob.glob(f'{base}/svg/*.svg')):
    cairosvg.svg2pdf(url=f, write_to='/tmp/w46-page.pdf')
    w.add_page(PdfReader('/tmp/w46-page.pdf').pages[0])
with open(f'{base}/print-tmp.pdf', 'wb') as fh:
    w.write(fh)
print("cards+print pdf done")
EOF
ls -la "$ED/cards/" | head -3
CODE=$(echo "$NATIVE" | tr 'a-z' 'A-Z')
$ROOT/tools/venv/bin/python $ROOT/tools/webpdf.py "$ED/svg" "$ED/Le-Lucerna-VOL4-${CODE}-web.pdf" 2>&1 | tail -2
W46_BUILD_DIR="$BUILD" W46_OUT_MD=/tmp/w46-${NATIVE}.text.md $ROOT/tools/venv/bin/python $ROOT/hidden_files/w46/text-export/export.py 2>&1 | tail -1
{ printf '# %s\n\n%s\n\n' "$TITLE" "$META"; cat /tmp/w46-${NATIVE}.text.md; } > "$ED/${SLUG}.text.md"
CODE=$(echo "$NATIVE" | tr 'a-z' 'A-Z')
mv "$ED/print-tmp.pdf" "$ED/Le-Lucerna-VOL4-${CODE}.pdf"
echo "--- verify ---"
ls -la "$ED/"*.pdf "$ED/${SLUG}.text.md"
pdfinfo "$ED/Le-Lucerna-VOL4-${CODE}-web.pdf" | grep -E "Pages"
pdftotext "$ED/Le-Lucerna-VOL4-${CODE}-web.pdf" - | wc -c
pdftotext "$ED/Le-Lucerna-VOL4-${CODE}.pdf" - | wc -c
sha256sum "$ED/Le-Lucerna-VOL4-${CODE}-web.pdf" "$ED/Le-Lucerna-VOL4-${CODE}.pdf"
