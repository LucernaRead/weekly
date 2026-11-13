# Gate log — W47 zh-tw × ko, proof1（機械門，全跑，輸出留檔；針對重 fan-out 新建版）

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語讀者語）
- 交付物 SHA（開工前核對，全部機械門跑完後復核未變）：
  - 印刷 `Lucerna-VOL4-KO.pdf` 16,838,018 B / `75610665146d9903c5144148f799386d2ed928f11264e2a8697cb24429c307f0`
  - 網頁 `Lucerna-VOL4-KO-web.pdf` 2,325,041 B / `140f83acdba99fba9b67ec26f8e1418d85a2e5aa9f791d3f16238265c67bb282`
  - `2026-w47-zh-tw-ko.text.md` 53,922 B / `2e7038cc4c1266146824db80b1a20f87f83593b69f3e8bd755596b435e6986a8`
- 探針：開工前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 首次因 `/dev/null` 被寫成普通文件而失敗；以空普通文件恢復（與探針前既有狀態相同）後成功（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）。目錄 `scratch-proof-zh-tw-ko1/` 真實寫盤通過（`.probe`、`gates/`、`baseline/`、`render/`、`flow.txt` 均已寫入）。`TMPDIR=<scratch>/tmp`。
- 舊輪文件：本目錄內 09:21–09:45 上一輪 proof1 的 `PROOF-NOTE.md`／`GATE-LOG.md`／`baseline/`／`gates/` 已原樣移入 `proof1-old-build/` 保全，本輪輸出為全新文件。

## 1. Freeze — baseline 8/8，diff 8 頁全覆蓋 ✅

- baseline：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-zh-tw-ko --core-svg production/2026-w47/2026-w47-zh-tw-ko/svg --out scratch-proof-zh-tw-ko1/baseline`
  → `baseline: 8/8 SVGs byte-identical`，8 頁逐一 OK（p1-front 2f021d71…、p2-life 050e53b0…、p3-culture 6b01d169…、p4-sport 80d4d8db…、p5-youth 96565ffd…、p6-deep 6301c38d…、p7-lang ba9b4b48…、p8-test 75eb33e0…）；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。運行時 Pillow 13.0.0 / FreeType 2.14.3。
- diff：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-zh-tw/svg --edition-svg …/svg --json gates/freeze-diff.json`
  - 逐頁增／刪：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187
  - 新增 CJK 共 4,692 字，全部為韓文音節 + 家具標題／被注詞彙／繼承串；刪除含漢字的串全部為雙語家具（中文標題 + 英文注 → 中文 + 韓文）或含引詞的英文答案注，無簡體字、無意外新增中文（`gates/freeze-diff.json`、`gates/freeze-diff.log`）。逐頁 CJK 淨增量已逐項核對（見 PROOF-NOTE §7／§8）；P7 淨增 入／集／圍／間／夜／市各 1 皆為韓語釋義引用的中文詞。
  - 注：freeze-diff.json 內一處 `星光���道` 經按字節核查為 diff 工具顯示偽影（8 個 SVG + text.md 含 0 個 U+FFFD；SVG 實測為完整「星光大道」）。

## 2. checks.py（本版自帶）✅

- `tools/venv/bin/python production/2026-w47/2026-w47-zh-tw-ko/checks.py` → `CHECKS PASS`
- 8 條金句各恰出現 2 次、`SIMP_ONLY_HITS []`、P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]（`gates/checks.log`）。

## 3. Occlusion 審計 — 0 flags ✅

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-zh-tw-ko/svg`
- 輸出（`gates/occlusion.log`）：
  `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
  `production/2026-w47/2026-w47-zh-tw-ko/svg: 0 flags`

## 4. P8 extract + compare — 150/150，CLEAN ✅

- extract：`tools/venv/bin/python tools/p8.py extract --p8 …/svg/p8-test.svg --total 150 --json gates/p8-extract.json`
  → `noted set = 150 of 150`（`gates/p8-extract.log`）
- compare：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg --edition-p8 …/svg/p8-test.svg --total 150`
  → `core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]`（`gates/p8-compare.log`）
- core extract 另存 `gates/p8-core-extract.json`（供 keycheck.py 三源交叉用）。

## 5. keycheck-150（三源交叉 + 全版掃查）✅

- 腳本：`keycheck.py`（本目錄自寫，ko 改寫版；源：A = 版 P8 SVG keys、B = text.md 答案區、C = 核心 P8 SVG keys）
- 結果（`gates/keycheck.log`、`keycheck-150.json`）：
  - B 解析 150 項，1–150 連續無缺；**三源一致 150/150，mismatches []**（Q150 歸一化為「✓」）
  - SVG CJK 版獨有 {韓}、核心獨有 {英}；text.md 同然
  - 彎引號：版 SVG U+0022 0、U+0027 1（`Kanahei's Little Animals` 專名）、U+201C/U+201D/U+2018/U+2019 皆 0；text.md 同然
  - 英文星期／月份名、"next Sunday"／"Next Sunday"、"finish line"／"end point"、「下週日」、「다음 주 일요일」、BABYMONSTER、결승선、장소：版 SVG 與 text.md **皆 0**；「이번 주 일요일」版 SVG 2（字串計；第 3 處跨 SVG 節點「이번」＋「주 일요일」，已核實）、text.md 2（同理，第 3 處跨行折斷）
  - P8 六節標頭全為繁體中文 + 韓語對譯
  - 寫作範文：去空白計 **142 字**，CJK+數字計 126，在 120–180 區間內，與文內「142자」標註相符
- 填空鍵：`check_fillin_keys.py`（nl1 gtools）→ **54/54 在正文，缺失 []**（`gates/fillin-check.log`）。

