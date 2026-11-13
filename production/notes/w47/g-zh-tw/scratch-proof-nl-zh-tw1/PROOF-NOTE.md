# PROOF-NOTE — 2026-W47 · nl → zh-tw（荷蘭語目標語 × 繁體中文讀者）· proof1 獨立復校（build-3）

- 版目錄：`production/2026-w47/2026-w47-nl-zh-tw/`（規範路徑；staging 副本 `production/2026-w47/fanout-nl/2026-w47-nl-zh-tw/` 僅作對照）
- 復校員：獨立復校（proof1）· 2026-11-11
- 依據：倉庫根 `SOP.md` §8（全量 proofread、答案逐題復核、8 版逐版看圖、循環規則）+ 附則一/二（幾何遮擋審計、共享工具）；`~/workspace/weekly-git/AGENTS.md`（定稿須一輪全量獨立復校零問題 + 幾何審計零標記）
- 工作區：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-zh-tw1/`（TMPDIR 全程指向其下 `tmp/`；/tmp 512M 未用）
- 本輪校的是 delta build-3（core-nl fix3+fix4+fix5 同步）。**注意**：本目錄內此前留有一份 11:54 的舊 build 復校（PROOF-NOTE/GATE-LOG 舊版），其三 SHA（印 `a2a86521…` / 25,995,622 B）與 staging（`3a81e9cf…`）和本 build-3 均不符；舊版所列 D1/D2/D3 在本 build-3 上逐一重測，結果見「未復現項」——本文件只對 build-3 下結論。

## 結論：(a) 零缺陷可定稿

全量復校一輪零問題。150 題答案鍵三源逐題比對 149/149（Q150 為開放寫作例外）；8 頁交付印 PDF 逐頁目視；全部機械門禁通過；D6–D11 六處 delta 修復逐項實測通過；上一輪（舊 build）的三項缺陷在本 build-3 上均未復現（見下）。無缺陷清單——按任務硬要求，結論只寫 (a)，不寫「基本通過」。

## 身份核對（磁碟實測 = 任務給出值，全部一致）

| 文件 | 字節 | SHA-256（實測） |
|---|---|---|
| `De-Lucerna-VOL4-nl-zh-tw.pdf`（印） | 25,993,186 | `6de893ca2811357c7be524b2b17e78af1c5362abc647e957d8665559466c704a` |
| `De-Lucerna-VOL4-nl-zh-tw-web.pdf`（網） | 2,369,230 | `172c1be81d32d871c323064c685e0918e41b12b29a25a19a50cf4926d217ff20` |
| `2026-w47-nl-zh-tw.text.md`（文） | 44,320 | `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60` |

- 探針：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2…`，rc=0；goals-side scratch 寫入探針文件成功。磁碟 150G 總 / 91G 已用 / 59G 空閒。
- 改動範圍核對（`diff -r` 本版 vs staging，排除 svg/cards/PDF/`__pycache__`）：僅 7 個文件不同——`bslib4.py`、`content34.py`、`content56.py`、`content7.py`、`content8.py`、`2026-w47-nl-zh-tw.text.md`（diff 恰好 1 行：text.md:415 `kort `，+5 B）、`WEEKLY-KIT.md`（新 SHA + delta 節）。與 delta 聲稱一致，無其他源文件被碰。
- SVG 字節核對：p1/p2/p5 與 staging 逐字節一致；僅 p3/p4/p6/p7/p8 變化（與 delta 聲稱一致）；8 個 SVG 哈希與 delta `svg-hashes-after.txt` / `svg-hashes-postcompare.txt` 逐一相符（p7 `d7e08e59c1d8…`）。
- KIT 所載三 SHA 與上表實測一致（`WEEKLY-KIT.md:20-21,24-25,29,179-180`）。

## 機械門禁（全部通過，詳見 GATE-LOG.md）

