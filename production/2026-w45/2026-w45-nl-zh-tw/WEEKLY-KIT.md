# WEEKLY-KIT — NL×ZH-TW（荷語正文 VOL.2 + 繁體中文講解，W45）

**Status: BUILDER-COMPLETE（建造完成，未定稿——定稿須獨立校對一輪）**

## §0 本版身份

- 配對：目標語 = 荷蘭語（De Lucerna VOL.2，W45 2026-11-02–08）；讀者母語 = 繁體中文。
- 產出：`files/weekly-report-w45-nl-zh-tw/`（svg ×8、cards ×8、印刷 PDF、網頁 PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
- 建造目錄：`hidden_files/weekly-report-w45-nl-zh-tw-build/`（W45 荷蘭語核心 build 的副本 + transform.py + 全部門禁原始輸出）。
- 方法：複製核心 build → freeze.py baseline 8/8 逐字節復現 → transform.py 只改講解層與列家具 → run.py 一進程渲染 → render.py 出卡片與 PDF（README #7）。
- 開工前置核查：出貨目錄與建造目錄均不存在、無本版進行中寫盤（同期 NL×IT 的 insert 進程與本版無關，未受干擾）；開工後 60–120 秒復查零新寫盤外來干擾。
- 繁體講解以台灣/香港用語原生撰寫、逐行審讀（見 §2 方法與 §6 字形掃描），非未經審讀的機械轉換。

## §1 凍結與雙軌證明

- freeze.py baseline（核心 build 改道副本）：**8/8 逐字節一致**，核心 SVG sha256 前綴：p1 5424557b · p2 78e6fcd2 · p3 5b9854e3 · p4 cc227fd9 · p5 e58064c9 · p6 6583fe28 · p7 65cfe2b3 · p8 fe22a151；收尾重哈希核心全等，**核心未被觸碰**。
- freeze.py diff（正文軌）：逐版字串增減對稱（P1 +27/−27 · P2 +21/−21 · P3 +12/−12 · P4 +15/−15 · P5 +21/−21 · P6 +16/−16 · P7 +29/−29 · P8 +142/−142）；新增 CJK 共 **927 字**，全部為繁體講解層與列家具。
- 非 CJK 殘差流比對（逐版 difflib，CJK 剝除後）：差異**全部**歸因於列家具——頁腳（8 版同式）、P1 徽章槽（荷文副標 → 繁體徽章，見 §3）、P1 名牌（荷蘭語周報 → 荷語週報，W43 列先例）、P1 引號裁定（“”→「」1 處）、P8 頭與分隔（見 §3）。**荷蘭語正文殘差逐字節全等**。
- 幾何軌：8 版非文字元素（rect/line/path/image/circle）多重集與核心**全等**（含 P6 圖表柱體 180/100/80/40 px 與全部框線）。

## §2 變換與 svglib

- 變換：`transform.py`（在建造目錄內，拒絕對已變換副本重跑；修復輪 = 重拷核心 + 改本腳本 + 從頭重跑，保證可復現）：
  1. 底本：OpenCC s2twp（tools venv 自帶 opencc_python_reimplemented）對 5 個 content 模組全文轉換；斷言轉換前後非 CJK 字元流全等，故荷蘭語、數字、程式結構零觸動。
  2. 台灣原生修正（逐項計數斷言，全文 diff 逐行審讀後定稿）：
     - 週字：s2twp 遺留的周 → 週（氣候週 ×22、設計週 ×2、歐戰週 ×1；週一/週六/週日/本週/下週由 s2twp 已轉；殘留僅周圍 ×1 與名牌間隔形，後者由家具步替換）。
     - 練習資料 → 練習數據 ×3（統計語境取數據，非 s2twp 的資料）。
     - 程式碼 → 代碼 ×5（全部為 KNMI 顏色代碼：P2 指令 + 2 注、P6 注、P7 金句譯文；s2twp 誤作軟體碼）。
     - 比賽專案 → 比賽項目 ×3（P5 框 + gloss + 注；專案為商務語境誤轉）。
     - 報道 → 報導 ×1、集市 → 市集 ×2（P3 gloss + 注）、把片語成正確的句子 → 把詞組成正確的句子 ×1（s2twp 拆壞把詞組 + 成）。
  3. `.bridge(` → `.expl(` 改名 22 處呼叫 + bslib4 定義 1 處；operative code 內 bridge 0、全文 桥接 0。
  4. OUT 改道：5 個 content 模組（expanduser 形式）+ render.py BASE 改指本版出貨目錄；印刷/網頁 PDF 名：`De-Lucerna-VOL2-ZHTW.pdf` / `De-Lucerna-VOL2-ZHTW-web.pdf`（W43 列字尾先例 -ZHTW）。
