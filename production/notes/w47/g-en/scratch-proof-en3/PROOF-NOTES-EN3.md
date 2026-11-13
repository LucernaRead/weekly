# 第三轮全文复校笔记 — 2026-W47 en 核心版（2026-w47-en-zh-cn，VOL.4）

- 校对员：独立第三轮（叶子），只读不改，未修改 core-en 内任何文件与 tools/p8.py，未跑 insert.py / lint --write / git 写操作。
- 校对对象：`~/workspace/weekly-git/production/2026-w47/core-en/`；印刷 PDF `The-Lucerna-VOL4-en-zh-cn.pdf`（41,407,278 字节，8 页）；网页 PDF `The-Lucerna-VOL4-en-zh-cn.web.pdf`（2,765,419 字节，8 页）；`2026-w47-en-zh-cn.text.md`（50,768 字节）；`registry.json`；`ABSTRACT.txt`（505 字节）；`svg/` 8 个。
- 结论：**零问题**（定稿）。以下为逐项核查记录。

## D9（完形 112–119 逐题独立验证）— 全部通过

- 印刷选项（P8 渲染图 + SVG 文本双重核实）：
  - 112. A. Monday · B. Tuesday · C. Friday → 键 Tuesday（11 月 3 日是周二，`date -d` 已验）；Monday/Friday 皆错。唯一。
  - 113. A. vote · B. call · C. seat → 键 call（"a ___ is a news organisation's judgement"）。唯一。
  - 114. A. continuing · B. was continued · C. continues → 键 continues。A 裸分词、无限定动词不成句；B 过去被动，与正在进行的计票（故事现在时周三、"The counting continues"）冲突；唯 C 成立。唯一。
  - 115. A. meet · B. met · C. will meet → 键 will meet。A 与单数主语 The new Congress 主谓不一致；B 过去时，2027 年 1 月在未来。唯一。
  - 116. A. writes · B. write · C. is wrote → 键 writes。B 与三单 Maya 不一致；C "is wrote" 畸形。唯一。
  - 117. A. certified · B. will certify · C. certifies → 键 will certify。A 过去时，12 月 18 日截止日在故事现在（11 月）之后；C 与复数主语 states 不一致；唯 B。且与 P2 正文 "States will certify their counts." 及 Q17 键一致。唯一。
  - 118. A. wears · B. is wear · C. wearing → 键 wears。B be + 原形错误；C 裸分词无限定动词。唯一。
  - 119. A. watched · B. watch · C. will watch → 键 will watch。A 过去时，周五 11 月 20 日在故事现在之后；B 裸形与三单 she 不一致；P8 范文 "On Friday, we will watch…" 佐证。唯一。
- "is continuing"/"is wearing" 核查：text.md 中 "is continuing" 出现 0 次；"is wearing" 出现 2 次，皆在 P8 阅读理解 Tom 短文正文（"Tom is wearing one red sock and one blue sock."）及 Q131 题干，均非 114/118 选项。content8.py 同。SVG 文本 "is wearing" 2 处同为 Tom 短文。**不在选项里，D9 修好。**
- 注：114 的 B "was continued" 语法上成句，但时态与语境冲突，属 A2 完形可接受的干扰项排除；不构成双答案。

## D10 — 通过

- P7 "THE DRILLS" 栏首渲染图两行完整呈现，无溢出：`用下列词填空：won / more / lost / will / published / whether / chose / win。`
- 8 词按题号 100–107 顺序，与键一一对应（100 won、101 more、102 lost、103 will、104 published、105 whether、106 chose、107 win）。
- 100/107 的 win/won 区分由词库一次性使用 + 107 题干明示 "is a headline" 消解：100 用 won（投票已结束，过去时），107 用 win（标题现在时）。

## 全量 proofread

- 通读 text.md 全文 1,306 行 + 8 版渲染图逐版目视：英文拼写、语法、标点、重复词、截断句均无问题；中文讲解层逐项对照正文，注释词全部真实出现于正文（P1 midterm/call/seat；P2 certify/runoff/sworn in/turkey；P3 tribute/mentor/arena/campmate；P4 Test/tour/injury/break；P5 bullying/speak up/right/silence；P6 call/certify/runoff/map）。
- 目录与跨版引用：P1 目录 p.2–p.8 标题与级别（A2 / A2→B1 / B1 / B1 / B2 / A2→B2 / all）与各版一致；IN BRIEF 三条页码引用正确；P2 "Page 3 has the story"、P1 "Page 6 explains"、"Read page 6" 均正确。
- 页脚每版 "第N版／共8版" 正确；级别徽章与题号级别一致（抽查 P1 A2/B1、P6 B2/B1 混排均符）。

## 150 道题逐题复核 — 全部通过

