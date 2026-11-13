# W47 ru 家庭补修 2b FIX-LOG-2b（接 PROOF-NOTE-2 二轮重校的同类残留）

- 任务：第二轮修复工人修完 G-1～G-6（`scratch-fix-ru/FIX-LOG.md` §8）后，协调员验盘发现的两处同类残留（本 LOG 称修复 1、修复 2）。
- 日期：2026-11-12（Thu）
- 前置已读：`scratch-reproof2-w47-ru/PROOF-NOTE-2.md` G-4 一节；`scratch-fix-ru/FIX-LOG.md` §8.1（人称裁定）与 §8.5（观察到、未修）。
- 范围：只动 `production/2026-w47/2026-w47-ru-pt/`（修复 1，重渲染）与本 scratch 目录；`2026-w47-ru-nl/` 仅查证，结论为不动，全目录文件未变（SHA 见 §2.3）；不碰其他家庭、其他周；不 commit、不 push、不跑 lint、不改 SOP。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程（未用系统 python3）。
- 磁盘：开工 95G 已用、收尾 95G（门限 100G，全程未触发）。
- 工作文件：本目录 `apply2b.py`（5 处源头修改，断言计数）、`expected-pt.json`（backfill 预期替换）、`backfill2b.py`（复用第二轮 `round2-backfill.py`）、`driver-pt.sh`（构建驱动）、`verify2b.py`（印/网核验 + ru-nl 未动核验）、`gates2b.sh`（门禁驱动）、`pre-2026-w47-ru-{pt,nl}.text.md`（修前 text.md 快照）、`pre-{pt,nl}-svg.sha256`（修前 SVG 快照）、`logs/`（run/render/textmd/backfill/webpdf 日志）、`gates/`（门禁日志/JSON）、`build-pt.log`、`summary-pt.txt`。

## 1. 修复 1：ru-pt 练习指令称呼统一为 tu 体（5 行）

### 1.1 依据

- 本版主导人称为 tu（FIX-LOG §8.1：tu 式约 18 词次 `Lê/escolhe ×4`、`Completa ×4`、`Escreve`、`Traduz ×4`；第二轮已修标题 `E VOCÊ?` → `E TU?` 与 L471 `Responda` → `Responde`）。
- 5 处小节指令行（`e.bridge`）仍用 você 体命令式，与 G-4 同一缺陷类。定位方法：text.md 行号 → `grep` 源文件；`content34.py:74/96/238`、`content56.py:88/209`（FIX-LOG §8.5 记的 `content34.py:88` 实为 `:96`，以盘上 grep 为准）。
- 未动：L125/L129 `E tu?` 行；`content12.py:149` P1 注 `Leia a primeira página e escolha a resposta certa　Respostas na página 8`——text.md 全文 `grep -c Leia` = 0，该行只在 SVG（P1），不在 text.md；按任务要求未找、未碰。`Responde`（L471，第二轮已修）未动。

### 1.2 源头改动（`apply2b.py`，每处断言计数 1，全部通过）

| text.md 行 | 源文件 | 改前 | 改后 |
|---|---|---|---|
| L250 | `2026-w47-ru-pt/content34.py:74` | `Complete a forma verbal ou o caso correto.` | `Completa a forma verbal ou o caso correto.` |
| L268 | `2026-w47-ru-pt/content34.py:96` | `Forme frases corretas com as palavras.` | `Forma frases corretas com as palavras.` |
| L341 | `2026-w47-ru-pt/content34.py:238` | `Complete com o tempo correto do verbo entre parênteses.` | `Completa com o tempo correto do verbo entre parênteses.` |
| L418 | `2026-w47-ru-pt/content56.py:88` | `Forme frases corretas com as palavras.` | `Forma frases corretas com as palavras.` |
| L495 | `2026-w47-ru-pt/content56.py:209` | `Junte as duas frases numa só.` | `Junta as duas frases numa só.` |

改后复核：旧串 4 式在 `content34.py`/`content56.py` 中计数均为 0；新串各在位（`content34.py:74/96/238`、`content56.py:88/209`）。

### 1.3 重渲染记录（`driver-pt.sh`，`logs/`，2026-11-12 19:18–19:19 UTC）

