# nl-es proof1 handoff — coordinator follow-up 2026-11-11 12:45 EST

## 1. Q140 漏译 `corto` (es D6) — 来源已核查，已修，待建后复验

- **键的来源：核心**。键 `Ik maak een surprise met een gedicht.` 出自 core-nl `content8.py:75`，
  fan-out 逐字复制核心荷兰语键（只译解释层），不是版翻译表所生。核心源句
  `我做一个带小诗的伪装礼物。→ ___` 本身就含 小诗，键漏了它——缺陷源头在核心。
- **es 已修（apply_fixes.py，建前已验）**：`content8.py:75-76` 键 →
  `Ik maak een surprise met een kort gedicht.`，注 → `surprise: expresión fija; corto = kort`；
  源句 `Hago una sorpresa con un poema corto. → ___` 不动。es 建后复验：P8 答案 140 + text.md。
  p8 compare 门：翻译题 137–140 属 legitimately re-aim，免于与核心键比对，改键不破门。
- **同类不匹配另有 6 版（键漏了源句里的限定词），按协调员令只修 es、其余 9 版按原简报不动，
  仅记录供协调员定夺**（核心键加 `kort` 一次可全修 7 版，属核心级修补，需另行派单）：
  - en：源句 `... with a little poem.`，键无 kort —— 不匹配
  - fr：源句 `... avec un petit poème.`，键无 kort —— 不匹配
  - ja：源句 `小さな詩つきのプレゼント…`，键无 kort —— 不匹配
  - ko：源句 `작은 시가 담긴…`，键无 kort —— 不匹配
  - pt：源句 `... com um poema curto.`，键无 kort —— 不匹配
  - zh-tw：源句 `我做一個帶小詩的偽裝禮物。`，键无 kort —— 不匹配（与核心同文，逐字继承）
  - de：源句 `... mit einem Gedicht.` 无限定词，键匹配 —— 无缺陷
  - it：源句 `... con una poesia.` 无限定词，键匹配 —— 无缺陷
  - ru：源句 `... со стихотворением.` 无限定词，键匹配 —— 无缺陷

## 2. es D1/D2 框标题 — 已缩短，建后复量

- P6 `VOOR OF TEGEN?　¿A FAVOR O EN CONTRA?` (+47.8) → `¿SÍ O NO?`（PIL 预量 +103.5）
- P7 `HET WOORD　PALABRA DE LA SEMANA` (+34.0) → `PALABRA SEMANAL`（PIL 预量 +21.5）
- es 建后由 check_one.py 从建成 SVG 实测 ink clearance；仍超则再缩短（只删词不加词，保持原意）。

## 3. O1 裁决（不改）

- Q78 `Zij ___ (maken)` 键 `gaat maken`：单数 zij 为练习常规读法，键可辩护；不改题干、不改键。
  接受单数 zij 约定。es content8.py 未动 Q78。
