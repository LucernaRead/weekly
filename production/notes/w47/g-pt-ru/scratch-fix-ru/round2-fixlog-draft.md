# FIX-LOG §8 第二轮修复（草稿；数字待 round2-summary.txt / round2-gates/summary.txt 填齐后定稿）

## 8. 第二轮修复（2026-11-12，接 PROOF-NOTE-2 的 6 项 low 发现）

- 任务：第二轮独立重校 PROOF-NOTE-2（`scratch-reproof2-w47-ru/PROOF-NOTE-2.md`）的 6 项 low 发现 G-1～G-6；第一轮 PROOF-NOTE 与本 FIX-LOG 全文已读。
- 范围：`production/2026-w47/` 内 ru 家 8 版（`2026-w47-ru-{en,de,fr,it,pt,nl,ko,zh-tw}`）；core-ru、ru-es、ru-ja 干净未动；不碰其他家庭、其他周；不 commit、不 push、不跑 lint。
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python` 全程。
- 流程（SOP §8）：改源头 content*.py → `run.py` → `render.py` → textmd 干跑到 /tmp → diff → 回补被丢标题行 → 落盘 text.md → `webpdf.py` → 门禁 → KIT 更新为盘上实际 SHA。
- 磁盘：开工 95G 已用（门限 100G，全程未触发）。

### 8.1 人称裁定（G-4）：各版主导人称以其余部分的祈使/人称标记为准

| 版 | 主导人称 | 证据（其余部分） | 改动 |
|---|---|---|---|
| ru-de | Sie（正式） | `Lesen Sie / Setzen Sie / Bilden Sie / Füllen Sie / Antworten Sie / Fassen Sie`（6+ 处 Sie 式祈使）；du 仅见于 G-4 说明句本身 | 标题 `UND SIE?` 不动；说明 `Und du? Schreib …` → `Und Sie? Schreiben Sie …`（wrap 计高 + 正文两处同改） |
| ru-fr | vous（正式） | `Lisez / Complétez ×2 / Formez / Répondez / Réunissez`；tu 仅见于 G-4 说明句本身 | 标题 `ET VOUS ?` 不动；说明 `Et toi ? Écris …` → `Et vous ? Écrivez …`（两处同改） |
| ru-it | tu（非正式） | `Leggi/scegli ×4+ / Completa ×4 / Metti / Forma / Rispondi / Unisci`；voi 仅见于 G-4 标题本身 | 标题 `E VOI?` → `E TU?`；说明 `E tu? Scrivi …` 不动 |
| ru-nl | U（正式） | 正式物主 `uw` 约 20 处（content12/34/56/7/8）；`jij` 仅见于 G-4 说明句本身，`je` 仅 1 处（L427 通用 `je`） | 标题 `EN U?` 不动；说明 `En jij? Schrijf …` → `En u? Schrijf …`（两处同改；`Schrijf` 两式同形） |
| ru-pt | tu（非正式） | tu 式约 18 词次（`Lê/escolhe ×4`、`Completa ×4`、`Escreve`、`Traduz ×4`）；você 式约 8 词次（`Leia/escolha`、`Complete ×2`、`Forme ×2`、`Responda`、`Junte`） | 标题 `E VOCÊ?` → `E TU?`；说明 `E tu? Escreve …` 不动；L471 `Responda …` → `Responde …` |
| ru-ko | 여러분（复数） | L35 P1 标题 `지금, 여러분 차례` 与 L129 说明句均为 `여러분`；`당신` 仅见于 G-4 标题本身 | 标题 `당신은요?` → `여러분은요?`；说明 `여러분은요? …` 不动 |

### 8.2 G-1 说明（ru-en）：任务箭头字面 `родина = родной город` 未照抄

- 任务原文：`родина home town` → `родина = родной город`（括号：родина 是故乡/祖国，hometown 应为 родной город）。
- `родной город` 是俄语“家乡（城镇）”本身，不是英语。英文版词汇注全行皆为英语（`поздравить to congratulate · … · повод occasion`），把俄语词填进英文注会让英语读者无从理解；且其余 9 版均以读者语注为“故乡/祖国”（de `Heimat`、fr `pays natal`、es `tierra natal`、it/pt `terra natale`、nl `geboortestreek`、ja `故郷`、ko `고향`、zh-tw `故鄉`、core `故乡`）。
- 故按任务括号的本意执行：`родина home town` → `родина homeland`（`content12.py:176`）。“home town”对应的俄语词正是 `родной город`——这正是原注错把两个词混为一谈的证据。
- 若协调员坚持要字面 `родина = родной город` 进英文注，请明示，我重做。

### 8.3 G-3 key 126 不动（ru-de）：已核实为整句译文

- `content8.py:43`（text.md L616/L812）：`Die Wettervorhersage: Regen mit Schneeregen` 是 Q126「Что обещают синоптики？A. Жаркое лето · B. Дождь с мокрым снегом · C. Устойчивый снег」的整句答案说明（“天气预报：雨夹雪”），不是单词注释。
- 佐证：其余 9 版 key 126 同样是整句意译（en `Forecasters say: rain with wet snow`、fr `Selon la météo : pluie et neige mouillée`、it `Secondo i meteorologi: pioggia con neve bagnata`、nl `Volgens de meteorologen: regen met natte sneeuw`、es/ja/ko/zh-tw/core 同式），其中各版用的都是该版的惯用天气短语，而非词表定义式。
- 只改词表/小结处的单词注释：`content7.py:18` bridge `мокрый снег Schneeregen` → `мокрый снег = nasser Schnee`，与本版 L170/L515/L691/L786 四处一致。key 126 两处（L616/L812）不动。

### 8.4 观察到、未修（超出本次核实的 6 项范围，留协调员裁定）

- ru-pt 除 L125/L129/L471 外仍有 você 式残留：P1 注 `Leia a primeira página e escolha a resposta certa`（`content12.py:149`）、`Complete a forma verbal ou o caso correto` / `Complete com o tempo correto do verbo entre parênteses`（`content34.py:74,238`）、`Forme frases corretas com as palavras`（`content34.py:88`、`content56.py:88`）、`Junte as duas frases numa só`（`content56.py:191`）。与本版 tu 主导不一致，但不在 PROOF-NOTE-2 的 6 项内，本次未动。
- ru-nl 词表 `Dooi`（`content12.py:218`，text.md L141）同样首字母大写，与 `natte sneeuw / gladheid op de weg` 小写不一致；PROOF-NOTE-2 称 `IJzel` 为“唯一大写项”与盘上事实不符（`Dooi` 亦大写；印 PDF P2 文字层 `Dooi` 1 处、`IJzel` 1 处）。本次只按任务修 `IJzel` → `ijzel`；`Dooi` 是否同改留协调员裁定（另：en/fr 词表第 1、3 项亦大写——`Thaw, warmer weather / Freezing rain`、`Redoux / Pluie verglaçante`——属跨版同式，`Dooi` 可能系有意句首大写体例）。

### 8.5 逐版修复记录（待填：改前/改后印/网/text.md 尺寸+SHA 前 12、SVG 变动页、text.md 最终 diff 行数）

（见 round2-summary.txt；en 已完成，余 7 版待驱动完成。）
