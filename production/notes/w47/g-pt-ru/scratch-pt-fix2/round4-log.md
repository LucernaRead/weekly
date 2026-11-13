# W47 pt 核心版第 4 轮返修续做记录（builder，2026-11-10 22:11–22:40 UTC）

对象：`production/2026-w47/core-pt/`（2026-w47-pt-zh-cn，VOL.4，刊期 2026-11-16..22）
范围：只跑完第 4 轮渲染闭环；源头（D1/O1/O2/O3/D2）本轮未改任何源码。

## 0. 开工复探（22:11，全部通过才继续）
- core-pt 写探针 `.probe-r4.txt` 成功；`git hash-object -w` rc=0，返回 db093c21298ed98580259168d8cf0f79a97c402d；探针已删。
- 复核：SVG 8 个均为 22:07–22:08 第 4 轮版；p8 SVG 内含 `131. A`；text.md 中 `7h15` 0 处、`às 7h` 2 处；P8 card 仍为第 3 轮旧版（21:40），PDF 仍为第 3 轮版（21:41/21:43）——与协调员 22:10 所述一致。
- `df`：`/home/hatch` 150G、已用 103G、可用 47G（69%）；`/` overlay 7.5G 可用 7.3G。未满。

## 1. render.py（只跑一次，成功）
- `tools/venv/bin/python render.py` rc=0，耗时 ~255 秒，无 CairoSVG 写错误、无 Errno 122/EPERM。
- 8 张 cards 22:12–22:13 全新（含 p8-avaliacao.png 22:13，1,358,045 字节）；印刷 PDF `A-Lucerna-VOL4.pdf` 22:16，25,311,662 字节（第 3 轮 25,311,660；+2 字节与 Q131 B→A 一致）。
- 日志：`render-r4.log`。

## 2. webpdf.py（成功）
- rc=0；`A-Lucerna-VOL4-web.pdf` 22:19，1,571,251 字节（<7MB），文字层 44,482 字节；539  distinct chars，4 字体族裁切。
- 日志：`webpdf-r4.log`。

## 3. gates_core.py：16/16 PASS（rc=0）
- 含 VOL.4/刊期、页脚 8/8、基线零碰撞、页框零穿越、P6 图表标签覆盖 0%、29 译注词头全存活、8 金句各 2 次、读者园地披露、5 图+出处、P1 头条 41 字符 ≤56。
- 日志：`gates-r4.log`。

## 4. 三工具
- `occlusion_audit.py`：自检 6 类全触发、干净对照静默；当前 SVG **0 flags**（`occlusion-r4.log`）。
- `p8.py extract --total 150`：**150/150**（`p8-r4.log`）。
- `freeze.py baseline`：工具自报 0/8（已知重定向局限：副本写进 `build-copy/svg/` 而非 `--out/svg/`，与第 3 轮记录一致）；**直接 sha256 比对副本与交付 SVG：8/8 一致**；工具自检“shipped core SVGs unchanged”（`freeze-r4.log`，`freeze-r4/`）。

## 5. 第 4 轮机械复核（round4-check.py = round3-check.py 原样复用，ALL PASS，rc=0）
- D1：print/web 均无 `7h15`；`Singapura × Brasil, às 7h` print 与 md 各恰好 2 处。
- O1：P6 时间线含 `Primeiro dia do Enem: redação, Linguagens e Humanas.`，旧串已无。
- O2：无 `por volta de 1830`；P1 图注含 `Voyage pittoresque dans le Brésil, Paris, 1835`。
- O3：Gary Todd 出处仍在。
- 题号 1–150 在 md 中完整无缺重；8 金句各 2 次；长散文句 66 条在 SVG 中 0 缺失。
- 日志：`round4-check.log`；全文提取：`print-r4.txt`（44,477 字节）、`web-r4.txt`（44,482 字节）、`print-r4-layout.txt`（867 行）。

## 6. print/web 文字层一致性
- 词级多重集 diff = **0**（各 7,263 词）；5 字节差 = web 多 5 个空行（提取引擎 artifact，与第 3 轮一致）。

## 7. P8 答案键：印刷版 vs .text.md 逐键比对（113–150，共 38 项）
- 大写选择键 113–132、145–149：print（plain 与 -layout 双模式）与 md **0 不符**；小写配对键 141.c / 142.d / 143.b / 144.a 在 print 中均存在；造句/翻译 133–140 与 md 一致；150 为范文标记。
- **Q131：SVG `131. A`；print 文本 `131. A` ×1、`131. B` ×0；web 文本 `131. A` ×1；P8 渲染图目视 `131. A – 周六他看帕尔梅拉斯×弗拉门戈`；web P8 渲染图裁剪目视同样 `131. A`。已印出。**
- 印刷题干中无内联答案键（8 个 SVG 中 `(A)`–`(D)` 出现 0 次；答案只在 P8 Respostas 区）。
- P8 答案字号实测：pdftotext -bbox 答案区词框高 **10.12pt**（≥ §1.1 下限 9.75pt，与第 1 轮一致）。

