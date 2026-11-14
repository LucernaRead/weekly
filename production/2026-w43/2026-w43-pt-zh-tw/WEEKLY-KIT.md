# WEEKLY-KIT — PT × ZH-TW（葡萄牙語正文 VOL.1 · 繁體中文講解）

狀態：**PROOFREAD-PASS**（獨立校對一輪零缺陷，2026-10-22；記錄見 §10——含對 §4/§5 兩處建造者計數的更正，兩處均為賬面錯誤、版面無誤）。週次 W43（2026-10-19–25）。
配對：正文 = 巴西葡萄牙語（核心 VOL.1 逐字節凍結）；講解 = 繁體中文（台灣/香港語境原生撰寫，
非由簡體版轉換——見 §2 方法）。報頭：A Lucerna。

針腳（磁碟實測，2026-10-22）：
- 印刷 PDF `A-Lucerna-VOL1.pdf`：18,305,238 B · sha256 a8e8102ff3891dcca026659b6732c83e58bb6e27e0f54ca363ec9b6b7fa7c664
- 網頁 PDF `A-Lucerna-VOL1-web.pdf`：3,515,949 B（<10 MB）· sha256 82890d61d958ad368db49ab5b908e6cbf47750f74f32c9cb96d982ee97914ca3
- svg ×8、cards ×8（1950×2700）齊全。

## §1 建造出處與凍結基線
- 建造目錄 `hidden_files/weekly-report-pt-zh-tw-build/`（核心 build 副本）；OUT 改道
  `files/weekly-report-pt-zh-tw/`（5 個 content 模組 + render.py BASE，共 6 處斷言替換）。
- 開工 freeze.py baseline：拷貝版 8/8 逐字節復現核心；收尾核心出貨 SVG 8/8 sha256
  未變（082acac0/c4a853ac/bba9906a/b9941754/4a1121e8/0d0ad436/d3dc772b/8a944c11）。
- svglib 偏離（開工實測裁定，僅 3 處，與 EN×ZH-TW KIT §2 同法）：`_sc_index`→`_tc_index`、
  字體族判定 `endswith("TC")`、預設族名 SC→TC（serif+sans 各一）。其餘 wrap 量測行為與
  核心版逐行相同；CJK 字寬兩面皆 1em，折行與核心全等（freeze diff 逐頁字串增減平衡佐證）。
- 渲染：一進程 run.py（TOTAL 150；A2 44 · B1 75 · B2 31；範本詞 92；零 FLOW OVERFLOW /
  零 HEAD TOO WIDE；P8 答案流終點 y=2397 ≤ 2552）。

## §2 變換方法（講解層原生繁體）
- 先以腳本抽取核心講解層全部 325 條 CJK 文本 run，再逐條以台灣/香港用語原生撰寫繁體
  對應（搜尋〔非搜索〕、數據、透過、範本、巴西利亞、半決賽/決賽、裡、週——用語層面重寫，
  非字形對照轉換），以「精確字面 + 次數斷言」兩階段套用（階段一家具/式樣 31 條、
  階段二 run 替換 250 條，最長優先 + CJK 鄰字守衛 regex）；--check 全斷言首跑通過。
- 變換腳本位於建造目錄 `scratch/transform.py`（scratch 例外）：其字面含核心講解函數
  原名的搜尋樣式（供改名 `expl()` 用），operative code 內原名 = 0（def 1 + 調用 21
  全改）；禁用術語於 KIT 與 operative code 皆 = 0。
- freeze.py diff 雙軌分賬閉合：P2–P7 非漢字字串增減 = 0（葡語正文多重集與核心全等）；
  P1 唯一非漢字移除 = 被徽章行替換的核心副標行（§3）；P8 非漢字移除 = 8 個
  «— PÁGINA N —» 分隔（換列定式 «— 第 N 版 —»）；新增漢字 944 字全為繁體講解層。

## §3 家具逐項（繁體列定式，依 EN×ZH-TW KIT §3 登記）
- 徽章：«葡萄牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本»。槽位裁定：PT 核心家族
  （同 EN/DE/ES）用核心自有副標槽——替換 P1 y=372 葡語副標行，19.5pt 粗體 BRICK 居中
  （PT×EN 已入倉先例同槽同式）；P1 頂帶 y=92 中文 «每週一期 · 讀巴西人正在讀的葡萄牙語» 留存。
