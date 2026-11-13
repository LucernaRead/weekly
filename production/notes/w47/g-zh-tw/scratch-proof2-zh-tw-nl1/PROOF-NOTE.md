# PROOF-NOTE — 2026-W47 zh-tw-nl (proof2, independent full re-check)

**結論：(a) 零缺陷，可定稿。** (2026-11-11, proof2, 全量重校，不依賴 proof1)

- 版：`production/2026-w47/2026-w47-zh-tw-nl/`（目標語 zh-tw 繁體中文 × 荷蘭語讀者，VOL.4，重擴散新版）
- 核心 zh-tw 已定稿（re-proof #3 结论 (a)）；本版為重擴散重建，核心全程未動。
- 只讀生產：未 commit、未 push、未改任何生產文件；收工重驗三 SHA + 8 個生產 SVG + 8 個核心 SVG 全部不變（見 §10）。

## 三 SHA（盤核與任務值逐字節一致）

| 文件 | 大小 | SHA-256 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-NL.pdf` | 20,939,172 B | `730e15c9e70631a990d021e16e11f80de018683219c3beba08c897abf90c8832` |
| 網 PDF `Lucerna-VOL4-NL-web.pdf` | 2,409,973 B | `1c8dc05ba68db691cd54569b3161f6310959578d952cbb062e34353a25c867c3` |
| text.md `2026-w47-zh-tw-nl.text.md` | 50,596 B | `a3662561fff3e167b98bc8b4006ead5fe2166b56bed8ebe5e7c67105bb6ac0a5` |

兩 PDF 均 8 頁，1462.5 × 2025 pt。核心基線（核對用）：印 PDF 19,420,552 B `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`；網 PDF 2,324,042 B `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240`；text.md 49,798 B `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`（收工重驗一致）。

## 1. 門禁匯總（全部獨立重跑）

| 門禁 | 結果 | log / 證據 |
|---|---|---|
| run.py（scratch 副本） | RC=0，TOTAL 150，0 警告（無 FLOW OVERFLOW / HEAD TOO WIDE） | `run-copy/run.log` |
| 重建 SVG vs 生產 | 8/8 逐字節一致 | `run-copy/run.log` |
| checks.py | PASS，RC=0；8 金句各 2×；SIMP_ONLY_HITS [] | `checks/checks.log` |
| p8 extract / compare | 150/150，CLEAN（missing=[] extra=[] uncertain=[] keydiff=[]） | `p8/extract-ed.json`, `p8/compare.json` |
| freeze baseline（核心） | RC=0，8/8 逐字節一致 | `freeze-base.log` |
| freeze diff --strict-cjk | RC=1，裁為工具局限（見 O5），非缺陷 | `freeze-diff/diff.log`, `freeze-diff/diff.json` |
| occlusion 幾何遮擋審計 | selftest 6 類全觸發；審計 RC=0，0 flags，0 NEW vs 核心 | `occl/` |
| 奶油盒 canonical scan | 36 盒，0 內部負餘量 | `cream/creambox.log` |
| boxtitle | 36 盒，0 超出，題右緣最小 1.5px（P2） | `boxtitle/boxtitle.json` |
| PIL 奶油盒 | STRADDLE 0，CREAM-COVER 0；頁底最小餘量 P5 4.4px（正值） | `cream/creambox-pil.log`, `cream/creambox.json` |
| 印/網文字層 | 全文逐字節一致（107,779 B 各）；逐頁 P1–P8 全一致 | `textlayer/` |
| P8 最小字號（PyMuPDF） | P8 最小 9.75pt = SOP §1.1 下限；他頁最小 11.62–12.75pt | 見 GATE-LOG |
| 重渲印 PDF（scratch） | RC=0，與交付逐字節相同（SHA `730e15c9…`） | `render/render.log` |
| §1.1 配色 | 全部 fill 均為 §1.1 配色；額外 fill 只在品牌 moth mark 內；無金/紅棕/近黑 fill | 見 GATE-LOG |
| KIT 交叉核對 | 全部宣稱值與實測一致，惟一處 KIT 內部陳舊數字（見 O7，非版缺陷） | §9 |

- 總量：A2 44 / B1 74 / B2 32；頁 P1 10、P2–P6 各 18、P7 12、P8 38；類型 單選 67、完成句子 54、配對 16、完形單選 12、寫作 1。
- P7 幾何：col3 止 1823.3，teaser 止 2577.3（footer rule 2596，餘 18.7px）；P8 鍵止 y≈2358 < 2560。
- P4 柱 [90.0, 450.0, 900.0] ∝ 10/50/100；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]，間距 (1371.5−188)/7 = 169.07/小時，14:00→188、17:00→695.21、18:30→948.82、19:00→1033.36、20:00→1202.43 全合。

## 2. 150 題手驗（登記 REG vs text.md vs P8 印出鍵，三源逐題）

- 方法：scratch 腳本 `keys/dump_reg2.py`，以 `reg_ex` 呼叫點追蹤（AST 文件順序 + 堆疊歸屬），把 REG（題號/頁/級別/類型/鍵/註）接上 ex() 題幹與 P8 印出鍵。17 項非 ex() 登記已全數交代：16 項配對子題（4 組 × a/b/c/d，content12:155、content34:59、content34:183、content56:64）+ #150 寫作（直接 `reg_ex`，content8:116）。
- REG↔P8：149/150 完全一致；唯一差異 #150 寫作題：REG 鍵 `(開放題，範文如下)`，P8 印 `✓`——按設計（核心亦印 ✓；keydiff=[] 證實）。
- REG↔text.md：150 題幹全數找到（空白正規化後）+ 8 金句全數找到。
- 全表：`keys/reg-table2.txt` / `keys/reg-table2.json`（舊 `reg-table.txt` 為 BFS 錯位的第一版，已廢棄，勿引）。
- 逐題抽驗（鍵皆對題幹/正文重算，非僅一致性）：
  - P1 #1–10：B/C/A/B，封王/大巨蛋/夜間/感謝祭/鹿魔/紅色全合。
  - P2 #11–28：1200+800=2000（B）；退款 800（A）；配對 小雪→a / 點收→b / 鑑賞期→c / 主燈秀→d。
  - P3 #29–46：17 天（C）；1.5h（B）；配對 入圍→a / 頒獎→b / 鋼雕→c / 默片→d。
  - P4 #47–64：5×10=50（B）；70+30=100（C）；配對 遊行→a / 感謝祭→b / 集點→c / 封王→d。
  - P5 #65–82：48 天（B）；6 天（A）；配對 市集→a / 亮燈禮→b / 爵士→c / 打卡→d。
  - P6 #83–100：5h（B）；1.5h（C）；最晚 = 鋼雕 20:00（A）。
  - P7 #101–112 全合；P8 #113–150 全合，含 #118 題幹「爵士音樂節11月24日由肯尼·基收尾」鍵 A 為真（早先 110dpi 誤讀「第二週」已對印 PDF 文字層糾正）；#139–143 D 組、#144–149 E 組。
  - #150 寫作範文：142 字（不計空格），在 120–180 要求內；P8 鍵註「(142 tekens)」經 AST 字面量求值驗證。
  - P8 級別徽章：38/38 題皆有（P8：A2 8、B1 20、B2 10）；F 寫作頭 `F　寫一寫　Schrijven` 帶 B2 徽章。

## 3. 日期 / 星期 / 算術（`date -d`，Asia/Taipei，全部逐項重算）

| 日期 | 星期（date -d） | 紙上寫法 | 驗算 |
|---|---|---|---|
| 2026-11-13 | Fri | 11月13日（五） | ✓ |
| 2026-11-15 | Sun | 11月15日（日） | ✓ |
| 2026-11-16 | Mon | 11月16日（一） | ✓ |
| 2026-11-17 | Tue | 11月17日（二） | ✓ |
| 2026-11-19 | Thu | 11月19日（四） | ✓ |
| 2026-11-21 | Sat | 11月21日（六） | ✓ |
| 2026-11-22 | Sun | 11月22日（日） | ✓ |
| 2026-11-24 | Tue | 11月24日（二） | ✓ |
| 2026-12-27 | Sun | 12月27日（日） | ✓ |
| 2027-01-03 | Sun | 2027年1月3日（日） | ✓ |
| 2026-12-04 | Fri | 12月4日（五） | ✓ |
| 2026-12-06 | Sun | 12月6日（日） | ✓ |
| 2026-10-23 | Fri | 10月23日（五） | ✓ |
| 2026-11-06 | Fri | 11月6日（五） | ✓ |
| 2026-10-01 | Thu | 10月1日（四） | ✓ |
| 2026-11-22 | Sun | 小雪（11月22日） | ✓（廿四節氣標準日） |

- 算術：耶誕城 11/13–12/27 含首尾 = 45 天 ✓；迪士尼 11/17–1/3 = 14+31+3 = 48 天 ✓；金馬影展 11/6–11/22 = 17 天 ✓；爵士週二 11/17–22 = 6 天 ✓；主燈秀 17:30–23:00 每 30 分鐘 = 12 場 ✓；1200+800=2000、2000−1200=800 ✓；5×10=50、7×10=70、距 100 差 30 ✓；17:00→18:30 = 1.5h、14:00→19:00 = 5h ✓。

## 4. 8 金句（逐字核對出處，各恰 2×）

1. 封王遊行從天母棒球場出發（P1）
2. 夜間遊行晚上7點，最後一場不要錯過（P1）
3. 小雪之後，天氣一天比一天冷（P2）
4. 主燈秀每半小時一次，每次5分鐘（P2）
5. 頒獎典禮晚上6點30分開始（P3）
6. 保險箱裡，裝的是高雄的勞動記憶（P3）
7. 穿上紅色衣服，一起上街為龍隊喝采（P4）
8. 迪士尼聖誕，從11月17日開始（P5）

checks.py 8×2 通過；text.md 全數核對；P7 頁碼引用（p.1×2、p.2×2、p.3×2、p.4、p.5）全正確；荷蘭語譯文通讀無誤。

## 5. 標題數（實測本版；「56」為幻數，三種定義皆不符）

- 定義 A（文章標題 `Flow.title`，32pt）：**14**。P1：封王遊行，本週日天母出發！/ 夜間遊行最終場，六福村見！；P2：小雪快到了，保暖先做好 / 雙11包裹到了，先點收再拆箱 / 新北耶誕城開城，燈亮到晚上11點；P3：金馬獎本週日頒獎，誰會得獎？/ 鋼雕藝術節：最後一週，快去看 / 電影小課：1902年的月球之旅；P4：本週日，封王遊行天母出發！/ 棒球詞卡 Honkbalwoorden；P5：香港迪士尼聖誕，11月17日開始 / 西九爵士音樂節，免費戶外舞台 / 寶可夢、耶誕市集，11月繼續玩；P6：11月22日，一天四件大事。
- 定義 B（+ 練習節頭 `Flow.head`，25）：**39**。
- 定義 C（+ 7 頁眉帶 + P1 展示標題 + P6 時間軸頭 + P7 金句頭 + P7 下期預告）：**50**。
- 「56」三種定義皆不符，不得用作待驗數。

## 6. 目視（交付印 PDF，8 頁逐頁，110 dpi 渲染 `visual/p-*.png`）

P1–P8 全部乾淨：無溢出、無重疊、無頁尾侵入、無截斷。P7 欄止於頁尾之上甚遠；P8 鍵止 y≈2358 < 2560。圖片與授權皆在：P2 雨（CorraleH CC0）、P3 Méliès 1902（公有領域）、P4 Bain News Service 棒球照（PD）、P5 舊維多利亞港（作者不詳 PD）、P7 舊書（CC0）、P8 鉛筆筆記（CC0 Unsplash）。

## 7. re-fanout 報告 §7 未決項——獨立實測裁決

### 7.1 英文源 key「next Sunday」未改——未漏入本版

- 版 SVG：0 處；印 PDF 文字層：0 處；核心 SVG：3 處（凍結英文 gloss，re-proof #3 (a) 認證）。
- 荷蘭層用「zondag 22 nov.」/「Deze zondag」。無英文家具殘留（THE BIG STORY / Staff report / TAIWAN AND HONG KONG：0 處）。
- 「下週日」：0 處；「本週日」：版 SVG 11 處；「finish line」：0 處。
- **結論：無缺陷。未改的 key 只活在核心 + en 版。**

### 7.2 雙語小文件標題 STRADDLE——無回歸

- 獨立 PIL 掃描：STRADDLE 0（舊版 0）、CREAM-COVER 0；occlusion 0 flags。
- 最緊標題 P2「耶誕城小檔　Christmasland-fiche」（盒 [1439.5, 1430.0, 1862.0, 1890.0]）：PIL 真墨右緣餘 1.5px；**交付 PDF 200 dpi 像素 verdict**：最右墨在圖像 x=3874，盒右緣經奶油→紙色階確認在 x=3879（240,238,229 → 251,250,246），間隙 5.6 圖像 px = 2.7 SVG px；裁圖 `crops/p2-title-crop.png` 顯示標題全在盒內。
- **結論：無缺陷，記觀察 O1。**

### 7.3 P6 18:30 / 19:00 標籤縫

- 標籤 頒獎典禮（墨 906.8–990.8）與 夜間遊行（991.4–1075.4）分別對中 dots 948.82 / 1033.36；PIL 盒間隙 0.6px；**交付 PDF 200 dpi 像素 verdict**：兩墨段間 5 圖像 px = 2.40 SVG px 背景（探針 `crops/pixel-probe-p6.py`）；裁圖 `crops/p6-labels-crop.png` 顯示分離。Occlusion TEXTX 0 flags。
- **結論：無缺陷，記觀察 O2。**

## 8. 事實核查（網上多源各驗，2026-11-11）

- **第 63 屆金馬獎**：11月22日（日），台北流行音樂中心；紅毯 17:00、典禮 18:30；主持 柯煒林（首度）；主題「再見江湖」；入圍 10月1日公布；《狂忘警探》11 項提名最多；**587 件報名**；影展 11月6–22日（goldenhorse.org.tw；zh/en 維基、feminine.com.my、popdaily、cava.tw、applealmond.com）。一簡體鏡像文誤寫柯震東，為少數孤例，紙上柯煒林正確。
- **味全龍**：4–2 勝中信兄弟，隊史第 6 冠；遊行 11月22日 14:00 天母棒球場 → 台北大巨蛋松菸大道；球迷祭 11月21–22日（21日草地音樂會+露營、22日球員互動/合照/簽名/棒球教室）；穿紅衣；U-Sport 11月1–30日、267 場館、5→10 點、滿 100 換悠遊卡儲值金（TSNA 2026-10-30，與紙上署名「TSNA … Oct 30-31」相符；台北市政府）。
- **六福村墓碑鎮 10 週年**：9/12–11/22；夜間遊行《墓碑鎮：鹿魔覺醒》19:00 週五–日（11月22日=週日為最終場）；5 米鹿魔 Wendigo；日間《異界狂想曲》每日 14:00、週二休演。
- **新北耶誕城**：11月13日（五）–12月27日（日），45 天；Kanahei 主題；主燈秀每 30 分鐘 17:30–23:00、每次 5 分鐘；德國市集 12月4–6日；4 大 + 7 衛星燈區。
- **高雄鋼雕藝術節 SUPER STAGE**：10月23日–11月22日；B3 蓬萊倉庫、哈瑪星、鹽埕；週一–四 10:00–18:00、週五/六/日及假日到 20:00；主題 SUPER SAFE（倉庫即保險箱）；85 歲 林洪玉秀《萬年吉祥花》金屬網花、鹽埕學裁縫。
- **西九爵士音樂節第 8 屆**：11月13–15、17–22、24 日（10 天）；Diana Krall 11月13日揭幕（戲曲中心）、Cory Wong × 盧之昊 11月15日、Stacey Kent 11月17日（自由空間）、Kenny G 11月24日壓軸（Wonderland 竹翠公園）。
- **香港迪士尼「A Disney Christmas」**：11月17日–2027年1月3日；魔雪奇緣世界首個冬季市集；11月19日起城堡前新日間聖誕演出；樹燈亮燈 + 飄雪 + 無人機；聖誕音樂會 11月21–22日 + 12月5–6日共 4 場、香港兒童合唱團；香港居民雙重暢玩限時優惠（任選兩天入園）。
- **寶可夢 30 週年又一城**：11月11日–2027年1月3日；巨型衝刺皮卡丘氣球、10 米精靈球燈光裝飾、官方快閃店（festivalwalk.com.hk、likemagazine.com.hk）。
- 小雪 2026-11-22（廿四節氣）；雙 11 七日鑑賞期為台灣通訊交易法定解除權；《月球之旅》Méliès 1902。

## 9. KIT 交叉核對（WEEKLY-KIT.md，2026-11-11）

以下宣稱值與本 proof2 實測逐一相符：總量 150（A2 44 / B1 74 / B2 32；頁 10/18/18/18/18/18/12/38；類型 67/54/16/12/1）；三 SHA 與大小；P7 col3 1823.3 / teaser 2577.3（本方 run.log 第 24–25 行一致，餘 18.7px）；P8 9.75pt；occlusion 0；p8 CLEAN（keydiff=[]、missing=[]）；freeze 8/8；奶油盒 36 盒 0 負餘量（P7 最小 +12.5）；boxtitle 最小 1.5px；STRADDLE 0（舊 0）；P6 標籤間隙 0.6px（PIL）；P8 徽章 38/38（A2 8 / B1 20 / B2 10，本方由 reg-table2 獨立數出一致）；核心基線三 SHA（印 19,420,552 B `5ec35fe2…`、網 2,324,042 B `1c0799ac…`、text.md 49,798 B `09e083e1…`）收工重驗一致。

惟一不一致（見 O7）：KIT「Proofread record — Web PDF」行寫網 PDF「2,393,503 bytes」——此為首建舊值；交付網 PDF 為 2,409,973 bytes，KIT「Measured totals」行已載正確值。屬 KIT 內部陳舊數字，非版缺陷，交 K6/K7 文件收尾處理（本任務規定 KIT 不碰）。

## 10. 收工重驗（生產未動）

- 三交付文件 SHA 逐字節等於任務值（§首表）；大小一致。
- 8 個生產 SVG hash-only 比對開工基線：全同（p1 `00d5a2c0…`、p2 `5759d814…`、p3 `ecc2fc51…`、p4 `709c9dde…`、p5 `cad12e73…`、p6 `4eb302d0…`、p7 `78b0e2c7…`、p8 `68cf3890…`）。
- 8 個核心 SVG hash-only 比對開工基線：全同（`cc70b39c…`、`55378c70…`、`1ef68658…`、`ec781f9c…`、`183e0bc4…`、`51dafd84…`、`839a8093…`、`8e65cb3f…`）。
- `git status`：版目錄為未追蹤（`?? production/2026-w47/2026-w47-zh-tw-nl/`，開工前即然）；本員未改生產任何文件。倉內 W43 修改為開工前已有的無關改動，未碰。

## 11. 觀察項（非缺陷，不計入結論）

- **O1**：P2 標題「耶誕城小檔　Christmasland-fiche」右緣餘 1.5px（PIL）/ 2.7px（渲染像素）——全刊最緊盒標題，墨嚴格在盒內，未越界。證據：`boxtitle/boxtitle.json`、`crops/p2-title-crop.png`、`crops/pixel-probe-p2.py`。
- **O2**：P6 時間軸標籤 頒獎典禮/夜間遊行間隙 0.6px（PIL 盒）/ 2.40 SVG px = 5 px @200dpi（渲染）——墨分離，無接觸。證據：`crops/p6-labels-crop.png`、`crops/pixel-probe-p6.py`。
- **O3**：P5 最緊奶油盒底餘 4.4px（盒 [1439.5, 649.6, 1862.0, 1119.6]），正值無溢出；P5 渲染目視乾淨。
- **O4**：入圍釋為「被選進最後的得獎名單」（#43/#105/#132）語義偏鬆（入圍 = 提名/入選決選），但三處內部一致且為凍結核心文本（freeze diff 無新增 CJK）——非擴散缺陷。
- **O5**：freeze diff --strict-cjk RC=1 為工具局限（唯一新增 CJK = 荷/蘭，共 18 字：P1 ×4 字 = 2 處，P2–P8 各 ×2 字 = 各 1 處，全在家具「荷蘭語講解」內；核心對應處為「英語講解」），非缺陷。證據：`freeze-diff/diff.json`。
- **O6**：P8 最小字號 9.75pt 為 SOP §1.1 下限（梯級第 4 步），非 11.25pt 目標值。
- **O7**：KIT「Proofread record — Web PDF」行載網 PDF 2,393,503 bytes，為首建舊值；交付為 2,409,973 bytes，KIT「Measured totals」已載正確值。KIT 內部陳舊數字，非版缺陷，交 K6/K7 收尾。

## 12. 局限與未獨立證實項（非缺陷）

- Stacey Kent 11月17日「在自由空間連開兩場」：日期、藝人、場地已核（JazzNode / HK Cheapo / WestK 排程）；「連開兩場」（兩場次）未在所查來源中獨立證實，亦無來源反駁。核心凍結文本，不列缺陷。
- 「下週日」以外的英文家具掃描：以 checks.py + 全文 grep 驗 0 殘留；未對全部荷蘭語句逐字回譯，荷蘭語譯文以通讀核對。

## 13. 文件索引（scratch）

工作區：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-nl1/`

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- `run-copy/`：run.py scratch 副本 + `run.log`（TOTAL 150、0 警告、SVG 8/8 一致）
- `checks/checks.log`；`p8/extract-ed.json`、`p8/compare.json`；`keys/reg-table2.txt`、`keys/reg-table2.json`、`keys/dump_reg2.py`
- `freeze-base.log`；`freeze-diff/diff.log`、`freeze-diff/diff.json`
- `occl/`（selftest + 審計 log）；`cream/creambox.log`、`cream/creambox-pil.log`、`cream/creambox.json`；`boxtitle/boxtitle.json`
- `textlayer/`（印/網全文 + 逐頁 pdftotext 檔）；`render/render.log`（重渲印 PDF 逐字節一致）
- `visual/p-*.png`（8 頁 110 dpi 渲染）；`crops/p2-title-crop.png`、`crops/p6-labels-crop.png`、`crops/pixel-probe-p2.py`、`crops/pixel-probe-p6.py`
- `prod-hashes-before.txt` / `prod-hashes-after.txt`（開工/收工生產 hash，含交付三 SHA）；`core-hashes-before.txt` / `core-hashes-after.txt`
