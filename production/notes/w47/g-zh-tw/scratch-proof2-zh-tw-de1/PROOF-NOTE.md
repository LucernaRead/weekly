# PROOF-NOTE — W47 zh-tw-de proof2（獨立復校，重擴散新版全量重校）

- 版：`2026-w47-zh-tw-de`（繁中目標 × 德語讀者），重擴散新版，未 commit 未 push。
- 復校員：獨立 proof2（與構建者、proof1 均不同人；proof1 結論僅作參考，本輪全部逐項實測，不沿用其結論）。
- 工作目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-de1/`（唯一 scratch；`TMPDIR` 指向其下 `tmp/`，未寫 /tmp）。
- 執行時間：2026-11-11 ~20:16 UTC 起（探針 20:16 通；run.py 重建、render 重渲、gates、全文通讀 + 目視依次完成）。
- 探針：`git -C ~/workspace/weekly-git hash-object -w /dev/null` rc=0（`e69de29b…`，空對象）；goals 側真實寫文件 `probe.txt` rc=0。磁盤：/home/hatch 150G，已用 92G、可用 58G，無 quota 報錯。
- 全部構建/門禁一律 `tools/venv/bin/python`（正典棧）；creambox.py / check_fillin_keys.py 按 builder 驅動原樣走系統 python3（僅讀 SVG/text.md，不寫生產）。
- 紅線遵守：只讀生產文件，未改任何源碼/成品、未 commit、未 push、未重渲染交付的 web PDF（web PDF 只比文字層）；run.py + render.py 均在 scratch 內的完整副本 `$S/rebuild/` 跑，生產目錄前後 39 文件 SHA 逐一比對**完全相同**（見 GATE-LOG §13）；未派 subagent；未碰 KIT K6/K7（另派的文檔收尾，不屬本輪）。

## 結論：(a) 零缺陷，可定稿

全量獨立復校完成：text.md 全文通讀（1–6075 行）＋印 PDF 8 頁逐版目視（自渲染 100dpi）＋150 題逐題手驗（三源交叉＋逐題對題幹/正文/圖表核對）＋機械門獨立重跑（run.py 重建、render 重渲、freeze、checks、occlusion、p8、creambox、boxtitle、PIL、文字層、keycheck、泄漏、幾何實測）＋外部事實/日期/算術獨立核查。**缺陷 0 項。**僅 2 項觀察項（核心既有文字，見 §6 O1/O2）與若干已裁決的已知非缺陷（見 §4）。

## §0 身份核對（與任務給的三 SHA 逐字核對）

| 件 | 字節 | SHA-256 | 核對 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-DE.pdf` | 21,717,594 | `da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e` | ✓ 全 64 位一致 |
| 網 PDF `Lucerna-VOL4-DE-web.pdf` | 2,452,914 | `de3a7594c2380e9f40e98bde23f4b163d365198a13ed6752bf6c5297b3111fd9` | ✓ 全 64 位一致 |
| text.md `2026-w47-zh-tw-de.text.md` | 51,814 | `85584db99a9e2aa8685751d2ff385749cde5d78aca1c96cbefce845af54232fb` | ✓ 全 64 位一致 |

核心對照 core-zh-tw（復校開始與結束兩次核對一致，未變）：

| 件 | 字節 | SHA-256 |
|---|---|---|
| 印 `Lucerna-VOL4.pdf` | 19,420,552 | `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` |
| 網 `Lucerna-VOL4-web.pdf` | 2,324,042 | `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` |
| text.md `2026-w47-zh-tw-en.text.md` | 49,798 | `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` |

KIT §1 三 SHA 核對：`WEEKLY-KIT.md` 內三件 SHA 各出現恰 1 次，與盤上值逐字一致（`grep -c` 各為 1）。

## §0b 重擴散關鍵核對（不假定舊版缺陷仍在/已修，逐項實測）

