# GATE-LOG — W47 ru-ja 第二轮独立复校（re-fanout 重建版）

- 校对员：proof1；日期 2026-11-11；对象 `production/2026-w47/2026-w47-ru-ja/`。
- 全部工具均为 repo `tools/` 共享工具（`tools/venv/bin/python`，Pillow 13.0.0 / FreeType 2.14.3）或 `hidden_files/w47/tools/` canonical 工具（creambox.py）或首轮复校同款扫描脚本（`boxtitle/boxright/colspill/pixel_verify`，原样复用）；`check_core.py` / `s11_check.py` / `adjudicate_ru.py` 为版内与 fanout 共用脚本。本版无 `verify_ed.py`（仅 en 家族有），以 check_core + s11_check + keycheck + p8 compare 等效覆盖。
- 除特别注明外，所有门均在 scratch 副本或对交付文件只读运行；生产目录零写入（收工 44 文件 SHA 与开工快照一致）。
- 各门日志：`logs/` 下 `run.log`、`check_core.log`、`p8-extract.log`、`p8-compare.log`、`ru-ja-p8.json`、`ru-ja-p8-compare.json`、`occlusion-selftest.log`、`occlusion-audit.log`、`ru-ja-occlusion.json`、`adjudicate.log`、`freeze-core.log`、`freeze-edition.log`、`freeze-diff.log`、`freeze-diff.json`、`s11.log`、`creambox.log`、`boxtitle.log`、`boxright.log`、`colspill.log`、`pixel_verify.log`、`kicker.log`、`d1d2d6.log`、`keycheck.log`、`sweeps.log`、`webpdf-rebuild.log`、`print.txt`/`web.txt`、`prod-sha-before.txt`/`prod-sha-after.txt`。

## §0 三 SHA（开工核对）

| 成品 | 字节 | SHA-256 |
|---|---|---|
| 印 PDF `Lucerna-VOL4-ru-ja.pdf` | 27,409,704 | `150f970828142d50cc10ba157182dd282c22dd74d82de5f7c932141d86cda0a3` |
| 网 PDF `Lucerna-VOL4-ru-ja-web.pdf` | 3,721,635 | `57cf6b07ba4fc83404848cd43f2dc1c08304255ef94dae0e3ec359203bc7b67d` |
| 文 `2026-w47-ru-ja.text.md` | 64,514 | `c17ff1877155c5155e55ea43eec43dee516d133ec456817bb7549c23d17ea840` |

与协调员盘核值逐一一致。印/网 PDF 各 8 页（`pdfinfo`），网 PDF < 7 MB。

## §1 run.py（scratch 副本 `build/2026-w47-ru-ja`）

- rc=0，TOTAL **150**；by level A2 50 / B1 76 / B2 24；by page 1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38；by type 空所補充 54 / 選択 55 / 語と意味を結ぶ 20 / 組み合わせ 12 / 書きかえ 4 / 翻訳 4 / 作文 1；model words 97。
- FLOW OVERFLOW / HEAD TOO WIDE：0。
- Morozko 图 SKIPPED（`col 3 y 2203.08`，按构建条件，依设计，与首轮一致）。
- 重生 SVG 与交付 SVG **8/8 逐字节一致**（`logs/copy-svg.sha` vs `logs/prod-svg.sha`，diff 为空）。

## §2 D1 / D2 / D6 / kicker（独立量测，日志 `logs/d1d2d6.log`、`logs/kicker.log`）

- D1 web 斜体：`pdffonts` 交付网 PDF 含 `LucernaNotoSerif-Italic`（UGYISX+）与 `LucernaNewsreader-Italic`（USKPKN+），子集化嵌入；网 P1 文字层 `чёрная пятница` 带空格（`чёрнаяпятница` 0 次）；200 dpi 裁图 `render/crop-web-wordbox.png` 肉眼确认斜体 + `»` 紧贴。
- D1 四串在 SVG：K1 图标题 ✓、K2 免责声明 ✓（P6 SVG 专有，text.md 中无，依设计）、K3 P7 副标题 ✓、K4 P8 副标题 ✓；text.md 分段 L459 / L504 / L596 ✓。
- D1 三头墨水右缘：P6 图标题 998.0（余 952.0px）、P7 副标题 1832.0（余 118.0px）、P8 副标题 1832.1（余 117.9px）。
- Kicker：`content12.py:18` 9 处双空格；PIL 间隙 `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`，最小 **5.9px ≥ 4.0px**（10 词 + 尾逗号拆出，与报告逐值一致）。
- D2：Q25 选项 text.md L187 `17 ноября — День студента (key b · 学生の日 b)`；全称 `Международный день студента` text.md ×2 = core ×2。
- D6：`желании` text.md ×2（L173、L694）；p8 key 20 = `желании` = core `ru-p8.json`。