## 6. Creambox（canonical 全版掃描）+ boxtitle + creambox-pil ✅

- canonical：`python3 hidden_files/w47/tools/creambox.py production/2026-w47/2026-w47-zh-tw-ko/svg/*.svg`（`gates/creambox.log`）
  - 36 盒（P1 5、P2 6、P3 7、P4 4、P5 8、P6 3、P7 工具盒 3）
  - 全部負清除皆為盒下 +37.0／+44.0px 的下一欄標題／首句（假陽性類：如 '夜間遊行最終場，六福村見！'、'讀懂了嗎？　이해했나요?'、'鋼雕藝術節：最後一週，快去'……），盒內自有末行均為大正清除；+44.0 為本版固定的盒底至下欄標題間距，非真漫出區間（真漫出實測為 +12.7／+18.0）
  - 各頁 inside-only 最小清除：P1 18.8、P2 41.8、P3 16.1、P4 35.8、P5 6.4、P6 19.9；P7 工具盒 inside +40.5／+12.5／+14.0，P7 匯總：3 盒、最小 inside +12.5、最小 desc-clear +6.5
  - P5 最小盒（迪士尼小檔，y=629，盒底 1099.4）：inside-only +6.4、desc-clear −0.4——末行僅一字「日」，無下行筆畫，係 0.30 係數公式偽影；PIL 真墨實測底清除 +4.4px（見 §7），目視在盒內
- boxtitle（nl1 gtools，真墨）：36 盒，**超框 0**，最小右余 18.5px（P1）、最小左余 18.0px（`gates/boxtitle.log`、`gates/boxtitle.json`）
- creambox-pil（nl1 gtools，真墨）：36 盒，**STRADDLE 0、CREAM-COVER 0**；各頁最小底清除：P1 16.5、P2 39.8、P3 14.1、P4 33.8、P5 4.4、P6 17.1、P7 10.5（`gates/creambox-pil.log`、`gates/creambox.json`）

## 7. P6 abutting（真墨）+ P5 緊盒驗證 ✅

- P6 18:30「頒獎典禮」墨右緣 990.8 → 19:00「夜間遊行」墨左緣 991.4，墨縫 **0.6px**，與核心先例完全一致（`gates/abutting-p6.log`）
- P5 緊盒 PIL 真墨：迪士尼小檔盒末行「日」墨底至盒底 **4.4px**（creambox-pil 各頁最小底清除 P5 4.4px）

## 8. 印／網文字層比對 + PDF 指標 ✅

- `pdftotext -layout` 印／網：各 95,034 字節（`gates/print.txt`、`gates/web.txt`）
- 字符多重集差：印刷獨有 0、網頁獨有 0（逐字相同）
- PyMuPDF（`gates/pdf-metrics.log`）：印、網皆 8 頁、1462.5 × 2025 pt；最小字號 9.75pt（整刊與 P8 皆然）、最大 147.0pt（P1）、P8 最大 34.5pt
- 網頁 PDF 2,325,041 B（< 7 MB）；BABYMONSTER 印網文字層皆 0

## 9. 助詞／繫詞窮舉（K1 核實，見 PROOF-NOTE §6）

- 全版 CJK 引詞 + 助詞窮舉 26 行：錯誤 5 行（入圍은／鋼雕은／入圍을／市集는／入圍이），「本週…이」3 行為「이번」融合偽影（已排除），正確 18 行；按落版計：正確 24 處、錯誤 6 處、偽影 3 處
- 純韓語詞空格消去後全版掃描：元音＋을 0、輔音＋를 0、元音＋은 0、元音＋이에요 0、輔音＋예요 0；CJK＋이에요 全數：封王／遊行／市集／集點正確，僅 入圍이에요×2 錯；CJK＋예요 僅 鋼雕예요（Q107，正確），反襯 K1-2 為筆誤
- K1 源頭核實：`scratch-fanout-zh-tw/tables.py:1939`（入圍이에요）、`:2171`（入圍은／鋼雕은）、`:2182`（入圍을）、`:2215`（市集는）；落版 `content7.py:43/:44/:52/:60`、`content8.py:58`
- `입니다`／`습니다`：text.md 0、8 個 SVG 0（M4 已修復確認）
- U+FFFD：8 個 SVG + text.md 按字節計 0

## 10. 其餘核查

- VOL：VOL.4 ×10、VOL.3 ×2（延期披露所指上期）、VOL.5 ×1（下期預告），均正確
- ABSTRACT.txt：單行 236 字（去空白）、0 個 ASCII 雙引號、韓語、含刊名／目標語／A2–B2／150 題與真實主題
- 頁腳「제N면／전체 8면」8 頁齊全
- 8 張渲染卡片（`render/p-1.png` … `p-8.png`，100 dpi 自印 PDF 渲染）逐版目視：無溢出、無重疊、無裁切、無頁腳碰撞
- 星期核對（`date -d`，Asia/Taipei）：11/6 五、11/13 五、11/16 一、11/17 二、11/19 四、11/21 六、11/22 日、11/24 二、12/27 日、2027/1/3 日、10/23 五，皆與版面標註相符
- 機械門跑完後復核：三交付物 SHA 與開工前一致，未改動任何源文件；兩目錄 `git status` 仍僅為 `??` 未提交狀態

## 結論

機械門 10 項全綠；上一輪 8 項缺陷已全部驗證修復；但內容復校發現新缺陷 1 類（K1，韓語助詞／繫詞誤用，5 處、6 個落版點，機制層），本版按 SOP §8 **不可定稿**，需改 tables.py 4 條 ko 值 → 重擴 + 重渲染 + 從頭再復校一輪。
