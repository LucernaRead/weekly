# GATE-LOG — W47 zh-tw-ru proof1（重建版，机械门输出留档）

复校对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-ru/`（重建版；SHA 见 §0）。
工具一律 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3），除注明者外。
门禁驱动脚本：本目录 `gates-proof1.py`（逐门调用并把原始输出存入 `gates/`）；汇总见 `gates/gates.json`。
**注意**：本目录此前存放的旧版 proof1 记录（SHA `e1f3c46a…`）已移入 `archive-old-edition/`；旧版 GATE-LOG 的门禁结果属于旧版文件，不适用于本版。本文件只记录重建版的门禁。

## 0. 探针 + 对象核验（2026-11-11）

```
echo test | git -C ~/workspace/weekly-git hash-object -w --stdin
# -> 通过（写盘探针成功）；另在 goals 侧 hidden_files/w47/ 真实写文件成功，才开工
sha256sum Lucerna-VOL4-RU.pdf Lucerna-VOL4-RU-web.pdf 2026-w47-zh-tw-ru.text.md
# 1dbe1d8ec96fe91eeccb8b2a2f92080dd83c1302d85aed555e2e4e255224eeee  Lucerna-VOL4-RU.pdf
# cb05eba2e641e3a200fff8d58648092788f08fca70f1d0ab8736ac76cfb50d52  Lucerna-VOL4-RU-web.pdf
# 2fb4b97ef37d490e834dbef5c9553fb476c209222f061f7a17c4274e882ae03b  2026-w47-zh-tw-ru.text.md
# 字节：print 12,896,218 / web 2,007,900 / text.md 62,492 —— 与任务给定全符
# 复校结束时再次 sha256sum + stat，SHA 与字节不变（文件未动）
# 核心对照 core-zh-tw：印 5ec35fe2… 19,420,552 B；网 1c0799ac… 2,324,042 B；text 09e083e1… 49,798 B；重建前后未变
```

## 1. Freeze baseline — 核心 8/8；本版 8/8

```
tools/venv/bin/python tools/freeze.py baseline --core-svg <core>/svg --out gates/freeze-base
# rc=0
# runtime: tools/venv/bin/python | Pillow 13.0.0 | FreeType 2.14.3
# baseline: 8/8 SVGs byte-identical
#   OK p1-front.svg core cc70b39c778862a4 produced cc70b39c778862a4
#   OK p2-life.svg core 55378c704c403076 produced 55378c704c403076
#   OK p3-culture.svg core 1ef686586ca28490 produced 1ef686586ca28490
#   OK p4-sport.svg core ec781f9c0cdf540e produced ec781f9c0cdf540e
#   OK p5-youth.svg core 183e0bc4691239d6 produced 183e0bc4691239d6
#   OK p6-deep.svg core 51dafd84a692439a produced 51dafd84a692439a
#   OK p7-lang.svg core 839a809381116764 produced 839a809381116764
#   OK p8-test.svg core 8e65cb3f67c261fe produced 8e65cb3f67c261fe
# core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)
tools/venv/bin/python tools/freeze.py baseline --build <edition> --core-svg <edition>/svg --out gates/freeze-base-ru
# rc=0；8/8，哈希与构建者 gates/ru-final/freeze.log 逐字相同：
#   p1 613bc4fc1aad85ec / p2 73a170921ab16e1e / p3 2857c6bdb7ac5b29 / p4 cc15713ab1cbf254
#   p5 756727480dd0e1bc / p6 5de978a395ce9fc3 / p7 94281b35d9038213 / p8 5dee99964455cad6
# （构建者 freeze.log 的核心哈希与我方核心 freeze 不同，是因为那是本版重建而非核心——已复核，无漂移）
```
输出：`gates/freeze.log`、`gates/freeze-ru.log`、`gates/freeze-base/`、`gates/freeze-base-ru/`。

## 2. Freeze diff --strict-cjk — FAIL（仅家具 `俄`，已定位）

```
tools/venv/bin/python tools/freeze.py diff --core-svg <core>/svg --edition-svg <edition>/svg --strict-cjk --json gates/freeze-diff.json
# rc=1
# STRICT-CJK FAIL: edition adds CJK characters the core does not have
# p1: +25/-25 strings; CJK core 892 -> edition 879; added CJK chars: 2 {'俄': 2}
# p2: +42/-39; CJK 1111 -> 1106; added: 1 {'俄': 1}
# p3: +53/-48; CJK 1198 -> 1193; added: 1 {'俄': 1}
# p4: +43/-40; CJK 810 -> 805; added: 1 {'俄': 1}
# p5: +54/-47; CJK 1220 -> 1215; added: 1 {'俄': 1}
# p6: +37/-33; CJK 884 -> 879; added: 1 {'俄': 1}
# p7: +364/-107; CJK 822 -> 817; added: 1 {'俄': 1}
# p8: +202/-187; CJK 1114 -> 1109; added: 1 {'俄': 1}
# TOTAL added CJK characters: 9
```
成因：9 个 `俄` 全部来自页眉徽章读者语名（`Lucerna 繁體中文週報 VOL.4 繁體中文正文 俄語講解`，核心同槽为 英語講解）。字符串级差分审计：其余增/删均为英→俄注释翻译、双语标签翻译、相同中文串的换行重切——中文正文无增无失。与旧版 freeze diff（+36 字，含 `下`、`。`、BABYMONSTER 行）对比，本版只剩家具 `俄`，与旧-D1/旧-N3/旧-N5 的修复一致。
输出：`gates/freeze-diff.log`、`gates/freeze-diff.json`。

## 3. checks.py — PASS

```
tools/venv/bin/python checks.py   # cwd=<edition>
# PHRASE 2 封王遊行從天母棒球場出發 / 夜間遊行晚上7點，最後一場不要錯過 / 小雪之後，天氣一天比一天冷
# PHRASE 2 主燈秀每半小時一次，每次5分鐘 / 頒獎典禮晚上6點30分開始 / 保險箱裡，裝的是高雄的勞動記憶
# PHRASE 2 穿上紅色衣服，一起上街為龍隊喝采 / 迪士尼聖誕，從11月17日開始
# SIMP_ONLY_HITS []
# CHART p4 [90.0, 450.0, 900.0] expect [90.0, 450.0, 900.0]
# CHART p6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] expect [188.0, 695.21, 948.82, 1033.36, 1202.43]
# CHECKS PASS
```
输出：`gates/checks.log`。

## 4. Occlusion 审计 — 0 flags

```
tools/venv/bin/python tools/occlusion_audit.py --selftest
# rc=0；selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent
tools/venv/bin/python tools/occlusion_audit.py --json gates/occlusion.json <edition>/svg
# rc=0；<edition>/svg: 0 flags
```
输出：`gates/occlusion-selftest.log`、`gates/occlusion.log`、`gates/occlusion.json`。

## 5. p8 extract — 150/150；p8 compare — CLEAN

```
tools/venv/bin/python tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150 --json gates/p8-extract.json
# rc=0；noted set = 150 of 150 (parse: lines)；set: [1..150]
tools/venv/bin/python tools/p8.py compare --core-p8 <core>/svg/p8-test.svg --edition-p8 <edition>/svg/p8-test.svg --total 150 --json gates/p8-compare.json
# rc=0
# core 150 noted；edition 150 noted
# status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[]
```
注：构建者 `gates.py` 读 `extra_count` 有小 bug 显示 "?"；我方直接读 compare JSON，`extra=[]`。
输出：`gates/p8-extract.json`、`gates/p8-extract.log`、`gates/p8-compare.json`、`gates/p8-compare.log`。**keydiff 为空，无逐项差异可列。**

## 6. Canonical creambox — 36 盒，0 负间隙

```
python3 hidden_files/w47/tools/creambox.py <edition>/svg/*.svg
# rc=0；36 boxes；negative clearances: []
# min by page: p1-front 18.8 / p2-life 15.8 / p3-culture 15.8 / p4-sport 9.8 / p5-youth 6.4 / p6-deep 19.9 / p7-lang 12.5
# P7-TOOLBOX: +40.5「полчаса: 12 показов с 17:30 до 23:00.」/ +12.5「X, тем больше Y. Составьте фразу.」/ +14.0「остаётся, приглашение открыто.」
```
输出：`gates/creambox.log`、`gates/creambox.json`。

## 7. boxtitle — 36 盒，0 超出

```
tools/venv/bin/python <scratch-refanout-zh-tw>/gtools/boxtitle.py <edition>/svg gates/
# rc=0
# boxes measured: 36；title/line overruns past box right edge: 0
# min right margin by page: p1 63.8 / p2 28.5 / p3 26.8 / p4 34.5 / p5 22.5 / p6 55.2 / p7 38.2
# min title right margin overall: 22.5 px；min title left margin overall: 18.0 px
```
输出：`gates/boxtitle.log`、`gates/boxtitle.json`。

## 8. creambox-pil — STRADDLE 4，CREAM-COVER 0（新版 + 旧版备份对照）

```
tools/venv/bin/python <scratch-refanout-zh-tw>/gtools/creambox-pil.py <edition>/svg gates/
# rc=0；cream boxes total: 36；STRADDLE flags: 4；CREAM-COVER flags: 0
#   STRADDLE p2-life.svg '耶誕城小檔　Крисмасленд: коротко' ink [1461.5, 1452.5, 1903.5, 1479.5] cream [1439.5, 1430.0, 1862.0, 1890.0]  （超盒右 +41.5）
#   STRADDLE p3-culture.svg '金馬小表　«Золотая лошадь»: коротко' ink [1461.5, 671.8, 1942.2, 699.1] cream [1439.5, 649.6, 1862.0, 1119.6]  （+80.2）
#   STRADDLE p3-culture.svg '鋼雕閉幕行程　Последние выходные' ink [1461.5, 1428.1, 1915.5, 1454.6] cream [1439.5, 1405.6, 1862.0, 1855.6]  （+53.5）
#   STRADDLE p5-youth.svg '迪士尼聖誕小檔　Дисней: коротко' ink [1461.5, 672.1, 1876.2, 699.1] cream [1439.5, 649.6, 1862.0, 1119.6]  （+14.2）
# min bottom clearance per page: p1 16.5 / p2 15.6 / p3 11.3 / p4 5.3 / p5 4.4 / p6 17.1 / p7 7.7
tools/venv/bin/python <scratch-refanout-zh-tw>/gtools/creambox-pil.py <scratch-refanout-zh-tw>/backup/2026-w47-zh-tw-ru/svg gates/
# STRADDLE flags: 5 —— 上述 4 处墨迹坐标像素一致，另第 5 处：
#   STRADDLE p4-sport.svg 'занимаетесь спортом?' ink [1461.5, 1346.9, 1683.5, 1366.7] cream [1439.5, 1128.0, 1862.0, 1358.0]
#   （旧版盒底 1358.0，墨迹底 1366.7，穿出 8.7px；新版盒底 1372.0，间隙 +5.3px —— 核心 fix5 已修好，见 PROOF-NOTE §5）
# 注：旧版扫描尾部报 FileNotFoundError（向不存在的 gates/old-ru/ 写 creambox.json），测量输出本身完整无缺；5 个 flag 均已打印在日志中。
```
输出：`gates/creambox-pil.log`、`gates/creambox-pil-old-ru.log`。裁图：`crops/straddle-p2.png`、`straddle-p3a.png`、`straddle-p3b.png`、`straddle-p5.png`、`p4-d4.png`（200 dpi，目视 4 处字形完整、无压叠）。

## 9. 印/网文字层比对 — 多重集差 0

```
pdftotext -layout Lucerna-VOL4-RU.pdf gates/print.txt       # 112,947 bytes
pdftotext -layout Lucerna-VOL4-RU-web.pdf gates/web.txt     # 112,947 bytes
# 字符多重集差：0；位置差分：仅 1 行（P1 页眉行距，1 个空格列）—— run-boundary 伪影
pdftotext Lucerna-VOL4-RU.pdf gates/plain-print.txt         # 58,580 bytes
pdftotext Lucerna-VOL4-RU-web.pdf gates/plain-web.txt       # 58,581 bytes
# 多重集差：仅 1 个 \n，同类伪影
# 文字层内计数（印/网一致）：本週日 11 / 下週日 0 / BABYMONSTER 0 / 取捨 2 / end point 0 / 小雪 36
```
输出：`gates/print.txt`、`gates/web.txt`、`gates/plain-print.txt`、`gates/plain-web.txt`、`gates/pdftotext-print.log`、`gates/pdftotext-web.log`。

## 10. PDF 度量（PyMuPDF，tools/venv）

```
# Lucerna-VOL4-RU.pdf：8 页，1462.5 x 2025.0 pt；P8 min 9.75pt / max 34.5pt；12,896,218 B
# Lucerna-VOL4-RU-web.pdf：8 页，1462.5 x 2025.0 pt；P8 min 9.75pt / max 34.5pt；2,007,900 B
# P1 顶部字号：[147.0, 45.0, 27.0, 24.0]
```
结论：双 PDF P8 最小字号均为 9.75pt，恰达 SOP §1.1 下限。

## 11. 填空键 + 答案键连续性 — 54/54，1–150 连续

```
python3 <scratch-refanout-zh-tw>/gtools/check_fillin_keys.py <edition>/2026-w47-zh-tw-ru.text.md <edition>
# 填空键总数：54；在正文：54/54；缺失：[]
# （逐键记录见 gates/fillin-check.log：每键附正文出现次数与源码行号）
# text.md 答案区编号：1–150 全齐，无缺无重（keys_continuous_1_150: true；keys_found: 150）
```
输出：`gates/fillin-check.log`。

## 12. 泄漏扫描 / 相邻墨迹 / 引号 / 简体字 / E 节标签 / 星期

```
# 泄漏扫描（全版 SVG 文本 vs 核心英文；deny 串含 "next Sunday"、"finish line"、4 条英文答案注、"Memory trick: learn 入圍 first…" 等）：
#   deny_hits: {}（0 命中）
#   唯一共有长 ASCII 串："A. 12:00 · B. 14:00 · C. 19:00"（Q140 选项，构造性共有）
# 相邻墨迹（P6 18:30 頒獎典禮 / 19:00 夜間遊行）：ink gap 0.6 px
#   label1 box [906.8, 955.8, 990.8, 977.5]；label2 box [991.4, 955.8, 1075.4, 976.2] —— 与核心先例相同
# 直引号：ASCII " / ' 在 8 SVG 与 text.md 中均为 0；俄文 «» 全篇，嵌套 “„
# 简体专属字（邮说国龙马发观欢对让认识语学读书报纸电话车门问间见风云气头）：SVG []、text.md []
# 台灣 0 次；英文 UI 词 Fill in / True or false / next Sunday / finish line 均为 0
# E 节标签：A 判斷對錯、B 本週大測驗、C 完成句子、D 讀一讀，答一答、E 情景說話、F 寫一寫（全繁体 + 俄文）
# 星期（date，Asia/Taipei）：2026-11-16 一、11-17 二、11-21 六、11-22 日、11-13 五、11-19 四、11-24 二、12-27 日、2027-01-03 日——与报纸一致
```
以上核查逻辑在 `gates-proof1.py` §9–§10 及后续 grep 中；结果汇总于 `gates/gates.json`。

## 13. 150 题三源交叉（keycheck-150.json 生成）

```
# 键来源：A=text.md 答案区；B=P8 SVG（p8.py extract 导出）；C=核心 text.md 答案区
# 生成：tools/venv/bin/python gates/make_keycheck.py  （读 gates/keycompare-raw.json、gates/keycompare-core.json、gates/stemcheck.json）
# 结果：three_source_agree 150/150；mismatches 0
# 题干：150 题干全在版面 SVG 中；仅 41、77、78、84、85 在 PDF 文字层中因 pdftotext -layout 跨栏交错未成连续串，
#   已在渲染页上逐一目视核实（Q41 在 P3、77/78 在 P5、84/85 在 P6）——提取伪影，非缺陷
# Q150：三源均为写作范文（142 字，120–180 内）
```
输出：`keycheck-150.json`（SHA-256 `28897d6beb9e6d30eb9dd3f69c9f607fc9faf9a7dfdb6058fdb526c6d0410c15`）、`gates/keycompare-raw.json`、`gates/keycompare-core.json`、`gates/stemcheck.json`。

## 14. 旧版缺陷处置复测（旧-D1 + 旧-N1–N7，见 PROOF-NOTE §0）

```
# 旧-D1：grep -o 本週日 text.md | wc -l → 11；grep -o 下週日 text.md | wc -l → 0；SVG 下週日 0；следующее воскресенье 0
#   P4 注分两元素：это / воскресенье, 22 нояб., в 14:00, от
# 旧-N1：content7.py:18 与 tables.py:2114 均为 "Выучите их один раз"
# 旧-N2：tables.py grep "Тайбэйском музыкальном центре" / "Сяосюэ — 22 ноября" / "Четыре больших события" / "Накапливать баллы" 各 1 命中；ENTRIES 242
# 旧-N3：BABYMONSTER 在 content56.py 与 P5 SVG 中 0 命中；content56.py:107 by4 = by3 + 436（与核心逐字同）
# 旧-N4：content12.py:68 "本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行"
# 旧-N5：P8 SVG key 134 "Накапливать баллы — это 集點."
# 旧-N6：SVG "гигантский надувной Пикачу" ×2；tables.py:373 / :1541 同值
# 旧-N7：SVG "Рождество в Диснейленде" ×4；"Рождество в Диснее" 0
# → 8 项全部已修好
```

## 15. KIT 登记核查（新发现 D1）

```
grep -n "1,993,092\|2,007,900" <edition>/WEEKLY-KIT.md
# :35（现行登记行）：… web 2,007,900 bytes … SHA-256 cb05eba2… … Web PDF 1,993,092 bytes; web text layer 58,581 bytes …
# :79（Proofread record 旧轮次历史）：Web PDF: tools/webpdf.py exit 0; 1,993,092 bytes …
stat -c %s <backup>/Lucerna-VOL4-RU-web.pdf <edition>/Lucerna-VOL4-RU-web.pdf
# 1993092（旧版）/ 2007900（新版）
# 结论：:35 同一行内自相矛盾（2,007,900 与 1,993,092），1,993,092 是旧版残留 —— D1（轻微，版级）。
# :79 是保留的旧轮次历史记录，数值就其历史语境正确，不列缺陷。
# 其余旧值（印 PDF 12,896,270、旧 SHA、文字层 58,526/58,528）在新 KIT 中均已更新，无第二处残留。
```

## 16. 渲染卡逐版目视

```
# 印 PDF 8 页自渲染 100 dpi：pages/p-1.png … p-8.png，逐页目视：无溢出、无重叠、无页脚碰撞
# （网页 PDF 未另渲染：印/网文字层 -layout 均为 112,947 B、多重集差 0，且同版式；旧版证明曾渲染网页 P1/P7，0 发现）
```
