# GATE-LOG — 2026-W47 pt-zh-tw proof1（re-fanout 版）· 全部門禁逐項實測值

- 版：`production/2026-w47/2026-w47-pt-zh-tw/`，核心對照 `production/2026-w47/core-pt/`（fix2 `d2b0e182`）
- 解釋器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，freeze 實測打印）
- 全部輸出只寫 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-zh-tw1/`
- 身份：印 PDF SHA `42d7d4de02fadf02f82007e7230cc84ed75fb6181a90c0d65702a257bb7d9b11` / 24,130,648 B；
  網 PDF SHA `bf86bcc80642b13d164c523cd683b1cd6f41578a67bd9f8664226ba8153b7512` / 1,820,203 B；
  text.md SHA `5cd5c7270e6a3dc0bfe2f5c0c644f782189bffff9df5be2d10d9e07fd49a2888` / 36,875 B（開工與收尾兩次核對一致）

## G1 · run.py 重建（本版自身 8/8）

- 命令：`cd scratch-proof-pt-zh-tw1/rebuild && tools/venv/bin/python run.py > <scratch>/run-rebuild.log 2>&1`
  （rebuild 為版目錄的 scratch 副本；輸出重定向用絕對路徑；生產 SVG 未觸碰）
- rc=0；TOTAL **150**（A2 48 / B1 71 / B2 31；按頁 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38）；
  `FLOW OVERFLOW` / `HEAD TOO WIDE` 出現 **0** 次；`ALL DONE`。
- 重建 SVG 與生產 SVG SHA-256 逐字節一致 **8/8**：
  `p1-capa.svg 5c6328a0808f798d…`、`p2-vida.svg db47a3bb9633fbfb…`、`p3-cultura.svg 11323559ec80e61e…`、
  `p4-esporte.svg caccb1abc0479128…`、`p5-jovens.svg cdaa61045c73b2d0…`、`p6-aprofundamento.svg 95d6e3ce796d1a7d…`、
  `p7-lingua.svg 7bbbdb8a7e0ff70c…`、`p8-avaliacao.svg 799f10358a524cc2…`（全值見 `run-rebuild.log` 尾部對照表）
- 證據：`run-rebuild.log`

## G2 · gates.py（版內自檢 16/16）

- 命令：`cd <scratch>/rebuild && tools/venv/bin/python gates.py > <scratch>/gates.log 2>&1`
- rc=0；**16 PASS / 0 FAIL**，`FAILURES: none`
  （含 P1 VOL.4 + 日期、頁腳 8/8、無 VOL.3 殘留、P1 刊頭行寬 {330: 319.2, 372: 389.5}、同基線墨跡碰撞 0、
  頁框墨跡穿越 0、P6 圖表標籤覆蓋 0、gloss 29 項齊全、P7 金句 8 句 ×2 且頁碼正確、讀者園地披露齊全、
  圖片 5/5+出處、P7 金句區距預告框 107px、P1 頭條 41 字 ≤56）
- 證據：`gates.log`

## G3 · freeze baseline（核心 8/8）

- 命令：`tools/venv/bin/python freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out <scratch>/freeze-base`
- rc=0；**8/8 SVGs byte-identical**（repointed files: none）：
  p1 `bd87a867…`、p2 `0a8300c3…`、p3 `e3c97081…`、p4 `f539bdb8…`、p5 `51629e93…`、p6 `a3c3cf38…`、p7 `43b845fc…`、p8 `a7b7a661…`
- core 完整性自檢通過：8 個 shipped core SVG 前後哈希不變。
- 證據：`freeze-base.log`、`freeze-base/`（build-copy）

## G4 · freeze diff（版 vs 核心）

- 命令：`tools/venv/bin/python freeze.py diff --core-svg production/2026-w47/core-pt/svg --edition-svg production/2026-w47/2026-w47-pt-zh-tw/svg --json <scratch>/freeze-diff.json`
- rc=0；每頁增/刪字符串：p1 +20/−20、p2 +21/−21、p3 +13/−13、p4 +17/−16、p5 +22/−21、p6 +12/−12、p7 +35/−35、p8 +175/−180（p8 增 128 字符串/減 130 字符串，按計數展開為 +175/−180 行）
- **新增 CJK 合計 948**（p1 85、p2 70、p3 50、p4 69、p5 68、p6 45、p7 116、p8 445；相異 201 字；含 U+3000 ×9）
- 非 CJK 殘差核對（`cjk-reg-check.log`）：每頁增/刪去 CJK 後的殘差僅為讀者語家具（頁腳英文→繁體、P1 副標葡語標語→繁體說明）／空白口徑／括注換行拆分／引號與中圓點本地化——**葡語題干/正文 0 差異**。
- 證據：`freeze-diff.log`、`freeze-diff.json`、`cjk-reg-check.log`

## G5 · CJK / opencc 簡體殘留核對

- 新增 CJK 201 個相異字逐字 `opencc s2t`：**全部恆等（已是繁體），非繁體字 0**。
- 全版 `s2t` 掃描（SVG 全部文本行 + text.md + ABSTRACT.txt）：僅 8 行被改動，皆為 opencc 過度映射誤報——`才`→`纔`（1 處，P7）、`布`→`佈`（7 處，P8）；`才`/`布`本身即台灣標準繁體寫法。故**真簡體殘留 0**；ABSTRACT.txt 為 s2t 恆等。
- 證據：`opencc-scan.log`、`cjk-reg-check.log`

## G6 · occlusion 幾何審計（本版 + 核心，皆 0）

- 命令：`tools/venv/bin/python occlusion_audit.py <svgdir> --json <scratch>/occlusion*.json`
- 本版：**0 flags**；自檢通過（6 類 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 全觸發，對照靜默）。
  核心：**0 flags**（同上自檢）。
- 證據：`occlusion.log`、`occlusion.json`、`occlusion-core.log`、`occlusion-core.json`

## G7 · PIL 真墨全量橫掃（inkprobe）

- 命令：`tools/venv/bin/python inkprobe.py <svgdir> <scratch>/inkprobe*.json`
- 本版：31 個奶油框，**全部末行墨底在框內**；全域 RIGHT/LEFT 溢出 **0**；僅每頁 2 個 FOOTER 旗標——皆為基線 y=2624 的頁腳本身（墨底 2626–2627，設計值，occlusion 工具豁免）。
- 盒標題墨右距框右（最緊者）：P2 日程框首行 −16.5px；其餘 −30.5 至 −250.5px（P1 數字盒 −60.5；P2 `PARA NÃO ERRAR` −140.5、`VOCÊ SABIA?` −250.5、`E VOCÊ?` −160.5；P7 `ERROS COMUNS` −102.5、`A PALAVRA` −164.5、`CARTAS DOS LEITORES` −143.5）。
- 最緊框底餘量（皆框內）：P2/P3/P4 `E VOCÊ?` −2.42/−2.48px、P5 `E VOCÊ?` −2.51px、P7 工具箱 −2.48px。
- D1–D3 框（與 core 數值逐字節相同）：P1 底邊 2348 末行墨底 **−15.4**；P3 底邊 551 末行墨底 **−10.35**；P6 底邊 854 末行墨底 **−8.2**。
- 證據：`inkprobe.log`、`inkprobe.json`、`inkprobe-core.log`、`inkprobe-core.json`

## G8 · 交付 PDF 像素實測（200dpi，印 PDF 渲染）

- 渲染：`pdftoppm -r 200` 印 PDF 全 8 頁 → `render/p1-1.png … p8-8.png`
- D1：P1 奶油底邊 px=2347.68（svg 2348.0）；框底至 2409 間無文字墨，僅 y=2350 分隔線（全幅 3696px = 1774 svg px 全寬）。
- D2：P3 551–596 間零墨；首墨為下框標題頂 596.2。
- D3：P6 854–884 間零墨；首墨為下框標題頂 884.2。
- D5 gloss：末墨行 svg 398.9，底餘量 **+47.0**；末行墨右 svg 1013.3，右餘量 +398.2（`。` 在 SC 面渲染為小圓點）；第 3 行墨右 1390.1，右餘量 +21.4。
- 全頁橫掃（`pixel-sweep.log`）：8 頁墨跡 x 範圍均為 svg [88.3, 1861.4]（版框 88–1862 內）；y>2596 的墨僅頁腳行 2610.24–2624.64。
- 證據：`pixelscan.log`、`gloss-pixels.log`、`pixel-sweep.log`、`render/p*-*.png`、
  `render/crop-P1-D1.png`、`render/crop-P3-D2.png`、`render/crop-P6-D3.png`、`render/crop-P4-gloss.png`

## G9 · D5 gloss PIL 探針

- 命令：`tools/venv/bin/python gloss_probe.py`（`gloss-probe.log`）
- 框 989/270.48/422.5/175.4（右 1411.5、底 445.88），4 行：
  L1 `譯注｜o agregado 總比數 · os pênaltis`、L2 `十二碼大戰 · a decisão 決賽 · o título`、
  L3 `冠軍頭銜 · a pausa 休息期 · a taça 獎盃`、L4 `。`
- 右餘量（末行）：PIL **+383.5**（size 21 TC 面，與報告值一致）／精確 20.5pt 2× 測量 +384.0；
  底餘量：TC 面 +47.7、SC 面 +46.2（精確 20.5pt）；報告值 +45.7 與三法相差 0.5–1.3px（字體面/取整口徑差）。
- 第 3 行（最長行）右餘量 +21.0（精確 20.5pt）。
- 證據：`gloss-probe.log`、`gloss_probe.py`

## G10 · p8 extract / compare

- 命令：`tools/venv/bin/python p8.py extract --p8 …/svg/p8-avaliacao.svg --total 150 --json <scratch>/p8-extract.json`
  `tools/venv/bin/python p8.py compare --core-p8 core-pt/svg/p8-avaliacao.svg --edition-p8 …/svg/p8-avaliacao.svg --total 150 --json <scratch>/p8-compare.json`
- extract：noted set = **150 of 150**；compare：**CLEAN**，core 150 / edition 150，missing=[]、extra=0、**keydiff=[137, 138]**。
- 證據：`p8-extract.log`、`p8-extract.json`、`p8-compare.log`、`p8-compare.json`

## G11 · 印/網文字層一致（pdftotext）

- 命令：`pdftotext [-layout] A-Lucerna-VOL4.pdf print[.txt]`、`pdftotext [-layout] A-Lucerna-VOL4-web.pdf web[.txt]`（scratch 內）
- raw 文本：印/網各 **44,666 字節，`cmp` 逐字節一致**；
  `-layout` 文本：印/網各 **103,995 字節，`cmp` 逐字節一致**。
- 證據：`print.txt`、`web.txt`、`print-layout.txt`、`web-layout.txt`

## G12 · P8 最小字號

- 命令：PyMuPDF（venv `fitz`）取印/網 PDF 第 8 頁全部 span 字號。
- 印 P8 最小 **10.125pt**（599 個 span）；分佈 10.125–34.5pt；網 P8 分佈與印版完全相同。
  SOP §1.1 下限 9.75pt，本版高出 0.375pt。

## G13 · 150 題鍵三方比對 + 逐題手驗

- 登記表轉儲：`reg_dump.py`（run.py 進程內轉儲 REG）→ `reg-edition.json`（150 條）、`reg-core.json`（150 條）。
  REG 比對：鍵差異僅 137、138（繁體譯文鍵）、150（開放題標記）；其餘 147 鍵逐字節相同；
  210 個字段差異皆為簡→繁字形或台灣詞彙本地化，72 處詞彙差異逐條核對、0 語義改變（`cjk-reg-check.log`）。
- 三方比對（`key-triple-check.log`）：REG vs text.md Respostas vs P8 印出鍵——**149/150 三方完全一致**，
  僅 Q150 設計內差異（REG `（開放題，範文如下）` / text.md `✓ 範文見本版 H 區（88 詞）` / P8 `✓`）。
- 逐題手驗：text.md 全文 534 行逐行讀過；每題依據見 `keycheck-150.json`（150 項，pass 150 / fail 0；鍵程序化取自 REG，依據為本輪手驗記錄）。
  抽檢算術：16–30 日共 15 天、工作日 10 天、週末+假日 5 天、10+5=15；範文實數 **88 詞**（80–100 內）。
- 證據：`reg-edition.json`、`reg-core.json`、`reg_dump.py`、`key-triple-check.log`、`gen_keycheck.py`、`keycheck-150.json`

## G14 · 日期/星期核驗

- 命令：`TZ='America/Toronto' date -d` 逐日核驗 15 個日期。
- 全對：11/07 週六、11/08 週日、11/15 週日、11/16 週一、11/17 週二、11/18 週三、11/19 週四、11/20 週五、
  11/21 週六、11/22 週日、11/23 週一、11/27 週五、11/30 週一、12/06 週日、2027/01/01 週五。

## G15 · ABSTRACT.txt

- 全文 **531 字節 / 211 字 / 單行（尾換行）/ 無 ASCII 雙引號**；
  開頭「`A Lucerna 葡萄牙語週報 VOL.4：`」——首輪 D4 已消除，補寫正確。
  含目標語名（葡萄牙語）、A2–B2、150 道練習題；與核心摘要逐句對照無事實出入。
- 證據：版目錄 `ABSTRACT.txt`（生產文件，只讀核對）

## G16 · 字體面普查（觀察 O3 的數值依據）

- `grep -ho 'font-family="…"' svg/*.svg`：Newsreader 1228、**Noto Sans CJK SC 614、Noto Serif CJK SC 328**、UnifrakturMaguntia 1；
  **TC 面 0 處**。`svglib.py:52–53` 硬編碼 SC 面，fanout 繼承核心寫法。
- 渲染影響實測：`。`墨頂 SC 面 393.2 vs TC 面 387.2（@20.5pt，相差約 6px；見 G9）。

## G17 · 全頁目視 P1–P8

- 交付印 PDF 110dpi 全頁（`render/pg1-1.png … pg8-8.png`）逐頁看過；200dpi 重點裁圖 4 張（G8）。
- 結果：無溢出、重疊、壓頁腳、圖片缺失、豆腐塊。P5 `O PLANO DA ESPERA` 第 1/5 項孤 `）`（首輪已知觀察 O2）仍在，無溢出。

## 匯總

| 門 | 結果 |
|---|---|
| run.py 重建 | rc=0，TOTAL 150，0 溢出，8/8 字節一致 |
| gates.py | 16/16 PASS |
| freeze baseline（核心） | 8/8 |
| freeze diff | 新增 CJK 948，0 非繁體；葡語正文 0 差異 |
| occlusion（本版/核心） | 0 / 0 flags |
| PIL 真墨橫掃 | 框標題最緊 −16.5px；D1 −15.4 / D2 −10.35 / D3 −8.2（皆框內） |
| 交付像素 | D1/D2/D3 框下淨空；全頁墨跡框內；頁腳外無墨 |
| p8 | extract 150/150；compare CLEAN，keydiff [137, 138] |
| 印/網文字層 | raw 44,666 B 一致；layout 103,995 B 一致 |
| P8 字號 | 最小 10.125pt（≥9.75pt） |
| 150 題鍵 | 三方 149/150 一致，Q150 設計內差異；手驗 150/150 pass |
| 日期 | 15 個日期星期全對 |
| ABSTRACT | 531 B，刊名在首，格式合規 |
| 簡體殘留 | 真殘留 0（僅 opencc 誤報才/佈） |

**結論：(a) 零缺陷，可定稿。** 缺陷 0 項；觀察項 O1–O5（見 PROOF-NOTE.md），均不阻定稿。
未 commit、未 push；生產目錄未寫入任何文件。