- `run.py` rc=0，TOTAL 150，zero FLOW OVERFLOW / HEAD TOO WIDE（`logs/pt-run.log`）。
- `render.py` rc=0；印 PDF mtime 2026-11-12 19:19:12 UTC（重建成功非仅返回码：mtime + SHA 逐项验，见 §1.5）。
- `ru_textmd.py . 2026-w47-ru-pt.text.md "VOL.4 · Russian text · Portuguese explanations"` rc=0（干跑 `/tmp/fix2b-dryrun/`）。
- `backfill2b.py` rc=0：干跑丢弃 2 行标题（与第二轮同批，导出器 ≥24pt 规则 + D5 后缩字号所致），已原位置逐字回补——`### СМИ · O QUE DIZEM OS MEDIA`（pre L45–46，P1，`content12.py:73`，23pt）与 `### ЗА И ПРОТИВ · PRÓS E CONTRAS`（pre L448–449，P6，`content56.py:136`，22pt）；两行在落盘 text.md L46/L449 在位。
- 落盘后 text.md diff（vs 修前快照）**恰好 5 行**，即 §1.2 的 L250/L268/L341/L418/495，无其他行（`logs/pt-backfill.log` 全文 diff + `build-pt.log` 的 `diff` 输出）。
- `webpdf.py` rc=0；网 PDF mtime 2026-11-12 19:19:57 UTC。
- SVG 变动（vs 修前快照）：p3/p4/p5/p6 变，p1/p2/p7/p8 不变——与 5 处 bridge 所在页一致；P2（`E TU?` 栏）未动。

### 1.4 印/网核验（`verify2b.py`，全部 PASS）

- 印/网 PDF 各 8 页；印/网提取文字（归一化空白后）一致。
- 新串印/网计数：`Completa a forma verbal…` ×1/×1；`Forma frases corretas…` ×2/×2；`Completa com o tempo correto…` ×1/×1；`Junta as duas frases…` ×1/×1；旧串 4 式印/网均为 0。
- 未动标记仍在位（印 PDF）：`E TU?` ×1、`Responde com a faixa` ×1、`Leia a primeira` ×1（P1 注存活）、`E tu? Escreve duas frases` ×1。

### 1.5 新旧 SHA 对照（盘上实测全值；网 PDF SHA 为本次重建实时值）

