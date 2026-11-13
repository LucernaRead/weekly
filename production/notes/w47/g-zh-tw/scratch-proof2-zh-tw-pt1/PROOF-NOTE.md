# PROOF-NOTE — 2026-W47 zh-tw-pt（繁體中文 × 葡萄牙語讀者，VOL.4）proof2

**結論 (a)：乾淨可定稿（zero issues）。** 獨立完整復校，未發現缺陷。

- 復校員：獨立 proof2（首次獨立復校，與重擴散報告無關，從頭驗）。
- 復校時間：2026-11-11（UTC 約 15:55 之後開工）。
- 工作目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-pt1/`（全部中間件、門禁日誌、渲染圖均在此；生產目錄只讀，未寫入、未 commit、未 push）。
- 探針：`git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0；scratch 真實寫文件 RC=0。TMPDIR 全程指向本 scratch 下 `tmp/`。

## 0. SHA 硬核對（開工前，三件全對）

| 件 | 字節 | SHA-256（實測） | 與任務給值 |
|---|---|---|---|
| 印刷 PDF `Lucerna-VOL4-PT.pdf` | 20,944,900 | `6302ea7c3cb5ba6d8bc7069a9bb69d0458da46f93bcad4462019c2320ff1b5d5` | 一致 |
| 網頁 PDF `Lucerna-VOL4-PT-web.pdf` | 2,412,857 | `4a257e9f33a988e88735e7c396ca73dfe9d3029b51ec21052bb698ef907804d3` | 一致 |
| text.md `2026-w47-zh-tw-pt.text.md` | 51,492 | `02387ce2dd5e9b7b0fa1d21ce35334f16a3e398d4e7dd73388645f6e174aafb2` | 一致 |

## 1. 門禁總表（全部實測，見 GATE-LOG.md）

| 門 | 結果 |
|---|---|
| checks.py | PASS（8 句 ×2、SIMP_ONLY_HITS []、P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]） |
| occlusion audit | selftest RC=0，flags 0 |
| p8 extract / compare | 150/150，CLEAN，missing=[]、extra=[]、keydiff=[]（驅動 gates.json 內 `"extra": "?"` 為已知取鍵小 bug，已直接讀 `p8-compare.json` 核實 extra=[]） |
| canonical creambox | 36 盒，負清除 0；各頁最小內清除 P1 18.8 / P2 15.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5；P7 工具盒 +40.5 / +12.5 / +14.0 |
| boxtitle | 36 盒，超框 0，最小標題右余 9.5px |
| PIL creambox | STRADDLE 3，CREAM-COVER 0，P7 最小清除 8.0px |
| 印/網 text layer | pdftotext -layout 字節相等（102,844 / 102,844），字符多重集差 0；本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、小雪 36/36、end point 0 |
| PDF 度量 | 8 頁、1462.5×2025 pt；P8 最小字號 9.75pt（印/網一致，恰 SOP §1.1 下限）、最大 34.5pt；P1 頂部字號 [147.0, 45.0, 27.0, 24.0] |
| keycheck | 填空鍵 54/54 出自正文；答案鍵 1–150 連續 |
| leak scan | deny 命中 0；唯一與核心共有的長 ASCII 串為選項行「A. 12:00 · B. 14:00 · C. 19:00」（構造共享，非洩漏） |
| abutting（P6 18:30/19:00） | 墨縫 0.6px（頒獎典禮墨右緣 990.8 → 夜間遊行墨左緣 991.4，與核心先例一致，無重疊） |
| freeze baseline | 8/8 字節一致；核心完整性 OK（8 個 SVG 重哈希未變）。Pillow 13.0.0（pt 要求 Pillow 13，符合 freeze guard） |
| freeze diff（核心 vs 本版） | 僅預期差異：英→葡講解層替換；新增 CJK 字符僅「葡萄牙」×9（P1 2 處、其餘各頁 1 處，即頁眉/頁腳「葡萄牙語講解」）；新增串無簡體字、無 deny 串；被刪的純 CJK 碎片（P1「拿下總冠軍，叫封王。」、P7 單字碎片、P8 作文範例兩段）均已在 pt 版 SVG 內逐一核實仍在，屬重分行，非內容丟失 |

## 2. 通讀（text.md 6,057 行全卷 + 交付 PDF 8 頁渲染目視）

