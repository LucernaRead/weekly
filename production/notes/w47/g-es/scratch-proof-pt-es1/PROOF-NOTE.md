# PROOF-NOTE — 2026-W47 pt-es（葡萄牙语目标 · 西班牙语读者版）· proof1 独立复校

- 版目录：`production/2026-w47/2026-w47-pt-es/`
- 复校员：独立复校（proof1），2026-11-11
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-es1/`

## 结论：(b) 有缺陷，不能定稿

共 **7 项缺陷**：4 项核心携带（核心几何 + 冻结核心文字，在 core-pt 中逐字节相同、本版无法自行修复），3 项本版（西班牙语 gloss 过长导致框标题横向溢出）。

其中 D1、D2、D4 为肉眼在整版上即清晰可见的整行/长标题溢出；D3、D5、D6、D7 为 6–17px 的边缘溢出，放大检查清晰可见。

**源文件未改动、未重建、未 commit、未 push。**

## 缺陷清单

### D1 — 严重 · P1 · 核心携带
- **位置**：P1 右栏 EM POUCAS PALAVRAS（EN BREVE）奶油框，末行 `em Brasília. (Página 4)`。
- **实测证据**（PIL，真墨迹，`ink-line.log` / `p1-embreve-bottom.png`）：
  - 奶油框底边（SVG rect y=1874 h=436 → bottom 2310.0；实测奶油末行 2309）。
  - 该行墨迹行 2311–2342，整行位于框外白纸上，低于框底 **+33px**；基线 2327.6，框内末行基线 2300.4（clearance +9.6）。
  - Quiz 分隔线 y≈2312 横穿该行字形顶部（墨迹自 2311 起，线与墨重叠约 1–2px）。
  - core-pt 卡片实测完全相同（ink run 2311–2342，over +33；`ink-line-core.log`）。
- **归属**：核心（框高 + 文字均为冻结核心内容；rect 与基线在 core-pt/es 间逐字节相同）。
- **KIT 说法核实**：KIT 称此为 "LINEX graze" 且 "invisible in the render"——**与实测不符**。整行在框外白纸上、分隔线穿字，是可见缺陷，不是 0.2px 擦过。
- **修复建议**：核心层修——EM POUCAS PALAVRAS 框加高一行（或 O FUTEBOL 条目重排使末行落入框内），并使 quiz 分隔线避开末行墨迹；核心修好后全部 fan-out 版自新核心重建再复校。

### D2 — 严重 · P3 · 核心携带
- **位置**：P3 右栏 A SEMANA, DIA A DIA 日程框，末行 `16h30.`。
- **实测证据**（`p3-sched-bottom.png`）：奶油框底边 525.0（实测奶油末行 524）；`16h30.` 基线 540.6，墨迹至 540，整行在框外白纸上，低于框底 **+16px**。
- **归属**：核心（rect (1439.5, 200, 422.5, 325.0) 与基线在 core-pt/es 间相同）。
- **修复建议**：核心层修——日程框加高一行（或 Sáb 21 条目重排）。

### D3 — 中等 · P6 · 核心携带（即本版必查项 (b) 同类）
- **位置**：P6 右栏 O CAMINHO ATÉ O GABARITO 时间线框，末行 `Página do Participante.`。
- **实测证据**：框底边 840.0（实测奶油末行 839），该行基线 840.8——框高按基线+0px 定、无降部余量；`g`/`p` 降部墨迹至 y=845，**低于奶油边 6px**（行墨 841–845，每行 7–14 个深色像素，非噪点）。
- **归属**：核心（rect (1439.5, 200, 422.5, 640.0) 与基线在 core-pt/es 间相同）。
- **修复建议**：核心层修——时间线框底加降部余量（≥6px）；同类按基线定高的框一并复核。

### D4 — 严重 · P2 · 本版（即必查项 (a) 同类）
- **位置**：P2 中栏 PARA NÃO ERRAR 奶油框标题 `PARA NÃO ERRAR　La regla para recordar`。
- **实测证据**（PIL 真墨迹，`p2-paranao.png`；PyMuPDF span x1=770.2pt=1027px 一致）：
  - 框右缘 961；标题墨迹最右至 x=1028，**超出框右缘 +67px**，横穿栏间空白进入第 3 栏区域。
  - 视觉：gloss "La regla para recordar" 的后半截落在框外白纸上。
- **归属**：本版（西班牙语 gloss 过长；冻结框宽 422.5px 不变；核心中文 gloss 短、无此问题）。
- **修复建议**：缩短该标题 gloss（如 `La regla` 或 `Recuerda`），或缩小 gloss 字号/字距；改后重跑 gates + creambox + 标题右缘扫描。

### D5 — 中等 · P7 · 本版（即必查项 (a) 同类）
- **位置**：P7 右栏 ERROS COMUNS 奶油框标题 `ERROS COMUNS　Errores frecuentes`。
- **实测证据**（PIL 真墨迹，`p7-erros-full.png`；PyMuPDF span x1=1408.8pt 一致）：框/版心右缘 1862；标题墨迹最右至 x=1875，**超出 +13px**；"frecuentes" 末字母落在框外白纸上。
- **归属**：本版（西班牙语 gloss 过长）。
- **修复建议**：缩短 gloss（如 `Errores`）或缩小 gloss 字号/字距；改后重测。

### D6 — 中等 · P7 · 本版（即必查项 (a) 同类）
- **位置**：P7 右栏 A PALAVRA 奶油框标题 `A PALAVRA　La palabra de la semana`。
- **实测证据**（PIL 真墨迹，`p7-palavra-full.png`；PyMuPDF span x1=1410.4pt 一致）：框/版心右缘 1862；标题墨迹最右至 x=1879，**超出 +17px**；"semana" 末字母落在框外白纸上。
- **归属**：本版（西班牙语 gloss 过长）。
- **修复建议**：缩短 gloss（如 `La palabra`）或缩小 gloss 字号/字距；改后重测。

### D7 — 中等 · P8 · 核心携带
- **位置**：P8 第 4 栏 H 节范文（Texto modelo）第 2–3 行。
- **实测证据**（PIL 真墨迹，`p8-modeltext.png`）：
  - 第 2 行 `despertador: é feriado nacional. De manhã, leio sobre Zumbi` 墨迹至 1864，超出版心右缘 1862 **+2px**；
  - 第 3 行 `e Palmares e escrevo duas frases em português. À tarde, vou a` 墨迹至 1876，**+14px**（其余行均在 1796–1853 内，唯此两行超限）。
  - core-pt 卡片实测相同两行同样超限（+3px / +14px）。
- **归属**：核心（范文为冻结核心文字 + 核心版式）。
- **修复建议**：核心层修——范文段重排/改字距使各行落入栏宽；或核查该栏实际右缘设定。

## 未决事项

- **O1**：D1/D2/D3/D7 为核心携带缺陷，本版内无法修复（改动将破坏 freeze）。需核心层决策：修 core-pt 并自新核心重建全部 fan-out 版再复校，或由协调员明示接受为偏差（现有 KIT "invisible" 的说法已被实测证伪，不能作为接受依据）。
- **O2**：P1 `EM POUCAS PALAVRAS　EN BREVE` 标题 gloss 末字母墨迹恰止于框/版心右缘 1862（0px 余量），未溢出，不计缺陷；但零余量，任何字距/字号变动即溢出，列为观察项。
- **O3**：任务所列 `freeze_direct` 在仓库 `tools/freeze.py` 中无此子命令（仅有 `baseline`/`diff`）；本次 freeze 证据为 baseline 直接重跑 8/8 逐字节相同。如协调员另有所指的 freeze_direct 步骤，请指明路径。

## 核实摘要（全文通读 + 150 题手验 + 机械门）

- **印 PDF 8 页 + text.md 全文已通读**（8 张整版卡片目检 + text.md 534 行逐行读过）；星期核实：2026-11-08/15 周日、11-16 周一、11-20 周五、11-21 周六、11-22 周日、11-27 周五、12-06 周日，全部与版面一致。
- **150 题逐题手验：150/150 通过**（见 `keycheck-150.json`；P8 提取键与 text.md Respostas 摘要 150/150 一致，Q150 为 ✓ 标记与指引文字的表述差异，非不符）。范文 88 词已数过。
- **机械门实跑**：gates.py 16/16 PASS；occlusion 0 flags（自检阳性对照全过；KIT 所记 1 个 LINEX flag 在当前工具下未复现——但 D1 的几何事实由 PIL 独立证实，不依赖该工具）；creambox.py 全版扫描 31 框（P7 toolbox：3 框，最小框内余量 +4.5px）；p8 extract 150/150；p8 compare CLEAN，keydiff=[137, 138]（两题翻译答案手验正确）；freeze baseline 8/8 逐字节相同；freeze diff 新增 CJK 仅 U+3000（9 个）；印/网 PDF 文字层逐字相同（44,224 字符、8,582 词）；P8 最小字号实测 **9.75pt**（= SOP §1.1 下限）；弯引号 U+201C/U+201D 各 2、U+2019 0，仅 P8 E139/E140 西班牙语句；text.md CJK 0。
- **必查项核实**：
  - (a) P1 框标题：除 EN BREVE 零余量（O2）外无溢出；但同类缺陷在本版另三处复现——D4（P2，+67px）、D5（P7，+13px）、D6（P7，+17px）。
  - (b) P3/P5 右栏奶油框末行降部：P5 数字框 `2027.` 余量 5px、P3/P4/P5 E VOCÊ 框与 P7 词框降部实测在框内（P2 恰止于边行；P4/P5/P7-词框仅 1 个抗锯齿像素越边 1px，肉眼不可见，不计缺陷）；但 P6 时间线框复现同类缺陷 D3（降部越边 6px）。
  - (c) P7 toolbox clearance 实测：3 框，最小框内余量 +4.5px；词框末行墨迹止于边内，读者园地框余量 4px；引言区 clears 预告框（gates PASS，最大基线 2380.67 < 2404）。Toolbox 本身无溢出。
  - (d) text.md 第 E 节：标题 `E · Traduza` 已本地化；全文无 CJK、无「翻譯」/「翻译」残留。未复现。
- **其余判为非缺陷的项**（证据见 GATE-LOG）：P1 `EN BREVE` span 框超 +4.3pt 为字框 advance 含边距，真实墨迹恰止于边（0px）；`Página N de 8` 页脚 +0.6pt、P1 `2026` +0.1pt、`Respuestas en la página 8` +3.6pt、`Los niveles están mezclados` +3.2pt 等 span 框超均为边距假象，PIL 实测墨迹在边内（-5 至 -10px）；P7 A2 gloss 用 ASCII 单引号 `'caer en un día'` 是与 en/de 版一致的 gloss 约定（en `cair means …`、de `bedeutet 'auf…'`），非缺陷；内部标签扫描命中均为误报（`todo(s)` 含 TODO、`sopesar` 含 SOP）。
