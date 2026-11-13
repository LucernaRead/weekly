# PROOF-NOTE — Lucerna Weekly 2026-W47 · ru-it · proof1（re-fanout 重建版）

- **版**：`production/2026-w47/2026-w47-ru-it/`（Russian target × Italian reader）
- **复校员**：独立子代理，会话 `f84a995f-048c-4872-943e-4da771dfdcde`（proof1，与重建者不同人）
- **日期**：2026-11-11
- ** scratch**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-it2/`（全部证据在此；生产目录零写入）
- **SOP**：仓库根 `SOP.md` 为准绳；KIT `WEEKLY-KIT.md` 仅作待核对的声称，不作证据。仓库 `AGENTS.md` 已读（内容仓规则：用 `tools/venv`、不改已提交版 frontmatter——本次只读校对，无任何修改）。

## §0 身份核对（三文件 SHA 与任务全符；核心对照亦全符）

| 文件 | 字节数 | SHA-256 | 与任务 |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-it.pdf` | 21,265,865 | `c69b7bdf3165ed24f05be8004559e0102c0c8e38f15e395bc32360094628359b` | ✓ 一致 |
| 网 PDF `Lucerna-VOL4-ru-it-web.pdf` | 3,384,095（< 7 MB） | `91028029155a32dab67c77d4fa0d69e6373ce790730f296cfd3a29d46ae60afd` | ✓ 一致 |
| text.md `2026-w47-ru-it.text.md` | 64,014 | `ac9636b971959d9f9c25e253aff6ff35f575512b5be70088240f365fb3ac10d1` | ✓ 一致 |
| 核心印 PDF `core-ru/Lucerna-VOL4.pdf` | 31,429,147 | `d60fbd6c…cab81` | ✓ 前缀一致 |
| 核心网 PDF `core-ru/Lucerna-VOL4-web.pdf` | 4,025,834 | `2f995f1d…4197` | ✓ 前缀一致 |
| 核心文 `core-ru/2026-w47-ru-core.text.md` | 60,953 | `348511e0…8cc` | ✓ 前缀一致 |

