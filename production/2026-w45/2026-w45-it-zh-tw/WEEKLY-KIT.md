# WEEKLY-KIT — IT×ZH-TW（義大利語正文 VOL.2 · 繁體中文講解）W45

狀態：**待獨立校對（PENDING，不宣布定稿）**。本 KIT 記錄恢復構建員的復核結論：round-0 交付物全部門禁復測通過，**無修復輪、未重渲染**；定稿須獨立校對一輪零問題後另行判定。
配對：正文義大利語（La Lucerna VOL.2 凍結核心）× 講解繁體中文（台灣原生寫法，非簡體轉碼）
週期：2026-11-02–08（W45，issue dated Mon Nov 2, 2026）· 核心出貨 `files/weekly-report-w45-it-core/` · 本版 build `hidden_files/weekly-report-w45-it-zh-tw-build/`
交付物：svg ×8 · cards ×8 · 雙 PDF · 本 KIT · ABSTRACT.txt。未入倉、未發 Discord、未往主聊天發卡片/PDF。

## 1. 建造溯源與上一任遺留狀態復核

- 上一任構建員未交報告即結束，但盤上 round-0 狀態完整。本輪開工前查重：files 與 build 兩目錄在 60–120 秒複查內零新寫盤（最新寫盤 2026-10-27 23:38 UTC，早於本任務），安全開工。
- 上一任狀態逐項復核結論（**全部屬實，僅兩項補充**）：
  - svg ×8、cards ×8、雙 PDF 字節數與 sha256 與上一任記錄逐項一致（見 §8 針腳；本輪結束時再測仍一致，未動）。
  - 流程終值（round-0 build-log 存檔值，本輪未重渲染故引用存檔）：P1-headline 1497、P7 col3 1673.0、P6-ex 2569、P8-keys 2484；計數 150，A2 47/B1 70/B2 33，頁分布 10/18/18/18/18/18/12/38，範文 81 詞。
  - occlusion 分版 0 / 核心 0 / NEW 0、p8 CLEAN 150=150、keydiff [6,15,58,71,77,137,138,139]——本輪以共享工具重跑，**逐項再現**（見 §6）。
  - **補充 1**：上一任未在構建樹留下 freeze baseline 產物（僅 tools/scratch 有舊的 baseline-it）。本輪已用 `tools/freeze.py baseline` 重建（見 §6），產物存 `hidden_files/weekly-report-w45-it-zh-tw-build/baseline-w45-it.json`。
  - **補充 2**：transform-log 末行 `for 重阳. → for Double Ninth.` 僅為 svglib docstring（程式註解），不刊印、無版面效應；另見 §7 偏差 4。
  - 另：復核初查時某頁轉儲曾顯示 P4「第 4 版练习」含替換字元，經原始位元組核查為輸出顯示噪聲，core 與 edition SVG 該串皆乾淨（`ESERCIZI · 第 4 版练习` / `第 4 版練習`），非文件問題。
- 變換方法（上一任 transform.py 登記，本輪核查與其一致）：OUT 改道（5 content + render.py）→ OpenCC s2twp 整檔轉換 5 個 content 模組（非 CJK 字元流斷言逐字節不變）→ 台灣原生修正（周→週 3 處、片語→詞組 2 處、資料→數據 4 處、引號→「」4 對、P7 讀者園地說明句重寫 2 處、P8 頭與分隔列定式）→ bslib4 家具（頁腳、譯注｜、expl 改名 22 處）→ P1 配對徽章插入 → svglib TC 面切換。
- 構建命令（上一任，單進程；本輪未重跑）：`cd hidden_files/weekly-report-w45-it-zh-tw-build && ../../tools/venv/bin/python run.py`，再 `../../tools/venv/bin/python render.py`（tools/venv/bin/python；系統 python3 無 cairosvg）。核心 build 目錄內未 import 任何模組（README #11）。

## 2. 註冊表（實測，round-0 build-log）

- 總量 **150 題**：A2 47 · B1 70 · B2 33；分頁 10/18/18/18/18/18/12/38；題型 完成句子 61 · 單選 48 · 詞彙配對 12 · 造句 7 · 句型轉換 1 · 判斷對錯 3 · 完形單選 13 · 翻譯 4 · 寫作 1；範文（MODELO）81 詞。
- P8 版式：破折號式 `N. key — note`、寫作題 `N. ✓ note`（IT 家族，README #8/#14）；答案由登記表生成，非手打。
- P8 幾何沿用 W45 核心（見 §7 偏差 2）：答案流終值 2484，頁腳帶上方安全收尾。

