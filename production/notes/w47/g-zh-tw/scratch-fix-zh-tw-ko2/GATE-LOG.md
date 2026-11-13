# Gate log — W47 zh-tw × ko, fix2（機械門，全跑，輸出留檔；針對 K2 重建版）

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語讀者語）
- 交付物 SHA（開工前核對：印 16,838,020 B / `c04102a9…`、網 2,325,041 B / `ed9e11a5…`、text 53,916 B / `2af17f02…`，與任務給定一致；拷回生產後復核為新三件）：
  - 印刷 `Lucerna-VOL4-KO.pdf` 16,838,020 B / `09fd27a05b0864bbb30da93339d4f2285abf351d44ca72cef5adb7e254ea3d1c`
  - 網頁 `Lucerna-VOL4-KO-web.pdf` 2,325,045 B / `e4832f3f8a789eb89e7a68c39f3986fc7428baae395223a1de27844dfd8dede4`
  - `2026-w47-zh-tw-ko.text.md` 53,916 B / `a44ba8cbb74f28c862b8f689f27e260a2fde3c5ac328e1597147ff933029b1e1`
- 探針：開工前 `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0；目錄 `scratch-fix-zh-tw-ko2/` 真實寫盤通過。`TMPDIR=<scratch>/tmp`，系統 /tmp 未用。解釋器全程 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。
- 工具來源：`gates.py`／`gtools/`／`keycheck.py` 自 `scratch-proof2-zh-tw-ko2/` 複製，僅把其中硬編碼的 scratch 路徑改為本目錄、版目錄改為 scratch 候選版（見 FIX-LOG §7 過程事件 1 的兩處補丁修正）；`tools/creambox.py` 為 `hidden_files/w47/tools/` 共享 canonical 工具。未改任何工具邏輯。
- 核心基線（重建前後未變）：印 `5ec35fe2…570d9a`（19,420,552 B）、網 `1c0799ac…6d240`（2,324,042 B）、text `09e083e1…44e02f02b`（49,798 B）。

## 1. Freeze — baseline（生產版 8/8）+ diff 8 頁全覆蓋 ✅

- baseline（生產版，拷回後重跑）：`tools/venv/bin/python tools/freeze.py baseline --build . --core-svg svg --out gates/prod-verify/freeze-base`（cwd=版目錄）
  → `baseline: 8/8 SVGs byte-identical`（`gates/prod-verify/freeze.log`）：p1-front 2f021d71…、p2-life 050e53b0…、p3-culture 6b01d169…、p4-sport 80d4d8db…、p5-youth 96565ffd…、p6-deep 6301c38d…、p7-lang ea987634…、p8-test a390fcc6…；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。P1–P6/P8 與 fix1 版逐字相同，僅 P7 變（31f7898a→ea987634）。
  - 註：scratch 候選版的 gates.py 版 freeze 為 0/8（見 FIX-LOG §6 註）——freeze.py 重定向正則不認 `hidden_files/` 路徑，屬工具局限，非版面問題；該次重建為確定性重建，8 個 SVG SHA 事後核實未變。生產版重跑即 8/8。
- diff：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-zh-tw/svg --edition-svg <scratch 候選版>/svg --json gates/freeze-diff.json`（rc=0，`gates/freeze-diff.log`；生產版 SVG SHA 與候選版逐字相同，結果等價）
  - 逐頁增／刪：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187（與 fix1 版逐值相同）
  - 新增 CJK 共 **4,690** 字（與 fix1 版同；K2 為等長替換，不變字數）；新增皆為韓文音節 + 引用的中文詞

## 2. run.py（scratch 構建）✅

- `build-run.log`：rc=0，`FLOW OVERFLOW` 命中 **0**，HEAD TOO WIDE 0；P7 col3 ends 1821.42、teaser ends 2575.42（與 fix1 構建值逐值相同）；150 題：A2 44 / B1 74 / B2 32；REGISTRY by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；MODEL chars: 142。
- render.py rc=0（`render.log`）；webpdf rc=0（2,325,045 B，`webpdf.log`）；text.md 導出 rc=0（`export.log`）。

## 3. checks.py（本版自帶；生產復核同）✅

- `tools/venv/bin/python production/2026-w47/2026-w47-zh-tw-ko/checks.py` → `CHECKS PASS`（`gates/ko-fix2/checks.log`）
- 8 條金句各恰出現 2 次、`SIMP_ONLY_HITS []`、P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]。

## 4. Occlusion 審計 — 0 flags ✅

