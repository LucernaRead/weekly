# PROOF-NOTE — 2026-W47 zh-cn × nl · 独立复校 reproof（fix1 后全量重校）

- 校对员：reproof（独立复校，只复校，不改生产文件，不 commit、不 push）
- 对象：`production/2026-w47/2026-w47-zh-cn-nl/`（fix1 后状态，2026-11-11）
- 核心对照：`production/2026-w47/core-zh-cn/`（已定稿，未动）
- 工作区：`hidden_files/w47/scratch-reproof-zh-cn-nl1/`（独占；脚本、日志、渲染件全在此）
- 结论：**(a) —— 零缺陷，可定稿。**

## 三 SHA 先验（开工 / 收工两次核对，一致）

| 文件 | SHA-256 | 大小 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-NL.pdf` | `3a160cae374c2e713daac7de9f7a0bfba0f77513db31894673c0d40f8344c628` | 44,048,879 B |
| 网 PDF `Lucerna-VOL4-NL-web.pdf` | `495594dc8d712268b336c6bcfb39dc0286f45ce20624cb163d02e9f5e9aeefac` | 2,703,048 B |
| 文 `2026-w47-zh-cn-nl.text.md` | `9bc8212fa100631226c03c4debbf31bba96557d1c0cad002076cba0c1d0732b8` | 50,059 B |

开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功 +
scratch 内真实写文件成功后才动手。生产零写入：收工时全版 46 个文件 SHA
与开工快照逐一比对，46/46 OK，0 差异；三 SHA 与开工值相同；核心 SVG
开工/收工重哈希无变。KIT 三 SHA 与上表一致，KIT 的 b2"26.3px clear"改写
在位（Adjudications 节已说明 26.3px 是到照片的距离，盒边为准）。

## fix1 四项逐项独立重测（PIL 真墨 + 交付 PDF 渲染像素双法，门限 ≥+5px）

四行均为左锚定（`svglib.py:387` `anchor="start"` 默认；`content12.py:88`
`p.text` 与 `content12.py:187`/`content56.py:25` 的 `Flow.box` 标题均无
anchor 参数——已逐一核实，缩短措辞确能移右缘）。

### b1 P5「这一周的高频词 Woorden」—— 修好 ✓
- 源码：`content56.py:25`，`Woorden van de week` → `Woorden`。
- PIL 真墨：标题墨右缘余量 **+118.0 px**（盒内最紧行 +64.5 px）。
- 交付 PDF 文字层：span 右缘 632.47 pt，盒边 720.75 pt，余量 **+88.28 pt**。
- 交付 PDF 100 dpi 渲染像素：最右墨点 630.72 pt，余量 **+90.03 pt**
  （+125.0 px @100 dpi）；盒边外波段内无墨（1097 pt 起的簇为第 3 栏正文，
  与标题隔 376 pt，非溢出）。裁图 `render/b1-title-zoom.png` 目视：标题
  在盒内结束，右缘大段留白。

### b2 P2「本周生活小日历 Data deze week」—— 修好 ✓
- 源码：`content12.py:187`，`Data van deze week` → `Data deze week`；
  盒边 x=1411.5 为准（KIT 改写已确认在位）。
- PIL 真墨：标题余量 **+44.5 px**（盒内最紧行 +31.6 px，为 `BLG` 行）。
- 交付 PDF 文字层：span 右缘 1026.37 pt，盒边 1058.625 pt，余量 **+32.26 pt**。
- 交付 PDF 100 dpi 渲染像素：最右墨点 1025.28 pt，余量 **+33.35 pt**
  （+46.3 px @100 dpi）；盒边外 1079.28 pt 起为第 3 栏照片，与标题隔
  20.7 pt。裁图 `render/b2-title-zoom.png` 目视：标题在盒内结束，与照片
  有明显间隔。

### b3 P1 截稿行 `Sluiting: 10 nov. — finale nog niet gespeeld`—— 修好 ✓
- 源码：`content12.py:88`，删 `de `；`:86` 长段落未动（已核实原文在位）。
- PIL 真墨：该行余量 **+24.0 px**（为该奶油盒最紧行）。
- 交付 PDF 文字层：行最右 1379.39 pt，盒边 1396.5 pt，余量 **+17.11 pt**。
- 交付 PDF 300 dpi 渲染像素：最右墨点 1377.84 pt，余量 **+18.66 pt**
  （+77.8 px @300 dpi）；盒边外无墨。裁图 `render/b3-sluiting-zoom.png`
  目视：`gespeeld` 的末字母 `d` 完整，行尾距盒边有明显留白。

### b4 P1 数字框第 3 行重排 —— 修好 ✓
- 源码：`content12.py:50`，`21 nov., zaterdag — première van de nieuwe
  film 《试探》`，同词重排，仍 2 行、盒高不变。
- 交付 PDF 文字层逐行扫描（全 8 版）：行首闭合标点（`》/」/）/”/、/。/，`）
  **NONE**；该两行实测：`21 nov., zaterdag — première van de`
  （x=417.4–667.0 pt, y=993.4–1008.4 pt）/ `nieuwe film《试探》`
  （x=417.4–561.5 pt, y=1007.4–1029.0 pt）。裁图 `render/b4-box-zoom.png`
  目视：`》` 落在第 2 行行尾、盒内，无孤儿。
- 核心对照：核心印 PDF 孤儿扫描亦为 NONE；0 新增。

## 通过项（逐项实测值，详见 GATE-LOG.md）

- **版本重建**：scratch 副本 OUT 重定向后 `run.py` rc=0，TOTAL 150
  （A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW，
  0 HEAD TOO WIDE；P7 teaser ends 2586.3；P8 keys ends 2491.1。重建 8/8 SVG
  与交付版 sha256 一致；freeze baseline（核心）8/8；freeze baseline
  （本版自身）8/8；重渲印 PDF 与交付印 PDF SHA 逐字节相同
  （`3a160cae…4c628`，44,048,879 B；8/8 卡片亦逐字节一致）。
- **freeze diff**：`--strict-cjk` rc=0，TOTAL added CJK **0**。与 proof1 的
  #3 版 freeze-diff 逐串比对，差异恰为 4 处 fix1 改动（P1 三串分段变化、
  P2/P5 各一串），无其他串变化。
- **occlusion**：自检六类全触发；本版 0 flags，核心 0 flags，NEW vs core 0。
  （空信号说明不变：occlusion 对纯填色奶油盒横向越边全盲，本轮越边结论
  均由真墨横扫 + 渲染像素得出，`boxtitle_rc: 0` 从不作为证据。）
- **奶油盒真墨横扫**：全 8 版 **35 个**奶油盒（盘上实数；proof1/KIT 的
  “40”系多计，核心同为 35，逐页 5/10/5/3/4/5/3/0），0 负余量；
  最紧 +13.5 px（P4 `看比赛的中文　Wedstrijdwoorden`，未动旧盒）。
  盒标题横向真墨扫：35 盒标题 0 负，最紧 +13.5 px；纵向跨底边扫 0；
  spill 扫 0；P1 绿带最紧 +29.95 px。
- **P1 重点扫**（zh-cn-ru proof1 教训）：P1 日历盒（b3 行）+24.0 px；
  P1 数字框标题 +45.25 px（盒内最紧行为第 1 行正文 +21.0 px）；
  P1 各盒标题均 ≥+45.25 px；绿带 +29.95 px。
- **P8**：`p8.py extract` 150/150；`compare` vs 核心 CLEAN（keydiff []）；
  P8 最小字号 **9.98 pt**（≥ 9.75 pt）；芯片 A2 11 / B1 24 / B2 3 = 核心。
- **150 题三方手验**：REG 150 题全部题干在 `.text.md` 中（0 缺失）；
  `.text.md` 末 150 行答案键与 P8 提取键 0 差异（Q150 两处同为 `✓`）；
  5 组配对题逐组核对无误（P2 a/b/c/d、P3 b/d/a/c、P4 d/b/c/a、P5 c/b/d/a、
  P6 c/d/a/b）；150 行题干 + 键逐行读过，单题语义抽查覆盖全部 150 题，
  键与题干、键注、正文事实一致；仅 Q150 一处预期差异（开放写作题，
  REG `(开放题，范文如下)` vs 印出 `✓`，为截断式印法）。Q150 范文实测
  **138 字**（含标点），在 120–180 字内；范文内星期与日期自洽
  （周日决赛 15 日、周一包裹 16 日、周六电影 21 日、周日小雪 22 日）。
- **印/网文字层**：P3/P4/P6/P7/P8 msdiff=0、posdiff=0；P1 msdiff=6、
  P2 msdiff=1、P5 msdiff=3——三处差异恰为 b1–b4 的 4 处改动
  （P1：b3 删 `de` 1 + b4 重排 5；P2：b2 删 `van` 1；P5：b1 删
  `van/de/week` 3），其余页 0——为已知待全家统一重建状态（网 PDF 仍为
  #3 版），记为预期项，不作缺陷。网 PDF 孤儿扫描仅含 #3 旧串 b4
  （`》gaat in première`），与预期一致。
- **§1.1**：纸色 `#fbfaf6` ×8；描边 rect 0；VOL.4 全 8 版在位
  （P7 VOL.4 2→1 为 KIT 已载明的 letters-box 删 "in VOL.4" 修复；
  VOL.5 各 1 处为下期预告，核心同）；调色板：P2–P8 无表外色；P1 的
  9 个表外色（插画色，如 `#d7b257`/`#edd17f`/`#4d72b4`）与核心 P1
  色集逐项相同（版-核心色集差 0），为核心继承插画色，非本版新增、
  非家具禁用色。U+2019 在 SVG 与 `.text.md` 中均为 0。
