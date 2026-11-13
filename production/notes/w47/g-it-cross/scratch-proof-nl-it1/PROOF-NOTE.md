# PROOF-NOTE — 2026-W47 · nl → it（意大利语读者版）· proof1 独立复校（delta build-6）

- 复校员：独立复校（proof1）
- 日期：2026-11-11
- 版目录：`production/2026-w47/2026-w47-nl-it/`（delta build-6）
- 核心：`production/2026-w47/core-nl/`（slug `2026-w47-nl-zh-cn`，已定稿）
- 对照：`production/2026-w47/fanout-nl/2026-w47-nl-it/`（build-5 re-fanout，staging）
- scratch：`hidden_files/w47/scratch-proof-nl-it1/`（本轮专用；上一轮 build-5 记录已移入 `prev-build5/`）
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；正典 creambox `hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与上一轮一致）
- TMPDIR 全程为本 scratch 的 `tmp/`（系统 /tmp 为 512M tmpfs，未使用）

## §0 身份核对（磁盘实测，开工与收尾两次一致）

| 文件 | 任务给定 SHA | 磁盘 SHA（开工） | 磁盘 SHA（收尾） | 字节数 | 结果 |
|---|---|---|---|---|---|
| 印 PDF `De-Lucerna-VOL4-nl-it.pdf` | `4d297162d9e9f2ac99896ab2cf41865af0588d0d060ad76b89b3a7dabe44da15` | 同左 | 同左 | 12,667,201 | 一致 |
| 网 PDF `De-Lucerna-VOL4-nl-it-web.pdf` | `15d1b6480e5d3456b527f8f5f2e70b0afd6fa7d90e0b17e9e5ea145ddfe410f6` | 同左 | 同左 | 1,610,237 | 一致 |
| text.md `2026-w47-nl-it.text.md` | `f1d9e3f58b82e1bc0f9f51c52a1c7e14ac8bb69c87dd60a3d54df44bb44b781b` | 同左 | 同左 | 47,060 | 一致 |

探针：`git hash-object -w /dev/null` 正常（`e69de29b…`）；scratch 探针文件写入成功。
生产零写入：开工/收工 44 文件快照 `prod-snapshot-before.txt` / `prod-snapshot-after.txt` diff 为空。
不 commit、不 push。全部构建/测量均在 scratch 重建副本里完成（`rebuild/2026-w47-nl-it/`，开工时 `cp -a` + `diff -r` 干净，三 SHA 与正本一致）。

## 结论：(a) 零缺陷，可定稿

150 题全部手验通过（0 不一致），全部机械门通过，delta D6–D11 逐项复核通过，
build-5 的三项旧缺陷（D1/D2/D3）已全部消除（见 §2）。未发现新缺陷。

## §1 Delta D6–D11 复核（全部自测，非照抄 delta 结论）

| 项 | 声称 | 本轮自测 | 结果 |
|---|---|---|---|
| D6 `w=419.4`（P3 bridge，sans 20.5） | 带 399.9–438.9 | 本版 `wrap()` 0.1px 扫描（200–500）：带 **399.9–439.0**（上沿差 0.1px 为网格取整），中点 419.4 在带内；2 行，末行 `agli ausiliari hebben/zijn.`，与交付 SVG 一致；拼接还原原文 | 通过 |
| D7 `w=432.7`（P7 gloss bridge，sans 20.5） | 带 415.5–449.9 | 扫描带 **415.5–449.9** 精确一致；3 行，末行 `scoren segnare.`；最宽实测行 415.5px < 栏宽 422.5，无溢出 | 通过 |
| D8 `capcn_w=377.7`（P6 图注，sans 18.5） | 带 367.4–388.0 | 扫描带 **367.4–388.0** 精确一致；4 行，末行 `(100 giovani)`；渲染图确认 `l'esercizio` 直引号紧密 | 通过 |
| D10 `dt_zh_w=388.7`（P7 读者来信，sans 20） | 带 343.7–433.7 | 扫描带 **343.7–433.7** 精确一致；2 行，末行 `esempio; promessa passata a VOL.5.` | 通过 |
| D9 两处同修（Q140） | 键 `Ik maak een surprise met een kort gedicht.` + 题干 `Faccio una surprise con una breve poesia.` | `content8.py:75` 键、`:76` 题干、text.md:415 三源逐字一致；text.md vs staging 的 diff **恰 415 行一处**（+11 B，47,049 → 47,060）；P8 题干与答案键渲染图确认（`img/crop-p8-q140-stem.png`、`crop-p8-q140-key.png`）；三方比对 keydiff 由 [137,138,140] 变为 [137,138] | 通过 |
| D11 顶留 62→89（P4 HET PROGRAMMA 盒） | 末基线 1209.49、盒底 1229.6、余量 +20.11px | SVG：盒 `y=591.6 h=638.0` → 底 1229.6，末基线 `18:45 uur.` 1209.49，余量 **+20.11px**；PIL 4× 真墨底 1209.74，余量 **+19.86px**；交付印 PDF 150dpi 渲染最低墨行 SVG y=1209.53，余量 **+20.07px**；盒底下 7px 条带 0 非纸像素；渲染图确认 `18:45 uur.` 在盒内、留白清晰。staging 同盒 `h=611.0`、底 1202.6，末基线在盒外 **−6.89px**（确为旧缺陷，已修） | 通过 |

