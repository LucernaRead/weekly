# ⚠️ 磁碟配額事件（記錄開頭，依硬性約束寫明）
- 2026-11-10 23:5x，Build 14 freeze.py baseline 在 copytree 整個 core 目錄（含 19MB print PDF＋8MB cards）時報 `[Errno 122] Disk quota exceeded`，複製中斷；同時 tee 寫 freeze14.log 亦報配額不足。
- 處置：立即停手，未重跑 freeze.py baseline；刪失敗的殘缺複製 freeze14/（9.3MB，我方自產廢件），小寫入恢復；改用等效輕量驗證：就地 hash SVG → 重跑 run.py（僅覆寫約 500KB SVG）→ 再 hash 比對，8/8 位元組一致（見下「Build 14 終版驗證」）。/home/hatch 檔案系統本身有 45G 空間，122 是共用卷的使用者配額，非磁碟滿。
- Build 12 的 freeze baseline 已在配額事件前完成：自報 8/8（freeze.log）。

# W47 zh-tw 返修記錄（D1–D8，Build 12 起）

- 返修 builder：葉子（第二輪，只修 D1–D8，不動無關內容；不跑 insert/lint/push，不提交）
- 依據：PROOF-NOTE.md（第一輪獨立校對）+ 協調員裁定（N1 不修、N2 不修、中文數字空格與選項流式折行不列缺陷）
- 工作目錄：`production/2026-w47/core-zh-tw/`；本記錄：`hidden_files/w47/scratch-zh-tw-fix/`

## 修改清單（源碼級）

- D1 content56.py：P6 主文第 2 段刪去雙 11 殘句「回饋不是折價，實付金額才是真的——看活動也一樣：時間花在哪裡，才是真的。」段落以「去不了就留到下次。」收束。
- D2：D1 刪句後 P6 主文縮短約 2 行，孤字「的。」隨之消失（重渲後以 SVG 座標 + 渲染圖驗證；如仍有孤字再調斷行）。
- D3 content7.py Q110、content8.py Q135 鍵「燈秀」→「主燈秀」（與 Q22、P2 正文一致）；登記表由 REG 重建，P8 答案區隨之統一。
- D4 content56.py：P6「數字一覽」「時間：14:00、17:00、18:30、19:00、20:00」拆為兩條「時間：14:00、17:00、18:30、」「19:00、20:00」（避開 kinsoku oidashi 把「、」行首的 0 拉下造成的數字斷行；內容、數字全保留）。
- D5 全角化 6 處 + 波浪號 1 處：content34.py「SUPER STAGE,」→「，」、「運動,U幣」→「，」、「頒獎：11月22日(日),」→「（日），」；content12.py「小雪：11月22日(日),」→「（日），」；content56.py 同上；content7.py「延期披露:」→「：」；content8.py「120~180」→「120～180」。
- D6 content8.py：P8 眉注「All notes in English · ✓ = the writing model」→ 全角空格分隔「All notes in English　✓ = the writing model」。
- D8 content7.py Q111：題干「魔雪奇緣世界的冬日市集在哪裡？」→「想逛冬日市集、買聖誕禮物，要去哪裡？」（鍵 A＝魔雪奇緣世界不變；題干用詞取自 P5 正文「第一個冬日市集，可以逛市集、買聖誕禮物」）。
- 觀察項：P7「words: 遊行」「Make your own: 夜越深」源碼本已有半角空格（SVG 內拉丁 run 尾含空格、下一 run x 已含空格進位），屬文字層提取 artifact，非視覺缺陷，不動。
- N1/N2：不動（裁定）。P8 題干 13.8px、答案鍵 13.0px 不動。

## D7 嘗試（待基線綠後另起小節記錄）

- 實測基線：文章正文 f.para 預設 24px＝18pt（已在 SOP 頭條正文 18–19pt 內）；22.5px＝16.875pt 為側欄正文／練習題干（SOP 16.5–17.5pt 內，不用動）；真正偏離的是 Notes 講解框 20.5px＝15.38pt（SOP 講解層上限 13.5pt）與 P7 欄正文 21.5px＝16.13pt／P7 練習 20.5px＝15.38pt（SOP 側欄正文下限 16.5pt）。
- 嘗試方案：Flow.gloss／Flow.expl 20.5→18px（＝13.5pt，階梯頂）；P7 三欄正文 21.5→22px、P7 練習 20.5→22px（＝16.5pt，階梯底）；P4 練習 21.5→22px 視 P4 餘量決定。24px 正文與 22.5px 側欄／題干不動。
- 如重渲後任何溢出／孤行／重疊或機械門失敗且無法乾淨解決，立即回退。


## Build 12 基線驗證（D1–D8，不含 D7）— 2026-11-10 23:31

