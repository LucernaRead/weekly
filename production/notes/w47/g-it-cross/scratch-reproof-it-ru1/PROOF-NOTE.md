# 复校结论：(b) 发现 1 项新缺陷 D-2（冻结核心句，P7）——D-1 已干净回归，门禁 20/20、freeze 8/8

**版本**：2026-w47-it-ru（意大利语目标语 × 俄语读者，VOL.4），fix1 后第二轮全量复校（SOP §8.4）。
**复校员**：独立复校（scratch-reproof-it-ru1）。生产文件只读，未写生产目录任何文件（生产文件最后写入时间 2026-11-11 21:12:56 UTC，早于本次开工 21:14:35 UTC；未 commit、未 push）。

## SHA 核对（开工前实测，与任务给定值逐字节一致）

| 文件 | 字节数 | SHA-256（实测） | 对照 |
|---|---|---|---|
| La-Lucerna-VOL4-RU.pdf（印刷） | 14,180,929 | af980e26fcb124773e0e3a5824e3ff742e6a72f8da50c8e53ab017418adf6200 | 全对 |
| La-Lucerna-VOL4-RU-web.pdf（网页） | 1,441,248 | 3e10d785bd1eab5318ef175a52bdebef89649622d1a7f53ea891b54b4f652cc9 | 全对 |
| 2026-w47-it-ru.text.md | 67,752 | 8a49ce37cc7df3ba92569243cd28b0286bee6651547f526c8cacdf112c5c895c | 全对 |

