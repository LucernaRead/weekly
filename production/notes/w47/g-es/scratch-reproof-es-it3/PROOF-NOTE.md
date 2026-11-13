# PROOF-NOTE — W47 es-it fix2 后独立复校（re-proof-3，直撇号专项）

- **版**：2026-W47 es-it（西班牙语正文 + 意大利语讲解）
- **复校员**：独立复校员，与 fix2 修复者不同人；亦与 re-proof（ef27d671，弯撇号轮）不同人
- **探针（开工前通过）**：`ls /dev/null` 存在（字符设备 1,3）；`git hash-object -w --stdin` 通（`e69de29b…`）；本 scratch 真实写文件成功（`probe/test.txt`）。三者皆通后开工。
- **对象（任务书 SHA 与盘上实测一致；复校前后各测一次，未变）**：`~/workspace/weekly-git/production/2026-w47/2026-w47-es-it/`（未 commit；`git status` 仅显示该目录未追踪 `??`，无任何修改）
  - 印 `La-Lucerna-VOL4-es-it.pdf` 3,498,553 B，SHA-256 `12e7e0817b13bdd21576b820bd567b821fb69c679508189b1ef9ba973b442724`
  - 网 `La-Lucerna-VOL4-es-it-web.pdf` 882,084 B，SHA-256 `626e7588389b3c835eec0c8eebde974332ab27a90bca7a0dd2c5ffbdce19f6bd`
  - 文 `2026-w47-es-it.text.md` 45,176 B / 1,806 行，SHA-256 `434e8df8f0d64924b89efe561adcc9406e7b1442e801eee66c16ceeca7f06abe`
- **复校范围**：text.md 全文 1,806 行通读；150 题逐题键—题干手验；8 页印版逐页渲染目视（150 dpi，`renders/p-1.png`～`p-8.png`）+ 网版 P1/P3 渲染目视；全部机械门独立重跑；28 处直撇号逐处核对（字符、位置、字体、渲染）；C1/C2 回归重测；D5 只记录。
- **生产目录只读**：未改任何生产文件，未 commit、未 push。网 PDF 只在 scratch 副本里重渲（`tmp/webrerun/rerun-web.pdf`），绝未覆盖生产目录的网 PDF；交付网 PDF 复核末 SHA 仍为 `626e7588…`。

## 结论：(a) 定稿 — 零发现

re-proof 的唯一缺陷 E1-空隙（12 处弯撇号 sans 空隙）已消除：本轮独立重测 12 处 sans 词内最大墨隙全部 6–7px（弯版 24–29px），目视全部紧贴；Newsreader 对照 2–3px。其余全部机械门绿（见 GATE-LOG.md）。按 repo `AGENTS.md`（定稿须一轮零发现复校），本版可定稿。无缺陷清单。