## 3. 家具（繁體列定式，以 W43 同配對已上架 SVG 為準，逐項實測）

| 項 | 本版定式 | 在位證據 |
|---|---|---|
| 徽章 | «義大利語正文 · 繁體中文講解 — 給繁體中文讀者的版本» | P1 唯一 1 處；實測 x=975 居中 · y=574 · 22pt sans 粗體 700 · BRICK #a4553a · Noto Sans CJK TC，與 W43 同配對 SVG 屬性逐字節同（IT 家族無空槽位故插入式，README #20） |
| 頁腳（每頁） | «La Lucerna · 義大利語週報 VOL.2 · 正文義大利語 · 講解繁體中文» | 8/8 頁 SVG 各 1 |
| 頁碼行 | «第 N 版 / 共 8 版» | 8/8 頁逐頁對應 |
| gloss 前綴 | «譯注｜» | P2–P6 各 1（共 5 處，與 W43 同）；P1 為 «講解｜» 行，與核心同構 |
| P8 頭 | «RISPOSTE · 全部答案與簡析（第 1–8 版）»；右行 «每題附一句中文簡析 · 帶 ✓ 的為範文題» | P8 SVG 在位 |
| P8 分隔 | «— 第 N 版 —» | N=1..8 各 1 |
| P8 band | «VALUTAZIONE E RISPOSTE · 練習與答案» | 在位 |
| P1 期名行 | «意 大 利 語 週 報 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A» | 在位（間距版式沿核心） |
| 注內引號 | 台式「」：P1 1 對、P7 2 對、P8 #104 注 1 對（共 4 對；核心 “” 計數 P1 1→0、P7 2→0、P8 1→0）；義語 «» 逐頁與核心全等（P2 8、P5 5、P6 5、P7 28、P8 4 對等） | 引號逐頁對賬畢；P8 #104 的「」來自 P7 練習 104 登記注文共享串（transform C4），非新增改動 |
| 報頭 | La Lucerna（義大利語 masthead，凍結） | — |

## 4. 鍵差異全表（p8.py compare 實測 keydiff = [6, 15, 58, 71, 77, 137, 138, 139]，逐項裁定）

| 題 | 類別 | 裁定 |
|---|---|---|
| 137 | 翻譯題鍵改向（IT→讀者語） | 鍵 «週一第一場寒冷來了。»（核心簡體同句之繁體形）；注 «對照原文»。合法改向，同 W43 137 |
| 138 | 翻譯題鍵改向 | 鍵 «觀眾可以免費品嚐。»；注 «assaggiare gratis = 免費品嚐»。合法改向，同 W43 138 |
| 139 | 翻譯題鍵改向 | 鍵 «週日晚上，佛羅倫薩對尤文圖斯。»；注 «si gioca = 進行比賽»。合法改向（本期 139 鍵本身即中文譯文，與 W43 的 139 題幹改向情形不同） |
| 6、15、58、71、77 | **提取偽影（README #13 類）** | 五題義語鍵逐字節未變（previsioni / termosifoni / più bella / gratuiti / ci sarà）；提取器把破折號後注文首段併入鍵串比對，差異全在繁體注文（如 «預報（複數）»、«暖氣片（複數）»、«週日晚最美（主觀評價）»、«免費的（陽性複數）»、«將來時：ci sarà（將有）»），非鍵差異。證據：提取鍵以 « — » 切分後首段兩版全等 |
| 140、150 | 非 keydiff 對照 | 140 鍵 «Ogni previsione deve essere chiara.» 兩版全等；150 兩版同為 ✓ |

其餘 142 題鍵與核心逐字節全等。**為何少於同族 EN/FR 的 14 項**：已證為真實差異而非漏測——兩版印刷集皆 150/150（missing=[] · extra=0 · uncertain=[]），keydiff 係對全部 150 條提取鍵逐條比對得出；且 freeze 多重集差分顯示 P8 全部變更行皆為中文注文轉換、3 條中文鍵（137/138/139）與家具（頭/分隔/頁腳），無其他義語鍵變動可漏。EN/FR 核心的題型/注文結構不同，其 keydiff 項數自然不同，不可橫向套用。

