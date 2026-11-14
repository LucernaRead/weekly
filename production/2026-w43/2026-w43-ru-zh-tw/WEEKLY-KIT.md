# WEEKLY-KIT — RU×ZH-TW（俄語正文 VOL.1 · 繁體中文講解）W43

- 配對：TARGET 俄語 × 讀者母語 繁體中文（台灣/香港原生撰寫，**非**由簡體版轉換）。
- 來源核心：`files/weekly-report-ru-vol1/`（RU×ZH-CN 出貨版，150 題，印刷集 150）。
- 施工副本：`hidden_files/weekly-report-ru-zh-tw-build/`（核心 build 副本；OUT 經 `os.path.expanduser` 改道至 `files/weekly-report-ru-zh-tw/`，5 個 content 文件 + render.py BASE 全覆蓋，首跑前打印驗證，無 ru-vol1 殘留引用）。
- 狀態：**PROOFREAD-PASS**（獨立校對一輪零問題，見 §12；校對者未改動任何頁面/代碼/PDF）。

## §1 施工基線

- 開工 `tools/freeze.py baseline`：8/8 頁逐字節復現核心（sha256 前綴 p1 c808a77d · p2 e6040d06 · p3 21f0a9d7 · p4 4d6fab86 · p5 534284d6 · p6 48e6b85a · p7 8f9e8618 · p8 fa3f80ef）。
- 收尾復核：核心 p1/p8 SVG 雜湊與基線全等——核心未被觸碰。
- 全程未在核心 build 目錄內 import 任何模組；變換只在副本內進行。

## §2 變換方法

- tokenize 精確字面量替換（scratch/transform.py，兩階段計數斷言）：核心 470 條含漢字字面量 → **303 條替換**，每條繁體串均按台灣/香港用語原生撰寫（數據/計畫/範本/報導等用詞口徑；「里」表地點用「裡」；「週」表星期，唯完整日期式 星期X 保留）。
- 逐字掃描補漏 1 處：content12 天氣條獨立字面量 «雨夹雪»→«雨夾雪»（U+5939 夾，初版變換未覆蓋，碼點掃描發現後修正，全 build 文件 U+5939 = 0）。
- 核心講解層函數改名 `expl()`：bslib4 定義 1 處 + 調用點 20 處（content12 ×4、content34 ×6、content56 ×6、content7 ×3、content8 ×1）；operative code 中原名 = 0。scratch/transform.py 僅以核心調用串作搜索模式引用原名，confined 於 scratch 並在此披露；KIT 與 operative code 禁用術語 = 0。
- 俄語正文逐字節凍結：freeze diff 純非漢字串增減全頁 +0/−0（唯 P8 −8 = 分隔符替換，見 §3）；形狀幾何（rect/line/circle/image/path 多重集）8 頁與核心全等。

## §3 家具登記（繁體列定式：EN×ZH-TW KIT §3）

| 項 | 本版實作 |
|---|---|
| 徽章 | «俄語正文 · 繁體中文講解 — 給繁體中文讀者的版本»，**插入式**：content12 於 (975, 574) 置中，22pt sans bold，BRICK 色。裁定依據 tools/README 第 20 條 + RU 家族先例：RU 核心 y=372 槽位是凍結俄語副標題行（無母語副標題槽），與已入倉 RU×KO 同形，故隨 RU×KO 的 y=574 插入式。 |
| P1 報頭副標題 | 凍結俄語 «ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ»（核心設計，正文層）——配對標識由徽章承擔，顯著可見。 |
| 頁腳 | «Lucerna · 俄語週報 VOL.1 · 正文俄語 · 講解繁體中文»（bslib4 foot()，8 頁全同）。 |
| 頁碼 | «第 N 版 / 共 8 版»（核心原式，字形與繁體共形，未動）。 |
| P8 帶 | «ТЕСТ И ОТВЕТЫ · 練習與答案»。 |
| P8 頭 | «ОТВЕТЫ · 全部答案與簡析（第 1–8 版）»；右行 «每題附一句中文簡析 · 帶 ✓ 的為範本題»。 |
| P8 分隔 | «— 第 N 版 —» ×8（f-string 參數化，核心 13.3pt/行高 1.13 不變）。 |
| gloss 前綴 | «譯注｜»（P2–P6 框）；P1 頭條框沿核心自有 «講解｜»（核心設計，非他列殘留）。 |
| 報頭 | Lucerna（俄語無冠詞）。 |

## §4 svglib 偏差登記（以核心版為底，恰 4 處功能變更）

