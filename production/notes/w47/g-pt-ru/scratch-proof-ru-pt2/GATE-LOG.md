# GATE-LOG — 2026-W47 ru → pt (proof1, re-fanout 重建版)

- 版：`2026-w47-ru-pt`（俄语目标 × 葡萄牙语读者），VOL.4
- 工作区：`~/workspace/weekly-git`，版目录 `production/2026-w47/2026-w47-ru-pt/`
- Scratch（只写这里）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-pt2/`
- 解释器：`tools/venv/bin/python`（Pillow 13.0.0）；TMPDIR = 本 scratch `tmp/`（/tmp 仅 512M）
- 核心对照：`production/2026-w47/core-ru`（fix1 `f11854bf`）
- 首轮备份对照：`scratch-refanout-ru/backup-old/2026-w47-ru-pt/`
- 探针：`cd weekly-git && echo test | git hash-object -w --stdin` → `9daeafb9…`，rc=0（/dev/null 存在）

## §0 SHA 核对（磁盘实测，逐一核对，全部一致才开工）

| 文件 | 实测字节 | 实测 SHA-256 | 预期 | 结论 |
|---|---|---|---|---|
| 印 `Lucerna-VOL4-ru-pt.pdf` | 21,205,597 | `59f01012f5c64fdddb73e1b73a50b448e21b8d2c68f59b740b4927a6f1444cdd` | 同左 | ✓ |
| 网 `Lucerna-VOL4-ru-pt-web.pdf` | 3,383,529 | `485a27b6be196e7f7d95c3b2d2e218ba3969ebe8fe084668ec20eea4f7bcff70` | 同左 | ✓ |
| 文 `2026-w47-ru-pt.text.md` | 65,155 | `54d8a766e18daf5f256e91c76765c9e71fefb48c9435e83d28e103bba603d60e` | 同左 | ✓ |
| 核心印 `core-ru/Lucerna-VOL4.pdf` | 31,429,147 | `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` | 前缀 `d60fbd6c…` | ✓ |
| 核心网 `core-ru/Lucerna-VOL4-web.pdf` | 4,025,834 | `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` | 前缀 `2f995f1d…` | ✓ |
| 核心文 `core-ru/2026-w47-ru-core.text.md` | 60,953 | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` | 前缀 `348511e0…` | ✓ |

与 `scratch-refanout-ru/FANOUT-REPORT-ru.md` §Core 表逐值一致。生产目录零写入；core-ru 只读（freeze 自检：8 个核心 SVG 跑前跑后 hash 不变）。

## §1 run.py（scratch 副本 `run-copy/`，不含 PDF）

- 命令：`tools/venv/bin/python run.py`（cwd=`run-copy/`），日志 `run1.log`
- rc=0，`TOTAL 150`（A2 50 / B1 76 / B2 24；按页 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38）
- `FLOW OVERFLOW` / `HEAD TOO WIDE`：0 行（grep 0 命中）；`ALL DONE`
- 备注：`P8 morozko SKIPPED: no room (col 3 y 2317.03)`——Morozko 图按构建条件跳过，符合设计
- 重建 SVG 与现盘比对（sha256）：p1–p8 **8/8 字节一致**

## §2 freeze（`tools/freeze.py`）

- 核心基线（正确路径：`--build production/2026-w47/core-ru --core-svg …/core-ru/svg --out scratch/freeze-core`）：rc=0，**baseline 8/8 byte-identical**，`core integrity: shipped core SVGs unchanged (8 files re-hashed)`。build-copy 内确为核心目录（任务要求的路径；版目录作 build 的证据无效，故另跑核心路径）
- 版内自比对（补充：`--build <版目录> --core-svg <版 svg>`）：rc=0，baseline **8/8**
- diff（core SVG → 版 SVG，`freeze-diff.json`）：removed distinct **484** / count-sum **848**（与重建方记录 484/848 一致）
- Cyrillic-bearing removed：恰 **15 项**（count-sum 15），全在 p8：
  `Билибин, Билибина, Зимняя, Иван, Ивана, Иллюстрация, Морозко, год, достояние, иллюстрация, к, можно, ноябрю, общественное, сказка`（各 ×1）
  - 其中 14 项 = 核心 p8 y≥2450 图注区 runs（x=1439.5，y=2486–2560，«Морозко» 图注块），版 p8 已核实无 `Морозко`（图被跳过，见 §1）；其余 1 项 = Q46 `можно`（已知合法）
  - Unexplained Cyrillic：**0**
- Added CJK：仅 U+3000 ×8（家具分隔符）；其余 0

## §3 occlusion / p8 / keycheck / check_core / s11