## §3 check_core.py（rc=0）

- GOLDEN: 8（每句 ×2，P1×2、P2×1、P3×1、P4×1、P5×1、P6×2）；golden BAD **0**；gloss fails **0**；P8 svg text chars 8475。
- orphan line-starts 4：`(p7-yazyk.svg, 553, '”».')`、`(p7-yazyk.svg, 756, '：')`、`(p7-yazyk.svg, 756, '。')`、`(p7-yazyk.svg, 940, '。')`——CJK 标点行首类，非缺陷。
- same-baseline collisions 1：`(p1-pervaya.svg, 1712, 'чёрная', ' ')`，与 core 同款。

## §4 p8（`logs/ru-ja-p8.json`、`logs/ru-ja-p8-compare.json` 本体已读）

- extract：noted set **150 of 150**，rc=0。
- compare：`status: CLEAN`，core 150 / edition 150，missing=[]、extra_count=0、uncertain=[]，**keydiff=[137, 138, 139, 140]**，rc=0。
- 直接 keydiff vs core `ru-p8.json`：恰 [137, 138, 139, 140]（137 `11月17日（火）、学生の日。`、138 `荷物は追跡し、受け取り、確認すること。`、139 `火曜、ロシアはベネズエラと対戦する。`、140 `みなさん、学生の日おめでとう！`——E 节日语译键，依设计）。

## §5 150 题 key 手验（`tools/keycheck.py`，`logs/keycheck.log`）

- 行内键 150/150、答案附录键 150/150、印 P8 键 150/150；行内 vs 附录 0 差异；行内 vs 印 P8 0 差异（Q150 除外：印键 `✓`，依设计）。
- 配对组逐一对 SVG 选项表核实：25–28 b/d/c/a、39–42 b/d/c/a、57–60 b/a/c/d、75–78 d/b/a/c、141–144 c/d/a/b——全部配对正确。
- 范文 H 97 词（空白分词）；`___` SVG 共 87 处（P1 6、P2 9、P3 9、P4 9、P5 9、P6 15、P7 9、P8 21），text.md 亦 87。

## §6 盒标题逐一 PIL 真墨量测（`tools/boxtitle_scan.py`，`logs/boxtitle.log`）

- 方法：每奶油盒首 100px 标题带内全部行，`occlusion_audit.ink_box` 真墨右缘 vs 盒右缘；>盒右缘为 OVER，余量 <5px 为 TIGHT。
- 结果：32 盒（P1 4、P2 8、P3 4、P4 2、P5 3、P6 8、P7 3、P8 0）、67 行，**0 OVER、0 TIGHT**；日志与首轮复校逐字节一致。
- 最紧三处交付 PDF 渲染像素交叉验证（200 dpi 裁图）：`render/crop-p4-title.png`（P4 y=742，余 19.3px）、`render/crop-p1-title.png`（P1 y=1296，余 22.0px）、`render/crop-p2-title.png`（P2 y=343，余 22.2px）——墨水均止于盒右缘前空白处。
- 67 行 clear 表（余量 px，按余量升序；br=盒右缘，ink_r=墨水右缘）：

