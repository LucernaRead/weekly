# ES × ZH-TW — WEEKLY KIT（西班牙語正文 × 繁體中文講解）

- **Status: PASS**（獨立校對零問題，2026-10-22；記錄見 §10；校對未作任何修改）
- 配對：西班牙語正文（冻结核心 VOL.1）× 繁體中文講解（台灣/香港用語原生撰寫）
- 週次：W43 · 2026-10-19 – 2026-10-25 · VOL.1
- 核心來源：`files/weekly-report-es-vol1/`（build: `hidden_files/weekly-report-es-build/`）
- 本版 build：`hidden_files/weekly-report-es-zh-tw-build/`；產出：`files/weekly-report-es-zh-tw/`
- 繁體列定位：zh-TW 讀者列第四格（EN/DE/FR 核心之后）；列家具定式以 EN×ZH-TW KIT §3 登記為準，目標名換西班牙語。

## 1. 開工 baseline 與改道

- 開工前置核查：`hidden_files/weekly-report-es-zh-tw-build/` 與 `files/weekly-report-es-zh-tw/` 均不存在、無施工痕跡、無相關進程 → 正常開工。
- 核心 build 整份復制為本版 build；OUT 改道以 expanduser 形式逐處改寫並打印驗證（5 個 content 模塊的 SVG 目錄 + render.py 的 BASE），副本內無 `weekly-report-es-vol1` 殘留引用。
- `tools/freeze.py baseline`（自核心 build 的中性復制）：**8/8 逐字節復現核心**后才動工。核心 SVG sha256 前綴：p1 41f0d53f · p2 42f8603d · p3 ba31dbb0 · p4 524ad07b · p5 bf2a0790 · p6 b99e70a0 · p7 26432db2 · p8 229b1b13。收尾復核：出貨核心目錄 8/8 哈希與開工 baseline 全等，核心未變。
- 構建紀律：一進程驅動（run.py 順序 content12→34→56→7→8）；不在核心 build 目錄內 import 任何模塊；變換不用 AST 字節偏移（README #17），用 token 級字面量替換（#18）：解碼 STRING token、值命中映射表才原位重編碼，計數斷言先行、全過才落盤。

## 2. 註冊表與印刷集

- 註冊表（自核心復制一進程轉儲）：**150 題 = A2 52 · B1 70 · B2 28**；逐版 10/18/18/18/18/18/12/38；注空缺 0。本版重轉儲逐項比對：等級/版面/題號全等，注空缺 0。
- **印刷集**：核心 P8 以 `p8.py extract` 實測 = **150/150 全印刷**（content8.py 對註冊表無條件全印，短橫式 `N. key — note`，寫作題 `N. ✓ note`）。故本版不設 PRINT_NOTES 白名單——同集由結構保證，`p8.py compare --target es` 實測 **CLEAN（150 = 150）** 為準。
- **鍵差異（僅 3 項，全登記）**：

| # | 類別 | 核心鍵 | 本版鍵 |
|---|------|--------|--------|
| 137 | 翻譯題（E 區，鍵為中文原句） | 周日我们多睡一个小时。 | 週日我們多睡一個小時。 |
| 138 | 翻譯題（E 區，鍵為中文原句） | 周一在九个自治区是假日。 | 週一在九個自治區是假日。 |
| 150 | 裝置項（寫作題範本標記） | （开放题，范文如下） | （開放題，範本如下） |

