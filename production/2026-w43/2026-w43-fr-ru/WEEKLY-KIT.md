# WEEKLY-KIT — Le Lucerna VOL.2 · FR×RU（法语正文 + 俄语讲解）

- **校对状态：PASS**（建造者全量自校完成；独立校对整轮零问题，见 §12）
- 版面：files/weekly-report-fr-ru/（svg ×8、cards ×8、印刷 PDF、网页 PDF）
- Build：hidden_files/weekly-report-fr-ru-build/（自 FR 核心 build 复制 → freeze 基线 → 套用 FR×NL 已定稿扇出模板的 bslib4/content 结构 → 讲解层全量替换为俄语）
- 配对：目标语 = 法语（VOL.2 核心，files/weekly-report-vol4/）；读者母语 = 俄语。每页页脚与 P1 徽章明示配对。

## 1. 基线与核心完整性

- tools/freeze.py baseline：复制的 build 未改动即 8/8 逐字节复现已发布核心 SVG（p1 5f1dc8a1…、p2 b99e94be…、p3 cb4dc01e…、p4 14b128b7…、p5 f2d679f3…、p6 82021a2b…、p7 cb2bfc1c…、p8 5ac98ee1…，全表在 build 目录 core-shipped-hashes.txt）。
- 基线副本 OUT 指向曾误指核心 files 目录，已即时改指 build 内 baseline-svg/ 并复验核心 8/8 sha256 不变（事故与处置全程记录在案，核心零损伤）。
- 收尾复验：核心 8 SVG sha256 与出货值全等（sha256sum -c 全 OK）。另在 hidden_files/fr-ru-regcheck/ 以独立副本重跑核心 build，产物与出货 SVG 逐字节全等（二次证明）。

## 2. 总量（与核心逐项一致，注册表双 dump 对照实测）

- 总量 **145** = A2 55 · B1 65 · B2 25；逐页 10/16/18/18/17/18/11/37。核心与本版注册表（hidden_files/fr-ru-regcheck/{core,ru}-reg.json）对照：page/level/type 元数据差异 0。

## 3. RU 列家具定式（本版首立，逐项登记；结构沿 NL/PT 列，tables.json 无 RU 列条目）

- P1 徽章：«ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ»
- 页脚：«Le Lucerna · ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ФРАНЦУЗСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ»（期号 VOL.2 随 FR 核心）
- 页码行：«Страница N из 8»
- Gloss 前缀：«Пояснение — »
- P8 分隔：«— СТРАНИЦА N —»
- P1 顶带左：«VOL. 2 · № 2»；副题：«ФРАНЦУЗСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ОСЕНЬ И ПРАЗДНИКИ»
- P1 顶带中（strapline）：«HEBDOMADAIRE EN FRANÇAIS · ФРАНЦУЗСКИЙ, КОТОРЫЙ ЧИТАЮТ ФРАНЦУЗЫ»（见 §8 缺陷 3 的缩短裁定）
- 章节双语头样式：法语原题 · 俄语译名（如 «VIE QUOTIDIENNE · ПОВСЕДНЕВНАЯ ЖИЗНЬ»、«LES PHRASES DE LA SEMAINE · ФРАЗЫ НЕДЕЛИ»、«CLINIQUE DES ERREURS · СТОП!»——俄语部分受栏宽约束时取短式，逐项在 build 代码内）
- P8 顶带右：«ТЕСТ · ОТВЕТЫ ВНИЗУ ЭТОЙ СТРАНИЦЫ»；P8 大标题：«RÉPONSES · ВСЕ ОТВЕТЫ С ПРИМЕЧАНИЯМИ (СТРАНИЦЫ 1–8)»
- 目标语名（俄语形）：法语 = французский / на французском；各版页脚与徽章按此表套用。

## 4. 印刷注释门（FR 家族硬性项）

- 核心印刷集来源（三路独立互证全等）：
  1. tools/p8.py extract 于出货核心 P8 SVG：67 条；
  2. 核心 build 注册表按核心自身打印规则（page 8 ∨ 注 ≤10 字 ∨ 类型 ∈ {改错， 图表读数}）复算：67 条；
  3. FR×NL 先例显式集。
  集合 = {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71–74, 80–85, 92, 97, 105–145}。
