# GATE-LOG — 2026-W47 zh-tw-pt proof2

驅動：本 scratch 內 `gates.py pt proof2`（自重擴散 scratch 複製，僅改路徑指針向本 scratch；`gtools/` 同）。運行環境：倉庫 venv `tools/venv/bin/python`（Pillow 13.0.0，pt 要求 Pillow 13，freeze guard 通過；FreeType 2.14.3）。TMPDIR=`<scratch>/tmp`。總日誌：`gates-run.log`（RC=0）。各門原始輸出：`gates/pt-proof2/`。

## 0. SHA 實測（開工前）

- 印刷 PDF `Lucerna-VOL4-PT.pdf`：20,944,900 B / `6302ea7c3cb5ba6d8bc7069a9bb69d0458da46f93bcad4462019c2320ff1b5d5` ✓
- 網頁 PDF `Lucerna-VOL4-PT-web.pdf`：2,412,857 B / `4a257e9f33a988e88735e7c396ca73dfe9d3029b51ec21052bb698ef907804d3` ✓
- text.md `2026-w47-zh-tw-pt.text.md`：51,492 B / `02387ce2dd5e9b7b0fa1d21ce35334f16a3e398d4e7dd73388645f6e174aafb2` ✓
- 三值與任務給值逐字節一致。SVG SHA 見 `gates/pt-proof2/gates.json` 的 `files.svg_sha256`。

## 1. checks.py — PASS（rc=0，`CHECKS PASS`）

```
PHRASE 2 封王遊行從天母棒球場出發
PHRASE 2 夜間遊行晚上7點，最後一場不要錯過
PHRASE 2 小雪之後，天氣一天比一天冷
PHRASE 2 主燈秀每半小時一次，每次5分鐘
PHRASE 2 頒獎典禮晚上6點30分開始
PHRASE 2 保險箱裡，裝的是高雄的勞動記憶
PHRASE 2 穿上紅色衣服，一起上街為龍隊喝采
PHRASE 2 迪士尼聖誕，從11月17日開始
SIMP_ONLY_HITS []
CHART p4 [90.0, 450.0, 900.0] expect [90.0, 450.0, 900.0]
CHART p6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] expect [188.0, 695.21, 948.82, 1033.36, 1202.43]
CHECKS PASS
```

## 2. occlusion audit — 0 flags（selftest rc=0）

- `occlusion-selftest.log`：自測 6 類 planted 均觸發（由工具自帶斷言保證，rc=0）。
- `occlusion.json`：`flag_count` 0，rc=0。

## 3. p8 extract + compare --total 150 — CLEAN

- extract：`noted_set` 150/150。
- compare（顯式 `--core-p8` / `--edition-p8`）：`status` CLEAN，`core_count` 150，`edition_count` 150，`missing` []，`extra` []，`uncertain` []，`keydiff` []。
- 註：驅動 `gates.json` 內 `"extra": "?"` 為已知取鍵小 bug（讀了不存在的 `extra_count`），已直接讀 `p8-compare.json` 核實 `extra: []`。

## 4. canonical creambox 全版掃描 — 36 盒，負清除 0

- 盒數 36（P1 5 / P2 6 / P3 7 / P4 4 / P5 8 / P6 3 / P7 3）。
- 最小內清除（每頁）：P1 18.8、P2 15.8、P3 15.8、P4 35.8、P5 6.4、P6 19.9、P7 12.5。
- P7 工具盒：+40.5（"hora: 12 vezes, das 17:30 às 23:00."）、+12.5（"mais Y. Crie sua própria frase com ela."）、+14.0（"continua aberto."）。
- PIL 補充掃描 P7 最小清除 8.0px；各頁 PIL 最小底清除：P1 16.5、P2 11.3、P3 14.1、P4 31.3、P5 4.4、P6 17.1、P7 8.0。

## 5. boxtitle — 36 盒，超框 0，最小標題右余 9.5px

- `boxes measured: 36`，`title/line overruns past box right edge: 0`。
- 各頁最小右余：P1 26.2、P2 41.2、P3 20.5、P4 25.0、P5 9.5、P6 34.5（整體最小 9.5px，P5）。

## 6. PIL creambox — STRADDLE 3，CREAM-COVER 0

