# GATE-LOG — 2026-W47 zh-tw-ru proof2（独立复校）

复校时间：2026-11-11 ~20:56–21:10 UTC。驱动：本 scratch 内 `gates.py ru proof2`（由重扩散 `gates.py` 复制，仅改输出目录 + 修 p8 `extra` 取键 bug：`extra_count` → `extra`）。仓库 venv：`~/workspace/weekly-git/tools/venv/bin/python`。TMPDIR=`<scratch>/tmp`。原始日志：`gates/ru-proof2/`；汇总 JSON：`gates/ru-proof2/gates.json`。

## SHA（开工前 + 完工后两次实测，均一致）

| 件 | 字节 | SHA-256 |
|---|---|---|
| Lucerna-VOL4-RU.pdf | 12,896,218 | 1dbe1d8ec96fe91eeccb8b2a2f92080dd83c1302d85aed555e2e4e255224eeee |
| Lucerna-VOL4-RU-web.pdf | 2,007,900 | cb05eba2e641e3a200fff8d58648092788f08fca70f1d0ab8736ac76cfb50d52 |
| 2026-w47-zh-tw-ru.text.md | 62,492 | 2fb4b97ef37d490e834dbef5c9553fb476c209222f061f7a17c4274e882ae03b |

## 逐项门禁

### 1. checks.py — PASS (rc=0)
```
PHRASE 2 封王遊行從天母棒球場出發
PHRASE 2 夜間遊行晚上7點，最後一場不要錯過
PHRASE 2 小雪之後，天氣一天比一天冷
PHRASE 2 主燈秀每半小時一次，每次5分鐘
PHRASE 2 頒獎典禮晚上6點30分開始
PHRASE 2 保險箱裡，裝的是高雄的勞動記憶
PHRASE 2 穿上紅色衣服，一起上街為龍隊喝采
PHRASE 2 迪士尼聖誕，從11月17日開始
SIMP_ONLY_HITS []
CHART p4 [90.0, 450.0, 900.0] expect [90.0, 450.0, 900.0]
CHART p6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43] expect [188.0, 695.21, 948.82, 1033.36, 1202.43]
CHECKS PASS
```

### 2. occlusion audit — 0 flags (selftest rc=0, audit rc=0)
`occlusion.json`: flag_count 0。日志：`occlusion-selftest.log`、`occlusion.log`。

### 3. p8 extract + compare — 150 / CLEAN (rc=0)
- extract：noted_set 150/150（`p8-extract.log` 末行：`noted set = 150 of 150 (parse: lines)`）。
- compare：status CLEAN；core_count 150、edition_count 150；missing=[]、extra=[]、uncertain=[]、keydiff=[]（`p8-compare.json` 全文核对）。keydiff 只量不预设：实测 []，即答案值与核心 150 项逐项一致。

### 4. canonical creambox（tools/creambox.py，全 8 SVG）— 36 盒 / 0 负清除 (rc=0)
各页最小内清除：P1 18.8、P2 15.8、P3 15.8、P4 9.8、P5 6.4、P6 19.9、P7 12.5（P8 无盒）。
P7 工具盒（canonical creambox [P7-TOOLBOX]）：+40.5（「полчаса: 12 показов с 17:30 до 23:00.」）、+12.5（「X, тем больше Y. Составьте фразу.」）、+14.0（「остаётся, приглашение открыто.」）。

### 5. boxtitle — 0 超框 (rc=0)
boxes measured: 36；title/line overruns past box right edge: 0；min title right margin overall: 22.5px；min title left margin overall: 见 `boxtitle.log`（逐盒见 `boxtitle.json`）。

### 6. creambox PIL — STRADDLE 4 / CREAM-COVER 0 (rc=0)
- P2「耶誕城小檔　Крисмасленд: коротко」ink [1461.5, 1452.5, 1903.5, 1479.5]，cream 右缘 1862.0（+41.5px）
- P3「金馬小表　«Золотая лошадь»: коротко」ink [1461.5, 671.8, 1942.2, 699.1]，cream 右缘 1862.0（+80.2px）
- P3「鋼雕閉幕行程　Последние выходные」ink [1461.5, 1428.1, 1915.5, 1454.6]，cream 右缘 1862.0（+53.5px）
- P5「迪士尼聖誕小檔　Дисней: коротко」ink [1461.5, 672.1, 1876.2, 699.1]，cream 右缘 1862.0（+14.2px）
- 旧版对照（同一脚本跑备份旧版 SVG，`old-ru-check/creambox-pil-old.log`）：旧版 5 处，余 4 处坐标逐字相同；消失的 P4「занимаетесь спортом?」已被核心 fix5 修掉。非回归。
- 渲染像素复核（交付印刷 PDF，PyMuPDF 1pt=1px）：墨右缘/cream 右缘（pt）P2 1426/1395、P3-horse 1457/~1396.5、P3-steel 1435/1392、P5 1406/1395；框内外 20px 墨密度基本连续（0.19/0.18、0.14/0.13、0.22/0.21、0.17/0.11），字形完整无裁切；裁切图 `render/straddle-p*.png`。P7 PIL 最小底清除 7.7px。
- CREAM-COVER 0。

