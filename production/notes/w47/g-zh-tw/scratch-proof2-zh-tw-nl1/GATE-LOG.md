# GATE-LOG — 2026-W47 zh-tw-nl (proof2)

獨立重跑記錄。工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0, FreeType 2.14.3）。
工作區：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-nl1/`
（TMPDIR 全程指向其 `tmp/`；系統 /tmp 未用。）
開工探針：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29b…`，RC=0；scratch 寫入測試通過。
凡 import 生產源碼一律 `PYTHONDONTWRITEBYTECODE=1`；`content*.py` 的 OUT 硬編碼指向生產 svg，`render.py` BASE 為自身目錄——一律走 scratch 副本（OUT 經 sed 重定向，驗證零殘留 `workspace/weekly-git` 引用）或 freeze.py（自行重定向）。

## G1 — run.py（構建 + SVG 重建）

- 方式：生產源碼複製至 `run-copy/build/`，OUT 重定向至 scratch svg；`svglib.py` 由 repo 拷入（首跑因缺 `svglib` 模組失敗，為環境問題，非缺陷）。
- RC=0；TOTAL 150；警告 0（FLOW OVERFLOW 0、HEAD TOO WIDE 0、error 0）。
- 總量：A2 44 / B1 74 / B2 32；頁 P1 10、P2–P6 各 18、P7 12、P8 38；類型 單選 67、完成句子 54、配對 16、完形單選 12、寫作 1。
- 重建 SVG 8/8 與生產逐字節一致。
- P7 幾何：col3 止 1823.3，teaser 止 2577.3（footer rule 2596，餘 18.7px）；P7 語帶 fy=1847.3。
- Log：`run-copy/run.log`（第 24–25 行載 P7 值）。

## G2 — checks.py

- 方式：scratch 副本 + 指向生產 svg 的符號連結（唯讀；首試因副本缺 svg 目錄致 PHRASE 0s，為副本瑕疵，非發現）。
- RC=0，PASS：8 金句各恰 2×；SIMP_ONLY_HITS []（零簡體字）；P4 柱 [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]。
- Log：`checks/checks.log`。

## G3 — p8.py（抽取 + 比對）

- extract：150/150。
- compare 核心 vs 版：CLEAN——missing=[]、extra=[]、uncertain=[]、keydiff=[]（鍵與核心全同）。
- 唯一 REG–P8 差異：#150 寫作題，REG 鍵 `(開放題，範文如下)` vs P8 印 `✓`——按設計（核心亦印 ✓）。
- 寫作範文 142 字（AST 字面量求值），在 120–180 帶內；P8 鍵註「(142 tekens)」。
- P8 級別徽章 38/38（A2 8 / B1 20 / B2 10，獨立數出）；F 頭 `F　寫一寫　Schrijven` 帶 B2 徽章。
- 檔：`p8/extract-ed.json`、`p8/compare.json`。

## G4 — freeze baseline（核心）

- 方式：repo `tools/freeze.py`（自行重定向路徑）；build-copy 驗證確為核心版（重定向核心 content 檔；核心 gloss 為英文，如 "next Sunday"、"TAIWAN AND HONG KONG"、"英語講解"——與版明顯不同）；核心 SVG 收工重驗不變。
- RC=0，8/8 逐字節一致。
- Log：`freeze-base.log`。

## G5 — freeze diff --strict-cjk（核心 vs 版）

- RC=1，裁為**工具局限，非缺陷**。
- 唯一新增 CJK = 荷/蘭，共 18 字：P1 ×4 字（2 處），P2–P8 各 ×2 字（各 1 處）；每處皆在家具「荷蘭語講解」（P1 副標 + 每頁頁尾 `繁體中文正文　荷蘭語講解`）；核心對應處為「英語講解」。
- Log：`freeze-diff/diff.log`、`freeze-diff/diff.json`。

## G6 — occlusion 幾何遮擋審計

- selftest：6 類全數觸發一次；乾淨對照靜默。
- 審計 RC=0，**0 flags**，0 NEW vs 核心。
- Log：`occl/`。

## G7 — 奶油盒 canonical scan

- 工具：`hidden_files/w47/tools/creambox.py`。
- 36 盒，**0 內部負餘量**；11 處負「末行基線」餘量（-37/-44px）皆裁為下一標題假陽性（內部餘量 +44.1，desc-clear ≥ +38.5；唯一正則漏判 P2 box@757 人工確認：內部基線 976.0，+44.1）。
- P7 工具箱：3 盒，內部最小餘量 +12.5，desc-clear 最小 +6.5。
- Log：`cream/creambox.log`。

## G8 — boxtitle

- 工具：refanout gtools `boxtitle.py`。
- 36 盒，**0 超出**盒右緣；標題右緣最小 1.5px（P2）；左緣最小 18.0px。
- Log/json：`boxtitle/`。

## G9 — PIL 奶油盒

- 工具：refanout gtools PIL creambox。
- 36 盒，**STRADDLE 0，CREAM-COVER 0**。
- 每頁底最小餘量：P1 16.5、P2 37.1、P3 10.8、P4 31.1、P5 4.4（盒 [1439.5, 649.6, 1862.0, 1119.6]，正值無溢出）、P6 17.1、P7 9.0。
- Log/json：`cream/creambox-pil.log`、`cream/creambox.json`。

## G10 — 印/網文字層比對

- `pdftotext -layout` 全文：印/網各 107,779 B，diff 0 行。
- 逐頁：P1 9672 / P2 11466 / P3 13964 / P4 9272 / P5 14085 / P6 10270 / P7 12611 / P8 26439 B，全數一致。
- 檔：`textlayer/`。

