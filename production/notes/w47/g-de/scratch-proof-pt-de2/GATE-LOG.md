# GATE-LOG — 2026-W47 pt-de proof2（重建版，独立复校机械门实跑记录）

独立复校员 proof2，2026-11-11。工具链：`~/workspace/weekly-git/tools/venv/bin/python`
（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 全程指向 scratch 下 `tmp/`（系统 /tmp 未用）。
正典 creambox：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`
（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与 proof1 所用同一文件；refanout scratch 内的
`creambox.py` 是旧 13 行版，md5 `a5dbea58…`，本次未用——正典版多 inside-only/desc-clear 实测）。
所用运行命令与输出均列于下；KIT 自述数值一律不采信，只认以下本人实跑结果。
Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-de2/`

## §0 身份与探针

- 探针：`ls -la /dev/null` 存在（crw-rw-rw-，1, 3）；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` →
  `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，RC=0（与 proof1 同值，无引用孤 blob，无影响）；
  scratch 写 `probe-write.txt`（`ok`）成功。
- SHA/字节核对（`sha256sum` + `stat`，开工与收工各一次）：印 PDF 12,938,914 B `77243c72…e6284a` ✓；
  网 PDF 1,147,629 B `56eb92d0…13b84b` ✓；text.md 37,907 B `519ab0de…d784305` ✓。与任务完全一致。
- 核心 HEAD：`d2b0e182`（fix2）；版目录 git 状态 `?? production/2026-w47/2026-w47-pt-de/`（未入仓）；
  本次未 commit、未 push、未改生产目录任何文件（收工 SHA 与开工一致，`git status --porcelain` 无修改）。
- SOP：仓库根 `SOP.md` 摘要与仓库 `AGENTS.md` 已读（本次复校在前序 proof1 的完整上下文上进行；
  proof1 的 PROOF-NOTE/GATE-LOG 位于 `scratch-proof-pt-de1/`，作为“旧修复”对照源）。

## §1 run.py + gates.py + render.py（scratch 副本内重跑，生产目录只读）

命令：`rsync` 版目录（除印/网 PDF、`cards/`、`__pycache__`）至 `build-copy/`，其内依次运行
`run.py`、`gates.py`、`render.py`（`run.log` / `gates.log` / `render.log`）。
- run.py：RC=0，`P8 saved, TOTAL exercises: 150`，`TOTAL 150`，`ALL DONE`。
  by level `{'A2': 48, 'B1': 71, 'B2': 31}`；by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；
  by type：Sätze vervollständigen 61 / Multiple Choice 49 / Wortschatz-Zuordnung 12 / Satzbildung 7 /
  Richtig oder falsch 3 / Lückentext mit Auswahl 13 / Übersetzung 4 / Schreiben 1。
- gates.py：16 处 `[PASS]`，`FAILURES: none`，RC=0。
- render.py：RC=0，8 张卡片；重渲印 PDF 12,938,914 B，SHA 与交付印 PDF **逐字节一致**
  （`77243c72c38a14232ea443f03856ccf0a88f3d4b2c0c89e75aa87cf658e6284a`）。
  重建的 8 张 SVG 与交付 SVG 逐字节一致（p1–p8 全部 True）。
- webpdf.py（scratch 副本 svg → `web-rerender.pdf`，`webpdf.log`）：1,147,629 B（与交付网 PDF 同字节数），
  SHA 不同（重渲 `fb94a0e9…` vs 交付 `56eb92d0…`——网 PDF SHA 逐次浮动，为任务预告的预期现象）；
  文字层逐页与交付网 PDF 一致（8/8 页，8,436 词）。交付网 PDF 未被触碰。

## §2 freeze baseline（8/8，两路）+ freeze diff

