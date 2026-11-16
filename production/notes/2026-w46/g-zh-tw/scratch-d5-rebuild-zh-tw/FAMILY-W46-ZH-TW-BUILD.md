# W46 zh-tw 目标语家族 D5 重修 BUILD 报告

**家**：W46 zh-tw（2026-11-09 → 2026-11-15，VOL.3）· **10 版**：读者 de/en/es/fr/it/ja/ko/nl/pt/ru + core-zh-tw（兼 en 读者版，无独立 `2026-w46-zh-tw-en/` 生产目录）。
**Builder**：scratch `hidden_files/d5-redo/scratch-2026-w46-zh-tw/` · 仓库 HEAD `6753a650`（"W46 zh-cn: D5 rebuild"，开工时核对一致）。
**解释器**：`~/workspace/weekly-git/tools/venv/bin/python` 全程。`fc-cache -f` 已暖（开工时；VM 重启后未重跑——见 §10 事故记录）。
**磁盘**：开工 74G/150G（50%）；终盘 75G/150G（51%）。

## §0 方法、分母与盘点结论

### §0.1 方法

- **基线 = fanout，不用 production**：production 的 10 份 `svglib.py` 全是 307 行旧引擎（D1 fix 0、Newsreader 0、`_D5_READER` 0、`_char_font` 0、`_tc_index` 2），从未持有 §1.1 port；fanout 的 svglib 为 490 行（fr 524、nl/pt/ru 505，读者专属 wrap 修正），D1 fix 1、Newsreader 10、`_char_font` 3、`_D5_READER` 0。**本家是 D1+D5 一次做**（与 W43/W45 zh-tw 同）。
- **安装**：手写 port `scripts/d5_port_zhtw.py`（从 `apply_variant.py` 逐字取 FIX2_BLOCK/D5_BLOCK/READER_CONST，无转录；face= 锚点翻译），`scripts/install_zhtw.sh`（`--check` 先行）。ja/ko 先做 TC→JP/KR 全量改名（计数断言），再装 port。
- **导出**：naive 导出器 `style-port-zh-tw/textexp_zh_tw.py` 存在且可用；D5 版用 joiner `scripts/textexp_zh_tw_d5.py`（`--base-svglib baseline/<slug>/svglib.py`），基线回归与 fanout `.text.md.new` 逐字节相同（de 已验 50,143 B）。
- **本周词**：`實付金額`。已发 text.md 10/10 存在（production text.md 与 issues text.md 逐字节相同，9 读者目录 + core 的 en 件）。
- **门禁分母：19 verdicts/版**：G1–G14 + G15a + G15c + G16 + D18 + D37。**G15b 仅记录**（D27：共享 `verify_textmd.py` 对 zh-tw 格式未校准，diagnostic only；native verifier 为准）。
- **交付网 PDF**：显式 `webpdf.py svg/ <slug>.web.pdf` 为交付件；render.py 内建的 `Lucerna-VOL3-XX-web.pdf` 与之差 ~1 字节（随机子集标签），不是交付件。**单网 PDF**（zh-cn 家同；ko 家双网 PDF 不适用本家）。

### §0.2 盘点结论

| 项 | 结论（实测） |
|---|---|
| D1+D5 还是 D5-only | **D1+D5 一次做**：production svglib 307 行旧引擎，D1 fix 0；fanout 490 行已 §1.1 + D1 |
| fanout svglib 与 MANIFEST pin | 10/10 吻合（de/es/it/ja/ko/en sha `f19643ce…`；fr `6ff7d978…`；nl/pt/ru `f23c5f80…`） |
| content 文件 `face=` 形参 | 0 处（fanout + core 全部 content12/bslib4）：svglib `face` 默认值管一切，无 W45-ru 式 face bug 可能 |
| KIT / ABSTRACT.txt | fanout 与 production 逐字节相同（10/10） |
| render.py | fanout 10/10 为 ED-relative `BASE=os.path.dirname(...)`；production 10/10 为死路径 `~/workspace/goals/.../files/weekly-report-w46-zh-tw-<r>`（core：`.../files/weekly-report-w46-zhtw-core`）→ **D54：同步 fanout 版 render.py** |
| run.py | fanout 与 production 同一 W47 式 runner（内容相同，仍列入同步表） |
| core-zh-tw 与 (zh-tw, en) | **core-zh-tw 兼 en 读者版**：production 下无 `2026-w46-zh-tw-en/` 目录；core 内含 `2026-w46-zh-tw-en.text.md`；MANIFEST §zh-tw-en (CORE) 明文 "core-zh-tw doubles as the en-reader edition"。en 版由 `render-zh-tw-core-w46/core/` 建。**closer 绝不能用 core 覆盖读者目录** |
| (zh-tw, zh-cn) 版 | 不存在（简/繁互斥），未编造 |
| 已发 text.md `###` 行 | 10/10 皆 **0 行 `###`、8 行 `##`** → **D47 不适用**（无行可丢）；D49 carry-over 不适用（导出器存在） |
| fanout `.text.md.new` 与 MANIFEST text pin | 10/10 SHA 吻合（de `5c5411e2…`、es `3896cdd0…`、fr `d3d37655…`、it `ccb4c196…`、ja `9240e553…`、ko `76511d17…`、nl `e67ba39a…`、pt `74678b1a…`、ru `3ef06342…`、en `5c22412b…`）；字节数 de 50143 / es 50390 / fr 51122 / it 49785 / ja 54394 / ko 52840 / nl 49273 / pt 49761 / ru 61885 / en 47635 |
| 已发 text.md vs fanout `.new` | 已发件更小（de 47681 … ru 59161）：旧式导出，换行不同 |
| 印 PDF | **未入仓**（MANIFEST 注明 build artifact, NOT shipped）；MANIFEST 有逐版字节 + SHA pin（见 §9 对照） |