- **8 条本周金句**：各恰 2 次（正文 + P7），与核心一致。
- **D4/D5**：P4 正文「这是中国队第一次在全球总决赛的BO5里打赢T1」
  与 Q56 题干、键注 56 全部在位（空白归一化检索；早先一次逐行直查
  MISSING 系提取换行断裂假象，已用归一化复核纠正）；P1/P4 的 S16
  限定表述、淘汰赛一局没输均在；150 题键未动（freeze-diff 差异仅
  4 处修复串，无 key 串被编辑）。
- **日期**：`date -d` 核验 11 月 1 日周日、4 日周三、5 日周四、6 日周五、
  7 日周六、8 日周日、9 日周一、14 日周六、15 日周日、16 日周一、
  21 日周六、22 日周日，与文中全部一致。
- **目视**：8 页 100 dpi 全页渲染逐页目视（`render/p*-small.png`），
  无溢出、重叠、压页脚；P7 teaser 带距页脚有空隙，P8 答案区末端
  2491.1 距底边 2560 有余量。
- **"next Sunday"**：本版与核心的 SVG、`.text.md`、源码中均无此串，
  该条规则本版空适用。

## 缺陷清单

无。结论 (a)，零缺陷，可定稿。

## 观察（非阻塞，不计入缺陷；多为核心继承）