| 门 | 结果 | 证据位置 |
|---|---|---|
| run（scratch 副本） | rc=0，TOTAL 150（A2 50 / B1 72 / B2 28；页 10/18/18/18/18/18/12/38） | `run-copy.log`（副本已清，日志留存） |
| SVG 重建一致性 | 副本重建 8/8 与 shipped 字节一致 | `run-copy.log` 下 `identical` 8 行 |
| SVG vs refanout | 8/8 逐字节一致（fix1 的 `svg-BEFORE.sha256`） | `svg-now.sha256` + §1 |
| 印/文 vs refanout | 逐字节一致（fix1 的 `SHA-BEFORE.txt`） | §0 |
| occlusion | 0 flags（自检 6 类全触发） | `it-occlusion.log` / `it-occlusion.json` |
| p8 extract | 150/150，[1..150] 连续 | `it-p8-extract.log` |
| p8 compare（vs core-es） | CLEAN，keydiff=[137, 138]（已裁定，见 §2） | `it-p8-compare.log` / `it-p8-compare.json`（本体已读） |
| freeze baseline | 8/8 OK，core SVG 未变 | `it-freeze.log` |
| freeze diff | CJK 新增 6，全为 U+3000（P1–P6 各 1，P7/P8 为 0） | `it-freeze-diff.log` |
| creambox | 6 处负余量：5 处假阳性 + C1（见下） | `it-creambox.log` |
| creambox_diag | 0 负真墨余量；C1 真墨余量 **+3.8** | `it-creambox-diag.log` |
| boxtitle | 0 溢出，最小余量 +14.4 | `it-boxtitle.log` |
| keycheck | 149/150，仅 #150 ✓ 例外 | `it-keycheck.log` / `keycheck-150.json` |
| 印/网文字层 | `pdftotext -layout` 逐字节一致，108,723 B | `it-print.txt` / `it-web.txt` |
| 网重渲（scratch 副本） | 文字层与交付逐字节一致，882,091 B；SHA 不同属已知非确定性（见 §6） | `webrerun.log` / `webrerun-web.txt` / `tmp/webrerun/rerun-web.pdf` |
| P8 最小字号 | 10.125 pt（n=375），<9.75pt 为 0 | `it-minfont.log` |
| sweep（桥接/孤儿/寡行） | 0 / 0 / 0 | `it-sweep.log` |
| 孤儿标点全版扫 | SVG 0，text.md 0 | 本文件 §5 |
| 150 题三源逐题手验 | 150/150 通过 | 本文件 §4 |
| 范文词数 | 97 词（P8 SVG 实数，去“Texto modelo:”后；run.py 同值） | 本文件 §4 |
| C1 回归 | 真墨余量 +3.8，非真溢出 | §3 |
| C2 回归 | 已修：`antes del jueves` 0 处，`hasta el jueves 19` 5 处 | §3 |

## §0 SHA 链（独立实测）

| 文件 | 任务书 fix2 SHA | 盘上实测（开工 / 收工） | refanout（fix1 `SHA-BEFORE.txt`） |
|---|---|---|---|
| 印 PDF | `12e7e081…` / 3,498,553 B | 一致 / 一致 | `12e7e081…` —— **逐字节一致** |
| 网 PDF | `626e7588…` / 882,084 B | 一致 / 一致 | `17d4b8ef…` / 882,077 B —— SHA 不同，属已知 webpdf 非确定性（见 §6），文字层与重渲一致 |
| text.md | `434e8df8…` / 45,176 B / 1,806 行 | 一致 / 一致 | `434e8df8…` —— **逐字节一致** |

## §1 E1-空隙修复验证［本轮核心］— 12 处 sans 空隙已消除

**独立复测（fix2 的自报只当线索，以下全部是我自己的实测；方法与 fix2 不同：词坐标取自印版 `pdftotext -bbox` 的词框，我自己的脚本 `measure3.py`，墨 = 亮度 <128，词框内墨迹列轮廓）**：

| # | 页 | 词 | 弯版间隙（re-proof） | 本轮直版间隙 | 目视 | 裁图 |
|---|---|---|---|---|---|---|
| 1 | P1 | `L'EDIZIONE`（刊头配文，16pt） | 24px | **6px** | 紧贴 | `crops/rp3-P1-LEDIZIONE.png` |
| 2 | P2 | `l'articolo`（桥接句，20.5pt） | 28px | **6px** | 紧贴 | `crops/rp3-P2-larticolo.png` |
| 3 | P3 | `l'anima`（gloss 行末，20.5pt） | 28px | **6px** | 紧贴 | `crops/rp3-P3-lanima.png` |
| 4 | P3 | `l'articolo`（桥接句，20.5pt） | 28px | **6px** | 紧贴 | `crops/rp3-P3-larticolo.png` |
| 5 | P4 | `l'articolo`（桥接句，20.5pt） | 28px | **6px** | 紧贴 | `crops/rp3-P4-larticolo.png` |
| 6 | P5 | `l'urna.`（gloss 行末，20.5pt） | 29px | **6px** | 紧贴 | `crops/rp3-P5-lurna.png` |
| 7 | P5 | `l'articolo`（桥接句，20.5pt） | 28px | **6px** | 紧贴 | `crops/rp3-P5-larticolo.png` |
| 8 | P7 | `L'ora:`（解说行首，20.5pt） | 28px | **6px** | 紧贴 | `crops/rp3-P7-Lora.png` |
| 9 | P7 | `l'indicativo.`（解说，20.5pt） | 29px | **6px** | 紧贴 | `crops/rp3-P7-lindicativo.png` |
| 10 | P7 | `L'una`（解说，19.5pt） | 27px | **7px** | 紧贴 | `crops/rp3-P7-Luna.png` |
| 11 | P7 | `d'errore,`（例句，19.5pt） | 26px | **6px** | 紧贴 | `crops/rp3-P7-derrore.png` |
| 12 | P8 | `un'unica`（H 组头注，20.5pt） | 29px | **0px** | 紧贴 | `crops/rp3-P8-ununica.png` |
| 对照 | P8 | `Dov'è`（Newsreader 13.5pt） | 3px | **3px** | 紧贴 | `crops/rp3-P8-Dovè.png` |
| 对照 | P8 | `l'urna?`（Newsreader 13.5pt） | 3px | **2px** | 紧贴 | `crops/rp3-P8-lurna.png` |
| 网 | P1 | `L'EDIZIONE` | 24px | **6px** | 紧贴 | `crops/rp3-WEB-P1.png` |
| 网 | P3 | `l'anima` | 28px | **6px** | 紧贴 | `crops/rp3-WEB-P3.png` |

