# PROOF-NOTE — 2026-W47 it-nl 独立复校（proof2，全量重校）

**结论：(a) 零缺陷可定稿。** 本轮全量复校零问题；全部 20 项机械门禁独立重跑全绿，150 题三源逐题一致，8 页逐页目视干净，事实逐项经公开来源核实。

- 版：`2026-w47-it-nl`（目标语 it 意大利语 × 荷兰语读者，VOL.4，重扩散新版，核心 it 已定稿）
- 印 PDF：14,034,409 B，SHA-256 `2091448cb9155812311ae298e0c2f349d0b2d83ac6fa94f26f79f10b4c4c5a7f`
- 网 PDF：1,291,738 B，SHA-256 `039ee0bb9cc55f4faeceba85d5e11752abbb6fd2843de2e082c9c4cdf2b88b8f`
- text.md：55,509 B，1,317 行，SHA-256 `0a044d4b87da3cf281a18dad08cecef6d2842a99f4cb44da36276e35f902f4dd`
- 三 SHA 与任务值逐字节一致（开工盘核通过）；收尾复核三 SHA 仍一致，生产区未改动（`git status` 无 `M` 项；版目录为 untracked 既有状态）。
- 复校员工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof2-it-nl1/`；门禁详见同目录 `GATE-LOG.md` 及 `logs/`。

## 1. 开工探针与 SHA 盘核

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29b…`，RC=0；scratch 真实写文件通过；TMPDIR 全程指向自有 scratch 下 `tmp/`，未用系统 /tmp（除一次误写 45KB 至 /tmp/x，已删除）。
- 三 SHA + 三字节数与任务值逐字节一致后才开工。

## 2. 门禁汇总（独立重跑，详见 GATE-LOG.md）

20/20 PASS，RC=0（`logs/gates-proof2.log`；gates 逻辑复刻自 re-fanout `gates.py`，输出写进本 scratch，结论为本次实测）：

| 门 | 实测 |
|---|---|
| occlusion 几何遮挡审计 | 0 flags（工具先过合成阳性对照自检） |
| p8 extract | 150/150 |
| p8 compare vs core-it | CLEAN，keydiff **[137, 138, 139]**（见 §5） |
| freeze diff P1–P7 | 0 未解释片段（added/removed 皆由 translations.py 值/键、NOTE/gloss 复合、"(Pagina N)" 复合或家具解释） |
| freeze strict-cjk | 仅 U+3000 ×8（SOP §1.1 家具分隔符，豁免），其余新增 CJK 为 0 |
| 印/网文字层 | 词多重集一致，7,888 词；逐页比对 8/8：字符与词数逐页全等（见 §7） |
| 网 PDF < 7MB | 1,291,738 B |
| 印 PDF | 14,034,409 B，8 页，1462.5×2025 pt |
| P8 最小字号 | SVG 最小 13.0 px；PyMuPDF 实测印 PDF P8 最小 **9.75 pt**（SOP §1.1 下限，网 PDF 同为 9.75 pt） |
| §1.1 | 纸色 #fbfaf6；无金/红褐/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（下期预告头、LETTERE 披露、P2 交叉引用）；徽章色 A2/B1/B2 齐；全页 rect 0（无双线外框）；字体 Newsreader 963 节点 / Noto Sans CJK SC 643 / Noto Serif CJK SC 37（仅 U+3000 分隔）/ UnifrakturMaguntia 1 |
| text.md validate | forward-miss 0 / reverse-miss 0 |
| 150-key audit vs core text.md | 150/150（137–139 重定向、写作题除外）；notes 与 translations.py 一致（137–140 + 写作题除外），table_gaps 0 |
| run.py | RC=0，TOTAL 150，A2 47 / B1 70 / B2 33，页分布 10/18/18/18/18/18/12/38，范文 99 词，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE（`logs/run-rebuild.log`） |

## 3. 复现（重建 SVG 8/8 与重渲印 PDF 逐字节相同）