- 頁腳（8/8）：«A Lucerna · 葡萄牙語週報 VOL.1 · 正文葡萄牙語 · 講解繁體中文»；
  頁碼 «第 N 版 / 共 8 版»（8/8 實測）。
- 欄目帶中文：頭條/生活/文化/體育/青年/深讀/語言/練習與答案；子題繁體（一步一步學會投票、
  吉他的回歸、足球之週、真人秀、高考與年輕人的打算、第二輪投票詳解、三個級別，三件工具、
  第 8 版）。
- P8 頭：«RESPOSTAS · 全部答案與簡析（第 1–8 版）»；右行 «每題附一句簡析 · 帶 ✓ 的為範本題»；
  分隔 «— 第 N 版 —» ×8 實測齊全。P8 式樣照 PT 家族扇出代碼實證（核心碼印 `N. key — note`、
  寫作題 `N. ✓ note`，本版代碼逐字未動、僅註文換繁體）。
- gloss 前綴 «譯注｜»（5 盒實測）；P1 關鍵詞行前綴 «講解｜»（核心 expl() 式樣）。
- 引號：注內中文引號核心 “” 10 處全換台式「」（P1×1、P7×4、P8×5，逐頁計數與核心對位）；
  葡語 «» 逐頁計數與核心全等。

## §4 鍵差異登記（註冊表一進程導出對照，唯三真差異）
| # | 核心鍵 | 本版鍵 | 類別 |
|---|---|---|---|
| 137 | 周日，巴西重返投票站。 | 週日，巴西重返投票站。 | 翻譯題鍵（譯文即鍵） |
| 138 | 出门前，核对你的投票地点。 | 出門前，核對你的投票地點。 | 翻譯題鍵（譯文即鍵） |
| 150 | （开放题，范文如下） | （開放題，範本如下） | 寫作裝置項 |
- 頁/級別差異：0。注差異 131 條（全譯繁體）、同文 19 條（語言中立）。
- p8.py compare：CLEAN（150=150）；其 keydiff=[3, 8, 58, 137, 138, 146, 147, 148] 中
  {3, 8, 58, 146, 147, 148} 經註冊表證偽為行級抽取偽影（兩版註冊表鍵逐字節相同；
  偽影集與已入倉 PT×EN 的 compare 清單相同）；真差異即上表三項（#150 為 ✓ 裝置項，
  不入 p8.py 抽取面）。

## §5 計數與繼承核驗
- 總量 150（A2 44 · B1 75 · B2 31；逐頁 10/18/18/18/18/18/12/38），與核心全等。
- gloss 詞條逐條點數：5 盒逐盒 [5, 5, 4, 4, 5] = 23 條，核心/本版全等，一項未刪；
  P1 «講解｜» 行 3 詞條全等。
- P7 金句：8 條葡語引文逐字繼承（出現次數核心/本版皆 1 次於 P7 全文連接面，頁標籤
  分布 {(Página 1):2, (Página 2):2, (Página 3):1, (Página 4):1, (Página 5):1, (Página 6):1}
  兩版全等）；譯文 8 條全繁體。
- 圖表幾何：P1 搜索條 + P6 雙圖的 rect 多重集與核心逐一全等（20 / 29 個）；
  標籤與數值為凍結葡語，元素級無覆蓋（遮擋審計 0 相關旗）。

## §6 機械門結果（最終渲染面）
- occlusion_audit.py（自檢先行通過）：本版 1 旗 = 核心自有 1 旗且數值逐一相同——
  P1 數字盒標題 «A SEMANA EM NÚMEROS · 數字看本週» 墨跡右端 968.5 > 盒邊 961.0。
  裁定：凍結核心化妝項（核心簡體版同字串同量測；繁體字寬同為 1em 未加寬），非本版
  缺陷、不修（家具標題文字屬雙語欄目標題，計入凍結面）。工具列其為 NEW 僅因字串
  SC→TC 不同，量測同一。