```
  19.3 | P4 box y=742 br=961 title y=780.7 ink_r=941.7 [ok] '解説 — сравняли счёт 同点に追いつく ·'
  22.0 | P1 box y=1296 br=1862 title y=1378.0 ink_r=1840.0 [ok] 'Стр. 2Студенты и Дед МорозA2'
  22.2 | P2 box y=343 br=961 title y=381.9 ink_r=938.8 [ok] '解説 — поздравить 祝う · родина 故郷'
  22.5 | P6 box y=200 br=1862 title y=289.0 ink_r=1839.5 [ok] '16–20 ноября — пять рабочих дней'
  23.5 | P7 box y=992 br=1862 title y=1081.2 ink_r=1838.5 [ok] '«распродажа» — большая продажа'
  24.8 | P3 box y=760 br=1862 title y=849.0 ink_r=1837.2 [ok] 'Вечером — в кино: «Рокки — это я».'
  26.3 | P4 box y=742 br=961 title y=810.5 ink_r=934.7 [ok] 'поправка 訂正 · в зоне вылета 降格圏'
  27.6 | P2 box y=919 br=961 title y=957.2 ink_r=933.4 [ok] '解説 — успехов 成功 · желание 願い。'
  28.3 | P5 box y=416 br=961 title y=454.9 ink_r=932.7 [ok] '解説 — календарная дата カレンダー上'
  29.7 | P2 box y=795 br=1862 title y=884.0 ink_r=1832.3 [ok] 'А вы? Что вы пожелаете студенту'
  34.0 | P3 box y=200 br=961 title y=268.2 ink_r=927.0 [ok] 'криминальная 犯罪もの · сказочное'
  35.8 | P6 box y=669 br=961 title y=707.8 ink_r=925.2 [ok] '解説 — задают ритм リズムを決める ·'
  37.7 | P2 box y=200 br=1862 title y=289.0 ink_r=1824.3 [ok] '16 ноября — День толерантности.'
  41.6 | P1 box y=1174 br=961 title y=1245.0 ink_r=919.4 [ok] '8 — матчей сыграли в 14-м туре: все'
  42.5 | P7 box y=200 br=1862 title y=291.0 ink_r=1819.5 [ok] '«Поздравляю с День студента!»'
  42.6 | P6 box y=669 br=961 title y=737.5 ink_r=918.4 [ok] 'честные 本物の · середина 真ん中。'
  48.9 | P5 box y=416 br=961 title y=484.6 ink_r=912.1 [ok] 'の日付 · подошёл ぴったり合った ·'
  49.0 | P3 box y=200 br=1862 title y=289.0 ink_r=1813.0 [ok] '19 ноября — пять премьер сразу.'
  50.4 | P1 box y=1174 br=961 title y=1211.0 ink_r=910.6 [ok] 'ТУР В ЦИФРАХ　数字で見る今節'
  57.1 | P1 box y=1296 br=1862 title y=1336.0 ink_r=1804.9 [ok] 'В ЭТОМ НОМЕРЕ　今号の目次'
  58.7 | P5 box y=647 br=1862 title y=736.2 ink_r=1803.3 [ok] '«Чёрная пятница» — 27 ноября.'
  75.5 | P7 box y=1227 br=1862 title y=1315.7 ink_r=1786.5 [ok] '«Здравствуйте! Я учу русский'
  77.1 | P4 box y=615 br=1862 title y=704.2 ink_r=1784.9 [ok] '1–2. «Зенит» и «Динамо» — 31'
  82.4 | P7 box y=200 br=1862 title y=242.0 ink_r=1779.6 [ok] 'ОШИБКИ　間違いクリニック'
  92.6 | P6 box y=664 br=1862 title y=705.5 ink_r=1769.4 [ok] 'ЗА И ПРОТИВ　賛成と反対'
  94.5 | P5 box y=647 br=1862 title y=689.2 ink_r=1767.5 [ok] 'ЧЁРНАЯ ПЯТНИЦА: ДАТЫ'
  97.6 | P6 box y=664 br=1862 title y=752.5 ink_r=1764.4 [ok] 'За: ритм ровный, ничего не'
 105.1 | P6 box y=1344 br=1098 title y=1392.0 ink_r=992.9 [ok] '19'
 105.1 | P6 box y=1344 br=592 title y=1392.0 ink_r=486.9 [ok] '17'
 105.1 | P6 box y=1344 br=845 title y=1392.0 ink_r=739.9 [ok] '18'
 105.2 | P6 box y=1344 br=339 title y=1392.0 ink_r=233.8 [ok] '16'
 105.2 | P5 box y=1131 br=961 title y=1169.3 ink_r=855.8 [ok] '解説 — в прошлом году 去年 ·'
 105.2 | P6 box y=1344 br=1351 title y=1392.0 ink_r=1245.8 [ok] '20'
 112.8 | P6 box y=1344 br=339 title y=1424.0 ink_r=226.2 [ok] 'пн'
 113.4 | P6 box y=1344 br=845 title y=1424.0 ink_r=731.6 [ok] 'ср'
 113.5 | P6 box y=1344 br=1351 title y=1424.0 ink_r=1237.5 [ok] 'пт'
 114.0 | P6 box y=1344 br=1098 title y=1424.0 ink_r=984.0 [ok] 'чт'
 114.0 | P3 box y=200 br=961 title y=238.5 ink_r=847.0 [ok] '解説 — биография 伝記映画 ·'
 114.4 | P3 box y=914 br=961 title y=952.9 ink_r=846.6 [ok] '解説 — экранизация 映画化 ·'
 114.5 | P6 box y=1344 br=592 title y=1424.0 ink_r=477.5 [ok] 'вт'
 120.5 | P6 box y=200 br=1862 title y=242.0 ink_r=1741.5 [ok] 'НЕДЕЛЯ 16–22 НОЯБРЯ'
 124.0 | P2 box y=1618 br=1412 title y=1706.0 ink_r=1288.0 [ok] 'дождь, который замерзает'
 125.0 | P2 box y=1618 br=1412 title y=1672.0 ink_r=1287.0 [ok] 'ледяной дождь'
 131.7 | P3 box y=760 br=1862 title y=802.0 ink_r=1730.3 [ok] 'КАК ПРОВЕСТИ ВЕЧЕР'
 135.6 | P3 box y=200 br=1862 title y=242.0 ink_r=1726.4 [ok] 'ГЛАВНОЕ — КОРОТКО'
 137.4 | P2 box y=200 br=1862 title y=242.0 ink_r=1724.6 [ok] 'ПРАЗДНИКИ НЕДЕЛИ'
 148.6 | P1 box y=588 br=1862 title y=664.0 ink_r=1713.4 [ok] 'СМИ　メディアの声'
 155.0 | P7 box y=1227 br=1862 title y=1268.7 ink_r=1707.0 [ok] 'ПИСЬМА ЧИТАТЕЛЕЙ'
 161.6 | P2 box y=1618 br=510 title y=1706.0 ink_r=348.4 [ok] 'тепло зимой: снег тает'
 164.3 | P2 box y=1618 br=961 title y=1672.0 ink_r=796.7 [ok] 'мокрый снег'
 164.7 | P5 box y=1131 br=961 title y=1199.1 ink_r=796.3 [ok] 'бытовую технику 家電。'
 167.8 | P2 box y=1618 br=961 title y=1706.0 ink_r=793.2 [ok] 'снег с дождём, он тает'
 178.6 | P7 box y=992 br=1862 title y=1034.2 ink_r=1683.4 [ok] 'СЛОВО　今週の単語'
 184.3 | P2 box y=795 br=1862 title y=837.0 ink_r=1677.7 [ok] 'А ВЫ?　あなたは？'
 186.5 | P2 box y=1618 br=1862 title y=1672.0 ink_r=1675.5 [ok] 'гололедица'
 196.8 | P4 box y=615 br=1862 title y=657.2 ink_r=1665.2 [ok] 'ТАБЛИЦА: ТОП-5'
 204.8 | P1 box y=588 br=1862 title y=628.0 ink_r=1657.2 [ok] 'О ЧЁМ ПИШУТ'
 208.6 | P3 box y=914 br=961 title y=982.7 ink_r=752.4 [ok] 'кинозрителя 観客。'
 211.6 | P1 box y=1874 br=1862 title y=1914.0 ink_r=1650.4 [ok] 'КОРОТКО　短信'
 212.8 | P1 box y=1174 br=961 title y=1272.0 ink_r=748.2 [ok] 'восемь завершены'
 212.8 | P2 box y=343 br=961 title y=411.7 ink_r=748.2 [ok] '· повод きっかけ。'
 233.0 | P2 box y=1618 br=510 title y=1672.0 ink_r=277.0 [ok] 'оттепель'
 236.3 | P5 box y=416 br=961 title y=514.4 ink_r=724.7 [ok] 'примерки 試着。'
 257.6 | P2 box y=1618 br=1862 title y=1706.0 ink_r=1604.4 [ok] 'лёд на дороге'
 302.0 | P3 box y=200 br=961 title y=298.0 ink_r=659.0 [ok] 'おとぎ話。'
 302.5 | P1 box y=1874 br=1862 title y=1966.0 ink_r=1559.5 [ok] 'ВТОРНИК'
 363.5 | P4 box y=742 br=961 title y=840.2 ink_r=597.5 [ok] '内。'
```