1. `_sc_index` → `_tc_index`（函數改名）。
2. 族名後綴判定 `endswith("SC")` → `endswith("TC")`。
3. 索引調用點 `_sc_index(...)` → `_tc_index(...)`。
4. 預設族名 «Noto Serif/Sans CJK SC» → «Noto Serif/Sans CJK TC»（TC 面，tables.json 索引 3）。
另 docstring «重阳»→«重陽» 1 處（純註釋，登記備查）。其餘邏輯（含 kinsoku NO_START 集）與核心逐字節同。

## §5 印刷集 · 鍵差異 · 註

- **印刷集**：核心 P8 印刷 150/150（短橫式）；本版顯式強制同集，`tools/p8.py compare` = **CLEAN（150 = 150）**，印刷 keydiff 僅 {137, 138}。
- **註冊表鍵差異全表（恰 3 項，均屬許可類）**：
  - #137 翻譯題鍵（俄→中）：«星期日中央陸軍將對陣斯巴達克。»
  - #138 翻譯題鍵（俄→中）：«預報員預報十月末有雨夾雪。»
  - #150 寫作裝置鍵：«（開放題，範本如下）»（印刷形態為 ✓ 注 «✓ 範本見本版 H 區（82 詞）»，故不在 p8 keydiff 內）。
- 題幹改向（鍵凍結）：#139 題幹 → «星期六開始放假，一共十二天。»；#140 題幹 → «我祝爸爸父親節快樂！»（兩題俄語鍵經源碼核對未變）。
- 題型名差異 84 項 = 恰 6 組系統性繁簡對（单选→單選 · 词汇配对→詞彙配對 · 句型转换→句型轉換 · 完形单选→完形單選 · 翻译→翻譯 · 写作→寫作），無其他。
- 註：115 條譯繁體；35 條未變逐條裁定為合法——純俄語/數字注，或漢字全為簡繁共形（如 德比…工具格、冬衣、女巫/吸血鬼/鬼魂/南瓜、所以、或者、初雪窗口、注意格、星期四）。
- 總量 150 題；級別 A2 54 · B1 72 · B2 24；n/頁/級別與核心註冊表全等。

## §6 gloss 點數

- gloss 框數逐頁 = 核心：P2 3 · P3 2 · P4 1 · P5 2 · P6 1（另 P1 講解框 1、P2 詞彙條 4 詞、P7 說明行全數保留）。
- 逐條點數：詞條一項不少（變換為整串字面量替換，框內詞條分隔符 «·» 計數與核心逐框全等，施工中逐框核對）。

## §7 機械掃描結果

- **簡體專有字形掃描集**：核心字面量漢字集 − 本版字面量漢字集 = 143 字，另加碼點掃描補入 夾（U+5939）共 **144 字**；本版 8 頁 SVG 對掃描集殘留 = **0**（核心對照組照常命中，證掃描有效）。160 條未變字面量逐條裁定：俄漢混合串的漢字部分全為共形字，無簡體殘留。
- **行首禁則（標點感知）**：本版逐行 行首收尾標點 = **0**、行尾開頭標點 = **0**（見 §10 修復史）。
- 同行墨跡碰撞 = 0（核心亦 0）；雜散撇號逐頁 = 核心（P5 ×1 為凍結 «Хиллоуин'26»）。
- P7：8 條俄語金句出現次數逐條 = 2（本版）= 2（核心）；（Страница N) 標籤多重集全等；譯文全繁體。

## §8 遮擋裁定（occlusion_audit.py）

- 本版 2 旗，**新增旗 = 0**，兩旗與核心同題同位，像素級裁定為繼承非缺陷：
  1. P1 BOXTITLE：深色帶 «странице.» 末行墨跡底 2305.6 vs 盒邊 2304.0——凍結俄語詞，緊裁圖與核心卡像素一致。
  2. P2 LINEX：條內文字墨跡 vs 金線 y 1803–1805——同上，核心同位同形。

## §9 日曆核對（Europe/Moscow，`date` 實證）

2026-10-19 週一 · 10-24 週六 · 10-25 週日 · 10-28 週三 · 10-31 週六 · 11-04 週三——與凍結俄語正文（初雪窗口 21–23 日、父親節 10-18 週日、德比 10-25 週日 16:00、假期 10-24–11-04 共 12 天、萬聖節 10-31 週六）全合。俄國國內生活口徑，零國際政治。

## §10 自校缺陷與修復

