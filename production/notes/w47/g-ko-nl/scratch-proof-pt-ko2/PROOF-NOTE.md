# PROOF-NOTE — 2026-w47-pt-ko (proof1, re-fanout 重建版)

**结论：(b) —— 有缺陷，需返修。** 机械门禁全绿、150 题键全对、三 SHA 与重建报告一致、freeze 8/8，
但成品质检发现 **2 处孤儿标点行（P1 `）`、P7 `.`，均为渲染可见）+ 2 处行首冒号（kinsoku）+ 1 处逗号缺空格**。
其中 P7 孤儿 `.` 是重建者自家 sweep 工具已报出的 1 处（`bridge widows: 1`），与 FANOUT-REPORT-pt.md §2 /
KIT §9 所称 "sweep 0 bridge widows" 直接矛盾。

- 版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-pt-ko/`
- 核心：`core-pt` fix2 (`d2b0e182`)；解释器全程 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）
- 复校员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-ko2/`
- 生产目录未动：复校前后三 SHA 逐字节复核一致（见 §0）。所有重跑（run/gates/render/webpdf/keycheck）均在
  scratch 副本里做；只读门禁直接读生产文件。网 PDF 只在 scratch 里重渲对比，未覆盖交付文件。

## §0. SHA 核对（复校前 + 复校后两次一致）

| 文件 | 字节 | SHA-256（实测） | 与 FANOUT §1 |
|---|---|---|---|
| `A-Lucerna-VOL4.pdf` | 17,185,806 | `ac839d227acb506f71ccfd05a1b63915a22cca91c6bcb0cec0cecd025c2de6e1` | 一致 |
| `A-Lucerna-VOL4-web.pdf` | 1,431,508 | `f505a301e3cb22645aba7131fb61d2f6f445d41ff670bfb3aa63dcebb071c38f` | 一致 |
| `2026-w47-pt-ko.text.md` | 37,823 | `fe14281fdd24abcfc527d359d707aef97b6d92bc9d602cd38ce1a4fbf6c791c4` | 一致 |

探针（开工前）：`/dev/null` 存在、`git hash-object -w` 能通、scratch 目录真实写文件成功。
中途说明：一次服务重启打断了 scratch 副本的 render.py（停在 p7 卡片）；重跑后 rc=0 完成，
重渲印 PDF 的 SHA 与交付印 PDF 逐字节相同（`ac839d227acb…`），无影响。

## §1. 缺陷清单（按严重程度）

### F1. P7 B2 bridge 孤儿句号行 —— 返修（rebase 回归）
- 位置：`svg/p7-lingua.svg`，P7 第 3 栏（x=989.0），y=654.4 的 `<text>` 元素，内容仅为 `.`
- 渲染（`render/crop-p7-b2bridge.png`，2× 放大特写 + `build/.../cards/p7-lingua.png` 全页可见）：
  ```
  quando、se、quem 뒤에는 접속법 미래가 와요
  : sair、for、tiver（공식 정답을 기다리는 문법）
  .
  ```
- 来源：`content7.py:52` 的 bridge（`c.bridge("quando、se、quem 뒤에는 접속법 미래가 와요: sair、for、tiver（공식 정답을 기다리는 문법）.")`）。
  首轮版该桥为 2 行（句号附在第 2 行末）；重建后 D6 的 `: `（冒号后加空格）使第 2 行宽了约 1 字，
  句号被挤到第 3 行独占一行。**是 rebase 引入的回归，不是首轮遗留。**
- 工具证据：独立重跑 `sweep_de.py`（`logs/sweep.log`）：`bridge widows: 1`，
  `WIDOW content7.py: 'quando、se、quem 뒤에는 접속법 미래가 와요: sair、for、tiver（공식 정답을 기다리는 문법' -> line '.'`。
  重建者自家 `ko-sweep.log` 同样为 `bridge widows: 1`，但 FANOUT-REPORT-pt.md §2 与 KIT §9 均写
  "sweep 0 bridge widows"——声称与日志矛盾。