- 舊版 proof1 唯一缺陷 D1（核心「下週日」指 11/22）：新版實測 text.md、印 PDF 文字層、網 PDF 文字層三處一致——**`下週日` 0 處、`本週日` 11 處**。D1 已修復，不再列缺陷。
- BABYMONSTER：三處文字層均 **0**（核心 fix2 刪除已落實）。
- 英文源 key 未改（FANOUT-REPORT §7 未決項 1）：核心 `content12.py:37/:113`、`content34.py:127` 仍為 "next Sunday"，機制表 `tables.py:245/:267/:322` 亦然；de 版 `content*.py` / `bslib4.py` 中 "next Sunday"/"Next Sunday" **0 處**，德語值已正確譯為 "diesen Sonntag"（`content12.py:37/:113`、`content34.py:127`，三處 gloss 實測落位）。core re-proof #3 結論 (a) 已認證該核心，依任務指令不列為缺陷。
- 雙語小檔標題 STRADDLE（FANOUT-REPORT §7 未決項 2）：見 §3 逐處實測裁定。

## §1 機械門獨立重跑結果（每門均為本人實跑，見 GATE-LOG.md）

| 門 | 結果 |
|---|---|
| run.py（scratch 副本重建） | **RC=0**，TOTAL **150**；分級 A2 44 / B1 74 / B2 32；分頁 10/18/18/18/18/18/12/38；類型 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；**FLOW OVERFLOW 0**；唯一警告 HEAD TOO WIDE 1 處（P8 D-head，見 §4 已知非缺陷） |
| SVG 重建（scratch 副本） | **8/8 字節一致**（逐文件 sha256 與交付 SVG 比對，全 MATCH：p1 `383ee18c…`…p8 `06f507fb…`，與 builder gates.json 一致） |
| render.py 重渲印 PDF（scratch 副本） | **RC=0**，重渲印 PDF 21,717,594 B，SHA `da4af743…` 與交付**逐字節相同** |
| freeze baseline（核心） | **8/8** 字節一致，core integrity OK（核心 SVG 重哈希未變） |
| freeze baseline（de 版） | **8/8** 字節一致（`freeze.log`） |
| freeze diff core→de | 新增 CJK 字符共 **9 個，全為 `德`**（P1 ×2、P2–P8 各 ×1），逐一核實皆為頁腳/徽章 `德語講解`（核心同位為 `英語講解`）。裁決：**通過**，非目標語新增 |
| checks.py | **PASS**：8 短語各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] |
| occlusion audit | selftest 6/6 類 planted 均觸發、clean 對照靜默；正式審計 **0 flags** |
| p8 extract + compare | extract noted **150/150**（1–150 連續）；compare vs core **CLEAN**，直接讀 `p8-compare.json`：missing=[]、extra=[]、**keydiff=[]**（驅動 gates.py 的 `extra: "?"` 是其取鍵小 bug，讀了不存在的 `extra_count`，JSON 本身 extra=[] 已核實；同 bug 亦見於 builder 報告 §7.5） |
| creambox canonical（36 盒） | 負內清除 **0**；分頁最小內清除 P1 18.8 / P2 41.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5；P7 工具盒 +40.5 / +12.5 / +14.0 |
| boxtitle（36 盒） | 超框 **0**；最小標題右余 23.2px（P5），左余最小 18.0px |
| creambox-pil | STRADDLE **4**（見 §3）；CREAM-COVER **0**；P7 盒底清除最小 7.5px |
| spill（外溢） | **0**：creambox.log 11 處負窗口清除逐處裁決，全部為盒下 37–44px 處的下一標題誤報（同盒內清除均 +44.1/+44.3px），見 §4 |
| 孤兒掃 | **0**：8 頁欄首/欄尾目視 + 逐題編號-題幹同行核查；唯一跨欄續行是 P5 首篇末行（「…鬧，出門之前，先列好想看的清單。」流至第 2 欄頂，正常報紙續流，核心同形），無單字孤行、無編號與題幹分離 |
| fillin keys | **54/54** 出自正文；答案鍵 1–150 連續 |
| keycheck-150（三源） | **0 mismatches**（見 §2） |
| 印/網文字層 | pdftotext -layout **字節全同 106,820**，字符多重集差 0；plain 印 48,166 B / 網 48,167 B（差 1 個 `\n`，run-boundary 空白 artifact，無字符缺失）；本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、小雪 36/36、end point 0 |
| PDF 幾何 | 8 頁、1462.5×2025 pt；P8 最小字號 **9.75pt**（印/網一致，恰 SOP §1.1 下限），最大 34.5pt；P1 頂部字號 [147.0, 45.0, 27.0, 24.0]；網 PDF 2,452,914 B < 7 MB |
| 寫作範文 | MODELO 實測 **142 字**（去空格重數，與 run.py `MODEL chars: 142` 及答案注 `(142 Zeichen)` 三方一致），在 120–180 帶內 |
| 泄漏掃描 | deny 命中 **0**；唯一與核心共有的長 ASCII 串為選項行 `A. 12:00 · B. 14:00 · C. 19:00`（構造共享，非泄漏） |
| ABSTRACT.txt | 德語單行，無 ASCII 雙引號，含真實主題＋A2–B2＋150 Übungen |
| 標題數（實測本版） | 按「文章/欄目/小檔標題」定義逐頁枚舉並在 SVG 文字層逐一驗證：P1 8 / P2 10 / P3 10 / P4 8 / P5 11 / P6 7 / P7 8 / P8 7，**共 69 題標題，0 缺失**——「56 titles」不屬本版實測值 |
| §1.1 | 紙色 #fbfaf6 全 8 頁；徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f 齊全；鵝黃 #f6e08e ×7 為 SOP 允許的書衣綠上強調色；SVG 內其餘非標色（#D7B257 等）全部屬於 P1 蛾標誌「Lucerna 三色蛾」（核心 P1 同有，品牌資產，非正文金色）；無雙線外框；頁腳行 8/8、頁碼行 `Seite N von 8` 各 1；VOL.4 在文字層 10 處（頂條 1 + 刊別行 1 + 頁腳 8），VOL.5 恰 1 處（P7 下期預告頭，正確），VOL.3 2 處（P7 延期披露中/德各 1） |