- 命令：`tools/venv/bin/python tools/occlusion_audit.py --selftest` + `... --json gates/ko-fix2/occlusion.json <版>/svg`
- 輸出（`gates/ko-fix2/occlusion.log`）：selftest rc=0，`production/2026-w47/2026-w47-zh-tw-ko/svg: 0 flags`（生產復核 `gates/prod-verify/occlusion.json` 同）。

## 5. P8 extract + compare — 150/150，CLEAN ✅

- extract：`tools/venv/bin/python tools/p8.py extract --p8 <版>/svg/p8-test.svg --total 150 --json gates/ko-fix2/p8-extract.json`
  → `noted set = 150 of 150`（`gates/ko-fix2/p8-extract.log`）
- compare：`tools/venv/bin/python tools/p8.py compare --core-p8 production/2026-w47/core-zh-tw/svg/p8-test.svg --edition-p8 <版>/svg/p8-test.svg --total 150 --json gates/ko-fix2/p8-compare.json`
  → `status: CLEAN  missing=[] extra=[] uncertain=[] keydiff=[]`（core 150 noted / edition 150 noted；`gates/ko-fix2/p8-compare.log`；注：gates.json 中 "extra": "?" 是 gates.py 取鍵名 `extra_count` 未取到所致，compare JSON 原文本身含 `"extra": []`，實為 0；生產復核 same：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]`）。
- core extract 另存 `gates/p8-core-extract.json`（供 keycheck.py 三源交叉用）。

## 6. keycheck-150（三源交叉 + 全版掃查）✅

- 腳本：`keycheck.py`（本目錄，沿用 proof2 版，僅改輸出目錄與版目錄）；`gates/keycheck.log`、`keycheck-150.json`
- 結果：
  - B 解析 150 項，1–150 連續無缺；**三源一致 150/150，mismatches []**
  - SVG CJK 版獨有 {韓}、核心獨有 {英}；text.md 同然
  - 彎引號：版 SVG U+0022 0、U+0027 1（`Kanahei's Little Animals` 專名）、U+201C/U+201D/U+2018/U+2019 皆 0；text.md 同然
  - 英文星期／月份名、"next Sunday"／"Next Sunday"、"finish line"／"end point"、「下週日」、「下周日」、「다음 주 일요일」、BABYMONSTER、결승선、장소：版 SVG 與 text.md **皆 0**；「이번 주 일요일」版 SVG 2（字串計；第 3 處跨 SVG 節點「이번」＋「주 일요일」，已核實）、text.md 2（同理）
  - P8 六節標頭全為繁體中文 + 韓語對譯；P8 標頭「第8版　本週大測驗　全部答案　이번 주 큰 테스트와 모든 정답」
  - 寫作範文：去空白計 **142 字**，CJK+數字計 126，在 120–180 區間內，與文內「142자」標註相符
- 填空鍵：`gtools/check_fillin_keys.py` → **54/54 在正文，缺失 []**（`gates/ko-fix2/fillin-check.log`）。

## 7. Creambox（canonical 全版掃描）+ boxtitle + creambox-pil ✅

- canonical：`python3 hidden_files/w47/tools/creambox.py <版>/svg/*.svg`（`gates/ko-fix2/creambox.log`）
  - 36 盒（P1 5、P2 6、P3 7、P4 4、P5 8、P6 3、P7 工具盒 3）
  - 負清除 **0**；各頁 inside-only 最小清除：P1 18.8、P2 41.8、P3 16.1、P4 35.8、P5 6.4、P6 19.9；P7 工具盒 inside +40.5／+12.5／+14.0，P7 匯總：3 盒、最小 inside +12.5（與 fix1 版逐值相同）
  - P5 最小盒（迪士尼小檔）：inside-only +6.4、desc-clear −0.4——末行僅一字「日」，無下行筆畫，系 0.30 係數公式偽影；PIL 真墨實測底清除 +4.4px，目視在盒內
- boxtitle（gtools，真墨）：36 盒，**超框 0**，最小右余 18.5px（P1）、最小左余 18.0px（`gates/ko-fix2/boxtitle.log`、`boxtitle.json`）
- creambox-pil（gtools，真墨）：36 盒，**STRADDLE 0、CREAM-COVER 0**；各頁最小底清除：P1 16.5、P2 39.8、P3 14.1、P4 33.8、P5 4.4、P6 17.1、P7 10.5（`gates/ko-fix2/creambox-pil.log`、`creambox.json`）

## 8. P6 abutting（真墨）+ P5 緊盒驗證 ✅

