#!/bin/bash
# W46 zh-tw fix part 2: web PDFs via tools/webpdf.py + text.md regeneration + inventory
G=~/workspace/goals/lucernaread-social-media-operations
FIX=$G/hidden_files/w46/zh-tw-fix
PY=$G/tools/venv/bin/python
cd $G/tools || exit 1
declare -A PDF=( [en]=Lucerna-VOL3-web.pdf [de]=Lucerna-VOL3-DE-web.pdf [es]=Lucerna-VOL3-ES-web.pdf [fr]=Lucerna-VOL3-FR-web.pdf [it]=Lucerna-VOL3-IT-web.pdf [ja]=Lucerna-VOL3-JA-web.pdf [ko]=Lucerna-VOL3-KO-web.pdf [nl]=Lucerna-VOL3-NL-web.pdf [pt]=Lucerna-VOL3-PT-web.pdf [ru]=Lucerna-VOL3-RU-web.pdf )
declare -A DIR=( [en]=weekly-report-w46-zhtw-core [de]=weekly-report-w46-zh-tw-de [es]=weekly-report-w46-zh-tw-es [fr]=weekly-report-w46-zh-tw-fr [it]=weekly-report-w46-zh-tw-it [ja]=weekly-report-w46-zh-tw-ja [ko]=weekly-report-w46-zh-tw-ko [nl]=weekly-report-w46-zh-tw-nl [pt]=weekly-report-w46-zh-tw-pt [ru]=weekly-report-w46-zh-tw-ru )
declare -A H1=( [en]="VOL.3 · Traditional Chinese text · English explanations" [de]="VOL.3 · Chinesischer Text (traditionell) · Erklärungen auf Deutsch" [es]="VOL.3 · Textos en chino tradicional · Explicaciones en español" [fr]="VOL.3 · Textes en chinois traditionnel · Explications en français" [it]="VOL.3 · Testi in cinese tradizionale · Spiegazioni in italiano" [ja]="VOL.3 · 中国語（繁体字）テキスト · 日本語の解説" [ko]="VOL.3 · 중국어 번체 텍스트 · 한국어 해설" [nl]="VOL.3 · Teksten in het Chinees (traditioneel) · Uitleg in het Nederlands" [pt]="VOL.3 · Textos em chinês tradicional · Explicações em português" [ru]="VOL.3 · Тексты на китайском (традиционном) · Объяснения на русском" )
for c in en de es fr it ja ko nl pt ru; do
  d=${DIR[$c]}
  echo "=== $c webpdf ===" | tee -a $FIX/webpdf-textmd.log
  $PY webpdf.py ../files/$d/svg ../files/$d/${PDF[$c]} >> $FIX/webpdf-textmd.log 2>&1; echo "webpdf-$c rc=$?" | tee -a $FIX/webpdf-textmd.log
  echo "=== $c text.md ===" | tee -a $FIX/webpdf-textmd.log
  $PY ../hidden_files/w46/export_zhtw_textmd.py ../files/$d/svg ../files/$d/2026-w46-zh-tw-$c.text.md "${H1[$c]}" >> $FIX/webpdf-textmd.log 2>&1; echo "textmd-$c rc=$?" | tee -a $FIX/webpdf-textmd.log
done
echo "WEBPDF+TEXTMD DONE" | tee -a $FIX/webpdf-textmd.log