| 門 | 實測值 |
|---|---|
| `run.py` | rc=0，TOTAL 150，by page 10/18/18/18/18/18/12/38，A2 46 / B1 73 / B2 31；0 FLOW OVERFLOW / HEAD TOO WIDE |
| occlusion 審計 | `tools/occlusion_audit.py svg/` rc=0，**0 flags**（自檢通過） |
| p8 extract | noted set **150/150** |
| p8 compare（核心 vs 本版） | **CLEAN**，missing=[]，extra=0，uncertain=[]，**keydiff=[137, 138]**（翻譯題合法重定向，見下） |
| freeze baseline（核心） | `freeze.py baseline --build core-nl --core-svg core-nl/svg` rc=0，**8/8 字節一致**，core integrity 行確認核心未被改動 |
| 版內自比對 | clean-dir 重跑 `run.py` 再 sha256 比對 **8/8** |
| freeze diff | rc=0，新增 CJK **1051 個，全部繁體**（見簡繁殘留掃描） |
| 印/網文字層 | 8 頁 posdiff=0、msdiff=0（tokens 749/705/664/658/685/648/735/1677）；pdftotext 印=網=44,329 B；網 PDF 2,369,230 B < 7 MB |
| P8 最小字號 | 答案區 min **10.12pt**（median 10.12，566 spans）≥ 9.75pt（SOP §1.1） |
| P8 級別徽章 | A2 8 / B1 24 / B2 3，核心與本版一致 |
| §1.1 SVG | off-palette={}，無 GOLD/舊色，無 stroked rect，VOL.5=5=core，paper fills 8 |

## Delta 六處修復逐項實測（本輪獨立重測，非抄 delta 日誌）

| 點 | 實測值（交付件） | 證據 |
|---|---|---|
| D6 P3 橋接 | 2 行：`用現在完成式填空。注意助動詞` (y=2250.5) / `hebben/zijn。` (y=2280.225)，`。` 在行 2 末尾 | `svg/p3-cultuur.svg`；孤兒橫掃 class-a=0 |
| D7 P7 橋接 | 3 行乾淨：`de wedstrijd 比賽；de groepswinst` (725.66) / `小組頭名；de kwartfinale 八強賽；` (755.385) / `scoren 進球。` (785.11)；術語完整、無行首標點 | `svg/p7-taal.svg`；孤兒橫掃 class-b=0 |
| D8 P6 圖注 | 2 行，基線 635.02/659.44：`練習數據：虛構數字，僅供練習，非真實調查。` / `問題：你在鞋裡放什麼？（100 名年輕人）`；`。` 在行 1 末尾；圖表盒（底 665.0）真墨余量 +4.00px（cards）/+4.52px（交付 PDF 150dpi），盒底下 7px 條帶 0 非紙像素 | `svg/p6-verdieping.svg`、P6 全盒探查（見 GATE-LOG §9） |
| D9 Q140 | 三源逐字一致：registry 鍵 = text.md:415 答案 = P8 節點，均為 `Ik maak een surprise met een kort gedicht.`（`kort` 在場）；其餘 149 鍵未動；3-way 比對 **149/149 MATCH**，DIFF=[]，MISSING=[] | `p8-compare-3way.json`；`content8.py:75` 含 `kort`；題幹 `我做一個帶小詩的偽裝禮物。` 含「小」，key 與詞幹一致，無殘留 |
| D10 P7 來信 | 2 行，基線 1754.27/1782.67：`截稿時未收到真實來信或第 8 版最佳作文，` / `刊登示例信，承諾順延 VOL.5。`；`，` 在行 1 末尾 | `svg/p7-taal.svg` |
| D11 P4 盒 | 盒 `<rect x=1439.5 y=591.6 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基線 1209.49，基線余量 **+20.11px**；真墨余量 **+20.60px**（cards 1×）/ **+20.48px**（交付印 PDF 150dpi 渲染）；盒底下 7px 條帶 0 非紙像素（雙渲染）；spill 掃 P4 該盒 0 BELOW 命中 | `svg/p4-sport.svg`、`inkprobe-d11-delta` 方法重跑（見 GATE-LOG §7）；P4 目視末行在盒內、下有明顯留白 |

- 全版孤兒標點橫掃（重建 SVG 上獨立重跑，PIL + svglib 雙 advance，1419 行）：獨行標點 **0**、行首標點 **0**，兩方法 8 頁全 0；brute-force 行首標點 `<text>` 元素 8 個，其中行內最左 **0 個**（其餘 8 個均為行中定位符：P1 `：柏林奧林匹克`、P8 答案區 4 個 `：`/1 個 `，`/3 個 `）`，非行首）。修前為 1/3，見 delta 日誌 §1。
- p8 compare keydiff [137, 138] 裁決：137、138 為 E 節翻譯題（NL→繁體中文），鍵本身就是讀者語；核心為簡體（`圣诞老人新闻每天 18:00 播出。` / `前两名晋级四分之一决赛。`），本版為繁體（`聖誕老人新聞每天 18:00 播出。` / `前兩名晉級八強賽。`），按設計不同，非缺陷。修前 [137, 138, 140]——D9 已把 140 移出該表。
- 配對字母已對印刷選項逐項核對（非僅三源一致）：P2 D 選項 a=`een lijst met wensen voor Sinterklaas`、b=`een klein versje bij een cadeau`、c=`eten voor Sinterklaas' paard`、d=`die staat 's avonds bij de deur`，鍵 25→d、26→c、27→a、28→b 全部正確；P8 F 選項 a=`een klein versje bij een cadeau`、b=`een dagelijks nieuwsprogramma op televisie`、c=`de eerste plaats in de groep`、d=`die staat 's avonds bij de deur`，鍵 141→b、142→c、143→d、144→a 全部正確（P8 SVG y=807.05/845.05/916.05/954.05）。