## 5. 繁體獨立性三軌（本輪實測）

- **直接以繁體寫成**：變換以 OpenCC s2twp 為底，經逐串人工覆核修正（transform C1–C6 登記），非簡體機械轉碼殘留；台灣慣用形在版：週報、義大利語、數據（4 處）、詞組（2 處）、機率（非概率）、搜尋系表述沿核心語境。
- **簡體殘留 0**（雙軌交叉核驗，非自表）：
  - 軌 1：W43 同配對 SVG 字符集 ∪ W43 繁體核心體（`weekly-report-zh-tw-it` 正文）字符集，並集 941 字；本版 431 個相異漢字中 50 字不在並集，**逐字按語境裁定皆為合法繁體新主題詞**：寒冷、論壇、品嚐、傳統、博物館、杏仁、圍巾、衣櫃、糕點師、克雷莫納、牛軋糖、追思日、初雪、都靈、潘妮託尼、爭議、禦寒、發稿、繼續、返程、麵包等（皆為本期新主題「初寒／文化論壇／潘妮託尼／牛軋糖／松露／民俗影展／天氣預報」之正當用字）。
  - 軌 2：OpenCC s2twp 變體掃描命中僅 2 字——«里»（亞得里亞海一側之 «亞得里亞»，音譯固有名詞內共形字，同 W43 利古里亞先例）與 «栗»（烤栗子；栗為台灣栗子正字，慄為戰慄義之異體），皆裁定正當。
  - 大陸詞彙掃描 0：代碼/比賽項目/報導/市集四類概念本期未出現（簡繁兩形皆 0）；NL×ZH-TW 第 5 類 «把詞組成» 在版為正確形（片語/片语 0，詞組 2）；另掃 軟件/視頻/打印機/網絡/信息/意大利语等簡體形皆 0，對應繁體形 週報 8、義大利語 21、義大利 22、數據 4。
- **簡體字形區塊掃描 0**：同上兩軌；除裁定正當的 里/栗 外，無簡體專有字形殘留。
- **引號**：一律「」（見 §3）；**TC 字體切換與 W43 同形**：svglib diff 核心→本版恰 4 行 TC 面切換（函數名、SC→TC 後綴、_IDX 引用、字體族名），與 W43 同配對 build 的 svglib 形狀一致（另見 §7 偏差 4 兩處非字體差異）。

## 6. 機械門（全實測，本輪 r1）