- 題幹改向（鍵不變、題面中文改向）：#139/#140 題幹即鍵的西班牙語句不變，其 P8 題面以中文出題（國家德比週日晚九點開踢。→ ___ / 每個圖表都必須標明來源。→ ___）——此二題的「鍵」是西班牙語答案句，與核心全等，不入鍵差異表；題幹中文在凍結差分中歸講解層。
- `p8.py compare` 另報 keydiff [12, 16, 57, 73, 75, 83, 95, 96, 101, 105]——**行級偽影，已逐項證偽**（README #13）：此 10 題註冊表鍵與核心逐字節全等（y media / duermo / muchísimos / salas / postre / A / para que / Aunque / Son / más importante），工具的鍵/注邊界解析因繁體注折行位置不同而漂移；#150 因 ✓ 寫作行不印鍵而不被工具標記，其鍵差異以註冊表比對為準（上表）。
- 注：150 注中 122 條改寫為繁體；28 條與核心全等——其中 19 條含漢字者逐條核為字形合法繁體或語言中立（如 `poner el 1–1 = 打入扳平球`、`volver a + 原形 = 再次…`、`eFootball 10 月 23 日起可穿新球衣`、`marcar 的 indefinido：marcó`），其餘 9 條為純西班牙語/數字注。注全譯繁體逐條核畢。
- 題型標籤本地化（不入鍵差異）：單選/完形單選/判斷/判斷對錯/句型轉換/改寫/詞彙配對/翻譯/寫作/填空/完成句子/造句（後三者字形兩岸同作）。

## 3. 家具（繁體列定式，逐項）