- 本版以显式 PRINT_NOTES 集强制打印同一 67 条（俄语注普遍长于核心的 ≤10 字阈值，不强制则只印 48 条——已实测）。
- tools/p8.py compare（--target fr）：**CLEAN — core 67 noted = edition 67 noted，missing=[]、extra=0**。p8.py 行级 keydiff 列表 [4, 26, 35, 46, 71, 72, 73, 82, 108, 109, 111, 123, 132, 140, 145] 系注释译文进入印刷行所致；注册表级对照（§5）为键差异的权威口径。

## 5. 键差异登记（注册表逐字节对照；与 FR×NL 同构）

| 题号 | 核心键 | 本版键 | 性质 |
|---|---|---|---|
| 71 | ex. : amusant, parce que les enfants adorent se déguiser（参考答案） | ex. : amusant, parce que les enfants adorent se déguiser (образец ответа) | 法语范文逐字节不变，仅后缀译俄 |
| 72 | ex. : j'aime les histoires et les mots nouveaux（参考答案） | ex. : j'aime les histoires et les mots nouveaux (образец ответа) | 同上 |
| 73 | ex. : ce ne sont pas les résultats（参考答案） | ex. : ce ne sont pas les résultats (образец ответа) | 同上 |
| 132 | 读一份民调，本身就是在参与政治。 | Читать опрос — уже заниматься политикой. | 译俄题：答案语言随读者语 |
| 145 | 开放题 — 要点见写作框，范文在第 8 版写作框内 | Открытый вопрос — баллы в рамке для письма, а образец — в рамке MODÈLE на этой странице | 开放题装置说明译俄 |

- 其余 140 键与核心逐字节相同。注释差异 122 条（121 条中文注译俄 + #119 仅括号形制规范化：全角→半角，与全版印刷行口径一致）；未变的 23 条为法语语法注（与 FR×NL 的未变集逐号相同）。
- 题干改向（仅翻译/写作题）：#132 题干 «Переведите на русский: « Lire un sondage… »»；#133–135 题干 «Переведите на французский: <俄语句>»，其法语键逐字节不变。#109 选项与键为法语原文（samedi — 键内注 «24 октября — суббота» 为俄语历注）。
- P8 键式：沿 FR 核心括号式、注前空格（俄语注同式）。

## 6. P7 短语（逐字继承核心，含页标签）

- 7 条短语连同 (page N) 标签在核心与本版 P7 均逐字在版：« À trois heures, il sera deux heures. » (page 2)、« Les élèves sont en vacances depuis samedi. » (page 2)、« On n'offre jamais de chrysanthèmes pour un anniversaire. » (page 3)、« Wembanyama est plus grand que la plupart des joueurs. » (page 4)、« Les fans attendent ce jeu depuis des années. » (page 5)、« Si l'élection avait lieu dimanche, pour qui voteriez-vous ? » (page 6)、« On gagne une heure de sommeil. » (page 1)。
- 全刊出现次数 核心 = 本版 = [2, 3, 2, 1, 1, 2, 1]（逐条相等）。
- 短语的讲解行（语法点）译俄，法语例句与填空不变。

## 7. 冻结层核验

- tools/freeze.py diff：全 8 页新增 CJK 字符 = 0；edition CJK 总量 = 0（无全角残留）。
- 移除侧非法语项分类完毕：P8 12 条均为法语键/题干行因注释长度变化的重排折行片段（同一法语词群在新增侧全数在版）+ #132 题干改向 + #71 键后缀 + 第二层家具串（页脚、P8 顶带）替换；P3–P7 的 «。/）。» 为移除的中文讲解标点碎片。
- 图片：逐页 <image> 载荷 sha 与核心全等（P1/P2/P3 各 1 图，其余 0）；三条图注署名行与核心逐字相同（Hiroshige/LACMA、Atget、Flora de Filipinas (Blanco)）。
- P6 图表：条形 rect 与核心逐项全等（28+24+17+11+9+11=100，条长 504/432/306/198/162/198）；全页 rect 差异仅讲解框高度（俄语 gloss 多一行等）与随之位移的标记 chip，尺寸不变。
- 日历对照真实 2026（Europe/Paris 实测）：10-17 周六（假期开始）✓、10-24 周六（对话日/夜间换时）✓、10-25 周日 03:00→02:00 ✓、10-31 周六万圣节 ✓、11-01 周日诸圣节 ✓、11-02 周一复课 ✓；俄语注内日期（«1 ноября 2026 года — воскресенье»、«24 октября — суббота»）与之一致。

