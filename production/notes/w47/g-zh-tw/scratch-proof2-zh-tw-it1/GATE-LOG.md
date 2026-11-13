# GATE-LOG — W47 zh-tw-it proof2（重擴散新版）

- 版：`2026-w47-zh-tw-it`（繁體中文 × 意大利語講解），重擴散新版
- 執行：2026-11-11 ~20:16–20:45 UTC；`PYTHONDONTWRITEBYTECODE=1` 全程；`TMPDIR=<scratch>/tmp`
- 工作區：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-it1/`
- 原則：生产只读。run.py/render.py 在 scratch 副本 `build/it/` 內重跑；web PDF 未重渲染（字节不可复现），只比文字层；freeze baseline 在 scratch 副本上跑。
- 門驅動：`gates-driver.py`（重擴散 `gates.py` 的拷貝，路徑指向本 scratch；freeze 一門改在 `build/it` 內跑；p8 extra 字段取鍵小 bug 沿用——實值另見 `p8-compare.json` 的 `extra: []` / `extra_count: 0`）。
- 匯總 JSON：`gates/it-proof2/gates.json`

## 逐門結果

| # | 門 | 結果 | 實測值 / 證據 |
|---|---|---|---|
| 1 | 探針（磁碟可寫） | PASS | `git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0；scratch 真實寫文件 RC=0（`probe.txt`） |
| 2 | 三 SHA 核對 | PASS | 印 5594005aae1b2ff3b69ae37edf191dc482f2c3773b29a1cdc75c72ce5b485ce9 / 19,420,437 B；網 a0d80c26bdc7c8eb6029af991c4d14e8af966f0e3f6d3a066f74f98bf220d0a5 / 2,323,037 B；文 48e04f1540a9b6bcf292f9163af32707ac2ba54bcd91b18a127f45903dc12ba7 / 51,685 B；開工與終驗一致；KIT 所載一致。`gates/delivered-hashes.txt` |
| 3 | run.py | PASS RC=0 | TOTAL 150；A2 44 / B1 74 / B2 32；分頁 10/18/18/18/18/18/12/38；單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；FLOW OVERFLOW 0；HEAD TOO WIDE 0；無警告。P7 col3 1823.3、teaser 2577.3（頁腳規則 2596，餘 18.7px）；P8 writing strip 1280.2；MODEL chars 142。`gates/run.log` |
| 4 | SVG 重建 8/8 字節一致 | PASS | scratch 重跑 run.py 後 8 個 SVG 的 SHA-256 與交付逐一相同（p1 4ed936c2…、p2 ec470f0c…、p3 eca7b6e8…、p4 7ffa59f7…、p5 41823b2c…、p6 cfcae666…、p7 61a2f200…、p8 bd19e134…）。`gates/rebuilt-svg-hashes.txt` |
| 5 | 重渲印 PDF 與交付逐字節相同 | PASS | scratch render.py RC=0，重渲 `Lucerna-VOL4-IT.pdf` 19,420,437 B，SHA `5594005a…` = 交付值。`gates/render.log` |
| 6 | checks.py | PASS | `CHECKS PASS`；8 句各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]。`gates/it-proof2/checks.log` |
| 7 | occlusion 審計 | PASS 0 flags | selftest RC=0（6 類 planted 全觸發，clean 對照靜默）；audit RC=0，flag_count 0。`gates/it-proof2/occlusion-selftest.log`、`occlusion.json` |
| 8 | freeze baseline | PASS 8/8 | `baseline: 8/8 SVGs byte-identical`；core integrity：shipped core SVGs unchanged。`gates/it-proof2/freeze.log` |
| 9 | freeze diff（--strict-cjk） | RC=1，裁定非缺陷 | 唯一新增 CJK = 「意大利」×9（27 字），來源為每頁頁腳 + P1 badge 的家具「意大利語講解」（核心為「英語講解」）。其餘 added 均為意大利語講解層；表面缺失句為 P1 第 6 題填空切分（見 PROOF-NOTE O2）。`gates/freeze-diff.log`、`freeze-diff.json` |
| 10 | 奶油盒 canonical 全版掃描 | PASS | 36 盒；負內清除 0；分頁最小內清除 P1 18.8 / P2 41.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5（P8 無盒）；P7 工具盒 +40.5 / +12.5 / +14.0（desc-clear +34.7 / +6.5 / +8.0）。`gates/it-proof2/creambox.log` |
| 11 | 奶油盒 PIL 真墨掃 | 見 O1 | STRADDLE 2（P1「本週一詞　Parola della settimana」+0.8px PIL／+0.4px PDF 渲染；P2「耶誕城小檔　Scheda Christmasland」+24.5px PIL／+22.5px PDF 渲染）；CREAM-COVER 0；P7 最小底清除 9.5px。裁決見 PROOF-NOTE O1（字形未裁、無重叠、無回歸 → 觀察）。`gates/it-proof2/creambox-pil.log`、`gates/crop-p1-straddle-marked.png`、`gates/crop-p2-straddle-marked.png` |
| 12 | boxtitle | PASS | 36 盒；標題/行超框 0；最小標題右餘 13.8px（P3）；分頁標題數 5/6/7/4/8/3/3/0——「56 titles」為幻數，本版實測 36。`gates/it-proof2/boxtitle.log`、`boxtitle.json` |
| 13 | spill 掃 | PASS 0 | occlusion EDGE 0；全部 flow 終值在底線內（P7-b1 1568 vs nominal 1560 為 P7 欄佈局既有值，與舊版一致，occlusion 0、目視乾淨）；無字形出頁邊。`gates/run.log` |
| 14 | 孤兒掃 | PASS | 逐版目視 + flow 終值審核：無孤兒頭/行；P5 首篇末行跨欄為 KIT 已載常規報紙流（與核心一致）。 |
| 15 | p8 extract | PASS 150/150 | noted set = 150 of 150。`gates/it-proof2/p8-extract.json` |
| 16 | p8 compare（vs 核心，顯式 --core-p8/--edition-p8） | PASS CLEAN | status CLEAN；missing=[]、extra=[]、extra_count=0、uncertain=[]、keydiff=[]（驅動 JSON 中 `extra: "?"` 為取鍵小 bug，實值見 `p8-compare.json`）。`gates/it-proof2/p8-compare.json` |
| 17 | 印/網文字層比對 | PASS | -layout：印/網逐字節相同（111,245 B 雙向）；plain pdftotext 印 48,087 B / 網 48,088 B，多重集差恰 1 個 `\n`（run-boundary 空白 artifact，與 KIT 記載一致，無字符缺失）；計數印/網一致：本週日 11、下週日 0、BABYMONSTER 0、取捨 2、小雪 36、end point 0。`gates/it-proof2/print.txt`、`web.txt`、`gates/plain-print.txt`、`plain-web.txt` |
| 18 | PDF 度量 | PASS | 8 頁、1462.5×2025 pt（印/網一致）；P8 最小字號 **9.75pt**（印/網一致，恰 SOP §1.1 下限）、最大 34.5pt；P1 頂部字號 [147.0, 45.0, 27.0, 24.0]；網 PDF 2,323,037 B < 7 MB。`gates/it-proof2/gates.json` → pdf |
| 19 | keycheck（填空鍵 + 連續性） | PASS | 填空鍵 54/54 出自正文、缺失 0；答案鍵 1–150 連續（150/150）。`gates/it-proof2/fillin-check.log` |
| 20 | leak 掃 | PASS 0 | deny 命中 0（"next Sunday"/"Next Sunday"/"finish line"/6 條英文 key note 全部 0）；唯一與核心共有的長 ASCII 串為選項行「A. 12:00 · B. 14:00 · C. 19:00」（構造共享，非泄漏）。text.md grep 英文殘留 0。 |
| 21 | P6 18:30/19:00 墨縫 | PASS 0.6px | 「頒獎典禮」墨右緣 990.8、「夜間遊行」墨左緣 991.4，縫 0.6px（與核心先例一致的發絲縫，無重叠）。 |
| 22 | P8 最小字號 ≥9.75pt | PASS | 9.75pt（印/網一致，見 #18）。 |
| 23 | §1.1 | PASS | 紙 #fbfaf6 ×8 頁；墨 #302c28、說明 #6f675d、徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f；鵝黃 #f6e08e（SOP 允許色，書衣綠上副標題）×7；金/紅褐 0；無雙線外框；字體 Newsreader 1050 / Noto Serif CJK TC 1318 / Noto Sans CJK TC 746 / UnifrakturMaguntia 1（刊頭）；✗ 用 DejaVu Sans fallback（P7 診所 3 處，與核心同制）；VOL.4×10、VOL.5×1（下期預告）、VOL.3×2（讀者園地延期披露，歷史引用）；頁腳 `Lucerna　繁體中文週報 VOL.4　繁體中文正文　意大利語講解`、頁碼行 `Pagina N di 8`。 |
| 24 | 日期星期全驗 | PASS | `date -d`（America/Toronto）：11/16 週一、11/17 週二、11/19 週四、11/21 週六、11/22 週日、11/13 週五、12/27 週日；刊期 2026年11月16日至11月22日 ✓；P2 日曆逐項對上；小雪倒數 6 天 ✓；耶誕城 45 天、迪士尼 48 天、金馬影展 17 天含首尾均驗算通過。 |
| 25 | KIT §1 三 SHA 與盤上一致 | PASS | KIT「Measured totals」+ Re-fan-out 節所載三 SHA/字節與實測一致；P7 幾何（col3 1823.3、teaser 2577.3）、P8 9.75pt、文字層 48,087/48,088 均與實測一致。 |
| 26 | 目視（8 版逐版） | PASS | 生產 `cards/` p1–p8 全部看過：無溢出、無重叠、無頁腳碰撞、圖片/署名位置確認；P4「Parole del baseball」折行、P5 跨欄為 KIT 已載非缺陷；P2「泡腳10」疑似缺「1」經像素實測推翻（見 PROOF-NOTE §8.3）。 |
| 27 | text.md / ABSTRACT | PASS | text.md H1 `VOL.4 · Testi in cinese tradizionale · Spiegazioni in italiano`；150 題號齊全；英文殘留 0；ABSTRACT.txt 單行、無 ASCII 雙引號、意大利語、含真實主題 + A2–B2 + 150 esercizi。 |

## 未決項回應（重擴散報告 §7）

1. 英文源 key「next Sunday」未改：本版無影響——意大利語 D1 值全部為「questa domenica」，leak 掃描 0 命中。改英文 key 屬核心範圍，不在本版裁定內。
2. 雙語小檔標題 STRADDLE 2：本輪實測裁定為觀察（PROOF-NOTE O1），非缺陷、非回歸。
3. KIT K6/K7：另派的文档收尾，不屬本輪。

## 生產未動證明

- 終驗重算三 SHA 與開工一致（見 #2）；`git status` 顯示該目錄為未入倉新目錄（`??`，開工前已然），本輪未寫入任何生產文件。