| 文件 | 改前 SHA-256 | 改后 SHA-256 | 字节（改前 → 改后） |
|---|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-pt.pdf` | `0c119e4a6afa9748a81ea5e20af553a887756c070415a1b46ee9c474efc420e3` | `34344b82815de7808a0307e9fe6d84aee874a369c298753b6e98fc74dab59992` | 20,883,685 → 20,883,686 |
| 网 PDF `Lucerna-VOL4-ru-pt-web.pdf` | `853af83ca0ff2c275fa995ee8a33b961b2de3042c8d66f48fd3a9689b47c65b0` | `680702793672437cc43d22e247d0848911ebcd8708bdc682e1021d96def84264` | 3,337,224 → 3,337,241 |
| text.md `2026-w47-ru-pt.text.md` | `0920202237b2c2bea8e244c06bce2ccb5d50f6ceeb5f42ca4318f5f790de8bf5` | `00e972b717fb34055f76a435be87ba5fc51acbd9011ab34aba9eba373cbf5532` | 65,113 → 65,113（同长替换：Complete→Completa、Forme→Forma、Junte→Junta 均等长） |

改前 SHA 与 FIX-LOG §8.6 及 PROOF-NOTE-2 §4 逐一核对一致。KIT 已更新：§5 印/网行（L53–54）改为上表改后实测值；§7 列表末追加补修 2b 条目（源头改动、diff 行数、回补行、SVG 变动页、新旧 SHA、门禁结果）；历史条目（Fix 1/D5/F-2/第二轮）一律未动。

### 1.6 门禁（修后重跑，`gates/`，全部 rc=0）

| 门禁 | 结果 |
|---|---|
| `p8.py compare --total 150` | **CLEAN**：core/edition 各 150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 140]（E 节翻译题，预期） |
| `occlusion_audit.py`（svg/） | **0 flags** |
| `boxtitle_check.py` | **0 DEFECT、0 OBSERVE、0 marginal**（57 标题、683 正文行） |
| `spill_sweep.py` | **rc=0**（1 条既有 `[observe]`：`ABOVE -23.91px` 的 Black Friday gloss 行，与第二轮同式，非新缺陷） |
| `pdf_edge_scan.py`（印 PDF） | **0 TOUCH、0 NEAR**（8 页） |
| `head_check.py`（vs 本次 run.log） | **PASS 0 defects** |
| D5 census（`scratch-reproof2-w47-ru/census.py`，11 版全量） | **CJK+Latin=0、CJK+Cyrillic=0，全部 11 版**；本版弯引号 2 处全部 Newsreader |
| 引号普查（`census_quotes.py`，本版 svg） | **GRAND TOTAL defective: 0**（Newsreader U+201C×1、U+201D×1） |

## 2. 修复 2：ru-nl 词表 `Dooi` 大小写——查证后裁定不动

### 2.1 查证过程

查的是 Q141 选项在 SVG / 印 PDF 中的写法（任务指定；text.md L646/L827 答案键作 `Dooi c` 只是线索，不是结论）。

1. **源头**：`content8.py:85`，F 节匹配题（Q141–144）的选项标签列表为 `["Dooi c", "Grote uitverkoop d", "Uitslag a", "gladheid op de weg b"]`——`Dooi` 大写。词表源头 `content12.py:217` 为 `("оттепель", "тепло зимой: снег тает", "Dooi")`。
2. **印 PDF P8 答案区**（PyMuPDF 文字层）：`141. c — Dooi c` / `142. d — Grote uitverkoop d` / `143. a — Uitslag a` / `144. b — gladheid op de weg b`——Q141 选项正文作 `Dooi`，大写。
3. **SVG p8-test.svg**（`<text>` 元素拼接）：`141. c — Dooi c 142. d — Grote uitverkoop d 143. a — Uitslag a 144. b — gladheid op de weg b`——与印 PDF 一致，`Dooi` 大写。
4. **题面区无反例**：P8 F 节题面（`141–144. Koppel`）只印俄语词（141. оттепель…）与俄语释义选项（a. результат матча… / b. лёд на дороге / c. тепло зимой: снег тает / d. большая продажа со скидками），荷兰语选项词本身不出现在题面——即印版上不存在小写 `dooi` 的选项写法。SVG 含 `Dooi` 的仅 p2（词表）与 p8（答案键）两文件。
5. **同列表内比对**：同一选项标签列表 4 项中 3 项大写（`Dooi`、`Grote uitverkoop`、`Uitslag`），仅 `gladheid op de weg` 小写；P8 其余匹配题答案键亦大小写混用（`75. d — Grote uitverkoop d`、`78. c — Korting c` 大写 vs `76. b — retour b`、`77. a — kortingscode a` 小写）——大写是该答案键标签按源词原样刊载的体例，不是 `Dooi` 一处孤例。
6. **小写 `dooi` 的出现处均为行内释义，非选项/词表 headword**：P7 bridge `оттепель dooi; мокрый снег natte sneeuw; ледяной дождь ijzel.`、P8 key 16 `оттепель = dooi`——与词表 headword（独占一行的大写 `Dooi`，P2 印 PDF 文字层 1 处）属不同位置、不同体例，不构成版内矛盾的证据。
7. **FIX-LOG §8.5 的附带说明**：PROOF-NOTE-2 称 `IJzel` 为词表“唯一大写项”与盘上事实不符（`Dooi` 亦大写）——本次查证确认 `Dooi` 大写属实，但其大写与 Q141 选项标签大写一致，故不构成与 G-5 同类的缺陷。

### 2.2 结论：不动，裁定为已接受体例

- 按任务二分规则：选项正文作 `Dooi`（选项标签大写体例）→ 不动。词表 headword `Dooi` 与答案键选项 `Dooi c` 大小写一致，改词表为 `dooi` 反而会制造词表与答案键的不一致。
- ru-nl 未改任何文件，未重渲染。

### 2.3 ru-nl 未动核验（`verify2b.py`，全部 PASS）

| 文件 | SHA-256（修前 = 修后，盘上实测） | 字节 |
|---|---|---|
| text.md `2026-w47-ru-nl.text.md` | `b600944e5e5faacf6127e0a892c87519286bd2cd5429bbc070dafaf63fab184b` | 64,011 |
| 印 PDF `Lucerna-VOL4-ru-nl.pdf` | `5dedd8ecc30dae8a5a39ae1ed2e2066afc6c0e173d6b3dd5ae2056e2cd341e88` | 20,876,260 |
| 网 PDF `Lucerna-VOL4-ru-nl-web.pdf` | `1abee50e00351cd4d9663bae1f2fd188f45a83a9f0bd1378c883bef97aba9622` | 3,329,737 |
| svg/ 8 文件 | `sha256sum -c pre-nl-svg.sha256` 8/8 OK | — |

## 3. 收尾核对

- 触碰范围：`production/2026-w47/2026-w47-ru-pt/`（content34.py、content56.py、text.md、印/网 PDF、SVG p3–p6、WEEKLY-KIT.md）+ 本 scratch 目录；ru-nl 只读查证；其余家庭/周、SOP、lint 均未碰；未 commit、未 push。
- 进程：本次构建为单版串行，无需杀进程；未杀任何进程（FIX-LOG §8.9 的误杀教训已遵守）。
- 磁盘收尾 95G 已用（门限 100G，未触发）。
- 干跑/终版中间件在 `/tmp/fix2b-dryrun/`、`/tmp/fix2b-final/`（临时件，VM 重启即失）；修前快照 `pre-2026-w47-ru-{pt,nl}.text.md` 与 `pre-{pt,nl}-svg.sha256` 留在本目录。
