# FIX-LOG — W47 ja-ru 第一轮返修 fix1

- 返修员：fix1（叶子）。开工：2026-11-11 03:37 EST / 08:37 UTC；收尾：2026-11-11 09:15 UTC 左右。
- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-ru/`（map：`hidden_files/w47/scratch-fanout-ja/map-ru.json`）。
- 依据：proof1 (b) 缺陷 D1–D4（`scratch-proof-ja-ru1/PROOF-NOTE.md`、GATE-LOG.md 已读）；
  SOP.md §8 与 §1.1 全文、AGENTS.md、brief-coordinator.md 已读（brief 实际路径在
  `goals/.../hidden_files/w47/briefs/brief-coordinator.md`，任务写的 weekly-git 路径不存在）。
- 未跑 insert.py、lint --write，未做任何 git 写操作；未碰 core-ja、其他家庭、tools/、issues/。

## 0. 探针与成品身份核实（盘上实测）

- PROBE1 `git hash-object -w` OK（f2789363…）；PROBE2 笔记目录写盘 OK；磁盘 45G 可用。
- 任务简报曾把两枚 SHA 写反，**以盘上实测为准**（与 FANOUT 报告一致）：
  print `Lucerna-VOL4-JA-RU.pdf` 25,858,425 B，SHA `abc44c9c695ddac9df434e93cf51e6eae5604c7f78b663331603dacc425a525f`；
  web `Lucerna-VOL4-JA-RU-web.pdf` 4,396,999 B，SHA `e2fc538241a3d1446ab78dab0acfa411b0f95f126a7c926a82f69fe7d350e94e`。
- 修前 text.md 核对：`Уми-но-уми` 1×、`Фудзирюг` 5×、`Фудзирёг` 0×，与任务所给实测一致。
- 备份：修前 `WEEKLY-KIT.md` / `EDITION-RECORD.md` / `2026-w47-ja-ru.text.md` /
  `ABSTRACT.txt` 已拷入本目录（apply 会清空整版目录，KIT/RECORD 须事后恢复）。

## 1. 修复内容（map-ru.json，共 9 处键/值改动）

### D1（严重，5 条 map 值 → 6 处渲染）
| map 键 | 旧值 | 新值 |
|---|---|---|
| 首日败给丰升龙的是美之海 | Уми-но-уми проиграл в 1-й день Хосёрю | Чура-но-уми проиграл в 1-й день Хосёрю |
| 第三天战胜丰升龙的是藤凌驾 | Фудзирюга победил Хосёрю на 3-й день | Фудзирёга победил Хосёрю на 3-й день |
| 藤凌驾的金星是初登场后第11个场所 | Кинбоси Фудзирюги: 11-й турнир с дебюта | Кинбоси Фудзирёги: 11-й турнир с дебюта（供 #54/#111 两处） |
| 藤凌驾第三天拿到金星 | Фудзирюга выиграл кинбоси на 3-й день | Фудзирёга выиграл кинбоси на 3-й день |
| 丰升龙第三天输给了藤凌驾 | Хосёрю проиграл на 3-й день Фудзирюге | Хосёрю проиграл на 3-й день Фудзирёге |

### D2（meta p8_bridge）
`Письменное задание (единственно правильного ответа нет)` →
`Письменное задание (единственного правильного ответа нет)`。

### D3（#86 注，机构名补全）
`Прогноз Японии: Арасияма с 13 нояб.` →
`Прогноз Японской метеорологической ассоциации: Арасияма с 13 нояб.`
（en/fr 皆写全机构名；新值在 P8 折为两行，几何门 0 flags，见 §3）。

### D4（P7 诊所第 4 条）
`Оканчивайте глагол формой ます.` →
`Глагол должен оканчиваться формой ます.`
（proof1 建议译法；新值在诊所框内折为两行，几何门 0 flags，见 §3）。

### 附带发现：core-ja 事后改键导致 map 键过期（不在 D1–D4 内，修时撞见）
- 首轮重 apply 报 rc=1：`MAP key never occurs quoted in core: '首日战胜大之里的是一之富士'`。
- 根因：core-ja 在 ru fanout 之后自行修过 `一之富士 → 义之富士`（core-ja `ja-gates.log:16`、
  `WEEKLY-KIT.md:393-414` 有记录，content34.py:186 现为 `首日战胜大之里的义之富士`），
  map-ru.json 的旧键对不上，致该条注文（#47）在重建版里残留中文原文
  `首日战胜大之里的义之富士`——apply 的 frozen 集豁免了它，故未报 leftover。
- 处理（只改 map，不碰 core-ja）：map 键改为 `首日战胜大之里的义之富士`，值不变
  （`Ёсинофудзи победил Оносато в 1-й день`）。第一次改键时我漏写“是”字，
  第二轮 apply 仍 rc=1，纠正为仅 `一→义` 后第三轮 apply rc=0。
  221 键完整，JSON 校验通过。旧版 text.md 里 #47 本就是正确的俄语值，故新旧
  text.md diff 无 #47 行（见 textmd-fix1.diff）。
- 知会协调员：同类 drift 可能存在于其他 fanout 语的 map（凡引用 `一之富士` 旧键者），
  各语重 apply 前应先跑一次 apply 看有无 MAP-key 告警；不在本棒范围，未动。

## 2. 重建流程

1. `tools/venv/bin/python apply.py ru`（第三轮 rc=0，`APPLY ru: OK`，221 keys + 6 instr）。
   前两轮 rc=1 均为上述过期键所致，文件已写入、仅告警 1 条；第三轮 0 问题。
2. 恢复被 apply 清空的 `WEEKLY-KIT.md` / `EDITION-RECORD.md`（备份拷回）。
3. `tools/venv/bin/python run.py`（build-fix1-run1.log）：rc=0，FLOW OVERFLOW /
   HEAD TOO WIDE 0 条，TOTAL 150（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38；范文 154 字）。
4. `tools/venv/bin/python render.py`（单进程；事前查 ps 确认本版目录无并行渲染；render-fix1.log）：
   rc=0，8 cards + print PDF 25,858,387 B。
5. `tools/venv/bin/python tools/webpdf.py svg Lucerna-VOL4-JA-RU-web.pdf`
   （webpdf-fix1.log）：rc=0，4,396,966 B，53,363 text bytes。
6. `export-textmd-ru.py`（export-textmd-fix1.log）：rc=0，53,029 B，1382 行。
7. 新旧 text.md diff（textmd-fix1.diff，36 行）：恰为 D1 6 处 + D2/D3/D4 各 1 处，
   别无任何差异。D3、D4 注文各多折一行（行数 1380→1382）。

## 3. 新成品身份（终验复核，与 KIT/RECORD 记录一致）

| Item | Bytes | SHA-256 |
|---|---|---|
| Print PDF `Lucerna-VOL4-JA-RU.pdf` | 25,858,387 | `86af0bb5bd5fb3e2a521cb92cd355185b9e3a1bd297511121b11d30e2f2a1592` |
| Web PDF `Lucerna-VOL4-JA-RU-web.pdf` | 4,396,966 | `dd5fdc63020f5365c714937ac5835c057cd5b42a56005011ce35c6e8db86ef57` |
| `2026-w47-ja-ru.text.md` | 53,029 | —（1382 行） |
| `ABSTRACT.txt` | 464 | —（未变，apply 由同一 meta 重写，内容同前） |

- KIT §7/§8/§11 与 EDITION-RECORD.md 已更新为 fix1 数值与 F3 记录；
  KIT §11 旧句“Фудзирюга / Уми-но-уми”已按正形更正。
- 修前值存档：print 25,858,425 / `abc44c9c…`，web 4,396,999 / `e2fc5382…`。

## 4. 插曲：EDQUOT（Errno 122，一过性）

- 目视渲染页图时首次 `mkdir` 报 `Disk quota exceeded`（df 仍有 45G 可用，
  属共享配额瞬时峰值——当时另有 zh-cn-de、ko-en 等兄弟返修在并行渲染）。
- 按任务指令停手：本笔记目录仅 260K，无可清的大中间件（只有小日志/备份），
  故未删任何文件；小写盘随即恢复正常（touch/mkdir 均 OK），遂重试一次，
  把 16 张页图改写到 /tmp（一次性中间件，本就该放 /tmp），成功。
  无文件丢失、无工作重做。

## 5. 结论

- D1–D4 全部修完；新形 `Фудзирёг` 5×、`Чура-но-уми` 1× 就位，旧形全清零
  （py/SVG/text.md/双 PDF 文字层）；附带修好 #47 过期键 1 处。
- 全套门禁重验全绿（见 GATE-LOG.md）；print 8/8 + web P7/P8 目视全过。
- 待第二轮全量复校（协调员另派）。
