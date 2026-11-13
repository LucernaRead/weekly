# GATE-LOG — 2026-W47 pt-ko proof1 机械门实跑证据

- 复校：proof1，2026-11-11；工具：`~/workspace/weekly-git/tools/venv/bin/python`，正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，已核对）。
- 原则：只信自己跑的结果。全部命令在 scratch（`.../scratch-proof-pt-ko1/`，TMPDIR 指到其下 `tmp/`）内执行；源文件未改动。

## §0 身份核对与三 SHA

- 印 PDF `A-Lucerna-VOL4.pdf`：SHA `10c758cf1bab74442e2a4cb54603a9b1a753eb74f8418fe8adb6f4b6c8414fed`，17,185,929 字节 ✔（与任务一致）
- 网 PDF `A-Lucerna-VOL4-web.pdf`：SHA `b1b609fdf3437cd15991f3b4016f182e7a1abf051d0f6422128bd7151f6884ac`，1,394,979 字节 ✔
- text.md `2026-w47-pt-ko.text.md`：SHA `fb9248014654f2b7b4c4ec1e69ebaaa6a56b56b7aa8f2435228a003a8cb72296`，37,797 字节 ✔
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 写探针 OK。
- **与 KIT 的两处不符**（记入 PROOF-NOTE O2/O3）：① KIT 称 occlusion 有 1 个 LINEX flag（P1 graze），本次同工具同 SVG 实跑 **0 flags**，kits 自检（6 类植入均触发、干净对照静默）通过；② KIT 称 P8 答案流止于 y=2458，本次实测最低答案墨底 **y=2551.9**（76 题注，基线 2550.4），仍距页脚线 44px。两处均低于缺陷阈值，底层几何已在 PROOF-NOTE 中如实记录（D2 为其一）。
- 版目录在复校后核查：SVG mtime 仍为 2026-11-11 05:22:18–05:22:37，`find -newermt "2026-11-11 05:40"` 无文件；git 状态仍为 `??`（untracked，未变）。

## §1 gates.py — 16/16 PASS（rc=0，`gates.log`）

结构/数量/引用类 16 项全过，关键项：
- 8 页、8/8 SVG，4 栏结构；图片 5/5 已嵌入 + 署名；`VOL.4 ×9`、`VOL.5 ×3`（另 `VOL.3 ×2`，历史引用）；masthead 行宽 300.4/383.7 ≤1820；P7 末引基线 2292.17（墨底 ≈2297.2），距预告盒顶 2404 约 107px；P8 答案流最低墨底 2551.9（本节 §0 已述）；每周插图 ≥1。
- 页脚：8/8 页脚规则 + 页码；目录页码 2/3/4/5/6/7/8（P1 不编号）；本期日期 16–22 NOV 2026。

## §2 occlusion_audit.py — 0 flags（`occlusion.json` + `occlusion.log`）

- 自检：6 类植入（rule-cross、img-overlap、textbox-spill、title-spill、footer-invade、grid-misalign）全部触发，干净对照静默。
- 实跑 8 页：0 flags。注意：该工具对奶油盒内溢出、框标题溢出、横向溢出、降部溢出是盲的——本复校另行实测（§5–§8），并因此抓到 D1–D4。

## §3 creambox.py 全版扫描（`creambox-all.log`）

- 31 个奶油盒；P7 toolbox 3 盒，最小盒内余量 **+4.5**，最小 desc-clear **−1.5**（模型误报，见 §5）。
- 盒底以下 +32…+44px 的“溢出”6 处（P2/P3/P4/P5 E-VOCÊ 盒、P5 数字盒 `2027.`、P7 `A PALAVRA` 盒）：皆盒下方的下一节标题，非盒内容（§5 PIL 实测确认）。

## §4 框标题逐个实测（PIL 真墨迹，`ink-measure.log` / `ink-measure.json`）

