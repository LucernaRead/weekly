# GATE-LOG — 2026-W47 es-fr proof1（独立复校）

**对象 SHA（开工前 `sha256sum` 实测，与 brief 一致）**
- `La-Lucerna-VOL4-es-fr.pdf` 3,499,799 B — `c1c3ecdc326da7d91a4c55e8ad578e66d574db4436d6ec7a23164d653f54b168`，8 页
- `La-Lucerna-VOL4-es-fr-web.pdf` 846,204 B — `e6e5abbf4f923e4dfbae62777b1cea88f863e444d5be2e61892609005a245065`，8 页
- `2026-w47-es-fr.text.md` 45,272 B — `94476219c438fc47ba2613e45b7a266302540ec57ece4d39203400def46a4bc7`
- Web PDF 846,204 B < 7 MB ✓

**探针**
- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，成功（`probe.txt`）
- scratch 目录真实写文件成功；`TMPDIR=<scratch>/tmp`；/tmp 未写。磁盘 77G 可用。
- 复校中未改任何源文件：`git status --short -- production/2026-w47/2026-w47-es-fr/` 仅显示该目录为未入库新目录（`??`），无修改。

## 逐门结果

| 门 | 命令/方法 | 结果 |
|---|---|---|
| occlusion 审计 | `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-es-fr/svg` | **0 flags**；自检六类全触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1，clean 对照静默） |
| p8 extract | `tools/p8.py extract --p8 …/svg/p8-ejercicios.svg --total 150`（`p8-extract.json`） | **150/150**（parse: lines） |
| p8 compare | `tools/p8.py compare --core-p8 production/2026-w47/core-es/svg/p8-ejercicios.svg --edition-p8 … --total 150`（`p8-compare.json`） | **CLEAN**，missing=[] extra=0，keydiff=[137, 138]（翻译题按 W45/W46 裁定改以法语句为键；136/137/138/139/140 法译逐句核对正确） |
| freeze 渲染 | `tools/freeze.py baseline --build production/2026-w47/2026-w47-es-fr --core-svg …/svg --out <scratch>/freeze-es-fr-proof1` | **8/8** SVG 逐字节相同（实测 sha256 前 12 位：p1 cf8be0375430 / p2 79cda10bf00c / p3 859b7c191db0 / p4 d4d068ef068e / p5 f281a379e4f2 / p6 b9a8ec2fdaed / p7 2190c844e7d4 / p8 7cc5b110e731，生产件与 freeze 复现件一致）；核心 SVG 跑前后哈希不变 |
| freeze diff | `tools/freeze.py diff --core-svg core-es/svg --edition-svg …`（`freeze-diff.json`） | 各版增减字符串均为讲解层替换；新增 CJK 仅 1 字 U+3000（P1，全角空格，SOP §1.1 规定分隔符） |
| creambox.py 全版扫查 | 复制自 `hidden_files/w47/scratch-proof-de-es1/creambox.py`（de/es 各版同款脚本）到本 scratch，跑 8 版 SVG（`creambox-all.log`）＋逐盒诊断（`creambox-diag-p123.log`、`creambox-diag-p45678.log`）＋PIL 真实墨水测量 | **2 盒漫出（D1）**，其余 20 盒在内；6 处负 clearance 为误报（盒下标题/盒下注文，与核心同坐标一致） |
| keycheck（150 题逐题） | 全文通读 text.md：答案键逐题对照题面/原文/图表复核；配对组 25–28 / 52–55 / 141–144 逐字母核对 | **150/150 一致**（逐页：P1 1–10 ✓，P2 11–28 ✓，P3 29–46 ✓，P4 47–64 ✓，P5 65–82 ✓，P6 83–100 ✓，P7 101–112 ✓，P8 113–150 ✓） |
| P8 最小字号 | PyMuPDF 逐页 span 字号（印版与网版同值） | **P8 min 10.12pt**（KIT 称 10.125pt，方法差内一致），≥9.75pt 底线；其余页 min 11.62–12.75pt |
| boxtitle 宽度 | occlusion 审计 BOXTITLE 类（含框题墨迹 vs 自身框界；自检 BOXTITLE 触发） | **0 flags** |
| 印/网文字层同一 | `pdftotext`（无 -layout）印版 46,247 B＝网版 46,247 B；`-layout` 版各 108,606 B，`cmp` 逐字节一致（`print.txt` / `web.txt`） | **同一** |
| 8 页目视 | 印刷 PNG（`cards/`）全 8 页＋网页 P1/P8（`web-p1.png` / `web-p8.png`，110dpi 渲染） | 无溢出/重叠/压页脚/图文不符；P7 预告框底离页脚线有余量 |
| 金句 8/8 | 全文空白归一化计数 | 每句恰 2 次（原文＋P7 引文） |
| 范文词数 | P8 模型文本实数 | **97 词**，与版面标注一致 |
| 译注词 ≥2 | 各版 Note 词全文计数 | 全部 ≥2（见 PROOF-NOTE） |
| 弯引号/撇号 | SVG 文本字符计数 | « 56＝» 56；无直引号/弯双引号；撇号统一 ASCII |
| 禁词 0 | text.md grep | 「桥接」0；「12 de noviembre」0；VOL.4 ×9 / VOL.5 ×3（后者均为正当下期预告） |
| CJK | SVG `<text>` 字符清点 | 可见文本仅 U+3000（119 处）；唯一真 CJK 为 P1 虫标非渲染 `<title>Lucerna 三色蛾</title>`（与核心相同） |
| 日期星期 | `date`（Europe/Madrid） | 11-13 周五、11-16 周一、11-20 周五、11-22 周日、11-27 周五、11-29 周日，全部吻合 |
| 外部事实 | 现场检索（La Moncloa/RD 806/2026、UNESCO、LaLiga/DAZN、UEFA/Eurosport、JEC Acuerdo 342/2026、Sportradar 等） | 大选日历、弗拉门戈、联赛、欧冠、MiDNI 均证实；RTVE 具体分党数字仅核心 KIT 引文，未独立再核（记为限度） |

