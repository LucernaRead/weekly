# 第二轮全文复校笔记 — 2026-W47 英文核心版 (en × zh-cn, VOL.4)

- 校对员：独立第二轮（叶子），只读不改，未修改任何 core-en 文件与 tools/p8.py，未跑 insert.py / lint --write，未提交。
- 校对对象：`~/workspace/weekly-git/production/2026-w47/core-en/`（2026-w47-en-zh-cn），印刷 PDF 与 web PDF 各 8 页。
- 结论：**有缺陷，不算定稿**（见下 D9、D10）。D1–D8 返修逐项验证全部通过；其余 146 道题、事实、版面、机械门均通过。

## D1–D8 逐项验证（全部通过）

- **D1（众议院 254–162–19）通过**。成品全文 `252`/`161`/`34 more` 为 0（SVG 文本与 PDF 文字层均核实；仅 KIT §8 修史记录里保留旧数，非读者面）。`254 is 36 more than the majority` 在 P7（content7.py:24）与正文一致，254−218=36。Q7=B、Q82=B、Q83=C、Q87=C（254+162+19=435）、Q120=B、Q130=A 全对。外部复核：californiatoday.com（AP 11 月 8 日晚 9 点 ET：Dem 254、Rep 162、19 未确认）、usnewspulse.com、en.newjinmedia.com、bitcoinversus.tech 均报 254–162–19；另确认参议院 20/33、7 席翻转、州长 5 席翻转（GA/IA/NV/OH/TX）、众议院控制权 AP 于 11 月 4 日 1:24 a.m. ET 宣布、新国会 2027 年 1 月 3 日就职——与 KIT §3 一致。注：political.org 同页显示 252–161–22 为更早的快照（最近一次 call 为 11 月 6 日），AP 实时页现为 Dem 253 / GOP 166（仍在变），均不推翻 11 月 8 日晚 9 点的 254–162–19 定格。
- **D2（决选仅佐治亚）通过**。P2：“If no candidate wins a majority in Georgia's Senate race, there is a runoff on December 1. Mississippi has no runoff: the most votes win.”；P6 图表：“Runoff, if needed: December 1 (Georgia only)”。Q13 键 1、Q21 键 C（12 月 1 日）不受影响，核实无误。
- **D3（Q107 win）通过**。registry Q107 key=`win`，注记“复数主语用 win（标题现在时）”；题面为标题现在时 “Democrats ___ the House” is a headline，win 正确。
- **D4（P8 注记 108–111）通过**。独立重跑 `tools/p8.py extract --p8 …/svg/p8-test.svg --total 150`：noted set = **60/150**（parse: joined），含 108、109、110、111；P8 渲染图上四条注记完整可见（won/win 时态错；continued；more than 结构；whether 引导从句）。注：跑的是 builder 改动后未提交的 p8.py，行为正常，无异常。
- **D5（范文 80–100 实词）通过**。独立计数：MODEL_TEXT 按含字母数字的 token 计 = **82**（ naive split 为 84，差 2 个独立 em dash）；build log 印 “MODEL words: 82”。P8 渲染图范文框完整收纳全文，末句 “…in English.” 齐全，无截断。
- **D6（完形 112）通过**。题干现为 “On (112)___ morning, November 3”（content8.py 与 P8 渲染图一致）；11 月 3 日为周二（`date -d` 核实），Monday/Friday 均不成立，键仍为 Tuesday，注记“周二 11 月 3 日投票日”已改。
- **D7（法语标点）通过**。8 个 SVG 文本与 PDF 文字层中 ` :` / ` ?` / ` !` / `«` / `»` / `252` / `161` 均为 0；每页弯引号 “ ” 开闭数相等（P1 2/2、P2 1/1、P3 10/10、P4 3/3、P5 11/11、P6 2/2、P7 29/29、P8 25/25），SVG 文本中直引号 0。
- **D8 通过**。(a) P4 “Australia lost their first Test at the ground in November 2024, by 295 runs to India” 及 Q63 同句；外部核实：cricket.com.au / ESPNcricinfo——2024 年 11 月 22–25 日珀斯体育场印度胜 295 分，确为澳大利亚在该场地首败。(b) P2 “two months after the vote”：投票 11 月 3 日、新国会 2027 年 1 月 3 日就职，正好两个月。(c) P7 win/won Try-it：“Will England win the Ashes?”（系列赛开始前）/ “England won the first Test.”（首场之后），逻辑已改顺。

