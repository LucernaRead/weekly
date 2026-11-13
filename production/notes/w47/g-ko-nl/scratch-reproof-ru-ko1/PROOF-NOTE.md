# W47 ru-ko 独立复校记录（re-proof，fix1 之后）

**结论：(a) 零缺陷，可定稿。**

复校员：独立复校（SOP §8.4，修后从头完整复校，不只看修处）。
复校日期：2026-11-11。工作区（唯一）：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-ru-ko1/`。
对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-ko/`，fix1 已落地。核心对照：`~/workspace/weekly-git/production/2026-w47/core-ru/`。
约束：不 commit、不 push；生产目录只读验证，不写生产文件（42 文件 SHA 快照开工/收尾比对零差异）。

## 一、三 SHA（开工与收尾两次实测，逐字节相同）

| 文件 | SHA-256 | 字节 |
|---|---|---|
| 印 `Lucerna-VOL4-ru-ko.pdf` | `78e4442af8af9ec286c407ff66e08bac2029dd79d3ded43d1bfde3d555a6a400` | 22,007,810 |
| 网 `Lucerna-VOL4-ru-ko-web.pdf` | `3bf39ecf4fa4563458c68319ca42171642f9ad0be24650064faa9b7d9bd03195` | 3,513,230 |
| 文 `2026-w47-ru-ko.text.md` | `5e9bd67201fd232aff598e0bbb487ba45821878e533392bc6e749444b090bffe` | 65,012 |
| 核心文 `2026-w47-ru-core.text.md` | `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` | 60,953 |

KIT §5（`WEEKLY-KIT.md:57`）与实测一致：65,012 B + SHA `5e9bd672…`。

## 二、D-1 独立验证（fix1 的唯一缺陷，仅 text.md）——已修好

- text.md L836 逐字为 `150. ✓ 모범 답안은 이 면의 H란(97 단어)`（`check_appendix.py` rc=0 实测）。
- P8 印出键逐字一致：交付印 PDF P8 渲染目视，附录区末行 `150. ✓ 모범 답안은 이 면의 H란(97 단어)`；`p8.py extract` 150/150，`compare` CLEAN。
- 附录 150 题机械核对：keylist 各 150 条、连续 1–150；题头 vs P8 印出键 0 不符（150/150）；题头 vs 核心附录差异仅 [137,138,139,140]（韩文翻译键，按设计）；note-only 差异 139 条；与核心逐字节相同行 7 条（[34,35,36,61,63,64,96]，纯俄语动词变位 note）。
- keycheck vs REG：149/150，仅 Q150 预期差异（注册表 key 为括号 note，附录按规则渲染 ✓）；按 REG 全行重建附录 150/150 一致。
- 导出器补丁在位：`ru_textmd.py:625` `e["key"].startswith(("(", "（"))`，:620 类型无关注释；`ru_textmd.py.FIXED` 在 scratch 内重生成核心 text.md **字节一致**（SHA `348511e0…`、60,953 B，L836 `150. ✓ 范文见本版 H 区（97词）`），核心目录零写入。
- 其余 9 版 ru text.md 的同类长串形式是已记录的入仓批量项，本次不修、不判。

## 三、16 门禁自跑自验（全部实测，见 GATE-LOG.md）

