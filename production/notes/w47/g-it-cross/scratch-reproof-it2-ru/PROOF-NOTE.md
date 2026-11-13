# 复校结论：(a) 零缺陷可定稿

**版本**：2026-w47-it-ru（意大利语目标语 × 俄语读者，VOL.4），core D-2 fix 后重扩散（refanout-it2）的新版全量复校（SOP §8.4）。
**复校员**：独立复校（scratch-reproof-it2-ru；与重扩散员不同人）。只读生产，未 commit、未 push，未重渲染交付的 web PDF，未写生产目录任何文件（收工重验三 SHA 与开工值逐字一致）。
**开工探针**：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 内真实写文件通过。解释器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）；`TMPDIR=<scratch>/tmp`，未写系统 /tmp。
**已读**：`~/workspace/weekly-git/SOP.md` §8、§1.1 全文；`scratch-refanout-it2/FANOUT-REPORT-it2.md` 全文；`scratch-reproof-it-ru1/PROOF-NOTE.md`（re-proof (b)）；`scratch-fix-it-ru1/FIX-LOG.md`（fix1）；`scratch-fix-core-it-d2/FIX-LOG.md`（D-2）；`~/workspace/weekly-git/AGENTS.md`。

## SHA 核对（开工前实测，与任务给定值逐字节一致；收工重验 unchanged）

| 文件 | 字节数 | SHA-256（实测） | 对照 |
|---|---|---|---|
| La-Lucerna-VOL4-RU.pdf（印刷） | 14,180,915 | 966a9d10c033ed0297cef6d018b23a548dec2b016bc0eb3ecf61440ac2247666 | 全对 |
| La-Lucerna-VOL4-RU-web.pdf（网页） | 1,441,240 | db22fa31244bb4fe0a7649660a621aa15da22cda010eaad4fd0ff9e619ed0505 | 全对 |
| 2026-w47-it-ru.text.md | 67,731 | 47c0471515d3b249855e33a290d0c4259ecce431995db45ac0ce926cf5a52b1d | 全对 |

重扩散前生产三 SHA（`scratch-refanout-it2/shas-pre.txt`）核对一致：印 `af980e26…df6200` / 网 `3e10d785…52cc9` / 文 `8a49ce37…c895c`（备份目录三文件 SHA 逐字相符）。

## A. D-2 回归：干净（逐项独立重测）

- **新串各就其位**：`Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.` 在 content7.py:17、p7 SVG、text.md:775、印/网 PDF P7 文字层各 ×1；`Il verbo è leggere, regolare al futuro: leggerò.` 在 content7.py:18、p7 SVG、text.md:777、印/网 PDF P7 文字层各 ×1。content7.py L17/L18 与 core-it 逐字相同。
  - 注：PDF 文字层箭头粘词（`→assaggerò,`、`guardare→`）+ 换行断句，须先空白折叠再箭头归一化（`\s*→\s*` → `→`）后计数方为 ×1；SVG 须按文本节点加空格拼接后计数（节点按行断开）。直接整串 grep 会误报 0——本次初版计数即因此误报 0，后以归一化方法重测纠正（`check_ab2.log` / `check_ab3.log`）。
- **旧串全版清零**：`Le forme sono regolari: andare` 与 `irregolare al futuro: leggerò` 在 content7.py、8 个 SVG、text.md、印/网 PDF 文字层均为 0。`andare` 一词仍在 P7 出现 1 次，仅在 Q101 题干 `(andare)` 原形提示中，与旧串无关。
- **只许 P7 变化**：与备份旧版逐项 diff——SVG 仅 p7 不同（p1–p6/p8 逐字节一致）、cards 仅 p7 不同、text.md diff 恰为 (774,775) 与 (776,777) 两处 replace（difflib 并为一个 774–777 区间，内容即两行）、content diff 恰为 content7.py L17/L18 两行、text.md 恰 −21 字节（67,752 → 67,731）。两 PDF 因 P7 重建而变。
- **P7 教学段语义逐句事实核查（独立检索，不抄前人结论）**：
  1. 新 L17 只举 assaggiare / guardare 为规则形——正确：assaggiare、guardare 的未来时为规则构形（-ciare/-giare 去 i 为拼写规则，不是不规则；FlexiClasses 规则表列 LEGGERE 为规则 -ere 例，FluentU 列 -ciare/-giare 去 i 为规则拼写调整）。andare 已从规则例中删去——正确：andare → andrò 属元音脱落型不规则未来时（规则形应为 *anderò*），FluentU / FlexiClasses / Rosetta Stone / Dolce Vita 四源一致列 andare → andr- 为不规则未来时词干（"Wrong: andarò → Correct: andrò"）。
  2. 新 L18「Il verbo è leggere, regolare al futuro: leggerò.」——正确：leggere 未来时规则（FlexiClasses 规则动词表：LEGGERE → io leggerò）；leggere 的不规则处只在远过去时 lessi 与过去分词 letto，不在未来时。
  3. 指涉不悬空：L17 首句仍提 andremo/assaggeremo/guarderemo（只作未来时用法举例，不作规则性断言）；L18 前句仍提 `leggeremo a BookCity`；桥接句 `Говорите о планах в будущем времени: andremo, assaggeremo, guarderemo, leggeremo.` 未动。全文 `regolar` 仅此两处（grep 全文 = 2）。
  4. Q101–103 键 andremo / assaggeremo / guarderemo、Q104 键 B 不变；Q104 键注无规则性断言。P7 其余教学句复核正确：B1 passato prossimo（è partito / è finita，avere 分词不变）、B2 congiuntivo（piova / nevichi / leggano；so che + 直陈式 torna）、ERRORI TIPICI 四例改正全对。