## 其余验证（全部通过）

- **150 题逐题复核**：registry 150 题编号 1–150 无缺无重；按页 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22；text.md 附录 150 条答案与 registry 逐项比对（题型+键），0 不符。除 D9 的 4 题外，其余 146 题键均对题面、原文、图表再验算无误（含 Q84 33/35、Q87 算术、Q100–111、对话 145–149、翻译 137–140、配对 141–144）。
- **8 版逐版看图**：P1–P8 均渲染成图精读，无溢出、重叠、压页脚、图片缺失；页脚“第N版／共8版”齐全；目录（P1）与各版标题、页码、级别徽章一致；图片 8 张逐张核对 CREDITS.md，全部 PD/CC0 且页内出处齐全（国会大厦 Noclip、火鸡 Audubon、老虎 Rousseau 1891、W.G. Grace Barraud、劳伦斯儿童 Bain/LoC 1912、投票亭 Zirkel CC0、约翰逊 Reynolds 1772、阅览室 Highsmith）。
- **事实与日期**：全部日期星期经 `date -d`（America/Toronto）核实（11 月 3 日周二、8 日周日、9 日周一、15 日周日、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、12 月 1 日周二、2027 年 1 月 3 日周日）；儿童权利公约 1989 年 11 月 20 日通过、灰烬杯历史（2010–11 上次英格兰在澳赢系列赛、2017–18 与 2021–22 均 0–4、2023  draw）等可核历史事实无误。选举数字与体育/娱乐前瞻阵容为本期情景内容，内部一致；AP 计数已外部复核（见 D1）。
- **机械门**：`occlusion_audit.py` 0 flags（selftest OK）；`freeze.py baseline` 工具自报 0/8 为已知重定向假象，直接 sha256 比对复现 SVG 与交付 SVG **8/8 一致**（哈希与 KIT §9 所列逐一相符）；`p8.py extract` 60/150（见 D4）。
- **文字层**：print 与 web PDF 各 47,492 字节，`diff` 0 行，实质一致；web PDF 2,765,993 字节 < 7 MB；8 页，1462.5 × 2025 pt。
- **P1 标题**：“Democrats Win the House and the Senate” 38 字符 ≤ 56。**金句**：P7 8 条逐字出自本期正文，脚本核实 8/8 命中，版面归属（P1/P2/P3/P4/P5/P6）全部正确。
- **§1.1**：纸色 #fbfaf6、书衣绿 #37402f、橄榄绿 #46581f、鹅黄 #f6e08e、徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f 均在 SVG 实测到；拉丁正文 Newsreader、刊头 UnifrakturMaguntia、中文 Noto Sans CJK SC；栏目条/导读条/刊别均用全角空格分隔；无双线外框、无金色文字/底色（#D7B257/#EDD17F/#7898CD/#4D72B4 仅见于三色蛾标志图形内部，非文字与底色）；P8 最小字号实测 **15.5pt ≥ 9.75pt** 下限。
- **讲解层**：全部 讲解｜ 词条的英文词均在正文真实出现（脚本核查 0 缺失）；ABSTRACT.txt 单行、无 ASCII 双引号、简体中文，含刊名、目标语、分级与题数。
- **(b) P8 答案键行间断开裁定——不构成缺陷**：200 dpi 放大核查：个别中文注记在栏边断开（如 113 “call=宣｜布结果”、142 “runoff=｜决胜轮”、144 “a (｜midterm=中期选举 a)”、76 “b｜(right=权利 b)”），均为标准 CJK 断行点（汉字之间、“=”或“(”之后），无英文单词中断行、无字符丢失或重叠，阅读顺序完整可解析，与修前基线同一 wrap 行为一致。读者视角可接受，不列为缺陷。

## 缺陷清单

### D9（主要）：P8 完形填空 112–119 中 4 题答案不唯一——非键选项同样正确
位置：P8 A · CLOZE（题 114、117、118、119）；来源 content8.py 选项表与 P8 渲染图一致，答案键见 registry 与 P8 答案区。

- **114** “The vote is over, but the counting ___.” 选项 A. is continuing / B. was continued / C. continues，键 C。“is continuing”同样正确自然（“The vote is over, but the counting is continuing.” 为规范英语），题面无任何语境线索排除 A。两解。
- **117** “states ___ their counts by December 18.” 选项 A. certify / B. will certify / C. certifies，键 B。“States certify their counts by December 18”为表时间的一般现在时，同样正确——且正是 P2 正文自己的写法（“the states certify their counts — between November 10 and December 18”）。按 P2 选 A 的读者会被判错。两解。
- **118** “On Monday, she ___ odd socks to school for Anti-Bullying Week.” 选项 A. wears / B. is wearing / C. will wear，键 A。“is wearing”对具体某天同样正确（“On Monday, she is wearing odd socks to school”）；且本段叙述时间本就不稳（周三写句子用过去时态语境、周五用将来），C 亦可辩护。至少两解。
- **119** “And on Friday, she ___ the new Hunger Games film with her class.” 选项 A. watched / B. watches / C. will watch，键 C。“watches”为表计划的一般现在时，同样正确，且正是本报自己的行文习惯（P3 “the film opens on Friday”、“I'm a Celebrity returns”）。两解。
- 其余 4 题唯一：112（仅 Tuesday）、113（仅 call）、115（仅 will meet）、116（仅 writes，“is wrote”不合语法）。
- 影响：完形 8 题中一半答案不唯一，读者答对却被判错，答案键不可信。须重写 4 题的选项或题干，使每题仅一解（例如 114 删 A 或加语境锚点；117 改题干时态锚点；118/119 加叙述时间锚点）。

### D10（轻微）：P7 “THE DRILLS” 栏首说明与练习内容不符
位置：P7 THE DRILLS · 本周小练栏首（content7.py:62），P7 渲染图可见。
- 原文：“在句首写 win / won / will / whether，完成下列练习。”
- 不符两处：(1) 8 道题（100–107）无一空格在句首，全部在句中；(2) 所列 4 个词只覆盖其中 4 题（100 won、103 will、105 whether、107 win），其余 4 题答案（101 more、102 lost、104 published、106 chose）不在所列词中。按说明字面做题无法完成 101/102/104/106。
- 建议：改为“用所给词填空”或列出全部 8 个词。

## 观察（不列为缺陷）
- “·”仍用作单选选项分隔符与讲解词条内分隔符（如 P1 “A. 218 seats called · B. 254 seats called”）；SOP §1.1 的“不用「·」”条文所举示例为栏目条、页脚、页码行、刊别——这些位置本期均用全角空格，符合条文；选项与词条内的“·”与已出版的 W46 家具习惯一致，首轮 D7 范围亦为法语标点。提请协调员知悉，不作缺陷处理。
- P3/P4/P5/P6 栏尾留白为模板流式行为，与 KIT §8 记录一致，非缺陷。
- p8.py 为 builder 改动后未提交版本，本轮使用中行为正常（60/150 含 108–111）；未改工具、未提交。

## 本轮跑过的检查总表
SOP §8/§1.1 通读；text.md 全文精读；registry 150 题逐题复核；8 页渲染图逐版目视；occlusion_audit（0 flags）；p8.py extract（60/150）；freeze baseline + sha256 直接比对（8/8）；print/web pdftotext diff（0 行）；法语标点 SVG+PDF 双重核查（全 0）；D1–D8 逐项源码+成品+外部来源核实；范文独立数词（82）；P8 字号（15.5pt）；金句脚本逐字核对（8/8）；讲解词脚本核查（0 缺失）；ABSTRACT 单行/无引号；§1.1 颜色字体实测；CREDITS.md 8 图授权；日期星期 `date -d` 全核；Perth 295 分外部核实；AP 254–162–19 外部复核；P8 答案键 200 dpi 放大核查。