1. **run.py** rc=0：TOTAL 150（A2 50 / B1 76 / B2 24；各页 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW / HEAD TOO WIDE；scratch 重建 SVG 8/8 字节一致；生产 SVG 哈希不变。REG 导出 `reg.json`（n=150：type `쓰기`、key `(열린 문제 — 모범 답안은 아래에 있어요)`、note `모범 답안은 이 면의 H란(97 단어)`）。
2. **check_core.py** rc=0：golden BAD 0、gloss 0；8 句 golden 各 ×2；孤儿行 1（P7 y553 `”».`）+ 同基线碰撞 1（P1 y1712 `чёрная`），均与核心相同。
3. **s11_check.py** rc=0，FAILURES: none；P8 最小字号 9.75pt；§1.1 全 PASS。
4. **p8.py extract/compare**：extract 150/150（核心与本版均）；compare CLEAN，keydiff [137,138,139,140]；与核心 `ru-p8.json` 直接比对 keydiff 相同；key20=`желании`、key150=`✓`；Q137–140 为韩文翻译键，已逐一核对原文。
5. **freeze baseline/diff**：baseline 本版 8/8 rc=0；baseline 核心 8/8 rc=0；diff：removed distinct 361、count-sum 529；含西里尔 removed 恰 15 = 14 个 Morozko 图注词（P8：Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、ноябрю、общественное、сказка）+ Q46 `можно` ×1；unexplained 0；新增 CJK：汉字 0、假名 0、Hangul 2,832（工具 total 2,851，含 19 个 U+3000 全角空格）。
6. **occlusion audit**：selftest OK（6 类 planted 全触发，clean 对照静默）；42 TEXTX，0 LINEX/COVER/FOOTER/EDGE/BOXTITLE。
7. **occlusion 交付 PDF 像素裁决**：**42/42 CLEAR**。卡片裁决 38 CLEAR / 4 OVERLAP（全是 `Краснодар`，flag 6、20、21、24）；PDF 像素裁决 41 CLEAR / 1 OVERLAP（flag 38，P7 `Кипренского`，系 dark_bg 极性误判）。直接列扫描在交付印 PDF 上逐个解决：flag 6/20/21/24 CLEAR（96dpi 间隙列 x=231 零墨，卡片与 PDF 在该列差 1px 光栅化）；flag 38 CLEAR（x=556 列在卡片与 PDF 中均为零墨，192dpi 下仍为 3 列零墨 1111–1113；flag 6 的 1px 间隙在 192dpi 下亦存续，463 列零墨）；web PDF 渲染同样：flag 6 列 231=0、flag 38 列 556=0。`flag38-crop.png` 已目视：图注“…Кипренского, 18…”干净无重叠；`flag6-crop.png` 已目视：`«Краснодар» —` 间隔干净。注意：旧 `adjudicate_ru.py` 硬编码 `SX=1950/1800` 且 CORE=core-ru，是错标尺（本族 SVG 宽 1950，卡片 1950×2700，须用 SX=1.0），未使用；用的是自写裁决器。
8. **附录机械核对**：见第二节（150/150）。
9. **keycheck vs REG**：见第二节（149/150，仅 Q150 预期差异）。
10. **150 题手验（`check150.py`）** rc=0 PASS：练习行各 150 条（130 tagged + 20 matching 式）；题干全文差异 0、西里尔序列差异 0；key-head vs 核心差异仅 {137,138,139,140,150}（150 为括号开放题 note，韩 vs 中，按设计）；范文 97 词、与核心 L664 逐字节相同；`Международный день студента` 全文 ×2（两版同）；Q20 题干 `Дети пишут Деду Морозу о своём ___.`、key `желании`；Q25 题干 `17 ноября — День студента`、key b（matching 式）；Q73 题干 `В прошлом году сделали 14,4 млн ___.`、key `заказов`；Q137–140 key 已验；P2 渲染含 Q25 全部 4 个选项（День психолога / День студента / Всемирный день ребёнка / день рождения Деда Мороза）。
11. **核心守卫（fix1 守卫复核）**：见第二节，修后导出器重生成核心 text.md 字节一致。
12. **印/网文字层**：pdftotext 各 58,692 B，逐字节相同。
13. **P1 统计盒（`p1stats.py` v3）**：标题 runs 在 y=1211.01（`ТУР` x=556.5、`В`、`ЦИФРАХ`、`　숫자로 보는 라운드` x=726.6）；advance 末端 931.7；数字盒 rect (538.5, 1174.01, 422.5, 380.0)，右边界 961.0；advance 余量 29.3px；交付 PDF 最右墨 x=928 → 余量 33.0px。ru-de/ru-en 越框缺陷本版未复现。（fix1 称 PIL +29.1px / PDF +33px；本人 advance 测得 29.3，与 PIL-ink 29.1 差 0.2px，系方法口径差，非缺陷。）
14. **D1/D2/D6/D1a/D1b 存活（`dsurvival.py` v2）** rc=0 PASS：D1 text.md L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、L596 `Большой тест недели` 均在；SVG 中 P6 图标题 + 完整免责句 `Это учебный опрос редакции для упражнений — не настоящая статистика. 이것은 연습을 위한 편집부 설문입니다. 실제 통계가 아닙니다.`、P7 副标题、P8 副标题均在；D2 P8 key25=b；D6 P8 key20=`желании`；D1a L99 `роди나` 为纯西里尔（码点 0x440,0x43e,0x434,0x438,0x43d,0x430）；D1b L538 `синоптики` 在；8 页 SVG 逐 token 混排扫描：西里尔+Hangul 混用 0、汉字 token 0、假名 token 0。
15. **kicker PIL 复测**：内容在 `content12.py:18`、y=372、16px sans，9 处双空格。正确字体已确认：`svglib.py` `FONTS_DIR="/usr/share/fonts/opentype/noto"`，CJK 为 `NotoSansCJK-Regular.ttc`；CJK 空格 advance 实测 3.578125px（= KIT 的 3.58）。PIL 真墨间隙（下一词墨左 − 上一词墨右，Noto Sans 16 + SVG 实测 x）：**[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 5.4, 6.8, 7.2]**，最小 5.4px ≥ 4px 门槛，**通过**。与 KIT 值 [7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6] 对比：前 6 项逐项一致；第 7 项（—→НАСТОЯЩАЯ）本人 5.4 vs KIT 7.4、第 9 项（РОССИЯ,→ПО-РУССКИ）本人 7.2 vs KIT 7.6——差异因破折号/逗号 run 在 SVG 中用 CJK 字体渲染，本人按 Noto Sans 计墨宽；光栅实测（交付 PDF）这两处间隙分别为 9px、10px，均宽于 KIT 值。最窄处为第 2 项 ГАЗЕТА→ДЛЯ：PIL 5.9（= KIT 值），192dpi 光栅实测间隙 3.5px（8 列零墨，1553–1560），仍为空白、无接触；原因是 ГАЗЕТА 末尾 `А` 超出 advance 约 3px。结论：kicker 9 处接缝全部开放、无重叠，PIL 门槛通过。
16. **交付 PDF 全页目视（P1–P8，96dpi 渲染，`pdf-render-p1.png` … `pdf-render-p8.png`）**：无溢出、无重叠、无裁切、无 tofu、无孤儿行越界。P1 统计盒、P2 Q25 四选项、P6 图表+免责句、P7 Кипренского 图注、P8 附录末行 `150. ✓ …` 均已目视确认。P2/P3/P5/P6 中栏下半部空白为核心版式固有几何（freeze 证实仅讲解层变化），非本版缺陷。