## B. D-1 回归：干净（逐项独立重测）

- 旧形「налоговая ставка」全版 0 次：text.md 0、8 个 SVG 平文（去标签 + 空白折叠）0、印/网 PDF 文字层各 0（pdftotext grep 0）。
- 新形「ступень налоговой шкалы」text.md 恰 5 处各就其位：:663（P6 NOTE gloss）、:763（Q100 注）、:987（Q144 注）、:1217（P8 key 100）、:1305（P8 key 144）——与 fix1 位置逐字一致。渲染层 3 处：SVG p6 ×1、p8 ×2；印/网 PDF 文字层各 3 处（P6 ×1、P8 ×2）。
- **P8 key 100 / 144（交付印 PDF 词框实测，0.75 缩放）**：key 100 单行，右缘 1001.1 pt = 1334.8 SVG 单位，栏（col3，右缘 1411.5）余 **+76.7 SVG px**；key 144 单行，右缘 1311.3 pt = 1748.4 SVG 单位，栏（col4，右缘 1862.0）余 **+113.6 SVG px**。两值与 re-proof (b) 实测（76.7 / 113.6）逐字一致，远高于 +5px 底线。200 dpi 渲染目视（`render-p8.png`）：两行均为单行、栏内、无换行、无溢出。
- **P6 NOTE 注释盒**：SVG 盒 x=538.5 y=1102.4 w=422.5 h=264.575；注释 7 行基线 y=1140.9/1170.6/1200.3/1230.1/1259.8/1289.5/1319.2 全部在盒内（上沿余 38.5、下沿余 47.8 SVG px）；PDF 渲染词框：盒内词最右 x1=708.0 pt = 944.0 SVG，盒右缘 961.0，余 +17.0 SVG px；最末行 `процедура.` 在盒内。200 dpi 渲染目视（`render-p6.png`）：7 行完整，「ступень налоговой шкалы」在第 6 行完整可见。

## 其余复校结果（全文通读 1317 行 + 门禁，皆通过）

