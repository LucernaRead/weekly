# GATE-LOG — 2026-W47 de-en fix1（重建 4，2026-11-11）

构建：`TMPDIR=<scratch>/tmp tools/venv/bin/python build_edition.py en`
（解释器 `~/workspace/weekly-git/tools/venv/bin/python`，Pillow 13.0.0；
日志 `build-fix1b.log`；另 `measure-fix1b.log` 24/24 先行通过）。
第一次重建（build-fix1.log）因 /tmp 写满致 webpdf ENOSPC 失败 3 门，
见 FIX-LOG §6；以下为第二次重建的全套门禁。

## 门禁总表（build_edition.py 输出，ALL GATES PASS）

| 门 | 结果 |
|---|---|
| run.py exit 0 / 0 FLOW OVERFLOW / 0 HEAD TOO WIDE / TOTAL 150 | PASS |
| render.py exit 0，印版 10,966,406 B | PASS |
| webpdf exit 0，网页 1,597,882 B < 7 MB | PASS |
| verify.py TOTAL 150，编号连续，SVG 重跑字节一致，SOP 1.1 样式审计 True，verbatim OK，P8 字号底线 True，17 禁词全无 | PASS |
| occlusion_audit.py 自检通过（6 类 planted 全触发，clean 对照静默） | **0 flags** PASS |
| p8.py extract | 150/150 PASS |
| p8.py compare vs core | **CLEAN**，missing=[]，extra=0，keydiff=[137, 138, 139, 150] PASS |
| freeze.py diff exit 0 | 新增 CJK 7 个，全为 U+3000（P2–P8 各 1，P1 0）PASS |
| print/web 文字层（pdftotext） | default 50,433B / 50,433B，词多重集相同；-raw 归一化 49,277B 双方完全相同 PASS |
| chips（rx="2.7" 矩形） | 逐页 10/15/18/15/18/18/12/35，TOTAL 141；P8 A2 22 / B1 13 / B2 0 PASS |
| text export（源稿导出） | exit 0，49,665 B，48,034 字符，591 条目，150 题 PASS |
| P8 最小字号（PyMuPDF） | **9.94pt** ≥ 9.75pt 底线 PASS |
| measure.py en | **24/24 PASS，0 FAIL**（含 P7 toolbox D4 entry 2 行） |

流向末端（build.log）：P1-headline 1554、P3 col3 1643.19、P5-ex 2441（= core）、
P7-A2 1278 / B1 1342 / B2 1306、P7 image ends 1541.83、**P7 col3 ends 1534.38**、
P8-battery 1409、P8-keys 2481（底边 2560，余 79px）。除 P7 col3（D3 下移 16.4）
外与 rebuild 3 一致。

## keydiff 逐项说明（[137, 138, 139, 150]，全部预期内）

- Q137：核心键 '德甲周五回归。' → 本版 'The Bundesliga returns on Friday.'
  （E 组正向翻译题，键译成英文，预期内）
- Q138：核心 '市场周日关闭。' → 'The markets are shut on Sunday.'（同上）
- Q139：核心 '我做一个降临节日历。' → 'I am making an Advent calendar.'（同上）
- Q150：核心 '开放题' → 'Open task'（开放写作题标签译成英文；抽取器截断，见 keycheck）
- Q140 不在 keydiff 中：反向题（英译德），键本就是德文目标语句，正确。

## keycheck（独立，keycheck-150.json）

- REG 150 条 vs P8 抽取键：**149/150 精确**；唯一非精确 Q150（抽取器把 REG 键
  "Open task — follow the points in the writing box" 截断为 "Open task"，预期内，
  Q150 已在 keydiff 中）。D2 所在 Q67 键 `B` 正确（只改了键注引号）。

## freeze 直接冻结（freeze_direct.py，freeze-direct.json）

- 渲染级：**8/8 PASS**，frozen 数 / sha8 与 rebuild 3 逐字节一致：
  P1 147 `083e2a2a` / P2 163 `689045ad` / P3 195 `fc88f676`（Q34 新题干指纹）/
  P4 166 `df1bebf7` / P5 173 `86fa4421` / P6 175 `2bbe05f9` /
  P7 150 `b7aa0771` / P8 186 `57e118e7`。
  （D1/D2/D3 均不在冻结交集内：D1/D2 是英文独有串，D3 只改盒高不改文字——
  冻结指纹不动正是"未动德文正文"的证据。）