### §0.3 字面盘点（D52，§5 详述）

- 已发网 PDF（issues/，`pdffonts` 逐版实测）：**10/10 全为 TC 面**——`LucernaNotoSansCJKTC` + `LucernaNotoSerifCJKTC`（Bold/Regular，多子集标签）+ `LucernaUnifrakturMaguntia-Regular ×1`。无 SC/JP/KR/Newsreader。
- 管治规则"复现已发版字面"：latin/ru 读者 + core 用 **TC 面**；ja 读者 **JP 面**、ko 读者 **KR 面**为机制指定行为（D53/D55/D56/D60），已裁定接受，不是缺陷。fr 家的 SC 面是 fr-specific（D51），不适用于本家。

### §0.4 安装核查（patched/ 已装机，2026-11-16）

- `_D5_READER` 位于 L132，10/10：latin（de/en/es/fr/it/nl/pt）×7、cjk（ja/ko）×2、ru（ru）×1。
- fix2 标记 5、`_QUOTE_CLS` 4、D5 block 1、`_CYR = range` 1，10/10 一致（与 W43/W45 zh-tw 先例同数）。
- 与基线 diff 行数：latin/ru 98 行、ja/ko 140 行（改名行在内）。
- 路由单元测试 `test_d5_routing_zhtw.py`：**10/10 FAILURES: 0，rc=0**。
- 幂等：同读者重装 = no-op；异读者重装 = FATAL（已验）。
- ja/ko 改名后残留 `\bTC\b`：仅 fix2 注释内 "SC/TC" 1 行（L146）；latin/ru 残留 15 处（TC 面本色，未动）。
- latin svglib（de/en/es/it）装机后逐字节相同（md5 唯一值 1 个）；fr/nl/pt/ru 因读者专属 wrap 修正各异（预期内）。

## §1 基线表（10/10 CLEAN，13 项检查/版）

基线构建：run rc=0 → render rc=0 → webpdf rc=0 → textexp rc=0，TOTAL 150/版；印 PDF 字节 + SHA 与 MANIFEST pin 逐版一致；naive textexp 与 fanout `.text.md.new` 逐字节相同；native verifier ADOPT（`實付金額`）；pdfdiff vs 已发网 PDF：trim `「實付金額」—|「實付金額」` 后 8 页 IDENTICAL（`—` 为 §1.1 预期变换：旧 `「實付金額」 — der Endbetrag…` → 新把本周词拆到独立行，破折号去掉；与 W45 `「金融科技」` 同形）；p8 extract 150/150 + compare CLEAN；print/web 字符多重集差 0。

| 版 | 印 PDF（B） | MANIFEST pin | census lat/cyr/curly_cjk | 13 项核查 |
|---|---|---|---|---|
| de | 16,757,957 | `955fcc3c…` ✓ | 602 / 0 / 1 | CLEAN |
| en | 14,485,787 | `6463dcd7…` ✓ | 577 / 0 / 0 | CLEAN |
| es | 15,978,939 | `1230d545…` ✓ | 603 / 0 / 0 | CLEAN |
| fr | 15,207,760 | `aa5e2e9a…` ✓ | 603 / 0 / 0 | CLEAN |
| it | 13,662,577 | `6dfc61b8…` ✓ | 590 / 0 / 0 | CLEAN |
| ja | 12,008,855 | `797b555a…` ✓ | 283 / 0 / 0 | CLEAN |
| ko | 10,081,582 | `fb24601f…` ✓ | 282 / 0 / 0 | CLEAN |
| nl | 13,664,637 | `9b868ee4…` ✓ | 602 / 0 / 0 | CLEAN |
| pt | 15,209,462 | `c00fda9f…` ✓ | 596 / 0 / 0 | CLEAN |
| ru | 8,845,916 | `d26888f4…` ✓ | 297 / 480 / 0 | CLEAN |