- 测量口径说明：本轮词框取自印版 bbox（如 P1 `L'EDIZIONE` 框 pt [777.4, 446.6, 841.5, 464.0]，词宽 129px），与 fix2 的裁图盒坐标独立来源、数值一致（fix2：12 处 6–7px；本轮 11 处 6px、1 处 7px、1 处 0px）。P8 `un'unica` 0px 是因我的词带更贴词框（±4px），撇号墨与相邻字母在 150dpi 下无空白列——目视确认紧贴，无反向问题；fix2 同处测 6px，同为“紧贴”结论。
- 全部 16 处裁图（12 sans + 2 Newsreader 对照 + 2 网版）均已目视，无一处可见空隙。弯版同坐标的 24–29px 空隙已不存在。
- **撇号三处独立重数**：text.md 直 **28** / 弯 **0**；SVG 直 **28** / 弯 **0**（P1 1、P2 1、P3 2、P4 1、P5 2、P6 0、P7 4、P8 17）；印版文字层直 **28** / 弯 **0**；网版文字层直 **28** / 弯 **0**；印版 `-bbox` 含直撇号的词 **28 个**，与 re-proof 28 处表逐词对应。源文件弯 **0**（content12 2直、content34 5直、content56 6直、content7 6直、content8 19直——其中 9 处正文 + 10 处代码引号）。content8.py:133/135 代码引号 `e_['n']` 未动（实测行文与 fix1 报告一致）。
- **版式变化核实（fix2 声称的两处，皆属实、无溢出）**：(1) P1 刊头配文行 middle-anchored，起始 x 657.5（回 refanout 值，弯版 650.9），同 y，仍居中——SVG 实测 `x=657.5`；(2) P3 Nota gloss 重排逆转回 refanout 形态：行 1 以 `l'anima` 结尾、行 2 `del flamenco.`——SVG 实测两行原文如此，P3 全页目视干净。
- **改动范围核实**：text.md 与 refanout 逐字节一致（SHA §0），故 fix2 相对 refanout 的净改动为 0；相对 fix1 弯版的差异仅为 28 处字符 + 1 处重排（fix2 报告，SHA 链佐证：印/文双双回到 refanout）。

## §2 p8 compare keydiff [137, 138] 裁定（与 re-proof 同结论，本轮独立重测通过）

- 本轮直接读 `it-p8-compare.json` 本体：`status: CLEAN`，`missing: []`，`extra: []`，`uncertain: []`，`keydiff: [137, 138]`。
- 核心键实测（core-es P8 SVG）：137. `周一是国际弗拉门戈日。`、138. `周六我们看塞维利亚德比。`——中文译句。
- 本版键：137. `Lunedì è la Giornata internazionale del flamenco.`——题干 `El lunes es el Día del Flamenco. → ___`（西→意翻译题），键与题干逐句对应，正确；138. `Sabato guardiamo il derby di Siviglia.`——题干 `El sábado vemos el derbi Sevilla–Betis. → ___`，对应正确。差异纯因读者语不同。

