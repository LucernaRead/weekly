# PROOF-NOTE — 2026-W47 it-zh-tw（獨立復校 proof1）

- 復校員：proof1（只讀，未修版、未 commit、未 push）
- 日期：2026-11-11
- 復校對象：`~/workspace/weekly-git/production/2026-w47/2026-w47-it-zh-tw/`
- 對照 core：`~/workspace/weekly-git/production/2026-w47/core-it/`（盤上已是 fix3 狀態，見 §1 末）
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-it-zh-tw1/`
- 先讀：本版 WEEKLY-KIT.md、core-it fix3 commit 36bdec2e、it-de / it-nl proof1（方法與缺陷類別參照）

## 0. SHA 核對（三件與任務所給一致）

| 件 | 大小 | SHA-256 |
|---|---|---|
| 印刷 PDF `La-Lucerna-VOL4-ZH-TW.pdf` | 27,779,760 B | `6171fea645bd67e0c06d77934229c727b71465aec3fc3f42a82a41ab1933e9f0` |
| 網頁 PDF `La-Lucerna-VOL4-ZH-TW-web.pdf` | 2,042,022 B | `57e29e6ff725a3c093e4d1a51f9d2c0113aeff8c8481e62c27752da0e43fce16` |
| 文本導出 `2026-w47-it-zh-tw.text.md` | 52,568 B | `53c3ca77e2a365ed7aa4ec804db8cf9cc7029eb9fbb622f5bbff771e3dc438d3` |

兩 PDF 均為 8 頁、1462.5×2025 pt。探針 `git hash-object -w --stdin` rc=0（`probe.txt`）；TMPDIR 用 goals 側 scratch 下的 tmp。

**重要前提（已驗證）：** core-it 盤上已是 fix3（commit `36bdec2e`，2026-11-11 11:18 UTC）：P1 頭條改「Sabato 21 novembre torna la Serie A」、P2 25–28 選項 b/d 改句、P3 Torrazzo 改「torre medievale in mattoni più alto d'Italia」、P4 b/c 與 P8 F 選項縮短。本版建於 fix3 之前，因此以下 D1–D5 全部是**預期的舊版 core 缺陷在本版的殘留**，無一項是本版 fan-out 新引入的；修法全部已在 core 落地，**重 fan-out 即可重建本版**，復校員未動手修。

## 1. 門禁全套

| 門禁 | 結果 |
|---|---|
| occlusion audit（edition svg/，selftest 6 類 planted 缺陷全部觸發） | **0 flags**（`occlusion.log`） |
| p8 extract（本版 P8 SVG） | **150/150 noted**（`p8-extract-zh-tw.json`） |
| p8 extract（core P8 SVG） | 150/150 noted |
| p8 compare（core-it 對 it-zh-tw，顯式 --core-p8/--edition-p8） | **CLEAN**，keydiff 恰為 **[137, 138, 139]**（預期的翻譯題重定向鍵）；Q140 鍵為義大利語句、兩邊相同、無 diff，正確（`p8-compare.json`、`p8compare.log`） |
| freeze baseline（重跑當前 core 構建） | **8/8 字節一致**，core 完整性復核通過（8 文件重哈希未變）（`freeze-base.log`） |
| freeze diff（core-it/svg 對本版 svg） | rc=0（`freeze-diff.log`、`freeze-diff.json`、`freeze-fragments.txt` 586 行**逐條讀過**）；全部片段均可解釋，見 §2 |
| 印刷/網頁 text layer | **字節相同**（各 102,884 B），詞多重集相同（各 6,843 詞，0 單邊詞）（`print.txt`、`web.txt`） |
| P8 最小字號（SVG 實測） | 最小 13.0 SVG px = **9.75 pt**，符合 SOP §1.1 下限 |
| 練習編號 / 級別 | 138 單題 + 3 區間（25–28、52–55、141–144）= 150，無斷號；A2 47 / B1 70 / B2 33，與 KIT 一致 |
| 頭條長度 | `La Lazio resta in vetta: Inter e Roma inseguono` = 39 非空格字符 ≤ 上限 56 |
| VOL 計數（SVG） | VOL.4 ×9，VOL.5 ×3（均合法：P2 E TU 交叉引用、P7 LETTERE 披露、P7 下期預告） |
| ABSTRACT.txt（SOP §9） | 一行、繁體中文、無 ASCII 雙引號、含 **La Lucerna** 與 **VOL.4**，事實與本期一致（pt-zh-tw D4 類缺陷**不存在**） |
| 禁用詞 | Ucraina / Russia / Putin：0 命中 |
| CJK 掃描（.text.md） | 101× U+3000（家具分隔符，豁免）+ 全角冒號 62×（凍結的動詞範式注 16–20、60–61 及答案，core 模式）；唯一簡體疑似字符為「译」×4（見 O6） |
| 範文詞數 | 99 詞（實數），與 KIT 一致 |
| creambox 全版掃描（canonical `tools/creambox.py`） | 見 §4；盒內清除量最小 +3.9，9 條負值均為窗下誤報 |
| BOXTITLE 真墨跡 + 全版橫向真墨跡掃描（PIL，`sweep.py` / `sweep2.py`） | 見 §3；**盒題全部 fit，無 P1/P2/P7 盒題溢出**；全版僅 P2 b/d 超出版心 |

## 2. Freeze diff 逐條分類（對照的 core 已是 fix3，故差異含 fix3 增量）

586 行片段全部讀過，分類如下，**無未解釋片段**：

- **(i) 繁簡讀者層互換（預期 fan-out）**：全部 P1–P8 的簡體 → 繁體互換（如 `意大利语周报 LUCERNA ITALIAN WEEKLY` → `義大利語週報 正文義大利語 講解繁體中文`、`说说你自己` → `說說你自己`、`翻译成繁体中文` → `翻譯成繁體中文`），以及 P1 數字盒的整行繁體改寫（KIT §9 已登記：29/24/20.45/150 四行）。
- **(ii) fix3 前舊 core 文本（即本版 D1–D5 的來源）**：P1 added `Domenica 22 novembre torna la` / removed fix3 `Sabato 21 novembre torna la Serie A`；P2 added 舊 b/d 首行 / removed fix3 改句；P3 added `più alto d'Italia. La leggenda lo lega al` / removed `medievale in mattoni più alto d'Italia.`；P4 added 舊 b/c 長行 / removed fix3 短句；P8 added 舊 F 選項長行 / removed fix3 短句。
- **(iii) 同文重斷行**：其餘 added/removed 均為同一義大利語/繁體字串的不同斷行切分（如 P3 `sedici giorni, il torrone è dappertutto:`、P7 `essere，分詞配合性數`），無文本改動。
- **無 it-nl D5 類 fan-out 擅改**：義大利語目標文本除 (ii) 的 fix3 前舊版外無任何改動；P8 由 p8 compare + 150 鍵核對覆蓋，不另作片段分析。

## 3. 版式幾何——真墨跡量測（PIL，audit 字體解析；Noto Sans CJK TC）

### (a) P1/P2/P7 盒題：全部 fit，無溢出

19 個奶油盒標題逐一量過（`sweep.log` §a）：

| 盒題 | 墨跡右緣 | 盒右緣 | 餘量 |
|---|---|---|---|
| P1 `LA SETTIMANA IN CIFRE　數字看本週` | 960.0 | 961.0 | **+1.0 px（見 O1）** |
| P1 `IN QUESTO NUMERO　本期目錄` | 1822.8 | 1862.0 | +39.2 |
| P2 `LA FRASE PER RICORDARE　口訣` | 918.0 | 961.0 | +43.0 |
| P7 `ERRORI TIPICI　常見錯誤` | 1735.8 | 1862.0 | +126.2 |
| P7 `LA PAROLA　本週生詞` | 1699.8 | 1862.0 | +162.2 |
| 其餘 14 題（含 P1 `LA SETTIMANA`、`IN BREVE`、P2 `LO SAPEVI?`/`E TU?`、P3 `IL WEEKEND DOLCE`、P5 `I GIOVANI IN NUMERI`、P6 `LA STRADA DELLA MANOVRA`/`LEGGERE I NUMERI`、P7 `LETTERE DEI LETTORI`） | ≤1766.0 | 1862.0/961.0 | 均 ≥ +96 |

- P1 cifre 標題另做 200 dpi 渲染像素驗證（`crop-p1-cifre.png`）：實渲染墨跡最右 svg 959.3 px，盒緣 961.0，**fit，餘 1.7 px**；背景 cream→paper 轉折恰在盒緣處。it-nl D1–D3（+113/+137/+59 px）、it-pt D3（+159 px）、it-fr D1（+173 px）同類缺陷**本版不存在**——繁體標題短，無溢出。
- P1 副標題 `本週日程　Cosa succede, giorno per giorno` 墨跡 1461.5–1839.2，盒右緣/版心 1862，餘 22.8 px，200 dpi 裁圖（`crop-p1-subtitle.png`）目視盒內無恙；it-de D1 類缺陷**不存在**（繁體前綴比德語前綴窄）。

### (b) 全版橫向掃描：僅 P2 b/d 超出版心（D2）

- 全版唯一墨跡超出版心 1862 的節點就是 P2 b/d 兩行（見 D2）；其餘全部在界內。
- 近版心線（墨跡 1859–1862 之內）均為家具/圖注/頁腳/範文行，無超限：P1 讀頭版行 1861.9、P2 圖注 1860.2、P5 圖注 1862.0（恰在緣上）、P8 範文行 1861.5/1860.8、各頁頁腳 1861.8。
- PDF span 框另有 ≤1.9 pt 的框外延（P2 圖注 0.0、P2 副標 `Una festa, una giornata verde` +1.6、P5 圖注 +1.6、P8 範文行 +1.8/+1.9、P1 `2026` +0.2）：均為字框 side bearing，PIL 真墨跡在界內，見 O5。

### (c) P2 b/d（D2）、P4 b/c（D4）、P8 F a/b/c（D5）

數值見缺陷清單 §5。P2 b/d 另做 200 dpi 裁圖（`crop-p2-match.png`）目視證實：b 行末 `del 21`、d 行末 `si accende` 明顯探出其餘行之外、逼近頁邊。

### (d) 精煉溝槽掃描（單欄正文行、墨跡止於 28 px 溝槽內）

除 D4/D5 的匹配題行與 O2 的 P7 FRASI 譯行外，**無其他溝槽侵入**。P6 `LE MINIME DI ESEMPIO　練習用示例最低溫 (DATI INVENTATI PER L'ESERCIZIO)` 墨跡 ..1053.2：為雙盒上方通欄標題，跨溝槽處上下 18 px 內無物（盒頂 y=1594，標題基線 y=1576），與 it-de 同型，不列缺陷（O3）。

## 4. 版式幾何——目視與 creambox

- 8 頁印刷 PDF 100 dpi 全頁渲染逐頁目視（`pages/p1.png`–`p8.png`）：除 D2 的 P2 b/d 行外，無溢出、重疊、頁腳侵入、豆腐塊。P3/P5 中部結構性留白為 core 固有模式；P1 體育場照片注 `(Pagina 4)` 為指向體育版的交叉引用。
- canonical creambox 全版掃描（`creambox-all.log`，355 行已讀完）：盒內清除量最小 **+3.9 px**（P3 E TU、P5 E TU）；P7 工具盒最小 +4.5。9 條負「末基線」清除量均為 +45 px 窗口誤報——窗下行是下一節標題/表行/圖注，不是溢出（P1 `ADESSO TU` −37.0、`LA PAROLA DELLA SETTIMANA` −24.0、QUIZ 副標 −44.0；P3 `IL TORRAZZO E IL TORRONE` −37.0；P4 結果表行 −40.0/−40.0/−26.0；P6 `ESERCIZI` 標題 −42.0 ×2）。
- desc-clear −1.1…−2.1 px（9 盒，最大 −2.1 為 P3/P5 E TU）：計量 artifact——末行無下行字母（如 P3 E TU 末行 `更喜歡牛軋糖還是巧克力？寫兩句寄來。` 全為中文 + `。`），200 dpi 裁圖（`crop-p3-etu-bottom.png`、`crop-p5-etu-bottom.png`）目視確認末行完整在盒內、下方留白清晰。**不列為缺陷**（O4）。
- pdfscan span 重疊對（`pdfscan.log`）：全部為框 artifact——刊頭帶與 LIVELLO 行框重疊、同行粗體導語框重疊、換行括注框重疊；P8 `16./19./26.` 全角冒號 `：` 框重疊 1–2 px 為凍結動詞範式注的 span 切分所致；8 頁目視均無可見碰撞（O10）。

## 5. 缺陷清單（共 5 項，全部 core 級、全部已在 core fix3 修復，待重 fan-out）

### D1 — P1 頭條段：意甲第 12 輪回歸日寫錯「週日 22 日」，與 P4 自相矛盾（core 級，嚴重度：中）

- **位置**：P1 LA NOTIZIA 正文第 3 段，text.md 約第 31 行：`Domenica 22 novembre torna la Serie A con la 12ª giornata: la sera, a Bergamo, c'è Atalanta–Inter. Sabato 21 la Lazio capolista gioca in casa con il Lecce.`
- **證據**：公開來源一致——第 12 輪週六 11 月 21 日開踢（calciostyle：「Il campionato riprenderà sabato 21 novembre con la dodicesima giornata」；minuto91.it 賽程同）。本版內部自相矛盾：同版 GIORNO PER GIORNO SAB 21 寫「torna la Serie A」；P4 正文寫「La Serie A riparte sabato 21 novembre con la 12ª giornata」；P4 表下注「si gioca dal 21 al 23 novembre」。只有 P1 頭條段的「Domenica 22 novembre torna」是錯的（22 日週日晚上只是 Atalanta–Inter 一場）。
- **修法**：core fix3 已改（`Sabato 21 novembre torna la Serie A con la 12ª giornata: domenica sera, a Bergamo, c'è Atalanta–Inter`）；重 fan-out 本版即可。注意：Q5/Q9/Q51/Q115（Bergamo、週日晚上）鍵不受影響。

### D2 — P2 匹配題 b、d 首行墨跡越過頁面右版心（core 級，嚴重度：中）

- **位置**：P2 右欄匹配題 25–28 選項 b、d 的首行，SVG y=2162（b）、2271（d）。
- **證據**（三重獨立驗證一致，與 it-de D2 / it-nl D4 同值）：
  - PIL 真墨跡量（SVG 源，Newsreader 23 px）：b 行墨跡右緣 1875.0 px（超 13.0 px）、d 行 1877.8 px（超 15.8 px）。
  - PDF span 框（PyMuPDF，交付件實測）：b 行 x1=1408.2 pt（超 11.7 pt）、d 行 x1=1409.7 pt（超 13.2 pt）。
  - 200 dpi 渲染像素掃描（`crop-p2-match.png`）：b、d 首行末字明顯探出其餘行之外、逼近物理頁邊。
  - 全文為舊版措辭 `b. il ponte di barche per la festa del 21 / novembre` 與 `d. la piccola luce di cera che si accende / in chiesa`；僅首行溢出，續行在界內；同組 a、c 行在界內。
- **嚴重度**：中。文字完整可讀、無遮擋、無內容丟失，但兩行 visibly 伸出版心約 4 mm；屬 proofread-until-zero 的攔停項。
- **級別**：**core 級**。本版繼承 fix3 前 core 文本（freeze diff：added 舊 b/d 首行 / removed fix3 改句 `per la festa in`、`accesa in`）。
- **修法**：core fix3 已改句（b → `il ponte di barche per la festa in novembre`、d → `la piccola luce di cera accesa in chiesa`）；重 fan-out 全部 it 母語版。

### D3 — P3 Torrazzo「全義大利最高鐘樓」說法不成立（core 級，事實，嚴重度：輕微）

- **位置**：P3 邊欄 `IL TORRAZZO E IL TORRONE`；text.md 約第 317 行：`Il Torrazzo di Cremona è il campanile più alto d'Italia.`
- **證據**：it.wikipedia「Torri e campanili più alti d'Italia」排名：Mortegliano（UD）Duomo campanile 113.20 m 列第 1，Torrazzo 112.54 m 列第 2（`Campanile di Mortegliano` 條目：「è il primo campanile, precedendo in altezza il più noto Torrazzo di Cremona (112,54 metri)」）。Torrazzo 正確的最高頭銜是「全意最高中世紀/磚結構塔」（la torre medievale / in laterizi più alta d'Italia）。
- **級別**：**core 級**，繼承（freeze diff：added `più alto d'Italia.` / removed fix3 `medievale in mattoni più alto d'Italia.`）。
- **修法**：core fix3 已改；重 fan-out。

### D4 — P4 匹配題 b、c 首行伸入欄間空白（core 級，繼承，嚴重度：輕微）

- **位置**：P4 匹配題 52–55 選項 b、c 首行。
- **證據**：真墨跡 `b. che non ha mai perso, ancora senza` 墨 end 969.0（超第 2 欄右緣 961 達 +8.0 px）、`c. il gruppo di squadre che giocano tra` 墨 end 973.5（+12.5 px）。行尾落在 28 px 欄間空白內（第 3 欄起於 989），無碰撞，讀者不可見。另：P4 結果表行 `Cagliari – Frosinone 1–0`、`Torino – Lecce 1–1`、`Genoa – Milan 1–2` 同類伸入（it-de O1 同值）。
- **級別**：**core 級**，繼承（freeze diff：added 舊長行 / removed fix3 短句 `che non ha mai perso`、`il gruppo di squadre in un torneo`）。
- **修法**：core fix3 已縮短；重 fan-out。

### D5 — P8 F 節匹配題 a、b、c 首行伸入欄間空白（core 級，繼承，嚴重度：輕微）

- **位置**：P8 F 節（Q141–144）匹配題選項首行。
- **證據**：真墨跡 `a. la parte del sistema fiscale, un livello` 墨 end 1430.0（超第 3 欄右緣 1411.5 達 +18.5 px）、`b. i soldi che pagano una misura, la sua` 墨 end 1430.5（+19.0 px）、`c. la differenza tra spese ed entrate, in` 墨 end 1419.8（+8.2 px）。行尾落在欄間空白內（第 4 欄起於 1439.5），距下一欄文字最近 9.0 px，無碰撞，讀者不可見（P8 渲染目視確認）。
- **級別**：**core 級**，繼承（freeze diff：added 舊長行 / removed fix3 短句 `a. un livello di reddito del sistema`、`b. i soldi che pagano una misura`、`c. la differenza tra spese ed entrate`）。
- **修法**：core fix3 已縮短；重 fan-out。

## 6. 內容事實（5 組公開來源抽查，D1/D3 除外全部相符）

| 事實簇 | 核查結果（2026-11-11 公開來源） |
|---|---|
| Serie A 第 11 輪（11 月 6–8 日）10 場比分 + 積分榜 | **已核實**：10 場比分全對（Venezia–Udinese 2–1、Fiorentina–Juventus 2–2、Inter–Como 2–0、Napoli–Lazio 1–1、Roma–Sassuolo 3–0、Genoa–Milan 1–2、Monza–Atalanta 0–1、Cagliari–Frosinone 1–0、Torino–Lecce 1–1、Parma–Bologna 1–2）；24 球；Lazio 29 / Inter 28 / Roma 27 / Milan 第 4 名 24 / Como 23 / Udinese 墊底 5；Roma 最佳攻擊 31 球；Lazio 不敗；Gattuso 為 Lazio 主帥。第 12 輪週六 21 日重啟（Lazio–Lecce 週六、Atalanta–Inter 週日 22 日 20:45、Monza–Fiorentina 週一 23 日 20:45）——**據此 D1 成立** |
| Torrazzo 高度 | **已核實反例，見 D3**：Mortegliano 113.20 m 第一，Torrazzo 112.54 m 第二 |
| Festa del Torrone / Eurochocolate | **已核實**：Torrone 第 29 屆 11 月 7–22 日（16 天、3 週末），主題 «Il Confine»，Sforza–Visconti 婚禮重演；Eurochocolate 佩魯賈第 32 屆 11 月 13–22 日，主題 «Fate dolci»，嘉賓大區卡拉布里亞；Torrone d'Oro 授予 Davide Simonetta；1441 婚禮傳說已按傳說表述 |
| BookCity / Torino Film Festival | **已核實**：BookCity 米蘭第 15 屆 11 月 23–29 日，主題 «Il senno sulla Luna»（Ariosto），1,360 活動 / 2,487 人物 / 1,164 書 / 443 場地；開幕週一 23 日 20:00 Dal Verme 劇院（Colson Whitehead，兩屆普利策）；預展週日 22 日 16:00 Luigi Rovati 基金會（Edmund de Waal）。TFF 第 44 屆 11 月 24 日–12 月 2 日（9 天，官方章程）；Filmmaker Festival 米蘭 11 月 14–22 日，週日 22 日閉幕；Alba 白松露集市至 12 月 6 日 |
| Manovra 2027 | **已核實**：DPB 10 月 15 日送布魯塞爾；2027 增長 +0.8%、赤字 3.4%（含歐盟條款；無條款 2.8%）；部長會議 10 月 28 日批准法案，約 260 億（政府口徑；DPB 口徑 235 億——文中已註明 260 億為報紙重建數，可接受）；法案號 C. 3174-bis（11 月 4 日三條款被刪後重編號）；聽證會 11 月 9–12 日（義大利銀行、UPB、Giorgetti 部長週四 12 日）；修正案截止週二 17 日 18:00；終批截止 12 月 31 日；Irpef 第二檔 33% 由 5 萬延至 5.5 萬；約 50 億來自銀行/保險。P1/P2/P6 均有「PROPOSTA ≠ LEGGE」提示；P6 練習圖表已標註虛構數據 |
| （另核）Madonna della Salute / 植樹節 / Santa Cecilia / ATP Finals | 與 it-de/it-nl proof1 的核實一致，未發現新出入：Salute 11 月 21 日、1630 誓願、Longhena 聖殿 1631–1687 年；植樹節 11 月 21 日（1898 首屆、2013 立法）；Santa Cecilia 11 月 22 日音樂主保；Nitto ATP Finals 都靈 11 月 15–22 日，Sinner 膝傷缺席、Zverev 世界第一、Cobolli 首秀 |

## 7. 語言與鍵（全文逐句讀過，text.md 1317 行 + 8 頁渲染）

- 義大利語正文與繁體中文講解層逐句讀：拼寫/語法/術語/一致性無問題（除 O6/O7 兩處注記）。
- **150 題答案鍵全部語義核對**（不只比鍵值）：RISPOSTE 1–150 與 P8 印刷鍵逐項比對——**0 差異**（僅 #150 記法差異：P8 `✓` vs text.md `✓ 範文見本版 H 區（99 詞）`，同義）；正文行內鍵 138 題與 P8 鍵一致（其餘 12 題為匹配題組頭，另行人工核對）；匹配題逐項核對題幹語義：P2 25–28（salute→c、ponte votivo→b、candela→d、piantare→a）、P4 52–55（vetta→d、imbattuto→b、girone→c、debutto→a）、P8 F 141–144（manovra→d、deficit→c、copertura→b、scaglione→a）均正確。
- 抽查鍵：Q7 A、Q8 B（24 球）、Q9 C、Q21 B、Q22 A（1630）、Q29 B、Q30 C（32 屆）、Q32 A（`Fate dolci`，見 O7）、Q40 è arrivato、Q43 ha chiuso、Q51 B（週日晚上）、Q58 più bella、Q59 meglio、Q66 B（11 月 23 日）、Q80 Vero、Q81 Vero、Q82 Falso（書城 22 日開幕為錯）、Q85 B（13−11=2）、Q86 A（6+7=13）、Q87 B、Q92 B（+0.8%）、Q104 B（leggerò）、Q108 A（è finita）、Q112 B（torna）、Q120 B（11 月 24 日）、Q137–140 翻譯鍵（見下）、Q145–149（B/A/B/A/B）均核對無誤。
- Q137–140：**渲染的 P8 標籤為正確繁體**「翻譯成繁體中文」×3、「翻譯成義大利語」×1；鍵本身正確：137 聖母健康節人們走過還願橋。/ 138 週日晚上亞特蘭大對國米。/ 139 週六，拉齊奧在主場對萊切。/ 140 `Ogni cifra deve essere chiara.`（dovere = 必須）。見 O6（text.md 括注標籤事宜）。
- P7 FRASI DELLA SETTIMANA 8 條引文逐字核對原文及頁碼（P1 ×2、P2、P3、P4、P5、P6 ×2）無誤；Q150 範文逐詞數 = 99 詞。
- P7 ERRORI TIPICI 4 項正確；LETTERE 為標註的編輯示例 + 繁體說明（無真實來信，W46 模式）；VOL.5 預告欄在位。
- `.text.md` 與 PDF 文本層：逐頁詞比對——差異全部可解釋：md 含行內 `— key:` 注解（答案行內注，PDF 各頁無對應行，答案只在 P8）與 `[A2 · …]` 類型標籤（PDF 用繁體短標籤）；PDF 提取存在並詞（缺空格）與寬距刊頭拆字。全文人工通讀未發現任一內容句單邊缺失。

## 8. 觀察（非缺陷，無需修）

- **O1 盒題餘量僅 ~1 px**：P1 `LA SETTIMANA IN CIFRE　數字看本週` PIL 墨跡餘 1.0 px、實渲染餘 1.7 px——**通過，但極緊**；重 fan-out 後須重測此標題（fix3 未動此標題，但任何字體/字距變化都可能使其越線）。
- **O2 P7 FRASI 譯行伸入溝槽（無碰撞）**：`一百五十多名身著文藝復興服裝的演員。 (Pagina 3)` 墨 end 533.2，超第 1 欄右緣 510.5 達 +22.8 px；同行下一欄文字起於 x=989，無碰撞。
- **O3 P6 圖表標題跨溝槽（空白處）**：`LE MINIME DI ESEMPIO…` 墨 end 1053.2，越過 961 溝槽，但標題在雙盒上方空白處（盒頂 y=1594，標題基線 y=1576），與 it-de 同型，不列缺陷。
- **O4 desc-clear 負值**（見 §4）：計量 artifact，真墨跡均在盒內，不列缺陷。
- **O5 PDF span 框 ≤1.9 pt 外延**（見 §3b）：side bearing，非真墨跡，不列缺陷。
- **O6 text.md Q137–140 括注類型標籤為簡體「翻译」**：text.md 第 969 / 971 / 973 / 975 行 `[A2 · 翻译]` 等（共 4 處，字符為簡體「译」）；KIT §8 已披露為「deliberately kept（W46 precedent）」。**按任務 (d) 方向不計為缺陷**，僅此記錄：渲染的 P8 標籤是正確繁體「翻譯成繁體中文/義大利語」（§7 已驗）；任務所述「翻譯」與文件實際「翻译」字形有別（繁譯 vs 簡译），留請 parent 知悉。
- **O7 Q32 注引號風格不一致**：Q32 注（正文與 RISPOSTE）寫 `"Fate dolci"` 直引號，其餘注/標題一律用 «…»；KIT §10 已披露（與 nl/ko 同）。輕微，不攔停。
- **O8 passato prossimo + "domenica" 的時態歧義**（it-nl D13 同類）：Q40/Q43/Q105/Q106/Q108 所涉事件為週日 11 月 22 日，付印時在未來；但 P7 B1 盒明確把 passato prossimo 框定為「講述週末」，讀者在週末之後做題時可把 "domenica" 讀作過去。形式全部正確，僅作觀察。
- **O9 P1「GIORNO PER GIORNO」缺少週三 18 日條目**：條目只有 6 行（LUN 16、MAR 17、GIO 19、VEN 20、SAB 21、DOM 22），**MER 18 完全缺失**；其餘 6 條內容全部核實無誤。core fix3 已明確接受（「D12 accepted, no fabrication」），故僅記錄、不攔停。
- **O10 pdfscan 重疊對**（見 §4）：框 artifact，8 頁目視無可見碰撞。
- **O11 P3/P5 中部結構性留白**：core 固有模式（KIT 已註明），不列缺陷。

## Verdict

**(b) 有問題，須修後重校：D1–D5 共 5 項，全部 core 級。**

- D1（core 級，中）：P1 頭條段稱意甲第 12 輪「週日 22 日回歸」，實為週六 21 日，且與本版 P4 自相矛盾。
- D2（core 級，中）：P2 匹配題 b、d 首行超出版心右緣 +13.0/+15.8 px（PIL 真墨跡 + PDF span + 200 dpi 裁圖三重證實）。
- D3（core 級，輕微）：P3 Torrazzo「全義大利最高鐘樓」不成立（Mortegliano 113.20 m 第一）。
- D4（core 級，輕微）：P4 匹配題 b、c 首行伸入欄間空白 +8.0/+12.5 px。
- D5（core 級，輕微）：P8 F 節匹配題 a、b、c 首行伸入欄間空白 +18.5/+19.0/+8.2 px。
- **本版級（fan-out）缺陷：0 項。**盒題全部 fit（§3a）、P1 副標題 fit、150 鍵語義全對、門禁除上述 core 殘留外全綠。
- 全部 5 項的修法**已在 core fix3（36bdec2e）落地**；重 fan-out 全部 11 個 it 母語版後，本版須**重校**（重點重測：P1 頭條段、P2 b/d、P3 Torrazzo 句、P4/P8 匹配行、P1 cifre 標題 O1 的 ~1 px 餘量）。

---

**證據文件**（均在 `scratch-proof-it-zh-tw1/` 目錄內）：`sweep.log` / `sweep2.log`（真墨跡量測）、`crop-p2-match.png`（D2）、`crop-p1-cifre.png`（O1 像素驗證）、`crop-p1-subtitle.png`（P1 副標題 fit）、`crop-p3-etu-bottom.png` / `crop-p5-etu-bottom.png`（O4）、`pages/p1.png`–`p8.png`（8 頁渲染）、`freeze-fragments.txt`（586 行片段）、`p8-compare.json` / `p8-extract-zh-tw.json` / `p8-extract-core.json`。