- O1：Q37（P3）与 Q74（P5）为同一题（读书月 7 场馆），key 一致，核心亦然；
  Q36/Q140（小雪之后天气更冷）、Q131–Q146 的 P8 复习复用亦与核心同构。
- O2：P1 日历盒内两条截稿线内容重复（长段 + 短行）；核心同构——核心亦有
  长段（"…not yet played at press"）+ 短行（"Press time: Nov 10 — the
  final not yet played"），短行即 b3 行的英文原文。
- O3：P1 快递柜配图为俄语文字储物柜（「ТУТ ПОСЫЛКИ 24/7」），标为（资料图），
  核心亦然（proof1 已记）。
- O4：KIT 称“Photo credits kept in English”，实际各页均为 `Foto:` 且 P5 为
  `Publiek domein`——版面本身前后一致的荷兰语化，无问题，唯 KIT 表述不准
  （proof1 已记；KIT 文字问题，非版面缺陷）。
- O5：奶油盒实数 35，非 proof1/KIT 所称 40（盘上逐页计数 5/10/5/3/4/5/3/0，
  核心同数；本轮 35 盒全部实测，0 负）。
- O6：首次重渲遇 Cairo 字体子集化瞬态异常（见 GATE-LOG 门 4 备注）：首跑
  PDF 290,435,383 B、67,372 对象、24,921 个 BaseFont 条目（逐元素子集化），
  与交付 SHA 不符；但该文件文字层与交付 8 页全 0 差、P1/P5 渲染像素
  100% 一致，内容等价已证。干净重跑（无并发孪生进程）即逐字节复现交付
  PDF（44,048,879 B，SHA `3a160cae…4c628`），与 fix1 19:03 的复现一致；
  异常未再现，判定为渲染环境瞬态，非版面缺陷。
- O7：P7「Zo wordt het Engelse «Sunday, Nov 22» 11月22日星期日」以法语引号
  标英文例；P1 副标「De finale ontmoet de pakketten」措辞生硬但可懂；
  P4 C-head「Lees het programma」与 glossline「Lees het schema op pagina 4」
  对同一赛程表用词不一（programma/schema）；P1 用「Vul de zin in」，
  其余各版用「Vul in」——与核心自身的 Fill in the blank / Fill in 差异
  同构（proof1 已记）。
- O8：孤儿填空行（Q130/Q36/Q37 式）属观察类、核心继承，不修不报缺陷。