基线门禁（de 烟测，`gates_zhtw.py`）：17/19 PASS；两处 FAIL 皆为预期基线态——G3（D5 未装，lat=602）、G16（弯引号 defective=1，即 census 的 curly_in_cjk 1 处，p6）。其余 17 项全 PASS：G1 TOTAL 150、G2 head 0、G4/G5、G6 遮挡自检 OK + 0 旗标、G7 p8 150/150、G8 CLEAN、G9 freeze 8/8、G10 cjk_added 0、G11 0 SPILL（117 OBSERVE）、G12 0 DEFECT（备份在位）、G13 0 TOUCH/0 NEAR、G14 0 defects（ratios n=536 med=1.0，自比）、G15a print/web 差 0 + pdfdiff IDENTICAL + text.md BYTE-IDENTICAL、G15b rc=1（仅记录，D27）、G15c ADOPT、D18 最小间隙 21.0px（y=316 行 42.0px、y=378 行 21.0px）、D37 最小边距 31.5pt（内容边 1862 排除页脚带 y>2600 后最小边距 20.6px——页脚 "Seite 1 von 8" 按构造恰贴 1862.0，故排除；终轮全版同值）。

**基线事故（§10 详述）**：VM 重启（~08:58 UTC）杀死基线循环（pt 做到一半、ru 未开始）；`--resume` 续跑（de 因首版为前景手动跑、无 rc 行，重建一次；其余 7 版跳过）。续跑中 pt render.py 一次产出 120MB 印 PDF（9054 字体对象 vs 正常 48，Cairo 子集化偶发分裂）；重建一次即复现 MANIFEST pin 15,209,462 B、48 字体行——偶发，已解决，无代码改动。

## §2 逐版终轮门禁表

终轮标签：run1（de/en/es/fr/it/ko/nl/pt，8 版）、run2（ja、ru，2 版——各修 1 处后重建重验）。分母 **19 verdicts/版**（G1–G14 + G15a + G15c + G16 + D18 + D37；G15b 仅记录，不计分）。**G15a 全版 REFLOW（D30 接受）**：print/web 字符多重集差 0 + pdfdiff 8 页 IDENTICAL + joiner text.md 多重集 0，差异纯为 D5 换行（Newsreader 更窄，同行装更多词）；脚本按设计把 REFLOW 记为 FAIL，裁定见 D30，不计为真失败。

| 版 | 终轮 | G3 | G10 lat_added | G11 | G12/G14 | G15a difflines | G15b | G15c | G16 | D18 | D37 内容边 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| de | **18/19** run1 | 0/0/0 | 263 | 0 SPILL (132 OBS) | 0/0 | 108 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| en | **17/19** run1 | 0/0/0 | 253 | **2 SPILL**¹ (132 OBS) | 0/0 | 32 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| es | **18/19** run1 | 0/0/0 | 242 | 0 SPILL (132 OBS) | 0/0 | 302 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| fr | **18/19** run1 | 0/0/0 | 246 | 0 SPILL (131 OBS) | 0/0 | 132 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| it | **18/19** run1 | 0/0/0 | 222 | 0 SPILL (128 OBS) | 0/0 | 50 | rc=1 | ADOPT | 0 | 21.0px | **3.5px**² |
| ja | **18/19** run2 | 0/0/0 | 157 | 0 SPILL (132 OBS) | 0/0 | 500 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| ko | **18/19** run1 | 0/0/0 | 157 | 0 SPILL (**178 OBS**)³ | 0/0 | 100 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| nl | **18/19** run1 | 0/0/0 | 229 | 0 SPILL (133 OBS) | 0/0 | 42 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| pt | **18/19** run1 | 0/0/0 | 237 | 0 SPILL (129 OBS) | 0/0 | 82 | rc=**2**⁴ | ADOPT | 0 | 21.0px | 20.6px |
| ru | **18/19** run2 | 0/0/0 (noto_sans=1013)⁵ | 70 | 0 SPILL (137 OBS) | 0/0 | 510 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |

全版共通（终轮）：G1 TOTAL 150、G2 head 0、G4 render、G5 webpdf（< 7 MB）、G6 遮挡自检 OK + 0 旗标、G7 p8 extract 150/150、G8 p8 compare CLEAN、G9 freeze 8/8、G10 cjk_added=0、G13 0 TOUCH/0 NEAR、G16 defective=0、D37 最小边距 31.5pt（全版同一中文行 "折扣、回饋、免運，常常不能同時用。領券要先看門檻和名額：有的券先領先用，領完就沒"，y≈1423–1453，盒 y=1128）。D18 全版最小间隙 21.0px（y=316 行 42.0px、y=378 行 21.0px；en 副标题含 3 个 U+3000 段，故 6 个间隙值）。

注：
1. **en 2 SPILL 为基线先存残留，接受**：P4 盒底 1358.0 下 +4.20px "exercise?"（y=1362.2）；P7 盒底 1803.7 下 +6.30px "the invitation stays open."（y=1810.0）。基线 en 同盒、同偏移、同文本——D5 未引入。W45 前例（en/it/ru 各 1 SPILL）同样接受。
2. **it D37 内容边最小 3.5px**（元素 "Parola della settimana"，y=1750.0）——全家最紧，仍 PASS（> 0）。
3. ko G11 OBSERVE 178 处为全家最多（韩语行多），SPILL 0。
4. pt G15b rc=2：共享 verifier 无 pt 读者表（与 W45/W46-ko 家先例同）；仅记录，D27。
5. ru G3 noto_sans=1013：西里尔字母走 Noto Sans，D26 设计行为（`_D5_READER == "ru"` 分支），不是缺陷。ru G14 creambox ratios med=1.028（西里尔 advance 与 CJK 差异较大），defects=0，PASS。
6. ja run1 曾 16/19（G12 2 DEFECT、G14 1 defect，见 §3）；ru run1 曾 17/19（G11 1 SPILL，见 §3）。两版修复后 run2 均为 18/19。

## §3 修复表（字号 only）

共 **2 处修复**，均为字号下调（未改文案、未改盒高）。其余 8 版 run1 即 18/19 或 17/19（en 残留），零修复。

| # | 版 | 文件:行 | 内容 | 旧 → 新 | 依据（终轮前） | 修复后边距（实墨量测） |
|---|---|---|---|---|---|---|
| 1 | ja | `content56.py:21` | P5 gloss（arts-in-the-park） | 20.5 → **19.5** | run1 G12/G14：逻辑行 "界」。17の体験型アート屋台、900点以上の" 溢出 gloss 盒右缘 **+5.5px**（y=1092.925）；D5 重排使该行比基线多 1 字（"の"）。P6 同形 "キャッシュバックは割引ではありません。実" +4.5px 为基线原样（元素逐字节相同），未动 | P5 该 gloss 最紧行边距 **12.4px**（盒内）；run2 G12 0 DEFECT、G14 0 defects |
| 2 | ru | `content34.py:200` | P4 右盒俄语段 | 20 → **19.5** | run1 G11：**真 D5 回归**（基线 0 SPILL）：俄语段 "Пойдёте смотреть парад? Сколько раз в неделю вы занимаетесь спортом?" 在 Noto Sans 下多绕一行，"спортом?" 落在盒底 1358.0 之下 **+4.2px**（y=1362.2）。wrap 模拟：20pt → 3 行，19.5pt → 2 行（[374.8, 350.8]，内宽 378.5，余 27.7px） | 2 行，末行 y=1335.5，距盒底 **~17.6px**（计下行）；run2 G11 0 SPILL |

修复机制说明：ja 的 gloss 字号由 `bslib4.py:193-194` `gloss()` 硬编码 20.5——修法为 `gloss()` 加 `size=20.5` 参数（默认值不变，其余 11 处 gloss 调用不受影响），仅 `content56.py:21` 传入 `size=19.5`。ru 直接改该 `p.para` 调用的字号实参。

## §4 D19

`scripts/d19_check.py`（D48 修正逻辑，2026-11-16 补过三处——见注）：**TOTAL 7 PASS 7 FINDING 0，rc=0**（`logs/d19-check.txt`）。

核查范围：patched/ 10 份 KIT 的 D5 节 + 本报告全文中全部 `content*.py:NNN` 引用，共 7 处：

