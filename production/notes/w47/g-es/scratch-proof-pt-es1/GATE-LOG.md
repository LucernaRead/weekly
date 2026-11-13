# GATE-LOG — 2026-W47 pt-es · proof1 机械门实跑证据

Scratch: `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-es1/`
工具：`~/workspace/weekly-git/tools/venv/bin/python`；正典 creambox `hidden_files/w47/tools/creambox.py`（md5 已验 `ee7a55d8b2057cf4ad42a97bb1197383`）。
全程 `TMPDIR=<scratch>/tmp`；未使用系统 /tmp。源文件未改动、未 commit、未 push。

## §0 身份核对（磁盘为准）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0；scratch 写入探针 `probe.txt`（内容 probe-ok）成功。
- 印 PDF `A-Lucerna-VOL4.pdf`：SHA256 `faf2f098043d4126fb49f45b6d0f943c905b98599530e81db0afa3c5a119a321`，**12,933,122 字节**——与任务一致。
- 网 PDF `A-Lucerna-VOL4-web.pdf`：SHA256 `8ef5e4200eef8d5c890d74178086cb73a076cef529d3dcf9f25336258dec5950`，**1,103,156 字节**——与任务一致。
- text.md `2026-w47-pt-es.text.md`：SHA256 `337bb77b771583be56f4b9dd31a4bff5bf86f45c887d3a376f9ad9de6978b5a8`，**37,449 字节**——与任务一致。
- 三者 SHA 与任务消息完全一致，无不符。

## §1 gates.py — 16/16 PASS（`gates.log`，RC=0）

VOL.4/日期、副标题、页脚+页码 8/8、无 VOL.3 版标残留、截稿注+决赛命名、P1 刊头行宽 ≤1820、同基线碰撞 0、页框墨迹穿越 0（最小边距 L/R/T/B = 47.0/32.5/35.0/32.0）、P6 图表标签 GRAZE 0%、gloss 29 项枚举+词头存活、P7 金句 2×+页签+西语、读者角逐字串 5/5、图片+credits 5/5、P7 金句区 clears 预告框（最大基线 2380.67 < 2404）、P1 头条 41 字符（≤56）。FAILURES: none。

## §2 occlusion 审计 — 0 flags（`occlusion.log` / `occlusion.json`，RC=0）

