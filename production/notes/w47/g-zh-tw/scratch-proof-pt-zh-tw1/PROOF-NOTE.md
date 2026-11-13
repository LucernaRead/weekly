# PROOF-NOTE — 2026-W47 pt-zh-tw（葡萄牙語目標 · 繁體中文講解）· proof1 獨立復校（re-fanout 版）

- 校對員：獨立復校員（proof1，本輪）
- 日期：2026-11-11
- 版目錄：`production/2026-w47/2026-w47-pt-zh-tw/`
- 核心對照：`production/2026-w47/core-pt/`（fix2，commit `d2b0e182`）
- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-zh-tw1/`
- 注意：本 scratch 內 `round1-first-edition/` 子目錄是首輪版（SHA `ddc35d9b…`）的舊校對件，已歸檔、與本輪無關；本輪所有實測均針對下方 SHA 的 re-fanout 版重跑。

## §0 身份核對（磁碟為準）

| 文件 | 任務給定 SHA | 磁碟 SHA（本輪實測，開工 + 收尾兩次） | 字節 | 一致 |
|---|---|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | `42d7d4de…7d9b11` | `42d7d4de02fadf02f82007e7230cc84ed75fb6181a90c0d65702a257bb7d9b11` | 24,130,648 | ✓ |
| 網 PDF `A-Lucerna-VOL4-web.pdf` | `bf86bcc8…3b7512` | `bf86bcc80642b13d164c523cd683b1cd6f41578a67bd9f8664226ba8153b7512` | 1,820,203 | ✓ |
| text.md `2026-w47-pt-zh-tw.text.md` | `5cd5c727…49a2888` | `5cd5c7270e6a3dc0bfe2f5c0c644f782189bffff9df5be2d10d9e07fd49a2888` | 36,875 | ✓ |

三個 SHA 與任務及 `FANOUT-REPORT-pt.md` §1 行 48–50 完全一致，無不符。收尾再次 `sha256sum`，三值不變——校對過程未改動任何生產文件。

## 結論：(a) 零缺陷，可定稿

全部門禁本輪重跑全部通過；首輪 D1–D3（核心盒底漫出）與 D4（摘要缺刊名）均已消除並經三法（源碼 + PIL 真墨 + 交付 PDF 像素）獨立復測確認；150 題逐題手驗通過；P1–P8 全頁目視乾淨。**缺陷 0 項。** 僅 5 項觀察（O1–O5），均非缺陷、不阻定稿。

## 報告旗標逐項核對

### 旗標 1 — FANOUT-REPORT-pt.md 行 109：D5 gloss「冠軍頭銜」/「o título 冠軍頭銜」，4 行，+383.5/+45.7

- 表項是 **P4 譯注框（`p4-esporte.svg`，框 x=989 y=270.48 w=422.5 h=175.4，底邊 445.88）**內 D5 生詞譯注的第 4 行結構：全框共 4 行，第 2 行行尾 `o título`、第 3 行行首 `冠軍頭銜`，第 4 行僅一個 `。`。
- 盤上一致：`冠軍頭銜` 在 P4 SVG 出現 1 次（譯注框第 3 行）、在 text.md L215 出現 1 次（`*譯注｜… o título 冠軍頭銜 …*`）；核心 text.md 對應位置為簡體 `冠军头衔`（core-pt fix2 `content34.py:134` 改 `o título 冠军` → `o título 冠军头衔`），本版為正確繁體對譯。
- 數值復測（見 GATE-LOG §D5）：右餘量：PIL **+383.5**（與報告值逐字一致，size 21 TC 面）；交付 PDF 像素實測末行墨右 +398.2（`。` 在 SC 面渲染為小圓點，墨跡本身比 PIL 框窄，兩數皆為「遠在框內」的同一事實）。底餘量：交付 PDF 像素 **+47.0**；PIL TC 面 +47.7、SC 面 +46.2（精確 20.5pt 2× 測量）。報告值 +45.7 與三法實測相差 0.5–1.3px，屬字體面/取整口徑差，非溢出、非缺陷；本輪以交付像素 +47.0 為準。
- 無溢出：4 行末行墨底距框底約 47px，第 3 行（最長行）墨右距框右 +21.4px（像素實測）。

### 旗標 2 — 報告行 166：D5 核心 gloss 值「冠軍頭銜」；ABSTRACT.txt 缺 masthead 由構建驅動補寫

- 核心 gloss 值：core-pt text.md L215（簡體 `冠军头衔`）與本版 text.md L215（繁體 `冠軍頭銜`）逐字對應，SEG 最長匹配正確（`冠軍頭銜` 優先於 `冠軍`），本版無殘留的裸 `冠軍` 歧義寫法（全版 grep `冠軍` 僅命中 `冠軍頭銜` 1 處 + P4 正文 `o título` 葡語原文）。
- ABSTRACT.txt 補寫核對：全文 531 字節、211 字、單行（尾換行）、無 ASCII 雙引號，以「`A Lucerna 葡萄牙語週報 VOL.4：`」開頭——補寫正確、格式合規。與核心摘要逐句對照：除繁體轉換與台灣詞彙（巴西盃/格雷米歐/帕爾梅拉斯/佛朗明哥/馬內・加林查）外，事實、日期、數字（11 月 20 日星期五、12 月 6 日、11 月 21 日、A2–B2、150 道練習題）全部一致。**此為構建行為，非缺陷。** 首輪 D4（缺刊名）已消除。

### 旗標 3 — 報告行 75 門禁聲稱：全部重跑驗證（詳見 GATE-LOG）

| 聲稱 | 本輪實測 | 結果 |
|---|---|---|
| p8 extract 150/150、compare CLEAN | extract 150/150；compare CLEAN，keydiff `[137, 138]` | ✓ |
| freeze 8/8 | core baseline 8/8；本版 run.py 重建 8/8 字節一致 | ✓ |
| occlusion 0 | 本版 0 flags（自檢通過）；core 0 flags | ✓ |
| keycheck 149/150 | REG–P8–text.md 三方 149/150 完全一致，僅 Q150 設計內差異 | ✓ |
| 印/網文字層 byte-identical（103,995） | `pdftotext -layout` 印/網各 103,995 字節、逐字節一致；raw 文本各 44,666 字節、逐字節一致 | ✓ |
| P8 10.125pt | PyMuPDF 取 P8 最小字號 10.125pt（印/網分佈完全相同） | ✓ ≥9.75pt 下限 |

## 校對任務逐項結果

### ① run.py：rc=0，TOTAL 150，0 溢出，重建 SVG 8/8 字節一致

- scratch 副本（`scratch-proof-pt-zh-tw1/rebuild/`）內 `tools/venv/bin/python run.py`，輸出重定向至 scratch 內絕對路徑 `run-rebuild.log`；rc=0，TOTAL 150（A2 48 / B1 71 / B2 31；按頁 10/18/18/18/18/18/12/38），`FLOW OVERFLOW` / `HEAD TOO WIDE` 出現 0 次。
- 8 個重建 SVG 與生產 SVG SHA-256 逐字節一致：p1 `5c6328a0…`、p2 `db47a3bb…`、p3 `11323559…`、p4 `caccb1ab…`、p5 `cdaa6104…`、p6 `95d6e3ce…`、p7 `7bbbdb8a…`、p8 `799f1035…`（全值見 `run-rebuild.log` 與 GATE-LOG）。
- 版內 `gates.py` 16/16 PASS（`gates.log`，FAILURES: none）。

### ② freeze：baseline 8/8；diff 新增 CJK 948，0 簡體殘留

- `freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg`：**8/8 字節一致**（`freeze-base.log`），core 完整性自檢通過（8 個 shipped core SVG 前後哈希不變）。
- `freeze.py diff`：新增 CJK 合計 **948**（首輪 946，+2 = core fix2 的 D5 gloss `頭銜` 二字，p4 頁新增 69 vs 首輪 67，其餘 7 頁與首輪一致）。201 個相異新增字經 opencc `s2t` 逐字核對：**全部為已是繁體的字（s2t 恆等），非繁體字 0 個**；`U+3000` 出現 9 次。
- 全版 opencc `s2t` 簡體殘留掃描（SVG 全部文本行 + text.md + ABSTRACT.txt）：僅 8 行被改動，皆為 opencc 過度映射的**誤報**——`才`→`纔`（1 處）、`布`→`佈`（7 處）；`才`（刚才/才華）與 `布`（公布）本身即台灣標準繁體寫法，改成 `纔`/`佈`才是錯的。故**真簡體殘留 0**。ABSTRACT.txt 為 s2t 恆等（潔淨）。
- freeze-diff 非 CJK 殘差逐頁核對（`cjk-reg-check.log`）：全部可解釋——① 頁腳/副標為讀者語家具（core 英文 `LUCERNA PORTUGUESE WEEKLY` → 本版繁體 `正文葡萄牙語 講解繁體中文`；P1 副標 core 葡語標語 → 本版 `葡萄牙語正文 繁體中文講解 — 給繁體中文讀者的版本`）；② `EXERCÍCIOS 2` vs `EXERCÍCIOS2` 等為去 CJK 後的空白口徑差；③ P5 `（`/`）` vs `（）` 為括注換行拆分（即 O2）；④ P7 `「落在某日」` vs `“落在某日”` 為台灣引號本地化；⑤ P8 `・` vs `·` 為中圓點字形本地化。**葡語題干/正文 0 差異。**

### ③ occlusion：真實審計 0 flags；盒標題 PIL + 交付像素全量橫掃

- `occlusion_audit.py` 本版 **0 flags**（自檢 6 類全觸發、對照靜默）、core **0 flags**（`occlusion.json` / `occlusion-core.json`）。
- PIL 真墨全量橫掃（`inkprobe.py`，1950×2700 全版）：全部 31 個奶油框標題墨右距框右均為負，最近者 −16.5px（P2 日程框首行 `Palmeiras × Flamengo, às`）；重點部位：P1 數字盒標題 `A SEMANA EM NÚMEROS　數字` −60.5、P2 標題 `PARA NÃO ERRAR　口訣` −140.5 / `VOCÊ SABIA?` −250.5 / `E VOCÊ?　說說你自己` −160.5、P7 標題 `ERROS COMUNS　常見錯誤` −102.5 / `A PALAVRA　本週生詞` −164.5 / `CARTAS DOS LEITORES` −143.5；全域 RIGHT/LEFT 溢出 0（僅基線 y=2624 的頁腳本身觸及 inkprobe 的簡化 >2596 線，屬設計值，occlusion 工具豁免）。
- 交付 PDF 像素全頁橫掃（200dpi，`pixel-sweep.log`）：8 頁墨跡 x 範圍均為 svg [88.3, 1861.4]（版框 88–1862 內）；y>2596 的墨僅頁腳行 2610.24–2624.64，無任何越框/漫出墨跡。

### ④ p8 extract 150/150，compare CLEAN（keydiff [137, 138]）

- `p8.py extract`：noted set = 150 of 150（`p8-extract.json`）。
- `p8.py compare`（core vs 本版）：**CLEAN**，missing=[]、extra=0、keydiff=[137, 138]（`p8-compare.json`）。137/138 為讀者語譯文鍵，逐字核對準確：137「11 月 20 日週五是全國假日。」← `Sexta, 20 de novembro, é feriado nacional.`；138「帕爾梅拉斯在十二碼大戰中 5 比 4 獲勝。」← `O Palmeiras venceu nos pênaltis por 5 a 4.`。

### ⑤ 印/網文字層逐 token 一致

- `pdftotext` raw：印/網各 44,666 字節，`cmp` 逐字節一致；`pdftotext -layout`：各 103,995 字節，`cmp` 逐字節一致（`print.txt` / `web.txt` / `print-layout.txt` / `web-layout.txt`）。網 PDF 不可復現字節是已知特性，只比文字層——一致。

### ⑥ P8 最小字號 10.125pt ≥ 9.75pt 下限

- PyMuPDF 取印 PDF P8 全部 span：最小 10.125pt（599 個 span），其餘 10.5–34.5pt；網 PDF P8 字號分佈與印版完全相同。SOP §1.1 下限為 9.75pt（非 10pt），本版高於下限 0.375pt。

### ⑦ 150 題逐題手驗：題干 vs 核心 0 差異，鍵 vs 鍵 0 差異（除設計內 137/138/150）

- text.md 全文 534 行逐行讀過；登記表（REG）本輪重建轉儲（`reg-edition.json`，150 條）與核心登記表（`reg-core.json`）逐字段比對：**鍵差異僅 3 題**——137、138（繁體譯文鍵）與 150（開放題標記 `（开放题，范文如下）` → `（開放題，範文如下）`）；其餘 147 鍵逐字節相同。210 個字段差異全部是簡→繁字形轉換或台灣詞彙本地化（`現在時→現在式`、`過去時→過去式`、`將來時→未來式`、`公交→公車`、`培训机构→補習班`、`点球→十二碼`、`弗拉门戈→佛朗明哥`、`格雷米奥→格雷米歐` 等 72 處詞彙差異逐條核對，**0 語義改變**；詳見 `cjk-reg-check.log`）。
- 三方比對（`key-triple-check.log`）：REG 鍵 vs text.md Respostas 鍵 vs P8 印出鍵——149/150 三方完全一致，僅 Q150 為設計內差異（REG 標記 / text.md `✓ 範文見本版 H 區（88 詞）` / P8 印 `✓`，皆指同一開放題；範文實數 88 詞，符合 80–100）。
- 鍵–題干契合逐題手驗：見 `keycheck-150.json`（150 項，全部 pass，每項附核對依據）。抽檢要點：Q58 `mais cedo`（16:30 早於 17:00）✓；Q83–86 算術 16–30 日共 15 天、工作日 10 天（16/17/18/19/23/24/25/26/27/30，20 日假日不計）、週末+假日 5 天（21/22/28/29+20 日）、10+5=15 ✓；Q125 第 36 輪週六 21 日（35 輪週三/四結束，`date` 核驗 21 日為週六）✓；Q120 13:30–18:30 = 5 小時 ✓；Q65/90 15 日考 Natureza e Matemática ✓。
- P7 本週金句 8 句逐字核對皆出自本期文章（P1/P2/P3/P4/P5/P6 各有出處，頁碼標註正確）；gates.py 金句檢查 8 句 ×2 次出現亦通過。

### ⑧ 全頁目視（P1–P8）

- 交付印 PDF 110dpi 全頁 + 200dpi 重點裁圖逐頁看過（`render/pg1–pg8`、`crop-P1-D1/P3-D2/P6-D3/P4-gloss`）。未見溢出、重疊、壓頁腳、圖片缺失、豆腐塊。P2/P3/P4/P6 中部的留白與 core 幾何相同，為版式固有結構。P5 `O PLANO DA ESPERA` 第 1/5 項孤 `）` 見 O2。

### ⑨ 核心 D1–D3 框溢出：已由 core-pt fix2 盒高修正消除——獨立復測確認

| 缺陷（首輪值） | 修正（源碼行） | 本輪 PIL 真墨復測 | 本輪交付 PDF 像素復測 | 目視裁圖 |
|---|---|---|---|---|
| D1 P1 `EM POUCAS PALAVRAS` 末行 +22.6px（舊框底 2310.0） | `content12.py:129` 框 436→474（+38），底邊 2310→2348；`content12.py:150` quiz 分隔線 2312→2350（同 +38） | 末行 `em Brasília. (Página 4)` 墨底 −15.4px（框內）；框下 45px 窗內僅 quiz 標題 | 奶油底邊 px=2347.68；框底至 2409 間無文字墨，僅 y=2350 分隔線（全幅 3696px） | `crop-P1-D1.png`：末行完整在框內，分隔線在框下 2px 處，未擦字 |
| D2 P3 日程框末行 +15.6px（舊框底 525.0） | `content34.py:40` 框高公式 +26，底邊 525→551 | 末行 `16h30.` 墨底 −10.35px（框內） | 551–596 間零墨；首墨為下框標題頂 596.2 | `crop-P3-D2.png`：`16h30.` 完整在框內，下有淨空 |
| D3 P6 時間線框末行 +5.8px（舊框底 840.0） | `content56.py:132` 框 640→654（+14），底邊 840→854 | 末行 `Página do Participante.` 墨底 −8.2px（框內） | 854–884 間零墨；首墨為下框標題頂 884.2 | `crop-P6-D3.png`：`Página do Participante.` 降部完整在框內 |

- 三處幾何與 core-pt 逐字節相同（core inkprobe 數值一致：−15.4 / −10.35 / −8.2），歸屬為**核心層修正的傳遞結果**，非本版自有修復；修正方法是加高盒體（未改文字），符合首輪修復建議。另：P1 quiz 分隔線隨盒同移 38px，現位於框底下 2px（y=2350）、quiz 標題基線 2386 之上，線與末行墨（墨底 2332.6）相距 17.4px——首輪「線擦過字形頂部」的附帶問題隨之消失。
- 仍偏緊但框內的餘量（與首輪相同，非新問題）：P2/P3/P4 `E VOCÊ?` 框末行 −2.42/−2.48px、P5 `E VOCÊ?` −2.51px、P7 工具箱 −2.48px——皆在框內，無漫出。

### ⑩ ABSTRACT.txt 完整核對

- 全文 531 字節 / 211 字 / 單行（尾換行）/ 無 ASCII 雙引號；含刊名（`A Lucerna 葡萄牙語週報 VOL.4`）、目標語名（葡萄牙語）、A2–B2、150 道練習題，符合 SOP §9。
- 與核心摘要逐句對照無事實出入（見旗標 2）；與正文一致：黑人意識日、祖比與帕爾馬雷斯、巴西盃決賽（12 月 6 日馬內・加林查）、Enem 第二天與官方答案、11 月 21 日巴甲爭冠戰皆見於正文。
- 註：W47 全家（含 core-pt 與 pt-en）的 `.text.md` 均無「正文摘要節」（grep abstract/摘要/Resumo/Summary 皆 0 命中），為本週管線的跨版既定形態，非本版獨有——列為 O4，不阻定稿。

## 觀察項（非缺陷，不修版）

- **O1**：摘要收尾「適合學葡萄牙語的讀者透過巴西新聞學葡萄牙語」——字面近禁寫的「以新聞學」類表述，但與核心摘要及 pt-en/de/es/fr 各版寫法完全一致，是跨版既定寫法；是否更動屬跨版決定，不在本版 proof 內裁決。
- **O2**：P5「O PLANO DA ESPERA」框第 1/5 項中文括注換行後孤「）」獨佔一行（首輪已存在，核心繼承的合法換行；框內末行墨底餘量 −44.6px，無溢出）。
- **O3（D5 字體問題，只記錄、不修）**：本版全部中日韓文字的字體聲明皆為 SC 面——`Noto Sans CJK SC` 614 處、`Noto Serif CJK SC` 328 處，TC 面 0 處（`svglib.py:52–53` 硬編碼 SC，fanout 繼承核心寫法）。實測影響：`。`在 SC 面與 TC 面的墨跡相差約 6px（PIL：SC 面墨頂 393.2 / TC 面 387.2 @20.5pt），D5 gloss 底餘量因此在 +46.2（SC）與 +47.7（TC）之間浮動——兩者皆在框內、無缺陷，但字體面選擇是可測量的渲染差異。是否改 TC 面待用戶定範圍，本輪不修。
- **O4**：`.text.md` 無正文摘要節（見 ⑩ 註），W47 全家一致，跨版問題。
- **O5**：報告行 109 的底餘量 +45.7 與本輪三法實測（交付像素 +47.0、PIL TC +47.7、PIL SC +46.2）相差 0.5–1.3px——字體面/取整口徑差，非缺陷；本輪以交付像素值為準。

## 核實摘要（本輪實測，非 KIT 轉述）

- 全文通讀：印 PDF 8 頁逐頁看圖（110dpi 全頁 + 200dpi 重點裁圖）+ text.md 全文 534 行逐行讀過；葡語拼寫/變位/標點、繁體中文講解層對照正文、15 個日期用 `date` 核驗全對（7 日週六、8 日週日、15 日週日、16 日週一、17 日週二、18 日週三、19 日週四、20 日週五、21 日週六、22 日週日、23 日週一、27 日週五、30 日週一、12 月 6 日週日、2027 年 1 月 1 日週五）、事實一致性（比分、輪次、工作日數 10+5=15、Enem 時間 13:30–18:30/90 題 5 小時）均無問題。
- 150 題答案鍵：逐題手驗 150/150 通過，見 `keycheck-150.json`（鍵取自登記表程序化提取，與 P8 印出鍵、text.md Respostas 三方比對）。p8 compare CLEAN，keydiff 僅 [137, 138]。
- 機械門：run.py rc=0 TOTAL 150、0 溢出、重建 8/8；gates 16/16；occlusion 0 flags（自檢通過）；freeze baseline 8/8、diff 新增 CJK 948（0 非繁體）；p8 extract 150/150；印/網文字層逐字節一致（layout 103,995 / raw 44,666）；P8 最小實測字號 10.125pt（高於 SOP §1.1 下限 9.75pt）；簡體真殘留 0；內部標籤掃描乾淨（freeze-diff 非 CJK 殘差皆為讀者語家具/空白口徑/換行拆分/引號與中圓點本地化）。
- D1–D3：**全部消除**，三法一致確認（見 ⑨ 表）。

## 源文件狀態

源文件未改動、未重建、未 commit、未 push。全部重建/重渲染均在 scratch 副本或 scratch 渲染目錄內完成，生產目錄（`production/2026-w47/2026-w47-pt-zh-tw/`，含 SVG 與兩份 PDF）SHA 在開工與收尾兩次核對中不變；freeze baseline 的 core 完整性自檢亦通過（8 個 shipped core SVG 未變）。工作樹中其他家族的改動與本輪無關、未觸碰。
