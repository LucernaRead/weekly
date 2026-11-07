# La Lucerna VOL.1 · ES × DE 版工具包（西班牙语正文 + 德语讲解）

读者：德语母语者。底本 = 已定版的西班牙语核心版 VOL.1（西语正文 + 中文讲解，含其 §12 P7 诊所补丁与 §13 P8 页脚补丁），冻结复制后只重写讲解层。制作法与 FR×DE / EN×DE 同门版完全一致。

## 1. 怎么做出来的

- 复制 `hidden_files/weekly-report-es-build/`（核心版补丁后构建）→ `hidden_files/weekly-report-es-de-build/`；核心版目录全程未动。
- 基线证明：未改动的副本重建 → 8 页 SVG 与已发布核心版**逐字节相同**，注册表 150 条全同。之后才动讲解层。
- 全部改动走断言式替换脚本（每条模式核对命中次数）；构建一条命令跑完（见 §11）。

## 2. 交付物与规格

目录 `files/weekly-report-es-de/`：

| 文件 | 规格 |
| --- | --- |
| `La-Lucerna-VOL1-DE.pdf` | 印刷版，8 页，5,799,784 B |
| `La-Lucerna-VOL1-DE-web.pdf` | 网络版，8 页，3,940,099 B（< 10 MB） |
| `cards/p1…p8-*.png` | 1950×2700 PNG 卡片 ×8 |
| `svg/p1…p8-*.svg` | 源 SVG ×8 |

- 全刊可见字符 43,931（核心版同法计 37,488）；最终 SVG 中汉字节点 = **0**，全角括号 = **0**。
- 图片与核心版逐字节相同（每页 `<image>` 数据比对一致），图注保持西班牙语原文。
- 刊头仍为 "La Lucerna"（西班牙语冠词，不动）。

## 3. 配对徽章与页脚（照印）

- P1 倒计时黑带下方砖红色徽章（居中，22pt 粗体）：
  „SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
- 每页页脚：„La Lucerna · SPANISCHE WOCHENZEITUNG VOL.1 · TEXT AUF SPANISCH · ERKLÄRUNGEN AUF DEUTSCH" / „Seite N von 8"。
- P1 顶栏：„CADA SEMANA EN ESPAÑOL · JEDE WOCHE · SPANISCH, WIE SPANIEN ES LIEST"；版次行：„SPANISCHE WOCHENZEITUNG · VOL.1 · EL RELOJ · EL CLÁSICO · LA F1"（核心版该行下方的中文标语行由徽章取代，同 FR×DE 先例）。
- 黑带右侧：„EINE STUNDE MEHR SCHLAF · UND DER CLÁSICO" / „DREI TERMINE IN EINER NACHT · SEITEN 2 UND 4"。

## 4. 习题注册表

- 总量 **150**，分布与核心版全同：A2 52 · B1 70 · B2 28；分页 10/18/18/18/18/18/12/38；题型分布全同。
- 程序比对（核心版注册表 vs 本版注册表）：page/level/type 差异 = **0**；key 差异仅 3 条 = §5 的重瞄准条目；其余全部逐字节相同。
- P8 每条注均为德语；每条注的括号均为半角且括号前有空格（程序核查 0 违规）。有 6 条注与核心版相同（#60–63 纯西语变位注、#87 纯算式、#103 纯西语注——本就无语言属性，正确保留）。

## 5. 重瞄准条目（唯一允许动 key/stem 的地方）

| # | 改动 |
| --- | --- |
| 137 | ES→DE 翻译：key 改为德语 „Am Sonntag schlafen wir eine Stunde länger."，注 „Übersetzung (Original Seite 1)" |
| 138 | ES→DE 翻译：key 改为德语 „Am Montag ist in neun Regionen Feiertag."，注 „Übersetzung (Text Seite 3)" |
| 139 | DE→ES 翻译：题干改为德语句 „Der Clásico wird am Sonntagabend um neun Uhr angepfiffen. → ___"；西班牙语 key 逐字节不变 |
| 140 | DE→ES 翻译：题干改为德语句 „Jede Grafik muss ihre Quelle angeben. → ___"；key 逐字节不变 |
| 150 | 写作题注册行改为德语装置句 „Offene Aufgabe — Mustertext unten auf dieser Seite"，注 „Mustertext in Abschnitt H auf dieser Seite (82 Wörter)"；范文（西班牙语 82 词）逐字节不变 |