## G11 — P8 最小字號（PyMuPDF，venv）

- P8 最小 **9.75pt** = SOP §1.1 下限（11.25pt 目標在 8 頁內不可達；梯級第 4 步）。
- 他頁最小 11.62–12.75pt；P1 最大 147.0pt（masthead）。
- 印/網兩 PDF 皆 9.75pt。

## G12 — 重渲印 PDF（scratch）

- 方式：render.py scratch 副本 + 生產 SVG。
- RC=0；重渲印 PDF 與交付**逐字節相同**（SHA `730e15c9e70631a990d021e16e11f80de018683219c3beba08c897abf90c8832`，20,939,172 B）。
- Log：`render/render.log`。

## G13 — §1.1 配色

- 使用的 fill 全為 §1.1 配色（#302c28、#6f675d、#46581f、#37402f、#5c6e30、#f0eee5、#f4efe1、#fbfaf6、#f6e08e）。
- 額外 fill（#F1E8D4、#34483A、#7898CD、#4D72B4、#EDD17F、#D7B257、#84A283、#4F765D）只在品牌 moth mark 內；無金/紅棕/近黑 fill。

## G14 — 150 題三源逐題驗證

- 方式：`keys/dump_reg2.py`，`reg_ex` 呼叫點追蹤（AST 文件順序 + 堆疊歸屬），REG 接 ex() 題幹接 P8 印出鍵。
- 17 項非 ex() 登記：16 配對子題（4 組 × a/b/c/d，content12:155、content34:59、content34:183、content56:64）+ #150 寫作（直接 `reg_ex`，content8:116）。
- REG↔P8：149/150 一致（#150 見 G3）；REG↔text.md：150 題幹 + 8 金句全數找到。
- 全表：`keys/reg-table2.txt` / `keys/reg-table2.json`（`reg-table.txt` 第一版 BFS 錯位，已廢棄）。

## G15 — 日期 / 星期 / 算術

- `date -d`（Asia/Taipei）驗 16 個日期星期全合（含小雪 2026-11-22（日））。
- 算術逐項重算全合：45 天、48 天、17 天、6 天、12 場；1200+800=2000；5×10=50、7×10=70、差 30；1.5h、5h；P4 柱 / P6 dots 比例全合（見 PROOF-NOTE §1、§3）。

## G16 — 8 金句逐字核對

- checks.py 8×2 通過；text.md 全數核對；荷蘭語譯文通讀；P7 頁碼引用全正確。
- 金句見 PROOF-NOTE §4。

## G17 — 目視（交付印 PDF，8 頁逐頁）

- 110 dpi 渲染 `visual/p-*.png`：P1–P8 全乾淨，無溢出/重疊/頁尾侵入/截斷；P7 欄止於頁尾之上；P8 鍵止 y≈2358 < 2560。
- 圖片與授權：P2 雨（CorraleH CC0）、P3 Méliès 1902（PD）、P4 Bain News Service（PD）、P5 舊維多利亞港（作者不詳 PD）、P7 舊書（CC0）、P8 鉛筆筆記（CC0 Unsplash）。

## G18 — §7 未決項像素實測（交付 PDF 渲染像素為準）

- **next Sunday 漏入**：版 SVG 0、印文字層 0、核心 SVG 3；英文家具 0；「下週日」0、「本週日」11、「finish line」0。結論：無缺陷。
- **P2 標題 STRADDLE**：PIL 右緣餘 1.5px；200 dpi 渲染：最右墨 x=3874，盒右緣 x=3879（奶油→紙色階 240,238,229 → 251,250,246），間隙 5.6 圖像 px = 2.7 SVG px。裁圖 `crops/p2-title-crop.png`；探針 `crops/pixel-probe-p2.py`。結論：無缺陷，觀察 O1。
- **P6 標籤縫**：PIL 盒間隙 0.6px；200 dpi 渲染：兩墨段間 5 圖像 px = 2.40 SVG px 背景。裁圖 `crops/p6-labels-crop.png`；探針 `crops/pixel-probe-p6.py`。結論：無缺陷，觀察 O2。

## G19 — 標題數實測

- 定義 A（`Flow.title`，32pt）：14；定義 B（+ `Flow.head`）：39；定義 C（+ 頁眉帶/展示標題/時間軸頭/金句頭/下期預告）：50。「56」三定義皆不符。

## G20 — KIT 交叉核對

- WEEKLY-KIT.md 宣稱值與本 proof2 實測逐一相符（總量、SHA、P7 幾何、P8 字號、occlusion、p8、freeze、奶油盒、boxtitle、STRADDLE、P6 間隙、P8 徽章、核心基線 SHA）。
- 惟一不一致：KIT「Proofread record — Web PDF」行載網 PDF 2,393,503 bytes（首建舊值）；交付為 2,409,973 bytes，KIT「Measured totals」已載正確值。KIT 內部陳舊數字，非版缺陷，交 K6/K7 收尾（觀察 O7）。

## G21 — 收工重驗（生產未動）

- 三交付文件 SHA 逐字節等於任務值；大小一致。
- 生產 8 SVG hash-only 比對開工基線：全同。
- 核心 8 SVG hash-only 比對開工基線：全同。
- 核心三 PDF SHA 重驗一致（印 `5ec35fe2…`、網 `1c0799ac…`、text.md `09e083e1…`）。
- `git status`：版目錄未追蹤（開工前即然）；本員未改生產任何文件；W43 修改為開工前已有的無關改動，未碰。
- 檔：`prod-hashes-after.txt`、`core-hashes-after.txt`、`prod-hashes-after-only.txt`、`core-hashes-after-only.txt`。
