# GATE-LOG — 2026-W47 · nl → zh-tw · proof1 機械門實跑證據（build-3）

復校員獨立實跑，不信 KIT，只信自己跑的結果。全部命令用 `tools/venv/bin/python`；
TMPDIR 全程指向本 scratch 下 `tmp/`（系統 /tmp 512M 常滿，未用）。
工作區：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-zh-tw1/`。
證據文件見本目錄：`gates-zh-tw.json`、`gates_proof1.py`、`p8-compare-proof1.json`、`p8-extract-proof1.json`、
`p8-compare-3way.json`、`registry-new.json`、`freeze-diff-proof1.json`、`freeze-core-proof1/`、
`boxtitle-proof1.log`、`orphan-proof1.log`、`orphan-sweep-proof1.json`、`spill-proof1.log`、
`crop-p8-head-proof1.png`、`render/all-1.png`…`render/all-8.png`（交付印 PDF 150dpi 渲染）、
`render/p-4.png`、`render/p5-5.png`、`render/p6-6.png`、`render/p8-8.png`。

## §0 身份核對（磁碟為準）

- 探針：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，rc=0；scratch 探針文件 `probe.txt` 寫入成功。df：150G 總 / 91G 已用 / 59G 空閒。
- 印 PDF `De-Lucerna-VOL4-nl-zh-tw.pdf`：SHA `6de893ca2811357c7be524b2b17e78af1c5362abc647e957d8665559466c704a`，25,993,186 字節——**與任務一致**。
- 網 PDF `De-Lucerna-VOL4-nl-zh-tw-web.pdf`：SHA `172c1be81d32d871c323064c685e0918e41b12b29a25a19a50cf4926d217ff20`，2,369,230 字節——**與任務一致**。
- text.md `2026-w47-nl-zh-tw.text.md`：SHA `30af89dfbfe2dd31caf41a7e13a21dc615f77c0a1dde18ba9c93328e5d806c60`，44,320 字節——**與任務一致**。
- KIT 所載三 SHA（`WEEKLY-KIT.md:20-21,24-25,29,179-180`）與上表一致。
- 改動範圍：`diff -r` 本版 vs staging（排除 svg/cards/PDF/`__pycache__`）僅 7 文件不同（5 個 py 源文件 + text.md + KIT）；text.md diff 恰好 1 行（:415 `kort `，+5 B）；SVG 僅 p3/p4/p6/p7/p8 變化，p1/p2/p5 字節一致；8 個 SVG 哈希與 delta `svg-hashes-after.txt` / `svg-hashes-postcompare.txt` 逐一相符。
- `git status`：版目錄為未跟蹤（`?? production/2026-w47/2026-w47-nl-zh-tw/`），無已跟蹤文件被改動（見 PROOF-NOTE 末節透明說明）。

## §1 門禁套件（`gates_proof1.py`，9 項，ALL PASS）

- 命令：`tools/venv/bin/python gates_proof1.py <edition> zh-tw`（由 delta `gates_delta.py` 拷貝，SCRATCH 指向本目錄；內含 occlusion / p8_extract / p8_compare / freeze自比對 / print_web_text / pdftotext / p8_fontsize / p8_chips / s11_svg）。
- 結果：**OVERALL: ALL PASS**（見 `gates-zh-tw.json`）：
  - occlusion rc=0 flags=0；p8_extract noted=150/150；p8_compare verdict=CLEAN（stdout 口徑 keydiffs=0，見 §4 口徑說明）；
  - freeze_sha256（版內自比對）：run rc=0，match=8/8；
  - print_web_text：8/8 頁 posdiff=0 msdiff=0（P1:749/749 P2:705/705 P3:664/664 P4:658/658 P5:685/685 P6:648/648 P7:735/735 P8:1677/1677）；
  - pdftotext_nonempty：print=44,329 B，web=44,329 B，web_size=2,369,230；
  - p8_fontsize：answer-zone min=10.12pt，median=10.12pt，spans=566；
  - p8_chips：core={'A2': 8, 'B1': 24, 'B2': 3} = edition；
  - s11_svg：off-palette={}，gold/old=False，stroked_rects=0，VOL.5=5（core 5），paper_fills=8。

## §2 幾何遮擋審計（`tools/occlusion_audit.py`）

- 命令：套件內第 1 項，`tools/venv/bin/python tools/occlusion_audit.py svg/`（cwd=版目錄）。
- 結果：**rc=0，0 flags**，自檢通過。盒標題無邊框奶油盒部分不在其覆蓋內——由 §6–§9 的獨立光柵實測覆蓋。

## §3 `run.py`（TOTAL 150）

- 套件 freeze 自比對內含：`run.py` rc=0、**TOTAL 150**、by page 10/18/18/18/18/18/12/38、A2 46 / B1 73 / B2 31；獨立取 registry 時（`dump_reg_proof1.py`）同值：registry 150，by page 相同，by level 相同，model words 81。
- 0 FLOW OVERFLOW / HEAD TOO WIDE（delta 日誌 §4 同值；本輪套件輸出無溢出警告）。

## §4 p8 compare / extract（顯式 --core-p8/--edition-p8；--total 150；--json 本體）

- 命令：`p8.py compare --core-p8 <core-nl>/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150 --json p8-compare-proof1.json`。
- 結果：core 150 noted / edition 150 noted；**status: CLEAN，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138]**。rc=0。
- `p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150 --json p8-extract-proof1.json`：**noted set = 150 of 150**。rc=0。
- keydiff 裁決：137、138 為 E 節翻譯題（NL→繁體中文），鍵本身就是讀者語；核心簡體 vs 本版繁體，按設計不同，非缺陷。修前 [137, 138, 140]，D9 已把 140 移出。
- 口徑說明：套件 `gates_proof1.py` 的 p8_compare 項數的是 stdout 裡 `key diff` 行（0），與 `--json` 本體的 `keydiff=[137, 138]` 口徑不同——以後者為準。

## §5 三源逐題比對（REG × text.md × P8 印刷鍵）

- 方法：`dump_reg_proof1.py` 取 REG（150）→ `p8compare_proof1.py`（三源 verbatim，text.md 標記 `— 答案： KEY（note）` / `(答案 <letter> ·`）→ `p8-compare-3way.json`。
- 結果：**3-way MATCH 149/149（排除 Q150 例外）；DIFF=[]，MISSING=[]**。
- Q140：`{"n": 140, "level": "B2", "type": "翻譯", "page": 8, "reg_key": "Ik maak een surprise met een kort gedicht.", "reg_note": "surprise 是固定搭配", "md_answer": "Ik maak een surprise met een kort gedicht.", "p8_key": "Ik maak een surprise met een kort gedicht.", "verdict": "MATCH"}`。
- Q150：開放寫作例外——P8 鍵 `✓`，text.md 載 Tekstmodel（81 詞），REG 為開放題占位 `（開放題，範文見下）`。
- 配對鍵 25–28 = d/c/a/b，141–144 = b/c/d/a；配對字母另對印刷選項逐項核對無誤（見 PROOF-NOTE）。

## §6 freeze：核心基線 + diff

- 基線：`freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-core-proof1` → **rc=0，8/8 SVG byte-identical**（p1–p8 逐頁 OK 行）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。`--core-svg` 指向核心的 svg 子目錄，build-copy 內是核心版重建（非本版自比）。
- Diff：`freeze.py diff --core-svg <core-nl>/svg --edition-svg <edition>/svg --json freeze-diff-proof1.json` → rc=0；逐頁 +/− 串：p1 +31/−25、p2 +24/−24、p3 +11/−11、p4 +15/−16、p5 +22/−23、p6 +16/−16、p7 +33/−33、p8 +217/−221；**TOTAL added CJK characters: 1051**，逐頁新增 CJK 全部繁體（含每頁 1 個 U+3000 全角空格分隔符）。
- 移除串核查（`freeze-diff-proof1.json` 全量走讀）：移除的拉丁串均為家具/講解層合法本地化——刊頭 `LUCERNA DUTCH WEEKLY`→繁體刊頭副標；`perfectum`→「完成式」（P8 答案注 40/42）；金句 #8 譯法重寫（見 PROOF-NOTE）；PAS OP 注釋重寫。無荷蘭語正文丟失。
- 簡繁殘留掃描（text.md 395 異體 CJK / SVG 414 異體 CJK 對簡體專用字集）：僅 `文`（兩岸同形）命中；`征` 3 處均在「遠征」；無 `台`；**零簡體字殘留**。
- 版內自比對（套件第 4 項）：clean-dir 重跑 `run.py` 再 sha256 比對 **8/8**。

## §7 D11 盒底余量（交付 PDF 光柵為準）

- 方法：`inkprobe_d11_proof1.py`（delta 方法重跑；SVG 盒 + 末行基線 + 雙渲染真墨探查；墨定義 r<200 或 g<200 或 b<190；紙定義 r≥228 且 g≥226 且 b≥210）。
- SVG：盒 `<rect x=1439.5 y=591.6 w=422.5 h=638.0>` 底 1229.6；末行 `18:45 uur.` 基線 y=1209.49，基線余量 **+20.11px**（≥20px 門檻）。
- [cards 1×] 末行帶最低真墨 y=1209.00，墨底余量 **+20.60px**；盒底下 7px 條帶 non-paper=0。
- [交付印 PDF 150dpi 渲染 `render/p-4.png`] 末行帶最低真墨 y=1209.12，墨底余量 **+20.48px**；盒底下 7px 條帶 non-paper=0。
- spill 掃描（§8）：P4 該盒 0 BELOW 命中。P4 目視（`render/all-4.png`）：末行在盒內，下有明顯留白。

## §8 孤兒標點橫掃 + spill 橫掃

- 孤兒橫掃（`orphan_proof1.py`，nl-ko 復校腳本改針為本版 D6/D7/D8/D10 內容；PIL + svglib 雙 advance；brute-force 第三法）：
  - [PIL-advance] lines=1419 class-a=0 class-b=0（8 頁每頁 0/0）；[svglib-advance] 同值 0/0。
  - [brute-force] 行首標點 `<text>` 元素 8 個，行內最左 0 個（P1 `：柏林奧林匹克`；P8 `：`×2、`，`×1、`）`×3——均為行中定位符/答案區標點）。
  - 定向行：D6 `用現在完成式填空。注意助動詞` (2250.5) / `hebben/zijn。` (2280.225)；D7 `de wedstrijd 比賽；de groepswinst` (725.66) / `小組頭名；de kwartfinale 八強賽；` (755.385) / `scoren 進球。` (785.11)；D8 `練習數據：虛構數字，僅供練習，非真實調查。` (635.02) / `問題：你在鞋裡放什麼？（100 名年輕人）` (659.44)；D10 `截稿時未收到真實來信或第 8 版最佳作文，` (1754.27) / `刊登示例信，承諾順延 VOL.5。` (1782.67)。四處全部乾淨。
- Spill 橫掃（`spill_proof1.py`，`spill-proof1.log`）：BELOW 命中 7 處，全部為盒下獨立版塊（P1 `HET WOORD VAN DE WEEK` +24.0、P1 `讀頭版，選出正確答案` +44.0、P2 `譯注｜de schoen…` +50.5、P2 `Let op: schrijf je gedicht…` +32.0、P5 `譯注｜de surprise…` +50.5、P7 `HET WOORD 本週生詞` +60.0、P7 `BRIEVEN VAN LEZERS` +60.0）——與 delta 日誌 §6 同類裁決，非溢出；P4 HET PROGRAMMA 盒（底 1229.6）僅 ABOVE 命中（盒上標題），0 BELOW。ABOVE/SIDE 均為圖注/鄰盒標題。

## §9 盒標題光柵復測 + 奶油盒全盒真墨探查

- 盒標題（`boxtitle_proof1.py` → `boxtitle-proof1.log`；定義：32 個 Flow head 源字符串 + 26 個奶油盒標題 = **58 項**；量度：cards 1× PIL 真墨，掃描窗至限值+28px 溝槽）：
  - TOTAL 58，OVER-EDGE 1：P8 `A　VUL DE KRONIEK IN` ink_right=537、limit=510.5、margin=−26.5（裁決見下）。
  - 其餘 57 項全部 ok；最緊余量 +0.5px（P1 `NA DE INTOCHT: DE SCHOEN`、P2 `A　BEGRIJPEN` / `C　SCHOEN EN GEDICHT` / `D　WOORDEN`；P7 `A2　VOETBALWOORDEN` / `B1　DE VERLEDEN TIJD` / `B2　BIJZINNEN MET OMDAT` 均 +0.5/+1.0；P8 `H　SCHRIJF ZELF` +1.0）。
  - P8 head 裁決（STRADDLE 規則）：標題節點 x=88.0 y=201 size=21 weight=700；PIL advance（Newsreader SemiBold 21pt）264.92px，墨止 x≈353，余量 +157.6px；超限墨只在 y=173–181 行（基線之上、字形帶之外），屬 B 欄 B1 徽章矩形（x=538.5 y=180.0 w=60.0 h=30.0 fill=#46581f）與欄頭橫帶；字形帶內 510.5 右側無墨；staging cards 同值（ink_right=537、同行）、交付 PDF 150dpi 渲染同值（537.6）；裁圖 `crop-p8-head-proof1.png` 目視無裁切、無重疊。——觀察項，非缺陷。
  - CREAMSTRIP 翻案：腳本硬編碼 P5 盒底 1023.5 為錯值（本版真底 936.5；條帶落在盒下照片 `<image x=1439.5 y=962.5 h=250.0>` 內，故 2961/2961 非紙像素）；按真底重探：P5 盒底下 7px 條帶 0 非紙 / 0 墨（雙渲染），末行真墨余量 +3.50px（cards）/+3.38px（PDF）。P2 條帶（底 1445.8）0 非紙像素。
- 奶油盒全盒真墨探查（本輪補寫探查腳本；盒底下 7px 條帶 + 末行真墨底，cards 與交付 PDF 150dpi 雙渲染）：
  - P2 8 盒：條帶全部 0 非紙 / 0 墨；末行真墨余量最小 **+3.43px**（EN JIJ 盒，底 1387.8，末行基線 1383.36，交付 PDF 真墨底 1384.32）；其餘 +9.25~+53.14px。
  - P5 4 盒（EN JIJ 盒見上）：其餘盒末行余量 +9.25px 以上；條帶全部 0/0。
  - P6 3 盒：條帶全部 0 非紙 / 0 墨；末行真墨余量 **+50.43px**（譯注盒，底 906.4）、**+4.00px**（D8 圖表盒，底 665.0，末行基線 659.44，cards 真墨底 661.00；PDF +4.52px）、**+11.00px**（VOOR OF TEGEN 盒，底 1000.0）。
  - creambox desc-clear 負值（P2 EN JIJ −1.6、P5 −1.5、P6 +0.0）均為固定降部余量假設對中文行的模型偽報，已由真墨翻案。

## §10 印/網文字層 + 斜體 + P8 字號

- `print_web_text`（套件第 5 項，PyMuPDF 位置排序）：8 頁 posdiff=0、msdiff=0；tokens P1 749、P2 705、P3 664、P4 658、P5 685、P6 648、P7 735、P8 1677（P8 較 build-2 +1 = `kort`）。
- pdftotext：印 44,329 B = 網 44,329 B；網 PDF 2,369,230 B < 7 MB。
- 斜體（舊 D2 重測）：印 PDF italic span 1 處（P1 `«de groepswinst»`，`Newsreader16pt-Italic`，16.12pt）；網 PDF italic span 1 處（同詞同字號，`LucernaNewsreader-Italic`，16.12pt）。——舊 D2 未復現。
- P8 最小字號（套件第 7 項，PyMuPDF 逐 span）：answer-zone min **10.12pt**（median 10.12，566 spans）≥ 9.75pt。

## §11 舊 build 三項缺陷重測（build-3 交付件）

- 舊 D1（P2 選項 c 超出版心）：選項 c 文本為 `c. eten voor Sinterklaas' paard`（`svg/p2-leven.svg` y=2233，x=1473.5，size 23）。PIL advance 右緣 1790.09（Regular 23pt）/ 1808.77（SemiBold 23pt），余量 +71.91/+53.23px；交付印 PDF span（`Newsreader16pt-Regular`，17.25pt）bbox 右 1346.04pt vs 版心 1396.5pt，余量 +50.46pt；150dpi 光柵最右墨點 1793.28 SVG px，余量 **+68.72px**。三法一致，在版心內。——未復現。
- 舊 D2：見 §10（網 PDF 帶斜體）。——未復現。
- 舊 D3（譯名不統一）：text.md：`聖誕老人新聞` ×8（:106/118/304/387/392/405/412/427）、`辛特克拉斯新聞` ×0；`《荒島遠征》` ×3（:239/:244/:374）、`《魯濱遜遠征》` ×0；印 PDF 文字層 `辛特克拉斯新聞`/`魯濱遜遠征` 0 次、`聖誕老人新聞` 8 次；P8 SVG 0 次；staging text.md 計數相同。——未復現。

## §12 全文與事實核驗（摘要；全文見 PROOF-NOTE）

- text.md 431 行全文通讀；交付印 PDF 8 頁逐頁目視（`render/all-1.png`…`all-8.png`，150dpi）；無溢出、重疊、壓頁腳、裁切。
- 算術重算：19 天、1 天、4 小時、17 年、65、100、13 天；範文 81 詞（實數）。
- 日期/星期（`date -d`，Europe/Amsterdam）：14/11 週六、15/11 週日、16/11 週一、21/11 週六、22/11 週日、24/11 週二、29/11 週日、5/12 週六，全部吻合。
- 外部事實（2026-11-11 檢索）：Heel Nederland Leest 2026 =《Het diner》（CPNB 官網 + Wikipedia + 地方媒體）；歐冠 MD5 2026-11-24 Real Madrid–PSV、Feyenoord–Porto（uefa.com）；Feyenoord–Ajax 2026-11-29 14:30 De Kuip（KNVB 官方賽程）；PSV 26 分等 P4 內容與舊 build 復校的外部核實一致且正文未動。
- ABSTRACT.txt：單行、無 ASCII 雙引號，含 Lucerna、VOL.4、150 道練習題、A2–B2、繁體中文講解。