- 自检：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`。
- 结果：`flag_count: 0`。
- **与 KIT 的差异**：KIT 记 1 个 flag（P1 LINEX graze）；当前工具版本下未复现。但 D1 的几何事实由 §6 的 PIL 实测独立证实（整行在框外 + 分隔线穿字），不依赖 occlusion 工具。

## §3 creambox.py 正典全版扫描 — 31 框（`creambox-all.log`，RC=0）

- 全 8 页奶油框 31 个；+45px 窗口内负余量全部为后继标题假阳性（+32–+42px），唯三处为同流续行，逐一 PIL 裁决：
  - P1 EM-BREVE 框：框内末行 clearance +9.6，BELOW +17.6 `em Brasília. (Página 4)` → **D1，真溢出**（见 §6）。
  - P3 日程框：框内末行 +14.9，BELOW +15.6 `16h30.` → **D2，真溢出**。
  - P6 时间线框：框内末行 +28.6，BELOW +0.8 `Página do Participante.` → **D3，降部真溢出 6px**。
  - 其余 BELOW（P1 数字框 +37 `AGORA VOCÊ`、P2 日程 +32 `Atenção:`、P3 +37 `UM DIA…`、P6 图表框 +42 `EXERCÍCIOS`）均为后继标题，非溢出。
- 框内末行降部余量（desc-clear）为负的 6 处，PIL 逐一实测（§6）：P2/P3/P4/P5 E VOCÊ 框与 P7 词框——墨迹在框内（P2 恰止于边行；P4/P5/P7-词框仅 1 个抗锯齿像素越边 1px）；P7 读者园地框 clearance +9.6（墨迹余量 4px）；P5 数字框 `2027.` 余量 5px。均非缺陷。
- **P7 toolbox**：3 框，最小框内余量 **+4.5px**，最小 desc-clear -1.5px（公式值；真墨实测见 §6）。引言末行基线 2380.67，预告框顶 2404，余量 ~18px。

## §4 p8 — extract 150/150；compare CLEAN（`p8-extract.log` / `p8-compare.log`，RC=0）

- `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150`：noted set = 150 of 150。
- `tools/p8.py compare --core-p8 ../core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150`（显式路径）：`status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`。
- keydiff 裁决（手验）：137 `El viernes 20 de noviembre es festivo nacional.` 与 138 `El Palmeiras ganó 5–4 en los penaltis.` 均为对葡语原句的正确西班牙语翻译；139/140 反向翻译亦手验正确。
- 150 题手验见 `keycheck-150.json`：150/150 verified-correct；P8 键与 text.md Respostas 摘要一致（Q150 为 ✓ 标记与指引文字的表述差异）。

## §5 freeze — baseline 8/8；diff 仅 U+3000（`freeze-baseline.log` / `freeze-diff.log`，RC=0）

- `tools/freeze.py baseline`：`baseline: 8/8 SVGs byte-identical (repointed files: none)`，8 个 OK；core integrity：前后重哈希一致。
- `tools/freeze.py diff`：P1 +26/-39、P2 +41/-33、P3 +34/-29、P4 +30/-26、P5 +41/-48、P6 +25/-22、P7 +52/-46、P8 +189/-753；新增 CJK 仅 U+3000，共 9 个（P1 2 个，其余每页 1 个）。
- `freeze_direct`：`tools/freeze.py` 无此子命令（仅 baseline/diff）；baseline 直接重跑即 freeze 证据（见 PROOF-NOTE O3）。
- D1/D2/D3/D7 的核心携带属性另有直接证据：三框 rect 与三行基线在 core-pt 与本版 SVG 间逐字节相同（`rects` 对比；另三处为解说层正常加高/移位，如 P1 数字框 380→434、P2 Nota 框 175.4→205.1、P7 词框移位），且 core-pt 卡片对 D1/D7 的 PIL 实测与本版相同（`ink-line-core.log`）。

## §6 PIL 真墨迹实测（`ink_probe.py` / `ink_line.py` / `title_right.py`；证据裁剪图见 scratch `*.png`）

方法：卡片 PNG（1950×2700，与 SVG 单位 1:1）上，奶油边 = 填白区内奶油末行；墨迹 = 亮度 <190（降部复核 <210）的最下/最右像素行。量具误差 ±1px。

| 检查 | 结果 |
|---|---|
| D1 P1 EM-BREVE 末行 | 奶油末行 2309；墨迹 2311–2342；**+33px** |
| D2 P3 日程末行 `16h30.` | 奶油末行 524；墨迹至 540；**+16px** |
| D3 P6 时间线末行降部 | 奶油末行 839；降部墨迹至 845；**+6px** |
| D4 P2 PARA 标题 gloss | 框右缘 961；墨迹至 1028；**+67px** |
| D5 P7 ERROS 标题 gloss | 框/版心右缘 1862；墨迹至 1875；**+13px** |
| D6 P7 PALAVRA 标题 gloss | 框/版心右缘 1862；墨迹至 1879；**+17px** |
| D7 P8 范文 2–3 行 | 版心右缘 1862；墨迹至 1864（**+2px**）/ 1876（**+14px**）；core-pt 相同两行 +3/+14px |
| P1 EN BREVE 标题 | 墨迹恰止于 1862（**0px**，零余量，非缺陷，列 O2） |
| P2/P3/P4/P5 E VOCÊ 末行降部 | 墨迹止于边行（P2 止于 908=边行）或仅 1 抗锯齿像素越边 1px（P4/P5）；非缺陷 |
| P7 词框末行 / 读者园地框末行 | 词框墨迹止于边内；园地框墨迹余量 4px；非缺陷 |
| P5 数字框 `2027.` | 墨迹余量 5px；非缺陷 |
| 其余标题 gloss | `En cifras` -10px、`En este número` -24px、`Habla de ti` -158px 等，全部在框内 |
| span 框超复核 | `Respuestas en la página 8`（+3.6pt 框）墨迹 -6px；`Tres días…` -5px；`Los niveles…` -10px；`Página N de 8` +1px；均为边距假象，非缺陷 |

## §7 印/网文字层比对；P8 最小字号；弯引号；内部标签

- **印/网文字层**：PyMuPDF 提取逐字相同——印 44,224 字符 / 网 44,224 字符，均为 8,582 词。Web PDF 有原生文字层。
- **P8 最小字号（实测，不用 KIT 数字）**：PyMuPDF 取 P8 全部 span，最小 **9.75pt**（173 个 span），次小 10.5pt；= SOP §1.1 下限 9.75pt。
- **弯引号全版扫描**：本版 SVG `“` 2、`”` 2、`’` 0——仅 P8 E139/E140 两句西班牙语引文；core-pt 为 `“` 3/`”` 3（多一对在 P7 中文 gloss `“落在某日”`，本版作 ASCII 单引号 `'caer en un día'`，与 en/de 版 gloss 约定一致）。text.md `“` 2/`”` 2/`’` 0，无直引号。
- **直引号/撇号扫描**：SVG 文本元素中含 ASCII `"`/`'` 的仅 1 处（P7 gloss `'caer en un día'`，见上），非缺陷。
- **内部标签扫描**：SVG 文本层无 SOP/proofread/W47/2026-w47/pt-es/cover/lint/TODO/XXX/placeholder；text.md 的 grep 命中均为误报（`todo(s)` 含 TODO、`sopesar` 含 SOP）。
- **text.md**：CJK 0 字符；第 E 节标题 `E · Traduza` 已本地化；无「翻譯」/「翻译」残留（必查项 (d) 未复现）。
- **外部事实来源**：事实均取自 KIT §2 所列公开来源（核心 KIT 2026-11-10 核实：Lei 12.519/2011、Lei 14.759/2023、Copa 半决赛 11-07/08、Enem Edital 64/2026 §15.1、Brasileirão 35/36 轮、圣保罗 GP 11-08、国家队 FIFA 窗口 11-14/17）；星期由系统日历核实（`date -d`，America/Sao_Paulo）：11-08/15 周日、11-16 周一、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日。Q125 题干“36 轮”核实：P4 正文称 35 轮止于周四 19 日，故周六 21 日场次属 36 轮，题干正确。

## §8 其余机械事实

- 8 页，1950×2700，4 栏；页数 8（4 的倍数）；VOL.4。
- 150 题分布与 KIT 一致（每页 10/18/18/18/18/18/12/38）；题号连续无缺重（p8 extract 150/150）。
- 5 图与核心字节相同（KIT §3；cmp 已验，见 KIT）。
- P7 金句 8 条，每条正文出现 2× + 页签 + 西语译文（gates PASS）。
- 读者来信栏：葡语示例 + 葡语披露原文 + 西语披露译文 + 示例标签 5/5（gates PASS）；无真实来信（F-MAIL 规则，仅用户直发计入）。
