# GATE-LOG — 2026-W47 pt-zh-tw proof1（獨立復校機械門實跑記錄）

- 版：`production/2026-w47/2026-w47-pt-zh-tw/`（印 PDF SHA `ddc35d9b…bd173`，24,130,201 字節；網 PDF SHA `fff6b335…56cc12`，1,781,773 字節；text.md SHA `d3e70bf9…cc6b5`，36,865 字節——三者皆與任務一致）
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`）
- 全部命令的輸出存於本 scratch：`gates.log`、`occlusion.log`、`occlusion.json`、`p8-extract.log`、`p8-extract.json`、`p8-compare.log`、`p8-compare.json`、`freeze-base.log`、`freeze-diff.log`、`freeze-diff.json`、`creambox.log`、`creambox-core.log`、`occlusion-core.json`、`inkprobe.json`、`inkprobe.py`、`print.txt`、`web.txt`、`render/p1–p8.png`（200dpi）、`crop-P1-empoucas.png`、`crop-P3-schedule2.png`、`crop-P6-timeline.png`、`keycheck-150.json`
- TMPDIR 全程為 scratch 內 `tmp/`；探針：`git hash-object -w` 通過，goals 側可寫通過。

## 1. gates.py（構建者自檢門重跑）— 16/16 PASS

`venv/bin/python -u gates.py`，RC=0，`FAILURES: none`。16 項全 PASS（含 VOL.4/日期/副標題、頁腳+頁碼 8/8、無 VOL.3 殘留、P1 刊頭行寬、零同基線碰撞、零頁框墨線穿越、P6 圖表 GRAZE 0%、gloss 29 項、P7 短語 2×+頁碼+繁體、讀者園地 5/5、圖片+出處 5/5、P7 引文離預告框、P1 頭條 ≤56 字實測 41）。

## 2. occlusion 審計 — 0 flags（自檢通過）

`venv/bin/python tools/occlusion_audit.py svg --json occlusion.json`，RC=0。輸出：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`svg: 0 flags`，`flag_count: 0`。
core-pt 同跑亦 0 flags（`occlusion-core.json`）。注意：此門對奶油框內溢出為盲——D1–D3 均不在其檢出範圍內，須以 creambox + PIL + 像素掃描另行實測（見 §3–§5），不能因 occlusion 0 就放過。

## 3. 正典 creambox.py 全版掃描（+45px 窗口 + 逐行 clearance + P7 toolbox）

`venv/bin/python tools/creambox.py svg/*.svg` → `creambox.log`（368 行）。須裁決的負值/框外行：

| 框 | 框內末行基線餘量 | 框外行 | 裁決 |
|---|---|---|---|
| P1 數字框 y=786 | +45.0 | +37.0「AGORA VOCÊ 換你試試」 | 下一欄目標題，偽報 |
| P1 EM POUCAS PALAVRAS y=1874 | +9.6 | **+17.6「em Brasília. (Página 4)」** | **D1 真溢出**（本框 own text 續行） |
| P2 提示框 y=1618（4 並列格） | +31.5–+60.8 | +32.0「Atenção: …」 | 框下正文段，偽報 |
| P3 譯注框 y=200 | +47.7 | +37.0「UM DIA, DOIS SENTIDOS」 | 下一欄目標題，偽報 |
| P3 日程框 y=200 | +14.9 | **+15.6「16h30.」** | **D2 真溢出**（本框 own text 續行） |
| P6 時間線框 y=200 | +28.6 | **+0.8「Página do Participante.」** | **D3 真溢出**（本框 own text 續行） |
| P6 圖表框 y=1594（×2） | +40.0/+62.0 | +42.0「EXERCÍCIOS 第 6 版練習」/「答案見第 8 版…」 | 練習區標題/副標，偽報 |
| P7 工具箱（3 框） | 見下 | 無 | 通過 |

P7-TOOLBOX 匯總：`3 boxes, min inside clearance +4.5, min desc-clear -1.5`（基線口徑）。PIL 真墨跡口徑見 §4：三框末行墨底餘量分別為 ERROS COMUNS −24.7px、A PALAVRA −2.5px、CARTAS −7.6px，全部 clearance 為正；引文區末行基線 2292.17，距預告框頂 2404 約 107px。**P7 toolbox 實測通過**。

core-pt 對照（`creambox-core.log`）：P1 同框 +17.6、P3 同框 +15.6、P6 同框 +0.8——三處幾何與本版逐字相同，D1–D3 歸屬核心。

## 4. PIL 真墨跡實測（inkprobe.py，自寫測量腳本，字體取 tables.json 真實路徑）

字體：Newsreader Regular/SemiBold（tools/fonts）、Noto Sans/Serif CJK TTC index 3（TC 面）、UnifrakturMaguntia；錨點 `ls`（左基線），量墨 bbox（非 advance）。輸出 `inkprobe.json`（8 頁，2,010 runs）。

- **D1**：P1「em Brasília. (Página 4)」Newsreader 20pt，墨頂 2311.6（框底 2310.0 之下 1.6px），墨底超出框底 **+22.6px**。
- **D2**：P3「16h30.」Newsreader 21.5pt，墨頂 523.6（框底之內 1.4px），墨底超出框底 **+15.6px**。
- **D3**：P6「Página do Participante.」Newsreader 21pt，墨頂 825.8，墨底超出框底 **+5.8px**（g/p 降部）。
- **(b) 類未復現**：P2/P3/P4/P5 E VOCÊ 框末行中文墨底距框底 **−2.4/−2.5/−2.5/−2.5px**；P7 A PALAVRA 框 −2.5px；P5 數字框「2027.」−5.4px。creambox 的 desc-clear −1.5/−1.6 是拉丁 0.30em 預留對中日韓字形的高估，真墨跡全部 clearance 為正——但餘量僅約 2.5px，極緊，記錄在案。
- **(a) 類未復現**：全部奶油框標題墨右距框右 −16.5px 至 −548px，墨頂距框頂 +13 至 +25px；全版掃描：墨右超右邊界 1884 者 0、墨左超左邊界 66 者 0。唯一 FOOTER 標記是 8 頁頁腳自身（基線 2624，設計位置），非正文侵入。
- 其餘框內末行墨底餘量皆為負值（即 clearance 為正），最小者為上述 −2.4px 一組。

## 5. 200dpi 像素掃描（印 PDF 渲染，render/p1–p8.png）

方法：取奶油色 `#f0eee5` 底邊最後一行（±40px 內搜），統計其下 60px 內深色墨點行。

- **P1 EM POUCAS PALAVRAS**（框底 svg 2310.0）：奶油末行 px 4811；其下 56 行有墨（svg 2311.2–2337.6，最多 294 墨點/行）。裁圖 `crop-P1-empoucas.png` 目視：整行在白紙上。
- **P3 日程框**（框底 svg 525.0）：奶油末行 px 1093；其下 32 行有墨（svg 525.1–540.0，最多 30 墨點/行）。裁圖 `crop-P3-schedule2.png` 目視：`16h30.` 完整在白紙上。（首輪誤取同 y 的譯注框底 375.4，檢出的是其下欄目標題，已糾正重測。）
- **P6 時間線框**（框底 svg 840.0）：奶油末行 px 1749；其下 13 行有墨（svg 840.0–845.8，最多 89 墨點/行）。裁圖 `crop-P6-timeline.png` 目視：g/p 降部越過底邊。
- **P2 E VOCÊ 框**（框底 svg 880.0）：框下 30px 內零墨——像素級證實 (b) 類未復現。
- 全版目視：8 頁逐頁看過（render/v1–v8.png），除 D1–D3 外無溢出、重疊、壓頁腳、圖片出處缺失；P5「O PLANO DA ESPERA」第 1/2/4/5 項中文括注孤「）」獨佔一行（O2 觀察項，合法換行、無溢出）。

## 6. p8 compare（顯式 --core-p8/--edition-p8）

`p8.py compare --core-p8 ../core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150`，RC=0：`status: CLEAN, missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
裁決：137/138 是僅有的鍵差異，皆為翻譯題答案的讀者語譯文——137「11 月 20 日週五是全國假日。」（Sexta, 20 de novembro, é feriado nacional.）與 138「帕爾梅拉斯在十二碼大戰中 5 比 4 獲勝。」（O Palmeiras venceu nos pênaltis por 5 a 4.）逐字核對準確；P8 SVG 答案流同行亦有對照注「— 對照第 1 版頭條」/「— nos pênaltis = 在十二碼…」。接受，無缺陷。
`p8.py extract --p8 svg/p8-avaliacao.svg --total 150`：`noted set = 150 of 150`。

## 7. freeze / freeze_direct — 8/8

- `freeze.py baseline --build production/2026-w47/2026-w47-pt-zh-tw --core-svg …/svg`：**8/8 byte-identical**（`baseline: 8/8 SVGs byte-identical (repointed files: none)`），core 完整性自檢通過（8 個 shipped core SVG 未被寫入改變）。
- `freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg …/svg`：TOTAL added CJK 946（與 KIT run2 一致；run1 的 947 差 1 字是已修的「週六 16 日」多餘「日」）。分頁：p1 +20/−20，p2 +21/−21，p3 +13/−13，p4 +16/−16，p5 +22/−21，p6 +12/−12，p7 +35/−35，p8 +175/−180；每頁 U+3000 各 +1（家具分隔符，共 9）；p5/p8 的 1 串不平衡是同文換行拆分。
- freeze_direct：baseline 即 freeze_direct（工具自報 8/8，見上）。

## 8. keycheck — 150/150

逐題手驗見 `keycheck-150.json`（150 條，每條含答案鍵與核對依據）。題面+正文/圖表+P8 答案流三方核對；其中 Q131=A（core D2 修正已在）、Q125=A（第 36 輪周六 21 日，35 輪周三/四結束，date 核驗 21 日為周六）、Q83–86（16–30 日 15 天、10 工作日+5 周末/假日、10+5=15）皆經算術核驗。**150/150 pass，0 fail。**

## 9. boxtitle 逐個實測

見 §4：全部 31 個奶油框的首行（標題行）皆以 PIL 真墨跡量過——墨右距框右最緊 −16.5px（P2 SÁB 21 格「Palmeiras × Flamengo, às」），墨頂距框頂 +13 至 +25px，無一溢出。P1 刊頭/副標題亦在全版橫向掃描內（墨右超 1884 者 0）。

## 10. 印/網文字層比對

`pdftotext -layout` 兩版：print.txt 103,930 字節、web.txt 104,022 字節；詞多重集差 **0/0**（各 7,267 詞，按 KIT 口徑為 7,010 詞——計數口徑差，非內容差）。兩版文字層皆非空。網 PDF 1,781,773 字節 <7MB。

## 11. P8 最小字號實測（PyMuPDF 渲染 pt，不信 KIT 配置數）

印 PDF P8 全部 819 個 span：distinct 尺寸 10.125–34.5pt；答案區（top>1250pt）411 個 span，最小 **10.125pt**（406 個 span ≤10.5pt）；全頁最小亦 10.125pt。答案流末行基線 2548.7（底限 2560）。高於 SOP §1.1 下限 9.75pt。KIT 的 10.125pt 數字經實測證實。

## 12. 彎引號 U+201C/U+201D/U+2019 全版掃描

SVG 文本層：U+201C ×2、U+201D ×2（皆在 P8 E 節 139/140 題幹，為成對中文引號 “…”），U+2019 ×0，直引號 `"`/`'` ×0。text.md 同：LDQUO 2、RDQUO 2、RSQUO 0、直引號 0。葡語正文用 « »（U+00AB/BB）引號，正確；無錯用、無不成對。

## 13. 其他核實（外部事實來源）

- 日期星期：`TZ=America/Sao_Paulo date -d` 核驗 13 個日期——2026-11-07 六、08 日、15 日、16 一、17 二、18 三、19 四、20 五、21 六、22 日、23 一、27 五、12-06 日，與文中星期全部一致。
- 工作日數：11 月 16–30 日工作日為 16/17/18/19/23/24/25/26/27/30 共 10 天，周末 21/22/28/29 + 假日 20 日共 5 天，10+5=15，與 P6 圖表一致；第 10 個工作日 = 11 月 30 日，「27–30 日」窗口是文中明示的兩種計法分歧，非錯誤。
- 範文：text.md 模型文實數 **88 詞**（80–100 範圍內）。
- 內部標籤掃描：SVG 文本 + text.md 中 `W47`/`2026-w47`/`zh-tw`/`pt-zh`/`SOP`/`proofread`/`cover`/`TODO`/`XXX`/`Lorem`/`占位` 皆 0 命中；VOL.3 ×2（皆在 P7 讀者園地披露中，屬允許引用）、VOL.4 ×9、VOL.5 ×3；P1 刊頭「VOL. 4 · QUARTA EDIÇÃO」為間隔體，屬設計。
- 簡體字掃描：SVG 文本層簡體字 0（常用簡體對照集）；全文全形「。」49、「！」1（皆為繁體原生標點）。
- 混合括號掃描：`(`/`）`、`（`/`）` 混用 0。

## 14. 判為非缺陷的項

- (a) P1 框標題/副標題橫向溢出——未復現（§4）。
- (b) P3/P5 右欄奶油框末行降部漫出——未復現，真墨跡餘量 −2.4/−2.5px，像素零墨（§4–§5）；但餘量僅 ~2.5px，後續改版須留意。
- (c) P7 toolbox clearance——實測通過（§3–§4）。
- (d) E 節 type 標籤——「翻譯」×4 是正確繁體本地化：core-pt 為「翻译」×4，pt-en 為「Translation」×4，pt-zh-tw 為「翻譯」×4；text.md 省略逐題小標籤與 pt-en 導出行為一致，非缺漏。
- P1 quiz 區 y=2312 分隔線與 D1 續行墨頂相交——本輪 PIL 實測墨頂 2311.6（線在其下 0.4px，擦過字形頂部；KIT 另載 Pillow 10.2.0/13.0.0 下墨頂 2312.85/2313.1，約 1px 口徑差），屬 D1 的附帶現象，隨 D1 修復消失，不另立項；venv（Pillow 13）下 occlusion 0 flags，KIT 記載的 1-flag 記錄是系統 python（Pillow 10.2.0）四捨五入所致，已核實。
- P5 括注孤「）」（O2）、摘要收尾句式（O1）——見 PROOF-NOTE 未決事項，非缺陷。
- P3/P5 詞表引入處「欄 2 頂 + 欄 1 底標題」、P4「B AS PALAVRAS」欄底孤標題、P1 足球段第 3 行位置——皆為核心 flow 行為，與 KIT 記載一致，非缺陷。
- P4「B AS PALAVRAS」等欄目標題 orphan、P2 欄 2 頂續句「uma semana depois do feriado。」——核心分欄流，非缺陷。
