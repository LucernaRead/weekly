# FIX-LOG — W47 nl-ru fix2 (boxtitle right-overflow after fix-xru)

- 版次：2026-w47-nl-ru（俄语读者 × 荷兰语目标）
- 任务：修 sweep 发现的 4 处 boxtitle 右溢（回归 vs core）。只修这一版，不碰其他版；不 commit、不 push。
- 工作区：`hidden_files/w47/scratch-fix-nl-ru2/`（日志、门禁、快照全在此；生产源直接改，循 FIX-LOG-3 惯例）。
- 日期：2026-11-12 20:12–20:35 EST（2026-11-13 01:12–01:35 UTC）

## 0. 开工核对

- **三 SHA 与任务书一致**（开工实测，`pre-sha256.txt`）：
  - 印 PDF `De-Lucerna-VOL4-nl-ru.pdf` 12,260,999 B — `5541fc59de37cc5186b447e37f317f7f5dd628f862dd1b0701986c6d29e3e19e`
  - 网 PDF `De-Lucerna-VOL4-nl-ru-web.pdf` 1,674,515 B — `5df8b0d6af5b2b94ed9c55222e572df9c8b76fee907b24a07b037b9bbcb4d3b8`
  - 文 `2026-w47-nl-ru.text.md` 57,909 B — `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228`
- 扫查证据：`scratch-sweep-xru-occl-2/SWEEP-LOG.md` 全文已读（已抄 `SWEEP-LOG-ref.md`）；boxtitle 基线 JSON 已抄 `boxtitle-pre.json`（4 DEFECT）。
- 磁盘：开工 95G 已用（门限 100G，未触发）；收尾 95G。

## 1. 缺陷（4 处，全部右溢、无墨迹碰撞、无裁切）

| # | 位置 | 文本 | 溢出 | core 对照 | 墨右界 / 盒右界 |
|---|---|---|---|---|---|
| 1 | P1 [TITLE] | `ЦИФРАХ`（`DE WEEK IN CIJFERS　В ЦИФРАХ` 末词） | +1.5px | −7.8 | 962.5 / 961.0 |
| 2 | P2 [TITLE] | `ЗАПОМНИ`（`ZO ONTHOUD JE HET　ЗАПОМНИ` 末词） | +8.5px | −18.0 | 969.5 / 961.0 |
| 3 | P6 [TITLE] | `ДАННЫЕ`（`DE GRAFIEK　УЧЕБНЫЕ ДАННЫЕ` 末词） | +14.1px | −22.0 | 1876.1 / 1862.0 |
| 4 | P6 [BODY] | `?`（`VOOR OF TEGEN?　ЗА ИЛИ ПРОТИВ?` 末尾 `?`，实为该头条） | +9.7px | −22.0 | 1871.7 / 1862.0 |

第 4 处注：boxtitle 工具标为 BODY，但 y=785.0 与该头条基线（by6+42）一致、字号 21 与头条一致——溢出元实为 P6 pro/contra 盒头条末尾的 `?`（SVG 中 `?` 为独立 run，x=1840.8）。修法按头条降字号。

## 2. 修法（只降字号、不改措辞；循 nl 25→23pt 先例）

四处均为 fix-xru 后拉丁文改走较宽 Newsreader 致宽；措辞无须动。改前 `text_w` 实测（sans bold）：

| # | 源位置 | 改动 | 节省 | 需省 |
|---|---|---|---|---|
| 1 | `content12.py:43` P1 numbers-box | `f.box(..., tsize=22)`（23→22） | ~17.5px | 1.5px |
| 2 | `content12.py:179` P2 box | `f.box(..., tsize=22)`（23→22） | ~17.9px | 8.5px |
| 3 | `content56.py:148` P6 chart head | 24 → 22pt（23pt 只省 ~17px、余量仅 ~3px，取 22pt 求稳） | ~34.5px | 14.1px |
| 4 | `content56.py:168` P6 pro/contra head | 21 → 20pt | ~19.4px | 9.7px |

措辞零改动 → text.md 无须重导出（见 §4：SHA 不变）。

## 3. 重建

- `run.py` rc=0，TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE（`logs/run.log`）。
- `render.py` rc=0；印 PDF mtime 2026-11-13 01:20:53 UTC，12,261,013 B。
- `webpdf.py` rc=0；网 PDF mtime 2026-11-13 01:21:17 UTC，1,674,522 B（< 7 MB），55,036 text bytes。
- SVG 差异（vs `pre-svg.sha256`）：仅 p1、p2、p6 变；p3、p4、p5、p7、p8 逐字节相同。SVG 内四标题已是新字号（22/22/22/20）。

