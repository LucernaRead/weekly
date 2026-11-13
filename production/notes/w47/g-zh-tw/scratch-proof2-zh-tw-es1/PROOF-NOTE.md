# PROOF-NOTE — W47 zh-tw-es（西班牙语读者 × 繁体中文目标）· proof2（重扩散新版全量重校）

## 结论：(a) 零缺陷，可定稿

重扩散新版自头全量重校（SOP §8.4），未发现任何缺陷。全部机械门禁一次通过（见 GATE-LOG.md），全文精读 150 题、日期星期、算术、西班牙讲解层逐项核对无误，8 页目视干净。
本轮发现 0 项缺陷；下方“观察”2 项均按任务给定裁决规则核定为非缺陷（STRADDLE 四处无裁切/无重叠/无回归；freeze strict-CJK 字面 FAIL 只是家具语名）。

- 校对员：proof2 复校（独立重校，不依赖 proof1 旧结论）
- 校对时间：2026-11-11 ~19:30–20:35 UTC
- 对象：`production/2026-w47/2026-w47-zh-tw-es/`（重扩散新版；核心已定稿，re-proof #3 结论 (a)）
- 只读生产：未改任何生产文件，未 commit/push，未重渲染交付的 web PDF；run.py / render.py 重建结果与交付逐字节一致（19/19 文件 SHA 校验通过）

## 三 SHA 核对（开工先核，与任务给定一致）

| 件 | 字节 | SHA-256 |
|---|---|---|
| 印 `Lucerna-VOL4-ES.pdf` | 23,256,381 | `e32c58c489ebb9a79e2d9c6029c3c0c23931c8bcbaea631144489daef3454a2c` ✓ |
| 网 `Lucerna-VOL4-ES-web.pdf` | 2,529,735 | `fb90e8270f4bfba8a517c8f81a95dc3814b0d3fd0fa5287d12aceb76767e5b6e` ✓ |
| 文 `2026-w47-zh-tw-es.text.md` | 52,246 | `59439c7db9e176b8bb6138fafde56e0ee6f720460659a0277d2ed8c42bffc778` ✓ |

## 缺陷清单

**无。**（零项）

## 观察（非缺陷，逐项实测裁定）

### 观察 1 — 双语小檔标题 STRADDLE ×4（旧版既有属性，无回归）

双语小檔标题（中文名 + 西班牙语名）墨迹伸出无边框米色盒右缘，文字本身完整可读、无任何重叠。按 STRADDLE 裁决规则实测：

| # | 标题（源码行） | 页 | 墨右缘 → 盒右缘 | 超出 |
|---|---|---|---|---|
| 1 | 耶誕城小檔 Ficha de Christmasland（`content12.py:190`） | P2 | 1899.0 → 1862.0 | +37.0px |
| 2 | 金馬小表 Ficha de los Golden Horse（`content34.py:76`） | P3 | 1902.0 → 1862.0 | +40.0px |
| 3 | 鋼雕閉幕行程 Último fin de semana（`content34.py:93`） | P3 | 1898.0 → 1862.0 | +36.0px |
| 4 | 爵士音樂節時間表 Fechas del jazz（`content56.py:110`） | P5 | 1869.2 → 1862.0 | +7.2px |

- **字形被裁：无。**交付印 PDF 200dpi 裁切（`crop-p2-straddle-2.png`、`crop-p3-straddle-gh-3.png`、`crop-p3-straddle-steel-3.png`、`crop-p5-straddle-5.png`）逐字目视：Christmasland / Horse / semana / jazz 末字母完整，墨迹落在空白纸面，无任何元素遮挡。
- **墨迹重叠：无。**occlusion 0 flags；CREAM-COVER 0；四处标题右侧均为页边空白（盒右缘 1862，页宽 1950），无后绘元素。
- **回归：无。**同一 PIL 扫描跑重扩散前备份旧版 SVG：旧版 5 处（上述 4 处坐标/超量完全相同，另有 P4 `deporte?` 一处）；新版 4 处——核心 fix5 修好了旧第 5 处，引入 0 处。净效果：修好 1 处，零新增。
- 裁决：记观察，非缺陷。缩短标题属设计决定，留待协调员定夺；本轮不改。

### 观察 2 — freeze diff `--strict-cjk` 字面 FAIL：新增 CJK 仅「西班牙」×9，全部在家具语名里

`freeze.py diff --core-svg core-zh-tw/svg --edition-svg es/svg --strict-cjk` 报 `STRICT-CJK FAIL`，新增 CJK 字符合计：西×9、班×9、牙×9（即“西班牙”×9）。

- 9 处逐一核实：全部位于家具字符串「西班牙語講解」——页脚 `Lucerna　繁體中文週報 VOL.4　繁體中文正文　西班牙語講解`（P1–P8，8 处）+ P1 badge 行（1 处）。无一处在正文。
- 逐页 CJK 账（`freeze-diff.json`）：P1 +2、P2–P8 各 +1，恰为家具出现次数；其余增删字符串逐页核对，全部是讲解层 EN→ES 一一对应替换（栏头、Notes、P8 答案注），中文正文零增删（例：P8 移除 `5. 封王 — Clinching the championship is 封王.` 对应新增 `5. 封王 — Conseguir el título es 封王.`）。
- 裁决：非缺陷。strict-CJK 工具的字面规则（“任何新增 CJK 即新目标语正文”）未考虑双语家具必须写读者语名——核心对应位置写的是「英語講解」，西语版本当写「西班牙語講解」，此为版本身份所需，非新增正文。建议后续：freeze.py strict-CJK 对家具语名白名单（或以正文区计），由协调员定。

### 观察 3 — 重扩散报告 §7 未决项 (1)：英文源 key「next Sunday」未改——本版无影响