- 源层级：FAIL——新增字面量 1 处未入账：`WEIHNACHTSWÖRTER　Words`
  （rebuild 3 盒标题修复，共享 tr_en.py 仍是 `Christmas words`，见 FIX-LOG §8；
  预存问题，fix1 未引入、未修。删除字面量 0 处未入账。）

## 弯标点全扫（U+201C/U+201D/U+2019；SVG + text.md + 双 PDF 文字层）

| 位置 | U+201D | U+201C | U+201E | U+2019 |
|---|---|---|---|---|
| P1 SVG | 0 | 5 | 5 | 0 |
| P2 SVG | 0 | 0 | 0 | 0 |
| P3 SVG | 0 | 0 | 0 | 0 |
| P4 SVG | 0 | 0 | 0 | 0 |
| P5 SVG | 0 | 6 | 6 | 0 |
| P6 SVG | 0 | 0 | 0 | 0 |
| P7 SVG | 0 | 21 | 21 | 0 |
| P8 SVG | 0 | 3 | 3 | 0 |
| text.md | 0 | 35 | 35 | 0 |
| 印版文字层 | 0 | 35 | 35 | 0 |
| 网页文字层 | 0 | 35 | 35 | 0 |

- **全版 U+201D = 0**（改前 2 处，即 D1/D2，已清零）。
- U+201C = U+201E = 35：全部成对为德式 „ "（P1 德文提问 5、P5 德文标题 6、
  P7 德文句 21、P8 德文对话 1 + D1/D2 新对 2），保留。
- U+2019 = 0（直撇号 U+0027 11 处不变）。
- 字体实测（Noto Sans CJK SC，em=40）：U+201C 40.0 = U+201D 40.0，
  U+201E 19.0（见 FIX-LOG §8）。

## 盒间隙核查（creambox）

- 原版 creambox.py（+45px 窗口）P7 改后：工具盒 y=330 底 799.9 末基线 783.9
  间隙 **+16.0**；LESERBRIEFE +10.4；NOCH EIN WORT +13.8。
  其 −35.0 三行（'101.'/'105.'/'109.'）是窗口伪报：练习题号在 BEISPIELE 盒
  下方 35px 的流内，非盒内溢出（盒内末基线间隙 +47.4，P7 全页目视无溢出）。
  同理 P1 y=1312（−24.0）、P2 y=1222（−44.9）两行是下节标题落入窗口，
  改前即有，与 D3 无关。
- 精炼版 creambox_check.py（溢出带 = 底边外 0–8px，8 页全扫）：**NO OVERFLOW**，
  exit 0。改前同一脚本只报 1 处溢出（工具盒 783.9），改后 0 处。
- 全版其余盒内间隙 +10.4…+47.7（见 creambox-check-after.log）。

## 盒标题（boxtitle）

- 以发货 SVG 实测 7/7：DIE STILLE WOCHE 394.6、WEIHNACHTSWÖRTER Words 359.9、
  DER TIPP 262.5、ADVENTSWÖRTER 397.9、DER WERKZEUGKASTEN 382.9、
  LESERBRIEFE 352.8、NOCH EIN WORT 366.1（与 proof2 的独立实测逐一吻合），
  墨水均止于 1862.0 盒右缘内。
- `boxtitle.py en` 读共享 tr_en.py 得 6/7（`Christmas words` 483.5 超），
  系 §8 预存的共享 tr 旧值所致，成品以 SVG 实测 7/7 为准。

## Q34 与 content12 不回退

- 新题干 `"Am Montag öffnet in Köln der erste ___."`：源码 / text.md / P3 SVG /
  印版文字层 / 网页文字层各 1×；旧题干 `"Am Montag öffnen in Köln die ersten ___."`
  源码 / text.md / P3 SVG 0×。P3 冻结 sha `fc88f676` 不变。
- content12.py:58 未动（`Deutschland hat nach vier Spielen ___ Punkte.`）。

## 目视

- P7 全页 100 dpi（render/p7-100dpi.png）：工具盒、读者来信、NOCH EIN WORT、
  Sätze、诊所、预告均在位，无重叠、无越线，页脚完整。
- P7 工具盒 200 dpi 裁切（render/p7-toolbox-200dpi.png）：6 条全在奶油盒内，
  末行 `Es ist fraglich, ob ... = Whether … is open` 下方有干净奶油余量，
  g 降部在盒内。
- P8 H 写作框 200 dpi 裁切（render/p8-hbox-200dpi.png）：D1 已为德式
  `„My week in November“`，开引号紧贴；闭引号与句号间空隙与 P5 标题同式
  （字体实测见上）。
