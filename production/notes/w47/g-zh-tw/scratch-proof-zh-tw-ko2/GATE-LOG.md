# Gate log — W47 zh-tw × ko, proof1 #2（fix1 後完整重校，機械門全跑，輸出留檔）

- 版：`production/2026-w47/2026-w47-zh-tw-ko/`（繁體中文 × 韓語讀者語，fix1 後重建）
- 交付物 SHA（開工前核對，全部機械門跑完後復核未變）：
  - 印刷 `Lucerna-VOL4-KO.pdf` 16,838,020 B / `c04102a9a1ceef1cf25fc7f3df6e69266e5f3d8bb2fec8d4370a3f782217d3a6`
  - 網頁 `Lucerna-VOL4-KO-web.pdf` 2,325,041 B / `ed9e11a5c8997eb6b09cd6fd1f9bad6b64d686e2280d4730eac3d48ff65bad61`
  - `2026-w47-zh-tw-ko.text.md` 53,916 B / `2af17f023ab203259aeeb294b04f31e4bbb766398a28ec5f7fd2f163622b06f7`
- 核心對照 core-zh-tw（復校前後未變）：印 `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a`（19,420,552 B）、網 `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240`（2,324,042 B）、text `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`（49,798 B）。
- 探針：開工前 `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0（返回 `da0c4eb8…`）；目錄 `scratch-proof-zh-tw-ko2/` 真實寫盤通過（`probe.txt`、`gates/`、`baseline/`、`render/`、`view/`、`flow.txt` 均已寫入）。`TMPDIR=<scratch>/tmp`。`/dev/null` 為字元設備、正常。磁碟 68G 可用。解釋器全程 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。

## 0. K1 核對（先於門禁）

- 舊錯形全版計數（8 個 SVG + text.md + 印／網文字層）：`入圍이에요` 0、`入圍은` 0、`入圍을` 0、`市集는` 0、`鋼雕은` 0。
- 新形：入圍는（p7-lang 1 + text.md 1）、鋼雕는（1+1）、入圍를（1+1）、市集은（1+1）、入圍예요（p8-test 2 + text.md 2）。
- 源行：`content7.py:43`（入圍는／鋼雕는）、`:44`（Q105 入圍예요）、`:52`（入圍를）、`:60`（市集은）、`content8.py:58`（Q132 入圍예요）；text.md :4443／:4479／:4603／:4763／:6210／:6266。

## 1. run.py（副本重建）+ freeze

- run.py：整版複製至 `build-copy/` 後在副本內執行（生產目錄零寫入），`gates/run.log`，**rc=0**；overflow / overwide / warn / error 命中 0；REGISTRY TOTAL 150（A2 44 / B1 74 / B2 32；by page 1:10 / 2:18 / 3:18 / 4:18 / 5:18 / 6:18 / 7:12 / 8:38）。副本重建 8 個 SVG 與出貨 SVG `cmp` **字節一致**。
- freeze baseline（倉根執行）：`baseline: 8/8 SVGs byte-identical`，p1 2f021d71…、p2 050e53b0…、p3 6b01d169…、p4 80d4d8db…、p5 96565ffd…、p6 6301c38d…、p7 31f7898a…、p8 a390fcc6…；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`（`gates/freeze-baseline.log`）。
- freeze diff（core vs edition，`gates/freeze-diff.json`／`gates/freeze-diff.log`）：p1 +24/−25、p2 +35/−39、p3 +42/−47、p4 +36/−39、p5 +46/−47、p6 +31/−33、p7 +360/−120、p8 +188/−187——與舊版 B 逐頁相同；新增 CJK 共 4,690 字（舊版 4,692，差 −2 = 兩處 이에요→예요 各減 1 字）。逐頁新增 CJK 全為韓文音節 + 家具／被注詞彙，無簡體字、無意外新增中文。

## 2. checks.py（本版自帶）✅

- `CHECKS PASS`：8 條金句各恰出現 2 次、`SIMP_ONLY_HITS []`、P4 bars [90.0, 450.0, 900.0]、P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]（`gates/checks.log`）。

## 3. Occlusion 審計 — 0 flags ✅

- `selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`
- `production/2026-w47/2026-w47-zh-tw-ko/svg: 0 flags`（`gates/occlusion.log`）。

## 4. P8 extract + compare — 150/150，CLEAN ✅

- extract：`noted set = 150 of 150`（`gates/p8-extract.json`、`gates/p8-extract.log`）。
- compare：`core 150 noted / edition 150 noted / status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]`（`gates/p8-compare.log`）。
- core extract 另存 `gates/p8-core-extract.json`。

## 5. keycheck-150（三源交叉 + 全版掃查）✅

