# GATE-LOG — W47 core-zh-tw re-proof #3：fix5 後全套機械門獨立重跑記錄

- **復校對象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（fix5 交付狀態，未動）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
- **日誌目錄（絕對路徑）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-core-zh-tw3/`
- **時間**：2026-11-11 10:24–10:40 UTC（05:24–05:40 EST）
- **探針**：每次寫盤前 `git hash-object -w` rc=0。`/tmp` 實測僅 2%（12M/512M），仍全程
  `TMPDIR=<scratch>/tmp`，未寫 /tmp。
- **未重建交付物**：按任務紅線，未跑 run.py / render.py / webpdf.py / export（未重建、不改源）。
  freeze 門以 `freeze.py baseline`（副本重建進 scratch，不碰交付文件）+ 交付 SVG 的 SHA 直比雙重驗證（見 §6）。

## 0. 交付物（盤上實測，與任務指定值逐字一致）

- print `Lucerna-VOL4.pdf` 19,420,552 B / SHA `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`
- web `Lucerna-VOL4-web.pdf` 2,324,042 B（< 7 MB）/ SHA `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240`
- text `2026-w47-zh-tw-en.text.md` 49,798 B / SHA `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`
  （與 fix4 逐字節相同；與 KIT L53/L129 登記一致）
- 雙 PDF 各 8 頁、1462.5×2025 pt（pdfinfo + PyMuPDF 實測）

## 1. 文字層一致（print.txt / web.txt，pdftotext -layout）

- print 101,461 B；web 101,461 B（均 > 0，有文字層）。逐頁字符數雙版完全相同
  （-layout 模式；總字符 85,055 / 85,055）。
- 字符多重集差：print-only **0**；web-only **0**。
- `本週日` print/web 各 11×；`下週日` 各 0；`BABYMONSTER` 各 0；`取捨` 各 2×（正文 1 + P8 鍵 1）；
  `小雪` 各 36×；`夜間遊行` 各 25×；`finish line` 各 0；`end point` 各 1×；`台北演唱會` 各 0。
- **結論：文字層完整一致，PASS。**

## 2. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），乾淨對照沉默。
- 本版審計 rc=0：**0 flags**（`flag_count: 0`）。
- （註：首次誤以文件列表調用報 rc=2 usage error，屬調用錯誤而非門失敗；
  改按工具用法傳目錄 `svg` 後 rc=0。）
- **結論：PASS。**（注：本版無有邊框矩形，BOXTITLE 類空過；奶油底框見 §9 creambox 門。）

## 3. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（無簡體字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——與預期一致。

## 4. p8.py（p8-extract.log / p8-compare.log）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare --core-p8 svg/p8-test.svg --edition-p8 ../2026-w47-zh-tw-de/svg/p8-test.svg --total 150` rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
- **結論：PASS。**

## 5. 150 題逐題語義核對（keycheck，本復校人工全量 + 程式輔驗）

- text.md 6023 行逐行通讀：全部 150 鍵對題面、原文、圖表再驗算，無誤
  （含 Q41 17 天、Q42/Q85 1.5 小時、Q60 差 30、Q77 48 天、Q78 6 天、Q84/Q99/Q128 5 小時、
  Q99 鍵 5、Q100 鍵 4、Q144 A=11月22日、Q149 A=保暖、Q139–143 阿玲短文一致）。
- 程式輔驗：題號 keys 區 1–150 連續；分布 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 /
  P7 12 / P8 38；分級 A2 44 / B1 74 / B2 32（4 組配對折算後）；Q34 鍵在 text.md L5772 同文。
- 寫作範文 142 字符（去標點後 126），落在 120–180 字帶內。
- **結論：PASS。**

## 6. freeze（freeze-base.log / svg-hashes-delivered.txt）

- `baseline --build . --core-svg svg --out <scratch>/freeze-base` rc=0：
  **8/8 SVGs byte-identical**（重建產物與已交 SVG 逐字節相同；core integrity：
  運行前後 8 個已交 SVG 哈希不變）。——副本重建，不碰交付文件。
- freeze_direct：交付 8 個 SVG 的 SHA-256 與 fix5 `svg-hashes-delivered.txt` 逐頁直比，
  **8/8 相同**（p1 `cc70b39c…`、p2 `55378c70…`、p3 `1ef68658…`、p4 `ec781f9c…`、
  p5 `183e0bc4…`、p6 `51dafd84…`、p7 `839a8093…`、p8 `8e65cb3f…`）。
  與 fix4 比對：僅 p4-sport.svg 變化，其餘 7 頁與 fix4 逐字節相同。
- **結論：PASS。**

## 7. 彎撇／彎引號全掃（U+2018/U+2019/U+201C/U+201D，Python 按碼點計數，analysis.log）

- 源 `.py`、8 個 SVG、text.md 全掃：**0 命中**。PASS。
- 另：`松菸` text.md 5 處（皆 U+83F8 菸），`松煙` 0；`小雪` text.md 36；
  `夜間遊行` 25（源 26，第 26 處為折行拆分，見 PROOF-NOTE §7.3）；
  `end point` 1；`finish line` 0。