- `freeze.py baseline`（核心版，`--core-svg` 指核心 `core-it/svg`，build-copy 核实确为核心版——含核心 `2026-w47-it-zh-cn.text.md` 与核心 PDF）：**8/8 字节一致**，RC=0（`logs/freeze-baseline-core.log`）。
- 同一工具以版目录 `--build`、核心 svg 为比对目标跑出 0/8 是预期的人为错配（版 ≠ 核心），不作门禁结论；该次运行产出的 8 个版 SVG 与交付版 SVG 逐字节比较 **8/8 MATCH**（`logs/freeze-baseline.log` 产出，逐项核对）。
- run.py 在版 build-copy 内重跑（OUT 已重定向至 scratch，生产 SVG 未动）：RC=0，SVG 8/8 与交付一致；随后 render.py 重渲印 PDF：**14,034,409 B，SHA-256 与交付完全一致**（`logs/render-rebuild.log`）。
- webpdf.py 重建网 PDF：1,291,734 B（交付 1,291,738 B，相差 4 B），SHA 不同。分解证实非内容差异：文字层 `pdftotext` 逐字节一致（45,938 text bytes）；19 个子集字体解压后 Length1 相同、cmap 码点集与字形数 13/13 已比对者全等（其余 6 个为无 cmap 的符号字体，两版结构相同）；差异仅为 fontTools 子集字体的字节序不确定性（疑似 PYTHONHASHSEED 相关字形排序）。内容等价，记观察（§9-1），不计缺陷。任务的逐字节要求针对印 PDF，已通过。

## 4. 全文通读（1317 行）与 150 题手验

- text.md 1–1317 行逐行读完；登记（run.py REGISTRY）vs text.md 题面 vs P8 印出键三源逐题核对：编号 1–150 连续无缺重；每题题型/级别/键/注三源一致；Q137–139、Q140 见 §5。
- 算术逐项重算：MD11 10 场进球 3+1+2+3+3+2+3+1+2+4 = **24** ✓（"ventiquattro gol in dieci partite"）；Q85 13−11=**2** ✓；Q86 6+7=**13** ✓；P6 例图 Torino 5° < Milano 6° < Bologna 7° < Roma 11° < Napoli 13°，柱长单调 ✓；Torrone 11月7–22日 = 16 天、3 个周末 ✓；TFF 11月24日–12月2日 = 9 天 ✓；范文实测 **99 词** ✓（80–100 词要求）；Q58 "più bella"、Q59 "meglio"、Q93–96/109–111 虚拟式（piova/nevichi/controllino/sia/leggano）、Q77 "ci sarà"、Q108 "è finita" 等语法键全对。
- 日期/星期（`date -d`，Europe/Rome）：11月16日周一、17日周二、19日周四、20日周五、21日周六、22日周日、23日周一、24日周二、29日周日、12月2日周三、12月6日周日、12月31日周四——文中全部星期表述一致（含 "martedì 17"、"giovedì 12"、"sabato 21"、"domenica 22"、"lunedì 23"）。
- 8 金句逐字核对出处：8/8 在 text.md 中恰好各出现 2 次（正文一次 + P7 FRASI 一次），页码标注与实际页一致（P1/P1/P2/P3/P4/P5/P6/P6）。
- 荷兰语层：全文讲解为荷兰语，未见他语残留；"Translate" 0 次；"aantonende wijs" 为荷兰语直陈式标准术语，非错字；ERRORI TIPICI 四条纠正全对。

## 5. keydiff 与 re-fanout 未决项裁决（实测为准）

- **keydiff [137, 138, 139]**：实测与任务预期一致。P8 印出键：137/138/139 为荷兰语句子（"Voor de Madonna della Salute steken mensen de geloftebrug over." / "Zondagavond speelt Atalanta tegen Inter." / "Zaterdag speelt Lazio thuis tegen Lecce."），与核心（中文读者句）不同是**正确行为**——E 节 137–139 为"译成读者语"题，键随读者语重定向；Q140 的键在核心与本版都是意大利语 "Ogni cifra deve essere chiara."，无差异是正确行为，不是遗漏（Q140 为"译成意大利语"题，源句为荷兰语）。
- **"英文源 key 未改"**：本版无任何英文源键——"Translate" 全版 0 次，E 节标签为 `Vertalen`（`content8.py:69/71/73/75`，text.md L969/971/973/975），无未改的英文键。裁决：无此问题。
- **"双语小文件标题 STRADDLE"**（双语奶油盒标题越右缘）：独立实测——见 §6。裁决：无越缘，全部 29 盒最紧处仍余 4.8 px。
- **P8 `VUL DE KRONIEK IN` 类扫描**：本版 P8 无此标题；A 节标题为意大利语 "COMPLETA LA CRONACA"，无荷兰语长标题；P8 各节标题均经 EDGE/FOOTER 门禁（0 flags）且目视干净。裁决：该类情形在本版不存在。

## 6. 奶油盒标题（it-en 逃逸类）独立光栅实测