## §3 C1 / C2 回归重测

- **C1（P1 CINCO CLAVES 工具盒）**：本轮 `creambox_diag.py` 独立重测：盒 `y=588` 盒底 **1308.0**、OWN 末行基线 1300.0（余量 +8.0）、**真墨底 1304.2、真墨余量 +3.8**（`it-creambox-diag.log` P1 第 2 行，与 fix2/re-proof 测值逐字一致）。全版 0 负真墨余量（最小 +0.1，P2/P5 `y=939` 盒）。naive creambox 的 6 处负余量与 re-proof 同值同位置，皆为假阳性（下一栏目标题 / 插图图注，diag owner-rect 佐证）。C1 不复现。
- **C2（`antes del jueves 19`）**：已修。本版 text.md 中 `antes del jueves` **0 处**，`hasta el jueves 19` **5 处**。C2 不复现。

## §4 150 题三源逐题手验（150/150 通过）

方法：text.md 全文 1,806 行通读 + 每题题干对答案键逐题核对（三源：content 源题干 / text.md 答案区 / P8 SVG keys；keycheck 149/150 + p8 extract/compare 机械佐证，#150 ✓ 例外为开放写作题）。因本版 text.md 与 proof1/re-proof 已核实的 refanout 文逐字节一致，手验逐项复核无变化；以下为本轮逐项核对记录。

- P1（1–10）：13 / 29 / 19 / 16 / 20 / 15 / C·29日 / B·15天 / A·19日 / B·16日——全对（与头条“13 天”、15 天竞选、19 日截止、16 日弗拉门戈日一致）。
- P2（11–28）：16 / 19 / 29 / 22 / noviembre / empieza / dura / vuelve / recorren / llega / B·16日 / A·19日 / C·20日 / B·24–28 / c·dibattito / b·comizio / d·cartellone / a·seggio——全对。
- P3（29–46）：V / V / F（非仅舞蹈）/ F（圣塞西莉亚 22 日非 16 日）/ V（毕尔巴鄂乐队 22 日 12:00）/ cante / baile / guitarra / palmas / compás / B·Nairobi / A·duende 时刻 / C·Andalucía / B·29 日选举 / 43–46 造句（语序 S-V-O / 时间前置 / 地点前置 / 间接疑问 si）——全对。
- P4（47–64）：A·33 分 / B·20–23 日 / C·18:30 / A·周日 14:00 / B·24–25 日 / c / b / a / d / más importante / muchísimos / peor / mejor / ganó / recibió / perdió / volvió / cerró——全对。
- P5（65–82）：B·19 日 / A·9 日 / C·9:00–20:00 / B·MiDNI / A·27 日 / correo / papeleta / envío / identidad / censo / plazo / Voy a pedir / Vas a votar / Va a abrirse / Van a comparar / V（Correos）/ F（静默日周六 28 非周日 29）/ V（MiDNI）——全对。**Q73 重点核**：题干 `Para votar en persona llevo mi documento de ___.`，键 `identidad`（→ documento de identidad），答案区 `73. identidad — documento de identidad = documento d'identità`，键—题干适配，正确。
- P6（83–100）：A·各 45 分钟 / B·195 分钟（45+45+30+30+15+3×10=195，自洽）/ C·Podemos 15 / A·5 天 / B·15 / C·官方数据+来源 / B·仅 laSexta 已确认 / A·13 日 21:30 / C·提议≠确认 / B·foto con margen d'errore / tenga / sea / para que + subjuntivo / Aunque + 直陈 / sondeo / muestra / indecisos / margen de error——全对。
- P7（101–112）：Es / Son / las / B·Es la una / más goles / tan rápido / mejor / B·más mejor 错 / baje / sea / es / B·tenga——全对（101–104 与 P7 解说“Es la una 单数、Son 复数”一致；111 creo que + 直陈 es；112 ojalá + 虚拟 tenga）。
- P8（113–150）：A·suena / B·empieza / A·21:30 / A·19 日 / A·vuelve / B·周六 / A·músicos / A·vota / A·13 日 / B·16 日 / A·19 日 / C·18:30 / B·27 日 / C·应用 / B·24–28 日 / C·24–25 日 / A·Lucía / A·Diego / A·读纲领 / B·《两城一星期六》/ 133–136 造句 / 137–140 翻译（137/138 见 §2；139 西译正确、140 意→西正确）/ 141 c / 142 d / 143 b / 144 a / **145 A·votar** / **146 A·identidad** / **147 A·urna** / A·sobre / A·cierra / 150 ✓ 范文——全对。
- **两处涉键改动重点验**：146 题干 `— ¿Tiene su documento de ___? (A. identidad · B. puente)`，键 `A — documento de identidad = carta d'identità`：`carta d'identità` 为 `documento de identidad` 的正确意译，键—题干适配；P8 目视该键行紧贴无空隙。147 题干 `— ¿Dónde está la ___? (A. urna · B. guitarra)`，键 `A — ¿dónde está la urna? Dov'è l'urna?`：`Dov'è l'urna?` 为 `¿Dónde está la urna?` 的正确意译，适配；P8 目视紧贴（本轮 Newsreader 对照裁图 `crops/rp3-P8-Dovè.png`，间隙 3px）。
- 范文（H 组）：P8 SVG 实数 **97 词**（10 个文本元素共 99 词，含头注 `Texto modelo:` 2 词），在 80–100 词要求内，与版面标注“97 parole”一致；run.py `MODELO words: 97` 佐证。
- 全文通读未发现与 proof1 已核实外部事实矛盾的新表述；未独立锁定的两项沿用 proof1（RTVE 195 分钟逐项第二来源；Sargent 图年份 1880–81 到年精度），不列缺陷。