- 同行墨跡碰撞掃描（README 第 10 條）：0。
- 行首禁則掃描：真違規 0。7 處行首 «·» 全與核心逐字同位（葡語選項/詞條分隔符的
  家族折行式樣，標點感知口徑下不計；清單：P4×2、P5×1、P6×2、P8×2）。
- 簡體專有字形掃描（掃描集 169 字，由本版變換映射導出 + 謝/勝補入）：出貨 SVG 命中 0；
  operative code（bslib4/content×5/render）命中 0。唯一登記例外：svglib.py 庫註釋內
  «重阳» 一詞（核心庫文件逐行繼承、不渲染、不入版面；與 FR×ZH-TW 先例同裁定）。
- 雜散引號逐頁計數：«» 與核心全等；“” 本版 = 0（全換「」，見 §3）。

## §7 自校缺陷與修復（建造者全量自校一輪）
1. P8 注 #149 殘留簡體 «obrigado = 谢谢»（變換 run 漏收）→ 改 «謝謝»，已上版目檢確認。
2. P7 金句 5 譯文殘留簡體 «，博卡胜。»（同上漏收）→ 改 «，博卡勝。»，目檢確認。
   漏收成因已全量排查：325 條 run 中未被變換覆蓋者逐條過目，餘皆共形字或階段一
   家具字面已消費，無第三處。
3. P1 搜索盒註腳（自有講解行）因 谷歌→« Google » 加寬越盒邊（墨跡 1905.2 > 1885.0，
   遮擋 BOXTITLE 旗）→ 改短為 «第一輪前後Google數據：搜尋熱度，非投票意向»（墨跡 ≈1876），
   旗消除。同盒副題 «巴西人在 Google 搜什麼 · as buscas no Google» 墨跡止於 1884.0
   （距邊 1px）→ 一併收緊為 «巴西人在Google搜什麼 · …»（墨跡 1876.0，距邊 9px）。
- 八頁卡片全量目檢：TC 面渲染無缺字/方框；徽章、頁腳、頁碼、譯注、分隔逐頁在位。

## §8 日曆核驗（America/São_Paulo，date 實查）
2026-10-19 週一、10-23 週五（Globo 決選辯論）、10-24 週六（Vasco×Corinthians）、
10-25 週日（決選投票）、10-31 週六（Halloween）、11-01 週日（巴西盃半決賽首回合——
在 11 月，未提前）、11-02 週一（Finados）、11-08/11-15 週日（ENEM）——與版面陳述全合。

## §9 校對提示
- P8 注文破折號式樣以 PT 家族代碼為準（見 §3），勿按他列式樣改判。
- freeze diff 的 P8 字串增減（+154/−154）為答案欄重排面，鍵真值以 §4 註冊表對照為準。
- 核心 P1 數字盒標題旗已於 §6 裁定凍結，勿重報。

## §10 獨立校對記錄（2026-10-22，獨立校對者）——判定：PASS，一輪零缺陷、零修復

校對者獨立複跑全部機械門 + 人工逐項核（證據在 `hidden_files/proof-pt-zh-tw/`）。除下方兩處**建造者賬面計數更正**外，§1–§9 自報全部屬實；版面本身無一處需改。

### 兩處賬面更正（版面無誤，僅 KIT 數字寫錯）
1. **§4 注差異數**：自報「131 條不同 / 19 條同文」為 §7 修復 #1 之前的舊數（該修復把注 #149 由與核心同文改為繁體，已使一條由「同文」轉「不同」）。獨立雙 dump 實測終值：**注不同 132 / 同文 18**；18 條同文全為語言中立（葡語釋義、公式或簡繁同形字全同句：#2、16–20、35、56、57、59、66、73、87、102、103、113、116、128），132 條不同 = 128 條同骨架詞彙/字形替換 + 4 條引號式樣轉換（#33、#69、#82、#85 的 “”→「」）。
2. **§5 gloss 計數**：自報五盒 [5,5,4,4,5]=23 為誤數。誤因：P4 gloss 原文串自身含「擴大（比分）· a arbitragem」（分隔符前無空格），按 ' · ' 計數漏一條。獨立按源碼 gloss() 調用串逐條點數（核心 content12/34/56 與本版同源）：**五盒真值 [5,5,5,4,5]=24 條**，兩版逐條（葡語詞頭與順序）完全相同——gloss 逐條點數硬項實質滿足（24=24）；P1 expl 行 3 條兩版同。建造者 §5 兩欄數字同錯一格，結論（與核心全等）不變。

