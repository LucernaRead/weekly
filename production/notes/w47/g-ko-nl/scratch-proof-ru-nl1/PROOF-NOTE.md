# PROOF-NOTE — 2026-W47 ru-nl（Russian × Dutch）独立复校 proof1

- 校对员：独立复校（proof1）
- 日期：2026-11-11
- 版目录：`production/2026-w47/2026-w47-ru-nl/`
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-nl1/`

## 结论：(b) 有缺陷，不能定稿

发现 **3 项缺陷**（D1–D3，均为 minor，无 major/critical）。其余全部复校项通过。
按 proofread-until-zero：修复并重渲染后须再做一整轮全量复校，直至零问题。

## 缺陷清单

### D1（minor）— P1「СЛОВО НЕДЕЛИ WOORD VAN DE WEEK」标题超出右版心
- 页码/定位：P1，右栏栏目头，基线 y=1660；run `x=1617.5 Noto Sans CJK SC 22 '　WOORD VAN DE WEEK'`。
- 归属：**本版（fan-out 讲解层）**。核心同位置为短中文 gloss `　本周单词`，不溢出；荷兰语 gloss 加长导致溢出。
- 实测证据：版心右边界 1862.0（P1 绿带 rect x=88 w=1774，横线 x1=88 x2=1862）。像素扫描：
  卡片 `p1-pervaya.png` 在 y 1643–1659、x 1863–1876 有 137 个深色像素，即末字母 K 的墨迹；
  墨迹最右 x=1876，超出右边界 **14 px**。2× 放大裁图 `p1-woord-header.png` 可见标题末 K 明显超出下方横线右端。
- 修复建议：缩短荷兰语 gloss（如 `WOORD V/D WEEK`）或缩小字号/左移，使墨迹右缘 ≤1862。

### D2（minor）— P2 练习 D 选项 b 行超出右版心
- 页码/定位：P2，练习 D「25–28 Koppel」选项 b，基线 y=2162：`b. Международный день студента`，
  末词 run `x=1764.7 Noto Serif 23 'студента'`。
- 归属：**核心（core-ru 预存）**。核心 `core-ru/svg/p2-zhizn.svg` 同基线 run 的 x/y/字体/文本与本版逐字节一致，
  同一溢出存在于核心；本版未引入，但渲染件中真实存在。
- 实测证据：像素扫描卡片 `p2-zhizn.png`：y 2149–2161、x 1863–1870 有 51 个深色像素；
  墨迹最右 x=1870，超出右边界 1862 **8 px**。2× 裁图 `p2-studenta-line.png`。
- 修复建议：在核心改行处理该选项行（如折行或缩字号），再重建全部 fan-out；本版单修会偏离核心版式，
  不建议只在本版改。

### D3（minor–moderate）— 网 PDF 丢失斜体（ru-en D3 同类，机制）
- 页码/定位：P1 本周词 `«чёрная пятница»`（SVG y=1712，`Noto Serif 21.5 italic` + `Newsreader italic`）。
- 归属：**机制（tools/webpdf.py）**。本版网 PDF 建于 2026-11-11 05:15 UTC，早于仓内修复提交
  `40963281`（2026-11-11 09:39 UTC，`tools: webpdf weight + italic face resolution (ru-en D3)`）。
- 实测证据：`pdffonts` 网 PDF 63 个字体中含 italic 的为 **0**；印 PDF 含 `Newsreader16pt-Italic` 与
  `NotoSerif-MediumItalic`。同坐标渲染并排对比 `italic-sidebyside.png`（上=网 PDF，下=印 PDF）：
  网 PDF 的 `«чёрная пятница»` 为直立体，印 PDF 为斜体。
  但文字层本身未坏（见下「三联症其余两腿」）：网 PDF 的 `«чёрная пятница»` 出现 10 次、0 次丢空格，
  闭引号贴合（`»,` 4 次，印/网一致）。
- 修复建议：用当前 `tools/webpdf.py` 重建网 PDF（内容与印 PDF 均不动），重建后复验 `pdffonts | grep -i italic`
  与并排渲染。

## 未决事项

- **O1（观察，非缺陷）**：P8 E 节两条模型翻译较自由：Q139 `Во вторник сборная России играет с Венесуэлой` →
  `Op dinsdag speelt Rusland tegen Venezuela`（`сборная` 省略，以 `Rusland` 替代）；Q140 `Поздравляю с Днём студента!` →
  `Fijne Studentendag allemaal!`（`allemaal` 为原文没有的添加）。两者均为可接受的荷兰语表达，
  不判缺陷；请定稿方确认是否收紧为直译（`Op dinsdag speelt de Russische nationale ploeg tegen Venezuela` /
  `Fijne Studentendag!`）。
- **O2（已裁定，非缺陷）**：P8 答案头右注 `Elk antwoord met een korte Nederlandse toelichting ✓ = modeltekst`
  墨迹最右 x=1864，仅超右边界 2 px（渲染抗锯齿量级），不处理。
- **O3（已裁定，非缺陷）**：P8 未渲染「Морозко」插图（构建条件：键表末行 y=2374.10，`img_y+250+90 > 2560` 时跳过，
  与 W46 ru-nl 相同）。键表完整到 Q150、无空缺、无悬空图注；`text.md` 末尾的图注行是与核心一致的导出器格式。
  插图缺失不影响内容与答案。

## 核实摘要（全文通读 + 逐题手验 + 机械门）

- **全文**：印 PDF 8 页卡片逐页目视全读 + `text.md` 203 块全文通读；日期/星期全部用日历核验
  （16 Mon、17 Tue、18 Wed、19 Thu、20 Fri、21 Sat、22 Sun、27 Fri、30 Mon、12 Thu 全部正确）；
  11 月工作日 20 天/休息日 10 天（含 11 月 4 日公众假期）正确。
- **150 题**：逐题手验，见 `keycheck-150.json`（150/150 pass）。印刷键由 `p8.py extract` 提取 150/150，
  与 `text.md` 答案节逐题比对 0 不符（Q150 为开放写作题，两种表述同义，已注明）。
  P4 结果表 8 场比分逐项核对，总进球 1+3+1+6+2+3+4+1=21，与「21 球」一致；积分榜（31/31/29/26/26、
  15 名降级区）与表一致。
- **外部事实**：第 14 轮 8 场比分已用公开来源独立核实——Forbes.ru（2026-11-09 综述）、sports.ru、
  rusfootball.info 三处一致（含 83 分钟扳平、90+1 制胜球、«Балтика» 20:45 开球、«Родина」为 2026/27 赛季俄超球队）。
  其余事实（学生日 17/11、Ded Moroz 生日 18/11、电影 19/11 五首映、母亲节 11/29 周日等）与正文内部一致。
- **金句**：P7 8 句全部出自本期正文，页码标注（1/1/2/3/4/5/6/6）逐个核对无误。
- **必查项**：(a) P1 标题横向溢出——D1 复现（另 D2 同类）；(b) 奶油框末行降部溢出——未复现
  （唯一 desc-clear −1.0px 的 P2「А ВЫ?」框经 PIL 真墨实测：末行无降部字母，墨底=基线 1153.98，框底 1159.0 上方 5.0px，
  y≥1154 框内 0 深色像素）；(c) P7 toolbox——实测通过（3 框，最小内 clearance +11.9，min desc-clear +5.9）；
  (d) text.md E 节 type 标签——4 处均为荷兰语 `[Vertaal naar het Nederlands]`，0 CJK 字符，无「翻譯」残留；
  (e) 网 PDF 斜体三联症——丢空格否、闭引号脱离否、斜体丢失**是**（D3）。
- **弯引号**：全版仅 1 对 U+201C/U+201D，在 P7 错误诊所 `«на “чёрной пятнице”»`，为任务注明的故意保留；
  U+2019 全版 0。
- **P8 最小字号**：PyMuPDF 实测印 PDF P8 最小 **9.75 pt**（393 个 span），等于 SOP §1.1 下限，不低于。
- **版式**：8 页，页脚 `Pagina N van 8` 齐全；摘要 ABSTRACT.txt 为荷兰语单行；无内部标签/周次/语言代码外露。

## 参考文件（scratch）
- `GATE-LOG.md`（全部机械门证据）、`keycheck-150.json`（150 题逐题手验）
- `occlusion.log/.json`、`creambox.log`、`p8-compare.log/.json`、`p8-extract.log/.json`、`freeze-diff.log/.json`、`freeze-base.log`
- 裁图：`adj/*.png`（occlusion 42 条像素裁定）、`p1-woord-header.png`、`p2-studenta-line.png`、
  `p2-ayvy-boxbottom.png`、`italic-sidebyside.png`、`p2-credit-zoom.png`
