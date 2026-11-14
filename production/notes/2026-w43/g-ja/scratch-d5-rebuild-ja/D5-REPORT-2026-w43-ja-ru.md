# D5 重建报告 — 2026-w43-ja-ru（俄语读者版）

W43 ja 家 D5 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader；西里尔字母改走 Noto Sans；日文正文仍走 Noto Sans/Serif CJK JP）。施工 2026-11-13/14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-ja/logs/2026-w43-ja-ru/`（`GATES-SUMMARY.txt` 为门禁总表）。
家族报告：`hidden_files/d5-redo/FAMILY-W43-JA-BUILD.md` §2–§9。

## 一、装机

- 本家走**移植模板路线**（D5-METHOD §1.7）：组装后的 fanout svglib（427 行，JP/TC 双下标 + `face=` 参数）被安装器按设计拒绝（`apply_variant.py --check` 死于 step 2 cmap，`pattern found 0x`；证据 `logs/installer-refusal-fanout.log`）。故 svglib 取移植模板 `svglib-ja-d5.py` 原样装为本版 `svglib.py`，只改 `_D5_READER` 一行。
- 本版 `_D5_READER = "ru"`；装后 svglib 与移植模板 `svglib-ja-d5.py` diff 恰好 1 行（`_D5_READER` 一行）；旧 `_D5_READER == "ru"` 分支在位（拉丁 AND 西里尔 → Noto Sans）。fix2 块 + `_QUOTE_CLS` + kinsoku（NO_START）齐全；旧分支 routing probe（在已装文件上实测 `_char_font`：拉丁→sans_noto、西里尔→sans_noto、fix2→news、CJK→sans）0 失败。
- **D26 纠正（2026-11-14）**：本报告初版按 Q4 裁定装为 fix-xru 态（删旧 ru 分支、与 W47 ja-ru 逐字节相同）；Q4 已被协调员 D26（2026-11-14 ~04:30，PLAN Amendments）取代——W43/W45/W46 的 ru-reader 版一律用安装器态旧分支，fix-xru 仅属 W47。证据：(1) 安装器正典代码 `tools/mechanism-w47/apply_variant.py` D5_BLOCK（L96–108）写明 `_D5_READER == "ru"` routes Latin AND Cyrillic to Noto Sans；(2) SOP §1.1 L64 字体表“俄语读者用 Noto Sans”，L67 Newsreader 无西里尔字形；(3) W43 已入仓并独立重校通过的 en-ru、es-ru 均为旧分支。2026-11-14 按 D26 重装（模板 + `_D5_READER="ru"`，不跑 `apply_variant.py`）+ 重建 + 重门禁；原 fix-xru 态作废，run1 门禁/交付物值（§四/§五旧值）一并作废。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（全家共用一次）。


- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `style-port-ja/textexp_ja.py` 新建导出（本家无已发 `.text.md`，11 份全新建，随 bundle 入仓）。

## 二、基线（修前组装版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- SVG 8/8 与 fanout 逐字节相同；textexp 与 fanout `.text.md.new` BYTE-IDENTICAL。
- 印 PDF 37,533,904 B，SHA 与 fanout D1 后印 PDF 一致；网 PDF 文字层 print=web 差 0、web vs fanout 网差 0；pdfdiff vs issues 已发网 PDF **IDENTICAL 8/8**。
- 修前普查 `d5_census.py`：D5 拉丁 214、西里尔 227、弯引号在 CJK 0（>0，符合装机前提）。
- P8：noted **150/150**（core 对照亦 150/150）。

## 三、缺陷与修法（D26 重建 run1 → run2）

D26 重建 run1（旧分支重装后首轮）出 2 门新红，同根——P2 餅图注 credit「写真：Fumikas Sagisavas — CC0（Wikimedia Commons）」在 Noto Sans 下实测宽 424.8px、超 CW 422.5，贪心断行后 kinsoku 尾字下移致「Wikimedia Common / s）」两行（15c HOLD：Page 2 仅此一处 token 差，`Commons` → `Common` + `s`）；图注多 1 行致“あなたは？”框下移 20.15px，末行俄语墨盒顶 1553.8 触季节横线 y=1554（occlusion LINEX 1 旗，`[87.0, 1553.0, 1863.0, 1555.0]` 触墨盒 `[1461.5, 1553.8, 1747.5, 1569.6]`；基线末行基线 1544.69、墨盒底 1549.2，离线 3.8px，本无此旗）。

修法（只动字号，未动任何文字内容）：仅该图注 credit 字号 15.5→15.0pt（实测 411.2px，复归一行；`bslib4.py` 的 `caption()` 加 `credit_size` 参数默认 15.5，`content12.py` 餅图注调用传 15.0；余 6 处 caption 调用不动）。其余 4 条长 credit（Bain/Hersom/Kratochvil 等）基线即 2 行、布局已计入，不动。run2 全量重建（run → render → webpdf → textexp）+ 全部门重跑：occlusion 0 旗、15c ADOPT（0 UNEXPECTED，REWRAP 30），其余门全绿（§四）。

- 门 15b `verify_textmd.py` carryover FAIL：共享校验器的表与 drop 规则按 pt 目标语家族标定，ja 目标语格式不在其覆盖内——基线（修前 port 期已验版）同跑亦 FAIL（ru 自身对照：基线 MD-only 1799 / SVG-only 2，run2 重建版 MD-only 1814 / SVG-only 4，增量仅 +15/+2，全是重排），故为**工具-格式口径差，非重建缺陷**（D27 裁定）。权威验收为门 15c：ja 原生校验器 `verify_textexp_ja.py --edition` **ADOPT（0 UNEXPECTED）**，与 it/es 家用各自原生校验器作门 15 权威证据同款。仅余 SVG-only 4 token（`200`、`hersom`、`／`、`〜` 各 1），均为 D5 run 拆分 token 化边缘——对应行在 SVG 与 .text.md 两侧俱全，无内容缺失。
- P8 行数 237→**238**：H 节（写作题）俄语指示 `Задание на письмо (единственно верного ответа нет); образец (150 знаков) — ниже.` 在 Noto Sans 下比 CJK sans 宽，2 行→3 行，下方整体下移约 30px；末行 y=703.9，距页脚线余量不变（49.4px），occlusion 0、creambox PASS。属良性 D5 重排，非缺陷，不修。

## 四、门禁（run2，17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0；noto_sans_elements=745 |
| 4 render | RC=0，印 PDF 37,658,315 B |
| 5 webpdf | RC=0，网 PDF 2,697,920 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[137, 138]——KIT 已登记的读者语答案键 #137/#138） |
| 9 freeze baseline | 8/8（patched 自复现） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings TOTAL 89，run 拆分所致；本家无 es 家的 U+3000 TOTAL 1） |
| 11 spill | 0 SPILL（0 SPILL, 117 OBSERVE） |
| 12 boxtitle | 0 DEFECT（32 titles，405 body lines；0 DEFECT, 0 OBSERVE, 0 marginal） |
| 13 edge | 0 TOUCH, 0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 237→238 行，slack 49.4→49.4px） |
| 15a 文字层 print=web | 字符多重集差 **0**（print 22280 = web 22280） |
| 15b verify_textmd carryover | FAIL（工具-格式口径差，见 §三；权威证据为 15c；D27 裁定） |
| 15c verify_textexp_ja --edition | **ADOPT**（0 UNEXPECTED；REWRAP 30，仅 D5 重排；8 页 token 全同） |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | ja 家无 gates.py |
| 18 masthead（D18） | **PASS**：标语右端→日期左端间距 **266.0px**（VOL 左缘误差 0.0、日期右缘误差 0.0） |

**OVERALL: 16/17 门 + D18 全绿；门 15b 为已解释的工具口径差（D27；权威 15c ADOPT）。**（run1 fix-xru 态门禁值作废：webpdf 2,624,973 B、15c REWRAP 26、刊头 261.4px、noto_sans_elements=719、spill 175 OBSERVE、boxtitle 46/599、freeze diff 拉丁 TOTAL 91。）

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；印 PDF 不入 issues）

- 印 PDF：`Lucerna-VOL1-RU.pdf`，**37,658,315 字节**，
  SHA-256 `bfbd7b5aad026a8bb1c5ae44e79edeea9f22b9c982117336463a2bea34ecf278`
  （D5 前基线 37,533,904 字节，`c545d49bfd0c…`；run1 fix-xru 态 37,584,200 字节，`fb3ad433…`，已作废）。
- 网 PDF：`2026-w43-ja-ru.web.pdf`，**2,697,920 字节**，
  SHA-256 `d6373f0c2316c5225794f5faae0ba833a48ac7d4c4ffad5bff6b513d5a625c53`
  （D5 前 issues 已发版 2,627,129 字节，`29d162d735b1…`；run1 fix-xru 态 2,624,973 字节，`f42fbcd4…`，已作废）。
- text.md：**新建** `2026-w43-ja-ru.text.md.new`，54,776 字节，
  SHA-256 `d71da6d92f3e8c1689e40e2d41ec880deabcc156c5531257d75a7d14fb804f25`
  （本家无已发 `.text.md`；与 fanout `.text.md.new` 的差异仅 D5 重排，15c ADOPT；run1 fix-xru 态 54,775 字节，`93be6414…`，已作废）。
- 练习总量仍为 **150 题**，与 core 逐题一致（KIT 注册表未变；keydiff [137, 138]）。

## 六、KIT

- `production/2026-w43/2026-w43-ja-ru/WEEKLY-KIT.md`：文末追加 **D5 rebuild（2026-11-13）** 节（装机、基线、门禁、新交付物 SHA/字节）。
