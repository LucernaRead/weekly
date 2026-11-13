# GATE-LOG — W47 zh-tw-de proof2（重擴散新版，機械門獨立重跑記錄）

復校對象：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-de/`
核心對照：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`（正典棧；creambox.py / check_fillin_keys.py 按 builder 驅動原樣走系統 python3，僅讀不寫）
日誌目錄：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-zh-tw-de1/`（下稱 `$S`）
執行時間：2026-11-11 ~20:16 UTC 起

## 0. 探針與身份核對

- `git -C ~/workspace/weekly-git hash-object -w /dev/null`：rc=0，`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`（空對象）
- goals 側真實寫文件 `probe.txt`：rc=0（內容 probe-ok）
- TMPDIR：`$S/tmp`（goals 側 scratch 下），未寫 /tmp；磁盤 /home/hatch 150G，已用 92G、可用 58G
- 身份核對（sha256sum + stat）：
  - 印 `Lucerna-VOL4-DE.pdf` 21,717,594 B `da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e` ✓
  - 網 `Lucerna-VOL4-DE-web.pdf` 2,452,914 B `de3a7594c2380e9f40e98bde23f4b163d365198a13ed6752bf6c5297b3111fd9` ✓
  - text.md 51,814 B `85584db99a9e2aa8685751d2ff385749cde5d78aca1c96cbefce845af54232fb` ✓
  - 核心三件：印 19,420,552 B `5ec35fe2…`、網 2,324,042 B `1c0799ac…`、text.md 49,798 B `09e083e1…` ✓（與 FANOUT-REPORT §0 一致；復校結束重驗未變）
- KIT 三 SHA：`WEEKLY-KIT.md` 內三件 SHA 各 `grep -c` = 1，與盤上逐字一致

## 1. run.py 重建（scratch 副本，`$S/rebuild/`，`out/run.log`）— RC=0

- 完整複製版目錄到 `$S/rebuild/`（`cp -a`，僅 ownership 警告，外觀；刪 `__pycache__`），在副本內跑 run.py，stdout 重定向到 `$S/out/run.log` 絕對路徑
- TOTAL **150**；by level A2 44 / B1 74 / B2 32；by page 10/18/18/18/18/18/12/38；by type 單選 67 / 完成句子 54 / 配對 16 / 完形單選 12 / 寫作 1；**FLOW OVERFLOW 0**
- 唯一警告：`!! HEAD TOO WIDE [P8-ex]: D　讀一讀，答一答　Lesen und antworten`（1 處，已知非缺陷，見 PROOF-NOTE §4）
- P7：flow A2 1343 / B1 1602 / B2 1535（bottom 1560）；col3 ends 1849.82；teaser ends 2589.82；P7 image ends 1570.86；P8 writing strip ends 1280.2；P8-keys ends 2373（bottom 2560）；MODEL chars: 142
- 重建 SVG 與交付 SVG 逐文件 sha256 比對：p1-front/p2-life/p3-culture/p4-sport/p5-youth/p6-deep/p7-lang/p8-test **8/8 MATCH**

## 2. render.py 重渲印 PDF（scratch 副本，`out/render.log`）— RC=0

- 在 `$S/rebuild/` 跑 render.py → 印 PDF 21,717,594 B，SHA `da4af743994c0c238549d6d87bc4fe95822b3215893988f8683ab4bf2402068e`，與交付印 PDF **逐字節相同**
- Web PDF 未重渲染（任務紅線：字節不可復現，只比文字層，見 §7）

## 3. gates 驅動（`gates-proof2.py`，builder gates.py 副本，M 改指本 scratch，tag proof2；`gates/de-proof2/gates.json`）

驅動原本把 `gtools/` 掛在 M 下，首跑 boxtitle/creambox-pil/fillin 因路徑不存在而 rc=2（見 `gates/de-proof2/*.log`）；已補拷 `gtools/` 到本 scratch 後逐項重跑，結果如下（重跑日誌 `out/boxtitle-rerun.log`、`out/creambox-pil-rerun.log`、`out/fillin-rerun.log`）：

## 4. checks.py（`gates/de-proof2/checks.log`）— rc=0 PASS

- 8 短語各 2 次；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]；CHECKS PASS

## 5. occlusion_audit.py（`occlusion-selftest.log` / `occlusion.log` / `occlusion.json`）

- `--selftest` rc=0：planted 6 類皆觸發（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），clean 對照靜默
- 正式審計 rc=0：**0 flags**

## 6. p8.py（`p8-extract.log` / `p8-compare.log` / `p8-extract.json` / `p8-compare.json`）

- `extract --p8 <ed>/svg/p8-test.svg --total 150 --json p8-extract.json` rc=0：noted set = **150/150**（1–150 連續）
- `compare --core-p8 core-zh-tw/svg/p8-test.svg --edition-p8 <ed>/svg/p8-test.svg --total 150 --json p8-compare.json` rc=0：**CLEAN**；直接讀 JSON：missing=[] extra=[] uncertain=[] **keydiff=[]**
- 注意：驅動 `gates.json` 的 p8.extra 顯示 `"?"` 是驅動取鍵 bug（讀了不存在的 `extra_count`），JSON 本身 extra=[] 已核實；builder 報告 §7.5 已記錄同 bug

## 7. freeze（`gates/de-proof2/freeze.log`、`out/freeze-core.log`、`out/freeze-diff.log` / `freeze-diff.json`）

- de 版：`freeze.py baseline --build . --core-svg svg --out $S/gates/de-proof2/freeze-base`（cwd=<ed>，僅重建 scratch 副本）→ **8/8 SVGs byte-identical**，core integrity：shipped core SVGs unchanged
- 核心：同命令（cwd=core-zh-tw，--out `$S/gates/de-proof2/freeze-base-core`）→ **8/8**，core integrity OK
- `freeze.py diff --core-svg core-zh-tw/svg --edition-svg <ed>/svg --json out/freeze-diff.json` rc=0：每頁 +25–192 / −25–185 strings；**TOTAL added CJK characters: 9**，全部為 `德`（P1 ×2、P2–P8 各 ×1；頁腳/徽章 `德語講解`）。裁決：通過

## 8. creambox canonical（`gates/de-proof2/creambox.log`）— 36 盒

- `tools/venv/bin/python hidden_files/w47/tools/creambox.py p1-front.svg … p8-test.svg`（cwd=<ed>/svg）rc=0
- 負內清除 **0**；分頁最小內清除：P1 18.8 / P2 41.8 / P3 15.8 / P4 35.8 / P5 6.4 / P6 19.9 / P7 12.5
- P7 工具盒：+40.5（`Stunde: 12-mal, 17:30–23:00 Uhr.`）/ +12.5（`mehr Y. Bilde einen eigenen Satz damit.`）/ +14.0（`Einladung bleibt offen.`）
- 負窗口清除 11 處：逐處裁決皆為盒下 37–44px 的下一標題（見 PROOF-NOTE §4）；同盒內末行均 +44.1/+44.3px。**spill 0**
- P5 `日` 盒：內清除 +6.4、desc-clear −0.4；真墨實測見 §11（墨清除 +4.4px，代理值誤報）

## 9. boxtitle / creambox-pil / fillin

- `gtools/boxtitle.py <ed>/svg $S/gates/de-proof2` rc=0（`out/boxtitle-rerun.log`）：36 盒，超框 **0**；最小標題右余 23.2px（P5），左余最小 18.0px；分頁：P1 35.2 / P2 28.2 / P3 65.8 / P4 33.0 / P5 23.2 / P6 44.0 / P7 150.0
- `gtools/creambox-pil.py <ed>/svg $S/gates/de-proof2` rc=0（`out/creambox-pil-rerun.log`）：STRADDLE **4**（P2 +64.2 / P3 +29.8 / P3 +28.2 / P5 +17.5，見 PROOF-NOTE §3）；CREAM-COVER **0**；P7 盒底清除最小 7.5px
- `gtools/creambox-pil.py <backup-old>/svg $S/gates/de-proof2`（舊版對照，`out/creambox-pil-old.log`）rc=0：STRADDLE 同為 4 處，墨盒/米色盒坐標**逐值相同**；P7 盒清除同值
- `gtools/check_fillin_keys.py <ed>/2026-w47-zh-tw-de.text.md <ed>` rc=0（`out/fillin-rerun.log`）：**54/54** 在正文，缺失 []

## 10. 印/網文字層（`gates/de-proof2/print.txt` / `web.txt`）

- `pdftotext -layout` 印/網：皆 **106,820 B，字節全同**；字符多重集差 0
- `pdftotext` plain：印 48,166 B / 網 48,167 B；多重集差僅 web 多 1 個 `\n`（run-boundary artifact）
- 計數（印/網一致）：本週日 11/11、下週日 0/0、BABYMONSTER 0/0、取捨 2/2、小雪 36/36、end point 0、next Sunday 0、Next Sunday 0

## 11. 幾何實測（`out/geometry.log`；PyMuPDF 數值見 gates.json pdf 節）

- PyMuPDF（venv）：雙 PDF 各 8 頁、1462.5×2025 pt；P8 字號 [9.75 … 34.5]，**最小 9.75pt**；P1 頂部 [147.0, 45.0, 27.0, 24.0]
- P7 teaser：矩形 [88.0, 2485.82, 1862.0, 2589.82] 高 104px，底緣 **2589.82**；頁腳規則 2596 → 餘 **6.18px**；頁腳墨頂 2609.25 → 墨距 19.43px；內文末行底 2572.07
- P8 D-head：墨盒 [989.0, 400.18, 1412.0, 420.68]（`D　讀一讀，答一答　Lesen und antworten`），寬 423.0 vs 欄寬 422.5 → **墨超 +0.5px**；右側 col4 級別章文字 `A2` 墨左緣 1457.5，淨空 **45.5px**（W46 已知非缺陷）
- P6 abutting：`頒獎典禮` 墨右緣 990.8 / `夜間遊行` 墨左緣 991.4，同基線 y≈974 → **縫 0.6px**，無重疊（gates.json abutting 節同值）
- P5 `日` 真墨：墨盒 [1461.5, 1095.5, 1484.0, 1115.2]，盒底 1119.6 → **真墨清除 +4.4px**

## 12. keycheck-150（`out/keycheck-150.log` / `out/keycheck-150.json`）

- 三源：(1) scratch 副本重跑 content*.py 取得的 `bslib4.REG`（150 項）；(2) p8-extract.json keys（150）；(3) text.md 答案區解析（150 行）
- 結果：**mismatches: 0**；第 150 題寫作三源一致 `✓ / Offene Aufgabe`
- 類型：單選 67 / 完成句子 54 / 配對 16 / 完形單選 12（＋寫作 1）；級別 A2 44 / B1 74 / B2 32
- 寫作範文重數：text.md Musterantwort 去空格 **142 字**，與 run.py `MODEL chars: 142` 及答案注 `(142 Zeichen)` 一致，在 120–180 帶內

## 13. text.md 全文通讀與導出驗證

- muse.read 1–6075 行全部讀過（P1 頭、P1–P8 正文、P8 A–F 節、答案區 150 行、頁腳）
- 獨立重跑 exporter：`tools/venv/bin/python export_zhtw_textmd.py <ed>/svg $S/out/text-export-rerun.md "<H1>"` rc=0 → 重跑 51,814 字節，與 shipped text.md **字節全同**（`cmp` 通過，`out/text-export-rerun.md`）
- 掃查：`next Sunday`/`Next Sunday`/`下週日`/`BABYMONSTER`/`finish line`/`TODO`/`Lorem` 均 0；`本週日` 11、`取捨` 2、`小雪` 36；`XXX` 5 處全在 SVG 內嵌圖片 base64 數據中，非可見文字
- 彎引號/直引號全掃：SVG 8 頁＋text.md 中 `“ ” ‘ ’` 均 0；`"` 在 SVG 中 41,606 處全為 XML 屬性引號
- 簡體字掃查（簡體專用字表 国/学/发/对/会/东/车/马/风/龙/乐/头/体/轻/边/达/过/还/这/为/与/实/义/广/门/开/关/见/贝/长/电/话/读/课/运/动/时/间/阳/阴/气/华/丽/观/护/让/说/认/识/应/灵/页）：text.md＋8 SVG **0 命中**
- title 數：按「文章/欄目/小檔標題」定義逐頁枚舉（P1 8 / P2 10 / P3 10 / P4 8 / P5 11 / P6 7 / P7 8 / P8 7 = **69**），在 SVG 文字層（去空白拼接）逐一驗證，0 缺失
- §1.1 顏色：紙色 #fbfaf6 全 8 頁；徽章色齊全；鵝黃 #f6e08e ×7（SOP 允許）；其餘非標色（#D7B257 等）全屬 P1 蛾標誌「Lucerna 三色蛾」，核心 P1 同有；VOL.4 文字層 10 處、VOL.5 恰 1 處、VOL.3 2 處；頁腳行 8/8、`Seite N von 8` 各 1
- 凍結 key 核對：核心 content12.py:37/:113、content34.py:127 仍為 "next Sunday"；de 版 content*.py / bslib4.py 中 "next Sunday"/"Next Sunday" 0 處；德語 "diesen Sonntag" gloss 三處（content12.py:37/:113、content34.py:127）已落位。依任務指令不列缺陷
- E 節 typ：144–149 為 `完形單選`；全部 typ 字符串繁體，簡體形式 0
- 英文殘留：僅正名 `The Awakening of the Wendigo` / `A Trip to the Moon`、德語借詞 `live`、exporter 固定英文頁眉（`## Page N — …`，已知非缺陷）

## 14. 外部事實獨立核查

- 金馬 63、小雪、新北耶誕城、香港迪士尼聖誕：見 PROOF-NOTE §5，全部與正文一致
- 星期核對（`TZ=Asia/Taipei date -d`）：10/1 週四、10/23 週五、11/6 週五、11/11 週三、11/13 週五、11/15 週日、11/16 週一、11/17 週二、11/19 週四、11/21 週六、11/22 週日、11/24 週二、12/4 週五、12/5 週六、12/6 週日、12/27 週日、2027/01/03 週日 ✓（正文標註星期之處全部一致）

## 15. 目視（自渲染，`render/pg-1..8.png`，pdftoppm 100dpi）

- P1–P8 逐版看過：無溢出、無重疊、無頁腳碰撞；STRADDLE 4 處標題字形完整可讀（裁切圖 `render/straddle-contact.png` 及 `s1-p2/s2-p3/s3-p3/s4-p5.png`）；P6 時間線、P7 teaser、P8 鍵尾均在畫面內

## 16. 未執行的項（按任務紅線）

- 未改任何源碼／成品；未跑 insert.py、lint --write；未做任何 git 寫操作（add/commit/push 皆無）；未重渲染交付的 web PDF；未動 KIT K6/K7
- 三件交付物 SHA 復校前後一致：生產目錄 39 文件 SHA 復校開始（`out/production-sha-before.txt`）與結束（`out/production-sha-after.txt`）逐一比對**完全相同**；核心三件 SHA 結束重驗未變；`git status --porcelain` 僅顯示該版目錄為 untracked（`??`，即未入倉狀態本身），無修改
- 未派 subagent