## 盒標題逐一光柵復測（定義與計數如實註明）

- **標題定義（本輪）**：Flow head 32 項（`HEADS_SRC` 源字符串，`NU JIJ　YOUR TURN`…`H　SCHRIJF ZELF`）+ 奶油盒標題 26 項（每奶油框內最小 y 的 700-weight 文本，框右緣內 22px 為限）= **58 項**。Brief 模板的 "56 titles" 是模板數，不以它為準；本版實測 58（nl-en 超集 59、nl-it 超集 85，定義不同，各版自報口徑）。
- **結果：57 項通過；1 項方法偽旗已裁決為觀察項（非缺陷）**，見下。最緊的三項通過余量均為 +0.5px（P1 `NA DE INTOCHT: DE SCHOEN`、P2 `A　BEGRIJPEN` / `C　SCHOEN EN GEDICHT` / `D　WOORDEN`），均為真墨恰在欄內，無越邊。
- **P8 head `A　VUL DE KRONIEK IN`（掃描值 −26.5px）——觀察項，非缺陷（STRADDLE 規則裁決）**：
  - 標題本身 PIL advance 僅 264.92px（Newsreader SemiBold 21pt），自 x=88 起墨止於 x≈353，距欄右緣 510.5 有 **+157.6px** 余量；
  - 超限墨只出現在 y=173–181 行（基線 201 之上、字形 cap 頂之外），即 B 欄 B1 徽章矩形（`svg/p8-toets.svg`：`<rect x=538.5 y=180.0 w=60.0 h=30.0 fill=#46581f>`）與欄頭橫帶，不是標題字形；
  - 字形帶（y≈186–213）內 510.5 右側**無墨**；交付 PDF 150dpi 渲染裁圖目視：標題完整、無裁切、與鄰欄無重疊；
  - staging 備份 cards 同值（ink_right=537、同行）、交付 PDF 同值——**與備份舊版無差異，非 delta 引入，非回歸**。符合任務給定的三判據之反面，故記觀察項，不判缺陷。