- 核心 freeze（任务要求：`--build` 指真核心）：
  `tools/freeze.py baseline --build production/2026-w47/core-pt --core-svg production/2026-w47/core-pt/svg --out <scratch>/freeze-core`
  → `freeze-core.log`：`baseline: 8/8 SVGs byte-identical`，核心哈希
  bd87a867 / 0a8300c3 / e3c97081 / f539bdb8 / 51629e93 / a3c3cf38 / 43b845fc / a7b7a661；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`，RC=0。
- 版 freeze：`--build` 版目录、`--core-svg` 版 svg → `freeze-ed.log`：`baseline: 8/8 SVGs byte-identical`，
  f988db96 / 613f558b / c33752e6 / af3e206b / d146ca3d / dd562a7a / 2d53f697 / a4447964
  （与 refanout `de-freeze.log` 逐值一致），RC=0。
- freeze diff（core vs edition，`freeze-diff.log` / `freeze-diff.json`）：RC=0；
  每页 +26…+196 / −22…−752 串；新增 CJK 共 9 个，全部为 U+3000 家具分隔符（P1: 2，其余每页 1）。
- **中断与重起**：第一版驱动（`gates_proof.py`）在 freeze-core 途中静默死亡
  （ps 无进程、`freeze-core/svg/` 为空、无 gates-proof2.json；原因未明，疑似运行时回收——
  同期另有多个 agent 的 freeze/webpdf 在跑）。发现后重起：两次 freeze 各自单独后台跑，
  均完成 RC=0（`freeze-core.log` / `freeze-ed.log`）。快门随后以前台批量重跑（见 §3–§7），全部 RC=0。

## §3 occlusion 审计 — 0 标记（附盲区说明）

命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-pt-de/svg --json <scratch>/occlusion.json`
输出：`{"svgdir": "…/2026-w47-pt-de/svg", "flags": [], "flag_count": 0}`，RC=0。
（本次未重跑 `--selftest`；proof1 已跑过自检阳性对照 6 类全触发，见其 GATE-LOG §2。）
**盲区**：`occlusion_audit.py` 的 BOXTITLE 检查（约 L471–500）只考察带描边或 fill `#2c2822` 的矩形
（`e.attrs.get("stroke") not in (None, "none") or e.attrs.get("fill") == "#2c2822"`）；
奶油框为 `<rect … fill="#f0eee5"/>`（无 stroke 属性，p1-capa.svg 4 框均如此），根本不在检查之列——
故 0 标记不能证明框标题不溢出。D4（§4）即由此漏网。

## §4 框标题横向实测 — D4（四法一致）与 E1/E2

1. `boxtitle_core.py`（PIL advance，4×）：`boxtitle.log:4`：
   `box x=1440..1862 y=1238 title y=1278.4 fs=24.0 … title_w=402.1 right=1863.6 clear=-1.6  <<<< OVERFLOW | 'NESTA EDIÇÃO　In dieser Ausgabe'`。
   其余 30 框标题 advance 余量均为正。
2. 本人独立 PIL 真墨水实测（`boxtitle_ink.py`，svglib `_pil` + `_runs`，anchor 感知；
   `boxtitle-ink.log`）：31 框标题，OVERFLOW 1 处——NESTA 墨迹右缘 1863.5，clear **−1.5**；
   最紧其余：EM POUCAS +0.5、A SEMANA EM NÚMEROS +1.5、P2 `Palmeiras × Flamengo, às` +22.5、
   P4 HINWEIS 框 +24.5。
3. 交付印 PDF 像素实测（`pixel_compare.py` 同法同分辨率 96dpi，1px=1 单位；
   `pixel_boxtitle_pdf.py` 200dpi 复核）：印 PDF：NESTA 墨迹右缘 1864.0（96dpi）/ 1864.8（200dpi），
   超出框缘 1862.0 约 **+2.0 / +2.8**；EM POUCAS 墨迹 1862.0 / 1862.4（约 +0–0.4）；
   A SEMANA EM NÚMEROS 墨迹 1408.3–1409（框缘 1412，余量 +2.9–3）。
   网 PDF 同法：NESTA 墨迹 1864，EM POUCAS 1862（与印 PDF 一致）。
4. 交付印/网 PDF 文字层 span（fitz，单位换算 1 单位 = 0.75pt）：
   `'In dieser Ausgabe'` bbox x1 = **1866.1**（印与网同值）；`'IN KÜRZE'` 1864.0；
   `'In Zahlen'` 1410.3（框缘 1412，在内）。
5. 目视：300dpi 原生裁图 `visual/crop-p1-nesta-pdf300.png`——末字 `e` 完整、横跨奶油框右缘，
   右端约 3 单位在白底上；`visual/crop-p1-poucas-pdf300.png`——末字 `E` 完整、右缘贴框边。
   对照：Cairo 直渲卡片 `cards/p1-capa.png` 同区裁图（`visual/crop-p1-nesta-card.png`）显示
   NESTA 墨迹右缘 1860、余量 +1——即卡片不溢出，只有交付 PDF 溢出（渲染器间约 5 单位宽度差）。