探针：`echo test | git hash-object -w --stdin`（仓内）→ `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；TMPDIR 全程指向本 scratch 的 `tmp/`。`git status`：生产目录仅为原样 untracked，无 tracked 修改。

## 结论：(a) 零缺陷，可定稿

**缺陷 0 项。** 首轮（proof1 #1）的 D1（网 PDF 斜体三联症）与 D2（P2 Q11b 选项越界）均已修好并实测复核；ru-de 同批 D1（P1 统计框标题溢出 +36.6）在本版**未复现**（标题真墨余量 +115.4 px）。其余全部机械门与 150 题手验通过。

## 缺陷清单

无。

## 重建修复复验（D1 / kicker / D2 / D6，全部落地）

| 项 | 实测 |
|---|---|
| D1（网 PDF 斜体） | 印/网斜体 span 各 **3 处**，位置逐字相同（`«` bbox x 1079.6–1088.0、`чёрная пятница` 1088.0–1222.8、`»` 1220.6–1229.3，印网完全一致）；网 span 文本为 `чёрная пятница`（**带空格**）；`»` 在印/网均紧贴（与斜体词尾重叠 2.2 pt，同形）；印/网 P1 斜体裁图 `crops/p1-italic-print.png` 与 `crops/p1-italic-web.png` **字节一致** |
| kicker 双空格 | 11 个 token，9 处 PIL 间隙 **[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]**，最小 **5.9 px ≥ 4** ✓ |
| D2（Q25） | P2 选项 b 现为 `День студента`，裁图 `crops/p2-q25b.png` 目视行尾距内容缘甚远；text.md 全称 `Международный день студента` ×2 = core ×2；短式 ×11 |
| D6（Q20） | 键 `желании`：text.md ×2（L173 题干键 + L694 答案键），P8 印出键 = core 键 ✓；`о своём ___` 后接前置格，语法正确 |
| D1 map 4 串 | s1 `УЧЕБНЫЕ ДАННЫЕ` 在 text.md L459 ✓；s3 `Три уровня, три темы` L504 ✓；s4 `Большой тест недели + все ответы` L596 ✓；s2（免责声明）不在 text.md ✓，在 P6 SVG ✓；4 串全在 SVG（p6 s1/s2、p7 s3、p8 s4）✓ |
| 首轮 D2（P2 Q11b 越界 +9.2） | 已消失：Part B 全版零报告，各页最大墨迹右缘 1862.0（仅页脚） |

## 必查项（ru-de 同批 D1）逐项结论

| 项 | 内容 | 结论 |
|---|---|---|
| (a) | P1 统计框标题真墨溢出（ru-de D1，+36.6） | **未复现**。标题 `ТУР В ЦИФРАХ　IN CIFRE`（y=1240.735，23 pt 粗体）真墨右缘 **845.6 px**，奶油盒右缘 961.0 → **余量 +115.4 px**；核心同位置 864.6（余量 +96.4）；右邻栏 x=989，空隙 143.4 px。与首轮值 845.6 **完全一致，无回归**。裁图 `crops/p1-statbox.png` 目视：标题稳在盒内 |
| (b) | P1 框标题 / 副标题横向溢出（一般） | **未复现**。Part B v2（最小包含奶油盒 + 内容缘 1862 / 页缘 1950）**零报告** |
| (c) | P3/P5 右栏 cream box 末行降部漫出框底 | **未复现**。spill 横扫 V-BOT=0、V-TOP=0（见下） |
| (d) | P7 toolbox clearance | **未复现**。creambox：3 框，框内最小余量 +11.9，降部最小 +5.9（与重建报告一致） |
| (e) | text.md 第 E 节 type 标签未本地化（中文「翻譯」残留） | **未复现**。E 节标签为意大利语（`Traduzione`、`[Traduci in italiano]`）；text.md 全文 **0 个 CJK 字符** |
| (f) | 网 PDF 斜体三联症 | **已修好**（见上表 D1 行） |

## 核实摘要

- **全文通读**：印 PDF 8 页卡片逐页目视（`render/p1–p8-print.png`，150 dpi）+ text.md 全文 838 行通读。内容无缺陷；P7 读者来信披露（俄文+意大利文双语，`Nessuna lettera né testo: esempio della redazione, promesso per VOL.5.`）目视核实；P8 完整至 Q150，无 «Морозко» 图（按设计，build 条件跳过，keys 止于第 3 栏 y=2303.5）。
- **150 题逐题手验**（`keycheck-150.json`，本轮 fresh 手验，非沿用首轮）：**149/150 正确，#150 为开放题**（按设计，印 `✓`，text.md 为开放题说明 + 97 词范文，实数 97，在 80–100 要求内）。印 P8 答案与 text.md 答案机械比对：**149/150 逐字一致，0 不符**。关键算术/事实：P4 赛果表 8 场进球和 0:1+1:2+1:0+4:2+2:0+2:1+2:2+0:1 = 1+3+1+6+2+3+4+1 = **21** ✓（SVG 原文重算）；Q52–60、Q64 逐行对表 ✓；Q25–28、Q39–42、Q57–60、Q75–78、Q141–144 五组配对逐组对照 SVG 选项原文 ✓；Q86/87（26/18）对图 ✓；图表 38/26/18/18=100% ✓；8 句金句各出现恰好两次 ✓（check_core GOLDEN: 8，BAD 0）；Q20 `желании`、Q73 `заказов`（14,4 млн后复数第二格）语法重核 ✓；Q137–140 意译逐句核对 ✓；Q145–149 对话键 A/B/B/A/B 与购物对话语境一致 ✓。
- **机械门**（详见 `GATE-LOG.md`）：run.py rc=0，TOTAL 150，0 溢出，重建 SVG 8/8 字节一致；freeze 标准核心口径 8/8、版内补充 8/8；freeze diff 西里尔删除恰 15 项（Q46 `можно` + 14 个 Morozko 图注词）；occlusion 42 TEXTX / 0 LINEX，42/42 CLEAR（33 像素 CLEAR + 9 项 6× 裁图目视 CLEAR）；creambox 框内负余量 0，BELOW-WINDOW 95 全为 +28…+37 下一标题类，vs 首轮备份 0 行 diff；垂直溢出横扫 V-BOT/V-TOP/V-PAGE-BOT 均为 0，62 个 BELOW 节点全为下一标题类；p8 compare CLEAN（150/150，keydiff [137, 138, 139, 140]）；印/网文字层 multiset 全等（总体 + 逐页 8/8，30,923 字符）；P8 最小字号实测 9.75 pt（正在 SOP §1.1 下限）；弯引号 « » 199/199 平衡，弯双引号仅 P7 一对故意保留的例外；可见文本无内部标签/周次/语言代码；SVG 零真实 CJK（仅 U+3000 ×123）；`___` 字面 87 处（核心继承的模板缺口，依任务裁定不作缺陷）。
- **D5 字体**（只记录，不判定）：印 PDF 73 个字体引用，含 Newsreader16pt-Italic + NotoSerif-MediumItalic；网 PDF 73 个引用，含 LucernaNewsreader-Italic + LucernaNotoSerif-Italic（见 GATE-LOG §14）。
- **外部事实**：text.md 与首轮已验版本相比仅差 12 行（6 对修复行，无事实行），故首轮外部核实（2026-11-11，browser.search，来源见首轮 GATE-LOG §11）继续覆盖全部事实主张：Ozon 11.11 2025 单日 14.4M+ 订单；黑五日期 WB 16–30 Nov、Ozon 13 Nov–2 Dec、11.11 22 Oct–12 Nov；黑五在俄自 2013 年；Hunger Games 俄上映 26 Nov 2026；«Рокки — это я» 与 «Бумажный тигр» 俄上映 19 Nov；«Увидеть всё» 为 A24、Fielder+Oppenheim 拍 Elizabeth Holmes 的纪录片；Simonyan 百年诞辰 2026 年 10 月 12 日；工作日核对（Europe/Moscow）与 11 月 20 工作日 + 10 非工作日；母亲节 11 月 29 日为 11 月最后一个周日。

## 观察（非缺陷，记一笔）

- **O1**：P2 `per Nonno Gelo.` 框底余量仅 **+0.52 px**（真墨迹底 1158.48 vs 奶油框底 1159.0；与首轮值及首轮备份值完全相同，无回归）。裁图 `crops/p2-nonnogelo-boxbottom.png` 目视：降部贴框边、未跨出。记为观察，非缺陷；边际过小，重建时如顺手可加 1–2 px 余量。
- **O2**：P2/P3/P5/P6 中栏大面积留白（文章短、练习起得低），核心版式继承，非缺陷。
- **O3**：Nota/词注行俄意词对窄词距（U+3000 分隔符所致，如 `поздравить fare gli auguri`、`От редакции Lucerna`），渲染目视词间有小空隙，与核心同形，非缺陷。
- **O4**：P8 无 «Морозко» 图/注——与已发 W46 ru-it 同，为既定构建条件（P8 空间不足跳过），非缺陷；freeze diff 的 14 个图注词删除与此一致。
- **O5**：P7 普希金肖像紧裁剪——与核心同一图像处理，非缺陷。
- **O6**：Q100 键 `или`（并列两句，语法可用）与 Q140 意译添 `a tutti`（问候自然扩展，与德语版 `Allen einen schönen Tag…!` 同式）——均已裁决可接受，非缺陷。
- **O7**：text.md `— СТРАНИЦА ? —` 分隔符亦见于 core-ru text.md（导出器格式，非缺陷）；P1 moth `<title>` 元数据内 `三色蛾` 为非可见文本（与 core 相同）。
