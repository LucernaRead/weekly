# PROOF-NOTE — 2026-W47 nl-es（独立 re-proof，fix1 同步后版）

**结论：(a) 零缺陷可定稿。**

本轮为 fix1 后的独立全量重校（SOP §8.4），在交付印 PDF 上重测全部 9 处修复行、在交付 PDF 光栅上逐一复测全部盒标题、跑全部共享工具门禁、全文精读 P1–P8、150 题三源核对、外部事实抽查。未发现任何缺陷。生产目录未动（见 §9）。

**版本：** 2026-W47 `2026-w47-nl-es`（荷兰语目标 × 西班牙语读者），VOL.4，8 页，150 题。
**校对范围：** `production/2026-w47/2026-w47-nl-es/`，对照 `production/2026-w47/core-nl/`（冻结核心）。
未碰核心与其他版；未提交、未推送、未重渲染交付的 web PDF。

## 0. 开工探针与三 SHA 核对

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`（rc=0）；
  scratch 真实写文件成功（`scratch-reproof-nl-es1/probe.txt`）。TMPDIR 全程用本 scratch；
  磁盘 58G 可用。探针一次通过，无需等待重试。
- 三 SHA（实测，与任务给定值逐字节一致）：

| 成品 | SHA-256（实测） | 大小 |
|---|---|---|
| 印 `De-Lucerna-VOL4-nl-es.pdf` | `e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5` | 12,669,546 B |
| 网 `De-Lucerna-VOL4-nl-es-web.pdf` | `55e8489d18ee3d038c1da5a3c93aea144d2221289c98603c3c808306d577ad0b` | 1,616,170 B |
| 文 `2026-w47-nl-es.text.md` | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` | 47,649 B |

网 PDF 与 fix1 候选（`48b35efc…` / 1,616,171 B）差 1 字节：属 web PDF 时间戳不可复现的已知现象，
本轮只比文字层（§5：网/印逐行 0 差异），不以 SHA 判缺陷。

## 1. 机械门禁（全部通过）

| 门 | 实测值 | 证据 |
|---|---|---|
| run.py | rc=0，TOTAL **150**；by page 10/18/18/18/18/18/12/38；A2 46 / B1 73 / B2 31；零 OVERFLOW / TOO WIDE | `run-reproof.log`（scratch 副本内重跑；重建 8 SVG 与生产 SVG **逐字节一致**） |
| p8 compare | **CLEAN**；150/150 noted；keydiff **[137, 138]**（翻译题按设计对西语重定向，与修前一致） | `p8-compare.log`（两路：`--core-dir/--edition-dir` 与 `--core-p8/--edition-p8`，结果相同） |
| p8 extract | noted set 150/150 | `p8-extract.json/log` |
| freeze diff | rc=0；新增 CJK 仅 **U+3000 ×7**（P2–P8 各 1，荷西分隔符，非新增目标语文本） | `freeze-diff.json/log` |
| freeze baseline（核心） | rc=0，**8/8 SVG 字节一致**；核心 SVG 完整性复核无变化；`--core-svg` 指向 `core-nl/svg` 子目录；build-copy 内 8 SVG 与核心 SVG 逐一核对一致（非本版自比） | `freeze-baseline.log` |
| occlusion audit | 自检 6 类全触发、干净对照静默；**0 flags** | `occlusion.log/json`、`occlusion-selftest.log` |
| P8 最小字号 | **10.12pt**（P8 383 spans，0 个 <10pt；全版最小：P1–P5/P7 11.62pt，P6 12.75pt，P8 10.12pt；≥ 9.75pt 底线） | `p8-fontsize.log` |
| 网/印文字层 | pdftotext layout 与 raw 双路：**0 行差异**；均为 106,408 B | `print.txt`、`web.txt`、`web-vs-print.diff`（0 行）、`web-vs-print-raw.diff`（0 行） |

## 2. fix1 九行独立重测（交付印 PDF 光栅，600dpi，fix1 同方法，可直接比对）

源码 10 处修复均在位核实：`bslib4.py:21` `NOTE_RIGHT = RIGHT - 10`；
D2 `content12.py:147`、`:214`；D3 家具行 `content12.py:235`、`content34.py:50`、`:147`、
`content56.py:65`、`:183`、P8 `content8.py:133`；D1 `content56.py:153` 字号 24→23。
**行号出入（已核实，非缺失）：任务写第 5 处家具行在 `content56.py:180`，实际在 `:183`**
（内容与 `# fix1 … 5 of 5` 注释一致；同步员已先指出）。字符串均未动。

