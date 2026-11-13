# D5 重建报告 — 2026-w43-en-ja（日语读者版）

W43 en 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-en/logs/2026-w43-en-ja/`
（`GATES-SUMMARY-run2.txt` 为门禁总表，`GATES-SUMMARY-run1.txt` 为修前总表，
`logs/2026-w43-en-ja-run1/` 为 run1 日志快照）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core en --week 2026-w43`
  → `production/2026-w43/core-en/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-en-ja/svglib.py --target en
  --reader ja --week 2026-w43`（先 `--check` dry-run，10 项改动 + mode cjk 正确）。
  装后 `_D5_READER = "cjk"`。安装器注记 `CJK index already JP`（本版已有 kinsoku，
  走 skip port，未触发 P1b 断言路径）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**（66 PASS）；fix2 块保留。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由
  `scratch-prep-p3b/en_textmd_w43.py` 导出（P3b T5 已验与 issues 已发版字节一致）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 149**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 与 `MANIFEST-W43-D1.md` 同字节、SHA 不同（元数据浮动，同批 4 版之一）。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF
  **非空字符差 0**，仅空格数差（webpdf 文字层空格推断浮动，D5-METHOD §3.7 同款情形，
  零词字符丢失）。
- 修前普查 `d5_census.py`：D5 拉丁 **402**、西里尔 0、弯引号在 CJK **1**（>0，符合装机前提）。
- 基线 P8 口径：noted **62/149**（与 core 同口径；de/fr 两版为 149/149）。

## 三、缺陷与修法（run1 → run2）

run1 共 14 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽约 5.7%；日语版奶油框标题多为英日双语长标题，超幅最大），另有
1 项既有缺陷（P2 spill，基线同值）。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P4 `B　SPORTS WORDS　スポーツの語` | 25pt 宽 431.9px，超栏 9.4（栏宽 422.5） | `content34.py:148` 25→**24**（414.6 ✓） |
| 2 | head_check | P5 `EARNINGS, IN PLAIN ENGLISH` | 26pt 宽 425.1px，超 2.6 | `content56.py:23` 26→**25**（408.8 ✓） |
| 3 | head_check | P5 `C　THIS WEEK, LIVE　現在進行形` | 25pt 宽 426.5px，超 4.0 | `content56.py:54` 25→**24**（409.4 ✓） |
| 4 | head_check | P6 `READING THE CHART　グラフを読む` | 24pt 宽 452.3px，超 29.8 | `content56.py:188` 24→**22**（414.6 ✓；23pt 433.4 仍超 10.9） |
| 5 | occlusion | P1 暗带标题与副标 `欧州は時計を戻す` 重叠 | 65.5×25.0px（副标 27pt 左缘 x=1639.0；44pt 标题右缘 1613.6 仅余约 3px 墨水空隙，不够） | `content12.py:25` 暗带标题 46→**42**（右缘 1545.4，空隙 93.6px） |
| 6 | occlusion | P1 `One team will now win the World Series for` 与 `　今週の数字` 重叠 | 8.5×12.8px | 随 #7 框标题缩小解决（与 core-en 同款） |
| 7 | creambox / boxtitle | P1 `THE WEEK IN NUMBERS　今週の数字` | +36.5px | `content12.py:43` 加 `tsize=21`（23pt 441.0，22pt 421.9 仍超约 17px，21pt 402.7 仅余 1.8px——与 core-en 同题同值，run2 复核通过） |
| 8 | boxtitle | P2 `AND YOU ?　あなたのことを話そう`（AND YOU 框眉，裸 `p.text` 24pt） | +2.8px | `content12.py:205` 24→**23**（386.5 ✓） |
| 9 | creambox / boxtitle | P3 `SAY IT ON THE NIGHT　夜のひと言` | +2.6px | `content34.py:25` 加 `tsize=22`（389.7 ✓） |
| 10 | creambox / boxtitle | P3 `DATES TO REMEMBER　今月の日程` | +13.1px | `content34.py:90` 加 `tsize=22`（399.4 ✓） |
| 11 | creambox / boxtitle | P4 `THE WEEK'S FIXTURES　今週の試合` | +22.7px | `content34.py:130` 加 `tsize=21`（23pt 444.9，22pt 425.5 仍超约 3px，21pt 406.2 ✓） |
| 12 | creambox / boxtitle | P5 `WORDS OF THE SCREEN　画面の語彙` | +31.9px | `content56.py:76` 加 `tsize=21`（23pt 436.4，22pt 417.4 仍超约 13px，21pt 398.4 ✓） |
| 13 | creambox / boxtitle | P6 `HEADLINE LANGUAGE　見出しの英語` | +39.2px | `content56.py:158` 加 `tsize=20`（23pt 443.7，22pt 424.4 仍超约 20px，21pt 405.1 仍超约 0.6px，20pt 约 385.8 ✓） |
| 14 | spill | P2 `Check your number !` 跌出 DID YOU KNOW 框底 | +12.71px | `content12.py:193` 框高公式尾数 +14→**+34**（框底 +20px；与 core-en 同款既有缺陷，基线同值） |

P8 变化：183→**183** 行，距页脚线余量 33.7→**33.7 px**（正，无溢出）。

## 四、门禁（run2，全套 17 门 ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 149，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 |
| 4 render | RC=0，印 PDF 13,208,214 B |
| 5 webpdf | RC=0，网 PDF 1,577,598 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 62/149（与 core 同口径） |
| 8 p8 compare | **CLEAN**（missing=[]，extra_count=0；keydiff=[136, 139, 149]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（194 OBSERVE） |
| 12 boxtitle | 0 DEFECT（49 titles，409 body lines；本次以基线 svg 为真对照，backup 已补） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 183→183，slack 33.7→33.7） |
| 15 文字层 print=web | 字符多重集差 **0** |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | en 家无 gates.py（`audit_en_fr.py`/`audit_en_es.py` 是旧版几何审计前身，不算 gate） |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）

- 印 PDF：`The-Lucerna-VOL1-en-ja.pdf`，**13,208,214 字节**，
  SHA-256 `7c89a5133c3c2bfe3e5b9a296ad0330b4621738e34b47d8771262eeaf7413eeb`
  （D5 前 KIT §2 记值 23,259,458 字节；日语版印 PDF 含 CJK 字体嵌入，体量大于拉丁版，
  属正常）。
- 网 PDF：`2026-w43-en-ja.web.pdf`，**1,577,598 字节**，
  SHA-256 `dbf79aa49de5afee65579ea0a0b7b88206fb203828b95ae586b93e3e35c670a3`
  （D5 前 issues 已发版 1,787,577 字节，`979e8017…`）。
- text.md：导出与 issues 已发版 **BYTE-IDENTICAL**
  （SHA-256 `b27b6f2cfa1947c9bcf3deb164a3ad84ceae9693d32eda21c57e97c179dd54b4`）。
- 练习总量仍为 **149 题**。

## 六、KIT

- `production/2026-w43/2026-w43-en-ja/WEEKLY-KIT.md`：§2 交付物与实测针脚追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **§10. D5 重建记录（2026-11-13）**
  （装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