D6/D7/D8/D10 在本版预先不存在是真实的：staging 的 p3/p6/p7 SVG 与本版字节一致，
断行即上述实测行，盒内余量实测干净（creambox §4），不是漏检。
SVG 变化范围：vs staging **仅 p4-sport.svg（D11）+ p8-toets.svg（D9）**，其余 6 页字节一致；
`diff -rq` staging vs 正本：差异文件恰为 text.md、两 PDF、WEEKLY-KIT.md、bslib4.py、
cards p4/p8、content34/56/7/8、svg p4/p8——与 delta 声称的改动清单一致，无其他文件被碰。

## §2 旧缺陷复核（build-5 proof1 的 D1/D2/D3）

### D1［major 已消除］P7 HET WOORD 框标题溢出
- build-5：标题 `HET WOORD　PAROLA DELLA SETTIMANA` 墨右缘 1927.9，超框右缘 +65.9px。
- build-6：标题已缩为 `HET WOORD　PAROLA`（re-fanout 时改，不在 delta D6–D11 内）。
  本轮 PIL 真墨：墨右缘 1715.1，余 **+146.9px**；交付印 PDF 150dpi 渲染：墨右缘 1715.1，
  余 **+146.9px**（PIL 与渲染一致到 0.6px）；渲染图确认标题完全在奶油盒内。
- 结论：消除。

### D2［minor 已消除］网 PDF 丢失全版唯一斜体
- build-5：网 PDF 字体表无 Italic，P1 `«de groepswinst»` 被打平成正体。
- build-6：机制已修（`git log tools/webpdf.py`：`40963281 tools: webpdf weight + italic face resolution (ru-en D3)`）。
  本轮实测：交付网 PDF 含 `LucernaNewsreader-Italic`（`YCNQPM+LucernaNewsreader-Italic`），
  P1 `«de groepswinst»` 在印/网两版均为 `Newsreader-Italic 16.12pt`；
  150dpi 渲染图上该词明显斜体。网 PDF 全 8 页 1 个斜体 span，与印版一致。
- 结论：消除。

### D3［minor 已消除］弯引号 U+2019 在 Noto Sans CJK SC 里渲染成全角空隙
- build-5：U+2019 共 4 处（P7 ×1、P8 ×3），与 39 处直引号混用。
- build-6：全版 `<text>` 统计 **U+2019 = 0、U+0027 = 44**（staging 亦为 0/44，即 re-fanout 时已改，
  不在 delta 内）；P7 `un'antica`、P8 头注 `l'esercizio`、Q140 注 `un'espressione` 均为直引号，
  放大渲染图确认紧密、无空隙。
- 结论：消除。

### O2［上一轮记录的纠正，非缺陷］
- build-5 记录称 P2 D 选项 c `c. eten voor het paard van Sinterklaas` 墨右缘 1872.9（超版心 +10.9px）。
- 本轮复核：盘上根本不存在该字符串；实际行为 `c. eten voor Sinterklaas' paard`（Newsreader 23pt，
  x=1473.5，y=2233），与核心逐字节一致。本轮 PIL 真墨右缘 **1790.0**、交付 PDF 渲染 **1793.8**，
  均在版心 1862 内，余 **+68~72px**。上一轮的 1872.9 数值无法复现（字符串引用亦有误），
  记为上一轮记录错误，本轮以实测为准。O2 不成立。

### O1［沿用，非缺陷］
- text.md 首行标题含周次码 `# De Lucerna · Settimanale olandese VOL.4 · 2026-W47`，
  与冻结核心及已发 W46 同式，属全版共用导出模板格式，非本版可单改（与 build-5 结论一致）。

### D5 字体问题［只记录，不作门、不修］
- 字体统计（`<text>` 元素计数）：Newsreader 969、Noto Sans CJK SC 643、Noto Serif CJK SC 25、
  UnifrakturMaguntia 1（刊头 `De Lucerna` 196pt）。