- svglib：以核心版為底，僅 EN×ZH-TW §2 的四行 TC 面開關（`_sc_index`→`_tc_index`、`endswith("SC")`→`"TC"`、`_IDX` 呼叫、預設字體族 → Noto Serif/Sans CJK TC），實測解析面索引 = 3（tables.json 口徑 SC=2/TC=3）。NL 核心 wrap() 為樸素貪心換行，行為不變；換行後禁則見 §6 末。
- 渲染：run.py 一進程 **150 題（A2 47 · B1 72 · B2 31）**，逐版 10/18/18/18/18/18/12/38，題型 完成句子 65 / 單選 44 / 詞彙配對 8 / 判斷對錯 7 / 造句 8 / 完形單選 13 / 翻譯 4 / 寫作 1，範文 87 詞，零 FLOW OVERFLOW / HEAD TOO WIDE 警告；P7 三欄尾 1897.0（= 核心 Fix-1 後值；舊 build-log 的 1647 為 Fix-1 前值）、P8 答案流尾 y=2427 < 2552 界。
- 解釋器（run.py 與 render.py 同一解釋器）：`tools/venv/bin/python` = Python 3.12.3，PIL 13.0.0，cairosvg 2.9.1，pypdf 6.21.2。系統 python3 無 cairosvg，未使用。

## §3 列家具登記（繁體列定式，依 W43 NL×ZH-TW KIT §3 驗收版）

| 項 | 本版 |
|---|---|
| 報頭 | De Lucerna（荷蘭語） |
| 名牌行 | 「荷 語 週 報 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12」（W43 列先例：核心五字間隔名 → 四字荷語週報） |
| 徽章 | **核心自有副標槽（y=372）就地替換**：荷文標語 → 「荷語正文 · 繁體中文講解 — 給繁體中文讀者的版本」，19.5pt sans bold BRICK 居中（NL 家族出貨先例 NL×KO 同槽同式；README #20 副標槽家族情形；此為家具，非正文凍結項） |
| 頂欄中 | 「ELKE WEEK IN HET NEDERLANDS · 每週一期 · 讀荷蘭人正在讀的荷蘭語」（與 W43 列同式） |
| 黑帶右 | 「氣候週」／「本週全國氣候週 · 詳見第 2 版」 |
| 頁腳 | 「De Lucerna · 荷語週報 VOL.2 · 正文荷語 · 講解繁體中文」（8/8） |
| 頁碼 | 「第 N 版 / 共 8 版」（8/8，核心原式共形字不變） |
| 欄目標題 | 頭條/生活/文化/體育/青年/深讀/語言 + 練習標題「第 N 版練習」；P8 帶標「第 8 版 · De grote toets…」（荷文凍結） |
| P8 頭 | 「ANTWOORDEN · 全部答案與簡析（第 1–8 版）」；副行「每題附一句中文簡析 · 帶 ✓ 的為範文題」（W43 列先例：核心「參考答案 — 按版面分頁排列」頭改為列定式，分頁資訊由分隔承載） |
| P8 分隔 | 「— 第 N 版 —」×8（替核心「— PAGINA N —」） |
| P8 注式 | NL 家族**短橫式**「N. key — note」（答案生成碼未動，僅字串替換；README #8/#14 以家族出貨代碼為準） |
| gloss 前綴 | 「譯注｜」（bslib4 gloss()）；P1 講解行保留「講解｜」前綴（核心原式，TC 字形） |
| 引號裁定 | 講解層彎引號 “” → 台式「」（1 處：P1 本週生詞「氣候」；W43 列為 3 處，本期核心僅此 1 處） |