- occlusion 真实审计（`tools/occlusion_audit.py <版 svg> --core <核心 svg>`，不是 `--selftest`）：
  自测 6 类全触发、干净对照静默；本版 **42 flags，全 TEXTX，0 LINEX**（rc=1 仅因有 flag，与重建方一致）
  - NEW vs core：3 项，全为 U+3000 双语栏标题（p7 ` LÍNGUA/ЯЗЫК`、p8 `ОТВЕТЫ/TESTE E RESPOSTAS`、p8 说明行）
  -  adjudication（`scratch-fanout-ru/adjudicate_ru.py`，独立重跑）：**Counter({'CLEAR': 42})**，42/42 CLEAR（3 项 NEW 的 ink gap 分别为 21 / 19 / 21 px）
- p8 extract（`tools/p8.py extract --total 150`）：**150/150**（parse: lines）
- p8 compare（`--core-p8 … --edition-p8 …`，直接读 `ru-pt-p8-compare.json` 本体）：**status CLEAN**，missing=[] extra_count=0 uncertain=[]，**keydiff=[137, 138, 139, 140]**
- 直接 keydiff vs 核心 `ru-p8.json`（150 键逐键比）：恰 **[137, 138, 139, 140]**——四项均为 RU→PT 翻译题的正确葡语键（Q137 `Terça-feira, 17 de novembro, Dia do Estudante.` 等）；与核心抽取 JSON 比对结果相同
- Q20 键：`желании`（p8 抽取 + 核心 ru-p8.json:177 一致）
- check_core（版目录）：rc=0，golden BAD **0**，gloss fails **0**；orphan line-starts 1 项（P7 y553 `”».`）；same-baseline collision 1 项（P1 y1712 `чёрная`）
  - 核心对照（同工具跑 core-ru）：golden BAD 0，gloss 0，orphans 5（P7 `。`×3、`：`×1、`”».`×1——本版仅剩 `”».`，其余为中文桥接文本，随葡语化消失），collision 同为 P1 y1712 `чёрная`。两项均为继承/已知，无新增
- s11_check（`scratch-fanout-ru/s11_check.py`）：**FAILURES: none**；P8 min font **9.75 pt**；8 SVG / 8 页 ×2 PDF；web 3,383,529 B < 7 MB；web text > 0

## §4 印/网文字层 + P8 字号

- fitz 逐页非空白字符多重集比对（`textlayer.log`）：8/8 页各自相等，总体相等，**31,107 字符，token 差 0**
  - P1 3125 / P2 3400 / P3 2757 / P4 3400 / P5 2996 / P6 2934 / P7 3604 / P8 8891（印=网）
- P8 最小 PDF 字号：**9.75 pt**（s11，§1.1 下限；印/网一致）

## §5 150 题逐题手验

- 来源：text.md 150 题全解析（130 常规格式 + 20 配对项）+ p8 抽取键 + content*.py 源码 + 各页 SVG 选项原文
- text.md 键 vs p8 SVG 键：**147/150 逐字一致**；3 处表观差异为解析伪影，非真实差异：
  Q73 键 `заказов`（text.md 行内括号注释被正则误并入键）、Q83 键 `B`（同）、Q150 开放题（p8 键 `✓` vs text.md 开放题说明，与核心一致）
- 五组配对块（20 题）逐组对照 SVG 字母选项原文，全部正确：
  - Q25–28（P2）：a=День психолога，b=День студента，c=Всемирный день ребёнка，d=день рождения Деда Мороза；键 b/d/c/a ✓
  - Q39–42（P3）：a=человек…，b=фильм о жизни…，c=показ…，d=фильм о реальных событиях；键 b/d/c/a ✓
  - Q57–60（P4）：a=победил ЦСКА 4:2，b=проиграл «Рубину» 0:1，c=победил «Акрон» 2:1，d=сыграл с «Ростовом» 2:2；键 b/a/c/d ✓（赛果与 P4 正文一致：Спартак—Акрон 2:1，Зенит—Ростов 2:2）
  - Q75–78（P5）：a=код со скидкой，b=товар возвращают…，c=цена ниже обычной，d=большая продажа…；键 d/b/a/c ✓
  - Q141–144（P8）：a=результат матча…，b=лёд на дороге，c=тепло зимой…，d=большая продажа…；键 c/d/a/b ✓
- 重点抽查（正文/图表/日期核实）：
  - Q20 键 `желании`（前置格，`о своём ___`）✓；Q73 键 `заказов`（14,4 млн + 属格复数）✓
  - Q33 饥饿游戏 26 Nov（P3 正文）✓；Q56 `20:45`（P4 正文：Балтика—Динамо Мх 0:1，8 ноября 20:45）✓
  - Q65 2026-11-27 为星期五（`date -d`），Q69 2013 年（P5 正文）✓
  - Q85–87 图表：工作/学习 38（最多）/ 购物 26% / 影院图书 18%（content56.py 图表，和 100）✓
  - Q129–136 Masha 叙事（content8.py:50）：大学生、周二祝贺同学、周四看电影、周六取件点 ✓
  - Q137–140 翻译键正确；Q140 增 `a todos` 为地道问候许可，非缺陷
  - Q145–149 对话键正确（`со скидкой` 工具格等）✓；Q150 范文实数 **97 词**（80–100 要求内）✓
