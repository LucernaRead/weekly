# GATE-LOG — W47 core-zh-tw re-proof #2：fix3 + fix4 後全套機械門獨立重跑記錄

- **復校對象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（fix4 交付狀態，未動）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
- **日誌目錄（絕對路徑）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-core-zh-tw2/`
- **時間**：2026-11-11 09:57–10:09 UTC（04:57–05:09 EST）
- **探針**：每次寫盤前 `git hash-object -w` rc=0。`/tmp` 實測僅 2%，仍全程 `TMPDIR=<scratch>/tmp`，未寫 /tmp。
- **未重建交付物**：按任務紅線，未跑 run.py / render.py / webpdf.py / export（未重建、不改源）。
  freeze 門以 `freeze.py baseline`（副本重建進 scratch，不碰交付文件）+ 交付 SVG 的 SHA 直比雙重驗證（見 §6）。

## 0. 交付物（盤上實測，與任務指定值逐字一致）

- print `Lucerna-VOL4.pdf` 19,420,551 B / SHA `97e896947fba550a0e4dd496e093a2cbafef88ed5cd0398052a3508aa77f11b0`
- web `Lucerna-VOL4-web.pdf` 2,324,051 B（< 7 MB）/ SHA `121cba14278ef1af117eff324b4ac9c2ec6837e0564186c3d91bd98148cd8d62`
- text `2026-w47-zh-tw-en.text.md` 49,798 B / SHA `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`
  （與 KIT L53/L129 登記一致）
- 雙 PDF 各 8 頁、1462.5×2025 pt（pdfinfo + PyMuPDF 實測）

## 1. 文字層一致（print.txt / web.txt，pdftotext -layout）

- print 101,461 B；web 101,461 B（均 > 0，有文字層）。逐頁字符數雙版完全相同
  （-layout 模式；与 fix4 记录的 P1 7909 / P2 9239 / P3 10806 / P4 7612 / P5 11268 / P6 8525 / P7 11477 / P8 18211 一致）。
- 字符多重集差：print-only **0**；web-only **0**。
- `本週日` print/web 各 11×；`下週日` 各 0；`BABYMONSTER` 各 0；`取捨` 各 2×（正文 1 + P8 鍵 1）；
  `小雪` 各 36×；`夜間遊行` 各 25×；`finish line` 各 0；`end point` 各 1×。
- **結論：文字層完整一致，PASS。**

## 2. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），乾淨對照沉默。
- 本版審計 rc=0：**0 flags**（`flag_count: 0`）。
- **結論：PASS。**（注：本版無有邊框矩形，BOXTITLE 類空過；奶油底框見 §9 creambox 門。）

## 3. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（無簡體字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——與預期一致。

## 4. p8.py（p8-extract.log / p8-compare.log/.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare --core-p8 svg/p8-test.svg --edition-p8 ../2026-w47-zh-tw-de/svg/p8-test.svg --total 150` rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
  （注：首次誤用 `--core` 旗標報錯 rc=2，屬調用錯誤而非門失敗；改用 `--core-p8/--edition-p8 --total 150` 後 rc=0。）
- **結論：PASS。**

## 5. 150 題逐題語義核對（keycheck，本復校人工全量）

- text.md 6023 行逐行通讀：全部 150 鍵對題面、原文、圖表再驗算，無誤
  （含 Q41 17 天、Q42/Q85 1.5 小時、Q60 差 30、Q77 48 天、Q78 6 天、Q84/Q99/Q128 5 小時、
  Q99 鍵 5、Q100 鍵 4、Q144 A=11月22日、Q139–143 阿玲短文一致）。
- 寫作範文 142 字符（去標點後 126），落在 120–180 字帶內。
- **結論：PASS。**

## 6. freeze（freeze-base.log / svg-hashes-delivered.txt）

- `baseline --build . --core-svg svg --out <scratch>/freeze-base` rc=0：
  **8/8 SVGs byte-identical**（重建產物與已交 SVG 逐字節相同；core integrity：
  運行前後 8 個已交 SVG 哈希不變）。——副本重建，不碰交付文件。
- freeze_direct：交付 8 個 SVG 的 SHA-256 與 fix4 `svg-hashes-after-run.txt` 逐頁直比，
  **8/8 相同**（p1 `cc70b39c…`、p2 `55378c70…`、p3 `1ef68658…`、p4 `182d9301…`、
  p5 `183e0bc4…`、p6 `51dafd84…`、p7 `839a8093…`、p8 `8e65cb3f…`）。
  與 fix3 比對：僅 p1-front.svg 與 p7-lang.svg 變化，其餘 6 頁與 fix3 逐字節相同。