- 逐题对题面、原文、图表再验算（含 254+162+19=435、33 of 35、254−218=36 等算术），1–150 键全部正确；编号 1–150 连续无缺重。
- 页分布：P1 10、P2 17、P3 18、P4 18、P5 18、P6 18、P7 12、P8 39；级别 A2 62 / B1 66 / B2 22（registry 实测，与 KIT 一致）。
- 附录 vs registry 逐项比对（脚本比对 level/type/key/note 全 150 条）：**0 不符**。配对题印刷 a/b/c/d 顺序逐版核对 SVG 文本：P2 a=bird/turkey、b=second vote/runoff、c=confirm/certify、d=holiday/Thanksgiving；P3 a=guides/mentor、b=chosen/tribute、c=lives with/campmate、d=place/arena；P4 a=pause/break、b=five-day/Test、c=series/tour、d=damage/injury；P5 a=saying/speak up、b=every child has/right、c=saying nothing/silence、d=hurting/bullying；P8-F a=midterm、b=call、c=runoff、d=certify——与 registry 键全部一致。
- 范文 "My Monday, November 16" 实测 82 词（字母数字 token 口径，不含 2 个独立破折号），在 80–100 范围内。

## 8 版逐版看图 — 全部通过

- print PDF 经 pdftoppm（80 dpi）渲染 8 页逐版目视：无溢出、无重叠、无压页脚；8 张图片均带图说与出处（P1 国会大厦 Noclip、P2 奥杜邦火鸡、P3 卢梭《惊奇！》1891、P4 W. G. Grace、P5 1912 年劳伦斯童工游行、Bain、P6 投票亭 Zirkel CC0、P7 约翰逊 Reynolds 1772、P8 国会图书馆阅览室 Highsmith）。
- P3/P4/P5/P6 栏底留白为模板流转行为（KIT §8 已说明，与 W46 相同），非缺陷。

## 事实核查

- 星期全部 `date -d` 核验：11 月 3 日周二、11 月 10 日周二、11 月 16 日周一、11 月 18 日周三、11 月 20 日周五、11 月 21 日周六、11 月 22 日周日、12 月 18 日周五，全部正确；感恩节 11 月 26 日为 11 月第四个周四。
- 实时网查核实（2026-11-10）：饥饿游戏《Sunrise on the Reaping》2026 年 11 月 20 日上映、Joseph Zada 饰海米奇、McKenna Grace 饰 Maysilee、Ralph Fiennes 饰斯诺、Whitney Peak 饰 Lenore Dove、Francis Lawrence 导演、2025 年小说、第 50 届/第二次四分之一大赛、参赛人数翻倍；反欺凌周 2026 年 11 月 16–20 日、主题 "Break the Silence"、奇袜日 11 月 16 日十周年、Anti-Bullying Alliance（National Children's Bureau）主办、覆盖约 800 万儿童、80%+ 学校、主题由 200+ 儿童参与制定、英格兰/威尔士/北爱尔兰；I'm a Celebrity 第 26 季 11 月 16 日周一晚 9 点 ITV1/ITVX、Ant & Dec、Unpacked 在 ITV2（Sam Thompson、Kemi Rodgers）、因英格兰对西班牙欧国联赛（11 月 15 日周日）推迟一天、ITV 未确认营地成员；世界儿童日 2026 年 11 月 20 日周五、UNICEF 主题 "My day. My rights. My future."、《儿童权利公约》1989 年 11 月 20 日通过。以上与本期文字逐项一致。
- 中期选举数字为 KIT §3 规定的情景 AP-call 数（11 月 8 日），全刊内部一致（P1/P2/P6/图表/题键），无一处自相矛盾；P1/P6 均明示 "call ≠ 正式结果"、认证期 11 月 10 日–12 月 18 日；佐治亚决胜轮 12 月 1 日、密西西比无决胜轮与 D2 修复一致。
- 历史事实：英格兰上次在澳赢系列赛 2010–11、2017–18 与 2021–22 均 0–4 负、2023 年在英格兰打平、印度 2024 年 11 月在珀斯赢 295 分、珀斯体育场未办过灰烬杯、卢梭未出过法国、灰烬杯始于 1882 年，均正确。
- D1–D8 回归：SVG 文本节点中 `252`/`161` 每页均为 0（裸 grep 命中为 base64 图片数据，非文本）；两版 PDF 文字层均为 0；`36 more` 在 P7 为 1 处，`34 more` 为 0。

## 机械门槛（独立重跑，工具 venv）

- `tools/occlusion_audit.py`：自检 OK，**0 flags**。
- `tools/p8.py extract --p8 svg/p8-test.svg --total 150`：noted set = **60/150**（含 108–111），与 KIT 一致。（注：builder 改动过未提交的 p8.py；本次运行行为正常，未见异常。未改工具。）
- `tools/freeze.py baseline`：工具自报 0/8 为已知假象（比较空 `<out>/svg`）；直接 sha256 比对复现 SVG 与交付 SVG：**8/8 MATCH**；复现后交付 SVG 哈希不变。P1–P6 与第一轮 freeze 复现（scratch-en/freeze-final）逐字节相同；P7/P8 与第一轮不同（D9/D10 改动所致，符合预期），与第二轮 freeze 复现（scratch-en-fix2/freeze）8/8 相同。
- 构建日志 build-en.log：零 FLOW OVERFLOW / HEAD TOO WIDE；MODEL words: 82；TOTAL exercises: 150。

