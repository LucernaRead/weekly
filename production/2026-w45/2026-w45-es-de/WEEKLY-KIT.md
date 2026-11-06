# La Lucerna VOL.2 · ES × DE 版工具包（西班牙语正文 + 德语讲解）

读者：德语母语者。底本 = 已发布的 W45 西班牙语核心版 VOL.2（西语正文 + 中文讲解，
`files/weekly-report-w45-es-core/`），冻结复制后只重写讲解层。制作法与 W43 ES×DE 版同门。

## 1. 怎么做出来的

- 复制 `hidden_files/weekly-report-w45-es-build/`（核心版构建）→
  `hidden_files/weekly-report-w45-es-de-build/`；核心版目录与核心版已发 SVG 全程未动。
- 基线证明：未改动的副本经 `tools/freeze.py baseline` 重建 → 8 页 SVG 与已发核心版
  **逐字节相同 8/8**（sha256 见 §7），之后才动讲解层。
- 全部改动走断言式替换脚本 `hidden_files/weekly-report-w45-es-de-build/transform.py`
  （PAIRS + SHORTEN + FIX2 三段，每条模式核对命中；脚本已验证可重跑幂等：
  重跑 278 处 SKIP、exit 0、源码哈希不变）；构建一条命令跑完（见 §8）。
- P8 答案生成代码**字节未动**（破折号体家族：`N. key — note`，分隔符
  `— PÁGINA N —` 沿用 W43 ES×DE 已发版式；见 §6 第 5 条）。

## 2. 交付物与规格

目录 `files/weekly-report-w45-es-de/`：

| 文件 | 规格 |
| --- | --- |
| `La-Lucerna-VOL2.pdf` | 印刷版，8 页，7,162,280 B |
| `La-Lucerna-VOL2-web.pdf` | 网络版，8 页，3,748,613 B（< 10 MB） |
| `cards/p1…p8-*.png` | 1950×2700 PNG 卡片 ×8 |
| `svg/p1…p8-*.svg` | 源 SVG ×8 |
| `ABSTRACT.txt` | 德语单行摘要（见 §9） |

- 全刊 SVG 中汉字节点 = **0**，全角括号 = **0**（程序核查）。
- 图片与核心版逐字节相同（P3 烤栗子 CC0、P5 南瓜 USDA 公共领域各 1 张；
  P1 房屋插图为编辑部程序绘制，非照片，图注保持西班牙语原文）。
- 刊头仍为 "La Lucerna"（西班牙语冠词，不动）；P1 西班牙语 strapline
  `EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA` 原样保留。

## 3. 配对徽章与页脚（照印 W43 ES×DE 注册表，VOL.1→VOL.2）

- P1 徽章（黑带下方，居中，22pt 粗体 BRICK，y=574）：
  „SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER"
- 每页页脚：„La Lucerna · SPANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF SPANISCH · ERKLÄRUNGEN AUF DEUTSCH" / „Seite N von 8"。
- P1 顶栏：„CADA SEMANA EN ESPAÑOL · JEDE WOCHE · SPANISCH, WIE SPANIEN ES LIEST"；
  刊行行（y=330）：„SPANISCHE WOCHENZEITUNG · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL"。
- 黑带右侧：„NOCH 27 TAGE BIS ZUR WAHL · DIE WOHNUNG ENTSCHEIDET" / „TITELTHEMA · SEITEN 2 UND 6"。
- 栏目德语后缀（与 W43 ES×DE 一致）：VIDA · LEBEN、CULTURA · KULTUR、
  DEPORTE · SPORT、JUVENTUD · JUGEND、A FONDO · HINTERGRUND、LENGUA · SPRACHE；
  EJERCICIOS · ÜBUNGEN；„Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen"；
  gloss 前缀 `HINWEIS · `；桥句前缀 `Hinweis · `；instr：填空→Ausfüllen、
  判断→Richtig oder falsch、造句→Sätze bilden、改写→Umformen、翻译→Übersetzen、
  写作→Schreiben、把词和释义配对→Zuordnen。

## 4. 习题注册表

- 总量 **150**，分布与核心版全同：A2 50 · B1 72 · B2 28；分页 10/18/18/18/18/18/12/38；
  题型分布全同（完成句子 48 · 单选 47 · 词汇配对 12 · 判断对错 8 · 造句 7 ·
  句型转换 10 · 完形单选 13 · 翻译 4 · 写作 1）。
- 程序比对（核心版注册表 vs 本版注册表）：page/level/type 差异 = **0**
  （type 为内部键，保持中文原值，与 W43 ES×DE KIT §4 一致）；
  key 差异仅 §5 的重瞄准条目与注德语化；其余全部逐字节相同。
- P8 每条注均为德语；P8 注的括号均为半角（程序核查 0 违规）。
  有 2 条注与核心版的西班牙语部分相同（纯西语变位注、纯算式——本就无语言属性，正确保留）。

## 5. 重瞄准条目（唯一允许动 key/stem 的地方，W43 ES×DE KIT §5 同款）

