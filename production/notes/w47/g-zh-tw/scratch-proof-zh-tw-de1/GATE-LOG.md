# GATE-LOG — W47 zh-tw-de proof1（重 fan-out 新版，機械門獨立重跑記錄）

復校對象：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-de/`
核心對照：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`（正典棧；絕不用系統 python3）
日誌目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-de1/`
執行時間：2026-11-11 ~12:00–13:20 UTC
舊版 proof1 文件已備份為 `PROOF-NOTE-old-edition-2026-11-11-0838.md` / `GATE-LOG-old-edition-2026-11-11-0839.md`。

## 0. 探針與身份核對

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`：rc=0，`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`
- goals 側真實寫文件 `probe-proof-zh-tw-de1.txt`：rc=0（內容 probe-ok）
- TMPDIR：`$S/tmp`（goals 側 scratch 下），未寫 /tmp
- 身份核對（sha256sum + stat）：
  - 印 `Lucerna-VOL4-DE.pdf` 21,717,594 B `da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e` ✓
  - 網 `Lucerna-VOL4-DE-web.pdf` 2,452,914 B `de3a7594c2380e9f40e98bde23f4b163d365198a13ed6752bf6c5297b3111fd9` ✓
  - text.md 51,814 B `85584db99a9e2aa8685751d2ff385749cde5d78aca1c96cbefce845af54232fb` ✓
  - 核心三件：印 19,420,552 B `5ec35fe2…`、網 2,324,042 B `1c0799ac…`、text.md 49,798 B `09e083e1…` ✓（與 FANOUT-REPORT §0 一致，重建前後未變）

## 1. freeze baseline（第一步，8/8 才繼續）

- 核心：`tools/venv/bin/python tools/freeze.py baseline --build . --core-svg svg --out $S/freeze-base`（cwd=core-zh-tw）→ **8/8 SVGs byte-identical**，core integrity OK（`freeze-baseline.log`）
- de 版：同命令（cwd=2026-w47-zh-tw-de，--out $S/freeze-base-ed）→ **8/8**（`freeze-baseline-ed.log`）；SVG SHA 與 builder gates.json 逐一一致（p1 `383ee18c…` … p8 `06f507fb…`）
- `freeze.py diff --core-svg core-zh-tw/svg --edition-svg <ed>/svg --json freeze-diff.json`（`freeze-diff.log`）：rc=0；每頁 +25–192 / −25–185 strings；**TOTAL added CJK characters: 9**，全部為 `德`（P1 ×2、P2–P8 各 ×1）；逐一核實皆為頁腳/徽章 `德語講解`（核心同位為 `英語講解`）。裁決：通過，非目標語新增。

## 2. checks.py（checks.log）— rc=0 PASS

- `cd <ed> && tools/venv/bin/python checks.py`
- 8 短語各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]；CHECKS PASS

## 3. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest <ed>/svg` rc=0：planted 6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean 對照靜默
- `<ed>/svg --json occlusion.json` rc=0：**0 flags**

## 4. p8.py（p8-extract.log / p8-compare.log / p8-extract.json / p8-compare.json）

- `extract --p8 <ed>/svg/p8-test.svg --total 150 --json p8-extract.json` rc=0：noted set = **150/150**
- `compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 <ed>/svg/p8-test.svg --total 150 --json p8-compare.json` rc=0：**CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]

## 5. creambox canonical（creambox.log）— 36 盒

- `tools/venv/bin/python hidden_files/w47/tools/creambox.py p1-front.svg … p8-test.svg`（cwd=<ed>/svg）rc=0
- 負內清除 **0**；分頁最小內清除：P1 18.8 / P2 41.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5
- P7 工具盒：+40.5（`Stunde: 12-mal, 17:30–23:00 Uhr.`）/ +12.5（`mehr Y. Bilde einen eigenen Satz damit.`）/ +14.0（`Einladung bleibt offen.`）
- 負窗口清除 11 處：逐處裁決皆為盒下 37–44px 的下一標題（見 PROOF-NOTE §4）；盒內末行均 +44.1/+44.3px
- P5 `日` 盒：內清除 +6.4、desc-clear −0.4；真墨實測見 §8（墨清除 +4.4px，代理值誤報）

## 6. boxtitle / creambox-pil / fillin（boxtitle.log / creambox-pil.log / fillin-check.log）

- `gtools/boxtitle.py <ed>/svg $S` rc=0：36 盒，超框 **0**；最小標題右余 23.2px（P5），左余最小 18.0px；分頁：P1 35.2 / P2 28.2 / P3 65.8 / P4 33.0 / P5 23.2 / P6 44.0 / P7 150.0
- `gtools/creambox-pil.py <ed>/svg $S` rc=0：STRADDLE **4**（P2 +64.2 / P3 +29.8 / P3 +28.2 / P5 +17.5，見 PROOF-NOTE §3）；CREAM-COVER **0**；P7 盒底清除最小 7.5px
- `gtools/creambox-pil.py <backup>/svg $S`（舊版對照，`creambox-pil-old.log`）rc=0：STRADDLE 同為 4 處，墨盒/米色盒坐標**字節級相同**；P7 盒清除同值
- `gtools/check_fillin_keys.py <ed>/2026-w47-zh-tw-de.text.md <ed>` rc=0：**54/54** 在正文，缺失 []

## 7. 印/網文字層（print.txt / web.txt / print-plain.txt / web-plain.txt）