开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` RC=0；scratch 内真实写文件通过。

## D-1 回归：干净（已修好）

旧形 «налоговая ставка» 全版 0 次：text.md 0、8 个 SVG 0、印/网 PDF 文字层各 0。
新形 «ступень налоговой шкалы» 在 text.md 5 处各就其位：

| 位置 | text.md 行 | 内容 |
|---|---|---|
| P6 NOTE 注释 | :663 | `lo scaglione, ступень налоговой шкалы` |
| Q100 注 | :763 | `key: scaglione (scaglione = ступень налоговой шкалы)` |
| Q144 注 | :987 | `lo scaglione — un livello di reddito del sistema fiscale (key a · scaglione = ступень налоговой шкалы, a)` |
| P8 key 100 | :1217 | `100. scaglione — scaglione = ступень налоговой шкалы` |
| P8 key 144 | :1305 | `144. a — scaglione = ступень налоговой шкалы, a` |

来源核实：`scratch-fanout-it/translations.py` 三处 ru 值 L805（gloss）、L1782（key 100 注）、L2080（key 144 注）均为新形。
Q144 题干「un livello di reddito del sistema fiscale」（收入档位）与答案注「ступень налоговой шкалы」（税级）不再矛盾。
注：5 处中 Q100 注与 Q144 注只存在于 text.md——这是本流水线的既定设计（习题括号注一律 text.md-only；实测 p7 SVG 中 `играется`/`должен`/`Переведите` 均为 0 次）。渲染层的新形为 3 处：P6 注释、P8 key 100、P8 key 144（印/网 PDF 文字层 P6 «ступень» ×1、P8 ×2；P6 词组因换行分行，提取时不断行计数为 0，但渲染像素中完整可见）。

**P6 NOTE 注释盒（交付 PDF 渲染像素实测）**：盒 rect（SVG）x=538.5 y=1102.4 w=422.5 h=264.575；注释 7 行基线 y=1140.9/1170.6/1200.3/1230.1/1259.8/1289.5/1319.2，全部在盒内——上沿余 11.0 pt、下沿余 31.3 pt、右沿最小余 12.7 pt（«слушания» 行；«бюджетный» 行 18.8 pt），无字越盒。渲染截图 `crop-p6.png` 目检：7 行完整，«ступень налоговой шкалы» 在第 6 行完整可见。

**P8 key 100 / 144（交付 PDF 词框实测，0.75 缩放）**：
- key 100：基线 y0≈1589–1592 pt，词 `100. scaglione — scaglione = ступень налоговой шкалы` 单行；右缘 1001.1 pt = 1334.8 SVG 单位；栏（col3，右缘 1411.5）余 **76.7 SVG px**（fix1 称 77.9，差 1.2 px，在 PIL 与真实渲染的 ±5 px 系统差内）。
- key 144：基线 y0≈1747–1750 pt，词 `144. a — scaglione = ступень налоговой шкалы, a` 单行；右缘 1311.3 pt = 1748.4 SVG 单位；栏（col4，右缘 1862.0）余 **113.6 SVG px**（fix1 称 112.8，差 0.8 px）。
- 渲染截图 `crop-p8.png` 目检：两行均为单行、栏内、无换行、无溢出。P8 最小字号重测 13.0 px = 9.75 pt（SOP §1.1 下限，恰达下限）。

## 缺陷清单

### D-2（新发现，高严重度）：P7 未来时讲解把 andare 与 leggere 的规则性说反了

**位置**：P7（Lingua）A2 IL FUTURO 段；源码 `core-it/content7.py` L17、L18（冻结核心意大利语，本版 `content7.py` L17、L18 逐字相同）；text.md:775、:777；印/网 PDF P7 文字层各出现 1 次；渲染截图 `crop-p7-futuro.png`。

**原文（全错在规则性标签，动词形式本身拼写全对）**：
1. L17 / text.md:775：`Le forme sono regolari: andare → andrò, assaggiare → assaggerò, guardare → guarderò.`
2. L18 / text.md:777：`Il verbo è leggere, irregolare al futuro: leggerò.`

**事实**：
1. **andare 的未来时是不规则的**：andrò 属元音脱落型不规则未来时（规则形应为 *anderò*）。公开依据：LibreTexts《Il futuro》附录 F（不规则未来时元音脱落组：andare → andrò, avere → avrò, potere → potrò, dovere → dovrò, vedere → vedrò；https://human.libretexts.org/Bookshelves/Languages/Italian/Tutt_a_tavola_II/02%3A_Appendices/2.06%3A_Appendix_F_-_Il_futuro）；Transparent Language《Irregular Verbs in the Future Tense》（andare → andrò；https://blogs.transparent.com/italian/irregular-verbs-in-the-future-tense/）。故 L17「Le forme sono regolari」在包含 andrò 时为假；andremo 同样不规则。
2. **leggere 的未来时是规则的**：leggerò 恰为规则构形（不定式去尾 -e + 词尾 -ò，如 prendere → prenderò、vincere → vincerò）。公开依据：Reverso  conjugazione leggere 注「Passato remoto e participio irregolari (io lessi/letto)」——不规则处只在远过去时与过去分词，不在未来时（https://conjugacao.reverso.net/conjugacao-italiano-verbo-leggere.html）；Wiktionary leggere 未来时表 leggerò / leggerai / leggerà / leggeremo / leggerete / leggeranno（https://it.wiktionary.org/wiki/Appendice:Coniugazioni/Italiano/leggere）。故 L18「irregolare al futuro」为假；leggere 不规则的是 lessi / letto，不是未来时。

两处标签正好互换。习题键不受影响（Q101–103 键 andremo / assaggeremo / guarderemo 形式正确；Q104 键注只说「leggerò — будущее время глагола leggere」，无规则性断言）。

**严重度**：高——这是语言学习报纸的教学内容错误，且正在教的正是未来时构形；读者会记错 andare / leggere 的规则性。**修复路径**：属冻结核心，版内无法单修（否则破 freeze）；须 core-it 改 L17–L18 后重走 12 版 it-* fan-out，由协调员定夺。建议最小改法（供修复方参考，非定稿）：L17 改为规则形只举 assaggiare / guardare，andare 另标不规则；L18 改为「Il verbo è leggere, regolare al futuro: leggerò.」

## 其余复校结果（全文通读 1317 行 + 门禁，皆通过）

- 门禁 20/20 全过（详见 GATE-LOG.md）：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137, 138, 139]（预期的重定向读者句键）；freeze diff P1–7 0 未解释增减；strict-CJK 除 U+3000 外 0；印/网 PDF 字符集完全相同（各 7590 词）；web PDF 1,441,248 B < 7 MB；P8 最小字号 13.0 px；§1.1 扫描通过；text.md validate 0/0；150 键与注释与核心/翻译表一致。
- freeze baseline 重建：8/8 SVG 字节一致，核心完整性校验通过（重建前后核心 SVG 未变）。
- 全文通读：P1–P8 事实与数字自洽（积分榜 29/28/27/24/23/5、24 球/10 场、比赛结果表与正文一致、20.45 周日、BookCity 15 届/1360 活动/2487 人/443 场地、图表题算术 13−11=2、6+7=13、样文 99 词与所称 99 词一致）；150 题键逐题核对与题干一致；Q140 键在核心与本版同为意大利语 «Ogni cifra deve essere chiara.»，为正确行为，未动；「next Sunday」为冻结核心，永不是缺陷。
- P6「LA STRADA DELLA MANOVRA」时间线（28 OTT / 9–12 NOV / 17 NOV 18:00 / 31 DIC）与正文一致；P7 虚拟式/直陈式讲解（piova/nevichi/controllino/sia；so che + 直陈式）正确；ERRORI TIPICI 四例改正正确。

## 观察项（不是缺陷，不拦定稿）

- **OBS-1（P1/P2 双语小标题越框，沿用观察项）**：P1 标题 `НЕДЕЛЯ В ЦИФРАХ` 墨水右缘 1066.6 SVG 单位，越过无边框 cream 框（x=538.5，右缘 961.0）105.6 px；P2 `ЗАПОМНИТЕ` 右缘 1022.7，越框 61.7 px。按 STRADDLE 裁决：框无边框、无字形被裁、无墨水与他物/可见边框重叠，且与备份旧版逐字节相同（text.md:45/:205 相同；SVG 标题节点 x/y/文字相同；印 PDF 词框位置相同，新旧皆 P1 x1=800.0 pt、P2 x1=767.0 pt），非回归——fix1 未动它们。occlusion 审计 0 flags 亦无重叠。保持观察项。
- **OBS-2（混合语种空格偏窄，旧版同款，非回归）**：少数拉丁↔西里尔边界处的独立空格节点渲染偏窄（墨水间隙约 2.2 SVG 单位，正常词间约 4.8），如 P8 key 104「глагола leggere」、106「vedere с」、108「finire с」；pdftotext 合并词共 22 个、13 个去重形。备份印 PDF 实测完全相同（22 个、同分布、同词形），属 svglib 按语种分段 + CJK 空格节点的全系旧有表现，fix1 未引入。词仍可辨读，不拦。

## 交付文件（本 scratch 内）

- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`（每项门禁结果 + 实测值）
- 证据：`gates-ru-raw.log`、`freeze-baseline.log`、`svg-counts.txt`、`render-p1.png`、`render-p2.png`、`render-p6.png`、`render-p8.png`、`crop-p6.png`、`crop-p8.png`、`crop-p7-futuro.png`、`key104-zoom.png`
