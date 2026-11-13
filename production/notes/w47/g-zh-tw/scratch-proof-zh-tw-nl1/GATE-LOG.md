# GATE-LOG — W47 zh-tw-nl proof1（獨立復校，針對重 fan-out 新建版）

執行：2026-11-11 12:07–13:05 UTC。解釋器一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，正典棧；未用系統 python3）。`TMPDIR=<scratch>/tmp`。門驅動為 `scratch-proof-zh-tw-nl1/gates.py`（由 refanout 輪 `gates.py` 拷貝，僅改輸出目錄為本 scratch、並把兩處 `python3` 調用改為 venv），輸出於 `gates/nl-proof1/`。

## 探針（開工前）
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0
- scratch 真實寫入：`hidden_files/w47/probe-proof-zh-tw-nl1.txt` 寫入成功（`probe-ok 2026-11-11T12:07:17Z`）
- 磁盤：`/tmp` tmpfs 507M 空閒；全程用 goals 側 `<scratch>/tmp`，未寫 /tmp

## 身份核對（復校前、後各一次，皆一致）
- `sha256sum Lucerna-VOL4-NL.pdf Lucerna-VOL4-NL-web.pdf 2026-w47-zh-tw-nl.text.md`
  → `730e15c9…` / `1c8dc05b…` / `a3662561…`；字節 20,939,172 / 2,409,973 / 50,596，與任務給定全 SHA 一致
- 核心 `core-zh-tw`：`5ec35fe2…` / `1c0799ac…` / `09e083e1…`，復校前後未變
- `git -C ~/workspace/weekly-git status --porcelain -- production/2026-w47/2026-w47-zh-tw-nl production/2026-w47/core-zh-tw` → 兩目錄皆 `??`（未提交重建狀態）；復校只讀，未寫入生產文件

## 1. freeze baseline（第一步，兩次獨立運行）
- `tools/venv/bin/python tools/freeze.py baseline --build . --core-svg svg --out <scratch>/freeze-base`（cwd=版目錄）
  → `runtime: …/tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3`；`baseline: 8/8 SVGs byte-identical`；`core integrity: shipped core SVGs unchanged`，RC=0。見 `freeze.log`
- 門驅動內第二次運行（`gates/nl-proof1/freeze.log`）：同樣 8/8，RC=0
- 若 0/8 即停手的觸發條件未觸發（8/8），繼續全量復校

## 2. freeze diff（core vs edition SVG）
- `tools/venv/bin/python tools/freeze.py diff --core-svg …/core-zh-tw/svg --edition-svg …/svg --json freeze-diff.json`
  → 每頁新增 CJK 僅 荷/蘭（p1 各 2 次、p2–p8 各 1 次，合計 18）；其餘增減皆為荷蘭語譯文替換英文。RC=0。見 `freeze-diff.log` / `freeze-diff.json`
- 舊版 D1 對照：舊版 freeze-diff 含「下」×11 淨增；本版為 0（見 PROOF-NOTE §0）

## 3. 門驅動全量運行
- `tools/venv/bin/python gates.py nl proof1`（cwd=本 scratch），RC=0，輸出 `gates/nl-proof1/gates.json` + 各門日志。逐門結果：
  - checks.py（版目錄內）：`CHECKS PASS`，RC=0；`SIMP_ONLY_HITS []`；CHART p4 `[90.0, 450.0, 900.0]`、p6 dots `[188.0, 695.21, 948.82, 1033.36, 1202.43]`（見 `gates/nl-proof1/checks.log`）
  - occlusion：selftest rc=0；audit `flag_count 0`，RC=0（`occlusion-selftest.log` / `occlusion.log` / `occlusion.json`）
  - p8 extract：`noted set = 150 of 150`（`p8-extract.log` / `p8-extract.json`）；compare：`status CLEAN`，`missing [] extra [] uncertain [] keydiff []`（`p8-compare.log` / `p8-compare.json`）
  - canonical creambox（`hidden_files/w47/tools/creambox.py`，venv 運行）：36 盒，負清除 0；P7 最小內清除 12.5（工具盒 40.5/12.5/14.0）；各頁最小 P1 18.8 / P2 41.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5（`creambox.log` / `creambox.json`）
  - boxtitle（`gtools/boxtitle.py`）：36 盒，超框 0，最小右余 1.5px（`boxtitle.log` / `boxtitle.json`）
  - creambox-pil（`gtools/creambox-pil.py`）：STRADDLE 0，CREAM-COVER 0，P7 最小清除 9.0（`creambox-pil.log`）
  - 印/網文字層（`pdftotext -layout`）：print 107,779 B = web 107,779 B，多重集差分 0；本週日 11 / 下週日 0 / BABYMONSTER 0 / 取捨 2，印網一致（`print.txt` / `web.txt`）
  - PDF 指標（PyMuPDF）：印、網皆 8 頁、1462.5×2025 pt；P8 最小字號 9.75pt、最大 34.5pt；P1 最大字號 147.0
  - keycheck（`gtools/check_fillin_keys.py`，venv 運行）：填空鍵 54，無 MISS 行；keys 1–150 連續（`fillin-check.log`）
  - leak scan：deny 命中 {}；唯一共有長 ASCII 串「A. 12:00 · B. 14:00 · C. 19:00」
  - abutting：P6 18:30/19:00 墨縫 0.6px（label1 box [906.8, 955.8, 990.8, 977.5]；label2 [991.4, 955.8, 1075.4, 976.2]）
  - freeze（門內）：8/8，RC=0
  - 文件 SHA（門內重算）：與 §身份核對一致

