# PROOF-NOTE — W47 zh-tw-it（重擴散新版）proof2 全量重校

## 結論：(a) 零缺陷，可定稿

- 對象：`production/2026-w47/2026-w47-zh-tw-it/`（重擴散新版；核心已定稿，re-proof #3 结论 (a)）
- 校對方式：從頭全量重校（SOP §8.4）。未假定 proof1 舊缺陷仍在或已修，逐項實測。
- 工作區（唯一 scratch）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-it1/`；生产目录只读——全程未改生产文件，未 commit/push，未重渲染交付的 web PDF（只比文字层）。重建与重渲染均在 scratch 副本内完成，交付件 SHA 終驗與開工時一致，未變。
- 探針：`git hash-object -w /dev/null` 成功；scratch 真實寫文件成功；`TMPDIR=<scratch>/tmp`，未寫 /tmp。

## 三 SHA 核對（開工 + 終驗一致）

| 件 | 字節 | SHA-256 | 核對 |
|---|---|---|---|
| 印 `Lucerna-VOL4-IT.pdf` | 19,420,437 | `5594005aae1b2ff3b69ae37edf191dc482f2c3773b29a1cdc75c72ce5b485ce9` | ✓ 與任務給定一致 |
| 網 `Lucerna-VOL4-IT-web.pdf` | 2,323,037 | `a0d80c26bdc7c8eb6029af991c4d14e8af966f0e3f6d3a066f74f98bf220d0a5` | ✓ 與任務給定一致 |
| 文 `2026-w47-zh-tw-it.text.md` | 51,685 | `48e04f1540a9b6bcf292f9163af32707ac2ba54bcd91b18a127f45903dc12ba7` | ✓ 與任務給定一致 |

KIT §「Measured totals」/ Re-fan-out 節所載三 SHA、字節數與盤上實測一致。

## 缺陷清單

**無。零缺陷。**

## 觀察（非缺陷，實測裁定，記錄在案）

### O1 — 雙語小檔標題 STRADDLE 2 處（重擴散報告 §7 未決項 2，本輪實測裁定：記觀察）

按任務 STRADDLE 規則實測三項（字形被裁 / 墨跡重叠 / 回歸），三者皆無，故記觀察、非缺陷：

| # | 標題 | 墨右緣（交付 PDF 200dpi 渲染像素實測） | 盒右緣 | 超出 | 字形被裁？ | 墨跡重叠？ | 回歸？ |
|---|---|---|---|---|---|---|---|
| 1 | P1「本週一詞　Parola della settimana」 | 1862.4 | 1862.0 | +0.4px（PIL 真墨 +0.8px；CairoSVG 卡片 +4.0px） | 否：字形完整，墨止於 1862.4，距頁緣 1950 尚有 87.6px | 否：CREAM-COVER 0、occlusion 0；x=1900、y=1780 處像素為紙色 (251,250,246) | 否：舊版同 2 處、同座標 |
| 2 | P2「耶誕城小檔　Scheda Christmasland」 | 1884.5（卡片 1885.0） | 1862.0 | +22.5px（PIL 真墨 +24.5px） | 否：末字 "d" 完整成形於空白紙面，距頁緣 65.5px；見 `gates/crop-p2-straddle-marked.png`（紅線=盒緣、藍線=頁緣） | 否：CREAM-COVER 0、occlusion 0；x=1900、y=1464 處像素為紙色 (251,250,246) | 否：舊版同 2 處、同座標；重擴散引入 0 處 |

- 盒為無邊框奶油盒：occlusion 0 flags 對此類橫向溢出是盲的，故未以其為據；裁決以交付 PDF 渲染像素 + PIL 真墨 + advance 交叉核對為準，證據在 `gates/crop-p1-straddle-marked.png`、`gates/crop-p2-straddle-marked.png`、`gates/creambox-pil.log`。
- 備註：P1 的 +0.4px 為亞像素，不可見；P2 的 +22.5px 肉眼可見標題伸出盒外，但字形完整、無任何碰撞，屬版式既有屬性（舊版 proof1 未列出是因當時未跑 PIL STRADDLE 掃描，不是新引入）。

### O2 — freeze diff `--strict-cjk` RC=1，僅因家具「意大利語講解」（裁定：非缺陷）

- `freeze.py diff --strict-cjk` 報 `STRICT-CJK FAIL`，但新增 CJK 合計恰 27 字 = 「意大利」×9（`freeze-diff.json` 的 `cjk_added_total`：意 9、大 9、利 9）。
- 來源逐處核實：每頁頁腳 `Lucerna　繁體中文週報 VOL.4　繁體中文正文　意大利語講解` ×8 + P1 badge 行 ×1；核心對應位置為「英語講解」，屬讀者語家具替換，非新增目標語正文。
- 其餘所有 added string 均為意大利語講解層（對應 removed 的英語講解層）；removed 的中文串逐頁核對，CJK 語段均在新版以意大利語對譯或同字重現，唯一表面「缺失」`拿下總冠軍，叫封王。`（P1）實為 P1 第 6 題填空：SVG 中為 `拿下總冠軍，叫` + 空格 `___` + `。`（`p1-front.svg` y=2140.5 三節點），答案「封王」在 P8 key 5——非缺文。
- 故 freeze diff 的 CJK 增量全部由家具解釋，diff 本身（字符串多重集）無未解釋增減。

### O3 — 已知非缺陷（KIT 已載，與本輪實測一致；不重列為缺陷）

- P4「棒球詞卡　Parole del baseball」頭折兩行（欄內折行，無溢出警告、無重叠）——目視確認。
- P5 首篇末行跨欄流至第 1 欄頂（常規報紙流，與核心一致）——目視確認。
- P8 題幹 10.35pt（核心裁定）；keys 9.75pt，恰 SOP §1.1 下限。

## 全量校對實測（SOP §8.1–8.3）

### §8.1 全量精讀（交付印 PDF 的 -layout 提取文本 898 行，P1–P8 通讀 + SVG 意大利語串全檢）

- 意大利語講解層：922 個含拉丁字母文本節點（764 個純意大利語節點，395 個去重）全部讀過。拼寫、重音、性數配合、變位、標點均無誤；抽查例句：P1「La parata scudetto dei Wei Chuan Dragons è fissata per questa domenica, 22 nov., alle 14:00, dal Tianmu Baseball Stadium al Taipei Dome」；P3「La 63ª edizione dei Golden Horse segue domenica 22 nov. al Taipei Music Center — red carpet alle 17:00, cerimonia alle 18:30, condotta da Will Or (Ko Wai-lam)」；P6「Domenica 22 nov. è la giornata più intensa dell'anno: la parata scudetto alle 14:00, il red carpet dei Golden Horse alle 17:00, la cerimonia alle 18:30, l'ultima parata notturna alle 19:00 — e il festival dell'acciaio chiude alle 20:00, proprio il giorno di Xiaoxue」；P7「Trucco per ricordare: impara prima 入圍, poi 星光大道 (il red carpet alle 17:00, prima della cerimonia), poi la cerimonia (頒獎) alle 18:30」——與核心 fix4/fix5 內容一致。
- 註釋詞逐項對照正文：P7 三欄詞（遊行/封王/夜間/終點；入圍/頒獎/星光大道/鋼雕/保險箱；小雪/節氣/燈秀/市集）全部真實出現在正文；P8 150 條 key note 的詞頭全部出現在正文。
- D1「本週日」：印/網文字層「本週日」11 處、「下週日」0 處；意大利語各處均為「questa domenica」（P1 note「fissata per questa domenica, 22 nov.」；P2 note「Questa domenica, 22 nov., è Xiaoxue」）。英文源 key「next Sunday」未改是核心範圍事項，本版無任何 "next Sunday"/"Next Sunday"/"finish line" 殘留（leak 掃描 deny 命中 0；text.md grep 0）。
- 標題數實測（「56 titles」為幻數，本版無此數）：奶油盒標題共 **36** 個（P1 5、P2 6、P3 7、P4 4、P5 8、P6 3、P7 3、P8 0），boxtitle 超框 0，最小標題右餘 13.8px。另版頭 8 個（P2–P8，第 1 版為刊頭行）。

### §8.2 答案逐題復核（150/150）

- p8.py compare vs 核心：**CLEAN**（missing=[]、extra=[]、keydiff=[]，`gates/it-proof2/p8-compare.json`）；extract noted set 150/150。
- 獨立重算抽驗（題面↔答案↔正文/圖表）：41 題 11/6–11/22 含首尾 17 天 ✓；42 題 17:00→18:30 = 1.5 小時 ✓；59 題 5×10=50 ✓；60 題 7×10=70、缺 30 ✓；77 題 14+31+3=48 天 ✓；78 題 11/17–11/22 含首尾 6 天 ✓；84/99/128 題 14:00→19:00 = 5 小時 ✓；85 題 1.5 小時 ✓；23 題 1200+800=2000 ✓；24 題 2000−1200=800 ✓； error-clinic 第三條「17:30 到 23:00 一共 12 場」✓（17:30、18:00、…、23:00 共 12 場）；F 寫作範文 142 字，在 120–180 帶內 ✓（run.py：MODEL chars: 142）。
- 編號連續性：keys 1–150 連續（text.md + p8 extract 雙重驗證）；分頁歸屬與 KIT 一致（P1 1–10、P2 11–28、P3 29–46、P4 47–64、P5 65–82、P6 83–100、P7 101–112、P8 113–150）。
- 日期/星期全驗（`date -d`，America/Toronto）：11/16 週一、11/17 週二、11/19 週四、11/21 週六、11/22 週日、11/13 週五、12/27 週日、12/4 週五、12/6 週日；P2 日曆「週一 11/16、週二 11/17、週四 11/19、週六 11/21、本週日 11/22」全部對上；「小雪倒數 6 天」（11/16→11/22）✓；「11月22日是星期日，也是小雪」✓；新北耶誕城 11/13→12/27 含首尾 45 天 ✓（18+27）；迪士尼 11/17→1/3 含首尾 48 天 ✓（14+31+3）；金馬影展 11/6→11/22 含首尾 17 天 ✓。
- 事實抽驗：587 部報名、11 項入圍最多（《狂忘警探》）、10 月 1 日公布、63 屆、柯煒林首主持、《月球之旅》1902 梅里愛、鋼雕 10/23–11/22、267 場館、U 幣 5→10、滿 100 換悠遊卡、寶可夢 11/11、爵士 13–15/17–22/24（Diana Krall 13 日、Stacey Kent 17 日、Kenny G 24 日收尾）——均與正文、P8 答案一致；意大利語 note 無新增核心報以外事實。

### §8.3 八版逐版看圖（生產 cards/ 全 8 張 + P1/P2 STRADDLE 裁切 + P2 事實框裁切）

- P1–P8 全部目視：無溢出、無重叠、無頁腳碰撞、圖片/署名位置確認；P6 時間軸標籤「頒獎典禮」墨右緣 990.8 與「夜間遊行」墨左緣 991.4，縫 0.6px（與核心先例一致的發絲縫，無重叠）；P7 teaser 止於 2577.3，距頁腳規則 2596 餘 18.7px；P8 keys 止於 2344，距底 2560 餘 216px。
- 誤讀糾正記錄：目視初看 P2 事實框疑似「泡腳0到15分鐘」缺「1」；像素實測推翻——卡片 P2 在 y=778–798、x=1790–1850 帶內墨跡含「1」（旗形襯線豎筆，x 1785–1809）+「0」（x 1814–1824），與核心卡片同帶像素一致；SVG 源码亦為「泡腳」+「10」+「到15」「分鐘」四節點。非缺陷。

## 機械門禁（詳見 GATE-LOG.md）

run.py RC=0（150 題、0 FLOW OVERFLOW、0 警告）｜SVG 重建 8/8 字節一致｜重渲印 PDF 與交付逐字節相同（SHA `5594005a…`）｜freeze baseline 8/8｜freeze diff 僅家具 CJK（見 O2）｜occlusion 0 flags（selftest 6 類全觸發）｜奶油盒 PIL 真墨掃 STRADDLE 2（見 O1）、CREAM-COVER 0｜canonical creambox 36 盒、負清除 0、P7 工具盒 +40.5/+12.5/+14.0｜boxtitle 36 盒、超框 0｜spill 0（EDGE 0 + 全部 flow 在底線內）｜孤兒掃：逐版目視 + flow 終值審核，無孤兒頭/行（P5 跨欄為 KIT 已載常規流）｜p8 extract 150/150、compare CLEAN（keydiff=[]）｜P8 最小字號 9.75pt（印/網一致）｜§1.1 全驗（紙 #fbfaf6 ×8 頁、鵝黃 #f6e08e 為 SOP 允許色、金/紅褐 0、字體 Newsreader/Noto Serif CJK TC/Noto Sans CJK TC/UnifrakturMaguntia、✗ 用 DejaVu Sans fallback 與核心同制、VOL.4×10/VOL.5×1（下期預告）/VOL.3×2（讀者園地延期披露，歷史引用）｜日期星期全驗（見上）｜KIT §1 三 SHA 與盤上一致。

## 交付文件

- 本文件：`scratch-proof2-zh-tw-it1/PROOF-NOTE.md`
- `scratch-proof2-zh-tw-it1/GATE-LOG.md`（逐門結果 + 日誌索引）
- 門證據：`scratch-proof2-zh-tw-it1/gates/`（`it-proof2/gates.json`、各門日誌、交付 PDF 渲染裁切、STRADDLE 標記圖）
- 重建副本：`scratch-proof2-zh-tw-it1/build/it/`（scratch 內重跑 run.py/render.py 的完整副本；生產目錄未動）