### 7. text layer 印/网比对
pdftotext -layout：印/网字节均为 112,947；字符多重集差 0（print_only 0、web_only 0）。
计数（印/网一致）：本週日 11、下週日 0、BABYMONSTER 0、取捨 2、end point 0、小雪 36。
（附：plain pdftotext 未跑——-layout 已逐字节一致，无需复核 run-boundary 空白 artifact。）

### 8. PDF 度量（PyMuPDF）
印/网均为 8 页、1462.5×2025 pt；P8 最小字号 9.75pt（恰 SOP §1.1 下限）、最大 34.5pt；P1 顶部字号 [147.0, 45.0, 27.0, 24.0]；网页 PDF 2,007,900 B < 7 MB。

### 9. keycheck — 填空 54/54、正文键 1–150 连续
`check_fillin_keys.py`：填空键总数 54，在正文 54/54，缺失 []。
text.md keys 区：数字键 1–150 连续（150 个）。

### 10. leak scan — deny 命中 0
DENY 清单（next Sunday / Next Sunday / finish line / the place it happens / The ceremony is at the Taipei Music Center. / Xiaoxue is Nov 22. / Four big events fall on the same Sunday. / Collecting points is 集點. / Memory trick: learn 入圍 first, then the ceremony / Parades give you four useful words…）：全部 0 命中。
与核心共有的长 ASCII 串仅 1 条：「A. 12:00 · B. 14:00 · C. 19:00」（选项行构造共享，非泄漏）。

### 11. abutting — P6 18:30/19:00 墨缝 0.6px
label1「頒獎典禮」box [906.8, 955.8, 990.8, 977.5]；label2「夜間遊行」box [991.4, 955.8, 1075.4, 976.2]；缝 = 991.4 − 990.8 = 0.6px，与核心先例完全一致。

### 12. freeze — 8/8 (rc=0)
baseline：8/8 SVGs byte-identical；log 尾：`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。`freeze-base/` 在 `gates/ru-proof2/` 内。

## 独立重建（scratch 副本跑 run.py，见 rebuild-run.log）

RC=0。TOTAL 150；by level {A2: 44, B1: 74, B2: 32}；by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；by type {單選: 67, 完成句子: 54, 配對: 16, 完形單選: 12, 寫作: 1}；FLOW OVERFLOW 0 处；P7 image ends 1637.74（A2 flow ended 1409.94）、P7 col3 ends 1823.3、P7 teaser ends 2577.3；P8 writing strip ends 1280.2（flow ended 529.05）。

⚠️ 披露：`content12.py:10` 将 OUT 硬编码为生产目录绝对路径，本轮重建实际把 8 个 SVG 重写回生产目录。事后核对：8 个 SVG SHA 与门禁前记录值（`gates.json` 内 svg_sha256）逐字节相同，三件交付物 SHA 亦未变，仅 SVG mtime 变为 2026-11-11 21:01–21:02。内容零改动；建议后续将 OUT 参数化。

## 目视

交付印刷 PDF 逐页渲染（PyMuPDF，0.75×，`render/p1.png`–`p8.png`）+ 4 处 STRADDLE 裁切图（2×，`render/straddle-*.png`）：8 页全部看过，无溢出、无重叠、无页脚碰撞；P4 D4 盒底穿已修好（末行在盒内）；P7 teaser 条与金句区完整；P8 答案键完整。详见 PROOF-NOTE.md §4。

## 补充核查

- 「next Sunday」：俄语版 SVG + text.md 命中 0（grep -ri，大小写不敏感）。
- 孤儿填空行：text.md 与 8 个 SVG 中 `____` 命中均为 0，本版未出现。
- 8 个 SVG SHA（门禁时记录）：见 `gates/ru-proof2/gates.json` → files.svg_sha256；重建后逐字节复核全部 IDENTICAL。