另：P1 非盒头 `ТУР В ЦИФРАХ` 行 tspan x=556.5–722.9（Q6 chip x=989，余 266px+），无冲突。

## §7 盒右缘与溢出双法

- `boxright_scan.py`：8 页每盒最差超界均为 **0.0px**（无任何盒内行超盒右缘）。
- `creambox.py` 全扫：负 inside-only 余量 **0**；BELOW-WINDOW 95 行，直方图 +28.0 ×25、+32.0 ×41、+34.0 ×4、+37.0 ×25，全部已分类为既有（下一块标题/通栏行/图例行）；扫描与重建记录 `records/ja/creambox.log` 逐字节一致（路径归一化后 diff 为空）。
- `pixel_verify.py`（渲染卡片像素）：除 P1 y=1874 盒底 +8px（设计橄榄色横线；盒内末行基线 2246、余量 +58）外全部盒底干净；全页最右墨水 P1–P7 **1861**、P8 **1869**（O2，见 PROOF-NOTE）——P2 已由 1869 变 1861（O1 随 D2 消失）。
- `colspill_scan.py`：仅已知系统性误报类；与首轮 diff 恰 3 行——P2 `y=2162 … 'студента' +9.2` 消失（O1），P6 随 D1 重排新增 2 行（`y=1552 '練習用データ' +37.0`、`y=1582 免责声明 +487.2`，通栏注类，墨水右缘 ≤1448）。

