# PROOF-NOTE — 2026-W47 ru-de（德语读者版）独立复校 proof2（re-fanout 重建版）

- **版**：`production/2026-w47/2026-w47-ru-de/`（目标语俄语 × 读者母语德语，VOL.4），re-fanout 从 core-ru fix1（`f11854bf`）全量重建
- **复校员**：独立 proof2；只读复校，生产文件未改动、未重建、未 commit、未 push
- **结论：(b) 有缺陷，不能定稿** — 缺陷 1 项（中），见下。#1 的 D2、D3 已修好，D1 原样未修。

## §0 身份核对（磁盘 vs 任务，全符）

| 文件 | 磁盘 SHA-256 | 字节数 | 与任务一致 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-de.pdf` | `26bfbcd169594a07595083f36f7306568eb4387f122ab6f94507c52141eadad2` | 21,231,822 | ✓ |
| 网 PDF `Lucerna-VOL4-ru-de-web.pdf` | `99173b8cacdde82a5d1147b54d61d254f16a59e9d8858f246c0acd3958bed4ee` | 3,385,962 | ✓ |
| text.md `2026-w47-ru-de.text.md` | `5ae444c8724da5b8d0c07874c3f4ce2ffc8a6a6f6dd8504ec3b00f49a732a911` | 63,516 | ✓ |

核心对照亦核实：core-ru 印 `d60fbd6c…cab81` / 31,429,147 B、网 `2f995f1d…4197` / 4,025,834 B、文 `348511e0…8cc` / 60,953 B，与任务一致，未变。探针（`git hash-object -w` + scratch 真实写）通过后开工。

## 缺陷清单

### D1 — P1 统计框标题溢出奶油盒（中；#1 D1 原样复现，重建未修）

- **位置**：P1 左中栏 `ТУР В ЦИФРАХ` 统计框，标题 `ТУР В ЦИФРАХ　Der Spieltag in Zahlen`，基线 y=1241，字号 23 粗体；源文件 `svg/p1-pervaya.svg`，`　Der Spieltag in Zahlen` 节点 x=727 y=1241
- **实测**：框 x=538.5、y=1203.7、宽 422.5（右缘 961.0）；PIL 真墨右缘 **997.6 px = 超出框右缘 +36.6 px**，并超出下一栏左缘（989）+8.6 px。核心同位置标题真墨右缘 864.6（余量 96.4 px，未溢出）
- **目视**：`crops/d1-p1-subtitle.png`（400 dpi）— 奶油盒右缘切过 “Zahlen”，词尾落在盒外白纸上
- **碰撞**：无（最近的其他文字在 x≥1461.5）
- **归属**：fan-out 构建（德语 gloss 加长所致；核心未溢出）。重建只改了 D1/D2/D6/kicker 节点（SVG 文本集 diff 见 GATE-LOG §13），该标题节点未动，故缺陷完整继承
- **修复**：缩短德语副标题（如只留 `Der Spieltag`）或换行/缩小标题字号；修后重跑 boxtitle 真墨实测

## #1 回归对照（与 backup-old 盘点）

- text.md 新旧 diff **恰 6 行对**（L173 D6 键、L187 D2 选项、L459/L504/L596 D1 标题、L694 D6 键表），别无其他。
- SVG 文本集 diff：p3/p4/p5 **完全相同**；p1 仅 kicker 双空格重排（20 节点），p2 仅 Q25 选项 b 缩短，p6 仅 D1 s1 + 免责声明俄语段，p7 仅 D1 s3，p8 仅 Q20 键 + D1 s4。无手 patch 丢失（de 的旧 map 本无仅存于 map 的手修；fr/it/nl/ja 的手修保留与 de 无关）。
- #1 D2（P2 匹配行 +9.2 px）**已修好**：Q25 选项 b 改为 `День студента`，`crops/d2-p2-matchline.png` 目视行尾距内容缘甚远；全版 PIL 横向扫描除 D1 外零溢出。
- #1 D3（网 PDF 丢斜体 + 闭引号脱离）**已修好**：网 PDF 斜体跨度 3 处 = 印 PDF 3 处（`«` Newsreader Italic、`чёрная пятница` NotoSerif-MediumItalic、`»`）；`пятница»` 印/网各 7 处、脱离式 `пятница »` 0 处；`crops/d3-p1-web-standfirst.png` 目视网版 `«чёрная пятница»` 为斜体、» 紧贴。
- KEEP/REVERT：重建报告所称 4 串 KEEP 全部落地（见下“核实摘要”），无 REVERT 项。

## 核实摘要

- **全文通读**：印 PDF 8 页逐页目视（`render/p1–p8-print.png`，150 dpi）+ text.md 全文通读；版式、图片（P1 照片、P2 尤恩《冬·罗斯托夫》、P4 1912 年国家队照片、P5 市场玉米照、P7 普希金肖像）、页脚 `Seite N von 8`、各页练习 A–H 均在位；无剪切、无重叠（除 D1 外）。
- **150 题逐题手核**（`gates/keycheck-150.json`）：编号 1–150 连续；P8 印出键与 text.md 答案键 **0 不符 / 149**（Q150 为开放写作题，印 ✓，范文 97 词，在 80–100 要求内，实数）；分级 A2 50 / B1 76 / B2 24；分面 Ankreuzen 55 / Ausfüllen 54 / Zuordnen 20 / Sätze bilden 12 / Umformen 4 / Übersetzen 4 / Schreiben 1；P1 10、P2 18、P3 18、P4 18、P5 18、P6 18、P7 12、P8 38。逐题对照题干/正文/表格核对；重点项——Q20 `желании`（`о своём ___` 后接前置格，#1 的 `желание` 已改正）；Q25 选项 b 现为 `День студента`；Q73 `14,4 млн заказов`（миллиона后接复数第二格，文中原句一致）；Q137–140 德语译文逐句核对无误；Q145–149 对话键 A/B/B/A/B 与购物对话语境一致。五组配对块逐组对照 SVG 选项原文核对无误（P2 D 25→b, 26→d, 27→c, 28→a；P3 C 39→b, 40→d, 41→c, 42→a；P4 C 57→b, 58→a, 59→c, 60→d；P5 C 75→d, 76→b, 77→a, 78→c；P8 F 141→c, 142→d, 143→a, 144→b）。
- **机械门**（全部自跑，不信重建报告；证据与命令见 GATE-LOG.md）：occlusion 42 TEXTX/0 LINEX，33 项像素裁决 CLEAR + 9 项 400 dpi 目视 CLEAR（`crops/flags-contact-sheet.png`，均为词与后随标点/引号分离字形）；creambox 全版扫描零框内负余量、95 BELOW-WINDOW 全为 +28…+37 的下一标题类；垂直溢出另扫：62 个节点全属同一 BELOW-WINDOW 类，框内墨底零违规、墨顶零违规；p8 compare CLEAN（150/150，keydiff [137–140]，与 core JSON 直接比对一致）；freeze **标准口径**（`--build` core-ru 构建目录、`--core-svg` core-ru svg）8/8 字节一致，核心完整性复核通过，edition-internal 基线 8/8 作补充；freeze diff 西里尔删除恰 15 项（Q46 `можно` + 14 个 Morozko 图注词）；印/网文字层 multiset 全等（逐页亦全等，31,009 字符）；P8 最小字号 9.75 pt；SVG 零真实 CJK（仅 U+3000）；`___` 字面 87 处（核心继承的模板缺口，依任务裁定不作本版缺陷）。
- **本版必查项**：D1（map 4 串）——text.md L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、L596 `Большой тест недели + все ответы`，免责声明仅 SVG（P6）、4 串全在 SVG ✓；Kicker 9 处双空格落地，PIL 间隙 [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]、最小 5.9 px ≥ 4 ✓；D2 Q25 `День студента`，全称 text.md 仍 ×2（与 core 一致）✓；D6 Q20 key `желании`，text.md ×2、P8 键 = core ✓。
- **D5 字体**：只记录不判定——印 PDF 65 个字体引用，含 Newsreader Italic + NotoSerif-MediumItalic；网 PDF 为 Lucerna 前缀同系字体，含 LucernaNewsreader-Italic + LucernaNotoSerif-Italic（见 GATE-LOG §14）。
- **判为非缺陷的项**：见 GATE-LOG §12（P2 降部候选真墨余量 +1.0 px；P8 无莫洛兹科图/注——与已发 W46 ru-de 同，为既定构建条件；窄字距为测量产物，400 dpi 已证实词间有空隙；P7 普希金肖像紧裁剪为核心继承；各页中栏留白为核心版式；P6 图表 38+26+18+18=100% 并标明为练习数据；Q100 键 “или” 语法可用）。

## 观察（非缺陷，记一笔）

- P6 右栏 `ЗА И ПРОТИВ PRO UND CONTRA` 标题贴近奶油盒右缘，但 PIL 真墨未出框（Part B 零报告），不作缺陷。
- P1 刊头 kicker 双空格重排后整行居中左移约 16 px，行首 586.3、真墨右缘约 1375，均在版心内。