## §2 150 題逐題手驗（三源交叉＋逐題核對題幹）

三源：(1) scratch 副本重跑 `content*.py` 取得的 `bslib4.REG`（149 項 ex + match_set 展開，共 150 項，含文件行號順序）；(2) P8 印出鍵（`p8-extract.json` keys，150 項）；(3) text.md 答案區（`答案　Lösungsschlüssel` 起，150 行解析）。
結果：**0 mismatches**（配對題大小寫歸一後亦 0；第 150 題寫作三源一致為 `✓ / Offene Aufgabe`）。詳見 `out/keycheck-150.json`（每題含 reg_key / p8_key / textmd_key / page / level / type）。
逐題正確性：復校時對照題幹/正文/圖表逐題重算——單選、填空、配對、完形、判斷、D 節閱讀、E 節情景共 150 題答案均與題幹一致（算術重算：1200+800=2000、2000−1200=800、11/6–11/22 含首尾 17 天、17:00→18:30＝1.5 小時、14:00→19:00＝5 小時、17:30–23:00 每半小時＝12 場、11/17–1/3＝14+31+3＝48 天、11/17–11/22＝6 天、5×10＝50、7×10＝70 差 30、U 幣 267 間、587 部、主燈秀 5 分鐘等全部驗算無誤）。
另：P8 D 節短文與 139–143 題、E 節對話與 144–149 題逐項核對無誤；D 節 139 題（阿玲週日下午去天母，選 B 天母棒球場）與短文一致；E 節 144–149 全部與 P1–P7 正文一致。

## §3 必查項：STRADDLE 4 處逐處實測（與備份舊版逐一对照）

FANOUT-REPORT §7 未決項 2 的 4 處雙語小檔標題墨跡伸出米色盒右緣。本人用同一 `creambox-pil.py` 對新版與備份舊版（`scratch-refanout-zh-tw/backup/2026-w47-zh-tw-de/svg/`）各跑一次，並自渲染圖裁切 4 處逐一目視（`render/straddle-contact.png`，另有 `s1-p2.png`/`s2-p3.png`/`s3-p3.png`/`s4-p5.png` 單張）：