## §8 occlusion

- selftest rc=0：planted classes fired {BOXTITLE 1, COVER 1, EDGE 1, FOOTER 1, LINEX 1, TEXTX 1}；clean controls silent。
- 真实审计 rc=1（有 flags 故）：**42 TEXTX、0 LINEX**（JSON `logs/ru-ja-occlusion.json`），与报告计数一致。
- 裁决 `tools/adjudicate_ru.py`（须传本版目录为 argv[2]）：**Counter({'CLEAR': 42})，0 UNRESOLVED**。教训记录：默认 argv[2]=core-ru 时会误报 6 处 UNRESOLVED（卡片错配），不可盲用默认。

## §9 freeze

- 核心标准 baseline：`--build production/2026-w47/core-ru --core-svg production/2026-w47/core-ru/svg`，rc=0，**8/8** byte-identical；core SVGs 前后重哈希未变。
- 版内自比对 baseline：`--build scratch/build/2026-w47-ru-ja --core-svg production/2026-w47/2026-w47-ru-ja/svg`，rc=0，**8/8** byte-identical。
- freeze diff（core→本版），rc=0：删除分页面 distinct **349** / count-sum **536**（全局 distinct 319——同一数据两种口径：349 为分页面 distinct 之和；`freeze-diff.json` 与重建记录逐字节一致）；西里尔删除恰 **15** 项：P8 `Билибин Билибина Зимняя Иван Ивана Иллюстрация Морозко год достояние иллюстрация к можно ноябрю общественное сказка`（各 ×1）= Q46 `можно` ×1 + Морозко 图注 14 词（图按设计跳过），**无法解释 0**；新增西里尔 0；新增 CJK 仅 U+3000 ×8（家具分隔符）。

## §10 印/网文字层

- `pdftotext -layout`：印/网各 106,251 字节；字符多重集差 **0**（全文 + 逐页 P1–P8 全 0）。
- PyMuPDF 非空白字符：印 **26,630** = 网 **26,630**，逐页 [2910, 3006, 2454, 3056, 2682, 2503, 3126, 6893] 全等。
- 网 PDF 重渲染（仅 scratch 内，`tools/webpdf.py svg`）：rc=0，3,721,643 字节，文字层与交付网 PDF 全等；SHA 不同系已知根因（wall-clock 入 head.modified），不以 SHA/字节数论证；生产目录网 PDF 未动。