- P6 18:30「頒獎典禮」墨右緣 990.8 → 19:00「夜間遊行」墨左緣 991.4，墨縫 **0.6px**，與核心先例完全一致（`gates.json` abutting 節）
- P5 緊盒 PIL 真墨：迪士尼小檔盒末行「日」墨底至盒底 **4.4px**（creambox-pil 各頁最小底清除 P5 4.4px）

## 9. 印／網文字層比對 + PDF 指標 ✅

- `pdftotext -layout` 印／網：各 95,029 字節（`gates/ko-fix2/print.txt`、`web.txt`）
- 字符多重集差：印刷獨有 0、網頁獨有 0（逐字相同）；「本週日」各 11、「下週日」0、BABYMONSTER 0、「取捨」2、「end point」0、「小雪」36
- PyMuPDF（`gates.json` pdf 節）：印、網皆 8 頁、1462.5 × 2025 pt；最小字號 9.75pt（整刊與 P8 皆然）、最大 147.0pt（P1）、P8 最大 34.5pt
- 網頁 PDF 2,325,045 B（< 7 MB）；BABYMONSTER 印網文字層皆 0
- 英文泄漏掃描（`gates.json` leak_scan）：deny_hits {}；shared_ascii_long 僅「A. 12:00 · B. 14:00 · C. 19:00」時刻串，與核心共有

## 10. K2 修后核對 + K1 回歸 + 助詞窮舉 ✅

- K2 舊形「小雪는」：8 個 SVG + text.md + content7.py 出現皆 **0**；新形「小雪은」各就其位（content7.py:60、SVG p7-lang 節點 x=989.0 y=458.42、text.md:4699）；交付印 PDF 200 dpi 渲染放大 `render/zoom-k2-p7-b2-prod.png` 目視確認在版。
- 羅馬字形 `Xiaoxue는`：text.md 6 處，未動（元音結尾，正確）。
- K1 舊形 5 串（入圍은／鋼雕은／入圍을／市集는／入圍이에요）：8 個 SVG + text.md 出現皆 **0**；新形（入圍는／鋼雕는／入圍를／市集은 各 SVG 1 處 + text.md 1 處；入圍예요 SVG 2 處 + text.md 2 處）各就其位；`입니다`／`습니다` 全版 0。
- 助詞窮舉（CJK 引詞 + 助詞，`particle-sweep.py`）：19 形 50 命中，新舊掃查 diff 僅「小雪는」→「小雪은」一處；其餘 25 例（proof2 口徑）全部正確；「封王은」跨 SVG 節點「封」＋「王은」，已核實。純韓語詞空格消去後全版掃描（`pure-ko-scan.py`）：元音＋을 0、輔音＋를 0、元音＋은 0、元音＋이에요 0、輔音＋예요 0（元音＋이 2 命中皆為輔音結尾 이 풍선이／한작품이，正確）。
- U+FFFD：8 個 SVG + text.md 按字節計 **0**。

## 11. 其餘核查

- VOL：VOL.4 ×10、VOL.3 ×2（延期披露所指上期）、VOL.5 ×1（下期預告），均正確（與 proof2 同）
- ABSTRACT.txt：韓語單行摘要，0 個 BABYMONSTER，含刊名／目標語／A2–B2／150 題與真實主題；與舊版逐字相同
- 頁腳「제N면／전체 8면」8 頁齊全
- 8 張渲染卡片（`render/p--1.png` … `p--8.png`，100 dpi 自印 PDF 渲染）：P7/P1/P8 逐版目視：無溢出、無重疊、無裁切、無頁腳碰撞；其餘 6 頁 SVG 與舊版逐字節相同；另有放大證據 `render/zoom-k2-p7-b2.png`（scratch 構建）與 `render/zoom-k2-p7-b2-prod.png`（交付印 PDF，兩者逐字節相同）
- 機械門跑完後復核：生產三 SHA 與 scratch 候選構建逐字相同（印 09fd27a0…／網 e4832f3f…／text a44ba8cb…）；核心三 SHA 未變；生產 `__pycache__` 與修前逐字節相同；`git status` 僅為 `??` 未提交狀態

## 結論

機械門全綠；K2 一處已修（舊形全版 0，新形各就其位，交付 PDF 放大目視確認）；K1 五處六落版點回歸全過；全版助詞重掃除 K2 外無其他錯誤、無新增同類錯誤。本版已拷回生產（未 commit、未 push），待 proof2 #2 從頭再復校一輪。
