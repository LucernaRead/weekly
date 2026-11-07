# 独立校对报告 — W45 RU × ES（俄语正文 + 西班牙语讲解版）

**结论先行：ZERO PROBLEMS，可定稿。** 纸面（8 页 SVG + 8 张卡 + 两 PDF）与 WEEKLY-KIT 逐项核对一致，无编号问题。
唯一单列项是徽章槽位（见 §6 待裁定项）：字符串、颜色、字号、可读性、碰撞均实测通过，槽位本身按任务书不单独判不通过，交协调员据三方实测裁定。
另有一处冻结核心几何（P7 披露语第 2 行与盒底的关系，见 §7）：与核心逐值相同且可读，按协调员在 ru-en 先例中的裁定不重报，不计为问题。

**查重：** 开工时 files/weekly-report-w45-ru-es/ 与 hidden_files/weekly-report-w45-ru-es-build/ 无进行中渲染进程；最新写盘 2026-10-27 18:52（UTC），75 秒复查零新写盘后开工。校对全程只读已发文件；核心与分版在校对前后重哈希均无变化（见 §10）。
**未做事项（按任务书）：** 未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未写入 W43 已发版与核心目录。

## 1. 基线（freeze.py baseline，独立重跑）

`tools/freeze.py baseline --build hidden_files/weekly-report-w45-ru-build --core-svg files/weekly-report-w45-ru-core/svg --out hidden_files/w45/ru-es-proof/baseline`：
**8/8 逐字节相同**（p1 8bfcb7e2…、p2 5b35f1d7…、p3 8be9ba7f…、p4 9d699050…、p5 f49d0ed8…、p6 8559d61d…、p7 961119d6…、p8 2738ae04…，与任务书基线前缀全符）。事后核心重哈希无变化。

## 2. freeze diff（分版 vs 核心）

- 各页 added CJK = 0；分版 8 页 CJK 字符总数 = 0（核心原有中文讲解层已全部替换，新增 CJK 为零）。
- 西里尔词元多重集（正则 `[А-Яа-яЁё]+`，逐页独立重算）：P1 400=400、P2 443=443、P3 338=338、P4 306=306、P5 316=316、P6 354=354、P7 397=397、P8 641=641，**8 页全部 exactly equal，core-only 与 ed-only 均为空集**。P1 零差异的解释成立：徽章为纯拉丁文，目录 «все» 标签按 W43 已发版保留未译，无任何俄语词元丢失。

## 3. P8 答案（p8.py compare + 独立 dash-parse）

- `tools/p8.py compare`：**CLEAN，150 noted = 150 noted，missing=[]，extra=0，keydiff=[83,137,138,148]**，与 KIT 一致。
- 独立 dash-parse（自写脚本：按 fs 13.0 答案行拼接折行续行，再按首个 ` — ` 切键）：150=150，无 missing/extra，**keydiff = [137,138] 仅此两项**。
- 83：印出键两版均为 `B`；148：印出键两版均为 `A`。p8.py 的 83/148 差异确为 README #13 所述括号提取 artifact（西语半角括号 vs 核心全角括号），非真改动。
- 137/138：合法翻译重瞄准（W43 同配对先例类）。俄语题干保留，指令 `Traducir al español`；键为西语：137 `El miércoles 4 de noviembre es festivo.`、138 `Un código promocional es un código de descuento.`。
- 139/140：反向键（`Traducir al ruso`），俄语键与核心**逐字节相同**（139 `В субботу «Краснодар» играет с ЦСКА.`、140 `Поздравляю с Днём народного единства!`）。
- 150：西语 apparatus（`(Pregunta abierta — texto modelo a continuación)` / `El texto modelo está en la sección H de esta página (84 palabras)`）；范文体俄语原文不变，实测 **84 词**（核心与分版范文体逐行 10 行、词数同为 84）。
- P8 括号形式：西语注全程半角括号，与 W43 RU×ES 家族已发分版一致（README #14）。
- KIT §6 “P8 keys flow ends at y=2419” 的实测含义：分版重渲染日志原文 `flow[P8-keys] ended col 3/3 y=2419 (bottom 2540)`，即 P8-keys flow 在末列的光标位，非全部答案的最大基线。全部答案最大基线实测 2534.97（在前列内，flow bottom 2540 内），距页脚规则线 2580 仍有 clearance；遮挡审计 FOOTER 0 flags。数字与 KIT 一致，无 KIT 不一致。

## 4. 几何审计（occlusion_audit.py，先 --selftest）