| # | 来源 | 引用 | 形式 | 结论 |
|---|---|---|---|---|
| 1 | KIT ja | `content56.py:21`（20.5 → 19.5） | kwarg-added：patched 行含 `size=19.5`，基线同行无 `size=`，行不同且在 fixlines 内 | PASS（旧值 20.5 在 `bslib4.py` gloss 默认值里，不在引用行——非 NN→MM 形） |
| 2 | KIT ru | `content34.py:200`（20 → 19.5） | NN→MM：patched 行含 19.5、基线行含 20、行不同 | PASS |
| 3 | 本报告 §3 表 L105 | `content56.py:21`（20.5 → 19.5） | kwarg-added（同 1） | PASS |
| 4 | 本报告 §3 表 L106 | `content34.py:200`（20 → 19.5） | NN→MM（同 2） | PASS |
| 5 | 本报告 §3 机制说明 L108 | `content56.py:21`（无箭头，提及） | 指向实际修改行 | PASS |
| 6 | 本报告 §8 表 L181 | `content56.py:21`（无箭头，提及） | 指向实际修改行 | PASS |
| 7 | 本报告 §8 表 L185 | `content34.py:200`（无箭头，提及） | 指向实际修改行 | PASS |

**修复引用均指向修复行本身**（ja 的 `size=19.5` 附加在 `content56.py:21` 调用处；ru 的 `20 → 19.5` 即 `content34.py:200` 行内实参）。无坏引用。

注（d19_check.py 本次修正，2026-11-16）：初跑 7 PASS 1 FINDING 6，6 处均为检查器局限而非引用错误：(1) 箭头正则不容 `**19.5**` 粗体标记（§3 表行）；(2) 只有 `tsize` 附加形，未覆盖 gloss 的 `size=` 附加形（ja KIT）；(3) 无箭头的提及行直接判错（§3 机制说明、§8 表行）；(4) BUILD 引用 slug 为占位符 "—"，需从同行解析读者码（ja/ru）。四处已修并重跑至 0 FINDING。

## §5 字面核查（D52）

管治规则：**重建版必须复现已发版字面**。已发版（issues/ 网 PDF，`pdffonts`）：10/10 全 TC 面（`LucernaNotoSansCJKTC` + `LucernaNotoSerifCJKTC` + Unifraktur ×1），无 SC/JP/KR/Newsreader。

重建版实测（印 PDF 为 Cairo 名、网 PDF 为 Lucerna 名；svglib index 计数为 `grep -c _XX_index`）：

| 版 | 已发面 | 重建印 PDF 面 | 重建网 PDF 面 | svglib index | 结论 |
|---|---|---|---|---|---|
| de | TC | NotoSans/SerifCJK**tc** + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans/SerifCJK**TC** + Unifraktur | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| en | TC | 同 de | 同 de | tc=2, sc/jp/kr=0 | ✓ TC 复现（core 亦然） |
| es | TC | 同 de | 同 de | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| fr | TC | 同 de | 同 de | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| it | TC | 同 de | 同 de | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| ja | TC | NotoSans/SerifCJK**jp** + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans/SerifCJK**JP** + Unifraktur | jp=2, tc/sc/kr=0 | ✓ JP 面（机制指定，D55） |
| ko | TC | NotoSans/SerifCJK**kr** + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans/SerifCJK**KR** + Unifraktur | kr=2, tc/sc/jp=0 | ✓ KR 面（机制指定，D56） |
| nl | TC | 同 de | 同 de | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| pt | TC | 同 de | 同 de | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| ru | TC | NotoSans/SerifCJK**tc** + **NotoSans** (Bold/Medium) + Newsreader16pt | Newsreader + NotoSans (Bold/Regular) + NotoSans/SerifCJK**TC** + Unifraktur | tc=2, sc/jp/kr=0 | ✓ TC 复现 + 西里尔 Noto Sans（D26） |

**结论：10/10 字面符合，无缺陷。** CJK 文本面与已发一致（latin/ru/core TC；ja JP、ko KR 为机制指定行为，已裁定接受，D53/D55/D56/D60——与 W43/W45 zh-tw 先例相同）。新增面均为 D5 机制行为：Newsreader（拉丁字母）、Noto Sans（西里尔字母），不改变任何 CJK 文本的字面。SC 面全家 0 处。fr 家的 SC 面（D51）为 fr-specific，不适用于本家。

## §6 core 关系

- **core-zh-tw 兼 en 读者版**：production 下**不存在** `2026-w46-zh-tw-en/` 目录（W45 有一 log-only 的同名目录，W46 连那个都没有）；core-zh-tw 内含 `2026-w46-zh-tw-en.text.md`；MANIFEST-W46 §zh-tw-en (CORE) 明文 "core-zh-tw doubles as the en-reader edition"。en 版由 `render-zh-tw-core-w46/core/` 构建，产出目录为 `core-zh-tw/`。
- 9 个读者目录（de/es/fr/it/ja/ko/nl/pt/ru）由各自 fanout 读者目录构建；en 由 core 目录构建。issues/ 下 10 个目录 `2026-w46-zh-tw-<r>/` 各含 `.md` + `.pdf` + `.text.md`。
- **closer 绝不能用 core 覆盖读者目录**：core 与读者目录是不同构建源；本家 scratch 内仅为 boxtitle core 对比建了符号链接（`baseline/core-zh-tw → 2026-w46-zh-tw-en`、`patched/core-zh-tw → 2026-w46-zh-tw-en`），同步表已排除，不进入交付。
- en 版的 KIT、印 PDF（`Lucerna-VOL3.pdf`）、网 PDF（`2026-w46-zh-tw-en.web.pdf`）、text 导出均以 `core-zh-tw` 源构建、归属 en 版；§8/§9 中 en 行即 core 行。