- **门禁 20/20 全过**（详见 GATE-LOG.md，`gates-ru-raw.log`）：occlusion 0 flags；p8 extract 150/150；p8 compare CLEAN，keydiff 恰为 [137, 138, 139]（预期的重定向读者句键）；freeze diff P1–7 无未解释增减；strict-CJK 除 U+3000 外 0；印/网 PDF 文字层多重集一致（各 7,587 词，较修前 7,590 恰 −3，即删去的 `andare`、`→`、`andrò,` 三词）；web PDF 1,441,240 B < 7 MB；P8 最小字号 13.0 px = 9.75 pt（SOP §1.1 下限，恰达下限）；§1.1 扫描通过；text.md validate 0/0；150 键与注释与核心/翻译表一致（`pdftotext` 印/网字节亦逐字节相同，`cmp` rc=0，各 6,112 词按 pdftotext 分词）。
- **freeze baseline 重建：8/8**（`freeze-baseline.log`）：`--build` 指 `production/2026-w47/core-it`（build-copy 核实确为 core-it 自身：其 content7.py 与 core-it 仅 OUT 路径行不同，L17/L18 为 D-2 新串；与本版 content7.py 的 diff 含 band/bridge 本地化行，证非 edition 冒充）；`--core-svg` 指 core-it 的 `svg/` 子目录；P7 核心 `a7e6afa4…` 精确复现，其余 7 页与改前字节一致；发货核心 SVG 运行前后重哈希无变化。
- **全文通读 1317 行**：150 题键逐题核对与题干一致（题号连续：单号 138 项 + 3 个区间头 25–28 / 52–55 / 141–144 = 150）；事实与数字自洽——积分榜 29/28/27/24/23/5、24 球/10 场（10 场比分逐场加总 3+1+2+3+3+2+3+1+2+4=24 ✓；比分表与正文逐场一致）、BookCity 15 届/1360 活动/2487 人/1164 书/443 场地、Torrone 29 届 7–22 日 = 16 天/三周末、Eurochocolate 32 届、Torino Film Festival 44 届 11 月 24 日–12 月 2 日 = 9 天、图表题算术 13−11=2、6+7=13、样文 99 词与所称 99 词一致（实测 99）；星期全验（`TZ=Europe/Rome date -d`）：12 日周四、15 日周日、16 日周一、17 日周二、19 日周四、20 日周五、21 日周六、22 日周日、23 日周一、24 日周二，与文中星期称谓逐一相符；Madonna della Salute（1630 誓愿、Longhena、1631–1687 建堂）、植树节（1898 始、2013 年立法）、Sforza–Visconti 婚礼 1441 年 10 月 25 日等史实与正文一致；P6 时间线（28 OTT / 9–12 NOV / 17 NOV 18:00 / 31 DIC）与正文一致；Q140 键在核心与本版同为意大利语 «Ogni cifra deve essere chiara.»，为正确行为，未动。
- **8 金句逐字核对**：8 句在正文中各出现 1 次、在 P7 FRASI DELLA SETTIMANA 列表中各出现 1 次（全文 grep 各 ×2），逐字一致，页码标注（P1/P1/P2/P3/P4/P5/P6/P6）与出处页相符。
- **8 页逐页目视交付印 PDF（200 dpi 渲染，`render-p1.png`–`render-p8.png`）**：无溢出、无重叠、无裁切、无豆腐、无压页脚；P3/P5 中段结构留白为核心既有模式；P1/P2 标题越框见观察项 O1；P7 两条 D-2 新句渲染干净，Q101–104 完好；P8 答案区末行未侵页脚带。
- **盒标题横向溢出专项（STRADDLE 规则，备份旧版对照已跑）**：occlusion 审计 0 flags（含 BOXTITLE 类）；除 O1/O2 外无其他框题溢出。

## 观察项（不是缺陷，不拦定稿）

- **O1（P1/P2 双语小标题越无边框 cream 框，沿用观察项，与备份逐字节相同）**：P1 标题 `НЕДЕЛЯ В ЦИФРАХ` 墨水右缘 1066.6 SVG 单位，越框（右缘 961.0）105.6 px；P2 `ЗАПОМНИТЕ` 右缘 1022.7，越框 61.7 px。实测：live 与备份印 PDF 词框逐字相同（P1 x1=800.0 pt、P2 x1=767.0 pt，新旧一致）；框无边框、无字形被裁、无墨水与他物/可见边框重叠；occlusion 审计 0 flags。非回归，本轮未动（p1/p2 SVG 与备份逐字节一致）。
- **O2（混合语种空格偏窄，旧版同款，非回归）**：少数拉丁↔西里尔边界处的独立空格节点渲染偏窄（墨水间隙约 2.2 SVG 单位，正常词间约 4.8），如 P8 key 104「глагола leggere」、106「vedere с」、108「finire с」；pdftotext 合并词 22 个。备份印 PDF 实测完全相同（与 re-proof (b) 一致），属 svglib 按语种分段 + CJK 空格节点的全系旧有表现。词仍可辨读，不拦。

## 缺陷清单

无。本轮全量复校零缺陷，结论 (a) 可定稿。

## 交付文件（本 scratch 内）

- `PROOF-NOTE.md`（本文件）
- `GATE-LOG.md`（每项门禁结果 + 实测值）
- 证据：`gates-ru-raw.log`、`freeze-baseline.log`、`check_ab.log`、`check_ab2.log`、`check_ab3.log`、`measure-p6p8.log`、`measure-p6p8b.log`、`print.txt`、`web.txt`、`freeze-baseline/`、`core-svg-sha-pre.txt`、`core-svg-sha-post.txt`、`render-p1.png`–`render-p8.png`、`ru/p8-extract.json`、`ru/p8-compare.json`