600dpi 复测（`edge600_reproof.py`，RGB max<180，值为最右暗像素左缘；与 fix1 `edge-after.json` **逐值一致**）：

| 行 | 页/带 | 实测（600dpi） | fix1 称 | 余量（限 1862） |
|---|---|---|---|---|
| D1 图标题 | P6 y210–260 | **1849.44** | 1849.44 | **+12.56** |
| D2 桥接行 | P1 y2320–2360 | **1856.16** | 1856.16 | **+5.84** |
| D2 栏目标题 | P2 y1566–1620 | **1855.68** | 1855.68 | **+6.32** |
| D3 家具行 | P2 y1850–1900 | **1853.92** | 1853.92 | **+8.08** |
| D3 家具行 | P3 y1620–1675 | **1853.92** | 1853.92 | **+8.08** |
| D3 家具行 | P4 y1620–1675 | **1853.92** | 1853.92 | **+8.08** |
| D3 家具行 | P5 y1620–1675 | **1853.92** | 1853.92 | **+8.08** |
| D3 家具行 | P6 y1620–1675 | **1853.92** | 1853.92 | **+8.08** |
| D3 答案头行 | P8 y1275–1330 | **1854.08** | 1854.08 | **+7.92** |

300dpi 独立交叉复测（`edge_scan_reproof.py`，灰度 <128，值为最右暗像素右缘；系统性高 0.08–0.40px，
为像素取位约定差，非真实差异）：D1 1849.52、D2 P1 1856.24、D2 P2 1855.92、D3 家具行 1854.32、D3 P8 1854.32——
全部在内，最小余量 +5.76px。

整页墨右（不含页脚带 y>2550）：600dpi：P1 **1862.24**，P2–P8 **1861.92**（与 fix1 一致）。
P1 1862.24 成分解剖（本轮独立确认，见 §3）：刊头日期行末字 + hline 端点 x2=1862.0 + 深绿满栏条右缘，
均为设计边；D2 行本身在内（1856.16）。

## 3. P1 超限成分独立确认（设计边，非缺陷文本）

- y50–100 带：仅刊头日期行（`content12.py:16`，SVG 已转为 x=1434.6 起锚）末字 “6” 的抗锯齿边，
  600dpi 墨至 1862.24。PIL 真墨算式：getbbox 右 362.75 + 字距偏移 1.7×38=64.6 → 预测 1861.95，
  与光栅 1862.24 差 0.29px（Cairo/PIL 字宽差，同 proof1 的 1.4–4.1px 机制量级内）。
  该行按设计右锚于 1862（与 hline 同缘）。
- y400–450 带：hline y=420（x2=1862.0，stroke 2），窄带实测 1861.92。
- y450–600 带：深绿满栏条 rect y=470–588（右缘 1862.0），实测 1862.32（300dpi）。
- y1500–1800 / y2100–2400 带：照片/奶油盒右缘 1862.0，实测 1862.0。
- **核心对照（决定性）：同一 300dpi 方法扫核心印 PDF，整页墨右 P1 1862.64、P2–P8 1862.32，
  与本版逐值相同**——该墨右是冻结核心继承的设计边，不是本版文本溢出。
- 左缘：87.68（0.32px 以内系统性墨，核心亦同），非缺陷。

## 4. 盒标题逐一光栅复测（26 个，全部通过）

**标题定义（本轮注明）：盒标题 = 每只奶油底框（fill `#f0eee5`）内的首行文字；计数 = 含标题的奶油框数。**
P1–P7 共 26 框、26 标题、0 无标题框；P8 无奶油框。
brief 模板写的 "56 titles" 在此定义下为幻数（本版实测 26；六版独立测量亦证实模板数与实测不符），不以 56 为准。
裁定以**交付印 PDF 光栅**为准（300dpi，灰度 <128，取标题 y 带内、框 x 范围内最右暗像素）；
PIL 真墨（`occlusion_audit.ink_box`，4× 超采样）仅交叉验证。
盒坐标与语言标记均按本版重推导（未复用他版盒坐标；本版为 nl-es，es 标记）。