## 8. 缺陷与修复（建造者自校全量）

1. **P2 §A expl 溢出**：俄语 expl 3 行（核心/NL 为 2 行）引发级联，P2-ex 流溢出 386。改短为 «Заполните предложения по времени.»（2 行）→ 流位与核心/NL 逐点吻合（终于 2572，同核心）。
2. **P4 SAVIEZ-VOUS 框溢出**：俄语 «Теперь вы» 行 6 行（NL 4 行），框高超限且 _fit 钳制后框体压到页脚带下。改短为 4 行版 → P4-main 终于 2524（同 NL），框完整在栏内。
3. **P1 顶带同行碰撞（真墨迹重叠）**：居中 strapline 俄语部分过长，与右端日期 «SEMAINE DU 19 AU 25 OCTOBRE 2026» 墨迹相叠（«ФРАНЦУЗЫ» 与 «SEMAINE» 叠印，截圖实证）。裁定：删 «КАЖДУЮ НЕДЕЛЮ ·»（HEBDOMADAIRE 已含每周义），保留 «ФРАНЦУЗСКИЙ, КОТОРЫЙ ЧИТАЮТ ФРАНЦУЗЫ» 全义。修复后同行间距实测充足。注：规范遮挡审计的 TEXTX 只查异行，此类同行碰撞靠自加 scratch/rowcheck.py（同基线文本节点真墨迹间距扫描）兜底——本版/核心/NL 三方扫描均为 0 碰撞。
4. **P1 sommaire 标题 BOXTITLE**：«DANS CE NUMÉRO · В ЭТОМ НОМЕРЕ» 墨迹右端 1918.5 越框界 1885（规范审计实测命中）→ 改 «DANS CE NUMÉRO · В НОМЕРЕ»（墨迹终于 ≈1845）。
5. **P1 趋势框行溢出（advance 口径）**：«Чаще всего ищут: президентскую гонку 2027 года.» 右端 1936 越框 → 改 «В тренде: президентская гонка 2027 года.»（终于 1860）。
6. **P2 ET VOUS 框 LINEX**：俄语行 3 行（NL 2 行），末行墨迹被下方金线穿过（规范审计命中）→ 改短为 2 行 «У вас переводят часы? Во сколько вы встаёте в воскресенье? Напишите нам.»。
7. **P7/P8 章节头过宽（构建日志 HEAD TOO WIDE）**：5 处俄语头改短式（«NIVEAU A2 · БАЗОВЫЙ»、«NIVEAU B1 · СРЕДНИЙ»、«CLINIQUE DES ERREURS · СТОП!»、«B · CHOIX MULTIPLE · ВЫБОР»、«D · PHRASES · ПРЕДЛОЖЕНИЯ»），以 build 自带 text_w 实测 ≤434 为据；终版构建日志仅余核心继承的法语冻结头 «REGARDER UN MATCH EN FRANÇAIS»（核心与 NL 构建同样告警，非缺陷）。
8. **P8 顶带荷兰语残留**：«TOETS · …»（自 NL 模板继承的半截替换）→ 改 «ТЕСТ · ОТВЕТЫ ВНИЗУ ЭТОЙ СТРАНИЦЫ»。事后以荷兰语功能词表全量扫 8 页 SVG：零残留（命中均为法语词 pas/onze 的假阳性）。

- 终版构建日志：FLOW OVERFLOW = 0；唯一告警为上述继承法语头。

## 9. 遮挡与几何审计

- tools/occlusion_audit.py（自检先行，planted 六类全命中）：本版 **0 flags**，core 0 flags，**NEW vs core = 0**。
- scratch/rowcheck.py 同行碰撞扫描：本版 0（核心 0、NL 0）。
- advance 口径右扫（>1885.5）：终版唯一曾命中项已按 §8.5 修复；修复后全页零命中（中心/右锚元素按锚点口径计）。
- 8 页卡片逐页肉眼全检（P1–P8 渲染图）：家具、框体、练习流、答案块均无压字/越界。

## 10. 交付物与针脚（实测）

