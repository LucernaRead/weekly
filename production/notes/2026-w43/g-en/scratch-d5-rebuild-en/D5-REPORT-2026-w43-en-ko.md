# D5 重建报告 — 2026-w43-en-ko（韩语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-ko/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-ko-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-ko/svglib.py --target en
  --reader ko --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode cjk 正确）。
  装后 `_D5_READER = "cjk"`。安装器注记 `CJK index SC -> KR`（韩文面重排）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 逐字节一致（7 行精确一致之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **399**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 10 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%），另有 1 项既有缺陷（P2 spill，基线同值）。修法只动字号，
**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超栏 2.6（栏宽 422.5） | `content56.py:23` 26→**25**（408.8 ✓） |
| 2 | head_check | P5 `B　SCREEN WORDS　화면 단어 빈칸` | 25pt 宽 435.8px，超 13.3 | `content56.py:41` 25→**24**（418.3 ✓） |
| 3 | occlusion | P1 暗带标题与副标 `유럽은 이번 주 일요일` 重叠 | 两处 TEXTX：`유럽은` 74.5×24.5px + `이번` 11.2×24.8px（副标 27pt 左缘 x=1612.5；44pt 标题右缘 1613.6 仍重叠约 1px） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4，advance 空隙 67.1px） |
| 4 | creambox / boxtitle | P3 `SAY IT ON THE NIGHT　그날 밤 표현` | +4.8px | `content34.py:25` 加 `tsize=22`（391.8 ✓） |
| 5 | creambox / boxtitle | P3 `DATES TO REMEMBER　이달의 날짜` | +8.9px | `content34.py:90` 加 `tsize=22`（395.7 ✓） |
| 6 | creambox / boxtitle | P4 `THE WEEK'S FIXTURES　이번 주 일정` | +23.9px | `content34.py:130` 加 `tsize=21`（23pt 446.4，22pt 427.0 仍超约 4.5px，21pt 407.5 ✓） |
| 7 | creambox / boxtitle | P5 `WORDS OF THE SCREEN　화면 단어장` | +27.6px | `content56.py:76` 加 `tsize=21`（23pt 432.6，22pt 413.7 仍超约 8.7px，21pt 394.9 ✓） |
| 8 | creambox / boxtitle | P6 `HEADLINE LANGUAGE　헤드라인 언어` | +33.2px | `content56.py:158` 加 `tsize=21`（23pt 438.0，22pt 419.0 仍超约 14px，21pt 399.9 ✓） |
| 9 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

附注：本版 boxtitle 计 66 titles、645 body lines、0 DEFECT（run2 实值；run1 为 76 titles、634 body lines、5 DEFECT），系韩语版框数多，非缺陷。

P8 变化：183→**182** 行，距页脚线余量 33.7→**33.7 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 10,013,644 B |
| 5 webpdf | RC=0，网 PDF 1,396,153 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（240 OBSERVE） |
| 12 boxtitle | 0 DEFECT（66 titles，645 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 183→182，slack 33.7→33.7） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-ko.pdf`，**10,013,644 字节**，
  SHA-256 `57e0a3e072b569b4ea26691e684790e271e35a976e21094b315b5fa33c71d8ed`
  （D5 前 KIT §11 记值 15,122,583 字节；韩语版印 PDF 含 CJK 字体嵌入，体量大于拉丁版，
  属正常）。
- 网 PDF：`2026-w43-en-ko.web.pdf`，**1,396,153 字节**，
  SHA-256 `40500e99cebaaa09867973eaa80d818aeea5bc6e3954ca4664c4435bc0e213c6`
  （D5 前 issues 已发版 1,478,283 字节，`6ce8cdc7…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `a1d45cf15662c0aa797e0fa58adea37edc99729ccc6a2be434a0ac377d9b839d`）。
- 练习总量仍为 **149 题**。

## 六、KIT

- `production/2026-w43/2026-w43-en-ko/WEEKLY-KIT.md`：§11 交付物与针脚追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **§14. D5 重建记录（2026-11-13）**
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
