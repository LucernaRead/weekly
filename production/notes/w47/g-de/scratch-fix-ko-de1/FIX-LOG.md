# FIX LOG — W47 ko-de, fix round 1 (builder fix1 · 2026-11-11)
# 对象：production/2026-w47/2026-w47-ko-de/（proof1 run 2 成品）
# 任务：只修 D1、D5。D2/D3/D4/D6 是 core-ko 的问题，由核心线另修、全家重扩——未碰。

## 开工身份核实（盘上逐字核实，与任务书一致）
- 印版 Lucerna-VOL4-KO-DE.pdf：45,682,479 B，SHA bcf8f141b015d01d32eff843ce0970751fce996d99ea5ddeaca9ffb913c4fda6 ✓
- 网版 Lucerna-VOL4-KO-DE-web.pdf：4,037,656 B，SHA 101073970b4eb50c514a105741f262ae98d6cc681427221e3527c0771be9b604 ✓
- text.md 2026-w47-ko-de.text.md：26,597 B，SHA a298889b64ef43918920c4c728d23b36058910a2c878202e9471056c5869e3e7 ✓
- 8 SVG 预修哈希与 KIT run 2 记录逐个一致（见 sha-svg-pre.txt）。
- 开工探针通过：`git hash-object -w --stdin` 返回 9daeafb9864cf43055ae93beb0afd6c7d144bfa4（与 proof1 相同值），笔记目录可写（PROBE.txt）。磁盘 df 45G 空闲。
- 先读：SOP.md §8 + §1.1 全文、AGENTS.md、proof1 PROOF-NOTE.md / GATE-LOG.md 全文。
  任务书写的 brief 路径 `~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md` 在盘上不存在；
  该文件实际在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`，已读该处副本（已记入 KIT fix1 节）。
- 预检 D1：8 SVG 全扫 U+201C=2、U+201D=2（全在 p7-mal.svg）、U+2019=0；核心 core-ko 三者皆 0。核心同款写法已核对：core-ko content7.py:81 `wcn = "句式拆解：「在〜之后」。提问：「〜 후에 뭐 해요?」"`。
- 预检 D5：content12.py:174 `작황 = die Ernte` 属实；其余 19 条术语注未动。

## 改动（仅 2 行源码 + 由此重建的成品；未碰 core-ko、其他家庭、tools/、issues/）
### D1 — content7.py:81
- 改前：`wcn = "Rahmen: “nach ~”. Frag: “〜 후에 뭐 해요?”"`
- 改后：`wcn = "Rahmen: 「nach ~」. Frag: 「〜 후에 뭐 해요?」"`（核心同款 「」 包裹）
- 动手前先实测：core `svglib.wrap`（`/usr/bin/python3`，锁定的构建解释器）——新旧 wcn 均为 2 行（378.5px 宽、20pt sans），框高 wh 不变、P7 teaser 末端不变。

### D5 — content12.py:174
- 改前：`f.gloss("조사하다 = untersuchen · 작황 = die Ernte · 이어지다 = weitergehen · 할인 = Rabatt")`
- 改后：`f.gloss("조사하다 = untersuchen · 작황 = Ernteaussichten · 이어지다 = weitergehen · 할인 = Rabatt")`
- 选用理由：작황（作況）指作物长势 / 收成前景，不是"收获"本身；句中「가을배추를 많이 심었고 작황도 좋았어요」意为秋白菜种得多、长势也好。
  核心中文注为「작황 收成、长势」（收成 + 长势两义）；`Ernteaussichten`（收成前景）同时覆盖两义，且是「작황이 좋다」
  的惯用德语说法（die Ernteaussichten sind gut）；`Anbaubedingungen` 只指栽培条件（成因），不指作物本身的状态与预期收成，故不取。
  另：`Ernteaussichten`（15 字母）比 `Anbaubedingungen`（17 字母）短，且与本版注文体例一致（裸名词，如 `할인 = Rabatt`、`효능 = Nutzen`）。
- 动手前先实测：含 `Hinweis — ` 前缀、386.5px 内宽，20.5pt sans——新旧均为 3 行，P2-feature 末端不变。

## 重建（与 run 2 同一锁定工具链）
1. `/usr/bin/python3 run.py`（build-fix1.log）：0 FLOW OVERFLOW / 0 HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；各页 10/18/18/18/18/18/12/38）；P2-feature 1531（下限 1540）；P7 teaser 2539.22（页脚 2580）；P8-keys 2457；范文 169 字。
2. `tools/venv/bin/python render.py`（render-fix1.log）：8 张 PNG + 印版 PDF。
3. `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-KO-DE-web.pdf`（webpdf-fix1.log）：8 页，540 distinct chars（原 542，弯引号退出字体子集），52,015 text bytes。
4. `/usr/bin/python3 textmd.py . 2026-w47-ko-de 2026-w47-ko-de.text.md "Lucerna Korean Weekly VOL.4 — Korean text, German explanations (2026-W47)"`（textmd-fix1.log）：332 items。
   重建前已验证该命令可逐字节复现旧 text.md（diff 0），故新 text.md 只差 D5 那一行。

## 重建后成品（新哈希）
- 印版 Lucerna-VOL4-KO-DE.pdf：45,682,367 B，SHA c19fe6c12ee7f34515110a506072e593b92580efcf4d268dd67f44c3e8be3f38
- 网版 Lucerna-VOL4-KO-DE-web.pdf：4,035,061 B，SHA 375f0cf79e6c4592edc504cdafcca469aff402ee79393aa694a5cb4cc3dd0878（< 7 MB）
- text.md：26,603 B（+6），SHA a76413749471ee248e5f6bf4c83d1047a63e3134104f9fd63098c148196ca0d1；与旧版 diff 仅第 157 行（D5 注文）。
- SVG：仅 P2（92390ad4…→cfab7ef105e3eee5e7ed3ef787bb9b750246d11bc84b0c253f58c4b5f9df920b）、P7（50e68b61…→64b828232bd7ccd6a48446f47cdacc6ceacfe7bed598bfdee5b9e27995672606）变化；其余 6 张逐字节一致（sha-svg-pre.txt / sha-svg-fix1.txt）。
- 文字层：印版/网版 pdftotext 各 52,015 字节，逐字节一致（较 run 2 的 52,009 增加 6 字节 = `Ernteaussichten` 替换 `die Ernte` 的净增；「」与弯引号均为 3 字节，互抵）。
- PDF 文字层核对：P2 `Ernteaussichten` ×1、`die Ernte` ×0；P7 `「nach ~」` 在、`“nach` 不在；P7 全文 U+201C/U+201D 各 0。

## 未碰项
- D2（ex 10/47 어디예요）、D3（ex 48 시리즈 중복）、D4（金句 #7 自引）、D6（text.md 缺 P7 信件三段 / textmd.py 缺口）：一行未改。注意：本轮进行期间核心线已在盘上修好 core-ko 的 D2/D3/D4（content12.py:157、content34.py:199/201、content7.py:80/130，mtime 2026-11-11 08:40 UTC）——本版韩文原文仍冻结于旧核心，待全家重扩时带入。
- 未跑 insert.py、lint --write，未做任何 git 写操作（另：`production/2026-w47/` 整树在本地克隆中为未追踪状态 `??`，故 git diff 为空；改动凭哈希快照记录）。
- KIT：仅在末尾追加 "Fix round 1" 一节（新哈希 + 门禁结论），历史 run 2 记录未改。
- 叶子：未派 subagent。

## EDQUOT 事件（一次）
- 写 freeze-baseline 日志时报 Errno 122（df 显示盘余 45G，属配额）。按指令立即停手：仅删本人笔记目录内可复现中间件（`freeze/` 68M，freeze.py 可重跑复现）+ 0 字节残日志；重试一次，freeze 的 --out 改放 /tmp（用后即删），基线 8/8 通过；小体积日志写盘恢复。未删任何他人文件。第一次失败时 freeze/ 内只有 build-copy 与空 svg/（重建未完成），无可用结论；重试的完整日志见 freeze-baseline-fix1.log。
- 其余写盘（render/webpdf/textmd/各门禁日志）均正常。

## 待协调员（proof2 注意）
- 本轮 proof2 仍按修后成品做全量复校；核心修后全家重扩时本版须重建（届时 D2/D3/D4/D6 一并带入，freeze diff 基线随之改变）。
- freeze diff 对当前新核心新增 CJK 16 个（见 GATE-LOG.md 第 3 门）：其中 9 个是冻结滞后 artifact（D2/D3/D4 旧韩文），非本轮引入；逐字裁定见 GATE-LOG。
- proof1 观察项（EDITION-RECORD.md Files 一节误贴 ko-en 文件名/哈希）是 builder 记录笔误，不在成品内，本轮未动他人笔记目录，特记于此供协调员转达。