- svg ×8（files/weekly-report-fr-ru/svg/）：p1 3c0c305b…、p2 8abbce72…、p3 5ae1eca6…、p4 968651d7…、p5 868e5d5b…、p6 fc950098…、p7 0584f45d…、p8 308be510…（sha256 前 8 位）
- cards ×8：1950×2700 PNG（同目录 cards/）
- 印刷 PDF：Le-Lucerna-VOL2-RU.pdf — 9,783,685 B，sha256 c8f8e21bd66999617c079e8c54a14b6520fe1a7fee16d69f7d8cdd29a30d8718
- 网页 PDF：Le-Lucerna-VOL2-RU-web.pdf — 5,982,188 B（< 10 MB），sha256 3a106ff3b7b0a24f063c87b6c5795dd747ea996915075327c2f6a3a39910b0eb
- D5 重建（2026-11-13，见文末 D5 节）：印 `The-Lucerna-VOL1-fr-ru.pdf` **9,033,989 字节**（SHA-256 `df80755b444a4efd6811346dc9fac6b4ece0c473244f17cf08e0dad5106b4103`）；网 `2026-w43-fr-ru.web.pdf` **1,968,635 字节**（SHA-256 `5992c782b1f7b1307c4530ecd2133999c3e15cbd61f1aabb3217d845c8d4af1c`，< 7 MB）；text.md 与已发版 BYTE-IDENTICAL（SHA-256 `02e10cd09e7af51737861a3599ad03eabf978002861247668f1563df4c895502`）。D5 前值：印 9,783,685 B（SHA-256 `c8f8e21bd66999617c079e8c54a14b6520fe1a7fee16d69f7d8cdd29a30d8718`）、网 1,809,364 字节（`e0688ed4…`，issues 已发版）。

- 渲染：一进程 driver（scratch/build.py 顺序导入 content12/34/56/7/8）；渲染用 tools/venv（CairoSVG + PIL + pypdf）。

## 11. 纪律声明

- 中间层禁用术语（中英两形）在 paper / 本 KIT / operative code 中 0 出现（grep 实测）；模板方法名为 expl()（bslib4 自 NL 定稿模板继承，本无禁用名）。scratch/transform_ru.py 内的搜索模式串含对核心原文调用的引用，confined 于 scratch/ 并在此披露。
- 变换规模：自 NL 模板讲解串提取 316 条互异串，mapping 328 处替换全部计数断言通过（与 NL 构建同量）；核心 build 文件（bslib4/svglib/content）除 OUT 路径与讲解串外未动。
- 未入仓、未发 Discord、未向用户发消息。**独立校对：PASS（见 §12）。**

## 12. Independent proofread record — PASS, ZERO PROBLEMS