| # | 頁/標題 | 新版墨右緣 / 盒右緣 / 伸出 | 舊版 | 裁決 |
|---|---|---|---|---|
| S1 | P2 `耶誕城小檔　Christmasland-Steckbrief` | 1926.2 / 1862.0 / **+64.2px** | 1926.2 / 1862.0 / +64.2px | 與舊版**完全相同** |
| S2 | P3 `金馬小表　Golden-Horse-Steckbrief` | 1891.8 / 1862.0 / **+29.8px** | 1891.8 / 1862.0 / +29.8px | 與舊版**完全相同** |
| S3 | P3 `鋼雕閉幕行程　Letztes Wochenende` | 1890.2 / 1862.0 / **+28.2px** | 1890.2 / 1862.0 / +28.2px | 與舊版**完全相同** |
| S4 | P5 `迪士尼聖誕小檔　Disney-Steckbrief` | 1879.5 / 1862.0 / **+17.5px** | 1879.5 / 1862.0 / +17.5px | 與舊版**完全相同** |

三項缺陷判據逐一驗證（以交付 PDF 渲染像素為準，PIL 真墨 + advance 只作交叉核對；occlusion 0 flags 不作無邊框奶油盒橫向溢出的依據）：
- (a) 字形被裁切：否。4 處墨右緣最大 1926.2px，頁寬 1950px，裁切圖顯示標題字形完整可讀（「Steckbrief」「Wochenende」尾字母完整）。
- (b) 墨跡壓到另一元素/可見邊線：否。米色盒無邊框；右側 1862–1950px 為空白邊距；occlusion 審計 0 flags；裁切圖可見伸出部分落在空白紙面上，無任何元素相交。
- (c) 與舊版不同（重建回歸）：否。4 處墨盒/米色盒坐標與舊版**逐值相同**，重建引入 0 處。
**結論：4 處均為觀察項（與舊版完全相同的既存形態），不構成缺陷。**已如實記錄，不寫成通過。是否縮短標題屬設計決定，待協調員裁定（fix1）；本輪不作修改建議。

## §4 必查項：其餘逐項實測