### 機械門（tools/，獨立複跑）
- **freeze.py baseline 8/8** 逐字節復現核心（svglib md5 92efd4db…）；收尾複核核心出貨 SVG 8/8 sha256 與開工值全等（核心未被觸碰）。本版 build 副本（改道至 hidden_files/proof-pt-zh-tw/edition-copy，**從不在核心 build 目錄 import**，README 第 11 條）全量重渲染與出貨 SVG **8/8 逐字節全等**。
- **freeze.py diff 雙軌分賬閉合**：P2–P7 非漢字增減 = 0；P1 唯一非漢字移除 = 核心副標行（徽章槽，登記項）；P8 非漢字移除恰 = 8 條 «— PÁGINA N —» 分隔符（換列定式）；新增漢字 944 全為繁體講解/家具（逐串核：P8 答案塊繁體注、分隔符、各版講解；無殘留簡體講解）。P3 漢字移除 9 字 = «數字看本周»→«數字看本週» 之差，屬登記雙語題的繁體化。
- **p8.py**：核心 extract 150/150、本版 150/150、**compare CLEAN**。所報鍵差 {3, 8, 58, 146, 147, 148} 經註冊表逐項證偽為提取偽影（六鍵註冊表逐字節同核心；且該集合 ⊂ PT×EN compare 的偽影集，同機複驗 PT×EN 一致）——按 README 第 13 條裁定非缺陷。**真鍵差恰 {137, 138, 150}**，與 §4 賬一致並經 SVG 原文複證（週日/出門前/範本）。
- **註冊表雙 dump**（一次性雙進程、各自改道副本）：總數/級別/頁分佈/題型全同核心（150 = A2 44 · B1 75 · B2 31；頁 10/18/18/18/18/18/12/38）；題型差 = 僅中文標籤簡→繁；鍵差恰 {137,138,150}。
- **代碼骨架核**（tokenize 去字串對照）：content34/56/7/8 與核心**完全相同**；content12 唯一差 = 徽章一處調用（19→19.5pt、加粗、GREY→BRICK，§3 登記家具）；svglib 差恰 = TC 面切換四行；bslib4 差恰 = 頁腳串 + expl 改名 + gloss 前綴；render.py 僅 OUT 改道。P8 答案生成邏輯逐字未動 → 破折號式由構造保持（README 第 8/14 條）。expl() 調用 21 處 + 定義 1 處；operative code 中橋接詞 = 0（僅 scratch/transform.py 搜尋串，按先例披露）。
- **occlusion_audit.py**（自檢 OK）：本版終局 1 旗 = 核心 1 旗，數值全同——P1 數字盒題 «A SEMANA EM NÚMEROS · 數字看本週» 右墨 968.5 > 框 961.0，兩版同字串同值（核心 «数字看本周» 同值），建造者已預登記為凍結核心化妝項，獨立複測確認未惡化，裁定非缺陷。
- **針腳獨立實測**（與自報全等）：網頁版 3,515,949 B / sha256 82890d61164c554f252764e2598a933161efaebc68bd264c49c437322fe1fe40；印刷版 18,305,238 B / a8e8102f590abc1fa73de400cacd216efc0c0cd5926a55e5f33279411365c43e；均 8 頁。
- D5 rebuild (2026-11-13–14, see D5 rebuild section at the end of this KIT): print master `A-Lucerna-VOL1-pt-zh-tw.pdf` **7143708 B** · sha256 `ddbe4e1e0767baa560e8580bb57cbb83a39860ecdf88eaef3c860b74d0b14d58`; render-web `A-Lucerna-VOL1-pt-zh-tw-web.pdf` **3135271 B** · sha256 `c2ec27437ccfabbeb86a7c8045ed403980fe8728e1404352542bb4b56edd6067`; web (issues-type) `2026-w43-pt-zh-tw.web.pdf` **1093758 B** · sha256 `5ec32860d37179ec25bbf65942950fdc9c0d39a0da23440100c6c83bebc0b567` (< 7 MB); text.md byte-identical to the shipped version (sha256 `612b6beb750ab677791d176b0dcecac21ed23330126f6b0c47c623a4f891e58d`). Pre-D5 KIT pins above (print 18,305,238 B (sha256 `a8e8102f…`); render-web 3,515,949 B (sha256 `82890d61…`)) are D1-era values, already expired before this rebuild (toolchain drift: Bold/Italic subset split in tools/webpdf.py commit 40963281).