6. 历史对照：第一轮备份 `backup-old/2026-w47-pt-de/svg/p1-capa.svg` 中两标题元素与本版逐字相同
   （`x="1461.5" y="1278.3500000000001" … NESTA EDIÇÃO　In dieser Ausgabe`；
   `y="1914" … EM POUCAS PALAVRAS　IN KÜRZE`）——D4 为既有缺陷，非重建回归。
7. proof1 测量分歧：其 `boxtitle2-proof1.log` 称 NESTA 墨迹右缘 1845.5（+16.5），比上述全部方法窄约 15–18 单位；
   其粗体标题值系统性偏窄（EM POUCAS 1843.5 vs 各法 1861.5–1862.4；A SEMANA EM NÚMEROS 1393.0 vs 1408.3–1410.3），
   而非粗体行（HINWEIS、Newsreader 标题）与各法一致——其方法（脚本未留存）对粗体标题的测量有误。
   字符串来源：`content12.py:89`；德语副标题译自 `tables_de.py:139`（`"本期目录": "In dieser Ausgabe"`）。

## §5 正典 creambox 全版扫描 + diag — 31 框；D1/D2/D3 已修复

命令：正典 `creambox.py svg/*.svg`（`creambox.log`）+ `creambox_diag.py`（`creambox-diag.log`），RC 均为 0。
- 31 框 OWN 真墨余量全部为正，最小 **+2.1**（P2 `Palmeiras–Flamengo-Duell`，墨底 1765.9，框底 1768.0）。
- D1：P1 闪讯框（y=1874，bottom=2348.0）末行 `em Brasília. (Página 4)` 基线 2327.6，
  墨底 2332.6，墨余 **+15.4**（第一轮为框外 +17.6）。修复存活 ✓。
- D2：P3 日程框（y=200，bottom=551.0）末行 `16h30.` 基线 540.6，墨底 540.9，墨余 **+10.1**
  （第一轮为框外 +15.6）。修复存活 ✓。
- D3：P6 时间线框（y=200，bottom=854.0）末行 `Página do Participante.` 基线 840.8，
  墨底 846.0，墨余 **+8.0**（第一轮降部约 +4.8 漫出）。修复存活 ✓。
- 5 处 below-window 负 clearance（−32.0 ×1、−37.0 ×2、−42.0 ×2）均为已知假阳性：
  下块标题/段落（P1 `AGORA VOCÊ…` +37.0、P2 `Atenção:…` +32.0、P3 `UM DIA, DOIS SENTIDOS` +37.0、
  P6 `EXERCÍCIOS　SEITE 6 ÜBUNGEN` +42.0 ×2），creambox-diag 判 owner-rect=NONE。
- 6 处 inside-only desc-clear 负值（−0.3…−1.1）均为误报（`creambox.log:99,156,191,228,237,335`）：
  `schicken Sie sie ein.` ×2、`zwei Sätze und schicken Sie sie ein.`、`2027.`、`Sie sie ein.`、`Kultur.`——
  diag 真墨复测墨迹底 ≈ 基线 +0.2–0.5（无降部字母），墨余 +4.8–5.4，无漫出。
- P7-TOOLBOX 汇总（`creambox.log:361`）：3 框，min inside clearance +5.1，min desc-clear −0.9；
  diag 真墨余量：ERROS +24.6、A PALAVRA +4.8、CARTAS +5.9。

## §6 p8 / keycheck / sweep / gloss

- `tools/p8.py extract --p8 svg/p8-avaliacao.svg --total 150`：`noted set = 150 of 150`，RC=0（`p8-extract.log`）。
- `tools/p8.py compare --core-p8 core-pt/svg/p8-avaliacao.svg --edition-p8 svg/p8-avaliacao.svg --total 150`：
  `status CLEAN, total 150, core 150, edition 150, keydiff [137, 138], missing []`，RC=0（`p8-compare.json` 本体已读）。