- 31 个框标题：仅 **1 个溢出**（D1）——`A SEMANA EM NÚMEROS` 韩语 gloss 墨右缘 1417.3 > 盒右缘 1411.5（+5.8px）。其余 30 个墨右缘距盒右缘 ≥18px。标题上溢 0 处；页缘溢出 0 处。
- 同法复测 core-pt：标题 `A SEMANA EM NÚMEROS　数字` 墨右缘 −60.5px（余量充足），确认 D1 为本版 gloss 加长所致。
- 200dpi 像素扫描（`pixelscan.py` / `pixelscan.log`，PyMuPDF）：确认 D1（标题带最右墨 x=1413.1，≥+1.6px）、D3（墨底 540.8 vs 盒底 525）、D4（墨底 846.2 vs 盒底 840）；E-VOCÊ 各盒墨底干净。

## §5 盒内末行墨底实测（PIL 真墨迹，§4 同批结果）

- P2/P3/P4/P5 E-VOCÊ 盒、P5 数字盒、P7 `A PALAVRA` 盒的末行（皆纯韩语/数字，无拉丁降部）：墨底分别 ≈876.8（<880）、≈821.6（<825）、≈872.8（<876）、≈779.7（<782.5）、≈508.2（<513）、≈1369.4（<1372.5）。**任务项 (b) 未复现**——creambox 的 desc-clear −1.5 是 0.30×字号余量模型的误报（韩语无降部字母）。
- 同批实测抓到：D2（基线 2327.6 / 墨底 2332.6，盒底 2310）、D3（基线 540.6 / 墨底 540.9，盒底 525）、D4（基线 840.8 / 墨底 846.0，盒底 840）；core-pt 同法复测三处数值完全一致 → 核心携带。
- P7 CARTAS 盒底 y≈1901 墨迹：为整页橄榄绿分隔线（y=1901.5，线宽 2），非文字漫出。

## §6 p8 compare（`p8-extract.json` + `p8-compare.json`）

- p8.py extract：150/150。
- p8.py compare vs core-pt：`CLEAN`，keydiff 仅 **[137, 138]**——两题韩语译文（Q137/138），逐字核对均正确（见 §9）。
- 印版键 = text.md 行内答案 126/126（已解析项）= text.md Respostas 143/143（已解析项）；另 7 项行末项目视核；三源 0 不一致。

## §7 freeze / freeze_direct — 0/8（`freeze-baseline.log` / `freeze-diff.log` / `freeze-diff.json` / `direct-run.log`）

- freeze 工具 baseline 0/8（与 KIT 记录的已知局限一致）。
- 独立复跑：scratch 副本内 `run.py` 两次，两次结果彼此逐字节一致、与交付 SVG 8/8 不同。差异限于坐标 ±1–5.4px（每页 1–5 个数值属性）+ P2/P3/P4/P7 韩语 gloss 换行点差 1 字（同串，P7 多一个 `<text>` 元素）。
- 已排除：交付后源码改动（全部 .py mtime 05:13:48–05:13:49，早于 SVG 构建 05:22；仅 gates.py/make_gates.py 在 05:17）、哈希种子（两次重跑跨进程一致）、路径（freeze 副本与本人副本路径不同但结果一致）、VM 重启（开机 04:25 EST，早于构建）。决定性证据：现字体下 P3 编版行实测 383.28px > 限宽 378.5px——交付时同行必然 ≤378.5px，字体度量在交付后变了。机制未明，记为 PROOF-NOTE O1。

## §8 keycheck 150/150（`keycheck-150.json`）

- 150 题全部手验：150 正确、0 错误；逐题注记见 JSON（Q44、56–59、80–82、85、125、131、137–140、150）。
- 关键核验：Q83–86 工作日算术（16–30 日 = 15 天 = 10 工作日 + 5 周末/假日）；Q125 周六 21 日；Q131 = A（core D2 修复已在）；Q137/138 韩语译文正确；Q150 模范文实测 88 词；Q56–59 mais/menos 逻辑；Q80–82 V/F 与 P5 正文核对。Q44 补词注记见 PROOF-NOTE O5。

## §9 P8 最小字号实测（PyMuPDF）

- 全页最小 span 字号 **10.125pt** ≥ SOP §1.1 下限 9.75pt。KIT 的 10.125pt 数字本次独立实测确认（非配置 px）。

## §10 印/网文字层比对

- 各 8 页、45,562 文本字节、7,030 词；词多重集差 **0/0**。

## §11 弯引号与全角标点扫描

