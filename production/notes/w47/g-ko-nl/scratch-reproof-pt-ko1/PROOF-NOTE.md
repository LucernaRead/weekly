# PROOF-NOTE — 2026-W47 pt-ko 独立复校 re-proof（fix1 重建版）

- 版：`2026-w47-pt-ko`（葡语目标 · 韩语读者层），8 页，150 题，VOL.4
- 复校员：独立复校 re-proof（与 fix1 修复员不同人，与 proof1 不同人），2026-11-11
- 结论：**(a) 零缺陷，可定稿** — 全部机械门独立重跑通过，150 题逐题手验通过，8 页整版 + 4 处修复特写目视干净
- 生产目录零写入（交付件 mtime 仍为 16:19–16:26 UTC，源文件 16:18:57，KIT 16:31:40——均早于本次开工 16:35 UTC；git diff 为空）。全部重跑在本人 scratch 副本内完成。

## §0 身份核对（三 SHA 实测，与任务书预期逐一一致）

| 文件 | 磁盘 SHA-256 | 字节 | 行数 | 与任务一致 |
|---|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `cdff9fe46e350a0d2889fcc99e51dfb36547eb158eb4aabfda021a2ad6f069a4` | 17,184,511 | 8 页 | 是 |
| `A-Lucerna-VOL4-web.pdf`（网） | `3046541c903ea95e4f74aa7124c790a290448bd01fc4d30f04a1c9a42e64c3ad` | 1,431,219 | 8 页 | 是 |
| `2026-w47-pt-ko.text.md`（文） | `3eb35dfb9070565c1b168d3e79b8319c4867434b53e0819e8f77cd8ca467cb4c` | 37,804 | 534 行 | 是 |

探针：`git hash-object -w` 在 repo 内能通（`9daeafb9…`）；`/dev/null` 存在；TMPDIR 全程指本人 scratch 下 `tmp/`；解释器全程 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）。

## 缺陷清单

**无。** 本轮未发现缺陷。以下为逐项复验结果（proof1 的 D1–D8 与 fix1 的 F1–F4 全部复验为已修；详见 §1–§6）。

## §1 F1–F4 修复复验（独立重测：wrap() 重算 + 渲染真墨实测，不照抄 fix1 数字）

| 项 | 源 | 独立重测结果 |
|---|---|---|
| F1 P7 B2 桥孤儿 `.` + 行首 `:` | `content7.py:52` | wrap（sans 20.5 / 422.5）重算 2 行：行 1 `quando、se、quem 뒤엔 접속법 미래가 와요:` 407.8（余 14.7）/ 行 2 `sair、for、tiver（공식 정답 기다리는 문법）.` 398.3（余 24.2）。渲染真墨：y=594.9 墨宽 408.0，y=624.7 墨宽 398.2，与 wrap 一致；特写 `render/crop-p7-b2bridge.png` 目视通过。原 y=654.4 的孤儿 `.` 与原 y=624.7 的行首 `:` 均消失。 |
| F2 P1 数字框孤儿 `）` | `content12.py:45` | wrap（serif 20 / 386.5）重算 2 行：340.0 / 331.7（余 54.8）。渲染：y=936.2 行墨 1007.0–1347.0，y=963.2 行末 `）` 墨止于 1338.8（盒右缘 1411.5，余 72.7）；特写 `render/crop-p1-numbers1695.png` 目视通过。原 svg/p1-capa.svg x=1007.0 y=990.2 的孤儿 `）` 消失。 |
| F3b P5 计划框第 4 项行首 `:` | `content56.py:25` | wrap（serif 21 / 386.5）重算 3 行：350.1 / 370.8（余 15.7，行末 `:`）/ 149.7。渲染：行 2 末 `:` 元素 x=921.6（盒右缘 961）；行 3 `TRI 가 정해요）` y=664.2；特写 `render/crop-p5-note.png` 目视通过。原 y=664.2 的行首 `:` 消失。 |
| F4 Q68 `,TRI` 缺空格 | `content56.py:74` | 全版 `,(\S)` 重扫 0 处；P8 渲染行 y=2313.1 `68. B — 맞힌 개수가 점수가 아니에요, TRI 성적을 정해요`；特写 `render/crop-p8-q68.png` 目视通过。 |
| 未动项 | `content12.py:266` | 该行仍为 `e.ex("A2", "문장을 완성하기", "1695", "줌비는 1695년에 돌아가셨어요",`——练习答案原文未动（verify_ed 亦 PASS）。 |
| 观察项 | 核心 P5 孤儿 `）` | core-pt 自扫仍有且仅有 1 处：ORPHAN p5-jovens.svg y=718.7 `）`（本版渲染该项不断行，无此孤儿）。核心未动，符合任务书要求；仅作观察记录，不修核心。 |