最小余量 **+12.58px**（D1 图标题）；其余 ≥ +18.34px。全表见附录 A。
另：全量 PIL 墨缘扫描（1,638 个文本节点）仅 16 个 LEFT+0.2 标记（墨左 87.8，系统性，见 §3），
RIGHT / PAGE / FOOTER 标记 0；奶油盒底容纳检查 0 标记。

## 5. Delta 六处独立复核（D6–D11，全部通过）

- **D6**（P3 桥接 w=377.5）：`svglib.wrap` 0.5px 步长实测区间 329.5–425.5，连续，中点 377.5，在内。
- **D7**（P7 gloss 桥接 w=419.5）：区间 414.5–424.5，连续，中点 419.5，在内。
- **D8**（P6 标题 capcn_w=370.75）：区间 349.5–392.0，连续，中点 370.75，在内。
- **D9**（Q140 键已修）：登记 `content8.py`、text.md:415、P8 印出键三源一致——
  「Ik maak een surprise met een kort gedicht.」，附注「surprise: expresión fija; corto = kort」；
  与题干西语「Hago una sorpresa con un poema corto.」（corto = kort）契合。
- **D10**（P7 致读者信 dt_zh_w=362.5）：区间 319.5–405.5，连续，中点 362.5，在内。
- **D11**（P4 HET PROGRAMMA 盒，sh=638）：事实行换行数重算 3/3/3/2/3=14 行，
  sh = 89 + Σ(n×30.5+12) + 32 + 30 = **638.0**，与 `content34.py:134` 一致；
  盒 rect y=591.6 h=638.0（底 1229.6），末行「18:45 uur.」基线 y=1209.49；
  盒下 7px 带（y1229.6–1236.6）交付印 PDF 像素探针：**0 暗像素**（最小灰度 249）。
  目视 P4 卡片确认盒内末行下方留白充足。

## 6. 全文精读（P1–P8，SVG 可见文本逐行 + 目视 8/8 卡片）

- 荷兰语拼写/变位/性数/标点：通读 1,638 个文本节点，无拼写错误、无截断句、无重复词。
  讲解层注释的词均真实出现在正文里（逐项对照 Nota/gloss 框）。
- P7 「ZINNEN VAN DE WEEK」8 句引文与源页逐字一致（P1×2、P2、P3、P4、P5、P6×2），页码标注全对。
- P7 读者来信明确标为编辑部示例（"voorbeeldbrief van de redactie"、"nog geen echte brieven … binnen"），无虚构来信。
- 孤儿行扫描：14 个以破折号开首的行候选，逐一核实均为合法续行/对话破折号/“— PAGINA N —”分隔头，**真孤儿 0**；
  基线出页检查 0。
- 算术重算：Q22/Q45 11月16日→12月5日 = 19 天；Q43 14→15日 = 1 天；Q44 12:00–16:00 = 4 小时；
  Q46 2009→2026 = 17 年；Q85 35+30=65；Q87 35+30+20+15=100；小组积分 NL 8 / GR 8 / DE 5 / SRB 0
  与所列比分可满足（NL 1–1、2–1、2–2、2–1 = 8；DE 1–1、0–1、2–0、0–0 = 5；GR 7–5 进球差需未印出的 GR–SRB 一场，
  版内未矛盾）；Q150 模型文印出 81 词，与 text.md 逐字一致（80–100 范围内）。
- 日期/星期（`date` 核对）：2026-11-01 周日、11-14 周六、11-15 周日、11-16 周一、11-21 周六、
  11-22 周日、11-24 周二、11-29 周日、12-05 周六，全部与版内一致。
- 目视 P1–P8（生产 cards/，与 8/8 逐字节一致的重建 SVG 对应）：版式干净，无重叠、无压页脚、无截断；
  图片均有来源标注（Wim van Rossem/Anefo 国立档案馆 CC0；Spaarnestad/Wikimedia 公有领域；
  Elise Iovenko/Unsplash CC0；Cristina Gottardi/Unsplash CC0；Aaron Burden/Unsplash CC0）。
  P6 中栏、P4 中栏大片留白为核心版式继承（见观察 O3）。