- 背景：canonical `occlusion_audit.py` 的 BOXTITLE 类只覆盖**有 stroke 边框**的 rect（或 #2c2822 填充）；`bslib4.box()/gloss()` 的奶油盒（fill #f0eee5，**无边框**）不在其检查范围内——这正是 it-en P1 +155px / P2 +39px / P7 +6px 逃逸的机制。本次用审计同款 PIL 真墨盒（`measure_cream.py`，`logs/cream-measure.log`）对全部 29 个奶油盒逐盒实测（标题行 + 盒内全部行，按基线分组聚合拆分 run）：
  - **29/29 盒全部在内，无一越右缘**（overhang > +0.5 px 者 0 个）。
  - 最紧前三：P1 LA SETTIMANA 盒内行墨右缘 1857.2 vs 盒右 1862.0（余 **4.8 px**）；P7 "LA PAROLA　WOORD VAN DE WEEK" 标题墨右缘 1853.5 vs 盒右 1862.0（余 **8.5 px**）；P1 "LA SETTIMANA IN CIFRE　CIJFERS" 标题余 23.0 px。全部标题均在内。
  - 渲染像素交叉核对（`crops/`）：P7 LA PAROLA 盒、P1 LA SETTIMANA 盒、P1 cifre 盒裁图目视——标题完整在盒内，右缘有可见余白；无字形被裁、无墨迹重叠他物、无可见边框被压。
- 刊头带独立实测：P1 刊头带 5 段墨左 10.5、右 1873.7（页宽 1950），左余 10.5 px、右余 76.3 px，spacing 11.0 修复在位（`content12.py:18`），无剪裁；渲染裁图 `crops/p1-masthead.png` 目视完整。

## 7. 印/网逐页比对与 8 页目视

- 印/网文字层逐页比对（pdftotext -layout，字符多重集 + 词多重集）：P1–P8 8/8 全等（词数 863/905/761/796/740/863/750/2210，合计 7,888）。
- 8 页全页渲染（`render/p1–p8.png`，由交付 SVG 直渲）逐页目视：无溢出、无重叠、无压页脚、无豆腐块、无图片缺失；页脚 "Pagina N van 8"（N=1–8）与 "La Lucerna　ITALIAANS WEEKBLAD VOL.4　TEKSTEN IN HET ITALIAANS　UITLEG IN HET NEDERLANDS" 逐页在位；目录页码（P1 IN QUESTO NUMERO）与实际版次一致；P3/P5 中部结构空白为核心既有版式（KIT 已载，非缺陷）；P8 练习区末行 y=870、答案区末行 y=2529（底边 2552，余 23 px），各流末位置均在底边内，无页界 spill、无孤儿行。
- 标题数（实测定义，不用幻数 "56"）：≥30 px 标题角色文本节点共 **37** 个；标题字符串出现 **27** 次；去重后不同标题字符串 **20** 个（版头 7：VITA/CULTURA/SPORT/GIOVANI/APPROFONDIMENTO/LINGUA/VALUTAZIONE；刊名 La Lucerna 1；刊头带 5 段；头条横幅 "LA LAZIO RESTA PRIMA!" 1；文章标题 6）。"56 titles" 在本版无对应实测数，不采用。

## 8. 事实核实（公开来源，2026-11-11 检索）