另有一处字形规范化：P7 示例信中西班牙语括号由全角改为半角（词句逐字不变），使全刊全角括号归零。

## 6. 版式决定与全部缩短记录（德语偏长，逐处实测）

1. **P8 答案流**：德语注使 21 条答案由核心版 1 行变 2 行，末栏溢出至 #145–150。逐条实测改短 16 条注至 1 行（如 #5 „empatados = punktgleich (je 7 Punkte)"、#88 „unsere Quelle nannte Sumar/Podemos im CIS nicht"、#91 „eine Umfrage ist ein Foto mit Fehlermarge"），5 条因 key 本身是整句而保留 2 行取最短注（#44/#45/#78/#137/#138）。结果：答案流末 y=2472（栏底 2552）；四栏最低基线 2535.6 / 2534.7 / 2521.6 / 2456.2，距页脚线（2580）墨迹净空 40.3 / 41.2 / 54.3 / 119.7 px，全部 ≥40 px（逐栏实测自最终 SVG，非流光标）。键字号未动（与核心版同为 13.5）。
2. **P6 习题流**：§A 桥句改 „Lies die Grafiken und wähle richtig."（1 行）；§D 桥句改 „Setze ein: sondeo · media · indecisos · margen de error"（2 行，词表并入桥句）；P6 习题间距 gap 3→1（仅 P6 的 size=19 调用，共 18 处）。结果末 y=2561（栏底 2580），核心版为 2571。
3. **P7 右栏**：诊所 4 条德语注、Palabra 注、Carta 注逐条按核心版行数实测改短至同行数（诊所各 1 行；Palabra/Carta 各 2 行，如 „empatar = unentschieden spielen. Zweimal: Stuttgart und Austin."）。结果右栏末 y=1663.96，与核心版**分毫不差**，短语区横线无碰撞。
4. **P2 框题**：„LA FRASE PARA RECORDAR · MERKSATZ" 实测宽 412.5 > 框内宽 398（渲
...[truncated 2132 chars]

---

## 独立校对记录（Independent proofread, 2026-10-21）

校对人：独立校对 subagent（fresh pass，不采信 builder 自述，全部实测）。结论：**修订 1 处版式缺陷后，第二遍完整校对零问题，本版定稿。**

### 发现并修复的 1 个问题
- **P7 诊所框标题溢出框线**：「ERRORES TÍPICOS · TYPISCHE FEHLER」在 fs 23 下墨迹 x 1473.0→**1914.8**，越过框右界 1885 达 29.8px（核心版同标题墨止 1802.2）。builder 的 KIT 未记录此问题。修复：`content7.py` 该标题字号 23→20（仅此一处源码改动），重渲后墨止 **1857.2**，距框界 27.8px；其余 7 页 SVG 与修复前逐字节一致，登记表统计不变。修复后 P7 卡图目检通过。

### 核心完整性（对冻结核心版 es-vol1 逐页可见文本多重集 diff）
- 两版 SVG 均可由各自源码在沙盒中逐字节重建（先验证再比对）。
- 所有被移除的核心版字符串均为中文讲解层；唯二外文重排经逐字核对无损：P5 选项 "camiseta el sábado."（DE 版跨元素折行）、P6 §D 桥句 "indecisos · margen de error"（DE 版桥句改排）。9 处全角括号/标点片段逐个定位到 DE 版对应半角文本（含 #18/#20/#102 的 „(ellos-Form)"/„(él-Form)" 自然德语化），西班牙语正文零增删。
- 登记表：两版各 150 题，A2 52 · B1 70 · B2 28，各页 10/18/18/18/18/18/12/38。键值差异仅合法项：#137/#138 德语译文键、#150 登记行德语；#139/#140 德语题干、西语键逐字节同核心版。**150 题键+注逐条与核心版对照并全部重解**（含 P2 匹配 25b/26d/27c/28a、P4 匹配 52b/53d/54a/55c、P8 §F 141c/142d/143b/144a 对照印出选项核验）。16 条 P8 缩短注逐条与核心版比对：内容无损（#56 注删举例括号、#89 注删「2023 预算顺延」——该事实在 P6 正文逐字在版，均判非失真）。注前空格违规 0。
- 讲解层：DE 版全部 SVG 原始文本 CJK = 0、全角字符 = 0；P1–P8 全部讲解（HINWEIS、读者注、诊所、图表注、P7 栏目注）逐段读毕，德语语法/格/习语自然。事实点：欧洲进球总数 **40**（P4 正文+P8 #57 注，无 38 残留）；国家德比 10 月 25 日周日 21:00 Spotify Camp Nou；半岛 03:00→02:00 与加那利 02:00→01:00 全版分开表述（正文、习题 #121/#122 键均然）；写作范文与核心版逐字节一致，实测 **82 词**。
- P7 短语：8 条西班牙语短语逐条程序核验，各在其标注来源页 + P7 各出现恰 1 次（共 2 次），页码标注全对。
- 徽章：P1 刊头 „SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER" 在版（墨 y 552–574，与黑带下沿 542 留 10px 气口，无重叠）；8 页页脚均标注配对（„TEXT AUF SPANISCH · ERKLÄRUNGEN AUF DEUTSCH" + „Seite N von 8"）。
- P6 流程末端：墨底 2559.0（末行基线 2554），高于核心版 2571 流程口径，无碰撞；图表柱长实测 Demócrata/CIS 两图均 ≈12.0 px/%（31.7→380、26.8→322、18.7→224、6.3→76、3.1→37；34.0→408、22.2→266、17.1→205），两列未混。