## 四、D5 字体问题（只记录，不作门、不修）

proof1 D5（web PDF 丢 P1 斜体短语）在本版不复现。实测：web PDF 内嵌 `LucernaNewsreader-Italic` + `LucernaNotoSerif-Italic`（pdffonts，对象号 50/54）；印 PDF 内嵌 `Newsreader16pt-Italic` + `NotoSerif-MediumItalic`（同对象号 50/54，子集命名不同，系构建器差异，非缺陷）；P1 斜体行 16.12pt 在印/网中结构相同（`«` + `чёрная пятница` + `»` 三 span）；spans 逐字相同为 False 仅因字体名不同；文字层逐字节相同。

## 五、观察项（非缺陷，核心继承）

- 各页 `От редакцииLucerna`（如 P1/P2/P3/P4/P5/P6 栏头）“редакции”与“Lucerna”之间无空格，核心亦同（proof1 §7 已记录），非本版引入。
- P8 附录区 Q150 键为 `✓` 形式，与 text.md L836 一致。

## 六、生产零写入

开工/收尾 42 文件 SHA 快照（`snapshot-open-sha256.txt` / `snapshot-close-sha256.txt`）diff 为空；三 SHA 收尾值与开工值逐字节相同。本次工作未写任何生产文件；全部输出均在 goals-side scratch 内。