- **freeze.py baseline**（本輪重建，上一任未留產物）：核心 build 副本重渲染 **8/8 逐字節復現**核心出貨 SVG；收尾複核核心 8 頁 sha256 未變（p1 81051bbb · p2 d42ce9ae · p3 9e45586d · p4 62f75269 · p5 c907b869 · p6 5545f8dd · p7 9fc999f4 · p8 3b87e54f）。產物 `hidden_files/weekly-report-w45-it-zh-tw-build/baseline-w45-it.json`。
- **freeze.py diff**（本輪 r1 與 round-0 存檔 JSON 逐字節相等）：8 頁文本多重集差逐項分類閉合——移除/新增串全為含漢字之講解/家具串；唯一拉丁-only delta 為 P8 分隔 «— PAGINA n —» ×8（→ «— 第 n 版 —»，列定式）與 P8 頭、頁腳行；P1 新增 +1 串 = 徽章。**義大利語正文多重集與核心全等**（去漢字多重集差分每頁僅剩頁腳行、引號轉換、P7 來信說明句重寫之標點殘差、P8 頭/分隔，皆為登記內變更）。
- **新增 CJK 逐頁計數（freeze 口徑，含全形標點/括號）**：P1 104 · P2 65 · P3 60 · P4 59 · P5 78 · P6 61 · P7 120 · P8 424，**合計 971**，與 freeze-diff 吻合；純漢字口徑為 102/65/60/59/78/61/115/420（合計 960），差額 11 = 「」4 對（8 字）+ P7 說明句新增 ；（1 字）+ P8 頭新增 （）（2 字）。新增字皆為繁體講解層/家具，無義大利語正文新增。
- **全文 桥接 0**：8 SVG + 5 content 檔皆 0（「桥」單字亦 0）。
- **p8.py**：核心印刷集 150/150；compare **CLEAN**（missing=[] · extra=0 · uncertain=[]），keydiff 裁定見 §4。
- **occlusion_audit.py**（自檢先行 OK，6 類陽性對照全發、乾淨對照靜默）：終局 **0 旗**，核心 0 旗，NEW vs core **0**。
- **同基線墨迹碰撞（README #10，PIL 真墨盒）**：8 頁同行重疊 **0**（P1 頂欄在內）。
- **框線壓框 + 右緣掃描（ADVANCE 法，PIL getlength）**：8 頁頁緣溢出 0、右框線壓框 0、左框線壓框 0。
- **P6 圖表標籤覆蓋（基線錨定墨迹法，PIL getmetrics，anchor ls；門限 <30%）**：P6 文本墨迹 vs 後繪 rect 重疊 **0 處**（最大覆蓋率 0）；P6 rect 幾何多重集 32 項與核心逐項全等；圖表標籤 Torino 3° / Milano 4° / Bologna 5° / Roma 9° / Napoli 12° 全在位未截斷，練習數據標示 «DATI INVENTATI PER L'ESERCIZIO» 在位。
- **P7 詞框定義句逐字保留（阻塞項）**：LA PAROLA 定義句 wt «« l'assaggio » è la prova di un cibo: un piccolo pezzo per decidere se piace. Questa settimana vive a pagina 3, alla finale del Panettone.» 核心 build 與本版 build **逐字節同**；僅其下 gloss 注本地化（«assaggio = 品嚐。本週見第 3 版：潘妮託尼決賽上觀眾可以免費品嚐。»），定義句本地化 = 0。
- **gloss 渲染後按 · 拆分（README #21）**：源 gloss() 串與核心逐項全等——P2 6 / P3 5 / P4 4 / P5 4 / P6 5，**合計 24**（IT 核心實測分布，非他族數值）；24 個義語詞頭皆在對應渲染頁 SVG 在位；gloss 前綴 «譯注｜» 計數與核心全等。
- **P7 金句 8 句各 2×，標籤與核心一致**：8 條義語金句在全冊合併文本中核心與本版皆 2×（正文 1× + P7 1×）；P7 內 (Pagina N) 標籤計數核心與本版全等（Pagina 1 ×2、Pagina 2 ×2、Pagina 3 ×1、Pagina 4 ×1、Pagina 5 ×1、Pagina 6 ×1）。
- **圖片載荷 = 核心且署名在版**：光柵載荷 sha256（前 16 位）核心與本版全等——P3 松露 9ea4244b4d216b67、P5 栗子 d6bc00b109d273c4，其餘頁無光柵圖（程式繪圖）；署名在版：P3 «Foto: Wikimedia Commons — dominio pubblico»、P5 «Foto: Wikimedia Commons — CC0»、P1 «Disegno della redazione»（霜花為程式繪圖，非照片）。
- **8 張卡片逐頁目視**：P1–P8 全數檢視——無溢出、無重疊、無壓頁腳、TC 字形無缺字/方框；P1 徽章居中、P3/P5 照片與署名、P6 圖表與圖說、P7 來信盒與金句、P8 答案塊收尾皆正常。

## 7. W43 同配對偏差清單（本版 vs W43 IT×ZH-TW）

1. VOL.1 → VOL.2（頁腳、期名行）：隨 W45 核心，非本版自改。
2. P8 幾何沿 W45 核心（非 W43 版式）：練習流底 1252→1332、RISPOSTE 規則線 1264→1344、答案標題 1302→1382、答案流起點 1328→1408、答案字體 13.5→13、行高 1.16→1.14（核心 KIT §6 登記之原因：P8 練習內容溢出原切分）。
3. 註冊表隨核心內容而異：A2 47（W43：46）、B1 70（W43：71）、B2 33（同）；題型 完成句子 61（W43：60）、單選 48（W43：49）；範文 81 詞（W43：90 詞）。
4. svglib 兩處非字體差異（皆不刊印/皆沿核心）：docstring «for 重阳.» → «for Double Ninth.»（註解一詞）；illus_frost 路徑由相對 `l` 改為絕對 `L`（W45 核心自有修正，防審計誤報 bbox，圖形同）。
5. P7 讀者園地說明句依協調員裁定重寫（見 §9），非 W43 舊句。
6. 主題隨核心而異：本期為初寒／文化論壇／潘妮託尼決賽／牛軋糖節／意甲第 11 輪／天氣預報讀法；W43 為其當週主題。keydiff 表隨題目而異（見 §4）；新增 CJK 971（W43：938）。
7. 無偏差項：徽章幾何/字號/顏色、頁腳/頁碼行/ gloss 前綴/P8 頭/分隔定式、TC 面切換形狀，皆與 W43 同配對已上架 SVG/build 一致。

