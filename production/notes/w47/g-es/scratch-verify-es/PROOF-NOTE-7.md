# PROOF-NOTE-7 — W47 es-ru 第七轮独立重校（round-6 后重建版）

- **轮次**：第七轮独立重校（SOP §8/§8.4；校对员与建造者、第六轮校对员 50ffaae9、fix-es-ru2 修复者 f9272fd5 均不同；只校对、不修复）
- **日期**：2026-11-13（UTC 约 04:50–05:20；门禁 GATES7 DONE 05:06:25）
- **范围**：仅 `2026-w47-es-ru` 一版。起因：round-6 CLEAN（2026-11-12 ~22:35 UTC）之后该版经历两次重建，印/网 SHA 已变，round-6 结论不再覆盖本版；按 SOP §8.4（改源码 → 重渲染 → 从头再做一轮全量校对）做全新全量重校。
- **结论：(b) 1 项 low 发现 — 不 CLEAN。** 除此 1 项外全部通过。须修复 + 重建 + 再做一轮全量校对后才能定稿。

## §0 指纹 — 与修后值一致，text.md 未动

| 件 | 字节 | SHA-256（前 12） | 与 FIX-LOG（fix-es-ru2） |
|---|---|---|---|
| 印 `La-Lucerna-VOL4-es-ru.pdf` | 3,100,944 | `d383753b4862` | 一致（修前 277b2d26…/3,100,942） |
| 网 `La-Lucerna-VOL4-es-ru-web.pdf` | 950,823 | `b6246122f94d` | 一致（修前 98536828…/950,829） |
| text.md `2026-w47-es-ru.text.md` | 52,367 | `ac246f8709d3` | 一致，未变（round-6 同值） |

- 印/网各 8 页；网 < 7 MB；印/网 pdftotext 各 53,413 B，**逐字节一致**（`cmp` 通过）。
- KIT 已同步新 SHA：印完整 SHA ×2、网完整 SHA ×2、text 完整 SHA ×4（含历史记录）。

## §1 发现 — 1 项 low（F1）

**F1（low，P5）：EJERCICIOS 分隔线横穿 ¿Y TÚ? 框，把框内最后一行切在框外一侧。**

- 几何（实测，`p5-juventud.svg`）：分隔线 `<line x1="88" y1="1608" x2="1862.0" y2="1608">`，全宽、后绘于框之上；¿Y TÚ? 奶油框 `x=1439.5 y=1277.55 h=356.0`，框底 1633.55；分隔线穿过框内，框底超出分隔线 **25.5px**。框内俄文末行 `пришлите их.`（基线 y=1626.59）在分隔线之下、框底之内——字形未被线划过，但视觉上该行与框体被绿线隔开。
- 目视证据：150dpi 全页 + 2× 局部放大（`p5-zoom.png`）：绿线在 `Напишите два предложения и` 与 `пришлите их.` 之间横穿框体。
- 机械门禁均未报：occlusion 的 LINEX 只查线穿字形墨迹带（线走行间空隙，未触字）；spill 只查文字出框（末行基线 1626.59 < 框底 1633.55，在框内）；boxtitle 只查框题。**此为共享工具未覆盖的新缺陷类：分隔线 vs 内容框的交叉。**
- 溯源（实测，非推测）：框高随字体改道逐次变高——2026-11-10 副本 303.0（框底 1580.55）、D5 前基线 2026-11-12 06:46 为 329.0（框底 1606.55，距分隔线仅 1.45px）、现行 356.0（框底 1633.55）。分隔线 y=1608 三版均未动。交叉出现于 11-12 字体改道期间（D5 与 *-ru 两轮）；round-6 当时的框高无存世副本可核，故**不能断定是 D5 还是 *-ru 引入**，只记为“11-12 字体改道期间引入”。
- 全家横扫：8 页逐一核对全宽分隔线 vs 全部奶油框，仅 P5 这一处交叉；其余 7 页无。
- 修法建议（供协调员定，不擅自改）：缩短框内俄文使框高回落至分隔线之上（约需省 26px ≈ 1 行），或调框内行距/字号；改后须重建 + 全部门禁 + 再做一轮全量校对。text.md 措辞若动须同步重导出并核对 diff 仅含意改行。

## §2 全量通读 — text.md 1888 行读完，无其他问题

- 西语拼写/重音/性数/变位/标点、俄语译文逐行读完；讲解层注释的词均在正文出现。
- 日期/星期经 `date` 全验（2026-11-13 五、16 一、17 二、18 三、19 四、20 五、21 六、22 日、23 一、24 二、27 五、28 六、29 日）全部正确；2010-11-16 为周二（正文未宣称星期，无问题）。
- 算术：RTVE 免费时长 45+45+30+30+15=165，另 3 党各 10 分钟，合计 195 ✓；竞选 13→27 日共 15 天 ✓；11 月 16 日至 29 日 13 天 ✓；范文 97 词机械计数 ✓（文本在印层在位）。
- 事实抽查：UNESCO 2010 年 11 月 16 日内罗毕列入非遗 ✓；Sargent 图注经独立检索核实——确有油画 `Spanish Dancer`（1880–1881，私人收藏，Google Arts & Culture），图为单人舞者、非《El Jaleo》（1882，群像），标题与年份均属实；投票箱照片与图注相符（青铜投票箱，SUFFRAGE UNIVERSEL）；中世纪祈祷书配图与图注相符；天鹅羽笔配图与图注相符。
- 8 金句逐字核对正文 + 印层 SVG 双源：各 2 次（正文 1 + P7 1），逐字一致。
- 已核查非发现（不重报）：F1 首字母下沉（已裁定不修）；text.md 页内顺序打散（跨家已裁定延期修导出器）；`laSexta`/`LaLiga`/`MiDNI` 品牌驼峰；P2/P4 的 D/B 节标题在栏底、内容在下一栏（正常流式排版）。

