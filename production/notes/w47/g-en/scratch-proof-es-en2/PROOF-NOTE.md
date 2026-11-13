# 独立复校笔记 — 2026-W47 es-en（第二轮，proof2，重建版全量重校）

- 版：`production/2026-w47/2026-w47-es-en/`（es re-fanout 重建版，未提交）
- 任务：对重建版做 proof2——从头完整重校，不沿用旧版 proof1 结论；旧版 proof1 曾 (a)。
- 开工探针：`git hash-object -w` 成功（`a7e6fcddc35f16bc353304c0452bcbbe6e604a0e`）；goals 侧 scratch 真实写文件成功。双通后动手。
- 解释器一律 `tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0）；TMPDIR 全程用本 scratch 目录，未写 `/tmp`（除运行时自身工具输出外）。
- 校对范围：印刷 PDF 8 版逐版目视（从印刷 PDF 独立重渲染 96 dpi，不采信 builder 的 cards/）+ 网页 PDF P1/P8 目视；`.text.md` 1,797 行全文读完；150 题逐题验算（三源一致：text.md 答案 == P8 抽取键 == REG 键）；金句 8 条逐字比对；禁词/内部词扫描；VOL.4；徽章逐页计数；P8 最小字号；翻译层专项；U+2019 全扫；孤儿标点全扫；P8 注文人名专项；机械门全套自跑；与旧版（backup-old，SHA 已核为 proof1 旧版）逐页源码/文本/像素三重对比；P1/P2 框题 PIL 真墨实测；外部事实本轮独立再查（UEFA、UNESCO、Sargent、Santa Cecilia）。
- 核心 es 未变复核：core-es 印 `2723a283…138b5`、网 `c2473211…85e235`、text.md `509c95fa…8ddb`，与 re-fanout 报告 §0 逐字一致；core 8 个 SVG 哈希与重建门禁日志一致，未变。

## 身份核对（结论：相符，继续）

| 产物 | 字节 | SHA-256 |
|---|---|---|
| 印 `La-Lucerna-VOL4-es-en.pdf` | 3,500,924 | `80b4ce0a095551599adbf0e8e0c617715513a6df3c6ad004cc1428d8bb99b602` |
| 网 `La-Lucerna-VOL4-es-en-web.pdf` | 886,730 | `f03047b1631fba034e3e65d2804a95c4c4ea40ba6af36a46e312921a7a70b5b0` |
| `2026-w47-es-en.text.md` | 44,983（1,797 行） | `6080c94c420fd1077fedee777bba77ec789fd4c6c431ef70e7b7313923cc8906` |

三件 SHA 与任务书逐字一致 ✓。旧版备份 identity 亦核实：旧印 `e881ebb9…b16`、旧网 `8ab8c66c…a77`，与 proof1 记录逐字一致，备份确为旧 build 5。

## 结论

**(a) 定稿。零问题，可定稿。** 缺陷清单：无。以下观察项单独列，不计缺陷。

## 缺陷清单

（无）

## 观察项（不计缺陷）

1. **栏中空白（继承自 core，非本版引入）**：P3、P5、P6 的第 2 栏中段与 P7 练习区下方有大片空白（P3 col2 在 “LO QUE QUEDA DE NOVIEMBRE” 段后空至练习分隔线；P5 col2 在 Note 框后空；P6 col2 在文章结束后空；P7 三栏练习结束后空至 FRASES 横幅）。版式如此，与 core 一致，无溢出、无重叠、无压线；本轮 P3/P5 像素与旧版 0 差异，P6 空白区未动。
2. **“·” 分隔符（全 programme 通行写法，数量与旧版完全一致）**：旧版 8 个 SVG 共 144 处 “·”，新旧 SVG 文本差分显示无任何含 “·” 的字符串增减，故数量不变，用于 Note 词表内分隔与选择题选项分隔。SOP §1.1 “不用「·」做分隔”针对家具标题行；此用法为 core 既定写法，本版未改动、未新增。
3. **“Your turn” 英译时态微松（意思无损，本轮重读确认）**：P2 “¿Qué harías el lunes 16…?”（条件式）译作 “What will you do on Monday 16 November…”（将来时）；P4 “¿qué miras…?”（现在时）译作 “Which game will you watch…”。任务指令本身清晰无误；P5 “¿Votarías…?” 正确译作 “Would you…?”。
4. **P3 byline 换行（继承自 core）**：本轮 P3 渲染图复见 “Nivel de lectura: A2 → B1” 折为两行，“→ B1” 独占第二行。版式小疵，非本版引入；P3 与旧版像素 0 差异。
5. **P8 答案注文笔风小差异（事实均与题干/选项一致，本轮逐条重读确认）**：#134 注 “Time first”，而 #44/#133 为 “Time first, verb second”；#39 注 “UNESCO announced it in Nairobi in 2010”，#30 注 “UNESCO listed flamenco as heritage in 2010”（同一事实两种说法）；#88 注 “Only the published free-airtime figures” 是对选项 C “solo datos oficiales, con fuente” 的意译。
6. **P8 keys 流终点 y=2569，超出名义底线 2560 约 9px（KIT §6.8 已裁定接受；本轮复核属实）**：run.py 未报 OVERFLOW；末键 150 基线 2553.14、最大墨底 2556.6（PIL 真墨实测），距页脚线 2596 约 39.4px；P8 渲染图目视干净；与旧版完全相同的已接受状态。
7. **P6 图表副题未配英文 gloss（与其它冻结西语内容标题一致）**：“LOS MINUTOS GRATIS EN RTVE　minutos de propaganda por partido” 保持西语，同 P3 “LO QUE QUEDA DE NOVIEMBRE” / “EL FLAMENCO, EN TRES DATOS”、P4 “LA CHAMPIONS VUELVE”、P5 “VOTAR POR PRIMERA VEZ”、P6 “EL CAMINO AL 29N” / “LEER UN DEBATE” 的处理一致（内容标题冻结，只译讲解层）。
8. **P8 注文人名专项（本轮人工核查结果）**：P8 全部 150 条答案注中无任何真人人名。P8 仅有的名字是 C 节阅读短文中的虚构人物 Lucía / Diego（练习虚构人物，与 core 一致，注 #129/#130 即指二人）及球场名 Sánchez-Pizjuán（地名，非人名）。正文 P6 人名（Ana Pastor、Carlos Cuerpo、Juan Bravo、Pablo Bustinduy、José María Figaredo、Isabel Rodríguez）均为冻结 core 文本——本轮新旧 SVG 文本差分证实该段零改动，与已定稿 core 一致。
9. **P6 时间轴 “(sin confirmar)” 措辞（继承自 core，本轮新旧对照无改动）**：时间轴 “16 NOV. — El PP propone el cara a cara Sánchez–Feijóo (sin confirmar)” 对照新文 “Los dos partidos aceptan la cita, pero no hay hora publicada”——“(sin confirmar)” 按 “未敲定” 解仍成立（P6 正文：“las fechas, las horas y los participantes siguen sin cerrarse”；P1：“esta página no da por cerrado lo que aún se negocia”）。非不一致，不计缺陷。
10. **P2 “D　LAS PALABRAS” 标题落在第 3 栏底、内容在第 4 栏（继承版式）**：标题与题身跨栏，本轮 P2 像素差分显示改动只在第 1 栏（特稿段落）， exercises 区零改动，与旧版完全一致。非重建引入，不计缺陷。
11. **WEEKLY-KIT.md §3 仍列旧 build 5 数值（builder 记录滞后，非正文缺陷）**：§3 仍写旧印 3,500,745 B / SHA `e881ebb9…`、旧网 849,020 B / SHA `8ab8c66c…`、text.md 1,779 行；新数值只在 §9 重建一节。建议入仓整理时顺手同步 §3；不影响本版定稿。
12. **P8 #150 行含一个纯空格 `<text>` 元素（构造如此，无渲染）**：`x=1478.8 y=2553.14` 的空格是 “150. ” + “✓” + “ ” + 注文之间的分隔符，P8 渲染图上不可见；新旧差分中新增的 `' '` 即此元素。
13. **D5 字体（只记录、不计入判定）**：拉丁讲解层用 Noto Sans CJK SC（`font-family` 元素计数 635；Newsreader 976；Noto Serif CJK SC 43，含 P8 #150 的 “✓”；UnifrakturMaguntia 1）。生产级待定项，按任务书不计入判定。
14. **creambox 最紧两处墨隙（框内，未溢出，本轮目视复核）**：P2 Note 盒墨底距框底 +0.1px（“escaño = seat in parliament.”）、P5 Note 盒 +0.1px（“box.”），PIL 真墨实测均为正，渲染图上两行均在框内、无压框线。

## 逐项核查结果

### 1. 机械门（全部自跑，输出存本目录，见 GATE-LOG.md）

| 门 | 结果 |
|---|---|
| run.py 重跑（scratch 副本，不碰 shipped） | rc=0；OVERFLOW 0 · TOO WIDE 0；TOTAL 150；A2 50 / B1 72 / B2 28；按页 10/18/18/18/18/18/12/38；按型 48/47/12/8/7/10/13/4/1；MODELO 97 词；P8-keys 终 y=2569；重跑产物 8 个 SVG 与 shipped 逐字节一致 |
| occlusion | **0 flags**；自检 OK（6 类阳性对照全部触发，干净对照静默） |
| p8 extract | **150/150**，rc=0 |
| p8 compare（vs core-es） | **CLEAN**，missing=[] extra=0 uncertain=[]，keydiff=[137, 138]（已裁定：翻译题键重定向为英文句，见 §2） |
| keycheck（REG vs P8 抽取键，跑在 rerun 副本上） | rc=0；149/150 逐字一致，唯一差异 #150（REG 键为开放题占位句，抽取为 “✓”，为设计） |
| freeze baseline | **8/8 字节一致**，rc=0；core 完整性：重哈希 8 文件未变 |
| freeze diff（core vs 本版） | 每页 added CJK 字符均为 0（TOTAL 0） |
| creambox 全扫 + 真墨裁定 | 原始 6 条负值均为已知框下标题（与重建门禁一致）；逐盒真墨裁定：**0 处自有墨溢出**（最小墨隙 +0.1px，见观察项 14） |
| boxtitle（PIL 宽度 + P1/P2 真墨复测） | 25 盒 **0 溢出**；最小余量 +21.3px（P5 “EL PLAN DE LA SEMANA　The plan”）；P1/P2 真墨右缘余量最小 +27.5px（P1 “LA SEMANA EN CIFRAS　Numbers”） |
| sweep（box-vs-hline / bridge orphans / bridge widows） | 0 / 0 / 0（20 座 bridge 全数同栏连续） |
| print/web 文字层 | pdftotext 各 107,966 字节，**逐字节一致**；两版均为 8 页、1462.5×2025 pt；web 886,730 B < 7 MB |
| P8 最小字号 | PyMuPDF + pypdf 双测：**10.125pt**（378 个有效 span），≥ 9.75pt 底线；低于 9.75pt 者 0 |
| 孤儿标点全扫（8 个 SVG 全部 `<text>` 行） | 独行 。/独行右引号 `”` /独行 `：` /独行 `–` 均为 **0**；行首闭合标点亦 0 |
| U+2019 全扫 | U+2019 总数 **0**；U+2018 0；ASCII 撇号 8 处；含撇号行目视无宽字形断裂 |
| CJK 扫描 | 8 个 SVG 可见文本仅 U+3000 ×117（SOP §1.1 分隔符）；汉字 0；唯一汉字在非渲染 `<title>Lucerna 三色蛾</title>`（与 core 一致）；`.text.md` CJK 97，全部为 U+3000 |
| em-dash 提取器假阳性专项 | 抽取键含破折号者仅 #60 “1–2”、#62 “0–2”（比分内的 en-dash，非键–注分隔符），提取正确；无键含 em-dash “ — ”；compare uncertain=[]。es-ru #137 式假阳性本版未遇上 |

### 2. 全量复校
- 印刷 PDF 8 版逐版目视（96 dpi 独立重渲染 `rerender/p-*.png`，1950×2700）：无溢出、无重叠、无压页脚、无截断句、无图片缺失。网页 PDF P1/P8 目视与印刷版一致。
- 150 题逐题验算：题号 1–150 连续（`.text.md` “N. ” 起点 150/150，无缺号、无重号）；按页 10/18/18/18/18/18/12/38；按级 A2 50 / B1 72 / B2 28；按型与 run.py 复跑输出逐字一致。**三源一致**：text.md 答案区逐项含 “N. KEY” 原文（150/150，对 P8 抽取键与 REG 键双向核对；#150 为 “150. ✓ See the model text…”，与抽取 “✓” 一致）；答案键逐题对题面/原文/图表复核，重点复算：#84 合计 45+45+30+30+15+3×10=195（B）✓；#87 45−30=15（B）✓；#86 24–28 为 5 天（A）✓；#83 PSOE/PP 各 45（A）✓；#85 Podemos 15（C）✓；#89 仅 laSexta 一场已敲定（B；SER 辩论 “acordado no es cerrado”，故仍只此一场）✓；#96 Aunque + 直陈式（已知事实）✓；#93 tenga / #94 sea / #95 para que / #109 baje / #110 sea / #111 es / #112 tenga ✓；#97–100 sondeo/muestra/indecisos/margen de error 与词框对应 ✓；#141–144 c/d/b/a 与定义对应 ✓；#60–64 不定过去时 ganó/recibió/perdió/volvió/cerró ✓；#76–79 ir a + 不定式 ✓；#133–136 造句 ✓；#137–140 翻译方向 ✓（137/138 西→英，键为英文句；139/140 英→西，键为西语句）。
- C2 改动题键全验：#3/#9/#22/#65/#116/#123 的 “by the 19th at the latest” 与正文 “hasta el jueves 19” 一致；#139 键 “El voto por correo se pide hasta el jueves 19.” 为 “The postal vote must be requested by Thursday 19 at the latest.” 的正确英→西译；MODELO 同句亦为 hasta ✓。
- 金句 8 条：逐字比对正文，8/8 每条在源页恰出现 1 次 + P7 引用 1 次（逐页 joined 文本核对，全句比对）；英文 gloss 8 条齐全；页码标注（Página 1/2/3/3/4/5/6/6）与出处页相符。
- 禁词/内部词扫描：8 个 SVG 可见文本中 “12 de noviembre” / SOP / proofread / cover / W47 / 2026-w47 / TODO / XXX / lorem / placeholder 均为 0。
- VOL.4：SVG 可见文本中 VOL.4 ×9、VOL.5 ×3（均为下期预告正当引用）、VOL.3 ×0；刊头 196 单位 = 147pt；纸色 #fbfaf6 ×8 版；金色/砖红 0；徽章三色 A2 #5c6e30 / B1 #46581f / B2 #37402f 齐全。
- 徽章逐页计数（rx=2.7 矩形）：P1 10（A2 8/B1 2）· P2 15（A2 13/B1 2）· P3 18（A2 11/B1 7）· P4 15（B1 15）· P5 18（B1）· P6 18（B2）· P7 12（A2 4/B1 4/B2 4）· P8 35（A2 11/B1 21/B2 3）；合计 141 枚 = 150 题 − 3 组共用题多出的 9 项；与 REG 级别合计逐项对上。Q113–150 均有徽章（150 写作题以 ✓ 标记）；无缺失、无错色。
- P8 最小字号：见 §1（10.125pt）。
- 模型文：从 content8.py MODELO 原文逐词数 97 词 ✓（与 KIT 及 run.py 一致）。
- 日期/星期：`date -d` 核验 2026-11-13 周五、16 周一、17 周二、18 周三、19 周四、20 周五、21 周六、22 周日、23 周一、24 周二、25 周三、26 周四、27 周五、28 周六、29 周日，全部与版内星期表述一致。13→27 含首尾 15 天、16→29 为 13 天 ✓；Black Friday 11 月 27 日为周五 ✓。
- ABSTRACT.txt：与旧版逐字节一致；“postal votes by 19 November” 与新 C2 措辞一致，无滞后表述。

### 3. 翻译层专项
- 讲解/界面语言确为英文：masthead 配对、Note 词表、栏目 gloss、“Your turn” 译文、练习说明、P7 三栏 bridge、ERRORES 注、Word of the week gloss、F-MAIL 英文编者注、P6 band gloss、P8 全部 150 条注与标题均英文；逐行核对 `.text.md` 英层，无错译、无漏译。
- 核心 CJK/源语字面量转写：`freeze.py diff` added CJK 每页均为 0；可见文本中 CJK 字符仅 U+3000 全角空格 117 处（SOP §1.1 规定分隔符），无任何汉字；唯一汉字在非渲染 `<title>`（与 core 完全一致）。
- E 组：#137/#138 键为英文句（Monday is International Flamenco Day. / On Saturday we watch the Seville derby.），#139/#140 键为西语句（El voto por correo… / Cada promesa…），方向与题干（137/138 西→英，139/140 英→西）一致；`p8.py compare` 148 键与 core 逐字节相同，唯 [137, 138] 差异（已裁定）。
- 中文残留：除上述非渲染 `<title>` 外，无中文残留（`.text.md` CJK 计数 97，全部为 U+3000 分隔符）。

### 4. 与旧版逐页对比（除重建修复处外无意外变化）
- 备份 identity 已核（见首节）；源码差分：仅 content12.py（26 行）、content56.py（9 行）、content7.py（2 行）、content8.py（12 行）有改动，content34.py / bslib4.py / svglib.py / run.py / render.py 零改动。
- 逐行归类：全部改动对应已记录的 core build 10 变更——C1（P1 CINCO CLAVES 盒 700→720）、C2（`antes del jueves`→`hasta el jueves` 及全部题键/注 “by the 19th at the latest”）、debate 协议新段落（cara a cara 双方接受、无公布时间；Academia 承办两场辩论）、SER 住房辩论已 acordado、RTVE debate-a-ocho 时间轴 INSERT 行（“26 NOV. … de la Academia” 同系）、RTVE 图表注加 “Acuerdo de la Junta Electoral Central del 4 de noviembre”、consejo 句补全（es-ja D1）、来信德比 viernes→sábado（es-ja D4）。无 DELETE、无未记录改动。
- SVG 可见文本差分：P1 +9/−9、P2 +5/−5、P3 0、P4 0、P5 0、P6 +26/−13（段落重写+时间轴 INSERT+图表注换行）、P7 +1/−1、P8 +12/−10（均为 C2 相关键/注/题干/MODELO；+2 为 #139 注换行与 #150 行空格分隔符）。
- 渲染像素差分（96 dpi，阈值 >8）：P1 27,695 px（头条段落+CINCO 盒+图注+consejo 行）、P2 10,118 px（仅第 1 栏特稿段落）、**P3/P4/P5 0 px（像素全同）**、P6 236,919 px（重写段落+时间轴+图表注）、P7 3,238 px（仅来信 “el sábado veo el derbi” 一行）、P8 9,552 px（C2 相关键/注/题干/MODELO 区）。改动范围与源码归类逐项对上，无意外变化。
- de/fr 两版的 boxtitle 溢出类修复（de/fr 各 2 处）与 fr/nl 的 P8 注缩行（各 5 条）——es-en 本轮 boxtitle 0 溢出、P8 注无溢出警告（P8-keys 终 y 与旧版同为 2569，已接受状态），无同类问题。

### 5. 事实核查（公开来源，本轮独立查证）
- 欧冠第 5 轮（UEFA.com 2026/27 赛程页 + NBC Sports）：Real Madrid–PSV 周二 24 日 21:00；Sabah–Barcelona 周三 25 日 18:45；Atlético–Viking 周三 25 日 21:00——与 P4 完全一致；第 5 轮确为 11 月 24–25 日。
- 欧冠第 4 轮赛果（UEFA.com / PSG.fr / Vavel）：Barcelona 3–0 Aston Villa（11 月 3 日）、Atlético 0–2 Bayern（11 月 3 日）、AEK Athens 2–3 Real Madrid（11 月 4 日）——与 P4 “En la jornada 4…” 完全一致。
- Sargent 配图（Google Arts & Culture DMA 记录 + Invaluable 拍卖记录 + Wikipedia 作品录）：确有油画《Spanish Dancer》（1880–81，私人收藏），为《El Jaleo》（1882）前身习作的完成版；P3 图注 “«Bailaora española», cuadro de John Singer Sargent (1880–81)” 准确；作者 1925 年逝世，公有领域 ✓。
- UNESCO 弗拉门戈（UN News 2010-11-16 + ich.unesco.org）：2010 年 11 月 16 日内罗毕会议列入《人类非物质文化遗产代表作名录》——与 P3 完全一致。
- Santa Cecilia（Wikipedia / 多家圣人历）：庆日 11 月 22 日，音乐家主保——与版内表述一致。
- 其它可核事实：国际弗拉门戈日 11 月 16 日、29-N 大选及 RTVE 分钟数为本期情景设定（core 冻结），仅核内部一致性（195 分钟合计 45+45+30+30+15+3×10、5 天禁发期、1 天静默均验算无误）；Pablo Bustinduy（Frente Amplio）为冻结 core 文本，本轮新旧差分证实零改动（proof1 已另用公开来源核实）。

### 6. §8.1 讲解词核查
- 每版 Note 词在当版可见文本中出现次数均 ≥2：P1 reflexión 2 · P2 mitin 2 / cartel 2 / escaño 2 · P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6 · P4 parón 2 / liderato 3 · P5 papeleta 2 / censo 3（大小写合计：小写 2 + 正文 “Censo Electoral” 1）/ plazo 3（与 KIT §3 一致，独立复算）。

## 未碰红线
未改任何源码/成品；未碰 core-es、W43–W46、其它目标语家庭、tools/；未跑 insert.py、lint --write、render.py（原地）；未 git add/commit/push/reset/stash。run.py 与 keycheck 只在 scratch 副本上跑；freeze baseline 自带写穿守卫并复核 core 未变。收尾复核：三件 SHA、8 个 SVG SHA、全部 mtime 与开工快照一致；git 状态仅显示两个未追踪目录，无修改。机械门输出、重渲染件、旧版对比件均只写在 scratch-proof-es-en2/ 内。
