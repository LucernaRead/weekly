# GATE-LOG — 2026-W47 zh-cn-es 独立校对（proof1）

- 版：`production/2026-w47/2026-w47-zh-cn-es/`；核心对照 `production/2026-w47/core-zh-cn/`
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）
- 本文件只记实测值；结论与缺陷清单见 `PROOF-NOTE.md`。
- 全部中间文件在本 scratch 内；生产目录开工/收工 SHA + mtime 均未变。

## §0 成品身份（开工 + 收工两次，全串一致）

| 成品 | 字节 | SHA-256 |
|---|---|---|
| 印 `Lucerna-VOL4-ES.pdf` | 44,799,104 | `f05d6126a7f55564787be64e370de7ce05ade6abb38b18fbecc9cb2d070a2508` |
| 网 `Lucerna-VOL4-ES-web.pdf` | 2,723,559 | `249ee578617c1c584f11ef2436d2438a41cf8c8b10b3e24baf3ff45b8396d437` |
| 文 `2026-w47-zh-cn-es.text.md` | 51,175 | `edc045da1f0cc5267ec18046a193e055dfbf90e70421d79bcf0ba93f2497f482` |

生产 SVG 开工 SHA（`prod-svg.sha256`，收工复验一致）：
p1 `64433b2d9eaa56194775a998afcf368dd562775d821efcaedd7e7a5c679f0b38`、p2 `6f972b4abd2f2236c06ed5dbf9444fa77256279a7ac25d7e2ebde7d78004cb2e`、p3 `d334d26867cd92693685b6f5c74e5bacd48ddf08ead5d80b0e17d3a11c8e477a`、p4 `7ef5a3c50ec309eb5bf4d42f40b7310af31f8d5894b8a6181652ce47435ff12f`、p5 `38c91b519b497ba91b9c35aa818b67b95806a055b5e7ccb522d73179b3b2729a`、p6 `1eb9d4748958517f0205e08d4b94c7c211ba312a74265b173e36bd63cda94a5d`、p7 `f9599e4d9fd4fd19a01564526ab99f1caee85c0c0ed9503f6fa789d54eb8232a`、p8 `5e71ed40e247f53710dc44b88367247952f5af42c41dbc73f52f21ec91a0a649`。

## §1 run.py 重建（`run-es.log`，scratch 副本，OUT 已重定向）

- rc=0，TOTAL 150；by level A2 56 / B1 69 / B2 25；by page {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}；by type {完成句子 68, 单选 50, 词汇配对 20, 完形单选 11, 写作 1}
- `OVERFLOW`/`TOO WIDE` 命中 0 行
- 重建 SVG 与现盘 8/8 sha256 字节一致（逐页 OK，见 `run-es.log` 末尾核对输出）
- `gates.log` 内同一重建（gates-zhcn 副本）：`freeze_sha256: run rc=0 match=8/8`

## §2 freeze（`freeze-baseline.log` / `freeze-diff.log` / `freeze-diff.json`）

- baseline（核心）：rc=0，`baseline: 8/8 SVGs byte-identical`；核心完整性：`shipped core SVGs unchanged by the run (8 files re-hashed)`
  - p1 `6685c71a…`、p2 `70a22dc6…`、p3 `1386ba27…`、p4 `0d9b8ed7…`、p5 `a0c0ae12…`、p6 `40db68d1…`、p7 `c6752fe2…`、p8 `ce8692e2…`（全串见日志）
- diff `--strict-cjk`：rc=0，TOTAL added CJK **0**
  - p1 +45/−45，CJK 886→870，added 0；p2 +52/−52，1065→1060，0；p3 +39/−39，864→859，0；p4 +42/−42，772→767，0
  - p5 +38/−37，969→964，0；p6 +42/−41，912→907，0；p7 +106/−103，753→742，0；p8 +207/−213，1125→1118，0
  - 删 CJK 712 字核对：全部是讲解层/家具/注释串（`Notes｜…` 各版 gloss、`头条 Top story`、`练习 Exercises` 双语栏头、页脚 `Lucerna 简体中文周报 VOL.4 …`、P7 英语讲解栏碎片）与范文重分段（同一 138 字、不同换行切分）；无题干中文被删。题干 CJK 另经 REG 对齐核对 150/150 一致（§7）。

## §3 机械门禁 11/11（`gates.log`，gates-zhcn 副本自跑）