## 4. STRADDLE 舊版對照
- `tools/venv/bin/python gtools/creambox-pil.py <refanout-backup>/2026-w47-zh-tw-nl/svg gates/old-nl-proof1`
  → 舊版 `STRADDLE flags: 0`，`CREAM-COVER flags: 0`，RC=0。新版同為 0，無回歸（`gates/old-nl-proof1/creambox-pil.log`）

## 5. 150 題三源交叉（`keycheck.py` → `keycheck-150.json` / `keycheck.log`）
- 核心 P8 keys：`tools/venv/bin/python tools/p8.py extract --p8 …/core-zh-tw/svg/p8-test.svg --total 150 --json p8-core-extract.json`
- 三源（版 SVG keys / text.md 答案區 / 核心 SVG keys）：**150/150 一致，mismatches []**
- 解析器修正記錄：初版用 `\s+` 匹配題號，把 text.md 第 77 題折行尾「48.」誤讀為第 48 題，且把 150 題「✓ Open opdracht」判與 SVG 鍵「✓」不一致；改行內空格匹配 + 150 題標籤歸一（與核心「✓ Open task」平行）後 150/150。皆為解析假象，非成品問題

## 6. 專項掃查（`keycheck.py` 同次運行，見 `keycheck.log`）
- CJK 字符集差：版 − 核心 = {荷, 蘭}（SVG 與 text.md 皆然）；核心 − 版 = {英}
- 逐頁 CJK 淨增量（freeze-diff.json）：僅 荷/蘭為正；其餘皆為英文串替換帶來的負向差
- 簡體候選碼點 grep（国/龙/马/门/风/云/电/车/见/读/写/爱/头/对/为/时/关/开/东/来/气/过/还/这/连/进/远/运/会/万/与/业/义/习/达/观/图/书/觉/视/长/乐/让/认/识/应/发/学/实/宝/话/后 等）：命中 0
- 直引號：U+0022 版 SVG 0、text.md 0；U+201C/U+201D/U+2018/U+2019 皆 0；U+0027 僅 11 處，全為荷蘭語 's（'s avonds / 's nachts / 's middags）
- 英文日/月名與凍結 key：Sunday/Monday/…/November/December/January、"next Sunday"/"Next Sunday"/"finish line"/"end point"：版 SVG 與 text.md 皆 0；"下週日" 0、"下周日" 0；"zondag" 14、"Deze zondag" 1、"op zondag 22 nov." 9
- E 節標籤：P8 標頭「E　情景說話　Zeg het in context」，A–F 六節標頭全繁體 + 荷蘭語對譯
- 寫作範文字符數：實測 142（去空白亦 142），120–180 帶內，與鍵註「142 tekens」一致
- 星期核對：`TZ='Asia/Taipei' date -d` 驗 11/6 五、11/11 三、11/13 五、11/16 一、11/17 二、11/19 四、11/21 六、11/22 日、11/24 二、12/27 日、2027/1/3 日、10/23 五

## 7. 目視（自渲染）
- `pdftoppm -png -r 100 …/Lucerna-VOL4-NL.pdf render/p` → `render/p-1.png` … `p-8.png`（2032×2813），逐頁讀過：無溢出、無重疊、無裁切、無頁腳碰撞（見 PROOF-NOTE §5）

## 8. 外部事實核查（公開檢索，2026-11-11）
- 金馬獎（63 屆、11/22 日、北流、17:00/18:30、柯煒林、再見江湖、587 部、10/1 入圍、《狂忘警探》11 項、影展 11/6–22）、味全龍遊行+感謝祭+U-Sport、六福村墓碑鎮、新北耶誕城+德國市集、高雄鋼雕+林洪玉秀、香港迪士尼聖誕、西九爵士音樂節、寶可夢 30 週年、圓方體能競技場、小雪 2026-11-22——皆與公開來源一致（見 PROOF-NOTE §8；「11/19 起」新日間演出日期在檢索片段中未直接出現，無反證）
