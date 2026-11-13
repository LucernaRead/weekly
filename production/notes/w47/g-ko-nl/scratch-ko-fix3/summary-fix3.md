# W47 KO core — 第三轮返修工作记录（fix3，run 7–9，2026-11-10/11）

> **⚠ 停手记录（任务硬性约束）：本轮在 run 9 门禁收尾时写 `svg-hashes-run9.txt` 遇到 `tee: Disk quota exceeded`，按任务要求立即停手，未硬锤重试。** 此时 `df` 显示 /home 仍有 46G 可用（70% 已用），属配额层面的单次写失败，非磁盘写满——前序所有构建/渲染/门禁写文件均正常。停手时状态：run 9 印刷版 + 网页版已建成，机械门（occlusion 0、p8 150/150、check_core 0/0/0、check_gloss 与 run 6 逐字节同、print/web 文字层逐字节同）全过；**未完成：KIT 文字改写（缺陷 3 准确表述 + 修复记录 + Output files 更新到 run 9）、run 9 freeze baseline、P4/P6/P7 run-9 渲染图复看。** 详见末节「未完成清单」。run-9 SVG 哈希见下（tee 写文件失败，但哈希已打印在终端输出中，逐字抄录于此）。

## 成品（run 9，最终）
- Print PDF `Lucerna-VOL4.pdf`：46,232,133 字节，SHA-256 `48c2fa985529bbf9b1cd7afbc351285133ebb5293afa160aa797ca4c57ac1485`
- Web PDF `Lucerna-VOL4-web.pdf`：4,232,753 字节，SHA-256 `c030926848df2832b084e60ad392a3b07b49fe52023a29f9ce4f8170c865bf8d`
- text.md 未变：26,014 字节，SHA-256 `81ebd0a392266c0762df33fb73a8ce1b9bf1d8f6912891e107d74e9341e6e8c0`（与 run 6 一致）
- SVG 哈希（run 9，终端输出抄录）：p1 `c47bc434067fdc90`、p2 `8619ec50796062b5`、p3 `b447a559c6f8d61d`、p4 `0524233d9624bbbb`、p5 `09f7fc23850a1deb`、p6 `d45b03557f02f47a`、p7 `e6908156fe45e85f`、p8 `e88f7d421d621f92`（完整见下方工具输出记录；其中 P1/P2/P3/P5/P8 与 run 8 逐字节同，P4/P6/P7 为本轮改动所致）

## 缺陷 1 — 左右版心边距（修完）
- 改动：`bslib4.py`：`MX = 65 → 88`（§1.1 66pt），`CW = 434 → 422.5`（`(1774 − 3×28)/4`，与 core-en/ja/fr 同值），`RIGHT = 1885 → 1862`。`content12.py:32` 头条行宽 `1358 → 1323.5`（= 3×CW + 2×GUT，3 栏跨度）。
- 验证：8 页 SVG `<text>` x 范围逐页均为 88.0–1862.0；刊头线 `x1=88 x2=1862.0 y=420`；上边距未动（栏目条顶 y=72）；下边距未动。构建 0 OVERFLOW / 0 TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；分面 10/18/18/18/18/18/12/38）。P1-headline flow 仍 1814/1828（band 下移未动 flow 起点 hy=580）。

## 缺陷 2 — 刊头三色蛾（修完）
- 改动（按全周 11 版共享实现，不发明）：`assets/lucerna-moth.svg` 从 core-it 复制（md5 `c22d616d8391af2caab71187097a8094`，与全部 11 版一致）；`svglib.py` 加入与 core-it svglib.py:134–147 同形的 `moth(p, cx, y, w=96)`（内联 SVG，384:284）；`content12.py`：刊头线 `y=405 → 420`，加 `moth(p, 975, 420)`，band `y=424 → 470`、band 内两行文字 `478/522 → 524/568`（与 core-it/en 同几何；蛾子上沿 384.5、下沿 455.5，副标题墨底 ~376、band 顶 470 均留空隙——**band 下移是共享布局本身的做法，不是因为蛾子需要**，ko 原 band y=424 与线 y=405 仅隔 19px、放不下 71px 高的蛾子）。
- 验证：P1 SVG 嵌套 `<svg x="927.0" y="384.5" width="96" height="71.0">`；印刷版像素实测：蛾子墨迹 x 971–1059（中心 svg x≈974，页心 975）、y 398–444，线在 y≈420 当中穿过，band 顶 470.3；渲染图目视：蛾子居于线中、无重叠；P1 其余元素无位移。

