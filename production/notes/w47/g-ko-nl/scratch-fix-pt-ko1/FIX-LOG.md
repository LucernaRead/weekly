# FIX-LOG — 2026-w47-pt-ko fix1 (proof1 结论 (b) 返修)

返修员：fix1。对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-pt-ko/`（Portuguese target × Korean readers）。
核心：core-pt fix2 (`d2b0e182`)，未动。解释器全程 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）。
专属 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-ko1/`。
不 commit、不 push。

## 0. 先验 SHA 核对（开工前，与任务书一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `A-Lucerna-VOL4.pdf` | 17,185,806 | `ac839d227acb506f71ccfd05a1b63915a22cca91c6bcb0cec0cecd025c2de6e1` |
| `A-Lucerna-VOL4-web.pdf` | 1,431,508 | `f505a301e3cb22645aba7131fb61d2f6f445d41ff670bfb3aa63dcebb071c38f` |
| `2026-w47-pt-ko.text.md` | 37,823 | `fe14281fdd24abcfc527d359d707aef97b6d92bc9d602cd38ce1a4fbf6c791c4` |

探针：`/dev/null` 存在；`git hash-object -w` 能通（`c4b82938…`）；scratch 真实写文件成功（`probe.txt`）。
`TMPDIR` 全程指向 scratch 下 `tmp/`。

## 1. 缺陷修复（逐条：源文件行号 + 改法 + 验证）

断行设计依据：`svglib.py wrap()` 贪心断行（拉丁词整词、CJK 单字），用 venv 实测各候选改法
（`tmp/probe_wrap.py` / `probe_wrap2.py`）后选定，只缩短文字/移动断点，不改事实与答案键。

### F1 + F3a — P7 B2 bridge 孤儿 `.` + 行首 `:`（同块，一并解决）
- 源：`content7.py:52`（bridge）。
- 改前（实测 wrap，sans 20.5 / 422.5）：3 行——`quando、se、quem 뒤에는 접속법 미래가 와요` (421.0) /
  `: sair、for、tiver（공식 정답을 기다리는 문법）` (421.8) / `.` (5.7)。
- 改法：`뒤에는` → `뒤엔`（缩 1 字），`공식 정답을 기다리는 문법` → `공식 정답 기다리는 문법`（去 조사 `을`）。
  新桥：`quando、se、quem 뒤엔 접속법 미래가 와요: sair、for、tiver（공식 정답 기다리는 문법）.`
