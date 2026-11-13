# GATE-LOG — 2026-W47 ru-fr · proof2（re-fanout 重建版独立复校）

**版本：** `production/2026-w47/2026-w47-ru-fr/` · **日期：** 2026-11-11
**Scratch：** `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-fr2/`
**工具：** `~/workspace/weekly-git/tools/venv/bin/python`；canonical creambox
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
**环境：** 每条命令均设 `TMPDIR` = scratch `tmp/`（系统 /tmp 512 MB 且常满）。
未修改任何生产文件，未 commit/push。先探针（`git hash-object -w` 于 weekly-git 内通过、
scratch 真实写通过、`/dev/null` 正常）再开工。

## §0 身份（磁盘 = 任务，开工前与收尾后两次实测）

| 文件 | SHA-256 | 字节数 |
|---|---|---|
| `Lucerna-VOL4-ru-fr.pdf` | `8f09a2703081f12b76ace75331a79b5c4507282894b119298e68b7ce77c83562` | 21,291,969 |
| `Lucerna-VOL4-ru-fr-web.pdf` | `45f6401dc1e20dfc12d596d4d31e49e4803f6a41c442d9e757940ef15d823929` | 3,385,758 |
| `2026-w47-ru-fr.text.md` | `7a402199542afaf125a8648fe7fd4bcc67766718e0e70b2351e35418b18522ec` | 63,543 |

Core（比对用）：print `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` /
31,429,147 B；web `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` /
4,025,834 B；text `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` /
60,953 B（fix1 `f11854bf`）。Edition 目录 untracked（`?? production/2026-w47/2026-w47-ru-fr/`）；
收尾时 `git status` 显示的 `issues/2026-w43/*` 修改属他人并行工作，与本轮无关，
本轮未改动任何已追踪文件。

## §1 check_core.py — rc=0

`logs/check_core.log`：`golden BAD: 0`，`gloss fails: 0`，`P8 svg text chars: 10994`；
orphan line-starts 1（`('p7-yazyk.svg', 553, '”».')`，已知良性——#1 同项）；
same-baseline collisions 1（`('p1-pervaya.svg', 1712, 'чёрная', ' ')`，与 core 相同）。
与重建记录一致。

## §2 p8 extract + compare — CLEAN，keydiff [137, 138, 139, 140]

`logs/p8-core.log/json`、`logs/p8-edition.log/json`、`logs/p8-compare.log/json`：
core 150/150，edition 150/150；
`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]`。
直接比对 core `ru-p8.json` 的 150 个 key（自写比对）：差异恰为
`['137', '138', '139', '140']`，与 compare 一致。
4 项均为 E 节翻译 key，正确重指法语（137 `Mardi 17 novembre, Journée des étudiants.` ·
138 `Un colis doit être suivi, retiré et vérifié.` ·
139 `Mardi, la Russie joue contre le Venezuela.` ·
140 `Bonne Journée des étudiants à toutes et à tous !`），core 为中文原式，属设计如此。
Q137 提取值为完整句，未见 em-dash 截断（见 PROOF-NOTE §必查项 6）。

## §3 Keycheck — 150/150 手核 PASS（`keycheck-150.json`，自建）

自写 `build_keycheck2.py`（机械比对表；未复用 #1 的 verdict/notes）：
题干解析 150/150，答案行解析 150/150；
印刷 key vs text.md key：**149/150，仅 Q150 除外**
（印刷 `✓` vs text.md `(Question ouverte, texte modèle ci-dessous)`，同义表示差异）；
vs core keydiff `[137, 138, 139, 140]`。
级别 A2 50 / B1 76 / B2 24；题型 Compléter 54 / Choix 55 / Appariement 20 /
Phrases 12 / Transformer 4 / Traduction 4 / Rédaction 1；
按页 10/18/18/18/18/18/12/38。
手核方法：text.md 838 行全文通读，逐键核对题干；
Choix 对文章/比分表/图表；Compléter 核格/数/时态与事实；
20 道 Appariement 的选项单逐一从练习 SVG 提取核对——
P2 D：a. День психолога / b. День студента / c. Всемирный день ребёнка /
d. день рождения Деда Мороза；
P3 C：a. человек, который смотрит фильм / b. фильм о жизни реального человека /
c. показ фильма в кинотеатре / d. фильм о реальных событиях；
P4 C：a. победил ЦСКА 4:2 / b. проиграл «Рубину» 0:1 / c. победил «Акрон» 2:1 /
d. сыграл с «Ростовом» 2:2；
P5 C：a. код со скидкой / b. товар возвращают в магазин / c. цена ниже обычной /
d. большая продажа со скидками；
P8 F：a. результат матча, например 2:2 / b. лёд на дороге /
c. тепло зимой: снег тает / d. большая продажа со скидками。
G 对话按 P8 SVG 顺序通读（145 A · 146 B · 147 B · 148 A · 149 B）。
H 范文 97 词（80–100 ✓）。