```
STRADDLE {'page': 'p2-life.svg', 'text': '耶誕城小檔　Ficha do Christmasland', 'ink': [1461.5, 1452.5, 1900.0, 1476.5], 'cream': [1439.5, 1430.0, 1862.0, 1890.0]}
STRADDLE {'page': 'p3-culture.svg', 'text': '金馬小表　Ficha dos Golden Horse', 'ink': [1461.5, 671.8, 1874.0, 696.1], 'cream': [1439.5, 649.6, 1862.0, 1119.6]}
STRADDLE {'page': 'p3-culture.svg', 'text': '鋼雕閉幕行程　Último fim de semana', 'ink': [1461.5, 1424.3, 1906.2, 1452.1], 'cream': [1439.5, 1405.6, 1862.0, 1855.6]}
CREAM-COVER flags: 0
```

舊版對照（同一掃描跑重擴散備份 `backup/2026-w47-zh-tw-pt/svg`，`old-pt-creambox-pil.log`）：STRADDLE 3，3 處坐標逐字相同（至 0.1px）；CREAM-COVER 0；舊版 boxtitle 36 盒、超框 0（`old-pt-boxtitle.log`）。**非回歸。**
交付 PDF 渲染裁決（`render/p2-straddle.png`、`p3-straddle-a.png`、`p3-straddle-b.png`，2 倍渲染）：3 處標題字形完整可讀，伸出部分落在無邊框奶油框外的白紙上，無裁切、無墨水重疊、無可見邊框。按裁決規則為觀察項，非缺陷。

## 7. 印/網 text layer 比對 — 字符多重集差 0

- `pdftotext -layout`：印 102,844 B / 網 102,844 B，差 0 字符。
- 計數（印/網一致）：本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、小雪 36/36、end point 0/0。

## 8. PDF 度量（PyMuPDF）

- 印/網均 8 頁、1462.5×2025 pt。
- P8 字號：最小 9.75pt、最大 34.5pt（印/網一致；最小恰 SOP §1.1 下限）。
- P1 頂部字號：[147.0, 45.0, 27.0, 24.0]。
- 字節：印 20,944,900 / 網 2,412,857（與 §0 SHA 核對一致）。

## 9. keycheck — 填空鍵 54/54，答案鍵 1–150 連續

- `check_fillin_keys.py`：填空鍵總數 54，MISS 行 0。
- text.md 答案區獨立提取：題號 1–150 連續，無缺無重。
- 練習題號獨立提取：150 個獨立題號，1–150 全齊。

## 10. leak scan — deny 0

- DENY 串（next Sunday / Next Sunday / finish line / "the place it happens" / "The ceremony is at the Taipei Music Center." / "Xiaoxue is Nov 22." / "Four big events fall on the same Sunday." / "Collecting points is 集點." / "Memory trick: learn 入圍 first, then the ceremony" / 遊行長串）：命中 0。
- 與核心共有的長 ASCII 串：僅「A. 12:00 · B. 14:00 · C. 19:00」（Q140 選項行，構造共享）。

## 11. abutting（P6 18:30/19:00）— 墨縫 0.6px

- 「頒獎典禮」墨盒 [906.8, 955.8, 990.8, 977.5]；「夜間遊行」墨盒 [991.4, 955.8, 1075.4, 976.2]；縫 0.6px，與核心先例一致，無重疊。

## 12. freeze — baseline 8/8；diff 僅預期差異

- baseline（`--core-svg svg`，重建僅在 scratch 副本內）：`baseline: 8/8 SVGs byte-identical`，rc=0；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
- diff（core-svg vs edition-svg，`freeze-diff.log/json`）：每頁 +/− 串數 P1 25/25、P2 41/39、P3 50/47、P4 39/38、P5 49/45、P6 34/33、P7 113/108、P8 189/187；新增 CJK 字符合計 27，僅「葡/萄/牙」各 9（頁眉頁腳「葡萄牙語講解」）；新增串掃描：簡體字 0、deny 串 0；被刪純 CJK 碎片已在 pt 版 SVG 內逐一核實仍在（重分行，非丟失）。

## 13. 通讀與目視（獨立復校，非法門禁複述）

- text.md 6,057 行：13 條 Notas 逐條核對日期/時間/數字無誤；M1 終點 (linha de chegada)、M2 順序與時間無誤；Q1–150 題幹與答案逐條核對無誤（含全部算術題重算）；Q150 範例實測 142 字符，與標註一致；Latin 串全卷掃描 482 處均為葡語層/專有名詞，無英文殘留。
- 交付 PDF 渲染：8 頁聯絡表（`render/contact.png`）＋ P7/P8 大圖（`render/p7-big.png`、`p8-big.png`）＋ 3 處 STRADDLE 裁切圖全部目視，無溢出、無重疊、無頁腳碰撞。