- `--selftest`：OK（6 类 planted 全触发，clean 对照静默）。
- 本版：**0 flags**；核心对照：0 flags；**NEW vs core = 0**。
- 同基线墨迹扫描（自写，复用 occlusion_audit 的 PIL/FreeType 真墨迹盒，按精确基线分组）：核心 0 flags，分版 0 flags。
- P6 图表逐元素检查（XML 解析 + 目视）：4 条 bar 矩形与核心逐值相同（x=685，y=1612/1658/1704/1750，宽 600/494/388/282，高 30，fill #3e4c2a）；4 组标签与数值全部可见且位置与核心相同（`Дома с семьёй 34%`、`Короткая поездка 28%`、`Ярмарка или концерт 22%`、`Просто выспятся 16%`；34+28+22+16=100）；无后绘 rect 遮挡（遮挡审计 COVER 0；RU 的 P6 图表无 ES 核心那样的冻结压字，0 重叠是正常结果）。练习数据标注完整（`УЧЕБНЫЕ ДАННЫЕ · Datos de práctica` + 西语“非真实统计”句，全句已核对非截断）。

## 5. 总量与 gloss、图片、金句

- 分版重渲染复现（构建树拷贝至校对目录并重定向输出，不碰已发文件）：**8/8 SVG 与已发分版逐字节相同**；日志 **零 FLOW OVERFLOW、零 HEAD TOO WIDE**；registry：TOTAL 150，A2 51 / B1 75 / B2 24，分页 10/18/18/18/18/18/12/38，类型 Completar 54 / Opción múltiple 42 / Emparejamiento 20 / Frases 12 / Transformación 4 / Cloze 13 / Traducción 4 / Redacción 1——与 KIT §1 全符。
- gloss 按 `·` 本身拆分：9 次调用共 **26 项**，逐 call 与核心相等（content12: 3/3/3；content34: 3/3/3；content56: 3/2/3），核心与分版逐文件相同。
- 图片载荷与核心逐字节相同：P1/P4/P5 各 1 张，其余页 0 张；P1/P4/P5 credit 与核心一致（Toxer427 CC0；1912 佚名公有领域；Preston Keres USDA 公有领域）。
- P7 金句：P7 所列 8 句俄语原文（去引号内文）在全刊各恰 **2 次**（文章页 + P7），分布 P1×2、P2×1、P3×1、P4×1、P5×1、P6×2，与核心 KIT 一致；P7 引文字符串与核心逐字相同。
- P7 读者园地：编辑示例俄语原文（`— М. (пример от редакции)`）与俄语披露 5 行逐行相同，只译讲解层（西语披露 2 行），无编造读者/来信/引言。

## 6. 家具三方比对 — 徽章槽位

| 项目 | 本版 W45 RU×ES | W43 RU×ES 已发版 | W45 RU 核心 |
|---|---|---|---|
| 徽章字符串 | `TEXTOS EN RUSO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES` | **逐字相同（代码判等 True）** | 无此徽章 |
| 槽位/字号/颜色 | (975, 574)，22pt，#a4553a (BRICK)，700，居中 | (975, 372)，20pt，#a4553a，700，居中 | y=372 为冻结俄语 strapline（见下） |
| 墨迹跨度（真墨迹盒） | 402.46–1547.46（宽 1145.00；KIT 记 402.5–1547.5，舍入一致） | 454.50–1495.50（宽 1041.00） | — |
| 上下空隙（本版） | 深色带底 542 → 徽章墨迹顶 551.75 = **9.75**；徽章墨迹底 574.25 → 标题墨迹顶 588.00 = **13.75**；右侧栏顶 580 → 徽章墨迹底 = **5.75** 纵向净空（x 向 1451–1547.5 有重叠但纵向无交） | — | — |
| y=372 行内容 | 冻结俄语 strapline 保留：`ЕЖЕНЕДЕЛЬНАЯ ГАЗЕТА ДЛЯ ИЗУЧАЮЩИХ РУССКИЙ ЯЗЫК — НАСТОЯЩАЯ РОССИЯ, ПО-РУССКИ`（19pt #57523f，与核心逐值相同） | 该槽即徽章本身，无 strapline（W43 核心 y=372 为空闲槽） | 同左 strapline |

- 机制已证实：W43 的 y=372 槽在 W45 核心已被冻结目标语文本占据，沿用该槽即删除目标语文本；本版沿用 W45 RU 家族先例 INSERT 于 (975, 574) 22pt BRICK。
- 同核心先例对照：ru-de 徽章亦在 (975, 574) 22pt #a4553a；ru-en 与 ru-fr/ru-it/ru-pt 徽章在 (975, 372) 20pt（ru-en 颜色 #3e4c2a，其余 #a4553a）。即 574 插入与 372 替换均为 RU 目标已通过的先例。
- P1 卡面目视：徽章砖红清晰可读，位于深色带与 `ГЛАВНАЯ ТЕМА · El tema principal` 标题之间，无碰撞、无压字。
- 其余家具与 W43 逐字/逐项一致：顶条 `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · CADA SEMANA · EL RUSO QUE LEE RUSIA`（判等 True）；8 页页脚左 `Lucerna · SEMANARIO RUSO VOL.2 · TEXTO EN RUSO · EXPLICACIONES EN ESPAÑOL`、右 `Página N de 8`；gloss 前缀 `Nota — `；P8 分隔符 `— СТРАНИЦА N —`（8/8，与 W43 相同）；目录 `все` 标签保留；双语栏目标题形式与 KIT §3 一致。