## 8. 全量自查（第 4 轮独立重做，不采信“全部正确”现成结论）
- **全文精读**：.text.md 535 行逐行读完；长句 SVG 存在性 66/66（见 §5）；layout 文本与 md 词级核对，仅家具/徽章/填空线类 token 差异（预期内）。
- **150 题逐题独立验算**：逐题按题面/原文/图表重算（非对照答案抄录），1–112 与 113–150 全部通过。重点 P8 113–150 逐项重算：
  - 113 A（20 日全国假日）、114 A（祖比）、115 B（周五）、116 A（12 月 6 日）、117 B（帕尔梅拉斯）、118 A（11 月底前）、119 A（15 日）、120 B（5 小时）、121 B（14.759 设全国假日）、122 A（总比分 3 比 1）、123 B（点球 5 比 4）、124 B（Norris）、125 A（第 36 轮周六 21 日）、126 B（卡波耶拉定义）、127 A（10 个工作日）、128 A（阿拉戈斯）、129 B（萨尔瓦多）、130 B（卡波耶拉活动）、**131 A（周六看帕弗之战；短文原句“No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão”）**、132 B（非官方答案）、133–136 造句、137–140 翻译、141 c / 142 d / 143 b / 144 a、145 A（Mané）、146 A（sexto）、147 A（quinto）、148 A（na internet）、149 A（obrigado）、150 范文。
  - 易错点复核：Q58 16h30 mais cedo ✓；Q83–85 工作日计数独立算得 16–30 日：工作日 10 天（16,17,18,19,23,24,25,26,27,30）、周末+假日 5 天 ✓；Q91 周末假日不计 ✓；Q108 saíram（过去时复数）✓；Q109–112 虚拟式将来 sair/for/tiver ✓；Q125 轮次：35 轮止于 18–19 日，21 日为 36 轮 ✓。
  - 范文独立数字数：**88 词**（80–100 区间内）。
  - 日期星期经 `date` 核验：11 月 8 日周日、14 日周六、15 日周日、16 日周一、17 日周二、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、27 日周五、30 日周一、12 月 6 日周日——与刊内全部一致。
  - D1 事实独立复核（本轮新查 CBF 官网）：cbf.com.br 征召通稿（2026-10-29）：“日本 14 日 7h15，17 日 7h，新加坡国家体育场”；多家独立媒体一致。刊内两处 `às 7h` 正确。
- **8 版看图**：print PDF 每页 110dpi 渲染（`pages-r4/pg-1..8.png`，2235×3094）逐版目视：无溢出、无重叠、无压页脚、5 图齐全且有出处、页脚/页码 8/8。P3/P5/P6 中部大面积留白与第 1 轮记录一致（版式疏朗，非违规）。
- **结论：本轮全量自查零问题。**

## 9. §1.1 逐项实测复核（首次明确认定）
| 项 | 实测 | 结论 |
|---|---|---|
| 纸色 #fbfaf6 | 每页恰好 1 个整版底色 rect，共 8 处；无旧奶油纸 #f5efe0/#faf3e3 | PASS |
| 禁用金色 | 无 #d4af37/#c9a227/#b8860b；#f6e08e 9 处均为书衣绿底副标题（允许用法） | PASS |
| 禁用近黑底 | 无 #000000/#111111/#1a1a1a；栏目条为书衣绿 #37402f | PASS |
| 禁用双线框 | 8 页 stroked rect 共 0 个，无外框双线 | PASS |
| 拉丁 Newsreader | 拉丁目标语文本 1,231 处 Newsreader；刊头 UnifrakturMaguntia 1 处；中文讲解 Noto Sans CJK SC、中文标题 Noto Serif CJK SC | PASS |
| 全角空格分隔 | 页脚 8/8 为 `A Lucerna　葡萄牙语周报 VOL.4　LUCERNA PORTUGUESE WEEKLY`（U+3000）；栏目条标题同样（P4 `A SEMANA DO FUTEBOL　足球周历` 等）；每页全角空格 12–18 处 | PASS |
| 徽章颜色精确匹配 | 逐个核对：A2=#5c6e30、B1=#46581f、B2=#37402f，填色与标签 100% 对应（P1–P8 全量；首个 #37402f 为栏目条底，非徽章） | PASS |
| 字体字重/字号 | 答案 10.12pt ≥ 9.75pt 下限（§7）；其余阶梯沿用第 3 轮版，未改动 | PASS |

## 10. 非阻塞观察（旧版即有，本轮未改；请协调员定夺是否另立项修）
1. **选择题选项流式折行**：排版引擎将选项作流式文本折行，多处选项在中间断开，如 P8 Q123 `C. 6 a / 5`、Q125 `B. / domingo 22`、Q131 `B. / ao Enem`、Q132 `B. o gabarito / extraoficial`；P1 Q7 `A. no / dia 15`、P2 Q11/Q12、P3 Q29、P4 Q49、P6 Q89 同 pattern。§1.1 排字有“选项不在中间折行”一句；但此为全期系统性引擎行为（第 3 轮版已相同，第 1 轮独立校对 8 页目视通过），选项文字完整、分隔符清晰、无歧义；改动需动排版引擎、超出本轮“只跑完渲染闭环”范围，故记录在案、不阻塞。
2. P4 赛程斑马纹用 `#f4efe0`/`#efe8d2`（与 §1.1 侧栏浅底 `#f0eee5` 同色系、非等值）。表格斑马纹，非侧栏小框；不属禁用色。
3. P1 数字框 `( 2023 年立法…` 左括号后有一空格；P5 计划第 5 条中文译注右括号 `）` 独自折行。纯排版微瑕，旧版即有。
4. 其余 §1.1 之外未发现新问题。

## 11. 未做事项（硬约束遵守）
- 未改 `tools/p8.py`；未跑 insert.py、node lint.mjs --write、git push/add/reset/stash；未提交任何东西；未碰 W43/W45/W46；未改 core-pt 内任何源码（本轮 0 处源码改动）。
- 工作产物只在 `hidden_files/w47/scratch-pt-fix2/`（未覆盖第一轮 `scratch-pt/`）。
- 写失败 0 次：render/webpdf/freeze 全程无 EPERM/EDQUOT/WRITE_ERROR；唯一工具异常是 freeze 工具自报 0/8（已知重定向局限，直接 sha256 8/8 已代证）。