- **P5 CREAMSTRIP「REAL OVERFLOW」翻案（腳本偽旗，非缺陷）**：`boxtitle_inkscan_delta.py` 硬編碼的 P5 盒底 1023.5 在本版是錯的——本版 P5 奶油盒實為 `<rect x=1439.5 y=632.0 h=304.5>`，**真底 936.5**；y=1023.5–1030.5 的探查條帶落在盒下照片內（`svg/p5-jongeren.svg`：`<image x=1439.5 y=962.5 h=250.0>`），故 2961/2961 非紙像素。按真底重探：盒底下 7px 條帶 **0 非紙像素、0 墨**（cards 與交付 PDF 雙渲染）；末行 `禮物加小詩？寫兩句荷蘭語寄來。`（基線 932.05）真墨底 933.0/933.12，余量 **+3.50px / +3.38px**。在盒內，非溢出。
- P2 / P6 奶油盒已同法全盒重探（見 GATE-LOG §9）：P2 8 盒、P6 3 盒，盒底下 7px 條帶全部 0 非紙 / 0 墨；末行真墨余量最小 +3.43px（P2 EN JIJ 盒，交付 PDF）、+4.00px（P6 D8 圖表盒，cards）。creambox 的 desc-clear 負值（P2 EN JIJ −1.6、P5 −1.5、P6 +0.0）均為固定降部余量假設對中文行（無降部字母）的模型偽報，已由真墨翻案。

## 上一輪（舊 build）三項缺陷在本 build-3 上均未復現

舊版 PROOF-NOTE（11:54，印 SHA `a2a86521…` / 25,995,622 B，與 staging 及本 build 均不符）所列 D1/D2/D3，本輪在 build-3 交付件上逐一重測：

- **舊 D1（P2 D 選項 c 超出右版心約 12px）——未復現**：本版選項 c 文本已改為 `c. eten voor Sinterklaas' paard`（`svg/p2-leven.svg` y=2233，x=1473.5，size 23）。三法一致：PIL advance 右緣 1790.09（Regular）/ 1808.77（SemiBold），余量 +71.91/+53.23px；交付印 PDF span bbox 右 1346.04pt，余量 +50.46pt（≈+67.3px）；150dpi 光柵最右墨點 1793.28，余量 **+68.72px**。P2 SVG 與 staging 字節一致——該改寫在 build-2 staging 已在位，非本 delta 改動，但本 build-3 確無此缺陷。
- **舊 D2（網 PDF 丟失 P1 本週詞斜體）——未復現**：印 PDF 與網 PDF 各有 **1 處** italic span，同詞 `«de groepswinst»`、同字號 16.12pt：印版 `Newsreader16pt-Italic`、網版 `LucernaNewsreader-Italic`。webpdf 已帶斜體面。
- **舊 D3（兩節目專名譯名不統一）——未復現**：本版 text.md：`聖誕老人新聞` ×8（text.md:106/118/304/387/392/405/412/427，含 Q121:392、Q137:412、Q149:427）、`辛特克拉斯新聞` ×0；`《荒島遠征》` ×3（:239 gloss、:244 Q65、:374 金句 #6）、`《魯濱遜遠征》` ×0。印 PDF 文字層：`辛特克拉斯新聞`/`魯濱遜遠征` 0 次、`聖誕老人新聞` 8 次；P8 SVG 0 次。staging 的 text.md 計數與本版完全相同（diff 僅 text.md:415 一行），故 D3 在 staging 已不存在。

## 全文通讀（text.md 431 行全文 + 交付印 PDF 8 頁逐頁目視）