Proofreader: independent subagent (fresh pass, nothing taken on the
builder's word; every load-bearing claim re-run or re-measured).
Scratch: `hidden_files/proof-fr-ru/scratch/`.

**Freeze.** `tools/freeze.py baseline` on a pristine copy of the core
build repointed at this edition's outdir: **8/8 byte-identical**
(sha256). `tools/freeze.py diff` vs the core: added CJK = 0 on all 8
pages; edition CJK total = 0; every removed string classified — pages
1–7 removals are 100 % CJK-bearing (explanation layer / bilingual
furniture / Chinese footers), zero French body text removed; page 8's
12 non-CJK removals are answer-line re-wrap fragments whose word
groups all reappear on the added side, plus the registered #132 stem
re-aim. A one-process re-render from a repointed copy of this
edition's operative build code reproduces the shipped edition SVGs
**8/8 byte-identical** (and likewise the core's).

**Printed-note set — three-way proof.** (1) `p8.py compare`: **CLEAN,
core 67 = edition 67**. (2) `p8.py extract` on the shipped core P8 =
exactly the prescribed set {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47,
55, 56, 65, 71–74, 80–85, 92, 97, 105–145}. (3) The proofreader's own
one-process registry dump of the core, re-applying the core's own
print rule (page-8 section ∨ note ≤ 10 chars ∨ type ∈｛改错，图表读数｝),
recomputes exactly that 67-set; the shipped FR×NL P8 extracts the
identical set. The "unforced rule prints only 48" claim re-verified:
the naive rule on this edition's registry yields exactly 48, missing
exactly the 19 forced items. The explicit-set forcing in the shipped
edition is real and correct.

**Key diffs (registry, byte level).** Proofreader's own dumps of both
registries: 145 entries, metadata diffs 0; totals **145 = A2 55 · B1
65 · B2 25**, per-page 10/16/18/18/17/18/11/37. Key diffs exactly
{71, 72, 73, 132, 145}: #71–73 French sample text byte-identical,
only the suffix «（参考答案）» → « (образец ответа)»; #132 key → «Читать
опрос — уже заниматься политикой.»; #145 → the Russian apparatus
string. Note diffs 122, unchanged 23 = [3, 6, 16, 17, 18, 19, 54, 59,
61, 62, 75, 77, 86, 98, 101, 102, 103, 104, 117, 118, 120, 134, 135] —
the identical set to FR×NL's unchanged notes (symmetric difference
empty); each is a language-neutral French grammar note; #119 is pure
bracket normalization. Printed keys extracted from the shipped P8
SVGs differ from the core's at exactly the same 5 numbers; the other
10 line-level keydiff entries are note translations riding the same
line. Stems re-aimed as registered: #132 «Переведите на русский»,
#133–135 «Переведите на французский» with Russian stems and
byte-identical French keys. **All 145 keys additionally re-derived by
hand from the French body text on the final cards, page by page —
145/145 agree with the registry and the printed answers.**

**Same-line ink collision scan (README note #10, proofreader's own
scanner).** All text-node pairs, true PIL ink boxes, y-overlap ≥ 40 %
+ x-overlap > 0.5: **0 candidates on all 8 pages, edition and core**.
P1 top band measured: strapline ink [572.0, 1378.0], date ink starts
1487.8 → 109.8 units clear; deleting «КАЖДУЮ НЕДЕЛЮ ·» harms nothing
(«HEBDOMADAIRE» already says weekly).

**Geometry (ink measure).** `tools/occlusion_audit.py` (synthetic
selftest first): edition **0 flags**, core 0, NEW 0. Right-edge
sweep, ink and advance: max 1885.1 / 1885.0 in both editions — only
end-anchored furniture at the 1885 margin, identical to the core;
nothing > 1885.5. Builder's fixes pixel-verified: P1 sommaire title
«DANS CE NUMÉRO · В НОМЕРЕ» ink right = 1845.0 < 1885; P1 trend line
ink right = 1859.8; P2 ET VOUS Russian 2 lines, ink bottom 1549.1 vs
the gold rule at 1558 (8.9 clear); P2 §A explanation shortened as
registered; P4-main flow end 2524, deepest P4 content rect bottom
2540.7 < 2580; the five shortened section heads measure 316–410 ink
width (≤ 434 basis); P8 top band «ТЕСТ · ОТВЕТЫ ВНИЗУ ЭТОЙ СТРАНИЦЫ» —
no Dutch residue (function-word sweep over all 8 SVGs: 0 hits).
Final build logs (proofreader's reruns of core / RU / NL copies):
FLOW OVERFLOW = 0 in all three; the single warning in each is the
inherited frozen French head «REGARDER UN MATCH EN FRANÇAIS» — the
core and FR×NL logs carry the identical warning.

**Furniture pattern (§3) — adjudicated FIT to copy.** Every §3 string
verified verbatim in the shipped SVGs (badge, subtitle, footer ×8
with VOL.2, «Страница N из 8» ×8, «Пояснение — » glosses, P8
separators «— СТРАНИЦА 1–8 —», P8 big title, P1 «VOL. 2 · № 2»).
Russian forms checked: «тексты на французском» / «объяснения на
русском» (правильный предложный ряд), «выпуск для русскоязычных
читателей», «французский еженедельник», «все ответы с примечаниями»,
«французский, который читают французы» — all grammatically correct
and idiomatic. The pattern is approved as the RU-column standard for
the remaining ×RU editions.

**Images & credits.** One embedded payload on each of P1/P2/P3,
byte-identical to the core per page; credit lines verbatim identical
(Hiroshige / LACMA, Atget, *Flora de Filipinas* (Blanco)).

**P7.** Phrase occurrence counts edition = core = [2, 3, 2, 1, 1, 2,
1]; (page N) tag distribution identical (9 tags).

**Calendar (real 2026, Europe/Paris).** Oct 17 Sat, Oct 24 Sat,
Oct 25 Sun (03:00→02:00 fallback), Oct 31 Sat, Nov 1 Sun, Nov 2 Mon —
all match. The only two Russian date+weekday claims in the edition
(«1 ноября 2026 года — воскресенье», «24 октября — суббота») are both
correct. Content red line respected: French domestic politics only
(frozen core material); the Russian layer adds no international
politics.

**Banned-term scan.** The intermediary-layer term occurs 0 times —
in both its Chinese and English forms — in the paper SVGs, this KIT,
and the operative build code (the explanation helper is `expl()`);
its only occurrences anywhere are quoted core-original call strings
inside the one-off scratch transform, as disclosed in §1.
Transform spot-check: `to_translate.json` expected-hit total = 328 =
the registered replacement count, and the transform asserts per-string
hit counts.

**Final PDF pins (measured by the proofreader from disk, identical
to §10).** Web: 5,982,188 B, sha256
3a106ff3b7b0a24f063c87b6c5795dd747ea996915075327c2f6a3a39910b0eb
(8 pages, < 10 MB). Print: 9,783,685 B, sha256
c8f8e21bd66999617c079e8c54a14b6520fe1a7fee16d69f7d8cdd29a30d8718.

**Core integrity.** The frozen core's 8 shipped SVG sha256 values and
this edition's 8 were re-verified after all proofread work —
unchanged (§2 table).

**Verdict: PASS — one complete independent pass, ZERO problems.**
No fixes were needed, so no re-pass was required. Ready for repo
insert as slug `2026-w43-fr-ru`.

## 13、D5 重建记录（2026-11-13，D5-only）

SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader（SemiBold）。
施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：
`hidden_files/d5-redo/scratch-2026-w43-fr/logs/2026-w43-fr-ru/`；
逐版报告：`production/notes/2026-w43/g-fr/scratch-d5-rebuild-fr/D5-REPORT-2026-w43-fr-ru.md`。

**装机**：core 落盘 `apply_variant.py --patch-core fr --week 2026-w43`（core-fr
`svglib.py` +95/−3 行，`_D5_READER = "latin"`）；本版 `--svglib patched/…/svglib.py
--target fr --reader ru --week 2026-w43`，装后 `_D5_READER = "ru"`；路由单元测试 FAILURES: 0；fix2 块保留。
D1 组装先于安装：patched svglib 取本地 fanout D1 版，组装后与生产版 svglib 的 diff 恰为 D1 hunk 一处（28 行）。

**基线**（修前生产版）：run TOTAL 145，0 警告；印 PDF 与 `d1-fix/work/2026-w43-fr-ru/RESULT.txt`
的 shipped SHA/字节逐字节一致；印/网文字层差 0；自建网 vs issues 已发 web 非空字符差 0（仅空格差）；
修前普查 D5 拉丁 442、西里尔 310、弯引号在 CJK 0；基线 P8 noted 67/145。

**缺陷与修法**（run1 → run2 → run3；修法只动字号、盒高与间距，未动文字）：
head 0 项（D5 后 head/boxtitle/creambox 全过，无读者专属修复）；仅 spill ×2（共用）与 run3 sav 补偿；run2 P2 LINEX → run3 消除。

P8：208→198 行，距页脚线余量 32.7→32.7 px。

**门禁 run3（全套 16 门 ALL-GREEN）**：run TOTAL 145、0 警告；head_check 0；
d5 census 0/0/0；render RC=0；webpdf RC=0（1,968,635 B < 7 MB）；occlusion 0 flags；
p8 extract noted 67/145；p8 compare **CLEAN**（keydiff=[71, 72, 73, 132, 145]）；freeze baseline 8/8；
freeze diff 新增 CJK 字符 0；spill 0；boxtitle 0 DEFECT（45 titles）；
edge 0/0；creambox PASS 0 defects；文字层 print=web 差 0（各 106,829 字符）；census_quotes
0 defective；fr 家无 gates.py。

**新交付物**：印 `The-Lucerna-VOL1-fr-ru.pdf` 9,033,989 字节（`df80755b…`）；
网 `2026-w43-fr-ru.web.pdf` 1,968,635 字节（`5992c782…`）；text.md BYTE-IDENTICAL
（`02e10cd0…`）。练习仍为 145 题。