- 外部事实抽查（独立检索，2026-11-11）：
  - Grave 全国入城式 2026-11-14 周六、Maaskade 约 12:00、节目 12:00–16:00、NPO Zapp/NPO 3 直播、
    市长 Marieke Moorman 迎接、主持 Merel Westrik、马 Ozosnel——与版内全符（vandaagingrave.nl、NTR 通稿源）。
  - Amsterdam 入城式 2026-11-15 周日、**第 88 届**、船 De Omval 10:15、Scheepvaartmuseum 约 11:30 获市钥、
    陆上巡游 Stopera 13:00 经 Rembrandtplein/Utrechtsestraat 至 Leidseplein——与版内全符
    （desinterklaassite.nl、iamsterdam.com、holland-explorer.com）。
  - Pakjesavond 2026-12-05 周六。
  - Heel Nederland Leest 2026 书为 Herman Koch《Het diner》（2009），11 月全月图书馆免费取（含大字版、
    Makkelijk Lezen 版、电子书、有声书、读书圈）——与版内全符（cpnb.nl）。
  - Expeditie Robinson 2026：11 月 1 日周日 20:00 RTL 4 首播；19 名选手（10 荷兰 + 9 佛兰德）；
    马来西亚 34 天；主持 Nicolette Kluijver 与 Edson da Graça，记者 Camille Vanuxem——与版内全符
    （nl.wikipedia.org、veronicasuperguide.nl）。
  - VOL.5 预告日期：11 月 24 日周二、11 月 29 日周日，与星期一致。

## 7. 150 题三源核对（登记 vs text.md vs P8 印出键：0 不一致）

- REG（scratch 重跑 `run.py` 导出）：150 条，编号 1–150 无缺重；by page 10/18/18/18/18/18/12/38。
- text.md：`Respuesta:` 142 处 + 配对项 `(Respuesta x)` 8 处 = 150 键全解析；`答案：` 0 处；
  CJK 表意字 0；U+3000 分隔符 59 个。
- P8 印出键（`p8.py extract`）：150/150。
- **三源逐题比对：0 不一致**（Q150 为开放写作题例外，P8 印 ✓ + 模型文 81 词）。
- 荷兰语题干 vs 核心：140/150 题干在核心 SVG 文本中逐字出现；其余 10 项均有设计内解释——
  Q25–28、Q141–144 配对项（题项与选项分栏排布，不构成连续串，核心与本版同状）；
  Q139/Q140 为翻译方向题源句（西语句，本版独有；核心为中语句，按设计）。
- 配对题键逐一核对：Q25–28 = d/c/a/b；Q141–144 = b/c/d/a；与 P2/P8 选项表一致。
- p8 compare keydiff [137, 138]：仅翻译题按设计对西语重定向（137/138 译入西语；139/140 译入荷兰语，键与核心同）；
  Q137 西语译文「El noticiario de Sinterklaas se emite cada día a las 18:00.」正确；
  Q138「Los dos primeros pasan a cuartos de final.」正确。

## 8. 观察类（不列缺陷）

- **O1（工具发现，非本版缺陷）**：`tools/occlusion_audit.py` 的 `ink_box` 对带字距（letter-spacing）的
  字符串系统性低估右缘：`getbbox` 不含字距位移，而实际排版每字后移 `spacing×(n−1)`。
  以 P1 日期行为例：PIL 右缘 1797.35，真实光栅 1862.24，差 64.6px = 1.7×38。
  结论：occlusion 审计对字距字符串的右缘溢出是盲的；本版靠交付 PDF 光栅全页扫描兜底（§2–§3），
  未发现任何溢出。建议协调员将该修进工具（`ink_box` 的墨右应加 `spacing×(n−1)`），再跑全周复核；
  本版结论不受影响（光栅为裁定法）。
- **O2**：左缘系统性墨 x=87.68（0.32px 内），8 页与核心均有，属渲染系统误差。
- **O3**：P6 中栏、P4 中栏大片留白，核心版式继承，非缺陷。
- **O4**：Q78「Zij ___ (maken)」键 `gaat maken`（Zij 单数）：与 Q79「De kinderen → gaan schrijven」
  （复数）构成单/复数对比设计，有设计依据，不列缺陷（proof1 O1 同断）。

## 9. 生产未动证明

- 校对全程只在 `scratch-reproof-nl-es1/` 内重建/重渲染；生产快照 `snapshot-before.sha256`（42 文件）
  vs `snapshot-after.sha256`：**逐字节一致，零变化**。
