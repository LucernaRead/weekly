# FIX-LOG — 2026-W47 it-ru xru-regression fixes (occlusion 1 + boxtitle 4)

- 版：`2026-w47-it-ru`（意大利目标语 × 俄语读者版），VOL.4，8 版，150 题
- 修复员：fix-it-ru2；日期：2026-11-13（UTC 约 01:15–02:10）
- 依据：`scratch-sweep-xru-occl-1/SWEEP-LOG.md`（5 处新回归，core-it 对照全为负/0 flags）
- 范围：只修这一版。生产源 `content7.py`、`content12.py`、`content34.py` + 重建产物
  （svg p1/p2/p4/p7、cards p1/p2/p4/p7、两 PDF、text.md、WEEKLY-KIT §19）。
  未碰 core-it、其他版、tools/；未跑 insert.py / lint；无 commit、无 push。
- 工作区：本目录 `scratch-fix-it-ru2/`（`rebuild/` 为重建副本，生产 SVG 绝不被重建过程直接写；
  `rebuild.py` = F 轮 `rebuild_one.py` 的改编，指向本 scratch；`gates.sh`/`gates-prod.sh` 为
  F 轮 `gates_it.sh` 的改编；`TMPDIR` 全程指向本目录 `tmp/`）。

## 0. 修前核对（与任务书逐字节一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-RU.pdf`（印） | 13,644,353 | `97095d301dc1aa799e0a332fbea509394c14cecf041cd213fd178b55a07d25f8` |
| `La-Lucerna-VOL4-RU-web.pdf`（网） | 1,361,680 | `55368ada2028f6c812f0d14fc61f95af9b01a320bede61a35b133b3a7b82313d` |
| `2026-w47-it-ru.text.md`（文） | 67,681 | `298c2cd79bb89c588b4297ec76d75a0b498fa7d0c0ed76de2a30deda4210b0e6` |

修前 SVG 快照 `svg-before.sha256`；修前 text.md 存 `text-before.md`。

## 1. 5 处修法（实测先行，`measure/measure1.py` 用本版 svglib + `boxtitle_check.ink_bbox` 真墨复核）

| # | 缺陷（修前） | 修法 | 修后真墨余量 |
|---|---|---|---|
| 1 | Occlusion P7 [LINEX]：LETTERE disclosure 俄文 gloss 4 行，末行 'VOL.5.' 基线 1696.32，FRASI 分隔线 y=1686（宽 2px）横穿字形；LETTERE 盒底 1702.0 也压线 | `content7.py:100/:106`（公式行 + 渲染行，两处同改）删一词 «настоящее» → «Пример от редакции, а не письмо. Писем и лучших сочинений нет; обещание переносится на VOL.5.»（4→3 行；删 «лучших» 会弱化 VOL.5“最佳习作”承诺，删 «и лучших сочинений» 会丢该承诺，故删 «настоящее»——“Пример от редакции”已明示非真信） | 'VOL.5.' 基线 →1667.92，盒底 →1673.0；200dpi 像素复核：字墨最低 1671.8，分隔线顶 1684.8，净空 13.0px；'VOL.5.' 本身净空 17.3px；裁图 `pages/crop-vol5-final.png` 目视无穿字 |
| 2 | Boxtitle P1 'ЦИФРАХ' +31.8 | `content12.py:49` cifre 盒 `tsize 22 → 19.5`（20 只余 +1.6px 真墨，太薄；19.5 才够。措辞不动） | +11.3px |
| 3 | Boxtitle P1 '.' +4.8 | `content12.py:90` sommario 头 `24 → 23pt`（措辞不动） | +9.8px |
| 4 | Boxtitle P2 'ЗАПОМНИТЕ' +26.5 | `content12.py:179` frase 盒 `tsize 19.5 → 17.5`（措辞不动） | +10.5px |
| 5 | Boxtitle P4 'DOPO 11 GIORNATE' +18.1 | `content34.py:132` classifica 头 `21 → 19.5pt`（措辞不动；溢出段本身即拉丁文） | +13.1px |

字号削减循 nl 25→23pt 先例（2pt 档）；余量均为 PIL 真墨（与门禁同一算法），
非 advance 估算。接受的 HEAD TOO WIDE（P6 `LE PAROLE DELLA MANOVRA`）未动。

## 2. 重建（scratch 内两轮）

- 第 1 轮：tsize #2 取 20 → 重建成功，但真墨复核仅 +1.6px，判太薄，改 19.5 重建第 2 轮。
  第 2 轮即最终交付（`logs/rebuild-driver2.log`）。