- **結論：PASS。**

## 7. 彎撇／彎引號全掃（U+2018/U+2019/U+201C/U+201D，Python 按碼點計數，analysis.log）

- 源 `.py`、8 個 SVG、text.md 全掃：**0 命中**。PASS。
- 另：`松菸` text.md 5 處（皆 U+83F8 菸），`松煙` 0；`小雪` text.md 36（正文 32 + keys 區 4）；
  `夜間遊行` 25；`end point` 1；`finish line` 0。

## 8. §1.1 字體／配色／字號（PyMuPDF，analysis.log）

- 字體（雙 PDF）：刊頭 UnifrakturMaguntia（CairoFont-2-0 子集）147pt；拉丁 Newsreader；
  中文 Noto Serif CJK TC（標題/正文）／Noto Sans CJK TC（講解層）——符合 §1.1 字體表。
- 字號階梯實測：頭條 45pt、刊別 27pt、欄目條 34.5pt、次級標題 24pt、正文 18pt、
  練習題幹 16.5–16.88pt、欄目小字 12.75pt、講解層 11.25–13.5pt——皆在 §1.1 階梯內。
- P8 最小字號：print 與 web 雙 PDF 皆 **9.75pt**（= §1.1 下限）；P8 最大 34.5pt。
  P8 題幹 10.35pt 為 KIT 已披露的預披露偏差（見 PROOF-NOTE §7 第 1 條），不計缺陷。
- 紙色 #fbfaf6：雙 PDF 各 8 頁全幅填充（get_drawings 實測 8/8；渲染像素 (251,249,246)，
  1 階舍入差，矢量值為準）。
- 金色系 fill（#b8860b/#d4af37/#c9a227/#8b4513/#a52a2a）：**0**；
  "gold" 子串 9 處皆為英文 "Golden"（Golden Horse）或字體子集隨機 ID，非顏色。
- **結論：PASS**（除已披露的 P8 題幹字號偏差外）。

## 9. creambox.py 全版掃描（creambox.py / creambox.log / creambox.json，本目錄新寫補充工具）

- 方法：復用 `tools/occlusion_audit.py` 的真墨盒解析（PIL＋原字體）；
  36 個奶油底框（fill #f0eee5，SOP §1.1 側欄淺底）逐框核查：
  (a) STRADDLE——墨盒跨框邊（半入半出）；(b) CLEARANCE——框內文字墨盒至四邊的最小距離；
  (c) CREAM-COVER——後繪奶油矩形蓋字 ≥30%。
- 結果：36 框；**STRADDLE 1 處**（見下）；CREAM-COVER 0。
  - P1：5 框，最小底距 16.5px；P2：6 框，37.1px；P3：7 框，14.1px；
    P4：4 框，17.1px（不含溢出行）；P5：8 框，4.4px（迪士尼小檔框，框內）；
    P6：3 框，17.1px；P7：3 框，底距 40.3 / 7.7 / 9.2px（左 22.0/21.8/22.0、
    右 24.5/27.0/13.5、上 22.0/22.2/22.2——「P7 工具盒清除量」如數）。
- **STRADDLE 唯一命中（缺陷 D4，見 PROOF-NOTE §6）**：
  p4-sport.svg，文字 `exercise?` 墨盒 [1461.5, 1346.7, 1546.0, 1362.4]，
  奶油框 [1439.5, 1128.0, 1862.0, 1358.0]，溢出框底 4.4px；
  源頭 `content34.py:210`（框高 230px）；裁切圖 `p4-straddle-crop-big.png` 目視確認。
- **結論：FAIL——1 處 STRADDLE（D4，輕微）。**

## 10. boxtitle 全標題 text_w 實測（boxtitle.py / boxtitle.log / boxtitle.json，本目錄新寫補充工具）

- 方法：同上真墨盒；每框（本版 36 個皆為奶油底框——全版無有邊框矩形，
  另核實 stroked rects 8 頁皆 0）取首行標題，量墨寬 vs 框寬、左右邊距，
  以及框內最寬行的右緣逾越量。
- 結果：36 框全量；標題／行右緣逾越 **0**；最小標題右邊距 26.2px（P2）、
  最小左邊距 18.0px；各頁最小右邊距：P1 61.8、P2 26.2、P3 47.5、P4 60.8、
  P5 47.8、P6 39.5、P7 107.2（px）。
- **結論：PASS。**

## 11. 日期星期（`date`，Asia/Taipei）

- 2026-11-16 週一、11-17 週二、11-19 週四、11-21 週六、11-22 週日、11-13 週五、
  12-27 週日、11-06 週五、10-01 週四、10-23 週五、11-11 週三、12-04 週五、
  12-05 週六、12-06 週日、2027-01-03 週日、11-24 週二、11-15 週日——
  與本期全部星期寫法一致。**PASS。**