### 人工核（獨立）
- **150 鍵全量重推導**：校對者從葡語正文逐題重推 #1–#150（理解/填空/配對/造句/翻譯/判斷），與註冊表及 P8 印刷答案塊逐條全合，含算術複核（982+514+431+312=2,239；350+350=700；900−250=650；66.026>66.000；#150 範文 92 詞元與核心同口徑、80–100 區間內）。
- **繁體原生性**：簡體專有字形掃描獨立複跑——語料差分法 361 候選逐一裁定為簡繁同形字（域/執/廢/奧 等命中均為正確繁體用法：執法、廢票、格雷米奧）；定版 SIMP 集（2,426 字）掃出貨 SVG 命中 4 串全為誤報；operative code 唯一命中 = svglib 庫注釋 «重阳»（不渲染，登記例外維持）。大陸式詞彙掃描 = 0。台式用語全冊在版（搜尋/數據/透過/範本/巴西利亞/裡/週/影片/螢幕）；詞級改寫證據（搜索→搜尋、通過短視頻→透過短影片、乐队→樂隊、搜索量测→搜尋量測）證非字面轉換。
- **建造者三處自修實證**：注 #149 «謝謝» 在註冊表與 P8 印刷行在版 ✓；P7 金句 5 «，博卡勝。» 在版 ✓；P1 搜尋盒全冊 CJK-run 未覆蓋串逐條復掃 = 0 漏網（自修後同類漏收全冊 = 0）。
- **列定式**（EN×ZH-TW KIT §3 + README 第 20 條）：徽章恰 1 次、y=372、19.5pt、粗體、#a4553a，文 «葡萄牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本»（PT 核心有原生副標槽 = EN/DE/ES 家族例）✓；頁腳 8/8、頁碼 «第 N 版 / 共 8 版» 8/8、P8 頭 «RESPOSTAS · 全部答案與簡析（第 1–8 版）»、分隔 «— 第 N 版 —» ×8、gloss 前綴 «譯注｜»、報頭 A Lucerna ✓；他列家具殘留 = 0；禁用詞 bridge/paper 於頁面與 operative code = 0。
- **幾何兜底**（自研 PIL 墨跡口徑，升部校正）：同行墨跡碰撞（README 第 10 條）兩版均 0 對；每頁 rect 多重集兩版全等（P1 23、P2 26、P3 26、P4 27、P5 27、P6 31、P7 19、P8 38——§2 的 20/29 為子集計數，實質以全等為準）；後繪元素覆蓋文字兩版均 0（P1/P6 圖表元素級，第 12 條）；建造者 P1 修復實測：副題右墨 1,875.8（盒右界 1,885，餘 9.2）、注腳右墨 1,877.8 ≤ 1,885 ✓（README 第 15 條：本版自有講解串溢出已由建造者縮短，未以「核心同旗」為藉口）；引號 “”→「」 恰 10 對（P1×1、P7×4、P8×5，與 §3 賬合），雜散直引號兩版全頁 0=0（第 18 條）。
- **禁則（標點感知口徑）**：行首禁則命中集兩版全同——7 元素以 «·» 起行（P4×2、P5×1、P6×2、P8×2），座標與核心逐一同位，皆葡語選項/詞表續行（凍結正文版式），裁定家族式樣、非缺陷；中文講解行無一行以收尾標點起行。真違規 = 0。
- **P7**：金句 8 條與核心逐字全同、同位；頁標籤分佈兩版全等 {(P1):2,(P2):2,(P3):1,(P4):1,(P5):1,(P6):1}；8 條逐字回溯所標正文頁各恰 1 次出現，驗真 ✓；VOL.2 預告在版（凍結）。
- **日曆**（TZ=America/Sao_Paulo，date 實證）：10-19 週一、10-23 週五、10-24 週六、10-25 週日（決選）、10-31 週六、11-01 週日（Copa 半決賽首回合，未提前）、11-02 週一、11-08/15 週日（ENEM）、11-07 週六——與版面全部星期斷言相合；百分比全為 Google 搜尋數據並明示「非投票意向」，無民調百分比冒充選情 ✓。
- **卡面目檢**：8 張卡逐張看畢，TC 面渲染無缺字/方框；P6 條形與數值成比例、標籤無遮擋。