- **13 條 Notas 全核**：日期/時間/數字逐條對正文無誤（14:00 遊行、19:00 夜間遊行最終場、5 米鹿魔、Xiaoxue 第 20 個節氣/冬天第 2 個、泡腳 10–15 分鐘、耶誕城 13 nov–27 dez・45 天・17:30–23:00 每半小時 5 分鐘、金馬 6–22 nov・587 部・10/1 公布・11 項・第 63 屆・紅毯 17:00・典禮 18:30・柯煒林主持、鋼雕 23 out–22 nov・21–22 nov 最後週末・SUPER SAFE 保險箱・林鴻育秀 85 歲、Méliès《月球之旅》1902、迪士尼 17 nov–3 jan・48 天・19 nov 新演出・音樂會 21–22 nov + 5–6 dez 共 4 場、爵士節 13–15/17–22/24 nov・Diana Krall 13 日・Cory Wong 15 日・Stacey Kent 17 日・Kenny G 24 日收尾、寶可夢 11 nov・10 米精靈球燈飾、P6 四件大事 14:00/17:00/18:30/19:00/鋼雕 20:00 閉館＋「一個人看不完，要取捨」）。
- **M1/M2**：終點 (linha de chegada)——非 finish line；記憶口訣順序入圍 → 星光大道（紅毯 17:00，典禮前）→ 典禮（頒獎）18:30，無 place 類措辭。
- **練習 Q1–150**：題號連續無缺（獨立提取 150 個獨立題號）；答案 1–150 逐條對題幹核實，全對（含算術：Q41 11/6–11/22 含首尾 17 天、Q42/Q85 17:00→18:30 為 1.5 小時、Q60 7×10=70 還差 30 滿 100、Q77 14+31+3=48 天、Q78 11/17–22 含首尾 6 天、Q99/Q128 14:00→19:00 為 5 小時、Q100 四件大事、Q127 100 U 幣換悠遊卡儲值金——正文 P4 有據）。
- **Q150 作文範例**：實測 142 字符（去空白），與 P8 鍵尾標註「142 caracteres」一致；題目要求 120～180 字，142 字在範圍內。
- **Latin 串全卷掃描**：482 處命中均為葡語講解/欄目標題/圖注/專有名詞（MUVIE、CINEMAS、TSNA、Georges Méliès、Diana Krall、Kenny G 等），正文無英文殘留。
- **目視**：交付印刷 PDF 渲染 8 頁聯絡表 + P7/P8 大圖 + 3 處 STRADDLE 裁切圖全部看過——無溢出、無重疊、無頁腳碰撞；P7 三欄＋工具盒＋金句條＋下期預告、P8 大測驗＋範例＋150 條答案鍵均在頁內。

## 3. STRADDLE 3 處——觀察項，非缺陷（按裁決規則）

| # | 位置 | 標題 | PIL 墨跡 / 奶油框右緣 | 超出 |
|---|---|---|---|---|
| 1 | P2 `p2-life.svg` | 耶誕城小檔　Ficha do Christmasland | 墨右 1900.0 / 框右 1862.0 | +38.0px |
| 2 | P3 `p3-culture.svg` | 金馬小表　Ficha dos Golden Horse | 墨右 1874.0 / 框右 1862.0 | +12.0px |
| 3 | P3 `p3-culture.svg` | 鋼雕閉幕行程　Último fim de semana | 墨右 1906.2 / 框右 1862.0 | +44.2px |

- **非回歸**：同一 PIL 掃描跑重擴散備份舊版（`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-pt/svg`），3 處坐標逐字相同（至 0.1px），舊版 boxtitle 亦同（36 盒、超框 0）。
- **交付 PDF 渲染裁決**：3 處裁切圖（2 倍渲染）均見標題字形完整、清晰可讀，伸出部分落在無邊框奶油框外的白紙上——無裁切、無墨水重疊、無可見邊框。符合任務裁決規則的觀察項條件，不判缺陷。
- 另：occlusion 0、CREAM-COVER 0、canonical creambox 全正，與之印證。

## 4. 已核實的非缺陷（任務事先說明，獨立複核確認）

- 「next Sunday」僅存於凍結核心（core `content12.py:37/:113`、`content34.py:127` 及核心 Notes 句）；本版印/網文字層「下週日」0 處、「本週日」11 處，pt 講解層均為「este domingo / Neste domingo」。凍結核心永不是缺陷。
- SIMP_ONLY：本版 checks 為 `SIMP_ONLY_HITS []`。任務所言 ['國','學'] 為 ja 版誤報，與 pt 版無關。
- 孤兒填空行 Q36/Q37/Q130：題幹與核心逐字一致（僅 Fill in→Completar），答案與核心一致（36 星光大道、37 保險箱、130 夜間），屬核心繼承觀察項。
- P6 18:30/19:00 墨縫 0.6px：與核心先例完全一致的發絲縫，無重疊。

## 5. 缺陷清單

無。

## 6. 文件索引（本 scratch）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- `gates.py`、`gtools/`（自重擴散 scratch 複製，僅改路徑指針向本 scratch）
- `gates/pt-proof2/`：`gates.json` 及全部門禁日誌（checks.log、occlusion*.log/json、p8-extract/compare.json、creambox.log/json、creambox-pil.log、boxtitle.log/json、fillin-check.log、freeze.log、freeze-diff.log/json、print.txt、web.txt、pdftotext-*.log、freeze-base/）
- `gates-run.log`（驅動總日誌）
- `old-pt/`：舊版備份 STRADDLE/boxtitle 對照掃描輸出；`old-pt-creambox-pil.log`、`old-pt-boxtitle.log`
- `render/`：`contact.png`（8 頁聯絡表）、`p1.png`–`p8.png`、`p7-big.png`、`p8-big.png`、`p2-straddle.png`、`p3-straddle-a.png`、`p3-straddle-b.png`