- keycheck（`keycheck.log`）：`REG entries: 150; p8extract keys: 150; exact match: 149/150`；
  唯一 MISMATCH：`n=150 page=8 type=Schreiben: key='(offene Aufgabe — Mustertext unten)' extracted='✓'`（预期）。
  附注：keycheck_core.py 将 `keycheck-150.json` 写到其硬编码路径
  `scratch-refanout-pt/keycheck-150.json`（覆盖了 refanout 同名文件；内容为同一确定性结果 149/150，
  未动生产文件）。
- sweep（`sweep.log`）：box-vs-hline flags 0；bridges found 20；bridge orphans **2**；
  bridge widows **0**；RC=0。2 个 orphans 均为 `Ergänzen Sie mit den Wörtern aus dem Kasten.`
  （content34.py:85、content56.py:79），候选坐标 P3/P5 行 1 `(88.0, 2564.45)`、行 2 `Kasten. (538.5, 1696.5)`——
  与第一轮备份 SVG 坐标逐字节相同（proof1 O4，KIT 已注明，核心流式排版行为；链式判定跨栏不断，故计为 orphan；
  P6 的同句加长版 `Kasten: prazo · dia útil · coerência ·` 在同栏连续，完好）。
- gloss（`gloss.log`）：P4 gloss 框 rect#0 x=989.0 y=270.48 w=422.5 h=175.4 bottom=445.88，
  4 行，末行 `pausa die Pause · a taça Pokal.` 右余 +101.5、底余 +42.7；
  `GLOSS VERDICT: lines=4 last-line right clear +101.5 last-line bottom clear +42.7 overflow=no`。
  渲染 `o título Titel`（第 3 行 `decisão das Finale · o título Titel · a`）。

## §7 印/网文字层、字号、孤儿标点、D5 字体

- `pdftotext -layout` 印 vs 网：逐字节一致，111,362 B（`print.txt` / `web.txt`，cmp 通过）。
  fitz 逐页比对：8/8 页 print-bytes == web-bytes（5370/4598/4280/4919/4599/4536/5215/13489）。
- check_final（`check-final.log`）：`pages print=8 web=8`；`words print=8436 web=8436 multiset-diff=0`；
  P8 answer-region span sizes [9.75, 10.5, 14.625, 18.75]，min 9.75。
- minfont（`minfont.log`）：`P8 min effective font size = 9.75 pt (n=380)`；`below 9.75pt: 0`。
- 斜体 span（fitz）：印 1 = 网 1，文本同为 `« consciência »`。
- 孤儿标点：SVG 全部 `<text>` 行首扫描——以 `, . ; : ! ? » ) ] }` 开头或仅为标点的行 **0** 条。
- D5 字体（只记数）：印 PDF 第 5 页内嵌字体子集 **4** 个：
  `NGCYSB+NotoSansCJKsc-Regular`、`UIKPPO+Newsreader16pt-Regular`、`WRUMGD+Newsreader16pt-Regular`、
  `YCHKXS+NotoSansCJKsc-Bold`（3 个字体族）。
- text.md：按行迭代 534 行（KIT 附录称 535 行；refanout `de-gates.json` 亦为 534——计数口径差，非缺陷）；
  范文重数实测 **88 词**；CJK 扫描：除 U+3000 分隔符与 P1 `<title>Lucerna 三色蛾</title>` 元数据外为 0。

## §8 150 题手验与外部事实

- 方法：text.md 全文通读（535 行宣称/534 实测）+ keycheck 机械比对 + P8 目视。
  逐题结论见 PROOF-NOTE（Q73 题干/键适配、Q65、Q83–87 工作日重算、Q120 5 小时、Q137/138 德语、范文 88 词等）。
- Q125 外部事实（36ª rodada Palmeiras × Flamengo，周六 21/11 16h30，Nubank Parque）：
  proof1 已用 CBF 赛程外部核实（brasileirao.com.br 2026-11-07、colunadofla.com 2026-11-06、
  portaldopalestra.com.br 2026-11-01、sportradar 赛程页），本次未重复外部核查，结论沿用 proof1。
- 其余事实（Zumbi/Lei nº 14.759、Enem Edital nº 64/2026、半决赛比分）为核心冻结内容，
  以核心 KIT 来源为准，本次未逐项重查外部来源（与 proof1 同口径）。

## §9 Hand-patch 盘点复验（de-classify.json）

- `de-classify.json`：24 KEEP（bslib4 9、content12 11、content34 2、content56 1、content8 1），
  0 REVERT / 0 MERGE / 0 INSERT / 0 DELETE。