- 修法建议（供返修者）：重断该桥（缩短措辞或调措辞），使句号不独占一行；顺带修 F3 的行首 `:`。

### F2. P1 数字框孤儿右括号行 —— 返修（首轮遗留，重建未修）
- 位置：`svg/p1-capa.svg`，P1 第 3 栏数字框（x=989..1412，y=786..1193），y=990.2 的行，内容仅为 `）`
- 渲染（`render/crop-p1-numbers1695.png` + `cards/p1-capa.png` 全页可见）：
  ```
  1695 — o ano da morte de Zumbi dos
  Palmares（줌비는 1695년에 돌아가셨어요
  ）
  ```
- 来源：`1695` 项的韩语括注 `（줌비는 1695년에 돌아가셨어요）` 换行后右括号独占一行。
  首轮备份 SVG 同位置同行完全相同（行文本逐行比对一致），即首轮即有、重建原样继承。
- 同类对照：核心 core-pt 的 P5 第 2 栏 y=718.7 也有一行孤儿 `）`（`agradece（假日好好休息：大脑会感谢你` /
  `）`，同一 "Descanse no feriado" 项，韩语版反而不断行）。核心已定稿不动，但这说明该类断行是
  渲染器 wrap 的固有毛病，不是"核心也有"就能接受的理由——ko 版 P1 这一处仍须修（缩短括注或调断行）。

### F3. 行首冒号 ×2（kinsoku，行首禁则）—— 返修
- (a) P7 B2 bridge 第 2 行行首 `:`：`svg/p7-lingua.svg` y=624.7，x=989.0，
  `: sair、for、tiver（공식 정답을 기다리는 문법）`（`render/crop-p7-b2bridge.png` 可见）。
  KIT §6 item 8 已记录为"cosmetic quirk（recorded, not fixed）"，理由是"Korean has no kinsoku
  rule against this"——该理由不成立：`:` 属 CJK 行首禁则字符（행두금칙문자），不应出现在行首。
  与 F1 同一桥，修 F1 时一并修掉。
- (b) P5 "O PLANO DA ESPERA" 第 4 项第 2 行行首 `:`：`svg/p5-jovens.svg` y=664.2，x=556.5，
  `: TRI 가 정해요）`（`render/crop-p5-note.png` 可见；全句为
  `4. Não confunda acertos com nota: a TRI decide（맞힌 개수가 점수가 아니에요: TRI 가 정해요）`）。
  此处未在 KIT/FANOUT 任何地方记录。D6 的 `: ` 是修对了，但断行把冒号留在了行首。
- 判定说明：行首 `:` 不如孤儿标点行刺眼，但属于同一断行规则族；proof1 零发现标准下应列为缺陷。
  下述观察项（`·` 分隔符、`（` 行末）因核心同样如此，未列入此条。

### F4. Q68 逗号后缺空格 ×1 —— 返修（轻微）
- 位置：`svg/p8-avaliacao.svg` 答案区 y=2313.1：`68. B — 맞힌 개수가 점수가 아니에요,TRI 성적을 정해요`
- D8 的规则只写了 `，→,`，未加空格；全版韩语语境行中 `,` 后无空格仅此 1 处（独立扫描实测；其余
  如 `의식, 양심` 均为 `, `）。与 D6"冒号后加空格"的处理不一致。修法：`，→, `（或在该句补空格）。

## §2. 声称项逐项实测（重建者声称 → 实测）

