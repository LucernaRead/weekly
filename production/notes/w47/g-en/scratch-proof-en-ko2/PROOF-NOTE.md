# PROOF-NOTE — W47 en-ko · proof2（独立复校，Q73 delta 后）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 结论：**(a) 零缺陷，可定稿**
- 复校员：独立 proof2（与 delta 执行者非同一人）；本轮会话 `a6718c59-84f2-461c-bc42-0ac1904beb1f`
- 只复校，未改任何生产文件、未重建生产件、未 commit、未 push、未动 `tools/`、未碰 core-en
- 交付：`GATE-LOG.md`（逐门结果 + 完整 SHA）、`render/`（8 页印版 + 网 P1/P8 + P2/P3/P5/P7/P8 放大裁切）

## 1. proof1 缺陷 D4（Q73）已修——四源一致

- 题干（text.md:589、P5 印版、core-en 源码一致）：`73. [A2] 빈칸 채우기 — Speak ___: tell a teacher.`
- 键（三源一致，均为 `up`）：
  - `registry.json` n=73：`key: 'up'`，`note: 'speak up = 목소리를 내다'`
  - text.md 答案区 1151 行：`73. [A2] 문장 완성 — up (speak up = 목소리를 내다)`
  - P8 印版 ANSWERS 块：`73. up`（`render/crop-p8-answers.png` 清晰可见：`72. rights … · 73. up · 74. d …`）；P8 抽取键亦为 `up`；SVG 内 `73. speak` 出现 0 次
  - 核心对照：core-en registry Q73 = `up`，core-en P8 SVG 含 `73. up`
- P5 印版目视：B 组 `73. Speak __: tell a teacher.`；页首注释 `to speak up = 목소리를 내다`；同页 C 组 `75. to speak up`、D 组 Q79 `Children (speak) up this week.` 一致
- 完成句现为 **“Speak up: tell a teacher.”**——合语法。delta 声称的范围逐项独立核实通过：registry 与 delta 前恰好 1 条差异（Q73 speak→up，其余 149 条逐项相等；registry SHA `56f6620b…cf732a` 与 DELTA-NOTE §3 一致）；text.md 与 delta 前恰好 1 行差异（1151 行）；8 个 SVG 中仅 `p8-test.svg` 变化（`c50c2edd…` → `007698e2…`），其余 7 页 SHA 与修前逐个一致；**p5 不变是正确预期**（Q73 键只印在 P8，P5 只印题干空白 + `speak up` 注记；P5 内 7 处小写 `speak` 均为题干/正文/注释文字，无一处是 Q73 键）

## 2. ko1 三项缺陷无回归

- **D1（Ashes）**：P4 标题仍为 `Perth, One Year On: How Australia Kept the Ashes`（SVG 内分两个 text 节点：`Perth, One Year On: How` + `Australia Kept the Ashes`）；`Perth is winning` / `Ashes begin` / `second week in Perth` 全版 0 处（含 text.md）
- **D2（Q39/Q40）**：registry 38=b、39=a、40=d、41=c；text.md 答案区与 P8 抽取键一致
- **D3（ODD SOCKS）**：P5 框题仍为短标题 `ODD SOCKS, IN NUMBERS　숫자로`；源级 375.4px、PIL 真墨余量 +29.5px、SVG advance 余量 +29.1px；`render/print-p5.png` 全页目视确认标题全在奶油框内

## 3. 150 键逐项手核（Q73 教训：三源一致也可能同错）

- 全文 1305 行逐行通读；答案区 150 条编号 1–150 连续无缺重；text.md 答案区 vs registry 150/150 一致；registry vs P8 抽取键 149/150 + #150 截断例外（见 GATE-LOG）
- stub 机制逐项复核（`stemfit2.log`，57 个含 `___` 题干 + 完形/对话 2 段）：机械 flags **0**；每键填入后合语法、合题意；Q70 `Break the silence`、Q71 `wear odd socks`、Q72 `Every child has rights`、Q73 `Speak up: tell a teacher.`、Q100 `The Democrats won the House.`、Q107 `“Democrats win the House” is a headline.`（标题现在时，正确）；完形 Q112–119 与对话 Q145–149 代入键后全文通顺
- 5 组配对题释义顺序逐组对 SVG 核对无误（P2 D Q24–27、P3 C Q38–41、P4 C Q56–59、P5 C Q74–77、P8 F Q141–144）
- 其余逐题核对无误（选择 120–128、阅读 129–132、句型 133–136、翻译 137–140、写作 150）

## 仅作观察（非缺陷，沿用 proof1/delta 定性）