| # | 改动 |
| --- | --- |
| 137 | ES→DE 翻译：key 改为德语 „Am Montag ist in neun Regionen Feiertag."，注 „Übersetzung" |
| 138 | ES→DE 翻译：key 改为德语 „Am Sonntag sehen wir die NFL und Atlético–Barça."，注 „Übersetzung" |
| 139 | DE→ES 翻译：题干改为德语句 „Das Bernabéu ist Gastgeber eines NFL-Spiels. → ___"；西班牙语 key 逐字节不变，注 „acoger = beherbergen" |
| 140 | DE→ES 翻译：题干改为德语句 „Jede Grafik muss ihre Quelle angeben. → ___"（与 W43 #140 德语句逐字相同）；key 逐字节不变，注 „tener que = müssen" |
| 150 | 写作题注册行改为德语装置句 „Offene Aufgabe — Mustertext unten auf dieser Seite"，注 „Mustertext in Abschnitt H auf dieser Seite (84 Wörter)"；范文（西班牙语 84 词）逐字节不变 |

另：匹配题注统一为 W43 ES×DE 的 P8 式 „wort = deutsche Glosse (Buchstabe)"
（如 „puente = Brückentag, drei Tage frei (b)"），键字母不变。

## 6. 版式决定与全部缩短记录（德语偏长，逐处实测）

1. **P8 答案流（首轮溢出修复）**：德语注使答案流溢出 8 条（末 8 条被压在同一基线
   y=2565.5 重叠，FLOW OVERFLOW ×8）。逐条实测改短 22 条注至 1 行
   （如 #3 „die Wohnung entscheidet den Wahlkampf"、#125 „das DANA-Gedenken
   ist am 29. Oktober"、#117 注删冗余括号 „(das Bernabéu beherbergt die NFL)"
   ——该事实在题干中已在版，判非失真），4 条因 key 本身是整句而保留 2 行
   （#1 冻结西语长键、#44 冻结西语长键、#138 重瞄准德语键、#139 冻结西语长键）。
   结果：答案流末 y=2427（栏底 2552），0 FLOW OVERFLOW。
2. **P1 刊行行字号 46→45pt（仅此一行）**：德语刊行行 46pt 时墨迹 36.1→1913.9，
   压过内框线（1910）；45pt 时 56.5→1893.5，词序与内容分毫不改。
3. **P7 诊所框标题字号 23→20pt（仅此一处，W43 ES×DE 校对修复原样）**：
   „ERRORES TÍPICOS · TYPISCHE FEHLER" 23pt 时墨止 1914.8，越过框右界 1885；
   20pt 时墨止 1857.2，距框界 27.8px。
4. **FIX2（首轮几何审计 3 标记修复）**：德语文本撑出核心版式——P1 词条注释
   2 行擦到 y=1844 横线（裁图证实 p 下伸部被压）；P7 栏 3 过长致预告框压页脚
   （py=2582.6，框底 2700.6 超出页界）；金句 #2/#5/#8 译文 2 行超 128px 固定行距。
   修复：P1 词条注缩为 1 行；诊所注 #2 缩为 1 行；生词注 4 行→3 行；
   读者栏德语说明 6 行→3 行（西语原文披露保留全部事实，含未收到最佳作文）；
   金句 #2/#5/#8 译文各缩为 1 行。结果 P7 栏 3 末 y=1820.08，预告框底 2558.1，
   距页脚线 21.9px。
5. **P8 分隔符取舍**：`tools/tables.json` 的 DE 通用模板为 „— SEITE N —"，
   但 W43 ES×DE 已发版实际使用 „— PÁGINA N —"（FR×DE 用 SEITE，ES×DE 用 PÁGINA，
   各对自有先例）。本版沿用 ES×DE 已发版式，答案生成代码因此保持字节一致。
6. **徽章槽位取舍（见 §7 末，提请父级裁定）**：任务简报引 README #20 称
   ES 核心有 y≈372 原生副标题槽、徽章原位替换 19.5pt；但实测 W43 ES×DE 已发版
   是黑带下方插入式（y=574，22pt），且 y=372 的西语 strapline 在该版中保留。
   本版从 ES×DE 已发版（对内先例），未删 strapline；若父级坚持 372/19.5，
   改动仅为移徽章 + 删 strapline 一行，可低成本返工。
7. **冻结核心原有轻擦（实测，不改）**：
   - P6 右图 „Inmigración" 标签墨迹右界比条形起点多约 5px（条形后画，压住
     末字母 n 右缘约 3–5px），与核心版裁图**逐像素相同**（sha 一致），字母完整可读，
     属核心版式固有轻擦；改动将触动冻结图表与西语标签，故不改，提请校对知悉。
   - P1 目录 „Pág. N" 与标题间距 3.9px：冻结版式与冻结字符串，核心版完全相同，
     间隙为正、无重叠，非缺陷。

## 7. 核查证据

- 基线：`tools/freeze.py baseline --build ../hidden_files/weekly-report-w45-es-de-build
  --core-svg ../files/weekly-report-w45-es-core/svg` → **8/8 逐字节相同**：
  p1 a1b3010296ad129e · p2 10e78c2e6cb29519 · p3 5986ba9e318c985e ·
  p4 1894836e06be824b · p5 cd15c68b5f8db752 · p6 fcfccf8267e10cc7 ·
  p7 b1774024b6a17353 · p8 d1c46fa439ac505d；核心 SVG 事后重哈希无变化。