## 缺陷 4 — ABSTRACT.txt 日期去空格（修完）
- 改动：`ABSTRACT.txt`：`11 月 19 日 → 11月19日`、`11 月 22 日 → 11月22日`（两处）。纯文本改动，未重渲文本层以外内容；`grep "11 月"` 得 0。text.md 不受影响。

## 缺陷 3 裁定 — 正文色（不修颜色；KIT 文字改写未完成，见末节）
- 核实（为 KIT 准确表述 grounding）：SVG 全文 `#3a3631` 8 页均为 0 次；正文/题干用 `#302c28`（P1–P8 计 816 处级）。core-en / core-ja 的 `svglib.py` 同样只定义 `INK = "#302c28"`、无 `#3a3631`——与 core-en/ja 共享实现一致，裁定成立。**KIT 该句改写未做**（停手时未完成，见末节）。

## 边距修复的连带修复（run 8→9，缺陷 1 的直接后果）
- run 8 自查发现：硬编码旧跨度 `1388`（= 旧 3 栏跨度 1358 + 30）在新边距下侵入第 4 栏——**P7 泡菜照片**（`content7.py:110`，88–1476）盖住了第 4 栏「이번 주의 틀」「독자의 편지」两框左缘 36.5px（标题「독자의 편지」被盖掉「독」字，句式行「句」被盖），渲染图目视确认；occlusion_audit 未报（`<image>` 不在该工具遮盖检查之列，工具盲区，已记录）。
- 同类（无文字被盖，但跨出 3 栏跨度）：**P6 对照表** `tw=[300,544,544]` 合计 1388，右缘 1476，侵入第 4 栏 36.5px；**P4 梯形图** `bw=320/gap=26` 合计 1358，第 4 框右缘 1446，侵入 6.5px；另 P4/P6 图注行宽 1388。
- 修复（run 9）：P7 照片与图注宽 → `span_x(0, 3)[1]`（= 1323.5）；P4 梯形 `bw=312、gap=25`（合计 1323，右缘 1411）、图注行宽 → 1323.5；P6 表 `tw=[300, 512, 511.5]`（合计 1323.5）、表注行宽 → 1323.5。run 9 构建 0 警告；复扫跨栏：除全宽 band/页脚外无 straddle。
- run 8 还暴露 1 个新孤儿（窄栏重排所致）：P7 读者园地 `lko` 段末行单剩「이어져요.」（check_core SHORT-TAIL）。修复（run 8）：该段换行宽 `CW-44=378.5 → 340`（文字一字未改；仍 4 行，框高公式同步改宽，`lh` 数值不变，P7 col3 ends 仍 1805.7）。run 8/9 check_core：orphan issues 0。

## 机械门（run 9，最终态；除 freeze 外全部实跑）
- 构建 run 9：exit 0，0 FLOW OVERFLOW / 0 HEAD TOO WIDE，TOTAL 150。
- occlusion_audit：0 flags（自检 6 类全触发，干净对照静默）。
- p8.py extract：150/150（`--p8 svg/p8-siheom.svg --total 150`）。
- print/web 文字层：49,376 字节，逐字节一致（`cmp` 通过）。注：run 9 相对 run 8 的 49,362 仅为 pdftotext 断行位置变化，字符多重集差为空（无一字增减；系 P4 梯形移位致 pdftotext 块排序变化）。
- check_core：gloss fails 0、P7 金句 8/8 verbatim、orphan issues 0、日期全对。
- check_gloss：10 项，与 run 6 日志逐字节相同（已裁定债务 c）。
- freeze：run 8 实跑 baseline 自报 0/8（已知重定向局限：副本进了 `freeze-run8/build-copy/svg/`），**直接 sha256 比对 build-copy 产物与在仓 SVG：8/8 逐字节同**（run 8 哈希见 `svg-hashes-run8.txt`）；run 9 freeze 未跑（停手）。
- P8 最小字号：run 8 实测 9.975pt（162 spans，PyMuPDF，y≥976.5pt）；run 9 的 P8 SVG 与 run 8 逐字节同（`e88f7d42…`），该实测继续有效，未重跑。
- 150 题键复核（run 8）：P8 SVG 逐条解析 150 键（1–150 无缺重），与登记表逐题比对——149 项一致，唯一差异为 150 号开放写作题（登记键「(开放题，范文如下)」vs 印「✓ 范文见本版 H 区（169字）」，与 run 6 同格式，非实质不符）。字符多重集 run6→run8：差集为空（18,100 字），即窄栏重排只改断行、未改一字。
- §1.1 逐项重测（run 8 SVG）：纸 `#fbfaf6` 每页 1 处（P4/P6 各另 3 浅底框，共 14）、旧 `#f7f1e2` 0；`#2c2822/#b3a06a/#a4553a` 皆 0；刊头线唯一一道 y=420 橄榄绿 2px；徽章 rx=2.7 共 138 个；刊头 196px ×1、头条 56px ×1；P8 15.375pt 题干、刊头 196px、头条 56px 保持不动；第一轮 5 处归属保持（웨더아이 SVG 5 处、공단 0 处——run 8 复核时未重跑该项计数，以 run 6/第三轮校对结论为准，字符多重集为空差佐证内容未变）；text.md `___` 23 处不动；check_gloss 10 项不动。