## §7 抽查

`scripts/spotcheck_zhtw.py`：3 探针/版，**30/30 PASS**（`logs/spotcheck.json`）。

| 探针 | 内容 | 结果 |
|---|---|---|
| P1 主标题 | "雙11來了！旅展落幕，購物車先列好" 在终轮 joiner 导出与已发 text.md 中 | 10/10 ✓ |
| 每周词计数 | `實付金額` 在终轮导出 vs 已发 text.md（去空白计数） | 10/10 ✓，均为 18 |
| P8 末键 | P8 SVG 中 "150." 行（同行拼接）vs 已发 PDF p8 末键行 | 10/10 ✓（de "150. Schreiben"、en "150. Writing"、es "150. Escritura"、fr "150. Écriture"、it "150. Scrittura"、ja "150. 作文"、ko "150. 쓰기"、nl "150. Schrijven"、pt "150. Escrita"、ru "150. Письмо"） |

探针修正记录（脚本事故，§10）：初版词计数朴素比对 18 vs 17——已发 text.md 中该词一次被旧导出器断行拆成 "比實\n\n付金額"，内容实为 18 次；改为去空白计数后 10/10 一致。P8 初版只取 "150." 单元素——D5 把末键行拆成多段（数字 CJK 面、词 Newsreader 面），改为同行（|Δy| < 1.0）且 x ≥ 种子元素 x 拼接（左栏习题同行，需排除）。

## §8 同步表

`scripts/sync_table.py`（KIT 更新后重跑）。逐版 9 个源文件 + KIT + production text.md。**无 JPG**（D20）。render.py 按 D54 同步（production 为死路径版）。

| 版 | 源文件不同 | 相同者 | KIT 不同 | text 导出（新 vs 已发） |
|---|---|---|---|---|
| de | 8/9（bslib4、content12/34/56/7/8、render、svglib） | run.py | 是 | 50,151 vs 47,681 |
| en | 8/9 | run.py | 是 | 47,637 vs 46,350 |
| es | 8/9 | run.py | 是 | 50,498 vs 47,926 |
| fr | 8/9 | run.py | 是 | 51,149 vs 48,653 |
| it | 8/9 | run.py | 是 | 49,786 vs 47,324 |
| ja | 8/9（+ content56.py:21 修复） | run.py | 是 | 54,698 vs 51,992 |
| ko | 8/9 | run.py | 是 | 52,890 vs 50,130 |
| nl | 8/9 | run.py | 是 | 49,282 vs 46,800 |
| pt | 8/9 | run.py | 是 | 49,762 vs 47,298 |
| ru | 8/9（+ content34.py:200 修复） | run.py | 是 | 62,036 vs 59,161 |

- svglib.py 差异最大（de 例：417 difflines，15,333 → 31,853 B；D1+D5 port 全量）。
- render.py 差异（de 例：14 difflines，1,324 → 1,803 B）：fanout 版 ED-relative `BASE`，替代 production 死路径。
- KIT 差异 = 追加的 D5 重建节（含终轮门禁、交付件字节 + SHA、修复引用）；KIT 前部与 production 逐字节相同（kit_update.py 断言通过）。
- text 差异 = D5 joiner 导出（D30 REFLOW，内容多重集 0；新导出字节更大——旧导出断行/漏行，见 §7）。
- 同步范围：8 个源文件 + WEEKLY-KIT.md + text.md.new（取 patched/ 侧导出件，§10）。core-zh-tw 符号链接不进入同步（§6）。

## §9 SHA-256 全值表

`scripts/sha_table.py`（网 PDF 以 builder 原件为准，**未重跑 webpdf**）。单网 PDF/版（zh-cn 家同；ko 家双网 PDF 不适用）。印 PDF 为 `Lucerna-VOL3[-XX].pdf`（en/core 为 `Lucerna-VOL3.pdf`）；网 PDF 为显式 `webpdf.py` 交付件 `<slug>.web.pdf`；text 为 D5 joiner 导出 `.text.md.new`。