- `pdftotext -layout` 印/網：皆 **106,820 B，字節全同**；字符多重集差 0
- `pdftotext` plain：印 48,166 B / 網 48,167 B；多重集差僅 web 多 1 個 `\n`（run-boundary artifact）
- 計數（印/網一致）：本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、小雪 36/36、end point 0、next Sunday 0、Next Sunday 0

## 8. 幾何實測（p8-font.log / p7-teaser-dhead.log / abutting-dhead.log / p5-ri-ink.log）

- PyMuPDF（venv）：雙 PDF 各 8 頁、1462.5×2025 pt；P8 字號 [9.75 … 34.5]，**最小 9.75pt**；P1 頂部 [147.0, 45.0, 27.0, 24.0]
- P7 teaser：矩形 [88.0, 2485.82, 1862.0, 2589.82] 高 104px，底緣 **2589.82**；頁腳規則 2596 → 餘 **6.18px**；頁腳墨頂 2609.25 → 墨距 19.43px；內文末行底 2572.07
- P8 D-head：墨盒 [989.0, 400.18, 1412.0, 420.68]（`D　讀一讀，答一答　Lesen und antworten`，font-size 21），寬 423.0 vs 欄寬 422.5 → **墨超 +0.5px**；右側 col4 級別章 [1439.5, 397.4, 1499.5, 427.4]，淨空 **27.5px**（W46 已知非缺陷）
- P6 abutting：`頒獎典禮` 墨右緣 990.8 / `夜間遊行` 墨左緣 991.4，同基線 y=974 → **縫 0.6px**，無重疊
- P5 `日` 真墨：墨盒 [1461.5, 1095.5, 1484.0, 1115.2]（Noto Serif CJK TC 22.5），盒底 1119.6 → **真墨清除 +4.4px**

## 9. keycheck-150（keycheck-150.log / keycheck-150.json）

- 三源：(1) content*.py `ex()`（133）＋`match_set()`（4 組 ×4＝16）按文件＋行號順序，共 149 項；(2) p8-extract.json keys（150）；(3) text.md 答案區解析（150 行）
- 結果：**149/149 一致**（配對題大小寫歸一）；150 題寫作 `✓ / Offene Aufgabe` 一致；mismatches: 0
- 類型：單選 67 / 完成句子 54 / 配對 16 / 完形單選 12（＋寫作 1）；級別 A2 44 / B1 74 / B2 31（＋150 題 B2＝32）

## 10. text.md 全文通讀與導出驗證

- muse.read 1–6075 行全部讀過（P1 頭、P1–P8 正文、P8 A–F 節、答案區 150 行、頁腳）
- 獨立重跑 exporter：`tools/venv/bin/python export_zhtw_textmd.py <ed>/svg $S/text-export-rerun.md "<H1>"` → 重跑 51,814 字節，與 shipped text.md **字節全同**（`text-export-rerun.md`）
- 掃查：`next Sunday`/`Next Sunday`/`下週日`/`BABYMONSTER`/`finish line`/`TODO`/`XXX`/`Lorem` 均 0；`本週日` 11、`取捨` 2、`小雪` 36；英文殘留掃描僅命中選項字母、德語詞內 `an`、正名 `The Awakening of the Wendigo` / `A Trip to the Moon`
- 彎引號/直引號全掃（`quotes-simp.log`）：SVG 8 頁＋text.md 中 `“ ” ‘ ’ " '` **均 0**
- 簡體字掃查（60 字簡體專用字表）：text.md＋8 SVG **0 命中**
- 凍結 key 核對：核心 content12.py:37/:113、content34.py:127 仍為 "next Sunday"；重 fan-out 機制表 tables.py:245/:267/:322 亦然；de 版 content*.py 無 "next Sunday"（德語 gloss 已譯 "diesen Sonntag"）。依任務指令不列缺陷
- E 節 typ：144–149 為 `完形單選`；全部 typ 字符串繁體，簡體形式 0
- 寫作範文重數：MODELO 去空格 **142 字**，與 keys 注一致

## 11. 外部事實獨立核查（2026-11-11 檢索，見 PROOF-NOTE §5）

- 金馬 63：2026-11-22（週日）臺北流行音樂中心，17:00/18:30，主持人柯煒林，587 部報名，入圍 10/1 公布，《狂忘警探》11 項領先，影展 11/6–22 ✓
- 小雪：2026-11-22 15:23，第 20 個節氣、冬季第 2 個 ✓
- 新北耶誕城：11/13–12/27（45 天），主燈秀 17:30–23:00 每半小時 5 分鐘（12 場）✓
- 香港迪士尼聖誕：11/17–2027/01/03（48 天），World of Frozen 首個冬日市集，音樂會 11/21、22＋12/5、6 共 4 場 ✓
- 星期核對（`TZ=Asia/Taipei date -d`）：11/13 週五、11/15 週日、11/16 週一、11/17 週二、11/21 週六、11/22 週日、11/24 週二、12/27 週日、2027/01/03 週日 ✓

## 12. 目視（自渲染，render/pg-1..8.png）

- `pdftoppm -png -r 100 Lucerna-VOL4-DE.pdf render/pg`（8 張）
- P1–P8 逐版看過：無溢出、無重疊、無頁腳碰撞；STRADDLE 4 處標題字形完整可讀；P6 時間線、P7 teaser、P8 鍵尾均在畫面內

## 13. 未執行的項（按任務紅線）

- 未改任何源碼／成品；未跑 insert.py、lint --write；未做任何 git 寫操作（add/commit/push 皆無）
- 三件交付物 SHA 復校前後一致：復校結束時重驗，de 版三件與核心三件 SHA 均與 §0 完全相同（未改動）
- 未派 subagent
