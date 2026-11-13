# GATE-LOG — W47 core-ru fix1 后独立复校（第二轮）

- 校对员：独立复校员；日期 2026-11-11；对象 `production/2026-w47/core-ru/`，fix1 commit `f11854bf`
- 工具链：`tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；系统 python3 未用
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-ru1/`
- 注：任务所称 `text.md` 在磁盘上即 `2026-w47-ru-core.text.md`（与 `2026-w47-ru-zh-cn.text.md` 字节一致）

## 身份核对（开工前 + 收尾重验，未变）

- 印 PDF `Lucerna-VOL4.pdf` 31,429,147 B，SHA-256 `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` ✓
- 网 PDF `Lucerna-VOL4-web.pdf` 4,025,834 B，SHA-256 `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` ✓
- text.md 60,953 B / 838 行，SHA-256 `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` ✓
- 探针：`/dev/null` 缺失 → `touch /dev/null` 垫回；`git hash-object -w --stdin` → `9daeafb9…` RC=0；goals 侧写文件成功

## 回归复测

| 项 | 方法 | 实测值 | 门限 | 结果 |
|---|---|---|---|---|
| D2 选项 b | 源码 `content12.py:276` | `День студента`；`:168`/`:238` 的 `Международный день студента` 未动 | — | ✓ |
| D2 选项 b | SVG advance（23px Noto Serif） | 右缘 1664.27，clearance +197.7px | +5px | ✓ |
| D2 选项 b | PIL 真墨（盘上卡片，thr<200） | b 右缘 1666，clearance **+196px**；a +181、c +69、d +34，0 溢出 | ≥+5px | ✓ |
| D6 Q20 键 | 源码 + JSON | `content12.py:257` `желании`；`ru-p8.json:177` `желании` | — | ✓ |
| D6 Q20 键 | 五方一致 | SVG P8（键 x=109.7 / 注 x=185.5）+ JSON + text.md:173 + text.md:694 + 印/网 PDF `20. желании — желание = 愿望` | — | ✓ |
| D6 keycheck | 自写 keycheck.py | 印/网各 **150/150**，0 真 mismatch | 150/150 | ✓ |
| kicker 词距 | 源码 `content12.py:18` | 9 处双空格 | 9 | ✓ |
| kicker 词距 | 方法一 PIL 墨框法（按 SVG font-family 取字） | **7.20 / 5.90 / 6.80 / 6.30 / 7.10 / 7.40 / 7.40 / 6.80 / 7.60**，最紧 5.90 | ≥4px | ✓ |
| kicker 词距 | 方法二 渲染列扫 y357–374 | thr<128 最小 5；thr<150 最小 4；thr<200 最小 3（仅 ГАЗЕТА/ДЛЯ，晕边口径，已披露） | ≥4px（实墨） | ✓ |
| kicker 影响面 | `cmp` + `<text>` diff | P2 与修前字节一致；P1 971 个 `<text>` 恰 20 个不同（全在 y=372 行），非 `<text>` 完全一致 | — | ✓ |

## 机械门

| 门 | 命令 / 依据 | 结果 |
|---|---|---|
| freeze baseline | `tools/freeze.py baseline --build …/core-ru --core-svg …/svg` | **8/8 字节一致**；core 完整性重哈希无改动 |
| run.py | scratch 副本重跑 | RC=0；0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150；A2 50 / B1 76 / B2 24；范文 97 词；重跑后 SVG 不变 |
| render.py | scratch 副本重建 | 重建印 PDF SHA 与磁盘一致 `d60fbd6c…` |
| webpdf.py | scratch 副本重建 | 4,025,864 B；文字层 56,024 B 与磁盘印/网版一致 |
| ru_textmd.py | scratch 副本重导出 | 与磁盘 text.md **字节一致**（60,953 B / 150 题 / 277 块 / 838 行） |
| check_core.py | `check_core.py .` | golden BAD **0**、gloss 失败 **0**、P8 字符 8191、孤儿行首 5（已裁决标点）、碰撞 1（P1 y1712 `чёрная`，已知） |
| occlusion | `occlusion_audit.py --selftest` + `svg --json` + 自写 `adjudicate.py` | 自检 OK；**42 TEXTX、0 其他类**；像素裁决 **42/42 CLEAR** |
| creambox | 正典 `hidden_files/w47/tools/creambox.py` | **32 框，0 真溢出**；below-window 全 +28…+44；desc-clear -1.6 像素复核为 +3px 在盒内（假阳性） |
| p8 extract | `p8.py extract --total 150` | **150/150** |
| p8 compare | `p8.py compare --core-dir . --edition-dir . --total 150` | **CLEAN**，keydiff=[] |
| 印/网文字层 | `pdftotext` + `cmp` | 各 56,024 B，**字节一致**；重建网 PDF 文字层亦一致 |
| P8 最小字号 | PyMuPDF 印版第 8 页 | **9.75pt**（恰达 §1.1 下限） |

## 全量复校

- text.md 838 行全文精读；150 题逐题手验：**全部键正确**，无错键
- text.md vs 修前导出：恰好 3 行 diff（173 / 187 / 694），与 fix1 所称一致
- 8 版逐版目视（自渲染 96 dpi）：无重叠 / 溢出 / 新缺陷；proof1 D-1 已在渲染件中修正（P4 a. `победил ЦСКА 4:2`；`играет с ЦСКА` 全版 0 处）
- proof1 §1.1 (b)(c)(d)(a)(e) 模板级项：状态未变（87 处 `___`；INK `#302c28`；Newsreader+Noto Serif 混排；无首字下沉；`·` 分隔 115 处）
- 范围外（按任务）：D1 fan-out 机制问题、D3 旧网 PDF 斜体——未列缺陷；D3 实测现状：当前网 PDF 内嵌 Italic 字体、文字层与印版一致
- ru-en 原定稿已因 D2 作废，须另派重校

## 结论

**(a) 零问题，可定稿。**（承接裁定：proof1 模板级项维持原裁决，不阻塞本版定稿。）