- 结论：150/150 题干与键逐项适配，无错键

## §6 水平盒标题真墨检查（重点）

- 方法：自写 `boxtitle2.py`，用本版自有 `svglib._pil/_runs` 字体路由（与渲染器同一批字体文件），按 run 实际字号/粗细量真墨右缘；前导空白 advance 计入（U+3000 在 23pt = 23.0px，27pt = 27.0px；未修正前曾低估 23px，已修正并复核）
- 覆盖：全部 8 页所有 BOX（#f0eee5）矩形顶带（rect.y+15..+100）内全部粗体行——box() 23pt 标题 + 手绘标题（如 P1 27pt「О ЧЁМ ПИШУТ СМИ」），共 **28 行**；另单测 P1 y=1660 栏目标题（无奶油盒，见 §6b）
- 结果（发货版）：27 行在框内，最紧余量：P1 `Стр. 2A2` +22.2px、P1 `СМИ　O QUE DIZEM OS MEDIA`（§6a）、P6 `ЗА И ПРОТИВ　PRÓS E CONTRAS` +32.6px、P7 `«Поздравляю с День студента!»` +42.3px、P1 统计框 `ТУР В ЦИФРАХ　EM NÚMEROS` 23pt **+56.4px**（真墨右 904.6，框右 961；ru-de 同类 D1 为 +36.6 溢出，本版无此问题；ru-es 最紧余量 +8.6px，本版最紧的 23pt 标题为 +56.4px）
- 与首轮备份逐行一致（28/28 数值相同）：相对首轮备份**无回归**
- occlusion 0 与 boxtitle_rc 0 对此类确为空信号（已不用其作证据；本节为 PIL 实测）

### §6a P1 y=664 `СМИ　O QUE DIZEM OS MEDIA`（27pt，观察项 O1，非缺陷）

- 四法：PIL 真墨 1864.4（+2.4）、span advance 1863.4（+1.4）、印 PDF 3x 光栅 1862.9（+0.9）、4x 裁剪光栅 1863.0（+1.0）；首轮 proof1（pt1）印 PDF 渲染恰为 1862（贴边）
- 判定：约 +1px，属光栅抖动/取整噪声，未见字形被裁；沿用首轮结论，不计缺陷；建议修 D1 时顺手缩短 2–3px（见 PROOF-NOTE O1）

### §6b P1 y=1660 `СЛОВО НЕДЕЛИ　A PALAVRA DA SEMANA`（22pt，缺陷 R2-D1，见 PROOF-NOTE）

- 该标题不在奶油盒内（右栏栏目标题，`content12.py:109`，栏右缘 1862；其下划线 hline 亦止于 1862），故 §6 的盒扫描未覆盖，单测发现
- 四法一致：PIL 真墨 **1886.5（+24.5）**、span advance **1887.4（+25.4）**、印 PDF 3x 全页光栅 **1886.9（+24.9）**、4x 裁剪光栅 **1887.0（+25.0）**；首轮备份 runs 逐值相同（未回归，是**存活**的首轮 MAJOR 缺陷）
- 进度管理说明：重建方 gate 未覆盖无盒栏目标题；重建报告的 “D1” 指地图 4 串（已落地，见 §9），与此标题溢出（首轮 pt1-D1）不是同一缺陷

## §7 溢出横扫（creambox + 矩形扫描）

- `tools/creambox.py` 全 8 页扫描（`creambox.log`）：**inside-only 负 clearance 0**；BELOW-WINDOW **95 行**，全部分类：+28.0 ×25、+32.0 ×41、+34.0 ×4、+37.0 ×25（次块首行，属设计；无 y=2348 例外行——本版为 95 行非 96 行）；未分类 0
- 与首轮备份扫描比对：**0 差异行**（字节一致）
- P7-TOOLBOX 汇总：3 盒，最小 inside clearance +11.9，最小 desc-clear **+5.9**（通过）
- 矩形/纯填充盒横扫（`rectscan.log`）：16/25/21/35/20/34/18/37 个 rect；无 rect 出页、无 rect 越右缘 1862、无文本起于 RIGHT 之外或 MX 之前；唯一纯填充盒为 P6 民调条（olive #46581f，x=708，右缘 ≤1308，全在页内）
- P2 盒降部观察（O3）：末行 `para o Avô Gelo.`（基线 1154.0，盒底 1159.0）PIL 真墨底 = **1159.00**，恰贴盒底（余量 +0.00px，未越出；独立复现首轮 1158.98 / +0.02 结论）