## §4 印刷注釋門（p8.py）

- p8.py extract 核心 P8：**150/150 全印**（短橫式，與工具錨點一致）。
- p8.py compare：**CLEAN，印刷集 150 = 150**，missing=[]、extra=0、uncertain=[]。
- compare 報 keydiff 8 項 [7, 70, 71, 76, 96, 137, 138, 148]：其中真差異僅 {137, 138, 150}（見 §5，150 不在 compare 表內因 ✓ 裝置項提取同鍵）；其餘 6 項全為 README #13 行級偽影——逐項查證：6 條注文均以全角「（…）」收尾，p8.py 在括號分支將注文前段誤作鍵（如 #7 提取鍵「B — 氣候週共 7 天」vs 實印鍵 B）。SVG 級抽證（印刷鍵 token 與核心逐字節相同）：#7 B、#70 eiland、#71 proef、#76 gaat winnen、#96 advies、#148 B。註冊表比對（§5）為準。

## §5 鍵差異登記表（註冊表實測，權威口徑）

註冊表雙 dump（核心 build 副本 vs 本版 build 副本，各自一進程 dump 後比對）：
n/版/級別全等；TYPE 差異 77 項全為型名簡→繁對譯（單選/完形單選/判斷對錯/翻譯/詞彙配對/寫作）；注文變更 119/150（餘 31 條字形中立——荷文/數字/共形字注文）。**KEY 差異恰 3 項**：

| # | 類 | 核心鍵（簡體講解版） | 本版鍵 | 說明 |
|---|---|---|---|---|
| 137 | 翻譯題 | 气候周持续七天。 | 氣候週持續七天。 | 譯文鍵本身（E 區翻譯題） |
| 138 | 翻譯題 | 橙色预警意味着：做好准备。 | 橙色預警意味著：做好準備。 | 譯文鍵本身（E 區翻譯題） |
| 150 | 裝置項 | （开放题，范文如下） | （開放題，範文如下） | 寫作範本裝置（印刷作 ✓ 範文見本版 H 區（87 詞）） |

題幹改向 2 項（鍵為荷文不變，屬上表外）：#139 題幹「博物馆之夜从晚上 19 点到凌晨 2 点。→ ___」→「博物館之夜從晚上 19 點到凌晨 2 點。→ ___」；#140 題幹「我参加气候周。→ ___」→「我參加氣候週。→ ___」。

## §6 機械門與掃描結果

- occlusion_audit.py（自檢先行通過，6 類全發、乾淨對照靜默）：本版 **0 旗**、核心 **0 旗**、**NEW vs core = 0**。
- 同行墨跡碰撞掃描（README #10，複用 canonical 審計真墨盒，checks.py）：核心 0 · 本版 **0**。
- P6 圖表標籤覆蓋（README #12 盲點，checks.py 基線錨定墨跡法：PIL getmetrics ascent/descent、anchor ls、4×  supersampling 還原，getbbox 法不用）：四條標籤 + 數值（45/25/20/10）與後繪柱體交疊 **0.0%**（<30% 過；標籤在柱上方 10px，數值右對齊無觸碰；柱寬 180/100/80/40 與核心全等）。
- 簡體字形掃描（三軌）：
  (a) 交叉核對——本版全部 CJK 字元對 W43 繁體版（weekly-report-nl-zh-tw）+ 繁中核心字集（W45 zhtw core + W43 zhtw vol1，共 1127 字）：未見字元 56 個，逐字逐語境裁定**全為正規繁體形**（僅舉易混項：周圍之周、建議之建、腳踏車之腳/踏、茲韋洛之茲/韋、薩格勒布之薩、只是猜測之只——只在此為「僅僅」義，繁體正字；郵局類殘留 0，本期無郵政詞彙）。
  (b) 簡體專有字形塊掃描（發/讓/說/國/對/車/馬/門/問/電/話/語/學/頭/義/云/龍/著/鐘/種/獲/達等）：命中僅「只」×1（上列正當用例），其餘 0。
  (c) 大陸詞彙掃描（搜索/谷歌/数据/信息/视频/网络/软件/质量/出租车/上网/网友/博客等）：**0**。台灣用語在版：搜尋無（本期無此詞）、腳踏車、數據、市集、報導、比賽項目、代碼。
