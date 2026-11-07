# 独立校对报告 — W45 DE×IT（德语正文 × 意大利语讲解）VOL.2

## 结论：ZERO PROBLEMS（可定稿）

校对对象：`files/weekly-report-w45-de-it/`（svg×8、cards×8、双 PDF、WEEKLY-KIT.md、ABSTRACT.txt）。
对照核心：`files/weekly-report-w45-de-core/`（VOL.2）。SOP 与工具箱按 `tools/README.md` #7–#22 执行。
构建员自述一律未采信；以下全部数值为本校对从渲染产物/SVG 坐标独立重测。

开工查重：20:48（UTC）首次检查时无 de-it 写盘进程；20:49 复查发现一个 `render.py` 在跑，
经 `/proc` 核实其 cwd 为 `hidden_files/weekly-report-w45-de-pt-build`（DE×PT 分版，与本版无关），
de-it 目录自 20:47 起零新写盘。按任务规则（完成交付的新鲜时间戳不是 stand-down 理由）正常开工。
校对期间未写 de-it、未碰 weekly-git、未改核心/W43 目录、未发 Discord、未往主聊天发卡片/PDF、未建 cron、
未派生下级代理。校对所用脚本与中间结果仅存于本报告同目录 `scratch/`。

## 必查门实测值

### 1. Freeze — 通过
- `tools/freeze.py baseline`（核心 build `hidden_files/weekly-report-w45-de-build`，重定向到 proof scratch 执行，
  未在核心 build 目录内 import 任何模块）：**8/8 SVG 字节复现**，核心 SVG 事后重哈希 8/8 不变。
- 核心哈希（校对前后一致，与 KIT §2 前 16 位全符）：
  p1 `6cbd48022b5f863d` · p2 `9362256dca74f877` · p3 `3e8a8d16136a46a3` · p4 `b787f592599cc4d1` ·
  p5 `4dcbeb97c566f4df` · p6 `01b75ad49a54c803` · p7 `fbaf8cdd8a90f299` · p8 `299524bd2ad25ec4`。
- `freeze.py diff` 核心 vs 分版：p1 +23/−23 · p2 +36/−32 · p3 +41/−40 · p4 +26/−22 · p5 +44/−39 ·
  p6 +37/−33 · p7 +58/−53 · p8 +157/−141；**新增 CJK 0/页，分版 SVG CJK 总计 0，全文“桥接”出现 0 次**。
- P1–P7 移除的非 CJK 字符串逐项核查：仅 4 类——(a) P1 德语 strapline（见门 7，W43 同配对版已发先例的家具替换）；
  (b) P3/P4/P6 各 1 个孤立 `。`（中文句号，意大利语 gloss 句末改用 `.`）；(c) P7 标签 `Ein Beispiel der Redaktion!` →
  意大利语标签、`（Seite 2）` → `(Seite 2)` 半角括号化（W43 DE×IT 家族先例）、`……` 换行碎片；
  (d) P8 全角括号碎片（家族半角化，见门 2）。**无德语正文行被改动**。

### 2. P8 — 通过
- `tools/p8.py compare`（显式核心/分版 P8 路径）：**CLEAN 150=150，missing=[]，extra_count=0，uncertain=[]，
  keydiff=[137, 138, 139, 150]**。
- keydiff 逐项从 P8 SVG 行组核实（非工具输出照抄）：
  - 137：核心中文键 → 分版 `Lo sconto sul carburante dura fino a dicembre. (laufen = durare)`，DE→IT 翻译题合法重定向；
  - 138：`Guardo il calcio di martedì. (schauen = guardare)`，合法重定向；
  - 139：`La scuola è ricominciata. (wieder begonnen = ricominciato)`，合法重定向；
  - 150：写作题，`Domanda aperta — segui i punti del riquadro di scrittura; il testo modello è nel riquadro di questa pagina (Si valuta secondo i punti indicati)`，提示语言变更，非德语键；
  - 140（反向题，不在 keydiff）：键保持德语原文 `Am Sonntag schlafe ich eine Stunde länger.`（跨两行完整），
    仅提示改为意大利语 `Domenica dormo un'ora in più.` + `Traduci in tedesco`。
- 括号/破折号伪影检查：分版全 8 页全角括号 `（）` 出现 0 次；P8 键区双括号仅为合法嵌套
  （如 `(kochen (prima persona plurale))`，核心中文版亦有对应嵌套）；无提取伪影。