## §8 引号 / CJK / 禁词 / 填空键

- 弯引号成对：每页 SVG «/» 均平衡（P1 25/25、P2 4/4、P3 21/21、P4 73/73、P5 22/22、P6 1/1、P7 36/36、P8 17/17；text.md 165/165）；“/” 1/1（仅 P7 有意保留的 `«на “чёрной пятнице”»`）；SVG 直引号 `"` 0 个；直单引号 `'` 0 个
- CJK 孤儿标点：check_core 仅 1 项（P7 y553 `”».`，与核心相同；核心另有 4 项 CJK 孤儿，随葡语化消失）
- SVG 可见 CJK：仅 U+3000（每页唯一 CJK 字符）；text.md CJK 0 行；无简体残留
- 禁词/内部标签：SVG 与 text.md 均无 SOP / proofread / cover / geometry / lint / W47 / 2026-w47 / ru-pt / placeholder / TODO / FIXME；`VOL.5` 出现页数与核心完全一致（P1/P2/P4/P7 各 1 次，正文前瞻句「Полный итог — в VOL.5」，属内容非缺陷）
- `___` 字面填空：text.md **87** = 核心 87；SVG 87——模板缺口（核心同形继承），不作缺陷
- Q150：p8 键 `✓`，text.md 开放题说明，与核心一致

## §9 重建修复复验（D1/kicker/D2/D6）

- 地图 D1（重建方编号）：text.md `УЧЕБНЫЕ ДАННЫЕ` L459、`Три уровня, три темы` L504、`Большой тест недели + все ответы` L596；K1/K2 在 p6 SVG、K2 **不在** text.md（SVG-only 设计）、K3 在 p7 SVG、K4 在 p8 SVG——全部落地。源码：`content56.py:158`、`content7.py:12`、`content8.py:12`
- Kicker（`content12.py:18` 双空格已落地）：独立重测（`kicker.py`，INVEST-NOTE 方法 1，whole-run getbbox）：9 gaps **[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]**，min **5.9 px ≥ 4** ✓（与重建方数值逐值一致）
- Q25 D2（重建方编号）：`content12.py:276` 选项为 `День студента` ✓；全称 `Международный день студента` 在版/核心 text.md 各 ×2 ✓；首轮 pt1-D4（P2 y=2162 选项溢出 +6）亦因此修复：现该行真墨右 1663.8，余量 +198.2px
- Q20 D6：`content12.py:257` 键 `желании` ✓；text.md ×2 ✓；p8 键 20 = `желании` ✓；p8 SVG 答案行同步更新（`желании — желание = um desejo`）
- pt1-D7（网 PDF 斜体，MAJOR）：**已修复**——网 PDF 现含斜体字体 `LucernaNotoSerif-Italic` + `LucernaNewsreader-Italic`（首轮为 0 个）；P1 «чёрная пятница» 网/印均为斜体 16.12pt，span bbox 与印版逐值相同（1088.0–1222.8，» 1220.6–1229.3 紧贴）；文字层网/印均为 `чёрная пятница»`（无脱离）。系 webpdf.py 补丁（commit 40963281）所修
- D5（首轮 pt1-D5，P8 y=1302 答案说明行）：**只记录，不判**（按任务指令）。实测：PIL 真墨 1861.7（框内 +0.3）、span advance 1865.9（−3.9）、首轮印 PDF 渲染 1864（+2；该行 SVG runs 与首轮备份逐值相同）、**新测印 PDF 3x 裁剪光栅 1864.4（+2.4）**

## 附：首轮缺陷存活对照（pt1 PROOF-NOTE，7 项）

- pt1-D1（P1 СЛОВО НЕДЕЛИ +24）：**存活**，见 §6b / PROOF-NOTE R2-D1——重建未动此标题
- pt1-D2（P1 y=2348 quiz 行 +3）：**存活**，见 PROOF-NOTE R2-D2——光栅 +3.1、span +5.0、PIL +0.5、首轮渲染 +3
- pt1-D3（页脚说明行 5 页 +2）：**存活**，见 PROOF-NOTE R2-D3——PIL +0.3、span +4.3、首轮渲染 +2、**新测 P2 光栅 +2.9**；p3/p4/p5 SVG 与首轮逐字节相同，p2/p6 该行 runs 在 run-diff 中无变化
- pt1-D4（P2 选项 b 全称溢出）：**已修复**（Q25 短式连带修复，见 §9）
- pt1-D5（P8 y=1302）：见 §9，仅记录
- pt1-D6（Q20）：**已修复**（§9）
- pt1-D7（网 PDF 斜体）：**已修复**（§9）