- 「·」59 處（text.md）：全部為選項分隔/外國人名/P6 圖例；SVG 59 處同分布
  （P5 12、P6 4、P8 43）。家具無結構性「·」。
- 簡體字獨立掃描（checks.py 同款字表）：text.md + 8 個 SVG **皆 0**。

## 8. §1.1 字體／配色／字號（PyMuPDF，analysis.log）

- 字體（雙 PDF）：刊頭 UnifrakturMaguntia（CairoFont-2-0 子集）147pt；拉丁 Newsreader；
  中文 Noto Serif CJK TC（標題/正文）／Noto Sans CJK TC（講解層）——符合 §1.1 字體表。
- 字號階梯實測：頭條 45pt、刊別 27pt、欄目條 34.5pt、次級標題 24pt、正文 18pt、
  練習題幹 16.5–16.88pt、欄目小字 12.75pt、講解層 11.25–13.5pt——皆在 §1.1 階梯內。
- P8 最小字號：print 與 web 雙 PDF 皆 **9.75pt**（= §1.1 下限）；P8 最大 34.5pt。
  P8 題幹 10.35pt 為 KIT 已披露的預披露偏差（見 PROOF-NOTE §7.5），不計缺陷。
- 紙色 #fbfaf6：本次獨立 get_drawings 實測，雙 PDF 各 **8/8** 頁全幅填充；
  SVG 內 #fbfaf6 rects 8 個。
- 金色系 fill（#b8860b/#d4af37/#c9a227/#8b4513/#a52a2a）：**0**；
  "gold" 子串 9 處皆為英文 "Golden Horse"（base64 數據先剝離後再驗），非顏色。
- analysis.log 與 fix5 的 diff 僅兩處非內容行（fitz FutureWarning 表頭 2 行 +
  末行 "ANALYSIS DONE"），字體/字號/配色/奶油框數值零差異。
- **結論：PASS**（除已披露的 P8 題幹字號偏差外）。

## 9. creambox 全版掃描（canonical + PIL 真墨雙重）

### 9a. canonical 工具 `hidden_files/w47/tools/creambox.py`（creambox.py / creambox.log）

- 36 個奶油底框（fill #f0eee5），每框 inside-only 末行基線清除量皆為正：
  P1 最小 18.8、P2 41.8、P3 15.8、P4 **9.8**（D4 盒，末行 `exercise?` 基線 1362.2，
  框底 1372.0，desc-clear +3.8）、P5 6.4、P6 19.9、P7 12.4。
- BELOW-WINDOW 行全部為 +37/+44px 的下一標題，無 +12..+18px 整行外溢特徵。
- P5 最小 desc-clear −0.4（`日` 字行，0.30×字號的保守下行估算所致）——真墨實測見 §9b，該行墨底在框內。
- **結論：PASS——無溢出。**

### 9b. PIL 真墨盒補充掃描（creambox-pil.py / creambox-pil.log，re-proof #2 同方法）

- 36 框；**STRADDLE 0，CREAM-COVER 0**。
- 各頁最小底距：P1 16.5、P2 37.1、P3 14.1、**P4 9.6**、P5 4.4、P6 17.1、P7 7.7——
  除 P4 由修前 −4.4→+9.6 外，其餘各頁與 re-proof #2 的 creambox.json 逐值一致，無連帶變化。
- **D4 獨立重測**：框 rect x=1439.5 y=1128 w=422.5 h=244（源 `content34.py:210` 同值），
  框底 1372.0；末行 `exercise?`（Noto Sans CJK TC 20px）PIL getbbox 墨底 **1362.2**
  （fix5 稱 1362.4，差 0.2px，量法差異），框底距 **+9.8px**（fix5 口徑 +9.6px），
  清除量 **+14.0px**；框下（x≥1439.5，y∈(1372,2500]）text 節點 0 個、rect 0 個，
  頁腳線 y=2596，距新框底 1224px——**零擠壓**。
- **結論：PASS——D4 已清除。**

## 10. boxtitle 全標題 text_w 實測（boxtitle.py / boxtitle.log）

- 36 框全量；標題／行右緣逾越 **0**；最小標題右邊距 26.2px（P2）、最小左邊距 18.0px；
  各頁最小右邊距：P1 61.8、P2 26.2、P3 47.5、P4 60.8、P5 47.8、P6 39.5、P7 107.2（px）。
- boxtitle.log 與 fix5 的同名日誌逐字相同（diff rc=0）。
- **結論：PASS。**

## 11. 日期星期（`date`，Asia/Taipei）

- 2026-11-16 週一、11-17 週二、11-19 週四、11-21 週六、11-22 週日、11-13 週五、
  12-27 週日、11-06 週五、10-01 週四、10-23 週五、11-11 週三、12-04 週五、
  12-05 週六、12-06 週日、2027-01-03 週日、11-24 週二、11-15 週日——
  與本期全部星期寫法一致。**PASS。**

## 12. 54 個填空鍵答案詞出自正文複核（fillin-check.log，check_fillin_keys.py）