## §4 Occlusion audit — 42 flags，全 TEXTX，42/42 CLEAR

真实命令，未加 `--selftest`（按任务要求）：
`tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --json logs/occlusion.json`
（`logs/occlusion.log`，rc=1 表有 flags，非失败）：
`42 flags {'TEXTX': 42}`，0 COVER / LINEX / FOOTER / EDGE / BOXTITLE。
裁决：复用 #1 的 numpy 极性无关栅格法（`adjudicate4.py`，
路径改为本 scratch，于本轮新渲染 `render/p-*.png` 上跑，
`logs/adjudicate4.log`）：**38/42 raster CLEAR**
（接缝最宽空白列 0.48–10.56 SVG px；0.48 px 为 P1/P4 `ЦСКА` 与 P1 `пятница` 接缝，
字形仍分离）。
余 4（全为 `Краснодар»`，P1 ×1 `[101.2, 1200.5, 233.7, 1224.8]`、
P4 ×3 `[101.2, 578.7, 233.7, 602.9]`、`[101.2, 685.6, 233.7, 709.9]`、
`[1042.2, 2215.4, 1174.7, 2239.6]`）：列测试在每列都见墨，
因 `р` 字碗与 `»` 尖角在不同高度占同一列。
`crops/crop-krasnodar-{0,2,3,4}.png`（4× 放大）显示 `р` 字碗与首个 `»` 尖角之间
有清晰亮隙——字形不接触，系工具墨框（侧边距）假象。
**最终：42/42 CLEAR。**

## §5 Creambox（canonical，全 8 页）— `logs/creambox.log`

`tools/creambox.py <edition>/svg/*.svg`（rc=0）：
BELOW-WINDOW 95 行（+28.0 ×25、+32.0 ×41、+34.0 ×4、+37.0 ×25），
全为既定分类的下一区块首行；
inside-only 负值仅 1 处：P2 “А ВЫ?” 框 desc-clear −1.0（见 §6 OBS-1）；
P7-TOOLBOX：3 框，min inside clearance +11.9，min desc-clear +5.9（PASS）；
P8 无奶油框。
**本轮扫描与重建记录 `records/fr/creambox.log`、与 #1 `logs/creambox.log`
均逐字节相同**（路径归一化后 diff 为空）。

## §6 Spill sweep（自写 PIL 真墨扫，`spill_sweep.py` + `spill_sweep2.py`）

对象：32 个无描边奶油框（fill `#f0eee5`，stroke 无），于 200 dpi 渲染上量真墨
（墨 = min 通道 < 150；SVG→PNG 缩放 K=4062.5/1950）：
- **A. 四边穿越：** 仅 1 处标记——P1 box1（1439.5, 588.0）EDGE-top 墨 881 px。
  甄别：墨在 SVG y 584.2–587.5（框顶 588.0 之上），框顶线 y=588.0 及以下墨为 0；
  `crops/crop-p1-boxtop.png` 显示框顶上方深绿横条与框顶贴合收边，未穿越。
  系 ±1 px 窗口假阳性，**非溢出**。
- **B. 盒标题（严格框内矩形过滤，v2）：** 32/32 标题墨框水平在框内，
  最紧为 P6 box2（墨右缘 1855.2 vs 框右 1862.0，余 6.8 px），余者余量 11.6 px 以上；
  标题墨底均远在框底之上。P1 head `ТУР В ЦИФРАХ　EN CHIFFRES` 墨 max-x 895.7
  vs 框右 961（与 #1 的 895.7 一致）。
- **C. 末行墨底：** 32/32 在框内；最紧为 P2 box3（OBS-1）**+1.24 px**，
  次紧 P7 box1 +7.98 px，余者 +11.68 px 以上。
- **D. BELOW-WINDOW 行：** 95 行墨顶均在对应框底之下，无重叠。
**结论：0 实违规。**
（注：v1 用 y-only 过滤曾漏 P2 box0 等 6 框的标题/末行归属，v2 改严格 x+y 框内过滤后
32 框全量复核；v1 的唯一标记即上述 EDGE-top 假阳性。）

## §7 Freeze — 标准口径 8/8

首次按任务旧口径（`baseline --build <edition>`，无 `--core-svg`）调用失败
（rc=2，工具要求 `--core-svg`；见 `logs/freeze-baseline.log`——旧版 freeze.py 已改口）；
按现行工具口径重跑：
- **标准：** `freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg --out freeze-core`
  （`logs/freeze-baseline-core.log`）：`baseline: 8/8 SVGs byte-identical (repointed files: none)`，
  8 个 OK 行（p1 `409d5c2d…` … p8 `6ad2c7f1b…`），
  `core integrity: shipped core SVGs unchanged by the run`。