- 纯拉丁-on-CJK 段（本轮方法：CJK 字体 `<text>` 且内容仅拉丁字母/数字/标点/空格，含等级徽章）：
  各页 56/63/55/58/60/62/49/68，合计 **471**。方法口径与核心 re-proof 的 245 不同（其口径更窄、
  且核心读者语为中文），数值仅作记录，不作比较、不作门。

## §3 必查项逐项核实

- (a) P1 框标题/副标题横向溢出：**未复现**。副标题 `SETTIMANALE OLANDESE VOL.4 ORANJE SINTERKLAAS
  PAKJESAVOND` fits；日期行 `WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026` 在版心内；P1 整版目视干净。
- (b) P2/P5 右栏奶油盒末行降部漫出：**未复现**。PIL 真墨重测：P2 EN JIJ 末行 +5.34px、
  P5 EN JIJ +5.40px（均无降部字母）、P6 `(100 giovani)` +3.97px、P2 `po' ironica` +7.11px、
  P6 `En jij?` +9.75px——creambox.py 的 −0.4/−0.3 desc-clear 为 0.30em 一刀切余量的误报（见 GATE-LOG §2）。
- (c) P7 toolbox clearance：**通过**。正典 creambox.py：P7 三盒最小框内余量 +12.5px、
  最小降部余量 +6.5px（PAS OP! +20.4、HET WOORD +12.5、BRIEVEN +28.5）。
- (d) text.md 第 E 节 type 标签本地化：**通过**。E 节为 `Traduzione`／`Traduci in italiano`／
  `Traduci in olandese`；全版无中文「翻譯」残留（0 次）；其余 type 标签均为意大利语。
- (e) 网 PDF 斜体三联症：**未复现**。斜体已保留（见 §2 D2）；空格与闭引号完好
  （印/网文字层逐页 msdiff/posdiff 均为 0）。
- (f) ABSTRACT.txt 刊名：**通过**。意大利语单行，含 `Lucerna`、`VOL.4`、目标语 `olandese`、
  `150 esercizi`、`livelli A2–B2`；无 ASCII 双引号。

## §4 150 题手验摘要（详见 `gates/qa-table.txt`、`gates/registry.json`）

- 150/150 逐题手验：题面＋正文/图表/算术复算＋text.md 答案＋P8 印刷键三方比对，机械三方
  **149/150 MATCH**（唯一差异为 Q150 开放写作，见下），语义搭配逐题读过，**0 不一致**。
- Q73 类键-干错配检查：Q73 题干 `In vier regels schrijf ik een ___.` 配键 `gedicht`，语义贴合；
  全卷无键-干错配。配对题：P2 D（25–28）与 P8 F（141–144）的 a–d 选项内容已从 SVG 核对，
  字母映射正确（25–28 = d/c/a/b；141–144 = b/c/d/a）。
- 算术全对：83 题 35、84 题 30、85 题 65（35+30）、86 题 15、87 题 100（35+30+20+15）；
  22/45 题 19 天、43 题 1 天、44 题 4 小时、46 题 17 年。
- Daan 对话题 129–132（B/B/B/B）已与 P8 G 节对话原文核对：Rotterdam、周一看 Duitsland–Nederland、
  鞋里 wortel + verlanglijstje、每天 18:00 看 Sinterklaasjournaal。
- 翻译题 137–140：137 意大利语译句、138 意大利语译句、139 荷兰语句、140 D9 修复后
  `Ik maak een surprise met een kort gedicht.`——四句译文与原文逐词对应（breve↔kort、poesia↔gedicht）。
- Q150 开放写作：P8 印 `✓`，范文 81 词已数（`81 parole`，与 KIT 一致），属设计如此。
- P8 实测最小字号 **10.12pt**（SOP §1.1 底线 9.75pt，让步第 4 步范围内，与 KIT 一致）。

## §5 全文通读未发现的其他问题

- 8 页逐版看图（交付印 PDF 150dpi）：除已消除的旧缺陷外无溢出、重叠、压页脚、图片压字；
  页脚/页码行正确（第 N 版／共 8 版）；P3/P6 中部留白与核心版式一致（短文章所致），非缺陷。
- 荷兰语拼写/变位/性数：通读无误；过去时/完成时（hebben/zijn）选择正确；`omdat` 从句动词居末正确；
  `kwartfinales` 复数、`kandidaten` 复数正确；`Ozosnel`（Q21）与正文一致。