- run.py：150 題（A2 44／B1 74／B2 32；分佈 10／18／18／18／18／18／12／38），零 FLOW OVERFLOW／HEAD TOO WIDE。P6-main 末行 col 1「次。」收束、Notes 框在 col 2 頂；P7 col3 末 1825.4、teaser 末 2579.4（頁腳線 2596，清 16.6px）；P8 鍵末 2287。
- render.py：print 19,420,646 B，SHA 64317427…；web 2,307,626 B（<7MB）。
- checks.py PASS（8 金句各 2 次、簡體字 0、P4 柱 90／450／900、P6 圓點 188.0／695.21／948.82／1033.36／1202.43）。
- occlusion_audit 自檢 6 類全觸發、審計 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff=[]）；freeze baseline 自報 8/8（見 freeze.log）。
- print/web 文字層：raw 46,201 vs 46,203 位元組，多重集差 0 字元（僅 web 多 1 空格＋1 換行，已知 run 邊界 artifact）；-layout 98,909 位元組等長，僅 2 行差（P1 刊頭間距 1 空格、「1902年的月球之」vs「1902 年的月球之」同類 artifact）。
- P8 最小字號 9.75pt（160 spans，print/web 一致）；題干 10.35pt（288 spans）。
- D1：全刊「回饋」0、「實付金額」0；P6 段末「去不了就留到下次。」✓。
- D2：P6 col 2 頂（y 208–320）零文本元素；全刊無獨立「的。」文本元素（其餘單字 run 為字體分段，非孤字）✓。
- D3：SVG 串接文本 22／110／135 皆「主燈秀」各 1 次；印刷版 PDF 文字層欄位重組獨立提取 150 鍵，與 .text.md 登記表 149/149 一致（Q150 為寫作 ✓ 形式），Q22／Q110／Q135 皆「主燈秀」✓。
- D4：數字一覽「時間：14:00、17:00、18:30、」＋「19:00、20:00」兩行，「19:00」完整不斷 ✓。
- D5：SVG 串接文本舊式 6 處＋「120~180」皆 0，新式全角皆在位；殘留掃描命中僅兩類既定慣例（P7 英文講解句引用 CJK 詞的 ASCII 逗號／括號；P8 選項標記「(A. 對 · B. 錯)」的半角括號）＋跨元素串接 artifact（「(Wikimedia Commons)事實框」等），皆非 D5 殘留。
- D6：眉注「All notes in English　✓ = the writing model」（U+3000）✓。
- D8：Q111 新題干「想逛冬日市集、買聖誕禮物，要去哪裡？」✓。
- D7 未做（見下）。

## 邊距核查（協調員追加核查項）

- 實測 8 版 SVG：欄條 rect x=88、寬 1774（左 88px、右 1950−88−1774＝88px）；頁腳線 88–1862；最小文本 x＝88。**左右皆 88px＝66pt，合 SOP，無 ko 版 65px 問題，不改。**（P1 無 p.band，以頁腳線＋最小文本 x 核驗，同為 88。）

## D7＋P8 題干同一輪嘗試（Build 13，協調員 2026-11-10 18:36 追加）

- P8 題干：content8.py 37 處 f.ex size=13.8 → 20.5px（＝15.375pt）；D 段段落 15px、寫作 20px、範文 16px、答案鍵 13.0px 不動。
- D7：bslib4.py Flow.gloss 20.5→18px、Flow.expl 預設 20.5→18px；content7.py P7 三欄 Flow 正文 21.5→22px、練習 size=20.5→22px（診所／句式／讀者園地固定盒內字號不動）；content34.py P4 練習 size=21.5→22px（14 處）。
- 24px 文章正文（已 18pt）、22.5px 側欄正文／練習題干（已 16.5–17.5pt 帶內）不動。
- Build 12 源碼備份於本目錄 build12-src-backup/（回退用 cp，不動 git）。
- 判定：重渲後任一溢出／孤行／重疊或機械門失敗且無法乾淨解決，即回退對應項（D7 與 P8 分頁歸因：P8 問題只回退 P8，P1–P7 問題只回退 D7）。

## Build 13 試驗結果：D7 保留，P8 回退

- D7（P1–P7）：重渲零 FLOW OVERFLOW／HEAD TOO WIDE；P7-b1 末 1501（底 1560，餘 59px）、P7-a2 末 1377、P7 圖末 1604.3（金句條 fy=1712，清）；P4-ex 末 1973（餘 587px）；P4-main 改走 col 1 末 976（底 1020，圖表在 1070 之後，清）；P1–P6 各 flow 皆因 Notes 框縮小而提前收束。occlusion 審計 P1–P7 零 flags。
- P8 題干 20.5px：run.py 報 8 次 FLOW OVERFLOW（P8-ex，col 3，need 95／70／95／95／95／95／95／66，底 1050，flow 夾至 1132）；occlusion 審計 381 flags 全在 p8-test.svg（TEXTX 345、COVER 21、LINEX 15）——溢出題目被筆記照片 rect 蓋住、被寫作條分隔線穿過、與圖注／答案鍵重疊。缺口約 700px（4 欄共 3400px 容量，20.5px 題干需約 4100px）；寫作條＋答案鍵僅 273px 餘量、答案鍵已在 9.75pt 底線、不得削題，無法乾淨解決，按回退條款回退。
- 回退執行：content8.py 37 處 size=20.5 → 13.8，與 Build 12 備份 diff 為空，確認還原。D7 改動保留，進入 Build 14 終版重建。