- **补充（edition-internal 自洽基线，非标准口径）：**
  `freeze.py baseline --build <edition> --core-svg <edition>/svg --out freeze-ed`
  （`logs/freeze-baseline-ed.log`）：亦 8/8。
- **Diff：** `freeze.py diff --core-svg <core-ru>/svg --edition-svg <edition>/svg --json logs/freeze-diff.json`
  （`logs/freeze-diff.log`）：P1 +19/−22、P2 +38/−36、P3 +27/−28、P4 +28/−28、
  P5 +27/−27、P6 +34/−32、P7 +51/−48、P8 +173/−629；
  removed count-sum **850**、per-page distinct 合计 **484**；
  西里尔删除恰为 15 项（全在 P8）：
  Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、
  иллюстрация、к、можно、ноябрю、общественное、сказка（各 ×1）；
  其中 14 项（除 `можно`）均在 core P8 y≥2450 图注区 runs 内（自核），
  `можно` 为 Q46 已知合法项（P8 答案注），**unexplained 0**；
  Morozko 图在 edition P8 中不存在（image skipped by design，与首版同）；
  新增 CJK 仅 U+3000 ×8（每页 1）。
  `logs/freeze-diff.json` 与重建记录 `records/fr/freeze-diff.json` 内容完全一致
  （Python `==` 比较 True）。
  （注：#1 的 P6 −54 / P7 −55 / P8 −639 与本轮 −32/−48/−629 的差异，
  系 #1 对旧版 edition 跑的旧 diff；本轮 diff 与重建记录的 diff 一致，
  且西里尔清单逐项核对无误。）

## §8 print/web 文本层 + #1 D1 斜体回归 — `checks2.py`（`logs/checks2.log`）

- 页数 print=web=8；非空字符 multiset 总体与逐页均全等，30,771 字符；
  空格 print=web=4,880（差 0），换行 print=web=1,599（差 0）；
  pdftotext 字节数 print=web=57,973 B（`logs/print.txt`、`logs/web.txt`）。
- **斜体回归（span 级，PyMuPDF）：**
  print 斜体面 `NotoSerif-MediumItalic`、`Newsreader16pt-Italic`；
  web 斜体面 `LucernaNotoSerif-Italic`、`LucernaNewsreader-Italic`（已嵌回）；
  P1 词条 span：print `NotoSerif-MediumItalic` 16.12 `чёрная пятница`，
  web `LucernaNotoSerif-Italic` 16.12 `чёрная пятница`（带空格）；
  `чёрнаяпятница`（无空格）span：print 0、web 0；
  ` »` 计数 print=web=1。#1 三症状全部归零。
- **视觉回归：** `crops/crop-wordweek2-web.png` vs `crop-wordweek2-print.png`
  （P1 СЛОВО НЕДЕЛИ 框 2× 放大）：web 版词条为真斜体、词间空格清晰、闭引号贴合，
  与 print 版一致。
- P8 最小字号 print=web=9.75 pt（全页最小亦 9.75 pt）；页面尺寸 1462.5×2025 pt，双 PDF 同。

## §9 s11_check.py — rc=0，FAILURES: none

`logs/s11.log`：badge B2 `#37402f`、foot 含 VOL.4 + 全角空格、VOL.3 仅 P4 更正、
P1/P8 band 无 VOL.5、masthead 196 px、band title 46 px、left margin ≥ 87（实测 88.0）、
no CJK in visible svg、双 PDF 各 8 页、web < 7 MB（3,385,758）、
**P8 min font >= 9.75pt 9.75**、`FAILURES: none`。

## §10 D1 / D2 / D6 / kicker / CJK / `___` — `checks2.py`

- D1：KEEP_AS_IS 的 4 条 fr 值逐字核对——s1 在 P6 SVG ✓、s2 在 P6 SVG ✓、
  s3 在 P7 SVG ✓、s4 在 P8 SVG ✓；s2 不在 text.md ✓；
  text.md 段落行：`УЧЕБНЫЕ ДАННЫЕ` [459]、`Три уровня, три темы` [504]、
  `Большой тест недели + все ответы` [596]。
- D2：`Международный день студента` text.md ×2 = core ×2；Q25 短式见 L187。
- D6：`желании` text.md ×2（L173 + L694）；P2 SVG ×0（key 只在 P8，不在 P2——符合预期）；
  P8 提取 key 20 = `желании`。
- Kicker：tokens 11 个（末尾逗号拆分后）、gaps 9 个
  `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`、min 5.9；
  全串 `ЕЖЕНЕДЕЛЬНАЯ  ГАЗЕТА  ДЛЯ  ИЗУЧАЮЩИХ  РУССКИЙ  ЯЗЫК  —  НАСТОЯЩАЯ  РОССИЯ,  ПО-РУССКИ`，
  与 core P1 行逐字相同。