- 他列家具殘留 0；禁用術語：operative code 內「bridge」0、「paper」僅餘核心庫顏色常量名 PAPER（繼承性標識符，非版面文字）；svglib 內 illus_climb docstring 含「重阳」二字為核心庫非渲染註釋，同例登記（W43 列同款例外）。
- gloss 詞條逐條點數（渲染後 gloss() 字串拆 · 計數，首行起算）：P2 6、P3 5、P4 5、P5 5、P6 5，**與核心逐項 1:1**（P3 第 2 項「de rondleiding 導覽」跨行不斷義，僅接合顯示為連寫）。
- P7 詞框凍結：核心荷蘭語定義句「«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.」**逐字保留**，僅 gloss 本地化為「meedoen = 參加、參與：氣候週全荷蘭都參加。」。
- P7 金句：8 句荷文逐字回溯本期正文驗真（裸句各出現 2×：正文 1 次 + P7 引文 1 次，與核心全等），頁標籤序列 [1, 1, 2, 3, 4, 5, 6, 6]，每句在其標註頁上實測存在；P7 短語逐字取自本期文章。
- 讀者園地（零編造）：頁上同時有三事實——截稿時無真實來信（荷文披露句原文保留、繁體披露句同義）、無最佳 P8 作文（同句內）、示例 + VOL.3 承諾——與顯性繁體邀請（祈使句「歡迎寄來你的真實來信和第 8 版最佳作文，VOL.3 刊登！」）；示例標註為編輯部示例（「Li (voorbeeldbrief van de redactie)」+「編輯部示例信，非真實來信」）。
- 圖片/署名：僅公有領域/CC0 圖片（核心 KIT §5，2026-10-21 經 Commons API Artist 欄位核實）；4 張署名圖片均排版在版面上且 credit 行在位：P1 herfstbos Vovogov90 CC0、P2 kinderdijk Nationaal Archief CC0、P3 gracht W. Punt / Anefo, Nationaal Archief CC0、P4 elftal1912 Spaarnestad Photo 公共領域。
- 禁則掃描附記（繼承性換行）：P6 圖說末行 lone「）」、P7 A2 讲解末行 lone「。」、P7 B1 讲解行首「：」——三處與核心 SVG 逐行結構全等（同字數、同字體、同寬換行），為核心樸素換行器的繼承行為，非繁體引入，不改（改動即破凍結）。
- 日曆對照（Europe/Amsterdam 實曆，核心 KIT §4 已驗）：2026-11-02 週一 · 11-03 週二 · 11-07 週六 · 11-08 週日——與版面全合。

## §7 目檢記錄（8 張卡片逐頁）

- P1：徽章（磚紅 19.5pt）/名牌/黑帶/頭條/數字框/日程/生詞框/閃電問答/照片 + Foto: Vovogov90 — CC0 均正常，無重疊、無截斷。
- P2：codes 四框/口訣框/譯注框/風車照片 + credit 均正常。
- P3：運河照片 + credit、譯注框、練習區均正常。
- P4：Fix-1 後頭條「Europa: drie keer feest, twee keer verlies」、1912 隊照 + credit、譯注框均正常。
- P5：無照片頁；Robinson 框/譯注框/練習區均正常。
- P6：圖表四柱 + 標籤 + 數值無遮擋；正反方框/譯注框/練習區均正常。
- P7：BRIEVEN 框內全部行在框線內（含披露 + 邀請末行）；HET WOORD 框、金句帶、VOLGENDE WEEK 黑帶均正常。
- P8：練習區 + 全部答案區（分隔 — 第 N 版 — ×8、頭「全部答案與簡析（第 1–8 版）」）均正常，答案流尾在界內。

