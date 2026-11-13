# GATE-LOG — 2026-W47 zh-cn-fr re-proof（独立复校，全部自跑）

复校员：独立复校员（与 fix1、原 proof1 不同人）。日期：2026-11-11。仓库：`~/workspace/weekly-git`。
工具：Python 一律 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）。所有输出在 `hidden_files/w47/scratch-reproof-zh-cn-fr1/`。

## G0 开工探针与 SHA 核对 — PASS

- 探针：`cd ~/workspace/weekly-git && echo test | git hash-object -w --stdin` → rc=0（注意：在 `~` 下跑会报 `fatal: not a git repository`，必须在仓库内跑）。scratch 内真实写文件成功（`probe.txt`）。
- 三 SHA 核对（均为协调员 18:10 UTC 实测值，开工逐项核对，全部相符）：
  - 印 PDF `Lucerna-VOL4-FR.pdf` SHA `097c8818a56d955e509d5beeae51b3ef6b879b582003f3192dccb82905c68b8e` / 42,504,769 B ✓
  - 网 PDF `Lucerna-VOL4-FR-web.pdf` SHA `467527f24998e7af8738670b8b99af3d444893f950b198e3dabf077ef9ac0573` / 2,663,732 B ✓
  - 文 `2026-w47-zh-cn-fr.text.md` SHA `e125a9d1b75bb02ca922dcbcb73ac012714270d1e3c3ec22c50a68d1aecc12e6` / 51,821 B ✓
- 开工快照：`snapshot-start.sha256`（46 个文件）。
- 缺口：`hidden_files/w47/briefs/brief-coordinator.md` 不存在（`hidden_files/w47/briefs/` 目录本身不存在）；已读 repo 根 `SOP.md`（§1.1、§8.4）与 `~/workspace/weekly-git/AGENTS.md`。

## G1 run.py 重建 — PASS（rc=0，TOTAL 150）

- 方法：`cp -r` 整版目录到 scratch 内 `rebuild/`（删 `__pycache__`），`sed` 把 5 个 content 文件 + `render.py` 的硬编码生产 OUT 替换为 scratch 绝对路径；`grep -rn "weekly-git/production" rebuild/ --include="*.py"` 返回空（grep rc=1）；`cd rebuild && PYTHONDONTWRITEBYTECODE=1 <tools/venv/bin/python> run.py`。
- 结果：rc=0，TOTAL **150**；分级 A2 56 / B1 69 / B2 25；按页 1:10、2:18、3:18、4:18、5:18、6:18、7:12、8:38；题型 完成句子 68、单选 50、词汇配对 20、完形单选 11、写作 1；P7 预告条底 2588.78、P8 keys 流底 2537.2（与声称存活值一致）。
- 证据：`run-rebuild.log`、`run-rebuild-logged.log`（wrap 日志版重建，亦 rc=0、TOTAL 150）。

## G2 SVG 重建 8/8 字节一致 — PASS

- 重建 SVG 与生产 `svg/` 逐个 sha256 比对：**8/8 IDENTICAL**（第一轮与带 wrap 日志的第二轮均 8/8 一致）。
- 证据：`svg-rebuild-compare.log`。

## G3 freeze baseline（核心）— PASS（8/8）

- 命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-zh-cn --core-svg production/2026-w47/core-zh-cn/svg --out <scratch>/freeze`
- 结果：rc=0，**8/8** byte-identical，core 完整性复核通过。
- 证据：`freeze/`、`freeze-baseline.log`。

## G4 freeze diff --strict-cjk — PASS（新增 CJK 0）

- 结果：rc=0；每页新增 CJK **0**。
  - p1 +47/-45（CJK 886→870）、p2 +52/-52（1065→1060）、p3 +38/-38（864→859）、p4 +43/-43（772→767）、p5 +37/-37（969→964）、p6 +42/-41（912→907）、p7 +107/-105（753→742）、p8 +201/-205（1125→1118）。
- badge：p1 新增串含 `TEXTE CHINOIS　EXPLICATIONS EN FRANÇAIS` ✓。
- 证据：`freeze-diff.json`、`freeze-diff.log`。

## G5 几何遮挡审计 — PASS（0 flags）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py --core production/2026-w47/core-zh-cn/svg`
- 自检 OK（6 类全触发、干净对照静默）；版 **0 flags**，core 0，NEW vs core 0。
- 证据：`occlusion.json`、`occlusion.log`。