- 改后（实测）：2 行——`quando、se、quem 뒤엔 접속법 미래가 와요:` (407.8) /
  `sair、for、tiver（공식 정답 기다리는 문법）.` (398.3，余 24.2px）；`:` 落行 1 末，`.` 落行 2 末。
- 仅缩 1 字（`뒤엔`）的方案亦可（行 2 417.2/422.5，余 5.3px），但余量太紧，未采纳。
- SVG 实测（逐栏重建）：p7-lingua.svg y=594.9 / 624.7 两行如上；渲染特写 `render/crop-p7-b2bridge.png` 目视通过。

### F2 — P1 数字框孤儿 `）`
- 源：`content12.py:45`（numbers box 第 2 项）。
- 改前（serif 20 / 386.5）：3 行——`1695 — o ano da morte de Zumbi dos` (340.0) /
  `Palmares（줌비는 1695년에 돌아가셨어요` (374.5) / `）` (20.0)。
- 改法：括注去主语 `줌비는 `（由项首 `Zumbi dos Palmares` 承接）→ `（1695년에 돌아가셨어요）`。
  新项：`1695 — o ano da morte de Zumbi dos Palmares（1695년에 돌아가셨어요）`。
- 改后（实测）：2 行，行 2 `Palmares（1695년에 돌아가셨어요）` (331.7，余 54.8px），`）` 落行末。
- 未动：`content12.py:266` 练习答案 `줌비는 1695년에 돌아가셨어요`（Q 键原文，保留）；
  核心 P5 孤儿 `）`（y=718.7）是核心的，未动核心，未修它。
- 渲染特写 `render/crop-p1-numbers1695.png` 目视通过。

### F3b — P5 计划框第 4 项行首 `:`
- 源：`content56.py:25`（`O PLANO DA ESPERA` 第 4 项）。
- 改前（serif 21 / 386.5）：3 行——`4. Não confunda acertos com nota: a` / `TRI decide（맞힌 개수가 점수가 아니에요`
  (385.4) / `: TRI 가 정해요）`。
- 改法：韩语 `맞힌 개수가` → `맞힌 수가`（同义缩短）。
- 改后（实测）：3 行，行 2 `TRI decide（맞힌 수가 점수가 아니에요:` (370.8，余 15.7px），行 3 `TRI 가 정해요）`；
  冒号落行末，无行首冒号。葡语原文未动。
- 渲染特写 `render/crop-p5-note.png` 目视通过。

### F4 — Q68 逗号后缺空格
- 源：`content56.py:74`（Q68 答案 B）。
- 改法：`맞힌 개수가 점수가 아니에요,TRI 성적을 정해요` → `맞힌 개수가 점수가 아니에요, TRI 성적을 정해요`（逗号后补一空格）。
- 全版韩语行 `,` 后无空格重扫：仅此 1 处，修后 0 处。P8 渲染 `68. B — 맞힌 개수가 점수가 아니에요, TRI 성적을 정해요`
  （特写 `render/crop-p8-q68.png` 目视通过；加一空格未引起 P8 答案区重排，行位不变）。
- 未改 `transform.py` 的 D8 规则（`，` → `,`）：修法按任务书落在 Q68 源文本；D8 规则改动会影响全部
  `，` 转换点，超出最小改动范围。

## 2. 机制同步（transform 输入，与手改逐字一致）

`tables_ko.py`（版内副本 + `scratch-fanout-pt` 机制副本，两份逐字节相同）：
- SEG `:62` `后用虚拟式将来：` → `뒤엔 접속법 미래가 와요：`；SEG `:173` `（等官方答案的假设）` → `（공식 정답 기다리는 문법）`（F1 两段）。
- OVR `:246` 1695 整项值 → `（1695년에 돌아가셨어요）`（F2）。
- 新增 OVR 整行：`4. Não confunda acertos com nota: a TRI decide（答对数不等于分数：TRI 说了算）`
  → `…（맞힌 수가 점수가 아니에요: TRI 가 정해요）`（F3b；不用 SEG `:176`，因该片段与 Q68 答案共用，
  改 SEG 会连带改答案措辞）。
- 新增 OVR：`答对数不等于分数，TRI 决定成绩` → `맞힌 개수가 점수가 아니에요, TRI 성적을 정해요`（F4；
  该中文串在 core-pt 全仓仅 `content56.py:74` 一处）。
- 耐久验证：`tmp/transform-test/`（core-pt 拷贝 + 新机制）跑 `transform.py ko`，rc=0，
  4 处产出与手改版逐字相同（F1/F2/F3b/F4 transform==handfix）。`transform.py` / `furniture.py` 本身未动。

## 3. 重建（生产目录内，顺序 run → render → gates → textmd → webpdf）

生产 SVG 与 scratch 验证版 8/8 逐字节一致，印 PDF SHA 一致，text.md 一致，4 张修复页卡片一致
（故 scratch 的目视结论直接适用于生产件）。text.md 与重建前 diff 恰 3 行（L38 F2 / L280 F3b / L393 F1；
F4 在 text.md 中无出现处，符合预期）。

### 修后三件 SHA（新交付件）
| 文件 | 字节 | SHA-256 |
|---|---|---|
| `A-Lucerna-VOL4.pdf` | 17,184,511 | `cdff9fe46e350a0d2889fcc99e51dfb36547eb158eb4aabfda021a2ad6f069a4` |
| `A-Lucerna-VOL4-web.pdf` | 1,431,219 | `3046541c903ea95e4f74aa7124c790a290448bd01fc4d30f04a1c9a42e64c3ad` |
| `2026-w47-pt-ko.text.md` | 37,804 | `3eb35dfb9070565c1b168d3e79b8319c4867434b53e0819e8f77cd8ca467cb4c` |

text.md 534 行（`wc -l` 与 `splitlines` 一致，以换行结尾）。词数 print/web 7,049/7,049
（原 7,052；−3 来自行合并的 token 合并，非内容丢失）。

### web PDF 说明
生产 web PDF 由重建流程的 `tools/webpdf.py` 在生产目录内重新生成（任务书重建序列包含该步），
是 fix1 的正式交付件。任务书门禁括号“web PDF 只在 scratch 重渲比对，不得覆盖生产 web PDF”理解为
比对用的重渲在 scratch 做——本修全程如此：scratch `webtest/` 重渲（1,431,223 B）仅用于文字层比对，
其文字层与生产印 PDF 逐字节一致；生产 web PDF（1,431,219 B）是 webpdf.py 的正式产出，
字节数浮动属已知逐次浮动（proof1 §15 同类：1,431,506 vs 1,431,508），文字层与印 PDF 逐字节一致
（105,211 B，生产件实测）。

## 4. 报告数字更正（proof1 核实三项）
- bridge widows：重建版实为 **1**（非 0）——`WEEKLY-KIT.md` §9 Gates 句与 `FANOUT-REPORT-pt.md` §（L61）已更正；
  fix1 重扫为 **0**（见 GATE-LOG）。
- D6 冒号：实为 **24 处**（非 22；content34 5 + content56 11 + content7 8，proof1 §5a）——KIT §9
  “(22 instances” 与 FANOUT L135 “(22 spots” 已更正为 24。FANOUT “+22” 词数增量是另一数字
  （D6 `: ` 切词所致），未动。
- text.md 行数：实为 **534 行**（非 535；`wc -l` = `splitlines` = 534，文件以换行结尾）——KIT §9
  “New files” 535→534、“535 行”解释段已重写为纠错说明；FANOUT 无 535 表述。
- 另：KIT §9 末附 fix1 附录（含新 SHA、逐条修复、门禁摘要）；KIT §9 其余重建版记录（旧 SHA/字节）
  保留为历史记录，未覆盖。

## 5. 其他说明
- 只改本版源文件（content7/12/56、tables_ko）+ 本版 KIT + ko 机制表；core-pt 未动
  （verify_ed 三重核验：无 core-pt 文件新于本次开工、git diff 为空、freeze-core 称 core SVG
  前后未变；核心 P5 孤儿 `）` 未修）。
- `gates_pt.py` 未直接跑：其路径硬编码生产版 + 共享 refanout scratch，
  且 keycheck 步会在目标目录重跑 run.py——全部步骤按其清单在本人 scratch 内手工复现（命令见 GATE-LOG）。
- `check_s11.py` / `verify_ed.py` 无 pt-ko 版（现存均为 en 家族专用：core-en、Ashes 内容），
  本修据 en-ko2 版改编通用 §1.1 部分为 `check_s11_ptko.py`，并写了 pt-ko 专用 `verify_ed_ptko.py`
  （Q65/Q68/Q137/Q138 键、4 处源文、text.md 行、core-pt 未动）；两脚本在本人 scratch 内，均 rc=0。
  en 版的结构性 P8 检查（Q113 选项行等）不适用 pt P8，未生搬。
- “registry 重 dump”：pt 家族无 registry.json 文件（全仓无此文件）；解释为 keycheck 的 REG 重导——
  生产重建后在全新生产副本（build2）上重跑 keycheck（其内部重跑 run.py 并重导 keycheck-150.json），rc=0。
- 副作用记录：`textmd.py` 每次运行把 diff json 写到机制目录（`scratch-fanout-pt/ko-textmd-diff.json`，
  其内置行为）；本次两次运行（scratch + 生产）均覆盖了该文件，内容现为 fix1 版的 diff 报告，可复现。
- 生产目录的 `__pycache__` 与 `cards/` 由重建流程正常刷新。未 commit、未 push。