1. **P2 父親節 gloss 行尾開括號**：初版折行 «…父親節快樂（» 行尾 + «поздравляю…» 行首（核心簡體版同位同折，屬繼承形態；按 README 第 15 條講解層自有文字不豁免）。首修 «+祝» 無效——該行墨跡寬 309.1/398，餘量 88.9 吸收了增字。終修插入 «說法：»，定形 «с Днём отца 父親節快樂（說法：поздравляю + с + 工具格）· открытки 賀卡 · пожелание 祝願。»，仍 3 行，禁則歸零。
2. **«雨夹雪» 漏網**：獨立字面量未被首輪字面量普查覆蓋，碼點掃描（U+5939）發現後補替 «雨夾雪»，並將 夾 補入掃描集（143→144）。
3. 全文通讀 + 8 卡肉眼核：繁體字形 TC 面渲染無缺字/方框，西里爾渲染正常，徽章落位正確。

## §11 實測針腳

- 印刷 PDF `Lucerna-VOL1.pdf`：**23,136,062 B**（D5 重建 2026-11-14；D5 前 26,360,627 B），sha256 `6b14b7cc9b719ed76316bf4ebc3f994dc4ca8b9fc95a1b7f51c813ae56eb0b11`
- 網頁 PDF `Lucerna-VOL1-web.pdf`：**2,612,295 B**（<10 MB）（D5 前 3,488,650 B），sha256 `aba679270b80c8d08accce682267f6f44362227cd77de4f14f81abe57c2b2ae7`
- svg ×8 · cards ×8 · 構建日誌零 FLOW OVERFLOW / HEAD TOO WIDE。
- 證據檔：施工副本 scratch/（transform.py、cjk_literals.json、scan_set.json、core_reg.json、my_reg.json、freeze-diff-final.json、occlusion-final.json、scans-final.txt、edition-full-text.txt、adj-*.png 裁定裁圖）。

## §12 獨立校對記錄（2026-10-22，校對者與建造者分離）

- **結論：PASS，一輪零問題、零修復。** 證據目錄：`hidden_files/proof-ru-zh-tw/scratch/`。
- freeze.py baseline：核心 build 副本 8/8 逐字節復現；本版 build 副本亦 8/8 復現出貨 SVG；校對始末核心＋本版共 16 個 SVG 雜湊兩次自測全等（核心未動）。
- freeze diff 雙軌：純非漢字串增減全冊僅 P8 分隔符 −8（«— СТРАНИЦА N —»→列定式）；逐頁逐串讀畢，新增 CJK 串全為繁體講解/家具，俄語正文（含混合串內俄語部分）逐字節凍結。
- 形狀幾何（rect/line/circle/image/path 含全屬性多重集）8 頁與核心全等。
- p8.py compare：CLEAN（150=150，keydiff 恰 {137, 138}）。註冊表雙 dump（各單進程、改道副本）權威比對：鍵差恰 {137, 138, 150}、題型差 84 = 6 組繁簡系統對、注 115 改 / 35 未變（35 條逐條裁定：純俄語/數字或共形字，成立）、級別 A2 54 · B1 72 · B2 24、逐頁 10/18/18/18/18/18/12/38 全等。手工從俄語正文逐題重推導全部 150 鍵，零分歧（P6 圖表條長實測 17.62–17.65 單位/%，成比例；#150 範文手數 82 詞合）。
- 簡體殘留三軌 = 0：(a) 全庫 zh-cn 減 zh-tw 語料導出 289 字掃描集；(b) 398 個出貨 CJK 碼點普查逐字目檢；(c) 常用簡體專有碼點逐一掃描。U+5939（夹）於 SVG 與 build 代碼均 0。大陸式詞彙 = 0。
- 禁則（標點感知）：本版行尾開括號 = 0（P2 父親節 gloss 終修在版實證）；餘 6 旗與核心同位同形（5 處 «· » 分隔符起行 + 1 處俄語正文 «%» 起行，均凍結/家族式樣，非缺陷）。
- 幾何：occlusion_audit 自檢先行，本版 2 旗與核心同題同位同數值，NEW = 0；兩旗元素墨跡帶與核心卡像素比對 0 差異（P1 «странице.» 帶、P2 條帶），裁定繼承非缺陷。同行墨跡碰撞（真墨盒）雙版 0。
- gloss 逐框點數：P2 [3,3,3] · P3 [3,3] · P4 [4] · P5 [3,2] · P6 [3] 與核心逐框全等，一項不少。P7 金句 8 條逐字回溯原文驗真、頁標籤全對。svglib diff 恰 §4 登記 4 處功能變更 + docstring 1 處。家具逐項合 EN×ZH-TW KIT §3：徽章 (975,574) 22pt BRICK 插入式（README 第 20 條家族裁定，隨 RU×KO 先例）成立；頁腳 8/8、頁碼、P8 頭/帶/分隔 ×8 全合。撇號逐頁 = 核心（P5 «Хиллоуин'26» ×1）。禁用術語於出貨 SVG = 0；operative code 中 bridge = 0（expl() 定義 1 + 調用 20），svglib 首行 docstring «weekly-paper» 為核心庫自有原文（繼承性標識，同 PAPER 先例裁定不計缺陷）。
- 日曆（Europe/Moscow 實查）：10-19 週一 · 10-24 週六 · 10-25 週日 · 10-28 週三 · 10-31 週六 · 11-04 週三，及 10-18 週日（父親節·十月第三個週日）、10-22 週四、10-23 週五、11-01 週日全合；俄國國內生活口徑，零國際政治。卡面肉眼核 P1/P8 全頁 + P2 gloss 區：TC 面無缺字/方框，西里爾正常。
- 最終針腳（校對者實測，與建造者自報全長逐字全合）：印刷 26,360,627 B · sha256 `8655371ebd976adb9be8f94e592be1f4decb7607279b97e21f226a17f7cd9aac`；網頁 3,488,650 B · sha256 `44cb72ba2ec7da86772b25ddc5394429a946a88e252b36c21b8e5782dbfe3b8a`（各 8 頁）。