本版实测：leak deny 命中 0；「next Sunday」/「Next Sunday」/「finish line」等英文源串 0 处；文字层「下週日」0 处、「本週日」11 处（印/网一致）；D1 西语值已为「este domingo」（P1–P3 Notas 及小檔均实测）。英文 key 的改动须先做核心 fix，属协调员决策，不构成本版缺陷。

## 全量重校实测记录（摘要；逐门数据见 GATE-LOG.md）

- **全文精读**：`2026-w47-zh-tw-es.text.md` 全文（52,246 B）逐行读过。西班牙讲解层：拼写、重音、性数配合、变位、标点均无误；Notas 与正文事实一致（时间、地点、数字逐项对过）；双语栏头一一对应（Vida/Cultura/Deporte/Juventud/Lectura a fondo/Lengua/Test y respuestas 等）。
- **日期星期全验**（`date -d`，America/Toronto）：2026-11-16 週一、11-22 週日、11-13 週五（耶誕城開城）、11-17 週二（迪士尼開幕/爵士第二週）、11-19 週四（城堡新演出）、11-21 週六（感謝祭/音樂會首場）、11-15 週日、11-24 週二、11-11 週三、11-06 週五、10-01 週四、10-23 週五、12-27 週日、2027-01-03 週日——与正文所写星期全部相符。
- **算术全验**：耶誕城 11/13→12/27 = 45 天；迪士尼 11/17→1/3 = 14+31+3 = 48 天；爵士第二週 11/17–22 = 6 天；影展 11/6–22 = 17 天；17:00→18:30 = 1.5 小时；14:00→19:00 = 5 小时；1200+800 = 2000，退 1200 实付 800；5 次×10 = 50，7 次 70 差 30 满 100；主燈秀 17:30–23:00 每半小時 = 12 場；P8 写作范文 142 字（120–180 带内）。
- **150 题答案逐项核对**：p8 extract 150/150，compare vs 核心 CLEAN（missing=[]、extra=[]、keydiff=[]）；P8 答案区 1–150 连续；填空键 54/54 出自正文；另人工抽验全部 150 条答案注与题面/正文一致（113–150 逐条读过，无错）。
- **注释孤儿扫**：P7 三组词表（遊行/封王/夜間/終點；入圍/頒獎/星光大道/鋼雕/保險箱/勞動記憶；小雪/節氣/燈秀/市集）+ P4 詞卡（遊行/感謝祭/集點/封王）+ 其余被注词（主燈秀/點收/鑑賞期/默片/鹽埕等），正文出现 2–70 次，0 孤儿；32 个 P8 填空键全部出自 P1–P7 正文，0 孤儿。
- **标题实测数：77 条**（“56 titles”是幻数，非本版数）。规则：逻辑标题 = 故事头条（32px/60px）+ 版头（46px）+ 栏头/级别头（25px/27px/bold 小头），折行合并计 1；排除家具（Lucerna 刊头、P1 36px 刊头行、第 N 版 kicker、頭條 kicker）、级别徽章、题号、图表标签、图注。分頁：P1 9、P2 11、P3 11、P4 9、P5 12、P6 8、P7 9、P8 8 = 77。
- **几何**：occlusion 0 flags（selftest 6 类 planted 全触发）；canonical creambox 36 盒、负内清除 0、P7 最小 12.5px；boxtitle 36 盒超框 0、最小右余 9.8px；PIL CREAM-COVER 0；spill 扫：3399 元素 0 出界（1950×2700）；P7 col3 1823.3 / teaser 2577.3（页脚规则 2596，余 18.7px）；P6 18:30/19:00 发丝缝 0.6px（渲染裁切目视有发丝间隔、无重叠，与核心先例完全一致）；P8 D-head `讀一讀，答一答 Lee y responde` 实测 242.8pt < 316.9pt 栏宽，无 de 版 HEAD TOO WIDE 问题。
- **§1.1**：纸 #fbfaf6 8 页各 1 处；金色/砖色类 fill 0；VOL.5 恰 1 处（P7 下期预告，正确）；VOL.4 10 处；徽章色 #5c6e30/#46581f/#37402f 齐全；页脚 `Página N de 8` 8/8；P8 最小字号 9.75pt（印/网一致，恰下限）；P1 顶部字号 [147.0, 45.0, 27.0, 24.0]。
- **文字层**：印/网 pdftotext -layout 字节相等（108,948），字符多重集差 0；ABSTRACT.txt 西班牙语单行、无 ASCII 双引号，含 VOL.4/A2–B2/150 ejercicios 与真实主题；KIT §1 三 SHA 与盘上一致（各 1 处命中）。
- **P1 顶部字号 / P4 bars [90.0, 450.0, 900.0] / P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]**：与期望完全一致。

## 证据文件（本 scratch）

- `gates/es-proof2/gates.json`（全部门禁汇总）、各门日志（`checks.log`、`occlusion*.log`、`p8-*.json`、`creambox.log`、`creambox-pil.log`、`boxtitle.log`、`fillin-check.log`、`freeze.log`、`freeze-diff.json`、`text-layer print.txt/web.txt`）
- `gates/old-es-check/creambox-pil-old.log`（旧版 STRADDLE 对照：5 处）
- `crop-p2-straddle-2.png`、`crop-p3-straddle-gh-3.png`、`crop-p3-straddle-steel-3.png`、`crop-p5-straddle-5.png`（交付 PDF 200dpi 裁切）
- `crop-p6-abutting-6.png`（P6 发丝缝裁切）、`contact-8pages.png`（8 页联络表）
- `rebuild/run.log`、`rebuild/render.log`、`snapshot-before.sha256`（重建前后 SHA）
- `orphan-spill-s11.log`、`orphan2.log`、`orphan3.log`（孤儿/溢出/§1.1 抽查）
