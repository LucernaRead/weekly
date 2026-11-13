# PROOF-NOTE — W47 ko-pt proof1 独立复校（ko fan-out #3 新版）

- **复校员：** proof1（独立，与 fan-out #3 构建者不同人），2026-11-11 UTC
- **对象：** `~/workspace/weekly-git/production/2026-w47/2026-w47-ko-pt/`（新版，无旧版可对比）
- **结论：(a) 定稿零缺陷。** 全部门禁独立重跑通过；150 题逐题三源手验 0 失败；8 页逐页渲染目视零问题。
- **未 commit、未 push。** 所有证据在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-pt/`（GATE-LOG.md 同目录）。

## 1. SHA 复核（开工前、复核后各测一次，全部一致）

| 文件 | 字节 | SHA-256 | 与任务简报 |
|---|---|---|---|
| 印 `Lucerna-VOL4-KO-PT.pdf` | 45,680,335 | `358303d15e17c8a2589f3edcad416368720a1f091a560b475180ade171131c74` | ✓ 一致 |
| 网 `Lucerna-VOL4-KO-PT-web.pdf` | 4,033,877（< 7 MB） | `9abb351ca17918574a0f143a4486a8aa9deaaf8ff6e99495ca793c68500ac6da` | ✓ 一致 |
| text `2026-w47-ko-pt.text.md` | 35,080（449 items） | `80cc61ef7bc993f8e3681a971009a72969a4a42b612a6bdca9e8a6216c868ca0` | ✓ 一致 |

核心 core-ko 复核前后未变：印 `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`、
text.md `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`（开工前/复核后两次测量相同）。
两 PDF 均为 8 页、1462.5 × 2025 pt。

## 2. 门禁汇总（全部通过）

| 门禁 | 结果 |
|---|---|
| run.py（freeze baseline 内重建，系统 python3） | exit 0，0 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38） |
| freeze baseline（系统 python3，Pillow 10.2.0） | **8/8 字节一致**（`freeze-baseline.log`）；venv 下 ABORT rc=2 为预期守卫行为（ko 豁免，见 §4） |
| freeze diff vs core-ko | 新增 CJK 7，全部为 U+3000（页脚分隔符），与 de 系拉丁版一致 |
| occlusion audit | **0 flags**（selftest 6 类全触发，干净对照静默） |
| p8.py extract | **150/150**，编号 1–150 连续 |
| p8.py compare vs core | **CLEAN**，missing=[]，extra=0，keydiff=[137, 138]（E 组重定向，W46 先例，按设计） |
| 印/网文字层（plain） | **逐字节一致**，各 51,790 B（`cmp` rc 0） |
| P8 最小字号（PyMuPDF，印 PDF） | **9.975 pt**（167 spans，162 在最小值），≥ 9.75 pt，通过 |
| boxtitle | **8/8 ≤ 386.5 px**（§3） |
| keycheck（REG vs P8 SVG，我自己的 extract） | **150/150**（149 exact + #150 `✓`，与核心相同） |
| census ex/match | 166 项，text.md 缺失 0；D6 缺失 0 |
| §1.1 grep audit | paper/VOL.4/`·`/颜色与核心逐页一致；hanzi 0；U+2019 0；P7 VOL.5 3→2 按设计（去掉 lko/lcn2 行） |
| check_core（scratch 副本，系统 python3） | rc=0；gloss fails 0；P7 短语 8/8 verbatim；orphan 0 |
| check_gloss（scratch 副本，系统 python3） | rc=0；gloss fails **0**（连贯跑法 ED=pt；见 §5 的 10-miss 调查） |
| textmd 重导出（scratch 副本，系统 python3） | **与交付件逐字节一致** |
| U+201C/U+201D/U+2019/U+2018 扫查 | 8 SVG + content py + text.md + ABSTRACT + 双 PDF 文字层，**全 0** |
| 孤标点 sweep | 单独标点 `<text>` 0 个；行首闭合标点候选 7 行，与核心**逐行相同**（坐标与文本一致，选项分隔符 `· B./· C.` 换行，按设计） |
| creambox 真墨复核 | cream rect 14 个，**全部内含文字**，空盒 0 |
| 150 题三源手验（`three-source.py`） | 题干（页 SVG + text.md）+ 键（P8 SVG）+ P8 注（P8 SVG）：**0 失败** |
| 目视 | 印 PDF 8 页 100 dpi 逐页全读 + 网 PDF P5/P8 对照：**零问题**，无豆腐块 |
| text.md 全文通读 | 全文读完，零问题（葡语讲解正确，韩文与核心事实一致，P7 frame 为「」） |

## 3. 本版 carry-forward：P5 box-title（#3 新版重点）

- P5 标题 `이번 주 청년 숫자　Números jovens`（`content56.py:21`，map 源头已缩短）实测 **368.6 px**，限 386.5 px，**余量 17.9 px**，单行 fit，P5 渲染目视确认。
- 全部 8 个 box-title 重测：349.8 / 236.7 / **371.1** / 317.4 / 368.6 / 286.8 / 265.0 / 343.5 px，**8/8 fit**。
  最小余量在 P3 `김장 장보기 목록　Lista de compras`：371.1 px，**余量 15.4 px**。无 over、无逼近项。

## 4. `Tudo` is_prose quirk（核实：仅分类器 quirk，无实质影响）

- 出处：`content12.py:101` 目录行 `("8면", "시험과 답", "Tudo")`——P1 目录第 8 面行的级别栏。
- 实测：P1 SVG 中出现 1 次（P1 渲染目视：目录 8면 行右端 "Tudo"，正常显示）；印 PDF 文字层 1 次；text.md 中 0 次。
- 定性：`textmd.py` 的 `is_prose` 把 4 字母裸拉丁词 "Tudo" 当作非正文剔除，与 ko-en `All`、ko-fr `Tout`、ko-it `Tutto`、ko-de `Alle`、ko-es `Todo`、ko-nl `Alles` 同类同因；text.md 449 vs 核心 452 的三项 drop（Tudo + lcn2 + lko 按设计）已逐项对账。**无内容缺失，不是缺陷。**

## 5. 调查记录（均已查清，不构成缺陷）

### (i) check_gloss 的 10 个 GLOSS-MISS——核心继承的检查工具 artifact
- 初跑（BUILD=pt 源码、ED=core-ko SVG 的混合跑法）报 gloss fails 10：조사하다、등재되다、아삭하다、하나가 되다、전하다（×2）、가벼워지다、피곤하다、졸리다、바뀌다。
- 对照实验 A：在 core-ko 自身原样跑未改动的 `check_gloss.py`，**同样报这 10 个 miss**（`gloss-miss-verify.txt`）——9 个不同词头在核心 SVG 当页都以跨 `<text>` 元素断行形式出现，检查的字符串包含逻辑看不见跨元素词。
- 对照实验 B：ED 与 BUILD 均指向 ko-pt 的连贯跑法，**gloss fails 0**（`check-gloss-pt/`）。
- 结论：10 miss 是检查工具对核心自身 SVG 的固有限制（换行断词），核心继承，非本版引入；本版连贯检查为 0。沿用 builder 的 0 结论。

### (ii) 印/网 `-layout` 文字层差 1 个空格——系统性 web 字体子集位移，非缺陷
- plain 文字层逐字节一致（51,790 B）。`-layout` 导出仅第 7 行刊头 "Lucerna" 缩进差 1 列（印 69 空格 / 网 70 空格）。
- 根因实测（PyMuPDF）：网 PDF 刊头 "Lucerna" x0=501.7422 vs 印 502.1719，**左移 0.43 pt（0.15 mm）**，系 fontTools 子集化 UnifrakturMaguntia 的字宽度量漂移；ko-en 的网 PDF 有**完全相同的 0.43 pt 位移**（x0 亦为 501.7422），只是未落在 pdftotext 分列阈值上故 layout 一致。de/it/fr/es layout 均为一致。
- 结论：内容、字形、肉眼位置均不受影响（刊头中心 731.42/730.99 pt vs 页中心 731.25 pt）；layout 1 空格是分列取整 artifact。**不判缺陷**，如实记录。

### (iii) “next Sunday”冻结规则——无适用对象
- `grep -rn "next Sunday"` 在 core-ko/*.py、ko-pt/*.py、`tools/tables.py` 中 **0 命中**。本版无适用对象，不套用旧行号。

### (iv) D5 字体——只记录数量（不判）
- SVG 与双 PDF 中**无 Noto Sans CJK SC**：`pdffonts` 仅见 NotoSansCJKkr / NotoSerifCJKkr / UnifrakturMaguntia（网版为 Lucerna* 子集重命名）。
- 拉丁字母 `<text>` 段数（SVG）：Noto Sans CJK KR **406**、Noto Serif CJK KR **345**、UnifrakturMaguntia 1；Noto Sans CJK SC **0**。仅记录。

### (v) 继承裁定（均在核心源码/记录中找到出处，非本版引入）
- #43/#123/#124 注 "previsão da Weatheri"：核心自有渲染（웨더아이，核心 run 4 已正名），见 `content34.py:107,121`、`content8.py:39`。
- #150 键印为 `✓`：核心 extract #150 同为 `✓`；"(tarefa livre — texto modelo abaixo)" 是题干非键。
- P8 #81 注换行（"Não há voos durante o teste / de audição"）：P8 渲染目视在栏内，compare CLEAN。
- P8 答案注题干 10.35 pt：核心已记录裁定。

## 6. 缺陷清单

**零缺陷。** 无 (b) 项。

## 7. 备注

- 旧版对比：ko-pt 为 fan-out #3 首版，无旧版，不适用逐页对比。
- 网 PDF SHA 每次渲染不同（fontTools 子集改写 + cairo CreationDate）已知；本次只在工作区 scratch 副本里重渲染验证，未动生产目录网 PDF。
- 探针：`/dev/null` 存在；`git hash-object` 通；goals 侧写盘通；全程无 EDQUOT。