- 读者母语层：全部讲解/导读/图注/题干说明为意大利语；无他语导读残留；无内部标签/周次/语言代码
  进入正文版面。图片：6 图均有目标语图说＋出处（与 build-5 一致）。
- P7 金句 8 条逐字出自本期文章（P1/P2/P3/P4/P5/P6），意大利语译文与原文对应、页码标注正确；
  P7 下期预告（11 月 24 日欧冠 Real Madrid–PSV、Feyenoord–Porto；11 月 29 日 Feyenoord–Ajax；
  12 月 5 日 pakjesavond）与 P8 范文一致。

## 方法备注（非缺陷）

- **M1「56 标题」计数无法还原**：任务称盒标题扫描 56 个。本轮可还原的集合为：
  橄榄色奶油盒标题 **17** 个、奶油盒内含行 **25** 个（含 7 行 `Pag. n` 索引行与 `QUESTA SETTIMANA` 第二行）、
  粗体标题超集（Noto Sans CJK SC 粗体 ≥21pt）**85** 个——没有一种自然定义得到 56。
  本轮扫了超集 85 个（PIL 0 溢出/0 紧张）并对全部奶油盒标题做了交付 PDF 渲染复核（最紧 +32.3px），
  覆盖了 56 的任何可能子集；请协调员确认 56 的定义，以便下一轮对上。
- **M2**：delta 的 `spill_creambox.py` / `orphan_sweep.py` 所写 ED 路径
  （`~/workspace/weekly-git/hidden_files/w47/scratch-delta-nl-it/rebuild/...`）在当前克隆中不存在；
  本轮将其指向本 scratch 的重建副本（SVG/cards 与正本字节一致）后重跑，结果复现（0 spills、orphan 0）。
- **M3**：正典 creambox.py 当前接受 SVG 文件列表作参数（`creambox.py svg/*.svg`），
  build-5 GATE-LOG 所记 `--window 45` 与其现行 CLI 不符；本轮按现行 CLI 以 8 个 SVG 文件实跑。
- **M4**：`tools/freeze.py` 仅有 `baseline` / `diff` 子命令，无 `freeze_direct`（与 build-5 备注一致）；
  本轮按任务说明用 `baseline --core-svg` 指向核心 `svg/` 子目录，核心 8/8 + 本版自身 8/8。
- **M5**：`occlusion_audit.py --selftest` 是只跑自检（不审计目录）；本轮自检与正式审计分开跑，
  自检通过，正式审计 0 旗。occlusion 对纯填色奶油盒的框标题横向越框是盲区（BOXTITLE 只覆盖
  带描边或 `#2c2822` 填充的盒子），已用 PIL 真墨 + 交付 PDF 渲染像素另行验证（§4 门禁）。

## 证据索引

- `GATE-LOG.md`：门禁逐项实测值。
- `gates/`：`run.log`、`render.log`、`webpdf.log`、`freeze-core.log`、`freeze-self.log`、
  `occlusion.log`、`occlusion.json`、`p8-extract-ed.json`、`p8-compare.json`、`p8-compare.log`、
  `threeway.log`、`registry.json`、`textmd-qa.json`、`qa-table.txt`、`width-scan.log`、
  `d11-svg.log`、`d11-render.log`、`d11-rect.log`、`textlayer.log`、`creambox-all.log`、
  `creambox-trueink.log`、`spill.log`、`orphan.log`、`box-titles-enum.log`、`box-title-scan.log`、
  `box-title-render2.log`、`title-census.log`、`title-census2.log`、`style-d5.log`、
  `match-daan-q150.log`、`daan-q150-count.log`、`o2-recheck.log`、`p8-svg-textdiff.log`、
  `headings-scan.json`、`box-titles.json`。
- `img/`：交付印 PDF 150dpi 整版 `p1.png`–`p8.png` 及裁切 `crop-p4-programma.png`（D11）、
  `crop-p7-hetwoord.png`（D1）、`crop-p8-q140-stem.png`／`crop-p8-q140-key.png`（D9）、
  `crop-p3-d6b.png`／`crop-p7-d7b.png`／`crop-p6-d8b.png`／`crop-p7-d10b.png`（D6/D7/D8/D10）、
  `crop-p1-italicb.png`（D2）、`crop-p7-zinnen.png`（D3）。
- 本轮脚本：`width_scan.py`、`textlayer.py`、`threeway.py`、`box_titles_enum.py`、
  `box_title_scan.py`、`probe_d11.py`、`probe_d11_render.py`、`spill_creambox.py`、
  `orphan_sweep.py`（后两者为 delta 方法的复用，ED 已改指向本轮重建副本）。