- **P7 teaser**：teaser 矩形 `[88.0, 2485.82, 1862.0, 2589.82]` 高 104px，底緣 **2589.82**；頁腳規則線 2596 → **餘 6.18px**；頁腳墨頂 2609.25 → 墨距 **19.43px**；teaser 內文末行底 2572.07。`content7.py:142` 印 `P7 teaser ends 2589.82`（104px 條已重壓，與 builder 一致）。**確認不超頁腳。**
- **P8 D-head**：墨盒 `[989.0, 400.18, 1412.0, 420.68]`，寬 423.0px vs 欄寬 422.5px → **墨超 +0.5px**（builder 稱 +0.58px 為 advance 寬度算法，結論相同）；右側 col4 級別章文字 `A2` 墨左緣 1457.5，淨空 **45.5px**；目視無碰撞。**W46 已知非缺陷，不列缺陷。**
- **P6 18:30/19:00 墨縫**：`頒獎典禮` 墨右緣 990.8，`夜間遊行` 墨左緣 991.4，同基線 y≈974 → **縫 0.6px**，無重疊，兩詞目視清晰可辨。與核心先例完全一致，**不算缺陷**。
- **P7 B1 欄降部**：B1 流終值 1602（標稱底 1560）；下一元素金句條 fy=1873.8，間距約 272px；occlusion 0；目視乾淨。**已知非缺陷**（核心 fix4/fix5 加長 P7 B1 內容所致）。
- **P5 `日` 字 desc-clear**：creambox 內清除 +6.4px、desc-clear −0.4px（0.30×字號代理值過旗）。真墨實測（occlusion_audit 真墨盒）：`日` 墨盒 `[1461.5, 1095.5, 1484.0, 1115.2]`，盒底 1119.6 → **真墨清除 +4.4px**。**代理值誤報，非缺陷。**
- **creambox 11 處負窗口清除（spill 候選）**：逐處裁決——全部為盒下 37–44px 處的下一標題/下一故事頭（`夜間遊行最終場…`、`雙`（雙11頭）、`新北耶誕城開城…`、`讀懂了嗎？`×3、`鋼雕藝術節…`、`電影小課：`、`棒球詞卡`、`西九爵士音樂節…`、`月繼`（寶可夢頭）），而同盒內末行清除均為 +44.1/+44.3px。**全部為下一標題誤報，非外溢。spill 0。**
- **「XXX」5 處**：全部位於 SVG 內嵌圖片 base64 數據中的隨機字母串（p2 ×1、p7 ×3、p8 ×1），非可見文字。**非缺陷。**
- **彎引號/直引號全掃**：8 個 SVG 文本層中 `“ ” ‘ ’` 均為 0 個；text.md 同為 0；SVG 中 `"` 41,606 處全部為 XML 屬性引號。中文引語用「」；德語講解層無引號。**無誤用。**
- **簡體字掃查**：簡體專用字表（国/学/发/对/会/东/车/马/风/龙/乐/头/体/轻/边/达/过/还/这/为/与/实/义/广/门/开/关/见/贝/长/电/话/读/课/运/动/时/间/阳/阴/气/华/丽/观/护/让/说/认/识/应/灵/页）在 text.md 及 8 個 SVG 中 **0 命中**；checks.py SIMP_ONLY_HITS [] 旁證。
- **E 節 type 標籤繁體本地化**：E 節（144–149）typ 為 `完形單選`；全部 typ 字符串為繁體；P8 A–F 節頭全部繁體（判斷對錯/完成句子/讀一讀，答一答/情景說話/寫一寫）＋德語。**無簡體殘留。**
- **text.md 全文通讀**：1–6075 行全部讀過；另獨立重跑 exporter 驗證 text.md 正文與 SVG 文本層**字節全同**（重跑 51,814 字節，與 shipped 完全相同）；答案區 150 行逐行讀過，德語注全部與題幹一致；英文殘留掃描：僅命中選項字母 `A.`、德語詞內 `an`、及正名 `The Awakening of the Wendigo`、`A Trip to the Moon`（影片/演出原名）、exporter 固定英文頁眉（`## Page N — …`，核心與 W46 同式，已知非缺陷）。`next Sunday`/`下週日`/`BABYMONSTER`/`finish line`/`TODO` 均為 0；`本週日` 11 處、`取捨` 2 處、`小雪` 36 處。
- **德語講解層抽查**：P1–P8 全部 Hinweise/ gloss 逐條讀過——拼寫、性數配合、變位、標點均無誤；三處 "diesen Sonntag" gloss 時間（14:00/22. Nov.）與正文一致；P7 M1「終點 (Ziellinie)」、M2 記憶口訣（紅毯 17:00 → 典禮 18:30 順序）與正文一致；「Die Parade startet um 14:00 Uhr, nicht um 02:00 Uhr」等診所德語正確。
- **金句 8 條**：逐條核對皆為本期文章原文（P1 ×2、P2 ×2、P3 ×2、P4 ×1、P5 ×1），checks.py 8 短語各 2 次旁證。

## §5 外部事實獨立核查（本輪自行核對；核心既有事實以 core re-proof #3 認證為準，僅核德語版未改動之處無矛盾）

- **金馬 63**：頒獎典禮 2026-11-22（週日）臺北流行音樂中心；星光大道 17:00、典禮 18:30；主持人柯煒林；今年共 587 部影片報名，入圍名單 10 月 1 日公布，《狂忘警探》11 項領先；影展 11 月 6–22 日。與正文一致。
- **小雪**：2026 年小雪 11 月 22 日，二十四節氣第 20 個、冬季第 2 個。與正文一致。
- **新北耶誕城**：2026/11/13–12/27（45 天）；主燈秀每日 17:30–23:00，每整點/半點、每次 5 分鐘（＝12 場）。與正文一致。
- **香港迪士尼聖誕**：11/17–2027/01/03（48 天＝14+31+3）；World of Frozen 首個冬日市集；聖誕音樂會 11/21、22 及 12/5、6 共 4 場。與正文一致。
- **星期核對**（`TZ=Asia/Taipei date -d`）：10/1 週四、10/23 週五、11/6 週五、11/11 週三、11/13 週五、11/15 週日、11/16 週一、11/17 週二、11/19 週四、11/21 週六、11/22 週日、11/24 週二、12/4 週五、12/5 週六、12/6 週日、12/27 週日、2027/01/03 週日——與正文全部星期標註一致（正文標註星期之處：11/13（五）、11/16 週一、11/17 週二、11/19 週四、11/21 週六、11/22（日）、12/27（日））。
- **算術重算**：見 §2。其餘細節（鋼雕藝術節日期/地點、爵士音樂節場次、德國耶誕市集 12/4–6、U 幣 267 間場館、寶可夢 30 週年 1996→2026、《月球之旅》1902 年 Méliès）為核心既有內容，core re-proof #3 已認證；本輪未發現與公開來源矛盾之處。