- 腳本：`keycheck.py`（proof1 #1 版，路徑改為 ko2 後重跑；見 §9 事件）。
- 結果（`gates/keycheck.log`、`keycheck-150.json`）：
  - B 解析 150 項，1–150 連續無缺；**三源一致 150/150，mismatches []**（Q150 歸一化為「✓」）。
  - SVG CJK 版獨有 {韓}、核心獨有 {英}；text.md 同然。
  - 彎引號：版 SVG U+0022 0、U+0027 1（`Kanahei's Little Animals` 專名）、U+201C/U+201D/U+2018/U+2019 皆 0；text.md 同然。
  - 英文星期／月份名、"next Sunday"／"Next Sunday"、"finish line"／"end point"、「下週日」、「다음 주 일요일」、BABYMONSTER、결승선、장소：版 SVG 與 text.md **皆 0**；「이번 주 일요일」版 SVG 2（字串計；第 3 處跨 SVG 節點，已核實）、text.md 2（同理）。
  - P8 六節標頭全為繁體中文 + 韓語對譯。
  - 寫作範文：去空白計 **142 字**，CJK+數字計 126，在 120–180 區間內，與文內「142자」標註相符。
- 填空鍵：`check_fillin_keys.py`（fix-ko1 gtools，`text.md` + 源目錄為參數）→ **54/54 在正文，缺失 []**（`gates/fillin-check.log`）。

## 6. Creambox（canonical 全版掃描）+ boxtitle + creambox-pil ✅

- canonical（`hidden_files/w47/tools/creambox.py`，`gates/creambox.log`）：
  - 36 盒（P1 5、P2 6、P3 7、P4 4、P5 8、P6 3、P7 工具盒 3）。
  - 負清除共 11 盒，全部為 −44.0／−37.0：P1「夜間遊行最終場，六福村見！」、P2「雙」／「新北耶誕城開城，燈亮到晚上」／「讀懂了嗎？ 이해했나요?」、P3「鋼雕藝術節：最後一週，快去」／「電影小課：」／「讀懂了嗎？」、P4「단어」、P5「西九爵士音樂節，免費戶外舞」／「月繼」／「讀懂了嗎？」——皆為盒下 +37／+44px 的下一欄標題／首句（假陽性類，與舊版同一批）；盒內自有末行均為大正清除。
  - inside-only 最小清除：P1 18.8、P2 41.8、P3 16.1、P4 35.8、P5 6.4、P6 19.9；P7 工具盒 inside +40.5／+12.5／+14.0，P7 匯總：3 盒、最小 inside +12.5、最小 desc-clear +6.5。
  - 唯一 desc-clear 負值：P5 迪士尼小檔 −0.4（末行僅一字「日」，無下行筆畫，0.30 係數公式偽影；PIL 真墨底清除 +4.4px，見 §7）。
- boxtitle（fix-ko1 gtools，真墨，`gates/boxtitle.log`、`gates/boxtitle.json`）：36 盒，**超框 0**，最小右余 18.5px（P1）、最小左余 18.0px。
- creambox-pil（fix-ko1 gtools，真墨，`gates/creambox-pil.log`、`gates/creambox.json`）：36 盒，**STRADDLE 0、CREAM-COVER 0**；各頁最小底清除：P1 16.5、P2 39.8、P3 14.1、P4 33.8、P5 4.4、P6 17.1、P7 10.5。

## 7. P6 abutting（真墨，獨立重測）+ P5 緊盒驗證 ✅

- 以 `occlusion_audit.parse_svg` 真墨盒重測：頒獎典禮 ink box [906.8, 955.8, 990.8, 977.5] baseline 974.0；夜間遊行 [991.4, 955.8, 1075.4, 976.2]；墨縫 **0.6px**，與核心先例完全一致（`gates/abutting-p6.log`）。
- P5 緊盒 PIL 真墨：迪士尼小檔盒末行「日」墨底至盒底 **4.4px**（creambox-pil 各頁最小底清除 P5 4.4px）。

## 8. 印／網文字層比對 + PDF 指標 ✅

- `pdftotext -layout` 印／網：各 95,029 字節（`gates/print.txt`、`gates/web.txt`；舊版各 95,034，差 −5 B，逐行 diff 僅 5 行皆 K1：P7 三行含四處、P8 兩行 Q105／Q132）。
- 字符多重集差：印刷獨有 0、網頁獨有 0（逐字相同）。
- PyMuPDF（`gates/pdf-metrics.log`）：印、網皆 8 頁、1462.5 × 2025 pt；最小字號 9.75pt（整刊與 P8 皆然）、最大 147.0pt（P1）、P8 最大 34.5pt。
- 網頁 PDF 2,325,041 B（< 7 MB）；BABYMONSTER 印網文字層皆 0。
- `pdffonts`：印、網兩 PDF 僅嵌入 TC 字體（NotoSansCJKtc／NotoSerifCJKtc／Newsreader 等），無 SC 字體（D5 記錄，見 PROOF-NOTE §7）。