- `git status` 中 `2026-w47-nl-es/` 为未跟踪目录，系开工前即有状态（尚未入仓），非本人写入。
- 本人未在生产目录写任何文件，未 commit、未 push。

## 附录 A. 盒标题全表（26 个，光栅裁定）

标题定义见 §4。box_right 为奶油框右缘；raster 为交付印 PDF 光栅最右墨（300dpi，<128）；
pil 为 PIL 真墨交叉验证；余量均为正。

| 页 | 标题（截） | 框右缘 | 光栅墨右 | 光栅余量 | PIL 墨右 | PIL 余量 |
|---|---|---|---|---|---|---|
| P1 | DEZE WEEK | 1862.0 | 1613.26 | +248.74 | 1613.2 | +248.8 |
| P1 | IN DEZE EDITIE　ESTE NÚMERO | 1862.0 | 1830.86 | +31.14 | 1831.5 | +30.5 |
| P1 | DE WEEK IN CIJFERS　EN CIFRAS | 961.0 | 926.02 | +34.98 | 926.0 | +35.0 |
| P1 | IN HET KORT　EN BREVE | 1862.0 | 1750.54 | +111.46 | 1750.8 | +111.2 |
| P2 | WIST JE DAT? | 1862.0 | 1619.66 | +242.34 | 1617.8 | +244.2 |
| P2 | ZO ONTHOUD JE HET　RECUERDA | 961.0 | 941.38 | +19.62 | 940.2 | +20.8 |
| P2 | EN JIJ?　¿Y TÚ? | 1862.0 | 1647.18 | +214.82 | 1645.0 | +217.0 |
| P2 | Nota — de schoen zapato · de wortel | 961.0 | 917.70 | +43.30 | 915.5 | +45.5 |
| P2 | SCHOEN | 510.5 | 370.24 | +140.26 | 257.8 | +252.7 |
| P2 | WORTEL | 961.0 | 873.54 | +87.46 | 713.2 | +247.8 |
| P2 | LIJSTJE | 1411.5 | 1323.40 | +88.10 | 1144.5 | +267.0 |
| P2 | GEDICHT | 1862.0 | 1734.54 | +127.46 | 1625.0 | +237.0 |
| P3 | SINTERKLAAS IN CIJFERS | 1862.0 | 1757.90 | +104.10 | 1758.2 | +103.8 |
| P3 | Nota — de vestingstad ciudad fortificada | 961.0 | 942.02 | +18.98 | 940.8 | +20.2 |
| P4 | HET PROGRAMMA | 1862.0 | 1671.18 | +190.82 | 1671.0 | +191.0 |
| P4 | Nota — de groepswinst victoria de grupo | 961.0 | 942.66 | +18.34 | 941.5 | +19.5 |
| P5 | JONGEREN IN CIJFERS | 1862.0 | 1726.22 | +135.78 | 1726.5 | +135.5 |
| P5 | EN JIJ?　¿Y TÚ? | 1862.0 | 1647.18 | +214.82 | 1645.0 | +217.0 |
| P5 | ZO KIJK JE ROBINSON | 961.0 | 804.74 | +156.26 | 806.0 | +155.0 |
| P5 | Nota — de surprise regalo disfrazado · | 961.0 | 923.78 | +37.22 | 929.0 | +32.0 |
| P6 | DE GRAFIEK　DATOS DE PRÁCTICA | 1862.0 | 1849.42 | +12.58 | 1846.0 | +16.0 |
| P6 | VOOR OF TEGEN?　¿SÍ O NO? | 1862.0 | 1758.86 | +103.14 | 1758.5 | +103.5 |
| P6 | Nota — het verlanglijstje lista de deseos | 961.0 | 934.02 | +26.98 | 932.0 | +29.0 |
| P7 | PAS OP!　CLÍNICA DE ERRORES | 1862.0 | 1813.90 | +48.10 | 1813.5 | +48.5 |
| P7 | HET WOORD　PALABRA SEMANAL | 1862.0 | 1841.10 | +20.90 | 1840.2 | +21.8 |
| P7 | BRIEVEN VAN LEZERS | 1862.0 | 1701.90 | +160.10 | 1701.8 | +160.2 |

注：SCHOEN/WORTEL/LIJSTJE/GEDICHT 四格光栅值取标题 y 带内框内最右墨（含同带 gloss 行），仍在框内，
余量为对框右缘的真实余量；PIL 值仅为标题词本身。