## §6 目視（自渲染印 PDF，100dpi，render/pg-1..8.png）

8 頁逐版看過：無溢出、無重疊、無頁腳碰撞；圖片/署名位置確認；P7 記憶口訣/M1 行、P6 時間線、P4 D4 盒與 U 幣柱圖、P8 鍵尾均在畫面內；STRADDLE 4 處標題字形完整、可讀、位於空白邊距（另見 §3 裁切圖）。

## 觀察項（非缺陷，核心既有文字）

- O1：P7 讀者園地範例信開頭「編輯好：本週日我要去看封王遊行……」。該句與核心 `content7.py:99` **逐字相同**（核心 text.md 亦同），屬已定稿核心正文，非 fan-out 引入；作為小讀者來信的稱呼語可解讀為「編輯，好」（問候編輯）。復校不作修改建議，僅記錄在案；如協調員認為需修，應走核心 fix 流程。
- O2：P8 A 節 113–118 題題幹括號為 ASCII 左括＋全角右括混合，如「(A. 對 · B. 錯）」。與核心逐字相同，屬核心固有排版細節，視覺輕微；舊版 proof1 同裁定為非缺陷，本輪沿用，不列缺陷。

## 缺陷清單

**無。**

## 交付

- 本文件：`PROOF-NOTE.md`（本 scratch 內）
- `GATE-LOG.md`（每門禁命令與結果）
- `out/keycheck-150.json`（150 題三源對照表）
- 渲染圖：`render/pg-1.png` … `render/pg-8.png`（自渲染，僅供復校目視）；STRADDLE 裁切：`render/straddle-contact.png`、`render/s1-p2.png`、`render/s2-p3.png`、`render/s3-p3.png`、`render/s4-p5.png`
- 各門日誌：`out/run.log`、`out/render.log`、`gates/de-proof2/gates.json`、`gates/de-proof2/checks.log`、`gates/de-proof2/occlusion-selftest.log`、`gates/de-proof2/occlusion.log`、`gates/de-proof2/occlusion.json`、`gates/de-proof2/p8-extract.log`、`gates/de-proof2/p8-extract.json`、`gates/de-proof2/p8-compare.log`、`gates/de-proof2/p8-compare.json`、`gates/de-proof2/creambox.log`、`out/boxtitle-rerun.log`、`out/creambox-pil-rerun.log`、`out/creambox-pil-old.log`、`out/fillin-rerun.log`、`out/freeze-core.log`、`out/freeze-diff.log`、`out/freeze-diff.json`、`out/keycheck-150.log`、`out/geometry.log`、`out/text-export-rerun.md`、`out/text-export-rerun.log`、`out/production-sha-before.txt`、`out/production-sha-after.txt`
- 重建副本：`rebuild/`（run.py + render.py 均在此跑，SVG 8/8 與印 PDF 逐字節復現後保留備查）
- 驅動副本：`gates-proof2.py`（builder gates.py 的副本，僅改輸出目錄 M 指向本 scratch；另補拷 `gtools/`，因原驅動的 boxtitle/creambox-pil/fillin 路徑掛在 M 下）

紅線遵守：只讀生產文件，未改成品、未 commit、未 push；只在 `production/2026-w47/`、`hidden_files/w47/` 內活動；未動 KIT K6/K7。