## 9. 回歸差分（舊版 B → 新版）✅

錨點：舊版 B SVG（`scratch-proof-zh-tw-ko1/baseline/svg`）、B 版 text.md（`scratch-proof-zh-tw-ko1/baseline/build-copy/2026-w47-zh-tw-ko.text.md`，SHA `2e7038cc…`）、B 版源（`scratch-fix-zh-tw-ko1/old-build/`）。

- SVG：P1–P6 `cmp` 字節相同；P7 僅 4 個 `<text>` 節點（K1-1～K1-4，同一坐標）；P8 僅 2 個 `<text>` 節點（K1-5a／b，同一坐標）。
- text.md：`diff` 僅 6 行（:4443／:4479／:4603／:4763／:6210／:6266），皆 K1。
- 源：content12／34／56 完全相同；content7 :43／:44／:52／:60、content8 :58 僅 K1 行。
- 印／網文字層：見 §8，僅 5 行 K1。
- **除 K1 六處外無任何文字／版式變化。**

### 附：`keycheck.py` 路徑事件（已驗證無實質污染）

- 首跑直接複用 proof1 #1 的 `keycheck.py`，其 `S` 硬編碼指向 `scratch-proof-zh-tw-ko1`，致 ko1 的 `keycheck-150.json`／`gates/p8-extract.json`／`gates/p8-core-extract.json` 於 13:10 被新版重跑覆寫。
- 驗證：三文件只含答案鍵（不含注文）；以舊版 B 的 SVG（`ko1/baseline/svg/p8-test.svg`）重抽取比對——B 版鍵 == 現 ko1 文件鍵 == 新版鍵（全 True）；`keycheck-150.json` 各行亦只含鍵值（Q105／Q132 行皆為「入圍」），新舊版內容相同。
- 修正：將 ko2 副本的 `S` 改為 `scratch-proof-zh-tw-ko2` 後重跑，`keycheck-150.json` 已正確落盤 ko2（150 行，mismatches []）。

### 附：初跑失誤（皆非版面問題）

- `freeze.py` 取相對路徑，首跑在 home 執行報 `FileNotFoundError`；切倉根 `~/workspace/weekly-git` 重跑後正常。
- creambox／boxtitle／creambox-pil 三 gtools 取 `argv[1]`=SVG 目錄、`argv[2]`=輸出目錄；首跑誤傳 8 個 SVG 文件致 0 盒，以正確參數重跑後皆為 36 盒。
- 孤兒標點樸素掃查（按節點 x 距切分）初報 3 類命中，皆證偽（見 PROOF-NOTE §5）；以 `occlusion_audit` 真墨盒重切後為 0，與核心一致（`gates/orphan.log`、`gates/orphan2.log`、`gates/orphan3.log`）。

## 10. 其餘核查

- VOL：VOL.4 全版（SVG + text.md 計 21 處含 text.md 引用）；P7 的 VOL.3×2 為延期披露所指上期、VOL.5×1 為下期預告，均正確。
- ABSTRACT.txt：韓語摘要，含刊名／目標語／A2–B2／150 題與真實主題。
- 頁腳「제N면／전체 8면」8 頁齊全（每頁 1 處）。
- 8 張渲染卡片（`render/p--1.png` … `p--8.png`，150 dpi 自印 PDF 渲染）+ 網版 P1／P7（`render/web-p1-1.png`、`web-p7-7.png`）逐版目視：無溢出、無重疊、無裁切、無頁腳碰撞；K1 六處另有全解析度裁圖（`view/p7-b1.png`、`p7-mem.png`、`p7-b2.png`、`p8-q105b.png`、`p8-q132.png`）逐字確認。
- O1–O6 觀察項無回歸：O1「그 백 년의 여정을 기념해」新舊 print.txt 皆 1 處；O2 Q72 注在版；O3 Xiaoxue 14／샤오쉐 3（與舊版同數）；O4「燈區」新舊皆 1 處；O5 P6 墨縫 0.6px 獨立重測同值；O6 P5 desc-clear −0.4／真墨 +4.4 同舊版。
- D5 字體實測：SVG `font-family` 無 `Noto Sans CJK SC`（TC 717／Serif TC 1469／Newsreader 1142／UnifrakturMaguntia 1／DejaVu Sans 3）；純拉丁文節點 20 個，0 個用 SC；兩 PDF 僅嵌 TC 字體。
- U+FFFD：8 個 SVG + text.md 按字節計 0。
- 機械門跑完後復核：三交付物 SHA 與開工前一致，未改動任何源文件；兩目錄 `git status` 仍僅為 `??` 未提交狀態。

## 結論

機械門全綠；K1 六落點逐一驗證修復；回歸差分證明除 K1 外無任何變化；150 題三源一致；8 頁目視無缺陷。本版按 SOP §8 **可定稿（a）**。