## P1 标题 / 金句 / 图片 / 摘要

- P1 主头条标题 "Democrats Win the House and the Senate" 38 字符 ≤56。
- 金句 8/8 逐字出自本期正文（脚本核对 text.md 正文部分，含页码归属 P1/P2/P3/P4/P5/P6 均正确）。
- 8 图均为 PD/CC0，CREDITS.md 与页面图说/出处一致；football1910.jpg 未使用，不在正刊图说中。
- ABSTRACT.txt：一行、简体中文、无 ASCII 双引号，含刊名/目标语/分级/题数与本期真实主题。

## §1.1 独立核实

- 纸色 #fbfaf6 每页 1 处（底色矩形）；无金色（#d4af37/#c9a227/#ffd700 均为 0）、无近黑底；无双线外框（"double" 0 处；stroke-width 7 为三色蛾标志描边）。
- 字体：拉丁 Newsreader、刊头 UnifrakturMaguntia、中文 Noto Sans/Serif CJK SC；P6 另有 DejaVu Sans，仅用于 ☐ 选票框符号。
- 栏目标题一律全角空格分隔（THE BIG STORY　头条、LIFE　生活、CULTURE　文化、SPORT　体育、YOUTH　青年、DEEP READ　时事深读、LANGUAGE IN HAND　语言在手等）；页脚 "第N版／共8版" 中文数字无空格。
- 徽章颜色 #5c6e30（A2）/#46581f（B1）/#37402f（B2）齐全；栏目条书衣绿底、米白主标题、鹅黄副标题。
- 法语标点：SVG 文本中 ` :`/` ?`/` !`/`«`/`»`/直双引号 `"` 全为 0；弯双引号每页开闭相等（P1 2/2、P2 1/1、P3 10/10、P4 3/3、P5 11/11、P6 2/2、P7 29/29、P8 25/25）。

## P8 答案字号实测

- 口径：PyMuPDF 读两版 PDF 全部文字 span（pt 单位）。P8 最小 **11.62pt**（276 个 span），全刊最小亦 11.62pt；≥9.75pt 下限，且 ≥11.25pt 目标，无需让步。
- SVG 属性最小 15.5 为 px 单位（1950×2700 px ↔ 1462.5×2025 pt，px = pt×4/3），15.5×0.75 = 11.625pt，与 PDF 实测一致。第一轮实测 "15.5pt" 实为同一数值的 px 读法。
- 注：print PDF 亦含矢量文字层（非纯栅格），两版 span 数相同（1,817）。

## 文字层

- pdftotext：print 与 web 两版均为 47,501 字节，diff 0 行；8 页，1462.5×2025 pt；web PDF 2,765,419 字节 <7MB。

## 已裁定事项（未重议）

- (a) P8 答案键中文注记行间断开：标准 CJK 断行点，不构成缺陷。
- (b) "·" 仍用作分隔符：栏目标题已改全角空格；剩余 "·" 均为同一行内条目分隔（单选题选项、讲解词条、日历/数字列表、模拟选票、答案键条目），属已裁定类别，不构成缺陷。P1 12 处、P2 12 处、P3 15 处、P4 15 处、P5 15 处、P6 29 处、P7 0 处、P8 184 处，均已逐类核对。

## 非阻塞观察（不构成缺陷，报备）

1. KIT §9 首段 freeze 记录把 P7 1677d47d…/P8 a5ad8d60… 写成"第一轮基线"，实际是第二轮修复后的值；真实第一轮 freeze 值为 P7 2fffd800…/P8 ce6d8e36…（scratch-en/freeze-final）。属 KIT 文字口径问题，版本文件本身一致且本次已独立复现 8/8。
2. KIT §9 称 P8 最小字号 "15.5pt（SVG 属性实测）"，单位实为 px，真值 11.62pt（PDF 实测），仍达标；仅单位标注不准。
3. P1 顶栏家具写作 "VOL. 4"（字母间距样式），刊头/页脚用 "VOL.4"，与 W46 家具一致。
4. SVG 文本中英文缩写撇号用直撇号（I'm、Cummins's、Governors'），SOP 未要求弯撇号。
5. P2 "How do you say the date of the new Congress?" 措辞略别扭但可懂。
6. P3/P4/P5/P6 栏底留白为模板流转行为，与 W46 相同。
7. p8.py 为 builder 改动后的未提交版本，本次 extract 运行正常，无异常行为。