## Build 14 終版驗證（D1–D8＋D7 保留，P8 已回退）— 2026-11-10 23:51

- 交付物：print `Lucerna-VOL4.pdf` 19,420,492 B，SHA-256 `f2764750d3872fc07adc034ef3c1e80cad60d543067f6a96a710b16bd8f89fba`；web `Lucerna-VOL4-web.pdf` 2,307,484 B，SHA-256 `9191ef790de862fd1defc7e51ea661e8de71b1438e1d55068a393eb211dc54a2`；`.text.md` 49,816 B，SHA-256 `4a99110975bb0c4b684de82a8a9ed7fa11bddb59562bb75398327cb4446207a5`。8 頁，1462.5×2025 pt。
- run.py：150 題（A2 44／B1 74／B2 32；分佈 10／18／18／18／18／18／12／38），零 FLOW OVERFLOW／HEAD TOO WIDE。checks.py PASS（8 金句各 2 次、簡體字 0、P4 柱 90／450／900、P6 圓點同前）。
- 機械門：occlusion 自檢 6 類全觸發、審計 **0 flags**；p8 extract 150/150；p8 compare CLEAN（keydiff=[]）；freeze 等效驗證（就地重建）**8/8 SVG 位元組一致**（freeze.py baseline 複製路徑因配額事件未跑，見記錄開頭）；print/web 文字層 raw 46,224 vs 46,226 位元組、多重集差 0 字元，-layout 101,632 位元組等長、僅 2 行已知 artifact（P1 刊頭間距 1 空格、「1902年的月球之」vs「1902 年的月球之」）；P8 最小字號 9.75pt（160 spans，print/web 一致），題干 10.35pt（288 spans）。
- 150 鍵獨立驗算：印刷版 PDF 文字層欄位重組提取 150 鍵，與 .text.md 登記表 **149/149 一致**（Q150 為寫作 ✓ 形式）；Q22／Q110／Q135 皆「主燈秀」；Q111 鍵 A 不變。P8 113–150 逐題在列，無錯鍵。
- D1–D8 回歸（Build 14 SVG 串接文本＋渲染圖）：D1 回饋 0；D2 P6 第 2 欄頂零文本元素；D3 三鍵一致；D4「19:00」完整；D5 舊式 0、新式全在位；D6 全角空格眉注；D8 新題干在位。
- D7（保留）：Notes 講解框 20.5→**18px＝13.5pt**（階梯頂）；P7 三欄正文 21.5→**22px＝16.5pt**、練習 20.5→**22px**；P4 練習 21.5→**22px**；文章正文 24px＝18pt、側欄正文／題干 22.5px＝16.875pt 原已合規不動。重渲零溢出、遮擋 0、視覺層級仍清晰（正文 24px ＞ 講解 18px）。
- P7 餘量：B1 欄末 1501／底 1560（餘 59px）、A2 1377、B2 1435，金句條與預告位置不變；P4-main 改走第 2 欄末 976／底 1020（圖表在 1070 之後，清）。
- 8 版逐版目視（cards/*.png）：P1–P8 皆無溢出／重疊／孤行／壓頁腳。P6 段末「去不了就留到下次。」欄內收束、Notes 框在第 2 欄頂；P7 Q111 新題干、延期披露全角冒號；P8 眉注全角空格、寫作題「120～180字」、150 鍵全印。
- §1.1 重測：紙色 #fbfaf6（8 版）、刊頭 196px、頭條 60px、字體 5 族、徽章三色俱在、家具全角空格、左右邊距 88px＝66pt（8 版實測）、無金色／近黑底（新增 fill 色皆出自蛾標資產 lucerna-moth.svg，自 Build 11 即有）；P8 題干 10.35pt（見 P8 回退段）、答案鍵 9.75pt 達底線。
- §8.1：Notes 框皆英文（P4 一框 2 個 CJK 詞皆見於該頁正文）、P7 三條 expl 的 CJK 詞（遊行／封王／夜間／終點、入圍／頒獎／鋼雕／保險箱、小雪／節氣／燈秀／市集）皆見於 P7 正文，零缺失。
- 未動項：WEEKLY-KIT.md 未更新（仍記 Build 11 哈希；本次 briefing 指定記錄放 scratch，KIT 是否補記由協調員定）；tools/p8.py 未動；未跑 insert/lint/push，未提交，未碰 W43/W45/W46。