- `rebuild.py`：run.py RC=0，TOTAL 150，0 FLOW OVERFLOW / 0 NOSPACE，
  HEAD TOO WIDE 仅接受的那 1 条；render.py RC=0；webpdf RC=0；
  text.md 导出 dry-run diff guard：恰改 1 行（861 行 disclosure），无增删行。
- SVG 差异 vs 修前：仅 p1/p2/p4/p7 变，p3/p5/p6/p8 byte-identical（`sha256sum -c svg-before.sha256`）。
- P7 col3 ends 1702.0 → 1673.0；其余流终值见 `logs/run.log`。

## 3. 新交付物（三件新 SHA，生产盘上已验）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-RU.pdf` | 13,644,359（+6） | `bca811b034701cbf232b5959d389d6028efe31e760f5fd9d35172444a59f50db` |
| `La-Lucerna-VOL4-RU-web.pdf` | 1,361,661（−19，< 7 MB） | `ce75a0349c3e62b0631a8beb2c8fa9366608cec4c69d66da56be31cd7b3838af` |
| `2026-w47-it-ru.text.md` | 67,662（−19，1317 行） | `28e906435b1f47dbb2f1b6238b49b9c91061a292e458d07cf63cd132cb8fe9f2` |

## 4. 全部门禁（重建版与生产拷回后各跑一次，均 ALL-GREEN）

| 门 | 要求 | 结果 |
|---|---|---|
| run.py | TOTAL 150，0 溢出 | TOTAL 150，0 FLOW OVERFLOW / 0 NOSPACE；HEAD TOO WIDE 仅接受的 1 条 |
| occlusion | 0 flags | 0 flags，selftest OK（重建 + 生产各一次） |
| p8 extract | 150/150 | 150/150 |
| p8 compare vs core-it | CLEAN | CLEAN，missing=[] extra=0，keydiff=[137, 138, 139]（预期） |
| D5 census | D5 0/0/0 | TOTAL D5 0/0/0，curly_total 0，CENSUS PASS |
| boxtitle | 0 DEFECT | 0 DEFECT，0 OBSERVE，0 marginal（34 titles，500 body lines；生产版 core_dir 正确指向 production core-it） |
| spill | 0 SPILL | 0 SPILL（29 boxes，170 candidates） |
| edge | 0 TOUCH / 0 NEAR | 0 TOUCH，0 NEAR（8 页） |
| 文本层 multiset | 印/网一致 | 44,253 字符各，multiset_diff=0，nonws_diff=0 |
| freeze diff vs core | 只许改动处变 | 仅 p7 变，恰为 disclosure 重排（'настоящее' 1× 删 + 标点/空格重切；CJK 增 0，Latin 总数 145=145）；p1–p6/p8 完全一致 |
| freeze baseline | 8/8 | 重建源另拷重跑 run.py，8/8 byte-identical |
| P7 专项 | 'VOL.5.' 与分隔线无穿字 | 200dpi 渲染像素复核 + 目视裁图（见 §1 #1）；生产 PDF p7 与 scratch 像素级一致 |

## 5. 拷回生产（仅改动文件）

- 源：`content7.py`（2× 同串）、`content12.py`（3 处）、`content34.py`（1 处）——
  直接在生产文件上 count-asserted 改动；`content56.py`/`content8.py`/`render.py` 与重建副本
  的差异仅 OUT/BASE 路径行，未拷回。
- 产物：svg p1/p2/p4/p7、cards p1/p2/p4/p7、两 PDF、text.md；生产 SHA 与重建 SHA 逐字节一致。
- `WEEKLY-KIT.md` 追加 §19。`translations.py`（fan-out 表）未同步——它与生产早已不同步
  （D5 'В ЦИФРАХ' 缩短亦未同步）；按本周期惯例以生产源为准，记于此供协调员定夺。

## 6. 本目录产物

- `FIX-LOG.md`（本文件）、`rebuild.py`、`gates.sh`、`gates-prod.sh`、`probe.txt`、
  `text-before.md`、`KIT-before.md`、`svg-before.sha256`、
  `logs/`（run/render/export/webpdf/rebuild-driver/gates/gates-prod/freeze-*）、
  `gates/` + `gates-prod/`（各门 JSON/日志）、`measure/`（候选宽度实测）、
  `pages/`（200dpi p7 渲染 + `crop-vol5-final.png`）、`rebuild/`（重建副本全套）、
  `freeze-repro*.sha256`（基线重跑记录；重跑用的 `freeze-repro/` 副本已删，凭据为日志 + SHA）。