- 抽查 5 项（均存活，见 PROOF-NOTE）：content12.py:138（474 vs 备份 436）、
  content34.py:134（`Titel` vs 备份 `Meister`）、content34.py:40（+58 vs +32）、
  content56.py:132（654 vs 640）、content8.py:110（max_w=395，备份无）。
  fix1 标记：本版各文件有，备份为 0。`tables_de.py:39` `"冠军": "Meister"` 未动，
  `:40` `"冠军头衔": "Titel"`、`:41` `"墨底": "Tintenunterkante"` 在位。

## §10 目视（印 PDF 渲染，130dpi，`visual/p-1.png`…`p-8.png`）

- P1：D1 修复目视在框内；NESTA 标题贴框右缘（D4，见 §4 裁图）；EM POUCAS 标题贴框右缘（E1）；
  其余刊头、头条、数字框、日程框、quiz 均干净。
- P2：日程标题 `Drei freie Tage, eine Woche geplant` 止于右缘（O3，墨迹 1860）；四格日程框干净；
  `Kasten.` 孤字（O4）与 P3 同。
- P3：D2 修复目视在框内（`16h30.` 在框内）；`Kasten.` 孤字 + `B AS PALAVRAS DO TEXTO` 栏目标题落栏底（O4）。
- P4：gloss 框 `o título Titel` 4 行在框内；赛程表、注、练习 A–D 干净；`B AS PALAVRAS` 栏目标题落栏底（O4）。
- P5：Q73 题干 `Depois da prova, começa a ___.` 目视与 P5 正文原句一致；照片+出处干净；
  `Kasten.` 孤字（O4）；中部留白为版式固有（同 P3）。
- P6：D3 修复目视在框内（`JAN. 2027 … Página do Participante.` 在框内）；图表柱 10 天 : 5 天 = 2:1；
  D 节桥接 `Kasten: prazo · dia útil · coerência · chute` 同栏连续、完好。
- P7：三栏语法、ERROS COMUNS、A PALAVRA、CARTAS、Os Lusíadas 图、FRASES DA SEMANA（8 句 verbatim，
  含 `(wörtlich aus dieser Ausgabe)`）、VOL.5 预告栏均干净。
- P8：A–H 节 113–150 齐全；RESPOSTAS 键（含 `150. ✓ Siehe den Mustertext… (88 Wörter)`）干净；
  Mané Garrincha 照片+出处干净；无重叠可见。

## 附：输出文件（本 scratch 目录）

- `PROOF-NOTE.md`（结论 (b) + 缺陷 D4 + 边缘 E1/E2 + 旧修复复验表）
- `GATE-LOG.md`（本文件）
- `gates_proof.py`（第一版驱动；中途静默死亡，见 §2——其 run/gates/render/webpdf 四步日志仍有效：
  `run.log`、`gates.log`、`render.log`、`webpdf.log`）
- `run.log`、`gates.log`、`render.log`、`webpdf.log`、`freeze-core.log`、`freeze-ed.log`、
  `freeze-diff.log` + `freeze-diff.json`、`occlusion.log` + `occlusion.json`、`p8-extract.log` +
  `p8-extract.json`、`p8-compare.log` + `p8-compare.json`、`creambox.log`、`creambox-diag.log`、
  `boxtitle.log`、`boxtitle-ink.log` + `boxtitle_ink.py`、`keycheck.log`、`sweep.log`、
  `print.txt`、`web.txt`、`minfont.log`、`check-final.log`、`gloss.log`
- `pixel_boxtitle.py`、`pixel_boxtitle_pdf.py`、`pixel_compare.py`、`probe_bridge.py`、
  `web-rerender.pdf`（scratch 重渲网 PDF；交付网 PDF 未动）
- `visual/`（`p-1.png`…`p-8.png`、`contact.png`、`contact-half.png`、
  `crop-p1-nesta-pdf.png`、`crop-p1-nesta-card.png`、`crop-p1-nesta-pdf300.png`、
  `crop-p1-poucas-pdf300.png`）
- `build-copy/`（版源码 scratch 副本：run/gates/render 重跑地；内含重渲印 PDF，与交付逐字节一致）
- `freeze-core/`、`freeze-pt-de/`（freeze baseline 工作区）
- `probe-write.txt`、`tmp/`