- 冻结 diff（最终版）：各页 added CJK = 0，全刊 edition CJK = 0；
  移除串中纯西语项逐项核查均为换行碎片（括号、刊行行、注改写）或家具行，
  源码级拉丁词元核查仅 3 处丢失：页脚英文行（注册表德语页脚替换）、OUT 路径
  core→de、#117 注缩短删冗余括号（见 §6.1）；西班牙语正文零增删。
- P8：`tools/p8.py compare` → **CLEAN，150 = 150，missing = []，extra = 0**；
  keydiff 23 项 = 注德语化（#25–28、#52–55、#83、#85、#95、#96、#98、#107、
  #117、#118、#141–144、#148）+ 重瞄准键（#137、#138），逐条复核见 §5，
  其余键逐字节相同；答案键逐题与题干/原文重解一致。
- 几何审计：`tools/occlusion_audit.py`（selftest 全过）→ **0 flags**；
  `--core` 对比 NEW flags = 0。首轮 3 标记（P1 LINEX、P7 LINEX、P7 TEXTX）
  全部为本版德语文本所致，已按 §6.4 修复并复测归零。
- 同基线墨迹扫描：家具带（P1 顶栏／刊头带／黑带／页脚带）同基线相邻墨迹
  间隙除冻结目录 3.9px 外全部 ≥8px，无重叠。
- 图表页逐元素检查：P6 全部条形与标签／数值无覆盖（除 §6.7 冻结轻擦外）；
  左右两图数值右界均在框内（< 框内右界 852）。
- Gloss 计数（按 `·` 本身拆，README #21）：P2 5=5 · P3 5=5 · P4 5=5 · P5 4=4，
  合计 **19=19**，逐项相等。
- P7 金句：8 句西班牙语原文在全刊 SVG 文本中各恰出现 2 次（原文 1 次＋P7 1 次）。
- 读者园地：沿用核心披露与示例信（Ana，示例信标注未动），只译讲解层，
  未编造新读者／信件。

## 8. Build commands（复现）

- 构建目录：`hidden_files/weekly-report-w45-es-de-build/`
  （含断言式转换脚本 `transform.py`；`__pycache__` 已清除）
- 一次性全量构建（单进程，切勿单跑 content 模块——会重启编号）：
  `cd hidden_files/weekly-report-w45-es-de-build && ../../tools/venv/bin/python run.py`
- 渲染 PNG＋PDF：`../../tools/venv/bin/python render.py`
  （render.py 已指向新版目录与 VOL2 文件名）
- 几何遮挡审计：`cd tools && ./venv/bin/python occlusion_audit.py ../files/weekly-report-w45-es-de`
  （记录：`hidden_files/weekly-report-w45-es-de-build/occlusion.json` 首轮 3 flags →
  `occlusion2.json` 修复后 0 flags）
- 冻结 diff 记录：`hidden_files/weekly-report-w45-es-de-build/freeze-diff.json`

## 9. Self-proofread record（自校记录，非定稿证明）

- 全文校对：8 张 SVG 文本提取逐版通读，核对西班牙语拼写／重音、德语讲解
  语法／格／习语、每题答案由题干／选项／原文重新推导、编号连续性、
  全部日期星期、跨版引用（P1→P2/P6、P4→P5、P3→P2/P6、P2 ¿Y TÚ?→P7 来信栏）。
- 视觉校对：8 张 1950×2700 渲染 PNG 全幅目视，核查溢出、重叠、页脚碰撞、
  图表标签截断、P1 插图位置、P6 图表说明入框、P7 第三栏 containment、
  P8 答案块底部余量；另做家具带同基线墨迹间距目视扫描，无同行碰撞。
- 发现并修复的缺陷见 §6（P8 溢出、刊行行压框、诊所标题越框、FIX2 三标记、
  徽章三重套印——转换脚本幂等漏洞所致，已修复脚本锚点并验证重跑幂等）。
- 最终状态：**零已知缺陷**（除 §6.7 两项冻结核心轻擦已记录在案外）。
- **本记录不是定稿证明**：按 SOP §8.4，仍须经过完整独立校对。

## Coordinator adjudication 2026-10-27 — badge slot (FINALIZED, no change)
Independent proof measured three-way: this edition badge (975,574) 22pt BRICK with Spanish strapline y=372 retained = W43 ES×DE shipped edition byte-for-byte in slot, size, color, string and strapline retention. The brief's README #20 372/19.5pt replacement describes the EN-column instance (W43 ES×EN: badge at 372 replacing the strapline), not the DE column. Furniture rule = copy the W43 shipped same-pairing SVG verbatim; forcing 372 would delete target-language masthead text for no reader benefit. ACCEPTED as-is; future ES×DE proofs must NOT re-flag badge slot. P6 Inmigración graze likewise already adjudicated non-blocking known frozen-core defect.