## 8 版渲染图目视（run 8 印刷版，100dpi）
- P1–P6、P8：无溢出、无重叠、无压页脚；P1 蛾子/首字下沉/band/头条正常；P3 단풍 달력框、P4 梯形图（run 8 态，第 4 框右缘 1446 轻越第 4 栏 6.5px，该带无第 4 栏文字）、P6 对照表（run 8 态右缘 1476 越界 36.5px，该带无第 4 栏文字）均在 run 9 已改；P8 答案区三栏 + 照片正常。
- P7（run 8 态）：照片盖住第 4 栏两框左缘（见上），已在 run 9 修复，**run 9 的 P7 图未复看**（停手）。

## 文件清单（本 scratch 目录 scratch-ko-fix3）
- build-run7/8/9.log、render-run7/8/9.log、webpdf-run7/8/9.log、occlusion-run7/8/9.log、p8-extract-run7/8/9.log/.json、check-core-run7/8/9.log、check-gloss-run7/8/9.log、freeze-run8.log + freeze-run8/（build-copy）、svg-text-run8.txt、svg-hashes-run8.txt、print.txt/print8.txt/print9.txt、web.txt/web8.txt/web9.txt、registry-run8.json、work/pg-1..8.png（run 8 印刷版渲染）、work/p1-masthead.png、work/p7-letters.png、summary-fix3.md（本文件）。
- `svg-hashes-run9.txt`：**写失败**（Disk quota exceeded，见卷首）。run-9 哈希已抄录于本文卷首成品节（源自 tee 终端输出）。

## 未完成清单（停手时）
1. **KIT 改写未做**：(a) Round 5 记录 / fixes #9 中「§1.1 palette / 全部边色按色板替换」的说法，改写为准确表述——正文用墨色 `#302c28`，与 core-en/ja 共享实现一致；色板其余项均已替换；`#3a3631` 未引入（缺陷 3 裁定，不修颜色）；(b) 「Deliberately retained」注 (c)(d) 已过时（边距与蛾子本轮已修），应改写/删除；(c) 增加 Round 7/8/9 记录与 fixes #12–14（边距、蛾子、ABSTRACT、P7 照片/P4 梯形/P6 表格连带修复、P7 孤儿）；(d) 「Output files」与「Mechanical gates」更新到 run 9（哈希/尺寸见卷首）。
2. **run 9 freeze baseline 未跑**（直接 sha256 比对亦未跑；仅 P4/P6/P7 SVG 变了，P1/P2/P3/P5/P8 哈希与 run 8 相同）。
3. **run 9 渲染图未复看**（P4/P6/P7 三处连带修复处、及其余 5 版只做了 run 8 目视；run 9 文字层与门禁已过）。
4. `svg-hashes-run9.txt` 文件缺失（哈希见卷首抄录）。
5. 第一轮 5 处归属（웨더아이 5 处、공단 0 处）本轮未重跑计数——字符多重集 run6→run8 为空差、run8→run9 印刷文字层字符多重集亦为空差，内容未变；但严格说计数本身未在本轮重跑。