### 3. 几何遮挡审计 — 通过
- `tools/occlusion_audit.py`：自测 6 类各恰 1 次、干净对照静默；**分版 0 旗 · 核心 0 旗 · NEW vs 核心 0**。
- 同基线墨迹碰撞扫描（按元素真实 font-family 的 PIL/FreeType 墨迹盒，4× 超采样，README §10 补位）：
  **分版 8 页 0 墨迹重叠 · 核心 8 页 0 墨迹重叠**。
- P6 图表（README §12 盲区，逐项实测；标签绘于条形之前，但墨迹无交叠）：
  `in famiglia` 墨迹右缘 520.8，距条形左缘 535.0，净空 14.2px；
  `servizio` 496.0，净空 39.0px；`in istituto` 512.8，净空 22.2px。**0 覆盖**。
  （构建员所报 522.3/496.8/513.7 为 advance 值，与本测 advance 522.2/496.8/513.7 一致；墨迹净空更大。）
- ÜBUNGSDATEN 行实测 advance 宽 1759.2px（槽位 1820px），未超宽。

### 4. Gloss — 通过
- 按渲染后 `f.gloss()` 调用字符串本身以 `·` 拆分（AST 静态解析，未执行任何 build 模块；裸 `gloss` 名匹配不到，
  实际为方法调用 `f.gloss`，已修正）：
  核心 5 调用 × 每页 5 项 = **25**；分版 5 调用 × 每页 5 项 = **25**，逐项 1:1
  （P2/P3/P4/P5/P6 各 5 项；德语词头逐项相同，仅 gloss 译为意大利语）。
- 另：P1 bridge 行 4 项（Englische Woche / Spieltag / empfangen / Bundesliga），`Nota — … = …` 形式，卡面完整。

### 5. P7 金句 — 通过
- 8 句德语全句（标点齐全）在整期归一化文本中**各恰 2×**（出处文章页 + P7），核心与分版一致。
- 页码标签（按 P7 四列逐列核对，非行合并猜测）与核心一致，行序为 Seite 4/2/2/5/3/4/6/6：
  Vier Nächte→Seite 4·B1（出自 p4）· Energiesteuer→Seite 2·A2（p2）· Wer 50 Liter→Seite 2·A2（p2）·
  Die Schule→Seite 5·B1（p5）· Die Tage sind kurz→Seite 3·A2（p3）· Zwei schwere→Seite 4·B1（p4）·
  deutsche Wirtschaft→Seite 6·B2（p6）· Es geht langsam→Seite 6·B2（p6）。
  每句标签页 = 该句实际出现的文章页，逐句核实无误。P7 短语均逐字取自本期文章。

### 6. 读者园地 — 通过（独立判定：征集句构成显性邀请）
- 页上实测（P7 LESERBRIEFE 框内，卡面亦目视确认框内完整）：
  - 标签：`Un esempio della redazione!`（编辑示例，非真实来信）；
  - 冻结德语延期行：`Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`；
  - 示例信本身为德语旧信、署名 `die Redaktion`，无编造人名；
  - 意大利语注文：`Nessuna lettera vera, nessun miglior testo di pagina 8; tutto rinviato a VOL.3.`——
    三事实齐全：无真实来信、无最佳 P8 作文、示例+VOL.3 承诺；
  - 意大利语征集句：`Scriveteci! Mandateci lettere vere e testi di pagina 8: i migliori in VOL.3.`。
- 判定：该句以第二人称复数祈使 `Scriveteci! Mandateci…` 公开向全体读者征集真实来信与 P8 文本并承诺刊登，
  构成显性邀请。内容预告行（`IN DER NÄCHSTEN AUSGABE` 德语预告）与练习提示均未计入，判定不依赖它们。
- 全版无任何编造的读者来信、姓名或引言。

### 7. 家具三方对照 — 通过（W43 实测胜过 README 泛写）
- 徽章：分版 P1 元素与 W43 已发 `files/weekly-report-de-it/svg/p1-front.svg` **逐属性一致**：
  `x=975 y=372 font-size=20 font-weight=700 fill=#a4553a text-anchor=middle`，
  字符串 `TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO — L'EDIZIONE PER I LETTORI ITALIANI`。
  槽位为 DE 家族 y=372 原生副标题槽（README §20 的 EN/DE/ES 情形），W43/W45 两版一致。