### 几何/遮挡审计（自建审计脚本，真实字形度量，绘制顺序；builder 与核心版同跑）
- 覆盖（≥30%，乃至 >1%）：两版 0。页脚带（y>2580）侵入：0。文本–文本重叠：0。页框穿越（墨越 1885/64）：修复后 0（修复前仅上述标题 1 处）。
- P8 各栏距页脚线实测净空：栏1 40.4px（末墨 2539.6）、栏2 41.3px（2538.7）、栏3 58.4px（2521.6）、栏4 120.8px（2459.2）——builder 所报基线（2535.6/2534.7/2521.6/2456.2）逐一吻合，净空口径（40.3/41.2/54.3/119.7）为保守值，实测 ≥ 其值，全部 ≥40px。
- builder 所报 3 个审计标记复核裁定：① 徽章带 2 处「0.6px 名义」——定稿 SVG 实测徽章与黑带间有 10px 气口，无重叠，良性；② 继承项 1 处 = **P1 词条 gloss 第二行下方的全宽发丝线（y=1844，基线 1841.85）**：线仅擦过括号脚与字母 g 的下伸尾端约 2–3px，字身完整、完全可读；核心版同位置同几何（中文 gloss 同擦逗号脚），双版裁图目检一致——判继承性轻微擦碰，非本版缺陷，不阻定稿。
- 图片：P1/P3/P5 三图嵌入载荷与核心版逐字节一致，署名行（西班牙语）一致。

### 产物（修复后）
- print PDF 5,799,789 B · web PDF 3,939,751 B，均 8 页。
- 注：本 KIT 的 builder 部分（§6 第 4 条）在磁盘上于句中截断（"…框内宽 398（渲" 止），其后内容缺失；本记录独立成段，不依赖该尾段。

## 事实订正（2026-10-21）：P5「jueves 23」→「viernes 23」

- **错误**：第 5 版西班牙语正文（与核心版逐字节相同）称 eFootball 球衣「desde el jueves 23」——2026 年 10 月 23 日实为**星期五**。ES×FR 独立校对发现；核心版与 EN/DE/FR 三个讲解版同日同步订正（本版改动在 `content56.py` 第 19 行，仅此一词）。
- **核验**：先证基线（未修改构建逐字节复现 8 张定稿 SVG）；渲染差异仅 `p5-juventud.svg` 一个文本元素、仅 P5 卡片重出，其余逐字节不变。注册表扫描无题目引用该星期说法；第 80 题（Verdadero，题干仅称「desde el 23 de octubre」）复解仍成立；P7 金句仅引「sábado 24」（正确）。几何：改动行墨迹右界 433→446px，距栏界余 53px；遮挡审计第 5 版 0 标记（第 1 版既有模型标记经像素实测非缺陷，与本次无关）。
- **产物（订正后）**：印刷 PDF 5,799,786 B（sha256 `d74580939950d1659ab898626d496b7a952b935a1933dd8dc19a79844a5073d2`）；网页版 PDF 3,939,899 B（sha256 `1e76afa94048a99efb80061d2ace95f623f1dacc29d40f8d8d5cf48b36d160f3`），均 8 版。GitHub 仓 `2026-w43-es-de` 已同步换 PDF 并更新 pin（附订正说明）。