- 方法：源 `.py` 解析全部 `"完成句子"` 調用得 54 鍵，逐鍵查是否出現於 text.md keys 區之前。
- 結果：**54/54**，缺失 []。其中「取捨」正文出現 1 次（D3 未回歸）。
- **結論：PASS。**

## 13. 目視（p4-d4-crop.png / p6-timeline-crop.png / cards p1–p8，本目錄 + 交付渲染圖）

- P4 你呢框（`p4-d4-crop.png`，原尺寸裁切 2× 放大）：`exercise?` 一行完整在奶油框內，
  框底下方有明顯餘量 ✓（D4 已清除）。
- P6 時間軸（`p6-timeline-crop.png`，2× 放大）：18:30 `頒獎典禮` 與 19:00 `夜間遊行`
  雙標籤間有髮絲縫、無重疊、各自對準其圓點；PIL 真墨量得墨距 **0.6px**（見 PROOF-NOTE §7.1），非缺陷。
- 8 版全頁逐版看過：除已清除的 D4 外無溢出、無重疊、無壓頁腳、圖片與出處俱全。
- P7 記憶句四行完整，`ceremony （頒獎）` 間有空格；M1 句 `終點 (end point)` 完整。
- **結論：8/8 版通過。**

## 14. ABSTRACT（SOP §9）

- `ABSTRACT.txt`：英文單行 379 字符，無 ASCII 雙引號；含 Lucerna、Traditional Chinese、
  A2、B2、150 exercises；所列主題皆為本期真實內容。**PASS。**

## 15. 防回退項

- D1：text.md / 雙 PDF 文字層 / 源 `.py` / 8 個 SVG，`本週日` 各 11、`下週日` 各 0——無回歸。
- D2：`BABYMONSTER` 0（源、text.md、雙 PDF 文字層、p5-youth.svg）；`台北演唱會` 0——無回歸。
- D3：`取捨` 源 2 處（文章 `content56.py:131` + 題目 `content56.py:184`）、text.md 2 處、
  雙 PDF 文字層各 2 次——無回歸。
- fix4 三句：`content7.py:52` 記憶句、`content7.py:18` (end point)、`content12.py:68` 末條——
  源、text.md、SVG、雙 PDF 文字層、卡片五重一致。
- Q34 鍵 `34. C — A Trip to the Moon was made in 1902.` 在 text.md L5772，與修前同行同文。
- W46 封王查證：`production/2026-w46/core-zh-tw/2026-w46-zh-tw-en.text.md` L966
  「封王：拿下總冠軍，叫封王」——P4「上週本報已經教過這個詞了」屬實。
- fix5 唯一改動核實：僅 `content34.py:210` 框高 230→244；僅 p4-sport.svg 變化
  （`182d9301…`→`ec781f9c…`），其餘 7 頁與 fix4 逐字節相同；text.md 與 fix4 逐字節相同。

## 總結

| 門 | 結果 |
|---|---|
| 交付物 SHA/尺寸 | 全符（§0） |
| occlusion_audit.py（自檢先過） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（本核心 vs zh-tw-de） | CLEAN，keydiff=[] |
| 150 題逐題語義核對 | 全數無誤 |
| freeze.py baseline --core-svg svg | 8/8 byte-identical |
| freeze_direct（交付 SVG SHA 直比 fix5） | 8/8 |
| checks.py | PASS（金句 8×2、簡體 0、圖表幾何一致） |
| print/web 文字層多重集差 | 0 / 0（-layout 模式） |
| U+2018/U+2019/U+201C/U+201D 全掃 | 0 |
| §1.1 字體/配色/字號 | PASS（紙 #fbfaf6 ×8，金 0；P8 鍵 9.75pt） |
| 日期星期（`date`） | 全數一致 |
| boxtitle 全標題 text_w 實測 | 36 框，逾越 0（與 fix5 日誌逐字相同） |
| creambox.py（canonical）全版掃描 | 36 框，inside-only 清除量皆正；D4 盒 +9.8 |
| creambox PIL 真墨補充掃描 | STRADDLE 0，CREAM-COVER 0；P4 最小底距 +9.6 |
| D4 獨立重測 | 框底 1372.0，墨底 1362.2，底距 +9.8，清除量 +14.0，框下 0 元素 |
| 54 填空鍵複核 | **54/54，缺失 []** |
| D1/D2/D3/fix4 回歸 | 本週日 11/11、下週日 0、BABYMONSTER 0、取捨 2/2、三句五重一致 |
| 雙 PDF 逐版目視 | 8/8 看過；D4 目視確認已清除，其餘通過 |
| 外部事實網上核實 | 本次 fresh 搜尋 7 組全數一致（見 PROOF-NOTE §4） |
| ABSTRACT（SOP §9） | PASS（英文單行，379 字符，無 ASCII 雙引號） |
| 內容全量復校 | **零問題，可定稿（verdict (a)）** |

## 未做事項（按任務範圍）

- 未改任何源文件、未重建交付物、未 commit、未 push、未動其他家庭、未派 subagent。
- 未跑 insert.py、lint --write；未做任何 git 寫操作（除探針 `hash-object` 外）。