- **O1** P3 `HAYMITCH'S GAMES　헤이미치의 경기`：SVG advance 401.9px，框右缘 1862，余量 **+2.6px**；PIL 真墨余量 **+2.5px**（ink_end 1859.5）；末字 “기” 完整在框内（`render/print-p3.png` 全页目视）。源级 `boxtitle-ko.py` 标 OVER（系统栈 400.7px / venv 401.9px vs 386.5px 通用预算）是口径 artifact——该框内宽实为 404.5px，以 SVG 实测 + PIL 真墨为准。入框但极紧，不构成缺陷。
- **O2** P2 `AND YOU?` 框末行基线余量 **+5.0px**：框底 1544.9，末行 “요.” 基线 y=1539.85。本轮独立复算：anchor=`ls` 帧下 “요.” 墨水在基线处止（ink_below_baseline=0），真墨余量 **+5.05px**；`ink_ko.py` 所报 −19.0 是该脚本自身的量测口径错误（`getbbox` 默认 `la` 帧的 y1 被直接加到基线上），非真实溢出。放大裁切 `render/crop-p2-andyou.png` 目视确认末行完整在框内，下方仍有奶油边。紧但在内。
- **O3** 独立填空线 19 处（核心级同位、proof1 已有、非回归）：P2 4 / P3 5 / P4 4 / P5 4 / P8 2，edition 与 core-en SVG 逐页坐标完全一致；填空线本身渲染完整、无裁切、无横向溢出。记为观察项，不列缺陷、不修版。孤儿标点全版扫为 **0 真孤儿**（8 处纯标点节点皆为同基线折分 artifact）。
- **O4** P7 “VOL.3 promised real letters from VOL.4”：W46 实际措辞为条件式，W47 此句略有夸大；实质处理诚实无误（无来信、承诺保留、真信自 VOL.5 起刊登）。沿用，不列缺陷。
- **O5** P5 配图说明 “Children from Lawrence, Massachusetts, marching in New York on February 19, 1912”：照片本身为真（Bain News Service，经美国国会图书馆）；具体日期 2 月 19 日未能从公开来源中确认。无反证，不列为缺陷，请协调员复核该日期。沿用。
- **O6** D5 字体（只记录、不判）：全版未发现字体问题——韩文层在全部 8 页渲染与裁切中字形完整、无缺字；P6 练习选票 ☐ 正常渲染；弯引号成对（“ 81 / ” 81）、英文撇号 ASCII 40 个；freeze 新增 CJK 2323 = Hangul 2309 + U+3000 9 + CJK 标点 5，**新增汉字 0**；印/网版各 43 个字体对象，全部已嵌入 + 子集化（见 GATE-LOG §D5）。只记录，不影响结论。
- **O7** Q108 纠错题最小修正问题：原错句 “The Democrats win the House in 2026.” 的公布正解为 “The Democrats won the House.”（删去了 “in 2026”）。正解本身合语法、合事实，属可接受的改写；不列缺陷。Q18/Q63 同类（公布键省去题干末尾状语：Q18 `Families will travel home.`、Q63 `India beat Australia by 295 runs.`），键本身合语法、时态转换正确，属可接受的简化改写；delta §8 已记，不改。
- **O8** P2/P6 佐治亚决选句为条件式教学句，佐治亚决选法本身正确；本期算术暗含佐治亚已定，存在轻微内部张力。条件式措辞，无直接矛盾。沿用。
- **O9** 构建栈记录：本版由 tools/venv（Pillow 13.0.0 / FreeType 2.14.3）构建；freeze.py 的 guard 对 core-en / `2026-w47-en-ko` 路径要求 Pillow 13（见 GATE-LOG “栈口径说明”）。系统 python3 重跑为 7/8 DIFF（仅 p4 MATCH），属栈 artifact，TOTAL/流末值相同。
- **O10** `·` 分隔符：U+00B7 见于术语注释行与 P8 答案分隔，继承自核心与 W46 ko 翻译记忆库、全周一致；各栏目标题与页脚用全角空格 U+3000，符合 §1.1。沿用。

## 已核实无误（要点）

- 全部日期/星期均用 `date` 核验通过（18 个日期）；P7 金句 8 条与原文页面逐字一致；P6 图表数字内部一致（254/162/19；20/13/2；翻转 7；州长 5；254+162+19=435）；P8 完形叙事星期一致；MODEL 范文 82 词（构建计数），在 80–100 词范围内
- ABSTRACT 未动（624 字节，SHA `927505ce…bc81a`，与 fanout-en2 `abstracts/ko.txt` 字节一致）
- 图片与出处齐全（见 proof1；本轮未改动）：国会大厦（Noclip，PD）、火鸡（Audubon）、Rousseau《Surprised!》1891、W. G. Grace（Barraud，1880 年代末，PD）、劳伦斯儿童（Bain News Service，经 LoC，PD）、投票亭（Zirkel，CC0）、Samuel Johnson 肖像（Reynolds 1772，PD）、国会图书馆主阅览室（Highsmith，PD）
- 目视：印版 P1–P8 + 网版 P1/P8 全页干净，无溢出/重叠/压页脚；P7 工具盒墨水全部在盒内（清除量 +48.5px）；P8 答案块字小但完整、未压页脚；网版与印版逐页目视一致
- 本复校未改任何生产文件、未碰 core-en、未动 `tools/`；复校结束时三件 SHA 与任务给定值逐符一致（见 GATE-LOG）