| 項 | 本版實作 |
|----|----------|
| 報頭 | La Lucerna（西班牙語冠詞形，同核心） |
| P1 名行（y=330） | 西 班 牙 語 週 報 · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1（核心同位同式，名換繁體） |
| **徽章（槽位裁定）** | 佔 **P1 y=372 核心西班牙語副標行槽位**（核心原行 `EL PERIÓDICO SEMANAL PARA APRENDER — …` 整行移除，與 EN/DE 繁體列及 ES×RU/ES×JA 先例同槽）：`西班牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本`，19.5pt sans **bold BRICK** (#a4553a)，anchor middle。此槽為本核心版式實測裁定並在此登記。 |
| 頁腳（每版） | `La Lucerna · 西班牙語週報 VOL.1 · 正文西班牙語 · 講解繁體中文`（bslib4 foot()，列定式） |
| 頁碼（每版） | `第 {n} 版 / 共 8 版`（核心原式即此，不變） |
| 帶標題 | VIDA · 生活 / CULTURA · 文化 / DEPORTE · 體育 / JUVENTUD · 青年 / A FONDO · 深讀 / LENGUA · 語言（右側副題繁體：換時與天氣 / 秋天的節日 / 國家德比之週 / 服裝 · 球衣 · 螢幕 / 走向 11 月 29 日大選 / 語言聚焦） |
| gloss 前綴 | `譯注｜`（bslib4 gloss() 前綴改字；P1 頭條 expl 行首同改 `譯注｜`——該行性質為譯注，與 gloss 統一） |
| P8 頭左 | `RESPUESTAS · 全部答案與簡析（第 1–8 版）`（列定式：目標語詞 + 全部答案與簡析（第 1–8 版）） |
| P8 頭右注 | `每題附一句中文簡析 · 帶 ✓ 的為範本題` |
| P8 分隔 | `— 第 {pg} 版 —`（核心 f-string `— PÁGINA {pg} —` 定點改式） |
| 引號式 | 讲解層 “” → 「」（列裁定）；逐版雜散引號計數：ASCII 引號兩版全 0；P1/P5/P7 彎引號 4/2/4 → 本版「」4/2/4，其餘版 0/0——與核心逐版全等（計數口徑）。 |
| 字體面 | svglib 四改切 TC 面（_sc_index→_tc_index、endswith("SC")→"TC"、_IDX 調用、預設族名 Noto Serif/Sans CJK SC→TC），與 EN/DE 繁體列同款；另文檔串一字 重阳→重陽。tables.json 口徑 TC=3。講解層全用 TC 面渲染，自校肉眼核無缺字/方框。 |
| 函數名 | bslib4 `bridge()` → `expl()`（定義 1 + 調用 20：content12×4 · content34×7 · content56×5 · content7×3 · content8×1）。 |

## 4. 凍結證明（雙軌）

- `freeze.py diff`：逐版增刪串數對稱（P1 +24/−24 · P2 +19/−19 · P3 +21/−21 · P4 +21/−21 · P5 +24/−24 · P6 +8/−8 · P7 +29/−29 · P8 +143/−143）；新增 CJK 字符總量 900，抽查全為繁體字形。
- **正文全等軌**：對增刪串剝除全部漢字與全角標點后比對殘餘（拉丁/數字）多重集，逐版差異全數歸因於登記家具：每版頁腳拉丁段變更（`LUCERNA SPANISH WEEKLY` 段隨列定式頁腳更換）；P1 核心副標行整行移除 = 徽章槽位（§3）；P1/P5/P7 引號式變更造成的串切分差；P8 頭行（`RESPUESTAS ·` 后段）與分隔行（PÁGINA→第/版，數字保留）。**無任何西班牙語正文串被刪改。**
- **講解新增歸因軌**：變換映射表 233 鍵 + IDENTICAL 聲明集逐項覆蓋核心全部 CJK 字面量（普查斷言：content12 98 · content34 114 · content56 117 · content7 56 · content8 94 · bslib4 5，出現次數逐項核合）；未映射者即報錯停工，實測零未歸因。
- 凍結內容在位核查：P5 正文 `desde el viernes 23` 本版在位（grep = 1），無 `jueves 23` 殘留——2026-10-21 全 ES 版修正未回退；真實進球總數 40（正文口徑，#57 注與 P4 正文均為 40）。

## 5. 機械門結果

- `freeze.py baseline`：8/8（開工）＋收尾核心哈希復核 8/8 未變。
- `p8.py compare --target es`：**CLEAN，150 = 150**（偽 keydiff 證偽見 §2）。
- `occlusion_audit.py`（自檢先行通過）：本版 2 旗 = 核心同旗 1 + NEW 1，逐旗裁定如下。
  - **P5 BOXTITLE**（`Murcia y Canarias.` 墨跡下緣 1037.5 > 盒邊 1036.8）：核心同旗同位，凍結正文元素，繼承不改。
  - **P1 LINEX（NEW）**：每周一詞 expl 末行 `連假被「劈成兩半」，見第 3 版。` 的 PIL getbbox 墨跡盒觸 y=1844 橫線帶 [1843.4, 1844.6]。**像素裁定 = graze 非缺陷**：渲染卡面實測，兩版該行固體墨跡同止於 1842 行；1843 行僅極淡抗鋸齒殘像素（閾值 200 下核心 7px / 本版 11px，閾值 160 下兩版皆 0）；線帶本行 1844–1845 兩版皆 0 墨。與 EN 核心已裁定先例（墨跡 ≤1842 vs 線 1843–1844、零交疊）同類。元素級復核：本版「後繪圖形壓字」= 0（核心同項為 1，即此行 0.7px getbbox 交疊）。
- 同行墨跡碰撞掃描（README #10，真墨跡盒、基線差 ≤1.2 逐對核）：核心 0 / 本版 **0**（含 P8 頭行左右同線對）。
- 圖表標籤元素級檢查（README #12）：P1 五大看點條、P6 雙圖條與值標籤逐元素核——後繪矩形壓字全版 = 0（上項），標籤無被覆蓋。
- **行首/行尾禁則掃描（中文禁則集，標點感知）= 0**。核心同掃描有 3 旗且與本版初稿同位同構（核心文字等長→折行同位）：P5 計劃盒注 `、陪家人）` 行首、P7 expl `；despertarse…` 行首、P7 expl 行尾 `（`。三處皆我講解層文字，已在原生改寫時以 ±1–2 字移開折行點修畢（見 §8），修后掃描 = 0，流終點與核心逐版全等（行數不變）。
- 折行后逐行墨跡寬復核：構建期 flow 終點 y 與核心逐版逐欄全等（如 P8-keys 終點 2382、P3-ex 2552），無 FLOW OVERFLOW / HEAD TOO WIDE 警告；TC 面字寬與 SC 同度量，幾何零漂移。

## 6. gloss 點數與 P7

- gloss 盒（`譯注｜` 起首）逐版計數：P2/P3/P4/P5 各 1，與核心 `译注｜` 逐版全等；P1 另有頭條 expl 行 1 條以 `譯注｜` 起首（核心同行為 `讲解｜`，性質同為譯注，§3 登記）。盒內詞條逐條保留、一項不少——變換普查對每條 gloss 串逐項映射斷言（§4），條數由構造全等。
- P7 短語：8 條西班牙語短語逐字繼承核心（凍結殘餘核對 §4 覆蓋 P7），出現次數與 (Página N) 頁標籤逐條 = 核心；其下繁體譯句原生撰寫（如 `西班牙分成兩半：一半放連假，另一半沒有。`）。
- 日曆對照（Europe/Madrid 口徑）：El Clásico 週日 Oct 25 21:00（2026-10-25 為週日）、F1 Austin 同時 21:00、冬令時 10 月 25 日凌晨 03:00→02:00、諸聖節 11 月 1 日週日、萬聖節 10 月 31 日週六——均凍結正文口徑，與真實 2026 日曆一致。

## 7. 殘留掃描

- **簡體專有字形掃描 = 0**：以變換映射源串與目標串的字符差集導出簡體專有字形集（170 字），掃描本版 8 張 SVG 全部文本 = **零命中**；掃描 operative code = 5 字（content7.py 一行核心遺留註釋），已將該註釋繁體化，復掃 = 0。凍結正文中的中文引用（如短語後注）均為字形兩岸同作或已在 IDENTICAL 集登記。
- 他列家具殘留 = 0：無 EN/DE/FR 目標名、無他列頁腳串（頁腳/徽章/P8 頭均本列 §3 式）。
- 禁用術語：operative code 與本 KIT 中 `bridge` / `paper` = 0（svglib 文檔串核心原字 `weekly-paper` 已改作 `weekly`，零輸出影響）；scratch 變換腳本含歷史命名，confined 於 scratch 並在此披露。

## 8. 自校缺陷與修復（建造者自校一輪，八頁卡面肉眼全核）

1. **禁則 3 旗（自校機械掃描發現，核心同位繼承）**：三處講解文字以原生改寫移開折行點——
   - P7 A2 expl：`報時只有「一點」用 es；…` → `報時僅「一點」用 es；…`（−1 字，`；` 回到行尾，次行以 despertarse 起首）。
   - P7 B2 expl：`…後用虛擬式（tenga/sea/llueva）。` → `…後用虛擬式：tenga、sea、llueva。`（括號式改冒號列舉，行尾 `（` 消除）。
   - P5 計劃盒第 5 項中文注：`（週日諸聖節：送花、陪家人）` → `（諸聖節：送花、陪家人）`（西語已明言 El domingo 1，刪冗餘「週日」−2 字，`、陪家人）` 不再行首）。
   修后禁則掃描 = 0；重建流終點逐版 = 核心，行數與幾何不變。
2. **P1 LINEX 旗**：像素裁定 graze 非缺陷（§5），不改文字。
3. 其餘自校所見皆為核心凍結形態（如 P5 BOXTITLE 核心同旗），按凍結紀律不動。

## 9. 實測針腳（交付版，渲染后實測）

- SVG ×8 + cards ×8：`files/weekly-report-es-zh-tw/{svg,cards}/`（p1-portada · p2-vida · p3-cultura · p4-deporte · p5-juventud · p6-afondo · p7-lengua · p8-ejercicios）
- 印刷 PDF：`La-Lucerna-VOL1.pdf` — **5,960,459 B · sha256 2bc920547fce94caae23ae54885770e5bcf761a7f210cce25e1fade5a55ba6e9 · 8 頁**（D5 重建，2026-11-13；見 §11 D5 記錄）
- 網頁 PDF：`La-Lucerna-VOL1-web.pdf` — **3,351,530 B（< 10 MB）· sha256 d427ea6d0a3d1f23a2ded40f5ceae47a348a7d071fb911be02a1dded73cf8a9e · 8 頁**（D5 重建，2026-11-13；見 §11 D5 記錄）
- 總量：150 題（A2 52 · B1 70 · B2 28），注 150/150 非空且全譯繁體（28 條字形合法同作/中立，§2）。
- 交付範圍：僅建造與自校；未入倉、未發 Discord。

## 10. 獨立校對記錄（2026-10-22，獨立校對員；零修改 PASS）

一輪完整獨立校對，**零問題、零修改**，建造者全部自報逐項獨立複證成立。要點：

- **freeze**：baseline 核心 8/8 逐字節復現；本版 build 改道複本同樣 8/8 逐字節復現交付 SVG（確定性成立）；收尾核心 8 SVG 哈希與開工一致（41f0d53f…229b1b13），核心未動。diff 逐頁對稱（P1 +24/−24 · P2 +19/−19 · P3 +21/−21 · P4 +21/−21 · P5 +25/−25 · P6 +8/−8 · P7 +30/−30 · P8 +143/−143；新增漢字 900）。殘餘分賬（剝漢字+全角標點）：差異僅頁腳列定式、P1 徽章槽（核心副標行移除）、P8 頭/分隔、P7 虛擬式列舉折行假象（tenga、sea、llueva 改寫）——西班牙語正文零刪改。
- **p8.py compare：CLEAN 150=150**（ES 家族短橫式、注全印無白名單）。工具另報 10 項 keydiff 按 README 第 13 條以雙份註冊表（核心/本版 build 各於改道複本單進程傾印）逐項證偽為抽取偽影；真鍵差恰 {137, 138, 150}＝註冊表鍵差，SVG 原文複證。註冊表 150=150、級別 A2 52·B1 70·B2 28、逐題 page/level 全等；注 122 改 + 28 同——28 條逐條裁定（19 條含漢字均字形中立、9 條純西語/數字），與建造者賬全合。**手工自正文重推導全部 150 鍵全對**（含 #150 範文逐詞點數 82；真實進球總數 40 於 P4 正文與 #57 雙處在位；P5 «desde el viernes 23» 在位、全冊 jueves 僅 P3 10 月 29 日周四語境）。
- **繁體原生性**：簡體專有字形掃描（2,421 字集，已經 zh-TW 核心語料交叉剔除同形/繁體誤收字）於 SVG 與 operative code 均 **0**；大陸式詞彙掃描 0；漢字存量：本版獨有 172 字全繁體形、核心獨有 169 字全簡體形。台式用語（比數/資訊/範本/球季/週末/螢幕…）逐處在位。
- **列定式**：徽章佔 P1 y=372 核心副標槽，19.5pt Noto Sans CJK TC 粗體 BRICK #a4553a 居中，與 EN×ZH-TW §3 及同槽先例一致，裁定合式；頁腳 ×8、頁碼 «第 N 版 / 共 8 版» ×8、P8 頭 «RESPUESTAS · 全部答案與簡析（第 1–8 版）»、分隔 «— 第 N 版 —» ×8、gloss 前綴 «譯注｜» 逐項自交付 SVG 提取複證。svglib 與核心版 diff 恰為登記四改（TC 面），wrap 邏輯未動。
- **禁則（標點感知口徑）**：本版 0 真違規。建造者三修（P7 A2 expl、P7 B2 expl、P5 計劃盒注）逐項在位複證。校對員更寬口徑掃描另得 1 旗：P5 «3. Por la noche: fiesta de Halloween（» 行尾開括號——該行與核心**逐字節同一、同坐標**，斷行點由凍結西語前綴+欄寬完全決定（注文全文落在次行），屬核心同位繼承、非本版缺陷（與 P5 BOXTITLE 核心同旗同類）；建造者 §5「核心 3 旗」係未計此逐字節同一行，屬計數口徑差異，特此更正記錄，頁面無缺陷。
- **遮擋審計**：自檢通過；本版 2 旗＝核心 2 旗 + 新 1 旗。新增 P1 LINEX 經**像素裁定為非缺陷**：兩版卡面實墨同止於第 1842 行，1843 行僅抗鋸齒殘留（閾值 200：核心 7px/本版 11px，與建造者賬全合；閾值 160：兩版皆 0），金線帶 1844–1845 行兩版零墨——與 EN 核心已裁定先例同類。P5 BOXTITLE 為核心同旗凍結西語元素（溢出 0.7 單位），繼承合法。同行墨跡碰撞 0/0；後繪矩形/圖像壓字（元素級、任意重疊）0/0；非文字圖形幾何多重集逐頁與核心全等；文本幾何序列 P2–P8 與核心逐項全等、P1 僅徽章行字號 19→19.5 一處差異（登記槽位）。
- **gloss 點數**：四盒逐條點數 P2/P3/P4/P5 各 5 條，兩版全等、詞條逐項不斷、折行位亦同；P1 頭條 expl 行 «譯注｜» 1 處＝核心同位。
- **P7**：八條金句逐字回溯 P1–P6 原文全驗真；(Página N) 標籤分佈 {1:1, 2:2, 3:2, 4:1, 5:1, 6:1} 與核心全等；非漢字串多重集僅差已登記的虛擬式 expl 改寫一行。
- **日曆**（Europe/Madrid 實測）：10-20 周二、10-24 周六、10-25 周日（德比 21:00 + 冬令時 03:00→02:00 + F1 Austin 同時）、10-29 周四、10-31 周六、11-01 周日、11-02 周一、11-29 周日、2027-03-28 周日（P2 冬令時終點）全對。
- **引號**：逐頁計數與核心全等，«» 各頁不變；“”→「」 僅 P1/P5/P7 共 5 處（登記裁定）；ASCII 引號 0=0——無第 18 條型洩漏。
- **卡面**：8 頁逐頁肉眼核，TC 面字形齊全無缺字/方框，無溢出。
- **針腳複核（實測全長）**：網頁 3,745,023 B · sha256 93e6e66b1701a975896a2d1c8d0dfd85ef2db502fdf0af0d703a1336ec378550；印刷 19,141,588 B · sha256 124953016f9a540675e321ed12da8a42c5f10631624a348a29818fcf45dfb517（均 8 頁、印刷版面 1462.5×2025pt）——與建造者自報逐字全合。
- 校對員勘誤（僅 KIT 計數文字，不涉頁面）：§4 逐頁增刪 P5 應為 +25/−25（建造者記 +24）、P7 應為 +30/−30（建造者記 +29）；以 freeze.py 實測為準。
- 結論：**PASS**。未入倉、未發 Discord（投遞暫停期，入倉由上級以 insert.py 辦理）。

## 11. D5 重建記錄（2026-11-13，W43/W45/W46 D5+§1.1 合併重修 Phase 1）

- **原因**：D5 缺陷——sans 層拉丁/西里爾字符落入 Noto Sans CJK 而非 Newsreader（拉丁讀者）/ Noto Sans（俄語讀者）。本版修前 census：D5 拉丁 338、西里爾 0、彎引號 CJK 0。
- **安裝**：`tools/mechanism-w47/apply_variant.py --svglib <版>/svglib.py --target es --reader zh-tw --week 2026-w43`（先 `--check` dry-run 通過）。`_D5_READER = "cjk"`。路由單元測試 `test_d5_routing.py` FAILURES: 0。fix2（U+201C/U+201D/U+2019 → serif）保留：本版彎引號 0 個。
- **基線**：重建前先證基線乾淨——`run.py` TOTAL 150、0 警告；`render.py` + `webpdf.py` 產出與已發版文本層逐字一致（字符多重集差 0）；重建 SVG 8/8 與已發版逐字節相同。基線實測（已發版配方）：印 PDF `129115ff97e879fa30b666e70e7e7cf3c1adf6a09914571b1723924c652fd108`（17,166,335 B）、網 PDF（render）`57675efd3af5547479cd39ed257ce7161b28fc27376942032d962feda589b02d`（3,340,861 B）。§9 舊值（19,141,588 / 3,745,023 B）為更舊配方，已過期，以上兩值為準。
- **二次修復（只動字號，文字零改動；實測 advance，patched svglib `text_w`，sans bold；欄寬 CW=422.5，盒標題內寬 404.5）**：
  1. `content12.py:125` P1 頭 `EL OTOÑO EMPIEZA DE VERDAD` 25→24（439.1→421.5）。
  2. `content7.py:16` P7 頭 `A2　DECIR LA HORA Y EL PRESENTE` 24→21（471.1→412.2；同時清除 P7 TEXTX 碰撞——該頭壓 `B1` 20.5×16.8px）。
  3. `content7.py:48` P7 頭 `B2　CREO QUE… / NO CREO QUE…` 24→23（428.8→411.0）。
  4. `content12.py:47` P1 盒 `LA SEMANA EN CIFRAS　數字看本週` tsize 23→21（427.0→389.8；22pt 仍 +3.9）。
  5. `content12.py:176` P2 盒 `LA FRASE PARA RECORDAR　口訣` tsize 23→22（410.2→392.4）。
  - P3 頭 `RECORDAR JUNTOS　一起紀念` 25pt 入欄，無需修。
- **P8**：行數 200→200，距頁腳線餘量 57.4px 不變；p8 compare CLEAN（keydiff [137, 138]）。
- **新交付物（D5 重建，2026-11-13）**：印 PDF `La-Lucerna-VOL1-es-zh-tw.pdf` sha256 `2bc920547fce94caae23ae54885770e5bcf761a7f210cce25e1fade5a55ba6e9`（5,960,459 B）；網 PDF（render）`La-Lucerna-VOL1-es-zh-tw-web.pdf` sha256 `d427ea6d0a3d1f23a2ded40f5ceae47a348a7d071fb911be02a1dded73cf8a9e`（3,351,530 B）；issues 網 PDF（`tools/webpdf.py`）`2026-w43-es-zh-tw.web.pdf` sha256 `172aa57c838bee09a75144e49956674dd823a44e226e61d754bd3ac05b37c08d`（1,506,359 B）——待 closer 換入 `issues/2026-w43/2026-w43-es-zh-tw/2026-w43-es-zh-tw.pdf` 並更新 pin（已發版 `50b1ccde913b73ca76a435edd056b84af004dc7026e81fd255335fa4342db72c`，1,885,857 B）。印 PDF 由 17.2MB 縮至 6.0MB：`pdffonts` 核查——基線與 D5 後均嵌 `NotoSansCJKsc`/`NotoSerifCJKsc` + Newsreader，全部 embedded/subset/unicode，無丟字體；縮小系拉丁文移出 CJK 字體後每頁 CJK 子集大幅縮小。文字內容不變（文字層 print=web 多重集差 0）。
- **text.md**：D5 不改文字內容；重建後重出因字體寬度變化斷行重排（21 REWRAP），交付件為已發版 `.text.md` 原樣沿用（BYTE-IDENTICAL）；驗收 `verify_textexp_es.py --edition` 判 ADOPT（0 UNEXPECTED；習題號 313/313 序列一致；8 頁 token 全同）。
- **D5 門禁（17 門，run 2，全綠 ALL-GREEN）**：run TOTAL 150、警告 0；head_check PASS 0 缺陷；d5 census 拉丁 0 / 西里爾 0 / 彎引號 CJK 0；render RC=0；webpdf RC=0（1,506,359 B <7MB）；occlusion 0（含自檢）；p8 extract 150/150；p8 compare CLEAN；freeze baseline 8/8；freeze diff vs base 新增 CJK 字符 TOTAL 1 個（U+3000，run 拆分）（U+3000，run 拆分）；spill 0；boxtitle 0；edge 0/0；creambox PASS 0 缺陷（ratios n=378，中位 1.040）；文字層 print=web 多重集差 0；census_quotes 0 defective；家族 gates.py N/A。日誌：`hidden_files/d5-redo/scratch-2026-w43-es/logs/2026-w43-es-zh-tw/`（`GATES-SUMMARY.txt` 為總表；run1 日誌歸檔於 `run1/` 子目錄）。D5 報告：`production/notes/2026-w43/g-es/scratch-d5-rebuild-es/D5-REPORT-2026-w43-es-zh-tw.md`。