- U+201C/U+201D：4 处，仅 Q139/140 韩语源句，位置与 core-pt 相同，为标准韩语引号；U+2019：0 处。
- 全角 `。` 0 处，`！` 0 处；全角 `，`（U+FF0C）1 处（D8）；U+3001 `、` 4 处（P7 B2 桥列举分隔，SVG 与 text.md 一致，著者写法）。

## §12 外部事实来源

- core-pt 对照：`production/2026-w47/2026-w47-pt-pt/`（core-pt build.py + tables_ko.py 的 SEG 键；D5/D7 的碎片键 `"周六 16" → "토요일 16일"`、`"至 18" → "18일까지"` 各仅 1 处撞点经 `grep -c` 核实；D2–D4 与 core-pt 同法复测数值完全一致）。
- 日历：`date -d` 核验 11-07 六、11-08 日、11-14 六、11-15 日、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-23 一、11-27 五、12-06 日。
- 无其他外部事实引用（内容事实均以 core 文本与版面实测为准）。

## §13 判为非缺陷的项

- (b) E-VOCÊ 末行降部：§5 实测墨底全在盒内，creambox desc-clear −1.5 为模型误报。**未复现。**
- (c) P7 toolbox：§3 + §5 实测干净（§3 数据）；末引距预告盒约 107px。**未复现。**
- (d) text.md E 节 type 标签：P8 SVG 中 번역 ×4；`翻譯`/`翻译` 全版 0 处；`E · Traduza` 为 core 原葡萄牙语节标题。**未复现。**
- (a) 其余框标题：§4，全部 30 个余量 ≥18px。
- Creambox 窗口内 +32…+44px“溢出”：下一节标题，非盒内容（§3/§5）。
- P7 y≈1901 墨迹：橄榄绿分隔线（§5）。
- P7 B2 桥冒号行首：韩语无此禁则，文字完整可读；KIT §6.8 已记 cosmetic，同意。
- U+3001 `、` 4 处（§11）：著者列举写法，一致。
- 弯引号 4 处（§11）：标准韩语引号，与 core 同位。
- P8 答案流墨底 2551.9（§0）：距页脚线 44px，无侵入；KIT 的 2458 数字疑为旧列。
- Q44 补词 `de novembro`（§8）：核心冻结、core-pt 同键，句子正确。接受。
- Q65/Q68 之外的 148 题答案注：无同类碎片键误撞（`\d일:\d` 与 `일까지:30` 式扫描全版仅 D5/D7 两处；全角 `，` 仅 D8 一处）。

## §14 证据文件清单（全部在 scratch `.../scratch-proof-pt-ko1/` 内）

`PROOF-NOTE.md`、`GATE-LOG.md`、`keycheck-150.json`、`gates.log`、`occlusion.json`、`occlusion.log`、`p8-extract.json`、`p8-compare.json`、`creambox-all.log`、`ink_measure.py` + `ink-measure.log`/`ink-measure.json`、`ink_measure_core.py` + `ink-measure-core.log`/`ink-measure-core.json`、`pixelscan.py` + `pixelscan.log`、`freeze-baseline.log`、`freeze-diff.log`、`freeze-diff.json`、`direct-run.log`、`direct-run2.log`、`svg-edition.sha256`、`svg-direct.sha256`、`svg-direct2.sha256`、`direct-diff-summary.txt`、`direct-textdiff.txt`、`print-text.txt`、`keys-compare.txt`、`keys-xcheck.txt`、`make_keycheck.py`、`seg-16-check.txt`、`note65-68.txt`、`colon-glue.txt`、`short-seg.txt`、`p7-y1901.txt`、`font-text-check.log`、`title-markup.txt`、`probe.txt`、`freeze1/`、`direct-run/`（复跑副本）、`view-p1.png` … `view-p8.png`、`crop-p1-title.png`、`crop-p1-flashbot.png`、`crop-p1-masthead.png`、`crop-p2-evoce.png`、`crop-p2-sab21.png`、`crop-p3-weekbot.png`、`crop-p5-evoce.png`、`crop-p6-timebot.png`、`crop-p7-wordbox.png`、`crop-p7-letters.png`、`crop-p8-q65.png`、`crop-p8-q68.png`。