| 声称 | 实测 | 结论 |
|---|---|---|
| SÁB 21 渲染 `토요일 16:30, 파우메이라스 대 플라멩구` | P2 SVG y=1736.5/1761.2：`토요일 16:30, 파우메이라스 대` / `플라멩구`（两行）；特写 `render/crop-p2-sab21.png` ✓ | 属实 |
| Q65 `65. B — 2일 차는 자연과학과 수학, 13:30–18:30` | P8 答案区 y=2224.1 逐字一致 ✓ | 属实 |
| D6 冒号 22 处 | 忠实复现 transform 步骤 5（机制文件与重建用 MECH 逐字节相同，同一 core-pt）：**24 处**替换（content34 5 + content56 11 + content7 8），非 22（见 §5a）。但全部 24 处渲染正确：新 SVG 中韩语语境冒号无空格仅剩时间表达式（`16:30`、`13:30–18:30`，正确）；例 `3 > 1: mais`（P8 y-answers）、`채워요: prazo`（P6）均已验证 | 效果属实，**数量声称不符（24≠22）** |
| D8 逗号全对 | 全版 SVG + text.md 全角 `，`= 0、全角 `：`= 0；首轮 P8 唯一 1 处 `아니에요，` 已改为拉丁逗号；P5 句 `맞힌 개수가 점수가 아니에요: TRI 가 정해요` 渲染正确（P5 y=635.6/664.2，两行）。但 Q68 留下 `,TRI` 无空格（F4） | 基本属实，留 1 处 F4 |
| text.md 5 行差异 | 与首轮备份 `diff` 恰为 5 行：L215 D5 gloss、L280/L363/L393 D6 冒号、L433 verbatim（`（이 호 기사에서 한 자 한 자）`）；其余 0 行 | 属实 |
| 词数 7,052（+22 来自 D6 `: ` 切词） | 独立 `check_final.py`：print 7052 / web 7052，multiset-diff 0（`logs/check-final.log`）；D6 冒号改动在 24 处切词，+22 量级吻合 | 属实 |
| D5 gloss `우승/타이틀`，4 行、末行右余 +280.5、底余 +42.7、无溢出 | 独立 `gloss_probe.py`（`logs/gloss-probe.log`）：4 行，末行右余 +280.5、底余 +42.7，`overflow=no`；渲染 `título 우승/타이틀` 在第 3 行；text.md L215 一致；特写 `render/crop-p4-gloss.png` | 属实 |
| D5 字体（只记录数量，不判、不修） | P4 gloss 框：4 个 `<text>` 元素，字体种类 **1 种**：`Noto Sans CJK SC 20.5`（4/4） | 仅记录 |
| freeze baseline 8/8 | 独立重跑 rc=0，8/8 字节一致，哈希与重建者 `ko-freeze.log` 逐项相同（`logs/freeze.log`）。另：我自己的 scratch run.py 重建 SVG 与交付 SVG 8/8 字节一致，re-render 印 PDF SHA 与交付印 PDF 逐字节相同 | 属实 |
| 词数/字数外：text.md 534 行 vs KIT §9 称 535 行 | 实测 `wc -l`=534，`splitlines`=534，文件以换行结尾；"535 行"不符（见 §5c） | 数量声称不符 |

## §3. 门禁独立重跑（全部绿，唯 sweep 1 项 widows=1）

详见 `GATE-LOG.md`。摘要：run.py rc=0 / TOTAL 150 / 0 溢出；gates.py 16/16；
occlusion 真实审计 0 flags；p8 extract 150/150；p8 compare CLEAN（keydiff [137,138]，预期）；
freeze baseline 8/8；freeze diff rc=0（added CJK 3403，均为韩语解释层 + U+3000，非目标语文本）；
creambox 真墨 0 溢出（naive 扫描 6 处负值均为框外行，diag 裁决全部澄清）；boxtitle 31 框全清（最小 +18.2）；
keycheck 149/150（唯一不符 Q150，预期 `✓`）；印/网文字层逐字节一致（105,505 B）；
P8 最小字号 10.125pt（≥9.75pt，0 项低于）；italic span 印 1 = 网 1（`« consciência »`）；
check_final 词 multiset diff 0（7052/7052）；sweep：box-vs-hline 0、bridge orphans 0、**bridge widows 1（F1）**；
150 题逐题手验全对（见 §4）；8 页逐页目视（见 §6）；KINSOKU 逐页扫描（见 §7）。