```
[PASS] occlusion: rc=0 flags=0 svg/: 0 flags
[PASS] img_overlap: hits=0
[PASS] p8_extract: rc=0 noted=150/150
[PASS] p8_compare: rc=0 verdict=CLEAN keydiffs=0
[PASS] freeze_sha256: run rc=0 match=8/8
[PASS] print_web_text: pages 8/8 posdiff=0 msdiff=0 P1:390/390:pos0:ms0 P2:369/369:pos0:ms0 P3:285/285:pos0:ms0 P4:357/357:pos0:ms0 P5:290/290:pos0:ms0 P6:354/354:pos0:ms0 P7:556/556:pos0:ms0 P8:1895/1895:pos0:ms0
[PASS] pdftotext_nonempty: print=45062B web=45062B web_size=2723559
[PASS] p8_fontsize: answer-zone min=9.98pt median=9.98pt spans=365
[PASS] p8_chips: core={'A2': 11, 'B1': 24, 'B2': 3} edition={'A2': 11, 'B1': 24, 'B2': 3}
[PASS] u2019: files_with_U+2019=[]
[PASS] s11_svg: off-palette={} gold/old=False stroked_rects=0 VOL.5=1(core 1) paper_fills=8
OVERALL: ALL PASS
```

独立再跑（`occlusion.log` / `p8-extract.log` / `p8-compare.log`）：occlusion rc=0，`selftest OK`（6 类阳性全触发，干净对照静默），`0 flags`；p8 extract `noted set = 150 of 150`；p8 compare `status: CLEAN missing=[] extra_count=0 uncertain=[] keydiff=[]`（core 150 noted / edition 150 noted）。

## §4 盒标题真墨横扫（`sweep.py` → `sweep.json`；核心对照 `sweep-core.json`）

方法：复用 `occlusion_audit.py` 解析与真墨度量；容器 = 全部 rect（含纯填充奶油盒 `#f0eee5`，BOXTITLE 不认此类）；每容器取顶行标题墨右缘与盒右缘之差。

- es：pages 8，flags **3**，title-rows 179
  - `BOX_OVERFLOW p2-shenghuo.svg '本周生活小日历　Fechas de la semana' right ink 1422.8 > edge 1411.5`（D-1）
  - `BOX_OVERFLOW p4-tiyu.svg '看比赛的中文　Palabras de los partidos' right ink 1911.2 > edge 1862.0`（D-2）
  - `BOX_OVERFLOW p5-qingnian.svg '这一周的高频词　Palabras de la semana' right ink 992.0 > edge 961.0`（D-3）
  - BASELINE_OUTSIDE 0、EDGE 0、IMG_OVERLAP 0；其余标题最小正余量 +17.8 px
- core：flags **0**；同位标题余量 P2 +22.0、P4 +82.2、P5 +12.5；最小标题余量 +12.5 px
- P1 重点：数字盒标题墨右缘 936.8，余 +24.2 px；截稿行 `Cierre: 10 nov. — la final aún no jugada` 墨右缘 1801.8，余 +60.2 px（核心 +56.5）——两处均通过（`pressline.py`）

## §5 孤儿标点扫描（全 8 版，行首收口标点；核心同法对照）

- es：仅 1 处——P8 y=912.4，行首 `》`（`》，故事很有意思。星期日是小雪，天气更冷了，我`），即 D-4
- core：0 处
- 成因已核实：`content8.py:104` 前缀 `Respuesta modelo: ` 比核心 `Model answer: ` 长，范文段（`content8.py:96–99`，138 字，与核心逐字同）重排致 `《试探》` 右书名号落行首；渲染对照 `flag4-p8-essay-orphan.png` vs `core-p8-essay.png`

## §6 P4 gloss（西班牙语前缀实测）

- 前缀 `Notas｜`（`bslib4.py:207`，`tr_es.py:13` 的 `译注｜` 值）
- 框 `[538.5, 557.4, 961.0, 792.2]` `#f0eee5`；行数 **6**，基线 595.9 / 625.6 / 655.3 / 685.0 / 714.8 / 744.5；墨底 749.7，框底 792.2；其下首行墨顶 801.9——不盖任何文字；与核心几何全同（同框、同基线、同墨底）

## §7 150 题手验（`reg-es.json` / `reg-core.json` / `verify-150.txt` / `keycheck-150.json`）