## creambox 详细数据（Newsreader 实测墨水底 vs 盒底）

| 页 | 盒 | 末行基线 | 盒底 | 墨水底 | 余量 |
|---|---|---|---|---|---|
| P1 | CINCO CLAVES (y=588) | 1266.0（盒内） | 1288.0 | — | 注文行 y=1300 在盒下 12px，**与核心同坐标**，设计如此，非溢出 |
| P2 | ¿SABÍAS QUE? (y=200, x=1440..1862) | 538.2 `ley.` | 543.5 | 543.45 | **+0.05px（贴边，未越）** O1 |
| P2 | ¿Y TÚ? (y=570) | 1044.2 | 1051.0 | 1044.70 | +6.30px ✓ |
| P3 | EL FLAMENCO, EN TRES DATOS (y=867) | 1266.5 `música.` | 1271.8 | 1266.75 | +5.05px ✓ |
| P3 | **¿Y TÚ? (y=1298)** | 1592.8 `deux phrases et envoie-les.` | 1594.8 | 1597.55 | **−2.75px（D1）** |
| P4 | ¿Y TÚ? (y=602) | 987.2 | 993.5 | 992.20 | +1.30px ✓ |
| P5 | VOTAR POR PRIMERA VEZ (y=939) | 1246.2 | 1251.5 | 1251.45 | **+0.05px（贴边，未越）** O1 |
| P5 | **¿Y TÚ? (y=1278)** | 1572.6 `deux phrases et envoie-les.` | 1574.5 | 1577.35 | **−2.85px（D1）** |
| P7 | ERRORES/LA PALABRA/CARTAS 三盒 | — | 1064.0 / 1376.0 / 1865.5 | — | 墨水余量 +42.5 / +26.5 / +0.95px ✓（P7 工具盒合格） |

## 结论

**(b) 缺陷清单：D1 一项（轻）**。其余门全绿。修 D1 后按 SOP §8.4 整期重渲染、从头再做一轮全量复校，零发现方可定稿。