## §3 150 题全量复核 — 全部一致

- `tools/p8.py extract`：150/150；`compare` vs core-es：**CLEAN**，missing=[] extra=0，keydiff=[137, 138]（已裁定的读者语翻译题差异，与 round-6 一致）。
- 印层抽取的 150 条答案键与 text.md 答案键逐项比对：150/150 一致（137 号键为 `Понедельник`，系工具取键首词；150 号为 `✓` 开放题例外，均与 KIT 注一致）。
- 题干与答案逐题核对：编号连续 1–150；分级与题面一致；Q85/Q89/Q90、Q123/Q132、Q126–Q128 的题号归属曾因 text.md 打散存疑，已用印 PDF 版式抽取逐一核实（85=Podemos 15 分钟→C；89=唯一已确认辩论→B；90=辩论时间→A；126=MiDNI→C；127=禁发民调 24–28→B；128=欧冠第五轮 24–25→C；132=最佳标题→B），答案键全部正确。
- P8 最小字号与级别徽章：p8 extract 150/150 通过；gates 侧未单跑，以上两项由 p8 工具覆盖。

## §4 8 页逐页看图 — 除 F1 外全部干净

- 渲染：`pdftoppm -r 150`，8 页逐页目视（`pg-1.png` … `pg-8.png`）。
- P1：修复标题 `LA SEMANA EN CIFRAS　В цифрах` 在框内、余量充足（boxtitle 直接测量 ink_r 最大 946.3px vs 框右界 961.0，见 FIX-LOG；目视确认）；`AHORA TÚ　Теперь вы` вы 体正确；其余无溢出/重叠/压页脚/豆腐块。
- P2/P3/P4/P6/P7/P8：无溢出、重叠、压页脚、图片与出处不符、豆腐块。P3 中栏留白、P6/P7 栏尾留白为正常栏空。
- 唯一例外：P5 F1（见 §1）。

## §5 机械门禁 — 全绿（共享工具重跑）

| 门 | 工具 | 结果 |
|---|---|---|
| p8 extract | `tools/p8.py extract --total 150` | 150/150，rc=0 |
| p8 compare vs core-es | `tools/p8.py compare --total 150` | CLEAN，keydiff=[137, 138]，rc=0 |
| D5 census | `scratch-d5-plan/mechanism/d5_census.py` | CENSUS PASS，rc=0 |
| 几何遮挡 | `tools/occlusion_audit.py svg/`（自检先行） | selftest OK，**0 flags**，rc=0 |
| 框题 | `tools/boxtitle_check.py` | 38 titles / 584 body lines，**0 DEFECT**，0 OBSERVE，0 marginal，rc=0 |
| 溢出 | `tools/spill_sweep.py` | 27 盒 / 149 candidates，**0 SPILL**，149 OBSERVE，rc=0 |
| 页缘 | `tools/pdf_edge_scan.py` | 8 页，**0 TOUCH / 0 NEAR**，rc=0 |
| 冻结复现 | `tools/freeze.py baseline` | **8/8 SVGs byte-identical**，rc=0 |
| 印/网文字层 | `pdftotext` + `cmp` | 各 53,413 B，**逐字节一致** |

- 注：首轮 occlusion 调用误加 `--selftest`（该 flag 含义为“只跑合成自检、不审 SVG”，返回 0 即出结论，属假通过）；已发现并用不带该 flag 的正确调用重跑，结果见上（`occlusion2.log`，`occlusion.json`）。gates7.log 已追加更正。
- 未跑 lint，未 commit，未 push，未改生产文件；工具解释器 `~/workspace/weekly-git/tools/venv/bin/python`。

## §6 KIT — 本版已同步

- 印/网/text 三个现行完整 SHA 在 KIT 中各 ≥2 处（印 ×2、网 ×2、text ×4，含历史记录），与盘上实时值一致；§8 有 fix-es-ru2 一节。无 KIT 缺口。

## §7 工作记录

- **只读**：未修复、未重建、未 commit、未 push、未跑 lint、未改 SOP、未碰其他家庭/其他周；除本 scratch 目录与 /tmp 抽取文本外未写任何东西。
- **磁盘**：开始 96G 已用，结束 96G，未触发 ≥100G 门限。
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-verify-es/`：`PROOF-NOTE-7.md`（本文件）、`gates7.sh` / `gates7.log`（已更正 occlusion 条目）/ `occlusion2.log` / `occlusion.json` / `p8-extract.json` / `p8-compare.json` / `census.json` / `boxtitle/` / `spill/` / `edge/` / `freeze/` / `pg-1.png` … `pg-8.png` / `p5-zoom.png`。
- **建议下一步**：协调员定 F1 修法（缩短俄文或调行距/字号）→ 单版重建 → 全部门禁 → 再派一轮全量重校（SOP §8.4）。修后须复核 P5 分隔线与框底的几何关系，并把“分隔线 vs 内容框交叉”补进共享工具检查（occlusion/spill 均未覆盖此类）。
