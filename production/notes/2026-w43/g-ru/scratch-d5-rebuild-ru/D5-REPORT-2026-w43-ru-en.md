# D5 重建报告 — 2026-w43-ru-en（英语读者版）

W43 ru 家 D5 + §1.1 合并重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字符由 Noto Sans CJK 改走 Newsreader / Noto Sans；本版为旧样式类，§1.1 组装来自 `style-port-ru/` fanout + D5 一次做完）。施工 2026-11-13–14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-ru/logs/2026-w43-ru-en/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表, `run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core ru --week 2026-w43 --i-understand-this-writes-production`
  → `production/2026-w43/core-ru/svglib.py` +263/−28 行，`_D5_READER = "latin"`（L107）；`import svglib` OK。
  core-ru 即 zh-cn 读者版的生产目录（`2026-w43-ru-zh-cn` 无独立生产目录），落盘值 latin；patched zh-cn 版装机后终值 cjk，与 core 差仅 `_D5_READER` 一行。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-ru-en/svglib.py --target ru --reader en --week 2026-w43`（先 `--check` dry-run）。
  装后 `_D5_READER = "latin"`；安装 diff +63/−2（D5 块 + fix2）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（本版 `fix2`=4 处、`_QUOTE_CLS`=4 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-ru/textexp_ru.py` 从 patched 源码导出（AST 路线，绝不从 PDF 反提；H1 取 fanout `.text.md.new` 首行 `"VOL.1 · Russian text · English explanations"`，WTYPE `writing`）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 22,280,654 B（MANIFEST 值 +0.001%，73 pdffonts 行），文字层 vs fanout 印 PDF 多重集差 **0**；网 PDF 2,332,240 B；网 PDF vs 已发件用 port 期工具 `pdf_text_diff_ru.py` + TRIM_ARGS（t2）→ **IDENTICAL**（印 PDF SHA 不作判据：确定性重渲已证但固定 +170 B vs MANIFEST，系 port 时代工具链漂移）。
- 修前普查 `d5_census.py`：D5 拉丁 **451**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 1。
- 基线 P8 口径：noted **150/150**（core 口径；keydiff 预期 [137, 138]）。

## 三、缺陷与修法（run1 → run2）

run1：14/17（13 门绿 + 门 17 N/A；门 6/12/14 红），刊头 PASS。（家族报告 §4 所写“15/17”为笔误，实为 14/17。）修法只动字号/断行与规则线位置，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| D1 | boxtitle/creambox 同项，P1 出处行 `From the Russian media, 15–20 October 2026` 越框 +2.5px（基线 −3.5px） | `content12.py:85` 出处行 19→**18pt**（同 de D1） |
| D2 | occlusion TEXTX，P1 目录行 `'A2' overlaps 'кино' 7.4×11.2px`（D5 新增；目录等级签右锚，Newsreader 粗体 advance +6.1px 吃掉基线 ~1px 间隙） | `content12.py:103` 目录标题 20→**19pt**（签 18pt 不动） |
| D3 | occlusion LINEX P2 ×6（基线同款，非 D5 新增；规则线穿 `Запомните` 句末行下行字母） | `content12.py:232` 规则线 `ey−12`→**`ey−8`**（下移 4px，下行字母底 ~1805，净空 ~2px；下方头顶 ~1824，仍余 ~16px） |
| D4 | occlusion LINEX P7（D5 新增，en 特有）：备注行 `An editor's example. VOL.2 prints letters!` 20pt 下 advance 381.8 > 栏内宽 378.5（仅超 3.3px），绕成 2 行，第 2 行 `letters!` 基线 y=1699.03 撞固定分隔线 y=1698 | `content7.py:90` wrap 测算与 `:96` p.para 两处同改，备注行 20→**19pt**（19pt advance 362.7 < 378.5，恢复 1 行，盒高回基线值） |

P8 变化：233→**233** 行，距页脚线余量 46.9→**46.9 px**（正，无溢出；D5 修复未触 P8 答案流）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（2 弯引号全在 Newsreader：U+201C×1、U+201D×1）；`noto_sans_elements=411` |
| 4 render | RC=0，印 PDF 21,911,614 B |
| 5 webpdf | RC=0，网 PDF 2,285,868 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**；keydiff=[137, 138] |
| 9 freeze baseline | 8/8（构建与重建同一解释器 venv；D2 freeze 门选项 (b)：D5 重建版 freeze 走 venv，基线 freeze 走 system python3 是预期行为） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 150，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（163 OBSERVE） |
| 12 boxtitle | 0 DEFECT（58 titles，713 body lines；本次以基线 svg 为真对照） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（n=404 median=1.023；P8 233→233，slack 46.9→46.9） |
| 15 文字层 print=web | 字符多重集差 **0**（印 39,585 字 = 网 39,585 字）；text.md BYTE-IDENTICAL（见 §五） |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | ru 家无 gates.py（`audit_ru_*.py` 是 port 期审计，不是 gate） |
| 18（D18）刊头 | 标语→日期间距 **289.6px**，PASS（gap ≤0 即真缺陷；本版余量极大） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`；W43 ru 在 `issues/` 内无已发 `.text.md`，closer 落仓时按 MANIFEST 把 `.text.md.new` 补进 `issues/`，新建，非覆盖）

- 印 PDF：`Lucerna-VOL1-ru-en.pdf`，**21,911,614 字节**，
  SHA-256 `bbb85d38244272d4292c67b02b3cc2eb0ca947975dee9e6dd28543881e5f59c7`
  （D5 前基线 22,280,654 字节；run1 印 PDF 21,911,603 B、网 PDF 2,285,840 B；D5 后通常变小，因嵌的 CJK 字形少了）。
- 网 PDF：`2026-w43-ru-en.web.pdf`，**2,285,868 字节**，
  SHA-256 `c633983434125e3ba9d77ab8a0a9909b5a1afed6b267fd072181059ad5425b5c`
  （D5 前基线 2,332,240 字节）。
- text.md：导出与 fanout `.text.md.new` **BYTE-IDENTICAL**
  （59,946 字节，SHA-256 `471768d603c58edf58c030f1d687f3e9348b452ad1cc578bb6bad5e5b7a819c9`）。
- 练习总量仍为 **150 题**，与 core 逐题一致。

## 六、KIT

- `production/2026-w43/2026-w43-ru-en/WEEKLY-KIT.md`：文末追加 `## 12. D5 rebuild (2026-11-14)`（装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）；Build/repro 的印/网 pin 行同步更新为本报告 §五实测值（KIT 旧 SHA 不可作基线，以实测发运值为准）。