## §2 proof1 缺陷 D1–D8 回归复验（重建版机制修复，均已修）

- **D1**（P1 数字框标题出盒）：标题现为 `A SEMANA EM NÚMEROS　숫자`，PIL 真墨右缘距盒右缘 **−64.2px**（余量充足；core-pt 同法 −60.5）。已修。
- **D2**（P1 快讯盒末行漫出盒底）：盒高 436→474，盒底现为 2348.0；OWN 末行 `em Brasília. (Página 4)` 基线 2327.6、墨底 2332.6，真墨余量 **+15.4**。已修。
- **D3**（P3 周历盒末行漫出盒底）：盒底现为 551.0；OWN 末行 `16h30.` 基线 540.6、墨底 540.9，真墨余量 **+10.1**。已修。
- **D4**（P6 时间线盒末行降部漫出盒底）：盒底现为 854.0；OWN 末行 `Página do Participante.` 基线 840.8、墨底 846.0，真墨余量 **+8.0**。已修。
- **D5**（P2 SÁB 21 格 `16일:30` 误译）：渲染现为 `토요일 16:30, 파우메이라스 대 플라멩구`；全版 `\d일:` 误译模式重扫 0 处。已修。
- **D6**（韩语冒号粘连，实为 24 处）：逐行重建扫描 `:` 后非空格非数字 0 处；冒号+空格出现 162 处；时刻 `HH:MM` 5 处均正常。已修。
- **D7**（P8 Q65 `18일까지:30` 误译）：渲染现为 `65. B — 2일 차는 자연과학과 수학, 13:30–18:30`；全版 `일까지:30` 0 处。已修。
- **D8**（P8 Q68 全角逗号）：全角 `，` 全版 0 处（F4 亦为此）；全角 `。`/`！` 0 处。已修。

## §3 150 题逐题手验（题干与键逐项适配）

- 三源交叉：REG 键 × text.md 行内答案（解析 108 项）× text.md Respostas 汇总（解析 150/150）× P8 印出版面键（150/150）——**不一致 0 项**，唯一差异为 Q150（写作题：REG 键为任务说明，P8/Respostas 为 `✓` + 模范文提示，预期）。
- 全文通读：text.md 534 行逐字读完；印 PDF 提取文本 8 页对照。日期/星期经 `date -d` 核验（11-07 六、11-08 日、11-14 六、11-15 日、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-23 一、11-27 五、12-06 日）全部吻合；Enem 算术复算：16–30 日 = 15 天 = 10 工作日（16,17,18,19,23,24,25,26,27,30）+ 5 周末/假日（20,21,22,28,29）；模范文实测 88 词。
- 题干-键适配抽查要点（均核实）：Q44 组句键补 `de novembro`（与 core-pt 同键，句子本身正确，接受——proof1 O5 同结论）；Q56–59 mais/menos 逻辑；Q65/66/67/68/69 与 P5 正文一致；Q80–82 V/F（80 真、81 假、82 真）；Q83–86 算术；Q104 B（nós→aproveitamos）、Q108 B（saíram）、Q109 sair / Q110 for / Q111 tiver（未来虚拟式）；Q125 A（周六 21 日，rodada 36）；Q127 A（数字 10 = 10 个工作日）；Q131 A；Q137/138 韩语译文正确（p8 keydiff 两项，逐字核对）；Q139/140 韩-葡翻译正确；Q141–144 配对正确；Q145–149（Mané / sexto / quinto / na / obrigado）正确；Q150 模范文 88 词。
- 11-07/08 半决赛与圣保罗大奖赛赛果（11 月 7–8 日已赛场次）与正文内部一致；11 月 14–22 日赛程在正文明示为赛前预览（"esta edição fechou em 10 de novembro"），与 proof1 同口径，不另判。

## §4 几何与版面（独立重跑，详见 GATE-LOG）

- 盒标题真墨：31 框全部干净，最小余量 −18.2px（P3 gloss 标题）；P1 数字框标题 −64.2px。boxtitle（advance 宽度法）31/31 clear，最小 +18.2px。页缘溢出 0 处，盒顶溢出 0 处。
- 溢出横扫：creambox naive 6 处负值全部裁决为框外行（下一节标题/页注，owner-rect=NONE）；creambox_diag 真墨 0 处负 ink-clearance，OWN 末行最小余量 +2.4px；ink_measure 6 处“墨底溢出”均为基线在盒底之下 37–44px 的框外行，core-pt 同法复测基线相同、墨底相差 ≤0.8px（中韩 gloss 字形差异）；P2 `Atenção…` 全宽行墨右缘 1683.3 < 页宽 1950，属误关联，非缺陷。
- occlusion 真实审计 0 flags；sweep 框-线 0、桥孤儿 0、桥寡行 0（20 桥）；gates 16/16。
- P8 最小字号 10.125pt（0 项 < 9.75pt）；印/网文字层逐字节一致（105,211 B）；斜体 span 印 1 = 网 1（P1 `« consciência »`）。