## §13 D5 重建記錄（2026-11-14）

D5 + §1.1 合并重建（2026-11-14；builder v3 接替 v2，v2 死于 2026-11-14 ~02:55 UTC 第 5 波 restart drain）。本节 supersedes 上述旧印/网 pin 行（以实测发运值为准；KIT 旧 SHA 不可作基线）。

- 装机：`apply_variant.py --patch-core ru --week 2026-w43`（core-ru `_D5_READER = "latin"`，+263/−28）+ 本版 `apply_variant.py --svglib patched/2026-w43-ru-zh-tw/svglib.py --target ru --reader zh-tw --week 2026-w43`（`_D5_READER = "cjk"`，diff +63/−2）；路由单元测试 `test_d5_routing.py` FAILURES: 0；fix2 保留。
- 基线：run TOTAL 150，0 警告；印 PDF 23,152,085 B（MANIFEST +0.001%），网 PDF 2,623,799 B，`pdf_text_diff_ru.py` + TRIM_ARGS → IDENTICAL；修前普查 D5 拉丁 206、西里尔 0。
- 缺陷与修法（只动字号/断行与规则线位置，不动文字）：
- D2 (occlusion TEXTX, P1): `'A2' overlaps 'кино' 7.4×11.2px` — `content12.py:106` 目录标题 20→19pt。
- D3 (occlusion LINEX P2 ×6, 基线同款): `content12.py:235` 规则线 `ey−12`→`ey−8`。
- 门禁（run2）：全套 17 门 ALL-GREEN。run TOTAL 150；head_check 0；d5 census 拉丁/西里尔/弯引号在 CJK 均 0（弯引号总数 0；`noto_sans_elements=414`）；freeze baseline 8/8；freeze diff 新增 CJK 0、新增拉丁 strings 67（run 拆分）；spill 0（177 OBSERVE）；boxtitle 0 DEFECT（58 titles, 734 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS 0 defects（n=392, median 1.015；P8 229→229 行，slack 61.4→61.4px）；文字层 print=web 差 0（34,196 字）；text.md BYTE-IDENTICAL；census_quotes 0 defective；p8 compare CLEAN，keydiff=[137, 138]；刊头标语→日期间距 513.8px PASS。日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-zh-tw/GATES-SUMMARY-run2.txt`。
- 新交付物（实测）：印 PDF `Lucerna-VOL1-ru-zh-tw.pdf` **23,136,062 B**，sha256 `6b14b7cc9b719ed76316bf4ebc3f994dc4ca8b9fc95a1b7f51c813ae56eb0b11`；网 PDF `2026-w43-ru-zh-tw.web.pdf` **2,612,295 B**，sha256 `aba679270b80c8d08accce682267f6f44362227cd77de4f14f81abe57c2b2ae7`；text.md **58,350 B**，sha256 `fbb0f25518eec8f70df127854fb2bcd6920664925a2fb3101cfc08b00f1446bf`，与 fanout `.text.md.new` BYTE-IDENTICAL。D5 报告：`production/notes/2026-w43/g-ru/scratch-d5-rebuild-ru/D5-REPORT-2026-w43-ru-zh-tw.md`。§12 獨立校對記錄末尾重複引用的舊針腳（印刷 26,360,627 B / 網頁 3,488,650 B）為 D5 前實測值，係歷史記錄，不改。