## 12. 54 個填空鍵答案詞出自正文複核（fillin-check.log，check_fillin_keys.py，fix3 方法重跑）

- 方法：源 `.py` 解析全部 `"完成句子"` 調用得 54 鍵，逐鍵查是否出現於 text.md keys 區之前。
- 結果：**54/54**，缺失 []。其中「取捨」正文出現 1 次（D3 未回歸）。
- **結論：PASS。**

## 13. 目視（p1-weekbox-crop.png / p7-memory-crop.png / p7-m1-crop.png / p4-straddle-crop-big.png / view-p*.png，本目錄）

- P1 本週日框：末條「本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行」兩行完整在框內 ✓。
- P7 記憶句：四行完整，`ceremony （頒獎）` 間有空格 ✓。
- P7 M1 句：`終點 (end point)` 完整 ✓。
- P4 你呢框：末行 `exercise?` 壓在框底邊界上，下半字形落在白紙上 ✗（D4）。
- 8 版全頁縮圖逐版看過：除 D4 外無溢出、無重疊、無壓頁腳、圖片與出處俱全。
- **結論：7/8 版通過；P4 一處版式溢出（D4）。**

## 14. 防回退項

- D1：text.md / 雙 PDF 文字層 `本週日` 各 11、`下週日` 0——無回歸。
- D2：`BABYMONSTER` 0（源、text.md、雙 PDF 文字層、p5-youth.svg）——無回歸。
- D3：`取捨` 源 2 處（文章 L131 + 題目 L184）、text.md 2 處、雙 PDF 文字層各 2 次——無回歸。
- fix4 三句：`content7.py:52` 記憶句、`content7.py:18` (end point)、`content12.py:68` 末條——
  源、text.md、SVG、雙 PDF 文字層、裁切圖五重一致。
- Q34 鍵 `34. C — A Trip to the Moon was made in 1902.` 在 text.md keys 區仍為 L5772，與修前同行同文。
- W46 封王查證：`production/2026-w46/core-zh-tw/2026-w46-zh-tw-en.text.md` L966
  「封王：拿下總冠軍，叫封王」——P4「上週本報已經教過這個詞了」屬實。

## 總結

| 門 | 結果 |
|---|---|
| 交付物 SHA/尺寸 | 全符（§0） |
| occlusion_audit.py（自檢先過） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（本核心 vs zh-tw-de） | CLEAN，keydiff=[] |
| 150 題逐題語義核對 | 全數無誤 |
| freeze.py baseline | 8/8 byte-identical |
| freeze_direct（交付 SVG SHA 直比 fix4） | 8/8 |
| checks.py | PASS（金句 8×2、簡體 0、圖表幾何一致） |
| print/web 文字層多重集差 | 0 / 0（-layout 模式） |
| U+2018/U+2019/U+201C/U+201D 全掃 | 0 |
| §1.1 字體/配色/字號 | PASS（紙 #fbfaf6 ×8，金 0；P8 鍵 9.75pt） |
| 日期星期（`date`） | 全數一致 |
| boxtitle 全標題 text_w 實測 | 36 框，逾越 0 |
| creambox.py 全版掃描 | **FAIL：STRADDLE 1 處（D4，P4 你呢框末行溢出 4.4px）** |
| 54 填空鍵複核 | **54/54，缺失 []** |
| D1/D2/D3/fix4 回歸 | 本週日 11/11、下週日 0、BABYMONSTER 0、取捨 2/2、三句五重一致 |
| 雙 PDF 逐版目視 | 8/8 看過；P4 一處溢出（D4），其餘通過 |
| 外部事實網上核實 | 15 組事實逐項一致（見 PROOF-NOTE §5） |
| 內容全量復校 | **1 條輕微缺陷 D4（P4 奶油框溢出），見 PROOF-NOTE §6** |

## 未做事項（按任務範圍）

- 未改任何源文件、未重建交付物、未 commit、未 push、未動其他家庭、未派 subagent。
- 未跑 insert.py、lint --write；未做任何 git 寫操作（除探針 `hash-object` 外）。
- 任務提及的 `creambox.py`、`keycheck`、`freeze_direct` 在倉內無現成腳本/定義——
  本次落實為：creambox.py、boxtitle.py 為本目錄新寫的補充掃描（SOP §8.6 允許作補充，
  不替代共享工具結論）；keycheck 以 p8.py＋150 題逐題語義核對落實；freeze_direct 以
  交付 SVG 的 SHA-256 直比 fix4 交付後哈希落實。