## §5 其余核查（均有实测）

- **孤儿标点**：SVG `<text>` 元素全扫（纯标点元素、行首闭标点）**0**；text.md 纯标点行 **0**。
- **引号**：本轮实测 text.md 直双引号 U+0022 **0**；弯引号 « » 各 56，成对，无落单。
- **禁词/内部语义**：本轮通读 text.md 未见 SOP / proofread / cover / 仓库链接等内部词；VOL.4 印刷层 + 刊头（合法）；VOL.5 均为下期预告（合法）。
- **题量分布**：P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38，合计 150；级别 A2 50 / B1 72 / B2 28（与 run.py REGISTRY 一致）。
- **ABSTRACT.txt**：意大利语单行（沿用 re-proof 结论，本轮未见改动：text.md SHA 与 refanout 一致）。
- **日期星期**：沿用 proof1 逐项校验，本轮通读未见改动（text.md 与 refanout 逐字节一致）。
- **8 页目视**：印版 8 页逐页渲染（`renders/p-1.png`～`p-8.png`）全部目视：P1 刊头配文 `L'EDIZIONE` 紧贴；P3 gloss 重排正确；P5 Q73 行正常；P7 四处撇号行紧贴；P8 146/147 键行紧贴、答案区完整。除 E1-空隙已修复外无新增视觉缺陷。P3/P4/P7 中栏留白为 refanout 原有版式，非新缺陷。
- **D5 字体（只记录，不判 (b)）**：SVG `<text>` 字体分布 Newsreader 973、Noto Sans CJK SC 632、Noto Serif CJK SC 43、UnifrakturMaguntia 1——与 re-proof/fix2 实测分布逐数一致。D5 全周级已知待定项，只记录。

## fix2 评价（供协调员参考）

- 28/28 整批 revert 准确（逐处皆为意语省音直撇号、无一错改、无一漏改）；代码引号 10 处正确排除；改动范围干净（印/文双双回到 refanout 逐字节一致，SVG 8/8 回到 refanout）；全部机械门绿；SHA 链完整；渲染自查充分（13+2 处裁图 + 像素实测）。本轮以独立方法（bbox 词框取坐标）重测，数值与 fix2 自报一致（6–7px sans、3px Newsreader）。fix2 的修复完整、可定稿。