- SVG 真实 CJK：0（U+3000 共 123 处，分隔符）；text.md / ABSTRACT.txt CJK 0、U+3000 0。
- 字面 `___`：text.md 87 处（与任务数一致，模板缺口，非缺陷）。
- H 范文：97 词。

## §11 D5 字体（只记录不判定）

8 页 SVG `<text>` 统计：Newsreader 3426（+ Bold 100）、Noto Serif 2830（+ Bold 83）、
Noto Sans CJK SC 433（+ Bold 506）、Noto Sans 219（+ Bold 198）、
Noto Serif CJK SC 32（+ Bold 4）、UnifrakturMaguntia ×1（Lucerna 刊名）；
SVG 最小字号 13.0 px，最大 196.0 px。

## §12 回归对照（与 #1 备份 `backup-old/2026-w47-ru-fr/`）

- text.md：`diff` 恰好 6 对行（L173、L187、L459、L504、L596、L694），余无他变。
- SVG 文本 run（按 (x,y) 对齐）：P3/P4/P5 零差异；71 处差异键全部归因
  D1/D2/D6/kicker（含双空格重排造成的 x 位移）。
- content\*.py：仅 content12.py（kicker + D6 + D2）、content56.py（D1 s1+s2）、
  content7.py（D1 s3）、content8.py（D1 s4）有 diff，且仅为既定改动（含修复注释）。
- Map：首版旧 map（`scratch-fanout-ru/map-fr.json`）vs 新 surgical map
  （`scratch-refanout-ru/maps/map-fr.json`）：`instr/key/meta/type` 0 改动；
  `lit` 335 条中恰好 4 条改动（4 条 D1 KEEP 值），0 丢失、0 新增——
  **49 处 fr 手工修正全部保留**。
- ABSTRACT.txt：与备份逐字节相同（435 B）。
- 其余：仅重建产物（PDF、text.md、5 页 SVG、5 张 cards、KIT）与 `__pycache__` 不同。

## §13 verify_ed.py 说明

仓库与各 ru proof scratch 中均无 ru 版专用的 `verify_ed.py`
（en 版的 `verify_ed.py` 为 en 专用，如 Q39/40/Ashes 检查，不适用 ru-fr；
#1 复校亦无此文件）。本轮以等效覆盖代替：`s11_check.py`（§9，全过）+
自建 150 键核对（§3）+ D1/D2/D6/kicker/CJK/文本层独立检查（§10、§8）+
`check_core.py`（§1）。无遗漏项。

## §14 目检与接缝量测

8 页 200 dpi 全页目检（`render/p-1.png`…`p-8.png`）：无溢出/重叠/裁切；
页脚 `Page N sur 8` 齐全；P4 八场比分、P6 图表合计 100、P7 金句 8/8 带页码均核对。
5 处低倍下看似连写的接缝以真墨/advance 复核（非缺陷）：
P1 `метеорологическая|зима` 5.55 px、P2 `поздравить|féliciter` 4.62 px、
P1 byline `От редакции|Lucerna` 3.85 px（advance 法；#1 PIL 墨列法 4.8 px，
与同行 `От|редакции` 3.83 px 同级）、P6 `d’|exercice` 墨间隙 0.25 px、
`D’|EXERCICE` 2.00 px（’ 紧排，同字号词空格参比 5.07/6.76 px）。

## §15 非缺陷裁定汇总

- (a) P1 head/chip 溢出——无（PIL 真墨：head 墨 max-x 895.7 vs 框右 961）。
- (b) P3/P5 右栏奶油框下溢——无（P3 +68.3/+68.7、P5 +63.9，spill v2 全框复核 0 违规）。
- (c) P7 toolbox——PASS（+11.9/+5.9；spill v2：P7 box1 末行 +7.98）。
- (d) §E 标签——法语 `[Traduction]` / `[Traduire en français]`，无中文残留，
  text.md/ABSTRACT.txt CJK 0。
- (e) #1 web 斜体三症状——已修复（§8）。
- OBS-1 P2 “А ВЫ?” 框：本轮真墨复测末行墨底 1157.8、框底 1159.0、余 +1.24 px，
  与 #1 完全一致，在框内，非缺陷。
- `14- й`——pdftotext 分词假象；span 文本存 `14-й тур`，非缺陷（#1 已证，本轮 multiset 差值 0 佐证）。
- P3/P5 中段空白、P7 普希金紧裁、Q147、Q62——观察项，非缺陷（见 PROOF-NOTE）。
- KIT 过期陈述 4 处——仅记录（PROOF-NOTE OBS-6），非版本缺陷。