## §5 判为非缺陷的项（本轮新核实的疑点裁决）

- 标点重扫 3 处疑似旗标均裁决为非缺陷：P7 `22일 일요일까지예요`（"연휴는 22일 일요일까지" = 延至 22 日周日，正确的日期用法）；P8 Q85 `주말에 공휴일까지 5일`（对 core `周末加假日 5 天`，`까지` = 含该日共 5 天，语义正确）；P8 Q59 `2일 < 7일: menos`（对 core `2 天 < 7 天：menos`，冒号后有空格，比较式记法正确）。
- U+3001 `、` 4 处（P7 B2 桥列举分隔，SVG 与 text.md 一致，著者写法）；弯引号 `« »` 各页 1 处，均为标准葡语引号。
- Q44 键补词（见 §3）；Q150 的 `✓`（见 §3）。
- P7 末引距预告盒约 107px（gates PASS）；P8 答案流止于 y=2458，距页脚线有余（gates PASS）。

## §6 观察记录（只记录，不判）

- **D5 字体问题（proof1 O1 字体度量漂移）**：本轮在当前 venv 栈下重建可逐字节复现交付件——scratch `run.py` 重建 SVG 8/8 与交付件一致、freeze 核心对照 8/8、版内自比对 8/8、render 重渲印 PDF SHA 与交付件一致。本轮未观察到字体度量漂移。按任务书要求只记录、不作缺陷判定。
- **textmd.py 行数口径**：该工具自报 "(535 lines)" 是 `split('\n')` 对末尾换行多计 1 的口径；实际 `wc -l` = `splitlines` = 534，文件以换行结尾。此为旧 "535 行" 误记的来源，已在 KIT §9 更正（见 §7）。
- 网 PDF SHA 不可复现（fontTools 嵌时间戳，铁律）：本人 scratch 重渲网 PDF 与生产网 PDF 同为 1,431,219 B、文字层逐字节一致，SHA 不同（`b0b40d96…` vs `3046541c…`），属已知逐次浮动，非缺陷。重渲只在 scratch，未覆盖交付件。

## §7 回归复验（proof1 其余门禁 + KIT 更正核对）

- proof1 其余门禁本轮全部仍绿：gates 16/16、occlusion 0、p8 CLEAN、keycheck 149/150、freeze 8/8、creambox 真墨 0 溢出、boxtitle 31/31、sweep 0/0/0、印/网文字层一致、P8 字号 10.125pt。
- text.md diff 相对修前（SHA `fe14281f…`）：恰 3 行（L38 F2 / L280 F3b / L393 F1；F4 在 text.md 中无出现处，Q68 答案注只在 P8/REG）。
- KIT §9 更正已核对：D6 实为 24 处（KIT L150 与 FANOUT-REPORT-pt.md L135 均已写 24，全文无 "(22 instances"/"(22 spots" 残留）；text.md 实为 534 行（KIT L127 已写 534 行并注明 535 为误记）。
- check_s11（pt-ko 改编版）ALL PASS；verify_ed（pt-ko 专用版）18/18 PASS；core-pt 未动（三重核验：无文件新于本次开工、git diff 为空、freeze-core 完整性行）。

## 证据文件清单（全部在 scratch `.../scratch-reproof-pt-ko1/` 内）

`PROOF-NOTE.md`、`GATE-LOG.md`、`keycheck-150.json`、`keys-table.txt`、`p8-extract.json`、`p8-compare.json`、`freeze-diff.json`、`ink-measure.json`、`ink-measure-core.json`、`ko-textmd-diff.json`、`logs/`（run/gates/occlusion/p8-extract/p8-compare/freeze-core/freeze-ed/freeze-diff/creambox/creambox-diag/boxtitle/sweep/keycheck/minfont/check-final/render/webpdf/textmd/scan/scan-punct/scan-core/check-s11/verify-ed/xcheck150/print/webtest/web-prod）、`render/crop-p1-numbers1695.png`、`render/crop-p5-note.png`、`render/crop-p7-b2bridge.png`、`render/crop-p8-q68.png`、`build/2026-w47-pt-ko/`（重建副本：SVG 8/8、印 PDF、卡片 8 张）、`webtest/A-Lucerna-VOL4-web.pdf`（scratch 重渲网 PDF）、`textmd-copy/`（textmd 重生成副本）、`freeze-core/`、`freeze-ed/` 及各复验脚本（`ink_measure.py`、`scan_lines2.py`、`scan_punct.py`、`xcheck150.py`、`probe_wrap.py`、`check_s11_ptko.py`、`verify_ed_ptko.py`、`keycheck-mine.py`、`minfont-mine.py`、`check_final-mine.py`、`textmd-mine.py`）。