## 4. 修后实测

修后墨余量（重建 SVG runs 实测 + `text_w`）：P1 `ЦИФРАХ` ink_r 944.0，盒内 +17.0px；P2 `ЗАПОМНИ` ink_r 951.9，+9.1px；P6 `ДАННЫЕ` ink_r 1841.4，+20.6px；P6 `?` ink_r 1851.9，+10.1px。

## 5. 新旧 SHA 对照（盘上实测全值）

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `De-Lucerna-VOL4-nl-ru.pdf` | `5541fc59de37cc5186b447e37f317f7f5dd628f862dd1b0701986c6d29e3e19e` | `d4f081587c7d85e155734d4008d191e8b6f009f50738b3370f966c311053002e` | 12,260,999 → 12,261,013 |
| 网 PDF `De-Lucerna-VOL4-nl-ru-web.pdf` | `5df8b0d6af5b2b94ed9c55222e572df9c8b76fee907b24a07b037b9bbcb4d3b8` | `7a06f80d9238669ae1c8c1bfc848a2b814d9f0999e3e9f4c79b942dd17747dff` | 1,674,515 → 1,674,522 |
| 文 `2026-w47-nl-ru.text.md` | `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228` | `dd1c0c087c46f96afc0903c3bf534c7b281d97f3f1c1a6753a4e4813aad64228`（不变） | 57,909 → 57,909 |

## 6. 门禁（修后重跑，`gates/`，全部绿）

| 门禁 | 结果 |
|---|---|
| `tools/gates.py`（occlusion + p8 + freeze + 印/网文字层 + P8 字号/ chips + §1.1） | **ALL PASS**：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff=[137, 138]（读者语 key，预期）；freeze 8/8；印/网文字 posdiff 0 msdiff 0，8/8 页（tokens 799/805/725/726/783/734/887/2207）；pdftotext 印 = 网 = 55,036 B；P8 答题区最小 10.12pt；chips core=edition {A2: 8, B1: 24, B2: 3}；§1.1 clean |
| `boxtitle_check.py` | **0 DEFECT、0 OBSERVE、0 marginal**（34 titles / 483 body lines） |
| `occlusion_audit.py`（单跑） | **0 flags**，selftest OK |
| `spill_sweep.py` | **rc=0，0 SPILL**，110 OBSERVE（均为 ABOVE/BELOW 负距离近邻候选，非溢出；同代 es-ru 为 149，量级一致——相对 KIT 旧值 36 的上升源于 fix-xru 的 Newsreader 改道，早于本次修复） |
| `pdf_edge_scan.py`（印 PDF） | **0 TOUCH、0 NEAR**（8 页） |
| `head_check.py`（vs 本次 run.log） | **PASS 0 defects** |
| D5 census（`scratch-d5-plan/mechanism/d5_census.py`，本版） | **PASS**：D5 Latin 0、Cyrillic 0、curly-in-CJK 0、curly total 0 |
| 引号普查（`census_quotes.py`，本版 svg） | **GRAND TOTAL defective: 0** |

`d5_creambox_audit.py` 未单跑：其接口为 baseline-vs-patched 双目录 diff，本次无 patched 副本目录；creambox 类检查由 gates.py §1.1 + boxtitle + spill 覆盖（P6 chart head 修后墨余量 +20.6px，盒内）。

## 7. 收尾核对

- 触碰范围：仅 `production/2026-w47/2026-w47-nl-ru/`（`content12.py`、`content56.py`、SVG p1/p2/p6、印/网 PDF、WEEKLY-KIT.md §Files delivered + 新增 fix-nl-ru2 节）+ 本 scratch 目录；其余版、核心、SOP、lint 均未碰；未 commit、未 push。
- KIT 已更新：§Files delivered 新 SHA/字节数/pdftotext 55,036 B；末尾新增 `fix-nl-ru2` 节（修法、实测余量、新旧 SHA、门禁结果）；历史条目一字未动。
- 文字层：text.md SHA 不变；印/网文字层逐字一致（posdiff 0 msdiff 0）；四处措辞零改动——文字层只变了字号，无一字增减。
- 进程：单版串行构建，无需杀进程；未杀任何进程。
- 磁盘收尾 95G 已用（门限 100G，未触发）。