- **意甲 MD11（11月6–8日）**：10 场比分与积分榜与 askanews 通稿及多家报道逐项一致（Venezia–Udinese 2–1；Cagliari–Frosinone 1–0；Torino–Lecce 1–1；Parma–Bologna 1–2；Roma–Sassuolo 3–0；Napoli–Lazio 1–1；Genoa–Milan 1–2；Monza–Atalanta 0–1；Inter–Como 2–0；Fiorentina–Juventus 2–2；Lazio 29 / Inter 28 / Roma 27 / Milan 24 / Como 23 / Fiorentina 9 / Udinese 5；罗马最佳攻击 31 球；MD12：Atalanta–Inter 周日 22 日 20:45，Monza–Fiorentina 周一 23 日 20:45，Lazio–Lecce 周六 21 日 15:00）。Gattuso 为拉齐奥主帅（2026–27 赛季，接替 Sarri；拉齐奥 11 轮不败）亦经核实。
- **Eurochocolate 2026**：第 32 届、11月13–22日、主题 "Fate Dolci"、Calabria 为 Regione Ospite——官方 Press Area 及多家来源一致。
- **Festa del Torrone 2026**：第 29 届、11月7–22日、16 天、3 个周末、主题 «Il Confine»；Torrone d'Oro 授予 Davide Simonetta（生于 Cremona），周日 22 日 11:00 Palatorrone；历史游行 16:00（150+  figuranti）、Sforza–Visconti 婚礼重演 17:00、旗手与火舞至 18:00——与文中时刻逐项一致。
- **BookCity Milano 2026**：第 15 届、11月23–29日、主题 «Il senno sulla Luna»（Ariosto《Orlando furioso》）、1,360 活动 / 2,487 主角 / 1,164 书 / 443 场地；开幕周一 23 日 20:00 Teatro Dal Verme，Colson Whitehead（两届 Pulitzer）；预展周日 22 日 16:00 Fondazione Luigi Rovati，Edmund de Waal（官方新闻包与 de Waal 本人网站一致）。
- **Torino Film Festival 2026**：第 44 届、周二 24 日至周三 12月2日、9 天（官方规则一致）。
- **ATP Finals 2026**：11月15–22日、Torino Inalpi Arena、8 人、两组；Zverev 世界第一（11月9日排名 9,550 分），Alcaraz 热门，Cobolli 首秀（意大利唯一单打代表），Sinner 为 2025 冠军、因膝伤缺席——逐项核实。
- **Manovra 2027**：DPB 10月13日通过、10月15日送布鲁塞尔；2027 增长 +0.8%、赤字 3.4%（含条款）；CdM 10月28日批准法案；法案号 **C. 3174-bis**（10月30日以 A.C. 3174 送交众议院，11月4日删节后为 3174-bis）；听证会 11月9–12日；修正案截止周二 11月17日 18:00；最终表决须于 12月31日前；IRPEF 第二档 33% 扩至 55,000 欧元；金融业约 50 亿覆盖——逐项核实。文中三次 "PROPOSTA ≠ LEGGE" 披露与"尚未成为法律"一致。
- 历史/文化：Madonna della Salute 还愿 1630 年、Longhena 设计、建于 1631–1687 年；树节 1898 年起源、2013 年立法；Sforza–Visconti 婚礼 1441年10月25日；Colson Whitehead 两届 Pulitzer——均与公开记录一致。
- 无国际政治内容（禁词 Ucraina/Russia/Putin 全版未出现——经 grep 核实为 0 次）。

## 9. 观察项（单独列，不计缺陷）

1. **网 PDF 重建非逐字节相同**（见 §3）：1,291,734 B vs 交付 1,291,738 B；19 个子集字体字节序不同但码点集/字形数相同，文字层逐字节一致。属 fontTools 子集化不确定性，非内容差异；印 PDF 逐字节复现已通过。
2. **KIT §10 两处"观察"与交付文件不符**（KIT  stale，非版面缺陷）：Q92 印出注实为一词 "**Groeiprognose** voor 2027: +0,8 %"（正确荷兰语复合词），非 KIT 所称 "Groei Prognose"；Q32 印出注用 «Fate dolci»（角引号），非 KIT 所称直引号 “Fate dolci”。建议 KIT 订正，本版无需改动。
3. **"circa 26 miliardi"**：部分媒体称 23.5 miliardi，但官方公报与多家来源称"约 260 亿"，且文中已写 "circa" 并注明"根据报纸重建"，P6 另有"数字随辩论更新、引用前核对"的提示。不构成缺陷。
4. P3/P5 中部结构空白、P8 答案字号压至 9.75pt 下限，均为核心既有版式与 SOP §1.1 让步第 4 步（与核心一致），KIT 已载明。
5. 无真实读者来信——编辑示例 + 披露（承诺 VOL.5），与 W46 模式一致，KIT §6 已载明。

## 10. 缺陷清单

无。零缺陷，可定稿。

## 11. 证据索引（本 scratch）

- `GATE-LOG.md`（门禁总表）、`logs/gates-proof2.log`、`logs/run-rebuild.log`、`logs/render-rebuild.log`、`logs/webpdf-rebuild.log`、`logs/freeze-baseline.log`、`logs/freeze-baseline-core.log`、`logs/cream-measure.log`、`logs/render-png.log`
- `measure_cream.py`（奶油盒独立量测脚本）、`gates/gates-proof2.py`（门禁复刻脚本）、`gates/nl/`（p8/freeze 输出）
- `render/p1–p8.png`（交付 SVG 直渲全页）、`crops/p7-la-parola-box.png`、`crops/p1-la-settimana-box.png`、`crops/p1-cifre-box.png`、`crops/p1-masthead.png`（光栅裁图证据）
- `freeze-base/`（版 build-copy 重建 SVG + 重渲印/网 PDF）、`freeze-base-core/`（核心 freeze baseline）
- `tmp/pw/print-*.txt`、`tmp/pw/web-*.txt`（逐页印/网文字层）