- 荷蘭語拼寫、變位、性數、標點逐行讀過；講解層逐項對照正文（注釋詞均出自正文；方框詞與填空題一一對應）。
- 答案逐題復核：150/150 與 P8 印刷鍵一致（3-way）；算術重算：19 天（11/16→12/5）、1 天（11/14→15）、4 小時（12:00–16:00）、17 年（2009→2026）、65（35+30）、100（35+30+20+15）、13 天（11/22→12/5）；範文 Tekstmodel 實數 **81 詞**（80–100 內）。
- 日期/星期 8 個全部用 `date` 核驗吻合：14/11 週六、15/11 週日、16/11 週一、21/11 週六、22/11 週日、24/11 週二、29/11 週日、5/12 週六。
- 金句 8 句逐字出自本期正文，頁碼標註正確（P1×2、P2、P3、P4、P5、P6×2）。
- 外部事實核實（2026-11-11 檢索）：Heel Nederland Leest 2026 中央書為 Herman Koch《Het diner》（2009），11 月全月圖書館免費領取、非會員亦可，另有大字版/Makkelijk Lezen/電子書/有聲書與讀書會——CPNB 官網（cpnb.nl）+ nl.wikipedia + 多家地方媒體一致；VOL.5 預告三場賽事：歐冠第 5 輪 11 月 24 日週二 Real Madrid–PSV、Feyenoord–FC Porto（uefa.com），荷甲 11 月 29 日週日 14:30 Feyenoord–Ajax（KNVB 官方賽程，De Kuip）；PSV 26 分、Cambuur–PSV 2–5、Grave/Amsterdam 入城細節與舊 build 復校的外部核實一致，且相關正文自 build-2 起未動（text.md diff 僅 :415 一行）。
- 簡繁殘留掃描：text.md（395 個異體 CJK）與 SVG（414 個）中簡體專用字僅 `文` 一字——`文` 為兩岸同形字，非殘留；`征` 3 處均在「遠征」中（繁體正確用法）；無 `台`；**零簡體字殘留**。
- freeze diff 移除串核查：移除的拉丁串均為家具/講解層合法本地化——刊頭 `LUCERNA DUTCH WEEKLY`→繁體刊頭副標；`perfectum`→「完成式」（P8 答案注 40/42）；金句 #8 譯法由核心簡體「传统因人们不断庆祝而活着」改為更貼合荷文的「傳統會一直活下去，只要人們繼續慶祝它」；PAS OP 例句注「放鞋子要说 mijn schoen（我的鞋）」→「mijn schoen = 我的鞋子。」。無荷蘭語正文丟失。
- ABSTRACT.txt：單行、無 ASCII 雙引號，含刊名 Lucerna、VOL.4、目標語名、150 道練習題、A2–B2、繁體中文講解（SOP §9 通過）。
- 8 張圖片均帶目標語圖說 + CC0 出處；圖注與核心一致。P1 HET WOORD gloss 末行與分隔線有間隙，未壓線（P1 目視）。

## 觀察項（非缺陷，記錄備查）

1. P8 head `A　VUL DE KRONIEK IN` 掃描值 −26.5px（見上文裁決；與 nl-ko 同值同因，nl-ko proof1 正按 STRADDLE 規則裁定）。
2. 盒標題最緊余量 +0.5px ×4 處（P1/P2 頭題），真墨在欄內，無越邊。
3. P4/P5/P6 版面中段有設計性留白（欄目結束後的空帶），非內容缺失。
4. 方法備註：`gates_delta.py` 的 `p8_compare` 項計數的是 stdout 裡 `key diff` 行（0），與 `p8.py compare --json` 本體的 `keydiff=[137, 138]` 口徑不同——後者為準，兩者均已如實記錄，不構成不一致。

## 透明說明（本輪操作對生產文件的影響）

- 全程只讀生產；未 commit、未 push、未重渲染交付的 web PDF。
- 例外說明：為取 registry 而在版目錄內 `runpy` 執行 content 文件時，8 個 SVG 被原地重寫（mtime 變為 19:40–19:41 UTC），但重建是確定性的——**8/8 哈希與 delta 的 `svg-hashes-after.txt` / `svg-hashes-postcompare.txt` 所載交付值逐一相符**，且 `git status` 顯示版目錄為未跟蹤（`??`），無任何已跟蹤文件被改動。交付三件 SHA 在收尾時重新核對，仍與任務值一致。