## §8 實測針腳（交付時點，磁碟實測）

- 印刷 PDF：`De-Lucerna-VOL2-ZHTW.pdf` — **8,735,263 B**，
  sha256 `f383951427de58679dc650e5ef22fd976a4c8998662cecaffa8e222076983421`，
  8 版，版面 1462.5 × 2025 pt（與核心印刷版同規）。
- 網頁 PDF：`De-Lucerna-VOL2-ZHTW-web.pdf` — **1,477,633 B**（< 10 MB），
  sha256 `c29697927c8bb6cf8690270a4480f8d029eddf2a38b37445b80a1d7bc373e0e9`，8 版，版面 1400 × 1938 pt。
- 卡片：8 張 1950×2700 PNG；SVG 8 張；試題總量 **150**（A2 47 · B1 72 · B2 31），印刷注釋集 150/150 CLEAN。
- 渲染輪次：本版僅一輪渲染（run1）；修復輪基線 `baseline-run1.sha256`（svg/card/PDF 全量）存於建造目錄；任何後續修復輪須先寫當版完整 sha256 基線再重渲染，且改動須同步進 transform.py。

## §9 建造日誌與復現

- 建造日誌：`hidden_files/weekly-report-w45-nl-zh-tw-build/` — transform.py（含全部斷言）、transform 執行輸出、build-log-run1.txt、build-log-render1.txt、checks-run2.txt（rowcheck 0、圖表 0.0%）、p8-compare.txt、occlusion.txt、freeze-diff.txt/json、reg-core/reg-ed 註冊表雙 dump、baseline-run1.sha256、core-svg-sha256-before.txt（核心收尾重哈希全等）。
- 復現：重拷 `hidden_files/weekly-report-w45-nl-build` → 執行 transform.py → `run.py`（一進程）→ `render.py`，即得本版出貨檔（除 PDF 內嵌時間戳外位元組一致；SVG/card 逐字節一致）。

## §10 交付說明

- 本版僅為建造完成（builder-complete），**未宣布定稿**：定稿須獨立校對一輪（凍結、字形、P8、遮擋、目檢全量復核）通過後方可入倉。
- 未入倉、未發 Discord、未往主聊天發卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目錄（只讀對照）。

## §11 D5 rebuild（2026-11-14，builder run；非校對輪）

D5: 讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK（SOP §1.1 字体修复）。D5-only 家族：新样式已在仓，单版施工只装 D5、重渲一次。