- 页脚 8/8：`Die Lucerna · SETTIMANALE TEDESCO VOL.2 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO`；
  页码行 8/8 `Pagina N di 8`；masthead 8 页均为 `Die Lucerna`（P1 黑体字 168pt，y=262，与核心同位）。
- 差异说明（非问题）：W43 页脚为 VOL.1，分版 VOL.2 跟随 W45 核心，正确；W43 P1 多一行 W43 核心自有元素，
  W45 核心无此行，故分版无此行，不构成缺失。

### 8. 继承项复核 — 通过（附构建员数字订正，见下）
- P1 目录行 `Ferienwechsel & Herbst`（x=1523，Serif 20pt）vs `A2→B1`（x=1863 end，Sans Bold 18pt），y=1436：
  分版、核心、DE×EN 三版**几何字节一致**；以各自真实字体重测：标题 advance 右缘 1755.1、墨迹右缘 1755.0，
  等级标签 advance 左缘 1800.0、墨迹左缘 1799.7——**advance 净空 44.9px，墨迹净空 44.7px**。
- P1 全页同基线扫描（正确字体）：**0 advance 重叠**；卡面目视该行间距宽阔。
- 结论：该行是核心继承几何，且墨迹确分离。**但构建员 KIT §5 所称“4.6px advance-width 重叠”未能复现**
  （Sans 错测亦为 58.3px 净空；正确字体为 44.9px 净空；三版皆然）。此为构建员报告的测量数字错误，
  不对应已发 SVG 中的任何缺陷，故列为**非阻塞订正**，不计入问题清单；协调员可据此修正 KIT措辞，
  无需返工本版。

### 9. PDF/卡片/题量/ABSTRACT — 通过
- 印刷 PDF `Die-Lucerna-VOL2-IT.pdf`：**8 页，4,137,863 B，1462.5×2025 pt**，
  sha256 `42d18ca43f7994db4245c702fc89cc319eef30d7f30b064d57f9bb087acff56a`，与 KIT 一致。
- 网页 PDF `Die-Lucerna-VOL2-IT-web.pdf`：**8 页，4,147,320 B，1400×1938 pt**，
  sha256 `09d9b4ae05e03fe9baf386bc70a2bb60d805cbb46bfa472a78abf5441d9b402b`，与 KIT 一致（<10 MB）。
- SVG 哈希 8/8 与 KIT §9 全符一致；校对前后分版哈希未动。
- 8 张卡面全部目视：无重叠、无截断、无溢出；页脚与页码行每页齐全；P6 图表标签与条形分离；
  P7 读者框完整在框内、金句标签未触 Fehlerklinik 规则线；P8 答案区 `— PAGINA N —` 分隔齐全。
- 题量（静态解析注册表：`ex`/`match_set` 调用 + content8 的 `cloze_defs` 8 + `ddefs` 5 + `scrittura` 1，
  核心与分版两版结果相同）：**分页 10/18/18/18/18/18/12/38 = 150 题**；
  **等级 A2 66 / B1 70 / B2 14**，与核心一致。
- ABSTRACT.txt：意大利语单行（1 行，419 B），ASCII 双引号 0 个；含真实主题关键词
  （calcio/Champions League/Europa League/Bundesliga、sconto sul carburante fino al 31 dicembre、
  assistenza a casa、ritorno a scuola）与学习者搜索短语
  （`imparare il tedesco con le notizie`、`esercizi di tedesco A2 B1 B2`），并含 masthead、VOL.2、150 题、A2–B2。

## 问题清单

无。9 道必查门全部通过；唯一记录事项为门 8 的构建员数字订正（非阻塞，见上），不构成返工理由。

## 校对方法备注（供协调员复核）

- 未执行任何 build 内容模块；gloss/注册表均用 AST 静态解析；字体测量用 `tools/tables.json` 所载
  Noto CJK Regular/Bold TTC（SC face index 2），按元素真实 family/weight/size/anchor 计算墨迹盒。
- 冻结 diff、P8、遮挡审计均用 `tools/` 现成工具重跑，非手写等价物；自测先行且通过。
- 本报告与 scratch（`hidden_files/w45/de-it-proof/scratch/`：baseline、freeze-diff.json、occlusion.json、analyze.py）
  仅为校对工作文件，未写入分版或核心目录。**未宣称上架；上架由协调员串行执行。**