## 7. P7 读者园地几何（实测）

- 信盒矩形与核心逐值相同：x=1451, y=1254.58, w=434, h=473，**盒底 1727.58**；短语规则线 y=1756 两版相同；**规则线空隙 1756 − 1727.58 = 28.42**（KIT 记 28.4，舍入一致）。
- 披露语第 2 行基线：核心（中文行）与分版（西语行 `redacción. La promesa pasa a VOL.3.`）均为 **1738.28**，逐值相同。
- 盒底接触：披露语第 2 行基线低于盒底（1738.28 > 1727.58），盒底边线穿过该行字形上部——**核心原样即是如此**（中文披露语同值同现象，见 p7-disclosure-crop 对照图），且文字在卡面放大后仍可读。按任务书：此为协调员在 ru-en 先例中裁定过的非阻塞冻结核心几何，几何一致 + 可读，**不重报、不计问题**。

## 8. ABSTRACT 与 PDF

- ABSTRACT.txt：西班牙语单行（317 字符，1 行正文 + 结尾换行），**无 ASCII 双引号**；含真实主题关键词（11 月 2–8 日周、周三 4 日节日、周二 3 日短日、11.11 优惠、俄超第 14 轮）+ 学习者搜索短语（`aprender ruso con noticias en ruso`）+ `150 ejercicios de niveles A2 a B2`。
- 两 PDF 均为 **8 页**：print `Lucerna-VOL2-ES.pdf` 13,554,108 字节，sha256 `5bead5b33bd234535468971d7007e67396548731e7ced27a9bad9f2e733438f1`；web `Lucerna-VOL2-ES-web.pdf` 3,212,084 字节（<10 MB），sha256 `daaab9ea4e31947639650c9f4e59acdef916703bc800d6d05f037067bd6375aa`——尺寸与 SHA 与 KIT §13 全符。
- 8 张卡均为 1950×2700 PNG。

## 9. 目视（8 张卡全部逐张目视，含 builder 未目视的 P2–P5）

- P1：徽章、目录（含 `все`）、数字盒、公园照片 + credit、闪电测验 7–10、页脚均正常，无溢出/遮挡/页脚碰撞。
- P2：gloss 盒 3 个、天气词条、练习 11–28、页脚正常。
- P3：gloss 盒、练习 29–46、页脚正常（中部留白为核心冻结版式，非缺陷）。
- P4：1912 照片 + credit、赛程表、练习 47–64、页脚正常。
- P5：市场照片 + credit、gloss 盒、练习 65–82、页脚正常。
- P6：日条、图表 4 条 bar + 标签 + 数值全部可见、练习 83–100、页脚正常。
- P7：三栏语言版块、错误诊所（西语单行讲解）、词盒单行 gloss、读者园地（示例 + 俄语披露 + 西语披露）、金句 8 句 + 西语译文、VOL.3 预告、页脚正常；盒底接触见 §7（冻结几何）。
- P8：测试 113–150、H 区范文体（84 词标注）、全部 150 条答案分栏清晰、页脚正常；答案 83 折行 `(miércoles, sábado y domingo)` 完整无截断。

## 10. 审计输出路径与关键证据

校对目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-es-proof/`

- `PROOF-REPORT.md`（本报告）
- `freeze-baseline.log`（8/8 逐字节）、`baseline/`（基线重跑输出）
- `freeze-diff.log`、`freeze-diff.json`（added CJK 0）
- `p8-compare.log`、`p8-compare.json`（CLEAN 150=150，keydiff [83,137,138,148]）
- `occlusion-selftest.log`、`occlusion.log`、`occlusion.json`（0 flags，NEW 0）、`occlusion-core.log`、`occlusion-core.json`（核心对照 0）
- `audit.py`、`audit.log`（西里尔多重集、CJK、dash-parse、gloss、图片、金句）
- `badge.py`、`badge.log`（徽章真墨迹、P7 几何、P6 图表、同基线扫描）
- `rerun.log`、`rerun-svg/`（分版重渲染 8/8 逐字节相同，零 FLOW OVERFLOW / HEAD TOO WIDE，含 `flow[P8-keys] ended col 3/3 y=2419`）
- `p7-disclosure-crop-ed.png`、`p7-disclosure-crop-core.png`（P7 披露语盒底接触放大对照）
- `core-svg-sha256-BEFORE.txt` / `core-svg-sha256-AFTER-baseline.txt` / `core-svg-sha256-FINAL.txt`（三份全同）、`edition-sha256-BEFORE.txt` / `edition-sha256-FINAL.txt`（两份全同）

**最终结论：ZERO PROBLEMS，可定稿；徽章槽位一项待协调员据 §6 三方实测裁定（不因此单独判不通过）。**