## 8. 針腳（實測，本輪結束時再測，與 round-0 一致，未重渲染）

- 印刷 PDF：`La-Lucerna-VOL2-ZHTW.pdf` **19,412,405 B** · sha256 `392b5d28da9ef19bebca02a4acdd966b0a6b276db071207f38b7bf14781835ce`
- 網頁 PDF：`La-Lucerna-VOL2-ZHTW-web.pdf` **3,450,084 B** · sha256 `fbb6e0a99b857adf1128dd8f112d3e11337255ad87a77e66c0d8a99191cb4acd`（<10 MB ✓）
- SVG：p1 26255475 · p2 f66b946b · p3 f9d7ff55 · p4 8ef6b3ed · p5 22a1f879 · p6 ca108696 · p7 78e22a1f · p8 79e52148（前 8 位，完整值見 build 目錄 sha256-r0.txt，本輪再測一致）
- Cards：p1 d3bb2267 · p2 5dd4b4de · p3 aee5f4a5 · p4 8e944cac · p5 f9bcf22d · p6 070f3b80 · p7 ec8a9bed · p8 43377291（前 8 位，本輪再測一致）
- 雙 PDF 皆 8 頁。

## 9. 讀者園地（協調員裁定，照此執行，實測在版）

- 絕無編造：P7 信件義大利語原文逐字保留核心（含 `(esempio della redazione)` 標籤；lt 串核心 build 與本版 build 逐字節同）；**未新寫任何義大利語披露句子**（P7 義大利語-only 字串多重集與核心全等）。
- 披露句本身以繁體中文寫明 3 事實（P7 卡面實見）：「這是編輯部示例信，非真實來信；本期無最佳第 8 版作文。請寄來信，VOL.3 刊登真實來信與最佳作文！」——(1) 示例信非真實來信 ✓ (2) 本期無最佳第 8 版作文 ✓ (3) 示例＋承諾順延至 VOL.3 ✓。
- 顯性繁體公開徵集邀請：祈使句 «請寄來信» ＋ VOL.3 刊登承諾，載於披露句本身（下期預告行不算邀請，本版邀請不依賴預告行）。
- P7 說明句在 SVG 中跨行折為三段，合併後與上句逐字節同；卡面檢視入框無溢出。

## 10. 修復輪記錄

**無修復輪。** 全部復核門禁一次通過（§6），故未觸動任何已交付 SVG/卡片/PDF，未重渲染；修復前基線記錄程序未觸發（無 pre-fix 哈希表可列——交付物哈希即 §8 值）。若獨立校對發現問題，修復必須同步進 transform.py、單進程重渲染，並另起一輪完整復核。

## 11. 復現與環境

- 解釋器：tools/venv Python **3.12.3** · Pillow **13.0.0** · cairosvg **2.9.1** · OpenCC（s2twp）可用。
- 復現（僅供獨立校對重跑門禁，不重渲染交付物）：
  - `cd tools && ./venv/bin/python freeze.py baseline --build ../hidden_files/weekly-report-w45-it-build --core-svg ../files/weekly-report-w45-it-core/svg --out scratch/baseline-w45-it`
  - `cd tools && ./venv/bin/python freeze.py diff --core-svg ../files/weekly-report-w45-it-core/svg --edition-svg ../files/weekly-report-w45-it-zh-tw/svg`
  - `cd tools && ./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-it-zh-tw --core ../files/weekly-report-w45-it-core`
  - `cd tools && ./venv/bin/python p8.py compare --core-dir ../files/weekly-report-w45-it-core --edition-dir ../files/weekly-report-w45-it-zh-tw --target it`
  - 本輪補充審計腳本：`hidden_files/weekly-report-w45-it-zh-tw-build/audit-r1.py`（輸出 `audit-r1.txt`；唯讀，不 import content 模組、不寫 files/）。
- 摘要檔：`ABSTRACT.txt`（繁體中文單行、無 ASCII 雙引號；insert.py 門檻用；tables.json zh-tw `abstract_heading` = «摘要»）。