- Core 落盘（全家共用一次，v1 执行）：`apply_variant.py --patch-core nl --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-nl/svglib.py` +95/−3 行，`_D5_READER = "latin"`（D24：按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-nl-zh-tw/svglib.py --target nl --reader zh-tw --week 2026-w45`（先 `--check` dry-run，mode=cjk）。装后 `_D5_READER = "cjk"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（svglib.py 含 fix2 标记 13 处，安装器日志 "added fix2 block"）。
- 基线（修前生产版，venv 重建）：`run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；印 PDF 19,997,826 字节；印/网文字层 vs issues 已发 web PDF 字符多重集差 **0**；修前普查 D5 违规 **拉丁 323**（>0，符合装机前提）。旧 pin 与基线实测不符（de 例：KIT 印 7,918,211 B，基线实测 7,526,971 B）——KIT SHA 滞后（PLAN 修正案：基线永不以 KIT SHA 为准），本节 pin 以实测发运值订正，旧 §8 pin 已同步更新为本次值。
- 导出器（第 0 步自验）：`scratch-2026-w45-nl/export_text_w45nl.py`（AST 导出，源自 content*.py 字面量，绝不从 PDF 反提；无 hardcode，标题由参数传入）。基线试跑 vs issues 已发 `.text.md` **11/11 BYTE-IDENTICAL**；patched 导出同样 BYTE-IDENTICAL（门 15）。
- 修复（run1 → run2）：共 **3 处**，只动字号，零文字改动。run1 缺陷：栏头超宽 3 处（ru 除外，ru 栏头未超）、occlusion TEXTX 1 处（P7 B1 栏头 'SCHEIDBARE WERKWOORDEN' 与 'B2' 重叠 5.2×17.8px；ru 除外）、boxtitle/creambox 0 处（ru/zh-cn/zh-tw 为 0），ru 另有 spill 1 处（codes 行注 'внимательны' 框底溢出 BELOW +13.34px）。
  - `content12.py:175` 栏头 DRIE ACTIES VOOR DEZE WEEK：25 → **24**（宽 425.0px；修后 408.0px）。
  - `content34.py:21` 栏头 TWEEDEHANDS IS OOK CULTUUR：25 → **23**（宽 456.7px；修后 420.1px）。
  - `content7.py:32` 栏头 B1　SCHEIDBARE WERKWOORDEN：24 → **22**（宽 455.7px；修后 417.8px）。
- 门禁（run2，全套 16 门 + D18）：**ALL-GREEN**。run TOTAL 150 / head_check 0 defects / d5 census 拉丁 0、西里尔 0、CJK 内花括号 0 / render RC=0 / webpdf RC=0（网 PDF 1,477,633 B < 7 MB）/ occlusion 0 flags（selftest 6 类全触发）/ p8 extract 150/150 / p8 compare CLEAN（missing=[] extra=0，keydiff=[137, 138]，137/138 为读者语重定向真重 aim，已裁定，非缺陷) / freeze baseline 8/8 / freeze diff vs base 新增 CJK 字符 **0**（新增拉丁 strings 420，D5 run 拆分所致；对照是 base 修前生产版，不是 core）/ spill 0（1 OBSERVE）/ boxtitle 0 / edge 0 TOUCH 0 NEAR / creambox 0 defects（P8 220 → 220 行，距页脚线余量 57.4px）/ 文字层 print=web 字符多重集差 **0**（28,652 字符），text.md BYTE-IDENTICAL / census_quotes 0 defective / D18 刊头 gap **105.1px** > 0。
- 补充校验 G15b（carryover，诊断性，不计入 verdict）：共享 `verify_textmd.py` 对 nl 目标家族未标定（表按 pt 目标语格式标定），patched 与基线同态 FAIL（de 例：SVG-only 711 / MD-only 1119，基线 711 / 1121；ru、zh-cn 基线与 patched 残差完全相同）——D27 类已知工具口径差，非 D5 回归；内容不变的证据以门 15（AST 导出器 BYTE-IDENTICAL + print=web 差 0）为准。
- 最终 pin（builder 原件；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）：印 PDF `De-Lucerna-VOL2-ZHTW.pdf` 8,735,263 B，SHA-256 `f383951427de58679dc650e5ef22fd976a4c8998662cecaffa8e222076983421`；网 PDF `2026-w45-nl-zh-tw.web.pdf` 1,477,633 B，SHA-256 `c29697927c8bb6cf8690270a4480f8d029eddf2a38b37445b80a1d7bc373e0e9`；text.md 37,541 B，SHA-256 `1b0d2d7139573bdcdb2f869acc00c4cc06f48cceab26a784e0f7233c4035a1f6`（与 issues 已发版 BYTE-IDENTICAL）。
- Builder scratch：`hidden_files/d5-redo/scratch-2026-w45-nl/patched/2026-w45-nl-zh-tw/`；门禁总表复本（D29）：`production/notes/2026-w45/g-nl/scratch-d5-rebuild-nl/logs/2026-w45-nl-zh-tw/GATES-SUMMARY.txt`。