**結論：PASS。本版可入倉（入倉由主線執行）。**

## D5 rebuild (2026-11-13–14, D5-only)

SOP §1.1 font fix: the explanation layer's Latin letters move from Noto Sans CJK to Newsreader (SemiBold). No commit, no push — insertion is done by the closer after an independent re-proof. Work log: `hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-zh-tw/`; per-edition report: `production/notes/2026-w43/g-pt/scratch-d5-rebuild-pt/D5-REPORT-2026-w43-pt-zh-tw.md`.

**Install**: core landed with `apply_variant.py --patch-core pt --week 2026-w43` (production `core-pt/svglib.py`, `_D5_READER = "latin"` — the core template); this edition installed with `apply_variant.py --svglib patched/2026-w43-pt-zh-tw/svglib.py --target pt --reader zh-tw --week 2026-w43`, `_D5_READER = "cjk"` (--check dry-run clean, RC 0); routing unit test `test_d5_routing.py` FAILURES: 0; fix2 block kept (5 occurrences).

**Baseline** (pre-fix production build): run TOTAL 150, 0 warnings; print/web/issued text layers 36,685 = 36,685 = 36,685 chars, multiset diff 0; baseline web PDF 1,441,322 B; print PDF 16,777,337 B (`0ff7cdb0…`); pre-fix census D5 Latin 344, Cyrillic 0, curly in CJK 0; baseline P8 noted 150/150.

**Defects and fixes** (run1: 4 items, sizes only, no wording changed):

- P2-ex head `C　COMPLETE COM OS NÚMEROS`: content12.py:256 `e.head` 25→22
- P3-main head `DOIS INSTRUMENTOS, UM PAÍS`: content34.py:21 `f.head` 25→24
- P1 box: content12.py:47 `f.box` close, `tsize` 23→20
- P1 body line `第一輪前後Google數據：搜尋熱度，非投票意向`: content12.py:85 `p.text` 19→18

(The P1 body line is the only body-text size change in the family; every other fix is a head or box title.)

P8: 207→207 lines, footer slack 57.4→57.4 px.

**Gates run2** (16 gates; no family gates.py for pt) — **ALL-GREEN (16/16 gates)**: run TOTAL 150, 0 warnings; head_check 0 defects; d5 census 0/0/0 (curly_total=0); render RC=0; webpdf RC=0 (1,093,758 B < 7 MB); occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN, keydiff=[137, 138] (the registered reader-language keys); freeze baseline 8/8; freeze diff added CJK chars 0 (added Latin strings 238, run splits); spill 0; boxtitle 0 DEFECT (28 titles); edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web 93,519 chars, multiset diff 0; textmd carryover PASS 0/0 (svg 5422 = md 5422 tokens); masthead gap (D18) 130.8 px PASS; census_quotes 0 defective.

**New deliverables**: print master `A-Lucerna-VOL1-pt-zh-tw.pdf` 7,143,708 B (`ddbe4e1e…`); render-web `A-Lucerna-VOL1-pt-zh-tw-web.pdf` 3,135,271 B (`c2ec2743…`); web (issues-type) `2026-w43-pt-zh-tw.web.pdf` 1,093,758 B (`5ec32860…`); text.md byte-identical to the shipped version (`612b6beb…`). Still 150 exercises.

**Exporter note**: pt has no `.text.md` exporter (verified: the `ru_textmd.py` trial differed by 757 lines). The issued `issues/2026-w43/2026-w43-pt-zh-tw/2026-w43-pt-zh-tw.text.md` is carried over BYTE-IDENTICAL; content identity is verified by `verify_textmd.py` carryover jointly with gate 15 (print=web text layer diff 0).