## G6 p8 extract + compare — PASS（150/150，CLEAN，keydiff []）

- extract：核心与版均为 **150/150**。证据：`p8extract-core.json`、`p8extract-ed.json`（+ `.log`）。
- compare：**CLEAN**，missing=[]，extra_count=0，uncertain=[]，**keydiff=[]**。证据：`p8compare.json`、`p8compare.log`。

## G7 印/网文字层逐页差 — PASS（p1–p8 全部 0 diff）

- 方法：`pdftotext` 逐页提取印 PDF 与网 PDF 后 `cmp`。
- 结果：p1–p8 **全部 0 diff**。
- 证据：`text-extract/print-p*.txt`、`web-p*.txt`。
- 注：P6 图注 `Chiffres :国家邮政局` 在印/网提取中一致无空格；经 PROOF-NOTE §10① 核实为空格 advance（5.0 svg px）真实存在、pdftotext 断词阈值 artifact，非缺空格；核心同款构造。

## G8 P8 最小字号 — PASS（9.975pt ≥ SOP §1.1 底线 9.75pt）

- 方法：PyMuPDF 测全部 span。
- 结果：P8 最小 **9.975pt**（360 个 span；另有 13.125pt×299 等）；fix1 声称 9.98pt 是同一值的四舍五入。其余页最小：P1 10.5、P2–P5/P7 11.625、P6 12.75。
- 证据：`p8-minfont.log`。

## G9 D-1～D-4 独立量测 — PASS（全部 ≥ +5px）

- 脚本：`ink_check.py`（PIL 真墨：版内 `svglib` 的 `_pil` / `text_w`，按基线 y 分组，`getbbox(anchor='ls')`；`sys.dont_write_bytecode=True`，只读生产 SVG）+ `pdf_pixel_check.py`（PyMuPDF 300 dpi 渲染交付印 PDF，暗像素 min(R,G,B)<150）。
- 结果：
  - D-1（`content12.py:47`，L52 `tsize=21`）：PIL 墨右 942.5 / PDF 像素 943.0 / 框右 961.0 → 余 **+18.5 / +18.0**（声称 942.0 / +19.0；0.5–1.0px 跨方法差为渲染/舍入噪声）。基线 y=1145.3。
  - D-2（`content12.py:88`，18pt）：PIL 1848.5 / PDF 1849.3 / 框右 1862.0 → 余 **+13.5 / +12.7**（声称 1848.5 / +13.5）。基线 y=1252.0。
  - D-3（`content12.py:187`，L191 `tsize=22`）：PIL 1397.0 / PDF 1397.0 / 框右 1411.5 → 余 **+14.5 / +14.5**（与声称完全一致）。基线 y=236.0。
  - D-4（`content12.py:50`，`le film 《试探》 sort`）：单基线；advance **349.9** ≤ 内宽 386.5，余 **+36.6**；墨右 907.0（PIL）/ 906.2（PDF），框 961.0，余 +54.0 / +54.8；wrap 日志 `nlines=1`。
- 裁图目视：`clip-D1-title.png`、`clip-D2-bouclage.png`、`clip-D3-title.png`、`clip-D4-filmline.png` 均已目视确认：单行、行尾与框右缘之间有明显空隙。
- 证据：`ink.log`、`pdf-pixel.log`、4 张 clip 图。

## G10 其余声称存活项 — PASS（全部复核一致）

- P4 注释框：`content34.py:134` gloss 首行墨底 600.9 vs 框底 792.2，余 +191.4（`ink.log`）。
- P8 keys 流底 2537.2、P7 预告条底 2588.78（`run-rebuild.log`）。
- ABSTRACT.txt 333 B，尾部 `re.\n` 有尾换行。
- 核心 D4/D5 措辞：核心 `content34.py:130` / `content12.py:42` / `content34.py:131` 与版内逐字一致；版 `content34.py:211` Q56 与核心一致（仅 `instr` Fill in → Compléter）。
- badge：见 G4。
- “仅 P1/P2 两页 SVG 变化”：**无法验证**——版目录未跟踪、无前版基线、无该版 fix1 scratch（见 PROOF-NOTE §0.2）。当前态 SVG 重建 8/8 一致（G2）。

## G11 150 题逐题手验 — PASS（无 key 与题干错配）