## §4. 150 题逐题手验（key 与题干/阅读文本逐一核对，非三源一致）

方法：`qtable.md`（题干取自 text.md，键取自 REG，extracted 取自 P8 提取）逐题读过，
每键对照题干、选项与阅读原文核对（Q73/en-ko 教训：三源一致不够）。
结果：**150/150 键正确**，键与提取值除 Q150 外全部一致。
- Q129–132（Rafael 阅读）：对照 text.md L474 阅读原文核对——Salvador、周五 capoeira、
  周六 Palmeiras × Flamengo、周一查 extraoficial，均与键 B/B/A/B 一致。
  （注意：Q150 模范文是另一文本，周日查 extraoficial——不影响 Q132。）
- Q137/138（翻译题，keydiff 预期项）：137 `11월 20일 금요일은 전국 공휴일이에요.`、138
  `파우메이라스는 승부차기에서 5–4로 이겼어요.`，韩语翻译正确；139/140 葡语翻译正确。
- Q131 = A（`a Palmeiras × Flamengo`）与核心一致；Q150 = `✓`（开放写作题，预期例外）。
- Q120 `5시간`（13:30–18:30）正确；Q65 全句键正确；Q68 键 B 正确（仅标点见 F4）。

## §5. 其他核查

### §5a. D6 数量复现（24≠22 的依据）
用与重建完全相同的机制文件（与 `scratch-fanout-pt` 的 transform.py / tables_ko.py / furniture.py
逐字节相同）+ 同一 core-pt，在 scratch 里复跑 transform（仅把步骤 5 的替换改成计数）：
content34.py 5 处、content56.py 11 处、content7.py 8 处，合计 **24 处**。
24 处明细见 `logs/` 下 `d6/` 复现记录（`D6-HIT` 行）。另：SEG 键以 `：` 结尾者 11 个（与 transform
注释"11 SEG values"一致），SEG 值含 `：` 者 11 个，OVR 键含 `：` 者 23 个——"22"无从对应。
**渲染效果无问题，仅数量声称不符。**

### §5b. proof1 旧修复存活复验（KIT §7/§9 之外无其他项；逐项复验）
- D1 `数字`→`숫자`：存活。SEG `数字`→`숫자`（首轮为 `숫자로 보기`）；渲染标题
  `A SEMANA EM NÚMEROS\u3000숫자`（P1 y=823.2）✓
- D5 SÁB 21 整句键：存活。SEG 键 `周六 16:30 帕弗之战`→`토요일 16:30, 파우메이라스 대 플라멩구` ✓；
  碎片键 `周六 16` / `至 18` 在新 SEG 中已删除（首轮 SEG 中确有，新 SEG 中无）✓
- D5 gloss 键：存活。SEG `冠军头衔`→`우승/타이틀`，旧 `冠军`→`우승자` 未动 ✓
- D6/D8：存活（§2）；另 `墨底`→`잉크 하단` SEG 键在 ✓
- D7 Q65 整句键：存活。SEG 键 `第 2 天考自然科学与数学，13:30 至 18:30`→
  `2일 차는 자연과학과 수학, 13:30–18:30`（最长匹配胜出）✓
- hand patch 盘点抽查：`ko-classify.json` 52 KEEP / 0 REVERT / 0 丢失，与声称一致。
  标记分布：25 处 ko D6/D8 标点机制、12+5 处 fix1 块标记、3 处 fix1 max_w 管线、1 处 max_w、
  1 处 `숫자`、1 处 `CW, 474`（P1 flash 框 fix1）、1 处 `qy = 2350`、1 处 `토요일 16:30`、
  1 处 `o título 우승/타이틀`、1 处 `2일 차는 자연과학`。抽查 content7（8 项）/content8（1 项）
  逐项为 D6 冒号或 fix1 行，无丢失的手修补丁。

