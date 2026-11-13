# GATE-LOG — 2026-W47 ru-nl（re-fanout 重建版，VOL.4）

- 校对员：proof1（SOP §8.4）
- 日期：2026-11-11
- 版目录：`production/2026-w47/2026-w47-ru-nl/`；core（只读）：`production/2026-w47/core-ru/`
- scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ru-nl2/`（`TMPDIR` 指向其下；生产目录零写入）
- 工具：repo venv `tools/venv/bin/python`
- **注（ru 家族等效覆盖）：** ru 家族无 `verify_ed.py`（仅 en 家族有），以 check_core + s11_check + keycheck（150 题手验 + p8 compare）等效覆盖。

## 0. 开工探针

- `echo test | git hash-object -w --stdin`（`~/workspace/weekly-git` 内）：rc=0，`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`
- scratch 真实写文件：OK（`probe.txt`）

## 1. 三 SHA

| 文件 | 字节 | sha256 实测 | 结论 |
|---|---|---|---|
| `Lucerna-VOL4-ru-nl.pdf` | 21,315,805 | `8982ce29eaf2bc57661a089b9bf0bd8021444130e2e0c9aa505f9176de4a1e17` | 与先验一致 |
| `Lucerna-VOL4-ru-nl-web.pdf` | 3,387,072 | `abc3ec69f695129c9e248dae36880da1754f6af5ef32b62f5438435458512593` | 与先验一致 |
| `2026-w47-ru-nl.text.md` | 64,053 | `96dc93598dec047b87a168c2332bc30b611b8a42250d22e65c7e1da2920ac694` | 与先验一致 |

## 2. run.py（scratch 内重建，日志 `run.log`）

- rc=0；TOTAL 150；0 FLOW OVERFLOW / HEAD TOO WIDE
- 按页：{1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}
- 按级：A2 50 / B1 76 / B2 24
- 按型：Voltooi de zin 54，Meerkeuze 55，Woorden koppelen 20，Zinnen bouwen 12，Zinsomvorming 4，Vertaling 4，Schrijven 1
- scratch 重建与生产 8 个 SVG 字节相同：8/8（版内自比对）

## 3. check_core.py（只读，日志 `check_core.log`）

- rc=0；golden BAD 0；gloss fail 0；golden 8/8 ×2
- orphan 1：P7 y553 `”».`
- same-baseline collision 1：P1 y1712 `чёрная`
- 两项与 core-ru 同值同位，见 PROOF-NOTE O2

## 4. p8（日志 `p8-extract.log`、`p8-compare.log`；`ru-nl-p8.json`、`ru-nl-p8-compare.json`）

- extract 150/150，rc=0
- compare：CLEAN；keydiff `[137,138,139,140]`（直接读 `ru-nl-p8-compare.json` 本体；total 150；missing/extra/uncertain 均空）
- 与 core `ru-p8.json` 直接 keydiff：相同 `[137,138,139,140]`；key 20 两版均为 `желании`
- keys 137–140（荷）：137 `Dinsdag 17 november, Studentendag.`；138 `Een pakket moet gevolgd, opgehaald en gecontroleerd worden.`；139 `Op dinsdag speelt Rusland tegen Venezuela.`；140 `Fijne Studentendag allemaal!`

## 5. occlusion 真实审计（`tools/occlusion_audit.py`，版内 `svg/`，未用 `--selftest`；日志 `occlusion.log`、`ru-nl-occlusion.json`）

- 42 TEXTX，0 LINEX，0 COVER/FOOTER/EDGE
- core-ru 同审计：相同 42 旗标（34 字节相同；8 处仅 y 位移或镜像 run 顺序）
- 裁决（修正版工具，SX=1.0；日志 `adjudicate2.log`、`adjudicate-core.log`、`adjudicate-pdf.log`、`adjudicate-web.log`）：
  - card 渲染：38 CLEAR + 4 OVERLAP（`Краснодар` vs 收 `»`：P1 box [101.2,1200.5,233.7,1224.8]、P4 [101.2,578.7,233.7,602.9]、P4 [101.2,685.6,233.7,709.9]、P4 [1042.2,2215.4,1174.7,2239.6]；PIL 重叠 3.1×11.0 px；card 行级最小单行间隙 0，无交错墨）
  - **印 PDF（`p96-*.png`）与网 PDF（`w96-*.png`）：均为 41 CLEAR / 1 OVERLAP**；4 处 `Краснодар»` 在两 PDF 上均为 CLEAR、间隙 1 px（行级最小单行间隙恰为 1）
  - 唯一 PDF OVERLAP：P7 `Кипренского` vs `, 1827 `——假阳性（取样行撞上上方深色普希金肖像）；正确阈值重测最宽净空 8 px（印 PDF）/ 9 px（card），thr<128 时 9/11 px；证据 `ed-p7-kiprensk-pdf.png`、`ed-p7-kiprensk-card.png`
- 工具 bug 记录（PROOF-NOTE O1）：re-fanout `adjudicate_ru.py` 硬编码 SX=1950/1800（本族 SVG 宽 1950，应为 1.0）；core proof1 `adjudicate.py` 计数器反向。两份 “42/42 CLEAR” 结论碰巧为真，但未被各自工具有效量出。

## 6. freeze（日志 `freeze-core.log`、`freeze-ed.log`、`freeze-diff.log`；`freeze-diff.json`）

- core-ru 基线（`--build core-ru --core-svg core-ru/svg`）：8/8 字节相同，rc=0；core SVG 未改动
- 版内自比对：8/8，rc=0
- core→版删除：distinct **487**，count-sum **854**（与 re-fanout 报告一致）
- 西里尔删除 15，全部在 P8：Q46 `можно` ×1 + 14 个 Morozko 图注词（Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、ноябрю、общественное、сказка），均位于 core P8 图注区（y≥2450）；**无法解释 0**
- 新增 CJK：仅 U+3000 ×8
- Morozko 图未入版 P8：`run.log`：`P8 morozko SKIPPED: no room (col 3 y 2389.29)`；版 P8 联合文本无 `Морозко`

## 7. 印/网文字层 multiset（PyMuPDF，非空白字符）

- 总体与逐页均相同：**31,087 字符**；8/8 页
- 逐页：P1 3115，P2 3386，P3 2719，P4 3400，P5 2950，P6 2865，P7 3615，P8 9037

## 8. s11_check.py（`scratch-fanout-ru/s11_check.py`；日志 `s11.log`）

- rc=0；**FAILURES: none**
- P8 最小字号 **9.75 pt**（SOP §1.1 下限）
- 8 SVG；纸色 #fbfaf6；无禁色；徽章 A2/B1/B2 配色；masthead 196 px；band 标题 46 px；左留白 88.0；可见 SVG 无 CJK；网 PDF 3,387,072 B < 7 MB

## 9. creambox（`hidden_files/w47/tools/creambox.py`，全 8 页；日志 `creambox.log`）

- 32 奶油矩形；**0 负向内侧净空**
- 95 BELOW-WINDOW 行：+28.0×25，+32.0×41，+34.0×4，+37.0×25——均在既有 +24..+37 向下一标题区间，无 +12..+18 整行溢出区间
- 扫描与 re-fanout 记录的 `creambox.log` 路径归一化后字节相同
- P7-TOOLBOX 汇总：3 框，最小内侧净空 +11.9，最小降部净空 +5.9
- 1 处内侧降部净空 −1.0（P2 框 y=795，底 1159.0，末基线 1154.0，行 `één voor Grootvader Vorst.`）：**假阳性**——该行无降部字形，真墨底 1153（card 与印 PDF 均同），真净空 +6 px；初扫 card 时框下发现的墨为 Yuon 画作顶部（独立元素），非文字溢出；与 core proof1 的 P2 −1.6 同类

## 10. 盒标题 PIL 真墨量测（`boxtitles.py`，复用 `tools/occlusion_audit.py` 的 `parse_svg`：transform + letter-spacing + PIL 真墨框；`boxtitles.json`、`boxtitles.log`）

- 32 个奶油矩形全部有标题；**最小 clear 18.9 px**；**0 负值**；无框内行 clear < 10 px
- 最紧五处：P6 `Uitleg — задают ритм bepalen het ritme` 18.9；P6 `ЗА И ПРОТИВ VOOR EN TEGEN` 21.3；P4 `Uitleg — сравняли счёт gelijkmaken ·` 30.6；P5 `Uitleg — в прошлом году vorig jaar ·` 41.0；P7 `СЛОВО WOORD VAN DE WEEK` 47.8
- PDF 像素交叉验证（生产 `cards/*.png`，SVG viewBox 1950×2700 = card 1950×2700，scale 1.0）：最紧处像素最右墨 943 vs PIL 942.1，一致（`pixelcheck.log`）
- P6 日条 21/22 黄色格为黄色填充、非奶油框，不在 32 矩形内；200 dpi 目检数字居中无溢出；P8 无奶油框

### 全部 32 行盒标题 clear 表（单位 px；clear = 框右 − 真墨右）

| # | 页 | 框（x1,y1,x2,y2） | 标题（标题基线） | 真墨右 | 框右 | clear |
|---|---|---|---|---|---|---|
| 1 | P1 | 538.5, 1203.7, 961.0, 1583.7 | ТУР В ЦИФРАХ IN CIJFERS（1240.7） | 872.6 | 961.0 | 88.4 |
| 2 | P1 | 1439.5, 588.0, 1862.0, 1288.0 | О ЧЁМ ПИШУТ（628.0） | 1657.2 | 1862.0 | 204.8 |
| 3 | P1 | 1439.5, 1296.0, 1862.0, 1626.0 | В ЭТОМ НОМЕРЕ INHOUD（1336.0） | 1782.7 | 1862.0 | 79.3 |
| 4 | P1 | 1439.5, 1874.0, 1862.0, 2304.0 | КОРОТКО KORT（1914.0） | 1667.7 | 1862.0 | 194.3 |
| 5 | P2 | 538.5, 343.4, 961.0, 489.1 | Uitleg — поздравить feliciteren ·（381.9） | 884.2 | 961.0 | 76.8 |
| 6 | P2 | 538.5, 948.4, 961.0, 1064.4 | Uitleg — успехов succes · желание（986.9） | 904.7 | 961.0 | 56.3 |
| 7 | P2 | 1439.5, 200.0, 1862.0, 769.0 | ПРАЗДНИКИ НЕДЕЛИ（242.0） | 1724.6 | 1862.0 | 137.4 |
| 8 | P2 | 1439.5, 795.0, 1862.0, 1159.0 | А ВЫ? EN U?（837.0） | 1626.2 | 1862.0 | 235.8 |
| 9 | P2 | 88.0, 1618.0, 510.5, 1768.0 | оттепель（1672.0） | 277.0 | 510.5 | 233.5 |
| 10 | P2 | 538.5, 1618.0, 961.0, 1768.0 | мокрый снег（1672.0） | 796.7 | 961.0 | 164.3 |
| 11 | P2 | 989.0, 1618.0, 1411.5, 1768.0 | ледяной дождь（1672.0） | 1287.0 | 1411.5 | 124.5 |
| 12 | P2 | 1439.5, 1618.0, 1862.0, 1768.0 | гололедица（1672.0） | 1675.5 | 1862.0 | 186.5 |
| 13 | P3 | 538.5, 200.0, 961.0, 345.7 | Uitleg — биография biopic ·（238.5） | 840.2 | 961.0 | 120.8 |
| 14 | P3 | 538.5, 914.4, 961.0, 1030.4 | Uitleg — экранизация verfilming ·（952.9） | 897.5 | 961.0 | 63.5 |
| 15 | P3 | 1439.5, 200.0, 1862.0, 736.0 | ГЛАВНОЕ — КОРОТКО（242.0） | 1726.4 | 1862.0 | 135.6 |
| 16 | P3 | 1439.5, 760.0, 1862.0, 1105.5 | КАК ПРОВЕСТИ ВЕЧЕР（802.0） | 1730.3 | 1862.0 | 131.7 |
| 17 | P4 | 538.5, 742.2, 961.0, 887.9 | Uitleg — сравняли счёт gelijkmaken ·（780.7） | 930.4 | 961.0 | 30.6 |
| 18 | P4 | 1439.5, 615.2, 1862.0, 1024.2 | ТАБЛИЦА: ТОП-5（657.2） | 1665.2 | 1862.0 | 196.8 |
| 19 | P5 | 538.5, 416.4, 961.0, 562.1 | Uitleg — календарная дата（454.9） | 821.1 | 961.0 | 139.9 |
| 20 | P5 | 538.5, 1130.8, 961.0, 1276.5 | Uitleg — в прошлом году vorig jaar ·（1169.3） | 920.0 | 961.0 | 41.0 |
| 21 | P5 | 1439.5, 647.2, 1862.0, 1122.2 | ЧЁРНАЯ ПЯТНИЦА: ДАТЫ（689.2） | 1767.5 | 1862.0 | 94.5 |
| 22 | P6 | 538.5, 669.3, 961.0, 815.0 | Uitleg — задают ритм bepalen het ritme（707.8） | 942.1 | 961.0 | 18.9 |
| 23 | P6 | 1439.5, 200.0, 1862.0, 639.5 | НЕДЕЛЯ 16–22 НОЯБРЯ（242.0） | 1741.5 | 1862.0 | 120.5 |
| 24 | P6 | 1439.5, 663.5, 1862.0, 945.5 | ЗА И ПРОТИВ VOOR EN TEGEN（705.5） | 1840.7 | 1862.0 | 21.3 |
| 25 | P6 | 89.4, 1343.4, 339.6, 1440.6 | 16（1392.0） | 233.8 | 339.6 | 105.8 |
| 26 | P6 | 342.4, 1343.4, 592.6, 1440.6 | 17（1392.0） | 486.9 | 592.6 | 105.8 |
| 27 | P6 | 595.4, 1343.4, 845.6, 1440.6 | 18（1392.0） | 739.9 | 845.6 | 105.8 |
| 28 | P6 | 848.4, 1343.4, 1098.6, 1440.6 | 19（1392.0） | 992.9 | 1098.6 | 105.7 |
| 29 | P6 | 1101.4, 1343.4, 1351.6, 1440.6 | 20（1392.0） | 1245.8 | 1351.6 | 105.8 |
| 30 | P7 | 1439.5, 200.0, 1862.0, 980.2 | ОШИБКИ FOUTENKLINIEK（242.0） | 1781.1 | 1862.0 | 80.9 |
| 31 | P7 | 1439.5, 992.2, 1862.0, 1214.7 | СЛОВО WOORD VAN DE WEEK（1034.2） | 1814.2 | 1862.0 | 47.8 |
| 32 | P7 | 1439.5, 1226.7, 1862.0, 1733.7 | ПИСЬМА ЧИТАТЕЛЕЙ（1268.7） | 1707.0 | 1862.0 | 155.0 |

## 11. D1 / D2 / D6 / kicker / web 斜体（日志 `d-checks.log`、`kicker.log`）

- **D1**：text.md 段 L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、L596 `Большой тест недели + все ответы` 精确一致；4 个 nl KEEP 值（`scratch-fix-ru-d1/build_map.py`）均在对应 SVG 内（P7 副标、P6 图表标题、P6 免责声明、P8 副标），且按设计不在 text.md 内（exporter 渲染 ` · ` 分隔符；免责声明仅 SVG）
- **D2**：Q25 选项 `День студента` 在 `content12.py:276`；全称 `Международный день студента` ×2 在 text.md（= core ×2）；短式已入版
- **D6**：`желании` ×2 在 text.md（L173 练习、L694 答案表）；p8 key 20 = `желании` = core；`content12.py:257` key，修复注释 :259–261；P2 SVG 出现 0 次（预期——key 只印 P8；core P2 SVG 亦 0；版 P8 SVG 1）
- **kicker**：按 INVEST-NOTE 方法 1 独立重算（整 run `getbbox`，10 token，9 间隙，尾逗号分离）：间隙 `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`，**最小 5.9 px ≥ 4**；kicker 行 y=372，19 元素含 9 处双空格 run
- **D1 web 斜体**：网 PDF 嵌 `LucernaNotoSerif-Italic`（CGSAUI+，embedded yes）与 `LucernaNewsreader-Italic`（JIOAFO+，embedded）；P1 `чёрная пятница` 带空格 ×5，无无空格 `чёрнаяпятница`

## 12. web PDF 重渲染（仅 scratch，`webrerender/`；日志 `webrerender.log`）

- `tools/webpdf.py svg Lucerna-VOL4-ru-nl-web-rerender.pdf`：rc=0，8 页，3,387,112 B，57,959 文本字节
- 文字层 multiset 与发货网 PDF **逐页相同**（逐页计数同 §7）
- SHA 与发货网 PDF 不同（预期：fontTools 写 wall-clock 进 head.modified；SHA 永不作证据）
- 生产目录的网 PDF 未覆盖

## 13. 全书通读

- **150 题 key-vs-stem 手验**：text.md 全文 838 行逐读，每题按题干语义核 key（非仅三源比对）；**Q1–150 全部正确**（含 Q20 `желании` 前置格、Q22 16:20、Q54 2:0、Q59 2:1 与 `content34.py:150–151` 结果表核对、Q61–64 动词形、Q73 `заказов` 属格复数、Q97–100 连接、Q127 B、Q137–140 荷译、Q145–149 对话 cloze、Q150 模板文 97 词——text.md 与 `content8.py` MODELO 双重核对）
- **matching 渲染字母顺序（按 SVG 基线拼接行实测，`q_match4.py`、`matching-verify2.log`）**：
  - P2：a=День психолога，b=День студента，c=Всемирный день ребёнка，d=день рождения Деда Мороза；keys 25b/26d/27c/28a ✓
  - P3：a=человек, который смотрит фильм，b=фильм о жизни реального человека，c=показ фильма в кинотеатре，d=фильм о реальных событиях；keys 39b/40d/41c/42a ✓
  - P4：a=победил ЦСКА 4:2（y=2352.4），b=проиграл «Рубину» 0:1（2390.4），c=победил «Акрон» 2:1（2428.4），d=сыграл с «Ростовом» 2:2（2466.4）；keys 57b/58a/59c/60d ✓
  - P5：a=код со скидкой，b=товар возвращают в магазин，c=цена ниже обычной，d=большая продажа со скидками；keys 75d/76b/77a/78c ✓
  - P8：a=результат матча, например 2:2（741.2），b=лёд на дороге（779.2），c=тепло зимой: снег тает（817.2），d=большая продажа со скидками（855.2）；keys 141c/142d/143a/144b ✓
- **练习 key vs P8 答案表**：150/150 相同，0 不一致（`keycross.log`）；P8 答案表按页分段与练习 key 逐段核对一致
- **8 页 200 dpi 目检**（`renders/p200-1.png` … `p200-8.png`）：无溢出/重叠/裁切；P4 八场结果表齐全、与 Q52–56/Q57–60 一致；P6 图表 38/26/18/18 比例正确；P7 金句 8 条带页码、读者来信含双语披露；P8 150 题与答案表完整
- **字面 `___`**：text.md 87、版内 SVG 联合文本 87、core text.md 87，一致；core 继承模板缺口，不作缺陷
- SIMP_ONLY 等非本版项：未判

## 14. 缺陷（PROOF-NOTE 详述）

- **D7（唯一缺陷）**：P7 band `content7.py:12`，`Drie niveaus, drie thema’s`——U+2019 在 Noto Sans CJK SC（18 px）中 advance 18.0 px，’ 与 `s` 之间墨间隙 **16 px**（card / 印 PDF / 网 PDF 三源一致；同 run 其余字母间隙 1–6 px）；证据 `ed-p7-band-themas.png`（4× 放大裁切）

## 15. 观察项

- O1：adjudicator 工具 bug（见 §5 与 PROOF-NOTE O1）——方法论问题，非本版缺陷
- O2：check_core orphan 1 / collision 1（见 §3）——core 继承
- O3：窄空格（KIT §7 已裁定）、P3/P5 结构留白、P7 普希金半脸裁切（与 core 同图同框）、P8 无 Morozko 图（设计）——已核实，无需处理