| 版 | 印 PDF（B） | 印 SHA-256 | 网 PDF（B） | 网 SHA-256 | text.md.new（B） | text.md.new SHA-256 |
|---|---|---|---|---|---|---|
| de | 5,459,405 | `76a33a5d1bee41c30c223f0e0e891023fda5d3c2a550e919d2eda7910596ce78` | 1,502,046 | `f82e36d092a0cb6e795b86baa24c20df709278059f36844667fae1332602eddd` | 50,151 | `90ea2c2ac0b0e4469b94169460b75d8dcb043f8d9c949bc80b087e567ebeb49a` |
| en | 5,487,327 | `4d5b8a5bd8790246346dbfc5cb676cfb971a4b164e14c7745f05b2b8e3cccdc0` | 1,524,374 | `886f5b22a8812b5d0d01671be7f23df96e707e74200bfa64c1fd0de092c688e8` | 47,637 | `94a69e96bc43918507435ee980708f4764a146ab10317bf8be6f741b5d1e43a6` |
| es | 5,458,175 | `6e829430088dd70841a58af647992a16fea8a8cdfc2055580af0d96018ce6f7f` | 1,500,683 | `bb2a587e7ba477786a8f01c171b62ab03ec710c913e1a73767fda64d97c35feb` | 50,498 | `0b725f273c5a99bfa917d7b43174d0bf55d80a52281375301f428ce938655a07` |
| fr | 5,457,617 | `2bfbe2ffae514531a63f510457b4d3e0ad83ff7c75ce0766170179717e41696c` | 1,500,234 | `ab92c0be4f16d52d8e64bf6bdbb3c1f2805951825443b3a78d5d6edf3f0f7129` | 51,149 | `1b4f4dff528f1c844da9d7e451c2fba7f4d7a9652ff7fc9cd8497512b8020051` |
| it | 5,450,370 | `a6eddb2de4d67565252825e29232972bb56bc3d5067ed3958fdc6561bd08645b` | 1,492,979 | `85e658a6f085d14284f38a4d156ace62d34a7f2a7c234ee0d0d06e8c06c9df2c` | 49,786 | `1adece96780fb62c19be8196ecb4d1b08c78ce4058fde1fc4c792e0bd32f31a5` |
| ja | 10,357,989 | `e58162ee734b63accd8b362e4831ae2f666909ea0b988a49a7c2f0cc8d6b2207` | 2,059,919 | `37156d13b4f297d5e0905cf861690d0d10fe591e2620509a8b1ccfc629b58138` | 54,698 | `a02ae6e46ddf30516af81d430aeca4d4c3647ce0102c316fef023c1e31df1077` |
| ko | 6,598,426 | `c50a994489749dc8adbabd4789dffb699803f4ba303fdd696c0c4bd09d87c9c0` | 1,713,006 | `644b7747b87e93a5e0cba3d895dbd0eb3bad549d049b349a5eba96284adb30ff` | 52,890 | `141a571cd9198e29ce4647c7e801c46a6f0eecd10568c5474f6697cf76f82cdf` |
| nl | 5,451,565 | `b08643e57063edd54a209be78d662dec4434f93dc3e855a784f84635f80806b0` | 1,494,129 | `443d0c2b558f0c7d3cc2e3e11638a1dbec188b3f0b349b9f2738a261bf3af8a0` | 49,282 | `9b17f0577f3016d5b872dc5b61a4147b8467ec7363c01bc006024c0db7a64a6c` |
| pt | 5,460,061 | `08492b6502ffda21cb8556d746ca08ed28e7fab004f74bf81066d2961a59cac3` | 1,502,560 | `351a62ae294c5c8dfcc21242998e05562559c09a53c37d2ba4ba24bcd6faf3d5` | 49,762 | `a3336a63f91c057cb31760b70c4a2322b622c85118615bf85b1b1771b81e6d04` |
| ru | 5,638,728 | `92ad4ec2d045577cc435c1074f371a48a2aa77599fb33e20179bf2683ebb5499` | 1,678,623 | `92ed43a2eedbee006387b7c611e226cfe76145a15375a5cf8442ba2020a0cd05` | 62,036 | `be4f1ecfa424ec9ca0a78c5b5c2879ec35e35d9626d52ffa6ce1a86438a30df5` |

注：重建印 PDF 远小于基线印 PDF（de 5,459,405 vs 16,757,957）——已知 D5 效应，非缺陷：拉丁字母改走 Newsreader（极小子集），不再塞进 CJK 大子集（W45 前例：de 印 10,668,176 vs pin 20,445,173）。内容正确性由 G15a（print/web 多重集 0 + pdfdiff IDENTICAL）证明，不由字节数证明。ja/ko 印 PDF 较大（10,357,989 / 6,598,426）——JP/KR 面子集仍大，预期内。