## §11 s11 / §1.1

- `s11_check.py` rc=0：**FAILURES: none**；纸色 #fbfaf6；无 #f7f1e2 / #c9a227 / #8b4513 / #000000；徽章 A2 #5c6e30、B1 #46581f、B2 #37402f；页脚含 VOL.4 + 全角空格；VOL.3 仅 P4 更正 1 处；刊头 196px；带标题 46px；左 margin 88.0px；印+网各 8 页；网 < 7MB；网文字层 >0。
- P8 最小字号：s11 报 9.75pt；另用 PyMuPDF span 直查印/网 P8 独立确认均为 **9.75pt**（= SOP §1.1 下限 9.75pt），P8 字号谱 [9.75, 9.98, 10.35, 10.88, 11.25, 12.75, 13.5, 14.25, 14.62, 15.38, 15.75, 17.25, 18.0, 18.75, 34.5]。
- 弯引号：U+201C ×1、U+201D ×1、U+2019 ×0（P7 `«на “чёрной пятнице”».` 故意保留内层引号，core 一致）。
- 内部标签（可见文本）：`2026-w47` 0、`ru-ja` 0、`SOP` 0、`cover` 0；`VOL.5` ×6（正当向前引用）、`VOL.3` ×1（P4 更正）；`三色蛾` 可见文本 0、仅 `<title>` 元数据 1 处；SIMP_ONLY `国` ×1（`国際学生の日`）、`学` ×14（`学生の日` / `心理学者の日` / `学生への`）——均为日文汉字假阳性。
- 刊头/页脚：8 页全部含 `Lucerna` 刊头与 VOL.4 页脚 + `Nページ（全8ページ）`。
- ABSTRACT.txt：393 字节（一行日语摘要，内容正确；KIT 称 392 字节，差 1 为尾换行计数，琐注）。

## §12 窄词距实测（O3 类，字形不相触）

- P1 `метеорологическая | зима` 1.40px（与 core-ru 同行实测值 1.40px 完全一致）；P2 `Татьянин | день` 5.20px；P2 `рождения | Деда` 3.05px；P1 `редакции | Lucerna` 3.90px。裁图 `render/crop-p1-meteo.png`（200 dpi）可见 1.4px 间隙，字形不相触。

## §13 视觉通读

- 交付印 PDF 200 dpi 渲染 8 页（`render/p200-1.png` … `p200-8.png`）逐页目视：无溢出/重叠/裁切；200 dpi 关键裁图：`render/crop-web-wordbox.png`（网 P1 斜体词条）、`render/crop-p8-eyebrow.png`（O2 眉题末字完整）、`render/crop-p8-q41.png`/`crop-p8-q41b.png`（Q41 注 `上映回` 与附录一致）、`render/crop-p1-meteo.png`（窄词距）、最紧三标题裁图（见 §6）。
- P4 八场比分表 8 场、15 轮赛程 8 场齐全；P6 图表 38/26/18/18=100%、柱长成比例；P7 金句 8 句页码全对；P8 答案印全至 Q150。

## §14 方法备注

- `occlusion_audit.py` 不带 `--selftest` 时直接审计目录；`adjudicate_ru.py` 的默认 core 目录须显式覆盖为本版目录。
- freeze `diff` 的 distinct 在 gate_lang 口径下为分页面 distinct 之和（349），全局 distinct 为 319——两数皆真，勿误作不一致。
- `ink_box` 为超采样且将行首 U+3000 计入墨水盒——PIL/SVG 度量与渲染不一致时，以交付 PDF 渲染像素为准（如 O2）。
- `boxtitle_scan.py` 的 TIGHT 阈值为余量 <5px；本轮最小余量 19.3px，无一贴近阈值。
- 严禁对含 base64 内嵌图片的 SVG 用 `grep -o`（或无界 dump）——本轮全程用 `grep -c`、Python 截断、目标模式。
