# 校对笔记 PROOF-NOTE — W47 zh-cn-ru（俄语讲解版），fix1 后独立复校（re-proof）

- **校对员**：独立复校员 reproof1（subagent，2026-11-11）
- **对象**：`~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-ru/`（fix1 已完成，31ce032d）
- **核心对照**：`production/2026-w47/core-zh-cn/`（已定稿）
- **工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-zh-cn-ru1/`（唯一 scratch；全部日志、渲染、裁图在此）
- **性质**：只检查、不改生产文件；未 commit、未 push、未 insert、未跑 lint、未重渲染交付的 web PDF（web PDF 字节不可复现，只比文字层）。生产目录只读验证。
- **解释器**：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；`TMPDIR` 一律指向本 scratch；凡 import 生产源码均设 `PYTHONDONTWRITEBYTECODE=1`。
- **前情**：proof1 (b) 唯一缺陷 D-01；fix1 只动 `content12.py:88` 删一词 `ещё `。本轮为 fix1 后的全量复校（SOP §8.4）。

## 结论（先写结论）

**本轮结论 (a)：零缺陷，可定稿。**

- **D-01 已修掉，三法重测全部通过**：PIL 真墨墨右 1850.5、余 **+11.5 px**；交付印 PDF 150 dpi 渲染像素墨右 1848.2 units、余 **+13.8**；文字层 span 右缘 1850.6 units、余 **+11.4**（印/网一致；旧串 0 命中）。三法均满足 ≤1862.0 且余量 ≥+5 px。
- 其余全部通过：机械门 11/11、SVG 重建 8/8 字节一致、重渲印 PDF 与交付逐字节相同、freeze 核心 baseline 8/8、freeze diff strict-CJK 新增 0、occlusion 0 flags、奶油盒横向真墨扫 599 文本 0 溢出 0 贴边、纵向 0 越边、页界 spill 0、孤儿 0、p8 extract 150/150、p8 compare CLEAN（keydiff []）、题干-键 150/150、CJK 守恒、日期星期全验、D4/D5 措辞在位、P8 最小字号 9.98 pt、§1.1 干净、8 页全页目视（交付印 PDF 110 dpi + 网 P1）零缺陷。
- 仅 1 项观察（O-1，proof1 已有，不列缺陷）：P2/P3/P5/P6 四处盒尾行西里尔下行字母贴盒底，墨底余 0.1 px（P6 0.7 px），严格在盒内，裁图目视确认未越出。

## 缺陷清单

无。本轮发现 0 项缺陷。

## 观察项（不列入缺陷清单）

### O-1（贴边，非溢出，proof1 继承）——P2/P3/P5/P6 四处盒尾行西里尔下行字母贴盒底

- **实测**：纵向奶油盒扫描 0 越边；最紧 4 处基线距盒底均为 5.1 px（P6 为 5.7 px），尾行字符串含西里尔下行字母 р/у，下行墨 5 px，**墨底距盒底仅余 0.1 px（P6 余 0.7 px）**，严格在盒内，与 proof1 数值分毫不差。
- **证据**：`crop-p2-tail-reproof.png`（交付印 PDF 110 dpi 裁图，2× 放大）——「предложения по-китайски.」的 р/у 下行恰贴盒底缘，未越出。
- **处理**：不列缺陷（量测与渲染均未越出）；与 proof1 相同量级，fix1 未动此处，无变化。

### O-2（只记录，proof1 继承）——D5 字体范围问题

- **事实**：全部俄文/拉丁解释层 `font-family` 均为 `Noto Sans CJK SC`。按任务书，此为待用户裁定的范围问题，只记录、不作门、不修。

### O-3（继承设计，非本版问题，proof1 继承）——P6 图表两柱非等比

- **事实**：P6 图表 139.38 亿件柱与 7.77 亿件柱长比约 5–10:1，而非数值比 18:1；与核心逐字节同形。图注已明示「两柱不同量、不作趋势比」，键 Q93–Q95 语义无误。
- **处理**：核心继承设计，本版忠实复现，不列缺陷。

## 逐项验证细节

### §A 身份与生产零写入

- 开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（`e69de29…`）；scratch 真实写盘 `probe.txt` 成功。
- 三 SHA 开工与收尾两次实测一致，且与任务书先验、与 `WEEKLY-KIT.md` Artifacts 一节完全一致：印 `bcfc550ff96ae87ce46fe1199592f5c7a690b91325dd3d5a410b11d95061305b` / 33,572,610 B；网 `8d3f72d35d4ac78cb0c9f52f56a930dae1c9251fc3a4527841bc30dd0ac888d3` / 2,486,423 B；文 `de12db587c41005301b221cce52ae0d088ec52f9eaccf2338aa94382f00e8094` / 60,508 B。
- 生产零写入核查：`git status --porcelain` 开工收尾相同（本版目录仅 `??` 未入仓）；SVG sha256 8/8 与开工快照一致（`svg-sha-start.txt` vs `svg-sha-end.txt`，哈希逐个相同）；`__pycache__` mtime 仍为 2026-11-11 14:30:58，未写新字节码。本轮 `run.py` 重建与 `render.py` 重渲均在 scratch 副本中跑，`OUT`/`BASE` 已重定向为绝对路径（跑前已验写盘目标），生产 SVG/PDF 零写入。

### §B D-01 重测三法（修后，交付文件实测）

| 方法 | 墨右 | 盒右 1862.0 | 余量 | 要求 |
|---|---|---|---|---|
| PIL 真墨（新串，19 pt；旧串复现 −29.5） | **1850.5** | 1862.0 | **+11.5 px** | ≤1862.0 且 ≥+5 px ✓ |
| 交付印 PDF 150 dpi 渲染像素（`render-p1-fix1.png`，3047×4219 px） | **1848.2 units** | 1862.0 | **+13.8 units** | ≤1862.0 且 ≥+5 ✓ |
| 文字层（PyMuPDF span，印/网一致；旧串 0 命中） | **1850.6 units** | 1862.0 | **+11.4 units** | ≤1862.0 且 ≥+5 ✓ |

- 渲染像素法校准：奶油盒右缘在 y=650 处实测 **1861.7 units**（与 proof1/fix1 一致）；同盒 18.5 pt 段落行最右墨 1836.7 units（proof1：1836.1，0.6 为阈值/舍入噪声，仍余 25.3）。
- SVG 元素复核（`svg-texts.json`）：P1 y=1252.0 单 run，x=1461.5 size=19，新串 `Время сдачи: 10 нояб. — финал не сыгран` 在位；`content12.py:88` 新串在位，`:86` 长段落 `ещё` 仍在 1 处（全文件 `ещё` 仅此 1 行）。
- **裁图目视**：`crop-p1-pressline-fix1.png`（交付印 PDF 150 dpi 裁图，2× 放大）——末行完整落在奶油盒内，尾部 `сыгран` 距盒右缘有明显空隙；长段落 `ещё` 未动。
- 结论：D-01 已修掉，三法余量均 ≥+11 px。

### §C 机械门（全部独立自跑，见 GATE-LOG）

- `gates-zhcn.py` 11/11 ALL PASS（occlusion 0、img_overlap 0、p8 150/150、compare CLEAN keydiff []、freeze 8/8、印/网文字层 8/8 posdiff 0 msdiff 0、P8 字号 9.98 pt、chips = 核心、U+2019 0、§1.1 干净）。网 PDF 按 fix1 后新版实测：P1 355/355（修前 356，恰为删去的一词）、pdftotext 印/网均为 52,554 B。
- freeze `diff --strict-cjk` 新增 CJK **0**（逐页与 proof1/fix1 计数完全一致：P1 +91/−45、P2 +71/−52、P3 +40/−39、P4 +117/−43、P5 +39/−38、P6 +114/−41、P7 +338/−105、P8 +1405/−208）。
- freeze `baseline` 核心 8/8 字节一致，core integrity 确认。
- scratch 重建 `run.py` RC=0、TOTAL 150（A2 56 / B1 69 / B2 25；分版 10/18/18/18/18/18/12/38）、0 溢出、P7 teaser 2588.78（≤2596）、P8 keys 2535.1（≤2560）、P8 测验流 964.8、配图末 1270.6；重建 SVG 与生产 SVG sha256 8/8 一致（`OUT` 已重定向，无 O-3 式写回）。
- 重渲印 PDF（`render.py`，scratch 副本）：33,572,610 B，SHA `bcfc550f…`，与交付印 PDF **逐字节相同**（`cmp` 通过）。
- occlusion `--selftest` OK（6 类 planted 全触发，clean 对照静默）；本版 0 flags。
- P8 字号独立实测（PyMuPDF，印/网一致）：P8 最小 **9.98 pt** ≥ 9.75 pt；各页最小 P1 10.50、P2–P5 11.62、P6 12.75、P7 11.62、P8 9.98 pt——与 proof1 分毫不差。
- ABSTRACT.txt 426 B，尾换行在位。

### §D fix 范围核查（只动一处）

- `text.md` vs 修前（fixer `textmd-before.md`）：`diff` **仅 L127 一行**（`ещё ` 删去，7 字节）。
- SVG vs 修前快照（fixer `svg-sha-before.txt`）：**仅 p1 变化**（`be2231cb…` → `fbe71fe7…`），p2–p8 逐字节一致 7/7。
- `WEEKLY-KIT.md`：Artifacts 一节三 SHA 与盘上交付一致；Fix round 1 一节记录的旧三 SHA（印 `7cd883dd…`、网 `ab0aaf10…`、文 `f722ad0f…`）为已取代版本，保留在案。

### §E CJK 守恒与题干-键全验

- 全刊字符串级 multiset 对照：**ru 无一 CJK 字符超出核心字符集**（`CJK(ru) − CJK(core) = ∅`）；核心独有 CJK 仅「英」「解」二字（P1 徽章行被俄文徽章取代）。
- 题干 AST 对照：ru 与核心各 150 条，**stem/key/level/type/opts 0 差异**（`stem-compare.txt`）；注记 149/150 为俄文（Q150 为 f-string 范文，同文，见 §G）。
- keycheck REG vs P8 抽取键：**149/150 精确**，唯一非精确为 Q150（REG 键 `(开放题，范文如下)` vs 印键 `✓`，开放写作题按设计；`keycheck.py` 自身 rc=1 只因其硬编码期望英文抽取词 `Open task`，proof1 已记录，不属缺陷）。
- 金句 8 条各在正文 + P7 出现 2 次。

### §F D4 / D5 措辞落地

- **D4**：全文「第一次」仅 2 处中文，均带「全球总决赛」限定——P4 正文 `:695`「BLG赢了T1，这是中国队第一次在全球总决赛的BO5里打赢T1」；Q56 题干 `:817`「BLG是第一次在全球总决赛的BO5里打赢___。」；键注 56 俄文「BLG впервые обыграла T1 в BO5 на Worlds」带 на Worlds 限定。SVG P4 同句 1 处。无未限定首胜表述。
- **D5**：假表述「GEN 今年一场没输」全文 0 处；真表述保留——P1 `:37` 与 P4 `:697` 均为「GEN在S16一场没输，只丢了一小局」（S16 限定）；P4 小日历 `:729`「GEN今年 — 淘汰赛一局没输」与核心逐字一致。Q4「三支韩国队」有据：P1/P4 均列瑞士轮 HLE、八强 DK、半决赛 T1 三场。

### §G P8 打包专项

- Q150 键为 **1 行**；键流终值 **2535.1**（容量 2560，余 24.9）；P8 印键 **149/150**（仅 Q150 开放题 `✓` 例外，按设计）；p8 extract 150/150。
- 范文与核心一致：同一范文，CJK 各 120 字；「138 знаков」计数与 `writing model chars: 138` 一致。
- P8 D-head 「Читай и ответь」advance 417.4，墨右 1406.0、栏右 1411.5，**余 5.5 px**，贴边但合。

### §H 几何（PIL 真墨 + 交付 PDF 渲染像素）

- **奶油盒横向扫描**：599 个盒内文本元，**溢出 0 处**（proof1：仅 D-01 一处；fix1 后为 0）；贴边（<8 px）**0 处**。
- 纵向奶油盒溢出 **0**；最紧见 O-1。
- 页界 spill：全部文本元 x∈[0,1950]、y∈[0,2700]，**0 处**。
- 栏目标题复量：A-head advance 406.3、墨右 494.0、余 16.5；P4 C-head「Читай расписание」376.6、余 45.5；P5 C-head「Время и числа」376.3、余 46.5；P1 数字标题墨右 941.5、盒右 961、余 19.5；P2 日历标题墨右 1403.0、照片左缘 1439.5、余 36.5；P2 词卡例句各 1 行（退换货例「не подошло? верни пораньше」1 行）。
- P4 gloss：俄文前缀「Примечания｜」量得 **6 行**（y=595.9–744.5），盒底 792.21，下方 GEN 行 y=822.4，净空 30.2 px；occlusion 0 flags。
- 孤儿扫描（行首闭合标点 + 同基线左邻判定）：ru **0 处**。
- 引号配对：「“”」2/2、「«»」6/6（proof1 计 8/8 为 text.md 层；SVG 层 6/6，逐行失衡 0）、ASCII 引号 0。
- 禁词：SOP/proofread/cover/lint/占位/内部/geometry audit 全 0；「VOL.」SVG 层 14 处与核心等数（VOL.4 10、VOL.5 1）；「第4号」SVG 层 1 处与核心等数（text.md 层 2 处与核心等数）。
- 繁体残留：`CJK(ru) − CJK(core) = ∅`，opencc 残留 0。
- U+2019：0（.py 层与 .text.md 层；gates 亦 0 文件）。
- 「Конструкция:」SVG 层 2 处（P7 句式框标签 y=1109.0 + 句式行 y=1200.1，均为同框合法出现）、「Структура:」0 处。

### §I 日期星期全验（`date -d`，2026 年）

- 11月4日周三、5日周四、6日周五、7日周六、8日周日、9日周一、11日周三、14日周六、15日周日、21日周六、22日周日。文中全部星期断言与之相符：11月8日星期日、9日星期一、11日星期三、14日星期六、15日星期日、21日星期六、22日星期日；P7 俄文注「(вс 15 нояб., 3 часа ночи)」「(вс 22 нояб.)」「(сб 21 нояб.)」全对（`content7.py:33`）；Q107 选项 A「11月22日星期日」✓（`content7.py:40`）。

### §J 徽章

- 徽章行（y=434，14 pt bold）：「КИТАЙСКИЙ ТЕКСТ　ПОЯСНЕНИЯ НА РУССКОМ」，**0 中文**；PIL 真墨 advance 333.8 px、墨右 422（x=88 起），远在版心内。核心同位徽章为拉丁-only；俄版西里尔-only 与之同构，通过。

### §K 目视（交付印 PDF 110 dpi 全 8 页 + 网 P1）

- P1：截稿行已收进盒内（见 §B 裁图）；徽章西里尔-only、截稿段、数字盒、日历、目录、本周词均正。
- P2：日历标题离山谷照 36.5 px；4 词卡例句各 1 行；练习 A–D 齐全；尾行贴边见 O-1。
- P3：三候、读书月、日历、练习齐全；尾行贴边见 O-1。
- P4：gloss 6 行净空；赛程表、三分之二、D4/D5 措辞、图注「2003年」无空格均正。
- P5：片单（撤档案在位）、高频词、电影小日历、练习齐全。
- P6：三波/139.38/7.77、图表、深读要点、三问齐全（图表比例见 O-3）。
- P7：诊所 1 行化、wcn 1 行、句式框、金句 8 条、下期预告条底 2588.78 清页脚。
- P8：A–F 齐全，keys 1–150 + 页脚清；Q150 范文 + 配图在位。
- 网 P1 与印 P1 目视一致（同 SVG 源；文字层 8/8 posdiff 0 msdiff 0）。

## 交付物

- 本文件 `PROOF-NOTE.md`；`GATE-LOG.md`（门禁逐项实测值）。
- 证据与日志见本 scratch：`gates-ru.log`、`gates-ru.json`、`freeze-diff.log`、`freeze-baseline.log`、`run-rebuild.log`、`render-rerun.log`、`p8extract.log`、`p8compare.log`、`p8extract.json`、`keycheck-150.json`、`keycheck.log`、`stems-ru.json`、`stems-core.json`、`stem-compare.txt`、`cjk-diff.log`、`cream-sweep.json`、`cream-sweep.log`、`orphan.log`、`text-checks.log`、`textlayer-D01.log`、`measure.log`、`svg-texts.json`、`render/p1–p8.png`、`render/web-p1.png`、`render-p1-fix1.png`、`crop-p1-pressline-fix1.png`、`crop-p2-tail-reproof.png`、`svg-sha-start.txt`、`svg-sha-end.txt`、`svg-sha-rebuild.txt`、`probe.txt`、`rebuild/`（scratch 重建副本）、`rerender/`（scratch 重渲印 PDF 副本，与交付逐字节相同）。