### §5c. 报告/文档层面的不符（不判、不修，仅记录）
1. "sweep 0 bridge widows"（FANOUT §2、KIT §9）vs 实测 1（F1）。
2. D6 "22 处" vs 实测 24 处（§5a）。
3. KIT §9 "text.md 535 行" vs 文件实测 534 行（`wc -l`=534，`splitlines`=534，以换行结尾）。
4. FANOUT §9 核心继承缺陷" P1 +17.6px / P3 +15.6px / P6 ~+5px 溢出"：用同一真墨 diag 工具
   在核心与 ko 版上同测，三框均为正余量（P1 +15.4、P3 +10.1、P6 +8.0），几何逐值相同——
   §9 的溢出数值在真墨测量下不复现（ko 版无溢出，是好方向；数值来源不明，仅记录）。
5. FANOUT §11 称 transform.py / tables_*.py / furniture.py / textmd.py 在 `scratch-refanout-pt/`——
   实际该目录无此四文件；机制文件在 `scratch-fanout-pt/`，与各版内副本逐字节相同。

## §6. 8 页逐页目视（渲染自与交付 SVG 字节一致的 scratch 重建卡片）

| 页 | 目视结论 |
|---|---|
| P1 | 除 F2（数字框孤儿 `）`）外干净；`숫자` 标题、头条、赛程、quiz 7–10、页脚均正常 |
| P2 | 干净；SÁB 21 渲染正确；gloss 重断行正常；练习 11–28 正常 |
| P3 | 干净；E VOCÊ 韩语重断行（`있나`/`요?`，音节断行，合法）正常；Zumbi 图+注正常 |
| P4 | 干净；D5 gloss 框 4 行无溢出；6 行赛程表+截稿注正常；练习 47–64 正常 |
| P5 | 除 F3(b) 行首 `:` 外干净；Q65 题干渲染正确；计划框、图片+注正常 |
| P6 | 干净；双图表、时间线、练习 83–100 正常；`채워요: prazo` 间距正确 |
| P7 | 除 F1（孤儿 `.`）与 F3(a)（行首 `:`）外干净；8 句引言 2×+页码正常，末行基线 2292.17 < 2404 预览框顶；读者来信 VOL.3→VOL.5 中韩披露正常 |
| P8 | 除 F4（`,TRI`）外干净；练习 113–150、150 条答案、88 词模范、球场图均正常；答案区末行 y=2458（底 2560） |

## §7. KINSOKU / 断行扫描（逐栏逐行重建）

- 孤儿标点行（单行仅标点）：全版 2 行——P1 `）`（F2）、P7 `.`（F1）。其余 `·` 开头/结尾行均为
  gloss/选项分隔符换行（核心同样 11 行以 `·` 结尾、6 行以 `·` 开头，属渲染器固有行为，不列为缺陷）。
- 行首禁则：`:` 行首 2 行（F3）。`）` 行首即 F2 本身。
- 行末 `（`：P1 2023 项、P7 B1 桥、P8 模范文桥——核心 P1 2023 项同样行末 `（`（几何相同），属固有行为，仅记录。
- 音节内断行（`있나`/`요?`、`고`/`마워할`）：韩语音节断行合法，不列为缺陷。
- 全角标点：`。`0、`！`0、`，`0、`：`0（全版 SVG）；text.md 同 0。

## §8. 返修建议（最小改动）

1. P7 B2 bridge 重断行：使句号不独占一行，同时消掉行首 `:`（F1+F3a 一并解决）。
2. P1 数字框 1695 项括注重断行：使 `）` 不独占一行（F2）。
3. P5 计划框第 4 项重断行：使 `:` 不居行首（F3b）。
4. Q68 答案键逗号后补空格（F4；或把 D8 规则改为 `，→, `，全版仅此 1 处受影响）。
5. 更正报告数字：sweep widows 1（非 0）、D6 24 处（非 22）、text.md 534 行（非 535）——文档即可。
返修后只需重跑本次同套门禁 + 目视 P1/P5/P7 三页（其余页无改动，SHA 应不变；改动页重验 freeze 8/8）。