- REG：es 150 = core 150；level/page/type 逐项一致；ex 130 条、match 5 组
- 题干：对齐后（ex 指针只在非配对题推进；印出题号与 REG 号 0 错位，130/130 消费完毕）CJK 逐字一致 **150/150**；非 CJK 差异只在题型指令译文（`[Fill in the blank]`→`[Completa la frase]`、`[Match the words]`→`[Empareja las palabras]`）
- 键：REG 键 es vs core **150/150 一致**；注文 149/150 为西语译文，仅 Q80 `悬疑 = suspense, b` 与核心同形（`suspense` 本就是西语词）
- 印出键：p8 extract keys 三方全同（core == es，150/150，含 Q150 `✓`）；keycheck REG vs 印出 **149/150**，仅 Q150 不同（REG `(开放题，范文如下)` vs 印出 `✓`，设计内差异；脚本 rc=1 为其 Q150 预期分支不适用，见 PROOF-NOTE 记录项 2）
- 词汇配对 20 项：印出字母顺序逐组核对——P2 a/b/c/d、P3 b/d/a/c、P4 d/b/c/a、P5 c/b/d/a、P6 c/d/a/b，全部与源码 `match_set` 数组一致
- Q150 范文：138 字实测 138 字符，与核心范文逐字一致；P8 印出 `150. ✓ Tarea abierta — modelo arriba, sección F (138 caracteres).`
- 键-题干契合：150 条逐条读过，无错配（事实键均对过正文/注文：三支韩国队、139.38/7.77、320−80=240、赛程 4/5/6/7、五部电影日期与主演、半决赛早上 6 点、Q113–120 对错、小林短文顺序）

## §8 修复点复验（重建报告 12 处声称）

| 声称 | 实测 | 结果 |
|---|---|---|
| P4 头 `Leer el calendario` | 墨右缘 898.8，单行 | 存活 |
| P8 头 `Leer, responder` | 墨右缘 1406.8，单行 | 存活 |
| P5 头 `Horas y números` 合 | 墨右缘 936.5，单行 | 存活 |
| P7 teaser（lcn 减 1 行） | 预告带底 2588.8 < 2596（余 7.2）；末行墨底 2559.0 | 存活 |
| P4 gloss 7→6 行 | 西语前缀实测 6 行，框底 792.2（§6） | 存活 |
| P2 日历标题 `Fechas de la semana` | 距山谷照确有空隙，但墨 1422.8 越盒边 1411.5（D-1） | **未遂** |
| P8 注 7 值改 1 行（Q13/17/18/20/24/109/150） | keys 区墨底最高 2539.6 < 2596（余 56.4）；与报告 2475.7 差 63.9 px，量法不同， verdict 同为通过 | 存活 |
| P2 词卡例句 1 行 | 4 句均为 1 行，墨底 ≤1756.8 < 卡底 1768.0 | 存活 |
| P2 词卡其余 | 同上 | 存活 |

## §9 D4/D5（印 PDF 全文计数，es = 核心）

`全球总决赛的BO5` 2 / `第一次在BO5里打赢` 0 / `GEN在S16一场没输` 2 / `GEN今年一局没输` 0 / `只丢了一小局` 2（P1 分行 + P4 整串；pdftotext 直数 1 为分行假象）/ `淘汰赛一局没输` 1 / `next Sunday` 0（印/网 PDF 与 .text.md 两版皆 0）。
Q56 题干含限定；P8 键 56 注文：`56. T1 — BLG venció a T1 por primera vez en un BO5 de Worlds.`

## §10 引号 / 禁词 / 繁体 / ABSTRACT / badge

- 引号：文 《》63/63、`“”`2/2、`«»`6/6；SVG 《》49/49、`“”`2/2、`«»`5/5；U+2019 0
- 禁词/占位：`TBD`/`XXX`/`TODO`/`Lorem`/`placeholder`/`占位`/`待写`/`乌克兰`/`战争` 均为 0（SVG 已剔 base64 图数据后计）
- opencc t2s：全版（文 + 8 SVG）繁体残留 0
- ABSTRACT.txt：335 B，末字节 `\n` 在位；西语，含刊名、目标语名、A2–B2、150 题与真实主题（S16 决赛、双 11、小雪、深圳读书月、《试探》）
- badge：P1 `TEXTO CHINO　EXPLICACIONES EN ESPAÑOL`，拉丁-only，无汉字
- .text.md：编号题 1–150 齐全，无缺失

## §11 目视（印 PDF 110 dpi，`vis-p1.png` … `vis-p8.png`）

8 版全读过。除 D-1 ~ D-4 外未见重叠、裁切、缺图、压页脚；P3/P6 自 transform 起未动，目视干净。P7 预告带距页脚线 7.2 px（紧但通过）；P8 keys 区距页脚线 56.4 px。