- 方法：`dump_reg.py` 在 rebuild 副本中包住 `Flow.ex` 与 `Flow.match_set`，重跑 5 个 content 文件 → `reg-dump.json`（135 次调用展平为 150 条 REG，顺序与 key 与 REG 完全一致）+ `reg-flat.json/txt`（530 行）。
- REG key vs P8 印刷 key：仅 Q150 不同——REG `(开放题，范文如下)` vs P8 `✓`；核心 P8 同为 `✓`，属写作题既定格式，非不符。
- Q1–Q150 已逐题读完题干+选项+key+法语 note 并核对：未发现 key 与题干错配（无 en Q73 式三源同错）。抽查要点见 PROOF-NOTE §5（Q56/Q48/Q73/Q67/Q126/Q76/Q77/Q68/Q114/Q115/Q118、Q141–Q146、Q20–Q24、Q89、Q93–Q95、Q97–Q100）。
- 证据：`dump_reg.py`、`reg-dump.log`、`reg-dump.json`、`reg-flat.json`、`reg-flat.txt`。

## G12 全文通读 — PASS（2102 行，8 页逐页）

- `.text.md` 2102 行读完；P1–P8 内容、数字、比分、日历、词卡、诊所、金句 8 条（逐条核对为本期正文原句）、读者园地（示例信标注 + VOL.3 预告兑现说明，SOP §10）、下期预告 VOL.5 均与题目/正文一致。
- 日期核验（`TZ=Asia/Shanghai date -d`，2026-11-11 实测）：11 月 8 日星期日、11 月 9 日星期一、11 月 15 日星期日、11 月 21 日星期六、11 月 22 日星期日——与文中全部星期表述一致。
- 写作范文实测 **138 字（含标点）**，在 120–180 字要求内；note 的“138 caractères”准确；范文在 `content8.py` MODELO（L96 起多行拼接）与 `.text.md` 中一致，且印/网 P8 文本层均含该范文。

## G13 外部事实核验 — PASS（公开来源，2026-11-11 检索）

- 农历：2026-11-22 = 农历十月十四；小雪交节 11 月 22 日 15:23 北京时间；第 20 个节气、冬天第 2 个；初候虹藏不见 11 月 22–26 日 ✓（bothmoons 等）。
- 深圳读书月：第 27 届，11 月 1 日开幕，主题“悦读深圳 阅连世界”；七馆全名；11 月 7 日国际美术馆日；文化馆之夜 ✓（新浪深圳 2026-11-02、21经济网 2026-10-27/28）。
- 邮政局双 11：2025 年 10 月 21 日—11 月 11 日（22 天）揽收 139.38 亿件，日均 6.34 亿件，单日峰值 7.77 亿件 ✓（新华社/国家邮政局 2025-11-12、英文 gov.cn 2025-11-13）。
- S16：四分之一决赛 IG 3-1 TES、GEN 3-0 LYON、BLG 3-0 DK、T1 3-1 KC（北京时间 11 月 4–7 日）；半决赛 GEN 3-0 IG（11 月 8 日早上 6 点）、BLG 3-1 T1（11 月 9 日）；决赛北京时间 11 月 15 日凌晨 3 点、纽约巴克莱中心、BO5 ✓；BLG 首支在全球总决赛 BO5 战胜 T1 的 LPL 战队（T1 此前对 LPL 的 BO5 13 连胜，追溯至 S3 决赛）✓；GEN 瑞士轮 3 胜 0 负（1-0 胜 IG、1-0 胜 HLE、2-1 胜 LYON）、小局 10 胜 1 负 ✓；BLG 瑞士轮 3 胜 2 负、生死战 2-0 胜 HLE ✓；IG 上次在国际赛事胜 LCK 是七年前 ✓。
- 《试探》：定档 2026 年 11 月 21 日，路阳/王红卫监制，侯逍遥执导，冯绍峰、陈雨锶、李梦主演；钢琴家丁伯阳（冯绍峰），女友万影（李梦）失踪，马娅（陈雨锶）✓（北方网 2026-10-27/11-06）。小注：来源多称“悬疑惊悚”，文中“悬疑犯罪片”的“犯罪”略有拉伸，Q65 答案无歧义。
- 《白衣逆行者》：刘德华主演，原定 2026 年 11 月 6 日上映，11 月 6 日当天无预售、无排片，豆瓣改期“2027（未定）”，片方未正式宣布 ✓（RFI/工商时报/明报 2026-11-06/08、联合早报）。小注：来源多用“疑撤档/悄然撤档”，文中作事实陈述，措辞强度注记，非事实错。
- 未单独再查：《珠穆朗玛：云中彼岸》11 月 6 日艺联专线、《我们仅有一次的人生》宋佳/文淇 11 月 7 日。