## §10 closer 注意事项

- **text.md 取件路径**：patched/ 侧 D5 joiner 导出 `logs/<slug>/<slug>.text.md.new` 为准（§9 全值表即此件）。**绝不取基线 naive 导出**（D5 SVG 上 naive 导出会碎成单字行——W43 de 差 688 行；本家 joiner 在基线 SVG 上回归逐字节等于 fanout `.text.md.new`，已验）。已发 text.md 为旧式导出，不可直接复用。
- **D47 不适用**：已发 text.md 10/10 皆 0 行 `###`、8 行 `##`，无行可丢；joiner 导出未丢任何 `##` 行（§7 抽查 + G15c native verifier ADOPT）。
- **D49 不适用**：textexp_zh_tw.py 导出器存在且可用，无 carry-over。
- **字面结论**：10/10 复现已发字面（§5）。latin/ru/core TC、ja JP、ko KR；新增 Newsreader（拉丁）与 Noto Sans（西里尔）为 D5 机制行为。SC 面 0 处。
- **终轮门禁**：9 版 18/19（唯一 FAIL 均为 G15a REFLOW，D30 接受）；en 17/19（另 2 处 SPILL 为基线先存残留，见 §2 注 1）。G15b 仅记录（pt rc=2 为无 pt 读者表）。
- **en 残留**：2 处 SPILL 基线同在，不修（修了会改基线已发版式；W45 前例同样接受）。
- **ja P6 OBSERVE**：gloss 行 +4.5px（基线原样），不是缺陷，未动。
- **core 绝不能覆盖读者目录**（§6）；en 版交付件取 core 源、归属 en 版。
- **网 PDF 单件/版**：显式 `webpdf.py` 交付件 `<slug>.web.pdf`；render.py 内建 `Lucerna-VOL3-XX-web.pdf` 差 ~1 字节，不是交付件。
- **印 PDF 不入仓**：MANIFEST 注明 build artifact, NOT shipped；§9 印 SHA 仅供核对。
- **事故与工具修正记录**（本家全程）：
  1. VM 重启 ~08:58 UTC：基线循环中断（pt 半途、ru 未开始）；`--resume` 续跑（de 前景手动跑、无 rc 行，重建一次；其余 7 版跳过）。无数据丢失。
  2. pt 印 PDF 120MB 冷缓存偶发：重启后首 render 产出 120,961,253 B（9,054 字体对象，Cairo 子集化分裂）；按 W45 前例重建一次即复现 MANIFEST pin 15,209,462 B、48 字体行。无代码改动。**closer 注意**：若冷缓存后印 PDF > 40 MB，重建一次再核对 pin。
  3. joiner 合并 bug：初版按首段字体估算合并后 x，Newsreader 与 sans_TC 同串宽度差 10px，masthead 碎成单字；改为增量 `_end` 跟踪（每段按自家字体计宽）后修复；基线回归逐字节相同（de 50,143 B）。
  4. D18 量测 strip bug：裸 `.strip()` 会剥掉独立 U+3000 段（y=378 分隔符），D18 只量了 y=316；改为 `.strip(" \t\r\n")` 后全版 [42.0×3, 21.0]。
  5. G12 备份量测 bug：备份树初版只有 `svg/`，boxtitle 的 `load_svglib` 两次失败（缺 `svglib.py`、缺 `assets/lucerna-moth.svg`），backup_baseline 全空；补 `svglib.py` + `assets/` 后 10/10 备份在位（备份树 14M）。
  6. `run_joiner.sh` 一次未 `cd` 进 scratch 目录即跑，相对路径落空、joiner 未执行（stderr 被 `grep wrote` 吞掉）；文件仍为 naive 导出（difflines 2518）。重跑即正。**以后一律先 `cd` 再跑脚本。**
  7. **build_deliverables census 路径 bug**：脚本读 `logs/baseline-<slug>/census.json`（目录），真实文件为 `logs/baseline-<slug>-census.json`（仅 de 有目录，de 正确、其余 9 版误写 Latin 0）。已修脚本（优先平铺文件、目录为 fallback）、重建 deliverables.json、剥离 10 份 KIT 的错误 D5 节后重跑 kit_update.py；现 KIT census 与 §1 一致（ja 283、ru 297/480、de 602/0/1 等）。
  8. 抽查探针两次修正（§7）：词计数去空白（旧导出断行拆词）、P8 同行拼接限 key 栏。
  9. `build_deliverables.py` 加了逐版标签覆盖参数（`run1 2026-w46-zh-tw-ja:run2 2026-w46-zh-tw-ru:run2`），终轮标签不再伪装统一。
