# GATE-LOG — 2026-W47 zh-tw-nl proof1

## 探針
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0（開工前；寫盤前重探一次，同樣通過）
- scratch 寫入探針：`hidden_files/w47/scratch-proof-zh-tw-nl1/probe.txt` 寫入成功
- 磁盤：`df` 顯示 /home/hatch 72G 已用／78G 可用，全程無 EDQUOT

## SHA 核對
- `sha256sum Lucerna-VOL4-NL.pdf Lucerna-VOL4-NL-web.pdf` → `254751618af573d5…`／`3c308d062aeda055…`，與任務書一致；字節 20,939,118／2,393,503
- 命令：`stat -c '%n %s'` 核對，RC=0

## occlusion_audit
- `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-zh-tw-nl/svg` → 自測通過，終輪 `0 flags`，RC=0

## p8
- `tools/venv/bin/python tools/p8.py extract --p8 …/svg/p8-test.svg --total 150` → noted set = 150 of 150，RC=0
- `tools/venv/bin/python tools/p8.py compare --core-p8 …/core-zh-tw/svg/p8-test.svg --edition-p8 …/svg/p8-test.svg --total 150` → `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`，RC=0

## checks.py
- `tools/venv/bin/python checks.py`（版目錄內）→ PHRASE 2×8、SIMP_ONLY_HITS []、CHART p4 [90.0, 450.0, 900.0]、CHART p6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]，`CHECKS PASS`，RC=0

## freeze
- `tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-zh-tw-nl --core-svg production/2026-w47/2026-w47-zh-tw-nl/svg --out hidden_files/w47/scratch-proof-zh-tw-nl1/freeze` → `baseline: 8/8 SVGs byte-identical`，RC=0（core integrity： shipped core SVGs unchanged）
- `tools/venv/bin/python tools/freeze.py diff --core-svg …/core-zh-tw/svg --edition-svg …/svg --json …/freeze-diff.json` → 每頁新增中文字僅 荷/蘭（徽章／頁腳）與 下（D1）；RC=0

## 文本層
- `pdftotext -layout` 兩份 PDF → 各 108,189 字節、8 頁；字符多集差異 0
- PDF 文本層 vs text.md：CJK 多集差異 0；去 md 標題行後全字符差異 56＝幽靈水印 "Lucerna"×8（核心同款設計，見 PROOF-NOTE）
- 題號 1–150 皆 present，無缺失
- 兩份 PDF：8 頁、1462.5×2025 pt；P8 最小字號皆 9.75pt（PyMuPDF 實測）

## abutting 缺口掃描
- PyMuPDF 詞框間距掃描（print PDF）：>8pt 缺口僅 P1 刊頭 "V O L . 4" 4 處 8.6pt（SVG letter-spacing 11.5 設計間距）；其餘無異常
- 註：SOP.md 與 tools/ 均無名為 abutting 的既定工具／規則；以上為本次實施的等效檢查（見 PROOF-NOTE）

## 專項 grep／計數
- `grep -c '下週日' text.md` → 11；`grep -c '本週日'` → 0；逐 SVG 計數：P1×3、P2×1、P3×2、P4×3、P5×0、P6×0、P7×1、P8×1
- 核心對照：`grep -c '下週日' core text.md` → 0；`grep -c '本週日'` → 11
- 荷蘭語 "Volgende zondag" 全版 1 處（P2 Notities L512）；"Volgende week (VOL.5)" 為下期預告，正確
- 彎標點：U+201C/U+201D/U+2019 在 SVG 文本節點中 0 次；ASCII 撇號用法皆正確，無 "' s" 間距缺陷
- 英文殘留定向掃描：疑似 17 命中皆專名／荷蘭語動詞，無英文散文殘留
- 寫作範文字符數：142（實測，與鍵註一致）
- 星期核對：`TZ='Asia/Taipei' date -d` 驗 11/16 一、11/17 二、11/19 四、11/21 六、11/22 日、11/29 日等
- 金馬獎事實：web 搜索多源驗證（63 屆、11/22 日、北流、17:00/18:30、587 部、10/1 入圍、《狂忘警探》11 項、柯煒林、再見江湖）

## 視覺目檢
- cards/p1–p8.png 逐頁讀過；另渲染 web PDF P1／P8（60 dpi）核對與印刷版一致
