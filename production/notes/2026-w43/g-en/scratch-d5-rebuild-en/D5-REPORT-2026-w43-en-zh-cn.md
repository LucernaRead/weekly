# D5 重建报告 — 2026-w43-en-zh-cn（core-en，简体中文读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Noto Sans CJK
改走 Newsreader/Noto Sans）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后
的 closer 做）。工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-zh-cn/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表）。

## 一、装机

- Core 落盘：`apply_variant.py --patch-core en --week 2026-w43
  --i-understand-this-writes-production` → `production/2026-w43/core-en/svglib.py`
  +95/−3 行，`_D5_READER = "latin"`（L100）。W47 未动。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-zh-cn/svglib.py --target en
  --reader zh-cn --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode cjk 正确）。
  装后 `_D5_READER = "cjk"`（core-en 目录本身按 zh-cn 读者装，终值 cjk——与 W47 的
  6 个 cjk core 一致，是预期状态）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**（W43 en 为 149 题，非 W47 的 150），0 FLOW OVERFLOW /
  0 HEAD TOO WIDE。
- 印 PDF：21,867,600 B，与 `MANIFEST-W43-D1.md` 差 −2 B（元数据浮动，同批 4 版之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**（各 101,517 字符）；自建网 PDF vs
  issues 已发 web PDF **非空字符差 0**，仅空格数差 447（webpdf 文字层空格推断浮动，
  D5-METHOD §3.7 同款情形，零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **403**、西里尔 0、弯引号在 CJK **3**（>0，符合装机前提）。
- 基线 P8 口径（`tools/p8.py extract --total 149`）：noted **62/149**（core 口径；
  fanout 版多为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 9 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号与
框高，**未动任何文字内容**；修前日志已快照至 `logs/2026-w43-en-zh-cn-run1/`。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P3 `B　FESTIVAL WORDS　节日词填空` | 25pt 宽 434.2px，超栏 11.7（栏宽 422.5） | `content34.py:43` 25→**24**（416.8 ✓） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | head_check | P5 `C　THIS WEEK, LIVE　现在进行时` | 25pt 宽 426.5px，超 4.0 | `content56.py:54` 25→**24**（409.4 ✓） |
| 4 | occlusion | P1 暗带标题与副标 `本周日欧洲拨钟` 重叠 | 38.5×25.0px | `content12.py:25` 暗带标题 46→**44**（标题右缘 x=1613.6，副标左缘 x=1666.0，空隙 52.4px） |
| 5 | occlusion | P1 `One team will now win the World Series for` 与 `　数字看本周` 重叠 | 8.5×12.8px | 同 #6（框标题缩小后副标右缘内收） |
| 6 | creambox / boxtitle | P1 `　数字看本周` | +36.5px | `content12.py:43` 奶油框 `THE WEEK IN NUMBERS　数字看本周` 加 `tsize=21`（23pt 441.0、22pt 421.9 仍超，21pt 402.7 才够） |
| 7 | creambox / boxtitle | P3 `　当晚这样说` | +3.6px | `content34.py:25` 奶油框 `SAY IT ON THE NIGHT　当晚这样说` 加 `tsize=22`（23pt 408.1，22pt 390.4 ✓） |
| 8 | creambox / boxtitle | P5 `　屏幕词表` | +8.9px | `content56.py:76` 奶油框 `WORDS OF THE SCREEN　屏幕词表` 加 `tsize=22`（23pt 413.4，22pt 395.4 ✓） |
| 9 | spill | P2 `Check your number!` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` DID YOU KNOW 框高公式尾数 +14→**+34**（框底 +20px；溢出行墨水约 2.8px 入框内；下方 AND YOU 框底随之 +20px 至 1554.6，距 y=1558 的 TELLING THE TIME 横线 3.4px，无接触）。**基线同样 1 SPILL（39 boxes，1 SPILL）——既有缺陷，非 D5 造成，但门禁要求 0 SPILL，须修** |

P8 变化：182→**181** 行，距页脚线余量 33.7→**33.7 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（6 弯引号全在 Newsreader） |
| 4 render | RC=0，印 PDF 9,076,058 B |
| 5 webpdf | RC=0，网 PDF 1,457,171 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（core 对自身，keydiff=[]） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 382，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（181 OBSERVE） |
| 12 boxtitle | 0 DEFECT（55 titles，389 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 182→181，slack 33.7→33.7） |
| 15 文字层 print=web | 字符多重集差 **0**（各 100,785 字符） |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-zh-cn.pdf`，**9,076,058 字节**，
  SHA-256 `ed53b86f7f11e7f36dc2ffff8ba7d9239a348923e51a8150ce21ad6c46ef78d6`
  （D5 前 24,496,906 字节，见 KIT §十一；D5 后变小属预期——新渲染管线不再内嵌未压缩整版图）。
- 网 PDF：`2026-w43-en-zh-cn.web.pdf`，**1,457,171 字节**，
  SHA-256 `ae8c2e4a7d3a13ad0ecb790d3a0617646325f8fd2673c4040a8bf89dd38de533`
  （D5 前 issues 已发版 1,705,044 字节，`9a10aa9d…`）。
- text.md：导出 `logs/2026-w43-en-zh-cn/2026-w43-en-zh-cn.text.md.new` 与 issues 已发版
  **BYTE-IDENTICAL**（SHA-256 `b45f90ad63dba5328e5b3b041ef36775caad370e7d42dbbab0951c843c91d849`）。
- 练习总量仍为 **149 题**，文字层字符数与 D5 前一致（text.md 字节一致；印/网文字层差 0）。

## 六、KIT

- `production/2026-w43/core-en/WEEKLY-KIT.md`：§一追加 D5 交付物行（新 SHA + 字节数，
  注明 D5 前值）；文末追加 **§十二、D5 重建记录（2026-11-13）**（装机、基线、缺陷与
  修法、门禁 ALL-GREEN、新交付物）。§四体量数未变（149 题；文字量不变），故不改。