## G14 孤儿扫描 — 观察项（宽口径 10，窄口径 0；不可写成“0 已复现”）

- 方法：`rebuild/svglib.py` 的 `wrap()` 加日志补丁（只写 `wrap-log.jsonl`；重建后 SVG 仍 8/8 一致）+ 核心副本 `core-rebuild/` 同法（`core-wrap-log.jsonl`）；分析脚本 `orphan_analyze.py`。
- 宽口径（多行 wrap 末行仅含一个空白分隔词（无 CJK）= A；末行仅 1 个 CJK 字 = B；末行仅标点 = C）：版 **A 8 + B 2 = 10**，C 0；核心 **A 11 + B 2 = 13**，C 0。
- 版 10 项中 3 项与核心逐字相同；其余 7 项为法语讲解层，核心有同类英语版。完整清单：`orphan-ed.log`、`orphan-core.log`、`orphan-scan.log`。
- 窄口径（`f.box` 单行意图的盒条目；盒宽 wrap 88 个、多行 38 个）：**末行孤词的盒条目为 0**；D-4 电影行单行。fix1 的“0”仅在盒条目口径下成立。
- 定性：10 项均为核心已定稿的同类版式（核心更多，13 项），SOP §1.1 无禁孤行末词规则，几何门为 0，可读性未受损。**非阻塞观察项**，缺陷清单仍报 (a)，交父代理裁断。

## G15 8 页全页目视 — PASS（无新缺陷）

- 交付印 PDF 150 dpi 渲染 `page-p1.png`…`page-p8.png` 逐页看完：无溢出/重叠/压页脚；图片与出处均正常（P1 快递柜、P2 山谷、P3 红叶、P4 老照片、P5 爆米花桶、P7 毛笔、P8 写字均为 CC0 资料图，图注完整）。
- 另：P4 栏 2 顶行 `半决赛3比1打赢T1。` 经 SVG 行表核实为 `content34.py:131` 段落末行（分栏接续，栏 1 y=1002.3 起 → 栏 2 y=224.0），非重复行，同核心版式（证据：`p4-topmid-crop.png`）。

## G16 生产零写入核对 — PASS

- 重建后中期：`sha256sum -c snapshot-start.sha256` → **46/46 OK，0 不符**（`snapshot-check-after-rebuild.txt`）。注：曾有一次误在 `svg/` 子目录下跑校验导致全 FAILED，那是路径错误，之后在仓库根重跑正确。
- 收工最终：`sha256sum -c snapshot-start.sha256` → **46/46 OK，rc=0**（`snapshot-check-final.txt`）。
- `git status`：该版目录仍为未跟踪（`?? production/2026-w47/2026-w47-zh-cn-fr/`），与开工状态一致；无新增的非预期修改。

## 汇总

| 门 | 结论 |
|---|---|
| G0 开工/SHA | PASS |
| G1 run.py 150 | PASS |
| G2 SVG 8/8 | PASS |
| G3 freeze 8/8 | PASS |
| G4 freeze diff CJK 0 | PASS |
| G5 occlusion 0 | PASS |
| G6 p8 150/150 CLEAN | PASS |
| G7 印/网逐页 0 差 | PASS |
| G8 P8 字号 9.975pt | PASS |
| G9 D-1～D-4 量测 | PASS（余量 +12.7～+54.8px） |
| G10 存活项 | PASS（“仅 P1/P2 变化”无法验证，见 PROOF-NOTE §0.2） |
| G11 150 题手验 | PASS |
| G12 全文通读 | PASS |
| G13 外部事实 | PASS |
| G14 孤儿扫描 | 观察项（宽 10 / 窄 0；核心 13） |
| G15 全页目视 | PASS |
| G16 零写入 | PASS（46/46 OK） |

**缺陷清单：(a) 零阻塞缺陷。** 观察项与小注见 PROOF-NOTE §8、§10、§11。
